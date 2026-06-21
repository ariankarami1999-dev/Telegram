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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 23:39:52</div>
<hr>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIinY0MFaAW6k6z2K3hUb0170UpuB2heigF5UcSdeuS91zQJ5vy1GubbRec2t-dvqz_jKK4Qm4tmjSs9x6x6lzsJIhnTw8Fk_bHjWJPhNH4x4Oi5LjugAiWnjCj2SHyr3k0ah2QYyhWysAica4RerzIkeP1l4rw5sar9hEWnjCkP3iElB38-lorz5xlaRsyyrbyC131O0D9I6NY_cmVtCmkX-WQkSaqlYsu1o1xo8gitEj9A6LaTEebeMXX3VBWgyiqTcZzLAZHa-Dzbdsxp6pBmECf5f6qAwfewWsKdnbkq5t6fZ4chpgkHzVyAFfMyQKcsgoT5JIcFDZDN6N5IsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRJPVLvahshFW0k6cQc419bTwku_x39NwS7WiGVBNSSnpozd2yn0VvhVte2Ipg5wmBqco4gJeOGfE-f4L5G__XrTrnkVyWM6l2TLPCbR0eeFdv7xfC_N5klzYXoiz-MKlq2o-LjwAzVdZQ8qYnggblArunLF3tfF2WgZxFBdlFRv98BiJq6OJcmmZ31tetKHDtOneBa7qaAKf-BCJLDftAtP2XUHlpaEwvvKJHeUoENbfJLQr43BTg_TqW8eMeSUOd96x-Qu2jriqLOO6r6AmA7-OsdfndoHCqgWJBEJP5xq5ydWICBI52ltCgNnmo5Jw9efDx8nuEk628Coj91SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIYhK15Sh0cGS91laW-EHNkwXJ1erUyknj2kwnWuYQEnWK8Ra6bD5C4JWBbpZhG6G5N92AdhONmky-ExHQAM3nDvLeU8cw_j4hg1GONC33pEVwyjHIWvcs0MjRtCBDTNItnTnei590jAQeTHI-B2qtDZ_TansdeD7FCTBMCcpXn0dHHvJCMPitgdUJPxBw7uFC-6gI7IEzgcWXIUsWEe7uAXnfUL7HrnZ0QTGY8W8ORvusgJ6onnHxRNH-VjziZgQ6xdGuaQvnn4Yl-1dbw7ysf89H_hXckK3KW4jd-72JbVem_0rYPxGiyugZp6kuN4M0Ci_RZWhTesaXemaAebPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kk6UzVHiJ5a-wdt0SySHcSrQ8Y-4lxQVZTO6H2iQzaRkCpqU-5HA65T3835alxbJElUi4teeWwwuGK--Uaj-E9VTOP_3YcZWEVx1Zb8ugOZ01F4MUCqjLb5ZSgcGH823Pj7GN_aQS_4_6MZ6wKoymD_gRN-Lz6DcdJkbBoTPNfpbeRpA30GGt5fGqzAHyLQiakSlhzVQWVk_y7sBwpe5c5zAkXKZ-9F471rtEgj-oMnS0fPeHQyH0TzCT1wcyemKXXq5yeL0mzki0WjVLkBsBUc7ZPpUZM6fSWI22_grsYvtYQYWnrrthHcwJp37YPKhnRVsVLTdjpx3K6JOKSkw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3Qj3kf-JJzINr17Bd4aFUCxfE4RNS74s08-2sj1vTt1Y68KO7rkOl8bv5Nzr6Dxpy-VSDZqbC-OgtuwHMXozZsPT7b3O-1gIW4parsuZEEjsYqAx6nrAQFNYpoyX19IC4psoqsnlqurvaZxOF7YRdd63iLoPo0N1BY6lFHScmTesRFSIgicaurVD0fJufELkf32dI5wuk03y_Ezw88HG90GhfPHercRsaInDzNgSuDYEF6VanyYR31UU74SA2PqN4sRfq9kzt07ZSWG-01uj_UEuq4NE5e-toJ1_WHK5g0cxBxflg3z5WOik3uG6GNQoRzm9ZLe02dTJzDPSgM0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgSKtERFlk7GeVHmOibaVa04Ek_gRAxDA09ET419nXzjgZnndD1_lSPx5vI7X0iA1bkJGuPSXaaBDoRMbh2bGf89RenuHNDrBXrYeu3whlkmTpYTXCls9Cs-2NyKW6P_2ijn2BFI3QCQ7XEREsy0WVKHR2lIVdLZviMzo5tGiIRyV5QHpjvMaupkOTwKai5wLr2Qi5zuA66CKfj9Oz2J2i2fRAKuNOjnHT6BPD6kA2b_45gaauXjUXBFF0jtSnOQyUwo0AgQUie6K4EExUKLEh79O6p3K83gsooTPwv1VDQ2fX5jPQmmbouBLU9jssIYCrGiPYFH14j3DSFiLNlXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBdeWNzf9v2czF2d-w4ILsENvZZaBY7oYT7T3MW_SMR-9JwcyjEJfHkUQh801LPyYGwrbOs1oSwAzKxmR5OJZdnUbp21v8rMaOV5_XH-JE2zpG-okI297oV1HBmQp6Nyav32Ts8LRUsXD3b3QN_w2nRTbRYSUUT_uyrfhAz4lXK9aSz2OdpjJcYYROp1ffwmO8kIe31DNn6Y9xaVDmbulXfBV942xlTxfhe7NhPVxyFEfxG1lZBsRj0AuuBXUN3Keex-qz1MruXuVHthv9HEC7-DbCkKAMOg57jVMRIbx2Gjlwn-JI6OWqYoGnQDzjoVWqezF3qjWNzoDPc0mcM_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgq5-bj90lOJ3EZOrEqyh25aVxF6nFKyIg7DJh9WYa3gNmh3eBkTa6jhQrq3mXJOHJMkx9st-q0sfnPwC0MigaeGEcMI6zj4Tz53rCOASxLXSCdFpK9KRUo9m6Ux-71fWfSGe34nvy5ZAXATURUiScrGPXFX54TA5_q3D4sEL6EjR3-1CnjB2HCAVx07zqfVQaajNFHXXNB-wjYuztOAokw-V0XswRrNCxkdJN1tpwZKmtsDzwbmoYjrJskysJtDcCrC-thGD8d2_wpzQDBalA2CHK-NZjpBM48wA-5uacfNbdcTeMYfnBRumXpNSSrdvg3sIeNlwUYndp3mmQSWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z14DqUyzcDLMh8ROn6n-yBOv8MaR1Se43nWVZ8FhzWfOtRLwGP8APzHGIazEDHKlqOY-flR4SbKb9l8gJ9EE-756Y9135rGhYPtvvOjgW3lhYUr1lxieB0pZaSCpojDX6SAUr2lKV_MW2zEO2VS6MD0B3weX9LzBq0iTFHmW3WblJa-kviI2tciKRisr4mEd8kTbvztC9_M6RDgh99nXZnR0olbwkw0E3VOTl0bsqTO4BPdWRsBN5EeS2TvuYM2snjUIv6OvJDjzNWeTcJvFyA1_sDDtOFExCH_njdde27USsc1BgPECfXm4PIBixP2h7z1_hGOkBCScSTozgPYZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=nTQ6X7_GjFCnizdx8V8F6mj3N07uha1B7benIhZ0wWwY5Rk3DTHcckpbx2EmNBWdv3KA959uigciTguWGS-OIdV6cyGSnDtI2J-THoS7yISivHCcK38D_4M45cLfLGwLvs2ieV88ZwfUOrLR777xt74lmCE9OIE7K-cYTA_qPnXuThoxXSxxM0BTGhWEdrQI2mh5lSsxcwhMBRZKH0Q1y7j3-NvE-kd67zl0_DezR1q6BTUTWyYlcdr1QtaceorqmICmcQkPqU5LCVyQcse2MEEp_fIXeSnSIgc2-OQTQJUo2UTSiswlBcQIk9JZ6UxiRkw70rMaY6vOXNeK5pM1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=nTQ6X7_GjFCnizdx8V8F6mj3N07uha1B7benIhZ0wWwY5Rk3DTHcckpbx2EmNBWdv3KA959uigciTguWGS-OIdV6cyGSnDtI2J-THoS7yISivHCcK38D_4M45cLfLGwLvs2ieV88ZwfUOrLR777xt74lmCE9OIE7K-cYTA_qPnXuThoxXSxxM0BTGhWEdrQI2mh5lSsxcwhMBRZKH0Q1y7j3-NvE-kd67zl0_DezR1q6BTUTWyYlcdr1QtaceorqmICmcQkPqU5LCVyQcse2MEEp_fIXeSnSIgc2-OQTQJUo2UTSiswlBcQIk9JZ6UxiRkw70rMaY6vOXNeK5pM1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adRz3-2w6mQiiUOo08V7YSgkVAHlQHYiLZ4VNw0VGEPyi31OxK4m_NegFPGCor1mhENBjjDhhpkK1m1FEI-ujToZnz0LWIJ3uheyOH_FtMzt4vw25vtPr9JfO6IOnyYalOqakQ1IM9IZfYPhZev5nbhSvfDg7YCT6w3phHifqnFEDKfdBtqOCN3ajD-vdH0NZhy2hspPI_s1u42UDJWsWBU8sFotrZaNlh-xmCMtEEYylenVUwok4LCao1S-p_Vxv7PJyapHjRlto-WfyWzfJ1pJGJM9y9xd1SbJmH1HqGBHJdAVKdXVgvgt3h6q4WboVkT2L-PKk4n-wvxoW-xAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTiHHa-YXTxQSSorFKHxNGavcGKzlqJfvcr5zRlQz5KMYU9NsAC1rRDHqhx3lmpa67xR_uRLyFMp9vy8FoMXM38-KdBguvomctElUwmqtsGuXs435GJvlfHyqaaJxuhxlYbGTWwk_xNeu0erW9TtNAXrAYdeN1wE0Q4XsPMEploQIiJI7lZDAa4PysDUGBpSpi68uhuSGnz-ICmx5BdMIaoa-fd1dZcdy9uwe0ssTB9LrsmEg7pxV67v9GA3c6ovWLWqETqYdlqXelblB7uZUj4e1mWW6pByHn1giDEn-dcu_2oRbjaQ0VKa68npnrgk_f5mHq2MHY_awa64no48Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2VchZg_KIe1nUsEPl5XuMt5ion6kWkkZ6STBX2cTHaRUPPQA2m7ZWHdrg40e-uuFSiUdCiFNKQbxxlXp6SHOURkCEHlS9HSCeCzA_1wtTfrcsAYcZ7b8PZbGNYfA09NMnsZrL838Yi65hVzvTzLK0xSaovujQD48G2LDtEPRB81eMmHW1nz1DAgofZZPbwps6XFWCC2q9d2Sub1tnnP2SHKUkg1ojn8ZKfO2ivTiYZnz6W7k5sfJCXtXXNU4raoOINQeRrOzvjaQU3mqu0LIN6Omtyb9MYjh6sZFM2DCaaR20tspfroRyQsOHAjvGkyWALy1JU1eU3OX22jobNVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=UlaYoaIzlRzrTQDUpFS7NKJSIQJtKvdKPxZSCBj5eO_Ie994k2Qkd-JWf_6hkft_w45F5yekGWR0zap7XXVkIIe6k1Q9TQK7gQmM4vSPojQDlT00ZlDSj5yEDrgoW8HNe-yBfCxZcX79S_wk7XKpgoEUWmw7Ck1R2fL1PtWIaG89231GQ3QD7UkaLoy0s4Ww_YU8OOydvjLMDoQImxOo00Zx5rKPWiFTxEKLGTfh4kyF_NzSrmU8h7FOvSfcKNKQoKeQCpKz5CbZ3wF031zn_MGaCjejlULPNYAI5v3PQrWZ9bmV6xgrsd_wVA0PXG5eGnWTx7C6REm_bBnzp_qH8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=UlaYoaIzlRzrTQDUpFS7NKJSIQJtKvdKPxZSCBj5eO_Ie994k2Qkd-JWf_6hkft_w45F5yekGWR0zap7XXVkIIe6k1Q9TQK7gQmM4vSPojQDlT00ZlDSj5yEDrgoW8HNe-yBfCxZcX79S_wk7XKpgoEUWmw7Ck1R2fL1PtWIaG89231GQ3QD7UkaLoy0s4Ww_YU8OOydvjLMDoQImxOo00Zx5rKPWiFTxEKLGTfh4kyF_NzSrmU8h7FOvSfcKNKQoKeQCpKz5CbZ3wF031zn_MGaCjejlULPNYAI5v3PQrWZ9bmV6xgrsd_wVA0PXG5eGnWTx7C6REm_bBnzp_qH8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Q9REQKwkxoKTOhgRO-L3kR5L3fwkkACyZw77ZkYGccXTsYK1QS-bHFcOx99K2xK5xOxtuu2EtBewdExNcASD4xlmgxwMKRXvprmZ0HvJZ1pmAxIKVbs3KCQBqb6M6M0Mr-YP58NFVSYXrTTseGE6OAuMkv3Ym9QX5fDTRqfQkdmxQIu-CJsuFUR-leO-iwtsWwmJIBw1o1csaKNEX2gGtESsUBUWL5XigkobinaKI1CMMk63sAOAwxa1NaMkoIk8Fm4qJkkRZ4aUyB-fQnTYN1peJ_ah_riiiETOTQJlnxdPjbWgJIpFf-eprh8-FQB05sbh62F1mOdLLXtwMF4k6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Q9REQKwkxoKTOhgRO-L3kR5L3fwkkACyZw77ZkYGccXTsYK1QS-bHFcOx99K2xK5xOxtuu2EtBewdExNcASD4xlmgxwMKRXvprmZ0HvJZ1pmAxIKVbs3KCQBqb6M6M0Mr-YP58NFVSYXrTTseGE6OAuMkv3Ym9QX5fDTRqfQkdmxQIu-CJsuFUR-leO-iwtsWwmJIBw1o1csaKNEX2gGtESsUBUWL5XigkobinaKI1CMMk63sAOAwxa1NaMkoIk8Fm4qJkkRZ4aUyB-fQnTYN1peJ_ah_riiiETOTQJlnxdPjbWgJIpFf-eprh8-FQB05sbh62F1mOdLLXtwMF4k6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=gK0XgcpVHDD3uMtwK03hcDWwAht29uOU8qqwNtj-9J7euZZtFP3mJgLZVCoKZAegDn9PnVa5iwMjxmVihxQ1kCgbrADL3s53c2kVKxQLjs71nlI0MRUEMjowKf4IhPvReb-Cd0N-IMtEIm2B6uxNhzHLmw3S0jrYn4qqbve_lpHIH8tM3NnmJyv-vu9oit3VpxtftxH8BtL5Tgi-6b2Rz7fq7dGkzJVieM7GWRQtD5RxVyWs5JfWFBrVOl9vuKmXjeKIjef2JMZSLYxOdqK0dkpL9d5JRiKPJA9ezGDzmV6cBLIS4yDckthnHpPsv7Z_w6N8zSs4fzLZeq2GqehzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=gK0XgcpVHDD3uMtwK03hcDWwAht29uOU8qqwNtj-9J7euZZtFP3mJgLZVCoKZAegDn9PnVa5iwMjxmVihxQ1kCgbrADL3s53c2kVKxQLjs71nlI0MRUEMjowKf4IhPvReb-Cd0N-IMtEIm2B6uxNhzHLmw3S0jrYn4qqbve_lpHIH8tM3NnmJyv-vu9oit3VpxtftxH8BtL5Tgi-6b2Rz7fq7dGkzJVieM7GWRQtD5RxVyWs5JfWFBrVOl9vuKmXjeKIjef2JMZSLYxOdqK0dkpL9d5JRiKPJA9ezGDzmV6cBLIS4yDckthnHpPsv7Z_w6N8zSs4fzLZeq2GqehzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=DsoV8DIdYQollLQVePZK-wx0UT6OKpgl73rgpDM3NauQSNn1_1BFQwym1qrPK0kUnhkQIfOhTTMMjOENPDHaUf7KdPsfEwtFc2LTd6mDiYo-60I-umeM5cYG2e-GUbH6I0fvDkAbIf6QdqNDMs5v1ccC9UUBlDLnk5YrB3ILGfcdIG7PjUKIeQTl8Bcw8jaIEQSN4ICm13mG6GidLjnivwaxY_8c-6OOaE5FSnvzEJm2Y32_TeSfp5Y8wN_wb01vP5_F_Jd_MzKEcdcFMRdgTraYDDXinKP7shexJbXUkQgLS12xAzy45RPgqq01HQJmFOG19oUu8xn4-1q5BIJ5exBUm_FkSsrij-rCnj5UQNhBpSqY2Xg53Uh9FyxwIkGiJS7PD8jVPIayi1iF2L4cDMP54-RYyVOrrcmvw3UDK4WIVEnfURa_-G0wGWc_anW7vL7R8FzckGDdgiBHHZsBHUdPt5boMJjE6q2OV03Y6yFbfFjEL6GLCm-TiCKKl-729fXVnbJOa4rA3-wS_pOONQtmUepZuW-CDZ6lETsv7oKqpU7v11NoziCdLh3BnxweNNguOMooO53QxsNLgu9ftzd8l8lm-c009C0jAvWZnT3fJCycGxf39HPHT3SzIInRA0ffZ7wlpwW4qGytWFRAwIxG6_0_4IZPbD_GYUtvzCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=DsoV8DIdYQollLQVePZK-wx0UT6OKpgl73rgpDM3NauQSNn1_1BFQwym1qrPK0kUnhkQIfOhTTMMjOENPDHaUf7KdPsfEwtFc2LTd6mDiYo-60I-umeM5cYG2e-GUbH6I0fvDkAbIf6QdqNDMs5v1ccC9UUBlDLnk5YrB3ILGfcdIG7PjUKIeQTl8Bcw8jaIEQSN4ICm13mG6GidLjnivwaxY_8c-6OOaE5FSnvzEJm2Y32_TeSfp5Y8wN_wb01vP5_F_Jd_MzKEcdcFMRdgTraYDDXinKP7shexJbXUkQgLS12xAzy45RPgqq01HQJmFOG19oUu8xn4-1q5BIJ5exBUm_FkSsrij-rCnj5UQNhBpSqY2Xg53Uh9FyxwIkGiJS7PD8jVPIayi1iF2L4cDMP54-RYyVOrrcmvw3UDK4WIVEnfURa_-G0wGWc_anW7vL7R8FzckGDdgiBHHZsBHUdPt5boMJjE6q2OV03Y6yFbfFjEL6GLCm-TiCKKl-729fXVnbJOa4rA3-wS_pOONQtmUepZuW-CDZ6lETsv7oKqpU7v11NoziCdLh3BnxweNNguOMooO53QxsNLgu9ftzd8l8lm-c009C0jAvWZnT3fJCycGxf39HPHT3SzIInRA0ffZ7wlpwW4qGytWFRAwIxG6_0_4IZPbD_GYUtvzCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=RMF_-ZqnnUoG6PYNLLUuuRXNq_fJqzOJzGQ2zpbq5LTIlzOnY3eB8VD7uFLMJj0a50m2jG6HHOP-qVlFuuxPczZE9BGwbHyQJO2GrH_cZt9nVxu53-7sjDFbxHjSWz5zF5Hy9tIQZuebuS63qD_AHTpoP21hWCfqyGm_dYUybYRnQgAgXJLTuXEGCKPhYWRWAfvwGhO5HsgK3WWUdcZOs3qKI_in2utis2WHPs0ffz3rd5JtMHCFGdMW9P9vwtU0prmcEN8ru3BDk04CBdA8DoSEL4dTQ2DW3QjNfbq0J6xKLetvuazf7RQIOTZofWS-VCqNrkKJP-geLaeeO0QBUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=RMF_-ZqnnUoG6PYNLLUuuRXNq_fJqzOJzGQ2zpbq5LTIlzOnY3eB8VD7uFLMJj0a50m2jG6HHOP-qVlFuuxPczZE9BGwbHyQJO2GrH_cZt9nVxu53-7sjDFbxHjSWz5zF5Hy9tIQZuebuS63qD_AHTpoP21hWCfqyGm_dYUybYRnQgAgXJLTuXEGCKPhYWRWAfvwGhO5HsgK3WWUdcZOs3qKI_in2utis2WHPs0ffz3rd5JtMHCFGdMW9P9vwtU0prmcEN8ru3BDk04CBdA8DoSEL4dTQ2DW3QjNfbq0J6xKLetvuazf7RQIOTZofWS-VCqNrkKJP-geLaeeO0QBUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR98TlhdxKbeRTwfFl6PGKgXgbXxMTYco0cHw4BU2PypYorWvQEDQV3MK46VNBKEq9miOb49IMl0Io4KF6-uHm_-MWDzONh_Ahvt9GZLGzxEfsXdxnnaS9N-jxZxCiP2SEhB0ir7LKdrVmKQ2c90Yqjjk73gHMc_v2SybbBsmSa_eecYfUN0lObjw4_m8jeYlMeoiFPmgGbZsxmw8z5kEMXmRETKm_dOBBOTx_t44jVpLeMrmXOgS1W8ooMHrYNiAoqMwog5q8EPfX7TRjU1fqy3mIEDExiGJ-2dVSyd55jlzeFs56C4djxcMgqZHAZcquCmVnj74U7N9e0qSYzKEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Nem1BaQ_Avtvb1cRW3iHM-oDuE3bp9oDtWiiFfaPOGpHzYsdplkNRHWaePngBB37jj684M5Yhc7oN8pEZ6sQuHr_5SbnMMkC7s0h0FSRlP9MzGPiyKKRa1kTuP-6zJ7OQPKvw0QAY_uklUY_Kpa8qBS8hHwHWwMkvjlVetveH9Uhj3mWD0k8JGG0vRj4Wybd6N0HcqEgOwDvrOLYSmUj9CCvyRWqVv5ZP8f4nDuFda8e-ZjHNMZQNQgkW-U9qPUByzeE0uZRPgxEjnk7nEX4om1GA6WoWvsCG7RKDHdpygq87RMKbY9rUV7B-jraUTgzn53AcrH6XWbEz33Nk0nxhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Nem1BaQ_Avtvb1cRW3iHM-oDuE3bp9oDtWiiFfaPOGpHzYsdplkNRHWaePngBB37jj684M5Yhc7oN8pEZ6sQuHr_5SbnMMkC7s0h0FSRlP9MzGPiyKKRa1kTuP-6zJ7OQPKvw0QAY_uklUY_Kpa8qBS8hHwHWwMkvjlVetveH9Uhj3mWD0k8JGG0vRj4Wybd6N0HcqEgOwDvrOLYSmUj9CCvyRWqVv5ZP8f4nDuFda8e-ZjHNMZQNQgkW-U9qPUByzeE0uZRPgxEjnk7nEX4om1GA6WoWvsCG7RKDHdpygq87RMKbY9rUV7B-jraUTgzn53AcrH6XWbEz33Nk0nxhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwtPyXg7KhlbBMbxqa_RCdMGC3E4o7mM0ehXNAwxJIvS-nat5C8Eh9wGMxMF-Ul0ZlgGb8i-HOnF21Mx8011disWXDrHylyx70KRCKKt1W_waOJCCKPYVydQYKhbnxmQ3_keQlVtttHrp1t8tzE762Jq1I5nhrwqjyJ6kSln14cQ-3Gqb61m7QZus9hQin1BDN4WVJrBwLh5IKUp3AWYrog4Gv5_mZ2KeZOLd8-Q9Y7D4gtQZaukReX6Senu7w3TswIh_Arf6BFbKi7XTchHlz6QoyCK7ziK52dcB1x2vnDIcBV_Bkrr7PYSEb5Gh1N6VjrxyXpO2wvE6SJzDFgS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzKE6uSMbU7sZeWbgnKfm19mNP_SuTxESzX7tjBIzcNrhaGWEAMY_snjqqgdiEZpwWcBZvQHJKn3CewzCmq3a90MRwQpMUEpQdl8qc6Q3u9CDOcWO3FAr92cMt4ckedyhPSyARKtTj7by_YrlUOtZ_mTZDnGXE2IhEPmZmxYCu--cznmh1hLv7GP2xvnqTTfmiODgEqwdMPkUcW36cAfBJM-Yl82PCdrbJeLSg5QTDhomeZQFtic9ztiuEj77gbxK4MH7T81DLwI-kp60O8WPmdOXpLg7jmoXa0UjNt-ceFLL5AJNZJ8Lv8jbp2zo7xzpVlt2u899xDMt_M5GvpA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=CkR7AB7gqgTIhXt8dx0ZN7Uqy1LXtzYw_YClOBmE1DjVE7rDxmtXcB6Zmw9fwfkMRUQ5AIZEwlJOVBg9Ql7XGi2PjtteDh_rlDj302bf01hfIZAAm_07AIFsTc9RtcKMVxOhQrpiav0ZhInUhkn42ySRuu3rfvyge3LeVvx8mrGoMGDUsI5bjbQ_og1q6gi9skWp7UTZxywTtzCwWkoHKbBzXh2ZVn2QxSo1DZQuOS-iA-nOmkXtg4bdYPcJhfpeebZ-rLeyfV0XRs5y3sL9SMLCUICO0Ld9YoVw1q47G8Sm69IZ3wAHsGAE1cxqSDCK2fagaA5AZqsID1SjxCvPuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=CkR7AB7gqgTIhXt8dx0ZN7Uqy1LXtzYw_YClOBmE1DjVE7rDxmtXcB6Zmw9fwfkMRUQ5AIZEwlJOVBg9Ql7XGi2PjtteDh_rlDj302bf01hfIZAAm_07AIFsTc9RtcKMVxOhQrpiav0ZhInUhkn42ySRuu3rfvyge3LeVvx8mrGoMGDUsI5bjbQ_og1q6gi9skWp7UTZxywTtzCwWkoHKbBzXh2ZVn2QxSo1DZQuOS-iA-nOmkXtg4bdYPcJhfpeebZ-rLeyfV0XRs5y3sL9SMLCUICO0Ld9YoVw1q47G8Sm69IZ3wAHsGAE1cxqSDCK2fagaA5AZqsID1SjxCvPuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WleLbUb4cIxwDo9TBu5ZxHDnPFZcDdKM1F6c-7Q1dZPeY0FwFQvEL3G5voZYoGSKkrXypaNP7txQKhaS21t4mbeEcX3WccOqr2cbtLKv-qdtOtjRCImd3-MsZbyVGeUF23jZ1jln6R_5VIcriNl63CuSMSr1Byu9yKEKjOw68gfNJIl93DcU8Gr5IuAnNTVTp6xDfI5vxIO6tDpv7pQjPpLY8EbhWBH_ZN2bi48q6rkPwYryWfPRPtiv92wrP48fp1jV2KuLcny4EF-1VlvRjGI43gA7wswMh8jBuFXSaFq71WcKsIocKUnw6GLer6j500-byfoSq_85rnJUNs5SXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=KCDbmqeuIFA3KC_dQxdHJYbEVcTQTeeMIGf6WivlfjYojgteI6XmifoQ60RhO5tjVvh7h2LJCrDQBBY5dhUj_embxxAphanziT_I84WTbRy2r2q8p1oXcSKcS-e0DfUYtVv7YsUi6hLNFOMJbZAbsWJ53sMDXXzyZQ20nMohg67BqU9w_uF1TpmhetXNFhErO3d3QOLWTgdKcD4_GcTyxmHoBN0jHWG7UrlGi5qhlcHjfYXHB7zb-T9AH4UrHdQEg6ZTJ0EYHzzk6jdup3BDehKu1xvU2y96OiT4V247wxps3lYqD6lcLuAxqbvts3a5sdC6fkxzRBYqaLmJETFsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=KCDbmqeuIFA3KC_dQxdHJYbEVcTQTeeMIGf6WivlfjYojgteI6XmifoQ60RhO5tjVvh7h2LJCrDQBBY5dhUj_embxxAphanziT_I84WTbRy2r2q8p1oXcSKcS-e0DfUYtVv7YsUi6hLNFOMJbZAbsWJ53sMDXXzyZQ20nMohg67BqU9w_uF1TpmhetXNFhErO3d3QOLWTgdKcD4_GcTyxmHoBN0jHWG7UrlGi5qhlcHjfYXHB7zb-T9AH4UrHdQEg6ZTJ0EYHzzk6jdup3BDehKu1xvU2y96OiT4V247wxps3lYqD6lcLuAxqbvts3a5sdC6fkxzRBYqaLmJETFsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ikHU-tMozsNS_cNx2HKMKsgZb4bqDGungIM1gsDjlkLKQ6fp4W6_pO54lnV7gJT6vJiGyxWsdhDaXMFoCsMWP7UpFXKz33f7xKKh07IKpGibJlofC17mWGZRIrNdzlFCtAILhVu9loIvPB92OTKr2PxKjiP5m6mVtlzVU4yjt33e5PF5ae3eIjV6Z7AFR4KE1AHkB9gT1v3W_PD3_8jAbmjduMKKK51YjkQilpd6_5KKjaghDOpkPVwFG_ekQebq9VJdJpDd2KSnBw_6hLQ3Zdggg6YB6RQpmA0YjmQNL3_PnBRixGeySm2HO4ka_koXEIO5-2EOVyCuwE35gE1Vig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ikHU-tMozsNS_cNx2HKMKsgZb4bqDGungIM1gsDjlkLKQ6fp4W6_pO54lnV7gJT6vJiGyxWsdhDaXMFoCsMWP7UpFXKz33f7xKKh07IKpGibJlofC17mWGZRIrNdzlFCtAILhVu9loIvPB92OTKr2PxKjiP5m6mVtlzVU4yjt33e5PF5ae3eIjV6Z7AFR4KE1AHkB9gT1v3W_PD3_8jAbmjduMKKK51YjkQilpd6_5KKjaghDOpkPVwFG_ekQebq9VJdJpDd2KSnBw_6hLQ3Zdggg6YB6RQpmA0YjmQNL3_PnBRixGeySm2HO4ka_koXEIO5-2EOVyCuwE35gE1Vig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj7_4_wFOUWH1WyvsRDGsySO4ETfvjb-rAgFDMp6cIuq1lB992oLui_Ue8qSyxtF9pivBkge1w4c3CuSAUjJV0eTL1k5YGtUIPy4d_cl8vduT_eblVfxkTTqsS86Z7PvY1T-SznG4SEx3ur1VxsGkzO7O23RBdUVqcZk6LeGvOSptaldcW1Gcvwt6hcQXFAyV6r-6os_UdzrIyj-csubcdJXjZ4EcdYf3fGA13jiv75UGefEuuVjPm0YLdcjM1ngAmFw3ktwCNl6vTjFooY_tPpeLT2YKLmDXTP5mBCyg7sauacdBOqmL-Xw-kK2ImTkAnj38AAfu65vUSwi0uo6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=e4G7t1MGl0_TaLr-jDLvDnAA3szt9n8JaKsdz16egJsAU44dxC-AW_yR1uGadESaoInP2bLtOVrCpSDReciHWDt5UUqcvW1ODlXNcxg0XiVPnELIOGP7W9kDfszMEYVCqfpHhJTLOfC1EWyMaxXU0md18JBecM-mZpI_Zx-DCIo9cMebUHiwaqVmvtsGZ11307s9ZkU3XcrTetZjuhLi9LfS-2j2A8s7GmMdDumdZwojkyHM5K-K_Xk-zOfjtLQe4LPzQji2NfSiyneDKDj1N9WuqWe6LjFkWf-Eje96lIb5spZP9SZ67ue2yW6FcTETICOHNmGOX1e8WrRgUiNRPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=e4G7t1MGl0_TaLr-jDLvDnAA3szt9n8JaKsdz16egJsAU44dxC-AW_yR1uGadESaoInP2bLtOVrCpSDReciHWDt5UUqcvW1ODlXNcxg0XiVPnELIOGP7W9kDfszMEYVCqfpHhJTLOfC1EWyMaxXU0md18JBecM-mZpI_Zx-DCIo9cMebUHiwaqVmvtsGZ11307s9ZkU3XcrTetZjuhLi9LfS-2j2A8s7GmMdDumdZwojkyHM5K-K_Xk-zOfjtLQe4LPzQji2NfSiyneDKDj1N9WuqWe6LjFkWf-Eje96lIb5spZP9SZ67ue2yW6FcTETICOHNmGOX1e8WrRgUiNRPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=UnwUKThZbk1DUPpnNugYw6St1kRhu_PS-wSaIrKazp-L2eHjsthfIvxRtz0b5dLSVhyDwZmqTHEmF5-totynK3nEHDwNj-BO_237FfXy4A24zmvi1yJ3UjONczMjpXX8CcOHnQU5wbJE-NFS22QyVu1YYXLCrNkhncRh4ia7ldYMOOBelOVVi7dVLB2b-W4S7IMc40DgrbJNZk8As5PzXm6edD8YxA5C2lhe-wEMHlQqSRCNzwJQ8tCd8Ml90Lsl8Jox8e8IvG_LODj7dss9j8YvPxn_k3b59IHNOte3GwcDQuvqsK9mdcXy84GNKY3n234aMTTe1CZtbd7kjvLIiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=UnwUKThZbk1DUPpnNugYw6St1kRhu_PS-wSaIrKazp-L2eHjsthfIvxRtz0b5dLSVhyDwZmqTHEmF5-totynK3nEHDwNj-BO_237FfXy4A24zmvi1yJ3UjONczMjpXX8CcOHnQU5wbJE-NFS22QyVu1YYXLCrNkhncRh4ia7ldYMOOBelOVVi7dVLB2b-W4S7IMc40DgrbJNZk8As5PzXm6edD8YxA5C2lhe-wEMHlQqSRCNzwJQ8tCd8Ml90Lsl8Jox8e8IvG_LODj7dss9j8YvPxn_k3b59IHNOte3GwcDQuvqsK9mdcXy84GNKY3n234aMTTe1CZtbd7kjvLIiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EfRaI_99g6V5PgnPGtvyYOfBZQlichXxDRhUWGV7zB4x4127YkQNmirBn2JbCvG7EndEIhr4hSM7mBwNXQnQ_ZHGEvpLm1m9x3hx0aMMXj5hKZf8zJkdXfFQZTShhtyzYBboJSEJQ0MVCPWYam8oiK3LxQrWFEnv1W9wFJkwg9i_dHjYjjSDCnLSkykTzOFXAa-QMB5V8wNKd07dCh10bmFVsnsftPouGIk4lvEzNMkDIzukG143JDaf9rbRUEYC9HctgEKcqJwP9bSSYwvFhFbSPeiTYTqiZogYTYIAFY--lUanTs7HqwHrL7nXgo04nfMejGAxi4OhvqkbPkA5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfbK4QWTSJ1XjZZ7SkDtzo_yB3yy0AwzkEB-uAGHJW9nKOvKpkIXCskWv8mttKoW3pb0oCEuTG0BFKeUXvzt5y6o3wOr-C3GsTo-3yUbfZpTlyhnBZosSDTPBIQ4du_EgfQKUf4OUgXFs7m5FCWbmUMB4basWPM7UIKlwfFFVLMHPFPpbMDuP7Y4mC3HViDUvSPdI3gOxpFfAz7luO4oZuO4eAbLu8jCEWbJ4a0FVsLJGHIoxyQ1wNEJgh--T28CTGuAC7uJ9QdqYKvzJYzJ_QMzXPJ0swQdCpIoXaXRayuzJL3c5egYYoZUP4J8G4ZKFkycieYuvVDkJRi6N1OW1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SixTZyetgjeyZRUlqoZSzzw4zeH9m2Yxiq-49lCaCA2S7rblf6TPMA_peeLI8dkFz6-s5sciZOIBLc87hfHsemJjsuKcJWkMbt3HPlAwog4uzhVDagMp3hGnIvI1dMoUz0ueX4uw9KDYaMbG-roLkPOL2IabFW3rAClzNwxM2wBPOaT7UHjVxUzoB5Lrj7Kv0Tp3cGYQavQ91ivc7SoJPKWF6NSXb0Rjc_GI7VCqXoIPavVaJIAaRNvokSa85MEL1F6LV8sxIUfgdKyd9neDEPmtRh_BDa8RFZYjTIc7u9ry3UHP3YFbHIZTNSzamVgc1QUA24hGRfbspBrIsEqWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp0a5WGjzl_ZrdiMzt4Nevuceuxjy298ccOkJ_9YTEr26NT5-Sv_cbKfFUAY4CY25cz4ZBmmM0_lHmwAWVCU15ajYyzl-u7TsXjR1RvYcbTtve7L8zjGPquKnFW2elMmqYDubGBZUtTyvh-sC59KCXwxc3uw479wYjkqAaU5SAiHzkfzr_7je_IqfugDw9tyPghi1owxvLvXWrNfZuk9mNyBp5FTpY_1Y0C-wY3Ji6n07wGgXqEqKZGzB6j3aG8vtTH4uo0Ru9fY_hdp036BP65vKY0_yG7lioG9valedo3wnzcB4aCTVmMsTc_XiyaF2JM0jiiojd0Rp56NrhkdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glzklcswa9oQl5JIjTTjEqOsljLvsR3QcG2szqI4taLLIcGXztndyie5DaaZ0CkTHdaCSGWmDFOjL7PHK5XRqqVRtqJTNvFrAFOSWease-eFoByK1Hfa4LkxEUQXTt8Nd-Kxg6PHHWP7qqfmss0O4CG8l2vMU5WUXxn5ttp9j3JxEdS_HRHdIMpwjL2NDj1Cdw0yAyau7rauyfJidSabV7FKTjs9EuHdTwLgmjy4Cc2ZepOq-4IeFgFKBS7LCszKTQqfJ_1uj0xGWgDYhFosx3eQS3pAuyQvlAYEvj5eLbxqYCtLZaiaUJgVMWoEBOMK3drPPLp1sxB7f-9zmDQItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYaCIvA62oEjS-i8-E_BTSjFq7hDNMd0OECg-ovawJN6GBbwBtWxOSP5XJMVlCee8YLEa0II5QA4A8EGPYIw5aF9fwXhx01-0jWBZCAaQBiMojq5ViEhsCcUh_VLgxUQouY9DLQMYRV09GElwSCaxQv7L5jK6DdW3pkL2x78s3NqPxdJKSb__Nl9wUzN7JuNziFWOl7UU-St0LZd9hTL9fKQAJzozP3DysRCczHUv7yJ3gx_OIQJ3qkhhA86yghKrddoxKIRu5Rh0tFLdOvfYbXutSS6b_RUWGRCLPeo7oQ39Q0FAcX-aEokI8_HaV8-R6LaJ_QmA7w33VsG-9kJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXSc2XPpGH10g-yJ0DKHry_lh9jUiIgRq3jfZiQEhnENOQFVKY-ayra7vwChnQ0K64Q5o5FIVtsvo7mjLl3n-ohXchbf-IPwoAWU7lRUpUzgsFRlJnrXR8rWwBDR5h5vw8k3hFey5pX_JsikjxaUY2EeSd-YZ9mh-dvBGtG53SpF2UuOWgu9cJyRhsGDUkikZ65Zq4zcmUFMaY9YDTbiHN2gvidjhwXqChI8-AFlfNLnTsa8Tawo8kvVWbIf90Oo--yBZf5dETRsZv1xU6ORnlAuceb-C0_shC_CcDYtd24CqWNhZNwyOZZNLYpszsC353NQHL0McaaI8yp61rCNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=Y-mnH1zqBZAFKS40MzJx8dligXdVIHaueJUIR1zef8G-8qrF7A-ZL1DiQ2QbdTm5hR-R5pdYfCIXnhMD5mv8WIh7dEGCbRwHy65Cg73pfs4WmuyB0m0ksRQ2hus_TelekWmoBZ1W3G5zTf9MZxGM-4T-reo4ITgpIqVJ6rptUVrIoh-Hd2ePhJjbI1vi1dt6e8xeCAgC385XCahCz-6ToKKuVYBt1s-cxkhF5TUv5WLCXbY4PBzqubPm4wSjtpqiaNw5rIWJkup_ij3822y3t4lcX7L7PsIPtyUJjtyPetIU3eeBg7YNGW_0R8ymjoOntL3CvTE0DI4Uspfai3nR5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=Y-mnH1zqBZAFKS40MzJx8dligXdVIHaueJUIR1zef8G-8qrF7A-ZL1DiQ2QbdTm5hR-R5pdYfCIXnhMD5mv8WIh7dEGCbRwHy65Cg73pfs4WmuyB0m0ksRQ2hus_TelekWmoBZ1W3G5zTf9MZxGM-4T-reo4ITgpIqVJ6rptUVrIoh-Hd2ePhJjbI1vi1dt6e8xeCAgC385XCahCz-6ToKKuVYBt1s-cxkhF5TUv5WLCXbY4PBzqubPm4wSjtpqiaNw5rIWJkup_ij3822y3t4lcX7L7PsIPtyUJjtyPetIU3eeBg7YNGW_0R8ymjoOntL3CvTE0DI4Uspfai3nR5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Ozim1CdjFR_TUyOzmf3db6pFdYaU-MIVPhsLvhpjzi0byMjP7eFYVnNg5zDqp_m3oudVBgXMe9Mev-617X76iv1Fc-52soz-BM3-xOO5T-vSYLwBYypGH1GSAAgE_xSOEurip0p7RHyZT0ZbO6RyX2N_WVex_tkij7LzkTW3MIHngbhuSTyDzrYh3OADV6zrgLhEmoTdVcziIaIzVQTl2YB8rjPK-fTLF4_0UXOeePpkvgEN1XBNaWnPMPuAEWWAQBJw3B2RIu6WYYdNAw-iSQDLInW0gkNYR128KAXtCppsGgATKvTZB-TZS2uBbqw6d6RmivCq7dS-P8CYRMHJOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Ozim1CdjFR_TUyOzmf3db6pFdYaU-MIVPhsLvhpjzi0byMjP7eFYVnNg5zDqp_m3oudVBgXMe9Mev-617X76iv1Fc-52soz-BM3-xOO5T-vSYLwBYypGH1GSAAgE_xSOEurip0p7RHyZT0ZbO6RyX2N_WVex_tkij7LzkTW3MIHngbhuSTyDzrYh3OADV6zrgLhEmoTdVcziIaIzVQTl2YB8rjPK-fTLF4_0UXOeePpkvgEN1XBNaWnPMPuAEWWAQBJw3B2RIu6WYYdNAw-iSQDLInW0gkNYR128KAXtCppsGgATKvTZB-TZS2uBbqw6d6RmivCq7dS-P8CYRMHJOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=CS8FnFxQ4jCBEfr7f_g2bN9uq8DYE8bOYDOBgBZEvWrTGpQtfpWUCDwQlzB8uVfoNqQiw8JqqgLrkr9F4-3VVkugGpPJEm-a8FOwJ0pwR2EiVI1ThhTCb86Ak78N9-Nm9Py9IfKRiT-tEmiXNVpQfs7AmlzQva_H0V7hTGmj8Z2Ps9CbggCpG1au2YK9aHuYzy3yetJn_pGmGyPZP5YvDn_t09DdFD-uWI9bon7SvnGDi21dai1jY9TVGQduh7gHuP7Q_0qqd527y3kNxm-gKgo20f-10WECttLEkBgakAPFgPt8c4YRqERmNQAjk2JBnFH2P4P_HrjVHf7rGsujgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=CS8FnFxQ4jCBEfr7f_g2bN9uq8DYE8bOYDOBgBZEvWrTGpQtfpWUCDwQlzB8uVfoNqQiw8JqqgLrkr9F4-3VVkugGpPJEm-a8FOwJ0pwR2EiVI1ThhTCb86Ak78N9-Nm9Py9IfKRiT-tEmiXNVpQfs7AmlzQva_H0V7hTGmj8Z2Ps9CbggCpG1au2YK9aHuYzy3yetJn_pGmGyPZP5YvDn_t09DdFD-uWI9bon7SvnGDi21dai1jY9TVGQduh7gHuP7Q_0qqd527y3kNxm-gKgo20f-10WECttLEkBgakAPFgPt8c4YRqERmNQAjk2JBnFH2P4P_HrjVHf7rGsujgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=otG2Tf3KohNIylpNIZLxqj1QsE8JAKdIchJXvGUe1tCC9DzBnfDnal6X37Tc7_FdIoC-ji4au42ZeuSD_nWk77kMIbbzIDg8OfL82_Lmcx6i99u924GACWnPxp4AnhIyTCCCNqRVhOtqD8fSvv3TL4Lx29uty-Ey61FEQEzw-ij8mnW5m-_eEhLVlWZrmitPQO96OsYZKMrVKyNgN2UYRqWo25lmrAt0gJ7pTcf19lPE2e9v38gfCCjGFjQ6NRq4Ee_K9KZCTyvy50FO1eN6S-LxHISI1_YD_ngQRyglw9gtJVAVzMpaome7OyyJvClWwSMnNOXvtJqf_wdLKsoycQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=otG2Tf3KohNIylpNIZLxqj1QsE8JAKdIchJXvGUe1tCC9DzBnfDnal6X37Tc7_FdIoC-ji4au42ZeuSD_nWk77kMIbbzIDg8OfL82_Lmcx6i99u924GACWnPxp4AnhIyTCCCNqRVhOtqD8fSvv3TL4Lx29uty-Ey61FEQEzw-ij8mnW5m-_eEhLVlWZrmitPQO96OsYZKMrVKyNgN2UYRqWo25lmrAt0gJ7pTcf19lPE2e9v38gfCCjGFjQ6NRq4Ee_K9KZCTyvy50FO1eN6S-LxHISI1_YD_ngQRyglw9gtJVAVzMpaome7OyyJvClWwSMnNOXvtJqf_wdLKsoycQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQd5JiO0ZkYcWTvxe0dkCtuPHsJtvxqtBJtN4wEczUyrlpxuAX2ZBY77bfHR5mtaorq1hr9rBoaBVy-twRRQhOnwWD-zQmLT-OXV3AxgoPPfB6tGrhP6fN-PN5eJlmGzu65RQ6MEQ3ZBT-OU9bMZ2iPF8d54ScK0eD6sJ4_iME8JyrrYuHCdUWQ8Pgq9HZxhr7jSGN1ld5I3hzrjDGMmntMV6i5ysD0efIBO4CGSIrgYMrNJrco-AxEJ5y7mmDJXliEkCmfgSmbWsVI7OpjrNc0Ew14alo9E5HoKiRQ7L6UuTB1pAH0umNTR4t1IyOSxf4c3LItsKfOF-odBnRQpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHkjLpLPRIXAhDGLHs_EZIVh-cr2lOpGM1cEYQSrISyyFYcTDDfUu3YW-SE8xRtDCxxebHluPxLhQclimMzMA35C-Rqfeg1p9-8lVkiCNWQe705SzrL9q9U9YOvTPuxLReM77QCpKZ-tbjhTn8s-d7IXROq7RwwQQZtvFTuUNbeJfrXLGyfRY_hdLXIm4-DmHJIPDJ5NRTMrrOtKt8YOftqdGmWNcoBTI3sZM1Xhm1wsbCc_R8MIUa4-qkBMi3qLRej87QgnxcMBeX-8N82V8ZfT-Tn8f427suTXELD9tMNrXHAgGkj8J8XT2XaYO7BW2ZGeamN7m-7UYNT2LHm1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=YKd8IdgZ3-FPZK0DFEWUuZCLh-SHFLJUAbgcKNKsEYtvV4bH_jxgNc49tBgtOYX8gpuXGHjGbz8cY-u05Piok51PrZ1dItFa6rgVyY7Qlk8fBYCMsSxvPwZmrkz02Hgoc0YbmNlXOlgsAmLmF04LGd7gnmZeOOtw9falUI8fzAmROXChJ2_MdqGx1pI9W9JfAi4XzRZz7RkJJX7x1RqZFGzKBGnNAw4T4XXTGFTT-LUTMhgxpGSFzO13J2UUBF3EhCdxI2DbfxSpBTHgdIGPOxQ836GWuwHTKSm85icVwHNOLuz3qKgF05u9-1O-BO2zKmKtKS457LANVpeH-4gP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=YKd8IdgZ3-FPZK0DFEWUuZCLh-SHFLJUAbgcKNKsEYtvV4bH_jxgNc49tBgtOYX8gpuXGHjGbz8cY-u05Piok51PrZ1dItFa6rgVyY7Qlk8fBYCMsSxvPwZmrkz02Hgoc0YbmNlXOlgsAmLmF04LGd7gnmZeOOtw9falUI8fzAmROXChJ2_MdqGx1pI9W9JfAi4XzRZz7RkJJX7x1RqZFGzKBGnNAw4T4XXTGFTT-LUTMhgxpGSFzO13J2UUBF3EhCdxI2DbfxSpBTHgdIGPOxQ836GWuwHTKSm85icVwHNOLuz3qKgF05u9-1O-BO2zKmKtKS457LANVpeH-4gP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbYbClUZ9AH7VID_IRV4LIw81BwDZcG_AzuONWSGkCdmn4WKJbM77-SZBPhVtcsnCnABMPQ2yY8RbLF6ZvERhdG11acCwyrRtJHbMJn6wDNeRbGJ8avi90y0kXBVwt3ZE22WlDP3XEhfY0ipP0vaRigSTARUhCo5YBMk76M7QIA48tJKQex-3EFepw_sYhP73F5KWOukWWYe_AKUO-mR09aJTiMSkMJfGWJgsuO620ed8_pz-B_lXScb3utbo9bTN9MT7UgPKxD5XkjgZjva1FeV3iHySD1fKbsHdCw2mLdwCvt1xZ6t_fcb1PEkiOH0Fvq-U94UwE_oWzNpDVwIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Mc_qx1h6SWvitPfMyVNU8ysahuN_fzao0xNEQIuhkg339KzXII3AkuvKIwxudNvNnU5S4zeqmEEOAO6gzzzPPEt120_kpr9Rsl7n3Cayse9Ujti2xH0VF3slEEXSKwL63-zzRDKXSs8GpokwSfXlAUby2FBVy8VYQqAp30_5XZH7rMNFEcpQkon3vVMvJW44mjMw958Ya3jOn9JHuf9uIw1bsY6FbN5hH3_5PeMDK5eJ41LgXonfndjnQRkf3yicv0Cs2PKTxAuQfJYcxHhKUVVaKv4qahpk1_ZkacbcaGPyLCA3eBpRgpcshI4rW0-clx1S8jCHg6vn9WlBmC2xNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Mc_qx1h6SWvitPfMyVNU8ysahuN_fzao0xNEQIuhkg339KzXII3AkuvKIwxudNvNnU5S4zeqmEEOAO6gzzzPPEt120_kpr9Rsl7n3Cayse9Ujti2xH0VF3slEEXSKwL63-zzRDKXSs8GpokwSfXlAUby2FBVy8VYQqAp30_5XZH7rMNFEcpQkon3vVMvJW44mjMw958Ya3jOn9JHuf9uIw1bsY6FbN5hH3_5PeMDK5eJ41LgXonfndjnQRkf3yicv0Cs2PKTxAuQfJYcxHhKUVVaKv4qahpk1_ZkacbcaGPyLCA3eBpRgpcshI4rW0-clx1S8jCHg6vn9WlBmC2xNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yshww4jwr-ucjbhtA6OsmG0dJ7d_jHSWiDYUA542-8T0dcKObrqiSPjHa4xcliIh1eYCpd85uMjtY3DFcTk_SUaAez_acrHLOMbhnb_wUVNXA-WyBtMytrUD6ioGPCTqsHQ1P72W30r_tZEKOc8Q2LjPH2xM0kW9ZusAQO7s5V8j55sTHSX68_OSaoSDe8VIL0MAMgO5N1F_JRNuui2leFiHu4IwhiyTopaxIOEyIiqphNcYwJxwa366QUTcv5NqFU8yY2IGMRWUSHuJWcTQ-QAB8Mnuoq-IGdiCfyj_xMxa78pqHaquX4xstGRaV0BO1TP8bDB9OSOgfwqW23r0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSHi1X-Uo9bzu17CmaiMmkoMfMC2JQNi8JXDNi6BwhOtRbKVISu2Hyn_8frJGYjmbQAZEpYrUehucqJby1zbKg2dmYW9mG88NG5FjfrMlIIxqS6GCjg7g70ZMIlAGrUIxUenMhFdhH4uaTOkp4C9_cdTAv49SlwbFXjjtFdyKcEfTUZFJtr9KHiDLhT6rgIKQYL8MYAb5cxSAiICLQqbnJGLG9Iokysq4lfaPUIqN-Yk_oHzA9Qesh1YkOTmd5Olwg_vR7LpDpjlx9U7vX-7dSeShtKwRJbBz1K9OF1GI7vE80rEEvoYg4703XHHmBbuNLEElrfxqf4how1Zd3u4kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=N_BVI5wmAr2xK45EYSWrJ1V1d73h3wD-QGh1MCwuwFraIV-DVk8uNlOpa55Df-M3JZh0D_U6LX3869SzXGjcfDjqw0_-BF1SLjUtVGnU57l33S_Tirsyk6DFk-kv-HCWtwgvVwBCqC204q8GbacN2tWI1No1nwo3zaRdKUZHYYmu6XHzAgpn1l1Cmd79DgidZmF_nYlSSoXyNadJaoApOIy8C_WZ3QeLnVjzCAX6YsrX0j6JdpsoJ0HLcLez0Ad0SZ0zoEyX_dKjkeNQE148RW-OZClypCKpgfii_Eia8cYeBzKksO1Do_wcm2QFZjoIIhyylQPMfXL6ilz6wuZQfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=N_BVI5wmAr2xK45EYSWrJ1V1d73h3wD-QGh1MCwuwFraIV-DVk8uNlOpa55Df-M3JZh0D_U6LX3869SzXGjcfDjqw0_-BF1SLjUtVGnU57l33S_Tirsyk6DFk-kv-HCWtwgvVwBCqC204q8GbacN2tWI1No1nwo3zaRdKUZHYYmu6XHzAgpn1l1Cmd79DgidZmF_nYlSSoXyNadJaoApOIy8C_WZ3QeLnVjzCAX6YsrX0j6JdpsoJ0HLcLez0Ad0SZ0zoEyX_dKjkeNQE148RW-OZClypCKpgfii_Eia8cYeBzKksO1Do_wcm2QFZjoIIhyylQPMfXL6ilz6wuZQfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=H3p7OXt3RAwakYGTEcBsItJIL4nPOlgLM_sHoy7_ZzpMIu7YL_PuYI5HH16rk6lWo2_HSLsPeZ-bDZZoYRA1gmSceSNypP18Q5HRlWvNRETtVESHEtAuA4D6JVjfO4cQnx_hQTRoQjkAkiHxRyJa8jHCVZFXRnBdgwn2jmKuR1D7l9G5gh1fLWAU5xuGJ67mXX_hySABOQ6VIbXhnne_cSyhPUYYVE6--B6yJUD3tB-T4yL3FI1FKwd6m5lXaCBg4bGlbkxvcsvPgvHILWNvHVWPsv9vNTh29_8izfzKV1ucoZxCfSRIg61aSwFODuzNL8WSxYKBeTFxNiBgtEicYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=H3p7OXt3RAwakYGTEcBsItJIL4nPOlgLM_sHoy7_ZzpMIu7YL_PuYI5HH16rk6lWo2_HSLsPeZ-bDZZoYRA1gmSceSNypP18Q5HRlWvNRETtVESHEtAuA4D6JVjfO4cQnx_hQTRoQjkAkiHxRyJa8jHCVZFXRnBdgwn2jmKuR1D7l9G5gh1fLWAU5xuGJ67mXX_hySABOQ6VIbXhnne_cSyhPUYYVE6--B6yJUD3tB-T4yL3FI1FKwd6m5lXaCBg4bGlbkxvcsvPgvHILWNvHVWPsv9vNTh29_8izfzKV1ucoZxCfSRIg61aSwFODuzNL8WSxYKBeTFxNiBgtEicYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihz34X9VForaHXxHVRrcXJ4E7Gq1DOJyCNFKqC8eW_nIIHMgEQplGBjmANp4NNztNbD5zZSAzm7uiMrBCpdc9OmkkFS6QKxORQG_ymZUmActfed29akAEXu1LpeLYEE2NjzMTpHZuN66iSOpcPQ3OPnJGsRVnMbTFf8rwOtyWue0ByvH6uQ_TXzs4ZUo3SYC9yivH8xO8zYq70XqL4n-kAczvKtfdY2pdav1w-1OHqZIABiR2N5XAN6VZVVtF5NoM0vF97f4GFACO8qM7KOnkAHdlqIUXq1QVgaiZY3UBGfJ3Syw7GoGO-4LYQVj_05fvro2rDGi39resL7MmyvSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUMHM7Yjd0pyBglwPZl5wXQ3QqETElDdXafo4JkQ8wbvXb7fgUQ-T2sFf2_iYFJasUxci_dkJQFI_boL3zbPisO8Sr929wQntdBk7eqt58VhexC9K4lY2Ho8YhDl6cnuH8e5fS3s9eN1GFGkMCSs4IrxKzEKmqfAM7cjZwDSE3HtPYFIstq_LJnKER3eEqGi1gDxcw9FreJlSphWbk1ctHDr_d70kI4GXo13ja2JX8nR4fzOErFSlcByCOIMP7gJOWZ8azFEN3JbHB9ztj-GgUBw7PFqiv4d23lytxf7hGZITMXXYdBJj1PMFxotkl2LP1I2q7mW6xaFzHwHdAegzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgk5fIcIYcEGUinxTybiityZcrHX8Eg9Yw2Ph8Q39QVu-vomzKTCzXY_k0yOvBy3cSRsyzJqTPxfP2ey3hZJcpv2RbBAyg7bbFOXz27kBmpNARXWBThA1w-0f24FpaMtey2JS5Si9L-YL-VQExShFJK_1ih63-83BrNEKVL_1FKVVzZwbfX_Y88N7uRPge5VroSSpFaeM9X-UYSRElqIiaOJdWTVQKHt67YGD-VD8aNh493rfxpRYPk0mYHvONdMZCBx5Fq1VNyQecuMJJaGa-0D7BmLydmmZKyFdsKsHkAviM92TX-WJo2YPzaYWuPFY0Uz815_g2gm89p_J1PqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=WoIqFNJjJ7uLllSzAyHeP_gM_KuKg7dm_h0iEnU8Px94qKMoYgwz3KGX1p25eJgnQNBCqfUgnryG4X_Po2rtq2E9sMYPRyGygoCbu_FljDoG_Wvr7T7Xa-siFqnP1FVDDts8rQ3TvCxUm6FnnxNfC0v2K6PfsKnRtj5e8susM7RUB2S779QArY7IUJuQ1fgDwBaqS_7Ocexdq8AFAMi6trZib4eK0F6083fBEfr7YRwQKVUXfqWhJhUmkd5RCs4BWum9SGMWaei_-H2UZOjuJGSFEzZkXuCaP1yxcBZIcWDB1Tcjm7Y_R0ps4QjEEsiGpZttPz99lGJsS8QQ1_Lz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=WoIqFNJjJ7uLllSzAyHeP_gM_KuKg7dm_h0iEnU8Px94qKMoYgwz3KGX1p25eJgnQNBCqfUgnryG4X_Po2rtq2E9sMYPRyGygoCbu_FljDoG_Wvr7T7Xa-siFqnP1FVDDts8rQ3TvCxUm6FnnxNfC0v2K6PfsKnRtj5e8susM7RUB2S779QArY7IUJuQ1fgDwBaqS_7Ocexdq8AFAMi6trZib4eK0F6083fBEfr7YRwQKVUXfqWhJhUmkd5RCs4BWum9SGMWaei_-H2UZOjuJGSFEzZkXuCaP1yxcBZIcWDB1Tcjm7Y_R0ps4QjEEsiGpZttPz99lGJsS8QQ1_Lz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQn1EOAXN65SO0AVlJAxCkQZLGb5j6atBmklx3DkFGqNL0Y8xiSiHy-799mfxOkHpzz74NrwF5rc9xlxisj-l_4qEQpb4p1rTYq-ZyO9dqDOhdV-GLU-aYQ-hi-F9mJLxZXuMfJXJZyEDTV8ZwIuXFfbUv6JCmtKmwdafLB43YK7Bb_dJfrI66rRrnFPz_4igyTG9H3s7IQRtm0xyn-0U5N1qY4FiGuZCrqe1UtspZzjKna_QnNENv9cOqhEJa_TtWpm4hAJI5J5LEWdHsuldPPR1WmWYynKgQ0rzbHJO-pjkKBA5cdPDD6km9cPiq3kq7-yGkToO8Dd3kP0ylEjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czn9uIpv2x6lDu9iWlubox1FDeasuYNig1yHfkmxgwsTDXf71EtGZql6vUxn8gXDuPquUxNfNHd1nWRyzdFufPA_yBJGDOOya7gTH2Z2QzPpDiIUoZP9UOGcWPqByFllw68tLYvwAmpvmNgp4mnt8nVOWnuAuLFj7URCl7pZEj27H-_7RfcNFVUwr90JPaYvkqBNrThlYGxuLg37GFeuCaUyUG-IMRrppFqDVT8lQDC0JFBKtuKkpTpbLP1TthAhlDXRrPMYmtvPFyk1gvDkvIJw1q8ppW6ZxpWfvOOCppkov41ep2ykumtv9BkA7G0cjs_FWFCzb34xM824K-oDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBgOdGb61520kgQVoEYVkPtBdXtclU99vu5VUSnT94Sx6fQnRJh8-zz0I-YbLXIdejKHqzsa_ywlQ08oE_NSgXXqsd_GyVxQlikb5QR0GUSlNn10bsTHa2A8IZ6F78XeKAQKv0Pm_6sDSG9VFnsnJDjE98LrO2UnjvbxMGQm5AZsn92T11Cd3v1U1ei79FbtCMHpqSoYY72YviASgOOOHTF5qwb-1zM0OCwIV3quJl6TdxFvZkqt9SsA5eh6oAEBP6SwkWWk-BfWdCZpOqMX1Tn1hcipIsTKYCMh4IhftIw7CjPBOQ8tImY9SdaQwSwAF_yJDfjaLjdqI0lWFXVDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZsHZllNfoWAOjDvgXXtd1P0SLyfcq9D81AleG15C8-OCwF_3qopRCPl2yO2Dkjb0XKle096BdCVQcvOBytGsHhHdVKPAwAPN7i_fjdKBdqfUIFqxgH_2qbTjIwePN7kJqrqrb56XiYrGkwmOsiRwAy09OUrICP0ogCEiClOd60Nr8c5W2jONK_dl9iQzfgrZHMwfiJLL8Py_gpNjVP_tw7QkWb0_VaYdZR6M8scMMWFBJqKoC-rVMP9hcJzJ5Sr9zfx4eD0qikiOlbtD9vs85Bsre029_eg6evYdmgYaotUHI4jKdkK16V8kFPXXyE26TAe8zvyjXEIqMywCrHG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=DYvbh7r2xrHX3j7BtVdVfKBDZ7F865XjaJs7HzQqm5hdbUfQy84pYROwv8eQHdDUih7h0Cu-PoqS-JAvGoDundJO2gOdj_N7JAmuIf8edduKyRLZFSu5Yb4tdptY3uKs6LhTOwUFk0m-ZFFkFKKgA0Zd5taRcJPbbZ4mO1pSwYzO28lGmwjIJGyCg_v49m41IKSy9bVi9BXAU-c0jXWivXSAqBTSHB1--EkssrwknoUei9OnhB0kXp5gysTAUAK8eNDe99KQtvCRAcIC_fytip5WowyQ-0JFRWxY7GaPZWWJZyHiffUIc5Xs9awdn79LdfTKmRZ11HuxJALg9TwPmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=DYvbh7r2xrHX3j7BtVdVfKBDZ7F865XjaJs7HzQqm5hdbUfQy84pYROwv8eQHdDUih7h0Cu-PoqS-JAvGoDundJO2gOdj_N7JAmuIf8edduKyRLZFSu5Yb4tdptY3uKs6LhTOwUFk0m-ZFFkFKKgA0Zd5taRcJPbbZ4mO1pSwYzO28lGmwjIJGyCg_v49m41IKSy9bVi9BXAU-c0jXWivXSAqBTSHB1--EkssrwknoUei9OnhB0kXp5gysTAUAK8eNDe99KQtvCRAcIC_fytip5WowyQ-0JFRWxY7GaPZWWJZyHiffUIc5Xs9awdn79LdfTKmRZ11HuxJALg9TwPmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpRyvBF3s9MmdgotAXz-kH6U3FSJblsWLMxgQJoH1l5oi9tF4bh3wg7B2BsdCUDINmEnoA0ghwWB0XNPFNXdcEf-TGsggmlBmY_3JGG8EWhXAHURIWNqu8uoyBZbhg1OpNbTIzS5Uu8pBLIY5POUfBlXlziZAV6yGYUHIFYL5Xhe8MEOCSjMkhwq_KrAoEQe7TCYnxM3xowSfyxHH89hBiBoORqYvGEECx00DlcSoz5ljsXDHxY568IOXvBDmp7_wL7y2EGLTUHPpVRmsvlNzBgYFPWVpBrgiWkYmRjjtXBmq6CheKky478PJP6VikGnD77aVi5TJCz2EzY-qE-iFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=NWRWMo-VHEw-j6s_ebBZXMej9zS7t2Av1IyeK0ChVMJ1NAy5sCP9gXkW7sQEDz1zGI1j5dPRMoZh7lik8Ag1ZhLDL1jFbLM8LNYv4czZqUedBvkn3-_4deP90QLsUCB7SEqL46_AybWcItTWh1UHm1vKxPTnNWTKN13fVPwoLzFhogCYeeFHv0vo-zvEHZaT7pZ2eTV-jg9xZy7PQZ1PIbkxMyFbOAtPl-2teE2QiB-0bNPy6x-cOfiNiwGZJJiqINGSMJVi_1qT8-bispemofRQnvs3Az-bQ9DT5vYmWPsfFGW24PmgNwkM2_QTemPpf4pdRxcgGss7LIXOmoCrUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=NWRWMo-VHEw-j6s_ebBZXMej9zS7t2Av1IyeK0ChVMJ1NAy5sCP9gXkW7sQEDz1zGI1j5dPRMoZh7lik8Ag1ZhLDL1jFbLM8LNYv4czZqUedBvkn3-_4deP90QLsUCB7SEqL46_AybWcItTWh1UHm1vKxPTnNWTKN13fVPwoLzFhogCYeeFHv0vo-zvEHZaT7pZ2eTV-jg9xZy7PQZ1PIbkxMyFbOAtPl-2teE2QiB-0bNPy6x-cOfiNiwGZJJiqINGSMJVi_1qT8-bispemofRQnvs3Az-bQ9DT5vYmWPsfFGW24PmgNwkM2_QTemPpf4pdRxcgGss7LIXOmoCrUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZICK44QU6q6o7WZImntmV1qaFDSZLwdkLbQTEK0XaUStqlYwv7c_6ll7oTduK_4cTneM2KmAo-o_MZkk4cpgMbclS0kssncGBS-f2Re64gdawPUATmVd5xi1mahSFBchSgnNmwqfr86cJUaB0K4gQmmSOB7GCKrPeOfzHqevuG37BeVDL6866-O5SAmLnxg_urjwmpoL8O-xNiq5YRlnSDQsO9L5qPAFc_tJC6gfc1AM7joM8jBMJLYBRuMA742fe1FLE1zKMBP_hwON3FC0ZVDgDBvmhMqL0Ml-iERYm9wXjqQ18LhH1Oe1lUCdCLrJhxQgkO84MnD3CQUYCAigLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=Nt5MhIQl1_rLh3VNbNqoVCbstUMoIAWZhgRodnSqmc80KcoMj_-_USbuekk25tmlTp32oLpO3MK381dqCkd0wBEwii8IiKRgTB56RrmN7aLwmbWDUVZWrD5C1B9Cm0X-Kr9nYallab2HzUUFArA_CusHPjHz2xrxX7YXVtZ-roRgVFTr6tGTylnkZxYT8h1J7UlVEtHZJlB6TxWhcW_Z34bDz6ruQKWhpdlFm_A03xEuQlLeZ9g1GZbEcfK-oOeqng44PZcLwPEImPLJ7iB79JzBKhiMkdS9gdpIKzsDvrTuVWGqDq_9ERNhsPICnFvUT0FL4bIsjn1OL2KiZ3woQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=Nt5MhIQl1_rLh3VNbNqoVCbstUMoIAWZhgRodnSqmc80KcoMj_-_USbuekk25tmlTp32oLpO3MK381dqCkd0wBEwii8IiKRgTB56RrmN7aLwmbWDUVZWrD5C1B9Cm0X-Kr9nYallab2HzUUFArA_CusHPjHz2xrxX7YXVtZ-roRgVFTr6tGTylnkZxYT8h1J7UlVEtHZJlB6TxWhcW_Z34bDz6ruQKWhpdlFm_A03xEuQlLeZ9g1GZbEcfK-oOeqng44PZcLwPEImPLJ7iB79JzBKhiMkdS9gdpIKzsDvrTuVWGqDq_9ERNhsPICnFvUT0FL4bIsjn1OL2KiZ3woQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=ntjrj0df2_JbV5cya7lEkGQsjhJaslFTco8_PBQolZpN8k4Uo_yQjDvEAi0ykatjppcPnVuuBCSZN1a_Yjhlx66ALwwtjD-n6stg2gPn8FrV7yMYlxs4IGid2vslzzcvDm8vWhJlL3k-vlm6VwJeB2waiahdr2xwcZhWioeGluEzpjMaKDzXTbI-5WbK9AoJFCKDLnetFbA6a5ALO25p1INFJyK1IFPMfhkFo3bHi9RuegYxkaN5NqGR7sjtW6zXITN1GJXc2Z63TKJjVYvESSWUtYwhnGUp3_f4cw2Pbm6M2Z9D83yzhfE7ahLJM7IoaaypHFuQYpl09bMghOkoRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=ntjrj0df2_JbV5cya7lEkGQsjhJaslFTco8_PBQolZpN8k4Uo_yQjDvEAi0ykatjppcPnVuuBCSZN1a_Yjhlx66ALwwtjD-n6stg2gPn8FrV7yMYlxs4IGid2vslzzcvDm8vWhJlL3k-vlm6VwJeB2waiahdr2xwcZhWioeGluEzpjMaKDzXTbI-5WbK9AoJFCKDLnetFbA6a5ALO25p1INFJyK1IFPMfhkFo3bHi9RuegYxkaN5NqGR7sjtW6zXITN1GJXc2Z63TKJjVYvESSWUtYwhnGUp3_f4cw2Pbm6M2Z9D83yzhfE7ahLJM7IoaaypHFuQYpl09bMghOkoRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghLuG4Tk-wUZwFZdDMwDZcGGR9GhtyTCNJGAcNEwS94ZJd96_QFeTcTicQpcckW43ZSQQobVoxJ9TEe3592_K1Y62EVK3LDsF7xTM0d-Uup1DyI7U50v62yP6bSvslMY573WpDHPlnnjMvpAknRq6yWZQfcGyCI8PW83nAwtGuggdZwz36QS0olPYPqEWlkyzjdl-ZHgz6587laemzXztZAWZHqpD8FOmPMB7HIeRMDDfy8o_Xpsm6aPlRg8l77mMxdcaDzZ2anF_m_4qkp3ZZk24mp6hQFVb9nvk-HurUyiUnPZrA3NXN86sbcMe_236wE_xZLUhIA5gYw5TetTeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3qa8-G3IjtQOK1yufqLJjLR0Y7aSbrJzxFwOKIXcjYQ0cYN6qH438roIwOwc2kjpctmb5d_a0Ctv8RxLeCAl1EQ9p2xkBJv4tK8ggplIailQ9hhkiKPKMVNCNvrHqZeWICVpMlPY3n1nvR075arPcUIqslIwHYkmrvPzt1X8zM-M2fVjTaPLwSl9S7rSj4itlkk6fd6diypjZo-JkaTMBhVtdAIGfwK3dwjF0x4KjCAzTy1JUmGCVAyqqD6E5xP8OaJ7dVAjI2sgplXez9XrPNBpH3wiLQRms7hUTn7ybhaUV66DVvYxAQ9tuVzHzXTAREkknnmhKDnax4WgtzaAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p87OyqNb-6qSzn_0z4lIRtHrZ7qk1jCKc_-LfZDqIi_xN-STPRttAArD0LPoHTAlbfhroEzYjAy66B5tj-MzMxAN5d7qCxACcEYJcmc9Y03KWk3yEauElJbGAfL_mmOytiPPZE_O8mEac3TQgOjXcki55Fiy01w5Um_L4O8BJmie1IFaD0ioEEpg9DQuUW0DQyDG4qO-tZ4i-7DnTTmeW29t8vx9r1rGh_qdB7vqFDZvzL7VYeNbQgD5_crdHFWUIbiExg_Y5jyh2Jwmfczo5Q8URofieTd4PBsYrVgRHsDaHmzLHhRe-Y4SF6MZz9Q4tI1R-Rto3TTwr5nP2g7ziQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
