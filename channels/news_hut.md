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
<img src="https://cdn4.telesco.pe/file/eGFEi3ORE3IVwqZ1fwZJWmaoi4ShnvAX42LasSw0K2gRsGpszqN1w4FMKLdOnNqhyTCABI_-2av5u46eCNddOpwz2y3hyHeKhGNRGXqufOwLUg8PtuE0jTVQQdEfL0AwDnCP468DmG6TRkSeWs2-EGwCw_5YnetNMqLMNhogOG5GTjHjd49eGu85fVwljVuupWiOYoYG7yq3cR4rrm-HTayYb4R0SYgm_M6ZtpGJSP30yHTW73r6c6LKE7hpsCEQH3AGm1m1SJsaZnzT9QlUtL2ye-dg0ZxtITU6TX72EArnK59Tjlh7T85z7VCtPobfF81i71ZmulAQ80Ro01MbtQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 02:39:50</div>
<hr>

<div class="tg-post" id="msg-72871">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را #رایگان کردیم برای 100 نفر اول
👇
꧁༒VIP CHANEL  GOLD༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/news_hut/72871" target="_blank">📅 01:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72869">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را
#رایگان
کردیم برای 100 نفر اول
👇
꧁༒
VIP CHANEL  GOLD
༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید
لطفا رعایت کنید تا حق خودتون ضایع نشه
🙏
چون عضویت فقط برای 100 نفر بازه
هرکس سود کرد دخترم و همسرم رو دعا کنه
❤️
🙏</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/news_hut/72869" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72868">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/news_hut/72868" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72867">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h6H-c0zMa68aZcSD7vTWLYBziAum_Tx0xp75acXGglNdkKQbzXdy_1fuFfJjVApHsmTHwQsZnDFoOCM37dwl4UanOelLnWSjy7vlaDfUYQ2NMLWpnZXjx5TgOSk7fxotKv-uY6rnl0Uy9eJpbex8qM0ewUY3Td5JOWlDxNiBNGOuZpSgUBFlrY_SgB_7rntC8BMxbODKfrwcKdkglCaDh76zMOyYX_2MczGXVOJIzT3WCnmdwC4_wqQDtYzR3IbTl2hUapuqc0lnVEP2mcpxy9ajoX8__nD2g_S-lpbcv80QFRgbCxm4e8QIPp88XvHyNXqecnmqykx6BkAZ2WAeig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/news_hut/72867" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72866">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzxsvq6m-knJXcHxKcD0Ue-Vc-_hzcT6fOXB9NCZYUI0NsXpzdu7omV8c9G0eydR_D_zt5MDjShPKcwCRP3xIasjT3K2ssElV3eNaZRTsbWGdxRQACyc6pskC0vXNEV3VUsndAbkK9l11rvYeQy7Ao6A_6M-ojPdpVGTHfc_udgCUhpiZMFkhJU1Qh0V2YaivoEJ4BRwlxcvYRUkU9v9VZrbiYWEXO6AN-O39sKnXDU8QPk_ATibHCRvhW53Vqkz5MtqdSqEUMKL2eGfMJiA-Bia0lUjBfjibGcmfjQj3oni0WiUVS-0h8T_7ZKGVzwMyqwPqlIE6pAGZRCk8Eo1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا:
«ایران یه وزیر نفت جدید داره.
با توجه به اینکه ایران از ۲۵ اوت حتی یه بشکه نفت خام هم روی هیچ کشتی‌ای بارگیری نکرده، این وزیر نفت دقیقاً قراره چی رو مدیریت کنه؟»
@News_Hut</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/news_hut/72866" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72865">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=rIaxJec51KH7R1ovIgu6byq0_aTq-IlL_WjBKzKEuRsQTG0h6AtEtx-F5zVBtw_q7ui_K70NWaD363ZHnEdwUnaYeAXquXaZtlyqb-YJhcoAR6SHy7TXjV6YV-ttpJO4PLdpgN-YveCIUd25fcMnjGeJK1z5D20wjUu-L8I7wJ7AyDtgu7tCVJ-MPIe9GztGI3VWaZAW9aalMoV_lVsnXYRYyHOz4-sLQhaXLjaXewySgxdTRwaQIAIU7NYp1CwdWMJE_iICxXyJIFcHy2ITVsYM6N0LjWzPEH8Dxrm02DSt6b0Q4iCyO5JvW2NT46uf5h1r3eTNp5cxNrh7N-l5joWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=rIaxJec51KH7R1ovIgu6byq0_aTq-IlL_WjBKzKEuRsQTG0h6AtEtx-F5zVBtw_q7ui_K70NWaD363ZHnEdwUnaYeAXquXaZtlyqb-YJhcoAR6SHy7TXjV6YV-ttpJO4PLdpgN-YveCIUd25fcMnjGeJK1z5D20wjUu-L8I7wJ7AyDtgu7tCVJ-MPIe9GztGI3VWaZAW9aalMoV_lVsnXYRYyHOz4-sLQhaXLjaXewySgxdTRwaQIAIU7NYp1CwdWMJE_iICxXyJIFcHy2ITVsYM6N0LjWzPEH8Dxrm02DSt6b0Q4iCyO5JvW2NT46uf5h1r3eTNp5cxNrh7N-l5joWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره طاعون در روسیه، با پوتین صحبت کردید؟
ترامپ: «به‌زودی یه تماس باهاش دارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/news_hut/72865" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72864">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=F9XoH5mI9GPdVUkgq0TYPMqXuWqSjd69YwLzS1l_BtBpX8pR7LMILI7j5WnVv3YO0kAkUJoWfkJDQj4Zb8ThQXQPJKnFhAWtaCCx84IvxjjChgKsNm3Hk3VsAajZZRHWzNjJPCtuwzbCfIDhQ-sKuRhb18ESqgg3bQp5eXI3cx-GQsoiO0JguES53kCqk_QZYoEvpGkHmYuEqD8O-yilxOlV8YzEQWR5ofH5iz4frNWmaMIPfAyvLUI2bYiBmEu-Q5kNTetnIY6LDO56QMUsHy2SH64RlDmpnLm9U7VbKTtBMl7EgVpVtu59J8K3cA2e7RhaQ78xrwSS8kMQMFNgJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=F9XoH5mI9GPdVUkgq0TYPMqXuWqSjd69YwLzS1l_BtBpX8pR7LMILI7j5WnVv3YO0kAkUJoWfkJDQj4Zb8ThQXQPJKnFhAWtaCCx84IvxjjChgKsNm3Hk3VsAajZZRHWzNjJPCtuwzbCfIDhQ-sKuRhb18ESqgg3bQp5eXI3cx-GQsoiO0JguES53kCqk_QZYoEvpGkHmYuEqD8O-yilxOlV8YzEQWR5ofH5iz4frNWmaMIPfAyvLUI2bYiBmEu-Q5kNTetnIY6LDO56QMUsHy2SH64RlDmpnLm9U7VbKTtBMl7EgVpVtu59J8K3cA2e7RhaQ78xrwSS8kMQMFNgJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌گن: اوه، ما شش ماهه که درگیر ایرانیم!
ما عملاً همون لحظه‌ای که بمب‌افکن‌های B-2 حمله کردن، کار رو تموم کردیم؛ چون با اون حمله، برنامه هسته‌ای‌شون دیگه تموم شد و ۹۵ درصد دلیل این کار همین بود؛ شاید حتی ۱۰۰ درصدش.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/news_hut/72864" target="_blank">📅 00:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72863">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gH2fibY0-2xqkNvoMZ1gwH5karxUDVfEWK992RobdYm7-JWNW7hmiHM_KRX9r0jOpCAOljckeARcw036LVKNcPsfuNdSpPFXiipFtHnyMVx4Mz-m6h4ZGOtm6e9wgowWgdfOc0KFCgZU1Ti-jBH_7yvJb1w3AxCdr_cPptVr3OssWvZwAiXw2ozzWdSIIYyjwG5pKIc8AsfvzWlJdgfi7yzp2rzmu64jE4YYLpkLhpdcWv3jANzxIrluFQbsOIcbT04XqKUY-m09q4NGmtO-uI1Dh3V73S1PTJC4T1sovDKKwf4_xC0LfFHzH3Hk25pLyV1lZZZWVDEEKLR48oQ-9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gH2fibY0-2xqkNvoMZ1gwH5karxUDVfEWK992RobdYm7-JWNW7hmiHM_KRX9r0jOpCAOljckeARcw036LVKNcPsfuNdSpPFXiipFtHnyMVx4Mz-m6h4ZGOtm6e9wgowWgdfOc0KFCgZU1Ti-jBH_7yvJb1w3AxCdr_cPptVr3OssWvZwAiXw2ozzWdSIIYyjwG5pKIc8AsfvzWlJdgfi7yzp2rzmu64jE4YYLpkLhpdcWv3jANzxIrluFQbsOIcbT04XqKUY-m09q4NGmtO-uI1Dh3V73S1PTJC4T1sovDKKwf4_xC0LfFHzH3Hk25pLyV1lZZZWVDEEKLR48oQ-9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«نیروی دریایی آمریکا یکی از مؤثرترین و نفوذناپذیرترین محاصره‌های دریایی تاریخ رو اجرا کرده. هیچ‌کس تا حالا همچین محاصره‌ای ندیده؛ حتی یه کشتی هم نمی‌تونه وارد بشه.
اگه کشتی نفت داشته باشه، به کابینش یا سکانش می‌زنیم؛ اگه هم نفت نداشته باشه، کلاً غرقش می‌کنیم.
الان محموله‌های نفتی که از خارج ایران ارسال می‌شن، تقریباً دوباره به بالاترین سطح خودشون برگشتن.
یعنی به زبان ساده، تنگه هرمز متعلق به نیروی دریایی آمریکا و ایالات متحده‌ست؛ جای واقعی تنگه هرمز هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/news_hut/72863" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72862">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU6737mHcPZjIjhqFd5nLOteQBYP7Q9NzgWoSmVWlqTP_kK-mjuWmE-EcPN0iG5wPcDk4Ey8cxns5hNO8tBwjYsulmRVgDCLW6EUhl2mmvsmH5ZYhe28ib7sWsEhab_UXYFuL5anYkaT41Zkq1BtTMBb8DsXXUf1taq_GYuGeRdYqzzyui-PSmk2BHBxuY-P-XnOjUV05YcSW3FvTQ2HLMG8vgshx0NXiRyNMulJkKZHQr3ZjjM70pVNkMtRo3X6T5OeHbY787_wj3irfPd2lim45y-lh83bJV2vk3_czoJpczD9rw3f1E4ilDbvhASBELeXz6KlStRGliSz8qC3RadeCUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU6737mHcPZjIjhqFd5nLOteQBYP7Q9NzgWoSmVWlqTP_kK-mjuWmE-EcPN0iG5wPcDk4Ey8cxns5hNO8tBwjYsulmRVgDCLW6EUhl2mmvsmH5ZYhe28ib7sWsEhab_UXYFuL5anYkaT41Zkq1BtTMBb8DsXXUf1taq_GYuGeRdYqzzyui-PSmk2BHBxuY-P-XnOjUV05YcSW3FvTQ2HLMG8vgshx0NXiRyNMulJkKZHQr3ZjjM70pVNkMtRo3X6T5OeHbY787_wj3irfPd2lim45y-lh83bJV2vk3_czoJpczD9rw3f1E4ilDbvhASBELeXz6KlStRGliSz8qC3RadeCUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«من مدام از رهبران کشورهای مختلف دنیا تماس می‌گیرم که بابت جنگ ایران ازم تشکر می‌کنن.
منم بهشون گفتم: خب، خوبه! کی قراره پولش رو بدید؟
ما داریم بارِ کل دنیا رو روی دوشمون می‌کشیم. اتفاقاً از این کار هم خوشحالیم، چون خودمون قوی‌تر شدیم و بقیه ضعیف‌تر.
اونا دیگه ضعیف شدن؛ دیگه کارایی سابق رو ندارن. ما داریم کارهایی می‌کنیم که هیچ کشور دیگه‌ای از پسش برنمی‌اومد.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/news_hut/72862" target="_blank">📅 00:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72861">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ درباره ایران:
«ایران یه کشور شکست‌خورده‌ست. همه دارن کنار می‌کشن و می‌رن. اقتصادشون هم عملاً به خاک سیاه نشسته.
وزیر نفت ایران هم گفته: «من دارم می‌رم، چون کشورمون دیگه تمومه.» خودش دقیقاً همینو گفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/news_hut/72861" target="_blank">📅 00:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72860">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=r4h89CcNeXy9iqt2h5F7cI3MKseAC1Np03g56vAqbzqPaE2KMnZq-BaEMvMgdmngx9BlJ_gqXoSlCExpqKqYfYP10OzhiY8Jsr3SRYzcyuRfaa-Q7g1PIuBKaKORF2dE30ErU8ZBhpXsMD3DZjMrK82Kvrff3K-d6jeyOJz_QbiPKiaJ505WywGum8DPEZpCdxN0bIovmeSvbX5XDWF83PIA4J2QDslZw1O1mdUPM41aH9A67NSQQzTfg_4-10f15KplEwV34_AHLRjhCIfygamNOBAGyGlmC8MC7kwQUh_ryrCRqbn4m9UatpsYnPrG6w3W9Urs5oKHAG5RWnoZCibzAvzfL7jrPIAvkXx3_nhJW8WS02TEAkHsY_sRiKjJn0ld3in8aoCtNI-CmobNTGuRorW-0Nj402oCK9-ezblThtDHALXQg2aGQ__3yO9Z7thgVnu-c_t16QuUL33Upgmsrn_w8wIn0zVYWIq7zB2YYJPl15WN8zOhYQBXeUiaIr8MrwlfmbDbUkAe_TQ28RoQUJuvagTnAK_6k07wvGjkjSiFIXd-rzP7DZqyZR007q8jBEy_UmTddTVVYkb8UsBjoggaTmGMQkEANnfbFRuy1jH96GwETCNpUTxgPuPbRTGLo4dmWtdswyWM8seS-3WoXsPER--jRLZPXZwY6s8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=r4h89CcNeXy9iqt2h5F7cI3MKseAC1Np03g56vAqbzqPaE2KMnZq-BaEMvMgdmngx9BlJ_gqXoSlCExpqKqYfYP10OzhiY8Jsr3SRYzcyuRfaa-Q7g1PIuBKaKORF2dE30ErU8ZBhpXsMD3DZjMrK82Kvrff3K-d6jeyOJz_QbiPKiaJ505WywGum8DPEZpCdxN0bIovmeSvbX5XDWF83PIA4J2QDslZw1O1mdUPM41aH9A67NSQQzTfg_4-10f15KplEwV34_AHLRjhCIfygamNOBAGyGlmC8MC7kwQUh_ryrCRqbn4m9UatpsYnPrG6w3W9Urs5oKHAG5RWnoZCibzAvzfL7jrPIAvkXx3_nhJW8WS02TEAkHsY_sRiKjJn0ld3in8aoCtNI-CmobNTGuRorW-0Nj402oCK9-ezblThtDHALXQg2aGQ__3yO9Z7thgVnu-c_t16QuUL33Upgmsrn_w8wIn0zVYWIq7zB2YYJPl15WN8zOhYQBXeUiaIr8MrwlfmbDbUkAe_TQ28RoQUJuvagTnAK_6k07wvGjkjSiFIXd-rzP7DZqyZR007q8jBEy_UmTddTVVYkb8UsBjoggaTmGMQkEANnfbFRuy1jH96GwETCNpUTxgPuPbRTGLo4dmWtdswyWM8seS-3WoXsPER--jRLZPXZwY6s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
«ما توی جمهوری اسلامی ایران داریم خیلی خوب پیش می‌ریم. کل اونجا دیگه داغون شده.
باید کار رو تموم کنیم؛ فقط مونده تصمیم بگیریم چطوری تمومش کنیم: با راه خوب و دوستانه، یا یه راه نه‌چندان خوب!
خیلی زود می‌فهمید قراره کدوم راه رو انتخاب کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/news_hut/72860" target="_blank">📅 00:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72859">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423715c427.mp4?token=mOUVpF7Nt69lxW8KssW62GYDx5OcJ9nZJPzrR0P-_uOWeiZNbVupVOAzBLfh9IvCFCJCKs1eBz9JuLQ6swoBVfrNIztnf93OBgKJCutrrXinB_0bRg9tn6Etj250GpKznnQEbzpA3tgZ9htVRY1kyjxS5jZ0bg1ok4r4KBpDC-ulJcND0-kNnMvzzYtHYa79GAmUPI0XYouWDIYv5gxPMTpOeTYDw8x9dlDgd_iHZ8vC3B6wdx1TjvTAnIo9J0cZz-DmvIIKOH_cyNKqokng5C69X-h1awHsy4lZJLWlrrtgmDwXXPGgPP1rO63f2LvjhYz4B0V9cLk-8t3nUx71fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423715c427.mp4?token=mOUVpF7Nt69lxW8KssW62GYDx5OcJ9nZJPzrR0P-_uOWeiZNbVupVOAzBLfh9IvCFCJCKs1eBz9JuLQ6swoBVfrNIztnf93OBgKJCutrrXinB_0bRg9tn6Etj250GpKznnQEbzpA3tgZ9htVRY1kyjxS5jZ0bg1ok4r4KBpDC-ulJcND0-kNnMvzzYtHYa79GAmUPI0XYouWDIYv5gxPMTpOeTYDw8x9dlDgd_iHZ8vC3B6wdx1TjvTAnIo9J0cZz-DmvIIKOH_cyNKqokng5C69X-h1awHsy4lZJLWlrrtgmDwXXPGgPP1rO63f2LvjhYz4B0V9cLk-8t3nUx71fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«یادتونه خمینی رو؟ همه‌شون دیگه نیستن؛ همشون رفتن.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/news_hut/72859" target="_blank">📅 00:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72858">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=V85QTZjHj_MT5NE4Xpv0oIHE6UG5VCJqujGWDkS7_umJAsmV5SirZCGi4Fh3dUnepZSjYuzsnEIiA9M3h7nDR57nVdJodbZiyFH_jnc7fQhdl5btZN_Ah43iuCNvLcAAhF7UEsJYYPsHQfzauP27NzikUrkXPn9751TOzrVnpDaTa9jgeeTgrv9b-yXi2fhkrQt8YRcO2p79tFjhKOmrmXO8ncpCv8jsTM-oiIUH1O_DgSRexFCwWxihq3JPblmUwzcdK9biX4zHjygmnMVTWIhIjOGdRE504rrwEuBsFpdsPjJD0YuWj98_sJhHFyqLdSaY9SFBkLeKNi2r0Z3bLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=V85QTZjHj_MT5NE4Xpv0oIHE6UG5VCJqujGWDkS7_umJAsmV5SirZCGi4Fh3dUnepZSjYuzsnEIiA9M3h7nDR57nVdJodbZiyFH_jnc7fQhdl5btZN_Ah43iuCNvLcAAhF7UEsJYYPsHQfzauP27NzikUrkXPn9751TOzrVnpDaTa9jgeeTgrv9b-yXi2fhkrQt8YRcO2p79tFjhKOmrmXO8ncpCv8jsTM-oiIUH1O_DgSRexFCwWxihq3JPblmUwzcdK9biX4zHjygmnMVTWIhIjOGdRE504rrwEuBsFpdsPjJD0YuWj98_sJhHFyqLdSaY9SFBkLeKNi2r0Z3bLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:
«ده‌ها نفر از سران تروریستی ایران رو از هستی ساقط کردن و مستقیم فرستادن اون‌ور، پشت دروازه‌های جهنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/news_hut/72858" target="_blank">📅 00:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72857">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=nmfLxZvdZ4f_BsqLxsXLtmqX0xqdBl440p5J-HD2pXub2iWC0LhgO5_MzHagNkuiX_8Aj90ZM_rI463k91qIph9uT_E9tNEgyZYZtmHZus4ThU4sdMNK6dV5fJYVceaaOvsvYNRbgaDCJN2QSaZP1hf8ds_F5lFrpQLTxH5Kz3zIUr60YP18kA31eeYyF7tim4ipnQu_svR5pkkkyp_njBcFgcsueBNIZzQxbyceiyd-fbQNjo_rpWV4W1bYNExVwFSzBtEVlHVkNSJK4nXNagi4vWDofhndikSvjlFLYkc04ZRUvr-04ABfZZ--tjZtJR_krg8aQj7S0-o_5QuU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=nmfLxZvdZ4f_BsqLxsXLtmqX0xqdBl440p5J-HD2pXub2iWC0LhgO5_MzHagNkuiX_8Aj90ZM_rI463k91qIph9uT_E9tNEgyZYZtmHZus4ThU4sdMNK6dV5fJYVceaaOvsvYNRbgaDCJN2QSaZP1hf8ds_F5lFrpQLTxH5Kz3zIUr60YP18kA31eeYyF7tim4ipnQu_svR5pkkkyp_njBcFgcsueBNIZzQxbyceiyd-fbQNjo_rpWV4W1bYNExVwFSzBtEVlHVkNSJK4nXNagi4vWDofhndikSvjlFLYkc04ZRUvr-04ABfZZ--tjZtJR_krg8aQj7S0-o_5QuU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.  @News_Hut</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/news_hut/72857" target="_blank">📅 00:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72852">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/news_hut/72852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/news_hut/72852" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72848">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/txgiXxxEvV-LPb7bmlFhnz4kG757nzBjfOngfVqxoMw4Aut9ARjnG7rib-aioG3uVe1sskDgCV-Yss9eB1z6_dvLRrNmbfzuEBL_-01kvYQc2CR0NFh_Sl7fxrN5kUNPzDAkJ0AZDzy5d55eFFMTf7XRagSHjGDMP2PPSxwqv0oyCU_qyNlIGT6Y9UOHJPYqvhkhjyRTXTDik8pnnN-SzbVzldWIbFjQrT880nHlP37RKzxumYCrZvHyj4sZVH065_ArIkkNhSlV6W39k4btxtpfbuVpp72V7vi91jY3L2ET3ea4I5YllepT_7qvQ_nP_vnbz2gt3XHK1YngntQUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VAFjvLn10hdLdMXBawMpgozMBLXEVQBLG9SHpRMTubejlawjqafFQRMOcATt2DodDEIbE3ukkGuyAsNDW1GLqQHrnvl7Z3z8su-Rs-lFc4kk8KCC4Tx6za-_6gGzvHBD0A1vC_i59DrS4pwZcdr6z6AlNm6zwma09cZ3qm-V9ovnwTRZCjzil8PL6EbAy3sHLI_4Praio2lgDHjX-kJqR_bxzHG3WfZ02IM8Xe9PJyaA6nbwaendDq_j7VsKji0gacvcUXhxEP9drUpVX89zoy9i2GWRS5jI_ksPKTqWiVzDCOZ5oCRHZDPndMr4CevC8JtYeHiqotCa5Z-_lwENXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=oo35xX_pjbd52LmaatCJV2V5Nk0WSDE9-0Y13y225-9mtY79g0hWVHFbs4FrOcEwbMGhPWLZIXW1pDUGj1dfVfyWn8yrzFpDIiQZedhRrkY9S9k9VBJQiILEsFZuq05JyxQIEaPeAFlpkO8RPopXKJy9Clls95dR7w3tt9iEDdJa_PodhOM0Q53QiC6NxxworcJoLa9GQb_Vb85OqTsF7o4zRXPyGCqr3rZcYe0bj5yPeo9vUMw8L2_MnC0VSz__vNXLMXU9VdHraKgw4irG4KsWx3hlBppt16xLn_qjo1vO1ZrJrujJ6r6IirZawIQlVt02Dzmq4b0K6B1Vv7c02Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=oo35xX_pjbd52LmaatCJV2V5Nk0WSDE9-0Y13y225-9mtY79g0hWVHFbs4FrOcEwbMGhPWLZIXW1pDUGj1dfVfyWn8yrzFpDIiQZedhRrkY9S9k9VBJQiILEsFZuq05JyxQIEaPeAFlpkO8RPopXKJy9Clls95dR7w3tt9iEDdJa_PodhOM0Q53QiC6NxxworcJoLa9GQb_Vb85OqTsF7o4zRXPyGCqr3rZcYe0bj5yPeo9vUMw8L2_MnC0VSz__vNXLMXU9VdHraKgw4irG4KsWx3hlBppt16xLn_qjo1vO1ZrJrujJ6r6IirZawIQlVt02Dzmq4b0K6B1Vv7c02Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا صرافی ایرانیه «omp finix» که دارای امتیاز رسمی و تایید شده هم هست، پول مردم رو بالا کشید و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده.
مردم هم مقابل قوه قضائیه دست به اعتراضات زدن و خواستار تعیین تکلیف و پرداخت پولشون شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/72848" target="_blank">📅 23:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72847">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=HynX9SBagFfPAq13e77l5y3Ka7HEMqUZM1FLuJWiuQ3U6NAUUUi8aukPFczYj2b15kUZ5IGc35Z6m7ZDe3Dm1J29PkijpoMM4Si--Dbr46SyGCBRdmtdNYdSQK7ugU9T6Wz3gfxEpwIhQaEkMPpffd9two6ySDEDg-zHg2XbdChiyJFdvoeanqTmKJzUn2WGwpUBmK6TDnJGTjKgq3Jt6ARp0XdZC75HohNrzlEaMnIz27ukpH0o0QFI68iGO4CQ0HDcluVBzsSvOrGwwY7QwkPFHr9KVoxONUa8mL0yNM4NpwweVM2LnCUzwRSbLWrFX0X-liLzLXmAw7CA3iU5gThhC82yq8yiG-cbcyKDyBqKPkt9cnLlZemiXshSw44AljklBVYie8VYKxfaCPpTb-HpTzfaKg4oIf3bn0Qm9wK1kO-zoKNbvFvE9K5mZWTkHB0wBqP_1vmW-C3hSgZ5EtmTjNLbfxUXQ0ltAohlMcRoUeBH1OCo0UXaCFOngwK73TUevAClOCr7ZrQVL0YNf5RJr5HmhJ-sUpdwqq2hGPyGtuLGhwjZ-rRs5YKRsR3X2d5qFZowpQqN9ZyyvUZpS65NTtjGG98DP_sjZURaD9DDAUDv0ApO8A8n8w4BLNKLiGcEGsRidV0TI27OYH06IUiA-wNkAOyb4HW6Pck892U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=HynX9SBagFfPAq13e77l5y3Ka7HEMqUZM1FLuJWiuQ3U6NAUUUi8aukPFczYj2b15kUZ5IGc35Z6m7ZDe3Dm1J29PkijpoMM4Si--Dbr46SyGCBRdmtdNYdSQK7ugU9T6Wz3gfxEpwIhQaEkMPpffd9two6ySDEDg-zHg2XbdChiyJFdvoeanqTmKJzUn2WGwpUBmK6TDnJGTjKgq3Jt6ARp0XdZC75HohNrzlEaMnIz27ukpH0o0QFI68iGO4CQ0HDcluVBzsSvOrGwwY7QwkPFHr9KVoxONUa8mL0yNM4NpwweVM2LnCUzwRSbLWrFX0X-liLzLXmAw7CA3iU5gThhC82yq8yiG-cbcyKDyBqKPkt9cnLlZemiXshSw44AljklBVYie8VYKxfaCPpTb-HpTzfaKg4oIf3bn0Qm9wK1kO-zoKNbvFvE9K5mZWTkHB0wBqP_1vmW-C3hSgZ5EtmTjNLbfxUXQ0ltAohlMcRoUeBH1OCo0UXaCFOngwK73TUevAClOCr7ZrQVL0YNf5RJr5HmhJ-sUpdwqq2hGPyGtuLGhwjZ-rRs5YKRsR3X2d5qFZowpQqN9ZyyvUZpS65NTtjGG98DP_sjZURaD9DDAUDv0ApO8A8n8w4BLNKLiGcEGsRidV0TI27OYH06IUiA-wNkAOyb4HW6Pck892U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار رحیمی: از امروز اگه یک سایت یا رسانه قیمت ارز (مثل دلار و یورو) رو منتشر کنه با اون سایت برخورد قانونی میشه.
جدی‌جدی اینا فکر می‌کنن با پاک کردن صورت مسئله، اصل مسئله هم پاک می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/72847" target="_blank">📅 23:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72844">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=fevPm3vt3dyg90ri-v_Ugm75qyqwA7Iwe4i7LXce11Kf-ZK5BiuCFBiYivI1u8Jfdd1irZoV7ibq4Y-sZtx_gV6bg0QQIiT2SKq95mT2QFztfPhGAsCKY-qwcaQBMHeKI6ytuxN2YuM_jbOffOHhR2Z3q7SoGjSOUkVgvARgQZmEkFMCIGODU5JF9ft0pVAphHt-rjvmwyEHb3qx7TSE50JC91ZPydw18hK1IuWbU6F0EcMvNnHwkXFQ9JuTx_pne349ilhXaMYwR6loh7Wr38Ur-zWpRpUFsu4h0YFp6-B5FAUHpx6tDHopPzi5B0MR2eo_CoYaCOV0Kc9_uR3Ncg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=fevPm3vt3dyg90ri-v_Ugm75qyqwA7Iwe4i7LXce11Kf-ZK5BiuCFBiYivI1u8Jfdd1irZoV7ibq4Y-sZtx_gV6bg0QQIiT2SKq95mT2QFztfPhGAsCKY-qwcaQBMHeKI6ytuxN2YuM_jbOffOHhR2Z3q7SoGjSOUkVgvARgQZmEkFMCIGODU5JF9ft0pVAphHt-rjvmwyEHb3qx7TSE50JC91ZPydw18hK1IuWbU6F0EcMvNnHwkXFQ9JuTx_pne349ilhXaMYwR6loh7Wr38Ur-zWpRpUFsu4h0YFp6-B5FAUHpx6tDHopPzi5B0MR2eo_CoYaCOV0Kc9_uR3Ncg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ توی آب‌های نزدیک سوچی
امشب یه آتش‌سوزی گسترده توی آب‌های نزدیک سوچی روسیه راه افتاده؛
توی ویدئوها یه خط طولانی از آتیش و یه ستون خیلی بزرگ دود سیاه دیده می‌شه که از نقاط مختلف شهر هم قابل مشاهده‌ست.
حساب‌های نزدیک به اوکراین مدعی شدن این نفتکش هدف قرار گرفته، اما منابع روسی فقط گفتن یه شناور نزدیک بندر آتیش گرفته و فعلاً علت حادثه مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72844" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72843">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72843" target="_blank">📅 21:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72842">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ایران در اعتراض به برخورد دولت فرانسه با اعتراضات دانشجویی و چیزی که «نقض آشکار حقوق بشر» عنوان کرده، سفیر فرانسه در تهران رو احضار کرد!
وزارت خارجه ایران هم از فرانسه خواسته به تعهداتش در زمینه حقوق بشر پایبند باشه و آزادی‌های اساسی، به‌خصوص حق تجمع مسالمت‌آمیز، رو رعایت کنه.
جالبه رژیم جمهوری اسلامی که بویی از حقوق بشر و برخورد مسالمت‌آمیز نبرده میاد به بقیه کشورا برخورد مسالمت آمیز و رعایت حقوق بشر توصیه میکنه!
یه نکته دیگه هم که هست اینه که تا امروز هیچ گزارشی مبنی بر اینکه معترضی در فرانسه کشته شده وجود نداره و گزارش های رسمی که وجود داره نشون میده فقط بیش‌ از ۲۱۵نفر دانش‌آموز و ۸۵کادر آموزشی زخمی شدن.
از نیروهای دولتی هم حدود ۷۱۵ نفر نیروی پلیس و ژاندارم در جریان اعتراضات زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72842" target="_blank">📅 20:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72841">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktiZNNkKxXMe4EtE7ikEhmK5UhkFceBH3cNH4do3hg8y8DbjByYZhwUD2RwcKLPBX61L4bn3u9ylUSZDnyPjDa1FTIsVxQpdS_xjAremgHceKgtiPuXbNJIWL2t9F9Zb0y90hLWo8HC2f2DDPB5tYU1Z9uVL4lpKSJ9kRQjhZpPslCiNjC1kCgwbbRUY-ethaS5Sna0-DeixSsK5pO_tMeVEGYBtc69YM5KqeLsxTrLirJzAKVKAx0KH1I7zZxxIVm-prwRk_yOS9G8d-Bn1YLNd8OEz9uClYBMM_xkG4wq5K73womnvGw5-ml1diuRimhuf0L8PRoANuHtSL5mtLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72841" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72840">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">#فوری
؛رایتل رسماً به مزایده گذاشته شد؛ شستا ۱۰۰ درصد سهام این اپراتور را با قیمت پایه ۱۳۰ هزار میلیارد تومان (۱۳۰ همت) برای فروش عرضه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72840" target="_blank">📅 18:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72839">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه مرد ۲۲ ساله بریتانیایی به اتهام مشکوک بودن به آماده‌سازی اقدامات تروریستی، در ارتباط با پرونده مشکوک پایگاه هوایی RAF Fairford بازداشت شده.
پلیس ضدتروریسم انگلیس گفته این فرد امروز توی وست‌مینستر لندن دستگیر شده و هفتمین نفریه که توی ارتباط با این پرونده بازداشت می‌شه؛ البته تا الان برای هیچ‌کدومشون اتهامی ثبت نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72839" target="_blank">📅 18:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72838">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=oR1RCz5I2jYI2QWfj88TmdSwsAbqzcp87r9ltt6QbjHLlXcwMsJ7bfqlUVN-49z7QhYq6cdU4QO0id3ohZPSEGYA66kKl0FWcCXVqha1b8TU2W9WnI2ri0lY9LVyJIBDYhwXJGdywyOgjxxdJiFrzu7J_YqXYoUrYTQyGrY-aGu4-X38p7iAG_eJa1BBubAlrLUR7GwstsJ_xGgUFWHFhRecjbf3jh22EDu1wCmogAuwWoTvZZehipZLUVEyklrH9Goi3w1tmgp2SwcCpzqHmAdutQQZyWq0C4P8-4x8DXyNHBwmcQ2v61Dmd9mbZYhcJywHll6rwbYnJKxWPfpdHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=oR1RCz5I2jYI2QWfj88TmdSwsAbqzcp87r9ltt6QbjHLlXcwMsJ7bfqlUVN-49z7QhYq6cdU4QO0id3ohZPSEGYA66kKl0FWcCXVqha1b8TU2W9WnI2ri0lY9LVyJIBDYhwXJGdywyOgjxxdJiFrzu7J_YqXYoUrYTQyGrY-aGu4-X38p7iAG_eJa1BBubAlrLUR7GwstsJ_xGgUFWHFhRecjbf3jh22EDu1wCmogAuwWoTvZZehipZLUVEyklrH9Goi3w1tmgp2SwcCpzqHmAdutQQZyWq0C4P8-4x8DXyNHBwmcQ2v61Dmd9mbZYhcJywHll6rwbYnJKxWPfpdHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون شاهد نخستین شلیک آزمایشی موشک بالستیک جدید M51.3 فرانسه از زیردریایی هسته‌ای «لو ویژیلا» بود.
مکرون:
این آزمایش، اعتبار و قدرت بازدارندگی هسته‌ای فرانسه رو نشون می‌ده:
«برای اینکه آزاد باشی، باید ازت بترسن؛ و برای اینکه ازت بترسن، باید قدرتمند باشی.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72838" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72837">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=QdOl0JzC7IA9NQCUXUK5WVGEARi5oRjegI0OYfRzX7PmuD95cWE5kVAnvXcQ7L2CAyOWA4xOb5mB5VRRPpcZ_iH3D3ognqJEaC89qmU5G2K2ahc8IhztKpuJ6APDAlF0HJG5YL0pJAz9pkwykEetnKK8gU_2eibU6JGYcfgp1-p6sMjcIq08ZQdUUo-a0qn_flJFcYq3FxRdcTebD5HLHNuT7IEZIxv4Gg13_nXx7H2hYtD3U514I3_F2gRzaR-WCR_mq4sHmn7fqTo_ILR6NxLPmdm5lKxEnovNSCTtn-kPSMW4VOkb6iNE-O_2y-u7eREji1els5sKa7T7sMScwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=QdOl0JzC7IA9NQCUXUK5WVGEARi5oRjegI0OYfRzX7PmuD95cWE5kVAnvXcQ7L2CAyOWA4xOb5mB5VRRPpcZ_iH3D3ognqJEaC89qmU5G2K2ahc8IhztKpuJ6APDAlF0HJG5YL0pJAz9pkwykEetnKK8gU_2eibU6JGYcfgp1-p6sMjcIq08ZQdUUo-a0qn_flJFcYq3FxRdcTebD5HLHNuT7IEZIxv4Gg13_nXx7H2hYtD3U514I3_F2gRzaR-WCR_mq4sHmn7fqTo_ILR6NxLPmdm5lKxEnovNSCTtn-kPSMW4VOkb6iNE-O_2y-u7eREji1els5sKa7T7sMScwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل: هر موقع میرفتم خونه و می‌دیدم کفشای لِه و درب و داغون پشت دره، می‌فهمیدم مجتبی خامنه‌ای اومده :))
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72837" target="_blank">📅 18:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72836">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72836" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72835">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shbHXp5Cxw4ei2HASAxENyv_JWqQX9X23xU8nEjGLqLxxtTP3PJ3XMN1cRXOdeLqZR_TX9y7elGihZEm7OM8lUtyq94ewTxI-H-aUDXRh-4g_MjbBxZsFYfqpSu-crkH7ZnWa3JHAdT5E1l_egUfIjh8YV9kOz3zcDjtkxPrejw3BELus8u8-pw4Ah2UZfAA49HJacelgBRY5POyYZ31fa3oizmiLclWpPzoluliQqonUFJfBSc8hRsMzc77tJ8F8g9iPzrzDwExLhInyx4n_72RBHc7Cj_IXHb4SvgyBhhSiB4jtXCI4bND7erxqEKiIyRZzQZmVyWY6bYLv67dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72835" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72834">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مارکو روبیو درباره مورد مشکوک طاعون در روسیه:
«فکر می‌کنم روسیه باید اطلاعات بیشتری رو در اختیار دنیا بذاره. کاری که باید انجام بدن همینه و امیدواریم همین کار رو بکنن.
ما هم داریم موضوع رو خیلی دقیق زیر نظر می‌گیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72834" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72833">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=aamscDhwd7r166cAwdI_A0bsel1gqbH018rmLibAdyLoOVjfQKuSUEzQQU9JAqYu83grZBW3FGaYv1cZKwSJFYU4LqNwfLgOvCdAV542_goLb1RnnKMusK6Vg4VtpqzHetpcl7Qb_z19fD_EN0YuGXmKlem2zYEL4tkNicC3K-_io_IHL-32HotK3Ocl0Zj9Z0je0tGuHo2GtujU7FurdwZh7jmRBExZsqr7iq--1IZRWAXLCVJEANGfvYUUojI_scwK2-HRwjhf1bcd4sdvAc6DVZfFeyCSpYWMvr1fCkw4PVl_Ib6eaxnD6HpOarNb8jwXkYKcqLtoWeiEdNBVZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=aamscDhwd7r166cAwdI_A0bsel1gqbH018rmLibAdyLoOVjfQKuSUEzQQU9JAqYu83grZBW3FGaYv1cZKwSJFYU4LqNwfLgOvCdAV542_goLb1RnnKMusK6Vg4VtpqzHetpcl7Qb_z19fD_EN0YuGXmKlem2zYEL4tkNicC3K-_io_IHL-32HotK3Ocl0Zj9Z0je0tGuHo2GtujU7FurdwZh7jmRBExZsqr7iq--1IZRWAXLCVJEANGfvYUUojI_scwK2-HRwjhf1bcd4sdvAc6DVZfFeyCSpYWMvr1fCkw4PVl_Ib6eaxnD6HpOarNb8jwXkYKcqLtoWeiEdNBVZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی : مردم ایران در دنیای واقعی خیلی خوشحال و شاد هستن ، واکنش ها تو فضای مجازی دروغ هس و حقیقت نداره
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72833" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72832">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=fAE1aXUiLMJ7lb7_7E5BBmct_cRisGst1sHBrA-ImHcj1IUGkdPCkqqx-h4noBaiR00dxghg39BfXLEYSrLnBzWH7HGZoBGFfSgXfaph40NPyx-Cud8_zP8Kf66ygAbyHbQ9SIIw2YzdaUgKBTMRzIMdIoGBfsAUAeQy5tModqLBuwAEO3Hz9wXPfMkXGwltFDzUiF76ArILZ62uqZAURsZTrLx1zxVUSMDHT9zPOGYPyF5fSMYRD33yasnJEf-37CgApXxYQm2w1mbzpjhF9BiIuyxPYxrlC2G6fOETEBd9L4fSVdHDAnJXCzNmI-mwT3CuI9vbR9x1YaKwnqAbnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=fAE1aXUiLMJ7lb7_7E5BBmct_cRisGst1sHBrA-ImHcj1IUGkdPCkqqx-h4noBaiR00dxghg39BfXLEYSrLnBzWH7HGZoBGFfSgXfaph40NPyx-Cud8_zP8Kf66ygAbyHbQ9SIIw2YzdaUgKBTMRzIMdIoGBfsAUAeQy5tModqLBuwAEO3Hz9wXPfMkXGwltFDzUiF76ArILZ62uqZAURsZTrLx1zxVUSMDHT9zPOGYPyF5fSMYRD33yasnJEf-37CgApXxYQm2w1mbzpjhF9BiIuyxPYxrlC2G6fOETEBd9L4fSVdHDAnJXCzNmI-mwT3CuI9vbR9x1YaKwnqAbnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش چشم بازم تحلیل کرد و گفت جنگ در پیشه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72832" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72831">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=gZEphx0wKm5eUfxPRoTRATcgRTbLZZBUDxX5Py6rzbFp83jR3MZSt-1uGgg3AtepOLOnsF4XL5U1NVN-mb1FAO6WVD_UFlEWAhimzXRqDjJadYUwoza3Qef274qvU2imkqFS3Q5jT_cuYEo3yX9bAmQJQ5F-aQMK94-ky7cWoTtsZc-V1hkLyW1DhaA0hO5ln_YFzr-3TZ_v4jQ3SrVrzaAI-HglcWoxRBurjuaiFuRRSSGnH3k-nybMe7tBQHfkQQ7S9nMBzR6lmauIy72Og2aFD32Eka03xpyUbW3Zogv_4xyh9uQtVL3mQcohL5gzUKc4mxRWVNd_-Q0DXGqnEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=gZEphx0wKm5eUfxPRoTRATcgRTbLZZBUDxX5Py6rzbFp83jR3MZSt-1uGgg3AtepOLOnsF4XL5U1NVN-mb1FAO6WVD_UFlEWAhimzXRqDjJadYUwoza3Qef274qvU2imkqFS3Q5jT_cuYEo3yX9bAmQJQ5F-aQMK94-ky7cWoTtsZc-V1hkLyW1DhaA0hO5ln_YFzr-3TZ_v4jQ3SrVrzaAI-HglcWoxRBurjuaiFuRRSSGnH3k-nybMe7tBQHfkQQ7S9nMBzR6lmauIy72Og2aFD32Eka03xpyUbW3Zogv_4xyh9uQtVL3mQcohL5gzUKc4mxRWVNd_-Q0DXGqnEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدنی وزیر دلقک اقتصاد: درمورد قیمت ارز از همتی سوال بپرسید.
خبرنگار: همتی هم گفت از شما سوال بپرسیم.
مدنی دلقک: نه دروغ میگه از خودش بپرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72831" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72830">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=t0lhJ3DdJMv08yPBD8qNiDqxi_23Gze6IYq1lu7g4IqqM9nLNqfiQRMuGjY-kxL8bmE91TuuQeB021fucSBJzX-YXZGhnDaRWPROLQiKVwxX_affWE1bxv4OFjutVXTQS9hqei2kh5j-QhocaXLbER3xukyFAldeNcesKwwvW2MmHGSuN4PKKIldn-ez_kOv1-wABPqiyKgNTndY7aqJIPLly-oskxMVgDCkTMbsywW_OcqpsYEgwtFttzsLDfE6u5vHJW_zYqyDM8L97zCltL1sEaZdYMd2AuQ3hpOGVusp9iD4nX8MVp61xSAoIJX6SKJDW1B9e7cadzJQxs0gQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=t0lhJ3DdJMv08yPBD8qNiDqxi_23Gze6IYq1lu7g4IqqM9nLNqfiQRMuGjY-kxL8bmE91TuuQeB021fucSBJzX-YXZGhnDaRWPROLQiKVwxX_affWE1bxv4OFjutVXTQS9hqei2kh5j-QhocaXLbER3xukyFAldeNcesKwwvW2MmHGSuN4PKKIldn-ez_kOv1-wABPqiyKgNTndY7aqJIPLly-oskxMVgDCkTMbsywW_OcqpsYEgwtFttzsLDfE6u5vHJW_zYqyDM8L97zCltL1sEaZdYMd2AuQ3hpOGVusp9iD4nX8MVp61xSAoIJX6SKJDW1B9e7cadzJQxs0gQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
اسرائیل توی ۱۴ ماه گذشته اسم ۱۴ تا خیابون و بزرگراه توی تهران رو عوض کرده! اونی که عملاً داره اسم خیابون‌های تهران رو تغییر می‌ده، اسرائیله؛ اسرائیل همین‌جوری مقام‌ها و فرمانده‌های سپاه رو می‌زنه، بعد شورای شهر میاد اسم همون‌ها رو می‌ذاره روی خیابون‌ها!
دفعه قبل هم بعد از جنگ ۱۲روزه، اسم چند تا خیابون و بزرگراه رو گذاشتن به اسم حاجی‌زاده، سلامی، باقری، رشید و شادمانی؛ یعنی اسرائیل اینا رو می‌کشه، شورای شهر هم جلسه می‌ذاره که خب حالا اسم کدوم خیابون رو بذاریم به اسمشون!
در واقع اونی که داره اسم خیابونای تهران رو عوض می‌کنه، نتانیاهو و موساد و نیروی هوایی اسرائیله؛ شورای شهر فقط می‌مونه و تابلو رو عوض می‌کنه!
با این حساب، اگه همین روند ادامه پیدا کنه، باید منتظر باشیم هر بار اسرائیل یه مقام دیگه رو هدف قرار می‌ده، تهران هم یه خیابون دیگه به اسمش دربیاره!
یعنی خلاصه تقسیم کار اینه: یکی می‌زنه، یکی تابلو می‌زنه:)
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72830" target="_blank">📅 15:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72829">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KL393hn6QS1HbnfjKMUhA0G_VPaZe7nHSvBiJDhgbthiMTHyaAWmorqalJX6wqwBvjflRPcQdp5QENuOtGH7wOQucVq8W32Q7eIAcYQQqShgDlhDjyoBfUo_ou4T_Bnz7IZ9ahUognHuykYYLpnPTTBIzqnJRdmru2cDJlqtqJ1CCSAu-5WWU78mVMAxwDzNSSsFf4dic4AXehzbYQ1nRB7fevrn7gaIPUMqwF6aVM0ROX1TXfCAzbJ5ATrlkaU4fraTuJvljEBW7VI6Hhl41VhZHZ6wJsKoxSS4-hMFmUKUIKsOYqa8ysgPI5scDnGpX4MUrj3LacgNI5ccZm2aWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه از تاثیر سهمیه! توی کنکور امسال یه نفر رتبه‌اش ۸۱ هزار شده بوده،
که با سهمیه ۲۵ درصد، رتبه‌اش ۲۸۳ شده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72829" target="_blank">📅 15:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72828">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=ekjSgKDrDLyn03Gr9ZQXefnP2BvAPRQCdDdREMUoHJPEhk4Erh89Eol3OMTAF3JzkuiHtue1glN-ztzMXJYRPh7vf23njDMdrjlmckCsdJYsjCfozETdcyjOQZdUjyDP2SeSN7WrHB0lg6nVQwEW4J8mhRdAjJzWCjWbzYigBFHiGiPuLstVCt2cfKrX7uYkRlOWsVQUZNmCdbNW2EovsQR0_he5OWk7zPO_p8itkz69EBJtzWSphRSFSkRzQYQ61O6qlPPk049QQwrFbA-POVbXTp85Gu5hWJcM-j1Q_fD5DPlVum0jMVBnrcxLK2B8c3HOalp9GQ3ku3iQ0fv0AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=ekjSgKDrDLyn03Gr9ZQXefnP2BvAPRQCdDdREMUoHJPEhk4Erh89Eol3OMTAF3JzkuiHtue1glN-ztzMXJYRPh7vf23njDMdrjlmckCsdJYsjCfozETdcyjOQZdUjyDP2SeSN7WrHB0lg6nVQwEW4J8mhRdAjJzWCjWbzYigBFHiGiPuLstVCt2cfKrX7uYkRlOWsVQUZNmCdbNW2EovsQR0_he5OWk7zPO_p8itkz69EBJtzWSphRSFSkRzQYQ61O6qlPPk049QQwrFbA-POVbXTp85Gu5hWJcM-j1Q_fD5DPlVum0jMVBnrcxLK2B8c3HOalp9GQ3ku3iQ0fv0AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشور چین واقعا عجیبه، روی یه شهرک یه شهرک دیگه هم ساخته شده. شبیه فیلم inception شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72828" target="_blank">📅 14:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pkx5WzJKSJz0vjYc-qarBhxdKLHhlyolOzYzO6z_3y2P2zT-VyUWRikOKRYkhulrvq_IBHALEjb_HVSbwis3IRYw1FX-imXkWJCT9f6-00E_Twa0Ye0vThszfFKYc9RPjIKqfvV9Eygm1DJpE6OpybQCeaCoUivDDdOXwYVX1CE3cTz6Bj8hnL-i5GNvv-Cmoc6Br8cgWzEtPmIPQJZVyiealJTREAKeJcZc60wTN9l8ktk2-MJ753-v8L2dlDdwW1x32irXyZtkTADbpTGwV0EryFTM2lhI8JfLpb_prPqc4QkLaQQtgZdNF7BySt-0TPWtPtlLOaW35oDvFcE6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOAcZdAzUciwkpoe2N5YAjo7XQTZErn_5QS0WtvxXn0fTSrhkcjpSfQHrzYx6hgFEj5t-RPMu5rtuqoQIhmEG7dXttXjB5spQ0lviTK0SWB0oGoCpt1VaSKPbUS4H9qB4H28BXuDThSj8nsx-bW-WNDeqBLafQGLu5dmN0fd_7Sj5Ohpx_-Mlxv-f6wfiFrH4LVKDAh8sHU6gbsZvyt1CHzPP5pc8HJKoXZisuaRoSaQCODDm_Z1fgUfgxzc0GgGW-1xQFtfXbzIagimSSq1khGavrluKRTqy1d7qYFiSviFNsE8Zcuwb38pjsb8SSerzMC4exo2AtSkob3i3JjPOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=UPYhWaCzx5NZMUkUEpKcnPDbfxTHdU7nRvG_nzZ5pU7fQJlWwu29MpWjLDdHZjxhZFzJKyeNUj9S1Xllw7CyLljpB-2aFnLUqfigok_2m5xtXB6qlangWPTFbpEIGCJhnJrt17LlSNVWeTT-fYX-5_k-fRBtjZBg7hMZQkQyKJzJczo3IaRaJd7k4nJuPiOcMyutzUoXLGFC5eb1PVtYBdBtsMUwPGaa9V6qWVqBUlBiQRC4nXizrPuUfZeQp43_XXtWSDdnLcz7GfQrEBWxIbUCleyc9-p5KHP_Bj6t05VCZDhXpZZEbe4pNfQlZsaNxB-F8fYnyjCbt2JwrGj8wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=UPYhWaCzx5NZMUkUEpKcnPDbfxTHdU7nRvG_nzZ5pU7fQJlWwu29MpWjLDdHZjxhZFzJKyeNUj9S1Xllw7CyLljpB-2aFnLUqfigok_2m5xtXB6qlangWPTFbpEIGCJhnJrt17LlSNVWeTT-fYX-5_k-fRBtjZBg7hMZQkQyKJzJczo3IaRaJd7k4nJuPiOcMyutzUoXLGFC5eb1PVtYBdBtsMUwPGaa9V6qWVqBUlBiQRC4nXizrPuUfZeQp43_XXtWSDdnLcz7GfQrEBWxIbUCleyc9-p5KHP_Bj6t05VCZDhXpZZEbe4pNfQlZsaNxB-F8fYnyjCbt2JwrGj8wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یکی از همون ناوهای آمریکاییه(USS Delbert D. Black (DDG 119)) که سپاه تو بیانیه‌ها گفته بود موشک بالستیک خورده و «خسارت قابل‌توجهی» بهش وارد شده. ولی خب، به نظر من برای ناویی که موشک بالستیک خورده و خسارت قابل‌توجه دیده، زیادی سرحال و سالمه!
الانم برای استراحت چند روزه خدمه، وارد پوکت تایلند شده و بعد از تمیزکاری جلبک ها مثل روز اولش می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72825" target="_blank">📅 13:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=OvAhr7R5Y8fIY9dVDOTyyQ5Eq54JaN3bKHC0Nnc-DgNQ5xh1D0mJNQvh7WFQ5DCdWk7riR8_BEb60uVwms40c_qmVnjkg8HfwVdbwqRCywEy7-bJcWjmCRd-CsdeVtD5mR11mHnDqJ6wZbiHW3Jb0iMoS87EK5p6m1l0MEuVzh2TBaoDyjC7EdYk9ndGgfABn72FRy5T3bbYebeOez1ZfQMqr22JlLixkG6k2-NONCEAxX2e4tLzEOjBIw_xT17wFdXLG4vMoMoRnSNMdTr4IO5f36M3drX6YqMifHDzl5sTGPLIjJQzF7uUE3FmbBqMPjrc5pdrUfRHnl8spCEhXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=OvAhr7R5Y8fIY9dVDOTyyQ5Eq54JaN3bKHC0Nnc-DgNQ5xh1D0mJNQvh7WFQ5DCdWk7riR8_BEb60uVwms40c_qmVnjkg8HfwVdbwqRCywEy7-bJcWjmCRd-CsdeVtD5mR11mHnDqJ6wZbiHW3Jb0iMoS87EK5p6m1l0MEuVzh2TBaoDyjC7EdYk9ndGgfABn72FRy5T3bbYebeOez1ZfQMqr22JlLixkG6k2-NONCEAxX2e4tLzEOjBIw_xT17wFdXLG4vMoMoRnSNMdTr4IO5f36M3drX6YqMifHDzl5sTGPLIjJQzF7uUE3FmbBqMPjrc5pdrUfRHnl8spCEhXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم طرفدار حکومت:به پسر نوجوانم گفتم اصلاً نگران نباش!
خواستی سیگار بکشی، بگو خودم برات می‌خرم؛
خواستی قلیون امتحان کنی، با بابات می‌بریمت سفره‌خونه؛
فیلم مثبت۱۸(پورن) هم خواستی ببینی، بیا با هم ببینیم! این‌طوری دیگه خیالم راحته که همه‌چی کاملاً تحت کنترله!»
@News_Hut
😐</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72824" target="_blank">📅 12:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=fc1ev3fgcI-e8CQwAF6XswIK9bD_UQ-Qz8timcjXDdkwPzD50Doiu8-dCeubxmWuvP301Lr2q2m2vPj9d8_pK6kY230m1RDvyQ8GsajvyyAW8QnhXxSWlK15UlF4tTEAQNNAsN-cKohjbDZhk7ipfi6x_Cu3LqF4BpyVIFRu1Df0vZBtM468CbN4mvtI3_154m72KghXCIuePEiLIDOgqEYtLAHCz83CfmAPrxzSyB7IUBaq7RKs1SeYd4rQBxINjOI4QKKp2-F8fXjAdyAz9wrbzg8KX80ZIR81B5F2AC1fL-no1Ogm_Rcp6CXw-y7DpDErqXY4s6lEHirj8S04QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=fc1ev3fgcI-e8CQwAF6XswIK9bD_UQ-Qz8timcjXDdkwPzD50Doiu8-dCeubxmWuvP301Lr2q2m2vPj9d8_pK6kY230m1RDvyQ8GsajvyyAW8QnhXxSWlK15UlF4tTEAQNNAsN-cKohjbDZhk7ipfi6x_Cu3LqF4BpyVIFRu1Df0vZBtM468CbN4mvtI3_154m72KghXCIuePEiLIDOgqEYtLAHCz83CfmAPrxzSyB7IUBaq7RKs1SeYd4rQBxINjOI4QKKp2-F8fXjAdyAz9wrbzg8KX80ZIR81B5F2AC1fL-no1Ogm_Rcp6CXw-y7DpDErqXY4s6lEHirj8S04QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سال 2023 یه میم به نام Opium Bird خیلی وایرال شد که یه موجود بزرگ و پرنده‌مانند تو کوه‌های برفی رو نشون می‌داد و سازنده‌اش گفته بود که سال 2027 (۲ ماه و ۲۶ روز دیگه) می‌فهمید یعنی چی؛
حالا شباهت Opium Bird و طاعون
👺
و همچنین لوکیشن برفی اون میم و آب و هوای روسیه، دوباره همه رو داره به این فکر فرو می‌بره که نکنه داریم وارد یه سیزن جدید می‌شیم...
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72823" target="_blank">📅 11:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72822">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=lH0WYLhnvzWk-gRy4Ii-HuX9ZenrnjDou6REaa8qXEoCr_e0A2NcC-rkeVS9Y2cyjpCqosu_b_CcE1lsesG5kfJpZGV4H63Gi4rDlawoUtSbv877Bb7dDwOp1aQdt3aKiTjGKgZmbMzytIvXf4LwfwavaSYBtf87atl9Skt-WblS3CHpKNHHTd9v0KcQI19q5gmN0OXhjKVEJwfw774xNnH1p_VuWMsCKA6RcaKs6w2lh_4NRfluXG1L17CWwtkqxsYzmRN94BRYRb7bZPSqPgSGj9EL8-NzJuIzugR_U0snuLq_dqOnfuvih6K3rRoCLovRwqBDOLJ-ctfhgwKmnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=lH0WYLhnvzWk-gRy4Ii-HuX9ZenrnjDou6REaa8qXEoCr_e0A2NcC-rkeVS9Y2cyjpCqosu_b_CcE1lsesG5kfJpZGV4H63Gi4rDlawoUtSbv877Bb7dDwOp1aQdt3aKiTjGKgZmbMzytIvXf4LwfwavaSYBtf87atl9Skt-WblS3CHpKNHHTd9v0KcQI19q5gmN0OXhjKVEJwfw774xNnH1p_VuWMsCKA6RcaKs6w2lh_4NRfluXG1L17CWwtkqxsYzmRN94BRYRb7bZPSqPgSGj9EL8-NzJuIzugR_U0snuLq_dqOnfuvih6K3rRoCLovRwqBDOLJ-ctfhgwKmnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«همه دارن می‌گن من GOAT ـم، یعنی بهترینِ تاریخ.
من می‌گم: «پس واشنگتن و لینکلن چی؟» اونا هم می‌گن: «شما از اونا هم بهتری، آقا!»»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72822" target="_blank">📅 11:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=cqIEOR2Y48ecJOCEBL79_MqGCTdilsTHAyNwaFj_J51UdQRuxWU4GYCgLoU1pCYddAIcNtyBEXjAgYI6VTpB24r3FScIsEo-qb9sEBzkKgQUmT4MipF9qkZhb3BLWCA50jwWR4vMDNWuQLS5P457SIuzatDIZeQ1qRlw9KdBhuIvqPtlvComHAC3StFqpxJWSwLH2P7JcdWd1VcnVB1vhiQkWSZlyePOzU2nNs3xLkNuHw7sRT-YkB1NcOvuNRW7LSH2ntXosbz8ht3ljpE0n5tV0gp95D75uyJQKlWcmgMEvZyGn6qHTs0_12lP2CVBatwZRFBIxoX8CvSpsd-rzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=cqIEOR2Y48ecJOCEBL79_MqGCTdilsTHAyNwaFj_J51UdQRuxWU4GYCgLoU1pCYddAIcNtyBEXjAgYI6VTpB24r3FScIsEo-qb9sEBzkKgQUmT4MipF9qkZhb3BLWCA50jwWR4vMDNWuQLS5P457SIuzatDIZeQ1qRlw9KdBhuIvqPtlvComHAC3StFqpxJWSwLH2P7JcdWd1VcnVB1vhiQkWSZlyePOzU2nNs3xLkNuHw7sRT-YkB1NcOvuNRW7LSH2ntXosbz8ht3ljpE0n5tV0gp95D75uyJQKlWcmgMEvZyGn6qHTs0_12lP2CVBatwZRFBIxoX8CvSpsd-rzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«این جنگ خیلی زود تموم می‌شه و قیمت‌ها هم قراره حسابی بیاد پایین. شاید حتی خودتون بگید: «خواهش می‌کنم آقا، این‌قدر سریع ارزون نشه!»
😂
خودتون ببینید تو یه مدت کوتاه قراره چه اتفاقی بیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72821" target="_blank">📅 11:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=ro-30RsLBNDOsoxnAfvwT1naYQV041Io4VQ3sBu3FgVGT0pvNUbXkbSNcaOEE9aWsY9oxGB8PIlRihru2KW7A0lN35nnKGFuyPBeC0b4XOBxK97NHhW7a9dliprW78x4YPWtHfYWLITHmHo1nrIk6t-lfsy7303aBwz5IUPxcU8zF9juX8GrCdgczDvV_3_kbNBXa2vW9pwV7FemvL1-_pLEBcFxXcXXPKOwMRTtWpEIlz-zfV87Om590x7gKgm4veEtJKNkEzHL0IhYKF9l7ncIS58xiDawTKcYAIu3Z8-W_VH9sEtborrZIjgr3YCqC73lDPEzWno2fVSRxcJvDgQ-uekcnV2s-X_nc1J1ktEloz95ABwbjaTJJb6waPzGk7cC_otIHM594E-kgXUK8aw2RqUlIMo-3txPrR3IpysmfgC4QqGgvCwcLogsldpcmLfeTOD1Aoaz-XeR6LU1_F39oa8urSDvHxxhIMOn4sf4uy_sk4S54BXn65QVKK5A4QJICebYWQAf0H4A01ZqLdoHvu2PhSKGgX5D7q9y7H6xkbao0aKqxKZEU1G68ODFA0rinKBdqy8UqmsTtBPtdHlkWj_YZ32tlkf9eHQBfNAmwh2mXb0R58wBVuHwU3ErDMEUr-XtS07JPZAsRBvxqRiFxtU0iVMHzR28PPsRBsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=ro-30RsLBNDOsoxnAfvwT1naYQV041Io4VQ3sBu3FgVGT0pvNUbXkbSNcaOEE9aWsY9oxGB8PIlRihru2KW7A0lN35nnKGFuyPBeC0b4XOBxK97NHhW7a9dliprW78x4YPWtHfYWLITHmHo1nrIk6t-lfsy7303aBwz5IUPxcU8zF9juX8GrCdgczDvV_3_kbNBXa2vW9pwV7FemvL1-_pLEBcFxXcXXPKOwMRTtWpEIlz-zfV87Om590x7gKgm4veEtJKNkEzHL0IhYKF9l7ncIS58xiDawTKcYAIu3Z8-W_VH9sEtborrZIjgr3YCqC73lDPEzWno2fVSRxcJvDgQ-uekcnV2s-X_nc1J1ktEloz95ABwbjaTJJb6waPzGk7cC_otIHM594E-kgXUK8aw2RqUlIMo-3txPrR3IpysmfgC4QqGgvCwcLogsldpcmLfeTOD1Aoaz-XeR6LU1_F39oa8urSDvHxxhIMOn4sf4uy_sk4S54BXn65QVKK5A4QJICebYWQAf0H4A01ZqLdoHvu2PhSKGgX5D7q9y7H6xkbao0aKqxKZEU1G68ODFA0rinKBdqy8UqmsTtBPtdHlkWj_YZ32tlkf9eHQBfNAmwh2mXb0R58wBVuHwU3ErDMEUr-XtS07JPZAsRBvxqRiFxtU0iVMHzR28PPsRBsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«یادتون باشه، این جنگ یه چیز مصنوعیه؛ یه مقدار هزینه‌ها بالا رفته، ولی خب برای اینکه دنیا امن بمونه، قیمت زیادی نیست.
اگه اونا بتونن یه شهر رو بزنن، بذار لس‌آنجلس یا سن‌دیگو رو بزنن؛ این در برابر حفظ امنیت دنیا، قیمت خیلی کوچیکیه.
در واقع، این ماجرا تقریباً دیگه تموم شده.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72820" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=SjJdEueXSTbXAodxlguJuK8fXAOYpVJntHXsOT-KLn0pDQcIK2mStp6iVj3jOn0gfKpdPn_08fUKCB3zOrjj82L_x-xp9YEt4DzTH1kFOodqiPT5yVCuRk9Zc_VBTCwDpw-iMo1ulruErggfJTotJx3YxMl2UY9kwRE5RPbLgtp5JXurvhADrff2Cji2PLfxs5EHp_Nhl0OA737sFUQ_4GAfkdrxsEsMsEU3QqllVMmxvpDNIpsgiJIsI4PJwYJ9ivcN7wnXPlKLjGTB-t76dy1uIHekZvcG7ElhtQxWInZ45-eheBE0gCCcJhtde26gHc9B-rCFVsKo1ADOUWWcTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=SjJdEueXSTbXAodxlguJuK8fXAOYpVJntHXsOT-KLn0pDQcIK2mStp6iVj3jOn0gfKpdPn_08fUKCB3zOrjj82L_x-xp9YEt4DzTH1kFOodqiPT5yVCuRk9Zc_VBTCwDpw-iMo1ulruErggfJTotJx3YxMl2UY9kwRE5RPbLgtp5JXurvhADrff2Cji2PLfxs5EHp_Nhl0OA737sFUQ_4GAfkdrxsEsMsEU3QqllVMmxvpDNIpsgiJIsI4PJwYJ9ivcN7wnXPlKLjGTB-t76dy1uIHekZvcG7ElhtQxWInZ45-eheBE0gCCcJhtde26gHc9B-rCFVsKo1ADOUWWcTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جنگی که علیه ایران راه انداختیم برای «
نجات دنیا
»ست!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72819" target="_blank">📅 11:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225b755540.mp4?token=MjC6E44AMfyGYPS0TKzw4fQqO-qCfXQbnjqHrC-f-IViszR9veirmnTzMP8xzLMx7daV8l43rjOjyQ0r60NvAM4M52EvegQisTfcH3J8Gr_RSG9ntYP6kYllCsszISgMNVd2QpKkrsJFmwx3y5aNBIAeZPpYrfghr9gzaDwxbmOeg8DbuQ3Wfz64581Vq4CNm0yxdKF6OtPfyuQvwb0OSdKgetyF8fAVrfBlJF8pkl_R6z1eEyBMEj-aqaIw1tzjbIeIepGPTckWCKVtdT9H2S1odZqvKjdJOzpQcdEzuzXTKXUBE-1MCLaQVEhM9IyQMGXzwOJRIs3v3JruOtca44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225b755540.mp4?token=MjC6E44AMfyGYPS0TKzw4fQqO-qCfXQbnjqHrC-f-IViszR9veirmnTzMP8xzLMx7daV8l43rjOjyQ0r60NvAM4M52EvegQisTfcH3J8Gr_RSG9ntYP6kYllCsszISgMNVd2QpKkrsJFmwx3y5aNBIAeZPpYrfghr9gzaDwxbmOeg8DbuQ3Wfz64581Vq4CNm0yxdKF6OtPfyuQvwb0OSdKgetyF8fAVrfBlJF8pkl_R6z1eEyBMEj-aqaIw1tzjbIeIepGPTckWCKVtdT9H2S1odZqvKjdJOzpQcdEzuzXTKXUBE-1MCLaQVEhM9IyQMGXzwOJRIs3v3JruOtca44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«راستی، داریم حسابی ایران رو می‌کوبیم، اینو که می‌دونید دیگه؟!
در هر صورت، این داستان خیلی زود جمع می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72818" target="_blank">📅 11:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72817" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72817" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI-W-26YJJiU6pLXKGar5HW1nwNkueUjTcYS9o4u0C_lUEFxLg5VlZDjOAIr5g80ZJ9f0pV00zxldmC6BWBow8X-0WA2m22BNDLtq7zd6I2cEzLGQNkM_5tDuqd6Q3JtHFOO8OHlhAwzwhaJobxWzr1Z_F1IxMFtMW9NS0_idry4FZLMRJtTpMIqv4BeusQeaA_a8iHU9xe6y1HopLSljl2uqh6gy41JFrEdOgvYBQbme_Z88vv4amkhR6Ktyvyw2VzPTNuGeAkSciWMGd3EPmw37J3hgYisjL6Hu1lcRQ4sWlKecu9EnTpcEs7USgzbZEbEH4XB6-ih800jxLvuYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیا
🆚
کرواسی
چک
🆚
انگلیس
اسلوونی
🆚
اسکاتلند
مقدونیه شمالی
🆚
سوئیس
ازبکستان
🆚
کره‌ جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72816" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72815">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=JXIc_eXXOjFkAiRteWjtYjlq0EmCg1SKphEdi83qJo2a2L3UOPJI4syj7AcRARo-sHrJB3i6TJGdLb1J1WDiN5Pyx0iOwbW1o7ijVXErpJ94dNSdgpFOPOFsUVWMY_X_qKovuN0ldK_7K2cFiIxh403qLeK_onRD4SccC08ncyV0Qn1mjPo0UFfhKAX4QLrk1uOxSQSji4qjJLmEiCGBwFOul2Tl9HaX2AHslnszFwnJJZQRwXcmxyWStZbmQ4AGh80HoA7McIQae_YrSHNDPfKq7YEveJBwN7UmbsCLzc9bQcs9wzyQX74jFHDhN33e_yDbbT3-FMIWhrDkzde7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=JXIc_eXXOjFkAiRteWjtYjlq0EmCg1SKphEdi83qJo2a2L3UOPJI4syj7AcRARo-sHrJB3i6TJGdLb1J1WDiN5Pyx0iOwbW1o7ijVXErpJ94dNSdgpFOPOFsUVWMY_X_qKovuN0ldK_7K2cFiIxh403qLeK_onRD4SccC08ncyV0Qn1mjPo0UFfhKAX4QLrk1uOxSQSji4qjJLmEiCGBwFOul2Tl9HaX2AHslnszFwnJJZQRwXcmxyWStZbmQ4AGh80HoA7McIQae_YrSHNDPfKq7YEveJBwN7UmbsCLzc9bQcs9wzyQX74jFHDhN33e_yDbbT3-FMIWhrDkzde7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش چشم: اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72815" target="_blank">📅 11:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72814">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=GpBBB6lKkFscfN2fS9_IRBI3akq2qbypPSR04mypONxdJQcI1pj2m-bdzZlfKs5eWv1SBHKfvGelLLjwj73ufwys5cp_2KVnW56BfWfViPP8x4sqilIIvrpZMUYhD2vOUfsetXG0AUhsEyjlwmvpyYzLK6rZuLZ3tsJk9eMlGZ8yMjgm-FNRxPwEpPMfjM3U6L1rcCzzXwWrJO02QjOzguUKnPbs8r02RR6VDEcl-uGo_UwMDnyu_rXOpuD4NVwXEQvZr1jCLLKgnAp_vWkJpT3e8F3rdMNvd1I8PKESaPjvM92nWhvUJMyT69AU_Y5HDlpkUdBYAOhRfKRAA-wEOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=GpBBB6lKkFscfN2fS9_IRBI3akq2qbypPSR04mypONxdJQcI1pj2m-bdzZlfKs5eWv1SBHKfvGelLLjwj73ufwys5cp_2KVnW56BfWfViPP8x4sqilIIvrpZMUYhD2vOUfsetXG0AUhsEyjlwmvpyYzLK6rZuLZ3tsJk9eMlGZ8yMjgm-FNRxPwEpPMfjM3U6L1rcCzzXwWrJO02QjOzguUKnPbs8r02RR6VDEcl-uGo_UwMDnyu_rXOpuD4NVwXEQvZr1jCLLKgnAp_vWkJpT3e8F3rdMNvd1I8PKESaPjvM92nWhvUJMyT69AU_Y5HDlpkUdBYAOhRfKRAA-wEOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز ترسناک‌تر میشه، یه پدر برای اینکه پسر 3 ساله‌اش رو تنبیه کنه، یه بسته مداد رنگی 24 تایی رو فرو کرده توی باسنش!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72814" target="_blank">📅 10:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72813">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=DoANQgeZl-KB-sBE0bM-tass19dc8odO5EIFXqguU4pMSN7Y7K93MJzXCOHjIFKGirwxk8DuaI4deFUMJDA_SkpPhlUk2MUznL61sE1PSODOzNnZALLpyivgO4YItT_h-K2YtoChNxQ6HtGvRxsaYa3Ll8WzNeckVLcUGBnJ5WUPJw7RjOtcF73Se8gb0OtZZeaM6zzP-bc8ER1UVFxNdg_3kfTDC_ulaeZd5PFkDWRx3sM62U_hezVJLXV4McvoL55PpITQJHlm_N5pRS6bGZ2hqWa42yf5DJ3brcg7MNj96_XzweNxoS1e66XMdEVx7KZzpKnFo7SAbbpt5VTP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=DoANQgeZl-KB-sBE0bM-tass19dc8odO5EIFXqguU4pMSN7Y7K93MJzXCOHjIFKGirwxk8DuaI4deFUMJDA_SkpPhlUk2MUznL61sE1PSODOzNnZALLpyivgO4YItT_h-K2YtoChNxQ6HtGvRxsaYa3Ll8WzNeckVLcUGBnJ5WUPJw7RjOtcF73Se8gb0OtZZeaM6zzP-bc8ER1UVFxNdg_3kfTDC_ulaeZd5PFkDWRx3sM62U_hezVJLXV4McvoL55PpITQJHlm_N5pRS6bGZ2hqWa42yf5DJ3brcg7MNj96_XzweNxoS1e66XMdEVx7KZzpKnFo7SAbbpt5VTP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا از لوکس ترین مدارس بالا شهر تهران که شهریه شون یک میلیارد تومنه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72813" target="_blank">📅 10:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72812">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOHgV9kw1dVJbNDBK7royF93saZABBLnnL9ddvKedYZVJnq77saJ0F6-C3mlvLfMdgaU5aleyLQsiBz-0aGAb5LXFMEpWs_QeQWvF-upzO4_xHby6vdHJhG-e8oK5uJIrot2TpRU7yawbxWjqARg4QGGR3V3Qc28tg7116HW5Qwgmmg6EtKu7GcGIPlWWWA1EXObl2F5oQuHUaHTIlx5KcwZkSHZIY_GdmXPlYR1QU0xccpnT7ObFsGDaiPzQQ8w18ciJVEBp-IhykuW7hHUv-kXxTVu8gHyaSxtUOcsWoUIX_QsPm579-p7dSYWCTAHd5zxIYrnZt56M7-WvT0rFmwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOHgV9kw1dVJbNDBK7royF93saZABBLnnL9ddvKedYZVJnq77saJ0F6-C3mlvLfMdgaU5aleyLQsiBz-0aGAb5LXFMEpWs_QeQWvF-upzO4_xHby6vdHJhG-e8oK5uJIrot2TpRU7yawbxWjqARg4QGGR3V3Qc28tg7116HW5Qwgmmg6EtKu7GcGIPlWWWA1EXObl2F5oQuHUaHTIlx5KcwZkSHZIY_GdmXPlYR1QU0xccpnT7ObFsGDaiPzQQ8w18ciJVEBp-IhykuW7hHUv-kXxTVu8gHyaSxtUOcsWoUIX_QsPm579-p7dSYWCTAHd5zxIYrnZt56M7-WvT0rFmwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: خبر داری دلار شده ۲۷٠ تومن؟
یه خانم تو تجمعات: اره ولی ما بخاطر وطنمون اومدیم، اگه ما نبودیم دلار حتی گرون ترم میشد
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72812" target="_blank">📅 09:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72811">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=quN5aUXujbDc4mA80EqVBq8VlWSCKLfeeaireqcWtv4bW7oI_YQQzICd0vpyiveLQnvCBnE7zp0SzEapwQrIOBCrRebxBJ3-Yn2RCMqHA2RvjddcCq_oGm-lIrRq3yE715BSL85sdzcaOSKlYVJJsoh0tu9IZmZn9ShPhNpohye9X5l2LDeb3V9Bir4aRFr0JBjJedPCKVCogXs7Am6wuwFJjcjDuvCu9AH_NYi8b-yPk_FEPgOQ2gIFAAWh_cb7Hx9Lb9KgbL54G7m5ey-V2bgSi09rQ2W92_YC3KWiW63G7N9kJvQWRQwgvXGdoh1jh-jKBT_cdgx9K9u48P35DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=quN5aUXujbDc4mA80EqVBq8VlWSCKLfeeaireqcWtv4bW7oI_YQQzICd0vpyiveLQnvCBnE7zp0SzEapwQrIOBCrRebxBJ3-Yn2RCMqHA2RvjddcCq_oGm-lIrRq3yE715BSL85sdzcaOSKlYVJJsoh0tu9IZmZn9ShPhNpohye9X5l2LDeb3V9Bir4aRFr0JBjJedPCKVCogXs7Am6wuwFJjcjDuvCu9AH_NYi8b-yPk_FEPgOQ2gIFAAWh_cb7Hx9Lb9KgbL54G7m5ey-V2bgSi09rQ2W92_YC3KWiW63G7N9kJvQWRQwgvXGdoh1jh-jKBT_cdgx9K9u48P35DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آجرلو عضو تیم مذاکره‌کننده:
بابا بالاخره یه جایی باید قبول کنیم یه‌سری از این تحلیل‌ها اشتباه از آب دراومده!
هرکی نظر متفاوتی داشت رو «خائن» و «وا داده» خطاب نکنید؛ وقتی می‌گفتید ادامه جنگ این‌طور میشه، اسنپ‌بک هیچ اثر اقتصادی نداره، نفت میره روی ۱۵۰ دلار یا با شکست ترامپ در انتخابات کنگره همه‌چیز تغییر می‌کنه، باید امروز جواب همون تحلیل‌ها رو بدید.
اینکه بگیم «ترامپ انتخابات کنگره رو ببازه، دموکرات‌ها جلوشو می‌گیرن» هم خیلی ساده‌انگارانه‌ست.
بین انتخابات تا شروع کنگره جدید چند ماه فاصله هست و رئیس‌جمهور آمریکا هم قدرت زیادی داره و می‌تونه سیاست‌هاشو دنبال کنه.
خلاصه اینکه تحلیل غلط، تحلیل غلطه؛ فرقی هم نمی‌کنه از طرف چه کسی گفته شده باشه. به‌جای توجیه و فحش دادن به بقیه، بهتره بعضی‌ها یک‌بار هم بابت پیش‌بینی‌های اشتباهشون پاسخگو باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72811" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72810">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72810" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72809">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt_bCDILDXj3Wz7heNESDaWPlHrJxoHXtFJLtDLjRl2eGs-z0ZWOXKCF7Aa_0tGxJopmTaJxs9NlQzpaWCPY475DyeeMxTouSbsELxOZ3Cz5TqMBMpYulsuq1ESHqYVORmsgDoAOzP_mWcfLn0evpyMtNvA4d0LrY47JvuYdVV5BOQXTacvGWAD9EoJrt1_jtrIf7x22kE63UQhciKm7fqVC8xIwuACsWWS5Jt1enCejwmsHOqVxh9kPPzgXqCKFfPZjuuhSnZewhh9mZJxFLLP8iRi8ySmWL9k5ZWadLLIl_2pKwZQMCBH7n7yU22PaE4kMAsUsggk_Pcp_J6rD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72809" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72808">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=GurlpGQ2NSvIHh40Wo28NySr-qAcVavKgE7LdJw9MjcdhPWdDqV8Bcf1DB4mCzH_stiO3v1kmhTF1Eo46cW1CTuAsmUKGaPk-BRjq1j2kmz-cUfRL1Wo8_L9VC7aEif7FDju4PSKf1tJ4Spj_Hw54o2nAqp4bVuUPVn8HvL1rqrKNomva6ITDosWWURv4GFy5zbjyiyfA4UvpT9AHq3jml3O84us492Fx756KuyVbi5GQ4HerC8MlGBnTQo95PMsXhdCPAspXiJjdMnt3tMrAjGwsjNW8ZLKMdG_KX3bTcRK8fdEUKbP113EmvzSg1tyY_LTlfj85dqANf2RnajJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=GurlpGQ2NSvIHh40Wo28NySr-qAcVavKgE7LdJw9MjcdhPWdDqV8Bcf1DB4mCzH_stiO3v1kmhTF1Eo46cW1CTuAsmUKGaPk-BRjq1j2kmz-cUfRL1Wo8_L9VC7aEif7FDju4PSKf1tJ4Spj_Hw54o2nAqp4bVuUPVn8HvL1rqrKNomva6ITDosWWURv4GFy5zbjyiyfA4UvpT9AHq3jml3O84us492Fx756KuyVbi5GQ4HerC8MlGBnTQo95PMsXhdCPAspXiJjdMnt3tMrAjGwsjNW8ZLKMdG_KX3bTcRK8fdEUKbP113EmvzSg1tyY_LTlfj85dqANf2RnajJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئوها از شهر طاعون زده شلخوف در روسیه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72808" target="_blank">📅 01:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72807">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=Zgi7t3N3X6F7GgJ0ZSiPDhDINskPkFzcfPoAzF73V7aKbw_K2BSjbXneky5ubDDLKlcbSOdwjbLk5BB1sZXBqjIzbMNbO57lMsDfODO9lWbXoJGQnzovS7h5WIumkM2F-RUienGQr-bSs_74UqESpz-290E7jgmLSA7Jj7gAimgKUTEczrWmpSinraEmB_dOIDg1T-QuZcwAMv7q901O9d_EsDFRKGlNuQLoJhE1k-2FHKotbA1P0XxngfW_udytp_ZHrB7sluAgb5mLe7Z9XN_JlF7UO-0lH-S8gY5-IzxF2qCdKqBOa-scQ35qfEJj52MSPzJjT52YgLyOKsJEgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=Zgi7t3N3X6F7GgJ0ZSiPDhDINskPkFzcfPoAzF73V7aKbw_K2BSjbXneky5ubDDLKlcbSOdwjbLk5BB1sZXBqjIzbMNbO57lMsDfODO9lWbXoJGQnzovS7h5WIumkM2F-RUienGQr-bSs_74UqESpz-290E7jgmLSA7Jj7gAimgKUTEczrWmpSinraEmB_dOIDg1T-QuZcwAMv7q901O9d_EsDFRKGlNuQLoJhE1k-2FHKotbA1P0XxngfW_udytp_ZHrB7sluAgb5mLe7Z9XN_JlF7UO-0lH-S8gY5-IzxF2qCdKqBOa-scQ35qfEJj52MSPzJjT52YgLyOKsJEgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پشم ریزونی که ارتش یمن منتشر کرده که دارن با ماشین، حوثی‌هایی رو که در کنار ساحل گرفتار شدن و در حال مقاومتن رو زیر میگیرن و له میکنن:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72807" target="_blank">📅 01:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72806">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e493def7.mp4?token=k3eKcf_Ek8yfprHLU6l0eG3vkxHp9vVzzq8A55RWr2lOmnak5lOa3d5vmLpUb3tjp7KlXYTqLvAqb4ZEjNu1xEvvLo9ejE4Dd23UEpKodyotPOfDTFZRueCtxt-VImPttvapE00d5f0ZPsPip_Def55xYEMnmUSpsGvyMX3_T8mAuniq6w7MQbQjLb7JuP3EC6G-Y-PFbgMoOwKOw3O-MxH10_541YZm4yQAZ8en43tpmt7cob2QxtbnTiR5QDRsDUjMJYsTXNCwRbtUGc68nUBjsnlbGuG3FJ7GKVOvS2n-pA0OGz6Sr2BjlLVA5WTnNXT6QdKiEadnYFZdGZKb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e493def7.mp4?token=k3eKcf_Ek8yfprHLU6l0eG3vkxHp9vVzzq8A55RWr2lOmnak5lOa3d5vmLpUb3tjp7KlXYTqLvAqb4ZEjNu1xEvvLo9ejE4Dd23UEpKodyotPOfDTFZRueCtxt-VImPttvapE00d5f0ZPsPip_Def55xYEMnmUSpsGvyMX3_T8mAuniq6w7MQbQjLb7JuP3EC6G-Y-PFbgMoOwKOw3O-MxH10_541YZm4yQAZ8en43tpmt7cob2QxtbnTiR5QDRsDUjMJYsTXNCwRbtUGc68nUBjsnlbGuG3FJ7GKVOvS2n-pA0OGz6Sr2BjlLVA5WTnNXT6QdKiEadnYFZdGZKb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان سخنرانی حسین رحیمی، رییس پلیس امنیت اقتصادی، درباره افزایش قیمت دلار، برق محل برگزاری سخنرانی قطع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72806" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72805">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqbnIFevzSy9Sh-K0KHMiPQ-jEwrYKrahU4f9NFZm9R7gvyoQ7zVx0rnWxsw7LT6Y5_ySlENDVFrPYwDkC-UMgyNQodOTwpesPz6TGvahuTI7PvEtEd9L2BEOmd2W7OjHZpkK6etDucD-EsXmL7u8dbAXtsenWjUhWHBnVVD9VQgyjtJdomhk1o2jGgVoXRiQEXqOnMeeg7nymdu4lLupvsWKxHhvi78QvU2BblKEnYSs17edHurGn0eC1LhuzXMK54cLp1LpSF2zQgdeVyN1_sUGDEEQBMpQ1dMYzmY9sC7Vpwa-rriLU5Rl3sbl-5j0zIwlX_770Uv7CMeN0_gEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت درباره ایران:
«عملیات طرد اقتصادی» نتیجه داده؛ ارزش ریال به پایین‌ترین سطح تاریخی رسیده، ایران ماه گذشته هیچ نفت خامی برای بارگیری روی نفتکش‌ها نداشته و حتی یکی از مقام‌های ارشد امنیتی ایران هم گفته کشور در یکی از سخت‌ترین دوره‌های تاریخش قرار گرفته.
حکومت ایران در حالی مردم خودش را تحت فشار و رنج قرار می‌دهد که منابعش را صرف حمایت از تروریسم می‌کند و عملیات طرد اقتصادی تا زمانی که جمهوری اسلامی از تأمین مالی تروریسم و ساخت سلاح هسته‌ای دست نکشد، متوقف نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72805" target="_blank">📅 00:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72804">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=Gt3_Xv9j1OBCdNFuHmhk_fLC5h1Q8-fbyeHiURn1imUQHh9iGAa7mCLMKbwNvEnawsA1dPYUCT-rlcVJ0tWSkdY6NOnzyTys8BsblbvgaG-Jrcnp-E5xPSE1UUxmnwqU2y27352ZTMSkHXG65v8m6QQVtaGLB68xQ1hLrsgQjpSrBCZ6reeaz-DNPLFk-hMfbXmBFWa6fVv6xWTKT93YlWSRMy9heTVgjXqZ561dm9AbGK15_ixL18eiiM0PrOHTmEVjT7s_8faBEGqFzeUsekJzMyL3CNCVSVE6-rFD-7r8L9yzdeMkG0ucTZTsnGoDH-D2mwFNvjGT2pm0hR0skg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=Gt3_Xv9j1OBCdNFuHmhk_fLC5h1Q8-fbyeHiURn1imUQHh9iGAa7mCLMKbwNvEnawsA1dPYUCT-rlcVJ0tWSkdY6NOnzyTys8BsblbvgaG-Jrcnp-E5xPSE1UUxmnwqU2y27352ZTMSkHXG65v8m6QQVtaGLB68xQ1hLrsgQjpSrBCZ6reeaz-DNPLFk-hMfbXmBFWa6fVv6xWTKT93YlWSRMy9heTVgjXqZ561dm9AbGK15_ixL18eiiM0PrOHTmEVjT7s_8faBEGqFzeUsekJzMyL3CNCVSVE6-rFD-7r8L9yzdeMkG0ucTZTsnGoDH-D2mwFNvjGT2pm0hR0skg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ:من فکر میکنم ایران مسئول حمله به هواپیمای «فلای دبی»است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72804" target="_blank">📅 23:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72803">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:
ما مقادیر بی‌سابقه‌ای نفت از تنگه هرمز خارج می‌کنیم. یکی از مشکلاتی که داریم این است که پالایشگاه‌های روسیه به‌شدت هدف حمله قرار می‌گیرند.
این یک مشکل است، اما اوضاع به‌خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72803" target="_blank">📅 23:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72802">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سؤال: آیا نگران شیوع طاعون در روسیه هستید؟
ترامپ: این بیماری‌ای است که قبلاً قادر به مهار آن بودیم؛ اما به نحوی، آن میکروب‌ها قوی‌تر و هوشمندتر شده‌اند. آن‌ها مثل یک ارتش هستند. ما به روسیه کمک خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72802" target="_blank">📅 23:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72801">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=kWRNXjk5Ph2wJvOgtrI9X43AJtRu0HobAH-OekdL4hrs8av13rsoTTyRBw2I9G_bSWJjIIwj0oDFUlNUKRBPBqYNz2iCxvjA8TWR0gRoyOUyyp59u4BHH1ZzY9LtpdUZ8NVgzGmfVyxIZZBpbFslE86xuHFbJNqG5vnPkF1U025BSArloaiUSeui-0ZCynMXx_Q-1p_3BGi62cKFMejcVMHk_IVYy2qdEBe92AAJGTM7LmVogyV-KxMsDKZ6GS6maY0NMSTjZiz8qQLBJnRxKEKGqtYArnS9xAbTuwET1CiY49D7aTsvRJd8N3w-eCvLkvuFioJ5qiH-TLJvDEj6fV_0ZgH8yEPZsvoxaS5U-qNEgQoZLgU8MsQdf96syiFoUi_St1MPbcq-xGHc-ZH9nn69iHs2ysP3KJQhGwPueeFtQcb5wa49Iy9zDcFBz9_T4of4fldIE6RGsU6l365uMLB-ins7SjWeP1jNTQtB7bnHjEmmPJlc3Vt_AIlvDC3tNacM8t57Wg489TvUmgJrb0JorZj6Ddg1GofExddaPGYfNDP2YBK3u0vfT8cu-DPuqgEXlwGSrlggt7AjOUbT9TeJjnqe88SDxIUYv-wSYWLOiR4bTD_3DA3m92rVQKsJ7_ApumGeG--ULqibY0JakJ7oKnVHFqyW9JaepvrY5Ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=kWRNXjk5Ph2wJvOgtrI9X43AJtRu0HobAH-OekdL4hrs8av13rsoTTyRBw2I9G_bSWJjIIwj0oDFUlNUKRBPBqYNz2iCxvjA8TWR0gRoyOUyyp59u4BHH1ZzY9LtpdUZ8NVgzGmfVyxIZZBpbFslE86xuHFbJNqG5vnPkF1U025BSArloaiUSeui-0ZCynMXx_Q-1p_3BGi62cKFMejcVMHk_IVYy2qdEBe92AAJGTM7LmVogyV-KxMsDKZ6GS6maY0NMSTjZiz8qQLBJnRxKEKGqtYArnS9xAbTuwET1CiY49D7aTsvRJd8N3w-eCvLkvuFioJ5qiH-TLJvDEj6fV_0ZgH8yEPZsvoxaS5U-qNEgQoZLgU8MsQdf96syiFoUi_St1MPbcq-xGHc-ZH9nn69iHs2ysP3KJQhGwPueeFtQcb5wa49Iy9zDcFBz9_T4of4fldIE6RGsU6l365uMLB-ins7SjWeP1jNTQtB7bnHjEmmPJlc3Vt_AIlvDC3tNacM8t57Wg489TvUmgJrb0JorZj6Ddg1GofExddaPGYfNDP2YBK3u0vfT8cu-DPuqgEXlwGSrlggt7AjOUbT9TeJjnqe88SDxIUYv-wSYWLOiR4bTD_3DA3m92rVQKsJ7_ApumGeG--ULqibY0JakJ7oKnVHFqyW9JaepvrY5Ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آن چه تهدیدی بود که باعث شد آن هواپیماها را از بریتانیا خارج کنید؟
ترامپ: احتمال وجود تهدیدی را می‌دادیم؛ خب چرا باید آن‌ها را آنجا نگه می‌داشتم؟ با تهدیدی مواجه بودیم. ما کسانی را که آن تهدید را مطرح کردند، می‌شناسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72801" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72800">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=QDY3bV47xfbyDk96kBQ-KlHXkd-ZVeiliGCEjZiAGhkZUc99_VtnSGmhNCCElYuz6p3UP8iC3pOJH7YiwfjJ78HJWbafzvJR7D1dHvPxb-_fMCDNU1MIsIoCBGOg8BmUbrJqpQlsN-eIPDIEUWP0jAy7rzlUvGlgaML2PIxXSLmbA7wGgYT2oF4UyqK1tq3tEMHNu5AekYS6KiBhZRGfvEHaxxr_8T4D55sL0CYaSLmY3cy8t7pYdkOKPtqg9xL0zPH6esppZtY5-A93OibP5rN7QjZD4f7tBpaIolgxfC9EWEv5Ul6AWKAEUhGv9Orx6Ywstp2wck8INSesJlAiXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=QDY3bV47xfbyDk96kBQ-KlHXkd-ZVeiliGCEjZiAGhkZUc99_VtnSGmhNCCElYuz6p3UP8iC3pOJH7YiwfjJ78HJWbafzvJR7D1dHvPxb-_fMCDNU1MIsIoCBGOg8BmUbrJqpQlsN-eIPDIEUWP0jAy7rzlUvGlgaML2PIxXSLmbA7wGgYT2oF4UyqK1tq3tEMHNu5AekYS6KiBhZRGfvEHaxxr_8T4D55sL0CYaSLmY3cy8t7pYdkOKPtqg9xL0zPH6esppZtY5-A93OibP5rN7QjZD4f7tBpaIolgxfC9EWEv5Ul6AWKAEUhGv9Orx6Ywstp2wck8INSesJlAiXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا فکر می‌کنید این خطر وجود دارد که ایران پهپادهای رزمی وارد بریتانیا کرده باشد؟
ترامپ: نمی‌توانم چنین چیزی به شما بگویم. اگر دست به چنین کاری زده باشند، بهای سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72800" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72799">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=V7reubp2apfz3hVzeQ2bzY4gGEOuVDd4kFoM6on73krrUB2EdnM-l_zGmKqMKAbNg_4hLWA60VUPfwYJOsd60Pxrp24-Um4MfIS0e5dDrgsYgYEySvuTtk3PphpvjDc68s0-Y9rHa7JjA58i3Q0AYCKECiUHgG7KYPFWA0VjWqnYdtGICaV-_wmS2eQ0DxhzTaY-Rc0rEQcsVI8OrDgd-OLiVVnOPhjEQPzEu99JRxIJfYOyy4871NkKJ2_39FpymJPdbxf4cz4jHurBDeV3St_5WMDnq6Nw5ZLyrNwl47S4X3gDG-os5S2t7dX-Vll8Ekh_iaml3YyjB5fYltjZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=V7reubp2apfz3hVzeQ2bzY4gGEOuVDd4kFoM6on73krrUB2EdnM-l_zGmKqMKAbNg_4hLWA60VUPfwYJOsd60Pxrp24-Um4MfIS0e5dDrgsYgYEySvuTtk3PphpvjDc68s0-Y9rHa7JjA58i3Q0AYCKECiUHgG7KYPFWA0VjWqnYdtGICaV-_wmS2eQ0DxhzTaY-Rc0rEQcsVI8OrDgd-OLiVVnOPhjEQPzEu99JRxIJfYOyy4871NkKJ2_39FpymJPdbxf4cz4jHurBDeV3St_5WMDnq6Nw5ZLyrNwl47S4X3gDG-os5S2t7dX-Vll8Ekh_iaml3YyjB5fYltjZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:نظر شما درباره ضدحمله عربستان و یمن علیه حوثی‌ها چیست؟
ترامپ: همه چیز به خوبی پیش خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72799" target="_blank">📅 23:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72798">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=FxJKnMCAYUYKzBb60dOXiHfF19onFKUNMaXNu3PXnfb3Wsv3pBMtiCowhtHksyWC_bKN-xnjeV3u0mr6_gtmKW3dflvuAI6DshyG6RjLQOSf6KRLHfIZja1z3RSb9JVvWVYPcEhbIjD_k_J9GKf-aIhjuoqzL4nDr8etaPejoO8Uo8Tw5CL3eLPwk8WcJJwNOfzi-3fYVyDgmlu4WqgLZN_m-Q7MND7mK6ObplM3TO7DbQhsOpojIfb-SRX0vjFTreSYHcL54ZtETq0eduoEcnJKlJCvzoAvyxZZntjQjmklEiHB-JCl826l6CcPSMgUVDx0NcCL5W5MNvAjwVvqmIjYFkPdI_3RZszw2UpCXxKz-Zzn37LwyPXzsr3BOcHUBfa2blt9pFGsS_hnVaKflblgfmqvnU9vhof3LR04sZA1J6rpyYX3joEWEGctq3-oOWFe-byguDVcB5r-NbUnRdL_Au_nabg0_H8UUw1JbDlni1fwPvoABbOPKI0G7V5v83Fl13Vb2lWIuI2j41I2_bze6T36JAwzRVqdhVrju7zIOWOO3x40Q9JFUb6-UYGAcjb0iTp1EUFPV6FMw_oP9CMLekuVJI9SCYn8plebAGY3grIbSJhRdGpAfEe0CJWtmeWAMw6EcVMv9iA7gwMtaOjPsnst4o08StfWQu9OpvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=FxJKnMCAYUYKzBb60dOXiHfF19onFKUNMaXNu3PXnfb3Wsv3pBMtiCowhtHksyWC_bKN-xnjeV3u0mr6_gtmKW3dflvuAI6DshyG6RjLQOSf6KRLHfIZja1z3RSb9JVvWVYPcEhbIjD_k_J9GKf-aIhjuoqzL4nDr8etaPejoO8Uo8Tw5CL3eLPwk8WcJJwNOfzi-3fYVyDgmlu4WqgLZN_m-Q7MND7mK6ObplM3TO7DbQhsOpojIfb-SRX0vjFTreSYHcL54ZtETq0eduoEcnJKlJCvzoAvyxZZntjQjmklEiHB-JCl826l6CcPSMgUVDx0NcCL5W5MNvAjwVvqmIjYFkPdI_3RZszw2UpCXxKz-Zzn37LwyPXzsr3BOcHUBfa2blt9pFGsS_hnVaKflblgfmqvnU9vhof3LR04sZA1J6rpyYX3joEWEGctq3-oOWFe-byguDVcB5r-NbUnRdL_Au_nabg0_H8UUw1JbDlni1fwPvoABbOPKI0G7V5v83Fl13Vb2lWIuI2j41I2_bze6T36JAwzRVqdhVrju7zIOWOO3x40Q9JFUb6-UYGAcjb0iTp1EUFPV6FMw_oP9CMLekuVJI9SCYn8plebAGY3grIbSJhRdGpAfEe0CJWtmeWAMw6EcVMv9iA7gwMtaOjPsnst4o08StfWQu9OpvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا تهدید خاصی وجود داشت که باعث شد آن بمب‌افکن‌ها را از بریتانیا فراخوانید؟
ترامپ: بله، فکر می‌کنم بتوان چنین گفت. پرواز آن‌ها تصادفی نبود؛ تهدیدهایی در کار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72798" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72797">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449cc78904.mp4?token=tJhBhq0UF9XZ0lNW_o94Ber5BjWleux7hMcASWKy4QZKWtGyxu3NOvxYhQNIdFarmayCstDLoiDHZrb9ERk6TlgJnZD89v5nKzTwXUkwC1MAHZR8PUxNg2-OinzudYSF_FKYA9q8whx9nEYq_7F-dC_QB2XWJ43J90D17YMhYtoEAxgrFXoVa7Vc-m1FfKedDBFJ2HPmVfzE9N3VtQaNRGEg2oNO2DCVQke6cTlwmkD1qCVlpsfddfF9O_tkKUsz6XMmhU_0s5ZeLJgPMdzZmFXV1XXKxCC-V-3vtjgxFXVNvfcr26uB1BsKXeDlVVYNZ-CyYwzPtGAn_ObNwdkfgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449cc78904.mp4?token=tJhBhq0UF9XZ0lNW_o94Ber5BjWleux7hMcASWKy4QZKWtGyxu3NOvxYhQNIdFarmayCstDLoiDHZrb9ERk6TlgJnZD89v5nKzTwXUkwC1MAHZR8PUxNg2-OinzudYSF_FKYA9q8whx9nEYq_7F-dC_QB2XWJ43J90D17YMhYtoEAxgrFXoVa7Vc-m1FfKedDBFJ2HPmVfzE9N3VtQaNRGEg2oNO2DCVQke6cTlwmkD1qCVlpsfddfF9O_tkKUsz6XMmhU_0s5ZeLJgPMdzZmFXV1XXKxCC-V-3vtjgxFXVNvfcr26uB1BsKXeDlVVYNZ-CyYwzPtGAn_ObNwdkfgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در میدان آزادی (میان اقبال) سنندج از این کوماندو‌ها رونمایی کردن برای مردم! امیدوارم این فیلم رو هیچ وقت ترامپ نبینه چون بعدش قراره دیگه شبا آرامش نداشته باشه
😂
یه ساختمون چند طبقه رو ۱ دقیقه طول کشید تا برسن پایینش! از پله‌ها میومدن زودتر می‌رسیدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72797" target="_blank">📅 23:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72796">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=td3XqTUl0Gp8cdz8nfJzRLhJGD87VHqCwSN-lo3ayBpv6z5EXxjux_9qFw3emfyZ-diWgyGhxV0U1OT2U_mi2nFmAf0uy6KF9ws9XddswMblJk7ju76dqaNZ1EHyyo4SMXSTGPXisuSfRfGYmXop8B_TZQqgC2E7fhfDGrQ1WlJrxbFQjr-OV7Y32U5NcLdoY_yGBanTDymftEmVDGALVoaBaGrSOEVpHNxhbdOy5JteNZ-uJON38p_vhTR-4wa2Qwqq60ZI9A26lDYf24VzFNECc-zOe4BLdvOfySFsP5nsxMwOP-S2x0lhL_axPmTSxXYMzdeHX2JnHgDsMh6lUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=td3XqTUl0Gp8cdz8nfJzRLhJGD87VHqCwSN-lo3ayBpv6z5EXxjux_9qFw3emfyZ-diWgyGhxV0U1OT2U_mi2nFmAf0uy6KF9ws9XddswMblJk7ju76dqaNZ1EHyyo4SMXSTGPXisuSfRfGYmXop8B_TZQqgC2E7fhfDGrQ1WlJrxbFQjr-OV7Y32U5NcLdoY_yGBanTDymftEmVDGALVoaBaGrSOEVpHNxhbdOy5JteNZ-uJON38p_vhTR-4wa2Qwqq60ZI9A26lDYf24VzFNECc-zOe4BLdvOfySFsP5nsxMwOP-S2x0lhL_axPmTSxXYMzdeHX2JnHgDsMh6lUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شامگاه شنبه ۱۱مهر۱۴۰۵؛لحظه برخورد صاعقه با برج میلاد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72796" target="_blank">📅 22:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72795">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=uflKWoWuFzUfs1S89HqXML_MA5_WD_Q8fuRgVPwg1bcssifBWci0FZ-Vue5RaEVpaqoqYmFGVmSRF6ewahZ6D90OukQAs9JbWbFfXe0-sz-gYyqMfRdLm78yD8tISsd2Iikc-XaMyrFuOm7r7UMTImLyLHW4ABFyGnpHaqoAipdvw-dVR4AOXPkktFSwDZ4_PcxyLQlfsbyP7Lx9UBGN8hLmi-Ibgvzdo5sRRR_xbPXOZ_JmtfkGjpl3QnYB09YX0ErKdFTXV4G9deMDtjSWDW4Ha-t9LBg-pPxGBKeD7BST6_eW8Dnun0V7BLGnYJzTc8QbLdv6Kl3Jj6laMwibHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=uflKWoWuFzUfs1S89HqXML_MA5_WD_Q8fuRgVPwg1bcssifBWci0FZ-Vue5RaEVpaqoqYmFGVmSRF6ewahZ6D90OukQAs9JbWbFfXe0-sz-gYyqMfRdLm78yD8tISsd2Iikc-XaMyrFuOm7r7UMTImLyLHW4ABFyGnpHaqoAipdvw-dVR4AOXPkktFSwDZ4_PcxyLQlfsbyP7Lx9UBGN8hLmi-Ibgvzdo5sRRR_xbPXOZ_JmtfkGjpl3QnYB09YX0ErKdFTXV4G9deMDtjSWDW4Ha-t9LBg-pPxGBKeD7BST6_eW8Dnun0V7BLGnYJzTc8QbLdv6Kl3Jj6laMwibHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: اخراج ما از آمریکا مثل اخراج تیم برنده از المپیکه!
پس خبر درست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72795" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72794">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=euHh1-VX6S0_QV2-kHbiwOh1tDeNr3qYuGuvvnXnGyT4_Ge0U3DoKZurm3v9qu0NXyAY3Rt8d7_LynYCy0kb0vXYHP9sNaHyN70dkgrR2eZwiRZIqZbvO8on-fFPgeHy27MHHrywpX-JQabjoSX-bUkZobABBHJtNX0C01iYcf_hPK7G6tNdm-LYNmdqc580dqlnOq0TsPeip8RIldvfEHHgZ4cLsg8po3pZLdGxxG-6iDNDLSTTrNnlyzfhAEev1FMtXvYO2GHCxuaXckkyoQmdo-lSqxRO0yTLpO_fNd8Nbf3RuikZXVAUktflvbLujOVuAnjIg2Id5PS-ab1Z2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=euHh1-VX6S0_QV2-kHbiwOh1tDeNr3qYuGuvvnXnGyT4_Ge0U3DoKZurm3v9qu0NXyAY3Rt8d7_LynYCy0kb0vXYHP9sNaHyN70dkgrR2eZwiRZIqZbvO8on-fFPgeHy27MHHrywpX-JQabjoSX-bUkZobABBHJtNX0C01iYcf_hPK7G6tNdm-LYNmdqc580dqlnOq0TsPeip8RIldvfEHHgZ4cLsg8po3pZLdGxxG-6iDNDLSTTrNnlyzfhAEev1FMtXvYO2GHCxuaXckkyoQmdo-lSqxRO0yTLpO_fNd8Nbf3RuikZXVAUktflvbLujOVuAnjIg2Id5PS-ab1Z2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آقای آتش‌نشان در مورد ساخت پلاک مشخصات برای دانش آموزان:
امروز رفتم یه دبیرستان دخترانه برای کنترل مسائل امنیتی بین حرفامون با مسئولین مدرسه متوجه شدم که دارن برای دانش آموزان پلاک مشخصات فردی درست میکنن مثل همونایی که زمان جنگ استفاده میشد؛
از این پلاک‌ها که زمان جنگ سربازها مینداختن دور گردنشون که اگه بر اثر بمب و موشک چهره‌شون دیگه قابل شناسایی نبود، از رو پلاک شخص رو تشخیص بدن..
وقتی پرسیدم برای چیه؟ گفتن نمیدونیم فقط از بالا دستور گرفتیم و مشخصات فردی دانش آموز رو دادیم تا براشون درست کنن!!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72794" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72793">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgPqpxvomLacOILrFGJ6anL-gmQ5i1nYLRyGXIDJPaEheXZBJrCoj1blYtiBe02gj6jBTkHrUy4rQYAfn17I0PLd6lCw_-DfuB7-1PPLLBlOm4GFshI33jjnUxAYplAt-TGx2dNtn2p9Ym3QPkyaUACml5ksZ6iM59htL-O-B3XEL5ec_IBMyc3gdXaKJo8_fhP2zkUtqubRdN6ZGcrPsnZ2_2WNxUxVS7LkCByBB151bdkyqfch5PTqHjJsURCY4z-8kM9jYFRgnYVeDGKCXafDCKnTxX3C6PsT59ypnAVPtrrDLh0CDqPbN7s6VzIwQk_rgSac9aq3bvYoQmXB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
آنچه باعث افزایش قیمت بنزین می‌شود دیگر تنگه هرمز نیست — چرا که اکنون حجم بی‌سابقه‌ای از نفت (بشکه) تقریباً به‌صورت روزانه(از تنگه هرمز)عرضه می‌شود
.
بلکه مسئله «پالایشگاه‌ها»ست؛ جایی که پالایشگاه‌های روسیه توسط اوکراین منفجر می‌شوند و پالایشگاه‌های ما در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط «دموکرات‌های احمق» تعطیل می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72793" target="_blank">📅 20:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72792">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902f67b684.mp4?token=TvWG7ERS82v_gncBb9zV6S3uveolgltOJb6F1f8ekWvqYIP28w_DWFll8m8YPJKL-NX-77X1shaGTUUAbqDcYjIMV0f5KONPhM-4578bDkZZaf9I9wlECyUhugW5frJ91RyZS2EmSTlQaA8FEuUfxdC3x3O1p7pXnHzIqxPv7jIcRiA5c8UezjbzgVlCwVsvouaB8na8suNwS2B5zN8yqyf86bQd7aBKMIkw3XQ_lpaeKT74C9GMvryW1nrfEZPoL9ieXv-1DMPffas7tKRy4Ul71ByZczR4POatZlLFPq2Pv_RtALBTXYjg52CpqGJkcbUaj0LYyAr53jEr4fU31Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902f67b684.mp4?token=TvWG7ERS82v_gncBb9zV6S3uveolgltOJb6F1f8ekWvqYIP28w_DWFll8m8YPJKL-NX-77X1shaGTUUAbqDcYjIMV0f5KONPhM-4578bDkZZaf9I9wlECyUhugW5frJ91RyZS2EmSTlQaA8FEuUfxdC3x3O1p7pXnHzIqxPv7jIcRiA5c8UezjbzgVlCwVsvouaB8na8suNwS2B5zN8yqyf86bQd7aBKMIkw3XQ_lpaeKT74C9GMvryW1nrfEZPoL9ieXv-1DMPffas7tKRy4Ul71ByZczR4POatZlLFPq2Pv_RtALBTXYjg52CpqGJkcbUaj0LYyAr53jEr4fU31Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا توانایی خودشو توی بسکتبال هم نشون داد و تقریبا همه توپاشو سه امتیازی وارد سبد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72792" target="_blank">📅 20:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72791">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=DLdWEpJzFCvGf29TfrvSOQCYia688RXPdhGL90rRz8hyfz5v3wC1VPK2KDVedjP35GkixJ3LA-9L9kHQy4sKaFxyZ3XBEwpCSBkRmPaovkpV72lPtd6rUOqw3EB9NDaDvDMsEpVFWZ7ip1t75ELo7YTsxVgVroqcUAbJL-arzO1nOi_chOTmyTag0vUUVagF64KGT62fPL7MT_R4huxmT8oGmxeGgvsznu_1zSlG4yfodjtO9YHeyySLasjQw18v_AVVV6DJzcY9Nx-6CjuwBZH0gCgiHaAEvzK5SBuZAOKQIMZfsLX7a2oj5iPADf5q4a3Fuw9EVChbU5ZZ6dpo7w8beqURUlDAOap_xq50P3NvDh5u51ZNCPRqdP_HngNy2nl1xyBtIJ4bJW77L8xlwNY_gjjWRgwhhCXIRMBV8gdzSj0VWOFYmEy_nel4esg6fHpYMNTxMF_maMYUsgjEbQD30Z-wa3SB3HquAXgC-9lQij_nRthSEZWXHJ-zC2A4KZuVhveU-7EmbOLS1VvlhdwAtpOG1lTFCnzzRQIWiPg7g7SVDI-DjbbWmHNYgduAh57hmLoo-zPWZsnFOzY_D85SnH1VkJTeMSJQ1tRLPlf0j8nlKNTRa7ngwE0fTcK5j6zutPSCILrxtWTnb5CjGfq1U8q-bOycSNXQw_-oZ1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=DLdWEpJzFCvGf29TfrvSOQCYia688RXPdhGL90rRz8hyfz5v3wC1VPK2KDVedjP35GkixJ3LA-9L9kHQy4sKaFxyZ3XBEwpCSBkRmPaovkpV72lPtd6rUOqw3EB9NDaDvDMsEpVFWZ7ip1t75ELo7YTsxVgVroqcUAbJL-arzO1nOi_chOTmyTag0vUUVagF64KGT62fPL7MT_R4huxmT8oGmxeGgvsznu_1zSlG4yfodjtO9YHeyySLasjQw18v_AVVV6DJzcY9Nx-6CjuwBZH0gCgiHaAEvzK5SBuZAOKQIMZfsLX7a2oj5iPADf5q4a3Fuw9EVChbU5ZZ6dpo7w8beqURUlDAOap_xq50P3NvDh5u51ZNCPRqdP_HngNy2nl1xyBtIJ4bJW77L8xlwNY_gjjWRgwhhCXIRMBV8gdzSj0VWOFYmEy_nel4esg6fHpYMNTxMF_maMYUsgjEbQD30Z-wa3SB3HquAXgC-9lQij_nRthSEZWXHJ-zC2A4KZuVhveU-7EmbOLS1VvlhdwAtpOG1lTFCnzzRQIWiPg7g7SVDI-DjbbWmHNYgduAh57hmLoo-zPWZsnFOzY_D85SnH1VkJTeMSJQ1tRLPlf0j8nlKNTRa7ngwE0fTcK5j6zutPSCILrxtWTnb5CjGfq1U8q-bOycSNXQw_-oZ1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره خروج هر ۱۲ فروند بمب‌افکن «بی-۱» (B-1) از پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford):
آنچه در آنجا شاهد بودید، اقدام وزیر دفاع برای محافظت از نیروهای ما بر مبنای احتیاطی مضاعف بود.
ما با اطمینان نسبی معتقدیم که ایرانی‌ها در پی انجام همان کاری هستند که حکومت ایران طی ۴۹ سال گذشته انجام داده است؛ یعنی ارتکاب اقدامات تروریستی علیه ایالات متحده و همچنین علیه بسیاری از افراد دیگر.
ما نهایت احتیاط را به خرج می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72791" target="_blank">📅 19:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72790">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rue_ay9sG0UWVcSgnmsfU2LhwARrs-bfoxWthTOCxV3PgyKYmhXVc56copREcm5r6cTit3VaCl58j8GbhGwc49VYFy4bZderuZo79-1wcxBqVnMhFqnijEwd_5K5CknpqacMoOj_02_5b5X9o8Hzt2gdIx1o9--qs55RN5f_YqfjeA4fgFqozVTsjaYIzRhTMvUdGrRg3S-vuh87siO-j5RPpGlKF-hlTYkHut9hyGPqdoDk84OeO3TyJFtj2r44-aQ1BPVOs_MoA2jVo2JM6uyX28BXVzsM_GHD6xc91_Cs-lF9oQpZu-nZjbvhUGa-LBuAuiuQT-bzqb3YJxWOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.
پوکت نخستین بندری است که این ناو از زمان ترک ایالات متحده در ماه مارس در آن پهلو می‌گیرد؛ قرار است کارکنان آن از ۴ تا ۹ اکتبر برای گشت‌وگذار، فعالیت‌های فرهنگی و برگزاری یک مسابقه فوتبال میان آمریکا و تایلند، در خشکی حضور یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72790" target="_blank">📅 19:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72789">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=IdoJWZqU_y6zxz9RxrAfd5VGDrw195CiAvlDpSWmEHvd1PZCUCHh4-08_4yzf5tBudhkdrdD2NVT5JcfOSjBOR0l7S3NJjMvcnh8cUmEUbNAE0Lt7NgslLvkZzrsLwszFh2uJ5a4-rXbK6F9FAU7ljEwm0IqevX3q4huy9rRgAS5ivBnP8JQwvtkOKNpQEqFxuReyu6ZGlR_4lG1hleUWywQNr9HLsxQ9jzll0mmp520NDH3Xdm8qwqo_hL9q8mOGYkXgScauWI03kavmeJ5-RbVkJJnPBQxaC7bdNAjkUTsd2F6ljIu2XVrZuYfwLKn9HBvfyVkib0l5fkd_Lq2jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=IdoJWZqU_y6zxz9RxrAfd5VGDrw195CiAvlDpSWmEHvd1PZCUCHh4-08_4yzf5tBudhkdrdD2NVT5JcfOSjBOR0l7S3NJjMvcnh8cUmEUbNAE0Lt7NgslLvkZzrsLwszFh2uJ5a4-rXbK6F9FAU7ljEwm0IqevX3q4huy9rRgAS5ivBnP8JQwvtkOKNpQEqFxuReyu6ZGlR_4lG1hleUWywQNr9HLsxQ9jzll0mmp520NDH3Xdm8qwqo_hL9q8mOGYkXgScauWI03kavmeJ5-RbVkJJnPBQxaC7bdNAjkUTsd2F6ljIu2XVrZuYfwLKn9HBvfyVkib0l5fkd_Lq2jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)  تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72789" target="_blank">📅 18:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72788">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)
تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون از دست می‌ره (کنترل شهر مهم تعز همچنان به دست حوثی‌هاست)
#hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72788" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72787">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حوثی ها دو موشک را به سمت منطقه ای که تحت کنترل نیروهای دولتی یمن بود شلیک کردند.
در همین حال خبرنگار شبکه العربیه در حال آماده‌سازی برای پخش زنده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72787" target="_blank">📅 18:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72786">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMYlvl1imaHqL0jcm6CSHMwlV3RgJ6_75dWykdAnJIrAT_-zebgwLEiaGlgznknRfc0iS847EpLYXhfOarQb6iUGn7K6qDMVrew5MZAolDhGb5caii5rHtszEGEwaH-1Nxza_GcyZfWsVpuQKYfXlESvxwUHWHw3fRGwaAZx0lZrnZHffOkKkEnIiacsTkglHxrhByjq5TRxgMsjKk5YVmGsplhaMaEjRVOQFu0Jb66NQDiIdIoV0E5gn8yl0KhUKN4PQZl4ofbPU1xR70GNORfCqUmMt0XvLJuF2fom5SyV56rGc3MKBVkIpKC_9FKK5pE8CB3_PKdGjMNl3Eje8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛
مشاوران ارشد امنیت ملی ترامپ نشستی محرمانه و چندساعته را در «کمپ دیوید» برگزار کردند تا درباره احتمال جنگ با ایران و درگیری میان عربستان سعودی و حوثی‌ها در یمن گفتگو کنند.
ریاست این نشست بر عهده معاون رئیس‌جمهور، ونس، بود و مارکو روبیو، پیت هگسث، استیو ویتکاف، جان رتکلیف (رئیس سیا)، ژنرال دن کین و اسکات بسنت (وزیر خزانه‌داری) نیز در آن حضور داشتند.
یک مقام آمریکایی اظهار داشت که در این جلسه درباره مسائل عمده خاورمیانه «تصمیم‌گیری شد یا دست‌کم بحث‌های عمیقی صورت گرفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72786" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72785">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72785" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72785" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72784">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaEbu5jmafnzUC_MZChUZySU8rbMfkU9yVKR3uen7WJwf3GKJsNqJDlGkw6xYPl98lzEJ_jeY1jhPDuP9Efcq-eSY5cuc5S4yCnOFSn8TFp8GSt9TarLA8wqeNkrKTQ9R6BawIZlvqP-IzSJdRVjenNYm1E01MTnWgTOLt9ljHCdE1B_0LUSQFtXGLzSAfvVGFteWNEzY_-DkTukxtfkY1m-YshEjLEUlAOW9vFb7gY-g92XN5CgaijrRlX8F4_LXklbhVRIFDprZO0syzRkt3qTFW8tVyS5vOWGGKZCnNULcra_fpF3g2XIhwqOhRVYmDLzZSE3jUw6VxaGD6xjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز بلژیک
🆚
فرانسه را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بلژیک: ۳ برد، ۲ شکست و ۱۰ گل زده
فرانسه: ۲ برد، ۱ تساوی، ۲ شکست و ۷ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72784" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72782">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=RpzSrKvt0qovABS48ThM04baScYQERwU-ZEGEdJe3z936UTZ7b5P_yCss56IR9n3jz-70aZ6kmW8ncDioDa1ksw3BMN0EKfeoxcs06pvzXWtuVfzBCC5HzdkLyrMm2tFzufFg9Dy1vwCw8sJGhZVeDgxZTN2TmNh-3uRRSAHgXs7cWCqCv23nWgDKGMfsBDtm0kmWdv_CWd00tDKR8WJkNMpcWZr82MNSYecUgcaUdu4PbRIWZES9DHynjUvl4795JT5XGB3DzW_rQvpabK0JCL9iNErhSlSpUrgMqQ-OuO2L4F0LHmdfsSnJ7VXorw-2dbrKe4VS0X3f7LO_hd54Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=RpzSrKvt0qovABS48ThM04baScYQERwU-ZEGEdJe3z936UTZ7b5P_yCss56IR9n3jz-70aZ6kmW8ncDioDa1ksw3BMN0EKfeoxcs06pvzXWtuVfzBCC5HzdkLyrMm2tFzufFg9Dy1vwCw8sJGhZVeDgxZTN2TmNh-3uRRSAHgXs7cWCqCv23nWgDKGMfsBDtm0kmWdv_CWd00tDKR8WJkNMpcWZr82MNSYecUgcaUdu4PbRIWZES9DHynjUvl4795JT5XGB3DzW_rQvpabK0JCL9iNErhSlSpUrgMqQ-OuO2L4F0LHmdfsSnJ7VXorw-2dbrKe4VS0X3f7LO_hd54Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جنجالی کوچک‌زاده مجلس :
کدام کارمند و مردم عادی پول دارد ۲/۵ میلیارد تومان بدهد ده هزار دلار بخرد، این پول زیر متکای امثال همتی و دزد‌ها و اطرافیانش میرود.
آقای قالیباف، چرا مملکت اینطوری شده که راننده رفسنجانی هر کاری می‌خواهد در این کشور می‌کند؟
طرح جدید بانک مرکزی؛
هر ایرانیِ بالای 18 سال می‌تونه تا 10 هزاردلار (۲ میلیارد و ۷۰۰ میلیون تومن) از بانک بخره!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72782" target="_blank">📅 17:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72781">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=VL_WkK8jjAGqWinQml6_1lvZC9mpug9YCH0-2Sm349Zj-6HZTHLroFTg3wrguGMzKL9cd_QZ5ubpKttOJDQiyB0-EP4UNerjcSaIOWKeFNxib1yK_oDjNoPayIvLP85V5wKw6uaxv7BkvsGSzW_OZMOMhnkQHLGbI4yB54KUcUpMh6SO9eD92Ig3bpXLdKWPoqEvwm-1dS8BKOFsFemEMx-X4jX3x6RZWz3z6JUIjNEm9wI5r29w3_5m3qEw2ZxG460WTLDm5b58Eay-a16ATyizeyRgnVbc74fSIO0Oe2v8ju3_6rddLuktWhl5kkM9WJt9f2fX9bTwZfAYu0iX10uMTpMIrrhdpn5yoqu-6FMtEkDtyJs2tBICVtHv8vkjIxLtVa6bT2EBAHcx6vDSxeRXAqCOguekpDMPUqwL2RCv2cT4jMIdqaGBJOxldu21t8oFi84ggL_kfdHxKluuRp9eOOfUPm1PTVdBf2r3wTj1daRRloTgVfs7k1Btkd_z3BpjZNleM_iJ0WW1Ub314dhlxxfydUc0kRBuoEA5TtYBmi2RB1JM_Bbr6fFVv5XpIcOuhBxkwuyU0q62hAjEwCZN1Wrpe9N81H6ydCx25y2B0uXygbhgTHNJNQP9y7eshLcO09ErvLF25jFo_FdFQV0oMDa_f-FitaPDAlbfU-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=VL_WkK8jjAGqWinQml6_1lvZC9mpug9YCH0-2Sm349Zj-6HZTHLroFTg3wrguGMzKL9cd_QZ5ubpKttOJDQiyB0-EP4UNerjcSaIOWKeFNxib1yK_oDjNoPayIvLP85V5wKw6uaxv7BkvsGSzW_OZMOMhnkQHLGbI4yB54KUcUpMh6SO9eD92Ig3bpXLdKWPoqEvwm-1dS8BKOFsFemEMx-X4jX3x6RZWz3z6JUIjNEm9wI5r29w3_5m3qEw2ZxG460WTLDm5b58Eay-a16ATyizeyRgnVbc74fSIO0Oe2v8ju3_6rddLuktWhl5kkM9WJt9f2fX9bTwZfAYu0iX10uMTpMIrrhdpn5yoqu-6FMtEkDtyJs2tBICVtHv8vkjIxLtVa6bT2EBAHcx6vDSxeRXAqCOguekpDMPUqwL2RCv2cT4jMIdqaGBJOxldu21t8oFi84ggL_kfdHxKluuRp9eOOfUPm1PTVdBf2r3wTj1daRRloTgVfs7k1Btkd_z3BpjZNleM_iJ0WW1Ub314dhlxxfydUc0kRBuoEA5TtYBmi2RB1JM_Bbr6fFVv5XpIcOuhBxkwuyU0q62hAjEwCZN1Wrpe9N81H6ydCx25y2B0uXygbhgTHNJNQP9y7eshLcO09ErvLF25jFo_FdFQV0oMDa_f-FitaPDAlbfU-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: چرا بمب‌افکن‌های آمریکایی پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) را ترک کردند؟
روبیو:
مشاهده چرخش نیروها و جابه‌جایی تجهیزات، امر غیرمعمولی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72781" target="_blank">📅 17:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72780">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=aoMXp5Ul5mGth8fZYuiT117o5nxXGZdCf-79jJaH7xZ0oMN0I0YrJWhDANVmL5Q11V6xa8_AdL7NqrX5FSzTR5wXvX0ejFiLBgfLS8jPDY2o2yBDx-sHgzi4HicmxlxH8u0PCOejmkkbVJGm_F1xZq0ucptexHWjHHxv-s5u7XZqXOaZ_RgS_NQfln7Nk4XVvdLDDfm4Z7ZtHXU-hxasnpu_y4LC6wLsap_ObHvF-avXLDtMhBdPAkMtiLcAemEpDRqNnrQipcG7H1UDZ1J_DXWYnYsLz_S2Zc1ODv4Jn-8qycR1T_Eieh4wf88zIcaDEp6rgr2yN0fe2_1dscBthw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=aoMXp5Ul5mGth8fZYuiT117o5nxXGZdCf-79jJaH7xZ0oMN0I0YrJWhDANVmL5Q11V6xa8_AdL7NqrX5FSzTR5wXvX0ejFiLBgfLS8jPDY2o2yBDx-sHgzi4HicmxlxH8u0PCOejmkkbVJGm_F1xZq0ucptexHWjHHxv-s5u7XZqXOaZ_RgS_NQfln7Nk4XVvdLDDfm4Z7ZtHXU-hxasnpu_y4LC6wLsap_ObHvF-avXLDtMhBdPAkMtiLcAemEpDRqNnrQipcG7H1UDZ1J_DXWYnYsLz_S2Zc1ODv4Jn-8qycR1T_Eieh4wf88zIcaDEp6rgr2yN0fe2_1dscBthw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آترینا فرحمند رتبه یک کنکور تجربی ۴۰۴، پارسال همین موقع:
دخترا خیلی خفن‌تر از پسران، من مطمئنم رتبه یک کنکور تجربی سال بعدم دختره.
نتیجه:
توی کنکور تجربی امسال از ۱۰ نفر برتر، ۹ تاشون پسرن و رتبه یک هم پسر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72780" target="_blank">📅 17:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72779">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=h3bXfKUH81KsbeJU8Af5X4Qy-l0n3Rqly_foUtmQ82eemHZbwqFf9CP7QCYmveB8fQ58GbwRpzSXAIZfOhINVedMqkOG_vKMSuYRaJp5XTZEJ53uzGA8iUZxSx76q-E2S8nCs-rFmnMVUfv1WAXbZjidhsGZj7TahLKhgugFzFATb2EWL62RLZcXXnZv9RJQj4Th8a-4UwYgsYaZG5_zsncyWqMBbqnKkbReYldn2AC2vhRmsOupAyF2edU4ys6B2xGHx-Xhe_UTMnyP1Gfa__xCih9sNQIgA6WNHJHIYLNLoKDAdyFl0gJZWirILpWzLY1abIN02k1GDJrCBS_Nujc7rxsrVwKZzaUUzJ7FxyEKi3jU1mJniiZ_xDUX-R4EgMcey4HVL_u3lgtR5ufRumj4DXKPhkErpSnyMHRNVaNhmv2ifwdTahZBDleaWZ9ihQ03XjQO4XbUyWbh0hjAFkg4Ohnb_ccaI7yQo1EaGhheKKwPYoMBcixUPPOu4LuS8dgXS4OXBFydoytbkpCXBNhRF53ckmAWN9Ew3gB1yMPvKYEXAS-BYFlR8UyWwZcVZ2bk_y1JR5wJBhJjumSoWcYg7vQlIh-6P6wdYJKPhToXE9TWpf-GIpKgg_ZlOydXzt00Cy5dKcMAD3XvoHRtORS3VATsJo0GxQX04uI1B6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=h3bXfKUH81KsbeJU8Af5X4Qy-l0n3Rqly_foUtmQ82eemHZbwqFf9CP7QCYmveB8fQ58GbwRpzSXAIZfOhINVedMqkOG_vKMSuYRaJp5XTZEJ53uzGA8iUZxSx76q-E2S8nCs-rFmnMVUfv1WAXbZjidhsGZj7TahLKhgugFzFATb2EWL62RLZcXXnZv9RJQj4Th8a-4UwYgsYaZG5_zsncyWqMBbqnKkbReYldn2AC2vhRmsOupAyF2edU4ys6B2xGHx-Xhe_UTMnyP1Gfa__xCih9sNQIgA6WNHJHIYLNLoKDAdyFl0gJZWirILpWzLY1abIN02k1GDJrCBS_Nujc7rxsrVwKZzaUUzJ7FxyEKi3jU1mJniiZ_xDUX-R4EgMcey4HVL_u3lgtR5ufRumj4DXKPhkErpSnyMHRNVaNhmv2ifwdTahZBDleaWZ9ihQ03XjQO4XbUyWbh0hjAFkg4Ohnb_ccaI7yQo1EaGhheKKwPYoMBcixUPPOu4LuS8dgXS4OXBFydoytbkpCXBNhRF53ckmAWN9Ew3gB1yMPvKYEXAS-BYFlR8UyWwZcVZ2bk_y1JR5wJBhJjumSoWcYg7vQlIh-6P6wdYJKPhToXE9TWpf-GIpKgg_ZlOydXzt00Cy5dKcMAD3XvoHRtORS3VATsJo0GxQX04uI1B6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا می‌توانید آخرین وضعیت مورد مشکوک به طاعون در روسیه را به ما بگویید؟
مارکو روبیو: ما به‌دقت وضعیت را زیر نظر داریم. فکر نمی‌کنم این مسئله جای نگرانی داشته باشد، اما نیازمند توجه و تمرکز است و ما نیز همین کار را انجام می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72779" target="_blank">📅 16:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72778">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a15378585.mp4?token=sB7szce_iG6tOhq68nni0iKyiwWlS1zpuVXX2GaUe1JW4Ht7xxUT1byxiSm8GuhzgYjtGvSnmx5KEAw6Mek-yq3iJ9dcDWt_xCNbcDEYEHCb7eJqSZrqj8Z4In_cu-0fswCDF5dGi9NmskPnCxvBE8Z6Hvu00zfw449evMneS7SgWBL7zPcbgYgRcwxaLUYWjj5u9TLxFmBeFBzcsv7xMRJg_3m-U4n4ztaZ0_cLFgJCJ7a9butS-1Am5aymYdpeq4uaDHprYI2rWOXqcbgH_FjkdwhZhrVXylnZrysOAuuxBKNaaTNLpfFMpcsnqYQxTEPrNi0S6sZN0ra5VDxYR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a15378585.mp4?token=sB7szce_iG6tOhq68nni0iKyiwWlS1zpuVXX2GaUe1JW4Ht7xxUT1byxiSm8GuhzgYjtGvSnmx5KEAw6Mek-yq3iJ9dcDWt_xCNbcDEYEHCb7eJqSZrqj8Z4In_cu-0fswCDF5dGi9NmskPnCxvBE8Z6Hvu00zfw449evMneS7SgWBL7zPcbgYgRcwxaLUYWjj5u9TLxFmBeFBzcsv7xMRJg_3m-U4n4ztaZ0_cLFgJCJ7a9butS-1Am5aymYdpeq4uaDHprYI2rWOXqcbgH_FjkdwhZhrVXylnZrysOAuuxBKNaaTNLpfFMpcsnqYQxTEPrNi0S6sZN0ra5VDxYR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره یمن:
به‌نظر من، سعودی‌ها و نیروهای یمنی به‌وضوح مخالف آن هستند که حوثی‌ها کنترل آن منطقه نزدیک به تنگه را در دست داشته باشند.
این منطقه در پی تهاجم حوثی‌ها به تصرف آن‌ها درآمده بود و اقدام کنونی، واکنشی متقابل به آن است. ما انتظار چنین اتفاقی را داشتیم و همین هم رخ داد.
سعودی‌ها هدف حملات حوثی‌ها قرار گرفته و متوجه تهدید ناشی از آن هستند؛ از این رو، حق دارند که از خود دفاع کنند.
نیروهای یمنی تلاش خواهند کرد تا مناطقی را که از آنجا بیرون رانده شده بودند، بازپس گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72778" target="_blank">📅 16:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72774">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=aiG71NWbdrV5-z7GUKn5XP0ZZQaTTtL9KAWQinVuDoxynEz615SFqfUpdfXi-jNrlKLajZiuvRD6hj2F6Q9t4WmoowkDNXfWKN-b2EunypGU_ihhFI75BjhXT6MfO6oBpjtFYKJIkwE1nfn7XMotaXd7x6XuvFMjZ4INsHB9ccyHbg_MTUc01WLfDfH14vtqUy1RemE4-l18kjK2Zb-E0R9sOvxhgJt8o1UKNbblPWZVGUZxcPFp4B0JAvWUp9nr6IsoqNIwCfsVB78-Rci8XrpVf-Dc8A6LJBCggg-bxACn7SyW240zLr3WPq_Qm635U9_31EPXt46eByL4xFcVKzhs6mNLt2L2xfPlDnekgLT0xD2IdrzYfoNhM-IuXxzWqULj9lWJqxEolTkBLEmdnjeSsubQ3-y2CtXI01HvsKikkUOPjNWma01Hmyd9uAOMzVdogjyjnjcTOl7VdR0ny_0_vLL8GB7jh6wcSsWi9pTqf-_gLpN7Iwq0omHhhTJ6OfjsY5MhmQy1MaZ369LNDL3J-UFWWM5jB9VuocNjhViDEffxTakNZgOoSdAbXTcXhOFFHphv1emjj7c2ZT58bJsGF-S2lrYQ86lxmv8DhoylWPqz4M8bpkbBZKAo1oiEAJGjpcuWnFbDXw6IO4yTu62ojY78IXZ0if_112A_UwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=aiG71NWbdrV5-z7GUKn5XP0ZZQaTTtL9KAWQinVuDoxynEz615SFqfUpdfXi-jNrlKLajZiuvRD6hj2F6Q9t4WmoowkDNXfWKN-b2EunypGU_ihhFI75BjhXT6MfO6oBpjtFYKJIkwE1nfn7XMotaXd7x6XuvFMjZ4INsHB9ccyHbg_MTUc01WLfDfH14vtqUy1RemE4-l18kjK2Zb-E0R9sOvxhgJt8o1UKNbblPWZVGUZxcPFp4B0JAvWUp9nr6IsoqNIwCfsVB78-Rci8XrpVf-Dc8A6LJBCggg-bxACn7SyW240zLr3WPq_Qm635U9_31EPXt46eByL4xFcVKzhs6mNLt2L2xfPlDnekgLT0xD2IdrzYfoNhM-IuXxzWqULj9lWJqxEolTkBLEmdnjeSsubQ3-y2CtXI01HvsKikkUOPjNWma01Hmyd9uAOMzVdogjyjnjcTOl7VdR0ny_0_vLL8GB7jh6wcSsWi9pTqf-_gLpN7Iwq0omHhhTJ6OfjsY5MhmQy1MaZ369LNDL3J-UFWWM5jB9VuocNjhViDEffxTakNZgOoSdAbXTcXhOFFHphv1emjj7c2ZT58bJsGF-S2lrYQ86lxmv8DhoylWPqz4M8bpkbBZKAo1oiEAJGjpcuWnFbDXw6IO4yTu62ojY78IXZ0if_112A_UwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دولت ائتلاف مردمی یمن می‌گوید نیروهایش باب المندب و فرودگاه ذباب را طی یک ضدحمله با پشتیبانی هوایی سنگین عربستان سعودی از حوثی‌ها (انصارالله) بازپس گرفته‌اند.
سرهنگ ماجد النزیلی، سخنگوی ارتش، گفت که تیپ‌های غول‌های جنوبی و نیروهای سپر ملی، این مناطق را به عنوان بخشی از عملیات «فجر یمن» ایمن کرده‌اند.
نیروهای تحت حمایت عربستان سعودی در حال پیشروی به سمت مخا هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72774" target="_blank">📅 16:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72773">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=oXZ8hMII7XTGB6k8vjnXtKOxYwWsWi71v25uPMQNYaRA3LCPXhBfdLuRoLb93LHM1i7S7ApeiBzCroZ0dvKPFtWVkmUEe781e5GEOWRtalok-pfqx_J-ar4uR88awN0aLuFHWjDUtXGvzu2Hb0A5YaO4ciO5qWQqTcFpDx6OJD5rVEhJzOADuKEFGp-NsymqbwHCHnZcsxZVY9FIKVikfDh0d37K1j7S-dqT4dYL0TqkazpHp0IwhQiXoN5G7ynI1Xn4b6h4oqJ3QFnTxkUEfCP_6K3OyIKKrjIuzh2aDoUJ3E5jH5OXfhnGEYqKcX70W2feaSX3PFxmFA4tT4yhLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=oXZ8hMII7XTGB6k8vjnXtKOxYwWsWi71v25uPMQNYaRA3LCPXhBfdLuRoLb93LHM1i7S7ApeiBzCroZ0dvKPFtWVkmUEe781e5GEOWRtalok-pfqx_J-ar4uR88awN0aLuFHWjDUtXGvzu2Hb0A5YaO4ciO5qWQqTcFpDx6OJD5rVEhJzOADuKEFGp-NsymqbwHCHnZcsxZVY9FIKVikfDh0d37K1j7S-dqT4dYL0TqkazpHp0IwhQiXoN5G7ynI1Xn4b6h4oqJ3QFnTxkUEfCP_6K3OyIKKrjIuzh2aDoUJ3E5jH5OXfhnGEYqKcX70W2feaSX3PFxmFA4tT4yhLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات خلبان هواپیمایی زاگرس در خصوص نبود رادار و تاخیر پرواز
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72773" target="_blank">📅 16:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72772">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=N-6qqU7DHnodZeCF2qtwjThEx5qZcIdpYruGc1EDg450jD4Q10zt_ezVlsbRCxmSCMidgbBLrP5_c5RzM6vtfmw5kNDzRGX-mXQrbbcZlZ-rDIe5KnS0PKXBdYvF8RCD7jRg2PTPvYOgQmlZ0Ev6s91fFg3sorAHkNp0eNCqeltO50W-MpZ-NcSlMW3qpUqEcU3MdJwIKP47Nncw43AxE6gQpeVgUWg_iYE4Q-FOeM3YqOSt4qCuFSULHeMApoMGfU6YgtDv-QiRV20tGE6h0UBwuFSjnlatPUgTT9GMfu84-KFavb6qRNytQu2N_sOJZoBb1y9CrWZ-iWrLAnhF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=N-6qqU7DHnodZeCF2qtwjThEx5qZcIdpYruGc1EDg450jD4Q10zt_ezVlsbRCxmSCMidgbBLrP5_c5RzM6vtfmw5kNDzRGX-mXQrbbcZlZ-rDIe5KnS0PKXBdYvF8RCD7jRg2PTPvYOgQmlZ0Ev6s91fFg3sorAHkNp0eNCqeltO50W-MpZ-NcSlMW3qpUqEcU3MdJwIKP47Nncw43AxE6gQpeVgUWg_iYE4Q-FOeM3YqOSt4qCuFSULHeMApoMGfU6YgtDv-QiRV20tGE6h0UBwuFSjnlatPUgTT9GMfu84-KFavb6qRNytQu2N_sOJZoBb1y9CrWZ-iWrLAnhF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی پویش جانفدا: در میان ثبت‌نام‌کنندگان افرادی هستن که اقامت آمریکا دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72772" target="_blank">📅 15:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72771">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=oQhTwaMkYiq3fCKdbwrBPcw4TD5K9iAgB-NIRw5NrRpU70NFZU_A7B8m-EGyNzGnjr8UuXcY22MR8ecupCymzq10EjLmiNnVB5JvV3IusKmynEgZkr7LdiM7KMlMOwjmICkCv1c1u3_qotWX6JY1KlYQTcqy5ikCK33K8KkZVfoidytUqMHA8TliAT4NKixkwfXfxKhQwKQF80gH_C9iaiX9lHAGGuSjrqK1m6k4rirw4BcV0sLWTC75vAZHXX5maImKejpdE5icmDJuQ1g0wOmT8ZRUjRSMLF8R982eFP901vATUYMtihMr4KkdfIvo3IK3eXXvyDtly2_iJRpy0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=oQhTwaMkYiq3fCKdbwrBPcw4TD5K9iAgB-NIRw5NrRpU70NFZU_A7B8m-EGyNzGnjr8UuXcY22MR8ecupCymzq10EjLmiNnVB5JvV3IusKmynEgZkr7LdiM7KMlMOwjmICkCv1c1u3_qotWX6JY1KlYQTcqy5ikCK33K8KkZVfoidytUqMHA8TliAT4NKixkwfXfxKhQwKQF80gH_C9iaiX9lHAGGuSjrqK1m6k4rirw4BcV0sLWTC75vAZHXX5maImKejpdE5icmDJuQ1g0wOmT8ZRUjRSMLF8R982eFP901vATUYMtihMr4KkdfIvo3IK3eXXvyDtly2_iJRpy0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاظمی وزیر آموزش و پرورش:
ما در آموزش و پرورش تمام هم و غم خودمون رو به کار خواهیم گرفت تا اقامه نماز کنیم در تمام مدارس کشور بدون استثنا.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72771" target="_blank">📅 15:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72770">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEFj4_ISWQqFoQNBfSnDn8ZY2OoTAFFEDzKxFmVyjj6Nlt2g_gSy1_GOA3c3A0Oo2aWWqxVwAluen1rg4Vd3PrNuxcosE5MS2r7bV_XpgBIX7pU_AqjiQsvv2R0NZlBDirw6qlXjysm_pBtMYXx9O1CRlJ9R23c3ipRov_n6g-MPRjnQ-RjPlz91UKqiJhIC2ncKxN9VhQT8vP0CvyBErxlkvg3YvHAAjqDrMaoUwtvTO7hsrED9h3jXSQzrU8Wyt6wVLUQdicl-qmqYXhe0SITcR8HnermtmZznD2TRcA9tDja_a26g1OI8HIGCFiClVEgL8CPA1t3Wc-_tp7IPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۱۱ مایل دریایی شمال «خصب» در عمان، از سوی سپاه پاسداران مورد خطاب قرار گرفت و به آن هشدار داده شد که در صورت عدم تغییر مسیر و بازگشت، هدف قرار خواهد گرفت.
نفتکش مذکور از این دستور پیروی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72770" target="_blank">📅 14:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72769">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruLEqmLAT63XHnkFbHFxpEl0bUTaBBAYRS1kjeYincZrWXOAucLi8n8K_pbIaJha1JTl4ibmiHkgNySNO8D131xx7auHpDLGIyq2Q4GBIDtOcQbYbNGVJo9uhw5AoK8dJ7PibBcBQi0LQvgYdesvYiOY5xVZIrUByUn2lBxqRQ_ZHqxMN6UQG2cPUL6_YSQJsUmNQ7vdwfKxNOYB4fq4EL2r5F4CetQxCUWFU9W-MrhU3MihDkcL-0afd__ffeXwgUQn2A5qasQUHhtdKLGyS0gdTmGUeBqf1jafTOiswRwEG1p4zdm8YL5WPG5_CIqUIa1WKscoFVOjfFhqN1062Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار در روسیه؛ قرنطینه نزدیک به ۲۰۰ نفر پس از مرگ کارمند مؤسسه ضدطاعون؛
در پی مرگ یک کارمند ۲۸ ساله مؤسسه تحقیقات ضدطاعون در منطقه ایرکوتسک، حدود ۱۹۷ نفر از افراد در تماس با او تحت مراقبت قرار گرفته‌اند و برخی مراکز درمانی نیز محدودیت‌های قرنطینه‌ای اعمال کرده‌اند.
با وجود انتشار گزارش هایی درباره نشت طاعون از آزمایشگاه، مقام‌های روسیه تاکنون ابتلا به طاعون یا وقوع حادثه آزمایشگاهی را تأیید نکرده‌اند و علت مرگ را ذات‌الریه با علت نامشخص اعلام کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72769" target="_blank">📅 13:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72768">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یکی از طرفداران پروپاقرص رونالدو:)))
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72768" target="_blank">📅 13:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72767">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مسلمانان در انگلیس با برگزاری تجمعی خواستار حکومت اسلامی در این کشور شدند.
جمهوری اسلامی بریتانیا!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72767" target="_blank">📅 13:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72766">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=DO91zJSwMnXBMKNETU57zMETrY-UeWhn-vSqKAJtK87ndIBrHV29GOuf9Yo91OldMEa6UjTdZJ03RP_t3HYH8RqELNTQxXJZqY5Kp_T0anyJlSvLC4o55g6FLdIZCse26RFRrAzwf-a7nSaVYVSitNpza5bY29YzO9rAxXSuhrPFwy9ZIfR8TkePQikwfibVcTuGfZgfjkJOzV59J7PBfyJawrTizHLo64Kq0q6dNb7naTDtTT8Gs1nEK2SMnH6RPRhNd4pcHXeSyOe_G719dSzdvD9_iSP1ArD-aIDEgh6efcS90UWKsGnky1-yO6ITTzp2_l5X4v3Xntw_sP3Q5i14EM618VT-W5Fa7ZgGmT0eYzyeDxK4Xq4qcA8VmWVAE7Zl2QONHmzcAzCcoY_c8-Tnw9SgFdowjVYrxsjwej2Z_21uvp1eqyoYZN8gDCEl_nB_20BXTst7qoZpnC-iU0ogQsMk9m7Ho-jpuCs7YhcE7yL6G_oUSH2wvVfNur1I4RsYAKfhiFxD9uETkMpdn-jCZFRmvk3hrszqOmRVznJjWaUyb5PLXHaOJQxXeSmaZf1YgFNlsm46sY4Gi7UfIfEWxyUcqTGSGPtjbANQXTSEPuDgsW8W_6mLvCvvQ0puWeH94xZPUpzSBy5E72LMkU2Sw5SdNr9D-hLJ7xjGuXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=DO91zJSwMnXBMKNETU57zMETrY-UeWhn-vSqKAJtK87ndIBrHV29GOuf9Yo91OldMEa6UjTdZJ03RP_t3HYH8RqELNTQxXJZqY5Kp_T0anyJlSvLC4o55g6FLdIZCse26RFRrAzwf-a7nSaVYVSitNpza5bY29YzO9rAxXSuhrPFwy9ZIfR8TkePQikwfibVcTuGfZgfjkJOzV59J7PBfyJawrTizHLo64Kq0q6dNb7naTDtTT8Gs1nEK2SMnH6RPRhNd4pcHXeSyOe_G719dSzdvD9_iSP1ArD-aIDEgh6efcS90UWKsGnky1-yO6ITTzp2_l5X4v3Xntw_sP3Q5i14EM618VT-W5Fa7ZgGmT0eYzyeDxK4Xq4qcA8VmWVAE7Zl2QONHmzcAzCcoY_c8-Tnw9SgFdowjVYrxsjwej2Z_21uvp1eqyoYZN8gDCEl_nB_20BXTst7qoZpnC-iU0ogQsMk9m7Ho-jpuCs7YhcE7yL6G_oUSH2wvVfNur1I4RsYAKfhiFxD9uETkMpdn-jCZFRmvk3hrszqOmRVznJjWaUyb5PLXHaOJQxXeSmaZf1YgFNlsm46sY4Gi7UfIfEWxyUcqTGSGPtjbANQXTSEPuDgsW8W_6mLvCvvQ0puWeH94xZPUpzSBy5E72LMkU2Sw5SdNr9D-hLJ7xjGuXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای دولتی یمن مورد حمایت عربستان سعودی اعلام کردند که کنترل تنگه باب‌المندب را به دست گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72766" target="_blank">📅 12:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72765">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG2kwf6atDELuq_AoMk1UOuc9DwsOH6Gk_U_tQ5gBf9d0z8RK7fTRHJFV5K4FTaqUj2TVePy9OLRa7ehF-V28vZ540kFnlHvBxnTyeSmORHGuHNoyZemfck-rbF0wYUrhf2x5L_j1DE_YXVhNvImMiVcFiIDADTBzpGHAIMNB0TouCb1vYZH15RgFBkVD0bbvynYl9OmUsm2lTIjnwES-8Fe2HAzCLkeP8Qd3jfHjoAs24iJLMVqTMCfvvgKrQpS5UXmI9hth8KjoPMhthuc-a8i2e89rTMqVMfAv8SuiSiedP54MnAPf_-VfaLh_dXjGrqHFBJEO-OLBsVTcASkEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72765" target="_blank">📅 11:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72761">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=Nj80fo5wof9bbRoqn_eLwL33fHg_KIwWBxfw1wo-86A_IHQdxuGIidLtl9Fcz8mBCEwbh7KU59I27MB1lemfunEfzRuME9LKb1cs0o9qkBiJsl_c92_ijQz4DeS5DXdDr0AMozcL1im8HLf25A4ZwgRWuEiP7f4gfLUV9GIymg50p3reO9R2aCjFTHATJvBmbM3zOaqDKEnRQaH3hIlK0_suQay5xDYpY4j3uOFM1pW7k8xDGV76-8PPYm_k3PVL41S4cXGUIbkRzl3M-IjVMTdh2Le1RB0UzAouOg_6MIWglVpgUswWB_H2IiqzSVbebYMYPD0-1bcPK2YoG6ZGKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=Nj80fo5wof9bbRoqn_eLwL33fHg_KIwWBxfw1wo-86A_IHQdxuGIidLtl9Fcz8mBCEwbh7KU59I27MB1lemfunEfzRuME9LKb1cs0o9qkBiJsl_c92_ijQz4DeS5DXdDr0AMozcL1im8HLf25A4ZwgRWuEiP7f4gfLUV9GIymg50p3reO9R2aCjFTHATJvBmbM3zOaqDKEnRQaH3hIlK0_suQay5xDYpY4j3uOFM1pW7k8xDGV76-8PPYm_k3PVL41S4cXGUIbkRzl3M-IjVMTdh2Le1RB0UzAouOg_6MIWglVpgUswWB_H2IiqzSVbebYMYPD0-1bcPK2YoG6ZGKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72761" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72760">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72760" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72759">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei8Oy0f74-KQ37cF6GIJ0_K7nledguun-TU-MKoSJKy_NHbWGqCPXrMAptFG0CnbgKtiI84HLPpBtvHOmS9Vv5JyyjsctxYAtjxWmztYi9JrlknXesKKCPbVOlzl-tsh56pX2FNywxfJX-e393FaGBfhz-J8990x9UAJiGvO4gzbYB2X6hl3unkowuCmHnZ1d6VJzlU8qE-r6NN3aPRRLnXK7z8NiV4ty4aoeUw5VmZhkKTZeISUv4mV-CrFFX5C_-6bfhBoiZx2zXaqivVRu3J2F3ke4CKAtv7h71lqeBNSaC37UwOEzXl1pe_gkJXIWgfYu8amnlxtzMgd-_oJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
فرانسه
ترکیه
🆚
ایتالیا
لهستان
🆚
بوسنی
سوئد
🆚
رومانی
نیوزیلند
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72759" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72758">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=SRRMIcwMMQcNgigPS66CfruTqkyWX88rt-_SD5vxy8vYqaOMXr1EWlLbdx5aL-HX5wkWMtIF2dHDNTXQFn9knwv6xylcvOQZ4onQbqUQj4baNpOhiGcK-6gUSeAn-i-2RxnabQ6maIlS3wXTXgkZld8hQEyh6SfTTqHBAO7Ri4_UfH35gmn-bWssKP4SiqsmerTOxAoIM4Uu0kYN9ei316cUwUWVcDgV4m3gTKS_6P5rcas71ztrvKCiBg0bq58jNNYDgCw36NuT7ZSsKEsaTLvdxT6GqM9SrfGUbIDt2FxsxIe9XUKER4JRzFryaxbZF9Zt9-eoc1hG-fmCkvHseQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=SRRMIcwMMQcNgigPS66CfruTqkyWX88rt-_SD5vxy8vYqaOMXr1EWlLbdx5aL-HX5wkWMtIF2dHDNTXQFn9knwv6xylcvOQZ4onQbqUQj4baNpOhiGcK-6gUSeAn-i-2RxnabQ6maIlS3wXTXgkZld8hQEyh6SfTTqHBAO7Ri4_UfH35gmn-bWssKP4SiqsmerTOxAoIM4Uu0kYN9ei316cUwUWVcDgV4m3gTKS_6P5rcas71ztrvKCiBg0bq58jNNYDgCw36NuT7ZSsKEsaTLvdxT6GqM9SrfGUbIDt2FxsxIe9XUKER4JRzFryaxbZF9Zt9-eoc1hG-fmCkvHseQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
جنگی که توی راهه، آخرین جنگ ترامپ با جمهوری اسلامی خواهد بود!
اما به قدری این جنگ شدید و گسترده‌اس، که جنگ ۱۲ و ۴۰ روزه، پیشش یه شوخیه!
شدت بمبارون‌ها خیلی شدیدتر خواهد بود، کشورای بیشتری درگیر میشن و این نبرد آخره!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72758" target="_blank">📅 11:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72757">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=ZVG0xAL-JCy4UKK-Ejir3XZPWmL4JnCkgVz9CpAI8GH3eqA7g6Jop0y4pGLDv_LpayMe0mmIegfuxjEMz6BRt1qqlAA3i2S3JVgMR0sMXxi-XlQ9ZdwYpGIX5xxHiSy8On8YV3ZGY-mqQW6w6GiXOS2tr6z1BMwWGEZxF6UNSM1yVLnURwdfjV-9F5jTmVg4tJKahQmwjyG6ky-SIAFESqNblZ77_Ex-75QwemyUQg_rLWU9O5gLlFyykE18ZyZjI6wW5JreFomJk9DZdKlBNkOhPcgVjvxzw79sqiKRqpdFeVnTpaJtVfQe-f8IBjEfj4tYBsfRjxhRmP7TWGkQQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=ZVG0xAL-JCy4UKK-Ejir3XZPWmL4JnCkgVz9CpAI8GH3eqA7g6Jop0y4pGLDv_LpayMe0mmIegfuxjEMz6BRt1qqlAA3i2S3JVgMR0sMXxi-XlQ9ZdwYpGIX5xxHiSy8On8YV3ZGY-mqQW6w6GiXOS2tr6z1BMwWGEZxF6UNSM1yVLnURwdfjV-9F5jTmVg4tJKahQmwjyG6ky-SIAFESqNblZ77_Ex-75QwemyUQg_rLWU9O5gLlFyykE18ZyZjI6wW5JreFomJk9DZdKlBNkOhPcgVjvxzw79sqiKRqpdFeVnTpaJtVfQe-f8IBjEfj4tYBsfRjxhRmP7TWGkQQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره یه دختر تن فروش: یه دفعه یه سید بهم گفت بیا رابطه داشته باشیم، فقط تو زود بیا چون ممکنه خانمم بیاد خونه.
رفتیم تو اتاق و شروع کرد صیغه خوندن، هر چی قرآن، آیت الکرسی، تابلو و کتاب دعا بود برعکس کرد و گفت زشته، گناه داره.
یه دفعه وسط عملیات زنش اومد، گفت سید زودباش درو باز کن خیس شدم زیر بارون، سیدم بهم گفت تو فقط چادر بنداز سرت شروع کن نماز خوندن.
خانمش اومد به سید گفت این کیه؟ برگشت گفت این خانم مسافر بود، اومد گفت نمازم داره قضا میشه، میتونم خونه شما بخونم؟ منم آوردمش نماز بخونه.
آخرشم خانمش بهم چایی داد و کلی پذیرایی کرد و رفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72757" target="_blank">📅 10:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72756">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=A-hX5Yre5t6ZXsVzalxvGG1UZN6wCwDUNUfLap0VbpHkmgJk2IhBoAwKamhrBwWc_d1QeO574oNlmZHQD8TKKJxAbxQoYGwDESSyilegdXrPqOoTc9V3l0fwmfv_ZUjsi1qDEZdxr0rwpTvUHK68NdzPy3PCL6iXVt9ueJFUsOI3OWdl0S8mpiuHzAC0aoG0_RzdV9KqAol1dqBHa6RpM4LFxg1cPBeQ-jOFKIlyU520oBHgfNEVjh6Ci08Mi2ZIc7kqs55X_5axUIrcicPw9_mC2pRYlSQkjBah9o4-mwnoUzy4fBfHLwqfBOqkdpe8-mdKq_bXE-ktJo-3Yq9PUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=A-hX5Yre5t6ZXsVzalxvGG1UZN6wCwDUNUfLap0VbpHkmgJk2IhBoAwKamhrBwWc_d1QeO574oNlmZHQD8TKKJxAbxQoYGwDESSyilegdXrPqOoTc9V3l0fwmfv_ZUjsi1qDEZdxr0rwpTvUHK68NdzPy3PCL6iXVt9ueJFUsOI3OWdl0S8mpiuHzAC0aoG0_RzdV9KqAol1dqBHa6RpM4LFxg1cPBeQ-jOFKIlyU520oBHgfNEVjh6Ci08Mi2ZIc7kqs55X_5axUIrcicPw9_mC2pRYlSQkjBah9o4-mwnoUzy4fBfHLwqfBOqkdpe8-mdKq_bXE-ktJo-3Yq9PUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه عراقی :
به حضرت عباس اگه بگن بین پسرات و جمهوری اسلامی یکیو حذف کن میگم بچه هامو حذف کنید تا فدای جمهوری اسلامی بشن
ایران از بچه هامم ارزش بیشتری داره
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72756" target="_blank">📅 10:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72755">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=Ilhr-itBxGYKSzouSeGBWb8AIgSbci3uFl7XhSGa8IsPcFc7UF94ra0LtwyHK1L5qzDzvb3ANcMwW5iai1ZPSPhs1MyurT5MwIGv6-j_D8LygYabv9Z-lPT1H_-W_k1dkJ6VkZ6gVtLYAuAtCZ-psjYreCJhBFtdXkSEVzDNhjLvW4dQjDYURLlMOS8eufKTTZOuExug4UGC5O-hqO5lF-CQTkkATBKkNCMJvqJAKjU9sItHGsfNwFpcIROz_S99aqT4SHHGFr_j0pe_rbjhBhrEec_0eUEKL39nbMOfCuyeTu1Iou7EicByjZVXMODMazwv15SC1MKDzrIhwgtG4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=Ilhr-itBxGYKSzouSeGBWb8AIgSbci3uFl7XhSGa8IsPcFc7UF94ra0LtwyHK1L5qzDzvb3ANcMwW5iai1ZPSPhs1MyurT5MwIGv6-j_D8LygYabv9Z-lPT1H_-W_k1dkJ6VkZ6gVtLYAuAtCZ-psjYreCJhBFtdXkSEVzDNhjLvW4dQjDYURLlMOS8eufKTTZOuExug4UGC5O-hqO5lF-CQTkkATBKkNCMJvqJAKjU9sItHGsfNwFpcIROz_S99aqT4SHHGFr_j0pe_rbjhBhrEec_0eUEKL39nbMOfCuyeTu1Iou7EicByjZVXMODMazwv15SC1MKDzrIhwgtG4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار :
از آقا مجتبی (خامنه‌ای) چخبر؟
حداد عادل پدر زنِ مجتبی خامنه‌ای :
سلام میرسونن...انشاالله خوبن...همیشه...خوبن الحمدالله
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72755" target="_blank">📅 09:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72754">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e173a359.mp4?token=tFSTov2rq5vtyI_8w-_0umTmGPxhGYETzneZkfK4EKIuRTBbg59UwHy5tCDa8L_toXEI2jkKTPJ3rMp9ftCfBb16hM9hVpbC__BKcbFd6MekZmVI0RkUxIY-HUjJnl9lgGWc3OhWmC-4Kgqa5qQmmwbobKiu5wPtdL2TsE-WgTEgqC6Y8JC5JdsIAbyYBduPgu3fNqr6zyI7lNpkoAjQ6F6F-L4iS4kLfUk6Gihw_lyFRcNMXaaQ5VIdfdUzhUemD4BK5XHHp7vgPrkeSbnhW2LXuAgQgSDLLe7UFIq90WslRGKc8QNDcXNswhzm8nVWYmAWWG-gg_iLs7nLyiBq8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e173a359.mp4?token=tFSTov2rq5vtyI_8w-_0umTmGPxhGYETzneZkfK4EKIuRTBbg59UwHy5tCDa8L_toXEI2jkKTPJ3rMp9ftCfBb16hM9hVpbC__BKcbFd6MekZmVI0RkUxIY-HUjJnl9lgGWc3OhWmC-4Kgqa5qQmmwbobKiu5wPtdL2TsE-WgTEgqC6Y8JC5JdsIAbyYBduPgu3fNqr6zyI7lNpkoAjQ6F6F-L4iS4kLfUk6Gihw_lyFRcNMXaaQ5VIdfdUzhUemD4BK5XHHp7vgPrkeSbnhW2LXuAgQgSDLLe7UFIq90WslRGKc8QNDcXNswhzm8nVWYmAWWG-gg_iLs7nLyiBq8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حاشیه ختم خواهر عباس عراقچی، وزیر اقتصاد از پاسخگویی درباره وضعیت فروپاشی اقتصادی و کاهش ارزش ریال فرار کرد و خبرنگاران را به همتی، رئیس بانک مرکزی، حواله داد و همتی هم بدون پاسخگویی فرار کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72754" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72753">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72753" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72753" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
