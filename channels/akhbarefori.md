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
<img src="https://cdn4.telesco.pe/file/RXqocQr2uIPH12uv7t5dB6IpwDGo_3TWNPIMVk9laTgBY2B-x6pQglUwecjjoCs8dr7tGge6K-O_ps14qKEuU1NNbS0oZOlmJpqglnZkRWJem91d8_GuZQFJVCJhbzbB9ZYZsYV0_-XBKTSriqX2qR_kb6_NLzMDDP2uSvFya2aCPmo7gNJz5sBWQS2huzOa2WfKvgiUScwWqayOhz-x3q9wm9MK9HasJWZqiJ_JXK75EVpiMXNPhXRmNOC-lq_j0_SXYCLLx5Kcg3GhqlzGDPZQpoYyNUGiArFjIy0w0I6P-soiHED9UNWHRzgkzGlrKeYmutaVRP7BnVYndPtAxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 21:27:45</div>
<hr>

<div class="tg-post" id="msg-654524">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
یک منبع دیپلماتیک به العربیه: توافق بین واشنگتن و تهران در دو مرحله انجام خواهد شد/ انتخاب
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/akhbarefori/654524" target="_blank">📅 21:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654522">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgQte6K4YYEJ_Cecca27tabVFU8LIpkTSTwfm9aJE2Ig8b7Yi2I3UZovHTl3A86fkp_ZwN4F2kfngDfMa899qWEEdzQTT0OAaHlHi90ZNbx1v4lio0U74bdT6B3O16IKmszfxaXevWcxQ0aoWPSZQy7SFhEIX7WFGGiboQfDCm3oIIaRq-EUnTLL7jemNQFi94k-H9NleBzFefwmIFyqveYOGXyLzFHNSkIdhHWjVIaafLD3gvOFfckYPSEe1FtMBrDVSdDqZ9xPopcDkKnBTG3ZGCzPtIvvRIZ5w2TRHZXNgSgBsMoCpSiMFznMGfCoDqMWvSkPDVephh-VfhQrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bccfbe369.mp4?token=Zl24OdHV9Tic4oTQTtTvmpq7WmAhmal9dHOlTm4-FI4Tloa9WsIm6ynBL9D8NrxlxtZ176KzQxhy3XftppqFps_5DFzfrenAATCXx2n_LSND8NTSqmaLVTkSPqqFqp2Y2kJ-aBZhR-A_4y1tsjRpW3kYiPEwTvlcp-aK4izN71Jb4Vt_0sxbZEQwhMAwzwqZu5jqtbaQ0mLDUNiRXdOqETTcSbWVgDeTEx8PeLwwWrMturBAXeXlsnralA4PlnOrzi-1Cp6lgGffBpr-3WawiBMSETOGgUZfr-hD-fC6_vziwI4P00nlGF7NsiUiwS34ZcVlCjiqHrLwAZTnOdyMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bccfbe369.mp4?token=Zl24OdHV9Tic4oTQTtTvmpq7WmAhmal9dHOlTm4-FI4Tloa9WsIm6ynBL9D8NrxlxtZ176KzQxhy3XftppqFps_5DFzfrenAATCXx2n_LSND8NTSqmaLVTkSPqqFqp2Y2kJ-aBZhR-A_4y1tsjRpW3kYiPEwTvlcp-aK4izN71Jb4Vt_0sxbZEQwhMAwzwqZu5jqtbaQ0mLDUNiRXdOqETTcSbWVgDeTEx8PeLwwWrMturBAXeXlsnralA4PlnOrzi-1Cp6lgGffBpr-3WawiBMSETOGgUZfr-hD-fC6_vziwI4P00nlGF7NsiUiwS34ZcVlCjiqHrLwAZTnOdyMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سفارت ایران در غنا به عکس روبیو و همسرش در تاج محل هند: بعضی مهمان‌ها آنقدر ناخوشایندند که خانه خودش بلند می‌شود و می‌رود. به‌خصوص وقتی آن خانه از روی عشق ساخته شده باشد؛ برای یک ایرانی
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/akhbarefori/654522" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654521">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnuHQJnFUSa7xciixbB1lpmayLnwCc9k71beVqJuuDx5kTqQYEUhBAmaQPTXrZuWWhW_u36kFSLgiExvGJdZu5lqjBrXS14GTItVWS4ERrEhIImGlJVa5nyz4zC-dMThzvypJqS4BK25odiUXIeZUyUVqM1yuBT-BTXCbAipcooB38zpky8zzQBj-Fytu2RpRKarDtv10bew9CEF2Wf7PB3QxQy9gFkoUOjEBijSlHgqdiA5bYAudeOU8G0G3nh6KzreVFTCTuVm2mq8C32zrcDztTCP8f-BlfilWPElEXs0nNYozeARIUhsS6DtPDZUMBgGTfof3Jtg-ch81rUhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه CNN: ایران به سرعت در حال بیرون کشیدن زرادخانه موشکی عظیم خود از زیرِ زمین است
🔹
روندی که ادعای ترامپ درباره نابودی این توان را زیر سؤال می‌برد. به‌گفته این شبکه، ایران با بلدوزر و کامیون‌های کمپرسی در حال بازگشایی ورودی تأسیسات زیرزمینی و خنثی‌سازی راهبرد پرهزینه آمریکا و اسرائیل است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/akhbarefori/654521" target="_blank">📅 21:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654520">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای یک منبع دیپلماتیک به «الحدث»: پاکستان به عنوان «شاهد» در مراسم امضای توافق آمریکا و ایران حضور خواهد داشت
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/akhbarefori/654520" target="_blank">📅 21:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654519">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQkOs4BqXjkrtqxCpldAYh3lRan2idhtXsCw_5rOlZJ2F0_RS0xvLyvwSsxK7K1sVZ9iGP30IajJ4yVxHPA9EyFDsO8Mp4aJcxIo8EWxNcTj_CejZ9OTzzOMKRXiF3-znNfvNByaQ6VxIIjgk_W1bNGWCGrxrpTO-oVIORkkUvK6BcyPKmq5ri-BRZJz6d9EOs7-_eAsOQ7Ygr04JLsSttTEhQ8V2dGwkbUs82xg7uSjhq1EPazahPvbftGWPAsjxE8rpLX63NJ8DzshpZ9NBgD5gHkrWt5kWKY5IHxOieAE3yHZINYsn-JT-unDxDCWgMImrmydE8pObEnn8NRjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا عمان را به اعمال تحریم تهدید کرد  وزیر خزانه‌داری آمریکا:
🔹
دولت ایالات متحده هرگونه تلاش برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد؛ به‌ویژه عمان باید بداند که وزارت خزانه‌داری آمریکا به‌ طور تهاجمی هر بازیگری را که در تسهیل عوارض برای…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/akhbarefori/654519" target="_blank">📅 21:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654517">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emnLN1_R7hl_lb1rRDCbBSMTSRE4athNFBOm8pVr-q2hVSVLcVD3eibS0nhwTH5kZelGoi3fg9d3WW7N-bGaESah7jDTYLRpFsqvi1tueIn1h1-pOo2DXfnTCcZxnqzJ08_d2wbMxwZMfFj3UdlpjohxXEV6PFmcLlPWp23pM-OYKCUrK20rVBPs-7XBmUYZjMn-dCQyUsLGTijnTMNCqjx4LKRq2_S9W-8eJfqbEyeHvoCJlO9kSFPcMDfE5fwRMhXdgmHuGVM4Uhe8lI3UVEu_Yo6q8lA4cCWqCe_D-Rc8weIYvFXmJbI-PDeUocTU3WsWUs-04HBszJNsS5XDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجله آتلانتیک: چرا ترامپ باخت؟
🔹
ترامپ که با وعده «تسلیم بی‌قید و شرط» ایران هیاهو به پا کرده بود، حالا اسیر همان جنگی است که نه بر اساس استراتژی، بلکه با انگیزه‌های شخصی آغاز کرد. او که پیشینیان خود را به بی‌کفایتی متهم می‌کرد، امروز در وضعیتی است که ناچار به مذاکره برای توافقی شده؛ توافقی که کفه ترازوی آن بیش از آمریکا، به نفع ایران سنگینی می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/654517" target="_blank">📅 20:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654516">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445ef439c4.mp4?token=FFcYR9A06yvEVgZOYVeudG0_XW4OI_OOzGmaSKxNWhFxCkUKCD7a0d48AzFSqDqzzX_8vXy_wy4ZpTqUPGRC1KpwxB71LrETHz6QM7oJMwQnMnGi_t3UzzsQAFaCUrEwV59gOWnURTLGrQLsZ9rUktGScFqkbqyzMLpZNOuypkhaCUThULF6XQn6xVe4xF4xEfP4xqQBjfEkscvyvbwy1Q9JcIHds-JzxmdWdbNGqIhB8xOivMpeISBs9ryop95nent5JuLOoeF4O45LsUYK4354FOEvFtSpynRz7-hk37xKs0wO-TuYfJDUrjP_4KJl03bf_xvfptNm51sn0iCKrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445ef439c4.mp4?token=FFcYR9A06yvEVgZOYVeudG0_XW4OI_OOzGmaSKxNWhFxCkUKCD7a0d48AzFSqDqzzX_8vXy_wy4ZpTqUPGRC1KpwxB71LrETHz6QM7oJMwQnMnGi_t3UzzsQAFaCUrEwV59gOWnURTLGrQLsZ9rUktGScFqkbqyzMLpZNOuypkhaCUThULF6XQn6xVe4xF4xEfP4xqQBjfEkscvyvbwy1Q9JcIHds-JzxmdWdbNGqIhB8xOivMpeISBs9ryop95nent5JuLOoeF4O45LsUYK4354FOEvFtSpynRz7-hk37xKs0wO-TuYfJDUrjP_4KJl03bf_xvfptNm51sn0iCKrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین پاک، خبرنگار ایرانی حاضر در لبنان: دولت لبنان و اسرائیل همین الان در حال مذاکره هستند تا ارتش لبنان به زور حزب‌الله را خلع سلاح کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/654516" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654515">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
اتحادیه اروپا خواستار مذاکرات با ایران بر سر مسائل منطقه‌ای شد
🔹
کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا امروز پنجشنبه گفت هر گونه توافق میان ایران و آمریکا بایستی با «گفت‌وگوهای عمیق‌تر» بر سر امنیت منطقه همراه شود.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/654515" target="_blank">📅 20:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654514">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
پزشکیان: به دنبال سلاح هسته‌ای نیستیم، ناآرامی منطقه به خاطر اسرائیل است
🔹
با ذلت، دیپلماسی نمی‌کنیم، اینکه مردم بیش از ۸۰ روز همچنان در صحنه هستند دنیا را متعجب کرده، درحالیکه فکر می‌کردند با دو بمب و موشک امکان دارد یک عده وطن فروش مملکت را با آشوب روبرو کنند‌.
🔹
اگر ما درمقابل قوی‌ترین قدرت دنیا ایستادیم باید سختی‌ها را بپذیریم، نمی‌شود بجنگیم و انتظار داشته باشیم روند طبق روال عادی قبل باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/654514" target="_blank">📅 20:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654513">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای یک منبع دیپلماتیک به «الحدث»: پاکستان به عنوان «شاهد» در مراسم امضای توافق آمریکا و ایران حضور خواهد داشت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/654513" target="_blank">📅 20:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654512">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار ایرانی حاضر در لبنان: جبهه مقاومت باید با فشار نظامی، اسرائیل را مجبور کند که از لبنان عقب‌نشینی کند/ اسرائیل بدون اقدام نظامی دست از تجاوزگری برنمی‌دارد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/654512" target="_blank">📅 20:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654511">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای منابع آمریکایی: یادداشت تفاهم با ایران در انتظار تأیید رئیس جمهور ترامپ است
ادعای منابع آمریکایی در گفت‌وگو با الجزیره:
🔹
ما تأیید می‌کنیم که ایالات متحده و ایران در مورد تنگه هرمز و مذاکرات هسته‌ای به تفاهم‌نامه‌ای دست یافته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/654511" target="_blank">📅 20:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654510">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
پایگاه تازه‌تاسیس «بِلاط» هدف قرار گرفت
🔹
رزمندگان مقاومت اسلامی در ساعت ۱۳:۴۰ روز پنج‌شنبه  پایگاه تازه‌تاسیس «بِلاط» را با یک موشک پیشرفته و منحصر به فرد هدف قرار دادند.
🔹
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/654510" target="_blank">📅 19:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654509">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
رادیو ارتش رژیم صهیونیستی به نقل از یک منبع نظامی عالی‌رتبه: بعید نمی‌دانیم که لبنان بخشی از توافق آینده آمریکا با ایران باشد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/654509" target="_blank">📅 19:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654508">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
رژیم صهیونیستی روابط خود با دفتر دبیرکل سازمان ملل را قطع کرد
🔹
وزارت خارجه رژیم صهیونیستی در واکنش به درج نام برخی نهادهای صهیونیستی در ضمیمه گزارش مربوط به خشونت جنسی مرتبط با درگیری‌ها، تصمیم به قطع روابط با دفتر دبیرکل سازمان ملل گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/654508" target="_blank">📅 19:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654507">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
عزیزی، رئیس کمیسیون امنیت ملی مجلس: تنها مشکل سردرگمی آمریکا است
🔹
ایران پیشنهاد‌های خودش را در قالب متن ۱۴ بندی ارسال کرده
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/654507" target="_blank">📅 19:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654505">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار ایرانی حاضر در لبنان: دشمن در جنوب لبنان بزرگ‌ترین ریسک تاریخ خودش انجام داده است/ ۶ لشکر بزرگ دشمن از ۵ محور به شهر نبطیه حمله کرده‌اند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/654505" target="_blank">📅 19:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654504">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c81dd164f.mp4?token=Ev6wi-rfvMmUbo7DxtNrs3G_ZZGdUO9Xkj0XJX_aRwksLRLHu4D0tpX2zFslq92mkH2CoOUM5EM88e2Pw95-lgkIgy7MJ1Eh3PREQLXb8p0QIhhmIOEnxKf2zFfMRDpWgeQ4WOZ1SyQAdFCexn1IJIVOXmPaniGLBFnokPCZVQiVKIG3LiHBxd2UIkFclPurLbYf87jvPT1vuLXE6E7q4f0Uar9gbybGZw4RnM8CPIvhtpdkeGR0RfbznPAg01RBzBgDvdUknVHI3YwI8OmIAu7g5o90kIIwxBkocVs9CnaU7Mv93ZZVrvjYA9XRzMVRyP56kFD-XphAIwDtN3FvuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c81dd164f.mp4?token=Ev6wi-rfvMmUbo7DxtNrs3G_ZZGdUO9Xkj0XJX_aRwksLRLHu4D0tpX2zFslq92mkH2CoOUM5EM88e2Pw95-lgkIgy7MJ1Eh3PREQLXb8p0QIhhmIOEnxKf2zFfMRDpWgeQ4WOZ1SyQAdFCexn1IJIVOXmPaniGLBFnokPCZVQiVKIG3LiHBxd2UIkFclPurLbYf87jvPT1vuLXE6E7q4f0Uar9gbybGZw4RnM8CPIvhtpdkeGR0RfbznPAg01RBzBgDvdUknVHI3YwI8OmIAu7g5o90kIIwxBkocVs9CnaU7Mv93ZZVrvjYA9XRzMVRyP56kFD-XphAIwDtN3FvuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: به هرگونه نقض آتش‌بس، پاسخ قاطعانه می‌دهیم
🔹
تا زمانی که تفاهمی در راستای منافع ملی نباشد، ایران آن را امضا نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/654504" target="_blank">📅 19:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654503">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
معاون وزیر ارتباطات: بهبود کیفیت سرویس‌ها و بازگشت ترافیک بین‌الملل چند روز زمان‌ می‌برد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/654503" target="_blank">📅 19:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654502">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
نماینده ایران در سازمان ملل: اقدامات ایران در تنگه هرمز، قانونی و منطبق با حقوق بین‌الملل است
🔹
هیچ کشوری نباید تصور کند که در آینده از سیاست‌های مداخله‌جویانه آمریکا مصون خواهد ماند
🔹
برخی ریشه‌های اصلی وضعیت فعلی را نادیده گرفته‌اند و به دنبال انداختن تقصیر به گردن ایران هستند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/654502" target="_blank">📅 19:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654501">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424fdf2b4e.mp4?token=pNbsQ4heAPk4V6CPqnqVisVZl8npQEtSFDs49gPTVv3QT2UBOzpaf2fCjE1RZQzhMTC6jqyFJwohFw0Z2BjUu2h0ObJaXxNSfqiTylGwBRCmYLIHdh1Yb52bTarnvibjqd9vy7aC1sLZw87opJ7QMixIEzI7pegXptWv6H4PBvqWGxQE7KxLTVT4dRN8sGJ9p7XnhoZAKHaBnQhS5AzvD5gMNtmdRrbrK70aa74cZq4a9F_hvn5-wW9vKko5OcUl5G5cU3V3H_dbT5NUVnTWKc3NpaExuPyVrZD04DchhVRPX6LVlTG24DOPynvZvTECiJO4H3D3MQNJ_JHzgqaGyQiQ5dhZNcuAHvZu33woLx4D9A4ggYqUWwFSDGdxGD0CGVOH09aXryf9G2uAe_HPhNmAKNqEtCIDuerR39KF8R6F6zWqIqURgCvYOtX7ghVXEjtd1ZVtIX1R_Dpqa_kaopYsjSeK94jerOv8lEysJKwkiTBc5P9d2VEEn8051jy3fgLJvHxZDq8UqiRuaUxpQKrsbhRQNdzdcOr2xpZTcrU2dT03pLPcybtZurSzY9lq1Q0o_h8s5cZZP5THFGZ6AY8NJYXw-G15c9KqI9qphHqLYj_9q-ZIl_fKGm0wtgQFj_qUoFFiPxNlGBKndFuhpDpAL3D_OMHTFci3oukZZd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424fdf2b4e.mp4?token=pNbsQ4heAPk4V6CPqnqVisVZl8npQEtSFDs49gPTVv3QT2UBOzpaf2fCjE1RZQzhMTC6jqyFJwohFw0Z2BjUu2h0ObJaXxNSfqiTylGwBRCmYLIHdh1Yb52bTarnvibjqd9vy7aC1sLZw87opJ7QMixIEzI7pegXptWv6H4PBvqWGxQE7KxLTVT4dRN8sGJ9p7XnhoZAKHaBnQhS5AzvD5gMNtmdRrbrK70aa74cZq4a9F_hvn5-wW9vKko5OcUl5G5cU3V3H_dbT5NUVnTWKc3NpaExuPyVrZD04DchhVRPX6LVlTG24DOPynvZvTECiJO4H3D3MQNJ_JHzgqaGyQiQ5dhZNcuAHvZu33woLx4D9A4ggYqUWwFSDGdxGD0CGVOH09aXryf9G2uAe_HPhNmAKNqEtCIDuerR39KF8R6F6zWqIqURgCvYOtX7ghVXEjtd1ZVtIX1R_Dpqa_kaopYsjSeK94jerOv8lEysJKwkiTBc5P9d2VEEn8051jy3fgLJvHxZDq8UqiRuaUxpQKrsbhRQNdzdcOr2xpZTcrU2dT03pLPcybtZurSzY9lq1Q0o_h8s5cZZP5THFGZ6AY8NJYXw-G15c9KqI9qphHqLYj_9q-ZIl_fKGm0wtgQFj_qUoFFiPxNlGBKndFuhpDpAL3D_OMHTFci3oukZZd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار ایرانی حاضر در لبنان: جنگنده‌های اسرائیلی حمله بزرگی به بیروت کردند و خط قرمز را شکستند/ یکی از رسانه‌های اصلی دشمن می‌گوید هدف حمله یک فرمانده ایرانی بوده است ولی ما اعتنایی به بیانات دشمن نداریم و منتظر بیانیه مقاومت هستیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/654501" target="_blank">📅 19:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654500">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
الجزیره: اتفاقات اخیر تاثیری بر مذاکرات ندارد
ادعای الجزیره به نقل از یک مقام آمریکایی:
🔹
رویدادهای اخیر در تنگه هرمز تهدیدی برای مذاکرات با ایران نیست.
🔹
مذاکرات در جهت دستیابی به توافق ادامه دارد؛ اقدامات نیروهای آمریکایی در تنگه هرمز و حومۀ آن «جنبۀ دفاعی دارد».
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/654500" target="_blank">📅 19:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654499">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeeB1rwJwtguTuNsABBEmYR0BG_eS5c09Rzq2HtgsdnTmbElAb6W4LLDG_tLbcHarbwKivyM1A9P3CQ6clb02dhro7vCe5xjPKDO7Oc_u1XYwlSdC8uGJwmgtLaVEytH4IGa-xG3C77eO8aUkt6N5WX_LtL80_pX4F14iMAkG2WDgRhNC2W8kfLYcAfXsYkDUl6YiE869ntlJ9udKtyyVC_m9dGXNncN4tcn78a2boUKpBRKuUtyZpnkWKjawNkfM36GXT0-xEgc98en97JZtF5n3sgpLue3ta6zIVXTnw8gdgMjugIAU2nN54aQhxfiJ_ISGi9vvWvQa_RlVaD7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراسم توپ طلای سال ۲۰۲۶ روز دوشنبه ۴ آبان (۲۶ اکتبر) در شهر لندن برگزار خواهد شد
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/654499" target="_blank">📅 19:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654498">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0CzWVXF7nixPlxS6aO4VO5OzuzxkIrzDhaWB8H6yeO65ZTdBTXM5XZkO28_U0gvNXsF4D-5TQ2dLAbliaEYMJj9HkCCkl7PY87E_sWOsAXS5Mqd59zHzvxCsMGViu6JnhVIG3Hjvwx9ekTemVlEWSC2eQDHHfWNQssoGNffCYnVAhS1hevNi-om1rQES4R84HQ8EkoJO8TRhKe7MKXDTDjTQxVlCtqifcxYZDRUqBjUKUT7RjjiKIXfAZSuev-1vZHPNFlTN60TiekTimiCfm43hqVYekjcp5CbW9MMX5xAPvYYnfNQqm5oGPep_XED9UYi4mL_mlrX9Oy0LGgkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفاوت‌های تیروئید کم‌کار و پرکار در چیست؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/654498" target="_blank">📅 19:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654497">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9gwkPP6zSG-QSTZgP3hO4y7G5pE9zBRl6Ge5rezUHo200KzJVmH9mVABtffCrgQ4PiJKu1X8A-QAiSh1DP4csiw_rkeSX_UPaJ-VvlWbi6_yGFOFx9GvmD-tuGsbjQUf7GODi7Me9Z6SD9D4bRqK6ZOSLdp_h6uf4Db3UBYq_nTWrXRcqCbaGHGv6EYquYUMWIn-K0H7gI5q87wpBJWYpkk9k-AkLiYGVtAGTRwXJmMOi75SVDYZfgx7ziAxuB1p_a1Jq0vAl1rcEQ0fB2v216kmmVUbbYxP_8RdUkfK6lrI1RlhYFfQU-_yWVggu3DgHqP8MB1cBIlpJ_MTDq-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه NBC: از سرگیری جنگ برای ترامپ سخت و پیچیده است؛ زیرا اهداف نظامی باقی‌مانده در ایران یا زیر زمینِ مخفی شده‌اند یا متحرک و دائماً در حال جابه‌جایی هستند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/654497" target="_blank">📅 18:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654496">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نگران نباشید؛ ابولا در ایران نیست!
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
سازمان جهانی بهداشت شیوع ابولا در جمهوری دموکراتیک کنگو و اوگاندا را به‌عنوان وضعیت اضطراری بهداشت عمومی با نگرانی بین‌المللی اعلام کرده است.
🔹
با وجود محدود بودن کانون اصلی شیوع به چند کشور آفریقایی، همه کشورها باید آمادگی لازم برای شناسایی و کنترل موارد احتمالی را داشته باشند.
🔹
تاکنون مورد قطعی از این بیماری در ایران گزارش نشده است؛ نظام سلامت ایران آمادگی کامل برای شناسایی، نمونه‌گیری و پاسخ سریع به موارد مشکوک را حفظ می کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/654496" target="_blank">📅 18:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654495">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
آمریکا عمان را به اعمال تحریم تهدید کرد
وزیر خزانه‌داری آمریکا:
🔹
دولت ایالات متحده هرگونه تلاش برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد؛ به‌ویژه عمان باید بداند که وزارت خزانه‌داری آمریکا به‌ طور تهاجمی هر بازیگری را که در تسهیل عوارض برای این تنگه نقش داشته باشد، هدف قرار خواهد داد و هر شریکی که تمایل به آن داشته باشد، مشمول جریمه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/654495" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654494">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo-tJvc5SWJk0jxANLK3R_SyXxFFQoZ2QEp5xCZqDKc3n66hMMWj0m9RWSMdK6Ke1ASmy-fzgCDA4Oz5CANZxNKCfoVGNlEVMTYwu9Sd7I6GPaH61WHcuVMje2EIwqxbo3mt8dWKwpPdgPa5p_hJTpD_tTRJt3JPzSsTdj71fjZnEmSI9d27uWbBEG3f6j8GJGROodlNweLrc6GsbZj57BK4I3qUKfbMORs5WsUx1K35Wv50QZlYNvnPsCP1dQF1WjCcWIc2XTQ_ovJ1nUYAa61go8jWN2OegYUtzESv5HYFo5ojQoBHJNQgG7cHZfeOm3zT_MUyk1IQHGPu-1Ma0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ملاصدر؛ بزرگ‌ترین فیلسوف اسلامی
🔹
صدرالدین شیرازی، فیلسوف عصر صفوی که فلسفه، عرفان و وحی رو با هم آشتی داد و مکتب «حکمت متعالیه» رو بنا کرد، دیدگاهی که بعد از چهارصد سال همچنان پابرجاست.
شاهکار ملاصدرا نظریه «حرکت جوهری» بود؛ یعنی کل عالم مثل یک رودخونه، لحظه‌به‌لحظه در حال تغییر و تکامل درونیه و هیچ‌چیزی درجا نمی‌زنه. ملاصدرا به ما یاد داد که تک تک اجزای دنیا، زنده و پویاست؛ فیلسوفی که نگاهش به هستی هنوز هم تازگی داره و اندیشمندان زیادی رو حسابی به فکر می‌بره.
#نامداران_تاریخ
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/654494" target="_blank">📅 18:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654493">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای اکسیوس: به گفته مقامات، آمریکا و ایران به توافق رسیده‌اند اما تأیید نهایی ترامپ باقی مانده   اکسیوس مدعی شد:
🔹
مقامات آمریکایی گفتند که مفاد توافق تا روز سه‌شنبه تقریباً توافق شده بود، اما هر دو طرف نیازمند دریافت تأییدیه از مقامات عالیه خود خود بودند/انتخاب…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/654493" target="_blank">📅 18:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654492">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای اکسیوس: به گفته مقامات، آمریکا و ایران به توافق رسیده‌اند اما تأیید نهایی ترامپ باقی مانده
اکسیوس مدعی شد:
🔹
مقامات آمریکایی گفتند که مفاد توافق تا روز سه‌شنبه تقریباً توافق شده بود، اما هر دو طرف نیازمند دریافت تأییدیه از مقامات عالیه خود خود بودند/انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/654492" target="_blank">📅 17:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654491">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت خزانه داری آمریکا دو شرکت هواپیمایی ایران را تحریم کرد
🔹
پالتیکو: حمله به کوبا منتظر دستور ترامپ است
🔹
بانک مرکزی: محدودیت‌های چک برگشتی از ۹ خرداد اجرا می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/654491" target="_blank">📅 17:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654490">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
گزافه‌گویی
مجدد
نتانیاهو: ما باید ماموریت در ایران را تکمیل کنیم و من تقریباً هر روز در این مورد با ترامپ صحبت می‌کنم
#Demon
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/654490" target="_blank">📅 17:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654489">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iqxg1ai_p0_rvw-lO2XyY8kXlYnGoB7CACmWW4KuOpKnBxi41yRuUD9LHcT5N8jggqLW3U2X_ymMcrxwK8WFW7EdOX5Qc4mZ_AjvK3fvXvUtOTsDoKaAo88YEYnJyddokd7l_or-oQoq6SEzGD5L5APIObC6SgK_EeDK-3esusry_WDhK2wioU9j2okAWPo-TEhyQUrUmC2xTgj8IsGGIj6DMeqAPmJ1dBtFTB3pyUTIHmtQU44vp2ZPTvf2qw3Hr5JlHso7pxTTyB5cXba59ei6HG2VEtdWTQ9CST0m-CvxuK9GbiieOCU5GiIji0e1XeXYDjmWBuUF8syqFsEG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والیبال بانوان آسیای مرکزی؛ ایران فینالیست شد
🔹
تیم ملی والیبال بانوان ایران در مرحله نیمه‌نهایی رقابت‌های قهرمانی آسیای مرکزی به مصاف نپال میزبان این رقابت‌ها رفت و سه بر صفر این تیم را شکست داد تا به چهارمین برد متوالی خود در این مسابقات دست یابد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/654489" target="_blank">📅 17:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654488">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
علی باقری: آمریکا قابل اعتماد نیست
معاون دبیر شورای عالی امنیت ملی:
🔹
نمی‌توان به آمریکایی‌ها اعتماد کرد؛ چرا که ماهیت آن‌ها بر پایه نقض تعهدات بنا شده است.
🔹
ایران در مقابله با تجاوز، بر توانمندی‌های اعلام‌نشده، نیروهای مسلح و ملت خود تکیه دارد.
🔹
دلیل پیروزی ایران و ایستادگی‌اش در برابر تحریم‌های غیرقانونی یا تجاوزات نظامی، در توانمندی‌های داخلی و پشتیبانی ملت ایران نهفته است.
🔹
علت اصلی بی‌ثباتی و ناامنی در منطقه، حضور آمریکا و رژیم صهیونیستی است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/654488" target="_blank">📅 17:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654487">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: در صورت عادی شدن شرایط آزمون‌های نهایی از ۲۱ تیر آغاز می شود
کاظمی، وزیر آموزش و پرورش:
🔹
برنامه‌ریزی لازم برای برگزاری امتحانات نهایی در دو سناریو انجام شده و در صورت عادی بودن شرایط کشور، آزمون‌های نهایی از ۲۱ تیر برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/654487" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654486">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBz6dqSpOFo10uZLiOlofVDzwxYR_bBR8lvlGBB15UQ-7NjQaW9sAkJRLByBKq5OHn5hiXh0lShOtWPa5jRpcnQBg-JKLTuxOwWR6rQw45hTMd4QRn0GP7fXI_eDn6HHoXnnrP4G5xXEv0Wf7s7hl-5Mmhki3evWilPC7E5H5swFnkPuuBZUuVrJlX80PhBa9ol9Y3vlTSsfmRUYcgn5DzmEgoQKJyow-EugIFN8UfBKZZ0xsfEWwcyZXQ_A_knhJMdRVgTAkSj3LnyJEShbtaXbw3h2mRuvm_lgy6eM94O7NTF2RcHv0AWD75vMku_WlKnzzmyLUJmkZAcW8jYwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شربت‌های سالم و مفید برای داغ‌ترین روزهای سال
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/654486" target="_blank">📅 17:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654485">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c85fa8037.mp4?token=qP4AdMDS1zBCJEU78SEwD2Eu0lXSveK51KS1wLjXLdSayRoqLOxxNFd-qZvV_uVrS3go-C2IpPZ13v3GjtJVDk_ci0ed6R5h9uO6M22gLp-GXO09liBF1CoF-_zeQNlLlaPTBL1PlQGNYDwYHBw174LfJBo09QqwKuLgotojnStkwoWCD2z8eN6w1DjLY2bY8szHGQOR_ff9H81m3JKZhGG7OFSQlMfNByJJWHCR6Q4_el5M4LWBJttiZhBN4zpcHXVRIactRICfav9TI0Li3-LL-zF5gG-MEWp6UhxNJJVYz8GPNuMbFT0j9t4zbf8FpykkuKO8jZZsNxO6v9g4miFcdNLZoHnpza1c-QRcQASKhFmLV95GL5-BY96unUQiZ91Ey19BO3AywL_JiA1I-3-p2OlpRFkuigO062AkCMKM9AsF--h4tFh_S9cs0saZ4FgOl5V33atziR9J22JoUve_DZpWQmMyRFQZhmA8s_YCm_hsrL35XntyocQ6JBV4qb2dxz1jZm9wg3QgjdiJvBAZlvjnRjTUxvoDkGPHWT0dzJD5rCVl9Wbqn4B62W0e9cBIzUlpLEMGtQKOb-hLeXr5mBH81KSnf1vCsVdCQwWvBmkC34dVqFRgmyrMKEkg-5qdEXEHAhaUTMuGqE-C1qqrbiQDrDUzBgJBhWhpYTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c85fa8037.mp4?token=qP4AdMDS1zBCJEU78SEwD2Eu0lXSveK51KS1wLjXLdSayRoqLOxxNFd-qZvV_uVrS3go-C2IpPZ13v3GjtJVDk_ci0ed6R5h9uO6M22gLp-GXO09liBF1CoF-_zeQNlLlaPTBL1PlQGNYDwYHBw174LfJBo09QqwKuLgotojnStkwoWCD2z8eN6w1DjLY2bY8szHGQOR_ff9H81m3JKZhGG7OFSQlMfNByJJWHCR6Q4_el5M4LWBJttiZhBN4zpcHXVRIactRICfav9TI0Li3-LL-zF5gG-MEWp6UhxNJJVYz8GPNuMbFT0j9t4zbf8FpykkuKO8jZZsNxO6v9g4miFcdNLZoHnpza1c-QRcQASKhFmLV95GL5-BY96unUQiZ91Ey19BO3AywL_JiA1I-3-p2OlpRFkuigO062AkCMKM9AsF--h4tFh_S9cs0saZ4FgOl5V33atziR9J22JoUve_DZpWQmMyRFQZhmA8s_YCm_hsrL35XntyocQ6JBV4qb2dxz1jZm9wg3QgjdiJvBAZlvjnRjTUxvoDkGPHWT0dzJD5rCVl9Wbqn4B62W0e9cBIzUlpLEMGtQKOb-hLeXr5mBH81KSnf1vCsVdCQwWvBmkC34dVqFRgmyrMKEkg-5qdEXEHAhaUTMuGqE-C1qqrbiQDrDUzBgJBhWhpYTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت نوزاد گمشده پس از ۳۴ سال جدایی
🔹
کایل آدلر، آمریکایی اهل شیلی، زمانیکه یک نوزاد بود ربوده شد، پس از ۳۶ سال با مادر واقعی‌اش دوباره دیدار کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/654485" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654484">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI8EN0_osPpSIKKLSW3GsT3s50Cx4UszomgR60-6Hyb2CVl9KTekAWlYxeK14hc6dCWVgciAQTm3tIGtRMxKhVc22z7khHjkQrZyKR-XwHHK17qa5KUMUg3t0ImGaH61r_Z-jqfTl0K_EKVjO2LXu4Ekw2YrzQGsfGu4txK3xKHsYuEgv-tYx8dO1vrkvgFefx3XbxHbO57hWQiaRFGJ3Oa1zgOL9vCgz0vRM8YDOx02h1R8HHqroGGMwZa6wjeNCaG8Ydyt4KAEPS_zapL5jAor64YAxFZUbv6TIuae4E-aQoceRoBmnYGcEnpTHQ614j4hFpgyBLUuNeN80IIRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ عاملی که سلامت قلب انسان‌ را به خطر می‌اندازد
#سلامتی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/654484" target="_blank">📅 16:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654483">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCwQ_rSJElzOhjf2qed-UQj1_Zo9RYXbl2qt47_bP7svfSM-uQdi_BULKbp1cVGWxlqZsnpNIqesqt4D61_BK9oDYVvEyh1vHMxiYm6yryE4KjknV-L3HMpF_zwG_7PpBCbIRjhBJmbaCLL2HAvG6jGUpxWzcK4jbFoWUgRqxhkXXjDKgnS3vjpttfqZw_CriJ6tcHLPp-fzrsPEPbK7VzMBGfq7FpsfWyLht0QhgXoI8_BbUGcCmQjX6y5E1tRafwblWoTtLNwtiICTrqjaL_4QoGSznkwo4np78K9PHxEJLZk1t73OWfFJKJS8gyIlSG-dk87pJSrWkFnoyKKvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
فرصت ویژه خرید از چرم مَنطِ
تا %70 تخفیف
➕
%10 بیشتر
و هدیه 1,000,000 تومانی اسنپ‌پی
برای خرید «حضوری و آنلاین»
کد: PAYSS9R
حداقل خرید ۴ میلیون تومان
مشاهده محصولات
👉
manteofficial.com
@manteofficial</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/654483" target="_blank">📅 16:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654482">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hk4HaLICCCEp49pob2LHRm1QLj1COsTylV5uOJui3ttN0T3Os4BFiV-K8_dT71xUN9S4pOrW8Z-7REhmwAMNfebVpWowwXuZHOg6c8_8J96XfyIapI9FPEMdKNuJ4DwAgV8r6Ll0PTfLcbG-trz5g--F615fagrjBMxDj9JpkRBlWz95q32oX2udLBNJ3HvNS6tnTP94rHdr3xenSU7qwDWdbDm61dSVwZkIGngSBPobfUgVp7DC6lYC-3LJJPkyu0RW6ZCgQFDL3dl7YhFz3LBJoc169goxIHP42TtBcOmYT2dg-Boml0fTMbe6jVpucng6hC9-X84Cu30c9SUvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ قصد دارد چهره‌ خود را بر روی دلار حک کند
واشنگتن پست:
🔹
مقامات دولت ترامپ دفتر مسئول چاپ پول کشور را تحت فشار قرار داده‌اند تا یک اسکناس ۲۵۰ دلاری با تصویر رئیس‌جمهور طراحی کند، که به گفته آنها، اولین حضور تصویر یک فرد زنده بر روی پول رایج ایالات متحده در بیش از ۱۵۰ سال گذشته خواهد بود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/654482" target="_blank">📅 16:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654480">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
فرار گوسفند قربانی روی پشت‌بام ساختمان در الجزایر!
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/654480" target="_blank">📅 16:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a04ecddcd.mp4?token=qbmZhSMFNiaAFMuRczY0fEIM-QngctjP2-WniayOnwSRicaeJ-3gEi4erPAz6ZOo48xWDO5wZe5Lt_ZMe3oqdVpnA53vQgxzqNpZ5PgTzFAD8K5bi_oe1eELq2VrM_e8Zh5L8Q4U2P35BlzeAi-c4ZAel5ieHvTCc9zX8mmgehPVNeEVtpbOARpER7OIHV-tQbiUvRTmphRDCo2GERzV1OJkLSw_HnYI8oLHC5zzBVFgWYbrxca91sthDPLLyTZz6NuTFovNi6-KlhAGviMoHgYaRdItnyf6apeOA0x1se_FbFLGKA_DEpAtCcMU-RnRRRO_wcEOvUFUs3bQYE63Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a04ecddcd.mp4?token=qbmZhSMFNiaAFMuRczY0fEIM-QngctjP2-WniayOnwSRicaeJ-3gEi4erPAz6ZOo48xWDO5wZe5Lt_ZMe3oqdVpnA53vQgxzqNpZ5PgTzFAD8K5bi_oe1eELq2VrM_e8Zh5L8Q4U2P35BlzeAi-c4ZAel5ieHvTCc9zX8mmgehPVNeEVtpbOARpER7OIHV-tQbiUvRTmphRDCo2GERzV1OJkLSw_HnYI8oLHC5zzBVFgWYbrxca91sthDPLLyTZz6NuTFovNi6-KlhAGviMoHgYaRdItnyf6apeOA0x1se_FbFLGKA_DEpAtCcMU-RnRRRO_wcEOvUFUs3bQYE63Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از فرماندهان مقاومت عراق ترور شد
🔹
جنبش انصارالله الاوفیاء شهادت فرمانده «عدی الحلفی» را در پی انفجار بمبی که خودروی حامل او را در استان میسان هدف قرار داده بود، اعلام کرد و رژیم صهیونیستی و ایالات متحده را مسئول این حمله دانست.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/654478" target="_blank">📅 15:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
وزیر خارجه پاکستان به آمریکا می‌رود
🔹
طبق اعلام منابع پاکستانی، اسحاق دار، وزیرخارجه پاکستان، در تاریخ ۲۹ مه (۸ خرداد) در واشنگتن با روبیو دیدار خواهد کرد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/654477" target="_blank">📅 15:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcCUGdqEKumrPWqZcG6Xwz1FIbdvOKr4XeMYVWXC-stMvz3ooyFB1ROhSfa2BpPXtfVRBb6JX2Dytvsr3qJARMY5gvu1wTMQaTe53wvN1u9rSnbd5ArTciDl6cvKY0I7-_GR1qjBirPEIZ3-j2MXP_CcPodX1aGrGpft1y5O4yUpS_BA5r2fBGQQIp8Z4x1gwYqVr_h0u_fGA14-rijqeV2fsfdYowT6GKzp9A8KUTT1BJx3F6wC336gAWlPJioEPUrMNGS-Beod72EmdasyyHZ05tv4IqfCNjynbVVDFf15F5LZrD8qxsm6_cUWcdBQKhSL2Bj9aDO8ZX-6P-EUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلعه بابک، آذربایجان شرقی
🇮🇷
#ایران_زیبا
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/654476" target="_blank">📅 15:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6fDH1QQ7ATvcZrSul11cD7QccuNUWAl_4XZEAWA7EtWWlHd2zoW3P9mOmj35yZtlm8nodCWIfAyth61x6RpFlqEfGhNHNXjGH-fz5rDLMqZYCe6tkUmqhSWPJfIA9h688ZQJRhCP__-P7g7l9rCn3YmmLz7mv8K4fcxcOQiZxM36xvMTLaTocpA-g0j2XZ0GdbbOdbYExwUPScaEqgskNIM7wYpfmcUDp9sTqR1XKKPkJDljbVyCvBNtrYJE6S59b9OzpGqH07FVdMz0ZAraXPetdIWNzHH2wY5HibHw2ELix3ZXXl4fKInDqU56mP71Ki9t_qvjA-tK8yPlMMBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام به سربازان خود در خصوص استفاده از مرورگر کروم هشدار می‌دهد
رویترز:
🔹
فرماندهی مرکزی ایالات متحده در نامه‌ای به تاریخ ۱۴ آوریل تأیید کرد که نیروهای آمریکایی در مناطق جنگی، به ویژه در منطقه خلیج فارس، هدف حملاتی با استفاده از داده‌های تجاری GPS قرار گرفته‌اند.
🔹
قانون‌گذاران هشدار دادند که این داده‌ها می‌تواند برای هدف قرار دادن نیروها با موشک و پهپاد مورد سوءاستفاده قرار گیرد و از پنتاگون خواستند اقدامات حفاظتی مانند غیرفعال کردن شناسه‌های تبلیغاتی و اجتناب از استفاده از مرورگر کروم را انجام دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/654475" target="_blank">📅 15:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR1SfmRXt2l6NdsI_1xRQu7ksyRY-vwAXp9tLOA-Lyxgrzj0aJS5jkPC1AacrhzuUTrPluqq4pPMd95QQz07WpR6VjCtw8IWWP312R6IOygmumdB1NaSBCTDFSzT7tXrPDVxb7tVWVSBRBg7Gh1rjJM033FYXrO95YZGf9g9UyjwCkeYIJAJEiq2jHvHO9cbuElAonx3erpXwWoMItR1OdcTAZwX55EK-_pO73zySdce8MxtAw6yjtiR98jIeZwNTtK4bc9XqYRiWgDhA9XDrgztpBTbaQR1bjGdwE7AbGJOjVrevWKsLX-ZUyQK3g0kXg2KBw9y3BclGWgcLgHLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لوگوهای تیم‌های ملی حاضر در جام‌جهانی
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/654474" target="_blank">📅 15:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654473">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMuD0BGMJYCfzD7mIaRxmSobHghlKY4cwTffNZBFMu9Vh-MNrCafjot6UAca3NdSZQgrs-fWeuhKRLhCNfE1dNNz8ibxIP8wxn_2btkO72F7TjPiEfNgrNmy381-Qj0anvTdkwHTPhzAP-nB1YL1FPYSEEoLrdw3mBP4lCVRmCuIDvo8otgpfjPs-ThyvihR1SfH55QIIbbUemrvIcCz3YdmEshabOSuCDmg1wKaipyckDuSmpkZxZsMiQ2yWRisYy58TRbbsWU9rVzQby3_v9tfyi9JLKZcqQ563lIsqnvBxAgfV8w9XO5qPvmwFCgaAMpCNl63ecE5PeU8EZoQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا مدعی نقض آتش‌بس از سوی ایران شد
فرماندهی مرکزی ارتش آمریکا (سنتکام) امروز در بیانیه‌ای درباره درگیری‌های شب گذشته در آب‌های جنوب ایران، مدعی شد:
🔹
در تاریخ ۲۷ مه ساعت ۱۰:۱۷ دقیقه شب به وقت شرقی، ایران یک موشک بالستیک به سمت کویت شلیک کرد که با موفقیت توسط نیروهای کویتی رهگیری شد.
🔹
ارتش متجاوز آمریکا ماجراجویی دیشب خود در آب‌های جنوب ایران را «نقض فاحش آتش‌بس» از سوی ایران خواند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/654473" target="_blank">📅 15:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654472">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
عبور ۲۶ کشتی از تنگۀ هرمز با هماهنگی سپاه  روابط عمومی نیروی دریایی سپاه:
🔹
کنترل هوشمند تنگه هرمز با اقتدار کامل در حال انجام است و طی شبانه روز گذشته ۲۶ فروند کشتی تجاری و نفتکش پس از کسب مجوز با هماهنگی نیروی دریایی سپاه از کریدور ایمن تنگه هرمز عبور کردند.…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/654472" target="_blank">📅 14:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
حمله رژیم صهیونیستی به بیروت
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/654471" target="_blank">📅 14:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654470">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3074d082f3.mp4?token=HtiIcjP6Dcn36g6mLpAcLw3EEuhfbuFq-Rwoz5Eb8kesFcUoSiqQpeJ7FTuhWgi-jkWSLhgR1FkuEzRNYcnx9mmH9EWQjLt3wcTxOtaXCb5CGnDI1LP_CMxOpJI6HvrLrG2-n4eJhulSyJuzVW0cNq2m_bOgPw4_x83kYppAtvLtloUKmrXaMaw86dvD63T4_wQAcCme2JFBymDJ7sSdWfx9DoMDslwR16awS73wj1RKzsptuknmoURjTU-1jh3syT0v5odplVb12S9WV8L_sDxnhnSFg9SesS2zzp0_ZK32JAN5Eseit95XTIwyUEFxm6uRKNMUgnQ56mlK-vB3UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3074d082f3.mp4?token=HtiIcjP6Dcn36g6mLpAcLw3EEuhfbuFq-Rwoz5Eb8kesFcUoSiqQpeJ7FTuhWgi-jkWSLhgR1FkuEzRNYcnx9mmH9EWQjLt3wcTxOtaXCb5CGnDI1LP_CMxOpJI6HvrLrG2-n4eJhulSyJuzVW0cNq2m_bOgPw4_x83kYppAtvLtloUKmrXaMaw86dvD63T4_wQAcCme2JFBymDJ7sSdWfx9DoMDslwR16awS73wj1RKzsptuknmoURjTU-1jh3syT0v5odplVb12S9WV8L_sDxnhnSFg9SesS2zzp0_ZK32JAN5Eseit95XTIwyUEFxm6uRKNMUgnQ56mlK-vB3UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله رژیم صهیونیستی به بیروت
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/654470" target="_blank">📅 14:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654469">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست
🔹
پیگیری‌ها برای مشخص شدن آن ادامه دارد
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد
🔹
اخبار تکمیلی…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/654469" target="_blank">📅 14:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
عبور ۲۶ کشتی از تنگۀ هرمز با هماهنگی سپاه
روابط عمومی نیروی دریایی سپاه:
🔹
کنترل هوشمند تنگه هرمز با اقتدار کامل در حال انجام است و طی شبانه روز گذشته ۲۶ فروند کشتی تجاری و نفتکش پس از کسب مجوز با هماهنگی نیروی دریایی سپاه از کریدور ایمن تنگه هرمز عبور کردند.
🔹
دریافت مجوز و هماهنگی برای تردد در تنگه هرمز یک امر قطعی بوده و همانطور که قبلا اعلام شد عبور از سایر مسیرها به مثابه اخلال شناخته شده و با آنها برخورد می گردد.
🔹
ارتش تروریست امریکایی در منطقه با نقض آتش بس اقدام به پرتاب چند تیر موشک به نواحی خالی  فرودگاه شهر بندرعباس نمود که هیچ گونه خساراتی در بر نداشته است و در پاسخ این تعرض پایگاه امریکایی مبدا تجاوز مورد حمله متقابل قرار گرفت.
🔹
در صورت تکرار این اقدام ارتش تروریستی امریکا با پاسخ  سخت ما روبرو خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/654468" target="_blank">📅 14:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
♦️
رهبر انقلاب: نمایندگان ملّت تمام توان و ظرفیت خود را برای حکمرانیِ هم‌افزا با دولت سایر دستگاه‌ها مصروف کنند
🔹
در این میدانِ جهاد، صندلی نمایندگی، به‌مثابه‌ی سنگرِ خط مقدّمِ تحوّل در مسیر پیشرفت کشور، قلمداد می‌شود؛ لذا شایسته است، نمایندگان ملّت، با اتّکال…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/654467" target="_blank">📅 14:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ety3Q_m8tJSm7AMj8nXYlOz3zhyKO_094iRDerdS0u2Y_47IjnqWS68o5k5LP6Uf6TBY0gmVIUNTEGBInM2qq4z4YzNXbCneMFmdVqEh6Y7ba1mrfrGK5KR-HkjsFhe_bGb9yq5yMlJGxjh-KDMgyHdcEj-YccEmNCC4rSDV-kCG30dCb8M98y0njGysI2azjU8xgP4WftlY-OExFm-CnTqRDGTb4DciwTY_eMzkzsUb7WlYAxfYBhxNvDRP5IH2gNSh0rm3c85noIz_50I4dMaFQU5L-S5_uG0ec95izDp1b5y4-XGtFHJyXwi0rE90RbcwfjvIqj62dRDLOo1rKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور فراری یمن، در ریاض درگذشت
🔹
رئیس‌جمهور پیشین یمن عبدربه منصور هادی که پس از تسلط انصارالله بر پایتخت این کشور به عربستان سعودی گریخته بود، امروز در سن ۸۱ سالگی در ریاض جان داد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/654466" target="_blank">📅 14:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654465">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
قولاً و عملاً، مظهر انسجام و یکپارچگی ملّت باشید
🔹
لازم است تک‌تک جان‌فدایانی که، دلشان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد، از این پس، بیش از پیش، برای پاسداری از وحدت صفوف منسجم و به‌هم‌پیوسته ملّت، اهتمام ورزند و اختلافات غیرموجّه و…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/654465" target="_blank">📅 14:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654464">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌
♦️
رهبر انقلاب: مجلس نقش مهمی در اِعمال اراده‌ی مردم دارد
🔹
مجلس شورای اسلامی عُصاره‌ی ملّت، مُظهر مردمسالاری دینی و رکن قانون و قانون‌گذاری در جمهوری اسلامی است که نقش مهمی در اِعمال اراده‌ی مردم دارد.
🔹
اکنون با سپری شدن سه ماه، از دفاع مقدس سوم، عیار باطنی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/654464" target="_blank">📅 14:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654463">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‎‌
♦️
رهبر انقلاب: از تلاش‌های آقای قالیباف، در راه اعتلای کشور قدردانی می‌کنم
🔹
عید سعید قربان و سالروز افتتاح اولین دوره‌ی مجلس شورای اسلامی را، به همه‌ی ملّت عزیز ایران اسلامی و نمایندگان محترم مجلس شورای اسلامی، تبریک می‌گویم و به این مناسبت، از تلاش‌های…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/654463" target="_blank">📅 14:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654462">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: لازم است، مصوّبات مجلس، با مسائل اصلی کشور و نیاز‌های مردم، نسبتی مستقیم و مشهود داشته باشد
🔹
آیت الله سید مجتبی حسینی خامنه ای در پیامی به مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم : در مقطع…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/654462" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654461">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام_حضرت_آیت‌الله_سیّدمجتبیٰ_خامنه‌ای_رهبر_معظّم_انقلاب_اسلامی.pdf</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/654461" target="_blank">📅 14:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654460">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_حضرت_آیت‌الله_سیّدمجتبیٰ_خامنه‌ای_رهبر_معظّم_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">131.9 KB</div>
</div>
<a href="https://t.me/akhbarefori/654460" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷ خرداد ۱۴۰۵
🔗
https://farsi.khamenei.ir/news-content?id=62984
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/654460" target="_blank">📅 14:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654459">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
آزمون سراسری ۱۴۰۵ و آزمون دانشجو معلمان به طور همزمان برگزار خواهند شد /زمان دقیق برگزاری این آزمون‌ها ۲۰ تا ۳۰ روز قبل از برگزاری اطلاع‌رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/654459" target="_blank">📅 14:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654458">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم منتشر خواهد شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/654458" target="_blank">📅 13:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654457">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5753456ce.mp4?token=XddiU8WWrzzSyGo2IWbpvay-dmE5cGWGbYvqH6BiN_h2XyjCaAkRwh_YxU5uA6LBnl9YqtFgT1aB_dRyiG5R8Q2hdAzfpI_V9N9hHglU-Aq4_EMmBhqAhl-FdPFVsiv5dWEJT2LCAQ4y5OC1dze3pQ0f2MKSyqfPs7teYP1oZFSRB5bWzrvUyvrO503eVJh4rHnKDK0g2j0QaDDAr_4krCq9JGYGukqPFw-pCGdsMjYc2GVpbPOcPtlVl709hgzcnIJ5cTGBTohKK25CvVC-JX67QYNOAG2o7wH0f1WhSJyTC3c7AYeVsjAc-DoU_ZRguOWsMD0ZfaBeINrEgwRKrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5753456ce.mp4?token=XddiU8WWrzzSyGo2IWbpvay-dmE5cGWGbYvqH6BiN_h2XyjCaAkRwh_YxU5uA6LBnl9YqtFgT1aB_dRyiG5R8Q2hdAzfpI_V9N9hHglU-Aq4_EMmBhqAhl-FdPFVsiv5dWEJT2LCAQ4y5OC1dze3pQ0f2MKSyqfPs7teYP1oZFSRB5bWzrvUyvrO503eVJh4rHnKDK0g2j0QaDDAr_4krCq9JGYGukqPFw-pCGdsMjYc2GVpbPOcPtlVl709hgzcnIJ5cTGBTohKK25CvVC-JX67QYNOAG2o7wH0f1WhSJyTC3c7AYeVsjAc-DoU_ZRguOWsMD0ZfaBeINrEgwRKrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی شهرداری تهران: مترو و BRT همچنان رایگان است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/654457" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654456">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سگ زرد شکایت ۱۰ میلیارد دلاری علیه وال‌استریت ژورنال را دوباره ثبت کرد
🔹
دونالد ترامپ پس از رد شدن شکایت قبلی، بار دیگر علیه روزنامه وال‌استریت ژورنال به‌دلیل گزارش مربوط به ارتباطش با جفری اپستین شکایت افترا با مطالبه ۱۰ میلیارد دلار خسارت ثبت کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/654456" target="_blank">📅 13:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654450">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pX31cl19t7i6RVmZivlLe9t1VBPQu0q9EY7ZprYhLgLJJ0IYhzOf9QXhFr6AacmfkKVIND_26YDrT5987lkPaZrAIC9Y28KpuGIR0L4LwPisqOEbgkwTcbH9Qoir_UCDjLvcVieC64Zga6aGbBsj7IiAkEdymwHiF3cWNOYFoS_5WXg1X3NqEAzG5d5p4bNN5uH5g_LHVlDXkciRBweSIf45VTtsX6z2q43o3n0b0DeVTj3vVLnaP0aJkPcwsLXrVRRsvt4Vr-GdDvMMz1G9m8O-N8Kn1_mTBmqjfMzvTZ5K-746B72No0OXeiVyaiejQzImjHcPQaYVStT1SsnPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBFn-XtANa5PFDsISsuQtVDBMR5Dc1VFCW2dSB4_Hm57xdsgLi-h02WErx8WlTZEQguCQ6Vf0FoTNf9vInPIA4skd0REpPx9spvjB38yHk3q_tgpauez7KK3o_040_J9pIlR1E3XPARlaAAzMN0WVBojte9DBpburcYd2z0ovEQ_140L1Yq27c-vVHTDXjrz8d8yEC8RIkNd4oFD00eHvuhFuy_qrNP8oEvq_E_P6SUPpOZO6C-YOYAm1uTQI5CIpf0RzzueToR750j7TkahV52r4_7pYJPMHEBok7tiTY_kvnhRliEE9BMOP4VMOp4UuVfNI60o8IEth8-QZ1RMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0WkabYMXt8EkKSrvo6EHH4hOIDtaFjt7gUg0j3dH7eW5gH81ou3-GNltPdLPCC5I_IPAZ0HOrPEkKttQvJNv-qcQi_4AICDzqy6Epm6zI0tC2QYvG5CrKE8G0_N8PFwbBBlU7wleRS5wlatmnlw8PzkUilWEhIws_SQBlrVqzdg7rkeofgLBLs-jIT2GSXhKbNJMHhSkhd5CIogzbpElhXGo26fJrYwUYwPqsQJraqRdknSUG6qaVXpLfb7pceHWWYa6oJv_JTEBHuIZron9jNPeDzNRCYzeMl8IB53Xf-JdEY9mJsXvR7E3TbMqen_gSXftAek2by2ecLEHDIcAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oi9h2a4nFRaufRXUOyEmRsOCjpP_-5F3LPhD-0pwULCaIhBn-kDGPHal7_5tO_S-G5wcMX2rPdJJr0BYQkRcWsqUWZ6ieDYsDG2DkmwmShArvR81kt_ioL2bznukpTG2R_0VFxH9Vw8dytLhHsUQoMaWJL0ud9jd6Bse1mY0rObMn8JvLEIKIoDD8xaQpp3WBoh8fh1sGEQ8Q-0H3Aw8N1Vidny2XthVypdAaInQPk8w_EjHSxRYZ-CWwcGl0kkytitogvbA6z8o8YReC5DmUJAHl6pIIlTJvZ23DFLYYQAu4FaQ9WWbsOYgkCESkrtRETjfgutB7psakRRWE-tT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unQed0qL2wsugrGC1PfhWY6d1eV59V5X7U3RwuXceC0xTMz7Xlpo1wtswW6fvZFqt4JXTixo1R6Lvbz2KA891hI_kfqP5HiuJNkDAgelSVkYAqwwlJ4sAZxVt8v5yC_ZbYTciwJq824XbTokz55pS7_v1N8YMUtIOuhUGjb1Az37UoxpPs0TMaW4gD-lv-bEcL0dT8afTp9yq9Oyef9xUxx3BFM5GlfUjLPXk-xt6WkLt-OXRCa1zhyIjVbGmygCCxMb74gm9qLwHuPvFxGlhZAvsZOt1aQ9n29kRHQMAwZIAjd-hLmk6FbzKZWQ-6PiQuIpvamgIy620F-V6ErXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zdt2tfszPexLh6sy3MLG5nacxeyNuTKmFkUfVqWKtNZ8uq8JJxMwSyxADo78bK3Beyl9MVQHPOeZCzwoBN8j_g48rXO0fs1UIVhQckWq8geyECkzYbwpUCHxA1Lv5uc9wO1lKzS3YhBQphmCsySUNi8p9twB--OSB6HhMvv-9nYHnTyhNX7XsithWyxEO8dBjOaumNyei9px-VcNbTqe7DLWJPHMhfiOuTG94makU_S6QEldnTwgicO12DQV878MT3sdWKgEopKfADL3fUvg9PcrhrtfBs8Hb_nIFKX69BxD6UF0dsBtFwxh9CFMryQJIU6L6LkfRxy9QGx2lA4apw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش رسانه‌های اسرائیل به توافق احتمال ایران و آمریکا
@Tv_Fori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/654450" target="_blank">📅 13:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654449">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1ticCD19uKoWGu1YgnciKF4tWC0R2fzM_8U0AgCSbgvFGaPPa8IYGj_y6EgvM_F6i8-j5LGX3eMpFCoF854EJwse0yFVKs_nfP4ShKZRZZTibybFn3MyDbPszMtUGH1OZOhRFDGo9luoK1xKd2Ufu4mmPMysJESq0eRVS820gRu06z_OVu4b_5hFXr4h3Zoiualn5T1dJpHQOARyOiX7SnyI7svovCnpxvH9EqiWaf8s1aK6zHulleEWOZRpKcD6l9nJJJSXwXTo3rcX6L5hLbDldAEqMV1lFu6ugQoiVK7wgs37wxHU1Fn7F1mc3108wJ-jvJKraOBp60mYCvKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت خبرنگار شبکه العالم در جنوب لبنان در حمله رژیم صهیونیستی
🔹
شبکه العالم از شهادت «حسام زیدان» خبرنگار سوری الاصل خود در حمله رژیم صهیونیستی به صیدا در جنوب لبنان خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/654449" target="_blank">📅 13:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654448">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/297ec41942.mp4?token=hCyZMxiULX1FMRsUTRxhKdC8Pm4vBjWKtxe0jiyv2JV_hvgyJqAvrp5b03dLDxSvzWhkva4pLyyAYZdQB7oUQD0ySTPYw-yQ5hAlECt35KstGl5T4wJtw5wEk1DgcnKlIwjMKNqikFiDaqwNFKEbDbOa_i44o8heiBvF9953s4Ib3U1smlj1QEgiR1zSZSkDhca4YgrcRmuZ_vvgFFyisykjjohw73XLyzd_WsP8v4qtitLHEHZNSCrtYs9qABmeVnPbFVGZ-5AKMmi9TZmDqpzcRTxzh-xFerlAEjleMGw-i2K_5Y9WjIxC1-0LtLmZ221SKphrTswINnhTxye6Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/297ec41942.mp4?token=hCyZMxiULX1FMRsUTRxhKdC8Pm4vBjWKtxe0jiyv2JV_hvgyJqAvrp5b03dLDxSvzWhkva4pLyyAYZdQB7oUQD0ySTPYw-yQ5hAlECt35KstGl5T4wJtw5wEk1DgcnKlIwjMKNqikFiDaqwNFKEbDbOa_i44o8heiBvF9953s4Ib3U1smlj1QEgiR1zSZSkDhca4YgrcRmuZ_vvgFFyisykjjohw73XLyzd_WsP8v4qtitLHEHZNSCrtYs9qABmeVnPbFVGZ-5AKMmi9TZmDqpzcRTxzh-xFerlAEjleMGw-i2K_5Y9WjIxC1-0LtLmZ221SKphrTswINnhTxye6Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجاوز زمینی مجدد رژیم صهیونیستی به خاک سوریه
🔹
منابع خبری از یورش زمینی مجدد ارتش رژیم صهیونیستی به جنوب سوریه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/654448" target="_blank">📅 13:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654447">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpQCK2cRP7Nb8IWW1sAj0p92OO8P6Ma5vfOIcU3IiO0pwipuXnIQy3w8p2Bwr3j39px3ybRF1BshBjPMLTAWzkdwTQLT31jxpMNKgWJG7ybi36QEG25kSd-PbPjmRdimfFqpAaR81R5b8hjrBAyUoPOi4LillY-YdsKZJJbr63qjUFveX3nubIFCAdwmboYbxgDLh8gyCJMCxjri6N8zY8y4dlACwG2mxC748D6CuMGgcxL7Ntwxa93b9gyR_74y-nSLG975AFzJTiE-17zvpm9iCkjNkrqMvsoe3VvbecJkmln5V7kRUu7vfCSw9cZSj2lMquC_vBT9It-96Mzjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمایی از دماوند از اتوبان قم
🔹
دریاچه حوض سلطان/۱۰۰ کیلومتری تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/654447" target="_blank">📅 12:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654446">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
آزمون سراسری ۱۴۰۵ و آزمون دانشجو معلمان به طور همزمان برگزار خواهند شد /زمان دقیق برگزاری این آزمون‌ها ۲۰ تا ۳۰ روز قبل از برگزاری اطلاع‌رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/654446" target="_blank">📅 12:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654445">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار برای هفته آینده؛ مصرف برق از ۶۰ هزار مگاوات عبور می‌کند
مصطفی رجبی، معاون وزیر نیرو در
#گفتگو
با خبرفوری:
🔹
با روند تدریجی افزایش دما انتظار داریم که در هفته آینده مصرف برق بیش از ۶۰ هزار مگاوات را تجربه کنیم. تا این لحظه تولید برق نیروگاه‌های تجدیدپذیر ۴ برابرِ سال گذشته است.
🔹
در تمام ادوار گذشته و دولت های قبل مجموعا ۱۲۵۰ مگاوات نیروگاه تجدیدپذیر داشتیم و در حال حاضر قریب به ۵ هزار مگاوات نیروگاه تجدیدپذیر در کشور است که رکورد بزرگی است.
🔹
ظرف یک تا دوماه آینده، ۲ هزار مگاوات را در مدار تولید قرار می‌دهیم که عدد بسیار بزرگی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/654445" target="_blank">📅 12:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654443">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgshvsoHRDQ95TpxyqEbxwoyoZqyPsONSudPiYcJMzARrv-Dj_Bpidc5jFtEwZ0cwv2bDequSGmCnrIybvGh3ag25jOkcBSPLnLS6r8EeGYaPm12-_lhlH-U6gUgpNjw-NynPlI0wV3-Mp1hrpxDQ0cVZa71ItYRdQAb37p9W5Vp1u8hNXrVuU8kIlN1vamxDVHWAnLJnRCjv0qihMmv-h0VLzUim95y_CtNmsVeTeMcqjuB-4bXZp0V3-jg20u8MzNLlXcv2JiwuZop4AmbjCmE-jgg4z3GFwPqtM3uXK-63erJpLli8LmvEGr0pfjm6uFfL1znMdJ2Ky_JsoZLpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای نماز خواندن کریستیانو رونالدو
سعد السبیعی، مدیر پیشین حقوقی النصر:
🔹
پیش از بازی آخر مقابل ضمک، رونالدو همراه بازیکنان نماز خواند و سعی کرد حرکات رکوع و سجود را تقلید کند.
🔹
او همواره به اسلام احترام گذاشته و در مراسم هم‌تیمی‌های مسلمانش نیز حضور داشته است.
🔹
همچنین گفته می‌شود گاهی پیش از ضربات، عباراتی شبیه «بسم‌الله» زمزمه می‌کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/654443" target="_blank">📅 12:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654442">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddKF5EwPYf57mIljMKnDoGt7l9mMTmC269UN-MaZHbMaSchaZY2fgMRKWiNdvssG2RXw7Ot9YCXeXZ5sA_TmYCAoEAWaxFGII8xgSHPfUZhEHQSHjaTcQgkguJtOgK8i9kryma1FcU7-2j20pn-pOxBupm2rGrXnniD3EhO5IawyM8JUEXnuauT9uYEgdDxzY5bBALu1JW8NMu_98iGvxhM8MwGDluZrzllJnWYpd3KxzO4XWN-AJaL1Ovn80p2iNmgTlt1qKYAl_fM9N524_8fJX0OXK-Zy9sRq_NqiRDizxim-smnYZ-9aMfQz6m7DHJYX3KGEIJegUMHZh6tYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سواد رسانه‌ای؛ مهارتی که جلوی فریب، شایعه و اخبار جعلی را می‌گیرد
🔹
قبل از انتشار: مکث کن، منبع را چک کن، بعد تصمیم بگیر.
#آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/654442" target="_blank">📅 12:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654441">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cfde2257.mp4?token=Cz6iYbtXMKqJTahUSFOEPf8b14CRnBdvcP_9dQhrssvc8pNqKhkgoKxLY9CKsPh1kNjhEqhyf773MAPDUe4OvbKbKpCHp2KRnhfIVOHctHKOUvQ_H0tgO0kjspxlVxwDk5W324mLp-GG9oelmF8rooffuABUB2DFyJy9Gtggl_zyBCfcPsFbx17lo7c5SuFgW3fWptSCdkyLcNOpXUIRg9TZZD9RyQWDKussgXyH2jsT8BIA1SpnuHKJKgQ6jBgNCbJhJYBa4p2gPjxgjZ7UnVvPuM6d5VLs8FTLAySVMyR9himwDf7NAyCjm9YmqG1-ykkrLhKXeXHBn74cGIr1tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cfde2257.mp4?token=Cz6iYbtXMKqJTahUSFOEPf8b14CRnBdvcP_9dQhrssvc8pNqKhkgoKxLY9CKsPh1kNjhEqhyf773MAPDUe4OvbKbKpCHp2KRnhfIVOHctHKOUvQ_H0tgO0kjspxlVxwDk5W324mLp-GG9oelmF8rooffuABUB2DFyJy9Gtggl_zyBCfcPsFbx17lo7c5SuFgW3fWptSCdkyLcNOpXUIRg9TZZD9RyQWDKussgXyH2jsT8BIA1SpnuHKJKgQ6jBgNCbJhJYBa4p2gPjxgjZ7UnVvPuM6d5VLs8FTLAySVMyR9himwDf7NAyCjm9YmqG1-ykkrLhKXeXHBn74cGIr1tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا فیروزجا، استادبزرگ ایرانی‌ تبار شطرنج فرانسه نابغه‌س. انگار بلیتس بازی می‌کنه!
🔹
پس از تساوی در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی (آرماگدون) و با چند حرکت سریع حریف صاحب‌نام هندی را شکست داد.
🔹
فیروزجا در اسلو با پای شکسته و آتل‌بندی شده به مصاف حریفان رفته!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/654441" target="_blank">📅 11:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654440">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaKO2zac_FfLSQ6KqczxePm-mhUOFZSAN5S5vQmZcR7bP350WB8HZVKInQVsHkvcw21Hbmi0IRovMzgffoCH3pELVvXbRCpEfrevPZ6A_LCHKV3QePk9Hr1S6CmRLCl8pvj5vfMNE6jnYylr_-g2VAZRkz9ITcSu1KyYM0qscXo_GkY9jSkD5PGgg85ECYZWOrYbx5TDAOT5FoQ1POeNaJrABNsiC1KmNs95wbj5PcD703IOm43u3EMt4v3rktW0LCamMcd9yPhwCxEZg0SpITrjiD3h6-8RgbjgQHa9dJOBGZaZi2oIZjBhvzohn5EKpc5sHOkrQ_01TgpnTiq6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا هزار موشک تاماهاوک به ایران شلیک کرده است
🔹
مرکز مطالعات راهبردی و بین‌المللی آمریکا اعلام کرده ارتش آمریکا بیش از هزار موشک تاماهاوک در حملات علیه ایران شلیک کرده و حجم عظیمی از رهگیرهای پاتریوت و سامانه‌های تاد را در این جنگ  مصرف کرده است.  روند فعلی تولید، بازگرداندن ذخایر به سطح پیش از جنگ احتمالاً تا سال ۲۰۳۰ زمان خواهد برد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/654440" target="_blank">📅 11:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654439">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
طبق ابلاغیه جدید آموزش‌وپرورش، تمام امتحانات غیرحضوری دانش‌آموزان باید فقط در سامانه «شاد» برگزار شود و استفاده از پلتفرم‌های دیگر ممنوع است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/654439" target="_blank">📅 11:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654438">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxyWoP8sIuU6ov3qbKyZRhLaCVStG82Ve8aAirJtD7Am_a_zGuu4gNw8S8yGw_R5Uqs0SAwBFcI-f4on_iVVbFbfZduvOCskX0q46FNDhDqg_p-9PrRV2OXcz3KgS9Pd-e1wyUuAnElbm2n2h9iehaLAqCk8BIJQsAK54wL-w8oLEe5nDAH8cijtS67-Y8MQqqte-x1Vfdo_-vAAM_cTe-gJHy-nW1nusiQIGPFCZ1hbtwHrOIhcmvF-uahL9xtYU6iV00nv61gT_YhJ2A9uNo_Bn7X6sZFCJhYmbxUXGBLlhZcJqPir2o5BaVzY0WsGdJK8nZOcze6_T1TeM7wBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست
🔹
پیگیری‌ها برای مشخص شدن آن ادامه دارد
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد
🔹
اخبار تکمیلی…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/654438" target="_blank">📅 11:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654437">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc1e549678.mp4?token=XOxwMtNRpMKkrMW2na-w8ntSbCYXLbTFKm318Qre-QqT8oKZi8BKvc3q5l2n1JrTFkILFbZvH34rUaWPFSMCNtHrAribezV74Ht1rrYTSHBbMvmW7KF4WAHkKcvSU2QVht9TM2-G4D0vERxejNLbs00dovRwuorfRPr9MRToXMgIjuVNQkN_84J_KTNbrNi1baqptFx_7WrevVaKTB_-rPFYtrR56tAs578o-XKffxdSE-nwdZO0b9adHgTJcmND6PrxiPXahhvVWHijoXG8FsJJYU5IWx12aiUyzTaaSX7GIBzCshhGIjLfjFwNSmj2HLLl2xMRHmYxAX4zrS1zvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc1e549678.mp4?token=XOxwMtNRpMKkrMW2na-w8ntSbCYXLbTFKm318Qre-QqT8oKZi8BKvc3q5l2n1JrTFkILFbZvH34rUaWPFSMCNtHrAribezV74Ht1rrYTSHBbMvmW7KF4WAHkKcvSU2QVht9TM2-G4D0vERxejNLbs00dovRwuorfRPr9MRToXMgIjuVNQkN_84J_KTNbrNi1baqptFx_7WrevVaKTB_-rPFYtrR56tAs578o-XKffxdSE-nwdZO0b9adHgTJcmND6PrxiPXahhvVWHijoXG8FsJJYU5IWx12aiUyzTaaSX7GIBzCshhGIjLfjFwNSmj2HLLl2xMRHmYxAX4zrS1zvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
🔹
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیه فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.    روابط عمومی سپاه طی اطلاعیه‌ای:…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/654437" target="_blank">📅 11:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654436">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEua0KcGZlRKGyhtMW-wPp2yLalChniYdWCM1nv7WYKSM7siJR6ECQBMf1_wEhdzv_vl2UWHvaNezwCRxyuyohsNpdSXht4qllKhtV-Ck2l651TpTfTwx_KAqskSk9_JYuWtLq8L_Uh8j18MHRi8RDT3i0221jKZOQ9q4pHma395BczvyFul7aQnJkNRFMgRjhbBCoAXNNAcawMb876-DPYleWBCXR-bc6PQx6EKDh1X3-73w5oGiexetKGwnS1y1JKj1iwFGyFCClJ9u-yZ4SjwJqc-CqfbgaFRcLWHQZ2eY3vDM13_KxuEv152UhAxYKGEuZWJrHzLuX-NniTWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بیشترین عنوان آقای گلی در لیگ‌های معتبر اروپایی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/654436" target="_blank">📅 11:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654435">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsc_0-CFl0Jvn9dS9FQLXGYfpZQHAwA8G7ilycA5tTQmiX5bMUz9z24Kr2EeK1RcvaWIi5OE0o1Xf9zdceco-JrMHBUpwtNsht662_LdUGUNfG_7N-YeR7hK8BFt5842a-NKW_986T8Up92-LAR7powa1gUSQVNAPqtILVRR6_r24yCOPMbTnviN8WQJH22LDZajwFR2UP7nUkliRQyMyFJAhD1wGr1y_Iw3zSOsTxzTAYbJ5Bmdar9UbtSJGp3a2AsSyuts078_jTjohd7fhNRXoN23xZYDC3Djd0wr06lMF2lNfz4-AFA4dnPGxndKPn2-CPN2NUtZ56qEeC8O3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار عجیب معاوضه گوسفند و سیم کارت با خودرو در ایران / مبادله کالا با کالا راه افتاد!
🔹
بازار خودرو ایران حالا وارد فاز عجیب و جدیدی شده است.
🔹
فردی یک سیم کارت ۹۱۲ کد یک را با خودرویی تا ۱.۵ میلیارد تومان برای معاوضه آگهی کرده است.
🔹
از طرفی معاوضه گوسفند با خودرو هم به شدت مشاهده می‌شود و به عنوان نمونه فردی ۱۰ تا ۱۵ گوسفند را برای معاوضه با خودرو گذاشته است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/654435" target="_blank">📅 10:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654434">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUZYnXKs0R9_HeHsw_fxfv4liX0wTjCH-sB7WaE0x-pEahfIH_D7rGYi-7JtIqvs65miUvpAXXHxuFAXZpnCevnmff7XXWe0fGIvusi2P0KGCmkxeI-fFMWhdvLT37U8QuImWfTRHgFs0fNx46in-QKG-I11nIjwobuqL1HdNeX5LN15mJCkCmmrcX8-pV-rJewWB2FPSphmKJsZd8Ued7DyMKIHAx54gLvaDw0O2adpZC6glCTupJjp1x80sZYni1skXjO4ynoIXaxVTN2_dTtZfXE8QDjgoMQUqt5NTvXlcdviJHz_uML8kYgj_GmPBlFKi8hoYQ-ideurvmQEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوتیوب دست به کار شد؛ ویدیوهای ساخته‌شده با هوش مصنوعی لو می‌روند!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/654434" target="_blank">📅 10:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654433">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
سازمان ملل اسرائیل را در فهرست سیاه عاملان خشونت جنسی قرار داد
🔹
سفیر اسرائیل در سازمان ملل در اعتراض به تصمیم این نهاد مبنی بر افزودن این رژیم به فهرست سیاه عاملان خشونت جنسی در درگیری‌ها، گفت که تل‌آویو همکاری‌اش با دفتر دبیرکل سازمان ملل را قطع می‌کند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/654433" target="_blank">📅 10:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654432">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI7y_rrfqWE0vg5YuisLDv1ij5r32Omo2I_2ho2g3que7X5p_XQHWdsCb8rejBxPTdDlQh9Td3gVxF1BtUeHwzC1G9D0maAhYpdHR_rDgFCxDNLjqTzfMgNkSbl_Vz77WQwqrzjeatjdgZLvBEvqPp7hOSVXn1PTYVDFkqecGzd3M2wrdsOPz9ay1BxDML1RVL-qY4E53Bs0Tq634hyhBR3aH6vg3_nAvV_zyvEmxbIhJxp9hhlclLyC-z1B8yoKMT07Fsc303Rut-NsGAvAVwCQRcIHwiIoc-D3-GN3h46pw3qhaGSvqedWY8lvvC62UcE_HLlgXHzqQGQ0N0mgYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه‌ فروش نفت ایران با وجود محاصره دریایی
وال استریت ژورنال:
🔹
انتقال کشتی به کشتی نفت ایران وسط دریا، قدرت کلیدی این کشور را نشان می‌دهد و آشکار می‌کند که چرا ایران توانسته است برای مدت طولانی در برابر فشار آمریکا مقاومت کند.
🔹
طبق گزارش کمیسیون بررسی اقتصادی و امنیتی آمریکا و چین، تهران سال گذشته حدود ۳۱ میلیارد دلار درآمد نفتی از چین به دست آورده است.
🔹
دولت چین اخیراً به شرکت‌های داخلی دستور داد که از تحریم‌های آمریکا علیه پنج پالایشگاه چینی پیروی نکنند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/654432" target="_blank">📅 10:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654431">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N68BAZAF5amVwNgDB11PW8gyWsqqGIfVPGt2bPFPNv2q5qyk6G1dlHf6MwkA5cOlz4RzuNsPDl0eCQA1HYMElJbGlq23wdcO3m8Z-JIlvGqq1QSZ65MjfH8XYF0NI_2O_ume4dR2m_lJTgXualvQJu0opS-8hq4PAZxg-IxjTjMPIz1l_tJb4phNN162hoMFtvb__kIcQLTZGKDMkC2WDIeIr4ZFT8Qz2Sk8XGTKwA7p3oiyjLsj9BSPEfS0AiuCPuNRog8WP57Ngw1U7LY9Q9D0EFjwQS0OmdF9X0NH2GhxhEo2oAnGVBSi_FE2z7Mys0aC265YIvf4QN7xcYTyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش فوری ویلا جنگلی در نوشهر (ریاست‌جمهوری)
-برای قیمت و اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat
🏕️
ویلا مدرن لاکچری
داخل شهرک معروف
🔥
✅
متراژ زمین ۱۰۰۰متر
✅
متراژ بنا ۶۵۰ متر
✅
۵خوابه (مستر)
✅
استخر چهارفصل،آسانسور،روف گاردن
✅
معاوضه با خودرو ،طلا،دلار و...
✅️
دارای سند تکبرگ
✅️
⭐
اقساط بدون بهره
⭐
-برای قیمت و اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/654431" target="_blank">📅 10:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654430">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmXm9JlvDf3-swL9xGusRY9hCn-KbJT0O-rIF1xfbXI36sTHz8YjwnNrF_CVBzN0p60jLG0J0u3y6WHbk-3ZX1dCND1zqeUagWNJcONi12vXsFxu-D1hoW3Z-zF8NJghC0eMiEsKEWRfq2Rcd_3N7QGnlI1jUDJw1TbKhhW04Xbi7_eZcBC8k-exRl1bmqcj2DvCVbUo2GHaQnbpbHaYNWDtSOEKlTntHHlZG1uk7r0nAh1VJjTs_pYVGD8bSdbbV9YGzjJsCsAbk5BgNCEe1cx5LV3JPrzSfU6C3CWbJPyqh4f7R0PQcIPlOkv7M0bI2iWZhs99efcHYY05vzloVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطر برق‌گرفتگی هنگام راه‌اندازی کولرها را جدی بگیرید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/654430" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654429">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a399e7aa.mp4?token=Prlqu60Dkj-dMl0kIEbXUAlNA9fQ3H3kSuMR0w0Rc9I69JG31cSXQeY129Wq0rNRdDpxkTwDzK1fEyk_4IAsILJzFquFoh9XA3xXbQy-SxEZ9qm9X82cVL11VEpxYjIkBAdePcsofV_1XJyayEncrNlRcaXAiuNJCsidtyCthzQjQpzFYxgKERyFZsXEW4WyZHWBUlYQ-q43OMGL92Zk56wP8T-NpVC1xJ886j6Nu3CshRXQxgpHDwjXB6iAqf4AoBCks3biSLSMuSPK2p9Pv3xj86w_aMBr_q-EEiJyDT-MVZAypq99daB3kKEft8d5ohf2v4ajPg688QOijYvQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a399e7aa.mp4?token=Prlqu60Dkj-dMl0kIEbXUAlNA9fQ3H3kSuMR0w0Rc9I69JG31cSXQeY129Wq0rNRdDpxkTwDzK1fEyk_4IAsILJzFquFoh9XA3xXbQy-SxEZ9qm9X82cVL11VEpxYjIkBAdePcsofV_1XJyayEncrNlRcaXAiuNJCsidtyCthzQjQpzFYxgKERyFZsXEW4WyZHWBUlYQ-q43OMGL92Zk56wP8T-NpVC1xJ886j6Nu3CshRXQxgpHDwjXB6iAqf4AoBCks3biSLSMuSPK2p9Pv3xj86w_aMBr_q-EEiJyDT-MVZAypq99daB3kKEft8d5ohf2v4ajPg688QOijYvQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روپایی زدن زیدان با توپ تنیس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/654429" target="_blank">📅 10:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654428">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379afc78bc.mp4?token=DYHxj_BBgaI1q4vEfVDtnYlzCFwBkgA5uCUqpp5R7eok3PzwEJhdTQ0jjU4cSNLigRJyprp3E0KbGU38ISpxryGGPWbeS1XUmskvJ9KEZKQhCRDmAVCR6gtqz-fwFyGdqcKU3u7hyIzhdFyJhudh3JsK3Ct41LX5LaUdq3KGpcddhtRnmU2lidX_izSAjvZqDRZj-0liVFRyk911zm3SsG_RQxqY8C3MDMJQxMxxqp2ceN3Qf7WrsT9uUXu949ZMIO3GhMsqKqGgUQzEG4IH-DfkOvSV9Ao8KCkSj_VywC3eXu4XtmPeYhzG5w-X-PR8Z4O23UKdx4cWc7377L_loQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379afc78bc.mp4?token=DYHxj_BBgaI1q4vEfVDtnYlzCFwBkgA5uCUqpp5R7eok3PzwEJhdTQ0jjU4cSNLigRJyprp3E0KbGU38ISpxryGGPWbeS1XUmskvJ9KEZKQhCRDmAVCR6gtqz-fwFyGdqcKU3u7hyIzhdFyJhudh3JsK3Ct41LX5LaUdq3KGpcddhtRnmU2lidX_izSAjvZqDRZj-0liVFRyk911zm3SsG_RQxqY8C3MDMJQxMxxqp2ceN3Qf7WrsT9uUXu949ZMIO3GhMsqKqGgUQzEG4IH-DfkOvSV9Ao8KCkSj_VywC3eXu4XtmPeYhzG5w-X-PR8Z4O23UKdx4cWc7377L_loQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک دسر خوشمزه و مقوی برای بعد افطار که می‌تونه کلی انرژی بهتون بده  مواد لازم:
🔹
موز ۳-۲ عدد
🔹
شیر حدود ۱ لیوان
🔹
کنجد و پودر نارگیل
🔹
بستنی وانیلی و انبه ۲ عدد
🔹
خامه صبحانه ½ پاکت
🔹
پسته، بادوم، گردو
🔹
عسل ۲ ق م
🔹
خرما بدون هسته ۶ عدد #آشپزی @AkhbareFori…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/654428" target="_blank">📅 09:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654425">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ig0W2Y04o7etzVqc-zGoSDbCDcOtc6NPn2KJhyTBPIPxUFDwC3VVrflI5JX_aEnEhBuSI8Phi34F-l9roJsHM8ioySHC3se4mmkZekgrhHxU52OI3nC5nDjnvdq8c_TfvKTZuz9JS34e0VnXMS6zSWdJ1HwcABkpeUrkmmbnxSB_t2ViX0g7D5sCS-xuH8nWsWEq2_cfNOnq8Har0W6zTQcJwvXm7C6vQVIbWqwDSklJWpLCvH-N45wrW0iKpgqV7uslP1ydRK7hSS_62pUg-2HxQO0g4LtgvzZXNSSikB9NZOI4x42yA0hez4XWqPE7iN-gS03AikTdhT3G8_NY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-KF2lG-L1SGH3AJJ58KARiwzzPXlj4X9m2j_Bm72UsLEifloY6YpSYZ7ba7jROsC_omZiZio2wMxIXqTBYsElljox7QDVbpykwWjRTB0_1lCGtH2aQRwpflnYhECtfmOP9D1I4IBd0IWVE_ZwB-hs5IfddEeHqvZceFPCchkMYFxT-qzrXs8uEwc74-QfoWstxCn9xBeSSOFFQQ29FHCjT0gynLwAxCYiG9-IDiOq-itOUP1NJRAIidZlJpHHOym3gx9n4_cGpVXw_a0QhcDcQ1GjyoBIMVuXIlVKrkOPQU6kzXQtuXYszBZPD8tk89RIAdnMR4_KDDxl0ciMVx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/car9ZYe0IVscsTsWIFt1AcT8z6CYeCFClBQsCdgUDwA6yYt7bUNCwbkTFYybxGxD8mw-nXKUyvLgj-ATQZeK2fTM_lbJ9E32jpWOIgg-OSi7MZSoTv3fkRn_Bv5zdUwQItXfslW30J4TV-WuDx7Z1s3Jol5ZfqlPNEFz_5oHU4bpSc2rbuWo09zlaBkM6laZ9oHS_A5Z1QdYl5u9vvnEM0Q5Gk5sh4sAi7Fa2DTh2Of3C9GjpznQeN1K5dLq2JWIYeiINae1Y2-zJwOHPizEDm94KYDSajL7HXW2ehlnKlNLTVNqwkq0F6XSxCA0GCOXAQYZ-wKk-tC9I-l_0itw4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اینستاگرام پلاس از راه رسید؛ قابلیت‌های ویژه با پرداخت ۳.۹۹ دلار در ماه
🔹
متا نسخه‌های پولی «پلاس» برای اینستاگرام، فیسبوک و واتس‌اپ را معرفی کرد.
🔹
این اشتراک‌ها با امکاناتی مثل آمار بیشتر، تم و شخصی‌سازی عرضه می‌شوند. قیمت اینستاگرام و فیسبوک پلاس ماهانه ۳.۹۹ دلار و واتس‌اپ پلاس ۲.۹۹ دلار است. همچنین متا روی اشتراک‌های جدید برای Meta AI هم کار می‌کند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/654425" target="_blank">📅 09:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654424">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa3af3e65.mp4?token=JPU6PcChoMcPQTp6pcRW9EORknTorCaZW02Y6vic9Hmai8kq5LbvwNV-4rj-6mrnbUNX2hYrBdR5ZThH7AQkQZNfCJgQxbdQJjofoImNAK0UJYyzoMBfej0_WlP3go2pkwRRktUqSWw0oWxYpC6G25fR2mRraUU5xZdZqfIZBCoXtv-1Iu8PFmzciE9sv-b3_o0ubYyRshSmz-GUIdf_62gUyEt1_XRaWHWmyDXS0Ld7lhrnF04m3N25cGwDeZdBPzOuQ0r7DcGIxxwBBujrO7knQFdPXyvPe0InNaZJ1AQWFmlpa7SreqnnfFRZIZz2keQWTTvQd8zwzLfE5XobzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa3af3e65.mp4?token=JPU6PcChoMcPQTp6pcRW9EORknTorCaZW02Y6vic9Hmai8kq5LbvwNV-4rj-6mrnbUNX2hYrBdR5ZThH7AQkQZNfCJgQxbdQJjofoImNAK0UJYyzoMBfej0_WlP3go2pkwRRktUqSWw0oWxYpC6G25fR2mRraUU5xZdZqfIZBCoXtv-1Iu8PFmzciE9sv-b3_o0ubYyRshSmz-GUIdf_62gUyEt1_XRaWHWmyDXS0Ld7lhrnF04m3N25cGwDeZdBPzOuQ0r7DcGIxxwBBujrO7knQFdPXyvPe0InNaZJ1AQWFmlpa7SreqnnfFRZIZz2keQWTTvQd8zwzLfE5XobzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون - وضعیت تنگه هرمز
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/654424" target="_blank">📅 09:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654423">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb4864206.mp4?token=v5uH5nzQltU-weaL19mpG4943gQGhVNbWCsJBXH-y2CjYM3ogzuTYBzE73AaijTNT0bmypTq3GytnvByPDmyN67dgKb93Qc-cMdp_7-3Yx3M1wItUhfiSakqS9VNjm1BrQDuWFlZum6E3U1HM1nJCMhA81lfvLk2ygwvSRcmzukXh7r0LpmMwxW0XH4gd_W9incgqgFNEbf-Smb-Qq8XOJ31WEV7RkICLHEEREBVVXy8GPtWFGv4pDOdW8kiodvrtF1JM65ri3NshGtIqArpzcrriUNVM_eh-DiyCrFmJbd0hJnzsiqEQRRk507a3zgcDFVM-KwtA4uHnONMcHOC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb4864206.mp4?token=v5uH5nzQltU-weaL19mpG4943gQGhVNbWCsJBXH-y2CjYM3ogzuTYBzE73AaijTNT0bmypTq3GytnvByPDmyN67dgKb93Qc-cMdp_7-3Yx3M1wItUhfiSakqS9VNjm1BrQDuWFlZum6E3U1HM1nJCMhA81lfvLk2ygwvSRcmzukXh7r0LpmMwxW0XH4gd_W9incgqgFNEbf-Smb-Qq8XOJ31WEV7RkICLHEEREBVVXy8GPtWFGv4pDOdW8kiodvrtF1JM65ri3NshGtIqArpzcrriUNVM_eh-DiyCrFmJbd0hJnzsiqEQRRk507a3zgcDFVM-KwtA4uHnONMcHOC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جیل بایدن درباره آخرین مناظره جو بایدن با ترامپ: فکر کردم همسرم حین مناظره سکته کرد
🔹
جیل بایدن، بانوی اول سابق آمریکا درباره آخرین مناظره جو بایدن با دونالد ترامپ در انتخابات ۲۰۲۴ گفت که تا سر حد مرگ ترسید و فکر می‌کرد که شوهرش دچار سکته مغزی شده بود.
🔹
من ترسیده بودم، چون هرگز جو را قبل یا بعد از آن اینطور ندیده بودم. هرگز.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/654423" target="_blank">📅 09:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654422">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnSUXXAM4tDYOOKe3wo0zhvGEIcgdkAzNhnzhEXHBxqj4VsmKn9x6YlfmkoW4e3fbS7ziaU04vW8w8Up6cdKtQWOf__l_moFVH-OEdXgWpzHIs3C5qpYYmzDTxAhmb-QtOsskDrReilmDZZpdZ0-y23FUInGZrpNHhhNCV7p23wqVb2XCFNz5FQ4fvWzzRQsHyAmTuJOqP4sVVVGpEH_isDEoVMoMCXnAyM-EnkJBgb37RGzFLFO4s3lnQkOuEk7zQ9_6PyygAW7m3gAfvz49NgB-6ZcVAH3-iWAHlHu0O8sYc61saYf3LRJHOLLyFzpIcGoDw2EXvuNiWkYXAyr2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باقری: دارایی های ایران باید بدون قید و شرط آزاد شود
معاون دبیر شورای عالی امنیت ملی ایران:
🔹
به دنبال آزادسازی تمام دارایی‎های مسدودشده ایران توسط آمریکا هستیم و این حق قانونی ملت ایران است.
🔹
دارایی‌های ایران باید تماما و بدون قید و شرط به ایران بازگردانده شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/654422" target="_blank">📅 09:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654420">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تاج: از احتمال دعوت سردار آزمون اطلاعی ندارم
🔹
ما قطعا به مکزیک خواهیم رفت
🔹
قرار بود ما، فیفا، مکزیک و آمریکا این موضوع را با هم اعلام کنیم
🔹
باید ویزای آمریکا قطعا به ما بدهند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/654420" target="_blank">📅 08:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654418">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
تحرکات نظامی نفت را گران کرد
🔹
همزمان با برخی تحرکات نظامی بین ایران و آمریکا در تنگه هرمز، قیمت نفت برنت از مرز ۹۷ دلار گذشت.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/654418" target="_blank">📅 08:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654417">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908fba3964.mp4?token=iUUkgtuJdnTo2SVwmvhnVZYj0OkIzUhzfpMmDlqfERSKYPyHWGdKgtoRZTVoWzXgbs2iXrbJ1lGZsdHLBmZdKxVaQ9a1YXpynrR7dkR7AvxZUdPHSpGgxPqRTd0u9jcCwcR0OvJ1WHCRXlNUiBHguk5EKEDx5hTKWWnhEeheIESrr_dplUjV_V-Y4iUI-Ta1hzKAWHtatadgoZUdCHPDcvR9iiBh66mjSrJzBHv9mWXBIptup2UTX0Ze_NH9dmXvOL4LR5tQ7-hhJFmFp-MHuzSLKfilzwbMRO5maFAQSP_nZQvvG6K64-a1UNiKjIzoyGeizZi4eXq4oUIJh_aw8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908fba3964.mp4?token=iUUkgtuJdnTo2SVwmvhnVZYj0OkIzUhzfpMmDlqfERSKYPyHWGdKgtoRZTVoWzXgbs2iXrbJ1lGZsdHLBmZdKxVaQ9a1YXpynrR7dkR7AvxZUdPHSpGgxPqRTd0u9jcCwcR0OvJ1WHCRXlNUiBHguk5EKEDx5hTKWWnhEeheIESrr_dplUjV_V-Y4iUI-Ta1hzKAWHtatadgoZUdCHPDcvR9iiBh66mjSrJzBHv9mWXBIptup2UTX0Ze_NH9dmXvOL4LR5tQ7-hhJFmFp-MHuzSLKfilzwbMRO5maFAQSP_nZQvvG6K64-a1UNiKjIzoyGeizZi4eXq4oUIJh_aw8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات اصلاحی برای افتادگی شانه
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/654417" target="_blank">📅 08:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654416">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fea9bc79f.mp4?token=N4og7CdeSmGEoNZGkq6kE5qDiANLW25bdgW428FtihCxl7iDZUrxoY7DfOuLuRQAj8lvoFsTPWpkQd_ry6U59vSy6DrGzYMLsD13IzcqYKeQiRepR99vBF_Sq05M7KuppvEfD8MPZIThCSBGLp59m6AS-P8UxSFtD0oahmu3airtAhFukWnFxUFiuWpOgsbndgvwI8Wz3AT5qcLImZvcU66fNFIzFWBLiQF5HThuAEvfRMGIW63cgXpSihCBN2bQMTh_jrOkl8AJ99mBRVIjFENVucXeds8cpnFc9O6mGG8NfT6YPjL3Z4vGRACKYGlPUnW5iV2NTw55OLQtLZn7L10YBlcNcCZxd0h508foOY_7x1m73ykIWpskh4D8eRaBu1BDKPggw3nExamQ5iGUywQqNrauZRWd2HnCWJzZVeuT3zNOpDJGJe3WZVtZCDd0DfGLCJ0fN8AnzAGTmFxT89kXAqvGVqpPCdszmbFZ66OSsgcddHmNQewn55KwngDovKn85JQmd15Ch6pMcLrpYI1J48jPN1449ppdKxe4l-C7jcQ0XMxoP0ZgNd-JX_RuE9hy4PBKAY79wmzqNdsSvt7CHH8ldPiy3XojWaPieMBzLXHHIQh5HJWiav5imHxechlpRpbxrXHUarvq9HGX1gxL2rFvU9yBuqFxHtnpwL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fea9bc79f.mp4?token=N4og7CdeSmGEoNZGkq6kE5qDiANLW25bdgW428FtihCxl7iDZUrxoY7DfOuLuRQAj8lvoFsTPWpkQd_ry6U59vSy6DrGzYMLsD13IzcqYKeQiRepR99vBF_Sq05M7KuppvEfD8MPZIThCSBGLp59m6AS-P8UxSFtD0oahmu3airtAhFukWnFxUFiuWpOgsbndgvwI8Wz3AT5qcLImZvcU66fNFIzFWBLiQF5HThuAEvfRMGIW63cgXpSihCBN2bQMTh_jrOkl8AJ99mBRVIjFENVucXeds8cpnFc9O6mGG8NfT6YPjL3Z4vGRACKYGlPUnW5iV2NTw55OLQtLZn7L10YBlcNcCZxd0h508foOY_7x1m73ykIWpskh4D8eRaBu1BDKPggw3nExamQ5iGUywQqNrauZRWd2HnCWJzZVeuT3zNOpDJGJe3WZVtZCDd0DfGLCJ0fN8AnzAGTmFxT89kXAqvGVqpPCdszmbFZ66OSsgcddHmNQewn55KwngDovKn85JQmd15Ch6pMcLrpYI1J48jPN1449ppdKxe4l-C7jcQ0XMxoP0ZgNd-JX_RuE9hy4PBKAY79wmzqNdsSvt7CHH8ldPiy3XojWaPieMBzLXHHIQh5HJWiav5imHxechlpRpbxrXHUarvq9HGX1gxL2rFvU9yBuqFxHtnpwL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم ملی فرانسه این شکلی بازیکنان دعوت شده‌شون به جام جهانی رو معرفی کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/654416" target="_blank">📅 07:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654415">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2MFUY56ly73v-N1jZv-HhV3864rEuufXt-xFAJkwryEpH7n-n08gB23KdJ1Cflp8Xdn5CQCkESwzXUB36eJ0gvBfXtysVg8OHO0BWTcbXKkWSHEC5_ttCJ-cTWGwJiFm7uEZdCK6Cw5_zp28oazrnFIp8vRjT0wxF1jZPfUb4RMQh7Bdy3P2_vy6Gu8VBV31PTsZTxWNdcIs2JZUuj0isP9YWbar40GG11tk50I3hCscr3-rjvXQqpcfs4VDo0DVtUJt3UE_G2vOi8s9FClTE9M8XbHqNosknqXnCAgKpMIQXVhzSOMm_2aa9w9c26Jk3M1vCQ9Az9oCbYucU-_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهکارهای ساده برای کاهش هزینه‌های برق
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/654415" target="_blank">📅 07:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654413">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
آمریکا تجاوز نظامی به بندرعباس را برعهده گرفت
رویترز به نقل از یک مقام آمریکایی نوشت:
🔹
ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگۀ هرمز محسوب می‌شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/654413" target="_blank">📅 07:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654412">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
🔹
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیه فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.    روابط عمومی سپاه طی اطلاعیه‌ای:…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/654412" target="_blank">📅 07:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654411">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYD_FQrFEjVPwxHngCyWJraU0Yo9i2426YHmSd7iwPyRiVEast3SEnnC7C-_1VnzN6ocky3zl9YvNa2wKF9IDhkvB6Lb6AbXnxIeGVUGfP_h-7Ik5GgRxi3a9KghHyMYLAO5w5a1m8NXpHOPr7h2GxvxQHiUHOFaQoCFBYnJ5C04eqrvTH7FFXyvtz5ChPfBFIR9FMJvSUFyIL9KUTW5IATV8XEKZF6d88oREu6YkpfCNPbZsUdDDY4msWcXkfnGPf8Yzf5DJNj9bzjhrJX-TH87QIM3eFECqZFlIZutI6-vYdET-UuM7LFNAyH15mCJ_bhnSgxYsF9hOoBiZJiBMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحرکات نظامی نفت را گران کرد
🔹
همزمان با برخی تحرکات نظامی بین ایران و آمریکا در تنگه هرمز، قیمت نفت برنت از مرز ۹۷ دلار گذشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/654411" target="_blank">📅 07:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654410">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
بیمه کامل معلمان مدارس غیردولتی اجباری شد
معاون وزیر آموزش‌ و پرورش:
🔹
با پیگیری‌های سه‌ساله در مجلس، مصوب شد که معلمان مدارس غیردولتی باید به‌صورت سی‌ساعته و با بیمۀ کامل در ۱۲ ماه سال تحت‌پوشش قرار بگیرند.
🔹
عدم رعایت این قانون تخلف محسوب می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/654410" target="_blank">📅 07:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654409">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRa0_pN-uAQxMFB6DLG4c6865nrZtPiyZT3HrmoW2FFBnTEal0_SBlkNyW3HQSs-MMZajSOkRk3EcG2Idb9GnGcnu9TRbz0JwhtM_7UD375xrg1Jv85hmpk6SteUi9DpdIfNrosO0fZrQhcUqz7DB2ldmidgFck_J1GPrpsT4X6mTltOLz_Ya5Gf4rBljGNlukt5KLFvQK0aA4-DU0kis1Yflc5-kdMah-ASoYLbPDmfQv6XMHVP_fN9H1a9tjGaNqMBjUA6FVlR5kAb6GmZ8Eww9BGHycNYlGjlNUzjcc75XHP7Or4wYp1Ksrgic-JT6EF3mHt16E-5ZJZPCD9rAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۱۰۰ دلاری قیمت طلا با تنش‌ نظامی بامدادی ایران و آمریکا
🔹
همزمان با تنش نظامی بامدادی در تنگه هرمز و تشدید نگرانی از رشد تورم و تیره شدن چشم انداز نرخ بهره در آمریکا، قیمت جهانی اونس طلا ۱۰۰ دلار کاهش یافت و به مرز ۴۴۰۰ دلار سقوط کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/654409" target="_blank">📅 07:01 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
