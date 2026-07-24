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
<img src="https://cdn5.telesco.pe/file/oCRfMHctDv52afti7MeH-h-_cA5m1j7NwspSUXMNMLQHQNSGkUCnqtozIL96feFaNMHLkUjV3vtRkwoiG_8aVaO3nWjHSxeGYPQEfjXaNu6wyK5FgncfrifKt_lWrIAeKyJufjuGv13meGpcxED2491AgyrReStQjt9OZuP1CwJN7XKEUSHe9HTaKnv-zMzkf07atj89DgXUoOn627D7vDAle6Jme-wGCe2XOxi2Iq2rXY8EInYSyOan2lZ54Ex9XfC7Wy8EQMBv9zfNdO28hpNz4wxk9azZa_59zuiCFud_zkzEWDt0oxQgGe9Npxj6PSt73zQ7WYzDMH_2wBGAzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 535K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 13:38:17</div>
<hr>

<div class="tg-post" id="msg-101763">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo7dPkxJHJExPnczQqFzZDSBXrlNZfvtHOB468fihtHcDVVgzb3lGDiEUaVZnq6LNPn8btUabfNCtJLc1zV5kbXpDpblqs0tr7tCUu9BxEGxuH3sar0gCET1s4rQCoVtrtvs_5pYrxnCWZL9xbMghTgk082eimqQzqb6lsnaEPC1w74PkkCeQVeLF7p4z9z_S4BHO0QBO318M9v3FR4dTOAvAzEwa1QWzgBxyYIP1975xV2RjTYdZxkCOaYc5EC2lBV-YI2jhcu1ZgmENmoS8dikFqD2IFbp-bVUFg2zy2P4SaofvbgCL6W8vt4c_JWdmhfKK9Z6V7wLpkHGAodQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/101763" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101762">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632f699042.mp4?token=B5PtDtVGmiaX4EzxzWXSqU9ekpidDAy1dwLO-odKdQu3QYzRBUXn2mtD4hX33hfGQ3yLm9pHR3tfjefIiW3QKtE6eK_gqIu6rNzC0O-leIDQ91N4O__b4GQMIavaTzdM0tn1oH8pXHKdKLA59xsx4QXCri06wv6PxZPDK9WGK4NlF1sCgxqIx8QPSHmzU90_Jo9EUBoOmmj6sBXbxXF6UQ9L1sfkvNNOrzR4nX2Fs7DC0acmZtEy50uxSkdDxPDMusNdZtrGHYwFLzg0m91_qjr2f0V9DoRdhRtnBLmD-gDaUpISD5n1-6t23MIqUh7ip53KTH69hB0-aBYED128Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632f699042.mp4?token=B5PtDtVGmiaX4EzxzWXSqU9ekpidDAy1dwLO-odKdQu3QYzRBUXn2mtD4hX33hfGQ3yLm9pHR3tfjefIiW3QKtE6eK_gqIu6rNzC0O-leIDQ91N4O__b4GQMIavaTzdM0tn1oH8pXHKdKLA59xsx4QXCri06wv6PxZPDK9WGK4NlF1sCgxqIx8QPSHmzU90_Jo9EUBoOmmj6sBXbxXF6UQ9L1sfkvNNOrzR4nX2Fs7DC0acmZtEy50uxSkdDxPDMusNdZtrGHYwFLzg0m91_qjr2f0V9DoRdhRtnBLmD-gDaUpISD5n1-6t23MIqUh7ip53KTH69hB0-aBYED128Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: ارزیابیت از عملکرد مسی در جام‌جهانی؟⁣
🎙
لوئیس سوارر: با سنی که اون داره، میتونست بشینه توی خونه، اما با انگیزه تمام رفت تا دومین جام‌جهانی رو برای کشورش کسب کنه و تیم ملیش رو هم تا بالاترین سطح بالا آورد اما نشد. فکر نکنم کسی گله و انتقادی ازش داشته باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/101762" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=EMPcfzSSFpOIX3BRp5D1Iuh2TfuFHS6Fhh1-p-oU2gxPvetolk66kQVydo57KxbKJYYCHV7ixJf2HuLkXcchm8J2ejcVkGDgDgXoQ_RCI6g34MaLNaVWqOpcLeFqsztVCUXIbhph38-pZ5wp7L3-g6Gxl7m3aHXBP0xSEJChR0BKPHp2IcvMq-vY_t4IhI2gJjJbWVxsAcJk4GMlnuqM4qyiLNZ2GcsTxkrLVOcszeWFhoR3mxuhh_BHRW_eYzeZxaDqgQ3xHSDAEQgngqVWhMPSjFXbw3u457shrVzdWrwXJgdT_QJAyHaBaJE4G0eN3w_Dlk3V2vI7eMFnyR70fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=EMPcfzSSFpOIX3BRp5D1Iuh2TfuFHS6Fhh1-p-oU2gxPvetolk66kQVydo57KxbKJYYCHV7ixJf2HuLkXcchm8J2ejcVkGDgDgXoQ_RCI6g34MaLNaVWqOpcLeFqsztVCUXIbhph38-pZ5wp7L3-g6Gxl7m3aHXBP0xSEJChR0BKPHp2IcvMq-vY_t4IhI2gJjJbWVxsAcJk4GMlnuqM4qyiLNZ2GcsTxkrLVOcszeWFhoR3mxuhh_BHRW_eYzeZxaDqgQ3xHSDAEQgngqVWhMPSjFXbw3u457shrVzdWrwXJgdT_QJAyHaBaJE4G0eN3w_Dlk3V2vI7eMFnyR70fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
هوگو لوریس درباره برنامه فرانسه برای مهار مسی: "یه دستور ویژه از طرف دشان به انگولو کانته داده شده بود. کانته همیشه باید سایه‌به‌سایه و تو شعاع حرکتیِ لئو مسی میموند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/101761" target="_blank">📅 13:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=H6ZZUWMFhIIN3VlPquU0RVs-rz-RyUBjOGaJV-S58ISBLiW5Sc-6n7qtFKAIW_0A6f_WLVxadqSIVaoxoOY6a2ewqiOJSkRiSYwyvMB05o2J68DTcR4-Y6dMkLxGI4-XorCbVYPy8re557QfTcOcOgte-pi_o58eFvqYO0vYoxcpfJvmOhVwHTyP8xp0sG3fvdQnh3ylDNCTOkOzvCwzco_D5rCDJ6lXVz069ibYF-jYYHALkdpdpJ2bA34KO_zI-au3zO2zIILh_z2KUFXukyWN_L6kQ1JT7xxt841-Y5W0hYUk4GCeIU784ArGz5Ky96zwBqSyfcpxAzMpdpUcD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=H6ZZUWMFhIIN3VlPquU0RVs-rz-RyUBjOGaJV-S58ISBLiW5Sc-6n7qtFKAIW_0A6f_WLVxadqSIVaoxoOY6a2ewqiOJSkRiSYwyvMB05o2J68DTcR4-Y6dMkLxGI4-XorCbVYPy8re557QfTcOcOgte-pi_o58eFvqYO0vYoxcpfJvmOhVwHTyP8xp0sG3fvdQnh3ylDNCTOkOzvCwzco_D5rCDJ6lXVz069ibYF-jYYHALkdpdpJ2bA34KO_zI-au3zO2zIILh_z2KUFXukyWN_L6kQ1JT7xxt841-Y5W0hYUk4GCeIU784ArGz5Ky96zwBqSyfcpxAzMpdpUcD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وضعیت استادیوم فینال جام‌جهانی که درحال کندن چمن و بازسازی برای مسابقات فوتبال آمریکایی هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/101760" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHavaanr95a53tSubLZaaEMUmhbHP_Lkuyf-KL4bOIbi0CNRlBcTsxoYDqqyJ4vbQQnV9juRKIX9vwxA4YlMF31wpzLaaEdw3Q0zB4q0okpWFzfddeGI4gwvFVYNEBf6hdQtev6dFf16fIuxzceKjXqkPmY98ORqfjJ7u3vtTdF23sQf7xnzaKVclGZILTujmVrT0SKYs-LcR4D3YpV1BVxCH3471ubIKAK7sfRN0R7M_vMVzTp98O0mpP1O2ttAZnA_Jn-mgBVCo2lExUFqQr5ErLWN9jo3DwfcI2oOVSXR3X6o7YJ8dWocUAlE_LvX7Fz3Oyi0LcsWOI6aJFf4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون فوتبال آلمان از انتصاب یورگن کلوپ به عنوان سرمربی تیم ملی با قراردادی تا سال 2030 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/101759" target="_blank">📅 12:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMg_vVJY5hwsUHX2GQ5ThU_IOiB45O6h3WLg_CM8StWZsNGzT8MoQniCD8kKrFouOi2v1fU3BpfcCGxbZnFFs_TRzfn2NWEunMz8kW_CCstIl-GMPQBil2InKMJALXJmrnt4lB-i1lMWWFvPOsZGgTy5O0Spp77JGTx6_qSFyALfqN7APmWvrM8a76u7ngyvIjfezc8PS9DQOOjbIexknCu7YyNAUDnwAIa-cA6DETih5rXbXRXG8qAa7RMqmkQd6zxYeyAD0uKOVES4yPBnLusHRjAmmvQJ9nVcgeDkTZgFwO6nUAPZrCPswhC72voPmdHKdgMLtIck6wqgd6xXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/101758" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513714e20.mp4?token=Abzt3iJ-NGrTj_rDnye3RKOTVT2Ym5Kvjh8bvYVS2eJeOA5wgEpS3aOG2H7Jof76EdclXaSp8a-HMfUYbX7wJhBG3ZA1eDztYwq5hNCpi6YNCBl_D3-KO8cpECVbOzjTHtAC496uajHn6L2EB_uCDOTKM_mQe5i2n8JDyogKkp1uGEiPrZqrK5fNGRJLOz8Yw0YQ3bO9SB8VyTsJtIvq9iktkeLbDsCe11E9y7b54nlT-68OBCzdE_T-iVr2WWHVGwKmbrInyeuVc289lt7n9dhus-Rb5iO7sKI8RqInWzfYW1x0YYF_ohujpa7SbGm63liDiZpAJ2Gr5zd0Bph2sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513714e20.mp4?token=Abzt3iJ-NGrTj_rDnye3RKOTVT2Ym5Kvjh8bvYVS2eJeOA5wgEpS3aOG2H7Jof76EdclXaSp8a-HMfUYbX7wJhBG3ZA1eDztYwq5hNCpi6YNCBl_D3-KO8cpECVbOzjTHtAC496uajHn6L2EB_uCDOTKM_mQe5i2n8JDyogKkp1uGEiPrZqrK5fNGRJLOz8Yw0YQ3bO9SB8VyTsJtIvq9iktkeLbDsCe11E9y7b54nlT-68OBCzdE_T-iVr2WWHVGwKmbrInyeuVc289lt7n9dhus-Rb5iO7sKI8RqInWzfYW1x0YYF_ohujpa7SbGm63liDiZpAJ2Gr5zd0Bph2sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/101757" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=NJwwebh4JO8Ps82XeWLsNXT-G7a6UdyFMrqHnEGpw2NGwVMvI3ql5ZVb8l7ewufoOcBZdFo0YGon4I9laptK6I91g3h1Wa9O2GKb2uMgjZiBb1z0-GIGhZolI0P1E6bfEn-Zj1pkGjaGzbNEMSd2zruph2LHPnlmAvohQg77Vt5d2FuBbB-4lC6-gnLuLQzdJ3AToecZITxLgtRcLdC_qH6gRYYCHZipgKLCVOUsStlia1DQhgUW2KKgfXsLr1TR00jn4-ZN19S--2phG2sbPZotG0XWZRXBI7k5oBmSa6y87QbO2yDUO_keip0bx28uhp7WrIvra5p80PbLshqe9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=NJwwebh4JO8Ps82XeWLsNXT-G7a6UdyFMrqHnEGpw2NGwVMvI3ql5ZVb8l7ewufoOcBZdFo0YGon4I9laptK6I91g3h1Wa9O2GKb2uMgjZiBb1z0-GIGhZolI0P1E6bfEn-Zj1pkGjaGzbNEMSd2zruph2LHPnlmAvohQg77Vt5d2FuBbB-4lC6-gnLuLQzdJ3AToecZITxLgtRcLdC_qH6gRYYCHZipgKLCVOUsStlia1DQhgUW2KKgfXsLr1TR00jn4-ZN19S--2phG2sbPZotG0XWZRXBI7k5oBmSa6y87QbO2yDUO_keip0bx28uhp7WrIvra5p80PbLshqe9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🤯
«لی میژن»، دونده ۲۵ ساله چینی، در حالی که تنها ۸ کیلومتر تا خط پایان ماراتن دریاچه هنگ‌شویی فاصله داشت، دچار قاعدگی شد. با وجود خونریزی و شرایط دشوار، از مسابقه انصراف نداد و با اراده‌ای مثال‌زدنی به دویدن ادامه داد. او سرانجام مسابقه را در زمان ۲ ساعت و ۳۵ دقیقه به پایان رساند و موفق شد حدنصاب لازم برای حضور در رقابت‌های قهرمانی را کسب کند؛ عملکردی که تحسین گسترده کاربران فضای مجازی را به دنبال داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/101756" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101754">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2O9vEwDrGP7GHrc3hkkhvoau5uTr07Jykao-JgOJIz32i1mNaYOlzKDWaKnNnV7XPyaIxlm2X9iL4FtLbSWHJCcplPkUyqr2gkBcc9yWUrmV2bFr5KHX97f_e13JhdyN0u9muBQzCg1FTLRrKDE4YH2-R1spJMkVwibfFqhluQFLFtLLLIlgqZTe70FTXc6lvqmJV5LecuoNNisq00DKViultKY3JIbWSAjT2mSJ6V-DLgibyLHWmG_UaBwseku_ThPTvtqQloLUZFNqNrauuXfi62S5vGjScxYLTWbDyFuzJE6gZG58jfWfCLhZS4-NC2Tf69AB2YdQab9cKY7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/101754" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101753">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=NcbUNbukg3LBsMLrUqceL0R7nIDs6-sZjmMKlYiGdEtrtAwxIih4hnb5Hp1_Iwn7MeQuGT4GtN0znVk6e2M5WHPzgLieDICVclsFOhNOa5sMFegUIf0jcYEckxo-c1FQRmlQpO390xB2RbWwmUg27BFMhGIbzEkgTQqf1yaY9OS2oEJm8sWpjrP9AHoIecwfXeTT_La6txMyAFxbumpfh-HivbV9LxnSySs7Ba4Vd_RhHpGfoSjoypD4B-vy1_iQ5zNl3CcVwI4z3S6jtglebjmcytgnDruK1x6qMVIECcB72XrEGS5wjPWUi-kVz6oVrYQDbdVKTW5KCbnkMBfoUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=NcbUNbukg3LBsMLrUqceL0R7nIDs6-sZjmMKlYiGdEtrtAwxIih4hnb5Hp1_Iwn7MeQuGT4GtN0znVk6e2M5WHPzgLieDICVclsFOhNOa5sMFegUIf0jcYEckxo-c1FQRmlQpO390xB2RbWwmUg27BFMhGIbzEkgTQqf1yaY9OS2oEJm8sWpjrP9AHoIecwfXeTT_La6txMyAFxbumpfh-HivbV9LxnSySs7Ba4Vd_RhHpGfoSjoypD4B-vy1_iQ5zNl3CcVwI4z3S6jtglebjmcytgnDruK1x6qMVIECcB72XrEGS5wjPWUi-kVz6oVrYQDbdVKTW5KCbnkMBfoUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد شدید عباس عراقچی از صداوسیما: صداوسیما مصاحبه‌های بین‌المللی من و استقبال مردم عراق را پخش نمی‌کند، اما شعار «مرگ بر سازشگر» و روایت‌های منفی را برجسته می‌کند؛ گاهی با خود می‌گویم شاید اسرائیلی‌ها در این روند نفوذ کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/101753" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101752">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-65pl8uMQ7Pv2FL5cjKJ_wtj3RPGru9vba4KGN4L1KYUyYLhkS5-K8tpwpNXIBNffStJiYYrO1xcetrMxb4IREuGZ5AXVUOmCUFybuspohEPNpiEdvPZ4lvum7wKRjiy9_NhybRaP0QOY8xH0Utk5QWcsowOjlyJhxKooRnzgXv_Alh7HPaYccPvFkKaSOB-3pS0OvpkQzpdALIKX-ifghmdsLwI24mautfnZ7Ulfc81lihmvt_gXYfmYIHIcr7P2PU0H0StqniNt551d-rrpXcx7GLbOn9QPSUTPbDwssCXNPQtCAsiZuNH_hismHkjM4JTVemH70f4Q9dz3kTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
اینترمیلان تماس اولیه با نمایندگان کریستین رومرو برقرار کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/101752" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101749">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fb93Z-bbGx1HOMtozJkZvjATUBSxmCp2Co267nspnyTGYAdfqTRIAH7tYszWRCRmlVn3a4-bUu2l4Bqzvu7mFCMgKc_0wCZZmHkTlVG51y4rI225dJ5MQ5Lr0FEDcsHDiQc4wH_J9hcv6NgNvRuIgCL5aUOqKxMLvzhglMk4YG5sbY8L-dKb_T-GbfLO1qlqU-4H5BHHYTgSYSxw_wGXLuiHfG85qj8cO8pfBy1LRrgH9njFavw6gdSZicGKO1hOEb4HJxoY8GBYj-KtbRRUGbzSGficbdPp2TWP32ho695cYfB5wX89v1xIKfeWUBexlmCnN0_e0MWsMnhloNVc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHbBrssoWVhhv6D8mW2QBTXGD1IxPE6i6SteKmfB6uvw8j6RLOdqUycw53dP8o3WUJPMvqVTr2gcZpze4ASgeScfiudsLc60RC2bGggXy5jfgS8MZf_qjgIdbwatzepF1QPiSVP64jW1YqzizISiPJQ8X3A-yzpoTdWAql-bN9u8A2cqhPyEq3sfjh4A9MlusdTFehXdfYaWva2AFr9zJDeQTUFvYnQj-4wI_wuZn5QdLl2PMKspM3vvNe5Zf-a_EeD0XKwL5v6QNmzi3LXQGrOG2h_tudomOneErhzG-6G2EXYPiGxF1kYnUuS06sJlAPKw0KS3VFYb0Bh5ZKwHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcnpPsBeyiSsZ_YcUnn9ypIs3vLD5UYgIysqc7fRwIAEZWBYg0LI2AvS6hF2RcoT0a39PeB-X5PwxVYLO3bWcHI4ZNPfMnI34H0jaxQW4ZntfMWKS_NWyLwbkNmEbcKvZSOYlrtnNB5JhYan2OdfEYSct8QhKba29xifUCsvuV-FP4Uie3d4FIbuuiTW6aTklk9IWhkxhCUYtGJHklOonL8uNeYP0MKZu-Z8NUFpudtXWSg2RMi4Nr1tnB3W8Q3wfoTmkaMBqNaY4Z-kSOvwayS59-52wEJEB6pWsgk-hWQ-BtHb5SSPxKRdCYwdTMZmHos5mEYNw0eHDLjA4kbMQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚫️
کیت‌دوم فصل‌آینده باشگاه نیوکاسل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/101749" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101748">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXHraIypG60UJV2mma5PX3YfTxmv1Yzl5dPsMkekACW9KM7qa5xymIuaNX5Q0zVQVzY9RFNZKjyC59hKj9wK0to_QNGDoN6g3ubqKLPxi7-BPI0jc5cWDRkNDiyXOxdhrSqDXq8lvw0QxxpEu9nTyndlvBJAE1Hou8zyCzveX5BTm_iA4i1D0993mmd5031qQ7276IGuP4SRC8LFzjM_cjxXGqWm6rcknqU3NWT0ep2ef1kdfJ8xAbtB3DsTVTq4DTQMapwR_OPL8va5VeE_lkmmnFCm7DEpVKYnHuofMAyvl9Psx-uHg6tQKeNg2KJoNeT5i1fvxr9w1m96cINNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
لاگاتزتا: فنرباغچه ترکیه با ارائه پیشنهادی به ارزش ۴۰ میلیون یورو بدنبال جذب رافائل‌لیائو ستاره میلان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101748" target="_blank">📅 11:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101744">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tza--ZDT7lsGycKmWj76pHW-r6zVrBT-yUri5yHWzmAkd5rOr6LC0-Amu6VQjXdS5MloYRJI4pCe61fhfWrpaZjTp5HJWnCfFINqDaImJgdwEoswGl69zx2pQdqsmDKteZN9eO6B6b6COkLBZ1Bvf-1M325biuTkPCG6dpoJJ2ledfx28bhiDfykeKXSs-HPSDMu7zLRaRG2jcT0ZRHUl1SNHbOXMuLZpFxXEzqj9RldzGkVzkldOHQN56VIzVuFXSW-7FCBPv1tnWazcFM8OPbT8jEJ1JqIePfvLTC9VV-h5FskZP0R4Gf5bd3SAlBdz4_IQO7WaIoURNcQ2Jn-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9pUUYzLjbmvmi1lROAuExOMgaGZQh2AY92G_wIS05QIyuM9GoqWI-iOfS5-kKn9zXDVmkmYGFKnwxq1XchGB_89s2YczGuA4roRLy7r5bcXrXLQ3LJbf5ATw8Xc7iERjdboKnzF7n3q3LIQgAVb-GbMZnfzvBCsdbNO04-_WNDewAmj4fGaYcMtAoeyNQCjBDc8McLtIaWWbBXy6fKyQZA_1C_I0vsg5aSqugygYr0VlXKFEFf7TdT8dG1od8uSQR6ibxUoJ2BUHvddt901CAslI0o60K7fZmbMNSOYiMjWJDQoFfQ2jXPAIInBVTIdSv4s0DDZKOo1C6BegSkaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfJKT4oWPWDhcGNh_HSkfM4bp7k-26v2gvjP87CB5RXgPKXOBaKYvY05PfZOwmWFon58lx-qOU1h0JTeAR-WwHl4t588iTd3lGStWqjSg-vyNwsl9382l0eY-edZF_5I2mzC-DEF8c3fumY6PKf8DBzfb1P9Xipd4RWtExzMNH4LQAjvhsH0Xdu4LiUFZ0xAwR62RAZVHu8HJNfbYgO5C60KBSTayecgL0st5vXF2vXVJdMfMS9rHKvxnFR3MnJB0m-krEBD4JctfeX1W6KbrUOOjy088BcVXq27bOznyTy6YPf6fcBzd15H-EWFoSKhY6U_eXG_uafaXMd4N3Bd_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم فصل‌آینده باشگاه آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/101744" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101743">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=LGHGtPCj9CRtKjtTTFYZKKSMxiZlAbuqGxZoL73u6dl8aGvbeptl073LEuf6YvNwsnNQzVVkeIPfDIfhMQ9c2ddGRvLnwLsGA-lcSUqgcljwQ08XaJJPCBFIe54-FgVBVZt0F5ya_tfMHBDoeuDP_bjiZX_8TyhIHxH-UUA9kiVafoUQUJkOpWnLunhmUzKH1FBcdpxF8ZiPKeiDfHdYhUwkxIaZOGfOo-ONFcVLlE_TX-0rN3HysXJL5h9AmN4ht74m5qtQ12dS8z2g0Bp8oUXMGuzn097Ir26Tc-e_VGTgfwxZ3HfKayFjs1t84k_my0pa4EOX9SIgQVMf4-vR3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=LGHGtPCj9CRtKjtTTFYZKKSMxiZlAbuqGxZoL73u6dl8aGvbeptl073LEuf6YvNwsnNQzVVkeIPfDIfhMQ9c2ddGRvLnwLsGA-lcSUqgcljwQ08XaJJPCBFIe54-FgVBVZt0F5ya_tfMHBDoeuDP_bjiZX_8TyhIHxH-UUA9kiVafoUQUJkOpWnLunhmUzKH1FBcdpxF8ZiPKeiDfHdYhUwkxIaZOGfOo-ONFcVLlE_TX-0rN3HysXJL5h9AmN4ht74m5qtQ12dS8z2g0Bp8oUXMGuzn097Ir26Tc-e_VGTgfwxZ3HfKayFjs1t84k_my0pa4EOX9SIgQVMf4-vR3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کاپیتانِ اسپانیا در رویای پیوستن به رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/101743" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=bIBiLS5Qdt8e3Pzb_h1REWM5oRBfULqfb3nRiDMJ9I--ngPEhCcCndh-hQZS2ikfriNvcHg49TqTmvIos4oID_nl3OJiVS29FT4korWoX3qDgJWpf-0Vp-JT1tjITIRtKnWmk5Ybus4k5y15PzJeRzyOKftneBE2_MwSqph7On2XGydWW30UoGPxdMpRrEpCCViALtREw3BGs4GcTjgf9bDsRrqTweovzcGa2EUEBA3l-pDPr9XFDljIWpfFI5dORJS4i05C4eGnvqsw6LaLUx1uBupICVt718uUSHfSJ_De9uYgFgGXWbpJOvXmU4ZpxeHFX5hIbzWHgpOHuY9mnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=bIBiLS5Qdt8e3Pzb_h1REWM5oRBfULqfb3nRiDMJ9I--ngPEhCcCndh-hQZS2ikfriNvcHg49TqTmvIos4oID_nl3OJiVS29FT4korWoX3qDgJWpf-0Vp-JT1tjITIRtKnWmk5Ybus4k5y15PzJeRzyOKftneBE2_MwSqph7On2XGydWW30UoGPxdMpRrEpCCViALtREw3BGs4GcTjgf9bDsRrqTweovzcGa2EUEBA3l-pDPr9XFDljIWpfFI5dORJS4i05C4eGnvqsw6LaLUx1uBupICVt718uUSHfSJ_De9uYgFgGXWbpJOvXmU4ZpxeHFX5hIbzWHgpOHuY9mnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101734">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mh9hyEzZoK6DkU7uHnmPqwZzzAJso8ujWYOCkchSzmfB69heDk3IHzZyglZJGC7iAR3e7TLlWUmTKREou48wqWqhT5QNkBr1-faMi6OtVaThMhRwez-hS4gOvckSQJ-imzFzfaCJGCwZlHR83U7Ku8FFmJvf4Uk2AtK2fyzkH0FzbBXWmQ27E2mwzPVImbFr7VxJxQP7Y-dWyirO1cuLuZa6BWkZbgJu1QBLg9y4113OQQMckKu7KVtv6UtvRozc2z2I92oP0ol0J64CQv5QwGXQo0nEyDJzBNqBgjfqpd5icg-M8O08cKAvLGAoIucaMh3VY7xXtWHxSHQLCDSeuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ho8GSJojYmHbaxpDqdpujhSn960MEKzhlXkP8MGApwFpaJj6rHY5U_JsXevMzHO9YRGGI_8o-1qVJ7iEquHxWEVKF0vtQK9CkL-37jvtDphnIDdwqaeE1nHj1nL1yAJO61R9RfJKpBA9Ou_STFqyTH_D0897IDDENxRVCuJwiflwyOJjybjwZYaq0xkihOIYomtNLnCMtCnfuf0iE_kOevfG_XO7vvgHxATn4u0e6OWuV_bZqxtCOJH1aAVoOHc-brPVvrp5UhQ_glt9lETzBtEQp7uUccpj6qG5LfGRg2aj6zon4U_JU-EcT3rx1ph76jo5eT5jmjZ0gRRyOmF34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-lNsM-Adkjw7M_a2P90yrWe8aAa5GFPPW7NP3kn-bN4eiYDGj0RRArpZy_WCHOXTmNWrLH5qXDO7x9EWxbvQC_w7enDvXquxuKeh0t9-wWRSKm1FqRdVVDlS-Z8C6sH3hUyA-irrFadfdoOqlUSpn-OWRL83FqxNyyZ3pRVnt_9aOfosw6ktJTm3yUuSc5HBl-1rNySaGf7UKNMdRvNRUFANhtG6Wjt7KXcDJRBcE0OeMZ6Ig2DFwqnm9O7r-uIXzlVpqCTKlv3xAa6eUSsKL0QuGFFzNYqo6LeoCGos0P3KKE-c9z1-c14YBf_E8XI9S42hiFdBg_ZtaISf30H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJffoNMyL9gwqHSZRp-5EfYkv7Ci4geB_4ser8aXrsJk2MGWY88zcad_9eWx3QtZTu4gb3IRN0jJNW8fSIBi6Zd-l2oGEBRSU-JmEab2H2oEVzLe_WTMRxcbF5B_RPw_dImuK2N4wi9cNRI1j8-MKz_zxOjaqp_mWW_E89Xc6rERWEDby59MW4vDZO0FmMi9yRhz2OEOqwWeG-_NuE0CM7-sLGJ08NxstlEPoqx4yjRU69gaUTk-O2Pg0iSrpnxzZEpJAyLN_zVzq37gFFnmUOaiMgNbozuO4GczIyyV-kGhvLOHMVBrI0hjswnfIHg7JDhi0dlovsgwsyBoh5rqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbiCkPrT29di3jZuclRDvyiwRA0_9CHenN3InJ6uaJAQepUdm_96fxuy-bsag5mdcG5Pc15UpmnZtxmgyAegrJv9PbO3K3gpB1UUnKs6OeoM5DDfmI5CYV1HdNvgZwxsruTHvdMYnsYSz80RAhK7tR58X0jlhcKDNNnPMYFwrbYmxvxtcN4dnklRGvbNmZZXtP9VlX-Mu1f6LFzOI6wc278OwODaTm7DIC7jK6Lu7Jhjacu6dQNp2HFQO4py4azppnqei9uiU_MqOesbpLiNPlIeFUGgM4ySFbKU4jumDHZIStWARaEix7xoFb1W9Z6TlgbYf-Aa62lPt72v5pa7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NeTqv4FXr31EsCdi8KcfP_MOaBhZe51Rftq9GLaUD2kdDBpwzV-35YL_DQxlGOWxpmOTrrS0GZ-zhmGDcAhPeify79h9sfllU9okoG7i4iJDhKY0fZ6jDriv9klxxtvQiJYh35k1NrdvzzXAQdZH7gIoPGyJUEZJ_VQrKE2XgV2Kgk2Awo4DMdtGuXF8A7bl1cMrVyrHpLXQxl43vFQX02fkdCMf5P7CZ2eV2afuI9b0PFbpbu9hB0RuzKlQ9_gHPeEopCvsO2RpeK3QMVVmaGZNzv8IKHQKBd23JcmU-Ti3KIiIk00VRDBW_JJIPJWRF5jt2QLJxIGaX0M6hczN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppM2Lnhl3CEtjq8VdrmBzYXigAeCEDzfM7cGakzXO9lX4q92aVE63LPiVs5QclSrkVnqR6NBkwWDIZ6vW58bxEMYasODJ8_NLR9EdJJofDW_2genE13KM7OQdleou8d6k36G5U_SDoxk_IT6olFDU5GOscAUvaKxOYjx2YK61H0MWtUW5pLcDiphoO1AfZw0LHvprzfM1aIot8vyrLcOZBW5r6S_FqD8tJ6yJ0YZPMMga__1YRwl58MgIx0PPqGJeGV-qIJ43qzTZVF0aNhmwP4B3qz1Z1Zu6DZ82-cEli2I9CYjbbCbJSUeReUDB1B7fkL9eaMLs0XU9d9mtFF2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLXiaX1BU7BxXFeqPwbs-Eankxn4fcER_1ASlQOvLZw5Y4j6KvgW81dtuPpM1Fk89tC69Kzesn2LnfMEm3psmsSm87fFURy5YE1Kv3h0hrgHU6rqeL9v71Kf86l6tQto7Zf3KyQRhOkfW_edD0PmgI-ObDm9UGYYKc7htVZGLLeNx5f9YPe7QI_neSo5ZPjSVxIjVMIsuKeV39w_iMHCAycXgd1pc29MZ1SiqYWzMid_e0yXSF0-9lZbdTEwU_pGcniUlAu4ONdGZxQOuYThNtrsndD_RlSBmAnFK7oxnz81c6Z37kkffQQ39ZqneY8z_KZhuXriVKVOu8AW4BujmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
کیت دوم فصل ۲۰۲۶/۲۷ بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/101734" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=rlTzCR7UhMECd3gH8uzIHuTGeG_mI-u5JHwnINyTJi8OJK4WGyIjEtQkOqDvU0a1y1kZD878b5zfwfQrqH_kjdGrmJjlaXZLtkyb5qZ7Iu81l4rX4NxQ7Deg3Pb2Y-3uX74_ydTP2RFe0kLaxU1EoeKfUYeSrow8-G6QxvyzybVjfQpaC2HpWCq98Gmtq1bnLg2koDdq99njllgas6M0QGLsndfLAKC1HACkgqJLfl4Ujlt5qeRLb4xapfkSI2SinftVm2xmhT_x7H_MAz_8MQ7T3DPS6I2VGu1xaGHScx2tkze_dSwYAguww8Def7SV8VQ8aZYDYrZCjfdDsfaXNi5KcBo7fSv5SdHLcOCBE-C2CFQkwRXdS5G-glCFAorSEuI6vujVnmcohgBn5mjiNHMcGzM0kZwNrwl3oOBzgjR12QFAYFyoe92YJvC5-nuoHY0r0gHba-hUQyrwlPhTDvD1TWoX9c0h-6ae92SLMmTcgKS2H1rym8m2uQ4lOE_L9P-cHrinFz4phqhp8y_xcEdxfl5JbYfyuovoOsJGF0ox3KFo3a-6aWMEyOZ6r_i3J8Y1fXKVpQYr2FXnc1lX5A_Wu3daNk-UeIf3D7-OG8ANZgFl7fLhpTg2rdF0TJ77L7IarFKMmsNk5i9Lh1jjnqVTPErvC_N7OkrmiOB8Iqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=rlTzCR7UhMECd3gH8uzIHuTGeG_mI-u5JHwnINyTJi8OJK4WGyIjEtQkOqDvU0a1y1kZD878b5zfwfQrqH_kjdGrmJjlaXZLtkyb5qZ7Iu81l4rX4NxQ7Deg3Pb2Y-3uX74_ydTP2RFe0kLaxU1EoeKfUYeSrow8-G6QxvyzybVjfQpaC2HpWCq98Gmtq1bnLg2koDdq99njllgas6M0QGLsndfLAKC1HACkgqJLfl4Ujlt5qeRLb4xapfkSI2SinftVm2xmhT_x7H_MAz_8MQ7T3DPS6I2VGu1xaGHScx2tkze_dSwYAguww8Def7SV8VQ8aZYDYrZCjfdDsfaXNi5KcBo7fSv5SdHLcOCBE-C2CFQkwRXdS5G-glCFAorSEuI6vujVnmcohgBn5mjiNHMcGzM0kZwNrwl3oOBzgjR12QFAYFyoe92YJvC5-nuoHY0r0gHba-hUQyrwlPhTDvD1TWoX9c0h-6ae92SLMmTcgKS2H1rym8m2uQ4lOE_L9P-cHrinFz4phqhp8y_xcEdxfl5JbYfyuovoOsJGF0ox3KFo3a-6aWMEyOZ6r_i3J8Y1fXKVpQYr2FXnc1lX5A_Wu3daNk-UeIf3D7-OG8ANZgFl7fLhpTg2rdF0TJ77L7IarFKMmsNk5i9Lh1jjnqVTPErvC_N7OkrmiOB8Iqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
تمامی‌گل‌های کیلیان امباپه در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101733" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101732">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=TbxuxGswDF46rMJh7mEyqbozzZyEE7-6zC6AuyLMdeSvasMFmVJdatbgckO_i-7oyKlajtFcgWLqpS6uib-O2yK8mD7GRw98_FAkXLA1Sk0kXXdjeme4Rw3F_LhsrmDzBdB_4liPD7FwRE5r4SNqpA1B76BpGP94u1zW3GV8W2p-5NDvTQ04_7HB_GPpS1AWDGCHasbRCMbCrVcCzmkgl05Sc045YDNAerB6-9yLrvsF5U9hmtR64aA7fWfaZlR5mDSsirakf0vF6-f2e517s3cb9dgGFpaclHkT59yy6opmzWx98MQlvBR5xB0O6wR6qVhzQJN4aJNkgTiPeG_dXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=TbxuxGswDF46rMJh7mEyqbozzZyEE7-6zC6AuyLMdeSvasMFmVJdatbgckO_i-7oyKlajtFcgWLqpS6uib-O2yK8mD7GRw98_FAkXLA1Sk0kXXdjeme4Rw3F_LhsrmDzBdB_4liPD7FwRE5r4SNqpA1B76BpGP94u1zW3GV8W2p-5NDvTQ04_7HB_GPpS1AWDGCHasbRCMbCrVcCzmkgl05Sc045YDNAerB6-9yLrvsF5U9hmtR64aA7fWfaZlR5mDSsirakf0vF6-f2e517s3cb9dgGFpaclHkT59yy6opmzWx98MQlvBR5xB0O6wR6qVhzQJN4aJNkgTiPeG_dXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
تفسیر نام اتحاد کلبا توسط مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/101732" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101731">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=uY29yekSXdXRx0Fn-ENSV2kOONr4MJYAMbkFbh15K9Rn0EM4AtxEFqI46mcTeeiEtxBHNqPu7xG6GuWjjupEdiihchVhVxys54HV2SvAyS3n9FnmPsArhWntRLkTRVy5pP7Z-iAG_wDYgrCvMovzDsBs9p5ov4D9hLBriVnpqyTdVtYHfaYf8vwyFlA2qT8HgiLA-USoRPL-leTMuhwJpVORmV_mrM_IgDI95461OryjeNsO8tiJsw-lKntcwUOXDBiWw360TJkaf-B-vNk9DNrd4Uw9aIfwdH9YwzeKHVZM9VlV1Ky3TJLrCt3AA90iViNnwcBLBM3lA2gQZ2N6Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=uY29yekSXdXRx0Fn-ENSV2kOONr4MJYAMbkFbh15K9Rn0EM4AtxEFqI46mcTeeiEtxBHNqPu7xG6GuWjjupEdiihchVhVxys54HV2SvAyS3n9FnmPsArhWntRLkTRVy5pP7Z-iAG_wDYgrCvMovzDsBs9p5ov4D9hLBriVnpqyTdVtYHfaYf8vwyFlA2qT8HgiLA-USoRPL-leTMuhwJpVORmV_mrM_IgDI95461OryjeNsO8tiJsw-lKntcwUOXDBiWw360TJkaf-B-vNk9DNrd4Uw9aIfwdH9YwzeKHVZM9VlV1Ky3TJLrCt3AA90iViNnwcBLBM3lA2gQZ2N6Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇦🇷
صحبت‌های یک‌آخوند حکومتی درباره عدم‌قهرمانی آرژانتین در جام‌جهانی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/101731" target="_blank">📅 10:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101729">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nly9Avq5v9FsnA4Elf1Y8FKcehk7RYvHTiGUxptXMX3w8ZPVNoRTeR_bjTYXGboqyzhNxdXkdPk59B2gPY7d_yLyJUHFOJDwxg4GfSuAkmphuAa3j0h6IKqOcXHUTcJSfvXA0DMVUPTWMqPwke-5YyMcmWaplKonweZQ9ysbeOzjCoV2HFDdXkCeSL64-0TYwwmLO61Jhc-YfaY2s4cwoUaThzYbeOrF7-fQmw-88takHHndKmou1lnadEocLv84tN67WCPXRNCm3besw6NyQaOB3llWeRE-dZn0X1cbmDfjelG7bHdfBmHnRVcOsxF39nSaR9nBn1W970zHPcOJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-3UMVyStN9IGXzen1pU8EpOItprcTLIobfmouYaQkNs8ZzCoWICwlFNYF9uwIA-em_eKG3JSw2Rv-bjgxuAixAqD0A9lBMyPzomiW_MluymY6krOHuelBbAoCll9s-e3kxuuSA-TX78cRWl5RqV5abUkOxGVxVx-ySsy6acEdC9NmDEj58i8ClUyC24ghJsG4rBT0SNVOuW1yHkEzmDGZPvX1_XQh0opvAlO5meST2i90SPUnWQUqf00PWo67Rv4SWyPBGwIWWPa9lHy8Y6T803Hvtgsuv9zRKV8nJlGDDbdrn4X99kp80AZJQ1_ojpt6vTrzWs7Hm4u4ABK8PA7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفته میشه لامین یامال، دو هفته پیش به دوست دخترش یک خودروی مرسدس کابریو به ارزش ۹۰۰,۰۰۰ دلار هدیه داده
‼️
این دو نفر در حین خرید خودرو با هم دیده شدند و عجیبه که این هدیه در ابتدای رابطه اونا داده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101729" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101728">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pS5kgn9ApiyCpk6Lf0EFuQPZagyTwnScgNffoLKGvPkHk4RldvC3WaBbyz9ZuwPnej2Wf_BWhx70whw0Cl4Pg4MeGzHOMzZdI7CkkoQ4x_ZxEwSHkrJpSsH9Mrg7hdtstanQ1fdEQS1x9h_o1GVL4buVehS1myMvKu_u4pboJ_8cNyXSmQj2yaX6hficX7amMkMSa-K3uhxh6cnvgc7NsRX8K2kmWcVDHdJtIOSNfoHqnmAOH9aQDB3Wi_e9exAd_0-2WMOBmzdXCACVxh0eW8U65QysnlzLi5MzrQWKURJsKZMwBc1ePaucf7W-S6YE8hV6X8Z82pSbfi1QhebpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇦🇷
پاردس: آخرین بازی ملی لیونل‌مسی مقابل اسپانیا بود و این بازیکن قصدی برای ادامه دادن نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101728" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101727">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5H-qpoaLqQafGeB5Oqcar4dhnaMBvMOvzZQOYJ0vxmB1UVBw8nczC_MH24Iw3AhzCzET4VEZy2CmzTyssFgnS7XsET4PQWh65ZD5ZP3zy1qo7FltCPtHiEdSgLsZBO2q5wNTxNf8BuFZo6rvjwyEPMDvZGitCZbj2Wp-mwQbPLYek4s16mO7w6p6-asQDyAoZBwqzvyA3nu5W2zffrzI-knDDY53epxQZsPXdFa7wB5zebCO1l6sNLF60_e-uD40wqv9jZSbXGac13l_EqOuZprCrX8PeS7tCzhoubTLwV5HuJ0V-h7owkEyL23GnJOT3hB9cxyh7Zt1rzYl_UHmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔻
الکس فرگوسن: "آیا منچسترسیتی از منچستریونایتد پیشی خواهد گرفت؟ در طول عمر من، این اتفاق هرگز نخواهد افتاد."
🔵
🔺
منچسترسیتی از زمان بازنشستگی او در سال 2013، در هر فصل، جایگاه بهتری نسبت به منچستریونایتد کسب کرده است
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101727" target="_blank">📅 09:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101726">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/octddM0hblzRKu2CBc1B9WVNjbADCSjKr6wBrCFngNckoARs8afmwcLuif8FburasyqKXFGBmE7vgWqxf1tdHl0tpKd3SfTCz9Davzhi9XiQOwwRIBbXZf6sDRrVYHICAzZqZKXuZeqwA9fNgAjzzVhl5STPO1I0bhdxXXZIp_q-30MvOhl6cI8Sf3Tv60a5zlAv3rcCd5fO2Fch-SvU_dUlL1IqEJ8z4n8kpdhAvC2JYYOjdMNHQmyf1oS-TuTb2FBu-RYMv6bfn37zwndaR9Ud6ykez2pK8B1bKN7hcIje5uuLn4baqnMqPr9omKvR8NC7Om-_2COqynd7D--nHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
✅
تمامی ورزشگاه‌های میزبان یورو ۲۰۲۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101726" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101725">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzsMs502RsvgSHY9wWGUIV_8_VUOcPkFn2ttRuMHNbAPKWiVrCyXWVmHyc-Hl8UvzYp0cIy__jtk7z1Hw8TS73dSYFXBp3nisChVeYYWb5eTbbl-IwGxE_yBiqn9OQc4tw2VCuF5tDGFyeQm2caCOIuHl1URs1USa0E4O8HdWnvfIu9yn39cl0wYEpj6cBCRdMT3Qtjciq8QSq-cQPGY6ZgH48lrZAshSLroD3gPzw6eM4asL5Tvpco-S04n0PdEn3-9hiD7u5nGfp_cxPjY-R1mBFrvPy5tCvmTXJvqLlKUN16wX7bOOIVlbbx6oFN5fAKECvEhHQdhMDuRDpP3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
کیپ ورد در بازی مرحله گروهی خودش مقابل اسپانیا، 0.28 موقعیت گلزنی (xG) ثبت کرد.
‼️
جالبه بدونید، فرانسه و آرژانتین هم در مرحله نیمه‌نهایی و فینال مقابل اسپانیا به صورت میانگین (Xg) 0.28 رو ثبت کردند.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/101725" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101724">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_LkXG9ytsMofTrPCj8bv5AOXjpWaiJsZWScK2G1GUZZOkSj-LuMhHLUD9feiTF4GNtn4ODG0Tu6HmBh7PP7ouBiL1x5Xyh_WKHk16tDFdLzORSmVMVIgHQ_OryECeoqg5G1XQxAZOoWV8GvFLoGx1IfqWhusYSsL3NxKJTq9PO_3rnrYRTm0RqcLLt4MuYxlJOeQ9qIWFwfkxxvH-m2PWpYpLmFOT6Stor3-DJ6zD6BybH9GL5ymhmf_wUgSu2FoLo2zZunHW0aufCMWmoH266tkpeeejI9T1TtYSVeJmrU5kMRyKXj2AtMorSe2EcZ9fBsfMv_2-7MGXX_svSUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇫🇷
آلمان و فرانسه میخوان درخواست میزبانی مشترک جام جهانی ۲۰۳۸ رو ارائه کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101724" target="_blank">📅 08:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101723">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlhLUd2O2WVKOmZXQWyU67-dDIml93U2yQu5xuTbZBDC_JCbEgY1TmwMJE7rXRrI6ftOCcaYOjL3NMvyMJT9j6husN_QLFVkR-b5GnXF0oWHASXJVLp-BYIcHOqvfox9xGgYRpvyzniOto6R5pRpCxyfGgk4rMFCPn3Zz-WZb1u8BJB0tJwiWmvAhXiV2u3oY0lbIzPhb0MJbpNwP6gYzA8C8WC8YsJeWhN4IG6-S6UhIerV3L3QRlsckytwKIe2aIriNYRFuyj17dMvWApDG2u8UjQwPW3hgMoE901QYHi2bdXBUtFUzj_m6N5FsxA1S4wzPBNV-Yre3GJYgF1ifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#
فکت
؛
پشماتون بریزه که بیشترین مبلغی که آرسنال از فروش یک بازیکن تو تاریخش درآمدزایی کرده 35 میلیون یورو بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101723" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101722">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=vKWIN0y_4OaP2ejbDUeBcS6UwI4gxgkTnrubmy7_fOtVyQx_HK86gnvJXvRgjrsdNvJwIAhAMFoY-sm_-h60yE6r0jGLVW4NmNKmFvYkEC_VD-wkYH0ihqLpJw5ia-zwHgorHgvaPaNrifozp6yL6sF2uh_n-WvKV2EWZQ7dohNsUtBNBEoFIsqaR5CjlKx_ziRGWlWq9di5lS3gMfKxXO78vpaG-ttx5XwTGYjWWmKzIBNogqvVVA9nii7JOatp0Wv0hDj-tyosvfMp5kcjalaQY4S1vPoJXH-0mg7S0orVfse603IuzJVf21T5A4NFkm9FhZiiBccnKZRo6EEUAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=vKWIN0y_4OaP2ejbDUeBcS6UwI4gxgkTnrubmy7_fOtVyQx_HK86gnvJXvRgjrsdNvJwIAhAMFoY-sm_-h60yE6r0jGLVW4NmNKmFvYkEC_VD-wkYH0ihqLpJw5ia-zwHgorHgvaPaNrifozp6yL6sF2uh_n-WvKV2EWZQ7dohNsUtBNBEoFIsqaR5CjlKx_ziRGWlWq9di5lS3gMfKxXO78vpaG-ttx5XwTGYjWWmKzIBNogqvVVA9nii7JOatp0Wv0hDj-tyosvfMp5kcjalaQY4S1vPoJXH-0mg7S0orVfse603IuzJVf21T5A4NFkm9FhZiiBccnKZRo6EEUAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اهواز از این زاویه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101722" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101721">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=Yvwqch9kApchezOHxyUpzqaCSuq-vhdE7wT7BRMTJNuVeFW6GZ6uqcEQYUkTsnzQo2ucrmeTwCUqxqzRdsO27t2nLt0oTG2BvoCCisxFrgeF1QkktzAYKNYqKW46A_nv1Fl3_5xM0nQXjEcH7Cnj_NjduK-y0t9IVvVaaJKHo-lxtw7EaTt3jrBQgIZHqC580RrAngF_Ib3IQ-4YSvGWcxH5RRnIuiNYT7YnN1SrrQ5cAvoDlnk6wruVEfPBFKxnM5GVIBUnwYPSiQjex4AieK7PbE3ymIVYLu2N7O3wWpCGGACnluZOjq6xGwPonMQBoY8oDnBYfC7tVNZPwzVYoXSOb8gFyPYf-RFA1t2B_m1Vv7-YMvs2FrhsGtjAhN-YilAePO1PplrM3g5do14ATx6w_AyO6ESNSNw7aOOosoTYwHfzIoLwDACJrRvAPJvW9H7lIFUfgaBui7mHf1FliSEstswLQNmsf8vMajmr45TMslNzHrQpnu7TbBm8UZWjgwGHG80b_zvqUFEj-NaEmJcZzRrPSDXM4Ssv7WEbdY0hiiLW1KlhKI7LcZX-P59WHcIXYyJq3lWIZQ0VVCGDhu32CZisRxZIRUfsT97qfaSck6RqtNJUAxlh8lQsBZ26axQuBeAbtmjChlfcs-zFi3Bg0KH3ONtNlMcsbGfqK-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=Yvwqch9kApchezOHxyUpzqaCSuq-vhdE7wT7BRMTJNuVeFW6GZ6uqcEQYUkTsnzQo2ucrmeTwCUqxqzRdsO27t2nLt0oTG2BvoCCisxFrgeF1QkktzAYKNYqKW46A_nv1Fl3_5xM0nQXjEcH7Cnj_NjduK-y0t9IVvVaaJKHo-lxtw7EaTt3jrBQgIZHqC580RrAngF_Ib3IQ-4YSvGWcxH5RRnIuiNYT7YnN1SrrQ5cAvoDlnk6wruVEfPBFKxnM5GVIBUnwYPSiQjex4AieK7PbE3ymIVYLu2N7O3wWpCGGACnluZOjq6xGwPonMQBoY8oDnBYfC7tVNZPwzVYoXSOb8gFyPYf-RFA1t2B_m1Vv7-YMvs2FrhsGtjAhN-YilAePO1PplrM3g5do14ATx6w_AyO6ESNSNw7aOOosoTYwHfzIoLwDACJrRvAPJvW9H7lIFUfgaBui7mHf1FliSEstswLQNmsf8vMajmr45TMslNzHrQpnu7TbBm8UZWjgwGHG80b_zvqUFEj-NaEmJcZzRrPSDXM4Ssv7WEbdY0hiiLW1KlhKI7LcZX-P59WHcIXYyJq3lWIZQ0VVCGDhu32CZisRxZIRUfsT97qfaSck6RqtNJUAxlh8lQsBZ26axQuBeAbtmjChlfcs-zFi3Bg0KH3ONtNlMcsbGfqK-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو جدید از حملات سنگین به اهواز
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101721" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101720">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=ZLtkFZ9V8ixgkTxfXz2YE_8MsE-UBfLMZm_JE4Mtkpq3IJuYvjb0DfioQgwanblmIbShW_7wjqDGUbk2Hva2hXc_QU_A1pv3vQdRw-jzYZ-Qj4L1Y6-ANOXUMcK0ncU6IBIsXGejQstS0bQ0J1POPTe8KPwlkzZM90bfXjfPewdsK52_C-lW_Rs9lvUFRgceIyGZtuN8I3mjwdcLqKR3a4-6pttHQS9XC0t5d_Zn7-sIyM8SGc538vbWe4_oMIWLLRb2_cR8SUjz3ZEcYnsnBSM2cfzpX6r3bEh7QEdpMYRHd3kZzpWJXauu_p7B9QTGTt4k9nBtHJMyvgRBGx8Tlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=ZLtkFZ9V8ixgkTxfXz2YE_8MsE-UBfLMZm_JE4Mtkpq3IJuYvjb0DfioQgwanblmIbShW_7wjqDGUbk2Hva2hXc_QU_A1pv3vQdRw-jzYZ-Qj4L1Y6-ANOXUMcK0ncU6IBIsXGejQstS0bQ0J1POPTe8KPwlkzZM90bfXjfPewdsK52_C-lW_Rs9lvUFRgceIyGZtuN8I3mjwdcLqKR3a4-6pttHQS9XC0t5d_Zn7-sIyM8SGc538vbWe4_oMIWLLRb2_cR8SUjz3ZEcYnsnBSM2cfzpX6r3bEh7QEdpMYRHd3kZzpWJXauu_p7B9QTGTt4k9nBtHJMyvgRBGx8Tlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پشماممممم صدای انفجار اهواز بشنویدددد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101720" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101719">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101719" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101718">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=gBicIgG9pm3x-tJ2RIxULra8k9cKIpiYOscY-jYVCUcxmBpJzR7zg0-36N8OuyB2eCEpkp0tR3z5GkbFmIhFZnWbXV-EZ-EY4jsQM6aulBDL30RULLBpfZSy7zaGcxk2LE6VekO_R_L_qdR_IOB5-1Czub-QUhXw6L93gC6aLmlB-0LPXS1-3fm-ybfyi-tknRgFADnEAISos3Wo05aQK9xRQUjB78Pjm8t0HEy95LP8dN4B_31oEi_yy918YLbmnrcVKs7saCxtsW3heWYx2yb37TRMrZI-y2WQ8Kf-8dJCcNs4ifMS6KFXHgcA-lTfujk_exgbu2xu3cew5BnnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=gBicIgG9pm3x-tJ2RIxULra8k9cKIpiYOscY-jYVCUcxmBpJzR7zg0-36N8OuyB2eCEpkp0tR3z5GkbFmIhFZnWbXV-EZ-EY4jsQM6aulBDL30RULLBpfZSy7zaGcxk2LE6VekO_R_L_qdR_IOB5-1Czub-QUhXw6L93gC6aLmlB-0LPXS1-3fm-ybfyi-tknRgFADnEAISos3Wo05aQK9xRQUjB78Pjm8t0HEy95LP8dN4B_31oEi_yy918YLbmnrcVKs7saCxtsW3heWYx2yb37TRMrZI-y2WQ8Kf-8dJCcNs4ifMS6KFXHgcA-lTfujk_exgbu2xu3cew5BnnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101718" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101717">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSF1k0sK8vl9cJPysRE0auE5m_y3cmTTFdUbvdDxPRATu5btp0T5sYFf6cD4wpWc-Dx4uYNG6x_usMMHYbQU6d2ZEo3k4NcO4BJMW70ac-GZEDxy2dyJFQsrLIr-WfwzL1Q8ADyquGuNVfEcWVgToRM1meSxIgwvpqH92SI6MOIqc7wMHfDNgvrosUvdfpQYOpa9jAkiywk0wmnS1ORgwzw7OSQgLgXiYFERx30ATmxyTIqd5nUAASsMEWGvgtbL9xcbgwEx_Sx_kAgsuih6UtloYYtCedNXANZp78KPY0PxLAZhgv49pdI9HiPXF4iKMPMDLTFITmdftknqWJZBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✅
کریم‌آدیمی ستاره بارسلونا و خانواده‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101717" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101716">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=I8-CrFUO66bkI_t0GWDdGWEzj5-BALcsf9E7Inkl7L5qil1bBtRMjBvFwFpEODHA88WZOE1FmTduj-XzLtzv7yozSnV-FG2zZkSparXeqU1anVP0z0WF41k4HVI0xtp7sJg5us_ODA4kuUnzE5nLgbcrXpseTVoR0iSNYN-snpefTTxTn0k7S2R-Hm-lxU1Bq9OkJzyfoj_3_KWf8cOz7YHAXuFjhgzUwcapUPdLNY48AUgaU_K9po5LGWSQ_9_flgb0QdZX9LPgDsw8DLrxVUtIiYCj2relJz7_zwlmVfDigeZBrgi5gj1Rn39bWzaBjNzwoNnXQ9Tm1rFosP3nag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=I8-CrFUO66bkI_t0GWDdGWEzj5-BALcsf9E7Inkl7L5qil1bBtRMjBvFwFpEODHA88WZOE1FmTduj-XzLtzv7yozSnV-FG2zZkSparXeqU1anVP0z0WF41k4HVI0xtp7sJg5us_ODA4kuUnzE5nLgbcrXpseTVoR0iSNYN-snpefTTxTn0k7S2R-Hm-lxU1Bq9OkJzyfoj_3_KWf8cOz7YHAXuFjhgzUwcapUPdLNY48AUgaU_K9po5LGWSQ_9_flgb0QdZX9LPgDsw8DLrxVUtIiYCj2relJz7_zwlmVfDigeZBrgi5gj1Rn39bWzaBjNzwoNnXQ9Tm1rFosP3nag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت تلخ کودکان در‌ جنوب کشور‌ بدلیل قطعی مکرر و گسترده برق...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101716" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101715">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDw4XY26XQUFt38WAgUu35MwaI9FCOcG6_RGXgVlS0R5Fn7yqTKgsh2S3lg-xcCSHbkEHtbrmVNT_qj8IL_vIAV6-h0_GojXhZMBYK5VJuODDDJc3AIprCmFt0FfizshBWthl1itlA00YPpYYG9PGlZ2YjFl1auRbMR1Pjsevd0DRgwXKx21jXV7GYwymMQq8JUXVxulllhivLycDhI-MfHxWzrw54Y4ujv-58mIs-LaiN-p7Rlf_0h64JSShyn4M89qbUJHxqZbnPoegr1WyYhKfMiGIWsX5NapoeAXKCd0dnclwGBipGMRw0Z6R0taH17rjaYgOMSOkbtriQkQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
اوتامندی رسما از مسابقات ملی برای آرژانتین خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101715" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101714">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDYynUaGog3y0X0XqAq1hBpg0XnLxHDcK2UTqICFqgk7dz-KzW5a4xtFPsZvFBGO_y3iGiycUlV310ZxO1IdiA1eki2uiVMn13jyDYA9winx0tAUf8vRUJLuMm9vHnY9ijMuKzMWWzSQa3C6jd517pST3wj_goJV44z0OjSxECRerb04rd0Qd_rRhG6AFH5RY-h2KgRyrnwBe0g68pOzhNQzVK3O4e-J3GknMCc6crulgcWIUh7B4bZrQVcKIuHh9nn4CfJrglb3s1mf3e8lwpb4-hyNX1CZetjHoIFNgIttrtK9epiw78rvU4Fb3o2sXx44x7-iZeyVYtAj0wI9gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101714" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101713">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=CJnS88KVcZIN2aTjVxo8wFYrQ6PJUHJhipNTYFzLwjLm_W8_IPHFtA30LVjRVkmLCkzLnG-NVBUC0iKXPqnOiW84A4xSkP1RX6MakiljM2OaULmMX1CZrtaV93Lxa8Wjeo7Utq4VmoZ00lMeWfAs1J-TsAsmIi7jZcC69XGglQP7AbeZqaY7QIaFn7M836NVdEOWxnFKc3smVuO2xBGtYVfZKWMjQXGN3k6cGhwGvtSNJLsjWvMUvBACPeOxYz8zOsvnF3SzudHTdAS4sJdI-Y88k3HaaGOsVWZCIlhxAGhs5tLZA4CLcyg57PN9IVugtKJi85we5B5AQ9cwxnjFNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=CJnS88KVcZIN2aTjVxo8wFYrQ6PJUHJhipNTYFzLwjLm_W8_IPHFtA30LVjRVkmLCkzLnG-NVBUC0iKXPqnOiW84A4xSkP1RX6MakiljM2OaULmMX1CZrtaV93Lxa8Wjeo7Utq4VmoZ00lMeWfAs1J-TsAsmIi7jZcC69XGglQP7AbeZqaY7QIaFn7M836NVdEOWxnFKc3smVuO2xBGtYVfZKWMjQXGN3k6cGhwGvtSNJLsjWvMUvBACPeOxYz8zOsvnF3SzudHTdAS4sJdI-Y88k3HaaGOsVWZCIlhxAGhs5tLZA4CLcyg57PN9IVugtKJi85we5B5AQ9cwxnjFNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد! باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101713" target="_blank">📅 00:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101712">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=szuF91iU1P7r6b1c7vaUwfM15OETkeRazbBlht6gEAi9wCz9TB73ayM4OpfxXbM_WMrE2Ro0Jz0MsOKl-tED-L9OJz7qeoAWtejQd1JERlsE_F1DVEMeHkBg2rIfIM--riZ7kYmPzhjlUT0jG-Iv-kgjzQXFySpFXa6gwB4aNbbBfTJ8-hbQ_DsqzsCK3XeNMmOG9l53QGck8MfjvGaS4rOiZlI-6e-E3LMzzrJGQojzm3iYL1JaPMX6rYSCRRcADYilcF9cAV6EuwhyZOX54FYBO6c6_q9m8ZXA-4BiFqnxuBaGh2PHjlwmGL32YXlZRZY-Rxd057FgQaxiTgSKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=szuF91iU1P7r6b1c7vaUwfM15OETkeRazbBlht6gEAi9wCz9TB73ayM4OpfxXbM_WMrE2Ro0Jz0MsOKl-tED-L9OJz7qeoAWtejQd1JERlsE_F1DVEMeHkBg2rIfIM--riZ7kYmPzhjlUT0jG-Iv-kgjzQXFySpFXa6gwB4aNbbBfTJ8-hbQ_DsqzsCK3XeNMmOG9l53QGck8MfjvGaS4rOiZlI-6e-E3LMzzrJGQojzm3iYL1JaPMX6rYSCRRcADYilcF9cAV6EuwhyZOX54FYBO6c6_q9m8ZXA-4BiFqnxuBaGh2PHjlwmGL32YXlZRZY-Rxd057FgQaxiTgSKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
‼️
🇪🇸
یه فرد فلسطینی رفته وسط اسپانیایی هایی که قهرمانی تیم ملی کشورشون در جام جهانی رو جشن گرفتن، پرچم فلسطین رو بلند کرده و اسپانیایی ها هم پرچم رو میارن پایین و پاره میکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101712" target="_blank">📅 00:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101711">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3W9SfZHea_-bwu8MEt5TjWTLJerj0ox16RcAcxEdZVTMimxj2T84tsgs3ZeRSenvmX4jCKQHp7HZAkrlAbpbWc5InfU6GlTb2E2FuZ74-f32dEp4clbA3P-z07wzgrnYY6vPjrS1jmjHUXf-89e2ygGMRt2x_CkH88LNR-JJDU7z0os_11fxBTOKnpC4Uny0EkMo50YCuOBDwpOD1jCD4bCcrTxeYUm1EPdt4gOQ8gwH8DtfLxo9IQUew4Ik9WyzOfLnaVnNb9BTWzi-jcFaEVbijjIqmvOdBMw0HAqFi_MoLPQhI7TO5b6_8s92eEb9w-62zxHoyVjD5QLHcC9jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رامون آلوارز:
لیورپول قصد دارد وینیسیوس جونیور را در تابستان آینده پس از پایان قراردادش با رئال مادرید به عنوان بازیکن آزاد جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101711" target="_blank">📅 00:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101710">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY0GAX1GE585Ga_-sXNCMRUWO5YoP7Jpg1dV3RDru3BgUUFPfq7XaW9U_F_ZMfyDRFeLhhecO7WR3y-a5J2cKSzxzw0WhBrm7kfJRAQQP48bAsS5pJzaQTFErKkfVehm6PBsjFDB_yo3zA37cMUIAj3uBozPYm0B_JpxAu3NmETm5QKpQP-ZNCOTtZBEe-pSJDXegRBdHqkp7DG_RFgx_tDQUjsQqNVOal7eNN3y34lEUOgdmEQXeOjgJyv4KOY-0qv_hef9qv3eO_JCi9FYZd2HqbC5KVtYz0OlaHpw_-UZlpDlcNwyQ8OUSt3UgxKjNgexexDB6yTqPyIUBRo15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزشمندترین بازیکنای دنیا تو ترانسفرمارکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101710" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101709">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101709" target="_blank">📅 23:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101708">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101708" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101707">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101707" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101706">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2tRimWTdH1YUTWmFjyw7_wbB-IwpviqrpLd5WRF5WpubB1Hsi0tE_pHV5rasLZ2GF1tcI8GZ8BhicPV99AK0W1euXzbmyFzrpHGkR4QFfvjzZ-WKeqwfSZpr8jrSXPReCyQgFakzxZNl1lf47-8smxzUXELEFeXXBe5du2_miJDu7SzlAA5xUDECfpuYSrlouSRQXFeR7SZtF1CevcDx7SWGrLLXcmzXAnZ2F-kKNJNRlxXB_5t5PTGPAw0nYwpoXj3er7fAUSJ9-qJXn3bugfSLbLOQSfKn35PpFzTTNjKk2UBFINWkLKSvLsxkkPbz8DV7HS2Jbi6WfkYuCROkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا درباره اینکه چرا همه بازیکنان کارلو آنچلوتی رو دوست دارن:
از نظر تاکتیکی دقیقا میدونست باید چه کاری انجام بده، اما چیزی که واقعا اون رو خاص می‌کرد، توانایی بالاش در مدیریت آدم‌ها بود. همه رو کنار هم نگه می‌داشت. هیچ‌کس از نیمکت‌نشینی ناراضی نبود، چون با همه عادلانه رفتار میکرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101706" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101705">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH3V7p8ls12R3L2gGM5S0cZiZGeEzPRe7gqBAZ87jZ0G5ehAHKvn_wx_KDh47Qr7zT43YFmgdwvCOPA7Xi5S9RBZtn-prm7Ks8NTyqLIEK2cG3PxRDOC3b5eo-JF7DIiOEOHN-jBXOENwbn32F5oGTx_NkZHg1d7p4Nk6OCyQ-CRQ7R1VYIik4GHGLcm4S1TNsDxmOv01V-8eTAB0-JzSXOXXCr_lKayBY0lFmXprsr_2eCRUmmKzJqCYSSqkEp1yhLUNt8hA46PkICaVn4nw4NKdRr61rvqWP1JxIt98dikVIe0KnkTKIKuGupkZ8my-IeaMkwMcFW_02nBovpEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
به پرتغال هشدار داده شده بعد از خداحافظی رونالدو ممکنه بخش زیادی از توجه و درآمدش رو از دست بده. کارشناسان میگن فدراسیون باید از الان برای دوران بدون کریستیانو آماده بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101705" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101704">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101704" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101703">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101703" target="_blank">📅 22:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101702">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwwQiERcKpOA8yxBfXximaddC0TZh4Tqo9ca-Nx04bv5DDqtdcvAMoReNugauWVT76PKkkSzrozCSHLGDJIHTTh9H3K3r87MWlgoI27zhJzfWdKETGPIdxuCAgAY8_K0-040DO9WZqbNnbEWMhQtS6KNhLzsVn_aFZumNk8Obu-ZgJsYdHKb2ZMUyk-WauqBxhL59FocFDw9Yx5R6QzMHPsZ8voPFem62qvm5sfWZKC7fbDOGlXo0SUW-4kDncmnSuLsa-kSZLVeve0KDYj2zyk2KqemOhBJIpeh0P2pqhNcrVP_8cr0EiD2eg1VUyFD6nZ_mHu3l3rrjcFtVwtxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101702" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101701">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntcWXnJpKYRpwT4MkIr3gx40Nc0PFpZ6XPdvWQINqihnu3C2C5LT1BudJXvZb-l39Zwt0mdKcPaMN9Lyv5pE3YDTgPids2JKlJbN421LXMqXdUTHTnAAysZkaxUETAo8uX0bcC7eN44KveduoQsTFfS-mowwnm02RpOdfgCi5KQdRrhOvr4yBgjAv6H_c3iAqAeuvO4dsBqUg_ay59W7LrG0fz2yJ_btnCiIP-Gn7syBOzsA8oOSt_vO8dZqjdDlIsnMyCD-9ssSYWkd0DzkeUbz-9OuyBKNf2M90AhchSvdAdgjpx0j7rQb1BIaOHnUKT1bxEu8PuMTgwdRhyaQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا:
رئال مادرید شبیه یک تیم ملی بود؛ چون در هر پست، یکی از بهترین بازیکنان دنیا حضور داشت. هم‌تیمی بودن با کریستیانو رونالدو، بیل، بنزما، مودریچ، کاکا، کاسیاس، سرخیو راموس و په‌په واقعاً چیزی خاص و فراموش‌نشدنی بود. هیچ‌وقت کامل متوجه نشدم که برای بزرگ‌ترین باشگاه دنیا بازی میکنم، چون فقط داشتم از فوتبال لذت میبردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101701" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101700">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMKT1E0a0Y3Duj847s1aPi3yVZtsPKFyjw_yVL1aaX4MnqA9q5zXt74SZzOTc3WuUl2b-B43gWKsyl__wt6KTd7sQjg9IkLcQgaLVU99X7dUQF0SfNk_HSI84DEhd06LH3kD4Huz8sgHBwkRcTQRnrSCeYKZ6hfM_ZSVJfEQGT_deh-GRAc2h3EOwJA4-SC4Rw5PvPvdGBt4kSh2Hx4mv43u4VQ9SQiore4fovRHkZxbh5CSOzNlir3CZBKhUIdKSms7UxfgSYSsiYeFYFxV0HVAjLD2zTUKbXTNIkhHrV06I26pTwGeLVXENLHWLNLRZYrLW5mfCdAB5IHXmJBHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101700" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101699">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHg0s6K5RNVaXy1dubBKUBWZ9ZAxPR1itUcDAiIDU-3ssCVsXz3OkFN_7WrpR-X0J-N4Fcp-hsnLbXmqKnPBYk9KBKLlO5uIuF8H2hem7RuttT-S4a9J59uEasvvLG1ZxUAdo1UYDXVjvxatEewOVLuQ5fCKuVzFLtiLZdBnbDm4_P_uemgNN1zi3p2ndqMmygVRk6X3TO0StiaVDAXiO4ntLB2VlviUr6nN3N_ThMlmorJ-2IIp_fXG7-NRPQic-pMpohX4wauN5i_qG99i-rnMeYL2ufzebXiuLNeLiIFa26V4qj4qeu9V_9fWGRx1hBKC5CbgiSbKQ_4pAKFRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
فدراسیون فوتبال نروژ قصد دارد بعد از دخالت دونالد ترامپ در ماجرای فولارین بالوگون، یک شکایت رسمی به فیفا ارائه کند. این فدراسیون نمی‌خواهد این دخالت بدون عواقب باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101699" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101698">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOKXcMKfvwLwTBMUtBUeFDXeDE4mv2gpJdqxr8-LfjsHJyKez9Czexmjcz56kUrVj0h9eloQYIkwruMUFVqtKd7Yc54yKYK63JC6qax0H6xiZKolErnlK2kDWE5q5EIxzJ3LNEXD-RBPqQep_D35Rsow2YRQZOpV2xGITl7jNmtxAKSS9zH5S68LjBWyoipLryKqxW0vL0hW6p_wqmBXyyX5Dt9VnYWCRHXerZ27HSVV1Q0cI518fyMdFkv4bUO1vOfR-cVaTcIhAP2MpZ_9A2qnHj-iadLisp9CkiDhUTA8UOLhIMEX7EbPcUh3fOSnglMup97pqgPD6MTv2xsX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آنجلوتی پیشنهاد فدراسیون فوتبال ایتالیا برای هدایت کشورش را رد کرده و گفته که میخواد در برزیل بمونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101698" target="_blank">📅 20:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101697">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101697" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101696">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3wd4s4nAsjhVFAS2JS3kQmHmFE_Rfgg-_egwbPKvr2Yvi1wPJTFdfAcVNanMGfPvDbcOUEd9Pv7yWW75cHuZ5-bu6qrvpnMbg7WUWbvv-v4caX8nJBTqiiGiAHEQV0rUk9awcjlSCMMaYPZVoTZ4xFTC6UtVoozOSGdnc9izFxlIEh91eG-mBuilCRTPHCNbj9qMnZKI4WJ8s1w7dKERX5X7FoNpQhxxgKHrEC52fg3h14nBZLwuiBhpJchzdAG8YBZl1a7ocCxno1g8VExFffLyfl4WIbB1a_mfln2A0Bc4EoYav-K6QaPXy-XGiCt0U9TfldhTY8z6NpzDrYB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار در کنار بتموبیل و هلیکوپتر و جتش :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101696" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101695">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101695" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101694">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM1UU5RzVARCgNQZDDirfmvhh-_DDfDnVPw7jIxvV9xmckFZ4NuVCUac_gkJT1qmShlADm7lAy3QF5tGmub9Ouw2Dcf9UUA_LF8YjBMQTySzv-SR1-U6l3gMB1ppVAJXJbS5inewWpMQ65ZwHEoEzTHIYdTZutH4iwvxiBHFUl2Zc2Xg_nf032ZvO9BnAEES4Wc74gWWH4Dhnje8fFTeoyCyi2-uTNu0eVkW6pcU8dvByajP_AaMjWoL9Sc8_2whjqi1L2-o7cfVkgdjAAwgk8v6p8OtED_NUulrl4DLHu_i9KaAYf9MgWrSJAaBbYoa2GdfQrCQBI8FOCAXbZASUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
سامی مقبل خبرنگار معتبر BBC:
🔻
باشگاه آرسنال قصد داره پیشنهادی به ارزش 70 میلیون پوند برای جذب برونو گیمارش به نیوکاسل ارائه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101694" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101693">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101693" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101692">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2JS1pvlAfTi4FSYEZRcJhL6bkQyT_bt8cxBNXcMc7UU6D35jDRSjFVhr1yEK3oKNBnqBXgb0VC4cFTb3KqRD7LRloqKJYwNZVdsNZb5twcTRIO0rw3SAfb1W2Dq1h4-owQohs7JuLxcvBjp7ai5RfKsVzQ38DEHKSavgLgT52D04Ih16Irn9vGpxbNikKs_0KowWDgFiFL8OtZpTGA5eZfF_VGad4pbTUDNRjwwGArV8ZFZ5nMWKg6F40ECPqbCzZlnkwuPNQdWgzAjeDnejs3WwjL4nNk402CKpIokOO6a5mJFdi76epeBFhXBLH3Tv_lwGxvHtaW695LInJMQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی که همه رئالیا رو برد به سال 2013 و اون کیت معروف..
⚪️
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101692" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101691">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8AZBzTilQ7Wdn0bDKRhw4DK-0324OqXQOTyco-ZHk8joypmaffrqEZQkGnzusgmYNVDFHW1NshyIbZcZyGZamhSNFGLSUW9XQd4xVrxepf2jgaRIS8FnCC6uIWmyHPhcHCgUb4p1z_GywDQdihoSSWkSdYRoXdGk0UVGt43b_QK2ayy9TJVhgmBIymdZzcLZNNpKABCw0nEEMOsw56kLee-5I22lNeeRbQCdgNV1Z9M1pXQ8GjedbeuI6exFPOgGL8yAp-2gKEo6d1aoQeV3lJwn62EsmdYe0UbbFprBcGY_jMaTDGwnw7a_Tjk-M2ORJ-Xz_m_tQGIgQm8-oep_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو درباره پیوستن به اینتر میامی:
بی‌صبرانه منتظرم به لئو مسی کمک کنم؛ بازیکنی که یکی از بزرگ‌ترین بازیکنان تاریخ فوتبال است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101691" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101690">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4rsWQMdTDPh2crJjgBkrvaUbM0jtmga0wWmXyFOrsVPaJikeEY9UJD6I4iUL0VRAC9gzQ7wXdCA5-EyDRCY9iSd-zbYOpG_UwZP1MNBOSBFPsFYx2hEIPXxbwoBdCsIFdeP57RNb__mCtCJ9keu4WpC99WG1WKyqUakHQnZj5wJKCd2qW-mrkcNiRL4iJFkcZ-cSNAFPyVPApXf7zrQHz4FmNgRb6vYCuZ__jXffR0h6Bmj48CTsW_WgEMFdGk8rv3Zxwbm88ha_SDKynXnlV820TT1keQoCtpwJacWRFrHt290r2WQxVWuSmhQgwrJtb-jeNpVsXx9DRCdEbjbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
فوت‌مرتکاتو: پاتریک‌ویرا اسطوره فوتبال جهان بزودی سرمربی تیم‌ملی سنگال می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101690" target="_blank">📅 20:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101689">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101689" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101688">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5zrh-93QaoOfsjoArYdy1uzzSEU1iftEtDLYl2Mvk3pNw26vpsRvjqfpU-EmIF9k3a2e_xnKd9zgZAhFvp5UWbFAI2DjxKbbnBoZ3X1EOYFuzbk6T8SsSQuEfCkz3r3KnOoCxkVIgF4muLZm9AnsMzIrOFqc9kle1SfhswRnV6asCzQDaA7cvptpDvKyM9DUoI23rAxzq1-YUwd66hDEn8jSYIbZbVAdAjHSigW9UBGO_zaHsfnNdMPHQj8hBFd3cR0KB_YWCO-8vWHz_pWqsP9cum4rdNMjvfHRCi2-ThyLKg-t3404y0pmV40NPeWm6Ej1oQ_FE8eWP1iGgKTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله کارت زرد به من نشان داد. من مطمئنم که این فقط به این دلیل بود که مسی آنجا حضور داشت. ما 2 بر 0 جلو بودیم، بنابراین احساس می‌کردم که داور فکر می‌کرد:  بیایید کمی به مسی و آرژانتین کمک کنیم.'"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101688" target="_blank">📅 19:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101687">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
فوووری و رسمی؛ تریلر FC 27 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101687" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101686">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEAmRjWaspdOmK7kunyDZ19wz5y_1jSgSZZo4u5w8cVZUgRGLAa4DBRCQYf-3OpaQ0fKTcC1RHvzj3aN2gBu5cxIhQxuIQ_HdQhLSjA7K4pIra1kbv3dvAjC2Bt2MlwC285YlA79uR-yt5tnvjd6B1T73c3bffRbEvAkTuhyJ741jP0XfRbPtxhPm9j7XhAmtIGkn46yn2ISwHO55BQQlcrKjLpJQbaGqPkvEEsV6zN0cuLRhRDwaUOkHam6Xi3cscU263RIWgtc2Rw9WOj4afVmAqmFUqhAyDEDPiJxoRboayDPMoRLSMZ-9gWzqRlW8gmsUi0bEx9wurqrKgWeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101686" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101685">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTeiqp4AmxG_xxm5rCx9tdmuk2D_Rep_1aMq9Jfz-SQ3yiPZo3DrFpLJdiHrVN3xtbXNugz9TRWdayejw_cHA6PxpXILwSKvCimmaAeF-IaRXKQw64CdCBcF9gvYz3TNYEZerSJKsWvt55oPen4hY-q3gRBih5kksUzXPD3CUKRVG-4m9doClApEeZGe41896A-kfVrk6eBO07XeiTiSpc-5SOJZuDzQ73X-fIs5-D8F5hxAgPU6ye1DbNewHT9LdInEVEek5viClDmhM4dqpHRqf6GLOkSkvHWO8Rxbe59hYjZQkVDXIeZ-d2u8UaOTn666QSzDIDyqeDa3RJJ0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101685" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101684">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2wInQZlJWHqUZHm7eGYuz5JvSjeG01WSmapSUWOIMJWRg8QWq9f8jtkEmRena4uq6gpgae-wXguKTbXxxqoLwQMRrPrExjZgSMc9Kyd_NKrLdl5z-mSDt5ERcOsSJlJX_qVnBYD7ZXTXLU3Bgi-DJYOxHPJpFtcVq36NTpYXvqSjRq3f7IiLJipG-f5VvOlBXBpdKdCByVpW-hdl09--81cJYPMkklWVZdwA-JJ9t2YA5hQnvHyJo05SnHD_F_YU4NGwaJWfmvdZOqmILerSvg48rsWZ8lXiKEB1W02SNOGO8X0xlkp-xIGM3iIKtbuj4qFJ1kAeKms8odbpJl_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسمیرو رویاهای همتونو داره زندگی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/101684" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101683">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp8Q2WMOMg7kqEXm43zLLDtv0jSRuMf0CihpPuIOtuAaRaLvyRbitvUUUUFTCe6ZesUesItTBDDwNc48xwr7rIi0IXUy_d3PjW1HdAUgcOX1PV9SeMFYNmV8l7BzpWafG5yu3jpfEIIe_wbfKfDMrcWDmXi9nbBZ8kNH5OnbhfeAJL6KmXiUYUn2cPAARCOZxAZdBt0xaUS0_EFIMV4UxcKL0aF4YbwY8h3h6nFN2cjmHUEzrxk2p5pSH0PfHiLDfX-w3212B9noY6ZmI7y7Nnz5SSAoE3aa6LBf1FMQ5a9k4rvtWK4YbCgJomjE7pNtJBy-Eki-jVGa9kov1ADnpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمیییییی
: قرارداد لوکا مودریچ با میلان به مدت یک‌فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101683" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101682">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVTOjhTjr3qKipc0YlSgDx2Fx0PhmT93e-LIxHMi8cCnetKaUur_fFa4wXV9RZX0BTQb0KjggRPE1rrltTlL2yRDpdlQGFX_p1Hytmf-dwl1_8WRoCVPMPbPOmuJjvHpz14PRVri2_zYWjepBAkeIqUIEkK5kcAIrlChz7BDzV5xjDu08hZu_XjwSg8255g9w-dLy3_m-5q3L7dKyJiwSH6BP_oQ3b4T2O5ZvSp7D1uDGxlc0JhHXhMny-OiDf1Ix3ercZFfbQCT05S2LChMWWYx4d7u1cuX_BgKAEUNqTDrlqC2ZE_HRp420rUMoB2-XW60IjxOtdXh5xT9ce77Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101682" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101681">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=jbf4slB-WE9YnFUtCKkUo5c8j8H-_M5iQly2h_kOrG2n3d2HwnQ2lF3nASGsS-ln96b2rD1SlCO37ElxSjH1zp0EANd4zkis52LTtxV6hrcNgghIf3Oj4mqLp1TmZg44fWneJ4mfoK5X9ow_Ou2QmL1VBcT2IH-rtklvyJhxKl0mjM_WnkqsJXXgkjb9e0U4CYAlD5RQF74X_GNVAbZKXVp4zQsPFaZJ8LK1ODsntf47-jQ9NEiSMJwlD774obevYRVa32thGTb8zuunrrAlus3xHN6ipANGhSLHfQ7kamcpM3HN5lrhOtUmW7MfwURkWZUcbHW_QHUSgemJLZlzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=jbf4slB-WE9YnFUtCKkUo5c8j8H-_M5iQly2h_kOrG2n3d2HwnQ2lF3nASGsS-ln96b2rD1SlCO37ElxSjH1zp0EANd4zkis52LTtxV6hrcNgghIf3Oj4mqLp1TmZg44fWneJ4mfoK5X9ow_Ou2QmL1VBcT2IH-rtklvyJhxKl0mjM_WnkqsJXXgkjb9e0U4CYAlD5RQF74X_GNVAbZKXVp4zQsPFaZJ8LK1ODsntf47-jQ9NEiSMJwlD774obevYRVa32thGTb8zuunrrAlus3xHN6ipANGhSLHfQ7kamcpM3HN5lrhOtUmW7MfwURkWZUcbHW_QHUSgemJLZlzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سوال: آیا مسی بهترین بازیکن تاریخ است؟
🇮🇱
نتانیاهو: باید بگویم، در کنار پله. اما در دوران ما و در دهه‌های اخیر قطعا مسی. او چند سال پیش به اسرائیل سفر کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101681" target="_blank">📅 19:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101680">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
فوووری ترامپ: من در حال بررسی یک حمله گسترده هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام داده‌ایم. به تصمیم‌گیری نزدیک شده‌ام. ما برای انجام آن کاملاً آماده هستیم.
اگر از اسرائیل بخواهم، ظرف دو دقیقه به این عملیات ملحق خواهد شد. ایران به اندازه کافی احساس درد نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101680" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101679">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=h23o_Rb1wRdOIqY5LzJbYpiivR86hWGCT-xhQk9PPzdSvkkG5tJuV_sxV-J0LwCkqs1_ZJh8EMMi95CkZP1M7K-dqlNRgMndwIN7AWiOsSVYpGZ7It2tK6DB9NgP1T8GhVHlz_m0_YFBtlaZNnbB9zAlNwibEgLdtO7m19LIxWHRZiRZTbX4boGKBXLle1bZS1020AYJF3ap_UNhsD4LQPXK8iotzKRs9qepsRlpTLXHkWr_m7ZGhz_F7do-FWgLJSqzEas9UuvfAYcZofk_swLxYMJBOMpQGhMHmNBQuYK6Jw163zTWQyQ7Zp-blrbvHRC3ECMGetKtnxkLxYgoVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=h23o_Rb1wRdOIqY5LzJbYpiivR86hWGCT-xhQk9PPzdSvkkG5tJuV_sxV-J0LwCkqs1_ZJh8EMMi95CkZP1M7K-dqlNRgMndwIN7AWiOsSVYpGZ7It2tK6DB9NgP1T8GhVHlz_m0_YFBtlaZNnbB9zAlNwibEgLdtO7m19LIxWHRZiRZTbX4boGKBXLle1bZS1020AYJF3ap_UNhsD4LQPXK8iotzKRs9qepsRlpTLXHkWr_m7ZGhz_F7do-FWgLJSqzEas9UuvfAYcZofk_swLxYMJBOMpQGhMHmNBQuYK6Jw163zTWQyQ7Zp-blrbvHRC3ECMGetKtnxkLxYgoVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تنها جمله درست گفته شده از صداوسیما در سال جاری خطاب به امیرحسین ثابتی: ‏مگه تنگه هرمز مال ننت بوده که بدیم بره:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101679" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101677">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXPVK0t04VUwlQualOU7-F4PpUw02ZXPhFkY0byyg4Plk_QqvsT2iQZB6UPh8ZL3JKOM3axHARW9JxfpPOL5ei1Iy00HN4qRurWoYmWwrwehszVPapmLq9zJEunyG7N7L7WjR-213KhxXDNp15VncTsfghKc7yn40kkq0CJGAJc7TgugNvle35xB48MSQEccZng_qk3E2nJiBS8pN3aPq3qR7ug4lbQchxwfZHdhRVjIEilBHXUGkwhNWwEMqALtO3BwvBagNjA9Hp9os1WnVPZSPM2iYONHWx__HexmgrH3JYQOXww3TwhPBWwGyqtzfkJ5DK768i5zBdP8qE3vkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvt7e6_Sxf8Bwl-AJ0gjNttL-r1ik7h6tNEWzpyrAPBHHXdgq9zsnFMbRwqF5PiWVLGU0Efz5z5Iv7lbZaHU6PvvyJFPfk9A-4TNJNVtFlJ8oPyJJWbBYKkxle1btgfIGHN-vpnwKEb65hFw4c3qNwtECxICcFzzr0hy8nKI0_N67cuFo09HqQrkgYGHqJVPz48YDE2nt0yf0ihhIJefbVxaTtkbNOa5KE83hxtBc_GYSPRBv4shPCsyxup6EiTzEDJxQWStU_hnJWhyehCMIzAIvT0rXdcmAcIFW6DdIvNcuuXZTrhrOofQkssdC1d2m-JrM4TOo5AtwgPjt32CbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تبلیغات جورجینا واسه برند خودش Mimoa
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101677" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101676">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2FbN9NZDFywWqC18D4V_PBzJDM1bVr5w6FbThio7klsE0ZCg8k93A0mpUpFc-Da__F1_AbE8hNqpzl0MReYXBKfsyGVVGorn4hU_LuQIgjOWaeEFaIp2UjsUaJijZpdpAd_h1ppveo8nJ98JKrOt4BIZ4EwS_z_967gSY8x41Bboj9KdWhGeSjiUPm4WKIGhTuLbCWrGAD2nwVg__88h6CrgnGIjdynf1wWtSqLfBD6DFs4dveJBZCJqp589v7mG9fO5DY4mCu66Ro-gnZZAcUPd-DycCwkoFEluya6g5agdFRHOPbx7dcR7emQ1pgheHNxHab7Cd3j-oliDzjt6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
منتخب بازیکنان آزاد فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101676" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101675">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d6746099.mp4?token=fYyHXVoXdSqrZDfiORzSpKMWZsDi4npCQzi9bhKjBDkfAdyjqWlrFzAWGYDzv7t8tkYkrp-evmart-jKq6COgZ2Ly1oIDY-T2uLLruKvavFhb7UtXYjzpeDzYOOb_Ox9eH5KGcr3TIBCEq05Tm2L7Nh43G0UEGgtI7hpwA1hK1jZv80TwiwAu4usF-i7mgbukHaFSsSAqBc6oc2yiwFa31-vsVPkYDfjUprOGYVXMnWWGNpY_X5rKDiKg-9O3F3pUcnxwtqE4oV3qM5MwSUbR5oHyJfOTxftNCY3Cu370Zt_r7jeUoocukmxPeg0_G3s45vxsBQECaY_8rGU9LwYs08FCyawM2ktAkxDHNESwyZUNkTQTkvkKHy5BYwqu3DTZz4iQ3Drl85EoZRn2JXFermFQm_Lqfnl96uB-1b7Caw3sZjv_iY6Ic_eJzRWKyNmk6yND3KRl0Z2xXt5nT1i2j9-x625swOLju1tCJkhHsaMDXD_drrW0onb5l4_nlUtzlSTqXpfWTRvW_yO776-U67nvEUm_eepLyZJ-H-5aNx_faKssSf7j5f9OLs4GFGpcEj-jN5uYypZlN_V5QjDIkKA-WM_5nvZIAjxO4Y0rjaigBpLkmpYIckyOqnt5Pb8oES-3xKv3gA2hXhaxo6PQY8vf8jtwu8rsPbZwt0Qzto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d6746099.mp4?token=fYyHXVoXdSqrZDfiORzSpKMWZsDi4npCQzi9bhKjBDkfAdyjqWlrFzAWGYDzv7t8tkYkrp-evmart-jKq6COgZ2Ly1oIDY-T2uLLruKvavFhb7UtXYjzpeDzYOOb_Ox9eH5KGcr3TIBCEq05Tm2L7Nh43G0UEGgtI7hpwA1hK1jZv80TwiwAu4usF-i7mgbukHaFSsSAqBc6oc2yiwFa31-vsVPkYDfjUprOGYVXMnWWGNpY_X5rKDiKg-9O3F3pUcnxwtqE4oV3qM5MwSUbR5oHyJfOTxftNCY3Cu370Zt_r7jeUoocukmxPeg0_G3s45vxsBQECaY_8rGU9LwYs08FCyawM2ktAkxDHNESwyZUNkTQTkvkKHy5BYwqu3DTZz4iQ3Drl85EoZRn2JXFermFQm_Lqfnl96uB-1b7Caw3sZjv_iY6Ic_eJzRWKyNmk6yND3KRl0Z2xXt5nT1i2j9-x625swOLju1tCJkhHsaMDXD_drrW0onb5l4_nlUtzlSTqXpfWTRvW_yO776-U67nvEUm_eepLyZJ-H-5aNx_faKssSf7j5f9OLs4GFGpcEj-jN5uYypZlN_V5QjDIkKA-WM_5nvZIAjxO4Y0rjaigBpLkmpYIckyOqnt5Pb8oES-3xKv3gA2hXhaxo6PQY8vf8jtwu8rsPbZwt0Qzto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ویرجیل فن‌دایک مقابل بازیکنان بزرگ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101675" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101674">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=YptV7Dgyroy-H10CPSvn7XwKjcQZWJLaiKoQoTBa5VyF-7mH50evgqBumFqZPtCAc1q4YKCeFLqNOZ8-s39TjULjrnaioQ9cB4pXVb9ilyhNDK-pHIcqkl-0uNd3PmiU3aztxVJ983P4Mv0v6PfkQeA4iXPYDm2n31lqiI-i8iFb_zj42dhhN78WP5JZ80TQNv_CQ4k-GvpgCfqD_E9hpHcADgI3yoIJ7NdcvvBlZj_F0GIKYOGG5mfMRVh3nnanaXIKmIwxhc6U3fmElhAU2VdtBS_Y1lwqAK9Grhc0KgHLmLZ02IfgnEzdOF9Hdosio5judoLk69gYJfvRuDFP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=YptV7Dgyroy-H10CPSvn7XwKjcQZWJLaiKoQoTBa5VyF-7mH50evgqBumFqZPtCAc1q4YKCeFLqNOZ8-s39TjULjrnaioQ9cB4pXVb9ilyhNDK-pHIcqkl-0uNd3PmiU3aztxVJ983P4Mv0v6PfkQeA4iXPYDm2n31lqiI-i8iFb_zj42dhhN78WP5JZ80TQNv_CQ4k-GvpgCfqD_E9hpHcADgI3yoIJ7NdcvvBlZj_F0GIKYOGG5mfMRVh3nnanaXIKmIwxhc6U3fmElhAU2VdtBS_Y1lwqAK9Grhc0KgHLmLZ02IfgnEzdOF9Hdosio5judoLk69gYJfvRuDFP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101674" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101673">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RKhy0f0ISd0OtKy0awvUedsoAniV-Pt9RbwQq8hgLiT5NIgley7Z9r2hIKpb5-qD0aNmpXCP3oevAK67XnIGs3457jPQYRbo24qc279JPu-_1hSOq0pLsO1MndqYmw1gGdEwDFHwAtHvUcOpSsDB1JqkLVofpoDFo9GyORKHYOYAhj4MZ1yCSTfdnFkhLF81-_YWy2qs_QpGNUFxeGfTjMcY8pkiivOrJ9XAlaj9LxVJN_jJrhU8v7Wb4hlN5TkRK6jPJrqRTxN8qybt1cfuFuojPdpuB3RLyxur_MIQ8NGHAc_JwXcoo1YKKTlypgrcaIB02j92p_HxipGzk3hQ6QPgO2GWp08Nyus1lZHANOUe5vgvF_Fv-dT5kpNe3UtfZSpd1l4dAuZISQOfs5RZcrWvn8i8jW16cbDF8ZwiMLJy3Xz9dkO3fgUZqwv7ylxBUS0LNiRPFYr_F-W8udw8gWQzb-CC7KshCS5E2LujQOKq8XjoBz2QZxgbavSKJuKJvl-2CDXdFmLckwfmIrEElRBrJOziOVyhqm9uEIBYmbZBprnA9u7qBvzLDXh4duk_PqBFHkwpC-_5PXF3p507Mmceqf4mINGPmRlMEVrkYxU6YrH42R3nblyTl_Jl28OIE02iykbAB9GYykG4108qhqjw7cfFWSMIaAjDTzbqA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RKhy0f0ISd0OtKy0awvUedsoAniV-Pt9RbwQq8hgLiT5NIgley7Z9r2hIKpb5-qD0aNmpXCP3oevAK67XnIGs3457jPQYRbo24qc279JPu-_1hSOq0pLsO1MndqYmw1gGdEwDFHwAtHvUcOpSsDB1JqkLVofpoDFo9GyORKHYOYAhj4MZ1yCSTfdnFkhLF81-_YWy2qs_QpGNUFxeGfTjMcY8pkiivOrJ9XAlaj9LxVJN_jJrhU8v7Wb4hlN5TkRK6jPJrqRTxN8qybt1cfuFuojPdpuB3RLyxur_MIQ8NGHAc_JwXcoo1YKKTlypgrcaIB02j92p_HxipGzk3hQ6QPgO2GWp08Nyus1lZHANOUe5vgvF_Fv-dT5kpNe3UtfZSpd1l4dAuZISQOfs5RZcrWvn8i8jW16cbDF8ZwiMLJy3Xz9dkO3fgUZqwv7ylxBUS0LNiRPFYr_F-W8udw8gWQzb-CC7KshCS5E2LujQOKq8XjoBz2QZxgbavSKJuKJvl-2CDXdFmLckwfmIrEElRBrJOziOVyhqm9uEIBYmbZBprnA9u7qBvzLDXh4duk_PqBFHkwpC-_5PXF3p507Mmceqf4mINGPmRlMEVrkYxU6YrH42R3nblyTl_Jl28OIE02iykbAB9GYykG4108qhqjw7cfFWSMIaAjDTzbqA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایت عادل فردوسی پور از الکس فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101673" target="_blank">📅 18:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101672">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJZDwPDS-Z2gOP_gZvp2PHISaKym98al7xY9Qpfn6V0eYH4gb4KjWVHl3lGJgAoY0LCdLX25ysBVHE5XNhrJlt6qXvNiLJYbOZEl2mfQGATNUl4JiP5gz_FkcIZgshBxr8Qzjw7hVhILbETubWCjXqFM7GVTM8CdJhPSIf3tXlXha7VNVTu6cWVy8xXhIoeefNlaOVn0VZfN83fXdCW6dEKqPbGGJ8p_cUAsSsQuMDTEDQ7W8uxSCM5I4DHJP4-uXKl4nuOu6XwXmGKVLIbRiMReSh0vxFU8OjzkDs_pCHptUgCqZBbDqjTOwO-G329_hdw0ZRs8KzNrxYMdmKS9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180
؛ باشگاه نساجی مازندران با ارائه پیشنهادی خواستار جذب محمد خلیفه به صورت قرضی به مدت نیم فصل از استقلال شد. این درخواست از سوی مجتبی‌حسینی به شهاب‌زندی مدیرعامل این تیم منتقل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101672" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101671">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815514f088.mp4?token=O0JZ85sjh_zBs9BwDh1we-8jsdwdr3Nl7I93xX9AC5XPx1noGk-IAGX08h9p6FI5xuJhHwDUa73B3eddVsrXuKkBY6M5Zy7KqEHjYVVAj3nMMjzJKIG8HPScillLq4l6KNAQDnuSa5ibfNSz5QpuBbREqpahkazalgj-xMP9YvA3RGVlAz3xBBjnc1mNigjm6zUaIwjHEyZbR8zrmQuv5PZbm6l77VtU5m4k2MuT0IYrtlg021fQUUn9--NnAIsv1RhedLyceD0CaDXQOBGEjxPF41qax5u8mq1CUeoMv2m8hK7GM_qZ-6K3dm1l-jD7GFxOo8Yv8UOGptmdUZYqgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815514f088.mp4?token=O0JZ85sjh_zBs9BwDh1we-8jsdwdr3Nl7I93xX9AC5XPx1noGk-IAGX08h9p6FI5xuJhHwDUa73B3eddVsrXuKkBY6M5Zy7KqEHjYVVAj3nMMjzJKIG8HPScillLq4l6KNAQDnuSa5ibfNSz5QpuBbREqpahkazalgj-xMP9YvA3RGVlAz3xBBjnc1mNigjm6zUaIwjHEyZbR8zrmQuv5PZbm6l77VtU5m4k2MuT0IYrtlg021fQUUn9--NnAIsv1RhedLyceD0CaDXQOBGEjxPF41qax5u8mq1CUeoMv2m8hK7GM_qZ-6K3dm1l-jD7GFxOo8Yv8UOGptmdUZYqgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مارک کوکوریا موهای بلندش را فقط به خاطر استایلش نگه نداشته است. پسر بزرگ او، «ماتئو»، مبتلا به اوتیسم است و در تشخیص چهره‌ها مشکل دارد. کوکوریا می‌گوید موهای بلندش کمک میکند پسرش هنگام تماشای مسابقه بتواند او را راحت‌تر بین ۲۲ بازیکن پیدا کند. به همین دلیل هم قصد ندارد موهایش را کوتاه کند؛ چون برای پسرش فقط یک مدل مو نیست، بلکه نشانه‌ای است که باعث می‌شود پدرش را گم نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101671" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_MogopVP4cpKx1OL8vx1-kHzZBSHSR24QAWA59hh1PrHFda9TTovFsADwv6eELsO86DqmbZ2wD1Nn37F00R2iQ8qynX3t9bgDZgmYVnbXaTqOdj1JqrTMhYQ6WFpNoARSm62gJ9WtfG2wrKkFM6uY-hVN3kbMPULxCkM7X2aDT8mFRdg7kRdtLND10w89P7nBaEm2PlOL4JFDQzy1q59SG-3JgzLvhmmqa8I6101k87Cr_owrSiOx_bKnA9bC1nLR7MoS3jKdnVzilkbI8EHyMzk7BWBDu2UdoE7eZ3PBDGUoxADTMjLdWYaxDm6dsIFqnEJppAPycFi3_MbUHrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GF4z8iFFczzFUtmM6X7cRKflJDw-nhyyC2H9NNypS4d_mDNXlz3zORMyg9tS987F3CmO6kC4xv7xEU_tD-xi2jK2TW75fviG38w2xO3GCJc5HiGlKYKWZA9Ui-ON_3y3SgvjpX1whMmDMFzl1K70TTcjo3IbnB7iZLoHYgaqJjNFp8GUU_wAAy2st4PzU11lsh6whZPI7KHOdV1WlgN6l-jpuOX4DDfhcOA8I34ZTNawBYKia8_3dymehBViiN8uYvkWDf2x94xgcVOhzMkAHxqPWaNn4ww4mZSGrfedYlnd0Ruk3rAdAUxQNLDgH2DIpfcRQUYEmf_6zewxkrHo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWhfxTTaptYPYVSwvdG3Wl4Xbdzjr82aGZpD2AXBFmrL1yxzfWkgCqr3rC99TTSvJ2u5F9dzesnkv__zLcMKTSN75VxTjCp6UayHmsee15Zqd6H0_wMXPPIK8MbBMREpkCC2eW2R3NTjvq91lHnEQ_Px_oB_1EtQIcOz_rs-0tRwrbkd0wZNOeTf6uUGYGlaGuwiHL1ATFiIpVnySevQDgoiF2AuEKOs0S7Z-70RIL80vzvDUlduDg4npKYe6jJjkOR-LNiE_PrjGqTgavRS5SCZ9xHvjMDDc-wzhg98uIDjw86Toe81dGO9cekqgnZF1KrNPlEGx8BAvonwFsszVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رونمایی الهلال عربستان از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101668" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101667">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLBlIUd3Rm4LvpSqt9lWTU7l6Y1xG9RLA67zNlV7F0aob-DiU5euKuhKdjYvbq1YdQm1_4_AOucoJMstRs0rf70FAvluwWi5pn4ExKzbrJ_Xz97qy1WA1rpDC8PPtgdCzT0ROm2E4V44mWJgIaGxxGZciA7F2udAYnfaewOTohCoXn4m3nWJxSw9nJKTA-DGOSPD5w3TAu90B93ilJuh5o67EFEdMwT1KA1u2egYfUQ1YIJLoU2W2X1ix2zr7M6Q1TqN0ftMsRSPZ-yvF-CCOMKbqrshT5WCTFgoVS7pwsU-T_-uSKs_OI6gd9sEvZ1SIaDtop0tG4w6-W9YUNQmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
جلد نهایی بازی FC27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101667" target="_blank">📅 18:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101666">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=nKRKXwaaK1aSZfi19MU5Ct9nAIuG0vK_4oWgYh9jLQUqTOsUaQhbB9vKoLflrttGUbvER4SxJAmBJfsu-tbNsRfSREcoIl_rW_flvklqU0YJ16M7CzZnCkHZ_uKe60B-nFtuNbJtl6SUfAoSrYBDexWvFG9reGlyl3Aj42il15XFOkWoKGD9P6DvRjMxlcUT_tLW1wBHl5D-eOa9gFjHGcdGwqZDJetmH4_YTdGA4GdlRM-8lvqtW__ay4LGTvsGpsj9KisgKaHRl8vrcWpPG34S_W4Nqlx2uZzyFcqoeQmZM0l58u1z7wEjP3fVUy1XhvV2fPrgULw8dd2i0fVZbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=nKRKXwaaK1aSZfi19MU5Ct9nAIuG0vK_4oWgYh9jLQUqTOsUaQhbB9vKoLflrttGUbvER4SxJAmBJfsu-tbNsRfSREcoIl_rW_flvklqU0YJ16M7CzZnCkHZ_uKe60B-nFtuNbJtl6SUfAoSrYBDexWvFG9reGlyl3Aj42il15XFOkWoKGD9P6DvRjMxlcUT_tLW1wBHl5D-eOa9gFjHGcdGwqZDJetmH4_YTdGA4GdlRM-8lvqtW__ay4LGTvsGpsj9KisgKaHRl8vrcWpPG34S_W4Nqlx2uZzyFcqoeQmZM0l58u1z7wEjP3fVUy1XhvV2fPrgULw8dd2i0fVZbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔵
خاطره قایدی از اولین بازی در استقلال: جمله‌ای که بعد چند سال هنوز از ذهن قایدی پاک نشده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101666" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101665">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=gIsVdv5NDr6W3uVKprfHfpZiFiJHuZa8PDAS--WBiyuZ8pnANKgJV4VfCpxhSbhhYrGjbDCPBLdY0hJINzTQb82OKuJNXngJI2_MzBr5YwHmj6Rb-gqDdOACInJ0naC2AT8CeP6t-9lTeykrFEopfR2jdQECFNGFKqUwVjNyyKKEAisi6e65fcKJNNrRakinkdmdWamOjBsr9Yc_WlpydLcrTAFeMgmwsf_L1WQJAiq1fIkHCbJJtu9V3EVQVeOMGD-ueRkPhG1qu8wPMjJwfd4vAJh5gsFU8RCAwqq0heWwao8rVJG-XmwrmTRebIVJvY7Hjzc66HifF_CnPYV2WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=gIsVdv5NDr6W3uVKprfHfpZiFiJHuZa8PDAS--WBiyuZ8pnANKgJV4VfCpxhSbhhYrGjbDCPBLdY0hJINzTQb82OKuJNXngJI2_MzBr5YwHmj6Rb-gqDdOACInJ0naC2AT8CeP6t-9lTeykrFEopfR2jdQECFNGFKqUwVjNyyKKEAisi6e65fcKJNNrRakinkdmdWamOjBsr9Yc_WlpydLcrTAFeMgmwsf_L1WQJAiq1fIkHCbJJtu9V3EVQVeOMGD-ueRkPhG1qu8wPMjJwfd4vAJh5gsFU8RCAwqq0heWwao8rVJG-XmwrmTRebIVJvY7Hjzc66HifF_CnPYV2WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های چندی‌پیش مهدی‌مهدوی‌کیا اسطوره فوتبال ایران درباره تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101665" target="_blank">📅 17:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101664">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enuaRayzOEWneO3VeJXap2e8AzEBCHCRSTDRL3k49noyyU8HU0hBl7X8a-k_0AEdOM_I2FRWjfKMdcoCSbVNiJd4WYqEk19w9LgB2F2k84lV5nQNlSmAlrjNPa6vbAdhDHteF0TXd1FCSkkQphggsYUVAjjI4XeQRRZ0FVrGyrxkU6wuLCKx_SxjHnb4tARbEJMvua8z4FKU73IgnrhEhtDfS4gmsiOHGcn8O5Fumq5hnWaFExeNZb9_LGh35GuNbTTMJPsneySOStJ28-9IF5yd_LadeytBaSJNefCMIg5v6YRtJjWvBPOen253Nk4f-CpN975o11r4Uql9Z4qwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گارناچو رسماً به صورت قرضی با بند خرید اجباری به استون ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101664" target="_blank">📅 17:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101663">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgc-ez6_gObmO3BRIWpUKDOmu8gFvcnzEkK7V2NYxX64YJwItCtigIz8RVqAi6jeZoWRg7cAi3KZU5AuovNJxLIt3K8tszA9ep-cQccV8dHFz_eDl2dUmIODkCd9Z10GMfejac34MMOPv6AfLAU20DhGupXbhyOlyspk2MjpNTxY1n8uz-uEPfYNDtPaVNqYHvf2zIi5jnhrRn5kT1ZuWiYxRY7l3fXg9pCv9DzRRx7WsCWZ4DzCuI_hlC7n4IdT1z5JeZdrmYyCUga9-2-5EewQxvbeWxXOSi8sItffTgGez28YxvOVlYBz6nAFhe330NY_eSKujD7cFpGjWEbu1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101663" target="_blank">📅 17:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101662">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=ckqtiezn0fSoly-Rq61DHpSXoiqvAdYp9OgOC50HynRfDmVc5reGkgBDnDvJf4VNrohEHD9LDNthakTcWnyETig5XxVaA9xtonSmVbRF4EFZy3UEX4eTPJvTVpmA9hJWtp-h1ikTxdD58dV_lZt7vhw_Ml9rGmQswMnj8EohJzLDPXxbvyvb9StI2JxZL0uF-ab50fZ1fQgwXq_VsLa6VFwWJyqyApANiITxFQWibYwqa1ujvDE-qRCkjFNLnDTNphJpKegmgib0cHqsoHFc9RczcBvvtTLpT90Xg7ZH3YmZabo3_PjsOZSP9KIIL-Ld_lYaRG6DMHzOjlG-vKJWmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=ckqtiezn0fSoly-Rq61DHpSXoiqvAdYp9OgOC50HynRfDmVc5reGkgBDnDvJf4VNrohEHD9LDNthakTcWnyETig5XxVaA9xtonSmVbRF4EFZy3UEX4eTPJvTVpmA9hJWtp-h1ikTxdD58dV_lZt7vhw_Ml9rGmQswMnj8EohJzLDPXxbvyvb9StI2JxZL0uF-ab50fZ1fQgwXq_VsLa6VFwWJyqyApANiITxFQWibYwqa1ujvDE-qRCkjFNLnDTNphJpKegmgib0cHqsoHFc9RczcBvvtTLpT90Xg7ZH3YmZabo3_PjsOZSP9KIIL-Ld_lYaRG6DMHzOjlG-vKJWmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمایت سید جلال و قیاسی از علی دایی و کنایه‌شان به بیرانوند: بعضی‌ها اصلا نمیدونن احترام چیه، هیچی دیگه سَر جاش نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101662" target="_blank">📅 16:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101661">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=OwkPk5ogH_fdSHMXtykUbwEjSVe_cUgOalmhyJBzwsCSE1E-0JsFRROrxscc7F59tWXfvUxvcimqI6benvyrcCL0Ujm001Ozx01xlbD94q-gTqzHXNTPn3NfCyQ31rcljsbLrmijB2ZEDOH9IaJtP5iz-j3OkesQlsUwJNJac4EDKVSFOlH03SbryyPNgEy5bPUpfdKnCHd9BSCOD3WXtbPbecqu2-rkFOM5QWyPIxqtZFHUP561QiCS1lfMh7lzlyYooswGIpWSUYQ7o-ERgHSyJRUfU2-ALt6qA1w6LyNOP3vxPxfSUYLhu8P4hFnegHNepY9xBoaQ3ND7xY_hEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=OwkPk5ogH_fdSHMXtykUbwEjSVe_cUgOalmhyJBzwsCSE1E-0JsFRROrxscc7F59tWXfvUxvcimqI6benvyrcCL0Ujm001Ozx01xlbD94q-gTqzHXNTPn3NfCyQ31rcljsbLrmijB2ZEDOH9IaJtP5iz-j3OkesQlsUwJNJac4EDKVSFOlH03SbryyPNgEy5bPUpfdKnCHd9BSCOD3WXtbPbecqu2-rkFOM5QWyPIxqtZFHUP561QiCS1lfMh7lzlyYooswGIpWSUYQ7o-ERgHSyJRUfU2-ALt6qA1w6LyNOP3vxPxfSUYLhu8P4hFnegHNepY9xBoaQ3ND7xY_hEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⛔️
نگرش متفاوت دو سرمربی؛ یکی شکست را پذیرفته و با قبول واقعیت به فکر آینده‌ست؛ دیگری زمین و زمان را بابت عدم صعود از گروه در جام‌جهانی ۴٨ تیمی مقصر می‌داند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101661" target="_blank">📅 16:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101660">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=bb344BsijLYiUw8qjLnwGRufvHjjSi47xQ7I9f-WggexlRYnPSKgaWNAM2BLPWpK0gUd8tVDmzhrlCXhWFcmx2Sj1WjBMK3XcO9SuX_M8hskWyUoGUbeRqXgdW6AhkbEolzFgaDizUnP72hLFdcTn6yteZF-zHU_inX3xDJe3C8l3JJ616bF4BuDRJIP-81zK0T0r6MyenWus9C6zUuQzL6u_TVi6OSrMKqvwd2CcTJuqKtmPtYKJK17i9dTgE3-dcVbnzSQj9ZYx0coYGe8xzQyJ4rnumJ91z6wPpv2vSd3vic63ST-n4svTM0pXMXUhrYtSa8dzpo6oO53_Hke7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=bb344BsijLYiUw8qjLnwGRufvHjjSi47xQ7I9f-WggexlRYnPSKgaWNAM2BLPWpK0gUd8tVDmzhrlCXhWFcmx2Sj1WjBMK3XcO9SuX_M8hskWyUoGUbeRqXgdW6AhkbEolzFgaDizUnP72hLFdcTn6yteZF-zHU_inX3xDJe3C8l3JJ616bF4BuDRJIP-81zK0T0r6MyenWus9C6zUuQzL6u_TVi6OSrMKqvwd2CcTJuqKtmPtYKJK17i9dTgE3-dcVbnzSQj9ZYx0coYGe8xzQyJ4rnumJ91z6wPpv2vSd3vic63ST-n4svTM0pXMXUhrYtSa8dzpo6oO53_Hke7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مهدی‌قایدی: حسرت خیلی زیادی دارم که چرا بهم در جام‌جهانی بازی نرسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101660" target="_blank">📅 16:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101659">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101659" target="_blank">📅 15:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101658">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=vyoc8CRlfpEwbA6Upm_Ldfzhd7gVceCFhlNQm0IKhFoxJnDl_J0r6RqfAvJA3Rp-wy9s9813267z3Uca5RHQQfxQ6EZmAWd7IeW7mAohxk1r2sxv1fae9rFYXAawrAlsq53reLZUm2p1MGgBCGvLXEFLDXGWhEhmcoD3ovuKrk1wwQpchXFq31zgTK70c3Zicq09ACSjAPyMZByg1Unv0uFkICEttN5L7-hzZklR7rDLSa2DnuVAMm2ggv7otECYS_Tq4XFFwSIv1jTlBRSr3UIyAlNC83iHEaWHdXy-HcdS924numsrkWB4qkLrPjPhdGO7ayD98c81re_mIoL2nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=vyoc8CRlfpEwbA6Upm_Ldfzhd7gVceCFhlNQm0IKhFoxJnDl_J0r6RqfAvJA3Rp-wy9s9813267z3Uca5RHQQfxQ6EZmAWd7IeW7mAohxk1r2sxv1fae9rFYXAawrAlsq53reLZUm2p1MGgBCGvLXEFLDXGWhEhmcoD3ovuKrk1wwQpchXFq31zgTK70c3Zicq09ACSjAPyMZByg1Unv0uFkICEttN5L7-hzZklR7rDLSa2DnuVAMm2ggv7otECYS_Tq4XFFwSIv1jTlBRSr3UIyAlNC83iHEaWHdXy-HcdS924numsrkWB4qkLrPjPhdGO7ayD98c81re_mIoL2nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجراى مريم اميرجلالى و حميد لولايى در بين ٢ نيمه جام جهانی‌سمه خالص
🤣
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101658" target="_blank">📅 15:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101657">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔥
▶️
چند سوپرسیو دروازه‌بان در فصول‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101657" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101656">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=MWs7WaDqVGjanIopcBeeFKOSJOPNuGYWcUisAjEGP3Xkjf2_nw9T86MJlBK7Ona-UayBN757e_RN_tKetIxsD3GuwpDKEmYQhKhuQdUQA4Z4RXKA8VPp3iaDiuhZwlqd0pAS-4XB1NFkn6lzQiu-49qO9YHZYaJUaZdmIa7A3r4o2JyYcZw4gPDKoYKw9K3gjukSosae054RmNymNMB1RUsbm1WJE4FEHjp-hcMZI92GW6zeSemOuh4Sh6sDF4o-KKRtsA0kvPnBFXQY6YZhqyG2dXkKVJmfzn_FvrPcsH_vZPzz9AHEIhnEue9pqZoSNTbToktOl0I4O2goYfcb-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=MWs7WaDqVGjanIopcBeeFKOSJOPNuGYWcUisAjEGP3Xkjf2_nw9T86MJlBK7Ona-UayBN757e_RN_tKetIxsD3GuwpDKEmYQhKhuQdUQA4Z4RXKA8VPp3iaDiuhZwlqd0pAS-4XB1NFkn6lzQiu-49qO9YHZYaJUaZdmIa7A3r4o2JyYcZw4gPDKoYKw9K3gjukSosae054RmNymNMB1RUsbm1WJE4FEHjp-hcMZI92GW6zeSemOuh4Sh6sDF4o-KKRtsA0kvPnBFXQY6YZhqyG2dXkKVJmfzn_FvrPcsH_vZPzz9AHEIhnEue9pqZoSNTbToktOl0I4O2goYfcb-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❗️
علی‌قلی‌زاده: امیر‌ عابدزاده استعداد بی‌نظیری در نوشتن و رپ داره؛ از او خیلی چیزها یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101656" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101655">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfokCAxW2QE7kCmevSCu0pUzGsmT8tXA-C8ZfO4Wqn56PVe61uNvh0oH7Bt9NpJ6mxu3RUqSe_XgGSvp8IiYEOOA9nQjrc_jgc0CAB21QmSXR94nvUa1YuSIeTPwCZnxIMviQxMvFGDHJFDvnIpJpIXHAfhgZTi9Fa260PN1mEp4DH7F6xGhJi5VzrCAoF6iI8B4hqrYWQT7vpmvEvge_czt1Oh4nskAwWrZIdtPVDlYQE5AaDBj_1Nj0SufsHSbAOTSKJdbA6sHea-Q52PwhZ_zRSrAyDR8rgg8_nlkmpZXCWzFeR5_ukF64vwDa4q5CypHTMnOcUH_l7Pe7JU2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت گاوی زیر پست یامال
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101655" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101654">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=L55TfygedqLRHW-Wg08KcS3oT-SjuM2rfMMLb2nNWqJiPur6cTzPZVy7EBMeL0saRhjAp5jYAQ6thY6J1abD1FrOn75BvxS7iG8WabUhTH74Cmc37AT7LPrJJtAWrn7E88N1SpcqJLfTuIn92Uf9lmW0dssjOU_P4Bov5A8d4X2wjCwiZeVwkFmIz6VaD0sx0DahVUXnU3x3jRpj6BweXdnJfur87v7S734hd7DpUKjIu2SoyT3hRLr3gVEMpY6hG_cU9lSj9TvHtDaNWMdk8esRcUkt6NSU4kMUC3lggKBrRQgCzpbp7LzM6JXg3yKQnXGwdPrDZW80UC1gh3exMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=L55TfygedqLRHW-Wg08KcS3oT-SjuM2rfMMLb2nNWqJiPur6cTzPZVy7EBMeL0saRhjAp5jYAQ6thY6J1abD1FrOn75BvxS7iG8WabUhTH74Cmc37AT7LPrJJtAWrn7E88N1SpcqJLfTuIn92Uf9lmW0dssjOU_P4Bov5A8d4X2wjCwiZeVwkFmIz6VaD0sx0DahVUXnU3x3jRpj6BweXdnJfur87v7S734hd7DpUKjIu2SoyT3hRLr3gVEMpY6hG_cU9lSj9TvHtDaNWMdk8esRcUkt6NSU4kMUC3lggKBrRQgCzpbp7LzM6JXg3yKQnXGwdPrDZW80UC1gh3exMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ینی چه بلایی سر اون تیم پرانگیزه اومده بود؟! ببینید قبل از بازی با فرانسه همگی بمب انرژی و انگیزه بودن ولی تو فینال امسال انگار همگی از مراسم ختم اومده بودن.
بازیکنان تیم آرژانتین تو بازی انگلیس داشتن به معنای واقعی کلمه میجنگیدن و بعد از بازی مثل دیوونه ها جشن گرفتن اما یهو نمیدونم چی شده بود که اونا از لحظه شروع فینال هیچ تلاشی برای بردن نکردن!
بحث تئوری توطئه نیست و هیچ خدشه ای به قهرمانی شایسته اسپانیا وارد نمیکنم اما مطمئنم تو رختکن یه خبر بد یا یه اتفاق ناگوار برای آرژانتین افتاده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101654" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101653">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=Cwx7YqUb8icIouv9r3AU08j6JATlY2hX_2FWCJDVrbDXxUpdZEZs3gPsPcPBAj3ucSqDm-XbwskRVEwddcjmO3AqZeH4bUKbD5S10HVfiMOdDL5b99WYrI27ZHSc2hAmY0HyBw7XObQQbnX86SwgOnk9XFK2QTBz01Y5QU6p2kc7gZbOv_-ra4TqXHaaCIJryipnDJMgsTOT7dSNEVGHvuPL0M5QvIvaYmAwR5qPBXhEzaueMsnf-Y61Lv0VY7ezkFbZg4ND_PiD4XGuxh5etDkhmHd3gLBetRir1sxpiVTJkM5mDJ6eLLyQtiWxhqFjrPTeeUb46472BlsLMhRcaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=Cwx7YqUb8icIouv9r3AU08j6JATlY2hX_2FWCJDVrbDXxUpdZEZs3gPsPcPBAj3ucSqDm-XbwskRVEwddcjmO3AqZeH4bUKbD5S10HVfiMOdDL5b99WYrI27ZHSc2hAmY0HyBw7XObQQbnX86SwgOnk9XFK2QTBz01Y5QU6p2kc7gZbOv_-ra4TqXHaaCIJryipnDJMgsTOT7dSNEVGHvuPL0M5QvIvaYmAwR5qPBXhEzaueMsnf-Y61Lv0VY7ezkFbZg4ND_PiD4XGuxh5etDkhmHd3gLBetRir1sxpiVTJkM5mDJ6eLLyQtiWxhqFjrPTeeUb46472BlsLMhRcaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رضا جاودانی در جواب نگرانی عادل فردوسی‌پور، به جای فکر کردن به خودش، با آرامش گفت: «بذار بیکار بشم... مهم نیست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101653" target="_blank">📅 14:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101652">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=JBsMF4wa1M2yjJdlHNXFX0eoCeNlwKsYiyOJU10DoeZATecZ_j9FrDpJmRYGjBOP9fH4pM-VZfNraUhhbhz_vNEX8QB_JBqYd0lPgzyzMZjNMuRQ7YL_iUTV8Q_WLquXVG2Tie9x7IitG9NT6bdxT65d92BstYxdx9xbyJAHO5Ece6ZjVC6x9TPcCL8ASXF5RPMnm_XGrALso8-HALFOTEf9XgKR96vjlyB_Eal-36XNuyMshn6uj5eYYM0hkrSYT57Jk3xkWlnoxhZnB4eUq-Q8-lY8pPUpLbXz_AR1FqYqHqsvBV7xObmkdARm9B_gQRQz7tFW4hUz7lQnNdZWJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=JBsMF4wa1M2yjJdlHNXFX0eoCeNlwKsYiyOJU10DoeZATecZ_j9FrDpJmRYGjBOP9fH4pM-VZfNraUhhbhz_vNEX8QB_JBqYd0lPgzyzMZjNMuRQ7YL_iUTV8Q_WLquXVG2Tie9x7IitG9NT6bdxT65d92BstYxdx9xbyJAHO5Ece6ZjVC6x9TPcCL8ASXF5RPMnm_XGrALso8-HALFOTEf9XgKR96vjlyB_Eal-36XNuyMshn6uj5eYYM0hkrSYT57Jk3xkWlnoxhZnB4eUq-Q8-lY8pPUpLbXz_AR1FqYqHqsvBV7xObmkdARm9B_gQRQz7tFW4hUz7lQnNdZWJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
شیروانی، مافیا ایرانی فوتبال ایتالیا: به اینزاگی گفتم طارمی را جذب کن، اما طارمی در اینتر جواب نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101652" target="_blank">📅 14:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101651">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sc2K0WVCsN0Yr-JRy2YSW4x_WPw_J3UXEqcAjAn7OOANEv-X3xOlsikdbJaS9zyd5lhpDPG30LXE2NMu9Q7pT5pfAvkkU5vZdtWCdo5CSj020VyqXJdfXSkuyExOLxs0jXhUNu7nkPdoBsmTHoxfG7c1cpdnOevGl5Wedds9-ASvD4UwgDiqEofnfIWIPzmxxvtBNizRidw5E5p_foDXQ6ihO0CeZv6RwQhoYT9aGMhYid43CdsgTOJTP-TRSwwZNVaD3JcQqaUv2mBoyHv9umlejEAOGR_KfnH_632NBxtwBMLbtEjRI2vLXg_l96zJbqNkQYHI1U9HJCvVqbqMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101651" target="_blank">📅 14:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101650">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=rrXv9c4u6AqnkFgJKiU7j_KMDxeI_upDnjITeU-2c4awVu2nPPNSbDCXlHowVWLRYFNpaKqTo3_5NkTm5eaH4YxaPrd5lEzwaUzGFGJ8QyOnKozgTygRQatX7f8mdi0mqWByoznhCGqEi6RyBo4zVh0Xl8aD8aFpV47r7UPHGuCL4AdzH085sWQmbuHUHKYBNzU1j4ZKXUAnRP8Kh2QkY6CQioZSQa3s-zoniP13AB6adPv5ZTV-Qpv4fS5OD0QtW5TA_dlH6dgYDJH7clII2AwmPzZV2u08Yar0oSFGd4XdB7j_3_FTIzLFvFrz2QUG0eajVmqkwi4rolNezea8Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=rrXv9c4u6AqnkFgJKiU7j_KMDxeI_upDnjITeU-2c4awVu2nPPNSbDCXlHowVWLRYFNpaKqTo3_5NkTm5eaH4YxaPrd5lEzwaUzGFGJ8QyOnKozgTygRQatX7f8mdi0mqWByoznhCGqEi6RyBo4zVh0Xl8aD8aFpV47r7UPHGuCL4AdzH085sWQmbuHUHKYBNzU1j4ZKXUAnRP8Kh2QkY6CQioZSQa3s-zoniP13AB6adPv5ZTV-Qpv4fS5OD0QtW5TA_dlH6dgYDJH7clII2AwmPzZV2u08Yar0oSFGd4XdB7j_3_FTIzLFvFrz2QUG0eajVmqkwi4rolNezea8Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد شیروانی از اعضای ایرانی مافیای فوتبال ایتالیا: با دیگو مارادونا رفیق صمیمی بودم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101650" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101649">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJMkKPr-BQqShyCebC-6qUIo92REfxTidFyYcuElP5U3tK2-0wX8-elZukBzmcdCTpdUsYV4TT8XfIsO2IxeMsZ81tV2XPJTslej4zTuDrK4hcrWIJ42EzLYahibd1eUcwl1VeLTQDGir7lIthPFLLFHRjhu4vJ6lJy_rjBDtKLpJA6l0R646sPxuIK8kDJfuYfIFdeqeHu5VAaFzRkogLeCor2PXUfDiAKcLRlqNk8q9LUjNc-BBp-8VJdlZQPSKAWs4o3L7hoDIyqDnDnVrJy_sEdnBMKbANv8yMjnHBNDnJ4tnQKRkpQ_yv9kuM0-JtrfN0ft6rjC1KK2SZAgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
⚽️
#فوووووری
از مارکا: انریکه در روزهای اخیر با فران‌تورس تماس گرفته و پروژه آینده تیمش با حضور این بازیکن رو توضیح داده. قراره تورس نظر نهایی خودش رو بزودی اعلام کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101649" target="_blank">📅 13:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101648">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=pRs830E-3pRnFq1ukQDuBkPButzEyP2rHHsgrf19sNWHhGKwsPF7taWYRgyel2x9-5qIMp6j1AAIqElSqprcKYg9nG-XsDDd9ZY4m_dnxMkehAYihrCsqohN9QfZCkW8mpBHaEpQuzYVNZR3nEjG6LuYQJIhff96ShwEoqxDU-5tusxZSxEFEpZxvxy9lhZ0aeYNrcsipqRt-3TERUKyY6agNUBqlHPdu4HoQ0n6iyl7ZTiOskan0dLXUrDzUUbAZpDnpWW00U1exikXRdIWeGe6FYUFSjqB1fFU5wu5N5YIoeKvAItfPLPNnwyXSecYvQnSTjxeCBS4Z40-yLbvQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=pRs830E-3pRnFq1ukQDuBkPButzEyP2rHHsgrf19sNWHhGKwsPF7taWYRgyel2x9-5qIMp6j1AAIqElSqprcKYg9nG-XsDDd9ZY4m_dnxMkehAYihrCsqohN9QfZCkW8mpBHaEpQuzYVNZR3nEjG6LuYQJIhff96ShwEoqxDU-5tusxZSxEFEpZxvxy9lhZ0aeYNrcsipqRt-3TERUKyY6agNUBqlHPdu4HoQ0n6iyl7ZTiOskan0dLXUrDzUUbAZpDnpWW00U1exikXRdIWeGe6FYUFSjqB1fFU5wu5N5YIoeKvAItfPLPNnwyXSecYvQnSTjxeCBS4Z40-yLbvQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیدجلال‌حسینی: بدترین خاطره دوران فوتبالم بازی معروف با اولسان‌هیوندای کره‌جنوبی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101648" target="_blank">📅 13:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101647">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=EG-vLQelYXqxU2y1GSt0etquJeecQdFKhmMKQbxIlvjrabfT1E9kd3xhGKHQfRvAgMgLz2XGCksXjnSKPKQcuYave0u9yvmeKhR88F7atotqoGaUAlpGnZErqA7YtZIzK6OrlvKkni64G0-DQ_s6B98uprbUSfYXqhcfN1kIVaH7PSVfrnI-P52Sohga6CFlit8YP5wVJRi4KlD4-yINgD_6jfHJ-Y0mzSkP9U0Yz9j0wOj-VeD_FwkOAl-wk1pyNWTQfyY6KiwfOYDTiL7kmdPQ5zlGWTJ_cyXMDWFrXzZk0A8vcDKAe2WTEHZwqHLEX-V3yGVHN6XKeucGihHE6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=EG-vLQelYXqxU2y1GSt0etquJeecQdFKhmMKQbxIlvjrabfT1E9kd3xhGKHQfRvAgMgLz2XGCksXjnSKPKQcuYave0u9yvmeKhR88F7atotqoGaUAlpGnZErqA7YtZIzK6OrlvKkni64G0-DQ_s6B98uprbUSfYXqhcfN1kIVaH7PSVfrnI-P52Sohga6CFlit8YP5wVJRi4KlD4-yINgD_6jfHJ-Y0mzSkP9U0Yz9j0wOj-VeD_FwkOAl-wk1pyNWTQfyY6KiwfOYDTiL7kmdPQ5zlGWTJ_cyXMDWFrXzZk0A8vcDKAe2WTEHZwqHLEX-V3yGVHN6XKeucGihHE6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101647" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
