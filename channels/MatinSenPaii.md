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
<img src="https://cdn1.telesco.pe/file/vU5VBi6Vxc0TJD6VpfaLGizVzQ6QRoq4HkawTMzQqhez5dwrQT4-1jgU_A2g07qP8WmaVsHdCxeexd-vJnazvnVP9kooGvABSpah4BpkTcEKDd0MEJqtcfHtOSX75DezlCe04eEphTOGrW0vlFXB0rW3PgrL2aWQAtPxnGXT_GqlA9ksgvS2Sos_Xf0rVSHlkwp5j8Jh4Ev2RK3jN2tmfWtOdSCUCMWnE1IGH9jwTIlLFicIQcz-qpQZl-_CQ0KyrWBQTsYkf2oT_3wxXLdnZ0lWU1lmXJqU2gVKJ6j5xQWwyQ--vzoQan4GzSx6ywbuKCjkCQOW9sVUEWb7Ipc0vQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 03:51:05</div>
<hr>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=b0y_PlyINNO48-OwcCZ7EqvlskMV7lAhPqL0gE1K0nXPLsz2p0wfEI1WNWOITwpehj5sos5ZL39xyTpymSItf0hUR29s9uQmvWR5rphB7wXkZqW851cdeIlwSEKLoUPFQDzZONPxsZVoBjQ5Hb60xOwxUMvNcmhFfLMYlFDb7yeQWUoYqxqhJ2pZkHZqY4hK6sXR5INqsX6RvAWAMLyX9ipdGi9EtK_pHc-LJ11_EQosnb8J9QdKRHruHA3lmgggEJY6KEmT6UH3zNmmwJ_9jtyS5_gkhD7_o7c3Jd9pPfmoJV2ocSvJlNkfHVm_cwL_LL6RhSpiOj6ExKydPO2ySg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=b0y_PlyINNO48-OwcCZ7EqvlskMV7lAhPqL0gE1K0nXPLsz2p0wfEI1WNWOITwpehj5sos5ZL39xyTpymSItf0hUR29s9uQmvWR5rphB7wXkZqW851cdeIlwSEKLoUPFQDzZONPxsZVoBjQ5Hb60xOwxUMvNcmhFfLMYlFDb7yeQWUoYqxqhJ2pZkHZqY4hK6sXR5INqsX6RvAWAMLyX9ipdGi9EtK_pHc-LJ11_EQosnb8J9QdKRHruHA3lmgggEJY6KEmT6UH3zNmmwJ_9jtyS5_gkhD7_o7c3Jd9pPfmoJV2ocSvJlNkfHVm_cwL_LL6RhSpiOj6ExKydPO2ySg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=VqgBU5RsQzwI9xHnoGAa9SSgan43qLVT5JFhym3HYPQVl7psAn3ZxYbn7HQgM4iqv16CRR3Bo9e9Hz_Oi6v1XCPtTplHFyGq6RK17BdP_55AZ7O3SJB7dqo8zsJ56CyknKJo0vDuBQ7YjpBgJyqowF93y2JmGLPlQMPJuCYmTAXah4J94BTnqtxKJG18DW6_km2Pq4nPbD86m4MPiZVJ51Un--2iSNhOxZeUUDUljzuoBblSrlSPBxAL3TSpgyU2BHhqV3elgnp-g1Ey_YJDcLq3wlsPFPj6OUxcBySDOvIMuFBVCONL_BJL4yflXX6k7ppScGTtw-PtQvPyD-zCmg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=VqgBU5RsQzwI9xHnoGAa9SSgan43qLVT5JFhym3HYPQVl7psAn3ZxYbn7HQgM4iqv16CRR3Bo9e9Hz_Oi6v1XCPtTplHFyGq6RK17BdP_55AZ7O3SJB7dqo8zsJ56CyknKJo0vDuBQ7YjpBgJyqowF93y2JmGLPlQMPJuCYmTAXah4J94BTnqtxKJG18DW6_km2Pq4nPbD86m4MPiZVJ51Un--2iSNhOxZeUUDUljzuoBblSrlSPBxAL3TSpgyU2BHhqV3elgnp-g1Ey_YJDcLq3wlsPFPj6OUxcBySDOvIMuFBVCONL_BJL4yflXX6k7ppScGTtw-PtQvPyD-zCmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LpE3HCYYI_nwwN4QHCMF6pKuCZzFC7QJHZkgXIXilsdU6mgfF02n7bGvl8Nb0UcwJvDDd3_93xqnlck3csfzmyjV_nUTVKfHBinbT1Z5_OAIV_s0my8v11AhfDMqZt4tP9Cl8poYaszg27f75qEFwqqQ9fnHWTiCECv9IlPk6R1sqjhnVR4AfRBlSyRxWyN68ifFNQPRhvJzevOdYmeDwY1RiWp0P6tx_I8Bswm3dxYZohF59iKVtKIMN3is1bC9-Ckv4zE9HsNNQyGIIZjn7SwFCMMlTxiNm8HoD8vU19Wo5ixUcanwQh56vEl5o6xD_Xj7pxO1RNWSUGGBhTw3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NpHqsou8aew2G65GE9KYDugGQgegotTzywY718T5cTJ0FLRbgoNipzO5BLFZfFn-p6AkBR_4iT0iYo83FDUJ-c9fvCSG7oQaVrA5vNQk24LgwS5H2YWhrx7voKwgx3qWLCWVMMRtHWDo1-BEGKNvb773Q0xECqOmIK9XriSWIqvS0wIKs2aThYlIAdKn0gHNzUpa0IbPRPEww-1-XxMLLHn4NMMckx2vF-wfgUlv8acxJhkdchIt2_bS5cX_4Ll6CSAmFi99Q-nQmLEAGXHmu_LqWaRqWHO6p9qaYKSI3jANoPPQPGj6UB4ry29wl_YUNM5FxXKT09Q4U7PZgn5How.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L7uvXbLWO5PZMepn7dno06Elo1a1zSU-riikaqfNuSSXjUCEvhq3T9fSezz9h6MmaUVtOkU3korG4SukmD2m2pJudhvWFJkK7-Df4udX4DKw-9r-HiLvG_Nb6QCFBEAZGVuY1kCPgpBvCYZ8CmrAqND4UurATUgdfSLonOU41Y-xgrioLyuIjkNS75fvzCpWadZelGEYI-qk9zIipF7FnbrxFhrtfsm1J5xGpUS4yZkXjnbzF7wEzn_qoVAIuuLQwPDCNWJS_f8CosoLZn64E02Wamq6nflhYMn18K003nLpEy8VsHJl8W-ll0tJXtSe2W4FUlf83DWreC1bqxy05Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LkVwqPrWHjyVhflEFeUcyBEDA8pzID-6exdLktzicU5h_qL62QV64lRh9c_ZOQosHEdWQJ_fYgGwOXoZ_aJLBOr9jR8szeXYMJNsWlwLWqULunO2gXOpuYEimOmwNsJ9KZgk2W8prHMhQbxqkruTrQY3F4oAY_p9U4DkXwLB6wtbk08-dthf4CniVZ8WrC-wuMRLbahtyCfK4Zk0J_6XL3In1cFK3lBHSOywVB7AKRlO6vul4ALcgynnKFMJRf-v3s7dF4HRC9tqjNvQh5qyEVxeGa6-EH06iqo565F7ZEIB6Es3r7GxJLWrJh7786A62vmiaSG3B3bSL77kY-pbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ Hermes، ایجنتِ دوست‌داشتنی ما، نسخه v0.20.0 منتشر شد!
📊
این نسخه که بهش "The Herald Release" می‌گن، کلی قابلیت باحال مثل ارتباط صوتی زنده، سرچ با منبع معتبر، وب‌هووک، اتصال ایجنت به ایجنت و بهبودهای شدید پرفورمنسی داره
🩰
تغییرات و ویژگی‌های اصلی این آپدیت:
1- گفتگوی صوتی زنده (Talk to Hermes): پشتیبانی از استریم صوتی زنده با قابلیت قطع کردن حرف ایجنت (Interruption) و کلیدواژه‌ای که باهاش بیدار میشه (Wake-phrase).
🎙
2- منابع و استنادات دقیق (Cited sources): توی کارهای پژوهشی تمام ادعاها رو با منابع واقعی و مستندات و سیستم راستی‌آزمایی (Fact-check) لینک می‌کنه.
📚
3- وب‌هووک‌های خروجی (Outbound webhooks): فرستادن اطلاعات و رویدادهای چرخه‌ی حیات ایجنت به HTTP Endpoint‌های خودتون به صورت امضا شده و امن.
🔗
4- ارتباط ایجنت به ایجنت (Agent to agent): پشتیبانی از پلاگین R2A v1.0 برای شناسایی و واگذاری کارها بین ایجنت‌های مختلف.
🤖
5- سرعت به‌شدت بالاتر (Faster everywhere): سرعت لود اولین توکن (First-token) تا ۸۰٪ کاهش پیدا کرده و پرفورمنس اپ دسکتاپ به ۶۰ فریم رسیده.
⚡️
6- پلتفرم دسکتاپ: قابلیت پیش‌نمایش زنده آرتیفکت‌ها، کیت توسعه پلاگین (Plugin SDK) به همراه تسک‌بورد Kanban و پنجره دسترسی سریع به دسکتاپ اضافه شدن.
💻
7- تاییدهای هوشمند (Smart approvals): پیشنهاد تایید دستورات ترمینال بر اساس تاریخچه استفاده و قطع‌کننده هوشمند برای لوپ‌های ریجکت شدن متوالی.
🛡
8- قدرت‌نمایی در CLI: اضافه شدن ابزارهای اسکن پروژه، مهاجرت ساده و اجرای مستقیم کدهای شل.
🛠
9- هدایت بهتر ایجنت وسط اجرای کار: قابلیت اصلاح مسیر و دادن دستور به ایجنت وسط کار بدون اینکه پیشرفت قبلیش خراب بشه. نسخه‌ی قدرتمندتر Steer که داشتیمش
🧭
10- ابزارهای خودترمیم: توانایی خواندن خروجی‌های نصفه‌کاره ترمینال، تشخیص خودکار خطاها و بالا رفتن محدودیت تعداد تلاش‌ها.
🧹
11- اتصالات جدید: هماهنگی کامل با پلتفرم‌ها و مدل‌های خفن جدید مثل Buzz, GPT-5.6, Claude Opus 5, Gemini 3.1 Pro, Grok-4.5 و  Vercel AI Gateway و رفع باگ‌هایی که داشتن
12- قابلیت‌های جانبی: پسورد Vault داخلی، فشرده‌سازی خودکار سشن‌ها، لوکال عربی، فایروال و مقاوم‌سازی امنیتی روی ویندوز اضافه شدن
🌐
این دستور رو توی ترمینال بزنید، آپدیت میشه:
hermes update
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O2IAkGQ3ZKy_fMPMQWPHrvOZJx7Bync8-f1xN1NXC_V-tt7yLfyEDdF483Wfa2jjZAHYa6nm89h_drlF2vtKguCdYi0hMDOuJsfsasDKPIkeVKyMBA6tQml_2TmgeBsR27jPFqPF7h0CgbHtru1TR9FDSzmwSK8T75uZYKKXnNz8Kp5bmNOyzyh-q6TTFT6W5nlMFLCn6bVXpcHKAAaF2_0co_llKWI5DGFxS8Tz4PixE_BHWnnpn7toQd5PH3Mv-0i2L_wPAmQtNcFNtv1U7eGCJR9B-ryWSf82kzcwTO0R5_G9RAFA2ms7DTzILsJnigrmbUu6nL5JxLuPb8_oWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GAHgtavKbw5frJ4eN7KSlHG7XSkLKqrI7XNR4MauTNwZxTWHaGJcZ5r6ySvKrUrOynf-_knneTgt2xMmAS_f7bGW_L6aI7jAoGSHi4MJuzIGoU05OCvMBbDH0HYDYoTFuxjToA3NHivwHlI1Modxls_X1c5bctMx3hzRROEPjlPDscNmEQZ7NkK43QRYQaifT2wUAtlzILEV5hgazHgr1uGva3BT9YhMOz1tx6E0bTXCO-hX2ux__ZBS4YuxtPyT8b9qlwlKK3WDfOeg49dyvXzFgY5xVGWoYy0QRWrA7S3wFH2-f1FF0YujvrdO746IUGhNALTEx0FaO86unbjqfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eQDq8eaH01vgZx0PNKE-hQIUX2o1bniu3kzXEcbeV2c-zLBi_QmzCrbz8PUaBy_QIixby3bR4mPq9qJi3U2pyr00wakIH4RdBRHwVDZlQv2pSSNtRZQ23HvGBvTOS9Y1rjjXBoE_Jhg662wzfzqj9lc12Fppmi6nVqQDFshPmHqB63Ufq0ZL4LsEfPPVlKdh6QHx0wrY92rXzGHzzFs0AIjBalStNNQvLHJHq3OOhYl0XTCDvFx-TW11EtFacrMjm3J_wECg-AhkU3S3w8CbA30i7bCRZUpQ7piOIsTyYm1AEiorwbtqrWjmd8_RLD7hy5jk0HPUK2xi22wdLwKI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b8w6i8pYGdj43WrBObPoyQ9bQ5GElu81kdHUkqjWvyDcLnfu_30XJSnNnxGxM3aX-DoXDfrObcQe3ObmqLYoItZ6vsnofqWrEIHhpCCGS1wfL0pN1jRdYZNn95rIRKLbYuHpSudu0OJP4cWTui-5ImYj-WqZ2-ypX2Qb6h1EjjvmTufX6eUADNGo2_6IOdwEtjuXDRpBMMPMNjbpWc_q0YwCXfTXc2yGNNN1n2wsPd3NOyVHdxyYSCOIDIxTKIKnN8s-o2KYpw66aWpWvcrG81YQWiCQaJjW68cEs3OXKtXfi9TFu2p32FQSdn9bcWyXJkwt-d-aFvyPTghbQUp_EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vM36vZ74vs9oEHuFIcx00uxsu2ZRoWjYAmItoGNijd6Gs2YIfRnabEkvre2fA2oXq-ZxOQguo0B5DsW1rvVzJqHkwAJ7ZKw-UlkqyVOkcF7KpmbebxFMXOFlmbNoKoe8kQxoIN8a45hvZLn-Fknkc6AlSB6fyn3pFVp9YGUswM2VP299SQDmDJ_-g7Kb-ndw3QqaXHQzLwpJqK9oMlhnrCLeYPFCzrh-1cdapVTyk7ApAkWupCQQrHTWqixSxSF5zD51HzhZnJLllVzQGz73QAg_wj6h1yhqnB7rQ4M0anFbg9mvpdcIk2f1OIzNixxvYrYU3HlB4nvWjnjN4PYylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nTltMZMMdKIUaJdMWxzcKQmYAB4whmalDDxlkOkR8vbcAwoU0oiazaM8u-FnRtggUFkqOx6dTNnz6wz_8EnKaZ6H-nO8HW1wkuO8pLGwcYCXI9FHaxyS4BeTmCstMIIUNK2woZF59BNOnMkwB4JTYpRP4Hw0YiNoRuWEodtzfEEuPe77cDwWFm7I_yTIMUoOMmAltxL2BgIvGNxJSFJxLIsB5hawvkQy7CDHWcY75j3f20O55Pp_Xvb5nrtZuxWR4suulyBGZwOhtcoAvWhE4_6WT3fG9bsoA_UvSCKXEs9IdLQ1N8FJTSUeFaTc7QaMp5plRXNF1aMFj4bOZj5dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sW84-cR7ZGFF_W39dWNTLFSgXTxGxC6nERxoxgNJQJxgLcUtq05zRiu-F2xKdZPNzI-Z-79kMaj4etdwRbUWujQ6gRDutWjJmt_5NuN2ve879W4LSe6w961BSxgrJnxg1W0HcnZ530UaEraps4eq0d8xvuTbXizWIrvpLiTlWVzEzCAIn2c-ZgKsbTdXegmi8R-7M1WLQSlZ84ucA3dCl5i61ePST6jLoUkLFsuHOwcsa-2_mevphAksiDW0bV9RxYg1-ph6F7BgdFzb5cld136AJjPotSAGR-vEtLmQlJB3SXAufunV7RBRFa0A4cZmuYWe4T38ZwOLyMbLm26rDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ODQCgAWDMU9PzymXE-Cq6qKNfCZc3TcA7xC1NkeENJdvp51V_kCKwhbLEvD53uzBHfBzEyiq_O_fKj92qG3b_g_1ECOHbZdkJupOhw2c9DXvcNVjtggmSV3Ep0Wy-RThj7NJEFR8uZfen_DUnxuiiKyEnyEWYAKrHDBwNDVyhhAeZoE-3AvU9TkFLSsDANmB3_jbwpCIe5yBoHigeUKMfdJITvhuPtVAd9Y7s4dD7p0g8TzC2SSxoF8HDyk198pkffLy8dD002yaTuxk5btN_TBs8bF1evG7UHEkN0ZeG41IGcknoxFhyiJEmFtwa6JkdRTqNT3hdcd_tW5tFZVjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cp3XdZZjq2ye9ZGnNpOtcpDf9O7fCtIKLLCIB-c3CWGl46Yiff_XaWQuqZ9axGHj6XOJL9zJaIhv89-Vwb21RzT4ZfaWfr2ZQ0KGiJBH6xcn6hvdUL58aN_KrHaMNz2W4MhwHc83-l8xbDMpZa0Je38XcFCLCcXyvE71j6kWJ_7ZdfrhTpCvEdiehYckAgWtREo5KL0qYCSXZCu7FGdPhg6EmzPZXTI7GcpuhFjTjskaB7xPbaXA_rPu6z1DBJolh_Jg7AVTqHYmQKuK9ihsrXi341YMNePNLVM-kfaD1fqXJN5t2mDRwB1Wj8ltLB9U0PhiF7VHW5J7C3-rvOVaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RnFnggmUDTINS1JXh6rBA6-ON_b-Deu4Byx0F73GpQnRDczoar4FI2ZbmGijov1XljigPfBcKdqrq6IkqCfiHdF5kug3mzWYygz6tglN4LwelTKV26a35wmNIaCO6vZWcrEBGxMZGelshwQh2-h6Qv9guqr0xX5RqRiYsI1cWQXARiA1WPl0KMp-ThpFPtEL-wb5nRx2N-IsC3rVwoWNCfv4xUaeRImpzhrew2aHKgNwRPrtTVLJftOA_2hgv6MOZkGojKx9Q9RoZIJylqq4ATEbmAiNL3B3vKnvfXc_CWrGqqRK7t4_Rb0GI68S6dLlbE24CeXY65ryNi_hkA3sRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RHDBMmQ1tNwz0swSnrE_wfwEACTaTKFo3PrjXW-lfnvLYuI1qD1r8l_N7ApTLvLLLHqohbEpwkXi-qI9TwjCjkmRCvY7HhrlMQXbVEueN2FtGi-4vszkRhY15TdeHk7bV7IkQ0i6dbsOiBKE3DEkecIDBypix9OuDf4zF3zq2_EHHbuBXVOE9xPa4FJCcoB3V9ZSgRanCjtNQr1rm_cwwOSWOcT4yEB3dbYJol-LQCuSRTsgxGlgX28OJzGYFmk2jc4RUqrSNMM3z0jYDdv7IrODrahb-AyxQDqjn2HRBnuVl2ubObfySlPVKNreTuJvHGDZrGjmji9CCMtZhXKWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pLt9KK9G1aUrYrQ54HNX06zSy3Q3vWX2ztb1FzZw2fJ_8IFTXFzf8h7_9R-2XsnxCtlmkwySlbmZBLaL3zLyFYNperBo_nFTE5yh_EzeB4UzMteXRPkGTOsNxQKZBkIO0-cH_DjBU01H205gYkegiLRskfxI2isPYohEErSDw_B4eAvlVEBV1TWzCHbiJ_YXqnSaHUZDRV8WOWxf0l5GKQ59d4PE0QYeCZBm9MQkuHSD9Iu3Soto4kaKcvtTygKrTjTK60jIlDg334qj0JDWV3iCDuwYg8BvbUxxTD5YScVFfEyEsKXklz_BXt_SJ7H-rqHEDpS1XfrW_28gYwIqPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZtVQQPd8YtTAUvb_fHGXoWqFkLNcxNYsgBr3XbBzT1kVksUTbJem1ExUUwfd3pYqQlH7wnTOSlBD3YtgkPSJqRJ8eXjhhnQYnN92hOX2CxQgITfO5Aa4KvhHY_mHy__ItsrDVK_j8HCd5BmfZTkzntOoe50qJBI0_LGb8tlLJTApRSKD_LmpWBVCjzUwqis4P4yKlE8d0lAV0_NbjVr9orxOoDaEBZuz6e4IShTAPTKFakP3l_sPxYoOHhHqHH1kWH1KsYdh14Q70DJd0Ih5gIih1jAH2sUpa9XCp3rt9uuQyb8a4EUmYlhGCC24fwg9hSblcthKsK50GRJccAGcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nLG4F3Ri0rH27Fx5S9cV_lf1JXfHGHYIevN2XuVckOgJ51Aznc9uzzYp9V_5OEemb_4YY2HjFG6OEJl8APcytSEuav1rixgsSch_HfGfT4dY71wBZMizDUu9M4ge4sUtCpZ7gD7Wekmsur4suR_r9F_fS6pdL10Dkl01M3ksSDJFwP8rTpBTgvxrRlCYR4AOaFs0f-JFgc9n1DIUBUT9_m49YKLF5v2v05nbSf7wBAhmoNOIVw7JaqYn3ogGexSHvXvsMocUyyU4O6jZsnu253zzakg8UQLiUGg2GRgsnLEIztTGb83ulnBEWvyzx_nxYDXwr-sDdrQaefPmL-cS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OzoXYQ88GygFtzCL7VQTZRPiGYe8FRSHcwDtz46u4tuzatDakEZzFPAL3M5ghap7ljJP3S3xPmUXD2zup4J0XXcFIKnbg6lmKL8Qocc62eteRYNWcvhIY_mOrdAti6IO_O4Iud0xlbVvIIZNiH3zvO4vdvQDzMD82M5pVGb4rVLhW-4tLqlKyVr26dhhbLii_MXxGrkC8nDp6TMsfIDeZiFf2rXqRYdbIurmTYtGZO4PktSz5QsBCPSefV2eSRhKARF-bwryJWvfTy7quCKr0-M1BQoGZwkGk2sdvgDnDI6POvvTuBwgErr_8zodN2xuMZw7i0Ymsfer0-bhyCjDeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbfnOsenKJLFwN_CTCl-elrilOlEjx5IWrpv5C7XParWTFoL19Uzas6kui4paSY3UGGTeZ2voORgvhP-hkEWGCjeZXrZzt2ngewKCaBgGtvlKU0mOSERlHHo8UAxcWUqf6rP_vanoTbJw7GSRUO8EVPGtwQ7URLzd7Z0tBDcckPdzjIENAYdd-nZIH1gS8YN-09M8u4Vy7ltH6ONzPiYsn5mcZiV3FE7_wew5npcbhMQTJCNqBAm-qqdz4xqulk6sNIhMluPxTqh1NcBd_37vXtvpN-zY-cCbQqKDgxcVLlKd_6NE5t2hz4l_R55YXivCIA3la8VFALlTPVG2mowHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
The 2026 International Olympiad in
Artificial Intelligence
starts today.
As a token of support for those who will reinvent our civilization, we'll issue
🏆
240
exclusive
Intelligence Cups
to the winners.
💵
We guarantee minimum buyback prices ($
1,000
per
Gold Cup
, etc.), but the cups' limited supply may make them worth much more on the secondary market.
Good luck, AI coders!
🍀</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ticu1C6E5FWIYQ9xUFgFHdeAXjpHf5G_5jjI2GjvX6yR7kztghymJs0u5-KbcQHMLDh_qTPTGULIaq-3DOwrCNvZMggWbN-RcOiMaSYHcV8YeD6S1W9lEjWTBrsEHyPiCs5Xf0OMSanQ2JhdMFkeIlO2bhI_L1acjpjEJAbtp0ON2Gscl1Koue-xuLZPdHn_icDYgI3qYBNZRNS4jDpo8yRX_qWjjNL5T0T7z5tf0FL_6aopnoM4HqX5WflpE1e8zQgENjP5MfumT6O5sBNEcx34Y9UpDdYq_klICDBCTJlSARSs9XCwtX9fRLzt2Z2mB5x0tLsbA4JI2FNgpqWQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/id8Mw52Fff1ZQ9YN5mRqN9JbLfWraykUWY7qv1qTr5BYhfal9TYAQsd_MdHwEk5SkPSge6IsBmwgzNjofRs6q24xkvSTUZxQ4NtcNuksZ2FrSdsRjb7qb4lPjgkQSyZkLDsTAyFYO1zGhpST_jWcGtIhLj4uGIC0vzdbYcLkOFwqEz40BZfZYhy7oGPlkgf7IOlBhRGehXLpCN9ABHY0QCrppLwuCTQPj0NmL5V6E0bLgvko9KffSu7xy6jcFTE3JXGHtA1Fq7-SIJ0lKX197QK2P5_qaSGyI516k3PvoWrLjFdFlu43STUKCYH_jhBpnE2QyUet0M0Xu2qtVisGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=RllP1tQ4tnvK5l4s8_OK6EjxCCAIjPCjiY5TS3TA0X7bswghfxDG_wGWjR1xWgsi5K3QNf1tdLmLvbkqnCkVx6_TROo-MsK4Zw_NskFbv7WigecvZf-JlMCWilzWqFYxP0y82LggKRI67R-xj8ufkMnWMHZJw3GrF4fXO8fcyeQuz6QS3qoKQLfoShNGRz5U8DSSEHlrVmRwwLwPzA2umSAKCSwYd30U-0RMCSCAm2JSwB93z7XA67EueztXZhxACvCU-Casa8KgCnHtqx7DLbTAQd2xAVZA93Bo80vGQ95YMmY-635yt43099fzTtyOjdlzM9Xy4dSjVttgE0Q-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=RllP1tQ4tnvK5l4s8_OK6EjxCCAIjPCjiY5TS3TA0X7bswghfxDG_wGWjR1xWgsi5K3QNf1tdLmLvbkqnCkVx6_TROo-MsK4Zw_NskFbv7WigecvZf-JlMCWilzWqFYxP0y82LggKRI67R-xj8ufkMnWMHZJw3GrF4fXO8fcyeQuz6QS3qoKQLfoShNGRz5U8DSSEHlrVmRwwLwPzA2umSAKCSwYd30U-0RMCSCAm2JSwB93z7XA67EueztXZhxACvCU-Casa8KgCnHtqx7DLbTAQd2xAVZA93Bo80vGQ95YMmY-635yt43099fzTtyOjdlzM9Xy4dSjVttgE0Q-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش
سا
خت کانفیگ Amnezia VPN(وارپ)
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
💡
نکته:روی تمام اپراتور ها متصله هست.
لینک ابزار(ساخت کانفیگ):
👇
https://darknessshade.github.io/Amnezia-VPN-Config/
دانلود اپلیکیشن ios
دانلود اپلیکیشن اندروید
@xsfilterrnet
👑
@ConfigWireguard
✅</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W_ElIMQTT7oWw-EJWMLcWGoRwq-h9WihjMujkwLwu6gNQC0r6EbLn8ezthmbM-Ftv0vNdFXilrFFFPFnAqShu4IqIe5jcxC_jxshzm282rJTnGziN560cgqT7s-RDEaKhXoeeA15uSTPnzCaA4osMBQrXTQbGayBmc8GRGTHB74Xi2i6WH-l-aGPmVsoXm8IVF1T4K-5c3XRhRB1qCX8518dG_M-77shBymwCnjfq7QCaGTVkn_zDcyKZj7JCuvYCBI--mPRDtP5Fi5_KYw-P_aoNfyf_pqBnT6uuKuz78lUYZyPulw9qfKLE2G1CASI0k3KlY6mAOY0aqzfMbzTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EAvSL8z4NNu4Nre-0xuIFlHF_58mszIO8i4w2Px8ULQLc847JBGK9u7_wMxtBk1x0XEUs0pyId2ttlfzjhYRyrCPFYcIxXY6TJP6085wM6NvBF-WRqG4Z3mFseOvXhrxgCzAHBLNp_JjxdM_AEZb8uOdOmlUtarZWaMAkNdseYLyzJEDxsI4tchO-M186Ayj2XCAE-yM-rNrnPMoY-hEXgT9-VbmOCvjrjqgoW6MIE0tlBDnQgtC3PlhdZDNKZP-ImMCDvyJhQmjXqtYyX--cgGeSthSbwXFDu8omSEaC0S_RJTHO6RGz4OsFKJj7kPjhF74XC_LgBaVRPBIj0woxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)
بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.
مهم‌ترین تغییرات:
🖥
یک GUI کامل دسکتاپ برای Windows، Linux و macOS
📱
اندروید از نو بازطراحی شده؛ Kotlin + Jetpack Compose + Material 3، پشتیبانی از اندروید 7 به بالا، APK جدا برای ARM64/ARM32/Universal
⚡️
دیگه لازم نیست منتظر پایان اسکن بمونید — هر وقت IP سبز کافی پیدا شد، متوقفش کنید و فقط از همون‌ها تست سرعت بگیرید!
📋
امکان کپی نتایج (همه IPهای سبز، ۲۰ تای برتر یا یک endpoint خاص) حتی وقتی اسکن هنوز در حال اجراست
🔎
اسکن همسایه (Neighbor Scan) دیگه اختیاریه و به‌صورت پیش‌فرض خاموشه
🌐
تشخیص ISP و ASN چندمرحله‌ای با چند منبع (Cloudflare، IPWhois، IPinfo، Team Cymru + دیتابیس داخلی رنج‌های ایران)
🛡
اعتبارسنجی واقعی کانفیگ‌ها با هسته Xray؛ پشتیبانی از VLESS، Trojan و VMess
📦
خروجی مستقیم به IP:Port خام، Share URL، Base64 Subscription، Sing-box JSON و Clash YAML
🧠
موتور اسکن بهتر: الگوریتم weighted-random برای رنج‌های Cloudflare، جلوگیری از IP تکراری، پشتیبانی چندپورتی، خواندن ورودی از IP/CSV/CIDR
جزئیات کامل و دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYDtQ8nAomnFa_5fQ-s-YQl7oDoL9MakllGduBSd57O9X7SeskHQYYFED1aLhmf0mQ8mKSElM7qVuBT82tBCP6Z7ulxL8csqPPnOSXWdxWyFL2-krLj5RSKoc8M-IkI6_SV_FFbx61o7MFzY4csIKT4iZf6yuYoI9LkV8RWteCYRFTiaVYYfOlVn60AtzThBfv2KN3lvOftu330dMJkfKYmkzY0ZQR-djNX_ahvVOrFvWTBkD_RwLb92Nfbsh9GGWYHVZ6VLWOtiDYoJfJc1MbkJMBI6Nyc_mykv8HcGAOzhJ2m269yyEfYobM5RhhLo0J4OgC8O8-M7_KdJ9X0PfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pZrzUSV1o0fltalBeOL95SYwmrz0YCX778FPGLQR2hbtGPye5wZtBf7LyA1WxrrP55mOgaq_noIg6nuuSEn-QgGUM51YN2efE9VMDjzPGiJSK5Rv-yaCg_OQNK9N7er4IKpFJCBJCci6lt7x-LWHOmaDYZbruvhUfChox0pSRcuGa3qNw94tZH83BIJ9QR1Mg6yGuF52l2jiV8nIGlwzlcFMNb3HNhKrQJ6mBh95pTSr66crLbV87Y2cMXHnl-h8w6t4cYwlDlkm2mguIwVQmbe_zWgbYnQTjZ0paeNRw0NMEVm3huQsLIplc8rNrbFbJoKNJJOeN1TFbsWY0_DHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/blg0TSZQNitSNe1fpZyXfJWpPC1l78zzgrLx7-XYVazMHZtKmb9yJpFy8RUPNgI2uwgpyBIekrpc3Gajy_ahPCwbsvHl1SyciWl8OtkW_8R4bxDO6bUBGkXKeZtHv8m_M7SeyHbr6GK24GavkCbSU39HHmAEP4VBsbspgpAzQTzaKVTXKCvXu7qnWAg1NGrtBC2nvlukk5QpHVJaR22WCv2ciJvy6C19a80tT0bqTfwghs2WeGdM7D8_OHuyaCEMgyE7LbKdjSM-XQNXgp7Db_C1unBHlnyAUnVNDsiFfNTHLGfQW_hkQKk0nHGFHvjghXT2nKpAf2IEgOmya8f3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DPC9W0T2KBkTyYPfzwKXtkK3vMjd5ZjE1RlIlHZWkMrLATw6FPPL8HDGtTAlj8Ln0JQT9nTTWyMpb5wKGWg574uPMaTep0_WWlyvYayhShLAwSXTLFV0ZxkxZl7KUby8aD5fMGDcC2KhF1nXKvQGYUU2UWpUmSQFF5e338WPQlz5mdWosUOMlP1ntWhyHmiXrzE_tkUxZN-dv9dmXe913B0S6v0Ll1yI5mAIs19f_N8w8wzYSj0_KaTidWoSYTvsuXd-wrun6pA4kJgL9EshQKUKWTIPOPcHorYu6MzC3TLOpOCKgOHaaEMj8pOQpxdmd2faf2m8riw5WWMazep9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VvMLZQMgk_lscZ0MsjeKtLahzoMpAQ-jCAXs8BrzgzDCiZLs_YAuU8UKUC4KkhbvjePK2aXU9R0fUGc1EUiaPcHR1u7s0imW0oMEU7HThp-gUKVkjiYcjfQjei53Ph6eThkge3HIID6BGNBorc1oU7pPNLrQzfZpRSn3PiymsDttm4UR5cloLw5KMFqRUwBs-ixgm8QBHQyDUmKlnL8w8XIOG1zFFWvhGYXhfg53qONGq7bEqLzGSDT6gvbSVmjtn5OWzyqbb2sJEbyDiC4OyPGKQUvYhUMSbTEkQno45kFS5yOnlEC6NZFYk954kgo4t3yjdV5s5S1sdf8TiZbNwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hfqi6FdAiY24j4Ojw9THoGvbiGJqNGHnvUbxPOY-h1CT6BmiwpC5aPA61hD81H1g63XsoTEe19tNQimYQCq8DnTdPjgqYfhxynK9xo10GxinU82pIoBQ4g9lTXCx1StjhpFXUjp4JuUp_3Fj0KxLuTf_L2UFmb93UoaCFDeHzUww5RVDgvOUSVJsWljos7Pu7QszSPJ3q3nOuUs8Ob42Qq2g90olk0BumaBuS2bjb3PaTsvhg0FPoVBFUPpZJnNol6lulcJc2NfXEjWAK077aWGiqChLzrrp_DiZYuWvcROJKN_BDikGbTJWw4BJZQElA06105HLOgGomA_lB3zaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ThHDHniY1rhZZGmly7Dg4kRaL0J8OBcIC_z91PJXU0bsDflC_RxVZtdMWQnPmotoVB7xjx0-xyT2Gb_PePO92q0gHUyFOSAnAPLllQ137uCUe0Icd8zZXS009K8ENwwW_XwQNWn3Wu4h7rENo4-UOMmJISFdUcvI0Gav34jgWqGz0ZsU1XAjsbhW7eb8nq25mf72p1944whKyW7ZHLNjoMLpv-neJRkQLIYqF1JxoF7IBlFOYQVGG2jP7hXC78YcQdy8VXLsAiiTqKBawiGgOs5gExY3dLTtaX5OSrmdR6lcMRVRkivzuWInN-P9IaY9pN6tNnsclcR_pLPa0P13rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MqEd0r2PGbiCRvpu5mPXnSrycBc3pMf2SUwQyzr3DMZFn5oO6JWDLV1NvFcLjqZylOF-Hei1xNC2JtC31H7cQADpObN-IdX1dnJq6bY9WHR8Ai-YBVg4G9sVAqpAkc0j1dJUrvUDsNC_0DTE0Q9HxApYKixmscvUfFZeGrULLjdb2HqcXiDlKj1lnQrW6v7fhL4WPvh8Y5_ulguMP8UeEKrvJaYU4U7Kz8X7SJYR4Okzi5_xOjQs_f07m66Z5TJMRZtrb0ECjvzQY4H447dEsfIUgUGrjKx71ljrJ8qbmZE0oASXZlnJcMcKIy1aFHNMouF1HyCSYxZ1Ezrqq2DuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIVLZOXeEYwRYNFcflLd2CNsbAxvJPRWQO597zXE2mtXasNKrVMLT7AzU6u4T0GLF67AnV4f0o93c3EE18QnPMxyaJWJUq6lk8L-elw9iQvQbfR6oR--_jynda_x8DDY-Vzvre8sxH03p2pN2tYcoH8butfVzwpth-Tv6fikIvgmZQvp_N-RpPAkbM-Ou1tSum1Svz7a6AzY0pyE28E_jdcwwZ1JbyqZtowcECxKB6xUyrKc-XNbFys_uKf_5aDG7JrvRrp-ksOwVMiZZfXMLjj-W2WxSvXpi4Xx3qP77uW4yhmtEyrNZju7ZNK8w8tfN7L7-7lqlkRckN6OXH4O4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7lIVgWsTKPsl4h6B8UQw9tA5UsVoE5AaR2r3OGSmJOG05InQuohMzjK2PCMJaUIwvt5jrsxAqWoajKrTlQAEaZrly9I78YVuCoP6sq1KDmOacSwSSOwrLxiH02nHXsSV5j5vSIxzzjjZ_bkBw7JKGnC0UWWOr6FFi1xRbWW5xEK7C7W7Wt9ff9aUt-S2e_Gbvc-LxueOVfbDJ_Jwf4YvEvSRxJqmDgJMuhm66Izep25DSsABjAKe01_A07lm9sO0T-ESjRjB4s2gTzTm2bK0RQsIgPDbyLl-XhAvYEn0s5u7tJ-lMdIKAd9e2jvrhQVuWMJnuAr-Bz1A9kCHWwtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHf829JjkjEDyhBK137X0V6mtl0aMhjVghbFjFAcrQbnBT472WrOpofudxrPcXnkHLihXr3Iz7FyFIwuBlreqB8DrA6jOWY2Ux1T_tah19JULD5kYnfPGMA6S3ryL3cDlpbmpr6lT8gDSj4r9LPu8dB-pEJqSWGNx2gOngWKGkO4yZqfGdsYsvnZL6O21TWnSsmd8D7gQn6idBZDbQRPC5NpN0-1Hfud0g-5RHi2BdMTPqozvthfCnwsTveg-GqV-E3U7l8GvJ_NRh8Q7PbGHT_lkfhCyPZ3WCcNnz87h68n87i4Bwxjlnypobmlnre2Zk-1rs3_GsecRiH6fhiKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnHOF18r5Ptr-eoUygQRxjTPACipyjlvK-lMUL1igm0JIiaSYUxtjRnAJkzzXj4kmMAHHdyBGNpHvc6Bth_wOHj8XEygWqe30G9sZ2sasgUnEecD7Hu-mc_OyvY6PlGa7zz0SkgXQBHfVioVgM-uyVEQBaNYK9EBr39ullUAojMNjciOJpQof7Vs_WZTsAguQuZ0nr1HB2WehJxWrLgYLtcSZ7h9F3TolcyoqKqL8OVqgc0sqRpHhswNHb93PDMaxFkII-wDN8RxCRkIzno2y8J2pO608zTVCRpG0WCLBYXVW-6DcjmVfCU8jt2xzlMl_FSm09iQYNr6QkDFbfeGrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B_xFasJAXuC4O1RVhd_lscbq-TvLtKpxD7zCJuQAXFi7AZU_VbUa4TtYAETV17j32jb5ejme-ouJuh5xHgQFUxxigLsxkGgkBpQ9ybDA9W84C2eHdu8pv0nLyfwQ5GYLQHxPlxsTj8zgn7Zb6Yg3o63Li74e7PWj2j4JgbFUCgBZTSG3l-w4g3r7zyVUo17w2uthC9vnYMD5jHAEkEP9F3ZptH3Al7u0F0fmZFUd9OSWMhJ5PMrqof1Vc9bfpqe7Pcmnw8K-X2g9sUFGYRltjsB5kmgt8i47Gmv2rSULg1l7hkCle9ydrXGOA4bk4M4e4YSu-24E_Uj_Uh3NhEB-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HgqK4NZMFD5g9852F1xnF1hV5yuy7OG-KBNkUKuFsxaLKg5ayjonSzE5r3z38rlCm4dnGOZTwQNfHy7mNUQA-prZ-S8c2kx4kiOGD5oEYyUncIyNNd5U_oRdDQQ7yM6NRGmlErnpM2hl0l0JgRCE3YH96J9lwRSlzi2WNAlC_TTnoDtp-yV2plj9EnQMzcYNdosnDrdHRfFXlD4J04QoypWJ3vij72dkkXd0EVNCQowP2Kbt2mOdHlgmdHncg-x1vfDVKQI9Hrc4hb59D9dbvfd6qUhbMCZJ2pyltOzWiAHxUo7iUf2DjkkDmPyysrVJheJITGg-BkuWMv0H_KxvVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HhSmkkQjrjnirSzutRm0CBBRplISN_PM2Xopl8l2Umq0inYBalZDCjpDdm9FaWhAdKexnbzNL6_5gmql9o1xl3afceB1cx77KWBj0kXl40Gimwd21iRNgFSBpXlfKPP0eQSwMUViLbV2oAVS39s8sTTTp9JmEVTMf9UP9D7_XEaXIblfusy4QNoLb2XwVEgBmpScR5uDfdnL1Lr5vKey8vlxncYcBgdb-jttXqHBPuTKJZQTFtgvs2szqJxcrQa49XunZ_mK6URyBloysSHGryAEFUFdNRPdzTqoclcZiRQo3JC0rd_YebmEGeAYezZlnLaH6JgGDGzGeTek37Urpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QJfm5wtF7zPTWDuBadd7emADtqqeL0hAIKy7-5FoOrS0xXWlvA3HVGbLG00xPGc_5MPnu5wLAirrofqvLv2QRV7tmFgmvk8728StVESCvUuKGlfTc7V7jwY9n84d_VIkd-WnTOcWqfnNjp0htEmwOr3sZuey0y46pOQjfL1flAnCeAiC8nPeuFfXqhxbx5UcGg9Y88tSxVyqE-_AEZHNppfoSwBQmyBpYCIussk-DqG1gZbniJaGVHfrNDBZAHuAtRVlX6fB5a6dgvZVBEuITrifg6PFHLM1fuws1RFcAYRsfZnnnUmY2KfgxAoBNBOwOpdfufshGmJU8L8jTJtq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود
مخصوصا راجب این Demo های وان شات
https://www.youtube.com/watch?v=LmXU6SEH3Ks
جمله‌ی کلیدیش این بود:
The Demo is cool, but not actually a game
این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم رو داشته باشید که می‌تونید همین الان(حتی با یه اشتراک 200 دلاری کلاد)، بازی بسازید بدون هیچ دانشی!
طبیعتا کار رو خیلی سریعتر می‌کنه، اما باید مراقب این باشید که ai، لااقل هنوز به این درجه نرسیده(و به نظر من امکانش هست که هیچوقت به این درجه نرسه که دانش پایه حذف بشه از این چرخه) و خلاصه، یادگیری رو متوقف نکنید. حالا توی هر حوزه‌ای که هستید
نه جزو اون دسته‌ای باشید که میگه ai به درد نمی‌خوره و Anti-AI هستن،
نه جزو اون دسته‌ای باشید که ai تبدیل به بُت‌شون شده و می‌پرستنش!</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ea5gk7FE7LteIrCAqS0eU2Fy4RMFbpI5esqAkjVaRtU5matC5RwrgxtsVYAIHWxil8K_2gWCav2wh8gkLH-FJ8qkawR8nWUQmsSAYuafQufczrUIrE4zueO1IuRGKqRAVsKcMfkvkGE12RaNeHo8Kp_8H-g-Y59IEXiw8Qit_Nhm-D4UGOW3j75IFN5bXgLW8kmR8jc_BXmXse3M6MGeANqOGwScFd8SHfFDBULSSyEfHpruDHv01BOIa4hf8DFQWWXkqpuiNwnV3jhBH1GVq5GHYYnHQxwKywhL2KYZk7adlc9TE2fYqVXhy6GWVEmEmDx_fPOWQiUFBnjdZrPIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی:
https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو:
1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت زدم رو بهتون نشون میدم
2- کلاد رو نصب میکنیم روی سیستم و به روش استفاده‌ی رایگان ازش رو یاد میگیریم
3- با استفاده از 9Router، بهش Mimo رایگان شیائومی رو وصل میکنیم و استفاده می‌کنیم ازش توی Claude Code
4- با استفاده از API از Kimi3(مدل قدرتمند Moonshot که توی بنچمارک‌های فرانت‌اند در حد Fable5 قدرتمند ظاهر شده بود) هم استفاده می‌کنیم
5- با Hermes+Mimo و با Claude+Mimo و با Claude+Kimi، و با یه پرامپت یکسان، یه بازی سه‌بعدی می‌سازیم و خروجی رو مقایسه می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vo1tXqyF-ZGfsDiPHmNjIg9EGdyG2FKBLklGydkNAFK7YcVvzF0vyRLx27CogNbFEDhQbpvEj5WUmQv2P4LRsj8-6yZEndGyywYyy6E_z9_XQalovjLrxEewiZvayIoxdJz8t87aL98MQ8jsK116wugaWDOKMdeLen5BZ7w1feKGaXv_gyN3jxFIob-IMbZNZGxQnfy9WRpbleSgnWs1coQBmM_xTV7saOTen5pULZb6naHtf6h7wdMtyiUa4uadIwE8dBlbrYWCPFrUFn0Icoomf5jUYhzHoy_1M_ay9S6XcbjixLRwnysLrJGdGOW4zetiZIopGaUNMDWAjtdYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">(با کلاد رایگان زدیمش ولی)</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/4764" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vsb0FelOjHGafT6JCs9iRAjR307vGMEBPcNZvA3US7aqddNZ4XjZ5btyZK4r8vbZIxvctbbP079jzyWDhfPuR7fF-CgPg3htVLk4GHyHEqOz0R1gGDFCcWsS2rwGnv4StyUQ7R9E7S7P1-pfgEGIJGwaSfVwb3lPWNy3OvdLs3vLFkmMg2XynfFIsnr34rRTo87CNaAL1XCWt58IBRTEe4PtXbo33iKZ9jIhyFv3zu0yuAJo0HcDlgibKgBx8gznUIJ1oEiOMc5gqJC-Phz2_C9kEk0RwfTaEmHFgMAh9crjOMQfX6q_G-r1hZ7DUhmNogumKVG_B4SWQy5itzzapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/4763" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4762">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4762" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Czp0IKhRe2A9DuhBGCF0rtVYIU0L0zjeWFT9dS8dRcSVF4-IU1Zw-FwLeNANhaUjSMqFu21Rp7Pvz0bpNcIjNkxhmzDsr5FKC444rsqdHCye-3DL1SO1Z3j8cpUm9sy33XQwD6P8jepChUv5Ii8fFnPgGQ0QMW2hdqrmbuny8oztICP3YyNFQjMChL5IXhV8rlwLorOXMGSsFCl0OnYkwMKm85E1gp6vMCTlxDbRzCaipGo0angKZ1TKnNq7eBB1l3npjjySZ39qR7gwYfmiMzPXxgr2WfCySoAXpUgQzez3iRR1v_NPmTRqPB_Q2se54yvvrUfOxsIdk-hKmt1pqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4761" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I07YRiLFxkUbGTCVx6ayrPhRRYdWcHDy7CmkJIdTZw1OYo95uFJsqjfnqAiRc_F-1A6xPVngOIPtQ5DCZpZDGOZRvHxB2VbTPyRBEDKvG_bkH3BbVxiCHZtrtG5tvhYeIRioIlt1TPjteAFBnftDGbbm2I34f_VPz__hlyJwxMrD-g5smNCzpZbuH33VwLblSiHIVN0sLAF-Ard6WCzduvRGwpO47QEbF1wcW4tbB45ityuZ7dj5UTh0_X-4adHfdAYgvFJ987kpTwEP1WP2YE7WaTGUZ9rXCbyQaJYN1eod7r1QXXDj_XzwDKD9NMhAB0fZcoIHyYIniqd0_kdszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پرامپت دادم به هرمس که تمام اتصالات سی پی یو لپ تاپم رو داره میسوزونه</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4760" target="_blank">📅 18:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hoybhkvs9YS94Ar-kupHLcbPZEwNUKGqzkuY35saKm2Aa6Nkd3EFHdXC6rhp5tcR1dABq-3mEkX3T2MiSbAQ_wQHQDZWJZofq8ZkF3W4vdsgOkot4ez6DycvRHeNHTziivZB6ELh5cdaUZjfDpMYMhGgALK2YUDJeb7xR5puMDYEa4TSJfLJ2p5obDW-4i_eKlRcZcjRphT1PovwSCbcTh1H8a0G6jBBpadfoeb9_FGxObO-jyhnT0XYO2BsOcL6z-LAQKCqAg8ZHcOxGVOjiNRT6Gvj4LKy-4V2OLvW8bsTQv4EypieJ0jVp5pZ4GCPSeHCAE9QtLxyPJcmH-65Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!   هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده. منم یه مشارکت کوچولویی روی خود هسته…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4759" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4758">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">و روی یه سری قابلیت خیلی عالی برای SenPai Scanner دارم کار میکنم که به زودی ریلیز میشه</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4758" target="_blank">📅 17:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4757">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UaT3_DmoIQyBSvTdWLxn5djvjj4ecCpZV52iCeI6E3xdYzcKbqJ1gjm3NZzNz6SaSermvNYybbgMYxhjle1iBCAK-elNdl3SvviaIxsskPIW5xmrMke-qtFGaUbHvLtRIZaL2MxhJEk87JryxjhgWP4xdcE-MLcr4rc_yOZwaxZG9QabLatjDZDLjNWmANyFU9YZxHZRUHunfry7aXcK0Zbf_mvhVSX44937rPBw_bCPrA3bNo-023uhK2kRJHdgYf-lyPydSkq_QaCTFeGg0WcGbgrppQ29X1HrfhxLNaGRCSmkuNtfjv3gqbfYjB8X5BwevGRANJktHvTHMvuaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن جدید Aether GUI هم به زودی آپلود میشه روی گیتهاب</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4757" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Aksoy</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=bLQHQIR4_Qu8DPBLeAbfAPkpnjlexREGE5AF4K0GTH0uVRgJBcM2RP6Wld9yDaHrQXiUo-aaOCs9P6aK40ge0SjucM-zvLdBcMPRqsS1apztq-BIeM4wqWlEcUhv7U_P48UaAlFDOC5iW4DgN3zXneoxihXMULzm4BY9TOFVZjmILSNTvRx6S26qsi0b4yhRqtU7XAt2CL-1vxxuqUsmh6CnDO2AxCz7AePrDJoyOk8LkDK9V7-CK5FXWJ-b11TemHshbIRtcpZZf6xbkTjQDoBr5o5xlidhb7aCO_DMJcoNMFS8iPt6Arev8Rse55OJamt4QfGii8C7wOXut-2Gvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=bLQHQIR4_Qu8DPBLeAbfAPkpnjlexREGE5AF4K0GTH0uVRgJBcM2RP6Wld9yDaHrQXiUo-aaOCs9P6aK40ge0SjucM-zvLdBcMPRqsS1apztq-BIeM4wqWlEcUhv7U_P48UaAlFDOC5iW4DgN3zXneoxihXMULzm4BY9TOFVZjmILSNTvRx6S26qsi0b4yhRqtU7XAt2CL-1vxxuqUsmh6CnDO2AxCz7AePrDJoyOk8LkDK9V7-CK5FXWJ-b11TemHshbIRtcpZZf6xbkTjQDoBr5o5xlidhb7aCO_DMJcoNMFS8iPt6Arev8Rse55OJamt4QfGii8C7wOXut-2Gvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر با QR Code یه سیستم جالب برای انتقال فایل از یه گوشی به گوشی دیگه ساخته.
فایل رو به تعداد زیادی QR Code تبدیل می‌کنه که با سرعت پشت سر هم نمایش داده می‌شن و گوشی دوم با دوربین اون‌ها رو می‌خونه و دوباره فایل رو می‌سازه.
بدون نیاز به اینکه دو گوشی روی یک شبکه باشن
https://github.com/bashalarmistalt/decimen-optical-transfer/</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4756" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مصرف GPT خیلی خوب شده الان که تست کردم
گویا از خود GPT-5.6-Sol استفاده کردن که مصرف هزینه‌ها رو کاهش بدن
😂
شرکت OpenAI امروز قیمت GPT-5.6 رو به شکل چشمگیری کاهش داد: مدل Luna حدود ۸۰٪ ارزان‌تر شده و Terra هم ۲۰٪ تخفیف خورده. نکته جالب اینه که خود مدل 5.6 Sol (قدرتمندترین نسخه) برای بهینه‌سازی load balancing و حتی بهینه‌سازی forward pass مدل‌های کوچک‌تر استفاده شده — یعنی یک مدل هوش مصنوعی داره مدل‌های دیگه رو بهینه‌تر می‌کنه.
این هم خبرش بود</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4755" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4754" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4753" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetBlocks</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9RtoORhTIU9r60tmqBA6mY6W_8F24ODib2B9QBpoIV1YmvrMUMvai1s3HD6h6fbPC-oUeXgbZsz5iKjBNaGS1mRzNzLD9CBQzQ2gVGk5dBX1ZUkwZHwLAaSZOmtH-UX8JNpacUg72RjrQ6OHxUHHQOaQXusiLPEC3x4Ym8AC2iKVASPO6UcdlryRYNgQQVIsAcArSztqHCtyAlyErEVjVhC8Uf9hBGiNPC9rU7CR1Yir_gBxW9udrFoDmRVfHd5K9V6JFegfNe-83ulsbiFvqhIk3KnwCADck-rAZ4LxpXldG10tPltdafUGfie-foPt1izOWQdsMEnnr9S-Im4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in
#Turkey
is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4752" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
