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
<img src="https://cdn5.telesco.pe/file/PWwb8sLpbgY0ZCNmZQLYm9Zam3CDDTGTgSh341yY00As8IFeXc6Yz9kjw5PFeDoH0cPDDlDtyh0ATYIOUffxHGM8t1B_6FtOKz1dyC7PT8JRLj6euAFG1xQVFpkM30LbnEdVI7VljHokLPFTyhQWMsZzL4z--roudc2rmR1jTVvzaJKc6HjbX_d3ePqCWvp36MaaCOmpBlk4qXzWXZhurtzXp_nfiP9xXfgSIF38tHfxV_jESyY-3PuSEPayEwAcTupwZBiw6z4rPuaH0qkwe9cM8SkxwXr2khVWdUNDBc0vnvP0shln7v-omG2DzjFs89dUres9r3_EiCpxqx7CMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 537K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 00:04:08</div>
<hr>

<div class="tg-post" id="msg-101711">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT3mZwSd9rJx2xLMIyoDO1mSsfj6I-RA_SLs2sTSnmw9CluDYSvqOIoIWo9itGA_l6MLCsnGMSITWqxN4cMHqOQO783UL0UxplirWLs7YHNLHfe6CNhUDBHO1UGfJI-OZ51cs_popUhAtUfkn_Ldqw-wSWSxgz4jfriwO3FophdyuKPUy5T5g_lnzZKTdd1UoT28DXEuzCSf0grHbhw6G-7qd2lB3SiEiE1Qs8hOTU04o5OMg7XgnknxZueeUZMog827KjXQ8j5huroCtQJSLkdQ_cVw88x3E6nKwRMyL8d_IOTzyq6UF4EaFp0R36177ky3dCkXyVJR3kGCYW6ujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رامون آلوارز:
لیورپول قصد دارد وینیسیوس جونیور را در تابستان آینده پس از پایان قراردادش با رئال مادرید به عنوان بازیکن آزاد جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/Futball180TV/101711" target="_blank">📅 00:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101710">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY0GAX1GE585Ga_-sXNCMRUWO5YoP7Jpg1dV3RDru3BgUUFPfq7XaW9U_F_ZMfyDRFeLhhecO7WR3y-a5J2cKSzxzw0WhBrm7kfJRAQQP48bAsS5pJzaQTFErKkfVehm6PBsjFDB_yo3zA37cMUIAj3uBozPYm0B_JpxAu3NmETm5QKpQP-ZNCOTtZBEe-pSJDXegRBdHqkp7DG_RFgx_tDQUjsQqNVOal7eNN3y34lEUOgdmEQXeOjgJyv4KOY-0qv_hef9qv3eO_JCi9FYZd2HqbC5KVtYz0OlaHpw_-UZlpDlcNwyQ8OUSt3UgxKjNgexexDB6yTqPyIUBRo15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزشمندترین بازیکنای دنیا تو ترانسفرمارکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/101710" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101709">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=dPDccm-ZEelcqwtFTv8wVMOAYHiiEvtAcSd29V_IshGTpveBwMf1KHwmFoCiW5m8ud9X9mQg6JtRFM4ZIQ7IzedW_OLd86p13DSj2hm-kOAbrhBvjTaZ0P9843czpIax8XH-jMWj7EmDfTgcJM2MjsKNwqfr9DSg265qRmkXTPtEN2dMRX1J764sFl9xohYjfzbsFt4aaV-h2FjvBfirNb39JQcO03tdsK0L84d1CzCXWrKpdMTX9dX6lasg9A7FkeyXeD1COEZaVuWWDyNht5DGdQwWGTUq9fFxMmlwZ-ETFfxi3xrolUIUREU-4qIv2IWTz8T2XSADJ_57uZW17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=dPDccm-ZEelcqwtFTv8wVMOAYHiiEvtAcSd29V_IshGTpveBwMf1KHwmFoCiW5m8ud9X9mQg6JtRFM4ZIQ7IzedW_OLd86p13DSj2hm-kOAbrhBvjTaZ0P9843czpIax8XH-jMWj7EmDfTgcJM2MjsKNwqfr9DSg265qRmkXTPtEN2dMRX1J764sFl9xohYjfzbsFt4aaV-h2FjvBfirNb39JQcO03tdsK0L84d1CzCXWrKpdMTX9dX6lasg9A7FkeyXeD1COEZaVuWWDyNht5DGdQwWGTUq9fFxMmlwZ-ETFfxi3xrolUIUREU-4qIv2IWTz8T2XSADJ_57uZW17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
▶️
در سال ۲۰۱۶، مرتضی احمدی، پسربچه افغان که توان خرید پیراهن مسی را نداشت، با یک کیسه پلاستیکی پیراهنی شبیه لباس ستاره آرژانتینی ساخت. تصویر او در شبکه‌های اجتماعی جهانی شد و به گوش لیونل مسی رسید. مسی تحت تأثیر داستانش، مرتضی را به قطر دعوت کرد و در آنجا با او دیدار کرد؛ لحظه‌ای که رؤیای یک کودک عاشق فوتبال را به واقعیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/101709" target="_blank">📅 23:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101708">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=Qx51gEOKzRgMTBkIPG5aIp7uZ8ZY9ANmDvJPzD3CMRJzC-BGxFyLShlsWJkwmJF6dxFYY1kRk44HRTmP11xb_VaOCtoWs4929V9LSRgWN_R-VeliaPCRiEY-6DS3jjOk5YhJvkV239y_vVGq27G5RbtRe0dgK3ma5Mu9U9OhQ_pJmQz76VQ2Geh9gxggCXbV4Mq5Vrti-Q-Zd0TOKIklwhHW0LPnVpwaMYXhoici0oRKzjXpZC3_I0WCN3R8SW6CD5iPW7-pcvEao_S_uHQvmvUnGqM_38ViuwV-jJB231gnVZInsGnRNlrxpq38Gu_ePLqIfybtC8a3GlQ2wRsiTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=Qx51gEOKzRgMTBkIPG5aIp7uZ8ZY9ANmDvJPzD3CMRJzC-BGxFyLShlsWJkwmJF6dxFYY1kRk44HRTmP11xb_VaOCtoWs4929V9LSRgWN_R-VeliaPCRiEY-6DS3jjOk5YhJvkV239y_vVGq27G5RbtRe0dgK3ma5Mu9U9OhQ_pJmQz76VQ2Geh9gxggCXbV4Mq5Vrti-Q-Zd0TOKIklwhHW0LPnVpwaMYXhoici0oRKzjXpZC3_I0WCN3R8SW6CD5iPW7-pcvEao_S_uHQvmvUnGqM_38ViuwV-jJB231gnVZInsGnRNlrxpq38Gu_ePLqIfybtC8a3GlQ2wRsiTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/101708" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101707">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utPP0cOMj-24S5810Uw6MuOAAQ2vtldgmNJXjzHWCN6lczYSzLRBuD9QbGW0PpqFY2Ej8u9aHG7XHOkemSmyRpDmWqBitX-9ECIUcH3fEjbVFb7Iyu_gH7Zd8OIwDiidIW-ctCGGXwU_LcwaiHMcRkDjmCOzawxyJyqg7ntRQyfoRc3jm475h9bSvOZRKp1UC-fqBLOlh-YQDTXW8FRalEmNTJ9vcgpN5yxit6UbGGRI5u5LWbc3ztjG0KWO_BGnrstKYgsrenE_7_4k7sExKJLDTT-jzMxurrydx7EUITSKQ2WnKvNPqk_U-42ufBq-3cBMHMmfhqnRqGsYrj2uEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ال‌کلاسیکو فقط یک روز قبل از مراسم توپ طلا برگزار می‌شه :
🔵
⚪️
۳ آبان ۱۴۰۵ : بارسلونا × رئال مادرید
📝
۴ آبان ۱۴۰۵ : مراسم توپ طلا ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/101707" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101706">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2tRimWTdH1YUTWmFjyw7_wbB-IwpviqrpLd5WRF5WpubB1Hsi0tE_pHV5rasLZ2GF1tcI8GZ8BhicPV99AK0W1euXzbmyFzrpHGkR4QFfvjzZ-WKeqwfSZpr8jrSXPReCyQgFakzxZNl1lf47-8smxzUXELEFeXXBe5du2_miJDu7SzlAA5xUDECfpuYSrlouSRQXFeR7SZtF1CevcDx7SWGrLLXcmzXAnZ2F-kKNJNRlxXB_5t5PTGPAw0nYwpoXj3er7fAUSJ9-qJXn3bugfSLbLOQSfKn35PpFzTTNjKk2UBFINWkLKSvLsxkkPbz8DV7HS2Jbi6WfkYuCROkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا درباره اینکه چرا همه بازیکنان کارلو آنچلوتی رو دوست دارن:
از نظر تاکتیکی دقیقا میدونست باید چه کاری انجام بده، اما چیزی که واقعا اون رو خاص می‌کرد، توانایی بالاش در مدیریت آدم‌ها بود. همه رو کنار هم نگه می‌داشت. هیچ‌کس از نیمکت‌نشینی ناراضی نبود، چون با همه عادلانه رفتار میکرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/101706" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101705">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH3V7p8ls12R3L2gGM5S0cZiZGeEzPRe7gqBAZ87jZ0G5ehAHKvn_wx_KDh47Qr7zT43YFmgdwvCOPA7Xi5S9RBZtn-prm7Ks8NTyqLIEK2cG3PxRDOC3b5eo-JF7DIiOEOHN-jBXOENwbn32F5oGTx_NkZHg1d7p4Nk6OCyQ-CRQ7R1VYIik4GHGLcm4S1TNsDxmOv01V-8eTAB0-JzSXOXXCr_lKayBY0lFmXprsr_2eCRUmmKzJqCYSSqkEp1yhLUNt8hA46PkICaVn4nw4NKdRr61rvqWP1JxIt98dikVIe0KnkTKIKuGupkZ8my-IeaMkwMcFW_02nBovpEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
به پرتغال هشدار داده شده بعد از خداحافظی رونالدو ممکنه بخش زیادی از توجه و درآمدش رو از دست بده. کارشناسان میگن فدراسیون باید از الان برای دوران بدون کریستیانو آماده بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/101705" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101704">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🔵
پنجره نقل و انتقالاتی استقلال باز میشود؟
🔵
💣
همانطور که ۱۱ روز پیش اعلام کردیم، باز هم دقایقی پیش که از محسن ابراهیمی هم ( ایجنت و معرف وکیل ایتالیایی همه کاره پنجره استقلال) پرسیدیم ایشان اعلام کردند پنجره استقلال به قطع باز می‌شود.
✈️
🏆
@abitajsport</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/101704" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101703">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0GRtTNIFyTx33WdclxNlph7cDXA42OoER4khwL2ZUMsi7myizFdnsEca8AprTbmYF-JgxAktYxKYgL743KzPRQO1NkiEAlvsnCOgDOQPCnpqbQ44IVtPxeUFJISPOtG3eWkEORFFtruy79Q0GJoVhXAV_CVubifJfphfFl863RKxf-H1XegUPKwcRiiY5QiMG-FWU8MsYWjxMqktH-aFk9b53hbpvOxysB-q6MCttU4gQFsf8xxFLEQei-CFdugt4KdqOZQcdjJG6FHL5mrpvqp7smrIbWwMOOSAO30Y5Qcdoz68ImqvIUGjTjd0wHGMpDuxebNO8CkoQagOONz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه هنوز شانس بردن توپ طلای ۲۰۲۶ رو داره.
نشریه اکیپ یادآوری کرده که چند بازیکن قبلا بدون کسب هیچ جام تیمی هم توپ طلا رو بردن.
✅
کریستیانو رونالدو در سال ۲۰۱۳ بدون بردن جامی با تیمش، توپ طلا رو گرفت.
🇵🇹
✅
لوئیس فیگو در سال ۲۰۰۰ هم در سالی که جام ملت‌های اروپا برگزار شد و فصل رو بدون جام تموم کرد، برنده توپ طلا شد.
🇵🇹
✅
گرد مولر در سال ۱۹۷۰ بعد از زدن ۱۰ گل در جام جهانی (مثل امباپه)، با اینکه به فینال نرسید و فصل بدون جامی داشت، توپ طلا رو برد.
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101703" target="_blank">📅 22:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101702">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwwQiERcKpOA8yxBfXximaddC0TZh4Tqo9ca-Nx04bv5DDqtdcvAMoReNugauWVT76PKkkSzrozCSHLGDJIHTTh9H3K3r87MWlgoI27zhJzfWdKETGPIdxuCAgAY8_K0-040DO9WZqbNnbEWMhQtS6KNhLzsVn_aFZumNk8Obu-ZgJsYdHKb2ZMUyk-WauqBxhL59FocFDw9Yx5R6QzMHPsZ8voPFem62qvm5sfWZKC7fbDOGlXo0SUW-4kDncmnSuLsa-kSZLVeve0KDYj2zyk2KqemOhBJIpeh0P2pqhNcrVP_8cr0EiD2eg1VUyFD6nZ_mHu3l3rrjcFtVwtxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101702" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101701">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntcWXnJpKYRpwT4MkIr3gx40Nc0PFpZ6XPdvWQINqihnu3C2C5LT1BudJXvZb-l39Zwt0mdKcPaMN9Lyv5pE3YDTgPids2JKlJbN421LXMqXdUTHTnAAysZkaxUETAo8uX0bcC7eN44KveduoQsTFfS-mowwnm02RpOdfgCi5KQdRrhOvr4yBgjAv6H_c3iAqAeuvO4dsBqUg_ay59W7LrG0fz2yJ_btnCiIP-Gn7syBOzsA8oOSt_vO8dZqjdDlIsnMyCD-9ssSYWkd0DzkeUbz-9OuyBKNf2M90AhchSvdAdgjpx0j7rQb1BIaOHnUKT1bxEu8PuMTgwdRhyaQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا:
رئال مادرید شبیه یک تیم ملی بود؛ چون در هر پست، یکی از بهترین بازیکنان دنیا حضور داشت. هم‌تیمی بودن با کریستیانو رونالدو، بیل، بنزما، مودریچ، کاکا، کاسیاس، سرخیو راموس و په‌په واقعاً چیزی خاص و فراموش‌نشدنی بود. هیچ‌وقت کامل متوجه نشدم که برای بزرگ‌ترین باشگاه دنیا بازی میکنم، چون فقط داشتم از فوتبال لذت میبردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/101701" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101700">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMKT1E0a0Y3Duj847s1aPi3yVZtsPKFyjw_yVL1aaX4MnqA9q5zXt74SZzOTc3WuUl2b-B43gWKsyl__wt6KTd7sQjg9IkLcQgaLVU99X7dUQF0SfNk_HSI84DEhd06LH3kD4Huz8sgHBwkRcTQRnrSCeYKZ6hfM_ZSVJfEQGT_deh-GRAc2h3EOwJA4-SC4Rw5PvPvdGBt4kSh2Hx4mv43u4VQ9SQiore4fovRHkZxbh5CSOzNlir3CZBKhUIdKSms7UxfgSYSsiYeFYFxV0HVAjLD2zTUKbXTNIkhHrV06I26pTwGeLVXENLHWLNLRZYrLW5mfCdAB5IHXmJBHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/101700" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101699">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHg0s6K5RNVaXy1dubBKUBWZ9ZAxPR1itUcDAiIDU-3ssCVsXz3OkFN_7WrpR-X0J-N4Fcp-hsnLbXmqKnPBYk9KBKLlO5uIuF8H2hem7RuttT-S4a9J59uEasvvLG1ZxUAdo1UYDXVjvxatEewOVLuQ5fCKuVzFLtiLZdBnbDm4_P_uemgNN1zi3p2ndqMmygVRk6X3TO0StiaVDAXiO4ntLB2VlviUr6nN3N_ThMlmorJ-2IIp_fXG7-NRPQic-pMpohX4wauN5i_qG99i-rnMeYL2ufzebXiuLNeLiIFa26V4qj4qeu9V_9fWGRx1hBKC5CbgiSbKQ_4pAKFRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
فدراسیون فوتبال نروژ قصد دارد بعد از دخالت دونالد ترامپ در ماجرای فولارین بالوگون، یک شکایت رسمی به فیفا ارائه کند. این فدراسیون نمی‌خواهد این دخالت بدون عواقب باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/101699" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101698">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOKXcMKfvwLwTBMUtBUeFDXeDE4mv2gpJdqxr8-LfjsHJyKez9Czexmjcz56kUrVj0h9eloQYIkwruMUFVqtKd7Yc54yKYK63JC6qax0H6xiZKolErnlK2kDWE5q5EIxzJ3LNEXD-RBPqQep_D35Rsow2YRQZOpV2xGITl7jNmtxAKSS9zH5S68LjBWyoipLryKqxW0vL0hW6p_wqmBXyyX5Dt9VnYWCRHXerZ27HSVV1Q0cI518fyMdFkv4bUO1vOfR-cVaTcIhAP2MpZ_9A2qnHj-iadLisp9CkiDhUTA8UOLhIMEX7EbPcUh3fOSnglMup97pqgPD6MTv2xsX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آنجلوتی پیشنهاد فدراسیون فوتبال ایتالیا برای هدایت کشورش را رد کرده و گفته که میخواد در برزیل بمونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101698" target="_blank">📅 20:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101697">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biZxtOpwShWOl0bjJESsqthGHCBBXp0FIYfX1wR7h-a4-rQo7_28eTTLKli0iovODyU0gSNlUCU7d5LCEN-PjyDfLkyUcLiHgEAH5KCI5Ekbnegq8Byfz8S5odYQOU_ZiX9gi7PJ6XJhHJcb6JynMtsuCTZNQ_Bm1IMjvNMHVqsh2Jwze8DmiLCA3tAGu-vlkSYIgq4sG27VhtQuhFj_n3GaZMjdb081SIqhhqrvjUYxhg934xm8xtrKNL07oJem2dsmp2tPseUbUXQRl8dAgC354QxV8IOb_T3jyU3LMrdY5P6EqczemUAPbGXIkruoaNj_6CmkisJ2UA290CYyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
لوئیس دلافوئنته بعد از قهرمانی اسپانیا در جام جهانی:
بعد از بازی، بازیکن‌هام به من گفتن: ما همه‌چی رو بردیم، در تمام رده‌ها. حالا دیگه چی مونده که ببریم؟
🚨
🔻
یادآوری:
این نسل از اسپانیا قهرمانی در یورو زیر ۱۷ سال، یورو زیر ۱۹ سال، جام ملت‌های اروپا، لیگ ملت‌ها و جام جهانی رو به دست آورده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/101697" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101696">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3wd4s4nAsjhVFAS2JS3kQmHmFE_Rfgg-_egwbPKvr2Yvi1wPJTFdfAcVNanMGfPvDbcOUEd9Pv7yWW75cHuZ5-bu6qrvpnMbg7WUWbvv-v4caX8nJBTqiiGiAHEQV0rUk9awcjlSCMMaYPZVoTZ4xFTC6UtVoozOSGdnc9izFxlIEh91eG-mBuilCRTPHCNbj9qMnZKI4WJ8s1w7dKERX5X7FoNpQhxxgKHrEC52fg3h14nBZLwuiBhpJchzdAG8YBZl1a7ocCxno1g8VExFffLyfl4WIbB1a_mfln2A0Bc4EoYav-K6QaPXy-XGiCt0U9TfldhTY8z6NpzDrYB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار در کنار بتموبیل و هلیکوپتر و جتش :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/101696" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101695">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ9-tqjLnzraQWX6OTQM5d4b6uF0QiUyS22OitZ9sxK9M-LspbgN7X-hL7RIucv4xVzCs0N9HnjbzacC-jCj31mUSGIQ3HBXGCEFVxkgtRPjegttoL0Te7o3n96lIWgF9XEGwh25cXhA1LM6r_rXcZdHv31uww9Lmq2EiBmQBmJdCF3YX-wm4SpZ9q3saMXnLIIpKvkH7LYg9gTiBvbZZcpkhvKqSBzfCOgmPwUCkv1Isji213P_2JNmgG3j4LNTZwP9no7VGdNUcPKgsvKTh-k3utDIVEbNsHow5yu6AuQHL88PHkh7h-F5mw9gQgo_QV6PQhRZzyzjbrgXGO1c9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101695" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM1UU5RzVARCgNQZDDirfmvhh-_DDfDnVPw7jIxvV9xmckFZ4NuVCUac_gkJT1qmShlADm7lAy3QF5tGmub9Ouw2Dcf9UUA_LF8YjBMQTySzv-SR1-U6l3gMB1ppVAJXJbS5inewWpMQ65ZwHEoEzTHIYdTZutH4iwvxiBHFUl2Zc2Xg_nf032ZvO9BnAEES4Wc74gWWH4Dhnje8fFTeoyCyi2-uTNu0eVkW6pcU8dvByajP_AaMjWoL9Sc8_2whjqi1L2-o7cfVkgdjAAwgk8v6p8OtED_NUulrl4DLHu_i9KaAYf9MgWrSJAaBbYoa2GdfQrCQBI8FOCAXbZASUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
سامی مقبل خبرنگار معتبر BBC:
🔻
باشگاه آرسنال قصد داره پیشنهادی به ارزش 70 میلیون پوند برای جذب برونو گیمارش به نیوکاسل ارائه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/101694" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=GhoGP0-Pz0VecKxZLQAWG8JZ9ynWtp0LOJamnOsHX1pgqfWLUlR0ZI-htl7t-DzusaU34bjSvdaPubKi4L3XF6BDQmAUnNRrPiBDpAPd3yS2ctueSZPYnIGV06lZElXdcDyw8SHWV8LOOeZmTxbHgKAP3A4EUKb0GxogT8XFA0ds9oUzpUqdEAbhHub6WsyzigJJXFjwhmNp7gfrOQJbk-__Fz8EIZ3PYoMDUQfynhVcTmJlKqthb6cRX4F7cyndXaYEEhvzyUmYfgv6iW0mEjy5N73vHwzUKX3as8JCikLgXP-PbHBnrZomVyx_zmln3wyzH7lNESrmMGFzdyGFGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=GhoGP0-Pz0VecKxZLQAWG8JZ9ynWtp0LOJamnOsHX1pgqfWLUlR0ZI-htl7t-DzusaU34bjSvdaPubKi4L3XF6BDQmAUnNRrPiBDpAPd3yS2ctueSZPYnIGV06lZElXdcDyw8SHWV8LOOeZmTxbHgKAP3A4EUKb0GxogT8XFA0ds9oUzpUqdEAbhHub6WsyzigJJXFjwhmNp7gfrOQJbk-__Fz8EIZ3PYoMDUQfynhVcTmJlKqthb6cRX4F7cyndXaYEEhvzyUmYfgv6iW0mEjy5N73vHwzUKX3as8JCikLgXP-PbHBnrZomVyx_zmln3wyzH7lNESrmMGFzdyGFGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اون دکتراهایی که دکتر علیرضا بیرانوند گرفته
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/101693" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZjI_PhXB5XGRM1Jzvly0fPLXD_qO2vFx5JtzscIAFmQwRuLD2BbgDSR-HTQe8jbe1py61UIon7c9PM_P-aV8i2ujJPyLAZ4kXRSHq1wFjSBOGVJN8SzG0Yq50B7UiqxjydMGugbXQsQCOQWVE-ebv6kbnnm4qSiAorE7hlmsXHsuWtrzzmXSoGu7aj2hkQAy4-Poyz0DdLQF5dfpCzM9y1InOlfxlpaMYz7uCgGeDdY1X80EIHHu257wpzqwJKEHiaxROksNEmTPfBZu2B2uPNPF0K337maTPOzlgUexXDXsnXb_418-3g4uAe0Ryv1piKEOYvDEnAS7fy97K_3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی که همه رئالیا رو برد به سال 2013 و اون کیت معروف..
⚪️
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/101692" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101691">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfHnv3Nucc2Cqtlwfx8AzOcGngqGBKqcdZCCqpNO4CsSl6DSu_VIhwW0sD9XvaKfGnpOkzIaumIjs5N_2PSATNht700eWyRDk0h-EVI6AQNUhzDPWnRF9clf22YJlv2povKLLINkxdxR1VlC8Epl3x7l44_Z8L-u_FQu5J11cGuvCR5FvXzspFGeqFsNz7AFLcuJ8WrmW6nlOqbZExE1ETbMMzEgPT16GeYS_WTLzU2vAbJvMQaYidOSBzfqy00o7_i09AbuSl1ZSwvRH334rtvZkEUq_78g8UUaHC4vzlWtSFvbXWJ7gPpvNsCC7M8ozUbPDNlIQMw3Mt_RQJ75rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو درباره پیوستن به اینتر میامی:
بی‌صبرانه منتظرم به لئو مسی کمک کنم؛ بازیکنی که یکی از بزرگ‌ترین بازیکنان تاریخ فوتبال است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/101691" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEGW7sU_G72g1rzeGwlEIfS1F4yH46mb9KsrFBlyN-Fi3-1DYQrAOEPA2LJ9AdGrGQmKN8AbhWvezkowNOVp2T__uVphVQKhJAt7c2fMe18RdpNGtiO_gRb4bWy8CJaeP-t4BRQlJ-35PHC4pHhHXLBSmIG6gMz8_8bA-3CkSJkraAKNCYL7GUCTbfi0djhBKSJdCd5WQoSgxTkOW1Q8vyfO6zWHLqf7VtSazWsVbs2SnwA7UAos1vxNkbRjULUCGh59r1WPkSCCms_tpxbA6akuE3eOEPaG0q3K6xeQwI5OQM4rljQJyVo7ERgNs447zHC_88Cx2AAHXGU0hI91iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
فوت‌مرتکاتو: پاتریک‌ویرا اسطوره فوتبال جهان بزودی سرمربی تیم‌ملی سنگال می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/101690" target="_blank">📅 20:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101689">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF2DKYPU7UOIVyKA9tmz801XxkXMG1NP1DXqOd3tr0JV5zFFdI56QCXb9z1Uys22lapQaCjHzXxRiUZ0KkNyGJgpowKc5J9aBg5vaxhZZ9I93s6t_k17vLfch2E2UuU9alGL0hobL1EK-GLcaMLJrOkbqjqQfqL6RGqZjz3Zjw0pBYtnnC_D1Ykiw39ajOa3XHnHcy79cr7GKSAGwqqRrA5Wcp5NsWEwJDpwMQoLxhqq6X26PeHLj5xhhFTG98CtV_V1WQpGA3hrAFizDugUI1Ww9UfwDVlYy8e-FbpahWO6x2ejvDb_pPkeAdNNCKBTXwy0Z8Oyz3NLNPtNJQDkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی
؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/101689" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101688">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtyMv5uynneFzs5LBVDAMha3_03KeoP1kWgB-1bYkYayrk9t8mFEwTBJrcLqEk0yvGZVc4NkQUQFcHaq0WBGphVpTiJRQ_NzW12vEQ4KdhN3AiQHd_RkGyBq94rPfyitD0wYNxGy98dsZbz1_UwZs7AX_1R5cLgMs8OpUT3wQPMrkdsCgtdnHr3fpF6dfHZ3Y9HrS4ntcs6lqZ5-qRoLQtyAzGMUDhZRbXIj8qnenym1IrH3xUBdG3O0DAJXeC4ZuwWUfQhdP0lQXxKWJ4eieCnVzaeZPGpIaw_akjdpyqVlpCjj1RgafXiY4O-vRZV5Dg_s9MaR3Q4DR0gKpU7s-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله کارت زرد به من نشان داد. من مطمئنم که این فقط به این دلیل بود که مسی آنجا حضور داشت. ما 2 بر 0 جلو بودیم، بنابراین احساس می‌کردم که داور فکر می‌کرد:  بیایید کمی به مسی و آرژانتین کمک کنیم.'"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/101688" target="_blank">📅 19:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
فوووری و رسمی؛ تریلر FC 27 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101687" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101686">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVInxnkaj2L1xYQkevoVZcOhWIZzyT9FViRKK-NYtKoFOxgrfwJJxyKC7ZgJhRZiflWcUHHbIgMNFmYwBmo6uF78UVdiafYa4zXw0-cN4ZI7pE8ThrYpZbqyv0tKaIK8ccaRvxAjYZgK_zr6-X1EOzevoBYydVOfO3vf8RGppKuZ_AuEUXS8OwdG6bjj_j93DTPA3KKGS8ekT4BrVVMpLAYDdILwe-21ZtRnH3tNmU_IcRat31_dFB4_yFbvUqDYEP3ZkddGvBlOk0Mf0yDLIrDFxq5cHzIQ4YgiokSE_I9ZVnwumuOIpFCBNIzM3vGmSanep-fvmAIsYdVr7xVOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/101686" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101685">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBAdYAfTvDPpPSBVbe1x_7BBbmtjzHPkx26MtIPZMjD301yyJtls7mOk4uRGrDxUq3946Qj88jjyEz1AcQlvPU-utcSKFHGjCHuccvVvMCenXrWVCKnBKG8PiuDxUPQNFh9VzMfqcVUT98uPQmg2MoGnPPbAbWbhCZS7WyLST35lVLxORDYoGDgF0lb1bGC3kVVdfKzFrF4zQFg1LJFjGo0Q3ZgmDblqz5z_YrSO4qM3N4HxBToQVC-pmj0r3VPZtD55z0v9Tsr1d9KqMmhMlXOsn095X9DT30o_hS1L0reYeJIePS3pcjMbOfXtToAzlpkcJ1XomueFB2b1lBx90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/101685" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101684">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfvRiurjBmkmc_PgbBdICH33E7aBs8bjV7JyXbcf9fS88FIT2dUq2lBl1RcLFW81HLdliQWbyBJP8OkEzVrCLeNjyEv7ZId2W8_5mAEe90Q_OWw9BRDCCiaE-1-pD0e1bqjoGpJ5uBguYCIspmEMwkp_HBfNXtksYvfukcjA97s_52bVUSKqohZe1XbQ32WySyTKEuvXHzkbtJY14BfICMcBpZ3WgKHUVm9a9uu5JPquAl73fWSlWGcUjqgpLplH_fxRCGtrowOiEKJXo3BpdTi2GhZzGN22vD86b8QEpzjtofIUV1hSCeRb0ikRUvZdaUCl9dOc4BTzQeb8zZHZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسمیرو رویاهای همتونو داره زندگی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/101684" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101683">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEiljS4vHyiit-kHamXfMhgjnaTCAatHey93LLepEHz1lHAFyf5b2VgQIBClCYWNQ_qX0EtglWaYkpBlj8_zFxxNn6fN6Nq59_gINMpj7jjxp8ubkbhThrW0zMH5CwOHi4OCJz4WBl890HhQoQqiNuZ-nMw7gPjoCK-vSZbbCoxYIGqxZbQHYTwAoK971haD2thQQimf4pj5k5F3erIJ1C8XzZfuwdwJrV3nDL3RNOaPALXWcgzgcE48BRs8url7i8kA3y_AYsUEh2kreRc1_dZTWTEVfGQTiS5fcMbbXIoCAh5bdHRAP97LZEOv-jFoir5zFp8F53tU84twC3RCmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمیییییی
: قرارداد لوکا مودریچ با میلان به مدت یک‌فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/101683" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101682">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf1Fos93-C8uyhHG5LdSPvMieoQbnXMPTGFQY7I3gImqqnbpT-kyF4xrN4dJwu9Hkrw9R2HRqracN746SkkGEjkgFdLcAGjUrTUN-oGKueit3bk7XjK3auT0DE94dO_ptRa3DxvF5EQu8z2pB1BTQs0tTg8R2vS5t2XMPi2uRks3en_EyU8fZBxnRE3gEdZhn9c6SwXfaQKaN90X72DZW8mqPuAG1XYgjPF_GuDuQi9MACtJ3MzwHg9ZPT0DBLle3iEgQQi4A6Cty6qCEYT2oHL-JB0OQIlo-wyLfNMTfsTOTczyIaaZzQYO_4UQrvcnn1Ja4wBG2ZtMAjesuVP3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/101682" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101681">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=YPOxpb9DuJPAqIDmwoZ6T8YmaGKHtEyoJtIaNRfi_9giFBH4ZMcY-k4UmXHxeHAiC0IgjqayWkplquux1mmHUDEiLpOCEZxW3bwc7ykYz0Z4dbumtsweKv9TvKgrU45ELOBhTZVRuCEGmnbhWAYTvioRLerX8mFKtBNQQdiEsbsWAHJKOldH77w6nCwqwpK_oHxCJT1hRlTaTtbHF_Zd_sLrOtKOhWQfBJH1q8G1mMX2v3OGvJQNjgwbzICRNoOIUNhdX3pjqthhOa_s1DQhwNAkUroNAUhvXt2gqHVdogqvxU2BSIulVrj2wdRwh3X9mzCK6_tfw7jc2sjhS4ndYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=YPOxpb9DuJPAqIDmwoZ6T8YmaGKHtEyoJtIaNRfi_9giFBH4ZMcY-k4UmXHxeHAiC0IgjqayWkplquux1mmHUDEiLpOCEZxW3bwc7ykYz0Z4dbumtsweKv9TvKgrU45ELOBhTZVRuCEGmnbhWAYTvioRLerX8mFKtBNQQdiEsbsWAHJKOldH77w6nCwqwpK_oHxCJT1hRlTaTtbHF_Zd_sLrOtKOhWQfBJH1q8G1mMX2v3OGvJQNjgwbzICRNoOIUNhdX3pjqthhOa_s1DQhwNAkUroNAUhvXt2gqHVdogqvxU2BSIulVrj2wdRwh3X9mzCK6_tfw7jc2sjhS4ndYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سوال: آیا مسی بهترین بازیکن تاریخ است؟
🇮🇱
نتانیاهو: باید بگویم، در کنار پله. اما در دوران ما و در دهه‌های اخیر قطعا مسی. او چند سال پیش به اسرائیل سفر کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/101681" target="_blank">📅 19:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101680">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
فوووری ترامپ: من در حال بررسی یک حمله گسترده هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام داده‌ایم. به تصمیم‌گیری نزدیک شده‌ام. ما برای انجام آن کاملاً آماده هستیم.
اگر از اسرائیل بخواهم، ظرف دو دقیقه به این عملیات ملحق خواهد شد. ایران به اندازه کافی احساس درد نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101680" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101679">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=MxmhuXRZ3K4XVbM0H4DMA9WfE3vEXqVMn-OpaEBhUjTiZmVVYb5Y0cJRMP-7Ewwt9SbA7BZwjXWG7B5DPlxdL_4G0BOYQky8130Ig-FpQ16JLelsFJGXRROhlOXm97F5AO_QbgodcqgoWtgTIidhJSmi42BRJcIZJJ3iqqfUIJgZVvy8YIHZHUOvf8WfgMKM45tFa-nkYo9Wbj5xItulYLfPDIUe0qhS8pJz3mrtXsR68LsLewoKSYdtPFkx8n_P9XCj-AWexrGktWpi51bLr3rZer3KABcDg8SWIPD7PgoGDcrHRLEBOy5VHdQuAfNdeGezEWjgTNVQBPizKO3HTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=MxmhuXRZ3K4XVbM0H4DMA9WfE3vEXqVMn-OpaEBhUjTiZmVVYb5Y0cJRMP-7Ewwt9SbA7BZwjXWG7B5DPlxdL_4G0BOYQky8130Ig-FpQ16JLelsFJGXRROhlOXm97F5AO_QbgodcqgoWtgTIidhJSmi42BRJcIZJJ3iqqfUIJgZVvy8YIHZHUOvf8WfgMKM45tFa-nkYo9Wbj5xItulYLfPDIUe0qhS8pJz3mrtXsR68LsLewoKSYdtPFkx8n_P9XCj-AWexrGktWpi51bLr3rZer3KABcDg8SWIPD7PgoGDcrHRLEBOy5VHdQuAfNdeGezEWjgTNVQBPizKO3HTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تنها جمله درست گفته شده از صداوسیما در سال جاری خطاب به امیرحسین ثابتی: ‏مگه تنگه هرمز مال ننت بوده که بدیم بره:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/101679" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101677">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBvBU9UvZ53UrRA77PoQTnoi5VwF04uCG2BZoiKHpFAR-7Ry2byf3XWqJiUDVLKCOLTSzb5RAqdYI_QB0QcIi0ZU3VY9aRUdLK_J3Ebm4UBSY13tTHGp2PRlIxYf4uyTfn0PMan9mbiN5EW39vXUgDe6wSZuhtW8BiD3wIs7RDtAxX5tnXgPpxjiVJ6K7gBGCNfTyJyI1zixgTo8mqi-B7xQvDMu9ABT0-clUk73d2FNRzr5BUAmMMkbj62uf5dGgDXVEp3RCu1nVqbFCvjo2s1DEWjf2tOi6rd9tFEkg7O1Rc6y09YaTuFCIhzcpPjJ0_SMgh7EPd2BuA6G9A59XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4cstiVUr2mWlDfsIZ0LugzXVIRuxfvMof9lxiKDWqr9w2alY5OrwWF0l8sIFJfG1OAi2LCEwyw5V8GrqAmrTcZs2kE4fHd4WErYrHwjkAJjP0tEaJZ0VKrHbGx-w0iJmikqV0B4ydzbALpRU309kQwHCS4YNRHfZSpt3QAz5-Il1P1LmKRtqiOxq-Bnu03GlkhG13PK0J9GXRIWOfmzBer_C6swwcVsc_hRvv8rICJayuFKz0ZBSI56My8vk0fll9l51SXtI-EMyAOdhhyAehpM7OCoQwSIKBaqeNnUUMSmjMF--SEPOvxwH6L1hjlrwxyMK_Zd8LhHicOpSj8g7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تبلیغات جورجینا واسه برند خودش Mimoa
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101677" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101676">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw8HNr0feMR04p14iPj-ew_zusvFoQq5MfRbzm_i5rDae5RI3NSSy41JfXOnEUy7jaKsmpqwJg-8kJTGgrH03zxn2I8R-DHgixrHsksvrQ7lMPSvuwu40-V-vIeCB2m3zbXVRheS068dQgKLXrFD_PpXkCML6HkJw82M3Epsd-lnxWuZ2y2PTfGF23Klt0PpqnTx1N_coNVonNlwUkTOacwf-JQyeQMj5Go18B1GGojeFU1lJe7eoNykv3QNNWu4RwDSWTYZR0lG45Ud3Fq_I19tfpD2FMgCe3xWznL1n5KxpTRDatU2EaiijIgORStluKvchKmqmelMeRf-Nwm3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
منتخب بازیکنان آزاد فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101676" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101675">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d6746099.mp4?token=Hb8z6I2Qetg-zk_BpHXgRiltOzXNQcm70NEjaujLTD0U5LObyUHjdJx7i0qrN7ZPHdsncxPNj67e4kBSKP5x2NPdKhOaJkprAJ0NCfUvQkmWRm_TBeATq9OM3EZLBsfMO5njDwI-8XRKbnMauZd8HiZsH9CFk-ylVPnsG8sXwCKk5ZQJQWWx1Tj2f7f1MuNjSKpbWiWYeLd31VMnk71sTyaAXbDLSBVoNREsOp-uKna3jcyoA_9W0a2sAMevwE_UkpPRf4lvaHHlkqeCpFLcCp1-pj0_fh48PQNzUXz3maglZVdNDwql73NSXOR8dpbmnwlOlKkNGZudduRuO5AuYTkSzCkG6c4wlBtCa5LMNJIIlmbIYoK8ocAGUi9brWf9D5cCVQ2VqEx82FkgNiO7NgTP_BSUk4O4lq_3OhtxpEInNKg4So85tv8Oj8ifLtZizoLOfjhnrh1E8MBSK9JyuStbCn9Kl8o_vVzCJ3OrdbwkV-te9v6SBthJ3uTKwt-p8HemYrObffAMB3HOz6Y5x8yMZtYDXJXADcVOrkVLClwZTPo7DlUGUcFoG85NjN0_6NNxHv1Z7Pd4TKiJ4YQb-1lSxJl-1KZH6B_VUzS9rWk4R44xkFlc6FvyvSM9KPhSFLULs4cvjFF2wByJgbzhtH9SpMnfnxBsSEfFMy2zE08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d6746099.mp4?token=Hb8z6I2Qetg-zk_BpHXgRiltOzXNQcm70NEjaujLTD0U5LObyUHjdJx7i0qrN7ZPHdsncxPNj67e4kBSKP5x2NPdKhOaJkprAJ0NCfUvQkmWRm_TBeATq9OM3EZLBsfMO5njDwI-8XRKbnMauZd8HiZsH9CFk-ylVPnsG8sXwCKk5ZQJQWWx1Tj2f7f1MuNjSKpbWiWYeLd31VMnk71sTyaAXbDLSBVoNREsOp-uKna3jcyoA_9W0a2sAMevwE_UkpPRf4lvaHHlkqeCpFLcCp1-pj0_fh48PQNzUXz3maglZVdNDwql73NSXOR8dpbmnwlOlKkNGZudduRuO5AuYTkSzCkG6c4wlBtCa5LMNJIIlmbIYoK8ocAGUi9brWf9D5cCVQ2VqEx82FkgNiO7NgTP_BSUk4O4lq_3OhtxpEInNKg4So85tv8Oj8ifLtZizoLOfjhnrh1E8MBSK9JyuStbCn9Kl8o_vVzCJ3OrdbwkV-te9v6SBthJ3uTKwt-p8HemYrObffAMB3HOz6Y5x8yMZtYDXJXADcVOrkVLClwZTPo7DlUGUcFoG85NjN0_6NNxHv1Z7Pd4TKiJ4YQb-1lSxJl-1KZH6B_VUzS9rWk4R44xkFlc6FvyvSM9KPhSFLULs4cvjFF2wByJgbzhtH9SpMnfnxBsSEfFMy2zE08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ویرجیل فن‌دایک مقابل بازیکنان بزرگ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/101675" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101674">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=f2pCn4L9-tBkk7ONXAXARFiZ6oDL47w-18UWhBbK9zQ39Txc3r3pAV__WrjItu9PbhStZCGQbi3-fEOJAy6kuMPcFrFx12_cNnPJ3bBFlG1wsHA8pD3I2pSFZzoXuLs2_qvqm0gU5VrjvDnVOuHObeFJj8Pl02U1v8Q_IRdRmoEh3VFOZ92F0OIeF_p--QVu2OuPgW45jZzEJ2OE7XDk3bxvNUkTR_59379DUov34CM19xcj0i5K2nXdlzxt0zFU6arXyhavXI1ke8urwZG86M6qnaAJ-8N2KFVyFe7kdNe32IuVuxphnaFq15xjdNJPrN8jxipuNUX3_PkUL6fhTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=f2pCn4L9-tBkk7ONXAXARFiZ6oDL47w-18UWhBbK9zQ39Txc3r3pAV__WrjItu9PbhStZCGQbi3-fEOJAy6kuMPcFrFx12_cNnPJ3bBFlG1wsHA8pD3I2pSFZzoXuLs2_qvqm0gU5VrjvDnVOuHObeFJj8Pl02U1v8Q_IRdRmoEh3VFOZ92F0OIeF_p--QVu2OuPgW45jZzEJ2OE7XDk3bxvNUkTR_59379DUov34CM19xcj0i5K2nXdlzxt0zFU6arXyhavXI1ke8urwZG86M6qnaAJ-8N2KFVyFe7kdNe32IuVuxphnaFq15xjdNJPrN8jxipuNUX3_PkUL6fhTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
داستان دختربازی افشین قطبی
😂
😐
محمدرضا مامانی، بازیکن پرسپولیس در دهه ۸۰ با یه دختره دوست بوده، افشین قطبی خبر نداشته از رابطه‌شون، قطبی به دختره شماره میده، دختره به مامانی میگه، بعد نیکبخت کثافت‌کاری میکرده و چاق شده بوده میخواستن بهش گیر بدن، این با آتویی که از قطبی گرفته بوده گروکشی میکنه
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101674" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RyfTUKBmqK8Clx2fQueQugKySoW2psDJLzxMpqtghUo1LJjMtU9fozwz9vuc1toC0UKE8m4TnQKAWSM8TsorOAU_IwtyR81CILb_YXOC9gvEtoQmNBiv0CSxvOKvMkpLSdeMSc_sSsX0D7jCmPAQXbHhHLI5mFzkrdn3DfZDsgY25mVJWPaUtypTgMpHKbRF3jDOJVvcULYg3xEyflyYw8NLrZVZrD8WMpyOTkJZpW7Oa1Bp5ozJqA6EimPGGLdw7meeCFatIL1vybP_Jx4DPe1Vyrmy8Kl7t_IusnrItT3EGPbdXDaahMkDYHVfteFB3RYfLviS1eOEhMsmT7B1yhTW4089XtxYVAxIB1B6Jz2hUdyRxPIwzECMw-RwjQfUJEUuNJ3aDtCq5w-Q1EFNPlrZP0O5i589WGBZakLp2IuS6c-5p_lzoRbbRmyj8fatxP5ne4xRKJAG1uMBCDRxrHik6LBOIkjLtLPpRQHzUWgfRils4pq0_4Tn8UkTqjibCs553PcpJGDeeeJscXHGkYyd1h0ykTcu3NXalfoGdMzJz2pgNhCZSTyV3eOEPqIWt_zr0pNU5fS77Qz3N_QBmoeqf21mcgIRBJkQkhIJsR8YCbOs-0nBe_RM5JoL1QT_0AnoT42uIYdhUTwCGOGmUJJu28kqjRxin9JvH3gTXlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RyfTUKBmqK8Clx2fQueQugKySoW2psDJLzxMpqtghUo1LJjMtU9fozwz9vuc1toC0UKE8m4TnQKAWSM8TsorOAU_IwtyR81CILb_YXOC9gvEtoQmNBiv0CSxvOKvMkpLSdeMSc_sSsX0D7jCmPAQXbHhHLI5mFzkrdn3DfZDsgY25mVJWPaUtypTgMpHKbRF3jDOJVvcULYg3xEyflyYw8NLrZVZrD8WMpyOTkJZpW7Oa1Bp5ozJqA6EimPGGLdw7meeCFatIL1vybP_Jx4DPe1Vyrmy8Kl7t_IusnrItT3EGPbdXDaahMkDYHVfteFB3RYfLviS1eOEhMsmT7B1yhTW4089XtxYVAxIB1B6Jz2hUdyRxPIwzECMw-RwjQfUJEUuNJ3aDtCq5w-Q1EFNPlrZP0O5i589WGBZakLp2IuS6c-5p_lzoRbbRmyj8fatxP5ne4xRKJAG1uMBCDRxrHik6LBOIkjLtLPpRQHzUWgfRils4pq0_4Tn8UkTqjibCs553PcpJGDeeeJscXHGkYyd1h0ykTcu3NXalfoGdMzJz2pgNhCZSTyV3eOEPqIWt_zr0pNU5fS77Qz3N_QBmoeqf21mcgIRBJkQkhIJsR8YCbOs-0nBe_RM5JoL1QT_0AnoT42uIYdhUTwCGOGmUJJu28kqjRxin9JvH3gTXlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایت عادل فردوسی پور از الکس فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101673" target="_blank">📅 18:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101672">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB70JOf1odqxzkYOu6FDTPTFHJbWe8mDCQ6pJkRrH6qdMKjF3vFJgzW14N8kMeIZpFw5YIWb8V3twGlrP2Kpg3xreOSqfP2CPECot1HelVNvWGiPb7dZ11VkYgcX3zOlcUTZ5GhXOzmi7w7ClOOADFwVsQXabcK_tMCropmI4pcvDgqZHy9EU4Lf0280AOuL87kjMx-UFj92i9y1RZPeCJNsMCXZ4rh4pTFP3XPUBX83DnsEBZPYv9kBwQVKWEOCKXd1V9uA2nIXqwsmdO2KlZhgPa5YaEgMEP6VNyEqS-PmpPg-2VSCjCvkw31hAjWGiFgapHoPaGpBunSe0r4P7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180
؛ باشگاه نساجی مازندران با ارائه پیشنهادی خواستار جذب محمد خلیفه به صورت قرضی به مدت نیم فصل از استقلال شد. این درخواست از سوی مجتبی‌حسینی به شهاب‌زندی مدیرعامل این تیم منتقل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101672" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815514f088.mp4?token=VXxUUX_kinZ2wdmNjcN694nTBiyonrspYBbogDFIjW-ShBZ9QzHM1q33nrak90xuLBxg39xiOY8wL39b4Vtx7wAO1R3jT6ye6KJ3zzgewmIok6KYWR-q_x6vRzGE4_m1g20SQn-ZSDhxhewkr-VtPBKFIZyVU9hbp8KIWIpZgQgl_0v_q3uV8liaiuiwckcKS3Sw3w0tJeH5YYYVp5HnYLwEgskwMj6qc0DJeAZ_QX_ljgZ1zCOAKbdv8T04A74X6NIMuAmhVg2nnETLhdj9vLjkuwdwtVRgn7ahtOZvIEr_YkdJELuhGT_ZQMoK8UXNuZIHjnHmPrtvPbM2kAcKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815514f088.mp4?token=VXxUUX_kinZ2wdmNjcN694nTBiyonrspYBbogDFIjW-ShBZ9QzHM1q33nrak90xuLBxg39xiOY8wL39b4Vtx7wAO1R3jT6ye6KJ3zzgewmIok6KYWR-q_x6vRzGE4_m1g20SQn-ZSDhxhewkr-VtPBKFIZyVU9hbp8KIWIpZgQgl_0v_q3uV8liaiuiwckcKS3Sw3w0tJeH5YYYVp5HnYLwEgskwMj6qc0DJeAZ_QX_ljgZ1zCOAKbdv8T04A74X6NIMuAmhVg2nnETLhdj9vLjkuwdwtVRgn7ahtOZvIEr_YkdJELuhGT_ZQMoK8UXNuZIHjnHmPrtvPbM2kAcKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مارک کوکوریا موهای بلندش را فقط به خاطر استایلش نگه نداشته است. پسر بزرگ او، «ماتئو»، مبتلا به اوتیسم است و در تشخیص چهره‌ها مشکل دارد. کوکوریا می‌گوید موهای بلندش کمک میکند پسرش هنگام تماشای مسابقه بتواند او را راحت‌تر بین ۲۲ بازیکن پیدا کند. به همین دلیل هم قصد ندارد موهایش را کوتاه کند؛ چون برای پسرش فقط یک مدل مو نیست، بلکه نشانه‌ای است که باعث می‌شود پدرش را گم نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101671" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101668">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ST6eo3B34Xj0ZeqX6Z3tSRbqDchYBiINa-qHASR8aMpOltYsx-9OKR0nD0i2kvw8xmvieaOKmTLXwrfefmHgpdP85m5nFQE8VMeIQgXS1lZuVGbkCTBwSAS64Dgl0YQpVAfWoqN0eEA9xkdhO8B3G80dHz8BD5uVF6mp42QRRs3K_P7UvNVgqzeFaKr140cJI1lJBIg6CKs2Ul-_tYiteRUJ58QKcCsdo-Cdl8lcPS_ApmUJB_bex7T9F1Yrgxd29qYJ217O8hwzUd8O1CfoIoJQ4fDfmwm2EmDCHIad0GVJbf4so-1h4XUmXvEFWKuFFcJVcVSx27Gv1HMN7CA1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1vkkjs21BmP7MfMcuyhV9smh1ODH-wqkd1bziKOL0-Pp5ZP6xSvKdRdsc9Qcanv0joIyy3EIN8GYdaBLxhKKrJIaIcgRGQeAK1vHUPDuAiWfCbekfu08ZaHyy01sBs9DkCA-olyU9ymp_zo9nU2RvbvH-Q6sFbuDUsF7Op2xAbycf_NPvHLRi3I3yIUUT29ebq7b8bZLNczV2WAoYXlZXhX7VqmKttJJZVLnVOJvmUqcvqP_k5LOlQk4HeCJRTZo9s6cv41h2k7G1VajipBagkFPM_10SHzind16vwJOBLmeKA6aXm-ppG4g2vQdDNPYlrkWNAc9C7gnntr5uu4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRrsPW05O3pwcUa82LJIda_m4qdtmLo4Y-wSmfelMnxaMHDajlA35i_8drW5F5zE7LaBDUWtSMiirTHq0xyiJZ5T1Q31gvEs3m10CUE0ioEF1N977Or1FwqmCUO8hykF3vNr8tAfR0dBN6uxKhkke2PetmyziMefOLqW7RIKMPCtGipe6a-1zGfjtpyWbGZr86veFxRcTzhuyEQaeRzW3DEWXgKot2654zUED9KK2OAwPEyPz2XW0KzMeq1jSJEckzXus65btVowV2T-TQXHZUuQFpjWOO8H7hALMtBTne-iVI6tHe4Y9FnZDSUWc3Ms0_GVZbdyVPIOugKivXij7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رونمایی الهلال عربستان از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101668" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101667">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGaeFby7uG2mrVSxh2Vi9NGZf5NOb_CHsP23AMWJqsFpp0Bl6EAVKm1OXp9lnchcuLvm8-HQ33PZLS7Z832YC0liB8JYC3_dq2E2qLozbsSSAjmVhTue4zcsbRbynPsjjG4Wqel4CBxdDzt0gEXNddKSGbe-poL07Uw4d1YtBDdKCqUWoKBm5lh21KMv4r2sqwUfbNXQvUkuoAohf3VQ1_MYz66HfEbbhH09940tJMtoKKRx72sYuV-YL2e3qS94adKcYgdYKmB-NheoNwXG3Bzw_PWWY78O0iuK2fAQiJvUUwMiY1RRV5NJH24ftVFnCIWzL58eKJEzm7Bhk6S4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
جلد نهایی بازی FC27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101667" target="_blank">📅 18:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=h31z2uhBPigjGoLQYEi9zAnAItFRDVlvPc03CsZlBM_Ux5MnRV0yBxYg7IfWnpTpTUGK2xUZl1tmjdrQsytYfkLfaX6U-BR0c_M_q4yo5Ye1zBs84yi5YwldDYtttpP2l5SiaMdALCQlwOjUMqXzRMiQ7SRrXcH_ZSs8l5CymW_Gw4xi2cnk_hzEVcK4XEGHL19Z3FJLeRznfA5jJaDg3l2JlDME2Q0bFIzT7j-6eJP_8qiJVHUX8Hbc8zW4X-ziI0tZFqOxbl9yJwUry0xsCPI8EwWJ56d2Tua_Xc19epYnqd1MjKZvj8oUJ2cJv7uKriY2Wo2NJVqzoRxNyGx4ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=h31z2uhBPigjGoLQYEi9zAnAItFRDVlvPc03CsZlBM_Ux5MnRV0yBxYg7IfWnpTpTUGK2xUZl1tmjdrQsytYfkLfaX6U-BR0c_M_q4yo5Ye1zBs84yi5YwldDYtttpP2l5SiaMdALCQlwOjUMqXzRMiQ7SRrXcH_ZSs8l5CymW_Gw4xi2cnk_hzEVcK4XEGHL19Z3FJLeRznfA5jJaDg3l2JlDME2Q0bFIzT7j-6eJP_8qiJVHUX8Hbc8zW4X-ziI0tZFqOxbl9yJwUry0xsCPI8EwWJ56d2Tua_Xc19epYnqd1MjKZvj8oUJ2cJv7uKriY2Wo2NJVqzoRxNyGx4ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔵
خاطره قایدی از اولین بازی در استقلال: جمله‌ای که بعد چند سال هنوز از ذهن قایدی پاک نشده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101666" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101665">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=kJvFWe3mZCGG68cTqHQ2uFqZMqDQ37LZDHlek1YO5aqW2nrQdKW9Ww7_BpkQAJbJEJlE6Si2sp0ThWHFVSW20p8U3jNCofIR58XL9jX1ISgd_kAvIMpikuw8aUsE5WQnCFcrf9wxawysz5HSLC55q5qyP1VZO_VwP89vwRNfJSjbljm-wTJUpTi7EfdVhfS-Pb9-umSImbl2CUEBobmRgBF4maR5mM5AwsWNvPuAtFvj1WyIzKxC-4B0bnwiqYAR4PI-yfbHiBWF3mOYOLHE3Xa-llRHssXiymloOUv-gmT7rY3s_DSbNRU2iDEBWKT1KHZSXvJW3lm9BjcHAYpyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=kJvFWe3mZCGG68cTqHQ2uFqZMqDQ37LZDHlek1YO5aqW2nrQdKW9Ww7_BpkQAJbJEJlE6Si2sp0ThWHFVSW20p8U3jNCofIR58XL9jX1ISgd_kAvIMpikuw8aUsE5WQnCFcrf9wxawysz5HSLC55q5qyP1VZO_VwP89vwRNfJSjbljm-wTJUpTi7EfdVhfS-Pb9-umSImbl2CUEBobmRgBF4maR5mM5AwsWNvPuAtFvj1WyIzKxC-4B0bnwiqYAR4PI-yfbHiBWF3mOYOLHE3Xa-llRHssXiymloOUv-gmT7rY3s_DSbNRU2iDEBWKT1KHZSXvJW3lm9BjcHAYpyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های چندی‌پیش مهدی‌مهدوی‌کیا اسطوره فوتبال ایران درباره تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101665" target="_blank">📅 17:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101664">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PB6aURjh67VKJhAhNBy9vyaTrFb3BVsUtIe9XkvHlJ1FyUvXKiR-s6qgBYIqRj9OUkl6JcTgd0vPtTYadAeuvKC4Akg-lNny8TiRMkkTOlWmKubcg3thbQdGCSiZrNCDNuiM5F1IgQM1IKe61rE2Hkbkh3I2lIkCw7M9U9X4QirgVQFyOTdl0yaWHyzxwiuomxtGvI29Ndyd_uITtmrsXU4daVd4Yz-3f_WuDlrZ2oDRToXzWudkZ0LaYMDDbKcM2XWEOKpgICko6Mj93D6mj2atqceE6L4gxSWsWxXJK8RSrGhLuNoRCVcq_itl56qHrdyamqq25IxufwSw-s8ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گارناچو رسماً به صورت قرضی با بند خرید اجباری به استون ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101664" target="_blank">📅 17:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUoWVDp1wJ2xdYE1idcnFrBSYzyEvdEL9EQu7JwCxwlyc93YpfbSRPtCFQZ70296OALQB2uBRAI0mDqsP0y-YG-2Gz9lLoKjHryfzLqhCp9RykDMNmt8cE9eLY_sCcdCl1g--XcBrMaVEI-cIk1OK0L4BNqDCx0U_ICMi3Wmo56XNuOPwgj6A1ciYD_eDQO6LjMFIiUjw3xPLaLwGMMaBNakmSMW8i5Rij8pGnh2d1jOOVgw4ARM1azTAruqp4qJzNPi38kscIA-2B0Bw1jXveEW99c8SNv2ZAFVO7678OnjH8tWri22CLFrN38O8t2mLKjwMOdpAHLRwhNvdR9mDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
آمار ۶ مهاجم برتر این‌فصل اروپا:
🇫🇷
دمبله ۲۶ گل‌ و ۱۴ پاس‌گل
🇩🇪
هری‌کین ۷۳ گل و ۸ پاس‌گل
🇪🇸
یامال ۲۵ گل‌ و ۲۰ پاس‌گل
🇩🇪
اولیسه ۲۷ گل‌ و ۳۴ پاس‌گل
🇪🇸
امباپه ۵۶ گل‌ و ۱۳ پاس‌گل ‌
🇫🇷
کوارتسخلیا ۲۳ گل‌و ۱۰پاس‌گل‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101663" target="_blank">📅 17:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101662">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=UrS997TzuZJOYvpAJypwo2CjCsqREHKG1OO6Ho-mJ6zlE-b8FykqPNlCqRGzJPC5F9zLYxzc3LlvbsbBtHJa1mi817NmFSHs9pjUFmhp3BshXaAoIr4SMZL00GC0DbmG-zeIubRHQZKm1wiFOEen1Z9EacZlE5DmSsj4-_2dAy-em0wW0pSbE_oOwLUISPXOSRwA7fl36XXf7LfZcP3dDubNXnQRqby_uaLuU69HQd5__cME94MSXtlvhSIv0KOLhdAoEw2n7ae2PO4nQrAdqQKWbSIelrysuY8ZvIV3ONiEzMaIwOdKdkcO7uT0zR5jYmrTo86Su0CEc21uvDvrVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=UrS997TzuZJOYvpAJypwo2CjCsqREHKG1OO6Ho-mJ6zlE-b8FykqPNlCqRGzJPC5F9zLYxzc3LlvbsbBtHJa1mi817NmFSHs9pjUFmhp3BshXaAoIr4SMZL00GC0DbmG-zeIubRHQZKm1wiFOEen1Z9EacZlE5DmSsj4-_2dAy-em0wW0pSbE_oOwLUISPXOSRwA7fl36XXf7LfZcP3dDubNXnQRqby_uaLuU69HQd5__cME94MSXtlvhSIv0KOLhdAoEw2n7ae2PO4nQrAdqQKWbSIelrysuY8ZvIV3ONiEzMaIwOdKdkcO7uT0zR5jYmrTo86Su0CEc21uvDvrVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمایت سید جلال و قیاسی از علی دایی و کنایه‌شان به بیرانوند: بعضی‌ها اصلا نمیدونن احترام چیه، هیچی دیگه سَر جاش نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101662" target="_blank">📅 16:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101661">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=DSE3HdPOFMH0eypkvXK3igm_Wvs1UUa43lnv464WxEMPIsQaODGRxcrMKR2H27gEmQEiyPiQN_zZkwN2rYQleRWxWjU1a3dMI3mgrFy44itNXRjM_2IuNV7dDaX8EURXVH9im8yUnwLQACZ8Xd7hGUC9mTybEUtg5DuCGmHfGVeXyN3I1FRZxpahDl6KwOT3rMQzwoKjeuLNv2kK4ZSt6D2qRyX9lYVWHl1mOSdyCtk8_F7gqzzH_Cv95cBYvWwOWZt5YgT0zY_X72EVN5dEU-TWfYIEfyevX9WqoX381qjqNSOjseshBKWQCjbDY1i7m9FFna4gayYLM1Pq3GpNPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=DSE3HdPOFMH0eypkvXK3igm_Wvs1UUa43lnv464WxEMPIsQaODGRxcrMKR2H27gEmQEiyPiQN_zZkwN2rYQleRWxWjU1a3dMI3mgrFy44itNXRjM_2IuNV7dDaX8EURXVH9im8yUnwLQACZ8Xd7hGUC9mTybEUtg5DuCGmHfGVeXyN3I1FRZxpahDl6KwOT3rMQzwoKjeuLNv2kK4ZSt6D2qRyX9lYVWHl1mOSdyCtk8_F7gqzzH_Cv95cBYvWwOWZt5YgT0zY_X72EVN5dEU-TWfYIEfyevX9WqoX381qjqNSOjseshBKWQCjbDY1i7m9FFna4gayYLM1Pq3GpNPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⛔️
نگرش متفاوت دو سرمربی؛ یکی شکست را پذیرفته و با قبول واقعیت به فکر آینده‌ست؛ دیگری زمین و زمان را بابت عدم صعود از گروه در جام‌جهانی ۴٨ تیمی مقصر می‌داند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101661" target="_blank">📅 16:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=McoEZ5_BQRDembH1ZNyXeV5lEngGZp1x5N2B1-YYGYMudDA2qLjlEW28lnYFScAZ1DooPgcsb_nr2F22yDoYW3LqTmLTdFiCmpSbWCHxbSf0PAiAalVcsqj92FoNLOVZ-LRo6DOEpKq8co2FIloUqHA1Vj-viUQBpUVJWF3LEar3aMjPgH4uBTdBUx8vPddqpkz10U_rTlFCnQaPBMsSxCkK7CR8LCfnJOf_8RdHhECrCfL8lxtWnIqBHC3rtWneQOizXi-kCIr7e0HxH7Yxuuh3g1JYp0fCa7PoZN8oqrB39rrbTIqKTdAWuxoymmxz-T5ZfqtatYlibzznQjvzKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=McoEZ5_BQRDembH1ZNyXeV5lEngGZp1x5N2B1-YYGYMudDA2qLjlEW28lnYFScAZ1DooPgcsb_nr2F22yDoYW3LqTmLTdFiCmpSbWCHxbSf0PAiAalVcsqj92FoNLOVZ-LRo6DOEpKq8co2FIloUqHA1Vj-viUQBpUVJWF3LEar3aMjPgH4uBTdBUx8vPddqpkz10U_rTlFCnQaPBMsSxCkK7CR8LCfnJOf_8RdHhECrCfL8lxtWnIqBHC3rtWneQOizXi-kCIr7e0HxH7Yxuuh3g1JYp0fCa7PoZN8oqrB39rrbTIqKTdAWuxoymmxz-T5ZfqtatYlibzznQjvzKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مهدی‌قایدی: حسرت خیلی زیادی دارم که چرا بهم در جام‌جهانی بازی نرسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101660" target="_blank">📅 16:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101659" target="_blank">📅 15:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=pDg6-wT3h_hqXaXduX-EgTvruowFfNu7IJVbklCPhendsL4OktX6XRBIWscmXMvNP2o4eEk9Hvs21ST-lO-K2OLazh_viNnGPxZ2ZHmtd2QzYy1snKRoJVMw0k7OYNTXerQ8wuPQcwO_oncOJZ3stLlzfUU6_rlooSSpMjhsWGe12F72hD9XAUocgrmUbuDJvaUx0vBOchMfQPqCWqjALf-J6Y5mBYxUEPwfzTGVio7y4Hx78BWx9K3u49WbOAT1xdc3p0RzIyjiKGmWU0D-wb5sI-Z53kksZPU6_TJYqxKZERay3265Kxo2jQOsYcMKoovig7t63I3CB-Xf9tIwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=pDg6-wT3h_hqXaXduX-EgTvruowFfNu7IJVbklCPhendsL4OktX6XRBIWscmXMvNP2o4eEk9Hvs21ST-lO-K2OLazh_viNnGPxZ2ZHmtd2QzYy1snKRoJVMw0k7OYNTXerQ8wuPQcwO_oncOJZ3stLlzfUU6_rlooSSpMjhsWGe12F72hD9XAUocgrmUbuDJvaUx0vBOchMfQPqCWqjALf-J6Y5mBYxUEPwfzTGVio7y4Hx78BWx9K3u49WbOAT1xdc3p0RzIyjiKGmWU0D-wb5sI-Z53kksZPU6_TJYqxKZERay3265Kxo2jQOsYcMKoovig7t63I3CB-Xf9tIwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجراى مريم اميرجلالى و حميد لولايى در بين ٢ نيمه جام جهانی‌سمه خالص
🤣
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101658" target="_blank">📅 15:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔥
▶️
چند سوپرسیو دروازه‌بان در فصول‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101657" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❗️
علی‌قلی‌زاده: امیر‌ عابدزاده استعداد بی‌نظیری در نوشتن و رپ داره؛ از او خیلی چیزها یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101656" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEXta4jOvFS0jlo8G5qtenvAOSz1qbROLwkgaHVUi9u_Y5fnlOzhZt63E0x_MNUgxnaH1OI9HcYgS8k_rbYdQXapwCi1pPYzh0qqBnTxxanODtl6tl_Fc0GXuR97k4WOGF4MW_CHy2yT1ithKLnItzJLP5Nu5mpypUopM8E6NXoiB6-a6BKXJDphBwa1q1Q6qpua3zjEq0Jc22qeBSCVW3-bUyvtNAkDBwNj0VFHRluGR6OVoeBfKGxzT85zrfxhK-3BhRPQAotr2Cu80t0mc6-mvWiIQKq5z1TvP7ZZb23gAEytyUff0D8gs2NMBxmmOwav47yWZWPx6B3_8xqeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت گاوی زیر پست یامال
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101655" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ینی چه بلایی سر اون تیم پرانگیزه اومده بود؟! ببینید قبل از بازی با فرانسه همگی بمب انرژی و انگیزه بودن ولی تو فینال امسال انگار همگی از مراسم ختم اومده بودن.
بازیکنان تیم آرژانتین تو بازی انگلیس داشتن به معنای واقعی کلمه میجنگیدن و بعد از بازی مثل دیوونه ها جشن گرفتن اما یهو نمیدونم چی شده بود که اونا از لحظه شروع فینال هیچ تلاشی برای بردن نکردن!
بحث تئوری توطئه نیست و هیچ خدشه ای به قهرمانی شایسته اسپانیا وارد نمیکنم اما مطمئنم تو رختکن یه خبر بد یا یه اتفاق ناگوار برای آرژانتین افتاده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101654" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=GKgzqka4zAmt4kQ2f2VkNIg-uqpUvgWn_yyNWzzW1o0ngjz_yJRLXIPMEO9U2e5j_w75dFAVCfc5NaMaiEryeM25pT3jsGeYca3DQ5-tUjCdMlw-MLALC02ISWI9tHi0NyiGrIh9pLiVOjcvhwMrJKe_W9uO9vYN1LPDgP8NGft3QMqFEfwb0JScLM1xGCCalry-_BVZgMdJVXThTnbZZp2ybotQM2QLAzTBi3CBEQntju-b9f9NlJs6R5tNmJxJaK5WGygOgssVTzjf2w5lOyp8SBSoVanpk3vNQU60S-piqLWoYR18tNqn_QKptu3U8_1WJmLAsBR-uat3HgndLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=GKgzqka4zAmt4kQ2f2VkNIg-uqpUvgWn_yyNWzzW1o0ngjz_yJRLXIPMEO9U2e5j_w75dFAVCfc5NaMaiEryeM25pT3jsGeYca3DQ5-tUjCdMlw-MLALC02ISWI9tHi0NyiGrIh9pLiVOjcvhwMrJKe_W9uO9vYN1LPDgP8NGft3QMqFEfwb0JScLM1xGCCalry-_BVZgMdJVXThTnbZZp2ybotQM2QLAzTBi3CBEQntju-b9f9NlJs6R5tNmJxJaK5WGygOgssVTzjf2w5lOyp8SBSoVanpk3vNQU60S-piqLWoYR18tNqn_QKptu3U8_1WJmLAsBR-uat3HgndLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رضا جاودانی در جواب نگرانی عادل فردوسی‌پور، به جای فکر کردن به خودش، با آرامش گفت: «بذار بیکار بشم... مهم نیست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101653" target="_blank">📅 14:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=sICydQOO5cVaECNUgbqIj7ncQt7112iwEnVaJwEgV638kvPwf4sK3kpbrq-kohukodmjjTJHrOvQ3UJG1ZE-_ca8IsqoaScz-pNA56E2w1wZBl20E_-6J1wQ-unvv-JhBPYqYNw71JgZzYAXRGeBHrBvJrWkb_JS0cENCst-x0HkisT1hqJy4_3mmQfx_x-wxiYPpEIA_KGa3E8cL1iAOn5rE-GZCP0uasBHC8cxzLofA1K0ir4yXjfO_w9Axpj8hLA7LQQ3Toh3QfVB_9MCZRpDPvghCCS8EccY_K26tJNG_bQSMRwXNnIknoHqgG11JPaYPCRTzd11qp8A6K7cTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=sICydQOO5cVaECNUgbqIj7ncQt7112iwEnVaJwEgV638kvPwf4sK3kpbrq-kohukodmjjTJHrOvQ3UJG1ZE-_ca8IsqoaScz-pNA56E2w1wZBl20E_-6J1wQ-unvv-JhBPYqYNw71JgZzYAXRGeBHrBvJrWkb_JS0cENCst-x0HkisT1hqJy4_3mmQfx_x-wxiYPpEIA_KGa3E8cL1iAOn5rE-GZCP0uasBHC8cxzLofA1K0ir4yXjfO_w9Axpj8hLA7LQQ3Toh3QfVB_9MCZRpDPvghCCS8EccY_K26tJNG_bQSMRwXNnIknoHqgG11JPaYPCRTzd11qp8A6K7cTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
شیروانی، مافیا ایرانی فوتبال ایتالیا: به اینزاگی گفتم طارمی را جذب کن، اما طارمی در اینتر جواب نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101652" target="_blank">📅 14:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxg6-eUGn7x1rflQlMmMP5_EvvWdqBLfhpKpf91FB9bXzmJhR0O0ny8n6CfJYMdC4ejeazW5-d2srtAOqfCrYZGGYF2F19-ifY0VakzHuD5dIouCmuSY8SAAvnbmPpGD7qtOmkHM2Ck0fUJRrWP9gHehuoo0jg3htxLMAZeewPZEGAlWTKwqNyWw0RB-aP8xpwoxmqTOih4HgqsRMTlC8eeQQDMDkL1s-fz7-vjvDo_SyMqoerT05fJa49_YDJzkHZ_2b1VjunELmpOX_0-ZQsdPcqZxyXW2pTeHGn_M2AYkfB-BpT7_iea94BjgJSCn1pG23CvpqkI2GgtisRRVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101651" target="_blank">📅 14:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101650">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=RHLffNks4NSwJq8Uh08sLfREwTYdNZ9YL9rK7Yabqx26ns-4ENsnQXSdp9nmoGQYaouv7La-ywTmx-hXLtc9TLX2Lzick_7183tR5iavC3jQzCgQiW1sH4wQIp3396xKRWOgE6o53AL6ACUwHMmkA0--L6tP7XUZP5G0kzIkQKODNbUUyJS93IgFJvDFFY5Jwl1mt8AEM07GPSvRmBZ7qiVaq9vNdnRI-ETiQmoSD-Dc_8dAjT99gmQfCDisrUc7d6e9oczsnCArF8AztX9Q4M4Y2ZOVBzIh_YcUKHv4YzLUA8hA8l6oCaUW7T2Ygf3y-iik6b9SDiJqzDwQ0ScePw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=RHLffNks4NSwJq8Uh08sLfREwTYdNZ9YL9rK7Yabqx26ns-4ENsnQXSdp9nmoGQYaouv7La-ywTmx-hXLtc9TLX2Lzick_7183tR5iavC3jQzCgQiW1sH4wQIp3396xKRWOgE6o53AL6ACUwHMmkA0--L6tP7XUZP5G0kzIkQKODNbUUyJS93IgFJvDFFY5Jwl1mt8AEM07GPSvRmBZ7qiVaq9vNdnRI-ETiQmoSD-Dc_8dAjT99gmQfCDisrUc7d6e9oczsnCArF8AztX9Q4M4Y2ZOVBzIh_YcUKHv4YzLUA8hA8l6oCaUW7T2Ygf3y-iik6b9SDiJqzDwQ0ScePw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد شیروانی از اعضای ایرانی مافیای فوتبال ایتالیا: با دیگو مارادونا رفیق صمیمی بودم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101650" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101649">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upBZPL2xfmD_clXboUDnPXVc3cV_AlrezYImCHaPn7D6_Ck39dYHj7bgETF4e0Eijctsuv5nC6qQf5v0nyjVt91_ViKPQrdQv5MsX7ArZAt0ahPs7SfNqc61g4ydiyCMLyv5GyICeVX5wl7rKhtBha4NABZujQyI0zxkDqyRDxCVkpL32x4XrKDIlmPJQwOYij-3CiieyM4rtvSq9AMB476-m0xgQMo2eJzsE-uxT3wAuabRGF_T7erj-dTe-0DcBiTCzCMpcMY-tY4yXWf1H0Hi9DmWaWNQ3bJcLPsGH7U1Ahe5nIsqMFgjxmYL6dBoTERbhUF4c1dJCHP1uK8gpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
⚽️
#فوووووری
از مارکا: انریکه در روزهای اخیر با فران‌تورس تماس گرفته و پروژه آینده تیمش با حضور این بازیکن رو توضیح داده. قراره تورس نظر نهایی خودش رو بزودی اعلام کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101649" target="_blank">📅 13:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101648">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=oDVqJ3RRcte5oFMyzlb4BeTgbZLd1BQx9dB3t9YHOS-l2-7ssTp-72DxgMXpXyXHT5p-RubXsGo12PaxXwqC_ufAap9-OZ--_GsLaFNmEZ_pcCHI9lB4AHl9Tw8sLz0SQwYxhYbSkYy83t1iaiXfFeUSK3vNTXfR7QokvCR9DbD-CcMvxRKOHAntlTmWVT1KMrkHihoRL-mzni8hYqaqO-6FQa2q6Lj7D90R6pjHm8Bmr0GEVoGtx3Dac3oC0940l-_DFUIGXDgW7-WsnqugdOwulswahSZJNXp5v_TT_oRzeERqMQuOGNfUN9yTP8jXVUMZkIe4F7CpnQ5oAuVwPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=oDVqJ3RRcte5oFMyzlb4BeTgbZLd1BQx9dB3t9YHOS-l2-7ssTp-72DxgMXpXyXHT5p-RubXsGo12PaxXwqC_ufAap9-OZ--_GsLaFNmEZ_pcCHI9lB4AHl9Tw8sLz0SQwYxhYbSkYy83t1iaiXfFeUSK3vNTXfR7QokvCR9DbD-CcMvxRKOHAntlTmWVT1KMrkHihoRL-mzni8hYqaqO-6FQa2q6Lj7D90R6pjHm8Bmr0GEVoGtx3Dac3oC0940l-_DFUIGXDgW7-WsnqugdOwulswahSZJNXp5v_TT_oRzeERqMQuOGNfUN9yTP8jXVUMZkIe4F7CpnQ5oAuVwPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیدجلال‌حسینی: بدترین خاطره دوران فوتبالم بازی معروف با اولسان‌هیوندای کره‌جنوبی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101648" target="_blank">📅 13:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101647">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=IPLORUASjXv0tQs2IQhDch6Tsxd1m8s6H4eSrfXlsauNMq3gjUI3pGCtfpYdUIEQVGQZ38AMYAQeiAR26vz0bxX1sA1xx3ztlCNU-Zst61q0kQceOuXMfFyJZUPusSGMgR1muDMQh5vjR-7utOKl7Juce3DVzJgnv2YhnR9arzSUDJFIsSfoLhprr2EDAJGaFXwPiutU4aY6LsQB2iwiKb3KMqjEsNxbSvcd6meZaxSgd47frMIU36k-XF2821iWU9LUiek-u2-Vd8XZ-wK68WplsHQLCtAue4By-E_1CFUASeX90N04A8zlDgXOSn3dMm_DWZxrUDS9VeRO7g5Q8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=IPLORUASjXv0tQs2IQhDch6Tsxd1m8s6H4eSrfXlsauNMq3gjUI3pGCtfpYdUIEQVGQZ38AMYAQeiAR26vz0bxX1sA1xx3ztlCNU-Zst61q0kQceOuXMfFyJZUPusSGMgR1muDMQh5vjR-7utOKl7Juce3DVzJgnv2YhnR9arzSUDJFIsSfoLhprr2EDAJGaFXwPiutU4aY6LsQB2iwiKb3KMqjEsNxbSvcd6meZaxSgd47frMIU36k-XF2821iWU9LUiek-u2-Vd8XZ-wK68WplsHQLCtAue4By-E_1CFUASeX90N04A8zlDgXOSn3dMm_DWZxrUDS9VeRO7g5Q8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101647" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=d4sQ5mc_QkOqHnrhJEd2ET1BU4IlIRXxxodh6EAkbSTKJydnHLmYSnVIobV4nxY66_bOzbWcNd-eKFFnMq8OJoeu1xPENLStPSYrrer9-0rRccYhMokECu3Ypa60BTM3IMusI_zBHdgKLy0NecYiPF9XM3tCc0obSko0F1ygtO0uqacJhbj8C8cS7qjSfONMFUiboD_ai0uNx-HX2m1OzDjLR3hMnbZJsF3RqDflTCvogi49X6zwPvEX9TzAZcTcRPDBjdCLu-P3GWVzMs1P0bSM1r08Kp9N-OJl2aY1wURksN7Y7P7r_tiZx9A7H8s7XriuC_0pMp41OaNT4DWpdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=d4sQ5mc_QkOqHnrhJEd2ET1BU4IlIRXxxodh6EAkbSTKJydnHLmYSnVIobV4nxY66_bOzbWcNd-eKFFnMq8OJoeu1xPENLStPSYrrer9-0rRccYhMokECu3Ypa60BTM3IMusI_zBHdgKLy0NecYiPF9XM3tCc0obSko0F1ygtO0uqacJhbj8C8cS7qjSfONMFUiboD_ai0uNx-HX2m1OzDjLR3hMnbZJsF3RqDflTCvogi49X6zwPvEX9TzAZcTcRPDBjdCLu-P3GWVzMs1P0bSM1r08Kp9N-OJl2aY1wURksN7Y7P7r_tiZx9A7H8s7XriuC_0pMp41OaNT4DWpdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یادی‌کنیم از دوران درخشان سادیو‌مانه سنگالی در ایام حضورش در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101646" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101645">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCzhMXnrcdpJCG0FaLbSnYUYLcDmQU81Sj9F4a39hTboBGvPzFE37YlcGnAKI0thqWRmzeVWC1m_SG9GqEF-P81-P2TVX_QamY2IqoYEwVBxlaXc6OplZwRlBPzIAe1RF4yh5ZXqvRYP18sxk_gBVry9TG_uxBPqszwFgIQZMREL_VM4fgTxc0W-kldrVKFcur3sDRrslfhbBAbi8tAE9sjwKisuNaIbUqjKBsA4EhnJAmOMEVSs5lgt9Q7iVfDxdmlzJ6fJ2_3TQpCThHlvHqFCYyhM0Zbces2IDvR_rCCGXPfpeA8GtEPxPHJtHNZTSyAp5jYJoZFplKY_4NyAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101645" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101644">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFQgYqNwnghqkJYuWsWBXAYjY39Q171UWegY0PzI_9oA7fj7OtPVvVt0o1dtDMiDuyog2C8gVphSQLFhxIqhiR38LiQPKR1oiAwz_YsV-ObP4d2JInqg61DM3Ud3JsVdpukU41J5q-H3CKQnwK4X84hvKtmx62xhoV0Nqxa_RQftiuh8I93u0hi41aV8rOkD755xHSl6Wa-2evokki01pJUT6M4_wEPcbLyrKvJGrEQSYwM9gbXWf_4afWEQhuylcpe-vh3qn-XRaJWv9-KFCZIjOi1D7NkQCcwLs53BgFtsR5fa2_x708iD9t2oKgH5NRl-YY7YksFXHoG2wPiVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101644" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101643">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2GTnpI7ZD6Z8gPxl4C3-sZiqaCaNiGl1e_TMRqEy1sC016w37SX_oijS3VgQhi8w1Dku8-ekVi8BVMbwE_E1PWIdONO6ROAiO0aP3GSwLwj1W9Rp5WUIUVLP7-KltqnDSVIjTFg85XunnmgqC5zjI_MqGNYm2V2mwGzoJCzEhsBXIr46X3RrSDOVWcSIG21OzsW64Alkoq5b5ajeAgaelYCOqrxwac-yKBO7qhoOs8ANuCNm4LB-0KV2Q2v10fXjw_gComlnYdtckSjq7j1Qj8hqs9qIkcvApiizrIkmeZJ-8Q1kPLPCXNWgx6Kz-ipb_g6BAQeqdcbFrmw3MxftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101643" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101642">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c46077059.mp4?token=qqCV741SSpo_1eMtL5mR_IVaGPqk8PpAse3lVB538--ZS42YTFkLFnJOblCtnvd8FOcY2HQOh3NFpPiZCnzgwAoZItU8oC5djEGDoO0-RiWVP5rDxfwMBelg30cmxlPJ9fRs7sk-MTHhdNmUv1Zcdjia6tcPInkbqlT7LJHBaLLdhHVwnlzifbECGIJtKRNoH6X5Khiy2H3zUGLeEjDpQPIAZMXxx3LeiJlfpjlm5mW01jc-RNbPeb7R-pprGZvyBYOS5NhughR5xluuR-B6zxwgYYp0jAgzUgfEDvZp1RRDtDHjJLoVJYCiWKYhbnkmuwdF_b3lh-msDc0ukzSuHVHk8LY6-FGYZ_XKdyfw5AjrMRRStXjiOOAjWx4BooucEcFGkYCoqGp3IhKCqvj-rag3RNVPeEyCD5lTDtp2SzkX-6l45ZWi4ZfwUnlNXp8qVv-QwT-JsXJK8BVVGEeLhCjOEwhwaU-O5HwBGdYx0NQRbA1JhINS9j-7lqe4dGqzgpEO9sNZLf_UhJcc3cWoWYBen2xixc69UZCmhoj5BoWyDu86cftWp-_hTSUv_mjeZubotrv-TjDZVTi5Hs8_KMUcVhrfaVx7dHns_OkSOh-skpj5llpaP-YEgQ80pERLfifn8wV9-SgLmWx5wqSKvIghFDDei3VFzMRX6Kk7o_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c46077059.mp4?token=qqCV741SSpo_1eMtL5mR_IVaGPqk8PpAse3lVB538--ZS42YTFkLFnJOblCtnvd8FOcY2HQOh3NFpPiZCnzgwAoZItU8oC5djEGDoO0-RiWVP5rDxfwMBelg30cmxlPJ9fRs7sk-MTHhdNmUv1Zcdjia6tcPInkbqlT7LJHBaLLdhHVwnlzifbECGIJtKRNoH6X5Khiy2H3zUGLeEjDpQPIAZMXxx3LeiJlfpjlm5mW01jc-RNbPeb7R-pprGZvyBYOS5NhughR5xluuR-B6zxwgYYp0jAgzUgfEDvZp1RRDtDHjJLoVJYCiWKYhbnkmuwdF_b3lh-msDc0ukzSuHVHk8LY6-FGYZ_XKdyfw5AjrMRRStXjiOOAjWx4BooucEcFGkYCoqGp3IhKCqvj-rag3RNVPeEyCD5lTDtp2SzkX-6l45ZWi4ZfwUnlNXp8qVv-QwT-JsXJK8BVVGEeLhCjOEwhwaU-O5HwBGdYx0NQRbA1JhINS9j-7lqe4dGqzgpEO9sNZLf_UhJcc3cWoWYBen2xixc69UZCmhoj5BoWyDu86cftWp-_hTSUv_mjeZubotrv-TjDZVTi5Hs8_KMUcVhrfaVx7dHns_OkSOh-skpj5llpaP-YEgQ80pERLfifn8wV9-SgLmWx5wqSKvIghFDDei3VFzMRX6Kk7o_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
هنر استپ‌ و گلزنی از برخی ستارگان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101642" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101641">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU9J0Eyuc1CS-DBur6eVnwEqg_N4Aq0n302nNhPDZ8lEhJ8gLOukbX35wb1vsTuI7TmzOUbLvBOL4_aUgHVaO2RUgUGh-n4dE8aCe7I9X65JlmfpRrNg5rNQWFnBSACQ_GM4R7T14Fedi1r6LwNdzT0U3esHdu3hVly8xWH_4VaXiEjvGKLW5okw7NCovzmTtVtdrhr6wFLSYCtm26gftHSVnJla2dGJU520N7BN9GMq148UfLmUqxxH15nOQS9lcdv6FNNYRmCLqk-sCP6G86TPxITTp5tYNCQrpnA00lF8PJj9VBjfyIilvuVRl8eQAp2GHpg6CPu_aT_C2XeRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
باشگاه بارسلونا در صورت عدم جذب آلوارز، داروین نونیز مهاجم الهلال را زیر نظر دارد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101641" target="_blank">📅 12:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101640">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqDPdcSb6BpClt85IbgQNSYwotGFMrZrwPYlvLagvsb5dMutdzZ7DBP4vR-g6veCOtbXqKAfINN0vrS2nZc_uoYqRxof5NsKslDrdo9_7M1t42YajlqcFzPV7njSX5bFEW54SvwRmsKJPai8zt2ECVGTtq6wauglP5IQ3Lef132JuhH3DLjkrRURxtFOmSWl-mXRgzuL2nyz4K6BatZkYL8tmGR6gxNSVBFoO4CpP7KTee5x2LuE6f_6a5qZE5piEchxKkqtMtaSt1677mtZPBUpQiryB9AFrOhOD5dzDTr29ad9QPtuATTeKRXzuaL_tRdpJ61vleQ5ZpntVegxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101640" target="_blank">📅 12:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101639">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=fSo6NipkgwDZWeIYIZsOLdSjEFhdhNrobVJkHIeWAwwA-a960P-YfCBcFsLRYAp_uYCjFcvwZsMy17xITT4q-9-kkaaZfpjfV5RnEjqjF_hmipPS20QQ9HbVDhHzc9W4P4H_H_tP5fyRme0m78P0l4gzRd2otcpUxutS5v223WVk3kXWE9_sHGrHDnX1RVbr_Ij0DRM3IC50l-6l2AXZHOuVBc74tecMfYBKkxiGZh-eGf3tt3LONUGKKIIbkxCr79UeN81Gjah24LXJf_OF_uL6iMJiHNxgljH4NNn74VMyTv0X8aL9YH2NIK3BIN-tSS0Rn3G5bnEFVb20ff7qSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=fSo6NipkgwDZWeIYIZsOLdSjEFhdhNrobVJkHIeWAwwA-a960P-YfCBcFsLRYAp_uYCjFcvwZsMy17xITT4q-9-kkaaZfpjfV5RnEjqjF_hmipPS20QQ9HbVDhHzc9W4P4H_H_tP5fyRme0m78P0l4gzRd2otcpUxutS5v223WVk3kXWE9_sHGrHDnX1RVbr_Ij0DRM3IC50l-6l2AXZHOuVBc74tecMfYBKkxiGZh-eGf3tt3LONUGKKIIbkxCr79UeN81Gjah24LXJf_OF_uL6iMJiHNxgljH4NNn74VMyTv0X8aL9YH2NIK3BIN-tSS0Rn3G5bnEFVb20ff7qSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سید جلال حسینی: اشتباه کردم همه زندگیم رو برای فوتبال گذاشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101639" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101638">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-6i4Hi1pXvYdw9oGngWMlNuaHLmAxkYUc-Y7Fb2MF1hbouMcIJhTPpjWjLpWrHB-QUIDM6AXpdd9Rv3nXArQAunmFU6GKlpALwa5Rho1kuWfrYKBh4DQDImGaEvs03xOoQs_q_bTJv-ObpDsFCbLagW3VhVpYeLrK_837Wis_Ol5AbKe-xDGYV6nZWGmmGKwmSH3tVba5Ay1t2lR_pfjQngdd4-BUa6x02uL72iC8I9XNFxuc8M1VlGpMjvhQwGvhHz71ZS_PImH-q8n-Qb68uqHaI5dmcwttTB6egc3j7DmasHbu1iV8611Hrl-4pG4gHgOcU7WODMFJuuk6MDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📰
بیلد‌آلمان: آرسنال حاضر است برای جذب دیامانده ستاره ساحل‌عاج مبلغ ۱۰۰ میلیون یورو پرداخت کند اما این بازیکن خواستار حضور در پاری‌سن‌ژرمن شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101638" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101637">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
▶️
عادل و جاودانی؛ دو مجری، دهه‌ها داستان!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101637" target="_blank">📅 12:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101636">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGU5wkGUFGQCcF65gO2c_5i7Djo8y3-hKiiM4btlYX1TdvvwdNi5vrokaOcqqpUcR--WTR3IsdxYI8WdbGs2GIvHGfk1iZIHTrrMzJHAd0Z5Xepf7KKkVXLMlhiliMpvrNe6l_mEL9SHRfVlerozmwAUXyFVQOGXcWSteW_R2sD44yssh8gQtw96EScIWejA4bQnR3x1Uld-DwR-y2r_Kw1AlsCYmxwxJaVFlzpfMS3WhgGXED3ITH8NIbzd5WjS6zZyu-LD9aGrRbaRquHj6o6KosOeXzhqXDSvnxIf7erYKmGqug7RKad_DJ9gz4N9w_WQH029-w6BVPFqmlN48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه پس از تعطیلاتش باید به دنبال خانه جدیدی در مونیخ باشد. او از سپتامبر ۲۰۲۴ ویلای ژروم بواتنگ در گرونوالد را اجاره کرده. بواتنگ اکنون می‌خواهد ملک لوکس خود را بفروشد، بنابراین اولیسه باید تا پایان ماه اوت از آنجا نقل مکان کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101636" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101632">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EClPR7Q7XSMM_3uV5fd7dc7IbEEIhdxIECvuKEG4_dSGiYYZXMoqqELZhkdE8_0OmpDdchXa0JLDOX45V6nvgd8S2HAiXmicpVKMmn9peQ09XowsL4i8L1fSu7gtBDAuL9LhhEmMVcjSuMAdCxZ0n3S2rbKqZw5ot3OhFxl9XJQoACfn9sOOyyqHolKm5Y9WzlCJmgYHafXH6_j1rwb3Uh4XBoLtrKZR3lnHOEeyZT9q9xKHYGLmFcYoWwxNlNAZ1Jb68umQmYoKtsbzw13yEfUEB6P6vfGakSarryvo1lRejUttqd1LuWLGQ3U-TpKQbIva7_B1GG6cxKUjT7_v8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsRJPDeZZ-A8L2WgzRXPlIxAUBgKtCnwGK_Z36bCRTLPEEtecWKdSLPlOKQjqAm-s6Co_MDMPh34gZalJbTtSQgFoX35_unk7I5a6yY7N2KfOsLMCsPcywXUg2pbMtOGFZfRkxzUZ9LtJwC96SOXLzgwzLToZOBjjN3Vqafjf-GBdqflK-29zXqPJm6rQ7_X6mx6fnzbQaLPRV1FfVIvrR__TfpmBMqfI6h5ecUgLEf0QeAtFNEXsgvfuZVqacjx5Sjy8Ut-oU1Nf0zN515nh_BLzuqJev0RPeFGUn8xKPPNRVdKSgrryr71NQmVH9bRw2MDO7ZbEcz0u61lvFmaOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMR07-MBuCV_9FmqIpY-mYHozuSDil5p9-VABU1cr1xRuL3mgYc83fSWBac3plCuzIn57vp7CF1UznVolT6AtzfyNzR8h-bLM44saoibVZAnRxIey6F8wqHO6ouDcu3I3RGcrCDDko6dkWPGX7ylUb5JuhSNgj3HZKDh2EQ6Hvq7H59gEY_auxDE4Mr9wTrs4vGznHSoHfHbybI1-CKu80QSZ9WEDDyCCyu_9h6UiQytzucjs5R9I2sz71VrrcdhFqg5Tx73ddRvPybkfy7tbmeIB2TuQo5XYrm6jHczKrHRvC2yLNGFAj2oXqMPOEUKxpxFdQRvMkk77gsOywj6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDlcMV2r57MEE2-325iygbWwYUQlLKOXnMnfJYuspdlOjlbX814n3is6c5n0UMX2JtkGC8s0JatP0UVsf7YkD6pkreRUXWQGH-2nSJ04YeNjDBBER3751Q5wHADmqmhSLT_lj2oCumGl8kbHxvK1oeD91uqSYrKuzZaO-vFF1r4gfTSpXdwgU_xxCvOvNpArSDOp8JddeSPlaHf-TCBG4rj8ZGJwiDyZ9DOS1UiQtxyygT3HcPddA7uv7Dh7eHDw1AIGY21610wWrXth8SWT8l2RlTp6MC_uN50DxKglM1j-M9aPrBwMxLhWbUd7vXVx47heZSWI31Q2-zGO5T3Egg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101632" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101631">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvumdLEn0c9TTQBwB3bwcxzAJMF9PcWUcTfW7d19TpDlTMQ1faXK07s_uCHETCc1azupu1dpgW32O6Ur2y60zW-hUY5y8vYUgyDUHZznQALI4VXE7-bYPUuLeUeY4rgVcLOjkIiT776c_z7Hf6ZIEBTgqzabY8s9maFazZQPRQl7WvC0eqsEMhjwtlitJ_-f4wPrT4Djw5nPNw4JUqwzopPAy_Eqhw_NmriLXD_WQlFdhHLtDowitWQ9gws8R7pziEj9dtpSpsMqsVPXBsqQt_OvDdrzuBlggLXYzLTjamTyqIo7VclBPjHiu1Rdq_dvHDrxGRCEVgPXfHKXsKGrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
هواداران آرژانتین بعد از شکست مقابل اسپانیا در فینال جام جهانی 2026، یک دادخواست برای تکرار بازی فینال راه‌اندازی کرده‌اند. تا امروز بیش از 61 هزار و 500 نفر این درخواست را امضا کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101631" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101630">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvSgG_N-RVGRzuWtb1F1T4lSqtPOsFoRsVGivJUPOQVcWA-Ti4bkJc2mx0Vxq6Nz7_Scyea2ZZSiBNU8sDBqcGaRqu5V6ikOCBiyARUz9I_fFuI28lHeLmswhvft_5qBvLPA9-iqHMtGvkyxxI1H8nZ71S1jgPA0AQWA7fa7w0zTXhqj2scW15GT-_sSaEoz6V9iPu4xOfJYWdUH5iBYNeIpG7ovmziIhPJg_CfEHBD5BEGSsSijZjYPQd1y-ncuIqVcg4xDD-leA-513AxaAK6xi0WR5k8dKuPJLj9nBUVsZy2kC7HhUapXpbt6NbqUyMiaxARfqBNzpkoMZvZjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
❌
لاگاتزتا: پپ‌گواردیولا پیشنهاد تیم‌ملی ایتالیا برای نشستن روی نیمکت را رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101630" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101629">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=s5YOhqowGy1w0GIJRLxt6RULOgfygypa2mOrDHTJYE7dvER_cO7gvxWg1rxn3abFM4vpYNrcla--AUKAgZmHPuF3gK3nuxcccMr1mWysWxsp8jB4m0cQzrEOSHmMhEeRUb17Evkloh01RuwlzBIXzTLejtprwE3RJQ_7XNIDlhSQo579e5RCbi0r31cqpz5ytaV-hHw7OglCJwBzCaE18r1PB49y7dYxEuQIzOnV_qhIl7VNAbZdRPa4N8Eo9zO9v1JqZg-nWRSr7WKg_MnIjlWbcFrQ_hwbFbhCAa_qzOi0HnhLvgirBGmWQIjRxPq0JWGMs_L413kVPqtRwjC0kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=s5YOhqowGy1w0GIJRLxt6RULOgfygypa2mOrDHTJYE7dvER_cO7gvxWg1rxn3abFM4vpYNrcla--AUKAgZmHPuF3gK3nuxcccMr1mWysWxsp8jB4m0cQzrEOSHmMhEeRUb17Evkloh01RuwlzBIXzTLejtprwE3RJQ_7XNIDlhSQo579e5RCbi0r31cqpz5ytaV-hHw7OglCJwBzCaE18r1PB49y7dYxEuQIzOnV_qhIl7VNAbZdRPa4N8Eo9zO9v1JqZg-nWRSr7WKg_MnIjlWbcFrQ_hwbFbhCAa_qzOi0HnhLvgirBGmWQIjRxPq0JWGMs_L413kVPqtRwjC0kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📊
▶️
آنالیز‌بازی رودری ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101629" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101628">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjJR7yTwKo1gNcYjlKI3vp-1-IdH5Vr6BDwR1DP060DG5wf2_CWfyYkIhOqiodEBxTaZJ1V9j9sYTisaAHdBnH_9fW-dMZ7_LDWWurprKs8NzyMQD_AU-eutcbzzxy0V1fITN_4LTiq1W0smrhqvfI4pCjO0xYUHhc8qDJX4D0atZm56FPmaVRN7gut9V6-xOLFZu1yaQ5R3F9hrrOCcKjolVVotzED7kLXSflpQWn1LdXHmm3i7BCsAz3iJSwy6u26jQl_LPpang4F12wAolCMu63gw9XB3Xp2bnLnUBYStoJmMieZoBKHelCrVsxwO2aFAiwTUIWqGlq4YDd_saQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🇦🇷
اسکواد احتمالی آرژانتین در جام‌جهانی بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101628" target="_blank">📅 11:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101627">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVMm45Td3seRuxcPD31JtsfnhZvZhfHT7u-BN3MSnCof1s6y_2Epebm42UssVVHOBPiOXZaPQnzV9qWzuaAIdiHyINUvW-jRuzm4XJboXCioZQbkPQtpDAgropOVfUD_439DZFeN9MN7GxQH_ZshEgTO_HB-cU7BA-fSaosJBf4Btpfg7r91k59lNC_7eB7XkUKEYSjlnD9uPmVUVPIDjVx-fFNnD-E5zTFeOpMwqgDs5yNbDGcSs2yp6uMvBEkocEylMoNkdSwbfiVhoBHNuew0JMTdA9fnB4plW700pd_06cvh0gExIQCeQoJ0Vv70eekAcLc-cOWifHwAMHekMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ نیمار بعد حذف برزیل از جام خیلی افسرده بنظر میرسه
- نیمار :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101627" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101626">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzxNwaeVxthyEmaQ9dlArWpJqJaU5PXnL-xGJ0Swo5jmV7SdjVlgCFP0_nZtbzbjbJ26fX1uMX70groZNVhSt5DAxcMcpsABcgs-efvde6eVsd9kdQLpFdDkOk9V2dj3d-Pc_cbctmJsD3e-ojAij__L6yxhaQ31pO9KwfORBCuQBZlpjVTpspGcu_Ic7dDxnbDF5FLUp-aXItCz0xxlEtLqF24fQSJc29Xg38D7O1A8O6fkwahRrx0MSYQs4KGJ5_Z_rlmNjmYBwSmCE-Wjhg46uDYd3VxNC2Xxxai7DIC5JGQoAzyaWzfaTU8eNoTUttZsYfLlXiINIBq7kSu5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101626" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101625">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbiC8DsbCHyIqRtmYMcHRmhWnegsIKEMc3fnb8dLmfmeBUHEdzbOGJAUPcw3KxI4a9WlJR2OashzbXTLndRq-43iWSjqZHczZbFkfWnurBbyERx4UTKP9HjuTQsu8sX0A9xDi0xu0NHnS2Aw8sHqiM919ZT-aSqvJX8p6QzJ7oV6vvWS0yLDAK6Wv8xCu1o_k9wAzayn-Lc2vIpzE9oy06j90x9lFq_ZXunvxfDeftbNnQh9ITbwoPRMc4wAnTmEuLyVR7yEdYo3a1KHPXuSl2H7353fB9grMv9rPB7LZFpZhyCBtNtHGhtFI0N4FGiwTWHyyRFrlZPSwMLeYp-5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لکیپ: انریکه و پاریس تا 2030 برای تمدید قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101625" target="_blank">📅 10:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101624">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=f9ncuMppB7EGgLgW6_0bf_Rrto_snx-E4RqgGNsT1Lc6PV5Agyn1YD4PiqElFBMp4-kr6-8V9Qpy0v7bB3Z4CdGGFu6fPf7ZyrNYPu15mh80-m9szbAZw3QHtXfflByemtlVClMXiRJEmzQLIBSSYDbvqV5G0uW3SApcHGeCambgA_Mq-sjPYw4vWs8p6ckIQYEgHhiB7vR8jnzMg4TjQCqCPnLiZANC36mv_5duF-9ao2wCv5O_GVMJ9niWNbg8WSni-ndVj4qAnUKEV357SX4-uz-ak4hdkIUUhcfF3BTNqYAdY1FGo_wbs7QdPM47tQZly-3dPaVexNW0SfLm8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=f9ncuMppB7EGgLgW6_0bf_Rrto_snx-E4RqgGNsT1Lc6PV5Agyn1YD4PiqElFBMp4-kr6-8V9Qpy0v7bB3Z4CdGGFu6fPf7ZyrNYPu15mh80-m9szbAZw3QHtXfflByemtlVClMXiRJEmzQLIBSSYDbvqV5G0uW3SApcHGeCambgA_Mq-sjPYw4vWs8p6ckIQYEgHhiB7vR8jnzMg4TjQCqCPnLiZANC36mv_5duF-9ao2wCv5O_GVMJ9niWNbg8WSni-ndVj4qAnUKEV357SX4-uz-ak4hdkIUUhcfF3BTNqYAdY1FGo_wbs7QdPM47tQZly-3dPaVexNW0SfLm8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سید جلال: حسین‌ماهینی واقعا بازیکن‌نفهمی بود. همیشه منو عصبی میکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101624" target="_blank">📅 10:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101623">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509c49999b.mp4?token=MWUIdnEggVHWU8XBJ2Y-Okz0vcWzSyStJasLq1nj4EaWhZggmCK8ygdDzzUHmwPcAoJ4NfsA-YoG2M-IoxPBUCS5tckwBkATdquGaMPM9nfDF-Gq3k-8sBq63-dMdguD8yXe31htuIA1qSZbL_Be-fk5ua-eiy13gyRG59K8OJtHq4aZv0ccj1d9pD-YPE5uQcAOs3iRNpLSEnTCb8HioKgpu0e-0wvjuG0dWwbQ0bB5DvMKpLf9QCE8PXYQSdOyHen3098vIxhBUQIj8vMTrelbLMT3WhDpR7FNC5RactH-68_-Mw_4fjZU_WDUJjLFRYI3I_Tls1mOhIi6whRGHBrT8ejFrUS50_G5iQUL8z9dVNK4HdrbFZJh4Q-t_6E1C8NAm4ZXXTI4HwBRZV3O99jupYdJEW1O6TO6kN1On5DUp1BgWjTEsTr9oDxNxWtN9OxteWALhigxPYTCVh9jj4mTdo6X9jz-PXqufRXb3uQ9WMR51DZ057GkVuqNz351prmnvxVqp3dG6EYxkFx8Gd8cptNMEQq6oxuvCKABckp6J-pTTr346UrBePhBBfwCCnlYxWNnVf-74FcPeZTmnccal5vYgBLTz_M39HLivE3cd3fVG4eNQ1M2mlPVAPjWelTnsUi-RCQcWn_Jghy-TbCK_lnRZdjzk9lIGzAy-HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509c49999b.mp4?token=MWUIdnEggVHWU8XBJ2Y-Okz0vcWzSyStJasLq1nj4EaWhZggmCK8ygdDzzUHmwPcAoJ4NfsA-YoG2M-IoxPBUCS5tckwBkATdquGaMPM9nfDF-Gq3k-8sBq63-dMdguD8yXe31htuIA1qSZbL_Be-fk5ua-eiy13gyRG59K8OJtHq4aZv0ccj1d9pD-YPE5uQcAOs3iRNpLSEnTCb8HioKgpu0e-0wvjuG0dWwbQ0bB5DvMKpLf9QCE8PXYQSdOyHen3098vIxhBUQIj8vMTrelbLMT3WhDpR7FNC5RactH-68_-Mw_4fjZU_WDUJjLFRYI3I_Tls1mOhIi6whRGHBrT8ejFrUS50_G5iQUL8z9dVNK4HdrbFZJh4Q-t_6E1C8NAm4ZXXTI4HwBRZV3O99jupYdJEW1O6TO6kN1On5DUp1BgWjTEsTr9oDxNxWtN9OxteWALhigxPYTCVh9jj4mTdo6X9jz-PXqufRXb3uQ9WMR51DZ057GkVuqNz351prmnvxVqp3dG6EYxkFx8Gd8cptNMEQq6oxuvCKABckp6J-pTTr346UrBePhBBfwCCnlYxWNnVf-74FcPeZTmnccal5vYgBLTz_M39HLivE3cd3fVG4eNQ1M2mlPVAPjWelTnsUi-RCQcWn_Jghy-TbCK_lnRZdjzk9lIGzAy-HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
به‌بهانه صحبت‌های اخیر قلعه‌نویی؛ یادی‌کنیم از روزی که مایلی‌کهن با شدیدترین الفاظ علیه سرمربی فعلی تیم‌منتخب ایران صحبت و افشاگری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101623" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101622">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=UhVjHZpSOzXPRgCR6R5gc7mfFtbwv51LV_VfZnBmKL3fN88L23jGW-rfo1Ih2_AhdUCcfRqDmenL3oqGQu4k5mCLheWhEGpFYja3qh5_M_SYeJWCtNjhK69funu7RNmhvCOmp8gAKTMl9HyuQQDwL5wBhxANPMNMbDACn85wH1vy1cDTmS1qxZIWRNcmMiRDHiqj_V-f4o_0aplX29qCaO8XfAgOxxYIsNtx5zNnrc6BSQD986U4ooryyIUkuZNzqxlwA_HCAsDVrLvGCSR7jziMCiEgGQBjp4WfRHnMo09zZ7UD8bmPQiPoG7qd2q8qqCg9yegzOdoaQZvU4anzEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=UhVjHZpSOzXPRgCR6R5gc7mfFtbwv51LV_VfZnBmKL3fN88L23jGW-rfo1Ih2_AhdUCcfRqDmenL3oqGQu4k5mCLheWhEGpFYja3qh5_M_SYeJWCtNjhK69funu7RNmhvCOmp8gAKTMl9HyuQQDwL5wBhxANPMNMbDACn85wH1vy1cDTmS1qxZIWRNcmMiRDHiqj_V-f4o_0aplX29qCaO8XfAgOxxYIsNtx5zNnrc6BSQD986U4ooryyIUkuZNzqxlwA_HCAsDVrLvGCSR7jziMCiEgGQBjp4WfRHnMo09zZ7UD8bmPQiPoG7qd2q8qqCg9yegzOdoaQZvU4anzEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
مهدی قایدی:
۲ سال دیگر قراردادم تمام میشود، اگر آن موقع استقلال من را خواست، برمی‌گردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101622" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101621">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=FImjGGv8KlGHUuXumh6ljlhM02XLsnBlgbeux7cOkcbcv8SMp48c3qxGSMesiiRCgjvNvxRZ0IPcmd84xV2XQDNHrYrCEcguFvUmJWbJ9K3HKkGNJCJsTqILoOWxG7X-u0b5MWbw0jK3WBQJ8YlSlSJcH1q6O9VMbnycRjQoZm6v8oPA4-1Sx-rrP1ejwEpYIObmJlaCqhkzeleZLkm0d_OrxRYOD6Xu9jNZFrTUQMweBaS6FE-OOTW5i43Yr4-Zd9VsrKR0DVlSuL-brqT7uUo7kkvGon_EAZga58yBmc6tZOCuyHRfXM2AxM9IR7Yz9DD0YFE2J0hlHEwCQgWbIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=FImjGGv8KlGHUuXumh6ljlhM02XLsnBlgbeux7cOkcbcv8SMp48c3qxGSMesiiRCgjvNvxRZ0IPcmd84xV2XQDNHrYrCEcguFvUmJWbJ9K3HKkGNJCJsTqILoOWxG7X-u0b5MWbw0jK3WBQJ8YlSlSJcH1q6O9VMbnycRjQoZm6v8oPA4-1Sx-rrP1ejwEpYIObmJlaCqhkzeleZLkm0d_OrxRYOD6Xu9jNZFrTUQMweBaS6FE-OOTW5i43Yr4-Zd9VsrKR0DVlSuL-brqT7uUo7kkvGon_EAZga58yBmc6tZOCuyHRfXM2AxM9IR7Yz9DD0YFE2J0hlHEwCQgWbIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
سیدجلال: بیرانوند رو مخ‌ترین همبازی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101621" target="_blank">📅 10:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101620">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGTPiEreryIIK_as8c1QE2YOA50VwXMVJ9_wQvkKskKa2OuLK3eaNlJmAaWN-XUH5feXGdFd_MKjR3ewgiufQzhbQ34DIkQG_1RUjgiBd2ODzvvgx60j7rpS7NBzUL-hhOTZwNpOJMGCVDN0IL58hgZpCpj9oCyEHVhSdxokANtojMaCScnMakIn5fqLO5LBHHAyaxcxKdcd2d5eFB8Hyn8gsDgVkzUuD_COM6m1uEFDWXgnrftoZ8cpMH8ZbDftSjaoCnjVOuRbjht-ikOkrHE7CSbYj0SOd9CxQ4VDEXD1TlG9P30LevEq83YUBKrYHp8jowpN7FN0-Gu2cvh_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استوری رسول خادم برای عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101620" target="_blank">📅 09:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101619">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=GXaqVg5-LHjyZWaIfmTN6kkI0cSvVMbLanf9jgf22HISROoPklqx5smjCwe8SoWcef5MlzMKOyrs8k-jxhkyNa2VR2CMqtc6XDFi8l2MiIVCefoK8DnEcxwoOM014QwcyttmuD4B3jwxnpmhMRovucPWTW46rlWH3dNGkFKaaADdctqa1Gre3UXLvpbvVJFUF_6QT7OFsFs6DqpoWguZOhnhvsgSmI53oytxgcgXz-J8GFveREInD-bC-v7HlfbxLBWL_PZFHaPGVMOSrJvghNaX0UcMZpc3k2yxJD7naQFipuaHNkR_ZnkYQjarfd8TeyvGnTOV6aKntSyhEvDf1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=GXaqVg5-LHjyZWaIfmTN6kkI0cSvVMbLanf9jgf22HISROoPklqx5smjCwe8SoWcef5MlzMKOyrs8k-jxhkyNa2VR2CMqtc6XDFi8l2MiIVCefoK8DnEcxwoOM014QwcyttmuD4B3jwxnpmhMRovucPWTW46rlWH3dNGkFKaaADdctqa1Gre3UXLvpbvVJFUF_6QT7OFsFs6DqpoWguZOhnhvsgSmI53oytxgcgXz-J8GFveREInD-bC-v7HlfbxLBWL_PZFHaPGVMOSrJvghNaX0UcMZpc3k2yxJD7naQFipuaHNkR_ZnkYQjarfd8TeyvGnTOV6aKntSyhEvDf1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
صحبت‌های جالب علی‌قلی‌زاده بازیکن تیم‌ملی درباره همسرش که فوتبالیست هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101619" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101618">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=Umgm4nwBrUlMdlRzPIjSfexcsx5hsNaeFR2Lz90cMUMi85Yfq5NGW4zJnU4Zhja-dMMVDiI7fL03-drmS2blPqPCfrEKI62eBawJnSfrA6W8dtQbf37jVlIOtPsv83KyeOxtBCiwNpqalD_WVnucz_SXdwWBVuabZIR-nb_xfjSNWAPtFsyu8bHbt8Hq-9R6QLmOLyyT59ClBlM3tZM00GXyr9dUYhu0mE5zmOrZsTdBlY90JEp7tHpnfK7ozcXaOAeoyHale7ib95m8HNMwF7ie6N3wW6ly-sT_pPoblfXjmBfhX1w1aT75guPAuiSjSaqB5Xuh5Jh5_ZvnafsNiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=Umgm4nwBrUlMdlRzPIjSfexcsx5hsNaeFR2Lz90cMUMi85Yfq5NGW4zJnU4Zhja-dMMVDiI7fL03-drmS2blPqPCfrEKI62eBawJnSfrA6W8dtQbf37jVlIOtPsv83KyeOxtBCiwNpqalD_WVnucz_SXdwWBVuabZIR-nb_xfjSNWAPtFsyu8bHbt8Hq-9R6QLmOLyyT59ClBlM3tZM00GXyr9dUYhu0mE5zmOrZsTdBlY90JEp7tHpnfK7ozcXaOAeoyHale7ib95m8HNMwF7ie6N3wW6ly-sT_pPoblfXjmBfhX1w1aT75guPAuiSjSaqB5Xuh5Jh5_ZvnafsNiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
سیدجلال‌حسینی اسطوره پرسپولیس: رپر مورد علاقم تتلو هست. بعضی وقتا هم شایع!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101618" target="_blank">📅 09:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101617">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmPXEAQMcELUYZXeYf6FXMvHIPqmHt_1WsN--hHWR6IoEP2ngPNVqtmqVsJlVtov9WtoFVY68QqbclP7qQ1MTxzHdkNXIItT783hSIrWgSqj7PRFu3S8_1XArd3pceE7xsW4u4V8S6TMIq9j-u6Q90hB1w7H5zUqUawNgHplnZYYRkz7vKngahtYQOp2rR4aVZOUZm8fJrRU0fzlGnchGfgc-ua9buu8Zu36QBAulNG3_OdyW0b60UCc3kjViYkKTmbyB1XysDW6cnoteR2q1P1ks3K8btETPhgY21sNm4Y-ircZcQuScSMc2AKl_ILOjAIZOkfHfQJUTDTKlf_Khw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔵
⚪️
منچستر سیتی احتمالا مبلغ زیادی رو برای انتقال رودری به رئال‌مادرید درخواست خواهد کرد. حتی اگر فلورنتینو پِرز موافقت کند، باید دید که آیا این انتقال از نظر مالی برای رئال مادرید امکان‌پذیر است یا خیر.
🔹
🔺
رودری هنوز قراردادش را با منچسترسیتی تمدید نکرده است، زیرا منتظر پیشنهادی از رئال مادرید است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/101617" target="_blank">📅 04:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101616">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=GRGTe_TZJWshFdd_dqJdY-iMy6-1pYh3qiIJNua7HFXRMCF3nHPX6HuPfCTE9Arh9Za-o_r6msKR0U8dsUeUK8_iI_HBtKQLEMSL7eeslSNtXRhamFZFF1XWL_kAoqtWqCGi4jJ9fExyx8a2cTjCjiS0p-8xqOy_4DkDTuH6Fl9z062x47_GTJA6NnJJs3GN9Mm-WJStKti3Xt_X2MAcKPxMExXXokK45SE8SR3N8-cLOihXYvcz2OYL9U55KSaesusxdodDS1-UWpFxCcXDahWbCe284EtyEzZtoW1ZOnYNtSCSWmMHV0ci7ywCBwp4VxcNM_XLF9iQ89Gas62aMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=GRGTe_TZJWshFdd_dqJdY-iMy6-1pYh3qiIJNua7HFXRMCF3nHPX6HuPfCTE9Arh9Za-o_r6msKR0U8dsUeUK8_iI_HBtKQLEMSL7eeslSNtXRhamFZFF1XWL_kAoqtWqCGi4jJ9fExyx8a2cTjCjiS0p-8xqOy_4DkDTuH6Fl9z062x47_GTJA6NnJJs3GN9Mm-WJStKti3Xt_X2MAcKPxMExXXokK45SE8SR3N8-cLOihXYvcz2OYL9U55KSaesusxdodDS1-UWpFxCcXDahWbCe284EtyEzZtoW1ZOnYNtSCSWmMHV0ci7ywCBwp4VxcNM_XLF9iQ89Gas62aMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
⚽️
خاطره مهدی قایدی: بیرانوند خیلی خسیسه. یه روز زنگ زد بستنی آوردن خوردیم و خودش رفت، گفتیم چرا حساب نمیکنی گفت فقط دعوت کردم نگفتم حساب میکنم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/101616" target="_blank">📅 02:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XusRZi_z3Mb3Iz0lXaan1KHCrq2zuaIGgMaNBDQdXbvmdmJDPGeVQXldgteEX9rHk8uwYbcv5m9dSUfj8yRVJNs56mlfLenhlFGgbJoyf_zKm27Dh1hHVCVuzaRvF6QyiN8lWC-qJhai2gmXliPZOsoyn-hem2RFn-FICsVAkBzndSVuH2wJi9BByeXSQ8J_SVjiVmtINEKAPe21mglD2gStpUa_zhpaYi6qCZarzZ7lGLkpXcUFTXxeyQsVSna8k8cdI0VJeCFTIvboP-sW3EGA9pM29gQdCJ5E5V7JoaBGMc5xZQCxuY6K9b_MBH7ZakLXRYqi6SCqPYh9fElhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/101615" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101614">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvyaVnQQsjFoBEr9y_qj2LVQFW10gu3zoJzyL-bvplAWMVf78g-PLrMWfGt1vDRJcIEHd72tk3rF_NXg7VtdHzOcJ3qcKy6dIU_SDtkfe86V0SR9M74X1iLybkNoB2G633ZWs0ZfXeUYUTfS7npVw0KRLZaYKsLf2nk-9L0FFbJkQeDIrfABf0l0qo7ockrxF6VxqHmnwecJ-INpxr1mC1p223Y6fk0Heng523A5PRDVwRJRqqPN6Z_Y4w2IfCEZAy30PobMOUmwcMyiQg4waYP8vUp8P5-nU1dLs-eEdYW1zwhsgONcmb3AQTdoNRvd3Qs2jyr_8lO006vTX2JCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/101614" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVuiv3Vq_LPqV31E64Tl-BoI-rdGD0vs44PDvBqWHR-Os3r0Xf2u1ldPJ5lEiR6hTz0hetYP1QmGENdAc6tamRVn5YWBhAjbSOBEipyuc-M4R-l4NCpHMl8gnbWYjFAeVhRWCctSMVEE8Ctkt6zprrP6-MSJjouTKCg6NgqRSbeM-oy8dm2Y-IEJZOpckJj7H4mXQuB7mK3hz7LtXKNQo4NGNJuA_qPHU5se4tVs7xXENtx9kmOp9h5rO3SGzYOj4ixiporheEKI8w0uFtwFU7dIclkJuFzro3jviF-Sca3QjBXpZJIwzJlOUfyewLLOeL3wL-eXexUBv4Tlpe4M3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام از تبلیغات تو جام جهانی 22 میلیون دلار درامد داشت و شکیرا 17.5 میلیون دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/101613" target="_blank">📅 01:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_yj9Z_ATzV2j-QaJf4FvuV0LODmombPgLvTTtBi-1oiZz-1W_DtaCCVQykOlzuNVaEs-3p_1Pt4CGo6Vk2PGV1h0wL9Y3P8GRwz0ZrvcgUEvQQKynFUcL2a74TG-LRcmfqgVCvqokk37xnqhLcaJ555NAU6y_ot_S3U0BivvlIA1c85Yp4jEwkcHHDzhxp-P6MraxviKoHfnTRZly9isanbheDC9UXh079Vl-N5FryTvADCYPriR3LFK1hTLGRzairzkjE4z0LTD3YK6RN6K4gNX0a5wjgKjUOTWPHKbSqNvFvalui7WAK5rW8e76rwzJKNh2HfmmqKJf4l6sZpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط 3 بازیکن فعال حال حاضر فوتبال این افتخارات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/101612" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJjT3hk7r49R381hKJi_3QsweL9ZQ2dHq8eC637N30gANIzGx_wlIoAMZ-bx47RKnM2wUUoiazCdqiIQV9a7ZouDthhrR1C52NUoawtWjGXnTKC088ecUH44q-6Pn_VY_iNuQWrEvG-dYBXBrER1Q-xDIn6HXq4PS0VsgMdIka9jjiOspb7o8VXVslfq_SZ0jp1Ix19WRy444NCf2PMMrEfo1WeavNgpdEkIRBBvJzrBOuO5VKvnZdhX4OQE-lpGX2GFYCfgKbL3NZ3qdy5a9KHMiahEk0lGvOTtemQ5MgWGd7_fm9rqW1tSJFQVP9PTvZLQY8cfbcdhdbegCQ07EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/101611" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fkteE6kM2TVuq7fQ6PEBpsMphwGldpHgaVhKqmrgXXDe8Qy_rEszlIOoIFlM5_BI654rQsCBVFVD_ncGDDENHUHCa1SHmligsT8K-XBLIJo9dBZrbXR2tRSfDb6P8L82TJRRjjFPXjkJBSVl-LRHa2o1TTTlvDuNKC9v0hhE2IAElFfzY4aZzdxzueOkkDAELiC8CSJsDgSIilbLw6Vq8VV5Lg3L-28rzAZlzJZJeUxmvpFvVhp87O0h23Ul-mXrSU53xHUN6qAMvkWA2kugjeVWs0uRow6u-Hf_ClhXFUyY0jCN7dZa98R3n7gnb5ncO5xWBZdyHmT-2I430DbqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/101610" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101609">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز: رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/101609" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101608">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCbGTOBW_77EAvnYGqOFxzMbykyhrYBsAhRgzyx96djmEjHjUZ2Amt2uik0eDOgBNQNW4qeidY5QwKTO1L-uSb6Ey_nTopRhbQBjQ3C6YTMVJk6np--iQNl8cBLmdujMWicqKYnv9r2YrBMV26CxLa8vX88ofAiWKu29GlYRq1fTLp696E8zCYXlSTMC8zbuunEUWAtxSxve3DeLLUdn57Ls6xXjjXtY-9tZBiQ4vgE_T2gEQzakDVLtkpOisC8Sg1TaM_5GcHGGx37VeaGpwA-UtrCtzsDJXoDAbNxrPOzm8xQY1Hpk50YpHgFLw9lZXOqwjsP93U3INb2-vmQbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
والنتین بارکو با قراردادی به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/101608" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101607">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
▶️
👤
حمایت‌جمعی از مردم فارسی زبان آفریقایی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/101607" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101606">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101606" target="_blank">📅 00:17 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
