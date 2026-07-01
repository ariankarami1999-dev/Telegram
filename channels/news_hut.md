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
<img src="https://cdn4.telesco.pe/file/FkoP_aIeIL4_-_inYPZro2KkX3opEAg21gfjMIaaHHMqWBonI0wH0NP7B1zMp9_tXARGNQLpQBLhpn8-vBOAwLZ1aGwwmFjStYdT7Ojt1pJias0tSQmw3qUZHuM6ax2iPaGj01C9cAX-3EdnCWYbkSH3AAoyKdgWRKdxJca61ijaFJtRyCvS83xET_e0hk0Jt_s4HmLIW99JH6RzpIrlJoF5KQM6TdfnzHjoUX5u7GqxpP8_E_ifu9k_w-Zv66zlX49xblAQJnVD_BxIABhHXMaUAvSxqSs77j0CHIjzii52kUIcOBZvE002_HJgdbEh8RIlT-NkM6M5WcmYOWfjEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 216K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 03:29:46</div>
<hr>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIEHIdySgO72RJzFnrbD_UUe8aXo1UoTMTJ6Vnwnz_BZRdwQfWUWSpgg_1QL9stERD0MdRPPeYAx2JDg0kd4hRqKiGqhDB73ceZZDwPjZXHLIKW7Jo0ZERfwZfwMOWfVXe_9zcN-0TUCKWw_PZD5m5lVszS8AJZHiaQ3aVfM05OjATLIXYgu3OFVUpgkukdrJ2G3naC-wMFf-qKhPfUnR8LuQ0nwiTrU69TOBtwq_t5wfSh51E4QsF88cYxAU875n5kHVfIBWV7i2qdWdnFXVZzKp4LyRIuqa3zOZrHVytai18Vw8f8Jcbgc_JooIeBlgNB_LWIf7HiYvi58Oof8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=NOqShHzu74iMPGBJ79thZcfbE1vB2X_ej3iYGMljksMV_IpZOHd4qht7A0-dnUbjFzOric9uWrcWRasd_FxFoGOYrfuPmOby4tv6uBIOXZlJq63azGBKfGMG4vb7DCr4IX9Cz827rnv4dbODlkRXAJ5IMPewfI3qg2lWy1BkyPkMx9nmREn__twy5TFR3Mgo40GCdJGVuTTQTw8Z7NXB-EknzbL4y5DMJyH8EwbsZSojvDlvWiF8nMrbbtJHCyyzgjL1nosWU1xnmkU1ROW8R_P9iTXtcYx-bOgWclyYai4AGXQ-86d9BhoiFYSrpjGrtnEgta-GAZueCgKjfnQ4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=NOqShHzu74iMPGBJ79thZcfbE1vB2X_ej3iYGMljksMV_IpZOHd4qht7A0-dnUbjFzOric9uWrcWRasd_FxFoGOYrfuPmOby4tv6uBIOXZlJq63azGBKfGMG4vb7DCr4IX9Cz827rnv4dbODlkRXAJ5IMPewfI3qg2lWy1BkyPkMx9nmREn__twy5TFR3Mgo40GCdJGVuTTQTw8Z7NXB-EknzbL4y5DMJyH8EwbsZSojvDlvWiF8nMrbbtJHCyyzgjL1nosWU1xnmkU1ROW8R_P9iTXtcYx-bOgWclyYai4AGXQ-86d9BhoiFYSrpjGrtnEgta-GAZueCgKjfnQ4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLPeW2ziJY8lR4naMS2QP14B8XHhya1B8hvm63qIDES12IZlR7OL_O_d9egn-QoHiINYaGf0kaFXc4uMCw8w_kMx-5732RX0WKheZYhD1-tyXbfiCoFqB2JbQjlQoVZi7JTBXgb4oypF4d3CZ2KD30-NKtIFACypdsNZenvBmHwlIhGGncTrpncqY_kVT7t3JB8zCQHvHFsqUISc-4kETXpSe66rPhXKA5nJBesKqOwaSpY_LMU6agSHNrwfuhqxWzqn9azin3hLIqF_1liAPFk3hOOhsSJMNoqHAAnZH4PUJXkvmhhNuDnbZ_sQWDrV2EOj5d5y4YuX-WnMnhcJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=DLRFM1FHaro_di4LzcA65twXCeNbca5Px53QaJua5K6zWhS9rsMFRJ4sg6o6E_D-wMP2a3TL-skVUyciM-D1UIJH7nIHM1cL5eEXLVDUQztfshJLrhRJUFQWp5afPRBqPBJXI4MQeuc5lD5mAASK8keSWM-BMD8qkXqTpuqVMrtGP_8IjLwR-K-lC8GSjAtylyKguQEtMf8QyuWQ7-bdG64znrSOyanLZREulwzrScXP2AzYuFtlWgUsUeBwiPcb_UdCerwlQBY0vivhNXNkCxmmdRsSyk3wf4rJ_WhyK_FXLsMgIzFpuNLmmzyYr6GH_y9hUWa42BwIOXHZAJrOrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=DLRFM1FHaro_di4LzcA65twXCeNbca5Px53QaJua5K6zWhS9rsMFRJ4sg6o6E_D-wMP2a3TL-skVUyciM-D1UIJH7nIHM1cL5eEXLVDUQztfshJLrhRJUFQWp5afPRBqPBJXI4MQeuc5lD5mAASK8keSWM-BMD8qkXqTpuqVMrtGP_8IjLwR-K-lC8GSjAtylyKguQEtMf8QyuWQ7-bdG64znrSOyanLZREulwzrScXP2AzYuFtlWgUsUeBwiPcb_UdCerwlQBY0vivhNXNkCxmmdRsSyk3wf4rJ_WhyK_FXLsMgIzFpuNLmmzyYr6GH_y9hUWa42BwIOXHZAJrOrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=pCrQtz0z6bWFIViSiYCSRnasJoLw1bQYNiRjqujliyT6OUuVYi3Fatec6c6NW1pu9fvKiZHgxMT0ZAmW6Y11vE1HyjA4hR3hDOySIc8hfD_VABIR7x-CKZC_kwPzxovkQ6oIHYxXEGcnRTBfQEPSZrp6U74DBbCY_L0vm2DlU6Xm1Q3MMQK9oEyyy3kz2cG7wtwTnxAdqHeVKzKG4f-p4hA2S9SEsGSPOSoNHO1dblpBjc4X1DmRV0q0J0-S3pqzuBDGp-A597TiU5THn_lPNtgM5DfBqqYds_MN-SYCP5P3cQ8L2vrnetkCRrSiBM8LNYjhs40RhZP8jKhss2TA3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=pCrQtz0z6bWFIViSiYCSRnasJoLw1bQYNiRjqujliyT6OUuVYi3Fatec6c6NW1pu9fvKiZHgxMT0ZAmW6Y11vE1HyjA4hR3hDOySIc8hfD_VABIR7x-CKZC_kwPzxovkQ6oIHYxXEGcnRTBfQEPSZrp6U74DBbCY_L0vm2DlU6Xm1Q3MMQK9oEyyy3kz2cG7wtwTnxAdqHeVKzKG4f-p4hA2S9SEsGSPOSoNHO1dblpBjc4X1DmRV0q0J0-S3pqzuBDGp-A597TiU5THn_lPNtgM5DfBqqYds_MN-SYCP5P3cQ8L2vrnetkCRrSiBM8LNYjhs40RhZP8jKhss2TA3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=TOLrQ2YekB22RjdW-S9xtnFDgL68vefPgcuXaSWVJ_Wy5JfCOU3g9iJQpya-pDb4sapcuoneTy2Di2aL_eYyE_DnxT38R_lHTQjOUF0Pi7yDPI7Swp4S_J4n2bUewjRCZ3VIVAUXgdKnLPT1TI46t_K7spv7Va8YhT8xnJUtI5jIoGMSxs2kwwnTkDS2gBJ0iVKMLigbHNq_Pb0pFTc7MRSrwvvAgfwrpm5v4169vcZAXdtICr8MZxeQ3jLFimTpSNZua8jHCctlhLvDbfYRSRMlR7Chn1F5MPikGcw75BtS-MYY9O97X4UVQGbkYNPr_42IGJJLUnmssYSmIz3efA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=TOLrQ2YekB22RjdW-S9xtnFDgL68vefPgcuXaSWVJ_Wy5JfCOU3g9iJQpya-pDb4sapcuoneTy2Di2aL_eYyE_DnxT38R_lHTQjOUF0Pi7yDPI7Swp4S_J4n2bUewjRCZ3VIVAUXgdKnLPT1TI46t_K7spv7Va8YhT8xnJUtI5jIoGMSxs2kwwnTkDS2gBJ0iVKMLigbHNq_Pb0pFTc7MRSrwvvAgfwrpm5v4169vcZAXdtICr8MZxeQ3jLFimTpSNZua8jHCctlhLvDbfYRSRMlR7Chn1F5MPikGcw75BtS-MYY9O97X4UVQGbkYNPr_42IGJJLUnmssYSmIz3efA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=VD8ZFjzLIQJ1S_ZpgZOBZv6LypkIZjZ3o0l0tcb127_0EizW1ymmdpdYxHeMCDSiamuWg3IOz9UDq4FmECFSzN7BtH0w52L42JYUXhpXQ7F7BrNVMD2FWYHjzzWQ2nAd9WpWycMSQJmwtBQc1zLEEMHqiTZl47-3Vw2tz3NywHC75ZHp_Hx94qqkMO_ewM8sfE2zVX4rkx5JlL0NzYlQplNG7F0_yhltsCtGDvEXTaOTLkmXjjeIns13Ip5SI6TrRLZaj2aMOolXJJuBRk0ROnJFbaR4FXjg_0uipN4JsRTDESIOuYDWv_nQxSgJ5fOIzZIVTS2WYCckiukwpjNt6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=VD8ZFjzLIQJ1S_ZpgZOBZv6LypkIZjZ3o0l0tcb127_0EizW1ymmdpdYxHeMCDSiamuWg3IOz9UDq4FmECFSzN7BtH0w52L42JYUXhpXQ7F7BrNVMD2FWYHjzzWQ2nAd9WpWycMSQJmwtBQc1zLEEMHqiTZl47-3Vw2tz3NywHC75ZHp_Hx94qqkMO_ewM8sfE2zVX4rkx5JlL0NzYlQplNG7F0_yhltsCtGDvEXTaOTLkmXjjeIns13Ip5SI6TrRLZaj2aMOolXJJuBRk0ROnJFbaR4FXjg_0uipN4JsRTDESIOuYDWv_nQxSgJ5fOIzZIVTS2WYCckiukwpjNt6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=mxOvuqvvf8KnMeZ25tJuqRFq3SKLsofQX1ArogW3QTRvZ5dv4--hyLjHXFVe_uKjAOY1vlqkIhYncRlXlWW4UCn_MGj5vCnYufM4LFstqD6xu84jN4i994r_EmQWWHaWngWFBcJhJtcxlkVRydPp_mXP_rLVSxEiDdN1rRRuKGxUeIvFskv5vLZfxHU9Q1RPRa30T3Fn3uys65pfxuSQDfwHfpWnud70RmVN6nEkXPxC8kPBZsIbnbK5E6lxPlBqocwqWc-HR38cyGQY3l6bCQqgAo7zCdvyHSxiVkvJ79sHeRIbfkpMw_KfIcsYox0e-3Q3z8mWl4N4EElq3LN_0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=mxOvuqvvf8KnMeZ25tJuqRFq3SKLsofQX1ArogW3QTRvZ5dv4--hyLjHXFVe_uKjAOY1vlqkIhYncRlXlWW4UCn_MGj5vCnYufM4LFstqD6xu84jN4i994r_EmQWWHaWngWFBcJhJtcxlkVRydPp_mXP_rLVSxEiDdN1rRRuKGxUeIvFskv5vLZfxHU9Q1RPRa30T3Fn3uys65pfxuSQDfwHfpWnud70RmVN6nEkXPxC8kPBZsIbnbK5E6lxPlBqocwqWc-HR38cyGQY3l6bCQqgAo7zCdvyHSxiVkvJ79sHeRIbfkpMw_KfIcsYox0e-3Q3z8mWl4N4EElq3LN_0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDwv2KQSR3uhiq-Vw_62tKvPSeCjZVsof6DyT8chB0Zq_rIMCZ6FbJ7hiGe9xow5yCMA0joDka3b8RzNb8nv51fxAZkwnM7leFkEiMk1N1QmAkDARWDNCLBIPiQtk4cfJZsrnRjqtQUC05r-chQexczEPv0pGLBdBJ69TSqaI5my18XLMuQIVJ0dTDj-JFewB-6ZVi88PpidHDfAlLf6pvjgBMpEMXIqzJz8WMW9T5t1HvTZ-CkFS8yHoe_hMcwN-a1EljzWnJLf3pCklm4DdEhGt5l7TsZTQC05UR_wnqfuX5ICSLbHProdZmTp_qstSRsm9oreZpA9_8wMEWvFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY7hxqacCNitGEG3Yy-8R8Pe3o0aEkJgPCGLfuqn2hE6XPhtZhR4Zbphn2TBWe3O_1mS9MCiJ1zzE44dcJ8a2kUlNAkKikUUjzBTT2n924O0TcoYtIusMsLbGdOte2N389PZd1iCTk9tGZ9YE-8EoR2NSMoCY9sjBa_TH22SKq5qlHpgK-D4aojndzxWLmvn9WvCC8wEwNQq-SCryCkLXTDKz5VzMZ1oIK4RUeBCdw2TjGQXsc48gtuL5rwp1FVFiHHZcfxq74BCfsSnMnTw2DgczTgMN9bfpodCYN-ZMCNi-7R9D4q12Lpv0Pp_G7eUpID424iOXuQELLhO_egq5Yxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY7hxqacCNitGEG3Yy-8R8Pe3o0aEkJgPCGLfuqn2hE6XPhtZhR4Zbphn2TBWe3O_1mS9MCiJ1zzE44dcJ8a2kUlNAkKikUUjzBTT2n924O0TcoYtIusMsLbGdOte2N389PZd1iCTk9tGZ9YE-8EoR2NSMoCY9sjBa_TH22SKq5qlHpgK-D4aojndzxWLmvn9WvCC8wEwNQq-SCryCkLXTDKz5VzMZ1oIK4RUeBCdw2TjGQXsc48gtuL5rwp1FVFiHHZcfxq74BCfsSnMnTw2DgczTgMN9bfpodCYN-ZMCNi-7R9D4q12Lpv0Pp_G7eUpID424iOXuQELLhO_egq5Yxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=gNtp01Fj5iZE8lHjmaFEHPdExbD0vLLY07j8HGUllyZSRrEdd3byCgPZAx_3HMgbUdrg0xXhciFaoIucxlBpDkoO3N5vOHuhnJMCWGbTMctUfaDYn1MRgE4MIbzddA8HU1amMAI9eqTVdDqjzy5i8gaLxOx-Z16hNk7WNSatEA6WiWCoFOAb5eWL4U6nY_TRcwN3TJnEzfkqzoeu2l-aNcjLId_iJ7gNz6wgDwi346yJcuVT7fm-1WLzBUnzBwkajks5nOqtyD9tlySqs9g_PP6xOnuzhPaMifKINcoPY4NOVyiSjHiuWkyzL2HhVTR2G2gGo6fRXc_rfw6IFlI8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=gNtp01Fj5iZE8lHjmaFEHPdExbD0vLLY07j8HGUllyZSRrEdd3byCgPZAx_3HMgbUdrg0xXhciFaoIucxlBpDkoO3N5vOHuhnJMCWGbTMctUfaDYn1MRgE4MIbzddA8HU1amMAI9eqTVdDqjzy5i8gaLxOx-Z16hNk7WNSatEA6WiWCoFOAb5eWL4U6nY_TRcwN3TJnEzfkqzoeu2l-aNcjLId_iJ7gNz6wgDwi346yJcuVT7fm-1WLzBUnzBwkajks5nOqtyD9tlySqs9g_PP6xOnuzhPaMifKINcoPY4NOVyiSjHiuWkyzL2HhVTR2G2gGo6fRXc_rfw6IFlI8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=nr0KPM5n_1384L_7R6NunEg767wDRtL_pnKmjEwOCuTRcZbmBh_S_S5GEspYeCDZRluAeP9Bfcuc9H6klWxLedNamKkfE8jiffyEjTENkjOLXgQ0_gdi1EkekEuF0UKsE9k6VkzvPwa-Ayo0NF8WmUlCVJ-yC6Sf8Y0FVnkv2gcG60vDwzvkjxlxOx-kfKFcy52Frydr7jqK17BDvMbOANg7byQCxwEl4LUVUvs6c97i4IsJY-OpIQk2YRZwG535fzCyJvqzKMnw7fn4WdjteuIEbw72hvd-mSlR_S9xVcS1tFCqsP0Qex6PpPjp7zfdySPsXD561liZQQLIjnKhmY_bDois8e3FSFS9bHMe-6cEJhcWCUPOCqoMVf_dXXCzS0NygQizVhGOh53g9zCrma25qh0bIK6p9qMScI3z6koBqAxbxOwx4GE9_krimxtHgY5DS1N85eUgpsv3k1bahV11YT_8SknCj9vNT3KUPQ0dhVdgzm82gtrY6G9btRBpm5CVyrs6bG25kxxSbCsONI8yXNzvuSi3Juv0DhN6gkblD4wtemkBSZx9panEmxtY_1XJ65fWvJ_5QXnGXzQ0Hn46VPhsxW4Swj0QoeNugL-si43Wth9H-wTNloLyrcSbXbyhyygxit-4WRJ1NuipzdNwQM9OwGGS69RAA3fm_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=nr0KPM5n_1384L_7R6NunEg767wDRtL_pnKmjEwOCuTRcZbmBh_S_S5GEspYeCDZRluAeP9Bfcuc9H6klWxLedNamKkfE8jiffyEjTENkjOLXgQ0_gdi1EkekEuF0UKsE9k6VkzvPwa-Ayo0NF8WmUlCVJ-yC6Sf8Y0FVnkv2gcG60vDwzvkjxlxOx-kfKFcy52Frydr7jqK17BDvMbOANg7byQCxwEl4LUVUvs6c97i4IsJY-OpIQk2YRZwG535fzCyJvqzKMnw7fn4WdjteuIEbw72hvd-mSlR_S9xVcS1tFCqsP0Qex6PpPjp7zfdySPsXD561liZQQLIjnKhmY_bDois8e3FSFS9bHMe-6cEJhcWCUPOCqoMVf_dXXCzS0NygQizVhGOh53g9zCrma25qh0bIK6p9qMScI3z6koBqAxbxOwx4GE9_krimxtHgY5DS1N85eUgpsv3k1bahV11YT_8SknCj9vNT3KUPQ0dhVdgzm82gtrY6G9btRBpm5CVyrs6bG25kxxSbCsONI8yXNzvuSi3Juv0DhN6gkblD4wtemkBSZx9panEmxtY_1XJ65fWvJ_5QXnGXzQ0Hn46VPhsxW4Swj0QoeNugL-si43Wth9H-wTNloLyrcSbXbyhyygxit-4WRJ1NuipzdNwQM9OwGGS69RAA3fm_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=EDGiCdzsTTxZnC_cDWJLIazQDoAhewA8PSzrFze0vSrJxoUgh_p9a-6f8j5tz5o1EQXdtyP61G7GqHxEksMXSr6E0jKbI0OcJyqvBy0gKIYkW_i6HA0V3t8t_7b3-9A1KTiOn4sfEaDuMEGWUupmp42D_V33sWqlZKLouSKad_Fn83sruQURpHjfTVNX9BvuIbrvq-07oBpgcLx8Pay6pUn-6aYdv9o5Cb_k5YOStDxmzsDvwC0dWtbVsW-pHtNElCv-d42q-CknzekB_RDwavlideFdW9dAgk6HXUsW-vagMZQltBMh3xCOkCqGQ8E6iPxDDJMrfUldHnl5dM_lPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=EDGiCdzsTTxZnC_cDWJLIazQDoAhewA8PSzrFze0vSrJxoUgh_p9a-6f8j5tz5o1EQXdtyP61G7GqHxEksMXSr6E0jKbI0OcJyqvBy0gKIYkW_i6HA0V3t8t_7b3-9A1KTiOn4sfEaDuMEGWUupmp42D_V33sWqlZKLouSKad_Fn83sruQURpHjfTVNX9BvuIbrvq-07oBpgcLx8Pay6pUn-6aYdv9o5Cb_k5YOStDxmzsDvwC0dWtbVsW-pHtNElCv-d42q-CknzekB_RDwavlideFdW9dAgk6HXUsW-vagMZQltBMh3xCOkCqGQ8E6iPxDDJMrfUldHnl5dM_lPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=POOQ-JMitB0WQORcxnHRvJIoevGIC58A9lwpzjwBMkck2wfaHOdaJJKblThRT95XbzBnT3lOpGMmKyxVfW8aiVQrPsU-C3shkNrEtQENkGWS1q3VTKy9eEmh1H7tu9TLXtgdvpzvMrf7feE9JskuCSO8cuVczizkZ6xzH9gQ-OuJHQzHUJN0OJft2yqOWQPr17Ji-1CNfIaeJKbgMKTE-ZLHUg9huVSnhHxVV5Shg9SVaggVHVR4bsZ1-6mVUrcN3JDejhM4ownEITFTFDwJ4jn3Q-2AcImMAebonpNlk3wCFrqcVNcs5dWWi_r_j9bZPJxIBW_GL79HyGrOW43o1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=POOQ-JMitB0WQORcxnHRvJIoevGIC58A9lwpzjwBMkck2wfaHOdaJJKblThRT95XbzBnT3lOpGMmKyxVfW8aiVQrPsU-C3shkNrEtQENkGWS1q3VTKy9eEmh1H7tu9TLXtgdvpzvMrf7feE9JskuCSO8cuVczizkZ6xzH9gQ-OuJHQzHUJN0OJft2yqOWQPr17Ji-1CNfIaeJKbgMKTE-ZLHUg9huVSnhHxVV5Shg9SVaggVHVR4bsZ1-6mVUrcN3JDejhM4ownEITFTFDwJ4jn3Q-2AcImMAebonpNlk3wCFrqcVNcs5dWWi_r_j9bZPJxIBW_GL79HyGrOW43o1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=I2lrf2HwvEO3LL3tH-nqYcVFkWA7maaw5dVxP_6vLeWeXz2rhtrY9IOQ9hYtQ7zGpfjf-7jH7gBL3abENelJrQAxDa3JbzN1axXtxKb2u0tLSigI2crmcQor5uMs4Jm8fQZoKWybUKdq3_CT9HgFmZUxA5N04pJOWkBkWBx1dI4ySt4wDNpeI2NmZ-70Aek7zCDos04lkT9UsgMJxsrvPVN4NjaFNfEsy9y9tu07cw59ghbKnupoJBezZKrPsaKYG_NeMWOFW36BQ_iQucqC7Kpn-kocBc4Ng1ld4xVD3-t2VbkNfPlg1wDZdbni8DlraAmY8frH2yWeM_fVU2HJNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=I2lrf2HwvEO3LL3tH-nqYcVFkWA7maaw5dVxP_6vLeWeXz2rhtrY9IOQ9hYtQ7zGpfjf-7jH7gBL3abENelJrQAxDa3JbzN1axXtxKb2u0tLSigI2crmcQor5uMs4Jm8fQZoKWybUKdq3_CT9HgFmZUxA5N04pJOWkBkWBx1dI4ySt4wDNpeI2NmZ-70Aek7zCDos04lkT9UsgMJxsrvPVN4NjaFNfEsy9y9tu07cw59ghbKnupoJBezZKrPsaKYG_NeMWOFW36BQ_iQucqC7Kpn-kocBc4Ng1ld4xVD3-t2VbkNfPlg1wDZdbni8DlraAmY8frH2yWeM_fVU2HJNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gw8No68lp9wWVHExlGYMWIzRJ7U-Pmp38-lKUJagida2Ot8jJwTKr8IuxewJ38ehjCASkJfo1-q0gyKAxZPyXxidUpi-NYUAl1WdT7481L5KW-TYNbEi38kYeSnfgIFu3Bmfa5z29njpCXFRuOMCowInGA5kciSmfZjjfXcGW_LTUIAMGxLy9DweQWwZi6G24eMIX1qPsdCtGTzi2vb6wb2GYCjSvQhmvFqAmMXl-oSJNMDDz1C5XTh6ZNS5-05fdgDsugi1LX843keu64Okc504aMMC7ezFjmkJjhZON0R8zEYmPB_GRzV-o08FzlzuPA0Wkl-XYRk35ZAtKesKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4_JVxkOlUfZEp32xhM3-wRs-fAtZ-cUabDYhytdUWY1zIlxzUQadG1CFrt5IzWOfiy9kRkiystB_tAp8mHvUDpP0wQt-DTDypXB7dc3Tc0X1Xl-kUb62Z8pYJHNgfJ6m8mQXT1UA5v-AtZJrqoGfxvhZvWPeEuGqs6BxrxdFv0oWlo5Z7zsQQbVf2X0_267dAKjdy8IicDGqKK4paclgxuT5YAoPhuVKYjNxbcWJ11zsFQYHvuvZhlYcAqtnLUzEf6kW-mjTB2U76ZGWMCd5Bo1H31h-SCDcUBBsyEqSkJNsjjFsF9r6eTdQpNazkjhOxDQXzn-OdgGD6DUTQt3Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDQsQxCBpCK6B-b4dFVzg2sEdHj7sffq4PtiYSy3y4kNASK_m7_9XPsmQe7whKL5HYbORklMjHJ4u-fHFtysX1SZ7lbLt1a06o5o8cgdAuLtUIrgygNMNSPoV2mSk_Im71_Ymc4UxuPbQiQJ7s_KLrmNpNdCPi70cOcmhETtj_179Ddw2f_4Efh-AbnqYcHNHf1hWEDpHzq7d4gvNypYCUuzjSh-Wsej2sYeyGs6zMqE9_aexDAjGkHRDmnlSdsAroM9EjlCSoQ3VFoCldzqp3dK_QwMw34CJNPd9byekNLsOSrNW2QsyYthq7CPg8PvuTfYaYRVgG04LrhD1s6ylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hn0HRuSnra2IoQNIKzDtnSh3pvSc-yK427wN5uHy9QSzriHWe4tyY-RgIw2RsA2VysVdawrxwvmIbRNN6fLtqGYTs2zP_45jaWD9U0TQodHSlPpiSNPDQBlqAikw0DtLN1Jt5RdWkanYhsVwgY6ZIn98K7D1MiThRxNtsKewO6iljnDr89SlEEuMU42ePkPha8rUYMI18Bj5bJx0Dcu7JHD5XeEPtcj7KTRRPjtzbF2dr2mQ9R18FICTDb0X6iv2y4cBFwxV3W5cIYaPqdttdgqKl4PfmW8OZfFf1tXLff4F81qwY7x-G2frI271NpXCLLD2F3xhwSK_NOiwaQxJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FE_Q6vbfr0ZwC8vOptYr03-M0qz9SCjp20l7BVespeY5sYbyxOYDKCZG9TRV075kPxl-2Urhmy8bhBJR3PR5kieT2KWj0R7Bf-LD0lrFwm2CjS9cGlFvV-0fJvFax3ED7368UknwXIF_LDvP5Yc-OFTW12uAWTBfko-i6RBBpr_rEYAAPqa1CGmobg2b-5ZY0zYsf26Ii4VMfbUYcV7o3RWZU-6ZNbI5i645GdUcBJmtNfSC2mSUGWnxBYmphhq4PEZcNSlTBiFlV7GpJcTkjx-caT-SUCmSYm9f6J3lk6GknqTyA9xWseayPkwQ5SgpoanxoR8paAECABhQ6qu9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzvNKrYOm9f3NbUw7shrZtFR34D5dkYKHM3Mg8gn2k-a2K0lNZLcrjZOx2yNiZXEZWytAsLCSMjZDSn3csK-03mGgvXvTznZyq_HqqC6N7U9FABKxM7slUif0BOJFjtULg73Ns5ODo84tuHOkOa9FZjuJcBYfWrK6jN6xTRxE9c2dnBSbmb_yClG7D-ep-zceVdAAnWx8pP_xKa38kDp61Po_303WLAN9iIiz9-OiUD_3uhqBl_zaasmbJULSOTaL6AKBW-yrn1JbM6n2UovnAKCLbRvhTrQLBSqXLB6bd2K7ukn57RJVAVhalGM-Sr-kymKiF48BmyRF4blLNryeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Jf71KIbGugXtlVk2Y6YKtb5HiveMEM9H7lR_ADYwwW4TIRFbe0V6jZOmhWw4Hb5zbxJH3pXKk-M8TnQ0EZIwUauYka3EmYCJIUfFfZBDYmv_Tv3CJ6Oo35OdoaKOy7ZiYpGHOWJDcUXhJVh4nGR-S_l27QVRlv9fhscPd5K-5aqdzO5CqPVSf_pPqO7yZF-cEr0zqHC6o0WK_Yw9-YFYPOR4uTn31BlzBSVxPSwQaqxUgdnpwmninipI-9-ER26cR2NNOa4S3GtJRSSSZRgKe7X0-nTWWsFwr2hK-S1D0XWy6X1hpYaHomtfFJ12aq3KjZEJxiiYJwVzpT6ZeLlZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Jf71KIbGugXtlVk2Y6YKtb5HiveMEM9H7lR_ADYwwW4TIRFbe0V6jZOmhWw4Hb5zbxJH3pXKk-M8TnQ0EZIwUauYka3EmYCJIUfFfZBDYmv_Tv3CJ6Oo35OdoaKOy7ZiYpGHOWJDcUXhJVh4nGR-S_l27QVRlv9fhscPd5K-5aqdzO5CqPVSf_pPqO7yZF-cEr0zqHC6o0WK_Yw9-YFYPOR4uTn31BlzBSVxPSwQaqxUgdnpwmninipI-9-ER26cR2NNOa4S3GtJRSSSZRgKe7X0-nTWWsFwr2hK-S1D0XWy6X1hpYaHomtfFJ12aq3KjZEJxiiYJwVzpT6ZeLlZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=OHDGa1HQv6JcSYxWgOuLpI9xGy0FvC4kEOj_xf-lpa2V-IIjbHK1OoEFoV7HSY09IAWYD0rZg3Xk9zdY89RY5b-EiOfEA7nFquSu11DsHcFvF4RWqYUd2MaB4-RAkbGGREjnsizbtysMiA-ntecEQ8Sgd-51TJqgVlCpyCt15W9gO49U0Wj3XLsdameYLsHDvjq3uuqkFZi8Dlza4XXdJjXmCZuZZW7osvRMIxJVM3UTgrbkZ1HZJlpuJJ_JA6Q7hXgJXBoC560Rc6PA1r74UY409ZJXp2k6Mcm11dwXMi22pK5miMYpLq0Y2iCS_KdHWziHG6HzpmqP6rMKQO6uSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=OHDGa1HQv6JcSYxWgOuLpI9xGy0FvC4kEOj_xf-lpa2V-IIjbHK1OoEFoV7HSY09IAWYD0rZg3Xk9zdY89RY5b-EiOfEA7nFquSu11DsHcFvF4RWqYUd2MaB4-RAkbGGREjnsizbtysMiA-ntecEQ8Sgd-51TJqgVlCpyCt15W9gO49U0Wj3XLsdameYLsHDvjq3uuqkFZi8Dlza4XXdJjXmCZuZZW7osvRMIxJVM3UTgrbkZ1HZJlpuJJ_JA6Q7hXgJXBoC560Rc6PA1r74UY409ZJXp2k6Mcm11dwXMi22pK5miMYpLq0Y2iCS_KdHWziHG6HzpmqP6rMKQO6uSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaoHAWLGnm-SsJHyNFl1K0_Jqc1hb3oHqoJvYY8wF7SmxWVca1Oy9Rayl43kp8q90pJJ0vhJ5C0Uzub6b7-Vy-LlrSONLHf7qWjCWvDkkfwjNlrKdtofdVT9P7Cv2bDaC1F8qJbtt1-RQsk8kiLEYAO6s3C9CNN8AGbhVqA9koxnOFU0MpSAPnTLeMUm07v3kpq3VHTTVhw7se-AEDpc0QK8AqTR8Q1boD6TPbqlhIOzYOEaFB-iFWxrd-I4i-WRoWxt6k_i7CGnsxzisVppDYKcp-7b5klSKGqIfkOcvGPAoC5NJYeaHau3hQWumEpHT4t4zXTWV4dvNuz7i1XPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfG9YDIHFfvl-S_btL325FsNuwgg-TWsCjRt1pjTPW8BqZ_wkhMHgvq6Ga8MkchVsjZGJOM86UK3V5S37ts5wrt5ToRdvuDIyqiwe22MH9R4NhRJ9PekzC10Yg83YO4bv5w2uKb7RhUvggFB2X4xoaDPDx2prqSqhcVAo6AWn0plkxDGnUK6vz2AGP-oLWoT4aRKo4t625QgIUcEkohLjp0FwkhZIYPkrqkx9nNfFfgzts0hOrfEu9-Jj3ZcnbbwRv2gpWiCLiwrN_zthAPCUAKVrX0MTmmozx1NZk070MwMTfgW_tKiliqc16rY7Vzf1i-UmqYeEspgxbb6GYlf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=mMVbJz35GVTuJbx2T3Jj-dPsg3MEwz5fmBpX_Yfms5GoTOE-Z2oABNV2jrH98UiexHHrihBlnxp7TMKihniUOjg9CG3TMCmz5lpsB2deoHA0S2EOwpbh_Opv4l_z5vZ6gEHvi3v4oT2BTe7i9yACoOulaMKeJZoyxKsqJ0PmAF28NpT49xzdJKvO_Vc98ICCFGIKQPr9fMpuotFaVevKL8sgTU0P-AFUAdBtbdXm54Er1syOHXVKuKsdHuOVIEpDfcnZhmQk_HbV-HkPQy7D5BPXaqynsJS4oGt8LMKRnC8ZzcmI2TacOlxodekyiJJXy4E7myNQHRF84eLQdE7O3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=mMVbJz35GVTuJbx2T3Jj-dPsg3MEwz5fmBpX_Yfms5GoTOE-Z2oABNV2jrH98UiexHHrihBlnxp7TMKihniUOjg9CG3TMCmz5lpsB2deoHA0S2EOwpbh_Opv4l_z5vZ6gEHvi3v4oT2BTe7i9yACoOulaMKeJZoyxKsqJ0PmAF28NpT49xzdJKvO_Vc98ICCFGIKQPr9fMpuotFaVevKL8sgTU0P-AFUAdBtbdXm54Er1syOHXVKuKsdHuOVIEpDfcnZhmQk_HbV-HkPQy7D5BPXaqynsJS4oGt8LMKRnC8ZzcmI2TacOlxodekyiJJXy4E7myNQHRF84eLQdE7O3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=vBrrYymBn_qFyVm2h-DvytUrN2Gyj_SjESTAbb1eIkXap8bsgcS5zoF4WV2UeLhrELmQW1C2aGoOHVw9M2DQNuBnjXHh_-M4ZU5WgZOK_fCxKih-QE1mbd_I9MApMeG9mK1XGJ4xR-BqBADwaJqMzVmjISLrofsqgHJV9XB8ScB3UPnWq_8hCqH79wav4oVMNk_kgs86NhqBqfVjZBRAIMJ9rAJ99k2pqHBY8uytLrAFtOt-qmuNgCuqEyDHvdbPG8ISvYcrgtVEU6WAHpmvT-hcSiWFI5OOgoAge_hhf5DzDvgIbHoFMeoksdjchH1Qmaf4-IgHM4tqNTR1438GNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=vBrrYymBn_qFyVm2h-DvytUrN2Gyj_SjESTAbb1eIkXap8bsgcS5zoF4WV2UeLhrELmQW1C2aGoOHVw9M2DQNuBnjXHh_-M4ZU5WgZOK_fCxKih-QE1mbd_I9MApMeG9mK1XGJ4xR-BqBADwaJqMzVmjISLrofsqgHJV9XB8ScB3UPnWq_8hCqH79wav4oVMNk_kgs86NhqBqfVjZBRAIMJ9rAJ99k2pqHBY8uytLrAFtOt-qmuNgCuqEyDHvdbPG8ISvYcrgtVEU6WAHpmvT-hcSiWFI5OOgoAge_hhf5DzDvgIbHoFMeoksdjchH1Qmaf4-IgHM4tqNTR1438GNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=D8a5GLdpUfOkdMG_3FRp7W92p_JRPV7vE23uGUnXcRBazmJzVvEInpitTIm5GFENIRiwBc8FHWEf6-SZnpU7KdqPypscIdqDcQLVudSQzeVrUA5slanDv4rTVyKS_6UVne60cXz_1xMS6iCglUTTGMze_SHeh-fTgGfOAqThpsijvglCh8UPXcwqRi3l5RtADQSrT7watIon-pD9CY39_L7-ClrK4l_RVBpsKTOsBivLy9dnkzL-rwSLHXQ5iDhOzq72hQBPbv0GBs_FcPsZL_AFH7serlPKMkTyWuDws8L5-p2Fa8CMeSQQHw7X6dK5ziWKDNYEPpr5KRRGdg0vOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=D8a5GLdpUfOkdMG_3FRp7W92p_JRPV7vE23uGUnXcRBazmJzVvEInpitTIm5GFENIRiwBc8FHWEf6-SZnpU7KdqPypscIdqDcQLVudSQzeVrUA5slanDv4rTVyKS_6UVne60cXz_1xMS6iCglUTTGMze_SHeh-fTgGfOAqThpsijvglCh8UPXcwqRi3l5RtADQSrT7watIon-pD9CY39_L7-ClrK4l_RVBpsKTOsBivLy9dnkzL-rwSLHXQ5iDhOzq72hQBPbv0GBs_FcPsZL_AFH7serlPKMkTyWuDws8L5-p2Fa8CMeSQQHw7X6dK5ziWKDNYEPpr5KRRGdg0vOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=lL9TP8EvNLmDBsDmATvfD7eALDHe6JV6tLWtE5NL--qBQQnJFyQQvw8-snroeup-DPmvihCx0DQuCcktQAA4F1Q1BaLq3KFzFUZgjQ60q8oDLCSGtApI_OTHzNwMyqWJyzOfOTZNDOTLlNeGywuHaTgMrZ-AIn4SDlbW4kNZHu-ply-cFUA5KuXqt712hjxOKyHx0vPkpvJ3jIKvmAqsKyxGDXFpABu33ezVCstakAsjs5WzkK-HN14tOHB_eVd9QCOBXSLcLwjdISwXSbu1racwDajWcBPu8DmAlYiJUjYQGo5xn5AMKRo_ZxMHz9GWR4rsoKbY_1Dy3et6ZmvdVzjxdSLhaFZfqgRgeNPJsEBL-Hmq80I_efTVoLWkzvKUqlM2n2jpPAfKma6pNMperVxr0MwWFbnsjtkIyz__pZTW3yDexP-_DHGBdJVYR_FNVqxpSqM85emy5f-PTxLeuqW4tzYlxUx2-ka3F-5sSJ57iYsDghgfNlVlXFpU8MpBNhvHjX0yAuaRpA-zDmkEXM_O_yleH0QS4DeL5L-zCQbmxWZAPNJCZLdVN6S6gLsJCdyvSw1N9LcCI2xU8MSXUvmr7PmzTaOmMvjiquPY3a6T3w36CG2OawLgYJX-dZcO4q1CUJKy5UKT4H6KLl-GcOouEXC9a4ZJwYZ4Eknsbdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=lL9TP8EvNLmDBsDmATvfD7eALDHe6JV6tLWtE5NL--qBQQnJFyQQvw8-snroeup-DPmvihCx0DQuCcktQAA4F1Q1BaLq3KFzFUZgjQ60q8oDLCSGtApI_OTHzNwMyqWJyzOfOTZNDOTLlNeGywuHaTgMrZ-AIn4SDlbW4kNZHu-ply-cFUA5KuXqt712hjxOKyHx0vPkpvJ3jIKvmAqsKyxGDXFpABu33ezVCstakAsjs5WzkK-HN14tOHB_eVd9QCOBXSLcLwjdISwXSbu1racwDajWcBPu8DmAlYiJUjYQGo5xn5AMKRo_ZxMHz9GWR4rsoKbY_1Dy3et6ZmvdVzjxdSLhaFZfqgRgeNPJsEBL-Hmq80I_efTVoLWkzvKUqlM2n2jpPAfKma6pNMperVxr0MwWFbnsjtkIyz__pZTW3yDexP-_DHGBdJVYR_FNVqxpSqM85emy5f-PTxLeuqW4tzYlxUx2-ka3F-5sSJ57iYsDghgfNlVlXFpU8MpBNhvHjX0yAuaRpA-zDmkEXM_O_yleH0QS4DeL5L-zCQbmxWZAPNJCZLdVN6S6gLsJCdyvSw1N9LcCI2xU8MSXUvmr7PmzTaOmMvjiquPY3a6T3w36CG2OawLgYJX-dZcO4q1CUJKy5UKT4H6KLl-GcOouEXC9a4ZJwYZ4Eknsbdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=sAjHB-Zx4EOXg8TUI1irCWqv_bX8YYWoZfdncx4m3ceEosD51_uKhyQ77K4t58dotjQCpXtjoTLO0xMhUT3WekfRe-W8S4BhHTHIl2N7p4kUMjiAwpGtmjwzZIIFNkzfvFqgJMUoQk2YUH3kSypazWicV9bkgxls8G3j4MOm6CjJVXuH9OzRkdnKAHTjEQZ5KJ18Y2m-PPgOWL3ihVsgXWIuVLccsjB34e53hXyQ5ijItZX78823iuGS6gt8dcmw5cOzppoHfQmdyJEyUN3cQoNrKr_HNmCgDB9KCCT8Htr2e9LDD6008l_btcg24GEQmQMGyq39fh_dHiFFwzy1mHtNmklPUyzy6SKqIJj44bo26AZgfb4wr7zKMrnissJ3DhNz2Zr46FfGwXwYwPKNFK-pX1Bt4NLKUuXC8D49M2k32A7LUWhOKWS1l-8D4ZGhOsv87SQEZux24oC0zjKJ0ExLW3meh9PL3kECZhbE3goi9acpScQwFZZacYrbSyjmQyuFbSf_BSE1Xke-ZunyuGtChQkLLM8g_CLrdfKtHRMQI6OzDmMAck9LVL820I5abLqh4xvIw5eYmF8Z5Sb1e5tSmhAAXaTOHMyHgH9XHw7fnTYc-81wVHhioMWWaMDq9jNG6Hnpb9GTcBh7Xhe6427MPStLkgdtZ6bpuPxqKuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=sAjHB-Zx4EOXg8TUI1irCWqv_bX8YYWoZfdncx4m3ceEosD51_uKhyQ77K4t58dotjQCpXtjoTLO0xMhUT3WekfRe-W8S4BhHTHIl2N7p4kUMjiAwpGtmjwzZIIFNkzfvFqgJMUoQk2YUH3kSypazWicV9bkgxls8G3j4MOm6CjJVXuH9OzRkdnKAHTjEQZ5KJ18Y2m-PPgOWL3ihVsgXWIuVLccsjB34e53hXyQ5ijItZX78823iuGS6gt8dcmw5cOzppoHfQmdyJEyUN3cQoNrKr_HNmCgDB9KCCT8Htr2e9LDD6008l_btcg24GEQmQMGyq39fh_dHiFFwzy1mHtNmklPUyzy6SKqIJj44bo26AZgfb4wr7zKMrnissJ3DhNz2Zr46FfGwXwYwPKNFK-pX1Bt4NLKUuXC8D49M2k32A7LUWhOKWS1l-8D4ZGhOsv87SQEZux24oC0zjKJ0ExLW3meh9PL3kECZhbE3goi9acpScQwFZZacYrbSyjmQyuFbSf_BSE1Xke-ZunyuGtChQkLLM8g_CLrdfKtHRMQI6OzDmMAck9LVL820I5abLqh4xvIw5eYmF8Z5Sb1e5tSmhAAXaTOHMyHgH9XHw7fnTYc-81wVHhioMWWaMDq9jNG6Hnpb9GTcBh7Xhe6427MPStLkgdtZ6bpuPxqKuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=TLqD1UKL1uRj3YWssU38DXMrRJNTZg_l-9yi82Ehprv7E2xSt63NNHfjTL80ur3banErNAr4FFbsgd3bTolwCdDJ_TLIb6PZ7_Ta3yFzXS-Sgopxx7X75Y4TnyFh9vf_u0Me5a73oF6-k8g4J-QNEHca4s8i5uqmT7TJ-Yk_PHvbtAxZZ4kc_e3wp1KG2CObprMFyIMm363FispuJBMTyDk6jnsCUV_Yk5jPHiqDTbc0eW0ZZPXJUpjD7cM1z03ndtvYQcoOkkvyM8o3eNz5ZCV8ryHrRXItl1TRNCrZOmpo6RqqJWwN3Na5wjBKUcdIU3WAhda_5lbBw8JXt8dWBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=TLqD1UKL1uRj3YWssU38DXMrRJNTZg_l-9yi82Ehprv7E2xSt63NNHfjTL80ur3banErNAr4FFbsgd3bTolwCdDJ_TLIb6PZ7_Ta3yFzXS-Sgopxx7X75Y4TnyFh9vf_u0Me5a73oF6-k8g4J-QNEHca4s8i5uqmT7TJ-Yk_PHvbtAxZZ4kc_e3wp1KG2CObprMFyIMm363FispuJBMTyDk6jnsCUV_Yk5jPHiqDTbc0eW0ZZPXJUpjD7cM1z03ndtvYQcoOkkvyM8o3eNz5ZCV8ryHrRXItl1TRNCrZOmpo6RqqJWwN3Na5wjBKUcdIU3WAhda_5lbBw8JXt8dWBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzHg7nZgAStd3i1qzaDQ2iPoHRhxKl4pDicOUHsIfUkh8p-9G2jeJMAm0Kf_1IZYi1GaRizrqcqMLBu2kOJbQ2XDuDrqxgpwLmTGuaOrn-jJkZ_xVUWyAWWZCFQAdGL_zvflYS-DOg5amRZNRR7Crp2O40GU9WN8zineStI3jn2B79Ji7K6mvhX8s9yKSMz7R1a52BCqA770l5C0F6hm78CYTv0bvXpiVv37YvLQCxjYQrR6O6pPFHqM0E1fdU6-sEkWZrxfqlX4xajF5btiF4g-PN3y0YMeeCINoxnZfviFrNYGxiwbjB5CS1CksnNScZuDQiUaEG8jAq0dgBmSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcooBHFheC8WEJKzTMvrtqaMMqgonozgYBUUjnypFRCp3p4XuUdHTxO9dg8l7FT-z3V1Uyx1_sHiMqH5bs5cIbZJZxK5HuvWvpeigKdqsMRYRIMVzx34-moGSc6GlS4fxs7-1-VdS53JLK-62xoVzrn6s4mZI0n02OpIrPLlhhff6sYJ_BRo0YcGxeY0f15J7TPuuSbi0JqKKH7lLRN3JagK1KykNh4piGKQSv2Pcha27gzoMhQX7qK9nhgVT_kDDZDUw95HtjqWSyTDAQkICCY1Er_E8DMBSUwfreJPOZbIc_gvV9XpshST02nU2M8Db0LQvMiHXo7LhzPaduBFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=vRFBr5UyYm9W4kyRJWZP4rVQO_YgrJ0qMUyVhRLAqTT7kOuAq6h4qhA6WwajsTbgx0GYCFM6SCUg6s5ie4mXgTzDaze4zu7hJl0Uo3eix7VDkPceujr9hdeNR8pKVaD0DRZgnOv7trr55WK8bDeT82MXF0vbxfvz4hzUTYQFQ7B0OvTf4VVcJaMJD8Tp0WIyXGjs_QUZ7vp0sLjjKbm8ciUaFt_mbRQl_kStjbllbrLTimEPG_xQZhVUwnCvSDI8cNP9LoC_ooYDq32wKwgDWqIpNcjahdqjyNZyGyW0FcP62Wrdd9Q0HvWOFMGea9mJXVxXLdwVkiqnKfRsB0QXcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=vRFBr5UyYm9W4kyRJWZP4rVQO_YgrJ0qMUyVhRLAqTT7kOuAq6h4qhA6WwajsTbgx0GYCFM6SCUg6s5ie4mXgTzDaze4zu7hJl0Uo3eix7VDkPceujr9hdeNR8pKVaD0DRZgnOv7trr55WK8bDeT82MXF0vbxfvz4hzUTYQFQ7B0OvTf4VVcJaMJD8Tp0WIyXGjs_QUZ7vp0sLjjKbm8ciUaFt_mbRQl_kStjbllbrLTimEPG_xQZhVUwnCvSDI8cNP9LoC_ooYDq32wKwgDWqIpNcjahdqjyNZyGyW0FcP62Wrdd9Q0HvWOFMGea9mJXVxXLdwVkiqnKfRsB0QXcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_qKH_xiHrdrHRlfBrkTI3objswcpNS1kkCOZF1jUUArYCY5iVVZTJZBxvP3RU1Rp6LcbwyFAUHBmS-bt0BaaXxHi4EXI6hPHl081--muZviuRPlCx_917O2g8iZiT6M9iBFb2lSH7fTlSBMqxq4kgE0c4Hbey5qG7r8E3qNvdAKnwAkvi27l4w8bldYl__NmBdaYAvW26L-o6VAPRt9kuVOW4_mLNjSQAeoAHBMS9FwfZZqwEWmtyDJBImF_kjy7k1nKd4_lBu6x3w_lB3q-sf_85E9HvKxtRYkOFpXnW7PGCWsE2rQ_-nM_U_r1NSTZStMSg2iyPbcYj6pkHFY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJMj3mAJE3Ir4G33bV6XA0GEyXH5EbnFMwAFXmw1hiPI8kLbfdOR_B4sMdzhoUrX2sOSBZkkUqBDJybXrKvsapuVc_nLgrTyI8rOTa_yqndUXxLhMfTXXFtCtq41KcCmKZLf8KGuF7AOeKPSkejvfkVHGChhPx8FvNf3G5lmQB-BLNFqQkSxI7PQ60QBYfRm4yCPyaELqw9W1ST_8FEh-PC6NRQTwgDu9wtFrYXr-WEtGRqBLEFGVTXZhuYRniLt2OM5lM7G2lLF_u7ca89VCVQHNewxMIwzQgdCqzMYLjpJSr9GXNR8XDHy87eOT3O39LCP6EHJohA7nU421xmp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8W7BnxqGbOLiZtnek5aICelEauX08rsAYtRpY0Pd9zTBe5wBVHUxRiNKjPUmnr-3_1eUr05I3a5YcUtvVgyPWrId7BpewexYiEqncfw4XVK2I5ChsdWx87TNljnsJigV4-yHlnh-3uY_AxM52-8PwUDgTTdqUQ2phueXoVTmz5jimmIyrMxHNK550xH085iIN89tGWcJ-d1Re8-BHHKl4v8PHK5vv2A4NKSj-KSrRD78EsPwxsVMrhSq4T6dgXcDp7CF_c8EMEMKuxVxKCqqbczxDSNQCdrDrd5OnPznJIQ1zM2quGXD1zlIzrEdlxnb4dbZUFArvCcgvaLtBOiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bReYRhxD9r-YQjR73jTJmspXLdhCrB0fufTtRlNacdbSURNoPh_3P-Tz8QFmdA-I2nX1bsJQlq4peig8FqHLmQZpnW7kh3OUT-TCHbPm_H6eHbVMDU8gHB8mYceqUUlb9aVwKAQI2X_efBP5in6i03ISLJyD8CyAgMoXp2bOyuxCYpgtCJvBWiA5m1OjSXCkMjj8DORyaMUHpJKY1TGE0ZL9vtNld8npdVItsOKcyh2iIPylYiwAxV8UE0dEtfiVPoYo5uy2Y_NB7hBDpLZLNn1pAmfs5ndtUHyskXbYeUKovIx6uZ-yinJ_anQWtnyld8kG1kD2D3dFDi3eQpG6aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rvpg4y1M7SsRdQ98M5Y1f4-tiFUI4iinfYqyPnU9mMogD_UiIlUg0lscpC34pIShrAGrSskc9Vi8ebO1bBk6WmrkN2qc8kdCcHLf6kRxDLMCytZ9Hb_G2xOetejNzrgloH71X1B7ijEOaf1PFbVbrea1Qe5BwbZdw8Fv0zupwX3HO-YtAUtZwkkKUmnZbXN9xXovo2Z5-Ya4TOrgysTwzMUK7mG77vpL7_FPIgPebG2XQkOoV3DJMXb3dzPITwCVvXnhc7WShSJnyVIvXyjARJ8ejL7oohmrH1vu4wsQ0zkpgV7X0nzVHT9EiltUmJ51oLXwEv4Sc3P841C2T00Meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeZEIRwJxWoR4nfR-4ioZYYyQxJ-2DvDceHCwR0bGeCrT0Zbc97pfeUXvgKQkSNoO3r0Yx1h0rJVoeHI27flJ3TtfKqecBq-I7puD33xxw7FX35OEnl_FI_42n8JEDzyzH7GUvoNJt4eUNUM1QXCTMGkcQLFADCwE5zb1TtXv8IO2Lv8oduzLH314F_uWsIaGxf_7dNzR-5X4tyUkjmZ0D8r-57p6anEZlKIIF5hjvxV41z1p5rbsqV14oP4Yku1YyORJK6d19QyOZXXdRDrhCNhJCZKBVjdZKW7e0kFEYez6BZapVGTseE34GOT83BTPkjqey7ipiGRosFpzALgsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk38KDy6znmqYVGv-nwJDpHoBmqOgvMwfc5_XbALGzBdRtJ9oJDH1219hbA6_54hQ7OQDITkEpGqO8N9a84Sa0XnJAkIujeMPB0kcIRMXBdjdcEP5z-OSVshQ6WHcHqm4RQ7XCgBYsLR1k9SGrGGwN4qdMzTRDWm91vTgC-z98vdjVcQwBdOqpBruu7kVlzxkusSlk8YVVZ23DQbm9LX3_kskdCUaU2LVyiKCNCoBztgUR0iFULKtYGUSnPdSDUbym-WWHf5cynTlMYB2wtMyQ7j7NCHMhz4VdCIlbQTJTWHEX_yBkbGwuZEO4JxUhTaMIKOBiIgx4g-dckV57qlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krAet1DFfkoFi3mUqzgbhb1N2jDs4CB5ZleEze0HKNzYz7Z70i4EH5RBMjymdnsog5SkKWrNmn-4gHdlnqnf0RwL_algxqWIBKZ85GqOjAUXK2X-m3B8in4ilWEvnSQFTRZ8Qt4j7LcoWHOxEwR4vp3v4eSflMpa4SL0LQeHPKDE9Zcw2dn3ukqsHulO2GnSQ3Oi4EUSaaCbhRtWHriOeCwA7sMOMQsUSi83tW_yuzx8a8yD6JTCPtLWBKi4u7anXKtwo6-ouIdYvrCzn911KW21Xn7k4-hgunqr01_JMc5_Sp0UXO9_XOJ5yO5ZSbor_pUmYV9ut5xSnCqvRioh1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBw_dHZXH-m34UbgDeRCx_keIRU-Iu4yuM-RLijU2TtpQL2SniQTlz7WzOgvXs-s2kWLIM-V5DdIXRP-ajoVq1HKFkDixgSLu-LJKgCB3TO1amoMBwnvhpJDbohLowCMe-FlYWDsNEk11DmEAoOovxiK7C9rPcVahBE3z8dodZ3sgc8kUtv4uu0HckmnWerFjBJVPXNRtaV9fDtJwjegN4qIcEZK-QxX2HIBIhUGASzyzW6aj1ZL3SCXohFy7-zqDOw5N_3wbdpxWaVtPVa4UokMwg1Ig6CkM-YbKWZNxqwD1gBSPwESkVYsuOQGyNGKj5GvcG7NeK24zXA4Rbs5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwCj4sXjjG2ZWT0327x2A1YM63b8RHzPGmk78SQ_hDHsYH9PTTl4ZHFLTSnosBPV9TTzQ0JyNt2wGDyFfQnIzZjBz9nv2RblbbMSvUVJX7jg4bR37-8ddfmFnkcsVNLGipb4VXv6Hdw0yl_XbQhrAGX_jGeKL9EPMnhcPuXpqqWwdBzo2u0nmKCTWdPbKVKh6wHEqJ32UKvWtbU8BydSmiZ3p94TOIcpTZulCuQhjGjxD_D7bwkSe3ovR8zMvcTB2qlxQBnWCVHYHrEso3dN7XIsxcuRdAUL9FvO8VMvsEtY5-84nuGud9OmcsS4KPmmBvM8gyfPKl1Ya_CFTSW5Sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVLproieiYIWXoonAb01ErmIyPuxEdVZw9ny0Qm71q_UlaJ8HZ3ZqPNBDW1_QjOGsMdX0iK9o0teFe6m46XQiLJuF9ILGR80qQe33l4q91WBRUlyrwI7tP9rkGsCE3YCB-Kj8jVsr68kwQeBieVMSNfugQowykQOC7mo0GLjslKTcLRyivFGXLJeraYfJVR_PIqS_NvQzA53PeEIhC_I1brphh70TCah5L5AB-rQdvZpZmfxKTd-vKJ6JdmXPJzi4U5XxUsFondgjiMin-TlS63ryG9ZycYQkIq24GJIxR0mEkBtTc34GFIg2ki-vbOMmIyH2CeO93OBCC6xV0fhBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=MGZV0_WYJ9UVQ5fkvHxRAcewPzTQTmjQIxZOOr1gbQX4JhX4mazbZEqt-fmZcvES_o93ykIUhqKKFdWbHp00iuPwrI8xWepXnM_rTx1c3EuzSYnborsXzt7FLx6CmL7j1qEV23l9Zx4Dgi62zHTb2v46FzFxrqwCZtoyL2jlmrK1ASFQdcD51ZjCT1IVUgMWwPHOB90H6NkGZOG81dBR_jZ-aS3JKjWnmnjXUrPfX_A-XKyl34tn0uVObM78bR0vuX0X9c39qpa5ibcaes1n7yOhQoVJxn0YV9L8zEEGsJOF17n7bgpx_t3T1lO8O6evXgAh5osB4Zb47OFfC4GU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=MGZV0_WYJ9UVQ5fkvHxRAcewPzTQTmjQIxZOOr1gbQX4JhX4mazbZEqt-fmZcvES_o93ykIUhqKKFdWbHp00iuPwrI8xWepXnM_rTx1c3EuzSYnborsXzt7FLx6CmL7j1qEV23l9Zx4Dgi62zHTb2v46FzFxrqwCZtoyL2jlmrK1ASFQdcD51ZjCT1IVUgMWwPHOB90H6NkGZOG81dBR_jZ-aS3JKjWnmnjXUrPfX_A-XKyl34tn0uVObM78bR0vuX0X9c39qpa5ibcaes1n7yOhQoVJxn0YV9L8zEEGsJOF17n7bgpx_t3T1lO8O6evXgAh5osB4Zb47OFfC4GU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=inXRHe0nFOoMmFLL3OTahbjgEMDPC88IQNDluTczC2_8H_g9uvx3QUZgtka7tOQJcYpUl1h1LbmXNTj0pzLUBVvVupTRfI20KsPiXs2laVV8MgPhf4Sbcmx1Oxgm-s4HYBuc3NtNdaF7rCL6-L2i2n9vIOQsWOpDAAkdxd-TjiWM6yT2co9ArJF0QEN2Pd30YRRnrk8gx6PNuy33rGMfbD8QLLNriO0ZotfAKMUn0u2gHnjzlpWJGNDVQk-23Js8D7JP8WKBcTmACBb4DPhth-vCvkMdew5OTzQcuLrJAGYcnyS13vw5MxFYkNSoC5OCJWEXmr_PVxsnY9e_5J0Rvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=inXRHe0nFOoMmFLL3OTahbjgEMDPC88IQNDluTczC2_8H_g9uvx3QUZgtka7tOQJcYpUl1h1LbmXNTj0pzLUBVvVupTRfI20KsPiXs2laVV8MgPhf4Sbcmx1Oxgm-s4HYBuc3NtNdaF7rCL6-L2i2n9vIOQsWOpDAAkdxd-TjiWM6yT2co9ArJF0QEN2Pd30YRRnrk8gx6PNuy33rGMfbD8QLLNriO0ZotfAKMUn0u2gHnjzlpWJGNDVQk-23Js8D7JP8WKBcTmACBb4DPhth-vCvkMdew5OTzQcuLrJAGYcnyS13vw5MxFYkNSoC5OCJWEXmr_PVxsnY9e_5J0Rvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=mX_PQzX04U-3-UHc4ctOrA2zrOuzNFcua8tSBiLf1kgjEZHksdobL3KVS_TbgIK9OF-11gy4mzYq7wAOF5uzruHLcPeZjdMfJ1hgYQ25Cs4hkARwupWTDId22XjAnPJdnxoGk7zO27wnP73tKp0uWbr9BszzBBh4a4H8wDURwgaBcb5taLum4mwTjlt2pO9BJ_t8PiBf5WGsD68SJQIqoRqvVzTObYK601-5Hu6T5KyL3XxTRITuiMuZJN8fgIbaO8xdV2CoGHeZ8EIN5QyYLDQThkOTH4SBXgbYFIO4jOTiXXjCmIiGRU1b5DwgVpJObGuaggl95PBHdIrqZB9suQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=mX_PQzX04U-3-UHc4ctOrA2zrOuzNFcua8tSBiLf1kgjEZHksdobL3KVS_TbgIK9OF-11gy4mzYq7wAOF5uzruHLcPeZjdMfJ1hgYQ25Cs4hkARwupWTDId22XjAnPJdnxoGk7zO27wnP73tKp0uWbr9BszzBBh4a4H8wDURwgaBcb5taLum4mwTjlt2pO9BJ_t8PiBf5WGsD68SJQIqoRqvVzTObYK601-5Hu6T5KyL3XxTRITuiMuZJN8fgIbaO8xdV2CoGHeZ8EIN5QyYLDQThkOTH4SBXgbYFIO4jOTiXXjCmIiGRU1b5DwgVpJObGuaggl95PBHdIrqZB9suQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=Iob2QYWnSYnnDMk81KdOvpwMolMEvJ8L_yJv3o9mTW-Nn_7fc6md8oBQ3Eri4QYhaWEuUd6M6di_7syoewdON7DFOx-DNo8H55YDYqDQ2VcVE_AEC9mb7QQpV9AJiV4RZKAtHJtUYNW5B_a22XrEtprxSpP4dYBpt2pB5EZ7Qr-DteFWWvxuB8JfWAiKBmLs0LYfmDlwYFvWYkNC_NenhdwSZRyAW1saPe8KayioriaGPvl62ZRogy7v7HEXbdv2fn50j6Qx9y5JrQUg2i-usTCKFspAkd7tuWjt7UnYEENF2ArnvXhTv2Fk2aNm5VF1YiRssD1E-lyas6fawJ9qIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=Iob2QYWnSYnnDMk81KdOvpwMolMEvJ8L_yJv3o9mTW-Nn_7fc6md8oBQ3Eri4QYhaWEuUd6M6di_7syoewdON7DFOx-DNo8H55YDYqDQ2VcVE_AEC9mb7QQpV9AJiV4RZKAtHJtUYNW5B_a22XrEtprxSpP4dYBpt2pB5EZ7Qr-DteFWWvxuB8JfWAiKBmLs0LYfmDlwYFvWYkNC_NenhdwSZRyAW1saPe8KayioriaGPvl62ZRogy7v7HEXbdv2fn50j6Qx9y5JrQUg2i-usTCKFspAkd7tuWjt7UnYEENF2ArnvXhTv2Fk2aNm5VF1YiRssD1E-lyas6fawJ9qIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8NwRTXNe4NGP5vMZegg3it8aVW67aH_8dVGIJEkuX-X33YEvtfABPQ--FNyn6eS2efdHunp1I50ZQgXIzEWcHqTvNHZONgh9hzXjFkEcDDycDI8P11QSZpHRVKXIhKnAD25qCUvUJX4BlnMMqRRMtaAbwWAuJ4IfnezrPwybO2cMCCh5OhLu_ZxDvWuMLyLtJ20kGa7qE3SXKqkQYSSpqjcZvo0VVNNvCkgLH_D_pKaf08ZxcrGWHiDH5PTny1v6pdbGDdlGvHJ34NjHQJNSx7FXmB8L4ejNB69D4oGaMUbbOMHsk7XkSOHCBwkiRDgV4xecYLhwHfrvg3hR-lNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxqgZMzsEJ6aIcxHe6T8o8cW8tjMNv9Jk_43aQif6xTIqNin1Vbpwf_3O1ov-Eao7A4GL6o7_Ty82QVj3k_nzkh0-e6ZNUwPlcqlpbZgpItCNox87-a4aVbqSLJuZP9OzuP6TKfYKj1d2myZ4VGk6w2msDokXeePYOY4Gz5A6I_vzrIwlgp04Tdas9SAgQphffqkYmzn1S0vBWajkszLtmACyeSQ1sFn1q80ZFKf4xi2Hut_dNWLWgaeZ3OGL5pPxpO6qShtyT9qvyBgx-x77qw8EM45ZqqPdWVStiTVg8kIO65ttFC_2oz7dpqd6i6jNxY2limN_gbZplYCVqAEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHmSo4ohHuMuqxxLjifz6fF823A1FNryFamiOS6OXIPEdj2qOjFfhIJziVbaLYBD8Hr6MHBoDh1jnd6ts65wmXD6ER3_gYIfrufltvFgSFwzNttNirfn6ZT5W1A9LrtydkOf2-BKW3ivf-keznntl0gholHXTphTAnRa4MAPEL2Z2HkmMIveS8R1o8Y5qltWNaZkW-DwnxidOGKX-OFdIFEuwxU1ZsgeO4LXDzlRmo5zbVGqhNOIAmKBINigNk36NKWl18Blbahcucul2x0sDsOJFc-ycmUCK18LJ3Vv6aBHvO8cq-JZ-wC-COVwQImYm8hkFtIrJEAvZ1NdRU0PlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=VHFHTqSEbUbT2P6NWLQOHHCGhgNMfmNIpqQK1xBLSXP_l838Ab2znBxWaHZIKsNfBiBuU3nylO8TOp7onNff1RrwttXe6hLyCKQ1s_0kteaYbYR5schZ670EgdZL46lrFRUCS8AsvaHULFpOo78uP9-Cbq4DqfTQwsy9Ja0n0mkyN8lg-_1IdlQ78SRbZpC71HW7G_aR9lWtM3PtnwFMDzVPfPlnTKETGqeoMc99QqkoJknU4uM5oImSU_W76GBD-MOcCNYjj9evEJe1_8ITUBhV16wWc5NyOiVcF4u8XLT-7v5dVms7f0kJacnjTfAIjSjcvWPvNZmdfkhkKXBKOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=VHFHTqSEbUbT2P6NWLQOHHCGhgNMfmNIpqQK1xBLSXP_l838Ab2znBxWaHZIKsNfBiBuU3nylO8TOp7onNff1RrwttXe6hLyCKQ1s_0kteaYbYR5schZ670EgdZL46lrFRUCS8AsvaHULFpOo78uP9-Cbq4DqfTQwsy9Ja0n0mkyN8lg-_1IdlQ78SRbZpC71HW7G_aR9lWtM3PtnwFMDzVPfPlnTKETGqeoMc99QqkoJknU4uM5oImSU_W76GBD-MOcCNYjj9evEJe1_8ITUBhV16wWc5NyOiVcF4u8XLT-7v5dVms7f0kJacnjTfAIjSjcvWPvNZmdfkhkKXBKOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbzFO9203sti-e0ydRtSyl7RW9mdjeV0JmIYvIwwHZ7A0SUZ1A9t-9hK27_vS6t-dNv3AaJyUlK0VRBORoMJ5jw0F-_GFYEOY06kz8eH0fufTjPbq_adKAwB4CmLnVFMqJLFdHvQ5WRs5iuCwgeM6RAc2cALMi3jlgzOi-2vbesPF4IyzEId-Vz9oZZftEzPg3MIltoxEOPbrRCYesnIAvUel0cMyPsTA862NfbbD5nWseQ115SxM2qiZ1q9QIeNJ9VXFLaCronZLajlJlOLjv3Az1yFiQyfvlu017TvCgKVQ4a8XeVHwh7zXNXTp6iz8WNovzIziUcsY5w11YhpuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=T3e6926fYsRqo1APeUMsOkU6H5WOLAFmmZjd8DAGh9F7M5lRfnRB3EHRFLFwCS-skGagqO_f5Tazq-s24WV14e5jfwNNNjJIiaB8QsVRBpQ56IW9CcQClxnMiOhC9IEY3n0FHsDVnoz8UjZf4HXrP2qSSVvCNAS9h1-99LOihO0cFURj_IOZpt3f9KtTsuJd796RhcFy0FSJsNCuHl_ONgmHenz7kzkx2pZpBuVgQNUJv4fFzW70kqvux3TFJoIVME1zhR0M47n3CFvrDhYFHCfBm1G_TEblH6xsaqb1gTZwQVTQ0Y8oUO4z_9QVHb2TgyomqwHS49t44gjzhxhTOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=T3e6926fYsRqo1APeUMsOkU6H5WOLAFmmZjd8DAGh9F7M5lRfnRB3EHRFLFwCS-skGagqO_f5Tazq-s24WV14e5jfwNNNjJIiaB8QsVRBpQ56IW9CcQClxnMiOhC9IEY3n0FHsDVnoz8UjZf4HXrP2qSSVvCNAS9h1-99LOihO0cFURj_IOZpt3f9KtTsuJd796RhcFy0FSJsNCuHl_ONgmHenz7kzkx2pZpBuVgQNUJv4fFzW70kqvux3TFJoIVME1zhR0M47n3CFvrDhYFHCfBm1G_TEblH6xsaqb1gTZwQVTQ0Y8oUO4z_9QVHb2TgyomqwHS49t44gjzhxhTOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=kW33b1G-3XOOWg6HlAyQ2WvZqAjvbvJ8qH9NEUZTwFuUL-PEndc-RBkcRVu0HTs7F-Kh9HfjZjeiIx2rSir1e1Yk2E8k4_gL_yNGif0NKGtdwHll3MYHt9iHiBjHovCs1gTWJrbbNM_y4R-cUfWPWPLIkilJjBzxB5GmCUBdAtcBbr8atIaLCsmPwc3eY66BKADwlxeNv-6jkODFpoPQ2PG_WTxQjUOvduZSg7HGp41EUMLlb-BriwkF6RmTBQ-ZObwDUNxn2vdN_-72BLkZ9MC9os1y7cQq92hu633HAXFH3g0NH6f-p2Xkg0gReeyfW3aXupxteQo3nmEpc5OmQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=kW33b1G-3XOOWg6HlAyQ2WvZqAjvbvJ8qH9NEUZTwFuUL-PEndc-RBkcRVu0HTs7F-Kh9HfjZjeiIx2rSir1e1Yk2E8k4_gL_yNGif0NKGtdwHll3MYHt9iHiBjHovCs1gTWJrbbNM_y4R-cUfWPWPLIkilJjBzxB5GmCUBdAtcBbr8atIaLCsmPwc3eY66BKADwlxeNv-6jkODFpoPQ2PG_WTxQjUOvduZSg7HGp41EUMLlb-BriwkF6RmTBQ-ZObwDUNxn2vdN_-72BLkZ9MC9os1y7cQq92hu633HAXFH3g0NH6f-p2Xkg0gReeyfW3aXupxteQo3nmEpc5OmQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=NlvlXoQtIf7Tl8TB1Cbr0R0xqWMXcXXAJysOV9lDEbwHronRZDHJqGoHVcXS1wT6X9hdxnKJbKtuRQIMMzItMR-XHFzio0qsQ-ms6hrP_EHtWorqKOw0X0E6qjWuDPG1bLWsjnZHmvIQX-4DKFTsWwCPRio_3t3axY1pnYEjLv7odUL3i87DO_lEPWwk5yLeQrZgWnK2C7OTtbJpoBjl0kECkZ98bvcV_dH-AnQHdIqGSXMDTvYGgSqGBRHn11GUeOt9py7enSl7glhbrC8_tUPF4etKLkZNQceAh2_y4y3zvPfGz3VIl5-g3So3dExXDbesWrdCBX8LyJFkSB1xdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=NlvlXoQtIf7Tl8TB1Cbr0R0xqWMXcXXAJysOV9lDEbwHronRZDHJqGoHVcXS1wT6X9hdxnKJbKtuRQIMMzItMR-XHFzio0qsQ-ms6hrP_EHtWorqKOw0X0E6qjWuDPG1bLWsjnZHmvIQX-4DKFTsWwCPRio_3t3axY1pnYEjLv7odUL3i87DO_lEPWwk5yLeQrZgWnK2C7OTtbJpoBjl0kECkZ98bvcV_dH-AnQHdIqGSXMDTvYGgSqGBRHn11GUeOt9py7enSl7glhbrC8_tUPF4etKLkZNQceAh2_y4y3zvPfGz3VIl5-g3So3dExXDbesWrdCBX8LyJFkSB1xdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJW5PIMDIBQT8ON6XP01FJJk4_WGw5nrGxupdmBBN6cFGTOSzsqCi1wReHZ7LV50aAujOmxmsqm7XDNdmSMN-VEzS4Y3vmgq9AjGlO0QVm2fhsj5jgLSqA2opBkEADJiRV9RIDpFoS3I1ok-bJaVuXPe46I-zgBezYLbtoWs6-PHw_cOWI1eBy40-bC6lvH3YMlLJNTKAHG2kI_KKLMci1NqdLyyBz49otqy_hcpVDQW3eqnU-iZPQIQ45dX_kXfAf-V5xonzY4iPcE7ViHx4gIhsCJTevAdhk9Fx-0GM7mA7V5phBMqCag3xULSgg4zi2LVHxtpYu6hWh7Tpw7d1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=l9RMqKhL_1cQq4Ukw3f0X55o3Eey2y8_0Tu6jnA5pMIqsb8UgEPrvaz4fDLpxD53_AtBLQE2L9Mc8kmYhxTgPIEOpm-jKHUqP07u7rIYomqkWpLjZAQakPIBn7wc92wyTSOIqFnj7T4YvPY17JI8fN-waDRaJM05EkG5vNQm5d_vN5-U31azs_HiCtrrTj0kupKEfSiQoIndcpwQKGdM6iT5i5Ql2KcEq8rtW1XTfsJU9qq69Kp94ZsBY_LhtxH8NecSOQSc2RRnmcHQ0YritNbcIkUe8I0fozzqCwO1SE00igd6VBSpAK5YocdrOMqDvZtHnln8wILcXqV_Q4Oh9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=l9RMqKhL_1cQq4Ukw3f0X55o3Eey2y8_0Tu6jnA5pMIqsb8UgEPrvaz4fDLpxD53_AtBLQE2L9Mc8kmYhxTgPIEOpm-jKHUqP07u7rIYomqkWpLjZAQakPIBn7wc92wyTSOIqFnj7T4YvPY17JI8fN-waDRaJM05EkG5vNQm5d_vN5-U31azs_HiCtrrTj0kupKEfSiQoIndcpwQKGdM6iT5i5Ql2KcEq8rtW1XTfsJU9qq69Kp94ZsBY_LhtxH8NecSOQSc2RRnmcHQ0YritNbcIkUe8I0fozzqCwO1SE00igd6VBSpAK5YocdrOMqDvZtHnln8wILcXqV_Q4Oh9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSXDbTdhYMNelfTjcECX8dItBC2TStIhoKisf5tdEgPaKiGyt2SKkCAFI-c2Jw0Pps4ljsOoxE1rMlvJjJuMbzCzfHifud2WWbPf4AI0TPf9oLnhqo0epGXbJJHuv30I9vPtKRIfPWH2VGAG-OmE_gea9KxaYyFFz2rmwYkAoe90mK-I8cx1J8-RY4oOH3EBpVV8fSS3On7oih65CW2PPe8w4qLxmcwS2ggTGBeCepbJYz-Mttc_qjWhLEA7QkBWdFrOX0QU7Dv2FSINYTeMkJjZTDq12epRClWn__uBrG_QlE0sho9wPTW8VwqqwzmDTbHSdxQ3fUT-muEIwpQ_SPLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSXDbTdhYMNelfTjcECX8dItBC2TStIhoKisf5tdEgPaKiGyt2SKkCAFI-c2Jw0Pps4ljsOoxE1rMlvJjJuMbzCzfHifud2WWbPf4AI0TPf9oLnhqo0epGXbJJHuv30I9vPtKRIfPWH2VGAG-OmE_gea9KxaYyFFz2rmwYkAoe90mK-I8cx1J8-RY4oOH3EBpVV8fSS3On7oih65CW2PPe8w4qLxmcwS2ggTGBeCepbJYz-Mttc_qjWhLEA7QkBWdFrOX0QU7Dv2FSINYTeMkJjZTDq12epRClWn__uBrG_QlE0sho9wPTW8VwqqwzmDTbHSdxQ3fUT-muEIwpQ_SPLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDbSWVUaeRDlavj4EdFJYqMlg93N-N6uOsGYoQ51x_VgPQ4IJsbTVoWVxHwZWmtBVNkOXPqmYyZgykjJ5Fv_HHIFTMegKi4VziDxoq34rUcHN6_qbg1wPuwPnvqiaNlgz_6N9I9Pb1DFEwKFY-fgR0NK3V6BoR3WQLSiGbJCrgfG8c9WpJWEz5007EoNgYRKuHZp-DVAigHT7zDmY3pA1DK8d4BtTu9ceQkHuSweRv4TuqWFsifa_fhXSbwKMQ2gdrNGpnzDdInICgOh4Y8zLrpeNTuSQeUph9-6r3DbVMDzQANoFjKNH40soafsnN8Cq3LVGUMXrV4mrT0dCOafxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=ua1XbAQejM8YCS8TWT9P6xIIJ0BdasLcPycbHsi7iRdZfwOqIfLvm1ZsZHp9rK5vHRXItKNtTuELuTbBIrfSA1SClwa3M8xxJflmhFqjJG45ts9gg-u0zK_bMABJ0RjZ2YvOh6znXPkpnW6-pKCK3ja4dhD1Avk30jEwx0wmvUn1ygDLyFzrARSG2JE1Sp9O6s8GpYvlqmsGbykHIaCopBVB_h8fwhVNhcVC61q8cfnEX_aF14grqeptbbuTd0t8bV0kauX_-TVxdSSV86g1xPcjEn0yGpN9Jvh4bJ7Y1eox4Jw_awqG2KbuuD5QPAZvMfF34EHLoX2TOamRjmzaNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=ua1XbAQejM8YCS8TWT9P6xIIJ0BdasLcPycbHsi7iRdZfwOqIfLvm1ZsZHp9rK5vHRXItKNtTuELuTbBIrfSA1SClwa3M8xxJflmhFqjJG45ts9gg-u0zK_bMABJ0RjZ2YvOh6znXPkpnW6-pKCK3ja4dhD1Avk30jEwx0wmvUn1ygDLyFzrARSG2JE1Sp9O6s8GpYvlqmsGbykHIaCopBVB_h8fwhVNhcVC61q8cfnEX_aF14grqeptbbuTd0t8bV0kauX_-TVxdSSV86g1xPcjEn0yGpN9Jvh4bJ7Y1eox4Jw_awqG2KbuuD5QPAZvMfF34EHLoX2TOamRjmzaNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTOQhaLd1mwCGTix-0vt2bMENfqcAmESBYvAEoKzSGel4bgrtfTL1pttvfeubSfoCMkarZMSxbDESqX7BjaU8Z2we_8qyCPV5IycCDSuv-5S5ogsTNFs1-2bDQiEUQQsctTJJ31JrubpJ01KTJQIgirTadt3G2YaK3kq1qL3zgFtn-ms9YKQMInVpg6oL6P8PM8aeVW_cQOtuga15LHRbRy0gHqQmGKyKMapxTGnZkbC2PTGoaC7ATuiGLMx6LbeOrRPDuDsCpR_wRE5Usnmp6yO-gB1fTqJqxVDfAtizmyU7g5ODyDx8c6fc-sHfPKwv4fIHfcW6ArtaTfMByhicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=cuYYTkiR8nUwZvgHNRY4yEWxwYiejHRntnvb9x7Y5neWfnHTpjWAgi1fl5372GHW4GgUQgUZbxLhMDIrf9KxU5Qo9oH1uQWkXxbOKJ1AWJf3LUh_qQveZuLdlzvBrXUKyb8C7pR3mcN6x7dlmCnjV2dFrJ7jztQMmeEAR05wJgCXJSB4IwJCF2dRS5Bfay8HHlLUKY6P7E_eOnO8uS67crI2_i_U5Z0xwHlFj6AdhYEKFFkyAtgus9_SpS2DyO-ZEGSAI4YOqNslnwx8lORpVWrv_3KfwrzV-3gpBpY5sinhE_FiXnZ_gKWzBdhxQUIIPqcn2RYqsyqRzm-SKMy844i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=cuYYTkiR8nUwZvgHNRY4yEWxwYiejHRntnvb9x7Y5neWfnHTpjWAgi1fl5372GHW4GgUQgUZbxLhMDIrf9KxU5Qo9oH1uQWkXxbOKJ1AWJf3LUh_qQveZuLdlzvBrXUKyb8C7pR3mcN6x7dlmCnjV2dFrJ7jztQMmeEAR05wJgCXJSB4IwJCF2dRS5Bfay8HHlLUKY6P7E_eOnO8uS67crI2_i_U5Z0xwHlFj6AdhYEKFFkyAtgus9_SpS2DyO-ZEGSAI4YOqNslnwx8lORpVWrv_3KfwrzV-3gpBpY5sinhE_FiXnZ_gKWzBdhxQUIIPqcn2RYqsyqRzm-SKMy844i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=tF7AA9Mle4fQMiw-_WyaBUYxnn7o77gEw6kgPSb9UhSmnBnRigIGuHpIrnpWJ26TvNsuv5WTx2Zx8WyzrYVj-Ma439Y6SQgpEbeVwQdcVNAR08clI4P-wR4pt6RxlmJEyiEq-2ZqyAWkO2k9snQwqYEcaJJPN-5u8d-kqol1LXP2D4z3ApZMjKo-RkcdzynKA1bAAblrY-awki1MRi-ZMz1LWalJXw-lMRwm0hEB2ORO9hBrVO0c4xsc0a0Xb5dr7a23Up6MRVOSJatAj9iyVWkE7CsBOYXeiJ2X3Wo381hwunjC90GcB8IEv6PbPDTpLuFc344Z9bJoe8hPYSMqNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=tF7AA9Mle4fQMiw-_WyaBUYxnn7o77gEw6kgPSb9UhSmnBnRigIGuHpIrnpWJ26TvNsuv5WTx2Zx8WyzrYVj-Ma439Y6SQgpEbeVwQdcVNAR08clI4P-wR4pt6RxlmJEyiEq-2ZqyAWkO2k9snQwqYEcaJJPN-5u8d-kqol1LXP2D4z3ApZMjKo-RkcdzynKA1bAAblrY-awki1MRi-ZMz1LWalJXw-lMRwm0hEB2ORO9hBrVO0c4xsc0a0Xb5dr7a23Up6MRVOSJatAj9iyVWkE7CsBOYXeiJ2X3Wo381hwunjC90GcB8IEv6PbPDTpLuFc344Z9bJoe8hPYSMqNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=AozJgT9p-qBp1RvBpLHGzB7HRMi56IudldhfJ4w3vQdbaMo1oTQ4mo2xXUdQdoxk1XiUPvG_dnY2sLxLDmWHmgN56loyTSXX0G7E2hZci_bOcoAY6q2XdUn8DkR_bV5wwlgKfwOm4NQaoZ1OzwkKTlBwSlWyfLTLB-0HveIghL4hMSs2zNGba8oa32QYRl6-japGaHEHqYNtJ9tQTqldZgdSOYvi5DwkkltJ0Q04Sk8BL0tIAspyiN7cDGopBvp33YHgnHys0K5IXzavsyjjHRWD8l2G49tE_X_9YQa0hO2WQ1toapwFk6jg0S7xBnbZYRRc6Q5VWN8sKvsf38na7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=AozJgT9p-qBp1RvBpLHGzB7HRMi56IudldhfJ4w3vQdbaMo1oTQ4mo2xXUdQdoxk1XiUPvG_dnY2sLxLDmWHmgN56loyTSXX0G7E2hZci_bOcoAY6q2XdUn8DkR_bV5wwlgKfwOm4NQaoZ1OzwkKTlBwSlWyfLTLB-0HveIghL4hMSs2zNGba8oa32QYRl6-japGaHEHqYNtJ9tQTqldZgdSOYvi5DwkkltJ0Q04Sk8BL0tIAspyiN7cDGopBvp33YHgnHys0K5IXzavsyjjHRWD8l2G49tE_X_9YQa0hO2WQ1toapwFk6jg0S7xBnbZYRRc6Q5VWN8sKvsf38na7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=BpEjw9tascPk5HM8g6aIgtsWuEm_0b7z_tu4SGYPd6SPSTetMeXhQZ4EwoxgmD9j2IceLyzWdpCroq1geh-aV4pxlgzqvjr-Y827BAhNk1glFQ6ZmjMeVOCq0xGAMd5Ea616TaaLvI_IwVvW6Amv_tA3yLnLNXpkxJf0_P5Bm_6M-P7jdiFvqx3JHI5UyzfBn0AA6tEBqbIyB7F1j0acH_WbuXAymbkDoVKDY6pnT2q4znX7yaQPQYwr0l-s_t-8QP33g3wbISdgfXl6TnyhqansZPlJoo5ykslwAvdQu50QQ1wJHMVO-P6ZuWffEEb5SmHMK1iQOkVWHaVG3N6eDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=BpEjw9tascPk5HM8g6aIgtsWuEm_0b7z_tu4SGYPd6SPSTetMeXhQZ4EwoxgmD9j2IceLyzWdpCroq1geh-aV4pxlgzqvjr-Y827BAhNk1glFQ6ZmjMeVOCq0xGAMd5Ea616TaaLvI_IwVvW6Amv_tA3yLnLNXpkxJf0_P5Bm_6M-P7jdiFvqx3JHI5UyzfBn0AA6tEBqbIyB7F1j0acH_WbuXAymbkDoVKDY6pnT2q4znX7yaQPQYwr0l-s_t-8QP33g3wbISdgfXl6TnyhqansZPlJoo5ykslwAvdQu50QQ1wJHMVO-P6ZuWffEEb5SmHMK1iQOkVWHaVG3N6eDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=VbAzyZl7xjFC1FZT1youL-y-S5IYC9IwsyhSvsXu2L1rnszcI8nvBfC2_S9y2qxK1PgzZhJiyFHEn_d6h2VJOFXKPXUsYmD4dNcTaiPnLmHKSeV2FTNnh8AYa4btlT9-Lq3ntDINWa_yaXcoQDnEcnB631m3fBIoSPnaU2mJS0o5le3iNq2zqTkO0kIeA8KOwiooRjLwqx95GVzPKYAU2vhVpj7R6LV1hFnYoU90NlY0TadXJZqUnoNIc7u6NRgcGluvxY5Rx9aYlXikzGbNT9gBiXEDBMcRsRK-yfrRlRdD5XHRO_UY8yE1Wo2c1gQtXRvbdpOFjeCLwHMCMGc3hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=VbAzyZl7xjFC1FZT1youL-y-S5IYC9IwsyhSvsXu2L1rnszcI8nvBfC2_S9y2qxK1PgzZhJiyFHEn_d6h2VJOFXKPXUsYmD4dNcTaiPnLmHKSeV2FTNnh8AYa4btlT9-Lq3ntDINWa_yaXcoQDnEcnB631m3fBIoSPnaU2mJS0o5le3iNq2zqTkO0kIeA8KOwiooRjLwqx95GVzPKYAU2vhVpj7R6LV1hFnYoU90NlY0TadXJZqUnoNIc7u6NRgcGluvxY5Rx9aYlXikzGbNT9gBiXEDBMcRsRK-yfrRlRdD5XHRO_UY8yE1Wo2c1gQtXRvbdpOFjeCLwHMCMGc3hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=W57Mr7HofgcJsCBIq48mI8ovGVorhbRC2-etg6fVnpO1HLUsSgVshGaKa6Qly-tOpC6lbt3S0uN6xIIDCf2NSkAs7mA5R8j8aJL_eSkb90XTPhigrUYVyHLaeTSPNNVlgJndIi9GcHrLy4DL_X1rQ3ThC83QM5zWoX7DXWAD1svDL2YEQGoceHKMVSTH83q_X6Gwi2ekhlEQOoDbQ7LuTNDe_c_s5bPW0G1MLuM-pa2Twpv50-RsK8Z7uNJYFz9uNCF42nqyxNkI8KBFx4dpldDCsVQlrHdOJRaBPWiZGf0FdbYzWzFI-HrCk4_zAb54o8X6cCn8gHWLbZ-u8glrbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=W57Mr7HofgcJsCBIq48mI8ovGVorhbRC2-etg6fVnpO1HLUsSgVshGaKa6Qly-tOpC6lbt3S0uN6xIIDCf2NSkAs7mA5R8j8aJL_eSkb90XTPhigrUYVyHLaeTSPNNVlgJndIi9GcHrLy4DL_X1rQ3ThC83QM5zWoX7DXWAD1svDL2YEQGoceHKMVSTH83q_X6Gwi2ekhlEQOoDbQ7LuTNDe_c_s5bPW0G1MLuM-pa2Twpv50-RsK8Z7uNJYFz9uNCF42nqyxNkI8KBFx4dpldDCsVQlrHdOJRaBPWiZGf0FdbYzWzFI-HrCk4_zAb54o8X6cCn8gHWLbZ-u8glrbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=hp6r5JtZfh_lI3V7fGN7O5aUXG04QGbu7SeHoGU8sngGUVXp1xcKwOtlwq2WseAGHCw8ZOjYJCy2PWBel6h_cnUxQ5i-UVv3_6YV_1QVckib3Y-YhRp7WetsK7x49wl7Y07imGbWQSzFeG72pTp35iVhZcfG4uyK7GgK9nsE8IAGHklgcsfw2IlZOW5uiuoqIPTPG4MKvwi0Iie49T-FHPZ4TACmUO5CPpvHD7f1RDcDlfIxngM2PkkMro8sDymXnR5JcKvHEFa4HfBYkbz60gmEF7B1sWliZAR_cwmA_FRVAkVC6-dhW9XPXc1--51OdIN-0wlP97PPEPFl1V64hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=hp6r5JtZfh_lI3V7fGN7O5aUXG04QGbu7SeHoGU8sngGUVXp1xcKwOtlwq2WseAGHCw8ZOjYJCy2PWBel6h_cnUxQ5i-UVv3_6YV_1QVckib3Y-YhRp7WetsK7x49wl7Y07imGbWQSzFeG72pTp35iVhZcfG4uyK7GgK9nsE8IAGHklgcsfw2IlZOW5uiuoqIPTPG4MKvwi0Iie49T-FHPZ4TACmUO5CPpvHD7f1RDcDlfIxngM2PkkMro8sDymXnR5JcKvHEFa4HfBYkbz60gmEF7B1sWliZAR_cwmA_FRVAkVC6-dhW9XPXc1--51OdIN-0wlP97PPEPFl1V64hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe679D-o3AuT1llNG6gULIsIXhyJY8wDQF1guW2z2gzxsxBUzWr2KmqD_65EL8MRtZbiSLSi684g5euWCL-KIiWXuvaydXVo7tobR_OT0egPhPMI3YD0sNtJRAPKRIIXp4nYpBUXUA7OjIurvO1pvpmBr93qiqbGE6USS6UgkQb_prz6Au1FA8yrqI1GC06kWDuJ5mLcefzLlKSQjtCDvmTL_C3cN5FQeoiDa-32F9Aj-hak1K0CgLp0bVllVnsxmkcWQiIhAZ2lQESh9jcWvYF0foNh2GhnFB9D1m8-z0onlPwCtcLXXh8tnawvk9oHKRwL5fdGS6WNoFZdG2XxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6EEhWhPUG7vg5iPoiHhFoZAAOFc9a3_6QjxBOvqAWzIeMaChMueHVH8ZEKyJ_ux9ImO2wpe-HTXidj66FrAc5RuNicLpaz8M80PvzXTIkNxY093nMWGwxeI63phO8xFgwIdtdJQSy678GXIhDQeQdW849YNeP6JEbZMfYfAVCPWl2RGNqz88gVFsUiliIdxrA8uEHVR6EuDreU-GXCVIVdekcr_SAOjKSJMwiovdJOrHA29jR9WRS8uXUz5zxa8RN6qV2klS1xryMldHqHSjwZd-M93RblvBSj9OV7FAUNw6sdhufgdXoWXkbjm4FA-K5sK9ty0GAIL-14HSTtS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEWr33Xi3YS5BmMM9czy0UEICnE-2CbZmmitOjM_qXvYAjjiDqjI1rSkb2oDR2QD0JinUrjpDOV0AQI7IZvZij7Qel5aHFL6oXFC96nVZyqtbfY2VESwNAptA5MGFP2VHp07ARQ5plR2_WJq2g0s9-fCQanfzwfLiGFIvoEteWKUpcJp6PHNTbghNcNqoB7anbBNph1mWkt5EGI6mkbNx9ngBj8-RS9Es1RC6sZfwSq-pYJCABw_S5ZhEDoGRffOjOwEe2GIvYcgtBvfP61ChubkU3o4cvdvXQZ4WlSPRtziikeWyQ7kyw8QPVX9GbdaTrAtZCykVbXU7-r0S15wnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=uBQtamZDdLxLu-u4gt356ZAE-2yvwwQs96KSEdVxH6D2WYNIuGghH85gsOWtPQj0sJimrvY0Zn0371kx1ppoTDXm4jJLHEe_bHVn3EK-QeWZ4Eo8Ev9jH3zKwDYqkfrqHPJr9Qr47M88WBJSM7Ow6Zb5E9_e_4sAme9b0gNQBl2NU-HlBvnRjtccTOBMnA8Tn6UnOBTcYUzj76ip_CzibLQMKYVGXq6dkgYDn9GatHef0D_IeHa_mEaBADM7OItkWAAB1CQPcJRprKfOe8BBPiomNOIdi1EosxHPTIlfeTl53_mVe2Hin95ZCKUHh0OITak9t--b8f3plpSP62qT8aSmhmKLTysGsA-XvCAsl7Z_ViZ-dwrgfl3iLpAJ_xRIop1VFqVgmW5UkVB1-NSIBwnxxEaZAs_70MD7a8NIM5svAhm3E_c_GdUKgvsQEZmG0EcIRYgiAGaxJSI7AZ2QotxSTNHrtHQ8Vtso9BuYlwznHYcMtskRFdvZuE_ZKI2iY8rOv1CgZDY939lwlY1Jk4Xf5xVyOjvMlvo2hk-3xZClhkckEKZ_DOnAdNTjkLlBzb8KKDgvmNayIjYgJhRtrXCVtxd-AhoSvBjZHP1aGL5aLmw5RBXfvX8ac2osiH0nM3I21AuyNUh0sKmQWdFhNQiIBTgT2T82dckcx8Ao2Os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=uBQtamZDdLxLu-u4gt356ZAE-2yvwwQs96KSEdVxH6D2WYNIuGghH85gsOWtPQj0sJimrvY0Zn0371kx1ppoTDXm4jJLHEe_bHVn3EK-QeWZ4Eo8Ev9jH3zKwDYqkfrqHPJr9Qr47M88WBJSM7Ow6Zb5E9_e_4sAme9b0gNQBl2NU-HlBvnRjtccTOBMnA8Tn6UnOBTcYUzj76ip_CzibLQMKYVGXq6dkgYDn9GatHef0D_IeHa_mEaBADM7OItkWAAB1CQPcJRprKfOe8BBPiomNOIdi1EosxHPTIlfeTl53_mVe2Hin95ZCKUHh0OITak9t--b8f3plpSP62qT8aSmhmKLTysGsA-XvCAsl7Z_ViZ-dwrgfl3iLpAJ_xRIop1VFqVgmW5UkVB1-NSIBwnxxEaZAs_70MD7a8NIM5svAhm3E_c_GdUKgvsQEZmG0EcIRYgiAGaxJSI7AZ2QotxSTNHrtHQ8Vtso9BuYlwznHYcMtskRFdvZuE_ZKI2iY8rOv1CgZDY939lwlY1Jk4Xf5xVyOjvMlvo2hk-3xZClhkckEKZ_DOnAdNTjkLlBzb8KKDgvmNayIjYgJhRtrXCVtxd-AhoSvBjZHP1aGL5aLmw5RBXfvX8ac2osiH0nM3I21AuyNUh0sKmQWdFhNQiIBTgT2T82dckcx8Ao2Os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGvWNnfLfHBACXzKqGsL4JVkLHykuN3mDTPtpu1UUsAzCYdwYbARmZY-Fq8hShUN0FTJTZtp-UbZo5TvwGheExu4wOsJuIXZPoI8Lal5ZZyF9TrVynBnTRokFLEkb_Jsgzv-XAY5Lp--g4pvB2ix-xEJRYa9tsYCeERbEwY530fpImsUlo_TIPiWceZE8r8-co1H9L3Yabzjny77pPTA-orqMgsdqd4NytaeN61PBtKEU6gB-vfX8MUYWlXTU1kPHuYCo92GcgLrmFSqliNiwqGAqfNy9LITwmgHdjWa63rzofukVsg9gBMKW8-OJ2PIqKtMOiQD34MbSXWLiM1-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=Aq0FSFXNG7zt96xbbVJQ4zWV-jJe71nP84PqrDToaD0mTAUjIiYQEoo7GfQydZUfedZnTQIHdNgLlxERvMKqiygyqpyKabdEN4wLUMQ_rgrObejrbnHUZzb2D8vSbzv-wodpiASEIKkmj6--gg0PQ0ji_QC031_eqYoiys1UwQEjRpi8phgfnPhr97HVkVz_5-q-tgUTn020uY9KYzpIETzo9ekq2p87daemUeCUKib_UqBWyVVRAt_oEEm2AeWnrnJxr8uQvDSd7CeE7GGtWKRXkkm501GA-hmyrYMr0LFy702R-rwH0hxQ76o1jObZkFWZsrI3K4xSPOR2C0cXag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=Aq0FSFXNG7zt96xbbVJQ4zWV-jJe71nP84PqrDToaD0mTAUjIiYQEoo7GfQydZUfedZnTQIHdNgLlxERvMKqiygyqpyKabdEN4wLUMQ_rgrObejrbnHUZzb2D8vSbzv-wodpiASEIKkmj6--gg0PQ0ji_QC031_eqYoiys1UwQEjRpi8phgfnPhr97HVkVz_5-q-tgUTn020uY9KYzpIETzo9ekq2p87daemUeCUKib_UqBWyVVRAt_oEEm2AeWnrnJxr8uQvDSd7CeE7GGtWKRXkkm501GA-hmyrYMr0LFy702R-rwH0hxQ76o1jObZkFWZsrI3K4xSPOR2C0cXag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=Wl4DMzk2L5rYNF1MVNtB38g3MGgccfDb3_4DWGdVJSeaIp8kvkE0MyCrYx7-ZCZiTms0r2KS2RktSIWZSpumkqxgiX1iNBfDImMeREtAaY6kOAvdRZz59TerEFcwwYnI_AVs1Bx9ZpOxmIM4FkmEXyGYlV5ZMTi0bAA7rko-WFgSunhRjGc2MLqMzthLLnZf2owNUjtxfpR0S2dKjSmEkpW3_-35mSqHn_4r47O3BtSJByBwdCLT4BSjwGzeCiSZ3J-3Iw2ImJJooRUwNcHo5vfSuUVrL0dhP0oyJJIpVgrgu27uBuq3utaQXabK-W9sMnt__aowHGtxYG8YvG65pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=Wl4DMzk2L5rYNF1MVNtB38g3MGgccfDb3_4DWGdVJSeaIp8kvkE0MyCrYx7-ZCZiTms0r2KS2RktSIWZSpumkqxgiX1iNBfDImMeREtAaY6kOAvdRZz59TerEFcwwYnI_AVs1Bx9ZpOxmIM4FkmEXyGYlV5ZMTi0bAA7rko-WFgSunhRjGc2MLqMzthLLnZf2owNUjtxfpR0S2dKjSmEkpW3_-35mSqHn_4r47O3BtSJByBwdCLT4BSjwGzeCiSZ3J-3Iw2ImJJooRUwNcHo5vfSuUVrL0dhP0oyJJIpVgrgu27uBuq3utaQXabK-W9sMnt__aowHGtxYG8YvG65pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=E3-QngybQ-H0n7w4cE5AZApErx8tXsBWOvGsfOcanDBqeHHG9duVrcoeqGD-4uhC62iSf1Gll1kcGYtRWUM79diF4Yhs3evYhOcVBpjepXIkaEcfEprmF3cU_UVDnC89xY46ig592bxZYSwrdQ4oKePsR2-kVvlm8yQhhTYUp2g0Ln8coJOyLdY9DqUqgXIIjQ9OQdy5P4JFffKoL0PyJOlyPQWvK6fASuM-nAHXrjxtbE7ziNCqxsEoT8L049dG1p49vceyjthCUIokyD2AtEL-Bd0QnJMDA5mzIUs6CVtYZgJ7TkCwqaiSkpuSNYAmH2aHc4K9SByk1msdShUUxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=E3-QngybQ-H0n7w4cE5AZApErx8tXsBWOvGsfOcanDBqeHHG9duVrcoeqGD-4uhC62iSf1Gll1kcGYtRWUM79diF4Yhs3evYhOcVBpjepXIkaEcfEprmF3cU_UVDnC89xY46ig592bxZYSwrdQ4oKePsR2-kVvlm8yQhhTYUp2g0Ln8coJOyLdY9DqUqgXIIjQ9OQdy5P4JFffKoL0PyJOlyPQWvK6fASuM-nAHXrjxtbE7ziNCqxsEoT8L049dG1p49vceyjthCUIokyD2AtEL-Bd0QnJMDA5mzIUs6CVtYZgJ7TkCwqaiSkpuSNYAmH2aHc4K9SByk1msdShUUxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=egnJnnZ1dVwJre9EBY3t74anbm3FA2Kw8raNSHRcb6CnvChJSZJM7WHPgoodW3fucHQcJwOv5oJWjp3oLNtzDdt0CLxc1gsljLspVMFKrdN_Ba9ZC5xGlknFiI2-02LGyAf56vuhZaOLj60CI-j82r5moZDzTY9Vje-M209BEWPSx3KyFylOuO--zKX_HTMDy5hcH7BH2zhGE16F6Rzl2QCeNU60n71hlA9s24TuANz6xeAFy6TKZge2IIOJnFadGx9jkQtaaknM09cDf63wEM0LUe2s8h7pvhGcPeZIKLyTQTMQERTR0jml1iS95YblqmfiTR5PH488qcUaRJKy7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=egnJnnZ1dVwJre9EBY3t74anbm3FA2Kw8raNSHRcb6CnvChJSZJM7WHPgoodW3fucHQcJwOv5oJWjp3oLNtzDdt0CLxc1gsljLspVMFKrdN_Ba9ZC5xGlknFiI2-02LGyAf56vuhZaOLj60CI-j82r5moZDzTY9Vje-M209BEWPSx3KyFylOuO--zKX_HTMDy5hcH7BH2zhGE16F6Rzl2QCeNU60n71hlA9s24TuANz6xeAFy6TKZge2IIOJnFadGx9jkQtaaknM09cDf63wEM0LUe2s8h7pvhGcPeZIKLyTQTMQERTR0jml1iS95YblqmfiTR5PH488qcUaRJKy7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUEaP26WOfkMC_b1S-GpuTG-VxBdg08njKXa6P_VDFxNEPCf5EQYoME3sX2cNNISGrjwogxWegHNa9g5UJUHIjU3Y1me1cMUat4Xcoc-l72epoXnRcF6B2mrMPduEjb0ZP2veiiT-QlXr7zibXGzIFfN3S3RvGZ3N7fBty1vjh--vTc2WNzsOjPolhh0cB0jcDqOB9WSjFTZEcDyhoeXXRHulGryqnbomLi549-_wsFpLJq_M2X4iCz71MACMaT4x1hPBGX7p0cYJVglMzqKbNOVhqrwqe7RqDFPzgjx1l5Hyq6H5ZrVcL0V4oRGLfDmHJt5WgTEIBtNretM5FdJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ry91IhHNufVuNZzXf8gNnFEIap61vK37Sr9nVHjFozwqONg4iwenaisO95Sb-RAXGx3AqkZYNEItooWRYZf80aSH2GIFJDLEJx3FxGuKKcEAn9LUmYKQEhCt1_S5ko8pBZB6iOdfVFrLYGXdfjwcO0A26jsU4IyaJ18617M2kN0MdfPiDWxeTIg4w6BVksXIfH-9hmurYscF3gXCLWoJMmpoFfMGL9RX_6ghqKNL_8JvzLmsOlJ3oX9wTWD63ywfMagsI7XBNt73W0-GLQ4kMv22C6laJ86h-ogryxJruySW58l1BmUnxsB0vinEzGPfTZUzVjhFNeM3TWbECublmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=tdjmHa4YnjNdQ-BL0T4qZnNq6U0UhEvmuIwUXBYighfjiSA-EuglU_iPFHnU9D2dvznWIK-CliwuhfvvxYDA32Yf3Sdd9iRfFcUQR85Od1LM3204eExf-Y7daz1ByL5As9nf9tdtZAlSH2qG88Wr7wD49IIuSVwFJgi2_CodmIP-7xFpGKD96sjb5DFm_5x99luDBTm11SMljeqFHMUXm0xBMjo4OeS2iYbYHQv8PgKo_AvvtDWJsfJSEovC2cOV31lxIcFks3-X-eQohmydHWYW4aTw4moDndTuijSwJrAAyvvHux49UILEfyKb8jr44stX58RfAFuttnmZ94LxOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=tdjmHa4YnjNdQ-BL0T4qZnNq6U0UhEvmuIwUXBYighfjiSA-EuglU_iPFHnU9D2dvznWIK-CliwuhfvvxYDA32Yf3Sdd9iRfFcUQR85Od1LM3204eExf-Y7daz1ByL5As9nf9tdtZAlSH2qG88Wr7wD49IIuSVwFJgi2_CodmIP-7xFpGKD96sjb5DFm_5x99luDBTm11SMljeqFHMUXm0xBMjo4OeS2iYbYHQv8PgKo_AvvtDWJsfJSEovC2cOV31lxIcFks3-X-eQohmydHWYW4aTw4moDndTuijSwJrAAyvvHux49UILEfyKb8jr44stX58RfAFuttnmZ94LxOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=vkbjNc9j09Hl7yM87vQSkhGoGRNmqkueQ2mxgBXIqWyqeui4bXbIj9hX1nlEejendtKQpFf65dF9z2o9yITPnymI_fTTUZuB_XnE0NYiR66sWnfHVqxYwKcBp6PgtR1tTWuyQTUc7o5-2sbcoc3FktWo_8xxwFee3BheafLVDz8Az-gEBHicN5UvpUgUndvi64RTZPjCgZUhEkf22IcZO1SgMOK27FLxjstruc9yqn6sTy6xTN-yP8N09f8h4TAN0Ju6E0hd_DLuPmUHkD9pGZj6UdL4Pbr5vXQwRLJYlKswo7aSst4yJTh4tWFUNTHm9QRSYefuwA3Z0YZpNdkITg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=vkbjNc9j09Hl7yM87vQSkhGoGRNmqkueQ2mxgBXIqWyqeui4bXbIj9hX1nlEejendtKQpFf65dF9z2o9yITPnymI_fTTUZuB_XnE0NYiR66sWnfHVqxYwKcBp6PgtR1tTWuyQTUc7o5-2sbcoc3FktWo_8xxwFee3BheafLVDz8Az-gEBHicN5UvpUgUndvi64RTZPjCgZUhEkf22IcZO1SgMOK27FLxjstruc9yqn6sTy6xTN-yP8N09f8h4TAN0Ju6E0hd_DLuPmUHkD9pGZj6UdL4Pbr5vXQwRLJYlKswo7aSst4yJTh4tWFUNTHm9QRSYefuwA3Z0YZpNdkITg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euZQRE_UYpwIC3fsK6ERnDOtayu2SbRRvh4arWLepGy1G_7Qr_4q1GVuRIxFBY57qtbNU_UwjvHw-7UIcXkg5-q3uutFTB01Y4wqj2CQUn1to4zMtL-yOe-iW0pl7hjEt8C2rGbvkYztaQdM_9Bj53lqEKAjcr0gVSokZNMN-E6RaXD6avvX8rrBjEAfSXlMZcB56xE0wrlVfXl8a2vB9l1jWSTRTYVDs2z4OdODId8skGou0cJYsqNy5na2DNaxrz_auc9pAz9KINfw_BXORbD6oAC_f8ZUvyEIyVzmUCqEAI1S2sYFXfizRiIQERcJn2t5NxfgDV3gFbLMzItHMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=KXh9xPbsK_dFgbctozDsikysNxopuCfypu3tiZ4SCMwP6QeZh-C98cKF2BoOeukO-yQPGIPYG3ULu_vwNyfOclQW9iGxXtmFGX0_4_fFwIrLtKPusumy9DkIzoBEj6RIakcJhrdaEnhUVCrm-9s1h3eb6-Wz6XpVmLsgnNJi7LRbVb-XTI6tF3dzTTlwnv_ZWHzpX2Ar-IJSneEly5QtpaZS02oyujOXBzuK40VxTS4dGGBcU7PY1tdvRxysKJwN7UqzB9FHBWem6C8LfphWUnvXtzvHf-FRanyRHylu7zvnxbAi4iC_l_jIdX-5e2xEEo6mVNxTv6GOjJO6xKS_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=KXh9xPbsK_dFgbctozDsikysNxopuCfypu3tiZ4SCMwP6QeZh-C98cKF2BoOeukO-yQPGIPYG3ULu_vwNyfOclQW9iGxXtmFGX0_4_fFwIrLtKPusumy9DkIzoBEj6RIakcJhrdaEnhUVCrm-9s1h3eb6-Wz6XpVmLsgnNJi7LRbVb-XTI6tF3dzTTlwnv_ZWHzpX2Ar-IJSneEly5QtpaZS02oyujOXBzuK40VxTS4dGGBcU7PY1tdvRxysKJwN7UqzB9FHBWem6C8LfphWUnvXtzvHf-FRanyRHylu7zvnxbAi4iC_l_jIdX-5e2xEEo6mVNxTv6GOjJO6xKS_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=Q9NYtC0uOWGaPgkXMhgak1Bn9hBb54jX1AHFr8lz28ItikcM0nuh__pf9W42t6NicnA0Q0yzIohNZYOdu3e143XyqFcVYMz878ETtfHKfEX1BkihWm0KPfyYrv5WHaEMINfeKLdfKjp-yE66_mjRA6m2rOjXxk-BGAh99wko1_zC0h3TleTzlq9PnUiW3eFV5FMjysZfxfxJ5IkNjdqBwhLn9md6iSpGnqR1zowl0P8csOE4KtRTVWlQrvs-6U0zkYvMKCpb-zIuIzkwxO-cp6p5Ng-PKK2FEtZ8Ralc7OMihxCRyo4f4eWdFNaqNBbGH3Z0J56ZFYZLkbIPribSOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=Q9NYtC0uOWGaPgkXMhgak1Bn9hBb54jX1AHFr8lz28ItikcM0nuh__pf9W42t6NicnA0Q0yzIohNZYOdu3e143XyqFcVYMz878ETtfHKfEX1BkihWm0KPfyYrv5WHaEMINfeKLdfKjp-yE66_mjRA6m2rOjXxk-BGAh99wko1_zC0h3TleTzlq9PnUiW3eFV5FMjysZfxfxJ5IkNjdqBwhLn9md6iSpGnqR1zowl0P8csOE4KtRTVWlQrvs-6U0zkYvMKCpb-zIuIzkwxO-cp6p5Ng-PKK2FEtZ8Ralc7OMihxCRyo4f4eWdFNaqNBbGH3Z0J56ZFYZLkbIPribSOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3vZtC-4dgEnvS5gv5spjWkzErsyUc5h61phupCJct1z5zOL0hgHPn9gZ9tpNGvH7Ko6WMXpjZlpqbe8AWH7NwEiR-O1pe9FpDy0XXcVdlGRk2TPiVswIreCdMhiWdGBVShN52R8LZ0SrdOVML9jobXBRqgLihbaywXjbKqTt7TSJ1uui2alB_dVwCbWDBrxMyxmmkSgeHTYsw-ytGP-7NFSohVKq3dAW38MHwt2mF7CuvqjOUEcUBLexbnmwS7iX5-Gc-jkeYaYbUnw0YAjAQFol1cA4E8ipEic-7gmL_IlH1sQB-FnS_XBVO9njtigHLXLJR0KObXFvW-1t_A6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPaIa9nZbyLTbW6Yd7ymPiikle5JZGOThR_b4v7eqLvFwzYvlkA9z9JNo-016ZYbZfquY7ilNJMbBG9fh5lcr-byU4Ypqwz-eW7dxPSo9nB-WFecN5qhebg2tpbefNHRXEALeoWF0FLkwesPLfvjmkWP10fkALbNhmnGOPtFKvy5Nhr_ZU6DXFkCcjcQvlWQFiQGxUtE-xbnj7XdpCtm0R6Kbu3nuKDgWyntir8d_ass-odiy1nWiDRJvdDKSEtAuX8D2NQqSJOqKevWnVkV444l95t9q-z6pYW-FFeXDstuDErUgJuLN8yw1mCBbchOiiaaiXzhlck7YvOsMDmyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
