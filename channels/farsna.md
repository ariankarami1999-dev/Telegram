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
<img src="https://cdn4.telesco.pe/file/pT8HOGHVuCVSfA5O-723fw6kpoBl_zlCm30uJ__4aq07XKyHAZh9SjpYLjFjtll4F4LTJfiBn22HgYke_GzCNqRdkDDdDTrgLwcJcwxx929aTM4veEqnFxDTxcQYPpLE0N5gpIM3qBoJqG1z-74Etd00uR1zth_QbD8SuneDCjTurAQIk20U8P4S2YL2BwBlXnT3vRBc3VBIGA4eZElLGtHeWdJOkOEexcTwTgomf2t-WuPB7lL50YsooApRwHmMuxL0fsO86Of-MUTdzud54dz6sDRNP84C22rqSXD86h_qRvfOcNsoE8kaBHXhnVlzGaoL5ReJ01G2m1Z8kCrX0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 02:20:11</div>
<hr>

<div class="tg-post" id="msg-438898">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eljM55BYV6uM7OtHECL_eFa6hWyH5lix74jVC9mV-Pv6dUESOdNlEDtEhtKpxuUrd-uCVrQrRudyZWsXs9bp4v_QMcSuHelsNtGAoYvvViZJPLT3Xb3xbsmUDLqRPaNIYLNe0OxCcwqFn0LbZBqYdCWWtspYh5GWvT52yQ3PIsq4h4__jEXzlTpH_zf5VqfofEl3Vim3K54xFgEkNU48D47-0vyxuEVtGVluzz5EFtOcbvanFGP033DVGMAEcmzFYTzmi2TH-u0WPq1LbGWhkoDB2hxpjRzLJdzB_Oyb0xaYPvqXYpJbdXC_rUgNk4-Nj50YYxBj6uqSc9L3yr8JrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی شدید رژیم‌صهیونیستی در جنوب لبنان
🔹
جنگنده‌های صهیونیستی بامداد امروز چندین منطقه در جنوب لبنان را هدف حملات شدید هوایی قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/farsna/438898" target="_blank">📅 02:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438897">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
«۲۷ رجب»، سریع‌ترین شناور هجومی ایران
🔹
جدیدترین شناور هجومی ایران با نام «۲۷ رجب»، با دستیابی به سرعت خیره‌کنندۀ ۱۰۰ نات و قابلیت پرتاب موشک‌های کروز بردبلند، به عنوان نماد جدید قدرت دریایی ایران شب گذشته در میدان انقلاب رونمایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/farsna/438897" target="_blank">📅 01:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438896">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">نایب‌قهرمانی دختر تنیسور ایرانی در تور جهانی
🔹
در رقابت‌های ۱۵ هزاردلاری تور جهانی تنیس «مشکات‌الزهرا صفی» به‌همراه هم تیمی خود از ایتالیا برابر تیمی از قزاقستان و ازبکستان ۷ بر ۵ و ۶ بر ۲ نتیجه را واگذار کرد تا در نهایت با کسب عنوان نایب‌قهرمانی این مسابقات را به پایان ببرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/438896" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438895">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌ سخنگوی شهرداری تهران: در واحدهایی که نیاز به «تخریب و نوسازی» دارند حدود ۴۰ درصد پیشرفت حاصل شده است.
🔹
اینجا، پیشرفت به‌معنای انعقاد تفاهم‌نامه میان مالکان و پیمانکار، صدور پروانۀ ساختمانی و قرار داشتن بخشی از پرونده‌ها در مرحلۀ تأیید نقشه است.
🔹
۶۰ درصد…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/438895" target="_blank">📅 01:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438889">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sc36kGRsbOBZhC8o6LgBA2Rlb5PuJBaQxUYPmADedXHSdySzKSy7zaKFcW0iXq8FhUtUh5t-J9wQ-zKsq7VHtQDjkBctDqXHFn-MAVnaxf9wtaef0J9UfEpi-R3tE3ef3WIB0HJbHjzxsBan4l6Em6cu4EK-FsAqz7foLnPkdFDZxt1C3oTbS-hJMyH1L53kTwGC2h2TfgnsYR_-OYgcwPBIVjOrkk7GeYTYwqASICNaTIm45k3Nca34axiWe3TgZdB3GPr7029fFt0Oah_yxVFO7ljAzAVcGpCw0FMH-fr_Opk4gM7cspKx7Hi3WX3-aV5Xe2TNVLEIzk0Ldjy83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1AHOhJC17q4Dk1yNV7SCcNo6Eokd2hRPoVY6OjWCCsVxBqvPwu6KD6KySlFEcKesUFcKJJBibkE-AkIY55V97BfwJbZI2WVCIugahrrZnrkbA9ihxQSvAFdACEwPbXgI4J8HYJO9XXmPc2IYfrCfv3UDEb2EzrukNaqcV6AuGXqpT74IHAS_vIRR45Wu-e3JsqGmj1Zu9U_MkDazfpxIbFnbDMpe7Crh8vLgzcz8bj7DS6Eo-VCYZiOgxDeYDtLPmuJRNkl4u_UvOfpXxI8V_6H6EFD7o3RsSyyK5M2vVJ3iHvcGiBCV4T363vAxqxt3449P4IoIbBgAddDWpftrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC9gQUr3KZV0p3YcHdd8RDRtVZrnTLH9_KJFwVL_8yfWVAsTBqd8RgXGKtoihc51y8xYGiTEOy25zDosCpBrlY8ZCBaBwUV74H_H5NXR7Yl9yLIZclavyXq4_B9jVKxKgRK2uhSqEgNekHt5zoOAPZ_g8hnA4ziYpXlo3YxsGPwADisTndEhmMNNRrygkNnFUQ3qjcKoB0C7-ZChb_1m0U9c2AfcwZeHzybTl53V24WhCuAOg1q1bxdl_SQRUuJ1eiFK8_Ts0GwuAna8s5YflqNc4lOFew4J1XP1zHDX7YComGB5S6Gp5WMkEaTpwkzBMF3V9t2blpviOsSznYCd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kzq1jqoc2VGHxLT71xxFBOA5bR43uUuF5sGrhqEyB9xdlDNrPspdUnkA8CjVlERXdRSJbPC7i_IgU3j8WW-rzktFrfMlIe-I0QDGqeZWz4Zqy5DVp7KADHUtvp8Kfkj2cQ-zh4IkBQWiwwe2urYqQYpxLHHTJLZXge_jFx1W7EYQMplpKYI-qN3-kxIep1QiEdEtruvIRQM69RFk3T0YLDs6y2TQ4B4j9VdBURGEV4KQzdl7iDUVffoPjI-bCVPvduGOSgG_K50jkhdIO5Qd7-l3xW7LFjw6CQB9gMtf4yRLQRVOjoyAjr2MPEGszvSHNNIV8QOQ257xsyTvn5pnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZsOAiUNdzevVz3XVTMRz3--N9x1AVB3_46eZFm-DWsqVRan4cC1RTzt5ICcilLupgXXkybyDBrUu1QYujMQu9MI0wNUC5uk1BvCOQjj7dwbKkFi8B_ogFihHiub8kViHuBhGv_WAs9cjU2AlgbHJPPrqpmduSiGSMH9Kr3ZnEJBvFerUkuvcWBuQzLZTftg3_VOHCtPXtTnispwgRsSBfFAc4iL6fQlH0n2SOwKJSBdPtm-QXrYPYr2HnvhhgoVWLC7KHFeroBB8DW8mex7H-Ocpat5uD3p6QRAbsFqx2B8DTWAvNlVM6ZScQ5E11OBnPgJ78Z2EHXvKvKgDwqW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nx1LMrIltIE5qggcc37-3tKXBddxPjS3LXERopCKE-vloX_IScOb0Jk5iYqX89-Rk7NRpigar64Sqd9ZHQk6zvos0eQ6K-HLYmo2YzGaLiiVykf3IUYd2ebylbGKBj6w3lxB_qpQr4YxRCFL6Z2sDIzYDwyQ9hbz6TNzgWzdvY0CDZ_ffJ6s0thglCAW7CTIVMSk7GIxUYf8oxuIgzT6llk5BQ_4GbzGoDDVZ3Fj7Q0rShG89e7d5FetZZ054WzubiCtyLP959Ks7gWLa4EdNHZpZKIbf-_HMKZSzpr9MTclj2RmsZWYcqYGC11LTrUCsfpGEALpHUmS9hbzIaKhjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۱۰ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/438889" target="_blank">📅 01:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438879">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VD5GnkD-tJNmhhRG7zo0CmGkwyv_-1E_FmsUKv7luCWrUJiNtrJ5kP5g52VMcZSuoSNHpZF2fm81qe6dhSTjeRMn0wKTvKWl9ZXbn1V-77FCTgw5ziszL0nrhMMsV9JIGKhI_b9oW0VQzMowBKbE0CZuU5_QkjTv4HUCtL-ey4gyIVN1BjbtZE-chDXtSTUa0NjMTouFS65F_KyXTO68yfQxI-rdtETPwCI8JxfEt2Fq18qTZQNdslvTV_EGTpetSC_mlrzgA3YUEoN97hiXV-XiwsZONeZG9CDixbLosUFZ_PZWe_Erul9QaTfHjAguMGFrnvr4YdadMFOiDs6FjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooRjh44RMmC0WPW8hU5My-7_Qlg3U2SA2e7pVCxx60HeDWR8ORY0pjFSaqHiCID1PjH4dE3m0ZpnskMfVye2TErR5wzAir1nBva5TbL1BShbXLOQtQdb3A-hyM3b_NjnGVC50Y6yUTg5-CkeSLQpszYnqQQsZQEf2ZEL7bpAZvq6cf418vn_nyUHOEReLlbVmBaG4FZXgSs6nsL1iG6dH_90oumWN-TKnQoQ9p8qWkoQEFH64t3VQ555Pn5PdG14nLD5shst8HL2j7kWhRh8OmAU5JsUeDxVbdXRyAq53P_yDoejo4TqxRkL0yW868nTb_EdS155OeKhyndkzWJKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUBnNTBkC0mB2GuYikxerWE8R8Nu2QI1QxWOMp9EvU2hh0wlrRpPAPVlf5-S0BZto6FAj9jnZICZK0U0SeWSBYI7qJs1733ivICFXWIT6VALCIKdAnvMiuxDbzgvhoL0VzNP2LgZEMtlmgzAhBohO1Lr9e8LouyJfYqIwuLuAjQDyiBwyNZjJuK3GF1xFGoGHh4s5ytvEBU5gvx-mW5W7OiSDsuZjRigAkVLH-i029D9RjP4_60F8OHUxeTJCIk_eYMMlIO5SnoSSV5ah8i1XKaEAhzYojtMWZlG7LUoZc39mOCTQv3vTm906Fz0-2dHML74h4krV4AcceYbDsZ2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yptl5PkI7vcQjrQlXOBaQwGa_YGOIrzq4mt7uSoOKq-KAu3qIopwOTvW6_ysyFYH3gm87c0cW8RnIoOZnzHKImGF5l_jWNw69yVVDzBFvsFwqSfaRYudFWc3Q0oTohxoFPl2KZd8eNi3tz2luIplDZITJZplnMKMCbzr0-TxO6p6eye6PdYGOYmZBLFfXx9g5uRdde1lLtZQLDLA7Ag1Cc4RrpMGQZK5KJBBIGejX4goUnhmqx0RyoHcgLFrn2hZhfMoYxq2CPmW_1B32KuO8KLd72uZjh_Av25GIKNzllANYk5g3SOTPGX6YbDwm1XWZqMxug4fVg6VjKPvRoscPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWGSzspdHv7XrseDRKdhmlZelg2b_-RfDd4aAL0wkLIurKqf8raH54nuQzP74FqddzJIVi_hIxFjaI3l37UvtyxMh4HTkV_VIs4XnCrGDfC3ttQ-ufDPrcs0PsTsCTznWMO0msl-W2XaXzVx_oHxU3DR5vzmbkz-AJ6_VpAXrTJo5YzHY1k-0KA2uC8sNCJmceJ-ea3PGvY4epmP8eUgjUpUaeX1ACd1VcynskSUgARHNE9Sl-Mgdl0fae73MuM_XUhHk5fGh74MK9XXr-Z_nvahN1sjBzwQaq2fqHIv7i5GG43xwbh3Osj-1aEP0rbkbFydeJZqJaionGwNaToSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPMhElt_SXwTf0EAs5auYojI0KwhBb7LwYKyO2wAA-fl63pU-zeQoBBUH8-m61DQnxL3rnLOPLS2GSZpVvWJWrwmTqqWLJyGEb2UwIY-ftixrOgd_nUGSj-M80LnIahwXTMeA5Zj0whxvivdHL_0BYTbg47Pqj-bh87Mi1kws1fQKLxXK9xX0649oPqR4Qm8muRw3TmG1I2aIJiqrbK3IJTFRgGxJbAJkihI7bWQy7dc9ednTQhqjLTqR5ZLqSmBGPL8DbZibfeiNzx40hdBM-_CRjDk6PK3SZyzhM2PCrTyiSkiS923dic7ka0TF7-ByA2iHYfTxklgVsbDlBNHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3VuY_ckd-087S44IXgzQWyeBSMAO443nH3NJun4V3LTQgL2O9WfWZd08qbzBsk4AGXLEHRuvGLsbjV98u7q0Cwrj1q5J9w6fodiNLxMxSydH_DWL_W_egh86qyXpc8hMCsSJG2e8-DH47qbhuCD2zv7wEyLPMQuC8ozz2rFuwLO-JgIvApuEhlFuGmbW4fTttvWK7VI-k3zAFa9NVcYy21QJWJV4zdQJA1yRQ8GObpV9chuyFKU8DEb59kffXNeKHYCs0PLlRZxg7-emI5uufCQx5JXoAAmrOE1z5LufsfD4YMcf9JD0oJNS6rLXadc5sNDvy70MQREcyF_ZEDUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghqXa6PVfzwjhJMxk24Ws8JrV8jPpGp1UH6VZCQJbHiZMjAzKWfyg9vJw-ZlOneZH3AiNNvut2Qplltkezb_RjSlY53K8mguMwwnSzFZOLs4WpzLdEb0_f8jCDCQc95ptcStcsWD4f3FXEQsJrPGLrA2SuRv9-0kXwnsAoZlQ6rso57yRNgjQ5cMfr_pZgRl7sPrOm7aIVpSXxgTMX9tGUhzi4KX30v9EI6KDKYsC1IQmX_baMXzXO1i8Uu_rLIxi1-ee5yBRGyYSpPMQV3k1_7sZMZ60ePyPimnRQqMVOXJBwaHf-d0WGzjelMzdyN7x7-758FuWU-oJC2L4Rn5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LU7XwWgaW3TuEB20Yf5x5TS__imgDBtpWpY_HpEccbmwGaLXJZxz4PSiejEA31AV1fLIv0vbT8LHz1eyRFKWBn2BMaG0RFN4-Arr4zzdFJnq6j17SCqqGBa4GtNpi2EG72oMvwJ19VGbS2Kf-uCapcLATL2HlwxjEpYwUt_GiwlPo8ZeSsdaP1-qhRTfJ4f8TnTW40vbUFPe8jSbK9GuMYUZewr9Wt5lORjN3-NCNZQGUcQJ0zrR9DufDrU5m-TQ8jYeey7-auky_eJilfsYOamdEI14BnnZdbT5DaKLE6e3q1jGFBJY2kSM2db5eezHf3HoshjSXKDQn6_NmEVoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKQ1m8ADHGDywaOQW0RAUuLPH0Ahr6RELQQTFjj2XwnH2zlWZ8sN4CNm9NycWPXZiNPb2Y_Od2qxTV_QQvmQrfN_62qIVYEUUrJAaC7cnMs87PCHzAe4s7sY16ZnmFQtTOF0qk9N1-Z5qyVzQElIfvQoZKt1iPrvxJ67DOqLdoOJore0wWazAywQadOSnULAeE4lNsLWNLBgTRQ_hvU-7RoCqEP_zq1RHm5Bd-akgpcCIE6IgNcbMEq3wer2AzgWjkuxQTzSxP4pcmOs648_iyGW6D9Z8IJ0qM2LNqHcvLSPW0pljILreM0wvOa11MSPRp5PmYa4TH2Q-Fgm6PsqTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/438879" target="_blank">📅 01:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438878">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هلاکت و زخمی‌شدن ۶ صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری از هلاکت یک نظامی و زخمی شدن ۵ نظامی دیگر در دو حملۀ حزب‌الله در جنوب لبنان خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/438878" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438877">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هلاکت و زخمی‌شدن ۶ صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری از هلاکت یک نظامی و زخمی شدن ۵ نظامی دیگر در دو حملۀ حزب‌الله در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/438877" target="_blank">📅 00:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438876">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی شهرداری تهران: پروندۀ بازسازی خانه‌های آسیب‌دیده تا تیرماه بسته می‌شود
🔹
در بازسازی واحدهایی که نیازمند تعمیرات جزئی بوده‌اند ۹۷ درصد پیشرفت حاصل شده، و احتمالاً تا پایان همین هفته پروندۀ آن بسته می‌شود.
🔹
در واحدهایی که نیازمند «تعمیرات متوسط» هستند،…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/438876" target="_blank">📅 00:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438875">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a02a1117bb.mp4?token=P8Z7LpK6M9xoonJDOglh1VTV2NprpEiE5WoWLIbIDzSCBLcI2QmGsPyqRztldr-Es7TcfJJh_Rp3Qx-PGRs1mk51F20hRjZrSDt070nRCflRty-0-iqUmmZ5Xr3Lyn-0GGYDH1k-0kvlsxsWeBrpsOtzBCeW578ON-0Nm7BxeypupTLVLcU95hhFybcNCvwUpxi4KniWwabuZJGoyvkUYc6Ow3wg3eXjwIz138qNOEDQb3ZhccYiEUzKKNhiT_WU3GutF_YMvmlDrBfGWx0_EmGqAvUXDUX2DmFyNwqcACZCMVSklrj-LoRD-zSXfaBCcgP3-tR0i0PhEwk-6ZiJ91ZkW_ik-xFHYOTkCDYWopgTwzuTj8f9HTixLKC72lWk8fiZRkI9YPO_9vB8Gl3ibNoZaKikGPK9whlAfwt1vosfnksuI0NQ91XTCaWX6-f1Smy8kVWUKt1wI1FK0iKRwyYSUdPEv7D6dOqEnkOiUQJUN0mKMdkXbKQLXQa__AK8_3Y_-UZyxRpkydAETgATN26v5z5tJ2rk0MKrZlFC_rzhry3XK1JPj0XqT4PgZ6eccKFTbqNyO1ArpI5L3KyQh9wPWdGNYI5lfxWzkxyYEHYVU7qE4l6WG3bILuMfoKGA8PDpT6FO2NFyE5pgOtH5WvVHhzDxBwdnP8sjsw7_1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a02a1117bb.mp4?token=P8Z7LpK6M9xoonJDOglh1VTV2NprpEiE5WoWLIbIDzSCBLcI2QmGsPyqRztldr-Es7TcfJJh_Rp3Qx-PGRs1mk51F20hRjZrSDt070nRCflRty-0-iqUmmZ5Xr3Lyn-0GGYDH1k-0kvlsxsWeBrpsOtzBCeW578ON-0Nm7BxeypupTLVLcU95hhFybcNCvwUpxi4KniWwabuZJGoyvkUYc6Ow3wg3eXjwIz138qNOEDQb3ZhccYiEUzKKNhiT_WU3GutF_YMvmlDrBfGWx0_EmGqAvUXDUX2DmFyNwqcACZCMVSklrj-LoRD-zSXfaBCcgP3-tR0i0PhEwk-6ZiJ91ZkW_ik-xFHYOTkCDYWopgTwzuTj8f9HTixLKC72lWk8fiZRkI9YPO_9vB8Gl3ibNoZaKikGPK9whlAfwt1vosfnksuI0NQ91XTCaWX6-f1Smy8kVWUKt1wI1FK0iKRwyYSUdPEv7D6dOqEnkOiUQJUN0mKMdkXbKQLXQa__AK8_3Y_-UZyxRpkydAETgATN26v5z5tJ2rk0MKrZlFC_rzhry3XK1JPj0XqT4PgZ6eccKFTbqNyO1ArpI5L3KyQh9wPWdGNYI5lfxWzkxyYEHYVU7qE4l6WG3bILuMfoKGA8PDpT6FO2NFyE5pgOtH5WvVHhzDxBwdnP8sjsw7_1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای میدان انقلاب در شب نهم خرداد
🔸
از ٩ اسفند تا ٩ خرداد
🔸
ايستاده‌ايم با خروش‌وفرياد
🔹
رهبر اگر فرمان دهد تحت‌فرمانيم
🔹
شش ماه ديگر در همين ميدان می‌مانيم
@Farsna</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/438875" target="_blank">📅 00:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438874">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درگیری شدید و کمین رزمندگان حزب‌الله علیه ارتش رژیم‌صهیونیستی
🔹
منابع لبنانی از تلاش ارتش اشغالگر برای ورود به شهرک «دبین» و مقاومت رزمندگان مقاومت خبر می‌دهند.
🔹
درگیری شدیدی در این محور گزارش شده و نیروهای حزب‌الله چندین کمین علیه ارتش اشغالگر انجام داده‌اند.
🔸
طی درگیری‌های امشب، یک تانک مرکاوا هدف اصابت پرتابۀ حزب‌الله قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/438874" target="_blank">📅 00:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438873">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD_15k7WWXu7TBIulVvfvb8vFXSn-BhgIwVLCv99M11z7JPccNE0Y7HTFAsTPUEL6RQthfQYrxYusdKtIovYY-P7NeXh2LMxwaMaPHsdbEuNXPECApGF848CHhDuVxTLY8nrsENxc399PysStR_U9i1sQ77z8dMGwlxbn1yEEOFfXt4Gt2Ko7Obxtos2f7JbSBbaLvUNeospvtOReKW1NKHNllQSW2KBLufnoAM80YeceJdiDepiSr4Pb8spczq4uBNnPnnbXxxLOE_vZAtE5Lduh-UW9Gya8QgSUF129IAzylordd0_FjKkWmt4PS7P_KZoi21hWZDXWjI30WKWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی شهرداری تهران: پروندۀ بازسازی خانه‌های آسیب‌دیده تا تیرماه بسته می‌شود
🔹
در بازسازی واحدهایی که نیازمند تعمیرات جزئی بوده‌اند ۹۷ درصد پیشرفت حاصل شده، و احتمالاً تا پایان همین هفته پروندۀ آن بسته می‌شود.
🔹
در واحدهایی که نیازمند «تعمیرات متوسط» هستند، یعنی آسیب به جداره‌های داخلی یا بخش‌هایی از منزل وارد شده اما اسکلت اصلی سازه سالم است، ۸۲ درصد پیشرفت ثبت شده و تا اواخر خردادماه به پایان میرسد.
🔹
امیدواریم کل پرونده بازسازی‌ها در شهر تهران، در تیرماه جمع‌بندی و تکمیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/438873" target="_blank">📅 00:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438872">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZCiggKijGcQFnn4aeZ3AgIxg20fVhDvLw_tY4pT8cxCQXtAPqOZQgvVMlQywbUcswA0-YlS-2ycUDMkuIaWRtD-p6QQ9WGupKwpKJOuJ5T6e0mZqVmc8fHtMjKnglyLUFVupu2-8GxZJ2RMTuihSEiIfEJ32ioiZjmEKgII7vw-y0-qYfeXUI4uJqOt_aP9-Y1KGgU9NFjJAhAe4YD0_ImjfQqkqtH4V-Y5TSHeq0zllRGDdhGKTR6a1-VSc_F6gVgIlsy5Rl0XyVG-3mCHnC9OEZRp3oUAuE-Wj3d6wyNiQCHtT1iK7eA6P5o3lWZixlUGz_jkldXYniLuJ1Du4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسب‌دوانی و افسار غنیمتی
🔹
در مسابقهٔ اسب‌دوانی، اسبِ مردی از همه جلو زد و اول شد. مردم یک‌صدا شروع به تشویق کردند و فریاد شادی سر دادند.
🔹
در این میان، مردی که در میان تماشاچیان ایستاده بود، ناگهان شروع کرد به بالا و پایین پریدن و بیش از صاحب اسب، داد و فریاد و خوشحالی می‌کرد.
🔹
صاحب اسب که از این همه شور و هیجان او تعجب کرده بود، جلو رفت و پرسید: «ای مرد، مگر این اسبِ برنده مال توست که این‌گونه شادی می‌کنی؟»
🔹
آن مرد گفت: «خیر، اسب مال من نیست؛ اما افسار آن مال من است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/438872" target="_blank">📅 00:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438871">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWZaNAiPVJxuC_ck69l5jBsM45QPQOMZzKiyeK3cbUBdm3_blpxxTlXYCm4nygaZprGzZ87k_tPBZnwzaDCaTrcgaTdAn9rwWR7fPoDbTQsskY7Im6nEERjEAamPD8eWWS2J6odrEzNGUfb0E-ar1fCgnI9pofXdnVWEUkvLzBuzjIclSIzZ2_xmlZEuxd4oxlHLlZpSsi51UMRwetEydw0ZLWIYgFKWeRxkTwYar3mIf7uJ2EVTo_1b3bG0Hn0ZLR3Dh3wBw5NwJBXh6t6nxO8xsDh85CKWZoMWAq8luSgGpxVWuYdOy4vzaGIHkPu4LN2jxivjiQhxxm8XaGLqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ چیزی که هیچ‌وقت نباید دور بیندازید!
🔹
مدیریت پسماند برای همهٔ کشورهای جهان بسیار پرهزینه است. علاوه بر اینکه پسماند زباله، مشکلات محیط زیستی را هم افزایش می‌دهد.
این ۷ وسیله از سطل زباله، فراری‌اند!
🔸
۱. فلزات مختلف
🔸
۲. لوازم الکترونیکی و الکتریکی
🔸
۳.انواع شیشه
🔸
۴. مواد پلاستیکی
🔸
۵. مواد چوبی
🔸
۶. انواع مواد کاغذی
🔸
۷. منسوجات و چرم
🔹
اغلب این لیست در خانه‌های ما پیدا می‌شود و ما بدون اینکه نیتی برای آسیب‌زدن به محیط خودمان داشته باشیم، همه اینها را در کیسه‌زباله راهی دفن گاه می‌کنیم
🔹
این‌بار بیایید بادقت بیشتری پسماند را جدا کنیم و باطری‌ها را به‌عنوان پسماند خطرناک، و باقی چیزها را در دستهٔ خودشان قرار دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/438871" target="_blank">📅 23:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438870">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📷
دیدار سخنگوی ارتش و سخنگوی وزارت خارجه  @Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/438870" target="_blank">📅 23:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438869">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1zANqRRXflK1vN4HFkDtY3Q4ntIV38N13OFXWMsvStPYoGGCNeEcG2RQtPefHkFP5GtOR0PwCw0rechfLV9JKcGO0DWdrcniAeqlUxGh6aXYWl5xMLnGOkETYVgbNnHol7PRLS04NEONXqxpEd0gQra7adVUJBxXqwrdCdYcgomd-6S5W5NdWkBDhZtEkpi3bdyqV_hiHbnMhLz59fp0LvCEB2S5Ic3eEBsLjokegHWmvh3FhtFAGcHqdBTQ_NjRBW75adOmMryCZZKEQY09J-t42LAo-PAuidoKaRrLXVG_EokYA3whs8Fy-_ZvT7kdE0V2ETCLvAmg5o8LG__Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار سخنگوی ارتش و سخنگوی وزارت خارجه
@Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/438869" target="_blank">📅 23:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438868">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
پشت همه این ماجراها موساد بود
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/438868" target="_blank">📅 23:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438867">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a04ca94d83.mp4?token=d5La8j9fa5KXpPno_gt38wNXhat9bQ_PAKI_2mSp9Hq21T3xk9jrzex6kMiSzfNAFWd17rmejMOoybTNlqiy4Dj52YptMfYVrY3p0TXfPJiuXqfF_mLZ5aQ9YeqvS5vObBSrUlrceVXiWtm0-yUFVAJcxxbhS6TRax0Slc31gZCXsNbK0yt2NaFNdkBzR-2AfZf47kGHtwa6SU5gKHdCjb4gWW1JH-463A4oq6LE33vOPw5H4FvkqrnJGea5s-285gz6KBRDksg2toMLPiRETGyY5HMtXY3887KHdyPqqz73RYuiUAy3zl-DG7ApecpIFZRCUKu3VpJ3Yevst25AsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a04ca94d83.mp4?token=d5La8j9fa5KXpPno_gt38wNXhat9bQ_PAKI_2mSp9Hq21T3xk9jrzex6kMiSzfNAFWd17rmejMOoybTNlqiy4Dj52YptMfYVrY3p0TXfPJiuXqfF_mLZ5aQ9YeqvS5vObBSrUlrceVXiWtm0-yUFVAJcxxbhS6TRax0Slc31gZCXsNbK0yt2NaFNdkBzR-2AfZf47kGHtwa6SU5gKHdCjb4gWW1JH-463A4oq6LE33vOPw5H4FvkqrnJGea5s-285gz6KBRDksg2toMLPiRETGyY5HMtXY3887KHdyPqqz73RYuiUAy3zl-DG7ApecpIFZRCUKu3VpJ3Yevst25AsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنالتی آرسنال سوخت؟
حیدر سلیمانی، کارشناس داوری خبرگزاری فارس:
💬
این صحنه کاملاً پنالتی بود چون مدافع پاری‌سن‌ژرمن دست مهاجم آرسنال را کشید و باعث سرنگونی او شد. به اصطلاح ما مدافع روی مهاجم آرسنال خراب شد و داور باید پنالتی اعلام می‌کرد اما انگار تیم داوری در تلاش است تا بازی را مدیریت کند و ‌بدون جنجال آن را به پایان برساند.
@Sportfars</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/438867" target="_blank">📅 23:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438866">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8817f3ad8.mp4?token=KC_LEGJboSxlGetSxu7GJX_muLBJ947kr2BkJB553m_A2nyAGQTR0-5JbrrMbJXFrkq-5GFuypZ9rqCnxwst4UlmhBTVWNVIosS2rUQNd4vOJZBpy8hIMyRzi0swI2iWOon-73-E8ZCtRljBVEVw3hDAshUAKpyd-bF1DI7XOLvT0x_DhTeXrqmiTCmsUYY5Yj6Ikh4G58AsQT0X3FmMrxClR68JkVWid0Unu3ea2lNxxh7UKXbgz-BqfpvnFRCpmuSyMeP6Mt0FEPU5-90q80n4ZNi8On661E3Ui7R8d1kG_yxZkggntwyPU4D_S90m3WatbVEaOdpn-n4ue3L5D5ealaWdA8hsGKs1ndiULEdM7bDjUd7jpkSKWx5HRE1BgjV_HiukOhD4bD9Vn_dldY0HA6aC9Cj7rnLU-ge1EllDou7ysD1mKyDepOls_JYiWIf-JoXhRvMr_tEqD0-F1SX2_zZQMHMnohwXBe_BYs0dEWXH7VIs1l5QjRVlYOpGcABAtJ6h5jOs_N1lsx3sHyo56MD41hWkE5ObdPEUXYVF8IUyJHY9vFq_nhrUYwi3FnzHnKxsL4vivmdxCpUVsX5L5XlY0h5QlrUSFY213LiXtjEq09ODQHBL3wHPwIRUlbBLA59up5Ax1vDddBmOXEdX1OVfxWu4vRXyNRI4qqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8817f3ad8.mp4?token=KC_LEGJboSxlGetSxu7GJX_muLBJ947kr2BkJB553m_A2nyAGQTR0-5JbrrMbJXFrkq-5GFuypZ9rqCnxwst4UlmhBTVWNVIosS2rUQNd4vOJZBpy8hIMyRzi0swI2iWOon-73-E8ZCtRljBVEVw3hDAshUAKpyd-bF1DI7XOLvT0x_DhTeXrqmiTCmsUYY5Yj6Ikh4G58AsQT0X3FmMrxClR68JkVWid0Unu3ea2lNxxh7UKXbgz-BqfpvnFRCpmuSyMeP6Mt0FEPU5-90q80n4ZNi8On661E3Ui7R8d1kG_yxZkggntwyPU4D_S90m3WatbVEaOdpn-n4ue3L5D5ealaWdA8hsGKs1ndiULEdM7bDjUd7jpkSKWx5HRE1BgjV_HiukOhD4bD9Vn_dldY0HA6aC9Cj7rnLU-ge1EllDou7ysD1mKyDepOls_JYiWIf-JoXhRvMr_tEqD0-F1SX2_zZQMHMnohwXBe_BYs0dEWXH7VIs1l5QjRVlYOpGcABAtJ6h5jOs_N1lsx3sHyo56MD41hWkE5ObdPEUXYVF8IUyJHY9vFq_nhrUYwi3FnzHnKxsL4vivmdxCpUVsX5L5XlY0h5QlrUSFY213LiXtjEq09ODQHBL3wHPwIRUlbBLA59up5Ax1vDddBmOXEdX1OVfxWu4vRXyNRI4qqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع مردم مشهد با شهید مدافع امنیت عیسی عباسی از کارکنان فرماندهی انتظامی شهرستان ایرانشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/438866" target="_blank">📅 23:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438864">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00b65b542.mp4?token=oP8AxmIaq4JWUQ79Fpbi65zKyoV-qqMi3-CViDvhMExXHFk1S5mdRY4g7avzZDolvNW5dhpCTlncWqYp_VzRX6a3EFP7RcmHD7ePdWt6EYCg_DV5V0Sa6hT0bL98yHPlow3jp1m-0nAdu4VowOZVXMIQ7Y43sRGpskXVmWFhodLMGf1dRQGbYp6KH3LI4v4rprsDb6NfumVdz6YPwv3_R_qD8s2MDV3LaOtzSma5W2R2UJnRWZJTLKxvGeazXgbzouR04P0t0WvdmuEor370f_vMTAC9XtXbpp4kB3w_XUuTeQfTheJIaGOclba5xb_nlBBmBlzdmB9jBnmCSiImnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00b65b542.mp4?token=oP8AxmIaq4JWUQ79Fpbi65zKyoV-qqMi3-CViDvhMExXHFk1S5mdRY4g7avzZDolvNW5dhpCTlncWqYp_VzRX6a3EFP7RcmHD7ePdWt6EYCg_DV5V0Sa6hT0bL98yHPlow3jp1m-0nAdu4VowOZVXMIQ7Y43sRGpskXVmWFhodLMGf1dRQGbYp6KH3LI4v4rprsDb6NfumVdz6YPwv3_R_qD8s2MDV3LaOtzSma5W2R2UJnRWZJTLKxvGeazXgbzouR04P0t0WvdmuEor370f_vMTAC9XtXbpp4kB3w_XUuTeQfTheJIaGOclba5xb_nlBBmBlzdmB9jBnmCSiImnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از شناور تندروی هجومی جدید سپاه در تجمع میدان انقلاب
🔹
این شناور مجهز به قابلیت پرتاب دو فروند موشک کروز دریاپایه با برد ۷۰۰ کیلومتر و قدرت مانور و عملیات در موج با ارتفاع ۳ متر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/438864" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438863">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50739c202.mp4?token=WTTZE_98sUVuL87l-jw8djpdPG_yHAmxmKoujAbC76jK7h98IQWyZv2LYH7LJsYIp7wyYM3ne1T2CgGjzxk_M1za40B6dudf7N_p2SgMDZr0462GiffQrft_y1bpMkLIxc5qXz6thyHgy3C7YDcxnN3gpRPjWpB-OUtOtou_CWJPLraMZsvSuAPrcY4mEotLGB1kHHZDMz849y3FooG8cC4qLupH5rTRkNhU5WQpU32oLJuwIkVhFlx-7Khh4e6WnD1oGZ6bfdr4lg0gXDwFgCqYH-F1C9ba9QBmixFgoqStmf4UC3ZrLEpm8tQfRAT8Sg_eINOp6xFsTsD94kr7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50739c202.mp4?token=WTTZE_98sUVuL87l-jw8djpdPG_yHAmxmKoujAbC76jK7h98IQWyZv2LYH7LJsYIp7wyYM3ne1T2CgGjzxk_M1za40B6dudf7N_p2SgMDZr0462GiffQrft_y1bpMkLIxc5qXz6thyHgy3C7YDcxnN3gpRPjWpB-OUtOtou_CWJPLraMZsvSuAPrcY4mEotLGB1kHHZDMz849y3FooG8cC4qLupH5rTRkNhU5WQpU32oLJuwIkVhFlx-7Khh4e6WnD1oGZ6bfdr4lg0gXDwFgCqYH-F1C9ba9QBmixFgoqStmf4UC3ZrLEpm8tQfRAT8Sg_eINOp6xFsTsD94kr7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌خوانی شعارهای ملی در یاسوج با لهجۀ شیرین لری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/438863" target="_blank">📅 23:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438862">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad67a09368.mp4?token=TRxWEV75Dx_gVsXF75MMmvVZNrlfMlep5uXkBZ3YTDCluYP5j9PwaM5lWwV0bQryOQXyzBNdw4kMnvrXs6HPdp1GUYF0Bw-IfAMV-zXC5doyLKuo-o9sPEOCrCpCoJMgwFf6L2J5w4ee2lSXZv9v7Df4rRq5h_eFXYz-rUj56Tt5BCE6rB_QpdaVGXbjNbmUlHj-qfs3qtf0Oa6OfhJODP9gghQZphvUhfCpE5f_ph8MtWlrC0VRCwB4ZAxsgM3SUYpsLTDkd0ltH4vfwbculU7ssQmLElGlMEdoqdzJ-vgr9GDR4bsTviw-HAaURPgn7TRix3a4iCVIQ_TM2LiSEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad67a09368.mp4?token=TRxWEV75Dx_gVsXF75MMmvVZNrlfMlep5uXkBZ3YTDCluYP5j9PwaM5lWwV0bQryOQXyzBNdw4kMnvrXs6HPdp1GUYF0Bw-IfAMV-zXC5doyLKuo-o9sPEOCrCpCoJMgwFf6L2J5w4ee2lSXZv9v7Df4rRq5h_eFXYz-rUj56Tt5BCE6rB_QpdaVGXbjNbmUlHj-qfs3qtf0Oa6OfhJODP9gghQZphvUhfCpE5f_ph8MtWlrC0VRCwB4ZAxsgM3SUYpsLTDkd0ltH4vfwbculU7ssQmLElGlMEdoqdzJ-vgr9GDR4bsTviw-HAaURPgn7TRix3a4iCVIQ_TM2LiSEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربات پنالتی که با تکرار قهرمانی پاریسی‌ها همراه شد  @Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/438862" target="_blank">📅 22:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438861">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e002a8710c.mp4?token=MpJp3BsFY96tVu8QP7Nlm1FCY6coreKSdby9apmW7k9hLEZOTKXsUc5nK39bV4WWVTAaW_Fmyr-LYRr3Gz8y-zKDPfqL41-7ooEJnaT3l9tp9hmohBm5gOPZV_RB3DCXvu8Bun19cLwhF5jaCU4VWDMiPzjrVmbtEiaSb4hBWh-LzBkZm4V4kfuQgntUJ11W2HxjVD9xLrvgbw0tRaJOC-kGD6QcnkCeF8N4uLJuO_JBf5UcQEHlkxrr21wDgOnZhLGi9PXjC8VYtAqxLYDymCt7zXr9BXtKspYvbct9BHPtwxc9VAuh5fw3LBwEiRrJoJcSQA-KiP7TpQyZvS1v0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e002a8710c.mp4?token=MpJp3BsFY96tVu8QP7Nlm1FCY6coreKSdby9apmW7k9hLEZOTKXsUc5nK39bV4WWVTAaW_Fmyr-LYRr3Gz8y-zKDPfqL41-7ooEJnaT3l9tp9hmohBm5gOPZV_RB3DCXvu8Bun19cLwhF5jaCU4VWDMiPzjrVmbtEiaSb4hBWh-LzBkZm4V4kfuQgntUJ11W2HxjVD9xLrvgbw0tRaJOC-kGD6QcnkCeF8N4uLJuO_JBf5UcQEHlkxrr21wDgOnZhLGi9PXjC8VYtAqxLYDymCt7zXr9BXtKspYvbct9BHPtwxc9VAuh5fw3LBwEiRrJoJcSQA-KiP7TpQyZvS1v0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوشش بیمه‌ای ۱۰۹۳ دارو که افزایش قیمت داشته‌اند، بیشتر شد
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/438861" target="_blank">📅 22:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438860">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1756c1018.mp4?token=E-eMNkd36UFFIXzOft3bcyYtldcYOlCfwCFEGfG7SjtTyLbibM4OCUZ-feks2ElOxUYDdizz31hwC5ywg88vi7EV58OOp7zOAY8Y-PLsVbb9yAhJ5grQnSrDrA18UOugEUXfunWiRsFZsJeLNR9W0zcnRMxphDqQJV4PyLCSRX2d1p3WFVm59x5NsGorGAXw1vqBkQTljYupVImZtrgGrFMVc-fL9jR-TwvJBLB3GR7SmPLNsuPyAfvXLiO6S4WvxMKOYvQM-_6YvJgELADAQuDmUxdPJGg42swvKf0QYZ1vDr-zieAG8nn1r-CGfFYVFXUeRR0KJyTFQMtt4uZiLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1756c1018.mp4?token=E-eMNkd36UFFIXzOft3bcyYtldcYOlCfwCFEGfG7SjtTyLbibM4OCUZ-feks2ElOxUYDdizz31hwC5ywg88vi7EV58OOp7zOAY8Y-PLsVbb9yAhJ5grQnSrDrA18UOugEUXfunWiRsFZsJeLNR9W0zcnRMxphDqQJV4PyLCSRX2d1p3WFVm59x5NsGorGAXw1vqBkQTljYupVImZtrgGrFMVc-fL9jR-TwvJBLB3GR7SmPLNsuPyAfvXLiO6S4WvxMKOYvQM-_6YvJgELADAQuDmUxdPJGg42swvKf0QYZ1vDr-zieAG8nn1r-CGfFYVFXUeRR0KJyTFQMtt4uZiLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری باشکوه مردم قائن خراسان‌جنوبی در حماسهٔ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/438860" target="_blank">📅 22:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438859">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پاری‌سن‌ژرمن دوباره بر بام اروپا ایستاد
⚽️
پاریسن‌ژرمن ۱(۴) - ۱(۳) آرسنال @Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/438859" target="_blank">📅 22:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438858">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6AKyHbRKYC5oGwFrrOhaMnSGHoFevyLpToINWvR2CdE21BjR7b5MR0CPpz5rsd-G8i3TAA9qQ3TupGJDPEXrRvyhyNf1667e8FiS7dNFN5fGnTfcXAI4OmpfAZJxvvRU-dh40B6A8vy2pUEPJnYurhPbB9_b316vx7ZKeFJEK_fCJbywmCd56q7km2iyPVy84eHipj8Nrr9bOp4RXxVmZH-ftv5IbVjeEm4wH3PK-nxYZKgLI9byIzd9c1qGftEE-Fvn0LhqNjhqCGPVlrB1HloLByalHdorFk4gt2hmoeJMz7fDkM2nmRZiOI7n575kTnulHAa7i9PYeAGCaNd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل تساوی پاری‌سن‌ژرمن به آرسنال توسط دمبله در دقیقه ۶۷
⚽️
آرسنال ۱ - ۱ پاری‌سن‌ژرمن @Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/438858" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438857">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8849fa944.mp4?token=QMGAVjuQM1aaIf3ZXR1P58N6L1TpD1k3jBxWVTHguadne-LgaAMu7HKyQzdaC8PNdJbzpz7KWd56ng6Us39tZALD3wItEcCqZmWqEj_ALMqgkmzSfGtbAT5e5cPSV6Nm0FPGbiFSHNFB2d37bGaATAc7UvCUGyd1C0A_6UYLhQ0anqjlvKt3f3EUdNeySGrXhhkRs0Ap7RLyFIsAEmmo3tYGUh3SRdORB8XbRhWOT2-uRUOxMHJNsUK_H6Dfnf5hPYH-uOu4XgPqtOe3soDCIU1pmORM7ikfe_vm3fSJSoeYYiC4NaLZ-1KnY9htvZGE2FK4ce1Ok1HU0E83dQ27nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8849fa944.mp4?token=QMGAVjuQM1aaIf3ZXR1P58N6L1TpD1k3jBxWVTHguadne-LgaAMu7HKyQzdaC8PNdJbzpz7KWd56ng6Us39tZALD3wItEcCqZmWqEj_ALMqgkmzSfGtbAT5e5cPSV6Nm0FPGbiFSHNFB2d37bGaATAc7UvCUGyd1C0A_6UYLhQ0anqjlvKt3f3EUdNeySGrXhhkRs0Ap7RLyFIsAEmmo3tYGUh3SRdORB8XbRhWOT2-uRUOxMHJNsUK_H6Dfnf5hPYH-uOu4XgPqtOe3soDCIU1pmORM7ikfe_vm3fSJSoeYYiC4NaLZ-1KnY9htvZGE2FK4ce1Ok1HU0E83dQ27nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلمی دیگر از شنیده شدن صدای انفجار در بوستون و رود آیلند آمریکا
🔹
منابع غیررسمی از احتمال برخورد شهاب سنگ به این منطقه خبر داده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/438857" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438856">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb9f4b3dc.mp4?token=NglPWuwWcF8hb4OVsyAdmTPKZvz4qEooW1Ou2qYKdyeazy_PqiFsvycX8FXmQ6ME3Bsue27Oy8ulGdJJcGdgDR9p0ITzyfrwWv3Fr080fx5QCWaGwlkw1zdLvKlVLOtQ259rC_qbsm9Ozqnh4IiGFXhsplC7noVBVqXDgX1Uhfb5NM_72wzFl5dfE4scDkdo1IGxZhZvMzfuTtFkTo49SOT9NvmOqjtPvWNTXHQH4lCg1B8rpeo3kDo9G24yhYJLeMZB_MOWqsu2R0k6PjarSn7elv5a7YqhiOLHzi6y8qWpR1_nKwKC-vO1tE5vWMrpINASBRey54stTS_3YD2wGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb9f4b3dc.mp4?token=NglPWuwWcF8hb4OVsyAdmTPKZvz4qEooW1Ou2qYKdyeazy_PqiFsvycX8FXmQ6ME3Bsue27Oy8ulGdJJcGdgDR9p0ITzyfrwWv3Fr080fx5QCWaGwlkw1zdLvKlVLOtQ259rC_qbsm9Ozqnh4IiGFXhsplC7noVBVqXDgX1Uhfb5NM_72wzFl5dfE4scDkdo1IGxZhZvMzfuTtFkTo49SOT9NvmOqjtPvWNTXHQH4lCg1B8rpeo3kDo9G24yhYJLeMZB_MOWqsu2R0k6PjarSn7elv5a7YqhiOLHzi6y8qWpR1_nKwKC-vO1tE5vWMrpINASBRey54stTS_3YD2wGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش‌ها از انفجار در بوستون آمریکا
🔹
رسانه‌ها از وقوع انفجاری در شهر بوستون واقع در ایالت ماساچوست آمریکا خبر می‌دهند. علت این حادثه همچنان نامشخص است.
@Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/438856" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438855">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb147db4c.mp4?token=kOSx93iIwXD8fpui7ntnwoX23HtotdeuRxF8hK1a9-tLD3Xivsb6lKeCWwb35JiTXlES8fAMCAJlWeku1jagpaMl1eKSEcImxejhzAOdZzxhx_g9Nt7FyXSoV_noNwb8cjxt8vL8SJ5x8RK011h5TOX9ormYEkqLurapMifeWKfArkEv9qUJ5C_fYqQ9PAtI0wfqorB7oc_lvaZcwwtpPMjcWOujzYp4O9FzFRltvMP__gwxGnOvGRuKjtB5veMqPeosHCIwP0kvuCvQhc6ozftQ1-ME3FthPzD-k4vvl6iuHCY95mtqj8pMLzGOqJ8PqyZkhrYkMK2et89mnfG8Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb147db4c.mp4?token=kOSx93iIwXD8fpui7ntnwoX23HtotdeuRxF8hK1a9-tLD3Xivsb6lKeCWwb35JiTXlES8fAMCAJlWeku1jagpaMl1eKSEcImxejhzAOdZzxhx_g9Nt7FyXSoV_noNwb8cjxt8vL8SJ5x8RK011h5TOX9ormYEkqLurapMifeWKfArkEv9qUJ5C_fYqQ9PAtI0wfqorB7oc_lvaZcwwtpPMjcWOujzYp4O9FzFRltvMP__gwxGnOvGRuKjtB5veMqPeosHCIwP0kvuCvQhc6ozftQ1-ME3FthPzD-k4vvl6iuHCY95mtqj8pMLzGOqJ8PqyZkhrYkMK2et89mnfG8Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت صمت تأمین نشدن قطعات سایپا توسط کروز را تایید کرد
🔹
مفتح، قائم‌مقام وزیر صمت: زنجیرۀ تامین قطعات وابسته به شرکت ایران‌خودرو، باید براساس قراردادی که با سایپا دارد قطعات این خودروسازی را تامین کند، اما این موضوع انجام نشده است.
🔹
از بهمن پارسال هزاران…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/438855" target="_blank">📅 22:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438854">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05cad0fa31.mp4?token=NSKXE5bm5qvuByA1FJ0WgYZ1w-lOgD9PpIbScktOIWvMrW8Dhf2RqpdZl64m1aC9L_fsBA4aHM6-zDjHvLysvHjU0aF2YLKbkWrzaquSgyElgjNYc8PSc-AVbbx0Ld5iHdmZWIDYZnwxErcM4YpObVGmLd1CnE1w3CW3AjSXUH-14KbygW99AOBluMava4FQ3H8FGVADRDgamYK6tcPWHwuT0VBsK80XVKsbqsYfTSM8FMXQca7LgZ0zSXsrTlyADoyoDXXEIiIxScjwAOsT0CcFNKLFVvbPQ8-n6Vrsx8v13-OM8Pbe5SPZ2PaoM_qZReXTBgqQEilljx4_ILlvNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05cad0fa31.mp4?token=NSKXE5bm5qvuByA1FJ0WgYZ1w-lOgD9PpIbScktOIWvMrW8Dhf2RqpdZl64m1aC9L_fsBA4aHM6-zDjHvLysvHjU0aF2YLKbkWrzaquSgyElgjNYc8PSc-AVbbx0Ld5iHdmZWIDYZnwxErcM4YpObVGmLd1CnE1w3CW3AjSXUH-14KbygW99AOBluMava4FQ3H8FGVADRDgamYK6tcPWHwuT0VBsK80XVKsbqsYfTSM8FMXQca7LgZ0zSXsrTlyADoyoDXXEIiIxScjwAOsT0CcFNKLFVvbPQ8-n6Vrsx8v13-OM8Pbe5SPZ2PaoM_qZReXTBgqQEilljx4_ILlvNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلم لورفته از پشت‌پردهٔ مقاومت در برابر آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/438854" target="_blank">📅 22:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438853">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261e43d697.mp4?token=jdrcoaidx3-FVoydjLFGWsXKHqwLqNMjJa3dQFwXfp1Pra2M3m8Ih_4CPqKXswSaQKn3SYTkHa31qp3YEWfK6MzpMpvXMMt15Er8k-iHStC-TNLEbL9i78xtotbof46XepirVhZemXSkT6MZSAV5jILDsE8L0dU5N76eT51TvbfXBCZeOicpO3CFD672BMbYnXnPwrx6v7FYfKdQfmv5MzsRG6kEHE9LaU3b6fSNuFWRihPZIfa1CR7VyCV5JJ6uIlsUjgWbyF3veuGP0q4HVLDOnPJB8DE7oMYhYpXKpp1AkZlI7RrnSSjbVFa0hBiLUWtcwnQVk0-DasbkoxQo7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261e43d697.mp4?token=jdrcoaidx3-FVoydjLFGWsXKHqwLqNMjJa3dQFwXfp1Pra2M3m8Ih_4CPqKXswSaQKn3SYTkHa31qp3YEWfK6MzpMpvXMMt15Er8k-iHStC-TNLEbL9i78xtotbof46XepirVhZemXSkT6MZSAV5jILDsE8L0dU5N76eT51TvbfXBCZeOicpO3CFD672BMbYnXnPwrx6v7FYfKdQfmv5MzsRG6kEHE9LaU3b6fSNuFWRihPZIfa1CR7VyCV5JJ6uIlsUjgWbyF3veuGP0q4HVLDOnPJB8DE7oMYhYpXKpp1AkZlI7RrnSSjbVFa0hBiLUWtcwnQVk0-DasbkoxQo7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائران ایرانی در کربلای حسینی یاد رهبر شهید انقلاب را زنده نگه‌داشتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/438853" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438852">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYxQTfPPuR8DQSDSQ0fne2VAbuAUBehB4QfbKNv0ijLHv8Oqs7BXgQVWQu0tGB7fIDBV2KAiU-hwzQ5_UhcB5P7qWqW3RHbIiE2AG6Fv_ynxYrLrJn7nGnbjmOsxPbkvUbdH1NcqOfD_cO-97YFsWwzeqkid_2S19_GNjXcmkRnwgJS7i3Wt2C0g5Vs06Oc9nFUv8dL7zzDCjaG4iYPE0bBJlkdEdBfKVPRwT07nqkCOtUdNcyPsFYj9pPJzJwDBWymxZ9WiM7KPP2ye3qxx_RMX0yd5B2BQQAGH15nZM-c8JoMyuH4_iH6ccSMaGCBNBixiRhEF97t2u9fVTgYAYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان مشارکت در برپایی مواکب برای آئین وداع و تشییع رهبر شهید
🔹
علاقه‌مندان برای مشارکت در برپایی مواکب، ایستگاه‌های صلواتی و برنامه‌های فرهنگی به‌منظور پذیرایی و استقبال از زائران آیین وداع و تشییع «قائد شهید امت» می‌توانند از
اینجا
اقدام کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/438852" target="_blank">📅 21:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438851">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186ff4263.mp4?token=KUn343VlybK1r0pYvZ5CIqjl9EzJdTttgcofbKi3n1ssOFYif-jg9bgS7J-pDzS1MmzEtjKNGqAzdJ4qtW39gnVAsMdb2IJbUUEJnlafN-CrdLEKPep8TPsDM9X05zUdDh9_JyD5djEh-vE3rUrAWNUUQNqxH1_pETBm6ZLGovMu9bYfn1YBpemWrCr3x1eXxJ9LBx-GKIOS_1i8Nx9Lnl95lqCn04_zlwXkzh3rBHmothRIzI7PWv8gPQoXIWzXu_FQzGy1BPjRAGS1KLWU3YhJjxBFnyygUWplem7h2hu06c_sXqv4uiaFlUBlm9nWCO5gwrOE_8yLx5G5mRkiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186ff4263.mp4?token=KUn343VlybK1r0pYvZ5CIqjl9EzJdTttgcofbKi3n1ssOFYif-jg9bgS7J-pDzS1MmzEtjKNGqAzdJ4qtW39gnVAsMdb2IJbUUEJnlafN-CrdLEKPep8TPsDM9X05zUdDh9_JyD5djEh-vE3rUrAWNUUQNqxH1_pETBm6ZLGovMu9bYfn1YBpemWrCr3x1eXxJ9LBx-GKIOS_1i8Nx9Lnl95lqCn04_zlwXkzh3rBHmothRIzI7PWv8gPQoXIWzXu_FQzGy1BPjRAGS1KLWU3YhJjxBFnyygUWplem7h2hu06c_sXqv4uiaFlUBlm9nWCO5gwrOE_8yLx5G5mRkiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع نود و یکم مردم بندرعباس عطر غدیر گرفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/438851" target="_blank">📅 21:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438850">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8d222832.mp4?token=HSWfnn4B5jsNYQ0s_eoHx6IsXtxc-S4LEHktF63x2TmA4xn4n77F6-tTPVyl4YBxDLx1l_iebL6yyY3H8O-2bzqe5fmNz8qRauPaSEGBXKVnVUTDWid8rlNljoJo_jW59rgvsYUuhfZpoUsfvYuR-z9hc-VAwZVAomEy0LmhOBY-k9bbDaYHxQCz0U-J9xwtHitU8PC3PrSdbQahi2j7Y2c3fxIG7XdKuOHlHd4-RWuNDSWM1-cHarvJfw58jw9H_BLn9uskPnmZRKiokfwQWW18DpBonLETZyJFRX59WpN5J-KRQiBg8btsjqUYynZO9eYzQX8zceNN0Nxqu9vSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8d222832.mp4?token=HSWfnn4B5jsNYQ0s_eoHx6IsXtxc-S4LEHktF63x2TmA4xn4n77F6-tTPVyl4YBxDLx1l_iebL6yyY3H8O-2bzqe5fmNz8qRauPaSEGBXKVnVUTDWid8rlNljoJo_jW59rgvsYUuhfZpoUsfvYuR-z9hc-VAwZVAomEy0LmhOBY-k9bbDaYHxQCz0U-J9xwtHitU8PC3PrSdbQahi2j7Y2c3fxIG7XdKuOHlHd4-RWuNDSWM1-cHarvJfw58jw9H_BLn9uskPnmZRKiokfwQWW18DpBonLETZyJFRX59WpN5J-KRQiBg8btsjqUYynZO9eYzQX8zceNN0Nxqu9vSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تساوی پاری‌سن‌ژرمن به آرسنال توسط دمبله در دقیقه ۶۷
⚽️
آرسنال ۱ - ۱ پاری‌سن‌ژرمن @Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/438850" target="_blank">📅 21:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438849">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5747870e0.mp4?token=XtJidSvFSujfWiExh_a7hrOeb0IRnY4TgqJ4vB8eA9qoeIaLkrDc3bBbP9LOuLie8ALeb_ti91lQhYqiJpBKezn-zJhkfEc9xUFnBZnMsxTNYZsz9oXEoz0vvnqdNhq4JK-ZDjPnTEbpFcjzrtP34Vn6RJmgZ5cwxy2C736wl5m_3K_fI_fXtTCobB3fkSHss3eIF_avUQdzkdAaBnfy1gYgRPHcrkSSjihXGPkgy1CF05jgwlvAtjA21kA3-wKf-meZoun9dt7selyXA5n5fsgv6R6swZyxL_vkyIjnkKx4IDXkaRElw1Nt1TfTa_vdWm9JwSKt5uQYoMz--zCaKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5747870e0.mp4?token=XtJidSvFSujfWiExh_a7hrOeb0IRnY4TgqJ4vB8eA9qoeIaLkrDc3bBbP9LOuLie8ALeb_ti91lQhYqiJpBKezn-zJhkfEc9xUFnBZnMsxTNYZsz9oXEoz0vvnqdNhq4JK-ZDjPnTEbpFcjzrtP34Vn6RJmgZ5cwxy2C736wl5m_3K_fI_fXtTCobB3fkSHss3eIF_avUQdzkdAaBnfy1gYgRPHcrkSSjihXGPkgy1CF05jgwlvAtjA21kA3-wKf-meZoun9dt7selyXA5n5fsgv6R6swZyxL_vkyIjnkKx4IDXkaRElw1Nt1TfTa_vdWm9JwSKt5uQYoMz--zCaKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شبکه ۱۲ اسرائیل: از صبح امروز هر ۲۲ دقیقه صدای آژیر حملات موشکی در شمال اسرائیل به صدا در آمده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/438849" target="_blank">📅 21:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438848">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837a69b9b6.mp4?token=aoudzo08cPdAdIkfeek4iRrVQPr4CWdpMDlR1EyYylyWAo89Y11urnJXCX5mlrtwS50KVPGzbwjXula3N1kCcfueuUzn6oMMxMatHcG0fFV8Ovm6vwM-fvKNWl8nnATLZsYUEkgaYA4Z-4NhGxAnE6t00DBFMboDDmnfcDlcx2wZfrKWdmz0OK-_5E1s6PRe79z-yF9SV1eWiJn283cU1s70YE1ydxi3rWOqFbIm4LAzdTmVtFDcmfRP6rQN8jggRFkTMTBocudOl_oWDn-wxgvu_0uNNiYz0Q85SO_hiKPcINYXXDWsh9hpqAReKdHJTqD72Sr4cugLxftpr2ihgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837a69b9b6.mp4?token=aoudzo08cPdAdIkfeek4iRrVQPr4CWdpMDlR1EyYylyWAo89Y11urnJXCX5mlrtwS50KVPGzbwjXula3N1kCcfueuUzn6oMMxMatHcG0fFV8Ovm6vwM-fvKNWl8nnATLZsYUEkgaYA4Z-4NhGxAnE6t00DBFMboDDmnfcDlcx2wZfrKWdmz0OK-_5E1s6PRe79z-yF9SV1eWiJn283cU1s70YE1ydxi3rWOqFbIm4LAzdTmVtFDcmfRP6rQN8jggRFkTMTBocudOl_oWDn-wxgvu_0uNNiYz0Q85SO_hiKPcINYXXDWsh9hpqAReKdHJTqD72Sr4cugLxftpr2ihgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاریخ‌سازی ایلامی‌ها به شب نودویکم رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/438848" target="_blank">📅 21:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438847">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfe0b7103.mp4?token=rN6EATdOVpud5YTb5r3n_u-5OoWqA2VFzofqAemJ3bM-5ugN6-S1DcI8e2Z1ug5QEEtRzx-q2Qsj1KTLtH8O3kepzgML9F8hoUaOKa8ONBcWa6F0uWjpHW9k-lLAeGNIbq3B6v_rzAXYPU_rlZCeYWc-Od-ZJWVaaZyJLfG8-IP9LbcH61lCGpMgVkUHLk4MB1jV7nqLiwAfUVIv9wmohQ0xtPTbZAU5qllPlAFEuvLDFDyEj_EFhitrplaLY5r_pAFH9ObAl68d6_dZXJ4__4fe37k3idDAjn24KXW5MrOuFad_B9s5ZnkeDzJ27GezzqTtZiL0j6lQ4i0aHM3w_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfe0b7103.mp4?token=rN6EATdOVpud5YTb5r3n_u-5OoWqA2VFzofqAemJ3bM-5ugN6-S1DcI8e2Z1ug5QEEtRzx-q2Qsj1KTLtH8O3kepzgML9F8hoUaOKa8ONBcWa6F0uWjpHW9k-lLAeGNIbq3B6v_rzAXYPU_rlZCeYWc-Od-ZJWVaaZyJLfG8-IP9LbcH61lCGpMgVkUHLk4MB1jV7nqLiwAfUVIv9wmohQ0xtPTbZAU5qllPlAFEuvLDFDyEj_EFhitrplaLY5r_pAFH9ObAl68d6_dZXJ4__4fe37k3idDAjn24KXW5MrOuFad_B9s5ZnkeDzJ27GezzqTtZiL0j6lQ4i0aHM3w_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول آرسنال به پاری‌سن‌ژرمن در دقیقۀ ۶
⚽️
آرسنال ۱ - ۰ پاری‌سن‌ژرمن @Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/438847" target="_blank">📅 21:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438846">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWf_z9HY_3uooAWWe94wpvXvi6oAD0lw-Ln0hU6wa8kNvSIAUcc0TUP3vSH1MN5kQeHAthoZfhK6ra9mhW-PH92WsjREm2v0Eds89p6YJJqWizSnyyDg4cETKro2nW2B4RrdxkA0pteMblOHVJ6jecdkWH44QfGRZGspT1wU0qc5UFiS-2tCaYNA1mBiJx7PtHppOcrw1vQuMovK6ku7xsXFH1pQl7fXTIRpgyr2biPPu132D01oaGlHtWIktXyUBhEsx3F2FcOq3dWxDr6AbltpivDEDHFbleUNgMOdjAzSNnc5fWAl_qS3SG4w_Sc4T0kHCStR8Gq9VOi4DGfVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار‌ وزارت بهداشت درباره نوشیدن قهوه در تابستان
🔹
مدیرکل دفتر بهبود تغذیه وزارت بهداشت: گرمازدگی و حمله‌های ناشی از آن زمانی رخ می‌دهد که بدن قادر به خنک‌کردن خود نباشد؛ از‌این‌‌رو وجود آب کافی در بدن اهمیت دارد.
🔹
نوشیدنی‌هایی مانند قهوه، چای پررنگ و نوشابه می‌توانند موجب دهیدراته شدن و کم‌آبی بدن شوند و بهتر است در روزهای گرم مصرف آن‌ها محدود شود.
🔹
مردم حتی در صورت نداشتن احساس تشنگی نیز به میزان کافی مایعات مصرف کنند و منتظر تشنه‌شدن نمانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/438846" target="_blank">📅 20:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438845">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51323067c2.mp4?token=RfwznwCwERZtcs4ZlJTt9h3HEpLAKAG_8jP70sCsx72RE8UJl9wQYlAx8iOrQfoeRnJhU2qP4Rn2Naw6-x7XUt67BlzdWRFJDX_lWixIwAucO9P1GNxm6DPt_OhxI29R9gfT4Wov6AExRmdD2zbGw0lFSLlYzh6hVEukQ6IsdcmH9pkFy_tlxqPiJ603cReNtbOA9Gkzh_YeHHg7CQmuxzLkjQeBhBeMLrtHEwjezY1ZlY7poppiBq0UUzHljFXm7Bs4m80x9ckxPQh9crCF5hmkkOGpWlbvkLwmWWR9R5xZbu60mGiq1KRozK6KesIQAliLoycTKSVd0pLPPSBrTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51323067c2.mp4?token=RfwznwCwERZtcs4ZlJTt9h3HEpLAKAG_8jP70sCsx72RE8UJl9wQYlAx8iOrQfoeRnJhU2qP4Rn2Naw6-x7XUt67BlzdWRFJDX_lWixIwAucO9P1GNxm6DPt_OhxI29R9gfT4Wov6AExRmdD2zbGw0lFSLlYzh6hVEukQ6IsdcmH9pkFy_tlxqPiJ603cReNtbOA9Gkzh_YeHHg7CQmuxzLkjQeBhBeMLrtHEwjezY1ZlY7poppiBq0UUzHljFXm7Bs4m80x9ckxPQh9crCF5hmkkOGpWlbvkLwmWWR9R5xZbu60mGiq1KRozK6KesIQAliLoycTKSVd0pLPPSBrTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری اینترنشال: اپوزیسیون تنها رؤیافروشی می‌کند؛ باید گروهی مثل جولانی در ایران تشکیل شود
!
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/438845" target="_blank">📅 20:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438839">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDQyVdFebdcSKhPI6nkMZ3L0KCv4tJOe-9pzDzQ0aLqgwO_04W7bvkTTvLivM2o1WXx3j5_rSdfvAQ_LGNBRpB118bcrFnrj74i24Ya1uwAjC1D6Fi2NyFHKSbDyVUnKcBGlgpR1x6TeBRwPs_3mBjEoRXvUPA9dO3wE9TPn_FLdj9N9S_befnuD6EAZAmF1CRixJvxrt80JBrlP8gYzZYwfFtmtw2iF84weCBBSpxET2Ufx7xMeyl5eut75_OOp_GDW5494UZ4C_gKX9QQT5H5wTNaDzm5SRv_iIDYmsxMiix7HVQEf4_Ejdf3BBAgFmZyPHVDogrjICSoeToIW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kI2BSFBvgpsUH_wueHBTvLqEwMBKvgYA7PrpoOwwMujr-yj7kiZ5Xi-xplxGRGhplGkT3IES24aaLzSPAotYr6TWNEJUyIShr9wBni6t-MkPHles5z-zRufAxUbX4n6DUpYKahcuHz5XnzerS0GTZe6PPwDp6mBRmEM86uSogQ481Z-d-V6BAdA6mQFS7PkFByr-R5v3zcMR5AC8QitvOA9Hx3HL0XSrpv4f8Ae4eVvw-3j6pGGVFIficgemUYRBznVQ1zxHsiGykw0UWj4s6XKyhfc1vKx_SlFtENdwg_WXeBpdBY0jkp3lSprVEYRcaUNhbbM7-KyXX25dI9iqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pwzi8c4ACINAYAO66Gy6r8miX3CVkcLOP-BWxOBTVahjnuyJ4UdF6QwVv9rEXI71DCBlOg4OPMvMm5RQPPFQhIbFJvfO0q9OnG4_e64GjfJa81sJ5UkL7u-eZnWWmed6671MynJmR1OWp-KT62vGrpIvreZfUps7WJZWMJisOZ8w-jzZxNwzuXd6jKCX2ctSchhdvcm24AAg9KZMSvunnYarQSiJCBRvKJk5W8Nojlgkn1mkV6FlPNh_Aij_3Hk2vSoiw_Qj73Wh9K6blUb0igklneNusbdM7O0SvPgHbpyUEIz963kpNbbaW3-hEP6S7cM1aTxHtgq8-_hzKjUtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cf_Q7HzieyY9ItZ2yNLQ5bUSA7t2aGzRDARbANO2C9BQo3eMNqALYHWwa1By9S6uNGDNYWsy0tAAANCtU6HffzubQX4oWdn4JfBMvyPFn0Lkfi3cspgfznNoEh1sLbK0h8IPX0nSoJVqwk2IhYlNdmvXTbJhOHaa4ChhxkTDCwiGSSxmsH99EiwJAkpbGa3pAJR62S_lxyoxjQBaf8-3mGPqbP4tgjHs8tYcn3X7r4SNhJDhntdCXnML1vkjM17TbW7k2mGALZaERrhsvgVTf3v6RgalbN-0TtMuCs1nTpT7PMiieD56pusZyfd_bWzVo2p9r9S1F8Up3TIXdfhlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKoAE9X84qpv4uoFHhvMN7wdJiUO7sRTi0ncjC14C5yRr71c9bwWSpFGMD4YQGKb94L0RJRezk57c8SL45e2uswLE8QzrSkXf-s3TI5uOM1RJVC0nIEeGeiX6K-uc7zO0PyhmGOLx0NbxyqHlRFl612F2_lrr1D6RvM39anDR6b9LVD9s-kX7K82mrGxsdlrJENordSylHYH4HFv6DochQgJTFa1rqq2n8hLUqjDsR7ivIxKFCwQIqNHsxHDYs7oLVfG9LD1AnONZDABzkf4-b4nNDLjG9xIFjwapI7j2zNlwHoVMYSQuNzA7rPdP-p6yDt3Ir04OUJiwlDSPrxxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AeOyBwamN9TF3tC6n-UtZOYQmU2nK24XpKG7P1bvWJj5XzSYkIUr3CzVLFX5cjlleHIoOWWFd-xLCVyOpGklTuLDZepX0KOA04LAWr-78CnbHqu-Rz0sJKKFk6RRi14r5YC_-5eA4zTHdhtfPtcOPizTOK_IoI2UIHabmy6uzGn1Ke5e3ilxPvOMxUeqy438HwuRG3N5zg8MutvojnLihWCO_HzM7zsbvd9FXpi4DsIyUpkLHFQRJBl7Sh0HB74In4zqrK3QgrqHZWAxk9o2z8uS3rR5E-lE_zAW0kx2WsO5NCjDiq2MshtILzPVAywzibakwgxvWW95Tum7_rHA2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رئیس‌جمهور برای مدیریت انرژی کت خود را درآورد
🔹
پزشکیان امروز در نشست مدیریت بحران آب با تأکید بر ضرورت مدیریت مصرف انرژی، از حاضران خواست به‌جای پایین‌آوردن درجهٔ کولرها، کت‌های خود را درآورند.
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/438839" target="_blank">📅 20:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438838">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJE4RkImuXaVYy6NgKpxUfHrU___OMdWoyMZvyTM3H1pbKlND9SNbwtAzJ2KeRBHE3iG5r1pypilvLDPuyHX8hSuMWWHr9ETN5gF_XGeaXywarHhbQWpIqOf664sppUwgdY3mgJqxq8nXAKXj9ljmMz-gU93sItP4xLeWdVH-5DKiKWXtrc2KBtVYa4j570EjvV9cpclOHXmSsqtd3IePkda5dUP5JTewHJX6q0o-FJYAK2eQB0B2vy3wnKhVijMuZEvTTRB2YeUX_gPZIlS2nXcHMznIlFSGznmDP7tRfPL91egm5IuPap9CE4CqCPxT6_Usx_zno-r8YKU4zRTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیاتی از وضعیت خوش‌حسابی مردم ایران
🔹
از حدود ۵۳ میلیون ایرانی بالای ۱۸ سال که اعتبارسنجی شده‌اند ۲۸ درصد در رتبه A و ۳۰ درصد در رتبه B قرار دارند. باقی افراد حدود ۲۵.۲ درصد در رتبه C، حدود ۱۱ درصد در رتبه D و ۴.۸ درصد در رتبه E  قرار دارند.
🔹
با این حساب، بیش از ۵۰ درصد مردم ایران جزو افراد خوش حساب محسوب می‌شوند که برای دریافت وام هیچ مشکلی نخواهند داشت؛ در حال حاضر بانک‌ها برای اعطای دسته چک باید حتما گزارش اعتبارسنجی را مبنا قرار دهند اما برای پرداخت تسهیلات، مبنا قرار دادن این گزارش الزامی نیست.
🔸
سابقه بدحسابی مانند عدم پرداخت اقساط و یا عدم وصول چک به مدت ۶ ماه در پرونده اعتبارسنجی افراد باقی می‌ماند بعد از آن در صورت پرداخت از سابقه افراد پاک خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/438838" target="_blank">📅 20:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438837">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDf2s0_W86phsMD6Q5CNqDwheqvywPHeLkAWfggmNccr1oYO8v4xX6BlO2ZmnNb_MYbIOntIepJM0eq4zIRWFmWXzwLLodJrgY2Vc4h2cDMPWnFXbXHBfZ1LWAJ5t2uk7rmXgEKPym5QySK1EbDWoW03WyIxXoTY84OHDElLcmCgEKUkiRQMDa4szwpKuh5hq74ar3NcZ5bNeKpyEEdkvK6vV26d4rlgehI5-XxlcwCtkwqj-7-DfjLVZeHKy6MIQ-Jk2H7hGBqvm7pSFixzXvfqS2NyjibIXg2aVs62qRZxeanRyXzV1dwTjT_5ntQFstxBs4C6Es7eJcO2UlOEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی نخست‌وزیر لبنان از خوش‌بینی به مذاکره با اسرائیل
🔹
نخست‌وزیر لبنان: آنچه در جنوب، النبطیه، صور و روستاهای آن اتفاق می‌افتد، دیگر تنها علیه مکان خاصی نیست بلکه سیاستی برای تخریب همه‌جانبه شهرها، روستاها و الزامات زندگی با هدف کوچاندن اجباری و دسته‌جمعی است.
🔹
دولت تصمیم گرفته است که مناسب‌ترین گزینه را برای محافظت از لبنان در این شرایط دنبال کند؛ آیا تضمینی وجود دارد که مذاکرات به نتیجه برسد؟ قطعاً نه.
🔹
دولت از هیچ تلاشی برای دستیابی به آتش‌بس، عقب‌نشینی کامل اسرائیل، آزادی اسرا و بازگشت آبرومندانه و امن مردم به خانه‌هایشان و بازسازی مناطق آسیب دیده دریغ نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/438837" target="_blank">📅 20:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438836">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هشدار سازمان بازرسی برای استرداد وجه بلیت‌های پروازهای لغو شده
🔹
سخنگوی سازمان بازرسی کل کشور: برخی ایرلاین‌ها و دفاتر خدمات مسافرت هوایی، با وجود صراحت قانون و بخشنامه‌های صادره، از برگشت کامل وجه بلیت به مسافران خودداری کرده‌اند که این امر منجر به نارضایتی…</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/438836" target="_blank">📅 20:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438827">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vChUr0GIE6G1BrZScoY1I1mumZrnf7O1R0ZFSWWpmeWgvRArmO5h-0FAiKnUQNmqswnH68my_maJXkPbQ5j7en3e0d0UoYn0pAVZlmS7wBz6t-KZIPhdvmhIzEpaPwzLLX4ZSJdIhNuxqSF0DxGI3J1pWn_9p68GmnSbTyVJ2RZEmOEFlafPNrLZp33EMRK4Fe-UAqnAo7TBk3CFFN-lEGqeaKcJqOBXNKcuV36XKN0t_33ezQ2v1epXhrJ9lLGiTfSSDiCTPNjHDxeFoFN3Xv_avDyM2_nyGmTJxeI-Fm1WSxLdlQZdHIq6DdLH9FuUQRckS9s_Fy_DpvsKgQtVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWm06clmkAHqIV8sqNXg18H3vcvQHGGoQhbiJK35LZMoJG63M7GFxXXWW7KDoFrFpakAOt6ROZAgRGz71N3p7O_6_qf-5a7u_oW4Ih6zNX8E5W5RnID0PeSWywmiNAqfRXalXZzMBNwDYnk4ZWbkNwjV5MqUBKY3vWC4si9QttTtw9M3EUrRfjsHF7sYVRXZjQbpqTMHbehpM3qwSpMBmKxZxxiibXsaAXDRHbQtQN9rfgMgl0Of0UaNepGJrwty01LSvwxihzhPDDVHn1cnr5twGZg9Ha-Faz2fp2kSzwZF0zWKxKJEYoV2Xgz80Xz_kG76hpvjLH0X3N9S90GWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkJqCqQNVLPx1RzivNKb0rHVFk23lOZYyKRw0Nn4fFYNKNqiyd-KuS3Wml4LVQ0pfgU3pnz0WjJM_qf9Qjd_XDsigvLATCeVMpIeWk4oQd1Z_a7PyHJp-o7tjYCNCcJiXWVdIWcM_ZQIq2H6ftYX-6BRzRmA5hNIl4VcgmM6AOb3k2N54QjX16T_tG7ZwrQrQiAGDj_h-SEzg4kVXH9e-vA5GDEtecZx8gjfRjQ_QmeD4oge94x8HysFUbBT3VQeELU6HmR2eZxCByUKWxVCmmdsSMn9064yxDHbPd7WuKbxtN_dCYcG9b_bQdK7HPCRbWolNXPVjI0K5xzk9q3Spw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsgY8Pv8BxPKudnwRMOqDJAg-F448ACeteMlgZE7pDa2-D9huoxjG-bE20Ljk7j4OSoFUUpTmmdkRoHLBQP18fAhLD2UWOU_TxcR1cNfQ7LGCgQaR-WpEKXtxGbMX5ne7i52-XWEDwGo2VP5wf9RS-S2QANLNEJNaaGAb9Ca7gkNenzLZjVuCuj27g_1ToKjbBEBewHYfXgaUBYeJufKdOw9fTuv1G6y4Gbg6DrLqUIZi102LPD0OGvZvfnUbrKnJWl0A-yTE4lwsph2sQZXYbaj67PKYGinrKrpB9xoKVUayDZ1Ih1VCGcxRPjxko4cgDC9iBYIFR3dOSSJDBrFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LP8sROcD026x_Tz4fNCeatduSJmemhro1LHYnbi0-Iw2cOcCLn3--9BTXJxx-TuinfmZAWaX-8Gcdq7CIJjM0_hLGi8bLBHiqTRwgWcuwBsnKkBacr_GVyFhTAghidzqyohJ7ZX-3p3NIYbOvgu4MDnzi9TB0thTy8Lfi9JacRW6w5CSKe8-kn0RN46mcnzjxIQaz8tQp7qTwXycsQkpwIthjp8M6bXnafEZL_M4T4miNWoOdedEUbtB6_AoZ76sBNda4zd9PfHSGKekKSpivRuO2_kj__EC9DKhixXnpZA1Mrc8tqrlH6z5h97vlwG6lYqfKSPjk_o3-PErRD9Nmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCGEmcs5DC4IdcbK2kKvEER9x_tFCOWZwxDiBrd2g6IGDksDpT2zHcE6VZ6m3gaSReoN92k1L12Ff40-cZcmiZOX7Pv-I9-8PkNM6i5jhLbB2KNS7lcaaXAlCYSlg7WaaGk8586qEJwDuFnQABqD82RBi8szt_1J1FEaVR63VZNIvAd8DliyAqmbvgNrt637HeEJaoaE2cWgCYbNO8bYGgG125rt0xVveJuPaYTZQ3HYlI5wPyw22YSPNFQaUni6pX6aRCrN2iQh8FsAIu1VX-hSC4rD4CDenCSNiwAcvMrB5bfDNEJjLIUQCGHAKIhtz8EmIOalyQWd3LhLUM9-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zqo0xW7AAoRnDyMyc2Ge67-5jeAO3xlzfuIFkXXzR6ZbCUzAhL2bGT75BNO3SS3puHuPiwjVlf6bo2V6xLOyPSkm8v-e7GnrnVI7TloQPru1IqwkfL0br-3f4QZNNAiTeR_-JivFWoBFoJbbREs6Zyx0A8aVZs8O8JJOIx9ATmiRAflc5i0Tt84yngb-6zt5y73V5xFkUPvfAFfOgMz9h8v7r-X4K5G6mYU_TNdp01sxbnvqZaGe83u2-7S36X1foIasy7RmnN_kG10l5xDvu-ji4W5uhmGRqo5g5SwbE0r3WWLmjNxDZLtab6nKquyoVquGbMV_9YoxwI5T8Z1WZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گشت‌وگذاری در بازار مریوان کردستان
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/438827" target="_blank">📅 20:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438826">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روزنامهٔ معاریو: اسرائیل در آستانهٔ شکست مجدد در ایران و لبنان است
🔹
تحلیلگر نظامی روزنامهٔ معاریو: هنوز مشخص نیست که آیا توافقی بین آمریکا و ایران حاصل خواهد شد یا خیر، در اسرائیل، باور غالب این است که توافقی که در حال حاضر در حال تدوین است، بد است، در واقع بسیار بد است.
🔹
زیرا آتش‌بس برای ۶۰ روز دیگر تمدید شده است، در حالی که آمریکا و اسرائیل عملاً هیچ پیشرفتی در دستیابی به اهداف جنگی خود نداشته‌اند.
🔹
یک افسر ارشد نظامی اسرائیل که هدایت عملیات علیه ایران را بر عهده داشت، به وضوح گفت که اگر حکومت ایران در قدرت بماند و اورانیوم غنی‌شده در دست آنها باقی بماند، ما به هیچ یک از اهداف جنگ دست نخواهیم یافت.
🔹
اکنون مشخص است که تنها یک برنده در این جنگ وجود دارد و احتمالاً آن آمریکا یا اسرائیل نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/438826" target="_blank">📅 20:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438825">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ecba9eb1.mp4?token=qE4H_BPrTaFyAOHh8-aKZalRkTH3RybSzSwi7K7pFKrQsHW9b_S18iFRq4YPWFoUH_rq1BNzVs-3qH2YuRgWf6MAXhCU7rjtkZK7c_eZRUDPlP41uW3zvYjokhFqPowSDCXh4m0joSxxUgdtN7_bMTqHcWeJzxjGB0aLqzr0f7qPDbY14Nb0SwEo_dM-lLZ_A9YFUBo7oPPS6sTSszSoXihe1UlK4UjtVVX6RF1JwnNQ_EXb6Bwc_kU7n4BFBIsmz6E8e-RM8vSmylZ0w1CEDNCVWWQIONs_rCqfGyKxbO0akrzb8XD68SQWe3lG6ZHlxiJGbzI7hg76xTSMSXdp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ecba9eb1.mp4?token=qE4H_BPrTaFyAOHh8-aKZalRkTH3RybSzSwi7K7pFKrQsHW9b_S18iFRq4YPWFoUH_rq1BNzVs-3qH2YuRgWf6MAXhCU7rjtkZK7c_eZRUDPlP41uW3zvYjokhFqPowSDCXh4m0joSxxUgdtN7_bMTqHcWeJzxjGB0aLqzr0f7qPDbY14Nb0SwEo_dM-lLZ_A9YFUBo7oPPS6sTSszSoXihe1UlK4UjtVVX6RF1JwnNQ_EXb6Bwc_kU7n4BFBIsmz6E8e-RM8vSmylZ0w1CEDNCVWWQIONs_rCqfGyKxbO0akrzb8XD68SQWe3lG6ZHlxiJGbzI7hg76xTSMSXdp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله: ارتش اسرائیل در هیچ نقطه‌ای در لبنان نتوانسته مستقر شود
🔹
شبکه المیادین به نقل از منابع موثق در حزب‌الله لبنان: دشمن صهیونیست کوتاه‌ترین و نزدیکترین مسیر به مرز را برای رسیدن به رودخانه لیطانی انتخاب کرده و با توجه به ناتوانی در تأمین امنیت نیروهای…</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/438825" target="_blank">📅 19:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438824">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b3b30263.mp4?token=Vu1n47pVcTh-i_HNyo-jo4VdQN4bwnGbF1ldL9bSOBjSshYg_6cF55ojr6ibNEtWRGh20nh6z3GYDGdYOZhVeGarNUvgq_WYPym0iuHBZvjFJ97jhYBd7c63qwm7D0y12sGitd7wwMTQ95oJ12u3NkHj2FuQMfHrMSZDZRxTOXZmXkrBqNy9LZct03yJdjlBlLf95hENFNBh6s_zqC1DzMISEp7N4gKO7XSzKiZZXfe5ge0FhhqjqqIsayRqjEcm73sO-W-r50e6JzDYxXtOam2_c1Ish1MtUj72a885l6GRW6DgqVAbO0lujQmZQ0lmMnDBSSrVcrG59U0vbIAhpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b3b30263.mp4?token=Vu1n47pVcTh-i_HNyo-jo4VdQN4bwnGbF1ldL9bSOBjSshYg_6cF55ojr6ibNEtWRGh20nh6z3GYDGdYOZhVeGarNUvgq_WYPym0iuHBZvjFJ97jhYBd7c63qwm7D0y12sGitd7wwMTQ95oJ12u3NkHj2FuQMfHrMSZDZRxTOXZmXkrBqNy9LZct03yJdjlBlLf95hENFNBh6s_zqC1DzMISEp7N4gKO7XSzKiZZXfe5ge0FhhqjqqIsayRqjEcm73sO-W-r50e6JzDYxXtOam2_c1Ish1MtUj72a885l6GRW6DgqVAbO0lujQmZQ0lmMnDBSSrVcrG59U0vbIAhpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول آرسنال به پاری‌سن‌ژرمن در دقیقۀ ۶
⚽️
آرسنال ۱ - ۰ پاری‌سن‌ژرمن
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/438824" target="_blank">📅 19:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438823">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌ ‌ رشد کم‌سابقۀ سکوهای داخلی در دوران جنگ  طبق نظرسنجی یک موسسه نظرسنجی وابسته به دانشگاه تهران:
🔸
سهم کاربران فعال سکوهای داخلی از ۴۵٪ به ۹۱.۶٪ رسیده است.
🔸
روبیکا مهم‌ترین مقصد مهاجرت کاربران از اینستاگرام، تلگرام و واتساپ بوده است.
🔸
۵۳.۸٪ کاربران از سکوهای…</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/438823" target="_blank">📅 19:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438822">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌ مردم دربارۀ مذاکره با آمریکا چه نظری دارند؟  طبق نظرسنجی یک موسسه نظرسنجی وابسته به دانشگاه تهران:
🔸
۶۲.۳٪ مردم از پذیرش آتش‌بس توسط ایران حمایت کرده‌اند.
🔸
۵۴.۲٪ با ادامه مذاکرات موافق‌اند.
🔸
فقط ۴۲.۱٪ احتمال دستیابی به توافق را بالا می‌دانند.
🔸
۷۸.۹٪ معتقدند…</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/438822" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438821">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آخرین نظرسنجی از ایران پس از جنگ
🔹
درحالی‌که جنگ روانی دشمن بر القای فروپاشی اجتماعی، گسست نسلی و انزوای سیاسی ایران متمرکز شده است، داده‌های پیمایشی یک موسسه نظرسنجی وابسته به دانشگاه تهران، تصویر متفاوتی از واقعیت‌های میدانی ارائه می‌دهند؛ داده‌هایی که نه…</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/438821" target="_blank">📅 19:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438820">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آخرین نظرسنجی از ایران پس از جنگ
🔹
درحالی‌که جنگ روانی دشمن بر القای فروپاشی اجتماعی، گسست نسلی و انزوای سیاسی ایران متمرکز شده است، داده‌های پیمایشی یک موسسه نظرسنجی وابسته به دانشگاه تهران، تصویر متفاوتی از واقعیت‌های میدانی ارائه می‌دهند؛ داده‌هایی که نه در رسانه‌های معاند، بلکه در دل جامعه ایران و در میانه حملات نظامی و رسانه‌ای ثبت شده‌اند:
🔹
ایرانِ پساجنگ؛ افزایش غرور ملی و انسجام اجتماعی
🔸
۵۸.۸٪ مردم در تجمعات مردمی یا مراسم تشییع شهدا حضور داشته‌اند.
🔸
۵۹٪ مردم نتیجه جنگ را به سود ایران ارزیابی کرده‌اند.
🔸
تنها ۱۰.۲٪ آمریکا و اسرائیل را پیروز جنگ دانسته‌اند.
🔸
احساس افتخار به جایگاه ایران در جهان از ۴۴.۲٪ به ۶۶.۹٪ افزایش یافته است.
🔹
این اعداد نشان می‌دهد جنگ نه‌تنها باعث فروپاشی اجتماعی نشد، بلکه به تقویت هویت ملی و احساس تعلق به ایران انجامید؛ در همین مدت، تمایل به مهاجرت از ایران افزایش پیدا نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/438820" target="_blank">📅 19:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438819">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فرانسه: استراتژی امنیتی ما مستقل از آمریکاست
🔹
وزیر نیروهای مسلح فرانسه: پاریس بودجهٔ دفاعی خود را در دههٔ گذشته ۲ برابر کرده و به افزایش هزینه‌های نظامی ادامه می‌دهد.
🔹
سیاست دفاعی فرانسه محدود به همکاری با آمریکا نیست و فرانسه توافقات دفاعی جداگانه‌ای با امارات، قطر و چندین کشور دیگر در خاورمیانه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/438819" target="_blank">📅 19:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438812">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CL1xAHqjsEm3VB2FNtLplOKlih0e_icumV15KS6O7OWJosSnGCqrxCSPLL7gliMu_S8kXeqXy3seYPziQPLc9NDYIFa_aPjHzFec_xI_iohRl_2bhfxeBx2ltaXjH2Wu0Q_XApytgQqxycXD3-hD1QMspMgM79FpUTQdnm2lFUyedRYWzCR-4sDI15XHQ-r-lT7GybLEtENowjjh6-nA58Y1kaWkYDylpfGfIlI4oUJLOdyuwhA2ya9mtMcWxH-vt9yWOQeL_8eTGXSdhYoj_DV00p7OrZmRjlBZXISKXJ5hx9kmzZfwsGowSQMQCz2Jx8S9aq57Z1tDM63A948JLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSnXX3MKbUiWCn6pimGh_4pzH1rY6eS9A9xqM0PcEOPWZU38wswJGopFCxA7E95ISZgJiDOelXWxM_lBjaHBuMB7YcMmhO6LmVbk4whI8_7wDoCoui7rD-tZCd0erOX1N16bWAs5OltEC_fgh04VHx6WSyl8XZ9U_AWeZKW83DgpdC5CVJFMyZji2Nc6hZqYsPuTX6naIBjI2FZ7bK11urhuN2sj0X29k3VwswJ9BXlcDiahCFWVRvvsQ_L7LoVyeHznjpeVq9UsQeMSfKf3Po0yeuaxpyrqO0uUkW6gVQ8FB4xYom-pLqv2UoHzRWUP-i2srGNplxPjFqhIvwsddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrSY6SQtxkamEGb-rJl7sNx7z0NTm_BManQ8LAbs3zyBaot3MSUlkmJLPmUgiKHEMaJ_vwheLAVcSLAIa1DTlP-wyI4uTMihjI7C5OX9xwaqLngnrB8YSbCpU_eUoEYc0ZfdhcFVRi7SwJjZsEufkR19SdhqsJbJMouzChjw15Kqb4yRHInt8Rqv7ACy8u2zNb5Mi4Z37iqKHxQmkZD2RtvjZN-z0pGBjaUTtPF34xjsbcbsIkFsTIWRLQBqHW23OMgc5E4Of4RS6JtWoUXkL7613lSvrOvshYGxC2228v42QcGAxHop2FR_taTcxPb1sUe8F9yQ1DE9g7L8BGl7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4o9fOXHk96BtoJ0Z9alciCWKZm8Z0hzUX4wpP5c7krRxTcQFwB1IjCcf0RrlZXjWYGPNgXjt4brUT3yvy582ooyP4NMBIqbalnI-LtDA0NfJPYtz6cYYM5yiFW42bIBAN_uTzJeYSEfBtD41Jy2IdgQMqdfi0w2Ht6G1NTSvfoXIpuYMuWhAeunQkuf6U60TofGFq2ixt5bIBDiiuyrCyTF5IrWUinkay93swQq1Bb8XHGD8a39yszC83SM0aGyJTdXVrjwMaozenChjvt03ddkty1zcdhaWwq1HpBqeTXRSEQsKAADWqx9bAMhIeUhV-Km8p8GQxS_JhMhR4Siaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Apea4_ljmWMs_Fgulu4vTVIB0LUj1wCnxbLJKT9Lta2wVeARX_l4C_B3k3jNzPhuZuBO8ZUu-ttb1nv6OWEn3RPtDgUsnUbUhCfgJR5101IFJ_NqjdgjEa5WqbspVrL0EPz-D0m5-Xvcn_85bVEmbTZyBYzrR2YrUV7tf0ePD5x51gTeXUzRIdazZ9rWZPeoTTtvYfAuJIRQ66TLYZrtNAoMIZBRpyo6CCR0NXqR3WuWPNrl7Syy4JWK-yvXcGCneCe4p_cwG6eErHJQQHW0Ado80wLEqNhH7MdL7K_sTCDoUQttsvzdhJe4grwjnRMtqu_wrS1fxtiywJTNvEjnLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
مدیرفروش سایپا: تعهدات معوق ما ۱۰ هزار خودروی شاهین و ۱۵۰۰ خودروی کوییک است.  @Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/438812" target="_blank">📅 18:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438811">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قرارگاه مرکزی خاتم الانبیا: مدیریت تنگۀ هرمز توسط نیروهای مسلح جمهوری اسلامی ایران با اقتدار کامل اعمال می‌شود
🔹
با توجه به یکپارچگی این مسیر، تأکید می‌شود کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفاً ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران انقلاب اسلامی هستند. هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.
🔹
همچنین هشدار داده می‌شود هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگۀ هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی ایران قرار خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/438811" target="_blank">📅 18:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438810">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adfefdfd81.mp4?token=tSWF6Uwx7T2tdhlKmLnWqFDQNK9GF1aiqzgcl-Cock4zyI_pkyq6Y9yVsbX3CGc60ia7L4hR-28Iwl-gm0wtXVFIZkHP4aNbMSPlTwCbGpN1WCMa1fCGqtrB76lvP7cpB4hStotjI-PCgucB_qCWj-E6bA0asqeZOjofNcjgDhd8Nuh7MrNvwpitRU-wYZH8U07TDGKU8AmXiW2C6XMiX_PeNCO_3isiVI_TtBurnDEZsZhEHyUcvUGXJEElZrwW2Xdb9mu13NuduSzJt6QtVou846fxuLqVYAFQsR2mBiBk17SAuxBpW8amzlk-_UHBQw_EIQFYtDFAYn8L-DSlig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adfefdfd81.mp4?token=tSWF6Uwx7T2tdhlKmLnWqFDQNK9GF1aiqzgcl-Cock4zyI_pkyq6Y9yVsbX3CGc60ia7L4hR-28Iwl-gm0wtXVFIZkHP4aNbMSPlTwCbGpN1WCMa1fCGqtrB76lvP7cpB4hStotjI-PCgucB_qCWj-E6bA0asqeZOjofNcjgDhd8Nuh7MrNvwpitRU-wYZH8U07TDGKU8AmXiW2C6XMiX_PeNCO_3isiVI_TtBurnDEZsZhEHyUcvUGXJEElZrwW2Xdb9mu13NuduSzJt6QtVou846fxuLqVYAFQsR2mBiBk17SAuxBpW8amzlk-_UHBQw_EIQFYtDFAYn8L-DSlig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فراستی، منتقد سینما: دوستان سینمایی ما این شب‌ها کجا هستند؟
🔹
من و مردم حتی یک شب هیچ‌کدام از آن‌ها را در تجمعات شبانه ندیده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/438810" target="_blank">📅 18:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438809">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
شبکه ۱۲ اسرائیل: از صبح امروز هر ۲۲ دقیقه صدای آژیر حملات موشکی در شمال اسرائیل به صدا در آمده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/438809" target="_blank">📅 18:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438808">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsOMgMnYWpW4LjMMjT4t5Cb0Ens0uc1wSUUeBkA1Q3eSYrvMP_-QQkTybSiQpsChDdl_ZVr2npgRAubt95o-asgQfXO_fZuXsYvg8uf1tP19FkaVhQYnJXdI2_s6XY87H6861fc3DB5KxlKCaMlLrQiRCMg_bHV76JKsL38jE_3n3rsjoUtj63nMucOX-RaJFoqIzMCeS0THuT2xtzqOuXknbym61FcoQFm9gMzaFd4p4B4QHEZvyGWdQIfS6LO-gOqaLjeBjdcYR9B-p2ZKs0EBK7N1v8uoui22hNEriKlWhbniBC6bUj6RozG2HljuDVZbrMi6ErBq0MZNs1SbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات موشکی حزب‌الله به زیرساخت‌های ارتش اسرائیل
🔹
رادیو ارتش اسرائیل ساعتی پیش اذعان کرد نیروهای مقاومت لبنان شهر «الصفد» واقع در شمال فلسطین اشغالی را هدف حملات راکتی خود قرار دادند.
🔹
حزب‌الله با انتشار بیانیه‌ای تأکید کرد که در این حمله، زیرساخت‌های ارتش…</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/438808" target="_blank">📅 18:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438807">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b05a6002ef.mp4?token=OIkzW-DrpELyZ9EfjjyHk-RyHFWRjKlyj5RI-k7W2-5i5CRQTIPeJdhxvX5GfiJjm9IMPRy7UgTjgchw6lPG2mjJSWD7_S7J4OdDNsgVqoV9NI3exKk6vZvrta9X_r32cJzVqx19I1O35w1ex7D-h-9KtubrRVP3ARBkDPFXMiN0L3AHtZAU93v7ayNUqMG7r-MqhVzuskXry1zfuLkDapzOM5c8Gbb6XgogRuDHtaJ6wZjAf3amrlINABsfkXr3at6fflpq-8muZnEEovj-VnOZaP7u5kytvVtrS4uasSC5oRiuZ7Oc79ISOr8MKNk6ym98L-GauZ3A-6HM2B1M5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b05a6002ef.mp4?token=OIkzW-DrpELyZ9EfjjyHk-RyHFWRjKlyj5RI-k7W2-5i5CRQTIPeJdhxvX5GfiJjm9IMPRy7UgTjgchw6lPG2mjJSWD7_S7J4OdDNsgVqoV9NI3exKk6vZvrta9X_r32cJzVqx19I1O35w1ex7D-h-9KtubrRVP3ARBkDPFXMiN0L3AHtZAU93v7ayNUqMG7r-MqhVzuskXry1zfuLkDapzOM5c8Gbb6XgogRuDHtaJ6wZjAf3amrlINABsfkXr3at6fflpq-8muZnEEovj-VnOZaP7u5kytvVtrS4uasSC5oRiuZ7Oc79ISOr8MKNk6ym98L-GauZ3A-6HM2B1M5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجهیز جنگنده‌های سوخو ۳۰ ارمنستان به بمب‌های ایرانی
🔹
به گفتهٔ کارشناسان نظامی، در رژهٔ هوایی روز ملی ارمنستان در میدان جمهوری ایروان، جنگنده‌های سوخو-۳۰ نیروی هوایی ارمنستان با بمب‌های گلایدر (هدایت‌شوندهٔ دقیق) ایرانی یاسین پرواز کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/438807" target="_blank">📅 18:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438806">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-2K79x86WT_EPEBc-TPz-dG6k-RHjSiqGhiju2C7998ABvxh2FXtQIx9hh9Q5msRZR4yvLp_WwMxntOJ6i2e-Kv6jpl46A2Ve-EfVb7cRYwGZ5_lVeuPrd61scicBBoz2IqUO_Z6ciCfMmoAvKlBnp_3nDAq1bLegUfa9l8jC3YdCWsYOAccHUJ7bTA-1O0ydOtIQhnv52dGwVbDalZ-dKnrP3yZhGc6jaA-8WX7lYq3f7vIJc2KMb0zMzEiQVbyL32CE7SSjuoFqVHOz5Doj_TWGX_9b6fz-bN6z9Zx-umrVWnjLYf6QnreOS4hgpUpdPvlAtu2ehu12mVreyD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود رسمی پزشکیان به پروندهٔ باشگاه پرسپولیس
🔹
درپی نامهٔ باشگاه پرسپولیس به رئیس‌جمهور در روزهای گذشته مبنی‌بر درخواست‌هایی مانند سهمیهٔ آسیا و شرایط فوتبال کشور، پیگیری‌ها نشان می‌دهد که این نامه وارد فاز بررسی در نهاد ریاست‌جمهوری شده و جلساتی نیز در همین…</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/438806" target="_blank">📅 17:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438805">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBDgu5wdmqFHQc7ND4tSjYZnW9M_wpJz8OOskpOwi0SUT8FOjwSgLTKU48yHayqzvUiP13W1G9B1j4phmV3pt_NaKUqLM7IVq7OaDfRza12bc4ffprxvAMRJw9lFnRJR8SwNeqnzq9Hdrb1D94VLoUosh2kmOLkke1ClEIini8xTR1qJa9BuaQMov-QAvpcq71zS5ZTl8rAwt0XNuDEQmzNVHGwlYpX0LynjDSh1_cTQcYy0obQ1L6VEKK3729eVsH8ABKeCGTuQdsc5-JfdvGDwJzwBoyryKxK72Qzn3fiki55nC_wNG2YSHqHv2sBg5aopvswqgNFmq9PMhzeXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات موشکی حزب‌الله به زیرساخت‌های ارتش اسرائیل
🔹
رادیو ارتش اسرائیل ساعتی پیش اذعان کرد نیروهای مقاومت لبنان شهر «الصفد» واقع در شمال فلسطین اشغالی را هدف حملات راکتی خود قرار دادند.
🔹
حزب‌الله با انتشار بیانیه‌ای تأکید کرد که در این حمله، زیرساخت‌های ارتش رژیم صهیونیستی هدف قرار گرفته است.
🔹
حزب‌الله در یک حملهٔ دیگر،  ۱۰ موشک به سمت نظامیان صهیونیستی حاضر در شهرک «یحمر الشقیف» شلیک کرد.
🔹
نیروهای مقاومت لبنان همچنین محل تجمع نظامیان صهیونیست در شهرک  «بیت لیف» در جنوب لبنان را هدف حملات موشکی قرار داد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/438805" target="_blank">📅 17:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438804">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xkm0Y8_xi_pvI8V1JZPyUzOT7ep2MScI6NdAqTktt2Lp8ysYQ3RqEgB8_ALHPLGqw2Bb0OsygViSW3GDKzca-JO2QgQPKPeNJVfdCATQJiLiYn96r7WnF-f7Ru5JdUPjmfbqD92W4_w7q_BbqB6LeXz88FBP_9c1L_FRXhCKjudmTbMZdo59nlvrB1dkmDfeTp9fVe0sxwn7ZHnaJseVZa830xNArU_x-Vv8GLDiQySEQNQyqZbeK-L8PWaUhD58Xol2JjFWlMXeB_uWWrsR11js3vsMR9k-wpTZpgs_rhe1i7egAL4UFoabacaP-K70LZPDNVqqKO-CPTAICfbvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج انصراف هنرمندان از جشن ترامپ برای ۲۵۰ سالگی آمریکا
🔹
چندین خواننده و گروه موسیقی که قرار بود در فستیوال «نمایشگاه بزرگ ایالتی آمریکا» در واشنگتن دی‌سی به مناسبت دویست‌وپنجاهمین سالگرد استقلال آمریکا روی صحنه بروند، در روزهای اخیر از حضور در این رویداد انصراف داده‌اند؛ اقدامی که به بحث تازه‌ای درباره سیاسی شدن برنامه‌های ملی در دوران ریاست‌جمهوری ترامپ دامن زده است.
🔹
خواننده موسیقی کانتری مارتینا مک‌براید نیز در بیانیه‌ای در شبکه ایکس (توئیتر سابق) اعلام کرد که تصور می‌کرد برای حضور در یک برنامه غیرسیاسی دعوت شده است.
🔹
موج کناره‌گیری هنرمندان نشان می‌دهد که حتی مراسمی که قرار است نماد وحدت ملی باشد نیز در فضای به‌شدت قطبی‌شده سیاسی آمریکا از مناقشه و اختلاف مصون نمانده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/438804" target="_blank">📅 17:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438803">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91ce3ea462.mp4?token=rM5TQh9T4W8-gGdGxfc_-C1ccD8UxVlTyhk2Uu1QwAxaGjuXtROri5Hy4mWIuN86iGmU1xDQBP-MOIssxspnit_Xg8bYS20i8WJsfTHpBMLm4P1E1mgfcd9cLCDllwedxlGnhbbHfW_k3ldsZvU_G634Izu7Ty39SR_chb9NQ1mAyA7TE5fc9K5DqyLJcGj6UswSpzb82U0GOVHqbtbHOegL00HfCzZpsEUzeq528s90qFRuUswwMwFmEUSjuIfLsanlH7PJGq06xvClcRxefvT98AveQK1-C6odT3doh0PGPjdTcOtSlYxB8AiJARO-ielqoAu8BQmnr94dHwePc4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91ce3ea462.mp4?token=rM5TQh9T4W8-gGdGxfc_-C1ccD8UxVlTyhk2Uu1QwAxaGjuXtROri5Hy4mWIuN86iGmU1xDQBP-MOIssxspnit_Xg8bYS20i8WJsfTHpBMLm4P1E1mgfcd9cLCDllwedxlGnhbbHfW_k3ldsZvU_G634Izu7Ty39SR_chb9NQ1mAyA7TE5fc9K5DqyLJcGj6UswSpzb82U0GOVHqbtbHOegL00HfCzZpsEUzeq528s90qFRuUswwMwFmEUSjuIfLsanlH7PJGq06xvClcRxefvT98AveQK1-C6odT3doh0PGPjdTcOtSlYxB8AiJARO-ielqoAu8BQmnr94dHwePc4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل بانک رفاه کارگران در حاشیه نشست «راهکارهای تأمین مالی غیرنقدی»: زیرساخت‌های تأمین مالی غیرتسهیلاتی در بانک رفاه کارگران به‌طور کامل فراهم شده است
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/438803" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438802">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdrquBies-ndsP5oFNUfvY2I37YwurtTUNFDCmTEz2j9qgSiiPBt7TAPye4uE_USxt_mMq01owQpyBWIcmWrblIDHFs4oxlz7SUb5hy_xVurWnrXWXWpy3hE5A7WuE2XzqfVn7JeNhCzca8r8HcUZdTa_VRdLcTS9K_7JeAtr30JrGTPeQ_dATKk6-5wxHbn89jG6oK6ScLKv_kHCwJHV5JtRdt8UiL1guQtHOzDteQDUqvMdy95uHoox-Ck5J33nZNX7EX2bmxAlRgVS_s6EWpQyvJHb8HirrXq3tI_jVYh9tHw7HcXnLxrx_GOjhrvilFtsdDB-6-rxYYXwGw5Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همراهی و شرکت در پویش هنر برای زندگی
لازم نیست هنرمند باشید.
هرچی دلت می‌خواد بفرست:
نقاشی، دل‌نوشته، عکس… حتی یه خط ساده.
چون هنر راهی برای آروم شدن دل
و کم کردن اضطراب و
خستگی‌هاست.
آثارت رو به پویش هنر برای زندگی بفرست
تا با هم، با هنر،
از سختی‌های زندگی عبور کنیم
شما می‌توانید آثار خود را
اینجا
ارسال کنید</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/438802" target="_blank">📅 17:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438801">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/438801" target="_blank">📅 17:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438800">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1s3Nj0DM7xcYzV8y8td7im0s7n7hGuh51HpivMhH6naM54ey-mJmzgN_4vufN6pni6ckbLbGh63V531EolGZOGP1EqKu9WGwMcfdafeoxZNRO3rfDP3_DRetr_1r9SEpOprt0dMaRdx4_o6s_mNFlsDV3BqfpZsIuvNZiUuN3CGgZ3MURQKMANIUNZd54j9q_0enLDzf7e9xwWanrlCC_lUa5U2qHsD3q3BHWx5C1V8x619l4uZg09qPPcRSIwbM4-MZ2wynMi6YDpjz9Y69clwZSuJyXxmEHgMuE0XVenkL6u3QNS4bdfZPOI4FsjbTwYhD_dhgzUcR1KDQgHVhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
واکنش وزیر کشاورزی به بازار سیاه گندم
🔹
روال همیشگی نشان‌داده که کشاورزان مایل هستند گندم و محصولاتشان را به وزارت کشاورزی تحویل بدهند. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/438800" target="_blank">📅 16:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438799">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpbiUP6V6m0koLp28Cp96pUXRG0h3GmrsCkG_BPp5OFO7I3IpbOrACS42OmPkWjzd48Qxuv2291eSShWjg9swn_0sCiGHI0IhVVzhe8GKyK6eziDEDjQ3kmAGYrcdP2SSxvoEuBL_MzNJAcu1cLanXIxhtXFAHWh6Xq3favCb_hjmxXk2XuRtonCiZGRkUn2NDhNyMm0k0gRVC0TjWqouVyGJlsi7V2R48akRvrS-8E7mhA85qWzy8Tk3tqLs4qxtMN5dATiiqXN1rtFYPP2rPKcROvfJ3CIaald8X0xVQT1jq8OQAa4ZbekOZwBeGbarbwFPtpLW6xJYfj7BxVojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان از مشاهدۀ یک مین دریایی در غرب تنگۀ هرمز خبر داد
🔹
مرکز امنیت دریایی عمان: درپی مشاهده یک شیء شناور مشکوک به مین دریایی در غرب مسیر تردد ساحلی کشتی‌ها در تنگۀ هرمز و در آب‌های سرزمینی عمان، از تمامی دریانوردان، ماهیگیران و شناورها درخواست می‌شود با نهایت احتیاط در این منطقه تردد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/438799" target="_blank">📅 16:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438797">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMBLQxxSbzQPkaQeIBc53QVcMyntK4gZvUXCTyi-4NHyVZEvybY8tKpZU8zfX-zhjoupECmXZu5HdGc7EmNEbaZVut_MyvXPb4_rB6Agzr3Y-u9h0L57C_HT_9Ldg9FhFk--I-0JYqz6ads0y0ZjfqJF6hL-hw_v7cjSkFQxC9WUEqMklNrFJM_GV6UrUt89nFIW-nGwAVSCuGCLW2Ke1Qt6TtYPq60czcyR_nCeEZYZfj48i3vWkwcOCq7xTTvu0flnwNfEC6vDF2tdTBeR4a8HMW5s1hdYeR72yL8wIb1G-3BWTdMRLE64h_ghTQuKyH0QGcBc9XlMr-Ww3N22Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا دانشجوی دانشگاه شریف بازداشت شد؟
🔹
بررسی خط خبری رسانه‌های معاند طی چند روز گذشته بیانگر برجسته‌سازی یک پرسش از سوی آنها مبنی بر این است که چرا یک دانشجوی دانشگاه شریف باید متهم به همکاری با منافقین باشد؟
🔹
پاسخ به این پرسش با بررسی سوابق خانوادگی علی یونسی…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/438797" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438796">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ff6a2b530.mp4?token=d5j95dBj8nnliUihVWsl3lkhMpz4wyVsZEyBcugShTHMIIZnn4pMxZGdp63yx7HA1RjMbfrtUOgEbDOFfD_TdheZ6JSPmKQrUQ3xRviHXzAbruB5oSIpOJhvUSi_YRP647absTAg1kdRw8jHUMim3r3W3GsUohlkfRN-b3RrQe2ES7aIgC7ZOQHBHy_puOl4ROP3y0tOqDnMikyX91aqtGMRHuq5fqURbpW2WluLXhizh2FDWvGAfpJK3q1fZFO0BlfoDPNphntxXeWvYHQIuUGRFATpnma4pUQ87bY_kUiaqt06ddU1JicFi1QmnOP1mLf0fuiscMYco1GnYMVA8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ff6a2b530.mp4?token=d5j95dBj8nnliUihVWsl3lkhMpz4wyVsZEyBcugShTHMIIZnn4pMxZGdp63yx7HA1RjMbfrtUOgEbDOFfD_TdheZ6JSPmKQrUQ3xRviHXzAbruB5oSIpOJhvUSi_YRP647absTAg1kdRw8jHUMim3r3W3GsUohlkfRN-b3RrQe2ES7aIgC7ZOQHBHy_puOl4ROP3y0tOqDnMikyX91aqtGMRHuq5fqURbpW2WluLXhizh2FDWvGAfpJK3q1fZFO0BlfoDPNphntxXeWvYHQIuUGRFATpnma4pUQ87bY_kUiaqt06ddU1JicFi1QmnOP1mLf0fuiscMYco1GnYMVA8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیت‌الله ‌محامی: توجه رهبر انقلاب به سیستان‌‌و‌بلوچستان استثنایی‌ست
🔹
نمایندۀ ولی‌فقیه در سیستان‌‌و‌بلوچستان: صدور چندین پیام و اعزام هیئت ویژه از سوی رهبر معظم انقلاب به این استان، در سطح کشور بی‌سابقه بوده است.
🔹
همان‌گونه که وعده داده شده بود، هندسهٔ جدید…</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/438796" target="_blank">📅 16:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438794">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هلاکت ۲ تروریست در چالدران
🔹
فرمانده مرزبانی آذربایجان‌غربی: حمله عناصر گروهک‌های معاند به یکی از یگان‌های مرزی چالدران ناکام ماند؛ در این درگیری مسلحانه،۲ تروریست کشته و تعدادی دیگر پس از زخمی شدن به آن سوی مرز متواری شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/438794" target="_blank">📅 16:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438793">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4132519ad3.mp4?token=pl-7cYoAuPwMUT-XfgWLixQFJ_L_R93rFSNmBXubhka7IIZWicbXZDKx92PJJw0lhkBu7TEOVV230cbolFyxwco7CkH4wMZK2BQu0XRGBva1BjyQcIAL77umCznbe7qvUdkUIkebxIfNpsR0p0uFi68Lui2_6D84FYUpum7xigWvVqjYWq4LpURSpdKbu72UdE9M4ULQwtwEUuIR1t5aDaRTuMyPT_HrSPkxUY0mJWqqRRnrfKclQ5NaiqwvTmiPtKCZ5YAf3Av6tXVT8QAqc1SQaCLVXJEN-N5hXJD2fSVG9qvJcAGXpc4y4WaKWP7QZ6xjERjITobkWD-8Qx-m1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4132519ad3.mp4?token=pl-7cYoAuPwMUT-XfgWLixQFJ_L_R93rFSNmBXubhka7IIZWicbXZDKx92PJJw0lhkBu7TEOVV230cbolFyxwco7CkH4wMZK2BQu0XRGBva1BjyQcIAL77umCznbe7qvUdkUIkebxIfNpsR0p0uFi68Lui2_6D84FYUpum7xigWvVqjYWq4LpURSpdKbu72UdE9M4ULQwtwEUuIR1t5aDaRTuMyPT_HrSPkxUY0mJWqqRRnrfKclQ5NaiqwvTmiPtKCZ5YAf3Av6tXVT8QAqc1SQaCLVXJEN-N5hXJD2fSVG9qvJcAGXpc4y4WaKWP7QZ6xjERjITobkWD-8Qx-m1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: مردم می‌توانند ماینرهای غیرمجاز را معرفی کنند
🔹
ماموران وزارت نیرو بدون اینکه هویت آنها مشخص شود، به گزارش‌ها رسیدگی می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/438793" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438792">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738784b50.mp4?token=k3sTh_CrxStqVA23ejff98wDV-xu14a9CwThGGxOChuZ85ERqv9khyDrfkM0aM_UIg0J7_mrtutWM3g4m8-j4bYasuffzOlALxKtzGHxkKIfzRY4btShXfsvlvJ57S4FSYz_NZPE7kzRNNWlQO0gf1P7UyzOrec3DqiTkWtJF3WeoJTlaO2VltGxyw4I089iglpr4URx_7x6NqSyk5AIT6ZvKFo83xIEcqN4Mvn3n-vVl-XcL3gF4IKHe30ROIGZgyasSQ8J5GRTEWhib-YYkuAoMptm8ExLSL33KDfZErzLgf9InYjpNKbhGObXl1akpBeAQBVHe9Cu8WRjl4OKQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738784b50.mp4?token=k3sTh_CrxStqVA23ejff98wDV-xu14a9CwThGGxOChuZ85ERqv9khyDrfkM0aM_UIg0J7_mrtutWM3g4m8-j4bYasuffzOlALxKtzGHxkKIfzRY4btShXfsvlvJ57S4FSYz_NZPE7kzRNNWlQO0gf1P7UyzOrec3DqiTkWtJF3WeoJTlaO2VltGxyw4I089iglpr4URx_7x6NqSyk5AIT6ZvKFo83xIEcqN4Mvn3n-vVl-XcL3gF4IKHe30ROIGZgyasSQ8J5GRTEWhib-YYkuAoMptm8ExLSL33KDfZErzLgf9InYjpNKbhGObXl1akpBeAQBVHe9Cu8WRjl4OKQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: مردم می‌توانند ماینرهای غیرمجاز را معرفی کنند
🔹
ماموران وزارت نیرو بدون اینکه هویت آنها مشخص شود، به گزارش‌ها رسیدگی می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/438792" target="_blank">📅 15:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438791">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06fbcfb22.mp4?token=TZEHAPP3vjLNYpgWL19_IU0LbNYQ0nHIquYsSM0vh9sfEAJWcZ_L8mCJYlxhTQxg9g3Yn-FLcMh2cBSVwQWrRPA0G4yRpDbyJMvqXY7MeDIewbBL4KA39qPxemmzfPKGQe19woN3wZiSOz6a5UILhBFIdqn8xR6Dzc15-4h0ILhWreR71Mr_dGPe5M6TLP5S-oL5CN9pGyKp35JDM2kG519G5XkoJBNgla2zVEgsSE0fOaNrp9uJpcMq7uuSAuomisCmon6mwgdK9lWSIQWUkvQz9qHKeMWrVw7zeFXDCPlUFz96OOtHoKxRCwKY5mC0wd4rFXJm9PboIzL9RNpYHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06fbcfb22.mp4?token=TZEHAPP3vjLNYpgWL19_IU0LbNYQ0nHIquYsSM0vh9sfEAJWcZ_L8mCJYlxhTQxg9g3Yn-FLcMh2cBSVwQWrRPA0G4yRpDbyJMvqXY7MeDIewbBL4KA39qPxemmzfPKGQe19woN3wZiSOz6a5UILhBFIdqn8xR6Dzc15-4h0ILhWreR71Mr_dGPe5M6TLP5S-oL5CN9pGyKp35JDM2kG519G5XkoJBNgla2zVEgsSE0fOaNrp9uJpcMq7uuSAuomisCmon6mwgdK9lWSIQWUkvQz9qHKeMWrVw7zeFXDCPlUFz96OOtHoKxRCwKY5mC0wd4rFXJm9PboIzL9RNpYHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شبکه ۱۲ رژیم صهیونیستی از اصابت پهپاد در نزدیکی شهرک المطله در شمال فلسطین اشغالی خبر داد
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/438791" target="_blank">📅 15:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438783">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ5OhnRdvZccU7oPZqt70waa3-0Dp6Us3vUApSRvFjJZdHbwim4yNGQfUWD-05nsKSU6nMP1h6sg5Ei-fp-5fdLqVo__CoW9I_F55MlEwbIElK0x8V7yt_MZDJajGsWkCSkb1vf6FkYpq2hWhZsPqcPoRcamiXsPAL6ZlPHmS3_ZKDCZCbWrBPh9h49VLDno7GW_w46R0K0pohL5NBIe1CxABE1pPQjj49xG22Jyuc0qHtGMFPbkrdz4j0AK1nxlzVDCrAmP4UVEduh-ZkSwCYxDzh13cFcCPodVYTfyRqclNXKIOl54ldyfHmJyALOaAlKkzz8VR0bWH-xg9jeJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسب ۲ مدال آسیایی در ۲۴ ساعت توسط دوندهٔ ایران
🔹
هانیه شه‌پری ملی‌پوش دوومیدانی زنان که روز گذشته در مسابقات دوومیدانی قهرمانی جوانان آسیا در ۳ هزار متر با مانع نقره گرفته بود، امروز نیز در ۳ هزار متر بدون مانع نایب‌قهرمان شد.
🔹
شه‌پری در این رقابت رکورد ملی ۳۰۰۰ متر جوانان و بزرگسالان ایران را هم شکست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/438783" target="_blank">📅 15:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438782">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2adbe067b.mp4?token=tE5fDb8FyLp16XyiqosMCF6wTCuX1eoS_Turlj7lFsQL9bb2U9wQTJO3rTEa6-Tul_8JsBoGwG7jleLsxf30m5HXy_UmpFoX78I8N26GwWCsJWGygONGzC3LG3DPeHO07CJPK1Qt1XST0Ac2FDPTS9nWZHROCkF0s-5sAxHMUR2i10zSoSeauVDLCVQMBdVqOax31aEtYKD2h_W5NPFZj8cRBq5xFc-HB-x7zu8E5vQf5AfJvgqBApI-m1WnBOSDcdRCtII_aGqTqsIZIwKwx1o3FHKsXne8A6aKQYVuElb9gH2gxUDLlBDJjbu3LarqqWwmPQJjJF8WPB7Y3XIzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2adbe067b.mp4?token=tE5fDb8FyLp16XyiqosMCF6wTCuX1eoS_Turlj7lFsQL9bb2U9wQTJO3rTEa6-Tul_8JsBoGwG7jleLsxf30m5HXy_UmpFoX78I8N26GwWCsJWGygONGzC3LG3DPeHO07CJPK1Qt1XST0Ac2FDPTS9nWZHROCkF0s-5sAxHMUR2i10zSoSeauVDLCVQMBdVqOax31aEtYKD2h_W5NPFZj8cRBq5xFc-HB-x7zu8E5vQf5AfJvgqBApI-m1WnBOSDcdRCtII_aGqTqsIZIwKwx1o3FHKsXne8A6aKQYVuElb9gH2gxUDLlBDJjbu3LarqqWwmPQJjJF8WPB7Y3XIzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلاکت ۲ عامل اصلی آشوب‌های دی‌ماه دره‌دراز کرمانشاه
🔹
۲ نفر از عناصر اصلی آشوب‌های دی‌ماه سال گذشته در منطقهٔ دره‌دراز کرمانشاه به نام‌های مجتبی ویسی و میثم ویسی، روز گذشته در درگیری با نیروهای حافظ امنیت به هلاکت رسیدند.
🔹
این ۲ نفر از عوامل اصلی اقدامات…</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/438782" target="_blank">📅 15:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438781">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
🔹
سپاه هرمزگان: عملیات خنثی‌سازی مهمات عمل‌نکردهٔ دشمن در بندرعباس از فردا به‌مدت ۳ روز آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/438781" target="_blank">📅 15:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438780">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o84ozzuhr61Eh2hJ5XBAGGflTnF76dYuDdzyTzdMk6V8Mvzqj8v0Arngc5z6hjUOfUvc3zYJ46kH5ewUuGnip2uckgA-oea3cXZaddqPsdhSMQQJk2HixqNpkY2RLFHQz1AESKXbnp1fHpwGcPGwLloHen6TX81OPuB2lE2smsagaGI9iQAhhfMqwUESUR95omlU5cgYQ_72ORzRD_tt-XAecvRfuBn6bGoGXw6IjG9j1PoT4yWStOnW3CSm0689jWYV4R0FLr99OR61CO3cLAQY80zed--sFR-hBae7TWM2o5vDc0z2AVq40JpzgTpuqQgrshP7p0k1zGkxhJNQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در پیامی قهرمانی تیم پسران کشتی فرنگی نوجوانان در آسیا و تیم بانوان در مسابقات والیبال آسیای مرکزی را تبریک گفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/438780" target="_blank">📅 15:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438779">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5144346269.mp4?token=HK-1qWwQ8Q0CgTqge6EOAPEYqPS1lGaUvN7xGhELQplZaGMDjPqgmtPb8qCyHbwehEgvOU3nYyaKV9Qzkh1A40OddKuTXs22utGm7WIo7klYoys1GbDw3Kmayrl6Vfiw2hl2YlsoCshh9ik0lnyQmyVm1iDUfRxBuVHYob58lyoR3E2eKSxDB4F_GIqii3eHwhBxwH4XU4cHut67kIqw11tcILYEq73hGdLuUgKYRj38kCRQ_fGKjPvogiYipfQDVoSZN8vUsyrnJ8DkDEWR30oFgmWs5QglPgUDQ_rsDo7pqM5GEYE7oe-825Dtr9EZwbfJ7wHFcJDcBsFDbqKllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5144346269.mp4?token=HK-1qWwQ8Q0CgTqge6EOAPEYqPS1lGaUvN7xGhELQplZaGMDjPqgmtPb8qCyHbwehEgvOU3nYyaKV9Qzkh1A40OddKuTXs22utGm7WIo7klYoys1GbDw3Kmayrl6Vfiw2hl2YlsoCshh9ik0lnyQmyVm1iDUfRxBuVHYob58lyoR3E2eKSxDB4F_GIqii3eHwhBxwH4XU4cHut67kIqw11tcILYEq73hGdLuUgKYRj38kCRQ_fGKjPvogiYipfQDVoSZN8vUsyrnJ8DkDEWR30oFgmWs5QglPgUDQ_rsDo7pqM5GEYE7oe-825Dtr9EZwbfJ7wHFcJDcBsFDbqKllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از فروش برنج خارجی در کیسه‌های ایرانی تا فروش برنج‌های معمولی در کیسه‌های برنج مرغوب
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/438779" target="_blank">📅 14:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438778">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eff7c2ccd.mp4?token=OgxmX_GdLa3hg4pRuujiR_YNdQXO4ht3SshR_J6sxlE0-TxuMZPSoa6pERLZqVhe2a_HMcQ1Eki8VM5uD6pQO_MUmd-R-44rr8AkTGPzAeJxnaO-D8w0SCiIdr5tgOtswFmY7xs6vKgzHkFwirPD87nwbArB4K3rQ5hOlxPkLu4Ro3AccEVN_CxqFsZiDBt9fx8H1z3EV4iE6XeDe4bzlWWbDAB3DmaKcwxsAeXtyIelONOSjMFWmV5mapgQnYyiDTDSBfT62zDpZ8iElq8l8B8uACBpubB8e3ekvJb9NzUyDilYfKHpAAG5mrkDa1ZdhEf9HO0Jz2qExGuO9y9v0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eff7c2ccd.mp4?token=OgxmX_GdLa3hg4pRuujiR_YNdQXO4ht3SshR_J6sxlE0-TxuMZPSoa6pERLZqVhe2a_HMcQ1Eki8VM5uD6pQO_MUmd-R-44rr8AkTGPzAeJxnaO-D8w0SCiIdr5tgOtswFmY7xs6vKgzHkFwirPD87nwbArB4K3rQ5hOlxPkLu4Ro3AccEVN_CxqFsZiDBt9fx8H1z3EV4iE6XeDe4bzlWWbDAB3DmaKcwxsAeXtyIelONOSjMFWmV5mapgQnYyiDTDSBfT62zDpZ8iElq8l8B8uACBpubB8e3ekvJb9NzUyDilYfKHpAAG5mrkDa1ZdhEf9HO0Jz2qExGuO9y9v0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وام ودیعهٔ مسکن از اجاره‌بها جاماند
🔹
با وجود افزایش چشم‌گیر اجاره‌بها در کشور از ۵۰ تا ۷۰ درصد، دولت سقف وام ودیعهٔ مسکن را حدود ۳۳ درصد افزایش داده و خبر می‌رسد که سقف تسهیلات فعلاً تغییری نمی‌یابد.
🔹
امسال سقف وام ودیعه‌‌ مسکن در تهران ۳۶۵ میلیون، مراکز…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/438778" target="_blank">📅 14:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438777">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g38snRLO5ENNz1CXoxdD-snM-0h4qa6iLIfCAmTU5DTnXoEqS506tYfivN3U-NBNIYPCuYWpr8YexCdoTyT4BnJ_YYxlFU4eRNxXcPqNExSECG6fzF8-CLUQwuKxWl0AfkQ0j1z7I52BiehPO8TPm-UWcd0Mx4BeKmBqMGkTsyH22VCEhvEyhBhivFMDljRtiGph2N6zxUmflTseidOqp0RpsJf6yduGlfywQrvdRBefphADC5VGTDF3wqjk5J3vPhmT09ctvz2wBm9kFRaH-gY1aEg3-lchFzia6RIJ1GIBM-OBEu3MX254WA6cZwYLQ4J9KfVXqjQr4PO5hFCGpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
حمایت از دانش‌بنیان‌ها در صدر برنامه‌های بانک صادرات ایران / اهمیت سرمایه‌گذاری هدفمند و بلندمدت در پروژه‌های زیست محیطی
🔹
در جریان بازدید قربان اسکندری، سرپرست بانک صادرات ایران از شرکت دانش‌بنیان ایران‌دلکو، بر ضرورت سرمایه‌گذاری بلندمدت و هدفمند در پروژه‌های زیست‌محیطی و فناوری‌های سبز با هدف ارتقای کیفیت زندگی شهروندان و توسعه پایدار تأکید شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/438777" target="_blank">📅 14:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438771">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Py0SE3RVIAJAeLOdQRa8vUmbIyESgEfQWPVCovEGfE979qMw-C4CGrz_RIsTlwineQVlyt6UH9wW8FOYHFOrU17wSL13XhB2yJ5HPIimkCRdYoNNNK6NREvZ3c3bXZmXw1jzkhFGycczoYUTarVrkeSzvAWmn3FyH-zlrZjg0Mq0cLdEblFgZZMHhefi2749PvhEZNtlx1zCYAuOrfXEFnV1Ih6EydR4PEeFLrmUcHRovrAbZ0yt5vrxt2zKth-Vlm4IAnxegv_y9bqpNacLxH45nA1BZ1AahrrifJ972MBQVk6P0mddNfl8z--JIG6ELTa4VU0jY45SmpRKTn6NPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ND2K9hQxFzytj8BOAVTMb9zkB2H8gKBP7RQg3Gwi6t8gZl5twsWzphHgGg4QwmhTkCev9T6IKMv3LOJJebTYi3X6QY0s7YPpEOmuvOy3ffn2RJtGk2Tc0yBbxeahajJlmk12w2R0PbZWAkix4NoiMR70yVwb9oGfaPsI2FmPcFL0ZiGFaO5QyHtAjUE3go16rqVH5AI7a5zYyi_BCp1iP6hxlZEEhjsJBCGoaVWPQcEuWj9SQS6I0AcXsySWUTju7VJetKdQ-b3B195h7e-dhAiQepUp1UEbXUXCls9e5jMvPsLg5Fk350DZdUHMiBwojZWBWgaDXflR_fHXIYgVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhmiNA3AbPtiOxgVETyJNyMLj-s6cB-6PKB3LOrOYxzRIJtl7qiCesZ6hKfCZ7a6r2iwKje3aw75LbIFVpovX8ygCi07Vsp-KVF1-bLXT5KAFFQYxNzYuFoibLD40VyfXDmuFd9uSvH5OBwtEYeSD-xxf5Aisa-TF7fRsYvX3x1e2StNR2Psb8fB4opvX6dTAknt0InoHTjCC2GqORMceH9jpU7tFW-cWOo2D7jzQGFM_DOaidHYXExGQCcsHA56p6kKqIUNCsLCEj66LKuC_3_uPHmdrr3fl7B05sNk4r0lLxXpjdFfsjM70THCIWTB8DHrk6BTCfJDaT_vRH8nkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ug4kZ9FjEhP1R4WUOcqdEXvFBvjMDING_bGJc3XMa4HDNEU1eB0fTW2LEUY8L5qPN4qkC2vgamOT0TJz8ffBpzzcsjUAVNYMNdnNPx9HTVOJcbei_V1GxTHIlvx7DJGOAGmSIVT6mMMs14LKNgcHC3DzYnsGOiCw929wDFF8HeWcXCktsKh_mOTmgWRZw7cOQ56bOG20KINPr076N9YTpmW4BijSiH7Wt4En_2AA3eWccNp8SeDamVm3xm_vhZntt6LfuAcRy4vGikfQEUapfKg5DsC_uqmACtE62IzQ-IKz-KNQYzOSp2Mq5ugNBYevwnl7AGh0Hg_1Ao4O5EgFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4IkD45MVNx_TEl92H9BM9WXmI7TJ3QPxV0yeyYDf2N3iGNh_1x_ZuuYoF62ltbJzaQm7qPIOBQd820Vofb2-bGF5xjXNjo4yklyc2XqDP-RcSaYmg5Fy1c9blrXhBj5F1gmUvt3oXhmg14oLO7z2aPcqhNsgljZ07ygDwkKTu4Yefg9e9Mg1Yg7CzUMkL5jkXsikt1R2fU3LTVyJT8DCLN_uOnAdLAFviNr6u5OsVfAGDVKUOJJimvDpzRMSBgMeraq7FFAwaSH_taKPy_LSI7Z9kcumE45il4YPWBcRfGiNympz3w1x09iUBMrp5pGEUgldE3ao9LEqLrQxlOQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKvzkwT25gr0euUja-lZzB5gLDoiT3SWGCvxznQ38cHzzSrrm7jt6LPXfqN69VzRMeV-Ci9YtiXAq1yLiAUW4pXM9IeKQbpqWT0zvXLGqGAXfTtPKq9clZ-TWwOs4nzH2saUL4jtqNj1fKuPLxEy_t3mHbMJk6derAA3tiGgwr2ZxCZAn25SMZxrmSLyNwtVltLSnGBk6uxHJi_mYAH2PWMNfppXL0sr7YYJn0mNzoHh2eT4o2OsFlMViyIlVYDoDf97lZS3voNG2Us8QIs51OvsG_wUGf-DWiapfrzgI45Zemnhv6NBbiNe857s-TLrsjsHs231m_ySOwvuspsNBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#گزارش_تصویری
🔰
بازدید مدیرعامل شرکت ملی مس از مجتمع مس سرچشمه
🔻
دکتر سیدمصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، امروز جمعه هشتم خردادماه با حضور در مجتمع‌ مس سرچشمه، آخرین وضعیت تولید، پروژه‌های توسعه‌ای و طرح‌های زیرساختی این مجتمع را از نزدیک بررسی کرد.
لینک خبر در مس‌پرس؛
mespress.ir/x6QT
◀️
شرکت ملی صنایع مس ایران را در شبکه‌های اجتماعی دنبال کنید:
👇
|
بله
|
اینستاگرام
|
ایتا
|
سروش
@mespress_ir</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/438771" target="_blank">📅 14:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438770">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/438770" target="_blank">📅 14:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438769">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">توقیف
اموال ۷۴ خائن به وطن ساکن خارج از کشور در گلستان
🔹
دادگستری گلستان: اموال ۷۴ نفر از خائنین به وطن و افراد تاثیرگذار در شبکهٔ همکاران دشمن که ساکن خارج از کشور هستند به نفع مردم توقیف شد؛ اموال توقیف‌شدهٔ این افراد شامل حساب‌های بانکی، خودرو و املاک ثبتی است.
🔹
همهٔ دارایی‌ها و حساب‌های این افراد توقیف شده و هرگونه نقل‌وانتقال مالی برای آن‌ها ممنوع و پروندهٔ آن‌ها در دادسرای مرکز استان درحال رسیدگی است.
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/438769" target="_blank">📅 14:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438768">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc124551.mp4?token=vfg-LO-liRk-S8VG_me9bQsDiXokMWKxEdRbwknQEsa0NjwcAfJL72ntbLsr0xz2D3fus3vn--qWoztziNdZ5ls2mK3hGgGGevTjCfKh2YprmkQN03t2LogFJUYvkNX6IWNICG_cc48wgkEVMYqiWEzLsk37N8qfsX29DG-wsK-T3Pai2jHR7v-4jAozJD0Qh_6m6YHLezPMXvLJTGsH4OXieiJcQyeZroDSkyzgY6TAJTBgOzU27MSUW7vDy2hYwFi2t34Mks3Geo36g5zMWsfnPLNsk21D_UBYmj-nGs3OVng1D7S5LC4ioM7CCMX2ukHxHwTiSRRoWX0OfDXYeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc124551.mp4?token=vfg-LO-liRk-S8VG_me9bQsDiXokMWKxEdRbwknQEsa0NjwcAfJL72ntbLsr0xz2D3fus3vn--qWoztziNdZ5ls2mK3hGgGGevTjCfKh2YprmkQN03t2LogFJUYvkNX6IWNICG_cc48wgkEVMYqiWEzLsk37N8qfsX29DG-wsK-T3Pai2jHR7v-4jAozJD0Qh_6m6YHLezPMXvLJTGsH4OXieiJcQyeZroDSkyzgY6TAJTBgOzU27MSUW7vDy2hYwFi2t34Mks3Geo36g5zMWsfnPLNsk21D_UBYmj-nGs3OVng1D7S5LC4ioM7CCMX2ukHxHwTiSRRoWX0OfDXYeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در شبانه‌روز گذشته ۲۰ کشتی با هماهنگی نیروی دریایی سپاه از تنگۀ هرمز  عبور کردند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/438768" target="_blank">📅 14:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/157ceae8cb.mp4?token=ncU_dNZxLSt_KmVx2CmW6VzG8rnB1BDXcZ7tFahQA6sVIAGMcFRRaWdI0-0N9vQ-nYnAcLZXuPuS7EurAxa2I4HdJqbGspV9xgKP4-9QoO9fGf-ogbc615gWT7SdWkKdqoeU-_K5QX40Yp2JJUDD8ZoRk8PbcSt1mCE7-r9EwIh1l-Mzke4FM35SWQ5lF1hg6xur5g9P8gor1AGppBJLAXF7dpyZwfsccfYHluPK6UBuUT4aDQC7hfhemRyet8SzvsvOu-QVqh5ojpOPZap9ZT9i09Bv9CHKPNZdVYeFrng2WoIh1lhfSPfqJP_JchTBWFtLklf_X8Y3bxeb5MBSlYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/157ceae8cb.mp4?token=ncU_dNZxLSt_KmVx2CmW6VzG8rnB1BDXcZ7tFahQA6sVIAGMcFRRaWdI0-0N9vQ-nYnAcLZXuPuS7EurAxa2I4HdJqbGspV9xgKP4-9QoO9fGf-ogbc615gWT7SdWkKdqoeU-_K5QX40Yp2JJUDD8ZoRk8PbcSt1mCE7-r9EwIh1l-Mzke4FM35SWQ5lF1hg6xur5g9P8gor1AGppBJLAXF7dpyZwfsccfYHluPK6UBuUT4aDQC7hfhemRyet8SzvsvOu-QVqh5ojpOPZap9ZT9i09Bv9CHKPNZdVYeFrng2WoIh1lhfSPfqJP_JchTBWFtLklf_X8Y3bxeb5MBSlYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرکاواهای اسرائیلی هنوز هم از حملات ابابیل حزب‌الله امان ندارند
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/438767" target="_blank">📅 14:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438766">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امحای مهمات عمل‌نکرده در سنندج به‌مدت یک هفته
🔹
استانداری کردستان: امحای مهمات عمل‌نکرده از فردا به‌مدت یک هفته در سنندج آغاز خواهد شد؛ مردم نگران صدای ناشی از انفجارهای این عملیات‌ها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/438766" target="_blank">📅 14:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438763">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مجلس فردا میزبان‌ وزیر راه خواهد بود
🔹
سخنگوی هیئت‌رئیسۀ مجلس: یکشنبه نشست وبیناری مجلس با حضور وزیر راه و شهرسازی با محوریت بازسازی اماکن خسارت‌دیدۀ ناشی از جنگ تحمیلی سوم برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438763" target="_blank">📅 13:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438762">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxAxmgB5tKvVZnD_1qO9kwpSVX_CJaqO-H3JkRmf5F0wuopd82Vx-an1mdEy4rR22nB4FanjGWWglJ79BZLha1v949nvF3UD3AbZRp4-raoZrLF51r-7MNsnxD-_RyMZ0C5Z17VuJ9v5uJueA-veSL0xF8sCNfc6YECCMqIKaoGtQB37II186OdDsO8hvnh6xPQIB2TbsMNU-BCysWI8d-33brlQw5uD9UQy3Ouhrot0wdovT2cxM5hHtilPmjAoH4cD6N1Nzcz1Qda1mG8YrfIfwnkvgoOwlvSKc5Gazz74Yi7alMPTuj5hTdV5_ufTbmDMiM4aDCwlN8_uI5VAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف ۲۳ تن مرغ منجمد تاریخ‌گذشته در اهواز
🔹
دامپزشکی اهواز: در بازرسی از یک سردخانهٔ نگهداری فرآورده‌های خام دامی ۲۳ تن مرغ منجمد تاریخ‌گذشته کشف و از چرخهٔ توزیع خارج شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/438762" target="_blank">📅 13:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438761">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyZd4ibbMJTzhjQMFEfoqMbrJADQAUPYbHWLSu7Nv9G5_NrSzsiDmUWezViDoaEiSI6fj7eAARnXbZYlJrt9PMlgWwPLsB0Ujmmt9_BuCHyavFNY8vJrv7afRav24FMnmtmZh_OInZEhepQzpZcsXVryv6tfBggsS0R071powqOBU_jNNdWQn1Q0wRc1OkVlyeZoLU8_--L6K1nMjybTvYSxM5WiCJtl9nPTtyaU9Cm72-CwuGzxDnHfOhwkx2v2tpVaN18vm55eEN9-kt331pSGXAh2d_7o-1IHYuLUatGFTPwwgclsO_gWPhrv_7ztVvJteUjJRfzGrt6rvXIhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول‌هفتهٔ تماماً سبز بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۰ هزار واحدی به ۴ میلیون و ۱۵۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/438761" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438760">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8stocrsLTS8ByM_PB1q8hzlfI2L3zj7DcRn7U-GKfgAsFkrbp80dqfqiFExl7Pe3Yu8xlYUfnHvlFZANQ8Jv3S4UKMdYon6xLViaTBZUQItjxq-kx2nTKPkQdpnxfWklrEN9sJsSLQAfHmiKpfBn7-T5X_7kp2v3klcz546y-IMBfzg6ka5tSlqf7FkQ28hPf-fOaGe2Hm0gAjxbYHGTnGyUmYEH77CT4OTJR37nIG_alVnKZngdqJEFGx3kQTrHZfiDaZxHR_ooQLXQPvSX3YwfEpUx46XTD0Mc11dgsiiRHXkgHD8hnIkKGXIb7KEoLoYjuRfDJIj6oJcIi4Z1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با دور زدن آمریکا سوژۀ اول جام‌جهانی شد
🔹
بعد از اعلام مهدی تاج برای انتقال کمپ تیم‌ملی ایران از آمریکا به مکزیک با موافقت فیفا، این خبر امروز در رسانه‌های معتبر جهان به سوژۀ اول جام‌جهانی و بمب خبری تبدیل شد.
🔸
خبرگزاری AP این اقدام ایران را دور زدن…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/438760" target="_blank">📅 12:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438759">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVZSrvlc_sUSjFxAk5j1ayR-5AcajwCflQ3Nad2ahB-_3MsrSQfP0vSxV7GXaK4q7fucW0lZ7bX8Wog4h65KL-Kw9k0GhN24CMmWYtaO680N4GQaDTgxN0TSbdrGfrgbtKYfr737W_ExattSM2IOMLy3gj8Z0H01gb_H7jyT6TlV9FRG2XSAQ-sZSEp3qofXlAy1wbquxByPaUZxC8F7BROiFKHNkBcUxE_vpIxCr6VwOwmg1FDwBCuwf9u5kq3i4aUu5GxzdqSZO8MvyrYWHCDj4zhx1R040pgdfCU4rTgaR_wFp37R21f9jj7gTUUQLiCGH00uXHIq2Ogv8fWi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپادها دوباره فرودگاه مونیخ را تعطیل کردند
🔹
برای دومین بار در کمتر از ۲۴ ساعت، دیشب مشاهده پهپادهای ناشناس موجب تعطیلی چند ساعتۀ فرودگاه مونیخ شد.
🔹
پلیس آلمان تأیید کرده هم‌زمان ۲ پهپاد در نزدیکی باندهای شمالی و جنوبی دیده شده‌اند و به سرعت محل را ترک کرده‌اند.…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438759" target="_blank">📅 12:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438758">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmcQdenirc8V2ll7yFb4Eje8wRZ_1h-4ZTyrjxeRWaXQdmLfsaAJkLS04g3zwiqLHPx-BkKfd-dlzEcxvDwhOw4rqbdFs80QG_D1q82toJqep_zRQPwjPZPVbR6-e3qxQf2Bhaht1X_PGfYiIbQCQR7m6sShrGuXU2FVKrYlxdFkO6agDqhgEZ2UVl0pQRdan-PYokajMPcF15rkkbMMZqPJLBET0K1QWFAjPf-MyOKu8OnCaifbxUx-8gXCxLAhwRU8YKVRrEugKmWzLGfVqjmGHGTlE7mjZMN6w5EUFXh0NZBMoYIele5ufq8VxfFTEs8FUR8pwq8AUuOi4HPcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۷۳۱ تن آهن‌آلات احتکارشده در یزد
🔹
فرمانده انتظامی یزد: درپی بازرسی از یک انبار در حاشیهٔ شهر، ۷۳۱ تن آهن‌آلات احتکاری به‌ارزش ۸۰ میلیارد تومان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438758" target="_blank">📅 12:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438757">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات عمل‌نکرده در بندرلنگه
🔹
معاون امنیتی فرمانداری بندرلنگه: به‌دلیل خنثی‌سازی مهمات عمل‌نکردهٔ دشمن تا ساعت ۱۷ امروز، احتمال شنیدن صدای انفجار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438757" target="_blank">📅 12:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438756">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeMuY-xjOWtkrvH4MNgge8gn5wMjj9WuEWPIPeDin1BvLYLfg9a1zRGVARoiMKTH8aqLATN5qrrRVpylITnCc0tXOaMjzDeAuZKoBHmw0Vj1g_OCz_pSxI_cwV1gAdn-hrOiE_E8aLnQatM2ANcVGrNkSURElTxeDEwPr2IaKQIQimd9FtAzWki38I4cuRUu7gs15xChgF0b7YuyKTaOuvoF0ewh5qs5G-tRqQpLqI4_2cgJD7eKhKkuLhWHv6M-M_bseCmDlxKzaFVoJtEl4ReryMUENJr7iuv5WbqEjl0ms2hZjWahVO87fvCSLHhgbfGL1EbCLa_FgEI2wJzscQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محسن رضایی: رئیس‌جمهور آمریکا برای بار سوم درحال خیانت به دیپلماسی است
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438756" target="_blank">📅 12:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438755">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">توقیف
اموال ۳۴ عنصر خائن در خراسان‌جنوبی
🔹
دادگستری خراسان‌جنوبی: اموال ۳۴ عنصر حامی دشمن آمریکایی-صهیونی و خائن به کشور با دستور قضایی به نفع مردم توقیف شد.
🔹
تمامی اقدامات قانونی جهت شناسایی، توقیف اموال منقول و غیرمنقول و نیز حساب‌های بانکی این افراد انجام شده و تاکنون تعدادی ملک ثبتی و آپارتمان، خودروی سواری، حساب‌های بانکی و چند وسیلهٔ ارزشمند دیگر توقیف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438755" target="_blank">📅 11:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438754">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCv3ZQmgYChSsnnxzLqvpSpg_xcGi8yWJNap93iohh-USkyQFXOruTJOGxMpSWDyu8MaRalvbMsPVjNdb5t0aR2K7RbxvyF9tuv7pHVwKwlnC-KH6MdJN_rMc_omormwdIuebtTU6zqxXio0cno0YJ41NgtirkwQEQ-0WVu3yEflsUNNe02Sltu2QmTBdgTR_YKMdRs0S9o6UXb48_v98A7ClRmu-l_pcL8T_VzxvJ-APqdpQvJ2YJ1mOpBTUCUMHajVT7jPMS05zYF5j0KfVFa7u6OSkDnUFmUkJvBzEKXhso8TVPB0iG6-xXVUfYtP3z3i8WtRgpmsftnw9IgUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام پهپاد اوربیتر توسط نیروی پدافند ارتش در منطقه قشم
🔹
روابط‌عمومی ارتش: بامداد
امروز
یک فروند پهپاد «اوربیتر» دشمن متجاوز آمریکایی‌صهیونی با رهگیری و شلیک موفق سامانۀ‌ نیروی پدافند هوایی ارتش و تحت شبکه یکپارچه قرارگاه مشترک پدافند هوایی کشور، در منطقه قشم منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438754" target="_blank">📅 11:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438753">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUpqN0BYYSy6X4fpRUb-X9YL6mSLMuzI48SjWFqNwvH5GQM4pZ1l9vJ6fJuemw0ntO1ykijSQ5c2m3CeWhhPxtWuhZIzG_47n3lS5KjlDo112DQ6cJQlfzcVpX_Nchn7o4fA5LN-_WrPnII86kiNBtFduDHCsPWgQ1c6ZiQ_kCF2cLE3-IKXKOmr9a7eR-wBPurnkiXS-npiP9-MmBLZK97g95FlzlF_iFNOFuiQFiZMCS418g6GPhyAjd1gw22lyxeyoYTdO3Y6p0rilDJ9ymKZV7RZUHgGgX0vpxcS5-HEH0mxfv5yNLVnqeBwm_8jy0o94k9pPWjYW7_sYndpAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی ایرانی با عبور از محاصرهٔ آمریکا
به خانه رسید
🔹
داده‌های ماهواره‌ای نشان ‌می‌دهد یک کشتی فله‌بر ایرانی به‌نام کامران با عبور از محاصرهٔ دریایی آمریکا به سواحل ایران در نزدیکی بندر امام خمینی(ره) رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438753" target="_blank">📅 11:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438752">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCIzfB4aK9zziAzwUW-P_25PjeftBS5MKOVY0UebJwLs4yF3s3Onrmta7FY5PMMls9eC1SfoEsoxcEKdEputiXDnrBvu9IfvD2Lhm_Rl3sgTk0LVjz2kJ7QbU_9TaTyPFPbPF7h2LVd5MyHPf-3RExCjemetLsOtKfwSg0u14w5ckQsM_7mtLwd7B9JskJ5Kwb502Rgll8zWecg1uvBe8UP2IQvYYtol1fRQbEK8KnTO7D1v47MdWKceGHexhpOrym_ZwGDb298qX05DU9PL9SUX7JcyqytfNgP3u3e9GYsGGGOtVw24JsXAMClS1Gj-I3KUD7ojU_7p5qLD58tBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت سفر در راه است
🔹
مدیرکل توسعه گردشگری داخلی وزارت گردشگری: تا هفتهٔ آینده کارت‌های سفر در اختیار مردم قرار می‌گیرد.
🔹
مردم از طریق این کارت می‌توانند هزینه‌های سفر خود را در درازمدت به‌صورت اقساطی پرداخت کنند.
🔹
اعتبار این کارت‌ها براساس سابقه بانکی افراد و بدون سقف تعیین خواهد شد و سودی به آن تعلق نمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438752" target="_blank">📅 11:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438751">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY9p6CfWyS2gE-cI-AQ1lpwMw8yXZxakqA8HYGfISAsm0fZfiJ_1wcEF-o_suSnxh88mnyPlAPaEBnCDY5QOfo0FTssYBFxO5aO6CuVdQj9YxqtOEjOlBWO9GieNPGx5aQZaLKevrN8G1i5I2qhd40fWEFzdg8C14FJ4twzo1YKadsQOmJ6Kb66eOa2xqufL6W3TS1ucwCZozmzIMtm6qsMCaPyw3KeSDTDrvoLEJgkscS1Jz7TDfEB4xMaM9Dapt4y0aetYLwGIvjdjPtDKkrkQ5LkH8GCx6H8h5lKazq-5ZmxGVmL9ylyXRLz4FkzONcUeqxBWeXG2GrCYYD2TfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان جای خالی امارات را برای ایران پر کرد
🔹
پاکستان با کاهش تعرفه‌های بندر گوادر خود و پذیرش اولین کشتی تغییر مسیرداده ایران، تلاش دارد انحصار امارات بر ترانزیت ایران را برای همیشه بشکند.
🔹
این تصمیم درحالی عملی می‌شود که مسیرهای مرسوم واردات و صادرات ایران…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438751" target="_blank">📅 11:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438750">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5746a288c.mp4?token=uCoJfx9_9JAcCJ_dwXY_ohbFDfEtSa1XRdb8UIypDSnKlbd9LM7LUth4zRabh6hVJJi3SwEY6A9YJZcfq2HfhiFHd-SiyBNmSXRFA3Xr_sqDLZKfUp_vEjjQP3D37f2VvrDWGheIa505xS18VIGdf76BLvSyrZ-20rc2UMJOKKvYVAwG7tUU3Vn04IoJ5J5Id7VngPazjMrT1uLfTJbn6t-i86SSm1QD5o_R2kGGSBw2xKzKASE_1uVwQWUtXd0ZL_QNsjnspmoa6-28nAkBAZQ0WO0XITvM0mSIT8USOu5Xcl7cbaROhVrUgpr45BMMJrzcnav60c-hbTgpvfdKtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5746a288c.mp4?token=uCoJfx9_9JAcCJ_dwXY_ohbFDfEtSa1XRdb8UIypDSnKlbd9LM7LUth4zRabh6hVJJi3SwEY6A9YJZcfq2HfhiFHd-SiyBNmSXRFA3Xr_sqDLZKfUp_vEjjQP3D37f2VvrDWGheIa505xS18VIGdf76BLvSyrZ-20rc2UMJOKKvYVAwG7tUU3Vn04IoJ5J5Id7VngPazjMrT1uLfTJbn6t-i86SSm1QD5o_R2kGGSBw2xKzKASE_1uVwQWUtXd0ZL_QNsjnspmoa6-28nAkBAZQ0WO0XITvM0mSIT8USOu5Xcl7cbaROhVrUgpr45BMMJrzcnav60c-hbTgpvfdKtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی محمود کریمی در منزل مادر شهید مجید سیب‌سرخی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/438750" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438749">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUyEsvYYJ5j52BveoZ6vlp53CUpqfc_TD1xlCSE_uaqt3HvhyQKxQTdWwKCLKERiqMFN5KVwL5QmtoqPHcEGpqoYmncFzHlSjv3Jzsiecx8bTsvbDkWqsgIo5e_IH91G0eoOQPsyoMOjkUzEpfkVDmsVX__gOjwkS9tlmyz1_XRVTWlehShmj6-H5bkH2GGIjYetHKhpnt3TEltokjntg-XwpMATIqpFPbCAOMU3gzjjci_R5B5PXPZVhNaJTcFYAlRMtpkYwACjwhAZzc9i_kCMOrf4Whme9pUwlL_fM15fEwfGn4tigDxtSGW2xRnRRYmq5qT5ZMnyNi6Ml1ACog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهلت ثبت‌نام کنکور تمدید نمی‌شود
🔹
مشاور رئیس سازمان سنجش: مهلت نام‌نویسی کنکور امشب به پایان می‌رسد و این مهلت تمدید نمی‌شود.
🔹
داوطلبان برای ثبت‌نام باید تا پایان امروز به سایت سازمان سنجش مراجعه کنند و ثبت‌نام خود را انجام دهند. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/438749" target="_blank">📅 10:48 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
