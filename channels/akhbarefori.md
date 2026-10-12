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
<img src="https://cdn4.telesco.pe/file/ErUBJj5DlLH96z_Io5gwWDsCCGkTI53ukcG3jGjPTKIc3PtQs8I78vxK06ry5ouzOf4Hn__jtiKFh44FkSTmrmYiLKEpME1X98sIjCVJjKgvVsDC340fdfvapDWp7iPAylyyf-LIt9UdbVnvPAC7AJDFe-l4AYLEJ_pX9o17LsuJa66i4WmLf8zBVjD3ue_x-5Z9Qe9K_Btj8w9XGrKs7elecr9n4rpdCIzUCZDcnAOWllDz3oEk0cqFvBB5MHkn1Tdke76luZDERr2wHGS4DvS-fWD3vCSl0IdppVQ0n58ZxJhskHQwE7pGj6GHqEpq55duDPCwv4_ofeV-lDTCSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 11:11:52</div>
<hr>

<div class="tg-post" id="msg-697660">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c3eb4098.mp4?token=KEXlnydeFMi6THkCW8rK5VYj4tiXac5Jkr2NldOiMszuzBXPYyK2QSurrYbPB-KZpsMANf10YehWQ2TQNyvxzYx8WgSsr4PTjHb-YkpkihEHRFCSUugkXFn4KF-pn5DJzrqsgnxTYsf-blVkLmAQWW-zLJLG1ZTSyWH5515Su0u8PSgIINxpgiM1ynkkGlJpIPPeqRCvwUI7LS204-ILy4C7Ist_KO5WDrykbGL6JBo7P0R5n7OcdWFYjuQpz5yp4XaLq-roB56IjQ3xq9Nmv0VXhkiNZ6K8fIWMRSLG1FxpQ-z7w-Gwoo_lfb8057hdRdaJl246g7VV6_d6BCn0oUipmSSvQ9d6Zl0xAXZn6rk8sFcWN-zHdNofmI61HN_hcH1zgcLerbPvAdT1aczOBwQfC26W9tRRuRjmYlhjn2Fz6_SSjRwsN_0kzcEGHk-6_T7sx8fU9n2TPC0AjkmHY8DmJ71ba2v90wvzuZl5fJItzRJdli9HigHUufazkXNTp3jOU6xW96wUi2P2-cnMMyJ8KqdkLcSvA-WsZRJJOWGQm555Ue-Uyo3y83f3cgBlYgssWpuRQ47PxxopcXxTrLBvEQw3MttEJ2YAkZ1srTFobiTQD5-V5-ec7Ke3g9B9yZv_uWmyrfCmwM378D0f6bf_JgF-NCd4CIlfxG0Iloo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c3eb4098.mp4?token=KEXlnydeFMi6THkCW8rK5VYj4tiXac5Jkr2NldOiMszuzBXPYyK2QSurrYbPB-KZpsMANf10YehWQ2TQNyvxzYx8WgSsr4PTjHb-YkpkihEHRFCSUugkXFn4KF-pn5DJzrqsgnxTYsf-blVkLmAQWW-zLJLG1ZTSyWH5515Su0u8PSgIINxpgiM1ynkkGlJpIPPeqRCvwUI7LS204-ILy4C7Ist_KO5WDrykbGL6JBo7P0R5n7OcdWFYjuQpz5yp4XaLq-roB56IjQ3xq9Nmv0VXhkiNZ6K8fIWMRSLG1FxpQ-z7w-Gwoo_lfb8057hdRdaJl246g7VV6_d6BCn0oUipmSSvQ9d6Zl0xAXZn6rk8sFcWN-zHdNofmI61HN_hcH1zgcLerbPvAdT1aczOBwQfC26W9tRRuRjmYlhjn2Fz6_SSjRwsN_0kzcEGHk-6_T7sx8fU9n2TPC0AjkmHY8DmJ71ba2v90wvzuZl5fJItzRJdli9HigHUufazkXNTp3jOU6xW96wUi2P2-cnMMyJ8KqdkLcSvA-WsZRJJOWGQm555Ue-Uyo3y83f3cgBlYgssWpuRQ47PxxopcXxTrLBvEQw3MttEJ2YAkZ1srTFobiTQD5-V5-ec7Ke3g9B9yZv_uWmyrfCmwM378D0f6bf_JgF-NCd4CIlfxG0Iloo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات استاندار اصفهان در خصوص تلف شدن ماهی‌های زاینده‌رود./ خبرفوری
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/697660" target="_blank">📅 11:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697659">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
فرمانداری بندرخمیر: صدای انفجار در بندرخمیر مربوط به عملیات معدنی شرکت سیمان است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/697659" target="_blank">📅 11:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697658">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
بقائی: ادعای آمریکایی‌ها با آنچه که روی زمین شاهدش هستیم هیچ تطابقی ندارد می‌توانند ادامه دهند و بگویند تنگه هرمز  دیگه کارکردی ندارد؛ بازارها هم قرارنیست به چنین ادعاهایی وقعی نهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/697658" target="_blank">📅 11:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697657">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
کنایه بقایی به وزیر خارجه آمریکا: توصیه می‌کنم یک دیوان حافظ که به کوبایی هم ترجمه شده (کنایه به ملیت روبیو) به ایشان بدهند تا با لطافت تمدن ایرانی آشنا بشوند تا ازین سخنان دیگر تکرار نکنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/697657" target="_blank">📅 11:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697656">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ba443abf8.mp4?token=sV3Z1z6MReACsiJFis8VbH3W_GLct6nK3jTx8o_AB5Sm1xF846WyGOmuqcCQb-d322NOcuh_M5T2w_MXpeecXApSc2DAgDnldeZON3Al_hyl8rntCtWqIkd5XiAQam4XhVRK7nAGtd9m0zhXL45gXrABk_8xC568ENuNvWxXxpcWG3C9uIpecZBcFENbdLb_cP7JLVN6_FPR72LdAL6Gs634g3rd5zUncVEoN63AMxDw0kVnRmbMiohsxZjCoZFF8cPFy3C9i41KTkG6pO4YmqXIVsQ-PJMcglcffUz7G4qpun7-BYZwA1BwBtmcmF4W8rvAQvRqZKF4OOxeCIbxBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ba443abf8.mp4?token=sV3Z1z6MReACsiJFis8VbH3W_GLct6nK3jTx8o_AB5Sm1xF846WyGOmuqcCQb-d322NOcuh_M5T2w_MXpeecXApSc2DAgDnldeZON3Al_hyl8rntCtWqIkd5XiAQam4XhVRK7nAGtd9m0zhXL45gXrABk_8xC568ENuNvWxXxpcWG3C9uIpecZBcFENbdLb_cP7JLVN6_FPR72LdAL6Gs634g3rd5zUncVEoN63AMxDw0kVnRmbMiohsxZjCoZFF8cPFy3C9i41KTkG6pO4YmqXIVsQ-PJMcglcffUz7G4qpun7-BYZwA1BwBtmcmF4W8rvAQvRqZKF4OOxeCIbxBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/697656" target="_blank">📅 11:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697655">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
خانم دکتر افتخاری، معاون فرهنگی اجتماعی نیروی انتظامی استان سیستان و بلوچستان در حمله عناصر گروهک تروریستی به شهادت رسید
🔹
عامل اصلی بمب‌گذاری هنگام فرار کشته شد.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/697655" target="_blank">📅 11:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697654">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شرط جدید افزایش اعتبار کالابرگ برای ۴۰ میلیون نفر اعلام شد/ مهلت ثبت‌نام تا سه شنبه   سازمان برنامه و بودجه کشور:
🔹
حدود ۴۰ میلیون نفر از هموطنان (حدود ۱۸ میلیون و ۳۰۰ هزار خانوار) پس از تکمیل فرم خوداظهاری و ثبت درخواست در پنجره ملی خدمات دولت، مشمول افزایش…</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/697654" target="_blank">📅 10:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697653">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnApiPYIrSRogykc2TXdB5HFJ5eGRnIim7TDKUDwhWCK5AmvbuYgiPbSdFFX6s0ZBxOkKbJksVbcPwbd0RG_2d5bjdH1IfKaCvOvfyhQEfPsQqmFqWYn_VhYtvWc-8SWcmIGoVgPFOsqiFGDdEG2sybiwHBHkPMk--GPIWXdeq38Ty5aaRM525z6rF8xG9LyIJOHUhYc3ps36N1EsklORpgbvT2ZaM_Lw5wX0xt-1KDevehf0fV09mwNxwQ0xp1LThG92qVqAg5YHv4xOJ4BvjQlEZ_38o7t-NW_VOHsKCRl2EXcklyJ_dmcAJr3BNUGNA-1kCDXUvfylwVAREu_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در زمان قدیم صندوق صدقات به شکل ستون سنگی بود
‌
🔹
این صندوق‌ها حفره‌ای داشتند که دست در آن فرو می‌رفت و مشخص نبود که از آن پول برمی‌دارند یا پول می‌گذارند و آبروی محتاج حفظ می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/697653" target="_blank">📅 10:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697652">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce52d5813f.mp4?token=nwpIAcRoRZj_pzrBRWueEjUIg0qzbSRjoQjXwhvhBueKnJ3bDXztrUEv42JRUBPaYvH-wML2yTpHbBh4gVQuOvdlPZ1ojcrhW9R2f4w3Miqz5N8t08UOphav4RshDPhRT5HS_rFvdvAssJXRyOfakvpwKDFKMLtLQAKK8hClR9BMaapSGdc3gM5kgGJT4JJhroSDpk8uOZ_qK5RamQxExqSZwzOT-vFIQi2sfZLGluTILSkb2q5vnXhJEp6k7dBeyQZoyjl6Li6mSIFIkhctDHSJLa7q4Xp4eG6fUeiVpq95Nga_QltnT1A7s8ethx3WeiaOI6ZhAxndMj3KANXsow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce52d5813f.mp4?token=nwpIAcRoRZj_pzrBRWueEjUIg0qzbSRjoQjXwhvhBueKnJ3bDXztrUEv42JRUBPaYvH-wML2yTpHbBh4gVQuOvdlPZ1ojcrhW9R2f4w3Miqz5N8t08UOphav4RshDPhRT5HS_rFvdvAssJXRyOfakvpwKDFKMLtLQAKK8hClR9BMaapSGdc3gM5kgGJT4JJhroSDpk8uOZ_qK5RamQxExqSZwzOT-vFIQi2sfZLGluTILSkb2q5vnXhJEp6k7dBeyQZoyjl6Li6mSIFIkhctDHSJLa7q4Xp4eG6fUeiVpq95Nga_QltnT1A7s8ethx3WeiaOI6ZhAxndMj3KANXsow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت میرزاده، معاون وزیر آموزش و پرورش: هیچ تعطیلی مطرح نشده و با تمام قوت مدارس باز است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/697652" target="_blank">📅 10:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697651">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocWjadIIp7KL9D-0sHV920Q1nzB6vFa_jZyUU9s0CmCCqlH1THugW2Q0iHC6HrlLuO_BuVlP64n3g1xHupWFR_eXY-MBeCI9bVWJO_GKU-39zjktlpMtXHbPbgUSaHGYTUMupvjwJSC0dbpPGtlWi27fcHDFS6Dvj4YcTb9VwNtfMxMUPpjoTXamX5ns4OTPgAY79kt8Olmcp4yxvyAW3TmOvcVf2WAU-vOzU3iK7uDN-Mfim4pny1B0cAaqCuaB5OXizrT-D2aGs5JWNYLFakhOwBhte0NEZXvBVswFgbON0NqpXVidJ3QrJC1yn8_TUmjsdhrjLP0aK7mAxVe_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با انواع و اقسام توپ آشنا شو؛ هر توپ برای یک بازی و کاربرد خاص!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/697651" target="_blank">📅 10:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geCWkdkJ9Ok_AIBsOvdyHIW5CKZF13Whd5Rpmec1PXPp1TgEvAboYStSgZ5Q0o9FgPAXY9BjQUCCFGloxwUOxef-RqRq-PWs2ZNE0Ng7A9GJWIMNzdOdTB2u8khXZMzZgyW3TX_Q7aEgD9w8ggec-xzl4LJweIvFia67-8euQ1DPtdYfXRyYII2BlWxX-XaKPE929Qi7ZHxSsMyDZWsuek2fv98Ue2EFvH0zQY094xGf21YOQwbxHcUpnBHrjw4wEf_wSOdCc0Bn5RnKopIif2DQ8RZ3P4n6P__fD3NG5BNXiSwt9HhUgRJ6mN0YY6xHekpDo4qSQJxWVUsHQKJhqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sje-DpdxeN2qR2qtVWQfswubQYw3Wtt13VRgvGdvTh1ZtaeQfV-yFK_TjKqBF9rpcmQA1LSCCjha9OHGxKzsOaTaE5cp2yhPqF3hIm-JccLFsfsNW1nwu2zxN6_LbAVXqhVMLr2SUQHk4PMCw0nn29cZ3Ackh5pKPggsxAZcAs3F51E0E8D54FvrlCTaaiTuNlBsCOX9znArwHrNdK4ag5fJQHlZfJjwjFA92GWP-K-3OR-PuXKyi1ZpT2nQGBsAMH2DvfPiRXHU2V8KDua0nqxHPrJaLF7geBasBhigL4h28lcCqzqWhfsCXCLO3tGqZEIy69Cml1R6Hb4Wn4m29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsx0kpGpyZzYQbon1Nl3LSSmi71XFSeQ4cw2iBDK3i1juf__GYMIcfwYx8vwsFBHxBU4po1jox4kT8ljVueBzlabuRiWw7L_O6ZYYMnTPAe_OUzRrEw-XmybM8fJse0EnzEID5kmvdk-Zp3ks5LaJHclrKxzz9qpGdutbsFn5xeQFUmbkHcorb_Hg-CFns7NcLagwkWjpRc1OIrJuXd6xVncDZdcZs3s7pmOufs94zTwKPQuXZKVWFit8_BHBh381DgiiYUZRxKBhlP_6I3tZfVrdLXFunbpmPTOxufBQnmoz2xoeVa2kYwme9v7PkYu6C0nydo53tkXCyUoUm9Sng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لپ‌تاپ، سیگار و پوشک در فهرست ۵۵ کالای مشمول احتکار
🔹
فهرست جدید وزارت صمت، کالاهایی از جمله شیشه ساختمانی، توتون و سیگار و پوشک را نیز شامل می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/697648" target="_blank">📅 10:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
شب گذشته روسیه به نیروگاه برق خارکیف اوکراین حمله کرد
🔹
اوکراین نیز به یک پالایشگاه روسیه حمله کرد؛ این اتفاقات پس از توئیت صلح ترامپ و آتش‌بس انرژی انجام شده‌است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/697647" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
عربستان برای شناسایی حملات یمن به گزارش‌های مردمی متوسل شد!
🔹
عربستان از یک اپلیکیشن برای ثبت مشاهدات مردمی رونمایی کرده و از شهروندان خواسته است در صورت مشاهده پرتابه‌ها، اطلاعات آن را گزارش دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/697646" target="_blank">📅 10:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm8YaRqs6hMrswGw0ZlQTBC8L5UZXcVdDH_BXvVKDlDY2AKjoF2WHMtljBb_Um65RrL9-e8kRyR3KkJyipfM2sinVu1YfNgzHRl2QxNjWMRdYMVOumgb8SONDlZxal2kOCxO3dGYErpcgK1aF_fbndcaENIlRwKZbyqWOXfAPnwreaTS3lEQq5o9spNn_C-lIyyuByqXA63WSzJZzvlLxok9fc05j2IXWWAT-msp8uTYsoVXLGCMOvOvcPjncqb-X8WYrLtCo7O5llAhMdBKywkAxLRE3aA42uFV_gi7x60YjAjoAL0cgz9-goXeBx8BOBBwGVGOFYqUktvLrgzGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسیر باورنکردنی‌ای که تیم فوتبال گل‌گهر برای بازی با المحرق بحرین طی کرد!
🔹
سیرجان > تهران > نجف > بغداد > مسقط > منامه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/697645" target="_blank">📅 10:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ویدیو وایرال شده از خداحافظی عجیب خانم کمبرلی سفیر آمریکا در یونان با روبیو وزیر امورخارجه آمریکا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/697644" target="_blank">📅 10:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/422efc0277.mp4?token=fT8_CAsINmomrZNB3gls9NkmVlfLGyMSF2jtcj4UXUlbw6Cu694Fo1mLMBdjSHy20oSqTGa8HSSr_QBR4s01u9Bt0-TYM01WMdF8x7z9U-ySaeQD3BdrtxdqpidcAY2CGC5jIISgnYo0_S1QctwP-KivmrNcZ3XyvLE0AOjAHAVknHpVT-VcKjPHbL1msVkb2T7SmPlLea_3CKj2ApNKxtuRMBACy-6mRcT3u1Mu_X8FWAcZuJZg4-cWs21p8J8VZZzHYWyVe3H8pA3Ir7TzQm3HFuuTkYfmapIYZsezzdejRRPEj168JmnVgJdtm3eijGkISo72ebqtvyhKGimEgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/422efc0277.mp4?token=fT8_CAsINmomrZNB3gls9NkmVlfLGyMSF2jtcj4UXUlbw6Cu694Fo1mLMBdjSHy20oSqTGa8HSSr_QBR4s01u9Bt0-TYM01WMdF8x7z9U-ySaeQD3BdrtxdqpidcAY2CGC5jIISgnYo0_S1QctwP-KivmrNcZ3XyvLE0AOjAHAVknHpVT-VcKjPHbL1msVkb2T7SmPlLea_3CKj2ApNKxtuRMBACy-6mRcT3u1Mu_X8FWAcZuJZg4-cWs21p8J8VZZzHYWyVe3H8pA3Ir7TzQm3HFuuTkYfmapIYZsezzdejRRPEj168JmnVgJdtm3eijGkISo72ebqtvyhKGimEgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم یک لقمه خوشمزه برای مدرسه بچه‌هاست؛ هم یک غذای شیک و ساده برای مهمونی‌ها  مواد لازم:
🔹
آرد نودل قوی یا ارد فانتزی ۳۵۰ گ
🔹
آب+ شیر ترکیبی ۲۱۰ گ
🔹
مخمر فوری ۵ گ
🔹
نمک ۷ گ
🔹
شکر ۱۰ گ
🔹
روغن ۳۰ گ
🔹
استراحت نهایی رو تا زمانی‌که حجم خمیرتون دونیم برابر بشه بدید.
🔹
دمای…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/697643" target="_blank">📅 10:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیشگامان توسعه ارتباطات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrrMvCwVBEeRL6l5SIZkdpMRunAFiaqdR9OGwsMoSdwsZ1DtDTPLVu_SAQH_q-pnYZBOH3SjjmJE-v4YRQzJE8nEkTJ5VdpQstN-fZB3Mr_X8Q70BkzqdRnNz4fl_04bxQ7q_twWpYAXTxTCJZuIEZO3N39Tu33-m-sUJRzi4xCsV4jQzbzi9v0Jf3v759w0lTg885_j0JGAYPzT3mnJE_wJjoYfsTY9S-84_tKHPaGDuXoUu4oEhILQRJBgaApQMVQi0IwkZWxK_6ax3e7nLYAlxUzLknPB0PuMUG_0QgS54ll951y-g7wnXD92By4nyHZ3N6XVbRAEAMydkTfqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط تا 24 مهر با 600 هزارتومان تخفیف
🔥
🔥
فروش ویژه اینترنت + مودم LTE پیشگامان
🚀
🧡
خرید ۴ قسطه بدون ضامن
( ترب‌پی و اسنپ‌پی )
🚚
ارسال رایگان + سیم‌کارت هدیه
✅
بدون نیاز به خط تلفن ثابت
🎯
ثبت نام سریع:
https://pte.ir/QTsiz
☎️
تلفن سراسری: ۱۵۷۷
🆔
کانال پیشگامان |
@pishgaman_official</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/697642" target="_blank">📅 10:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697641">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33fe8fdec.mp4?token=kv5wo79esexvBvgkGM51P859-cYr5oebnzmxQ_5KkRlPWL6whMfjOmifB1ZnBio5tmoekHzX17EwqE9TM23Pele-UEF7EsmNm3dcbey_Tgjb2qoXedVIPZnJZEj1TqvV56YyOJVcqpuK5WP3G9DSMuI6AafyFBH1S6K6w1QyE1MHruxARghWqrB8NgvH90xrmnOpOlCNYcAiqzsKgteI46LXnLqLEiantNOCQSiW27fYp2-q6c5Xa59CplBwKJ-fdrh2aQZsrzzZubgAHv0luZ82rglF91cHRT7ac7T0O5na288Eom2Ni4kBvTqvXlRnPmjL0CWP-wvvYQvY_p-kca99zVgrpdwjTEokmDSToVlSP-rmOqazLPl87UZfvy4kPcWeeS34PlzR9_4pVTXE2Etcvl3kDjV0tWocT-TI5ughNK_szYMyZ3-8C8r6SNgb16h_EvkA_YdW2_lzPlroYn4YxTJLVd2h94nqohaU-3VD0yLaN1SFIIDhLbje2RqGAnAtkNDlNy7oPMgGo9Vc5HzzCtZHQ9UsIAWe3KZkLG1W5r_NpHWwbbaL4ZtO890WiaF_tIeJqkOcNX9HSMURRTudHmsmBmVZkYR7A5Zr_A4kwNFwMZ3ezFIlZSWMx4j-F5JCuJ9e5mhgLXBfuESxmZmfw-z96HJegMCD4ZwgOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33fe8fdec.mp4?token=kv5wo79esexvBvgkGM51P859-cYr5oebnzmxQ_5KkRlPWL6whMfjOmifB1ZnBio5tmoekHzX17EwqE9TM23Pele-UEF7EsmNm3dcbey_Tgjb2qoXedVIPZnJZEj1TqvV56YyOJVcqpuK5WP3G9DSMuI6AafyFBH1S6K6w1QyE1MHruxARghWqrB8NgvH90xrmnOpOlCNYcAiqzsKgteI46LXnLqLEiantNOCQSiW27fYp2-q6c5Xa59CplBwKJ-fdrh2aQZsrzzZubgAHv0luZ82rglF91cHRT7ac7T0O5na288Eom2Ni4kBvTqvXlRnPmjL0CWP-wvvYQvY_p-kca99zVgrpdwjTEokmDSToVlSP-rmOqazLPl87UZfvy4kPcWeeS34PlzR9_4pVTXE2Etcvl3kDjV0tWocT-TI5ughNK_szYMyZ3-8C8r6SNgb16h_EvkA_YdW2_lzPlroYn4YxTJLVd2h94nqohaU-3VD0yLaN1SFIIDhLbje2RqGAnAtkNDlNy7oPMgGo9Vc5HzzCtZHQ9UsIAWe3KZkLG1W5r_NpHWwbbaL4ZtO890WiaF_tIeJqkOcNX9HSMURRTudHmsmBmVZkYR7A5Zr_A4kwNFwMZ3ezFIlZSWMx4j-F5JCuJ9e5mhgLXBfuESxmZmfw-z96HJegMCD4ZwgOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: همه می‌دانند که بنزین را نمی شود با لیتری ۱۵۰۰ تومان داد چون فقط حمل و نقل آن ۴ الی ۵ هزار تومان می شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/697641" target="_blank">📅 09:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhZ0il2lK4m0fqUYHrNcYZn2ArxN2EfYFmlTuZUkzCXIfStZWilKUwsyldpjtgTMkoMhsatC-NAaqsn4BbBfEDLPMvH_m3H1JFbmxby2KbU11Joh0Z4BaBn7KhJvGwoML8KuvZUrr6JIP2cbpkXPsVbeId465wsvCViWUU8avfMiN8nvoGBIAdosok0pF6kw8WwVA4YynWp1qsfyNgra8wRQ3SniKYjKlcxGMXXUdx503dYAUYFhU17yEK2f50sRS2JvKS0_RTj7dbvKSGgd36qed5nWHxYutSrhlCcwjqim89LZDnc0O1M5kz60HE3EiI-c3yX4rwz062Fbbg-wYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر عرب: ای آزادگان امت، مژده باد! خبرهای خوشی از یمن و پیروزی‌هایی که سرمان را بالا می‌برد!
🔹
بزرگترین فرودگاه‌های عربستان سعودی بسته شده‌اند و بزرگترین میدان‌های نفتی نابود شده‌اند، به خواست خدا ده‌ها مکان استراتژیک و مناطق وسیع جدید در حومه تعز، بزرگترین…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/697640" target="_blank">📅 09:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99dfad9336.mp4?token=JnhA53wkCMbrakrGljylVqqkH2VS1Ypdu0ekdHqSzWM_1YzsWIaZLwKPA39Ezse2FwnMJo831aZ15g6id0CoppajdhiQoRIH_w71jm-Uh-0O4a9wa5r3p4clZtCfA8K475Mz9SLJzjgOiX6AfmVeDx81u66nNH_N7mttAbXSZPB97biQcGBo0DL4ETkfTau0PqThTz1gRf4N6qjCbaNBJJbB2w0B2qbMrLXCBL47PvdeqSB4VBzjHbZbd9u7thrYSifola-MgzErfIGbSMViAMhwD1tCqv34InUH-_oRQWhvZBLtsmexZXoTsw_SD-Rqm82KyA9xig5rLUDOrbmJezzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99dfad9336.mp4?token=JnhA53wkCMbrakrGljylVqqkH2VS1Ypdu0ekdHqSzWM_1YzsWIaZLwKPA39Ezse2FwnMJo831aZ15g6id0CoppajdhiQoRIH_w71jm-Uh-0O4a9wa5r3p4clZtCfA8K475Mz9SLJzjgOiX6AfmVeDx81u66nNH_N7mttAbXSZPB97biQcGBo0DL4ETkfTau0PqThTz1gRf4N6qjCbaNBJJbB2w0B2qbMrLXCBL47PvdeqSB4VBzjHbZbd9u7thrYSifola-MgzErfIGbSMViAMhwD1tCqv34InUH-_oRQWhvZBLtsmexZXoTsw_SD-Rqm82KyA9xig5rLUDOrbmJezzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از ساختمان پلیس دیپلماتیک در میدان فردوسی پس از اصابت موشک دشمن آمریکایی صهیونیستی در جنگ ۴۰ روزه
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/697639" target="_blank">📅 09:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ترامپ تصویری از آرزویی که گراهام با خود به گور برد را منتشر کرد  ترامپ:
🔹
لیندسی همین چند هفته پیش داشت خوش می‌گذراند! کلاه را ببینید!
🔹
اشاره ترامپ به کلاه گراهام است که بر روی آن نوشته «ایران را دوباره با عظمت کنیم»، شعاری که گروه‌های برانداز و تجزیه‌طلب…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/697638" target="_blank">📅 09:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وزیر بهداشت: در سال گذشته بیش از ۱۸۰ دانشجوی شهید داشتیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/697637" target="_blank">📅 09:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ضبط حداقل ۶ ماهه گواهینامه رانندگان فاقد صلاحیت جسمی و روانی
جانشین پلیس راهور:
🔹
گواهینامه رانندگانی که صلاحیت جسمی یا روانی لازم برای رانندگی را نداشته باشند، حداقل ۶ ماه ضبط می‌شود و این افراد به مراجع قضایی معرفی خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/697636" target="_blank">📅 09:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX8dBAbRzkoAitEpKJiZy8EwvZsAahJJkCTXlK9U7CnA_ZnRFodVv1nYBrIu8Gn7dK8zRCBkrznK8uxdB-bGphWB9VxRZWbfveRfM5TLsrvn0DEf6rWMzuw0W_wX50EPPK-AhEe3nyGRyiG-qKFh3dzdP4308N7o3N8MlE-ufG0C4kFs0otnXZcAyojP3yQHUQwlYMzaOM3CyOCTzkzf8-NKBE5LJusBYI6FWzz8yWOb99_ygv0_PTx7NM_Y8FkFbF7FCOLp2ZAF25-0Fql9A9D5AA7N5_NT0unwqJrxnlF1rhQABZr28G0GQvrObYhCFzrq7xvWsLTxI9CuGqkm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماریو نوفل :فراموش نکنید که قبل از اینکه ترامپ تصمیم به بمباران ایران بگیرد
:
🔹
هرمز باز بود
🔹
خلیج فارس صلح داشت
🔹
یمن صلح داشت
🔹
ایران صلح داشت
🔹
اسرائیل در حال حمله به لبنان نبود
🔹
هیچ‌کس اسرائیل را بمباران نمی‌کرد
🔹
اتیوپی صلح داشت
🔹
نفت زیر ۷۰ دلار بود
🔹
پایگاه‌های آمریکایی در خلیج فارس دست‌نخورده بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/697635" target="_blank">📅 09:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-OHoslOe4ThaA80X9dCrEapATZL2xISZxrG9Rk_U87RDwSwEHa2eYwDUY3XHCJtc2JJs0yde5GxC_nen2VEeLdzO2g4_McDQvSqiq-Dr8Pf-xjuvvX9cGoxDZgPAIk5qiQ5bASZW3H0VrbMgT5hrLbgLhDTySnEKEoqhRrAsyXFDh9z4b1L-J4ujczGLtr6fmA3BY-3PejrorvjMhxn45Yk3VTviJRHpA9nPk8IKcN9GCaAGMNYjXovTk2gBrs_tvW9ZKBv0UWtNFxyy0cIMQBxpztItehwqh-dyclspnZP6e1qFXyZ28bdb8j_bwp1MS3wsHKmG5a2N8yXkNGjAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان هواپیمایی کشوری عربستان: در حمله به فرودگاه بین‌المللی ملک خالد در ریاض در روز یک شنبه یک نفر کشته و ۱۱ نفر دیگر زخمی شدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/697634" target="_blank">📅 09:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
سردبیر مجله فوربس: ترامپ میان افول آمریکا و فروپاشی آن گرفتار شده است
🔹
ترامپ یا باید از جنگ عقب‌نشینی کند و شاهد افول آمریکا باشد، یا در جنگ بماند و خطر فروپاشی این کشور را بپذیرد؛ تصمیمی که به گفته او، آینده پترو‌دلار و تنگه هرمز نیز به آن گره خورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/697633" target="_blank">📅 09:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه بیستم و یکم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/697632" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه بیست‌ویکم؛ رحمت توبه
🔹
توبه حقیقی انسان را از منیت نفس دور می‌کند و او را متواضع می‌سازد.
🔹
ابزار توبه کفاره است و انسان باید برای پاک شدن جرم نیاکان و اشتباهات خود از راه خیرات و خدمت به خلق و اکوسیستم این کفاره را پرداخت نماید.
🔹
سالک همواره باید یک قاضی سختگیر برای خود و یک هیئت منصفه‌ پر از رحمت برای دیگران باشد تا خود را از ظلم باز دارد و بر دیگران بخشش جاری کند.
🔹
تابش نور التواب از قلب به محیط، بندهای نفرین، طلسم و ظلمت را می‌گشاید و با پاک‌کردن خطاها فرصت جبران می‌بخشد.
🔹
به کودکان آموزش دهید که نعمت‌ها را ببینند، شکرگزار باشند و بدانند توبه راهگشا است.
🔹
نور التواب، منفعت طلبی را پاک می‌کند و به انسان وسعت اندیشه می‌بخشد بگونه‌ای که برای دیگران هم طلب بخشش از خداوند دارد.
🔹
با نور التواب، خطاهای نیاکان و اشتباهات مردمان بخشوده شده، این خاک آماده‌ نجات و مغفرت می‌شود و در مسیر بازگشت قرار می‌گیرد.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/697632" target="_blank">📅 09:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICvJ02db145cCegcI_EhIWfw6iYio0Ofjo90YDCRbmp-NQti6I-MlAdLbYJx_bP28zyad_MJ9BZqTZvhmThrj_gB9hFd_faCG3_We4q5WmH1SCYc0zdHXmlfSxFpWnIucdqzq1W2QKRvPJsPFwwDMQlEE7Air82TQZqNhPJR5oc0MvTdXSVW6jbr_Oe7C67GIVsPXijua5sQL7mS9wzDXyFWOM6IPs49SA8CzqGEoSBXv0uw-mnI2UxjIo9Fv1WGFaYTUesgBTWS1rl0ryEbysqKe9ecY_OSqNkw7tZpzjsiaqSCTfkWD1u7RbxTgG3JbFJXYPd0tWZ5gfSXTfQOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/697631" target="_blank">📅 08:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de790cc65a.mp4?token=LJy4QNVS3B-ka8n4zkQnCeB0sAu-BaCMBXu27JkLflGZ83xUZa1BrSq9EIVtCRuv2nojLaS8rpMKRODkonZzcgzFuA9B4WSSxhqYpfghE_3P9Icm1gRbOXvtGO2eZX6yV31_QaIeiKsKrQ0q-XFwBnG2rHRL_uhxxhNP8HwbqATzNd-Ej7mZ62zh1SIbYRo7539hsfE6YcFB501pX8whG5DEhrVv6rIzc-uyUzsyaK8S9__23MVwAQGmZlh9krgygO33rI12HzATwOoafTEhge9vXti0slkuMlYaaW3H8QTWUNrnR7q2dZ-Nl356seKc5PDtM-SaNW0ecEa2j104XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de790cc65a.mp4?token=LJy4QNVS3B-ka8n4zkQnCeB0sAu-BaCMBXu27JkLflGZ83xUZa1BrSq9EIVtCRuv2nojLaS8rpMKRODkonZzcgzFuA9B4WSSxhqYpfghE_3P9Icm1gRbOXvtGO2eZX6yV31_QaIeiKsKrQ0q-XFwBnG2rHRL_uhxxhNP8HwbqATzNd-Ej7mZ62zh1SIbYRo7539hsfE6YcFB501pX8whG5DEhrVv6rIzc-uyUzsyaK8S9__23MVwAQGmZlh9krgygO33rI12HzATwOoafTEhge9vXti0slkuMlYaaW3H8QTWUNrnR7q2dZ-Nl356seKc5PDtM-SaNW0ecEa2j104XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دومین سوپر نفتکش با مین دریایی در تنگه هرمز   نیروی دریایی سپاه:
🔹
این سومین نفتکش متخلفی است که  از روز گذشته تاکنون با مین‌های دریایی در مسیر غیرمجاز تنگه هرمز برخورد کرده و دچار آتش‌سوزی شده است.
🔹
تمام کشتی های در محدوده تنگه هرمز که سامانه های…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/697630" target="_blank">📅 08:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/042153d214.mp4?token=aI2RH-2lAJu38BQZOhFdptefFMcphQnx_OTtKrfVrIHOlRQ1uHPPf0yzWB6-rx0RpxIfAU1zYQoZFyOhkmTHVS1qN3es7MAz2dsLLvCbn8MPx3QRwKdDrV9-SYLUAxwqlIFUaC45Xf9O6LYtZu_3zREvflSSVrW32-2IseGR9FFLYlqnzQUywN1K3vbbg_EbxPcY4OaexFUG5gXEEkSsQvFITQDWKl1_b4gjECxg5HP4fsXaksK1CHzPLNpJu_UbbUNfTdUy2scu975PtLAs804P1bSJcRJuYoSCLcxE5UNXrWxsiNfimSWqSEwcVrXEzrT5ms-dxe6d2umDLPVPfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/042153d214.mp4?token=aI2RH-2lAJu38BQZOhFdptefFMcphQnx_OTtKrfVrIHOlRQ1uHPPf0yzWB6-rx0RpxIfAU1zYQoZFyOhkmTHVS1qN3es7MAz2dsLLvCbn8MPx3QRwKdDrV9-SYLUAxwqlIFUaC45Xf9O6LYtZu_3zREvflSSVrW32-2IseGR9FFLYlqnzQUywN1K3vbbg_EbxPcY4OaexFUG5gXEEkSsQvFITQDWKl1_b4gjECxg5HP4fsXaksK1CHzPLNpJu_UbbUNfTdUy2scu975PtLAs804P1bSJcRJuYoSCLcxE5UNXrWxsiNfimSWqSEwcVrXEzrT5ms-dxe6d2umDLPVPfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همین‌طور که روی صندلی نشستی، این حرکات رو انجام بده و چند سال بدنت رو جوون‌تر کن #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/697629" target="_blank">📅 08:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewRgLVUP704pgmQbw1c1EPvzLgOeW0NJOOlAiR810ynV6i0ygjy6EiVFYsqm34ZOrHceJjqzhJT8d2CDGEg0OyBoHPE5V-QztiYTUbj3UP6Whj-BmpK5eHfzMiH8j87dLRGgrzwf67z_ZJQGATmDGUlHOeK2pj-aA3jLsJZD3pZk2TrGYV8BTS4IQoUfbMq4riTk8Wry9tYuzK91A2fPen9VyKLtuyY2P8L6F2KpMbiMY9y4Oul2BqwQBgT4rkStfYpmFPsdAcD2Tazvrkp59sW2Lc5vFMF4N4LaOEtdfehzcp0Fb6UMxyrQSy2lk4rcuguYfLlDjWOTHQXRD-KPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تسنیم: استیضاح عراقچی در سامانه مجلس ثبت شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/697628" target="_blank">📅 08:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697627">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/447bce5ad3.mp4?token=mKJu5Arht4QjYyN4NFR0mXyjRZ4bA0A126QUUZlubmirCgeO3RpCGI1QdjebzY_hNTKcqMUKtgtKzjLOpuTb5CHlPc2As50gl2_Ma7jkD7DkUKZBUNeYAy1OCGiu2loxs7TPw6yJq4QfYTS-198zevqy3VJNabDCu4ZGV0u1FqlxwjFD4PSuMJdsqcYX2Qe6mbkpm5A1sNIY6Fk_KKWbND8-YT2x2D744kdG7itcavSF9xjRmctzwGfqXzhCoFlz5zLBfuhYhMQgzHcUebTG4ERV6NUYT0LPIjcqhpJcZMvj7YNISoO8sSJisrr-Wggx389YboV2Un527SF4w9TZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/447bce5ad3.mp4?token=mKJu5Arht4QjYyN4NFR0mXyjRZ4bA0A126QUUZlubmirCgeO3RpCGI1QdjebzY_hNTKcqMUKtgtKzjLOpuTb5CHlPc2As50gl2_Ma7jkD7DkUKZBUNeYAy1OCGiu2loxs7TPw6yJq4QfYTS-198zevqy3VJNabDCu4ZGV0u1FqlxwjFD4PSuMJdsqcYX2Qe6mbkpm5A1sNIY6Fk_KKWbND8-YT2x2D744kdG7itcavSF9xjRmctzwGfqXzhCoFlz5zLBfuhYhMQgzHcUebTG4ERV6NUYT0LPIjcqhpJcZMvj7YNISoO8sSJisrr-Wggx389YboV2Un527SF4w9TZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ : از همین لحظه، در جنگ میان روسیه و اوکراین آتش‌بس در حوزه انرژی برقرار می‌شود؛ هر ۲ طرف توافق کرده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/697627" target="_blank">📅 08:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697626">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haKRXrjJyta5XBKJIKC9Xt4sCIlaZD5YCz2LgQV3c4FDgHWlCATcr0S4UQMxVm8E8WVIrQPQgAzo38FlyaY1fpkuA0pdLQeecZY5M66z-jkMTug5aKN_7IHvX0_IpaA2msJvmlac9YxkwPTtPL9iyX_in8SdC98nUxdpJ4MnMFDVjYp3ERqCjBeakpID5dcD5N2wW_10i2NnAJ2iw2G4yxYv1y4MzKbLvwrjwYAhBO6zZJt-z1as8cBXoSxFEVyA3ZvF0XhQTgvwH01TdfLjffjzb7sZOrPzQQFYUBuES0MGn8lDrCe7gm58Z2LH0Zmku0TW52P1qYknZ8kixgzGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دوباره زانو خواهی زد؛
You will kneel again.
برای دیدن فیلم کامل به توییتر خبرفوری بپیوندید
👇🏻
https://x.com/Akhbare_Fori/status/2109369511111692491</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/697626" target="_blank">📅 08:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697625">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103305f580.mp4?token=E_fTJSJ7qTVNMs_xx_XKl4YZSuhT_sQo08cZ_UxYFzqxrG-NsXEtbK9awAbG80dJ5jpvWvijbNizy4q0teQvRB3LLYsCWA_sHJviBu_ro69-8ivRXCnwTNwZ3qFaojeKpxlaE3KEEOV3V1nXKmdHOHzk8VjrpLZYb0TBDBbQeUopI3UAz3PdtkQTZ579P9S_FxomWuMxTmjkCsEMl_nkB5-K6dHDxd_oOFPP3VTW73hSgV7uZtKhKb7ipFbiRSWomuL13rgo314busJ7ISjYsUu8owE6ddF6RlUhZ2z52REqc8FN3c2PnWLCWJH4LZB0Pqwj202EklJmfqvTU5W2Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103305f580.mp4?token=E_fTJSJ7qTVNMs_xx_XKl4YZSuhT_sQo08cZ_UxYFzqxrG-NsXEtbK9awAbG80dJ5jpvWvijbNizy4q0teQvRB3LLYsCWA_sHJviBu_ro69-8ivRXCnwTNwZ3qFaojeKpxlaE3KEEOV3V1nXKmdHOHzk8VjrpLZYb0TBDBbQeUopI3UAz3PdtkQTZ579P9S_FxomWuMxTmjkCsEMl_nkB5-K6dHDxd_oOFPP3VTW73hSgV7uZtKhKb7ipFbiRSWomuL13rgo314busJ7ISjYsUu8owE6ddF6RlUhZ2z52REqc8FN3c2PnWLCWJH4LZB0Pqwj202EklJmfqvTU5W2Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
حمله تند رابرت دنیرو به ترامپ: ‏در انجیل کمتر از هزار بار نام عیسی آمده؛ در اسناد اپستین ۳۸هزار بار نام ترامپ آمده!!
🔹
رابرت دنیرو از چهره‌های مشهور و ماندگار سینمای آمریکاست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/697625" target="_blank">📅 08:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697624">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7607b9c078.mp4?token=U4CebMgXLrJdbeYPzE4ygfh_zjcg3z0O8QOpcHVXktdn0vBTg2vAU8QdIyObWa3PN4eoHsusUpUjodUR4gX-OFq4LHFJtqgr5-PD_so9nbl8-aKiaWH6i2K-wc44lptkavd5sBXVPTC3tTEeLDS3oSTOax1S1LXxGaNbNU6-cJmQBXMMz3krwsFSuJRV0MrDzsh_j-oa_2fVUfe5twdo7M1PV_Plb2ZyhVZzutzFFdoRulS1IcGKXeDEOZnctd-6tSCgPx32QEGNIZuQau5jXhgwxdIMKfUvVhOQfdYC2Fhc-rpLXcpUDTCIwFzk_Inl55tYzR1uMWjXZBs6nEE0RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7607b9c078.mp4?token=U4CebMgXLrJdbeYPzE4ygfh_zjcg3z0O8QOpcHVXktdn0vBTg2vAU8QdIyObWa3PN4eoHsusUpUjodUR4gX-OFq4LHFJtqgr5-PD_so9nbl8-aKiaWH6i2K-wc44lptkavd5sBXVPTC3tTEeLDS3oSTOax1S1LXxGaNbNU6-cJmQBXMMz3krwsFSuJRV0MrDzsh_j-oa_2fVUfe5twdo7M1PV_Plb2ZyhVZzutzFFdoRulS1IcGKXeDEOZnctd-6tSCgPx32QEGNIZuQau5jXhgwxdIMKfUvVhOQfdYC2Fhc-rpLXcpUDTCIwFzk_Inl55tYzR1uMWjXZBs6nEE0RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر ارتباطات: یکی از عوامل تاثیرگذار بر کیفیت شبکه، تحریم‌ بخش قابل‌توجهی از اینترنت توسط کسانی است که شعار دسترسی آزاد به اینترنت را می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/697624" target="_blank">📅 08:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697623">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KD0U0mJYy7I25PUC9vp9TKUIjG_Pb8DE0l3WOschUvVBJ86Do5Gelxt6wlkE5JaU0UxYVyJYbqULHjFnaDvjJoauncQhtMKbhzg9wU0fpxfXRXv7xDxqfTGTvT-5ilwwSByNtgP4eGt0lnNck_BDbfIBnmofyqJ_AUQ4_9p6ViaQ8sHZDiwDl3UlGT8y93RLSv-sJ9E_j-wCO15MFAbiIUqXG2aaioXS2caIm0chdeg1Czp7l1S_2YL39olxoMVqw8Q8CIvetGAGeANXLFCDVvOVBNNizTUj8qwVSskhjBzfDlCGAhJtygVHe3P6rT1eQ3DneJ3qOisxmg59swH_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/697623" target="_blank">📅 08:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697622">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb5ce1dfe.mp4?token=EhsENpl1cTd8j0CE-K82NLk6kw1kOZ6xgPgnxLgdUXTEgE-saHBUFg2GWpSBCSA1zarQE347Rb9hx6AwWuHKU8Mm2J_eQxL5Na4KRShUj9fzmc_EQ-vJ18un7GFsOmUgUY_x1OqgSCr5w7tFlYGNV5cDs4VV5t2qGhRcHhg84XKR4pVDRPKqPNlHVoPIC-H7-ePwpkNNMjKjmCrvyIbo2nG8zvbU285YHR29A5beM3HXb0-gSTFqjU0wMpALM2ZKnBOFUVB-5e8jFJvYFAFet0xfwOPVlQ-6f2ZESmKfnEI0UpyS265n53Q8loQ_jJzyvAsrv0ETq0D-ZM5ZE2GgLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb5ce1dfe.mp4?token=EhsENpl1cTd8j0CE-K82NLk6kw1kOZ6xgPgnxLgdUXTEgE-saHBUFg2GWpSBCSA1zarQE347Rb9hx6AwWuHKU8Mm2J_eQxL5Na4KRShUj9fzmc_EQ-vJ18un7GFsOmUgUY_x1OqgSCr5w7tFlYGNV5cDs4VV5t2qGhRcHhg84XKR4pVDRPKqPNlHVoPIC-H7-ePwpkNNMjKjmCrvyIbo2nG8zvbU285YHR29A5beM3HXb0-gSTFqjU0wMpALM2ZKnBOFUVB-5e8jFJvYFAFet0xfwOPVlQ-6f2ZESmKfnEI0UpyS265n53Q8loQ_jJzyvAsrv0ETq0D-ZM5ZE2GgLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری جدید از وسعت خرابی‌های ناشی از اصابت موشک یمنی‌ به فرودگاه ملک خالد ریاض
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/697622" target="_blank">📅 08:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/697620" target="_blank">📅 08:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
بارش پراکنده و وزش باد شدید در شمال شرق کشور
🔹
امروز در بخش‌هایی از شمال شرق و شمال غرب بارش پراکنده و در مناطق شرقی وزش باد شدید و گردوخاک پیش‌بینی می‌شود.
🔹
طی پنج روز آینده نیز ارتفاعات کرمان، شرق هرمزگان و بخش‌هایی از سیستان‌ و بلوچستان شاهد رگبار، رعدوبرق و باد شدید موقت خواهند بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/697619" target="_blank">📅 08:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ob9XvQ4igLVhSZWSGey163boalMjusnMmPBwLtq4ZipIOEl-WmpC0jp0td4iV39Khc9e_xTRp8YWzFWHWiOAAHZ9d66LP-Ozt9UjZAClvEkOBPk4qfFw8q1mtRu06rCPNAJ3kvmifg1ihgFkB-kMwedYM72l1TG_SeePibCxD13VgGBavGcSM8Q85cq0WPiGwYyrXCR2B-ryV-Qdp6KIEgDMIhe-CRlHJmqQ37Ax7q0zmPyY-xsE-4MrcKWW51zVSeUlb5ihHmQRsSLIZXlLbIqfmwsrybehZjRIues5SLxUfeDX9r_q3xbw27vQqhIqsA5Jil38gIr99lT5fR3G4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۰ مهر ماه
۱ جمادی‌الاول ‌‌۱۴۴۸
۱۲ اکتبر ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/697618" target="_blank">📅 08:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buwPJo_FdcncFQ6DJ1080inH13xTGMrZD6hn37aQB-vbg1aFqmTe7mf8HdBxa46Jl6BPw4A_UDHFlJNmK_UY92Q0bupwAExLIrbWmXEjce50thxlCZ4ExFi0rePASqaxszy2Jz0YgAyLiULykjqWol-dnujlMw8RekjEMLkt-tQ6eA4CTAIL07iqEpQ0x2AtCYS8mpTRPMloNj3cbtBmtSNJGMj1fDrr8BvlN8v-K1EWDgZ77kk41gfQbFNKoRlg5Ha1ZNBDczErSCwPsvwJ05wMvcnZiQ-lnbqovf6D5LqeGT-b0G7e6yWmKybBVEcgbXVh5mtBeNwFqsBX8vC7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👟
تجربه‌ی سبکی و استایل؛ نایکی مدل فرزاد
وزنی به‌قدری سبک که فراموش می‌کنید چیزی پوشیده‌اید!
«الان بپوش، زمستون تسویه کن!»
❄️
💰
قیمت نقدی:
۱,۸۵۰,۰۰۰ تومان
💳
شرایط اقساطی: ۴ قسط ۵۱۵,۰۰۰ تومانی (بدون فشارِ هزینه‌ای)
📏
سایزبندی موجود:
۴۱، ۴۲، ۴۳، ۴۴
تعداد محدود است. برای سفارش بزن رو لینک
📦
https://memarket24.ir/product/fast/59406/180124/</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/697617" target="_blank">📅 00:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bc07a869.mp4?token=KliKaYZLyX89hbtU8-kytUdVwSyYSoR95LO6Gw8dnMMkU86zVp-8WLjmHJajrrDuOQvLtdI-thNPVc8RYx8XxkSiavwVVReZUfu9-8Ayts5gLpNwy754yzYaF9oSMN-NrSYoEbRNxTqLmjT5ddoKlfhTqoTuSsJ7oP86hRhePrQRcMGrICQZRGrh3z-pq349j23eG_Qy8eQoPqSB-nA0mcX1oPaf56uNFVF68I-3or_QOieMBVVxX78FjDLdmMEikvRSzMdHV-kW9A4l_uu-uIbsbP7LU7VWajaQlITXv0CTG3Z4Lzwtt5EvgqydoqA8bs17-_K6VgcpUjR7NKsrvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bc07a869.mp4?token=KliKaYZLyX89hbtU8-kytUdVwSyYSoR95LO6Gw8dnMMkU86zVp-8WLjmHJajrrDuOQvLtdI-thNPVc8RYx8XxkSiavwVVReZUfu9-8Ayts5gLpNwy754yzYaF9oSMN-NrSYoEbRNxTqLmjT5ddoKlfhTqoTuSsJ7oP86hRhePrQRcMGrICQZRGrh3z-pq349j23eG_Qy8eQoPqSB-nA0mcX1oPaf56uNFVF68I-3or_QOieMBVVxX78FjDLdmMEikvRSzMdHV-kW9A4l_uu-uIbsbP7LU7VWajaQlITXv0CTG3Z4Lzwtt5EvgqydoqA8bs17-_K6VgcpUjR7NKsrvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساییدگی لاستیک، از مشکلات فنی خودرو خبر می‌دهد!
🔹
نوع خوردگی آج لاستیک می‌تواند نشانه‌ای از تنظیم نبودن باد، مشکل فرمان یا خرابی جلوبندی باشد؛ تشخیص به‌موقع این علائم می‌تواند از هزینه‌های سنگین جلوگیری کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/697616" target="_blank">📅 00:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697613">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df7ca88cb3.mp4?token=v6sfAe-El3r-0vMV0H-_j_ayEgT72A5V_MoQPP9OWVc8PJ0ZX-CM8FL7Y9E58P5oj1d2xdUePaaW3bWA4KrL6kh9RRxE-h-Yt7GN_NoJ4W2mCUoXko6Sl63IPAWx463BKDGM-MQSfd5H9gxHMi-Jhkt2scKWLlDlCulqXUOxc-9Igmk6Oe8SvrYar9qqR1JrhAVpl7rtc3OyIJp-WYnsE2f0MOwJ6srKUNHUVqvruMVntkl8ZlVVtRdXV77ll_THY40t8JQ18oVMGRFEufOIXNGAQy-bXX_xpPJRx5wgg8nRYSXHj8X2VlunkUV0QyLzzKx2mRMti2baY7rZevDicQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df7ca88cb3.mp4?token=v6sfAe-El3r-0vMV0H-_j_ayEgT72A5V_MoQPP9OWVc8PJ0ZX-CM8FL7Y9E58P5oj1d2xdUePaaW3bWA4KrL6kh9RRxE-h-Yt7GN_NoJ4W2mCUoXko6Sl63IPAWx463BKDGM-MQSfd5H9gxHMi-Jhkt2scKWLlDlCulqXUOxc-9Igmk6Oe8SvrYar9qqR1JrhAVpl7rtc3OyIJp-WYnsE2f0MOwJ6srKUNHUVqvruMVntkl8ZlVVtRdXV77ll_THY40t8JQ18oVMGRFEufOIXNGAQy-bXX_xpPJRx5wgg8nRYSXHj8X2VlunkUV0QyLzzKx2mRMti2baY7rZevDicQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله مرگبار ببر به مردی در انگلیس؛ ورود به محوطه ممنوعه پایان خونینی داشت
،
فرد توسط ببر کشته‌ شد
🔹
ویدیویی قبل از ورود این فرد هست که میگه «من میرم بین ببرها، ازم عکس بگیرید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/697613" target="_blank">📅 00:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697612">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
قدیری ابیانه: حسن روحانی می‌خواست اروند را به صدام بدهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/697612" target="_blank">📅 00:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697611">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DORqptQXeWhiHS9Z6FZyYJf8kSPciMvWSv679Ql8EtPuRfcTJg_4tv1S0aZ14ehyrHOVZ4ZWbTil5JED_Okm9QPvbVDRGOrXf2gukme6mhPxNmVj9O9cSiTdj5c42fBFNnEF_P-4FkLzu0rUha8yG__xP9VQJUa3zVWLSvJ1TBhhE-sESbPKbbA9xJI2_TDoUL0PSUFLWDX9wWiRIKnTODsNYKxcixvAkoCTHR3CzDCskY-ziLRWQ7V8ow2zsAkR8IXoht2pCR1546FWhD4ztANxUJG7g3AasE8flGQ0agxE7bqTeIsdaS9C_kumiTmk9IpPpURVZQBJZJ2ptRtOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/697611" target="_blank">📅 00:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697609">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkDDzsIWyVNJcAWfLbPS8H5xN1f4KzKtYU7usImE6qdZd2y944bFq1Wfhb3Qzv42QPJ4fHjl4vRqweSUMZpJbDEEWxJvXe_11qC-vG0PrGJITDHuuTR5ydPYNx9_eMjke3l4cW-xcQepo1IvPJsk-R97k3g3GuNZDujAF6kEv8vJE4nXwWL1cwAhyPoOz9rQDUyEzy51vVH6FSkoxS5IZ-pufS1BJdYYB2YciQ_RlkhRbLI7nrsnq8VASzIRIsEBMJUViHxYEKgDc7UgCqujRwrOCNo4sCbdAvP3WK87JtJBlr7QAPzrTyob9uDhZtO00X-ia8QWJ9GL11iiLiqg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما منتظریم
🔹
سخنگوی سپاه با انتشار تصویری در فضای مجازی نوشت: ما منتظریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/697609" target="_blank">📅 23:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را ا دست ندهید
🔹
🔹
پروژه شوم ترامپ و روبیو علیه ایران در آستانه جنگ
👇
khabarfoori.com/fa/tiny/news-3251656
🔹
دلار بی‌سابقه خواهد ریخت؛ آماده باشید، طوفان در راه است!
👇
khabarfoori.com/fa/tiny/news-3251427
🔹
این چهره‌ها در لیست جدید ترور اسرائیل هستند
👇
khabarfoori.com/fa/tiny/news-3251640
🔹
از اورانیوم ایران تا گازوئیل آمریکا؛ معمای سیاست دوگانه روسیه در جنگ | پوتین، میانجی صلح ایران یا معامله‌گر با آمریکا؟
👇
khabarfoori.com/fa/tiny/news-3251551
🔹
حکم دادگاه اعلام شد: قاتل خواننده مشهور زن، دخترش است!
👇
khabarfoori.com/fa/tiny/news-3251333
🔹
خبرهای جذاب را در خبرفوری کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/697608" target="_blank">📅 23:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697607">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75db946e2.mp4?token=c95cj_GmwBTlAUDMXqbSJL9SNBwX39VcHCapnoK1ykURBf8YezKkZqniOSEK0fzXl7m513VCXJiTjnXKvVPIejRXuh7ILEWFqZjoehshpXFq1QeaM2tV2D86Xm9FrTgMbGpZgZk-ALqDz75SwKp2dBbXL5YybXfkRmhEsMTNNLpfmu7Tj1iNYx1-CWjzwbauQPjvOIwJIENyJlBK-oTPYuiE06UTA50gWWlaLulnRJmcZp6QGSFdUv2PlZQ9mxf22oh9zVKrZG8DDhNxhd-NgdtpDgR5h9WUr1b4BMm_0aVYuOdVwEjY6lZjd9Fa3u_e-PhKQntwaF9Xr0QRWnizIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75db946e2.mp4?token=c95cj_GmwBTlAUDMXqbSJL9SNBwX39VcHCapnoK1ykURBf8YezKkZqniOSEK0fzXl7m513VCXJiTjnXKvVPIejRXuh7ILEWFqZjoehshpXFq1QeaM2tV2D86Xm9FrTgMbGpZgZk-ALqDz75SwKp2dBbXL5YybXfkRmhEsMTNNLpfmu7Tj1iNYx1-CWjzwbauQPjvOIwJIENyJlBK-oTPYuiE06UTA50gWWlaLulnRJmcZp6QGSFdUv2PlZQ9mxf22oh9zVKrZG8DDhNxhd-NgdtpDgR5h9WUr1b4BMm_0aVYuOdVwEjY6lZjd9Fa3u_e-PhKQntwaF9Xr0QRWnizIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر در آسانسور گیر افتادی، این نکات ایمنی را فراموش نکن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/697607" target="_blank">📅 23:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7joKIow3Uqk7ct7HbO6GKElz4cc5NDxdNsSist5J8bBxokDaA2Ntd6rSe1JTOXe9C93ItbaonAETGWPNjvuKz5utxKFE3ZfHmnu3E9fj8JQDcK-pigXxORP8ClyhpcK9ywZXZ3WCTLaEtIywhYZx1hIb0iU5_yw-JLYnXlGbzEU7jvaz0mGyMuZtYis6uZpakvtUPVDUbrE4OKhcCBu1hrg-gCP-Bj0skZpxPLSUzwBkI-ZvOHlnZuX4f4_w1QfGfBxdsZoQibzx4-h8Et_PsJmx6AZClwCrb1V6mzvOEgld4BKPUZScYhbtDHjbfze3EIXG95NJ6OwVQY9IZafHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شریان‌های راهبردی هوایی اسرائیل و ۵ کشور منطقه در بانک اهداف احتمالی ایران
🔹
بر اساس اسناد و نقشه‌های منتشرشده از سناریوی پاسخ متقابل که توسط رسانه امنیتی جریان منتشر شده، مجموعه‌ای از مهم‌ترین فرودگاه‌های بین‌المللی و قطب‌های هوانوردی منطقه به‌عنوان اهداف احتمالی و راهبردی در سناریوی واکنش متقابل معرفی شده‌اند.
🔹
بر این اساس، در صورت وارد آمدن خسارت به زیرساخت‌های ایران، مراکز کلیدی حمل‌ونقل هوایی که نقش تعیین‌کننده‌ای در جابه‌جایی مسافر و کالا، پشتیبانی لجستیکی، مدیریت کریدورهای هوایی و حفظ پیوندهای بین‌المللی کشورهای منطقه ایفا می‌کنند، در زمره اهداف اولویت‌دار قرار خواهند گرفت.
🔹
این فهرست، مهم‌ترین دروازه‌های هوایی رژیم صهیونیستی و کشورهای عربستان سعودی، اردن، بحرین، کویت و قطر را در بر می‌گیرد. از جمله این مراکز می‌توان به فرودگاه‌های بن‌گوریون، حیفا و رامون در سرزمین‌های اشغالی، ملک عبدالعزیز در جده، ملک خالد در ریاض و ملک فهد در دمام، ملک حسین در عقبه و ملکه علیا در امان، فرودگاه بین‌المللی بحرین، فرودگاه بین‌المللی کویت و فرودگاه بین‌المللی حمد در دوحه اشاره کرد؛ مراکزی که بخش قابل توجهی از ظرفیت ترابری هوایی، پشتیبانی لجستیکی و ارتباطات فرامرزی منطقه بر آن‌ها استوار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/697606" target="_blank">📅 23:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5652cb8a.mp4?token=XfqudERxHcNS20uLXrRrqpq1gDc0mbShM5nf18Fh59YZKzrsSMJ6JRq4oFfgdw3pqAepCsLLTmO-0UX5W0yFOAdIAl_S06JoMQZAGfSf4EcFA-6WrlSVcTKjubC-IgZO8WUuiomS2xP9U3QXGSuSOfCEQ_prrw409eRaFiumWPHoMJbi0RRDUDmwnOxlu9tGNvx2189gZG6Pju9RRLnIUZgoQzvf8x9HRtq1ikg_I0Ga_jvVYyyRCFlHL6pKjhffNPJHSxjpy2UB0BFEQuvnLOlViXQD_vepk99vczNEE92CbV5TMuOvrVw6DwkpyIeTc44UfmMzIB0pAOZ-oVMCX4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5652cb8a.mp4?token=XfqudERxHcNS20uLXrRrqpq1gDc0mbShM5nf18Fh59YZKzrsSMJ6JRq4oFfgdw3pqAepCsLLTmO-0UX5W0yFOAdIAl_S06JoMQZAGfSf4EcFA-6WrlSVcTKjubC-IgZO8WUuiomS2xP9U3QXGSuSOfCEQ_prrw409eRaFiumWPHoMJbi0RRDUDmwnOxlu9tGNvx2189gZG6Pju9RRLnIUZgoQzvf8x9HRtq1ikg_I0Ga_jvVYyyRCFlHL6pKjhffNPJHSxjpy2UB0BFEQuvnLOlViXQD_vepk99vczNEE92CbV5TMuOvrVw6DwkpyIeTc44UfmMzIB0pAOZ-oVMCX4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرار سارقان موتورسوار که گوشی و طلای مردم رو می‌دزدیدند از دست ماموران پلیس که در نهایت با شلیک گلوله متوقف شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/697605" target="_blank">📅 23:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 12- میدان دوازدهم، یقظت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/697604" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح کتاب صد میدان خواجه عبدالله انصاری
🔹
میدان دوازدهم، بیداری
🔹
انسان بیدار و هوشیار، به هیچ‌وجه نباید در غفلت فرو رود، همچنین مسئولیت‌های آن بیشتر شده و می‌تواند حکمت اتفاقات جهان‌هستی را به طور کامل درک کند.
🔹
در مسیر طریقت هرچه خود را هیچ پنداریم، موفق‌تر خواهیم بود و آن زمان که خودمان را برتر و سرتر دانیم سقوطی بزرگ خواهیم داشت.
🔹
عزت و رشد بشر در خاکساری‌ست، جهانی شدن و به نمایش گذاشته شدن با خلاف این امر سازگاری چندانی نخواهند داشت.
یقظت را سه رکن می‌باشد:
🔹
نعمت‌های بزرگ را از وی دیدن
🔹
جرم‌های بزرگ را از خود دیدن
🔹
عیار روزگار خود از زیادت و نقصان شناختن و مدام از جمله‌ی مکر ترسیدن
🔹
اول، نعمت‌های وی را به سه چیز توان یافت: به نیاز دل_شنیدن علم_پاکی قوت
🔹
دوم، جرم به سه چیز توان يافت: کوتاهی امید_دوام فکر_بیداری سحرگاه
🔹
و آخر به سه چیز توان یافت: بدگمانی به خود_بریدن از علایق_تعظیم حق
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/697604" target="_blank">📅 23:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697602">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxnLuqDvUDy5cSJobI35MKYnLOyHPxyM1UVTrsr1uxbGNZQ6J19D3H8xOM6cXgo_sXW4V2elTHTCYg9ZZX5145F-AhmthOmvftHFZqx-3PnBeNrz4l0CrInNxQGDQQM1w3QMlzeM-94lhnS-EFsvqQPu5ZTK-4ibQTplsXXV3HGMjge7Y7VsIkyJiAVpgKGg-M4oAdxc4xMj_h_B-eEfVPeFNX3hZeATnpueCm_iLvR6Uqk3hu5_a8d0C-pgJHxlJMrJgietT8i4mCW0UhehuzXkYKV95m3ADLVIOsrCTjvunOWEie2kMCVUjjgsY-_RG6gtOZioSHu_pNIiqhRdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چشم‌ها چه هشدارهایی درباره سلامت بدن می‌دهند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/697602" target="_blank">📅 23:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSLkHcsfEt3FlQOKy8jEAQKqfreQGem905hRdhpte8aCqeQSC-wKq_zueoxaC7EL2aloDTnkplJI9fVSRYbVCnNcR9qUSaDWBYBuTee1NT5eV1j841xQWAmakvz1pxTWqq7UvIqqZ_W0C8v91ByuFt5K0dgEYifNUje2lN2iJikAOAZwC1JcSyx4HBwAGyhoPbSHvqZ2BRlcfEbHShrz5IJQs9t5QvDxLLS3O6b1hrT8grtlbXCyIFbCFmxKKZQWor0-5ZTlM5U55oZVfUQIXdrte98kW_LuqIz1qHiSMNMmswlqqJUgvAoCdEwt3wowUifs7epCrarsuDqr8JSfpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای عضو کمیسیون امنیت ملی مجلس در مورد تذکر رهبر انقلاب به صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/697601" target="_blank">📅 22:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
نشست امنیتی نتانیاهو با محوریت ایران
🔹
رسانه‌های اسرائیلی از نشست امنیتی نتانیاهو با اعضای کابینه برای بررسی تحولات منطقه، به‌ویژه پرونده ایران، خبر دادند.
🔹
این نشست در آستانه انتخابات کنست و کاهش محبوبیت او برگزار می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/697600" target="_blank">📅 22:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697598">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/829439bcfb.mp4?token=g90GZwxvuJ37ozoXXRdG3k2xscOntWhD1GhuHNCCilCpYhhBwuyMi9TUxlIHRzFUgKLfQAZkfqRvNkw3RG-sdA-k9ij687zCp0YpS14nvdMaZLBoP_rVtXVmVH2XQYT4y_nMHAwkaxtQqnAZlCotiJHSSuxRP3YQ-pYfdcTnwsuoxh0l4kNerYUubAqHTnikULm8FQ_RgoLbN83pupsve0auI1VZvhTDvwHRMvWofKIDd2vu56_dQ1inxHvez_hcrNs-PAvie9bdnOYCNlbYXoboINDhmKuPAgu-71HDJzhMFrzbS1I-xedvx23DoL5adk9qgu3yD-qFFGTQbHj9Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/829439bcfb.mp4?token=g90GZwxvuJ37ozoXXRdG3k2xscOntWhD1GhuHNCCilCpYhhBwuyMi9TUxlIHRzFUgKLfQAZkfqRvNkw3RG-sdA-k9ij687zCp0YpS14nvdMaZLBoP_rVtXVmVH2XQYT4y_nMHAwkaxtQqnAZlCotiJHSSuxRP3YQ-pYfdcTnwsuoxh0l4kNerYUubAqHTnikULm8FQ_RgoLbN83pupsve0auI1VZvhTDvwHRMvWofKIDd2vu56_dQ1inxHvez_hcrNs-PAvie9bdnOYCNlbYXoboINDhmKuPAgu-71HDJzhMFrzbS1I-xedvx23DoL5adk9qgu3yD-qFFGTQbHj9Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوباره زانو خواهی زد
You will kneel again</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/697598" target="_blank">📅 22:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697597">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2db05af4.mp4?token=Z51Bc0aTxbvPkf7W0-8d8pLm0oTn2bGSKDkXkcGf14wReBPZHKMu1vKGRWCvDvct8b_ImVvGkqI_KXDYUvj8CcA4bAM6Aio551fxEgV3k-OB83N0JSNUlmbzjksyqjTjfAB1di803dNYo3UzaWL6uF-xIjc5wF4B2vevaFdK8Ielga_abF1HcKGq0Z56Pts0tgkSaFhply4qUoEFvZyQWu5XXliyfMS64B9D-L1KGkhLOlOiusPWwiMMnxtjROwNh16ULQnYJXnSW7rFYAROP8atOsHvmpWbTZzNiMan1bYyECo0Xc-nLG3QbCKYOjdHRuktYhtcHLoLfDYtlslQFoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2db05af4.mp4?token=Z51Bc0aTxbvPkf7W0-8d8pLm0oTn2bGSKDkXkcGf14wReBPZHKMu1vKGRWCvDvct8b_ImVvGkqI_KXDYUvj8CcA4bAM6Aio551fxEgV3k-OB83N0JSNUlmbzjksyqjTjfAB1di803dNYo3UzaWL6uF-xIjc5wF4B2vevaFdK8Ielga_abF1HcKGq0Z56Pts0tgkSaFhply4qUoEFvZyQWu5XXliyfMS64B9D-L1KGkhLOlOiusPWwiMMnxtjROwNh16ULQnYJXnSW7rFYAROP8atOsHvmpWbTZzNiMan1bYyECo0Xc-nLG3QbCKYOjdHRuktYhtcHLoLfDYtlslQFoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا مطلبی: دلسوزیِ بی‌حد، حتی برای عزیزترین آدم‌های زندگی‌ات، گاهی بزرگ‌ترین ظلم به خودت است؛ لطف کن، اما خودت را فراموش نکن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/697597" target="_blank">📅 22:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697595">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzxD_UyxnMLuCQw-jovJ166d8XVlsuoTr7z_vY8vH6-2wM-taOipv7QHeG0LL5HMUbPXc2aRga4cgOq9fB3UJUG85N_WVN2GvmM-7aTzNiM41XYzJYtn8hHYLioZw9xfhuWDK6MioQ53R2qQid5-21oOy9p0HSA12yQXATGym1yNeWnuc7NdFtwfDXgGjjUb5rL7NJtVUo7PX_NXzxOgPoNzNaTWhGNPZYKYTdNpaQL9u6atGc1FVMslIe8MTjoI2MC9A-t1PUkrBNEpKBf5jOJktaJVhYmjkTo7LmcnR0y2FVwUPkk2fZ2kKiPyQz54stIdsYWD0bD3qiKBdIXhIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sw_VVqZT2UNZVz8KONBkC3wlkNhXp9ECiepzgv4AfpCiKBHskjQIMRNXRinzUGM5bjAdej_a7dhbqVumiCSl09IrIfhleNMeJHROd797pcJpqUeO2hroJUUk0Lsq--7zNRBHb2EPv5HrMbgptqjktjmtkP_baznUjYtz2l1T3fbvS5P-VK1HWNPxW8fb1NMp_2PNOXoKXbE29EfIARB_cflnKtk7NUoN1XY3yolKH9SW709iceAaaqpexQlupOIPNVOauq1GYLHkKg726NpjykP1rtpN9esLAiHzBj38MBwp4a84HIRaP9yIwLbaGDLV88qhMemoxoe3CjtR8_A9CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرقت ۲۷۰۰ گربه برای فروش گوشت در ویتنام؛ بازداشت ۱۲ نفر
🔹
پلیس هوشی‌مین ۱۲ عضو یک باند سرقت گربه را بازداشت کرد که حدود ۲۷۰۰ گربه را برای تأمین گوشت رستوران‌ها دزدیده بودند. در این عملیات، ۵۰ گربه زنده نجات یافتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/697595" target="_blank">📅 22:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697594">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
محاصره زمینی ایران شدنی است؟ | نقشه ترامپ برای بستن آخرین راه‌های تجارت
🔹
در حالی که آمریکا به دنبال تشدید فشارهای اقتصادی علیه ایران است، اظهارات اسکات بسنت، وزیر خزانه‌داری این کشور، درباره رایزنی با ترکیه و پاکستان برای محدود کردن مسیرهای زمینی ایران، پرسش مهمی را مطرح کرده است: آیا واشنگتن می‌تواند با همراه کردن کشورهای همسایه، راه‌های تجاری ایران را مسدود کند؟
نظر شما چیست؟ بیشتر بخوانید و کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3251621</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/697594" target="_blank">📅 22:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697593">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-MEcqlVWFB5WM0d0OJVL5GS3sHmUEl1ZN9VLpXI6O3FupXdQtvMnxd2XzbhmLeHYhSwTgOaM1W4eT-SMSGFsjPfl6ojsQW2rY_Pm4o8RKNbS-lDKijZ0ZCU4Xo_qBiAPUL2wS9hBFFIkRtDRBSYFwdX40DPeAfI6fV7to3vhXfFWMPC01M6suyc4xMKANyS_z3au4DQkGiJ1cYooLAX0TcYuAtrEQaKdhM8T0ue-khhz8ouJ5VOWKByrk_NvFsWSPqEPTVqBOvDSrQxhC0-jv2IwmjY-Cvs7JpH9tlDUG27x348tG88UMtys38bVUpG9bIQBObd7jUjo_SqUyWplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش قسطی شمش طلای فیزیکی
با پشتوانه
گروه مالی فیروزه
✅
بدون بهره
✅
بدون کارمزد
✅
بدون ضامن
https://in.firouzeh.com/gold2
https://in.firouzeh.com/gold2
🔙
مشاوره تخصصی و رایگان سرمایه‌گذاری
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/697593" target="_blank">📅 22:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697592">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATUu0KxwZYHvucECXHVM7DLZKRjeySuC8mHK5FoEOPKIMf_6ciez4ne-bNPHqJ2isi4XwqfSgc6cpHeZysy25elK3b_4UXVCtyYMUPdvfCO1PvfmAoNRwkakLGvxyQFtSTUDrBhLmatrl2GjRrzzkeToikfTKd5sscxz5h8aItEuymnw2vgpiEedYEWXmgtpf80CzdvYeLeVUxZgyON-oXLQyXeYzfy5CzwxNbvIZ8kSuujjqh0Ot1K1_gxzE7d6y6UzPL4I7N-neZkbLBGWe8-kMtl9UZDaWg_pVa00YY8d2tyHBl7k8WzkKM5Iii2qinpRkLPncwTrWxr1TjfYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای خرید ۱۱ قسطی، بیمه، بازار داره!
کلی هزینه توی سر آدم هست و همیشه موعد تمدید بیمه موقعی میرسه که اصلاً انتظارش رو نداری…
برای همین دنبال جایی بودم که هم بتونم راحت
قیمت‌ها
رو
مقایسه
کنم و هم
هزینه‌ها
بهم فشار نیارن.
راستش برای خریدش رفتم سراغ
بازارِش
!
چون فهمیدم تو
بیمه‌بازار
می‌تونم بیمه‌ام رو
۱۱ قسطی
و با خیال راحت، تمدیدش کنم.
👈
خرید قسطی بیمه، از بازار بیمه!
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/697592" target="_blank">📅 22:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697591">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZK3g8eF2tdOuSJsUEURr16D89SAGKsDefcdUIpiI5M5vqt_cHWOdJhxRjRA39aNWiDRtEbcEGH0B0p4nyUADkb_JdmOoYd-wUx2gMo7W_CzLv1C8hWMZ86Q_SsEStfdPwuErYPsPbW_n-WOknrAt-FnZVlE1iIc7wXs8BTMkrpCLiBz9T31AZDmpwnbpYVn5z0Zk1ZMv6g5ZPqK_75gzkjKD-O4HzGOL54NBBHWgF7qGIHyg9vJrPpEOkk7JrMa07-mMRIbNHJAtZRBcib0LT53RghGAk5YJv0hqgkFlLEHsUTODbXANw8kSkr3j8njRTncNHLUMLnPasGG0ro_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر خروج زینب ابوطالبی از کشور تکذیب شد
🔹
خبر منتسب به باهنر درباره خروج زینب ابوطالبی از ایران که در برخی رسانه‌ها منتشر شده است، صحت ندارد و وی در ایران حضور دارد
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/697591" target="_blank">📅 22:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697590">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec619d00b.mp4?token=slDwpwJpvfZu2XlUbT30NGem6Ya7w6dh1OCcy_wS4Zaf4xwlm8rEuhf4vDUTh0tzyYbTdReNoXDzmHF1X9rX1N-EaCvmndFZMqZQHKquZHfC8OpItm7I-8v1I5h8P0xy92Ur3HhalF6rBqjM-Z-b0zAif_vqTrXtib5oMkmXxePOcEkfEGC5NIcWa9mB1EOURKWJ37aj2KaPWFMx-XdUmqidsoa6VHdRuhPNpAUFevFW7_P6JrKHObhPpwqWeAcVs19dSIsZvTpCCFMTUyTdyPRoo7ZyPxrNsBQoevlwhYrOYo_duV6mifm38gJ1eJ0Lq9SmgX8EOFeBwTtRCmVUxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec619d00b.mp4?token=slDwpwJpvfZu2XlUbT30NGem6Ya7w6dh1OCcy_wS4Zaf4xwlm8rEuhf4vDUTh0tzyYbTdReNoXDzmHF1X9rX1N-EaCvmndFZMqZQHKquZHfC8OpItm7I-8v1I5h8P0xy92Ur3HhalF6rBqjM-Z-b0zAif_vqTrXtib5oMkmXxePOcEkfEGC5NIcWa9mB1EOURKWJ37aj2KaPWFMx-XdUmqidsoa6VHdRuhPNpAUFevFW7_P6JrKHObhPpwqWeAcVs19dSIsZvTpCCFMTUyTdyPRoo7ZyPxrNsBQoevlwhYrOYo_duV6mifm38gJ1eJ0Lq9SmgX8EOFeBwTtRCmVUxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌گرفتن پاوربانک، هواپیما را مجبور به فرود اضطراری کرد
🔹
یک هواپیمای مسافربری شرکت «ایندی‌گو» در مسیر دهلی‌نو به چنای، پس از آتش‌گرفتن پاوربانک در کابین مسافران، تغییر مسیر داد و فرود اضطراری انجام داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/697590" target="_blank">📅 22:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697589">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d71afbb8.mp4?token=nIJUqw9T58JGqZNcNPmn7X5L3wTxUj5rlDZnJJxjxSA0t42v4GsuQ9B7fzI6l7INt1qkfyNJFpL97HjmW9lRFQEJqIyULbgjQXzmuYTvlEDC1FB_sOt--7ohdDVoSb5ovNqqtlVUJM3RObvhMKizGNfTMLxoBfoAT79M4r9k0yAbeQsvPjfgNmxCZbPY7qKtPeY73J5BScTZyg0uH3vx3glZGCEitIxIwhZk61tgPoz3o_KHvMukLF7bFfWJMKymtNI2MwIbq27LFH-VIS8tARWTdnVCYfkV7xVoK0fnV2Ds4nYP2brYyQFgd1aj287TU4UTk9jf5d9mDSCZzXgAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d71afbb8.mp4?token=nIJUqw9T58JGqZNcNPmn7X5L3wTxUj5rlDZnJJxjxSA0t42v4GsuQ9B7fzI6l7INt1qkfyNJFpL97HjmW9lRFQEJqIyULbgjQXzmuYTvlEDC1FB_sOt--7ohdDVoSb5ovNqqtlVUJM3RObvhMKizGNfTMLxoBfoAT79M4r9k0yAbeQsvPjfgNmxCZbPY7qKtPeY73J5BScTZyg0uH3vx3glZGCEitIxIwhZk61tgPoz3o_KHvMukLF7bFfWJMKymtNI2MwIbq27LFH-VIS8tARWTdnVCYfkV7xVoK0fnV2Ds4nYP2brYyQFgd1aj287TU4UTk9jf5d9mDSCZzXgAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار عظمایی فرماندهٔ نیروی دریایی سپاه در اجتماع مردمی
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/697589" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697588">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/697588" target="_blank">📅 22:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697587">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
گزارش وقوع حادثه برای یک فروند نفت‌کش در نزدیکی لنگرگاه صحار در کشور عمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/697587" target="_blank">📅 21:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697586">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN8v8SrfGjtFwXC7eiHpXmedjblwr-6Ng5_k7MK0fKxSe6c6E3kp7tsNjH96rWSacAm2hraroWHWGSTZJcIX1bNprMwzEb9Cvb79VF2vulkHA61TriFOVPVQcdupW1YZ0QJ8sy4g91H-yLngFqIF4EEOp7f_wvx1-25VP5CYIZW2tGMjJhw2KQFDR59ddIrx5P8f04gpRiv7rVj2wH-R6pi8wFAZTAJAQOYn4qDtABppVmCPF98O1STkdiKDbL4Yr3KzMB_2__f4HaKLsrmAVkEZzb6fBfcF8UsMPgp8ndsHXDm5rjKF8thkzbfkKysWd-00zgTxWleLBIN9ykl5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رصد پرواز جنگنده‌ها و هواپیماهای نظامی در حریم هوایی عراق
🔹
۵ هواپیمای سوخت‌رسان KC-135، دو جنگنده F-16 و دو جنگنده F-35 با مبدأ پایگاه‌های اردن و اراضی اشغالی، دیروز در حریم هوایی عراق پرواز کرده‌اند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/697586" target="_blank">📅 21:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697578">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8aoxTygta2TMKib_czugoEEADE5BWAEL-jHHUH1bUhUMce86RdlGG0g4NOdYcoWQqoziPR_A3ub2qxZgr_VD9pY5lrouSnpQn6Rj9Gw5rdYjR6UwUBS_wruOJRYozyVOEeSlquMPpBGxCwd7_UZoVjVVGWImDmQAUmWavi4rPWVZPLHU4OzTurCkrKmYzHdKLyliU1QD1UfYhDf_fyIowcs_C1n0in8meD0l9dJpd8I8EVaqNEN2hdJHXuYFvJEn3k-ePCNPQur-7pTjX0WtApxl-f4HBAjaWxHPvfJyEvkMpGUfF2Wz2yd0RwVJzxb8XqY5Lk9IYt2apFdMXBjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NVNYbaci962S_Mk_4HCJvonp8Br0wbgpKhVnQeRWzrDb3TYhRuJK_CR5fUoca9ylRA5BgQSxa1ATKeSr5AWqPdJcNW3aALh5GdKW1G4EMcnxLrwKngeEo0gHwWEAgSyeKDlieo6jnGbl0tUOAWBT_WpcV-Ar0fQ6xNzhXXJEdL_SPvr0KMk8Ft5fGqocmCZkOXh3v5KW2ervMXndSUI1vIAh2rxlSM5My1Td4_NWgT1XS7m-fOfIpQLOqc1_eB2ZMwm60QMLhRQv0cBYmYm2TTpM5jSdNolBzNdeeswqcVWuSvbw23k4HxkulTCw0XTcma3UHIxX-ucYjO9-2GbOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqAIP8lEx-aIQlzZMynwDCyQ_BQY9iixHFz_PmRFIdsQSodcDdZI3-2Keye9xCMhYh-upDUH1VFwajhvym32PxMKNUpvOnzxw_IrrBdB2bq685Um3GL9_m3qrFMIq4edaP5UxGVmVEgShvHQiIie0HKrkopGZFJnI7gAxwpajIsSqZnkl_zWrmyrF7P5h9ZWKfasOyI8NT0m-AgCgqrX-rbRf1Q36WNnfq2Cu3GN7XVEu_6F_k7E8CP8KcnL7YUn9-T7Mz7vyZf4V6sYNu4weve5_PBil8LJCBbyyrxh4iQCR-GI2Y5YhkROjMdxi7WFuyP3r5FzxFYpv4E9ghskGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhQ63qjWSOcts8Ddt6v9Od3tVMVbxCuZu2lqw5CTv9w9jL1ZXkvDNpUxpWPEpWLeIu0Ihihj8BdgXoIFNmnWF562UQ-f2IH6ydXdYnleLIIXB4Zv8Lbkd2W6ZUuUZ-Vo6bcIlyRvTRpKcFYwyYDp9UFfu9m7GwkoR8S5eoTGxDNSPvHtsFzZsomTodE9X3WetctBkXH9xtD8FD8j15lnScgHHr6YBxyHRKv5luTQDEu3i3dohCwEGi4Ebd0FF0_2QuBmU0iGC5mXhj6ASqvXqE-WlLbAab1zXvmHpaehSoTJ7K_NOzTBr826KnjYBLOINw8fcqD0mfFYanm0FmARSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDUE941fI43_qrwWek6zcMu4edBR5FZcfvhDsT8y_08BUWtdai5u1-mMy2g5Hy8-VOfQHOjz87TUSvXiEtmX56vFGEwHCE-dVw8czl9jPLRjql7Oi0VXYyVKuFB-Dy3Jp_VPavdXWCfn5k-qC33kNSzKKimeGUb--s2lP2AW8j655SjAOnJF4ZTjtBRHB54Zk42pxoLhbFUsbKvbKz9YO7xEZ60vQi1Uj54eCo8OA8ZLI3heO-8VoY88JJDEXA8YzwiXEtKuaEfZqrdOl0EN-h_d54g-bmYhUm6U5tcdqG6rDybAlX63uhpzteYc3IlA22VNpZ6kQZfd1LAgrqvtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBN2ko2JJW064JgN1kMkp1Dy7QL46oh9QpzLa58VPlBNWmYi7I-1khmr4ZIYOA84DF7if1C6qPM8JGt9Sl8ilMTwL4pNh_qty1EcUwWX73YdbhGk6oX9npAlg3IYfSU_u3SYhGTkhR8To1kz0naNk8gibDn4e1NdK9Y4Ik1gs49owux15m6jJR3FZDgKA7SP3jLwJdRqNHjowSU1ZCt0IHLGY7ZBaPf_J6jhGThRDXzU9Bo4ugwBAJnk56DWELbuQ0cqE6dCFexd_WTdkLiNm0BHfsBpUqM2OGzDD1Cv1dkXi8jAbbCICYRyN6MS6FbUOpzgl-s9L5RpNtrVaupwZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/splocHU6fGrgU5p8i8LvskWLLcjFbKUvm98wtIzXyyM_OToRNSBZGPr-1vtgSQUuXBDqZBqo6H88qZW0U6-FsZkxlqupkCnvw6MMNu6R4-CFfZ7emQEsZQYu63J4CDQN08_ZN1Nicul9PP4pVUiqARQuQnVwjwh1TIzaRZFA5hXDCHTWEJxC9KtuxkEZERlF0_7zCN-AiDkVdkoBRZFHofCl-zeBq3VI4rQK-T0F8snOCGap1fSwOF74KEd-nanNJf5hhaBU8UGwL_ywEiX7X5rMfizHW0G7aj0Z3oo3cv99RGm1AFtwNvjlN8ClWApuCm4-ti5ezcti-rkKpa7Ohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9zQpokKO6w_pcrqs-xSzuqlBmpaIsnPp03EWGw3Yn9fH6fFpAsRKvSHSugh5AH0B11wING3kAJPvaqFDgbMq4oFma6QFRTIf5cAMGTYQQtDFkNIR3MYz47fg7QzPnEqpl38feO4wmX3jcL4r6ZONG5rzDuTgXSFRMJfbtCqJjkA6LJA1u--MGjq7f7AjUtf9f89CN-qLhOAIdxlEWE948AX93gAwrCYV1gph93s2vIbUjaWxr74k8jaA-wgnZz3sTbb8yzeYpUJXV1yzPbIT28CVBMFk7MpMKbNwgudG6iK135LsPabd5rs-kcTIlVx4zsK_tXjJZf3FQKIhfHaVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با چندتا کد ساده می‌تونی ادیت‌هایی روی عکست انجام بدی که معمولاً کلی زمان می‌برن؛ از تغییر نور و رنگ گرفته تا ساخت استایل‌های متفاوت با AI
🔥
#هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/697578" target="_blank">📅 21:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697577">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a5a7390.mp4?token=VKG4GnsPH1q19ZNkVLubUz3KCMhHGdy425yzRAQ6H_a8rYNQzlBxuMoKcBvAeo6tgo0TrOjR7jyOff7vgSKnq3j3HluPM9LSRNMp1k0NfRcZAIMpC20_d3UpHcPkXT6fXSaxK0CwT_NdhZfDwIH9AOjWO59kQYLdd44o_9yCyapD2Wr8fctb4GTy6uC0chH5x_xSSaTrw4NyhZsxRBWeMikxfsuoyPcjLpe0QMhCWmQSlbpIuTJzEVe2m5kHFhQ2rg8vjmj26Wyy7xIpGlBI7IDs4BW4J1Ex15vqeO5spX2YU-nBTgnMj6LX4ckkbedYsGR9qV7hr_gSZSg8b8j_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a5a7390.mp4?token=VKG4GnsPH1q19ZNkVLubUz3KCMhHGdy425yzRAQ6H_a8rYNQzlBxuMoKcBvAeo6tgo0TrOjR7jyOff7vgSKnq3j3HluPM9LSRNMp1k0NfRcZAIMpC20_d3UpHcPkXT6fXSaxK0CwT_NdhZfDwIH9AOjWO59kQYLdd44o_9yCyapD2Wr8fctb4GTy6uC0chH5x_xSSaTrw4NyhZsxRBWeMikxfsuoyPcjLpe0QMhCWmQSlbpIuTJzEVe2m5kHFhQ2rg8vjmj26Wyy7xIpGlBI7IDs4BW4J1Ex15vqeO5spX2YU-nBTgnMj6LX4ckkbedYsGR9qV7hr_gSZSg8b8j_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعضی همکاری‌ها با یک جلسه شروع نمی‌شوند؛ با یک گفت‌وگوی متفاوت شروع می‌شوند.
در گراد، ما به فرصت‌هایی فکر می‌کنیم که هنوز شکل نگرفته‌اند؛ به ایده‌هایی که می‌توانند به همکاری تبدیل شوند و به ارتباط‌هایی که شاید مسیر تازه‌ای برای کسب‌وکار بسازند.
این بار در شیراز، نه فقط برای معرفی یک برند، بلکه برای شنیدن ایده‌ها، شناختن ظرفیت‌های تازه و پیدا کردن نقطه‌های مشترک کنار هم هستیم.
اگر شما هم به امکان‌های تازه فکر می‌کنید، شاید این دیدار آغاز یک مسیر مشترک باشد.
گراد در Shiraz Expo 2026
|
📍
سالن حافظ | غرفه‌های ۴۳ و ۴۴ |
| ------------ | ---------------- |
GERAD | G NEXT
www.Gerad.ir</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/697577" target="_blank">📅 21:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697576">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/697576" target="_blank">📅 21:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697574">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
محققان: هوش مصنوعی و جنگ هسته‌ای می‌توانند تا سال ۲۱۰۰ بشر را منقرض کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/697574" target="_blank">📅 21:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697572">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای ترامپ : از همین لحظه، در جنگ میان روسیه و اوکراین آتش‌بس در حوزه انرژی برقرار می‌شود؛ هر ۲ طرف توافق کرده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/697572" target="_blank">📅 21:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697571">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuFbTtKopCj0_XqNonGmlBPb6xZxOC0f2QShPj8o6TAziXDmcwDxMkSsR13l3-zc7xDLbcDV5CCl6BSypM6NgCseQJZq9mGeZ2E9Kh1fZd6YbpVWz6B3H4dMmXAb2KqINEC58W1jo3PJohVMxw2mopDKqLkXgq6xM3crTP1ZQCO2RE5_k_QpfWsSFKsyMG4t-6OQEtfVaEYnzzQBwD1751RU3wALNLBVtITO5JBm_3ryy5X9xoQnS_v95eosBzOCfbDX3cuqI4WRxHyIEiJ6XbivX1DX4HMHZMTIjwr3e6PjmvMiglSvA8cD9BK0CmEDD0-GoeNjXPeYtC4uRuFalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از دنده اتومات چطوری استفاده کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/697571" target="_blank">📅 21:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697565">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOKP_BwCRncO6z4_TAqKZoY5a2qWRN68UXyHehJYmem8lX48mrfML4Eo5x7nV63uLFHtvGFgA1RT6aTrt3_4set4IYoqE9Jpg7jEaD3e_CIPRMBA8NOTVk_oR1RnuUdUV2zIEyrjLUmsXIWzXL6w7yedQnDF3KpWw4gtbF8Ge6IdtJpN1HckprfA0GWiHRAl8KCq_vyEmkFkCBq8PoRJEwhK78673VN2VDH2kvohdENq86T-sEu3dUyN3_4dwXvp0OZXgrhixt5Lq_14jpotLdQWHmzIfTtkpFcANV5vLCzsRWSayrerJuoOTKbP3KSX0m6si9PVs2VZdsMdtgpfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsICzV7j5ewKDrX64FgZT5pul1vwMmuIHdG3Rn3U6fUPQ7UFeW9idcyZ5TPxkrmSljKvRvsLtrDjLOCU3AHyrKHc4Kk9dqq8ZGaMchNCz3iBFiNoZs1Umevb04FxSAywBVRB28Po9AbVLU-jMw-TrqChOWEjqKcKcnZK9x3WSHTg25Hra3PW7QikFusyd5ZUt9icbpD7aCw76LV5CPV3vohyAegd_k67hGAEWzKOgTmDHeAx20wwCoU5dJFAQZpua30z5b1N6t1bN2XEFXIIIGooJVpHb-45JoCRUBJGxqny8NCtrgH4teipl0d8TtUVid3ylFkPsnLe4FXzWz9ZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UV44nkwG6entJLXsyvikRzbgiDyqxH-XOPt0lTIOqZzbyKT77SM50UC7XFsn24LWFZ4F3TgRUq2oTIw8cXJ0RyLyeR3_MvYghhvcpNLR-_SSEvoMTOIJOw8wKWpNG81vELWgYFuSIi-g9KPoO2M7q8Oo0giiqXopckxJ3hq4IlP_oCeyPdQREY5xFD99lWqGCquhMR5zARoGRIKjKhFxxk2TimOgxaez8ueOUx8T25cv8n-r05Fuj9c-4RoA5qC-Kz02Idi9COeN7e-W-l2mYQtUw6BsrRiJzBO_XLDjBCB9NX7aa7ztksYinkEhtAfLJDTYmnShCZ-PUVK1oyGSJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2e4wWjTgGXwDNgQGrSeuy0LFiyv_R_OSudFGu7bJqudN4etkimLJ-9n5r2Rd8pw_VUTQXPWqeV4YLYYt-pHQ7qSkLxfkoYEElE34YpgkBkzXs40MPccjKhGSSZ1YiB81WhdBYhGoyhg8o38npG-dxrXlBdtnSrxW89E9dU_nggbQZHFFvSRMBm5tPvmwq0Qy632d0PJdTVyHMTBWKEyHGFG-L58zTPg8nTTWOqXpQcSHRVZZfGWx2PJfodGBQn4kBbgclwrUP867yfckR6XI1CSZLtpLoO_aS4nYb-X-McyHZVvqaZHuXHqHvsiz6htUdGK_8p6tjRn_BKOtOwW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QB1PC9tFRiJWOYuM1XK-j7-libUmeyQlENf1VcN7ueBUMEyteEv_oghTpd2A6pBaHTSLJI8N5O2sapCRLH2vBDmPzgJW1DT7IfkN5ES1ItEmk0StvrZ0eM2zAdoVAp-sqCqhcChiQUMwgbrSbIcHZlpEKdEObpM13uVR2Li4hstNSxz7hTvXjp-mvw3ZPf9ht32SURQyIl1sbpGggqz2Df3Vs4uZsLeC4xoCWxRrUFj8vzXjkDTLTxGdfUFvQDs3zlEVlf9v-dkqFVZtMEvF8ipGFo-bIPUE62oXJH3dNI5okaUWaAQCv-AxuXo4yqs82q--jCIntHiVL6PuUodrfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
"پیام محسن رضایی و قالیباف خطاب به وزیر خارجه آمریکا" روی بیلبورد‌های شهری
در مقابل ایران زانو خواهید زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/697565" target="_blank">📅 21:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697564">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
مرشایمر: به نفع امارات و عربستان است روابط خصمانه ای با ایران نداشته باشند، امریکا دیگر نمیتواند از انها دفاع کند
نظریه‌پرداز علوم سیاسی:
🔹
از این به بعد هیچ کشوری در خلیج فارس جرات اقدام علیه ایران را ندارد؛ ایران خیلی قدرتمندتر از همه انها خودش را نشان داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/697564" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697563">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92dec01ca3.mp4?token=j2rLeCH4WI2As9qzTQCSfGxE6s-gF1vRytM2IiNFzvjjTP-Uws3DhzJN6SEJoFDrpGRI5xhFNQuC17HxTE8VjF6H5y-4y14mhSSI6qLPk6fFb32XolwvLNB2W8CsNcJabpNc1mgzkBzTAqhaw93IYSbtZCtgKRdDGyPpb7Rx1ITAbOWOwhEpSr9TA77dET-DX00kFPO11pZQpAJgFqIPY5eeKOOsDINvOBXqx5waYNAo4zItojgH4BgjZtZX8me8fDN08On5RmIx1czbVf52tIT5-ykVCRv3VHRrak8u2ycmduIVGRfpeAUeBGK6ixx-v5WJObns95JeEir8l_Jqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92dec01ca3.mp4?token=j2rLeCH4WI2As9qzTQCSfGxE6s-gF1vRytM2IiNFzvjjTP-Uws3DhzJN6SEJoFDrpGRI5xhFNQuC17HxTE8VjF6H5y-4y14mhSSI6qLPk6fFb32XolwvLNB2W8CsNcJabpNc1mgzkBzTAqhaw93IYSbtZCtgKRdDGyPpb7Rx1ITAbOWOwhEpSr9TA77dET-DX00kFPO11pZQpAJgFqIPY5eeKOOsDINvOBXqx5waYNAo4zItojgH4BgjZtZX8me8fDN08On5RmIx1czbVf52tIT5-ykVCRv3VHRrak8u2ycmduIVGRfpeAUeBGK6ixx-v5WJObns95JeEir8l_Jqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازهم فاجعه در فوتبال؛ کتک زدن داور این بار در اصفهان
🔹
این اتفاق در لیگ‌ زیر ۱۳ ساله‌های اصفهان افتاده است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/697563" target="_blank">📅 21:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697562">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5fee01983.mp4?token=BFIjz2nBF9kjZT4YZ1f8FfPqrP35TNeApnVc_ofgCWJ1O0q85V8qbsAVoSaDhAsXSTvo_0G5fB5oUtNXftKxIalA7a52gvL-GJgD8yTt2VhaYfWY9_8RjFEGfK4g0_CN2ldiECbZaRBCruPw23VpFSZZ3vs27B0DmBpheVpjHpQK69FLAWiL9sjw9nYQqr9wJDUeYJIN3UWzj3Tg1ZYH0lnNeSI4PBk-1rI7eg7ueLyuE87afVyjI5Yo1GlQfutISLOn9APOf27hs4OnfD8yqMHWAlAVf1DU5M13MKe8CipLs_FvEui7z0NgtIzJCN05gbu0AiZ6nlmOOdi5cc1d3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5fee01983.mp4?token=BFIjz2nBF9kjZT4YZ1f8FfPqrP35TNeApnVc_ofgCWJ1O0q85V8qbsAVoSaDhAsXSTvo_0G5fB5oUtNXftKxIalA7a52gvL-GJgD8yTt2VhaYfWY9_8RjFEGfK4g0_CN2ldiECbZaRBCruPw23VpFSZZ3vs27B0DmBpheVpjHpQK69FLAWiL9sjw9nYQqr9wJDUeYJIN3UWzj3Tg1ZYH0lnNeSI4PBk-1rI7eg7ueLyuE87afVyjI5Yo1GlQfutISLOn9APOf27hs4OnfD8yqMHWAlAVf1DU5M13MKe8CipLs_FvEui7z0NgtIzJCN05gbu0AiZ6nlmOOdi5cc1d3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرارگرفتن یک کشتی متخلف در سواحل امارات
🔹
به‌دنبال صدور بیانیه نیروی دریایی سپاه درباره انفجار نفتکش متخلف در خلیج‌فارس،‌ امارات هم از آتش‌ گرفتن نفتکش خود در این منطقه خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/697562" target="_blank">📅 20:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697561">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04822bdcc.mp4?token=acQDceWyOlDHUBaoCu2YtDBAv2a5fUG4hzbb-V2XRYLm4qrxDMEdCbQ-ydueFJLo5jMIJF44tAtTXRCEGndwKygkQyIEWrcKSsp2qipQESusedFc65nzBhf9RomoFDjWadZiqst3VAqfgeSAfj4UC8i9NxuvpXqDuZrkh26owMq97JmoDrXCcWtCp3t0VHxOnNiRzCz7Deb0ScfcUmHHltbUQQQ_SGI0trgb-jT8L8Jg2IaaRVs1GM7HXaeDSqtY3c7CvzSdlw1kvukgo_CLRPgkPBq5KxK9LUjIBTp9OdulcJ9u8M5yIW8cmHMY-Q0DP4aLdvGvUt0tFx_RRtGDyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04822bdcc.mp4?token=acQDceWyOlDHUBaoCu2YtDBAv2a5fUG4hzbb-V2XRYLm4qrxDMEdCbQ-ydueFJLo5jMIJF44tAtTXRCEGndwKygkQyIEWrcKSsp2qipQESusedFc65nzBhf9RomoFDjWadZiqst3VAqfgeSAfj4UC8i9NxuvpXqDuZrkh26owMq97JmoDrXCcWtCp3t0VHxOnNiRzCz7Deb0ScfcUmHHltbUQQQ_SGI0trgb-jT8L8Jg2IaaRVs1GM7HXaeDSqtY3c7CvzSdlw1kvukgo_CLRPgkPBq5KxK9LUjIBTp9OdulcJ9u8M5yIW8cmHMY-Q0DP4aLdvGvUt0tFx_RRtGDyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قهوه رو اینجوری بخور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/697561" target="_blank">📅 20:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697560">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec4ba8b0a.mp4?token=MtKrrhBuhBFeAuPSGMi2GDVjNQHY2g1eJggetX7XqjueoUngODKGJutPt1oOlz0AYIjwZHBanWOJ_IZ2d2Ph4RnSWNtz9E8QfAMozCzsdWYve40z-Jpn043Ijg-_o1FeDl39P0ZQx_QItgCYlvXZo2ICGnUHSUu9DPL5FG3bDX1Wrb6udooQiRxgOD9twp2FO_WXO-gzIsvAJPnmU5dozPID3rxXRajse4XRmzbGKgWdv0-M8T6sGD7LARG5EJoes0cqpMnM9DdVv01FhtZhYNRpwpMEyJ7ImEbHmQ0tMGay4oAMII8XsB71WKhbF0dSh1GPBgOC1x5rDJoeoMBwJh_K2K2dxoe16NzfBVZI-KEc11_R2hVkhlASvzAm8h_Q6TPQyD9SHeHutqfixgXCl9jvoQbwo_sVfHbYP4uqR1Vqe-DkImVTpelUMBHu0FYzAOR3bQAJn4M91w2aAsq-q7H25diTGP-jHVUqxHgLsHqnXmRT0eTT06UETRTS-DPWW8rB0M5a6kEbM12iveUnP9BuM6jx2naRJDLXZWCmOAtzDGISitlbFCmLU1tPyDX9wtxEb6B7Xv6QrnEUYyggHFNdVvT8stzkQoGi_23ZEjT5mqqfyGUt9ioUWLnF_2EtqalWvt1xVIPOkHjgC8-zm1Xf4_vX-mpStpy1pktfbZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec4ba8b0a.mp4?token=MtKrrhBuhBFeAuPSGMi2GDVjNQHY2g1eJggetX7XqjueoUngODKGJutPt1oOlz0AYIjwZHBanWOJ_IZ2d2Ph4RnSWNtz9E8QfAMozCzsdWYve40z-Jpn043Ijg-_o1FeDl39P0ZQx_QItgCYlvXZo2ICGnUHSUu9DPL5FG3bDX1Wrb6udooQiRxgOD9twp2FO_WXO-gzIsvAJPnmU5dozPID3rxXRajse4XRmzbGKgWdv0-M8T6sGD7LARG5EJoes0cqpMnM9DdVv01FhtZhYNRpwpMEyJ7ImEbHmQ0tMGay4oAMII8XsB71WKhbF0dSh1GPBgOC1x5rDJoeoMBwJh_K2K2dxoe16NzfBVZI-KEc11_R2hVkhlASvzAm8h_Q6TPQyD9SHeHutqfixgXCl9jvoQbwo_sVfHbYP4uqR1Vqe-DkImVTpelUMBHu0FYzAOR3bQAJn4M91w2aAsq-q7H25diTGP-jHVUqxHgLsHqnXmRT0eTT06UETRTS-DPWW8rB0M5a6kEbM12iveUnP9BuM6jx2naRJDLXZWCmOAtzDGISitlbFCmLU1tPyDX9wtxEb6B7Xv6QrnEUYyggHFNdVvT8stzkQoGi_23ZEjT5mqqfyGUt9ioUWLnF_2EtqalWvt1xVIPOkHjgC8-zm1Xf4_vX-mpStpy1pktfbZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاح کشتار جمعی زیر کت مکرون
🔹
رئیس‌جمهوری که برای ترسناک به نظر رسیدن، به‌راحتی آزمایش اتمی انجام میده و دنیا رو تهدید می‌کنه! اما واقعا چه کسانی دارن امنیت جهان رو به خطر می‌اندازن؟
🔹
جزئیات رو توی این ویدئو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/697560" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697559">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YccbDzWAFyzEd-19rY_xMa7c9-YyJjNNrdF5zxcf9QdbinUNnkkkljvQ4Is8hiNkbiS3BzdyJ_p-rbiUfAAySV1X383kSutW2VclTsL5lZXClwxavotmmFhtmM2ll1rjUZAUd_D3tZpj1hQyBThr3ws2P7g6Vs4MdS5AGHwgchD9mkUiv-5kvXUwb0eXnZUJ7PYzLlb8bE8W7UCHrjRIicLuW82wFULWbwVVeH0jdsIkoFqLuFOy0zXMLA2_L1x0BntgSGYbANsEx4VFPIhBxnQZIvIZd5oqCcangkh00rncS0JElIHvm6UBHjas5wYssDTiswuknrEA27jP7YnZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان صف تسویه در میلی/ ۱۳ همت پول به کاربران واریز شد
🔹
میلی از پایان صف درخواست‌های برداشت کاربران خبر داد. بر اساس اعلام این پلتفرم، از ۲۰ شهریور تا ۱۸ مهرماه، بیش از ۱۳ هزار و ۲۱۳ میلیارد تومان از مطالبات کاربران تسویه شده و ۶۹۶ هزار درخواست برداشت با موفقیت انجام شده است.
🔹
همچنین ۲۶۳ هزار درخواست برداشت از سوی کاربران لغو شده و تمامی درخواست‌های معوق از طریق تسویه ریالی تعیین تکلیف شده‌اند. با پایان صف، تسویه درخواست‌های جدید طبق روال عادی ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/697559" target="_blank">📅 20:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697558">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c020369ef.mp4?token=oxO_C6uQ9ce_E7Satgz5PQrQk_lXJq6CzrRq6gqnBl6DG0ytoWgaEKoSXNUF6TQAlvTi9sg8oKlfUu3BqxJKjYhrH-DrjehM24r07bqUK-zYyK9JU4F3lLDKtYYXM9vDl8FeF8k9_TFKQz_P1VqQgYb0QY6_HYMx3JTVWKksKsK-V65Pos73h28iHD0VpZQY9alhsfkkihIKxsEZvAvJZ5qQfj_aAY0fqupuLBLNFqminZTMCRVLNt3aqsqnDbKUCCHUo1mHxX2gUmiTNUz3GU7TXIYrUzF0BMUynFZzAYy98Ez-CLvyjuIUqwSAWI8gRc3Ro7UshJMCs7Ssc9DjJamhS3nqwt7CT8RKRNSqbSIkHQecTndpwsUdSNVWlV0R95RILbi3Pe3cle_FIqin418wSe72JZd_6jSR8VFORCMLumPTSXmhP4q9fzsWx99aQeA82TXhILbexLbNTt3H53wHxn26OyXuk6kUwjUTXxqzAGjyczqdC4C86RGferpUezy7OQJ5yOzfRTc-SSXjGcc0j8huS3Rh-x5y16NdyijZasXKVRiXmR9oBgM9_z3hmTSopB0lG4r5XBQ4FGa3vdxFagzTUKZaL0yO9gBusclVPgbAchMIlBVFhFGLG8vqwsjjzAuTfITLLXdz2Vi_PbfOdLjMosqyGFdv7kMSnyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c020369ef.mp4?token=oxO_C6uQ9ce_E7Satgz5PQrQk_lXJq6CzrRq6gqnBl6DG0ytoWgaEKoSXNUF6TQAlvTi9sg8oKlfUu3BqxJKjYhrH-DrjehM24r07bqUK-zYyK9JU4F3lLDKtYYXM9vDl8FeF8k9_TFKQz_P1VqQgYb0QY6_HYMx3JTVWKksKsK-V65Pos73h28iHD0VpZQY9alhsfkkihIKxsEZvAvJZ5qQfj_aAY0fqupuLBLNFqminZTMCRVLNt3aqsqnDbKUCCHUo1mHxX2gUmiTNUz3GU7TXIYrUzF0BMUynFZzAYy98Ez-CLvyjuIUqwSAWI8gRc3Ro7UshJMCs7Ssc9DjJamhS3nqwt7CT8RKRNSqbSIkHQecTndpwsUdSNVWlV0R95RILbi3Pe3cle_FIqin418wSe72JZd_6jSR8VFORCMLumPTSXmhP4q9fzsWx99aQeA82TXhILbexLbNTt3H53wHxn26OyXuk6kUwjUTXxqzAGjyczqdC4C86RGferpUezy7OQJ5yOzfRTc-SSXjGcc0j8huS3Rh-x5y16NdyijZasXKVRiXmR9oBgM9_z3hmTSopB0lG4r5XBQ4FGa3vdxFagzTUKZaL0yO9gBusclVPgbAchMIlBVFhFGLG8vqwsjjzAuTfITLLXdz2Vi_PbfOdLjMosqyGFdv7kMSnyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/697558" target="_blank">📅 20:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697557">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تغییر جدیدی در روند مذاکرات غیرمستقیم ایران و آمریکا رخ نداده است
🔹
بررسی پاسخ آمریکا به طرح ۷ ماده‌ای ایران در داخل کشور ادامه دارد و پیش‌بینی می‌شود این پاسخ طی چند روز آینده از طریق میانجی قطری به آمریکا منتقل شود./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/697557" target="_blank">📅 20:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697556">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
بدون نظریه اینشتین، مسیریاب گوشی شما روزانه چندین کیلومتر خطا داشت!
🔹
ماهواره‌های GPS با اندازه‌گیری زمان حرکت سیگنال‌ها، موقعیت شما را تعیین می‌کنند؛ اما ساعت آن‌ها به‌دلیل تفاوت گرانش و سرعت حرکت، روزانه حدود ۳۸ میکروثانیه سریع‌تر از ساعت‌های زمینی کار می‌کند.
🔹
نور در این مدت بیش از ۱۱ کیلومتر حرکت می‌کند! بدون اصلاح این اختلاف زمانی با استفاده از نظریه‌های نسبیت خاص و عام اینشتین، خطای GPS به‌سرعت افزایش می‌یافت و مکان‌یابی دقیق مختل می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/697556" target="_blank">📅 20:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697555">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
مهلت انتخاب رشته کنکور ۱۴۰۵ تا پایان روز دوشنبه ۲۰ مهر تمدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/697555" target="_blank">📅 20:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697554">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e933c02e46.mp4?token=Y3QYQ_piPHfiu7spwZuEQc9g1oIA-UqU1VKZYLWWncqB0jcWnRvLXgrabhk-vZqPMhMd7Nj76N5g-gIsJSFACV3gOKz4mISQPquepNbGVV0L8X628Ca2kWaISdCzF4saK9Rw_c5d8HSj2f6YZAKtSSrsyTPboz2vpPAoKarcD3pzAjYho3skJrM2aI7Kprlb-4BQ-hKQkiTu8Q47Nu1C82ub4Fw_iiRvixp2BCXI3eb3MIQxm2gx7WsMXD6kl73KjkQICMW3xA95SPK92lAPSozE-Hm6zrshgcv0bDelCLJUnw8iFue6YUJfE3ifNqgRPGy-EYq69Ir23v_uveqknQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e933c02e46.mp4?token=Y3QYQ_piPHfiu7spwZuEQc9g1oIA-UqU1VKZYLWWncqB0jcWnRvLXgrabhk-vZqPMhMd7Nj76N5g-gIsJSFACV3gOKz4mISQPquepNbGVV0L8X628Ca2kWaISdCzF4saK9Rw_c5d8HSj2f6YZAKtSSrsyTPboz2vpPAoKarcD3pzAjYho3skJrM2aI7Kprlb-4BQ-hKQkiTu8Q47Nu1C82ub4Fw_iiRvixp2BCXI3eb3MIQxm2gx7WsMXD6kl73KjkQICMW3xA95SPK92lAPSozE-Hm6zrshgcv0bDelCLJUnw8iFue6YUJfE3ifNqgRPGy-EYq69Ir23v_uveqknQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در نهایت متوجه میشی که مسیر سخت، تنها مسیریه که ارزش طی کردن داره …</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/697554" target="_blank">📅 20:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697553">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e753101023.mp4?token=b8hyg6gaiR-06qr9yn5rstgP18bcuD-ykJ6viwlKHKFZFTBLoLdq-fnTE1evGv6pp5VFOFiQy6tgOmjRqzjt1gnWbOsFq8wMngi9cfcQKKeMBTXPD1txfo5ve5ycr6ino0omNWMTN5AT0O2uPfhFHd34brdALQQ4XI-LOydfIrMqCqitTN0OXGf0josKCxOqPS9aKba_pNQo8snKRcsCw7aVnupUnxd4fJhNF5g6wOtEYrEmPpuZa1pwt2XDIbN1PHs20lNBuXP1rQ9obKlOWRaQ_XHPJTAErNv5aOYv4BUv78odRB1ksoc0mHrM28tok85btTZtPv9hqwUGk1PSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e753101023.mp4?token=b8hyg6gaiR-06qr9yn5rstgP18bcuD-ykJ6viwlKHKFZFTBLoLdq-fnTE1evGv6pp5VFOFiQy6tgOmjRqzjt1gnWbOsFq8wMngi9cfcQKKeMBTXPD1txfo5ve5ycr6ino0omNWMTN5AT0O2uPfhFHd34brdALQQ4XI-LOydfIrMqCqitTN0OXGf0josKCxOqPS9aKba_pNQo8snKRcsCw7aVnupUnxd4fJhNF5g6wOtEYrEmPpuZa1pwt2XDIbN1PHs20lNBuXP1rQ9obKlOWRaQ_XHPJTAErNv5aOYv4BUv78odRB1ksoc0mHrM28tok85btTZtPv9hqwUGk1PSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مدیرعامل پرسپولیس به پیشنهاد استقلال برای از سرگیری جام حذفی: قاعدتا نمی‌توانند مسابقات را از سر بگیرند وگرنه لیگ هم باید ادامه پیدا می‌کرد
پیمان حدادی، مدیرعامل باشگاه پرسپولیس در
#گفتگو
با خبرفوری:
🔹
بحث ادامه جام حذفی را دوستان فدراسیون باید بررسی کنند اما فکر نمی‌کنم عملی شود، زیرا آن فصل تمام شد و فدراسیون و سازمان لیگ به AFC اعلام کردند که مسابقات لیگ و جام حذفی، نیمه  کاره تمام شدند و قاعدتا نمی‌توانند آن مسابقات را از سر بگیرند و اگر به این شکل بود، لیگ گذشته هم باید ادامه پیدا می‌کرد.
🔹
فکر نمی‌کنم که اختلاف امتیاز زیادی در لیگ گذشته وجود داشته باشد، اگر مسابقات ادامه پیدا می‌کرد، حتما در صدر جدول شاهد تغییر در رتبه‌بندی تیم‌ها بودیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/697553" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697552">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/697552" target="_blank">📅 20:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697551">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌
♦️
دبیر شورای‌عالی امنیت ملی: آمریکا دارایی‌های بسیار گران‌قیمتی در امارات و پیرامون تنگهٔ هرمز دارد که ما هنوز آن‌ها را در میان اهداف خود نگنجانده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/697551" target="_blank">📅 20:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697550">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d86d3bae.mp4?token=iK_mL8CAYf6UV56tRmDuQa3TXRS_8Vr6vNRocX7Dly7u-vnUlr-lEzujC65cxiDKp1addmpajN31En0uPEIVOYndODncN8jvLgEPihiKmPmWEtAC_hvaVHfG-brBxyPswz99j8mYbhJbOcfQc20-hWUAr6My7CEbb88ODVlgEbunwyqmrMa7mp7L9Dss2gyCRZq0Mbmc4sBhg83u7aWwt5-BuSMpCoE5164cwP3SvAwtggQGGznswScGvzKMXJNRCXdKurqXtwwhNhNq8fmKs31Mo30-ZlB0CoBNa9dIuFuUmDQv0lozpzQ874qFrOdBcBIyHPzobNhT3INNcF_VUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d86d3bae.mp4?token=iK_mL8CAYf6UV56tRmDuQa3TXRS_8Vr6vNRocX7Dly7u-vnUlr-lEzujC65cxiDKp1addmpajN31En0uPEIVOYndODncN8jvLgEPihiKmPmWEtAC_hvaVHfG-brBxyPswz99j8mYbhJbOcfQc20-hWUAr6My7CEbb88ODVlgEbunwyqmrMa7mp7L9Dss2gyCRZq0Mbmc4sBhg83u7aWwt5-BuSMpCoE5164cwP3SvAwtggQGGznswScGvzKMXJNRCXdKurqXtwwhNhNq8fmKs31Mo30-ZlB0CoBNa9dIuFuUmDQv0lozpzQ874qFrOdBcBIyHPzobNhT3INNcF_VUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند، قدیمی‌ترین لکه‌های چربی هود و کابینتت رو ازبین ببر! #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/697550" target="_blank">📅 20:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697549">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-o1czF6Z7l8zOSlA5SDPnN65uZqbCV-53_mz6_LWD1ob6uFrw2dUQd8eq2zPmNSH6Bu9xlh859jebfoY8KIdokFb7ZWm28c9t7SVcPtKenXJfUQUEmVBOTWB-bwh0WNhHrq_BjKOKvai2_LVJKAAUR7Sw94tKtGM99GL2yJ7pGQY_mWloZa2eTF0dw5O1FUDpkJE6x-IDx45yZXQK9WKT_VLsO68K7G2w55ais_v_tHU4WxE4DOgk_tQ__GTJnoySgFW5lTem-4Ksc_LqudL0k7wRau59VGfD1Lutj_IKrak9aChWFtD_nMcGGXb1k0cpT3jelDIiP0HdkQHU-y3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه آبگیر با سه رنگ متفاوت گیلان زیبا
🇮🇷
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/697549" target="_blank">📅 19:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697548">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYmQnQ2PN_s0OZr4crEil-fMiJ6Fim3leyhrmk_Ia7XvOuaXTP9GunIZ_tbIUJQ_-VhSXXEwJDAbUXT-LHoiRs2Mkwkewv9tRmmmT4sbcFSMIR_MCL2O-1-qvAEStMkWcaalM-i2QbROLqKcfR-KmCvC-ntaYr_LLcdA5h-IWhzljZtbdpEuzQhG8fYevO6-K4fIRmczyl4rDnK1d-JnLcJ7ay0dp1BOetHqSE9vuKQRKinA-F4wpuFsWkU2d8EcLZR0y1fLTHo2UML8fSpKTfSRcTZB0KiwTIC-lpe29447hWgnb2U9GOUjbLZOPTrhhb4TC8foS1k8sgdcIJf2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران نه، ریاض
🔹
پس از ۸ ماه جنگ آمریکا علیه ایران، دامنه‌درگیری‌ها به دیگر نقاط منطقه کشیده شده است. آمریکا که به دنبال مختل کردن پروازهای ایران و اعمال محاصره هوایی بود، حالا در پی تشدید درگیری‌های انصارالله و عربستان، با توقف فعالیت فرودگاه ریاض و لغو گسترده پروازها روبه‌رو شده است. این تحولات بار دیگر یک واقعیت را یادآوری می‌کند، در خاورمیانه صلح و آرامش یک‌جانبه معنایی ندارد، یا صلح برای همه است یا برای هیچ‌کس. جنگ‌افروزی آمریکا اکنون بیش از هر زمان دیگری پیامدهای خود را نشان می‌دهد، پیامدهایی که از مرزهای ایران فراتر رفته و دامن متحدان منطقه‌ای آمریکا را فرا گرفته است.
🔹
هشتصدوهشتادوسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/697548" target="_blank">📅 19:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697547">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
لایو ای‌آی‌اس به نقل از ملوانان نفتکش‌ها در تنگه هرمز: اسکورت‌های آمریکا دیشب پس از حمله به یک کشتی، در میانه راه متوقف شدند
🔹
دو کشتی خروجی پس از حادثه امنیتی، مسیر خود را تغییر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/697547" target="_blank">📅 19:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697546">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcff288f73.mp4?token=tbpMFe0P-XPw-khlCkcDCmeSyma5ihQLzGvEix7XsdNzvG1Cg5dER8dpcdWMeIYYsZSPrT-YbrvPcfjJmSIAwAB99lT0YGZqNiFWqu_0wJr5PcK3RcLrwviIne6rIKN6rEw_k3D7PDhv5dYMv4AF2OQTzZiPThO52XANxm8Gnzc4wF-c2_vAv5TVu-Y1loJGKxsyOZvKgGxTR_Huiy8fA6oVFypIiBefxT98t7I3fcbX7JbcDRJxzPz66vH-lMUZsELCdYeDAzMRgIpY7Kv9Us0s1trqSuZDBm3Q8d8ZiCs2TPt8li_VD1BrFRZEw2hNXNjvLSru_liKyy_l04Yvsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcff288f73.mp4?token=tbpMFe0P-XPw-khlCkcDCmeSyma5ihQLzGvEix7XsdNzvG1Cg5dER8dpcdWMeIYYsZSPrT-YbrvPcfjJmSIAwAB99lT0YGZqNiFWqu_0wJr5PcK3RcLrwviIne6rIKN6rEw_k3D7PDhv5dYMv4AF2OQTzZiPThO52XANxm8Gnzc4wF-c2_vAv5TVu-Y1loJGKxsyOZvKgGxTR_Huiy8fA6oVFypIiBefxT98t7I3fcbX7JbcDRJxzPz66vH-lMUZsELCdYeDAzMRgIpY7Kv9Us0s1trqSuZDBm3Q8d8ZiCs2TPt8li_VD1BrFRZEw2hNXNjvLSru_liKyy_l04Yvsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساخت گل‌های زیبا و دست‌ساز با وسائل دم‌ِدست
🌼
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/697546" target="_blank">📅 19:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697545">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=g8nEuwJoqEwR6Y8jsVOAo8dPyfn5WrjZny9rmMkpATcZOwdQw0-OZJU2mq3WvkNpRxIWSMp95nLMWICYjgqmJU6DUMlgUyvhlUjSekq9aWH3GaX0iOWsaBWtwa2dXKm3XE5q4xh7KWJR8ZOSBse6ARBgjlmnR5IXsrph6oWIaEJDdws6YVdmmSfZdtSQu12uweLy0NEujjlZ3IIr0IItA1VvKCqJj4g-CMYZ6KAshSKLGylyqGEcEcSFfyIUZCuebEhfPx4Cr3R__5uYaEnhJfatS56GIjXKw20hcuLOgvbnjW84I12sOilVxwWkokSg7gMbMFf-xinim_z_1uvuBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=g8nEuwJoqEwR6Y8jsVOAo8dPyfn5WrjZny9rmMkpATcZOwdQw0-OZJU2mq3WvkNpRxIWSMp95nLMWICYjgqmJU6DUMlgUyvhlUjSekq9aWH3GaX0iOWsaBWtwa2dXKm3XE5q4xh7KWJR8ZOSBse6ARBgjlmnR5IXsrph6oWIaEJDdws6YVdmmSfZdtSQu12uweLy0NEujjlZ3IIr0IItA1VvKCqJj4g-CMYZ6KAshSKLGylyqGEcEcSFfyIUZCuebEhfPx4Cr3R__5uYaEnhJfatS56GIjXKw20hcuLOgvbnjW84I12sOilVxwWkokSg7gMbMFf-xinim_z_1uvuBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیرعامل پرسپولیس: در ازای هر گلی که بزنیم، یک نفر را آزاد می‌کنیم/ در این فصل ۴۳ زندانی آزاد شدند
پیمان حدادی، مدیرعامل باشگاه پرسپولیس در
#گفتگو
با خبرفوری:
🔹
از آذر ماه سال گذشته، باشگاه پرسپولیس به عنوان بزرگترین تشکل مردمی غیر دولتی کشور، کمپین مهر سرخ را شروع کرد و در این پویش یکی از کارهای اساسی و بزرگی که به کمک هواداران انجام دادیم، آزادسازی زندانیان مالی جرائم غیر عمد است.
🔹
سال گذشته در استان تهران، ۶۰ نفر از هم‌وطنان که در زندان‌های تهران بودند، آزاد شدند و در ماه گذشته، در بازی پرسپولیس - استقلال ۶ نفر دیگر از هموطنان آزاد شدند.
🔹
امروز در آستانه بازی هشتم پرسپولیس در لیگ، در شهر آقا امام رضا (ع) نیت داشتیم که ۸ نفر دیگر را آزاد کنیم، اما به کمک خیرین، این ۸ نفر به ۳۷ نفر افزایش پیدا کرد و مجموعا طی این پویش ۱۱۰ نفر را آزاد کردیم.
🔹
از ابتدا این فصل قرار شد به ازای هر یک گلی که یکی از ۶ تیم فوتبال پرسپولیس می‌زند، تحت عنوان گل آزادی، یک نفر را آزاد کنیم و در این فصل ۴۳ زندانی آزاد شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/697545" target="_blank">📅 19:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697544">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517f29697b.mp4?token=QMBd5s6RGMabmmbido5KL_U8rfy-vuz09tvk07f0ci28MR_JjvuWIEuPJtRD851oG_F_qi7tdJ72U6ZCZFSLmeoEy72-dr8_zBtDWV_S6MjeVVcYDCkOyTLcxqxy0NFcSoMPpyYetTglRqrAE_M_VnVzOXAmb2M6EsOtQdH3C1xOH6yYDfX3QrQKLVUX7198GH-0yOaB6iOZZGS0rjnF7gPKGW8c4AEaltMXtZ71F8zmSh5FNwpDLTUzUWQP4NL-HDImar7QDGVeQyNHgcl1z2pKTXvz5TNJNEkx1uBjKBcLjID60_97syH1rektxBgtxROESRf7wIgPCW-92X7GHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517f29697b.mp4?token=QMBd5s6RGMabmmbido5KL_U8rfy-vuz09tvk07f0ci28MR_JjvuWIEuPJtRD851oG_F_qi7tdJ72U6ZCZFSLmeoEy72-dr8_zBtDWV_S6MjeVVcYDCkOyTLcxqxy0NFcSoMPpyYetTglRqrAE_M_VnVzOXAmb2M6EsOtQdH3C1xOH6yYDfX3QrQKLVUX7198GH-0yOaB6iOZZGS0rjnF7gPKGW8c4AEaltMXtZ71F8zmSh5FNwpDLTUzUWQP4NL-HDImar7QDGVeQyNHgcl1z2pKTXvz5TNJNEkx1uBjKBcLjID60_97syH1rektxBgtxROESRf7wIgPCW-92X7GHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیلی از خوراکی‌هایی که روزانه میخوریم احتمال ابتلا به کبد چرب رو افزایش میده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/697544" target="_blank">📅 19:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697543">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714574dcee.mp4?token=YGF4hr1ox2ii3l8NW9cwi0rOJgEG40vH7v5huskwoGjlTBvLpQzuDTrq-jPsLt93x0X5ZI9ZosHZphcbyvWJNoPFwKXaQlhB79R_J0lA2KmXISAKTZc5PkwdFCPgR7Y3StNK5s-tvZ42P0_YUjJb82Ln_00oD4YCknIviO8qWovTXf4YBtMhFdSVMiI92agM6ERi1IgI3xb_uu5JAvb_miazl1yx_vuiInG8DAK48oBwOzexBsn_9zeVKGCgQH3To4iJTzuU1qgGMmDOe2ZNyCRWXk2TptQuUfdFK6msPHNPYOHZtyh-ar2Xs1D0cLLeiH_dGSeZhemKrfcWPrQyrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714574dcee.mp4?token=YGF4hr1ox2ii3l8NW9cwi0rOJgEG40vH7v5huskwoGjlTBvLpQzuDTrq-jPsLt93x0X5ZI9ZosHZphcbyvWJNoPFwKXaQlhB79R_J0lA2KmXISAKTZc5PkwdFCPgR7Y3StNK5s-tvZ42P0_YUjJb82Ln_00oD4YCknIviO8qWovTXf4YBtMhFdSVMiI92agM6ERi1IgI3xb_uu5JAvb_miazl1yx_vuiInG8DAK48oBwOzexBsn_9zeVKGCgQH3To4iJTzuU1qgGMmDOe2ZNyCRWXk2TptQuUfdFK6msPHNPYOHZtyh-ar2Xs1D0cLLeiH_dGSeZhemKrfcWPrQyrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دانشگاه فردوسی مشهد:
روایت تحول و تغییر رویکرد خاص در معاونت علمی، باید مورد توجه نخبگان کشور قرار بگیرد.
🔹
عبدالرضا جوان‌جعفری، رئیس دانشگاه فردوسی مشهد، با اشاره به اهمیت سخنرانی دکتر حسین افشین، معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، درباره «تغییر پارادایم معاونت علمی»، از نخبگان، استادان و دانشجویان دعوت کرد این سخنرانی را با دقت بشنوند.
🔹
این دعوت، بر اهمیت تبیین رویکردها و سیاست‌های جدید در زیست‌بوم علم، فناوری و نوآوری کشور و ضرورت آگاهی جامعه دانشگاهی از مسیر تحول در معاونت علمی تأکید دارد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/697543" target="_blank">📅 19:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697542">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
محسن رضایی خطاب به روبیو: قدرت‌های بسیاری در طول تاریخ رؤیای اشغال ایران را داشتند، اما نامشان از تاریخ پاک شد و ملت ایران همچنان باقی ماند
🔹
هرچه بیشتر علیه ایران تلاش کنید، بیشتر در باتلاق فرو می‌روید و بار دیگر در برابر ملت ایران زانو خواهید زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/697542" target="_blank">📅 19:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697541">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 اگر بخواهید یک مشکل اجتماعی را در محله خود حل کنید، کدام را در اولویت قرار می‌دهید؟</h4>
<ul>
<li>✓ آلودگی و نظافت</li>
<li>✓ امنیت</li>
<li>✓ کمبود فضای سبز</li>
<li>✓ کمبود امکانات ورزشی و فرهنگی</li>
<li>✓ آسیب‌های اجتماعی</li>
<li>✓ فرسودگی معابر</li>
</ul>
</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/697541" target="_blank">📅 19:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697540">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/697540" target="_blank">📅 19:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697539">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
محسن رضایی: می‌توانستیم تنگه هرمز را کاملاً ببندیم، اما به دلایل انسان‌دوستانه این کار را نکردیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/697539" target="_blank">📅 18:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697538">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499fae8935.mp4?token=QKUuflA8n1cF32XbkaaX-_1-iHP4aeE5c6aZWQLlbkEtejNak4ElKku1lMGHq0fO3t9bI9t-1sokWDL_BYPoBzLte7cniAXyHrvJniqqHQ6LcGTM3dmfz9_6AnKMFbTi6YDsqo60ntB4mIrt4XzhbHdB32w-fxfdhabKOMJh3afJoSOI_DfPUaO5lq7uEhzNJQhQG4Lfkd_OIIdWlVQvsgOeVckEM2duVQe2Ko90ewvp3fuJGdmknsjr42RJ_vjr455RDFNLIS2OxY094nvSaPUxrB8DNpRb53xjXNMZ17aWwAyc5ysXSEJ-gPMWW9XSldj8VFDOBVGibyh8nwVT3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499fae8935.mp4?token=QKUuflA8n1cF32XbkaaX-_1-iHP4aeE5c6aZWQLlbkEtejNak4ElKku1lMGHq0fO3t9bI9t-1sokWDL_BYPoBzLte7cniAXyHrvJniqqHQ6LcGTM3dmfz9_6AnKMFbTi6YDsqo60ntB4mIrt4XzhbHdB32w-fxfdhabKOMJh3afJoSOI_DfPUaO5lq7uEhzNJQhQG4Lfkd_OIIdWlVQvsgOeVckEM2duVQe2Ko90ewvp3fuJGdmknsjr42RJ_vjr455RDFNLIS2OxY094nvSaPUxrB8DNpRb53xjXNMZ17aWwAyc5ysXSEJ-gPMWW9XSldj8VFDOBVGibyh8nwVT3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/697538" target="_blank">📅 18:49 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
