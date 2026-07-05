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
<img src="https://cdn4.telesco.pe/file/D_LKKWV7a9LL7VQdBcI-CRi0Xpl6zVcC4pni9CbKcYhlQtc3IGbh0uYZuUcKvASv-GwqjZvsD0GYeBiWPmu8bunj-a-AMZykpLbSbb3kzsM6KIylkTwVZ2lVt84gyC5setlLn3IJLqhFbad0PhyjHQcRlqjjhXvq4RCnEYVRPv7UInQ6MWHmqklUtalB0wnvX70FVI9_-QTcLCsRcihMpf-lt72bV8_6YjOWb9_CtTSMEVL6mw8-LbN-8FnXzoM9eUCi8KkfSvE2OVM1nEjRmlEwCrgt-KrDkKhrS6VLViS4fklY5Cy2GL-sPRy75Lj6MX8cAU3EV_hxFWLsflyk3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 04:45:03</div>
<hr>

<div class="tg-post" id="msg-666703">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae95ef246.mp4?token=BJGf8M3CvZKDUuO5GoI2HWDd0_R68-L_eapmWYOf3sYtHOckPABVfNecSQhM1nuwO2z-mozhIsxLu87Z5rjaKJxN34YcjEIcmcfJIC7dMIW6lh3D5bPNFhNaY_1mmE9pnsjMnhc4_ftPzPBoJtQweoZBYisB45_EYBMmVn1iTQIvcuRPseqdAA1Z2GKFpQfKhlFV9b48ul_gV5riSBJYpAeAFoJymFrExb1WaqWt0nJS5061wakXXXeZxGnnM3t28htbZeC7s8DSR5wO-PeFRM5NsmeDixdaNATAio4PyXkORxUFnrshK8z2fOD3Sm-CfIZGtVfcyPxF0z2NCR9BX7CoyMnmfbb2t3U0RF2eMo0dlm1OKjidN37K6jUeNBj36c2GAcgNMWTEojRqgywFdZ0jUX8XFs2wXaaKGG2G1SwtG5mdLOSSOvF2qIHd6ev3jryjUzcB_0LXfcUi4l_9sTFJkGyebcfoJ2ougjumjKbltYwTNDxSTkzKT_v7GTsrE9zZUAjBxpavgTxX4rrGBimnikljbJ3bHbtMqdMP6PhxDVPk1RcNQLviBLv5WKWzFVxmbAxjIOt2wOLqQBjc5hYN4I4YwaNapG7_b-9uzeIeuMC_iHlPVP1Rx8iBFGZ_W2TEZnH3gPKShZ0Bbt3413VAwBBpbAAbeoXnLwL8qhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae95ef246.mp4?token=BJGf8M3CvZKDUuO5GoI2HWDd0_R68-L_eapmWYOf3sYtHOckPABVfNecSQhM1nuwO2z-mozhIsxLu87Z5rjaKJxN34YcjEIcmcfJIC7dMIW6lh3D5bPNFhNaY_1mmE9pnsjMnhc4_ftPzPBoJtQweoZBYisB45_EYBMmVn1iTQIvcuRPseqdAA1Z2GKFpQfKhlFV9b48ul_gV5riSBJYpAeAFoJymFrExb1WaqWt0nJS5061wakXXXeZxGnnM3t28htbZeC7s8DSR5wO-PeFRM5NsmeDixdaNATAio4PyXkORxUFnrshK8z2fOD3Sm-CfIZGtVfcyPxF0z2NCR9BX7CoyMnmfbb2t3U0RF2eMo0dlm1OKjidN37K6jUeNBj36c2GAcgNMWTEojRqgywFdZ0jUX8XFs2wXaaKGG2G1SwtG5mdLOSSOvF2qIHd6ev3jryjUzcB_0LXfcUi4l_9sTFJkGyebcfoJ2ougjumjKbltYwTNDxSTkzKT_v7GTsrE9zZUAjBxpavgTxX4rrGBimnikljbJ3bHbtMqdMP6PhxDVPk1RcNQLviBLv5WKWzFVxmbAxjIOt2wOLqQBjc5hYN4I4YwaNapG7_b-9uzeIeuMC_iHlPVP1Rx8iBFGZ_W2TEZnH3gPKShZ0Bbt3413VAwBBpbAAbeoXnLwL8qhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر مظلومِ شهید، خدانگهدار...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/666703" target="_blank">📅 04:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666702">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5891bf502.mp4?token=BW2k-G4x7DEcus4uNrisMeueJmn30fWCDrniIpnhNfUY8WdzADG60Mda-O_Jr7ffuX6QwDZ2VYYYfhBq03JGTcDLpqAVigsXix0Bkh5YHrPm7e4tgIH5hAsyO40IDfTvtr9WMoRn43FC33n-UWGa4f4ygAzJ1qGeFBv3SF67qsA5G3ulYeV-ofropg90JqhJ32yORm0CHtd3BnBCPFgyd3Y-E4H-RkvsFYN8yodqITIjXnpdT6niGXoorBtEpBr62fZPBQB_FpleGLfTAG889QIBRPKaOOPtCLwuMomrJbYh7KjmylQXCKAPhkVqZJbAI-K_E4dMFqF8SJJXqN63Bl5IlFG8ItlFes4apMKfPV87shzVhRCtXN7RVahTGJKbiiSk5ggMg2cujgRyc1splzbZGzJpYkS6MR4ocNrw6qJOFq9YTpyarLMD6yW3o-86OBJH8XVurue7aU5oVule6Ok7ii8wEXYlL1C7W6BksqZwz_qOusFT3pb7PCItgK3F9R2GFBH1iOLPufMZ_BxD6URDeE80RqkmUMbHba6SZNfNjjJPnrDbvwLGsI0gAlsgIBsYFl7fKOlTTS74NqmTxEQAABermQaap-E4EC57ru6guBjqzEstuj3duu3VIwkVyIpHum3rjHSoa2CsslcB7uhysJmBWxxkDorzpBp0pi4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5891bf502.mp4?token=BW2k-G4x7DEcus4uNrisMeueJmn30fWCDrniIpnhNfUY8WdzADG60Mda-O_Jr7ffuX6QwDZ2VYYYfhBq03JGTcDLpqAVigsXix0Bkh5YHrPm7e4tgIH5hAsyO40IDfTvtr9WMoRn43FC33n-UWGa4f4ygAzJ1qGeFBv3SF67qsA5G3ulYeV-ofropg90JqhJ32yORm0CHtd3BnBCPFgyd3Y-E4H-RkvsFYN8yodqITIjXnpdT6niGXoorBtEpBr62fZPBQB_FpleGLfTAG889QIBRPKaOOPtCLwuMomrJbYh7KjmylQXCKAPhkVqZJbAI-K_E4dMFqF8SJJXqN63Bl5IlFG8ItlFes4apMKfPV87shzVhRCtXN7RVahTGJKbiiSk5ggMg2cujgRyc1splzbZGzJpYkS6MR4ocNrw6qJOFq9YTpyarLMD6yW3o-86OBJH8XVurue7aU5oVule6Ok7ii8wEXYlL1C7W6BksqZwz_qOusFT3pb7PCItgK3F9R2GFBH1iOLPufMZ_BxD6URDeE80RqkmUMbHba6SZNfNjjJPnrDbvwLGsI0gAlsgIBsYFl7fKOlTTS74NqmTxEQAABermQaap-E4EC57ru6guBjqzEstuj3duu3VIwkVyIpHum3rjHSoa2CsslcB7uhysJmBWxxkDorzpBp0pi4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرائت زیارت عاشورا در مراسم وداع با رهبر شهید انقلاب در مصلی امام خمینی (ره) تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/akhbarefori/666702" target="_blank">📅 04:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666701">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af442446f5.mp4?token=skqSUORSFfqeDUBq4yk3fyoBUtKYTj5jtelxawtWvPd8rcfuOwoTWQKLX0wb2z76UopP-TjAC39XhZQaelBVyWxd-uNy7trqytdkMnAffxs7Ptt8g3baGo-jD-sP_vHqEwQm8kwwSqC-xNFAyLN7Jo_BZkwhyfQVMuTOmbyLzBfkabjPbXFmlLnIUl91t8Xy5-sHiTsVkaWKjPlSrmvof9R01C3M8gFHuO-P4uveBPRLPp88xyNmoPfsarDg8WvRzJ1jLGUpP7QUY2-rolNKFi_sepLU5D_5v_5oKEDyJ6hqFJ8A2KpRQRMjKmg_Js9sx1RGC3rI8GwpSmrOB64paA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af442446f5.mp4?token=skqSUORSFfqeDUBq4yk3fyoBUtKYTj5jtelxawtWvPd8rcfuOwoTWQKLX0wb2z76UopP-TjAC39XhZQaelBVyWxd-uNy7trqytdkMnAffxs7Ptt8g3baGo-jD-sP_vHqEwQm8kwwSqC-xNFAyLN7Jo_BZkwhyfQVMuTOmbyLzBfkabjPbXFmlLnIUl91t8Xy5-sHiTsVkaWKjPlSrmvof9R01C3M8gFHuO-P4uveBPRLPp88xyNmoPfsarDg8WvRzJ1jLGUpP7QUY2-rolNKFi_sepLU5D_5v_5oKEDyJ6hqFJ8A2KpRQRMjKmg_Js9sx1RGC3rI8GwpSmrOB64paA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت حاضر در مترو صادقیه؛ حرکت به سمت مصلای تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/akhbarefori/666701" target="_blank">📅 04:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666700">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868bd0c26a.mp4?token=bax4iB_7pQZ0r7YOnIIGO8wbXF-qvb_fbhw9Mf9EtbEbKtQJpTgPvo-4btE09hNh1rd3u3aLLYkILEQ5ISvB7QCQ2brJFEKv0uSrkmReaQunCzqrmP0PgreKAm3qFbb3WdRh8W1gSK8zCffYPsVIkWP1L0uU2-fqGvcAYWyhC7K4aJWaCUUVD02avHjP_pg7sXgmchoPF97PxdDKCQU6_tMwST2rRv0nNQ1vZ1r9-WGuDJIRPRmtia61Y6g3hfKPnb83qjLGdrI4AxyqnvmJ06CofxPds9-7MF_dn7ZCtI-SSb9Xgim9NVzdOlxM0cUhUP6ogzqvLJRnUSy8BLSiVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868bd0c26a.mp4?token=bax4iB_7pQZ0r7YOnIIGO8wbXF-qvb_fbhw9Mf9EtbEbKtQJpTgPvo-4btE09hNh1rd3u3aLLYkILEQ5ISvB7QCQ2brJFEKv0uSrkmReaQunCzqrmP0PgreKAm3qFbb3WdRh8W1gSK8zCffYPsVIkWP1L0uU2-fqGvcAYWyhC7K4aJWaCUUVD02avHjP_pg7sXgmchoPF97PxdDKCQU6_tMwST2rRv0nNQ1vZ1r9-WGuDJIRPRmtia61Y6g3hfKPnb83qjLGdrI4AxyqnvmJ06CofxPds9-7MF_dn7ZCtI-SSb9Xgim9NVzdOlxM0cUhUP6ogzqvLJRnUSy8BLSiVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت مردم به سمت مصلای تهران ادامه دارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/akhbarefori/666700" target="_blank">📅 04:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
شعار مرگ بر آمریکا در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/akhbarefori/666699" target="_blank">📅 04:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4ec55162.mp4?token=hiX-8vJhR-rI4uAh_VJNY85oPoadX1HWvKw6xrWLFyowSjXeL2VSEJNPwLPcopPIrqWfWibNkcQsufctMz0hjahBjA4b28QgDSCpVfjmtcLoRec1oWmKeANrI7qy-AL4DIhxbDmw7Nt3BiNKM1evnF9v5tp3kjY9zJhQqRpjPVeHcbLkd7D9OfMVwbxatyBZSBMDKJ4uG0h1QOFptbYMAvggOi5S2YHwL3SAD0aPbi5CbJK50HLbCYbOWgebIK5Sg3bnjd3Tm-avdeiKKbW17Ebd1cjMMN3WW49xEYy-_eZNh2eGH-pEO7YPWPMdfs7RpGLR_yuEFx8iT5Ml8GXGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4ec55162.mp4?token=hiX-8vJhR-rI4uAh_VJNY85oPoadX1HWvKw6xrWLFyowSjXeL2VSEJNPwLPcopPIrqWfWibNkcQsufctMz0hjahBjA4b28QgDSCpVfjmtcLoRec1oWmKeANrI7qy-AL4DIhxbDmw7Nt3BiNKM1evnF9v5tp3kjY9zJhQqRpjPVeHcbLkd7D9OfMVwbxatyBZSBMDKJ4uG0h1QOFptbYMAvggOi5S2YHwL3SAD0aPbi5CbJK50HLbCYbOWgebIK5Sg3bnjd3Tm-avdeiKKbW17Ebd1cjMMN3WW49xEYy-_eZNh2eGH-pEO7YPWPMdfs7RpGLR_yuEFx8iT5Ml8GXGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم متبرک به ضریح و بارگاه منور حرم امام حسین علیه‌السلام در بین مردم عزادار رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/666698" target="_blank">📅 04:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
لغو سفر بن‌گویر؛ نشانه پایان مصونیت مقامات صهیونیستی
موسسه هند رجب:
🔹
لغو سفر «ایتمار بن‌گویر» به نیویورک، نشان‌دهنده هراس مقامات اسرائیلی از پیگرد قضایی و گامی عملی در پایان دادن به مصونیت رهبران سیاسی و نظامی این رژیم است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/666697" target="_blank">📅 03:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666687">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqMfqeFREmfGgjR7mBzq2GsRRGxPuQYJjNemsQsWkbLfwI3lSrLI3YFS3_PT_6HB-kO7WhMf1q9C4KEuz4gRi5dXBc966m6pRBv_EhG-BYFZriuFMDkmwSVeyuKkbnwJjN0uQ6wkbnZL67McRamwK-lVexp67_Gm8k90lJ3rYpEDXDLrno8nIpyPJgwVdMaf7SUn5q6wqh2JzpnE7PzUpc9dhQe_-fKBdw1n9SbOZt4OOG8Dk7Wje5ShAS0z36CujBxmt-HNHvo56ybi0ffTpCB6NinynvY3WbtkvhnepqUpSvmpmzVJj2KzbJbE8ZXOLl_4uGwylx5QIYojrDK4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzmX807GG28oTJIAkRLqWlmfxZDQ3IsjqRlSEMU6jRddgccIopQp-l6XajyNcqVcwZ4p865vQ-PwDWUzm1CrAUZehcol3IiEeKGJ8et4XorpHMah2_TTYXDQysQBol48gX-_4KOgokzIi0YXZtVvX7hDpch-NbrfSEuhsbRITvWna8RW4JR5jCWqQaYNbOQJiZqe2Sf87oYa0UiV69WV3cR7poX7u87w6uW_d5vAkGp4EASv32IfuwMpw_NjWWs6_W4VFyAWsOMj2JZKYwSZ77mvUVKwwcBC0uITF-BY3PF67Yz_3rDzc03dHIPnktulV1uQV1m3JJKIRV7b6aeuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3xfXFUc1FQLD7dj6lCvKdKKQOF2NJUnp5e92p_uwSoVHPLqwrafLK37W5L_GP3HFn-C5jeD8PaoZ7mpUsAkvMbtLnJSm17rLqD4uGx5vfMyhlHF9Mv09_xWwhZFl_f6KJpvTrqOL70D7AG4a4Yr7lc7p2qN9SPwp71ZiYAaNnpFxI7RInSGxIoBkatNrC2-NfGPUqPN9KhHkbLF1YhwpbOc4v37bCXjiFYzzNcnn7LFDu3LYb4g4hi2rlD2uO-IgAulRKByOfWpJordx_6kZ3UIZ7LpYVcIvWDg-IkgWBSX6XQmyi0bwmaqjUiELS2jlxznVsa9QCqldCOcgMIewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUk1Bnjxhz_UtqDauDrn8ecdJGcIOYC4vIPeCPr2Ay2Z25-D1jER9w27ZX6a19QgD0yMNToWDZMlE5VQlC8vvkghwjODbcs52_h0wcd_0B964-45YtfZQ-8mCcE-yipMMEtMML8uNJQ_yiT0PaiCyk8Bd7xG465ZefeVlIL9T6v_s1hiMiJXpq4p5K9-PFUee5ZY4H6no3iRUbXEdUhtnlCkSD2HJgD4kM-pn7HsOaLEntEIANgmAxdW21J57qKYRp2iUp2q8KhrCJVJgW4bfK9TKQlYvWmBwlQHkZRC9DgLcMkczmscp9k3DttPWCVl-ytLTuiUvSSLuPz4KXGmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFi0454WgstoMSQRYP155E-IbGLtbQ4O6Bt-_E3xqF05zVlKXKFN08KayzOgvI-T88emAO7T8hHY4LU6ahidAakyFHquo2cnvjsK7idLYcZ4dqUkG1hc9AdJima5LZzhSl_OfOZFgir8aKqyXnhYCBjCYVbGxo6tAb6uB_xBgU6Y6Y116ZUXc6hPjbU-E7u3QPc9s4dDA-t0ylW9UeDN6QcH-daU7ml2As5lRvZ2UsS5o1xunS-YFASHFzemboHOQIubLIvDHTxGMCww2dMPH-DtbJJ83O8oXhSUdVCsKCSy1mcBLJgH7FWkUfp9FpAeyS2ESz1GVL1nhA0HnCTUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6rY9EmjeyDi_z61wUrkCjOAEqWw_LnQFIpxI67snzFsP5xXlH0SMYcvqwzXe6W0x9AXX8RAN-b_9BOTC1990NAfk9jQe9J7pNRosX1oEVgx1fzKpauf3cwcnG2t0MmBniilGe2lWXkwNg7EsRVlVXvkRCwJRzvVetD8d4uEe3B--SN9qZoRBcCvntKCAEr1fJA0OqGZc7KJok7JuuikP2ncVtlKScuveIOKvjIGPT_U5oQ68SapACwG8nVQrQkqDZMlsdkvyDLZivQE4LUvpWPU6LYvuLMvzOBPx1jBiYV7YD93q6FU834-sJeFxj0K5AbqMpECtrTSedd5iA3SOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvZpSpQu6CFr084Q6G0jkQJvc8SAl-D_2ujQ-ttaF9vOCvdCLICzdy94WDTYTtCi_3UwM-kZ1nce8LuK4AXizdGgWcIc1JZ0T-8PEC_Dvo6XTwlkxVaezRzRPq7MBq7NX8aqbxfIGSmloQ5G4X-K5Ifw7y4L4Q8U3YSJH8o5RWhvvz1PjPiuf630-axgOeNIrBzmO8x_NTh05Wgevo3canrgP0ih5xos5UNOXCs2AZb9eZgtFXhgjAoBVnmuOiagZZN7O3IqRJkXKElcY-LhRPxStTPsJ04eURBQ6s9A_wE5v2Js8ToEVpF0ycQYJzdQ7_FtpHU9lgDNq80uHDCmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9PaIjGgx94upnwlhI8fw-YQoJ8mENleGs8AEQpLECxovfI5qb9-BacKX8z7ziJxoRIdaXb5qTN70nUC9Pwxu-nvPwPEkbVLvyJ_c9NvKFt8RCgs4UpbEPk_l4XCwRkCpkprppT1pnXqtUiaJ1YqZzglPhzLgPQIUFGM4BZrDJp5gwUSOhyZm4xaLV69xc5n71YBJ2mKeUzTood8Lozi6ACQhwdWbxuTj6vs9_wJ9bTIxX8nj5tuIj-BFoOzqo5XdZyU9suA-CwCZOhKNumPVSAQejLi2BYhRHzLc0kaedwCO7DfwtT80JRbpz83blloz2Y74U5mKJujxI69VzUjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YozNh86vh14NmxYFKqMCdmbrq9sllPLBQEHTUkf6fiorXOPx2ySA1dbA8ST1SzAk6DXaBcgNp-2n_PVcxTYoNGRhkkBgri1ZoJmpbmf4JgLPSYKxwouTR_9pupE8hPs3iaXSeCgzBK1t69rAtmOQdnqclHFuzgf78UCGmaOion0ozoyDZqHX6I1wPssBigKahhUExQvc2MgHUvi2cum-Iv-sZzpbfrmzNWIPgGdJhGl6t7Bcc8YmgDqagzFLNpNLvnQxZb7dt6EDdfX4V1lnbjV_t4vgUT24Nn95T7isUKYIC9ODCwjvKqnatUHWK6W9POiyMfPoq5LPtfK1woOuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLtaoJ0iy2g4pcoyR43ecZ7VPY7xs5g3wY0PmJsr-HHu80ptNq70_SL2-UnCL8ndcWyXPie6dqbQA5aEKm8nk4ECF2HClHU8QJNOW6_465aj6Z3sVW-uB8DfmsqoEC9YDNYa_VJsXejfGGjidJJp5nbvy-tcI865xEBLN29Ifg-oB-DyZbY37fd2kYBc2vnEYQKxfO-cX7fdCDldIhDnREOjKzZpbyWPb6oSwOXN-M-945boehj1FKsy1-hE5Hljhkg52vFt-uqjuPLh0d9-98F5dZBTcxFi-d4BT87WA-a2I-cbzZgZIRgxRtC-A7adIU6mE2QtPDcMBG3eesPkzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور شبانگاهی مردم عزادار در مراسم وداع با رهبر شهید انقلاب در مصلی امام خمینی(ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/akhbarefori/666687" target="_blank">📅 03:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666686">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
حال‌وهوای لحظات ملکوتی اذان صبح در مصلی امام خمینی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/akhbarefori/666686" target="_blank">📅 03:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666685">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
قابی از تابوت شهید زهرا محمدی، نوه رهبر شهید انقلاب در مصلای تهران #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/akhbarefori/666685" target="_blank">📅 03:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666681">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrFmtNanMv_Df4Uzs0MIJN4GfOgVd8_i3E0pErszQtVUyF1RfS0p_sw7IQRP8uvxkM2dYo1tXKEitRccLFGoepAd0ZDKy_yqB-DngUOtS2yf5mCH_tQX1majpZK4zS-g7rV3ubvDlFTZcNPj3qL8AY5lz6a8BAFpegnIGQNUcnqwyORaZFbcuDNI01A9JYsgjBe6IyMFUD4cC5ojdfJ3uM3TczY-3gh__tOpJOgUH4LoUK3Tuc7dzHwku7MSezdyCmuiciKCruYvqFdMt1OX2LGe8zm7NbjCW58ScCPbCEHZEij3KUBdJhgTmKC8dQ_oYJJGHL2LQ6ed5VULmALl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ASfDMGRTgvudeqIVSv2rxUkYdAWu69x0nPDUw-yXleJedvYjTzGFPcmPFR-sZOGiVVkCJDwzpD5V5pFPiW9-hwPxgYMpDmEqNoR4cxpcLHpf9EbxRUt1oV56yzT6dJtXUkYhJL8MmwzZ5HLSdendSAax0d-d36Q8k-C7J9q89EcFIifjEFsyWZeeykjZf2RFfeLjPiDLOG9UFzTN8awENLhjT3Gr5l8LvG01QWZc8Boc5W7fO6B8A9A0nSYUsN5dNJqyHyqM0DiTvx3N7MJ7IYTLP-Cnr0zKYa6FK0EsG-9RPsz10yIEp7xcTTtnOoF83lE_U_-69BfkpxoyKomChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1xNjL-q1ejgKB8txNbykLNLoy65nO4s4Wnvk0GErAIkU-IOuRpgfSGMl83C9OMgjjnC9dip5y1DS6-XOScSIsJ0V8UI-ioc9SdiJsnqo-SzJdekdoaTa-nzl6MUbbZy815TzVC9X8UI3jY3YCkZOamrzIZY7HPV0xHaKd2UsJtKMFTeAHtBXgqArxx5Odri0ZLtTm25hNVP8a3cSRNsL2iMqEmgkcHOsAu61dadY_rpWjvuhJh-EhiAgXte1qfLEfXpJr9hUW_emmBaRtYEkcXFNv-y_1EAlJ9XMH-f2In2nm-9TiBNL8AEJ2W5iiGpl_3KXCJPY3IwFrBGkTQPxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f1a683e6.mp4?token=mBtk0qL5EIvESWlzkcP8naiSwSDOB5a8EPevOWbMurMNHyYufKzVUNcY7zH7PoOJDVJX9dYGnbjGiXfTf7ecEQGA2mdT9WmrO-zzJH483ClDYRusxkkkCLItdo_e7lZLVH9jL63dEDvlfG_wvXrS4JQPbFqf26xC8UBSNdsPnU7JYTBTRgZqnIZDzPRboTHh0SG1Y8qaDvSoo_l2cOpqNhlGDJR18LQh17foDjKKEzXu-dtwItl9nrF3B2ZeBl3FFN7dLOHUnLGlUnXeENcmq0Fg8ewtCdnyi7oko6vNwpgwoZ90IkkUUoZXaW8zNkIfe2m-sD0BAIDNzT2eV2-TOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f1a683e6.mp4?token=mBtk0qL5EIvESWlzkcP8naiSwSDOB5a8EPevOWbMurMNHyYufKzVUNcY7zH7PoOJDVJX9dYGnbjGiXfTf7ecEQGA2mdT9WmrO-zzJH483ClDYRusxkkkCLItdo_e7lZLVH9jL63dEDvlfG_wvXrS4JQPbFqf26xC8UBSNdsPnU7JYTBTRgZqnIZDzPRboTHh0SG1Y8qaDvSoo_l2cOpqNhlGDJR18LQh17foDjKKEzXu-dtwItl9nrF3B2ZeBl3FFN7dLOHUnLGlUnXeENcmq0Fg8ewtCdnyi7oko6vNwpgwoZ90IkkUUoZXaW8zNkIfe2m-sD0BAIDNzT2eV2-TOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی خیابان‌ها برای استقبال پیکر رهبر شهید انقلاب توسط مردم عراق
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/666681" target="_blank">📅 02:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666680">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJzHMUnrbqnA8LJsolx4g208bVTJHIlOTlPAx0-HY50jwTw6GbZBPd3zjIigP-Sekx5QimbC3mSZLjlGCpNZ3Ls3ab_JDB4ZDqE5kXWe1T_Gx7ZoGvLV91F-XVNUQmmFb0nTs9e9pOgMMIbYW544lJE8pcI1gqqRcgAiQZ86rN8nhAZ1JszEl5bxiGwDsfiFOk-Ayy2RevBMA2ie1pdxkxYbQRXvJSB78PTxzEv462vQkLioOVCbsvmwZuFh09OkT0UZy5ynsDrFf2fyerXUFlC-9FsyPzPS5rcWY36UIpbMNLV0baT6dBiKb-EwGoCLKfsT37NpUJf1NImYDF1FDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌اکنون؛ قابی ماندگار از وداع باشکوه مردم با رهبر شهید انقلاب در مصلی امام خمینی(ره) تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/666680" target="_blank">📅 02:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666679">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-SLjLr9QXRsZk4MbndDd7LzlAmO8hUc2baHHSi-s6Fo1lBRFkz8tPA9Hre0t0X6jEIog_k9T_gBN7U2JF2SSlOTMpNeZCtiRinFTIQQiA0uJmnCoRN5r1O3jPXBGuHBCsrE0UhLOa6TZITNmDs1jQF9qVLkAWIEy1lRMRZuIc9vl0KwhQYAu1V2HTXYZTVde46Hl-eNpjClaTnQaJPq0YBDCU8BcuPaIw6DkQEHLZOuXoA7p4HpgLGDTwYF3QV4-_Y8GE0sYn70m9B77KZbcXva1q-12zLcZgNtvRuDZEFQ7S_iTNkEDX19qo-0vXqEE9VAaNyUhnoS5ERJVWS1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بروزرسانی نمودار مرحله حذفی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/666679" target="_blank">📅 02:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666678">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZhJKYMD3lDL9Un46Fs4yhafaLr44Ks3NPOzh7Nl2xNYiVLgGSMEFmUVR_YyssExBI6jrggowOKW1JZ4X8-3GJv6wIVwfkjn-P7pdoTtRWDNyGnwWTQpWV2BhXbaBM8ZsGfOl3tBmEyml5jfotQqojnRzPT5AqY9F756jEuSAyUtVnuwsQzMKmR5c4oQbVT9fblq8G28XXh3pDaa_M9_61_0Hsq-zgip9RHsN3dcwd5GO-sxQ1AZtpmtldQy3XgEMSG9s-4slWqrAWLfvhk2QxicMS3g9TBCyNcMhOBxR9g1tftFXfsGBFbi5lcg3nD4u8SVfLx27GP2VLlvIkHyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پایان بازی پاراگوئه ۰ _ ۱ فرانسه
🔹
فرانسه با تک گل امباپه به یک‌‌چهارم رسید
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666678" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666677">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c91f002533.mp4?token=X-xe369pYgEqxb7myCuBSzFP8mh6KtMf4nnVMiXdkz5yYgF7RXjBJKL6I2cNeQc0ikWi9ghNRvwI3t9rsp-Tx1E-OSiHjwKnFwb2CH5QlGjjTFwByR5aRc1Mb1hwsk13AxYEtgueM_rlacIbrbPESRRNFixe3FgtkH0KcPhr6G4sgR0YMAHN0pPg3ZMKhX4XMNPRk2_nnBJytbLPXyjVB1Z6qLR3q5W0iOCiHRZ1_wrtElDWpYDnIyJ-SS1at2ZZB8WQJ0WZR0P5bnNtN3sJbiZ7BixJi11OwFq88lcm7qqpboRqGM4dF13DG0uq1IMV5EDmhxvcQhDqBMZvLfwfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c91f002533.mp4?token=X-xe369pYgEqxb7myCuBSzFP8mh6KtMf4nnVMiXdkz5yYgF7RXjBJKL6I2cNeQc0ikWi9ghNRvwI3t9rsp-Tx1E-OSiHjwKnFwb2CH5QlGjjTFwByR5aRc1Mb1hwsk13AxYEtgueM_rlacIbrbPESRRNFixe3FgtkH0KcPhr6G4sgR0YMAHN0pPg3ZMKhX4XMNPRk2_nnBJytbLPXyjVB1Z6qLR3q5W0iOCiHRZ1_wrtElDWpYDnIyJ-SS1at2ZZB8WQJ0WZR0P5bnNtN3sJbiZ7BixJi11OwFq88lcm7qqpboRqGM4dF13DG0uq1IMV5EDmhxvcQhDqBMZvLfwfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورودی مصلای تهران در بامداد وداع با امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666677" target="_blank">📅 02:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666676">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
روایت مداح معروف در مصلای تهران، از توصیۀ رهبر شهید انقلاب به وی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/666676" target="_blank">📅 02:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666675">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2c4881ee.mp4?token=qLLnbG2gFirVb3Aj_xPArXqC-7Jzi4Y57U2lQD7iJUNYGpIOkrEvVNzUJpi0CTawjP1CpCSMk8WfcRWbN52uWLjjGzvDq9CV2Hd9cgyHiezg7VQHIvLDZc9OqFITfUISkI6BP90hUt5ThC-BwbWz2f56H6JCTcu6toNYajEsaIpcp5cxCuictGzLKlhu2MGjiuprtBjwMvVYaZJ64VgXwNLVsZ08jLI0n0RGU1wMiIazRQ2s2SHqxgp3ux6w3uv10soShRc5dJsNqq_Ld507oAHcR257nhyF8f7FbRr3BFVrkUwcBhyAfk3QGj_I-z_IJt9BEx2SlyqvvTP706z7_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2c4881ee.mp4?token=qLLnbG2gFirVb3Aj_xPArXqC-7Jzi4Y57U2lQD7iJUNYGpIOkrEvVNzUJpi0CTawjP1CpCSMk8WfcRWbN52uWLjjGzvDq9CV2Hd9cgyHiezg7VQHIvLDZc9OqFITfUISkI6BP90hUt5ThC-BwbWz2f56H6JCTcu6toNYajEsaIpcp5cxCuictGzLKlhu2MGjiuprtBjwMvVYaZJ64VgXwNLVsZ08jLI0n0RGU1wMiIazRQ2s2SHqxgp3ux6w3uv10soShRc5dJsNqq_Ld507oAHcR257nhyF8f7FbRr3BFVrkUwcBhyAfk3QGj_I-z_IJt9BEx2SlyqvvTP706z7_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای مصلی در ساعات اولیه امروز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/666675" target="_blank">📅 02:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666674">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
همزمان با افزایش شمار قربانیان زلزله در ونزوئلا، تابوت‌ها یکی پس از دیگری به لاگوایرا می‌رسند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/666674" target="_blank">📅 02:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666673">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
خروش مردم ایران برای انتقام از ترور رهبر شهید
روزنامه القدس العربی:
🔹
هزاران ایرانی با تجمع در مصلای تهران برای وداع با پیکر آیت‌الله خامنه‌ای، خواستار انتقام خون ایشان از آمریکا و اسرائیل شدند.
🔹
عزاداران با حمل پرچم‌های سرخ (نماد خون‌خواهی)، تصاویر رهبر شهید و پلاکاردهایی به زبان‌های فارسی و انگلیسی، خشم عمومی خود را نسبت به ترور ایشان در فوریه گذشته ابراز کردند.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/666673" target="_blank">📅 02:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666672">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuSkTDcX1Y26nivsPQjn5AWsfhHeZDv2j8UyBhbdw-L8SsQcyvri08TJZ53eWrnwI4_KGzM-dUQHAapN2iBsPfHFyabIlGeUA48xM16esLb30xRkyOm-AaxeX62WD3fRvqTnN80S2mjVeZi1cIfThW7uRpyadmHkBBvEs1e4F3sZdD1xnqx19q33BSER01joDTrWiF4PfUtpCZU3lrB6erc81sRdKmBHSDVlJ2lFZBf8SHaMn5CBiytukFcmngCHzFOvIt0mX14PbTaWt_b0-JaF6hZsZcb0DBlBwmfg5SYF46HBs7G2F6FXDTbSy0_AZhr7SU0iewa6zQuzJmqkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/akhbarefori/666672" target="_blank">📅 02:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666671">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8024d7e3bf.mp4?token=WDXzO8B8BZmiW5TIKJufoSES57L0WMrIlGVAO4DX36PkncVK34c0aR1eSU-pdYYyi8W3KLbwQq_OxVo2tQ4WmKYTf6f16AAeKMTRRs7bAhKX3gQdGHR7l4-TL8NdLkz9jfX7usqlxWAxM2jw-21Fxyx0qX_2YE7_ZQz0zhTaotyg8elb9SPo-nv4NJDQq9e_titPQJgqoj922tUXU5brVw0Xp6ILJFaXH72uU48zg9vJSTRy9bbk0pg5uW_32_nNPB6vzJekJsavJqm_I_XFzN_tm5HwrawsT0J7on_cS7c13zbpnsEuUV3cPslZ9CEqY3GO-JmXJbYVxotLy8iT8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8024d7e3bf.mp4?token=WDXzO8B8BZmiW5TIKJufoSES57L0WMrIlGVAO4DX36PkncVK34c0aR1eSU-pdYYyi8W3KLbwQq_OxVo2tQ4WmKYTf6f16AAeKMTRRs7bAhKX3gQdGHR7l4-TL8NdLkz9jfX7usqlxWAxM2jw-21Fxyx0qX_2YE7_ZQz0zhTaotyg8elb9SPo-nv4NJDQq9e_titPQJgqoj922tUXU5brVw0Xp6ILJFaXH72uU48zg9vJSTRy9bbk0pg5uW_32_nNPB6vzJekJsavJqm_I_XFzN_tm5HwrawsT0J7on_cS7c13zbpnsEuUV3cPslZ9CEqY3GO-JmXJbYVxotLy8iT8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه از نقطه پنالتی
🇵🇾
0️⃣
🏆
1️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666671" target="_blank">📅 02:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666670">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d812881e1.mp4?token=npuqDXehvFKVlZcVyU-BNQcfj0pihnBZx-HaCJGJ-iwVod5Aojm15JqOtpCEqDxpXxn83ZmvEyz-TRpy3rlspbQ4PVCmANjiUOoumMuS7eIEgPFh5HjjyeiXsNvnue9713PMQnaNIk_vz_elU95qIL_wGFMw7PsNN-ei9AvrXgTYkpxptn5qMsDdXaUDWzl_AGSr8H7MFQSIoTIzItef6MnSy2ndJUvJmWlaDyyzN4QOaeAbIR7xVSL30tLRxrIc2rQ5sXjfWudqmOACi42iCXqSS8S4Lz-r9GOGwnJLdLfKDwg63OBDhzMcCoSr0IHROQyHu_CvVTlk7me1Eyp-aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d812881e1.mp4?token=npuqDXehvFKVlZcVyU-BNQcfj0pihnBZx-HaCJGJ-iwVod5Aojm15JqOtpCEqDxpXxn83ZmvEyz-TRpy3rlspbQ4PVCmANjiUOoumMuS7eIEgPFh5HjjyeiXsNvnue9713PMQnaNIk_vz_elU95qIL_wGFMw7PsNN-ei9AvrXgTYkpxptn5qMsDdXaUDWzl_AGSr8H7MFQSIoTIzItef6MnSy2ndJUvJmWlaDyyzN4QOaeAbIR7xVSL30tLRxrIc2rQ5sXjfWudqmOACi42iCXqSS8S4Lz-r9GOGwnJLdLfKDwg63OBDhzMcCoSr0IHROQyHu_CvVTlk7me1Eyp-aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین بانگ «یاحسین علیه‌السلام» ساعاتی مانده به آغاز مراسم اقامه نماز بر پیکر مطهر آقای شهید ایران در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/666670" target="_blank">📅 02:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666669">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6OwsGt8abfB-vVh6BdCd2f0IV86bdLBBcn7ZZnY1hj3LyAHyW-RNlccpaBvSWFH7zGfgA0Qld32rg-9SnW-RVb2mZ9D5Sdv9DZbvM1TCxt-q75LuH_UaU5nZYUtuu5SucQ2DWpu9-V6i8ZgRsqXpwviiITOZIMEMlEK_B2VRrsCc8KjYHSqBd7Hble8rPTHgPZCUiFk7ziMLIsUjnqHtJtG3Yh-1YM3fHE0ULW6OKUEoPVrNHEuTIzvjSHt0InJi-G1ZrkF7gcJTFwGX7LZa5JF5L5xUSC5rx0_-5ozRjQd9lhIHHnb9hn411n17gtyhrTHkCfMmJdYikNYFxzjxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمجید استاد مشهور عمانی از رهبر مقاومت
🔹
مراسم تشییع رهبری آغاز شد که با ایجاد ساختارهای نظامی، سیاسی و مالی، در برابر قدرت‌های امپریالیستی غرب و صهیونیسم ایستادگی کرد.
🔹
دکتر حمود النوفلی، دانشیار دانشگاه سلطان قابوس، رهبر شهید را مؤمنی پرهیزگار توصیف کرد که از هیچ‌کس جز خدا هراس نداشت و برای پیروزی ایران، مسلمانان و آزادی فلسطین دعا کرد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/666669" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666668">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
مراسم وداع با پیکر رهبر شهید انقلاب امشب تا نماز صبح ادامه پیدا خواهد کرد
سخنگوی ستاد بدرقه رهبر شهید:
🔹
مراسم وداع با پیکر رهبر شهید انقلاب امشب تا نماز صبح ادامه پیدا خواهد کرد
از جلوه‌های ویژه مراسم امروز حضور خانوادگی و وداع خانوادگی مردم با رهبر شهید انقلاب بود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/666668" target="_blank">📅 01:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666658">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEKsvqDWoPOQcVKLQTfa75PFR_Aj_1JlRMELRj3_BY2wRELGkW5QJy4lbUdAFPANcErwLyRpCA6gY2SDDUa20XsNWfruuGNGQaqjEAjGCoNNQmhO4Ad3AN88fhhkXzZfoxtNTh7Siibpu2jIzUXgF7QJ0o93z2TkOxiQxkZ8OsFXwvm9HTM3aONT2JxB30G6oaLXZIeiCJBqwO4Y_4pbZjfBjzuO5_KwDuojIT4S2R9XVTLD19uU5cY3TfDDMHUJdLulY77Bj1VnOhSQCEihAI4RmR5FpeeHM-A4YSSLE4xXMVZpAG54enXWemyGkKjFrc5GiDMomVGbyKSEwhSFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ud-6LJB8lp31KvFzMg2-dKZetdzS_Hxk0T5Wj5wDEJzMaZXk6mWGZTjjlJ76HAP86x7G2WtiANoptvfyF-FULDZHuOmlXZPWLl0g9Y5P88gyDGZpZ6o2yE1aARHo5X1ShcriRP-370pdbIrM1HhGuK4xMR8VbGiandj91bQ2CGARN6AQ3_jQKYervPe9lTQmZLv6w_n4sNp2_qVm20BvfZxlqi5yrS2NAutgOG8VlQK9n7K1cXFlaiDGaEq0JVksyFuvbv4AaUCcl_BN7HX1I-UN3BObOshicNlYM3pWJeiV5tm5kJBMvljSM6qMiuLxRY4pzLsI8KyNv6KNwDKlow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAfeRLExCuihsIAUxGUp8nkEVJlHvQmwdX3TBHdyYT1wn2IhCCz_12vR6beb8Jf6yp2fsgbj0mmhX05xQ4CNutqW8_Sl4DevFLUbuWHfRLZVw1_a_mTmhpFf2hORssDFdvNPx3mIAIaJgwWc-RQ625tgQrSdHCsWRdGnqUfzzv0VboofpPjyFKzcqmpVlfVAQRSAb-Knl48LfwLuPRFhDWKTUZSmCJNNFBJu10OhxEZgkfiDDFnR3Wppa6dtiHTafPRHUCbVwX4WZ7R8j4Fti9BEUjf5J8n6M1iqxrxcEYiWTamg6mrckoFi51ym34ffGHnQHu8evlldcg72LjksJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltEwpfw5wbN5KwzlciwwJAefOS9-P033l7d_RcGD646SG_vl7x2hW_qXvgh0efqNUTQnARQs_-R9DQMsex1-OM3lrLEYFqlCvxajzTJU2-A0hI5bW8epPtKYOyXNaQPs1B8MPbSKDbI9MrdC0A9frDP-DUkY6GelVdvVkwtR0hF3DRRirPimt0R9MHsZg2VEGSOQ-tj-097FaSkfSWZ72t8H9n4EWBUTBtAueU1V550TrESxG8vRYDzXeA0ODzURc9tLGims9qV1LIIU8a3j8fEgdtqh4GiWGfbbHRDlGeb53Kr6TsifLqIGSzqjNMP3EpEjmLjk8yrfVXBURB9TKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBmwwqEjgnhUNMu9ZAhPuqGdGcVYZMy0u6NinwUuAvmRRjnq5LOi4YPmLM3eyFHYTUJnHYlX92WtgWvLZjmvRMpyRBLR0ntWkPj5BmNXaV52jZ-iCtmoCGV3OQV6qdo46mcTnAbpru4ttVJan2pDHUzDH6N4q_fMrvvXKJTy9hzduXH2oHiNj7lq32ftFTCLNrvEIKqNSwlQHwik2LJ07Zvbi9T9_l2TPDI_WdvBBMX33SvO6UQZACQ0HTHaCkQRwB5cpgQ_WDtdjgQ5Pa5r9wVLiDboYnQtRLJ9I1rSJrbeXkqBYLwXs-qhFizLLhNao-af86ifkPFp5LKt1qiEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfXQsv43pGnbqmjKmPgRMDBjJX6pES83fh1X-Br4hIilEr7yvnQOuZVOf3B2K-XXNvaHWE2ou-bJ0fM3r1lCIxNeBd5SBZNvmjFsaL4jzzESHFnr_vXzjwlF6zy73nng0PM6ino9OjFYTyRkMWRM4zR0J7-vhTKpJtBZpWOEkC7okhkzuCNTJkDOaaMHJZUUi09zlnM8mAAAiEurqGMAGEiYRgLWhnVzLTkpq7idV_sTicyZLCNJxGwOjIXi10dscOsU_X2AKDT-zmZsK5k76DLQ_Hk6khCJGUP-Vb9kMj_ZAMnfCkX2pNYR4eg6v3QZvMHaTJiPZcuQpDGf46xiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fr1kqS3d4pI9kDb4ZPAJfe7wOvHvam9M642mKgbRRVnQIDy8pub24fOM9CEDf2lH5XU0dZrwCkhVF_DvLwGVunJ34s6H486LAEsKzh4YUggUtqEqmTvSNtMV9bw6bNQF90BJIrsT61DmD1PY8vDan2KC_1JrOUMBAulXkFbScIApjaqUJ7LQZddWlh5uwlD3ps4KLkhU1x3XL9bnlvYi1GwY3n1IgFDYfachLxq4jmXJurzzsSp2IF-pvVH7iFaNW-FcpCLg0a1J0wPHadctZsw_DsBScp9bvn0a8kgZKiHn0QspisxvVJs-oIgJ1ivRg21DtHtwSwoD6SlzE6iLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJySvwo4EalRhTM9RO30KVcNbhVsjPq8bbx3PsD3M9avVEX6v11ewOhaNPr_h1zZFTGAg-BRiRdYNztDEEtexczPscnxu0huUw6Y6Cw29aJds8jF7nLkWdMNG13eGbDyejIFmyodrivWSYl55_4ptxu5Z_DTbWcLzAwrOxEw7U3y5qYFD2Ckt_WmaylHkzLUsXZn_RxfejACud--yIQzEqWHb9QE9UFp8U1RlWLuhq_KppS5bhnoubeksuzQ60vyCh8wz3L7kDaHoSkLcBhgGEJvvT8gsihg9Dm6qOeI65z53XkNbyCdzZVBEUlGjmdp_mPP5A5MUITKqHTcEMDdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3IiKeRVypev0tYqzyU1KM0LZKjrXaSAt5B1z-Nd4pcbSiHrIzeUptoqT6e8M6U-jnXD0c6Phiu93mYEbX_qC8JA-gAphNnooHp-Hd-cEW6MhYnhUiUtlqyxIK-7aCu7hs9tzoW47qHS8NivJ5bBb6FcOirsj59cRkW6iBPcfjf-Nal_vFDyot11edXbfIuY57iyBTh0FpjymcmrA8FAUWouNbOSb8lSTrpYukQ4AqSpE5HEMdtFi0JA4cC0MULAH3ZtOIsXC77JZv4lHuoUpF-mruXiMtTzyqSghtIk3jAYgeHKExTNpEfGUGPsOKL6flEL8C1oBPtRNJ0EraQipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixrUkX7-fad3NNSq_viml9UhNlYzUY0QYLnOO9nsjFX_xlRRQjzB6l7TlguTTHVmf_NWCsK7OGtDLZFIqPUFEXgL-oGV4ppdj3T8vyPNqQubDlcb6kkSgVi2o5PSZj5yCGf7fr2poXLYcZLvdZ0dK3FEVSWd3vOEOgK9izgqAa-kMACA4DgJ4V_fh4ZdPwdRr79fyMQOwvUjtUBzE2_T-IsftsQSJGMFnkCMdz6k6H_tckKfImY9Ka-MHic3q6w6qXiq1AOznCvASxFrrYx-X9h49ng7onjidauclCPGuIzS8rLkM2kdd6uKWNrTMKVUOJi8nUH0XRt0lTrKYjUfSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حال‌و‌هوای وداع شبانۀ مردم با امام شهید در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/666658" target="_blank">📅 01:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666657">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLPBxdOCDyPWZDOI7RA4mgWuWakoMGnAK__MZmFhuzder69wCiKdgl_RjvOZLAKqA78W-Uh6wrkMZXx3dCj9fz18QTojjRixAiUiUGNnXk-G27PCS8AkfrhTVvH4xU6fcn7Sb39UAsuWSQ4vsDoARImo4cKuRLKp4IeuowJtJP76T-Ozpaoq5SsB_QgXzA70WEiv3uzpncZXggi6t8eb3ETMO_5QqENy7A409kx9aaTPHdpzVoWTR6vTCykMAQRz59NJLy4BeqNfvhl3nTc4eZXIyZkCUpZbsTR47APRICInOLE8hv0OkIhBvF8_Zc-m-Fdl7chcIVV01zAR0g46vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اللَّهُمَّ إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْرا
🔹
مراسم اقامه نماز بر پیکر امام مجاهد شهید و شهدای خانواده ایشان
🔹
یک‌شنبه ۱۴ تیرماه ۱۴۰۵؛ مصلای امام خمینی (ره)
🔹
شروع مراسم از ساعت ۶ صبح
🔹
اقامه نماز، حوالی ساعت ۸ صبح
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/666657" target="_blank">📅 01:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666656">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4K72GabFo1ub8udraDi8JyI6pagHTqyswfJuHT9Xnrmzaus7Njs8wz4hiHaWUuwYBqXm9nsc_EzXF-EfFVUEXcwb1-QKq1jhmm_B1NlkzfAtGwTzer8LYQCNcYjJq_IHrEDiHvjr5zFHF5GNR6L2_lFKOZk6XpPX658LOJPXU_A_gvq6ybWlAfv2xnPNBschSXDbFyHe1J6ALwWyReFZtxfxoH-Yd7GvGsWspFPafHbRQ5HTfTVcWQ6zj9ecuVc-iuzzNn5JEohER5nb70CAhMiWjGt_QjAKRNHd2Tmi2mVn-oAXKST6jFbG5pgL4PvvDgLh84NG-BjifMoQNbVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم‌های سرخ انتقامت، از دست ما نخواهد افتاد...
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/666656" target="_blank">📅 01:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666655">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10ca3a6d9.mp4?token=LdR23wCfnpsqYrsALKUG-UtR-HJcIIC6kx__-K7SIBQmellBP7CKd8RLrPoK3JPwTn018fDv3nzjUdtvB1nKE38T0uZMddWaN4_fQ99kbOX9EXNZ-NJgd3PuR0a884xC-IvugVmuRMewSLayxmrROVxg8o5tAoQUjSPvkFdpllEbtC0X8FSOh2he9CwViNREER3CKv0FIMSGldgUf7Soj_cuHqozJG-F92Hr6y2ldcGY8WBs5pdf-E4Jf718uf0h3t0QoIplr_eufvf9J7DG1nQlG41rBS_e4cgpGVX4aiDTcr_3MmkmQhchbMY2wWLcjSivnJSEP4j4Zew8sC55Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10ca3a6d9.mp4?token=LdR23wCfnpsqYrsALKUG-UtR-HJcIIC6kx__-K7SIBQmellBP7CKd8RLrPoK3JPwTn018fDv3nzjUdtvB1nKE38T0uZMddWaN4_fQ99kbOX9EXNZ-NJgd3PuR0a884xC-IvugVmuRMewSLayxmrROVxg8o5tAoQUjSPvkFdpllEbtC0X8FSOh2he9CwViNREER3CKv0FIMSGldgUf7Soj_cuHqozJG-F92Hr6y2ldcGY8WBs5pdf-E4Jf718uf0h3t0QoIplr_eufvf9J7DG1nQlG41rBS_e4cgpGVX4aiDTcr_3MmkmQhchbMY2wWLcjSivnJSEP4j4Zew8sC55Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضه‌ای که محمود کریمی به نوۀ خردسال رهبر شهید انقلاب تقدیم کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/666655" target="_blank">📅 01:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666654">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5579cfd64b.mp4?token=lcPnJ1lSxek09LXwKRWaacHOPag5W0BZ37JJfZF8P79mXDiskjJJqwX571RsIlDlM4wn1boif2F0d4lEdLpVc4BnZXwy4iua10I9Hopckkk_-wipqUu-azblmRSwcUkl7N3-ZOUqH1xJ54ZCOU1AG5cz9AlGqV6SHFh5foefk-z7dnLxw_oC7VSDQ1leWh__459hAm9XJkjTTJkjk2Cz8Dx6yXRuQVj3x4zDIp0_MuWOyH-Zkf33qbTDw-DEarGqLu-p8qXfA_GRV9aEajgmOXVwLY_GLkUXSv3uSodFT9ejZCMuM7B9LMq0w1_qctcfAUys7vx44V-Fg63n9WbYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5579cfd64b.mp4?token=lcPnJ1lSxek09LXwKRWaacHOPag5W0BZ37JJfZF8P79mXDiskjJJqwX571RsIlDlM4wn1boif2F0d4lEdLpVc4BnZXwy4iua10I9Hopckkk_-wipqUu-azblmRSwcUkl7N3-ZOUqH1xJ54ZCOU1AG5cz9AlGqV6SHFh5foefk-z7dnLxw_oC7VSDQ1leWh__459hAm9XJkjTTJkjk2Cz8Dx6yXRuQVj3x4zDIp0_MuWOyH-Zkf33qbTDw-DEarGqLu-p8qXfA_GRV9aEajgmOXVwLY_GLkUXSv3uSodFT9ejZCMuM7B9LMq0w1_qctcfAUys7vx44V-Fg63n9WbYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ممنونم اگر نروی، میمیرم اگر بروی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/666654" target="_blank">📅 01:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666652">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab6c85366.mp4?token=EDyoBbj6OPg7YRiqffvzTSj-Ek5mPdr05HXWNcrFy3ZWfqBB87pMMcRCQyzGTH4vDIruhxvmXD9eIHenAd5erpYs-NmJk9g3arWVhNeDphDcf6Sf1mjqld2jJsDl364oUtosWphFSYkN_C3O1oN1cdSScIsC7nYMDIasJBQL3xidnoY4Z-KfEhGatejf4EN__-4ZSg3QcIJ7SdTK2zzdprLjZOFgr70r8AuSOfsS1gwwwIL3Fi13lzzbZL-W6zuUO7wollvW0xUKVA_hqwPzuC4rCo_ClRMP-WfaEKae2y2ahB_jxMg_OZtz3k0N9sGmBB20uqpPC--AqI5fW90VDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab6c85366.mp4?token=EDyoBbj6OPg7YRiqffvzTSj-Ek5mPdr05HXWNcrFy3ZWfqBB87pMMcRCQyzGTH4vDIruhxvmXD9eIHenAd5erpYs-NmJk9g3arWVhNeDphDcf6Sf1mjqld2jJsDl364oUtosWphFSYkN_C3O1oN1cdSScIsC7nYMDIasJBQL3xidnoY4Z-KfEhGatejf4EN__-4ZSg3QcIJ7SdTK2zzdprLjZOFgr70r8AuSOfsS1gwwwIL3Fi13lzzbZL-W6zuUO7wollvW0xUKVA_hqwPzuC4rCo_ClRMP-WfaEKae2y2ahB_jxMg_OZtz3k0N9sGmBB20uqpPC--AqI5fW90VDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه شب‌های دلگیری...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/666652" target="_blank">📅 01:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd59919123.mp4?token=I03Tgv956tIXwRQnHpeNVKaMTs7907Sana3_RM2N6NbMQzs87Ak8Q9GwtiHQ4ZcEHe6nJ61rVai_u1aBdyLNUbJzhN9VXWrsUd7-E1AajWQJu1a1WVOv_kMrfx_PimdZ7DJJhVBak2PaiZBsN9lxMOa3RJUQ4zF94MA9sbi2OcrwTHzGgr0Qyaqe9iPV8VW9tLTTZott7o85iK813nQvMlWGtIK9ZzIDK7up5wOlqJtoAoAhTx-gyFGHOWushP7azfHln9zOx0J5w_urYdfd0RQvexpfSl1_boOVoQcdcCrmxoKTJVcp3768Y6rNAoyy3fNFXbkGdRquC9E05nXbIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd59919123.mp4?token=I03Tgv956tIXwRQnHpeNVKaMTs7907Sana3_RM2N6NbMQzs87Ak8Q9GwtiHQ4ZcEHe6nJ61rVai_u1aBdyLNUbJzhN9VXWrsUd7-E1AajWQJu1a1WVOv_kMrfx_PimdZ7DJJhVBak2PaiZBsN9lxMOa3RJUQ4zF94MA9sbi2OcrwTHzGgr0Qyaqe9iPV8VW9tLTTZott7o85iK813nQvMlWGtIK9ZzIDK7up5wOlqJtoAoAhTx-gyFGHOWushP7azfHln9zOx0J5w_urYdfd0RQvexpfSl1_boOVoQcdcCrmxoKTJVcp3768Y6rNAoyy3fNFXbkGdRquC9E05nXbIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا: این لحظات شب‌های قدر جمهوری اسلامی ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/666651" target="_blank">📅 01:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666650">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
کاخ کرملین اعلام کرد: ولادیمیر پوتین، رئیس‌جمهور روسیه و دونالد ترامپ، همتای آمریکایی‌اش، تلفنی گفتگو کردند
🔹
بر اساس این گزارش پوتین در این گفت‌وگو روز استقلال آمریکا را به ترامپ و ملت آمریکا تبریک گفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/666650" target="_blank">📅 01:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666649">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c2c91744.mp4?token=DHcNoJKNCUA8_xgl3SKreTlmCawiGhKUIes74EC_t7PXGp5pTjgVeV1PXaszOLljxzezhfMdzAMA8-0uV2-Y6zmxSK5iHzKHmHcKvWqo70wnwTCOHnAWW3AqJxp4VvgkxVWicxmG9wZsejlHF27rNkbDZYM05vJYhQ9gf4pWCfJ-_rVl0j_t0A5w8IQJ91diBHjEkK0JH9dnqtltZoSQqddBezR4uadBQAU7d6FZsFwQFejsS3VwAWHWOMHrYh04nleLeefDuhECDTpmD7UPNGrj7LnnfWBubHHAmLnc5pFq2yYNXbYIRkHpuc-0rQv24X2FKzaZl9LmkNNfC3-rkIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c2c91744.mp4?token=DHcNoJKNCUA8_xgl3SKreTlmCawiGhKUIes74EC_t7PXGp5pTjgVeV1PXaszOLljxzezhfMdzAMA8-0uV2-Y6zmxSK5iHzKHmHcKvWqo70wnwTCOHnAWW3AqJxp4VvgkxVWicxmG9wZsejlHF27rNkbDZYM05vJYhQ9gf4pWCfJ-_rVl0j_t0A5w8IQJ91diBHjEkK0JH9dnqtltZoSQqddBezR4uadBQAU7d6FZsFwQFejsS3VwAWHWOMHrYh04nleLeefDuhECDTpmD7UPNGrj7LnnfWBubHHAmLnc5pFq2yYNXbYIRkHpuc-0rQv24X2FKzaZl9LmkNNfC3-rkIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اباالفضل علمدار خامنه‌ای نگهدار
🔹
نمایی دیگر از فضای حماسی و جمعیت باشکوه مراسم وداع با آقای شهید ایران در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/666649" target="_blank">📅 00:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666648">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4225985517.mp4?token=V9cHEbAU5Dl3cFg223xMX2NwTd_qu_jIEPsc_xPOFmH7j7mLr0AAJ82B9kAqKC74yKbD2rPkowcLZTTuh7HC_twrAV8N7hJpIw6hBVVeLbgq1ajCbEf_dYQiCPT4kpvYDP7HbgsWamADwj8Kr8DLySK0YnZwOsJ7uE-hih8Vsm3pGkGnq1uGWkbxH6A3BSGdp7eS_zfMf9qgFPXfzCazHMreK3-yJ0-X0lZ_LiGHlXOh4MbrKp7aj5EOY0Mz74G9lJpLJLn4HuuiYlchzqmhWsQ_frDAELIQwarplecHuuDm7GcH_6vmGKnVyVeChLpPTcZt6UVFGSLH0fgHHojIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4225985517.mp4?token=V9cHEbAU5Dl3cFg223xMX2NwTd_qu_jIEPsc_xPOFmH7j7mLr0AAJ82B9kAqKC74yKbD2rPkowcLZTTuh7HC_twrAV8N7hJpIw6hBVVeLbgq1ajCbEf_dYQiCPT4kpvYDP7HbgsWamADwj8Kr8DLySK0YnZwOsJ7uE-hih8Vsm3pGkGnq1uGWkbxH6A3BSGdp7eS_zfMf9qgFPXfzCazHMreK3-yJ0-X0lZ_LiGHlXOh4MbrKp7aj5EOY0Mz74G9lJpLJLn4HuuiYlchzqmhWsQ_frDAELIQwarplecHuuDm7GcH_6vmGKnVyVeChLpPTcZt6UVFGSLH0fgHHojIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای ورود عجیب عباس موزون به بیت رهبری برای دیدار با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/666648" target="_blank">📅 00:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666647">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3751ef30.mp4?token=p5fN4YZvlFEruUf2Eao14fjOx60F0XgEfjmng3vwtY-Dl5xIBXmTRzbUKKnKAD1MV1_tYaw7ZhvNL_k5Em1HZbc1hz0MtquHrbccB9_QnBIb-SQcREwhkXUbzdq0ngGNXS7rBjgR9g_eJRlrTBB3b5tR3GYuuiByjjR7o9wTxjfwjtQ2UKb1A_E6fuiOzae6VJoqfIEVkjSwRvAgpEL4YeWiowGY2DrtQGrb2jQAhTbeAGokD-12KO_wJZvaMW2RilWkbB9rUIARe0B1zBfa704Xd6vV7MCdgFUe_57SmV8pWi_t4VWHm7W1v3xrsdTtXf8FCi6V8vWG7wYa49wzfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3751ef30.mp4?token=p5fN4YZvlFEruUf2Eao14fjOx60F0XgEfjmng3vwtY-Dl5xIBXmTRzbUKKnKAD1MV1_tYaw7ZhvNL_k5Em1HZbc1hz0MtquHrbccB9_QnBIb-SQcREwhkXUbzdq0ngGNXS7rBjgR9g_eJRlrTBB3b5tR3GYuuiByjjR7o9wTxjfwjtQ2UKb1A_E6fuiOzae6VJoqfIEVkjSwRvAgpEL4YeWiowGY2DrtQGrb2jQAhTbeAGokD-12KO_wJZvaMW2RilWkbB9rUIARe0B1zBfa704Xd6vV7MCdgFUe_57SmV8pWi_t4VWHm7W1v3xrsdTtXf8FCi6V8vWG7wYa49wzfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ ایستگاه مترو شهید بهشتی ‌و سیل عاشقان امام امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/666647" target="_blank">📅 00:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666646">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JR1dHmg8GWDvD78yBG_6JX8n1BQUMWmNqO532inGenEgAvx6b962VSudGJPZAqM8K5H0v-lcwfV4mse_F2hJxXOuajjdq1LPTlWG3uDje28U3HKreXQDu3SdBhxBF93OQxnpg4ipjQu80wAQYx6j9TK0O30KpnMVvu8sATJB_yR0HBYoQxa702e52gud2Qn-Dph8vGQKhexx6dOXydijKNONKW92ZcjFdN2aYyA7eeV_CmxBMkhxQQu0ADeoJQWoWlK1xYPH3SHi7ctiMSkj12BD9uxv2PyWuGUST4NPk6YCQCPXV1P18cFfIqL-uGYXYDfGUmEH3Zxtey4PqeLTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرمای جهنمی در دیدار فرانسه - پاراگوئه
🔹
دمای داخل ورزشگاه محل برگزاری دیدار فرانسه - پاراگوئه به ۶۰ درجه سانتی‌گراد رسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/666646" target="_blank">📅 00:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666645">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb608438c.mp4?token=srTSZCbdfrHIZSJGp8B3vJVrK0F74YIcM4pQroRY4JqHN2FFzt4r5AsLdGzYvHPUJ1x3YIyCVjDROmC9Nx_16Iqrnsax0Qg1we9XN5ul_lcUT-TLXZoYhPWY_N487Novxx2t640BQyc7XWqEoNs834DpDcMbHGh4dvUuJ8OIbjKwL44cn52hUR4p2PWKlZ97lS_cICTwYeZjtg7agUtZb3FjG67YldMYe5ZfGsUfQ4NYO2L00OFMTL0FnpSkosDPimVGAliiaDCdKYj7rsdqwSkl8nT4k6T3lCNs4ds2zckMUdgf_iY0WLn6PSYc8dHI2lTB7hxNzZothVaBiJLTGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb608438c.mp4?token=srTSZCbdfrHIZSJGp8B3vJVrK0F74YIcM4pQroRY4JqHN2FFzt4r5AsLdGzYvHPUJ1x3YIyCVjDROmC9Nx_16Iqrnsax0Qg1we9XN5ul_lcUT-TLXZoYhPWY_N487Novxx2t640BQyc7XWqEoNs834DpDcMbHGh4dvUuJ8OIbjKwL44cn52hUR4p2PWKlZ97lS_cICTwYeZjtg7agUtZb3FjG67YldMYe5ZfGsUfQ4NYO2L00OFMTL0FnpSkosDPimVGAliiaDCdKYj7rsdqwSkl8nT4k6T3lCNs4ds2zckMUdgf_iY0WLn6PSYc8dHI2lTB7hxNzZothVaBiJLTGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله اعرافی: رهبر شهید، ایران را به یک نقطۀ اقتدار جدید رساندند و معادلات اقتدار ایران را تغییر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/666645" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666644">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/666644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/666644" target="_blank">📅 00:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/666643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666643" target="_blank">📅 00:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666642">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2329cb39e.mp4?token=BetVlPdzGUeCCz2ZKbLMoM3q4KFJXQXXJagUPriOrGtXu2csYZWpWmLsS36dcq34BS7u3XH_cJbQO6iv_xb5MHsPNremMk5G31kwROKmRo-FB20trE7c_X31YEYwvqQdXNtaavHdPt84iKOPqqQ3wSkYrTzCHuF9It9ksOXIdirNLSgGgggnM-J8clisLAQiPS3w_Q3-Y8I2fF9a4AdIF21WFyTbxmG6W7rPdkTYmCIfIg9WAbbu84O-sTsDA9uM9gFKWF15tZKORqB61t1IYSSIjpLYrj2ekzylIx64n-Cli74XXzVBS8uT_AJJS1UYczR3uJXNmNR6by8jYGnQgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2329cb39e.mp4?token=BetVlPdzGUeCCz2ZKbLMoM3q4KFJXQXXJagUPriOrGtXu2csYZWpWmLsS36dcq34BS7u3XH_cJbQO6iv_xb5MHsPNremMk5G31kwROKmRo-FB20trE7c_X31YEYwvqQdXNtaavHdPt84iKOPqqQ3wSkYrTzCHuF9It9ksOXIdirNLSgGgggnM-J8clisLAQiPS3w_Q3-Y8I2fF9a4AdIF21WFyTbxmG6W7rPdkTYmCIfIg9WAbbu84O-sTsDA9uM9gFKWF15tZKORqB61t1IYSSIjpLYrj2ekzylIx64n-Cli74XXzVBS8uT_AJJS1UYczR3uJXNmNR6by8jYGnQgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باران‌های سیل‌آسا در چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/666642" target="_blank">📅 00:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666641">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
باز هم نقض چندین باره آتش بس و تفاهم با حمله توپخانه‌ای رژیم صهیونیستی به شرق اردوگاه البریج
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/666641" target="_blank">📅 00:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666640">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e9711db.mp4?token=njezoSGEZ93vxyxiLW1CVkqJxXjlYTAWuNc5zm5GTtaGSXHILhXRrNb8rkmiPVb53UftUOjT81C7zFkZK8_grK5QXVY9S77mPuKBaupBhFRq-Hu2YIcMVinea5I-LHwZaZjuyhdPou22-visdKIJN6xoIQVJ6PRSesyvRYTrOl3ytAJm6j6_4EnxRtOZhlDCuxzlWMhSpuIuNv37Bdj8Yfp8nmxJ9FplYr6-pDeG580rpXVhtsBvvGDyMFGnmBaWYlGs7BpbRGQgOuQyxWJ9gTiVj1yQ6VcidW5H0XRYV579CetE8GkmTU83zdXaIZGzHj8cD05BWQOZ2JqLSm1MpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e9711db.mp4?token=njezoSGEZ93vxyxiLW1CVkqJxXjlYTAWuNc5zm5GTtaGSXHILhXRrNb8rkmiPVb53UftUOjT81C7zFkZK8_grK5QXVY9S77mPuKBaupBhFRq-Hu2YIcMVinea5I-LHwZaZjuyhdPou22-visdKIJN6xoIQVJ6PRSesyvRYTrOl3ytAJm6j6_4EnxRtOZhlDCuxzlWMhSpuIuNv37Bdj8Yfp8nmxJ9FplYr6-pDeG580rpXVhtsBvvGDyMFGnmBaWYlGs7BpbRGQgOuQyxWJ9gTiVj1yQ6VcidW5H0XRYV579CetE8GkmTU83zdXaIZGzHj8cD05BWQOZ2JqLSm1MpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا: وسط جنگ جهانی در میانه بازی‌های جام جهانی، در ایران یک اتفاق تمدنی درحال رقم‌خوردن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/666640" target="_blank">📅 00:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666639">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769f973c05.mp4?token=bsAP2C5gs5c0c1nYeNfC5iOr386Z8-c9m-Q3vphMjnw--LV6LZkGjkzg5h_dkgie9uqoDz7ZrE6vi0XNPHezxwtVD3dRF8xKnvBg8820idm5PDw0nsjuPQpmEE_X-feblK5IoLxk_9dYaBVcLr48yhe9l9smPXrsjwMU-NsrSqNez5l4n1mjIckfhPYJpXDoo_GjBDsdMraOzpXNXEom0J4ggMVAgodZ09fY2bkon4JUPHN3p1jql9W5klRD2NtjbOTk4OQDArasu6TjcSsN7KkdRtUP_0aoQlLTS3ccr_zI-DOmB9tcN1uVCs5wJywMFNwIPvPWVcHqq_Vxymokdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769f973c05.mp4?token=bsAP2C5gs5c0c1nYeNfC5iOr386Z8-c9m-Q3vphMjnw--LV6LZkGjkzg5h_dkgie9uqoDz7ZrE6vi0XNPHezxwtVD3dRF8xKnvBg8820idm5PDw0nsjuPQpmEE_X-feblK5IoLxk_9dYaBVcLr48yhe9l9smPXrsjwMU-NsrSqNez5l4n1mjIckfhPYJpXDoo_GjBDsdMraOzpXNXEom0J4ggMVAgodZ09fY2bkon4JUPHN3p1jql9W5klRD2NtjbOTk4OQDArasu6TjcSsN7KkdRtUP_0aoQlLTS3ccr_zI-DOmB9tcN1uVCs5wJywMFNwIPvPWVcHqq_Vxymokdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین دیدار با شاخه گل‌هایی که روایت دلتنگی می‌کنند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/666639" target="_blank">📅 00:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666638">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa61908915.mp4?token=gOe3FGXkL0YT3oBxDINU27MZZEzMAo-K7fOYAzBJwdjexF4BaZtUeug6g01I1sN_S97Edo7OFuKp-lJVVrp9Cq2C_s8GblTaBgDgf4uwAICXc3XI4QnDOXqVCn_-VY8QXAtE4EZr22KnquiWzk0j0b3SOgKUosetPV8Tp52MuGCOKGXb7m_PCSwHuBwE5tKT2idpieTczxt3hIh7H8KeUritC-bL0uZLBbtAHOcHssd-cbvjpavC3ZFOJ27h5geRm0R9qOIbroIxVuuCEju4c2GIRM8nK18AdkzhK48TN92r8cLd_zd6ufrr8jy5VPhqiQ5tE8h--hezFoAPtKxo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa61908915.mp4?token=gOe3FGXkL0YT3oBxDINU27MZZEzMAo-K7fOYAzBJwdjexF4BaZtUeug6g01I1sN_S97Edo7OFuKp-lJVVrp9Cq2C_s8GblTaBgDgf4uwAICXc3XI4QnDOXqVCn_-VY8QXAtE4EZr22KnquiWzk0j0b3SOgKUosetPV8Tp52MuGCOKGXb7m_PCSwHuBwE5tKT2idpieTczxt3hIh7H8KeUritC-bL0uZLBbtAHOcHssd-cbvjpavC3ZFOJ27h5geRm0R9qOIbroIxVuuCEju4c2GIRM8nK18AdkzhK48TN92r8cLd_zd6ufrr8jy5VPhqiQ5tE8h--hezFoAPtKxo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه وداع، قاب‌های متفاوت از حضور بانوان در مراسم وداع با رهبر شهید انقلاب در مصلای امام خمینی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/666638" target="_blank">📅 00:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666637">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
استان میسان عراق چهارشنبه و پنجشنبه را تعطیل اعلام کرد
🔹
استاندار استان میسان عراق روز شنبه اعلام کرد که روزهای چهارشنبه و پنجشنبه آینده به مناسبت تشییع پیکر حضرت آیت‌الله خامنه‌ای در عراق تعطیل خواهد بود. #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666637" target="_blank">📅 00:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666636">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
المسيره تصاویر فرود هواپیمای ایرانی در فرودگاه صنعا را منتشر کرد
شبکه المسیره یمن:
🔹
با فرود هواپیمای غیرنظامی ایرانی و اعلام نیروهای مسلح یمن مبنی بر ادامه دائمی پروازها و مقابله نظامی با دشمن سعودی در صورت تلاش برای مانع‌تراشی، رسماً نبرد برای شکستن محاصره فرودگاه بین‌المللی صنعا آغاز شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/666636" target="_blank">📅 00:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666629">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qe8dR9FWuuE8ZJT5DnZr3qAdFx-6_OG1V2B3IXMjn2awfw4D7qam7P_8LOKPyBDtIXPmbznA0KY9E-K7zsOpUaSF87JdLX_jGqLScyLNt6L1OMuItZzPX-kmjuxAcGQ-auETkxnQqsjxRuns26kVRy2vJJE9LxYamb8gLG2zlqAVxOtI4NuewMMb0n6IG4rJvNu6WhUb8DOiBGrH6Dt4JLpP1X0XTVtKfkydJ79Wcg7IUrdu3hMFbSHAJV7j2gdrOSKZWdtPqgNKdZYYm1zbuJgd_xX5Nz6Zgks56xV4Jtk1id7ulcDFbpMkqgb6ZEIGXou5UzQkciRUZassItG7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kq6TVoVQyV0xrhV2ZX0Xj-1CQ3t1mTdVjfo0kHEHYmebbO2lY3eZZ3szos9fewX6wbWTpsW6rZuqujeCBHgfZyjnkNWtI54b21Zz2QmH-WgT4eFfOM4bTiMH1eaeSC03gIH_ZpRoZS-aEZvcP0USVFx6ZJSwV9xrTxuBnBdfkkKZxyWG7RmbzhYU94BDTjHbWYSLDEfFpWRLOzIzBoKS2Mvk0_bPsmEK3KDgzF5yWMlzSUnb_3Bi8yxIS2XEp9fnr4uBBCW-ImxFZWzax2Vr_5TEpAk5Qlhx96DK_SUwQjzmBboD7ihe1Jjh_j-NeSdLop9iM1jc1kjRrZ0T-7IzjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0-n36SYAzG6PF7WebU_CJ1xZQGvoZBAPAMYDAgGEZORx2km2sw8JqJGc98fVbqO5maTpsmmawJDsuXFFhgaSO3rNeaPNPN4FOWCrG6sET5IAFkOPsAw4YsXoCsi8Sie4a655g-S2LjLN-y83BbTzQMQ82PEFJgymsT-Jr_gY7gF_bT08KHY1Pvc2z6-b3REFQ3_Ne4pbbAZKadU8KUqDnbabmpKJOiI5a_Q07J4c4bOy1oJQc-iRenayPfDN_ZyksVAjMWNRnOK8-aXbsKcisLhbgziAbwSEWJqguofrymSgfBK2aHAtPxIn3soPvgaVeTwKMT4MBe4Z6YEPuuSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSnS1psJorHUFAoKx7jQvBGJvVJed46h5la58dbW7qv6CFMBd5GdGb4ZxiFWEXOlvqZ6j1rwJ50EYJM3RTZhvi_-d_Zqe-4fbZXT0jhQqWsHYoa8i-YuDiej1K-N4zqpOdc0p_Omskkc3PMu0l1G-rI5P26KmYQlk50A2XnUtP40ASRBu4vSfX8i9ndHb9boDiqZArxS8Cki5e2JKSIsK6oCVHpEnO506mSt-rfMRtZB2ABU7Ynm-Ajc1AScTBe3_lvaIQwTD93fTBtyaXytj254p0wuGyU41El9A-1H6cYEuRNlF-7nyHWA7f9jBiTYjQOdqAW7phvIXy8jTubkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ri6VMe2TZch9aJFE2WMbHNzITOb_xLjdIyRpkVTkXZPMf6kHYxUTFxJfuvZw9TzBNaH2blBcF20DUXYLuP4jjD_Gf9yv91D4gOywMyQj-K3CijtB635JLOAbuc2CqNk63vm-eEbeIkqZ39F_JJ0UlKrrh40qVwmi8ZqPaaqSXl3DrZJOp_yaQkmetNmb45hS6RG-o0bUrOS2F2o2h91_SU49D8vEuOQIzFplcZ_rW551EAHQ5Ri18rA9p8_t52ogmu-WLERkkHa3P_5cftIo90R58R7wRXF5hn8hO-f0jOIpZVRdEaiKWtYcUb_4P8_is2Goqe7tKLBh7fHmxHCTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tF78CnRObChqp2f4QpsHGaDuIF_19jLxzjyysfEMMPGqSwe810UTsr4dhNFuE2KZ0Uy6O_AqnjemI38CPgQHDVZfq7Hn5UyM8rgHBuq_ThNFvAboDqJ44I8rq3uxCYc7EyNhFaK6OIRg8aewUlUP6UqUtpt4UVlw_1_iXi7iW6M7YOBOWOLWLTVxdUWEidQIHhEplLRJ-TQD1HOUY4eFovo-G_Oil8BPIIVHyzqcKbnEDj9wjFMWRGOFklxQEkFODcy9mtVhJhVpV7bOi-0a6QFviP1dXR66MZ8r7Hj41QpaNovlt0lpb6dB6wP_ZMh3tzFtqkYJivmCuA0UywYmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0-n36SYAzG6PF7WebU_CJ1xZQGvoZBAPAMYDAgGEZORx2km2sw8JqJGc98fVbqO5maTpsmmawJDsuXFFhgaSO3rNeaPNPN4FOWCrG6sET5IAFkOPsAw4YsXoCsi8Sie4a655g-S2LjLN-y83BbTzQMQ82PEFJgymsT-Jr_gY7gF_bT08KHY1Pvc2z6-b3REFQ3_Ne4pbbAZKadU8KUqDnbabmpKJOiI5a_Q07J4c4bOy1oJQc-iRenayPfDN_ZyksVAjMWNRnOK8-aXbsKcisLhbgziAbwSEWJqguofrymSgfBK2aHAtPxIn3soPvgaVeTwKMT4MBe4Z6YEPuuSLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اولاد حسینیم و خون‌خواه رهبر شهیدمان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/666629" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666628">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5f384d1a.mp4?token=vuO1RR8IOOWO5w_IdsxHcurZLijh_yOyIO_PRDFlKfktsvqVwHWbu-ashvH3ALkti-mHjQa9ZZ1pw0LOYDRlTOutGrfcENAZsLVKln9JLTe6wjBs2_xNIeU2TENxWobb2SKCdL4pWThwddFvWJ9cm-55AzhfVY-X3o-c-11lzCo6UaAaDMDjS7nnUv_0tbv_vRc1zGLT3VXrRIlxbLH2JHKQrxE6wOuFh1y06y2f0N4DKJZuB10PTh1_lTyLjUQJQi9MHNdrjkeqoHGvR5yXjB-am_2yvgTS9T3flfzikmxrv9X85swNTo2Qt9NYMDihk-KpXBydhgY84x1OHz_ooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5f384d1a.mp4?token=vuO1RR8IOOWO5w_IdsxHcurZLijh_yOyIO_PRDFlKfktsvqVwHWbu-ashvH3ALkti-mHjQa9ZZ1pw0LOYDRlTOutGrfcENAZsLVKln9JLTe6wjBs2_xNIeU2TENxWobb2SKCdL4pWThwddFvWJ9cm-55AzhfVY-X3o-c-11lzCo6UaAaDMDjS7nnUv_0tbv_vRc1zGLT3VXrRIlxbLH2JHKQrxE6wOuFh1y06y2f0N4DKJZuB10PTh1_lTyLjUQJQi9MHNdrjkeqoHGvR5yXjB-am_2yvgTS9T3flfzikmxrv9X85swNTo2Qt9NYMDihk-KpXBydhgY84x1OHz_ooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات حمل‌ونقل عمومی تهران در روز دوشنبه
معاون حمل‌ونقل ترافیک شهرداری تهران در برنامه پرچمدار:
🔹
در روز بدرقه خط یک BRT مسافر پذیری ندارد اما مترو همان مسیر برقرار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666628" target="_blank">📅 00:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666627">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va4z76lR3asxCwhzScyUzHzXDSFWblMLJFlMfcYHtMuZH7_PfKFK8FvGgCdbISjZgezTr3imyNhsdLw2MsHUh4c-CwCRaTEfqJ5weWRIAiBU7YcovLCa_SsU-8p4BcQ_x0TbZRpPeJYiqE4wXr4b5Kirg-zTpN-G758OjAe74pXgpI2F0FIT3Fb55khSD307WJolj3bMhCSqM7sMvwgVk0grgDqbY0ap-lp6PRutai5d_K1WOHTUudjS0bBzBzWGLhNZhdybf66GylnEXs68MFmrG1Xc9_z4A3nNlW8GhJBUQfWXgnYw4ogE-ch_HUmPQ93UdAS-ImKqx_FxkY-ebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_دهم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید محمد رئوفی نیا  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666627" target="_blank">📅 00:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666626">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d2d2c1542.mp4?token=fk5AAEDA8XEynNjnBLe2SO5HLkOagSTQmy_cnTfe264lK6Dcu8ebQu0_lPwCX1NaJbYgPVUwp-PR3PaerulN6SKHJaSXn_Ela59K0RA1JjKX70xGq3JsG0le7qRDI1C20SI5y3-oGDFbd-4M3MF_83c5BHa8IH_SIgxHmO-8GXqijt4FrJuxyqRfef1PxkQurw78ZS8a0n-VYI9S4ejJY0vYbv0BKkDHoCq_l7S3qExQX2u7h-7fvDb_vJbBAKGugf_OkMnl0jUSw9lacmreZJePbrSaELwGUwo5yQQmVo7kQrfwj4n7U8KjCHuaHoLBoKLrDah3bVtB6VkIfU3ffkDqpQsZJHPRxyFDl9ZO0za5s0cYGWtg0C1odOe2oIOoGG6iVRJ2Qb5tyGYzRJPg-BkZta1ZZ-M-g51tcVRnxaYG86JMsZMbcq_29kd-EXt4lqrSJXvF4cuRF4mHAjDjaoVmUR563ndF6DAAusazwXV56Hs5ONxQ9F4HQV_WZowrEIczZRJIQyy2EOSSTkwiO7LlFfYDKcnoZQXFCgWtS-Ag_ltC-tGieh-hL5lYMiR_sLpaiMCv0rFJz482IxY_sq5peppKwAstxuE4kh7wE1BFTI8hr359RvQfrQlm47Z54KdB9fGHBRxJH9_Ld0LFaJHjh-l9dw7VdCmj50ecnBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d2d2c1542.mp4?token=fk5AAEDA8XEynNjnBLe2SO5HLkOagSTQmy_cnTfe264lK6Dcu8ebQu0_lPwCX1NaJbYgPVUwp-PR3PaerulN6SKHJaSXn_Ela59K0RA1JjKX70xGq3JsG0le7qRDI1C20SI5y3-oGDFbd-4M3MF_83c5BHa8IH_SIgxHmO-8GXqijt4FrJuxyqRfef1PxkQurw78ZS8a0n-VYI9S4ejJY0vYbv0BKkDHoCq_l7S3qExQX2u7h-7fvDb_vJbBAKGugf_OkMnl0jUSw9lacmreZJePbrSaELwGUwo5yQQmVo7kQrfwj4n7U8KjCHuaHoLBoKLrDah3bVtB6VkIfU3ffkDqpQsZJHPRxyFDl9ZO0za5s0cYGWtg0C1odOe2oIOoGG6iVRJ2Qb5tyGYzRJPg-BkZta1ZZ-M-g51tcVRnxaYG86JMsZMbcq_29kd-EXt4lqrSJXvF4cuRF4mHAjDjaoVmUR563ndF6DAAusazwXV56Hs5ONxQ9F4HQV_WZowrEIczZRJIQyy2EOSSTkwiO7LlFfYDKcnoZQXFCgWtS-Ag_ltC-tGieh-hL5lYMiR_sLpaiMCv0rFJz482IxY_sq5peppKwAstxuE4kh7wE1BFTI8hr359RvQfrQlm47Z54KdB9fGHBRxJH9_Ld0LFaJHjh-l9dw7VdCmj50ecnBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایندۀ اهل‌سنت مردم کردستان: شرکت در مراسم تشییع، ادای دین به رهبر شهید است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/666626" target="_blank">📅 00:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666625">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDVuvhK6rCGYZxWk8zqYlrgiwOgcIM4tXWPwIKdHCIxQdYd1pN6D1oi7QXDm21IySXLAcZWQtCRsPP5kR25Cbky-CiRNykJ2h4eFxq6PaPawZpOakd-GSRAp87lBoLrUWsFgRx-Thar4GJiX_ndoboMtDpPB_I0x5T2k_f-kkTEUEvSN5ruio-9tNd7qlHEVht7l_qxqzwiYODXaCqTajHN_77zOiRilUjsgyE9j2pLXZ6xCjc14R2BYzHmMIYk66yoh76rO3OYu6hknw31aq3rbU0EbM1ouskfCCiHl29Nhuxj7xhF3btYh_E6IJLU8HamUUFHe5bWV0lleMkfkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/666625" target="_blank">📅 00:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666624">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f3489673.mp4?token=Qp0b2S9y9XSc6zcNuwwwhGiGWFG7CThHKLAGgdrqM-cmDa-t5DYnogD3AiEMFhbGeYxENQloGYEIb547h_DU7KQhVO6DDSVFQetH1abWR3uKmhIYfvvbnU-uUV_WQlOKfbY7CWSTA3pMNHM8oTwm9Ad8HTTveXjsflQ-Wj87MITSUMZ8S0W_uw5Vfvzc5GG1tli6IP8r-W3sZBs-ImNbPUsInJoZsnLZpJ6Nns_3juyNtn949J7Mb7sVdTXXYkQmNBJcrHYT0N4G2i-aVuUT8wfGTra3QMrvky7WA53tXk8UG4H6GK8EKK-3Ip2RVdKBn63itx3KWScoXT4Jrc8uxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f3489673.mp4?token=Qp0b2S9y9XSc6zcNuwwwhGiGWFG7CThHKLAGgdrqM-cmDa-t5DYnogD3AiEMFhbGeYxENQloGYEIb547h_DU7KQhVO6DDSVFQetH1abWR3uKmhIYfvvbnU-uUV_WQlOKfbY7CWSTA3pMNHM8oTwm9Ad8HTTveXjsflQ-Wj87MITSUMZ8S0W_uw5Vfvzc5GG1tli6IP8r-W3sZBs-ImNbPUsInJoZsnLZpJ6Nns_3juyNtn949J7Mb7sVdTXXYkQmNBJcrHYT0N4G2i-aVuUT8wfGTra3QMrvky7WA53tXk8UG4H6GK8EKK-3Ip2RVdKBn63itx3KWScoXT4Jrc8uxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک نماینده مجلس: شخص آیت‌الله سید مجتبی خامنه‌ای دستور تشییع پیکر رهبر شهید انقلاب در مشهد را دادند/ اگر امکان تشییع پیکر رهبر شهید انقلاب با ماشین در مشهد نبود، از طریق بالگرد پیکر منتقل می‌شود
حسنعلی اخلاقی امیری نماینده مجلس شورای اسلامی در ستاد تشییع رهبرشهید در هلدینگ خبرفوری:
🔹
مکان تدفین در حرم مطهر مشخص است و نماز نیز خوانده خواهد شد.
🔹
بنا بود در مشهد مراسم وداع رهبر شهید برگزار شود اما با فرمان شخص رهبر انقلاب وداع به تشییع تبدیل شد. رهبری دستور دادند که در مشهد تشییع انجام شود.
🔹
باید تجربه تهران و قم دیده شود، ممکن است در اجرای این موضوع کمی تغییرات انجام شود ولی در حال حاضر قرار است به مجرد ورود پیکر به مشهد، تشییع برگزار شود.
🔹
در این زمینه اگر امکان حمل ماشینی بود، اینطور پیش می رویم اما اگر نشد، از طریق حمل هوایی از طریق بالگردهای خاص این موضوع دنبال می شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/666624" target="_blank">📅 23:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666623">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f66194c8.mp4?token=ZfXwjSvh6XDZ37ZaC8ecNb3XH4Y5fE5AEq5h4vdtG-8sZuZcEz-STNxHQ-PpH5JZIPPvIQf6paK5q3pw6kjjYzdGewtIjkUpqVZmf_fRcjU26qOp1akCl0B5IzsqzShPUTR1-57Ra_pKMxiRaeQlpWhYa5TGS89nsujOhjr8ITjNvUSWom8ZRA5i1_bNq2zmt22P0UysroGSL3SjGIVJkx-lWq1FvptL8mXRURmwd7kzmLiWrMsULt8zb60mvIEEEH0q-5ghGdykiLm6z7G0sYnmrBnXgY7WS3JxBH0R3w53PNw9SrZtix2cTmJZ7rwmPUfmlfhnaOnp0wHVvgK0oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f66194c8.mp4?token=ZfXwjSvh6XDZ37ZaC8ecNb3XH4Y5fE5AEq5h4vdtG-8sZuZcEz-STNxHQ-PpH5JZIPPvIQf6paK5q3pw6kjjYzdGewtIjkUpqVZmf_fRcjU26qOp1akCl0B5IzsqzShPUTR1-57Ra_pKMxiRaeQlpWhYa5TGS89nsujOhjr8ITjNvUSWom8ZRA5i1_bNq2zmt22P0UysroGSL3SjGIVJkx-lWq1FvptL8mXRURmwd7kzmLiWrMsULt8zb60mvIEEEH0q-5ghGdykiLm6z7G0sYnmrBnXgY7WS3JxBH0R3w53PNw9SrZtix2cTmJZ7rwmPUfmlfhnaOnp0wHVvgK0oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم‌های سرخ در مصلی امام‌خمینی (ره) تهران به نشانه انتقام‌ خون امام شهید امت
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/666623" target="_blank">📅 23:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666622">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb1dcd259.mp4?token=n9ym0nqKIjUm6JThX8OJ3B05irER-m6KIbivHyoorsUYTxmVntF4Jvtqt3dq6MQIWWVHjEkx6ApDWwjg7DgUSUPxfIiqov3v7y-RWx5nfggQGYPz2JMexytzZ71e_FQj5ITdsrImm8rIHpdS9pJeTt_FZWenWIUqAMg97lJSRzXUc_5trPIXm6SmSQiRVFi3oa6iEDLG156brSt8wpGhj47DzJwPoHaBz-bv9i8_euKn86hDBI0f3hW5M9U26xJfrKxmYI3LA7Nimhe1OKYDaV6w7anUsM_pphLDT4gWfmGu-1Zg4SzdkRUNVMdoQqwkN3sgA_2i9UAdj7pe3_AsZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb1dcd259.mp4?token=n9ym0nqKIjUm6JThX8OJ3B05irER-m6KIbivHyoorsUYTxmVntF4Jvtqt3dq6MQIWWVHjEkx6ApDWwjg7DgUSUPxfIiqov3v7y-RWx5nfggQGYPz2JMexytzZ71e_FQj5ITdsrImm8rIHpdS9pJeTt_FZWenWIUqAMg97lJSRzXUc_5trPIXm6SmSQiRVFi3oa6iEDLG156brSt8wpGhj47DzJwPoHaBz-bv9i8_euKn86hDBI0f3hW5M9U26xJfrKxmYI3LA7Nimhe1OKYDaV6w7anUsM_pphLDT4gWfmGu-1Zg4SzdkRUNVMdoQqwkN3sgA_2i9UAdj7pe3_AsZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا در برنامه پرچمدار: مردم عزیز! خدا به ما رهبری عنایت کرده که فرزند شهید، همسر شهید و دایی شهید است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/666622" target="_blank">📅 23:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666621">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
حملات جنگنده‌های اف16 عراق به مواضع تروریست‌های داعش در کرکوک
روداو:
🔹
نیروهای امنیتی عراق روز شنبه با اجرای رشته عملیات هوایی و زمینی در استان کرکوک، مخفیگاه‌ها و مواضع تروریست‌های داعش را هدف قرار دادند و در عملیاتی جداگانه در این منطقه، یکی از سرکردگان این گروه تروریستی را به هلاکت رساندند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/666621" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666620">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_lFwfbxK7sgk56irwjJWcYB34lRjnISR46YQio_bqvBH2fnCL-iq5nfeky4LFf80GsgQ9NQA0jCgQvTfhmR_wcu5bZE1YH_4vXAN73HYo6EtOSKzZ0Dtlx0n59kasQGshyDsVGd9jsH8XbI-ywsXp0cirL8dfnmbxW1K0g4PVelxXikLD7-lqLOorL9MrAyiDhP4XhMsMbodAt4DLilcl37ZPk2eLY734LEILbPj8u2Znu_gXTPY93BvdmOGEYLTrFKNEAy_yjClAcbGLkBcvbyddYA35sYUQlhcFDBplgSpf5KsYPFLrazmcpzz3m1IomTXR08M1E512x-1r-LKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ای قلّۀ سرفراز ایران بدرود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/666620" target="_blank">📅 23:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666619">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
متن و حاشیه مراسم امروز وداع با پیکر رهبر شهید انقلاب + آلبوم کامل عکس و ویدئو
👇
khabarfoori.com/fa/tiny/news-3227648
🔹
خون‌خواهی؛ آرمان مشترک میلیون‌ها آزادی‌خواه | سرنوشت ترامپ و نتانیاهو چه خواهد شد؟
👇
khabarfoori.com/fa/tiny/news-3227630
🔹
واکنش ترامپ به مراسم وداع با امام شهید: یک هفته مرخصی دادیم!
👇
khabarfoori.com/fa/tiny/news-3227705
🔹
ادعاهای تازه درباره استعفای پزشکیان
👇
khabarfoori.com/fa/tiny/news-3227847
🔹
کالابرگ این افراد حذف می‌شود
👇
khabarfoori.com/fa/tiny/news-3227640
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666619" target="_blank">📅 23:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666618">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
پاسخ سفارت ایران در ارمنستان به اظهارات ترامپ علیه شرکت‌کنندگان در مراسم تشییع رهبر شهید
🔹
انسان‌ها را می‌توان کشت، اما آرمان‌ها را خیر
🔹
شما آیت‌الله خامنه‌ای را ترور کردید، اما در واقع، شیشه عطری را شکستید که رایحه آن همه جا پخش شد. شما این چیزها را نمی‌فهمید چون نه تمدن دارید، نه تاریخ و شرف!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666618" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666617">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f2df4beb.mp4?token=g5IpaM_wtHt7YChzyeM7qs3nmA7hXHbSKo55GbVbzCcdGzztVP2SH2PwvXMoqC8WOfmR7h06RroEZJtdlbeFln0x_-S9cMxpSQhqr-RDj-P-7aZLHSYHtct1EpO3tZ2gr3SpaEn700GW9BPdWpzEQVCXgrM03sXZaAJvJEA425NGuf1N14sn8b0QzDl5fJoqFt7_QVSy-Vu-4I45xapOZjGDGJ3mMfjOgIwa154dVWOiZ3-XI1L0cWwQxE3aCDCHldQvbJrgZowSysIXfdgi3jP2URxVLu0qbUXJxmlcwOVgmqUqQ8v-94aXNGPk01orsPCAkZckyyugdPtYFhPYQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f2df4beb.mp4?token=g5IpaM_wtHt7YChzyeM7qs3nmA7hXHbSKo55GbVbzCcdGzztVP2SH2PwvXMoqC8WOfmR7h06RroEZJtdlbeFln0x_-S9cMxpSQhqr-RDj-P-7aZLHSYHtct1EpO3tZ2gr3SpaEn700GW9BPdWpzEQVCXgrM03sXZaAJvJEA425NGuf1N14sn8b0QzDl5fJoqFt7_QVSy-Vu-4I45xapOZjGDGJ3mMfjOgIwa154dVWOiZ3-XI1L0cWwQxE3aCDCHldQvbJrgZowSysIXfdgi3jP2URxVLu0qbUXJxmlcwOVgmqUqQ8v-94aXNGPk01orsPCAkZckyyugdPtYFhPYQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجموع سفرهای انجام‌شده در شبکه متروی تهران به ۴ میلیون و ۹۲۰ هزار و ۶۹۱ سفر رسیده است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666617" target="_blank">📅 23:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666616">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83029552c0.mp4?token=j9i_Dnr02QbfwbKIof_qz8e9DkkAk_X5LZdb59Y3HeMX4jRWzbbcMTKm_kx0Q24FDi0CEL78iR1Yv9Yag0524dP0zqrKXkIbs99h3Z1xuUFkjHy_diaZ-0vHoYTIXWRTSXW5FLKqDSbD1j4B4c08mHxxj99QOCsUxm15djlJGWpWH9ayOu-LDNZMDfIJOB1KYIGc84SFXc2cn0klwXCWoEAvTzd6ubEnf-gmPr929A4tLE0bwOpzs5ndiHpe0aq9uUlteO07WepL6Qp4NIRhWy2uxSyhL_8y26AfFKPGyHtICYlt2ElfYp-XzEl3EDHXSBOYEmFmISymfuGDF19Qtb_GVaXV2BXnm9sCxaNQzulgY76G5MwBrAYFJqFMD82Di923ZiC54xK6q-I4QyxE52vj2C3iagBiAFBBUASNG6rxG-3-WZvjSYEyI4aiSczyfxoMBx2LnPhHJhqPu61yd8fpBo1mRCqPEU7kCX1vC5pyHiZC8HsfkR1zdBbLyR9xNpXlUTdwEzXaID0AAToyMtgknke7tsmbiQjlE1Tgr1k1u_ITQ-LaDCnSbZmKAmusxVEdM-dAZTS46RSQFKutCZMjHrP17Hp9odxLDgKXF1IdaaoU7H3x3W_fjXOp0lFSJX3qjso05SyxKDSmDMAT9xl2aQwo72kGa7c_fjKH0Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83029552c0.mp4?token=j9i_Dnr02QbfwbKIof_qz8e9DkkAk_X5LZdb59Y3HeMX4jRWzbbcMTKm_kx0Q24FDi0CEL78iR1Yv9Yag0524dP0zqrKXkIbs99h3Z1xuUFkjHy_diaZ-0vHoYTIXWRTSXW5FLKqDSbD1j4B4c08mHxxj99QOCsUxm15djlJGWpWH9ayOu-LDNZMDfIJOB1KYIGc84SFXc2cn0klwXCWoEAvTzd6ubEnf-gmPr929A4tLE0bwOpzs5ndiHpe0aq9uUlteO07WepL6Qp4NIRhWy2uxSyhL_8y26AfFKPGyHtICYlt2ElfYp-XzEl3EDHXSBOYEmFmISymfuGDF19Qtb_GVaXV2BXnm9sCxaNQzulgY76G5MwBrAYFJqFMD82Di923ZiC54xK6q-I4QyxE52vj2C3iagBiAFBBUASNG6rxG-3-WZvjSYEyI4aiSczyfxoMBx2LnPhHJhqPu61yd8fpBo1mRCqPEU7kCX1vC5pyHiZC8HsfkR1zdBbLyR9xNpXlUTdwEzXaID0AAToyMtgknke7tsmbiQjlE1Tgr1k1u_ITQ-LaDCnSbZmKAmusxVEdM-dAZTS46RSQFKutCZMjHrP17Hp9odxLDgKXF1IdaaoU7H3x3W_fjXOp0lFSJX3qjso05SyxKDSmDMAT9xl2aQwo72kGa7c_fjKH0Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خرج زندگیت کن
🔹
اینا تجمع هم می‌رن شبی دو تومن میگیرن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/666616" target="_blank">📅 23:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666615">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d6a8980c.mp4?token=MDBuwsxGLecl0IFSDWRVHHgUWI29fV7sZhwjcHCip2VaGQLunJQBuX2kCNcHdAn5W7MwbJMK2LgUBptB6AUy8zsiWd5BZ2D7ay355_u3vy-qsfyohlvqCTGf0XQ0zr8GieYbUneX5bVKq25SYuzpkAx3rg27JgU6hkTYtYeJwqW3Uksawt77ZO4R37C-m-pG77-ICg9gyGm3W6_G0l3aZxfPdr9Uvfu5LXxpSuS8GXhsrXFqkAIZnQIZsqxQtgQzx8QqOUDRVGKbc7TdEwqw0tD5PCRY6aqZHPzxdyNR0u6ASIJvAkND-0vhjeebnjYRAC2JflUsVjf6JNbr-Emx8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d6a8980c.mp4?token=MDBuwsxGLecl0IFSDWRVHHgUWI29fV7sZhwjcHCip2VaGQLunJQBuX2kCNcHdAn5W7MwbJMK2LgUBptB6AUy8zsiWd5BZ2D7ay355_u3vy-qsfyohlvqCTGf0XQ0zr8GieYbUneX5bVKq25SYuzpkAx3rg27JgU6hkTYtYeJwqW3Uksawt77ZO4R37C-m-pG77-ICg9gyGm3W6_G0l3aZxfPdr9Uvfu5LXxpSuS8GXhsrXFqkAIZnQIZsqxQtgQzx8QqOUDRVGKbc7TdEwqw0tD5PCRY6aqZHPzxdyNR0u6ASIJvAkND-0vhjeebnjYRAC2JflUsVjf6JNbr-Emx8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام عابدینی: رهبر شهید انقلاب در ما باوری ایجاد کرد که امروز حتی کودکان ایرانی نیز ناوهای آمریکایی را به تمسخر می‌گیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/666615" target="_blank">📅 23:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666614">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN7Sk_Tqvj1dDUQ88f494gKzMN02a1ugy8VXqvKmM2mqlx1SRvhdChcoIYIyfi-ikTlZbDc2VkolhoyLU1aJh8RmtDkXI21w6fIvjcO2N1h3UTeVwIqSTWaSkN7ADrnslFZaHiOFjW7QFaVfVHxexJs4IHDAZnVxZ6uUXASs_V99I8HQYMBVUdjFkn00Ws8IRc52lTtM3TVB6VPWu37IVSdOADxIABVvUfVHm1W_we9dFWvJ4yFJbJJiJJIq8HWqzfPamvGUwYWJGgLMbgQsprtkmBR0s5tMvfP_Ij596cqT2lUhTkSXPbkX-_0K3eEtPIKcQwZYrwRvmbokAYdWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقرار تیم‌های تخصصی ارزیابی خسارت
#بیمه_البرز
در محورهای مواصلاتی تهران به منظور خدمت رساني به زائران مراسم وداع و تشییع رهبر شهید
همزمان با برگزاری آیین وداع و تشییع پیکر مطهر رهبر شهید انقلاب، کارشناسان و ارزیابان خسارت مجتمع تخصصی خودروی
#بیمه_البرز
در پلیس‌راه تهران - قم و سایر محورهای مواصلاتی منتهی به پایتخت مستقر شدند تا خدمات ارزیابی و جبران خسارات احتمالی خودروی زائران را در سریع‌ترین زمان ممکن ارائه دهند.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5055</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/666614" target="_blank">📅 23:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666613">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
استان میسان عراق چهارشنبه و پنجشنبه را تعطیل اعلام کرد
🔹
استاندار استان میسان عراق روز شنبه اعلام کرد که روزهای چهارشنبه و پنجشنبه آینده به مناسبت تشییع پیکر حضرت آیت‌الله خامنه‌ای در عراق تعطیل خواهد بود. #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/666613" target="_blank">📅 23:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666612">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/539939e159.mp4?token=R6AVhE6594_LP4pLMLSAGjpHV6y20qwklWY2uhSXR0iG3yPuHNB5iSqCby8Da2xF9_sPNqRhr_OrQXV-osIF8lAMWjma6NsHD1D_-_VIVHs-I7N93nkQapfpZLudjwztYtlUjYNnhjuwtBb-yPEadLQT2gFP1oMaRHpDCuW0esrj1BCP5cRyJ-aC0D4I66w5LZjmbuQrhzM-3PFMCA6gG8OJeB5Er4vLnmxgvPs9mOwbawmsu-O-yYTWhHTumSN1WyheNgD_2lc3zfcowXTYQCYvbmFOOMwlWwIO6EyHa6p4AMMGL1JtyKsLMiXwMWO8zi1w5hQiXvdrB3oRzIIviDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/539939e159.mp4?token=R6AVhE6594_LP4pLMLSAGjpHV6y20qwklWY2uhSXR0iG3yPuHNB5iSqCby8Da2xF9_sPNqRhr_OrQXV-osIF8lAMWjma6NsHD1D_-_VIVHs-I7N93nkQapfpZLudjwztYtlUjYNnhjuwtBb-yPEadLQT2gFP1oMaRHpDCuW0esrj1BCP5cRyJ-aC0D4I66w5LZjmbuQrhzM-3PFMCA6gG8OJeB5Er4vLnmxgvPs9mOwbawmsu-O-yYTWhHTumSN1WyheNgD_2lc3zfcowXTYQCYvbmFOOMwlWwIO6EyHa6p4AMMGL1JtyKsLMiXwMWO8zi1w5hQiXvdrB3oRzIIviDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جامانده
🔹
رهبر شهید، دل‌های مردم را از گوشه‌گوشه ایران به هم گره می‌زند.
🔹
اگر از قافله عاشقان جا مانده‌اید، دلتان را به ما بسپارید؛ و اگر توفیق حضور دارید، به نیابت از جاماندگان قدم بردارید.
این پیوند، از دل‌ها آغاز می‌شود...
🖤
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/666612" target="_blank">📅 23:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666611">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b89806084.mp4?token=UUNklu4K1a_aavGiNV1hoEv80yFb-bMDKxp06q6bO8xU3TYeQIKNIBihuC1NybAUXZ7pFEisQYFy1HtZDOQzHziDhykHEkUAC7hXmN2TGoZcgEq8zZSP5rvdy1xnl1oqlDE2Q1JpLkRsGcv_Zoow_SQPdf9DYb9Ilvd4ydbw3OOSYNVIsQ9gfHiPsS3pXN4lzoMABnokBDFbkECwRlEg53kXy_z_cuaYRNhRWFcxaYPfwtqqFxpcNHkwr7fyFSscqxkE2I8p94tyTf0FowA-_jrfOFkbfYmf9eYq0nOWhcC7coC4pwCCiYy8dLvYCRc8TYcaiIpdot4-6TgzObheoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b89806084.mp4?token=UUNklu4K1a_aavGiNV1hoEv80yFb-bMDKxp06q6bO8xU3TYeQIKNIBihuC1NybAUXZ7pFEisQYFy1HtZDOQzHziDhykHEkUAC7hXmN2TGoZcgEq8zZSP5rvdy1xnl1oqlDE2Q1JpLkRsGcv_Zoow_SQPdf9DYb9Ilvd4ydbw3OOSYNVIsQ9gfHiPsS3pXN4lzoMABnokBDFbkECwRlEg53kXy_z_cuaYRNhRWFcxaYPfwtqqFxpcNHkwr7fyFSscqxkE2I8p94tyTf0FowA-_jrfOFkbfYmf9eYq0nOWhcC7coC4pwCCiYy8dLvYCRc8TYcaiIpdot4-6TgzObheoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همونی که براش نمردیم، آخر سر فدای ما شد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666611" target="_blank">📅 23:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666610">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395e2222e3.mp4?token=JU-2kK7pgALGgeuyAX9YLcCtpdABZXW7IYKHhwyDr5UT4AOjsH2mInFoR7F6HKau6sqiqe3F65jifEscXBnb4yeT-VCJdj9TBG9J1GV3yn1-6igJKZa1g_NT9X5I69nQxilYgNN8gXoFiQ6bPVPTh2RK4epyKVS3mRxTtxHdl93oFCFNPzwsZHWKPnlw9IWQMBp8-ao_tDxF6BRu03-XgdzlefGEaCoy-1-v4S2iY7TmVLK73lnnQ2vOlQ5Rly1alqeYIBJn3hoofgt-FBIl1OxMsqhCNQ9C4SNme-cWi2SvBPcfu4_nbpjsVJ5rBMSY_S5xQ1FOVmMowc1i0j02uiGa0esRKuKFXStZz54at_5XmlU111hRkW99fXAsT0DpQd0UgQvggFVEpMFDOlqhPw7tw5Jve_VRV6ON571-K-iCvf95aSbYMd4_TzYeIuy7GCqVQLVfjreAesxBj5sJ6OQr3bi2v8PShRWnJ8qlabTZsubu9n-ZQo9Raa2QswvA4P3yFHYvXYVPtcPHx550OrBqFr-51EBzB8Hmj-b-yVJpMpQTu1hGnKqTv2NwQ3wlKWBVCPC3_aMTpK0FHXYo4DRUslk9ORBklOwMvZT5fRcM56e73oY20b98tsrfrR2U-J-JRgMoqol8hbX5GAMl32rRayESB0ti6j64lD9srSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395e2222e3.mp4?token=JU-2kK7pgALGgeuyAX9YLcCtpdABZXW7IYKHhwyDr5UT4AOjsH2mInFoR7F6HKau6sqiqe3F65jifEscXBnb4yeT-VCJdj9TBG9J1GV3yn1-6igJKZa1g_NT9X5I69nQxilYgNN8gXoFiQ6bPVPTh2RK4epyKVS3mRxTtxHdl93oFCFNPzwsZHWKPnlw9IWQMBp8-ao_tDxF6BRu03-XgdzlefGEaCoy-1-v4S2iY7TmVLK73lnnQ2vOlQ5Rly1alqeYIBJn3hoofgt-FBIl1OxMsqhCNQ9C4SNme-cWi2SvBPcfu4_nbpjsVJ5rBMSY_S5xQ1FOVmMowc1i0j02uiGa0esRKuKFXStZz54at_5XmlU111hRkW99fXAsT0DpQd0UgQvggFVEpMFDOlqhPw7tw5Jve_VRV6ON571-K-iCvf95aSbYMd4_TzYeIuy7GCqVQLVfjreAesxBj5sJ6OQr3bi2v8PShRWnJ8qlabTZsubu9n-ZQo9Raa2QswvA4P3yFHYvXYVPtcPHx550OrBqFr-51EBzB8Hmj-b-yVJpMpQTu1hGnKqTv2NwQ3wlKWBVCPC3_aMTpK0FHXYo4DRUslk9ORBklOwMvZT5fRcM56e73oY20b98tsrfrR2U-J-JRgMoqol8hbX5GAMl32rRayESB0ti6j64lD9srSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاج حسین یکتا: وسط جنگ جهانی در میانه بازی‌های جام جهانی، در ایران یک اتفاق تمدنی در حال رقم خوردن هست/ در مصلای امام خمینی یک اتفاق الهی در حال رخ دادن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/666610" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666609">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e9a8d5f77.mp4?token=ZseJsZBG9qCvQBLVbVaXnq-35ek8MiZ-x9yaxjdfpQ1wn3cXB_Hs6w_NXz3Qg-3utlj_ekbcvd_LqJwyrOturt55JHi_3ItM0wbyprd-q2EZzrpQ4JZNgeGa_M0KQYrIg8CkGhrzZoZpY-_iwr_kFtzWdse4_zi-CMH9iQALlnbKJjOo6LbM5v29EKZaiBg4r32I1XHWNKyggxvhFnEhSash0TQxIvNeUDzCqRup1VZv8ApCyGnK7SREzpbiiGrQZXOm8lKMDZzlvmzvGHnOC2dt9ZuiRh2DAy0jzzb7Js1hCbTIECzEByftjaFwPjdrhW9Hd9JOiwZ-4pnpIjQGoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e9a8d5f77.mp4?token=ZseJsZBG9qCvQBLVbVaXnq-35ek8MiZ-x9yaxjdfpQ1wn3cXB_Hs6w_NXz3Qg-3utlj_ekbcvd_LqJwyrOturt55JHi_3ItM0wbyprd-q2EZzrpQ4JZNgeGa_M0KQYrIg8CkGhrzZoZpY-_iwr_kFtzWdse4_zi-CMH9iQALlnbKJjOo6LbM5v29EKZaiBg4r32I1XHWNKyggxvhFnEhSash0TQxIvNeUDzCqRup1VZv8ApCyGnK7SREzpbiiGrQZXOm8lKMDZzlvmzvGHnOC2dt9ZuiRh2DAy0jzzb7Js1hCbTIECzEByftjaFwPjdrhW9Hd9JOiwZ-4pnpIjQGoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای ترامپ این پیام یک نوجوان ایرانی است به تو:
داغ آقایمان را به دل‌ها گذاشتی؛ انتقام خونش را می‌گیریم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/666609" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666608">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174a13c993.mp4?token=JTb4y79AJ1KyQEtznrwGDbvf48S0YcwZYmYpDqYBkkh8TodMaaAw5W2m_yZd_tNx3LnBCRQV_XiLg546Ly8gXumDxzHSzubxkE2XF3QOC_AlUfI_GoTOTPKqQutWZ8lsb3QyW3BOdLfzeWjzPC7QaDF4KtW-bi_yFPE_PhkV_ANHKa5Ji5taDCMOt0V8KAAQah38_YbieG08s7QmU22b1eL767LQEE_R9bLbj8g8B2V1fsK0zCK3kaqBJXLgIl_PDg8Gkr0ycL-mG0t39V_VEldp3Fh8qdTUtyP38QXtHBcBUu3tHzzsht8oTpy-9zGJqg8PJzBQ_zpgYEY3GoErRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174a13c993.mp4?token=JTb4y79AJ1KyQEtznrwGDbvf48S0YcwZYmYpDqYBkkh8TodMaaAw5W2m_yZd_tNx3LnBCRQV_XiLg546Ly8gXumDxzHSzubxkE2XF3QOC_AlUfI_GoTOTPKqQutWZ8lsb3QyW3BOdLfzeWjzPC7QaDF4KtW-bi_yFPE_PhkV_ANHKa5Ji5taDCMOt0V8KAAQah38_YbieG08s7QmU22b1eL767LQEE_R9bLbj8g8B2V1fsK0zCK3kaqBJXLgIl_PDg8Gkr0ycL-mG0t39V_VEldp3Fh8qdTUtyP38QXtHBcBUu3tHzzsht8oTpy-9zGJqg8PJzBQ_zpgYEY3GoErRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن محمدی‌پناه، مداح نماهنگ «باید برخاست»: ما مدیون آقا هستیم و نتوانستیم حق ایشان را ادا کنیم
🔹
این داغ هرگز در دل ما سرد نخواهد شد و سوخت موشک ما برای حرکت‌های آینده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666608" target="_blank">📅 22:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666607">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b464301f47.mp4?token=CXW-HzZwizfS231FitrIdPchjOUpUZ64WkuRmraF9TqRU86Q47cbOAHlDNTa6fZvK3AQNnKka4y8WOXHbcD1HfRMUHnIt-duxJavKxUrP7GYym02gv7iDTvemev3gUbnwOvMSZH7j0x_XAl0gbOe4JvLivzmLzKUVxteUudBJXDjoCGNVZhlyugG2DZZ46RthmV23Nl6hGn3MrURKRx3GxYeaNKDUtqLZl2T4gwLIYh6orundN2qH5zK5deNkikqRvtB0CnADXIl5XmS06Gxr1tiGGXJYdZDWeZgm8HhVxFedSE2rxb7-w7EcMHXKSOMcvAwOok2xotAdStLl3niZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b464301f47.mp4?token=CXW-HzZwizfS231FitrIdPchjOUpUZ64WkuRmraF9TqRU86Q47cbOAHlDNTa6fZvK3AQNnKka4y8WOXHbcD1HfRMUHnIt-duxJavKxUrP7GYym02gv7iDTvemev3gUbnwOvMSZH7j0x_XAl0gbOe4JvLivzmLzKUVxteUudBJXDjoCGNVZhlyugG2DZZ46RthmV23Nl6hGn3MrURKRx3GxYeaNKDUtqLZl2T4gwLIYh6orundN2qH5zK5deNkikqRvtB0CnADXIl5XmS06Gxr1tiGGXJYdZDWeZgm8HhVxFedSE2rxb7-w7EcMHXKSOMcvAwOok2xotAdStLl3niZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقاجان بانی این روضه شمایید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/666607" target="_blank">📅 22:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666606">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
اشعار حماسی محمدرضا طهماسبی در مصلی امام خمینی(ره)
🔹
از بامداد امروز تاکنون ده‌ها شاعر فارسی زبان از ایران و چند کشور دیگر اشعار خود در رثای رهبر شهید انقلاب را در رویداد ادبی آخرین دیدار خوانده‌اند.
🔹
در این محفل ادبی که از بامداد امروز در شبستان مصلی امام خمینی برقرار است، ۲۰۰ شاعر در ۴۸ ساعت بی‌وقفه برای رهبر انقلاب شعر می‌خوانند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/666606" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666605">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJE3nbuJlXs6XNtq471E3_fFNJNvNTJioyO3pNtZ-mI7vk6XrFETO4GrCku98oZ810ssrrX0NxKJbJPBFArUKcUI-5Q-Q6w9qaf_CdpgxwMgXhLiQSwmcQFpccO75HLNtqaVwyGtd6nC286Hu8d-J6YHwOB3OIe3Ula3sDq_UX0UC0an0vZYuQYWNUIpN4lFrjavTgzUIU_eBXkvyyyX42_cpNuIxbgGjVqzInrx3J8KpfsTsx8l_Cobr3IfYEy63HfneSgoQLxMUSRDznNZVeaC8mAcj30hC0WG10cmoRlhg9MtUqty6TXQdd0-Bu1SgAs1Er83Hn1lq9zX1DmOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار نخستین‌بار
تصویری از شهید دکتر مصباح‌الهدی باقری در کنار رهبر شهید انقلاب اسلامی در حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/666605" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666604">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq9pSj4N7J2DOOVHzSJR9o7-P2JNoxdPKWJOHz5_b00FnBUa-3IXZlrHY3PUQ3L1Y4mvux9W2AnGlSqjlO4fdRsM3dLOH6e_FzlW7rnNg4x7b7vmjnFPuziH4U8amn9-NKa4FyKoVN-ajB9Z2CTDjNKG5HM3qdx13HESbmDOI0B0qTJ6DVZU92d1wJgv1Di1lmlsES_-UX0HR-xXwbe_8wCiO1wmXaWb8C48RtX8m1f_dBchTIKPePIKj0ywAGPZ_hIbO6VR3aF4w33tAZmuhyl26mdx8fWhfyx5iym6HOjr1qAJ1iPnmuilUtpoR4y6llMBr797i9RtgVDoAsw2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مچ‌بند سرخ، نماد عهدی است که فراموش نمی‌شود
🔹
با این نشان در مراسم تشییع حضور یابیم.
🔹
تا پیام عدالت‌خواهی و ایستادگی را به نمایش بگذاریم. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/666604" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666603">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiKRoO3g-jpRx8TbPQ3CRvaPKAgloy1of_YUo_iKvdyPAseladpSVXWHJGCq-Aqnq-bFoqKU-MVZm9XBodsRZ0IRQDmGIBPE9IVs1LCzhyWnVDGNcS1YYM4gh6aMqR1OqiwOYkem7mLDA2eZu1l7S4_98V2jlK-TpFMcJFKCBBOpIB31Io6IehV5FDMBtgvmm01-2piUjv5p90aRXDw6c3XmGdGpVNKhItMrKmF4f_kkL47ecLX2nB_RE2AIUcnPeaRZR1RScNZVbmbQZmhYhqZh5N2xQ6_Pado1RzZS7iUW7nxZQpKgu3yTprL6gmwkQavJigV_6uURYboHxRvsiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آغوش ایران
🔹
تهران امروز صحنه یکی از ماندگارترین بدرقه‌های تاریخ ایران است. از نخستین ساعات بامداد، مصلی تهران میزبان خیل عظیم مردمی شد که برای وداع با رهبر شهید انقلاب اسلامی گرد هم آمده‌اند. این حضور، تنها به مردم ایران محدود نیست؛ مهمانانی از کشورهای مختلف نیز خود را به این مراسم رسانده‌اند تا در این آیین سوگواری سهیم باشند. زن و مرد، پیر و جوان، در کنار یکدیگر پیکر مردی را بدرقه می‌کنند که نماد مقاومت، ایستادگی و پایداری به شمار می‌رود. امروز خیابان‌های تهران در میان اشک، نوحه و شعار، روایتگر پیوند عمیق مردم با رهبر شهید خود است؛ وداعی که تنها بدرقه یک شخصیت نیست، بلکه تجدید عهد با آرمان‌های اوست. تصویر ماندگار این روزها، همبستگی و حضور مردمی را در حافظه تاریخ ثبت خواهد کرد.
🔹
هفتصدونودویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/666603" target="_blank">📅 22:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666602">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
حکم سنگین دادگاه کویت برای یک شهروند کویتی به اتهام ارتباط با حزب‌الله لبنان
🔹
دادگاه کویت، یک شهروند کویتی را به اتهام ارتباط با حزب‌الله لبنان به ۱۰ سال حبس محکوم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/666602" target="_blank">📅 22:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666600">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f415f88f0.mp4?token=sVhpXXBLvXZtkxJWYDp71q5N6gZHewjzSxmkcsB1Y7jvirF9HW0YupYH_UCpaKEpzY56hvKE6JQ9KxZn8hZSJexO9T6hkgo22vdsigMh_6VYLVkrIvFwYsbCeFwpPW6z0jsaKWjHeVEyDRQI8-EGKMlkiQJUhMA0OlGlGgrxGT2yL95suxpG8pVajNKGf7ntbLszPpR8xmdwy6RgrbqKmz9t-orxEpvlZxLkp5aRLhmUyg4G1ClkwgDgxwGeFTvdquqUSIbDISVFowALnhwUVdhvSIXYzuoN_sLXa1L4PYXxyHVmSxf5-pDzZJfolLgyYtjqA1rmLl9NuuWY1-_crw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f415f88f0.mp4?token=sVhpXXBLvXZtkxJWYDp71q5N6gZHewjzSxmkcsB1Y7jvirF9HW0YupYH_UCpaKEpzY56hvKE6JQ9KxZn8hZSJexO9T6hkgo22vdsigMh_6VYLVkrIvFwYsbCeFwpPW6z0jsaKWjHeVEyDRQI8-EGKMlkiQJUhMA0OlGlGgrxGT2yL95suxpG8pVajNKGf7ntbLszPpR8xmdwy6RgrbqKmz9t-orxEpvlZxLkp5aRLhmUyg4G1ClkwgDgxwGeFTvdquqUSIbDISVFowALnhwUVdhvSIXYzuoN_sLXa1L4PYXxyHVmSxf5-pDzZJfolLgyYtjqA1rmLl9NuuWY1-_crw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراکش مقتدرانه نسخه کانادای میزبان را پیچید؛ گل سوم مراکش توسط سوفیان رحیمی در دقیقه ۸+۹۰
🇨🇦
0️⃣
🏆
3️⃣
🇲🇦
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/666600" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666599">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl6k_n7vA0mLG05QUPBm4YeqEe0KUwavFYlZhmAtX4z5WKyI4nHcpyDesPmRF8gEvNAE1XtdMhUoPMJU6MpecUdc7Onp7JHENgCkHLeuy-v19EBtKvuSfDRnTNuYOtB2u2AtQEXytizZYK4BrOcO35SP2zYqS3uNd8d2JEY-jeNyObrheFKKu23q5bVf_iIc5Ags9qnBjwysOfX8n5BFSdG6DEsGwH2sDxp3vLlp8_mP2CRFQq_Rbq2ZXBiWpdim7yGivCG8EhsDNbro4N7waWS_TcIa4TLdIiLnDzCOvnDPBlefZq8QiTzdWUAsuPdm0xo0lLI74EbOQRLBcHn72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه‌حل امام برای خلاصی یافتن از ترس‌ها
🔹
امام عليه السلام مى‌فرمايد: «هنگامى كه از چيزى مى‌ترسى خود را در آن بيفكن؛ زیرا سختى پرهيز از آن از آنچه مى‌ترسى بيشتر است». ترس اغلب زاییدهٔ خیال است. انسان تا وقتی از چیزی فرار می‌کند در اضطراب می‌ماند؛ اما وقتی…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/666599" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666598">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
یدیعوت آحارونوت به نقل از منابع اسرائیلی: تاکنون هیچ‌گونه ترتیبی برای برگزاری دیدار میان نتانیاهو و ترامپ انجام نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/666598" target="_blank">📅 22:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666597">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2-m97smM8CmAll730-yXQzspZyPvH-7h2ILaFDvSGQ95ZYt2A4kWk2xeLvncTtk3TVjlwsjTOLXaYp3cw1Uw0lzN8ooXxJ4_I4qLm_iub-lHN7BA6YhCJRuSrhOumdEjvy_oc4ftKPTfzwcYMqYg6yjonxTHEKyKBiXfCbTWdY5Zj6dJR9TGtj1LgU28scYWtRep0cl8aHNOo-QUQEQoyEhFOSCogVmmouzGD4ZtL8Fg4F91tJUo1l9kVRlDPXimI7H4nObdXM0TYQgLa_V_wXQCR1e3xPlPU5qF4rD6-YefdAa9cSUyof48rma2zmqKMu2Vd3wJ6kzmaOY4Z-IVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی عراقچی از نمایندگان کشورهای شرکت‌کننده در مراسم بزرگداشت رهبر شهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/666597" target="_blank">📅 22:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666596">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سخنگوی ستاد بدرقه: مراسم وداع با پیکر رهبر شهید انقلاب امشب تا نماز صبح ادامه پیدا خواهد کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/666596" target="_blank">📅 22:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666594">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شب نورانی مصلا در هنگام مداحی حسین طاهری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/666594" target="_blank">📅 22:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666593">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c52c1e47d.mp4?token=QLSjloMXPyZ4gyuFX5myHr_JJbUNuwTMJxRt5uFGawEhUY_qN7XIKCO1YuRY9JXdPYd4Puw-dv7Xm4M4U8jj2r3po67uGHdsH1hkM8qlzDP0M_Yf1J60b3RRahaE9kgG7g_fxj5TouOwpmjfrTZ6_arC8f2wsJMKtcR9SkjadRB4WE5lGPOssQK7SqebAmnXd8CJ3BPk0e9J7e9_CbDA7xn9Cld2awyvwOzhDXr11YAH0_m1SzNjJU3NAGxVR7eJELZ-q_Et3iuTvJVnrIqp6olrWYd6hv0GnMhnBNcpFiZqMrBjYb1Ag8lAZ94t9zfBR4XQgjFEMBPPabiui2F3SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c52c1e47d.mp4?token=QLSjloMXPyZ4gyuFX5myHr_JJbUNuwTMJxRt5uFGawEhUY_qN7XIKCO1YuRY9JXdPYd4Puw-dv7Xm4M4U8jj2r3po67uGHdsH1hkM8qlzDP0M_Yf1J60b3RRahaE9kgG7g_fxj5TouOwpmjfrTZ6_arC8f2wsJMKtcR9SkjadRB4WE5lGPOssQK7SqebAmnXd8CJ3BPk0e9J7e9_CbDA7xn9Cld2awyvwOzhDXr11YAH0_m1SzNjJU3NAGxVR7eJELZ-q_Et3iuTvJVnrIqp6olrWYd6hv0GnMhnBNcpFiZqMrBjYb1Ag8lAZ94t9zfBR4XQgjFEMBPPabiui2F3SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضد حملۀ برق‌آسا
،
گل دوم مراکش به کانادا توسط اوناحی
🇨🇦
0️⃣
🏆
2️⃣
🇲🇦
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/666593" target="_blank">📅 22:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666592">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca5Y5b10rQWGIG2rPbt2hTgotktq5RWPozw8Huk6wwyYuepimphsz1LZjEu-9UlTRXT2W0VHm9-mb5HqEtf7N9LaSOY6Cfc9kl5nFx0EPxIOR6Ect0fKBC7w1Sfqp_VtJnQm6moFQ9TchMDQawYOlQuKwF3tMd3S680ePjxjwaM6sCpKlty8i4NhAfd5-03KKqXSJg-P7Jxz5SwS8J7pSS_BLUX7HlJdFgrTiF1qVHXMLq4F-0323Ezt8VWLFjmDQHXCOuzf5LMTp_M5zv_GhLu_rKdZz1fqD9Oc8T5wG4a0oPWfemTYlNc4cfzVkhigAARGCF4zt0NcWYG-4BF7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/akhbarefori/666592" target="_blank">📅 22:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666591">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cc42a03c.mp4?token=KWRGteJBvAw2GaFDWR80ZxQnEI8I_B9qPeIEz0yLpCrTmQnVPxiHJovei-UlVgNLauB1yDo-1zdC4FVj48a7vUbPtWdFoSaLcUyB9qGAvQJzd25d0DYXjQ8hlCabwLGjcFS-1WIqyVEqNRdOHZrMQnAWHeuUz_dkm-PEDGg3EUGdoNcuFNEeQNq8p1zBQ88iJMpQ22LCt64yBcqpw2-F2VlppbLkB-F9a81J6gnE3p0P8Y2NnbiKAApenGD3sf4H_8a_z1-Gp0-SB5OfwBDJXOmsHC3icogKhpmjkt8U18aFCxBqLC6TfGgH7AzRmA15XcN8pcAyjWfyCxhu7aczjHMmGnL7EbvVv_YR6H90M9hIs9VgVvnNs8x_UY6bO_zdKoMYdWiy_qyIkFfQ1jIHNCq98c8n8-hEH_2w8LmGsgiyBbac96qBmxkeNxNKR56J_IogWQD5Qchh6zXFo9falCb6Bnltknm0Dfj4cFdip509JJtCTvYaywTNE7bMDOXORoIufVvG9TR4Hl7ng3R8DYK1x_GrPY9gXFIZugKCxdRGRngUH82qF5QHA6znInjh3ixviwPW6nT4UBdq-soKyZWoJYd69JTfy5-QjfHM5REnQVCbby5CgEKxoC_LnwlIPYmjPYmMX3SjD53ddhDaOWeej_H33uel5NLPBZ_cApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cc42a03c.mp4?token=KWRGteJBvAw2GaFDWR80ZxQnEI8I_B9qPeIEz0yLpCrTmQnVPxiHJovei-UlVgNLauB1yDo-1zdC4FVj48a7vUbPtWdFoSaLcUyB9qGAvQJzd25d0DYXjQ8hlCabwLGjcFS-1WIqyVEqNRdOHZrMQnAWHeuUz_dkm-PEDGg3EUGdoNcuFNEeQNq8p1zBQ88iJMpQ22LCt64yBcqpw2-F2VlppbLkB-F9a81J6gnE3p0P8Y2NnbiKAApenGD3sf4H_8a_z1-Gp0-SB5OfwBDJXOmsHC3icogKhpmjkt8U18aFCxBqLC6TfGgH7AzRmA15XcN8pcAyjWfyCxhu7aczjHMmGnL7EbvVv_YR6H90M9hIs9VgVvnNs8x_UY6bO_zdKoMYdWiy_qyIkFfQ1jIHNCq98c8n8-hEH_2w8LmGsgiyBbac96qBmxkeNxNKR56J_IogWQD5Qchh6zXFo9falCb6Bnltknm0Dfj4cFdip509JJtCTvYaywTNE7bMDOXORoIufVvG9TR4Hl7ng3R8DYK1x_GrPY9gXFIZugKCxdRGRngUH82qF5QHA6znInjh3ixviwPW6nT4UBdq-soKyZWoJYd69JTfy5-QjfHM5REnQVCbby5CgEKxoC_LnwlIPYmjPYmMX3SjD53ddhDaOWeej_H33uel5NLPBZ_cApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به رهبر شهید ایران سلام / سایه سیدمجتبی مستدام
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/666591" target="_blank">📅 22:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666590">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0764895667.mp4?token=GXh5oguN4VB61HgPXbMnKe2FGv9jg9wAxL1kIwO_ISz5A5nJJrVRy_V9SUAIJ1Y0A8q5uVyZ6t-jQUsDLM4C8rrA1ib37ayX-Vpez70xhXizmBYl7suEziiiGTOZIsH6PyzfRoAnKyZdJIhLbmAaLsc2_AB1ifNM7GZZb7v3Iq9hW5FkptzJLdHIcKKn5PEABLRF-dJTDSUlvDKJgUEYZGAdRXcDmQ-ikiHSfBp6Th_fyoGGWOnZUsenQbf9Al_7R7hpIO9Fho4TIUUHzEOd-e2cMbnzF-0agu3FJy47VaQBfezZhfE6IkcQZKJ1b4r4NeTCgj2Whf5FUKjIHdTksw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0764895667.mp4?token=GXh5oguN4VB61HgPXbMnKe2FGv9jg9wAxL1kIwO_ISz5A5nJJrVRy_V9SUAIJ1Y0A8q5uVyZ6t-jQUsDLM4C8rrA1ib37ayX-Vpez70xhXizmBYl7suEziiiGTOZIsH6PyzfRoAnKyZdJIhLbmAaLsc2_AB1ifNM7GZZb7v3Iq9hW5FkptzJLdHIcKKn5PEABLRF-dJTDSUlvDKJgUEYZGAdRXcDmQ-ikiHSfBp6Th_fyoGGWOnZUsenQbf9Al_7R7hpIO9Fho4TIUUHzEOd-e2cMbnzF-0agu3FJy47VaQBfezZhfE6IkcQZKJ1b4r4NeTCgj2Whf5FUKjIHdTksw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار تانکر سوخت در آمریکا
🔹
این انفجار حوالی ظهر به وقت محلی رخ داده و علت آن نقض فنی اعلام شده است.
🔹
این حادثه منجر به قطع برق چندین خانه در منطقه شد. پلیس از مردم خواست تا از ورود به این منطقه خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666590" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666586">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UluqC2xGBrY9GmqIGeK2umximGchPreCgYgVc6NuTs2muz2oFHcYIbjrefD6gefLwsLz1cNuCGA-K9HLtS0nXirdk9nWKXIeZKmwwzqvmTDmy5kJ6dClTk5M85IhJLyBkBeISozT6OJY6GZfbCHiAHkACJ0UVH2_-WpfNsTJ9Ii31N1Ry-JGnlKnxnmQok0u-J5X3M-oZlhL6o7FbGRhbnXGTSe1sIJzKKfPo2OIaLhfTQ0lTgL-dGGb3gwKcd49BX9f8ujSxDhaqQam4k93ysPdF6WbcsZYxHoFllVH4ymviQx9fJaVG2I21D8xb9QlNuOkGICEzSYS-qYptgvEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lm2ud66OhaZlcPTB7cqR17Lmd9St0Z8HUYhJjFUhubJhS1cn_1S_mKVmFkznyrASCj656UBbmRXT0kJZWSAjwIGV6jr_hIvFZ8YGZy6e-fmcnHGOXPvXJnyhyABVJ33nXAOZmqwwOu6fTUU1tLCfsR_AMjsrNl34lxOIV2mGIt-lrA8mPSt4TmYaQBAH8ViJe6dVKhCV65BPYMTMhJvmhZUxgXo53JY1Ee_6W_rVLBQqICAjLU7YFYCtQwg2tf8CdQUqWosojLHOVopq5OTRYmjlNH2zdklphRKIQLAX4jLARkq6ScXREFLitniQdKo1JFhTo3e7SZW72G4x2jDRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2XuSozGut7Xyb3v7ajrls7qs8VfMWOz8IucLL6yoPQqQA_Nl9jCUQft2238-lq6L60jh3MXZ6UWtRXB0MxenTPXe7hW2XkxObu2b7HN1komFwz0WPlE5fuCcqY6QiIUO2OiTITkzQLZwWBHKIJCWrZ9x970qNcdSK4u9uaTrtEuynwc4Pes9WXJmVUrbPzpbK0upR6aw56qfCtFAqxx0CQV6gVklXYHpE6tDsw6H5sP6INNBJmdUFaoL6OcDCKSr0l4Uyt5PBzbB19VDowl2dnGeI3BGjMcWK14dTXv014pydKN-o0LYUbG0YI4IFkpIW75pmwI0otW39zfb-Y9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D61d7ASC9n5WH6eX_Ccw9lVMIR-y1B7HHRvGX_bQLKbh6tCR6YVjXM6LZROJrcbf6B55CcY4x1iuPykmDf7DC01TdllTHwt9NXbTR-MVW5T8ROj-yW3pXDpb34Mj__tAlWbwcgaZo1Z_0bvguP0nYb9szA-6aGDe8qivoUxuuFqbFh2XPmbvylF0VwJB_4ITP1e_1t17vp10JlX-qeLY-AW6UaZWPLQh7wOEFwKOf1VrR24wMEQbH5B9---CR2S1SxsCOkj3hNLRdVLPwtzKzpfQHQKqYeXLpnHM6pjAeedRxaVKg7Jz6JQ1NoVKj7cDhFi1hQlAEfp5LJf5N5ISJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طرح‌هایی در راستای راه اندازی موج خونخواهی رهبر شهید
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/666586" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4722481f4.mp4?token=NHH8c_u0NBfWch8ctqmyj0tdD8zc9bkoDb5NGKgaZWbAZyW3M-vJs7x8GVeGcwJd9B9WyqZ7ddT_VMY9IHOHDz_DFjOy4GBv2UDPWiGSvJ8wVB4lbXrZewKi4IJPPbnOScPhiBRUwh_n5sftVZRLJWnu6gKVe3cNmWy_-F983-G8UYN4OGFNryRTiRAtQJe0gogcfbtt8ds6wwxwTFutOUaiePnvcpf4S4-v5XXrN1nBykokg0YgpWGWiOnG18RZX0DvEqBtjOJrMBcl0nqjm3HJpJy0YU6QpG_doJbWl0CkImPnaiFEB5WAQVgs8M6cQBvqa8uRPKIWnQF03zv_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4722481f4.mp4?token=NHH8c_u0NBfWch8ctqmyj0tdD8zc9bkoDb5NGKgaZWbAZyW3M-vJs7x8GVeGcwJd9B9WyqZ7ddT_VMY9IHOHDz_DFjOy4GBv2UDPWiGSvJ8wVB4lbXrZewKi4IJPPbnOScPhiBRUwh_n5sftVZRLJWnu6gKVe3cNmWy_-F983-G8UYN4OGFNryRTiRAtQJe0gogcfbtt8ds6wwxwTFutOUaiePnvcpf4S4-v5XXrN1nBykokg0YgpWGWiOnG18RZX0DvEqBtjOJrMBcl0nqjm3HJpJy0YU6QpG_doJbWl0CkImPnaiFEB5WAQVgs8M6cQBvqa8uRPKIWnQF03zv_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جکسون هینکل، فعال رسانه‌ای مطرح آمریکایی: سید علی خامنه‌ای در مقابل هیولایی به نام آمریکا ایستاد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/666585" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c9ff5ee.mp4?token=nNyVOxqrVmI4oEwFvPQuSrvkJdWRZJI8QdEnW38PuGnXsNz5vyvo7ReuBOhDbPwjq52Q1WP9GApfR5foOw-oGDKLWfIYlTGcE58TDPWyXdzuIq6R6do6BjtgUFRIv-aKvUwqr_q6BT6c-VChSCwYEfkJSyfbJ0xzNXV34zjAnwewjfGhxkFRokGiOCtTbCbzmY8Lopb6wXSNhxSsEo149w_qADX0UROiaLBGk0n-yad4LK-2MtBm2IXfGknhJhQQQd11XIanr3dGfCzAMEVByCXQkKxPuSSO-shyAr-c6f_Grj0LzGOpzfWa9BVTjp-lVnEy76564Gk1Cs0K9NTqrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c9ff5ee.mp4?token=nNyVOxqrVmI4oEwFvPQuSrvkJdWRZJI8QdEnW38PuGnXsNz5vyvo7ReuBOhDbPwjq52Q1WP9GApfR5foOw-oGDKLWfIYlTGcE58TDPWyXdzuIq6R6do6BjtgUFRIv-aKvUwqr_q6BT6c-VChSCwYEfkJSyfbJ0xzNXV34zjAnwewjfGhxkFRokGiOCtTbCbzmY8Lopb6wXSNhxSsEo149w_qADX0UROiaLBGk0n-yad4LK-2MtBm2IXfGknhJhQQQd11XIanr3dGfCzAMEVByCXQkKxPuSSO-shyAr-c6f_Grj0LzGOpzfWa9BVTjp-lVnEy76564Gk1Cs0K9NTqrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مردم در مصلای تهران: ما همه خون‌خواه پدر، گوش به فرمان پسر
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/666584" target="_blank">📅 22:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666583">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
استان میسان عراق چهارشنبه و پنجشنبه را تعطیل اعلام کرد
🔹
استاندار استان میسان عراق روز شنبه اعلام کرد که روزهای چهارشنبه و پنجشنبه آینده به مناسبت تشییع پیکر حضرت آیت‌الله خامنه‌ای در عراق تعطیل خواهد بود.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/666583" target="_blank">📅 22:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666582">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تأکید عراقچی بر ضرورت خروج کامل صهیونیست‌ها از لبنان
🔹
وزیر امور خارجه امروز در دیدار عضو هیأت رئیسه جنبش امل با تمجید از پایداری و استقامت مردم لبنان در برابر تجاوز نظامی و تهدیدهای رژیم صهیونیستی، بر موضع قاطع ایران مبنی بر ضرورت پایان قطعی تجاوزات این رژیم و خروج کامل اشغالگران از لبنان تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/666582" target="_blank">📅 22:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666581">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/splcktFa8bjGSb6xchVx_-IB-n9CHQNTe_Bymc_DrZBPKgDt0Lp3NdKSZs73V1MQdnHEvfk0niW-K9RIf6gBo5DNx0ajRW_CVWF_mPAlotkUDpAjC0HG2vZlpSrV6kMs0171yfzus4-NaZtyB85SFX9bekSObJqgsjqg42WrhWfLtqXYg20yIkdBL4VAJjMm5TW8YtHUytcm8XZsNvsI4umMTZhofkaLYio6shlfJ4UPUWJeidOty2w44BBrHRUrtGgwbJCFqkd5GxVwBogy6ujRBGyCWyjVpBwG0cF0UUp4ymt2W7kOM1PpTR9VReFbMyZEpuLZJ8B9H2GY9WoKFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
هموطن گرامی در صورت
سرقت یا گم شدن
تلفن همراه،
امکان ثبت و پیگیری آن از طریق سامانه کشوری
همیاب24
در دسترس است.
اعلام سرقت از طریق لینک زیر
⤵️
https://hamyab24.ir/l/kbi
https://hamyab24.ir/l/kbi
سریعتر اقدام کنید؛ سرعت عمل در ا
علام مفقودی، 50 درصد احتمال بازگشت گوشی را افزایش می‌دهد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666581" target="_blank">📅 22:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666580">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqbJYzzKRoikUmJH-iYrb6ikZzlklRHYg9XZHYGIC0JuLOJOWI46tFBvclmSU9o3i_eFqrJVOGEgYFDM8rpJPvjUluqtK6RQzHzfsuGMKbNfjJeEpyd8MR5ro6Ji2tt4YeqLMb0WyoI78iIfvQ_Cn8P5pq7XW8dZ7rTYGt-V-Gzq2kKrvhqW55eqSCmhZcPH_eIG1Jd01PIFYKvUgFokpmE7sDUFXRLon3WvWYoD4Zc5OJcnwJm2gYW9nFN9b0baT3spvualpfNNXh8anDU6NfxPdMY1q5mkke6b_fsTkhl5tofDsZJNnbTuSp320ypT7MePRwLtT6Nmy77ZesxKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر شبکه خبری الجزیره از مراسم وداع با رهبر شهید انقلاب در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/666580" target="_blank">📅 21:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666579">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
محاکمه یک ایرانی‌تبار در لهستان به خاطر انکار هلوکاست
رسانه لهستانی Notes from Poland:
🔹
دادستان‌ها در لهستان، یک شهروند آلمانی متولد ایران را به دلیل اظهارات انکارآمیز درباره هولوکاست تحت پیگرد قانونی قرار دادند.
🔹
او سپس این اظهارات را در یک ویدیوی آنلاین منتشر کرد. در صورت محکومیت، او تا سه سال زندان محکوم خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/666579" target="_blank">📅 21:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666578">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حضور رهبران تاریخی مقاومت در مراسم وداع قائد شهید امت
🔹
از امام موسی‌ صدر تا نلسون ماندلا و.....
آزادگان عالم در خیمه حسین‌اند
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/666578" target="_blank">📅 21:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666577">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f8803cf1b.mp4?token=nSrqFcXr8gQ-9YTpIZiz0bjZwjT8BXf3qprR5XUkYESAF_JjPOkpR_tMzYtQyvSRmEPTjMZJNLLAideKZmCVAQmp7Wa_3UEoOGxczkd9_VnCS6BYPnFMQTf4wyVdf9bArjUm1oWQ0jQh53Fu5LqaGHaIARQVP_mTiJ_UWQ2BV_jnAa0Vy9xeYpF8pD4cLqch46sSUgQ_sGt2OEzPIjRuZinAc31Iwt67JdWz8__F0UfYtzbzNo0aUAQFfHA0pKNewvBfkZgvHzcC6QiEEP7ev3gnkSzn248q6OHINybL9z3cGSnsxQk8hINtRpSn20cRNX5tzDb7PVDkxeLIh5319w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f8803cf1b.mp4?token=nSrqFcXr8gQ-9YTpIZiz0bjZwjT8BXf3qprR5XUkYESAF_JjPOkpR_tMzYtQyvSRmEPTjMZJNLLAideKZmCVAQmp7Wa_3UEoOGxczkd9_VnCS6BYPnFMQTf4wyVdf9bArjUm1oWQ0jQh53Fu5LqaGHaIARQVP_mTiJ_UWQ2BV_jnAa0Vy9xeYpF8pD4cLqch46sSUgQ_sGt2OEzPIjRuZinAc31Iwt67JdWz8__F0UfYtzbzNo0aUAQFfHA0pKNewvBfkZgvHzcC6QiEEP7ev3gnkSzn248q6OHINybL9z3cGSnsxQk8hINtRpSn20cRNX5tzDb7PVDkxeLIh5319w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول مراکش به کانادا توسط اوناحی
🇨🇦
0️⃣
🏆
1️⃣
🇲🇦
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/666577" target="_blank">📅 21:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666576">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5762c89eb4.mp4?token=KBUdz4Z0BMtXGF918y24OCDgtkOAGbHAsGYFHru6SIC9sfIYOZQJrR8spZGau2v9jsRZhsp8vj0JI2uGtq3HQdjJkeMIVUoHG6IuppXH-Je_AdKToRNVWdORA9eOt0FK33HQH9dniXloSZBtpn-86a6USR7OLolFL2Flz7hZ8bkq7dFJHCBFG-GBQRYkwVFFJchZTGuZ73QSjX5fv_Yi5AFQmobRgdpYASI_rUgXswKew2rUEp76Bltr-YGy5UJEw41sMhZW8VIT7l_ZbT62YZ4XMZJkGqMcewrVw8PxP45q2pHUjmJR4gvg6dMmwJC47R-1DU-5Xp9hOcH4-7LfaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5762c89eb4.mp4?token=KBUdz4Z0BMtXGF918y24OCDgtkOAGbHAsGYFHru6SIC9sfIYOZQJrR8spZGau2v9jsRZhsp8vj0JI2uGtq3HQdjJkeMIVUoHG6IuppXH-Je_AdKToRNVWdORA9eOt0FK33HQH9dniXloSZBtpn-86a6USR7OLolFL2Flz7hZ8bkq7dFJHCBFG-GBQRYkwVFFJchZTGuZ73QSjX5fv_Yi5AFQmobRgdpYASI_rUgXswKew2rUEp76Bltr-YGy5UJEw41sMhZW8VIT7l_ZbT62YZ4XMZJkGqMcewrVw8PxP45q2pHUjmJR4gvg6dMmwJC47R-1DU-5Xp9hOcH4-7LfaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر حسن ابوالقاسمی: بمباران بیمارستان‌ها و کودک‌کشی‌ها و افتخار به آن توسط نتانیاهو نشان می‌دهد که دشمنان رهبر انقلاب چه کسانی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/666576" target="_blank">📅 21:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666575">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2869806eb4.mp4?token=eYSs-GfVb0rza8uvVQM5TR92_7TQ9HSzCCf3JmEV-gk9eMNboI1aV8podfrjQnCuGbecWTedDHYagohiDayxPhnsPyppcBjMJWRmuWDdCOFyeKcX2kBRu4J9Pkg6ugbYMBtSyNHyRwrPmIwX-rlM1rRIY2Fud_GmgC4gd7FHDMbj30rbZ64ccEJCz_ZNOa7F5X76ZjaBCixig3J6vFkRCY5klvU6pF767EhR5fIeiGwh2N8GGgS_ljSxlHqyCbKPMDdbDXEOVU1g6yTggdwdYGsGhPg3l6dRSm388nw_-2R5PyBDKrgmq7V_xFXlVeiaN3tNSEoT3ZxV2mPSAmCL9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2869806eb4.mp4?token=eYSs-GfVb0rza8uvVQM5TR92_7TQ9HSzCCf3JmEV-gk9eMNboI1aV8podfrjQnCuGbecWTedDHYagohiDayxPhnsPyppcBjMJWRmuWDdCOFyeKcX2kBRu4J9Pkg6ugbYMBtSyNHyRwrPmIwX-rlM1rRIY2Fud_GmgC4gd7FHDMbj30rbZ64ccEJCz_ZNOa7F5X76ZjaBCixig3J6vFkRCY5klvU6pF767EhR5fIeiGwh2N8GGgS_ljSxlHqyCbKPMDdbDXEOVU1g6yTggdwdYGsGhPg3l6dRSm388nw_-2R5PyBDKrgmq7V_xFXlVeiaN3tNSEoT3ZxV2mPSAmCL9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: ملت ایران عاشق رهبر و میهن خود است؛ مردم ایران خواهان انتقام بوده و خونخواه اصلی رهبر خود هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/666575" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666574">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ممنوعیت پیش‌فروش خودروهای وارداتی در مناطق آزاد
🔹
دبیرخانه شورای‌عالی مناطق آزاد تجاری ـ صنعتی و ویژه اقتصادی، هرگونه پیش‌فروش خودروهای وارداتی در مناطق آزاد را ممنوع اعلام کرد و نسبت به فعالیت افراد و مجموعه‌هایی که با عنوان پیش‌فروش خودرو اقدام به جذب مشتری می‌کنند، هشدار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/666574" target="_blank">📅 21:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666573">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7c265df.mp4?token=tc0FKoxOdE4r9D1DRx7eW1AeEBTrXn_mGXl_Bp80nw_onZPxpvbOdYaI7bi9Zk_jEPD9F8VvleOfpmpS_xwCoV2JtPh7GesivK3TE5YG5m2hfgg97kyDjPUj2OholOZDtgm6sNlO4aNL1JQvjOtOh43yiYom58ITmxYiUact0X5a-uqMBSgeHlRzs7SmcX68yeCoVwIZZtyvLYBGuBT3Ml44Y_mfQKJJbl9w52VnsUYFH0na2ibWRo_CzS65_3zeJsl2ZykbiR7tQF5EwmeEQeFKfR7dH0aEc_uAawo0aiGea5UlVhj15lj6MKr4K7jTxJxtf_ItH4jEeEE9bWDikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7c265df.mp4?token=tc0FKoxOdE4r9D1DRx7eW1AeEBTrXn_mGXl_Bp80nw_onZPxpvbOdYaI7bi9Zk_jEPD9F8VvleOfpmpS_xwCoV2JtPh7GesivK3TE5YG5m2hfgg97kyDjPUj2OholOZDtgm6sNlO4aNL1JQvjOtOh43yiYom58ITmxYiUact0X5a-uqMBSgeHlRzs7SmcX68yeCoVwIZZtyvLYBGuBT3Ml44Y_mfQKJJbl9w52VnsUYFH0na2ibWRo_CzS65_3zeJsl2ZykbiR7tQF5EwmeEQeFKfR7dH0aEc_uAawo0aiGea5UlVhj15lj6MKr4K7jTxJxtf_ItH4jEeEE9bWDikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ستاد بدرقه «آقای شهید ایران»: مراسم وداع با پیکر رهبر شهید انقلاب تا ساعت ۸ شب فردا در مصلی امام خمینی (ره) برگزار می‌شود
🔹
بدرقه آقای شهید ایران در خیابان دماوند بعنوان مسیر اصلی تا میدان امام حسین، میدان انقلاب، میدان آزادی و به سمت بزرگراه شهید لشکری صورت می‌گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/666573" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666572">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55afbb1663.mp4?token=T2TBlwLXzWCfT7nOAjsJJeRI3jTwh8l7QMrxGNZKhSROc19bxsrEiLzq3YVSsPBDTHCF2OhWFM208l4vC6Zp-U8_O5fUuPcuDhb4xx__GF2thr9lZLXZ28yVlRiPOBP3hS9xdi1IER78NG6pAsZD9Dj8oqTAq64HrgITtGXnkvzNIeJrScC9cv6mRsrLsoxeFJgBppVkEgq50gf5k2ttmjILJ3NUx90CYmTQCuIRIl2T7f0jr0YlVyqYhT-N5JLgPYKSRUKOqFqG8hkXzPO2bGfZnaUkv1bPEtJnMDrVrURqdixtLRVvAQvdQehXIvO_KknHKiyUA6CvU-vsSwOyKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55afbb1663.mp4?token=T2TBlwLXzWCfT7nOAjsJJeRI3jTwh8l7QMrxGNZKhSROc19bxsrEiLzq3YVSsPBDTHCF2OhWFM208l4vC6Zp-U8_O5fUuPcuDhb4xx__GF2thr9lZLXZ28yVlRiPOBP3hS9xdi1IER78NG6pAsZD9Dj8oqTAq64HrgITtGXnkvzNIeJrScC9cv6mRsrLsoxeFJgBppVkEgq50gf5k2ttmjILJ3NUx90CYmTQCuIRIl2T7f0jr0YlVyqYhT-N5JLgPYKSRUKOqFqG8hkXzPO2bGfZnaUkv1bPEtJnMDrVrURqdixtLRVvAQvdQehXIvO_KknHKiyUA6CvU-vsSwOyKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی رفتن‌ها، فقط نبودن یک نفر نیست؛ انگار بخشی از وجودت را با خود می‌برند. بعد از تو دنیا همان دنیاست، اما دیگر هیچ‌وقت برای ما مثل قبل نمی‌شود. دلتنگیِ تو پایانی ندارد
🥀
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/666572" target="_blank">📅 21:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666568">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9160db867.mp4?token=b-IkF9ji8PGkqZ9GRptU6S9b3dw9GTg8YS7z94GVRZBupJeZ_Jq_jIyBivoV1T_4ykIJQTffa2OWAP2zyDLUzvp4IR4szsVU7JHDz4eTnl3f6Bp1YFKwkBnNl-UHKxsK3DSGRaDpVZyfZltPagLwmnTzGlEvT9Gohh7whEPRQVj3qSFQNo-rxvwWH0MXC2wVRhL3ZNQ9NjxphpKFfwurSeKoKFSIvVzqFmDrLrCFqi626EwW7H3b_tRRYOtPicUY2hXnyk_xHw21--xrpTXWVnu_eVEbOSyXvOSHS9L3asFoXAuNlbUnoEDPrPCR6CjvI1e6u-QM5buLJ6MTtRF6SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9160db867.mp4?token=b-IkF9ji8PGkqZ9GRptU6S9b3dw9GTg8YS7z94GVRZBupJeZ_Jq_jIyBivoV1T_4ykIJQTffa2OWAP2zyDLUzvp4IR4szsVU7JHDz4eTnl3f6Bp1YFKwkBnNl-UHKxsK3DSGRaDpVZyfZltPagLwmnTzGlEvT9Gohh7whEPRQVj3qSFQNo-rxvwWH0MXC2wVRhL3ZNQ9NjxphpKFfwurSeKoKFSIvVzqFmDrLrCFqi626EwW7H3b_tRRYOtPicUY2hXnyk_xHw21--xrpTXWVnu_eVEbOSyXvOSHS9L3asFoXAuNlbUnoEDPrPCR6CjvI1e6u-QM5buLJ6MTtRF6SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
کلیپ های رهبر شهید حضرت آیت الله سید علی حسینی خامنه ای
همونی که براش نمردیم
آخر سر فدای ما شد ...
#رهبر_شهید
#استوری
@Heyate_gharar</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/666568" target="_blank">📅 21:37 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
