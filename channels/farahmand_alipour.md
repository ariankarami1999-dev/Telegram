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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 05:15:07</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIinY0MFaAW6k6z2K3hUb0170UpuB2heigF5UcSdeuS91zQJ5vy1GubbRec2t-dvqz_jKK4Qm4tmjSs9x6x6lzsJIhnTw8Fk_bHjWJPhNH4x4Oi5LjugAiWnjCj2SHyr3k0ah2QYyhWysAica4RerzIkeP1l4rw5sar9hEWnjCkP3iElB38-lorz5xlaRsyyrbyC131O0D9I6NY_cmVtCmkX-WQkSaqlYsu1o1xo8gitEj9A6LaTEebeMXX3VBWgyiqTcZzLAZHa-Dzbdsxp6pBmECf5f6qAwfewWsKdnbkq5t6fZ4chpgkHzVyAFfMyQKcsgoT5JIcFDZDN6N5IsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRJPVLvahshFW0k6cQc419bTwku_x39NwS7WiGVBNSSnpozd2yn0VvhVte2Ipg5wmBqco4gJeOGfE-f4L5G__XrTrnkVyWM6l2TLPCbR0eeFdv7xfC_N5klzYXoiz-MKlq2o-LjwAzVdZQ8qYnggblArunLF3tfF2WgZxFBdlFRv98BiJq6OJcmmZ31tetKHDtOneBa7qaAKf-BCJLDftAtP2XUHlpaEwvvKJHeUoENbfJLQr43BTg_TqW8eMeSUOd96x-Qu2jriqLOO6r6AmA7-OsdfndoHCqgWJBEJP5xq5ydWICBI52ltCgNnmo5Jw9efDx8nuEk628Coj91SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIYhK15Sh0cGS91laW-EHNkwXJ1erUyknj2kwnWuYQEnWK8Ra6bD5C4JWBbpZhG6G5N92AdhONmky-ExHQAM3nDvLeU8cw_j4hg1GONC33pEVwyjHIWvcs0MjRtCBDTNItnTnei590jAQeTHI-B2qtDZ_TansdeD7FCTBMCcpXn0dHHvJCMPitgdUJPxBw7uFC-6gI7IEzgcWXIUsWEe7uAXnfUL7HrnZ0QTGY8W8ORvusgJ6onnHxRNH-VjziZgQ6xdGuaQvnn4Yl-1dbw7ysf89H_hXckK3KW4jd-72JbVem_0rYPxGiyugZp6kuN4M0Ci_RZWhTesaXemaAebPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kk6UzVHiJ5a-wdt0SySHcSrQ8Y-4lxQVZTO6H2iQzaRkCpqU-5HA65T3835alxbJElUi4teeWwwuGK--Uaj-E9VTOP_3YcZWEVx1Zb8ugOZ01F4MUCqjLb5ZSgcGH823Pj7GN_aQS_4_6MZ6wKoymD_gRN-Lz6DcdJkbBoTPNfpbeRpA30GGt5fGqzAHyLQiakSlhzVQWVk_y7sBwpe5c5zAkXKZ-9F471rtEgj-oMnS0fPeHQyH0TzCT1wcyemKXXq5yeL0mzki0WjVLkBsBUc7ZPpUZM6fSWI22_grsYvtYQYWnrrthHcwJp37YPKhnRVsVLTdjpx3K6JOKSkw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3Qj3kf-JJzINr17Bd4aFUCxfE4RNS74s08-2sj1vTt1Y68KO7rkOl8bv5Nzr6Dxpy-VSDZqbC-OgtuwHMXozZsPT7b3O-1gIW4parsuZEEjsYqAx6nrAQFNYpoyX19IC4psoqsnlqurvaZxOF7YRdd63iLoPo0N1BY6lFHScmTesRFSIgicaurVD0fJufELkf32dI5wuk03y_Ezw88HG90GhfPHercRsaInDzNgSuDYEF6VanyYR31UU74SA2PqN4sRfq9kzt07ZSWG-01uj_UEuq4NE5e-toJ1_WHK5g0cxBxflg3z5WOik3uG6GNQoRzm9ZLe02dTJzDPSgM0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgSKtERFlk7GeVHmOibaVa04Ek_gRAxDA09ET419nXzjgZnndD1_lSPx5vI7X0iA1bkJGuPSXaaBDoRMbh2bGf89RenuHNDrBXrYeu3whlkmTpYTXCls9Cs-2NyKW6P_2ijn2BFI3QCQ7XEREsy0WVKHR2lIVdLZviMzo5tGiIRyV5QHpjvMaupkOTwKai5wLr2Qi5zuA66CKfj9Oz2J2i2fRAKuNOjnHT6BPD6kA2b_45gaauXjUXBFF0jtSnOQyUwo0AgQUie6K4EExUKLEh79O6p3K83gsooTPwv1VDQ2fX5jPQmmbouBLU9jssIYCrGiPYFH14j3DSFiLNlXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBdeWNzf9v2czF2d-w4ILsENvZZaBY7oYT7T3MW_SMR-9JwcyjEJfHkUQh801LPyYGwrbOs1oSwAzKxmR5OJZdnUbp21v8rMaOV5_XH-JE2zpG-okI297oV1HBmQp6Nyav32Ts8LRUsXD3b3QN_w2nRTbRYSUUT_uyrfhAz4lXK9aSz2OdpjJcYYROp1ffwmO8kIe31DNn6Y9xaVDmbulXfBV942xlTxfhe7NhPVxyFEfxG1lZBsRj0AuuBXUN3Keex-qz1MruXuVHthv9HEC7-DbCkKAMOg57jVMRIbx2Gjlwn-JI6OWqYoGnQDzjoVWqezF3qjWNzoDPc0mcM_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgq5-bj90lOJ3EZOrEqyh25aVxF6nFKyIg7DJh9WYa3gNmh3eBkTa6jhQrq3mXJOHJMkx9st-q0sfnPwC0MigaeGEcMI6zj4Tz53rCOASxLXSCdFpK9KRUo9m6Ux-71fWfSGe34nvy5ZAXATURUiScrGPXFX54TA5_q3D4sEL6EjR3-1CnjB2HCAVx07zqfVQaajNFHXXNB-wjYuztOAokw-V0XswRrNCxkdJN1tpwZKmtsDzwbmoYjrJskysJtDcCrC-thGD8d2_wpzQDBalA2CHK-NZjpBM48wA-5uacfNbdcTeMYfnBRumXpNSSrdvg3sIeNlwUYndp3mmQSWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z14DqUyzcDLMh8ROn6n-yBOv8MaR1Se43nWVZ8FhzWfOtRLwGP8APzHGIazEDHKlqOY-flR4SbKb9l8gJ9EE-756Y9135rGhYPtvvOjgW3lhYUr1lxieB0pZaSCpojDX6SAUr2lKV_MW2zEO2VS6MD0B3weX9LzBq0iTFHmW3WblJa-kviI2tciKRisr4mEd8kTbvztC9_M6RDgh99nXZnR0olbwkw0E3VOTl0bsqTO4BPdWRsBN5EeS2TvuYM2snjUIv6OvJDjzNWeTcJvFyA1_sDDtOFExCH_njdde27USsc1BgPECfXm4PIBixP2h7z1_hGOkBCScSTozgPYZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adRz3-2w6mQiiUOo08V7YSgkVAHlQHYiLZ4VNw0VGEPyi31OxK4m_NegFPGCor1mhENBjjDhhpkK1m1FEI-ujToZnz0LWIJ3uheyOH_FtMzt4vw25vtPr9JfO6IOnyYalOqakQ1IM9IZfYPhZev5nbhSvfDg7YCT6w3phHifqnFEDKfdBtqOCN3ajD-vdH0NZhy2hspPI_s1u42UDJWsWBU8sFotrZaNlh-xmCMtEEYylenVUwok4LCao1S-p_Vxv7PJyapHjRlto-WfyWzfJ1pJGJM9y9xd1SbJmH1HqGBHJdAVKdXVgvgt3h6q4WboVkT2L-PKk4n-wvxoW-xAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2VchZg_KIe1nUsEPl5XuMt5ion6kWkkZ6STBX2cTHaRUPPQA2m7ZWHdrg40e-uuFSiUdCiFNKQbxxlXp6SHOURkCEHlS9HSCeCzA_1wtTfrcsAYcZ7b8PZbGNYfA09NMnsZrL838Yi65hVzvTzLK0xSaovujQD48G2LDtEPRB81eMmHW1nz1DAgofZZPbwps6XFWCC2q9d2Sub1tnnP2SHKUkg1ojn8ZKfO2ivTiYZnz6W7k5sfJCXtXXNU4raoOINQeRrOzvjaQU3mqu0LIN6Omtyb9MYjh6sZFM2DCaaR20tspfroRyQsOHAjvGkyWALy1JU1eU3OX22jobNVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2XT7SAcOvHN2TvfAOhQ7qlCmXZzgjSL-gz66ArLCsA4wu0PB9tDX0NlocguSyc-qr35uAflE4-NFZkbIoyJoGYc7PO0OrWbHrIgoMeQKPL1wUU5P2oT3nzUfweFrpmXFXqv2hNX8KsWMNqIK9-nxV5gK40VNxws7U53ILclFUGqW50RFdRIWFisjMmT8fGDpLXnvLkWRaS_BvfquHdmjPzdAr06Xx6Fi_DOwdavAijfeFoXaelp1reHD6x9TZUSQZsrQq93WT_AOk3cuz36zIQevya4mms2DFvqPSzWHvEJJxLqH615TTbhqSRZ63Ta5xRoxvIF3mRNPLTZemU2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=UlaYoaIzlRzrTQDUpFS7NKJSIQJtKvdKPxZSCBj5eO_Ie994k2Qkd-JWf_6hkft_w45F5yekGWR0zap7XXVkIIe6k1Q9TQK7gQmM4vSPojQDlT00ZlDSj5yEDrgoW8HNe-yBfCxZcX79S_wk7XKpgoEUWmw7Ck1R2fL1PtWIaG89231GQ3QD7UkaLoy0s4Ww_YU8OOydvjLMDoQImxOo00Zx5rKPWiFTxEKLGTfh4kyF_NzSrmU8h7FOvSfcKNKQoKeQCpKz5CbZ3wF031zn_MGaCjejlULPNYAI5v3PQrWZ9bmV6xgrsd_wVA0PXG5eGnWTx7C6REm_bBnzp_qH8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=UlaYoaIzlRzrTQDUpFS7NKJSIQJtKvdKPxZSCBj5eO_Ie994k2Qkd-JWf_6hkft_w45F5yekGWR0zap7XXVkIIe6k1Q9TQK7gQmM4vSPojQDlT00ZlDSj5yEDrgoW8HNe-yBfCxZcX79S_wk7XKpgoEUWmw7Ck1R2fL1PtWIaG89231GQ3QD7UkaLoy0s4Ww_YU8OOydvjLMDoQImxOo00Zx5rKPWiFTxEKLGTfh4kyF_NzSrmU8h7FOvSfcKNKQoKeQCpKz5CbZ3wF031zn_MGaCjejlULPNYAI5v3PQrWZ9bmV6xgrsd_wVA0PXG5eGnWTx7C6REm_bBnzp_qH8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=htsxvtqAYwPo1NeEFcbGq7xlbPDOII5UcGSBd-S94KDAtdp14bEh9IdtgmcOWazyuTRmB-kigm5ZK0GkzxdqrMp9HAsJPclrEbDW2Wvcoz5RxtE5yHLhQjEA3j7pNaIz2v96IPu0PKLMc_Xj14ovi4jEk9a9ASFMaiDgHwBg04_yvLLJLs69RTwbuDFi3yaey4KXpB5V-OVLrCrZ64NHtTuXr_NRoLfzdAv3x9ko1op1kkLNn1FK1DiJ5GT4DJUzkmZJNJKohF_S2VI1IyRUA1T4ml17B9h5xBTKzT5MK6vxof7GTCLW9E2e0glZopj3ru23abOZonDG4swYPG4YhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=htsxvtqAYwPo1NeEFcbGq7xlbPDOII5UcGSBd-S94KDAtdp14bEh9IdtgmcOWazyuTRmB-kigm5ZK0GkzxdqrMp9HAsJPclrEbDW2Wvcoz5RxtE5yHLhQjEA3j7pNaIz2v96IPu0PKLMc_Xj14ovi4jEk9a9ASFMaiDgHwBg04_yvLLJLs69RTwbuDFi3yaey4KXpB5V-OVLrCrZ64NHtTuXr_NRoLfzdAv3x9ko1op1kkLNn1FK1DiJ5GT4DJUzkmZJNJKohF_S2VI1IyRUA1T4ml17B9h5xBTKzT5MK6vxof7GTCLW9E2e0glZopj3ru23abOZonDG4swYPG4YhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=i9VI2d-eksIj6HOvGPwXSRdxoVLZA5AiKYwolmlx7A8j_2rXh6oJyfMkUeQG45DQmxEUgKE2m8yhguvFfTdtkU4jwIZ-KMbnLBsphC_hw8zaUNIRmGS5VdvrL0d0K1wT5Ri1px45W-HH464k1QKrTli8JBchshGV8bACBtIushFQSce8mrDaHDs89SYEP_Dl45JiMdrDEoMDi6OmqQSjOAl7pz3tc-P9UVW1QU1GAWcQWY7G_n2nscktFNUzgFILRPGMut1tsKnWgNE--JXqUjblCXOuyIEr2aNC0GBeYGo0AoOKGI4UclpXowo_UxCNxp0Ufzt5BNchrhQeb3V3SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=i9VI2d-eksIj6HOvGPwXSRdxoVLZA5AiKYwolmlx7A8j_2rXh6oJyfMkUeQG45DQmxEUgKE2m8yhguvFfTdtkU4jwIZ-KMbnLBsphC_hw8zaUNIRmGS5VdvrL0d0K1wT5Ri1px45W-HH464k1QKrTli8JBchshGV8bACBtIushFQSce8mrDaHDs89SYEP_Dl45JiMdrDEoMDi6OmqQSjOAl7pz3tc-P9UVW1QU1GAWcQWY7G_n2nscktFNUzgFILRPGMut1tsKnWgNE--JXqUjblCXOuyIEr2aNC0GBeYGo0AoOKGI4UclpXowo_UxCNxp0Ufzt5BNchrhQeb3V3SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=i0sISG5zh9XXBDdx4GiBU-SKhFSHBJPjaAyMvqBDvsCNnX0JDLckxlHDbwILjbHOAb5rnHap7uQqniS7VgMzqdc3P5BL0T9KSBqNYH8q-98VLOOjmiwxlJib2ieI3NVXyHXLTQAv6OsWuIXZJwFDHjZRFkdyCZ3pHFyKffUYXgh0DPYFBK592qD_VRta6ywhcGOKrGQeEU0TB_ia4_XwJiaNwhJ6e65v5rImLQgdvv2XdP8L4_vvpAq1W0t44uL6hXutsQmGYzWFcQl8co4hq3ajni3lDK5AKUgePDSADkye2NAen3o3Rc0AjmdMs192QEXYxShDg_9PUHDsiU7ibUNdQ1F5468P2UV-RcdcxrBHijXTNmbI7y4Lw9Ag98iP2hK5LZoGh3pkedDrVAdQ3dQf61BveFQe4KC6HOoaQqygaAkO-dzUpXOtyjeRtnO2i9h7yrY009i7dIqyRQAawBpXRxmVP6rljI61ipLNURu3T9LUaoRliqt5m92asgt51nHItYSYgX5wSWDsKzrW6d84949MdhE0T7sRs-6v6AC96PEcD7JayoZGZT8wEB2CbJRFPXy8tZDCXb_1LAv1qvBBBTcnFhRrop4Gt2u23tFMcSNbEQ3ojpewk70DZu6BM64CrjzGdUHkLliD1ps2onoTyWFJwMgTCoUqgAiDdfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=i0sISG5zh9XXBDdx4GiBU-SKhFSHBJPjaAyMvqBDvsCNnX0JDLckxlHDbwILjbHOAb5rnHap7uQqniS7VgMzqdc3P5BL0T9KSBqNYH8q-98VLOOjmiwxlJib2ieI3NVXyHXLTQAv6OsWuIXZJwFDHjZRFkdyCZ3pHFyKffUYXgh0DPYFBK592qD_VRta6ywhcGOKrGQeEU0TB_ia4_XwJiaNwhJ6e65v5rImLQgdvv2XdP8L4_vvpAq1W0t44uL6hXutsQmGYzWFcQl8co4hq3ajni3lDK5AKUgePDSADkye2NAen3o3Rc0AjmdMs192QEXYxShDg_9PUHDsiU7ibUNdQ1F5468P2UV-RcdcxrBHijXTNmbI7y4Lw9Ag98iP2hK5LZoGh3pkedDrVAdQ3dQf61BveFQe4KC6HOoaQqygaAkO-dzUpXOtyjeRtnO2i9h7yrY009i7dIqyRQAawBpXRxmVP6rljI61ipLNURu3T9LUaoRliqt5m92asgt51nHItYSYgX5wSWDsKzrW6d84949MdhE0T7sRs-6v6AC96PEcD7JayoZGZT8wEB2CbJRFPXy8tZDCXb_1LAv1qvBBBTcnFhRrop4Gt2u23tFMcSNbEQ3ojpewk70DZu6BM64CrjzGdUHkLliD1ps2onoTyWFJwMgTCoUqgAiDdfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=ZTcmzVI6U-QqcajRLrY4E3uAR5azFaQF41-wq3cMmyzGmhODTqzJSZzQLi81kkaolZTJby1904aAPayg8exkecAglepDArdow6QdmEJpOYGG81IYKKIKc7knPd0ij_WsqSBm3QhpcP2HsVAea0-sOmLmmUBbc1CaaBNclPwFPIe6Lker-kSvpPVYmLiXZEFuwAwhQSZGqfqStbJDP7xBGE5cOO0tJv56pQrBl49Z5BnQMaNcSmo8XLrv4R2t0uzeBmM-amh8g4RvpR6w4Zw7b798VzNMWh0ayO_7bsoaw9BFWJw3628pmdmbkEnIl2CiTBQCTeA-wMTq9vsT8JSzSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=ZTcmzVI6U-QqcajRLrY4E3uAR5azFaQF41-wq3cMmyzGmhODTqzJSZzQLi81kkaolZTJby1904aAPayg8exkecAglepDArdow6QdmEJpOYGG81IYKKIKc7knPd0ij_WsqSBm3QhpcP2HsVAea0-sOmLmmUBbc1CaaBNclPwFPIe6Lker-kSvpPVYmLiXZEFuwAwhQSZGqfqStbJDP7xBGE5cOO0tJv56pQrBl49Z5BnQMaNcSmo8XLrv4R2t0uzeBmM-amh8g4RvpR6w4Zw7b798VzNMWh0ayO_7bsoaw9BFWJw3628pmdmbkEnIl2CiTBQCTeA-wMTq9vsT8JSzSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=RMF_-ZqnnUoG6PYNLLUuuRXNq_fJqzOJzGQ2zpbq5LTIlzOnY3eB8VD7uFLMJj0a50m2jG6HHOP-qVlFuuxPczZE9BGwbHyQJO2GrH_cZt9nVxu53-7sjDFbxHjSWz5zF5Hy9tIQZuebuS63qD_AHTpoP21hWCfqyGm_dYUybYRnQgAgXJLTuXEGCKPhYWRWAfvwGhO5HsgK3WWUdcZOs3qKI_in2utis2WHPs0ffz3rd5JtMHCFGdMW9P9vwtU0prmcEN8ru3BDk04CBdA8DoSEL4dTQ2DW3QjNfbq0J6xKLetvuazf7RQIOTZofWS-VCqNrkKJP-geLaeeO0QBUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=RMF_-ZqnnUoG6PYNLLUuuRXNq_fJqzOJzGQ2zpbq5LTIlzOnY3eB8VD7uFLMJj0a50m2jG6HHOP-qVlFuuxPczZE9BGwbHyQJO2GrH_cZt9nVxu53-7sjDFbxHjSWz5zF5Hy9tIQZuebuS63qD_AHTpoP21hWCfqyGm_dYUybYRnQgAgXJLTuXEGCKPhYWRWAfvwGhO5HsgK3WWUdcZOs3qKI_in2utis2WHPs0ffz3rd5JtMHCFGdMW9P9vwtU0prmcEN8ru3BDk04CBdA8DoSEL4dTQ2DW3QjNfbq0J6xKLetvuazf7RQIOTZofWS-VCqNrkKJP-geLaeeO0QBUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR98TlhdxKbeRTwfFl6PGKgXgbXxMTYco0cHw4BU2PypYorWvQEDQV3MK46VNBKEq9miOb49IMl0Io4KF6-uHm_-MWDzONh_Ahvt9GZLGzxEfsXdxnnaS9N-jxZxCiP2SEhB0ir7LKdrVmKQ2c90Yqjjk73gHMc_v2SybbBsmSa_eecYfUN0lObjw4_m8jeYlMeoiFPmgGbZsxmw8z5kEMXmRETKm_dOBBOTx_t44jVpLeMrmXOgS1W8ooMHrYNiAoqMwog5q8EPfX7TRjU1fqy3mIEDExiGJ-2dVSyd55jlzeFs56C4djxcMgqZHAZcquCmVnj74U7N9e0qSYzKEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=V62aqkqVYnMv2ZUVt6y-J6-6Z9iWXSvc770Arx2BGFTiBTuZXRjdroecY1asPjfzaFMYeO56LBxQX6WNvyIbsRPGAlwriq7Ku4dA-TAVnhgvr9LbEhHj6kmHBY9VTeh1mBysPc2wOEZB_iEKLaexQ-LK-GnRcQ5ZzZN4O7mjZfZjn1UBIW-x9wlujbc30sOp-llDZF3EX9S8zdH1Fs-I3P6DjvI1QfhtEFMcdMGtSmszqjAg_sYatCaekxZjGyEnEijML3EIXlLCCSXEVyH-Zl9sc5dQOZyDc7rIV8Hz2kqbYEtPA_A8fj25QqYijLnpihwr6G3omxuktli0K85naw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=V62aqkqVYnMv2ZUVt6y-J6-6Z9iWXSvc770Arx2BGFTiBTuZXRjdroecY1asPjfzaFMYeO56LBxQX6WNvyIbsRPGAlwriq7Ku4dA-TAVnhgvr9LbEhHj6kmHBY9VTeh1mBysPc2wOEZB_iEKLaexQ-LK-GnRcQ5ZzZN4O7mjZfZjn1UBIW-x9wlujbc30sOp-llDZF3EX9S8zdH1Fs-I3P6DjvI1QfhtEFMcdMGtSmszqjAg_sYatCaekxZjGyEnEijML3EIXlLCCSXEVyH-Zl9sc5dQOZyDc7rIV8Hz2kqbYEtPA_A8fj25QqYijLnpihwr6G3omxuktli0K85naw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwtPyXg7KhlbBMbxqa_RCdMGC3E4o7mM0ehXNAwxJIvS-nat5C8Eh9wGMxMF-Ul0ZlgGb8i-HOnF21Mx8011disWXDrHylyx70KRCKKt1W_waOJCCKPYVydQYKhbnxmQ3_keQlVtttHrp1t8tzE762Jq1I5nhrwqjyJ6kSln14cQ-3Gqb61m7QZus9hQin1BDN4WVJrBwLh5IKUp3AWYrog4Gv5_mZ2KeZOLd8-Q9Y7D4gtQZaukReX6Senu7w3TswIh_Arf6BFbKi7XTchHlz6QoyCK7ziK52dcB1x2vnDIcBV_Bkrr7PYSEb5Gh1N6VjrxyXpO2wvE6SJzDFgS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcpJbDmt2Jgss-FTxAqsC3eAVlOqpjZ8uufIq0VHoyGSG8SVk1hE_HuYk30GbKYkTLUaf7zNPQYR1i541JRwEyirfuxKc5YLRHYOlW9a8QYpliPRxSWLLoMt72FP5rUDJYtJ6ZO3kaco7IAB7uo1sVutsZQgNp2YHzIQW4oiA72p2Of5aTSQAjS-kRPyLA2uPy4p7Ye5GSpDM7TydlWyPJoBJ0kDUQep8c9qLcv33TbT8_wFTJYfTNugxq69DLOdRPsEtJjb3ra_3q8CqEdI4lSTzK8zoWHNsAn9PteUdZ8ubxwPwPuhjbyenaKlU_N_7oR7WIaExcTn3MUYYTt33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=CkR7AB7gqgTIhXt8dx0ZN7Uqy1LXtzYw_YClOBmE1DjVE7rDxmtXcB6Zmw9fwfkMRUQ5AIZEwlJOVBg9Ql7XGi2PjtteDh_rlDj302bf01hfIZAAm_07AIFsTc9RtcKMVxOhQrpiav0ZhInUhkn42ySRuu3rfvyge3LeVvx8mrGoMGDUsI5bjbQ_og1q6gi9skWp7UTZxywTtzCwWkoHKbBzXh2ZVn2QxSo1DZQuOS-iA-nOmkXtg4bdYPcJhfpeebZ-rLeyfV0XRs5y3sL9SMLCUICO0Ld9YoVw1q47G8Sm69IZ3wAHsGAE1cxqSDCK2fagaA5AZqsID1SjxCvPuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=CkR7AB7gqgTIhXt8dx0ZN7Uqy1LXtzYw_YClOBmE1DjVE7rDxmtXcB6Zmw9fwfkMRUQ5AIZEwlJOVBg9Ql7XGi2PjtteDh_rlDj302bf01hfIZAAm_07AIFsTc9RtcKMVxOhQrpiav0ZhInUhkn42ySRuu3rfvyge3LeVvx8mrGoMGDUsI5bjbQ_og1q6gi9skWp7UTZxywTtzCwWkoHKbBzXh2ZVn2QxSo1DZQuOS-iA-nOmkXtg4bdYPcJhfpeebZ-rLeyfV0XRs5y3sL9SMLCUICO0Ld9YoVw1q47G8Sm69IZ3wAHsGAE1cxqSDCK2fagaA5AZqsID1SjxCvPuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=WDZqEGOBlkKvqHLWEL_e0sQTRul-SENYOBKwCHuz5kib63XX_hdNsqX7hcEInJKmA_D4ve8mziS176JFCpjcTabu2KSQSVrU09Edp4Gc1FGJvsw9Kr15Qo6sNczO8biKziPilgMSZe4NMf4NpPTZ7O0JIikfmNkRmajhu5ZUVOz7uENumMMKkJTHFWUlIiaMl4zB0NNzf8-8QyhDFiCEq4gZ5HuJNvV7dD6quiH66Ul_Gx9sgpoi4dBIMMtdTS32QgVuL-M29rvfCdgdgZbBnwSQm_mgUxnLfAvdP1kYITVT28HBFjHG5xocy0mMQgx5C6az9INv3VLFkBMMWi86xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=WDZqEGOBlkKvqHLWEL_e0sQTRul-SENYOBKwCHuz5kib63XX_hdNsqX7hcEInJKmA_D4ve8mziS176JFCpjcTabu2KSQSVrU09Edp4Gc1FGJvsw9Kr15Qo6sNczO8biKziPilgMSZe4NMf4NpPTZ7O0JIikfmNkRmajhu5ZUVOz7uENumMMKkJTHFWUlIiaMl4zB0NNzf8-8QyhDFiCEq4gZ5HuJNvV7dD6quiH66Ul_Gx9sgpoi4dBIMMtdTS32QgVuL-M29rvfCdgdgZbBnwSQm_mgUxnLfAvdP1kYITVT28HBFjHG5xocy0mMQgx5C6az9INv3VLFkBMMWi86xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=tOKHPahwHA62qv_YOtRTyNvTu6A99Jm8gWgJG8KtVflVvdCIn_ZStjhB_GsytPBovgYM2gSRSsnlhwG9P3fT0-BdZLCr82yPCeex1QOMgINuqXf-ufhLQZyk2S3THgnogU3-o0RaQ0-F0uh8qq7Bti5A-7LF24DeZKb26YQAzA4hroIRzznIWlIS67OIFnt51qBEHBm7t3fov9KDhL0XhKY1ffpSs_KUvJdR4Kicc15IviltVvDk5MsmZEZlndHiowb7g-Vc7Sqi6V2KMl8QONISJLAHOK57TMcVlHDdcwfl6rsPZ7CgJEawO6-mFa3Qp2xS2PtRYaaLZcgwmQNU5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=tOKHPahwHA62qv_YOtRTyNvTu6A99Jm8gWgJG8KtVflVvdCIn_ZStjhB_GsytPBovgYM2gSRSsnlhwG9P3fT0-BdZLCr82yPCeex1QOMgINuqXf-ufhLQZyk2S3THgnogU3-o0RaQ0-F0uh8qq7Bti5A-7LF24DeZKb26YQAzA4hroIRzznIWlIS67OIFnt51qBEHBm7t3fov9KDhL0XhKY1ffpSs_KUvJdR4Kicc15IviltVvDk5MsmZEZlndHiowb7g-Vc7Sqi6V2KMl8QONISJLAHOK57TMcVlHDdcwfl6rsPZ7CgJEawO6-mFa3Qp2xS2PtRYaaLZcgwmQNU5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYQmjUz1H5bYG40HqGy5-Az1jmfSRSWnXGT5M5cPxV3djWgdWn42KX422D6oAM60GM9h7Zr5ub9SveJPe_yaLaY6SOL4AxahPi9VPH8T0nhEsMjYJueqr5ltcYZP-VjfhOKyXeeVAYpqLcvILEm1JAvrXeNMW07VJYp5c8VqI8W3--FHjRsUzE862cqtXSYqXHV3K8YroH85h4M5jPauR7E4T9VpVRpdsVc5K6E6zFAveob6i2laMFeoXX3KO3QfQ3xdUUkNh70EjBJUu3Tw7EgBOycBndYnMdOvFjh42_YrqQXSUI9nSUcsTAFqQYGsi8dKlityqO-mQaBErPES-g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=daRmU-uAxmkB8InzHkSHGEhMGM8KWA6vM1BkqRMcFib16X4FfJbcNWhOyuuDp-ijUt8qzFhHK16MZueTuCoUBbINWj51uDqjLOQgnRNrnuSy9KflpIDDvZfHHv1_XYC76Nxq_TLil8TpEImJykgmWNdbHBY1bfIVf20iXcN24etDMtxHeOLGTHcZsGKAS7P4_WwgSnvyTAGKXg0L-_FEJeY_xG8BcbY4SHmTaEQ-cKo00s42rvOcOmiJm8dWWkevd4OtE7X49_Ob1Tn2ys_kgRhbHdWtN0UTNLxgHDmfOz77UwNSsLyfT22iXbnRd8e1pX1sD9GnL-5Sq5LCqamjGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=daRmU-uAxmkB8InzHkSHGEhMGM8KWA6vM1BkqRMcFib16X4FfJbcNWhOyuuDp-ijUt8qzFhHK16MZueTuCoUBbINWj51uDqjLOQgnRNrnuSy9KflpIDDvZfHHv1_XYC76Nxq_TLil8TpEImJykgmWNdbHBY1bfIVf20iXcN24etDMtxHeOLGTHcZsGKAS7P4_WwgSnvyTAGKXg0L-_FEJeY_xG8BcbY4SHmTaEQ-cKo00s42rvOcOmiJm8dWWkevd4OtE7X49_Ob1Tn2ys_kgRhbHdWtN0UTNLxgHDmfOz77UwNSsLyfT22iXbnRd8e1pX1sD9GnL-5Sq5LCqamjGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ikHU-tMozsNS_cNx2HKMKsgZb4bqDGungIM1gsDjlkLKQ6fp4W6_pO54lnV7gJT6vJiGyxWsdhDaXMFoCsMWP7UpFXKz33f7xKKh07IKpGibJlofC17mWGZRIrNdzlFCtAILhVu9loIvPB92OTKr2PxKjiP5m6mVtlzVU4yjt33e5PF5ae3eIjV6Z7AFR4KE1AHkB9gT1v3W_PD3_8jAbmjduMKKK51YjkQilpd6_5KKjaghDOpkPVwFG_ekQebq9VJdJpDd2KSnBw_6hLQ3Zdggg6YB6RQpmA0YjmQNL3_PnBRixGeySm2HO4ka_koXEIO5-2EOVyCuwE35gE1Vig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ikHU-tMozsNS_cNx2HKMKsgZb4bqDGungIM1gsDjlkLKQ6fp4W6_pO54lnV7gJT6vJiGyxWsdhDaXMFoCsMWP7UpFXKz33f7xKKh07IKpGibJlofC17mWGZRIrNdzlFCtAILhVu9loIvPB92OTKr2PxKjiP5m6mVtlzVU4yjt33e5PF5ae3eIjV6Z7AFR4KE1AHkB9gT1v3W_PD3_8jAbmjduMKKK51YjkQilpd6_5KKjaghDOpkPVwFG_ekQebq9VJdJpDd2KSnBw_6hLQ3Zdggg6YB6RQpmA0YjmQNL3_PnBRixGeySm2HO4ka_koXEIO5-2EOVyCuwE35gE1Vig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=C5Y2UkP-h10pNUJlTv_GPA7SjV9kXcTzIaa0fX6OnL-ad_pM5ji1FNFDA9tqyDRFbylnz3SN8UmA4GJ2GKolAmtzyVXv5GFNaGetxLoki0i6QcbMbsPp9IudIQxoCyFAw6Vj5U-X407C9smR_vHsfk-pMfHh3v1B68TtYRg-4E1UwvTjPEeREUGksVFELDm5qt9-w4C8_HnTGY1M3toTS7g32kypY6gn81_WvSoa5iMh6pPkznkVz2s-c93XxzyJyWJY7LM1St-EwmCw4np2b17wu6Ajba2B3Hco1tMC4j5wMVXe9dXkEt8laUXGYw6QeaxoliVccE1WydaL835emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=C5Y2UkP-h10pNUJlTv_GPA7SjV9kXcTzIaa0fX6OnL-ad_pM5ji1FNFDA9tqyDRFbylnz3SN8UmA4GJ2GKolAmtzyVXv5GFNaGetxLoki0i6QcbMbsPp9IudIQxoCyFAw6Vj5U-X407C9smR_vHsfk-pMfHh3v1B68TtYRg-4E1UwvTjPEeREUGksVFELDm5qt9-w4C8_HnTGY1M3toTS7g32kypY6gn81_WvSoa5iMh6pPkznkVz2s-c93XxzyJyWJY7LM1St-EwmCw4np2b17wu6Ajba2B3Hco1tMC4j5wMVXe9dXkEt8laUXGYw6QeaxoliVccE1WydaL835emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3nVVPF61OgkiATNO-bOBoxhWNO1N68f1riCT8MmeYZRO0O36ipTlLPEdnoA6JPD74y5gxhqnqkI-fQqOyAsaXfuFiEN8b858-42yDYL9jHsxpRVTvABkbOGobyOMCyWdwOOK8kxGmrDTmMNVossa8e91BuxdiKwG6qgBDBbUubfcgp6ndPjqzv8jNmhwOE0pzT5zlntZhPPOFKMaYDg04Vqd67JnBWhEHUgr4KyesJDty0x88RG2R9tfHbNkkeuZNYTEc9pnZt1Aphk6A83vuUrhL2bShiWaqLSbOLG-zqJ9psVzZMxgWQf5VmKyZSOwkAbWIXIPLrzp4YB5NQDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ll1rCknwnJvMkFTIy5vmij2aJpveuYh6Vu9ZAoQQoaVy7FOT9dtcdt5WlUz_UjvUkqvW0_N3JsSr1ESR_VbFFKIXlRRMoEfgnqIP4N-epgkr-VAAxZxNl7LfELtpHRAw25oNBHtC2V9UId_CCm98R8Ra9qsS5OB_ai94iu8_ogJQ43hAlRWIjfQ2wMAmOkOuL9BGItHTEwWUmnIXbEcNGxgo0Q0njcju0d_zIsW39t7I2_2K6RGZMi4lnn5q1LHmEj-A45TEKaw0NSWYidLdmYz6sYtj05Eht2CXNYDlrEi_2lnkN4jCoy5BY35OdMnkrQvUeMm8UNwI1zCqWD_VaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ll1rCknwnJvMkFTIy5vmij2aJpveuYh6Vu9ZAoQQoaVy7FOT9dtcdt5WlUz_UjvUkqvW0_N3JsSr1ESR_VbFFKIXlRRMoEfgnqIP4N-epgkr-VAAxZxNl7LfELtpHRAw25oNBHtC2V9UId_CCm98R8Ra9qsS5OB_ai94iu8_ogJQ43hAlRWIjfQ2wMAmOkOuL9BGItHTEwWUmnIXbEcNGxgo0Q0njcju0d_zIsW39t7I2_2K6RGZMi4lnn5q1LHmEj-A45TEKaw0NSWYidLdmYz6sYtj05Eht2CXNYDlrEi_2lnkN4jCoy5BY35OdMnkrQvUeMm8UNwI1zCqWD_VaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj7_4_wFOUWH1WyvsRDGsySO4ETfvjb-rAgFDMp6cIuq1lB992oLui_Ue8qSyxtF9pivBkge1w4c3CuSAUjJV0eTL1k5YGtUIPy4d_cl8vduT_eblVfxkTTqsS86Z7PvY1T-SznG4SEx3ur1VxsGkzO7O23RBdUVqcZk6LeGvOSptaldcW1Gcvwt6hcQXFAyV6r-6os_UdzrIyj-csubcdJXjZ4EcdYf3fGA13jiv75UGefEuuVjPm0YLdcjM1ngAmFw3ktwCNl6vTjFooY_tPpeLT2YKLmDXTP5mBCyg7sauacdBOqmL-Xw-kK2ImTkAnj38AAfu65vUSwi0uo6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=qWcLXeC37F7R1Vac665yLiYgGxG5c8W1jdhj5F1Ksdhp2wWY-AUO_Lh5Fs8dlBukE-0lsv0iIiO96_zrRC62ZE5Q2vDr_rjYiwbS-ikz61-lSJC7B4lyEkbQBzvMSzx7Jd4dVpFV0zS6GfcGReHX8o5Q5F3AfuLxcG8k4kuuPL4ymkm4vnw6a7w3tJLOPcWCaEdcJ-QlKIzRMM7u4ekwa6Z5fIz1CyFdcIbYSxSvVKvojOmPq8pZ9D6vcUfYA2lnaKBGdI8hSvw7YZiPCvdOwf1H-tg0qe8tDyj59daAIx9AGvof-9o9svB3LeEhyX2pY-bOePS1wwyVUQv0XclFdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=qWcLXeC37F7R1Vac665yLiYgGxG5c8W1jdhj5F1Ksdhp2wWY-AUO_Lh5Fs8dlBukE-0lsv0iIiO96_zrRC62ZE5Q2vDr_rjYiwbS-ikz61-lSJC7B4lyEkbQBzvMSzx7Jd4dVpFV0zS6GfcGReHX8o5Q5F3AfuLxcG8k4kuuPL4ymkm4vnw6a7w3tJLOPcWCaEdcJ-QlKIzRMM7u4ekwa6Z5fIz1CyFdcIbYSxSvVKvojOmPq8pZ9D6vcUfYA2lnaKBGdI8hSvw7YZiPCvdOwf1H-tg0qe8tDyj59daAIx9AGvof-9o9svB3LeEhyX2pY-bOePS1wwyVUQv0XclFdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK_V8DhIw81KA2dMkL1d5GNxNo2oeZVd_lCEdzz5zV-Y4GBlWrYYpCG9G-qIUPNHUCNiI79xcJ6uwVk8CmZpzjijYM9HXxOqgyu-9QCe02NI69hwVUczVGgKFBox_XKJDtXUqzOFA1MhLItR0a0STnc7q5iH75Dnfr_jWdlOe8nyow6_opJGpll1NiBnVeWsX4rGYBRNkQN3tPbXezoLgXEbMYOAgJKHi15776cPdJI1jlfk00vB_EIjDeosc7cf2oE0EfEEjVmlfL9WAqRKQHZQOIWMGxq3x6h0v1AqR1XX05OeNzls1NkRG3AF3WO0jqyztPaEqWmBPdZZY1M4jA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=gzijsLJbDXOBIH8Cy7em8HE2-RvSHs1FrExo1k_bUYFS-igUDbTH50AJTugEy8teNWDtMvYWDX1u4vXL12nheTwzfw5W8zxGEUo4VadE8fn9wwte4aUoqOazVd1yLiKWLnoaGkDW8JA_KdBEbDngnhiIXD6i-YSpJ9TgbkN8605aFXUqXITCHOB8JT3yaqEC6Pyudz_zelRI23chT7JVEFPXoMfzhH1fdJvwYy6y_8M-7Eo7WlrCoRaeYB_kjb_gTC6u3GGOek0pzPjPWnhOX3xCWTPw50n5BIzS9D1DzDenxg0FkhQySrNLGl7vv-xbwpG4E-6xmlEFItlowXi4ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=gzijsLJbDXOBIH8Cy7em8HE2-RvSHs1FrExo1k_bUYFS-igUDbTH50AJTugEy8teNWDtMvYWDX1u4vXL12nheTwzfw5W8zxGEUo4VadE8fn9wwte4aUoqOazVd1yLiKWLnoaGkDW8JA_KdBEbDngnhiIXD6i-YSpJ9TgbkN8605aFXUqXITCHOB8JT3yaqEC6Pyudz_zelRI23chT7JVEFPXoMfzhH1fdJvwYy6y_8M-7Eo7WlrCoRaeYB_kjb_gTC6u3GGOek0pzPjPWnhOX3xCWTPw50n5BIzS9D1DzDenxg0FkhQySrNLGl7vv-xbwpG4E-6xmlEFItlowXi4ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2S4v2o7H2hkEHyipJvBwQie--He_i0sn5SaFFpyzKX844ROzQgsMepeGkIB7BJKxoLsUJezhRjebbgbKVvPRlsfvhOT17fYuYkLAJKbzNWjW8VePBkqoF1ISFTs5sGh9EPVjXlYQo_SJf9T4_nSRVW-shr_zo719RDTC4dGNs5pia4ZX0sw7KMEvzyww-GG4mIqmJULfJiGoTthDmYtYtNXoDS1rhjphED96hUBSgGo89vvvzSaKHiWOQJsaP3C_-ruVD0q3KNv0erIfd2BvIKbv7GHa1AEC2WrNad8ia7P9EUSo4Nl3VOSg54DAcihtTiz9iBCdjgTiU3PANy_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gxaZNHKUpKmqDdDZG7GjlY5qCI-uWe69WCkSQqqJaiU5Ie8VeA2c7nr364UrXiyDHQdXrPNfypgcr6STHhudxC1i5F3tOKNHgG5xOXuwtPa7KpcWfbuNNwl2AUofagkfFGywP3yaEqXK4Eg8j2RJiTGjrMYBU3r4uxCAfOnrlWMUjdvsfTOLKSBet_bFog0DCAvnBbj6JfmENN3-Qv4WncMGmlDuczFY9RwbIShVSORxn9DUhKglOYm72wh2jWmUqpO1IFMXP-yIh3T7vb1AoIX4Wy9j2P1T5U-ZDUZU-Ynd_ju71DaaApcWsKPMKVaqK8LvAhjUFeVdhYVU-gZdDg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=rpz_JH0tmpNp4HLZHF5mBcyGwlQezZCfHVpL8CThSTdwzT1rV07NZsyNrm4fewNYR-MtLcMPMAvKQdfY43w8h4DTS3158Mi_RmPXyGvAkNmTmOzCsdIBiFQdtO2w5PpR6_jrwqOiKEi0bCL2qR5CxTnGA5NzVvBBUS3RsJn9S4kX_7noExrccU2HD8OFybtRgzxuss1ntv7cE3hHzbu10d1Qbm39zUWSMyN8_PD2BRAn1Z-0ifU9YisZmVmga_qyeRPPSjeQtK19taChNscHn-hg9Pa7mqXzZKy949gIGDTsWsx-GNo1A22g6gkjFwUqqrfaDXCdiJ6GrDw9AtgSBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=rpz_JH0tmpNp4HLZHF5mBcyGwlQezZCfHVpL8CThSTdwzT1rV07NZsyNrm4fewNYR-MtLcMPMAvKQdfY43w8h4DTS3158Mi_RmPXyGvAkNmTmOzCsdIBiFQdtO2w5PpR6_jrwqOiKEi0bCL2qR5CxTnGA5NzVvBBUS3RsJn9S4kX_7noExrccU2HD8OFybtRgzxuss1ntv7cE3hHzbu10d1Qbm39zUWSMyN8_PD2BRAn1Z-0ifU9YisZmVmga_qyeRPPSjeQtK19taChNscHn-hg9Pa7mqXzZKy949gIGDTsWsx-GNo1A22g6gkjFwUqqrfaDXCdiJ6GrDw9AtgSBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBeJDsNTnWdJboY3G99DhGLi8q_Yhv0S2gXeOEvLMN8ZzCUn7jUWCYnBWGym4qYZGhiYdQ-jhAmMze4EQccmJjh0aFGt_w2iS0yu31CE778KQv1nOAFtgn69EG3yEjr3_8aITqbbDU3yCcTe7bmvB_nz6Wm0RjMBHWag9t9zO-5L783W0hQ8c2eIi6wxeYjlBHhHcvGwsmJulOWc1FvDGRCRa-aqFavkBzI3DthaWBDYAPAZRuxr_IDE6FKx9LchIvWaQQCiykwAJOpfx7sXKSVq3VQ7FlDgCVOsA9Pkde00tCvi877AaKpbo_AUDMHpgoSbQFXv5dZYzRq7j_j-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp0a5WGjzl_ZrdiMzt4Nevuceuxjy298ccOkJ_9YTEr26NT5-Sv_cbKfFUAY4CY25cz4ZBmmM0_lHmwAWVCU15ajYyzl-u7TsXjR1RvYcbTtve7L8zjGPquKnFW2elMmqYDubGBZUtTyvh-sC59KCXwxc3uw479wYjkqAaU5SAiHzkfzr_7je_IqfugDw9tyPghi1owxvLvXWrNfZuk9mNyBp5FTpY_1Y0C-wY3Ji6n07wGgXqEqKZGzB6j3aG8vtTH4uo0Ru9fY_hdp036BP65vKY0_yG7lioG9valedo3wnzcB4aCTVmMsTc_XiyaF2JM0jiiojd0Rp56NrhkdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hytFQsz_bEMXAJpBJq73p4cCMCJAUX1OXAIQJVWOzJVkh1v_z7tCtSHdUTNWyQ2qf5mHx_5cd4ugAyupfgIocTVJtv1wxI1IctsFh_PdxAP5TkrbIjD8c7CLgW9v4EHRaUVyO43EJFO8f0n-lh7d6_Wr_KNzY9SzSm8R_FlA76ukCfzZjE3Rvl6h1_FuZ5B-1qVJt9PsLoCFuQ8NVE6PCa4U5vyWCoZMr4Z2tf1Q35QRpCzsNHpf7e5dM07rAcwfVww0dKh7BNGBtiSMHQw-6tnIphvR5jI73U8t0iuGmhBq7d26Exf9cAap_OycyyWfxSfKJCs3P9KbEwt85mxE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abuc0GtHzBNOi-aKYL6W8Fx8XMkK9sVzOq4W_C9N0dESiEHvLWcIdM7xCg74lT5ubOvzhqFpNyJv9ZcZkh4pteCVBknDT56lB5BnJ5mBnQ9-dB9HclImlx_Q4JgyP9b-xWyTkQPFHGRzpQ_08MFJv6x_Gmmvt7_7_ehSe2qQEBKtoeP_jc6TS8v2ngyWbAnUhxHL8ChZyd6yGLQEbi2X8b6B9IHQjeVhsllV4QVxncS8S1SJadpwtPg0NMqcBJ7hWGK3SWLMJxF_yHIrROWwAXkLpwvoArtIlXoLVLLMXKNJxpDX5HIBFaB3aNYhaBBAViqlkF0nG_KY2HroXM8pGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VigvslzzRlBe-7svcI_zEmNEaUplVqLfWX8gWFcEkvdavEaGBV9IXQVMZBc7InROpj4mHnsBCZA35vC3M3NL4xzb5p-WGwmD9gBUm0lRlqr3b5kjxMpBn8bQncomEfrLfBT6skJeE9-yTzi8Cn5IA8SiBPQ-Qt8pEJhNKJh9v3-6PXxLdsESrbF25CWj7IJgSp-KqaHy4G1PyLpSl0tzQGVC3urKe7ZgDDVZ1OmBoVkFNQQsKAnOB2_dnVdOgm4reNOUlUuFE9MbwSX_7TUhR8f8YPeBmByRnYFwlK4BLZH9e3tR9E4RHNOu5x2i2DKGxeSG5yDDcOThR1DCvv4MJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=hq1R7cXSqm8MlWy8lu-h_uInRmJdIEidBCsH1df1FsIhybWLrFfF2z3OSWrjMPT9r-GXvt-jscC7eVg49yeP0ttJHr3rDEv8DBJt2Xd83Pxkr3mqE97C6_4a5vQmnUsyOWDrqipXqhbPkgNM2Ns2tAWoVqdIYqghr7LOqCEO7DlorRu2cGkBwHLHtSu7hqz_0DSbTDGTxOO5fmwbinDC59c1DUbDwlw9N0aPscHgciQIuFIt5FJNKl4v00nlqf2mdyAWQkwovCaNDsXObyUo-qPt20meLUyU-b8uYC_dx67IZPHHHOq446B44GVFfzwWPMFvKrrhY0orwjPxfoTt0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=hq1R7cXSqm8MlWy8lu-h_uInRmJdIEidBCsH1df1FsIhybWLrFfF2z3OSWrjMPT9r-GXvt-jscC7eVg49yeP0ttJHr3rDEv8DBJt2Xd83Pxkr3mqE97C6_4a5vQmnUsyOWDrqipXqhbPkgNM2Ns2tAWoVqdIYqghr7LOqCEO7DlorRu2cGkBwHLHtSu7hqz_0DSbTDGTxOO5fmwbinDC59c1DUbDwlw9N0aPscHgciQIuFIt5FJNKl4v00nlqf2mdyAWQkwovCaNDsXObyUo-qPt20meLUyU-b8uYC_dx67IZPHHHOq446B44GVFfzwWPMFvKrrhY0orwjPxfoTt0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=aIh_11vKsNVFGXXahd49gD5aJxI_3q-0tOqN-VurGhonhCN0jQltlHReHNnhcGqT234x1G7bjkxsGD6vFMxEEoq_D5i4rreZjqfuScvkfgao1kMacWtQsdU5xBVQJfN0s96Y0JloJxUToTpRsrliPe2Wg8LOtq28nMwKuYRpj48-0Qnt1leFAKeoYiYHPN4I-w08cBfdmJKXRpPUeRGpOB7qe1LGcnrbcy2-LdrsHMMZd0XTp5X8rcUiGCaFTVkOBCKOkm_AEvGupCol4Buy3OxDcRxT9IOO-ss_jBJ4vt5E8cdbwjcdXrcQFw2KgSiF8-P_Rt-lVR0VbpJc1R2eLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=aIh_11vKsNVFGXXahd49gD5aJxI_3q-0tOqN-VurGhonhCN0jQltlHReHNnhcGqT234x1G7bjkxsGD6vFMxEEoq_D5i4rreZjqfuScvkfgao1kMacWtQsdU5xBVQJfN0s96Y0JloJxUToTpRsrliPe2Wg8LOtq28nMwKuYRpj48-0Qnt1leFAKeoYiYHPN4I-w08cBfdmJKXRpPUeRGpOB7qe1LGcnrbcy2-LdrsHMMZd0XTp5X8rcUiGCaFTVkOBCKOkm_AEvGupCol4Buy3OxDcRxT9IOO-ss_jBJ4vt5E8cdbwjcdXrcQFw2KgSiF8-P_Rt-lVR0VbpJc1R2eLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=EX3JJQKugIQbZBZjbD6glS54b0qnFHVuPKfZjSu1h-YYEaIlKavFU4SFI4jIjA90aGGbzAIKDWRl9rEtGkwDcEXtxl4Xckp2_6wBfAHSys2P8VXyJBOsZwNw9faJKeUFkkYr_6aHy_eWOQK-MWcnJwdhtqsScAqaTr_4czQCi63p8knBzNbGqnKLjnqFgl837kYfBwK7bAtCB_fawzxTiNSC8Ad2SHepodSKev2kLE9vqqkxydba2ABug3Is1oeT8MusGQNOTQqvqKNOIoKC_H3WI1l7i6Jet9ibUi2KjP0lKbKZw9SQCW_GtEM-eCdZdpLQvqsEs174GPQ8yJyBGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=EX3JJQKugIQbZBZjbD6glS54b0qnFHVuPKfZjSu1h-YYEaIlKavFU4SFI4jIjA90aGGbzAIKDWRl9rEtGkwDcEXtxl4Xckp2_6wBfAHSys2P8VXyJBOsZwNw9faJKeUFkkYr_6aHy_eWOQK-MWcnJwdhtqsScAqaTr_4czQCi63p8knBzNbGqnKLjnqFgl837kYfBwK7bAtCB_fawzxTiNSC8Ad2SHepodSKev2kLE9vqqkxydba2ABug3Is1oeT8MusGQNOTQqvqKNOIoKC_H3WI1l7i6Jet9ibUi2KjP0lKbKZw9SQCW_GtEM-eCdZdpLQvqsEs174GPQ8yJyBGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=OBwdZv8wPbrgjNgb3OXbw6bQjj-VhvS6x9vYup045-2TCCBjsRjCfRQAHmu94xezwRFSb8nwtILfgGiw1LFD89SrVbO3sw4GkyVa_X65QMUfhxE71eb6D6wC7pY1VMlQ8hCqY0lVU59NVztsworWTrbw8eTHYWuqLxyr6GboJ-7ffZl88EPkHn3qkmsZ9kMAuRdwk375ZyoqDNrCXHs6T9064ho2Zhq4jLbLG_PnGb3aYInDlttaB_h-kdbvuYXAg9f64P73IWwZ_D5IG1kkqNoy8lzIGaofIPtRZc8zrwVfTkT_l7Ucdpy2-lD_TpDumSphcJXTXOCZU3FXhmDhQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=OBwdZv8wPbrgjNgb3OXbw6bQjj-VhvS6x9vYup045-2TCCBjsRjCfRQAHmu94xezwRFSb8nwtILfgGiw1LFD89SrVbO3sw4GkyVa_X65QMUfhxE71eb6D6wC7pY1VMlQ8hCqY0lVU59NVztsworWTrbw8eTHYWuqLxyr6GboJ-7ffZl88EPkHn3qkmsZ9kMAuRdwk375ZyoqDNrCXHs6T9064ho2Zhq4jLbLG_PnGb3aYInDlttaB_h-kdbvuYXAg9f64P73IWwZ_D5IG1kkqNoy8lzIGaofIPtRZc8zrwVfTkT_l7Ucdpy2-lD_TpDumSphcJXTXOCZU3FXhmDhQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0eEMBZmaFcDJ_yjHMN3iQi15X2rqfow9MYXCGKHY5zgGsxf6c3ApVGXMY154ykPKLxIUOPdS8wB2PffkwpNm7rjAypZsBEpyeZobowV9GfgNCXaZQZBqj36F60h1Dh5VRfA5lvjxS4QqWBgOBvBBREndz1dSYmnXk4G1fc3ZLxsUeBEJswDyDvg4y_VFPU7pevol1a84GB9DpX_uq80bctHE9idAYVtSJki38IA68vw3Hf8SL23fxS9pnF2wCoaT4g8hoHdupTnIXA8w7Tdhpqf5ra7fWJ222l-0NrB0SUtXcR4Mu0WemsgfX-Jj88iTa7VL2UWz4Cj2fPjFwN-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxEN_T6QNcZdZ5tb5YZuVxoZq2OLo6qPw9nTSwlm6lQprnLoYpES5Yh77u4lI36uqA7vXM2nD6GR-n5UFsOCoeAgukoMLcmcC2q9KAPAt_U6IbJOFU3r5P1ZoGq5QM4u24H5TfVtMZkKHPCQ9Lj1ZZcHRjsTH_Syrqnpr3GNs4f3Q0RLAz8oYjTeAvbo1ZgqB0uCl-l0uBHf03KHHmwC_ow_WOfvZkzkKYRSZwCWSoGZrTXg0oh1iwdT12rmoSUZcloqrIN_HXc5Ke0FocV70t4v6I7kPruP5wazVZ5CFbetioXcSpWc-MYjdtonTObXaN6IcSQ2I2IEbmpVSySK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=SdXjSP4w7w1NFS8B50XrmhbIaI57-5IJ2I-h0T_EWMIYOX4LnA-NtaamXOF0ZmjvOI5O2Bq3rbXMOyGV07gYZjzkFF7sv1R76iDdSANHyFxs_8Yr1hCzGnEs8MLKPXLteQowTB_XbWcMjbtqq6jGSYe1bLuk3WxgBCjkg8vN7fZ-caoG4IKBxdaQUfRlCb_1UytqGPMCZdjnXpGBJiQkslGBrTJNFIS26l70_Cg47P01a5irfGaqttfwNw-HWEr1suLmKdnmKi3VPEYDiSuhl8i5t6QL2ax9GoGjmFI4TqrKrPKpUY3TY-nPB4wAtG4Cs1Glh7yuxXcro2bxc4Uqbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=SdXjSP4w7w1NFS8B50XrmhbIaI57-5IJ2I-h0T_EWMIYOX4LnA-NtaamXOF0ZmjvOI5O2Bq3rbXMOyGV07gYZjzkFF7sv1R76iDdSANHyFxs_8Yr1hCzGnEs8MLKPXLteQowTB_XbWcMjbtqq6jGSYe1bLuk3WxgBCjkg8vN7fZ-caoG4IKBxdaQUfRlCb_1UytqGPMCZdjnXpGBJiQkslGBrTJNFIS26l70_Cg47P01a5irfGaqttfwNw-HWEr1suLmKdnmKi3VPEYDiSuhl8i5t6QL2ax9GoGjmFI4TqrKrPKpUY3TY-nPB4wAtG4Cs1Glh7yuxXcro2bxc4Uqbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a699XJW3YbaMlhwnvG4yP8Oba-HYBl6ur4YvqUmCEhnHWMhfX1u3DnpIdnoaFOLuSLHuyGB5z3oZYAEDTmJzac2EBwsFGfYE7qYBWeq_sQKMtnd5hdoTtqkonYFns4B5EwPtu_5vt1C06HraX5ihQ5w0VaxYK2PL4JR14Ch1fweNtjvS80D6k694SuoC0smuOSHNpQGlWXPktcH3dyg9m1v6pN89MO6VZfd4oAfTufQm_hKvNcCX3f7FLAyGwxSHxaPvnODVyvt1ipCS57ubBypobmiilB-Si2sxpTT7FLXH9cw3bMkRe4Plihyhs8DwuFCYRRhis5Sbsnf1TviMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Zb91yATdp7cPu8E3j-r1fcv2A0MV7Nv1xagW85dm7MFgRmTRfa6NLoEeboKVptPB0bw716sqOSq0NHlJNYAlX0CJzLYWO57KwL916AcMGEMZ8I-of3TKfEStK_HY7hIA5CLeW8czouUc_hEx0hR0rzxt3fr5fLX47EFym-X7HJoJ6DrxYrJIs3pGWNteTMWoIraXzVcTb3iJqGEkJXKM3BJx-j9TYwZaBrijnbmir8x_m5vFZi4OjN4BJevh8bbOQzwiF_CTlGbuezq8J81fWFRC6CnE9sz6tswZiLtTuabxzJ16LuCNxrwbMA6e3QuOVHuuAR4Mqa6-pPfZPpO-Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Zb91yATdp7cPu8E3j-r1fcv2A0MV7Nv1xagW85dm7MFgRmTRfa6NLoEeboKVptPB0bw716sqOSq0NHlJNYAlX0CJzLYWO57KwL916AcMGEMZ8I-of3TKfEStK_HY7hIA5CLeW8czouUc_hEx0hR0rzxt3fr5fLX47EFym-X7HJoJ6DrxYrJIs3pGWNteTMWoIraXzVcTb3iJqGEkJXKM3BJx-j9TYwZaBrijnbmir8x_m5vFZi4OjN4BJevh8bbOQzwiF_CTlGbuezq8J81fWFRC6CnE9sz6tswZiLtTuabxzJ16LuCNxrwbMA6e3QuOVHuuAR4Mqa6-pPfZPpO-Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNqJvInCy8XYNsh8lEk_ezwVb3iWy3ErEP3LfXVj2YAWwWuU8q9ZmaB-GPV2b1_G7MKhc4-sx7FVVbneswup4E_XGu6pBXvJXQxZYAZy2FT2mvkPIfpbC1PuCdQE1YCEdd5A9jh52m4ej2rKEGCSwHeDwphWisjL8CQMUH36pGssEyAMJybqev-ocZyr2dmZ37BT5jQVdkUd593eJLYxkqaNCCPVObJ10x9r-yoklrfjtrHg_Y6fhXairHwQM7qY8qC8ltEC4CCdsHVXySyMqagRTzjLktMSAmcT7W_2tlVio7gmes0Itibf9yGvz77FN-Jw5iCgDzdnNieTU260Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfBkWTMGPkjKcMXeNs_DZRlUfUa_CS-qiQPf-L3uV5YZHwG8GCJlb4W6Q-lwFUNcvn-LX2dv0wOagZG5wCNzN44cgTF9VOgXnDfsZSHicBHPVnRFTKnkfiCAVr_BA4jRTZ1BbPolzaRi8Ex16woZg9WGJd51-Pt9UYJ5eteEu8VzKNBfsxcxzK6o7c6avNCZN4D1_gV5D2MMFDJ_p6KR71NPQW0vNFVVNB6yQhR33relwgNAvUFz4tQG5b79BoEPiUeKo-2T6Cz5rQD9fEgsugPt10fHbSUopsC1hlPOkxCJVJ6KAdfEhGKtd6yIo3zgc28RFveJsHTzZvC8luK-bA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=s6X-Qjucp5HoYv4c6TlcTbmUzaRtSB1Uru32Ec0FKym3JJ9-jItyF0wKcwvu-YkCd6kzSA-oOTGISZNJbM2DSa8YioIFDJaRpfSKvo7dm7_eo_PacFt_LfkuRIFM0OlTHmoJ6LxEjqcYLLkoNYO3HyU_TMA1OEs8WWF9Tb93pmU37JqITrdUeqiLOIdAV_A55gvbG2tfEYr1riYWyI5vLy_S13U6X1E73WAsWhQDLlKmqT7k7eJ2mfO39h_PBK4LY9-J0gljy78Og3cSbfkXIzn9MpwU7ZRvLnNpgDjZqUU2rJykbcIdGWEPCZR7IfEZOFgaU_9v_I8QsKdrVE0ZSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=s6X-Qjucp5HoYv4c6TlcTbmUzaRtSB1Uru32Ec0FKym3JJ9-jItyF0wKcwvu-YkCd6kzSA-oOTGISZNJbM2DSa8YioIFDJaRpfSKvo7dm7_eo_PacFt_LfkuRIFM0OlTHmoJ6LxEjqcYLLkoNYO3HyU_TMA1OEs8WWF9Tb93pmU37JqITrdUeqiLOIdAV_A55gvbG2tfEYr1riYWyI5vLy_S13U6X1E73WAsWhQDLlKmqT7k7eJ2mfO39h_PBK4LY9-J0gljy78Og3cSbfkXIzn9MpwU7ZRvLnNpgDjZqUU2rJykbcIdGWEPCZR7IfEZOFgaU_9v_I8QsKdrVE0ZSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=OX7ArD77RHoTQfekK0jyYh3j3WNWkNcNRglAL4Dp_kjavP8zWGWecvSO7JWRkUh51VpVD4e1fbHCpb4pPcCCMgDttrrmsTUb7YlFnYxq6RD1hxV_eI4m2zE9LvWDGHkKnM4jlVd_eeqrDaQvjHfaD-7E_-sHnRgw08oBnZgBdo-HB9cUXUzfJND1PVfPnYAepKnGMsqmlhpeDz6NLdaT62kxZTFEjOnR9yFtgM0SeGRSW11Vkg47KFxlPyTM65eBq9nEJWKRNTCPip345dhgDNcuuuMrOBW_KipEBhz9kMSxQnmgfiFxi6FZzYNf3bk8oRpRLCUSmO_oDV5qPBwj5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=OX7ArD77RHoTQfekK0jyYh3j3WNWkNcNRglAL4Dp_kjavP8zWGWecvSO7JWRkUh51VpVD4e1fbHCpb4pPcCCMgDttrrmsTUb7YlFnYxq6RD1hxV_eI4m2zE9LvWDGHkKnM4jlVd_eeqrDaQvjHfaD-7E_-sHnRgw08oBnZgBdo-HB9cUXUzfJND1PVfPnYAepKnGMsqmlhpeDz6NLdaT62kxZTFEjOnR9yFtgM0SeGRSW11Vkg47KFxlPyTM65eBq9nEJWKRNTCPip345dhgDNcuuuMrOBW_KipEBhz9kMSxQnmgfiFxi6FZzYNf3bk8oRpRLCUSmO_oDV5qPBwj5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmlqZ9cafVgOTm6JmolDWFIwyMSf6K-Xpkqp_5E2unSxK_pltHBRBYaDyoOv3N5rrCt4Psptoov6QljFEtjGrHPl9MO4E8EYnh0lJPmyGVuB_-LTmppzMasCF0g2VzxpJLigr56yRFkO6aiUJwzTGi8gOG3py24GGKQ6f2AWQ15yef5tqejTAyvs3UaV0BTYJ9mcD6ThlPmS-6wf2hNR98paJxTOGGGnB_g2SvTKS6UiQpjpLurqsxJaLEt96mWHSdSTo28sXScZ8R1Icmk8ts6GeV2Qk-vVaRLT9m1ZNWtlmJ6Ezx9JtoUpNQC3kp5CZH0rSUMaeEnwu_pFClh0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db_Pcm3gBINf2A_nzsgVQPbPvMJQ8WVBQGw25O-FIq4VFfjMSG_lse7kUAKU316lqmX7jVC2xbukoktkX-2H9G_-yZSW8w-y_s0zz2josjL5eX7nM8Ver4QyWFy0vSjzrCr2CsowsSul3S1amWrzXBWrD05E7ogy_tGfmUueKzcWonJbhFkEOGWdfOSlUBMgNwGAbRC68Nc47cJm-koWQhJn5WaX6YDqfydL-yAdSRcJBVWrM5RKteJZ-2ihw6LUq6_C8V78KwrwAXsuPHjRXNc1wqZ8porhXBicCQaZ-k9GFCqjc0GLXpYrVHY6FwSSIrisIu-J-DLmYCxLWe82fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwBa37XOCO7t58ITtiaz-zreolpyYs-QItCaHMsok3PRzljwAfdDQAX3UZLUiotkbbB3hz9hnhd0BT_dQOYlLRW4ocm67_sUK3WuFHzEaOf2BOJsHHCXUIoTqdDvsYVHkB8hAO9SiKMtaHEsw8c-auJfatemFgj_nZJwPZXQjoI4GaTgOeutWLjMoruJYiOmC-lOGEIwH1cAAtTGxmXppDKESHtmdETEF3r7a5qDUxkADFAvSzIHqNgPxNG_OG4tISX0XzGo1GxCxauQhzVmnU8ylD6FLgG4buvW0utbUJTvkWhPh-uVMgtAGA5KAnIk9ODrGfFHtmX3lBET-4qgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=DIulMXnNZMUMm89YQFOtLpRpXyo-HGjIrfSG4YkgPFiGPDclICz36uYHbw1WSETN0q-3xLbHOuKMs_1THzGP9XUaeruY5uGUG-XnuQsGgNIvvIvS8fkgiJzLpnB1AQ6EPJtfBALEQexLITFnTpISu_U44RPptvLujGCXvHjFupyTdKJCSzOps2vfTqK_bBcXw7NM0R-ocxrmJDZJJ_Sh7w8c7cYDFa_P9n-dpO37XmnC9f3FELnoDkRhQgoMMIqa4_1A8W6MYV10bCB0438WBorAiDx4IZJoYg52Tbv1YFTOzHLhvZx6LOu1qmwNgzw_hqeG5dMhvuI7MByPea8HDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=DIulMXnNZMUMm89YQFOtLpRpXyo-HGjIrfSG4YkgPFiGPDclICz36uYHbw1WSETN0q-3xLbHOuKMs_1THzGP9XUaeruY5uGUG-XnuQsGgNIvvIvS8fkgiJzLpnB1AQ6EPJtfBALEQexLITFnTpISu_U44RPptvLujGCXvHjFupyTdKJCSzOps2vfTqK_bBcXw7NM0R-ocxrmJDZJJ_Sh7w8c7cYDFa_P9n-dpO37XmnC9f3FELnoDkRhQgoMMIqa4_1A8W6MYV10bCB0438WBorAiDx4IZJoYg52Tbv1YFTOzHLhvZx6LOu1qmwNgzw_hqeG5dMhvuI7MByPea8HDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD9v5sygMsPuxxLNkdiqAHrWaA9aLJ8hYQ2Q4IQqlxmSeUOcpTjYatnaD2Me-Z3QkreLzDA6BmhQtZ3byVw4H8-El0HK45lJnszSW8VqHg_HkAbDYLX63l-xC6lqsS2OvY0f6vcI2y8DeLesT5tA7maEFFGY5UKwT24SZEwtIUSbUX4UDz6zkFuZNdLIv-bdoA5Vozk2LIaGWqtFAPmW9NYTtI2ZSgSaQtHmehya3ux0yFPoDewolMBDhkTMutPe5exJDPXjJ4lYIBTLxdigeCxMnwmBE1tJqDNKiCqNVtC7V0YZOLUJga04BWUYfQaf_XtoevCovCSF9BR-Megpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ad_ASPEeW6SuF_VkVNzcjTKUcWQbtQ_Sels5hTeeZCqWjf9ewYCk3Bcnro3ohmUY_psEQX4EOkmnabsmkwNakPtNytI7YIxgEtHa8zWMZymJkpP5ZjhlGDAjOYdJwb8g9MiLNJ7XlnRoYBquHYBzH78uQde0_gVRkc6RHmNHSKDMlxHs-IF5gCHGtAEWKN62XZh1ayD0eD-n3vimbpd3F2vVL5t0KqlWDzHE7QfbsoiuRWCZ4GCe8mvExKz-jW7y2Uwwr8HX4Wt8h3xkgoWHulCWskomdP7jMo3sBpExe-HeszgTUCarkhaupA2ICkQVKtgCSNmT5iK8zvrTgNrI1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7eYidmBzAR-q07G_j27WPYaD0X9Dy7dvtzS5mx4Ya3WyrQCRqoCPgIsWTLTAzWj4_cFtChVE37H4YC1abO2N0CIySyZ6Ih6J7QMDwDC3tgd29ePPt3gmb9LxTpEMkGycDINOpvcoqtHW8j3DmDEiiRaXuRUaGNv1Cf-WFU4KxIBtYprMLLJ-vvE4z7OoX6PLnYGSUy2fTnox7yIu2ScccteRf5xIhYunxGdFXTzRQ42TNcMMYeE16UYcZgOurbpjvQ_vpJLYA1uHWho6ZZ5byGdu_u_gAotdC_pRfEzQYgIUDqO4GSm7uZ3gu02qo_RM9sFpLluG1dO42DuDHR-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuIraG9Ke4klaxPdl9_OvZxeKK1DtQnXgaNWyiXZvJqABQ2LzrIZ7AgEPgyqJHQw2Px16oKySZv9uqWD31Wb9FCe6k8AMuFiqah15I5V-LNmQq_KobCUFlvmz-Jrrwlf_5t6eO37PYdbcnjVkEHZ96k4O72R0FuhaHB-iDEvVaSz-dDGyOHeFeAcr0qm0ENLkuX6JSnmv8CpOpIazSI2X6stU04vQt4pikNQeDX7b8BwpqAj7Nc8kbZhdcdLTA3KyxnDNfhHdfgCD2tVnD9FBXq4gj8Fg_QF8Gb0SEMCjOR304Rkp3GnwDEu6ZvAcibwdEYfmi8SYkPsKFsKyBXDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=NjqcamVZyGXNwHWpVjzmvSmxZL-AXEneZtTt0eSrePW5gaYwxXxYhuS0CEu1ha49ojSpD4GPhZ9P06ssasNUXofNvseR5x6KHpP6ERqSCknkQaytj2MyC3IoP3edQYEPgD2gXk6LgyfPNVfKnPz76xIJO-upY0jjC_Q7KehEQhlyipkFbk3BPMTY42ULrw3v2C89txG5UuMKlgM-sTtkYzCTNxypX6sLZ5bWsAFrT16NR1PTouBujWI_x1Q3ryHozAjjXWFD1CmeL33Q3PscC3ACcA-BaeLJ1v5o0WUfQnm3c1KibrEe89BTu1G_q4MYFIsPnJT6--NIPXe6TZYGYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=NjqcamVZyGXNwHWpVjzmvSmxZL-AXEneZtTt0eSrePW5gaYwxXxYhuS0CEu1ha49ojSpD4GPhZ9P06ssasNUXofNvseR5x6KHpP6ERqSCknkQaytj2MyC3IoP3edQYEPgD2gXk6LgyfPNVfKnPz76xIJO-upY0jjC_Q7KehEQhlyipkFbk3BPMTY42ULrw3v2C89txG5UuMKlgM-sTtkYzCTNxypX6sLZ5bWsAFrT16NR1PTouBujWI_x1Q3ryHozAjjXWFD1CmeL33Q3PscC3ACcA-BaeLJ1v5o0WUfQnm3c1KibrEe89BTu1G_q4MYFIsPnJT6--NIPXe6TZYGYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv421GzxlZGrG_u5ACs_IIti1Vc1RaXjxNkscnFqG9Cx95xQfIAS_ZoJpQdNIeJ15Iao_f8mB-HCaEQydvCa-NDRPpU8xy6gT9yFuRJOnnE_Ff4A3CAhaXdmTeSjqxCcC-xMJ08CEF7Dq1fCsjJAGn7Ph2RPyauAT5uJJxYgBjYPyEMLp7Wh5pPfttTEb61n6HmVAIW05C66aDHjppjuvVeEX5pnNK99iVRMHYDKj1e-EbQfDgTZbRSWkNG8IFDNxdnpwmbPpiX5H0o2zTrLWHaZxcidVb5I47xNzidFOWWZlYzAwPCR1vccFQ0fe66EPVog0x5qndMlGP_HFEfOYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=CmWqHrpS6pWBn08MiciW6eEDlvJAgtDe1cbq-76o1pMj85iL5BI3NvEbfKY3MlciKZOAoQDpx9oYCPkuAoZYNXLXzjPy-Z34o57vXNpzc6eEoiB1ZIKlnPbX7HgvMUicvheXBIg4whv003EhIpnLnZUl6_4USjgAonGuK8UUsN2juW0u_x1fmldr3UjcaYg6hS7n17aIUztwJ_sjpcNgmPpSY8KtmF2MbeimhQTjKsyPAMHFZMVmGdemOgpZMRktoGpPMRQns36fliUM2gwcDnQfUbEalSJ_21UDxFgwOR864sd0HG0xzfE0cwH_sBl1UssFhSm3nfqnqMjCeSaqNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=CmWqHrpS6pWBn08MiciW6eEDlvJAgtDe1cbq-76o1pMj85iL5BI3NvEbfKY3MlciKZOAoQDpx9oYCPkuAoZYNXLXzjPy-Z34o57vXNpzc6eEoiB1ZIKlnPbX7HgvMUicvheXBIg4whv003EhIpnLnZUl6_4USjgAonGuK8UUsN2juW0u_x1fmldr3UjcaYg6hS7n17aIUztwJ_sjpcNgmPpSY8KtmF2MbeimhQTjKsyPAMHFZMVmGdemOgpZMRktoGpPMRQns36fliUM2gwcDnQfUbEalSJ_21UDxFgwOR864sd0HG0xzfE0cwH_sBl1UssFhSm3nfqnqMjCeSaqNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=BcZjGkIy10lQ4GHQqc0jJC_WHe4Lcz9a3g0etEYGkeaTEKTrJw7tmqVxIzcrwXsy5Wcd47YAvWjVPjDG8lGXJvZvhgvTeCDyJW_4xw3VnIvbxCeQgEnCBmHQnndaiqh7aSQzef_dWIaftUYrpZh8-vqHbzPpK_VlWDfRvGnJItN3wn269BtVRrUziaR8U60jm9CG2YbEhg2FJfRe0Y-2EWNXystxivjo-Cx2yFnRnBfUTHydcQ-NQOHD2MQ8_lT0GMKwESCZyGIfHhBOfvm6zaEzmaGI0zdl4kwpvLMc1p6zl5AAP-Ylgg9Atd9D7xeVDLqRCjwItq7NHP7z4XI79Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=BcZjGkIy10lQ4GHQqc0jJC_WHe4Lcz9a3g0etEYGkeaTEKTrJw7tmqVxIzcrwXsy5Wcd47YAvWjVPjDG8lGXJvZvhgvTeCDyJW_4xw3VnIvbxCeQgEnCBmHQnndaiqh7aSQzef_dWIaftUYrpZh8-vqHbzPpK_VlWDfRvGnJItN3wn269BtVRrUziaR8U60jm9CG2YbEhg2FJfRe0Y-2EWNXystxivjo-Cx2yFnRnBfUTHydcQ-NQOHD2MQ8_lT0GMKwESCZyGIfHhBOfvm6zaEzmaGI0zdl4kwpvLMc1p6zl5AAP-Ylgg9Atd9D7xeVDLqRCjwItq7NHP7z4XI79Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXqSyxlbgsyUAk-o5SC1mfggf4Rw2FA-4ouRDeAVzYbxe72F5r7j450brGWHuD-CRUk8qAWhInvvKA-eBTVqyEeQUVQZSjFqk84uFWf-h6YhuL7xbozjVa2F3XTFJEHUqnXnusIuccO9IRLPq6tMo9FkJF1Kr7K0B1z40AxTfoHZWY-2I330CZcZm7UIqb2qDJYj3gelzDs8c_f-QrM4hzPaDondY8YOKJpIE7etZSYQRtm4eoBpxzvSMVDRa1v02me4kRsIr3Fh3kJ_LkO4DGzQ_zxyGoCda79gFJEiR_m0tj14Y6rBZLK_MxlPjad-o0ajz8Rc8fmPLxV36hSK_Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=RaoLvssUHXR102I9OgbTh3ZHE1HEq0muryDsRbVL_f_voLBkMitu7EpwlSn7qLNstd81Lw8WpfBh-2r-H6LfA17uCxL968dvAsLk83GlbJTZpjQFCnTtInJJ10vobn7WSL-IXSTnPzxbU-AaUqLySSwVYHCVRNntOFuVyxOip6qHiZR35yXd8_oEoLl-lZgHII-mdhQikzI59wIK0LBzot01qnRjN1EF0YekIcSojwxLif_jFjTYK_Zt6DCtMRtu9sGoUTwxjl_hDhNT7cPrjqR-NUDIAloGrJWW1FsYcEnfzlhqkSMK7mV0QqUlpbfbtzGvbGeXhuFVZG8UdejvKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=RaoLvssUHXR102I9OgbTh3ZHE1HEq0muryDsRbVL_f_voLBkMitu7EpwlSn7qLNstd81Lw8WpfBh-2r-H6LfA17uCxL968dvAsLk83GlbJTZpjQFCnTtInJJ10vobn7WSL-IXSTnPzxbU-AaUqLySSwVYHCVRNntOFuVyxOip6qHiZR35yXd8_oEoLl-lZgHII-mdhQikzI59wIK0LBzot01qnRjN1EF0YekIcSojwxLif_jFjTYK_Zt6DCtMRtu9sGoUTwxjl_hDhNT7cPrjqR-NUDIAloGrJWW1FsYcEnfzlhqkSMK7mV0QqUlpbfbtzGvbGeXhuFVZG8UdejvKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=KVX-gWS6tIHezKTQP8Ec3Kr99vLB4QrMYLdgwR5DD1MOZWrvW3VaIj5OXjCe0HCKeP2JQUBUwRPZYx0m5dQ7lXYryKgWE74Fh8sCm8sKDq_o-FGX6s3Rr5xP_LR-_XhAM3G6hEy0jagwj7CHHvglF-FYhotHXyKmR_bRmA1GeflJVJDSCSq5gLRvDkbZRMQVuC6FMrBx0gIK9akXdlgPyKLg9mFwjZcgC8UV_S-kWWc5Ev1Bts6lcJXEo7ES0EL9pSgI8DLzjS6P5FotDrKZU6nHwI5LQniI9DBF73YeSH-KgyeWtIGE-kj-FuJk6PqLp-DsToH2FldiUSqw-5L-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=KVX-gWS6tIHezKTQP8Ec3Kr99vLB4QrMYLdgwR5DD1MOZWrvW3VaIj5OXjCe0HCKeP2JQUBUwRPZYx0m5dQ7lXYryKgWE74Fh8sCm8sKDq_o-FGX6s3Rr5xP_LR-_XhAM3G6hEy0jagwj7CHHvglF-FYhotHXyKmR_bRmA1GeflJVJDSCSq5gLRvDkbZRMQVuC6FMrBx0gIK9akXdlgPyKLg9mFwjZcgC8UV_S-kWWc5Ev1Bts6lcJXEo7ES0EL9pSgI8DLzjS6P5FotDrKZU6nHwI5LQniI9DBF73YeSH-KgyeWtIGE-kj-FuJk6PqLp-DsToH2FldiUSqw-5L-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROVrTBOxVi1iLB2N_qjbMl0YTLmIPf7d07amfv198bJd3kH8zBA0X4gSxd2BigLOEuwvy33hWUAjF0B9J2QcMvyE-R09bqUjLf0YpDck8cVS6sCrnSCQ1UWWlqP8yTX1LCBeqz2WIKiEtVycqycxsg8ys62-n795lb2XKUbHYr3Lx634wnpc0kPDirSH7iXSCs1eM5kHzPewzYzuK6oKCGN163nWpn3Ys90jzYnCe8YoObJWjlgcmkPiGbzepk6nu3V0lT_D_ZtKXu-vvXlmDH9992JkReUVjKqrQNJy0bQyvwenNhlsle8mQ7Fw5EQwoSdulrBf7wxeptY8Zt6O0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWOs2_l8DHI3ur2Duy9JDRsSQVQ8aCJFJHgQ4lVExBJI8zrBpn1KN5GVuHPejiVVmedbz9QlQW9Xa_Cwn3Y9kOHRo3xPdGGOgaaclDm9EdYXhzJMWctgEJiipK5owIRPXOUWbmIwB82jxHomy6LDyRXuGwRvX5RXT2qc-d7xs8YzB4O5tfZURL4JmRRP0rzfJhqVxPao5KKDNuc7ROpvSVmf3lJWpSXj8WpsrcnqfxzEDwVNhvoMy-90C5HEzSBB89NKDSkGdf5_-Lc6MUsssRWo53VWg7orSOtUxQoBNhnPb213dsbhu-Brl9c0hLPO1FLUtmw9MBtoyNutDixTWQ.jpg" alt="photo" loading="lazy"/></div>
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
