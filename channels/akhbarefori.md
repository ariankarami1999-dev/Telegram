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
<img src="https://cdn4.telesco.pe/file/mswG9WrXWmyTnlM6inCcPUKERp5ISVy92UpEIGokcO7d9ep0KC2Bv11jJR6yxU_ahekZsIwnuek-wTbXb7JdQ2pG9eSluC8jf6ruPfLvJuKTcb_bjPfjE5FTkaUgj-M18QKmfglEOfbMEzcj_9pNuq7MhCOVj4uDfd2VMmcXhOTxHslKBmsmWGKFhDQ-XriC864glkL8FNu-5bnMVJneGSY7Rrz8evabqStrRSaKLfGzlgxpj26BxFxDjyHEVqcY_ZPgqguK6lUhi-IE57oXsgvkq1-vC7h9p8a66zfna5byc7f6sf0_pMGkyEhqYTVq5p2eju-m3f9dy1Z64W4-Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 20:43:45</div>
<hr>

<div class="tg-post" id="msg-663554">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dskneu5r6KDg8dieFVx2PWniMkLvwbl3RRTKo-NafDqFixp8Lnuy8hxkg02r-qKv-DJZi2Y28VG1TbYYRiBMflQyUeekXt_OhkRe1D8kOOQbXwYdiDZzriFAYes8XY5wc6SjNKSSEjdVqbVO7_lDYDKAJg1nblbVg7E9F8PjTQv2aSs7y4KDK6mZD6s7W-Bgiy0RrNSnpi7HL0whxmvuQIxmJ6YfxsxDp1_jHFfassFcsJkqgSnGvV3nmKGPRzineu55xf1xBM6e_8FgqGDdh43mwMZLSL0WSc_XoRsScgNWEKs-phn1N-HQotukteQ02hAlSOKTtfITCwWBV7o0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عکس کمتر دیده شده از داریوش مهرجویی، خسرو شکیبایی و جکی چان در حاشیه نمایش فیلم «هامون» در فستیوال فیلم توکیو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/663554" target="_blank">📅 20:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663553">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔹
خبرنگار آکسیوس از امضای توافق بین اسرائیل و دولت لبنان خبر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/akhbarefori/663553" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663552">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a899637c4.mp4?token=guYr6ws5KRzwU3BeNDH-lWAkKQVmdgD9KMU6qiTAHOaCv-JtAUBVWT-47YQ5CCfDRSeAkiqTd4fxVjk17PhPDJE-EOX5Of15lymvu9X9fg86OEIgoaYISycFAiJIX6UjMspZXMcc470sZlMcSH-I5YM7qmCN6qK6fU5uZgAZh_S6KVNJQil3fIGVmNIOWl0SVCV8Lvp1S-CYJCBkIeRO9nh_lhMG_knm-Spkn2CzAP1rLYOLtaUPya9IoGF5hyBejGBOya1jgY_CWzIJ_z3nPavoO9GV3rF1-YXZX8ph-IcnYY_pm00D_eQCITYV6ERliQ7Fz521inC6DYcan_BZnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a899637c4.mp4?token=guYr6ws5KRzwU3BeNDH-lWAkKQVmdgD9KMU6qiTAHOaCv-JtAUBVWT-47YQ5CCfDRSeAkiqTd4fxVjk17PhPDJE-EOX5Of15lymvu9X9fg86OEIgoaYISycFAiJIX6UjMspZXMcc470sZlMcSH-I5YM7qmCN6qK6fU5uZgAZh_S6KVNJQil3fIGVmNIOWl0SVCV8Lvp1S-CYJCBkIeRO9nh_lhMG_knm-Spkn2CzAP1rLYOLtaUPya9IoGF5hyBejGBOya1jgY_CWzIJ_z3nPavoO9GV3rF1-YXZX8ph-IcnYY_pm00D_eQCITYV6ERliQ7Fz521inC6DYcan_BZnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحنه‌ای جالب از تقابل کفش کوهنورد و دمپایی فروشنده دوره‌گرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/663552" target="_blank">📅 20:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663551">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfa562drFtfNpneBCZKLNdBPz24ys1-2vF7TCKuEt-abITZxUlPfRLKYT0-3RQz2hI_OOqlqFZNwif65qC3oHonRF0-RZtmwu_vle5Y3AiNxBoe3XEFrAF26pYwZR5eZTxZspJ4dCMhnLQV0W1KDG-oTWzPklPK1NfbWJXgf-WxHB36m0hwiT8o0NN_IJ_vPdEe7R8GJiJuGAX2mR6TsWL6vGRCxhI9F1iQWOfXEaNu77yyOTKE0WKMvSpj8D_3zTUJVaKRsmKm9FYYhHEDKRYQKop7uUfO4pnCJqMxgvXCb8ji8xzEAUOo_B5_9tVZ_EqeCBl7vp9WV30HERLJnMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
خبرنگار آکسیوس از امضای توافق بین اسرائیل و دولت لبنان خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/663551" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663550">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔹
پایان ست دوم | والیبال ایران و ژاپن  ایران صفر _ ژاپن ۲
🇮🇷
۱۹ | ۱۹
🇯🇵
۲۵ |۲۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/663550" target="_blank">📅 20:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663549">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4a710aedc.mp4?token=TxNfs8K6KeEpT9wozxx-AStbWOK9sfbxFk4lAyybSPcqDQtRyOkhlI21lqd09tFKAu3RJLktJpx4lGhcOH-fzJnJsf2q1rTJ-aGhNG_-FJDyXafsFA7GzIhJNIjZMiChmZdFbezVfA3Y7BvSNaOhFkm_r1nnKPmNbnAd5B_lhy5XtCrUS4JSurS2noRHCEfChFhFhv0Ah2EvndBa5zj2tj4k6ZOfNrrhIdlLnBrjSHyDoGXACUm1y3M0kb1aEfk20Yy9Y44yrETEdBsSNoXASY0RGoRIEy-3LCds2m3Isn1c5JXnKf2zrgs_Ffad-eB1ris_G9RXfoUyyCiSSmZ3ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4a710aedc.mp4?token=TxNfs8K6KeEpT9wozxx-AStbWOK9sfbxFk4lAyybSPcqDQtRyOkhlI21lqd09tFKAu3RJLktJpx4lGhcOH-fzJnJsf2q1rTJ-aGhNG_-FJDyXafsFA7GzIhJNIjZMiChmZdFbezVfA3Y7BvSNaOhFkm_r1nnKPmNbnAd5B_lhy5XtCrUS4JSurS2noRHCEfChFhFhv0Ah2EvndBa5zj2tj4k6ZOfNrrhIdlLnBrjSHyDoGXACUm1y3M0kb1aEfk20Yy9Y44yrETEdBsSNoXASY0RGoRIEy-3LCds2m3Isn1c5JXnKf2zrgs_Ffad-eB1ris_G9RXfoUyyCiSSmZ3ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گروسی: اجرای توافق مستلزم دسترسی و بازرسی آژانس در ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/663549" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663547">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4Se911q861nkHEKYvgnJ1VJr4_ISTSr-S57NiPBqqc9lXFKimqtVw1dOevMghNMFjSRa0jZx7KCnovSsGNb7o-VZ5cwwVTaYRP4jQy5u1oy37t2CeaGKDcNQu9PdeYLNdgDzbfYwgXfv753ODpDNUt9dzOKTgBdDFDzFIHuMbDNawEElpKEeyWa6qGrThFLr7Ygqy2i7gV0H3Q9MDHEVM7QhLcdMcC3qhBuCwOfnPbU_9wFpzKIKUBDzkrP18yXJEapxSrMFEQqfWxRekBAheD92MKeD72lhctskRJinEdCpveCzc7YcURV5w_MMfU_eMW5gOudkDxRRTmlTfo7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j75u2vpfRlnK8o2zH7ajBVPLbYEdKkIy-uKwHs6yRHVHqnNpQX4lNkBSLYdYj4frbh2ZsazvoJZSp2q8DgwD5elxm2dmRwT05zgeQDIMxUQCh_1J556onZcot5Ga-ByR_UxsWUrwpK96WRxTTFy2CNyktHlieh5Qvxym66-0oU7DaaZEiRm3w2MC8bTkfTx47lpAJQykeAogc4NILWYq9Jl2lzYiSMNYy0wBFLXOQNJWCnwsCz2aE6MRgF8NXmqoxZtgqk4XeLsKKythO_SyrR-MOFSYpSLKeHsGmXubQECYNPZNl4Ex1Ji484RU_TlnsGDpEToaj1igXNZi_8d9Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصویری پربازدید از ساخت یک هتل در جوار ارگ کریم‌خان
🔹
ساخت و سازی که اعتراض حامیان میراث فرهنگی شیراز را به همراه داشته!
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/663547" target="_blank">📅 20:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663546">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234209cb14.mp4?token=kDiVdTl4KCW7deaCcJciONwCFHmhpQHADYIh5BR2Wkxgyban63YJ1mvtDX8lEE78B1gbx9Si7IT1EQbsbTWLN-eUgDCMvSJIaH3WeW8uA5qUUy7xv73ZxqGGBybfarWk9mYLZtWzByFhjPP_teUnzdxkmaijaVz_YwbjkVMiwwvZVhTyPjZpc5t155xVw4KM0Qmlq1ISjsaY3rKpa-EyL97safJR0GsMVPt8g--S-q36NsQMFJNBjp0UZACBF15_aBeS3gE7xG04a4pmxsINV4YiCDABLufzvawl9oTJfYdKZrATGn74B_H9883VrbrMrrDdOOTYaVU-BatDyyO9RoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234209cb14.mp4?token=kDiVdTl4KCW7deaCcJciONwCFHmhpQHADYIh5BR2Wkxgyban63YJ1mvtDX8lEE78B1gbx9Si7IT1EQbsbTWLN-eUgDCMvSJIaH3WeW8uA5qUUy7xv73ZxqGGBybfarWk9mYLZtWzByFhjPP_teUnzdxkmaijaVz_YwbjkVMiwwvZVhTyPjZpc5t155xVw4KM0Qmlq1ISjsaY3rKpa-EyL97safJR0GsMVPt8g--S-q36NsQMFJNBjp0UZACBF15_aBeS3gE7xG04a4pmxsINV4YiCDABLufzvawl9oTJfYdKZrATGn74B_H9883VrbrMrrDdOOTYaVU-BatDyyO9RoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قربان‌زاده، عضو اقتصادی هیئت مذاکراتی: چرا پذیرفتیم که به مدت ۶۰ روز هزینه‌ای برای عبور کشتی‌ها از تنگه هرمز دریافت نکنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/663546" target="_blank">📅 20:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663545">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr4FQFbToAuz1WImzR8l7i5EPPERfY_TZICDV9VyQIY1aVplBMTYHuHTdyfkz9Y0hg97Iqxzx0ABae_L8nmTZGHFLkdkYbUAj6e5jy0_oxUy_K9MqMcG1Adp2qKJ-hg2BAL00r6dSGwPnvvlfe1LGik517Jb9NTIfNwBPtkd02hSSXWZT642YEd6xuIbbQFrXBCqJNONoQRRjswh_ObBuas7UsuB3yNXLcHLUPryKlCYyhAPcBO0TE8NUW_ADfqB8vX3BL1Voj7UY4XCv4t3iIe9TCozuiEp-_J5MOuU8O1rwH_cBUQIaNCwpwbEGnvzzPjvLsYwAX5mVoaHLWrjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سردار محبی، سخنگوی سپاه: تنگه هرمز سرزمین ایران است و هیچ ارتباطی با آمریکا ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/663545" target="_blank">📅 20:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663544">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaQFjCPi_CjBa0cSfnB3lcTZIJILPZnFypA1dpwjjXDrI4cD7bVLuqyauOURdVz2JTfrt7maGaZ0BpRQZTu6YHN73VhRMInnYZd4f6DEkbx1UFQSo8a9eywAcGewMaZd4C1iVm1OsXK1MaQ2v1NMdzTpTkwjgaiB0a0dKj2Z4eu-D2Sgivx-LkflAZD7v2a5Y2lCeeFSAOgCZBb-tORbI2z3V1ZfE_-kDNBPBzw-Cc6h9NsobJOS0KBjmWTBLDSKXtkYyHkq7Dirxwbeeb6B7gPPldGtT-Nz4wPmAGFsYJGVEyVx9k_67C-cPz5n0eWesmM_ahtxLcsZIUFPod8PmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هشدار رئیس کمیسیون امنیت ملی به سران شورای همکاری خلیج‌فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/663544" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663543">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862168a14.mp4?token=XSmIDvI_Yzhk7B5bTLIoXbFMDi9hTUbTZqk3rs2D32-roThwEfgEKK_w7oc3f1l7FYuorvzHp4VFzjMdAYo7pMTil18coGi-FMbX2SPube6XtM1mlj1o-XjBEtHsofxzgA2umg2nYo7rY9K80_wgMcXRwMYgzk8AEOhZUDjTERNj9SHNLSD7LM_LVqJBjyugns36M2TLHqlEu5gesolW3SLAKrJldg47Od2tV6zGhHFmPIc7ByS7-HSRshJRrybQ1pAg6cABobI8alTs6uAjyBrJR5uOn1kinC73v0gmp9RYhmMphOUl3P9jSCSJazLKC9ag0dk4gtk8pUKdJZJ9gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862168a14.mp4?token=XSmIDvI_Yzhk7B5bTLIoXbFMDi9hTUbTZqk3rs2D32-roThwEfgEKK_w7oc3f1l7FYuorvzHp4VFzjMdAYo7pMTil18coGi-FMbX2SPube6XtM1mlj1o-XjBEtHsofxzgA2umg2nYo7rY9K80_wgMcXRwMYgzk8AEOhZUDjTERNj9SHNLSD7LM_LVqJBjyugns36M2TLHqlEu5gesolW3SLAKrJldg47Od2tV6zGhHFmPIc7ByS7-HSRshJRrybQ1pAg6cABobI8alTs6uAjyBrJR5uOn1kinC73v0gmp9RYhmMphOUl3P9jSCSJazLKC9ag0dk4gtk8pUKdJZJ9gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
طغیان رودخانه در ژاپن؛ هشدار تخلیه برای یک میلیون نفر
🔹
بارش‌های شدید و نزدیک شدن دو طوفان حاره‌ای در ژاپن، باعث طغیان رودخانه کامو و صدور دستور تخلیه برای حدود یک میلیون نفر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/663543" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIaeSTJYF28YDNg3sdDgbQq9Cb-gx1m9C8FciCu0TKnVqbmALZkzn10fWwK2R_n2SrXn3P0TjevZcDK-20tEf8wXlOiWkiVB-cWUa_OgwdZ9nFngq0YFrlbR41tB4knrdJH5LO7h96DU5tCZK3KCxH6C-qbHd0yVYV7PBqDP2s82zQt1ewLPa1zIrPWGM0AbPbSX0JyJN-NJ1lAwqQnPq3AN4BsB0qBWleugGSJdbmJFBRU1og8PPq1nv_bUUnYsVwyJocmXFD9SZM4vAYEZWukFkTHT2ItOmsxuF5QimPbiIP_sYcPalaDztTsH-qiftbw53q9lbXBX5QnyqMSVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
روابط عمومی نیروی هوافضای سپاه پاسداران انقلاب اسلامی پیام منتسب به سردار سیدمجید موسوی را تکذیب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663542" target="_blank">📅 19:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663540">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btSWxmgV4_uLmL2v6p8fJ9Xz1RbtIUw52mRjIf4ahdVw1AJfH1-_anDjD3JYFwlbMBl4sNozLXxvEfUFfXkWiZbd39Ce2JbIn1sjxwGR4EkDmE2bXMOCDOr4VOKsI23qwa7WBlIPOIi1OeaaIVUEzcqF774kJn3v3fP71AFDaapuGZrnG2oow8FptrJKKQcgGUSnXmrMrr_HyRqhJso_ScQGUL0ByT5_D-lj10D11E-Xhn4MkU8_VGX6Dw7oB7bPKOokuLPBFpg3FuTXMIWZbysFd2eevIuuQqQh0rDGqzl0WA0Fz3C3BFsCca_JxLMf5SwZBOyQos20_Onuu_hDrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPHHyeIyosHHgLbofJdGdadn8Zn2UQFnPTJ7BgaCsudI-5oJX5N0l8oOCIpMyEYITfm-v1vSVOZS5HoAEMW3I0s2qK9JVh0kU0tpW7xYavg964tqIu4x3ESDotSxW7MkZ0RkSzGWWXqCfXh0ZBvXzlQkYymAJb4oM1e6ff10sY57come3u_6MepuI-u4LyPciwfbF8n-9gVYO1QYANDEO4tgIvRLiuA78AN1lpMu4Z5uffExsXjf-kpkdw2BlWMDW-dOaP0ubEdGSLE0fDtci3_-rDi1ftas7qIhq6yxORnKSMrUpcPW1KJU7Nsb4PGzm5fofpQCDtc7G2cD5xGiCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
رقیب کره‌ای آیس آمریکانو؛ آیس بلک سزامی لاته چیه؟
🧋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/663540" target="_blank">📅 19:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663539">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
پایان ست اول | والیبال ایران و ژاپن  ایران صفر _ ژاپن ۱
🇮🇷
۱۹
🇯🇵
۲۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/663539" target="_blank">📅 19:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663538">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa5c97e84.mp4?token=sTPu2vfxPtsbE3iPRemJl3MJU8RBBZxADmsk1UyRfuX3wg4Yks7deWrd2iO868MHdZG_4FvEJwWmuMjegEBuzm6xYs_HxU2deYCzwgQY_gAcBAFnn5qEmy868s-lFFzZI-6Iy39X4U08nF3OgiEkZOIyuUl7ny8_ODSUpxSILcHjBY2v0q4hQ6qth4Wk3JAvTmB6KqWbJ_iWxLxtWQyUHBHCijYTl2tfgO3fItWQb86tJmuzoMJgJSZSHBBhscpAUFhkQFte2e7NMu32TdWsc27Lbyq87P3Xcs9y1OxH47rwQ2jJhx5zcZU1-XMPDER2uouUHFT3qGP02dFuTbvq0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa5c97e84.mp4?token=sTPu2vfxPtsbE3iPRemJl3MJU8RBBZxADmsk1UyRfuX3wg4Yks7deWrd2iO868MHdZG_4FvEJwWmuMjegEBuzm6xYs_HxU2deYCzwgQY_gAcBAFnn5qEmy868s-lFFzZI-6Iy39X4U08nF3OgiEkZOIyuUl7ny8_ODSUpxSILcHjBY2v0q4hQ6qth4Wk3JAvTmB6KqWbJ_iWxLxtWQyUHBHCijYTl2tfgO3fItWQb86tJmuzoMJgJSZSHBBhscpAUFhkQFte2e7NMu32TdWsc27Lbyq87P3Xcs9y1OxH47rwQ2jJhx5zcZU1-XMPDER2uouUHFT3qGP02dFuTbvq0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای ایران
🔹
در آستانه دومین بازی تیم ملی فوتبال ایران، مخاطبان خبرفوری از گوشه گوشه ایران با لهجه های زیبای شهرهایشان  ویس هایی از جنس عشق و انرژی در حمایت از ملی پوشانمان ارسال کردند.
🔹
این ویدئو،  بخشی از صداهای پر مهر شما همراهان خبر فوری است.
🔸
الوفوری را دنبال کنید
👇
#برای_ایران
‌
@Alo_fori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/663538" target="_blank">📅 19:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663537">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReVbTcR6_X94QqKKwx2ZlKYnerc6SMOX9bx_rjhazZtriuY-VTl4k3pm9KvoLKV0VVT8mFvI1ETE5p0RXUbMAPQyCU_F6PqAkENunH3ftGME3W37LMf4jw5RaXqgndo_0rFK5FCZ8lcIvFOMURoYVebu5NkEAkIJvFIfxQVxTixOWutZg3sLbrE8_nJTqZN5cUBMzk_qIOJVr0i3AWUiMfcDUyYhmLaDO5HlsCdRZji2y875A8e8wofsilyDxPzFIiSE61AfFYG05TBoZKWgSyU17GTOdsMtEmefpHNloAJySl-XDRJ0PJRPkcAV3jD-_f6zXqdGFfNS5OTDbA9CYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ادعای ترامپ قمارباز درباره نقض آتش بس ازسوی ایران
دونالد ترامپ:
🔹
ایران دست‌کم چهار پهپاد انتحاری به سمت کشتی‌ها در تنگه هرمز شلیک کرده؛ یکی از این پهپادها به عرشه یک کشتی باری خسارت وارد کرده و سه پهپاد دیگر توسط نیروهای آمریکایی سرنگون شده‌اند.
🔹
این اقدام نقض احمقانه توافق آتش‌بس است./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/663537" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663535">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3NpUGTLb4SChG5DkuRvMwY6o2ibExg7z1EJx56XqrjC5I_aoNTk_DUv1NByBNbzZji_kxW0pdl1HzLlNU7eGe_5YwJ_jSuBAFf2AefpBkZUYTlZFRdvOEQdHn7XQ8rGvzH5jcEjtoLyn6MImAA_0Ol_SJilWlrFkuA0dBjiuFHigNouAQ81-iYlGgqptatqM0WyDEhkpCkpEW-sO6OKWuodEwiv1tQhC3z_tROhJsVCnWnE46N-p222uNZrgYEYvd6VIpMChKAG43rww8CMN_fJZ27BjSPLlHumUrCHgUcjSYD_ipx7HAZNfWyo-FTdYNB4abLfojkWbILeTBON1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpS54vi-ab1fX0x6XWeVU6qfC-yoap9Y_6dwSrmUhQ3QzUDhSyeqFvM11JWwUv6WyX32CkRIfjixAmaTz9Q_Hb0vdTA5Km3AVq0my4Ys4Ui4AR14NpTRBIgLHUiqb27Rd30nHRunTjoTfRZT72DWWZ_jsGlMV2PJ1IIsBFpBFOxfq0m0dcmlsCxibPGGeeDfLuZNJbIH_M_kfCpyajOKqFOqnQ7tnEyiSjNPV-Zbb6KJs9_t78NHNfItC4gDP7a2BKs9kY2IPbzWYsteO3iGoqMbf0ILIZRnS3Zbs4A1ZDtokPeOSzV5x3aE3Tc1lBrTjlDUHjraSa3HAFtyiCtPsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برج هواشناسی بوشهر؛ قبل و بعد جنگ
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/663535" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663534">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suazLNmVj15siWIepcFFK4F633bFNx3gy9CtBL5hlD8jcCyR2sJQu3XZ8f8pMuLAeE7gMbhC1Fz2vpR6heGRipJ255YL2EamqLeVE_R_4sz9xemSkTyPPc2O-JEgQ-G2HscjJy4xfvkIRWfbF07VK7OTkl8spnANWe_GT-2MQfanEInzn7fm2xm7wiDB7EQEheKWrl-cx2eR_xJ1UDIVdiWpNU-7nja1NGyYVSg0iSKnQVJPmg2H593Uju219d-F0-hkaZfjonPHy1SCt7UPABf_bYZ2Ed2VrCrIfoXjqOSOGlJWBrusdHO_tkRXq5xzXoitmUHn9UTKiMMBkNCf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
والتر بلومبرگ، تحلیلگر آمریکایی: عمان به اروپایی‌ها گفته عبور از تنگه هرمز مستلزم پرداخت هزینه خدمات است
🔹
عمان به متحدان اروپایی گفته کشتی‌هایی که از تنگه هرمز عبور می‌کنند بایستی برای ارائه خدماتی مانند کمک دریانوردی و کنترل آلودگی هزینه پرداخت کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/663534" target="_blank">📅 19:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663533">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcrBZgYp8vBpfsGEhpJf7PSPQ4Eaw4Xauv4EcPie1MJgXOWllxyJayeLAeMRGjAHbBAg-jUc4U2-aVMkNlMt8Ki8Vur8-gUZEUgCcAFFPe7WxD5nOPKhJRDp3kMdsos6fHLvCm_y_D6fUBxmEOsQKtL4Ee7wbROcBLwMFuXQnLHNyAhMEwbQAY2CK5sVVARy1WxIdemT6cE0vBUPDBsTBcrZyWfGGsPKJq_uNdwzAJFolX7-IrifVD8UOFEm49H7jsetfA0-i-HN_D48hm4N4f41NuRk6TaKv2qHmfedqI4GFJYFfvp1ArUmEjTNvL05AZnFL7ydcYPt5RZ-CprYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵
مشکل گوارشی که نباید نادیده بگیرید
🔹
مشکلات گوارشی همیشه با دل‌درد شروع نمی‌شوند؛ گاهی خستگی، مشکلات پوستی، نفخ یا حتی مه‌مغزی می‌توانند نشانه‌ای از اختلالات گوارشی باشند.
🔹
اگر این علائم را به‌صورت مداوم تجربه می‌کنید، بهتر است به‌جای نادیده گرفتن آن‌ها، علت اصلی را بررسی و با پزشک مشورت کنید.
@amarfact</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/663533" target="_blank">📅 19:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663532">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2e5da6e1.mp4?token=fPbXL1RIdgTCTNKdN0May2cE8hp1hjpUCQ7GGdDypZlFjiySHbwJqv_hiB1eLOZoelwYQH0_kmqyud-51MaH0OhKEi3FVWF3isCwmsRIIgc9SctwNBeCTo_cb2IL2xwuGcxtlAt0NnFQxPUwpowfBP10ZxW5cVsSFiY7xQSrUbyTHuAL_afUe2bzsVNiVGbxsMntjorXkg_a6Ha_d3Lk_6mNxu7CzSfOCb4A4lfb1vy8KJ18eIrZLDcYce9l4iEtYzD1NPzWIkkFNS4DudhS7xoGkPdLVxb11K8twmmKZ4IBe4ZFZX7io7I18j5n1AuHSU7I-sCE-_Bf2SiDuFDr9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2e5da6e1.mp4?token=fPbXL1RIdgTCTNKdN0May2cE8hp1hjpUCQ7GGdDypZlFjiySHbwJqv_hiB1eLOZoelwYQH0_kmqyud-51MaH0OhKEi3FVWF3isCwmsRIIgc9SctwNBeCTo_cb2IL2xwuGcxtlAt0NnFQxPUwpowfBP10ZxW5cVsSFiY7xQSrUbyTHuAL_afUe2bzsVNiVGbxsMntjorXkg_a6Ha_d3Lk_6mNxu7CzSfOCb4A4lfb1vy8KJ18eIrZLDcYce9l4iEtYzD1NPzWIkkFNS4DudhS7xoGkPdLVxb11K8twmmKZ4IBe4ZFZX7io7I18j5n1AuHSU7I-sCE-_Bf2SiDuFDr9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حسن رحیم‌پور ازغدی: تُف بر روزگاری که رهبر ما را شهید کردند و ما از صلح با آمریکا حرف بزنیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/663532" target="_blank">📅 19:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663531">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6DB3IpmmRMgBH6vQ21TftkN4AotzTSGDYZCYhheoUU47SZFklVmVH1LhFxJ7cAEm9Sw44yzLGrKBemoo7djx38jsE-eK-oCEpvAhWOMyoqa8R_85T8B61q3SiEFLDtS8RQm1xSq2px7JXFIRN1LxEO_WbNKnw61wEODQE5LlrjPspF3L3GFgEw2JPwRhT3e6GD1HRE4YeB32AhKDgH2z8htrv1w-1AKSW7svbxyOxmp9ToErx4N9m6Ao0nS4fSzIZtuJR3LrzQYn0yDu5xFN_SasK5KxCjiZ_nCNs8wu9hUobFu_r-lTf3-NqXBMk1yG6Pi4kjyLkSniMKCvp4sUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
همه خدمات بانک صادرات ایران در بسترهای حضوری و غیرحضوری برقرار شد/شعب شنبه و یکشنبه تا ساعت ۱۷ خدمت‌رسانی می‌کنند
🔹
با تلاش شبانه‌روزی متخصصان بانک صادرات ایران، اختلال موقت در سامانه‌های این بانک به‌طور کامل برطرف شد و تمامی خدمات بانکی در بسترهای حضوری و غیرحضوری از سر گرفته شد. همچنین شعب بانک صادرات ایران در روزهای شنبه و یکشنبه تا ساعت ۱۷ آماده ارائه خدمات به مشتریان خواهند بود.
🔹
به گزارش روابط‌عمومی بانک صادرات ایران، بلافاصله پس از بروز اختلال در برخی خدمات بانکی، اقدامات فنی با اولویت‌بندی دقیق و متناسب با نیازهای مشتریان آغاز شد و هم‌اکنون تمامی سامانه‌ها در وضعیت پایدار قرار دارند. مشتریان می‌توانند بدون محدودیت از تمامی خدمات بانکی این بانک استفاده کنند.
🔹
بانک صادرات ایران ضمن عذرخواهی صمیمانه از مردم شریف ایران بابت وقفه پیش‌آمده در خدمت‌رسانی، از همراهی، شکیبایی و اعتماد ارزشمند مشتریان قدردانی می‌کند.
🔹
این بانک در پایان ضمن تاکید بر لزوم  تقویت و توسعه زیرساخت‌های فنی، از عملیاتی شدن مجموعه‌ای از اقدامات پیشگیرانه با هدف جلوگیری از تکرار چنین مواردی خبر داد.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/663531" target="_blank">📅 19:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663530">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca0158cd18.mp4?token=eTryZDqa8Fg6o7letFQZjvseG37Ktt1Q6Sb6D8wsUlczGJDvgXd8Kz_QpYrPhW242pG_ut5wWijUdhB9UJYxbfoU4z6DznIahtl33Qtg0rus4MuMaVLre9EJx7Gm9P6M-VlX51HWdWz_8ErB94EabUlcb8mTkSlnqfu9bh7o1YSZCIpH8JgxeFN9olEyB3WH2uCfBV5LyRdvTjQSFAq_mU94tvaj0OnbKQEssrcLtP_WcGv3896vQJXXBIfvdxCAnVGSsY0M3AS3Rm9rvMJ1-oGyELzy3X5kmvhsQoiVpTe7Fz0EXT1q4uTWEWodYfY-tolbnJo_OOyuuIW4CoaoEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca0158cd18.mp4?token=eTryZDqa8Fg6o7letFQZjvseG37Ktt1Q6Sb6D8wsUlczGJDvgXd8Kz_QpYrPhW242pG_ut5wWijUdhB9UJYxbfoU4z6DznIahtl33Qtg0rus4MuMaVLre9EJx7Gm9P6M-VlX51HWdWz_8ErB94EabUlcb8mTkSlnqfu9bh7o1YSZCIpH8JgxeFN9olEyB3WH2uCfBV5LyRdvTjQSFAq_mU94tvaj0OnbKQEssrcLtP_WcGv3896vQJXXBIfvdxCAnVGSsY0M3AS3Rm9rvMJ1-oGyELzy3X5kmvhsQoiVpTe7Fz0EXT1q4uTWEWodYfY-tolbnJo_OOyuuIW4CoaoEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های جدید حاج حسین یکتا که موجب واکنش‌های فراوان در فضای مجازی شد: علی‌الاصول یعنی ما نباید اجازه بدهیم دیگر جام زهری به خمینی داده بشه/ وقتی ترامپ فاسد اهل فحشا به مقامات ما توهین می‌کند باید محکم تو دهنش بزنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/663530" target="_blank">📅 19:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663529">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoqXV-B_iXTMUj-jVPnqycATyKcmcHO8vfoUkXQqGSnXF7XpGmm_L-UgXsMrOIcjEnVbWcXCOlFjvHdJLV535o9tVrYCYaUPR5yBYBUh69Mw0cVvgiIspztS0SH_wuFvwmU8ecC85Y-MwulGfOYFQWpLfSBYkdPvToNY8xZ-v-kc_Zt06f04riV2puDh5UPXnD60C5Q1-XUozda8JYG9C8UbEiAmDGSK-yD6u86yd7__NlJa1kbI8dOv_4PzZnxgCtIVgobA4St6KSXudBFowaF7VV6ulFPHx5iFGVvwhLbSeEHcLNOHMKSMf3vbZseP2dzy4IA8h1QdotW7nPvX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/663529" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663528">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔹
پایان ست اول | والیبال ایران و ژاپن
ایران صفر _ ژاپن ۱
🇮🇷
۱۹
🇯🇵
۲۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/663528" target="_blank">📅 19:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663527">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4VH8vgQkfnnCR8rsuViACvfueML9xqwmQ8zlQbGVaxjCBcwZDqUznuyICmAxQSPNW2plGy-JTv7F7bKRpxoVURvi03zCaqCFfUpIngL_8ndz3IVIwoI4AwV7xGPxsLrzoBSkm878uUtVuK3CCKZoDjx8g1KZ58Bb-EfJyNXK9c6z5cfTPr1iyFIz8eD46VZSXb7o44-p7xP7gFSyLEiFYDqWizu63ff6EXrCTLSUH4MovkEzTungGkDlPXi7AygLyPLCP4zmRPl0YPPCEK7PodXFZI2YTWjYsuuAB48TJTHXelofK5dQ1Eri-pziWmtMdtR2C2bfSvZCUmhvrJtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کالکشن جدید ورساچه مورد توجه کاربران قرار گرفت
🔹
برخی کاربران فضای مجازی می‌گویند مدل‌های جدید کفش ورساچه بیشتر شبیه کفش‌های قدیمی  بابابزرگ‌هاست
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/663527" target="_blank">📅 18:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663526">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ادعای العربیه: دور بعدی مذاکرات آمریکا و ایران در تاریخ ۲۸ و ۲۹ ژوئن در سوئیس برگزار خواهد شد
🔹
دور بعدی مذاکرات آمریکا و ایران فنی و در سطح کارشناسان و با حضور میانجی‌گران خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/663526" target="_blank">📅 18:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663525">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWBToFqQHPPRPLu-iXXdl9awjb_EHGvOApoUN-X_A22lc43buep5bWdF-lrZjJr9_gomPfDFycZYXc3IHu-S7Te-gqcbelP1g-7J_Sy98Xt8JEeHjIkMi25XKziUkgdoRLB5x1u2DZCF759q3L7aPxarIaDvjtrhU1V9qEQpiy2I_uTpHCm_tiFkwBM5_XTFkkB_bxqVzRyfobAd32mMbMubAhEGW43KByJ8h2rWVlFFV3qazi5ufb3oOaOLCFqM1GSrdKojsbmcGm5Q_uMfRyPpiieNrMVmYWYCWhzno4_QHmCbX0_4zOT8kZ2QHtV6RNfuMPbwmyXjCMOilGieqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مشاور رهبر انقلاب: قطب نمای برخی همسایگان هنوز دوست و دشمن را وارونه نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/663525" target="_blank">📅 18:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663524">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLg45zsS-rl6cRIh7XeB-TcKxceWIQjVIo841o-84q6HyJdWU1CXT07pmCpyBjHxyZdEbXdycIlij0i79dTQ_VNxdE308GETgPglyJCrY6ggVcedb65vQEQMBpfPCYXBI1QpF6LyzonBp5JvRDQ0iMMc3WY6P5S7OIMAfDnqLiQBc92gw2bGM-fZVV580IcO1V1DFSqM2mxKzlbxRn8SU00RcUVvdq0vUa53kRNatbavvrp_HmYiAxF160NZBvEiChl5TUw4o7_d8sH36jgA9VrVewtY9sV783-waF4WitwSU1lz_UqD0iCS7EXo1GZHppyVssCfjVQSU385pAXq8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تعرفه‌های گمرکی مناطق ازاد اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/663524" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663519">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fN7HulHmX0vpWrDJRzKVfHRkQQdnISM5g0m4EzhyrUbynWYDT1d_ThLYezK27LGN2L7DzmgOG_oebkGC5B7kR1JQF5M0-MMWEq_Ns6-_RGhks4jjIalL5ZzSzS4zh7l9Ttp3v4gaCljFSeMO1ymoygvQMo-OgcZuWyvBePIlrFN7oPJVRfUh4dmfQ-IfOXrAdDocpn8XWfwcJWeaKpxqDIMVqlkLpJZuJt75NPsqOoxhhXzaBK0-5nwhaE4C0zFjrjaz7KTbv3skBsa20WNvCPa6jQiHAv9zS7wOvonlYD8hjE8k30--ZH_RyDp8W3CHh1OTr5k9HHSkX9sZ1BwyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LkYSwEY49r8XgFf1YmMdqWnNUdh5ZZ4CDcrXJn7VkFtVDKMau4RXWet-1F8G-QpQcRP_XyNQ4o9W-M3EjdbuPvI95y_HWhQfN-wDnmt6kMVkKEJnXcCigquw_GMB1xHSGYYV68XFiJxaeYNZt_wz28SAb0N7RKFiHs_RpW2wju9xRS3ez9pRILroY2F13U6Lx-6GIP8C7Pmskx0WeGDldLM443OWGd9PjzdRT4z5WkUWOSw7mGurIeXqIbFDYLmijVqqFfC3nDIqJ2EtTlQ9tq-fiZU5mrpDZuZguH5YTe2Y-nOvsKLSlUoWSwELlgJxJmIUnIXW_7hiTSE3thDADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwc3FVKCPemAlv4da7S-TSu_Qy3SI3rV0b97dyMHDWE2X6khsZfAaQGBt2gabh86IbnaukvZUVIj_7cykgB0yk6Vwpxjyd_CZsSRD45wEv6PIybOeneWD8ATMmox0D600fTXF0_4TEASRtTui9uXuWIgW3Uu9Zh6rwWEjqjlyDP0EWEHG17rdThq5sVsrfGqbxovnFjL59RwZ-OVmObrdtnOiAYVzBZnpWebQNnH-qp7L62AGt51VU8VVQyNmiP1r_wePU4jLKIZxdkhE8qhzpWsjtTBeTOxwOTJAWCqx-sqqYo-nvBlnvdyOEapy5NeZDev4bDuKwXCG33Xc5AXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnRGOJNCvd2pPG5e6dlSMP23aXBHjuk54GJb5I4vEnHYBhXpSzMsrG-cKyqOryN5TUlqyM18L3ZcOpxoD9T2eSi4B5GM3MPO5aBksaG3BjCj5vBrQMXpQoC-wQYcj8smFtFwc9kuvFgDxbK-6bUtuKpC5VmIVQV3qTyb-u03SNj67YKRl_HbyFjvrbss9ThoLc0Or6xcBhR_LHUjIuVW-FSwmxMo9934uUZYS9aTJECUmMsSQnNAeiGPFyPCjX3sgayIc4GRCTegj_jDJD3YUgQfQ_ilk4s-D-jPFz8G_e1zEO12NhK4AUKYmCTb0o34fWD8nmyHrqCcUmRzndpCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRo7cSRx6g4pFqFdjEezDudl06-tZbwCgjlIlXaicdou4ATZBrnOV246bV4Xxn4Hr3FTyDKwFJZe55Zwu8WPPMc4UI0IouLYepqMgXU6qoisoYoPj01-Z9KnMvrwsaLdzDypzSqUAaLO2IHZyWnzSGqoEimZ_5EQjRZK_g_s6FK2WHsqD45Gva8x2IDzO5tSSQJSV0ooBEYAqGRkh7GlZmDB4QbwMlclaKKXKM_4NtuWxj_2wYXQbA6dn_beuTBt9bZVZzq9jf2O0DM_9bAnqn55K6qaEPLYwVLRWIuOUvQjsrkpkhXnBuVXUD3lbl1rgwXxrVWfOzgNi5cw9hq2kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصاویر هوایی از مراسم عزدارای ركضة طويريج در کربلای معلی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/663519" target="_blank">📅 18:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663516">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjGaH8D3TXZaRTZo-Af1TNHXYg0BnwqRtXjli4cum9O8ybXANPuA-cqa17hmZ5tTWhPWmwmiSY3_Jsch7sht7NxOd7oo91AJawE0x1aiJTiBCt7sGzMDfVA1VDUJHscy-0u4gpGSnmb3068WVTqj3u1hupC1wT0utn5PFT-RXLOB7YqP8-AFPo0LhSHGkfKklP3E4v0LV4orvgw4YAeAwgmNnRTNLmwLLjaCmJ8NLsQFpx5ozWS2TWZ8BXrv28iAqpPwHLR9ZyADpTEPwNmCvXJ5vG7kl-5W3fY4r5pkUoGdYu3aIS6y3AiqpSDLrkYVrD5Qk1mOjAaveuigSDahIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCQC72QPRoXebjuOY7Cw1uHXeurj639RG-K4l5FWBbP3Wt4lC2n2Bb5Rw_5YLgNkRDpyOFL-s500_BDHjjxnDD3v1yfUISNLfhf1KY94O40D7fZE8E-4Te1tE_QolHgVap7C3_DJl8Cd6WgidHxenRZVu1ri9O1ehPbotTuyxQNI92pPvPInXcV9OqQLZKaKx1AqQNNpISA-Pmot8X3JyBAcb9DUh095JC3cTaY-UwmZusxiuRNdrvAkSLOQKyslulxmD7v-D0l2rN4sK0rnbCeGYZMRn29S8ovsFgcMs5c3M63wTawTe36NW9zRcteqzg6kEC2e11X64rxOB_DFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8XHQZFG7U6iV96aQmuCP_moGehjQUhkLcqjzuZ2sL15OUsN04Qsx00xmBCAx4hKeO4hLb9NIGycZukeevOZjJto2seQJhsezXXO8dKJPzMwP5QKhh1h2DJGJbiefNX6EGTuNgT0eGpnScfiwsVqe6lXCXOaCOR86rF6c24YbVj1T6u3XkztvLTaHGOd1IRcaILtewxtciTaaSGOWR-A5FEw5ur1xF6UWHTw6XbL6oPuEgF7h2raLdujEKYw3z1A5P-lM1PLWD5fmpMyPNJRyFQ7X5W5JK25F17OhPBcxIf8hmLVfQzdS9hgUGNdYCY8HGfiBllpjbjFN91HVIl9Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور رئیس‌جمهور در مراسم درخت‌کاری اسلام‌آباد با واکنش طنز کاربران همراه شد
🔹
بعضی از کاربران با اشاره به پشتکار وی نوشتند که اگر نخست‌وزیر پاکستان مانع نمی‌شد، پزشکیان تمام اسلام‌آباد را بیل می‌زد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/663516" target="_blank">📅 18:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663515">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKp7RTZSwwfRXlz34WHNpRYXB6GgK13afSfrogmIvxNP9B9NyNf0cYeehPp5HgpWU65ddwB3ViXiHFZOxD3gtGEfuiOUmF_GXXL7nodagilwSQWzc6Mf5amOLu7cLQHXAxBKmEpOsVs5xippKapj94pb-pJlRz778q6UnilNEJ2OrYPELU4BDKF0ocjD2a2DRvToLtX2w6oYsYuOoz0BtJd9xlEzpe4FGE1BQXZHa7dQn9De_eXLUIZ3cyQvbS8pEMbAB3cwEdCIIiHhoqCIiAxas17kbpQrGEqoCNPu06mPNt6pSv_8IdPfVjX4rwA5QztKkIuNb39JqomjHzq8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
منابع آگاه از ابلاغ هشدار جدی جمهوری اسلامی ایران به دولت مرکزی عراق و اقلیم کردستان درباره فعالیت گروهک‌‌های تجزیه‌ طلب خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/663515" target="_blank">📅 18:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663514">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔹
خدمات کارتی بانک ملی از ۲۲:۳۰ تا ۲۴ در دسترس نخواهد بود
بانک ملی:
🔹
در راستای به‌روزرسانی، ارتقای زیرساخت‌ها و افزایش پایداری برخی سامانه‌های بانکی، خدمات مبتنی بر کارت بانک ملی ایران امروز جمعه ۵ تیرماه ۱۴۰۵ به‌صورت موقت از ساعت ۲۲:۳۰ تا ۲۴:۰۰ در دسترس نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/663514" target="_blank">📅 18:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663513">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
دبیرکل IMO: بیش از ۶۰۰ کشتی در تنگه هرمز گرفتار هستند
؛
۱۴ ملون در جریان درگیری‌های تنگه هرمز جان‌ باخته‌اند
دبیرکل سازمان بین‌المللی دریانوردی:
🔹
شمار زیادی از کشتی‌ها در حال ترک تنگه هرمز هستند و از کشتی‌ها درخواست می‌شود از عبور در مسیرهای تأییدنشده خودداری کنند.
🔹
طی چهار روز گذشته ۱۵۰ کشتی با حدود ۴ هزار ملوان تخلیه شده‌اند، اما بیش از ۶۰۰ کشتی همچنان در تنگه هرمز گرفتارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/663513" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663512">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee97d789f.mp4?token=GavInZF7XJc_3pgl3RvHLnz3Hu4kYs8AhzZFdiYoWN6s2vSLSaY12Gaje1Wcdk-qM5gbSP0F2w4DXaQMVIA_Q2QkC79i3zo9lzJIV1V6tFeHWbMxNmtj7zLUus2MgK7rP_DhuQKqkA-bKvUi6QeN7FNr-ongIzzcuyiHF3iYR5CbD173NnY8dV4gQOp3mwPirWESDkJajG_nDk9hHwjn1iusOvScr3pFDflGnEoUqVpWq4U4CJdDYeu1kulkVl6xF2_K2LFuJ-9PTt8OZ46CFdJhl-kjQbJ5LrhsjPul_myi12EOOVrqQBtaITqOof1tSIpxsmr7kSAG8D9WOY_ceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee97d789f.mp4?token=GavInZF7XJc_3pgl3RvHLnz3Hu4kYs8AhzZFdiYoWN6s2vSLSaY12Gaje1Wcdk-qM5gbSP0F2w4DXaQMVIA_Q2QkC79i3zo9lzJIV1V6tFeHWbMxNmtj7zLUus2MgK7rP_DhuQKqkA-bKvUi6QeN7FNr-ongIzzcuyiHF3iYR5CbD173NnY8dV4gQOp3mwPirWESDkJajG_nDk9hHwjn1iusOvScr3pFDflGnEoUqVpWq4U4CJdDYeu1kulkVl6xF2_K2LFuJ-9PTt8OZ46CFdJhl-kjQbJ5LrhsjPul_myi12EOOVrqQBtaITqOof1tSIpxsmr7kSAG8D9WOY_ceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
سینماهای 4DX در ژاپن
🔹
در سالن‌های 4DX، هنگام نمایش صحنه‌هایی مثل طوفان و سونامی، با پاشش آب، حرکت صندلی، باد، مه، بو و نور، حس فیلم برای تماشاگر واقعی‌تر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/663512" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663511">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyuSx-PtPRp1bkJ-cYyNLrzgxGRRyC5xJ_kz4R0d2dJH5-inHGnUqxpR1MSTKJ7eaJoOFgT-fcxdAbOkouHGa47S19h1KIfVvZz6x5DtMfbvRPSci2jnPZ4NsUTbaZexFEC65MEKFFDujMw3Z_ztwo3s9mkIKzJ3hh_2Z9wOEifsqQqjF3BGQM5dRY2yQRDwLWSi7zvBKRnIFn0JgU22auh5XzrvWG9h3P5q8NEWnTDZlYk7tSjAwn-NaRo6TnBXAmV8QLtMFTnOa_cbIT-blom_3i48CxTpKO6BAHB9VWdaUYzlM23tPlA-hMWzqBME77jTkrXea_K8NpNA_vcm4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/663511" target="_blank">📅 18:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663510">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔹
بازی ایران ـ مصر فعالیت ادارات در برخی استان‌ها را به تأخیر انداخت
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های کردستان، قزوین، فارس، سمنان، گلستان، یزد، مرکزی، خوزستان، کرمان، مازنداران و زنجان فردا با حداقل ۲ ساعت تاخیر شروع به‌کار خواهند کرد.
🔹
تیم ملی کشورمان ۶:۳۰ صبح شنبه در مرحلۀ گروهی جام‌جهانی فوتبال به مصاف مصر خواهد رفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/663510" target="_blank">📅 18:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663507">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSXUUYk1SfRmf1KlB8PNv3UlrZFLTqqoN9hAMEBLUyoMoGAmmYzShV6lFFIeFUgzBra8UIRpdkvUDBFqbEzPIIE6RnKPvn3xM6hIKrT0jmLvYSiK-zY6NnH2BrnjMYJIB_pZK3W1aMsVHK9B_RxFfeJo3vgnmxPHulUuOKaCn5Q3tn3pJewJJgTnXGigowvDl-EhtXY6R5D3vRrYO00ym3fm5GMGkdFLjPaQXwglYQM0XWsaZFsRYM3gSIcYKwX75Hi7U5yCVH3OIvfTFJHHdifHAEt_VEd4xHUHJ9l_iAv95QZ4ne2OILhNTxFXZ1jTbzSGQvZQrxJaFxTnUY9LGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUkh9v_saz8msBT5Q_OEZfajS_NGvVnlSeyxJ3UBgtyZd1kjdzgfgFg7K-knqUP0VLzXvbja0kLEDLq2ghuTTO4f98a2gIkLs79YlSIAH8BwnCo-gv6Lvj6LLqcVX2Y5G1UAcAJQ-7Qgb2xP-T56NKfpQaREtOWj0--Y2ZHcszpY6kw8xN78ddZKXmGwTRN4A6tgkMr79sndf8MlBELCiDsEsnTyCmLmVRSoS8S1I-SQyZe-xd4MBt1E0skSmnFcMscO9Dig5ds1V7KppqC2SKYM-fCmEh0N9pJz4DJGZzXKY5DAqbE_KkkxIyDnU0QvftW-HZhuAEImiMMIZStSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oY1EGut6F4bdK7wsuE7GUsnhoKeYicKgReo2A0igX6vCHqH_Th1R_CblQXw6VMwSlomQGesx4plp53niVR-U4F1OCz66rMhHe3w-07MssHy0lREqPq7OGh1W4PhKpDwOB552Ndmyv8FzgxG_Qjs-_aJGmHBmoQI-hNfV_fnn_I13bMU1kfD6yj9SXQIlQNtQPDDMko_1HHmB_h1oqlMcCe3jRlblIQYTxEDTn7JdzXqGSWeiqdEVrLatAN5_UbYsxbqDnb4b7QbOxoMyqhS8NxQRVAash-DXB9R8AJ3fBJ6NRm4k_aOG97rz3wQLrXgEOLL0VPLyolIAst1cIAzSrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
حضور مهدی کروبی در حرم امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/663507" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663497">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7V_08iUw0bhuFc5xltYRTFxZge8rpCVHk00I5V4MMAZNpbuQXVCjN3-9NbHsuVnUzxQkSSVAvrrwgsNlU9-LGCgmRhh6J4V1Aa0-dzBR1mNzD9fVQkHL3ZO70h2lP4GQpi_qU6IVSJviEPQST-SvtakUIQEqQAwXT5zQvO7tK3BobY6P67H76mwsbFVUSQo_jjeDVeKk5MxwR6Ojc5X_LcljXkqI0TDXLJLkwiyu4bt-a3COz84LqP7sdQBGCSvLY2C6rgobRBgyEqq5IGCB3cwSHUqVaIkS2rCxWr_04b83z83zPguzXw95N-H7ePoekDl1FItnfUSky4z_vBtWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZ3SNrjW6aIGjR4PLudD6HIQaIFdu8j_Hmedm0FKGdEKr7jx03lT7sExFSsN402O_25bpAkiDNJui-E9UkCk_mCW5DvFIvYwEL5alR8AssIecOMR9BroqnVPFdITOMHpdafUr6sFT133eV0xiZVRC7uiv_VXt5fkzff9j1w4VfLVdKuUi1LJVnTWnV1NtbW26orzf9LqlrM0GadEZTgGi6EnleaoAQQTHcJEg_W11-aJBRHKFl6vn9awbG6yYZ6ekt7_0-KvtLjFEWnKTEQEwF7BEa8qJP5R0FSQq1iJDsdVOp4L3fiioSw6YJId_-rZ6ygioI_g6PNX-7lDOCkN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9hESdNLbUP-jlIyK3nWh7z5Pq8UYOA9rcQHKKHnW6nPGtRQEYZlVGTfwIx7fjz9vPLGeKh-Uip1Ud0QeQNiC-QZiTxSTRH3fjeDV3HObxQJTmN2C-6Fd7Z7JHFFKguHUI-2wh2wuIEXobQq9PKgblwXbjeG1EBkT6v40Eu46A7m2JmRCrHE_ekVa4DheXZ_oK0N3ScsUjewptssbNHLq-Oao_sNAKEX46DlPJ6QeDkuwC4eKFv5vslDZnhCsYa_G4ztcitufGF-0g3p3AYGpDiplLdRx6d6ngAIQMn_zsz7cV52BIoM6JHuzmT30o5dV8o1ROZMZ0jCyfIDnyhCag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdE_MYga_PnUNib0Sm5nA4V3ZqFe_B_9p0bl9lvV3XguLdBOqPiQ0p2ygwrCD6_LVhFvTD7q_TO6EFBWDtnYLXfktKPALSjBPrPXIoEtHxr4NJUe1YoRakIWPdv4JOY7JDfyscAASzjWvpjWhIEmghb4HjhcIgzVFZXuwNzS9ZN8Mzp2inwe1cDJbEnfJRTl5sstR6SDbTzIAvDLECAqjEJWQu5wqYVijBrHtbQfbGgCXiIZZlODz4bARj7I8IRRvmPJKYC6k9cfYTo6h-NFmWx7gr0ocV_b3DiSbRgvHNolVw_8ccJm765whChL9ouifbpEQyYShtWLTdWLW4QLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7yDNqvHiGMjs9GH0sokPJ2ZKpSlk4L6xdq8kT2aUaBg5k6drqfhvk_i95FKUHL6AhCQD5nIJjuj2NF4Hx09lRQACwy4ocMmqgOrVnSZVQ7izAEIy8EXe9dop0SsP9QIHsL5xdkpBGSgIm9P-jTaFO4yJXvDjftmFviuNF_ZaSZhWS7P2gqq3xUX2SXEDaho1kahL_zHFZn8y9naQswFmO5rS3we7MHlE0_2lAsCG9dDJz4bBEz4fMevBYWJQr8lWIbfjSqh-28JLHNffwUqMnJccAP_6oSOmyhHljQrXAaTNhjAd0M3Mn5L0Ve8-Cd8PebR1gH72lc1bhXrY9nPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqrzBgfPHdKAfnbNzQ66bUiDBuvPYPK9Ofg42_Q7aKdbNcRnZMmgrX72Q7-cnBki63hWpUYGlpxzh5KNH7X-HoNm3b3MJ2ljddCgIoPIfWEkhwCkywEmQrbWpi590yDPJHTCIOZNnQPIM__69zrRUQuqDI9SDMn0WrOGt6LsfzCI6_Xu6lwKuWlWRtYLbCN_a_eSw7i41evJFdJEeUw65yf4_jLMsIwGDKaIkGM1Nt-w1elx9vQ5uPYI5b58yrFDdBJOIXWwpIeOtxDpxFYsKJ0lXI1EUruvCsfIaNhhdZQ0QdowQR7RYKtmUkFmhTb56fR8vGZiMBJ3evdzGVV8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sdp0DMC_W4t_sE1R_t8mMpJLtOrpUP7KEhNj6Jes-5KtV3ld8zm3IQdF1vrk8MmkgbcaFVjpKA9DJorhPMUGQKH2gqb_X3petNqem9aPyUqXN9UMOhFGe7KsXAEcZt66RimLtKePtCONxe83wU9ZXh--0mUaB9pYVlpN1GCssEEp3aKuCP-aLzcYansNeDRzUTBrsG21wouJ6IGw3DzjtMae5wNQItQ4PHPWaGrFTYQrL07MRsRWMQuBAPxDFc0DBzIIPBCwaJOnTN2HHAOuGXTVTddsIEy3epHJvN1xtNCFBeWDv1KTYLHyBvor6mjHp-2aKiZZSTKE7EEgnMqWBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmi-kutsgfjMk9HqtI4umSPQx8xDAfNlXCMA1ShvUiodowaQ2IR8ttTypR3Mo5NdzyRafgp2I_vp7hn042ONkx7rmJnQmkVqlMu2KrvNxcbVZo-1jhiBweX-EH1YbpvFHABI4Le3LxuicOXXXHKF1m5TMkiZHuYshmZ0sLdOjLobb7zNaR_vjqsClfuil-EQ56EyHIzVyxyGs6_vH2tUHn1kWllfhdcKjbmyOFA00A21tast4wQ-MFrF4Aw5T_AX5qtJbJw9tHnSfhkv12jtc6smdc8Z6JQkMOXLiIpSSsO-JrwNT-MiOaFYD1UoaR6ITzb1FwA9G85nMGRTfr3aqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuks0JJdEhM7ht1mRhrsUOgc5rbhgFkx8T3quJp5da57H4Itk7ZtnnLdG9A77cxy1oJNGCN3aXnM66_HRqwj-dQkEyvd9oF9fBwm1dkN6oMc7hYIK6C9gd1WoMeq1uKSWNTMenVtSB4rTaiuQy-0aNLjLSnPMCSJ53s8KwZy24lrmsesHzx7gacDj5BvbgNPpVjTlXsfv9R_1iOuCrrdCHfu1ErXLOhPC5PXhXpBX5p1VxrIXMIS6rrW8J3fwNgwP4tHprZ1a9g4HdEtaGceQ8kdBx9AyFZdEnFd3yjhYzgBeHy9U1qVOMEPf1E4yc7qDS1u54RXAMomwPwwsB0M7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYlRymn2GiWGsfAPYeGOEHsEpBwwZdaS_KjbdN_imVz9t9FWTLW_c-SRhLmRpuzyt9dXJXkwJM6a7VMBCa1gVcYhB7AlLlcKLP-hR3EtxM3oQKB_rgEDdat7cximsCPvmQonJ65gg0nTE3IZq1k6Pt3C3_PINEPrl6Heua70ygS_NoyqioTxzo-6R_MOK6nW6a2ci6HZnasfbZsqlw5o7fQL09qZ6PYaUIMSSuGC1gdwIH6-KB4dpsdXAN8xX8yKi0X5YMyy90FHK6KoaCHNB7ov6ewJbQGEhL0lhyAm2lmhoCocvyEOSVS4sLrNWxtrt604WrwojVFPE3fo7wnBjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برگزاری ویژه‌برنامه‌ محرم برای کودکان در مرکز شیعی بنت جبیل آمریکا
🔹
مرکز فرهنگی Bint Jebail Cultural Center در شهر دیربورن آمریکا، همزمان با ماه محرم، با برگزاری برنامه‌های متنوع برای کودکان، نوجوانان و خانواده‌ها، مفاهیم عاشورا را از طریق قصه‌گویی، بازی، کاردستی، نقاشی و آموزش ارزش‌های اخلاقی به نسل جدید منتقل می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/663497" target="_blank">📅 17:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663496">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDXHTH6R_PrgXLyJPpPxdxaj2M_pw40-EcFF23LxQk6gTD0I8t9mhnKfZDyGBw60GslwgK9iapdp279ULz7xT3Zpi3tVwFmCnhDdYs7fM8rTRuGaw9ApHJlJdwfR3v_zD8tML066tOkKk89pxu8UydZojGMNqm6n-9iC5uU_GXNAc7a8flPzvZBSecK_mLW0fP_E_mbzH7bbKUfgIe2YX0HoGdBp2un-J0eSyB7bz65o7NPR85xJz-ctFStgfWbd8FuGDcQXsr3iIGfftQnxRGnOgA8QIIBI950GkKYZ6YsG0S1K2ta2w8UnM1D9Ph47VBDq92l_Wl1rQ3ih-FjcfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید «ستاره یک» منتشر شد
🔹
«ستاره یک» اعلام کرد نسخه فعلی این برنامه به‌زودی غیرفعال می‌شود و کاربران برای ادامه استفاده از خدمات، باید نسخه جدید اپلیکیشن را نصب کنند.
🔹
از این پس دسترسی به خدمات ستاره یک تنها از طریق نسخه به‌روزشده امکان‌پذیر خواهد بود و نسخه‌های قدیمی دیگر پشتیبانی نمی‌شوند.
🔹
ستاره یک برای کاربرانی که به نسخه جدید مهاجرت کنند،
۵ هزار امتیاز هدیه
در نظر گرفته است؛ امتیازاتی که در قرعه‌کشی جایزه
پژو ۲۰۷
قابل استفاده خواهد بود.
دریافت نسخه جدید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/663496" target="_blank">📅 17:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663495">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0347f806.mp4?token=bGssg1rWBbg98Q1ujtYyfCKvmNgHjUntwFWqOQjQdxlrQWBIqzYKcZnRTyTmmn_-zv5EcDGC9PQehz8gTiTUaewGXHNZ1p3Dld4wVZWNflRnbXI6uQTKXJiOn5kJlAVRLWdDg9GH7juLtofXpojFDv7XfonQwwazN76uDA0awhiGilrlAG7gtpHr09f_s4HyYFyeG4WLeajPTzfsXbm6ZlMpKz5HV0Jd6TD8saloEL4B6ErhYbTIzpZS2o7E6OLc0_0n9SmNGo-WkR676ZA9jV58MPMYqhOFqJS33CAU4crzr1B0LE143C6nfUE-rVV3dv1kG-FPiCV9exOIzT47vxJq4oCCZmUPvuDFwZIsElwZXJmskLQ6JZvhrShVGXAptPCIYRw19QpSM5nMFlI5zEE-UEuEsKRz_Dh-pquYeptokmNVcaQMJG3aZ1YMNeVR6oh2kudUxQOxgsema7p2ZgvN-mkNfRaWOLmaazLednRu63f_8T-SyJ4oXltYt-ub5srWXZufCb8tYyEQcQLaUfU2SEgnwTThgeFRtYegRVIuPKl-ccZ5uh2atLzxB6wuDeWGitHGOPt_GvTFX4_7AbYhH_55gS0FQLda1xB1YN6KqOHHqSTXeze6H8xZXWgBxhtJt8WB06wDR2eH1knA4An9VGf3ypMFcKlzl10irso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0347f806.mp4?token=bGssg1rWBbg98Q1ujtYyfCKvmNgHjUntwFWqOQjQdxlrQWBIqzYKcZnRTyTmmn_-zv5EcDGC9PQehz8gTiTUaewGXHNZ1p3Dld4wVZWNflRnbXI6uQTKXJiOn5kJlAVRLWdDg9GH7juLtofXpojFDv7XfonQwwazN76uDA0awhiGilrlAG7gtpHr09f_s4HyYFyeG4WLeajPTzfsXbm6ZlMpKz5HV0Jd6TD8saloEL4B6ErhYbTIzpZS2o7E6OLc0_0n9SmNGo-WkR676ZA9jV58MPMYqhOFqJS33CAU4crzr1B0LE143C6nfUE-rVV3dv1kG-FPiCV9exOIzT47vxJq4oCCZmUPvuDFwZIsElwZXJmskLQ6JZvhrShVGXAptPCIYRw19QpSM5nMFlI5zEE-UEuEsKRz_Dh-pquYeptokmNVcaQMJG3aZ1YMNeVR6oh2kudUxQOxgsema7p2ZgvN-mkNfRaWOLmaazLednRu63f_8T-SyJ4oXltYt-ub5srWXZufCb8tYyEQcQLaUfU2SEgnwTThgeFRtYegRVIuPKl-ccZ5uh2atLzxB6wuDeWGitHGOPt_GvTFX4_7AbYhH_55gS0FQLda1xB1YN6KqOHHqSTXeze6H8xZXWgBxhtJt8WB06wDR2eH1knA4An9VGf3ypMFcKlzl10irso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تأکید کارشناسان غربی بر اهمیت هرمز برای ایران
فواز جرجیس، تحلیلگر مسائل خاورمیانه:
🔹
تنگه هرمز برای ایران فقط یک مسیر تجاری نیست، بلکه اهرمی امنیتی، نظامی و دیپلماتیک است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/663495" target="_blank">📅 17:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663493">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a8e8128b.mp4?token=mKiStlOuULD7v40WxeHkhiP_oCkiTleZIjGS_mkm0ItMUNaBhmZAei-pVOLR8qJyc-UdARcOp-Io-f9gFyFAC8T_Ac0UpVFG3Y7ewt2OjoCk66hI0SGE2Wij5ss_CNoJep9-qMGtPURuS2fkfOdLsCDU_OACUCSuw6N7-xVVCbPp1fOKxCWcqXzeOvasNypGLM3JUFpHOzJ9pDaWAzYefU0hjRWzl7F2E8YoP0gt5h_6ZrPirAJ-QG3rjytOVRgtnOSbtQsu2sCUKXNzWwsiCn6wzbTH7iqEKejyYdnhiO-mcAp8fh25aFvSv01jhSBwppXgnmz9cLb71L4sRWSfGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a8e8128b.mp4?token=mKiStlOuULD7v40WxeHkhiP_oCkiTleZIjGS_mkm0ItMUNaBhmZAei-pVOLR8qJyc-UdARcOp-Io-f9gFyFAC8T_Ac0UpVFG3Y7ewt2OjoCk66hI0SGE2Wij5ss_CNoJep9-qMGtPURuS2fkfOdLsCDU_OACUCSuw6N7-xVVCbPp1fOKxCWcqXzeOvasNypGLM3JUFpHOzJ9pDaWAzYefU0hjRWzl7F2E8YoP0gt5h_6ZrPirAJ-QG3rjytOVRgtnOSbtQsu2sCUKXNzWwsiCn6wzbTH7iqEKejyYdnhiO-mcAp8fh25aFvSv01jhSBwppXgnmz9cLb71L4sRWSfGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
موکب تنگه هرمز در عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/663493" target="_blank">📅 17:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663492">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFqYgsFkGaytdsqABJuL6MAsK_omJ429tqbNHby9dvOyhyA2hhNY5uWFBhO_e5fenzEV03u2ggbKLWb_UCEDbWtZ2owsN8sYWibt-6zsG1DZUm7UcLNYjiItS_PqHfkmqa2pI2H4UisrLRycgJ36YjA-VQwYxyeJ_J3_k94DpuNd3heUV58yMBd_m-GkVxwa1myYaZgVIX-SNhdHsIsz_-V1RfP1sY51OYpUVmMDjcZOS4o6ycMAXfb_MQaiETA3I-uS3shIq_6gWzFEloXHwkIyR8Jb6ROSTxPO1gkkU09Z7Y7JKPAZTTNFnKAevV5vv6extDtNwKK5rR5HAUSxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
وزارت کشور امارات: وضعیت در دبی عادی شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/663492" target="_blank">📅 17:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663491">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYGtBt6E5pe2CnkkSHTnImYR1xLCJWrnyiKD7owdlxURCoPg0kpDOuXjaPC9nEOJ_pDy49H8pM99FUMGskgCX8-oKZE-QPYDPgz1eORPak8LMrlxPvaL22q-CHitwqKvbPbAA-Bty5QgCAt30YrTquYg21BWlBJz2wY_2ERJaNlqX7uDqTnPh6LwD3FtHHd7wzmqAVCwS6ly5CLtu7jIj21v4brKIWbonBI-eahLuV4cR3MrCeYOJIEli0-i2fjLp1GnwaArIdIPowamx48KfohIqCKV5MRDIP7jT_Rrsf5J2a3-s6KqHS3K_PDJVGGKYUUv6ndlYCm8DsxVzdbsOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگاه ششم ایران در میان بزرگ‌ترین تولیدکنندگان سیمان دنیا در سال ۲۰۲۳
🔸
چین با تولید خیره‌کننده ۲.۱ میلیارد تن سیمان در سال ۲۰۲۳، با اختلاف فاحشی در رتبه اول جهان قرار دارد.
🔸
هند و ویتنام، پس از چین جایگاه‌های دوم و سوم تولید جهانی را به خود اختصاص داده‌اند.
🔸
ایران با تولید سالانه ۶۵ میلیون تن سیمان، در رتبه ششم برترین تولیدکنندگان دنیا ایستاده است.
@amarfact</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/663491" target="_blank">📅 17:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663489">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfiOMnBnds5JnwTZ9rlOgT8Hot3A4O76i4QRMWd_IEnz26HlM0Ge14ZUSmDSca6CasHrHZit4VGKcDQ3x1mfbvRwGz8zK9-naJ-vornk5jyznhRn4NdnFkDnxlbUUCcK4YybOiREPSsRxb3QenLn3jDKHd3MEGFSm8vxqfh6ED44F_Hb0IFdkSJvBEKM7YJf4bJIoYIZ1sYADlRbjAL0Tge7Qk1Yrsaef9XPSOxmHT-x53wHJKYTdgKXI9yMRz4ArsUCo_aZTVbVR3lRdHOA3O2TPBzrEoWbuoUAoY4U34JKj99m4-qI38IyN45yl4tWVNHgeKMkQMVgpQj1fMk7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پوستر فدراسیون والیبال برای دیدار امروز ایران مقابل ژاپن در لیگ ملت‌های والیبال
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/663489" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663488">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dc1o1iNQoznTko11qMB6AgCOYxsB9dv5JaIFZBhHt_8kKpktuXynTOau20ULDVxA-9U9H8VNTl-s3YL6rZOJ1e0pRw2HZzM87trDSP1t9Bkc9m2joY3v3K_EHy2pxxikTG4-En4p6T3FNag0tWwVl_cXA5-CBX2wjR_OZvyMlwcn6iLWWh2mGjMma4N6P7-iTkEdzNsE1cczV2Lsvyg7Mw32zlShFlWMvRbBd6ng7DxWAn0_4be701xCmXr85d3u-1rrnPqv2tFfo_goH2bnCAr5sopVm7paA5WglyqtgK6UVVL-kJw1yKeQt-O3PwTUvj48ihmlcMoGH8hRaRBeyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
شنیده شدن صدای انفجار در دبی
🔹
منابع خبری از شنیده شدن صدای انفجارهایی در دبی گزارش می‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/663488" target="_blank">📅 16:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663487">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔹
شنیده شدن صدای انفجار در دبی
🔹
منابع خبری از شنیده شدن صدای انفجارهایی در دبی گزارش می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/663487" target="_blank">📅 16:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-0aoX20zgB_ryUz2BJekIig0Sm9fI6yyFb7gwnnbzNh0WIXvUk1XNnjO-uVOI_ilPvjL_M0KrLVMgABg8JpJpDpPJrgcY3gHo2LMEvUJYvbeL3FoU5r10Zmz2392SRS47piG8mqSdYo7QVpaZq-SeqXzns41d-tJ9IZgDvzgAcjw856oLwQHyutcMBvYySPE40PsYSIZNiCzG-28M29V7OY6tj4Brqz_yqIeI_SPvhC3x9U94krKqwlfxTi71L-mjO3W6bBRehi3DMnTEt24SehiCagzUC0-9t7IH5PCXbeDcAYKMcjtNFzv5EvjAqWjl5aZUQqCNee2kYk0i8OYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سخنگوی وزارت خارجه بیانیه مشترک کشورهای عربی و آمریکا را «طنزی تلخ» و «نشانۀ درس‌نگرفتن تجربه‌های اخیر» خواند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/663486" target="_blank">📅 16:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a2e0060c.mp4?token=JJO-6IUp1csnjtVd98IBINHCNDo1209dILmtre-DZRxsMnbzZdwKaGZksksyhb1mJX1N1GizUpGFH36fPGl5g-GQgYpG-_1kRK0osqvowbX5J0wn37l9SFNXHDyZ--nP0xu60jGkHGfMB-SDITRLCWusiXz96B2HQ83qkbmXSye665fHYv6GU6JJ_7Ii9n3miYO2yCI-YJU6lsH8r8HmiTF9FLLSqkff-n2lcw3BJpIDDGpn0U1VWClP9wGqWlhrDx_O_M6xYJqiSNpsw73mhw2gSEBHO5c8o4FZd5eJH5DaYgV8oSFkENsa8dPYH7tKp4evDSQmRNJ139k84fTbpCyVwf0XgUa0ZkJs3X_0uNYISFkYjqYCNnMPGCl_Qd7XEHZrpw9GeIH3JyM-uykRSPeE_bVm2Yt4lrXRXXC3QA_ckEBrjLyrOT9M3qwGIxc8c9-NDVcHG8fymZh6UUtbZWKbRPUWt_hvtQthEzVEAj0hTm6JySqw77weaM5BSMo2fsPg56IIbByXkIueb28EfUBC6uflcSGx3mnhgsvvJTWLt6ndej7sqso0zjXuSGEqD4E7VGDHEf-Ha-737I9Rd5b2hdxghAPBNlZsEMg8uCCbRDc_Li6bY5Xr2a3JYZHOK6EBJIzvMVIe4YZTCfX6RynoS5TO8WvX-iZhRoWUuuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a2e0060c.mp4?token=JJO-6IUp1csnjtVd98IBINHCNDo1209dILmtre-DZRxsMnbzZdwKaGZksksyhb1mJX1N1GizUpGFH36fPGl5g-GQgYpG-_1kRK0osqvowbX5J0wn37l9SFNXHDyZ--nP0xu60jGkHGfMB-SDITRLCWusiXz96B2HQ83qkbmXSye665fHYv6GU6JJ_7Ii9n3miYO2yCI-YJU6lsH8r8HmiTF9FLLSqkff-n2lcw3BJpIDDGpn0U1VWClP9wGqWlhrDx_O_M6xYJqiSNpsw73mhw2gSEBHO5c8o4FZd5eJH5DaYgV8oSFkENsa8dPYH7tKp4evDSQmRNJ139k84fTbpCyVwf0XgUa0ZkJs3X_0uNYISFkYjqYCNnMPGCl_Qd7XEHZrpw9GeIH3JyM-uykRSPeE_bVm2Yt4lrXRXXC3QA_ckEBrjLyrOT9M3qwGIxc8c9-NDVcHG8fymZh6UUtbZWKbRPUWt_hvtQthEzVEAj0hTm6JySqw77weaM5BSMo2fsPg56IIbByXkIueb28EfUBC6uflcSGx3mnhgsvvJTWLt6ndej7sqso0zjXuSGEqD4E7VGDHEf-Ha-737I9Rd5b2hdxghAPBNlZsEMg8uCCbRDc_Li6bY5Xr2a3JYZHOK6EBJIzvMVIe4YZTCfX6RynoS5TO8WvX-iZhRoWUuuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کاش از ایرانی‌ها می‌آموختیم
مجری مطرح عرب:
🔹
بینندگان، شما را به خدا قسم خودتان مقایسه کنید، ببینید ترامپ چگونه با ایرانی‌ها رفتار می‌کند و چطور ما را خطاب قرار می‌دهد، ای کاش از ایرانی‌ها می‌آموختیم و اینگونه ذلیل نمی‌شدیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/663485" target="_blank">📅 16:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663483">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
ادعای پرس‌تی‌وی: یک خط ارتباطی میان ایران و ایالات متحده در تنگه هرمز ایجاد شده است تا به جلوگیری از بروز حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، کمک کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/663483" target="_blank">📅 16:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663482">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkvdCbqC2C9bAOupC6LReUy7ut6_RTlEbkzE55KIfKBhqQWM9yd65gZnOOyWj6UE3eniGZ4gB91F4rY-pD-A6omquRg8pJt7VBXtWtYDxFVpEP92nn8k_Nwv4TjhGTqRT1kAa5XP5X6bLdNK5hDuB2O7foSbs4B1hXceu48jxKV068KfOC8LRcZzG80v0NTeAf4ksbW6EmERri40LbTD7F27j-bKayFA0zCryPmrMc9hEI3tBO5oOa0H5P-kT8IF3uQvAVUMobK-ZBgSINwL3jrUUAg1cOyz3OeZsuLBbnKt5lkxiA5sqj2I7WHnSS73MRBHiwWRaQbAE_TepGKruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام سردار قاآنی خطاب به سربازان تروریست ارتش رژیم صهیونیستی   فرمانده نیروی قدس سپاه:
🔹
سربازان متجاوز و تروریست صهیونیست ، کمتر از ۴ روز ۱۰۰ نفر تلفات دادید!!!، اگر با پای خود از جنوب لبنان خارج نشوید، حماسه سال ۲۰۰۰ بار دیگر تکرار خواهد شد؛ همان سالی که…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663482" target="_blank">📅 16:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663481">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔹
تلفات زلزله‌های ونزوئلا به ۵۹۸ نفر رسید
دلسی رودریگز، رئیس‌جمهور موقت:
🔹
درپی وقوع ۲ زمین‌لرزه پیاپی در این کشور، دست‌کم ۵۸۹ نفر جان باخته و ۲ هزار و ۹۸۰ نفر دیگر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/663481" target="_blank">📅 16:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663478">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔹
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
🔹
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/663478" target="_blank">📅 16:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55fc979037.mp4?token=tHkvIqCtiL3Mk31chjHNkNxJr3kZKfL42OsSjj7mCZZEa7pr8H3MCBVc2tDeg8tb_UqOmdTM8lv2a_W5Fbj8RXTAamhqsUlpGaTzQdzrWc0S9BJscVgSO-XVe85KWtGDJX9CHQDJDxAnD-zgCn9cvvZEbq8T7PbvAGKS4ExmHFlf5Ycj0kstMoJhoDFPujwbS2h7A4RSgKxdQo2coD0B3tRQTulROZEe0cWf9yypdgm89D23XR-N3sr1BkSFRVlWcy2CeTw4SdtdCDCmNgtxu-3SUGDgec9NSi2rqapdN_mroyNhhklxc2kATrInVBxmm40NjK-1a2mdlZx0jdevBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55fc979037.mp4?token=tHkvIqCtiL3Mk31chjHNkNxJr3kZKfL42OsSjj7mCZZEa7pr8H3MCBVc2tDeg8tb_UqOmdTM8lv2a_W5Fbj8RXTAamhqsUlpGaTzQdzrWc0S9BJscVgSO-XVe85KWtGDJX9CHQDJDxAnD-zgCn9cvvZEbq8T7PbvAGKS4ExmHFlf5Ycj0kstMoJhoDFPujwbS2h7A4RSgKxdQo2coD0B3tRQTulROZEe0cWf9yypdgm89D23XR-N3sr1BkSFRVlWcy2CeTw4SdtdCDCmNgtxu-3SUGDgec9NSi2rqapdN_mroyNhhklxc2kATrInVBxmm40NjK-1a2mdlZx0jdevBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
محبوب و مردمی مثل کریم باقری
❤️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/663477" target="_blank">📅 16:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idoFQzU-NtSTWXSYGFFyYSf3gGwaEA3T3YdgHqSNTRG_YBu9YfF0rQ2yFLF6PV7THzWViQXwBlgfbwXg7F_fas0rkNBhdwMfTcrZcHnzfXmI_ASOnOO99gD3A9H35oO8Hx-YOfIUpHEbzqDLVvNPq48Z-a31-xifyy4hMjhvrddGHcbYm9Tagh2GXY0TrJT5rNtpRB9swrjCwE8pakRBv-pz_Dz5h81KNovJgZE7xjt0RE2akmj97yzxrmK77_jjpq9kBqIez_L7zZvwgKLjPRK7Q-JRfd3Uig6s5MFnsAQ1c3qbnXQ20kwjBOlZwHTR1adKZHF55HzIHK7pe8-45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کیش به مبادی مجاز «ته‌لنجی» اضافه شد
🔹
جزیره کیش به لیست مبادی مجاز ورود کالای ملوانی (ته‌لنجی) افزوده شد؛ همچنین مقرر شده است تا ممنوعیت‌های اخیر در واردات لوازم خانگی از طریق رویه‌های ملوانی و کوله‌بری، در جلسات کارشناسی جهت بازنگری و اصلاح بررسی شود./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/663476" target="_blank">📅 16:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663474">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d190b96eff.mp4?token=ozYtYRDBsadMErhXf5USSLqFYlS-CDIJwjC3ei-k52Khll68ODPVqQfCUWHIRPkz6yi2ZjGPWDuxI8ngvPiaTNohw69DufqiyBb0rXQLUTFsHq9_sq7RAXxi4mluvJ79C_W5sSEMzVtBO2IqNjSV7VOhdAWr5e8d0naqBTdoaAJbzp3V0bp2DSVZKyRERmZzcNCxemThg0w9Mu439qEP5Qf9gB_B99r2G1jqfV2uixwFqTOMGOzxfSTfbc3sp_wcNSQOzeqzxZEyHCEKzmLyk4CBJEkXme26cv4-3NzakllWZ92PaFq9o7hpEJSpPRPwOejTtyUOxneMIA68tmYwaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d190b96eff.mp4?token=ozYtYRDBsadMErhXf5USSLqFYlS-CDIJwjC3ei-k52Khll68ODPVqQfCUWHIRPkz6yi2ZjGPWDuxI8ngvPiaTNohw69DufqiyBb0rXQLUTFsHq9_sq7RAXxi4mluvJ79C_W5sSEMzVtBO2IqNjSV7VOhdAWr5e8d0naqBTdoaAJbzp3V0bp2DSVZKyRERmZzcNCxemThg0w9Mu439qEP5Qf9gB_B99r2G1jqfV2uixwFqTOMGOzxfSTfbc3sp_wcNSQOzeqzxZEyHCEKzmLyk4CBJEkXme26cv4-3NzakllWZ92PaFq9o7hpEJSpPRPwOejTtyUOxneMIA68tmYwaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویر هوایی از مراسم عزدارای ركضة طويريج در کربلای معلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/663474" target="_blank">📅 16:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f26aab3e5c.mp4?token=Aw1IByCHrWN2lQNn1C4_AAqeBa9xCvIefCTnXXbTBwrRT8WCbNLY5dFruXQ_QLAaBFVbPz63wYItyWstspUTEQmWx0LC4Qs_BQcHZcGA9Hz3x96fbBRPeoTKLVrdBsXmpuw-PgeCeFyOJ0CCRcgF4sNl5hpba4_p5R3YDUyDaaU24eGT_zIXh7vQKuXpI6t2H6sa-rjNNQQraPYr9pTSbfAwB_kYni5P6tDMO99ZwTS08q_ThP8vWC1_ArynTTFIJWBEEPNDYtmhnoFX2L81v8AAUSsa2LzYxboLFcyvSW7n0vvG72ChLO0q1feR7afMmtMkBWbzs2UvEKaf9fLcPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f26aab3e5c.mp4?token=Aw1IByCHrWN2lQNn1C4_AAqeBa9xCvIefCTnXXbTBwrRT8WCbNLY5dFruXQ_QLAaBFVbPz63wYItyWstspUTEQmWx0LC4Qs_BQcHZcGA9Hz3x96fbBRPeoTKLVrdBsXmpuw-PgeCeFyOJ0CCRcgF4sNl5hpba4_p5R3YDUyDaaU24eGT_zIXh7vQKuXpI6t2H6sa-rjNNQQraPYr9pTSbfAwB_kYni5P6tDMO99ZwTS08q_ThP8vWC1_ArynTTFIJWBEEPNDYtmhnoFX2L81v8AAUSsa2LzYxboLFcyvSW7n0vvG72ChLO0q1feR7afMmtMkBWbzs2UvEKaf9fLcPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قاسمیان: مذاکره‌کنندگان وصل به شبکه یهود هستند!
🔹
اجازه مذاکره صادر شد تا منافقین به مردم معرفی شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/663473" target="_blank">📅 15:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663470">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔹
نیمکت‌نشینی گران‌ترین بازیکن مصر مقابل ایران
🔹
سرمربی تیم ملی فوتبال مصر در دیدار برابر ایران قصد دارد چند تغییر در ترکیب تیم بدهد از جمله اینکه عمر مرموش را نیمکت نشین کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/663470" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663469">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5a6136739.mp4?token=t_auHjKYjpFMUagc5tqCoKVE5g_pp9GdRzwNeHuCDlv6bg2KbKWuTIhkPvlW5jdHYJ4sSz9iecPqrPHpn0Jih7bBoO0iP_H0CdopifLfkWuBu6DxGNXiT8XRfYUK1S53OqrlAvpmAi08J_5VZCqgxURcdt2MoGcnYvnXkvCTRzO1sdUO5sLpmT5zilHkA3EcEnjX_njFvzuJ9jOb8w96ILq9i1EIsght0Ywiq0S1ZQfFSAGUrsKusyYjkt2lM9G6C0BBgVh-XURgAq5VEHtFGDPqM9C2eSf-94bJYgM1teb8sZCv-O9KFJ6LUTgD-uImW1E68gv49ILULsP39KIi_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5a6136739.mp4?token=t_auHjKYjpFMUagc5tqCoKVE5g_pp9GdRzwNeHuCDlv6bg2KbKWuTIhkPvlW5jdHYJ4sSz9iecPqrPHpn0Jih7bBoO0iP_H0CdopifLfkWuBu6DxGNXiT8XRfYUK1S53OqrlAvpmAi08J_5VZCqgxURcdt2MoGcnYvnXkvCTRzO1sdUO5sLpmT5zilHkA3EcEnjX_njFvzuJ9jOb8w96ILq9i1EIsght0Ywiq0S1ZQfFSAGUrsKusyYjkt2lM9G6C0BBgVh-XURgAq5VEHtFGDPqM9C2eSf-94bJYgM1teb8sZCv-O9KFJ6LUTgD-uImW1E68gv49ILULsP39KIi_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تلفظ اسم بازیکنان بارسا توسط برادر یامال
🔹
به لواندوفسکی میگه اِلامانوسکی
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/663469" target="_blank">📅 15:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663465">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IY9O4xr28q6rkV9Srz615bGa8tswJ3bb05NljcyX1sJum6hebLmmv8Pn-L4rC4VAAoulJgY9feJbTQawAUU6wM_oIRxadSi6GKbLvCJOvPkYcTNPYsRR7VSNjDXbH83Tr55POkipgeO21lNeTAeq-GxtslF90_udoTkSLu3W91ce_V4oN8o8r4fJWPG-QMo3eQmEDCg3cWQUk_gk2Nh_w7Rtq_BMZBve03JOMAmHFx2h-Nk0G59MRNCq7kdeyV-wsDLqUtOrZl3pPL13FPYf7iloR8cIwkit1BHqqyfXsR0PykbjEut99ludnQuobCsosYC-AAXdDo4mDhs-cElexQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivcR9OCj35uCHA7K9tN9cIju0_penT7RLjfUAo9YtEjw2FnVezFprD6we7RwFsr82Dor6_-TOWsi8a0ZOSiCsJ4278TuZjP5x0ymlJZL-auztXg3YEWxlNotMHahsWTfYV-63yw9bL_IdvstcWf4aH6_ynV3kpmzwSvGIRTdaee5veX8nxvUM50cGNgAhuojRCCYtm-tij0Li_mQ82VqSzarAr86vV5KNhQsOJk_QSQDy63e7QzL7zxC5UpESl8q7vf9lN0uTCsSEIggLAc_JeGklYHwlvOAFfw7PYJAcnkn4fLfFKpgGULiE8KQ7EVKqWe5Kc66MGBFA0fGDdcBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAWT9xtaKwTKrAUSL62tTqjZqfbnOxhLRQFY7f6TFE8-MX6kznruHkbaFhPUvqmm2QOtKiZT3Hp7TK0OKJLuUY2GB5G6mtNEzIPZ1BF861N8RM2d9uy_GHeA1IgOwC6fV1vyQr358pZIjQBcYNwMswpfrhSQ7TKIAeD_MZ1ZYVX0BwaORO1I2EO7GSfWMMRaZ_VyQVXSvEZTV_X-8XBn5R9z_de-a08hhTpX9kkToq6IgHcQFoSbVJ7BTqz3PmJGMvUrodUEkEaUsk9_By5-QNsR1U1jy1SfXXp8JN-O4pyJmOh1Hd_pjecIoYJt9c_1gJgPCy7hbjGKg_a-QoO9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcNyrEGKtoOA9i167gxLp4DdFauSx4mcFTVPtZoi_TspcmBrY84zAz-baXdISgSzz1ArXkYKY9L-WJnriI3W-uNUET-b7-J3LVpSgRPhh2Z9N2zs7XIvNALUVnwbHRDpxtYuYZofwCFgHdHMjo0HkeDsFQVET43N8VpvJYqDLH5SDS52zx3wwU0rldajJ027aIpezx_pCCFFREnGxfj9In9KG_iGLaaIztN5GWxxCUWBOKEuEEWo-_ZoxbA5HNrwcCeslYl-6PmBTX14w4ro_oDujDVCyDfy-P5gjXfMoCvZ4oOUIwEnC7oyBOdgxvEDOmnNXZoQiPka3bvVSJ1pZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
قیمت بلیت نجف-تهران و بالعکس چند؟
🔹
با افزایش تقاضا برای سفر به عتبات در روزهای گذشته به منظور شرکت در مراسم تاسوعا و عاشورای حسینی، قیمت بلیت هواپیمای تهران-نجف بسته به نوع پرواز، میزان بارمجاز، ساعت و روز پرواز متفاوت و از ۲۱ میلیون تومان تا ۳۲ میلیون تومان فروخته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/663465" target="_blank">📅 15:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663464">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41b8f262a.mp4?token=pJeMS9IokKm47iQ3cmmJRjaHz42bJ_B-uq2Y4M9o4olXLHGjhQEel5Lc6zIxAU2bg-YxpNLv8mLwQ_c3sVt2dP6hA5pVcB92vCwIqm8431wFRVQZYHJoKXNTxuwtGWlJyMGUcv76Jn3x-2VpGf_O9lqKHKHzcZ_r7wy8ybha2T05hYMu5bJ2BPCNtdM2WPhzqKsa67bkkHKBGqPo1LXDlz2VRSWxvouALXHC37VIGz3yF-BTDvuuHPLTNPAF-rrKETXWdZ3_KjfRJZz0QZ_xcdgX1vxn-MqDmtDVRGhnNHPjs7eBF9Q2OCv_MKytyckQ8dYlfPjlcXBn7-j1muAUTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41b8f262a.mp4?token=pJeMS9IokKm47iQ3cmmJRjaHz42bJ_B-uq2Y4M9o4olXLHGjhQEel5Lc6zIxAU2bg-YxpNLv8mLwQ_c3sVt2dP6hA5pVcB92vCwIqm8431wFRVQZYHJoKXNTxuwtGWlJyMGUcv76Jn3x-2VpGf_O9lqKHKHzcZ_r7wy8ybha2T05hYMu5bJ2BPCNtdM2WPhzqKsa67bkkHKBGqPo1LXDlz2VRSWxvouALXHC37VIGz3yF-BTDvuuHPLTNPAF-rrKETXWdZ3_KjfRJZz0QZ_xcdgX1vxn-MqDmtDVRGhnNHPjs7eBF9Q2OCv_MKytyckQ8dYlfPjlcXBn7-j1muAUTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
در آسمان روسیه یک ابر رنگین‌‌کمانی دیده شد که شباهت جالبی به نقشه ایران دارد
🌈
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/663464" target="_blank">📅 15:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663462">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a549d6b41d.mp4?token=aqMfvyQJP7x7DseEudAYJK6CxiTK7SUkj2Jp3sfwzQ_ZIWNSbXJXbNT8wGVhUFZw7nqRrYlTiJRd59FWPKy-ba1zAzfLwXwZ4ywsh3CJXQd3cd4C6XSUpV82JRmsUETFYTXIsDjtuXVu868bbjzx5_UEGAJxS8D8iWJiwAaWM7VgWdcFs_vtGFazN1La5U1iT30fYj7XohnS2dE91G-Y9ZIfJMsnnm8S9GCzx2Po912dMGX6Y1_duH4eeYl_Z9YBY3UM1FdoqUcC9wnLH1rSd83ovPLOu7x5ONVJL9HEOqKlHnC6WP8tclZS2r8sqx675zj6QNGtRx9T1olgwE50fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a549d6b41d.mp4?token=aqMfvyQJP7x7DseEudAYJK6CxiTK7SUkj2Jp3sfwzQ_ZIWNSbXJXbNT8wGVhUFZw7nqRrYlTiJRd59FWPKy-ba1zAzfLwXwZ4ywsh3CJXQd3cd4C6XSUpV82JRmsUETFYTXIsDjtuXVu868bbjzx5_UEGAJxS8D8iWJiwAaWM7VgWdcFs_vtGFazN1La5U1iT30fYj7XohnS2dE91G-Y9ZIfJMsnnm8S9GCzx2Po912dMGX6Y1_duH4eeYl_Z9YBY3UM1FdoqUcC9wnLH1rSd83ovPLOu7x5ONVJL9HEOqKlHnC6WP8tclZS2r8sqx675zj6QNGtRx9T1olgwE50fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شادی جنجالی سرمربی تیم اکوادور در پخش زنده تلویزیون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/663462" target="_blank">📅 15:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663459">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGXI1dJDoG3BSl2OwgpnEkED34sHMASIFInx3vKefA0mLAyNcYFCeuJBkCvnbV5yjypzRjCnUuQPaVzVfLYnGl8VPAQeowAxa-DgS8a5jjNvN6zul0CYNuMx1JXBGnAS0AxNSyplZvDzbINZiZIoi_o0LbDglOzP0vQbhn-ZMPRIgCJki2k3a6Q5NyWh1M1BJxQYDBC0P4DTVHl5xfSAglryd5Ep-wxB-jxwjo7X9p_PPAq5CwzH-292IBwJOjiAVvHrsAR27m5m_DNECzH4Gyj69Ftd6HSGHBwIRjh_YwwaRGim0_2NWK2ZxN9GAZwe9jPwJKNC8rU0X20KIXKrTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/663459" target="_blank">📅 14:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663458">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74883fc491.mp4?token=uuZDMw1I0L7W3daKjHknfuwUmqsHcWgUdNtXZQEUzTzaMq1WT4K66KoSmhDul1q6K6j4QJZXuhvzoVUp7V-r396wwrXQualAlGHcEJMCaemI_ve-4XUmtKtsC7ray7ap30FB3S98Sx3wUvsj-dcoovUJl1AW8AkDz8qJ6-fS4hLhzNEJ0Ibn-Kq-YV_0zMlrX8DLHqS-WzQf6v4lFEHDAI3y-SRWYI_gHaLEVtoJugAfADZRGIGDHeMDuvSitnXJJZZT27q8nafVWIxZpi9xX0bnd9jOu8jk4dktrx9GzTUdsSJk95YGLmUF62QSnEIeOtclcz8ISw4Kf8zzOTqQ5Q1oXaqOK05yfxQ6QbVN06xwcAmFfi8iHRj8pC4B-Saz_jSEAQtIDhcTEp_Boyuq-0QJTCZSPDNgVAUijPqvEZ2WtlJf2H4PjCSGiBP6xHX-PNFbpmwdMbpaBdO6s9tgbK4Y9WvE7JgXNdpaGxRGF9zFbYDTJ4jzr21iZE2iZuNLLaU7oZ1LLBzDCqNXt0ZcXEM9w_n5_iOovdur274eX9zJj-8Y-S7Ax34PQu-mwlD7hhtghgLpEPj6D7-6_lzgVlWvyrNoLhcjtUQaEK1MZNvYu-M_jEzFueKuEcVPS5TU0Wuw2v1Z_vG2tqx6qe6yNGuFmWxHtP9LEcpHTUocFLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74883fc491.mp4?token=uuZDMw1I0L7W3daKjHknfuwUmqsHcWgUdNtXZQEUzTzaMq1WT4K66KoSmhDul1q6K6j4QJZXuhvzoVUp7V-r396wwrXQualAlGHcEJMCaemI_ve-4XUmtKtsC7ray7ap30FB3S98Sx3wUvsj-dcoovUJl1AW8AkDz8qJ6-fS4hLhzNEJ0Ibn-Kq-YV_0zMlrX8DLHqS-WzQf6v4lFEHDAI3y-SRWYI_gHaLEVtoJugAfADZRGIGDHeMDuvSitnXJJZZT27q8nafVWIxZpi9xX0bnd9jOu8jk4dktrx9GzTUdsSJk95YGLmUF62QSnEIeOtclcz8ISw4Kf8zzOTqQ5Q1oXaqOK05yfxQ6QbVN06xwcAmFfi8iHRj8pC4B-Saz_jSEAQtIDhcTEp_Boyuq-0QJTCZSPDNgVAUijPqvEZ2WtlJf2H4PjCSGiBP6xHX-PNFbpmwdMbpaBdO6s9tgbK4Y9WvE7JgXNdpaGxRGF9zFbYDTJ4jzr21iZE2iZuNLLaU7oZ1LLBzDCqNXt0ZcXEM9w_n5_iOovdur274eX9zJj-8Y-S7Ax34PQu-mwlD7hhtghgLpEPj6D7-6_lzgVlWvyrNoLhcjtUQaEK1MZNvYu-M_jEzFueKuEcVPS5TU0Wuw2v1Z_vG2tqx6qe6yNGuFmWxHtP9LEcpHTUocFLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
خبر خوب برای عاشق‌های هدیه دادن
🔹
دیگه لازم نیست برای خاص کردن کادو، هزینه زیادی کنی؛ فقط کافیه بسته‌بندی شیک و خلاقانه داشته باشی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/663458" target="_blank">📅 14:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663456">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔹
هشدار نیروی دریایی سپاه: عبور از تنگه هرمز فقط از مسیرهای اعلامی ایران ممکن است
🔹
همچنان تنها قانونی که بر این منطقه حاکم است، قانون جمهوری اسلامی ایران و نیروی دریایی سپاه پاسداران است./ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/663456" target="_blank">📅 14:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663455">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📖
اگر قرار باشه روزی فقط یک آیه قرآن بخونی...
همون یک آیه می‌تونه حالِ دلت رو عوض
کنه...
❗️
🌿
گلچین بهترین تلاوت‌ها، آیات و تفاسیر کوتاه قرآنی همینجاست
👇🏻
👇🏻
یک بار وارد شو... موندگار می‌شی.
@Heyate_gharar
@Heyate_gharar</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/663455" target="_blank">📅 14:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663454">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ff56f338.mp4?token=MZBVJ0-6-nfPGL9wvHHIyeLZWvTk60viXA2dMdgJq5wPDz_eWsvKH7oV9CcI8wdVsdmSpfAdFovsuDEuzBKWKhO_KH62h1qRvDsd9j0pVdd2Wm0pfjRcuMmB3MgnaTLPez3UgMNDuzSYTtWxjBj9WB9nJB1J7Glx-x-LJyWe_ELuGuwWgDqSI7Cuc9J0AyBIvIZ1AXhR1hkpG9gOTRIyjS4HJDcCL1lcirnY4YkoTi1B5m-Gn3xZTb1aTW_Y6Xn9596c9QGW1NCZ9DebyJbG_LCtGy7USf5Q31tAXUwxruXKXjmBuKjMcIqFmcdFVX3zqARD2c38MY4mh52sJsaF0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ff56f338.mp4?token=MZBVJ0-6-nfPGL9wvHHIyeLZWvTk60viXA2dMdgJq5wPDz_eWsvKH7oV9CcI8wdVsdmSpfAdFovsuDEuzBKWKhO_KH62h1qRvDsd9j0pVdd2Wm0pfjRcuMmB3MgnaTLPez3UgMNDuzSYTtWxjBj9WB9nJB1J7Glx-x-LJyWe_ELuGuwWgDqSI7Cuc9J0AyBIvIZ1AXhR1hkpG9gOTRIyjS4HJDcCL1lcirnY4YkoTi1B5m-Gn3xZTb1aTW_Y6Xn9596c9QGW1NCZ9DebyJbG_LCtGy7USf5Q31tAXUwxruXKXjmBuKjMcIqFmcdFVX3zqARD2c38MY4mh52sJsaF0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ریختن بنزین روی گدازه‌ آتشفشان
🔹
وقتی بنزین روی گدازه‌ آتشفشان (که دمای آن بیش از ۱۰۰۰ درجه‌ سانتی‌گراد است) ریخته می‌شود، به دلیل دمای بسیار بالای گدازه، بنزین فورا بخار شده و به گاز تبدیل می‌شود. این بخار بنزین با اکسیژن هوا مخلوط شده و به سرعت مشتعل می‌شود که نتیجه‌ آن یک احتراق انفجاری بزرگ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/663454" target="_blank">📅 14:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663449">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdL7coCgkB0p6nqoKeQiHyGsnWyvooinQ81flO1cphjPJO_sqhmAa5I7-F8zYhdHesDWSrTRvmsnfaDkdtsjBcP6ji7bOozi4WdQCINOYRtEmrmyzATO8jsDtpXzrnm4qbMki44pq8uMMF64dS9v_qRPaC8uu71ZKb2hDxPTTAcfqnav_JkmMlYjnn0ulnErlRIO2wlSkOflE9siQe-2-r48eYlAn2Nznt-hFKNyVnXur4EUD43FRTmsS0mqVQNiV13f_4feNxMeFluHyK_D2mwmZD_nzdB4HDwb8JGLRoMwo3HchCrmWbKMaOPql_WV1PwCYoP_M6LMHfrhd58i2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAs1fWlojLMLfOzAjhPCXLWaarchLqKQ20jhCRuOZYTPZtin144-fP-DInYsEsj379Dnq6QmvBpr69aLaEJvKxG0ORLckR4zKA3zMlXQNhFJlgp4V-kDuD0QkLNa09Zn0VaDzf2HcZgHLqaRi3X7H1qPqvtADSp5R7XnaPNeDPuKUCvrobLzLxW74GS6kUunq9s6M36xYNmLGiW-BFtVg0pWQKAEAxPN1IS4rYFSR-S-yZMRuTy5xwSrxKxYjvc7eiekGp_JzDwM0_09RABxuO6rj1OaZhdVS9QuaCN9GJOjYgNb9P-K4g-Ag9Zq6fHM7QqjA0MLxRif-MGJ8DwJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJiyPoaOoYLX0IjlsRLvsGJ0rlxW4Hg5NZ-137Mvv31rQHYcKI1f8Wdg4SaeJ-IDMFe53SIwtfLoxlSdAyhTpLRBieI2VMFVg2-Tf6YlGvj_3ZEewJ0LbFY3cwMhqYY9lpLNxBTaRfEnT8YSRmvWFcCHLG252vIXopO1SdgFZgxXuP_I-fwAWQMwFfERpxTWM5i9W1Owm71YXEV5LKy_awrPtnUT_oz7ysA0nUfVuDI3lF97CiIAYwxv6fSx49L-RGaNWtW3y7HkGFCMGmsd-ZP9rclFV4xPqcD5eEdmqZ0FxWQ2tSKC83OmTJDaE7J-X8vvlGTmuez7htsSbd4m_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcQUDa8Y6px6yVnO67QslkLymXWBxsjVsLRnU7oWKy699jAGVCTEyPskECEUZMCYqqvKoOnbsyTTFxq4Sr_b_8EWHB6zsNQxrBJmRfl3I5GFwKIfZBILgZytFfNK13EGRPGjweOcssmySLlk2rlkDJ0nS7tqrmMmM8-JPJb3ZpTi6zN0k81TwxiTgVxBrzz0iwOtRbAvdvO4p8XFpMIhI5OLpAf9Inj7VUsXnv0r2iGWo1-Vz3cmYL3GwcqRDNwgDB9kk6pJndH2Ka87Yn27wbMGGBc1d0n2kmGJleUjh1itLUoaWU9PSpnG-jQ-ZmcDrDMAXUm2GoSIwKtY_cce2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ویدئویی جدید از حمله هوایی به پل B1 کرج در جنگ رمضان  #اخبار_البرز در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/663449" target="_blank">📅 14:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663448">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe0859499.mp4?token=JrgaTwYQqWnvlD3-ap3z5W0P8d88B89aJdTbwN5Pc73egb1bFS36m-S6uLW0vaXEwp0oWEKB8u6GBd-Pp5jfeey3cBysEiK26KzY7HJbFZWTDpEtFnjjqn6LV2lVgUsFv3neY2sG0F-INx55XFA6fkBcmntWnTpzg_yUhKr4mzDk3QWEzBzP6qwo6wEg4HjBX8Hg-QzPP4OlRmYktO8U5Fp9lRIR6se9D3O-ofw5QUTnGjnN7BzYI7D3O6c9ObLmGVChiGbbjt3pU1EBG2Z53aR_9J6CjspJ5mzZXS7jpGFohtbkrGhsFBhs81IAmZQx8h5ZwsnVupjC0M9yg4h_qR2h46nzc9-zyTRJYPRawxp8bLMaHH6g1zvOtA5ibZ6bF5wGQD_ZSG-HkSKWL0JEWPqzgxM6A_yw4DAsux2xo3ThdCNapM8ykO-LUOk-SLJseB_j4dlP5WX6wQ54hSDWz4ETijd4zVjUqv--vuZrQjY50ghDpgjF7tE-pgdBKaPQSIKdhOcmkU_1Lq5IgSGcR5A8gd1alh8g9txgbWfi7nz4ShRiva7QRTOscH_CPhGd0_x4MpleDszGjUiOjrsNX0NEoe4OHo_bXYeuBtJjMack0SC25n0JOX8op411oWgSn0S4t3uQvCJ7vPFvwIBi6PV7PUun9w8apfumTqE_liA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe0859499.mp4?token=JrgaTwYQqWnvlD3-ap3z5W0P8d88B89aJdTbwN5Pc73egb1bFS36m-S6uLW0vaXEwp0oWEKB8u6GBd-Pp5jfeey3cBysEiK26KzY7HJbFZWTDpEtFnjjqn6LV2lVgUsFv3neY2sG0F-INx55XFA6fkBcmntWnTpzg_yUhKr4mzDk3QWEzBzP6qwo6wEg4HjBX8Hg-QzPP4OlRmYktO8U5Fp9lRIR6se9D3O-ofw5QUTnGjnN7BzYI7D3O6c9ObLmGVChiGbbjt3pU1EBG2Z53aR_9J6CjspJ5mzZXS7jpGFohtbkrGhsFBhs81IAmZQx8h5ZwsnVupjC0M9yg4h_qR2h46nzc9-zyTRJYPRawxp8bLMaHH6g1zvOtA5ibZ6bF5wGQD_ZSG-HkSKWL0JEWPqzgxM6A_yw4DAsux2xo3ThdCNapM8ykO-LUOk-SLJseB_j4dlP5WX6wQ54hSDWz4ETijd4zVjUqv--vuZrQjY50ghDpgjF7tE-pgdBKaPQSIKdhOcmkU_1Lq5IgSGcR5A8gd1alh8g9txgbWfi7nz4ShRiva7QRTOscH_CPhGd0_x4MpleDszGjUiOjrsNX0NEoe4OHo_bXYeuBtJjMack0SC25n0JOX8op411oWgSn0S4t3uQvCJ7vPFvwIBi6PV7PUun9w8apfumTqE_liA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تیزر قسمت بیست‌ودوم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای اکبر بابامرادی که به دلیل آسیب دیدن و فرو رفتن ترکش به چشم در جبهه روح از بدن جدا شده و با صعود به آسمان هفتم با همراهی دو تن از ملائک درک زیبایی از عالم دیگری را تجربه می‌کند، نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: اکبر بابامرادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/663448" target="_blank">📅 14:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663447">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔹
درب فردو و نطنز چه زمانی برای بازرسان آژانس باز می شود؟
🔹
بر اساس شنیده‌ها از متن تفاهم‌نامه مذاکرات هسته‌ای، تا پیش از توافق نهایی، ایران تغییری در برنامه هسته‌ای خود ایجاد نمی‌کند و دسترسی بازرسان آژانس به تأسیساتی مانند فردو، نطنز و اصفهان برقرار نخواهد شد. به گفته منابع مطلع، بررسی نقش آژانس در این مراکز به مرحله اجرای توافق جامع و تحقق شروط تعیین‌شده موکول شده است. موضع قاطع تهران، ادامه روند فعلی و رد هرگونه زیاده‌خواهی آژانس پیش از توافق نهایی است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/663447" target="_blank">📅 14:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663443">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d333ab5ac6.mp4?token=L6WQdbSfmyQKtFyEB4v8ILbbxvcBKWZNm3sQpG2xApAWAlFiAWJzGqWohSaRRsvpEiQ-BfzabnpSynQ-3IASPSgXBEJJnYHKGCSixiWS5NN4m6lk6fOMCny9Z6Vh7Xt8GMdeCmGbEqujlf_Ee6VsdxhQYH4H73JyhXsL4MRzzeYRVgXTU2OCIBC3gm7_eK0QAdc-LM0Gkh4DFgGhE_CCKENpeuPxUGslEz9Hob6yN6eVy_gNZDiveJsh8nq2acjkf5Yqgb7Sb847tQHIlaZkRgLfpWJy6qiwRgGKRwHPz2Am6phnJHLAEXF3hVN7QPDNLgtFlhhu92JjsoN2mkm-mRA3GdJauIeiDEjhsAJi6honLf_coWMOtjeC-2LSZuuxwI8-a2CJ4xb2gOwg_aEBSzxxf7EHK5bApwP7c-GBvH4qDxaU71k2P3adL8tOmsH69ZFCpiH8kXummQuFfbDqk5HLU4imBEIeS6U0UAopZSOEuKc6gfkNNI4ooLSYkKkCpN9Q4dAvArgRkYqWvfILdm7lnxCUedNPw7dbRsc0U8WpElYIm9oifLYykIUOOaIUXrXHMh3GXiAOvzhCURVUz-yzU3i-7IDm3WIvH0YwM-uoZVmNKaEaqx0TUrmGehEBoHE7a3Xw9ImP66YBYC-9re0sEZ4UGUuXXqlo2ARyf6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d333ab5ac6.mp4?token=L6WQdbSfmyQKtFyEB4v8ILbbxvcBKWZNm3sQpG2xApAWAlFiAWJzGqWohSaRRsvpEiQ-BfzabnpSynQ-3IASPSgXBEJJnYHKGCSixiWS5NN4m6lk6fOMCny9Z6Vh7Xt8GMdeCmGbEqujlf_Ee6VsdxhQYH4H73JyhXsL4MRzzeYRVgXTU2OCIBC3gm7_eK0QAdc-LM0Gkh4DFgGhE_CCKENpeuPxUGslEz9Hob6yN6eVy_gNZDiveJsh8nq2acjkf5Yqgb7Sb847tQHIlaZkRgLfpWJy6qiwRgGKRwHPz2Am6phnJHLAEXF3hVN7QPDNLgtFlhhu92JjsoN2mkm-mRA3GdJauIeiDEjhsAJi6honLf_coWMOtjeC-2LSZuuxwI8-a2CJ4xb2gOwg_aEBSzxxf7EHK5bApwP7c-GBvH4qDxaU71k2P3adL8tOmsH69ZFCpiH8kXummQuFfbDqk5HLU4imBEIeS6U0UAopZSOEuKc6gfkNNI4ooLSYkKkCpN9Q4dAvArgRkYqWvfILdm7lnxCUedNPw7dbRsc0U8WpElYIm9oifLYykIUOOaIUXrXHMh3GXiAOvzhCURVUz-yzU3i-7IDm3WIvH0YwM-uoZVmNKaEaqx0TUrmGehEBoHE7a3Xw9ImP66YBYC-9re0sEZ4UGUuXXqlo2ARyf6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
خلبان اف۱۵ سقوط کرده آمریکایی در کهگیلویه گفته پهپادهای سپاه با آرایشی شبیه عروس دریایی در آسمان و مثل یک میدان مین در حرکت بودن...!
🔹
اکنون شبکه‌های اجتماعی غربی‌ها از این فیلم‌ها پر شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/663443" target="_blank">📅 13:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663440">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔹
زمان مسابقه پرسپولیس - چادرملو تغییر کرد
🔹
با اعلام سازمان لیگ، به دلیل پخش مسابقه تیم ملی والیبال ایران مقابل ژاپن، مسابقه چادرملو و پرسپولیس به جای ساعت ۱۸:۴۴ در ساعت ۲۰:۳۰ در ورزشگاه پاس آغاز می شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/663440" target="_blank">📅 13:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663438">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ2SF5Tej9QTb0UND8KetcIFK7MG5X9vcinvTnD1Z0_XZOSMwts__v9K693MEA24QaBS_RCcAjYwDhp0A5t2AMtEw0P5CGbZVpMy258V2_49GhU1AtZ4a5Fj2Hk85OwoLZZky0UHZPpuFPolYCUxYGvnxSMKZmne78SeE4kf3BDl1JA6AEQGrn9McWvNuzqZaxEsBlUQFhWeFI-51t-0LjX7OInuHzwWekWOIIQ__BH_myWRxgczrULzY_c0ESdG9Hgam4ctRDyVF90SPALAqNn-F0qyfYky0S5vXKSEFFq1JQEBvun_ZxjbaB9UFgCWOLG16y4_Bd0rCT0TylfZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سخنگوی وزارت خارجه: آمریکا نیازمند احسان و خیرات برای حل مشکل گرسنگی است
🔹
طبق گزارش "سازمان جهانی آموزش خدمات گرسنگی" «در ایالات متحده، بیش از ۴۷ میلیون نفر، شامل یک نفر از هر پنج کودک، از دسترسی به غذای کافی برای یک زندگی سالم محروم هستند. از سال ۲۰۲۰ تاکنون، تعداد افرادی که با ناامنی غذایی مواجه‌اند، ۴٫۲ میلیون نفر افزایش یافته است.»
🔹
طبق گزارش سازمان "تغذیه آمریکا" «چهل و هفت میلیون نفر آمریکایی با ناامنی غذایی روبرو هستند — و هر روز با چالش‌ گرسنگی و تبعات بهداشتی و اجتماعی آن دست‌وپنجه نرم می‌کنند.»
🔹
البته خبر خوب این است که مدتی است مقام‌های آمریکایی دیگر نباید چنین آمارهای ناخوشایندی را ببینند چون بعد از ۳۰ سال گزارش‌دهی مستمر سالانه درباره وضعیت ناامنی غذایی و گرسنگی در آمریکا، وزارت کشاورزی آمریکا (USDA) از سپتامبر ۲۰۲۴ بی‌سر و صدا تهیه این گزارش را متوقف کرد. بدین ترتیب اکنون نزدیک به دو سال است که مشکل گرسنگی در آمریکا حل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/663438" target="_blank">📅 13:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663432">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZx8QPlSG7NFRjnsZv9-EjGtsmwgw9pkZswnW7YCA3W2p6EnNBumLCCJwzhP8NDg-zc1snys5EcVr9sZtPSzlFW_RrnF735Jtvcja-QL3VXsxjw37Xmpn9MpJhgXSK-EscvcItoYxYWOhzR8unS1OVPC-hCCBq3HEqH_Mk7NLo25P_E-na40mV4zLNY7jEHG0OGXJgXdku8FVCiLO-WbVLP85vZYsCQnWfK16sdgdVCKvjJXjB9PRHoP1a07kdY4GDOQMCAc1qzXDBeHI8zIIAAORDxysPdlTXWzufSdMd9PsIhaHCrDy9jy7w_HHxxroDcLLFlZxCCXxpWCRFN_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vG6qQ2YuvTq4TjjlHvksIq3Nh3FNHHz8JiXcbfd1KMCju08175HD-iDyZwheMRmrMCQyfvdtzYW9PPa3__NxtZqYNKWIgSdo5KQwpMwiblaUpOEJ4L9P6cLw3FAbqsdKmUgAl4ugm7O6xUFCxQRtY3e2Oc1I_-LcewgBR-dQlaBwRH47-fXTGt1R1ON4LrSaRV9LAQrry4-opVz1PJCR7xuHL6cxq7QzvramMR3_Sf8b0kGjgdlLPSEWSe5x4k4kt2obAJ0gyY6xBy-NUmYj8Ure30ugkDo8RignenbrHsKaXCwuxf1An2C3bvk_DWpShK-8QAh9RIFItEn2thsFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8NydjYmhMIcF5yz3hUj3SoWfKag6VsYOc23NWyKwzA14PkuPKcsC6M0gPxQkubZGqBuhOG2IhESbvRYL7K9O0V2KHu8aBl4gdINadfSleR6hegGyR0Blj0006eshw9yNuPln_czZBc4zawwD5n__8Lfq9ZMHnX6g0-cEUlkiqGLnvqJSyccpNDfkEljKdvhz1AvGvi6ra_6BUS7Kr-lKGsTpBDBXORi1ooeT-WkPs_XZjJigWSnt0NEwhm8Sl7gyxg7T50KgUQdeCAOGM3tikULuifABTCHF40cD8tjf5Hn9ucOE_5XLI9X2jht5AcAzc9pvpETKqxHwCuaO9vwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRWn1ViidzWEz4fie3kUphIyfeiIHcUhXYZOYUm7OV5to2NkrjyOLNSyj3zT4SGALi_zdmQmc7VfLDp4NuKbbq_a9NqhkpWttNm15UdFeSBydGHfg-vYYGCSLtRiFGa6XCbOv-_hRB5d8Epb8ZNTI4uxvxtdAGOpdGjDeDOjbYpYzXrsxKXQMA1Gb3TVVv9vHskumbGr34QivFGI2F9rhX6R8g3GtBooW9SbxaGyFtnfr1ZJgiqsPUo-O8hX64wubHd-ZqJh4gFgdTJ64BQ_IwRjHz2CZuF-lDI5WolmM43xB7EVFnQemF7DeIvuXe9b4fdO7gFO-HL77kURP44_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFfrPaclNxMCA_iFjgxcnMREHeMXFbtnWIkTw7PHpRtx7otjTc7dS72-875cjSFAYWmqLPsFqE_TWXtr16yH0_5KkeCHWhdapDLuPyGTYib1prOb7C1ceF9Ve5GHQz6-scIJGIMUIBmSKmHuk3ooi4U0QvHmunA4F2F3SLKSFXxi82vqK_f3kiGEuZE2kAdgauKnmr44ug5E0w6kolsfFbvDncKo6SyO2NyF5OcyojWUkE6b_41LAGS-xI_7IVCkWsneO-QqY5VipUZZKmmYSHkvXmPG_14OJp-ET0L9RLNRR5jH27G_QxOd7gV2iuDqyOrvVzxTnPZCZPsgCzveGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fla2qWhAJHCSmNYvVtmCYTvhZtTEwY18Y7XzglFwn-AuU8DWgRzxLku-Dg7h1b4xRNbqOaOuSJcqPcLvWwhCOj5L0vG8ARVTgcXg3Ci0zagsTX76s_R_u-FD2Aw55SF9uP3O1xNO4ETqACJa98rUJfKyFcslGA0eoDTNCptPnPL4OqDPmvphaRzdElobP6mIcgtKDooEFgu3ZBi9sFHZmCnx3J6Mstb63NBMTgikCxG8uXP2QLT4RXHunylViF2zjhWI5873FDivgOK7Tr0vanYz6FxIiLJ_Agcd60M2H6oM_R2SWsZ_XIEVonRihMzDSv84WFVKNkaL8PNAJ_8z_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصاویر جدید ماهواره‌ای
WSJ
ابعاد خسارت‌هایی را که ایران به پایگاه پشتیبانی دریایی آمریکا در بحرین وارد کرده، آشکار می‌کند
🔹
در این حملات، ساختمان فرماندهی پایگاه، دست‌کم ۱۲ ساختمان دیگر و همچنین دو پایانه ارتباطات ماهواره‌ای به‌شدت آسیب دیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/663432" target="_blank">📅 13:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663430">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S20hePo2Cq3GEJSfj4aWXFyNXzRpiAOyJsY35eI9qC0vC6O2qkOWfFxOHim_cSBcnc6khzWf2Bofb9seHClxsT9a1fWX0eUN7Da6DsNphwuwttk7fXJaMNWxXgVeENA1negZgD3LWjC4xdv2JJM8tocmMNm8ZvYIP2La8cyxtN55pfXeKaiz65dR2C4tg8v3DU2-zOA-s_4AXSY8a0R4SLP3x7VPnYG58eQ8a5iNWgCyEnuEiYE-nNMcshnJ77NkHJGAigc6EimmVjIqxrmjp00Tx0FMgUW9YFHk7rxVuek3lbU0rlu06Y9wdZuLhcfRpLqz5b7-D_h7lGyhYcCBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هشدار آشنا: جایگاه رهبری را در حد فهم ناقص خود پایین نیاوریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/663430" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663429">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMcW10zBhoZ7dbrwSkyueiWTjEvAhU9tKF3Ikagrwo_jBc9TAgbiYOX9RnCcDyUOBdAwsR3dG6F--IhZKmLa2k9d1_dizuBsocQ9yA26xCu12P8wkM4ZqCp8iNgAdE47ckBo2MUMpUPbm3PmoCyaaBAcRCHPU8NmZklWQ15RHJmLwltfbXePZ7S8M4KUndGSU8nNC75QfwRttZks1WIY2enywTN7HUJeMQeTIIUdINFWplyDVbc9sJZM0AFeD7lsirdmDDl5DZLDgIf9M4a6PqjrkVxkEyHLIYp685X0whf0sfyyxQRjjI3Y8dyswHiWtEbCDKacff1hfL8wasn-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چین اولین هتل کاملاً رباتیک جهان را تا سال ۲۰۲۷ افتتاح می‌کند
🔹
شرکت چینی Pudu Robotics اعلام کرد قصد دارد تا سال ۲۰۲۷ نخستین هتل کاملاً رباتیک جهان را در یک جزیره مصنوعی افتتاح کند؛ هتلی که تمامی خدمات از پذیرش، حمل بار و نظافت تا آشپزی، بدون دخالت انسان و توسط ربات‌ها انجام می‌شود. این هتل ۴۴ اتاق لوکس، رستوران و باشگاه خواهد داشت و با مدل هوش مصنوعی PuduFM 1.0 فعالیت می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/663429" target="_blank">📅 13:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68cfec430.mp4?token=Z2o1GRH4XB9gAJKzHHkDv70O5V9_rZIUsQAalcFj7W8CbXNM2U9Zv9LV5auuoxEG_Q1HUQDgCh4hpPYQVjmm7-ZxuHremxVZXK8itwM1zOaw2POj7X6oMhDhKgRkXg3n9NKHJVg-X3qQFPcN2B-Sg4jvjk28MXGcPeHuC3Tf2-KmqK_RA-2b-xDPWzGjXFW6wg1fEhVN0P9hx9JPIT7RxzpZb-7sgDSnbgM_XBQFWraAtyjj4-SQmBlhacZGQdEMBO8SitBoJt17qawtRmkHL4FDEN58pL8NdW8W4aFgSKegjpay48Rk4soQLKTGKJSvzWlDLvdaW_FA6jL5NnBdww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68cfec430.mp4?token=Z2o1GRH4XB9gAJKzHHkDv70O5V9_rZIUsQAalcFj7W8CbXNM2U9Zv9LV5auuoxEG_Q1HUQDgCh4hpPYQVjmm7-ZxuHremxVZXK8itwM1zOaw2POj7X6oMhDhKgRkXg3n9NKHJVg-X3qQFPcN2B-Sg4jvjk28MXGcPeHuC3Tf2-KmqK_RA-2b-xDPWzGjXFW6wg1fEhVN0P9hx9JPIT7RxzpZb-7sgDSnbgM_XBQFWraAtyjj4-SQmBlhacZGQdEMBO8SitBoJt17qawtRmkHL4FDEN58pL8NdW8W4aFgSKegjpay48Rk4soQLKTGKJSvzWlDLvdaW_FA6jL5NnBdww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مراسم عاشورا در لبنان
🔹
این مردم، سه سال است زیر حمله اسراییل قرار دارند، رژیم صهیونیستی خانه و کاشانه آنها را نابود کرده، مردم را آواره کرده، فرزندانشان را کشته تا تسلیم شوند، اما امروز سربلند و با پیامی واضح به دشمنان گفتند: "كِدْ كَيْدَكَ، وَاسْعَ سَعْيَكَ، وَنَاصِبْ جُهْدَكَ، فَوَاللَّهِ لا تَمْحُو ذِكْرَنَا، وَلا تُمِيتُ وَحْيَنَا"
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/663427" target="_blank">📅 13:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔹
آغاز مراسم عزاداری سنتی «ركضة طويريج» در کربلای معلی
🔹
در سالروز شهادت امام حسین (ع)، میلیون‌ها عزادار حسینی در کربلا، مراسم تاریخی و باشکوه «رکضة طویریج» (با پای پیاده و هروله‌کنان) را آغاز کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/663425" target="_blank">📅 13:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxQ9UtvFH5MRcdNaVGn18CEUmpJh6qv5NG-0q9UMr04f17LOw0EMw6mNuefN9OK7lVJ9aLCINRsk4fY34mCM_839EtI_bJrt86Q1RF3kTJf2Z_Ub7XI7XBBjPNwzqdENolp5I2Rulhu-hQ-6BqPvwu4yzvC-BfAeqKLTJKIs6I99arHdimYNJgSkl4nkOT21Pm2VmmmYMg1WPGCTK7_hiisUj-zd-SQQG4JaGimqtgVSuvO-ZarKLH-7q5tX6Icxhb3KyoVF-G3acrRXpLJh2tEaEb3hB2a0jYiXVn8Qb96b7dNgMZTFfSvlPxoLiX0QZQClTiwdP9DfOH3mqFP1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
غریب‌آبادی: عبور ایمن در تنگه هرمز با تصمیم‌سازی خارج از ملاحظات ایران تضمین نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/663424" target="_blank">📅 13:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔹
اکوادور غول‌کشی کرد و به‌عنوان تیم سوم صعود کرد؛ شکست ناباورانه شاگردان ناگلزمن مقابل اکوادور
⬛️
🇩🇪
1️⃣
🏆
2️⃣
🇬🇶
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/663419" target="_blank">📅 12:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda213ddce.mp4?token=hUrXVv5z6kIWMS0in3BF1wo_kVWybsSZVBiQvSHcNvBsRra2dWr0-GzQxxamEd-37iCS6CX7rxPO3KVBNKtzIcepJBJwVwESMPzcNCkr6810TQ_2pEjeQW0KPr3YpjugZRnQYWq4XOdFsJQpyk4IdcseYhJMYWRtvfD1xzOjgf0sWAA99NCDf0t_kmm3_QOj0Dzp3bMSjMQT_9Ln6P4-UK5-LGcDw2Vosse3UF1LfjzdGST0SqC59cOmJRrdM49GmMWfrGkcXZhFkRGMQFmnXoj-ZGA1KiDK0T7efDc_CQ2qILpenVJAuo3tVrQQ7Lix3d_ycIuTvs76ePmj-7AFsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda213ddce.mp4?token=hUrXVv5z6kIWMS0in3BF1wo_kVWybsSZVBiQvSHcNvBsRra2dWr0-GzQxxamEd-37iCS6CX7rxPO3KVBNKtzIcepJBJwVwESMPzcNCkr6810TQ_2pEjeQW0KPr3YpjugZRnQYWq4XOdFsJQpyk4IdcseYhJMYWRtvfD1xzOjgf0sWAA99NCDf0t_kmm3_QOj0Dzp3bMSjMQT_9Ln6P4-UK5-LGcDw2Vosse3UF1LfjzdGST0SqC59cOmJRrdM49GmMWfrGkcXZhFkRGMQFmnXoj-ZGA1KiDK0T7efDc_CQ2qILpenVJAuo3tVrQQ7Lix3d_ycIuTvs76ePmj-7AFsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
روسیه داره باقی مانده زیرساخت‌های اوکراین رو میزنه
🔹
اینجا یک پمپ بنزین با پهپاد شاهد ۱۳۶ هدف قرار گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/663418" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6267db3ddb.mp4?token=pQ1mngnqgsvMAoVlfAtq3EFobhwmOeX1aVCIsWBDzWG2S1YzdYY_CatO-w7sXXek__wKWuXhAiOpLHAlgcg2Re9ROp4TxbSdQK59IPFVSeJyBQnHB2HQOLuGPXweuNwEkPX4YRJ1wh35s7yhVOqc_2WepQ34S1C6D-UQbsfLnbuao_dD28Z7Sl3rVCEbH8wBDtLsthxffyejKkHJql_riGg9WlkGgVGzhRp9hCI7JH60LGtFhBQ3XqH-jyIY5wfjgTkdJi6hHSBJN21GFXj_HAQvIm0qIwwcHqKtAvXC9-3J4FsVUDyb0MSkx2TSgxvzYBxA6DWZMEOJGL4HwCwgTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6267db3ddb.mp4?token=pQ1mngnqgsvMAoVlfAtq3EFobhwmOeX1aVCIsWBDzWG2S1YzdYY_CatO-w7sXXek__wKWuXhAiOpLHAlgcg2Re9ROp4TxbSdQK59IPFVSeJyBQnHB2HQOLuGPXweuNwEkPX4YRJ1wh35s7yhVOqc_2WepQ34S1C6D-UQbsfLnbuao_dD28Z7Sl3rVCEbH8wBDtLsthxffyejKkHJql_riGg9WlkGgVGzhRp9hCI7JH60LGtFhBQ3XqH-jyIY5wfjgTkdJi6hHSBJN21GFXj_HAQvIm0qIwwcHqKtAvXC9-3J4FsVUDyb0MSkx2TSgxvzYBxA6DWZMEOJGL4HwCwgTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پیش‌دستانه‌ای که شکوه را به ایران برگرداند...
ماجرای کامل این دستآورد بزرگ نظامی
👇🏻
https://youtu.be/AXNLsCbNe7w?si=DA0CyGP385V7uitO</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/663417" target="_blank">📅 12:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663416">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔹
وقتی نوه ترامپ راهنمای تور کاخ سفید می‌شود!
🔹
در ویدئویی تازه که در فضای مجازی منتشر شده، کای ترامپ، نوه دونالد ترامپ، رئیس‌جمهور آمریکا، مخاطبان را به گوشه‌هایی از کاخ سفید برده که کمتر جلوی دوربین رسمی قرار می‌گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/663416" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFRORvIgsfoV4itmd_mnZoIAArkCNQppxpWXbeR0Nwdj9fVPZvX2PrEf00zM90k8CZTvkC35SlMKW0T8_B_szSPI2IAAR9ZhDXSiweUBWdGZj220dAUWzoAKDmQjgOzKg85JYdKoY1tZJv6aSxRu9irR1NIwhm4lr1IlTPz8rY_gOFNuM8CEf2xIGaTmf_UaeaLG5ahELAOYnKpkMpp6Wofq8tlGTXO-E9Lqc8x3zDsQorreSOA3F3G4YYwevZV_oZSblErXOjVumwQzg92Ja0zmX1DpgLEYgr7i1rySO6GIJRBfu_Ab9ZEpPThyMpJeFJgdkihEn7FP86Al6_A4zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۲٪ اسرائیلی‌ها ایران را پیروز جنگ می‌دانند
🔹
طبق نظرسنجی دانشگاه اورشلیم ۹۲ درصد اسرائیلی‌ها معتقدند ایران برنده جنگ است.
🔹
۸۷.۸ درصد معتقدند اسرائیل به اهداف اصلی خود در این عملیات نرسیده است و ۸۲.۹ درصد می‌گویند این جنگ امنیت بلندمدت اسرائیل را تضعیف کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/663415" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d17ce1a9.mp4?token=JQMnnBOYNbXM6hem6mYfO343Ia0LSx5i6LUL732lkhfLPgC0H82CZl96zVN2kOLoX5bqEov8DRH5-zTl_3lb8Ni3r_L_qJqgdJdHcw5_347s4KjoRql26QWpg36ztSvYmyyAzIlWB1iy0jr5nNkeDfY_VPu5QXXWhROc790Z8egIorvW2pnHN3c-uXnpGYkH1Sy4eZ_jTEEA7PYkNqHKf6ZWuurNUZSPs3Mk_2nqKdGdWwXzdG7gFBosU5nuba4CaUeB-oYuCzIyZ1LLMs7Aftu5osHgjNDvVpzM_PUrbXSWPX1CsFCVMpCNFD9qT_jBz8tiSIcxDImTg4toVq__7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d17ce1a9.mp4?token=JQMnnBOYNbXM6hem6mYfO343Ia0LSx5i6LUL732lkhfLPgC0H82CZl96zVN2kOLoX5bqEov8DRH5-zTl_3lb8Ni3r_L_qJqgdJdHcw5_347s4KjoRql26QWpg36ztSvYmyyAzIlWB1iy0jr5nNkeDfY_VPu5QXXWhROc790Z8egIorvW2pnHN3c-uXnpGYkH1Sy4eZ_jTEEA7PYkNqHKf6ZWuurNUZSPs3Mk_2nqKdGdWwXzdG7gFBosU5nuba4CaUeB-oYuCzIyZ1LLMs7Aftu5osHgjNDvVpzM_PUrbXSWPX1CsFCVMpCNFD9qT_jBz8tiSIcxDImTg4toVq__7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توزیع نذورات در میان خودروها در عزاداری شب عاشورا(دیشب) در شهر دیترویت ایالت میشیگان آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/663414" target="_blank">📅 12:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663413">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f98e55a0.mp4?token=eqGNlOSXQaui5utL6fyIFMYU0An-lZQa1m1sJ_yaPozbbEDG90wF5-9a5Ag-n_3A_XwqHQndZeim4ac-CZ-sDLPlsqwHZIOb7JsxbwBWt9ny1pjnU9U6Kwr8K0w19JDG1a66sIspiXNoF2mkrOl2Wk__GrU7IkIDnOycfo_PCTi212YM1XM9nHs7KNtuAAl3yc_Ho0dy7EDchOGAAmqEjP1duQC1YG-3CWAXWADyr5Kd6sffBQvcb8_6oofQkn8YAPBfMw_yYgANFwDu0ApxJmzzP-0QCWGnZJPj34YSYHO573Gm0JPstmFfrYsdpItKvlSUz77ycYfGpgqvVZV1ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f98e55a0.mp4?token=eqGNlOSXQaui5utL6fyIFMYU0An-lZQa1m1sJ_yaPozbbEDG90wF5-9a5Ag-n_3A_XwqHQndZeim4ac-CZ-sDLPlsqwHZIOb7JsxbwBWt9ny1pjnU9U6Kwr8K0w19JDG1a66sIspiXNoF2mkrOl2Wk__GrU7IkIDnOycfo_PCTi212YM1XM9nHs7KNtuAAl3yc_Ho0dy7EDchOGAAmqEjP1duQC1YG-3CWAXWADyr5Kd6sffBQvcb8_6oofQkn8YAPBfMw_yYgANFwDu0ApxJmzzP-0QCWGnZJPj34YSYHO573Gm0JPstmFfrYsdpItKvlSUz77ycYfGpgqvVZV1ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
لاابالی یعنی چی؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/663413" target="_blank">📅 12:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663411">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
طبس گرم‌ترین نقطهٔ جهان شد
🔹
براساس داده‌های منتشرشده از سامانه Relay Weather، ایستگاه هواشناسی طبس با ثبت دمای ۴۶.۸ درجه سانتی‌گراد در ۲۴ ساعت اخیر، در صدر فهرست گرم‌ترین نقاط جهان قرار گرفت.
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/663411" target="_blank">📅 12:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663410">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uImsY8fTugR1sLoBKs1jBWjolnXYpVsfFo6ayZaDFlhbsHRwdw9gxDh_lfA0pAoRABhCvVBWQAWUOaLiSlU5FOdnoQWrQiyrKKXM0mTbIdTn9q_ALVtPpYB4tUm2hFa5hT0quAyt8JDS151biUe2vYqtEAfUqPXR8bvUwqvC7aekURR-h30GW0C4ZMOvLV6YS7uwiZwcJxDw-W0l9Y1q0fiXgBPSmVWo6JPYknAOsa1pyH1YmRgjjrOJvt6bAacJ5W2L5KzPr4LvDUCJ9dE8pkTAyltC8xa-lyy9YLS26h-bclStwJRjw25p8sqaHUKTNa8wznVH8iWovHZWhFbB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اقداماتی که بسیاری تصور می‌کنند به کاهش آکنه (جوش) کمک می‌کنند، اما در واقع باعث تشدید آن می‌شوند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/663410" target="_blank">📅 12:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
کارشناس نظامی لبنانی: ایران باید استراتژی خود را در دوران پساجنگ بازتعریف کند
روی، فعال رسانه و کارشناس نظامی لبنانی در
#گفتگو
با خبرفوری:
🔹
ایران در دوران پساجنگ با مرحله‌ای پیچیده روبه‌روست؛ جایی که نبرد اصلی از میدان نظامی به جنگ روایت‌ها و رقابت ژئوپلیتیکی منتقل شده است. هم‌زمان تلاش‌هایی برای بازترسیم تصویر ایران در سطح جهانی و تغییر موازنه مسیرهای راهبردی منطقه در جریان است، موضوعی که نقش آینده تهران را در نظم جدید منطقه‌ای تحت تأثیر قرار می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/663408" target="_blank">📅 12:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663407">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔹
بازداشت یک ایرانی در مونته‌نگرو با درخواست اف‌بی‌آی
🔹
پلیس مونته‌نگرو به درخواست اف‌بی‌آی، یک تبعه ایرانی را به اتهام حملات هکری گسترده علیه دانشگاه‌های آمریکا و آنچه «خدمت به سپاه» خوانده شده، بازداشت کرد.
🔹
بنا بر ادعای اداره پلیس مونته‌نگر، این فرد از سال ۲۰۱۳ تاکنون حملات هکری گسترده‌ای را علیه بیش از ۱۵۰ دانشگاه در ایالات متحده انجام داده و خسارتی بالغ بر ۳.۴ میلیارد دلار به بار آورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/663407" target="_blank">📅 11:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b677f8d906.mp4?token=lb-mnabzCuwtjvWmV2lE-LULyTuam7lAXyoPWqeGqeO3azv0RzVFOk0ZuekPBujdLkeORYg1in9m8C_P6TatmIrWIJ1CT_7GNPJLyouBHAa293eNZpkKMogkZZjSaIoxBBl2Z4dymVNU-WLt_YsEUady2k1S-hbxIo0lKnB5G7o9XslSf0LC_9TN3VVKRDbDdOY_TryxhQsUyvOP2KYUA0gvDqVlPpb7BWnPAYxre4tUvrf1m6DNUpOKhgHzT25MN5qDJ5gMW6wGB8rxW79yrmnG3LNlzVgg4UaMRXYT5dtXxnIuRt8MP0s5hnN8oU4M2ruHZ8Gu_q2Yh8tjf0owxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b677f8d906.mp4?token=lb-mnabzCuwtjvWmV2lE-LULyTuam7lAXyoPWqeGqeO3azv0RzVFOk0ZuekPBujdLkeORYg1in9m8C_P6TatmIrWIJ1CT_7GNPJLyouBHAa293eNZpkKMogkZZjSaIoxBBl2Z4dymVNU-WLt_YsEUady2k1S-hbxIo0lKnB5G7o9XslSf0LC_9TN3VVKRDbDdOY_TryxhQsUyvOP2KYUA0gvDqVlPpb7BWnPAYxre4tUvrf1m6DNUpOKhgHzT25MN5qDJ5gMW6wGB8rxW79yrmnG3LNlzVgg4UaMRXYT5dtXxnIuRt8MP0s5hnN8oU4M2ruHZ8Gu_q2Yh8tjf0owxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قاسمیان: نباید فعلا مذاکره کرد؛ باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/663406" target="_blank">📅 11:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f3991ef0.mp4?token=vssQKrbwGgkJsQc4PsXBPUijoVP35Np6cQFCORZbbqx72hgO_x5Yb5xI2pRbeTgTaYxhhHrdjwCAcQc0kiYcan-SoEsZa0tTzGuDYPhQO1SsDbcZAsfOdWuncrYlZ_Lus1ZtzWgB5Z9nsRQajj384UUAZR3gCfG5TA4bt2Vz4aej2HDZVojAAASZZeDFBmfauU-L63u7WoiHZYTsiQaqHPfzmlu6XlAZfSMC23yhp3vbq5Xa1zE9VqfCCQbDr2Iv56uOse3nVXGfSSyeK_mdTGgNrEVSbTUgpxGO7QHe18gU7k84LfMFvmOzOQPskzfAQ7v_AONXesCpnOW8vO0vkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f3991ef0.mp4?token=vssQKrbwGgkJsQc4PsXBPUijoVP35Np6cQFCORZbbqx72hgO_x5Yb5xI2pRbeTgTaYxhhHrdjwCAcQc0kiYcan-SoEsZa0tTzGuDYPhQO1SsDbcZAsfOdWuncrYlZ_Lus1ZtzWgB5Z9nsRQajj384UUAZR3gCfG5TA4bt2Vz4aej2HDZVojAAASZZeDFBmfauU-L63u7WoiHZYTsiQaqHPfzmlu6XlAZfSMC23yhp3vbq5Xa1zE9VqfCCQbDr2Iv56uOse3nVXGfSSyeK_mdTGgNrEVSbTUgpxGO7QHe18gU7k84LfMFvmOzOQPskzfAQ7v_AONXesCpnOW8vO0vkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
یاسر جبرائیلی: اگر بناست با آمریکا ببندیم؛ ظریف را ببریم
🔹
یک بچه و بساز بفروش و پاساژدار را به مذاکرات فرستاده‌ایم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/663404" target="_blank">📅 11:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663403">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtn8ortyWmi7V8qFb26xo2YuC6StLVNw1_rPsXcVE2bWFYlBMSWfdqUHnj3L8r1P_as181Je3MIZi9DPC-Enz2hxpa2QOYnD56hCmX_VaQ39VKwztoFJF4Id9vEcOg3Yqyn7CJgwXFy0IR4nsX_SP8CCxOa6Y3HG_pND1l9z79fqNVwFHuSRRsFStMZD0nGmJF1XoTc_I3fhw91yvSh_ajrI6Mu0RGp33jb6syjj18L0ps7tDRZxiEuoslQWAQQC1AKqgm251Xuk_-Xo-1mUAY3PfhlIVzHbQISKYZuSrKVt9QiNFGrB5o_KJKN1sw92QcrbpvoZYytgFbL75JWyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هفت دستگاه موسیقی ایرانی به زبان ساده...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/663403" target="_blank">📅 11:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663402">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔹
آغاز پروازهای فرودگاه کیش پس از ۴ ماه وقفه
🔹
پروازهای فرودگاه کیش پس از چهار ماه وقفه با ورود نخستین گروه از مسافران و گردشگران در سال ۱۴۰۵ از مسیر هوایی به این جزیره آغاز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/663402" target="_blank">📅 11:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663399">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igstEMSkxB8yvzEgLr2DhTvW5IQuZra--9Apn4skd63o5jwT1q9bfl3g06DHCIIBOiM5Q79eJE2VyIh0Bdz-IPzwnx2vxYgxFI3ODVC-dhezrYYN47wOWCo90k2pPVyfTma5-18MCtYsAq2_7BrBcF5KvPiWcaDADPDu4tC72TBqNkyXiMbsc2TQwLIGuvxFrSN__z1fUiFBFlHMxshbzByyg21dlpRCJFC-l99qHo4LeZl3MTYxZNmtCGl57rvolKMmwhW1E2oyOcOxEACJlCt388ptyoiOV2OpQ-GSP9uFX17Cnr8NI6d_CCTmQAnGZuh4Z-YrgsC3V2wE9sCETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7flK3GgjNYkL2mpNb0fvqzqDILTaobsK-k9t2K7GYLsymkr-yvjdd24Ia9OU03N9bOaSftvQzT4sWFQmb6lLJgYAdsjoBO8eH1PpV9gRdHj-pSWBzrtx-srZbOMaqakrS7X-tkmL7PJDnFdCKVhduspUqTCecG6n3ucqyN-lt-XFlGM3MNh5OfYs3tYoECjgyNrZ9CldVRVjm8DJcXuibODHpZsqEcVj8MoQwC4jVbEfTCISKTlp-EKgkKQgpjlV7z36MLdepYU5DhCrIYu9vHYiOTX7a33TDuwQVyL3zx9XAzM-ATLDYopTpGO3hOEVtvnB0_ed_MZoJVk7TL_vQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
بیانیه وزارت خارجه درباره بیانیه مداخله‌جویانه وزرای خارجه آمریکا و شورای همکاری خلیج فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/663399" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663398">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L088yLGZ7lWfTKUaNkWP_n6wiA9NfnwA4bqnshUIxqjgOMZoUzthlIqL_q-GBdSuvLibTTf-OH8BMtbYvdV6fgUE_S_dEpu9FuOnPuCAyo8e63b8rtaoMy4ecyGBo9Lihp4TDxSwVNoo4CHHEHAUNOcKlQB13XUWRuTu1fVEFYBoE2g7h-dGWlT08vehWg9_KoOH3MtYml3XrKWUUtMHXfO-cH-Io8f-TUyC6kkyo6xCHNb7cvhSdCejC1LLHE53jbtxviZmW40a1xQdL1PYP817E3TEw9Gz0DsraPrAA5ZxrGODCX6bvtXof5kn79Etj03Nn-RPzOTuUCbUnZ9TgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه مسابقات روز شانزدهم دور گروهی
جام جهانی ۲٠۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/663398" target="_blank">📅 11:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663394">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
دبیرکل حزب‌الله: در کنار ایران خواهیم بود
‏
شیخ نعیم قاسم
:
🔹
ایران با ایستادگی خود موفق شد به تفاهم‌نامه‌ای دست یابد که به معنای اعلام رسمی‌ شکست آمریکا و اسرائیل است.
🔹
امسال، شاهد باشکوه‌ترین مراسم عاشورایی و حضور گسترده مردم با وجود آوارگی، درد، فقدان و مشکلات بودیم.
🔹
امانت شهدا، جانبازان و اسرا بر دوش ماست و از آنچه فدا کردند، محافظت خواهیم کرد.
🔹
اسرائیل چاره‌ای جز عقب‌نشینی کامل از لبنان و توقف تجاوزات زمینی، دریایی و هوایی ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/663394" target="_blank">📅 11:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663393">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg8otOpjdMLg5f59qSiso8tVdgh_8WOk8igYiUpU-vesW-8defu-mBLKbcNFDupuNd5b6nm0vYH8TxIGAdsp6h_pRc3mQ6nBg2P8pqxpCw2RoM5hx8ONOPzGhSaX-19MWrGTrWUc0BzWr_vWd5HOJ0fwgZuWBglFf5RaIbbynj-KrZk4G_68ST4X3jDeBj3kbQT4AhcD6TT0R9XAmaYPxHqkWHEYDCqqcHSyASdzNaHH5bW3SugpCiu1MrU-CHaByYIpnnMafmV63uBXOHJZ9uBXXNXSEUU5Ye1COaYDFgVAKE7jtARac-hnVi5GFHEBardRxShYLEe9mNiKKoJwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دانشمندان ردپای بی‌خوابی را در دهان پیدا کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/663393" target="_blank">📅 11:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/5e05107ccc.mp4?token=bHh99Pu3m3bB4KWzR8J8bhkwoJuvEdkAe3oJYUR3Q33T7UQ8I21p_6Ku9P36HRFS_U1B0UOlklA3SKwn7CRcEEcKQAKgp8D_0Esn6Vkd9oN5X0BAhaO19X2wtj6Qx233h-koaBU0wtGdruZopNwWISUFN9-W3s5uElzNQv_Mx6OO_p5zArwPANauIDYH_XHGd18ysjE-Udxps5qM_HtggATqLmfTgC9hkaxfbUYe_4gcdlk1PnSNMZkTbIitkBFu6V-ROqqs0ORsH12nlUQ5NjGnjYUxjXXMdt-_qQybj4tRW2jKBxmJEVxpm-aZ23ai4MmHv2MRmhInz0SJ1OfLbA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/5e05107ccc.mp4?token=bHh99Pu3m3bB4KWzR8J8bhkwoJuvEdkAe3oJYUR3Q33T7UQ8I21p_6Ku9P36HRFS_U1B0UOlklA3SKwn7CRcEEcKQAKgp8D_0Esn6Vkd9oN5X0BAhaO19X2wtj6Qx233h-koaBU0wtGdruZopNwWISUFN9-W3s5uElzNQv_Mx6OO_p5zArwPANauIDYH_XHGd18ysjE-Udxps5qM_HtggATqLmfTgC9hkaxfbUYe_4gcdlk1PnSNMZkTbIitkBFu6V-ROqqs0ORsH12nlUQ5NjGnjYUxjXXMdt-_qQybj4tRW2jKBxmJEVxpm-aZ23ai4MmHv2MRmhInz0SJ1OfLbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداران در روز عاشورا در استانبول ترکیه، یاد و خاطره دانش‌آموزان شهید مدرسهٔ میناب را گرامی داشتند
اخبار به زبان ترکی را در کانال زیر دنبال کنید
👇
@AkhbareFori_TR</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/663390" target="_blank">📅 10:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663387">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMVAbYB6wYnJ5m_4o_RJ5NbXDaZKQzIxE22YbW4EaAqD9sey8DBO4GK0q0MEaSOUHOLP7U68fxay7b3byWbMNNtLFs2yvN542UAz5-x7me5OnaBHYLSfGdpX7qy5CceGQLDmOKK-VRr08sszou-nXqSNOZ8pBeYtrokOW5_VeEnE7AQbjjWOAeD87waD7xylqIBQrVpqrV43QInTnh2VKih3rTv_3hqi0riY31pDqBesZHHUc9wLZm58sd7eY8eVmB9uQncSD_CMxJFgazHmPiieTU9OfMPyqM0Ekh-yhdYXpVQxtMAqPiycU6b_V-0Kd328R1ChaAbdSANdabfVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور شهردار نیویورک در مراسم عاشورا
🔹
شهردار مسلمان نیویورک با انتشار عکسی از خود در مراسم عزاداری امام‌ حسین (ع)، تصریح کرد، عدالت امام حسین(ع) الگوی مبارزه با ظلم است و این ارزش‌ها را در ساختن شهری عادلانه‌تر دنبال می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/663387" target="_blank">📅 10:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663386">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70106d33a9.mp4?token=MVzQ8JVBalXSjzy2hLRp7i-9tEKEupQq45FqJw0T4k7YxkKYOHZHVtWKZKOKUVS6y2hBqsghVKeBjI7EYhuB_RXBzJjGygB3bBR01mKHflC56KA2xLnqd_ZAksEKkf1-BuSiDM7L4csPxaOHvy12C2nUJSioqLfWaDQJ0Y8VUxdkaISFa9aGKcRWv1l1y8qvMrBrnCxGG_dxw-STfp0-b9TE3feaaUgbZcy1XXSrJlNfEuA0BWgMZluzg5JwrMC_HByUul9GJYBuWZcZGANXEAyq7MehWhIPhxjs16TlHQAkIkN1_gnk8RQ1DgsGBl9K7k63ttCRIZx_vE3rOQs6gRkowIdhiqlpZcnvduyXJi__lvFQHgsdyHggJ92sMNxTNrjSMrU70KYGD7UfqcqKtrPQDSZ1TKsCeDzTaASrrOr42ZfebXUaNgMCa18cseO4fjS1Skvqs9ojjxOhhqkW6OZB2IbNauLv4aXUQt7B3Hj6q36pRhTiweDyUTqMnNzPZpzU184buWpR4_PBqCjFxDl_t_BzjbCAFDNqFq9fZJTZArxKIsr0ggBaPv2xK1pvFL4P6uHny3_iZ1RK7xPXZkUBHlx32kQrqPIo4FmOA6_EWCZEgnpKgenbvN0Vk7igEbDQXx9LSfi13459CpArs6ggTLmip7e8ed1oYugQ5jI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70106d33a9.mp4?token=MVzQ8JVBalXSjzy2hLRp7i-9tEKEupQq45FqJw0T4k7YxkKYOHZHVtWKZKOKUVS6y2hBqsghVKeBjI7EYhuB_RXBzJjGygB3bBR01mKHflC56KA2xLnqd_ZAksEKkf1-BuSiDM7L4csPxaOHvy12C2nUJSioqLfWaDQJ0Y8VUxdkaISFa9aGKcRWv1l1y8qvMrBrnCxGG_dxw-STfp0-b9TE3feaaUgbZcy1XXSrJlNfEuA0BWgMZluzg5JwrMC_HByUul9GJYBuWZcZGANXEAyq7MehWhIPhxjs16TlHQAkIkN1_gnk8RQ1DgsGBl9K7k63ttCRIZx_vE3rOQs6gRkowIdhiqlpZcnvduyXJi__lvFQHgsdyHggJ92sMNxTNrjSMrU70KYGD7UfqcqKtrPQDSZ1TKsCeDzTaASrrOr42ZfebXUaNgMCa18cseO4fjS1Skvqs9ojjxOhhqkW6OZB2IbNauLv4aXUQt7B3Hj6q36pRhTiweDyUTqMnNzPZpzU184buWpR4_PBqCjFxDl_t_BzjbCAFDNqFq9fZJTZArxKIsr0ggBaPv2xK1pvFL4P6uHny3_iZ1RK7xPXZkUBHlx32kQrqPIo4FmOA6_EWCZEgnpKgenbvN0Vk7igEbDQXx9LSfi13459CpArs6ggTLmip7e8ed1oYugQ5jI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جزئیات حمله زمینی تروریست‌ها به خاک ایران
🔹
خودروها خریداری شده بود، روی آنها دوشیکا نصب شده بود، به آنها قول داده شده بود به محض اینکه جنگ شروع شود بعد از ۷۲ ساعت وارد خاک ایران شوند و چهار استان ایران را تصرف کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/663386" target="_blank">📅 10:35 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
