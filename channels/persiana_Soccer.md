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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 21:15:36</div>
<hr>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aclk6r7Fp5OTjOC24oGlm_7PeJ7yVTqO3EKGFQLoqeB7xI1h4VTgwEJ04UDVZwm3uUHIc6HNkH7V2eB1r9VQs6oAUOc5YoK37fPlz-xvHL_6gpDTtgZPguTt30iUheZTVsTjL8z8--zd89_QOLU6MR631m-2ldR7kihrOem4Jttt_l2vFS9xqxAjVA-Hs0FLiFRTOqHgGdSeSR88aAATdMkE2IazUOYn7kuVhzR29k4Hl5X9DtSpZVd0ZAKjoc2e7HL4si_j-DIcdaGS6ZNvEp0vLga-kX5dyl1qcC6Rad1cpCFKcn5yCaw5oVWscrfKDwJCCY0kflprNxfF3s_zMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrtxX3FZ9ivxfc7jxd351GvB3FefXYgYXSU5WXsYsxUzSprVQvrqnqfYEaXp2u5VEHxd-DRdRe5r-YYoVlJlD3mFDtqATm4YiYVOJcgQBJpOMVydjaqWyaZAMqfTT7onLG1VPz3uZCLxfP2JtdBTBv6alLU0FBqZII70Q2QmSWzN5aqE5kUo3wNfAcjX3bvSFbCAzKMM-bhVf-OryZ1eJyeNqTVisB3u2zBxI8CERQMH0STgtvjVAyeEZGXKcpY-Cw-ijvmUQTxCvJOnYh0A0sdpPNFNhCq8Wi5_9H98YjioIjOP8OV4tfcRr-C4IMWmZz8GXKkGKpmOBR1k_FdWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8YQQszUoYzFSu4dOA5Q8xha25QbeQLnnm8r52C-KytrlaY4FdW-udiQzCULfNfNQALj-gJjxSDkJtlbpaQMk80NADXrvnWLTXPlFdgI1zrri8X0T1P_lXMpThU9eoX19DTTYiPoYlrNAjubbqzJRkAF8T__ggJ6TqEfwplFYdwqToqdWaXWw5CGzXq7J47SHOPepsWFB0PI0xkZKsAS8uBqokK2OhS8rQ49X7LTgf5KciCHUwKGjEo1RQt8rfqYgpX_yWZZNmLeYJbKLYUyVkA6gMUgKtxL7iqr4kY4ohLyWczyC2Kw1zfJfz4lR7qxnmg72v8N1byJPuE18voxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7QKJlp7UmH7NE8RskMht3bTHv8sdnEcLALUowPGCbFXQqM2VwrZHKMSdTV3r5Na8mruNCNu5pBEOU9kEzx_v9qyOHJmvXMJIIhnGoTfFjPdInkXFxnGcpF7yUuErhSO0Fhb3NctCHjLZsaAQMkHADKh8UKhuVoRDtoI5JPrMgC86EoRQC39F1Zxw4rcv198vJSasJ1biti_N0l6UGybzMRC0_NE2NOh-_JD7I9eCT9yurztG5a0g4UVaH07_6ZJMS-7a7hQHQ0XBLdztnx0HzYsdw-03J7Fr_LXZxEFgydyuTgYDi2Lz3hB01boCZaMOR0SY32CuSqerm9tNbjAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfyto_CWiqKMnlqFVzm9kKGRRQgdX12Zn0RPKY3AuZUEFDhexXbJZa6ox25TT2Xbj6UzZn1202C2YMohvUpEKOmV1uj2UpB0feMyoHWPLZXzLNRqqy0PPv25M98stV-fBtKvH9IW0DhBe3tUmAbeI5pYBEZQRqb822hcHgepNqdqtRJXgQPYG8zE-9MNKu6MlhoYza1YKdfHUcGMx1yPIEs-qJF9IGJlo-hSp5chtuNJ8-03Jq8iO0vGMSuwuv3NuqXTIrR0w-E5lkdWswrN05qAMbKEuirggRH_nbw3IPdl4pB1RdpG6r5NbuvVTR4CPwcV99rPPhJBxbcaM_Ao7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuWK_MJGyya90dKu9jl4xK337fVPM4EGIUlg_HjjD9MpA4uSF-5trAYexxah79NaMItmjpeQpwXxSPB5FF9bQPZOnWgyA7tYaOE3DKVdKv4D-4-1ado9KxpZn3z0ubnZ6jEjxqtFnTk1z6WQ2orCHlk4fSp590DBxzeRyFIvn6CxEU9I3yv7Kug_yIrsDRXgL_YzM2fS5tAlXHKOkGPC7v4aPR5rF0g-9_zTr5CcqPqycOlX-j2U0E8nFDAlceS_W-dih-MmK6Kj2uW-RToMBlbFKBMLpP4TyLH2UrrqlNGTKqdyJWWOvIcWV3D7kwjYRkpcRKamc61L1XJX9_4Siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1vD6B6GkeaK62DLDfOgWB3_20YtnP_cnFCscG95Tb5x5Q7t0ZpArKExp5BCwjMs6TCMwujWtniulm2rUlmOVjD9od2qEEnRwMi9nKJQeF4jC1-z8A2ffcKjU1SPJVhNx2tzfqbUQRDkZN9-MxNFYk-RnzZM0HIbWqhP7gBjZfJ7TABYNhXl_dJ0b-7XHsUqWye8qeg29sMqDJTG2sW4Jk-gD-IzcR6Y_LV4CdnStc1w70zHPfy5rKyhOp9Fmp9hgdsbthoS83Xiq_5WD6D1fKF-y3sPCc5Soh3YjhGP9IUQzKttcVi34fsD55ySfo1gV0suZdAHDQMO14UmPYSQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENVP1cJbcN47mhh1YBHzPPzyh3Ny2UL0QybGdQaXGwiF9-UA66FJNZPuO76UAplslcZCT2uDIFFheF082pApEmakAtKn97iRTmPetqmti4aV955vvVhGg1OJh4JMwu5aGj9kPLvpmnfK5436MxGPtNY0rgQpmNdK-rhi-mmJHhGo7PrcaSvf71k_9iEQPBUO_Q8pGVTU4RbMmdzRzVraxsE8ojJZDwsbCNV75yFc77lbFpYRJCfM9DWE8KZsqrY_lJXC5P8M2y16sSaZ-c9MjvCQNB2b-eerlqfK48Rsa7mBMsI-HkKrjvP3yg8bP0iwNWq3bBwjMWmTsyetQsxNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEyKeJebEgefFkaCxtgEkA1lpV37SDo1xrDTTL0zzDSZaZf1k1K6E5BdzkBNtld2KlPq4WFr3N8UhDhigSUsxqqMjn1_HGQnR9kxNKeJRF2-N7t90rt3chT8c4B3ALEDr7bLXctscaDyzm-Za6NX_c72GR8DaNoubSj2Xybk_plyWlKkLRyD0t181PU9C0Gty2lsOW6yCx-ChtFNM8cShWIeAHZqbJTQDGGcuEn5Pr8Hrt9UWlx3MmM2UJVosGkFnJv9SpMFNZUzLclAw7o3SokiZ5qOKGVJ-e0bZbN_Q_R5ZrnRCyKyxU19THud73h5imB0NyrosI-S64XAAB3Xeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uu8-0UGjhbkaLewHhvfUnByqwL9qby5wZfbWlotfuSU9fdOjVGTCtVERGPeTcoprF2rgAPYtBbgezVTYjY3-0L7wzde-dqlIiRDlSk5o_ReGrDoV3H9Eqbt-HujyYbNyqFhKuq-2_SrqbHSYXoLgicsbl_7VPLv-nXpSO9hoWN6KiOw3G_XPNQ-Ibp0VliSE_dQza4wvfeTEEDz-DT8HuTby6m04K4C7TgczmJUH3QU9mWEv96RLx0v26__lDd1yCuYkQVTo0SAA73lJ7-09r_N_Jg5ZELr0QbhCj3LzGE3og8TDYvlxngPlWVweFprdgOYEb3VHr3mBR-gsTODciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg1qOpK1HQCpFgFC5ch8R0EeWM3aC1Jj5nekXDTk-oQhFFmkbn4JJYTITKO727sb_4iftPyeG2bxNmFY1Qoxhc3PZagTLc3Piq-0uoeKfcE6MpK9UgAzAIuNuLvCMJJ9l6LrR-me2JHjq0mBit19Kx0wGSrm-l1VgLGGc7v0prX5cgdLu2QtyOOowrs6qMMENmBrDPr6C7T0KJCO-aDMKM98X6L2R3eDjNejuAEOrv0cdvRafyI9rG61UG8YzwMHm0qk-T30Mkhx3U9SIBpYQsQEyTqn66y4HgTvTXmyCpPljis9WsK1I-PvI83C5YJ8Tyb5M7b4ounOsM8aq8sbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-EpLWKuf0SXX5Q9g639JYCYs2WMVjLbHIzS4jIrFdhVGsG4UieZ_CQS1qrSpVzUJXByneCTRTp5rEZwMVT8bcL9_XmUheYC_ztvkeLUzG4CLMuMM9lIDRm4kFhru2-v2gO5RTgxNk-cF-GnXZimYky_6VwoqFeD5U66vSAyhHYrjkWRRA7in11fL_UgyVY-FD8c0rO7dTTPhg0KWo19BpSbhKghc-XeQ8M1O5NXFQNh58MncBuziN2QC9_wYUtNpP1LaKnxl1j3gVZWMPFWc9MhQyltPorTbHuQH_GLIgVdpN2DR1mspXcjac_F-YgQiX9JrKd7EQUSj7E-fet76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6iTacoSV1zuwQsabZSp7cWK4BrheeDLmto6NSLyl_eitLDy9FxG7jxjTFTyGaMsCR6pqfB7TTvnIcTfGBx-YGyJWndoawxmyS-K2OYy6qd1i4S36cUz3csGhgxQhfq1ikPQKmeKlTObejnpHxSEtad-uw0BP02q5Y6CGpFIWuLAlftJ_Rf0PD5Y8rElctU5mkhO5nGURL5F9G2cbg2yprOtPADC7mRioXoTFKRPfNCkrD9F7ayF9WYojeZ4dxf8IcOFOWJNkrRO-_ZK4fuvC-yfQQWrIPapqQp7o20TwjJi1_tXkLdlMHHd6ygd8oKxUW_UJU_W3MLbkkZuz6FY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpdEk8RIsUUp4mbJJ8n2NVWRUvFWBO5HVxl2oL5c99cKxjtDuQNfupxZkMjBunVulf8t76P7GGTLl10fBhmskln8jqURMQdd2BY2w0tn7CSHlSmSUP7mH9xPMfnaAo5bhda1WoKXeoc2QT4ya7mijQLlMnDyqX50yyyj9KogdLAt-Dy6RmgyaCahEXrBvy8fI8XIT2jE_Az9yUXTotxPn4gzJiDIvhrO_x92Nf3IX06PjaYRLSXyjxB6KX594tmgW1HuixbIedO_qejaqs2i37utBRnkJ3GmcqTQbSdQvmsAdd2ShIJ6QF3tJKUqRmg55pTL6Gb4171OyCQYiATbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De8xmqfelYtdE7kAU27yM3upHLGRuIAVu59wPDEBEnjINldTeK1oMdOKl3pkTMToDZSm8OT2rjl1RLFRLmk9n_wcHL8OsECbcaQqcn4BOMKN68OK1kjHb4KCH2ZvFl64aGfx4_UUIpo4-ScdBhUYowIf5DCJvm3C3LAnze9vkStEmbvglIS-vWQwFR27usI05W3BAxiJ8OZDte4jFRcKw3_5FkdI7pto5zUkwMT0DgH3Q5Trt2LGKskP8JyKxp7x_xuFnrNSGEyHhyPhFigNRHnzptFkvpGSLqd86EygEKgW_D_gVrwmaCmvc6YRndFTZLWYDSjJD6yODHty3Y5dZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA6KKRUXJsVzi1aexljtT9b1dyuuES9fI31Wo_RewXu-HJ-5MQpLOupKZZRaaw_8ZEvcfRzpgkPNIGrbw5yMKg98mndSLP2WTcKBwYgXbfUoL7qeaG2_eXf5VaMQ4_d-Z8fo9HH7iU6PyzZNF1u9M-qtlYjkwzriLKCVhb3I4RNTGreMOeRixL8_SsQUyxqr6GkjEKaGCfaOnsfukpAirF6JrjlKIo7-HZ4Z8P7bRaMQCs4V4qJeoRhj2xKlk6uf6GA_qSDnVW7Ufn5FttpvAxfqM6OitjF_msmU8BNp-fMHrS0yEOyhnmiXV9m5Gt9ZVsN5KIX844hHB0pepobqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqicYASW9B9T3Ua0z-s9Q3VVLnasml1uorRuw7W5nJ0QuiCLQTQC8K8aRF12PYIr-cXIM_l8kq1TIcGrQ53b-QJK5NnVPBrBW1QWF6z511HEqnOpVm_SJ8eABnameckWqNk88Z96LAnHKFXWoRLhVO4JUNDiR2rURqGCVbbNRJAOe2mznxJp1vaz93x_NrLNUqj3LEBKrn2m4Q3M_J5zZ8HyHaSOZPfrL5Iu_L7EUNXa2TlNIM7FSq_CiSWnBkPV3IJJ8rmnZ-gxNlg6o6LLwKzEgKnmhWFLuJeYiQFJ1JuNPYs1ppYLRdLJUN87dF9AklKbDhgv_Wkh5K0JD4YhXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg4IOQy0Kd1_9mlj_lfwQpqnrprn0od0z3bqfhZZWs4kB--kCw-bUZSPI0YILtLI01Rz4_Io5d_wqSPBvYay6BBvCRA1QuLBNuGmzE8VMBsBQaajK9DiVxIq7xUCZGM10LIP7FFAi-dry2U8i3oro-MFSmR76tU95tzdrMb3IBgMsxipgcBaHvG8yrEfeVdM6tY4p0PFEO1amSmRe3frBU9WXvC1AeCo_AgqgqbYI4eYcbOgUMmtcmmPerzEP9Hvsg6uFkOxwtxhvQv99wGX7t0l1ihrQjSJ8LLMqagaEg3KgX4Fbj_DAPtX1C4P_7ISAl7n-_zB38zrEdZxGY6zKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlnjSF0k2tsgKbT2I5qzdoW64vdbAmAIH9yCV_xV9iy-WPTtXEzCiuw179FBsRladpF2dYF5r2BPxW_pJ-iEWYJiq__Mre-YWmst-HXqsL0HXpfaXr8g4nGgpVjO8ETwhAu1s5kRpNJmdBk9DTck876_8dzM8iN7OoR6BaQ8VvdyvhMu_BDHFtQ1pZXsSm_yi6M0OPfmfPE-b8gQ3CQ-Df932tDHzCc00DqTPfygLkp28e9HNsalU6BYYHkTRprXou37c4M19iJn6edZ4lUouHZRzgaMF9gSnWLGocjGBfT8IVa8ocdDGONaTOT6PINT6x7cpNIuww0glrfpBTWrvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/22227" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYXb2qaeHjZCkfZCX6ux_uYGsr5IAM_GzoR4Ydxoncwy7zBGg_qaPKkaU1qKWUBw8qWh9uXBdmeTQyxWb1g64g6zYzzxHKlZbg6jNTfMGTriGyuNuRX8poscqIFISc8UjJXfiH7Yn-D_5mNgXMm5TywAF8X_MeIuEUqzVulGqYwWfNHfYmHziQL6hKlds7HwYa-2My0NBHgxTOoeir3woaUbN7mDFx7WHNltQ8vlEAXSRVcoA_DpZoUhq5Sed5yjWWKd95TC5Mf7p2k14SHH6aRR8sKl1-tjuws0X_3w_0MVH8qjFDALntB4OrRChl_Lv0MVt7sN9Tvdtybzg6cfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfQ3fHrwdAwA7ID9ojM92JvHzuhT4bAVFOXpkKmJls4NombMD2vXcKEQ-GxKiSMdBovAj3HzertCMsWSpzrdt4v27_QIlLIPrfKXXE67ej8ZnBcreENOGDaebEYlbFfJbcikIIo8Xr3VNUSQQGryv4dNu3nxtcYXHpktT6DkWKjbWuZWSxAb8KHu1WXJJJO-KgMUbiW_FVXP9FSjGaFYrCVh2boSdjpLgdiqxY4wczNAfxlOtgf2nbfdNidgRDW9HIk8lp0TwNU7uR0H_2eqRlzCUhrgYaK-doOdezuQzAjh5vEvddqEJJoqa5BV3EGMCGG_VDsRG9Aonoc_uete9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUgnn5Y4jCvWSK4P04FVVCFYzaLVbsLX9e1EQdfEq_KeNwEtb1R7SFp9kKhnjQQ5tseramTKWgr2q5a5DpuqwHDIjLDFNThxte40pFXmiBz3kPUFhmWK66Wqdak9u3egUnRGKkgPEKWXTNABH1QS7YJnWJGUGMQ-NU_8M4bNHnRBpDp_Box6VBX3K9uGo-kezPN16_1cDU296yGBdcztILdFO1S0B-h6WeO80eN1Ck6tIe6hAdSAPO2PzIC1gbHXCKDAE6QHlEQyglB-ZM3ZVXz636eBpY9n7zMjWPgkLUvw9F-XrJen_Yqg-5iYOE3-cPGFQEI5sy0eu1RQBSGMwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22221" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUwkyoQWyBOMd8Ai9ZqiEJSuaZNEdxnQZF20b8MRXCobImub4x_20tVFQ5CuozL3Qn3UrMPnnEj3Rs-KYc71wsnFbB1bXyXmLw7GB84s9Jod7I1u44DcyFWzNERqKuM0JlgddyzEbXcJh117hlnXBBFKxMi9uUNQUkNprxpYTLAQhGRWqRuN2RUzJ1xAFxfC7uSTYN9BvkHhHAoZlV8xtHFqUff9wW6pJhhSn7Ifm44yK45sqr_0hQvdzud87ItaAwdeHgQLY8LhNnrjatARIZTXO-gFxlKv5B7y1ar8RYVJo9RVPAVhZ_B7KnVhHcpsJBj2RGgg8JKia0bS-M2xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYks4UkYvi-xSil3K6Hb80jV-hH7h9__1PGF2CRPfSEgSNHD31zZiMdvgH7D5yiiidsOEHxb9vnl4lA_XqK6NGFPpe4mNPnzVZALF1wxti4EQmYVhp6hdy1nK3zUzcseqUyYgCP3doUxMNuWuGsyEhzmhxUDRAzn9u4cJ2VDXklWtT48HenLJpgtWgl5J9r7ml_UwsHbl4-c0O2KcY3qlBcEq_Yd7QUpb-LtIO-wiFdW_c4n_VC33_b42kl0P74SZypZtzBLRfFBLZZs-pgivokVfp7Zt0--0JpBkge4o4qtDCzK43eVuzFHaBRtQsTQkazhpS-s7aEo4VX8rCP9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv5YpdoUclf2DLsVguk6fNwwkPRC2Es3TGKhTiOND4c5OLZyh6ZiiDyn8iXaEPlijU3nutHhepGemT5s-392f0YaQhlNsYo7nZi2Jl8lLRDlysv39E99_ZAOMwGDAo8l9y6L1yqphZo4zKcMaCsk3iSOVrpB3RuJKAM1AjyP1EO_rjDLnz5M4n-FZEu9Glwx8iq6S8RLakXWgXZXdNzRCdDFA6fP6g1oVPZv_ZWJ0BhHei9E3epRB1ayJS4jHxjgJZ7dF-yeVgSvJB4LVwSTxWpdsNVa8z4mOm5tIxpfaY2zDXYic22jjHkdClC93IFnVnvf7Q-A0UC2OVOU5jDpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0RDDxpbUBcacsDEXWGZXW-tc7fXr1Jpgu4sOENaCNELFrCCAnpRtF70z3CKeqSAN9dxNp3l2IU19oMh2_2hzziBELzhi5K3qPaFVVkc-EkmQN5hm94JOnqHNqNfNX8LWECPs6TH17x3eKWv4UIIy84XqnkJ6-HHaV8JYOs_OPh7-Pwx2VZ4vWZgL7beX8K1cJvEiaWcUYXqN-7fD8GI-nndnUNHsIW4_oFMNUd2hR_75qE39gF6hVuIHWljYOiP8ewYxruX_b5k28oZLsrRY7WAIPStIvq1JC3Y212cqUZziRVViXSjECkt3Hs4V6D63icBTK8h5n9DapGUSMopSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3vMFgAmKsYAIsaeFYMFh1KRISsW_xVaVk_IwcEPB770zusdv1tXQY-pXtfHxsNXZL57yXAOOXtWMsJ8tisoGrOFWyHgsTUD3b35v29KOo3Z9acUNSil8qI1u1fGWazwOiXeVeFajER7nC6ezfbvuKr2uwzevqQ8Za0gPsWN6MdH1pPFrHm_r3W6HZJtnUhnSYPfH4FIhp3FuWNOW0cgw3mR0i28TEKEBrWQsefiB0hX9SZ3MXgW-UdnG0Esd_TCecy7vLEkoL84-zfWhOzxYFNsznq91B7_YELmWi0kbDXoO8Dy9kgs_EAMR0D8u4G9jtH11Bey9OeuuU94gn5UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBX0LEFz7weFXZSgLiOjC16E2Flq2UuLo1sKhgO7TIp82j7lC7Ca1CjBwfTjNT55ncYxRZiTDjLADT1Mpeoh5YBT8thwNP3-pUMsNPuEm5lpKcwot3s00IqJMzjMQsl6dZzpCn61Tpwb_a2662jzJjIHTr1Zcr4AqPlcUXoCCnjoCwrzvTvdmoW9YljzCWw3beS8KqKh_bYUvljJEveoMsktE8cNKNz4IOipF-ZQpOG1OSlO28Hbj7vrsZBmm1BOVP6465zvab9DLdPJsgT7IkDuEibjLKfshQLiyAvDubfGg-C7utRA8qfkxV859YEvtkHnSCGUhZkY7-OBv6O4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOU1qMbPZDydHn9kB6BVyRWOHEJ1ao-urnb4NcKsKSy2S0qt3aIwI09tE9_B8yWGarbuipu8_fvpH--YMLZBNnH1TpQMbEr85G5E0C2X7CI5IBHPaDUS4XpIZrIEpCrikxaRiKB8MLEJvbNFC8jGZo8gvatdC5j8ROKLqEPhBnKssnrAWBDX5QxOh6Kflc4Nir5QzhBQV78uA_Q6q4Fyy7P4HeqaKNJk2hrna12ub9ty69IaLljda-TuymEwwo1X38IzgB32J6_q5cINA4dXH7AonZTP-tcD8vy2TCi2MoWFHdODe7ccPMljIOEnAN2oYg15q-PDsJaj0ikbfqnPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1hMJKNeV93V2Ao4XfzZ12PbvxjTnnmOYm6gA94gg-Ll6R8VYBvAkOGv_Uf9koqHrIIoSXamOWv63NEc_J6EtFQVH78CgxfFRgOK3ZeEHqofVHyQ6rhamJl0g1qW6qUX8C92rjGZ14T4FNkGEnsLq5D66B2djknxR8dx0ZLy9np4YrZ7djwudstxRbhKQxUlSCCmWwh3o7fRbzITvxn1tAPupF82idUoDWHHcDrFjULnPJYyXK0pLeTGI9DOgG0kT8vbkZ44lWxdcEjz2pfPiHft7FsyiWtTw4ChvOMWBKsORJ7iw7JjevUH6GnOw5ZDC-aGlHqf3tl0LZHu1Ei0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lClAbhLtfVDqJb81WP6LFp2cipbVGbRz-whM4ZrZ_zosjstN62rXfeYpWyaWhGsAo9y--b-IVRgPgJ7Uhmw7ItnqKZp3CIuo0hRbYsAdVmfU-T-X5gzN9XxoevoWlzME9FSHsHr5RScnuK_icLENb_m3YaU_rwrRTu4PBBUcxhnJzMBlPZFYGKtfpKxHHqtr9Fv12bmL_dPGdvwbklkWs34svJVqMzn95nxRVtTuBzQWZ94O-sAJNVblZcfhyz9TzWvRvhc0qC95xM1-BJexTX9pssltqpTK4aiT5WhEyqQgZyC3iwNN-lU8LInAnyRgIorWht46MZK8ro1orsGNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX1E48H6q6NUk4Fd3n8avhiT04RpLCKMU43YIdKEM-ycQHTZVUB9U5ssmK6_0ZR4rPDcr3gq0mg8i6yeN_iL9VEih66QAIMzHUgkvyWOOdKODUHtSd3MGos_UEIGcdzAIDC2T2fifONDFAg0H3BI1xAEdCT0qde_5yxyx9NSqlyfUIMEG8X5KtNPq9Hk-TA7i7gnSI49lgJIImXcsdnHVbzZu8AB4nR9Mm4kV9D3EvjFExZET1sGRqS-JeJaOpe8IDiRqk9ccWJG5SbqDAT7cN58RKEGP3IsF3DcOr4mo0UdoMfNvO_OtJiqnftjwv2XPHBHwT03eBlebVfSBnUq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-JauixGHvpFMKFXECPThDbat3wj1w1UtUbU1CyS6GbaiCrLgcVXxww1QGjDCDoR9pyEFDVjdz6dlgFobxuFmrCSg8-qR4WEZl-PYRrfEMH8y6heKoAVl9H6RySmrD7uJJ-MSz_eXG-Csu0UKDwGrhNojOv6STvgHVl3bgTicvzKqkBC3sXQCO17JNCR8uLE7rVCLYro7KRmE4kKI2SO_S2n9y_1IVdu9j5jZ0YDd7E8kXYAheDLviKIG3tg0mprcFCiiG4dxWpylF8oYm4jduKGdm3cVjOhtS7LB4qRlQsw_SBoC6o5B1f5aXsKBdZGyQ9I-KdKsiFFY9_uMicMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDlUk6rvoW0CXQkGz8tiNI3_P0m_gJCLTtiB60EL7m1D8T_dx5l37CBNkkp7gHYkutgsWzu9F5jt-AvVKKegMjsbuIlQ0Z3NerXpAkZ024qki78TePMlrKkVKcjmk2XH69qQHDdxlDFDQnNQAPfi0aLGaQ6VYsBshq7TCEG4xaQ1rdBkjy31QAgX6fWsGGAeltUa7hVzRrVb8U7xiRemBd-ZeBu4xkiFC0MnMFevkme5BSLt_MiJbXtS1wJ3bJSjSKNcbSQ889sJ8J8Zk64UklumFFlClE6qwDE-QEvy8jbuNUQjHNVvGY5Tuw9UD7YBZlVFc5IHKC_AdGZLMlbyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGePQt4zW9xPGNUa9k_V-DM6zGh5Rr-fC71N-i0sQAgbIGwGneNM4HZePcp12aIlnCI571hzYVXjC3nXONI5uQ8d4x5XvLhC9SOXsVpNXoN8FHFwMTijl0U7Eet1TLAr1Hv_4m4hYfL2I1B2i63q1vBvgy34J2Qo5RkXUxnTwwTU_H0R-_xvLUU6TdzSEQT-ud8POCdKY9JBaitc1-h1zVwQXWFR7Fu1XE1d_jk3Mz62XH8R2K95FTq3Ff3PXW0pEpP7CFdskQD8lLneDY53hpmrmzrSvhEXFjt4EwA6PzTbaw1zVln1XoT0qmV3jjHMG5bGiOf05BmcScaQrBJCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT77mMORvB-YdlUXnBguEBzbr6TOTPaTIzI9hFb-YFf5zBK3cOjRTEH39eLGCc38HZnAvSSDfMW_9HYsicKIWf_550BUBxJ1HrL86Jbx-OcPA8KsXcIeoLr_zLl5YSBwhw3jB1H442GLSvRL5hXz36AAQaYcr57-Ksvzf0fE5h-UTYLpSqPfVGI7qtXKUJLn-MNW2HyIYMBATzEkBwfLQ77vsKovWnKqdjDMW5agMpMtaHs-rTeFBG6_WxqYWBvlrHT34BJtsBdzGxxs6KrTFzrXbl57OZxhR4i8wUoDk_V38-GT37d9aiOdshgCbBVUz51v8IsOTnODFJvbkgMkMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-pfk_t9sErXphuLf8KD7deTiT7wbItfCqXOUcd9609WLLpyOzj9whNGu6p4yez2fhp-pqfqZzKqb2SRnTjRhzbFPWbpyDIntphNPpH88CkyUCydpHTz2wno7Rp0lIU8Xv12TQJZFkkA9dmi2-MLF1SiHvF3DtvJMxQtGAXlCFSYBxETVkJNBG7RemXNg65OTGHaDMgNf_L-P_HI7xKTd0fU3JV4seli_dcS1cf3S-M0D7XsSZNLMnUNr8lcmq9WV0KYdM3p5nodZb5R9VLPljSqWIXAI__5LbEoQnc3fs7YwzKTwxFKn5o03vssGK0KMRCtAZxwjxyT52GQgYKk2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUGw_FiIic9suM4gXuyi9iiIz4j1_E38h4zr0xnnrqLS5BNNd6Bpg9Orkzz5avQMJpa_TgR4PhzbNHOuZt3MKSLOdNSxesycE-aWVXU-8XteEHhm9LjjwXzybnF8DAOl6UsjNU3n__q6u9jQxZBAPDCgJppbYquaJ2x83F3SNLKclS60acIbqvZIBt86mE0LI3Zj1F-qJ643ORMrlxm5XhIw7dLEGzr6babtFbNhydQdgKcu28hYc2sW8jZ--rQDxSy3gIGXW0NecWKNe9XhRYaSDaH1Wb5dsET-9n1nXseQ4hy5ezQWRvap9rOguWLrQtHBwOeXfw16fInSk2vjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfcnvzeMMWWGguyeIRdWn9vTWQYhHV6FCKhOEUbopKtayMTDyP2sHTEPzoX4UWkJh-kUmJNL0R6mdKYb5EZ0rlB5_5a7YT-OHpybvhECWpaTC33ywMkLpNFbDaMzSBPdwbnQbiGLhor8M4k2-Lo1pxATNQ7SLI2dVrDWpSQRm8W34_LzwxNZyoFTT8EpZmfEGFynKY4PUWOFKu9NdpjkP3N6acyUfADlRHkDBut0cHTcU0_HzzQ6MHYzljCfh481dQwTRgoNqzwy8gwODFdXT-2Ce7bHpF4ugcp3tSJV5uUX-rRASe5Q5e9UqteTb73d8sPpPrLL1hJPg_OHMrlnFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=iLz_eN4pGEUSpvvDoGgSzCMmyCD_oj1uYgjlK0fDXENv1TKkSV3uQwaPkfnpPhjoa9MN2P_7tbC_FnYBS8XoziYHktJL8ggD0QwE-lgZ-L6uQVC6Oqdp3A7VnP23VNUhz3ICFMFjOALHjefg04tAYqveNCcFqERct14zd2-QyKu3Dr-XIeC3onhAr5K9xO5Vrfl6B0OBaiUAUdSh6MQaXuEEaEeb-llLyeaVKxytPNrLBuXU3XjKicYt6IhGj1wjmRpB1HWkeSDsmN2MG3Zut94pehAwyB6knKZsUOKGfztI5AX4x-o_wYHewd1ljQhb0CLr6Vxl8dWJ70flMfxHng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=iLz_eN4pGEUSpvvDoGgSzCMmyCD_oj1uYgjlK0fDXENv1TKkSV3uQwaPkfnpPhjoa9MN2P_7tbC_FnYBS8XoziYHktJL8ggD0QwE-lgZ-L6uQVC6Oqdp3A7VnP23VNUhz3ICFMFjOALHjefg04tAYqveNCcFqERct14zd2-QyKu3Dr-XIeC3onhAr5K9xO5Vrfl6B0OBaiUAUdSh6MQaXuEEaEeb-llLyeaVKxytPNrLBuXU3XjKicYt6IhGj1wjmRpB1HWkeSDsmN2MG3Zut94pehAwyB6knKZsUOKGfztI5AX4x-o_wYHewd1ljQhb0CLr6Vxl8dWJ70flMfxHng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntNsieEHlq8vvjmK76WwNLsrIr6IclxNcWaqM2dbUPuTQD7I4wUzO7pwG4STJ4njrXWZi1ulzXHQlIvV4RzH8JT8jM2ayjR5s7I5-gYU97lPk6s0DwgSh7WA8-20u8GQqUYlZRUU6z2DL2Ysd1W-sF9w1aHT0aIgSMAr1grwQmEUcc5nBbkjn1bWee-GrOQmyCDwxkKK8IR7_dhNvIri-_jOVL86wexF8pHcjE95zlSnobSrlBXjl7FW_fj5E0LHuI4yYwdPM22YBtb87p7VaoXUabyniS_0St2PNeoFnTlppXPIoRq-DKYYEqXDqWhVb7LrDGNOy6I3GKShBYuUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy2wWDJZ8WA1zeZLfYdrcdkzKasVPakWTk2kedGMtnvve-11LHxTtbO9oH9C2VvhK8RyXBnIeDjG0BIgKwrvv8CpOr3Hkza1xSKIKe5UIww0Gt4U0QrKOikWJw93EeumaK7Ixulm96VhwbszcwvgUFQ8VU5jG5MWVNJ0gGWTn3FeshMsTf0kMbagGKuKKTV2jAuzNzo0_9kvdZK1DorkOfY-69zp75TS32goHzf8Ms9LwcXCaojw0zRcVQ7JlEWt4Kpbx5aY1Miif41WyySLYgua-9M7yTWRvL_D3tiEh7N6SYZlHXvrvTsMKxwSy0A14j2x3_ad-N9A6wQNYv-YiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLzlwFVs5CGAxt9wqjAKLar0caLlz9Uuv58_M0wEbsbkibiD1jLhAMAXM_-ZEsAJMuFsRqI431Y7nTv2cMth_KROlnwlXKARyK_NOihpHqUVa76sYPOg4PcfHQGUXG3nDPtU14O6J3rhSHiByCLLcbKONsoiy1wFw5kwMJRl5EURl-0ErlFUER7WjustdBLIfByNa9n0sW5usfTadw9jw_j5UBJd8-yUWolz6y7kLfaJwDob8WsLc22CG0ppiBhg9uDBiRwRx726byp3UWsDNQwUAr0wcxG4kVARZJzbD44vdnm3OVeVM1VC8JRBJSQR-8es71eZgIbCVuXBycvhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La32mngOKLG0Oy_vWH7Z4LAmrX9JDtZnA8g3ik-WRmkny8Nu9np4ks9Q7CDZXjCIU2Uoxhv_D8HwjHAxdrmMC4VOE3t-m1bug9ZWxpWnfTHObMNhjJn7nIDUJlDrygFQqsDx8V9GQJP9mxbg-gwlfUFfsoPtyrZrDk1aSpMUUyMDsRhBSSHNd8j2quvIrt_RyTGnOWjEcBEZ6ZSLk7ESo6C3LYyyUoZ_BdEqxwZXS08hdC-9GtA1sD_QwAyQo9AoklcSZ-2VVcw7w7G8GK59ORRE_hSFvg1ARHoT9DdxKhnsMJ6KZK6CeA_sOas1g1Iazmbl1J82XnNqXo61iZjRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKSdOwvx0APKYgtQ5hQNs-XIj9Jubpc8JK4HVQz6nxym7ewQzGhULiwi0Xq6Lg9h2rxM6TfwcsojCVbq5c-zxERWj8aL7cxhOS3dnoNIvQbm0tMc2SS-y9CUE6yaVaU_GHrxE0fd3W0vn7En6QSLh1zD0m3wxulvs1F6YFKiNwxjTbJHRLipfC9nVJR7bZQuxGsrIOFhLtUYDDNHcAuyYtvcFr9w6kC0ggfxgyE7MS4D8g30oyNYpBrQpKZOD3dNx5WuNvgVW9RDh-pSfeOWlF3ZK7-t_sCVSxvxPAPflmIBzhInE0RLtbSEx8aWr5OR_6ueV41qOAq9e5XRUurLtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5eL06af3yzAvJoP-LwUsy4fEklmh0KfjrBgTKlPEsRsuF-06xI4D_-k1KZZTgq7AwBWjprO3oHo5eMjUprJ55HyruQbzbSDJEIUMfOyVNcURXyf9PKyVxBIxet8Vhi9VjPSKOjdmzAkT5Yn0TalD5wRmwJkkgY0Pgw_uAU17spU9OrmgOvAsbYeHJCLEYl5k4PJAMFz1O6h3pGVugtAWaBp2okfp5kikmWPGuWTZ0nm6cpkrV18yK6yTM5Cn3UzGWTsnMpr48-9Br_pkXszx8Nqq-zluFuZNT3TW6Qzrgy36ACQzTeFaHD6EoId_3OnbLmcP5oFbd8gNYZt3xCddQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0qZWkThkUPuioO-O7YXQ9y8Z7P-BoYlpEKMijbspswKDgNSLKcVb8dknrXDnRppdEYaM9PohRDSVWwNv0CUM4_BUxalGxtxSsXcJxTnc1rZ96WXPiEUULJrpWCAlUXFxl-mO5g-MG8pQ1zFzZYJXSFZ-Dw4NorNWLkzH79vruIMXEwVb8tTdinGmrzBYiyCRsfDEDqLExj9voFVRzpOGQad-9fZrxcgtYTbCAxIZLOK1w0xvHkHT8BNw2h_dE02LmJJCSqpc24gr_QAHhn9nT3nm59slLWM4tX283QBZ_gBXWZOWL93UmTk95jPz9WEgRiK9DoMphOiX-MJurYc_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkl0d8Vd_yw557MqgaAW7ydMU3YD2kFwxJvRGylvYC7OwvxQhnObB-ORzNqwg44_8zbtp2XGKDMi7Z1_7wruRgCDC2ZG1S6U3bXbqmHmx01t7TcOa_QRjUUTdMCKmFj5qZhiLEfsn6xN-tEjTQPl3Kyqc8udr8gaXJPSLD-Y2XhD981lYAm0TOuMQlzTLJByuwRFFEG1HuBLGJj3Iw1iTzdu36H6pWmoAJQaJVAuQIAm3F-2EnQeaPprQnv3dFTM8f5lkYxz3KdzbPifYck8ihN6yX-vqvj7lFPc9pVhh96VawT36XCD5D9vsZTpBYLre6xvT5DDaNaF-lXnNqqQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoouSMiGPBpDKYyFIEKbu91m0GB-cwM6FpQxoFR_k08wrQfy9NLzkMzedMdyRZUSt3lO71x0s0N0hNn9N2Vnm2Mn3MykWngIuFYFZxS1wFKqA2S_ThDRLSX1be3SVYyQJ5gT2gTobN36FD1ndpxUYTRD2PIIRHCsZtGtFFTuzzFu7Z6bvBdnAiIEpy6yx-bVaSF-coiyPTLfrLitgZbKIik-fw5YNGdV_ZV6ovltcXVqPl6SD2W8VgKDZJIj1F_MjN5m8K2WAAfPd5dycPsCy9zg9v_A61iorvXu9QZPE1PjKCne1FFLKxs7MWHOl5AywWe9i3-8n4m_zSLvC-49NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smLENOI-rnwvOg_RLVif2qgEYYbNeZf78g0a6PzShoXgIgLRJLNJ3jn--p8ZchKnzNBbSzXldjX1996BbakdtZhvf3B0Pzg2fzI_6Dhyk4Ff1pt73k8zCvO2AtujQBT9D60lsBnUOJ1DodNVpiYpvblMyxU6SPLFGYyW_1JaJFTMQUM0OCBP28By15c0eAaD5LE0vtkY84b-8nhjfEQmlA7CF6osEl0cEtUAaS6MY2NN5UnR-dQhokyinvPjH0MawQlAjs9KnW7gRnIz1StgZN0Levlgq5k3dPBMvJmPtOIq2-FKonRrCYujUo5Kq34fuWE4z60EAPnxMtrsouHXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1EcLjYrZdVfF6QKMtDIoQhy7owaqLP75znbZZKv64Eyu1Yj9HXyGEhNyxNB-a9YPttqQcSQbTskGGuCJKkAHEMiC9QHwSrPf8nZSFqaBcwQZ0S9kA5knZ9KqVLJGmgK0jeNaMZUjF6jM9F0ZrvSh0XJtgn-vr1GH16zySEQPbiIpYLsxk573IU9QXOjql7IpQz4_bule8sJvr3-4mAj2QXWiyK2NgXTKFW8knfsIzdbCu4ACLXkiw0Nz9N3-TtPMbZ6qj4YssKX64wI5hbsrhvEZqwTlDG4Vt5ruUk73sBZea0J0mF0enJ3WlkalIPiYXqugKDPxRFrASkiPHODxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=gwUSCPDpoVk2nCNtemR47R4xxv1SF76TOm2K7lPEddmo5MmeHE_4Y-zJXRcvp2qC-iHwMQUPff4BmRPkSqypghbfCO7npAxN7xgXeILU-afNIDOQmLPjsuPI8DtV5rDJmfS0YHqssRn7KFWKPOc-4Kkv1lK-0N5oR3IQey3u5W5uX67DCOAX20Mbjfb4hflEtspf-_alovFdxgys-97djh7CtsgkWNv1eXVQ_Zb3UrX4YPpF-wyNy8jMYXvbiwsSu3XEJMLtz_b8XTIgyqOr9afrtoKSyJpm5PhK_LWveKaGk2id7bdNI3o4IA5pl7c7zHQSZGn6XmpkY8uqAZTU8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=gwUSCPDpoVk2nCNtemR47R4xxv1SF76TOm2K7lPEddmo5MmeHE_4Y-zJXRcvp2qC-iHwMQUPff4BmRPkSqypghbfCO7npAxN7xgXeILU-afNIDOQmLPjsuPI8DtV5rDJmfS0YHqssRn7KFWKPOc-4Kkv1lK-0N5oR3IQey3u5W5uX67DCOAX20Mbjfb4hflEtspf-_alovFdxgys-97djh7CtsgkWNv1eXVQ_Zb3UrX4YPpF-wyNy8jMYXvbiwsSu3XEJMLtz_b8XTIgyqOr9afrtoKSyJpm5PhK_LWveKaGk2id7bdNI3o4IA5pl7c7zHQSZGn6XmpkY8uqAZTU8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU-dIJu-boU1y8ZRS0MKnGsZWDjVg00mHgnDmWN3hNFjmO5uIKb65dxLiClnvxF90mVqToe2pYwrQMGopfPHaPOK43RvGhzOucHPXa5OYHvhTSpzL4Ajth8fc8Nk1QTL6ZNJYJwMhO4Cd0_kt2jPKE3TIhjZTb1DGrih0W63QriUCpWKUaIzwvFPDOG3awU8c5Q630oVDX8dy8QE5yWNTjOq-Qz8JM6ots9Q2ZVg8GDSg52HnuM6o1xtTe_1bzzyXTGdRKtGYQg-braV88x36YneZrB8hKr_R0q6EnS9HhESAccYRRU7yR5LQsDFAzU12YZDDxKVtU6YR9SM-potgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkdS2mvpN0sS0A1HA1Z_DCMGbZOHwcyzDcEaWmn0E7sp45VTptLsKTTJ4JXbM1cLRLpS1TY-A_bH7QWdRVosjuPY3Hdxf2cLNOuNG1WkRruoh79FYbpQy965Wit3ikEdY22YkUA9eyfsp4B46alloARZI0R1tbrFypH2GfbKgqlyMB4_2KFYhi5IrptBBLOv0dNIa8DPmmtWj0-u9GC98MtVcc-YeQJu1vDy0RTzfeB-LNGAKZt0cBu-eL_l_nKmh0JRnP90YEL2RTzAUjBnIrp95702f75896vlONX2LArHSbzql25fIGtIjKHqYxjjDdnD6T8vBIVzswJ70kTgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwKOQQhxIaP2wlm8_d6uSk-rNg7UvzKY0fnpTx7h_5QuCo7jpR2c2EgVsD03Ly5E8jsl7Ft_zZu534AtX7XNGlSsFRbu2VkyU4bt1F0XBldPIUro0vQe7f_vRJvPLI1_TreFFdMjd9pHdO0gI8gOhFxQUpfdvN83hJXrkQGItQTHStu2CCIND5o-F8Vz_5ShXpJBRfEEdc21R3AA1fzDQUwr9XcyE9Hhm2EchcWecpqmb92xrh2Gjjpe3rr70xUv-jVvLyXnrk2OKPKe6mWVb7eok6sewjLGVOPFk9xLewpz4c7e57t6FQEP0vhd6Igz7UcuAd5M3yypf9tStRXnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd28f2yAghAhDhx01Dw2vhrvX_mrBtA5SuDo7fyREvuurJ4FRsI1HM2lL8joYJ6Ld0GYKecQkxdJ5t9gKIKAzYY-15b1dB1FyuuOLOzzE458wNiNNoLDRJuwMXoSm2toxKeYduj67vvXMlGK6MrPuHHn_eXdYOdW7ahQDqnQ17_ETFJe1lJHoQNJKvDtSUTJ050bAmDs65Jr5B1OZyr7au56I5oQY2aPS9Fx5ghoR0H2eMAZsFWQE_4P973frDOl3JxYNMnrdX8NdMVMe-bdX9ZBMZeRkkqXd1CGzPAKKvPxv3wd3jLnlgXYuVJ2rmRMz6ip0oIuQ_NnO_caGYSQUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Is5AwNRXawjm2uPUAKNB60DwpIVuD7ctADuyGILOZ29G2mIVnjMZzMAqVZy-h_GrGmb5VOqfT2greDOURTpiPWcI-rB_7kjGOxZMw_AV_dbnkN-r3eYAJjpvs5bBLqM4W0fX4vtOnhG3ZPzf9PbF114WyWmZ2zhW4TZV6FKMcoIxnP9sj7RBszv1Y3aVYHsABoglONE3Q46Lacu0dp3-c6OxSNwERNPTBbexg3N5pLw-ujdnu5o1rIF984PzIFDTDiEt2TmuFCwTsFX6RzJ9sg7giZcIyrDEB5O1SOA-KzD6ImIRSVsx93IXrukdyYzmbEF3pxX4-7rcXok8FRt20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5zf4f0_mfnidSvJVM_wv4KSjFgT1-6XY-ySikUVG1GT5ElLhcqEhPQNebI678AE2uS2aERaw53E8unWkL55U7yXFRXyYq9xPFR75RAufv3zIR53-o9W1jPqlFmEGl5ig80HfSadIhgK3bX5X66khP664ZU0au_hozQhD-z2_5VmXfvSosI18ohocz_3OM0hf-OYC6JIfd82WhHxnVdJQGOvJq_W1IYvScD-uTCom0KXb8EUBXV4P2OWARH-QJPNTiumXi6Zq5bMR14C5bk5QTlhhWTXt69qLkOoxgZwIUBXyHASnnRP-G4lrWX3mlCSTiw7v1Yy5PFEErcDZ0_v1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VH1iEndJVLgtSYjT3p-bW2iubW97_YU0qofqqjU7BL0NvnRbZfr5qAB2qxqbPpmK_oYyO1f3kyAEo78rJh2w0-JVj1NQSjxOdig-Bx-h1cGqhLZMAOKBg_ecgoj5rEb11DpIMeO_m1RCRYt1s1BUAX0TALgZTjbGT7QRIDan6FAUJhFZh2B9HBR9FUgC_zEkg60g2ZIqOmv41qB74aAAuGs8pN27ewyqDxTw30yB26sDr2n_NPgVylv6asIEpnR7TT_rUbsVBE5Zd1CQg5GdR0bKpDZUCcx-WgbbQGA1SIVJ-5YFaUr3GtkyfzAzruHODpcxb_dv0WoRKO_BthwvmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEwzZBwk8gSYHDh_m7Z2fEFAsV970C_ejHEVcOWjzVl-0RLWMLg4BpB7eYvPXIwL_glZmP0isO2iJtUSvVy9FgOV3g45c-tqAg-_eKaGbVoBo2-SU5t_UIpoEciFOnOQZKzLmgA3097P1cIFWyEb7mQcfgGmIkySO66IAyL26Mc9ZSRbb-5sPOQgPe_HH9pEAWzP9QTT4BP863iwNo77mf0b3rj5NzkOoXzbkan4LWY7G1IexbSNo0cXtFnmAzN5DDMhxEyR_mY83gYUF93WPsCPJqSMIcbhibswzR_ExCFj5ONZX0wTVspeyIgTLQzrUV0SbQKOZvXeNHZQIASqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAqwXQZ581ApC543aOhcIYP6ag1pYNquzIBRaLcpivyLivZUHrgIuICsjovFUHIUEJLaYniFQVIPUOcYWSQj5Od_KRm7joAI3KAxcB-BADEM4tUhSxYRhvPRqXoa1cPgKRsHPfz9rnS1s3zQPlJa3K2RbG--CM5-uUrJmhHjOrhOqrhUKp3YpyIAtMRfbCn0oQHyNNZgwCTwqBPAgwbyJIBsVbj2367RkBUygl7g6eSUfN-rNqCm8-AfYQ0J_xaBhJBnNJWqR9JyOEBzivKNIWnZtNKmBVD9dQAwIWS7eLLM09xtYwRyscUkfGK6o2UVviFhc6nDiWuWrLa4ii7APA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=SLu0qq50Vf7shdOyoPoJ_UHZAA43sjAoqZwUX1LQ_YdH_cc5MCpBVNdtSwBp1F3JMXUpoZS6mEzrBE_uTKT_E8ZGIbmKiymO9Rw28nJuciS_0XPKDYvisx9iGkXq3DDhsQy_fnhwT8_iEMYvA9keA40a02c-R_oS0WyFF1dWOqwzG4j66MP3E0q_UQC7KiNSm9EyDfhbMtN5nwNy1gnSzX6L06TyKVBuzkP25rYcRCpwdvfbSJd-fZidLcDpWrKrmQTExH-yICGtsJWJekhx6egE-MwSrCt3VeaI4-ViWrtuMw6PSUy_n77sg2YGsSBSu76FMHhHZl1SY1xDkjfUlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=SLu0qq50Vf7shdOyoPoJ_UHZAA43sjAoqZwUX1LQ_YdH_cc5MCpBVNdtSwBp1F3JMXUpoZS6mEzrBE_uTKT_E8ZGIbmKiymO9Rw28nJuciS_0XPKDYvisx9iGkXq3DDhsQy_fnhwT8_iEMYvA9keA40a02c-R_oS0WyFF1dWOqwzG4j66MP3E0q_UQC7KiNSm9EyDfhbMtN5nwNy1gnSzX6L06TyKVBuzkP25rYcRCpwdvfbSJd-fZidLcDpWrKrmQTExH-yICGtsJWJekhx6egE-MwSrCt3VeaI4-ViWrtuMw6PSUy_n77sg2YGsSBSu76FMHhHZl1SY1xDkjfUlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=Ngy6fpKJ2JiOD1Fm0o8j7q9D8AvTyp2CCrmoWTVrpL28pYFfvfPHsSSUMqqLd_Vy0ZmZ_ej0rdHgMMCd8nBdzzC5SOwsw7efQVeG71F6glW9WwfSiakYRfaRc7fRs5WFf6baJBIBTyPRciQUyJPRrMbLmMorFhnTd9yp71E8RSiTLdxCHlvulG4A-B9G8KO7Ek0UsXabKpkjq_nh1N7r4rQtNrQ_Sw0OxyB-SbI0zps-EsYMN4JuuSIk6Ld5_97wazwXPeiCPBxrDMXAw43U-bikQ6mrxrBrYlJAbc6EqSi3S55hlWWzZOQ1E5HuDduhMQJxq9rJEBXeivalt4doqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=Ngy6fpKJ2JiOD1Fm0o8j7q9D8AvTyp2CCrmoWTVrpL28pYFfvfPHsSSUMqqLd_Vy0ZmZ_ej0rdHgMMCd8nBdzzC5SOwsw7efQVeG71F6glW9WwfSiakYRfaRc7fRs5WFf6baJBIBTyPRciQUyJPRrMbLmMorFhnTd9yp71E8RSiTLdxCHlvulG4A-B9G8KO7Ek0UsXabKpkjq_nh1N7r4rQtNrQ_Sw0OxyB-SbI0zps-EsYMN4JuuSIk6Ld5_97wazwXPeiCPBxrDMXAw43U-bikQ6mrxrBrYlJAbc6EqSi3S55hlWWzZOQ1E5HuDduhMQJxq9rJEBXeivalt4doqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRY1vlhYLB2kbOsCilzRlC9s7-J8V9vglms7puT2oRPz_4wwvR7XtBqpGvsvnv5TBtkN98rPZVKGymSHS8DzTPnTDsfR_cHpx5Sd9JwAeJGFIFJ6yFQgIJryF_lKFVvdmamnyk6tztO_YDQ_hO0_7vbH2Qbl4qt89QY5f6UXiHSGpFWIDAYuhH79kTn6PVlAvxdEr5PybI5OVToLObCmDoMJbJg-SXvHj_ICUGc4PeI5D-ukGYSQGkKMG-jrFIidnXnsG7faZxQpgDWkBu5TXtSeKQ7rczhE5yW4hJsilk5MIuxFvFgc06_3v3P8bflOcLncqAlKsuseGZaS2Zm08Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSPGew4U50te3ARZiwI0OJfOqL1C--YN4opkZVYHaecoOGFwko3f53T-g_-0UCM1Evesy4XRUuBaHr_-sW3AaBJOLFv0WQNOCl_MvnfjjtOz-637MlmEkdmj3ZYGJq7zNwM2_M9beY8l-SdFC_7fwaAP35Irgijj3lzv83-WWDIIFdnowt3FWsaSo7jKAMVTi35Yo256nwCxGExteINoKtAiGV7btrtLT-C0jyF9r7FgPqE_Qfz2cGmzjI1E7grONpxI8mclzAobf0v8vml9MT6zcpWJBwUK_lPbPithz1gZCjR3OJGshFBfRsknKuA-eqn9D2697S9RJJXTP7gHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQmTpaWUjCTTdnfau0n6JjWkhB7MFQ3GtHgRPfaDfH2tH9LRuBMej75RIPakU8kKsfHFGURd1jvhJ9NWONBXK0gW687cmV7O5bcx9ll2eAU6nFMxHsYud16yyxjMsK2bWEC5koQUXJX6zvn_HiY0o2oyCg-0jGSE7mgo2tUown1bEaXNg5e_6GHrxo7X1Gnk7riOwb_yUV7BfkScbkQY4Wzq56fyFf1LGdhhya27EySN0nStntftGXEpnxcqdSUJTH1mmKQojd3S96kxQ9wKJLgxH-T37X82SaqjnRPj3ANrafRXE3e3upC_TKve1690qhJZQDbbPQEJXRyfS20CDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dokMOJWL-lgiOgfiAjo1WJxYJCDjmnx8SZjZvj-qjI5c9XGlTVe3qKFYyR7YQttQv9JBbvGFI72j-wYk8rmUZ2QiAy8N5b8Zc30j5bOelJ4Z_YFucGQH1nmn3hU8zxrKw9A3QdCthNJuCzs4snktGIjFxJUn4RcuOlRH2KwgzGVAB8srKxzltDeyu0V7PBx6JC5GUGPO1et5wmWp6sd3K2C6JP7MnMPlOct9fDX8PCuNz3_J9aJwQijBqA8byTi_4obD7lzXljr5VvkbeFyNou8uStUsTZxABhwASIxPbDUow2BaDZTe5qLoz4GeUM8liCwfghZ4LXqKOV6jw5_nCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc9Sr_v35RgdcnEFsD5KzOg0AVOg15RhgwsWaaoAm0oE3eN5WlLEfUUmo0IWsD4BN0r4aqyegze6QG6QHukB_GJKgJfX06Yk7PRzX42bRcRji_SB9nwALr3Cv8cJXBOXfNXOn2UBd7UHi1s5tLoHn67jpLmMx9DbTaH9_E2B1E5yobO1MbRSLJwx5nqF3QHhHM-URZEeWbGlImYCRBMSNbw5e18c_vOhfd5iVdhPirIKTgHRZKwIg266ZpvigADXkiAx8aaSV5854ghdBt9i6uCvpFm2dnXLlpStBX5dUMHBIG_VqQPwkKVw0hJ33Tix3eIWoTAxbCvK2G98284WPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F81EMQIlqK4afDPhSUJFgbMAAL68sLIEl6sTLxr9ZX0p3tb5QgQHVGwhSbD-8HlNjEvcXxKkOwyoM2irlkmEYFMeXih4nyQ8-I-qfYg-i9FODobW0xfu0i3Q1cN1iINEfO1jSzl4CaLmv7WT0F-HawpGjw2TYMRFvZDPKLYZe8wGwfVQzzi0yBSBPEA5tZT0J4H5Ic75YlbMY-QsrjCuWHXPl8xbYBqjMWEnuMWCG3jWicHwCnZkkHMY09uLKx2tmzyetksbFng0NGfm1o2-WAngotD0gwCKncxlBngRCXtpfUBtaZrWl4KiAolmtE0yvZuCRrLYS53sYk6hL8lGNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hwm-J23HmadRD7GiggE7G21Np8CzkTGgHNF-gWZWa9w1MDhkw7yQCkQnRAKpzVwcQudAuMmjvPO-GJhMh7vpDKjsCweErxxLy2msxUiHiRtSBXGpKZtrWhOljAPuUaV2K044in5mvAaZ1nHP0IzMds1LanhkwQUHZGuzuztnkDsjPuW2r1Kz8sZHpIdc5xLaKgKPP78ymJ8kUiBPFjjPUPvtl7RcF5BbK7LFMml6ZH1GgceqEczWucp8BWwOxXOu-m-FVh9556qolwEmMFXbS1wGlzxPUxkMsL8LlVdFKdgb5GCs-PX8A9QOtpeAw3SwjViQvlzFqD1xLYdL9VyXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXugx2ApUHQilc8Y1DVFEVTbcLMBAXxW5qv_kzz1sCsSGt1GmEtSAoauL9px3CAJn3Mv_Ja5Dr8Zbtv8Yzqws-7SWlTwmfQbQBhVLNXHn75dv3YrCoTXJoTh5J6fimUtfW7zfZCaz13waBKxiJcUXfG2Ulqa_kVETRlwHiwfAFnlzxV-MUvC_HpPsKdfzhxS2gEwoIB5ED1t5_OqCFO9lKtPC29sKcWr6g5vmdpzp9YSbYfbl7G6FgpV03PIE4tOOwTgx0AYIm5q2cXnsjpEtnRtu18QkgC4CxhpuTbAEET3an8ygaCV9s1FCScN2eDF4r3GUKm4JXw9cdctAuRSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiiyP_n70589c7IdFfYnqzjDedJTROM6xULzvu9lARhYPa0yJqU_e1T3fjkUjLeKb4Rtr6Ckj31rF--2UA3dsR7hDMaW00VEfqkFGNw6vCC-wd1LFFrA2hFffgcg_lgrlJtwAk-SfTZoYkz-Xhp9odDM41Ev2x8tYBBImuW_jrmZWzME2CIpDPRMKcogg2XK8a_f5D_AF-rNAlJLDj8KOyn5K0sHpo4Pf5C-tnAr3DsPCTVIkPDv0wu54UL4Je3Umk2x6bLF3U5_B4ca1PMR2hTR_MoksA4hLYSVwrcg1naf0p8W-ydhy5ERiW1-DiogeUVVf7lQ-Z_0JVWN3hLY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFZBEy8ZVznTlciJ_mBAhSdRi04XIDBr4h7e4CSMyZdC8IWk42zLj_ZEHDJ62sPui7c0txGw8lhzMyuh4DClvSJXmrqeWJBx8vPBZfWUkuqKvC_5pMSrktREYL8827QQ8oL_fdDAVH71qVpGsgj3JySPiwIIUZyrptO-JNpi2LM9BVUFf-JmOM07mI5SCVaXEKMiwb1gXZ94jNt2cOz2WmNe1nyCJQ16mUeL45HcR0IkQbx_-HGQhSewCbfWIwhqQZol6KdVTaPkAIFAR69H9xKY5EPYFdb19nyNZHowwHnJ22lPulTAjbquRIrSzPVDrQD0PkXZJ1uQ9-5dUnYbBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IH-BJuZi-NxiapieV9ncBAo2fry__8vXuAwte-hKGlBS7Eh6VKyLoq_BLghMOyq7jGE-WYzeG0Z8cZ8kSruFZ7OTKNx7rLfkpBrWNqSTyqf1TMQYPppanFX6r3VPGknFT2EQsYrrTivMw7QEGphWbDdOTwk-SeXkqC917cwbgQFvz4QGrNXzkwfhy47WSToyZ-kD9IYxskYNsdF3jUvJh2Nr59fhBAQWI71R-QSeF6jYfj5204v6Il0rTRTsqje7lBCIvyxuYyfm1PSOlFrhWypTSqNFfWWH3zPhj07tG8NaLRJNTkN7_7Yk_aYi4Zq_PWLdEcgdYpSjtlJsJ8iZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC8oQAXipZX5lr8i5OedPTJDZgrrrOlpG_L4hjw-8hsw2yeaF9hoMOxvfurr_corPnq-MtvARdQAP7lLu76DYvIxfiURrAykfwxIPuQ8MLhuDHCkyLmX1EPapV7ny0e0JKo-Lrnvt86bByA6Ym7eRn-MlDA1ttWen54vzTvTHtL3ikTmhcpPjjH302WDJjJZdh3ylu7ySmFZnOCDcBBuLDuN5sT0a9E-DgiSiu2cdRIIOjVn23JrPGVYE6acbka7nvdGJzHKyYgJbLJGI_gmq1Ux51p3RoXCkL_irkBfpKONGyxV6coS1tH5g93flVH5lkeUguw9erfJSDRxdNoQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmQkItQSx-nTheEdfModzqLGq_8_qNqsE9TTo0eGFUd6xhxy6uEMtJxwE917Hy6I4Zn4wNdiuuU2ONlRk0m9Ylj9RAGil7aSezVeQmL9uavPl-HgVK3rTpxO-mi2BZoJzw_ve6A0WRZ_NP69BJg9eJypx6twDSHIDioU-pOv0meAhyh8Mjx7l6Tc-jl-59q0CgoBGNqaL2F7uO20vCwVI-97N5eUNPP1L6in-dFWgtyNJScV2wRV1aXwS4QTaKzEebWLmOJhzI_kBtq3h2HQQQX0TTYNsdstC2c6b0B-ojuM3dC5o8U0kfg5tuO0rGASWjWHgj3cZzpLLS9MnImloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFkwHNnEkxCfXb3PtqVpRK6CHLNdS0U76IrTGlGF1d_RkyWVNSGl9HSnRwlHUkB-IiF4ElyNz4wES7xjeovf-YRML2jpLbnyGvKgC26B4w9Ou0wdkqCBMZLsLc6sDudeSDTJ4jFrqqVYGxJDo07xxB37RhHZsGpHICYxbWVtSrSl3rC0IIRxt98iVzs4nszIQXsNylfsmpkrtLyEbzwVQetvlf9a2GU4SfeKWpsby7OSRHPevec6-bcfE-zszykTNp6qnCr1VfPBPT6CEV-ko0LpFYDv9gOZSZ8k0LcYxzqvZfSxDlXs_QJqqOMNLpmIwD2uhJ2plL-K8HKZRrxhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVC93Evwxczpy16Tlhh35ihXVNcdkvSgnIqC4dtANPwyZjClRLLAOeoaiOG62xt1NxeBwM5hf099qTGtqteqhg_R431KjqM8jeT0ESXhaKJU6bnBf5rz7wfV6jY3RIS8OhXYTmkn84F3kdQX5Piwo-PKulf4mp8iAV0-PnGoN8nSJr_6zDL1mBic8N4aDmIAF5QkkWDAuBP8JhwyboWRf3UpiGOzfMIRdwXrK2F9a7rJk8X00uC5yPuDhJGqwe3cKjpmWRyMqWIeKkTGJ0XTbrNRzL0d4I0YY3T2vADg7OffI7a5A3pO0MbQyWgicquhxHQdysgjO-EIFGTvH05WbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/timhnc0luvA1FWdri_oNJOh28JxMA_XsO8Kg8qjZN4-pWelAKlGcF8V84gL4oLRVJ7dzDaIs6wNVOp8hQflE7Z4CoWpEQvwGUcBQtwUYCLbNNtkArXRIT-upkRKx5IusQT9acUnu1s5VP2yBo2yRCdp14kYs7MSqAIjw04EI1fJJOM8x4R6Jdx2JivvzaRB5G05KonVnxviabKvXclptTMd1NcAV7irqwLgvvZxpdRbK7uRjXM8R1NyCrO9BNFOsqAluI9yr606p676n921rxJv8TIXE0QnrTpO76GAb0aqZY0cSv6IHWHcgzr73EdrxtyoaazyelGwjuBfjgcfEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3wirpPS59tvYOFPMp0kdM6c9t7mbvs-5sH89htEvWGzuSwnyyccdOtGqyzh1Ad9U9amPeWRJ2bSlMsmjOBhcIBdGmX4aApp2uSfUDATerTnecvizV_leQymUNZsvB3uQowqEAESz41SEuASUzLj9k_D2prK4_G8kF-JSd7iTg-YgAidKk9wtYMBDxGwi5ByIrhx1vz08p9Fm9WbgMyU_DelDY5vDz2wN83JlCpKM0B48TdmXYsu5PtFUBLaCXEIro7pChuy3bX1x2dSIIujtcNoAe1Q6PNx3W3zUcl2cA9bKdvmc2FyNqRUIdTDMclw3iM8vOVl9YLwqAQEaEcZgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAfH3tPfz5iLu9dz9Z7mKja8iKJEu595ZlaXNgmsom1l0fgj2vIdqc7Btg1cz6_qfMuXcEIlNIN6F2vHSQx-31OCC_F5Av4EJr2yoz5IoqxqWwQyiyeRv7VEp5iIg2uExX1dbHLtAj300HU9ATmS5fK0PvcjQ8mgszJ2HowVFReLTzPIwiSBPB60J6O28SWpBWFy0CoiszcEUKcwBlKMcwgRi1PI204Bs9pdoZSEINQqylyqiQOVS0DlqZ5rz9AU4rWE3arN9h25sROYY-E0jnHLWb5zBEUgkznkp3cL_OjFaIfRACOQvNaRobSlZulEQTeq8uByY2eE1aJ4mMc9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CACGGxVj6TYajVHDZ1dVeSVK-MbmWdcb0XXYzD97bxZm3pP95sc51oJOVIAXcbSkwcfzblHbFFKzK4HT7QI1uotk4zCRQ2moWiwJsbIe01rmcnd8Yt_zYxP0I1IJT0Rzi3TSo9Hrjh-ecaFNZSk5pHyterH4Zoe9ViXzm_ygwJXyvUX_QmFU0pWNCMVl-8CK8mBUqfdKNqFNHyOpbqR-rLEB3lpPhaZxILVzoKPOu4GBLHz0k6QwqinjdxT1d8twWw-d8OiEXkR1p3ndLRj5n9uGpfy_R8NGsvm7Vwzcp6Bw7kU92UkKdGJqKuSER3VXOL-yxn-KFU4-JrYYXQcW2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AloI3X1AKZyDzOYU7X9b9hADA2WId7g7NbhV3ElimegsU9ePfoaDsymtVL_VqRLousEFn64YXG7VNcobT7i3KN-4Fgyl4uJQBYm_ZND4RfTdw6488ehc1V1ZyQHwbfNZkMrjHEfJwxPolqTOFxmyYIq8qQHz4shOV0CECB6WfD8DzruyUTisRD_A3KHPbTMR5IVGsv-zYIZJemr3Q5VcI7f2hip8EvGeL486gmQP_0je6wE3eWsOvgRf5c89PF2cuEyIpoz_aR06WdwaQxNdjpm3nSUq-Aw7pUhClrTxGaEAQo9WNZfhssf_7aCbP-8aJiX6AfCuiNabs7p1ztdhmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpC5q6Q80-eaKjIWVuhf801yFI7e5cXlKd0VP2p7dG9OBtKC6LnIm97F0bFOUMhWFQJjQ2dCKKeoUVf3DmgdWGiY2WrL_VGvQxrbURAmNPM6mtkev08_GJGm95i63JmCHHEkSnV-o5vOAsj_F5Fnwu2An18LLpWhBcBlG-8kEz4hG5AYT5wfhLLVEX3DaQTgg484bdgZDxyhWQPOdcLtDWOMJZtt054n6FxtDx7yb6dgCwzEwM8T2TUH7mkHfi2FHQ1zzJhHbsPdybvAJXqLG8Dszs3-Uu5P4pGXgeI-CqoJDeIUlXDpx-_dEO5-OO-tDJK-J4cJdw2RzLANHodA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QI2om1X4E7K2UwJOLOWaDTsApsiv6o0799KnktjZ5IHbqUaKsH_wooKd4I-yeQPH-GqtvFrKOJYmaEq3bXwJe-M0fu4kyBtrJ0lp615Z_YZRnYd8qf72AhN6-uASAnoEdIOsnsBzzAqKm5zgE1y77ncF7jf-9vxRrYHEwFKQJQorbJ29CkDaW6roKZBmfq7LDTATFR3p0Q58ynA_tT6iESGh2cewb1My7CV6uUo0v6y7AYTaAN_1Cb0AXNZbkZh_mfFS0y6zNwbdVLElZm9Uf4ItYd3PqWuaNbmh7qS5kopYtecULKHvweom7JSPfBBZ-CwrVvZMuUNg0k8sd7fmag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc9VpFV5n-eYXQpVlsAMmDV1b8mYJJ0KXsPKPHRwGfTA5RSNS7G3NmxaBipkADRBKA9u4aGuTuhMWzVTGB6O8KWxJKNWysEkmNLupdjXGRXF9c3wCqrLmjkMCtMh_6dV5qSo19ppcTKMnHBaL_57LUjagaYFdhVQqVCDj6JyU45mTFF0B_Q5tnqSeqyGc4YEjhgW5Ywea90n1aLcaNi3fPGLlNPmhdmw5oAQP4nDgZ1dqZzYueShCpgMZjuzYAoHEUyk4rHnrwCcPQeA58l4jLCafrQAWD2hv39jEJjHMZ8dvLixZnX7jO0dVIhVjVd1UycTXoqoxE2tSlwzZ_dOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZBwNWQJw990LbiZ_HRC1kd7VssmMOuXAue5UtLmwUHwIutbxxzJVR5j9p9tjEZC_Ur12lwmCDIzm77Mb5F6FYZglvJA7NrpDs7KWvthoTikpdfJ_Rd2Xi4VTOfh3vCURxtxXo4Esrp3WLlvOFanLyQ4dwgEuOfnVWks1yq74Do_HrcXcYk6gB5DuyIqSjhR3PVRx2hq_N_4qDfNpgbjeMSfqFmxEjIcykXCCcgY76uJaBzCMFFjt2duVgRGqf093_NQLb_J651rVX_vSGxntKCD7xhGMVEDeDYk2ZVWWCoGSIHd-rG_kn72WT4BbFVXu_NPqkncCsv-ZkZgUUW5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNVeykHt-LnV_GSRriHsOjTjHqPODrphN8Q_DwvhqMfpfAPa4cE4xcI73mGAu_NTU5_7bnYVylNB4xuCntogijxxvfq7Upp4VRKqRitSsCA_6H--G7PMm0kWE5vviaPptTxwHkA32Zwad3pcpa673TOZWFpCpHGpGWg0FTRZGO6CQUgT-GpsvyvTLZAm0sYB-iVlh3Ff3tClVGboER67LhtDt7gZOl8ifjlCbrSaOgXMm28jRywESP0PReJxyuAUwRvrH3AcO1-bz2cYKKXCukcXMxpODfq10UR9FBEoEFaBMJ81PEAn4u3WaaZ6vg9FkrBgshhX0oDXzYQCTyVznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEDESm0SFVD5qhEtQN6XWNRbhYMviCAlMV26dQsup-CV6hxtJ3HjrfG0Uicydxhy9JJDUWmTeqvqaEslUS_nuuXpery6663myqAXswwY0BOnzQwktOwc1jwXW49ENPYfTnj9ycf_JBUBPDtxpjTj1_497yQOuYRQR9Ho0Wxg-_bnM0Oy1PmInbpYIKh0oAEJGTKdX3j7x068AYG9gSYB8FSmzFyoTI41yRoARiOQ3SYx4-c6KOEatHzdgnPRkAzMIh1PUfKeX_Cv2flEs_0nJXgUDAImf3fBLdBVBibvZGESunD_ZHoZFs6ffwsYAmN-Pyw6LlaL3JXn6Kbit4PYXw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=GpuGCNzrkA95QrWDd11qjh9u1djIeOWXtGJ_el4PT_gGOt1EozHO7-hnCaBPrqfF5KB0QKOB_cRoPwr1IHfyMnwW5Ih5KL90E8v6rWfMTd2oenN3RsS6I7lwCOZL_sGnzrTkZJ9RTgqpZi3YfFIUtNtmjAjki6POxhjwOf4q-57JJIeIliHgeBsTHgBqA8zPYQi0Ix1pWBvby0ITN3Sv-YOCYFJJhA0b32e0s5stp9buq8pbfvn82XL23TeF-x8jgmSwaH6pjpgtpHo6ZGjdRjQnij61Xwob-SsYpJf4iojbc0SuqY1weJlpS5sBKBdCAg9-RSiEmSulHUTILrr7rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=GpuGCNzrkA95QrWDd11qjh9u1djIeOWXtGJ_el4PT_gGOt1EozHO7-hnCaBPrqfF5KB0QKOB_cRoPwr1IHfyMnwW5Ih5KL90E8v6rWfMTd2oenN3RsS6I7lwCOZL_sGnzrTkZJ9RTgqpZi3YfFIUtNtmjAjki6POxhjwOf4q-57JJIeIliHgeBsTHgBqA8zPYQi0Ix1pWBvby0ITN3Sv-YOCYFJJhA0b32e0s5stp9buq8pbfvn82XL23TeF-x8jgmSwaH6pjpgtpHo6ZGjdRjQnij61Xwob-SsYpJf4iojbc0SuqY1weJlpS5sBKBdCAg9-RSiEmSulHUTILrr7rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
