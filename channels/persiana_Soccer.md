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
<p>@persiana_Soccer • 👥 198K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 02:35:17</div>
<hr>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0t_3SmphGbpN_PKwcNN-KtBeurCXR9rbYjSnPHfxdoQozZ-W--P-3fEmR7mKTSGisUMaZcC2jNO6kRzDVm_TikwWN6n3mIIz_uzrOF2i7BKpU8Q6GttI6OK7PDSjL-YLVNlEOcM5uzyHKIOR-h-BGt8j5K3f02G3QFhS0prrVDJ7clT4Iwm8qKY8qzICPblY5IHuH1LQRCiKgqBtQkvCb-Kqxq7bfCj8oyjY91edRrBCnZuUjb3X9TOYeeyqTVTUEVyyE3zCoOAYb9vJt2oFAHADrl53gM5lxPtmpeubcidClFHuwtcOs6pv_Qf2ptptzvpssUIxxJ_lb6PzA70qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTxyK3o2e5C-0z0EGN2bRAOrf6sjeoOD4UPv6qfCkuoSJ8WVCibgMMoKAstodnLUkyM56vvGM19ReZB2qYdbUXv2SQrdvs_gH95tBSpc6KxKERWw6_fxrSSAedqEuIf3H3CEETc5dAqFInp5LBWsLDGVnYBW-yOQ3vqkL-dQHxuKnIKjJGmtTV3qZOdfn7CcaaOh9taEwdQeielaIe2ZcqB7fVpwmExCtWqNFuR-aaG1CKIhFarXlRergBGB6mi18O6yvWequkPVfoguKomVPVhlZyZCC2VZpg9krkaeekg8MwehOoiWb08wvMO_PhH1xB-bXgPsYCuRymB25DFz2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aclk6r7Fp5OTjOC24oGlm_7PeJ7yVTqO3EKGFQLoqeB7xI1h4VTgwEJ04UDVZwm3uUHIc6HNkH7V2eB1r9VQs6oAUOc5YoK37fPlz-xvHL_6gpDTtgZPguTt30iUheZTVsTjL8z8--zd89_QOLU6MR631m-2ldR7kihrOem4Jttt_l2vFS9xqxAjVA-Hs0FLiFRTOqHgGdSeSR88aAATdMkE2IazUOYn7kuVhzR29k4Hl5X9DtSpZVd0ZAKjoc2e7HL4si_j-DIcdaGS6ZNvEp0vLga-kX5dyl1qcC6Rad1cpCFKcn5yCaw5oVWscrfKDwJCCY0kflprNxfF3s_zMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrtxX3FZ9ivxfc7jxd351GvB3FefXYgYXSU5WXsYsxUzSprVQvrqnqfYEaXp2u5VEHxd-DRdRe5r-YYoVlJlD3mFDtqATm4YiYVOJcgQBJpOMVydjaqWyaZAMqfTT7onLG1VPz3uZCLxfP2JtdBTBv6alLU0FBqZII70Q2QmSWzN5aqE5kUo3wNfAcjX3bvSFbCAzKMM-bhVf-OryZ1eJyeNqTVisB3u2zBxI8CERQMH0STgtvjVAyeEZGXKcpY-Cw-ijvmUQTxCvJOnYh0A0sdpPNFNhCq8Wi5_9H98YjioIjOP8OV4tfcRr-C4IMWmZz8GXKkGKpmOBR1k_FdWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8YQQszUoYzFSu4dOA5Q8xha25QbeQLnnm8r52C-KytrlaY4FdW-udiQzCULfNfNQALj-gJjxSDkJtlbpaQMk80NADXrvnWLTXPlFdgI1zrri8X0T1P_lXMpThU9eoX19DTTYiPoYlrNAjubbqzJRkAF8T__ggJ6TqEfwplFYdwqToqdWaXWw5CGzXq7J47SHOPepsWFB0PI0xkZKsAS8uBqokK2OhS8rQ49X7LTgf5KciCHUwKGjEo1RQt8rfqYgpX_yWZZNmLeYJbKLYUyVkA6gMUgKtxL7iqr4kY4ohLyWczyC2Kw1zfJfz4lR7qxnmg72v8N1byJPuE18voxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7QKJlp7UmH7NE8RskMht3bTHv8sdnEcLALUowPGCbFXQqM2VwrZHKMSdTV3r5Na8mruNCNu5pBEOU9kEzx_v9qyOHJmvXMJIIhnGoTfFjPdInkXFxnGcpF7yUuErhSO0Fhb3NctCHjLZsaAQMkHADKh8UKhuVoRDtoI5JPrMgC86EoRQC39F1Zxw4rcv198vJSasJ1biti_N0l6UGybzMRC0_NE2NOh-_JD7I9eCT9yurztG5a0g4UVaH07_6ZJMS-7a7hQHQ0XBLdztnx0HzYsdw-03J7Fr_LXZxEFgydyuTgYDi2Lz3hB01boCZaMOR0SY32CuSqerm9tNbjAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfyto_CWiqKMnlqFVzm9kKGRRQgdX12Zn0RPKY3AuZUEFDhexXbJZa6ox25TT2Xbj6UzZn1202C2YMohvUpEKOmV1uj2UpB0feMyoHWPLZXzLNRqqy0PPv25M98stV-fBtKvH9IW0DhBe3tUmAbeI5pYBEZQRqb822hcHgepNqdqtRJXgQPYG8zE-9MNKu6MlhoYza1YKdfHUcGMx1yPIEs-qJF9IGJlo-hSp5chtuNJ8-03Jq8iO0vGMSuwuv3NuqXTIrR0w-E5lkdWswrN05qAMbKEuirggRH_nbw3IPdl4pB1RdpG6r5NbuvVTR4CPwcV99rPPhJBxbcaM_Ao7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=u-O9-01EtuxYh1oiLIqHjglRTJ2djDgGuucFieeccJoQ_D1kTsI8xTw425zEuwohSZqlh2ztrHHddwFDFgjBY9psTn4fBgB2DFFqQdmdxVh673JEHqGH7bX4IT2GD0FsEgCviaOROUTbQcp1VJds-a1yjLYlKD1NhO_EECJsU4qMmQxMSl-GkvcBF6WQ3Z7eeYrgGOgGcLW7qcxMOcUCy2kdZGmUC4NEDGYDYpA6C6v-16qbppFtNQ0MKO-6g8WnovvniGZyqVEqHkisacu85Xdk6V3V36vUWFBngD5dhul8Jf2aIzRBqFuBZsX_bcyhaG8g0a9tk5JJ3lci3crm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=u-O9-01EtuxYh1oiLIqHjglRTJ2djDgGuucFieeccJoQ_D1kTsI8xTw425zEuwohSZqlh2ztrHHddwFDFgjBY9psTn4fBgB2DFFqQdmdxVh673JEHqGH7bX4IT2GD0FsEgCviaOROUTbQcp1VJds-a1yjLYlKD1NhO_EECJsU4qMmQxMSl-GkvcBF6WQ3Z7eeYrgGOgGcLW7qcxMOcUCy2kdZGmUC4NEDGYDYpA6C6v-16qbppFtNQ0MKO-6g8WnovvniGZyqVEqHkisacu85Xdk6V3V36vUWFBngD5dhul8Jf2aIzRBqFuBZsX_bcyhaG8g0a9tk5JJ3lci3crm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuWK_MJGyya90dKu9jl4xK337fVPM4EGIUlg_HjjD9MpA4uSF-5trAYexxah79NaMItmjpeQpwXxSPB5FF9bQPZOnWgyA7tYaOE3DKVdKv4D-4-1ado9KxpZn3z0ubnZ6jEjxqtFnTk1z6WQ2orCHlk4fSp590DBxzeRyFIvn6CxEU9I3yv7Kug_yIrsDRXgL_YzM2fS5tAlXHKOkGPC7v4aPR5rF0g-9_zTr5CcqPqycOlX-j2U0E8nFDAlceS_W-dih-MmK6Kj2uW-RToMBlbFKBMLpP4TyLH2UrrqlNGTKqdyJWWOvIcWV3D7kwjYRkpcRKamc61L1XJX9_4Siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1vD6B6GkeaK62DLDfOgWB3_20YtnP_cnFCscG95Tb5x5Q7t0ZpArKExp5BCwjMs6TCMwujWtniulm2rUlmOVjD9od2qEEnRwMi9nKJQeF4jC1-z8A2ffcKjU1SPJVhNx2tzfqbUQRDkZN9-MxNFYk-RnzZM0HIbWqhP7gBjZfJ7TABYNhXl_dJ0b-7XHsUqWye8qeg29sMqDJTG2sW4Jk-gD-IzcR6Y_LV4CdnStc1w70zHPfy5rKyhOp9Fmp9hgdsbthoS83Xiq_5WD6D1fKF-y3sPCc5Soh3YjhGP9IUQzKttcVi34fsD55ySfo1gV0suZdAHDQMO14UmPYSQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENVP1cJbcN47mhh1YBHzPPzyh3Ny2UL0QybGdQaXGwiF9-UA66FJNZPuO76UAplslcZCT2uDIFFheF082pApEmakAtKn97iRTmPetqmti4aV955vvVhGg1OJh4JMwu5aGj9kPLvpmnfK5436MxGPtNY0rgQpmNdK-rhi-mmJHhGo7PrcaSvf71k_9iEQPBUO_Q8pGVTU4RbMmdzRzVraxsE8ojJZDwsbCNV75yFc77lbFpYRJCfM9DWE8KZsqrY_lJXC5P8M2y16sSaZ-c9MjvCQNB2b-eerlqfK48Rsa7mBMsI-HkKrjvP3yg8bP0iwNWq3bBwjMWmTsyetQsxNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEyKeJebEgefFkaCxtgEkA1lpV37SDo1xrDTTL0zzDSZaZf1k1K6E5BdzkBNtld2KlPq4WFr3N8UhDhigSUsxqqMjn1_HGQnR9kxNKeJRF2-N7t90rt3chT8c4B3ALEDr7bLXctscaDyzm-Za6NX_c72GR8DaNoubSj2Xybk_plyWlKkLRyD0t181PU9C0Gty2lsOW6yCx-ChtFNM8cShWIeAHZqbJTQDGGcuEn5Pr8Hrt9UWlx3MmM2UJVosGkFnJv9SpMFNZUzLclAw7o3SokiZ5qOKGVJ-e0bZbN_Q_R5ZrnRCyKyxU19THud73h5imB0NyrosI-S64XAAB3Xeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uu8-0UGjhbkaLewHhvfUnByqwL9qby5wZfbWlotfuSU9fdOjVGTCtVERGPeTcoprF2rgAPYtBbgezVTYjY3-0L7wzde-dqlIiRDlSk5o_ReGrDoV3H9Eqbt-HujyYbNyqFhKuq-2_SrqbHSYXoLgicsbl_7VPLv-nXpSO9hoWN6KiOw3G_XPNQ-Ibp0VliSE_dQza4wvfeTEEDz-DT8HuTby6m04K4C7TgczmJUH3QU9mWEv96RLx0v26__lDd1yCuYkQVTo0SAA73lJ7-09r_N_Jg5ZELr0QbhCj3LzGE3og8TDYvlxngPlWVweFprdgOYEb3VHr3mBR-gsTODciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg1qOpK1HQCpFgFC5ch8R0EeWM3aC1Jj5nekXDTk-oQhFFmkbn4JJYTITKO727sb_4iftPyeG2bxNmFY1Qoxhc3PZagTLc3Piq-0uoeKfcE6MpK9UgAzAIuNuLvCMJJ9l6LrR-me2JHjq0mBit19Kx0wGSrm-l1VgLGGc7v0prX5cgdLu2QtyOOowrs6qMMENmBrDPr6C7T0KJCO-aDMKM98X6L2R3eDjNejuAEOrv0cdvRafyI9rG61UG8YzwMHm0qk-T30Mkhx3U9SIBpYQsQEyTqn66y4HgTvTXmyCpPljis9WsK1I-PvI83C5YJ8Tyb5M7b4ounOsM8aq8sbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-EpLWKuf0SXX5Q9g639JYCYs2WMVjLbHIzS4jIrFdhVGsG4UieZ_CQS1qrSpVzUJXByneCTRTp5rEZwMVT8bcL9_XmUheYC_ztvkeLUzG4CLMuMM9lIDRm4kFhru2-v2gO5RTgxNk-cF-GnXZimYky_6VwoqFeD5U66vSAyhHYrjkWRRA7in11fL_UgyVY-FD8c0rO7dTTPhg0KWo19BpSbhKghc-XeQ8M1O5NXFQNh58MncBuziN2QC9_wYUtNpP1LaKnxl1j3gVZWMPFWc9MhQyltPorTbHuQH_GLIgVdpN2DR1mspXcjac_F-YgQiX9JrKd7EQUSj7E-fet76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6iTacoSV1zuwQsabZSp7cWK4BrheeDLmto6NSLyl_eitLDy9FxG7jxjTFTyGaMsCR6pqfB7TTvnIcTfGBx-YGyJWndoawxmyS-K2OYy6qd1i4S36cUz3csGhgxQhfq1ikPQKmeKlTObejnpHxSEtad-uw0BP02q5Y6CGpFIWuLAlftJ_Rf0PD5Y8rElctU5mkhO5nGURL5F9G2cbg2yprOtPADC7mRioXoTFKRPfNCkrD9F7ayF9WYojeZ4dxf8IcOFOWJNkrRO-_ZK4fuvC-yfQQWrIPapqQp7o20TwjJi1_tXkLdlMHHd6ygd8oKxUW_UJU_W3MLbkkZuz6FY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpdEk8RIsUUp4mbJJ8n2NVWRUvFWBO5HVxl2oL5c99cKxjtDuQNfupxZkMjBunVulf8t76P7GGTLl10fBhmskln8jqURMQdd2BY2w0tn7CSHlSmSUP7mH9xPMfnaAo5bhda1WoKXeoc2QT4ya7mijQLlMnDyqX50yyyj9KogdLAt-Dy6RmgyaCahEXrBvy8fI8XIT2jE_Az9yUXTotxPn4gzJiDIvhrO_x92Nf3IX06PjaYRLSXyjxB6KX594tmgW1HuixbIedO_qejaqs2i37utBRnkJ3GmcqTQbSdQvmsAdd2ShIJ6QF3tJKUqRmg55pTL6Gb4171OyCQYiATbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De8xmqfelYtdE7kAU27yM3upHLGRuIAVu59wPDEBEnjINldTeK1oMdOKl3pkTMToDZSm8OT2rjl1RLFRLmk9n_wcHL8OsECbcaQqcn4BOMKN68OK1kjHb4KCH2ZvFl64aGfx4_UUIpo4-ScdBhUYowIf5DCJvm3C3LAnze9vkStEmbvglIS-vWQwFR27usI05W3BAxiJ8OZDte4jFRcKw3_5FkdI7pto5zUkwMT0DgH3Q5Trt2LGKskP8JyKxp7x_xuFnrNSGEyHhyPhFigNRHnzptFkvpGSLqd86EygEKgW_D_gVrwmaCmvc6YRndFTZLWYDSjJD6yODHty3Y5dZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9vWlh-NiJ2V27d4voq-TIV8USRY8QHvvr5tiZEy5dMpixhF8NSJ4hHO1BQsppvAIB-rL3Ch7dIKtNZuAy65og9jAcKlQYXH6dc1VggZmIhBfhwxIV7cCg_SFRs-uOC76BhpZULA1bLk1iR8PssgGqE6EIl1DEJUi31zS0yewB8LSTsMAt1SKwwzJwcB1zOGdiLR_Q_VpOL1bvtV5Dv2Zyr3qgk6ZAtJoUmH4KB_fmwfBELBIIDoO1ecDX3SMUl0xIb2f-cVicebEcY2xybu8rpG_jzQ6WltvphiQD-_xQnHQeiYu4jNOjpx3vmL8lkZg3XbkZgW0hhIROcVvu_moQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kR75JIKLJGEKY-oriwEAMxYnotvvBudN246Rd6VQDKRFqpXG4y51NaCnPE00-6LZZ4EHYqOF-dED6oHl2gSbWyQL5DTeIxYbtGjzQ8QFp-PMszC5s4vY7OBgeDesuN3snPQcjSiu2fJc_6mADNhHGdYVwvQ7PTS4us8QtrZffEFEFMdKv8lVFbdAyuipuT14skjaXaSdFDbzII8eZHPvUe79ftObph_HxlXLnnV4LF2Lmf0g4X0E48OKLutPMvunz0U3W7_GWqUe0xhwrHLS9zFzoGAX5wSPVfvu9aE79GbjcagykGxMzje0dgFaw4UtE7nkX6s_5LMSTBGg_UQgIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egEVcDlsJQ4EKi9-zNqk4YwfzWaJjZifEaZ1G78yKnWv2k5AM2TeSPAWiwv6O8Y7qK4c-7Lt6a1ZeVyAL7FJ3oeXGD90y-36FA4TF-SKbrX6WoW42oAuBdcAZAkP_QoYdzWwaUgydL06Welcw3UmC5UmDE81tBl_l235nDQdCwKnLg2Zkh1ES3L6ZTzVTxNw2XpwDIm-DIIpkhKkIcmmJcJ0cSOI0dpnWFgHBNGIusRNqVezknLB7vfIAxADQQlqjZXY8094rxnfEykGf1ZpMVlE3JnUs4sUFZe5b9m06ONEbij7xp1sLCZkTXjcGtgqMJckOp4S_rUnBQumu_yzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1wXvrQ7ECL2--Her_9dctuUiRtZE6Dm80yFCDOyNGRibMJwAh9yFVRwudSaTK8B3n_wc_SxEcbb6hfzRgxrNvGOHG_U5Hk0Z5dDOa41M-LcNwnWSHhGN0CaB2-txYgnmVcWH6hL0t_iep43qrFVr5-IPobwv5aJAz5iL4j5nMlxf9C8nbD5a675qIqz7VcoLUKzeZHVoa-oYQpYiIcfb24q0qZ4E_Tg0Rwoo1YS9bSG0MetNtIwXszWaYOu2g7YYv9ILIk77w96fTY55TjO8IoL3bYpa8ZvmZ_f0zPeSy3yj53aMBeLZrU1jX4BMZlNOPsGO4IQJh5eRpOR7Bl-2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z64h6LzPrN5K_ZnaLf-iz3CVQWJPlfUMm7Xn1tYS3b2yygTPHINiTfX5fhdw4X12rqwIg89khtyKItFCG1Q-b5d1fJBaplxfGikfCWA6eN24bSwxCfxnR1Tg4OR1WLR7cjPdN_JIy8IkKgxv4a3LhfGuGIHAhaTkVe63IbWJpfdOdlfwGR_5JwOl3DT6csRtNBOVaIzACvyf_bU3wTY0l_xXpOtUXy-g1rVkcBxy_dA2Q34fMcl8MfNA9jP7ZOI6t2fVigFhsCn1nVHwq5yfpqb0SufYyFGemUL1iC9GdSmHVeIbdaCCb_oXQzyeKhcI1FJNqU5DzU36fnuD8-ujJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4BD5SMuyOXvCBDz5pHnLylelfjqNpPx3pHSDtE7bxbmKomhwZ_r1Ca8L9Nih4MY_9HUyba936v0-vdU_pY9b8zR7JnLxRSJ_lcYbaYpkSbiAaPHZBB2Hd-BY2kCBObgIcBFxwQBv358tOkiMiB_9uYMB34TrEb_Jmr9qPdMIejx_yC8llmrNT7AVGUYfb0dqNLANt8SWvl6JLZn2P7fDrI51R44ynj475S7pdFwAMAdDwtbmwsg4UtI6EP9a0eGdZF-sy-jlGpUVGaM-ZxxOPF_AvqXW-Luby0A830FU3oWQePawu25obDxqc4m0ZsMjb9No6HAwGVx1UEYSEJuhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22227">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbfkTY7uNhcG8edmd5f--YYDeXGAjKbO8K0jvxyFCC41MIqBM2p4nBzxqXVgJVJI-6IevAkaFhJdne2MpFWIFwfA1LSis0grF6lv_p-IBpiGtLjDuEM-9KHQfM3Wmb9Ns0-Jec0BA6rh0iFYr1bqz0_hGh5J2-obGD1gUQBXp059bj_l8qeaiQHstNUYxL97b7EH8tQ3urjupaZBsd6bN3_XvbNn-8clepeHvsC22UVOv_FxPM7evC932b8WVho8Sl6kWIjnaM0ajtV-9zoap3OA_VQ7uTSJEsLbzpuH59hW8geq_pd20CxscBrQY9RtHSZrs8VHTSo6Njmow5FOSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22227" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYti468LgJao9SEFnbYUbGUMWG0hvLBATZu_kOzjeTXE8gBVXucxQSjlbsXqfm4t9S0ml01ZuxKnth5FR9KHVYhMtNcJwL71qx6iNDeTvmGIPlcQSxmS5WHP0m3vrJeQGDLY2BMO6jlGMCarLrC6bO2CTfIxh2C46Z_FAFbqCFATtEqznDkDUq-BBYHVbBg9jWu9HRDpD6h1ZWuQ2ykUwNLnDTjFEBI6sC93si7EsCC4XuoMO26EdwWbHbvzWU5N096qgo1q-yuUnYzDTLb6NiAZjscG6wxhrJNPsr6goUHr0ZKiAh_JJZ7sQ_0nlmqIuJdgeKH6w5hkr9817gpjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZfYEeYGQBg0elc9o8lfkjTC3Kbr0ob-Fyhtmd1Edu0VCE7R73FVuV6A-phRm1s4Jghfa9eurW-hiQk0fCcSIfsxNIQvQHCcGPSMFYKt2yyyOf3eHsEVm4JYFgA0M0kcP_2oBx441s7Lh5VYIAotTCFyRpErk0rPXk8mtPEU6eW_V62G1JVvSpWVlJHDY1-sMPAusSm8QfLBEwVmVigRF_idy-aJ1OIcFglmsnyrE9hfK8S9Q49TRYzRqqd6ZHFXNyc0OZBe1c9Tfsm5QBxKP5h4j9jgD-lvhG2SmngDTI_nG8rwvP-lzCkzbjQoEp1xzZOjhnVIj2ZRmCkiCKS9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=W-VOODP3V9mY26BUouzn1Jb_H2JYjRgH39XOITggCzrLM_to1ux-vBnSQ-EzFXLOTi2NnQDKdAvcSACc2-6KjhVJ-q89Xp6hzxRB5ULRvhSRZzn__50CACt8xUmID9dz4JRqgDWVxVMsiaP1WHoz4_q65qKw99PT07A6TVdmmwgQN_KaZwSwfI0o1Lz1OqIE2bihEwfNjoR9laltv2k2Xj4PkS1bQtcyeNjq3ZuZan_f7xsJ-B6vAVvqngJtg1wCBJG8c1-kTlOezXkUlpokBQJ8WlAGc3NA6M53Qy1x3Q6rOAFP-lZZ5JBFmFJNydpnkBWT5yIfXib0JaxLicMeDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=W-VOODP3V9mY26BUouzn1Jb_H2JYjRgH39XOITggCzrLM_to1ux-vBnSQ-EzFXLOTi2NnQDKdAvcSACc2-6KjhVJ-q89Xp6hzxRB5ULRvhSRZzn__50CACt8xUmID9dz4JRqgDWVxVMsiaP1WHoz4_q65qKw99PT07A6TVdmmwgQN_KaZwSwfI0o1Lz1OqIE2bihEwfNjoR9laltv2k2Xj4PkS1bQtcyeNjq3ZuZan_f7xsJ-B6vAVvqngJtg1wCBJG8c1-kTlOezXkUlpokBQJ8WlAGc3NA6M53Qy1x3Q6rOAFP-lZZ5JBFmFJNydpnkBWT5yIfXib0JaxLicMeDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=jJDAuRlmAmUzZ4FD5lncBlSZ9wSYzIAeNFqEOYsgs-PhKnSxPoLk_lqU9lVucGUIon7G9ZOBRmaDu0SFvfwlB8sz5QKuQ06PznkljioLz2ZnJ8pyk0kAtgTMR1ym_9mYD4NCb_FRwMHRFugl8QYdzHyXRUnF95skcoxzofap5JMgZATsF9CUXZtIyP8K9hjZDL9ZKDNMQb7TLjCw8VzdxYagfvhjOwMU_ZNZfS6sfcaThGKEpwrunlMlJhN3wS_t-F0gTOOV47omLTrHTu0SsR_JCo5PL7KM79FzQHNXsfwfE5EaClouUPg7AqlPR75gTPKvD_yXpoOhwC8dnmoPzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=jJDAuRlmAmUzZ4FD5lncBlSZ9wSYzIAeNFqEOYsgs-PhKnSxPoLk_lqU9lVucGUIon7G9ZOBRmaDu0SFvfwlB8sz5QKuQ06PznkljioLz2ZnJ8pyk0kAtgTMR1ym_9mYD4NCb_FRwMHRFugl8QYdzHyXRUnF95skcoxzofap5JMgZATsF9CUXZtIyP8K9hjZDL9ZKDNMQb7TLjCw8VzdxYagfvhjOwMU_ZNZfS6sfcaThGKEpwrunlMlJhN3wS_t-F0gTOOV47omLTrHTu0SsR_JCo5PL7KM79FzQHNXsfwfE5EaClouUPg7AqlPR75gTPKvD_yXpoOhwC8dnmoPzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUgnn5Y4jCvWSK4P04FVVCFYzaLVbsLX9e1EQdfEq_KeNwEtb1R7SFp9kKhnjQQ5tseramTKWgr2q5a5DpuqwHDIjLDFNThxte40pFXmiBz3kPUFhmWK66Wqdak9u3egUnRGKkgPEKWXTNABH1QS7YJnWJGUGMQ-NU_8M4bNHnRBpDp_Box6VBX3K9uGo-kezPN16_1cDU296yGBdcztILdFO1S0B-h6WeO80eN1Ck6tIe6hAdSAPO2PzIC1gbHXCKDAE6QHlEQyglB-ZM3ZVXz636eBpY9n7zMjWPgkLUvw9F-XrJen_Yqg-5iYOE3-cPGFQEI5sy0eu1RQBSGMwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22221">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22221" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUwkyoQWyBOMd8Ai9ZqiEJSuaZNEdxnQZF20b8MRXCobImub4x_20tVFQ5CuozL3Qn3UrMPnnEj3Rs-KYc71wsnFbB1bXyXmLw7GB84s9Jod7I1u44DcyFWzNERqKuM0JlgddyzEbXcJh117hlnXBBFKxMi9uUNQUkNprxpYTLAQhGRWqRuN2RUzJ1xAFxfC7uSTYN9BvkHhHAoZlV8xtHFqUff9wW6pJhhSn7Ifm44yK45sqr_0hQvdzud87ItaAwdeHgQLY8LhNnrjatARIZTXO-gFxlKv5B7y1ar8RYVJo9RVPAVhZ_B7KnVhHcpsJBj2RGgg8JKia0bS-M2xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYks4UkYvi-xSil3K6Hb80jV-hH7h9__1PGF2CRPfSEgSNHD31zZiMdvgH7D5yiiidsOEHxb9vnl4lA_XqK6NGFPpe4mNPnzVZALF1wxti4EQmYVhp6hdy1nK3zUzcseqUyYgCP3doUxMNuWuGsyEhzmhxUDRAzn9u4cJ2VDXklWtT48HenLJpgtWgl5J9r7ml_UwsHbl4-c0O2KcY3qlBcEq_Yd7QUpb-LtIO-wiFdW_c4n_VC33_b42kl0P74SZypZtzBLRfFBLZZs-pgivokVfp7Zt0--0JpBkge4o4qtDCzK43eVuzFHaBRtQsTQkazhpS-s7aEo4VX8rCP9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv5YpdoUclf2DLsVguk6fNwwkPRC2Es3TGKhTiOND4c5OLZyh6ZiiDyn8iXaEPlijU3nutHhepGemT5s-392f0YaQhlNsYo7nZi2Jl8lLRDlysv39E99_ZAOMwGDAo8l9y6L1yqphZo4zKcMaCsk3iSOVrpB3RuJKAM1AjyP1EO_rjDLnz5M4n-FZEu9Glwx8iq6S8RLakXWgXZXdNzRCdDFA6fP6g1oVPZv_ZWJ0BhHei9E3epRB1ayJS4jHxjgJZ7dF-yeVgSvJB4LVwSTxWpdsNVa8z4mOm5tIxpfaY2zDXYic22jjHkdClC93IFnVnvf7Q-A0UC2OVOU5jDpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjlats2ZH7iEBu0XTaAolq-4YsRrFHty1RsbvUnUZprKpGNlNUy-qS3jDLI6TCoWZTmU__WiQ1k88AgoG1EhrUELzTGkm0XneVn6c2jj37BmlahmLhRzWLxjxOVEYNqyNJ1PuOWN6-E0gTVfvvIailzr7Vi2QQTfC5MeJQeIjtKnBcDzsoiMkRoxekM1OnnaFc9v1JL42hChMZw7vV53mJjLLFvD5PyoYBNkj0Yx8EX1EXXkdOf318elYWzVXzVZCqc3nPrtOWJl5UiVra1UCgaV-IWsAVOiQ57izka_syNek3igCFx6J24ROqKIEF5H9Dx1Sj0Wg9x4SAcI_XwmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3vMFgAmKsYAIsaeFYMFh1KRISsW_xVaVk_IwcEPB770zusdv1tXQY-pXtfHxsNXZL57yXAOOXtWMsJ8tisoGrOFWyHgsTUD3b35v29KOo3Z9acUNSil8qI1u1fGWazwOiXeVeFajER7nC6ezfbvuKr2uwzevqQ8Za0gPsWN6MdH1pPFrHm_r3W6HZJtnUhnSYPfH4FIhp3FuWNOW0cgw3mR0i28TEKEBrWQsefiB0hX9SZ3MXgW-UdnG0Esd_TCecy7vLEkoL84-zfWhOzxYFNsznq91B7_YELmWi0kbDXoO8Dy9kgs_EAMR0D8u4G9jtH11Bey9OeuuU94gn5UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEnTV2O0z4KZ5MulsXJQ-nXCN_52z1MuErezVn5uMmk1K7vVdD3jb-M3s8e-D0AJ7U-OGxBoFnasqRxITwYcgCNCeN_Cg32isNSGa9SMFPDOixLXUeeVlIxkyH55CXsr2sjGFZLk_Tvtcu5MUNhhyvVTef_SFxBUReHPlSHaFbaqbPngucE3qx-ywrmG5FJU4n0fUp8I9HtIk_PptKoxJi1RFmhqmKX1LTIDAPRd2mIdzaILb8mw10r6n9YAKXMzbeR0jP27fV4Zr_HKTGicpRbZU9A-zmaiov2tbRHeiJv84xYxQAVPhB4nyIvBDJTrU1ikpwm71xA5yfoBGTQP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEb2SoDRVWaWCOX0J5SRnBgG2_QW6AUWX1bVJYg12829DwgZlu-VtTV4bGKHZYxMqXTD7jdhszgq613-6PonLolCKQ-S2jO0yLiZ_KC9pqNBrNor9JO_0Vb6N6ML63i0y_nWk8o7nn2RWy3r9rvdZh7WQfOAOp3mFaX5bKktKT4JSMQ0iItAlvzpOci1uyuYK6xMl1Iga2ByeOGQC5XF8SkPx21RCv96xOQCvBF2i_wHrfngpPjnbzySQ6pRo-tunBEss1Fwa9zE1RSbznSaLHkhMKySRNWnTL8GbRynO8h1e0pNNVjO5PDRWpJlMNZSfz4sIqxkfx8SqjZO_OIvXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBX0LEFz7weFXZSgLiOjC16E2Flq2UuLo1sKhgO7TIp82j7lC7Ca1CjBwfTjNT55ncYxRZiTDjLADT1Mpeoh5YBT8thwNP3-pUMsNPuEm5lpKcwot3s00IqJMzjMQsl6dZzpCn61Tpwb_a2662jzJjIHTr1Zcr4AqPlcUXoCCnjoCwrzvTvdmoW9YljzCWw3beS8KqKh_bYUvljJEveoMsktE8cNKNz4IOipF-ZQpOG1OSlO28Hbj7vrsZBmm1BOVP6465zvab9DLdPJsgT7IkDuEibjLKfshQLiyAvDubfGg-C7utRA8qfkxV859YEvtkHnSCGUhZkY7-OBv6O4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOU1qMbPZDydHn9kB6BVyRWOHEJ1ao-urnb4NcKsKSy2S0qt3aIwI09tE9_B8yWGarbuipu8_fvpH--YMLZBNnH1TpQMbEr85G5E0C2X7CI5IBHPaDUS4XpIZrIEpCrikxaRiKB8MLEJvbNFC8jGZo8gvatdC5j8ROKLqEPhBnKssnrAWBDX5QxOh6Kflc4Nir5QzhBQV78uA_Q6q4Fyy7P4HeqaKNJk2hrna12ub9ty69IaLljda-TuymEwwo1X38IzgB32J6_q5cINA4dXH7AonZTP-tcD8vy2TCi2MoWFHdODe7ccPMljIOEnAN2oYg15q-PDsJaj0ikbfqnPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1hMJKNeV93V2Ao4XfzZ12PbvxjTnnmOYm6gA94gg-Ll6R8VYBvAkOGv_Uf9koqHrIIoSXamOWv63NEc_J6EtFQVH78CgxfFRgOK3ZeEHqofVHyQ6rhamJl0g1qW6qUX8C92rjGZ14T4FNkGEnsLq5D66B2djknxR8dx0ZLy9np4YrZ7djwudstxRbhKQxUlSCCmWwh3o7fRbzITvxn1tAPupF82idUoDWHHcDrFjULnPJYyXK0pLeTGI9DOgG0kT8vbkZ44lWxdcEjz2pfPiHft7FsyiWtTw4ChvOMWBKsORJ7iw7JjevUH6GnOw5ZDC-aGlHqf3tl0LZHu1Ei0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lClAbhLtfVDqJb81WP6LFp2cipbVGbRz-whM4ZrZ_zosjstN62rXfeYpWyaWhGsAo9y--b-IVRgPgJ7Uhmw7ItnqKZp3CIuo0hRbYsAdVmfU-T-X5gzN9XxoevoWlzME9FSHsHr5RScnuK_icLENb_m3YaU_rwrRTu4PBBUcxhnJzMBlPZFYGKtfpKxHHqtr9Fv12bmL_dPGdvwbklkWs34svJVqMzn95nxRVtTuBzQWZ94O-sAJNVblZcfhyz9TzWvRvhc0qC95xM1-BJexTX9pssltqpTK4aiT5WhEyqQgZyC3iwNN-lU8LInAnyRgIorWht46MZK8ro1orsGNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX1E48H6q6NUk4Fd3n8avhiT04RpLCKMU43YIdKEM-ycQHTZVUB9U5ssmK6_0ZR4rPDcr3gq0mg8i6yeN_iL9VEih66QAIMzHUgkvyWOOdKODUHtSd3MGos_UEIGcdzAIDC2T2fifONDFAg0H3BI1xAEdCT0qde_5yxyx9NSqlyfUIMEG8X5KtNPq9Hk-TA7i7gnSI49lgJIImXcsdnHVbzZu8AB4nR9Mm4kV9D3EvjFExZET1sGRqS-JeJaOpe8IDiRqk9ccWJG5SbqDAT7cN58RKEGP3IsF3DcOr4mo0UdoMfNvO_OtJiqnftjwv2XPHBHwT03eBlebVfSBnUq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-FDb2WOJ6h1YFrXdEbs200NBzUrS9tHr_0HvWWAd28Vg2WZgBKnt8iB_240yYsoTEc_SPpZ5J66US1PMTS248YWdPnKj3sPiM-PsVQej94HqnJidw3R8Edyaqt8aSTg68ao0WFHTZJpa1ku9sYMMwBTZ9w7hcqfQfCdaNODDBDtVkdlhs3Ws7jpuwjUiwUTBTWyZjlwVyOJ1gvBlQerg_adSQhrj0oeCE4t2-OQraHCK5XtDHhdpWJ6N3WvFbcFse91O31wJ-uJxpi5BiI1vDGcVjHHWXSwju5i62-3XKnKLIkbT0s8zOPrYP2gV-Ozl406PrG05IeqM2jgpKURaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LchpbiN1n7CDBwLwD8wruov8a7fMgGgOCn2Jd3YmTzfqccAl_YWiwUXgqnJ7IrH6h01tCyKS2ogjEvujXAul23h0mQx-Ab37PB3B4wWHktqY8gE8c56g44lt6ZyierMOfZZcZay0M1PxHiuTHDf6Sa0LYOQjl1csbQ5_oIpXgIo4LiTa1-wxls4VVWLW1o4wTyReqhVXdo9jBGfZFRmcgfONKOsLirfE7-gSs0X7hLJ6SAV99TvmEAUppDsHJ8I5Dq98ZGnJD0tkI269vRLRFixdgHn3vKF945Lrji6DdXCiEX5nxJ0Cy8JDohs91IbxTeTwTWEWb_4TguBzAqmdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpqzBXU0-eECqP9L8bijibGJVY6Zf_Lx1UN8eCbhTH0ZXk5hlNP5kwhMdPKDWcsEaq2_XGlf9GLStiVyu9t1GfaKBraV_3dz8FhpDJxFP8-4N3LN-jehWP6iRC2D8o5XsSNvn_RjoP45z24Re33DyLuFvneIGsO21349Gn6IP4A5i2lLV3gQb4y7MUkCO4UUp0Q3OKpckAkRht2RoCp2D-SI9dBi5XfuBJPl820SMymdJ97aLXqNAkXAHgDB9d4CdL0bKIVHfudYqtBqSf2SA59TF3LWQrV-sAJQTyUNnk1getpPGj8tmmEkezrNuR4i1kFDV2Ipdg3v0QBea1fheA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKKS9gAfH5kYzkLUzioAy2hm29xLsrhW_VUpH859q8ngKjIdfLFfoGu13G9-5JrgLeDo42tBNeOKS8rkYZfzmLPPZYiwlrug3IUQo60_TRfgqwlyihMiI4JK8p_0rtNDWhJ7qEF8pArbYoxHmovPefuLFVkftAn2L207_1y2KuRHlRmgwqJnFwL44Bh5EnjF9Z0uKWSj5pZE-1VaqR9Jxqnlw-N7WIOGeAfqmAxXbhvjw_bFGiqnlAyHY7A3ZJkIhCkZMqdkTSYddCQviHPQCBIhs8uLg2zEjvj4CWUZqzkUQOO10JbJIglxU0IvgfG_lg-PksND5TvA9EHWHO6bXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf392KmRLKGLFmhyV4NGh-yPdsqR1Vh-YpHtmJoMuh7G_yipM3a6VPY3sad1-67FXCzCU0rhDL4wUMTPLPSHKrNvg4MYpDhVQq3XKXvljOaFr2I4Ru9gPv1oywq70MQjLStMdhdv4E_Ckk4SQYQ68gnNX1FujNJV5lzetfszO8YyJtWjtSeJMTUL3T4J7hxxvBV6IrQeeOObv95hIU19meLCZNNIu2izPTSGDEYo9jOrFnWnZFpgvd57Cyl-9qSeVuWZW2Lg0j_z8LaSl0sdr7YzIGNE3ARauV80TEgAsf_A8wue6rsRayomLRPZqNfxXpbX1SdzgRtOHCFY7o8yow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjVYzbJaFpuNSvqF-kIJHGycjrhT2x-SOU2U-w-TkuQnyOA6YPyias5xSmGfky0tzi5wz2vJbh-m6RnmnDRKoBJzCiaTCr20p5mCQ9EoMp8VYrZKU8QyOHPnX3a_MnU-X9ZfdxILteFq2A5EIBlgje1iF3pNZxE22TQDAQD4Wh6-Qqdp_nOsmiFVlGXWOH6r910TZkfShXoiVO0szvTHXpqxwy0dRat2gc2ac8fBtkxQ2QVUHj_UrNrom2X-BpZse6moZyTdjMpWuIl4vkrQKn5mDh1ueD2qIkwpN_0DrLmb3qGvsv-LnFw3Ma_vcGlaB3R3AIAyKQZ-2Ua0_KMp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfcnvzeMMWWGguyeIRdWn9vTWQYhHV6FCKhOEUbopKtayMTDyP2sHTEPzoX4UWkJh-kUmJNL0R6mdKYb5EZ0rlB5_5a7YT-OHpybvhECWpaTC33ywMkLpNFbDaMzSBPdwbnQbiGLhor8M4k2-Lo1pxATNQ7SLI2dVrDWpSQRm8W34_LzwxNZyoFTT8EpZmfEGFynKY4PUWOFKu9NdpjkP3N6acyUfADlRHkDBut0cHTcU0_HzzQ6MHYzljCfh481dQwTRgoNqzwy8gwODFdXT-2Ce7bHpF4ugcp3tSJV5uUX-rRASe5Q5e9UqteTb73d8sPpPrLL1hJPg_OHMrlnFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewQ8Q3qCOQi1WVi2GlaaobOLq6ae55PQB8KhX7pZhODVKIC20gIUtvTpUKVI9zsIh9UiDuapqoGcXaaYDfVOjjWTc7nnntrsx4yaj3zgNLWzKUkhBupT8FM8RMWFSVrCQSr8pg9Xh4p8T5SsVqAbvSPVG7zu1zWv_9Nut4E0hS0YdUEcFQixbM9ERscKhqP1GOmETSZo8CGWCtFq2w7Vaevd172eTdCalJYBGcs2fGE9dVmEHYEoMpt_6yXFczH4GVggPpXIR-2qUz-lInazPbWYF1DieKA8ebNtoZTJ1SGLCs1mo1KQAI95Ij1EHzYd_CFyJ4fowDwEkRtoa0Db3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBlMisIPO-_8OKwbjNJQrITmlULVh5NrNNLMOF43VgkUpzow5Btx7USj2OoS7g4Q2nA7UQYW2e_2DX6KiW2Wr3R1niDiLzO5_LSN7Sqv0yDMnq03j-a3PemPtdgDUF_5cG03up0RwX9NRDxjh3OWyRmnh9wgheGR6eV8HJK3KY1VkKfwCwQkEMuxjA0M7R0ErhC-cTBD6pmVyWbHC7bkQa0DfBn9KptCwx77C5ns6xTVludc7M4xXabJQPZMU7-o9E6rjJ833ffTgv3CuF5LaYQyD0xZlzcY1ihFSRubWPjrSfCkNAI-DTuqlcUDVXBXrQC6VcWjTualKVDkdGth3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHo819s7hMXebMluHEh50UyadS6QVG1k4ZZKc2Src_OXHoNJmcFloS7DMim-rXI_lEU7WwIlMPquFxVjpQpFm_k6U8WvOV8U2jXMgtspeYNXCHCeLfKeMYWDFuWpFumbrCg2HmyShAbR8c5_AUfQF2Q5EdrX7H-2CcdWUGvoOB98AaosfXFuSps7POMQKkd9fzH1NND8FA3T_lwEFwVm17GK20OWKl2oIvR0urMz_qVeKPZUsK32ZQ9SPx4Y9jFMH_4acWu_Q6Wx9Mng53FhZBPWkgQJYrTfVdVGJgaOIC0GJQH9XfJriaNHqJolIYem6ezz0E54a779wO4DHuf34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whwxl37Y7PsOId8KRnBzfsNVHGPuQXy9mwm0ZqAy2t62eMnTx9hfTYGQQuga6SJnjzl46XkNG-joOM1Bp_YmNPDpNu-RImP5gXZ0_PqrN8jaBAiGy-FkSy4gpeM_qjiQYsuO1ZQCSLSSuSUfoymSqf72UFKYTQHl76F48TdBL2r7f3xFqCVIRVWtvP15IJ37YpzRym2MM0IgLW-e4SJkBKXbQOupiXvy8f3GF_wdq2o7DrjNLD1lRAhtncOI-rWmAHcikFXZwKfhnZ_tft22VOpGN2R_y0ig1i_QcQLoI5giKgY0R1rXTlrhaDu5Nk8HofnaDP9veeU7B_fJ9N1zKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_M9CccPNQikbzSSR9XS3nGOvKxMT62UiulTK57qYIOeQ9mGVKXCeGQtqNx2b9cDpEMCFo5cZNd7jfqlZ-nRjdAMhWqGBvOp7ucXG25N4zKRbw8vPSKLnsjMhKbZYBwpDNrwFe9KrcpQ4kEU-IGPMR0D7Zc-91OK9Azrc2nYvchGKkdfxP3XWrssyBlZKz76n5VDqz7qALzuqIJ25ERvQS83_7nMl6G03cSU2OLFETOLs8rNITmhyXrVIL2JEVj0w2IiAC8EGzGTQtrkFqrwG_ci-iEZteQp7kwrhlDQ44xkLekawSReLRJesyHgl58O4yRV6RtAL3S7c7ZYHpCPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hkpg--EOD9eUK5fND9ADHTssP-lYIIrhsrxBGQZgsse83PXlT9u8jilJetFZsyg-MI1Z1zJ9UDOx2vM7GLQy0kei7ytsuFS1vyM9trWuA4WswAkN8V_jcw6qG_Od1vu_seFyDmrA89Y4lk99CatZlP1ttIj1f1hb4ydt07UE-zys4iDtxNNmDyLZbhanSVlJLTPljZnq0q90g2tX3oFalHwwL1tNkuejdEgYiPhLUVG98qgPmB0LTqW2xNzBP_CkYjo-vFN3oy2vXUwzPyJ1OdkxxlGKuyDPPpRuMy1ncDLtOeY4jU2SGTleVzX1PqdPF4Hc4NtxsmSAfR8fyoKGgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAdGJo-u3kuYaaObRvsgVRT8M4V8wJ6XNrkI-6SuZaFa-zxJVT6hVrKiQ2voZJMMV3GNeAv9sYIkLyf2g23-T6g2GrhfaYuHIWUjTo_oF8F0vmQtz4z79CYUB2uVYFPgezsAMXmnG1ytxHtEJl1iKc768byaqcXIFzpfiFoE2p5qIPY5rqZzdqvbo_TknVLUua5kE3ZPF3km50wzugwltRgzYX6dufOua_x7VYmFgRNsQcN1Dv_tj7A6BbUhlV1zzq3bWEfdecIQ-S9ukyTn1TDQ_kHZKYZojZlxm85f3u5xMIkcbnlNtihoa4N7um86HKJ59DJ7svKLpT6om8GxZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb5f9qPV4griMXSk_9u1ZPHadoEfk3HyNJoJTPqHU1g17126YDr5ABT5otpgAxsdcDEp0tQrwhLuHDUEPJ1CmufHNl7tT3xgZwze_U9RIBeO6ff3paUdQHio2Ob1h9xETJm1FHp-WNvDPHasRPMos1Ejf2iioJkJ32ey7lj4Ag55zcIa_IxlszTPvJJtZHSdZW5hRaw45gkhMYLEtAYzzxd3WiyIJFTt5wlpXMne46an3S0DwIwsb65t0kWM4gi7AnvCXMrir1sVQSbVTPNnjaCMR13mpQ3nLMrADMlxNS57bxlCDmKOY9OPt6kMAeR_sx7UC4cmw1cR8oZmyCeMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8LameYJHuCTO-W94Ne028IzHVBML0INJ_AROLMt7upPPfIgQuYGFKGY-hTdWKPj1TMbmiYicCVnNyH7RKlpM0cPQRIzLIT37Nx3dniBXzCmQ79DTDBAGA7w8RCSisqL6VwUdGf2u2KBnLiwxXcBcZjkcsf9-elWyWNESS8Qn6aQ1EZhTFzzC6eRZ4NsLknT_tAHrpw4eglhypUhQbeStsYyu7e1SNzXU-kmYa3x-JQ0zUVZboXr4PntDo1-UGE_tkPJTVhLwjq6NkVvpyGiTJicXwKpLHKxmWWspw6_V2I8-Wr3ULbzQ4sJOEbe77-Xuv54k6JeGQbpzBTGKvt7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6kzOhfGA53Yqe7bOByxwocn24lFA8woBYp9_V5vQ6FesvifU7vKSPVr40iycwiWDdkzZ1CqDmyYuIJydpOFUNZ13h7gDJOnFDurPdwoqi3d-Zem8ZLyOefEsiAkPYiklEsRNkdhTZ4Fcy-wM4GDyTjdWIULyeLAPTpJJWAXQgSRge1ET81JtaEWXYu39W3YXtXglE-X03vPfeb_ZVw7IWZXNMa5Awig6ZiMwnLf2f6k-20UcFvxzfiyAw0N6pI7HdJE7Ka6v9I45nLCu5rkUbix4OnCjgSz0eyoDRvvrtlheGlD6es4_Z0bOIBpcSGfr1K17_p_WWqPM8IRYh24Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c08W2umHA2NnUctOKfVkSws_TfliQimwWPtjopFRjGgBfAt00t3OAYtpeQoBAuOhI2coFHKKGg88mg8NKga9k9uCWcgBPBgFpu6_411rtUqYBGf2ccGkd6YGLmnOBP5ax3HlSrDlie0dQ5OguWpxbj7DYpag7FgeHf9jPdbxedYcGrDOxKzmq7ycWr8KPnMt30UzgbKk4-eZO_IO8Kx-fpzF02b0asnk7x1kigjORaGBkFIj_6PTwQE5aSMTjJUwdGiPJ6G2-3vwRvUsKN-_ZL2sNGkCkIGQd-bTRTSJjCML1SaZIRdA9gYR66eRlojOrRRS-f09VCteeQ2iPj7IBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=YYKoPpab7N4gB0HEIopYyihTnMPV5nPStEjUY97Vh-BdviqKRch6MnFcnG19uI4LF2DFUdSBopbv7CgJqUdYLexcDakPSK_bWlzp7JvqEbNbyVKCi6STNFy0BKrjOvkm5iHebwLSlPnDw5sNLt4r7dd1JxY64IGfEmosO-Y2a5SBGQSu1Mx8Qast-QhAhO_L5rJ-I4LsJB2t80i17YN4ho-3ean96FL0BK4XjMlZZ6aIoD92K4ISTAOLyaGp-gGT1S6ptIzVm3VuKRL4LJAyzXbq6Huz6dwdHeFSiinyf5E2pNOMC4rxRBoC79_BdEzZqa-g5kqnRvgEOMQqmlr6qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=YYKoPpab7N4gB0HEIopYyihTnMPV5nPStEjUY97Vh-BdviqKRch6MnFcnG19uI4LF2DFUdSBopbv7CgJqUdYLexcDakPSK_bWlzp7JvqEbNbyVKCi6STNFy0BKrjOvkm5iHebwLSlPnDw5sNLt4r7dd1JxY64IGfEmosO-Y2a5SBGQSu1Mx8Qast-QhAhO_L5rJ-I4LsJB2t80i17YN4ho-3ean96FL0BK4XjMlZZ6aIoD92K4ISTAOLyaGp-gGT1S6ptIzVm3VuKRL4LJAyzXbq6Huz6dwdHeFSiinyf5E2pNOMC4rxRBoC79_BdEzZqa-g5kqnRvgEOMQqmlr6qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-QPQG20_h2GJ27kZ_TN6B03Cfn1oFEztWeiK_xT2di34pcEjfmqSfISiDX1CkwMVJw6E2dVT_eST0FBIIx8WcGAC9mZcdX7gp9t6Y7Ybpc_Fsd806vZBbi80slPZqY3bRLq6SWg8pxUVvhU0v3xh0D11qz9geTUDgZ3b_IoY54exQcb5VLc3rrcq14QSpRJqQ6in4ckfSqDmcouNCauLizmRu1heoCqgjD_RIB415D4PsJZ9vTEu_Xrz7ahQ3OzDBmoFhJEHdymGLbGQZGXfJuhGkabUTPu5O09TfH-z5dHmSRCbiJPPVvHWs7YCSDDB-faFkTx5Aq8akOInXegpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss5gZZg0NAuNETXfjtu67-qSo69qD4JRAKTYKIbm-ypL36kVoDKYa4iDX0Kq-z6QtDjxXuzqABQVD2fNa48DlnJDQlVu8cRS7XM7nHK0IpuImrTlaBMsfSnzlkpwncs4tU8CqRYDAHBIIuLysEUbqLtIbE1qUj8d2fk8kznWarYk5BIjP13FMjWhwvyQ1gnJLoP0ka_A3REDxWQ9VLlfQzphoK53CnVJubiqYZZ1oeah0Ua7u2kvYNLIj0c2gf3nZXoo3CsCKdbkDh_xmNnFQZA8-rV6Vv07ujHozWN2QMaluOQ-gx3L_GjKQ4jqKZBIn_98x3aavnmpVx7qv5qhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKcZwFgmNuJ2L1XBmle7DSoYhRRQop5AONIjqWw-itifm2XahWV_7R4r7yafTekZhW7Et57L_GSyanG4yYig92zsVX_XRYz80_CrprwnvPGNkxGXCFf2cKliL2CD-UxnfAWKR6YAo28B4mB2ghBMjLbaR3etGp32lJvOOAs9EmNCHYeLOYHf1jSUfaVjvpy1YxOpSqlChagCFnjNaf4EzJ9h1Yjwr-AOI6wrZXyLlnRO2tp8LMuxhHFrAa5R0OtrYjGli7odvs7Dxk6xaY1yXqOLWAAzKArEhIqILQ1rDOhH26dXA4KY7y7-MdKYUG9W4EbfjWmDkyIMjCvS1oxuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am7x4vEJAIlMxxuI20iqXgxo-Cqbgz1CQTI-bPvx0_cgnLZvseqCuV0lXMZjoTqW90zRSMfZM1iapKIgcHQdY8NEzwNtL75PXQoJ-eGShP-fPxAsOlJBWxD2fMqL9-VSthNbMpg472UMCj1Vhs-oJptjOAd67O2r2maEyZ6wG1Y0pFMWQKCXQ1xnvRcJ-sZJy_k2vDQKQEhXfgu_FmoKBTK9L7Ti-JBSA5L0VhB9U7jdqDwrJek6WWj2ALyUxmwYBX3j04PzF82zwE3-m0h0HhWlmhmwYW8Q4t4l58AuauT7AfkfB6CU1IZqzKlaPmqctdFYaw2Ty6Ez8QZWSfwbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjsRlfdRG6w8laX3UBWb7QlGVI2jofdUYPFNU2dMpTBF6ERobruMyVixts_iT9IRQHnuj6NHmMJSQ4vRJsfKper3qP1cWJMU87A41VRSMJRWkKnemz5MkZc5MXcENNFkh_JAX0neLk9GAN1UadwXVEA6JduhC6QbI11pZgTdJzdoCR1nthiN2H4IAhh7EgN9wJ-XlXga6zTDh_Fdjw9W9tluoGALGdCNObk7x8dLOgSC3j-mSf3R40THoE7QfsYKlrm_rGAeK6Q1wXfu4kxRd3To8felhESigsWCF6MqbkKR1PvTmd51uVwvi57pIQnbjpExilwL_tngZmPQH1Jy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmeM8-iATWf2gDyP--Q-2Ftc-aaLyNVQlNu956VkzvT-q4BD10Y3gzxDNMIKYXDnut5a9VdLRbFyODRVd61oJm5VibNJlSovP1Hvul2Lw9Zu-pHdHAhJVRTVD1EzNtFeNO4b5owHEJhrpL-pBBZRYqQARwK2f41VYDv6d_yVLVeW0LsYa6f16dP3uMtmyR77irEL_kZvaFeClY6A7MtMR0RPWGPOjGFllBxeZXLVjfDSxFTbiw2WYrLSIVZFriK_2fZXL3jDnss2ZlVVxGzmnqdDKRiE9_lA8kXsMQ0eBKHqj9MILE7EaHOmzyn6NxkxM32uR3hasM1N0gDQvl5IMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPgSRABYeqrw5Y8ArhQdk75zHpGO1RBhN__jOJ8uaPReCf3xKQIfmMJ5I_FMJW2m6UqNWQiiIMtmaREso_pfLVSTKHozqb3xyoX-m0rcBZM7y6R5hcvmKg28hXNWv7im3HgDT5AVA5iczYAB31W4OTdyXABumyM4-fj1mZJl418Iay16Piy0-8P-yULrzy40C3eXF13fufTy-UVCvAtcePA_Km_qMphyGzgL4lAK_a9K3a8yvtp_KHqCtuCc37VQLFISdInzzyPEMLGb-TtshSZhrRqOjx1eEVu83yiionTRtpCa3Y3tfylNqZ15R39hWHBHEeVxk2BF6gMvSYHNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXAkC-XcBsoBllsTPmcfe3WqRKvInZsfTBha5Q8VJqeCXcIOLgu9PCWr7r3nGmQAQMKehyVQHW_4bx_6PAn-SKnAsJUpv2pap8ZLxD_LPpeL6J8C_OXV1JGzznN_qvGY5xAnFhnoH2mWv21muDLQhkOap7yUQGrEGmtrmyMPyT_oYY7_18x17zu3tCJipZ8Tuk5Muzb-6W48TKLL0EGzfq0LFLwvXf9W_P37Ja-SJroIDtLHJAZIcf3EhpOIRJhhlyslEtAcE83u3Lkot0MM26Wr4KjUm_zQ7RDDupX1eAghhy0yjXciRMTANy-GR33jbyB1kRQehj3_T_O-g_XAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx56E8Gkylr_XPioIM7yUFpzn9EjPxHo2enXuRIAjh9WB_2GZ43lt5jbnqUycprKAY9i-lwKhjzWoKQA74UQG8xZ3SbPV1xBDpXbQaElm0vZfv9ByixYz9wehIINXzD_JOs23vfsV6fE-IJEpGBc8x5uiHlyGo7fPYL_fkZn9xiCVk0-JRD_dgPZFHsL6m4TqhmUID6xmmzuiiU5mGuuKaHEGRcGE8ojpH_f_Px4zi0s6JyIavWPJOnXpX9gctXNB09WGxssavlLbi64L2s0kiB1HDV1sYiZX3uKn8z2VLsyf4tX3PFF7LolTSytS-j1jCg6lbo7kWcjSwQ__ThEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=sxsVMIRl5DxIcQL14PmFk5odwWiVXbrGbDlq0Oicd-BM7r-vKchg-IBneVddeT8T3JA_ZBiD3S2PumlIaqxTJtYXe0epFCY3_wUf6t7w_Oyl-imqO4tbcTi0_SoHPQ3j-cbcGMG3l84x6eh2zhzQULFMJ_qXxTthC4g8-Ru_3-4fWImFpJzoHHYIzB_rQci5nfY0Z-MsFB4pln4u8MW6Kren0ZFZKZ8nYzt5EKqExb5e3TI7bv43AGgkiZYj90bZD3MAYM7pekrl8ugnEEmWUmqjTSQ4lxO1QaLWXEny8bHs6z502EF1VOA27Ck51lA3RPaWL8Pis-AAZHG8Tm7Ubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=sxsVMIRl5DxIcQL14PmFk5odwWiVXbrGbDlq0Oicd-BM7r-vKchg-IBneVddeT8T3JA_ZBiD3S2PumlIaqxTJtYXe0epFCY3_wUf6t7w_Oyl-imqO4tbcTi0_SoHPQ3j-cbcGMG3l84x6eh2zhzQULFMJ_qXxTthC4g8-Ru_3-4fWImFpJzoHHYIzB_rQci5nfY0Z-MsFB4pln4u8MW6Kren0ZFZKZ8nYzt5EKqExb5e3TI7bv43AGgkiZYj90bZD3MAYM7pekrl8ugnEEmWUmqjTSQ4lxO1QaLWXEny8bHs6z502EF1VOA27Ck51lA3RPaWL8Pis-AAZHG8Tm7Ubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=ZiDkaGiTGPNZMrirbmoPFaJ-WpuR0Ea73mjCrrFUroiHo6Ols72QGEor9jNZanJ1gI8Igc5QV5BVmk0nQSlpm3BLS2aEM5GHV5C-PVx--bL4DesNZrrsA1UBXWutz6qK0jv8Q8skEgoEwhboeTtfwkyKCZovrBDQHCsm3nBQZPp14Q9Dqdz6Jk5eYCC_coekVGaL6-yPbVMvRmbvyIwqvTavq7keSdSpBIeeA4jxTPNcNzKKFr1DxxyyATsZWkDanvAOpHfcbzSNJlqF36HafLEXFrZX708C02V02OqTYRHBSHl6uNqFldwPoXJOgJWUiYz8P27LPIYYXz8lX3y9_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=ZiDkaGiTGPNZMrirbmoPFaJ-WpuR0Ea73mjCrrFUroiHo6Ols72QGEor9jNZanJ1gI8Igc5QV5BVmk0nQSlpm3BLS2aEM5GHV5C-PVx--bL4DesNZrrsA1UBXWutz6qK0jv8Q8skEgoEwhboeTtfwkyKCZovrBDQHCsm3nBQZPp14Q9Dqdz6Jk5eYCC_coekVGaL6-yPbVMvRmbvyIwqvTavq7keSdSpBIeeA4jxTPNcNzKKFr1DxxyyATsZWkDanvAOpHfcbzSNJlqF36HafLEXFrZX708C02V02OqTYRHBSHl6uNqFldwPoXJOgJWUiYz8P27LPIYYXz8lX3y9_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NznGlmSJakeIvWqbPFB7zkUPJSaKQmbimoW8ERvUnp6-cMQIm0IyQ8hp5PHtN6lKdmfGpg21GCcbdUHHRhgo6-51gzf8zLHudBGyrCqd2fSw0NbyklKzA8MFKkO0KGxRaBqpGIk8I0Wj5UFZtmvv304Z7H3yynSaOL4DsQBtiX17l6fsbavz3rawxH57_SKmK9RsGmHoTE2b3qI22Y0TM4XzDStR0ZGbjnYiiWMENtGJw9gb-Ks3O1hwXkgEl4ewwjWvBANohsRD3p9olPOXyJQBewV2loa7f_h4xuHDmvEVEZnS6786XGxRbt1EJISK0x40AOpKtg-Hs7zDyzvSCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1viz8CMPEovdvQFYhT6WxQoLW_HLQv-WbbjqsnOFWMJf6HeAr3VuVBkwfDB-IEXoSG3G5yogpQjfnbPX8xd_SM9QWFtNKVXHImbs5wXaAOlGL8P_jUxo83pWb1HHXNRde-efGR4deaPCU3RdaRHfqinU4ZLfarc6svPMJtcM3-HCValVfnoTmoY9fPghMwV_LdyDWjlOD7hNqnSMrexyfRD-BTNqpXYl9yIL7_Rmrwjh9KDxyojYZCbixnaXDOB_0unHxUuebFuulAhrtUULQTzL2GRDF0Pwz793wO4rgIUvB7jsLP5bdlnHDVOOhNl920kq-xyJd2k0c5-GsGiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3fxo8abGbtLv4UnwRUKifEgN_xiN4NHi38OEgGE4igqZ-O23xyRzyoHdoNwG__9jdsLlSxmZxrfJP26VlACM7LOBAoG-KxZKR3v8J5z44hZtLc-CRHGDVMnlMrg4Zzf6OaqQ8xik5-2jtfElC-VnbBZWO_9F-lL2ouwZy3IyI5_Aqu4nuM0PPdxOvUjwqmOzTi2siSA94K7UGdBUR0fTJ_nxf5zNSdI9e_Tje6bRw-WAh37ZD8ejVYdxuL6S_Amx1qE9nlbqodkfgmV1h1fIr7tba6loCQpcKABgGO6ASyI08CKa_DLgobINqygfa_SDmnHxHH-yh9_XFf717NgJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRCoAADQaMZbwoJOLAFVdf7huHXktGEiWsRZqmJqsu-Fg_6Z-BK7v7c5iCPTYWhF1utrIu7J9WIUWz-qk2QoPIGLZi0BWrwIH2UWTVqHxeTb5q2dLqA30nfrSODSrjDGarDvbW0qrTOcX28iyhvDBUwhhdcFU0LNOBeb0rwZHRznmixoaMjEXrR-b4AyHNZSz6xojJmMyv-_ptnkCmG7MxXx4FZfZMOYPaz33ZDD_wewe7-_JCCvYbQHygCfCsFi-oIpEmVaPMRm6R8NbIpcNNtrBr6FkxvpBM_4SOmN1VOJ7hnNWCth7EgWTKNPlBJC8Yp5fniQJBba9eQguwByIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr5g3PIIF56TrL_VT9thIsoAkrQApbkn0LO3MB8J6vzZJP0f98y4KS9UiSvbWqrR1nTq2-srNCeEMfeDyXMEO7HyrxrHm8uoKY_YhL-ENbAP3bqdTh22vYi7BlKL_l1iJjPtPTjldvuXz5y9_s3EMLipfooQN3m3-rVX_64GVs7HfrwkXA0E-jgrXQIx83wGKAQvzGWaPBoMnMVheRFco-umTalzUzvuLJvw87oIVGltjll4OSDsiDfnEf26BtxzozFM8DRc01guMGvOssNPKK69_P7A8ydfBzv7FwlBaL-r2mxQUpL2A_p19hsfTWgOcJjpgS7MCBa_DFe6bKFIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9DFdRuOVi--B9W9bj72AUEfYXDBbvO7VwtIW0C5504HBXLJRpCxlAAibtwJV2pYeeHSMsbs5L4IDl1gyzn5MwQ-EZBBnIdIYh3PdOzV230cQubrvcKHCsMrAARjEiPoHOhctzKcOGaJMmNoxwDs9lRVYSs4ui0TiDOwSy72dTg9kyQdRmdTiv0GCZULAKSGoyQ2R7ZjBxhrxOfoL4OHpg9M26fzEpkCvn160_fC6wYW3u2GdGlXE49g9D4nZoup7gJwdQFza7bJYk0vcpG8otKiglWXcOtalmyxvHlF3GjCnoMjrErLKf_xWQ7oH0x1nDbclTkM37FDc2nvfYvPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chu-MET1pidUpjyihgZEBfj9HTyuCsy6cGxaiWZD9hE24yUuznFkuach1X3i123v8A9x2mObG9M88gLN_YEDxMKrclmudwiDOMDGNaFqlXywTd_53LChPjZDEGsFKYuoK3Uciw-4EKXTcjuloLUAOIVf5bBNYCFc5Wi3tZwr37rxWJRhiplEbmfawrFMxbx9W_DPUEtKXoP_KBm4mjO1xk0BFnM5miTS57JW2O9WH01yPuhskXIQZsjDaoyn7Gqz0IOVkb1jqP8P8W8VLgnxDAudNDoNo9s246C6bmmOz4vae4uh6XyEC_7uP18UGTIBwsdDzMRzMz6F7VQYmSeYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrnDZxFFZfCQcOgfCcXLWO7OQPcOfWcSnKImGXxWl08R9tYZyrXjO4wTRGqGakKScM6-XUNqVGtWgbOiYy7TLYrr_FFnfVyWDJ28o0tnV-NyCcpV7tICPxbwvHmjSFJJcAhGuJn-PBVteMFBQVV9tptPhKD8wn_1OEj_AX0ndfzwbSeAxe5Y9DS28jRKtezidLgGE6oJbay8vLyDvViWuXc90xrlPBeCOcegKFo5qJ1TX3i-53Cy4JjMKDWQTIFuQ6cgiJvyKHNguVozkgOxWoS0HQ-8pWgHNqRheSFucT3pbdQ3s77qTBrnpidjF3YLXart_8uatICEHH17IpLMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De7PqezNiyUPtckIXlurRYLv4Itgh2kWcc6abzmznu3MjuB1MK-a353tG7ipkESFiIoAtKPZFeBLqLLmLg88UWosuXIxB6-PXFVv9Wkh3ZZSNWatjOLTFdnO0Njx558yvFKDIVWUIVXR2rhOAxBaru_vZIG0LF65qFadQLA_F_JcNdoX6qjrCuc_-YyC8eIuwKElTmAI_fPCtHDRAHaSWmh1YnoP_jto7T47DXXP5A4QQLFShqQYhtVZ0q3vI0SdGBrILkh8iUxCOUpOs_-7520h7D7z2alhFOk0l7SQMAFZGlIp4em5mYabVcyEMN-4n4LU3DXSa-VCbBfUD1t_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrxLCVkmsfr4uFk8XIQQ1uNO9ax7ibbyKIGIBg1r2EErjTu2maQIJDGUiKp7IRc_k-m4HuSJ2lU5mjiIf-NqTgJueEsxbmzMO3uhxNBRZKLDgfPPXaN_2zcRx6ZlwYJGRYL8SbHHjRoGnX7ND0dJ97OB2jYljS-b9Ns-UhHczDFKtIsqvNwJRBFB7ToZvc3HAv16njnGEbevC1F2yIxRz9iEJ2UGzEgGTwNRZ5j5fEc67EqJOaXXU_cLQyUlv3I-Vx0kIz8V7fCnQU592ltSEeDcVnA34Y5FKaefFvXYzVdHm1Y7tkrS-butMPXGRRVmVfS8v8-Bhl1rQZidf5XnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLnc-kXU0WGYt9N5I2ZG12K9Mf6peMR_dbgqTUN634FYhU-f2QRxvv-g72UFrm_pW1OUFEHcCKrCT_bl1Z_Invx_fcSRe87aKfWuH-3UfOYz9RDSGSFONJOhlXD-2CSBfywDX5x80IywHO4oPB49b3_-BZfFB-oFVeJ0ISJ4gB6YVzoRBpBIKPWIIv1q_Gkpm-Db2Yvjs1JK3GAo_idu3kLQ10kzug0lVzRNHKRAOLTmUM5AaQ9kDygkXvLvfG2ZHsAMpzHtFOJWJ9WbcMpF-gtdYnKf8s0ajyslzhj_Iyh6QM6_P11Y1THujy3ZGnlEPqSkHnJMpN1S9YEnWrBwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjfSU_04bFEZzDTAjfDP0EeNbM1y4fF6bp7Hz0ARq3F9Gqsn9YBrjzpActcb3wihMtwZMUJTpTKQSOBY9abkkVSlL4da-23vzdoEjRXvxF_B86e3pm0IkBhWM8iMehshM_Lsxf4QmZpniO2mlSD1wBkPxvKzNYc9nq1Z8SaWromEIxmPtBPBoSrJTJDYHBgP-F5h0b_wGcr1FWX-d71Hx3eDpJI-2QNKzTkScWSvK6FUComAGKrR6vztyRCXvjZLhOWf6kpmbICmJJlMao-Zk2y8eVQSKtTwTnGTpc7_vaKn6uQ5VDuO6kUAfu2pGOyoR5BFsNPS1NWMvKjxM_pYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEHSSwUxi2I3Vs-IQ45bWo2-cbq_S0ZvjKLtBhZh1W9I2NtybvEG82-SRxnoCHn5xCw_TdVLjwEdozF-vZbRhVmsnubbl70m4gsRYNinZQIsxiiWJyhAjW-p6GQBHoCaGu98qcb8W936KwKQxNkfiQYgVGspDilivMn6oOAdeL5UEVKFPQoYg_Ebo9e2sl41olkALeANhuYvlsVTD-jzjB-epGyOTTRm2RunAnEyMhnu1fjPYA2MhaO2i8-gLjsfAjqLkc1wH6JaCJ9alXkUFIddstyDX_OtYXhdHeHjDHWNJ3BibDIH-5iD6tDnY2I7Tjr9bvSJgZK0qh4Ye85m2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdhSd1Pkw6FLQhW_RO0sQSNGq_BAtSgLHpXln5Q6Nl0ZkcE2b9oXa8YyIMRmjyXrkTjZIFe8jxD72MQq8Bz_XMa18S2fgYcd4xlDHab8xGcRAvkzJzmS71Vkzud0c21AzfkptoVHXtmhvmOOBBmgEqjH4HgNd1vt3jz_yBqMDgcg0PzT7Eqv9OlOOXV5-bC6JbUtjqlToioxd-WZoFgFguPlEMF9xe7IPP9uOMxAwFESTY1GweIS4oiIWCljOZgUL8Y7lV8xFuy1ZLkfTGMNzpEKE82fdjlqNB2Wv-V-Pj1WrwRi1enwbwwlXUmftpqEn7jp1JFa7iI1BZeMVV-O1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QguCMJdhCS0k3UUObVAk5MTAusgcf-N7m_NhPHThkBRQHqGaqtPq8vexfGvDL9rdxFEs_2-7qdhx_d_c2WawRKsjZxq9BZMWW1kMULfA5kbGHg0H7WuT0KXX83Ot85u1JOnAfkX-8DSsTk9PpFy5FDdFQZJJSfe9LlgOcxnS91pUgQop1i5GOhJyqqUp1MZQc5oiX0UdGiGvV8yaFEz7KszbShtMu42cKVtHUnhJFmDG2q_7t-rV9Uh6Wke_qPeICtZwpPAM3TK641xY7K4j9ZiQZu41J39LrYmAZFtv2dm-0xSBKH8NjvAr0KW6c2zbC2EHzXkXo_x49LHpOP3MSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU5eEcdslGWFiJu12AXPp5f6HHXpEfJQ7detNH4XpgzV3mCvjEazaaxwNIRE2UCdZmtdgNRTvZ8T7LeA_4MwWK9IIoOZcoK9UMm7x1-aA4V75El5yxUSW7dA4bF9_j0kQAQ3ISFGLyp25oIatK45mGPljBjn1waidsEXLIMIEh3S89Yjj8eBPIUNNCE74JtSPEjCfMAk6_vKKRm4Y-9lbxLMjyXSUX6PkLTfT57Zs5MlWo-m6gaHZZRk3nKMhOVnsM8-1bNojMaozNdKvHcdmPqKwtOP8HDl1vQvXzb0aheHl8O1j6nDY29VlPveBc7TqKmb_M5fL2mnf1nJX62aZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM-ZMgIbu5R04h1EWRZLzdDgqfP5MhzxoGkXAWgpr5bu0cbL6LePfgK4898BgrfFhH4qeX1rz9ajFSy0Eo8xJf_U-1-CnHznor_1GYSjuG4iDdcLh1JD-cY5h-qu9vsiZcL5RHlJzEqgsqNzTYHUJUHtL6kRbqik0yWJ-JCugBkaniMbPAzxumudsWRvoeWcqzongEvSGepBfKqAHbyukbVlewvay_VKUVhQQ9CeFRER-jJ7cE4_NnT4JnHD5-5jNDXTD4z4ZsFG1hHuvrzMfwj5TnS9EGWYqaRbSr30rAA9BVRwMgGIALW0U2GwAKlfc0QAu_At9AJ-9KRpDxCKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oh4ca1DvRlSjrDRknnB00KkV__P5hvlEUteQKwa1s6Gv_ZS3x6rY0eu7vwzwZT_v_hMsP830HSeptu53qGIacLQThq4rg_zyYV0H9ygZxJVDT_cdKadfCeC2ES8-pZgchL9Mf6P0TE-CKNiNi61AKhIxJemXB2S0sPx5P1NL6qqbPV4CIh4p8L2Dby4MB-NwgzgBtzTaOwh0AhEGlfrM7bZZkHbk9qICV5vh1bbB5PRHV24E442MW02sUme7Nuwzon10NDZ7pPqkAfnZzyp2UfHGvgnpGRDVt-ZQ1RlPPodZrtJJpZyJQBkGcKKPRE62w7l2fTcDV29YNmpIb7lt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs1i4tPgvPZD-tQsAiFGWjnylTgxYUPis4Spp34MqRC-N0Gxbg7-vHhDdqSF_KM6VDksLDayF9qIZC_0Ogi1S0A58VW64bFQw5fi590qtF56g_JEV-Qe5CjWdGnphYSqU4U756VcZVc3UL9fTlqs0al95jRVsAfu33vTwbrwnUdpR2TTKq1WrthcYmRKtmy-H3AmUexiASn6YAMMGa1aBEXlJsfmDffPRtoJlunwxIf18PkhU-DoMD_spaeGXk08YBMITzbnNVQn5eAMb_Y6XuDpb8_AHTKx658ySNc9Lk7-jBmgtmUeUq2f1ARhT-DIdJ9cXhQpFW71dbtnC5PqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8iN0bpfqaCOMMet_JumUosQWkWBJzTEaXQLmwb4pd-yC4OB69EzAIr-Mv24GdVB19W1JJ_jaZsQm06baf2m7UqvSAFBw3vj3Cy8Rkdd-03zY9eaCOZpccoJOg3KPXtbTEQ8DNVSpUiMlINdvjYQfS5sZCam3EbVT_M3Kjd5Pt5muwsreCFlwM8kIL98MGda7N8ly4lrfeMbv7cvgXWha1a-TqiizsKw7gs1vkgIN-NigiGfZwQppAzUZ0gr1P0nYYE7PxPFMXPh2pJw2_sm4TnktuLKxRrRAhi0x60cHVpBegTIvi4ZpJo8Q4ljVJi-9oIe_mXyCbZiUvUFEGD_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyW8HOzkdWAomi6BKY6nzaY92F-E6nYDc3rs6cGjR-GS7Q6WNfFe2rR-q0zIwSUxP0jCW054cDaGHpj7vSY1uff4w6CiTAgq_-2YoSBJOmaJaWG5SLku22spHYyy7uy5mNFUY7EM_-5GTDLrD53-w1NEm_lHuyB0baiysXcGwfeK3viO5NDCdy3Yz6XspIRDd8P7xQYkTwBFD9ZinsI2ckoEALK_cEjZafeTu7t7Wq-KEv7x2bRL-D3FugOtTdTFnOFfzLn7SR0NzwgXwbgSmupz8xEp79WwxXl59sCpfP2by2FTDlDWbY_aDC_mEa-JClWbwF9CMJygAlHFKo1y4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fctM0QtiAngvtJlaI3Eflk5AqIv8uOhKhsG1lj5eHQKDyxjyd0tjiG8uvHnqQbGn997LMhy0mBjxjArceq6FWBttHTSfRiDfLoZpvqdCY7zcoXlLnLx0BVekhHS9PzfoSuRVypzUI365Wwa4T0OKdeM6zhR5EJmloI4VkZ_YSU1WkjnNvuIGs2hMw8GyHEKEhBoq0DpXWGYN11hN-YYrXNe7kaU4ryL7UXolnlfYGdC3NrLxyQcUT7WHpu2kA176Bj57UWuvt5_CJjv4IY4HUVBLOF4LnGkWx9-hRLYmErifs-iorZSH_AGC8w7FUby0tOro5204qU3pwEejSvmyRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0JYR5ngf3_sZF8qV7V2WLqYp1Vu8kvl16xqkqIu0vYhtVj6sj-lnV3eWHTCs2EPP9IJWAFZfk1TT-LlJdKdc7OKema96URxPW2krub9PiWWpCNGHgbZp5W9mSHwhjG7zhm0AysY4RyrxrSOxMNqyPKHWfIcfhS9oCCgtuSGiUmn7azS61qcv557Wl0c34kFDL4fYrs_kHWMzTxvWvJgb9FkCCIG2qasQyUSOHoLupMZkSU6GSFxsWhZw93Cxf6kQbG6IbPN_yN_F99M2Ili9HpGS8EYpu_m7nemkGx_xw2fcLqbv5OrEMa7F4vs7oUhKDAU5kFdRp8VjaTPzJzopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWiH4Mlgrp8uL16BiWjvWdBqS_m7M2NcLh7ywWu6O2fCGQI-l5OJYgv2t9M60HlSz-lKO_pPr5i7A4AXBiy_DLUHRfMmyJk-sn21U_MXJchnvPuazT9VbxOyc2WtyY8-FIAeuKg5b2EX0cbz7-wCcywlGr9dyGEP_SZodImmTAiylKpZ-tFVN1NaSAxi3WsYuRfT8KB-_X7t_HZp-wp3mj3jXKqVEoYUPDEVfOvPsM773yE7lXBR94l-tmaDFrSotcd3PGtzUNwhikIruKfBe99IprK2edJnng8U4KYJE-stFnpK4JucKEtwrHgNIbDjcDhOYiElDRkqEw6UZ_dDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
