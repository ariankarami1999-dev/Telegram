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
<img src="https://cdn4.telesco.pe/file/uQhk-sN4BYEX2u-XZQCdiJTOwlohhS5TRWvkaDwWKKRR49SEu-Gj0BKi_kM2efxvizIdexUN2xtbsgIJAjSbZ3eBq8TtPqNizxI10tTxJhHB8ihTP1QcJWQ_4WuzQ4LCSGS8CB1SC9ZI993XWs-7i5SYI0GeyfZMV6Ac380EhaEeJdWbgtr1WZYKOuzyUwkafw6z_Bi1hILqGJZRfZKvI1FmG6T62hfdF_YrWaRLlD5QigJg57owXM6Ta1ZvCpmry3O4c1IWMwxO0XmcOvZMy9pWwjGaMeE5_q1_ojZZ2mFS-if6vlpg7DazDDyTWhHujA3NNCPAVx0mpxEUM1EyOQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 356K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 00:42:18</div>
<hr>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOZ_D1udFyesgBEYScwQN4m3RXKOV2Mma6Vutm6uga3d2W7Eyhhbm48aAbGJp3MvafO0P4Zty0gHNK9aorCPOdUVYuDh095ELzE1S6POC4LDeu0R1fQPOjjF3sW2C3JYLbrMDpfTSvvMMgZzh9R-X1wZ1rRmppxkUtgDvawqzEv-tM-k8X7mEy7X3RF668iLWroS0KklFKq5HQDwpwADMNwAGmMw7RMpv8pzRQ8owLrW8py0V5bBcEv76Yawy3AdYWngPPl7Lq8tAAVgGcTgY2SS_9WroT-0UKtijLoeSozl7P3oxyW8HWm9fyKtb6qKIAgOT25wB5qsPjIBJNkT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9YgkOrtOtxaK6lEIS7-eX7RCSStLrcKEiU_wwmR0MBm1Zwjov1jhh5rlPReIw9xmk1x9Ucxx-JAk6zYnqGcB75MbpuVwZc7jO3xBy8NSJFVkPKePYbfM0jcOIDqvctaoQABiVujrF7hgFMi2tH2YMsmJXx3S98YdzV3tn0PbJ_sMubix6ofrX_ScS9vWCfxy7PlwHDnwEIJi-zZzGE93bnuon2Wo0zi8AI7YAMxyeSTmDuA0IzOBPv_bQcJcS43RTdUchM_8XmAeJdLFJzLMQ4RX9de5dtD3hhy_9KVPECV7vKLuKQb436NPrdaw5reSbmhihnV2GGt_O95fGlVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLUlMjjFP-jaqC2mZf_JkuWGl2JdANXZbsEoqk6aeTO3-N16OVOnij0EdgGn0U7PGPtsQwpMsha_Dk-Aj5CXcq2zFkwKG-MAO5G39H4Ypp_JaetuKfhwco9b2mjf0QOu7pM1-iang-6j1xqoQVPi8CHWt9pNmeLfWBXSjywy6DUTgsvh0omcKYVSdX-FSB5VaBp-G-WB9i1cBvjISvtIDPryICwLlAuI-IbCSLOZbP2QSHA1H5VKNseOmXe4G8QcznaIQDNrLnReQM_BmSZORdV0uGHqlC7jZihD4eGMWfOT-Xwslzj_-Pu5DG3j-Obl_kJZZyUbXoD-dTvhIoWAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhqLMqkgu5rXeTUCFu7ZrF9iKLw6Iep7G5Y_UpI2b64WV9E5_uDYfgzy6A2nKjZpJpLVXM61c-YELNu-rZVS3Xgwh5lil9RrFVchzv6ijOD_A7CCEjkZeZjcqI1iUmLzyLr37rtVe2xG2eaFGX_dc7xd09jCHazAJPuR1walSGpWndsaS56HBCMCSW1pSU0Jn2JUyEpkN3qwttBvtJ0IiA-bFey1O21vVVtLY4Uh2RqLgCAx2IN1g6PNbJT8XdYhjiftkuNUeQwShTdJbgi3dgae81rywX12Ltr7G2DvnekhysFdSXIck6B206vYFoIsZOTtJ-mKcgWGQ12Pg0Awbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g219ldTcho1iMJ7KwQ-ouyl04AMLIDPk9EF3cqpTc9nQsLR4N4lS9oFdhOwEXAfboAwV6HDed6uhqxwQWIPTheU55LHJgpkspA48g06KUZLUa9n32O8iRkaMecwp91uO2tXBzSBLmOe9x9179hIIoU2SbmwfKtkbxpgzqrHipGGuYMI-PqegpFE_DWlLJ2GAJKTujAS31ne7h4eysWLB6cKP8GXQ1wWEgluB7mi_UKVI3PhbcAuT7K1cBLeS4xoEuxAC8MwbmYvqR2JhymTgYy7Ab70pRRDXwZ87sCnlMuklIuALt6RlfnnZglu0Bk3FNbSBmVj3tQP8dVgSrvw7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAN2dRqX_T1ywOxzPhoY3pvwy8VECJrbcHDiXBE_vNdP1NqDiRKF-MnkAZBcjG9GXn1U09DvjBUvuQhtX-25GnwaLBQU6Z70xOfpsFiy5EBvgIMfsSRkC8BX07yIt_MhFZmKW1ClyqVWoy1uUjeYTJAoo6U6Z7zAXqr5YmvAm28YT35nTqXjtN5Mc5sjzlyLoEK72ko7lL78Dv61MwwtPjtZDixXsjJ4TWs2_CoQVojr3fvtZIYXXikMwGo7JtP3pPpcI9EdnbvBtrlt3HfQUeVQGS8tKtwdNDC78JGgr2PnfMrW5ZgDhVt1oeAiZSjmmx-iD4ROX9L0ox5iCx5cFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am1hd1bno0NTAnTmYjQYN-kj1MI00CRpsI4hRpqkmBgQneUVAo2C9__hE3LhTgi5ERmHZVcVHFBhQ3mlFgpDZ5nS9WpsKSM6FT17D-JNWKVWrsxlGWDYWvoVVD7SUDrYycTSoC60HwSmcX_hsu-qABGLDu8u47qdufsYmgjxgGBlTSdVUUEyOFlHaidZ2O_INOR7ZIumMpNlZVWxrHfsnTyF6lNb3_Lzy45pQ-ipu99KYjRbbwkU7L6d8fum9V5-2BGWoEX2xDSESYH69DLd3QcUhcnDVTIoEM6hZ0Gd0hW1TtLfii7yEKIgxSQyLDUoMYV470U92UpMcHMGCptSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRlWk8iUpP6eygsDaKtg3C54FCB_IA-ctz8D7sX6Hp-NCnfkoUfzx2ottN2S01Tg4NoS27kFUyax0jPimRtX2vVI1iOKSLMIRgnBWMM_IzDXi4s16aFeUeHEGCEgBoggs_E7tO7_3LgLo8Vj2GFFBX22vUyqRDHdpvKui5oNiQXXSyRWCdoYEqt2UoPxJZP556Z1FYkMuYf1-wqReXuBDtIMXKUH70qQOQZ8FY1iPIMesvL_mtzqISVoW3cyA9KfBkls_-3aZ8bCHYGHAl76QwxWqj04VzGP1Frut1YsI0qAOZPh_j2cu2tJzQYoz__K1sjOMseTl6b8ml9lKts2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSgg5ma3FyAO-P_HBlP9krMgT3mZXMtqKxvyUd54y-6dZYDdznTWwYscjQ6JgPElWyMQjHDS8WzhVNXhI2Uyib_nHnWaWBfVJWOkzRyLdJcSQWyXJbx_iQZwcyS-Gja4968U9O7_k8_Gj1YxjQCun8CQADuhwOoQiEHlvEtgcNgttsg7dhKyP7kFQIUio4BV8vVzYwpAvpSPROTlPifek6PubpBAkn1OfVL8qhvg-wVpxTiYg9AftXZh_pFjuH1pbtcVWzLnCXW-7nhfy0A68WHIH1xr2HZQc_cPP-msc6ZNbH_4Sr12SS7acBualmo3z8hT94n2aiDhgKgrUn_b-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🆚
🇻🇪
🗓️
۱۰ تیر
⏰
۰۴:۳۰
مکزیک
🆚
ونزوئلا
صعود مکزیک یا شگفتی ونزوئلا؟
⚽
🔥
مکزیکِ به عنوان یکی از میزبانها این رقابتها برای ادامه مسیر به میدان می‌آید، اما ونزوئلا با انگیزه ادامه شگفتی‌هایش به دنبال حذف یکی از میزبانان است.
👀
⚡️
میزبان صعود می‌کند یا شگفتی در این جام ادامه دارد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/24705" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mG5YSnWAZvdKGUNRGSP7XKBUsEZZPN5eAtJdEqdVfwZKG7Wbzyf2A3GzEV7BKlLfS89bAEaMuoY3z3MIGUUCMNSSITeteDw75X7jeFFtMPRQCm7CWgO-qGiw7yHRJJbWjOq9BJtvqdwO6e5lHugqBldH2WURcs29qQO0h9zb4rdwzRls5SX-V0wkIX0NbB79do5QQVqzg7qWddwrT5NnTQtWKCbRwpBHPa3TUlSvZLVszpykVTxgB_FfnHRX-T-fX-IwXTBtBABL_GW_g4Z4NQ_69DGi1h_xzqTVhDsZQBRw-aoADHWCOHaM3oG56KriQs6dsqgD9xiby9HIlcJHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dr-om08pVyZjOdv4mIrA-Zx--sqii9yT3kUbu7kFbV0cILru3VnLBi7Y1u9YgA0133GvYEhy4FDGqIsP8l_OB2O5UhLb6b3iFFfmM2DI526eHHQ-3qf6mi3p7G0dbdsjphCn9627-sMYP98fC7q0eNQ4LBwGISZn0i9J2O-0qIy7LaWuJmQ8LJ7Gx0DzMQh2cCtfOJ3DmzRqRbfYsYjRL3lrl_GAz7Lix9Zo90RhWprGL2_og6aOwSteLgLQpnYgXnWs1xGJb79xH70G-JIXQ9zcDYMv76WlTaCQ79wWaKE7LTTsyn_f0dRO3Vha6D2IOGJAcFB4FfVQjWUJP1ru8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccKE8qDkqWHjD37RhMtQ5KeSRHZIZazEQ6gP7fKvvVwsGepaW3P4Hm0EzjAxWzmG3ERNe76GGnei7g03PeyJz0p3aDWi7LO1a8HWme2ZRxFHWCvBCC052f0DgDyitC7nFnl1vNvqhXkBe0wJbEv_YzvpXzxiEZE6-jU8n-vsvZLcjQezRzwjIesnrD6PRpahdgIc6X2B1uuCa_jMnSFhVRoFkKhhnUA8nYe6qtaY63XDrQXeKUYROCzXC7lf_tmySR9GiIveq_gt_fpklzghUUqAC1dHUMNAuWizP1fi7EA-aVEBor8uveyY8Q1F6qkU66Myljb0svZlhhrD6QLl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLnIdfs_am2_a2irfZi9CEF21zixY-pM1_5iQYYgSIh5hX2kFI1mkE9Y2BvKiI6YsVBFF6lAWTvYjIpMpx65jp3SiUqRtZK59JyGDs75iZhQQGDGsRD2uX0U0x1x97fQh5aQ92hAeBAoYXqCX3NrAg-OtX-7TRmfY4Lco_gUOzCVa3U-Z4nK6yFY6K6QHRuA0vOscYEFU5aUBomfeoTNdXO6FKSaUUH6jEq0iSozxataiAJUYA8RfcMo54cbmQpeUBcORKjy5eHYOBMv7iGf5r9FSy17clap2T1001xsghqYLiBRuSqTHcJ9y-BjGqo8TRAU1sTZgp1coxapHhv1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJRoAmosYAwTmtUiAs7-lkWJnwY_j3Ixtg7LGU4mD9tQHTvuefQ16dBdyGMBEFMSNL5EIHLpl6YHHWIVtSqxutTf5H9GJdaC7CR5SJ5s4VPkSNnKb0b4CrbKGDDD7iwszKbNfs_N62-SYSQg7SDChboQ4KfLAZlbIPQ43WIEAqinNAVjIKhP4iGjCQTd92kgX51l3TTXqafF6KKZ35R8G4hnlcj86vyRRKY67X69kwJeh6emxzgax8FH-tTiWZqBI7qHzjaeOBW6Qhr_ct4-jA0TA665dK5eP_sjVRyafSWTnGKePdza539ESwirHYWKV-vKXNvlLHW03Udjn8LNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN8E5EHIz8S2wOQANxf9okRmytkNMnJz6PDROHGdef9mypBwzsUD31WcgsD6iHMxePswKVg7Imu61ByjBJ9v9cI_jauinKE54FlGfdVlikJFRG-n1yZaD-m81XYTqMQv4VkovAwIw7jMynznAUh6izF8DwQ7J15b7IISxy222VshJqR74Ell80t2cAI1tzVGVi1gSJIoUYpFHtxZT-Jv1oFAOFtttEykn_UBF9u3kztYOmnZ8UJ1BIG8M2ETaKSmBggpWw4jTteoGx7aDnplm2RTc-Jhigy10rlh46KzoD47F5wXqzzPaGsEe3cmHqTV6GA6xjdtYle4iPrT4Le0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkVdl4aWrmcD0-A2_biYRPwxfrqKdr2cHc8CbE5Yl-nFxv_fPUDspNZkOjGmLWobLs745wwAtbvR77P1C_h6iSAU51orEwtM6dcETFVK8deCnk2maha9sFhndsfKIisZ7LsT6wIsh_lvRvTBqj8RyD1Dc4vkh7WR1-9gX9J8eYlhQe-RQavSgWImn-_M0ClY1MNpeeMYVzBO_lWxoV4oEV6GHNiagm3jhot3pQ6MiSPSk2KkYhHkBfzEXNdt-p5s6vMBowF7edwQr19vdGy_u97OkkdKxKrU2J2IUiQZzFCfKSk_ragaitLSSizhIHzyqCqk_ZAdDIUheeN_gkHVDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=dzzMgWHaFS5YeiGDShIN4Aj1tFkUeoJe9p20vIyvsqqn4jbsMNE_IqlPydxCkGeXaNTmEBVUZby53s_xgTCmc8eGap3dIocd3kZWjIhyzbFdRqWb_FJQyabxsVqkJ5doMyFVfp_pjnVV_fEbW8NeJzCmSQPIv1C7hqUNr4Yy8rdNEx2EVF96Fo5fxHFWzly7pZRyi5gpITisPgI3jkZ4Wwvo7fB9VYwuFiZMlZfazIxDKck-GiTZDPAXqiKDj5_G5Vy3s7ejUaTPlDtzdbcpi2Sa8NxLx3GNbUEjTf0FCCdNFxhhe__MY4SYY357ESwHAwkPrW0Q7ImW-NH861QN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=dzzMgWHaFS5YeiGDShIN4Aj1tFkUeoJe9p20vIyvsqqn4jbsMNE_IqlPydxCkGeXaNTmEBVUZby53s_xgTCmc8eGap3dIocd3kZWjIhyzbFdRqWb_FJQyabxsVqkJ5doMyFVfp_pjnVV_fEbW8NeJzCmSQPIv1C7hqUNr4Yy8rdNEx2EVF96Fo5fxHFWzly7pZRyi5gpITisPgI3jkZ4Wwvo7fB9VYwuFiZMlZfazIxDKck-GiTZDPAXqiKDj5_G5Vy3s7ejUaTPlDtzdbcpi2Sa8NxLx3GNbUEjTf0FCCdNFxhhe__MY4SYY357ESwHAwkPrW0Q7ImW-NH861QN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdMojqV6Cs3jFm147rBSxfAypPmTUufUDaEziotwWerM_ogeWQoO7oRA2VD3a026B_NuHc_k7Rv7tK_Qlz3Jx_D-skupZFKkBrotguEQgvAwKcObGmpXZto6E7wRLgh1bOno6mZri0NzLhB2OfvYs7Ym417-oHpz4-6MYbAV0J2mEv5c7anmJBKY6UQVH233E3Rr6KjaYPB0HVjvmIVATL9BhkK5Nx5s7uWBNSH4R25naOPScMyNFf4Z3EbHW7O5NlOFzwVlcVs0rtpO9hxWI3baRLTHy_RasJh3k4j0OX49dzMM5HXwoecXZhQYXmneHsx1ext-59vtZsEG9pDhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=KPetDvPBzAyfC-pilnTnr5XPmvNFAVmfrYZQTS6iTjE3DaC7-YzKAXuP2Ib5UH0CfW8oJijltEg4w1OJY6pi7ukn_HCVP77CpAw-O2O7RhRPP8-RTNb3sVEvth4P1p7XmM9SW9HK-6rleE17eOjUdbD9cA2hQL1t5yVJ4a73Vq8G1rTnp1igrc1kWLPEyngdb3ebQ1kO8iDjK3s-pr10rZ6DvNgIvSUbtr3U79TP5UlZDs-jQal-bN2atdQZpnWiLXrdVIHKdhpCxNcMUwPva9aytK6RvOynM2pv2bJGyfq5cXzt38dJvyKd9uLX1zdhsgSxb0ulVJVyaMzJTRU3ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=KPetDvPBzAyfC-pilnTnr5XPmvNFAVmfrYZQTS6iTjE3DaC7-YzKAXuP2Ib5UH0CfW8oJijltEg4w1OJY6pi7ukn_HCVP77CpAw-O2O7RhRPP8-RTNb3sVEvth4P1p7XmM9SW9HK-6rleE17eOjUdbD9cA2hQL1t5yVJ4a73Vq8G1rTnp1igrc1kWLPEyngdb3ebQ1kO8iDjK3s-pr10rZ6DvNgIvSUbtr3U79TP5UlZDs-jQal-bN2atdQZpnWiLXrdVIHKdhpCxNcMUwPva9aytK6RvOynM2pv2bJGyfq5cXzt38dJvyKd9uLX1zdhsgSxb0ulVJVyaMzJTRU3ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=iIaTcFIqbXhneYRHgA90lt0cLtpx-nWoXMzBtALoCSG65NDBmZLjWmDIkOC4h12UKOs8b7LHSChgm-AQEuLod5Q2XDk-8nRilmfX_tZ63hIJH6q-UxmWwmm5k8HBS1-zr7YNUntBvjuhfUNx-Emq7G5E8vv7KuaS3nqQXJ0ZxRKMoMl8n56Uud2SnWFfymLuLNhmGwDszjxs_7O2UP1SQKywVDsROtpqBSnMFMG6KX6LXzk7PjV2S2JolFp-B5_1n4-0LeuDGtaQ6Mo0TUpZELqgN4u80ZYKgHip6L6lNY7rqak-lP2bAUHSmQbcbLk4CulVnaZmEWSDu688errU-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=iIaTcFIqbXhneYRHgA90lt0cLtpx-nWoXMzBtALoCSG65NDBmZLjWmDIkOC4h12UKOs8b7LHSChgm-AQEuLod5Q2XDk-8nRilmfX_tZ63hIJH6q-UxmWwmm5k8HBS1-zr7YNUntBvjuhfUNx-Emq7G5E8vv7KuaS3nqQXJ0ZxRKMoMl8n56Uud2SnWFfymLuLNhmGwDszjxs_7O2UP1SQKywVDsROtpqBSnMFMG6KX6LXzk7PjV2S2JolFp-B5_1n4-0LeuDGtaQ6Mo0TUpZELqgN4u80ZYKgHip6L6lNY7rqak-lP2bAUHSmQbcbLk4CulVnaZmEWSDu688errU-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-Udv9cN13f1Enyax2S9JS8VnWNsE4-sbwMu1UiA2073DBYpc1co6o8ter_po3ddWkOzyUqDPlE3yWYzPzbeSrtIrYqKhYSfUjvHSeA_585CaZtAmls5I-AYvrZ4OKmZdlTczg2wtSGxPMD6ROELsTw2LAZcJzJcTKvG7_hTwmMrLoLGnto93V4EcloQW11kygxvpIlYKWNq_he-GVrfb069QAp42r693L1JtOFjzJlqQS0YRpBV--oDMPLkoi5ena3NP8pSBxZ-GoNOE8NjoaW6keo4wZNQlnlSdiGp_keOg0ht42a4gDVe5N8AHjSG2uOdIf-lSgKPpMVwTATaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMN7AT8fRVngPS3XUv5d3wc8MsNkCBF01IRFEn1pcTCKpBgbLwPCxhmwZDa-yEh8zfkMInVMyP_jTSKoXV5juBtMyZKzKPsK6qjOadKgD33BGzEr4QbptHtNUynTzjmLmc-mKHOu3JCF2Ad700m4bZ0o87V0sdn6bk3cLgHAnhtUJR3mpdrk2jArjDuHpA8GU33roh7A0Qs1gSa1XmlHzWblFP-uxWrebV8MQ5H_y72SgSgBs2KjvbFrdrWpXOoRSeAWziK04VefQUFv0um9cLRY_mAjuMML9irTxLyKu-myUw_H7-IogGugQQl7gGvUosIGznTnWJI_MED_x4dn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLjnQQ59dRRCgV7u82sDsnyiy5kzunGlS8pZaSDZGrxZ6T86CThu4IFcdenOj0eaWFU_3L0-Mf4zYY70F6DyGAEw7JjEb7PlOYq8fQNTZySu5cnni-bz5WigHW59CELTyN8JTYdWdGdtKe5oFf2rsuiqT_iBdUwwi3fKNYhrBsAz5QCSnAzfZg0gT15f_XybORI_TUL537r70llv4NWdn1cOWvNNPlzH-syMBddjBacusTQb95omkknjWLgYjFs3IVizyULnS2UeBCqmJXWuU2cR21g_a3M1M6NMyYrGFJKdy-2G0qrD7hp3kuafJ7ngYkoadVmT-Qg6acVT-gcgCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrGwScrGnSsY6uswge5bAXPzBNjLdDutkJJ_2NuEzmx4h2XB_ULAx5JGEy7M08oeFP-M94WhYRA1YZGGxnJ0zIYI8TuzBNFkd7Nu0TLBe6xIQQskIfNkkinLr4_a9uTDv_QwdIjXzg3NaJEouPxx1sEIzdx4hcUdfWY_xarTQa3iSlROYhO4UsZAD5dAiiT-yGq0hZxb6om3Z8V2KQuHotzb7gM8s3gUdXhIWmwbko3hN6AFA8ezS3CDSvbs_ke695X8RfTwzEy-VcLkvvru7rW5sRKvnFhZSNbC3Rk1JJ_nApIYPMdCvke3vNVENXR-XFy4MgtF0DT_LspxVmIsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1LhQXfUAV1hvnLemCvuhVrH58qle8UvTyaFDlSwF5wvFKp5feNRGuCbYFw4-IX-3fzZarideKCjVEsWbVA92zUu5o6YnIw5UHDsJ7b4iEP-YOcyEJp8xlIoa7Y1BcTk8hpseKMwjSa1vvxcn0TUnzS0Jgi4MVZqHYTYva2bOUFsBValbLa2K76vGAt4ovsU28YPfTARNWSYgYYpX-rpJ8GQbIOVOb4feqLCRqzs5mbQE_e36sgccM9DUOm_q0Y2aRXGY799Jue-q6AwBIya0rFQa95rH8lNb1DT1RhcnbbTuwopW_4qgBZ7kyBz7ZlVMrde4Leir4Afqrh-2__rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24688">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkjvtxCqd_7Bz-cGUSWdTaq0IIjalJIKyEQlu-XOlEmEDDfLrxg-uQUZO38Lt-JZ1FhQDL5Y1aFSfmbqA3uzEtk1qD4j993JGr_5IZOWjP5sKDyMZu1pWihPxpYSGrauGh-APoWp2YldunqbTXCnOdWRQIVD9E-BijOkVpMXHMOwPq_YstVXInvyS-d76XhzcJRYGIuioSVv4uhJNqsEH2iJU-ZC6vCTvMNFLC8aJHmsJndJQ_syFQL8MEvaKLBWWx0ICVhnmJTwOxXBrDdaDB8p4o-IIMxTFUN02MAaIzKHrhZruCcRes5X4q-_Z1Nvmz839gQPMbahCRrIUX593Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقات
جام جهانی 2026
⚽️
🏛️
رومابت دنیای آفر ها و بونوس های ورزشی و کازینویی میباشد
✅
🎁
با شرطبندی روی مسابقات جام جهانی وارد تورنومنت2.500.000.000تومانی رومابت شوید
تورنومنت
#میلیاردی
🚨
همین‌حالاواردحساب کاربری شوید و شرط مورد نظر خود را ثبت کنید
👇
🌐
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
🔵
@RomaBet_official</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24688" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=S9fhAAM-J75y0qxEQKf1CYkpYA54zSx7Gi76-KpF1TGX7HKkRrXD0VqiX6QMMrGbpcP0_Lq0CU4Cg0dwyWRRz4cq2jl6Od7ZDx7yjHVdWlryNFvaCCLxoVCENzJ97R5rsyzoMJNTyecBrso4ifGi8DyHzHMrxncKfjKs9P2QCyQYWrNcKJY7EfLQPPyANTN8CjZgSa_CLMF6sjVlybIEEk741w5BoHgMZOfqjhZoREhFlv7CdxLS7p0BLLb_tDHnJJZvYN2OvpmXTqov8Ik4WEK_PuyAWBOvI6OwsKAQG2rP6WhsqqETOiGn31Srpw3aEY8_UvrFl0JYxI6j4m9d1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=S9fhAAM-J75y0qxEQKf1CYkpYA54zSx7Gi76-KpF1TGX7HKkRrXD0VqiX6QMMrGbpcP0_Lq0CU4Cg0dwyWRRz4cq2jl6Od7ZDx7yjHVdWlryNFvaCCLxoVCENzJ97R5rsyzoMJNTyecBrso4ifGi8DyHzHMrxncKfjKs9P2QCyQYWrNcKJY7EfLQPPyANTN8CjZgSa_CLMF6sjVlybIEEk741w5BoHgMZOfqjhZoREhFlv7CdxLS7p0BLLb_tDHnJJZvYN2OvpmXTqov8Ik4WEK_PuyAWBOvI6OwsKAQG2rP6WhsqqETOiGn31Srpw3aEY8_UvrFl0JYxI6j4m9d1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=DayV63JvBtYo7iVk59NReyoqS1R3eIxpI5fv8GAm-IB87_POCHLmw5UDQqbO_ECzOEyV_Q8GBmOGMOXiTK7BdZE8tHPteeLq9A3A-Geq5rdECJXx1I1i4DVDrwERCIKKkWsgADyvYeKNyBo_81haL8cxkxvnylYj-M071bZSS9AjylqzUtbk-QIswIxDZZzUNj91nlXVdSDrswfGMhOuyWmlksUW1_bseAW4tywYKvBfOw4I30uEKBVqzwycInNSzS01BO5hiutPgKWv4SGO2pYbrSVeEoNPBNRQbB0aGoEXRbWv_11AgsQgj255iLMW9UgUbuSkKe2mI_r5K19VWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=DayV63JvBtYo7iVk59NReyoqS1R3eIxpI5fv8GAm-IB87_POCHLmw5UDQqbO_ECzOEyV_Q8GBmOGMOXiTK7BdZE8tHPteeLq9A3A-Geq5rdECJXx1I1i4DVDrwERCIKKkWsgADyvYeKNyBo_81haL8cxkxvnylYj-M071bZSS9AjylqzUtbk-QIswIxDZZzUNj91nlXVdSDrswfGMhOuyWmlksUW1_bseAW4tywYKvBfOw4I30uEKBVqzwycInNSzS01BO5hiutPgKWv4SGO2pYbrSVeEoNPBNRQbB0aGoEXRbWv_11AgsQgj255iLMW9UgUbuSkKe2mI_r5K19VWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLJgzDWZcG9AxvwON9lYhceyYnLF4GH8BZcYKnzbPYSbC5bVAr_MLEhNQqtRrpi4RcioAANtBgldc4svRg4U2bl97siRHtheVrIPzke7RvdbGvLhH6rCu7XYZt7-Lk8Pf08ZKG7iAILCiD5oq8GM3TEThaR4p5y3f3_5RuLWosk1jxNDX9NoDor5mtgmmY3U8DvxD8_il47lgLiYUiAWOX_tS8OHD2hCAQ7MmODCsIkwqRTwBQLtNrZcYW_C-ihTu81fm0c3rLw7VX7gLaK4v0-J5CpNf7hTIZf8vvqDXL1fC6aM9ALqs0RRSs8nBjiwwxGSIsRBC4P4HMbWQXpJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaCUPqxv32UYRku8h8qkKVQdWEAK8MtSQSZgjbsopbpTzAaponwwGxuokY5DqVCsnJQVLZpjT0jAZuANXM_nQvuBLPdjc7-IKXmp0NpnkvNi2LnmPGR0GEEWdHc8vzQD4EQvMk2wKbgGN7NuoZL8yoL3eF-pMlhW_JEbCnMJZ_X1kGBsVCH9eTc_BRTq-8WnpedUqejDJYhIUmIc5Mu5k6FVpRir2hOrsxT8-3ZHYfKNym5yEY4d8EelsQGlhyiAt9P4KD6YmAPR942htpcoW3bExbmJvk0y9iQirN9flb6Q1XaGHTqgF3W-Y-iwIG7h7T0cfinnefaydKflRMfCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsIXrE17XfkzWW8239RTeGd8uXxt-lz3UBWK42K4uF5GFgeowu3kJOdxtINLIWjFMQ2QxqPgQ71YgAWsnBXCBrO7yxOuK5_inqNfR9S9plfXdlP2tvA6WNcjVozwORoh3FvFBBEwaqbLEYDPL0YavgEOxWLF0yo3QEngIx8j0uZccz0qnqgJtKkGDi9syWYabscwXqfD8LcXHzgCQSznHL3bjZSPoP_EJvK-7WXMlwOdC2Cbw1EVUIl5heJYF80cq5qV0DAN9hndZO2K46pazLC7pXGZlELbyzOBlzNUJxmI9f-sOtGwkIAV-GNtj9_JVBkRgdDWukeenfCaJEaQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=QC0CcCVNr8lkSet0WcVm-rubgZTv-st0xs56uYPnF_IHywM2eFjsGS_hZqZsPORGr4Qi3djSndpFm1ux2Wc1SFE6Mipj8hACInQ3fjTQJGp63GFv5pvY1sSUFhdcWc2O7WBdBaSZlsXn1lfhZk4lv7ZXXL_Af1xoWdYrSMmF_npjpWTJZvCg8LM9fPbivwqPJQzrzKquwQP67DqJCRcKtM1E7W_GqBdu4ux5XrnVcczQsOa9Pjys3GAXXhW-PdCJNPL_mqQkTSiBWqPhDV-sYabjDGDtdAvaV4DLpaz13M0cqQ8BzAuOi7W_6nOd-IX9GlDtVQpiowQc4Yrswikgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=QC0CcCVNr8lkSet0WcVm-rubgZTv-st0xs56uYPnF_IHywM2eFjsGS_hZqZsPORGr4Qi3djSndpFm1ux2Wc1SFE6Mipj8hACInQ3fjTQJGp63GFv5pvY1sSUFhdcWc2O7WBdBaSZlsXn1lfhZk4lv7ZXXL_Af1xoWdYrSMmF_npjpWTJZvCg8LM9fPbivwqPJQzrzKquwQP67DqJCRcKtM1E7W_GqBdu4ux5XrnVcczQsOa9Pjys3GAXXhW-PdCJNPL_mqQkTSiBWqPhDV-sYabjDGDtdAvaV4DLpaz13M0cqQ8BzAuOi7W_6nOd-IX9GlDtVQpiowQc4Yrswikgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESibDmisJKlZ2zyEycqGMW2K333jb-N7lpBKQhkLy5trmW6yFGSF32GgvOjVDYvVJeNwnhzs_Tg3ILjg3fmdlQDAawTZ51pzeSao1mg3oZLGK7_Eui5uZA4xmCmFSBqXp-pa2DYZY_y5SXH-X4Zs3SqxPbAbS_CeN9CkcFkwG4hRbadD2-XIPxeOhbqId05TcolPrWXD6Yi4QeJ9GC3toobkkmIQF6g3n01L3S9N_662qBqLPfhSZwLlxNAB2J_oOrblY9kxZJMcsPLWszT_TuhC30BZfhSSzOk3M3vU9ATgIoybrGzmjXylZyYj5fLgzv3MJV65xOhpxedoHRO-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9VqGRQQwqWCw7DRSm5IRDFfkVW_AChBdyXlUaxdoVe3uUicRVMB09csv2FibYrSmeQpu63gol2w4fU0bVSY2Yzwbii54G_IibMx6VCsZdEQ6-TDHL8LQ6P7NvLDWsNOG53PzBaGnK-qlJOsmVIITlo4p9gUjDiO0QJDjm9YAD0nfaTX-57-fnNunrK9zuw8SAeNHb8XUEEr35R7xDXt1Rs9AgB5ezni1k-NuCTnlymdvB7f1qGPq00lW4Xr9iK_aWfTzlx4bh9zCksjT7A-HcfeYXeczT7hP2ZEMYn_OE1rd9aqxcR6CcTY_rWyvxlovltOJsDVz1u0eOTEN0-iaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5a1o-ts5-egllzUBeHk_zg0YUrqQ_f51B-vXYjBNF-WZJwREc7u112BhGxTxqvFmwosPrYZe4o_a-APzoVlSWDolwBhviZsmVCp6XoAsP5YkNGpfaZe_S8ob0Gf_C2L9Fuuh1W3vb9tmdzi22DmWioitKt6p_yV4B-cO1KFn1V0HeUuLNRyTNUJYjyY6izFoYVdZMyshzeAsQX6PLRbv1q5st9pE8pULl-Mv3yTas5-FOyMLVZvSJNfQf3BcNaPvRUVrxQYK0vZGSpwGAWpEoejubFCNsOW5QmyFB76msG2eWPsBISiaXUzb1B532VO2ytf2xT1ZhWPSuDClWYIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmayYgkO170ckdvm_x-3h8bxi9DgB30vAeRIVswYJftkvIJhQPQx9LQwIlNnB9wA7vww5TI80KHHMwoqhGWD8zwKgXw70BaN-g60z9c9sWJEjIggq-KmPUzY90U-h-IAgIaS6NS_9YgGhzhOggDj-bS1BQTAHEXiFRfrTBziTipv0eq1dWuo3_hjUyoB0utt9BQuJ8N93_FKT0YWz7k54RV4OZWWEEI1eNErHzrdGA3vYVLaTlzO4v__NxXKm6v-uXLmTyxr9W9GeOfJcKNmUHY5L9YulHlEtoTTtngPQkDx0bND-CGmnoD9e7F6cN_M7v9NGL_REUBVBtNfY1ai3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUDTzOf3jhg5g3q8R3rxF-ssYHIx9VOswn3pIVdAIuxz2jxqBOi3LDIVulByD7ocmayMR_91oXhLwPp6XEzQiFEiuepZMnFkRu3cO164q7CP1PHxL9i6S3xWmGEjURVXXpWS6V5TOg_4Du85qkdP5-27OJjHl3MvdXs_i-ve11ZWeKg4m8-SVmNENFHBC93jHxmLzXSHys__Fj1jqnbOUbt1CpWURItMWKJRlCHn7kgJwlk58AUJkuZCV9lIi1E-Z6N8w9eph3bCouFedim-rJmEEI6OdF3v7oyY8XtiW8bWQX_L6zQXKyPXnKqhMWhxE4AAq5OM6jpc5LIhUVxwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puuMnT651eBumwg8P0YZTgPhz08vvocvaMXhZBOO9V5TVbuBG9hbSu49f5Xhdg1JW9X2QHTnTY7YH9cNr7_jOBlRWDdXJDFBWSARr9FXUxzg0tnNAsuDDkPJx11-TsG1Pe6U4QjjLDfTH7ZzWCPc8DfOdJ_gMuMHZLOWPhWazMZoPz_Du9n8MelZ85k7i1YsQsW7unx_8z8Od1w82n3ne-9EOuGYUm94KWUx1_komVvPa8QsAEOLeaKGcVX5_Vo4OaMHpQMZIScyCKiMbZ3N64HHqTgMHnCMCewj6ZVeZRWRKdptm7gmKBuW0ydtUnu0eaICep-FiqrTZXrUhpwNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3q6OzGUzSlNro-M3Y0YX7uVSw_7a10aSQMMGjox2ba3jIevT4_d4W68QfYEZJIU9I6N0epQbis5UMMbQH5490YbfcRhTgu3kEeYnIbn07lQxwe1DFvg4LhbHaQEKFWekk3mUpmAVFVo1ys8ONZYZGP_t45BGN9_b30oMVHjWuVWlPfAE7p5c4Gs7AmUT1Dwh4168ExVotc3Hd_0TIqpWmCVQPaHY7X--eZzWAJrsUGH_YkbaHwi6tJOgASXgwLxzk3IWjlVHOneGgMbCpg5B0POZG11LLrQw5vsZj6d32xCdMNTHnORx79xgOQO-RoPJsL_1RmKdoKUTO85NCJSug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv2ZM5YxtQuOAz9lQ438wWywnISJalMEfPkCnm7zp0JWcgNvDf7OHQjTeGoivchHGSkKeipoV7B9mkiQMdJDyl2lruWmbL4qGUnowOMRQV0UMOnX-328RGCzRwVH307kmsy3_XtcOzjV6QTxO0JwBzG9wOoCY1wtc-ayadRQssqvGI3IAu4veXeyN_r4gIcvrM7Ms2fHStMovqAerZq53LiKLxJZa3tUfuwwYL3ou9ePCIh5oI8nkfAe6PmGwgk6G5vnj-2XghdKiVOmpFMa39Dn_kBGMFs1qA5Jens3A7jE2GWNGn2u0BGT-d8zsFceWiVnHEj9fWSLpFwk9BE1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=NrX6H9rFhTJsuenC70BcCu7oXekcPyjoLis8FjiG8cV8-NgiW7hBfmafB4CIauKOHgmGMOAb4mAUyT-8BVeIvrlNgyANcv7Yd2Sw3rTpmBQ9X-yQdvKd8UfmeudyTWFvJqzGbdwrViSqzZN75Sza5IANBZJji7g9YBAvY0eUJNg54n4Pn8iGkldU3BEUcJ57qJqSLRnIacgIcRaNoDXbApzp5wFnMXSAYnhBaB03fL3Ph8Zy1vo3vFfGSUaEnkdyLgXqq3g3kuWs26qT9PoH-i7XBzABQMJBpsPbxxgHNKtcJliFh9_dF2vOixcoCPJqhMPvF0QpuSwwF-N_liL0nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=NrX6H9rFhTJsuenC70BcCu7oXekcPyjoLis8FjiG8cV8-NgiW7hBfmafB4CIauKOHgmGMOAb4mAUyT-8BVeIvrlNgyANcv7Yd2Sw3rTpmBQ9X-yQdvKd8UfmeudyTWFvJqzGbdwrViSqzZN75Sza5IANBZJji7g9YBAvY0eUJNg54n4Pn8iGkldU3BEUcJ57qJqSLRnIacgIcRaNoDXbApzp5wFnMXSAYnhBaB03fL3Ph8Zy1vo3vFfGSUaEnkdyLgXqq3g3kuWs26qT9PoH-i7XBzABQMJBpsPbxxgHNKtcJliFh9_dF2vOixcoCPJqhMPvF0QpuSwwF-N_liL0nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIsSCb36fo1rgDf4ULgwT7hV4OCP9uZUbmEekk5zyjMTqg87l9vwJBR3ODS8IhvkauRUzEKOzwreCBEmTLJFrgMTiOizP7yGXFcA8HlWgDm63r2NhStFbyx4WYBnv1GeGN7iz2CuZnOGLXmjC8GOMs5F7KKx1SSFoWQDEZV5uz-NcNLfkhPCO-vJHFQ2aFM7r_GAbqdizs0FPXF3olfgKtIUZ8-RsA4_fHatN5VSZQJ5l7zvEBrMppA_ooHiC3T--9A4zdhaAW0_nxWdVzkgMo0tVDqpU3wLIeDMIRxatUwgXQo5plzB0ipKXg5kW-Giyoxfy0DLT9rEkEbj2L9gYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9NghSB-ZbuC9C7zw_w6IGC9SgwsVMDlnxkdWKBocn5TdXHJH1FYcWlphk-LyPhdmt86RmVEiIwZnqkItgT1-a85o4IlDoe4qWcJbwr_FZEv1AS9c8bJ3Tr_owsr3kceyCc1e0N3i6JiJGOYNhIBEe-kmhqICWYpl2nNJnSxktfjieaUGIxVOY5dnVNmNkmsJD0YAtCqn3sPgRlgCDXXxUPQ1Z_4LuY-7VQxRmVkyClshz09j6UesJSh3n_5tcWsFqnIEhBL_QY65sCu6PWjgadvQkiz91SmzNbGxQfR6Qa4KbpvdDdI1c-JAHo3GKEfJ9k99uEKnVFGngyFnR83Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=DHgfEELECk7ChhVVXy79hq4xWajwFZ7sM8iHTLigkuRr5hEXx1ylAHbivVgWFclcm_Y9hm6f375-pme2VetvYiSGjZGxh81p4-_HzylwBg3WH9b1759LOFc4j39ESScHCZGjd1IltXVB_fM4NsLNBR-OP6__WgsZDWTtta25wpGmRh_hZVDbPnKlV8LI22mINmfDsP6jldLXMruuUpJupgcdlesgoRYqrYc4sc8rBJpghE6CiB1H_AQRSoJi7fL80fMLkbExurKZPBWLQs0O-xK9BJFCMGmRemfTVEnhj5UInyuS4-iT9kbuznMxfji9p-LlEwZC2RxdeU_jDOLA1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=DHgfEELECk7ChhVVXy79hq4xWajwFZ7sM8iHTLigkuRr5hEXx1ylAHbivVgWFclcm_Y9hm6f375-pme2VetvYiSGjZGxh81p4-_HzylwBg3WH9b1759LOFc4j39ESScHCZGjd1IltXVB_fM4NsLNBR-OP6__WgsZDWTtta25wpGmRh_hZVDbPnKlV8LI22mINmfDsP6jldLXMruuUpJupgcdlesgoRYqrYc4sc8rBJpghE6CiB1H_AQRSoJi7fL80fMLkbExurKZPBWLQs0O-xK9BJFCMGmRemfTVEnhj5UInyuS4-iT9kbuznMxfji9p-LlEwZC2RxdeU_jDOLA1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=SaAmdpnyePTkoeLHVLVWHhc3h7qYHrQlXW6liKZphiy0MJWCWWtiOXfQ_37vUDlANRzH7Y2PUcAj6dpy3KdhK6AkqSgUC_abEVrDzcg7mgduwbtvJ-v76C0-p_lGkGPUKIOxsESo9t8p403wgXBfPapS_cCJTT7ncD6bx_Jbi8rRj5Sv0UKg1QGQ-8ATdg1ztC9K_jcwzvJhyobkOfTYFBdmE2_80AVFxp5oOypGg7vTZRsKsbDmywj4egecPPKxiYiP2oHfV-XjkPKr5IsXgbOvnHdKopUVZxtS7j38htUkxch0kUvOHsTA6d9o3RNKI097J5kwpaARRBZ-nqq6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=SaAmdpnyePTkoeLHVLVWHhc3h7qYHrQlXW6liKZphiy0MJWCWWtiOXfQ_37vUDlANRzH7Y2PUcAj6dpy3KdhK6AkqSgUC_abEVrDzcg7mgduwbtvJ-v76C0-p_lGkGPUKIOxsESo9t8p403wgXBfPapS_cCJTT7ncD6bx_Jbi8rRj5Sv0UKg1QGQ-8ATdg1ztC9K_jcwzvJhyobkOfTYFBdmE2_80AVFxp5oOypGg7vTZRsKsbDmywj4egecPPKxiYiP2oHfV-XjkPKr5IsXgbOvnHdKopUVZxtS7j38htUkxch0kUvOHsTA6d9o3RNKI097J5kwpaARRBZ-nqq6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=nnuYxKHSQa9MSPdOhabi8Judun9mvJtOX2oI0oD8WtPBCi-dyd8R1xgfMDFzlOdwz68LYnkouIgbTbfzFxYmMRdp-qjAYDcomYphDqxSovNOcsNMamk3Tvr0adNp8U9wDfsh-Ea6Veoys7aEh1ZFLe6WwH1Ww3eDxRkglSWjXDtnCMfsuKzwuCiy9Nd5a10EjrydQUw2SnqN-Zke5Sp7F7HD9po6ZTaPbKLyzrTSpeE8OMilABjT1E0pTqgVTqRsxDvdRbYfl2mMWow-dN5gKKFaj03WdAizSyKGWX9WpNOj6x_u1EqmEmdHz-rmgdh5S2gWgHWCYimEniCf5X1SyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=nnuYxKHSQa9MSPdOhabi8Judun9mvJtOX2oI0oD8WtPBCi-dyd8R1xgfMDFzlOdwz68LYnkouIgbTbfzFxYmMRdp-qjAYDcomYphDqxSovNOcsNMamk3Tvr0adNp8U9wDfsh-Ea6Veoys7aEh1ZFLe6WwH1Ww3eDxRkglSWjXDtnCMfsuKzwuCiy9Nd5a10EjrydQUw2SnqN-Zke5Sp7F7HD9po6ZTaPbKLyzrTSpeE8OMilABjT1E0pTqgVTqRsxDvdRbYfl2mMWow-dN5gKKFaj03WdAizSyKGWX9WpNOj6x_u1EqmEmdHz-rmgdh5S2gWgHWCYimEniCf5X1SyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5FtgdS-1zZbhiBfopeVm9wiSqURSBWC3uesYd9VzH2-vCvFUOEj_RSXIyFeVgmcH8UxhlLTO8eygVzYWdXWciXgG9C1zICczZxiy580mH-Jx2R371CEgcvItBmBDn2Mnf5W6gN1DUXNeuAfG2OL2fEr9RV_LZkvfrQ0SskYFcRYcy420tE8rGYRXclmH72aIZSpIZ8xwh-hLQIhr6ueY9AS0nn8IOSS7BPBXQUAgnfwoiL5N2TcKXbaI-MBJa9HROoPe2T0XIo7Y48Dc2wZ4nBFy0tgJfTSmgoIXL5glPMvmSzBLpb2j44EB7IcbJEBiLGpUJCVV5vltIc6_0gsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwHzCtYDTsxMlKTFF2SjdE-fxPTJKswEzh-AeIT93PL0_Mn56_9N6Hon3DgSM5tU0l_2WLjZXhMrfnbv74JZy-qW6Kut-z7yuDcQ8hcrv21gRhLPBoHt-r7MGR0jTlmIe4fYK6Dp8_VwV6n0irii0EvJ44iDNkg3HdMvuByql-9zXPjps-jDukpuKHE9TcY6y1hR6VDw3Yo0iE9CfZ1SiRQ7ap6JYsrP5HHiwpcZL5lXppY-FwGlPJAINGzJw9Xdl8kX4XlSdjBHdBDJwhY8UMGF8EQ3yheNfXgxu2p9SX9mBPvytPCo1vFwr-BLw-30_LgNzqcXvf8iMSeOB04evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24664">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad0hermrjx8bFfHul98GXT7CqfGqFvho3CBD-EnK1NshaKsCAN7erav0ThDd-RvTE7bQz1_dhdY5kBy9Of9KYRZmzB-zTfpVzNA9G1ILLFk7Xcv51bjwcnpuqWDOZ01vucm-Dd6rROrp-JeXzPxiE2oQcgRE7lWxFHRVqTZfZNTdUvwtZe9pkyPQ6GT0Hlb_KCmFXLdy1nVeoT5lYZaQvW7uuoh0RjkvCJ_BT8-6NVWaDyM6vdEYDIZ_Iwd-n1Da7CfkpKNW3jekr_mT5OcRZnaPi_zJ_1BuuJwflC78GralS-0_XtNiSPgRkq0eiW_MqfSwFZIUqCkxomx00ZPI1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از هر واریز
🤩
🤩
درصد شارژ اضافه خالص هدیه بگیر بدون قیدو شرط!
😮
تنها سایتی که
به ازای هر 1,000,000 تومان واریزبهتون1,200,000تومان شارژ میده
اینجاس
👈
این یک هدیه کاملا نقدی است!
✔️
هرچی شارژ کنی
0️⃣
2️⃣
🔤
موجودی خالص میگیری
👇
🔴
اگر هم باخت بدی همون لحظه
🤩
🤩
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان r9
@betinjabet</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24664" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2v5ag8KvO-cmSKnWqgVLopWlihOuGhYRdexwDKhFA8D-oVikOXMc0c2iMGfwGFx51NoK3Qb4bhIl1sYShYXeMEkvKy5AoDwEv9_gUO_FecWTe8ODi2tjURLpSdO3bLqIHSHlPh33x-pvAQPcKeRWh8QAeepf24YA6h1oeTgL4oj7mXiazorWagIDo-U5Hd3iVWFUwimTI7ZTisXvq8heHQsEWJL4EDm-pOVPizcmwIobwHb6306XbppKtPn8lvL_SsY2UxACGzeKzG6C0oCW7_cVSqVo90BuTuTbW1kt5_k5V9OilZaJOESo-83YuxGCEzJekDY4YKe4oOFqTMB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=vSc1wSDMiU4vtenzXzZa8mkzAp9qECoqFlr-SQtIPHnqMsa_PRjm9XmwcpahYQYPj5oQmoBsTudhF_oocDltrXiT1_sdlwlT3nlLJwW90oPUaZA81-pKgCU2EDEuNsl57CbJHULPnAT6vrMwDIEZUU_W2zFL17YlOAduOUWsN9iapEXpfDOh-W0w5I1xFKrR5YMI3wdgs3Sg36Xug1G89gUKgzFz1cuGkTlrE_eGeGSXHAAWz1GVZ5geStDSQYChF8sLz6J9Mv-RN4n02_p84K1cAJfZrlNvZ1hSffvaO8V6ah0VxzjPHRFcKyL3N6SzWQ7hC9RabvASYtvHcvoxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=vSc1wSDMiU4vtenzXzZa8mkzAp9qECoqFlr-SQtIPHnqMsa_PRjm9XmwcpahYQYPj5oQmoBsTudhF_oocDltrXiT1_sdlwlT3nlLJwW90oPUaZA81-pKgCU2EDEuNsl57CbJHULPnAT6vrMwDIEZUU_W2zFL17YlOAduOUWsN9iapEXpfDOh-W0w5I1xFKrR5YMI3wdgs3Sg36Xug1G89gUKgzFz1cuGkTlrE_eGeGSXHAAWz1GVZ5geStDSQYChF8sLz6J9Mv-RN4n02_p84K1cAJfZrlNvZ1hSffvaO8V6ah0VxzjPHRFcKyL3N6SzWQ7hC9RabvASYtvHcvoxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmllkOiLKqkdM1qcqss0fjzqtHGgCHZhWPRZsE3mP7YWDWISJ967EWptv6iAWstwZn548rTKkE2StBuOPKypK4j4DAqaFIy8vopCm-rc8oWI_ogYbK8eDz5R7gEqvO0i1jX1P2A__ipcimLz0DJzsLybq8lEYPRQujt15GbayYieBdYPvFoUMgJgHTEWEHoCcEWdJcTxGwFpPeffIT5mIOYvWSpfyvxdKS2J9sxgBzWlw3Lsp3n5nC3gPnuwfZHDc3tGs3ypgxixHxHLmW2IVmDYAdLbotbGdHor6J8hKqyhdEmlMH25Yng7MiV9hmGo8gbUDfxd22i2uHFHLeybzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jtmgq5moZ0fX3mfhCs3Zm4wefLY8_fIb3lzn2XjyuXxn00rkeCxhf698Ptq0tFDjz1BM1j8U94mNqB6i6MMXUwrmPUjnnL9dvco2h_n-FnJMjpKsE3_q_54nlOqppC6gI6MVKgTx0Irx9dHhdGtyoDbRtfpI2mq_QH4whIVIKYNnzSj1OqG16rJ4MMvnF3Z_jSmFRUxL_QPSc4R669ZBp-fY60d7H4OwwLQ02fwylHswoWdMDKlp-cdPkPmpicB9YiiAGwMvOA3Q7EltkTQIwQGI2tx2hLAWJqz7MMY3Z02BiHrTIFfjQTIu4C2Kuvm85KOjMxntxBiNaPPxJAqbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ_kUvWG5pYDW9YGw649ha5WV7goU0_je3hj3B7x2wxY832p6rQumrtdjanYfiIATnECx8CuDy4JNVhW5xmUBzlnYedq_9WYXM4zZwMf7lpArgGO25ky5S5PgSpRsVWpycXDvHQSpTlb7HhDlj8pKxKWFCnWQXW-j6rUs6QOXaGHQNblqNYwS1FmtjgH17Nd2V2aK8w94YKjs8hUu0IMLE5A0FgIeYMxuMH5jobJPGmlXxAVIgG6xo9aCbcoBkW3vD4XGGl49dLLfxQJ4vkQqRW13RggXohzlxzMtgaI0OTgUbjEWhrwHK-YhGr-50c2MjjvYdGkBbBpQMopk9QTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V874QS6eOp4OOBui1utrKu-tln8gOufhIXaSKhWwC1al6ivWaPokUPfDkzptiUwp9OR_88ZUiRQ0WoLDcr8kHTv3vBnoWyo3SrD5_t_BkvV9sYPunLqxjdjnBg85rDDflo4C3FU9Z8XyAZ36cAXSIFOpIsUXr7jKqmRgB_RI8l9aDXIBpUWYIKQKxWwgYq2FrrrAFUsrqK6mCfORKe-PtRpaRM1ibYHZC9Vg4kfQnIwy6uDvFmRAqPdn_nI5NIozZMryaWR7MaADqpj1hZdGtE-4GtA_B7YkMfZSR9xTuG2Bb1DdmTlG5E32D4TgE1CggmN5EuClgBvAktRWXHyoquTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V874QS6eOp4OOBui1utrKu-tln8gOufhIXaSKhWwC1al6ivWaPokUPfDkzptiUwp9OR_88ZUiRQ0WoLDcr8kHTv3vBnoWyo3SrD5_t_BkvV9sYPunLqxjdjnBg85rDDflo4C3FU9Z8XyAZ36cAXSIFOpIsUXr7jKqmRgB_RI8l9aDXIBpUWYIKQKxWwgYq2FrrrAFUsrqK6mCfORKe-PtRpaRM1ibYHZC9Vg4kfQnIwy6uDvFmRAqPdn_nI5NIozZMryaWR7MaADqpj1hZdGtE-4GtA_B7YkMfZSR9xTuG2Bb1DdmTlG5E32D4TgE1CggmN5EuClgBvAktRWXHyoquTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=oEIQjfhryka0wt2M7FXI28kM75ClIR6Ic1yVXufXFr-0_jo6f6vhjJk3yDBgYvkesBPN6MLXkMS3LqD-GSGI8rerQ-6s1QKH3fxqgDhzXPf7jWg1QeYQ2VED8NYrdNphyHaUb3UTRSrCaXDw4opf4ocTmGuSj5_42VQFOH4Z7xYZMcOrOuzb0NVs_YRYpSJE0lGVeT1LwsZvwrqn41FXeS1pcZs9UkSxzqPztEsvbM50GLa7sdn7n9IZ6k78gKs_ij1C4aYhQZd7W1WGbN6yn7EcDotc4eMty3ead_aEILdAZWC7pyUKVLNfVA3T-W1UB3QSTU8rMBdFDUUb_yMszVrmpFCKC5RcuXsbgCrxmQ0F6NUVnEJunNcCKlsIre6fXyYSkrMI7npOA3LEOG6Hlr4Rs6DtS4yJJ94ygu_1NvLUEG2s6rqwfx4-KEfs63f5pSBUc25CRm-j2QuG50SnPvGPAzBXQrnfEYjXu1xBpSau6IiXHRrzkqE3W5YzUTlSHPb3VcRmDVPB_uHYXLuaAEClXF282HW_AZev9e_v-RWCTaZ2su-zn9RM0D4Hrrobtd4QSBuLfggU-dxa1IR9KckCL1gK2oTa6WDPQm_RwvRQpnr6UivHQWNrojI1whezdMzI2NMr8R3UmRQ0Xogx-dnWs4YVahRRBWatdXiB07c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=oEIQjfhryka0wt2M7FXI28kM75ClIR6Ic1yVXufXFr-0_jo6f6vhjJk3yDBgYvkesBPN6MLXkMS3LqD-GSGI8rerQ-6s1QKH3fxqgDhzXPf7jWg1QeYQ2VED8NYrdNphyHaUb3UTRSrCaXDw4opf4ocTmGuSj5_42VQFOH4Z7xYZMcOrOuzb0NVs_YRYpSJE0lGVeT1LwsZvwrqn41FXeS1pcZs9UkSxzqPztEsvbM50GLa7sdn7n9IZ6k78gKs_ij1C4aYhQZd7W1WGbN6yn7EcDotc4eMty3ead_aEILdAZWC7pyUKVLNfVA3T-W1UB3QSTU8rMBdFDUUb_yMszVrmpFCKC5RcuXsbgCrxmQ0F6NUVnEJunNcCKlsIre6fXyYSkrMI7npOA3LEOG6Hlr4Rs6DtS4yJJ94ygu_1NvLUEG2s6rqwfx4-KEfs63f5pSBUc25CRm-j2QuG50SnPvGPAzBXQrnfEYjXu1xBpSau6IiXHRrzkqE3W5YzUTlSHPb3VcRmDVPB_uHYXLuaAEClXF282HW_AZev9e_v-RWCTaZ2su-zn9RM0D4Hrrobtd4QSBuLfggU-dxa1IR9KckCL1gK2oTa6WDPQm_RwvRQpnr6UivHQWNrojI1whezdMzI2NMr8R3UmRQ0Xogx-dnWs4YVahRRBWatdXiB07c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhonRnHharH5pCzWFUZ-htbKDIKsFKQApUf4wgjI7QgfZJICAvdr0uTYHEv1NoM6IFYomLW6SxPwYGzKtKCZVZ820ng5cdsrymuV_dUhCvzWB-7ZZa1nOwzTOKUrXB2CkJ8esIbwPLN3kZvXgsBbGmgDak6EjWZJDCFMKPgWv1xJ8Fq8NT_UTxyD5WAbVFhAK3qdQ0hF13YVJxZtoUCwY8VrcvhntUuJAxyYK_LUaSJdCD6q8C9f8n3TgbGJ0-vy94IRI-h6ZbtA8gWb29rnLcK8phRtGldLv9ejkWgZ_yvmE_iL5punW-Q-EKhA6Rk_P5YIyXrE04b67_FbjaQ3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=BUWvY5LsCC6mrFSLKox6T8FXfz8PEvB9va3eALSlIxw5eYNI6l4jjWelcXWJJYp_j5H7xc4jXucG-BZAULoODcFSwaJFpZl9Tj8DEfH4d3RcVGigbR6GxuzKjtcC91cio0JsS8fb3l5sypkDvY0OC2vPGtIG8ZqJTJDE0pQZzrbN0VrO7VKLnMLWYHBdsUoW7GyAVNb8rTef1OYYQ3h-aV5If_IS1aI0QyOUuMDP__70JVup1O1lxHT_cJOJ1pxtU5L5CP-PiLdihETO4ENa1nKGJjAsZ6S7djo7XXZIfTXpaIB3tlaBJc0cm58W10WXxzHX0XDESDAO6qGkTmPNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=BUWvY5LsCC6mrFSLKox6T8FXfz8PEvB9va3eALSlIxw5eYNI6l4jjWelcXWJJYp_j5H7xc4jXucG-BZAULoODcFSwaJFpZl9Tj8DEfH4d3RcVGigbR6GxuzKjtcC91cio0JsS8fb3l5sypkDvY0OC2vPGtIG8ZqJTJDE0pQZzrbN0VrO7VKLnMLWYHBdsUoW7GyAVNb8rTef1OYYQ3h-aV5If_IS1aI0QyOUuMDP__70JVup1O1lxHT_cJOJ1pxtU5L5CP-PiLdihETO4ENa1nKGJjAsZ6S7djo7XXZIfTXpaIB3tlaBJc0cm58W10WXxzHX0XDESDAO6qGkTmPNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgYbGyGDBIJaRcS_WL2DdIFCTZeB13M-hCqQQlvyw-pe50VY0XgOTXBmRjdBL8_dHbyYkI1p7FkOREoapaGbUCCgVjWSeLKwflsMs7Mi6two7fONCDzh4Au9iIzr3qIUQ4CULDESqVCU_5aPVzE93AskVlJc1R6hgeJMdL5co171Sbt42RZDTjPhgJ2voavPH9zoRyGrZW5BHU0wZDzWR1k2SMO3ErBHqaBHFV_p8t90UXJvW4xw7RVzBODFWj--9u8Ps06YQdsQm0WLBl9v-Ksc8xjNFP00u5Mc5ELvGhxfaWsuBlWKbSg0y0kmHiWwKCfKqeNle8etMXPN9HsMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGvncvIEdhLxqHBuoKy8jl2n_DIqebSEkLL8ngKesJ8vbTzgmpvbz6BvJIFYejUXme5rdoNyw_1xwUc7UyMKOuOe5TGx9-h69AyVlqxoWiVY6nrLLPSGMYRo97umw-j0KxsuG6rUL74X1IN9zuQ5dwMhcVyx5FwwurDLqLPHP-gg8hpf8bG7REuvEBCeGXPZ15fX1NduTNuLZVG3XJeSoEpNP3xEmSSgL-8Td74-QXrssesuHvtSqLiFogKKX68dNYBnnVhmt8qJXcZ_I2C8lsm-iPdSqOQcvoenTOYkwNSNQRkL8Q_JjDPcNxPvSXtSfIc2TMK9FtxWTlkyNXfvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=W1srKGq9tIqsrtH_ltZYS-_ehDxMSBAGVcow-r1gYCmwuRXGmu4os4r3L86tK6_XgI6_0gdV-5ckLEZi8XWHeE4bgS82ioCywxeA1_zVSK2owg0Q6u7sIfwci9KD-IjHmkpp93xRlJtm9-J_Nt-AogM9_Mc4toxPT0pAY9VgWYy8hmdA8tCySGd6eV_5gno5KYmAfiqtt7veJrKoMntJ8fv26ef86xXp_9V5Sr7Gdiy4yPgetT8JCC7mjidjQmeOHM4SgNiejWCIzYRq-ZeUo_eEumDQBT-JGPnVCKtGAFD_7zVs2tqbMIra0zg1kbNji5vv9qdWylOa9GRXoAhtmjGoGXqpyQEPQP9jUrXSEHqC3bZ6EkqIA817L_cdvCQMEPmj09dcvktsKEz12JV_uKAZbUcD0Bx5sEDixKRAzsBM05FJx3gCFH9B8F74Vahxn9S29ssOyN3_0e74pcH4qLzuGr-5yrU48eZEVXS69a27ywJsa1A6DweE2Aq9uhH7BAG-ec7J-Wa2Xcbs2XjV0F9hgcDum7_i_6WPdwlQqsAXcvHp0fCwe_kQEam1iUmLD6koofue_zU8dJB3y5Hktr--0dkDrMrADB9lRRTGMYpfosQNbqQ1JjBHtqOjmRvzJZR7KUDoiaxAxFaR1aV_kt4hzycuPGJ4rIzxJ7kPh3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=W1srKGq9tIqsrtH_ltZYS-_ehDxMSBAGVcow-r1gYCmwuRXGmu4os4r3L86tK6_XgI6_0gdV-5ckLEZi8XWHeE4bgS82ioCywxeA1_zVSK2owg0Q6u7sIfwci9KD-IjHmkpp93xRlJtm9-J_Nt-AogM9_Mc4toxPT0pAY9VgWYy8hmdA8tCySGd6eV_5gno5KYmAfiqtt7veJrKoMntJ8fv26ef86xXp_9V5Sr7Gdiy4yPgetT8JCC7mjidjQmeOHM4SgNiejWCIzYRq-ZeUo_eEumDQBT-JGPnVCKtGAFD_7zVs2tqbMIra0zg1kbNji5vv9qdWylOa9GRXoAhtmjGoGXqpyQEPQP9jUrXSEHqC3bZ6EkqIA817L_cdvCQMEPmj09dcvktsKEz12JV_uKAZbUcD0Bx5sEDixKRAzsBM05FJx3gCFH9B8F74Vahxn9S29ssOyN3_0e74pcH4qLzuGr-5yrU48eZEVXS69a27ywJsa1A6DweE2Aq9uhH7BAG-ec7J-Wa2Xcbs2XjV0F9hgcDum7_i_6WPdwlQqsAXcvHp0fCwe_kQEam1iUmLD6koofue_zU8dJB3y5Hktr--0dkDrMrADB9lRRTGMYpfosQNbqQ1JjBHtqOjmRvzJZR7KUDoiaxAxFaR1aV_kt4hzycuPGJ4rIzxJ7kPh3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=dtIPZht4__fPOLy8jan1Oot8S5DhoxSyoFqt7ek8IyH6E_TmWj5KJd26KVtOwsaogxRzkbWao4deZxvtJ0CD95JCa-Cy-Kr8oDy8yDsC6laqTj3dMolu1Y3BuIFBkLRHYs1dbntRyyhw7Y7S1-g0bmDlsKRVbRmCiKNSDhm9jZXxiUnZY9gqzvmrEOBTyuqTfdknerKaoLmUX7YNXqef6DDssI7XOSugrbPoOC3iAElMnM-REt_HD_vPVSqVLvvT3inLiFvAzg99wXiB4Zwf4Ej4BDXFbvWuXbU-e4W-2T5sLwWSjZbThskqStFGEI4d4mbAj0Nb3qaiKDI0JlqGww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=dtIPZht4__fPOLy8jan1Oot8S5DhoxSyoFqt7ek8IyH6E_TmWj5KJd26KVtOwsaogxRzkbWao4deZxvtJ0CD95JCa-Cy-Kr8oDy8yDsC6laqTj3dMolu1Y3BuIFBkLRHYs1dbntRyyhw7Y7S1-g0bmDlsKRVbRmCiKNSDhm9jZXxiUnZY9gqzvmrEOBTyuqTfdknerKaoLmUX7YNXqef6DDssI7XOSugrbPoOC3iAElMnM-REt_HD_vPVSqVLvvT3inLiFvAzg99wXiB4Zwf4Ej4BDXFbvWuXbU-e4W-2T5sLwWSjZbThskqStFGEI4d4mbAj0Nb3qaiKDI0JlqGww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmxbEetYcGG0aguT3zDYALWzasZmA80VgYIV6_mKEoAGb7eazwrKwM_hbd3ijZHerTvyoWDW-qTnTeERQsIdAoeCxl9HxGcSLoT_2lg_zG2re6WGT4qdhWlPEYuLy42Jv_M_BTKnVz7cD13kOrmBk2gZ-DyQYhQXhNmRS1xwMA88tgqDhsZzh5eJgHJvIbxsii523rvZ8mnxraCs0BTMzJu1ap__xK24NDLlutyGQBlWfhbRAKOKjQqpJeoLD4RFRhFs0h7RmqRvKXTIL7KMxXc1GY9y5U4n9je-8-Ej2DLYX4bdqLPQt8CG-R30FneEo7jQmUL7dRFT_2DepxXrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1_GnN08LImlqyHZCC5IBakWl8ZysPersSOuZnx42uYsae8Zz48ov5WiMYnLo0W4sgpfkB27bE0zad-jREsuqIrgmUYUytdFzCaCfAZHIOWUrYOjz8mkwWdUoZVkTNgGYh3WeCBo-dhavYm39TOLJIDtWdjMkypNEAy31zCw121ezjhxpthlGGjNzVbQupNFUrhohKgENq4FtxvMH70tRCiAhZvaRwT47t_k0cOrf6AEL1qMzNEnpoh2y6xOWaOPYEEVcFNA__uTXLcKfkAIiVemtHOAOVJ3oykKWrovCTBtdZjhBrXuNDvhTKxct9mLw4PDlUhv73yBt7QnX-mw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap6uVaF35tGBIiwOGBT2nukceFZykogrxADGy_cE1u1oI_HuZWtCJ7EQ6HHUn0pB1ABNtH2X3xPFBxby3kglHOp73TlkXFetjicYjt9ogRk6wH9kSK6bs5ty4dJvsbxxiEfn6WfehLVWr3IYGITWbNB_sWCd9LRAmleo7s4tijIZ2_fDNG1bbl28n11OrIRGZbrSsH-CdSqjW53X4lQfcfQKwiIIirHkXqv9FgAnQ8VkapqVRhj3B2IvBW3R0rnOIVelVhNmRa_-NLpgbCU4wZ6lTXO-U1ZWIsFXgI0cKnkaQPUp8cgGSUn0k1GXhP0dwGjaKDLlKh7K3Z3WkLWnBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAlEqKEly_lso0jxpTsbRKG8ge8VI74UGDKvCXbR4KXyqXukul9s9pXuxejCEPF4nGFwrQuN44r4pTiCBOIfYMdZLW4rLA4DDfgqCG0XRXuuEs9Y7c1VutOAl9fghCLzAN4IKlyy64ZFe4rxsjb6zFOmwSDAJh_GvD1pu5hwzptCMnNLu8Ij2H4Hb6xBA0a0Cp2ekVcYSfl_sYm0ycblXhIDO5IfG4Rzw_kOOs0q2t6WAbRU23Nu6y8y8yy--7AHnIjRIt0ouBoNvlH27N0bfWQtQHF8VOk9xI3pl9WFx56uAA2Bzu_P8q0TezSstxJnv7BEWCf7X8RWr0Kx3DFYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIOqq7KbDzNSHqoMDwyzZ8UAJieBCWUorRtvt9w5-32cdIFIukcs8pVdcWILucP4CoxQaQ7eS_B6bj0EK20R0q218uymVaxYDnh2TD5MEDNwHXvRx9MmGTQNXp8MZmDL88s90TCbm0t4qw85C0k8g_cSLbif_XqcbclWiCBKB5CAGb7QbnY6M4tCBVjE_p_YHafgKenRv6DKgSCKuvivZ4Kn1TkNJEV-Ox9VsaY0C3qfHodRWBIMRs_jgv2ZpSAFbXxtDbbzBd4xNYjwM7M23SlmWLMaxMIN1GjStSeGB8_IvI7-r1DzuSSwAKrinlkS147m7nChzZNeAXNc_Atj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=uRJZdcE8Z79hTGAJ5JS-WRlu-AItfZe0dmFX2BKCGGLSH2_CjkIwmV0cmHXfWp5uwJ8xueX9YpLr2lyDW8zpnyfGn2ZHRFz3gzZS1f1Zbs0M0UDFc-U6KiXHEoJCi1xpp4-RuSxNt5qjisIfw2E4gndhdaqt5vjaJBqx67OXLlIA7SUg78xghhwD3Wy3uzaZCuWILGvoTZXMZnPjQzjnZbNhvhLtpuZQ0VuR777mhZyA7A3ECOQ59pRjI7uNS0Bbh1PXWD05uDdffD1cSl94WwogMkGkvprx7CPK0upCnp4OsIJzYAfTu_TrZayxxJLYm7QQ-h7MEQDjlmCvhjC9tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=uRJZdcE8Z79hTGAJ5JS-WRlu-AItfZe0dmFX2BKCGGLSH2_CjkIwmV0cmHXfWp5uwJ8xueX9YpLr2lyDW8zpnyfGn2ZHRFz3gzZS1f1Zbs0M0UDFc-U6KiXHEoJCi1xpp4-RuSxNt5qjisIfw2E4gndhdaqt5vjaJBqx67OXLlIA7SUg78xghhwD3Wy3uzaZCuWILGvoTZXMZnPjQzjnZbNhvhLtpuZQ0VuR777mhZyA7A3ECOQ59pRjI7uNS0Bbh1PXWD05uDdffD1cSl94WwogMkGkvprx7CPK0upCnp4OsIJzYAfTu_TrZayxxJLYm7QQ-h7MEQDjlmCvhjC9tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff4MEdKRdHt1aAB6zeDjuwkhFpwyWFjs6AIlLi10pWVyLy_F3ZUu8cWxmDa2BEcPqypWI7BhQYKHQPixPq-pnQo-Gmik2yNa8v-E7tX3bbrqLDHRToDMhJcpZvRT1iEBipjrHs5wivlP9RKzpK1KGDI9Ibdl5NHR_VTDbuoXy-sLvX8_bZhS0oOyVbg02LXGK7n7JOte_ZJo8bDz9N0YO33xWah7Dobrw59vkpku6R4k62Bbyr74qocLWpFAlHNgHkc0hI2UBrtu-FRDDOHvSGmTH3bFXN4k5vG8awECaxodTD8qAS9uKIkj6GCxtcfQtV7K4bc7Mdx3DMbtcNeo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9MGoHGb-cDfbntJwQheSSfQwyXb8sJl4Kc7U1tQfAMUfdYEMdUsqzTOFKrtPje0J75Nt3tmt4lFInI4tFKSHOOc7P4lT3RCWuHdYd6x3daqYQj2j8-VSV6ZIQ3LTPA0rfXhoHEdoGQpS1NGqD9_cz1wsrzJsHB5YJEL08kO5Auk6848lCPDW3OpHTBmhtwdMu-V_WIkId8fzysIQrTFpH8-95jUQh_0JoOWFui-Lnfh9M1pkH7ZmHg7uMCTKL4TMIsf1zAlQUyWKPetE1m-BelifH-mVhpogWqspNUY0tBDvNskcbrpnJyzVmkbt7YLSrpU3K15k4J4Pza3WFsOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCHg9HFAauu_bW9UMRhFAURI4m4B8MvAi2U2PAWhMO0dCEAeDKnthdeQpV8QAdA0BAC1S5kQH9O26go7QrcdQtGbqeuJvbjVK_dIfNJ8WcO9Z7fmJpgevZAtPZwpdvc1oQvKsWaIotZZ5bjZ2ImPwajIodtmYnzcYkbcnu3xp2z24i8eWY652YjeEKWT__rrKaSmL-rPRBp17EdqOmWVAWx1kyIM_LrEqGjSGSoUFltQQ1rD-HPIV2_4GxLSmgND5g9qsAvVmy80yMy6M1NxLQp8Z3pLQL1qaHri5ziWm7mUqIlyfkvAo9FboVckIMDWQhUfyLN2tFjenlAGm4Wk1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCg47KGm6Ylj0TTSWDbREEWItn0TW6b-YVCNubHiLw1p49zwSsZCR9owhJOI7eK8MaFL04J8ztuKsZGZqek9XGTcf2O8ZybZbDJEiS6-MQ48U6FzuXqB2i4rB94lBumXoaw5HJukEfGoWIWq7lNLe3vsHDFK16V4hxu-WiBIHPMzAUiO-EPBpTAjpuKj86bBIQRpM18IZnpFNaxS1TjqWlACs0_v2VGZ29RrtCbu4r3EoMZ331_SP5SUSxwpdlKm6LPY9sq074chgK1F23dpFmkgb-QLIa0bFQ8GzkEFKhjICbUZ2mlAJ--rQXsupjDc7W95BumjBk6bHjobGghYyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhi-sMFu2z3OYMUWdziErmFIjkxuVQJP8gzIHJuSgA9MLI_xDMjeZ8AOl1ubgdaV6g-Ce1Pn2PwFTUNJ2koKwAE78ee5CfaIWF6N7YsnapW20Mg1etD7Qd2kZNsdML3i594-JY_rzSjHEClCtboHhHQDNzOzxXA1LF3T9lljtTQ_NaV1i-pnk4yCBgHVsamt9-3WICm26NKuLN-aMsCDkHg5OnzzWrU72Z90wNmZRCu3tdWETnNOnZu2-IAq2tlBzxUMA0zBYe3vOMTlO9KWGl5pQ-eBuDtNOjRjPp3lhqgrmueC7hW-xYjfO32lG3JO2tYAUTTRbYsNizqvYuayoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🆚
🇲🇦
🗓️
۹ تیر
⏰
۰۴:۳۰
هلند
🆚
مراکش
📌
هلند یا شگفتی دوباره مراکش؟
⚽
🔥
هلندِ که به عنوان صدرنشین صعود کرده برای ادامه مسیر قهرمانی به میدان می‌آید، اما مراکش با انگیزه تکرار شگفتی‌هایش، حذف یکی دیگر از مدعیان را هدف گرفته است.
👀
⚡️
لاله‌های نارنجی صعود می‌کنند یا مراکش همه را غافلگیر خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24634" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0BIGyon_heXv6QMlaqQxZtFlQ-dPsxomKV5Pno69p9-ZSazHctpYwg--1sJMF8qO6GTPPewpQDbbdhO1wQBP8_vv7tjN0hHlqx5GrA5cMl4fXipKCJHM81SJd95SuYykifC8_tvLwRKH2LeNFgBbcptf4xbvVGwv9ndMTDLvNSz6lTpf9K0TrQ9ny64Bx6gDynVPNbQt842aD5C34-iFU91GqLwaZBoYWq_wbV6g-9sVdSH2mNzmnAaMFXOQDZ6tIor_T76-xxZSWNn_-qB2z16E_82RKH771Evix800-ECsWHiHwE8_KqBWm6NDKjBwXdZClqPWSgHxXPF_breKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxTy7SvMsYHPpKWL7dI_-o65lWT6kQ2o0uDVKTiBLo5NVf1tegKHct1sA8-SaRLek_cZMEVHHiYPE5WoVkGGnXIfAQksK_IrtNKDz4Mk0OGxDy2Own0WyAqBIsEmBxVfXW3ALdpiG0CI5Est-Am9KTYvkxAJQe0DlHEzLQuaf47DZaCBG0njpNNJn3YV6QzojhoBWF4yq4QvnUqIUMlx9p1OwlduGrueJifhnHm1fFVkZbFqu7Ji_gjSJFqjZkJCUVmIy6Cm3nTNhj0KRQ5JiS_pZLr_FnsZ3EeMI6plVp1p6eFo1uqqG0ZpMq9hdYyiosEBNvGFlQs7MwRZNrUunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=WHZ36P3TdsVj5izhMzEpWSJbszP1UnvYrzb1knNwGasfRinIbGfO_IbCrwbm0oEckebUJ55gin610gxxFcOUTR2zwZTJAB2-crpBq5smQa4QnVzZUbSHDDixaCOihh7EJCOM8tDhZQr1W3QEEYpIVlk6dfop0xlUKsAXtBx3aLToTda3qMojvfoms103tR31kHKvIBYr6cX60jwvWEnDdzWdN0TJwpCu2iAxUkmvOUB_LlcsogCzEE81INhsnhPkiGz_321KwY7hhSc_b-XPtKz3Fu0GZud-rp0vTpRj-dnDYTZI7nUtV_E0m6_7lWVBDfNqFdyLbTsTa6EzZSvooZuf81M0WzNfCaQuxEGt5v3Vxb89JGIwWL1_Sq3MrG_nP34Bo2zK2gxUSkYEUg71JVCNIihB99Z2Z69YxWCizxEs-0YpEDWdqG1nYBYL8L5xx4Lhk7BRi_d4eYB1W-gOcgjsgbA9sVspWGspk_YIgXM9fvRgrSgleMN3Twe0uu7dPLy1vR7BRlvRUrqkDij4hpYkhOzqbJhbplLfeOH1XWVbNf1RVriZfnrr2aDP4RXG26JG8ZEYU5tR3LY7W6eaaFAo-27IQuQHuCX8Rljx4CpG9mJgDKOx7-XWh15mXh_n83gZ1joavqImhjjwUtzat3nV1AmXtutyZAT-laQciwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=WHZ36P3TdsVj5izhMzEpWSJbszP1UnvYrzb1knNwGasfRinIbGfO_IbCrwbm0oEckebUJ55gin610gxxFcOUTR2zwZTJAB2-crpBq5smQa4QnVzZUbSHDDixaCOihh7EJCOM8tDhZQr1W3QEEYpIVlk6dfop0xlUKsAXtBx3aLToTda3qMojvfoms103tR31kHKvIBYr6cX60jwvWEnDdzWdN0TJwpCu2iAxUkmvOUB_LlcsogCzEE81INhsnhPkiGz_321KwY7hhSc_b-XPtKz3Fu0GZud-rp0vTpRj-dnDYTZI7nUtV_E0m6_7lWVBDfNqFdyLbTsTa6EzZSvooZuf81M0WzNfCaQuxEGt5v3Vxb89JGIwWL1_Sq3MrG_nP34Bo2zK2gxUSkYEUg71JVCNIihB99Z2Z69YxWCizxEs-0YpEDWdqG1nYBYL8L5xx4Lhk7BRi_d4eYB1W-gOcgjsgbA9sVspWGspk_YIgXM9fvRgrSgleMN3Twe0uu7dPLy1vR7BRlvRUrqkDij4hpYkhOzqbJhbplLfeOH1XWVbNf1RVriZfnrr2aDP4RXG26JG8ZEYU5tR3LY7W6eaaFAo-27IQuQHuCX8Rljx4CpG9mJgDKOx7-XWh15mXh_n83gZ1joavqImhjjwUtzat3nV1AmXtutyZAT-laQciwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBmK8enFvGH1HkJcfBp54dskD5cviFrz2qjQL1_NdZnpyYjo8W4ta7H_wi0cGpfA-gvTJWQ-Zte3HcMfU79-PKu_YguIs_juU_TqJKQeUTx5TI3U9GrmbbQXT1PIuBZr-fORU-eSYxYxcRE9HW5DrrAp0WEPBIOWMaKnTJuKFYhMcGu4C1ycKf4sLyVw2iVKFEzQ7vuPiopyqm6rciiOsuOuyBahhpY_BUUeBz4ok4fYsqDv3q8aGiuox3rB5Fn8BRFwIQ9wJg7vwEyCj-_WyoxHp40accsPQuH5B17kHiobrrWm8n-6Pl_BH4XiNxHmf3r05sF4kfLeHMyeml4ZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=F163PSFeRn7cy8V7OWO-K_uEkfOM3uqdz9AkxXWEAlKMetV_mOGM8JijR9b3O7Zpyv8qRpJ_ts_QMVRTxAfWJaGAIvzdG6oLeVEhB4phea42KJ2sWxb5ZGT2wO1MEc1pv0OHk-a8Vz54Eg60yKM2EyGT6BnVAExDOGqYL2zuQaCfCjOl_JexHuSP7HDB0OKZcEULKywNWdnwLv76w4SmRl3k1oeQ6KM_BKiHrwW0d5lR1tOtWyYazOQgnQ-I94TFcSfO9uCSPl7cgpfH3q9-LezveNh4WckJBxp-EwRBtpaEL5JSv0qZw8aDvL4JTmV_7AKrZRN-Taj5emIgF8x24Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=F163PSFeRn7cy8V7OWO-K_uEkfOM3uqdz9AkxXWEAlKMetV_mOGM8JijR9b3O7Zpyv8qRpJ_ts_QMVRTxAfWJaGAIvzdG6oLeVEhB4phea42KJ2sWxb5ZGT2wO1MEc1pv0OHk-a8Vz54Eg60yKM2EyGT6BnVAExDOGqYL2zuQaCfCjOl_JexHuSP7HDB0OKZcEULKywNWdnwLv76w4SmRl3k1oeQ6KM_BKiHrwW0d5lR1tOtWyYazOQgnQ-I94TFcSfO9uCSPl7cgpfH3q9-LezveNh4WckJBxp-EwRBtpaEL5JSv0qZw8aDvL4JTmV_7AKrZRN-Taj5emIgF8x24Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=PwwZRo_5sV3zeFUg0Sq6aAj7rHfC6ooel-9ZyQt7lE1NU6Gfqp1aH8VmK2BEL5u1-bp_N7eZsjUW-cTNaJsfdAlq-UdASRTM19HXCy5oWHgYUgytx60cgzrnRukrVjrYCFZDEWuwyZ6hzwEUmvYHGBQ6qgVkcdqkBkMtxNzvP0lpNNhLeWJjPxz4JwzRevrJMOysj8dd_97t2EKDDOinE6e6acnBci_PtmAb-1HcYVlhoDZB75nppSZ8FvlgpPHc-zBYOupaNqe3sscnmLT1vWDuCfWs8LVAzmXAgJJy-pxKDU28aEaztdEdLp-fPf6aviabfjUL10uHMmjm7nMCCEDXt0Lk-0k0_ShHfIE4jUf9a-TCpDNx3LzpnkOStwdnu-hU8GZ-5jY0uCKHojv43iE456VzHYwLRP_73TPsf0t9uXnwUHMB9zEi5SufBEpEJk2P65YEdwnektpBTDzVqm-NkE8z23g13cEq5JegbxOWaVd9f56FWr5RmR-6VMPCrvDBrZg4LDjarore3XcGa3jfh2gmILfgEZkMtf-8vNLAd1kLwZRPYDaw9dN2KQdN3UiNj4ElrotYmNDCDJn0eFyALXcozQLdyp6gVeU4jzFKX-_ALMTvLTsTTtoNZpbfDZiWhlQOmNFYRxGvQxNwDn5Cc7wQDPiQukw3Nx60Hxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=PwwZRo_5sV3zeFUg0Sq6aAj7rHfC6ooel-9ZyQt7lE1NU6Gfqp1aH8VmK2BEL5u1-bp_N7eZsjUW-cTNaJsfdAlq-UdASRTM19HXCy5oWHgYUgytx60cgzrnRukrVjrYCFZDEWuwyZ6hzwEUmvYHGBQ6qgVkcdqkBkMtxNzvP0lpNNhLeWJjPxz4JwzRevrJMOysj8dd_97t2EKDDOinE6e6acnBci_PtmAb-1HcYVlhoDZB75nppSZ8FvlgpPHc-zBYOupaNqe3sscnmLT1vWDuCfWs8LVAzmXAgJJy-pxKDU28aEaztdEdLp-fPf6aviabfjUL10uHMmjm7nMCCEDXt0Lk-0k0_ShHfIE4jUf9a-TCpDNx3LzpnkOStwdnu-hU8GZ-5jY0uCKHojv43iE456VzHYwLRP_73TPsf0t9uXnwUHMB9zEi5SufBEpEJk2P65YEdwnektpBTDzVqm-NkE8z23g13cEq5JegbxOWaVd9f56FWr5RmR-6VMPCrvDBrZg4LDjarore3XcGa3jfh2gmILfgEZkMtf-8vNLAd1kLwZRPYDaw9dN2KQdN3UiNj4ElrotYmNDCDJn0eFyALXcozQLdyp6gVeU4jzFKX-_ALMTvLTsTTtoNZpbfDZiWhlQOmNFYRxGvQxNwDn5Cc7wQDPiQukw3Nx60Hxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZccMf1fVTAzUweI2XbIRiIrv1v-J0N4XoXOh349KKMboQeQ5tO7YqJEIGHdVzlZV72n3rrvns2guGTPxsVIiR6bWCH98deSwX4I7Mzfd6DbDP6X4p94VnxgGFXYRGULx6nxic2QUNqZnHSJy7uI1xFP-Gh7G5PXbX4gfUARZe_1Kk5L1kCDT8R_zOrsHDiCsdICD-HJamHA0r6XwgEIaJeBk1QiDByh271B9yYM3SvCBGZjpcWbmrtAEaJa4CB4xk8pAMqRAQA713piKEI0R8FP0ydnrzrH_I0rS-giLwxWb8oj5y7NYWd6X-zbCibCiIEyMCflMhtEEPhsEMnBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=h_zEh6v36r0QfqeOLcaLvj7HJYpwgICBzvxrTHVgB5NoJLT-k2-QnbSUtGJpgJ5xsT0hHmky80Ei6MIb2_24luqhacnumCXbkxTQJlrHBRg-F6ooLVFAHL_VkMPZyMwWR4hvUuMxP19uuCiYPx-YPC-pZXtmkCS-24qpO3jJtiOCYhNt-WTyqBTdMwDVQjU9_z2VgTlZFRDBpWEEBHHkERb9dHVQ5C15brtNC3FS-t4SBm2W05_lz_CfBDgnkOSXY5vPGKF2T-NjXzqaBV8OJ12yBCKFYi_qb9AlRJGHcN7yFoAFtaRB4VurvMflRytHfb5lge120LhDVaEvRYGH3i-iQUqzL-iSokeU_EpxRIbM2U-Qmj6d4mHF03S2BuaKwEjOJ9MvpoGdXfbF2290LMP5E5LsZPZtX61cop8SezXyEDGczB95is099JAGMaPoftFrKBj714yjuWpuPzMZhgabXwfiDn9afL1geGcTrwCEEPw3Qb4KPTCF0DeeNMAFaV4UV6OkhHI8Z0VDf3BhRorN_2VkrHsSgN4t4tH10FYNN6nokgmMgret6R_ZBWAg21N8wy1EF-G3pxOKhkSPfWDDO9DrOu9UgXkwwx7d5xPfPirpkmtFvCYhXcpZiU0tO6OEdWp7m_97DZQPCAb2nP4zFT4ajmC7voDMXs8mpiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=h_zEh6v36r0QfqeOLcaLvj7HJYpwgICBzvxrTHVgB5NoJLT-k2-QnbSUtGJpgJ5xsT0hHmky80Ei6MIb2_24luqhacnumCXbkxTQJlrHBRg-F6ooLVFAHL_VkMPZyMwWR4hvUuMxP19uuCiYPx-YPC-pZXtmkCS-24qpO3jJtiOCYhNt-WTyqBTdMwDVQjU9_z2VgTlZFRDBpWEEBHHkERb9dHVQ5C15brtNC3FS-t4SBm2W05_lz_CfBDgnkOSXY5vPGKF2T-NjXzqaBV8OJ12yBCKFYi_qb9AlRJGHcN7yFoAFtaRB4VurvMflRytHfb5lge120LhDVaEvRYGH3i-iQUqzL-iSokeU_EpxRIbM2U-Qmj6d4mHF03S2BuaKwEjOJ9MvpoGdXfbF2290LMP5E5LsZPZtX61cop8SezXyEDGczB95is099JAGMaPoftFrKBj714yjuWpuPzMZhgabXwfiDn9afL1geGcTrwCEEPw3Qb4KPTCF0DeeNMAFaV4UV6OkhHI8Z0VDf3BhRorN_2VkrHsSgN4t4tH10FYNN6nokgmMgret6R_ZBWAg21N8wy1EF-G3pxOKhkSPfWDDO9DrOu9UgXkwwx7d5xPfPirpkmtFvCYhXcpZiU0tO6OEdWp7m_97DZQPCAb2nP4zFT4ajmC7voDMXs8mpiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LghD4FJjVF6c2zfXA-10Qjkvi8R1uVFXMhqFpPT0iYlVVliypEQypOx9qVMM_FFoXCIZfLZGPsrDx0EdvBXavpGqe5vcB-4BCIBebbNtCU7cJ1Z6e-6omJTZ5DFXG9ovMDlWdJK3irJrGMEaW7uJkbuKmjAV6L6EjujBAhnkCAXaEHDhVLQvXN0Pd_e3sk1OB8QxaIkPhaPJmp0QPI9IeI4PhxNvDEQ77uXMz-BeFw4bSMVpWMBTpdejQoea_ou4C_Ez_NR6J6CDXdyWJib_hRKp_40IC9Mxn4rpUXBhI-UUCPO_CoTC8fqDU_xtwSfhZsSO7dcWwzpu0m18JUYagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFK39MPp2Pgds1jCsg766F9Nu7-sxG2kWPHy5NMvM3zq_wIy5boSvDuC8yNLeq5u0oCKSLzACRe0DZOZMMKrW8zLkyR1JSXTzc-NkWxDzz3GEiNcRzXMnALtXsoc7G5bhOq77dap4zC1bHik4tderTuNHX8v5s2kXzDQMjl1b07wzLAb0Edn4XnNN3ElNtj5V0JjD0DP0dlJzFE0fnLi93lpeEk9LYxFi1IOxsCVh2xt9qCTmIT7rwcSje9I26NBlNAxJsdTmWHUCzEiHO3KQdGBpo4-w8nqbvf-fhbNH_OnM31Kq-_LT2APBI0lFzl0geDuNUHzHXjrdu-_PZQKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cm8RvvhsDAv-PBY4lgALUSlzgHyF_88Ax_BXjtLpm_hcTz6los_Q07zHWe6bu-qEayzPhLz-k8blYZIDBs8QvCUmVadcLtRgeOlrkF8jtmTzTximCUHtmqeKk2SsWfPPWauBNSmkwy379zUNuivmHXS8opKKZmxksBfIw4ohQkMaUmQRllCBTSAqlHOV_K0g71ACX3KhXLVJoBl9ExV0mucWImzcwJ65TfK5A6vYSjyzGw7XdYyQ_Aqvjh8ZS34uXQTVxwkGmusHngacXhlCP_4xkizFPpeuByJPwdvwwa6R2Fc1fcPhtbuav_mdzWdCq02hp-b2DjDlkDQ7ddl-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XH26wCgguuHjzNUrgJO04ZmTwF66I2k0BcbD3LOJ6g9qsoRl07PxrcVgbmFxAI27Zbi3_fJ4xChxEu6f9DWk_KqdI3-FO9VYeO9IP_K8oLMS0watBS7gb0VdSEpX-7PNDWUOQZ2qmIeK58DppE6RJRvTC-18ikklRCFzla5dcsjeHZ5EpLmL7ek1nT87O-EqExEpNojHuXP3-WsO7MHGU1knyd8WvDPlFE9p6H1R6Hy0scVH3ViLLz749vH9adCxEpNWAiWarFyYls1jDh11HfDvD3YrFYUSSWtbnsy5WtDzsEz8y20EVd_yssh3SoFGXAto8qW9LV6Mj_8Rh5wkmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl9qU0WYTgBxes0q-xodtEs0TztbBR_DgcumHpTwOvRJf8eCjEjJbUK9klAtMKvlDIieyUXTdxCEbVSq3JwarqKXhHPmNIbtNzOUgDa6QOB-lSm2lOYS8_F9tfAmyy_TpPXdEJjdE51VJlVhMWSwQZeZPjcb4Nhq_ZWbY8jtSPKjVTP1W3OSqEB8HQKFmgX2opryIW34vlYObkD92hVfQqO2m9ETbN02FeTHzYwk7dIHJh_8v0d6FBH2SKJrS2WFkg-6NNoFM-Hv3nHEzB3vTnCQ5Y8EA2PQjTk8ydLppnEW0WE-uDH0eqnqc1kjYPpOs9AbFgP0Kxm577kSGINOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEPezBOtr05WG18xPotYYiEiuHuzNC7o80Qgzk1uMBXK2oty3KWx_wtepM0XU-cAFxXz0DfnKPeCYsrI7RmRFcw9yFSn1LLZIKwqHY9PRFNLibhCaay6pMa7Rt38GE6w0N378VrkEmhsqv5knu5ZR1kYwx9hJ6tz0OuzGnvUL49KOdTuvyqs-1EHkxewvboKxXMi_hYMt-jsSRCw1-eOhO_LW8JWrDQs6Fe_RKOsv-lB4U16t61l2f4srJfnpK9ynHZ3uxAXmUabGTBxSqx80eMN_7fErGQe0_MKOJLgak3kJjljDiWJU9140E0lJ1nybJgYMSA7uUfPv_3IQ-tDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NB9VBWSREVFQ9Ih6Y4Z0KSWbKKsRL4gBy14KHHZXEB5vkR-fFB9qn9l-nCo_i8PpuxzsUGGl7AFjf1kb1mKtlfc9ywg1rslJeJKPlnG9xUYI6jjxUiDUllkP7oqeeU1zpvDH-FoIcBHF_arIwakx6c04CkM7XmjbkpIcsCLZ1BsA3Tot9MZ10fgcKg_iPqh2wnDTFuvueZVWtcVdYSvDAm_up7ghBzs8AoFbABMM2NzpZ9cqdaJf6I4i-NG3jo53fWjgUPJfDDAg0HZ1qzeGb6hEq6oTKp0vIbqw8JFXI6lRH11q_GY9vYbsoAeFSEFFRYahMoqHg9MkC3YjshI9Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aH8q0pbDECDP5j2XdCPRbrCaxsk9afbd3jnrWI_zH3fwPCm5iwtTTdb-xYCwoFGifdXCOj7CUBGRNkhCg_nbHLU3DRCvtMBcCKxSM3w3BFChJYXEBqskw-6J6SJjsnMso3S3k3EQrVMjekvAIVeuH3p8idHNDoouxnOKMyAPAFa4ket4Y4HK39gMS0Dmw5kYcW_LKB_4dHTe2OpAuFCgrUke9rjhHxv8XcPKgCJs0qzLECLaMf7eSEZm1Nc9fVBBDtGURfl_KazGKqCybNcbZCkIAYRCGbEqU8SK_J1KicLvAfju5Bjz_rOsVy3a3H6EMLbCz5LBtRr_ul1YRtKiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFLK97SFAvfANbsS4NeY4Qm0M5lG_xI-ugrcs9ikO58s7xfdDUA3cpotZaEuBwY0x31MzebxsXsLb_WcDOYND6vCuhKkErQ5z3S1Okf-YxxJIaDTQAlRvBCS5Qc71FJVOlq7U6A9W6CO09salrCl0lU_i1IgWg7-1gHL3DCeZFcvufijuxSPOWH7g-Br7WaLP62zjl-PkBJXTSxaxOFKtmNU-Y0K0_PnKTC1r4fl2EvGmHoLbh-XIIWk3Q2sF-5tQ7cuXGew70aBHko7KXikxIRHK-iJdqwLiVORbtJKEmoV-8tVmZXxsSL7o6QORMmMEvLAymJujxjwYIBEecRP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz4YJh1tItA9EUucM2ZTN8XuiTrZMTDpkbI8GUHWtjef6IV_WHAO_Y8S7sYGeczp3meQAEBTRXHJqb1IlEaxYAth03_v1RJggqwJaZ0GXh-MtbAMnG0UbsYZUdMYSNjUq8LiLNZBmeNpa_fnlq0YQ-9dK2fwJm1z7Mqjtdzwz8G0LWkKtxJx011a65YgfWOd1rvp90EbBcwE99GBxlnkietKfxWnlZzRtE3hDNuMTrNglkCa_35gkR0pEJktKjkXb_f6aq-cpu7td_XRb5-2pA4SRqbWrlNC8aPCCmmkPYj1an1I7B7JJYwIRqsaJ7CqgaQ_FbH7SlGg69Cx--URdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDA3KSllL0V8b_l6qvYrzicrOGme3QHGsx5fW3Wxxh9wvScOSYGT64H937u2yTC0np2i9TZ-5gZwj1h2rNta8dhCf1UzeZtmxDXKy4NNwdnWynriNKcLMzugv_J3EwXmH3IPwGzFv7GvuJknpEmkw8BI6082jsBJ5Q8WZKiZaYMxtxDcwm1ME7cDf1ToPkHlMNrwX1ixk9SnRsvRka5apPECRa32uvjpP5Q534roRKyOMjD7xE20A86juea7e0RL7uqtw6TqNV0LKS_EOxIbbppNUn2CDNq2b1Z97_iis8H_u6WHiu2PvSquFLyCc62yk_kv5TkIvzuTiwHI6Ir4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAYLA3TTx2pNBA10um5AEqPva-J5qCXBjQdiwnjiKlXprrouWawSGKcv3YkH52-loR95ubFyUEcZ1wNRjApfJeafX2k1pY9YmD64sA-nhU7trf6w-yVouVXJvT69HuGbJXZf2uDxBJBx0g_ZDpo3gZenUhKbQ5l5Li0yMp3PH-4hBibn7URG7wq54G4taHZpR84CR35RZy68rkbI4IY6TfcxEGbiWM8KWOEaxLOxczS_yE39_9ooaq7dBWCEhpd8TNtU1Gefo33YwfeH7gUiraByiUkoH0UYbP2Pw2CKIRtQpFjR2tXHm0M1jrHR-4DweDHTfSFQOpHYW5zsVleEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=SlrejI8k3leowfT9Opy24i7LL6Gj9IH_B3aQlcSgZo6GSfyqe_B9S7sBsZJ1xfmkgIRMeZm1xyX74CIVWrjneXTw6VVUE-EzvNSgmjC0M8ffDtO6Yn6aHx-mpU_FrXTYZfpjhTp1D7DfLt9lGBe-f70kIKK5s_pqk5WjU6PJMthhFF9wLdCAaki2KT7eNgYqFLKjElwO24eeXIX8b3o4ZkF1Oo9CWxMLv2hJOav_2EXn3YJfQZcOHUTH3j9_7BfbYEa4R3XX8jKrTVg1w1XezYkrU6ayGA3CNkQeDKCYbcClDucb9Brnk92nmTPu60ghsTl60XZ9fZZmtJJzqEUmfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=SlrejI8k3leowfT9Opy24i7LL6Gj9IH_B3aQlcSgZo6GSfyqe_B9S7sBsZJ1xfmkgIRMeZm1xyX74CIVWrjneXTw6VVUE-EzvNSgmjC0M8ffDtO6Yn6aHx-mpU_FrXTYZfpjhTp1D7DfLt9lGBe-f70kIKK5s_pqk5WjU6PJMthhFF9wLdCAaki2KT7eNgYqFLKjElwO24eeXIX8b3o4ZkF1Oo9CWxMLv2hJOav_2EXn3YJfQZcOHUTH3j9_7BfbYEa4R3XX8jKrTVg1w1XezYkrU6ayGA3CNkQeDKCYbcClDucb9Brnk92nmTPu60ghsTl60XZ9fZZmtJJzqEUmfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B71ZYnnOUC14sXM0zQWutxDyeHfw9gfJPm-dkGlUmMEk8jexWDrNR6LbXykuFa6dGlK1B2BkuLMgxooqxrgUafhi-9AxsDcSHfWWQE-FSO9XCY3TktyBNZFK8V8sOKQ3S3zaNMXbe5fnkACkuFptztjGf8J5g6PRXMlGsMbNU8Y6VdBlrbDPGuN-IzeiM42st_s_HkhlxbLSUFHTxba3kT9mHN3s4ixQgRkEkcJ3drWCrrMpXzWXT4cwm4i5YWC1lfHHFS_8XhXFac0YPpq_jyBJzWI1yGtph8s7SaBXzgDu4MzNCiwZeuwWHy85SNHm2Hv7QvfBLbR6YVBU5bc9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq4eWFk3ICcHKuw9pyQ6aSIMQlLtpFM2qTXxfR0TlVTwhbWlXje7fUutF57nANIGUmVpuGwJrZQuHkpH4gNYihJpPC_blXCABK-nQCDoy9a7ZKDL8B2DWiTTPZqzelMsVKFDNqu5k0SPEDBFiKk64AqMemsvliUy0SeDCp3lVRRzHABh9cgh6QN4TfMhJIMN9W4J6L-jSIgOe6kqSee23Rq8HYghOkd-EkVkQl1SzeRh-FvZipe2-uDYvmN1mmYUEj9xmmorm0-eVgff3U-1JoYd_ZDlTdYU93hdWB6VnzXWmqOgSmyoZ0QkqekVs9Ehiks4HmkywNuwiCaOtUzXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrfSUqX77yY_VMUK-bT_oF1nf4y4bPpK4woVt7FI0Y6t6WWiDAswbiVoBgLX6DNeeMvLOw15_PPm_pd3Ig94NjHXUPwhevwgZO8FyEeQ_6TXb5TCwXBjIGQkIdwdIPZX_z66rTqul0bnde8eCHhvffqiKqjaC0_lSOzFqftKR1srWs_7BtaBEvz9gPMVyf-OhrTS8EomEnXL59KsIkyFIS-k0ukIqJY8dGHjZpjwAQ_oCI-xhYbL8rfQA_2HMIPHO6DPHEMGjMo28pt5bWnFqx_u9Kz-uSo23ZVhDJGu75k6KwBQ1Fv_jM70fOPLtAOJEsDhSajmvGBXxNL-CKlfDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU6NZOIJIvVHsoF1xZeYjiVI6kwWfiWrfJaDmt324vF-Y8ip5QnzSGLKXwEsWhkcWXqseaRVAn9HvsxV0N2333b5_fehWR2gHO4l-EjUfBWx1VqWg3X8Hd8pSLHmJj9U5PLibCVG20dQHRn9zuVX2IWhlF_BVNKRXb6z8icTOf-tR02nohQi2KTo30pTbnD4YLf7k_17e9cOn8whY_l_Pg1hnYYUTBnsjKasNoLcrMjYCEXDo7JHul5_JS30y6X4lQiZj6WPVTs6xR8B1WhzvWLJz38mcHXMEk20cI3AfdhMRBtFUp7N4bChOitrWN6amrG3FTz8VDWRbYnNOR2fHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn5P1KuEis4UlM2mmbuFIQ20PhXwBB7xwhEheUJ_srkeqE9AhpClepSepWv631Qw73RDE3k8POCof6tgY2CZee6L5UNOFdTNGsAj0qu7jlJUg1zTQYrtZHV_YTKjPcM6haU48kd4PYBxVp3tGQXZF_rF7W8lFt2N9pglwbgjDWBxQwhpm-5rByxH-aG5nMfYepekXarxpUFk2vt3LOOD1bJkN9aOJZzUPygcBjHgvCF68l08jLR7yavqaSU7yaf-n36UObyobCxJXKfFzEkNO1izZ-GtmMVXHsELiE5_3_PlduCkDgtpsT3TfRWb08Ep3qTRhCdT8LiVWhrR3Ay8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvluJjgKQszU30SEJLd-t4p56ox94ke9yxICb--CYULI12zxG75yeWhoYUHvDXlskNk1o7KqukAInx2BClNbNnyxrDKZZex_yLP1Eld5ZuULzjBA_15OdrsizvTTXvJnusam4ZhxUK4wYhDx7tOJhxvshVmPs-2G24idif7hvvjmtDskfwZgi53-Omk_EGLI1OIC8iHKRxtVjqi9t3CIBwvEpxuIiReyibEsGFE-flbZ6cxH8E5sEgidEfQb0nwv01PR-S_efAqyy_qVcbW_XBgFsbCwvYZIM0VR5IgwaujNBSh1modO_VsyY4lvKOSCWrExoFbO2sNNDoc_rcu-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=UUbf6hbbjLKV3wU2Up2gFodtX8xFmqhSGw_0Dv2XxJ7KaDy4x-Y1bTo-hY9mDj7ifuWE5I-3Q9PiNpJkr-z-3pPk0DH4Vyy8KjTrp-hp5X-UQR0b_lvdNFQtkKiO3dfopZ14zbqa0rYNhziN4VLqO0hlo9Lz-Ir-ElP7RkF2XGz86oAPikSa72DaRY8VpiA9YMzqzbe1Dz3Ulxj-50fic0ViwxEIadPpse_tKGrj770UAJJjx8Raxft0LJ_JwzOB9FwBg8HhDURtTjdP1AhG2sf9_P86JgFxYiPLagVKVhm5rg-Cg3LG4Pqujzr9SAdoaezZeHasdg4Nu8C-NhwHCjIit-CYiy4TEbpQafWpAhrf_SvlT7R8_OdyziwF51HzjAY2w9hgSrVgK0vYSyT1TAhgaJTh0jsQ9PqSYu2WLHspyExuayHnFBU8mvpfmv4o5bkeJAzZ2PqRVVX4bZnOR-02LmdJbs9BFEUDa9iDmkVpdPlxlIimJJKUaLNAq_YMXw4DqC23si7ig3WCOSqnm2AZDoB4_W6htaa2mYQtBnSbFeLMg64CplEHUm7ku4b4FEub0zKuJU79z004mHv6-5GOW6ftSMNwVs-NA_d81bo7Qh7X1qbjyPZhs-TtZpwd3xRwWagnESwtclZaow0OYNowJO_R8CBKYLUaTHnK6F0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=UUbf6hbbjLKV3wU2Up2gFodtX8xFmqhSGw_0Dv2XxJ7KaDy4x-Y1bTo-hY9mDj7ifuWE5I-3Q9PiNpJkr-z-3pPk0DH4Vyy8KjTrp-hp5X-UQR0b_lvdNFQtkKiO3dfopZ14zbqa0rYNhziN4VLqO0hlo9Lz-Ir-ElP7RkF2XGz86oAPikSa72DaRY8VpiA9YMzqzbe1Dz3Ulxj-50fic0ViwxEIadPpse_tKGrj770UAJJjx8Raxft0LJ_JwzOB9FwBg8HhDURtTjdP1AhG2sf9_P86JgFxYiPLagVKVhm5rg-Cg3LG4Pqujzr9SAdoaezZeHasdg4Nu8C-NhwHCjIit-CYiy4TEbpQafWpAhrf_SvlT7R8_OdyziwF51HzjAY2w9hgSrVgK0vYSyT1TAhgaJTh0jsQ9PqSYu2WLHspyExuayHnFBU8mvpfmv4o5bkeJAzZ2PqRVVX4bZnOR-02LmdJbs9BFEUDa9iDmkVpdPlxlIimJJKUaLNAq_YMXw4DqC23si7ig3WCOSqnm2AZDoB4_W6htaa2mYQtBnSbFeLMg64CplEHUm7ku4b4FEub0zKuJU79z004mHv6-5GOW6ftSMNwVs-NA_d81bo7Qh7X1qbjyPZhs-TtZpwd3xRwWagnESwtclZaow0OYNowJO_R8CBKYLUaTHnK6F0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
