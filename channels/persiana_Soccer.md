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
<img src="https://cdn4.telesco.pe/file/jGZBntk1z7E9aoCPAGexeVORjF1OgpiRDnmi9an5NVlvj_2YTlnKEfG2-puF8Nnmmb1ISvj_aer-nWmNIj4k0HgFdGJ5qet8kuzSSJrLAEscalST4fAPoj78qbivSdnPxIeS67weF9XmDDdNlupnrafQDd_O9MsIKrkmuPHbIrHDlVzYi9JQxY7ukWc-NL3CzQJpoWA9NZvcviGxhgtNHhWc3BEGYYW_20su04k9ENODig_S7FWj-6eFqi91sS03xwF3Q6ayY1guSARyrqhPN5x9k8gdLC-hSJ4aN6HuJtLC5v9NKAVDnX8RWVzXDbn7bex14gpML7rIbRYS06mDNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 199K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 22:54:31</div>
<hr>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aclk6r7Fp5OTjOC24oGlm_7PeJ7yVTqO3EKGFQLoqeB7xI1h4VTgwEJ04UDVZwm3uUHIc6HNkH7V2eB1r9VQs6oAUOc5YoK37fPlz-xvHL_6gpDTtgZPguTt30iUheZTVsTjL8z8--zd89_QOLU6MR631m-2ldR7kihrOem4Jttt_l2vFS9xqxAjVA-Hs0FLiFRTOqHgGdSeSR88aAATdMkE2IazUOYn7kuVhzR29k4Hl5X9DtSpZVd0ZAKjoc2e7HL4si_j-DIcdaGS6ZNvEp0vLga-kX5dyl1qcC6Rad1cpCFKcn5yCaw5oVWscrfKDwJCCY0kflprNxfF3s_zMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrtxX3FZ9ivxfc7jxd351GvB3FefXYgYXSU5WXsYsxUzSprVQvrqnqfYEaXp2u5VEHxd-DRdRe5r-YYoVlJlD3mFDtqATm4YiYVOJcgQBJpOMVydjaqWyaZAMqfTT7onLG1VPz3uZCLxfP2JtdBTBv6alLU0FBqZII70Q2QmSWzN5aqE5kUo3wNfAcjX3bvSFbCAzKMM-bhVf-OryZ1eJyeNqTVisB3u2zBxI8CERQMH0STgtvjVAyeEZGXKcpY-Cw-ijvmUQTxCvJOnYh0A0sdpPNFNhCq8Wi5_9H98YjioIjOP8OV4tfcRr-C4IMWmZz8GXKkGKpmOBR1k_FdWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8YQQszUoYzFSu4dOA5Q8xha25QbeQLnnm8r52C-KytrlaY4FdW-udiQzCULfNfNQALj-gJjxSDkJtlbpaQMk80NADXrvnWLTXPlFdgI1zrri8X0T1P_lXMpThU9eoX19DTTYiPoYlrNAjubbqzJRkAF8T__ggJ6TqEfwplFYdwqToqdWaXWw5CGzXq7J47SHOPepsWFB0PI0xkZKsAS8uBqokK2OhS8rQ49X7LTgf5KciCHUwKGjEo1RQt8rfqYgpX_yWZZNmLeYJbKLYUyVkA6gMUgKtxL7iqr4kY4ohLyWczyC2Kw1zfJfz4lR7qxnmg72v8N1byJPuE18voxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7QKJlp7UmH7NE8RskMht3bTHv8sdnEcLALUowPGCbFXQqM2VwrZHKMSdTV3r5Na8mruNCNu5pBEOU9kEzx_v9qyOHJmvXMJIIhnGoTfFjPdInkXFxnGcpF7yUuErhSO0Fhb3NctCHjLZsaAQMkHADKh8UKhuVoRDtoI5JPrMgC86EoRQC39F1Zxw4rcv198vJSasJ1biti_N0l6UGybzMRC0_NE2NOh-_JD7I9eCT9yurztG5a0g4UVaH07_6ZJMS-7a7hQHQ0XBLdztnx0HzYsdw-03J7Fr_LXZxEFgydyuTgYDi2Lz3hB01boCZaMOR0SY32CuSqerm9tNbjAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfyto_CWiqKMnlqFVzm9kKGRRQgdX12Zn0RPKY3AuZUEFDhexXbJZa6ox25TT2Xbj6UzZn1202C2YMohvUpEKOmV1uj2UpB0feMyoHWPLZXzLNRqqy0PPv25M98stV-fBtKvH9IW0DhBe3tUmAbeI5pYBEZQRqb822hcHgepNqdqtRJXgQPYG8zE-9MNKu6MlhoYza1YKdfHUcGMx1yPIEs-qJF9IGJlo-hSp5chtuNJ8-03Jq8iO0vGMSuwuv3NuqXTIrR0w-E5lkdWswrN05qAMbKEuirggRH_nbw3IPdl4pB1RdpG6r5NbuvVTR4CPwcV99rPPhJBxbcaM_Ao7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=u-O9-01EtuxYh1oiLIqHjglRTJ2djDgGuucFieeccJoQ_D1kTsI8xTw425zEuwohSZqlh2ztrHHddwFDFgjBY9psTn4fBgB2DFFqQdmdxVh673JEHqGH7bX4IT2GD0FsEgCviaOROUTbQcp1VJds-a1yjLYlKD1NhO_EECJsU4qMmQxMSl-GkvcBF6WQ3Z7eeYrgGOgGcLW7qcxMOcUCy2kdZGmUC4NEDGYDYpA6C6v-16qbppFtNQ0MKO-6g8WnovvniGZyqVEqHkisacu85Xdk6V3V36vUWFBngD5dhul8Jf2aIzRBqFuBZsX_bcyhaG8g0a9tk5JJ3lci3crm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=u-O9-01EtuxYh1oiLIqHjglRTJ2djDgGuucFieeccJoQ_D1kTsI8xTw425zEuwohSZqlh2ztrHHddwFDFgjBY9psTn4fBgB2DFFqQdmdxVh673JEHqGH7bX4IT2GD0FsEgCviaOROUTbQcp1VJds-a1yjLYlKD1NhO_EECJsU4qMmQxMSl-GkvcBF6WQ3Z7eeYrgGOgGcLW7qcxMOcUCy2kdZGmUC4NEDGYDYpA6C6v-16qbppFtNQ0MKO-6g8WnovvniGZyqVEqHkisacu85Xdk6V3V36vUWFBngD5dhul8Jf2aIzRBqFuBZsX_bcyhaG8g0a9tk5JJ3lci3crm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuWK_MJGyya90dKu9jl4xK337fVPM4EGIUlg_HjjD9MpA4uSF-5trAYexxah79NaMItmjpeQpwXxSPB5FF9bQPZOnWgyA7tYaOE3DKVdKv4D-4-1ado9KxpZn3z0ubnZ6jEjxqtFnTk1z6WQ2orCHlk4fSp590DBxzeRyFIvn6CxEU9I3yv7Kug_yIrsDRXgL_YzM2fS5tAlXHKOkGPC7v4aPR5rF0g-9_zTr5CcqPqycOlX-j2U0E8nFDAlceS_W-dih-MmK6Kj2uW-RToMBlbFKBMLpP4TyLH2UrrqlNGTKqdyJWWOvIcWV3D7kwjYRkpcRKamc61L1XJX9_4Siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1vD6B6GkeaK62DLDfOgWB3_20YtnP_cnFCscG95Tb5x5Q7t0ZpArKExp5BCwjMs6TCMwujWtniulm2rUlmOVjD9od2qEEnRwMi9nKJQeF4jC1-z8A2ffcKjU1SPJVhNx2tzfqbUQRDkZN9-MxNFYk-RnzZM0HIbWqhP7gBjZfJ7TABYNhXl_dJ0b-7XHsUqWye8qeg29sMqDJTG2sW4Jk-gD-IzcR6Y_LV4CdnStc1w70zHPfy5rKyhOp9Fmp9hgdsbthoS83Xiq_5WD6D1fKF-y3sPCc5Soh3YjhGP9IUQzKttcVi34fsD55ySfo1gV0suZdAHDQMO14UmPYSQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENVP1cJbcN47mhh1YBHzPPzyh3Ny2UL0QybGdQaXGwiF9-UA66FJNZPuO76UAplslcZCT2uDIFFheF082pApEmakAtKn97iRTmPetqmti4aV955vvVhGg1OJh4JMwu5aGj9kPLvpmnfK5436MxGPtNY0rgQpmNdK-rhi-mmJHhGo7PrcaSvf71k_9iEQPBUO_Q8pGVTU4RbMmdzRzVraxsE8ojJZDwsbCNV75yFc77lbFpYRJCfM9DWE8KZsqrY_lJXC5P8M2y16sSaZ-c9MjvCQNB2b-eerlqfK48Rsa7mBMsI-HkKrjvP3yg8bP0iwNWq3bBwjMWmTsyetQsxNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEyKeJebEgefFkaCxtgEkA1lpV37SDo1xrDTTL0zzDSZaZf1k1K6E5BdzkBNtld2KlPq4WFr3N8UhDhigSUsxqqMjn1_HGQnR9kxNKeJRF2-N7t90rt3chT8c4B3ALEDr7bLXctscaDyzm-Za6NX_c72GR8DaNoubSj2Xybk_plyWlKkLRyD0t181PU9C0Gty2lsOW6yCx-ChtFNM8cShWIeAHZqbJTQDGGcuEn5Pr8Hrt9UWlx3MmM2UJVosGkFnJv9SpMFNZUzLclAw7o3SokiZ5qOKGVJ-e0bZbN_Q_R5ZrnRCyKyxU19THud73h5imB0NyrosI-S64XAAB3Xeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uu8-0UGjhbkaLewHhvfUnByqwL9qby5wZfbWlotfuSU9fdOjVGTCtVERGPeTcoprF2rgAPYtBbgezVTYjY3-0L7wzde-dqlIiRDlSk5o_ReGrDoV3H9Eqbt-HujyYbNyqFhKuq-2_SrqbHSYXoLgicsbl_7VPLv-nXpSO9hoWN6KiOw3G_XPNQ-Ibp0VliSE_dQza4wvfeTEEDz-DT8HuTby6m04K4C7TgczmJUH3QU9mWEv96RLx0v26__lDd1yCuYkQVTo0SAA73lJ7-09r_N_Jg5ZELr0QbhCj3LzGE3og8TDYvlxngPlWVweFprdgOYEb3VHr3mBR-gsTODciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg1qOpK1HQCpFgFC5ch8R0EeWM3aC1Jj5nekXDTk-oQhFFmkbn4JJYTITKO727sb_4iftPyeG2bxNmFY1Qoxhc3PZagTLc3Piq-0uoeKfcE6MpK9UgAzAIuNuLvCMJJ9l6LrR-me2JHjq0mBit19Kx0wGSrm-l1VgLGGc7v0prX5cgdLu2QtyOOowrs6qMMENmBrDPr6C7T0KJCO-aDMKM98X6L2R3eDjNejuAEOrv0cdvRafyI9rG61UG8YzwMHm0qk-T30Mkhx3U9SIBpYQsQEyTqn66y4HgTvTXmyCpPljis9WsK1I-PvI83C5YJ8Tyb5M7b4ounOsM8aq8sbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-EpLWKuf0SXX5Q9g639JYCYs2WMVjLbHIzS4jIrFdhVGsG4UieZ_CQS1qrSpVzUJXByneCTRTp5rEZwMVT8bcL9_XmUheYC_ztvkeLUzG4CLMuMM9lIDRm4kFhru2-v2gO5RTgxNk-cF-GnXZimYky_6VwoqFeD5U66vSAyhHYrjkWRRA7in11fL_UgyVY-FD8c0rO7dTTPhg0KWo19BpSbhKghc-XeQ8M1O5NXFQNh58MncBuziN2QC9_wYUtNpP1LaKnxl1j3gVZWMPFWc9MhQyltPorTbHuQH_GLIgVdpN2DR1mspXcjac_F-YgQiX9JrKd7EQUSj7E-fet76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6iTacoSV1zuwQsabZSp7cWK4BrheeDLmto6NSLyl_eitLDy9FxG7jxjTFTyGaMsCR6pqfB7TTvnIcTfGBx-YGyJWndoawxmyS-K2OYy6qd1i4S36cUz3csGhgxQhfq1ikPQKmeKlTObejnpHxSEtad-uw0BP02q5Y6CGpFIWuLAlftJ_Rf0PD5Y8rElctU5mkhO5nGURL5F9G2cbg2yprOtPADC7mRioXoTFKRPfNCkrD9F7ayF9WYojeZ4dxf8IcOFOWJNkrRO-_ZK4fuvC-yfQQWrIPapqQp7o20TwjJi1_tXkLdlMHHd6ygd8oKxUW_UJU_W3MLbkkZuz6FY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpdEk8RIsUUp4mbJJ8n2NVWRUvFWBO5HVxl2oL5c99cKxjtDuQNfupxZkMjBunVulf8t76P7GGTLl10fBhmskln8jqURMQdd2BY2w0tn7CSHlSmSUP7mH9xPMfnaAo5bhda1WoKXeoc2QT4ya7mijQLlMnDyqX50yyyj9KogdLAt-Dy6RmgyaCahEXrBvy8fI8XIT2jE_Az9yUXTotxPn4gzJiDIvhrO_x92Nf3IX06PjaYRLSXyjxB6KX594tmgW1HuixbIedO_qejaqs2i37utBRnkJ3GmcqTQbSdQvmsAdd2ShIJ6QF3tJKUqRmg55pTL6Gb4171OyCQYiATbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De8xmqfelYtdE7kAU27yM3upHLGRuIAVu59wPDEBEnjINldTeK1oMdOKl3pkTMToDZSm8OT2rjl1RLFRLmk9n_wcHL8OsECbcaQqcn4BOMKN68OK1kjHb4KCH2ZvFl64aGfx4_UUIpo4-ScdBhUYowIf5DCJvm3C3LAnze9vkStEmbvglIS-vWQwFR27usI05W3BAxiJ8OZDte4jFRcKw3_5FkdI7pto5zUkwMT0DgH3Q5Trt2LGKskP8JyKxp7x_xuFnrNSGEyHhyPhFigNRHnzptFkvpGSLqd86EygEKgW_D_gVrwmaCmvc6YRndFTZLWYDSjJD6yODHty3Y5dZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA6KKRUXJsVzi1aexljtT9b1dyuuES9fI31Wo_RewXu-HJ-5MQpLOupKZZRaaw_8ZEvcfRzpgkPNIGrbw5yMKg98mndSLP2WTcKBwYgXbfUoL7qeaG2_eXf5VaMQ4_d-Z8fo9HH7iU6PyzZNF1u9M-qtlYjkwzriLKCVhb3I4RNTGreMOeRixL8_SsQUyxqr6GkjEKaGCfaOnsfukpAirF6JrjlKIo7-HZ4Z8P7bRaMQCs4V4qJeoRhj2xKlk6uf6GA_qSDnVW7Ufn5FttpvAxfqM6OitjF_msmU8BNp-fMHrS0yEOyhnmiXV9m5Gt9ZVsN5KIX844hHB0pepobqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqicYASW9B9T3Ua0z-s9Q3VVLnasml1uorRuw7W5nJ0QuiCLQTQC8K8aRF12PYIr-cXIM_l8kq1TIcGrQ53b-QJK5NnVPBrBW1QWF6z511HEqnOpVm_SJ8eABnameckWqNk88Z96LAnHKFXWoRLhVO4JUNDiR2rURqGCVbbNRJAOe2mznxJp1vaz93x_NrLNUqj3LEBKrn2m4Q3M_J5zZ8HyHaSOZPfrL5Iu_L7EUNXa2TlNIM7FSq_CiSWnBkPV3IJJ8rmnZ-gxNlg6o6LLwKzEgKnmhWFLuJeYiQFJ1JuNPYs1ppYLRdLJUN87dF9AklKbDhgv_Wkh5K0JD4YhXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRrckIYxNaYfaa4JXCJDqIXmYIshKnxbSpRaRcY2SqN227CUrQFHogFEVG14CAj9dTpe0Ua_QdnZeYXqwy8-F6-wS5WDD2FTT-wK8TDgN0WuhpoI--JwM68O04KEEmBZjNtMN1QDuigskpnXeiz0vCfSE9yPnapbVjXqSNbG7oTMQZrI6sA3rqupW_B1wiiqOiGSZTsO8PJjs4WAZMwpi5LsTUvbS0kMuj46ee5w5cET-xYE7UwSGlqrO0wH3VjYZJd-9DgvQ0DMUF9IJ0RwqjVUYXX6nP8hy5pBZo8M04XLCmvLowvsF8YcsJRP3NjX0EPaDaBufzVB9nNebO7ZLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIZK7PMtCq1XDO3-vpzC3d9WMQjWa3m9UXCRA4Md47dVr7ZfSear9DrVXIoH2m-Me0MSNvfSOAL1JdsifWUxPz1B15g3uO9rKh7Kd9lnd589MRveCbcXHLyDxtbZBNdUujkLbmvgRJtFXlOk-RVdQdHRjj4_OHETkGkWJQtTD_jlQap5LUZbd7WByueGx42WO8l7Rngbds1EWISKdMT-bR_7SlbfV6PzICEkoUtjewUQXMquZTHkhvf1Wyloe7WzxnZxmrDN1XiaItmGwEJR80AeMEh_bzw_zr9oclqFqucxybj8uUehsqXjM1d1hYcXBft4PDYbYlGaMQgZb9HLAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg4IOQy0Kd1_9mlj_lfwQpqnrprn0od0z3bqfhZZWs4kB--kCw-bUZSPI0YILtLI01Rz4_Io5d_wqSPBvYay6BBvCRA1QuLBNuGmzE8VMBsBQaajK9DiVxIq7xUCZGM10LIP7FFAi-dry2U8i3oro-MFSmR76tU95tzdrMb3IBgMsxipgcBaHvG8yrEfeVdM6tY4p0PFEO1amSmRe3frBU9WXvC1AeCo_AgqgqbYI4eYcbOgUMmtcmmPerzEP9Hvsg6uFkOxwtxhvQv99wGX7t0l1ihrQjSJ8LLMqagaEg3KgX4Fbj_DAPtX1C4P_7ISAl7n-_zB38zrEdZxGY6zKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlnjSF0k2tsgKbT2I5qzdoW64vdbAmAIH9yCV_xV9iy-WPTtXEzCiuw179FBsRladpF2dYF5r2BPxW_pJ-iEWYJiq__Mre-YWmst-HXqsL0HXpfaXr8g4nGgpVjO8ETwhAu1s5kRpNJmdBk9DTck876_8dzM8iN7OoR6BaQ8VvdyvhMu_BDHFtQ1pZXsSm_yi6M0OPfmfPE-b8gQ3CQ-Df932tDHzCc00DqTPfygLkp28e9HNsalU6BYYHkTRprXou37c4M19iJn6edZ4lUouHZRzgaMF9gSnWLGocjGBfT8IVa8ocdDGONaTOT6PINT6x7cpNIuww0glrfpBTWrvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22227">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JimHe9JIaMYKOTnZvCI8MfEeoXoMtoiIRcDfkX8N1_Y0xKXlxOOX0F-_SQPKM72njRkWXN45E9puydiWHp-SsaKbPPMvYQq2wivRDk40Zgi0qM7OwE0dNKZPcgNyDWy0gZ9gTcPllhZ2t_y-VTNixw_iFSH4Y4jZt4xtzeKTVY0pTdsUC0bmVVEjXDlR6ggXfDqJaEU1xHe8-7XxFwNFg8AzIzfIU1wf7aLQMNLYhVjrjru07oM54WC6SdDrLl_y1WLjax6ci95y0j701NUh3nxNWadI3GObLk1mAuCMmZZSElg_EyPMw1rbxdUYoCwrjhbRdKbE1n8U-FIaZj5oWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چنل ما برای اوناییه که فوتبالو نفس میکشن
📹
خبرای لحظه‌ای تحلیل، حاشیه، نقل‌وانتقالات
🟨
مهم‌ترین اتفاقای ورزشی پوشش داده می‌شه
🥅
یه منبع‌کامل و قابل‌اعتماد دقیقا همین‌جاست
▫️
https://t.me/+XdSZ8OmU62QwYTU0</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/persiana_Soccer/22227" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYXb2qaeHjZCkfZCX6ux_uYGsr5IAM_GzoR4Ydxoncwy7zBGg_qaPKkaU1qKWUBw8qWh9uXBdmeTQyxWb1g64g6zYzzxHKlZbg6jNTfMGTriGyuNuRX8poscqIFISc8UjJXfiH7Yn-D_5mNgXMm5TywAF8X_MeIuEUqzVulGqYwWfNHfYmHziQL6hKlds7HwYa-2My0NBHgxTOoeir3woaUbN7mDFx7WHNltQ8vlEAXSRVcoA_DpZoUhq5Sed5yjWWKd95TC5Mf7p2k14SHH6aRR8sKl1-tjuws0X_3w_0MVH8qjFDALntB4OrRChl_Lv0MVt7sN9Tvdtybzg6cfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfQ3fHrwdAwA7ID9ojM92JvHzuhT4bAVFOXpkKmJls4NombMD2vXcKEQ-GxKiSMdBovAj3HzertCMsWSpzrdt4v27_QIlLIPrfKXXE67ej8ZnBcreENOGDaebEYlbFfJbcikIIo8Xr3VNUSQQGryv4dNu3nxtcYXHpktT6DkWKjbWuZWSxAb8KHu1WXJJJO-KgMUbiW_FVXP9FSjGaFYrCVh2boSdjpLgdiqxY4wczNAfxlOtgf2nbfdNidgRDW9HIk8lp0TwNU7uR0H_2eqRlzCUhrgYaK-doOdezuQzAjh5vEvddqEJJoqa5BV3EGMCGG_VDsRG9Aonoc_uete9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=fxq8cCUzCXEN8KqEuwAikAckESdhuwLLcwfOmA2_-JYPvR0bLOO8HxFSTUGZdwvXW4LPT6m-ervpBsEgR9gT27LJJiyu45H_AOX_y7ONRHX__NOPnYfRXmryE_I72d38wA6e4dG1UuJkzvtivUCUEL-nlyEnSWwp8UwfZseUXDlHGUTEAq2gY05TbJqRWoMzvcGGeNdVnXGkcURbpCbp5N8nkK0TiSaE49XL8fMNF0oDIPAWr_mKj8Kno2vs5IhTrW5KFsC6aZivPIr-2-_JwXFQF7eUhrr3ufOW1lY-kaY8HBTevP0hI2b7vejnb3zNDnc6IYWNLH_BDDtL6ejbqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=fxq8cCUzCXEN8KqEuwAikAckESdhuwLLcwfOmA2_-JYPvR0bLOO8HxFSTUGZdwvXW4LPT6m-ervpBsEgR9gT27LJJiyu45H_AOX_y7ONRHX__NOPnYfRXmryE_I72d38wA6e4dG1UuJkzvtivUCUEL-nlyEnSWwp8UwfZseUXDlHGUTEAq2gY05TbJqRWoMzvcGGeNdVnXGkcURbpCbp5N8nkK0TiSaE49XL8fMNF0oDIPAWr_mKj8Kno2vs5IhTrW5KFsC6aZivPIr-2-_JwXFQF7eUhrr3ufOW1lY-kaY8HBTevP0hI2b7vejnb3zNDnc6IYWNLH_BDDtL6ejbqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=U3JNWoDuDTTayX8AZkq4YboJGAA1cnWQRMNc6j-maTc6W3HDK5WQxtpal-V_SzJbGMAfCDb6PZ_Kcu5hpaMqLHrqZg25WpFFhRHW7QLK4xswmJe0CkenH42nA6jjOAkF0KJqtNBkrozkFU1_uT_TbFDIuMBgc0F_8kd_UFy7YbLL__VSV94gYIhCbBbrwG-VIguLStdtE3IKn_SrEayqLQjA6yYDcuUaX5S3_ekZe_Il2TA6IM0I4pX5yjFhbET45ExZq0XIlu0pK8e4etTwb-6-cGuxvGAg6X5DxBFkHNSaMuIuuY2PTyOigdXO48t4fUSMxjaYhmslSMtKf-0NjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=U3JNWoDuDTTayX8AZkq4YboJGAA1cnWQRMNc6j-maTc6W3HDK5WQxtpal-V_SzJbGMAfCDb6PZ_Kcu5hpaMqLHrqZg25WpFFhRHW7QLK4xswmJe0CkenH42nA6jjOAkF0KJqtNBkrozkFU1_uT_TbFDIuMBgc0F_8kd_UFy7YbLL__VSV94gYIhCbBbrwG-VIguLStdtE3IKn_SrEayqLQjA6yYDcuUaX5S3_ekZe_Il2TA6IM0I4pX5yjFhbET45ExZq0XIlu0pK8e4etTwb-6-cGuxvGAg6X5DxBFkHNSaMuIuuY2PTyOigdXO48t4fUSMxjaYhmslSMtKf-0NjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUgnn5Y4jCvWSK4P04FVVCFYzaLVbsLX9e1EQdfEq_KeNwEtb1R7SFp9kKhnjQQ5tseramTKWgr2q5a5DpuqwHDIjLDFNThxte40pFXmiBz3kPUFhmWK66Wqdak9u3egUnRGKkgPEKWXTNABH1QS7YJnWJGUGMQ-NU_8M4bNHnRBpDp_Box6VBX3K9uGo-kezPN16_1cDU296yGBdcztILdFO1S0B-h6WeO80eN1Ck6tIe6hAdSAPO2PzIC1gbHXCKDAE6QHlEQyglB-ZM3ZVXz636eBpY9n7zMjWPgkLUvw9F-XrJen_Yqg-5iYOE3-cPGFQEI5sy0eu1RQBSGMwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
آفر مجموعه سوآن وی پی ان: ( علیرضا )
⭕️
مخاطبینی که 10 گیگ کانفیگ از ما تهیه کنند گیگی 185 هزار تومان براشون حساب خواهد شد.
⭕️
و مخاطبینی که 20 گیگ تهیه کنند، گیگی 177 تومن براشون حساب خواهد شد.
جهت خرید به آیدی زیر پیام بدین
👇
(
@alireza_mosve
. )
⚡️
𝑪𝒉𝒂𝒏𝒏𝒆𝒍
➡️
@vpnswan</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22221" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUwkyoQWyBOMd8Ai9ZqiEJSuaZNEdxnQZF20b8MRXCobImub4x_20tVFQ5CuozL3Qn3UrMPnnEj3Rs-KYc71wsnFbB1bXyXmLw7GB84s9Jod7I1u44DcyFWzNERqKuM0JlgddyzEbXcJh117hlnXBBFKxMi9uUNQUkNprxpYTLAQhGRWqRuN2RUzJ1xAFxfC7uSTYN9BvkHhHAoZlV8xtHFqUff9wW6pJhhSn7Ifm44yK45sqr_0hQvdzud87ItaAwdeHgQLY8LhNnrjatARIZTXO-gFxlKv5B7y1ar8RYVJo9RVPAVhZ_B7KnVhHcpsJBj2RGgg8JKia0bS-M2xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYks4UkYvi-xSil3K6Hb80jV-hH7h9__1PGF2CRPfSEgSNHD31zZiMdvgH7D5yiiidsOEHxb9vnl4lA_XqK6NGFPpe4mNPnzVZALF1wxti4EQmYVhp6hdy1nK3zUzcseqUyYgCP3doUxMNuWuGsyEhzmhxUDRAzn9u4cJ2VDXklWtT48HenLJpgtWgl5J9r7ml_UwsHbl4-c0O2KcY3qlBcEq_Yd7QUpb-LtIO-wiFdW_c4n_VC33_b42kl0P74SZypZtzBLRfFBLZZs-pgivokVfp7Zt0--0JpBkge4o4qtDCzK43eVuzFHaBRtQsTQkazhpS-s7aEo4VX8rCP9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv5YpdoUclf2DLsVguk6fNwwkPRC2Es3TGKhTiOND4c5OLZyh6ZiiDyn8iXaEPlijU3nutHhepGemT5s-392f0YaQhlNsYo7nZi2Jl8lLRDlysv39E99_ZAOMwGDAo8l9y6L1yqphZo4zKcMaCsk3iSOVrpB3RuJKAM1AjyP1EO_rjDLnz5M4n-FZEu9Glwx8iq6S8RLakXWgXZXdNzRCdDFA6fP6g1oVPZv_ZWJ0BhHei9E3epRB1ayJS4jHxjgJZ7dF-yeVgSvJB4LVwSTxWpdsNVa8z4mOm5tIxpfaY2zDXYic22jjHkdClC93IFnVnvf7Q-A0UC2OVOU5jDpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0RDDxpbUBcacsDEXWGZXW-tc7fXr1Jpgu4sOENaCNELFrCCAnpRtF70z3CKeqSAN9dxNp3l2IU19oMh2_2hzziBELzhi5K3qPaFVVkc-EkmQN5hm94JOnqHNqNfNX8LWECPs6TH17x3eKWv4UIIy84XqnkJ6-HHaV8JYOs_OPh7-Pwx2VZ4vWZgL7beX8K1cJvEiaWcUYXqN-7fD8GI-nndnUNHsIW4_oFMNUd2hR_75qE39gF6hVuIHWljYOiP8ewYxruX_b5k28oZLsrRY7WAIPStIvq1JC3Y212cqUZziRVViXSjECkt3Hs4V6D63icBTK8h5n9DapGUSMopSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3vMFgAmKsYAIsaeFYMFh1KRISsW_xVaVk_IwcEPB770zusdv1tXQY-pXtfHxsNXZL57yXAOOXtWMsJ8tisoGrOFWyHgsTUD3b35v29KOo3Z9acUNSil8qI1u1fGWazwOiXeVeFajER7nC6ezfbvuKr2uwzevqQ8Za0gPsWN6MdH1pPFrHm_r3W6HZJtnUhnSYPfH4FIhp3FuWNOW0cgw3mR0i28TEKEBrWQsefiB0hX9SZ3MXgW-UdnG0Esd_TCecy7vLEkoL84-zfWhOzxYFNsznq91B7_YELmWi0kbDXoO8Dy9kgs_EAMR0D8u4G9jtH11Bey9OeuuU94gn5UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEnTV2O0z4KZ5MulsXJQ-nXCN_52z1MuErezVn5uMmk1K7vVdD3jb-M3s8e-D0AJ7U-OGxBoFnasqRxITwYcgCNCeN_Cg32isNSGa9SMFPDOixLXUeeVlIxkyH55CXsr2sjGFZLk_Tvtcu5MUNhhyvVTef_SFxBUReHPlSHaFbaqbPngucE3qx-ywrmG5FJU4n0fUp8I9HtIk_PptKoxJi1RFmhqmKX1LTIDAPRd2mIdzaILb8mw10r6n9YAKXMzbeR0jP27fV4Zr_HKTGicpRbZU9A-zmaiov2tbRHeiJv84xYxQAVPhB4nyIvBDJTrU1ikpwm71xA5yfoBGTQP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEb2SoDRVWaWCOX0J5SRnBgG2_QW6AUWX1bVJYg12829DwgZlu-VtTV4bGKHZYxMqXTD7jdhszgq613-6PonLolCKQ-S2jO0yLiZ_KC9pqNBrNor9JO_0Vb6N6ML63i0y_nWk8o7nn2RWy3r9rvdZh7WQfOAOp3mFaX5bKktKT4JSMQ0iItAlvzpOci1uyuYK6xMl1Iga2ByeOGQC5XF8SkPx21RCv96xOQCvBF2i_wHrfngpPjnbzySQ6pRo-tunBEss1Fwa9zE1RSbznSaLHkhMKySRNWnTL8GbRynO8h1e0pNNVjO5PDRWpJlMNZSfz4sIqxkfx8SqjZO_OIvXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBX0LEFz7weFXZSgLiOjC16E2Flq2UuLo1sKhgO7TIp82j7lC7Ca1CjBwfTjNT55ncYxRZiTDjLADT1Mpeoh5YBT8thwNP3-pUMsNPuEm5lpKcwot3s00IqJMzjMQsl6dZzpCn61Tpwb_a2662jzJjIHTr1Zcr4AqPlcUXoCCnjoCwrzvTvdmoW9YljzCWw3beS8KqKh_bYUvljJEveoMsktE8cNKNz4IOipF-ZQpOG1OSlO28Hbj7vrsZBmm1BOVP6465zvab9DLdPJsgT7IkDuEibjLKfshQLiyAvDubfGg-C7utRA8qfkxV859YEvtkHnSCGUhZkY7-OBv6O4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOU1qMbPZDydHn9kB6BVyRWOHEJ1ao-urnb4NcKsKSy2S0qt3aIwI09tE9_B8yWGarbuipu8_fvpH--YMLZBNnH1TpQMbEr85G5E0C2X7CI5IBHPaDUS4XpIZrIEpCrikxaRiKB8MLEJvbNFC8jGZo8gvatdC5j8ROKLqEPhBnKssnrAWBDX5QxOh6Kflc4Nir5QzhBQV78uA_Q6q4Fyy7P4HeqaKNJk2hrna12ub9ty69IaLljda-TuymEwwo1X38IzgB32J6_q5cINA4dXH7AonZTP-tcD8vy2TCi2MoWFHdODe7ccPMljIOEnAN2oYg15q-PDsJaj0ikbfqnPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1hMJKNeV93V2Ao4XfzZ12PbvxjTnnmOYm6gA94gg-Ll6R8VYBvAkOGv_Uf9koqHrIIoSXamOWv63NEc_J6EtFQVH78CgxfFRgOK3ZeEHqofVHyQ6rhamJl0g1qW6qUX8C92rjGZ14T4FNkGEnsLq5D66B2djknxR8dx0ZLy9np4YrZ7djwudstxRbhKQxUlSCCmWwh3o7fRbzITvxn1tAPupF82idUoDWHHcDrFjULnPJYyXK0pLeTGI9DOgG0kT8vbkZ44lWxdcEjz2pfPiHft7FsyiWtTw4ChvOMWBKsORJ7iw7JjevUH6GnOw5ZDC-aGlHqf3tl0LZHu1Ei0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lClAbhLtfVDqJb81WP6LFp2cipbVGbRz-whM4ZrZ_zosjstN62rXfeYpWyaWhGsAo9y--b-IVRgPgJ7Uhmw7ItnqKZp3CIuo0hRbYsAdVmfU-T-X5gzN9XxoevoWlzME9FSHsHr5RScnuK_icLENb_m3YaU_rwrRTu4PBBUcxhnJzMBlPZFYGKtfpKxHHqtr9Fv12bmL_dPGdvwbklkWs34svJVqMzn95nxRVtTuBzQWZ94O-sAJNVblZcfhyz9TzWvRvhc0qC95xM1-BJexTX9pssltqpTK4aiT5WhEyqQgZyC3iwNN-lU8LInAnyRgIorWht46MZK8ro1orsGNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX1E48H6q6NUk4Fd3n8avhiT04RpLCKMU43YIdKEM-ycQHTZVUB9U5ssmK6_0ZR4rPDcr3gq0mg8i6yeN_iL9VEih66QAIMzHUgkvyWOOdKODUHtSd3MGos_UEIGcdzAIDC2T2fifONDFAg0H3BI1xAEdCT0qde_5yxyx9NSqlyfUIMEG8X5KtNPq9Hk-TA7i7gnSI49lgJIImXcsdnHVbzZu8AB4nR9Mm4kV9D3EvjFExZET1sGRqS-JeJaOpe8IDiRqk9ccWJG5SbqDAT7cN58RKEGP3IsF3DcOr4mo0UdoMfNvO_OtJiqnftjwv2XPHBHwT03eBlebVfSBnUq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-JauixGHvpFMKFXECPThDbat3wj1w1UtUbU1CyS6GbaiCrLgcVXxww1QGjDCDoR9pyEFDVjdz6dlgFobxuFmrCSg8-qR4WEZl-PYRrfEMH8y6heKoAVl9H6RySmrD7uJJ-MSz_eXG-Csu0UKDwGrhNojOv6STvgHVl3bgTicvzKqkBC3sXQCO17JNCR8uLE7rVCLYro7KRmE4kKI2SO_S2n9y_1IVdu9j5jZ0YDd7E8kXYAheDLviKIG3tg0mprcFCiiG4dxWpylF8oYm4jduKGdm3cVjOhtS7LB4qRlQsw_SBoC6o5B1f5aXsKBdZGyQ9I-KdKsiFFY9_uMicMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDlUk6rvoW0CXQkGz8tiNI3_P0m_gJCLTtiB60EL7m1D8T_dx5l37CBNkkp7gHYkutgsWzu9F5jt-AvVKKegMjsbuIlQ0Z3NerXpAkZ024qki78TePMlrKkVKcjmk2XH69qQHDdxlDFDQnNQAPfi0aLGaQ6VYsBshq7TCEG4xaQ1rdBkjy31QAgX6fWsGGAeltUa7hVzRrVb8U7xiRemBd-ZeBu4xkiFC0MnMFevkme5BSLt_MiJbXtS1wJ3bJSjSKNcbSQ889sJ8J8Zk64UklumFFlClE6qwDE-QEvy8jbuNUQjHNVvGY5Tuw9UD7YBZlVFc5IHKC_AdGZLMlbyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpqzBXU0-eECqP9L8bijibGJVY6Zf_Lx1UN8eCbhTH0ZXk5hlNP5kwhMdPKDWcsEaq2_XGlf9GLStiVyu9t1GfaKBraV_3dz8FhpDJxFP8-4N3LN-jehWP6iRC2D8o5XsSNvn_RjoP45z24Re33DyLuFvneIGsO21349Gn6IP4A5i2lLV3gQb4y7MUkCO4UUp0Q3OKpckAkRht2RoCp2D-SI9dBi5XfuBJPl820SMymdJ97aLXqNAkXAHgDB9d4CdL0bKIVHfudYqtBqSf2SA59TF3LWQrV-sAJQTyUNnk1getpPGj8tmmEkezrNuR4i1kFDV2Ipdg3v0QBea1fheA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKKS9gAfH5kYzkLUzioAy2hm29xLsrhW_VUpH859q8ngKjIdfLFfoGu13G9-5JrgLeDo42tBNeOKS8rkYZfzmLPPZYiwlrug3IUQo60_TRfgqwlyihMiI4JK8p_0rtNDWhJ7qEF8pArbYoxHmovPefuLFVkftAn2L207_1y2KuRHlRmgwqJnFwL44Bh5EnjF9Z0uKWSj5pZE-1VaqR9Jxqnlw-N7WIOGeAfqmAxXbhvjw_bFGiqnlAyHY7A3ZJkIhCkZMqdkTSYddCQviHPQCBIhs8uLg2zEjvj4CWUZqzkUQOO10JbJIglxU0IvgfG_lg-PksND5TvA9EHWHO6bXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf392KmRLKGLFmhyV4NGh-yPdsqR1Vh-YpHtmJoMuh7G_yipM3a6VPY3sad1-67FXCzCU0rhDL4wUMTPLPSHKrNvg4MYpDhVQq3XKXvljOaFr2I4Ru9gPv1oywq70MQjLStMdhdv4E_Ckk4SQYQ68gnNX1FujNJV5lzetfszO8YyJtWjtSeJMTUL3T4J7hxxvBV6IrQeeOObv95hIU19meLCZNNIu2izPTSGDEYo9jOrFnWnZFpgvd57Cyl-9qSeVuWZW2Lg0j_z8LaSl0sdr7YzIGNE3ARauV80TEgAsf_A8wue6rsRayomLRPZqNfxXpbX1SdzgRtOHCFY7o8yow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjVYzbJaFpuNSvqF-kIJHGycjrhT2x-SOU2U-w-TkuQnyOA6YPyias5xSmGfky0tzi5wz2vJbh-m6RnmnDRKoBJzCiaTCr20p5mCQ9EoMp8VYrZKU8QyOHPnX3a_MnU-X9ZfdxILteFq2A5EIBlgje1iF3pNZxE22TQDAQD4Wh6-Qqdp_nOsmiFVlGXWOH6r910TZkfShXoiVO0szvTHXpqxwy0dRat2gc2ac8fBtkxQ2QVUHj_UrNrom2X-BpZse6moZyTdjMpWuIl4vkrQKn5mDh1ueD2qIkwpN_0DrLmb3qGvsv-LnFw3Ma_vcGlaB3R3AIAyKQZ-2Ua0_KMp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfcnvzeMMWWGguyeIRdWn9vTWQYhHV6FCKhOEUbopKtayMTDyP2sHTEPzoX4UWkJh-kUmJNL0R6mdKYb5EZ0rlB5_5a7YT-OHpybvhECWpaTC33ywMkLpNFbDaMzSBPdwbnQbiGLhor8M4k2-Lo1pxATNQ7SLI2dVrDWpSQRm8W34_LzwxNZyoFTT8EpZmfEGFynKY4PUWOFKu9NdpjkP3N6acyUfADlRHkDBut0cHTcU0_HzzQ6MHYzljCfh481dQwTRgoNqzwy8gwODFdXT-2Ce7bHpF4ugcp3tSJV5uUX-rRASe5Q5e9UqteTb73d8sPpPrLL1hJPg_OHMrlnFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=aSAeKArQxVLjtkSNL6g-BXXmUqeWy2NCcd7wJ5RE6fa5BjTn0pFuD01T5ibeZBQq9vYr-tOQrLWeV59PW7MNC4sjuukhzVYT_Ez74D6AEozszHk3viTbsw2oJGjtO_O6MjE0D7RgBcI0RLtOPC5OnCPr055dBO6Ec2dOW3sP-Do0qcJmqHsG-yrKEbir9DfTxxxOWHo5J3yzmn-U0Dp-eBxIjtTYDHCa4kpfcflu9UWX25Ij3IlM5R_6Z5Xhgz01GS_0QIVcDJz_eo43HC6VAyqTltonCiyF6UGYwviCoEnG1r8OQEcbVcUEHnQM8Ov9h69ZDmuDzZ2A_is9AipXsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=aSAeKArQxVLjtkSNL6g-BXXmUqeWy2NCcd7wJ5RE6fa5BjTn0pFuD01T5ibeZBQq9vYr-tOQrLWeV59PW7MNC4sjuukhzVYT_Ez74D6AEozszHk3viTbsw2oJGjtO_O6MjE0D7RgBcI0RLtOPC5OnCPr055dBO6Ec2dOW3sP-Do0qcJmqHsG-yrKEbir9DfTxxxOWHo5J3yzmn-U0Dp-eBxIjtTYDHCa4kpfcflu9UWX25Ij3IlM5R_6Z5Xhgz01GS_0QIVcDJz_eo43HC6VAyqTltonCiyF6UGYwviCoEnG1r8OQEcbVcUEHnQM8Ov9h69ZDmuDzZ2A_is9AipXsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewQ8Q3qCOQi1WVi2GlaaobOLq6ae55PQB8KhX7pZhODVKIC20gIUtvTpUKVI9zsIh9UiDuapqoGcXaaYDfVOjjWTc7nnntrsx4yaj3zgNLWzKUkhBupT8FM8RMWFSVrCQSr8pg9Xh4p8T5SsVqAbvSPVG7zu1zWv_9Nut4E0hS0YdUEcFQixbM9ERscKhqP1GOmETSZo8CGWCtFq2w7Vaevd172eTdCalJYBGcs2fGE9dVmEHYEoMpt_6yXFczH4GVggPpXIR-2qUz-lInazPbWYF1DieKA8ebNtoZTJ1SGLCs1mo1KQAI95Ij1EHzYd_CFyJ4fowDwEkRtoa0Db3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBlMisIPO-_8OKwbjNJQrITmlULVh5NrNNLMOF43VgkUpzow5Btx7USj2OoS7g4Q2nA7UQYW2e_2DX6KiW2Wr3R1niDiLzO5_LSN7Sqv0yDMnq03j-a3PemPtdgDUF_5cG03up0RwX9NRDxjh3OWyRmnh9wgheGR6eV8HJK3KY1VkKfwCwQkEMuxjA0M7R0ErhC-cTBD6pmVyWbHC7bkQa0DfBn9KptCwx77C5ns6xTVludc7M4xXabJQPZMU7-o9E6rjJ833ffTgv3CuF5LaYQyD0xZlzcY1ihFSRubWPjrSfCkNAI-DTuqlcUDVXBXrQC6VcWjTualKVDkdGth3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHo819s7hMXebMluHEh50UyadS6QVG1k4ZZKc2Src_OXHoNJmcFloS7DMim-rXI_lEU7WwIlMPquFxVjpQpFm_k6U8WvOV8U2jXMgtspeYNXCHCeLfKeMYWDFuWpFumbrCg2HmyShAbR8c5_AUfQF2Q5EdrX7H-2CcdWUGvoOB98AaosfXFuSps7POMQKkd9fzH1NND8FA3T_lwEFwVm17GK20OWKl2oIvR0urMz_qVeKPZUsK32ZQ9SPx4Y9jFMH_4acWu_Q6Wx9Mng53FhZBPWkgQJYrTfVdVGJgaOIC0GJQH9XfJriaNHqJolIYem6ezz0E54a779wO4DHuf34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whwxl37Y7PsOId8KRnBzfsNVHGPuQXy9mwm0ZqAy2t62eMnTx9hfTYGQQuga6SJnjzl46XkNG-joOM1Bp_YmNPDpNu-RImP5gXZ0_PqrN8jaBAiGy-FkSy4gpeM_qjiQYsuO1ZQCSLSSuSUfoymSqf72UFKYTQHl76F48TdBL2r7f3xFqCVIRVWtvP15IJ37YpzRym2MM0IgLW-e4SJkBKXbQOupiXvy8f3GF_wdq2o7DrjNLD1lRAhtncOI-rWmAHcikFXZwKfhnZ_tft22VOpGN2R_y0ig1i_QcQLoI5giKgY0R1rXTlrhaDu5Nk8HofnaDP9veeU7B_fJ9N1zKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_M9CccPNQikbzSSR9XS3nGOvKxMT62UiulTK57qYIOeQ9mGVKXCeGQtqNx2b9cDpEMCFo5cZNd7jfqlZ-nRjdAMhWqGBvOp7ucXG25N4zKRbw8vPSKLnsjMhKbZYBwpDNrwFe9KrcpQ4kEU-IGPMR0D7Zc-91OK9Azrc2nYvchGKkdfxP3XWrssyBlZKz76n5VDqz7qALzuqIJ25ERvQS83_7nMl6G03cSU2OLFETOLs8rNITmhyXrVIL2JEVj0w2IiAC8EGzGTQtrkFqrwG_ci-iEZteQp7kwrhlDQ44xkLekawSReLRJesyHgl58O4yRV6RtAL3S7c7ZYHpCPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hkpg--EOD9eUK5fND9ADHTssP-lYIIrhsrxBGQZgsse83PXlT9u8jilJetFZsyg-MI1Z1zJ9UDOx2vM7GLQy0kei7ytsuFS1vyM9trWuA4WswAkN8V_jcw6qG_Od1vu_seFyDmrA89Y4lk99CatZlP1ttIj1f1hb4ydt07UE-zys4iDtxNNmDyLZbhanSVlJLTPljZnq0q90g2tX3oFalHwwL1tNkuejdEgYiPhLUVG98qgPmB0LTqW2xNzBP_CkYjo-vFN3oy2vXUwzPyJ1OdkxxlGKuyDPPpRuMy1ncDLtOeY4jU2SGTleVzX1PqdPF4Hc4NtxsmSAfR8fyoKGgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCz18M1InzxuNAW_jsm7OwbwgaAlwluUeazUw7S5WCz4O2Nb-cbryQoYWPSrkmX2TQB4N_QXjG92fyCwxoU32n0AvVWrrzhf_UJFoV9oKjpyr8VsK5qPY6iCIDyf9_kpHqp9pNcC14VQ8IvIdvLe-U62oCU4-r95_RxmZwftu5QVgVDSK_E_N7xNnnlKdqbxgm59kidVt8enTWPnj7C7tXSjjfnWsnI6fuNmldn1TksrvM9Y43DYMMjzUJUQUUGRQe3fl8roqpQ3MRabG-B7NOk12i9kMosI7NCE99fnkHP6A1ngHXahjjaQ5ff4CZ6mGGCjRMr782O98ivAUwVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb5f9qPV4griMXSk_9u1ZPHadoEfk3HyNJoJTPqHU1g17126YDr5ABT5otpgAxsdcDEp0tQrwhLuHDUEPJ1CmufHNl7tT3xgZwze_U9RIBeO6ff3paUdQHio2Ob1h9xETJm1FHp-WNvDPHasRPMos1Ejf2iioJkJ32ey7lj4Ag55zcIa_IxlszTPvJJtZHSdZW5hRaw45gkhMYLEtAYzzxd3WiyIJFTt5wlpXMne46an3S0DwIwsb65t0kWM4gi7AnvCXMrir1sVQSbVTPNnjaCMR13mpQ3nLMrADMlxNS57bxlCDmKOY9OPt6kMAeR_sx7UC4cmw1cR8oZmyCeMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyPGLg-PZrzro46h1XyPWRnZV4WTZhb1s92zjF8d8ShUqynWCqei6w3hUyonwGPuJK7sg3PFmb6rpeaU2US1bYG_fRXsq0JT6gDJ4SjtYL50WI1QMCeX14kA7LdAqbDAwqnKS9j19QsGRS4nZ54I0z3vdU5vph9u8JnyiAGUBbLnf-Ddk8qE9aXRdERqulHyLAZ7CTRBKQbUdQW2zyHTSxsxn7OQJ3Y9Uy5G68rr3TCNweMDkUzRgoqTnY3TUJiwKqMP9DU9jq9uTr7ftiMkMvv3feoG205JMEmlaoKb9DPoFytpqIUBMEwesbUoaiOfo3VZXjxwlaQMhqG7_ffUKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIITkPdrjK0XxPT_2_09PQvWiH9_xGtOTA8lx8qkzxbvK9FdDKpMA2r5YSWOEAges9kwGiDuDZUaEJgSHCrQFVhZr_stVsqRlfWm37_op-tzP55eO0VvYNmlsuhMkbK-l0NKXljflpPvlewmmMpBcZEp3uDDUA-VTuhhgaBoJomlXJf4NvOw8C5oX--rVzhAVEAsfUF0wmdnMquw2hmcFXRSYThHgwLFknKuoWR7ee8wPGYeIwHekh1aoN7jcNREpQXAkxrUjGprWhqP7RMzQbWWXCOP7ggMt_8esA2B4iG6ZR9TTFb1XKj5HGPyVa7nK82lkcJmQ-EG0dnSHlGTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c08W2umHA2NnUctOKfVkSws_TfliQimwWPtjopFRjGgBfAt00t3OAYtpeQoBAuOhI2coFHKKGg88mg8NKga9k9uCWcgBPBgFpu6_411rtUqYBGf2ccGkd6YGLmnOBP5ax3HlSrDlie0dQ5OguWpxbj7DYpag7FgeHf9jPdbxedYcGrDOxKzmq7ycWr8KPnMt30UzgbKk4-eZO_IO8Kx-fpzF02b0asnk7x1kigjORaGBkFIj_6PTwQE5aSMTjJUwdGiPJ6G2-3vwRvUsKN-_ZL2sNGkCkIGQd-bTRTSJjCML1SaZIRdA9gYR66eRlojOrRRS-f09VCteeQ2iPj7IBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=YYKoPpab7N4gB0HEIopYyihTnMPV5nPStEjUY97Vh-BdviqKRch6MnFcnG19uI4LF2DFUdSBopbv7CgJqUdYLexcDakPSK_bWlzp7JvqEbNbyVKCi6STNFy0BKrjOvkm5iHebwLSlPnDw5sNLt4r7dd1JxY64IGfEmosO-Y2a5SBGQSu1Mx8Qast-QhAhO_L5rJ-I4LsJB2t80i17YN4ho-3ean96FL0BK4XjMlZZ6aIoD92K4ISTAOLyaGp-gGT1S6ptIzVm3VuKRL4LJAyzXbq6Huz6dwdHeFSiinyf5E2pNOMC4rxRBoC79_BdEzZqa-g5kqnRvgEOMQqmlr6qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=YYKoPpab7N4gB0HEIopYyihTnMPV5nPStEjUY97Vh-BdviqKRch6MnFcnG19uI4LF2DFUdSBopbv7CgJqUdYLexcDakPSK_bWlzp7JvqEbNbyVKCi6STNFy0BKrjOvkm5iHebwLSlPnDw5sNLt4r7dd1JxY64IGfEmosO-Y2a5SBGQSu1Mx8Qast-QhAhO_L5rJ-I4LsJB2t80i17YN4ho-3ean96FL0BK4XjMlZZ6aIoD92K4ISTAOLyaGp-gGT1S6ptIzVm3VuKRL4LJAyzXbq6Huz6dwdHeFSiinyf5E2pNOMC4rxRBoC79_BdEzZqa-g5kqnRvgEOMQqmlr6qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmocrzLuKj0jNunu5qawF2NbJ0N1MB19DJuH9XBRStDhQyiEVwCdbA8M_5t5WuWs1MibNxFdvVE7yiWMdCsDNNooSqqm-SowBmo95gR7tj8FOpv4Ri3a8PJYYFh8EIGYBmgNkmQ3kAWsjv13jiQq5axtXG3QqcVfHvpQLVLBtVsTBZ3DhU7TGt85CGZIFdo-1GoAecZtbQjhDbra1UM9wwJaoRUDvE-0DQGd7rbLStPcrZpOv3nDa6ZxxFd4Nw2gvn5OR_sqr5_FvnkvNgj0htUaiI4CrkhCPwNPo3md85B27M2N-If74nYRO2ntDbkLXTcBmnZhfYCV3MUAe5VF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss5gZZg0NAuNETXfjtu67-qSo69qD4JRAKTYKIbm-ypL36kVoDKYa4iDX0Kq-z6QtDjxXuzqABQVD2fNa48DlnJDQlVu8cRS7XM7nHK0IpuImrTlaBMsfSnzlkpwncs4tU8CqRYDAHBIIuLysEUbqLtIbE1qUj8d2fk8kznWarYk5BIjP13FMjWhwvyQ1gnJLoP0ka_A3REDxWQ9VLlfQzphoK53CnVJubiqYZZ1oeah0Ua7u2kvYNLIj0c2gf3nZXoo3CsCKdbkDh_xmNnFQZA8-rV6Vv07ujHozWN2QMaluOQ-gx3L_GjKQ4jqKZBIn_98x3aavnmpVx7qv5qhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKcZwFgmNuJ2L1XBmle7DSoYhRRQop5AONIjqWw-itifm2XahWV_7R4r7yafTekZhW7Et57L_GSyanG4yYig92zsVX_XRYz80_CrprwnvPGNkxGXCFf2cKliL2CD-UxnfAWKR6YAo28B4mB2ghBMjLbaR3etGp32lJvOOAs9EmNCHYeLOYHf1jSUfaVjvpy1YxOpSqlChagCFnjNaf4EzJ9h1Yjwr-AOI6wrZXyLlnRO2tp8LMuxhHFrAa5R0OtrYjGli7odvs7Dxk6xaY1yXqOLWAAzKArEhIqILQ1rDOhH26dXA4KY7y7-MdKYUG9W4EbfjWmDkyIMjCvS1oxuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am7x4vEJAIlMxxuI20iqXgxo-Cqbgz1CQTI-bPvx0_cgnLZvseqCuV0lXMZjoTqW90zRSMfZM1iapKIgcHQdY8NEzwNtL75PXQoJ-eGShP-fPxAsOlJBWxD2fMqL9-VSthNbMpg472UMCj1Vhs-oJptjOAd67O2r2maEyZ6wG1Y0pFMWQKCXQ1xnvRcJ-sZJy_k2vDQKQEhXfgu_FmoKBTK9L7Ti-JBSA5L0VhB9U7jdqDwrJek6WWj2ALyUxmwYBX3j04PzF82zwE3-m0h0HhWlmhmwYW8Q4t4l58AuauT7AfkfB6CU1IZqzKlaPmqctdFYaw2Ty6Ez8QZWSfwbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjsRlfdRG6w8laX3UBWb7QlGVI2jofdUYPFNU2dMpTBF6ERobruMyVixts_iT9IRQHnuj6NHmMJSQ4vRJsfKper3qP1cWJMU87A41VRSMJRWkKnemz5MkZc5MXcENNFkh_JAX0neLk9GAN1UadwXVEA6JduhC6QbI11pZgTdJzdoCR1nthiN2H4IAhh7EgN9wJ-XlXga6zTDh_Fdjw9W9tluoGALGdCNObk7x8dLOgSC3j-mSf3R40THoE7QfsYKlrm_rGAeK6Q1wXfu4kxRd3To8felhESigsWCF6MqbkKR1PvTmd51uVwvi57pIQnbjpExilwL_tngZmPQH1Jy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZNH1SBckev0gfkTz1T6XtnuYi-ZcfTnyzGo3GRmQtc785LF2Wd4nHKCXfipMzkOely5RX-jv7fWzX4fwJ1jmPDotbf1vOjgJpKMYqStvwr4PhL1VmQrkaOWBrmztcW3C3xgdfUKglHyYO2qRXh-4bdB-T37-LddT88KIfHOXpb--abIVBA1Hp65L0aGwwTMiWkybsVWbQwaDIcWSDlpaqzkrNw7qxwm9dGI7I43N8ZEEO8W5kzuN7xae2omUbVUFo_VP4KxItZAjInrtIkE1uqSNaBNkgo1J-eYD1RDThsBrO0J8JOC4RoIruCGdb63CXdfwI0o5GlnfZqsvHpkIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vjlu7113tGIhrXJDEG_3IIOhpXNibfzIzlOs-YF0mvdltF2LI1DMi2jcneAXibzPiFOj5ZPBZwMviKWwYKPNb79f2qtA5x-Zb2X75UIZsJlUgYAQsFqx89r3dme9LDlc-sz_rRhH2Oin-flr8idE4NWU8sdiF1Zb-afimHjtiZRqGbD7OeZCg9gltRwjtuMn3H6SMoQCbsGn1yovlmw8RS2dG7uL2-twIvF81DIIO0nHjYVWFyoC1tRwR30TVexKEkcpcySoiOCwRY-bwVniGyYV9AoC_DJJpG_l_zjQ1iwOAWfF1NvtCiDIcTAs7c2lHGbXRfIRzbT_0x3TEpFfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFDbTJl3CSXsu29tDv8noHz12F5LpWcEhG0INuMdauMTI3AaxhLdr8kCC7c8Xlxy6nAMpRBSNfKsbIlmRmoQnUd_vfb9f4T5e8Gj1OLZSqemra7EYNxVM1L0h-tMD7Aw1kd3yS8PxchE4DwJmoWZAL3kX1U17Ue8-wXyqN9TBGNEdaHpgqXiCNbEPRnILXNfITmKhqSRMDnr98HNSR9SE3FBlgWTKFtEtukyjXFfl3r2RwImdTfiIhpSsyJuv9TRfGoXK_z_QhJd7GgNM_DSFNiv2kCxE9v2m81GjNuVshmmlzx_4RcBmw_gyK5EKHjuUoREDsKy-JwkP0o1aRK6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx56E8Gkylr_XPioIM7yUFpzn9EjPxHo2enXuRIAjh9WB_2GZ43lt5jbnqUycprKAY9i-lwKhjzWoKQA74UQG8xZ3SbPV1xBDpXbQaElm0vZfv9ByixYz9wehIINXzD_JOs23vfsV6fE-IJEpGBc8x5uiHlyGo7fPYL_fkZn9xiCVk0-JRD_dgPZFHsL6m4TqhmUID6xmmzuiiU5mGuuKaHEGRcGE8ojpH_f_Px4zi0s6JyIavWPJOnXpX9gctXNB09WGxssavlLbi64L2s0kiB1HDV1sYiZX3uKn8z2VLsyf4tX3PFF7LolTSytS-j1jCg6lbo7kWcjSwQ__ThEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=m4tS9y5BW1Mpl0MEfdza-QHRCUBuBLS79ju5vdCg7u8t_sBKM0t88vv8MJh2EgPd9HnItQFaGJVa09NuNQaWelCFNGFVI8196J-9ipUIdsJrKvjETEF5DBW6iZhvdhVe6I1PIkc4Y4aN0Yv3lnmuv3jLaanxYlhFIAyfE2BLGniKjvYXhjGC73Na_B3fm2qn4B5zF6wt6u_hJxt1vjiw_Dd-T_4HoceHeVztCIxvCWq9GcpbJYp4bBK3VljTJM-5K7cr_C8wfk-ML-Grvz6A2pMlV6kjz_lQ_wLzAx9YmatRrx77YQdGoTZ_nTlBq0lnvmNAcdue7VJk_87U84zt_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=m4tS9y5BW1Mpl0MEfdza-QHRCUBuBLS79ju5vdCg7u8t_sBKM0t88vv8MJh2EgPd9HnItQFaGJVa09NuNQaWelCFNGFVI8196J-9ipUIdsJrKvjETEF5DBW6iZhvdhVe6I1PIkc4Y4aN0Yv3lnmuv3jLaanxYlhFIAyfE2BLGniKjvYXhjGC73Na_B3fm2qn4B5zF6wt6u_hJxt1vjiw_Dd-T_4HoceHeVztCIxvCWq9GcpbJYp4bBK3VljTJM-5K7cr_C8wfk-ML-Grvz6A2pMlV6kjz_lQ_wLzAx9YmatRrx77YQdGoTZ_nTlBq0lnvmNAcdue7VJk_87U84zt_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=bycEKOeMpc73Gfai0BZDaY6LkaQYo7MDQ0X87FEzJI-XD1AG4xkxU2FRItCpaozuNouJnxKgUAlgzKH7Q-OBYnCmT9Mtq3uL0Lrj7ZOz350MdvHVrhmHU2G4XmdHQtWcMScvuEysv2W5EdFGGyaRPX334wdzbCPt6MPNAQ9uYBn-E4vvHWpavy1aZBBkusb_Nluy-edbCoU6bisB_EfwoV76anNIUxRxjzgc1iRrhG0VQ_5TBQ3Y9xZa-8gCJriPfnvZgYZC7I1GG1NXr8d0FnZI4t4cAVNtIFTP-RYcCp9fGVrGJ4_QUKCcmfcWLqeS4vXevZLK3Ozqm7-H_NWoig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=bycEKOeMpc73Gfai0BZDaY6LkaQYo7MDQ0X87FEzJI-XD1AG4xkxU2FRItCpaozuNouJnxKgUAlgzKH7Q-OBYnCmT9Mtq3uL0Lrj7ZOz350MdvHVrhmHU2G4XmdHQtWcMScvuEysv2W5EdFGGyaRPX334wdzbCPt6MPNAQ9uYBn-E4vvHWpavy1aZBBkusb_Nluy-edbCoU6bisB_EfwoV76anNIUxRxjzgc1iRrhG0VQ_5TBQ3Y9xZa-8gCJriPfnvZgYZC7I1GG1NXr8d0FnZI4t4cAVNtIFTP-RYcCp9fGVrGJ4_QUKCcmfcWLqeS4vXevZLK3Ozqm7-H_NWoig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4D7YdVpbv1yL6Ge_LvJZQLqYAhIeP0WgIzjhbPrpLTn4OKBmcj7rrvnyQ7Jyfc0g42rFb2PDbA771DtcT820BMNSe-o9njNab66PVjZd3JayfoDY-CvQ7InYUxQWZO_du5NtcKlC_Kc04QWZeIButU3wnUuqCY8tsomvYCsT6gwkZdktMnyd0CtekD4_Xg11HzDnBpHmE17cGlxZIgzoyd2iDMxB2EF_41eYlNxJgdL9b8m3dKG0WRyqebD_PVEeezeLobJZqs7-qJXEwgT8mbSiF-nhK0PXyws_YTJqRStYQ4ZdRjIfFeCSLNZr93HzUys51OuB_GnJszpodss8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1viz8CMPEovdvQFYhT6WxQoLW_HLQv-WbbjqsnOFWMJf6HeAr3VuVBkwfDB-IEXoSG3G5yogpQjfnbPX8xd_SM9QWFtNKVXHImbs5wXaAOlGL8P_jUxo83pWb1HHXNRde-efGR4deaPCU3RdaRHfqinU4ZLfarc6svPMJtcM3-HCValVfnoTmoY9fPghMwV_LdyDWjlOD7hNqnSMrexyfRD-BTNqpXYl9yIL7_Rmrwjh9KDxyojYZCbixnaXDOB_0unHxUuebFuulAhrtUULQTzL2GRDF0Pwz793wO4rgIUvB7jsLP5bdlnHDVOOhNl920kq-xyJd2k0c5-GsGiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga0arctoGMMcgpECZ-n78XXC7HrIFCUCClBXkUVxyq5tVHkSEP_p8FH5yJY6vHJe95yuPWP--re2fwc6J6UmzjpZymxap4FiPZQG1rs3CDMCyeU-6ZEYZ5EJ_2Kk-_zo2v4FTRfMF7owoGeKwbNiJY55nggF9O4HtC_kbw9cRKoLmpZgvjF2pKWUIHXnB0DPU3w_vifFJrJklbambmbF4iMEJg5mOjX1hl046D68ckoRkNbzn1T-K0LJowoLWAJNXY1H0Ev-2r8UUZLEq0a52SLcOdTRwMFXkGlJpMut8HgboJ_m_vNF4N6IuaLOebF9eeAzD13EKuX4dE-YJ0LHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn95FYV8-gkdLMHlB0QPPj4C1rYYXrR3Q1JIJO3WpBEwopWepSJmJ0z5yvLrWM3zcAdlL_al0n-JmSPBE6fTkuxDNiufSTUf0LSF2MdE63y3wBLXw6FKcjDaw3T1P7T-_Q0jZ1jax-9GyJRMtdmtXLR5Pscf43iPBUbdDSX3jFzVVFYUX17095d2jBIiecMPeAJfBRRUj0ZKsANbNHJ4fzE_VSsJWj_Uq6wP_jPAH4AQWET7H_I4-wZxmxGXwNj7rrGIP0jIDpAQD1bNN9IinRuSszFjQEDdUeVF8qrRNz_CjXv9Hac16mO79_nSky5bq8CAuarfp2TFwl_yUaeoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7xkeNeQQBi2KhIpEt-g0xGBbH0u6mvt35hDqES0zvbB4EzpcVaNZEbvePhtUyr8eLiDlD9TrxDVgIGCXLBtBkKgM_0_iN8dPMNXo0sM2U9JUcK3RBybTDe7iOFgQpVPGpXG45xzwJpXrpwTjLKT84wy1d3YMdGiiRxdtrH1h1OR7gQLGIxpJvgkjgYCsn0_kHe1qw84ViyWKS3mIyYcIsDlGuxmTcByvii0D0haUmP7Fptthew9Bkj2Q6YnG0vDTuPo51su_rB549gIjV2IZtrWd8mKQ9z59gCOgRPZmTRu4ojT5JDgYfQ57sg9Q7Ld4_YRMS8ew5M8n8ZWY20VYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbMoiKAu2DPqO71-DxT_762g5jvKEKaQ0gNZqxonGbPn_PAwxR9ZwZpxoEMl-0045tjmvQAGvxIqBqa1jt8fnsBqSVh6Pfz36OjgtXqABNsb0BrQL2VPSoh_WuM071_Z62v6zNdfaszFAKCnRg1iVLk1zwGUU447jZv2KzWLscSod-Ttn0pX2xr-WVzP1QDkPQGQ1XbXl0RdGf-ZO3gsHia8Xe-W5qCrJdBP_OoDG3LWyYPq1vlm5Z1VxUKcdyQWEa3hQDnxPICq2eW7fjbiXkHt2vkMc-61VCwKyEiBPA3CUZSgowmNebR4WrbOwqe5RHuvEK3_SvfCftrAzkNA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mG6D3SdLKdrKCtzoVAyQyUAaje-iDT4weQEEH-DCF12gLPOrgOw5pNpF0V3sQv-jrAA5693CiqbNgfdNvZ6kN47uUhmxi02iIHldRoP48N1PQ0nRtIl4FEby5dTLgq1axwK7nTH4loLdSJlmjLuwl36nb6GfKKtDV-qfOfOHH78q-5sWKQUE4yHEj76WEXkxBp7SZu6falBeqGr3j8Ep2gicwD-DLRUJE4fPw4YU8nfQ-QQbQqPhw6zkn0wM0OfPlWBtPDXO_7jbKQB_f18XNyuUTRq7ZmFR3qjKREVqvvdjU2RG4ZxxnprRNfPcIaxBr7j0gEI85EhGft87pSDW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chu-MET1pidUpjyihgZEBfj9HTyuCsy6cGxaiWZD9hE24yUuznFkuach1X3i123v8A9x2mObG9M88gLN_YEDxMKrclmudwiDOMDGNaFqlXywTd_53LChPjZDEGsFKYuoK3Uciw-4EKXTcjuloLUAOIVf5bBNYCFc5Wi3tZwr37rxWJRhiplEbmfawrFMxbx9W_DPUEtKXoP_KBm4mjO1xk0BFnM5miTS57JW2O9WH01yPuhskXIQZsjDaoyn7Gqz0IOVkb1jqP8P8W8VLgnxDAudNDoNo9s246C6bmmOz4vae4uh6XyEC_7uP18UGTIBwsdDzMRzMz6F7VQYmSeYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrnDZxFFZfCQcOgfCcXLWO7OQPcOfWcSnKImGXxWl08R9tYZyrXjO4wTRGqGakKScM6-XUNqVGtWgbOiYy7TLYrr_FFnfVyWDJ28o0tnV-NyCcpV7tICPxbwvHmjSFJJcAhGuJn-PBVteMFBQVV9tptPhKD8wn_1OEj_AX0ndfzwbSeAxe5Y9DS28jRKtezidLgGE6oJbay8vLyDvViWuXc90xrlPBeCOcegKFo5qJ1TX3i-53Cy4JjMKDWQTIFuQ6cgiJvyKHNguVozkgOxWoS0HQ-8pWgHNqRheSFucT3pbdQ3s77qTBrnpidjF3YLXart_8uatICEHH17IpLMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syGvOwslmDTm1mjHi6PWvd0qxnfa7-FKZ9eSw_aL0WjKb6EXHIjhP6flsih03xsy8dABzPVUFlOo2yU2pc6hcf2_28k7fh-VGxcgZJVLuZVx-TvY2DHJ9ZXKVKBXxTGFU7wjG1N2bWykQnnDUhfiV_Ie4qKeQMxv-0hg3bjjX8pb-F98MrpqmLV7DHITc5BCcrpnjOIGfNrsP55BEz6MPr0dIN7P_kmqa7tKqsSxVtstC4empyasTjhroCcjq6TH1vofVpSiV0avvrsIWVU6bz5hmcbCdS2uZisdx1M2UvgDhqvWhIMm5LpRzc-eEPNe_vx3SIHfULkkSk5l2InTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnhMPjvdLCunuLegHAfCLy7noKgVCLp9vI_jZOTim0t_tOINmNdR55m5LOyR0kt4I9RVkjMW0ZmkYSpoMR9v77zMoeeTtIn3rdU1G9gmVMlntvtKKdseQiZ9TQxotbfoqXG_NoABsJnlrMR2eZBKDWHA6CRLTkfOvOFXzPtI0cOlMZg7ogEjcu1TFL4ZOzXTd4u3qSphxEXLmn6Xa8ubjqbgTb0mTAI6H9voN_3dPZaRRQIOk-RGUnx6_IcgLCwC4ciYm9hXP3R7GEXfOMP1t85ROm4V8qnfZI8sLL0vZStpc7u67gijqNA_6YUI1ihZZzMHOC6Tn-JK_c2RyrVg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLnc-kXU0WGYt9N5I2ZG12K9Mf6peMR_dbgqTUN634FYhU-f2QRxvv-g72UFrm_pW1OUFEHcCKrCT_bl1Z_Invx_fcSRe87aKfWuH-3UfOYz9RDSGSFONJOhlXD-2CSBfywDX5x80IywHO4oPB49b3_-BZfFB-oFVeJ0ISJ4gB6YVzoRBpBIKPWIIv1q_Gkpm-Db2Yvjs1JK3GAo_idu3kLQ10kzug0lVzRNHKRAOLTmUM5AaQ9kDygkXvLvfG2ZHsAMpzHtFOJWJ9WbcMpF-gtdYnKf8s0ajyslzhj_Iyh6QM6_P11Y1THujy3ZGnlEPqSkHnJMpN1S9YEnWrBwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnvugB_8GtgdkeWbrs7U49Tj5_XK_4TMxKi6qTzjB5FD2vNttICkMs3294Bpk_EYwN-kJbM6vYWpdg-paKs6vGyMwIpBC_iuc4k8nfCgt7dCH5O1XqWsjYJzcs9wOEWF6U3NCjJQqXFw24QDLfuTmXJenwj3c3J36mQ_BM5cejDwf02XFb-beQGmNGLNeDCdGkDRCvb0wXwfccKVLhO54WKiWAYv27_Dt9gMRp4dsfRAyevySQp_q3dM1BvpQv_rUOyXgX4MwqylEOUtqK9f9L7Xz2Idm62o-HD0DA9M13ZV-I7TSj9r2S3R6cYQoUj10v0oyQ8EJUcrPb2XiSY9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMd8nTtNPRvssKP4_R8MzFYgZUf9OkJCCsVMXg8SgJATNm3DVmcQ7a3Aks8olsuRpkg8MQRHBVEPRf_n3UFKu-JkkAzD893XqmGBlVd_edTKiNfEivsYo_fiOCl-mMtJNN-Rxa2veu9l7GFfpeUps88CBRsSxhJ16cIoTQf2cqkPsWdxsObyuTeLVJvichxmWAUsm5WOGgZYlHSSbpeOtSrdqkzW_kXtWRRPifS89o5IpcI2MbCjHfagZ6x1dc1IT2mXxH9kPZflDumRz7lMzRQmHABVR_svKczs_-8xWMLsk0BPpW_2sX7pyyp3dooRXtOoBFOwjt-L955MWDJzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR8iZ3ANHqMFIBx5uE9cKhQzBiudxvuRuRXR2B-W2jjc_ZeZTFhxYtidjXQefSs0wYB6UVEiokVDA1ah5VT6sn_FUmWhtiw--GPZZk9XyC-vbPBcRCcajFzGENn-inNvfI1Gf3PBaUEkPGr7wQQwN3Og6FgGLTyqkLwOW4fMa4OoZZOMN9KZC6_52CqOLOuYDe6_JQ9RlyGWqjkl62Rw-u9dArR7045pvVvs3nyZNuE8Tr2tNcKCAHLSmxfuIkxdQAFWz9mgykopgBp9LEuNOFQ2YI18xV7vCRejeLm_1nbzOOWhucTwIA-iVzLuCEANjpgeGlgaY3-CItovRvYz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPYPdbC1DUtZDCx8KOjMXFpkyIK477idCq7iuuMy8bOTFMgAljhXdM0o2g0iOQx17LLl6ytd6-qZVU5c2lKOmJf8guhAvSdtMPXOeNP1dUkMsQg-xr4e93AdZqKFjsFkAff_eo8a_GoV07Om_VbADCXPmnTvPmwsHROwf6QhCh5aeOvRA28kFkbq7CEALixLq54-ay7s81d5TFEA_6gMN-5-p3bcMyv_U5AaYYzHy8OU9We9Wjp98w7sVHjQDiXTY_abytqCzrxyL_UysRMo-t-X3mx2kBx5joK1mLxQbIGZH9Ep6GrPMfdUnOpI1qyF-W54CEmnxXXGzEQJfCmGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeFJIl9oRgJcZrNV4xLb4w8lTgg1iRQ1xXJQcHDI-7IWAgG4bwaVoa6iNmAEfZwXwFpmyjAghuxoLfGzpPgLRNrTsjBsDcoGh5L1JyqiVoi_3-HMuCKIJdXEi2ezrCYAyorXCjQ6BS5TTwF97euawNRmMpqzTgsGkrug0BWCTSM8hek1_ZOCPHbgwpM8FLGatkFxHsebFuyAGaK0nQL50rw17GYZYFsF2PubfLp5dGNN4P4euk9Je_Iqj9ZN6gStKNtulIPgpk5gdTARaNgjy3Ib71EMof3ZB5TG79FdrqjmR-tG2QSL1Ylvn0HEdWb__I4KHOQc7hztrCqLdZ2Q8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM-ZMgIbu5R04h1EWRZLzdDgqfP5MhzxoGkXAWgpr5bu0cbL6LePfgK4898BgrfFhH4qeX1rz9ajFSy0Eo8xJf_U-1-CnHznor_1GYSjuG4iDdcLh1JD-cY5h-qu9vsiZcL5RHlJzEqgsqNzTYHUJUHtL6kRbqik0yWJ-JCugBkaniMbPAzxumudsWRvoeWcqzongEvSGepBfKqAHbyukbVlewvay_VKUVhQQ9CeFRER-jJ7cE4_NnT4JnHD5-5jNDXTD4z4ZsFG1hHuvrzMfwj5TnS9EGWYqaRbSr30rAA9BVRwMgGIALW0U2GwAKlfc0QAu_At9AJ-9KRpDxCKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekPkM86xPoLgamPOUwyKJYE15a1yb-_okntloOaj_lBa90EJ0prSM9qm1mrCeePmD2zkyHA9RY9XAaPw0FxQv_gP6qwYmNx_iVxwIUGfCa8VlyejAmMxgBsx2pFSYVB7enIGIY9vooZVoj802JlJ4WgW5-Wz-HHpfBl-78PkBnH0r3qTbVrCdpuQbQbbiTVMDgerYxTs4FToQa5HCg42TLnSDwnv5gSkOWBLXao0tk-DjYFzHZuL6bevWdbg5yyGb9M_P5K1DaPVVDLX1syl-FT41KV1_2SEeoFo1dca0K0t9MSt-DPE5TBnEXmAEao1HGdj4OVftILVnIFvt06kNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs1i4tPgvPZD-tQsAiFGWjnylTgxYUPis4Spp34MqRC-N0Gxbg7-vHhDdqSF_KM6VDksLDayF9qIZC_0Ogi1S0A58VW64bFQw5fi590qtF56g_JEV-Qe5CjWdGnphYSqU4U756VcZVc3UL9fTlqs0al95jRVsAfu33vTwbrwnUdpR2TTKq1WrthcYmRKtmy-H3AmUexiASn6YAMMGa1aBEXlJsfmDffPRtoJlunwxIf18PkhU-DoMD_spaeGXk08YBMITzbnNVQn5eAMb_Y6XuDpb8_AHTKx658ySNc9Lk7-jBmgtmUeUq2f1ARhT-DIdJ9cXhQpFW71dbtnC5PqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPfIZad6Ill1GruSaPXh-_WE_pxLP5yWTnrCMlID6e32Q9uhuKHhccptAdO65nXyr3zJ89f_Z9pblr187CQJ_MCkxhro1weHPm-vTVSCdaplnEdgnP6JdWGFS_ogOSpypRJnLCKpcLM4VqfJdp03YH2BiG520lzUcvWJeH7HP6_aCZjZHg9ohj093ztoI0k9lzUefUPJqXPVFD2pgj5J3if_Vqb4TSmcxaUWAVI9dRDJDX3tgN2yNZ-Ngl43_L39OjcE0CCcd9XmrxIBP4F2EtkBcgAAEoqwBjUKl3T7eJ5XUY9FaRw8YTzx2ASM2iin9t4RSAcs7KG4AyAdNT1YMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZcrlgBIl0DLUGzFT6hkCX735AsdWmX1HKq7DLAlbERMdvQZO4G6TiX6dIX4QE0cqa5A5VROAz9jTu5TTliJ_BGuLpFbgEBzy-ky8ZWU8cesetkF8urfI5uqT-p8uRTGG9JBbMJezKD5EKMhXdoDT2Q0hLacbqIYzT-1qRbrw2gSspjr30OBoqwBnVUqr3DOYDRyUXyYWjfihZckzivP4KQtdIPIe-Yxq0VSXjIG6XSKYNXtggTdfnpHAL26mypJP0dJOhi4ftVMkZyVFS64zpm_ia4kAa381XL1tBjy7ve7FXbB_VZP-El0h9xnTOVXeCoL5c5SC6fOl4kpPoqpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyW8HOzkdWAomi6BKY6nzaY92F-E6nYDc3rs6cGjR-GS7Q6WNfFe2rR-q0zIwSUxP0jCW054cDaGHpj7vSY1uff4w6CiTAgq_-2YoSBJOmaJaWG5SLku22spHYyy7uy5mNFUY7EM_-5GTDLrD53-w1NEm_lHuyB0baiysXcGwfeK3viO5NDCdy3Yz6XspIRDd8P7xQYkTwBFD9ZinsI2ckoEALK_cEjZafeTu7t7Wq-KEv7x2bRL-D3FugOtTdTFnOFfzLn7SR0NzwgXwbgSmupz8xEp79WwxXl59sCpfP2by2FTDlDWbY_aDC_mEa-JClWbwF9CMJygAlHFKo1y4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuxJ4hxTusjz1N1TP--1udXeCwsSMqkQu1nqM1JopcaT3rehoyG1QYV2uZA2x2y1gE4gyDlvfgmxyLHxLmYAm7NEjQl_QSO4K8Ey2v1HxRMwiVlk8QUZz0jeknVJOhufgn0x70pljxREfAP6ZQHvf1Cpz7zUKhXz2ap6LKNgHfValdWcS3oEWVPUdYBa7r8vCBoAld7Ux1PMJIPyde-lzfmaLaYUg0L8-wWAX-4l1RYQ9euUGlyiEjxRFGlq11R8_Y3W4ovq7NMAz5hGEDb-zpKSXShxU25NDmr3D1JJPIn9S6RgUTyLCz5i9QkeMlrIHRGi6xXhpGqtr2cUi7BELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eceZ6zb5yTcVaMUfAEgUvPSijk4V0g6NFRjhhaejBbNx7EawbDlMxnwFvp99zOL4OIP8Of1zIG_Gy_ir4K6lpICLToRDFGuElVNfUryNdTvYyTU478_8iPlNhPLpO60z2dkp3w9usY_KJb_NsF4EpSpqkkH4WYYrCe_FgrcfQHFlww53pA_GyBmFOycaBVYBhgGtFaS0kABike2Qd84aXsN_cMhFty2XAO_FKP_SPTiG-My6DZTxTNp7t5WHKsJPBrAs9EUgyeWdMxBEYbI3qbDMSPYw_A43JnF1CZabEjqyZoX0hRCn6dpkh94Se0cjyZ4ae47NhSfGDQKX3tqQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0JYR5ngf3_sZF8qV7V2WLqYp1Vu8kvl16xqkqIu0vYhtVj6sj-lnV3eWHTCs2EPP9IJWAFZfk1TT-LlJdKdc7OKema96URxPW2krub9PiWWpCNGHgbZp5W9mSHwhjG7zhm0AysY4RyrxrSOxMNqyPKHWfIcfhS9oCCgtuSGiUmn7azS61qcv557Wl0c34kFDL4fYrs_kHWMzTxvWvJgb9FkCCIG2qasQyUSOHoLupMZkSU6GSFxsWhZw93Cxf6kQbG6IbPN_yN_F99M2Ili9HpGS8EYpu_m7nemkGx_xw2fcLqbv5OrEMa7F4vs7oUhKDAU5kFdRp8VjaTPzJzopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANWph4Fzd1RlKgdoBAcber9a7flnmWjPxnLJ5TI9iaK0wj9-EpLPEKoyohaD2IPhZvmezOZx-xJBfO0wi1ZbCCivBIlxn45et-NxeWDBe_2a5l4BB0E0yon41Koq9gR1UujPrS1W33CjQkzQJCND4NcWwqH5M756Ntmog8KkgW7PlssGSUjI-hTwxav-RaoT_ruIOQlb6HVt2r3Rb6710LV4aOztRinWvAsEUecgtJoyMGcx7n27FC3Q0coESZvBfhOy-il_SzAVlWWJG5mDaTJOgA8brMkPfabG340EVl3RA3dEJW45fNw6wgX4ZbHXXq_0tVD18OvSxHTyeRW3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qllnGSAaJbVL2KhZKCCcAA7LyjoyDVFb4BzKmmfzLo6fOaYFvURvVkNGo1hT3_MWL3N2eXNqKL5WWbcwlTxRmkGlvfP26FDKQ7qe8Ih62ocjvTthWGq8LB9jiftFIORC3KLClK2g8CnPQHB2xON9dRhPN-nNjkZbPRMv2gouZ3tdLNAjysf2S7UVmAsTD8nLI0HrKaUqjc1XEOlAnv4tZ1QeB6YAxbMmMqQUGoiNstjNjGlpMhm-INxEMhYVkIhuXsVw_i-tW68vDlNCvtOHzfoymOOGkElVqotJdDndWpUjiIDk0Y4MY9Ht0mITmXN13xLTugEE3LLRi9D4hHervg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=Zp9Xu4Glfp-c_rTkYzkkORLqxBD5IN3Y9m_kDBa4Dd5NUq4hmrQgqoLLCrpEoy8SqBUBpsPUYzO_mHPuuR5ZJDu7bsShqTfp1BYz558qQeLs93hREORuxfBaTqbWYAIp3Bmh0Bg0zCUlt2igP7jQLSDsdBD_WFGz-bpAQ49gHhGRzPpv3109vvuxTifa6TqRy5UEBeh4bZ5Y4AVKIM_y_e-hYIKBJEdLuFgVNbj2i-esAlscDqpE0C6-zdRWaKEYzDJhh-L6fgraMwHM5gPyQRBEcwVHRwIVbm8X3mhtO8kP1dtTCQjWuoWRDEHgp7W5DzxXK5hixvaf2MPlT5afIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=Zp9Xu4Glfp-c_rTkYzkkORLqxBD5IN3Y9m_kDBa4Dd5NUq4hmrQgqoLLCrpEoy8SqBUBpsPUYzO_mHPuuR5ZJDu7bsShqTfp1BYz558qQeLs93hREORuxfBaTqbWYAIp3Bmh0Bg0zCUlt2igP7jQLSDsdBD_WFGz-bpAQ49gHhGRzPpv3109vvuxTifa6TqRy5UEBeh4bZ5Y4AVKIM_y_e-hYIKBJEdLuFgVNbj2i-esAlscDqpE0C6-zdRWaKEYzDJhh-L6fgraMwHM5gPyQRBEcwVHRwIVbm8X3mhtO8kP1dtTCQjWuoWRDEHgp7W5DzxXK5hixvaf2MPlT5afIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
