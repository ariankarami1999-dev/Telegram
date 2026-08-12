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
<img src="https://cdn4.telesco.pe/file/ijZjUCWOaUGUBrkIKEiBM-LB4InkCqHDMKWELpCmjfsxy8JxFwUGFngdG57_LyIojg-36d2Yw8HLDSX-KUJGfui_uvvgfNtXP_VBQmtISnAj81pi6z7Qozoiyw94bibFykJCTKqqJkHu65CJaXYFNoKgXd6cI_pPbvCLfPCO7_DjjUbla6uEe9qf-1006_dBPf7LCYzCSBXa70oB4rymLwaBjQqNNcSl3-aDmeNwJg-3aIOMAs96Un5AgIZUxgh3Zo1TGDxLERCTJI7_TYhKnmxqooRba0HBh5I_xXJFFtKH6coKxR_OOsSDYztMuWob3J1IfDWg_mLTnUCV30Ew-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 16:17:19</div>
<hr>

<div class="tg-post" id="msg-680603">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
دادستان اردبیل: افرادی که در انظار عمومی وضع پوشیدن لباس و آرایش‌شان خلاف شرع و یا موجب هتک عفت عمومی یا موجب ترویج فساد باشد، شناسایی خواهند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/akhbarefori/680603" target="_blank">📅 16:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680601">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFMjP6IILqWo2gsczM2tT72r1IKY7p2ZhRALm8wCmeo82PRkJTH0NNdJKWT3GgYqTplN7QzTasIFQuxD8KqllmopIXuOmoal_6cGCtgfyZz3-Fmm1KLaESZT40Vukeu4FBsOEmbhZiJluTDw6nMZGg8IbALSW_ZBkOYzoHJa1m_QS3Btpo0W7bLi_goZxqvAWPRVcfE7ilm1fHKjPfh_0Wwy1hzSzAb6TH1dzsxmrM54yhByxw9jf8nojf6uoH7WD8pQa-FLqsC32yJ5AW93SFSdGUHjsmdVACpOjIcdnZDRLTAqDPan15Fr5GCj3X_DOKM38heHRl0eT_OVxlGqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7caed88b4e.mp4?token=GaaGSqnMgvki-9bu805wylOTT5aj-677-LRq_vruYAIEdgGMfdFea7_1g1c2ks4VLE0BH8Ix4IRcrw9akRiSLeDtO_hZ7xd--qsOulOr-FRSF1LXuj8m4gPrt7XjII1TA8gyR2cMIACFIH-Y2DKu3m8CsKAaXFmXImiBOQEpeGRX85CFuA2Q8iCfGDDb0D46sLSYh8ZWGW9IV_OyYZvFf6dMSYIVb5XqUAsMazBxORdNizwQ4my4Qb4MI58VcLUf4ADfWgqbLDYxiK4ip5blYymXwaLeHPUa5yfs1VRgLxPYKg7i_2sHG3Wj_nRK1-2zzfSU2AdCvfUDsl6a0J7ldA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7caed88b4e.mp4?token=GaaGSqnMgvki-9bu805wylOTT5aj-677-LRq_vruYAIEdgGMfdFea7_1g1c2ks4VLE0BH8Ix4IRcrw9akRiSLeDtO_hZ7xd--qsOulOr-FRSF1LXuj8m4gPrt7XjII1TA8gyR2cMIACFIH-Y2DKu3m8CsKAaXFmXImiBOQEpeGRX85CFuA2Q8iCfGDDb0D46sLSYh8ZWGW9IV_OyYZvFf6dMSYIVb5XqUAsMazBxORdNizwQ4my4Qb4MI58VcLUf4ADfWgqbLDYxiK4ip5blYymXwaLeHPUa5yfs1VRgLxPYKg7i_2sHG3Wj_nRK1-2zzfSU2AdCvfUDsl6a0J7ldA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مبارزه عجیب سنگاپور با تب دنگی با کمک هوش مصنوعی
🔹
سنگاپور برای مقابله با تب دنگی، هر هفته بیش از ۱۰ میلیون پشه نر حامل باکتری Wolbachia را در شهر رها می‌کند. این پشه‌ها با ماده‌های وحشی جفت‌گیری می‌کنند، اما تخم‌های حاصل به پشه تبدیل نمی‌شوند و نسل پشه‌ها کاهش می‌یابد.
🔹
در این طرح، دوربین‌های مجهز به هوش مصنوعی میلیون‌ها پشه را اسکن و نرها را از ماده‌ها جدا می‌کنند. پشه‌های ماده‌ای که احتمالاً از سیستم عبور کنند نیز با دوز کم اشعه ایکس عقیم می‌شوند.
🔹
در نهایت پشه‌های نر با خودروهای مخصوص در مناطق مختلف رها می‌شوند تا با نرهای وحشی برای جفت‌گیری رقابت کنند؛ روشی که با هدف کاهش جمعیت پشه‌های ناقل بیماری به کار گرفته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/680601" target="_blank">📅 16:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680600">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef213bb96.mp4?token=VFlfEo757WwJbuAYe2yKsGtxY0pk2fqZCGMnhcUTqD93aF9tzNHUK3Y5_Ff6PZtTCwaaoeHn5XTCVvygombq4j-yVIBnRdu93zpyywmWhxcEss4-8mLZ7geTDVzBfX93heV9_MOB7tYzMcBJCqiOcNcZLWK8EsYPmU3v0_YScV1X4vmMlBKNeLHzH0HMLBFqkuPT3gyo_WGgupNcUN-cNdotsBQcig8B4DPZkZlC7z_WH1xNC7-gdfkfTxmpidTReh0vV1pPVrSO0Pnw6huEVjpMlc9F9nwOB2P0gDhaGwH79m_jlWJRuSGSshs0acWJWIduJ9I4vdgCWMNxXTKilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef213bb96.mp4?token=VFlfEo757WwJbuAYe2yKsGtxY0pk2fqZCGMnhcUTqD93aF9tzNHUK3Y5_Ff6PZtTCwaaoeHn5XTCVvygombq4j-yVIBnRdu93zpyywmWhxcEss4-8mLZ7geTDVzBfX93heV9_MOB7tYzMcBJCqiOcNcZLWK8EsYPmU3v0_YScV1X4vmMlBKNeLHzH0HMLBFqkuPT3gyo_WGgupNcUN-cNdotsBQcig8B4DPZkZlC7z_WH1xNC7-gdfkfTxmpidTReh0vV1pPVrSO0Pnw6huEVjpMlc9F9nwOB2P0gDhaGwH79m_jlWJRuSGSshs0acWJWIduJ9I4vdgCWMNxXTKilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛑
مغازه‌دارا و فروشنده‌های پوشاک، مشتریات منتظرن...
✨
مدل‌های ترند و پرفروش
💰
قیمت عمده واقعی
🚛
ارسال سریع به سراسر کشور
📦
خرید مستقیم و بدون واسطه
اگه دنبال سود بیشتر و جنس پرفروش هستی،
همین الان وارد کانال شو و لیست مدل هارو ببین
👇
🔥
تولید و پخش نیکلین (منگو سابق)
https://t.me/nikleinn
https://t.me/nikleinn
https://t.me/nikleinn
https://t.me/nikleinn</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/680600" target="_blank">📅 16:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680599">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgUSL3WhHCvli6PiGURQBMrvQZu8IzRBEI4DM1lGRnmaobA_P60mWiDqfi5pOcuh_7WH4AeYP_HWruCaXdFKKmQ6srElj9v_kZVAh71E197FIWhUpplL8MOQQwhJsBsD9Yoc1tLC9uFrgLpBU2wDAn9xdk3V_1ywp9ewOV9iar7yeRTNsW7SLtrkNfvMeOib7ibM0Bylc4NI6i4ZFwOkxJn5gafazOLV7n2xyXqEXvlhhOE11wIJT5c9bx_h3t_NVp5Uf9SDfZkDz3NLQPTalVEIRcjIDiolXkm4IFzOWoM4YVAtejOdgA0lbwHg1F3id6_MPVacqs3UWxgdIRUSDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای ماندگار موسیقی ایران خاموش شد/ ایرج درگذشت
🔹
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در سن ۹۴ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/680599" target="_blank">📅 16:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680598">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
یک هیات امنیتی بلندپایه عراقی فردا برای گفت‌وگو در مورد تعدادی از مسائل امنیتی به عربستان سعودی سفر خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/680598" target="_blank">📅 16:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680597">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lez96oPAAQ-xZQPJUewFoDMaI7Hz2n8hePyO9ToUuLikFN9cA7LA6t1QIMgg35LPngLt8IkwGxxEVqciihVFCX_PNcgnEWwHLJP79PJSwZMsNX96AGPP8pcvrFiCh7nptj3lGx9urv_gBJm6WBLE9l-gbhVhduPb3qRZoRJoEXSM225PudZlD8B_zHL8fBdMISkoh60vkWlIyyujpwL-3BHh-h00ay2lbuVx3pd6UsnnrCHfskOeyjilBw1RC_llmaqW69ZsrlcP9qkpEwc37nbXb5w1VHR6HozNrrMTxKIYJdXpRbEo1_upfM4nmU5UyGmAzee1iKAdIsz3yF50bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین اقتصادهای جهان بر پایه سهم از تولید ناخالص داخلی
🔸
مقایسه آمار سال‌های ۱۹۹۵ و ۲۰۲۶ نشان می‌دهد ایالات متحده همچنان با سهم حدود ۲۵ درصدی، رتبه اول اقتصاد جهان را حفظ کرده است.
🔸
بزرگ‌ترین جهش متعلق به چین است که سهم خود را از ۲.۳۶ درصد در سال ۱۹۹۵ به ۱۶.۵ درصد در ۲۰۲۶ رسانده و به رتبه دوم صعود کرده است.
🔸
در مقابل، کشورهایی مثل ژاپن و آلمان با افت سهم در اقتصاد جهانی مواجه شده‌اند و هند نیز توانسته خود را به جمع ۶ اقتصاد برتر جهان برساند.
@amarfact</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/680597" target="_blank">📅 16:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680596">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrLaVF4xUneRzj1UTQex83qK32q4_c_RO7DQYkGc60Yqmg6rsCHNcpK5HZmWT6f5DnXkG6PGSG2ZYtyp13uq7VCPrL6RJFCyi44_EJR54-5nQsBKjqO9Rbac6fpSn-NxUalJkm75BUmTlqw0E3i_SRKe7HLUaj9Y5aB_IkwgzN3VuAMGTCu7qzO2HG0ROCmXw5SoThWj5kVYsOZbbBZuM4XiX_FJ8PvZOdYGGXAzJa8rZi61tRIXPZq0YBmNDuX46mE3Cgn3rCYw_yJEU9Ec7xJp6yZzcPd1XVbSKl6cB2E_Wrlo-csPhGVTWGBJNY8u5D9oCEKstHXpdfGSGrj8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر فرار ترامپ با ماشین حمل آشغال غذا توسط جیمی فلن
🔹
فلن با کنایه این فرار ترامپ را به عنوان «طرح خروج ترامپ از جنگ با ایران» معرفی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/akhbarefori/680596" target="_blank">📅 15:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680595">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
آماده‌باش سفارتخانه‌های آمریکا در خاورمیانه از ترس درگیری علیه ایران
🔹
شبکه خبری «سی‌ان‌ان» گزارش داد که وزارت امور خارجه آمریکا با صدور دستوری فوری، از تمامی سفارتخانه‌های خود در خاورمیانه خواسته است برنامه‌هایی را برای فعالیت با حداقل پرسنل (کادر محدود) تدوین کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/680595" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680594">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tby6oJhuEpQKJaGNWT_e1SCDKchXV8YNyT35yNxAUOLR0-gXcuvOn1hqVsXAGTMaNLCFXOoaQbwowjPfmuoIIMn3ePKCjRkYj71TgkK1zjIMYLRJoHQ45HakS0uq2gmEVK_66dbAB3QqKp5AkUVpght-p2loJs6I35qszTpE-aBK_pRWA_P4tUwyljAnzUVzpyTX31ol_AjZuyS_f13oUEveR_SXdgbLiRJWT5cj2HH6hw5f3ZKcKYwodUwCtVaUgDSOSebd9wUeoziNmkDomJ7KZzlfOUyNxxDOpjIImqnKHD-mH2B3VlIjdapnl7XYWHX64hiuUOqbqfJI0nNvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مک‌گرگور مشاور ارشد سابق وزیر دفاع آمریکا و پنتاگون: ترامپ بر هنر شکست مسلط شده است
🔹
این بحران در پاییز ضربه بسیار سختی به ما خواهد زد... ۴۰ درصد گوگرد جهان از تنگه هرمز خارج می‌شود و در حال حاضر هیچ‌کدام از آن خارج نمی‌شود.
🔹
او باید بنشیند و کتابی با عنوان هنر شکست بنویسد، چون در همین کار مهارت پیدا کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/680594" target="_blank">📅 15:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680593">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شرور قمه‌کش تهرانی دستگیر شد
🔹
شروری که با قمه‌کشی، ضرب‌وشتم شهروندان و عربده‌کشی در خیابان‌های تهران اقدام به ایجاد رعب و وحشت می‌کرد و تصاویر اقداماتش را در فضای مجازی منتشر می‌کرد، دستگیر شده و در اختیار مرجع قضایی قرار گرفت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/akhbarefori/680593" target="_blank">📅 15:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680592">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b594ce2abb.mp4?token=NhpNKf3GhXWiw5bChN1Dn5DjXTQgmGMYVV1LPT3_720h3JLjaM3Md9WBYRx1ASKDiX6Boi_lbHf2i-hB9RB4Tzp5kxupV-5JHqliyETK3QfZLN_khdkKozSBdeMKoHV5g-TB2Wq9EjxQ2WAg0zrikZBMXaZ7zMeUJpcUSjr3m-eE-pngWIC4nnLl_M0_5xmHRSv15X8hMuQd62xSS6MLyfruOJtfzhobKA_5CWlYySoWnuQi-aRrx8t0WmVVtY6Wh4OT_KIX4ev9-6vaMbt0tdy7Os5iP4Sz1YrU2Rie-sbdQpXGDKGe_M8_cRgA8zJOZ7IMvRsf5bO-Urn8Jg9fEHceYyO0NvRda0Upbme13Ah6pgoPWj3dtNqh9RIfx_sNNhMGLp1-WyK17Mec3Xh_y4VWUiS8P0ZS9uYiWY4hZq4m1tKP0g4xc7Zu8beZgT6udhC2Cfmb86h7qhTyDay5AmDzyoItjKw-o6C3chckMq9_hUkKy-bOiWShNyf3jzk5dpAYisTRbVLjAufYTzoV_lgCJSaFaSJF4MdGEPr0Rt3L5-n6rQG6sLp6xO-rGUH23vMM_yq9-awBcN2uum6YwDDV69y6WA9oQN4KovWrnol1LcVSyfm4nJDNJH7qgmg-NOEmrskteqNWzt4GK5wyJ0kGcZ5u5znj9Y0ivjXzZKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b594ce2abb.mp4?token=NhpNKf3GhXWiw5bChN1Dn5DjXTQgmGMYVV1LPT3_720h3JLjaM3Md9WBYRx1ASKDiX6Boi_lbHf2i-hB9RB4Tzp5kxupV-5JHqliyETK3QfZLN_khdkKozSBdeMKoHV5g-TB2Wq9EjxQ2WAg0zrikZBMXaZ7zMeUJpcUSjr3m-eE-pngWIC4nnLl_M0_5xmHRSv15X8hMuQd62xSS6MLyfruOJtfzhobKA_5CWlYySoWnuQi-aRrx8t0WmVVtY6Wh4OT_KIX4ev9-6vaMbt0tdy7Os5iP4Sz1YrU2Rie-sbdQpXGDKGe_M8_cRgA8zJOZ7IMvRsf5bO-Urn8Jg9fEHceYyO0NvRda0Upbme13Ah6pgoPWj3dtNqh9RIfx_sNNhMGLp1-WyK17Mec3Xh_y4VWUiS8P0ZS9uYiWY4hZq4m1tKP0g4xc7Zu8beZgT6udhC2Cfmb86h7qhTyDay5AmDzyoItjKw-o6C3chckMq9_hUkKy-bOiWShNyf3jzk5dpAYisTRbVLjAufYTzoV_lgCJSaFaSJF4MdGEPr0Rt3L5-n6rQG6sLp6xO-rGUH23vMM_yq9-awBcN2uum6YwDDV69y6WA9oQN4KovWrnol1LcVSyfm4nJDNJH7qgmg-NOEmrskteqNWzt4GK5wyJ0kGcZ5u5znj9Y0ivjXzZKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای همسری امام زمان(عج) در سریال شبکه سه
مه‌لقا باقری در قسمت یازدهم سریال «رویای نیمه شب» ادعای همسری امام زمان(عج) می‌کند.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/680592" target="_blank">📅 15:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680591">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0CrSGtY_43B3kvQBm_rIWMsjI_14e238hynkvqvwQfRwDaWusZYSJ9FP3KCBhSKH7EeUADAZKhhE0kSavSpSGn_y8_z5zIM1Evc6u0rHYD9gIgHDm_fFY2IPHeROyNSTeIVB1DJ3ibmuGs0nJgVPN_JMH-s5eQcK3sryYXZhi2u4bYUF8NoXbJDj4umehRkK1tbKa2QErSclxpK5ZLp9YTcFjS4SladRDwwOGwyhC1zwFRpds7cQHwR2Gq19NN4wxUs7JPZ4rulHjgrHHKBgGaHe7zBhndI7xuGRuCIjQLghn42YQKsfEHQgUekz27OcKLjW-QsWYHpWdm6jFG3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش موارد خودکشی در صفوف ارتش صهیونیستی
🔹
یک نماینده کنست از افزایش خودکشی در ارتش اسرائیل خبر داد؛ به گفته او، ۲ نظامی در همین هفته خودکشی کرده‌اند.
🔹
هاآرتص نیز از ثبت دست‌کم ۶۸ خودکشی از زمان طوفان‌الاقصی و ۱۸ مورد از ابتدای سال جاری میلادی خبر داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/680591" target="_blank">📅 15:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIClQToYv1vwEZ5EJ68kpQjCf2JQhhfJRib-zbc66IgZUt4e-VMk7eqmoaDUYL-KWZYLXcClHODJKl-rRqFnEwzqaU-qsJcWZE5ctrHzLvTtQRXrnZD40btVf9Gc2BZKiZykyNU4CZvPo0LM11qG8l8fMwp4kXL3HgKdDqDfHDCEmY7QXrZxA8-71U7uYyuyEAnql64bSm743aQSfQRa0TyXgGVmguYuqju_VLQ2htTaC4DqzqcwR-cyUuLmyjTbSHKOdQfpv97BMxHoEeVpUY-QN7roErePQldc5VO2nC7omkLtfYY58mOjN_kCHBJ1i0xq4nFLjbc_un9VMyaY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnezMOd6ykYaiGxO_MCZgJgVVWbbaTUM66bi2Lp5-EviYA2Vah33fC_-RaVGNg3s129XoPX2JBhAO3H3KBc-CwFeLsuH3o1kHorQ6jPffVpyVbwfCedQcmzInkpwjc0Tfkmt5HcILng_VTGu9u4Bg4pHTX5Dl0SZMjA7rCuQXsGeVKbvL-xLDE4ld1flctIXoSUISRAsAgCrCBzJ6WJHlpEW-XiPEmAb1tOm95oXu6tO1nRCIG4y84Z41Ic2ufAuGmg07ZpIcyMr5eC5-iLvRsgrv5QdPcP8tzmFDmcAUHx0vvNBfuLc6lV5YX2mSwoV5HJpybNXadn5ICHd5d9O6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چیزهایی که به اعضای بدن شما آسیب میزنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/680589" target="_blank">📅 15:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93bd8e5d8.mp4?token=Zfg0d30MjVMq2sLPuKVaMYIBC-mSic43lZSBLmBiENKnEjpNjFNmn_IBijSDV3vIqyD6-JvpwmYuOZqNIRxvbR4cYYyV6azlS8Uh4Nb5Eu9OJGPOD1GO2S0yeXr0SBZP1QMWD1n03wuOhMZoA6CtMLzHa9uZ1-ks99mbdn31Pgnc9zFD-wql1u3UpUjwbGi9TiadUihX2oDWx-hqNkUHRvlHPo_MA8g6INPzHQscbhOnV9CgDRPuBeVV4XJQos2QidA0jOFDsn13Ext1tCuZ7p0zAKkWWPsxk5i5_km2w4ySaB-fYzs68mvc_RkZZJQ8rTGlMOpDh5XHfiem2ZrrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93bd8e5d8.mp4?token=Zfg0d30MjVMq2sLPuKVaMYIBC-mSic43lZSBLmBiENKnEjpNjFNmn_IBijSDV3vIqyD6-JvpwmYuOZqNIRxvbR4cYYyV6azlS8Uh4Nb5Eu9OJGPOD1GO2S0yeXr0SBZP1QMWD1n03wuOhMZoA6CtMLzHa9uZ1-ks99mbdn31Pgnc9zFD-wql1u3UpUjwbGi9TiadUihX2oDWx-hqNkUHRvlHPo_MA8g6INPzHQscbhOnV9CgDRPuBeVV4XJQos2QidA0jOFDsn13Ext1tCuZ7p0zAKkWWPsxk5i5_km2w4ySaB-fYzs68mvc_RkZZJQ8rTGlMOpDh5XHfiem2ZrrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت لعیا زنگنه از پشت‌پرده «در پناه تو»؛ سریالی که در زمان پخش با ممیزی‌های مختلفی روبه‌رو شد
🔹
صداوسیما می‌گفت پارسا پیروزفر زیادی خوش تیپ است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/680588" target="_blank">📅 15:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1c75d976.mp4?token=bZUAVuI8NMqqgxyi8G1ZXNcOV_oOMgq_HMGhMYryfg1LKVXYGIHQdwvkj26CHP2u4pA-UVpAWq_L5NdIYeHIz-KXRFGQEmCURZx4bCNkvUxR3eT7CwtHwPZQlANPR2U1wJTsP1QmwjrBy-lgHuamyc4U_UfI2q410Ic9Q574MuCmqFMHeYLzAPZdXkWuHL4h9qjqIcfZDoaaMQDwCZS0TSCT73L0p2PetS_76uRTnHNa6EJEXjyzr91JNyEFNNdeN14FZd4Nf7OiH4DOduxVleo-vujklYbVokDvrjOOG84bRRrJxohaToU_LPDDCHwya2oMILDpUyWv72pf4p_sZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1c75d976.mp4?token=bZUAVuI8NMqqgxyi8G1ZXNcOV_oOMgq_HMGhMYryfg1LKVXYGIHQdwvkj26CHP2u4pA-UVpAWq_L5NdIYeHIz-KXRFGQEmCURZx4bCNkvUxR3eT7CwtHwPZQlANPR2U1wJTsP1QmwjrBy-lgHuamyc4U_UfI2q410Ic9Q574MuCmqFMHeYLzAPZdXkWuHL4h9qjqIcfZDoaaMQDwCZS0TSCT73L0p2PetS_76uRTnHNa6EJEXjyzr91JNyEFNNdeN14FZd4Nf7OiH4DOduxVleo-vujklYbVokDvrjOOG84bRRrJxohaToU_LPDDCHwya2oMILDpUyWv72pf4p_sZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده باش؛ به زودی به سراغت می‌آیند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680587" target="_blank">📅 15:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680584">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">روز بود روز روشن</div>
  <div class="tg-doc-extra">حاج محمود کریمی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/680584" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🖤
پک
#مداحی
ویژه  شهادت پیامبر اکرم (ص) و شهادت امام حسن مجتبی (ع)
🥀
مزارت سجده‌گاه آفتاب است
ولی افسوس ويران و خراب است...
شهادت
#پیامبر
(ص)
شهادت
#امام_حسن
(ع)
@gharar_madahi</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/680584" target="_blank">📅 15:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680583">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af49a37116.mp4?token=GY1hBzcKznnwnUEVEy0Dx06OzU-jh0NFt4qPQXD-6dgMFKoP1eF-zZtaAavzikqpIhTM22IMXiD0UvnzPZ_mgfc0KAGLqpZgA6WcaRctj0A5wuTz2OLhyHyjzNWoHOAwq0sys9OxaDK5oSXbEfjGdnZVDR3uqGnwChiSxIhpECR-8UAz7SUCcMY2QIjo8G89UP-N8SeDCN2Kwcu4U___5TmwpX6temLr4biuglShRCrQ3WWbMLmShL3l4X3T6yUAPx6bbbA3qjSPISHsYh_ZomYzfyeWakbu5g9biVVvKOKuYUGDHyEFREQDhd-lBoj_7HVb-KWVZrWe9HPMvxd7DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af49a37116.mp4?token=GY1hBzcKznnwnUEVEy0Dx06OzU-jh0NFt4qPQXD-6dgMFKoP1eF-zZtaAavzikqpIhTM22IMXiD0UvnzPZ_mgfc0KAGLqpZgA6WcaRctj0A5wuTz2OLhyHyjzNWoHOAwq0sys9OxaDK5oSXbEfjGdnZVDR3uqGnwChiSxIhpECR-8UAz7SUCcMY2QIjo8G89UP-N8SeDCN2Kwcu4U___5TmwpX6temLr4biuglShRCrQ3WWbMLmShL3l4X3T6yUAPx6bbbA3qjSPISHsYh_ZomYzfyeWakbu5g9biVVvKOKuYUGDHyEFREQDhd-lBoj_7HVb-KWVZrWe9HPMvxd7DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختلافات در موساد
🔹
رئیس سازمان جاسوسی رژیم صهیونیستی تغییرات گسترده ای در ساختار ارشد این سازمان ایجاد کرده و شماری از مدیران را به دلیل شکست اطلاعاتی رژیم صهیونیستی در تغییر ساختار سیاسی ایران کنار گذاشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/680583" target="_blank">📅 15:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680582">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای آناتولی: ایران و آمریکا با تمدید مهلت ۶۰ روزه تفاهم‌نامه موافقت کرده‌اند
🔹
خبرگزاری آناتولی به نقل از منابع پاکستانی مدعی شد ایران و آمریکا با تمدید مهلت ۶۰ روزه مندرج در تفاهم‌نامه اسلام‌آباد موافقت کرده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/680582" target="_blank">📅 15:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680581">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69dda9395.mp4?token=tAu4kqQ-py2ewnTzrybgjO--sMrpdBs1wzz4rnPZN9E5zdekK_xm4SWGulB-Kpr1QFTAmgsxGyhm_Ozk5cc-6SrrTfcIHLt0uhuhbRwOxmXAvlvRp3pS1oEvrL_mq4YnQ8r-U2kGfY2SJe440LQrBz48WuJOv7CS8EGCgDpPRd_uJIrJapDEw_B6hivPWohfe3vUwYIB1NagPg8Ui4q3C8QYcLVIEqf5DMzhFCwghKLU4FsVsdl2IqdaLX4J2-4py7kFJlgWC0abwtQQ6d-gMOauMJhbvONJgLue_HKyE2SUyvzQ1nw0gsubnZXY_UxgtsaZdCvkSVtQO84tkodnuU4oOWdFpvSm3cZZC0aVdrPECuRJE1ZnxGcgNx_HIiAqRppVDMQAmoiMsa6g807IUr78wWmd8LfBPpujMD7-ZvCaVQJGDtjbW3lSa-HzzuHfkO0BBzMyIUygM5oJPcT9IXF2TSCj18dkemo9FxMKTvOYB7Wa8F33wT9GPPUZkC7g_L5CtgSgMla-pl0PwLruOj9bxODuAr1yLx_4em-x6HzuU0tjYdKOMLE2Z717MqYRFK0MpkghAPIWFK_0Aw-w7izuZ9ihJXLGIsNVW6V3djxTxEydFK6fmbGfzRMtcV7ywua3m3YGAwzYYh71oNcElFyx99d1vdFxzCu9LfRWgwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69dda9395.mp4?token=tAu4kqQ-py2ewnTzrybgjO--sMrpdBs1wzz4rnPZN9E5zdekK_xm4SWGulB-Kpr1QFTAmgsxGyhm_Ozk5cc-6SrrTfcIHLt0uhuhbRwOxmXAvlvRp3pS1oEvrL_mq4YnQ8r-U2kGfY2SJe440LQrBz48WuJOv7CS8EGCgDpPRd_uJIrJapDEw_B6hivPWohfe3vUwYIB1NagPg8Ui4q3C8QYcLVIEqf5DMzhFCwghKLU4FsVsdl2IqdaLX4J2-4py7kFJlgWC0abwtQQ6d-gMOauMJhbvONJgLue_HKyE2SUyvzQ1nw0gsubnZXY_UxgtsaZdCvkSVtQO84tkodnuU4oOWdFpvSm3cZZC0aVdrPECuRJE1ZnxGcgNx_HIiAqRppVDMQAmoiMsa6g807IUr78wWmd8LfBPpujMD7-ZvCaVQJGDtjbW3lSa-HzzuHfkO0BBzMyIUygM5oJPcT9IXF2TSCj18dkemo9FxMKTvOYB7Wa8F33wT9GPPUZkC7g_L5CtgSgMla-pl0PwLruOj9bxODuAr1yLx_4em-x6HzuU0tjYdKOMLE2Z717MqYRFK0MpkghAPIWFK_0Aw-w7izuZ9ihJXLGIsNVW6V3djxTxEydFK6fmbGfzRMtcV7ywua3m3YGAwzYYh71oNcElFyx99d1vdFxzCu9LfRWgwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی از نبش قبر نیما یوشیج برای انتقال پیکر او به زادگاهش، یوش
🔹
نیما وصیت کرده بود که پیکرش را در یوش دفن کنند اما برخلاف وصیتش او را در امام‌زاده عبدالله در شهر ری به خاک سپردند. از جمله دلایل عمل نکردن به وصیت نیما در زمان مرگش، آب‌وهوای بسیار سرد و دشواری رفتن به یوش در دی‌ماه بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/680581" target="_blank">📅 14:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680580">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293c0a782c.mp4?token=sRr7N7CycdP_QN1Js4LWxJyoR9E8xTVZLB7r6nd9ufwMPcWSPdoMsOv2gqTqVm9IaB-BDx42YPZJDLQjzsTwb7VOKljtWoG1uTAEk2F3LtEF1mwDuC9_SbFH16MFxK4ECpyg6LrlE9PN4A2AfJofXUnCYTan40d_8B2vTo9NNAiS9ZzgGNlLfr_tqW96jHB3t29KKGK2p8IOQ8mwuJuO1oU33397OTCMOQ5qf8RWhO-to5bDIb4cCpe1xi8JD6Lrgdm4yvMFmxg-knybHu3dLVDs0CtXq2XDSlLintsUDpQbrg8zMVUs8iTXxQ75AXeyG4DZfSSu2Cs7Gp_SKcg5UaG8iVC8FjWkyJYws3fJfBdo2AYqdBC_4GEXKRtwnHMVqNCqOB7MiyMngSt-dCsC41umpj0g-KjG15jfA-MuBq7rIOBcvGTMf8Ik35StTJWqTWLIBwROqlBf_9QU0E9pZzYL4PTeUQZcenHe4SOFXt0nnlmcvmxE8XMDDpo3KORUckwZfWt82XV5w8rZiz89rlBAY3DB0PSJ7W3fbVL4Q87IHUe0lsZjH9I2LuCmKfBf9VX2p8S38z4F__B_wxRm7gwDOfi47tWGFNV2GOaaJQ7Kp6COGkgEMKMo8T29pQzrrc05GHhYZmWnGbt-7xAhe8TE9ErYChGcbeP9XpREHCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293c0a782c.mp4?token=sRr7N7CycdP_QN1Js4LWxJyoR9E8xTVZLB7r6nd9ufwMPcWSPdoMsOv2gqTqVm9IaB-BDx42YPZJDLQjzsTwb7VOKljtWoG1uTAEk2F3LtEF1mwDuC9_SbFH16MFxK4ECpyg6LrlE9PN4A2AfJofXUnCYTan40d_8B2vTo9NNAiS9ZzgGNlLfr_tqW96jHB3t29KKGK2p8IOQ8mwuJuO1oU33397OTCMOQ5qf8RWhO-to5bDIb4cCpe1xi8JD6Lrgdm4yvMFmxg-knybHu3dLVDs0CtXq2XDSlLintsUDpQbrg8zMVUs8iTXxQ75AXeyG4DZfSSu2Cs7Gp_SKcg5UaG8iVC8FjWkyJYws3fJfBdo2AYqdBC_4GEXKRtwnHMVqNCqOB7MiyMngSt-dCsC41umpj0g-KjG15jfA-MuBq7rIOBcvGTMf8Ik35StTJWqTWLIBwROqlBf_9QU0E9pZzYL4PTeUQZcenHe4SOFXt0nnlmcvmxE8XMDDpo3KORUckwZfWt82XV5w8rZiz89rlBAY3DB0PSJ7W3fbVL4Q87IHUe0lsZjH9I2LuCmKfBf9VX2p8S38z4F__B_wxRm7gwDOfi47tWGFNV2GOaaJQ7Kp6COGkgEMKMo8T29pQzrrc05GHhYZmWnGbt-7xAhe8TE9ErYChGcbeP9XpREHCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال و هوای چند روز خدمت به زائران پیاده امام رضا(ع) در موکب قرار و کانون سلام/توزیع ۸۰هزار غذا بین زائران امام مهربانی
از سر جاده راه افتاده
پای پیاده، یه دهاتی
با همون لباس ساده
داره میاد برسه پنجره فولاد
بشینه روبرو گنبد
گوشه‌ی صحن گوهر شاد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/680580" target="_blank">📅 14:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680579">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
کپلر: این هفته تنها ۸۴ کشتی از تنگه هرمز عبور کرد
🔹
بر اساس داده‌های مؤسسه تحلیل و ردیابی داده‌های دریایی «کپلر»، میزان عبور و مرور شناورها از تنگه هرمز به شکل چشمگیری کاهش یافته و طی هفته جاری در مجموع تنها ۸۴ فروند کشتی از این آبراه راهبردی عبور کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/680579" target="_blank">📅 14:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680578">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تویوتا فراخوان جهانی داد
🔹
تویوتا موتورز به دلیل نقص نمایشگر که ممکن است باعث از کار افتادن چراغ‌های راهنما و چراغ‌های خطر شود، ۶۵۵ هزار دستگاه تویوتا کمری را در سطح جهان فراخوان کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/680578" target="_blank">📅 14:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680575">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJJgrn4NdVa23KhfCQuNDKI5kL02ScSt8PsB7_xzsCxF155f9ScQ4ImtHtSVqRqJAt42qj3fthQ6teWzY-BorWUW68Y5YW3GE61l__oswiejBtL5l9o9kNFWzPSao1Kc9atCvTF-foi8potr8kTfFd80bKQWDupAScq8BUL1p45hjpamJEvu9MzqxrsnyljLWaK4drLpEGBZDo0IH9ameH0TgPmxhBiIcnXs_ZVH4c-Wafitwa97xuTKuslDMbbLGU3jhrWWa54_F4laOOgd4A8-E06gZYjD_I_zbHir6TmVAnPHI8oFu-wzzXRsvtY3bdvWOXT-zXd8UCyi0IxGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زاکانی، شهردار تهران: موشک مستقیم به طبقه آقا مجتبی خورد؛ همسرشان، شهید و خود ایشان مجروح شدند
🔹
موشک به طبقه‌ای اصابت کرد که ایشان و همسرشان در آن حضور داشتند؛ حمله‌ای که به شهادت همسر رهبری و مجروح شدن ایشان انجامید.
🔹
پس از حمله، اطرافیان قصد انجام اقدامات درمانی و بخیه جراحت را داشتند، اما رهبری در همان شرایط نیز دغدغه اقامه نماز داشتند و یکی از حاضران از آرامش، مهربانی و توکل بالای ایشان در لحظات پس از حمله سخن گفته است./ دانشجو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680575" target="_blank">📅 14:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680574">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/680574" target="_blank">📅 14:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680571">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پنچرگیری هم لاکچری شد/ هر لاستیک نیم میلیون تومان!
🔹
هزینه‌های نگهداری خودرو در حالی هر روز سنگین‌تر می‌شود که حتی یک اتفاق ساده مانند پنچر شدن لاستیک نیز می‌تواند صدها هزار تومان روی دست مالک خودرو بگذارد.
🔹
بر اساس نرخ‌های اعلام‌شده، اجرت پنچرگیری هر حلقه لاستیک سدان بین ۲۰۰ تا ۵۰۰ هزار تومان و برای شاسی‌بلند تا ۸۰۰ هزار تومان اعلام شده است؛ رقمی معادل ۵ درصد حقوق پایه ۱۶ میلیونی یک کارگر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/680571" target="_blank">📅 14:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680570">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uzo0RA4sseRZUjLBLj9E3RbmlZm9vYNC8tNeDPBq8t0Cpm9jynlr8660wLFwZuo2osgdACkWbTQrWByIlL6SGIEXTbFH2wDAhhEtjmbVZcIHfiU8GkT0TihKSi23uBizWitARCQY4xrrygmVMAoJPsrp1x_I6BAFA1VQpWMkLpoOkRuUYWWMeIFnmCls5nmkQCULJhPILDvin2BDLYyZBhN6Mm681w82O1TzT7vr7cJ3J5U_ePMBwQ5p1fZhD122QsgOdPAOg44at0IWFP9IKEe3N_pMcFda0whOtZHE6jLlU4fr0VazEsi3S5Vg_BzTZbyhwjMCKakwfv-lzd1xMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده جدال بر سر دریای خزر/ ایران هوشیار باشد
🔹
مسئولان باید در نظر داشته باشند که مساله مالکیت دریای خزر بیش از اینکه یک مساله سیاسی یا اقتصادی باشد، یک مساله ژئوپلیتیک حیاتی است و می تواند امنیت ما را تحت تاثیر قرار دهد.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3237180</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/680570" target="_blank">📅 14:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680569">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
پزشکیان: ایران به هیچ وجه خارج از قوانین بین‌المللی عمل نکرده است
رئیس جمهور در گفت‌وگوی تلفنی با نخست‌وزیر ژاپن:
🔹
ایران به هیچ وجه دنبال ناآرامی در منطقه نبوده است.
🔹
آمریکا و رژیم صهیونیستی با تجاوز  به ایران و ترور رهبرانقلاب و شهادت جمع کثیری از غیر نظامیان از جمله دانش آموزان میناب و تخریب زیرساختهای غیر نظامی موجب بر هم زدن صلح و ثبات در منطقه شده اند.
🔹
امیدوارم تلاش‌های دیپلماتیک ژاپن برای برقراری صلح و ثبات در منطقه ثمر بخش باشد
سانائه تاکایچی:
🔹
توکیو از روشهای دیپلماتیک برای پایان جنگ حمایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/680569" target="_blank">📅 14:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680568">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVFsmsLOouKclHkASfk4o1-_bxTVpWmLGLInbTrlIe_VKKJXweOOR892fJ-LuDPSalbOatxghNP91vt2HYjGZm4fkiv7IVL4RBaG5T36MKHpJfr-cE8jmBII4wWT6PoGyLr13FefmDfNggfhlxVzMH6aEMipfT2XwGV9xTqCr_BOYl3ooajKsKm5PD2fSrlrD5FXdtqsvH27PW7YdO0IElEpNM3KHRzTVA_RE6vUd4y02wX_T3RAHWf-gzOTbUwM1XyIBxL2lHrBmYVdR9u4eObMQN79FtvRQB6FvI2mE7n2t9YAiqazUmTK0g5z_zp7QySRoFAIV15wUZCHb62maw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قوی‌ترین پاسپورت‌های جهان
🔹
سنگاپور، کره‌جنوبی و ژاپن دارای قوی‌ترین پاسپورت‌ها
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/680568" target="_blank">📅 14:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680567">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd389e9e9.mp4?token=lQNx0K4uYQz51j29czRlRQkS1Cm4BJepnWSHfa8JbszbUuQQ3HBHAv82mYhca_lod-JM87VAvj4iyXaoh7ZpgHP286sOI_RvJVy5L9Bxj7fWgj8yNGSDiVTn1pjT2qBhxJ9aRqumtWsfYz7z4mDmHGM9f9NMA6GxJIyMXL8UuTFwkkJrJvezfoNd-In3iWWCIDABBH4jH7u_ifzaXGlzWBknwK3D7MQav19yw68Wpf3aKL4SxD3bgUuB41dzQob_YPT1qXurK7unLH5OscKEQhbKRf0kPggxOys1B4iAPsQ79mNWVfwa_S9opeAuUMsQDU3z25WTHcyjYR5KmtlCwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd389e9e9.mp4?token=lQNx0K4uYQz51j29czRlRQkS1Cm4BJepnWSHfa8JbszbUuQQ3HBHAv82mYhca_lod-JM87VAvj4iyXaoh7ZpgHP286sOI_RvJVy5L9Bxj7fWgj8yNGSDiVTn1pjT2qBhxJ9aRqumtWsfYz7z4mDmHGM9f9NMA6GxJIyMXL8UuTFwkkJrJvezfoNd-In3iWWCIDABBH4jH7u_ifzaXGlzWBknwK3D7MQav19yw68Wpf3aKL4SxD3bgUuB41dzQob_YPT1qXurK7unLH5OscKEQhbKRf0kPggxOys1B4iAPsQ79mNWVfwa_S9opeAuUMsQDU3z25WTHcyjYR5KmtlCwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجموعه میم‌های وایرال شده کاربران خارجی از پنهان شدن ترامپ در خودروی آشغال غذا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/680567" target="_blank">📅 14:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680566">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ونهم از فصل پنجم
🔹
در این قسمت دومین تجربه‌ نزدیک به مرگ آقای سید محمد موسوی که هم زمان با جدایی روح از تن مادر در حین عمل جراحی، روح ایشان نیز بخاطر ناراحتی قلبی جدا شده و تجربه مشترکی با مادر در عبور از رودخانه‌ای طغیانگر را درک می‌کند و بخاطر نگاه به نامحرم و دروغ، خود را در طبقه‌ای از جهنم که شادمانی شیطان بزرگ‌ترین عذاب بوده است، می‌بیند اما بخاطر آبروداری فردی گناهکار در دنیا از این طبقه رهایی می‌یابد را در این قسمت و ادامه ماجرا را در قسمت بعدی نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید امید متقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/680566" target="_blank">📅 14:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680565">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
لکه‌های نفتی به جنگل‌های حرا در قشم رسید
🔹
بخشی از لکه‌های نفتی وارد محدوده جنگل‌های حرا در قشم شده و نگرانی‌هایی درباره آسیب به این زیست‌بوم حساس ایجاد کرده است.
🔹
مسئولان منابع طبیعی قشم در حال بررسی میزان آلودگی و وضعیت جنگل‌ها هستند و منشأ دقیق آلودگی…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/680565" target="_blank">📅 14:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680563">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdbw_mViNRC0ZR2AbwyhkpDMBPuLFdO2pDGF5u2134di-chqF5qZLVbbLQWg2RngwLb76RrP1TWR614-FJ3BJhhvyybc8MX1mp95hMTnbXFPBqpd5iuiJbQR7rvS5Azsc6JaHfqSShRq0uStMxDS_KnafD6VhFv3YPe5Snv6pZ3_cBM7MrLICsrsDkTEAs9DzWF92PEgeZCZEgU1r9nfLAaQm8ytP6QGV9fow7WJoCI2tohJ5ZHz0MIixYVa6fbWL8IMMOOSafErvETll-6cNGAbX9DeVbPOunZVA8PjtSaHgAh6YopHHUXxMhyu244eCI15je-IRDHWeiAyi8Guzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر اساس مجله اکونومیست، محبوبیت ترامپ به پایین ترین حالت خود رسیده. حتی از کم ترین محبوبیت دوره اول خودش و حتی بایدن، کم تر شده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/680563" target="_blank">📅 14:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680562">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
علی‌اف: کریدور زنگه‌زور و اتصال ریلی به ایران در اولویت باکو است.
🔹
بلومبرگ: امارات در صادرات نفت از طریق تنگه هرمز به عراق کمک می‌کند.
🔹
مسیر شمال به جنوب جاده چالوس تا اطلاع بعدی مسدود است.
🔹
آتلانتیک: ترامپ به گزینه اقتصادی روی آورده اما تاب‌آوری ایران را دست‌کم گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/680562" target="_blank">📅 14:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680561">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuqxxQDFdHkLlxY1EKYvfPeZO4t6xW2lBNeB_Zdo4jLUBAC7L-wm6xCbgbzAu6QmI3L2XhtT3xJfcACyTYg2sYCh3bMTWoZ_m_SJEhAhjrdYzzDJ3i3jyhESEabr6EGfBZ4RluV87l6-Ws0Zkj5MurW3-igkM44S97NEJyllu6IT_LezpdqfTvcM9FoRsXVfSevwlVMEX6cw9WCD4WGUtP3geR7DCUgamZyOwAb5CzOJl2oFm_6BWZmKYYJPvqRlIesNwYH_v8SIuMJpOdWBt_pFKE1wonsZTdLJnblc8BdlAx49r63ANFnmoXZ1HaIJTMIUrWNH-fZxCK0QeE9D-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال حوزه جنگ اوکراین: ترامپ در حال بررسی تغییر نام وزارت جنگ به وزارت تسلیم است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/680561" target="_blank">📅 14:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680560">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3Fz5gp9EJluFhrxOiOlmo4qwNN4OqHuME8qcWOrpAkFFZTIGtOLfAZGcpRwWjTEm-NkpSNwkNNjXUsg224DQJvZWoydP8Gw9C_5lltdbYRwwRsg7czmJr6Pxr9ch8LPmbZrE3YDYbhRCjsuuNk3_f5VRoMatabfZszIdMra50406crSU3uO_jaXR2qdZGzKqMIQLv92eHtfg_3_c26ps53W8CxPz9EZRc7LKx8gV5j1NCc8oeu_kET2R3HY2M3nCSeo161ozOZPbZaVxkNDeR6As6L1PwoVljCtudD8QBnmYy1fjWKa9p7RXc3mM8HPslMO65q1wsRZVbS5BNzChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ هگست را با خود برد، اما روبیو را گذاشت تا هدف موشک‌های احتمالی ایران باشد!
🔹
یک کاربر شبکه‌های اجتماعی با کنایه به روبیو: «مارکو داداش، اگر جای تو بودم، از این به بعد حواسم به پشت سرم بود.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/680560" target="_blank">📅 14:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680559">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNr5FcStelTtg7SyM8TgPe3F4mZHoy01HBkeUfPbbpwiazX40mu2YqBwIXwzcQEPn47kPNiE3X4lbIYeNUPLVGHIV4iY2wcwNDw7JhLExpxPGff8G0xuJ1vsZAooWqs3uPwbg8SWEM1QEtXkE8mjcD6UoV_0s1tISDDBEkWmo4Q58VECa1Sgsu8JJbH-huSYXt-s8PaaNY_jtLv6m0v97lmuCOZSA7wuIrzkpx1Hi_iyP65Yel-sOCkcdQ0JfeCTyrB0phNpKaZkbcfX04vyrY2CjUIH7lhKRLTV5RZ6Dv8ZwMRh7p8I-s0UC9-26_cFHi5XN87RlKiOm8ngcZiQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییر مواضع مارکو روبیو درباره توان موشکی ایران
مارکو روبیو، وزیر خارجه آمریکا، در اظهاراتی طی ماه‌های اخیر مواضع متفاوتی درباره توان ایران مطرح کرده است:
🔹
ابتدا: «ما ظرف ۲ روز ایران را له خواهیم کرد.»
🔹
چند روز پیش: «این نبرد در آخرین لحظه است؛ آنها دیگر موشکی ندارند.»
🔹
اکنون: «ما ایران را دست‌کم گرفته‌ایم.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/680559" target="_blank">📅 13:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680558">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9YRHwablTf6_wxDcnFnA8zB5KXRcsmlfqro_MvmVfthQ8jZykVluQ8L1VpRLRYkF7zoajyU41z_3pLIXIBCBqQMKViy__GhDXtErFHywzlwroIPm7EutK1HOv-gNIjd1nQuncWOQRTbAYXTnZMJRFZPBdyVnZAC9T7rpPIxYYQgmruQB-Yj-nDlXqo0grV-BKdjAWEueLfwVWb-DrYeiYVD-Zo8YUVQu49I54vW7MNsYW1JaBkQeh74_YK4DW0LDLDojcyqSbKhb0PLvIVpxVYM69btSuTdGK81l4opWZLcufyvRet5ZpZJdx-X1KWbxEEzPPxnMBVp44qJfcaJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانیل دیویس، افسر سابق و تحلیلگر نظامی و سیاست خارجی آمریکا: این هشدار را نادیده نگیرید، ما مدت‌هاست ایران را دست‌کم گرفته‌ایم و در همین جنگ هم چندین بار تاوانش را داده‌ایم
🔹
وقتی ایران چنین تهدیدهایی می‌کند،  واقعاً به آنها عمل می‌کند. بهترین کاری که رئیس جمهور ترامپ می‌تواند انجام دهد این است که از این جنگ کنار بکشد.
🔹
ترامپ در «اعلام پیروزی» و بزک کردن نیز مهارت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/680558" target="_blank">📅 13:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680557">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB2D2X4p0zWE02mXf0v3gYjRla5aHn3y8MxCeSA2EIWcDaNUxQZLnZ5S7eJ-lIK2EwcDe5-AjgIFRYDTqrUF8Kwc4JDwddUwckBv-l7EqtHnR1tZ5D2t9sWwr-m-xZw7zXH63jkfh3MCYa_2CiAAmQhenRl7HO2Q8jBzoLvoC9MPu0cn8lhBsFQYqmiBTRHe70oY4PuPc7Ej1oIluPsE449JJeA-GABypYV1i80rLfJfFGlR0CNv_bTWyaOmM7XJWlg_DpfvzEXuU3wiipQV7SrCzFOH-p3ThV_DV7nZa1h_qEooleszlhJub1MQ5eugLAPXQ_vy5s22q-IQxyKViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وندی شرمن، معاون پیشین وزیر امور خارجه آمریکا: در آینده قابل پیش‌بینی و شاید برای همیشه، ایران کنترل تنگه هرمز را در دست خواهد داشت
🔹
بعید است اعمال فشار اقتصادی بیشتر از سوی ترامپ، باعث شود رهبران ایران تسلیم شوند یا از مواضع خود عقب‌نشینی کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/680557" target="_blank">📅 13:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680556">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ضرب‌وشتم مدیر برق عسلویه هنگام جمع‌آوری ماینرهای غیرمجاز
مدیرعامل شرکت برق بوشهر:
🔹
مدیر برق عسلویه و همکارانش حین جمع‌آوری ماینرهای غیرمجاز با هماهنگی قضایی، از سوی یکی از استخراج‌کنندگان مورد ضرب‌وشتم قرار گرفتند.
🔹
مدیر برق عسلویه به‌دلیل آسیب جدی به بیمارستان منتقل شد.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/680556" target="_blank">📅 13:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680555">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo0DSuiO8R3i1KeTk9D6Ie-ga3McZZgYNRblLREAgo_cGx8VzEuqL-N4WKMwfqprAXLrvfknneqQG9iqhovV_IdUsmdKGv5Bk5EaH0Yqo1PlUTQ5NsRgTyxcCpiu7dMRMDU7FPC97RQpl2Q-KwGFlR0Gqp3UQb4Ona0nBi3vXA_I2JgnxCTtetXFCLoIP8JEw9rd-UDFC3ahU-XQwcUwITypn16QPRP-MugjWrwDuoTE0Wo1DeyawFvUnRbklj3A91Qyl4Rk3cyUnSyIKUElnw0rGiGI_xskvaAIAK9a0z99QTql2eHRPfegmj7NG1_7AUaoJG-IOPM4rMAIQ5Uwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طولانی‌ترین برج کبوترخانه ایران؛ چهل‌برج کلیسان
🔹
چهل‌برج کلیسان در روستای کلیسانِ فلاورجان اصفهان، از نمونه‌های کم‌نظیر کبوترخانه‌های چندقلوست.
🔹
این بنای دوره قاجار از ۳۲ استوانه تشکیل شده و حدود ۱۳۲ متر طول، ۸ متر ارتفاع و ۵ متر عرض دارد. نام «چهل‌برج» نیز به تقدس عدد چهل در میان مردم نسبت داده شده است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680555" target="_blank">📅 13:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680553">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbcf87c51.mp4?token=fBLgqKfKwyeLq2DO-rgKDFEfQnf3uxiRbhZWiDSN1zQEt8sL0ZF6ntZfkoBLvma_bkdF9iExltLulH9N-TmARJMpvQp7-QW225jkx_j6dX0ltrO_zVIg0E_StLoqiWgk5SilAtyxF6XsYD7Zjffv_XO1KMArlaJyfMKgTvF3Slv1NeZ-v9ICxw9UR4Qafr5WxRw0QtTMjASmZf9xq9oCRKNV_zH3LdsZhNCMxT_lBtSzsh2Yjuh_FabL5gGy3taZKjFRDyWeMzsHxShdpyXRmqt_Bj7Oa25vZ-6bzJKMRRKQGM9hZZgJuMUZn68Hf7xtZM3CvcD-KcSd9HnfauGAiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbcf87c51.mp4?token=fBLgqKfKwyeLq2DO-rgKDFEfQnf3uxiRbhZWiDSN1zQEt8sL0ZF6ntZfkoBLvma_bkdF9iExltLulH9N-TmARJMpvQp7-QW225jkx_j6dX0ltrO_zVIg0E_StLoqiWgk5SilAtyxF6XsYD7Zjffv_XO1KMArlaJyfMKgTvF3Slv1NeZ-v9ICxw9UR4Qafr5WxRw0QtTMjASmZf9xq9oCRKNV_zH3LdsZhNCMxT_lBtSzsh2Yjuh_FabL5gGy3taZKjFRDyWeMzsHxShdpyXRmqt_Bj7Oa25vZ-6bzJKMRRKQGM9hZZgJuMUZn68Hf7xtZM3CvcD-KcSd9HnfauGAiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: بریکس باید از گفت‌وگو به اقدام عملی برسد
🔹
بریکس می‌تواند سهمی مؤثرتر در شکل‌دهی به معماری مالی بین‌المللی فراگیرتر، متوازن‌تر و مقاوم‌تر ایفا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/680553" target="_blank">📅 13:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680552">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzvsqcU4m_sj0aAGD88hyShT9RXLGcn5Ol8K0L7aCRBQoIOpm5Pzh-mmvn2Ut4QnOdwcCIvlq_7DGaGNc28sA7hFuXScF_B5mCgKRvah_hCNAI2RqStnRsGbeD6EqklVQIyu1xAGTwmHAp6OJQfhgLsv47zNqX_GD6KP7KguRIHYquAu_GqK94RRf4zZbCzIcYe948NwUydp-xYBSj3o14Tum0UIQDq9A5vxvuVX_Zo-w-MWplt1JnkhFOf2g4xDCrx2TnrnaZ1wfpTJWFxiSSg_JKqaiVaP5OXjs-TpjKnOsVJu85mxXfUPKE2mYiRSUs97FbSexraPgx7s-PndVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه رویداد نجومی همزمان در آسمان
🔹
امروز خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی همزمان رخ می‌دهند؛ یک شب متفاوت برای رصد آسمان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/680552" target="_blank">📅 13:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680551">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اداره‌ فرودگاه‌های هرمزگان: فعالیت پروازی فرودگاه بین‌المللی بندرعباس از ۲۴ مرداد آغاز خواهد شد.
🔹
سازمان لیگ: بازی اول استقلال در شهر قدس با حضور تماشاگران برگزار می‌شود.
🔹
پوتین خطاب به اروپا: به توقیف کشتی‌ها پاسخ می‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/680551" target="_blank">📅 12:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680550">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSPGZcL66O4N2OrFpkppQCFgywQcpfSM7XM5abZh1BMUTCj80B24cFqMF2y3eLrf1ZbtoIwKH7nhmhknqRxsNpLj_-3tOWEKj2n0b6auruLtJ0Rd3hUNXOqiaEFOJxzxiZ7gbFbkRvQxl4SLhESuqnzFnFDoLe53sTYGCriPYdnavemb0G9eoNg8OdPRAF5VTg7rdrq_HxZXqRLdaqbqmY2p6zNi7IzX1ZwpjqA78PJ8-gxlj1xEkJNMbBUvlLORrL-nKwUwY6Ov-CGD6EW285FW6KGTs3zWrOE0QxxPyYCE4VK0yjhWa1a5DaEYo_TvhU18hmuSQsEm-Gm1GgLn9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به بهانه مسابقه امشب؛ قهرمانان سوپرکاپ اروپا از سال ۲۰۰۰ تاکنون
🔹
۱۸ قهرمانی برای فاتح لیگ قهرمانان اروپا
🔹
۸ قهرمانی برای فاتح لیگ اروپا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/680550" target="_blank">📅 12:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680549">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
لکه‌های نفتی به جنگل‌های حرا در قشم رسید
🔹
بخشی از لکه‌های نفتی وارد محدوده جنگل‌های حرا در قشم شده و نگرانی‌هایی درباره آسیب به این زیست‌بوم حساس ایجاد کرده است.
🔹
مسئولان منابع طبیعی قشم در حال بررسی میزان آلودگی و وضعیت جنگل‌ها هستند و منشأ دقیق آلودگی…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/680549" target="_blank">📅 12:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680548">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d72c32eb9.mp4?token=abJhs_g9kB9OmGclWTnBX_aXvPOm8sqZmPpji17e0GGsuZEmLYhRzH4sKgt38Oc5ihHYHfYMRolgGIb0idDWS-1Dw4EzH66EN5yKM40wAO2issLGJK3c2GZ2cIOVBOIONu3scH3Igxgdpf4mQWsLo1kjhBpi5CvdkMkBNJ6VZY-KQC_5j8kM-dELzL8BE--_3H_4WXwKc-1tJsvIf0NfNyc_PpVHFpLagXa_vGDzBWA0IhUAVxC2-WsTIShuYzfWWJEG6jQ_z128Uo3Sm3Z7K3Tz6bMxrzQTxFpHesZi35kA70T7bUDJ9WyuD4jrqWtmUOJaO57P0WD_F6dJ9nV0_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d72c32eb9.mp4?token=abJhs_g9kB9OmGclWTnBX_aXvPOm8sqZmPpji17e0GGsuZEmLYhRzH4sKgt38Oc5ihHYHfYMRolgGIb0idDWS-1Dw4EzH66EN5yKM40wAO2issLGJK3c2GZ2cIOVBOIONu3scH3Igxgdpf4mQWsLo1kjhBpi5CvdkMkBNJ6VZY-KQC_5j8kM-dELzL8BE--_3H_4WXwKc-1tJsvIf0NfNyc_PpVHFpLagXa_vGDzBWA0IhUAVxC2-WsTIShuYzfWWJEG6jQ_z128Uo3Sm3Z7K3Tz6bMxrzQTxFpHesZi35kA70T7bUDJ9WyuD4jrqWtmUOJaO57P0WD_F6dJ9nV0_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلوع خورشید بر فراز تخت فریدون دماوند
🇮🇷
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/680548" target="_blank">📅 12:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680547">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCGJ8Yh2jML18aXTHuszp1gfJoJFyOJC6Qex4tesSwJ0POuEtHL2uZoOb0dFiuCUBJcKYCwlWwrGH12rFhapVgIDNcaAlvpCcFDomb0nZ8ECPpB2ZzEAkxPWxQarlK3V97wdlLcDtq4rNCuJHWMYm7ONkJkBFdJ3IuJIdTbcD3HPjRhnO8j5aLE2CvdKGrkqCAZR9s_0X3K3CUWGR_ZhCVhk92asK3C9e2FUdr4BQaxFKgxKe3mqtGx9YfF9_3m9KPVC5DZZu3CIcpi-8k0eq_tvGh3abXEtB2gh4RZiR-_Dc9WQdEyPViXwdNvUKz6H2jwDGO1nTPu1H1PcFJleHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرویس دهی و خدمات رسانی متروی مشهد در ایستگاه بسیج خط ۳ برقرار است/ اتصال خط یک و سه در ایستگاه تبادلی
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/680547" target="_blank">📅 12:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680546">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
لکه‌های نفتی به جنگل‌های حرا در قشم رسید
🔹
بخشی از لکه‌های نفتی وارد محدوده جنگل‌های حرا در قشم شده و نگرانی‌هایی درباره آسیب به این زیست‌بوم حساس ایجاد کرده است.
🔹
مسئولان منابع طبیعی قشم در حال بررسی میزان آلودگی و وضعیت جنگل‌ها هستند و منشأ دقیق آلودگی هنوز مشخص نشده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/680546" target="_blank">📅 12:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680545">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261223a0ae.mp4?token=JXy6R1alL4fX1gvcSpXasD3qvYpz62nxcSVT6mPt_4zAyJDNHTbU05g2RAQ-Pw9FEaKM7t7sPTKoUdykt7d3iviGFOBAgDNtn0s4-at7UWaepElj9VWLknta2NRbzJkOW9vAZ7XFegd8alxxrtHGkbugcAOUvIi1RAFsAeh9biOu6SH_DCtT9_akN7LaxD2M-fjL-3qWFywN6CifRmzKS88G07jJC7B6Te5twnC_V9iRBCupjA2JmRg854NQZtyHed6Jih3jdtJI47Q1pliv2b2zjBzxrsqmvCR3VwZRgRKlzwyHgU5H9_zN9-erenLTl9bA-8aLym9_Iog0yPipgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261223a0ae.mp4?token=JXy6R1alL4fX1gvcSpXasD3qvYpz62nxcSVT6mPt_4zAyJDNHTbU05g2RAQ-Pw9FEaKM7t7sPTKoUdykt7d3iviGFOBAgDNtn0s4-at7UWaepElj9VWLknta2NRbzJkOW9vAZ7XFegd8alxxrtHGkbugcAOUvIi1RAFsAeh9biOu6SH_DCtT9_akN7LaxD2M-fjL-3qWFywN6CifRmzKS88G07jJC7B6Te5twnC_V9iRBCupjA2JmRg854NQZtyHed6Jih3jdtJI47Q1pliv2b2zjBzxrsqmvCR3VwZRgRKlzwyHgU5H9_zN9-erenLTl9bA-8aLym9_Iog0yPipgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع سیلاب در تویه رودبار دامغان
#اخبار_سمنان
در فضای مجازی
👇
@akhbar_semnan</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/680545" target="_blank">📅 12:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680544">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
حمله موشکی ارتش یمن به مواضع مزدوران سعودی در بندر «المخا»
🔹
گزارش‌های رسانه‌ای از حمله موشکی ارتش یمن به مراکز نظامی مزدوران عربستان سعودی در این منطقه حکایت دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/680544" target="_blank">📅 12:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680543">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
کشف پیکر مطهر یک شهید دوران دفاع مقدس
🔹
همزمان با شب شهادت پیامبر اعظم(ص)، گروه‌های تفحص شهدا موفق به کشف پیکر مطهر یک شهید دوران دفاع مقدس در منطقه عین منصور، شهرستان موسیان استان ایلام شدند.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/680543" target="_blank">📅 12:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680541">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjYypX6ZmORjKqgug6_tOMNuLwKVr9MkZYE6AJvGOHRwOi4sxuWOVJ4AE0sVHlHbexmJenIonzGlsQepTOfU_UJ92UN08wcGD17WXcLZOqUllVip9PceyT1gqmcxdAHfUSwYaCEs8GcWHRopVJ3RwgldJ5TpULVxutQDc7OCv9gFcsNwNGmqT9eMYDuPuw9OOTGsaVHfC0L89re7_n5mAFM9O-juy3SksbHZqILRzSRb2jE1famSeSJ9im3fcuAlPrceG01oFJ_QGsx6Av-DZ-yGHhpVDE5TdTNBlDb-xCljpl44taPoQJu1lKYGlHpA4R_93K0eMvQi-wlldn6yYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقاشی منتسب به آدولف هیتلر ۱۹۱۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/680541" target="_blank">📅 12:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680540">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
هزینۀ اجارۀ نفتکش در تنگه هرمز ۲۰ برابر شد
🔹
کرایه نفتکش‌های غول‌پیکر مسیر خاورمیانه به چین به ۵۰۰ هزار دلار در روز رسیده؛ در حالی که ابتدای سال ۲۵ تا ۳۰ هزار دلار بود؛ افزایش ریسک تردد از تنگه هرمز و کاهش نفتکش‌های در دسترس، عامل این جهش اعلام شده است.
🔹
یک نفتکش ۲ میلیون بشکه‌ای با محموله ۲۰۰ میلیون دلاری، برای سفر ۳۰ روزه حدود ۷.۵ درصد ارزش محموله را کرایه می‌دهد؛ یعنی یک بشکه از هر ۱۳ بشکه.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/680540" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680539">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBT3tn2kPwhFZne2pGEXJK1txWlGd9FR2s5MNs4YuXVlYSzBM_6RVqzxw2f2iEk567-gA3cX3Dee1Ht1Itu8dpjnN4YNq72cCGsWg2_r_8KbHAJm4-yw0_gC6ZdvWdRCQ--jT-qJ-IFoJl0Jhe5vLV1ODSS1AZWG3S6aVUSnbsH41apWwRQcfjTWgBMzhR0_NeC2NXjcPC8L5fxg-Dihdn6slcpimm0omO7_-35fXuzQ_ClA-2iNSpUSr5oQW3oroOz7AhvVnxrTVGcCJ-eJZaMK79aL-QN1EU25sqQNEoOTgMbfFUpALmiD_Vc9sZsxe49JSwAJFxEnrM-UMR90iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلون میزراحی، تحلیلگر سیاسی و فعال رسانه‌ای اسرائیلی-آمریکایی: تمام جهان غرب به یک فاحشه‌خانه انحصاریِ صهیونیستی تبدیل شده و اگر ایران نبود، بشریت هیچ امیدی به آینده نداشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/680539" target="_blank">📅 12:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سردار جاویدان: ادعای حمله زمینی به ایران توهم‌آمیز است/ مرزهای ایران امن و استوار است
فرمانده مرزبانی فراجا:
🔹
ادعاهای مطرح‌شده درباره احتمال حمله زمینی به ایران توهم‌آمیز بوده و تحرکات دشمنان هرگز نمی‌تواند اقتدار و امنیت کشور را خدشه‌دار کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/680537" target="_blank">📅 11:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680531">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyExXOoCgyyWKX69md1imvE7nGmnqldbDOQXN7Rg1j0o3tZxpyVDbEbdnq4Sz6i9ET3k-Ze8o9Mazd77kG64qZi_I2K18dLQXw98dA3m2dhyIOcCg99-RlbUnDM9P7SEz-nbJKV7Tf5WBCKQSurPfqB1Ih3EEfa0m53buFl2hXImiJhqFNAb3RtEa4sAxARs3eu-5pDHSCRLlDI1YvumFV61zFQq33no55UHJgVz1sHAxzGNmUMWNpwf9rpwQENoop0dLlso-Romlt28ElZLhAIZmtD98GcMo9oUbEv_XFEs7LEXyUFmnvJzFr1jAHWBU-8sc_i7HECoFQ1GQyzBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5OVI_J00l-r_p1YFTB06wt0yi5PafDRAy9FGNF6lTEA84ciBlS1rIcDmJgICSq4FOJ6uOhWQ3-2NZ-ntsRC_Kf_9Q5qk0AJ0eJYlB5G03iPBLB_9FyoWi6_A7zX_tEXgBhf0B-995iJulopxAI538rf5Qr7QsuiTy1Vm53-jl7ekWeTdyfbWdcgc7KKTvAlsK6Uqi0SHn6TiSQXX0-iQ3S4qA0GoX8qLOaFTMb1AaGE8gTH3kkh-5mkLxcB1hnrYQjk9H-BUa_XxWljQ1LOhket2MAr2pqPsRFu87j8v2CC8jIH6eOrYrxOTiFYH14Vi_r63xyOsd2u_2DfOrQ0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIVfWfv_TsayUyqdsvFBmE_RQ0psEQTApZFOE24d_YzCuWhuShmd_aXtcKSq7tS2V0Ija8FiuUPaH2J8XymFudNkH8N77ga6S7mcdocsonEEeCqYvRg_52F3WWyFXdS77LQ745Ezy6NzWjNfW27D_hht8bRMGhXIayeGxBsK9uiMTenNNDWaI0_dC050jj0rR8pt1xoWnRv64P2UOH-STfFgy02Set22-jc5dbOU01B7pzY5wiBh7qZi7Y06qpKnXPZQ_r3AzRKtRRXLgvojF5AeB4ihV3reYfDumFLWqJLUNVksHukwlCdb-YqhZ0ea6CnMgT8bjZBRGI6ucHOlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5eIQqJqX9Bxcd3Whq7R5XbbKPWaISI-943IYm11IRzjF5rICfsXc2C2DtDtH1kImoauObMhTOU8BTezqxxE6X22LLq2w4aOqWQDri7S2u5eizLqYCANC6cIeu-hW3k9clgRy1XOrTj3TT9xkQnms9hWIajxUzLbieKN8jBMTWSFfwqtaQf1HWwRwhh9-Tl3p3zQAzPeY5MSfyPINFyl6nXcXQHjG3ao7MxTasiCYmd1lWL6hN6_zogAOLlbojLZr7Kg_3PziOUHMAEuc5x_36c_lZ8wv0xDxlZ7Cfp0KihzobgB23BOBUOb0vfFtuyl113u_tfBGY9sb4q56OI2ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTy3huq-c0aVM6-Qf6mFRQEXItOTNe3XQF1jBY6QXUsWErthdnCdHo5q-r9QeBepAR1LoU3ifjjyJSCYh51xhHLKruey-KnL0X3qrRc1ES5z1Ao2spQH2O7QKfseAeVdkDasYW9IGiyCS4aV-W_yvK5rDHpN5f7TZarQ_y9l1AYUqy9TXbGOqhRsBuL_6O6YUFA17F2AAtsBpjxl6oX2LBxj2i0FIH4cQVPesNl108nSIMHv898j4_8xjXMxmyX9SoB9ut6-GXvnIHevodysZ-ee5PoPuxhMP_aafdgQnrhxkZ7AYbo18yU_RXAFiy2qGW9S1XBSQXJcUujjGK2Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvabj3dCO9NfpzsfWYP4RohUCl1aL4Cz5IX3qL8MtaFCcgKbavS2Y6fblQC2Lqd0vUHGFA41nxPUaY3Uq7no33gJM1Wh9lPujpQk7wAGkWwW2IvLKivqOza4CYDHcs5oD0nXUKtnrFvoCaCJs_qVmejYMW5O27Bk0Q-7F1yrA-EzGaAZRUg9baEBI25jZhq42eZcqPuxl_WOCrq2fWWFRlhY-_RWCM1QlW_94b8PF_ZCfRXvnAgZfAeb1fWX46yVuRNWhNzf0tZjsKKp1ZGmvICLS_estOE1if6Xv681nhn8VE7wDNEswkxInP8uuyCJ2kr9Y9zt7AoVmCOZDoQFKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تهیه و پخش بیش از ۸هزار ساندویج در بین زائران پیاده امام رضا(ع) در موکب هیئت قرار و کانون سلام
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/680531" target="_blank">📅 11:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680530">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/680530" target="_blank">📅 11:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgswgjwAp0zZ7zXLGYsXINO1IngGz0s9S7XlyfLgqGFGFXUsg7jnnmgxOFuG5eRuDt1dyI__wYXlNJIuuRG5kJn3HGcwvpsdBG-hGodYr0Z7Ii7PbNRCAAdAmlfCOEh7sEI7FHGS2paPbwelbUeuxt38GuqQ9Z54Y2RmbhTQj7Y6wVFwRqnomnHuXF_4v-dSOED0QiouJdhwC29xtPlv_X-E6xami8q136WwWatHtgDRyDZgcOXB7dt-KEiBlzlAZhqu3SUI5534lApMhKPeqOTHC-lv3NeaG8D8z6efG6Yphnx29R1NeL4_FKEDY-slF_JO3Fd1qAxjao0ZGo91Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3BH-JAldyCa-k60ePC2Sl3GbrzMnMsy4Wk0eu-GU-LqerkTL1NvzRbWA6cSc6t3KVfWkfqxQpIhEoWBzH96tf5o-ikgUVIgO8JapNCCaQGIkPdFKjcBYbysR2Xqk9TRQUZyygHy42sKF7qxtPxoRYM5s0tdMdxlzBJ9ncoAmaVG-sW5ZYPTBnY9xfJ1W_3GR5Ea4imVF2KvFYDonyvn_5ZIT5xmoVIBOmqBFVRnIB62uk3eDnA8XocW21i593GRZsZ_GR7u_Lvisb_ByzOcCIzdD742nXnk2cSbyO83ABdTLaSrJVsnXjZEypIKqHfEGvpXmvHDgE35QH7JVx7hSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این یک دیک‌دیک نر (Dik Dik) در پارک ملی اِتوشا در نامیبیا است؛ حیوانی با ظاهری عجیب و بامزه که واقعاً شبیه شخصیت‌های انیمیشن به نظر می‌رسد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/680528" target="_blank">📅 11:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680522">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqFQol-Ymy8-bu88HnshFpdybL0W0qV7qvoyL6_8ZjEvWCwUi7f3oaJtOV6l70pckK22CwQwOQtZ9Prc4iNaB68JpDkpShdXAovcr4OQ8MftTo9tVHaCe3LqzOUByF_GlZSa1WgZjxxxPY2KHxXFFahPggjCxB7msOwY33Z5nHFlUZkFJ0X5IWbxgJGKxHtC67PDoqkt9KBSrFhw37IpeEZ3ISvXMI7-gj8Bboab5BfaCJhSZ411dhHYrt1xCandNiRl6S2tUAIdmJol_f9kvkMYXRFlM-SDH3jHAb-M9p49hczusoutscZuUHG2Fqu6PogYoizUWrxz3hDnB1r5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af677bab1b.mp4?token=kO-983VCMM_LhDAFsHCb2C2EkbJUwLhutiZLwKMFOEpB9wAGCZ_drRggu4c6idLltjwsL0XnqbxAaJmXMrcxTLiv9J5XShH4hsmfnyWHaZUrMXuPnMaoXqxs6L9V8By4Hpymv8igK7eMt9Em7UBe2FmWvnfVndRZkBbbB3uRudlBTZQsCUrj91c7QB6bZny0fGyJHpDRgEn3Zti-hHREoFPNvKVjFhKx1ejLCCVKqfMb50TU4OtJriiSVHfM3KdKjk3IsYKGq6g_I7FhPnZ9Zl4vWFC6eQ6UW9uFffjN-G-JCTP9WcyYdgDWeqbdeXrz0dNUguGAc1_yqLjt0kagWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af677bab1b.mp4?token=kO-983VCMM_LhDAFsHCb2C2EkbJUwLhutiZLwKMFOEpB9wAGCZ_drRggu4c6idLltjwsL0XnqbxAaJmXMrcxTLiv9J5XShH4hsmfnyWHaZUrMXuPnMaoXqxs6L9V8By4Hpymv8igK7eMt9Em7UBe2FmWvnfVndRZkBbbB3uRudlBTZQsCUrj91c7QB6bZny0fGyJHpDRgEn3Zti-hHREoFPNvKVjFhKx1ejLCCVKqfMb50TU4OtJriiSVHfM3KdKjk3IsYKGq6g_I7FhPnZ9Zl4vWFC6eQ6UW9uFffjN-G-JCTP9WcyYdgDWeqbdeXrz0dNUguGAc1_yqLjt0kagWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شهادت پیامبر اکرم (ص) و شهادت امام حسن مجتبی (ع)
🥀
خلقت چه لایق است که صاحب عزا شود
عالم عزا گرفته و صاحب عزا خدا ست
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/680522" target="_blank">📅 11:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680521">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/680521" target="_blank">📅 11:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680518">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCMJgwoqg-ONbDE1lDcPZM0KPHIBDorDfhR5SxYsGuzX7lTbpNrV6uYcneMJD5JsZLKmtDu3SoURfZu4kF87TeEHcjfv_jq9kFPP6X9__SXHfyBZdhbn85X7X2Db53Q0nWLf7fz3IMN0chyTkF_ACkh6yAiTe_i2erZs2zwU2qTD6A5e4LTGdEe7E4eLMb6x-OnIY3yFaduGv25voLaEtDjY0yh5uaGGdMowfS-j_m6uVpaN_Y4w9yArng93bzdWWpTTjPkWIOQwf9ucPnS-BYJhnUTH_xTktXy8iHy-Mb9x3gMkLejc8F30S2a3bQTZqBIbISYb-khOv8bltUh5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید انقلاب به روایت خودش: من بیست‌و‌هشتم ماه صفر به دنیا آمدم
🔹
من در شهر مشهد، مرکز استان خراسان، در جوار آستان امام هشتم، علی بن موسی الرضا علیه‌السلام، در یک خانواده روحانی به دنیا آمدم. زادروز من، بیست و هشتم ماه صفر سال ۱۳۵۸ هجری قمری است.
🔹
امروز ۲۸ صفر مصادف با میلاد رهبر شهید انقلاب است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/680518" target="_blank">📅 11:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680517">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p674YY1Pv4yAwXR9RT7g_aqdv_ZckjxawrR4O8CMTo4REEiWiUpYFr0D0rRlqkru7KrZiRPEAvUYj6lGDibwF73kes0h4kCQLebDsHSL4ND0zJcQILYFvsUpwTQjB-S9ii7HDDan3isTYznRTSdPXNhrOULA4Dyhk3xP9d2vV0xTAE0-NYXhGox9xwIbkOauNDt7lgjBn_o2T5SLjAl_Eo84Kmk0dGXqfjfCHctzmdP0rnhUE0tdiy0dghUmcI3Y2zQtE-BeXVTV3SSccKoQmh7uRm5hgLwFeAd8AXf_DOvfQkQJhb0tqQwKHTIEHXP1dpDgYkbk-BGoGtOKqkvJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
مراسم عزاداری ایام پایانی ماه صفر و اربعین رهبر شهید
◼️
سخنرانان:
آیت الله کازرونی؛ حجه الاسلام دکتر رفیعی؛ حجه الاسلام پناهیان؛ حجه الاسلام علیزاده
◼️
مداحان:
حاج مهدی رسولی؛ حاج احد سبزی؛ حاج سید محمود علوی؛ حاج امیر کرمانشاهی؛ حاج محمدرضا طاهری؛ کربلایی حسین طاهری؛ کربلایی حسین ستوده
سه شنبه ۲۰ مردادماه الی پنج شنبه ۲۲ مرداد ماه از ساعت ۱۶
و ویژه برنامه شام شهادت امام رضا(ع) ساعت ۲۱
📍
بلوار سجاد ابتدای بلوار اخوان ثالث</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/680517" target="_blank">📅 11:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3162146fd7.mp4?token=i3YbJVLpHF-H-vAFQ-6iwzLWSmxz-rE2y51sxaSN1yz5cdChDkrLM6oE3DvLkrEpzZilooIPUDyaDE8ge_B2RgmNSq2vNztVE2kt93n-ZaMC6wioW06Tbuaisa9u5wHq1McR-3Edu1drNnizPSr3GYYvYcJK_RJ7YS5K66hkxWScxvt16h-4UgOFRC41wovaTT1YFI5E3OGJc0JqhfN6fFZE9Kv6FCyyZqlJw8HBJa_z_Ril4ikGkg3eOS3TFB1s7SFlYX7dE-n3U8SU5qL7hPFp5zxcZSx6yrfHsews6qIuo7S5ZlQONUlpeQUz3ro76AYWM2u1KWhDpygs5qnyFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3162146fd7.mp4?token=i3YbJVLpHF-H-vAFQ-6iwzLWSmxz-rE2y51sxaSN1yz5cdChDkrLM6oE3DvLkrEpzZilooIPUDyaDE8ge_B2RgmNSq2vNztVE2kt93n-ZaMC6wioW06Tbuaisa9u5wHq1McR-3Edu1drNnizPSr3GYYvYcJK_RJ7YS5K66hkxWScxvt16h-4UgOFRC41wovaTT1YFI5E3OGJc0JqhfN6fFZE9Kv6FCyyZqlJw8HBJa_z_Ril4ikGkg3eOS3TFB1s7SFlYX7dE-n3U8SU5qL7hPFp5zxcZSx6yrfHsews6qIuo7S5ZlQONUlpeQUz3ro76AYWM2u1KWhDpygs5qnyFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استهبان؛ بزرگ‌ترین انجیرستان دیم جهان
🔹
استهبان با بیش از ۲ میلیون درخت انجیر در ۲۴ هزار هکتار، بزرگ‌ترین انجیرستان دیم جهان است و برخی درختان آن بیش از ۴۰۰ سال قدمت دارند.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/680515" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlefbayesafar | الفباى سفر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyqUX58I42yxUjoWt7-csV3o9GFdg_LneH5WTILCoS50mX71xFPhdQLXDAkXj3S8STaUFdpSifb1d5a2COiFiKWiapeigG3w5ik52bAbJYaVSdCPrSv3kAio9RjKh9SNaTgk_owXOsK5R2au_xQy0XgEULCQKWNDmte3IL9dXVi7KR62h1hFGPJgBAFnGTxVbM5n7y55vY64hMolE4i--ftYNsfYzWnFDV6vSPjBZlCm9oaDpnfd8ABCWnVoWPdus2vvwSWfpJwfGKRoA7FaxztVrLrr2z7JMSgJVcjRvkC2W9MdGb3N7ujSeKZ0-079Dehy0OkQHVU2N1e_Vnv-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
آفر لحظه‌آخری مالزی | تخفیف ۲۰ میلیونی!
این آفر رو از دست نده
🇲🇾
قیمت پرواز از
۱۱۹ میلیون و ۹۰۰ هزار تومان
به
۹۹ میلیون و ۹۰۰ هزار تومان
رسیده؛ یعنی
۲۰ میلیون تومان کاهش قیمت!
🤑
🚨
این آفر فقط برای
۲۴ مرداده
؛ تا ظرفیتش پر نشده، رزرو کن!
✈️
پرواز با
ایران‌ایرتور
✅
حرکت از
۲۴ مرداد
✈️
مدت سفر:
۸ روز
💸
شروع قیمت تور:
۲۲۵ دلار + ۹۹ میلیون و ۹۰۰ هزار تومان هزینه پرواز
🛫
برای اطلاع از
هتل‌ها، شرایط تور و رزرو
همین الان با الفبای سفر تماس بگیر
با ما حرفه‌ای سفر کنین!
سایت الفبای سفر
💻
اینستاگرام الفبای سفر
📱
تلگرام الفبای سفر
❤️
☎️
۰۲۱-۴۹۳۵</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/680514" target="_blank">📅 11:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAZlCrRSokDkbPku_QvOg5nzodYhoe7QE7rcoJcHsijoi5s9wObbW_fyCEq4267BCOsN6B0zenb4Hpvui0lCBF3x7dkyK04JYxI4C4Eljz6Tt5JvhDx-8fGDinEz0sfaOfs4STeEAWflU6ovTxKffWscZlMAuY2sXWX3oa_ajsugEzqsLJ7FLsDT4aaFOPt0k4eZudaOYAU7orW1zwMW04dqjXqxHyRgFwOa9l2OhffEr4ISpmpyihX3Wek54MklMFuuhhYFTZdsj7d4LUrLJJYX0BPExu6IK0bFzFFuoEAgc25_SLczaxVPwQttHRld6SLsg1OPjzwZbix01oLuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nok5ACmBs6MwGsWt7ieiT4veoTMegRu0KgEbHVjr-UndNm77q3n559_bnP3qBEpxo4DAYtVo_HdcCG2dKyrGqUnPBoRy-zQJNt9PgTVB60cRoDqL1Szb_Nr2krkNp3u8UlUz9HgPFIPvTjtqcT-6VEsfgjDNd9t0yDL8RdT-GVo78T4ZGy7m-12yuTCtsD18bIWM6zzdr5yrB9DzD8BiIym4H_0yEyTbrMduRjRCMcmY4OzkTrrmn2myvRSJnGsVmOZKX4Hl8FB25JoCFQjMFCsrr0lYAANBqAORkMhhpEAlmh2xfWNTCBv1jzqeoEf3KBX9kcOU5A5qltpt9_fa3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxu_9w4ADb0W34dHLwLhUuQVgtLs5RAHSNgTtkEfnbYQeAOs5qiy5lXmO7awMv1n811yCv7cuEUSWk3s0BK859yuCCjvdm5twTR1l_ZMThejLPaBmfPD7BTcAZT9MbNN0XXO_cN9txZAbDs61lfGx4ak6QjxvtVA3PbRjCiBYKuoY_kANCD-c0nLg80XjWPe7rASTxhV_FuBy6yquCt9lNBf4eKym0pN9w42B2uBtLkkj4vB42wp53AJbkK6HBr-fIkSK2BITTX5sLjQphALb7djJHX59al_eSxMCwR224i_4N6E52FIqx8eqjbJSpcMSgeKTnSC7pqfZUa0Bi5LCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OnLTM19Xv_vYRV1B7aCF1iFGr3Kz1TFATYIdmk16JmOWln-DuFKVnJDLS9bR4xpIBjMU3knFnQvBUqhzvbnu8DlfmmY2iRDqbS4zNF8JUZ3bGrYc6Rj7Nm84t0AHtPYtU6KfUoMfJrEYwcEqVB51FeIoouNcMaS5NsrUtc2xRn3oMUQh5y0UETgKVKsODPBrSQtsRqD1AhXVeX-PQxViKV_N7pBtJOrSnF3nz5RK_nUTyiVZ8615U--3wvMSGTl2SIgUBVApvPyXHGd_YICwKVpZ4nvrPvEqlqkzpD54Zbudq9AnEYrimUBP2U37FlZg1YdnajoGWxcVla-RETPoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BquNF3fZtSZSJYXwTj4HQgpiLGdSp1jAnFsSib5-iPZRSzPDX3wAfRhcu_De8N_EkSZRclSVEA08Ut1Q-pYclXuYlIi7Y-GFfwnP4cr5N1PBgQAwoVQyQ183uQExQi9atBolYwQHAx0bEPK4MQIf93WotjirZ_OOF-Co-uhDocRo9HKGpbHrzppUe_lDHQWDrg2eSXZXt79HzuRt8mzt7uKlKyYjtPvsRSmolBRz4pTxEhFJsV2vWzLEHCyCzWyCDornNpCCC0bbhmQeYDrTT7ACpL1g19ROZfV_n1jUFzWEloEbIkXhf8iu6FPwJpSzdg6xmCpg9Et1keE6Dbl1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoUM03krx41EGl11n6muV5qy_LIsk8BJPHWClBM6Pbc3O93OT4fWZkKR_g6AZrw0DrVX0QRyLvpg5nvNBP79dnRGSXw6IBcMH-YZftZkxauv-4qGW7aLU2gVJoBu_c00J6hxS2zMDfwV9nHlyr2C_bQR_o-jOYvyAKHQc9Nqb50-BYjKw8ApiHEpUV9BGfwooYWHov-fVzmwrCT9bhwT7DHA8ckuxv7yCKBflrlKfQtBfJ33LlZt1U6vK5voosfyrbudDmMG0AFbcs9JgE9Srvi_91WS2VbzLHzqFZhAL5KHrzJZJX2FaE_UF6T5KooOp-_abqFKYHkwDo0f-BWn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbKsnEZxMdnNozvkCfV01m5crUaamcKJrH5UhYKbrqtG6Radds_gaBPcudIBwUqxH5HfnGjecFFfLPfZe4T2VxodOHPzHqvrfEUQjlwTyTi5PDEGW71EjjxDTcS2K6KrKCLyOyCa-MQeAZ8Rj6rV6WrdveWTVePHfwWa2o0vdD_SKa-2S8TdyZwARtBZD1iYPV2QHzrc7Szw17jjhEzhR1DAOeqxGHs1nZnYnJKBxvYjxvqU8QedVuLjcqgooxLbRrfyEdq14ieN9i2ELOd01OeXMz7Dg0x3lEzymoWN2DJTmP_xfJKupwjew4LOQe5Cz1ae0sWKaI4N2n_fb2Ddrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUKYIlVD-wkllzoajN-3bOywzWK8ZWY5aZF1dapTXaKjW3ntq04WNjYGhlik9C9FGsonY3gw4eMX_d1KFPfQrU_Qj3h5cYI4jNXj-crk5mbM6GIoTyzTjf2FikyV_A9smph_GqUlhbO3hMGzytBz7lwSXNX-BcLFp0pd8VAuSn9N9ABcETXAl9l9R-K-pE81I6CdoypNo6DNqdw44afSaIqHlMZF1U5WQIJ2tCVLS-cz--UVPF04PcPzFYjCLinKD38oZM2TPulj-y3zFsOtaRv7hC4ftQBDVrNhC49uS6Zehw3CYROzB4ZR_Q2FlA6-t5ArerWvSA6j2CwkMwZDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0CXKio3N83yvMmnQohatqdkkoyhr3VZCddA3Q5dKK00lg2xo-MajPsxqjfrpqS2WQuOnJbqZ2Mcq1YIeFViZRFDR6ee8DichIuSw8koYS0Ot_-Kzy_f54v6Pb0FgFfSpx5yiT7trYmmOKvVB0ahGY5GdOJCSKrdSXXzB1kfHHfCNp4FZfeA4TzQGGraHYZFcnkwrA1k3tNsDtSrQXBoacrYyHk0h2GHcm1TO2HQ4UPKX9iCZyR4ZrdDBAk38gimL-9W2tWpliCZBFMKI4tF05h-SIkciYcTuBCqfYeDwY-hMbD6diTYsUFVBPzCtDHgEvzJ5UmaRKFsvunot30xbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خدمت‌رسانی به زائران پیاده امام رضا(ع) هم‌اکنون در مسیرهای ورودی به مشهد
🔹
در موکب هیئت قرار و کانون سلام در محل تپه سلام منتظرتان هستیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/680503" target="_blank">📅 10:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680499">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
مذاکرات ایران و آمریکا درباره تنگه هرمز به نقطه اول برگشت
ادعای خبرنگار الجزیره در تهران:
🔹
مذاکرات ظاهراً به نقطه آغاز بازگشته و توپ در زمین واشنگتن است؛ تهران ممکن است به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
🔹
با این حال، تلاش‌های دیپلماتیک و میانجی‌گری‌ها ادامه دارد و احتمالاً در روزهای آینده نقش مهم‌تری در مسیر مذاکرات خواهند داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/680499" target="_blank">📅 10:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680498">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12f75205e.mp4?token=be3nSY7sWOPCApxtCjBvilv0EWE6AuqoLoRAgZV8R-epgcjIL0_UWUOJwRR-Fj5YnSGKpswnM9PbEXTSxsCeZHAn0_uwAuOSiFE_Ao8p7Rr2V21tN8RY8fXPYLk8PN92nOmedB_zI0SQT2NKAEfMu6OVlsl9yf7lfaiIG8WiSmNS4r-Jcc2OBZTVaht_UvxwYurXsknfqLZEF0SSSvEdQY-fN07_7R7HPSXgQgblEoqWI5IAsafXBo4dww9xKfF0u7Y0jJwnaEISuLGX6064dQfhQgRo2VcsDAJ7L3vGFXXPh6f0jR9mU7lcjDXCnLxDLhuJmWWTK8-7M2TMi8OLKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12f75205e.mp4?token=be3nSY7sWOPCApxtCjBvilv0EWE6AuqoLoRAgZV8R-epgcjIL0_UWUOJwRR-Fj5YnSGKpswnM9PbEXTSxsCeZHAn0_uwAuOSiFE_Ao8p7Rr2V21tN8RY8fXPYLk8PN92nOmedB_zI0SQT2NKAEfMu6OVlsl9yf7lfaiIG8WiSmNS4r-Jcc2OBZTVaht_UvxwYurXsknfqLZEF0SSSvEdQY-fN07_7R7HPSXgQgblEoqWI5IAsafXBo4dww9xKfF0u7Y0jJwnaEISuLGX6064dQfhQgRo2VcsDAJ7L3vGFXXPh6f0jR9mU7lcjDXCnLxDLhuJmWWTK8-7M2TMi8OLKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطار مغناطیسی چین در ۵.۳ ثانیه به سرعت ۸۰۰ کیلومتر رسید
🔹
مدل آزمایشی ۱۱۱۰ کیلوگرمی قطار مغناطیسی چین در آزمایشی روی مسیر یک‌کیلومتری، تنها در ۵.۳ ثانیه از حالت سکون به سرعت ۸۰۰ کیلومتر بر ساعت رسید.
🔹
این آزمایش همچنین موفقیت سیستم ترمز اضطراری را نشان داد و قطار پس از رسیدن به سرعت ۸۰۰ کیلومتر بر ساعت، در کمی بیش از ۲۰۰ متر متوقف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/680498" target="_blank">📅 10:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/680497" target="_blank">📅 10:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680495">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2685de5d44.mp4?token=LB3VkCIA1Vo3bjeOddbpjph_1nGxM3ksGBTEmZpp6FBYT6Kp1FcLYubVBJcZPHzYtLchgUZNbTlxYcsM_OaFkabnnqNQ81_jtVELUNs62WHW6-65nGXcAklGertEKKh0PNeERxT-_jtxrEDrRYl5Nu3cLr2tplbhP8h-08p2FRPGa8TtdVUqXXlWya0Ptvs_lmPx6Myg80ffj1O-vjRxWQzURtYjGLY5jGvMP0V7l7xs4pFjjzRb0wV0usx37tcrLKnhQcjJ8shsMm305oVpnET9Ka4WLAwLXgEv0H4FRI-yDz4-LtPcHeKLhEn0vWrUkf3AXTzPi4TwG4daRyZHmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2685de5d44.mp4?token=LB3VkCIA1Vo3bjeOddbpjph_1nGxM3ksGBTEmZpp6FBYT6Kp1FcLYubVBJcZPHzYtLchgUZNbTlxYcsM_OaFkabnnqNQ81_jtVELUNs62WHW6-65nGXcAklGertEKKh0PNeERxT-_jtxrEDrRYl5Nu3cLr2tplbhP8h-08p2FRPGa8TtdVUqXXlWya0Ptvs_lmPx6Myg80ffj1O-vjRxWQzURtYjGLY5jGvMP0V7l7xs4pFjjzRb0wV0usx37tcrLKnhQcjJ8shsMm305oVpnET9Ka4WLAwLXgEv0H4FRI-yDz4-LtPcHeKLhEn0vWrUkf3AXTzPi4TwG4daRyZHmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون استقبال از زائران امام رضا(ع) در مسیر پیاده‌رویی زائران به سمت مشهد در موکب هیئت قرار و کانون فرهنگی سلام
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/680495" target="_blank">📅 09:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDgusxUAH8YLKqUHCTRyrdS5ljdUJPWRpmkkR51zj7pbPKF_-yTfLN2ZOfLifYO_W2dm3bLiw7TarU9dMnXG4ZEpxhOs1TdiurAMjwjYl2AR-UmbI0lkhnyvM7UFl7LhvTmIRobdK6-kuxFecOV1zyRfn5bAznIy_JF1G07hZUNT4B73RK9CVu9ci6z1FrJK9BtBz8A263_-vmZdyC92KU0rv5kJCnrdGvXoBcLOl4k3ncY3loItCaZ_rDm9hntth86dvBbTbDNOTQWhYTrwWIn19UwWN6KmH5F2r2bkMH1m1P7N_bbZLOX-nTgyrUBLs5dkBjpS5T4tPW-RANbehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار مصرف همزمان مکمل‌ها
🔹
کلسیم جذب آهن را کاهش می‌دهد و زینکِ دوزبالا هم روی سطح مس اثر می‌گذارد؛ برخی مکمل‌ها را نباید هم‌زمان مصرف کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/680493" target="_blank">📅 09:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680488">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5zmpkY3wqADoyU4nwEtsziNFYQEfN5z7mUOG0q5oLeuqHJaNhgd1S_F3kDc43wcyPsjkiJtL-SMuxf-uq0Ovs60ERFZVTKaFFCXXysP7JBc0yuUnwsoq5VoIOfavEmxIu1HrM21m4YIutLLzFGfPhXlN0ziicVAGh60twjW6OqBCGus32OCih4kcNqDrRxo07VcZ2w98eHptSALTqxQ0b4P6Mer53Qj5keTPzyvifPA2j6KRrud8DjVw0pr9x0OaWPDFqkbbMwaAzyVFoAG9_hLclnvlxwRFfB1A0ysE23bBN8QcLvrowpfgait9K_6KHvB_5EGUHfqqEcOfIgVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برچسب انگشتی، پایش مداوم داروی پارکینسون از طریق عرق را ممکن کرد
🔹
پژوهشگران یک برچسب نرم برای نوک انگشت ساخته‌اند که بدون نیاز به باتری، میزان داروی «لوودوپا» را در عرق بیماران پارکینسون به‌طور مداوم اندازه‌گیری می‌کند. این فناوری می‌تواند به پزشکان کمک کند تا دوز دارو را به‌طور دقیق‌تر و شخصی‌سازی‌شده تنظیم کنند و بیماران را از بستری‌شدن در بیمارستان بی‌نیاز سازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/680488" target="_blank">📅 09:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680486">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
هشدار سازمان غذا و دارو: با توصیه هوش مصنوعی دارو نخورید
🔹
حتی دارویی که برای یک بیمار کاملاً مناسب است، ممکن است برای فرد دیگری به دلیل تداخل دارویی، منع مصرف، حساسیت یا شرایط خاص بالینی نامناسب و حتی خطرناک باشد. بنابراین نمی‌توان یک پاسخ عمومی تولیدشده توسط هوش مصنوعی را معادل نسخه یا توصیه دارویی شخصی‌سازی‌شده تلقی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/680486" target="_blank">📅 09:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680483">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed5443e66.mp4?token=SHsLuOwgdJEajbMj6E02j7C4A6hBDWQuKvPqMNWTt6Gf_Y4obi5H-m07VfOtgAUEKkSLcwFipc3OQLUovQjSEwcBUFyLjDYdu1N-8_ndXC1J_qIqib482fEf4STFFWlyApAUwTABsF20maTje3v6fbD2cy8CsiP9y9hOjcTBwsZ9CZGI_b3hKcmbY72pcS82iDzotZiiriSzj3phTMQifnTKCu5T0cuNrd2K10Lnsw0Yzd0o36t9uQU9L6_9-PblUkSOO5H3arJZ6UzrP5Hdje_NQFV8o52O8u5muPsASrDmbJ7Mv05CbK0D_e2mSeWjmY0Lf9mX_G2JdXgByiqJDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed5443e66.mp4?token=SHsLuOwgdJEajbMj6E02j7C4A6hBDWQuKvPqMNWTt6Gf_Y4obi5H-m07VfOtgAUEKkSLcwFipc3OQLUovQjSEwcBUFyLjDYdu1N-8_ndXC1J_qIqib482fEf4STFFWlyApAUwTABsF20maTje3v6fbD2cy8CsiP9y9hOjcTBwsZ9CZGI_b3hKcmbY72pcS82iDzotZiiriSzj3phTMQifnTKCu5T0cuNrd2K10Lnsw0Yzd0o36t9uQU9L6_9-PblUkSOO5H3arJZ6UzrP5Hdje_NQFV8o52O8u5muPsASrDmbJ7Mv05CbK0D_e2mSeWjmY0Lf9mX_G2JdXgByiqJDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعداد کشته‌های زلزلهٔ کلمبیا به ۲۲۴ نفر رسید
🔹
تعداد کشته‌شدگان زلزلهٔ ۷.۴ ریشتری دیروز در کلمبیا به ۲۲۴ نفر رسیده است. کلمبیا این زمین‌لرزه را «فاجعهٔ ملی» اعلام کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/680483" target="_blank">📅 09:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade0fc751a.mp4?token=sJyfWrWG7n6jXADmwSidMJgNFMpOPPTi4Ogl8ob52T87N9hatRlaiYxGh9oWk1rfI9WKjmiOrUgN_hbkELpRs3eWYJRmC0vJpxuOtvD8fT1l4LwwceKnmRxSsbPBV3_remYLv-cNjBYNZ42uwq4_eQq_XhVzMEBIIeZIzprOIPgctfctjUnQkn1A59KULT3N8oxslwcD2DWdr0PcNK-V-8fWA8i4qC6dxinhODeHZIV1ehZxzedIv9l2ZrePjNaagM3tpBPKwWVES4DhFscBWgXKdHBq8VtUx39thqekjdvEHzEM31k8R3-hxAwIqwfepqrwwVFWaYC5BQv39Wb5NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade0fc751a.mp4?token=sJyfWrWG7n6jXADmwSidMJgNFMpOPPTi4Ogl8ob52T87N9hatRlaiYxGh9oWk1rfI9WKjmiOrUgN_hbkELpRs3eWYJRmC0vJpxuOtvD8fT1l4LwwceKnmRxSsbPBV3_remYLv-cNjBYNZ42uwq4_eQq_XhVzMEBIIeZIzprOIPgctfctjUnQkn1A59KULT3N8oxslwcD2DWdr0PcNK-V-8fWA8i4qC6dxinhODeHZIV1ehZxzedIv9l2ZrePjNaagM3tpBPKwWVES4DhFscBWgXKdHBq8VtUx39thqekjdvEHzEM31k8R3-hxAwIqwfepqrwwVFWaYC5BQv39Wb5NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم مراقب خرید طلای آبشده باشند
رئیس اتحادیه تولیدکنندگان و صادرکنندگان طلاوجواهر:
🔹
برخی به دلیل کارمزد کمتر اقدام به خرید طلای آبشده می کنند که به دلیل نامشخص بودن عیار آن، خطراتی به همراه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/680479" target="_blank">📅 08:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680476">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: من به ایران اعتماد ندارم، من آخرین کسی هستم که به ایران اعتماد می‌کند، آنها دائما به من دروغ گفته‌اند
رئیس‌جمهور آمریکا مدعی شد:
🔹
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آنها کنترل آن را ندارند؛ ما کنترل کامل را داریم. تنگه هرمز مال ماست.
🔹
شاید در مقطعی آنها دست به کاری بزنند و آن وقت نابودشان می‌کنیم. اما در حال حاضر، ما در موقعیت بسیار خوبی قرار داریم.
🔹
ما با کشوری روبه‌رو هستیم که ۵۰ سال قلدر خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال است، درست است؟ ما چهار سال است که می‌گفتیم ۴۷ سال. اما آنها دیگر قلدر خاورمیانه نیستند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/680476" target="_blank">📅 08:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680470">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e163d5cec.mp4?token=eJ9fMa2anCaTa7c-7gC8BlLXgO-h5j_JzwveON-NPnApRrsdVOY7gjau9gsjOZ4v2B34uzlWbMncZJzRlooIeUwznJ2YX3hM1Qar459LI85NYu3it3Ss6e222qIykkW6H8OEOA6VP1KtN6rRm8R1PTIdr64sCTKM6MMVWL585bBtVlujroRBcZp1KNv36vWWeQhCEY7AoI7S1jV-cbCDIDABM3GhkNXUWSLG_jsMFcc1zOYxe2GLwzZ85XBhBN3lEmQdvpxGC6xLArb_6qaCugLfBCaKmAOdBNVm8D45Ut8sqL1oysdvDb02Hp23GjBWAYWE9vBHC15e9NtkGT--Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e163d5cec.mp4?token=eJ9fMa2anCaTa7c-7gC8BlLXgO-h5j_JzwveON-NPnApRrsdVOY7gjau9gsjOZ4v2B34uzlWbMncZJzRlooIeUwznJ2YX3hM1Qar459LI85NYu3it3Ss6e222qIykkW6H8OEOA6VP1KtN6rRm8R1PTIdr64sCTKM6MMVWL585bBtVlujroRBcZp1KNv36vWWeQhCEY7AoI7S1jV-cbCDIDABM3GhkNXUWSLG_jsMFcc1zOYxe2GLwzZ85XBhBN3lEmQdvpxGC6xLArb_6qaCugLfBCaKmAOdBNVm8D45Ut8sqL1oysdvDb02Hp23GjBWAYWE9vBHC15e9NtkGT--Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار و مفسر سیاسی آمریکایی: مردی که خودش را در کنار جورج واشنگتن و قهرمانان جنگ آمریکا می‌دید در یک خودروی آشغال پنهان شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/680470" target="_blank">📅 07:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680469">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e17cd8159.mp4?token=PkNkjExrRoS3USkb_7mO4n0jEm33ZF2gHsOn7H0DtDzd6sTeoaYXopWtexeWnJT5whuBaGJAXh_m8rVbkNSfSTE_p2SFs7eQ5-mb_ITnfH1ynKD3jEilVkSr0-2aaMNGlazG1hnfNxygxDA9biFFXnKK0TtKodYzhW7PrCVgX_K8Pqwtz-uJrm7ENaC6nBxk505R_hxxdsrIFGKOTQjxSQqj5mMq8D_FT4g8ePlRrXCBnNyNpKcoeZnMAlewSA6YazH3a2gOXQZVmUuvr3EMMSK_vaCFxA2VEkmRgHiaN_sHy4BDCYQ2tzEVm1KSjMbAmvcWB4Oefw1P_8r_AIrOLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e17cd8159.mp4?token=PkNkjExrRoS3USkb_7mO4n0jEm33ZF2gHsOn7H0DtDzd6sTeoaYXopWtexeWnJT5whuBaGJAXh_m8rVbkNSfSTE_p2SFs7eQ5-mb_ITnfH1ynKD3jEilVkSr0-2aaMNGlazG1hnfNxygxDA9biFFXnKK0TtKodYzhW7PrCVgX_K8Pqwtz-uJrm7ENaC6nBxk505R_hxxdsrIFGKOTQjxSQqj5mMq8D_FT4g8ePlRrXCBnNyNpKcoeZnMAlewSA6YazH3a2gOXQZVmUuvr3EMMSK_vaCFxA2VEkmRgHiaN_sHy4BDCYQ2tzEVm1KSjMbAmvcWB4Oefw1P_8r_AIrOLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش کاربران خارجی به مخفی شدن ترامپ در کامیون آشغال
📲
🇮🇷
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/680469" target="_blank">📅 07:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680464">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
واکنش کاربران خارجی به مخفی شدن ترامپ در کامیون آشغال
📲
🇮🇷
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/680464" target="_blank">📅 07:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680463">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAtlFrZK6ER2_WB8_sfDxgBd4XlvAId--W6hwV4E81dtjRTnxPCtAkPmX0QCfDedS45kSsv65FcXYUSvifTi5tiOMCtijJbNfkRncyX8ce99LHWcI1qcbdv7-BSNeK7Kke3SDq09CCoU52GMK_ZPetoo8xN18Zm6Rgsco7uUIG5OCV-d0XGvTs0yIFgKm3ydnJu5zLFlrXeF_1ohbNbdrhXt9WJgsIYFZR5gnymiCUjjgfHMQNjJ85wfc4jdOpQiMqM0VDmGVnfG1gFV_RJFip9Lyy3482hfc7LIPvJ6mGbwkga4Zxnhj5MKUgndSEXt-2XXcZcrDoshmutXHvujXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۱ مرداد ماه
۲۸ صفر ۱۴۴۸
۱۲ آگوست ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/680463" target="_blank">📅 07:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680456">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5171ee4322.mp4?token=PNP5eQpDWG5ZJaC2aCLMtnsx3CAAKfYd3uHOUFUHRrP7hBP24Frp1fIaMdHyUPNGkWNRKRV2cBKCQkj6eUWTzNzHau5OOsorDCECf46qbpamzT3iq99ZIOI_VFYMgBe7TWjmH903JeYi6b5EGjfWq6MJbT-Pq72zCOhd7uD6Murm8KwcMROxL-gan7nIV5XnG4dNVK7v5ts6sFZp5IgyrbH3TRuASzXVj93ZGeN5-EwJ77yAviAUHMpH2TPT6QNVAaeG6SwYlK6OyU_ys-fNs6mSbUyyja8ii5X2lg9dNMfKM927lqNeqHspX6IyuWUoKsU0QVppss_E3jJyrwpU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5171ee4322.mp4?token=PNP5eQpDWG5ZJaC2aCLMtnsx3CAAKfYd3uHOUFUHRrP7hBP24Frp1fIaMdHyUPNGkWNRKRV2cBKCQkj6eUWTzNzHau5OOsorDCECf46qbpamzT3iq99ZIOI_VFYMgBe7TWjmH903JeYi6b5EGjfWq6MJbT-Pq72zCOhd7uD6Murm8KwcMROxL-gan7nIV5XnG4dNVK7v5ts6sFZp5IgyrbH3TRuASzXVj93ZGeN5-EwJ77yAviAUHMpH2TPT6QNVAaeG6SwYlK6OyU_ys-fNs6mSbUyyja8ii5X2lg9dNMfKM927lqNeqHspX6IyuWUoKsU0QVppss_E3jJyrwpU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش سوزی بزرگ در اربیل عراق
🔹
علت حادثه مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/680456" target="_blank">📅 01:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680455">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-q5aft8N8AggG0ih-WwRg05oUuvuQK2pNX8cmTebvQXsB3QoflhIQAsV93-cwYwe2_M1wAb0LWwXzsyQGDaVg6QZqRE0RbBp3JTpNl2RyOohAOo7pj7P0IWcfBUGVRJfU5gl2HBSj6mCOowstJF0t-hbKD5Yh0pykI9DuhrZ_Gd_F0QtKMECeijtaoRHVvXth_H6tM4joOWeWSZ0MKrfrm-R1TgAU7Ix5ulI5vQNcpf53WX5pchr80nIAWrLoMrFOrAoc8MqaqveMfViE-8--MUJYzLMNJxw3chw-rlE_Dti6ncZQE_r_h9MffQ_3EPW6OG2Vi_pZh9MCiZmw6sEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: کاش رئیس‌ جمهوری داشتیم که بزرگترین جوک و مایه تمسخر تمام جهان نباشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/680455" target="_blank">📅 01:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680452">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPzaGxNajwcm_Y0JhuKcHKBzBrhxWES2iDxN2RFC89Oq_L4tpB818Vk7qpx_KzwFCpu7K_p-33hb0qzq5PZ7dYBMlJMD1xyZTK3f3_nkksLeS8eMYfRSE2xj40nuCDBMrP53lA4BwFXyAZTgtWehMUgZXwettixfX5DviDPGmX0FCxntDcqCk4emK9BIsoU--y-qThGjOxreTZYuc8O8xRFyUzMEBugeEEtTrHYAh0x1fX11T8dBKa7Ge9sHZdRmIDkI_4SmEgnqGVKjQXwZRHZZkYCl6cmbrFf4py8qrI3_FU6m0182WVuaYQ0GdQk_xb-lgAcekJKRG5ogzpCOtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر ژئوپلتیک آمریکایی: توازن قدرت در خاورمیانه به‌طور دائمی علیه آمریکا تغییر کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/680452" target="_blank">📅 01:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680449">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3b82593b.mp4?token=iRyBsajB1p7PNKUI6AeLCeYyeUOBMz54DAG6JQ8untjNQjcHUjG2LDu4911qaH2oRgKtiIR2DdTflAkSc_AU1ToFsYOj-m0EbfIY_OR1iUtvNitoaUxnV8xXoa_cBeI6uNy6Dr4XeI3OatjHpA7KKmI7b5ReZw5yNxFjs5X5WxGpO8oOnqpxjB4ae_ftYaADYmBpESrlWU3u2blgFK6shaB0mXQJzeViXqkS2ATgNeV_RPEBoPnah-R73_VMOEYFockylAhaQK3TsAsrRCq9gVk3uw7aUaevGqlyPPCoyJEXk-mjUu364_Blwb1AdXyWt40Dcx_dB7MtK4fuBsD9qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3b82593b.mp4?token=iRyBsajB1p7PNKUI6AeLCeYyeUOBMz54DAG6JQ8untjNQjcHUjG2LDu4911qaH2oRgKtiIR2DdTflAkSc_AU1ToFsYOj-m0EbfIY_OR1iUtvNitoaUxnV8xXoa_cBeI6uNy6Dr4XeI3OatjHpA7KKmI7b5ReZw5yNxFjs5X5WxGpO8oOnqpxjB4ae_ftYaADYmBpESrlWU3u2blgFK6shaB0mXQJzeViXqkS2ATgNeV_RPEBoPnah-R73_VMOEYFockylAhaQK3TsAsrRCq9gVk3uw7aUaevGqlyPPCoyJEXk-mjUu364_Blwb1AdXyWt40Dcx_dB7MtK4fuBsD9qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک یک سرباز روسی که با استفاده از یک سیستم شلیک همزمان، به یک پهپاد اوکراینی که در ارتفاع پایین پرواز می‌کند
🔹
این سیستم مستقیماً بالای کامیون‌ها نصب شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/680449" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f933dd533.mp4?token=p4oBf9Ba0XFNhVOhpvZUJOnCVL34PIbOVVvhO1iQFfNTucUf4BHzOI6lgIhj955Xah0RaViWW6R174glOZxLXEuAKfrikk23NGnEE5ErBJmfFLpYrn5DhZTYDf_BfCEYrn9FtYT7HI34VvzTnx_7nhf-GyZY9sB2wdJ_Ec6161_LGdh3O91eWxMG1Yc8hptSxNfZ3EY_zmal6vY3CSVrpZF44mJm8PJ39hLKfTQyiCUR-ai6_pXDrmoDtvmrNkJmtRoyDq4AwudyGxlByxWidXdydh-lGW5T7fAoPa86EdHj1DNQn7IKdPdNhr1ummphTXSKSN4TAyxmy2IkjSVYvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f933dd533.mp4?token=p4oBf9Ba0XFNhVOhpvZUJOnCVL34PIbOVVvhO1iQFfNTucUf4BHzOI6lgIhj955Xah0RaViWW6R174glOZxLXEuAKfrikk23NGnEE5ErBJmfFLpYrn5DhZTYDf_BfCEYrn9FtYT7HI34VvzTnx_7nhf-GyZY9sB2wdJ_Ec6161_LGdh3O91eWxMG1Yc8hptSxNfZ3EY_zmal6vY3CSVrpZF44mJm8PJ39hLKfTQyiCUR-ai6_pXDrmoDtvmrNkJmtRoyDq4AwudyGxlByxWidXdydh-lGW5T7fAoPa86EdHj1DNQn7IKdPdNhr1ummphTXSKSN4TAyxmy2IkjSVYvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پارسال همین شب‌ها؛ خادمی سردار شهید تنگسیری در حرم رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/680448" target="_blank">📅 00:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680447">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27b1027df.mp4?token=P-cVOjHBWyYs3UQ-d3wqAUmMBaJXs_IfnGeWMnygTEv1HENUshZt7i_KJ13gQpZxkMjARDYNFiYOiKXE87L08FBNcKLfO2u2IUZh4zVAL6UIl3AGlqNW4OuDpXQ14-S1QlJHTtX4NwNrhq8QhqQePzs3TxgeDN4PoJJjvZNAWIP5RFg-zztaA0W7kdiDTIraqqlO8SYi_63zFpUtyemfufSU4AK53Wugs_uZS9rOOWOOcwW0eyPbKZr_C6xigHVOolOhvXfpR01CPM3O7-MDAABTBf-7vM0HM9I9A8jdb-OBe-HwwHL2cvJHmM3lhKOc832StTU7inal4hs4faSo9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27b1027df.mp4?token=P-cVOjHBWyYs3UQ-d3wqAUmMBaJXs_IfnGeWMnygTEv1HENUshZt7i_KJ13gQpZxkMjARDYNFiYOiKXE87L08FBNcKLfO2u2IUZh4zVAL6UIl3AGlqNW4OuDpXQ14-S1QlJHTtX4NwNrhq8QhqQePzs3TxgeDN4PoJJjvZNAWIP5RFg-zztaA0W7kdiDTIraqqlO8SYi_63zFpUtyemfufSU4AK53Wugs_uZS9rOOWOOcwW0eyPbKZr_C6xigHVOolOhvXfpR01CPM3O7-MDAABTBf-7vM0HM9I9A8jdb-OBe-HwwHL2cvJHmM3lhKOc832StTU7inal4hs4faSo9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند گاز خونت را مثل روز اولش کن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/680447" target="_blank">📅 00:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680446">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
درخواست محرمانه عربستان از یمن برای پایان درگیری
🔹
در پی ضربات موثر انصارالله به مواضع ارتش و مزدوران سعودی در یمن، ریاض در پیامی محرمانه به هیئت مذاکره کننده یمنی ابراز داشته که خواستار پایان درگیری و بازگشت به توافق سال ۲۰۲۲ ریاض-صنعا بوده و این درخواست را به هیئت یمنی منتقل کرده است.
🔹
این درخواست با مخالفت مقامات انصار الله روبرو شده است. صنعا پس از دریافت پیام عقب نشینی ریاض از مواضع خصمانه اخیر تاکید کرده است که به دنبال دریافت تضمین‌های جدی و واقعی برای تامین منافع ملت یمن به ویژه در مورد پایان محاصره، دریافت غرامت و پایان دادن به مداخلات عربستان در امور داخلی یمن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/680446" target="_blank">📅 00:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amq3TYxnD71vXd83DZc5UHPvDoLVwccrf8MHOP7an1qHYGtu6N59Ea9o5RovnU_STOBkNUJ27hN8CrJF9ub_qBLO_LBRYuLCcWMxibNSKENY71OSk6lOvJmm1M8SylZZKqsmfDV5SYomN4BrDore_7GoSQbmgPLKfXo8cO8xXAY4COCtu0qyg_JOSwRgiBJZWOJe4NCwoj72utGuaXpsnH7K4kYaqNKaH2yugC2jI-ReWT84bOpP0_ttGl2mKtl6gxZXAMJE4tDFpuG9K73PpOEQ2PHm8pTsZAzKIIrumBZv1Ojqzvi6lGffXB225zm01fiDIZudfjcCan4LYsT1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/680442" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680434">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سردارنقدی: تولیدات موشکی و پهپادی ما تمامی ندارد
🔹
ما بیش از نواخت شلیک موشک‌های بالستیک تولید می‌کنیم و به دست رزمندگان اسلام می‌رسانیم. در حوزهٔ پهپادی نیز قابلیت تولید ما بسیار بیشتر از نواخت شلیک است.
🔹
اگر جنگ چند سال هم طول بکشد، باز هم موشک‌های بالستیک…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/680434" target="_blank">📅 23:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680432">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5981ac86.mp4?token=kc51Et97SxnEeoz0DsEINHVmEByflJbVMJkQH1s1Q32e3tX5wj1OhDUffdCY0iOKydK6LLO4Gd_Q-32kZ9UyCDKNfVgZ-K5piMON2uGt9p9KulXl_EPl3BO81uYWmTr4BuNpagWfrrpCM6NsNwi_h20WUWoe-VxvJgUmq1zdXgwcyKozLRfxG4UIfU3rr1W-lvIz2ReDGeT0kdXhLGATtyNkYIHX5dO7r8BGk9WQPVFgigMYVgsNLr_3puAZEBqRE9xLw2T8hEsKq1IPDC5rAA-Rgik7MODrLgmknZC2JqmssMyKODi23jQr8ccKYXIg5uNciGhzuVSg1hSj7uKqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5981ac86.mp4?token=kc51Et97SxnEeoz0DsEINHVmEByflJbVMJkQH1s1Q32e3tX5wj1OhDUffdCY0iOKydK6LLO4Gd_Q-32kZ9UyCDKNfVgZ-K5piMON2uGt9p9KulXl_EPl3BO81uYWmTr4BuNpagWfrrpCM6NsNwi_h20WUWoe-VxvJgUmq1zdXgwcyKozLRfxG4UIfU3rr1W-lvIz2ReDGeT0kdXhLGATtyNkYIHX5dO7r8BGk9WQPVFgigMYVgsNLr_3puAZEBqRE9xLw2T8hEsKq1IPDC5rAA-Rgik7MODrLgmknZC2JqmssMyKODi23jQr8ccKYXIg5uNciGhzuVSg1hSj7uKqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت سالروز شهادت امام رضا (ع)| حاجت‌روا
🔹
صداهایی از جنس امید؛ روایت شما از کرامت و نگاه ویژه امام رضا (ع) در زندگی.
🔸
الوفوری را دنبال کنید
👇
#حاجت_روا
@Alo_fori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/680432" target="_blank">📅 23:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680431">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSJ6VPfK7UN7zgJuArVzchuabRlG9W-m2dIRyluHQR1iZ6n9MVE9btCwGDKz9hHJsVZvcZbMtloYHDEFHQ4iXZVa6_XGbWejXbQeWOkXfghZ6Nm4G2nbEy30TDqYbFCgZgYXoYeXgO-Tili5_sgaEht_BlL2-0snI-SwQ44INTUT4OUyeQBQt_3y_WENNvtm-dYwFU7xPmWdeqmPkqpYdlUppbY_u5cYweNb2sV4i3IgaqPrtyoOd_6m0b2sMxDSbKdQHzN-tw9mLy5ULJAX-7QZGBabhyBK3q8IOW0AjisG94VjXXmGONCXkUWJ2GzJ9McYpwfbkydabIiT10dAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ری اکشن جالب یک مخاطب به رفتار دیوانه وار ترامپ
🔹
بزار ببینم‌ درست متوجه شدم ؟
🔹
ترامپ صدها دختر دانش‌آموز را کشت، سربازان آمریکایی را کشت، صدها نیروی نظامی زخمی کرد، قیمت بنزین را سر به فلک کشید، ذخایر موشکی ما را مصرف کرد.
🔹
همه این کارها برای این بود که در نهایت به ایران اجازه دهد کنترل تنگه هرمز را به دست بگیرد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/680431" target="_blank">📅 23:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680430">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823f7565ed.mp4?token=qBrBToiMtckkbJTe1WucKYwWb-c6_a0m8S14fibkedCBJVPVhTE17pczTVJAcRtcdJ5DFoOXShOgqDLH7shmPV1bRbPoEZfbTXqrk5M119xEJ41I1EPw1D4Ty9OrFAuJSZeWfpFHWKgOqBWaIpWJUkZavtRn00c3AlUFjoECyZzdDj8jX9vzvDoAeeXP390kxxQUYruxsGVS3f-BvyEv3tOaZ4JTb52IKiC8vlO7XWsuRF8tcjntumq2Hm_7yLviwuvz-lATMZxwAqmwId2EZvAUfuS9rEccJFT1LvEh_8EMzEsbEJQBODRP4llCjWo7m66r-keoK03zSirONqTSQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823f7565ed.mp4?token=qBrBToiMtckkbJTe1WucKYwWb-c6_a0m8S14fibkedCBJVPVhTE17pczTVJAcRtcdJ5DFoOXShOgqDLH7shmPV1bRbPoEZfbTXqrk5M119xEJ41I1EPw1D4Ty9OrFAuJSZeWfpFHWKgOqBWaIpWJUkZavtRn00c3AlUFjoECyZzdDj8jX9vzvDoAeeXP390kxxQUYruxsGVS3f-BvyEv3tOaZ4JTb52IKiC8vlO7XWsuRF8tcjntumq2Hm_7yLviwuvz-lATMZxwAqmwId2EZvAUfuS9rEccJFT1LvEh_8EMzEsbEJQBODRP4llCjWo7m66r-keoK03zSirONqTSQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: پیروزی ما حاصل حضور مردم در میدان و نفوذ در جهان بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/680430" target="_blank">📅 23:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680429">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5tYcpeTkLQKidzLjfUnfKiTMiCpL14x2rYKjM7qgU3MX1xnO5S-OKnfSjB0bMEfEGIdF1M2PgKhaFlxWQRyC8N60ocCqqdeTYqPCauTEMtJSX5r31qhKR783xYEYtFnuwHs-FvNem7w4lDEi4ptEppwuKKVIaD3oLmMzKJaQ-0Hf5UD5C_gta4ITGDrLINT2fHXzu2aXLJcVqRyKqofcGVm9g9Kk_LxSKa-A76_8GGhWOBkmu8bP3ISeBlxmF00Et3snZWMlGSzCcLkZscQKsLZs81bUhfJuTZbuZfGIUYdIQnKttjAcbm4LAD2-Y4aTAdHirMqk19zt-3sLhTYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی رونالدو برای ازدواجش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/680429" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680428">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
محسن رضایی شروط بازگشایی تنگه هرمز را اعلام کرد
👇
khabarfoori.com/fa/tiny/news-3237163
🔹
ترامپ چگونه در یک عملیات مخفی از ترکیه خارج شد؟ | فرار با کامیون غذا
👇
khabarfoori.com/fa/tiny/news-3237044
🔹
عکس های خانوادگی حمیدرضا رجب زاده مداحی که به قتل رسید
👇
khabarfoori.com/fa/tiny/news-3236968
🔹
محاصره دریایی از جنگ هم بدتر است و باید بشکند
👇
khabarfoori.com/fa/tiny/news-3237132
🔹
بشار اسد به اعدام محکوم شد
👇
khabarfoori.com/fa/tiny/news-3237066
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/680428" target="_blank">📅 23:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680427">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200c140ffa.mp4?token=N6q7YURVHJiRh1spcRxhVzS13_chJRXwT2VSXfst-LjYwy2JoUptc4dtPaCrc2kCreQV_CaROk0zH6sbb4wfNW9sUuPPpsLDBAFNAR9_zjmE_ITSzuWSwQ997i3OQBzlv2-HsZt2602yx_VuT_ax-jFWBdD-FNYKIbCfPWBu3GVb50krVk857jRKhDtcsD19VMK0o8AnCrT0FKKb66ynDJNKVlcAzv3LITUPjpsnzImxy7GxQ_XADsw7i7JjelzEoPWEqPnKFLVkB2VXXIOQIcr_BljDZo42q2kFESVgJ_fXAbXcF5HI87jFVyuxpW44C4TAPZNIf3um6rlZIcV8TDXPcHuzE17VKtg01Yh7yJqNesX-RgdsL6J-8odzE79UtQVg2d9tMn5JTqla-MHuGq1sOqfZYQ693ds_NncFQTSy3tTliGBbwrggmEfwCyK4p7CUfERyCaC6C2gUo9mpN6AXYhaOR7ORR0oRuuGEeUqCjdw2ze199vZqhAJRB-XgHYckwUjvm1ssRB_daAlFfTfTSOn96h76vmtn8tF48Gq0ZOlj9C9pJF7jIvLN5Sg5HzJFeyr6itJzJhgAtbhxsRLFXqJmMeUVl1pUWRwC08CF2eYZaASjTiXFyTq7g-RINKp3UpWPbZbAKx41rzY9egO-BjCZ1Py9NRze7-YGUcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200c140ffa.mp4?token=N6q7YURVHJiRh1spcRxhVzS13_chJRXwT2VSXfst-LjYwy2JoUptc4dtPaCrc2kCreQV_CaROk0zH6sbb4wfNW9sUuPPpsLDBAFNAR9_zjmE_ITSzuWSwQ997i3OQBzlv2-HsZt2602yx_VuT_ax-jFWBdD-FNYKIbCfPWBu3GVb50krVk857jRKhDtcsD19VMK0o8AnCrT0FKKb66ynDJNKVlcAzv3LITUPjpsnzImxy7GxQ_XADsw7i7JjelzEoPWEqPnKFLVkB2VXXIOQIcr_BljDZo42q2kFESVgJ_fXAbXcF5HI87jFVyuxpW44C4TAPZNIf3um6rlZIcV8TDXPcHuzE17VKtg01Yh7yJqNesX-RgdsL6J-8odzE79UtQVg2d9tMn5JTqla-MHuGq1sOqfZYQ693ds_NncFQTSy3tTliGBbwrggmEfwCyK4p7CUfERyCaC6C2gUo9mpN6AXYhaOR7ORR0oRuuGEeUqCjdw2ze199vZqhAJRB-XgHYckwUjvm1ssRB_daAlFfTfTSOn96h76vmtn8tF48Gq0ZOlj9C9pJF7jIvLN5Sg5HzJFeyr6itJzJhgAtbhxsRLFXqJmMeUVl1pUWRwC08CF2eYZaASjTiXFyTq7g-RINKp3UpWPbZbAKx41rzY9egO-BjCZ1Py9NRze7-YGUcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر مقاومت کردید، آن وقت قلّه را فتح خواهید کرد؛ کاری که از بعد از زمان رسول خدا تا امروز انجام نگرفته، این کار، کار شما است.</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/680427" target="_blank">📅 23:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680426">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6cb1de1d.mp4?token=M7ev7awuO_1RUqYl2jRFUcjJGqXe5AxUrljIYevPSGuHwSFClujLipd9ZSl2M01OwC53POuWFnvu_4KhuAz6bGo8GTnDIfWolB-anVtlaiJd1fpaqiauNxZUwK4goAswdv9KKRrh1xjE3aC_7jIZ1U0KDW8oJL4G4DzQ75EX7hZP3VXCjHE_8wWZ4Ps_BxxXnicqeSK9PA8hhbH295Ka2BD4Hn2rFUvzf7y7hBlTR7eXzQP28cOsg9VkZuWnH7NAfoTZlPjzv4ZDhjAXgpR80WlThlhCqIxIXl8kXISl34rXPcGhpfU4jS8rvRRmjOLflI5QhCEO2Ce8gMo5uYrP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6cb1de1d.mp4?token=M7ev7awuO_1RUqYl2jRFUcjJGqXe5AxUrljIYevPSGuHwSFClujLipd9ZSl2M01OwC53POuWFnvu_4KhuAz6bGo8GTnDIfWolB-anVtlaiJd1fpaqiauNxZUwK4goAswdv9KKRrh1xjE3aC_7jIZ1U0KDW8oJL4G4DzQ75EX7hZP3VXCjHE_8wWZ4Ps_BxxXnicqeSK9PA8hhbH295Ka2BD4Hn2rFUvzf7y7hBlTR7eXzQP28cOsg9VkZuWnH7NAfoTZlPjzv4ZDhjAXgpR80WlThlhCqIxIXl8kXISl34rXPcGhpfU4jS8rvRRmjOLflI5QhCEO2Ce8gMo5uYrP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه پاسداران: سپاه باید آماده عملیات هوشمندانه در خاک دشمن باشد
🔹
هر موقع اقتضا کند و فرمان صادر شود، باید بتوانیم عملیات را به خاک دشمن، به سرزمین‌های دشمن بکشیم و دور از سرزمین خودمان بتوانیم عملیات انجام دهیم.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/680426" target="_blank">📅 23:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680425">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac585917.mp4?token=DIBfvQpPoylk2etr_Avck46CH3SQ_jq7qwuZXjBxB4jLwgkuN-oCLog4bK30SIWvHt2Qx4Z-rxNzRf7aZJWWT6COzFI4T6b_y5A0ChXOlkV3oUSced20IIjUBScUrztlhpoRlbOW3BCKKhmnEF3XSK7gVerAMFopBuXrAaiNeBhRE86tm2-kxGSiepPEyigunUSS5gCtA-ZC9WlTFKuyg7D5HtaE7FWrpY5RYctYuD-2nOmH22LrYZoEcTJylsuTAM-paJYuvbv0bqTTHBPbouxGO0zJkDorsAdUasP53QcFI_BYC21DJTvhoeV1fBITeKHudIlaG4QIwmWswSQpzLhHWmbPTMpjxILQ_T2Xo8queSIgRnehO5AKuONyumQVCskxChiZqBprVg3EHen4O5QN2sWnjUqikufetCWehVYW_rtqM0lsn6KM0Hm3-Zm5B5ZPDMOeXbmK7nBPTBbVMmoDlx5UZzyFe-0TKAKcbjwwvBwzezojQsKGhljkLEHv_gOAKBEayR-CHQJQFtCoJXLbFgthDts1TrWeBHfYSXRxFVG4RVjTLN2VE1UTPIEU-SKdwNJs0ENsFbVfcYJzt9_XRni3pgwbGeYeT1Z-1wu9GxsoRxxhUjPzsEKFZpgEo78I2m1BPJ3R-l0SQeqdilMrpDMiEuk8_fRzugAr-Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac585917.mp4?token=DIBfvQpPoylk2etr_Avck46CH3SQ_jq7qwuZXjBxB4jLwgkuN-oCLog4bK30SIWvHt2Qx4Z-rxNzRf7aZJWWT6COzFI4T6b_y5A0ChXOlkV3oUSced20IIjUBScUrztlhpoRlbOW3BCKKhmnEF3XSK7gVerAMFopBuXrAaiNeBhRE86tm2-kxGSiepPEyigunUSS5gCtA-ZC9WlTFKuyg7D5HtaE7FWrpY5RYctYuD-2nOmH22LrYZoEcTJylsuTAM-paJYuvbv0bqTTHBPbouxGO0zJkDorsAdUasP53QcFI_BYC21DJTvhoeV1fBITeKHudIlaG4QIwmWswSQpzLhHWmbPTMpjxILQ_T2Xo8queSIgRnehO5AKuONyumQVCskxChiZqBprVg3EHen4O5QN2sWnjUqikufetCWehVYW_rtqM0lsn6KM0Hm3-Zm5B5ZPDMOeXbmK7nBPTBbVMmoDlx5UZzyFe-0TKAKcbjwwvBwzezojQsKGhljkLEHv_gOAKBEayR-CHQJQFtCoJXLbFgthDts1TrWeBHfYSXRxFVG4RVjTLN2VE1UTPIEU-SKdwNJs0ENsFbVfcYJzt9_XRni3pgwbGeYeT1Z-1wu9GxsoRxxhUjPzsEKFZpgEo78I2m1BPJ3R-l0SQeqdilMrpDMiEuk8_fRzugAr-Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان فرار مخوف شرور مسلح در عملیات مشترک پلیس
🔹
معاون مبارزه با شرارت پلیس امنیت عمومی فراجا از دستگیری شرور مسلحی خبر داد که پس از شلیک به یک شهروند، با تهیه گواهی فوت جعلی تا مدتی با هویت جعلی در ایران زندگی می‌کرد اما سرانجام در عملیات مشترک پلیس امنیت عمومی و پلیس فتا دستگیر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/680425" target="_blank">📅 23:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680424">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/894ec0af40.mp4?token=m4nHRzyYAYpmhOQ9fuUb36lJ5pCMmeTCIyM5wrIw2YMCmvqk6FP5uNIODWJOFrmOUF8gfHxh3PPOB7sKYnA5cnxf6wWUtGn5RVYgmaEwZOpK7m8JU1UGHvHwO85MZb4qsRrI7iULHX47ny7R0gcs0R7fXwCIIozbqVZg5fgf8hvI010mvbaSV8PYIG2AJKQguNathZP2CF4IGCyCBVCaBIbBu7-K_c1I9AnbY1nPZa3-t3_bIN7_x4uHLPojxRQaP1NPdu6ZxVL7cx8ahpzohwlGEcWbjrFfy6HXHFPE542MOKdsVRaNng3fYL3Ax4DLP3XE_Z46GrT0GgibrfYUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/894ec0af40.mp4?token=m4nHRzyYAYpmhOQ9fuUb36lJ5pCMmeTCIyM5wrIw2YMCmvqk6FP5uNIODWJOFrmOUF8gfHxh3PPOB7sKYnA5cnxf6wWUtGn5RVYgmaEwZOpK7m8JU1UGHvHwO85MZb4qsRrI7iULHX47ny7R0gcs0R7fXwCIIozbqVZg5fgf8hvI010mvbaSV8PYIG2AJKQguNathZP2CF4IGCyCBVCaBIbBu7-K_c1I9AnbY1nPZa3-t3_bIN7_x4uHLPojxRQaP1NPdu6ZxVL7cx8ahpzohwlGEcWbjrFfy6HXHFPE542MOKdsVRaNng3fYL3Ax4DLP3XE_Z46GrT0GgibrfYUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه پاسداران: سپاه باید آماده عملیات هوشمندانه در خاک دشمن باشد
🔹
هر موقع اقتضا کند و فرمان صادر شود، باید بتوانیم عملیات را به خاک دشمن، به سرزمین‌های دشمن بکشیم و دور از سرزمین خودمان بتوانیم عملیات انجام دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/680424" target="_blank">📅 23:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680422">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7f7e509f.mp4?token=PU3gkR1_J2KP3zRMXWZvj424Vh89jACp0qCaSwOHRAghWEikf5XW-vSi-x0Md4ppNVW6ayCs79eTvdtjJCtHhKJu7uxyKEUzXGRMTsu1FZ9B6E33-wh9ZyE-ENCZi8I4f53KRIb7DjSCujU70xBumAeRgPAMlxdddXVEWFIy8ePSgtXha2UEhQCzUxJ44N_DjYf92GXMAfJUfPpy5PyGpe2Emp1VzTOk4eCM4BMT1GmimYTZFKpHAT16-lHRUAFihasTPHsKZsvJDaE6veuRU5jgDK_3p7hNS8rBpOQxcfynk3991irjMy2AMZSj0y4DcrbcbGT0IqZceeL2qXH-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7f7e509f.mp4?token=PU3gkR1_J2KP3zRMXWZvj424Vh89jACp0qCaSwOHRAghWEikf5XW-vSi-x0Md4ppNVW6ayCs79eTvdtjJCtHhKJu7uxyKEUzXGRMTsu1FZ9B6E33-wh9ZyE-ENCZi8I4f53KRIb7DjSCujU70xBumAeRgPAMlxdddXVEWFIy8ePSgtXha2UEhQCzUxJ44N_DjYf92GXMAfJUfPpy5PyGpe2Emp1VzTOk4eCM4BMT1GmimYTZFKpHAT16-lHRUAFihasTPHsKZsvJDaE6veuRU5jgDK_3p7hNS8rBpOQxcfynk3991irjMy2AMZSj0y4DcrbcbGT0IqZceeL2qXH-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: تشییع رهبری اگر در نیویورک و لندن هم انجام می‌شد، میلیون ها نفر شرکت می‌کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/680422" target="_blank">📅 23:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680418">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/839e31ae75.mp4?token=NOWhgm0Z_wL7N2WiajSzZKamRMcOZILFyrUe3Vs3Gz7xbuksY_Ukh9hyedqQJFEyU-ctRIy6Xa_CHUZOoFqQk7WoJI4yQkEdltr0OZp_vegdZUx1PaRpP8sfZRCCUH9zP55u4vP5nqYqw2qZQSIwxhvfFxBnaTyhG1OGA8O0oShj9efcXVzHGCjAN9iHedu3mdbvL0IEvx_JT7KriDiS4b8O10dKlMvcKtQjOx_0cm7J5jv_ZCb-ZudSupLtOpuoq-rP9Y2m7y-HAfEocL5QAi_qxVINOHZ7DETo3H8oVzBOuZM8eJzSX5EnO_QPKtv3IkImhO8dVQotLuUGrvIK6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/839e31ae75.mp4?token=NOWhgm0Z_wL7N2WiajSzZKamRMcOZILFyrUe3Vs3Gz7xbuksY_Ukh9hyedqQJFEyU-ctRIy6Xa_CHUZOoFqQk7WoJI4yQkEdltr0OZp_vegdZUx1PaRpP8sfZRCCUH9zP55u4vP5nqYqw2qZQSIwxhvfFxBnaTyhG1OGA8O0oShj9efcXVzHGCjAN9iHedu3mdbvL0IEvx_JT7KriDiS4b8O10dKlMvcKtQjOx_0cm7J5jv_ZCb-ZudSupLtOpuoq-rP9Y2m7y-HAfEocL5QAi_qxVINOHZ7DETo3H8oVzBOuZM8eJzSX5EnO_QPKtv3IkImhO8dVQotLuUGrvIK6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردارنقدی: بعد از جنگ، جمهوری اسلامی طرفداران زیادی در دنیا پیدا کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/680418" target="_blank">📅 22:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680416">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
۲ مقام آمریکایی: ایران تنها در یک روز آمریکا را به شلیک ۵۰ پاتریوت مجبور کرد
🔹
۲ مقام آمریکایی امروز در گفت‌وگو با نیویورک‌تایمز خبر داده‌اند که تنها در یک روز از ۵ روزه نبرد میان ایران و ایالات‌متحده، آمریکا مجبور به شلیک حدود ۵۰ تیر موشک پاتریوت شد که هر کدام حدود ۴ میلیون دلار قیمت دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/680416" target="_blank">📅 22:48 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
