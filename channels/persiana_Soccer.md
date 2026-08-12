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
<img src="https://cdn4.telesco.pe/file/WPcZrfs_eJ9rPXoSQzDSTH9J9gkSP4p5WxFxpEbqaDeobq7LlH9sanTMq_r8EGDEysZUL3r-CHwVxmlHKZxJ7FMzlsNOS5_eqnmaW3t1s99g1SFs_mLQGEFW8LarcdKuByXcZ79OIyVVfDLTGeHVbtSPpBh1ZTvhueGemk91PAyJICPL5nWMeZkSJ4wla34q-a8lrZltZVJ7VapHC1mXvla3Oz3BYvMsZ9bagef70e1bnYWufbkEdP-OYDhITvdGMc1cw1BkvVTdN6rCS3siYrUpF9iG3VBS0oE1ymhJObBnncdnhBcdV28_bVFxHm5DJ8pZvDblMk41MwLtm5yjbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 623K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 03:00:46</div>
<hr>

<div class="tg-post" id="msg-27621">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA89Z4HRk6e-pyNiRXHk3M0s3_vwLSv8NoRnqWmfhzvLgurmuqJ1IY3pfL4EiBssywduys_uEGUKCQ13uxt9fXMeGSbJp4RKdy3f5cH2xN9YRP6mqFzMbuSNFvpfNneHOmPsgx9xvFV6KQKGXBQOC1H28xCqCpWoHQvOdLLckfZ47Wvzui6ro_eFHFbFtf7mrQyKCECViiBmqGAOz89hUHO4fd4n-nEysTsJSxuZFJmULi2P16ucyTPgqzMCVT27oAUuzXuhJLwx9DXb5uboLfKuZkKL-NNHhT2GaCeL_vsr_5DnbC3rUIkBq-EtvWJlVC6OMeZUyaL-9zhOPgNp_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیرو خبر شب گذشته پرشیانا؛ امروز صبح مدیریت‌ باشگاه‌استقلال 50 هزار دلار به آلمدین زیلیکیچ بوسنیایی روپرداخت کرد و پرونده‌او قبل از شکایت در فیفا بسته شد. مورد بعدیم طلب 25 هزار دلاری جوئل کوجو هست که‌طبق‌گفته مدیریت آبی‌ها فردا پرداخت‌میشه. باساپینتو،…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/27621" target="_blank">📅 02:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27619">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzleGhx9O9uwhXBkplRms71HwDJkm-YNqA5gtxchVn74bda6Z_twXXVngF0iF2YKYnlaYGe38QXir0TBsPpksKkXt3y3xQmpmqPaFlcTWJTJzz6WSxy1MKGoBHShlre6pWlgfSVoVVM_8jX900TvYOWk-GCyZO3ruRB4XvPGbQb8um-9IzKPLCNPpObgv911KWiecm5B4uhRNMqqwal1P3PQoeM0utsYqwpSPasErqYR2AQz46cDzPDpiclwaasj9ILZ5Dz-q_taTfkrQPyukIyMdc0geGhGMvqoIy_f85ORp3qlENPWIuqIkQNeLL4_cFe2_tSs7EG9zxeqSuziOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/27619" target="_blank">📅 01:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27618">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnfs_zruQ5-zW2oi6Wq-qFdOFCC18cDNchDAxfXj27-4LwxrjUhOvWG8hgGk4HLOIcznjAJHlymqN57kWSitBiMVr8vAW0ikTvJPC-5Nme3bwrsX7HBdfInhuHmNDc4_35YX1uO3H5W_JwINRDNGOhnzYMhf9nkNN_qQXgx7r9SC4rl80HpY3lz2AEpTtuV9bHLJ7bgtmuh9i6M_hiMgJqdlp7TcQthskb4wwhjLeN-ra8Scb8QjqRQ3YmqDc_-RrEWdkVsT7t_GvH6pzstkxGfzuFv7JvQ6x8dte0qqujXAxFTiiSAg9VRTtD4Govcagm8zbDPK6wR3rNEEPV271w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
هواداران‌پرسپولیس‌وتراکتور در زیر پست‌های این دو باشگاه اینستاگرام بشدت فشار اورده‌اند که محمد قربانی فوق ستاره 25 ساله الوحده رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/27618" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27617">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTYO4bUheuBGAJZk0sLcEX9hur1V3psVx5z_-psK6JAQEQzK36E6ZToHRv2XJcAbw243bMWoEmB28TIQ5Ufs7Ev_5675WKhHQ0c9EC_Q_LC1QXp93Om_7mV-Lcwbp-Y5gplQs2B_sIRn_FQlTqzh58GIF7Mlpm1947rutsEYTJkk4xYStFlh2DXcQhfnDW4gp0FE_nBw6hd65A4TEzvd3KOmFehHvnwm744-8HR1OzdCz6IQ8q2ajJseAwHsK-nx9Dl93EbvY_HIb8Fx5xl9Mf0Ack1a2UkeZ6fyjLQD729umM_1h1nkd6XxeOlkM6vX5ZqFTtePURghd4dpjnOlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌بازی‌های‌امروز؛
ازبازی‌اینترمیامی در غیاب مسی تا بازی برگشت پلی‌اف لیگ اروپا برای اللهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/27617" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27616">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7FwdaDFakyEg6DX2lI_GivHifSMiAG4lidfNniDRKW5I1vnbGzmZNPFiJFe-8Tc7c026YuIbQ-HyhNOy6YnsmoOz3xUQrroPy6hJHarcIW_mPkPkHTPigVZhRAunV2x2pviwz_0pcpo4xjZhYAsJcbXUMlb_q2usw4p0lsxadu7JdmYwo874pSrEDJLOZru3wcJ6Gs-0pRq8HzzsfOeurddgPuJhXuvJJsBBF_syq1KO7ALPbI8CeICzKIhRB7COYaqUAFTY2fUC5zMs9nUvxCVSQd7ltcB1wqozXprFSaR6bTw50Dl1ByjKMsBz617HM7Q2KGtC7LO6U52fjV7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
‌دومین‌قهرمانی پیاپی یاران انریکه در سوپرکاپ اروپا و برد رئال با پاس‌گل لونین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/27616" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27615">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3lerKx6lfXkYca-GssgRixuHY0r2aShdpdYjbrUwPwAXE4Xbp49jh8UdT28j3Fm_WS8HL_R7XjzaCL1vwxuTMaJFRN3r1McdZk4ATOeiW-WOg7m8o79FQ3k0pgXoXEbRO-P7Pa4UiSz00WHq0fyVNUg7cUYLTNVwgFpuLEZZUgWEitOPxxa8V6nergjTOaeB0rSVBV2ClAnJJr0-4EGJ1aQQBe4zQV0hrKXPOiF6dswCBzjjLUYBkwZxmvHJCWhvJqN9mGyiVUSFRdJbwBvYmV1wX4U4c3mKYv54t4nI18IsVhemoNdeX0CFlt5SDmtEokvkd3jmlrLfcGlQeGjzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
2.5 میلیون شارژ کن 10 میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینروشارژشو
🎁
به ازای 3  واریز اول در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
درگاه اختصاصی برای کاربران
💰
✅
پخش زنده ی تمام مسابقات
🔊
اپلیکیشن وینرو
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sa21
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/27615" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27614">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFsf-hT0zTz1BKKst0jYIUZ5nTOW-ZOrTrzSeQJmTt2coVuJg7NlvQVF3WaPykqdcXL9B64l23FJh8zymmHW1-gLGg6U_1lJnefnSJg1k9grW2bgdUhDwAz_1FusyQGcJnipKExY4Px6p38OEP_2fSB0joQ2oWY7zA0zeoyQjyJBwKpx2gyBwMoLNvoWh8upZeV79KtpfKqVxWHvSl4Kos72pXj-0qoXEX6sKQh-DmZUCWo3rfdJFmXvhgLowXvsea09zs6oNIgZePEOTJlSsTjPaUO2pV7ZoPBnsPyWT_nC65GVXER3cJudpQDiQCNTbO1wZVB8kDyN9h1kxQ8hLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماًآغازمیشود؛ طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87,200 تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/27614" target="_blank">📅 00:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27613">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc0eflkawxTxqaJgd8fdxgmxIfxtXuJP8Ss-aZVGUqtQHUKRB3TBASzE8OaGVBBzGh-y3sSY3V4q81vWKI1ybslobooi0SSxpvR9pWy0THrKCA_4pkVC2HfQMDRp1MjogjMf8C8KOF_fg39em6okmKE18irCfx3cPpwHjJLxQFYxVSAuKqYOF9Bh_8pSVap1m_YESIjnn7HyuSxlZUfh8Yzv5qMeHPkFPGQY1DZQsxkh9yQPiq6n2KCnXeLVq3zBemKKR8qsFBdRPdog8tAoyqwqA0r-d14RSti8XmIeOWHRw5vPlae8X5NtpIoTZ1aPzRCVNcmaDe9ABv1HRvraBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شاگردان لوئیز انریکه امشب با برتری دو بر یک مقابل آستون ویلا قهرمان سوپرکاپ اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/27613" target="_blank">📅 00:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27612">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaOk1Q-pq3B2KW5jTFMJu2pth7OhiV06xW3AkaZanIYFs60uE4e1I6hJuIZYSCZI8ZFa_GeC2_Qv2mHlpz3FVwEV930fNBPus39oR9JmGepkCMv9YWNHnwOuftuRkO8qhUb7LbHqpdnu6OAqnzl-HJ2F6Mv950Jjlu9UQ40XoTdPbUVqbqfkAZD-4gt344jLAibbQmByFEGfbmQSR9FEQd9A1p0OOQ_iU9E8UemUvMoLvNCmz7NmKPlnWH1VW2wqf8WjYvu8bNcs1QaCoTIFvd1esxfmJ5MlBLjFr9uQ5KrS-z0qNShfYYUTyySCbDfsV4Z7jFoFLGDbzubaE43ONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌سوپرکاپ اروپا؛ شماتیک ترکیب پاری سن ژرمن برای دیدار مقابل آستون ویلا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/27612" target="_blank">📅 00:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27611">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml28weRl7_ERhwxhDj6mBW6-Co-wQf28q6nenOiumQ6E3htMvlzRZ0vVMlxEj67Q6MtNEfrpaT2QbP8ngAZYDDo6m4SsD78b6-L4fSYq8l-Ok32lJpPR9_Me2n0gEUqHdGLZU9auEFewYcf9nGTklfHGGTSfOQXrn9B7Ygenylw75rUQ_NMfa1rSEd4w1qfFt8m8OEU-U1_I8fhfoPA2VjsMT7v6FV4qtja4cAa_-n7BIk7kBpsajpFLcCgwHdSC0Auz2QKA6PZVgfQsU0bhJ3-ni1Z8vt4ZN-YGrHnksb83253bdFMzKhpVq3-78T2GRfxPAj9ihN-Pn3bImyMosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/27611" target="_blank">📅 00:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27610">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbGlvt7895fE74nVLsM9XOufEVQYOZK8lu0r8sPQ0oiErQsZSzQQF1wUcFyMSTC5NkttVJwsqsbEBSInUnOM9kCMyRb45B2HVMEAquFlxciYOvBGGSkNEeZIc3EO3z2ahzMxNN43ipTDQgQ5DA-dz6S0mgvXTJT9apPfS3b7qDbBpvGmxL4HqzHMqGEZIK-9GLc6tHLH--IacTIC1FWRm4wJvYTbULEMmBqpV4NzO5I63awLuNJwiL6Gdf2PvsBC60xwDGENvbipQOV5qCTCz_gegn4aXBcEUX5avPRPTIM24yN337j67hyYwvPrgQ3uTu00-j6oT_BCk2GCFLUmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با اعلام باشگاه پرسپولیس؛ کارت بازی تموم بازیکنان این تیم از سوی سازمان لیگ صادر شدند و سرخ‌ها با تموم نفرات به مصاف شمس آذر میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/27610" target="_blank">📅 00:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27609">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEnYb2L0QF8Y8fJ3sk0ZRVi8VW6Za73HksDb-JLFAXc1ShEQtFJn5EAxWED6zbqgk0nz58kTv7rnz4wTelEOR-xsmE5JfXYcWtKHEgeFXYzeSH8lJF7_ty2_bKIWulkhG6M8oRcsadBD_tXtHd9GG9AX7p0S73YQZkBh-suYgkbO5CuBWYGMH6SKdNJcqhAqAXalx9g4--L8yYPyOkA8b_sTUPcaDexVTa2n7dYwwQcVEqXoEak2ZUlivSO8Oc1tc2gZyK9PTCFC5eP2iawQzOsKJFT_J60S57O47wjIf331Sr64V7Tn73BmaDvK4MI30_xAHYmyV39dTh7RZkcKpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو اسطوره پرتغالی تاریخ:
🔴
اگه من جای امباپه بودم، می‌ رفتم و ویدئو های کریستیانو رونالدویِ مهاجم رو نگاه میکردم، میدیدم چیکارمیکنه و همون‌کارهارو انجام میدادم، کریس رو الگو قرارمیدادم و سعی میکردم چیزی مشابه به اون در پست مهاجم نوک ارائه بدم تا بی نقص باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/27609" target="_blank">📅 23:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27608">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcE0VuB1aLHufP7DLq393l7n4-PuPCjUiw_jglVnLOH2Pby1RSe15kmliQlrQD0hf5X38BYr8BrIWUmSiSj4X2Pccl_q-ys5vyWomU2NJZbtHyE-3uFwcRX2-UHYsHeLeIkqdeECF4olHTu9xGnOiKtApbUerM2YenFpNHYK2XNnmrys9Ka1RLtSOgRRjCeAO6e5MRxF4nEyq6Wx1lMYy_fq4dZ-4GD36r62JdSmTrrjTyDRIZPy5U1EuwNjXY3uzL6LjdzA1ETeHYva3wRQSjc_pgj-9stdt952YnAoWVaFgScwgtBXYcot99Qj5LOOEY0LRSHOjwfmQ50XizateA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه شروع فصل جدید؛ نگاهی بندازیم به باسابقه‌ترین‌مربیان‌تاریخ سرخابی‌های تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/27608" target="_blank">📅 23:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27606">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jEI1eXeFSgDiNmGg5M-sJwOniUunbfn2LPjC4HO6Dcy2vbTS0SLmFa02ELSQFRjhb9vLqNTJd-J1I5GX8DgS7LXRpmffMR1ExJD2srWOBIaSHBU-F-IUJ-ytEsxL2fXpitGV63SWkWZKe8ur-dEybuHiH4YQII9A74LtGIF7rOKjd96FcsPJl_C-Cfc1dRaLndf0nZENel6aDE17LGWSQ-uTrXaG53bATSGAvlKzrM6hvZwGKgznjW81yiQuU5HPUONEa06SbI8Pyro_TrhF8iAGd0VbCdU0wUMp8kvvmNwEu-ow5HPKKh9QTJOAOT0caOY8YmMdNcODqfZr50nV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyXQ9mC89b3ItdDa_f0mXNfXGN7xQpLPS20qYHxVuHEls42tXgPBruVvKS_x77bRXNG82oSYxkhYmB24WHz9mVuljOOLAzX438oq9uArA9BjwvlVzVpZ8suA4hsYstl-fQcdz3m8OWRU4tb0vUz-UdwPijDNi44xHsNTsSohWebyoUCkLGmB5QzZDx-ERlEMnJuCpyFIRuFgr6QnhItrXGgRIYrCKBHl3m7Yz8V7TyDRNvAT109G0JG-vTGAEe5-e77rvAqpr6he06vgoHYtjRrlqBxcY7lrbPojRA1E6dFwXXAriO_WOl9jKdUnm_MUUkiIjQj5ayvzDYFsq7M3XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به بهانه شروع فصل جدید
؛ نگاهی بندازیم به باسابقه‌ترین‌مربیان‌تاریخ سرخابی‌های تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/27606" target="_blank">📅 23:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27605">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQVtCRKi2YJlglJknbvvlqehkiDamp6wXx-5K3LrFOcgAfhTwMWfCQdyF2Mwj9u6gLTGSO3ZK-B0MMuoCheWpqc8OAbJuZB8VXu_ESNBJ_suUzGP_E_0OSTkxXUhLY3RzXF1cuzPmX8Zh7_7HoEVJLyR7rh18ZjG5xkD4eoMhSvsjcOM21608kfc2UIqRGC85yDaNe-GvZZrSelBEVr25s4dvJx1p_0uJITl7vD15twVZ-CSc9AqeVIVuu3JuoBlUHZCSlJCN1G9OWC4ztQyw4_JTte3P_c4rHOXHVw63QkLku_Wk6oshSDZlAsH5tTH6YCiqcBY5-pfTbjH5OKq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تنها دو روز تاشروع‌فصل‌جدید شکایت نویسی؛ برنامه هفته اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/27605" target="_blank">📅 23:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27604">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5714c0bd.mp4?token=pnEfC7tz-WwB6GPwLURPnjuKn8C5qdIpznsha_IpTqxgYvXbivUVUMVKIouBbPiBBjwj2QXOhe6Q-h4y7YtetPpXzXqCnD9u9tmQQCTyIWJAl36u5bspURZaUaxlpgtMyHEUzsOl8MCgrofq4lW8-llnDU3bRtEDFERWFMSOQpPlltCVlCEKhC_NHDdBV0WhmjUb-X2OEQSGP1W5kkWl3frvrO5l2rBTl1r5fFdgPa2eyB5XU_QgxdMrqp3wztYFFVeJhGg0uhrouOd6na42cWXusLDoW2FdNc9VgZeE6DEwPrF367JKaOSoA_PiDpMCPf_JPQT3HiS-PzN8Vo02Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5714c0bd.mp4?token=pnEfC7tz-WwB6GPwLURPnjuKn8C5qdIpznsha_IpTqxgYvXbivUVUMVKIouBbPiBBjwj2QXOhe6Q-h4y7YtetPpXzXqCnD9u9tmQQCTyIWJAl36u5bspURZaUaxlpgtMyHEUzsOl8MCgrofq4lW8-llnDU3bRtEDFERWFMSOQpPlltCVlCEKhC_NHDdBV0WhmjUb-X2OEQSGP1W5kkWl3frvrO5l2rBTl1r5fFdgPa2eyB5XU_QgxdMrqp3wztYFFVeJhGg0uhrouOd6na42cWXusLDoW2FdNc9VgZeE6DEwPrF367JKaOSoA_PiDpMCPf_JPQT3HiS-PzN8Vo02Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/27604" target="_blank">📅 23:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27603">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmVTAr4YH0Ba0h8JUq6AUleT9CbPu9mTO5Gl34mr_TavncVGPdn32s1ty3fs2OefehFvO21qyTDJur-TeIZbqPPEiBlklIymv27i_Znj08rUNedihjqUtknm4lKcL7D1Ql0729iYkppmuKjDcQi-f7vCZsFvtk7BKBCAJuYUYdIGJH9fyiixxJ4kGmBszw-ya9SvE8NDa6vpd24N3eWLgdAwyCbKWXlac6tHT2vWmAAA8KAMAQ-EAVR7lQTtZl5DvNGbPQlTESrA850QRWN8OGzPxcIdLulZfXO-yLSLKDWr4H_jg3q8WrPKapaJM1vAhz52IBfbW0oA6LevUb2Ibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/27603" target="_blank">📅 22:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27602">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb932d906.mp4?token=dtnVMlZTaJwgpehK1BGJIFKM7xHtnwHWpM37gSKtqInQu76zk7Nik0x29mfARGfKpSZQm81RIMhFcF7qzfFC-wGvjXZGqTWzgL-ipEhQF2-7FeyMRiDorG75c639Js298czMr6jtg1LsTKwCOAuqTAOXMi3ZaIZvKL2gTYCHpbbrCVHSuSPHzbirc90HXL4jvdhjSKCzNQez1s-vZ6Ijocc_qe2KfHJYMjezfHTYN2MctW3q6yMcaM1h8wnCSdN2CIkqrH5sp1b80rNZRDidAZvDUv5KMzSsxsBwqvskFjAn32hhyTiN9ncVN1M3BeruqQuNmHcgEaXLvtJLXiIUfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb932d906.mp4?token=dtnVMlZTaJwgpehK1BGJIFKM7xHtnwHWpM37gSKtqInQu76zk7Nik0x29mfARGfKpSZQm81RIMhFcF7qzfFC-wGvjXZGqTWzgL-ipEhQF2-7FeyMRiDorG75c639Js298czMr6jtg1LsTKwCOAuqTAOXMi3ZaIZvKL2gTYCHpbbrCVHSuSPHzbirc90HXL4jvdhjSKCzNQez1s-vZ6Ijocc_qe2KfHJYMjezfHTYN2MctW3q6yMcaM1h8wnCSdN2CIkqrH5sp1b80rNZRDidAZvDUv5KMzSsxsBwqvskFjAn32hhyTiN9ncVN1M3BeruqQuNmHcgEaXLvtJLXiIUfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماًآغازمیشود؛ طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87,200 تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/27602" target="_blank">📅 22:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27601">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvJNVmLU1mdD_N1-twwjblZIRzFrYf9aRmYdVMx6pOfNwHzM7389pgDQ1snPMYn3XgGQWbNa1BFnj5CxjpI9XyA8tWSqrkaB0MYKDy5INVejOSNkQcK_exWO8BAFXKeDeph_7wEB2xCC7URU3mVeIKz6DxqEEbQ8Uh8yHRTMYVDMzYo0n1E-JAAJbewvtpWrAeDLxFZm8yfPjnN2nqJHb562XjkHs_9YnM51YQa20UAMBF0zpuOEGfbdORuwAozzUBPRCc8XcX6HpRJ1vQzGdx5q_H-liAPCrILujCifZ5B-E49fnVD0AyASUJGyvLNkX46gcVGvBySH4y8wvxQ0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
باشگاه‌الوحده‌امارات: دوباشگاه ایرانی برای جذب محمد قربانی مکاتباتی با ما داشته‌اند و بزودی تکلیف نهایی این بازیکن نیز مشخص خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/27601" target="_blank">📅 21:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27600">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip1hYLJCDnRvoIjTkQz54OfW1St9N8U_JCraFyJc9jgZP9L7WETjscmqKyrOspVV606IywM7zzmifxWjg26Xhr79dsavOmmXnL5mQObqlproZu6Z4QRb5XYwUuPxDafn5HxqI-xRpVXuShWj2tH9dPEsYrlc2FpG3_t2ucFmDKVKTplssDdX6iBZlSIJVRj5gYYeXojroQMvqLrOgpcKizrWpd7mgxok5J3TS1r2HmnXqA6uFF1S7QXooH7Y_qUlJaQn1EDQAvu1taGSN_vu8yR9V2kMCTNHEp-V6P4SGMlEudPvojGiTyJBKAFg9xBvCPAmjrVUbAHSYHiN5n5Cag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌سوپرکاپ اروپا
؛ شماتیک ترکیب پاری سن ژرمن برای دیدار مقابل آستون ویلا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/27600" target="_blank">📅 21:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27599">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzUGofjCFMbmvcPIWTPfAMdFbntX6XXYpAEKgLxBdefQkE8q_bXPjbWhu-h70qbZIwgr_Rk6I_-v17PxIxqBfpyw6sdEz7pF5y1Jc0NbntYPQFplEo2sFfS2xVXVeHaWp9Qr5_4eUhfwgJJTZCjpbvqvwRCX2fl3-2QCHnV2Wkxp3gUDbnG9mUB5iO9FoVeHbMN8BaxH8eiCgkm6IlTvWmFgiapuD1NwccVYLGLVowEwPbbmC0KikcaVfIbEgE-BZnLlhi4ut2vetDOc1RVdfJGxUdMKyFYtuX0rfy77Ow4CUl573MFAOi2HR3cJ6mZ45r9DNMIgc6riUUMhPw5new.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
حمایت‌قاطعانه‌عادل‌فردوسی‌پور از سعید کریمی کاپیتان ملوان درباره‌اتفاقات اخیر مراسم ازدواجش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/27599" target="_blank">📅 21:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27598">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeX19VRkLMbCNv1jBG6cMMss54wzfyYwDXJR0s0IUSsw0QF4XkRCf3FX0dFxTeGLhZdXjb6_HkpK31p9yoK8bIDd3Afn_rj91fpq20rcLYVJQbwyxpZv1vKFLUuOWVx7Q8eL9-nlJV_aiSi-SdNkI561U6jTJYhSvFN87nCOXbZ0mgclHr4gYAZD9Eba7KCZgMA6H3Fb0ZkhdmdtpNv2--Q8l0m8TSvfkoEjdDRt-faB83mbVoFWByXgtkSa4arg6sqMDqPK2S9K52Qdxh82Brey-bjg5RzzVPEs3FFuk1ARKO3aPoX8SC0_R82ZKt8KtpgrOeBximypbLNXWhZb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
#تکمیلی؛ طبق‌پیگیری‌ها؛ تا روز یکشنبه هفته آینده تکلیف‌نهایی‌باشگاه‌ جدید محمد قربانی مشخص میشود. قربانی بار ها اعلام کرده میخواد جایی باشه که‌فیکس بازی کنه. هرکدوم‌از دوتیم رضایت نامه‌اش رو پرداخت کنند میتونند با قربانی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/27598" target="_blank">📅 20:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27597">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaZ_ly8MBRZMChzK72ILR1C7uRRiPcVxmP0geav6D-CiJMeVnK-d1BLH61TQI2kRnfWFQPF-Yh010PAZtlA5Hslf5LvQyuXdETSACUyLd9_tsiDYuvfUl2ujZmdrMJLMISHySmWrjJOHA9APsm-MHMpS6f3A2ItNG6ClLERJSWpV5K1BpiqYMRXEGoY7LV5xUodh2klQdwzGtJVo_Oo0iwCsFVaCgaOgl6-R-RMnlfpO0BBRtrW0uYyIHmiK378V4c69rCa7KJkCh92ol30-fTo-ENkqbYMxIkdP0_wq0cMGyf3GJZrL4UPTXRqu81e5ClMip_d4RM4deWqYxT352Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ تکلیف محمد جواد حسین نژاد و باشگاه‌جدیدش تا پایان این هفته مشخص میشود. طبق‌گفته ایجنت این بازیکن حسین نژاد حداقل تا پایان نیم فصل به ایران نخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27597" target="_blank">📅 20:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27596">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDdce4CiOKGY6GayEiVSduhiPYlDW7Xdk20GYHjQkNKf3iUxuN64CVz2RxJJo0Zrgt8dc5zlsjnBYqzoQfN8Oli7Jzp7S4WuhsJnWThoQeneNi5XbKGJS9c6EZsuKt4smUPQBBxTYPxk1sET310cK8Y78CGt-5oE6FcradTogtKkUy10HITwE6XFvoZVmkcbsb_QEU4EfqSDdsyDAB8n4l4kU89ssLFazPcIQLuoBOYEKuNPMiBvrFxXzKfNbHaZJFus66NhWxf8AjV4BMFD59DrjzaIz0wmX82pZM04NZS9mGKsPg7zP1jRA5eADkk-_nkSuSj5DueQdGhTnsaa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27596" target="_blank">📅 20:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27595">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a80c00be8.mp4?token=ISwt3UI3nCygYwJmEVq0PsLKlNOZXPfnaEA6aJUa498x7_mrz3gWdQb-_Q8rxmAhDZPLDEEXexmNGDdFl7J4fVBsv6NvVOnx8hSS5Cq3ZfMhYBnLrzpb7xr1hFTwDBvo9b_Htm8KuvPPohDFn66AAEa-H9QKBb8IEqdDdhh8JrlTUFRVZc0URNQ3_kQ6RKT549LmBoTPPquRrfVuYYtu2fKIvT9pmbZ9cU8EJgs3wen08Wmk737tdi9R8pQeRJIPtcIZp9xGjYWfgIv2zCtIddXxnKTbvqgh3jnVqcUttdly5RLi2dNzB8opaLlJkbiduySNLLbuwrn2xiIlknG-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a80c00be8.mp4?token=ISwt3UI3nCygYwJmEVq0PsLKlNOZXPfnaEA6aJUa498x7_mrz3gWdQb-_Q8rxmAhDZPLDEEXexmNGDdFl7J4fVBsv6NvVOnx8hSS5Cq3ZfMhYBnLrzpb7xr1hFTwDBvo9b_Htm8KuvPPohDFn66AAEa-H9QKBb8IEqdDdhh8JrlTUFRVZc0URNQ3_kQ6RKT549LmBoTPPquRrfVuYYtu2fKIvT9pmbZ9cU8EJgs3wen08Wmk737tdi9R8pQeRJIPtcIZp9xGjYWfgIv2zCtIddXxnKTbvqgh3jnVqcUttdly5RLi2dNzB8opaLlJkbiduySNLLbuwrn2xiIlknG-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27595" target="_blank">📅 19:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27594">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9yYhomOai1RFJ1EuxTonIuGCIvAKO0EW1h7Jia43r1-cJ7RP4yjpqpX7SDGHdfon7EQQsKyrxpnJiaxCsnkLAhZOWrpKIQ3zTH6tf7jZOg51XCjZvEXRb_1IveE24oRQVX-z_-htiE58x7N1ARK0IBTV_TO-HRF8lsJ9xy85x_p4k2BSzIlwZarpC3WX9ACatu_eR3xrpcH0M4M9i6pwB87NFg0XQd81NV5htVmftOppZTkVQiwLUVWX_5nr2Lvn2GmMdMQNdSTEnOZO03B5gOfbP_p-12WsDWIk8iPmv39T78taZh3mlATUMiqWis31msIUuMqfnNe0QlhLLWgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/27594" target="_blank">📅 19:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27593">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLnpFEACdUgeMW6kg42Qu-ZvKsW0n924QewKtQxu7-XwFrlE9FxwyxqWC9o8fK75hEaM0BS2aRErvyEXfvcePKOX1jgkjlClw6l0G6FnZHLsdTt_HXMluhFNnRidp2dMOXJMkx3krAsAxb5f7rDakdvlHd5nsG9y8zal1ZBfDPpkwLpybt8OMKZvz5euwB_9RMoX0NTPQeO0o5iEiOuLBa1f5HILGaiK8_IoY8i6nhCC4HQHYX41ZZg-_mpw__sSmXmA2OvrtLUaXufdsB5BMb8xwROMJL_AueglsFGZBzeZYVxURqWPMxzuJfrkFP2L3z0FbCVwg4SJUjUwXusGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تنها دو روز تاشروع‌فصل‌جدید شکایت نویسی؛
برنامه هفته اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27593" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27592">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZMuYq8OiobfzVRr7VOPVZtvjghh43af3TC-SU5HdWG5tDgD6oDV9PgcWUaQOgCm2W_WlPud6pkAw2w9plzb2GMe8tO4HW7QOVOohtkvw3XAH6mIfF3ly14KPwVwYz6oppCvywjMW3UgXsBtyXLF_3FCBajoG6rm6TMNIUteQCkjfgEfAMlazmqURHrg9escxuuaLgI6JsjPNgMWjGCCRidnz43r-uIfQzW89MwM_40X8LFKEOELC34_VQT9iOtaVbnllFfltdic7hsFR6VnQsBD_kRaKSHHvX459oMsp2Ke3nL6dCFQNbgRtiXuFvHBovK3wigcESIPh6cDzS8CJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
شانس‌باشگاه‌‌های‌بزرگ اروپایی برای قهرمانی در فصل جدید رقابت‌های لیگ قهرمانان اروپا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/27592" target="_blank">📅 19:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27591">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a96IasAu94ix93hcHrEMwXwIwtqIc7stk5KneI9v8roZQ1UpGYGaZRG_sZzvETzcT7YhqySbaS1kriBxchw6Ktomv1nVuYBNbHFnyQEHgeENjUITinp0ntUAPRfqMb7fJLFhistq4-5izdQKR2BtNBPXZZOYTqLmt_EQuy6RTbRF4bV8boPjaXoNk0pIRHii1Dw7LjL5TGLn_Yh70uOvnLeAeTUQUi03ow9KlPme--cLFgoTfW6fyHH0WrOrUgvR77waAgtYvJkq2f6YOGupbV_t5omfZ0yjLFNQh5trzxb6hbgDAdacdZzfTRtu3BLgRBJsGfLGFdHympRAGBfoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 ابزار خفن‌وجدید هوش مصنوعی که سرعت تولید محتوا برای اینستاگرام رو بسیار بیشتر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/27591" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27590">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzJhGTzOHzGJaXszvLeqm3PbA44P-JUjV38oyIDYc3onydilrSELC6RIUjX67AK0IsoizynSlVon9gWQVNi7ygZCQoDS6K4NWkxjtXPD7UZQRgLjc4qKy6lZmx_bihj1boRkEAkgfB5YLvTQICM-Jf1hIg42vjN8Q0mRdnRi_MhTYiX1UKWbq1nMivkvgdWtdgxxwEdN48-niQLiVkA3NpLPUIMUj6fvsO5WKZG9hX09rMbSU9unOVRScrESVGcdTcYXRzRhMbGNXTOeB4f8wmxdxSyAZIua9gMhCLF1Xox9XP-P-o-MaqqELFitZySooIvdt3b9hy_8YpPuGWVSuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت: «در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/27590" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27589">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUzfmblB66Q88FUL7GkevfLzrXyuaRxt74e2x79VX8-UTULYTAmO3i2ceUFLviSBBRbOFMeZT6YhKl_pqndoODSd2-0j5VliELqDSTXGM8DT6q92EKPC-g0PoEz-NDXYAKDOTtzqvhFjLGMDDpRGcHH0HvC_UN_wbN1vIrE3HMCTMFCrsATC_xTJMvJNpz8jfql0WfP8CwrO6Oba6CqkkoVHMeLijwC_VhXTxJ_byIW07HbneUW4tvVR5KJAcf73IQGWgLFk5Au6B02HeifENMZDDt1jzTEf_BEYbhTha7nHkFUyAIxCjElmFNWQzDv566ahFw59X-kramz7WOOlfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سوپر کاپ اروپا
🔵
پاری سن ژرمن
🆚
استون ویلا
🔴
بیش از ۴۰۰ آپشن متنوع برای این بازی در بتگرام
⏰
چهارشنبه ۲۱ مرداد - ساعت ۲۲:۳۰
🎁
هدیه اولین واریز، ۱۰۰٪ بونوس رایگان
همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram
بهره‌مند شوید.
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/27589" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27588">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWM5B4WqQlAlNDMcYd5Bn2qmoo0JZWaO5JGkFu2g0jVl1E3JaXR4iEfYgzGpxLK4OfMqIZWMaAq3LhXSSq4ZlH7EtVEmtVs0EfdvDc_ghBka3yT0ioYSM1503G6w8udX1m_2edJCur4d3bx-h5gty2rWxtzeBlRb44THy-uiIBOYFVqKNyDCNOEdpQjdsyoKmdu9jw73LwyhGWn6D70DmSq6SF2bExWvgxTyyIfrkjlQxAEk1e7c5xeAKB-J6GvlKG31qwHObrrEa4fhw_Mq7UgxTqGosfiRUQAmuPMb7GsKx2wnrqCKlAmkPN710id2B_WplpDPxWkqdE0PNKXpbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغام سعداوی برای‌خدمت‌سربازی راهی ملوان شد‌.</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/27588" target="_blank">📅 18:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27587">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpXzPA1K7kxaeRsrW66viw6ztHq0rqFo5cTAq61fV5vxx-SYtd6GxNw9xah_plgGkeR01jKZo-yyqs4S0gr-POFUqreoCcmLO1GbJ-7jpvpQuoteSn8uTjm6Gz-uVwxS3F3FwALSorICoUBHmOqwuL5YuRlz7FBPNxgKrg1aMCyz1D30eKF5RTnMCCmrZRwbn0ktAWxDVNqiFXmX1oW23Z1fjluW4KaddJ5mFEaSJCEOGfLp6JS9n9eD2Ltyds73EqpRFIan9Ge28dTYKQoI8GKYnAMwmcrNHLlxsVHfqLTTimpWeNeTNQAhyAL50ow2W0Xy0GBW8M3mClw2bv6t4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/27587" target="_blank">📅 17:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27586">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU7hxA2wnJe4ukOMPvBs_ZOF8ljwbgSK9smn1tP1zMDvHk58IdmCpkQ1hTgjFFtZtc7yTfuk8RuYO36ZcEuQicz28e3Dwb9IyNzA2V2nDAVAyM-ly2TBfwXJDBZF_Am9DMp5hCY6Tf1JBsNEHrdi_EP0dDDUBUZfVf9BHOd1q5wL5fieIgA48liwo0hP2Wa6kKou_3_1FsUxKqK3yEdzTUwDW6qw_mv56ZF7-lbW1c6bM-F9XfyU7Fz5LuE0amKDnUt5gJe5DPEcTegTdqkavizKPO3PyWmczYjGQy3KzSvJVHUw6fnKsxFsOBSHgdbFryS-hxGm2jR7lVrIUadPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/27586" target="_blank">📅 17:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27585">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktx5itSYO7ehn_y9-0ePxTb7f_yp8ANEcbwhxaXlQ92wBNO3dkHK66wvuR1ozhc-XtiqeVYM7XRGuIjJ-1BF1HRTwrkYR8_lm552LehyNpvEB2NUe-hVpbU5HQSvaIPqKz3uKTLrbKSQLb4C32YyBcFKgHZU1u5d25eMKTScqN8dBe88Ax9SQvN7DtrNDoRedAICqA-Fjo1lZQb09TrhD0SjjpXS4kaogefyvJDU8APwtlKL-66BiL9wF24NuGPRg_cuDWo0fUZ5FWOJfqm2MhLhwy3j4L5QC_bguCBHgk_JnjVAuX5IoYL5LIlgnrKcl2jpbD3yc1nft6ud2R0CQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه اینترمیلان برای جانشینی دنزل دامفریس هلندی؛ جِد اسپنس مدافع‌راست26 ساله‌تاتنهام رو به خدمت‌گرفت. هزینه‌این انتقال 31 میلیون یورو شد. اسپنس انگلیسی فصل گذشته 44 مسابقه برای تیم تاتنهام به میدان رفت نه گلی زد نه پاس گلی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/27585" target="_blank">📅 17:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27584">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0r34kpljLJIcHiSAgektvh_yfOwpHE-kg9Zhk-oPRTcOHvgg55cN8xRLmy9-_Id7gcj6GKJ0w7zc8j3ZhhGjxUCpIaa2_ashXYIsx9MbGmFVtp01K1oDHAIZlKq0MgKRnJOL8HqQeFrr-4D13Nt2ebTl-yEIG7UJi0oqRUG8rcqbmPS3hbJNz8TDvuaVmrPCeTDKzaa4jnNAfqU_b7q2o9KGPmwMXdgeSaOt2-6o61WjSoMgL9kehb-BjSAp7Gz10SI3YDpVgpYwM4670iAhUlBgpgFVrIovBmx7nH29VkX7S6g-df3vlbJYClAuUGKED12ua7r1UbSOkWf_MQIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت: «در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27584" target="_blank">📅 17:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27583">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odpG9R5mPgXK3TLWy7WsBLn5mbB4khGcHQ1VrHnjL4rvOoKeZvh_ULhhgbAefGrOIn-1buWlz4jM6d6r1RSCLISgjas8O-w3NSbSzHh1UXToiliyxK4_2bgkrKAJXs8JOTYhkDDEoGk81335DVMe_LZVGiPBPBYa1oQsgAzKQDzJnHFghOLJkyL7X5NcZCoS3spuNyOMkhjuUYeZt2NsSfsgkZCnFnvnIBnVjJDkEmLj-sb5zNrc9NSjG5pS_6Cg0Sy8zAF6lM1ne29E7B25VZrm8sV1EUNTZpNYNdnMRhCgYYLTgT30jdMdW2MRoKUGB39GojCqq3g0ynpkTbNCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت:
«در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27583" target="_blank">📅 17:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAdSVqpV8my8c8x-Q1LWwP9rMuEcojI_xloW6OirBie9MM2LFhhpYZ6qr3QYvRFFx0S5eH-3pRlKgOuzOcXExILSDjuW_SHV7_LbKH8o7mrmgKdjKIL6BnhaLgNh60a4BvjvZ1RhlqPFJRWKEN1tspFe1aielGGq5U8FM4JT7gHY7pD9hllsaLSEcn8PdlCdsmpWgubMj0cGndk1dlo7zy9mxv0CAiFHP7nIrmeRo4Lmrbts6To7vhxQ9jKGEyASCwOtCP545Szna21rpPrPyOGy7qeD_STnpDdKon3LbAd3IsNqdSjYULUo2fZ3RBhCqIZp4nkfkxAxGt0cKkioYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فیفا کارت‌بازی یاسر آسانی ستاره استقلال رو برای فصل جدید صادرکرد و به مدیریت باشگاه اعلام کرده هیچ مشکلی برای همراهی آسانی وجود ندارد؛ باشگاه بزودی نامه فیفا رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27582" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amjA-2c6TFENukYxriTNf5NL4dx2VJDkxqw2Pn_nnrX5ouKFc_jeg1mrz4vba1nACeQ2GV541stjn255kOqwYDRIXH4lfGzsfVbAWeekdYSyWakKk8hlKlHLpP_6FzgUiNbGixtXgD-L6pV3eQDvHlJw_2V7uBmVbiYSR3dnPSYATRa2CCzp7DJIcwdJpTr8fUDnvtmW6uvwgjKTK-tvR9T6tCy1mNp5yV2KXHXW74tGTMwDHgxtEwmuqO1NWfVfbz_ARpJX40F4BcEvAIqDt8_g9gGSEAo6KLxVLcPVfbfzQ9-dhdW-dyzX89eQRUMjsfJcON4ZRBWh06dtY94UPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
درآستانه شروع فصل جدید رقابت‌ها؛ از کیت سوم دو باشگاه بارسلونا
🆚
رئال مادرید رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27581" target="_blank">📅 16:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEXCTJpPdlBLgKhY3vZ4OGK7KmrlHU1usLyUpK6jcDl8ZhfK7TKbcroBMCFV9LzM5Rb9prXbriV1EQbnPEEgqiTIPHl8gW8UpQLX9ZVy3SN2GuafEHMSTJAP7vjymLR45MSv4sfJEgqQYIhcN1jc7uQwgxqhtfjZZ-AQAs8m_hzDMEl2_Cim4wNCoNhyw_2pdJmFU7Lz158aLPs-6HTbslCTA_uPx0cAi0FeuQFxqSSsUE0Tl0Nrki3d4xuaVCM40XipweJF39uNHbIy65NWoZG1kuTTKR1ms0HB6VPjxTyz693kM7sVvKpXfMmaePkXiIrIhQU9jL-Q7ydb5-ZZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27580" target="_blank">📅 15:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27579">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFICh4Ktln74Trnr7WFH_oK-mU5qGR2_oIJUEDF72wEHnyoT-BDuafXE41LPqUG1m4ioioDmX5zd9cen54KfTc3nAgN8RsumnykrPeeM3WzP3p4yGU3eVazIxAkRYMYMW43HCaUSJhV-uC7CruJnSO53ruj89J_EThvIsPEDxpQMeWp3RxzXcD283t7nVf004O2MDIpyre1qxlWzW51zoL2FG4poFzWf0pm92iHUr8GW9jENWwZoKYV_Ou6Aa880mS2lMckbDI7Vnw-69G1fYa0zbQwbkndkh_u87moSrPbB9NjPbAVfgF5lkauZT6-lWqN3bXxBUNFQihRDv_iFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
چنین‌روزی درسال2014
؛ تونی کروس اولین بازی رسمی خود را برای رئال مادرید انجام داد. او در این بازی، اولین جام خود را به دست آورد. این جام، سوپر جام اروپا بود که در برابر سویا به دست آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27579" target="_blank">📅 15:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27578">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTLsc2LynphsAU1SDrXzIJvModL6VovRFxP_B8-83E7aP57luyDWQIyQjLVotPzDfFfFPnp7pnJ9eL9IFK1LNxS4Bv8wjnJ9bsu6hlfL5kXUkB7uQR3K5a-7_yxFudWE_uKRj6k0ppiEKhpTFb3W7Y6j9I8Eyk1wiO4LUsc6VWEm6g1TkO2nf9_tfkj70LYr8WDp37E--15K6M7ok3kQow086ks0DfobcGmZjfk1sGxYPL3RSOBC5avguendTFTupyIrxWdy3gHV_4wx3VZza8MXafOwT5JzJ9xoOYqC907qvYc9hUjcWDCpkxZu48CcV2R-Ki4BM6WVw9z97mA9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال طبق قرارداد بسته شده باید 200 هزار دلار برای فصل قبل و 400 هزار دلار برای پیش پرداختی فصل جدید به داکنز نازون پرداخت کنند. بنابر این نازون چه برای تیم استقلال بازی کند چه‌نکند باید این مبلغ به او پرداخت شود. اگر نشود‌ باکوچیک ترین شکایت داکنز…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27578" target="_blank">📅 14:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjAqcDx0ENZ0nsn4JhHJBaDw9d4B8xvKAlEZqrKiW9aXcwMu0EXlQHUU6Fk8yeoqKntpsFSJz3s1NdhT9Zo85oOcbRgeDhGGMMlKCbIA2jN_vkWCN4VFjZFvA1S8ARRj63IdTa5iH2PbvBkGhfIeqq40vPv3U0DWK2M30eWG-ozeyMpkGfj1uP1oWDqc1bG0QXzcjtJmo0m7HTL_Fk0DiQlXaPUOWVHofa7IEf8X0U5hqbH2Yh5kXZIvSKKoBgtFthRUziVQqEozFaPiwunFX3iCutlJiN-8-SusceICBfjKlnHxhFPiudOhu6VbO62Ung7yNWZZlNRMHBih3yau_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27577" target="_blank">📅 14:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27576">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufbtT9Dy6iIpOj_SVq3IwiZOklsYx8ov4A9tcHcJcuulNZPtDssfvJA-hlGZuxFTEMNOsO1FxkxvUlUXMrQiqW8ioNoiblnw_bhlJ8QEyAp9V5fPiwH-gi5IiqHbTHundofAWbYbXbQ-v8S_nmPG4C39QalRvCdfsU8sWAK1J4vhoA1qea_zqutU6R1FuoWTfpRHVoV7P7Y8dsLjgPy5NWo-PLeYevjWJFOTzFsZUaTqLiaVN6brg-_FSgJRTqlbZXJ9A64QGotkjadd56B6tBJzYLSt2b6vzNaRFZvmhIvpscLwW8DYHOT5T4BS-p860dZRriE5jE3NEFquq1HSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش روزبه سینکی به صحبت‌های شب گذشته رامین رضاییان روی آنتن زنده: به تخم مردم نیست‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27576" target="_blank">📅 14:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27575">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3v60Dl6Nh4giyRApDEBBKJqLkkoA50RF8M7Y4CJ8x8A6GodjC251BwaFOKtYfi4nTo8sqHnEhcHVZj65uRUux55J9kRtphQ_VpX5GUSHDfdSqGaLltt6DKG30_cq_GWP6Si2eXqCxnZlbFjzpQwn0uYwpnC70r-08re6E6oBh4DU_uWrOikDpHt9ZlIidI6--HFfbSLu_vBDu__db8NmUPPZV5RN1EzitNyayiCv_x565rW64Du2e7p_26CnAit9I_3BT0YS9jm5NQU2xdu5IQcQoEwhYuKECGeOArpldL-SVYKvHi7-xcdFgdVStXmiu0sX2oAaXQQ-G99OlFEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27575" target="_blank">📅 13:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27574">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLEgu3NbqOP8aonYHyMq1RXuXqkYy-7Scqz2xa0TfJLDC44oYupVUrgX0Wrt4EZmMgMeLF36Eyc5h6A14zB1PECp94XQGszSwQtd7qOtSLBm7QUUL8ooF7hUveeHS5PNHzZndMJ22rOp4UoGKoKQ3X9jBPBB6Uj8CwhO1cq_yzsY-s5fXJ9X_TKT1j7gn1vR8SYMR3zgT5G8fOkAD9OJr8umRcB4peHYd-n6QgGV82fq_4-NKpl3Vk4xjdtupjUkust7XlLwIfxIFdthRAoZBTnI7nbVGy1GnE26BLIFF3XWs38mg-nRTs1cI8-qus7IxalqqmQ_uGMfAR2WP_HIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27574" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27573">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOun21i5izNeYOcsPETbqO_yoR77jpMkj3OaVM40bAGc4qykw7YuLPJX9WbmbqJw-Cj-TRJaxECJafSKfNguit2zzkBVRClfJu1L-uTg33IxR8lbvAxcOe2wEESbguYjrF7zZ8-zfkMraktrqelUL_trm4Z9BCg-HHgayotFt_cpgAwAwy6hUxt7jitw4mg7LjlBNwjNf8K5Kq8jRLYRNYaiwmgFpZwNJ0m4KJkN3g6qZwB5Ck2SAxBAWiPYrjJJP7uq0mMG9f-7r0kh-FRP5Lp91dngd8z5AlR-qzci0L1MmHdoBgSgX6pNgxjzSCHkyUhXaBxApnZREAozJJu5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27573" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27571">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WATPPIXt4HTAJbDAabJOXeGeKfvN0CtiFvKhhOSm11FnSGM97U-e8BOPxRbX-nPtECo8dZ208mb35q6xFaTIzIOpLDSa_C3dgFEytrVvNnJtOPuARhTarNu27kDC8YwHZBAqjPCIyhhl8gK7ThRwllD-hvRTtbMz8lmcVjgvg6J_Dd8JzqeCArv9X46WrfJcaf6XVdxDHuqWwGejUFt_Vt1xBhaswjxZt7rk6Q1xrteAJ_JaiLlPR-EW6E5RvBxqMFy4HAtgoF0VjDWFk2mxBv8EUaYjWW8SnwyXm8ld-Bh94LaPQR7CfEfR26AA8nNuyRA6OMMK-magJUgDoRllGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌سائوپائولو داشته‌ازکشور واسه‌بازی دوستانه خارج میشده که تو اتوبوس تیم 86 کیلو ماری‌جوانا پیدا میکنن؛ حالا سه نفر از اعضای تیم و چندین نفر از کارمندای باشگاه مظنون شدن و در حال بررسین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27571" target="_blank">📅 13:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk8jXEsjLnm2qdFUqoG_j62p5yRzXt95SMIglW3d3YcHNAGtCZsEf27UC92l3otRphIjfxtAnfffmtAsKXobXcuhpzZT_sqZSTFn8J3JH2O6_Q5jZfkIaobStF_5XpMdmrXwIwFD9BJlCT2gRi0IuMH9ihOIjy167YZ4gHxzRoaCorBHtnyEnWNybosgHg4UktBb7xhoe59Hxe4Ya1edqAzXvQG48b4QW-FCTm0VxTN-HsS8bhFcQ5CdBYM4tZSjg6soOOn9v7mF0wG8LBVkdw9KDeI0pNMH09tEZ8XTtL23I9BALML6cb-UWrX9ETHb_XwUU1hPgsAdwMx7OBMqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27569" target="_blank">📅 12:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27568">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27568" target="_blank">📅 12:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27567">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn13Vx2Zbxx8q-6pA4iFgGq40Xywak8wO75r8sjjz4cY-zuEyS0s8xcjVcvkt1dXflFukOkKDhMLDuGAtxem1QWRWzT2rvgAMNcbXHkKOoBQj8-oDc5OZFkqeTTLmhVLMt8zjch2MfKQUMTaFrgCgT6s5ZyBqygrx4ToCjmEiIZZASNIK9q4-CCqvFxja2A1Syk0U-DkTnWC54ryQ98KwxiCQcfpM3phsB_XFyNx0Spj_-7i8QiAoWAztNP7UVA3pJBzrJWkiSomHbW4M4sDUj9k7j5vABTxkYBZYTpGQDgeA1eahhQFPh0p0BpgV46mv3N6JjpE88oGWxkW2WUfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
بااعلام سازمان لیگ؛ دیدار این هفته استقلال مقابل مس شهربابک در ورزشگاه شهر قدس با حضور هواداران تیم استقلال برگزار میشود. بعد از 229 روز بالاخره پای هواداران فوتبال به استادیوم باز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27567" target="_blank">📅 11:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27566">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec3WuAPauD5BSa0TlBXLT_rleq_NQtUXWLozgkdB536Qni9dJ6LMJ2jiJVP2UbHl7BK-x5X-sRKLy64T7fgwzq7EqaOMq0DmtcY07yHaY0eRIIOndqRDIZ7U4W_zQNEY-bM4IscBpvHbKzYt1EhqQjJxcjdWZO5B19DZyHMnM5RJYAJYFqzZ1hw9ZlLubOVRBHZm_1BZAoXo1bk9Whti0WNIjKqrRyFmlP3XMDuj_jasyz4SvT-7NOUzwN8Ri9sU0ivx0xfML2iQFOyzMMxEBHXeM18qNPzPAwBLmkyfSDrlEXz9S1lw0Ko4jtpR3HXvFBYrHEFr-kshOKOg2GqDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27566" target="_blank">📅 10:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27565">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7L5PV6ewBSgNb8JRsiO53Lh8C9QwRi603LriGUJ18R0MXMIJzm73tzhR8t4z1TLm5WLBT0LN-CQzv9YH5Z8eKA4hPEUG3vyLoGLfJYZvLbR4ayyoEeyN7a85-bCLNMykXnSGwurIPFiwZAROTaM5pYkBM5WiD1fn6hQ4_gISbvbrbMWKyHQ1dcvdbH4b3AX0XvwffwwJ6lHG06Cst72PacjHECEhB9E8Tv1KMLeWcX84D9Ebt9y6qdVRi4d9U0AvpylySVYXER90lhnNudg4HcSDrkM0y4Ofi9ZsbnIITUVUQMKtxQiNpQ4FngiRydtUnGUf_XprrsYWbl_UH_XcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27565" target="_blank">📅 10:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27564">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-iWDqOpwO5JzzecZzAUmekvcsfu4pKlLcF41DouobOmiYc_09n22OHRCIgHRr1K8MnLmEsGDuKBrirU6vF_Mg3GjplMyBfT_3iQoafRH1qQCam2l--o73IWftG_D9XFzC-cnZluqGn9pPfrNWZ2HK9fgB--cy5URY09T5GFzKkoOs6NAVVLz7xYo95_FjmJpbt0R4CoJXv2nDuDrglFXt8B_ECy9BFWeSajp_APq9VISNR4v8EC2tmhI4FGwRXSakGlzpnuK8jjsir55vpt5ysZdi9SAmYVbhFkXGvoVkS9GrcPXNw2YMjYIToH9HSqxXGwnmM_4Uy2HQT9ieSJ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27564" target="_blank">📅 10:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27563">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcUuCmYjZJK0WAULpF1hO2tRMTD55lSO0cxOm0B1NtYcDSuaQuU6TLt17hNFIcQ2dz7jMPmEfGDWecfIiHsvh5rFM-klYz0W11ZAOsan4xgScDn__QjmA0EotNiqSSVtE8V_7Wng1JSGUqvqB4k3Yfv-N_yEp_0xygNcKW_2OPShyS7NO8mengdHmLunZDKdQrCPtwlK5FC7uHIEOoX6TTKOpX7XHEzSLxP1q2y4usAAFJGNq-ynsl-x5twFj1owcXsKkqSGg7IVoDowcEGu1qeCCRqTxJv7iT2oBqcktCHYpojUxvqOI1iZwI0uQ3vgzem9OIYoINgEGQ65Ms8WoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
خبراومده‌که‌باشگاه پرسپولیس عملا قید جذب محمد قربانی رو به‌دلیل بالا بودن رقم رضایت نامه زده. در واقع باشگاه پرسپولیس با جذب لطیفی‌ فر و پورعلی عملا برنامه‌ای‌برای‌جذب قربانی نداشت و با تراکتوری‌ها نیز به‌توافق رسیده بود که ما محبی رو میگیریم قربانی هم…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27563" target="_blank">📅 09:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27562">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhsotT8fIDbKVTQerQU24ttOBQ33TYeWiQ2DAP0ZXoMoFR7AX4mUczNv0Iv_i1F4T0uqEJQQGR1jcnogWoMApQBhWH_43O66AGTfVfTh4cxuehJQXPrtzTJjOKVCSTKaepNTXemKWEqCdWMSO4U98J6B8HZzt908xjPeftFvPENVjpW8XB97t1QaBpoLerFFmFBQdiw88om_fLsHnDdf_MWGiFup-GS4hwy2_HLNfT6rq2lpiZ8eb7Qw-O77GJde1zkO1v__mpVpGfbCL2S-tp38aQWyzoY3SBingUjFxF94oeXn8mcsmLOdPpxthe_-1sGb8xW99-2hAWpEhHDMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27562" target="_blank">📅 01:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27561">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxjjWjn8QMonliIzbbij2A9Dfl0luTlXIO-Su3cynG8DCUFeDbYGIYq3LWQ7AEsfEoNol1mgaHncq7-Ta8OyZOUBfYiepQWniRad5SesCBBC-Ye7QAhD3Gt6b6-YEocMOwK75w4Z-MKfHH6OQJTSZSGzOnonZBXouY00DMTfpvobTb49Q0d-aP70tbuPdqYH-oWrW0jXE0NjCkcOqquMfJeyYy2zwItGYq0vedCfTPLPXD4jiD4TErLOq2caMISCbuKopzayitp-7bG9vNiP5ulXOKKpyWXpxPnw9UlajLC-tHR7V1-lLAdCsBEUV6OzIiBgm1Fs_9lZEftQp1n8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛
تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27561" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27560">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSiLYRwcURXI7MZUE2FfyppKN28unbAE1QFQXEhJoZjFVpkAqyEU7Ci_5KzxYaE5-x7VH8V2QI-BUu736qyUTHwXgcGeiI9h_qBJUUs6xukT4iD0PeiJ1emXndRN4wwxwHiCejDONpz2hqVVZLqhw8GvKqvxSwMEHJ0SWNzb3yH4qpkhUyey0SWlk2lN3UP_R4FSBxSQOus-NFShpNNv2tfsYrDFD4IP0lz73HGMJ49rZQV8KmJ1nEDOnTKSu3VqjMFthHmGFPbiHFQZmjqk3BFOiQTFRUDtB0vVXxb4pKKTv-JGFbbnVDeCYuJIbXYGREoaHndQe4tJ4TUe9QzBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
کامبک‌المپیک لیون در بازی برگشت و برتری فنرباغچه با ‌گل تالیسکا در دور سوم پلی‌ اف UCL؛ کارتال و فنرباغچه عالی مینوازند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27560" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27559">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=f3Tu_kL-wmT-9Ncx5KkX-fbKn6-r89kYUUm5us8vbAiSO1voJcHcjp1fSSyYoO7veiUjVqEWafP_V0ktJ6QzP6FDbpodSaEedTABBM1TJ8u5dtYbLBRqLJu274S6aSTKaTvwdSDKS2f3qmHrLDAgV86QyoCDl-VAT-LW4CmPJRocfQeXSSKIEHTpWtb3LuUSGrY8ynEKPSgqeqWTMFmyf8f2o8uiksIHWf_cfMCfqA-o_HKW09ScmGq-9Vbn9vPzPRuJsoNleTHB-nsAXrI99tfuiimHPhO9PGFXC6zxWQTCRUU3PWsmjICb8vY7MhAU-B8SsmL0l1r1t8YiPak6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=f3Tu_kL-wmT-9Ncx5KkX-fbKn6-r89kYUUm5us8vbAiSO1voJcHcjp1fSSyYoO7veiUjVqEWafP_V0ktJ6QzP6FDbpodSaEedTABBM1TJ8u5dtYbLBRqLJu274S6aSTKaTvwdSDKS2f3qmHrLDAgV86QyoCDl-VAT-LW4CmPJRocfQeXSSKIEHTpWtb3LuUSGrY8ynEKPSgqeqWTMFmyf8f2o8uiksIHWf_cfMCfqA-o_HKW09ScmGq-9Vbn9vPzPRuJsoNleTHB-nsAXrI99tfuiimHPhO9PGFXC6zxWQTCRUU3PWsmjICb8vY7MhAU-B8SsmL0l1r1t8YiPak6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارما به‌روایت‌تصویر
؛ روایت تلخی مردی که به خاطر مسخره کردن پدرش نابینا شد. حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27559" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27558">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=tDh2ZglICBv08yIYRvCAmwoVX4J1eOGkeNKHA_70JExQOUd02mHdAy9Je-CRKFh9aby1WZUzjyF3-TlXxdDFF_a5bdFUlJfkWlgAM56hbDPQthOxssqrKXeOUn1aOlhk9OfoXkH8wq40XZaxEG0GU76ElEW5V_BdVcL3VT-5pbzA5Vn0VwUovfRtNMEMm9SHBJ82-EA9WeVjZcLAm65TlMOwDmZgJHwl1rur3rUwOYaix529utxJQHADdFKeACtzjcV8mQJzl9LqDvAHb8xn-lDFU-XjRCIsKtDPRIFnowo9XCsT21zQlZh1AA_3rDecw5v1qyVrG2g0KifqH9bANg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=tDh2ZglICBv08yIYRvCAmwoVX4J1eOGkeNKHA_70JExQOUd02mHdAy9Je-CRKFh9aby1WZUzjyF3-TlXxdDFF_a5bdFUlJfkWlgAM56hbDPQthOxssqrKXeOUn1aOlhk9OfoXkH8wq40XZaxEG0GU76ElEW5V_BdVcL3VT-5pbzA5Vn0VwUovfRtNMEMm9SHBJ82-EA9WeVjZcLAm65TlMOwDmZgJHwl1rur3rUwOYaix529utxJQHADdFKeACtzjcV8mQJzl9LqDvAHb8xn-lDFU-XjRCIsKtDPRIFnowo9XCsT21zQlZh1AA_3rDecw5v1qyVrG2g0KifqH9bANg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکوردی‌فوق‌العاده‌برای CR7؛ پست اینستاگرامی رونالدو در فاصله سه ساعت از مرز 10 میلیون لایک گذاشت. فک کنم بعد از 24 ساعت عدد خفنی بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27558" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27556">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A76dqg3h59jjpMT_FN8r5H9A0et48joQfHOY2aZlyKH2EHz25KLzcsp17Iuz5sNuPx1CT5kLDPKrky-BAJqw-7d32d1q4GlqDQtGeMsbc76aL-VOWXS9y6vTl6TkFtFCAd2QLb8awzomqzjqswmMg4kGQ4ovnZhrmgp6ADzThGOoR3uCU4YeOjJPeS0He3HT0B7tixoUE8JccH_-cHJ7DuXHwX9xuQNo4oFV-TrGaBsXLLrtM3B4NU2-6ibXCgRve-FtEk4zyWaZ36v3KR-e0uJ3LNxVcylVA5Suso28x8rkk_zX1jpIR4_Lw5KXwvKyucpfFLOxlw7hxYUPAo9xHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27556" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27555">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZmZr4frL0uAnrju-RTuxNDBdm4ni0SbP7QqtGvjGS3VN_0XA7fBLDDBNh6gFm3ew4NTBr-nA7eaL8OcenLbSAf_8f1e-poXGp1r_UmShJvPrPYSVL_hpUHSUSCC59R3yHH0HHPxHx40dSqOK6UcXgT2B5y86Fv3xn_lMuMKdJPSDQ4d0B0V1MXVDXDAwqbkndX4VJc0GXft78NNZZYVYmKmrKUBpW_oWpaS7x5zRbcBEdx5bwo3kOycqCjk46cNGZENb1k6XajwnGYcWUGYREpP8whes2ziRJhUPoA1xjFz6R0EqE4e9f0oE_ZIaY4dYXmE2fGhSXNAzCfG0eHySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27555" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27554">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd7nYyeUMkcNjG-47uH7wqIoaIxzEMh1SkCnRau4Ec06pkhR-F1MJcCBZgtw7aceadQBC1e_2yEWES4ff-WuEicsFvlOJLmvbrBPFOMZlmz_l7iknlanzo2tigvvUBs9sIgR_HTreC0RG71EJTSVB7AvrcxYmonLVKSYSKpXLiU4ZoGzaHg9W1W7Le79N8sHI4v7f-pQ8HBzPa3i1a1PFArW2XfuhbwdqenTepWaFCIO_fD9uQsQCYoQiQHkdGh8j0Wc9H71bjzenuQR3jSfwoGbbaP79RMtksSN7yMuvfz0ZhulNjT4TwBOPmyXXdmhHN8sJx-CefX2qxb8sIuyRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27554" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAydqCYgA34ykulerjGMrGUVl3WvCAfLY1xe0QKAkZyzCd1rtbgYO9e7ACUfo8PA99jFtPdqRQk-fZE-7Kder2GQt_IQPy3jMtxLgrxXlR5VPrwHHKvRUkALIG-TiOCw6L-006fRlZW9KekjH4xK4i0ujz86Est124dOVZu4PXTSg8W8jHyBV2aVa4WBsuPLb7nY8ZviCh_SU6Z83ChQWsTtOmLBSkD1TMTijns6M2qjzyM9d7b50_mHQG3mJCl660g4dYabpgCJO_kN8mi4StwbjtPosq4_m21CV7MbhGVHEfNGmVG4K-3QGYNZdmmDM75hhF01LaBlMaj9W7hpuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو اسطوره‌پرتغالی‌جهان با انتشار این پست خبر از ازدواج رسمی‌اش با جورجینا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27553" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27552">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇹
🇧🇷
ویدیویی از عملکرد فوق العاده دیدنی و برگ ریزون رونالدینیو شاعرفوتبال‌جهان در فصل 2009
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27552" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u01IDMDjY66adm4XLB3KTJ58W6ebwkphjgyvMmgq-Cr3qMF5ASdd_SMYiH6vgqjJ18cUJiPrL2N-pRJ-39dUTHeuyNwMkjmSnq6x9nax75mZZgKAjnLppFgts0sb8mexkSMABJNiV8iCXQFK6JT9T9K8nCgN6xB8sGMOaCJz_kkt2lM1GUUfSzZ---95kPyRpPJLLEtjcaaZKJRuKBPG9KYHkqr_X95dbDa703GmJqFcj236V4pSE96ZxBa2u9a8_qlwcIaN1HkwO3zxo_M6VV2ubZ9-ZmDU5S1-ljpPsOze55TsTJ4YHgPfpcGJOp3t56_agpdfXmMHtSlluKv7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27551" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgBSY3P9nB7V2uBMdtwI8RKvCkJAXnWkjge2X5nvfVadRIgUiM9zLj1FeVmWW5craA9YmrJFDLEzsF0fOocrmBhVAdUPXu0Y40BQ3uE0kqBIbqCQLdRpcrsl1Gk1fXeg65jEfnDv0omnWF7TI1fEfFtg5a4Cv1Nh8sFo6bSGox0ifQPxeu7QclHqT1Qk3vWOmybUVYm0w8UIKjxjUYbR_al179njfu2kkNUDKkRR9lZ9CAWUnqtiCZ-TPDjzr35zwPvfOlR2h4tPT9p5n7lT4Wb0B9ZHcfF1xNYGXvbdjDIB-b78WzN6xGQK0vJtpO22X3s5AIdRTAaOQb0hQGO6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27550" target="_blank">📅 22:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27549">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7Q3VqBRd0vigxSqbGjgUoXhkYMpyj6DGn3rPUx8xMzOvQ2d_8XNiwsLW_67d3DOPF40dX0rLmLZMqpSrhQApog6RYVO-4KD1KusIUGdEJ02wzT4gzNIlRuCnef5Xz7jUXNyF5Jyt1yRknIBGC1H3QWbW-LuNhLlVdpIxnd7Pjb4xHsGZOH1-lcO7B-AE-8_dobPUaphkN-ghplli6XVib8lvYK3Idoh8pfjS9TTZszOwI4wiY6n5QM5_Rl8zZrFAx5pP0i7sqqjmSibNteBImish44KrcLSi8YPBr88-tvU7yVdbgLK6yFHM0DuH0euP2M05zsEXlr8k0BJDCvS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27549" target="_blank">📅 22:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27548">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYo6acMDVsaOTRn9wVP5ATrD0wr-RL_WXC0FsZx_WL2nKRMR_w8vKGCxaqVsTZHeE6S5VSTC-7H6GeKvd_wVpEKkNPZG08FMpQ7uPD0wqpBd4Yeg0Lleb1KPjtN80Vz5sXZam_Os2R-waMbsuhamwgvsIOw1P-kvp3ndbAB-OrmaT8e_08eklkFWJFxq8AAxkOUTp9fSpyBmm545I_FIToaXvIoyf3TThHDoaU5UVUmxN3wolOlL6xldgMSYqJ-9k3q6o2u1teSoal4NELLzhY1ExTWos5bvsqeJ4Tpz2joKxLrlqOtvurX5tfzDaNQzrX0OTCM6fVDstBaxM5pOSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام‌باشگاه‌پرسپولیس؛ سرژ اوریه مدافع‌راست ساحل‌عاجی بعداز توافق مالی با مدیران این باشگاه رسما از جمع سرخپوشان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27548" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27547">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppw9E6kAIjJbUKB6NrAFe5dTcCOT4GNa-4O16uP0SoDcSaBpIBn8yVSyqjf5qpXvNzZ7KcJBrKSKYoUxDn8j1WCOM37CQelN2N352H9wS3eCrbvhaoSSH6bSAa9MN8D5Z69rED-D2T062uHzL4ld7otnWeqTfi-jLpNYnb4Iix25UK6USaGVmD9UGol3zdJ0d5sJ9e8J91PDzb1KHdwn5y6F70DagBVa8vnUeL7mBGjgJeWZuNuryfdX-BAHvar0_XZwCE2faMl5myLxOqdHeHUh7ulqdjUdeuJiYR5ytsDIRAeqGG1erGTsF0aBmxc7ADsceapV67GjTd0B88hxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27547" target="_blank">📅 21:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27546">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM3VxeoWuI7n3HvOAF__p8pLlijC5n_Gi5UlsT_pj3jCA9AZjxEJjDZRcCQZavlKIJHj8aG8jHovRNzB2LidVU06M-OYK060lZhtrLAdKpIJJ3Cx4dDzQz1VVYHsW0hkrKeFcbDJjPfzm_DqvGFwAorN2xsadw-cGtk9y8SuAsCx7A5eN34RYSCsqzTL20JUeGpCQpnD5dD_DoRSsB721_5jgZOhc6-jAz_XoM0qCOY17vAJXf8fOhK7OoKy62jnN3NQNTu24T6rs1gUfdhObqU6Jm343ec85UkUwR-nWxIak_PXYHTCKHQ23Yb9Lb0VG15FF6iEc-Hh5NxLzuwlUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27546" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27545">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikaN65eJRVgJhGMEVIujneQ2ObUtRxADuKhKNPnCuhR7_wpNaoANYGruEHIifIxwUw_4irAk7Gy4xQlFsRfz7UAwb5shYKpOD0dU8HmBl0L203S0RLJPNu-dldXu0ktAG7PsyYTam-YGpm3XMMYuHXqXa6YO-PIr_HuNHIV1YhqBvDrJF-qOznNc9T8eMq4qdEy5A4iIxMuZTMeDN1h7xv0LcBOLw72yt7N86BNnJXjYPjwpXpxp7VVt3k7dtSOhEFYDiW0dkrH_hL9a3qalbQzxlLtXH7EKopx0YHg9Pd3ZQAHK_UP49WlrfMocH_TOvgUTIhDVCTdfYXNJUF0Pmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزیکشنبه پیش رو یک جلسه مهم در ساختمان فدراسیون‌بین‌هیات‌رئیسه فدراسیون فوتبال برگزار خواهد شد و اعضای هیات رئیسه برای اهدای جام قهرمانی به استقلال رای گیری خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27545" target="_blank">📅 21:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27544">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z04jeGREaq8UZjlG8qH3tLAMdRxbsI2ut-S8WoW5PgDbpTLuDK6Ce-usUesp_tewR9cjyY4ADCrrfx9_GuRkYGbdGwblfrEk3gM3vvoehxFhUibFJDEVE07QGK9fzfKForgbdqk2P77pXdqje_CElmGh8kZMLQOVVJSfebGnlqFzDU1gyM27XiAf-QnjBiudLjY6rFnznBSlwE-2E2gY8-5T_UfVlOjG4rXy_AehHhXOdaM2hkr-kKiIkW7SBx2vCErd2FQ693IEYw5vg8MBNYhU6jelUjInjGpC0RwvZLeDd-sI-Qv6jxoBWPL1-kqGg-Vy2CeehMAFKqkLL0DDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
بازگشت‌دوباره‌پُل‌پوگبا به‌فوتبال پس‌از ۲۶ ماه دوری! در شب شکست ۴-۱ موناکو مقابل رن، پل پوگبا از دقیقه ۸۵وارد زمین‌شد.  پل پوگبا بلافاصله بعداز سوت پایان مسابقه سجده شکر به‌جا آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27544" target="_blank">📅 21:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27543">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B15CFDYFd1VOr8QBd4yN_0mWugln0cWFS5BoAZpp-8_cldTijGcxGCTlZKoY8bx79ldErQTiDhppwE2JgAdBtZtMBEaOIN1GhMbHG8YJ_gFB17uM_gL9oNVeU7LSfEiQcEJfMvOzKmyPBRnAtm9uqqz7Bn4-M5TmuRcFZLR2UWZcDGSSXe-RgBYNLGAMKMD_NlKYDj2KdNktytItdIWtBdQCnWLtoilbiwAI0Tuk6hD_Kpsr7HmPVcAzQOfdMCj2veNAvNhCLVPB9GWP6L5DCea1I6LoU6AzhG2ZrxZxsjvWj-uJv81DfNKjP-OALkG-jw_WO3l89ODT-dGhwHkKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مرتضی پورعلی‌گنجی مدافع 34 ساله سابق پرسپولیس با عقد قراردادی یک ساله به ارزش 600 هزار دلار به باشگاه پاختاکور ازبکستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27543" target="_blank">📅 20:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27542">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
#تکمیلی؛ 7 گل فوق العاده تماشایی در مستطیل سبز روی ضربات‌کات‌دار و ماهرانه ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27542" target="_blank">📅 20:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27541">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGOIA2Ux2J2KEfnDiLRUdsPLOj3otlLpDBvN2e16OrEYpKSCbVLYGYBwTUtc3rsb58gO2tYOqFmhWp9D8HNiibO9TknnS65JqXAc7EzvmOyVPXsDI74fnCRBJ8_6s-AHTC2C9Yr1sz7o-BgTcw6cIEC0cBtWGQ27K6XbvVRO_H1a3yboPvHGk1899EPP3vDgMrN0-b8icJbJiNV-UuKbOGe-k2VTMPV7W685hwaruJbUfEqzVn-rHcw51pUKK8D4BgZeAT9OMUVWYx5JTHhVzXE6mYFzr9drX-SHWfsJA2pRCDIOm_sR1AZ-bdYIwxBdt1n9Vzn6g4sjlUUCNQ2ssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال تخفیف است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27541" target="_blank">📅 19:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27540">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn64px2pf3DkBdryS0t0V0YXxhPHx-IAL0aRu79M2Ps84zeG1LP4Pzt01p1rEIUCHi-7zsNePaJOg1E5yeK2QPk-Ol30khEAYexu5sHR0ADzBvM-iSmwaKj1USWLZ297SvYRTslgJqiXYejcScm8N_kFsj1Z12tN6krp5N8QymzSyH22ycBk2KHV_oAtBMl0pThryyLpi_snaYJ2Ioh5W0LyUrzZflQQuP78UmgdxZIgZmRsBMKMccAnhNWQ-O1JjGH8mVZlUE_26P7rp9kpEzAri6Ya-ddyTFL-8BV5rTB8NmedtyV5_U2Dcv47cZaSyCBYV6aVWB7wTXhXRCaasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27540" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27539">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZWrr_qqMPZDobIGpelr5bz7orvKwUPKkVETBGjI-Oqy4ARcEO3bMNRQCLPHuM_Fhes_QUquTQObQKtV1IasBedVcxJZ1JgQugil3jWp-6pw9iZmFLalc7fcSS6z9MUdqGdl6eaL3_na2UyhvtTBbisQiZfJ74VBraZwfZsrNt84xGRCbmtVsNU0DktLMBgpWTdeZUEgT1Wi09Ysw50Yy5mfyo2I7dncWYkZqOPSDCcmNQ6jZjT1XVmj40mW09am2jjTgOcdjEI5Bw6IO8WIMqKTBkRf-w4On0XOZjOuuvjpBVtQSLjtvRHh49kLUBaKRQucxwpmPUCCKQaA7K4lmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27539" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27538">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5Dslk7tNGMHBpTKncOA1kf96G1JalXrmziV3By2yVrUXnCm0QDV_BwTtuMY6VYli1ojsKNTXy1lCVXq3YvsefzXWclfq5b07spME0S8_H8SXi7Dxh1L3erwXdvJvF70x1VkVdUwOaKpci8g6dqSqzPthS9ozW9efx3-h2HEMZPED76klCWdgivayTm6XoQh9QNKSAFtYu3QrHQbtdDxa8a2IuKA-q0XTaznjzPEfaeScjPfyDR2WLceSq9EsVW0a2ckGEr6ymS_DNNq0uJao4Av1RY6x-kwgS4n1EANwHTIYHL0N9MIwQGZjzuGBrpJabFOURsJedx8BL-IUCvaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
سه‌روزتاشروع‌لیگ‌برتر
؛نگاهی‌ به‌ ترکیب احتمالی چهار باشگاه بزرگ ایران در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27538" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27537">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKyUJcyh3AsCRb76Nuc93Ht87Q-Eq4u0RS_9om10sLvj6dNYCx4GKtFvkFgGyoBlQFmDkAxNdwsDfnGcY5vOcLt6wloRFxj6JNz1QvTBNsxkyrJaTAFatjKEhZE1OkxCQGcg7rRRzKJJdREtMIQF-93854hsaehn-DaRHR2_g_whnkPgaVhnEl0kv8X1Ay8h7ETtXxYMNl2XaMETsjPSq6KdMoVBekvmL8JGT5OHneP2im81681yO7gfhposQjkAQjAVck5hPjjLUGDe35vO14_sQ1YOV0MoyQZXYzs2rqMy3H9orQaFx2TTYjagVCK_lfdFHhvGbqxDZwmtaH84_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
آنتونیو گالیاردی مربی‌جوان‌ایتالیایی‌که چند هفته ای دستیار امیر قلعه نویی در تیم ایران بود به عنوان دستیار روبرتو مانچینی درتیم‌ملی‌ایتالیاانتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27537" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27536">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=WgcyAJNmzr-Y3Ob7KQzZYXHWr8LnEZnRgEucn1hckW3Pu-DtDE7idALYVAFx-DNBhqVuhwnDNPusJgfllrOS9c51R2xC5w9P-QFgk54tDOVaO67g9lfIROpgLGZ6YtpSWWCFpiSJFQ1Anm4TuM0DnmQ-5qf4WFWPEWrp0plBJbkSOFxGwJIyMx6r0OWXqqw34hDXdT0EvrFGt1WbiLflZgGox_qN67ILjXeWnx-sxyLZm03Aq-hvbUUmJHl0zyZ8bsQ827m_QnADJ8Cus7IHWJjPvv94PC_UwhvmORvnxjiWhpGy1pg2I0EQbl7EEbau7bkQoCVWwwBQPilg0a7zJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=WgcyAJNmzr-Y3Ob7KQzZYXHWr8LnEZnRgEucn1hckW3Pu-DtDE7idALYVAFx-DNBhqVuhwnDNPusJgfllrOS9c51R2xC5w9P-QFgk54tDOVaO67g9lfIROpgLGZ6YtpSWWCFpiSJFQ1Anm4TuM0DnmQ-5qf4WFWPEWrp0plBJbkSOFxGwJIyMx6r0OWXqqw34hDXdT0EvrFGt1WbiLflZgGox_qN67ILjXeWnx-sxyLZm03Aq-hvbUUmJHl0zyZ8bsQ827m_QnADJ8Cus7IHWJjPvv94PC_UwhvmORvnxjiWhpGy1pg2I0EQbl7EEbau7bkQoCVWwwBQPilg0a7zJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27536" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27534">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzJIfbr_FnvXe4buk8KB9M8pnM9l9UxjpNbljwP6_ep4MacOiuVYtOisn_C3_wQsbeKwujZzAAXoUIRSRf1NVAdKW4aBiq3lSGKQAvDlMAUjx7K_OZwjtI5r6SDbbaQJQQohcfy2Mzl9POYFZYnrJP0n9fXBJxXdO1iPASasnSUO9HJ5Ghj9ACl4n8_RcpvYcRfc0BoAyCljojOhsApIgeXMR7ZeLq6huO-XYPF_HiPpeH7FWUaApfD0-5RtToH9aCUnnqw292o8IRF5_env36NEcIIYvFGTW1ZIWxebRC-bg8RV4oQTetjssoG4m5wiJdAAY5zVbGDLtRup2J-3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27534" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27533">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijBG8J5cRaw9UYB9XznDidPkq-l9EFOIk0h5bIJfgZeRwZiJYt8bfJ-23SOzCodvts8dZxlJRdG9lHEQ_MRD20-fR0-DReZK5fXk226HxzDxQvGQ0oEEPFRmeAFTB6GdpVK7_-DgGIlDfA41RuJbSdXDgoTPILH6wgR8cniNW_DaR3HqcRM24cVcmLidBzWEJFLv8IP6yogEvLRN42pa6PWsZqZ2S0FCAx5oNUNfJ0A0pr-95URrVeSAzPU-OgJh1s8G4OPBYV-rgP81j3tzJZyuE4F7dyqMs45OU4Wg6uxZI3iq4rkPpA9zjlxIdgs9SZfdtTD6pvwYpEiWfkCapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27533" target="_blank">📅 18:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27532">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_bHJMEMbBylIInjUjZE7JVQCspZTe7oHAswJQlbth4AcMM2qUNFRSokaHCHrINW2T0WXw7c4_MVIaTxUSWtycblss31NF8fG3uJZ2O4aFGf8PXzItGPEzp4zisA__LddYHt3B7tbHlycRvIo9VDIC3-gs1IAASnPu04al8rRynV279f8tnpjQIgt8JQYjYtaWTLtVVydey7DBthbNlu6T2QecEJoTmRD2bCv9S0h_WkJfoKhRqmja4kFPasy9UT4eOf-yja9jiclvyCeulO-iOirzoWyBiymXpTNWJlz_4Mb6u7DquntzPs9Ov3syAJIennGwUgOmejFtKOq0TwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا:
به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش گفتم، ازدست‌دادن کسی که دوستش داری میتونه آدم رو کاملاً نابود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27532" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27531">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27531" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27530">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVCaDZopBKwClvS1nlQQVQZ7U2s8m2KfwQuIOQmYzrXqYAbI2WYskJMf3zeJYtLF7qj81a7ATjAGMunZpFngqt1htcL07gRHp16ZpWRax4kOFocpvR2TTyc8ykLIowsZwiExOx_SifNfAsaE0Y82AiDUemtyazUnb4tcBabZA1Uv2hQVrbIaMVaq9k12suTnwRdxiMwDd6aRfjYBs8Wtz3n1ZJOaJNDL6xKJwvPdK641piW6NUxZ6H7JFsgg4B22jAfoGzPxfHNdygySgjpFcUvdRq_5OAPm5HDdKhj5j1BkQNIQJ5erETc9d6iL5qok_obwQqldknR1lPeMQM36pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی برای عقد قراردادی یک ساله با سپاهان به‌توافق‌نهایی‌رسید و اگر اتفاق خاصی رخ ندهد فردا قراردادش رو باطلایی‌پوشان‌امضا خواهد شد. ارزش قرارداد واسعی در سپاهان 10 میلیارد تومان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27530" target="_blank">📅 17:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27529">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqPSYMd0Bg6wx64x2NnCQGOcLUXN8sEVzIuOkdMJUVzBcND32vh7w2oDrGRUpIYc32CUHIuhc814SYFjf9U2PsQghIzI2PRL9vAjb37PVevzXcSnsM98K00NAOqmsthqufDukeWtKSGHS06UZ7Ki40BWEY29f4H2ebNfT9VsBoHWv1q1RhzTvAoGwSbQ8oHiA20POMzir2JrfGoaxjf5IdBkcPNnUzmmZvenKuSghaQTf4N4XVmvLRq5tRbHk95APpYqahFL-oIaSq2kwPLvvzXWE_azOD-6Mkf6zbL8iLCQtaM5FiMlEvIsVPLKRuM7tUpXB4kwi93KEy7XuqZyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27529" target="_blank">📅 17:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULrDshILRnAyz_TgWOoI6Tx-VEtTKtICzH2YP3ias4D-irbZ1qKnIyq6VrDTtYx-RJAp18WOtDKzOFZgEjBe90sFDI2A6M3mMlSmhH_cM_FrXOZXls02XSud1UiqbsnC1TmF5l-G97t2Zb6ymUri3z6ZaXnzZkgwUJ8DRadckmG7-qWIvE28_oFRhYJQZJ2oSU4Wpj1NZ0qGMJOkAijfoYxmYDbiT8-3JR_2ytQaFsFa5Du3qdzEKu4nr_1vkILZu4-WA8zmlrG-cDZZw1lkJZ6bWsdV38mXH7cyJ_BIbT61NwUckesJpuvRFaNrcgYmZLJhiv-HujxLrdLEnz2MrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔵
بیانیه حسین زاده رییس هیات مدیره هلدینگ خلیج‌فارس خطاب‌به‌هوادران استقلال: استقلال تحت حمایت کامل مالی هلدینگ خلیج فارسه. در نیم فصل و با باز شدن پنجره قطعا تیم رو تقویت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27528" target="_blank">📅 17:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27527">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETFEYX8jvS4jC47PSke64GA5VKzcKmJ1njmwkEQd5dyhBoUg498reXSDG4VhsPkjuO09mR7KSLkkJ8-5j9FNd7B2KrVVGTNrxxQ0mh3uaIv0z0Nfoi6cE9CGWyYUO-4YvI_WA218X0_Cd1fQbIq5qyPk3ghv9NjFgLttZxZDBgXOkbwpp4QuEVojcDUdhNxbl3N7nsgNSpjpQRS2Btvir8Qy0KZPAg8XSoY7lgzc3eKse1SV99eg1hbL942uRnQFqZtm9UUdw7qca6wlxaRf_B6je_JBhNfIq06IzbGtpHqbrFRQFuQMMbKWLGKZr_jIgUjdVKGZe5Mg_4IwIoS5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌های انجام شده مشخص شد؛
باشگاه‌جنوا ایتالیا باارسال‌آفری 1.2 میلیون یورویی خواستار جذب آریا یوسفی ستاره 24 ساله سپاهان شده و این آفر روی میز مدیران این باشگاه است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27527" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27526">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abXPYphILEIxRwhoN0_utm4cdd9iSRw7fLA4R4uCXpLvJxffpGvYEzJgVoqAkqfeIvu3K2ERw2m6l16OJYnw2RkEz8pwu63AymTUe6Zq0hmx7J1YVrQcXB2yDuFwTDM1cd_t4p83fsyrH1krb7gw87cL8Iv9GXTojTGcscQVVi60OWOEwwqGZFAtxtpFFF8PUTmjl-FF-y_Hhb9RtvHq-DT-EhKt2d1dpc5xBad608DyzJzX51F8pA5HHxR6o3fHqWXty4p5CEKG9Zehis1NCaLaHkaYmjKB68pgJbVg1iKZM5Gz5LpZJsCU4cdojDEg6I9kW3shuwoOhHkT04DOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇪
#تکمیلی؛روملو لوکاکو مهاجم 33 ساله سابق منچستریونایتد و اینترمیلان با عقدقراردادی دو ساله‌ به‌ارزش‌هفت میلیون یورو به فنرباغچه ترکیه پیوست و شاگرد اسماعیل کارتال دراین تیم شد. کارتال دست گذاشته رو هر بازیکنی مدیریت فنرباغچه نه نگفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27526" target="_blank">📅 16:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27525">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=pdib3qMNGhS7EEjxkjwTyRZT_BxtBw8fQ2lkoGeq3KGSlmZ5OnQzLG7XQMFaWAraZKMtH8TL-DHUeRXb6_jout0VTfAkkP1rrYkR4tJ2oT-vZvwGpzu8FYmlG83bZSltR2Q9lctoXbq_t1iQ7t7y21F8BuukNFmbCD-Dp6w1RPMeo97GwTXRQzOa7PooGfORHe_p6cR20-UjbIQTHDK3-HW6rW651bR4hB7hlKz7WppLrlpHFYT13WgS9UiYh1O8e3YswBNmN47ORUJCxaCcaSOG7GT6rLcziuqh5lCkMTebBEBUoQfdpf-_OkTjhsB_PsxsOVgeEJY0bnx4W_Esog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=pdib3qMNGhS7EEjxkjwTyRZT_BxtBw8fQ2lkoGeq3KGSlmZ5OnQzLG7XQMFaWAraZKMtH8TL-DHUeRXb6_jout0VTfAkkP1rrYkR4tJ2oT-vZvwGpzu8FYmlG83bZSltR2Q9lctoXbq_t1iQ7t7y21F8BuukNFmbCD-Dp6w1RPMeo97GwTXRQzOa7PooGfORHe_p6cR20-UjbIQTHDK3-HW6rW651bR4hB7hlKz7WppLrlpHFYT13WgS9UiYh1O8e3YswBNmN47ORUJCxaCcaSOG7GT6rLcziuqh5lCkMTebBEBUoQfdpf-_OkTjhsB_PsxsOVgeEJY0bnx4W_Esog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دخترخانوم‌رضارشیدپور مجری‌سابق‌ برنامه حالا خورشید شبکه سه به این شکل که در ویدیو میبینید پدرش رو به مناسبت روز تولدش سورپرایز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27525" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7BwkKKzrMenrzooEDkfWiW4t4QUwKFbmzls2ynegXvUB-BZQzZKbbND74z1_0Ju475E-EBUJyyoe5JasjwszA8JIxe0BIS1oheiTEAW0ckgmi-q28JVgVEe656lCevTTusvbzmB9Q3UzgGxyvfASkRndfuKyhDR2UsO7TBbCG7uMyf_I4dX7sZKnsluP95HbZWBbtA2K8IKoTXwNZjdYUHroq5Iui4zUcZP2Upz3EilSeEhMiRfQSfR5M0dmWRfs4hhy5mnmB2_rUbAzytSoos-D7kpnLjrooRnJk77KBJV3e5o9TfCZgZn_7F5bTc5G8NValjCHdYaq2XVLq68EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27524" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
بااختلاف‌بهترین‌ویدیووترولی‌که‌میتونیداز دعوای علی دایی و کاشانی تو برنامه نود ببینید؛ شاهکاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27523" target="_blank">📅 15:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27522">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/virjOjbBkdaQ-JVxytSlXkkomtTP8DV_8BhaQd9zOnFHbgG0yaAnvImMzDqAwXRjPNJMSvX8LK6kNuZkbJJZEjwH3-xnzivepCyznPAKIRzkHjXKqosiNvRZnTj79jPPFkNI5rDZ_lcMMUh5X_3ToilK98iKBLA-YrbiI1MJj18cZ7ihYNbM9EHO9cweWLMr6Mj1qA984joNaQbLhmX6PiCXSUI8iVfWtsctTr7lhpUA34nBbmkvgvBRCIS3HvvecZMQbVq-tcLWJF5CMM0Qg9f5QRHCFbMZY8Bcyb4WeFkK63uZXgo8hBsKKsb5gEzgApyVjdbGFuoGWE3746ueGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
وینیسیوس جونیور بعد از 9 فصل حضور در تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27522" target="_blank">📅 15:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27521">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hk4Wz30S8IIPFFRzDfN99xg0oOTOXAQe9uBRa_f92cT6S2N9FxC0a57XAEgQqKuRIKkLCDFOsRhrVOvYNrWndBOjVAfI_yUdTSJQzZBcWb-7bhmY5XDBLYOyFtCPcqGAcX9H5YyfrPUaU5nbJ5aDUfEMewNroxK4vxtrrGPqE3Cc83LRmf2vtxVLO_E97b2nYrM_QWw3ZoqO1mfQmElrnMTH0T8vAaymyJOfe2BWs3itKDQ-ZeUowoKdt6zyB0JIIijr_1rP0iCBeRknU_jKPCuathnYzZJLA8YE6zcpkDod-htLbTffWAAoXLDFFPbDYKhXe2dkTPDBRyB9XWXkDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27521" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27520">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/selhQJvLXBWCJfMLXPe8VubRc5oFzMEzArA4hksY6--5Iq1sJP2YrSnoPKHWNyLTjS2eM3XpWzpt20_UnujURJG7POSpA3XntjF3Vgdo9ABOv1kCUza-58vnxTmYUWcTlFfjj-JVGQ2O_hDZcLev1IEI9fIZk3LwwWpe-Uey3rq5FTCIkol1A0wEHi4YdIudBYCdhmzDw4X47u5K9J7n1P6q3t2qWxlfZmUD8GzuFi5wO7PUtfv0LmIf0BzL6PnHSHZo7G824WSzA_YCyF3QYnbEPysmjnBfHZp_iV-3VyTE9kVuS-hZrFfRQka8hv1hhEh82Tl_nTWGZVuHcX4_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال تنها 10 روز فرصت داره تا طلب پنجاه هزار دلاری زیلیکیچ وینگر سابق خود که یک دقیقه هم برای آبی‌‌ها بازی نکرد و احمد شهریاری اون رو به استقلال اورد پرداخت‌کنه درغیر اینصورت آبی‌ها از چهار پنجره پیش‌رو نیز محروم خواهند کرد. پرونده های ساپینتو،…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27520" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27519">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=F3PZKG1cGpAHks1BrYBY8TREFpFp8qR1ITk35JXqWsDCAMYr59NJDYOUne9Uf7IvSlAWD2H3Lo-1i1TIdNY3QIEAUPE5y9cWDpnHAEH1V566zu8YBHnVntetP8tyMo-1xJYVihV3yQAgFPs-99jDxp2C1jh4AV8Af2w9QGMpBAk1xjjpQ81AJr7s1ygEE94NWGIzRALLwnzFy1Vwjn_YIQ7715nJ7bvtyn2eek13k3E4GaRXHE_2sknMjwLmXzEArXuBTGPSNK51dZUKuq-pRxWRHby39RkV9KnVo3-JU5xCzTe8DtjIehdz4jHjiQ2HDy8v_KlJkEmfEOWKHJ01mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=F3PZKG1cGpAHks1BrYBY8TREFpFp8qR1ITk35JXqWsDCAMYr59NJDYOUne9Uf7IvSlAWD2H3Lo-1i1TIdNY3QIEAUPE5y9cWDpnHAEH1V566zu8YBHnVntetP8tyMo-1xJYVihV3yQAgFPs-99jDxp2C1jh4AV8Af2w9QGMpBAk1xjjpQ81AJr7s1ygEE94NWGIzRALLwnzFy1Vwjn_YIQ7715nJ7bvtyn2eek13k3E4GaRXHE_2sknMjwLmXzEArXuBTGPSNK51dZUKuq-pRxWRHby39RkV9KnVo3-JU5xCzTe8DtjIehdz4jHjiQ2HDy8v_KlJkEmfEOWKHJ01mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇵🇹
ژوزه‌مورینیو سرمربی تیم رئال مادرید:
هر کاپیتانی نمیتونه‌رهبرتیم باشه. رهبر تیم رو نه میشه خرید نه میشه ساخت، اگه یکی از این بازیکنان توی تیمتون باشه، همیشه یه گام از حریف جلو ترید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27519" target="_blank">📅 14:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27518">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgdlD536IgYy1PdueHNLXlchsvYLWdFiHiM9iMi23vkY55blR-jFXItmTzGJ2qIMU6tINmY1swG-cXWE_SfWEOSUQtvCvKs5NJ2L6ttEo_noKmiFlaQOIj1x88aChbQiAYT9zIiVGKqW0HnucpBuP8dknA-BcSTdHNxENEkDZLBzGe2FJaoyLdGIGZKZUCglKG0u-x9_jUSr73Lro63-UdSQ4_A4oBzdgL83aBRb6IHiavhfAaWbEhGPtjFi9j4OPipuTkCVNWBXY6hd925dhuDLganWEfs0LqNa43tC2GI6tfd_YzbHtv_N5SS7l1ODZgu3U1V3iTbc-OJJUCDBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27518" target="_blank">📅 13:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrwO4SdYgdo94FNUbRidb_DZ_3jQsO_9DkKVwc_7cty80LLCLhPUT1IviN872xif-vQ0TFDq1e9aJYU0k_1XulB_cJS0qGo-DxOj9DZ5gwmTRGYRXpDz2YyaJt_BfnGCtkA7PcdOhFG7xv1rV4_pIQGCjVOjciXQYrdEZ_GNjIBtfOMqeKbTmzsXxa4OR8zFTXdsBjmb_YNkGmcRWOYunz3tsZoTTC5FvJxyblm0vj0B4klCwJNCizGwqhJFQDNUTaLsmWecl7-rLkXi53cL0F5LOgC0deL8x1BsDu6j2sDwxZ1FLk8heiFxLco55qptA8DtSDoWdYRc9nwkDnIhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
مورد جالب دروازه‌بان سامورائی‌ها؛ سوزوکی دروازه‌بان تیم‌ملی‌ژاپن‌پدربزرگش نیجریه‌ایه، پدرش غناییه، مادرش کلمبیاییه، تو آمریکا متولد شده، تو پارمای ایتالیا بازی میکنه، تیم ملیش هم ژاپن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27517" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27516">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27516" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
