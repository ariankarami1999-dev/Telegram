<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/r3LpllfWVpwHykhgQ7_c-vmXeO-NEVKYHUcQb3Z4cxQ6BKZkxd6p8nqQjA5EuQZx-bQXmwq6cEyjW8J91TE8L3SE69QvUwofW4-qwymJWE4_DRQvTGyDSEcvXsgJs_WU9p5qlzxpaa-tbWWAJev-NJEmA9hMJ9YKB4qg9XtMV627tu4wNao6mR_RLxfddtopoIIa-m-516oZ2R5Xx0p99fPmqjx2Lf5khQfH4wFQgs8busQJPjsbOani6rA5y1_JwlwLy6WfQtduvZ4N3rPiYNHggnHaH9gnjm6uZNs-WpF5j9kuwLWZdp-At0Q8rmLFILTW0hZyWU9GBgI_A6RVIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 10:42:50</div>
<hr>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRMGjR_kUKZw5WQQVNdhkE4kdvWUBddcFTmeYacXXlQY5hLqYnaBWif_KFM1dBbAmJXangMEGrmuH0jKXm-L5YLqY_pyEzvV7RgRupCB1xG20vZHBkYlf9YQnC5AfztEsWAsHxh85dvMRgNb9FXN3yzBhdOf6g_2rVsBXPXQRaoaw6tnm3AnSE9v_OEgS29MfBMjmxOBHbs9MpuDLw8gsx-TU-ehGE6tIiI1hEmNvQhujfaXe_EObGgQr3cfEZn2VytHEuTG_qB60fULSpHbcfLMPI3Nl9k6wN2V1O-x2Lj7Inl8girEmUQB5YRDGTAqc6fSEC31NJlvy7j1ZndjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIinY0MFaAW6k6z2K3hUb0170UpuB2heigF5UcSdeuS91zQJ5vy1GubbRec2t-dvqz_jKK4Qm4tmjSs9x6x6lzsJIhnTw8Fk_bHjWJPhNH4x4Oi5LjugAiWnjCj2SHyr3k0ah2QYyhWysAica4RerzIkeP1l4rw5sar9hEWnjCkP3iElB38-lorz5xlaRsyyrbyC131O0D9I6NY_cmVtCmkX-WQkSaqlYsu1o1xo8gitEj9A6LaTEebeMXX3VBWgyiqTcZzLAZHa-Dzbdsxp6pBmECf5f6qAwfewWsKdnbkq5t6fZ4chpgkHzVyAFfMyQKcsgoT5JIcFDZDN6N5IsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRJPVLvahshFW0k6cQc419bTwku_x39NwS7WiGVBNSSnpozd2yn0VvhVte2Ipg5wmBqco4gJeOGfE-f4L5G__XrTrnkVyWM6l2TLPCbR0eeFdv7xfC_N5klzYXoiz-MKlq2o-LjwAzVdZQ8qYnggblArunLF3tfF2WgZxFBdlFRv98BiJq6OJcmmZ31tetKHDtOneBa7qaAKf-BCJLDftAtP2XUHlpaEwvvKJHeUoENbfJLQr43BTg_TqW8eMeSUOd96x-Qu2jriqLOO6r6AmA7-OsdfndoHCqgWJBEJP5xq5ydWICBI52ltCgNnmo5Jw9efDx8nuEk628Coj91SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIYhK15Sh0cGS91laW-EHNkwXJ1erUyknj2kwnWuYQEnWK8Ra6bD5C4JWBbpZhG6G5N92AdhONmky-ExHQAM3nDvLeU8cw_j4hg1GONC33pEVwyjHIWvcs0MjRtCBDTNItnTnei590jAQeTHI-B2qtDZ_TansdeD7FCTBMCcpXn0dHHvJCMPitgdUJPxBw7uFC-6gI7IEzgcWXIUsWEe7uAXnfUL7HrnZ0QTGY8W8ORvusgJ6onnHxRNH-VjziZgQ6xdGuaQvnn4Yl-1dbw7ysf89H_hXckK3KW4jd-72JbVem_0rYPxGiyugZp6kuN4M0Ci_RZWhTesaXemaAebPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kk6UzVHiJ5a-wdt0SySHcSrQ8Y-4lxQVZTO6H2iQzaRkCpqU-5HA65T3835alxbJElUi4teeWwwuGK--Uaj-E9VTOP_3YcZWEVx1Zb8ugOZ01F4MUCqjLb5ZSgcGH823Pj7GN_aQS_4_6MZ6wKoymD_gRN-Lz6DcdJkbBoTPNfpbeRpA30GGt5fGqzAHyLQiakSlhzVQWVk_y7sBwpe5c5zAkXKZ-9F471rtEgj-oMnS0fPeHQyH0TzCT1wcyemKXXq5yeL0mzki0WjVLkBsBUc7ZPpUZM6fSWI22_grsYvtYQYWnrrthHcwJp37YPKhnRVsVLTdjpx3K6JOKSkw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3Qj3kf-JJzINr17Bd4aFUCxfE4RNS74s08-2sj1vTt1Y68KO7rkOl8bv5Nzr6Dxpy-VSDZqbC-OgtuwHMXozZsPT7b3O-1gIW4parsuZEEjsYqAx6nrAQFNYpoyX19IC4psoqsnlqurvaZxOF7YRdd63iLoPo0N1BY6lFHScmTesRFSIgicaurVD0fJufELkf32dI5wuk03y_Ezw88HG90GhfPHercRsaInDzNgSuDYEF6VanyYR31UU74SA2PqN4sRfq9kzt07ZSWG-01uj_UEuq4NE5e-toJ1_WHK5g0cxBxflg3z5WOik3uG6GNQoRzm9ZLe02dTJzDPSgM0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgSKtERFlk7GeVHmOibaVa04Ek_gRAxDA09ET419nXzjgZnndD1_lSPx5vI7X0iA1bkJGuPSXaaBDoRMbh2bGf89RenuHNDrBXrYeu3whlkmTpYTXCls9Cs-2NyKW6P_2ijn2BFI3QCQ7XEREsy0WVKHR2lIVdLZviMzo5tGiIRyV5QHpjvMaupkOTwKai5wLr2Qi5zuA66CKfj9Oz2J2i2fRAKuNOjnHT6BPD6kA2b_45gaauXjUXBFF0jtSnOQyUwo0AgQUie6K4EExUKLEh79O6p3K83gsooTPwv1VDQ2fX5jPQmmbouBLU9jssIYCrGiPYFH14j3DSFiLNlXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBdeWNzf9v2czF2d-w4ILsENvZZaBY7oYT7T3MW_SMR-9JwcyjEJfHkUQh801LPyYGwrbOs1oSwAzKxmR5OJZdnUbp21v8rMaOV5_XH-JE2zpG-okI297oV1HBmQp6Nyav32Ts8LRUsXD3b3QN_w2nRTbRYSUUT_uyrfhAz4lXK9aSz2OdpjJcYYROp1ffwmO8kIe31DNn6Y9xaVDmbulXfBV942xlTxfhe7NhPVxyFEfxG1lZBsRj0AuuBXUN3Keex-qz1MruXuVHthv9HEC7-DbCkKAMOg57jVMRIbx2Gjlwn-JI6OWqYoGnQDzjoVWqezF3qjWNzoDPc0mcM_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=lDMnEdWbs3c0oCu3qJj0Ri4zry2IpEYAPONWLmiOn6aaljy8GGCgH6ysrralDxt0RZhj7uwV8_Mw2ZgylnEbvetl8mxO3m_8fSY5q6472QijcH7KOrHjmy6aRJt6SzibGsVjjCC9B1Tc6MaloSW9oiKFTLcP4-GLMnSRjZnYNIReoclccIzckaWassZlDNJ0ZZeBoN-0H-g5slm1DzVoc-rV3ELvSvI5a1aKOY0bUhgd6s2iPUh5dc5qeiLH_MwFEwnInl5qS1eqjqan7eOJbXmsm9ArKAKJmo9hnxk8efSs7zs4pAeLeKY3soHzY7DYP8di8ZepK9W4Ni3rgTvTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=lDMnEdWbs3c0oCu3qJj0Ri4zry2IpEYAPONWLmiOn6aaljy8GGCgH6ysrralDxt0RZhj7uwV8_Mw2ZgylnEbvetl8mxO3m_8fSY5q6472QijcH7KOrHjmy6aRJt6SzibGsVjjCC9B1Tc6MaloSW9oiKFTLcP4-GLMnSRjZnYNIReoclccIzckaWassZlDNJ0ZZeBoN-0H-g5slm1DzVoc-rV3ELvSvI5a1aKOY0bUhgd6s2iPUh5dc5qeiLH_MwFEwnInl5qS1eqjqan7eOJbXmsm9ArKAKJmo9hnxk8efSs7zs4pAeLeKY3soHzY7DYP8di8ZepK9W4Ni3rgTvTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgq5-bj90lOJ3EZOrEqyh25aVxF6nFKyIg7DJh9WYa3gNmh3eBkTa6jhQrq3mXJOHJMkx9st-q0sfnPwC0MigaeGEcMI6zj4Tz53rCOASxLXSCdFpK9KRUo9m6Ux-71fWfSGe34nvy5ZAXATURUiScrGPXFX54TA5_q3D4sEL6EjR3-1CnjB2HCAVx07zqfVQaajNFHXXNB-wjYuztOAokw-V0XswRrNCxkdJN1tpwZKmtsDzwbmoYjrJskysJtDcCrC-thGD8d2_wpzQDBalA2CHK-NZjpBM48wA-5uacfNbdcTeMYfnBRumXpNSSrdvg3sIeNlwUYndp3mmQSWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=OOB1Dn50w4GsobTpwCHE_bV0u3Xn6-UGNBEFLqHotj5Lyeps9OiP__nJaHlb4hjhwnphRcdHonRXdL6R9weeHE-sjjRSjjGb8oEKRBysdUf5Uvrlo6T5wGBLy6Q394hyKgfq2ta9TqcakqrXPTrQsgxDnRxy6xDZ-v6jB9_JYaHd0NPnpueUs0vx_s2Q6cNjv680_oWY0ya8wm0mlVv-fP6PUhTAwWnMiYGJJqmF3b2mQn0k_ObgBdNAV2Pc0g3QdF4SF_z2rgZ3VS7qEeNIlJvbyvUFAptc99zv9X_owPCWoKYd5HqSQ_9sUpqobFSGFDZx354gWG2teC8V6nBfew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=OOB1Dn50w4GsobTpwCHE_bV0u3Xn6-UGNBEFLqHotj5Lyeps9OiP__nJaHlb4hjhwnphRcdHonRXdL6R9weeHE-sjjRSjjGb8oEKRBysdUf5Uvrlo6T5wGBLy6Q394hyKgfq2ta9TqcakqrXPTrQsgxDnRxy6xDZ-v6jB9_JYaHd0NPnpueUs0vx_s2Q6cNjv680_oWY0ya8wm0mlVv-fP6PUhTAwWnMiYGJJqmF3b2mQn0k_ObgBdNAV2Pc0g3QdF4SF_z2rgZ3VS7qEeNIlJvbyvUFAptc99zv9X_owPCWoKYd5HqSQ_9sUpqobFSGFDZx354gWG2teC8V6nBfew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=N55dWWRotSbpoEjWX6mYCd2gSjmSSqBdAt3kDW-XyjPyQfgSoJERTouzuwnLO0gDZigppBzalz3hcbyDYCHmdb9mu09X0BSq8rmwUZGw7EwZoCBEzsWGAQAamBBrexQnxjPI2xtT1Xa-By5Ju7h56sGFJQG9ifUMPhP4LcG0v-tSeTha5rZVyyImh_BVCe7dLE3vdtgDBENEPf3EN3GUmtLrWKAgaPAlUvAgChqH_PqScVSltq6As84gMxqdX188KhL0aYw7RPVuQ_Uj7nDTlYFBi43wtdyeEwrak-k8mIY-kEyfQyxnp1CGZzecD8w2O2BFcL-fUfCy9_1yzWrD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=N55dWWRotSbpoEjWX6mYCd2gSjmSSqBdAt3kDW-XyjPyQfgSoJERTouzuwnLO0gDZigppBzalz3hcbyDYCHmdb9mu09X0BSq8rmwUZGw7EwZoCBEzsWGAQAamBBrexQnxjPI2xtT1Xa-By5Ju7h56sGFJQG9ifUMPhP4LcG0v-tSeTha5rZVyyImh_BVCe7dLE3vdtgDBENEPf3EN3GUmtLrWKAgaPAlUvAgChqH_PqScVSltq6As84gMxqdX188KhL0aYw7RPVuQ_Uj7nDTlYFBi43wtdyeEwrak-k8mIY-kEyfQyxnp1CGZzecD8w2O2BFcL-fUfCy9_1yzWrD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z14DqUyzcDLMh8ROn6n-yBOv8MaR1Se43nWVZ8FhzWfOtRLwGP8APzHGIazEDHKlqOY-flR4SbKb9l8gJ9EE-756Y9135rGhYPtvvOjgW3lhYUr1lxieB0pZaSCpojDX6SAUr2lKV_MW2zEO2VS6MD0B3weX9LzBq0iTFHmW3WblJa-kviI2tciKRisr4mEd8kTbvztC9_M6RDgh99nXZnR0olbwkw0E3VOTl0bsqTO4BPdWRsBN5EeS2TvuYM2snjUIv6OvJDjzNWeTcJvFyA1_sDDtOFExCH_njdde27USsc1BgPECfXm4PIBixP2h7z1_hGOkBCScSTozgPYZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=nTQ6X7_GjFCnizdx8V8F6mj3N07uha1B7benIhZ0wWwY5Rk3DTHcckpbx2EmNBWdv3KA959uigciTguWGS-OIdV6cyGSnDtI2J-THoS7yISivHCcK38D_4M45cLfLGwLvs2ieV88ZwfUOrLR777xt74lmCE9OIE7K-cYTA_qPnXuThoxXSxxM0BTGhWEdrQI2mh5lSsxcwhMBRZKH0Q1y7j3-NvE-kd67zl0_DezR1q6BTUTWyYlcdr1QtaceorqmICmcQkPqU5LCVyQcse2MEEp_fIXeSnSIgc2-OQTQJUo2UTSiswlBcQIk9JZ6UxiRkw70rMaY6vOXNeK5pM1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=nTQ6X7_GjFCnizdx8V8F6mj3N07uha1B7benIhZ0wWwY5Rk3DTHcckpbx2EmNBWdv3KA959uigciTguWGS-OIdV6cyGSnDtI2J-THoS7yISivHCcK38D_4M45cLfLGwLvs2ieV88ZwfUOrLR777xt74lmCE9OIE7K-cYTA_qPnXuThoxXSxxM0BTGhWEdrQI2mh5lSsxcwhMBRZKH0Q1y7j3-NvE-kd67zl0_DezR1q6BTUTWyYlcdr1QtaceorqmICmcQkPqU5LCVyQcse2MEEp_fIXeSnSIgc2-OQTQJUo2UTSiswlBcQIk9JZ6UxiRkw70rMaY6vOXNeK5pM1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adRz3-2w6mQiiUOo08V7YSgkVAHlQHYiLZ4VNw0VGEPyi31OxK4m_NegFPGCor1mhENBjjDhhpkK1m1FEI-ujToZnz0LWIJ3uheyOH_FtMzt4vw25vtPr9JfO6IOnyYalOqakQ1IM9IZfYPhZev5nbhSvfDg7YCT6w3phHifqnFEDKfdBtqOCN3ajD-vdH0NZhy2hspPI_s1u42UDJWsWBU8sFotrZaNlh-xmCMtEEYylenVUwok4LCao1S-p_Vxv7PJyapHjRlto-WfyWzfJ1pJGJM9y9xd1SbJmH1HqGBHJdAVKdXVgvgt3h6q4WboVkT2L-PKk4n-wvxoW-xAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTiHHa-YXTxQSSorFKHxNGavcGKzlqJfvcr5zRlQz5KMYU9NsAC1rRDHqhx3lmpa67xR_uRLyFMp9vy8FoMXM38-KdBguvomctElUwmqtsGuXs435GJvlfHyqaaJxuhxlYbGTWwk_xNeu0erW9TtNAXrAYdeN1wE0Q4XsPMEploQIiJI7lZDAa4PysDUGBpSpi68uhuSGnz-ICmx5BdMIaoa-fd1dZcdy9uwe0ssTB9LrsmEg7pxV67v9GA3c6ovWLWqETqYdlqXelblB7uZUj4e1mWW6pByHn1giDEn-dcu_2oRbjaQ0VKa68npnrgk_f5mHq2MHY_awa64no48Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ny3N2XICRYSTeBiAK8PuxunFztcSWS3cRUDBmfOkq2kxKkmjkENQPxOY1kAnqnT60hUDr5gm24zKQWUFFIK-rK6kGiEgGL2E9cmEsfK8YOjkOXUpazW7RbmzIS186CZHwd1reI2HdfO2KQ65rryx89QaL50CV7vns1mTOQ0aMtXk5MxXOC0ermuofA2e2_82AwW2bRUESNq_gojahg1MVFOLbvMEy2wc4wwuD7rGxfdyU8pOfIHSuJYJ9-1y3Pd1mDgpial4RcRh9qdTW5xQ9cRZKnUseqLq2sf3j2PtcNo_G1D64Ab8HEE0tdyULTld4RkzYsxN3-AMUUdq4e1xSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaVKimUARwhJJSHppwVFUaMLpxaUdCCupis_w7VExft6ekgRzJkDz0ofdtc3zzRzKal6OCINQQ95TtsmMrPYs7DnmuJr4RSzGwnY4d9s0sMY1ys42tJTOGRLAEM8KsspqTm4y7ZX2XDcLAZaUrVrxPIyhYThyx_nYdL9oT_4ctoB46eWiVTQfSyxfgPhbDrJ-dl5nc5796kGz17WhIpuV9afwHzGegyFjttQJeqreNgHpWwUKbOCvtvvCOKti7067zQJaFFLjTtZU7PfZpYqoSAd_jKz00KPu8GmjsgWfY9uPFty8ws19YsLsqAI1nLJuqHUHTC1ubPNsWAiSS8Q5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=DAi5AhU49LiBuDL4nwGtXianAfDKDGg6AN7kQF49P0KOdIZ69p37NakBq9aJKtS8G3-pMC3Wo81lfKaSIym3jH-M5_BIDzeQlnhh6q3ScCAhYB3mbM84OWbsvhALPFy8URTmJnTK0WHMxb9M3Qf33x2Gl-2Eyss2cmfJmBU5b4RuZBOljroSAvPMwsOn0SuKUY98ykOi72nvm3RxQL0YbYwEmc7tT5o9DTLmmX1SMSyBhUaCMM1A3aZwsAAjj85en2R1RQxRIbGWWESocghlb7MyoRlYHKYyuBgvWw-n1-EnmDDGbx-IG4Pve8tWR0xrB_aNScg6npr9LLNkZHputA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=DAi5AhU49LiBuDL4nwGtXianAfDKDGg6AN7kQF49P0KOdIZ69p37NakBq9aJKtS8G3-pMC3Wo81lfKaSIym3jH-M5_BIDzeQlnhh6q3ScCAhYB3mbM84OWbsvhALPFy8URTmJnTK0WHMxb9M3Qf33x2Gl-2Eyss2cmfJmBU5b4RuZBOljroSAvPMwsOn0SuKUY98ykOi72nvm3RxQL0YbYwEmc7tT5o9DTLmmX1SMSyBhUaCMM1A3aZwsAAjj85en2R1RQxRIbGWWESocghlb7MyoRlYHKYyuBgvWw-n1-EnmDDGbx-IG4Pve8tWR0xrB_aNScg6npr9LLNkZHputA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=EaW2KNRipLDNRKpD_Slb-nxyQvJnggPrvww1Im-YqZz7QGGG3F76lPwa-owwKvfxEyFynkOI21f7lZv8BpLV5WCM59eYjrVqyB397XERjKOKoKscZvYzrxmA_oFYfy_P40rytDJVz5oxD9d3UHB27qDc-Mta2lQJWywYO_beC7fYPAM9wyt7UpLoHg8PI7QbEs1prqolhQzBNgBmciyL29XXhXoM2wiNQz8tSMK1awJ9iy1GTGYKImiWGfitydpfIvD96LllIi2aXqg_fOOOfpJxybGo6R4nfITWk3UxT2XV7AFlzMN1u0reeIbkYdNzSibN09LTaqvZIMMvzRCfZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=EaW2KNRipLDNRKpD_Slb-nxyQvJnggPrvww1Im-YqZz7QGGG3F76lPwa-owwKvfxEyFynkOI21f7lZv8BpLV5WCM59eYjrVqyB397XERjKOKoKscZvYzrxmA_oFYfy_P40rytDJVz5oxD9d3UHB27qDc-Mta2lQJWywYO_beC7fYPAM9wyt7UpLoHg8PI7QbEs1prqolhQzBNgBmciyL29XXhXoM2wiNQz8tSMK1awJ9iy1GTGYKImiWGfitydpfIvD96LllIi2aXqg_fOOOfpJxybGo6R4nfITWk3UxT2XV7AFlzMN1u0reeIbkYdNzSibN09LTaqvZIMMvzRCfZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=FgYvYwm3BvO_zuOW_Cg5XlYVXWTWTgHgaQg--zIWuqm21LZuK_Pxp-OkHyAUxDeCf25B5PWTT2CHcc-NpkZYfswNuBXMXRbxkSJb_2W7mHDZ8_Y95zy8qPiufbLvkpZF4c6f7cdovSS7L5s-i4M-w9pJAUh3AA2MCezb6ar5jqWvby_c_GKPiWLRvgPt5qMKPFyIkg_WeaN8FB4sIW3bwjKQnbyLB2h4dHFSKRh0zPqhAnKXIv2iwateAJKft_LzUeWKO2YXmEY0uberBdlHknIoCAsllda61KQ2n7T6ZkxMcvbvPgeo4bV-h9Q1te65HH3mMnKRomSkjJnLML0Itw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=FgYvYwm3BvO_zuOW_Cg5XlYVXWTWTgHgaQg--zIWuqm21LZuK_Pxp-OkHyAUxDeCf25B5PWTT2CHcc-NpkZYfswNuBXMXRbxkSJb_2W7mHDZ8_Y95zy8qPiufbLvkpZF4c6f7cdovSS7L5s-i4M-w9pJAUh3AA2MCezb6ar5jqWvby_c_GKPiWLRvgPt5qMKPFyIkg_WeaN8FB4sIW3bwjKQnbyLB2h4dHFSKRh0zPqhAnKXIv2iwateAJKft_LzUeWKO2YXmEY0uberBdlHknIoCAsllda61KQ2n7T6ZkxMcvbvPgeo4bV-h9Q1te65HH3mMnKRomSkjJnLML0Itw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=bdJqsLO43u0FJvJvky1iVzpUzUDSx5vGCg-pBIXRGr5yLAn_QE2XbOxPrIo_K_Mo3s6Ln0a7E5C_Wo6LPnmhx95FSmPPZdIYY8bZucfC-34TBxtoV5hbuf6rgqTeVuvNm9RTN1XvIbo7yekKcH6ztcHi6v9BsXkGKjdJVvtny7lsdmIdjJUm-5l4por6FDh3IvslzI45fM98XzJf4e5-6o6SUfpAjRbSEcYNkAHw-SFUUBldJx94uAX4li7VsYCxFh-27uHOeb-7NW1k7TAkrFImloXM4Vm7f0WOVIAlCvJkTzXH9DjAYbArqxMb5GRs7Q9evuflU1-HUK4tP2oiW39E8XZADtHbEATY31LtlwgvEXMDIxZY5xnLxICuMmcL9TNk2dI5hT-MWUsxwBHBM4UUUXLwytgiI5VYcbQJXJhvnyQ_P3JHzELTpmtXYIuF1tJd9JMJKxK3JliSC-STU1Td4ah2ztHJmzR7LhV4IOQXRzYEC3O-5VFfRjx-6ClSCm78QrSwhAuqP3LDhaYv9WW2acDBvr7q9HJbUGwE5Ss5_HBCgMRPiWbvk6kaiFve141mzFDUWdj7UNxY_YQ2q75SeSkPc7kdiG36I6dOr0zv_LbTrRDGPUujhhuy2p1Ekun9d3JdFPHNs5pul4ZBKIWrdfxTGAKIs2vZ-jaRV4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=bdJqsLO43u0FJvJvky1iVzpUzUDSx5vGCg-pBIXRGr5yLAn_QE2XbOxPrIo_K_Mo3s6Ln0a7E5C_Wo6LPnmhx95FSmPPZdIYY8bZucfC-34TBxtoV5hbuf6rgqTeVuvNm9RTN1XvIbo7yekKcH6ztcHi6v9BsXkGKjdJVvtny7lsdmIdjJUm-5l4por6FDh3IvslzI45fM98XzJf4e5-6o6SUfpAjRbSEcYNkAHw-SFUUBldJx94uAX4li7VsYCxFh-27uHOeb-7NW1k7TAkrFImloXM4Vm7f0WOVIAlCvJkTzXH9DjAYbArqxMb5GRs7Q9evuflU1-HUK4tP2oiW39E8XZADtHbEATY31LtlwgvEXMDIxZY5xnLxICuMmcL9TNk2dI5hT-MWUsxwBHBM4UUUXLwytgiI5VYcbQJXJhvnyQ_P3JHzELTpmtXYIuF1tJd9JMJKxK3JliSC-STU1Td4ah2ztHJmzR7LhV4IOQXRzYEC3O-5VFfRjx-6ClSCm78QrSwhAuqP3LDhaYv9WW2acDBvr7q9HJbUGwE5Ss5_HBCgMRPiWbvk6kaiFve141mzFDUWdj7UNxY_YQ2q75SeSkPc7kdiG36I6dOr0zv_LbTrRDGPUujhhuy2p1Ekun9d3JdFPHNs5pul4ZBKIWrdfxTGAKIs2vZ-jaRV4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=F4tvutgfv1Jap5BM-BT64rQbcCqUq-WX-DayfhpUlDM89fndaCBC33y8EnzC_mGoSgtGJB7pXUnxLGMTnHI4HzBjQXCIsE_ApBivM7KG4eodrb79vUH4ED5qZ8LoDnyfLbRZ916Mj6bem4JZulfS1zmQdKNArnoWkr8LS87OGoSXSopsks0NCtmwx_OWpW8XtJhky95lsVw1wTKQ_UToNMh01h4T9L4rY4etpdjtHUmALglhEZ61z2ebwlIEOEy3Uc6JG8vnqH_VhdTzbJkrBFhuOFT3IlhXyJ6vWEQMCA4OjJMa3wOKBZOAudvXvS0abxpbg7qu63A9xay9OsTLgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=F4tvutgfv1Jap5BM-BT64rQbcCqUq-WX-DayfhpUlDM89fndaCBC33y8EnzC_mGoSgtGJB7pXUnxLGMTnHI4HzBjQXCIsE_ApBivM7KG4eodrb79vUH4ED5qZ8LoDnyfLbRZ916Mj6bem4JZulfS1zmQdKNArnoWkr8LS87OGoSXSopsks0NCtmwx_OWpW8XtJhky95lsVw1wTKQ_UToNMh01h4T9L4rY4etpdjtHUmALglhEZ61z2ebwlIEOEy3Uc6JG8vnqH_VhdTzbJkrBFhuOFT3IlhXyJ6vWEQMCA4OjJMa3wOKBZOAudvXvS0abxpbg7qu63A9xay9OsTLgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=ad6L7UL_RN3HiImu9qsUQzaej_K1MmsNQsGc3KmteONo5OyZgGJ_eK3aoZpfwszxGfIMQ7-3MzJQhquJBq4EaW-xx-leAk-rRhgc7k3Xibj4aXzbSc2Cir8ZnBbKjEMeG4btma44C_EjfNjTzM0MjiyQ1jn78mmq1loQNmwmWEkFZXWJoTl7DTy3mN1VGo6tXMpwODksnH94AHfcl4JCx9_YP1eXH6EQi3dPaGO3HbfCPE7E9GMNeMwbSZisLaCBnZyDRs2ImJq3z6hWelN5yIT7TZk79W0YCCn9sVLyC7SOHd6f-qkXf3DRr0BkBXCorLikNLhnORL3GyeejOaIxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=ad6L7UL_RN3HiImu9qsUQzaej_K1MmsNQsGc3KmteONo5OyZgGJ_eK3aoZpfwszxGfIMQ7-3MzJQhquJBq4EaW-xx-leAk-rRhgc7k3Xibj4aXzbSc2Cir8ZnBbKjEMeG4btma44C_EjfNjTzM0MjiyQ1jn78mmq1loQNmwmWEkFZXWJoTl7DTy3mN1VGo6tXMpwODksnH94AHfcl4JCx9_YP1eXH6EQi3dPaGO3HbfCPE7E9GMNeMwbSZisLaCBnZyDRs2ImJq3z6hWelN5yIT7TZk79W0YCCn9sVLyC7SOHd6f-qkXf3DRr0BkBXCorLikNLhnORL3GyeejOaIxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ew1hjIZLgIm6oWxvk0zc0q52samrWCTm4keh9yUvqNBKyqkorKk-fj5kV8APmHzIKrjChhSzsG8QqeoVfdh59JSccyTU3FVAAEXG6CnYF5DzhTGeisGXAjcff2mPaJWgAIbJYxME3mbrxE-ylfUONq878oFBIsRNK5Qnz1l-u8GOxLA7iGPB2EGUO215yrVoXTg1tavxFzSe1lzQ6BGURJkNp-No9y5tZdbJlMrOTrh_cBOeqWUA_XFtyfaJPO1ptIBhy2Y2aWVTcdLHb0YtCVsfIgb_KKcObTWFqgBbi_XCneAVBTZ5pGrNp8__ssTRPecZM1EBrVNrlWqBxMYAaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=wAm6Q0Dh57xU71un8O4iq-XevZ0LuWjI8up56xX39hvzXW0D2QdC71wfZMDORfuqS_Wl8O9OKdBh2NulTSimi19G3dcfYCHWcZhGtWCzvgPDXQ0fNvIMXaRkkca6-ERaVQ_4HUZdTDkSAiVfvn-NP_o7FsJ_VRI_w80UQRwusvzThMGYW7jCnkYLmPOW7qb7zr4Cl5xWoy8DmOxNHC6G_HjNTZmpUBZv8IhbJ66c8mf4wbujZqqViBg03t2p3t2OFtrSHuf8DtmOPxaf1QxgppURuElu1utJT2htOROzTSdmWCsVYgdH44NT6F40D47u6BNuQF2FeID_vEc9bKtXbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=wAm6Q0Dh57xU71un8O4iq-XevZ0LuWjI8up56xX39hvzXW0D2QdC71wfZMDORfuqS_Wl8O9OKdBh2NulTSimi19G3dcfYCHWcZhGtWCzvgPDXQ0fNvIMXaRkkca6-ERaVQ_4HUZdTDkSAiVfvn-NP_o7FsJ_VRI_w80UQRwusvzThMGYW7jCnkYLmPOW7qb7zr4Cl5xWoy8DmOxNHC6G_HjNTZmpUBZv8IhbJ66c8mf4wbujZqqViBg03t2p3t2OFtrSHuf8DtmOPxaf1QxgppURuElu1utJT2htOROzTSdmWCsVYgdH44NT6F40D47u6BNuQF2FeID_vEc9bKtXbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQFNjHrCXZPsIJw8dIkiQmvAmYFwHz4ZsOF5UI2BZyhRrUlwc0B2PBmMx0Vfmf7KjB6KCZSLhIz46rgcCve_LwMt4oJGoeIFymNuw9bzfaFeuzTIKZHxbnjCjh07SOEWhoQkiDrxI-92uIJpBdmCmAnwBhPZGhTwv42Ic2GIFAgVZ9ASlDN4yDMLgv37blIAxVuPxnIS3aSUpdxfIgDXV-c-ux6KiW1rQYmqowS-B8VsDhVkUxr97K7I9odFdHwniWXg9QjI7TGK_aPHnkJMrwrZaap4TGMA7sMfel3t0YM3ifQ0XJBDSw3lssuqPv-TVKEjo3L8r56bGfkEFVBy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxdowNqAccOeONSpAv2RR_Y4BYOhDV2S8wT53uIZT-87U16p8xDK_Eg_qzjMA7K0QT5PNWD5fEhNjjKWsRF6tmobzBq9-q_zVgIkmSPQ3Fjy7Xz6IrK03BHq0yEGgfh_lMpxQB9QsFhy9ks0ZGJ9xhQKu7SZlli_CY0J2OnatHzW8_ib6M96Os_iBzwzTPdllGvPGi8PKdytt8UHGIoEFeFH118oVC8w2YFXdn4cV9u-YhaReeHBIjOWQU-j91jYxoMtCuyrXzyAy0Bn9-Ijww1CAT9BEzN0QBrT1_4d_zp-tVewfAz7Z14jEhZgcVIAuIqRlyshbt4uO8lbezKKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=P2PB-fK4zODcAupCsuSl5pbDhy2ehCGa-3Wn3KwlY6VGDMUe07ToNxK6N8wsyJaAcAuCgjRmcOi4xwDNZNV-GBvK2IVw7v8hQwBA6NDJqpLPusTbx_PER2E0TX83L4ZaSZZly84LmZq8aMcOLRlzmAOxJOghV7jmdOI9BYokPjnVj59LOeZI_-9KcGh-JQwDM2-LX35YTWRTCyI-omwVvi_LPJjEEt7ZBOI3VhKlSYn0yTZINARIj6iSmCSmt25PHXQWbqRCoWyN9P1pKdav_4AHtKVfhY6YZg7usheZeIRLPs-0UyYJhqco4l0-vd6zOWbJ4rzQukOOoXhhhqpQkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=P2PB-fK4zODcAupCsuSl5pbDhy2ehCGa-3Wn3KwlY6VGDMUe07ToNxK6N8wsyJaAcAuCgjRmcOi4xwDNZNV-GBvK2IVw7v8hQwBA6NDJqpLPusTbx_PER2E0TX83L4ZaSZZly84LmZq8aMcOLRlzmAOxJOghV7jmdOI9BYokPjnVj59LOeZI_-9KcGh-JQwDM2-LX35YTWRTCyI-omwVvi_LPJjEEt7ZBOI3VhKlSYn0yTZINARIj6iSmCSmt25PHXQWbqRCoWyN9P1pKdav_4AHtKVfhY6YZg7usheZeIRLPs-0UyYJhqco4l0-vd6zOWbJ4rzQukOOoXhhhqpQkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=vPYz0DuOenIJ1ptDfrdHjleoRcNJIwu1UXzwjreSJkTkw4wTA1y0RYDVuYprI5eu4E-McCtfrmm50_ADf_YzOEhmaRnpp7uSIlQXg7G3QxTvrr5BeFgaKEDwm7UnqdeSyA-YZEg2Awz-1WdWm13ag1YkF8-e6APNw1DY9zTaW7BquW4rNweGiq8j9vCdia5UxMNn6-FZwczDNoRoWA9KLPqFasEWpCfUE_FHhUTODJf2K3vrb-r0TvTeJnRfheQ7qqTsUWTIaOI18CDeI7LcAtAWmzigK-C1msjMr7uuNt0desweF4MqOBKaY5GJYctFW9uV8Oeb3JS4ZyxxQriwTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=vPYz0DuOenIJ1ptDfrdHjleoRcNJIwu1UXzwjreSJkTkw4wTA1y0RYDVuYprI5eu4E-McCtfrmm50_ADf_YzOEhmaRnpp7uSIlQXg7G3QxTvrr5BeFgaKEDwm7UnqdeSyA-YZEg2Awz-1WdWm13ag1YkF8-e6APNw1DY9zTaW7BquW4rNweGiq8j9vCdia5UxMNn6-FZwczDNoRoWA9KLPqFasEWpCfUE_FHhUTODJf2K3vrb-r0TvTeJnRfheQ7qqTsUWTIaOI18CDeI7LcAtAWmzigK-C1msjMr7uuNt0desweF4MqOBKaY5GJYctFW9uV8Oeb3JS4ZyxxQriwTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=ZI87g7bnGfreIiBAyBXcCikD-4qSmvV6zJe9mTkHgvj5OMuHHWH5vjA8lHrAdRnj3ACnWgzdxj94ij6ge9ZkeiKkWDELXk3G1pxfiBYAefX1t9q2zoeLgyNckOSeQwoiindpttekH9_SKtrLrjNSbeVgj1c0WgDgPGhtXhJ810oymb88a35_kxJ3ydzhy9WWskYRuuUmwqrV_-lyZXqo6yNmtAy1JI1WY9L2DjTk0r1gmKxVSLnW9gh6oHxpCH8qdXcNzxqrd4Xl1qNOfRl83HD7l5CLdvlf2Ex4Dg0kfUu1BqxY4dZKXO54--b1rFmQC5_HfJA4qUhCgU8yun11cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=ZI87g7bnGfreIiBAyBXcCikD-4qSmvV6zJe9mTkHgvj5OMuHHWH5vjA8lHrAdRnj3ACnWgzdxj94ij6ge9ZkeiKkWDELXk3G1pxfiBYAefX1t9q2zoeLgyNckOSeQwoiindpttekH9_SKtrLrjNSbeVgj1c0WgDgPGhtXhJ810oymb88a35_kxJ3ydzhy9WWskYRuuUmwqrV_-lyZXqo6yNmtAy1JI1WY9L2DjTk0r1gmKxVSLnW9gh6oHxpCH8qdXcNzxqrd4Xl1qNOfRl83HD7l5CLdvlf2Ex4Dg0kfUu1BqxY4dZKXO54--b1rFmQC5_HfJA4qUhCgU8yun11cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLmFl97DVR44JfV_14TV3dvbjN95SHQGhNZVKdoI6zLmwt84XtsA3Y_vDxXOMdn-n9ngv6Qw7LkTMQtCMXUsF4TAJ-Ow-s5JsvW43TX8cxWk_2QfVfoCOLCCOooIPFSRCqasJqXES4ctQLK1RUwfZMYi365NEry_0iObfAtOXfNSoVJFLzhqy1AidrWfQImh8BlWXGsYVA8ieCQzIeVeTN1fxeqNtxFKlGg8qxaZS8epVx8fc4W8uZfrZvefAHZiY-QmVUk8aR3MaCcVWhBOi7cS4ap92Ykm8uCzCel0hRHcvTR7MIlNlIPNy7K16lpYRD1pVNUNrCwGf2LVJzl1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=u4kPlzhKfsQVoN_hEe17GNDA_nJ_1Z-HyWV6Jgcbon8NHIh0MedE8I8KDUPphYPTI4HP0sye2PprMvGkAAIGz_z493jfsK8M3oEk7b40XhSEf3-j7tZkFwVa_giPij_L-ouGt0ue83Dg00DCsYr3likM7PyZLf--_mBc6ghvYUErmX6l9DXvlcVCONPbMwly2Lv4ScIJu2d049Z-zEJvN_k2at6APKJ9nmMNdK6qRxP_WfyzL73tZuzuIno0aTUYkWyN_FTb8AN5X_i2dfsNnGW0XdxI9ARAW4Ma0dgtotkl1eNOoFXDd5zDCOAItnrd0yVqHBKRQzXtItKvrnfgOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=u4kPlzhKfsQVoN_hEe17GNDA_nJ_1Z-HyWV6Jgcbon8NHIh0MedE8I8KDUPphYPTI4HP0sye2PprMvGkAAIGz_z493jfsK8M3oEk7b40XhSEf3-j7tZkFwVa_giPij_L-ouGt0ue83Dg00DCsYr3likM7PyZLf--_mBc6ghvYUErmX6l9DXvlcVCONPbMwly2Lv4ScIJu2d049Z-zEJvN_k2at6APKJ9nmMNdK6qRxP_WfyzL73tZuzuIno0aTUYkWyN_FTb8AN5X_i2dfsNnGW0XdxI9ARAW4Ma0dgtotkl1eNOoFXDd5zDCOAItnrd0yVqHBKRQzXtItKvrnfgOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=Ng5v0fxfFVsRTLIvS6L-N3LUZ4J1ghNR2gDCsRDfkfHlhfbn78XzjUY5pmXB8TxxhnBJx1mIhq0H0Nr2nLdN_RUHuxPA4dk1qcKjAueSJwsLguWYV_TgiTY6E5YoH3c14aEQt5LM2ciSeKEqsRQHwqWLR3Fa2QbBTOpoOYnnV-Hz83j5ML8SjWTZeNqDwmE67cLKJfiQ-81ysIZlqJ1wHmDh33O0XQVm6IkYSnROYgv80T5TKVoh4vi3FtXqj9JEP4qtvVDGb8pcxpZgPDOVy0NlyVTEigX4N_5XH31V090YglWjXQrhEWmDa2W2D_CB7at3Q3lhvPDa1i31YlvN-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=Ng5v0fxfFVsRTLIvS6L-N3LUZ4J1ghNR2gDCsRDfkfHlhfbn78XzjUY5pmXB8TxxhnBJx1mIhq0H0Nr2nLdN_RUHuxPA4dk1qcKjAueSJwsLguWYV_TgiTY6E5YoH3c14aEQt5LM2ciSeKEqsRQHwqWLR3Fa2QbBTOpoOYnnV-Hz83j5ML8SjWTZeNqDwmE67cLKJfiQ-81ysIZlqJ1wHmDh33O0XQVm6IkYSnROYgv80T5TKVoh4vi3FtXqj9JEP4qtvVDGb8pcxpZgPDOVy0NlyVTEigX4N_5XH31V090YglWjXQrhEWmDa2W2D_CB7at3Q3lhvPDa1i31YlvN-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=eQM45Ys1pZcXVYi0h_BuNuwA2irpvgbjgy6pRU7XJz6QSlUjtLoQA2wVrbaXFgDRlb1U1swa__gjbA7l8sR_I2kP_G3zgmtGPxAf1-hqbhGUEPHY4IU-6hidMdxufB6I5VHh5auvRH0F0ADX6hifw_BAgydvQRWomURxyGQCeH_HsYcElLAD30CLkFtiD1xVSiprHi_s5m0auTO6Y4OCEduLuKn-Y87-w6map9l8ffk1s6pzTDHvsKVoWMyTzw5yvfmOYJiHA5tiSwqGZ4mpNJgiDll1ke55uFttpenbDZAWuTvYYT9RL96a9Vf7n4Ngljh3ZuV8WL8_lVZizVCJ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=eQM45Ys1pZcXVYi0h_BuNuwA2irpvgbjgy6pRU7XJz6QSlUjtLoQA2wVrbaXFgDRlb1U1swa__gjbA7l8sR_I2kP_G3zgmtGPxAf1-hqbhGUEPHY4IU-6hidMdxufB6I5VHh5auvRH0F0ADX6hifw_BAgydvQRWomURxyGQCeH_HsYcElLAD30CLkFtiD1xVSiprHi_s5m0auTO6Y4OCEduLuKn-Y87-w6map9l8ffk1s6pzTDHvsKVoWMyTzw5yvfmOYJiHA5tiSwqGZ4mpNJgiDll1ke55uFttpenbDZAWuTvYYT9RL96a9Vf7n4Ngljh3ZuV8WL8_lVZizVCJ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0FkvZIRWC1hOliUqjYoe8Fuw2ff5UtUQzTQGj8ftQtD-FbVBUWAtKo_x8ygRSrMOQXVvh529YJHdhfqPdvpWYVUw95jZiVdEkPVjaaDLLGLeH0kE69eppVOgwGykCo4_bAhGckrn3d_VEIanGKKbtjQJTldCKIhd_jsY9klv0PS_z5511KNB6yjMy2eG67j_ByxGJMvUsvwLBjcES3AV9Olfvpll08RDA1JgnIrTnJdGAlhN3Rd4JXI1ffrwYqV8Vq4g4MtWVktcR3BwDq18nxW8X7zqDtc2geEnWwWoFq3Eo2ri6yjonTAmgmoCcYO-qcMXlS-Yw6Ch6b0paPDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=JG-zXpY-GcOXaJAQ-XctF8YER2mztvCgxoP-4jRuHgmjQfDFWC-L2H3Owzz-l9sTmL9QWk5nbR5C5Y0KZMBWzSennJglYWK3CWL5UikNE5k51e1dHtF2AwnxjtLI4DOZQlAJaqBhcchzqnoqoisxiAP2K_mOyNRTpl4LpaJveRykGhnIvuBbZtWWtVQbjT1eQaUx38S7-7zUJ3ytT_7vfy5VJT9NuTK02197s9q_Z6FU0EOgU784JuBxvy4mNGMb9vZBLJf83CKQ24f-vIXDIip1xXJ7t3lFJs7kH6TFowp9TT_XrBklZsAUjl9Q3vwnZj0UE-C-ofgOAco6fo0IBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=JG-zXpY-GcOXaJAQ-XctF8YER2mztvCgxoP-4jRuHgmjQfDFWC-L2H3Owzz-l9sTmL9QWk5nbR5C5Y0KZMBWzSennJglYWK3CWL5UikNE5k51e1dHtF2AwnxjtLI4DOZQlAJaqBhcchzqnoqoisxiAP2K_mOyNRTpl4LpaJveRykGhnIvuBbZtWWtVQbjT1eQaUx38S7-7zUJ3ytT_7vfy5VJT9NuTK02197s9q_Z6FU0EOgU784JuBxvy4mNGMb9vZBLJf83CKQ24f-vIXDIip1xXJ7t3lFJs7kH6TFowp9TT_XrBklZsAUjl9Q3vwnZj0UE-C-ofgOAco6fo0IBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bq4T1Bq2bPy1bOyK1vvB0Q78icEMwhKYBTwKMZtYNzfBw6wEjZB-5F25c1nzzetpY2YItX0EcYsCg31I6zRB-ppDx89G4FpcHygw4h0gaSBjmIl9eztRycDpcLsRDuRK0sgcZk-a8q3tvRiLnWKHD9M6GcPo3wECHkS6x8GEoNrDHkZ1f49UDAzabL3lkkIjjJ8jGdqHVIDiMAEi1DauedNeBeO1qYW_-lKD46TZ3qi4IoaUEmJcuvwYIIPmI4E-L1WrJ0Afo71gzh4Zo1LDPs0NvRomCsSNjztZXnRwniibGuKZF2dDOGStOd3GOQ7uuTOwPuC6BCad1y-PyHDjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=NOYxRUCRBDPSTw_1alP911A5ZKaoneSIauHfI0ObkGPaXh06vE7cz_Xm4R_WVA5Pm0IDDuwMqdHQcPXkfJiqB0-B_LUWBhZAD1XFkEuRiez-jnMR1-uq3zOvztE0Iattv6zGqvO6m81Yb6zs5ZuDsWSXoimOTbdAcGvSpeNKwb44HPijYQNHGxYL2md7kxsK3i4spjpb5SK8qZ2QAO0xBmmNdjjkFmy50T4ga7SZV0AaNz7H_9alfFRoMjImRfq3nMR0rjKkHRipnyc1ftbmbel0J-Y0AnMeCAU5tRGNTFKVJj6Xm5gfXOUhYXqKBIhaMJ_4ACzZKdCp82lXb15FpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=NOYxRUCRBDPSTw_1alP911A5ZKaoneSIauHfI0ObkGPaXh06vE7cz_Xm4R_WVA5Pm0IDDuwMqdHQcPXkfJiqB0-B_LUWBhZAD1XFkEuRiez-jnMR1-uq3zOvztE0Iattv6zGqvO6m81Yb6zs5ZuDsWSXoimOTbdAcGvSpeNKwb44HPijYQNHGxYL2md7kxsK3i4spjpb5SK8qZ2QAO0xBmmNdjjkFmy50T4ga7SZV0AaNz7H_9alfFRoMjImRfq3nMR0rjKkHRipnyc1ftbmbel0J-Y0AnMeCAU5tRGNTFKVJj6Xm5gfXOUhYXqKBIhaMJ_4ACzZKdCp82lXb15FpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLywx3FWB4cIYPyyLnwlpr26QqTENS05AcFYHeSWJOJk4yGjohsXdxT0wtrwLey20wG4bvrCD_fPTyuIsBme-_GrbyNKyF6PqYESblqtl4qCaaY89ZfkLXx1yAbGfXVB_v9CkpQ9CjayBcIeEZq8hJNVPwVDujSTbCvhDOaH6Mh4OCcUq2QscSJLe1whjyJjlE7IwygIO78LWSq9q831FTC731mOyHn6RVDFXfu0spddrBpSJAbeXnN5o42m8vvzlZHhzg-1U0l7QhuE6vvp3C2OueDqXO1enEs8GgSGlHL9Qox3gx28mouqAhoatSR5FsVpB6zVEPPNyyLCBj2eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=ffWAok6PCK253f1fpKedkTdDo1k0QPAvioIZW0zY1FaN1l7EMGerpm6OpxbueKST0KRy4mt5sEtRXpgoGv_yXdnqV_MeNFyoHZlmgWRkW3GojFbhhODJWtiWoqnVsWmvQPkFNse2hEbJvZEIUop-79e4o2HAdmjRAfuK5PuYaLr-sNrIIuQ7tekL5A4Lo5Klow6M7SVUNqqmffVP4JROu0irdBA5g4G1RxckomN2vnDDcBhw0Yrd7q9I_Pxz1G8GexAM_VYIujth82zuZdWita0YM0hnnac15PxBxFqiiLr5CbuRw8gipfOtEDTuNfsIF2dsHT5virjPZQTxNKkhmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=ffWAok6PCK253f1fpKedkTdDo1k0QPAvioIZW0zY1FaN1l7EMGerpm6OpxbueKST0KRy4mt5sEtRXpgoGv_yXdnqV_MeNFyoHZlmgWRkW3GojFbhhODJWtiWoqnVsWmvQPkFNse2hEbJvZEIUop-79e4o2HAdmjRAfuK5PuYaLr-sNrIIuQ7tekL5A4Lo5Klow6M7SVUNqqmffVP4JROu0irdBA5g4G1RxckomN2vnDDcBhw0Yrd7q9I_Pxz1G8GexAM_VYIujth82zuZdWita0YM0hnnac15PxBxFqiiLr5CbuRw8gipfOtEDTuNfsIF2dsHT5virjPZQTxNKkhmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rU2PYaITQmDsj7sBH8huzWopN9smISQIIhgX9utzAQIZU5xkQIW-4SVYXgkBnCAKWyvka_F0NJTI4HPoSr4sFOGHnUAdoft2IVy5FB9gEChxOvGTOnvXhtO0yRkvEIvbszicBJDULwZ5e-UHMvvJ1oCmE9Xg5q78QUvyyvHn5lH1LIYLu2ywR74NVgFvTJDiQeBJ0O987s8u-XppoEJpx2Za52GwbYzYFvfTNEqeYZf9D3jT-589sHj_lBBTF3bLKI9tWpmL3QKh5YneI9zE3YSGGm2VwYhKOh8qfoupDxV4cA8O1oBc_4fqdH209xhbQv_LcbOePAul_g_a3fxe7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSdeADOEsKIpMcV-uGWTpX8YjMlgoOjtsh-hWIvn31SY60QqURox0IAWIcA1-9TVEFBv_RyLbZt1arg4x1jkI3WcBBbgqu2flHNYg5OZXXktTYpL2Z_6TsXT99Tdf2yY-T1OimEf9RFF11Z1dGudSJzH91oo5LmDD7Ndj6F8t-18n7XFZ7HREKTPC_ml1f_VDiOPmJdId9L91exhz8NbYlWCHjFavKWoxIxJNO06XORR7t17361wBeptAripNFemvSFfKieNB67FpzuJlqYsZK8TdyRfmQcOAthdFaCDViADHFf__5f1jspdeLFUwzRBhb0X9Q-UlcJMdjuqJbmZ2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=hHnv-YUImtDeQVNozzYxwFu4H3YJN8onE5Djx87iVI0YYrY5i6rBqnv-SCRXB5Vhk_z1EcyvBMdGuwVGzYOdT7DjC8wnT0tUIwcGVdTXMKm1vFlu87kg9FwO1wgu9byCgynS55mxMWgFfnOnL3J9udpglzmBuIYYvBtOQqzFdZjGQDfzU5DK84AbpwDAf7X5tcsAd-oIK3Faxt3E2GImYTZoP_Tl5lUVUr9r54P_Bdmc5OW3_XmywQp4_pHL6LlrIuzNkuUVhOA742fqV-aDrfJGAtZi10PN_jwrt2FEJuzLPl6J09UYcnsnXSePjOotGBbLPnOJIImWSyf1_kNtFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=hHnv-YUImtDeQVNozzYxwFu4H3YJN8onE5Djx87iVI0YYrY5i6rBqnv-SCRXB5Vhk_z1EcyvBMdGuwVGzYOdT7DjC8wnT0tUIwcGVdTXMKm1vFlu87kg9FwO1wgu9byCgynS55mxMWgFfnOnL3J9udpglzmBuIYYvBtOQqzFdZjGQDfzU5DK84AbpwDAf7X5tcsAd-oIK3Faxt3E2GImYTZoP_Tl5lUVUr9r54P_Bdmc5OW3_XmywQp4_pHL6LlrIuzNkuUVhOA742fqV-aDrfJGAtZi10PN_jwrt2FEJuzLPl6J09UYcnsnXSePjOotGBbLPnOJIImWSyf1_kNtFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5dKU3YgEV2b6nw8ZPigAo1L6RKerOEjS2pl3__d1oMZ4iZy6-UtUkYuCdhQdg0wrbAqxKovHXvkz3UrTBV2tebCeJGgA9hrKAQHr4V3Bpo2H8YbTcf2TNcMDjpKAnSny6NpqSsCMUsK8lcDMUdVf8L42DolqvN4pDQQIEe4eQnsLaiT2pFmkWzPZ_FB9iuUmfD7zU81GU7Nu3W0t0foTplWJ7kV77lvXzgASNgm9kB7Lexd--xACy0zV4n0CkKm3nmdi2Odf7ciERZ3YUQbyTIhdD_wifOgQsiRo_wZGFsx2h0Y4MSQOERJjrvMiAf_NO7SxPuo-soUEY3kSTzztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM2aC2mIZvUkiqk2eYx04VP3imatXxXjIt9Hz2jvnOmbDdIYVOBbylZQoS9KMzn-zBZRBdqfByl_byAoDQRD9ZYwwswkSYnvv5p-FiZ3IxGRBlCJoeEq5zGVUO0uxyNDXKGI1G-x1O6CtX4d-lqN2PLGbCglYYOglGHc4y2Lz8r30Uha9ELrsXUfMLDKkndsoYiu4wkkGly8AMuBEA16HwJdnxxHFn7RhuU5GgpOsKA1Vg3NUsWv9zqZqZ8fVG6LqIVxmBlpGLjeCt8pCd4GXuMnVtGjNeQZpy6qeP4mwbVd60COlTyzHA0l3bbF4Bu-1G_KWpypi-TQIIvgV1zt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYi24UYikgqKB8iGT0XWCH2zIuQp7Dyv68wW1SeAEszY1u4zQ0NsjcZ2zHLXGrtjJYzGSAj-7itarT4Yz581a2xRB3ytiPLtA43ohSbM-uSR9fHl60TqvuHTRv_dxibKU6dS3cO-ht0cuc_ObQBL7ituBmZo19O_3d8KJwWEvq5IYJnHrnJwFJB4jTZiTCgOV2SzrOLxxFVNNvR-f-gBv9OYy31W8a7iLX6Iq9OPgGrswmEAZkEuXotWuo9lVEl6dtoMgPlSwLhdY7Ma1ywYhmaZDEIHZNzpMYNh0KR78zkylzHN9ou327L0nG5T7jf8gMJL7b4AV9PbQOMyCpAPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeG6ewOI96ogqs12WRBkTLbhtCSm5I8wHJnJ7Hk7Qkj1AVrupOmG6tRWX51jbmMzaA_f0rsDA3dbQ6HC8KK4NCszyffL_s9dcvkP1i7As9hWf2_VOGY4x0kPuJSk0wruyb-a0_aDcA9GxGGMuHtQbLmeYwovwtVpNQakYuWghj6gIHxzEJfmzeIUWzFO1JQ7w4WknLNoT2YSfvN_CkW-Q30Emf2o6LNSbG5MOCGWGPguB4UG3bEqmZOm8LFW6__y8DzDzD9NcDJwAUYG_wT5E53aVN2CuCjSSxSB8D39IvUURaZIWshUwQocxgZU9GhCof6sNoIHF5F3FcheXYJRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q40Xhq5yB9YxbMXHIoQX4Du4keiCVkGaX_fvvBzZ9FymfnQpVUpqH2y9QATiE7o1UX_0Fgd87NYyE2QO4SC_Zx2PXiMtPIOc893PHy1NdrwtrAXu0HDEEcIAeb6Lj96KJG6z6yJBB1hS6koIXZWPHnWYUx_77Fb_oLKxdYQpMK6aeSXZ2hDi0p-VyIEn0FnB_7csCkhWVisuXxEvle1hPxmbwKzIhSkyxqDhKl69ow8m_T05Cy2_kGdK2OznxGi--L3waTlv5X2reeJ1IZmrL-E6jbpBLnb8d-88ttqsXJQe0VoTihZ19PRCKVuS6ad5pHM8ilQuXflJAFOjmv_VRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=V62mXnXK4xCLt-0CzG-J_yQlvotL3ZHBJeRq8uVUZSdeVTx09c0IOEGILVD3_DXZ8rRvKGYPDPvzIYgatKvCuLWWarEod59jRQCdVbnSb3zp8u7tZ5oqFv8DZM3iQXCQy335eqrZpqvPy0m5y_22VqxmmLmV0ywAmi1tpPkpYhuFzL9vOMTFzYOFvuPB9kq3AySN-3_eI19TH95i1UYUkgmxSZ7NvqvpKqMmlIlvZ1fbe4R-uS7e98IbEqh6t_90ZBxdxu2CtoldI7Y0wfR0EGIqErxg_QzCqLODbK1zW4lRsGRB5KcVkRJO3dCZSv45N7rw3062ZooVFdPd-qNuSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=V62mXnXK4xCLt-0CzG-J_yQlvotL3ZHBJeRq8uVUZSdeVTx09c0IOEGILVD3_DXZ8rRvKGYPDPvzIYgatKvCuLWWarEod59jRQCdVbnSb3zp8u7tZ5oqFv8DZM3iQXCQy335eqrZpqvPy0m5y_22VqxmmLmV0ywAmi1tpPkpYhuFzL9vOMTFzYOFvuPB9kq3AySN-3_eI19TH95i1UYUkgmxSZ7NvqvpKqMmlIlvZ1fbe4R-uS7e98IbEqh6t_90ZBxdxu2CtoldI7Y0wfR0EGIqErxg_QzCqLODbK1zW4lRsGRB5KcVkRJO3dCZSv45N7rw3062ZooVFdPd-qNuSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=ncHlWRQE8IuEMr0UypyE525NotgxIfW1p0jPJJJDGtBwxj82VzryQoeizShvJb3iW-ZX5eNYMXlgOXOLCZUKWH4YUxU6wmrkz7H-IrXuAtWDuiiPJsN--EZ3unkO5cmLGZ5vhWuQFaViXb2yciETFMvBAhjWkPp82RJtrazaD_8PPCNXtnzRx0QWO2mjhjXKFK6DXeGFt1YFE3OsX9fuRwkbIKwl43bP3QssK__rzH3fKFKVp5QistIaWhoVl5n7d3gH_RuB01vsIROtGqZNbrjgP57m4Ec_6bWZjevMo6xOzdNy6KSASn4WglL9WWUe-w7UiKgHewmH2T_PlMdoOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=ncHlWRQE8IuEMr0UypyE525NotgxIfW1p0jPJJJDGtBwxj82VzryQoeizShvJb3iW-ZX5eNYMXlgOXOLCZUKWH4YUxU6wmrkz7H-IrXuAtWDuiiPJsN--EZ3unkO5cmLGZ5vhWuQFaViXb2yciETFMvBAhjWkPp82RJtrazaD_8PPCNXtnzRx0QWO2mjhjXKFK6DXeGFt1YFE3OsX9fuRwkbIKwl43bP3QssK__rzH3fKFKVp5QistIaWhoVl5n7d3gH_RuB01vsIROtGqZNbrjgP57m4Ec_6bWZjevMo6xOzdNy6KSASn4WglL9WWUe-w7UiKgHewmH2T_PlMdoOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=RG_mcJpnzK70jGUsiBnlD1_1PwzoP35APhqJnWvAb7Qp9BqN08FCTQHhEADaiheW3DiH6GLS9v81By-xCjrpEb_6L0yA6Od9y_8cTbBu5ta6FK5VmNInMxoAez22g_9VTZ_J6rkcTwEdOZuVzPgj8vr-tTl70YXDk5Vjz4c9rW-hbg4wWabP8ksjApu9E7Q0rmJexOG1lDeBXmThzdxqpXqCa-pk7Mmc_0Okc9sEVNvq5oxE7vgVC0DXtnL0LPC4QxH15naN7LyfO01lVNs8DvS2_t2ybgtzIRUsGVPI0r7NC4fh5smC5G2FHwNwz9ABAYoNFOMonLeD1sJhZO4gWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=RG_mcJpnzK70jGUsiBnlD1_1PwzoP35APhqJnWvAb7Qp9BqN08FCTQHhEADaiheW3DiH6GLS9v81By-xCjrpEb_6L0yA6Od9y_8cTbBu5ta6FK5VmNInMxoAez22g_9VTZ_J6rkcTwEdOZuVzPgj8vr-tTl70YXDk5Vjz4c9rW-hbg4wWabP8ksjApu9E7Q0rmJexOG1lDeBXmThzdxqpXqCa-pk7Mmc_0Okc9sEVNvq5oxE7vgVC0DXtnL0LPC4QxH15naN7LyfO01lVNs8DvS2_t2ybgtzIRUsGVPI0r7NC4fh5smC5G2FHwNwz9ABAYoNFOMonLeD1sJhZO4gWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=i2Nh5AXEORqXe2nvX23_6bULvAltV5Jk2-laGMDA6P7CgBMXjPIrZvD6XKqGbQqV4Fkv87dUthHD5DL-EI-Ejyu0qve8K3Fls2rcvyklpVxOzYrwi1wKwHm4R7hlonPRfCeNpaEbghho7TIwCOdEYteVlNXwcagkeCGoIkkZIVg46KpWiFq4t5je2zGQ3xMyldsyqb2mbx8n8ln2M5bIhNSOLwzBe1Z8loW_4UJ_sjX8pkCW8TNfzmW1Zip0Mmc9JDxuRr9i-2SFdTlxanyMkTyebFp2xnd3YhBypG0CGQQrHm9uNhjDfif9eSwf3CL6hoLElL_9sej_9CsZyykopA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=i2Nh5AXEORqXe2nvX23_6bULvAltV5Jk2-laGMDA6P7CgBMXjPIrZvD6XKqGbQqV4Fkv87dUthHD5DL-EI-Ejyu0qve8K3Fls2rcvyklpVxOzYrwi1wKwHm4R7hlonPRfCeNpaEbghho7TIwCOdEYteVlNXwcagkeCGoIkkZIVg46KpWiFq4t5je2zGQ3xMyldsyqb2mbx8n8ln2M5bIhNSOLwzBe1Z8loW_4UJ_sjX8pkCW8TNfzmW1Zip0Mmc9JDxuRr9i-2SFdTlxanyMkTyebFp2xnd3YhBypG0CGQQrHm9uNhjDfif9eSwf3CL6hoLElL_9sej_9CsZyykopA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckYeAj3LRt-ScO285fVJG_owNsI97hytQW_Lcor0sut7zr7YEas-axa8c8DJkFtMD16ftksIL6JxfIteXgfubyW86qCMbDFgVJ9c6tOvntpDKzD658QfSIkomDL8cDjtDunRGzLAGV-S0E6p8YmTjppjyVzc6W0mCguIh4Sa_t2XLHHxG8rWwyaRkYrKHscCLoR0IddfD1oz8PTxr6PjfxrAzxyAi64KZhoojrcGilayoLjPAQB0NEYS8oczOS91DPqExj49f4T-2ovSDZo9Cme-suT3thEJrQeg9XSoh_IEY3ggFl22kgkmeb_NjVWJykvGgMpU0egUU_JY8emb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIz3FSPC8JQ3my56Bp7rwd4Asc_OFMPE29r4s2riC--gWf1RXsTF47uP3d1rt9krcuFcPDT6FBWNP6RXP-cq6WUd5X3OX5lqB4F2BLofLSxSBX5iRfzlld5k4y5OZTx85Zsz7UaYDRAkHAMpXt_8Qmel12xrvNwI9pmvKWz5otYFYC5P1nI-wREAyF_D84F4Eyzg6vTsVzbYL4hfuUk7uvVPBxtEu7_LXrCxHb7fqoWJ_FHxyfAoLse6Sdh_NfCGNXB1wm5LWc9anGwa-V5dZxqkS29T64KPi889LksEBP6qXhOLzt7Xkec0EZ2hjcAEwhU00NGGWZTyViuZpfpsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=Jt3wmYmHILEajhEwnckSpuDZANgPgEsII5e17bmyBm2DdMwxcWJINHSVMxv0asXO4Inb8hZMiQtx6thdJLx8PEg8AEJ61hlixxMMb1-Iv1DVXB5b_v7zy2zf-rg72fXjcCSTsQfXOqOjLafyA3gM_VZI15CBMTqwwo5NSX7qxyiQH-gVoTgX5LZZQ22ad81elKR3cg3ghuTFDZQxA_nM1lR-W8-ta0U_ksIlR0cb9KFsSlQW54SuHPKVeZjyVTcez7fo2T4gwTWVTSOOTFKl1HxAnk-ULY2tCuZHLi9MAqTF-xqhiZNkX5GHu73tQpy3kenMcVARV6nH8lSbOY_rYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=Jt3wmYmHILEajhEwnckSpuDZANgPgEsII5e17bmyBm2DdMwxcWJINHSVMxv0asXO4Inb8hZMiQtx6thdJLx8PEg8AEJ61hlixxMMb1-Iv1DVXB5b_v7zy2zf-rg72fXjcCSTsQfXOqOjLafyA3gM_VZI15CBMTqwwo5NSX7qxyiQH-gVoTgX5LZZQ22ad81elKR3cg3ghuTFDZQxA_nM1lR-W8-ta0U_ksIlR0cb9KFsSlQW54SuHPKVeZjyVTcez7fo2T4gwTWVTSOOTFKl1HxAnk-ULY2tCuZHLi9MAqTF-xqhiZNkX5GHu73tQpy3kenMcVARV6nH8lSbOY_rYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4_6_x-RBzNXMjW7iSM4UGv4unFtYAeThfRpAxQZNu-N0bT-61CDwKDDJRzw59CMYWeys3koB-FLIXHVZclNif4YmHNlFyojxOWWPNWFd856dzraqDjeZMQ7PUYlfMMei9IkHXtIJghkISVPZXoOwrCFnfVDEzcEKQVbZe9HZMhojxE4R5gU6tR9X7tAY_dJo6hTDR7QdU2WiMNbG4aCQQdOEt-4wLR-7OdmRZTItEhyPcVZCVIfsBwXXWoxNyyTi4_l-xGF6FGCY_9gv_ExofXS6d_Me_R4zSLKthW5_nKahKT_EopEebq4v8mQtgxsmrdG1n8aL7mwjYWh7oGYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=S34FSvAcFf8TLdn6xQwPLjHeKcsUEhF_pcKYYB37I_79rdgcPL-D6b3dFGE0-vdy6QbU4UPEqOxdSqHs8Mzdfj9lijAhul_7uacKGuZ4sfkWlWCbkpA6B3Srng9bzKii51AaHjHl7iaurZqZ6jerP7Ma84rph_laism6eDZTDKiB8fRjeywOXAm4UPNjZyh82ykd8ROLqYMfWVtOJeAOe4vO3wQ-yCb26f5-0Mmp6hSNaEqZjPRns_UbImhbEPnh0YXmNwMFYKMLZIzxt-2mXC7AVO-ueu1937v9dY3Uc94XLDhrer4lUxqLezAf0pbpWym0M6ruXQvSBupLGXOoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=S34FSvAcFf8TLdn6xQwPLjHeKcsUEhF_pcKYYB37I_79rdgcPL-D6b3dFGE0-vdy6QbU4UPEqOxdSqHs8Mzdfj9lijAhul_7uacKGuZ4sfkWlWCbkpA6B3Srng9bzKii51AaHjHl7iaurZqZ6jerP7Ma84rph_laism6eDZTDKiB8fRjeywOXAm4UPNjZyh82ykd8ROLqYMfWVtOJeAOe4vO3wQ-yCb26f5-0Mmp6hSNaEqZjPRns_UbImhbEPnh0YXmNwMFYKMLZIzxt-2mXC7AVO-ueu1937v9dY3Uc94XLDhrer4lUxqLezAf0pbpWym0M6ruXQvSBupLGXOoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWdcPiv1hVfO1-zMli5JmnvyjzF80a1Iav-dX99HzrJtPSAtNuAx4pX43gp7qXPivFEdMo3lJzLvliIa-WIko3u9LMOY69JErKyoZAMumTGJA161RoDoyTOn_ulOTZLQONfutaOjQIbGU1R82_zskdrlJrfZOhUS_wf7KAV54fXtN909Llzlt5xRn7FZlasBuR52-fLDyFQ07g4mCHKvB4hFuZtOvWeMPaj_sNKV4qOOEphRbfhfHpomEDWIYat2731Ig2OTs-ziGnvLrYTXqn1YLiCEebKA2tnww7r9yYT2KA7n4atGUhdg8qrTHvU1hJ6pfrlhw-GwoD42awwptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ0fGT0_JsbUo6ubIHE3NUdC3bUekRTiYZMZ7MZquIvmap7_bmLlWRCMB1ZnBgr5AMtPLN6G-5AFLEPybGU6OxpW1aXTcTvZXU5SCrLfytGs_EFH4JC0bwwZGF3e0fbTVIWPcL1UWpL_2b0V0a24nVT74AxlrRZaV0DhGNWw6NIg-JRarjhlSPIoKJPKE9XWlE23bzvEwU0ObwslH2Q6kRuXo12wBkDi2EFITyam1K9ymoE_Aww9wSbzh7-X_3HSdPDNPUeBLzWHMgiJb7d-aD71z_s5NMsGBnaUdNlW-l9TNg99EDSDvckbShMM2vVkjjaqDfKyjz8MU-qJgVzdiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=DI7xS2ZBc-4B74HHVrEhKwtmIo7XtWL14Keubx4-pr_IqS7xSw4mh7WBv9sY_gxa2zojN4zubVHcTocsul5IQLq0oZTdJpvkLRS6qMPjZmjQGo0yhwQNtYsgV5KSfrSNr3kok0hPfeMklFfTJd9jr0yy97qb9zxDnxDR0Z6nTS0k394Ru5CzP0H_Lghm544REePUHtxApQkkbg3cCBUlM8LQM1nrEmvb6svyFCAl4p2cOP3b0Zz2hfpnPBXSyLCBgnYSQSBAhGYYcj7OpaqxJPNlLNEoqKD1a3CNqXZm_21xukLkIetf8YsQb6i1grTOJXxKpbEa6sliBiYXZQ5xJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=DI7xS2ZBc-4B74HHVrEhKwtmIo7XtWL14Keubx4-pr_IqS7xSw4mh7WBv9sY_gxa2zojN4zubVHcTocsul5IQLq0oZTdJpvkLRS6qMPjZmjQGo0yhwQNtYsgV5KSfrSNr3kok0hPfeMklFfTJd9jr0yy97qb9zxDnxDR0Z6nTS0k394Ru5CzP0H_Lghm544REePUHtxApQkkbg3cCBUlM8LQM1nrEmvb6svyFCAl4p2cOP3b0Zz2hfpnPBXSyLCBgnYSQSBAhGYYcj7OpaqxJPNlLNEoqKD1a3CNqXZm_21xukLkIetf8YsQb6i1grTOJXxKpbEa6sliBiYXZQ5xJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=imzA2HzHBJELewTR04d6oiSAyw9jYTkeHD1gslUHrrKMp3Sss5StroINdD8j0oZnJmgNa3iCfWTu9z1-7SQ7H_VPPtNE_E-3pMr0jak59-JmwwVzlRvtpNixrbj4EPQ__ykuo9zPSYbNRzS8KGgHMH__VWEYNVARds1OYH3Z-8hXmsSQtMsTcKbo_kx3qBsFy3vJSmuC2Hurtx1QmQshTa1V0MX0GwXkSVy0hXWvNtpkgS4jhU347bHE8URRdYFROtp-bVaMHfDEB8pzieXJC9lRjp0bH4LOW5y8KtbhBf_KJr0HjPtWz388DFDMwrJhpM6D8Cw13YknUdJk3d6ymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=imzA2HzHBJELewTR04d6oiSAyw9jYTkeHD1gslUHrrKMp3Sss5StroINdD8j0oZnJmgNa3iCfWTu9z1-7SQ7H_VPPtNE_E-3pMr0jak59-JmwwVzlRvtpNixrbj4EPQ__ykuo9zPSYbNRzS8KGgHMH__VWEYNVARds1OYH3Z-8hXmsSQtMsTcKbo_kx3qBsFy3vJSmuC2Hurtx1QmQshTa1V0MX0GwXkSVy0hXWvNtpkgS4jhU347bHE8URRdYFROtp-bVaMHfDEB8pzieXJC9lRjp0bH4LOW5y8KtbhBf_KJr0HjPtWz388DFDMwrJhpM6D8Cw13YknUdJk3d6ymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqnXB9YNxt4cvO25r60Kw5L_Pc587pq63BfkgIFr2gKhT9cwAe3Xf-b2B-sYwcSgeCgXE9xEqmtpRLIH1FKve6WqcJqmM1GYk9dPnPuf-gaQ0m7f8foO-Gi3Bt9Octf9yNpb2iWWE09iTutZwX5fRDvYcZDCCOiyCZI65AnQOS7B9xnXJRfS65PKg2Qx-W9S82708XOporaGguRw65LkuqwbTnbl4BczWukuGLlbJD2n188qkfHLs7ypWBjrGfTlp6CIWLclHTA1_sU3uUmwkeh08PLbtDBPPHpaa8uDO7Nbpe2Tm3zgd6qvVMghj1GpJQ_DyOSMznfcoqMyYhwZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKfJEFZY9R00xd3NTCLFHkPnKWkBq2L78kFtGjF3VK7xX6P_B07exf8BR-aVRP4Xjr2Ec7w3L0bUkem-EErQOvH2jurgpbiCAuh2pJ4iAaUupitZCNiwNhl-FbssxSqrIZn_eqDoCvAaYlJyYqnNUWXWZewaYK-Z4s7yWg6j6XJ0TfaYK9oiPV5zX-35ntDnUitfZBxLk0IDKwteY6xS-X0Ri7iQEjXY439DUO2XTvTNMPtS6qAaUGr2eC36Cv0lbDnUdIgRhcs974zi92Ilnuw9CGOg56TN3nwzRFiYiT8cqyoM1j8p3d4FkyWp1TeiMm-RaGqdK1fM9l78tPCnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMsuOoA1AmLJMIqNOu01AFkgYAKSkhuWBWgJnAZey-OpGPMAl6qDmMKPfa4n4OOmLHatKfsdT94EuutUIFRaijRDoIEuRExhILDhYzbUYm6pziXsF_kewfRCYHhTBsJ2FyhqAc47t-W3gFi40XGeHXNsxQgilq1kgyglnC89-dmRn405eVP2j4aF43qXInMJAtZfCHeZMfc9LtixeF881uWzyKZ0fbufEzeuXNTJSi_Czp6D_r7xjjkS-DobY6D_70A6-gNNyks5aawY6veqWYKWXlxV7oLfKpGxJMvRcYjoY83VS1XDzK2op674Dp0gvNv2xTlN8rvFimzopOGk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=V7oxVfzrrhd2NQaiZRDl5C7Vmx3N1bvZMDYXDzIfod0d4Xu7oBMers22O7o0G3pSLKLhQda_Gxery5XBBDOc7E0gxADkHZ5QxFCHAqFhuEBYOtR6oJNrMnUAbcH8XfBf4qGVj7JJZ6PAZlOvQJt5Kg56UeHGNmvR4DK-M6JQ5-OKzSsmHcyWTL8ynp8kpxMTvkirTyJZ-l4B0TEhQU9C9INY-N1HIPgYJhWDUax0wuYV6t-XthJrGF6quvda1B314obpkyxfueUSARRmisK6je-Oz7SGk3u1Ib1jXNyDg50BZYZ_6HSEZrR_dDZYZq5MKKQNt9EWLsDi6vr-vTbQwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=V7oxVfzrrhd2NQaiZRDl5C7Vmx3N1bvZMDYXDzIfod0d4Xu7oBMers22O7o0G3pSLKLhQda_Gxery5XBBDOc7E0gxADkHZ5QxFCHAqFhuEBYOtR6oJNrMnUAbcH8XfBf4qGVj7JJZ6PAZlOvQJt5Kg56UeHGNmvR4DK-M6JQ5-OKzSsmHcyWTL8ynp8kpxMTvkirTyJZ-l4B0TEhQU9C9INY-N1HIPgYJhWDUax0wuYV6t-XthJrGF6quvda1B314obpkyxfueUSARRmisK6je-Oz7SGk3u1Ib1jXNyDg50BZYZ_6HSEZrR_dDZYZq5MKKQNt9EWLsDi6vr-vTbQwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rekDj0tltfwdL7_YLuMXg68XTLEjW-3c6hPLhNjtyLoYxp1kMujfM6Y-7PFHjYignc0jLHtxR2PujFSrMqLIO_FEPJ_ZYnxUQ6br7YUKWRaXAbBTq5txT-KVSUqc_4xKMdZTVkEaRb3JpWwm9fNQHBsj-_LWvchnqPjJF9Z4M7xFcIVDPKwsEm1eDxSsfFvbOUvW5GiWRya9Dklld93laiTRpt_GQX6Z_GBkw0E8f14sSinda7UqvikyjI1rRyvDaqIgMT8Yoaf3ztuBFxFL-TVFpkbCnshM0G3JphuJ2whwtDbWZolyBQrCcY8kdLzlQ5M97NdtoHQXPwR7S9efrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOyJu6gsP1uL1iGyB9pqiSO35PsPAtSBQ0uPr3FgkEeUE_yYwn1SmY7cBMbfCYHURYKlnE5ujMlibJYNvU1rI7jdDuRZW_-6-qAahOoBghHIIxRXyVPqtI4m6X2bbBAcaI28hidlq7YaOkSn3NjHQr01ARkYf-NSa-GXvazXTryAiqTiDqnfiUWckIEsqRyRq39nyXNM-aNjO2XaPEZWAH2PFcDGrIt5RQDW4OmS_eg0YKPCjlWVoHKShMcbbNUqTIlKK6rn9i0MOQBHw9HLAsJy_9Bi5qHtla3OKo7pu-NA9Ob2oaee3OvgFpg78ifcBzLlEickjF2WUdWQzX3aEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b42gPbSyQ1qh95sgZ14DChZ74QzGPe2T9JkxEM2pTVMaBR7z5bDY_fWPnmKxGPSy1Bsx4zGzs3bfo6w33-5n7otvUAL2s8vFPPjuTNe2VTa9tOcQLrB2ISOPQCGqNJBRXi9XNJNfe5KAH98Pj0P2poeDeB7CO8KorpU44Ng9KagFdp-KWPQuR6nWHdI-AGG5KyWCO2Np75-ZMa5xT_2CEPJJuaiXtbPJlpPDY_BklYxpObio4HXbuGOdiJsFqMjUQKiSCzwxWeILp4GwrPiYG5kHLSQ3R1exGrZQmHXn1GAfO0gijRTHsKtrFvhHXOlSllswdByzLEwOKlMpbntk5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9KhR86N1sIsTNtCx4TKO_QLq8wItDMITtbZJgaLG1vyOmM6nq8cCwdELP1Wg9T2zRB0_HtXKj-aXO50KTBKozbJeHWjNASugt47E2OmSnth5-iqTqFFY2DKV_EapL5WUOA0MhWrQ53vpIlGzkGGXKxCmu4fB00BF6EPFGqYiBkia5N8p-BVySj-wmPnp7RJxj2OZ1SqS1MfftKIGnNdAi48B9MbaQ6iqGdCc59qRSZeloaACfEW-mcL_p0ESTUlM_l1NRRV5nc2fBYnUeOqamnkPkRpbmyL_SQ_0M7glOlZSX-UZdE-HDtRFL7O0SMyexxmwxxQxevhAOR8einPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=Nlaov61FnYFAgU9-DDsKfTjbo-Grh0WNzBORWbO_vQBIDOcJ5oHC4zUHrtH8rB5vKZBryLE1ORY4ndI173hoX7hIwDs95VphsAuhgKrtAj_rKgJ3f5XbzJ3HgegpA16RC3qrqsANfg22TSlzhF0D7vYTiJMMsywq6TPIAODfhyicF0nIsrjk6BosLii8H1wMSDRwmYqV61NkAihj_m8I3h3WlSRADpEgG2R-5a8j_nNDxVefFgXPinWPvT7WR0ZDQiIzUj5OryzBfCqYUsb4c4Xx9YfynuFsXDrzNXWM_6XTcTXkpSZyNc3XPNcPHqNyjfrrMoIy-DXIPCp3_61BIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=Nlaov61FnYFAgU9-DDsKfTjbo-Grh0WNzBORWbO_vQBIDOcJ5oHC4zUHrtH8rB5vKZBryLE1ORY4ndI173hoX7hIwDs95VphsAuhgKrtAj_rKgJ3f5XbzJ3HgegpA16RC3qrqsANfg22TSlzhF0D7vYTiJMMsywq6TPIAODfhyicF0nIsrjk6BosLii8H1wMSDRwmYqV61NkAihj_m8I3h3WlSRADpEgG2R-5a8j_nNDxVefFgXPinWPvT7WR0ZDQiIzUj5OryzBfCqYUsb4c4Xx9YfynuFsXDrzNXWM_6XTcTXkpSZyNc3XPNcPHqNyjfrrMoIy-DXIPCp3_61BIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxRyvZcbZ7WdXhAm5hDiQYOgRhcxs3L_V-LCV9UCkpaYDZptazjdSpgjHBnWv_vHFsLwIfBV4PRA52u70enCItos0B8taZyc3w3h35IdTilCLPpHuwbWEXlq2jrgq86G4BmbCOOh_xU-6NGkk_gfegMWZvJ4eRGM-7qva20MPb_cKufdxaYRjt-w60MKPdAf5PHfcsgslDLAokjNu9GkSrskxqPSkyZG-tMxP9ShwrRqjUhlBtr6L98RuP5CT8w8InP2pzg9fMhazDo33xke2OmMgZ9ABUgxDFti83XXaUyi5efYaxeyNeJnqJNlT_eV571Eit9sEIn7V-odgLDc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=v6J1lxtxiy0i76d51KLIbJSqy4iFPzyyeIxZxWyJsg8kRgaw-WIQ3XMGQZlPA-ylpaR8wgkpIpzbPvwCbRpncvKmVq15aJ98dN5OH8-rbC_0yO717_3_rPeM0Ia8Fn8XQpl-5iXCZ3-Oe0PWJtTqu959BtfHOmSFXLhW7_ABIgUOroiXfotvjDIQEKGEuXrOPjOQ6Fns7wkHQGJ4VSJUeOWsIBrCrahEKRzj3KfemvFfGYxLd4WlxZMVKYFKXFKlcFa56bETH66bQjxgVP-OimO9Kmx84bwHLGMiNRWaZP2dpWMzTnYzSqo2uYMp7sSuBohKjMd-_NCF0Q9TQ-OTdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=v6J1lxtxiy0i76d51KLIbJSqy4iFPzyyeIxZxWyJsg8kRgaw-WIQ3XMGQZlPA-ylpaR8wgkpIpzbPvwCbRpncvKmVq15aJ98dN5OH8-rbC_0yO717_3_rPeM0Ia8Fn8XQpl-5iXCZ3-Oe0PWJtTqu959BtfHOmSFXLhW7_ABIgUOroiXfotvjDIQEKGEuXrOPjOQ6Fns7wkHQGJ4VSJUeOWsIBrCrahEKRzj3KfemvFfGYxLd4WlxZMVKYFKXFKlcFa56bETH66bQjxgVP-OimO9Kmx84bwHLGMiNRWaZP2dpWMzTnYzSqo2uYMp7sSuBohKjMd-_NCF0Q9TQ-OTdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=Qilf-h7yXJtLljBgyRtDF7YUexCHjSXuhpDtP2J-WnwbYBIKePWaZxfApsNUw2d3suHODvMKSl0gflJWhK6p6aPrW8LS4J4DKJ8yJ-IFCpJKgJF5KXdmVbVF3aVlWYLmW_eKU36Ic61k39Aaq1hWpaCnPGIT7OPZYjZp54SWfuFENIsRCEwDUsmPum03DJb8VEiqjrna4T_KmGid-k9zMvz95isT5IgsNnGrkWnuMTc1Ypey_LX0o_dC3dwTkyw7h-14u_7TJOW_pxfu0TouCKhFqzF302zI_jN92eX3ScJrRPV2TKPCBss2f9fz1w_veersxgNP5NNX4nXYp_KFJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=Qilf-h7yXJtLljBgyRtDF7YUexCHjSXuhpDtP2J-WnwbYBIKePWaZxfApsNUw2d3suHODvMKSl0gflJWhK6p6aPrW8LS4J4DKJ8yJ-IFCpJKgJF5KXdmVbVF3aVlWYLmW_eKU36Ic61k39Aaq1hWpaCnPGIT7OPZYjZp54SWfuFENIsRCEwDUsmPum03DJb8VEiqjrna4T_KmGid-k9zMvz95isT5IgsNnGrkWnuMTc1Ypey_LX0o_dC3dwTkyw7h-14u_7TJOW_pxfu0TouCKhFqzF302zI_jN92eX3ScJrRPV2TKPCBss2f9fz1w_veersxgNP5NNX4nXYp_KFJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILczP692GHC61nFoezfOjQvirNjtH_G67AkdzyKx4kDfDYje4B8j81zwdQryPnvG9N7tFvC0TLUB9WrpnsuiVlPAmKwQK9K630GNUxr0FjNRQm3CW-ouO97PboW2kvd06vUfyCdalAyuvm4ecFxRfC69wpvaFVDkc7apX78u9Yz7TCB9u9Vx8zhJeUBZ0i-_h9GPgylBjM3aywvcSCNMYn7PcvQk7Q1HjeoU9akQy9KT9jcCwFh3h7BY0dOz2veCHeiCPoiFQ8WYMxTu4PVWSqDAYlatIlF-9rQezlyUQRGARK1ynkW_x0zcWHYlCfGiGnAcFhFPBafyAHWk2xmc-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=VLxE3Pxt7MVOFYbszoUVooaGVoL-i6NT0aqN-KK6T50aYi7LHB7MaMnY7lLSqKhnNJkw0jUncdEHjqWoy6Z-6EKGdoqwDk7d56ed8-SZs_b3BjAJdR-sHgvQW7dMaMUxAncQMGj3G-jGrSd3UBQQTf29mi_YbDbXjADpq2FdlyKEUKvO0HcimQEYlQJWLEVgB6eUP9syO_qUmQQqrmGvwp-tsZcEDwhllRygP7Ow9f-x10NO83fj6Ony1eJRlDonHG7Jp__V0Wz0QCEki03VUsWHuT1g6VgDdPTyNgdzgVFIbb8_9iCBh47vaGmKxQNyrj81F_h3KBnfOwjhZVFJLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=VLxE3Pxt7MVOFYbszoUVooaGVoL-i6NT0aqN-KK6T50aYi7LHB7MaMnY7lLSqKhnNJkw0jUncdEHjqWoy6Z-6EKGdoqwDk7d56ed8-SZs_b3BjAJdR-sHgvQW7dMaMUxAncQMGj3G-jGrSd3UBQQTf29mi_YbDbXjADpq2FdlyKEUKvO0HcimQEYlQJWLEVgB6eUP9syO_qUmQQqrmGvwp-tsZcEDwhllRygP7Ow9f-x10NO83fj6Ony1eJRlDonHG7Jp__V0Wz0QCEki03VUsWHuT1g6VgDdPTyNgdzgVFIbb8_9iCBh47vaGmKxQNyrj81F_h3KBnfOwjhZVFJLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=AyGiSPWGTajsHTFfBBWY0Bv1ZeOBE3etkUx6SoMDkGSuFevrlP4XkJxRLUjhF_raLXyrqJ0YWXH-lRM3ZekpDaCn2Lampid-XO1kwAIeY5OaNxBu3obX37R_zpnGjDQhFZJSP47KB-kRp_6HYVSkLzPsc-kr9kT9NNF40-dPdKpadVTftNVC1u2vKnRnENZgZdQ3Xs2gIH9PkZv2FxRuRJuUM5erBwAwBkRM6XyjDYG-XmPOt5O2OBc-rx1Gcdw-Hcfpp9B5ywmjOPYFyaUkF6nP-EHZyZ-utBaX6CCH7cCTB60YinwD2J65VUWm9AwvocOHa7mwYgyRUCHsYItk2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=AyGiSPWGTajsHTFfBBWY0Bv1ZeOBE3etkUx6SoMDkGSuFevrlP4XkJxRLUjhF_raLXyrqJ0YWXH-lRM3ZekpDaCn2Lampid-XO1kwAIeY5OaNxBu3obX37R_zpnGjDQhFZJSP47KB-kRp_6HYVSkLzPsc-kr9kT9NNF40-dPdKpadVTftNVC1u2vKnRnENZgZdQ3Xs2gIH9PkZv2FxRuRJuUM5erBwAwBkRM6XyjDYG-XmPOt5O2OBc-rx1Gcdw-Hcfpp9B5ywmjOPYFyaUkF6nP-EHZyZ-utBaX6CCH7cCTB60YinwD2J65VUWm9AwvocOHa7mwYgyRUCHsYItk2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efix2Ktf4VQA6bPSPK5e7Kje_Dwl3drA6l7umMv37QNefgVbNtRTSk-1UdFAi3dpXOdMk66D5-4E_nTyWX5fSDGQnfsl2bXqqYSAXr6TOtBPDMrY50SE_tesYEkMxZeXRSjrux3cVkXtzPUH86Q-qaZrNmLjEyvUUgUNrMo79hrWF2y8cbARAO-laVDnv03yC_GayIDORy42g6OjgNVrMmDb12JvhmPE5YLXJp1u9Oo_dAg9sQ27snY4VojcW5bZY-Tuq-vtCykAfdK9rdyJp4WD535KYguTKsGcLvmvBtuhQUTwKEftALRkD92fllVAmmqNjAj__ayAEbUWqHBlHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swaHi60012p-vmGdv9laCPxsEXUTsMw2UM8vaCtHtTgPD4djnoyAgaD66x_2nB7-XCrxR-ORhMw8DgAtvHgVZ4gI2I61VxoxQD0m9F9lhSBMumraDV_sBUC4bd3qCV-4fKFfx-CtyeDf-zx9wyMSdeqXUf2I9OhhYG0BrfU8tmRtcdlqjMPuHXyDDVJl_STIeOKBjy9cn-svy2RNRCQI_58AFzH1uCoYY_IYFIH5JXmH4iLhnbAedqeYl8GWXPYVsR6feBZOtwVBeH8dPGHX5VzHKq1XRaUJQpXoDqzybFtYp-qsk0Rd4066GaoUSM7bfNaIF7BCJHkcQEUx77TTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
