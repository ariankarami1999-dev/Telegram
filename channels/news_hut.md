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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 07:45:33</div>
<hr>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLPeW2ziJY8lR4naMS2QP14B8XHhya1B8hvm63qIDES12IZlR7OL_O_d9egn-QoHiINYaGf0kaFXc4uMCw8w_kMx-5732RX0WKheZYhD1-tyXbfiCoFqB2JbQjlQoVZi7JTBXgb4oypF4d3CZ2KD30-NKtIFACypdsNZenvBmHwlIhGGncTrpncqY_kVT7t3JB8zCQHvHFsqUISc-4kETXpSe66rPhXKA5nJBesKqOwaSpY_LMU6agSHNrwfuhqxWzqn9azin3hLIqF_1liAPFk3hOOhsSJMNoqHAAnZH4PUJXkvmhhNuDnbZ_sQWDrV2EOj5d5y4YuX-WnMnhcJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDQsQxCBpCK6B-b4dFVzg2sEdHj7sffq4PtiYSy3y4kNASK_m7_9XPsmQe7whKL5HYbORklMjHJ4u-fHFtysX1SZ7lbLt1a06o5o8cgdAuLtUIrgygNMNSPoV2mSk_Im71_Ymc4UxuPbQiQJ7s_KLrmNpNdCPi70cOcmhETtj_179Ddw2f_4Efh-AbnqYcHNHf1hWEDpHzq7d4gvNypYCUuzjSh-Wsej2sYeyGs6zMqE9_aexDAjGkHRDmnlSdsAroM9EjlCSoQ3VFoCldzqp3dK_QwMw34CJNPd9byekNLsOSrNW2QsyYthq7CPg8PvuTfYaYRVgG04LrhD1s6ylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Evtnr7OQopGtYR68fjHEeF7yQ3Qf8ayn0tDmrURiPpYaJJKCSe6WrU4YmDftvuBo41B-Rz4ZmhOoewfrJS6DHS-AevW21_sgsLja8bdHQ_BUqHiSqgx7dWsWcVnQE7omvW4fLG0iOS_iPPPn7WgzuYbGNkkH9zO6zOFydBVN6W7JRu7qZP4RtXG8o2mWFvY14W86eAVU5VnkiMzhNZVcN7SlAoUr6o6fug6MI6abSnLoKulrkkIXDSpAYN8zedOQxHNtWOFFxBYlt8LTLSVrYAWJswh3KmgWIcdGvd1hPMgoO2hnLb7kSow-DTdTmNTdSleV00tYSuW4mP9QqM78-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWrN6Qt0MgGdYxdTRyVwla0ui1MQnarJdDgJwJYtmDRN1CkhuG7XykUav9CVuMdhoymmSbp2y9wHgGvIyyL7IXRjASIBJphsJe8VN60G4EFWYegjfvjNu_1jUVfx4RMf963pi50cp7MmsbYnt3ulxexh_kkaN7hniuaDR6M1rvDQZNdBlJdlhaAQhTghqyNFfXlg6jcuqp-hARjtD_yXsiS23EDBmAEZaylMJxl8wY4PUJhEEMm58bBnb9Uyt8Fvul4RrUHnE68U92mjnpFarfGmOocV014grj9NUtzi7vTmfhX99dG0ZulGJKSQIF_7XOgWVTff1s7p8M4SIP_7iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzvNKrYOm9f3NbUw7shrZtFR34D5dkYKHM3Mg8gn2k-a2K0lNZLcrjZOx2yNiZXEZWytAsLCSMjZDSn3csK-03mGgvXvTznZyq_HqqC6N7U9FABKxM7slUif0BOJFjtULg73Ns5ODo84tuHOkOa9FZjuJcBYfWrK6jN6xTRxE9c2dnBSbmb_yClG7D-ep-zceVdAAnWx8pP_xKa38kDp61Po_303WLAN9iIiz9-OiUD_3uhqBl_zaasmbJULSOTaL6AKBW-yrn1JbM6n2UovnAKCLbRvhTrQLBSqXLB6bd2K7ukn57RJVAVhalGM-Sr-kymKiF48BmyRF4blLNryeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=k6_98qr_26q0wxDAypSoqwop57kEBC8NiVIVg07xkqjkWoV8zijX752MmdVWSePDzUZtFmP8aaZb9mtPuWfRz2Saqhau2WQPQ51NB5X5BWSgpWUSopKxmXp5NV4fpXWp9OyRHXY0r8JmbMlS4aS_0MzEaTJhirs2518qjoKZyh5hfOIvLIsTp9uPV8QCe-OAaHvtvPbVI0FCQmT7k_J4N03yXivD_-4YlMPvCEWdOiehqel8yPFkMxRtiMIvDiQbuY2ODbZahS_hKM8ZlORRm601y8RzKVbWgTmhVDxruMJouVBtJfCJsm-J1ugxR-sjfd-Zpmq_WpuRT0wrOhRuzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=k6_98qr_26q0wxDAypSoqwop57kEBC8NiVIVg07xkqjkWoV8zijX752MmdVWSePDzUZtFmP8aaZb9mtPuWfRz2Saqhau2WQPQ51NB5X5BWSgpWUSopKxmXp5NV4fpXWp9OyRHXY0r8JmbMlS4aS_0MzEaTJhirs2518qjoKZyh5hfOIvLIsTp9uPV8QCe-OAaHvtvPbVI0FCQmT7k_J4N03yXivD_-4YlMPvCEWdOiehqel8yPFkMxRtiMIvDiQbuY2ODbZahS_hKM8ZlORRm601y8RzKVbWgTmhVDxruMJouVBtJfCJsm-J1ugxR-sjfd-Zpmq_WpuRT0wrOhRuzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2ONlFFUHCSQsZi-6kVN5ZF3L3acff7-BHm3TQ0tjXyNtmuMcdqBi9g0CWJ_y8mhKhWOjS0EU0q_ycYIQC2krCL_y8OSqORNIOoxsNOYac_7QBF508R3DsuUiLZsfXU8zJh4iOKfag-scSYJ9ge4rHJZ5B28Id3qZROVUKjrLRt-CS1DiZOQuowkQUBY_3CcaQDj4G1RlMxiPIFhlmY9uIEuqowfoHnZA3rkMiCSxs8UDpn6s877iVIo7vIaVdelxWzggcdR1Ds4Q2PENbHGCN-GeSVgXDTtJHkYeI8qZUsAuxjILVTjlOifqFAHBxsl-spD5SJUAeAlkj0bFQAgeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=VV4T3uESX2eKRAEQ4_CZbrf2gzYLclv1Wst0w1Sec0EYlfABZ_x2AKwGGdN1rnniYGadEmiNGsecBYca2xko_9bDsmUiI3kjtpozv3sPs1YnrAM5I_iRatw-1Po42aEXM-Yj6-attQ3K_ZI110XfCpIJ14PAfXNWEgFQOTH_rX-R4vxft-N5bCk-Z_8q0EIcP-EtpuG3PNdgmuKWkt4f08jddvEI-BqEzXa8tywWMdJvUdtj20U0nsyYtEygCjM4gM9Ma0E-S-JHTTzJd4NUW-2Ms4dLgfRlUO6eTH0QTgpd6GJkJp1WmxIffHn17FRWjKF_PZOOl9VeT29UvBk6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=VV4T3uESX2eKRAEQ4_CZbrf2gzYLclv1Wst0w1Sec0EYlfABZ_x2AKwGGdN1rnniYGadEmiNGsecBYca2xko_9bDsmUiI3kjtpozv3sPs1YnrAM5I_iRatw-1Po42aEXM-Yj6-attQ3K_ZI110XfCpIJ14PAfXNWEgFQOTH_rX-R4vxft-N5bCk-Z_8q0EIcP-EtpuG3PNdgmuKWkt4f08jddvEI-BqEzXa8tywWMdJvUdtj20U0nsyYtEygCjM4gM9Ma0E-S-JHTTzJd4NUW-2Ms4dLgfRlUO6eTH0QTgpd6GJkJp1WmxIffHn17FRWjKF_PZOOl9VeT29UvBk6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=jqobheVklNwo2zRVBNpfLa1nMaTjujLoqBuqOZLruLrpH1XuQE2bTk8-UtFUaQa3JrP_hAJlSsBhfoe5LPydDR4iqmSUrP3RZRscFGE-4J395uL59w5B7VjE70HmIHERK0vdju-RtcsM1Vlup4h9Q_9y1tFWzQ6Q8TeguBtcEWytrGQ3WKj875zqfh2HpYPEuNe00TMF2rS8c7Om6RewN_ltkeuv2fo4xEFrU7q1ntgL9U6QUOK8k4zLWiMBf7ee3MaDd3YFzvIRbYwKxlisdlGPwUz6GNM5wLL_I96-EsFeTIhc_4e6tIeWzHALeJ2EycLcWRzLbtZfQlsC1gw7aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=jqobheVklNwo2zRVBNpfLa1nMaTjujLoqBuqOZLruLrpH1XuQE2bTk8-UtFUaQa3JrP_hAJlSsBhfoe5LPydDR4iqmSUrP3RZRscFGE-4J395uL59w5B7VjE70HmIHERK0vdju-RtcsM1Vlup4h9Q_9y1tFWzQ6Q8TeguBtcEWytrGQ3WKj875zqfh2HpYPEuNe00TMF2rS8c7Om6RewN_ltkeuv2fo4xEFrU7q1ntgL9U6QUOK8k4zLWiMBf7ee3MaDd3YFzvIRbYwKxlisdlGPwUz6GNM5wLL_I96-EsFeTIhc_4e6tIeWzHALeJ2EycLcWRzLbtZfQlsC1gw7aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=dDCuoDcnrAkHkpyikiHAR57LZMAxhqphMJr4QXUbVFmH8Begflaf7__-i49wj7APWK2mMgVyMc6Pvbfu3kvigj7vJjMe4KkxwAcYjjmsrS0S7tjkLum9fZZGEsVUftAwu7yRBwEX0x9l86tuTVrVj_NysmlSPwr6UgrKxNP4hzaTeBcq6aJFy0czSBpFbXSiAjmTCbyn9CI8_5RINpHcLcbaaRQ57LXcMKJrDICb8MIA9cURQoo_wZ5QaCVYM-_d5ITXAHYdIYdovvXTtHZfzXmc0oxSNgaNdrdxRjIvzJ7AqCajGhpN42nFVXp2jYH6DKqgWyZ2ibxwv5KuhLgXpCQEi0kh5wJSUU3bKgIvrPnmlXwbv9bEYLUZMG7ovEBoMQih3-PSKu7KQz1v0_7m33e0VQSOe8jM2GgT7B8yRtzQB8mjXz69ZXdmGE-C9B2qVdf_be7sseQ9WCjbidhjahSRGJKaNqrj5ekiUMtBHhxxSrUPxCGetwYdj_I19bPBLGyGis_TcHYH2t1qu1JvLbxFkdhF30pBVNi9_hmypdbSgqpC-E_OxCSdgN2OK-l8ILjkGyX7M4FfScP6OdUr4hBLH7u3BS65MVDdws2uEKPcRGt-zDIqggwUFANwefT77SmQ8LhWEpYefucTLDnIjKfFOrKYfMh8k1HByMECDXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=dDCuoDcnrAkHkpyikiHAR57LZMAxhqphMJr4QXUbVFmH8Begflaf7__-i49wj7APWK2mMgVyMc6Pvbfu3kvigj7vJjMe4KkxwAcYjjmsrS0S7tjkLum9fZZGEsVUftAwu7yRBwEX0x9l86tuTVrVj_NysmlSPwr6UgrKxNP4hzaTeBcq6aJFy0czSBpFbXSiAjmTCbyn9CI8_5RINpHcLcbaaRQ57LXcMKJrDICb8MIA9cURQoo_wZ5QaCVYM-_d5ITXAHYdIYdovvXTtHZfzXmc0oxSNgaNdrdxRjIvzJ7AqCajGhpN42nFVXp2jYH6DKqgWyZ2ibxwv5KuhLgXpCQEi0kh5wJSUU3bKgIvrPnmlXwbv9bEYLUZMG7ovEBoMQih3-PSKu7KQz1v0_7m33e0VQSOe8jM2GgT7B8yRtzQB8mjXz69ZXdmGE-C9B2qVdf_be7sseQ9WCjbidhjahSRGJKaNqrj5ekiUMtBHhxxSrUPxCGetwYdj_I19bPBLGyGis_TcHYH2t1qu1JvLbxFkdhF30pBVNi9_hmypdbSgqpC-E_OxCSdgN2OK-l8ILjkGyX7M4FfScP6OdUr4hBLH7u3BS65MVDdws2uEKPcRGt-zDIqggwUFANwefT77SmQ8LhWEpYefucTLDnIjKfFOrKYfMh8k1HByMECDXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=g5mRucFdAHioTuJCQsvdxQjeTQS_wtj-0rSD4yBQmVG9dhoka6aH4xmL7w_WDa6x0ko9aBNeAWGFkqlVEoDAWn_InyKEBY5Y40JyCaZE6H6nQsxo9QqMqydKsJxe8b2kC1XrLjAi9cqxtvAOeXrqJ2sp8VofQHk5dGL_VddG2hQACAg8heRCf11sPlA8xmVrdux4i7M1F-_4i6Trv1_kStaNAPpt7KttYaVfSImXM3ihv4sHVM9-dQY3flGlrhbHcZdiFAlNp_I22ozGs-W6By0dbiMdRTALXQfoywSrsXtQmrpGyFfn5ZoP6WeZO9B79apzZ4tC_4xljmwUBAhlArRwCITk71csn_QIzTTtVWBZFnrY2jDZKTA4_MFq3E0rwe9mjCsTxHGxl-rkWqWI_KoabSgJX1JqDjBcDWayXBmQrdkDUPuMD5ilXKxD05sEDhk_CBPKxe44bKY8rP3c2SP_ti4DRntO9_W-BF7tMJctEGUFBwUfdgpwEcZLkf7EYrSXzQFSl-zpZthZsdVOqoKXVkYR49XnhV9mhXGrMGuGFrbktvy87wWxPw51gJbqfavF0RAewOdVWgqGzF8afrMX7ABdi4DedIv0KjO2Kw09AftheZzEp_V2LwVBn2IFUsGNqk4oPaeYXOUnyZG5Td1DUxse-6GGIAkAKkTWoFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=g5mRucFdAHioTuJCQsvdxQjeTQS_wtj-0rSD4yBQmVG9dhoka6aH4xmL7w_WDa6x0ko9aBNeAWGFkqlVEoDAWn_InyKEBY5Y40JyCaZE6H6nQsxo9QqMqydKsJxe8b2kC1XrLjAi9cqxtvAOeXrqJ2sp8VofQHk5dGL_VddG2hQACAg8heRCf11sPlA8xmVrdux4i7M1F-_4i6Trv1_kStaNAPpt7KttYaVfSImXM3ihv4sHVM9-dQY3flGlrhbHcZdiFAlNp_I22ozGs-W6By0dbiMdRTALXQfoywSrsXtQmrpGyFfn5ZoP6WeZO9B79apzZ4tC_4xljmwUBAhlArRwCITk71csn_QIzTTtVWBZFnrY2jDZKTA4_MFq3E0rwe9mjCsTxHGxl-rkWqWI_KoabSgJX1JqDjBcDWayXBmQrdkDUPuMD5ilXKxD05sEDhk_CBPKxe44bKY8rP3c2SP_ti4DRntO9_W-BF7tMJctEGUFBwUfdgpwEcZLkf7EYrSXzQFSl-zpZthZsdVOqoKXVkYR49XnhV9mhXGrMGuGFrbktvy87wWxPw51gJbqfavF0RAewOdVWgqGzF8afrMX7ABdi4DedIv0KjO2Kw09AftheZzEp_V2LwVBn2IFUsGNqk4oPaeYXOUnyZG5Td1DUxse-6GGIAkAKkTWoFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Fbgy2DpUxy9gWNp8jt2nGKV-00Xto00df2bSJ3wu8mqX9TVfXRntGs0oPWy3KqAeR66ffUU02g77uGfQwSGXPztN_3KhqYUpoZQwwxHYXvj_3f1KrwonPEjbW6G9uDBm_KcMVY8LBVSNnaM7jTLlY7o1B3QvoC2ltS7C1IwK-rS0n4OyZ0FXO0LuNA1SGOYJIZeewjZ5SQ8k9sQ0eSAcx2THz1Hy_USuOCHc6DvZBQaQheFonj_ffAnfQabbH9kDYagPt-2iNpCplcnFjj9oVhp6oJQHepS87DtjRg3hEMat6jIY4SFNczbCF61w3Ilmbj--H0n04fY712gyk4mIqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Fbgy2DpUxy9gWNp8jt2nGKV-00Xto00df2bSJ3wu8mqX9TVfXRntGs0oPWy3KqAeR66ffUU02g77uGfQwSGXPztN_3KhqYUpoZQwwxHYXvj_3f1KrwonPEjbW6G9uDBm_KcMVY8LBVSNnaM7jTLlY7o1B3QvoC2ltS7C1IwK-rS0n4OyZ0FXO0LuNA1SGOYJIZeewjZ5SQ8k9sQ0eSAcx2THz1Hy_USuOCHc6DvZBQaQheFonj_ffAnfQabbH9kDYagPt-2iNpCplcnFjj9oVhp6oJQHepS87DtjRg3hEMat6jIY4SFNczbCF61w3Ilmbj--H0n04fY712gyk4mIqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WydfMBT-oD28f8qXgwuOsUSyE9tC2ERivlYiv_Yg-dkYu0yqexPJv6-wgksTTRYqeTvPVx7lASC0uShDjfDu-RvA5B7gUFw0yGmAFi-XGV3GaCmOfVvjc8ps4HspugK2mLRp7GIl3SJj2WDfw_oDzi-Kf0iyFt5CpbUiM7GU1uEZGDOEGXuInpTGVtG1KGqzXzjtOOmE9Ax6oEA2p9VhM9eFIRuhVPExXrXPM0AYAGqFwUp7ITUrIXZ1AiHHsPZr-ayJ6c-BRefwaR_q-CHmAA756LEGyo_XOMor1eOwW8M9hFer9uqZ4UXQ53PbfZTCnnEAMQwyNPdvmsqI6K4vOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obQHCYWklnpoe-Ut8Hg45OhWl7dPOD-9dPKbHLnsUtRN1z_LYkcJ7XWbFebrQa3SmGJGtWvkhBHa-ht_e8UN1FKf2vUk7SzzqBavY_q_ZQ8nEEwWx5spc4aZnOV4WI7X7lCE9IP16z2t7oR6twDDAIVVeV-kigtGfR2x0pJ6mXl_E-66cXI0ts_HIGchLArkEIJSy7DMwhcdSNEy7qbIHsYMm6zCiMxGRGHgKRQgfulg6Za4LPAgtXl3iUFuNzfP9vZxkuEiVnqYTJJRTciS3NVfEBj22gGhOm4MULFKmWDjNSUvyAqZsImsvFMDeSczQWVcxNajyrD2sH3p-Yllcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=s8CiEQeYd8gkroudBEShdVgTLN9EYkV9Yx9yTq787yeT4LlpBZ-rngSYawbtiH0t-qynK4-UcQnUnhaoOLeEWquK0n6esnkApXb8pgBHpiX4mb5NM6wfPSoCvM4BknAnrz8rgenzxt7iE0Z_1_TjPy0BkBi0L4JlkFw8y9GMXoEvZZRVQnlOKLaAUkHuehURtVLgGt2tQLiwpcXk8CaS92zjN2OP1Ckc5URY2VhwGqSTU-KrZmN87hh0lIwZT7SY2XKzK5xTTPJOta2vhhrVBccXdOl8rN2NKUg4IIY4lbygj12m-ey_qM2FnlBoq7fo_-rx0PONEThplioqc0EUJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=s8CiEQeYd8gkroudBEShdVgTLN9EYkV9Yx9yTq787yeT4LlpBZ-rngSYawbtiH0t-qynK4-UcQnUnhaoOLeEWquK0n6esnkApXb8pgBHpiX4mb5NM6wfPSoCvM4BknAnrz8rgenzxt7iE0Z_1_TjPy0BkBi0L4JlkFw8y9GMXoEvZZRVQnlOKLaAUkHuehURtVLgGt2tQLiwpcXk8CaS92zjN2OP1Ckc5URY2VhwGqSTU-KrZmN87hh0lIwZT7SY2XKzK5xTTPJOta2vhhrVBccXdOl8rN2NKUg4IIY4lbygj12m-ey_qM2FnlBoq7fo_-rx0PONEThplioqc0EUJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_qKH_xiHrdrHRlfBrkTI3objswcpNS1kkCOZF1jUUArYCY5iVVZTJZBxvP3RU1Rp6LcbwyFAUHBmS-bt0BaaXxHi4EXI6hPHl081--muZviuRPlCx_917O2g8iZiT6M9iBFb2lSH7fTlSBMqxq4kgE0c4Hbey5qG7r8E3qNvdAKnwAkvi27l4w8bldYl__NmBdaYAvW26L-o6VAPRt9kuVOW4_mLNjSQAeoAHBMS9FwfZZqwEWmtyDJBImF_kjy7k1nKd4_lBu6x3w_lB3q-sf_85E9HvKxtRYkOFpXnW7PGCWsE2rQ_-nM_U_r1NSTZStMSg2iyPbcYj6pkHFY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJMj3mAJE3Ir4G33bV6XA0GEyXH5EbnFMwAFXmw1hiPI8kLbfdOR_B4sMdzhoUrX2sOSBZkkUqBDJybXrKvsapuVc_nLgrTyI8rOTa_yqndUXxLhMfTXXFtCtq41KcCmKZLf8KGuF7AOeKPSkejvfkVHGChhPx8FvNf3G5lmQB-BLNFqQkSxI7PQ60QBYfRm4yCPyaELqw9W1ST_8FEh-PC6NRQTwgDu9wtFrYXr-WEtGRqBLEFGVTXZhuYRniLt2OM5lM7G2lLF_u7ca89VCVQHNewxMIwzQgdCqzMYLjpJSr9GXNR8XDHy87eOT3O39LCP6EHJohA7nU421xmp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8W7BnxqGbOLiZtnek5aICelEauX08rsAYtRpY0Pd9zTBe5wBVHUxRiNKjPUmnr-3_1eUr05I3a5YcUtvVgyPWrId7BpewexYiEqncfw4XVK2I5ChsdWx87TNljnsJigV4-yHlnh-3uY_AxM52-8PwUDgTTdqUQ2phueXoVTmz5jimmIyrMxHNK550xH085iIN89tGWcJ-d1Re8-BHHKl4v8PHK5vv2A4NKSj-KSrRD78EsPwxsVMrhSq4T6dgXcDp7CF_c8EMEMKuxVxKCqqbczxDSNQCdrDrd5OnPznJIQ1zM2quGXD1zlIzrEdlxnb4dbZUFArvCcgvaLtBOiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eo1GaRBZMoFByuAQHZDfQk18ukwcZ1I5-UjeS6UfSVlWP0IQO_1TzeJb2F7ZSAE8LWoOUtDT4-i0sCVMXLO2Oe2FoH2cCCfMIBF589d1p4O0EQQ7V6FBiDrjgS4VZSw74Ll4VcwSJOhps9ilYJuFceoQysnHgXjuaNreDvH5lIQhGyxhISdaqXjDtF2TfWQniS0ptHmhO11m6DXBMbED5RJVg2H1an2fykkBlwCUYWSUF-kSZi4ORMakZ7DfdGk0xob_VMnYM0rP7ZcjQmUyiF_BDL5N1IBgkMVB0xNzjbX3wZVMhz-SQkbxKREipXf_zJIgzbqLvgkL1pLnnqecRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rvpg4y1M7SsRdQ98M5Y1f4-tiFUI4iinfYqyPnU9mMogD_UiIlUg0lscpC34pIShrAGrSskc9Vi8ebO1bBk6WmrkN2qc8kdCcHLf6kRxDLMCytZ9Hb_G2xOetejNzrgloH71X1B7ijEOaf1PFbVbrea1Qe5BwbZdw8Fv0zupwX3HO-YtAUtZwkkKUmnZbXN9xXovo2Z5-Ya4TOrgysTwzMUK7mG77vpL7_FPIgPebG2XQkOoV3DJMXb3dzPITwCVvXnhc7WShSJnyVIvXyjARJ8ejL7oohmrH1vu4wsQ0zkpgV7X0nzVHT9EiltUmJ51oLXwEv4Sc3P841C2T00Meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk6Mkfv2EP1LhBbk-7M82ADtCP-HRdL7OK-CjxUVZvphaY1M7BlqU3FeAs423o8ykuAUzL4JSNAn8cOmo8Cpuu0-VteQv8Ya1G6qMh0vu1v4QApQSUEGIxpttRd78jbv28YF86HvpTg_A-mLsPMBCVo2ep2vB46wz424l3rT8Zr94DIcO9NG1guwbJjCOUVL7fTUtWUcvj9SoMqH6r41tGIZ8wf0si5xyB6Ib3pNx6nqoiNUo-9KBsSPyXF0HHV9HxEbnEc08O5mAwr4o0PXAyrb7_1kyF7B4O4CaRqAD_6emR6mKPKM4NccoWrEvtXa8XiOwPJ6kLC6d0CRmG18wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWaDPfDgBem6lr5IZIHR6ZyWGek3gq3iTZazrarPYtii_3RH2Me2difkjm98EOwVio7olgsbmhtZwein6GQ-RI9XJUxva-UXEiV1LaMP3OiOOy532XMT-apjCzZ-6wsjZxLpG2cVcF-a6rImnvE0wplho29qdt__rL5NkZczQWyn4fXsKWrAa8aAkemXUcdhPwrCqtdiYLVjS481jfqb7yTQk31Z97sKqMkY_r9D4RXfdLmZFWZjERL2b6h4FxJDbkeWLaLwzAH5jFW326FzMMLXte31OOQO_RC-krqL5KwSckvdHiWcCi7KJTnv0RqlX3IwKRhP0720CsAD7jxBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g0kqDSfgUE5IXpBtQhnLNzphKzF5LDoLDdEfcGJKbEc3-Hi0OEY8tdZYfQ84TtrHWW5Wbr6gqjfQ5Ei-Fj9bMhg9E9m4qwmvf_6BGuViKx9Ka9NrTFcmh9i_VKEUnMIHi-3WQa4x0EVBL-r8SCoN-A6f3trpvBpHLLKBaH-nK4-yt_IlsRcL7Q4hD-H4TGGaY1sG49NPDOlALhhUq_ctrZbfSarsryidCcwhWct6I1KhTd5tsqrvY10lxF7Xy2I8T_WIuPMKBUuOJ7r02zYT7InFVbmwlWUl7hHIDOGnVWZsa25VHxKVPMRcNwwT3Dm_yMggt8IAoD7Lztbc5GIhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYJfhKVFcqylzxbvXUwxpS52rEPLt9nDJ8C-Su6YfotmtSnudlSoxOh-g5D-xU_0UqTcrGfVQEhKvBZdKbxwJFYBFMW3IJel4-tO0WT_BZL8ahEmIBUPlHYy8D5kOsTTVzD1fqHZcrdGXiic6aahe1FZT9w1keG8VkHRxgOIQgCmyYl0vFETbTOsadgkKSD0eKogzdPRkJjyEnoiqw4yytJg9p_eTqnabEpvOg1RgayXUvnTDrfmMilKCUVq5lDMcQtDaJrNq8IFytrt7Yq8zCRPv3qob1QFTUOHFkh-n7BFKbvAWYFmuVY13BFYd8cKiskGISrJ7JKT-EP1lINm5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqRurog3bETB_QcUTsRaCY2W_k4mnEwb8aIGOW-YwjQ_Ar7WNhSQO6ABHYJqjzv6nC14j1MN0uV5NJEgT-MKa7laUTYtWxcoBCqnGXpygyxcK_3xLHtPS7c3fMN2jbZJYlCezpPgvu4fhBi9Vme3sMCIdeCzzvJYZGgOEUKCMn-Nx_qS8JxN1hTmVF7UaIZMWq4GJgpomTBFy9KmOqbNuEYr2DmRqr_Qw1krWgTULgS623GvS-WGQfWfhYw6li_22KReUb3lO9trKp1wa-QZggwhBeqeMDhdNYjyHE1y4cgyJqU5RBkfbQCtktCWVAZISIhZFaUbpgYW98Wbsw6OsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG7nlIfE8b3KgRzMY-2Qke9iAHdtRs-FYCaxrcGq-j_PfKWzffkpFhHKIHv0hj6PIR1k7d79wH0MwoJePF7D-3SmutrSU4UF2DvwlU1JRvwtHvttlf9dUW5pG4qZRGw9P-HD_BPPKZETN-WKhByOB1dp8CU7J7gIjdYmNN_sjSr60WF4QNi0LxE0MWA8YkH0Ar1p2Vmp0hR2B-G-kTk0ZBOedMw5HBQ-1vitFFRNTbwhrHYGhw9EixQTc4DipsWoeHYeF6DyCARSjLR6pQT5Zl2tYpQQnREVk-vUg2TLbPVPQCEyyi5qzu_PCcIkJdc6FPMgT-KplJBPg31veNqkSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=IbI1NUe4pYoy3BhHjSuS7RLIu8tLKHLDTOC0pYXbv4_-3aQU84mYjX6MQvelnxDv_D3WLAEdbHx3ED_o8oT7jkaEhhZ-SX4Yqh8J9CqLKG42hRO4noUMWzS3WoLjQ4HztaIfNdXSz_Pb9660lSDeWh3rhWbEum0-H2EmVAdM-AQQANFLKpKrov0ed5Ov0FaDLNZezc44Vdgs1ZwmXKzpVp594Fj6GV24jNABML7Qsvvd_dTb3lE79PX4Fm6dF9grOb8-5Qj9J4xZAP-va12ztuxXdq5z-uJx6ZyK2cpSyhTVUMMupe7hqBEUdMTp3A2eB1tVvOpETrTmyzrgJRVEmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=IbI1NUe4pYoy3BhHjSuS7RLIu8tLKHLDTOC0pYXbv4_-3aQU84mYjX6MQvelnxDv_D3WLAEdbHx3ED_o8oT7jkaEhhZ-SX4Yqh8J9CqLKG42hRO4noUMWzS3WoLjQ4HztaIfNdXSz_Pb9660lSDeWh3rhWbEum0-H2EmVAdM-AQQANFLKpKrov0ed5Ov0FaDLNZezc44Vdgs1ZwmXKzpVp594Fj6GV24jNABML7Qsvvd_dTb3lE79PX4Fm6dF9grOb8-5Qj9J4xZAP-va12ztuxXdq5z-uJx6ZyK2cpSyhTVUMMupe7hqBEUdMTp3A2eB1tVvOpETrTmyzrgJRVEmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=BuLP5YSDpHDVWadG16OlXJNk5Gs6ShCXPy0YdHbO-0kUgvJIExOJGAMu9qwmq_Y222pZQED82ojDAD3LA4JOzTgu_5sKexoCHu65w-J3Jbkilk8XcylFODwslgze8MdLRlzxle6zvdpt4zxOslVyrZtOfBUwaZrK0tlm3P5epTgKXASdialSvMQkGdyP6S6Lw-xDflPKsj2SNk9_nYOP-4P_JeuIU7xSIUQhEjYFgZ-p0UpSUJW8EQcHZeGYhtcDwZi-HW3khPofK880yy_r2UxtBEK6080pQzs5KoOcxMzVpnk2oEVrWAmSonssjO5StbM2TaAYu_q0Tb8RxpKO-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=BuLP5YSDpHDVWadG16OlXJNk5Gs6ShCXPy0YdHbO-0kUgvJIExOJGAMu9qwmq_Y222pZQED82ojDAD3LA4JOzTgu_5sKexoCHu65w-J3Jbkilk8XcylFODwslgze8MdLRlzxle6zvdpt4zxOslVyrZtOfBUwaZrK0tlm3P5epTgKXASdialSvMQkGdyP6S6Lw-xDflPKsj2SNk9_nYOP-4P_JeuIU7xSIUQhEjYFgZ-p0UpSUJW8EQcHZeGYhtcDwZi-HW3khPofK880yy_r2UxtBEK6080pQzs5KoOcxMzVpnk2oEVrWAmSonssjO5StbM2TaAYu_q0Tb8RxpKO-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=kGB-QRq9iU2nUzBLUq_2iOVPjGwUlP4wx607tXL2I6W6w8C_0QDZFcTab2RMcvwy773HMoZGS5XIpY0dATJw5NUfL8FeFrwuRYz3hRmbNddeo73_UkCYQ8o_KMbBFPAtPUd65g0xjMquMflCoCKF91U3aOeq5UvAaNOlKDV1eYH2AUrLSAeFibdA4H5YMQTzXcjPRoKktcSBjadtlLVxWVxQfsLaOsGhi1d7SW9Tfc9BYJbEdweYYRwlRbWlB6vvGk-7yx4q0vvU_f096zIASObUY-OAs8ANauRvF3s_gvXsG_2RwO2nSrmHtXDdPzSCFRKKfUjZ-D6NKLEIWHcb_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=kGB-QRq9iU2nUzBLUq_2iOVPjGwUlP4wx607tXL2I6W6w8C_0QDZFcTab2RMcvwy773HMoZGS5XIpY0dATJw5NUfL8FeFrwuRYz3hRmbNddeo73_UkCYQ8o_KMbBFPAtPUd65g0xjMquMflCoCKF91U3aOeq5UvAaNOlKDV1eYH2AUrLSAeFibdA4H5YMQTzXcjPRoKktcSBjadtlLVxWVxQfsLaOsGhi1d7SW9Tfc9BYJbEdweYYRwlRbWlB6vvGk-7yx4q0vvU_f096zIASObUY-OAs8ANauRvF3s_gvXsG_2RwO2nSrmHtXDdPzSCFRKKfUjZ-D6NKLEIWHcb_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=AhiDMlDr2N4GwaJ_B9H7NROlfUOmIHHHOIErGUlUdu_Uf9aGuykapiiFndtxkwtv4ZCqBpdNR0YdAfKRigilN1EfC_25O_OBvFegMjNrnPGC_39Y2_t9n66BeDPW3GPjHvoXoQptrZZBId9d6vNTM-s6_X9WL-Tm6X9BxC1d_sKoIF3e5QZW7Stm2vgI-LUU3VM_6Iq9_a4290gkgV2s4tVR3C7V4z_rfWXbO_HcRjLXlFHuSX84Y_Rf_JkkyrhaGJYtYZ3KcnqZzvMDb2rXsTaB6JGAMVT_-cYivPUPKrkkUqRTPEXOIGb8UEhp1yS5u9c4UM5BeJj9ZC9oySpkcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=AhiDMlDr2N4GwaJ_B9H7NROlfUOmIHHHOIErGUlUdu_Uf9aGuykapiiFndtxkwtv4ZCqBpdNR0YdAfKRigilN1EfC_25O_OBvFegMjNrnPGC_39Y2_t9n66BeDPW3GPjHvoXoQptrZZBId9d6vNTM-s6_X9WL-Tm6X9BxC1d_sKoIF3e5QZW7Stm2vgI-LUU3VM_6Iq9_a4290gkgV2s4tVR3C7V4z_rfWXbO_HcRjLXlFHuSX84Y_Rf_JkkyrhaGJYtYZ3KcnqZzvMDb2rXsTaB6JGAMVT_-cYivPUPKrkkUqRTPEXOIGb8UEhp1yS5u9c4UM5BeJj9ZC9oySpkcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KBunA6BCD9pDYymLxoq8cYTQwvcIHnhZkiF7PH5wSB-IY_zfiGBn6Enzr1iEXQ9RxyaBP62F2IqfcSKUIi6S5GRv2n9tgvLmcyJMQCRavjf2Uji2Yf4HkrZvmbkhkwMYYC8NrMEyncwindCebGK9pXdDfYso3VW7VSDLBcoAuk8rGs2iwnDYyU0fE4JgtDLi9rD1Ys-9kjovwXK7lgbBlCcL0yOke3WNIt5cFDwSLA_n75JBVevCz0O8GAtdDXJhcBMkFFR_eM1lp0JmTu_ZlVTzMcJEMAhV2BsftgrvcNPEqt8EPTdOxYHcOBJ06cmdMj2nlZZv4aE5Xzq3eHm6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2PliM0x9pxnfub-iufKLUtQ-pM2lUqq1MJnOF67ekh1AbfaE0MhFF_XybZhjH1LqWL1LathwiSLQP13eGSy607ZfFIRk8Y7UCq_xgwsfYhZZGsXZxqA6ex6QIJhmu5fMRsl-U7jjkziV1MGNNYx9urZwMjjF5R8vrVmakRpfM8s-9I7MZlS-QYx0tov4Oe26nQojf0nsKTv2qHK3WGpkXbya8vJQRpyBw3ClzZm-7IvRK9EcK048AlYKvOz5-p0JbF2KZLo9uQFXe2RLMH_67NCkc7pXTWgSJcnZsCTJ-5WLOFcP9fhBcVSLUCJNjUxVxJYUIRO_SlZvv47nvj5iA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSQuz-t4DBC0kIfdzHql9rNsPtWP3OBoskeDkQBoWICUL-BsA048F9JZxUIEldT2QbY9lI2FPWRJNZGxz1XLILn__WTBu7iGRPIuQf7c3zG1web2fG8df2DzAHHCFqGNTk825WCI6X1Hgoi_Xt2oGkzX9avJTHyFtSd4sS2UrgyoR1q1f-94KxpB4AVgUl0e0SngE6Y1XhZcs1JAZqAuHxJNP8yPn6vFz8yW-dMdvr36ih-83ukGBC7r2ufsKRJu7rqHXRKwv0cgnGJz3uITE67xbZKOEf1uJPbkTxI5ZC6pdrLNu0V8BSjTranpOXjdNJHcOauP-5S0A8D9IptHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJEmFsrZK5i66K3Zx9WYD3d_hJTq_o7A6MxqUPFvmkjk99uiVfsZme7a5KcQ2g32yO-fUVYl1zgELLgqcCA5K62GXib1xru0NF4s3vpUffnGaQGkY11DmeluWkzK4UQzq0oKZrC6Mo6CvXgdLvjzmIl5ZJA2RqWcp93EfrD0UHD-Cwi4EMlGbcSKHkzcj38BwncAfFantQEhIcRfqJTqIXCTdis5i6KHaz-R3Legjs4brqyA0G_7E69nuHmk7kVCxD9ccvA8p_pffWkdWmuSqJMy_FzZbxgFVmO2c03PHTr9u36MtlxzJIpLQanCxYtEblDxGJmqyO7CeV9df5yvIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=bz0bSZs24GZORwmRv_aho19lx1KWfv2p9zrnLKSAF7o65S37DwPcXRP7zop_X5ipzhn-S9uB5VHDh2nB1RND-rI_JudOOJvnMzx4anO271Ks6Mb2v8v73N0FJuE1IAdKwf5SmAEtc0abBW1mnfTd0-ZswJz6QD2Q2YuwdPv2EMKYXmxty6pK01M8STN2RyTry0Tf5ODZF60N4Zq6ozatrtz-gjrP3tZan6jdOcMuWEtsnAQU2JKNGLrbbEtdpofdpBD7icbjGaCTB7Lpjv1TxH48UUfl9yECOj7teqNQ_C6-1v9tNzZU7JgT6tKZSuNf0CxQtfQnafkWGrE9RB7mpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=bz0bSZs24GZORwmRv_aho19lx1KWfv2p9zrnLKSAF7o65S37DwPcXRP7zop_X5ipzhn-S9uB5VHDh2nB1RND-rI_JudOOJvnMzx4anO271Ks6Mb2v8v73N0FJuE1IAdKwf5SmAEtc0abBW1mnfTd0-ZswJz6QD2Q2YuwdPv2EMKYXmxty6pK01M8STN2RyTry0Tf5ODZF60N4Zq6ozatrtz-gjrP3tZan6jdOcMuWEtsnAQU2JKNGLrbbEtdpofdpBD7icbjGaCTB7Lpjv1TxH48UUfl9yECOj7teqNQ_C6-1v9tNzZU7JgT6tKZSuNf0CxQtfQnafkWGrE9RB7mpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=t7-_d9ENPoN2FdrKQGECFKPIuiZvTO0fSgcObeWg_kqGQfLNuABh7cjWY3ghYa3-IZpJeTrTXhHB3YFsM4knP-W4G__Nhk_-HUmvYUPrlyf_yDkMP28s53e3R3jxoaECgU8hv6M2W0s3Fb4hTGE902tw1vMiAGLfzu93kIcqG_CTn-6G7xcrzhQrXvJ8aVUnj7Ife19G0qruOR5UdpqbaPElHqJRk6sBgu1zzvRvY3-K8oaamgWZrph2ZQipOKqFjCYtNJhy0eyGTTuxkolL6ARYOIVPczMKn9Yb6NyjxFPdd04G7Il_ck3rnM-3CGKhyOcmB-qG6AFnYbQSFvifDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=t7-_d9ENPoN2FdrKQGECFKPIuiZvTO0fSgcObeWg_kqGQfLNuABh7cjWY3ghYa3-IZpJeTrTXhHB3YFsM4knP-W4G__Nhk_-HUmvYUPrlyf_yDkMP28s53e3R3jxoaECgU8hv6M2W0s3Fb4hTGE902tw1vMiAGLfzu93kIcqG_CTn-6G7xcrzhQrXvJ8aVUnj7Ife19G0qruOR5UdpqbaPElHqJRk6sBgu1zzvRvY3-K8oaamgWZrph2ZQipOKqFjCYtNJhy0eyGTTuxkolL6ARYOIVPczMKn9Yb6NyjxFPdd04G7Il_ck3rnM-3CGKhyOcmB-qG6AFnYbQSFvifDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=M_YJJjwYsc14zThDsMjWLwPlMRAg09vGkWcZR-ReYqPZ1uymvAngG22UXZkSd2UohevU60tuYQZbW8YMHNfuTcCH9VeEqFdjQxgEnHhnLXX6nqsDL0fJrjE9nKY2ublT9kQaazwnCv6CLmQVjtTNMMlgTamzSkm4qKD9nHLa83NWIUAIf_bGfRyEjGCAi5FWbM2JdlC0FRnJCCwXqLolmW5SnNoW-0VsIxPOHfxwjHZk99c9vzBVgTrOwJMk_cMZV3-TTxqwEXjNQAE9GdH9ey3-aleGo7vjwQrkvxYte2dVLzizHeDktmh6niNpMp2MpEaLkJkPhukFw3PyW88IyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=M_YJJjwYsc14zThDsMjWLwPlMRAg09vGkWcZR-ReYqPZ1uymvAngG22UXZkSd2UohevU60tuYQZbW8YMHNfuTcCH9VeEqFdjQxgEnHhnLXX6nqsDL0fJrjE9nKY2ublT9kQaazwnCv6CLmQVjtTNMMlgTamzSkm4qKD9nHLa83NWIUAIf_bGfRyEjGCAi5FWbM2JdlC0FRnJCCwXqLolmW5SnNoW-0VsIxPOHfxwjHZk99c9vzBVgTrOwJMk_cMZV3-TTxqwEXjNQAE9GdH9ey3-aleGo7vjwQrkvxYte2dVLzizHeDktmh6niNpMp2MpEaLkJkPhukFw3PyW88IyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m--Lsgag9x5BSx4Khpyu4eLQWdlEril6Lt_g2Aua-V2Jkqg2pcbx1RdCL5U8yYjOYYHg-lKFWkx51P0TAxdrQBeDAMP8usW0oa_DERpaCELMDtTb3tSMhDSsKqzNbY9o94vKLFu6Ty_dV21kda0FlBaRIFk8NI09zSDDeD5kb4zuyt3F5JmyJwdDqB0igu28Qj8AaT3cN8ilw_lxGb3c5vLv-tfG3ISTtYdtRtbRXhHLCjrUVrUj7P3Nns85AZyWQBSu58hpNFrx-Ulh-Nd3OXs5E8i7QV5zRhR0_gN3RoZYoTdkadeyk4_batL9dR6lMZDjYu86jqwUHHFD4F6fPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=GbUjxozR-PQparkLaf0zMerHPi1DhFctzyfnuO8fAy73mtoYLdBrS2t63bUvhM8ZZ3JIMiwJqzS3cVX7S6-JTqSSpSsfl6Mxfuhm33jOz_49NsKGpC21fQtHDZTDO29evVr_0ho50gZCUCst38LMj7wBfPyv42vyQ_uthzBQkKYN9woQ6QJj-9dKrlw0LgcKRy_xxiA_xX5ZJImeNGO84IB23sDViIyRZmYXlngKAKwGKVKhppni8ZFf6d7EU8H70C_1g8qCvb9MEwgXzTsASruoYmI71RnfBNe7si7UDAGLjGdGjjnmQKIkARSB58WjwOHZY-PlYRt126Lt77jcSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=GbUjxozR-PQparkLaf0zMerHPi1DhFctzyfnuO8fAy73mtoYLdBrS2t63bUvhM8ZZ3JIMiwJqzS3cVX7S6-JTqSSpSsfl6Mxfuhm33jOz_49NsKGpC21fQtHDZTDO29evVr_0ho50gZCUCst38LMj7wBfPyv42vyQ_uthzBQkKYN9woQ6QJj-9dKrlw0LgcKRy_xxiA_xX5ZJImeNGO84IB23sDViIyRZmYXlngKAKwGKVKhppni8ZFf6d7EU8H70C_1g8qCvb9MEwgXzTsASruoYmI71RnfBNe7si7UDAGLjGdGjjnmQKIkARSB58WjwOHZY-PlYRt126Lt77jcSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSWLvEhPVKzpWsqn1UJ9ar0H5Tvnkda-6wOqRFD0wtrOG8aVtjInVLEe4crUZOgY5plToee3VM4-aXnNzux6iKHFT2wi6qDpTYGCft7scX_wzZCypVpf4gabh_aLVhtw4tRCaygIGG5E0JWV3VsK5c-FXaudTIoZtpFFUP6Zr85Vwa1awJGGaBrsgJyVA7mhUp8vO9Q0bvH5Ev0-rhimClpU2o-xpbZC-ZIlGBdX6eOwzrK58wLIQg4LKJ8VFohLzmho9I171GUEGuSDAQMAF2pDveO07WDjwIDq0eHZPPi7s1mxffyuo0oFuRRqZaRIjOsxmc1TlQxdcprPORfJtXtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSWLvEhPVKzpWsqn1UJ9ar0H5Tvnkda-6wOqRFD0wtrOG8aVtjInVLEe4crUZOgY5plToee3VM4-aXnNzux6iKHFT2wi6qDpTYGCft7scX_wzZCypVpf4gabh_aLVhtw4tRCaygIGG5E0JWV3VsK5c-FXaudTIoZtpFFUP6Zr85Vwa1awJGGaBrsgJyVA7mhUp8vO9Q0bvH5Ev0-rhimClpU2o-xpbZC-ZIlGBdX6eOwzrK58wLIQg4LKJ8VFohLzmho9I171GUEGuSDAQMAF2pDveO07WDjwIDq0eHZPPi7s1mxffyuo0oFuRRqZaRIjOsxmc1TlQxdcprPORfJtXtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfpmsEJpB2Iqoxf-Y3keY6EHn1Wo2GqkRmIkbU4cvLmpCKMPjXKvRa99oYf1jQXS9J08JA0nV0wDKlYO74sDK-O-b6XjaswpVDcmehX6wKS7tUdRi00IKhQ-Q1Fuy1nfaADUrjx584dtl2Juitza_VgVgSut_1-A1dwzS9j9SpIT3EJb7tunb1oGRFcL8T6NyFHKcuX05Ccz23pcXIgrorFbiJCbGYC_2MIBnU_ASlcRV2YaGwA2ULzCrPuqHxeKDX1fimmiiTR_necykcuAwslx64DUph-mny1DSDbK-s0SLSAuX-vVrHGTNRPbJDpb-YRNi7QfSG2kJADxBQwMNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=CsdHFpYb2aUlYuHERU6aM71HcNkgKGpL46ApmkQFS3e7KEjC4K8QGIhTA03A3OpIFhhiV8seKGCRH_WEp3q-brnzXK4v7FjruUAetPEtGigbXftms_lwYtsdFgGYOWm7OupUBiwTOL0j8JQf5vDWI4_xuaeIAQd1IsU7Xzs9sMc6SIOE0caGhEe47mRHRz-15YqHEZk2N3xGshYaATBgPngNw4QRxdcIwbAlJ6mEdcxKvECt9xosgCJ3QJau8zh_M0vNjfXxj0mfVAVjOb8G98MnAUmBBA5_ksqFdBQ7QYutbQew8Ll63cD4Llu49H81JZt_49sXgofKzndrCdRi5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=CsdHFpYb2aUlYuHERU6aM71HcNkgKGpL46ApmkQFS3e7KEjC4K8QGIhTA03A3OpIFhhiV8seKGCRH_WEp3q-brnzXK4v7FjruUAetPEtGigbXftms_lwYtsdFgGYOWm7OupUBiwTOL0j8JQf5vDWI4_xuaeIAQd1IsU7Xzs9sMc6SIOE0caGhEe47mRHRz-15YqHEZk2N3xGshYaATBgPngNw4QRxdcIwbAlJ6mEdcxKvECt9xosgCJ3QJau8zh_M0vNjfXxj0mfVAVjOb8G98MnAUmBBA5_ksqFdBQ7QYutbQew8Ll63cD4Llu49H81JZt_49sXgofKzndrCdRi5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4iTd6cTU9wzI4p-__eeHeF-FZCkyAeVROAwuqSjhoDXgUoG0tYwbRzP5TG0TiF7PQDs-MOW9nVCdKQuwxeqCKjdRQ-0OFaVVdw98VESQK1RBk2Hsbqu1XfMQavWUdJXXOZR8iz3aZm0mN_kv3pnkIdpNao3bNdlSt0sMZn7OkzxAjN0LIqX3uHPS5DHGB7NpoR2qgeOwC_FC2w9EbvkvnCzo34w79hiDtFZBqOmEGEhCnjwEl92YTW6SO0DRmQfHQnyTyZjCZuwAUaoiB1GpZmWj0_IvAZomKHjDSI0Rlk6mUbmI_IuWf2x2DaCzTzGRaDHkEQ--mEq6mwyZCOYYQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=WEED43lRIGk9wsdmFQ4JoVqz6v1bMOL2R-k77ShPfLHgK6vxwQJkVZifWKdvJxPwXAq61K70sZEz7mDrsPDTKsWoPIGL-h5X3vLx245urdCQhlxQr38Auv7DzAowQ6aKfECyX8aIBhGCn7Oz7Wku-4QBXP1sVrGRv_mvEoR98sQiLj7tELjXNshl6XI_gS0vBCrIH25fmdwrT1QmEw351t5nJefcATezNUMB2VIdl-t0rp8a_VZ8MBcsqXA9ngl0MSc_zarq-gKsNKxeiTJ8ezQiswSQpA0aIeqDEoCAKshk_NSs8oIUfm_7IkYyCzxHnDw7Ibog1rnkqatkIdKukzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=WEED43lRIGk9wsdmFQ4JoVqz6v1bMOL2R-k77ShPfLHgK6vxwQJkVZifWKdvJxPwXAq61K70sZEz7mDrsPDTKsWoPIGL-h5X3vLx245urdCQhlxQr38Auv7DzAowQ6aKfECyX8aIBhGCn7Oz7Wku-4QBXP1sVrGRv_mvEoR98sQiLj7tELjXNshl6XI_gS0vBCrIH25fmdwrT1QmEw351t5nJefcATezNUMB2VIdl-t0rp8a_VZ8MBcsqXA9ngl0MSc_zarq-gKsNKxeiTJ8ezQiswSQpA0aIeqDEoCAKshk_NSs8oIUfm_7IkYyCzxHnDw7Ibog1rnkqatkIdKukzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=I79LU7P5FPuWSfBn6gZuoD5emEZEMzyBT6f1p7ekJuwkiawlUSWYWOFGSlplrY-VvqQRBmXpO9ejVneRB_Kfcl66dSASmrMsSRA6KfZf15J96aku_TchKwP64tdsfYlApV4sc-2fnQsP4E1UDmNitx92M_LjjQgPlGfeZSI86Ih-zboJNZQ24GWDEMCPmlEIoRxIpyznlF2Xjaxgr-dQ2ohlgoH_v9GZFsPpRGLN2ST86gUACxyfL1I6G_bKypU7j0ib2JNcka3oNvL2Cz94Zr0qDBqqNLrwpdlLRlCvd3-4CHaWwNdv8mgj6X_fxAsqu5yP3KJq9pSldFzhiFZuBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=I79LU7P5FPuWSfBn6gZuoD5emEZEMzyBT6f1p7ekJuwkiawlUSWYWOFGSlplrY-VvqQRBmXpO9ejVneRB_Kfcl66dSASmrMsSRA6KfZf15J96aku_TchKwP64tdsfYlApV4sc-2fnQsP4E1UDmNitx92M_LjjQgPlGfeZSI86Ih-zboJNZQ24GWDEMCPmlEIoRxIpyznlF2Xjaxgr-dQ2ohlgoH_v9GZFsPpRGLN2ST86gUACxyfL1I6G_bKypU7j0ib2JNcka3oNvL2Cz94Zr0qDBqqNLrwpdlLRlCvd3-4CHaWwNdv8mgj6X_fxAsqu5yP3KJq9pSldFzhiFZuBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=v9kPKAkEjQvoHiSbHIQFqFR7ipjHUYm4a9L4jl1Ke4MeTXO-mhMEW2dCP2thSZZir04mavGZY0cIbvUKPjSu-0sJuA3iZVKCvOz25NgFAqP2fgfbvUxFHcLrz8pThrXBWiOiWyRwxVIdqp7X1-_uWcKi28pboXHf1DsLN_lO8lPkkLZFlZl0fTfwwn5gP_UUjiShpN1eWlznAMSxVzECZgzkaQFePMS-vA92NyglGp1zabJ9y5rTG6Cebu-8smaisvyM4F3zu-_eQ5ria8-h1ClbOZvX6y50C6zINeACfYVHJJAZI_rlxUq3Di1iOOrBcy4WAAmChMS7aZMKzpoAvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=v9kPKAkEjQvoHiSbHIQFqFR7ipjHUYm4a9L4jl1Ke4MeTXO-mhMEW2dCP2thSZZir04mavGZY0cIbvUKPjSu-0sJuA3iZVKCvOz25NgFAqP2fgfbvUxFHcLrz8pThrXBWiOiWyRwxVIdqp7X1-_uWcKi28pboXHf1DsLN_lO8lPkkLZFlZl0fTfwwn5gP_UUjiShpN1eWlznAMSxVzECZgzkaQFePMS-vA92NyglGp1zabJ9y5rTG6Cebu-8smaisvyM4F3zu-_eQ5ria8-h1ClbOZvX6y50C6zINeACfYVHJJAZI_rlxUq3Di1iOOrBcy4WAAmChMS7aZMKzpoAvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=T4o52buAGxS7BUfyx0uAKc0G6uA_kQe9Mi0QmzLp3y3Rcx2H7G_an9QhpPbAFgDh-kmfijn4WpBEM1R4M4VbzSMvJilTQbW-c3HQ5XjbZdqBQuP0GXe60rQQ_WMdTaGalKG_ZoD49XCQjLA6NaTCy44T7sqE_Te34r1NatOHIpZAC_INFkI_pDJKgyC3BcdaEdS1rQvIXWBX3lRxnNvDr_NrZfFBMV8XyTdc44G_9rqYnAvKvMt-mwXk0tk80slTWTb9nCfAcg5o5RPL4_lUDeiORatyZngaTtgrDt-empRu_xNK3SMQd2AyRVs_43V2pvAG4dVVVy4SLa00GifpRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=T4o52buAGxS7BUfyx0uAKc0G6uA_kQe9Mi0QmzLp3y3Rcx2H7G_an9QhpPbAFgDh-kmfijn4WpBEM1R4M4VbzSMvJilTQbW-c3HQ5XjbZdqBQuP0GXe60rQQ_WMdTaGalKG_ZoD49XCQjLA6NaTCy44T7sqE_Te34r1NatOHIpZAC_INFkI_pDJKgyC3BcdaEdS1rQvIXWBX3lRxnNvDr_NrZfFBMV8XyTdc44G_9rqYnAvKvMt-mwXk0tk80slTWTb9nCfAcg5o5RPL4_lUDeiORatyZngaTtgrDt-empRu_xNK3SMQd2AyRVs_43V2pvAG4dVVVy4SLa00GifpRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=GaAzCG6shwbWLBmVFLNeoxkz29kve4cGX8RjfC8MbHHdwH5OCqq-4Q3FH8-1E3sHfKMCNjOC3cMXS-q-gkpy3CXJTF6UyspsPOje_x4x4wVe8pOm8i20foquxQPTa5fmqdzXtRmGsyUK9xFkzQf1nASrY3xjGczhwadQwVtSZMdRVJXlA9XNk9ejGxPjUZIR27YkxFoUhiKTvXbZe1CCm__1gPvypd21ojO7PUyKkMqjrax_ZZfY0L18m_U4DkibYdc30kcw4BNYzrYKH0Ii98HOsux75vmTyFoAnQfJvEgteebl5Y_91rTAr6PqcwXpSbyUQGVIrrwqvvyR2hT_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=GaAzCG6shwbWLBmVFLNeoxkz29kve4cGX8RjfC8MbHHdwH5OCqq-4Q3FH8-1E3sHfKMCNjOC3cMXS-q-gkpy3CXJTF6UyspsPOje_x4x4wVe8pOm8i20foquxQPTa5fmqdzXtRmGsyUK9xFkzQf1nASrY3xjGczhwadQwVtSZMdRVJXlA9XNk9ejGxPjUZIR27YkxFoUhiKTvXbZe1CCm__1gPvypd21ojO7PUyKkMqjrax_ZZfY0L18m_U4DkibYdc30kcw4BNYzrYKH0Ii98HOsux75vmTyFoAnQfJvEgteebl5Y_91rTAr6PqcwXpSbyUQGVIrrwqvvyR2hT_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=uFc6zbbX0lpWm-dW-eIjyWEPpMTIgMiKk8Q2M2SYUcdIOP4k0EkuUtK1Nu8F3RVaAjNAXjDENDTDvogXiI_nisaX2Bcsk6YUyShiZG9_s17pnA3yf23MDie1O5qLX0bzmGuJKsEIL54zAitaBk9PDZdt-DXeh-WSGbooFbyrFKupTrMkKOEKcB526sSwjDtnjPq-cvkD34pSfYpxzOeGeWkM9QX880aTOzRwYv6GRFFAa5t3xkR7akz5g51AF2O-GqLqcxJbAx0KuSFXTaehIC2otEv7uSyf-HPjWyBACZAR-9Fsfzt4n4sznrQr5gc6vh5eS26_GtmQFpUMszsaRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=uFc6zbbX0lpWm-dW-eIjyWEPpMTIgMiKk8Q2M2SYUcdIOP4k0EkuUtK1Nu8F3RVaAjNAXjDENDTDvogXiI_nisaX2Bcsk6YUyShiZG9_s17pnA3yf23MDie1O5qLX0bzmGuJKsEIL54zAitaBk9PDZdt-DXeh-WSGbooFbyrFKupTrMkKOEKcB526sSwjDtnjPq-cvkD34pSfYpxzOeGeWkM9QX880aTOzRwYv6GRFFAa5t3xkR7akz5g51AF2O-GqLqcxJbAx0KuSFXTaehIC2otEv7uSyf-HPjWyBACZAR-9Fsfzt4n4sznrQr5gc6vh5eS26_GtmQFpUMszsaRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=ozFtpQimLxIFlf4ynigEZ5ktg3v9FkH3i-NhrVajkTyEhff-ca59GaWm-_tWwzU8wXmPK7MT9Lyok7blNn8xA3hilk9ZYS769mWYgp3vy7REo--vHwEUfjgFFqU4s4unyj01EYQ05oOoVGKlrzrYsChn0Ed10db6urX0b-IYYeQA23eLCqhleGQ_bV4SoD3QwuvD_SyzRERkIB9nR5cCbZ_aDPaEMxu0uofidzy_2VUvuqkFLOvpFEADsKKeyFEbXiueWA9cvZdOmZsBHsybv_FzN5ElyWodzCvLWIMgmBPO8XrO_A70EyxA7D1kS-F5yjM8YhpV_gxC35ehRTag2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=ozFtpQimLxIFlf4ynigEZ5ktg3v9FkH3i-NhrVajkTyEhff-ca59GaWm-_tWwzU8wXmPK7MT9Lyok7blNn8xA3hilk9ZYS769mWYgp3vy7REo--vHwEUfjgFFqU4s4unyj01EYQ05oOoVGKlrzrYsChn0Ed10db6urX0b-IYYeQA23eLCqhleGQ_bV4SoD3QwuvD_SyzRERkIB9nR5cCbZ_aDPaEMxu0uofidzy_2VUvuqkFLOvpFEADsKKeyFEbXiueWA9cvZdOmZsBHsybv_FzN5ElyWodzCvLWIMgmBPO8XrO_A70EyxA7D1kS-F5yjM8YhpV_gxC35ehRTag2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7fJ3VPG86KeXz9ZTEes-DiRPdBzCvxE2mBRBYgDQCZIZNCxOQNaLW7rRxV6FvW4ND5XlQTIKa-j-JqfP2ScK8wfDdRsldaKyNWOA6NMcdvxAthad-QaGl4O7TrV4LYu39IOlw5I_7sCg8_ZBfYymkT9fGbD7az5I3611C4BLo1QOhnvlzF6tXcc9n14eNJLGY-sCVt1nCU2AL2_FMUqnxLJmHH4kDdxMysMR-yhYKZ-2B_4KdK-PFOVpgHpv9TQySoQmIBn4BtCfIqgkmTQLEcISF-gD4vTLESHx6dCMVGOyPLZIkG9Oe0cVV9vVPa11yel5FqxmSdwUK6nP9LrTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vobFXKezbyp1zWiLhNHJUsKUc_eAqNZLNa80ZPX9IJRxXND5Z2EaV-nStvVWDw932Bii8Yrc8yEXbOUnxF9DJk7ZBExz8K-ig5l2r-xT8dZn-6JkVFLGXI7VpnVT94jTefi2z_4q2LvmFtc404j6VAsJz4d_3wsq44BQYisGWHXC2gA4BbiWY8F6r9e88kF_bwrFDue1B0LsbauFQjLR4FWMm23whYM9UNp_etP2NRNz1y92RfDbCEVDrbMlR4T7na_DtinLQcSQ1DPe3nMn0qmLd36Q9kLPTkIK-CcAsN0S73UDjOweb4uc1bp_SeAhFdCRjm0rqpSJtrOMl-Ouew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-ZNhW_gZWLt7fIphBpn4YrkVUEQGZSHQbLKHriPjSBst8228XSm6PhSGOX_vSgSUGA5IaLiS57Sv9l--HLnHX69oG3G80RVnyneWs9FqJUaRaRK2vb9bCX2P-GdEl-Up3xqYwyxISjYtfNzpV0EZ1mIYqrRx3yAdCNryh8s503vqB6fjtMSIIuF5GgktIEt8-81LfCelzG-85nE6ncLMNKYjXuMeWg9Gds79Dsejg7GyTmG6h3oT3mAr-cVKTy2RhhnviV2zfYgk6FjKAckhL9zGpiEgryIJjxRyTjVRgq_m7vpn9-LMO2lI3sCDh7I87EqTPwSV_9Lt-9oFZh4UA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=ObyhOmyNjlY6UCn-BYPOWpDJM6-3hSKP2iTJrax4MGGcV_zMiC-x4M4MVQR9qMs0j8ciY55yvZU92nQtBi1pk4AqHK8ozO31EbgZ1Qe5fduVEni5FZsNnLPuisT0XWUTQceH8E9BxX5QHsF7kA3AtXlrtW5HWql7V4mKUds424K5cOFmo3xkmVl7oCPXbb6Xm4zlqIJKnUIxsB3N196MJAsd2dY0WPzIMXrZa-Qhxba5dLt3rXxeENDMr55kwJWHFNc2bsWv_i9oMITtSSQlxoLZBytJRI_xZH9p5HGNXOI-q_R8obbsdVaFf_crNV_D63la9KbIfaZGIyLfp8xVHKsicmBsNecTiwHB7pQ3CKuiZqC_4g3FlCHQ8KQttvK6fLiA9rI-MOHn-dnvQmQ2F2cnN5OXFRABysFet7gLS2Ue6Xxqx7ig-5LYyiRWB0uzgAK9sTKD0sMQyvsy2b5nOudXpEtepLVu_cXXGN3M_ipvpYITdslWkrM8AGQATPPtUyYIUoA_ZsOGSxZJoLnTCGFgCgJfb7DincRan050Sw4gcZZJ4RcXRzX3jLgeIozY_EnXf0FP7xErKoU4UwpWygBlh_RwBfCDZzjkip3UOa1bosnK9a_VG3oLdp2YQoezupuHp1P8_0SXBkqwktpqznclUZvbhJueVPZxP4JtnMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=ObyhOmyNjlY6UCn-BYPOWpDJM6-3hSKP2iTJrax4MGGcV_zMiC-x4M4MVQR9qMs0j8ciY55yvZU92nQtBi1pk4AqHK8ozO31EbgZ1Qe5fduVEni5FZsNnLPuisT0XWUTQceH8E9BxX5QHsF7kA3AtXlrtW5HWql7V4mKUds424K5cOFmo3xkmVl7oCPXbb6Xm4zlqIJKnUIxsB3N196MJAsd2dY0WPzIMXrZa-Qhxba5dLt3rXxeENDMr55kwJWHFNc2bsWv_i9oMITtSSQlxoLZBytJRI_xZH9p5HGNXOI-q_R8obbsdVaFf_crNV_D63la9KbIfaZGIyLfp8xVHKsicmBsNecTiwHB7pQ3CKuiZqC_4g3FlCHQ8KQttvK6fLiA9rI-MOHn-dnvQmQ2F2cnN5OXFRABysFet7gLS2Ue6Xxqx7ig-5LYyiRWB0uzgAK9sTKD0sMQyvsy2b5nOudXpEtepLVu_cXXGN3M_ipvpYITdslWkrM8AGQATPPtUyYIUoA_ZsOGSxZJoLnTCGFgCgJfb7DincRan050Sw4gcZZJ4RcXRzX3jLgeIozY_EnXf0FP7xErKoU4UwpWygBlh_RwBfCDZzjkip3UOa1bosnK9a_VG3oLdp2YQoezupuHp1P8_0SXBkqwktpqznclUZvbhJueVPZxP4JtnMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqhqeyGzrCg95nCqUwZxjPGK-2xT4vFgdHkcWfwm9OhMHawZDsKJpcvMBpY3zndawjAOGqxbBWaJWbLEn5-GdhrX-oEUlVg2mYrNglnRB8_lER3_uYuKBRbniASJfNaEymDUdTxlWQiBub-vyefTqDxliLgkopwHMx8JUyQFPpDGJOu9z3gZyKQIYu8CTaiTLFFpLiHnj4E2vkXxrhAFB37BMZCWbKPmofNpK6OVohW4LwDIYwC3idl5V8hW_2OM5jE89IxqU_DWzfL5jFaHkEpVY8d-WDERVgrzgbdi8UPwAfPbPKTbs1pM1YXTmCDRMQEmAhgmCoBG-Z5DyI6Qng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=faCC8a4MClGahq9CVZG1FW55LxQPdKBxc1XZSl_USjTxdHMwHYtw5eo0ef68vcYA4nv0na_rLQ3i5Q_VawMgtFpYYucz7Q8nD8Z6EYqZ5SjFzChEmThtUK7m7TzVq2ye-o1qPNPaxcSJBTHnzh_jKbRRScw-rKDNlMJ-7RJQMOc-exP5h_UvM-pLLS_fs_Q9kfeNt6foGzRhlrZI1Ndw9EVBt5e04WTlO-WW9xEbgHVUzOudprEAt4YnY6OTiDBqUqH-VVHlOPE5R1YBOI2LBYlnvBjcEz-LdVVsUPqu7yn-j50_zOJ4ekAV2s7qwfE5GMDegDUuH6H9Vlnu7g6WAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=faCC8a4MClGahq9CVZG1FW55LxQPdKBxc1XZSl_USjTxdHMwHYtw5eo0ef68vcYA4nv0na_rLQ3i5Q_VawMgtFpYYucz7Q8nD8Z6EYqZ5SjFzChEmThtUK7m7TzVq2ye-o1qPNPaxcSJBTHnzh_jKbRRScw-rKDNlMJ-7RJQMOc-exP5h_UvM-pLLS_fs_Q9kfeNt6foGzRhlrZI1Ndw9EVBt5e04WTlO-WW9xEbgHVUzOudprEAt4YnY6OTiDBqUqH-VVHlOPE5R1YBOI2LBYlnvBjcEz-LdVVsUPqu7yn-j50_zOJ4ekAV2s7qwfE5GMDegDUuH6H9Vlnu7g6WAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=vvpFidf464avdFpWg_bDvUKZBEIETtSILxfHOVDYCsjeCSyu276j5_H_fCMnXrpb9F-JmLfBkDJuNHca72IEzEJ52tWtL0s1UzjOspP1gHM4mIpjGEslt--AOo0x9s9SWu3vOk8JLbKq45iwb-g7i4oAbv9aJgWuqj2dGMBgFMEmAuYzMBIJqY_UGD9Cu8cmA46NCU7HkE_yJhIPp2B9Gw_iRoubcqk1dDOamc6D8CfPp16GjTvXPRy8ymEU5iBht0ODa4fEBgN4pWVVUgFJafXTgrF3NTK0M4FQM_B3oufL-ztU3zy1w8Kcxi8N-j6kVfh5xq3TccBgLfCBNerK4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=vvpFidf464avdFpWg_bDvUKZBEIETtSILxfHOVDYCsjeCSyu276j5_H_fCMnXrpb9F-JmLfBkDJuNHca72IEzEJ52tWtL0s1UzjOspP1gHM4mIpjGEslt--AOo0x9s9SWu3vOk8JLbKq45iwb-g7i4oAbv9aJgWuqj2dGMBgFMEmAuYzMBIJqY_UGD9Cu8cmA46NCU7HkE_yJhIPp2B9Gw_iRoubcqk1dDOamc6D8CfPp16GjTvXPRy8ymEU5iBht0ODa4fEBgN4pWVVUgFJafXTgrF3NTK0M4FQM_B3oufL-ztU3zy1w8Kcxi8N-j6kVfh5xq3TccBgLfCBNerK4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=Yzdv8SIOhW4Kqc8JPw0fciSuRIOgjhXuhq8GTt4AH6zW60uzmNHiqvdHpIGuLI6kl8WO25xU7z9qtcQAgsckN8HOYmwkbRHAUFlOXy_PeA6LDIVknkq0PNn1kZ-TMoWkkiV4MswiiiHcWLM5hL3MyWv00pfeI9nluxPHySWBeDtLMqqUUi1ReVe3JhWYfD3cUTyNTw5_DJCH2wCWuWiUcrfiADwd7LtV0M4RJ0N_Ck41rDVfPQ-qVOWc43H_z9e-9ct4FWyfc5xUQgbSKcU0zQWY3r1MZhOU_5HAkMPEKSjbMqmGz2q2f6K7_rbURNNwVFOrgKQb33LJmbFYxuN_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=Yzdv8SIOhW4Kqc8JPw0fciSuRIOgjhXuhq8GTt4AH6zW60uzmNHiqvdHpIGuLI6kl8WO25xU7z9qtcQAgsckN8HOYmwkbRHAUFlOXy_PeA6LDIVknkq0PNn1kZ-TMoWkkiV4MswiiiHcWLM5hL3MyWv00pfeI9nluxPHySWBeDtLMqqUUi1ReVe3JhWYfD3cUTyNTw5_DJCH2wCWuWiUcrfiADwd7LtV0M4RJ0N_Ck41rDVfPQ-qVOWc43H_z9e-9ct4FWyfc5xUQgbSKcU0zQWY3r1MZhOU_5HAkMPEKSjbMqmGz2q2f6K7_rbURNNwVFOrgKQb33LJmbFYxuN_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=GJwElKOrOzhQNHVcrtsJTYpDpxjISxgzVvVT0qIECkm7ozn6uiwn_qyZl_nrZQJuqcOnrrtee3zVV8LjM_KzvVtEUk5O_YImLi6wj1wcVv58EMbTxpk8-A_UEkotDAXivyV11Zw0t049GxAz_jiXt29R0sGzUiHGu19szv3vrfnLsG6scMDmTDPFXkSyQHYeVN2aL4QfsDAly9_9OW1baxwmezMGSaxfCNRP9pBelclubdzz3t5WVwjPdmuCYf05LwSOK6zCRGetkZ6dHcjJeuGuRPmfF0ptm42-GAoRY9uTOWseLFvQKwf7XwkuFAmLjC-Q7lok7GGug7wqCqo5ioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=GJwElKOrOzhQNHVcrtsJTYpDpxjISxgzVvVT0qIECkm7ozn6uiwn_qyZl_nrZQJuqcOnrrtee3zVV8LjM_KzvVtEUk5O_YImLi6wj1wcVv58EMbTxpk8-A_UEkotDAXivyV11Zw0t049GxAz_jiXt29R0sGzUiHGu19szv3vrfnLsG6scMDmTDPFXkSyQHYeVN2aL4QfsDAly9_9OW1baxwmezMGSaxfCNRP9pBelclubdzz3t5WVwjPdmuCYf05LwSOK6zCRGetkZ6dHcjJeuGuRPmfF0ptm42-GAoRY9uTOWseLFvQKwf7XwkuFAmLjC-Q7lok7GGug7wqCqo5ioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TM9aqkyFlunuYwhR047DIRFfJbR7jW8cB_DhpcLzZcNFEILyHrcaupGAcoME-ki1CGjm1nb0jzJs0tNPOvCN7a5Xva_fNN5rqwR9DP2_QZvPseFFb2FXXn4l_1MMwk3B7H2PvbBrDZKM-LqjQY6MClCmdGkXn_F7fl-LHMLCoMPDKhCaNDwD_m2YcdhxfbwDvlRZdlumdW9_UdQwlA8eZp3oeHIs2fqQiSI3VgruR3MeSVbgCa7G9R_k-d36bWtMaLM2ikKAeycSReIJbFkczMoLgXBfMvRahMtWS_WNDG5tKGjR3IpGCfMpLpaCoFSgDLCjRlM0zaKwKpAjLOe8iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ghbq3IIXgJOmDjDb-F82lTJGJtaZxX9DBqZfrcZ4KDNZfCuTxi56s8aVUUU5JPdSO1NebntaDQbfXz2UA_kWKsye0Tg5aVmp6CGLbS0aZqq43BL-fogACvnF8jPj6CGX1wnkh5aUjxg3H1B68igg76ri6ITeu723ySrPBMdLGn0xd5iw6PB8zr3nVGuc6pmGHffbdRcVjx1ekcLwMfBVmokxWZU0yTNvXPzzScKGrSOSCPOxqAY5W9YHbI31_MAxiA9O4YgeyvxpPrQrDRWOQcQuBBKzV7rGgrpML2_GrVWG88Zo4JiRGp_aGYFzh1vNm9ywK6XNctQyyX5HhhPPWQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=gXFErKKoFxgJWJdhiH9venyur_Lk8K_XOdtgWdJ83M5BkM49mqSFED4bDRWRSpF6C5Gei2gtCCfBjjzLSiwyKGtfMuyq0L26vJl-dxDo5WLmTOWdfoM0rFlkW3EuRqS0TE2EGNA6cmknWfuGM4FoSnSQokRoybtmn6wRU03x80H2hpIurcqiQn_CHioZD8ChZzLOyumEoYc6CRByYEWoRXReGyi8LUZjsAA1RHHjLOrZuxOKogRB-_dPd0QP-tJuGbMuG3oXOmQw8Pz99OOCrhmnyQCEUlz6fBSUW_4lR361plHFHLuIi0S8Csc8BXYUtSyQO3ygQ4TLBeV7xNA9TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=gXFErKKoFxgJWJdhiH9venyur_Lk8K_XOdtgWdJ83M5BkM49mqSFED4bDRWRSpF6C5Gei2gtCCfBjjzLSiwyKGtfMuyq0L26vJl-dxDo5WLmTOWdfoM0rFlkW3EuRqS0TE2EGNA6cmknWfuGM4FoSnSQokRoybtmn6wRU03x80H2hpIurcqiQn_CHioZD8ChZzLOyumEoYc6CRByYEWoRXReGyi8LUZjsAA1RHHjLOrZuxOKogRB-_dPd0QP-tJuGbMuG3oXOmQw8Pz99OOCrhmnyQCEUlz6fBSUW_4lR361plHFHLuIi0S8Csc8BXYUtSyQO3ygQ4TLBeV7xNA9TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=K-B-PUpT_Gi122FpWyy_iKEGUATBnFEFmyuvJTl2kVhbv4sJlZzp8cKMfDjQ7gsi4ECAihO1Rt2pVEB8MGYJCSJZ7mY0FNytcaCXaG33F_lR66HVwAtqze97nj7i67hqr62g_lmj90fp2HY2IP915qMZFncHWBgTINFhrECK2ovAQEO-5KlCuMuFxCAw4w_HuygQNKNp2USqRie-oBnx8qYY2W8G9RL0fVuu9IH2dPqpudw0dH2674xmvTHO2NmZ6WGA9umMjwuySjbYZbQ7tF1QOd_roJ_GV-zH48wqylCP7XP65b5xNsGGJjce2EFPgp6rtY2MjX8IgLdiFFM8rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=K-B-PUpT_Gi122FpWyy_iKEGUATBnFEFmyuvJTl2kVhbv4sJlZzp8cKMfDjQ7gsi4ECAihO1Rt2pVEB8MGYJCSJZ7mY0FNytcaCXaG33F_lR66HVwAtqze97nj7i67hqr62g_lmj90fp2HY2IP915qMZFncHWBgTINFhrECK2ovAQEO-5KlCuMuFxCAw4w_HuygQNKNp2USqRie-oBnx8qYY2W8G9RL0fVuu9IH2dPqpudw0dH2674xmvTHO2NmZ6WGA9umMjwuySjbYZbQ7tF1QOd_roJ_GV-zH48wqylCP7XP65b5xNsGGJjce2EFPgp6rtY2MjX8IgLdiFFM8rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a731J8eSZw3mD3LdGcmWq89zrwetLg_LU1TIX7FlmgPApDIHxw6I2IRJSV0q038PjTlwiOrB1whFEFdpihHI2bGRFWgdaBkxgJpxMStgXfwEYmyGdfAEwR9LSS7UTclL1M-KDNIce0o5hzgVLP5aoU-WDwpdrTI48FsnbJECHDiBq4bLAcyp7hvGiYX8ed4J1X66GapLThCctoi_lXfE4zpZm1fNGrKDOj7c1cP1piGJD51EFC2PPzTf4gjHhGuYyqekYa30MueQorlUYkQZtSE2R_D3-1I247ld4Uocj8Wjz0dJuj6WGqQTMtI7pySOM6GiLsxRlH0PY99Qh_AXrw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=P28VGpvC1ATP-4UDKXEPoW7rZqSpLkw8C6VNV_ePky_-ogyr8n8FyAR6cXkcVfnZzK-awxNcbl3sQGTDbGD8E1NzXd44-IS_yrH7wpH4R6MfUou4Tef67y8uz2kLHbDkvD9d_LM5BDCeWn7NS-gycSDpRGKvMnQOGsB_-lnZII8FZ8KQk100CWP0h6vrbIYs25BcJDCemsKxJF04-1CERvCV4aSi8-sX7pbliYUqhYqjFDk_TN-HVd6N9RnUPP9tfYKDjlfXs3YUwOj8dlkXq-SVXXrTcBw8veagyCNaOyssmEj7wWeyLygQayPWHn6Gea27pgPGy7_eVyAGYLEhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=P28VGpvC1ATP-4UDKXEPoW7rZqSpLkw8C6VNV_ePky_-ogyr8n8FyAR6cXkcVfnZzK-awxNcbl3sQGTDbGD8E1NzXd44-IS_yrH7wpH4R6MfUou4Tef67y8uz2kLHbDkvD9d_LM5BDCeWn7NS-gycSDpRGKvMnQOGsB_-lnZII8FZ8KQk100CWP0h6vrbIYs25BcJDCemsKxJF04-1CERvCV4aSi8-sX7pbliYUqhYqjFDk_TN-HVd6N9RnUPP9tfYKDjlfXs3YUwOj8dlkXq-SVXXrTcBw8veagyCNaOyssmEj7wWeyLygQayPWHn6Gea27pgPGy7_eVyAGYLEhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=RXWMGUrzcFFYRU0-gkXrsOCZPiJsEzgLZMAeHmB1TXidW3H-0exCjnGYmvxyhiToq_gCkhyNj1cSB3b3_SGPSjNy8mh_tjHBGIJV3vf3E_Nz3vsKSXCKyQrvbJN7KFtJ3Q-5HMC0w33lTQSiTTaFpr0eiEvQM5MVk14Bv0th2oZPSoE5ZQdDTAxIviAjfydRM1wnLTAaJNhtLura6sTV6iwfT9p1foI8X2AAvtDDRHwQ63D1kexBOwvn7XO8KhGEE5OcSFpXSJn5t3c4Au-PvAWsJqBLe2L42Sh0knz-Zfc8-Eb4K-zeoI22rKg9ibL8nVxSuoZoW7i4Aolrg4RErQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=RXWMGUrzcFFYRU0-gkXrsOCZPiJsEzgLZMAeHmB1TXidW3H-0exCjnGYmvxyhiToq_gCkhyNj1cSB3b3_SGPSjNy8mh_tjHBGIJV3vf3E_Nz3vsKSXCKyQrvbJN7KFtJ3Q-5HMC0w33lTQSiTTaFpr0eiEvQM5MVk14Bv0th2oZPSoE5ZQdDTAxIviAjfydRM1wnLTAaJNhtLura6sTV6iwfT9p1foI8X2AAvtDDRHwQ63D1kexBOwvn7XO8KhGEE5OcSFpXSJn5t3c4Au-PvAWsJqBLe2L42Sh0knz-Zfc8-Eb4K-zeoI22rKg9ibL8nVxSuoZoW7i4Aolrg4RErQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCZGp44mmE2r8w2fhutMFBKPfp-ISF0yVb9Ok0FTUaaFwd_yGpUOhYIiii-d81gMjkBgbhPogiOqWgu6Pa0lvbrD4akGYKfjvHz_Ib11An2MvrcRMKTGtUpNy92xpSePXcKchWoceE2sjImyXJJaUlT0cOMYtW1_XqqXz0wKEtwnOnMR087b-2-hSp8T5OVRKn1qHpJQSieMhe4NVGxVLHT2qh7tfQLh2gZFXcXZIjonxWLpE5CLcFVSaNOcKDeFIENkmjWaZF7FV_9Z7bBgK1GR7MJ7UmaGABYsaTP_I21F0jNaSJ5y4F3eIS7jdkZZIW9DvJ4ql4D8UDf5wMwMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVplL7jlP4s0x8j_TOsf33VJZdgqsM7zQctadA5zZdXd03yBmEXUTFNEuimjqa3YHA4g0ozYAcMZ4DOC01tVEzywF7cTFsDnWtmT9z-0rgSPrz-Zl2FAnTlIKcdtDyj5-1WtHuiwUCoiCixsV2A62moKbLKSCUoDHjJ52Ooca2JJW0jcaWv5Zv4qMBQo3pEChy-naHDMx4rnDdgtKjTvAmi8YTek03m-fFCkoV1C0si3Q88kpO0sKSaSa66p4zbRfvLEfVaBvyXuKCux2pbNIp3sCe3Pe2XZC9E3TD_RtD-X8HqHMM-6RLb6vkIhVFLapFG2Q4wYyYu0-RVhIQrnlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
