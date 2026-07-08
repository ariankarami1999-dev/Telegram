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
<img src="https://cdn4.telesco.pe/file/BCbA99rckAyKz2GUIxK4n71XL3x2mQYFDupAxHeCekMjFIzYziLS5kITo4WSQrRd0aSKY_Y3kr4i-InYzeFCNN-x_mer4qJ1d4_UpcGREWErMNA5-fvghmWC2oKvX0eB0VCeaG7SckV7N_tVi67TvDKaxfXxORHQwpy6E0WxHGdAYSbguh7NKXoLzt5gSXRQHJzHsX0MWAZ-__vEc0Q1JKOlJ9Lg5fBy8NtJnh8KLA8ZltSWHp1NCeWcZ_osCe_dVe4roiB6xSngN7piXZqAXiuU6rs__ILQvjJ8ShjJhcADycnDKp7A2b7pxmy5Ryy63B1jUTXG25h8cq285G7v7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 347K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 21:26:16</div>
<hr>

<div class="tg-post" id="msg-16913">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسرائیل: اسرائیل در حالت آماده‌باش کامل قرار دارد و رئیس ستاد مشترک ارتش، جلساتی را با حضور مقامات ارشد نظامی برگزار کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/withyashar/16913" target="_blank">📅 21:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16912">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کان نیوز
:
بازگشت سوخت رسان های آمریکایی به منطقه آغاز شده است
@withyashar</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/16912" target="_blank">📅 20:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16911">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">@withyashar
فرهنگ سازی</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/16911" target="_blank">📅 20:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16910">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89ffde203.mp4?token=rwmc5MHD2yoF3fw-egIWprV_ODUNFCZwaDbcdZbs6Z9Rw0SwfG-Iaqc3UstWC-YtB0H9iriTdRy6ajOhCoxQAGynABDDWl0ll0r3ayxULF66SvsPDvlOOu7eFwaxdgYSOFQ07UTE5JKtjL2tUvZrRs8tOP3YaSztXGNFv8G9_xgx_M8oimBCJMo9J7XoZxQxEViszOEYhqekGkqWNJV0kzNYIOFqV9mdUtvWcwnEG38UNw_9DCbswOkU86m-_XQtDf08JWiI0EniJ7KKUD_C11QqJmLA9kjq2IeMlp9BKvAiYWKpBY9s6OQPbCW9M5Tei-MxOgaisw9DKBaL6RL-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89ffde203.mp4?token=rwmc5MHD2yoF3fw-egIWprV_ODUNFCZwaDbcdZbs6Z9Rw0SwfG-Iaqc3UstWC-YtB0H9iriTdRy6ajOhCoxQAGynABDDWl0ll0r3ayxULF66SvsPDvlOOu7eFwaxdgYSOFQ07UTE5JKtjL2tUvZrRs8tOP3YaSztXGNFv8G9_xgx_M8oimBCJMo9J7XoZxQxEViszOEYhqekGkqWNJV0kzNYIOFqV9mdUtvWcwnEG38UNw_9DCbswOkU86m-_XQtDf08JWiI0EniJ7KKUD_C11QqJmLA9kjq2IeMlp9BKvAiYWKpBY9s6OQPbCW9M5Tei-MxOgaisw9DKBaL6RL-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خطاب به محمدباقر قالیباف درباره اورانیوم : محمد چی چی محمد چی‌چی آنجا با بیل‌هاست.
بیل‌ها شما را به آنجا نمی‌رسانند. بزرگترین ماشین‌آلات جهان شما را به آنجا نمی‌رسانند
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/16910" target="_blank">📅 20:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16909">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe30e74b8.mp4?token=riOf4BR5Bovc2IHLJFT4moEwew0ZjX7B1nLEme0BA_HQWFwa1Xyqs7GSBx03dRVZh7uTGbc1WdPLPbki0XwibsHAvLWtnaoSHsawH7Rqejp9BZQImS7B7KtP4CXCBCgBIq0A7SDvXI8ChL93NtjnbA7cieXou5OIkXtYypreVcncCOqs6iogl2IdLanojDX0fwg-goSXdChL6z18MNpSaK6_82Tk5sli0uic9lMi6xwLTe2CSzoINhYj17WRP-1w6lpof_BaauI4JX7wTbeY-264k05cl3DgIGQ38PiMbreCvG5K6WojnhTP2Ozh8yfemW9dE3QfCqdmbw6ZegwkhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe30e74b8.mp4?token=riOf4BR5Bovc2IHLJFT4moEwew0ZjX7B1nLEme0BA_HQWFwa1Xyqs7GSBx03dRVZh7uTGbc1WdPLPbki0XwibsHAvLWtnaoSHsawH7Rqejp9BZQImS7B7KtP4CXCBCgBIq0A7SDvXI8ChL93NtjnbA7cieXou5OIkXtYypreVcncCOqs6iogl2IdLanojDX0fwg-goSXdChL6z18MNpSaK6_82Tk5sli0uic9lMi6xwLTe2CSzoINhYj17WRP-1w6lpof_BaauI4JX7wTbeY-264k05cl3DgIGQ38PiMbreCvG5K6WojnhTP2Ozh8yfemW9dE3QfCqdmbw6ZegwkhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد جمهوری اسلامی : هر اتفاقی قرار است بیفتد، بسیار سریع خواهد افتاد. ما به دنبال بلندمدت نیستیم.
@withyashar
ترامپ : من مطمئن نیستم که بخواهم با آنها معامله‌ای انجام دهم.
فقط بیایید کار را به پایان برسانیم</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/16909" target="_blank">📅 20:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16908">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: من شماره یک لیست ترورِ جمهوری اسلامی هستم.
واقعاً برام مهم نیست، دارم کارم رو انجام میدم
فکر نمی‌کنم جنگ ایران دوباره شروع شود
هر اتفاقی قرار است بیفتد، بسیار سریع خواهد افتاد. ما به دنبال بلندمدت نیستیم
@withyashar</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/16908" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16907">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/166026afde.mp4?token=Lyjy27L-VR_AIwQf54Au_Qddhi6fZJaLUqAjTO2ZhLn-WxhlTlDLgR39KPp_EsI64KWO95iL-nWYVKJbWXVKWA0c2EazwTwPEpmKsnSTBQFP4vWFrP1i85e_1MvD9_MPbh_4B7h_YI6MTpzWw1bRGT4XHhWitZdUnU6ypKBCTkqu0BEkjHtcILCOpTrGjnzSfP7L8QsgBmxVda7QHQ6U0XMoAwlDZqoX3sZ9185l6Uh6C8IEAI34V74609uJZlrPT3P6SoSh9NzQJa18wtrDicfGZur9ct_UJCAYWqzGPW62rey__MAeJPdq81vLG_iRdGT52_aM8okoiNkLGci82klhYN1X3rVPO2oSwWniu0dy6IGqYQK-UqY5izriLi322YJXI0w8tfIzASYo4iBEnpJRirNmW-OfPAiFCa6f4DiYyE-bCq_jI_rEzfdsAE-iSEY8vgpQc0ikFDZ5knv02cN99-4lXLZvtmX5ri1NA9NkQMNr-tI1wpacjiGKyrqt2rGmBuv0iPm75znLyBr6B98MYajgBt6anOcBtDj8DvgULyRCYDg04nOd_9hVnDfKXy7NxgahtUzLVhDVXTGnKQQ6MQ2WatC2qzzhsHFkqh0hCnDP128cAmE7qfVXmO858Y_qFDZZ54kjMBQCLYExoFeqeo1OlosP8bVg93GptNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/166026afde.mp4?token=Lyjy27L-VR_AIwQf54Au_Qddhi6fZJaLUqAjTO2ZhLn-WxhlTlDLgR39KPp_EsI64KWO95iL-nWYVKJbWXVKWA0c2EazwTwPEpmKsnSTBQFP4vWFrP1i85e_1MvD9_MPbh_4B7h_YI6MTpzWw1bRGT4XHhWitZdUnU6ypKBCTkqu0BEkjHtcILCOpTrGjnzSfP7L8QsgBmxVda7QHQ6U0XMoAwlDZqoX3sZ9185l6Uh6C8IEAI34V74609uJZlrPT3P6SoSh9NzQJa18wtrDicfGZur9ct_UJCAYWqzGPW62rey__MAeJPdq81vLG_iRdGT52_aM8okoiNkLGci82klhYN1X3rVPO2oSwWniu0dy6IGqYQK-UqY5izriLi322YJXI0w8tfIzASYo4iBEnpJRirNmW-OfPAiFCa6f4DiYyE-bCq_jI_rEzfdsAE-iSEY8vgpQc0ikFDZ5knv02cN99-4lXLZvtmX5ri1NA9NkQMNr-tI1wpacjiGKyrqt2rGmBuv0iPm75znLyBr6B98MYajgBt6anOcBtDj8DvgULyRCYDg04nOd_9hVnDfKXy7NxgahtUzLVhDVXTGnKQQ6MQ2WatC2qzzhsHFkqh0hCnDP128cAmE7qfVXmO858Y_qFDZZ54kjMBQCLYExoFeqeo1OlosP8bVg93GptNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام با انتشار این ویدیو نوشت: امروز، بیش از ۲۰ کشتی جنگی نیروی دریایی ایالات متحده در سراسر آب‌های خاورمیانه گشت‌زنی می‌کنند در حالی که نیروهای سنت‌کام به ترویج امنیت و ثبات منطقه‌ای ادامه می‌دهند.
ماه گذشته، کشتی‌های جنگی دریایی و هواپیماهای ایالات متحده در نزدیکی هم از دریای عرب عبور کردند و قدرت نظامی و آتش بی‌نظیر آمریکایی را به نمایش گذاشتند
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/16907" target="_blank">📅 20:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16906">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638d05d744.mp4?token=EcjUzXXXOSvt3cudTTMp4pvkBVj5e1y3ejH49taK7bUDCF9bfFRr8aBhcHKWQsTzL0ttp0h_wIm7neqdtCt11EG3CPpYGxskXV77lMrG6TXFV_70ywhfzrUBP7rGb3SDEac2TndH-1pikzn09OhCG4ddlAuP-tFBzxeVdn8oxRJczYhKebfJSY1cGvb5ZOqEn9mfLpkzR9WnTAuWGeQzeBF4j37Q1AvcvbcIQlKO38Wi6SnCGRTJQBsu-MMw-R6aJELrMFRLZEjahoDg7JvpL4Bjf_J-SaEv7WpwlmHBtXAOQsTr_fx2AiFD2iqHIqvWYIRn8NS067oKiuJJL94OvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638d05d744.mp4?token=EcjUzXXXOSvt3cudTTMp4pvkBVj5e1y3ejH49taK7bUDCF9bfFRr8aBhcHKWQsTzL0ttp0h_wIm7neqdtCt11EG3CPpYGxskXV77lMrG6TXFV_70ywhfzrUBP7rGb3SDEac2TndH-1pikzn09OhCG4ddlAuP-tFBzxeVdn8oxRJczYhKebfJSY1cGvb5ZOqEn9mfLpkzR9WnTAuWGeQzeBF4j37Q1AvcvbcIQlKO38Wi6SnCGRTJQBsu-MMw-R6aJELrMFRLZEjahoDg7JvpL4Bjf_J-SaEv7WpwlmHBtXAOQsTr_fx2AiFD2iqHIqvWYIRn8NS067oKiuJJL94OvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی سنگین در کرج الان
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/16906" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16905">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr1EDsAxkWJsUiOEdQwISb2Ub7T2TTR-qaIa_4Dw5B6uz4cpNbeWfjevi82Z4YbWYDFdPWUKmjlRgecL7VJqjU8Nj3WCpLXtivQMStyzL5EKOh--WqEafdvR3lFGoBZ36SwwBykCWeO1U2IMBgY_vYAueJmE4-YNAXAcVr2z8r6ktwuJw-JRn3bysrOQ1_jivRlJC-xSjYThTeGZ3xyC_pkwqtB06-9SyOTgvhMhS3NKqWVJmY494bIDSZGh-Ua6ZbgGe4s3WkUiz7XNJbB1REfPciIsITkfb0-8DjRo4zYEujO6syTivsJne3USkJTFZWB953YOTy-AokxzMPiuVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی کرج الان
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/16905" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16904">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ در اختتامیه نشست ناتو در آنکارا:
ایران صدها هواپیما داشت. همه آن‌ها رفته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/16904" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مراسم تشییع علی خامنه‌ای بازهم تاخیر خورد؛ دفتر مکارم شیرازی: با توجه به اینکه استقبال مردم ایران و عراق از مراسم تشییع علی خامنه‌ای خیلی زیاد بوده و ممکنه مراسم خاکسپاری دیرتر انجام بشه، مجلس ختمی که قرار بود 19 تیر برگزار بشه، به شب 25 تیر موکول شد. @withyashar…</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16903" target="_blank">📅 19:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16902">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1wZJTGk3qaxRBROMMfg3XeaEjeJwjldcFvDlbdV711JN1QXV_xCjOI5J71jP32yckSDfMk0jD5wq0qJAYB2coskygk3jBNO2E893BRscKs8kTp5BLvGItsTQncb3KHgDoB9XkE6sINTwuLxmzpZ7c4mzJvjKanHJhKgMY5titxrzn6N3a1PKotbZBsXM5Pj1jeIunzzcODJImJ1uKA-zjeKoTeai34PjIby21z-XJSHc2jjMunjKk72No3KM37T41kXMfJd8zizj5lSbsSxtyLsjoGI9IA1VnHQQW13psC-OJ6X5GXMFT7XMSWe04Wj5SBYLeXXF4SqZ7dRFnf1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام و جاسوسی E3A با رادار آواکس ناتو دوباره در ترکیه بلند شده. این هواپیما طبق الگوی منظم همیشه قبل از اتفاقات مهم برمیخیزد. قبل از ترور قاسم سلیمانی، قبل از جنگ دوازده روزه، قبل از جنگ چهل روزه و حالا دوباره پیدایش شده. معمولاً حدود دوازده…</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16902" target="_blank">📅 19:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16901">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس: حملۀ مجدد آمریکا با تغییر دکترین هسته‌ای پاسخ داده می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16901" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16900">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دقایقی پیش ارتش اعلام کرد : هشت نفر از پرسنل نیروی هوایی و نیروی دریایی در بندرعباس و بوشهر در جریان حملات صبح امروز آمریکا به جنوب ایران، کشته شدند.
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/16900" target="_blank">📅 19:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16899">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مراسم تشییع علی خامنه‌ای بازهم تاخیر خورد؛
دفتر مکارم شیرازی:
با توجه به اینکه استقبال مردم ایران و عراق از مراسم تشییع علی خامنه‌ای خیلی زیاد بوده و ممکنه مراسم خاکسپاری دیرتر انجام بشه، مجلس ختمی که قرار بود 19 تیر برگزار بشه، به شب 25 تیر موکول شد.
@withyashar
🎉</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16899" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16898">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مژده بدیدددددددد
😍
💥
💥
💥</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16898" target="_blank">📅 19:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16897">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتانیاهو: ایران قطعاً دارای تسلیحات شیمیایی است و اگر بتواند، ذره‌ای برای کشتن صدها هزار آمریکایی اهمیت نمی‌دهد. ایران در استفاده از سلاح‌ های کشتارجمعی هیچ ابایی نخواهد داشت!
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16897" target="_blank">📅 19:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16896">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5HO6uYT7fnjsmznvomF_KH8spkAtLV91fsmp5AdpUZiYvQL3HZiYiEgzoAOBQiCdeFrpxyAwyQOjrWb5af3f1JPBWESPhjKQTu9V7kOeJefm_QHlPFTCMa3lD7uk82k1MR7vU-bMYjom1CTNMapz84XJ4kbRHnY8sdwHaBFTZomKeFCEtZWbLOt-RSJWIkJzYr1gY5VA5g8HGY2NIDDAO7W4O61VlYcsaNeD8cW6gqA4Mc47XQ8YleAwsJNd1NQOfrqzaSRus2ot5sZf_ywjA1fpw0Di-4tA3ubEbftOy8xbMp4CPNjUCIC3gXz2vW5rDMEWjP0bEFE7RCz3vF_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ اعلام کرد که هواپیمای موقت ریاست‌جمهوری VC-25B Bridge به پایگاه هوایی نیروی هوایی ملدنهال در بریتانیا ارسال خواهد شد تا به پرسنل نظامی ایالات متحده حاضر در پایگاه اجازه دهد از هواپیما بازدید کنند. از VC-25A برای انتقال ترامپ از اجلاس ناتو در ترکیه به پایگاه هوایی ملدنهال برای استفاده از هواپیمای جدیدتر استفاده خواهد شد.
با این حال، دلیل واقعی این تغییر احتمالاً به امنیت ترامپ مربوط می‌شود. به احتمال زیاد VC-25B Bridge دارای همان قابلیت‌های امنیتی VC-25A نیست، زیرا یک هواپیمای اهدایی قطری است و از ابتدا اصلاح نشده است. احتمالاً VC-25A به دلیل احتیاط در برابر یک حمله ایرانی خریداری شده است.
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/16896" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_Y2p3FsquPulLQTsslakE5QK8y1koMGuNA---9YiNKD6xiUFBuydka9YbNgCO6WLAYElHvSqm0Z1lsLSjPOVd_YZPb2Xa_rawk5zu-WLIYCF78JXs4lNvWHe4wDMahsxkgyoTSX4OkpoLyWITwbxMoKG8ArJxY7im9aX4UAroiYBm9z3apUYeVJK3J3duBBO32E-v5EeAzW-gUgiHhpJtk4sJSdknq3h4VKtg4aKmyJ975c_2b1z0CKeizpyVzNuA6nTA3c8iUGZsBsriM0sqBfE9QpLQ7NQLJ0xexz0WKPbzVYt3FrriFgo6obImDwBrb3k7ssRHgFTVGIO_T5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b98e4f876.mp4?token=fZ4UHwQPA6aeNCVbVF2eP7cXGdQ9mH3qsUr2HC072IZQqgROSYgPpAIS4nfRDZiEalw6FJPCJgI5vlQguRrvKgfHbXEQZmKSF2QcvXeFLpgBdf-wdXI_-cpy85VTlVQwt4MXr9m1NnlWTtQ-QDCcDXAHbqixLNhQDiLPbEdE_ven9ipTPQjB-PPxo0DM8pZndj_taYv4vtIdsxOg2z3cCwzecRrtrWfhbj7C1hT-hovDV1YWoZD5XgGje0EuL9s-aKRiJlNqt2uN48AGOkhrOnzCHqgoHFo4uSvC1I29yYzi8_AKGiGZoo7ifLuzu5sshW1Wx3AEGW-MDu68CxgqAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b98e4f876.mp4?token=fZ4UHwQPA6aeNCVbVF2eP7cXGdQ9mH3qsUr2HC072IZQqgROSYgPpAIS4nfRDZiEalw6FJPCJgI5vlQguRrvKgfHbXEQZmKSF2QcvXeFLpgBdf-wdXI_-cpy85VTlVQwt4MXr9m1NnlWTtQ-QDCcDXAHbqixLNhQDiLPbEdE_ven9ipTPQjB-PPxo0DM8pZndj_taYv4vtIdsxOg2z3cCwzecRrtrWfhbj7C1hT-hovDV1YWoZD5XgGje0EuL9s-aKRiJlNqt2uN48AGOkhrOnzCHqgoHFo4uSvC1I29yYzi8_AKGiGZoo7ifLuzu5sshW1Wx3AEGW-MDu68CxgqAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدونستم یه جا این صحنه رو دیدم.
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/16894" target="_blank">📅 19:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ درباره احتمال اعزام نیروهای زمینی به ایران:
«چرا باید الان وارد عمل شوم؟ زمانی وارد می‌شوم که یا آن‌ها کاملاً از بین رفته باشند یا توافقی حاصل شده باشد.!!»
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/16893" target="_blank">📅 18:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لحظه سقوط هواپیما باری پاکستان @withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/16892" target="_blank">📅 18:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سی‌ان‌ان: تردد نفتکش‌ها در تنگه هرمز عملا متوقف شده است
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/16891" target="_blank">📅 18:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16890">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41cc5c19.mp4?token=RfuqAqX3pya4hqu76F8-DIFMCuWAcNoreFLZ6xeLMAHMP0n33JAxb371tmBUnSJxyzwvXQf5EG88H352LvKPbqB3MVgjIR--NwBlvRGtBQeIdG-9nNxhz_W_nYVJH7h5-I8oZz-weCqowSIDLeySqVeMnWjtx1-qebkZp-MKHvLSUpefTfYS5uhjzjJ6vWhpX1U7wlXXQlnj9A6yAdhL2DPYdQaVjbgyM0f8xNRsnIyc3aj9HGsWD4ICsxERIkTkk0FjMCXAeEDKabNG0jkEy8vBAjUoMPJpl-_tuxW7Qm2jFh4zNyF25JD_9BlU_010kmBfPoL-hzeAe8KO8CizsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41cc5c19.mp4?token=RfuqAqX3pya4hqu76F8-DIFMCuWAcNoreFLZ6xeLMAHMP0n33JAxb371tmBUnSJxyzwvXQf5EG88H352LvKPbqB3MVgjIR--NwBlvRGtBQeIdG-9nNxhz_W_nYVJH7h5-I8oZz-weCqowSIDLeySqVeMnWjtx1-qebkZp-MKHvLSUpefTfYS5uhjzjJ6vWhpX1U7wlXXQlnj9A6yAdhL2DPYdQaVjbgyM0f8xNRsnIyc3aj9HGsWD4ICsxERIkTkk0FjMCXAeEDKabNG0jkEy8vBAjUoMPJpl-_tuxW7Qm2jFh4zNyF25JD_9BlU_010kmBfPoL-hzeAe8KO8CizsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهپاد (پهپاد دريايي) اوكراين به يك نفتكش ناوكان سايه روسيه در درياى سياه حمله كرد
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/16890" target="_blank">📅 18:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16889">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7-rCVBiMtk73f-3AGK-vDFORzf-tqgynn2x2cZqg99HRN10VvpA7huWL1og6cmBMVjaO6tQjf9tdRBbFzbSuuc1oqGcryfwI8MuLgYkEg0v0BeiL6Gv1tcXscqcglG2z0Z-uSDl2WoHSV6K2bRL5qV1XSRom9l-FsxjetXGFiVeXOxtSuQmVvtRKcvYLdk7QIC8E34rcq2CBgjylXtZSt8MW9Uz1xTOLuGbCMjoUvm4BSA702wxzF2QOnxKSRZ1h88GfMu3oshZ3CJJNV8lXfe48u97OC4N7xNjupacGkPyi-3s2fZN-A2eyvao6SKFqTE5Xz_mM8hpq3Yrdyb3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت غیرمعمولی نیروی هوایی آمریکا در‌دریای سیاه مشاهده میشود، به طوری که دو فروند هواپیمای تانکر سوخت‌رسان KC-135R، هواپیماهای ناشناسی را اسکورت می‌کردند که احتمالاً بمب‌افکن باشند. این در حالی بود که دو فروند دیگر از همین مدل، از خلیج سودا به سمت فضای ترکیه پرواز کردند. این مسیر، جنبه غیرمعمولی این حرکت را نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16889" target="_blank">📅 18:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/255dda7e3b.mp4?token=D6sHqXbe-SBb7RcjCcKVvHSmXRZhG48cuda0FE2KnszWt50BIHc0KoUahrdm56Fe8Zi_TeUp2C2BfIGuS7U0Ws5rgjY8QYqXkEpCPbPjo7YOPZyeooBoqS7b3LyWuM8987DPRQncT9ZJ1RpSl29wY6pyXGRNcrSMoFKljQfg_iEd5_mCXqP5M_y3HsY0DPTuUsQol17WQGd_dQWWV0m01if-P6kzUZWnSeMja1EboFELfqwAAmzNf6b5uvS5asygtJgt5jBRXbb5NTOc4hpxM-T2KgfB6aMlTWfziv7biZ5l2BbexODLIY2yURnXMba4k78ynq-3mpRSoNDMRSYhuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/255dda7e3b.mp4?token=D6sHqXbe-SBb7RcjCcKVvHSmXRZhG48cuda0FE2KnszWt50BIHc0KoUahrdm56Fe8Zi_TeUp2C2BfIGuS7U0Ws5rgjY8QYqXkEpCPbPjo7YOPZyeooBoqS7b3LyWuM8987DPRQncT9ZJ1RpSl29wY6pyXGRNcrSMoFKljQfg_iEd5_mCXqP5M_y3HsY0DPTuUsQol17WQGd_dQWWV0m01if-P6kzUZWnSeMja1EboFELfqwAAmzNf6b5uvS5asygtJgt5jBRXbb5NTOc4hpxM-T2KgfB6aMlTWfziv7biZ5l2BbexODLIY2yURnXMba4k78ynq-3mpRSoNDMRSYhuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره اسرائیل:
اگر نخست‌وزیر دیگه ای (بجز بی بی) داشتید، اکنون اسرائیل توسط ایران به تکه‌های کوچک تبدیل شده بود.
و اگر من به عنوان رئیس‌جمهور امریکا نداشتید، اسرائیل امروز کلأ وجود نداشت!
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/16888" target="_blank">📅 18:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f22ec3f9c6.mp4?token=fBjI3ZC-xl5wgAgVwLhGr3kQGTQcnJUU9AW_H37Lo7bZmXjDsmuhwCtiwzayFy-VRxEBeXD3LPVtHCan4v30wQYbXahWTg3Kz3ckC8F0QkMM4XFjAiKXNrbvkxOUkjbs4BkSic5zHaSJXUm88zxP4PGwC0noV5B_THgtOQzSbfFuvFMPS8GNSy-ide7iPsXY1VQZDKjU4nXvGKhB3OdLkFBPklmVeRAbhyBQ31-0k3T7cOZqy47v-ikI8xPuR-HkCOavwc6PPQsGDIU4F_uIItvm-BTC9nU2liJC4ritjXxPWvj4FEw1th02fON0jmdrkP32GCbfXyGb6fufbGSfJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f22ec3f9c6.mp4?token=fBjI3ZC-xl5wgAgVwLhGr3kQGTQcnJUU9AW_H37Lo7bZmXjDsmuhwCtiwzayFy-VRxEBeXD3LPVtHCan4v30wQYbXahWTg3Kz3ckC8F0QkMM4XFjAiKXNrbvkxOUkjbs4BkSic5zHaSJXUm88zxP4PGwC0noV5B_THgtOQzSbfFuvFMPS8GNSy-ide7iPsXY1VQZDKjU4nXvGKhB3OdLkFBPklmVeRAbhyBQ31-0k3T7cOZqy47v-ikI8xPuR-HkCOavwc6PPQsGDIU4F_uIItvm-BTC9nU2liJC4ritjXxPWvj4FEw1th02fON0jmdrkP32GCbfXyGb6fufbGSfJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: مکان‌های مدفون شدن مواد هسته‌ای در زیر کوه‌ها را شناسایی کرده‌ایم @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/16887" target="_blank">📅 18:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: مکان‌های مدفون شدن مواد هسته‌ای در زیر کوه‌ها را شناسایی کرده‌ایم
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/16886" target="_blank">📅 18:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بلومبرگ : ترکیه در صورت لغو ممنوعیت فروش توسط دولت آمریکا به آنکارا، قرار است در یک معامله اولیه، ۶ فروند جنگنده F-35 از ایالات متحده دریافت کند.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16885" target="_blank">📅 17:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16884">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هم اکنون مهرآباد دارن هواپیما هارو خالی میکنن !
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16884" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8669368d.mp4?token=ssZlpyZDLe707nIIDbOY5MCfwekno6X3jeBKCviREhGcbg7LKmDEg06LHG3MTlC85cEdhYHsmHmvxycOc51CDjCuWPrG6b-8aqpLixv9ZRJKFjcXuwJMwIr0PfpNzzRnMMFUX_b9ZyXXURL8zbj4JYEfU9knb_PN1Uzj_K1uAkTCGXjKIw-4Tqdmr0EOOcrBjRO6DaeukzkKZf3ZyNFUQBOWp4jbXdyiY0roy-z5Vegjl2dGKzFjFPkHhj6-BmEn8fwpz38m5P8TTVnDGSHh0zZoD1TT0ziDwguauunXIukUG29x6GLTeXtRyiPg20Zhvovg53wfml_t1i-HCm5tAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8669368d.mp4?token=ssZlpyZDLe707nIIDbOY5MCfwekno6X3jeBKCviREhGcbg7LKmDEg06LHG3MTlC85cEdhYHsmHmvxycOc51CDjCuWPrG6b-8aqpLixv9ZRJKFjcXuwJMwIr0PfpNzzRnMMFUX_b9ZyXXURL8zbj4JYEfU9knb_PN1Uzj_K1uAkTCGXjKIw-4Tqdmr0EOOcrBjRO6DaeukzkKZf3ZyNFUQBOWp4jbXdyiY0roy-z5Vegjl2dGKzFjFPkHhj6-BmEn8fwpz38m5P8TTVnDGSHh0zZoD1TT0ziDwguauunXIukUG29x6GLTeXtRyiPg20Zhvovg53wfml_t1i-HCm5tAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریم به این لحظه نزدیک میشیم. گفتم از الان داشته باشین، سیو کنین، چون اون موقع ممکنه اینترنتتون قطع باشه و نفهمین چی شده. @withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16883" target="_blank">📅 17:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دبیرکل ناتو : تنگه هرمز را باید باز کرد
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16882" target="_blank">📅 17:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: وزیر جنگ هگست، از ایده‌ی ترور مسئولان ایران در مراسم تشییع [آیت‌الله] خامنه‌ای استقبال کرد
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/16881" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ: میتونستم همه رهبران ایرام رو در تشیع بکشم. اونا از من خواهش کردن که قربان مارو نکشید. منم گفتم باشه. بعدش به سه کشتی حمله کردن.
در یک روز می‌توانیم تمام پل‌های ایران را تخریب کنیم. نیروگاه‌های برق آن‌ها، جایی که برق تولید می‌کنند را در صورت لزوم نابود خواهیم کرد. آن‌ها تاسیسات تصفیه آب دارند. در صورت لزوم، این تاسیسات را نیز نابود خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16880" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ: من قصد دارم به ایرانی‌ها یک هشدار ساده بدهم , امشب به آنها ضربه سختی خواهیم زد.
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/16879" target="_blank">📅 17:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16878">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ff4e7c6e.mp4?token=C4yX7aUwYitKajeZ2udCU5YJJrjaSDfVCVoFPCvremAOwuIQDO1x3NsqO1cjjD7ZFDwTunqUEufCfW9futD1gbMqLAssWsD8FxLF5mQ6KWQdxFBOxjQQB25K4Qgm_T035hGZmOC5yZoYvUiGDWgAakzM06vrKlL5ToXlyZ7rvMzi7zqSSBp68GunrJny3wsDrcQlaXXYmami2CYYtAluvahcXfHlOv3irj3Jx4zV4CbmJgFQ45UJOQ-rX93mhaZy9DGdq7FlpqEZW_b6Aa7S79DWO5dGxCOzntRl-h6WQS1-tuJ42QX9J1bhMZHQvqLVP2_xtNiEENZXGmI-Ccg4FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ff4e7c6e.mp4?token=C4yX7aUwYitKajeZ2udCU5YJJrjaSDfVCVoFPCvremAOwuIQDO1x3NsqO1cjjD7ZFDwTunqUEufCfW9futD1gbMqLAssWsD8FxLF5mQ6KWQdxFBOxjQQB25K4Qgm_T035hGZmOC5yZoYvUiGDWgAakzM06vrKlL5ToXlyZ7rvMzi7zqSSBp68GunrJny3wsDrcQlaXXYmami2CYYtAluvahcXfHlOv3irj3Jx4zV4CbmJgFQ45UJOQ-rX93mhaZy9DGdq7FlpqEZW_b6Aa7S79DWO5dGxCOzntRl-h6WQS1-tuJ42QX9J1bhMZHQvqLVP2_xtNiEENZXGmI-Ccg4FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: ممکن است محاصره را دوباره اعمال کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/16878" target="_blank">📅 17:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16877">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرنگار : امشب هم قایق‌های ایرانی بیشتری رو هدف قرار می‌دید؟
ترامپ : معمولا بهت نمی‌گفتم ولی می‌دونی چیه؟ هیچ کاری از دستشون برنمیاد پس جواب احتمالا آره‌ست
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16877" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16876">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سی‌ان‌ان
: خدمه ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» می‌گن پایان آتش‌بس و ازسرگیری احتمالی درگیری‌ها برای آن‌ها غافلگیرکننده نبوده و هفته‌هاست در آماده‌باش ۲۴ ساعته قرار دارن.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16876" target="_blank">📅 16:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16875">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مدیر فرودگاه‌های هرمزگان در ایران: فرودگاه‌های استان تا اطلاع بعدی بسته شده‌اند و پروازها به دلیل شرایط موجود در جنوب کشور لغو شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16875" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16874">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">l
تایمز اسرائیل: "ارتش اسرائیل اعلام کرد که انتظار چندین روز درگیری با حکومت ایران و احتمال ازسرگیری کامل جنگ را دارد؛ ارتش اسرائیل همچنین از «هماهنگی کامل» با فرماندهی مرکزی آمریکا، سنتکام، خبر داد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16874" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16873">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یک مقام آمریکایی به NPR گفت: «به دستور رئیس جمهور ترامپ، آتش‌بس با ایران پایان یافته است. رئیس جمهور صبر خود را از دست داده است. از این لحظه به بعد، واکنش نیروهای آمریکایی در خاورمیانه نسبت به ایران به طور قابل توجهی تشدید خواهد شد.»
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16873" target="_blank">📅 15:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16872">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2j_n33KdsM7f1M3ZlwBYSRXt1dYmy4pqaBEY0Rj9ab9nuWkK096NIfn10wMTTACp6BkXDMyB4g8rq21FDdLE95dmz4Pu7TfKnfUqo2HwWbN26V67q894xH93psVoCzrIJNcWYlPABFF5XiKmp5ewyVjZhtfwJCJ7zoVEva8b6zeKLn-l9dT26iDpyhoDTbVumNqL-IeGHhr5E5yBVyJxFBIi1TLdMDnisb2FES9ABq5punpMVHE9Z7VDT_YEAEyUt7W1jBy-2OI815g5XDDbejRugvouzFqJcx9uLJqY3oUwmKWVzJHK4XD-SZ70rf4O-UsjiX_S37uG3wR2PUhQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه دو صیاد در حملات دیشبه سیریک کشته شدند.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16872" target="_blank">📅 15:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16871">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTc2ZRujdFWA90K2PdyMNGSXntUOdVK6enRqvg2hKc0__1st_GjAG3YoGWfT0wG-4O_UttzLg55v779nK0EIxK0MwDB2Ll4zKnCUeK2CO_6aj8Oht3dDni3vDp-a1CX7KCPSKCxktPpNCarF2Nn5grecXz1LnDLfTskZ576yE0Lx9x06XNOw8EAq39l27A8w_vH_wrcf6HweDsaRNPgT-nJI53SXCoF3aXr6NyFdvyOA0cwG9V8q8qYgoKyXAAXtDmm2K6SKp6UEFXuBDnYzUlnH_vBxj2UneEmDk6cwyrMChLHmfVGwBBpSqtJsCCQWAgb6dyeC_0Jq7EBJZtSA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک الان بعد از‌ حمله دیشب
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16871" target="_blank">📅 15:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16870">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">موبایل در امتحانات دانشگاه آزاد، آزاد شد
بر اساس اعلام دانشگاه آزاد، همراه داشتن تلفن همراه در جلسه آزمون پایان ترم تحصیلات تکمیلی با رعایت ضوابط و تحت نظارت مراقبان مجاز است. همچنین در امتحانات نظری دوره دکتری (غیرپزشکی)، استفاده از ابزارهای هوش مصنوعی نیز بلامانع خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16870" target="_blank">📅 14:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16869">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فارس: ایران باید پایان رسمی تفاهم را اعلام کند
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16869" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16868">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ : به نظر من، اردوغان هم از ایران خوشش نمی‌آید
اردوغان شخصاً فردی عاقل است، در حالی که ایرانی‌ها(مسئولین) دیوانه هستند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16868" target="_blank">📅 14:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16867">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">توییت یک عرزشی : به ۱۴۰ نقطه در جنوب ایران حمله شد.
معافیت تحریم باطل شد.
کریدور عمانی ایجاد شد.
عوارض ایران از تنگه هرمز هوا شد.
قیمت نفت نصف شد.
تجاوز به جنوب لبنان ادامه دارد.
پول‌های بلوکه آزاد نشد.
۳۰۰ میلیارد دلار سرمایه‌گذاری هیچی.
رهبری به ترور تهدید می‌شود.
خدا قوت به پزشکان و قالیباف!
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16867" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16866">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دریادار سیاری: سواحل ایران را برای‌ دشمن جهنم می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16866" target="_blank">📅 14:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16863">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8jH8EzTLjdjUKjPRU2IpwncrnMdfqfpzoBSgO7sNoWnGj3TymlJqCMeu7-P2vLkhV_LGiYz7AJVg7B0R0o_2b34Nx6xTw7i9rcsC59Mczvbtl1eb3CYlVrkYxAFNpQ8bhemUzS64Xr5VscjvaAzjevktelYU5LfyrpEpc4ol9ZcJqvnCxKo5kYNPHJ_1ShagiOVJ0DG2bUB_QLXlorN0Aw19wGwFrLG5stvTuEZm77n4cpodtmOXev9WYL7p-jelhi_To4_qLJt29t0RI3SbGH0sVx1zBDEuODfjZOYJBtMsXYKzyre2ROnURnJ1wxbMszZFqo34WIc8JEDL2pxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZGgksn3dUJa9aJsBiGvlQ-TAt6l0YB3YCqfbAt_mmIZjHY882R4R-neRN85C7a_oxrkQ3nywhglCUVug1G3i8RoT-pAvwC1iPyvJbRGAt1R3HUSmjGtp-nLl7wLwG12lxMrGgQaEYdxiG5OvQ03lVdJMcBQJ43TuhKfkee0LO50-q6dTbGmnp3JDK_MnSHbZJjoJjY8zKrFkO-TGrPZIu3gWUd1XItsdCMJ_jj_jSfngvIuwE7rpNGSH9gIGy5o1iIoPk64tfruv_XelsVlcKVWpTcXegzAtMiqX8B-0pT6PJStWwRZWnHCdlfY22qUk3D9I5LQoPdA7MoiwGvGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pL3UpFgUnrJucp4Firac_LTYTTv9yzwUQR7W4ugcUuw4Is2RYCZ1V5urbg0l5BAmcjg68l0G__KfWLhw17yL1ilpQZo8Rai7_mdLwyn6pHi05tJkcLrLMknR-6cvLb7Mt3Knn6kLlvFTvQPxSDteIvzjVGs4IGH3cnaQ_38SkAgfoQiMyVA98yT8ahaXGqN8HMG0AvOkjivpsMpbDjNrt-0G07zsQLkuWr3zwc4IdUv1VDYdz0cKkvdNlXTCwcagsvhwVFC-R-hpHMTzvmochi9pDrSHeWJ15H6cmMDIPMZq8XYCLN2uWRMm0ot6mshu2KX7FGArb-IX7dtarLpifw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم اعلام کرد یک پهپاد تهاجمی MQ-9 آمریکا در آسمان بوشهر سرنگون شده است.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16863" target="_blank">📅 14:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16862">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myV4WzQp_aQa3I2da7-tLIRr73ulRUav4K-drEZFl7ZsVfDqrtsJkIJOCRq-ckKmSOcA1GnFwfU4VpxfiKzeAOUyZi5B5952C0YZx2EUfQma-yfPOwJ8rZCfi7B-eQXexZqKFn-gaCZ8UVKfpfM8WBmgZcLozLSE7Cp_hZkXTqftSk18kEaxgu2J3zS5T4hO1ZQkmBTvSjE6h6dYb7agINkzYy5_0o2vEW7ieguydkkCwaYoaxQbhJ85ZzJHjYJt2HErEhXPSh7zN7ktmgZFeRmqU0QwmMRqSlrIOj6lW1pj0qKslJFRBs_HbHd3Sd2hnunE-d4VAmt6Ljey-E3ZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای انفجار و ستون دود جدید در بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16862" target="_blank">📅 14:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16861">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز: نفتکش آمریکایی شورون در دریای سیاه هدف قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16861" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16860">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هیچ چیزی تو دنیا مهم تر از سلامت روان شما نیست  !</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16860" target="_blank">📅 14:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16859">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یاشار : اصلا به من چه آینده خودتونه !من خبر دانش آموز ها رو کار نمیکنیم ولی شما هم در این مورد دایرکت ندید ! دیل ؟
🫱🏼‍🫲🏽
❤️‍🩹
اگه نمیخواین درس بخونین برین یه فنی یاد بگیرین براتون نون و آب بشه ولی بهانه نیارید ، من فقط دلسوز شمام در نهایت خودتونید و خودتون…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16859" target="_blank">📅 14:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16858">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یاشار : اصلا به من چه آینده خودتونه !من خبر دانش آموز ها رو کار نمیکنیم ولی شما هم در این مورد دایرکت ندید ! دیل ؟
🫱🏼‍🫲🏽
❤️‍🩹
اگه نمیخواین درس بخونین برین یه فنی یاد بگیرین براتون نون و آب بشه ولی بهانه نیارید ، من فقط دلسوز شمام در نهایت خودتونید و خودتون کسی دلسوز شما نیست !
زندگی خیلی‌ روزای سختی داره که درس و مدرسه اصلا به چشم نمیاد هنوز اون رو شو ندیدید</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16858" target="_blank">📅 13:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16856">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrHp0_6JDk7o_G4VQBQJsvRkuaU9iA7Nb-9EwHFGwzddPhL6O_MAXtl80RcorMHnHglhkXqMz7ImhokXu40613Lzu8FkPLzthfk1H8MibNTUiBW6Hpdwc9txCcLzzzqmKRofm0hoqZp9naq53abLyKeU6XxoDWWr5TcWX9uUb1EN0x8UNretgPzQsToEXYa18NrSrImEqdn5urpRZnT9MhgYBXslf574v-gXWcCsWGLqabpLKACukS13jbv2MSwC9AYMQcNEve_KaY-m_0x1ntEBqkISe2Yxcknf2tYIhkwrx0QihOrXsp4jqt8YGqnLzqiOO7ba0rbRgIZ5-nxLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ماهواره ای یکی از سایت‌های پدافند هوایی ارتش در جنوب کشور نشان می‌دهد یک لانچر صیاد-2/3، یک رادار کنترل آتش نجم-804 بی و خودروی ژنراتور همگی در جنگ اخیر مورد هدف قرار گرفته شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16856" target="_blank">📅 13:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16855">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ: من از بی بی خوشم می آید، او دیروز حرف های بدی درباره ترکیه گفت. اردوغان عالی است او به خاطر من به جنگ نپیوست. @withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16855" target="_blank">📅 13:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16854">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کلاس های تابستانی دانشگاه ازاد مجازی شد
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16854" target="_blank">📅 13:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16853">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تابوت خامنه ای به حرم حضرت علی وارد شد
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16853" target="_blank">📅 13:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16852">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آموزش پرورش : امتحان نهایی حتی در شرایط جنگی هم برگزار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16852" target="_blank">📅 13:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16851">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سی‌ان‌ان به نقل از آژانس ایمنی هوانوردی اروپا:
شرکت‌های هواپیمایی باید از پرواز بر فراز حریم هوایی ایران، عراق و لبنان به دلیل تنش‌ها خودداری کنن
.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16851" target="_blank">📅 13:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: اگر ایرانی ها سلاح هسته ای داشتند استفاده می کردند
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16850" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">والا نیوز عبری : ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16849" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16848">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ : یک مشکلی در آن‌ها هست. ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. بنابراین دیشب خیلی سخت به آن‌ها ضربه زدیم.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16848" target="_blank">📅 13:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ : آن‌ها دیروز شروع کردند به شلیک بمب، در واقع موشک، به سمت کشتی‌ها؛ عربستان سعودی، کویت و چند کشور دیگر. و آن‌ها نمی‌دانند... من فکر نمی‌کنم آن‌ها بدانند چه غلطی دارند می‌کنند، اما آن‌ها آدم‌های بدی هستند، آدم‌های خیلی بد.
اما این‌ها افرادی شرور و بیمار هستند و ما باید سرطان آن‌ها را ریشه‌کن کنیم، سرطان آن‌ها را؛ و می‌دانید با سرطان چه کار می‌کنند؟ باید سرطان را زود قطع کرد و برداشت. و این احساس من است.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16847" target="_blank">📅 13:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ سیگنال حمله (سلیمانی) را داد آن‌ها همه‌جا می‌روند و مردم را می‌کشند؛ آن‌ها هزاران هزار تن از سربازان ما را کشته‌اند، آن‌ها صدها هزار انسان بی‌گناه را کشته‌اند. آن‌ها سلیمانیِ بمب‌های کنار جاده‌ای را داشتند؛ من در دوره اول (ریاست‌جمهوری‌ام) کار او را…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16846" target="_blank">📅 13:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb46c094c1.mp4?token=Yh2yrenqjGYH0s8OOFXy4JnPKnDyKXtP9p3UAM8ubuUUz5m5OQFUSwunc8Cld__fjFJKBOCHvFC9eXsb19K6VeW5Wl0UvWWjxSdo7fj73UiDDIoK7nLcOdKiHeUhKs2Os3VekFlw0VGffdG2BuxCaxXwWMPfh139lPuuj8xVJGLjKn40SML-lWPLn5jJaN2H4YfcN2n0rOSJK0aJOCypOxUrjCh9jRQxaqZoxYdxhNtfJnjLFUUw_gUrVDOTeNCQAKh0WOdD6gZuy0BPU41yfcEh0dboHtjjoNwns2WWsnptTomkkUpun2Vm-gLZ_WZjNirFIJsJI-zMy_ayuLAjahOpTD9zBvyaxSUJc7HCDllmaNHIVgM5a9hXZhufWf3VsAqXyVeHAmXC0kIBk6eXcRtsx5ktGjorllcFftCxygNvjV1ICZpi7ZYaZyIrFU16cuac-kEEgVzeGMp4hnZ9pGUO98P1k5iCS34D3XJaalJJVczuwPfNm-vhc5TbRiBMWEr0YU4lKPmgVeOkNR16_MPvUCDacAHjbM3Ow4VbXNrn2eEHRLBDgtjOFhJKFBqiik2C-oki7oir3ElejhdGwYMXS06lrosjDI77eKDR3rAM6PW60jLj_8egqO6kdzc1btJyYFNzC-A4AGsfsS8SCGyWihmc-s7Kcdxw8D0xRmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb46c094c1.mp4?token=Yh2yrenqjGYH0s8OOFXy4JnPKnDyKXtP9p3UAM8ubuUUz5m5OQFUSwunc8Cld__fjFJKBOCHvFC9eXsb19K6VeW5Wl0UvWWjxSdo7fj73UiDDIoK7nLcOdKiHeUhKs2Os3VekFlw0VGffdG2BuxCaxXwWMPfh139lPuuj8xVJGLjKn40SML-lWPLn5jJaN2H4YfcN2n0rOSJK0aJOCypOxUrjCh9jRQxaqZoxYdxhNtfJnjLFUUw_gUrVDOTeNCQAKh0WOdD6gZuy0BPU41yfcEh0dboHtjjoNwns2WWsnptTomkkUpun2Vm-gLZ_WZjNirFIJsJI-zMy_ayuLAjahOpTD9zBvyaxSUJc7HCDllmaNHIVgM5a9hXZhufWf3VsAqXyVeHAmXC0kIBk6eXcRtsx5ktGjorllcFftCxygNvjV1ICZpi7ZYaZyIrFU16cuac-kEEgVzeGMp4hnZ9pGUO98P1k5iCS34D3XJaalJJVczuwPfNm-vhc5TbRiBMWEr0YU4lKPmgVeOkNR16_MPvUCDacAHjbM3Ow4VbXNrn2eEHRLBDgtjOFhJKFBqiik2C-oki7oir3ElejhdGwYMXS06lrosjDI77eKDR3rAM6PW60jLj_8egqO6kdzc1btJyYFNzC-A4AGsfsS8SCGyWihmc-s7Kcdxw8D0xRmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سیگنال حمله (سلیمانی) را داد
آن‌ها همه‌جا می‌روند و مردم را می‌کشند؛ آن‌ها هزاران هزار تن از سربازان ما را کشته‌اند، آن‌ها صدها هزار انسان بی‌گناه را کشته‌اند. آن‌ها سلیمانیِ بمب‌های کنار جاده‌ای را داشتند؛ من در دوره اول (ریاست‌جمهوری‌ام) کار او را ساختم، و این کار بزرگی بود چون فکر می‌کنم اگر او هنوز دوروبرشان بود، آن‌ها احتمالاً خیلی قوی‌تر می‌بودند؛ چون او آدم بدی بود اما یک... او یک نابغه شرور بود، اما یک آدم بد، و او پدر بمب کنار جاده‌ای بود. بمب کنار جاده‌ای بمبی است که وقتی با وسیله نقلیه کوچک خود در حال رانندگی هستید منفجر می‌شود؛ منفجر می‌شود و دیگر پا، دست و صورتی برایتان باقی نمی‌ماند. و آن‌ها هزاران هزار نفر را کشته‌اند، حتی ناوشکن یو‌اس‌اس کول (USS Cole) هم کار آن‌ها بود، اگر آن فاجعه را به یاد داشته باشید.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16845" target="_blank">📅 13:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کویت از مورد اصابت قرار گرفتن دو موشک بالستیک و ۱۳ پهپاد در سپیده‌دم خبر داد. @withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16844" target="_blank">📅 13:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اتاق جنگ با یاشار  : امشب ردبول میزنیم
😁
💥
⚔️</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16843" target="_blank">📅 13:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16842">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اردوغان: ما برای یک عملیات احتمالی پاکسازی مین در تنگه هرمز آماده هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16842" target="_blank">📅 12:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سنتکام : دیشب ما دور تازه‌ای از حملات تهاجمی علیه ایران را به پایان رساندیم که طی آن با استفاده از مهمات دقیق، بیش از ۸۰ هدف مورد اصابت قرار گرفت. نیروهای آمریکایی سامانه‌های پدافند هوایی ایران، شبکه‌های فرماندهی و کنترل، سایت‌های راداری ساحلی، توانمندی‌های…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16841" target="_blank">📅 12:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تتر از ۱۸۰،۰۰۰ تومان عبور کرد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16840" target="_blank">📅 12:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">@withyashar
تحلیل روز</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16839" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=qy0UHsNi7oWIebXD7avoQkF85cw3KylnRN2g3HYK8_iEoQ-E8rwnX7tktFifYXQCjM8XXZ4SWB1sWOL_kxyryNyqlPS8L4wI3AgHflm0fxsCym82hTva54dJwgUXgeIx48NpYx85NBiwPyaZF0Wp-cN9JmARmrWV25EQ1fgfoaLxQCMb9KSzi0bNNxMl3Z74yhLdFD6vuaFR1-b0KUDI6CalaRM42Uo7J9w2f5LjtLS01aUE-aEus7PsQ7_SU1oVZtNcjw24jrjc8-Wo4qftuR7AGtQoXI-OdX9MDxLbSqGTS9ZKonRw85V5igdZVKWLpN3AtSX79OIm9UjW0sm5xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=qy0UHsNi7oWIebXD7avoQkF85cw3KylnRN2g3HYK8_iEoQ-E8rwnX7tktFifYXQCjM8XXZ4SWB1sWOL_kxyryNyqlPS8L4wI3AgHflm0fxsCym82hTva54dJwgUXgeIx48NpYx85NBiwPyaZF0Wp-cN9JmARmrWV25EQ1fgfoaLxQCMb9KSzi0bNNxMl3Z74yhLdFD6vuaFR1-b0KUDI6CalaRM42Uo7J9w2f5LjtLS01aUE-aEus7PsQ7_SU1oVZtNcjw24jrjc8-Wo4qftuR7AGtQoXI-OdX9MDxLbSqGTS9ZKonRw85V5igdZVKWLpN3AtSX79OIm9UjW0sm5xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16838" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16837">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ: من از بی بی خوشم می آید، او دیروز حرف های بدی درباره ترکیه گفت. اردوغان عالی است او به خاطر من به جنگ نپیوست.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16837" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16836">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دبیرکل ناتو
در مورد نقش اروپا در جنگ ۴۰ روزه
: ۵ هزاربار‌ پرواز برای حمایت از عملیات نظامی علیه ایران از مبدا اروپا انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16836" target="_blank">📅 12:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16835">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کویت از مورد اصابت قرار گرفتن دو موشک بالستیک و ۱۳ پهپاد در سپیده‌دم خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16835" target="_blank">📅 12:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16834">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جروزالم پست: وزیر جنگ آمریکا، به دنبال حملات علیه ایران، سفر خود به اسرائیل را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16834" target="_blank">📅 12:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16833">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a5af1369.mp4?token=B2ru-3211Ktl1hLmpGvuP4x0RawCvTZ1lWtExH264T-GzArCfrWqGcIImLs2yXQm569Atas3UIvXx-8jkxVuZazs-yMArJKD4alMY7AGFYZx0Z0axJk62Z9jVnpFQKBEMcc_oqgy032cVhOUgf2hZrya-lxJk5tkOuIlySV4hqo0KRSmC-AN4TOPl2sJC6C6kUTT8BInaBjInNew7QJ04U8YkN1TQiQr860K0SUgZok3r7lan_ETmos95NAC5knRo4EB8MRF84fYCNzDfGJ3oOw8QqEHj5PBqKiF91PP3IJUbLP7X7ErY6bcloZS_BH-pf56ppW-6_ipofTK2X3oXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a5af1369.mp4?token=B2ru-3211Ktl1hLmpGvuP4x0RawCvTZ1lWtExH264T-GzArCfrWqGcIImLs2yXQm569Atas3UIvXx-8jkxVuZazs-yMArJKD4alMY7AGFYZx0Z0axJk62Z9jVnpFQKBEMcc_oqgy032cVhOUgf2hZrya-lxJk5tkOuIlySV4hqo0KRSmC-AN4TOPl2sJC6C6kUTT8BInaBjInNew7QJ04U8YkN1TQiQr860K0SUgZok3r7lan_ETmos95NAC5knRo4EB8MRF84fYCNzDfGJ3oOw8QqEHj5PBqKiF91PP3IJUbLP7X7ErY6bcloZS_BH-pf56ppW-6_ipofTK2X3oXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونا توی اعتراضات دی ماه ۵۴ هزار نفر از مردم بی گناه رو کشتن‌.
مردم دست خالی بودن و اونا با مسلسل بهشون شلیک میکردن.
از نظر من مذاکرات و توافق با ایران تموم شد.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16833" target="_blank">📅 12:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16832">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اتاق جنگ با باشار :کاملا مشخصه ناتو و ترامپ برای حمله به ایران به توافق رسیدند ، و کار تمام است !!!
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16832" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16831">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14e22ad6d.mp4?token=tzHW-eOPFN30pyXrw_sc2X4poaxkEmlUKy5oo59qkN2HROiFzSpMhzWM5zvpNJO3k7mDF0VQFOEwaxT82P-e9daZVUk6GuQx58pV8qnC9ECOLbGr3N7fy4bCq2sMrpurfWQkMfNyjgLP8zh9TxB6C2Dz5ATliTJ9xczVt-K49Q_7An5y_5T5llJCzYd5FS0oxvTcmuvg_NCb2lfZuGca7JK-yBscy30NHET_IoD2XV3IKUEgFjXWgxdc7RGL0Gs-QWtiJNIGdfEMkfIzpQ1cTch-FqHyiCJ4ib0YtVfsVHqOEvfHqYf_aX0aDn6ybdjDfSsAq9Frqgimvr2oa_eiYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14e22ad6d.mp4?token=tzHW-eOPFN30pyXrw_sc2X4poaxkEmlUKy5oo59qkN2HROiFzSpMhzWM5zvpNJO3k7mDF0VQFOEwaxT82P-e9daZVUk6GuQx58pV8qnC9ECOLbGr3N7fy4bCq2sMrpurfWQkMfNyjgLP8zh9TxB6C2Dz5ATliTJ9xczVt-K49Q_7An5y_5T5llJCzYd5FS0oxvTcmuvg_NCb2lfZuGca7JK-yBscy30NHET_IoD2XV3IKUEgFjXWgxdc7RGL0Gs-QWtiJNIGdfEMkfIzpQ1cTch-FqHyiCJ4ib0YtVfsVHqOEvfHqYf_aX0aDn6ybdjDfSsAq9Frqgimvr2oa_eiYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: مقام‌های ایران بی‌کفایت هستند؛ اگر کاربلد بودند، ۴۷ سال پیش توافق می‌کردند/وی در ادامه با استفاده از ادبیاتی تهدیدآمیز گفت: «باید سرطان را زود از ریشه درآورد. نظر من این است.»
در پایان این اظهارات جنجالی، ترامپ به صراحت اعلام کرد که مسیر دیپلماسی با ایران پایان یافته است: «به نظر من، یادداشت تفاهم با ایران دیگر مُرده است.»
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16831" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ: دیگر نمی‌خواهم با ایرانی ها مذاکره کنم @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16830" target="_blank">📅 12:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ: دیگر نمی‌خواهم با ایرانی ها مذاکره کنم
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16829" target="_blank">📅 12:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16828">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: بعضیا می‌پرسن چرا مردم ایران حکومت رو سرنگون نمی‌کنن؟ خب معلومه، چون خیلی‌هاشون کشته شدند @withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16828" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16827">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا:
مبدا هرگونه پشتیبانی از ارتش متجاوز آمریکا برای تجاوز  به حاکمیت و سرزمین ایران اسلامی، هدف مشروع نیروهای مسلح خواهد بود.
@withyashar
اتاق جنگ با یاشار : مبدا هر پشتیبانی از جمهوری اسلامی هم برای ما مردم هدف مشروع است !</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/16827" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16826">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ: بعضیا می‌پرسن چرا مردم ایران حکومت رو سرنگون نمی‌کنن؟ خب معلومه، چون خیلی‌هاشون کشته شدند
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/16826" target="_blank">📅 12:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: مقامات جمهوری اسلامی آشغال هستن , هیچکس آن قاتل‌ها را دوست ندارد
آنها دروغگو هستند. ما یک توافق می‌ کنیم. همه موافق هستند. هیچ سلاح هسته‌ای. ما یک توافق می‌ کنیم.
آنها به بیرون می‌ روند، با رسانه‌ها صحبت می‌ کنند و می‌ گویند که ما اصلاً درباره این موضوع صحبت نکرده‌ایم.
مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16825" target="_blank">📅 11:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اتاق جنگ با یاشار : لطفا از درس و امتحان غافل نشید انقدر در‌این مورد دایرکت ندید و دنبال در رفتن نباشید ! فک کنین ۱۸-۱۹ دی هست برای خودتون بجنگید و درستون رو بخونید ! اگه برگزار شد شما آماده هستید اکه نشد شما علمتون بیشتر شده و برای بعدی آماده هستید! اگه منتظر حمله بزرگین نه فعلا نمیشه ! پس یه تکون بده درستم بخون ! مخصوصا زبانتو خوب کن کلی پول در‌ میاری ! دیگه دایرکت امتحان و درس نخوندن نبینما‌!!!!!!</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16824" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ : سران ایران یه مشت آدم کثیفن. اصلاً ازشون خوشم نمیاد. کلی وقتمون رو باهاشون هدر دادیم. بی‌عرضه و ناتوانن. بهتره فقط کار خودمون رو انجام بدیم.
اونا می‌خوان رهبر آمریکا، یعنی من رو ترور کنن. سال‌هاست که من نفر اول لیستشونم.
باید سرطان رو از همون اول ریشه‌کن کرد. من این‌طوری به قضیه نگاه می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/16823" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ : اسپانیا یک هدف از دست رفته و شریک بدی در ناتو است. من روابط تجاری خود را با آنها قطع خواهم کرد و به دیدارشان نخواهم رفت.
ما نیازی به رابطه تجاری با اسپانیا نداریم
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16822" target="_blank">📅 11:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش بومی از اسکله صیادی شهر کوهستک شهرستان سیریک : به گفته تعدادی از ماهی‌گیران حاضر در محل، این اسکله پیش از حمله آمریکا تخلیه شده بود و هنگام اصابت‌ها کسی در آنجا حضور نداشت.
گزارش ها نشان میدهد چند سیاد ترکش خوردند و زخمی شدند
‌
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/16821" target="_blank">📅 11:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو به نیوز مکس: خطر ایران همچنان پابرجا است و تهران همچنان قادر به بازسازی برنامه هسته‌ای خود است
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16820" target="_blank">📅 11:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: ما اجازه نخواهیم داد ایران به سلاح هسته‌ای دست یابد؛ آنها دیوانه هستند و هزاران نفر را کشته‌اند.
ما وقت زیادی را با ایران تلف کردیم و باید کار خودمان را انجام دهیم
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16819" target="_blank">📅 11:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ: ایران سران آمریکا از جمله من را مورد هدف قرار دادند
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/16818" target="_blank">📅 11:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دونالد ترامپ: شب گذشته، ما به ایران با قدرت زیادی حمله کردیم. ایرانی‌ها مذاکره‌کنندگان کثیفی هستند. ایران به کشتی‌ها موشک شلیک کرد، و به همین دلیل، ایالات متحده واکنش نشان داد
فکر نمی‌کنم ایران بداند که چه کاری در حال انجام است
ایرانی‌ها هزاران نفر را کشته‌اند و آن‌ها یک گروه جنایتکار هستند
آنها دیوانه‌اند
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16817" target="_blank">📅 11:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">روابط عمومی سپاه : پاسخ اولیه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی در منطقه صورت گرفت
(پیشتر سنتکام گفته بود ۸۰ هدف رو زدیم پس‌اینام ۵ تا گزاشتن روش کردن ۸۵ بگن ما بیشتر زدیم ، دقیقا همینه ها !!!)
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16816" target="_blank">📅 11:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7690f1e966.mp4?token=W4oAy41x-zWMf5NbiwxMxOOv8k5kJ55s1k3iu3qPBDVqppGbXsYbjU2Onjyj-SSaCumhPSGskOT9P2C2BF6c804NBCsULoNPbQ3cXPY5QqfP3M6CgwCMDr6er8XPpQJaYfoo1vYb6zVNKcpAg4BuM34tqsWcoT5fJsM5fXzBpZ7_C5TiL6ahoAqDAiNQ6ov8ag5z44We8aybjUp8bF8W56riCliEtexRZrhiCvYjgoOzom8esGCms-LA_FqWottiCl7z657dIxOo_OkN4BJ2RxduMINhHagTTBi--pEjof-V7R6OPpDT4NXwmQmL53a9_jolPaSOdDkGVZydu8yXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7690f1e966.mp4?token=W4oAy41x-zWMf5NbiwxMxOOv8k5kJ55s1k3iu3qPBDVqppGbXsYbjU2Onjyj-SSaCumhPSGskOT9P2C2BF6c804NBCsULoNPbQ3cXPY5QqfP3M6CgwCMDr6er8XPpQJaYfoo1vYb6zVNKcpAg4BuM34tqsWcoT5fJsM5fXzBpZ7_C5TiL6ahoAqDAiNQ6ov8ag5z44We8aybjUp8bF8W56riCliEtexRZrhiCvYjgoOzom8esGCms-LA_FqWottiCl7z657dIxOo_OkN4BJ2RxduMINhHagTTBi--pEjof-V7R6OPpDT4NXwmQmL53a9_jolPaSOdDkGVZydu8yXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستون دود در بوشهر  دقایقی قبل
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16815" target="_blank">📅 11:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جاسم البدیوی، دبیرکل شورای همکاری خلیج فارس، اعلام کرد حملات ایران به کویت و بحرین در ادامه رویکرد تهران برای تضعیف تلاش‌ها در مسیر حل‌وفصل بحران جاری انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16814" target="_blank">📅 11:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">داریم به این لحظه نزدیک میشیم. گفتم از الان داشته باشین، سیو کنین، چون اون موقع ممکنه اینترنتتون قطع باشه و نفهمین چی شده. @withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16813" target="_blank">📅 11:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ارسالی : نیرو دریایی و پایگاه هوایی رو زدن پشت خونمون تو بوشهر
عکس دارم ولی لوکیشن خونمون مشخصه توش
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16812" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فارس  : ۲ مقر نظامی در بوشهر مورد حمله دشمن قرار گرفت معاون امنیتی استاندار بوشهر: امروز یک مقر نظامی در شهرستان دشتی و یک مقر نظامی در حوالی شهر چغادک از توابع بوشهر مورد اصابت پرتابه‌های دشمن قرار گرفتند. @withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16811" target="_blank">📅 10:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16810">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فارس  : ۲ مقر نظامی در بوشهر مورد حمله دشمن قرار گرفت
معاون امنیتی استاندار بوشهر: امروز یک مقر نظامی در شهرستان دشتی و یک مقر نظامی در حوالی شهر چغادک از توابع بوشهر مورد اصابت پرتابه‌های دشمن قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16810" target="_blank">📅 10:50 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
