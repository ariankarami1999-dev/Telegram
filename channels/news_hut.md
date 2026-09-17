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
<img src="https://cdn4.telesco.pe/file/VHa-eR98vradtqzR8xtJ1_vEV2jaCyfVwjGtR31hyK81_MdXJ7QBOXY08NdNlIzf4wMWJ6Q_aQSwYmGGbogK770ent1mXgT53WKauAOvXr8TDp3FacRySC2I-9fQLRY54Y18DUzcSRRbMNSy-bH7akmGC5T6wqIVoyyzJgj6ouCreAEE0j-qHz5RWM7abKaPv0aZTjBJZdW9fscOsMFuDXopyw_7hCp1GoTQPaA5MLzfKE8tH_ee9fYINbcCU7SpHBNheb2OKn7fWGB_xllKx5KPrVjTvanS-2eeX9oiIZoACGMAqGqcBljNesxcNzVsAJkcmNbwMPAGpZsCuPJ0GA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 18:02:50</div>
<hr>

<div class="tg-post" id="msg-71779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=b7_8JdXKo45Jn4FudUaFnxRH_8zch1aPqDQUsreqD9W543anFrHzDmRo9SyBJoh96pqd7Aahnu-G2yS2Uibglz00DTni-uMgtr6y8n5bDSvKcorqmkGiwgRG9M4qnmP8MVkinqWvvMP0SGuEb4DHlT8KX8hh96IiIBuuQk7AHV13UnwIcGDB0Qjlsg_7UAXK2FUbtpp3u1Fj6QwoiYKbB4dRcbr4pZJv_6zIhug4qqHOzWey8opLLJzltV-r_m5AUm8dR_VON27sOoj6gn8pNnCSus4Ztw41ZGjs5tCoNUeATPE6ErGRQSaa3EGoKL_zg-9-jdPz8UUb6BpCPnX2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=b7_8JdXKo45Jn4FudUaFnxRH_8zch1aPqDQUsreqD9W543anFrHzDmRo9SyBJoh96pqd7Aahnu-G2yS2Uibglz00DTni-uMgtr6y8n5bDSvKcorqmkGiwgRG9M4qnmP8MVkinqWvvMP0SGuEb4DHlT8KX8hh96IiIBuuQk7AHV13UnwIcGDB0Qjlsg_7UAXK2FUbtpp3u1Fj6QwoiYKbB4dRcbr4pZJv_6zIhug4qqHOzWey8opLLJzltV-r_m5AUm8dR_VON27sOoj6gn8pNnCSus4Ztw41ZGjs5tCoNUeATPE6ErGRQSaa3EGoKL_zg-9-jdPz8UUb6BpCPnX2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش اهالی یه روستا تو هند که حدود 2 سال از وضعیت بدِ اینترنت و شبکه 5G کلافه شده بودن؛
زنگ میزنن تکنسینِ شرکت مخابراتی بیاد و وقتی طرف واسه بررسی دکل اومد، گرفتن و به همون دکل بستنش و گفتن تا مشکل حل نشه، آزادش نمی‌کنیم :))
آخرسر پلیس اومد و 6 نفر از اهالی اون روستا رو بازداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/news_hut/71779" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71778">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/news_hut/71778" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71777">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUqSkFnpYiHV5n_S1wpkXzLAbgLlF8WO5qVlBWfBoZ8IV3nRdy5wUIeJEYK8GcMHhcY3lOR-yUpgqu74n4xqG4G8q6d09ulyz9zorLWYSLsDwBE5wLgKGGurjCux7CFN2Ui_A__9yGT_Mogvbv4K0TP-crqmL90skbKbuPhaV9xiYTYHUeopYRaPinDCzmKausThA0CtPhjYlbYRCnWaIz725eWtu9QkJregGyNvtedo8V4VkP4apcfon0klowVBoDhZWDkt_-9AB5sO2h3LJciEobcmLExk7XrCrERIzNA7uhAfemujqXZEiiEXhGrw5-3kWiwVD0Z3560kpvmRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/news_hut/71777" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=rfqMDEhI7OvznA4XP5FzbA3uvegcZPx3UkuCoa3skDzxUH8MUt5SbpLTqMJy9JrWVnOelLuJY0YHVQSvPFSgso8OoC_GSeFkU2G1q0PWKUouYBaDEGvxHYSxfOktv_bMalOWAPcNBTqhNIeNPZlFBDPCd2buXzYTLjniT1O-NyjZ9tZnJMlGAEiHpaw975q0Yz6uUksJPcejaTMb6WqJBwzGl73hkXZECH6fVSOxTP5W6VBiUlKh1kjx-cZv67YJgySZtfg1nDjHxDbJqEH90higObWaSlJe5JdGVcsmLq1dL5z2obxr1P0ky2JL01x-8JDAlz9thtyZPqq3KiN1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=rfqMDEhI7OvznA4XP5FzbA3uvegcZPx3UkuCoa3skDzxUH8MUt5SbpLTqMJy9JrWVnOelLuJY0YHVQSvPFSgso8OoC_GSeFkU2G1q0PWKUouYBaDEGvxHYSxfOktv_bMalOWAPcNBTqhNIeNPZlFBDPCd2buXzYTLjniT1O-NyjZ9tZnJMlGAEiHpaw975q0Yz6uUksJPcejaTMb6WqJBwzGl73hkXZECH6fVSOxTP5W6VBiUlKh1kjx-cZv67YJgySZtfg1nDjHxDbJqEH90higObWaSlJe5JdGVcsmLq1dL5z2obxr1P0ky2JL01x-8JDAlz9thtyZPqq3KiN1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تگزاس اونم وسط قم
@News_Hut</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/news_hut/71775" target="_blank">📅 17:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=po88ecTCmfFYBTyQkBJ7CPZljYSPjGioknYTf9Q8LOkl58VGfIxlFzhxzBOviszJYM-SXrBl1EVPte2TqZR-XXK5FhWWmNV6sb2judaFfnEX_KPklPD3QUYrYg1oE838eL1PzjsMlKREpBGm5OJPSTrNyoG49ofrvPXR3rwY_17LxdAd37ryTSjfOgKX05KI8m8ok-r6GGEeceszIrl--BYkV0RUQuCBHiXJG585AS_rnKZkTZDx3WN-igVvE5wSu3_sU5GIuo0Jcv4K4HDHV7A0rRrB2WRBeA9wIVFJD0baOkS72We2mSXWpk_Pe-pomcYIpAvU4wYO6ny2NE_gYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=po88ecTCmfFYBTyQkBJ7CPZljYSPjGioknYTf9Q8LOkl58VGfIxlFzhxzBOviszJYM-SXrBl1EVPte2TqZR-XXK5FhWWmNV6sb2judaFfnEX_KPklPD3QUYrYg1oE838eL1PzjsMlKREpBGm5OJPSTrNyoG49ofrvPXR3rwY_17LxdAd37ryTSjfOgKX05KI8m8ok-r6GGEeceszIrl--BYkV0RUQuCBHiXJG585AS_rnKZkTZDx3WN-igVvE5wSu3_sU5GIuo0Jcv4K4HDHV7A0rRrB2WRBeA9wIVFJD0baOkS72We2mSXWpk_Pe-pomcYIpAvU4wYO6ny2NE_gYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
میل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ تنها تضعیف شده است.
تواناییِ عملی کردنِ این هدف، عملاً به‌شدت آسیب دیده است. ما به وظیفه خود عمل کرده‌ایم، اما هنوز کارهای ناتمامی باقی مانده است که آن‌ها را به سرانجام خواهیم رساند.
ما حماس را نابود خواهیم کرد. همچنین، پیش از هر چیز، رژیم ایران را شکست خواهیم داد. ما آن را سرنگون خواهیم کرد؛ این رژیم سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/news_hut/71774" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71773">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=jM8iszzvkv39uVR1EKXRQt69jsKXtmdimTgUTYxXpc_txlj3efs6hjK_EKxdwM_hofE60uMG7LAERR11xWJZlTIXSlV2M-NTa6wqhmAXQ0Nqam4WpkIUGZb78-V7XYbi0E8bglsMUuLsjdkRMkDQWOFkKYlBET9laMu-t2HNf9YX2ppCAVUfZYa7pYxcJ24wtCQMq39F7RPjSvqyNSiEaMj8hVmXUvTSMr_YfunxRZ2EJ9wS93UPdebFuwfA19-6sQGhwjZz3CgYmut94d8lmUSl2O6jeeP9U-w6XhZ_WWW3eC4vWicYKJyvIpKWpsK7LekEa4egk0ygPIgHIveLXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=jM8iszzvkv39uVR1EKXRQt69jsKXtmdimTgUTYxXpc_txlj3efs6hjK_EKxdwM_hofE60uMG7LAERR11xWJZlTIXSlV2M-NTa6wqhmAXQ0Nqam4WpkIUGZb78-V7XYbi0E8bglsMUuLsjdkRMkDQWOFkKYlBET9laMu-t2HNf9YX2ppCAVUfZYa7pYxcJ24wtCQMq39F7RPjSvqyNSiEaMj8hVmXUvTSMr_YfunxRZ2EJ9wS93UPdebFuwfA19-6sQGhwjZz3CgYmut94d8lmUSl2O6jeeP9U-w6XhZ_WWW3eC4vWicYKJyvIpKWpsK7LekEa4egk0ygPIgHIveLXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو یکی از خیابون های همدان یه مرد به یه دختر تعرض کرده، مردمم متوجه شدن لباس و‌شلوارشو از پاش درآوردن.
@News_Hut</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/71773" target="_blank">📅 16:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71772">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=Be30Td9hnIzTAlkGbUUQdQ__Stkv0t2_z4b_SkmZ5Sd2NBFjhISp0XCrRlsyxXKk_k_PmGdsk9gexqlcXSnHATTUhJODfid2-5jJIb1EBSK-dqKzcuKIXB5bXoXe2X0n2qaco_ZeD5z6ZeB3NAWcogouYSx7bkpGeMoBHDFsoY6npzYOqu71V68TAy7PoB4R6_8uEWpQhPH8vlWeQlFrBZQhhxj_agmD35n9dqglJhJ18y-aOc46kHqAB2AAt4R-3aSNTe_RDUDBmWYPmbTKHO-eHvkBi50DhNWirK_e57O2ates-DkNvw3fU6oUEv0TXdVK4vWgrHhsJ_u214PHGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=Be30Td9hnIzTAlkGbUUQdQ__Stkv0t2_z4b_SkmZ5Sd2NBFjhISp0XCrRlsyxXKk_k_PmGdsk9gexqlcXSnHATTUhJODfid2-5jJIb1EBSK-dqKzcuKIXB5bXoXe2X0n2qaco_ZeD5z6ZeB3NAWcogouYSx7bkpGeMoBHDFsoY6npzYOqu71V68TAy7PoB4R6_8uEWpQhPH8vlWeQlFrBZQhhxj_agmD35n9dqglJhJ18y-aOc46kHqAB2AAt4R-3aSNTe_RDUDBmWYPmbTKHO-eHvkBi50DhNWirK_e57O2ates-DkNvw3fU6oUEv0TXdVK4vWgrHhsJ_u214PHGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو سیدنی سویینی برای اولین بار تبلیغ عظیم خود در میدان تایمز را می‌بیند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/news_hut/71772" target="_blank">📅 16:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71771">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d6312725.mp4?token=e-W-HNbGqS9skzTWvdS_-RXTGRJq4jLf4WR0KaGRza2ZgvA37aQZnjiQhEbqTnMvERbIaqitTio8r-J2GVGtscqFy7SAZmvSaxJbC1SoNxyp0XY9Q3ODDGzdjP8cwgh10zt8-yB7AgAkftdIjRL72BEu994EeuS2UTgkGbQHFhAN-t_lBvk9NU_J_4M0bSRavWHmXBzz7oclg0ImMq2G0OztLXI6Gm4bzWoREGC7xQYSSvpfARDQ-CiVm36Zeb57zdnNbD02KVxgInfH3X7NT3oY5AfOjt1QT_OmeY7bIGD0wizrzVLtqKhrs_5R6oxVZTLg_sazo3q7aaX1a9ZSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d6312725.mp4?token=e-W-HNbGqS9skzTWvdS_-RXTGRJq4jLf4WR0KaGRza2ZgvA37aQZnjiQhEbqTnMvERbIaqitTio8r-J2GVGtscqFy7SAZmvSaxJbC1SoNxyp0XY9Q3ODDGzdjP8cwgh10zt8-yB7AgAkftdIjRL72BEu994EeuS2UTgkGbQHFhAN-t_lBvk9NU_J_4M0bSRavWHmXBzz7oclg0ImMq2G0OztLXI6Gm4bzWoREGC7xQYSSvpfARDQ-CiVm36Zeb57zdnNbD02KVxgInfH3X7NT3oY5AfOjt1QT_OmeY7bIGD0wizrzVLtqKhrs_5R6oxVZTLg_sazo3q7aaX1a9ZSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبرائیلی:
ایران ظرفیت گنجایش ۱ میلیارد نفر داره، میتونیم به هر فرد ۴۰۰ متر زمین بدیم تا به ایران احساس تعلق کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/news_hut/71771" target="_blank">📅 15:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71770">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=ez4tJ2gzSWrtvizDgm6Fek0Jc3NU6OtYm8McAvd13oXx6S1j0idHcKFAG_HlbhYj8kqDWlMjjb_5nvrohgBCUw6GT_PRVDm3vHcMM8oL2kuCjxMQnIwVzih2hZnMkhju5gFG4wScjahiR2dvpNU6p7mJ76bkJ2cJnuzINczmKGEvkY7uyXFylYCaNRp8nS8pvgT9PsG2FZPJ-r8DeBvTcdLEbqjCR5IKIrUVisHdtV35Uu4dqKA5e8eVYxkgpNhLchduDf459DeTGUwQhXzE5XwCkeyKErdfIW9YUwxAYa8WHrvXfJ-8bzO18z6A7IAJjucZjjAziI4UjJGFLq13rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=ez4tJ2gzSWrtvizDgm6Fek0Jc3NU6OtYm8McAvd13oXx6S1j0idHcKFAG_HlbhYj8kqDWlMjjb_5nvrohgBCUw6GT_PRVDm3vHcMM8oL2kuCjxMQnIwVzih2hZnMkhju5gFG4wScjahiR2dvpNU6p7mJ76bkJ2cJnuzINczmKGEvkY7uyXFylYCaNRp8nS8pvgT9PsG2FZPJ-r8DeBvTcdLEbqjCR5IKIrUVisHdtV35Uu4dqKA5e8eVYxkgpNhLchduDf459DeTGUwQhXzE5XwCkeyKErdfIW9YUwxAYa8WHrvXfJ-8bzO18z6A7IAJjucZjjAziI4UjJGFLq13rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این گربه به محض اینکه براش موزیک میذارن، شروع میکنه هد زدن :))
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/71770" target="_blank">📅 15:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71769">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حال و هوای تهران در ایام تاجگذاری  شاهنشاه محمدرضا پهلوی، سال 1346 خورشیدی.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71769" target="_blank">📅 14:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71768">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMArnhiL3obpzA8WfaS9ANveEb2KQpelbtdcSjqnUDAi9KoUpUTxm4RdYPPpakNk29-AeOeNxvVajGWURn_WvW7AEhjyIW-07W6b1fGdXfz3YjQjp2aqUBeo81rihi_HCEcf8_CfpwaY0atD8GzaGPjDPm-4qzwlm9Smkdhxn1roilIarOR4x_IIxOP1AIIo06QRBOigly8nwy-twCuhmCeR6Nku4NymxcBxmptEX3jFng6mdwgfHnoJEVNKmhbqSv9xUPzBwaVUpzXZFAh7nJ_-TViWIg7a18dEzVFSpUg9mqvI5Zc1LUKIVstXnQKGP7Dqnkly54nxHieVAUeY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ده فروند جنگنده اف-۱۶ ایالات متحده، به همراه چندین هواپیمای سوخت‌رسان، صبح امروز پایگاه هوایی «لاجس» در پرتغال را به مقصد منطقه عملیاتی فرماندهی مرکزی ایالات متحده در خاورمیانه ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71768" target="_blank">📅 13:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71767">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0a15Cb7HfDskf4tHZPXhz0OVTHphwVZBKRHSuE8e-_933pQCmpFFWZnysBfYVrN_YKhRUwl1nJbLAeYb0cWGG8Z7hgvuCVd50DKN-EWQTAzepfIT77KYpyXxkbryofbOA6k6OpLwtCcFRfEbvN7z3ExwtsmFT4R6U6gHo5oKHckcaqmrH4XBcyl05dXkG14kMdttt_HAnWo2fToVGVGgrXDmHpxuzQ2J4l6eETri8NgW04Ol_kZwErDr2bnUP49SKjqyfhCmMtS5Y4mddZWKwcjbkt9vy2OTSn6m8TgpAFQ86c4-tYQRjrNPPQ5N7-PBmHydlMERJTVs5lbJK8X0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک به اونایی که بالای یک میلیارد تو حسابشون پول دارن، کارت سفید میده!
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71767" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71763">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKNFXQD22cKhoEG-WYi84hKg0RhVjcghh5VI3QRhEGA3E0OTIyHIAbu2N_AFHpB8bE5pU65qsFxQahcmtZqV5oqvzF5qC3S_A5ytACddmpfMXQ1EYdSq2jpDfftBEdMTJz4fk-EkH226grJvKgmL_zdxosGg0igGkCpuaRs0r8FnjrSrM_JLF9ZYOf_O67Fgaia-Ui971Z5jFhn_Gu0ae6PEaureEI9taCzgldJI8FzFjusxNyBgFdbPFn8jQzQxCJ_0kULykyMc0NImsLyhko5o2jfWA2X0srVaCdvANExky7PjSEXY8kj2ZmC4zzmLGUh4pTNTXScQE3dm3nBMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6wrSEmVWq9ckxF5edkQ-IYDvK7OmqwfXToANRUtuUCL1FwgbkTs7FKQuG92SQrttFhDzQD0OsVIZO990doWXurxKVu_1zkC1NTJIizJTD9bxbfURjQJ8iONDqsbYU7zXshgW56_gNSNV9VDA8zUpTBySWz6mGsc6MNhUKmV5ZfsIKTkSYd8uY5e7qPemHmKcoWp1QlWJAUhjNJLw8547E98wdnxyAmiScRm3bdmvE7xFgD7I7LHtnG9GTGTDHXLBxw-qKt-P_6MNKZiAgzStH7YHAxF0GFbFWBNLZ9hBKGk-lxZ-_9fgPVuzt7esBSYip3VuLPnbmIS79zi4gYnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBvMert7ND8fhHPgspDJhg0tWz9TEBIGOx72qW92iKHmHxB8Q2yX6PJ2SnGU3EG1BECk06CHvBoSsBEDOxvGDA0kKv2AgabGzc3NR8qJSDqfXJPD7V-cmd0q1iAhZWlY-TIwCKK_o6Cl1PZRLaDfYvy3ZlCnxnd4nBFGI1DI9m_YXK4yd-cW3TQONH6E5k764r0Yp5nclcDmkPDAzwfyBFWgYgdKryhpWOi_7E9UQkWeqnqyvwKN0sjeEG1B37vR1XqxKQzB1p4xZhYZLUbzMs4sYgHbsZ_PF-1PpSCXQ-gDZ1ieeLjvn8LfE_HIXo43PSZOlVinUggnaDO8Ac5ZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMrMwK1ROC_79riddj9VfghCbdXLzOCMULMg7p17KidE6QlIczffGGcHrEL7WSp6KyfgodPSEYcSc_x4gSQA8VS05Nkxfrfg6954HdCshJRZE1NTMfxtR0FpHr5x78P3t0IWdL4Mx2aYsSyVSOwSZmo3CILQr7A1EqKHJ_n8xLpQJ1MNFvBYautiooJXf6eY2DNrKAHsTyIy-NOKBCtugcqDwEkcarjsEgNK0zFiR3VaYtuB6H3l5vJxc8h3saheIyhnDF5PlwmS2AM89UJyihVi1NSCXRf8gUBVpB3vEJy1uovv5aCyQO89F6GSqTGPEATMLDP0CXiHvfhMtgi68Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز ۲۶ شهریور،تولد کمبوجیه پسر کوروش بزرگ و روز پسره.
26شهریور؛ زادروز کمبوجیه دوم، پادشاه هخامنشی
کمبوجیه دوم، فرزند کوروش بزرگ و دومین پادشاه شاهنشاهی هخامنشی بود.
کمبوجیه پس از پدرش به پادشاهی رسید و راه گسترش قلمرو هخامنشی را ادامه داد.
مهم‌ترین دستاورد نظامی او، فتح مصر در سال ۵۲۵ پیش از میلاد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71763" target="_blank">📅 11:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71761">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNnP-0AlN55vdKQfinAhKfsGx-WGfNBHQHWeAUGRFNbbvh3H5i_Lrcn7nQXMA1EHlYQ1nE8eg__GeZJmANpQYZeVTbLeznhCncf7wVLT20c_eMIrX4prWGGM0ef5vBtAWY2W3vh0Xy_slP4AvfI146ck_hZlhOixjM3uHSWLBvSehLErDpA7NAFj_AnCIuKkW8tKDDeNaTr4ydwlmiefG8l5ckgKHjGBd7KDp7mIzO0TeK9pNnPv2MLDx3fcZaO_qia-yCaF4PnSTCJXr1G9LyZdyv36DA5JPlnpcQV-IgEHJNNlHY5ntEUxucFt5eqSVevy1QB7zHlg0PhY2Z5bEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=MSU-2qu0HljiIXKguGYCRidGLJis7xyUvwjfP2RhocKFCdDMSoxHqGHqMy4_3ygUsvwC3HUrCjBaokVkTdOd0eZj3UHmCAmGCoEoteSCUCls39fIr4q5ndaiYMYyNCC0vTY3-rWf7Kt7TDoviGxvs1OHBIFSgdrJNyNyDkClrx7PXNIU0ImLMoX1Q5KzoBPZg9TxAwyQCGp4VU1DkhMd_KzY9FKvdRJaypDGok4YgB8W2AE09p5gig4_G2zBbZiS0Dv4BBsSrVjPDXNpYd393CciEG0t4la5vHrv4Dk9BY0Ow5o_EycLkImCsPRPV9A717BIrN2Wojn3GtUAuN3Ptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=MSU-2qu0HljiIXKguGYCRidGLJis7xyUvwjfP2RhocKFCdDMSoxHqGHqMy4_3ygUsvwC3HUrCjBaokVkTdOd0eZj3UHmCAmGCoEoteSCUCls39fIr4q5ndaiYMYyNCC0vTY3-rWf7Kt7TDoviGxvs1OHBIFSgdrJNyNyDkClrx7PXNIU0ImLMoX1Q5KzoBPZg9TxAwyQCGp4VU1DkhMd_KzY9FKvdRJaypDGok4YgB8W2AE09p5gig4_G2zBbZiS0Dv4BBsSrVjPDXNpYd393CciEG0t4la5vHrv4Dk9BY0Ow5o_EycLkImCsPRPV9A717BIrN2Wojn3GtUAuN3Ptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اوکراینی شبانه به یک پایگاه هوایی نظامی در منطقه روستوف حمله کردند که منجر به وقوع انفجار و آتش‌سوزی شد.
حملات پهپادی همچنین پالایشگاه نفت یاروسلاول را هدف قرار داد و باعث آتش‌سوزی در محوطه صنعتی آن شد.
این پالایشگاه یکی از بزرگ‌ترین پالایشگاه‌های روسیه است و ظرفیت فرآوری بیش از ۱۵ میلیون تن نفت خام در سال را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71761" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71760">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71760" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71759">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZSKIghoUhonbP_-GlX9jldNEbmfUuW1NvE5_BXHngVDVlDkeojQuHw1bmRCzJoZUuLg-Ub3AtA_8oOkvd1fxrwGCh0s_NgboT5T58_mNr2ZuvhuDHFSX-YaE1hvrbNRzm3P6KzaVSrn34mkihO5J9EHzyJrLGaCJwjVQFGeF4xrLG5m2GtJ0alYLeMCpTMtyrwPKv2DP6hPsZmWTP3ICRNNrenPjdQnVE-nuP02L_d-TmA8Km18QkFZ6dGEe0tomuLC4Twni5WtAtbrDyVUwinRdx0_sTvk0FLvqbzfBzyRyoZE7nJNLZFjAGbhZKuAzlvotCIdXSw7F6eFnNPBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
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
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71759" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71758">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=UQjRmU9X08Q30VYX1U1gL3Mx4BFhw8QO1H8SBIqAylPxEAVIXdI4pcyvL6HtlBlQNhtZNkLnduTb4LvuRIJ9ZkH0NJJL7I2siGIAXDxXKdvrgkfCPyLinBDyvRDFucB2U3kiZcFMnMhFeZ09CqUwdelsKWoyl4rUUHy4qGgLXgUNEmbeXJTfCbuEK0oPRO25mUq0QCH1uzX_dR6NqvmCVSMqAKHCytikjx5oKIwXeIe-c4buT4iEwiti_BR_0DfNPPwwlO9w-FcE31-FFydwZ6ZgxnAFT9LvcppFkDQRqXkbKeRKf1wSaXbaAuss7L77n_9PCYy_RYV4Q2UxGQdLzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=UQjRmU9X08Q30VYX1U1gL3Mx4BFhw8QO1H8SBIqAylPxEAVIXdI4pcyvL6HtlBlQNhtZNkLnduTb4LvuRIJ9ZkH0NJJL7I2siGIAXDxXKdvrgkfCPyLinBDyvRDFucB2U3kiZcFMnMhFeZ09CqUwdelsKWoyl4rUUHy4qGgLXgUNEmbeXJTfCbuEK0oPRO25mUq0QCH1uzX_dR6NqvmCVSMqAKHCytikjx5oKIwXeIe-c4buT4iEwiti_BR_0DfNPPwwlO9w-FcE31-FFydwZ6ZgxnAFT9LvcppFkDQRqXkbKeRKf1wSaXbaAuss7L77n_9PCYy_RYV4Q2UxGQdLzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی یک تک‌تیرانداز در رقابت‌های ایرسافت!
خوبه که این یارو تفنگ واقعی دستش نیست!
همه رو هدشات کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71758" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71757">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=fyb-JFgVyYqLAmUD-Vau76_mAZ-D4sXBkEZsfS7CWUp70k7W6aaRgcq4hZv47snmkqr9JQOIrkw5HN6sRCYnzqxFOUsxjcR6JlKBLykTLNIFM5NdZC71ovyNZpSZm-s30Wm_ImndHLDqlgq44ayMysXP4zNsJ1g-BKPoFvQqkgbjGxHFTGhwCmR3EnYJi1bDBqY7EHLF0ZCB9zuncdinDD5lZ2PKk8XQzXD_yDlaRNgFyzm1NZWPQC_9ozctiQQQQxV7FKk8dEhNXuaSMYh2s3HgiusNkRvEeC7s8fxALGIdZYUJOimtf2cEVW763rXAqQ28fHdQ7kQHIxT4HUxLkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=fyb-JFgVyYqLAmUD-Vau76_mAZ-D4sXBkEZsfS7CWUp70k7W6aaRgcq4hZv47snmkqr9JQOIrkw5HN6sRCYnzqxFOUsxjcR6JlKBLykTLNIFM5NdZC71ovyNZpSZm-s30Wm_ImndHLDqlgq44ayMysXP4zNsJ1g-BKPoFvQqkgbjGxHFTGhwCmR3EnYJi1bDBqY7EHLF0ZCB9zuncdinDD5lZ2PKk8XQzXD_yDlaRNgFyzm1NZWPQC_9ozctiQQQQxV7FKk8dEhNXuaSMYh2s3HgiusNkRvEeC7s8fxALGIdZYUJOimtf2cEVW763rXAqQ28fHdQ7kQHIxT4HUxLkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات سالم در تیمارستان یمن
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71757" target="_blank">📅 11:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71756">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=kPk5cPzaiHjyavB4oG4VPlbJaJEPhXbQ68_WhYYzB488B_TTibMXWmWb_CCLkVC20-QgqU4eZ_Eg--GCjeL2rDyVrl4lR59Yh-ADFZPPbB4hbEWt5eJ_GKHhf16fMjPopP5Y0SbM9lZwKmWQWFRA9lKzPQwsLCsdEN0PWFzqxq4gd5qeRzw-CsdguhxhD0vzSFTi2mGkLhZ6Urhj0PVHEFXzzUYi8twTyGZVxe5zgXrWov5WzbLJCsL6HK0OXiQwlIYUrE5BoNlTd89m3BHqL6jMxq04fsWLTM6WKIx3r3alyv_MhPlvnuTkfRgITySg9IFBZuiB5wEV2_J81m2tdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=kPk5cPzaiHjyavB4oG4VPlbJaJEPhXbQ68_WhYYzB488B_TTibMXWmWb_CCLkVC20-QgqU4eZ_Eg--GCjeL2rDyVrl4lR59Yh-ADFZPPbB4hbEWt5eJ_GKHhf16fMjPopP5Y0SbM9lZwKmWQWFRA9lKzPQwsLCsdEN0PWFzqxq4gd5qeRzw-CsdguhxhD0vzSFTi2mGkLhZ6Urhj0PVHEFXzzUYi8twTyGZVxe5zgXrWov5WzbLJCsL6HK0OXiQwlIYUrE5BoNlTd89m3BHqL6jMxq04fsWLTM6WKIx3r3alyv_MhPlvnuTkfRgITySg9IFBZuiB5wEV2_J81m2tdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
قیمت بنزین برای شما بالاتر رفته است؛ اما این بهایی بسیار ناچیز در قبال کاری است که ما انجام داده‌ایم. این را به خاطر داشته باشید.
ایران نمی‌تواند به این وضعیت ادامه دهد. کشورشان ویران شده است.
ببینید چه اتفاقی برای ایران خواهد افتاد. نتیجه‌ای واقعاً خوب در کار خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71756" target="_blank">📅 10:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71755">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اکسیوس:
انتظار می‌رود ترامپ هفته آینده در حاشیه مجمع عمومی سازمان ملل در نیویورک با رهبران کشورهای حوزه خلیج فارس دیدار و درباره جنگ با ایران و برنامه‌های مربوط به دوران پس از آن گفتگو کند.
پیش‌بینی می‌شود که در این نشست مقاماتی از عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان حضور داشته باشند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71755" target="_blank">📅 10:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71753">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abM9PyP_pesQ1Y6_G-Zc9toCe0My2kzjWpX2wouZAc-IJltpGEtYPsKCYM-lCtGfZSzMDDyFx8P_OG0wV-TaTUEjWYH5i6c0URG2SMNKssLg8BH6JY6_nxmuIXekUa26t0ngvMukqZF78Cvp09gjwQ1cBpmBg4KwtIFq0CeZLmqxl7C0YA-Sl1IQ_j2Cgfb9koxQHjt8Z5kzVHCUrXZ0hiFtqxiDZvgYW--WJjPiIkRn5YwpdDUws0YlTR2mMSsZzIKCIGURM82EdfXe279i03esV6PhSNaIYBvf_WtfCqPNyj0xRslyU-m8g9W9MibrXW-uE9NtuElnaF3pvYcCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cba858231.mp4?token=TmRr0aiaRMBJ6QyOqybP-9ZJTXMyKAtC8fOtl5TuSzfEO3QOrGZMk0Jiph2gZRCUJOni_0eWQY324mz8yhGAzRsWa-EIBw8MIaMTPzHGT8A7uN31TsM72EEh2mILaLaXwmPRnZ3__mQDQBykIPwvTJmDBwIzQs3jTVwd0i_aVcsGpwKu_Jwo5MtI_qSNqqrc-gskSqbELxxwJMal-WHknCz8nnAXeKwpU9cBLHGcNLlw81paiSmbSYrRaeSicmmvCgF9WH6kGVvnD7F-It8MvsDtieLNCyIdYqsHAteZSAe8RgtICIig8ixTNo0YYfi9Wbi_1QFH8Y4yRfxL9l6ZEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cba858231.mp4?token=TmRr0aiaRMBJ6QyOqybP-9ZJTXMyKAtC8fOtl5TuSzfEO3QOrGZMk0Jiph2gZRCUJOni_0eWQY324mz8yhGAzRsWa-EIBw8MIaMTPzHGT8A7uN31TsM72EEh2mILaLaXwmPRnZ3__mQDQBykIPwvTJmDBwIzQs3jTVwd0i_aVcsGpwKu_Jwo5MtI_qSNqqrc-gskSqbELxxwJMal-WHknCz8nnAXeKwpU9cBLHGcNLlw81paiSmbSYrRaeSicmmvCgF9WH6kGVvnD7F-It8MvsDtieLNCyIdYqsHAteZSAe8RgtICIig8ixTNo0YYfi9Wbi_1QFH8Y4yRfxL9l6ZEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">« امیر نوری » بازیگر؛ چند روز قبل یه مصاحبه کرد گفت خیلی پولدارم و فقط میخورم و میخوابم و از زندگی لذت میبرم. حالا دو روز قبل چنان تصادفی کرده که با سطح هوشیاری پایین باید سریعا جراحی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71753" target="_blank">📅 10:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71752">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoQQY08Fw_ID2GPb1amnn4RIOLAPpiDkmFGK9I7lJoaQyt4zwGxOxOMPUQU0r33_WYJCx-W36U-nn-Cwk1lj3bJwSZAgCcVu9LbTJZgWx7gce-vE1ASyw3HfI-FwYjLq_Yc8Obu8jG9frLpdeFsWEjC3AXAgKfNzZuDQLFc-BDwgyksOJzfDfPeVCZ8c4n6n8lDKN3cLHmIWxbzmo0-ZLkDq5n7D7hVFcb-vjizWoaaAclSZBGYmVL6soc9ZimoFZ1qSEdm-gvJbEUAmITQOPM8sno15CAbpC_wX_b8PwgwIQAuNjW-DqPYZlhUZxKf8WPwMcBA4H1NCc_BXbvVMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا بعد رزمایش جانفدا ها توی شهرری عقب نشینی رسمی خود رو از خاورمیانه اعلام کرد
اونی که اسلحه اسنایپر رو برعکس گرفته فقط
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71752" target="_blank">📅 09:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71751">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=R5dB61VpTVPHTbwb3l56Wryv1m0rlqJl_h8bCNQAa3_iVhIorXER6lwI4pJhr2cfU5IMPYhFEq3cXwMKlpS2qFUVxAPaOk4iqHcovaelSPn_w3S8rieLPsh7gQkDygKyu7G17EvFuWzS3klidOnZFsvOlq7Jtp3--5E0EFc8AZw2bEX1uPpXohBSxes4zgv_YrYnO9P8vVEYWr8gGgl4rcNr9Qy3Xth0Z33W92W_revx8qeuD1x1SuxM_ZzC5xmrs0zpyTt2LW3d8oYCsgdMhoBi4KvSB5kG5EgN-xihgG7iK6yRFa9qoqtP3lP4oAMpZC30l1uVqtvQLx9i3rAbeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=R5dB61VpTVPHTbwb3l56Wryv1m0rlqJl_h8bCNQAa3_iVhIorXER6lwI4pJhr2cfU5IMPYhFEq3cXwMKlpS2qFUVxAPaOk4iqHcovaelSPn_w3S8rieLPsh7gQkDygKyu7G17EvFuWzS3klidOnZFsvOlq7Jtp3--5E0EFc8AZw2bEX1uPpXohBSxes4zgv_YrYnO9P8vVEYWr8gGgl4rcNr9Qy3Xth0Z33W92W_revx8qeuD1x1SuxM_ZzC5xmrs0zpyTt2LW3d8oYCsgdMhoBi4KvSB5kG5EgN-xihgG7iK6yRFa9qoqtP3lP4oAMpZC30l1uVqtvQLx9i3rAbeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در میان مردم اسرائیل با استقبالی باشکوه
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71751" target="_blank">📅 09:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71750">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=OabBL5h9CdAXW8EJ0Iyg4vaHlWyeOvOJa_JvFC7r6c-387G5rObEq_y0Y5-YM5603TGajUwTNsWda6vbASgZM6Glw6YqtJi0yoMpxKZqEqYDDV5iZsH7Fkd1M8Tte1EsxOGJHTjlDl4kUZQiuZ6cSnQ642M6uz_z2Mt7BDBqvmtjat21XxmFx1sn7FhKSg2YpmwsoxDYePh8ii40mPpIijw5MeXdR67vMAOiwdrmXJQ_jVly0J6vVLAYESJP3ITZ8fAqsUfD34-n3TUcC0etgiUQbi_GOyNLEAH-3gQkka2xnMzHll_EQcHCkAK9KNxzfNpnFuOglNuGp_mLLoSLXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=OabBL5h9CdAXW8EJ0Iyg4vaHlWyeOvOJa_JvFC7r6c-387G5rObEq_y0Y5-YM5603TGajUwTNsWda6vbASgZM6Glw6YqtJi0yoMpxKZqEqYDDV5iZsH7Fkd1M8Tte1EsxOGJHTjlDl4kUZQiuZ6cSnQ642M6uz_z2Mt7BDBqvmtjat21XxmFx1sn7FhKSg2YpmwsoxDYePh8ii40mPpIijw5MeXdR67vMAOiwdrmXJQ_jVly0J6vVLAYESJP3ITZ8fAqsUfD34-n3TUcC0etgiUQbi_GOyNLEAH-3gQkka2xnMzHll_EQcHCkAK9KNxzfNpnFuOglNuGp_mLLoSLXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا قبول دارید که آن‌ها به خاطر جنگ در ایران، نرخ‌ها را بالا می‌برند تا قیمت‌ها را پایین بیاورند؟
ترامپ: نه، آن‌ها نرخ‌ها را بالا می‌برند تا عملکرد ترامپ تا حد ممکن بد به نظر برسد. مشکل آن‌ها این است که ما بهترین اقتصاد تاریخ را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71750" target="_blank">📅 07:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=PNASeZmTdZP_flaNn2YgB_TN-pYJ2fm6kyxcFRv24kZrpF5H0b_yuHz1i-su6wK-_d9G6OxtkAbpChiCmM3f_0kMUn8fIwMaASFv12OvZr3lpsF8WFEdo1RLLSiYG4-tKHYKF8nELhvow7HQrzcRH_oeg-mZJThkTeA6-P_6SLN4uwHzputpyTo8tT_cIzMLypHro9T9Nip58V9tDFjoDWB0bXE9cLJ9gAsgqOBpG_l2VHoW8WsLKeVD6jfkFXZz2T97_xCpk9sqH82d3Zmpueda4-9C3KGRdnJ12076908ACaqrjKpnr4fFlpB6ZywII7W3veU2XMtr_iTCZiw7pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=PNASeZmTdZP_flaNn2YgB_TN-pYJ2fm6kyxcFRv24kZrpF5H0b_yuHz1i-su6wK-_d9G6OxtkAbpChiCmM3f_0kMUn8fIwMaASFv12OvZr3lpsF8WFEdo1RLLSiYG4-tKHYKF8nELhvow7HQrzcRH_oeg-mZJThkTeA6-P_6SLN4uwHzputpyTo8tT_cIzMLypHro9T9Nip58V9tDFjoDWB0bXE9cLJ9gAsgqOBpG_l2VHoW8WsLKeVD6jfkFXZz2T97_xCpk9sqH82d3Zmpueda4-9C3KGRdnJ12076908ACaqrjKpnr4fFlpB6ZywII7W3veU2XMtr_iTCZiw7pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدواریم که به پایان ماجرای جنگ با ایران نزدیک شده باشیم. ایران خواهان دستیابی به توافق است.
خبرنگار: آیا مستقیماً از آن‌ها خبری دریافت کرده‌اید؟
ترامپ: بله.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71749" target="_blank">📅 07:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71748" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uwpWSAQaqKz5WgJlRrxug1TGwVjpRdLWXQDaepaN_UD_H60nGLOLnUOJkej2mp8Hr7lPDLQlKx90VP11YigIRNZL5vn1HZMFdU8B-VpeCakr1Xy5b50balhjJlCjWlTQTbikwF4USv376-bulfpNybIRp6EENRLvGK-HK6s9he8Xgf6eOHs4FNBhGbT9OmgirlQzXrCgL19GgxLt7EfCN98aZnDMkQyVhtG_Qc5gMUDitBLYSH9G1KEia07rVTgjXfJVbAgSgl7xr_CqQwbNh676QEM9gz995I4AvgPRDrYw_nw8R9-Ln0XQpL7oWponSW8u6bLegXi-Ll_qbLfKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71747" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=hEwv_Qzyw7444A_YH2BZZijpmXs67JtuvkHBlUVG5GxbwbwxGG0KtJMcnUTfiMWWYKcCgnT50Pn0mhfVkpM7aFMSmj2svAiBuUSeAtZ7vLZVeKVhlE2IQ6mV46GhbRXV-ROwwbS5i4bzkNkD-WsfOqPokrd2A3hlO3I4DEIcHL-moWGb2Q_1X0WsBLUyBBEui_7DN_5DE0K_CCXoaL3frU3q4mITwrDWHdnvjT1f93FqrJA2SrZvsDx_ghiycMvPsryRcUpkCgmoqSjV9cH1nxa--hUegIlJJo5CtuAaxE_hlRhUsO_c-NwFzZ3PSDXt5h22zVE3__egqqYTBTygwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=hEwv_Qzyw7444A_YH2BZZijpmXs67JtuvkHBlUVG5GxbwbwxGG0KtJMcnUTfiMWWYKcCgnT50Pn0mhfVkpM7aFMSmj2svAiBuUSeAtZ7vLZVeKVhlE2IQ6mV46GhbRXV-ROwwbS5i4bzkNkD-WsfOqPokrd2A3hlO3I4DEIcHL-moWGb2Q_1X0WsBLUyBBEui_7DN_5DE0K_CCXoaL3frU3q4mITwrDWHdnvjT1f93FqrJA2SrZvsDx_ghiycMvPsryRcUpkCgmoqSjV9cH1nxa--hUegIlJJo5CtuAaxE_hlRhUsO_c-NwFzZ3PSDXt5h22zVE3__egqqYTBTygwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواضع حوثی‌ها و تجهیزات نظامی آنها بار دیگر در مناطق خط مقدم شمالی استان تعز و اطراف المخا هدف حملات قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71746" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=rigTkHFkbmeEhC_XxdF9NTGAshucOCP7f0C_gRUJC5pv2Bhbe_VHYhCPnKFqhpJ1mhmbaJ844NI6kbQ-EQls8KsSwayFtH83yzEoF7xoc-hUfG_MOqH4VB5b5tLqkF-qyrOkOfgMy6oqLKV0fsAi8R23spX8sUXMBhkuRH1VjN6KBAI80M-KLLxJJy8IMrQ4wODWWuMEhYX1QoDkv3oh6dxnxUYx2cwKZVoFjJilaGqM1duxg8BcU5tSf_hfE-v1eWW3DLLcgbKtHoRPZyKTlp4vGpjm-YDmvbYjK3nLCKTwuXrrPrdK6Bq9YxjNsbMXyPKrM0YEgcr7UV5qiO31uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=rigTkHFkbmeEhC_XxdF9NTGAshucOCP7f0C_gRUJC5pv2Bhbe_VHYhCPnKFqhpJ1mhmbaJ844NI6kbQ-EQls8KsSwayFtH83yzEoF7xoc-hUfG_MOqH4VB5b5tLqkF-qyrOkOfgMy6oqLKV0fsAi8R23spX8sUXMBhkuRH1VjN6KBAI80M-KLLxJJy8IMrQ4wODWWuMEhYX1QoDkv3oh6dxnxUYx2cwKZVoFjJilaGqM1duxg8BcU5tSf_hfE-v1eWW3DLLcgbKtHoRPZyKTlp4vGpjm-YDmvbYjK3nLCKTwuXrrPrdK6Bq9YxjNsbMXyPKrM0YEgcr7UV5qiO31uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر از همه شانسش یک‌جا  استفاده کرد...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71745" target="_blank">📅 23:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=ZjoZ_KcJNv5nkrSeCmBDv5CN6difjTqVS5Mr7i5Evm90mipVBUXZYNPqM5dDfOWFqyQ_-b3fBZRYoJA5C0lu9gQhwa1U2gbRGO-LTySrT12mh9P2bDIpte89wXjhbQ5oKMLWbhIjO5rR3LUP6z31kV2aeizHxi9bqlLeb7uxRuAHSHIDX3rupwiAGvGWP2sfc5Dr3eLy_ioG97wVkXRDDKtk5x3yLWOfCnkHh_Syie0MKesh9L0st6Jw328ypl7jroQQsT8N9G93bpbjyWnbsujBj3bt2VD3nOJLXxPRJO3QGp4A9ERYukN4fG4r3FHk6bsxQ0lAkZ5FWp_Rh5ZWeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=ZjoZ_KcJNv5nkrSeCmBDv5CN6difjTqVS5Mr7i5Evm90mipVBUXZYNPqM5dDfOWFqyQ_-b3fBZRYoJA5C0lu9gQhwa1U2gbRGO-LTySrT12mh9P2bDIpte89wXjhbQ5oKMLWbhIjO5rR3LUP6z31kV2aeizHxi9bqlLeb7uxRuAHSHIDX3rupwiAGvGWP2sfc5Dr3eLy_ioG97wVkXRDDKtk5x3yLWOfCnkHh_Syie0MKesh9L0st6Jw328ypl7jroQQsT8N9G93bpbjyWnbsujBj3bt2VD3nOJLXxPRJO3QGp4A9ERYukN4fG4r3FHk6bsxQ0lAkZ5FWp_Rh5ZWeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نکته‌ای جالب درباره جنگنده سعودی که در مأرب یمن سرنگون شد:
شماره سریال (5529) روی دم هواپیما قابل مشاهده است که تأیید می‌کند این پرنده، مدل بسیار پیشرفته F-15SA ساخت آمریکا با ارزشی بیش از ۱۱۰ میلیون دلار است.
این هواپیما دو‌سرنشینه است؛ بدین معنا که شمار پرسنل اسیر یا کشته‌شده شامل دو خلبان می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71744" target="_blank">📅 23:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=i153gskJwT4AWFMJ3VU9hKpPReRJMIEhsfDfpTILfxcQlfmnDO8UQHMdj_6EXlRNeGyCzuJcKg62pVMkndScsK_eqSPymfRc5j9hczJFwjukTnikaNdMgXCn17x8BaJk46yIdTVtUWHFUWE8dQKF6RcJZfAdnJykRoaHH2c7gFs3Hb6OXD8zxJggMbvbVj-IH1dIv-3evn-Kr8FYn5unSxxa-Xa9EGZsTElYZc6tlNjrwZRM9E96w0IY4ElNKomi5xhzXR4g31X62HT02GiJQLodeYXgrLmi7zONuMC3PkzCHN8rU90IIMj0VGdFzfsBDXAlux3ioxepX4W6zhGdPlnKLlmiWzvHivdSCNEMB83XZnRMaQTT5I81QNubCxdIhVPwDGUhFRrxtd4qCoVzhbgE51UTQXfOH88rbWZTv9x6pDn7aenCxE3AVe10K-dxG1_surmNRDAlvEJ2MIorSMxES7pXfyfL9URlr9YTZub8wCj-MgL5gBX2YxS7ZfCFnCREWSWquP-20j_n6Y93Coh-1JadCPONIR_K2XqvubtRgQmWlKB74CgspSw4upnQ71obuSaAw6LueSYD5cfYUSAoRHuBVuz1j17kY4hd78TPnq06tPnS-NBmwLr1HexFjIlEW18RSZXpOjZ6Uv9cPKiknj7F8yvycIA6KTBm4eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=i153gskJwT4AWFMJ3VU9hKpPReRJMIEhsfDfpTILfxcQlfmnDO8UQHMdj_6EXlRNeGyCzuJcKg62pVMkndScsK_eqSPymfRc5j9hczJFwjukTnikaNdMgXCn17x8BaJk46yIdTVtUWHFUWE8dQKF6RcJZfAdnJykRoaHH2c7gFs3Hb6OXD8zxJggMbvbVj-IH1dIv-3evn-Kr8FYn5unSxxa-Xa9EGZsTElYZc6tlNjrwZRM9E96w0IY4ElNKomi5xhzXR4g31X62HT02GiJQLodeYXgrLmi7zONuMC3PkzCHN8rU90IIMj0VGdFzfsBDXAlux3ioxepX4W6zhGdPlnKLlmiWzvHivdSCNEMB83XZnRMaQTT5I81QNubCxdIhVPwDGUhFRrxtd4qCoVzhbgE51UTQXfOH88rbWZTv9x6pDn7aenCxE3AVe10K-dxG1_surmNRDAlvEJ2MIorSMxES7pXfyfL9URlr9YTZub8wCj-MgL5gBX2YxS7ZfCFnCREWSWquP-20j_n6Y93Coh-1JadCPONIR_K2XqvubtRgQmWlKB74CgspSw4upnQ71obuSaAw6LueSYD5cfYUSAoRHuBVuz1j17kY4hd78TPnq06tPnS-NBmwLr1HexFjIlEW18RSZXpOjZ6Uv9cPKiknj7F8yvycIA6KTBm4eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبرنگار فاکس‌نیوز از روی عرشه ناو هواپیمابر جورج واشنگتن؛
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71743" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مجری از خلبان آمریکایی میپرسه چی بهت کمک کرد با اون وضعیت از کوه بالابری؟
میگه هیچوقت اجازه نده کمبود انگیزه باعث بشه از تلویزیون جمهوری اسلامی سر دراری:))
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71742" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71741">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=Mo0WCNF3Ahte5P2Nd9hNBi9L9diC7_c7TQpwusMr4NehkSmJOVva2bewzlG-gev_oYgCiTHacdCcvBLUut0ypdwP6iNMCYxpvmfC6fXyVW9KIvBIYQSn3SFwjP6RcDULbF4PK5xEgjQvVQrhldUyHKAEw3AHolqQtZYQMLp5mcF2MDbOyEH_lb-XXRg3VtEK59Uhjub5ALFV0Q5DPzWeygRev_5545yBaKyxryuYCxtDPlS-6U-F7mZWMoIX5-yXFjW02nZbPDYfNn3c2vZ9crjRdi5hEqz2yAJ5ylFaPxNldCkcEg6WAHEif34orkbRVqVVTaOtY1EQiaIX6fV8NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=Mo0WCNF3Ahte5P2Nd9hNBi9L9diC7_c7TQpwusMr4NehkSmJOVva2bewzlG-gev_oYgCiTHacdCcvBLUut0ypdwP6iNMCYxpvmfC6fXyVW9KIvBIYQSn3SFwjP6RcDULbF4PK5xEgjQvVQrhldUyHKAEw3AHolqQtZYQMLp5mcF2MDbOyEH_lb-XXRg3VtEK59Uhjub5ALFV0Q5DPzWeygRev_5545yBaKyxryuYCxtDPlS-6U-F7mZWMoIX5-yXFjW02nZbPDYfNn3c2vZ9crjRdi5hEqz2yAJ5ylFaPxNldCkcEg6WAHEif34orkbRVqVVTaOtY1EQiaIX6fV8NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاله مرزبان بعد از دریافت جایزه بهترین بازیگر زن در جشنواره ونیز، جایزه‌ش رو به زنان ایران تقدیم کرد و گفت :
میدونیم که سخت ترین دوران زندگیمونو تجربه میکنیم ولی نباید ناامید بشیم
یه روز امیدوارم رویای مردممون برای آزادی و آینده بهتر به حقیقت برسه
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71741" target="_blank">📅 20:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71740">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2env_GZjwfKzR0en6Xu2ebrFjjiIOgU4vIdt6DxOJoLDJIpiOZ6Xh9zaEegL9FDDoAmB98RMhwSx2V67bbj-V2S_0zYybJEYaz3UwjJndO4aR_lBHmYZRwxD394hkaU7YxYwkFgD4cLqWR60PPAXUXdyUVu0Q1V1YxqhYt_m-bY5kgT2aNODcqpaH78iYnoP2hz0rzOSgJYAaSoNEwI0R3BGW2kUWBiU_SlAPnkMWDqF5oUZPLqKYQJIbR0qhnMwPKQLkkLfvMVl5a7RDBvTmvOCVa5IJkWllbQVDFibWQ-JuJVhfH1nKUdzPNi-FlSPIaGXI6iVAuNS7j0Ocks6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت گسترده ترابری نیروی هوایی آمریکا و جابه‌جایی مهمات میان پایگاه‌های این کشور در اروپا و خاورمیانه امروز!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71740" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71739">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزارت نیرو از پایان قطعی‌های برق خبر داد؛
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو:
خاموشی‌ها از هفته گذشته به پایان رسید، امسال ۱۴ درصد برق بیشتری به صنایع انرژی‌بر کشور اختصاص داده شد!
بیناموسا میگن دیگه خاموشی نداریم اما هرروز داره برق میره
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71739" target="_blank">📅 19:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71738">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ98Q3hZIFkM22nBhwNfDlQQcDfPjdljAVpZsjAfF-b3V79JvYiYOXv3E8y8jRMqJEBup5ql2tLjOCVIFWxu-gFFXhNjrDULheOj02NPNWkLUqxa0pLhb6fm1Ju8cDoyznxJKjiH0NDZXt9o8C3njhAjuaTOP6IOlQBU26ARw1Btms30Agha9q6pJNOoY0NRZY8JzmprFZmAnB4lj6jSyUDi4NKZ3jH4jhLPjqytd0XV_tac97TPsg8uV5oxA5akE0DCtFRb18MLtl5xzfI57k1gAH8UWQUrwBbHYapS7hrSrjUdAyDbHjkHbESHS8aUFDw800OZREi2jAkUkp0Jlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، به «نیویورک پست» گفت که مناقشه میان ایالات متحده و ایران ممکن است ظرف چند ماه آینده وارد «مرحله‌ای بسیار متفاوت» شود؛ او با ترامپ هم‌نظر بود که این جنگ می‌تواند «بلافاصله پس از» انتخابات میان‌دوره‌ای به پایان برسد.
ونس اظهار داشت که تردد در تنگه هرمز به «بیش از ۵۰ درصد» سطح عادی بازگشته است و استدلال کرد که ایالات متحده دیگر دست به عملیات‌های تهاجمی نمی‌زند، در حالی که ایران همچنان به حملات گاه‌به‌گاه علیه کشتی‌های تجاری ادامه می‌دهد.
ونس گفت: «این ماجرا در واقع دو مرحله دارد و مرحله اول به پایان رسیده است.» او هدف اولیه را نابودی برنامه هسته‌ای، توان نظامی متعارف و قدرت اعمال نفوذ (توانِ قدرت‌نمایی) ایران توصیف کرد.
وی افزود که مرحله دوم، جلوگیری از بازسازی آن توانمندی‌ها توسط ایران و در عین حال حفظ ثبات جهانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71738" target="_blank">📅 19:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71735">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apeV68qyoOPErigKe1NMJMej3K0Yh50RufINYjmJtPhcg0cXBSqZcowkCZE89x3Xc994LzbfxyZMRF54m2QP-X76H9jIa3Wnw2TZFF5N7wUvWM7JrCDxq96b2Wd6bOZW7DXifZ2V1bxzvLcOvYMgICPnWooMyd8iIYyWueIcsrDAauSYbNtiKhb2F-JyxVdTQruK4NxoWN5dZcQ7_sdI49Jm10J7lbka_ZxAfFgVttAkl3rSR-ru8J-qnuvmggJ5zB729mMcHFUXZGE6dbIm69RtCQoYO3S738W0xr8_IcPPhFg4gL7L41wn5wUZXswSvInj6JdEz1c62bfTTek81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bao42zozIJkvHyZ7ixLEXhZkDiNUx900lxwTti4d48fe7uL2TaUdwGfah029mmbGsufxHiyiqkPwQpiHIQhwBNlMwKg-IQfOWx_IXT3YXpCEM5EDh5q-DM6_m_dH8vu2t6-YWMgk4G6C2Y7cagfzg98Y8S80O23tkLTD0ZiZY-zUogYWtVvYyrzngOD87DRDNch2PARuANp0FEzHaS900sqq7w32yfV02fYha-8rQy1OzzhqmW3UEglebZPA9V7bZxEuboS2XwQs2SvEVgK_i43CuMG-jq_q_eWnOSgRlGzQSW41jjTfSuoPrdVuRDqMecwGpf8eteB0dkbSLBGvoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حوثی‌های یمن تصاویری منتشر کردند که مدعی‌اند سرنگونی و لاشه یک جنگنده اف-۱۵ عربستان سعودی در استان مأرب را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71735" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71734">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=q7ZvA9kEaWK4AgS6PhITUhVYgfqhGmunS5xTGfAsGne8GbxS2e11tO0CHQSBx-qK-1c7LRFT8Rn1x8oklw4-f0UQSsmZR4ijQwv4W5SUDsN-l0fxLx0b6X5QxHLSNli2TUsZzcKDyRlz3wjxqWHt5jARMaZPifR5qv99d1AHZ_vwq9tLOoxqAm9YzPMP8IFD-V4nOUsxUNhrW6owWstQk2eZRKR7QeAsIwAqnMps9hSVsbeflZ_nFXH8mJsVkZgcGch4HB_G8-CFwnN44SFerk-FNRN-gKHhfCpS-055ml5y0V5-lfGigtqKYqZPXrWOYaGiKNmpHVSz5HgI-KNj8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=q7ZvA9kEaWK4AgS6PhITUhVYgfqhGmunS5xTGfAsGne8GbxS2e11tO0CHQSBx-qK-1c7LRFT8Rn1x8oklw4-f0UQSsmZR4ijQwv4W5SUDsN-l0fxLx0b6X5QxHLSNli2TUsZzcKDyRlz3wjxqWHt5jARMaZPifR5qv99d1AHZ_vwq9tLOoxqAm9YzPMP8IFD-V4nOUsxUNhrW6owWstQk2eZRKR7QeAsIwAqnMps9hSVsbeflZ_nFXH8mJsVkZgcGch4HB_G8-CFwnN44SFerk-FNRN-gKHhfCpS-055ml5y0V5-lfGigtqKYqZPXrWOYaGiKNmpHVSz5HgI-KNj8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تهران یه کافه مذهبی به اسم ام‌البنین افتتاح شده و مخصوص آدمای مذهبیه و ورود افراد غیرمذهبی به اونجا ممنوعه.
شنبه هر هفته هم سفره‌ ام‌البنین دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71734" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71733">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71733" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71733" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71732">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OReiC0DkBGWY7BcJc-JxBlZB7MBjQLEBbU_M5evPji2MdhAKE2WNShO9XR3pkSTURJ1aiOZPO56j2Kcok0Ha_LCyl_fV-V2ZVxkm45fr3jWwo9sQnOFUoG7IiACr31D894iDjncKBUTRvSKqLpoOevwCvmURNRhNGYxMFqo4MEInpEWRX53uQDfXSjQ6HS-7UlUaix5GWldB8J0-s7ieogoVEQWXGPD2QGcofZQzMHhZGImdjcGzlSJ79ZUCgQ8vVDIEeMHXzhOQX7iPz91osSckLbu4MFXlOb_YScvCpv6Sjo4kvn-atHdUNNIAK-GW3XQfSSjKQSS6fadjYCFWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71732" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71731">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534f93c783.mp4?token=EeUZG0_zVJIMS5tc0ZmeVJiKq6VAX7xkKSCNhzrFXq-xnUJlV6KKWC4SrazOF0Iw2z4LhoW1AD8mmBJ8agNsx73_KyzywHco8SJtii9D22lVHHIVNMDCvvrfZGyqhgBJnRzZ_aqVs6LRxJzjMeXCLLEi71xJW2OML6TuFpmU3pTyq5hSenHugISNdHj5NX-6K137Bs2xM1vk77Y_t_llkNfv14olBmrnS5SrJNfQJxzcrHamXW7d4iEtiulqYiZ90g5YfzCUmQaqQ32qZEtBWZ36jGfDysfd1fee6D3ZHRFVDk_Z9_t06-dcYCdqFwnoHv4EWN3kp7mn_KyD3Ood4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534f93c783.mp4?token=EeUZG0_zVJIMS5tc0ZmeVJiKq6VAX7xkKSCNhzrFXq-xnUJlV6KKWC4SrazOF0Iw2z4LhoW1AD8mmBJ8agNsx73_KyzywHco8SJtii9D22lVHHIVNMDCvvrfZGyqhgBJnRzZ_aqVs6LRxJzjMeXCLLEi71xJW2OML6TuFpmU3pTyq5hSenHugISNdHj5NX-6K137Bs2xM1vk77Y_t_llkNfv14olBmrnS5SrJNfQJxzcrHamXW7d4iEtiulqYiZ90g5YfzCUmQaqQ32qZEtBWZ36jGfDysfd1fee6D3ZHRFVDk_Z9_t06-dcYCdqFwnoHv4EWN3kp7mn_KyD3Ood4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این کلیپ تاریخی که چند نفر میخواستن با برنو، سوخت رسان و جنگنده بزنن
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71731" target="_blank">📅 17:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71730">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فاکس‌نیوز:
یک کشتی طرف قرارداد ایالات متحده در نزدیکی تنگه هرمز هدف حمله‌ای از سوی ایران قرار گرفت که در آن از چهار پهپاد و دست‌کم یک موشک استفاده شده بود.
این حمله منجر به جراحات جزئی، از جمله عوارض ناشی از استنشاق دود، شد.
تعدادی از کارکنان آمریکایی در این کشتی حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71730" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71729">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU1xv8wN56L9yTfBnCzpilBJ1yBVAnfccFMTtDVYgas3mzaUfPwMpORkitPoZVPURnlzHKFj5CYeVY_0Uc2nsx0xds-tS5l579cU6d1kdAIlYNqxPXHi7r5_RhivMHNAlhnBRz3Q63lm5M04DUm5GIlJ4l8NVVlE8NRoLt84yDRUV3cJ7OWt018xa_8cPpk7Clmn5iuu8PdCmIwftIOKzk4qfGMaP3kGfcry0xu7s93Q_gLR68k1WDuLzKOjFX_OIuiwrAjeyhmaDKpTMhkjCXdLz_J6CF8zn4fsCKr2IZaB7-MALn9NSUd17uNngp9Dgfr1V4vpouQok_aC0Nxm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در تجمعات شبانه:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71729" target="_blank">📅 17:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71728">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2421361f81.mp4?token=KPAJ3StBTtWY3bCle601LaG9iHxtDwcgDZJ6b_8TBlZsE8VP1glNUo6tuHlxDH7wsCkemjHAE783KTwjIrSEI04yRBV-SohBIw6vfc9t7FFE7Dx6kCmwhcD2LhrdvZqWW-DJUenp6-W0mBOh-0OX_K6tOZZ_8WBnOpXRATvqD_lSglItQ20nVT4vZWclZA-G7opjRX2xitFL9P2MOUmw8bxhLxWcEo8vKgfi4MX7NVEhxt1WFYDALUscHzU_8wZxn3MOINILfwZYZrQHMR0udgJEdDkHpNcOug9tzRGlVd_Ad_dGhFDoHS2ya0d-P8s5rys4hl-aQGjTza2azvrADGAqbbyTLIKzkzUs3aOeBebMHS1T-w2xtNi0ZJEuT6D-fg3yftxZFj6-kBsbSp6YUON_UtAY4sQXYOhwku7HDFgbqOw1eZTTxmezjjJVKi90lbhbo5pEKoHKx-VIUkFEqeCCzl9lIn4PnWH63RP-b6I7kNag4WV25XsTD7EsNdpDWCIceNZuTwSUKUol21bAqtqp8kQSgZubxJJq0hOJw353HqpAoVQnfsUyhWYyySJFCaRR_HPRkKb_Y8q5U8vM1pm-0lOZdFo2LaPvIIRDrllCrlNDsGN_1IYxmAx9fu4MUETGmTv82q1CuaJoehG27ItMey7SVci1-EXIncLuZAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2421361f81.mp4?token=KPAJ3StBTtWY3bCle601LaG9iHxtDwcgDZJ6b_8TBlZsE8VP1glNUo6tuHlxDH7wsCkemjHAE783KTwjIrSEI04yRBV-SohBIw6vfc9t7FFE7Dx6kCmwhcD2LhrdvZqWW-DJUenp6-W0mBOh-0OX_K6tOZZ_8WBnOpXRATvqD_lSglItQ20nVT4vZWclZA-G7opjRX2xitFL9P2MOUmw8bxhLxWcEo8vKgfi4MX7NVEhxt1WFYDALUscHzU_8wZxn3MOINILfwZYZrQHMR0udgJEdDkHpNcOug9tzRGlVd_Ad_dGhFDoHS2ya0d-P8s5rys4hl-aQGjTza2azvrADGAqbbyTLIKzkzUs3aOeBebMHS1T-w2xtNi0ZJEuT6D-fg3yftxZFj6-kBsbSp6YUON_UtAY4sQXYOhwku7HDFgbqOw1eZTTxmezjjJVKi90lbhbo5pEKoHKx-VIUkFEqeCCzl9lIn4PnWH63RP-b6I7kNag4WV25XsTD7EsNdpDWCIceNZuTwSUKUol21bAqtqp8kQSgZubxJJq0hOJw353HqpAoVQnfsUyhWYyySJFCaRR_HPRkKb_Y8q5U8vM1pm-0lOZdFo2LaPvIIRDrllCrlNDsGN_1IYxmAx9fu4MUETGmTv82q1CuaJoehG27ItMey7SVci1-EXIncLuZAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیویس کیس سخنگوی سابق نخست‌وزیر اسرائیل:
دیکتاتورهای ایران ظرف چند هفته سقوط خواهند کرد؛
دو هفته، سه روز، شش ساعت و چهارده دقیقه دقیقاً
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71728" target="_blank">📅 16:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71727">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=AMcnWoj7-7Rf-Y4JxYwUCMMFtT8ULW4TDP91zVrbSNUQMfj1jYw9L27yS9bSLGcs10PsW0lEHCKxLLMzDe1j1Ye63fYTaqhlJrWax1zqrQKQ8urLUDzvZ5H4D1KJJoZRUZoflhpn5Crd1HTohMZWz0-_k_0ttpw6AOAp7nPLMgBT1fCCvzwSxQGaWvuoHO3lbBoglO9BvsV-99H9g5fGZKgUIRbrDjAPGllmnLrhcE4BpLfuOu3lnmmcE5G2aR-QnKrKYuOKHpKpFKI-AmsX1ClL8BgUqgf-jKz-Yl65CR6YrQt3SideUUlTR1fUn6_1fP5rq92I7a9UObUR6qs2bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=AMcnWoj7-7Rf-Y4JxYwUCMMFtT8ULW4TDP91zVrbSNUQMfj1jYw9L27yS9bSLGcs10PsW0lEHCKxLLMzDe1j1Ye63fYTaqhlJrWax1zqrQKQ8urLUDzvZ5H4D1KJJoZRUZoflhpn5Crd1HTohMZWz0-_k_0ttpw6AOAp7nPLMgBT1fCCvzwSxQGaWvuoHO3lbBoglO9BvsV-99H9g5fGZKgUIRbrDjAPGllmnLrhcE4BpLfuOu3lnmmcE5G2aR-QnKrKYuOKHpKpFKI-AmsX1ClL8BgUqgf-jKz-Yl65CR6YrQt3SideUUlTR1fUn6_1fP5rq92I7a9UObUR6qs2bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ دعوای این دو تا بچه گربه خیلی وایرال شده، از بس کوچولو ان، دستاشون به همدیگه نمیرسه و رو هوا همدیگرو کتک میزنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71727" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=iN6iW7_PWliUQh8Fk3fcNJ6JLgO1MTQ8QmNjKfXAFFTMsR-rZACMVtCP3Pk2Nu0cgNQnsXzq2rn7yVYllyUoSvkk8ih6WezZ6AliJslOZRKKeVfKDFAJUsRM02bEj4I04-VyNEDHUPXXmB3MZIXyRVxk7eoDTS1Ycfha8vEK_Z6L7gpBMd5hx8wawVBvjeU8gaVdpRUSQq2ObVbcWRO8kLZ792lw-sREwtvkH141s2RQ8uqmtw2AhmRq5fyTs3ukddHG9kmuTPOsLgNqOgsth1BpFmOGRnkd1n1PQsSkv01pLB4jEO_e3yaLx4UJz5qjN9jpJf3xxWzWFplDgf9y8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=iN6iW7_PWliUQh8Fk3fcNJ6JLgO1MTQ8QmNjKfXAFFTMsR-rZACMVtCP3Pk2Nu0cgNQnsXzq2rn7yVYllyUoSvkk8ih6WezZ6AliJslOZRKKeVfKDFAJUsRM02bEj4I04-VyNEDHUPXXmB3MZIXyRVxk7eoDTS1Ycfha8vEK_Z6L7gpBMd5hx8wawVBvjeU8gaVdpRUSQq2ObVbcWRO8kLZ792lw-sREwtvkH141s2RQ8uqmtw2AhmRq5fyTs3ukddHG9kmuTPOsLgNqOgsth1BpFmOGRnkd1n1PQsSkv01pLB4jEO_e3yaLx4UJz5qjN9jpJf3xxWzWFplDgf9y8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه رستوران تو آمریکا باز شده که تم بیمارستانی داره و تمام‌ کارکنانش کاستوم دکتری و پرستاری پوشیدن و اگه غذاتونو کامل نخورید باید براشون قمبل کنید تا خانوم دکتر بیاد شلاقتون بزنه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71726" target="_blank">📅 15:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=UsUGxHMA9-XEFyQRrxucIOsMtzlN77SSJoIal6bO0AOfIvf1KuWe_G5arwWoQcwrRAvTWqofvUVlWL9CTUtD238o_Vu7znoY3G0YIqzvmwKkPVXX-yZbAjhWoECQBzEfVe6C-Mty89ORU0Fc5a5cuUIvys3CyV0IAML-WTLSal9-RF18HCUp-q1H5wumF6UHwriZJMRTfE2_RaoRy863amhyUdEMmPXU2Jfft5dMGa2L6cmsJIw0J1MoNBBZIhrPVE_KYCgyq7GJBRMLSg_HrVr-v1NQfOukyo6hZeiCTIIssOybmd-Ui98Di6OOrxnRYk406Ka_qTzVaAOSWLcdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=UsUGxHMA9-XEFyQRrxucIOsMtzlN77SSJoIal6bO0AOfIvf1KuWe_G5arwWoQcwrRAvTWqofvUVlWL9CTUtD238o_Vu7znoY3G0YIqzvmwKkPVXX-yZbAjhWoECQBzEfVe6C-Mty89ORU0Fc5a5cuUIvys3CyV0IAML-WTLSal9-RF18HCUp-q1H5wumF6UHwriZJMRTfE2_RaoRy863amhyUdEMmPXU2Jfft5dMGa2L6cmsJIw0J1MoNBBZIhrPVE_KYCgyq7GJBRMLSg_HrVr-v1NQfOukyo6hZeiCTIIssOybmd-Ui98Di6OOrxnRYk406Ka_qTzVaAOSWLcdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله افراد لباس شخصی و آتش به اختیار به یک رستوران در رشت به نام « سحرخیزان » و تخریب رستوران به بهانه حجاب⁩⁩
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71725" target="_blank">📅 15:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71724">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8YgrH0yL2YOgAulGA0Tw26OUytqxbn6b3laEiEPiF42LHdviLKT2wywaUUigaZ2JvQIPxHS_MpIG8u14ToIv62nPUmOik2JpSGe4vbDqmEptWcLRMjIOWt2mDcIVCkxGp59dQGlp3XTLTRGkp6unfejyfoFn6mDr1bqrVpHO4jeICwRJiW9vewA-q_BoVpedUHy_Z4ZCxAmtPki4PW0fUlgXL3aXpRk8bfp1XQQcvrpS3ZkPCcyDTV7kGA4PTWqCn_TJSURhnxefGCqpnmXixjOz_fzVeR9erUNUCoaJBtVF2nXPJqb-MpjzhVK7zpQCYUe_hLRG3UudmvH6jeAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛  سامانه‌پاتریوت شیطان‌بزرگ مانع شد خانه‌خدا توسط حوثی‌ها نابود شود!  @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71724" target="_blank">📅 14:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=KJQLCMRW41qhVWuXTim3WiRo8B29XKOlV-bFQjrV77VjOiWJBSqzzkQaJ_NZ-l9C2g4YNJEujzjBcqz5U_YHWQKwfE51rfpleJzlcoBYICYLTgPj6vqpvU_hiayM_cNSDiW8llb5BE6k4GEyowsWQz_sXpuWy5mDRxvC8WLPZPoU-BK-rrzDyFTEEUAYaqIWaMHRswbD8hxjht3D_Ey-n_xy-s4izSSXVcZ9s8FAjyMWrkvAlXV3nFUbnAv0-e-3QvUtXXJi6O60UghOlUC_btqNl-KTzYk8gHr8_5vJ1pdvhnvhJC0XJyO_w98GH1meA46ykq_9ThivjofGUxww8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=KJQLCMRW41qhVWuXTim3WiRo8B29XKOlV-bFQjrV77VjOiWJBSqzzkQaJ_NZ-l9C2g4YNJEujzjBcqz5U_YHWQKwfE51rfpleJzlcoBYICYLTgPj6vqpvU_hiayM_cNSDiW8llb5BE6k4GEyowsWQz_sXpuWy5mDRxvC8WLPZPoU-BK-rrzDyFTEEUAYaqIWaMHRswbD8hxjht3D_Ey-n_xy-s4izSSXVcZ9s8FAjyMWrkvAlXV3nFUbnAv0-e-3QvUtXXJi6O60UghOlUC_btqNl-KTzYk8gHr8_5vJ1pdvhnvhJC0XJyO_w98GH1meA46ykq_9ThivjofGUxww8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛
سامانه‌پاتریوت شیطان‌بزرگ مانع شد
خانه‌خدا توسط حوثی‌ها نابود شود!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71723" target="_blank">📅 14:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IT9vWi4g2xm8mYXiyl-WsCEQUarNE_TjgWQfbcx1lLSMsp3Laj2lAFiNi3QVn5faPOYE74aF-hu9KfNa9xLGEhj3LOudbiUiIuFxkMXVeJLzwaj-zZbeBOZBipGCR535Pu2xnYlM-0UT4e54hEYnLMmI6V0mZtn1C3XUrWMBNsY360L4WxSRGx5AOFlDOB8wyN9bjo7zEwhEkvvQW3B0ET7Rf31YBv0v1waMd48pNPJmG3vaWhDTHlHfwhB4_xDP4XV9THnqjVE7-912zVEdulLG3btwfdCX7DvlgsQDIUv60dmiKmBy6PcZitfCDeBujmXaA0V0kqrPtuKR_skHPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fU33oS2fXVhBE60-zpQLdlAoMKloRiz1_oF4_JRbqWbKy1EW48XtvLR4vdW-6VJBNH9qLRgaOZGKC7TNFXs19S05GDGzzP_vT-23pcGBsZ00CNQ5Ppv-Nki-EaLDpTFlhan2f_kdu1Q9_UtdKRUAl3Li3Q-mHtiF61woFGkzYMZCJWP6NrhEkYsp2oOZyNTdudfWgfZYqfgaYGTva0qVtN5ytlrF8iEvFcxtbE0wqQfLnbHDy6jPIPawyrJrA4k79njgafkZug8hA9SMA8lG46rmnifAG0cCVUtX-69S88vTwwlsILB7Y0ET5YL4SJWFgQj5IzlA0lQY9l5m7oCA7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFVqO-Ppvlio3-h392rVoI7CmWI8mW-DfNma_ickU9MCNXIddrpCEyuD1uFyAbse02MlcQbcJZArpvxoF3YgQVotaiwRZEGXrKV-yt7DGnmiQx92_8xOyjvLmjXo1TkXzrW6ezWCqlPoDBA8LHI1pOJsT-i1kBaiEXbpplfBEONa_LTrzoxDWfx15A5bHFJxK0dUefI6b2jUHuuhLisUnukwYJ5rkn-40mWbab5YN_XH_j67c_UBSDfw8xrqu1HNdBdOSUdbjZ0jJl5GPSrIn8r95YDcpRavmQL0KfjmcYvAqatmn1vhYXyFXpRx6A5374NX2Wo8HVl7OgXP0soWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN7MZnVP3oeQxRtM16b3sO9gSck9vGV1JL1nA4li6sfehaQRfdBfm9HV1lXX2_cI4IPEpUxLPVGr0UfRA4URp7UAUWurFcNRjKpcl5F3O5aLSf82wEub0NF61VDU2iQmVtLnhUdgasdwns5bq6sut3jJzcb3lESa1CttGedDM5GT1Y9Jwet10O3ovQvqr892dK0h9KSPriwHyJj9KdktRsLih74t9EDs7MEPoAY8gDqDr5BNA58vCh0UrSqubDrCwssuRJpWZo2E5TFhQnVHNSfpi-mWRdJ_u6GGas_3cJVa7zk_VHxkLNKy5hEF_tQ-Rj6IHM3ZrgFcZfl7Br_5_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های اختصاصی که توسط سی‌بی‌اس نیوز به دست آمده، خسارات گسترده‌ای را در چندین موضع نظامی ایالات متحده در خاورمیانه پس از حملات موشکی و پهپادی ایران نشان می‌دهد.
این تصاویر که توسط اعضای فعال ارتش که ناشناس هستند، ارائه شده است، ساختمان‌ها، وسایل نقلیه و تجهیزات تخریب‌شده را در پایگاه‌هایی در عربستان سعودی و کویت نشان می‌دهد.
در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای بوئینگ E-3 Sentry مورد اصابت قرار گرفت و قسمت دم آن جدا شد.
در کمپ بورینگ و کمپ عریفجان در کویت، عکس‌ها نشان دهنده پادگان‌ها، تریلرها و وسایل نقلیه آسیب‌دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71719" target="_blank">📅 14:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmKDH39BnN8z8jeyy4W6gBishXc4YAO2DC_5Hmm2CqQAfSkYeQBMPlM7E3-VwqVf5Lr3WMOYivb6dmxPVkRSe2jGS1RqOPTDuE2JHUDyXqIgPFhju1DSUIJ2buU8SGPQbL7lf4kIRcUyTNZih2kvvFbHLVSq36viTHwayVdnDTTPFOXBtu8qGP8DPI5Ab4OI8nHDzG7Kv2dipG7PWYU6VFuAdNHoeL_bUVAVLGLfk52Y5HPYYw3DSY0B7mmNuXxT7Pgg3gWDVdcS6namO5aXwV9zNhU-iv-bDz-HtZowRdsls5aNBCSnUNDG6KXaoWdiES7MoToqIsNFHMoGzk7Q6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشته است
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71718" target="_blank">📅 13:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71714">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a175287c.mp4?token=CDte3JUZ9fCe9cWKs7r2nrwZstEASZIlyxLdfNgb0JxnjO2O_r6_vqonZKISDPHZm3btmSfdP1uPQ-z3RiogQM8TOGZ2e28Ofk7YjZ2D7DnG9GxxhRf6QFdSed8myjfqULV9HWllwmDvv90EOp_p5EOGch2ET27pf-UHg529XZakvtR3HHDGUZqPea8lG9P2tnfTlrv1v8IRhBgfhSxGOaEp2NOULj9OiV7ypwmEISKC1EOQ5I82vhi0oFMycwjDuKY71JG90AGT8xsDXuHzNnueL-yc4DWzVfmOoxoSUK52YYkIamraD5sgMZ9KhsGTIJXVxQJw2uwq7qjxo9LnTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a175287c.mp4?token=CDte3JUZ9fCe9cWKs7r2nrwZstEASZIlyxLdfNgb0JxnjO2O_r6_vqonZKISDPHZm3btmSfdP1uPQ-z3RiogQM8TOGZ2e28Ofk7YjZ2D7DnG9GxxhRf6QFdSed8myjfqULV9HWllwmDvv90EOp_p5EOGch2ET27pf-UHg529XZakvtR3HHDGUZqPea8lG9P2tnfTlrv1v8IRhBgfhSxGOaEp2NOULj9OiV7ypwmEISKC1EOQ5I82vhi0oFMycwjDuKY71JG90AGT8xsDXuHzNnueL-yc4DWzVfmOoxoSUK52YYkIamraD5sgMZ9KhsGTIJXVxQJw2uwq7qjxo9LnTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
:ویدیو هایی از اعتصاب عمومی در سنندج،سقز،دیواندره و دیگر شهرهای استان کردستان به مناسبت چهارمین سالگرد قتل مهسا(ژینا)امینی به دست حکومت آغاز شده است.
همچنین ویدیو هایی از شهرستان پیرانشهر در استان آذربایجان غربی رسیده که نشان می‌دهد بازاریان دست به اعتصاب زده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71714" target="_blank">📅 12:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71713">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یه پسر ۱۴ ساله با یه دختر ۱۳ ساله وارد رابطه شده و ا‌ومده پیش دکتر میگه من پرده اینو زدم و گشاد شده؛
حالا اومد پیش دکتر ازمایش بده ببینه این دختره قبلا رابطه جنسی داشته یا نه.
سن رابطه جنسی تو ایران داره به ۱۲ سال میرسه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71713" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71712">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71712" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71711">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAgYEXZDUbwsZ7bCj_97WaFxAdarOTZtKyvnuT6ll0MbM2vOYdJ34KO81D_F4QGwM8sejxcUldTfkNLLz_aSOjvUs6TJaXKdSbo85qWZGCPX7dU2rJ_mDDFu54AxUTw-kEzY9lEg54FVRfEwg5Bdr8DiRISF78c-Er1bWmkJdlxWnMX0Tw_EITPvt9hjd87yMVAUNJlWrokYEjSkLp77yE90cOOYQrrk_nvDj7pdavpmNHFUBNhtHFN1-Nb_LUpoDSttRb0Oe4gsD8lb7gkcNoXIORuou0lbicsds20zFGZf2LLCIp9yDDwUvRmLtArXueDCWnO7HZVzyDolWY9niQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71711" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71710">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfEpvgBxFkRCxbgwZnuwbeTl8XGj1fEwZv9KcOGuOP-9VOB7l_RkvchNMmnug3O1SYP3ilQq8w7bTR_oV9TDYUnYPkY1JIUddTPfG8mV64uAZ5pQ-KKTYgElfPSDxPTNLCA9chCFBUWJ0Qjrpe3MQe2qJzWiKQzEepMe-GvX3PB8fAo4SOMh7GS4KGzJfunYYm77g6GCSjZ6-zzVuTGLt2tBtyQTag8_unIPd60kom1N8Q8Q-yoHfqbG1HEpPqE6N8zS2Fa2qOnKThK4Zwm2iVj_DPhW27KLdgxOwYgJ1OXsW4Rz1ygX3kvUyYKXiI8arIzIIbWQDnq5NGw6s6V6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده برای اولین بار تأیید کرد که سلاح‌هایی در مدار دارد.
مینک، وزیر نیروی هوایی:
ایالات متحده اکنون سلاح‌های کنترل فضایی در مدار دارد که قادر به دفاع از نیروی مشترک در برابر اقدامات خصمانه دشمن هستند.
از بیان نوع، تعداد یا زمان پرتاب آنها خودداری کرد.
نیروی فضایی می‌گوید که می‌توان از آنها برای "اختلال، تخریب و حتی تخریب" به صورت تهاجمی یا دفاعی استفاده کرد.
کارشناسان فکر می‌کنند که به احتمال زیاد، پارازیت‌اندازهای فضایی یا جنگ الکترونیکی - سلاح‌های جنبشی - مشکلات مربوط به زباله‌های فضایی را ایجاد می‌کنند.
این به دهه‌ها ابهام رسمی پایان می‌دهد.
اولین نقاشی نیروی فضایی به معنای واقعی کلمه یک هواپیمای فضایی را در حال نابودی یک ماهواره متخاصم نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71710" target="_blank">📅 11:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71709">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26353c8137.mp4?token=BfwaHIA2YKwb0Z8pt1jG17cfwtzkz5aE55Pfdasn-Z5W2h6EMe4LFuTIuAaV4ZOuVMYaooOvw1ADVHPX6HR6HPgd5mz98hI3CSAMI_1o7cxW2JcsFaeYALxE-QAwBlmlPgnrPlqsoGWk1BV1myIvIUIu9RglwriU1vDPJVQV66l4DB-Zvy4ZiLj55Zc5Yl8t-2nnSVsOFBwD7fX5VBGXGTrqU1vYkaUP7EDrAgHsNCiJDdkynX2fzDpsoAkjxT_tDoBIlbnUo94m1hBF6opZdscbfs-0pILjdiDYUg3lMd5MNHvNLBMx4atGFtj1SoEni3WmyRwkGK95DB33DaAgZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26353c8137.mp4?token=BfwaHIA2YKwb0Z8pt1jG17cfwtzkz5aE55Pfdasn-Z5W2h6EMe4LFuTIuAaV4ZOuVMYaooOvw1ADVHPX6HR6HPgd5mz98hI3CSAMI_1o7cxW2JcsFaeYALxE-QAwBlmlPgnrPlqsoGWk1BV1myIvIUIu9RglwriU1vDPJVQV66l4DB-Zvy4ZiLj55Zc5Yl8t-2nnSVsOFBwD7fX5VBGXGTrqU1vYkaUP7EDrAgHsNCiJDdkynX2fzDpsoAkjxT_tDoBIlbnUo94m1hBF6opZdscbfs-0pILjdiDYUg3lMd5MNHvNLBMx4atGFtj1SoEni3WmyRwkGK95DB33DaAgZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک دانش‌آموز دختر برزیلی بعد از اینکه نمره‌ی خوبی تو امتحانش نگرفت با چاقو به معلمش حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71709" target="_blank">📅 10:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71708">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=ChYfP-0eonV6H83lsngtLrPmss4Lrn8-Z7IJ2LjWD81ct3vaqkv32x7KqzWmPkGzbBkxOURPS1XPHUnAY0PJGLme7s24jVOifUtVXKLmXR9d84wk7mhcOn2_tbm2FACNSun1iLwA5i5M7mB7n_1e9dX7ErE6c6fz9NW58N2Cstg-nRiWsjW2nR0bWucBn-kxnuhAdkt-Wh3Gb-ZBMQqYJMLGID8ePUTGOsSnjbr7DUKC4lKW3h3mV7KlGh_vWAIcPa9YdfCoam5n_STzSBLNovaWUBnquG8DzA9o3rRAIo4uSe3hUKW-EPF1bFH00xeZD4eHOdfAtMy7v3Tkuk7wvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=ChYfP-0eonV6H83lsngtLrPmss4Lrn8-Z7IJ2LjWD81ct3vaqkv32x7KqzWmPkGzbBkxOURPS1XPHUnAY0PJGLme7s24jVOifUtVXKLmXR9d84wk7mhcOn2_tbm2FACNSun1iLwA5i5M7mB7n_1e9dX7ErE6c6fz9NW58N2Cstg-nRiWsjW2nR0bWucBn-kxnuhAdkt-Wh3Gb-ZBMQqYJMLGID8ePUTGOsSnjbr7DUKC4lKW3h3mV7KlGh_vWAIcPa9YdfCoam5n_STzSBLNovaWUBnquG8DzA9o3rRAIo4uSe3hUKW-EPF1bFH00xeZD4eHOdfAtMy7v3Tkuk7wvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته خانم دکتر(روانشناس بالینی)؛
خودارضایی نه تنها ضرری نداره بلکه خودارضایی یه چیز سالم و بی‌ضرره که به عملکرد ذهن و مغز کمک میکنه، باعث کاهش استرس میشه و حتی به رابطه شما کمک میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71708" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71704">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyyRJyyBdqSDD1-QL5rSJQOiweDxwoWuayjdjxKOF08hRUfwX6mn-6UNf4wuCU8WKa-Ldn9vYSIF9epuHiGr_8AA6fBwYA2tCm_V-WlNGh9H2bBpYY-81aN-cQ7Uuls3oi18YNhEXwUaYlOhhJ6X-_gmmH14dUhJvzpJa5UntrCgTp9GMVYMWcFHV8WAOifB-vOMJXJSSQhvbch5rRnyM221uoCoFkR_Hy1_HCQnkh0F4lldncqgXdh9JX9ZD0qsBRJt-m7h4XNvHTP6IGe0Hp54z8HEfLeP79Yf5Hq5k7rltrSoeAgLEyiJOwb739PoXi8rRi8j8W-YQvr6P8ecwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=qZy-V7rFi11zNMsjodnOdBAaBjjiQi5Q1f6qBCD1S50Cdm8bK46KD8G8D_WuX6VKmk2RYezIgbdWKXwQnXcB7Ipn2WTa08GJ58teE__f8Z6BtiPefCOA7FgZVwPqciaGGCauJ2nddJQLZPXeTPWjxxSsd0oNursT6Ur2V9veBJo0wWBbj21HQXWcUXcUlgiglFJq6tmiV7n8FuCFq31fdp6je_5jPwthpcKqu7qf401tw_OBYONR1YFB929ud0g525D9sMguoj6RH73leJJUN3WM11LkLsm65UD8EMBZB2DeWw2Ey_927JFShK7jbdfb_l8_tmxb5xfsY3ucF7TGMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=qZy-V7rFi11zNMsjodnOdBAaBjjiQi5Q1f6qBCD1S50Cdm8bK46KD8G8D_WuX6VKmk2RYezIgbdWKXwQnXcB7Ipn2WTa08GJ58teE__f8Z6BtiPefCOA7FgZVwPqciaGGCauJ2nddJQLZPXeTPWjxxSsd0oNursT6Ur2V9veBJo0wWBbj21HQXWcUXcUlgiglFJq6tmiV7n8FuCFq31fdp6je_5jPwthpcKqu7qf401tw_OBYONR1YFB929ud0g525D9sMguoj6RH73leJJUN3WM11LkLsm65UD8EMBZB2DeWw2Ey_927JFShK7jbdfb_l8_tmxb5xfsY3ucF7TGMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر تیک تاکر به اسم فاطمه تاجیک دیشب توسط چندتا دختر که میگفتن عکساشونو گذاشته چنلش خفت شده و خودشو دوست پسرشو کتک زدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71704" target="_blank">📅 09:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71703">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGLDBUFiswQpqOPX5pgnStcnhakg65J70EZ5mtGVgmbnpn10VfCO2UZ3qXEh3iWGS66b6jZKj8MwUe8E0eHMqWd2aSIPY62euwuKZdu7PNmz-xUhrh_3_QX3KkTEZMOQBHpT3-frlRHSTKHsR4LHRcAmYkHnCenGYjR5fECNhn5x82LBekgOiqAM9iMdzvu_fmKwRGOCRuWHbnftV_6K8pmYKkVqYXfV-NbOnGKlW-KKu30TGILvi3S00uk-vxRu8ebsqKu0I8msdAjwBb93Lck-u1KoxLfxQAPrXAt9BmJVi2KfjIYGe2VXbQtGiMDI_-Q12AgZGa7zTXtHLLJVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس:
فرماندهان ارشد نظامی ایالات متحده، اسرائیل و هشت کشور عربی هفته گذشته در آلمان دیداری محرمانه برای گفتگو درباره جنگ با ایران و امنیت منطقه برگزار کردند.
این نشست که به میزبانی «سنتکام» (فرماندهی مرکزی ایالات متحده) برگزار شد، با حضور فرماندهان نظامی اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر همراه بود.
دریاسالار برد کوپر ضمن تأکید بر تداوم حضور نیروهای آمریکایی در منطقه با وجود حملات ایران، شرکت‌کنندگان را در جریان برنامه‌هایی برای گسترش تردد کشتی‌ها در تنگه هرمز قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71703" target="_blank">📅 09:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71702" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71701">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaqkylF86K56M81l8nl-6aOypse6Q_VJivkoCggAHIZkMxCyJSa45CQFgAJn2MfTL3yXEhpMDfT-VIo-xwdnmunhJND39_qCWLkZ68SJgFvsRQQrvlKygyMFSBzRYItvidjtszf0A6ahl_c3huK2b7FfwfF871zpvEoM8lfXuj2dsHv9k8JpnGJBqGrViBGylFieA_aQmbVPqiGHXzg6tCySAXqlKoV_pP1jZ8IFrr8kHsrfIPOKLGN-DbofNW68pQn5fRmyzPRjK0CtL90Yzfnb-8yRmks9KW1YCNKt6FSevOv1wsKk6x9ACEUKvr7Lvzcv3rV13UdaN4s0hbdDSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71701" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71700">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71700" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71699">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71699" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71698">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG4fOjP8BbWwWbKifvoDHWn4yGq-luheQAcZ3mIOaHaMwXtLBHRRdL1pPzdHXl2QEZ56Bb_GTvxzT4zma4gO5kYD5nuCmrgT9RwBnRnsD2tC1YFz_Xwh0rc__ZN18iTpZfVrq9Czp4aukZ68e8glskZHk35MtvV6tQMt9M6gQwX6g2gTN7igdr3TjCZ5ffVU3sxc9lxFSFtp7VibpqIOjy1iGabQ1bNJzJkfYPyhm5DtXQhyl_LIMMZwoJZAO7uykzuXTzVwAVFl9_8tqy03kIHAuNgMcEfLeDE2mU_5fScw82rORyMT1g_jUvzx5qiQGyvRPIVe4TJkVVo_uFjhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آلمان (DPA) مدعی است که حوثی‌های یمن اکنون در تنگه باب‌المندب مین‌های دریایی کار گذاشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71698" target="_blank">📅 01:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=WQf_p44mauCtxTtdfFQ4wmNaiOCz61pZZDOkheho6n6eMTYgBW2nc63khLm7a8C0vMBFpQBX6eHP5HdbD7YgNBQQekLopOY77md8wKQFPvyt5Ti4H7_3gk0ZI3X48WhyqKudHKyLNwEB3Zskn3SWuB6tN9s_0-4MX_eHYNPpLl1VeWCX52ta32DIlHS3420ehADvHvU0twWq2tpe8Yp-XSGhBJCxGyx-ND5j8E4pcqmRsQTygn0k6Z7Gf_D-Ay7Us8xN1R0G1AKMu7ozfmWPUrQbtI92zNv44O1KtA7tpwgtlE1QGiPKWApc2hs524gLt5vavxwunP6aHZpwb4lbhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=WQf_p44mauCtxTtdfFQ4wmNaiOCz61pZZDOkheho6n6eMTYgBW2nc63khLm7a8C0vMBFpQBX6eHP5HdbD7YgNBQQekLopOY77md8wKQFPvyt5Ti4H7_3gk0ZI3X48WhyqKudHKyLNwEB3Zskn3SWuB6tN9s_0-4MX_eHYNPpLl1VeWCX52ta32DIlHS3420ehADvHvU0twWq2tpe8Yp-XSGhBJCxGyx-ND5j8E4pcqmRsQTygn0k6Z7Gf_D-Ay7Us8xN1R0G1AKMu7ozfmWPUrQbtI92zNv44O1KtA7tpwgtlE1QGiPKWApc2hs524gLt5vavxwunP6aHZpwb4lbhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا به‌تازگی طرح استیضاح دونالد ترامپ را که توسط «اَل گرین» (نماینده دموکرات از تگزاس) ارائه شده بود، با رأی قاطع و سنگین ۲۳۲ به ۱۴۷ رد کرد.
بخش بزرگی از دموکرات‌های مجلس به این طرحِ پوچ و بی‌معنی رأی منفی دادند، چرا که اَل گرین خودسرانه عمل کرده بود و آن‌ها می‌دانستند که این قطعنامه به جایی نخواهد رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71697" target="_blank">📅 01:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ونس امشب گفت که تو ماه‌های آینده، جنگ وارد مراحل جدیدی می‌شه؛
اما در شرایط فعلی همه‌ی تحلیلگرهای نظامی معتقدند که بخاطر انتخابات میان‌دوره‌ای، جنگی گسترده از آمریکا نمی‌بینم.
اما یه نکته‌ای اینجا وجود داره، انتخابات سنا و مجلس نمایندگان آمریکا  نوامبر ۲۰۲۶ (۱۲ آبان) برگزار می‌شه ولی نمایندگان انتخابی، با ۶۱ روز فاصله به سر کار میان، یعنی از ۱۲ آبان ۱۴۰۵ تا ۱۳ دی ۱۴۰۵، سنا و مجلس نمایندگان با همون اعضای قبلی ادامه می‌دن و می‌تونن قانون تصویب کنند؛ بنابراین از لحاظ تئوری، بهترین زمان برای حملات دوباره‌ی آمریکا همین دو ماهه (در صورتی که دموکرات ها پیروز بشن)
ولی یادمون نره که ترامپ یکی از غیرقابل پیش‌بینی ترین سیاستمدار های دنیاست
#hjAly‌</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71696" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca73G4MvbNOaBbJO6VlqD1VKcIxCtD8bD4k2Vee753RkJiq4foHQZ6fyWq_xJrJVZVPlxbcprI0owHBnClu1v6QycSwD5WonuLG5qDVd5whdtZftKlkSStGFkII5wY-j77f8rOX48YQ_Df-YDJrAOWQ3LYS415veshHLLX6pFNU6ZRKxvewepCE3hbyxSI32W-VNao5WRaUpQUS48klz5YTvyWU3v6x8Ftz0emltzE-9fhX-NJCnXSWs3V0TqgLQB-sYEudKJs22MbLUDRC0ItHJYlgVQZoWTi2eAybk3hcyRddayE36YFPDoyD_Hp_UNp1kFb45ok8UfHlWSUKCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلیا هاشمی:  امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت. مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71695" target="_blank">📅 00:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ایلیا هاشمی:
امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت.
مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین لحظه لغو شد؟ یا مسئله‌ای دیگر…
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71694" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=vu6kyg34YAWa2R36n5zt1zrKmGr0OE4R6eRTOQ92PVu7GORrl8bn9QOkHAVkl6N9zzUjLKHuisjhf1CIfZMN7ryCU-hLudOVbmgSVuGgvcNEl1O9fhdI4dRMyYjriUVu9q8oGSSbGZiBjs3O-zR2bg6hPY319AqTi7V8vMfuy-9RpF0gQCUeH5oone_W0vZuci8YGuNJ6PA-L296v0ka6Wn3MN54LM1klzFLtleBlVfwGcA3Hz7bcWit6dx-q_aC_7yJuBL_IHwwPpDxQpa25XA15k0XQbv0CubaAxBS8zUmqUYvekVWUpZMnizKpbl90J1UZLRtbAGjyzMgpRhhXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=vu6kyg34YAWa2R36n5zt1zrKmGr0OE4R6eRTOQ92PVu7GORrl8bn9QOkHAVkl6N9zzUjLKHuisjhf1CIfZMN7ryCU-hLudOVbmgSVuGgvcNEl1O9fhdI4dRMyYjriUVu9q8oGSSbGZiBjs3O-zR2bg6hPY319AqTi7V8vMfuy-9RpF0gQCUeH5oone_W0vZuci8YGuNJ6PA-L296v0ka6Wn3MN54LM1klzFLtleBlVfwGcA3Hz7bcWit6dx-q_aC_7yJuBL_IHwwPpDxQpa25XA15k0XQbv0CubaAxBS8zUmqUYvekVWUpZMnizKpbl90J1UZLRtbAGjyzMgpRhhXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سریع‌القلم:
آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات نظامی علیه ایران می‌آیند چه دموکرات ها پیروز شوند چه جمهوری خواهان!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71693" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71692" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71691" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=R5ajhrHObRtip78aehvKfEiA_yFx6ro82YgjOURwKoF_f4E6BWgBHqe3RrQZVokXGFJSGLHQHQM3XWnd9ThUUH4ZK8KtWBvngdeGRA3_x2DHjhgQuAW4KY8vW0mG031NK1bdUxpRQhIltdwHYMNaQrCZUKJ3VOZvw-Pc6PfoVNrFV3yeoVxJhokU2fnqMjV-xVMwObZCqypRLUBCauYLDvnSlXA0kK76d8DWJsGtI3BvuwrqHVOuikVBTSz43R8YUc_P-yhgCb8E7WZuOPZFHZ3dhr8csBLZl4u3i6OrVj-fCzMUxZJVOF60AN6pxrYLFuEw9sJgrSLsA0OvVbZ26g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=R5ajhrHObRtip78aehvKfEiA_yFx6ro82YgjOURwKoF_f4E6BWgBHqe3RrQZVokXGFJSGLHQHQM3XWnd9ThUUH4ZK8KtWBvngdeGRA3_x2DHjhgQuAW4KY8vW0mG031NK1bdUxpRQhIltdwHYMNaQrCZUKJ3VOZvw-Pc6PfoVNrFV3yeoVxJhokU2fnqMjV-xVMwObZCqypRLUBCauYLDvnSlXA0kK76d8DWJsGtI3BvuwrqHVOuikVBTSz43R8YUc_P-yhgCb8E7WZuOPZFHZ3dhr8csBLZl4u3i6OrVj-fCzMUxZJVOF60AN6pxrYLFuEw9sJgrSLsA0OvVbZ26g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای جنجالی یه
جنده
: دختری که ادعا می‌کنه باکره‌اس، دقیقا به چی افتخار می‌کنه؟
تو قطعا ایراد داری، مگه میشه یه نفر با کسی رابطه نداشته باشه؟ آقایون حتی توی سوراخ موش هم فرو میکنن، اونوقت تورو نکردن!؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71690" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=FsXHnogiu8vhd_xTetz1DxX_g3CaXG6uWnPHOYQFZuiYlI1TOxdNQa9EGjcp6VODC_jP0QZSysWYzPyeQYbmVnvVLPDhvnbrcRQCl0NzEdufruYTa-VvZYxrkyEE7W_76KqJVTxpDTRD9dT-0YKLMvnh5UOcdv2DA1HRiY8jrEJradU_eBYvfljJ0Q3DqT5FWpdm73jQnx6tsav5qH7bEySNx3tYHA24Isuz6ubGbHnyhCWEQquE2eZL7zdH8WAkTFpWBjjdk-JQVoFNPmGTYdW86rPowGY-HKI1D-HTecOcQZCvK6n25S4BtAC5R4gjHN6QBNtZ0bv-clVgP2DlZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=FsXHnogiu8vhd_xTetz1DxX_g3CaXG6uWnPHOYQFZuiYlI1TOxdNQa9EGjcp6VODC_jP0QZSysWYzPyeQYbmVnvVLPDhvnbrcRQCl0NzEdufruYTa-VvZYxrkyEE7W_76KqJVTxpDTRD9dT-0YKLMvnh5UOcdv2DA1HRiY8jrEJradU_eBYvfljJ0Q3DqT5FWpdm73jQnx6tsav5qH7bEySNx3tYHA24Isuz6ubGbHnyhCWEQquE2eZL7zdH8WAkTFpWBjjdk-JQVoFNPmGTYdW86rPowGY-HKI1D-HTecOcQZCvK6n25S4BtAC5R4gjHN6QBNtZ0bv-clVgP2DlZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی ایران یه تور راه اندازی شده به اسم «هیلینگ آب دریا» ، این شکلیه که میرین کنار ساحل و تا جایی که میتونین باید گریه کنین.
برای شرکت در این تور هم میلیونی باید پول بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71689" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان با انتشار بیانیه‌ای مشترک، برای(فردا) روز چهارشنبه ۲۵ شهریور ۱۴۰۵ (۱۶ سپتامبر ۲۰۲۶) فراخوان اعتصاب عمومی صادر کرده است. این فراخوان هم‌زمان با چهارمین سالگرد ژینا (مهسا) امینی و آغاز اعتراضات «زن، زندگی، آزادی» اعلام شده است.
در این بیانیه از بازاریان، اصناف، کارگران و دیگر اقشار جامعه خواسته شده است با تعطیلی مغازه‌ها و بازارها و خودداری از حضور در محل کار، در این اعتصاب مشارکت کنند. صادرکنندگان فراخوان، وضعیت اقتصادی، فقر، گرانی، بیکاری و همچنین آنچه تشدید فشارهای امنیتی و صدور احکام سنگین می‌دانند را از دلایل این اقدام عنوان کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71688" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265561794f.mp4?token=WKcqVeGnRASMaBcr1RBgS4HazvGw6SvTIGXSUC7D0HR7vzcRlmNVue4hl2dYUge708Wlx6TlcrtLI2L9sHVjC81GerayHGQip49yhUNdoEqJMzJXcAcsCBbBo9rI-lxS2wnAVPs1bImDocdrHkKR92vhzGz3pq4tqvKK9BiH_2rAgPN7h4WeucTP18A5jGTxTP3_gIUL9s4FTN1BMnK-VJW2BBJxwoqWcwA7Tw7q1iBp8-60EN1jAXkRacDu6-7yac146DMi-2p2E6G_YpYbmmgmlP-mzn92HR1xicUfUudmmLImsZvffax1840npBVoAOKnYRXBsydPtw-a0jfwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265561794f.mp4?token=WKcqVeGnRASMaBcr1RBgS4HazvGw6SvTIGXSUC7D0HR7vzcRlmNVue4hl2dYUge708Wlx6TlcrtLI2L9sHVjC81GerayHGQip49yhUNdoEqJMzJXcAcsCBbBo9rI-lxS2wnAVPs1bImDocdrHkKR92vhzGz3pq4tqvKK9BiH_2rAgPN7h4WeucTP18A5jGTxTP3_gIUL9s4FTN1BMnK-VJW2BBJxwoqWcwA7Tw7q1iBp8-60EN1jAXkRacDu6-7yac146DMi-2p2E6G_YpYbmmgmlP-mzn92HR1xicUfUudmmLImsZvffax1840npBVoAOKnYRXBsydPtw-a0jfwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی سخنگوی دولت :
امیدواریم نیازی به تغییر سهمیه‌های اول و دوم بنزین نداشته باشیم؛ ولی اگه بخواهیم گرون یا کمش کنیم حتما شما مردم را در جریان خواهیم گذاشت و بدون اطلاع‌رسانی کاری نمیکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71687" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شنیده شدن صدای دو انفجار از سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71686" target="_blank">📅 21:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/61894edf33.mp4?token=rr09PEqLFDndmDt0ke88xlncRPEgPgWQnr7v8UbxhxzOsGJv3l04wP5GR2A92DkL8dzDj3Y-LeGo8aZDsCSYAHXBXn5a_xVTiJZ-mB9PSNXWViZ68-x7u83nYpkSfu8AL5G0TwWwB_lmRpa7ZFoyILepcWAqMbm2vfQraLqXynr1c8vPkl99CfoJG49h_Db84tyWepwAVk3kOnu2caeK1d0CoC0bXwKvGAN4lUUXCD72MTo2GTA9a96308x_QdzTFVh9jAx5EZpiKge5yrxH5RVYUMKwSZ5KQiaGq7VzxnrHwRCregpdSBbaj-5aLWQe2DmkiSLQFnFvR1y2Sf4sOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/61894edf33.mp4?token=rr09PEqLFDndmDt0ke88xlncRPEgPgWQnr7v8UbxhxzOsGJv3l04wP5GR2A92DkL8dzDj3Y-LeGo8aZDsCSYAHXBXn5a_xVTiJZ-mB9PSNXWViZ68-x7u83nYpkSfu8AL5G0TwWwB_lmRpa7ZFoyILepcWAqMbm2vfQraLqXynr1c8vPkl99CfoJG49h_Db84tyWepwAVk3kOnu2caeK1d0CoC0bXwKvGAN4lUUXCD72MTo2GTA9a96308x_QdzTFVh9jAx5EZpiKge5yrxH5RVYUMKwSZ5KQiaGq7VzxnrHwRCregpdSBbaj-5aLWQe2DmkiSLQFnFvR1y2Sf4sOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، هواپیمای تهاجمی A-10C Thunderbolt II نیروی هوایی ایالات متحده، مواضع داعش را در نزدیکی «جبل‌العمور» در شرق استان حمص (مرکز سوریه) هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71685" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1vZr_OPiWthA1Vl-mWpjnLPnR2_Ne5L0-tM9GTwopFl13Lp22aKQmFI5NccTaBCaB-EV5GPPJhXm0ysEtp9dQESB8CoZeMugOgGK-5k1m-JFhrZGcm7pnr4QuwKCKj0cFtFCDNV2IIeUVyddenano0L88lh8iiRP3Qfd8--9bJURVmighJi_eIjqb2q4TZd3JLGoA2nKpzde77TpjWw7SBV9j3WFk6y0ys7s_XQnNXEaQhGQ1GF2bcSXKKBWrhvSDOglcQ_IQro7Yz9moWGEqGPkrSx5bCPadeLBluG3j3jdUokAZYXiu797HzPt9Y5kzmgAQW0PsqzWmKZ45kETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست:
دولت ترامپ در حال تدارک فروش ۴۰ هزار بمب سنگین (از انواع MK-84 و BLU-117 با وزن ۲۰۰۰ پوند) به ارزش ۲.۸ میلیارد دلار به اسرائیل است؛ این بزرگترین معامله تسلیحاتی از این دست در سال‌های اخیر محسوب می‌شود که هزینه آن از محل پول مالیات‌دهندگان آمریکایی تأمین می‌گردد.
این‌ها همان بمب‌هایی هستند که بایدن پیش‌تر به دلیل نگرانی‌ از تلفات غیرنظامیان، ارسال آن‌ها را به‌طور موقت متوقف کرده بود.
این قرارداد برای تصویب به کنگره ارجاع می‌شود و می‌تواند آزمونی برای دموکرات‌ها باشد؛ چرا که در ماه ژوئیه، بیش از ۱۰۰ نماینده دموکرات مجلس نمایندگان به کاهش کمک‌ها به اسرائیل رأی داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71684" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71683">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=cTysnMp6gX1Aj0CtyXfuB-omS9cC3k4uwkuRAb1mHL-hCasBJ4LL8mOJOEAYLITofveUQgH8DlJPRIXVVVE96NBMjs_6Crul6g2ik7vp0VOQO3liXCcxtBjCMMdJGtl3W-WpIiLdsFRbE8Slzy9oZ8JK8exSv_elpHsmo-9T25WjjGolrWQqCwfm6MpZDsU0hGYZhOD79Eab7M5t6X-0WOQ--rcIved1Hak7gaefF5f6kPLxqNfkORUY_AyLVmA1Pl7ZwC4o1jlj6sWq8AzW9UmZWAzSaQFsjBIk53fB-88bI7KLFaepMnjBE1Z4WMnF5_X0EzFgkEF0IDbFLubGcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=cTysnMp6gX1Aj0CtyXfuB-omS9cC3k4uwkuRAb1mHL-hCasBJ4LL8mOJOEAYLITofveUQgH8DlJPRIXVVVE96NBMjs_6Crul6g2ik7vp0VOQO3liXCcxtBjCMMdJGtl3W-WpIiLdsFRbE8Slzy9oZ8JK8exSv_elpHsmo-9T25WjjGolrWQqCwfm6MpZDsU0hGYZhOD79Eab7M5t6X-0WOQ--rcIved1Hak7gaefF5f6kPLxqNfkORUY_AyLVmA1Pl7ZwC4o1jlj6sWq8AzW9UmZWAzSaQFsjBIk53fB-88bI7KLFaepMnjBE1Z4WMnF5_X0EzFgkEF0IDbFLubGcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از نفتکش «ال‌گایا» (EL GAIA) پس از اصابت به آن در بخش جنوبی تنگه هرمز منتشر کرد.
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که ایران ماه گذشته با موشک و در پایان هفته جاری نیز با پهپاد به این نفتکش حمله کرده است؛
در مقابل، ایران مدعی است که این شناور پس از ورود به «منطقه ممنوعه» در بخش جنوبی تنگه، با یک مین دریایی برخورد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71683" target="_blank">📅 20:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbAMrwzFfiZt8txI1h40TaPuAYvn_BICHbkKVvJ8soPxHHWzXm3JaNQ5rBDYbJMpk-molnnE9p5bwYV9uzqCVdbYTk9uge8i9QjfH4ejWlbLddNLfYcP5oUl6ihYBlxkagL3Yg3yA-B_LqHivanviDzzetRd9JodGB5Ti3vH2pZ85GQHf-MzKjshhIDJkFBkmmLnlGCexlJoQFzv8ReJI3rpwVslavi4GsPZBFj3CeOXyAudqzi-osRKulWOh2hGi7QH6Dz8Msgz1oSCzA5zk7OM7UOgVHn2aWdVjqzGqDl7sfYNEugPBy7IBnlCLeTFfSwmkF8PkSPTNv7UDqpy_gGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbAMrwzFfiZt8txI1h40TaPuAYvn_BICHbkKVvJ8soPxHHWzXm3JaNQ5rBDYbJMpk-molnnE9p5bwYV9uzqCVdbYTk9uge8i9QjfH4ejWlbLddNLfYcP5oUl6ihYBlxkagL3Yg3yA-B_LqHivanviDzzetRd9JodGB5Ti3vH2pZ85GQHf-MzKjshhIDJkFBkmmLnlGCexlJoQFzv8ReJI3rpwVslavi4GsPZBFj3CeOXyAudqzi-osRKulWOh2hGi7QH6Dz8Msgz1oSCzA5zk7OM7UOgVHn2aWdVjqzGqDl7sfYNEugPBy7IBnlCLeTFfSwmkF8PkSPTNv7UDqpy_gGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
تنها کافی است به سخنان رئیس‌جمهور، رئیس مجلس و رئیس بانک مرکزی ایران اشاره کنم که اذعان داشته‌اند اقتصاد کشور در وضعیتی بسیار وخیم و بحرانی قرار دارد؛ هشداری که خطاب به هم‌قطاران تندروی آن‌ها در سپاه پاسداران و همچنین مردم ایران بیان شده است.
ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم؛
و در کمال ناباوری، کشوری که سومین ذخایر بزرگ انرژی جهان را در اختیار دارد، اکنون با قطعی برق سه تا چهار ساعته مواجه است.
این وضعیت اسفبار اقتصادی ناشی از تحریم‌هاست؛ ترکیبی از تحریم‌ها و اقداماتی که ما طی ماه‌های گذشته برای شناسایی و مسدودسازی مسیرهای مالی و سیستم‌های پرداخت آن‌ها انجام داده‌ایم و در حال اعمال فشار شدید بر آن‌ها هستیم.
به باور من، واکنش‌های تند و خشونت‌آمیزی که اکنون از سوی آن‌ها شاهد هستیم، درست مانند رفتار حیوانی زخمی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71682" target="_blank">📅 19:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=UGhYWEfAk4Roc3RvskP5lo83zp176mBjf434qYeEKNDEZA-08VDdtC0yitXlHjJjy6tWAno6wMD2MJ65pRp7LY2OluewQVTswaKVRBhmBgz_lYwyCqkcBLcSB5Oshkb_jeixpSWD1ztb0vNmQnirLW0a7fmV7NN3eDaHotOOuU-ZWbopWzx28jvA4N0Bkgxov60EPSMd6TUqH3QCKK3dTJcPyPQuBc658e3blzIbJSWxHaJf1uSqAyWNWoekmcge4_qqnCsyXNVCFUMMW-_g5dYn0qEsuWSmcg1XGKnuep_1CR7xIJrXxLenoK7mUKmr-2BTutr-OD6huAoUgqknOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=UGhYWEfAk4Roc3RvskP5lo83zp176mBjf434qYeEKNDEZA-08VDdtC0yitXlHjJjy6tWAno6wMD2MJ65pRp7LY2OluewQVTswaKVRBhmBgz_lYwyCqkcBLcSB5Oshkb_jeixpSWD1ztb0vNmQnirLW0a7fmV7NN3eDaHotOOuU-ZWbopWzx28jvA4N0Bkgxov60EPSMd6TUqH3QCKK3dTJcPyPQuBc658e3blzIbJSWxHaJf1uSqAyWNWoekmcge4_qqnCsyXNVCFUMMW-_g5dYn0qEsuWSmcg1XGKnuep_1CR7xIJrXxLenoK7mUKmr-2BTutr-OD6huAoUgqknOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر، آتش‌سوزی‌های گسترده در تأسیسات ذخیره‌سازی «آرامکو» در «ابها» واقع در جنوب غربی عربستان سعودی را پس از حملات پهپادی و موشکی حوثی‌ها نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71681" target="_blank">📅 18:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
لحظاتی قبل یک پهپاد دیگر از نوع MQ-1 متعلق به آمریکا بر فراز تنگه هرمز با استفاده از یک سیستم پدافند هوایی متعلق به نیروی قدس سپاه پاسداران انقلاب اسلامی سرنگون شد.
این سومین پهبادی است که سپاه مدعی سرنگونی آن در روز جاری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71680" target="_blank">📅 18:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8132b94509.mp4?token=HRNwzUxFg5MIqUfXaH1fjbiq440Lp5Bg7mHkiiolVXHsCl7dCGGXAJ5ybq-Kri4Hz5UNoKcDIdIKyVG5YnofHPPNU_Led2YNCZYLROGW36fOA2QZkFyONIocZ_ZRFNXUPaIIUEIi1BgEr0MN1SpZFJ2-P6Qr40JiYR8M7QvCa9nssyazeGzBh2KpYuvRX0E7lhSZKMgzCwaJ3RdRqPO5P9P1-754ZnveWpF1l2HNJjg-YZC9Sfp7ITn9TIYg1xP1FDgf_83L2l4ca0_9G-yLBiuGj7ZxeC0GdEinpb7fecU5_3Z4vC8QKI6ccLOhA8mYr96j8-3gP8B-vWmquk3nlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8132b94509.mp4?token=HRNwzUxFg5MIqUfXaH1fjbiq440Lp5Bg7mHkiiolVXHsCl7dCGGXAJ5ybq-Kri4Hz5UNoKcDIdIKyVG5YnofHPPNU_Led2YNCZYLROGW36fOA2QZkFyONIocZ_ZRFNXUPaIIUEIi1BgEr0MN1SpZFJ2-P6Qr40JiYR8M7QvCa9nssyazeGzBh2KpYuvRX0E7lhSZKMgzCwaJ3RdRqPO5P9P1-754ZnveWpF1l2HNJjg-YZC9Sfp7ITn9TIYg1xP1FDgf_83L2l4ca0_9G-yLBiuGj7ZxeC0GdEinpb7fecU5_3Z4vC8QKI6ccLOhA8mYr96j8-3gP8B-vWmquk3nlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پروازهای داخلی(کرمانشاه به مشهد)دچار سانحه شده و بخشی از کابین دچار شکستگی و اسیب میشه، خوشبختانه مسافران این پرواز سالم به مقصد رسیدند. جزییات دقیق این پرواز و نقص فنی هنوز مشخص نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71679" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71678" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71678" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogwZLgo5fVQwSS9kUvswEX8A5W-p7Vspno6rtwsh8AQ7rwNhKXmTuYppxpZA1fcKmqp3Af_uDegzcXqJGFM51hbrVMI5suXP8iV-2G5xLhUnukMYUiLTJ8ZaeiFu64iscAd-iCaluWUPlFOXkGTXigqjvXq-pCmI1trikO6qaEufeRlGzIsggd_0dL3ynZVWYcTQkFvNS8wCmWcQ_lYSMMViLuSo79qRbFvfaFPBs3maIK4QNQt3cQ8DoBtX7uBsQCscAse4dMEDnDAxqX6DX0aMQMRxX_bjDuUGBYirMBMDmoDZ4YQMf1Nrq6jQ0LBzejjbJzoQW6YhstQDEmyQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71677" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=cdw-qqkdlKvwQVfESBDFQIPMiu63QS3cwctNDAEeaQns2rP0i8fhrW4STBShi1yu07FxKH8q0htMUfizkC0cuqWsPePgtpaQ79_YVMczN_zOvzI3IePo2ErP5LBtX1q4HvlyNBlzi7akcUAr7xNHGJqTE1Qicy_cgqWIgMkYjsf2viKMJsdnYHctc7ScCO-3EaGHdHI2Sw6tWwbFaRWoNH7Gaa3t6MLVm2pDYZuycpBzZnBx6PZRzAgCzYCu2huPih_PQJt_73rbGFVIqxefN76aiUzoETPd3kYBTeHmJE1OpA2ZTyEaTYI5GF1ujh_bgDr9v6ze2F6Y_EUhF_b4jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=cdw-qqkdlKvwQVfESBDFQIPMiu63QS3cwctNDAEeaQns2rP0i8fhrW4STBShi1yu07FxKH8q0htMUfizkC0cuqWsPePgtpaQ79_YVMczN_zOvzI3IePo2ErP5LBtX1q4HvlyNBlzi7akcUAr7xNHGJqTE1Qicy_cgqWIgMkYjsf2viKMJsdnYHctc7ScCO-3EaGHdHI2Sw6tWwbFaRWoNH7Gaa3t6MLVm2pDYZuycpBzZnBx6PZRzAgCzYCu2huPih_PQJt_73rbGFVIqxefN76aiUzoETPd3kYBTeHmJE1OpA2ZTyEaTYI5GF1ujh_bgDr9v6ze2F6Y_EUhF_b4jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
بسنت درباره ایران:
ترامپ در حال اقدام علیه رژیمی است که خود را وقف شعار «مرگ بر آمریکا» کرده و برای تحقق همین هدف به دنبال دستیابی به سلاح‌های هسته‌ای است؛
اقداماتی که رؤسای جمهور پیشین مدت‌ها از انجام آن طفره می‌رفتند.
تحت رهبری او،آمریکا دیگر تهدید ایران را مدیریت نمی‌کند؛ ما در حال پایان دادن به آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71676" target="_blank">📅 18:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSzXE5yIJdFqikBwn3PWsDfq2ZWA5-dBymuHWL_OVlzXT4aLeN9fcRUTUimgOOl8IDZjU45IEbuNv_ZBBR4R8USKjFhMnBGzF9eHWM8HhRPdtfPasI8L4p8shjczEOIzRSBZ99QxDpw9PmdKejGG6tVkCgRfziho45CDWkphnu8NJNGmKFyEhF8hgHs54mevfBN0T77a6PNeX_L7WGZuhjqjkwhXGA2s_ZjMPfQPoiBNk-2zOHZc2qNoRirbEvJf-PbnNeTsbzXbWjfoCELKRBw4Gi9ZAIjiLRifuVU_IiN5NWYZKUPMemfRaiwOOPu4zFvQ_5ieukUbQQFVhjb_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس. تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.   @News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71675" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71674">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=LF1oBOfgVpHHey6TAekZaxSl_rCB0PMlU0XjSMRQed7hv3kL5WBg5bglVW1HopYRKbV9NxGDglHyY1FzG91dZ10oyaTqViJgZO3K72szr9ObLfuoZ-oq5uJ219kNmn7Ls1L13wxftY8AwXE6679hGZWPjtr4pg-8dX-ZAYaVSzYJUoSRJL6oEkE4Kbmln-gcY-k-NGWc4666qu5u5sDj9BzP3zI8nnRqPM00YCp4E8zzkt1KThhriKx44j73ANDF_-TB74w0wmyjjU6C9rRd9pUEv7lu59vrvHrslSI0cCtENdDyBZHsxWjZF9tQw-BFFrSVx6w1mFYTxhvOwQyyVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=LF1oBOfgVpHHey6TAekZaxSl_rCB0PMlU0XjSMRQed7hv3kL5WBg5bglVW1HopYRKbV9NxGDglHyY1FzG91dZ10oyaTqViJgZO3K72szr9ObLfuoZ-oq5uJ219kNmn7Ls1L13wxftY8AwXE6679hGZWPjtr4pg-8dX-ZAYaVSzYJUoSRJL6oEkE4Kbmln-gcY-k-NGWc4666qu5u5sDj9BzP3zI8nnRqPM00YCp4E8zzkt1KThhriKx44j73ANDF_-TB74w0wmyjjU6C9rRd9pUEv7lu59vrvHrslSI0cCtENdDyBZHsxWjZF9tQw-BFFrSVx6w1mFYTxhvOwQyyVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سی‌و‌سه پُل اصفهان، یه پسر نوجوون اومد مثلا یه حرکت نمایشی بزنه و از یه ارتفاع نسبتا بلند بپره پایین که فرود ناموفقی داشت و با سر رفت تو زمین...
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71674" target="_blank">📅 17:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=H2kzzhyBhUmIGMulX6h6KdrUTZ1XmgDOUErue9jdCGm8ElgVvmRXGXZwT1Jaix55Iwf9JjCyzbHQP6AkMvAmwCqCOCC8v3KivOTSBcEhiUZ1qdB9EMJf2CCBot3rzOTWZHQk1WbuuAgVx2quRku0kPubuYvxHz8GirIzIo19yMVJa438tqd0puXy811hxKfWUZlTiDeK67CpT7515VP6_ThRzgi4wGi8Kjxgd0ae9rt1AqNqLMo-LDh2Kj43keuS2ZIdzv2lQLmXlO99jCzad8qbxO-YxELWCTdqwdzWB2BVOnhUn1vQiGmcCklT7xWIpmxpPZmsQnRp8gKHpl0g1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=H2kzzhyBhUmIGMulX6h6KdrUTZ1XmgDOUErue9jdCGm8ElgVvmRXGXZwT1Jaix55Iwf9JjCyzbHQP6AkMvAmwCqCOCC8v3KivOTSBcEhiUZ1qdB9EMJf2CCBot3rzOTWZHQk1WbuuAgVx2quRku0kPubuYvxHz8GirIzIo19yMVJa438tqd0puXy811hxKfWUZlTiDeK67CpT7515VP6_ThRzgi4wGi8Kjxgd0ae9rt1AqNqLMo-LDh2Kj43keuS2ZIdzv2lQLmXlO99jCzad8qbxO-YxELWCTdqwdzWB2BVOnhUn1vQiGmcCklT7xWIpmxpPZmsQnRp8gKHpl0g1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71673" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71672">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نفتالی بنت درباره ایران:
این رژیم فاسد و پوسیده است؛ همچون درختی که از درون دچار پوسیدگی شده و سرانجام فرو خواهد ریخت.
در مورد این درخت پوسیده، می‌توانیم اینجا و آنجا حفاری‌هایی انجام دهیم. منظورم صرفاً اقدامات نظامی (کینتیک) نیست.
صحبت من درباره اقدامات اقتصادی، کارهایی که نمی‌خواهم نامی از آن‌ها ببرم، و همچنین تقویت معترضان داخلی و تقویت دشمنانِ این رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71672" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71671">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=moNxkC09sTMFmLTrEqNgSwDY9lCrNMQKos6vGJIQKMcTccsKR3Kq4VSNygdmLQHiU-GwbOqFaMIjg2_47f0aKDRYSKIPMCD-fB6tDNIhHHt-vOLLg4YMfg0UzaRtAzGajE4P1y-AeePpLKBSSJlytGzMEND55wZ7pwpYPTO2O2yYgNDgK2dT1aea4NJa7NM706-C-3fGtyqeBOeo7n-Pp2Vg0B_y31tch1Z_VEM3br1vz1W8h5eoK7fNn0RXnU23NuJ5uBz7uHR6gUi3_fTskaDvJYbuXscU6Fk4P6s9AEu6UZ3h36cLyDBxeDewie2g1idfpVHDbwxpOReyy-i4XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=moNxkC09sTMFmLTrEqNgSwDY9lCrNMQKos6vGJIQKMcTccsKR3Kq4VSNygdmLQHiU-GwbOqFaMIjg2_47f0aKDRYSKIPMCD-fB6tDNIhHHt-vOLLg4YMfg0UzaRtAzGajE4P1y-AeePpLKBSSJlytGzMEND55wZ7pwpYPTO2O2yYgNDgK2dT1aea4NJa7NM706-C-3fGtyqeBOeo7n-Pp2Vg0B_y31tch1Z_VEM3br1vz1W8h5eoK7fNn0RXnU23NuJ5uBz7uHR6gUi3_fTskaDvJYbuXscU6Fk4P6s9AEu6UZ3h36cLyDBxeDewie2g1idfpVHDbwxpOReyy-i4XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌ های این خانم به‌شدت وایرال شده و دخترا هم خیلی بهش انتقاد کردن:
اگه یه مرد، دارایی های خودش رو به نام خانومش بزنه، اون زندگی رو با دستای خودش نابود کرده.
آقایون اگه ۵ تا خونه هم به نامشون باشه، هیچوقت تو دعوا خانوم‌ خودشون رو بیرون نمیکنن
ولی اگه خانوما یه چیزی به نامشون باشه به این موضوع فکر میکنن که میتونن بدون اون آقا ادامه بدن.
من خودم خانواده‌هایی دیدم که به دخترشون میگفتن تو که ماشین و خونه به نامت زده دیگه احتیاجی بهش نداری، خودت برو زندگی کن.
خانوما اصلا جنبه‌‌ی اینکه چیزی به نامشون باشه رو ندارن، اون اگه بخواد زندگی کنه با یدونه سکه هم زندگیش رو میکنه، آقایون بفهمید من دارم چی میگم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71671" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71670">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=BdkyHeGi-mauYx5ojAkJBWUyVFUhtnxCx91q0HzQZOO1E_-3oDtTXiu12ec6XFdV69J9QW_qfKkH0TkwbDM80XTKm9RWrZ80AaCl9kSlgTzNT2-zwOp47EXml62I6hu8qspru1FSNC_nXVMJj-p6tW6Jgp2AB88mJ0ahfLtzANwajWqny2kzPolyLb52hQERnGsCZ2oPLCVuun7KcVzA4Ydu0FtP0MefQ4geOREmiR82zt2rnUFyQtQARbJio3vjpY4MCoPMWHM0Uszv1OtogMnydIqjSYGa3w4oWwut_p_Rcs95GfiteFuZl030s-MbQHcaEgB8r8jvX-pMNB9sAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=BdkyHeGi-mauYx5ojAkJBWUyVFUhtnxCx91q0HzQZOO1E_-3oDtTXiu12ec6XFdV69J9QW_qfKkH0TkwbDM80XTKm9RWrZ80AaCl9kSlgTzNT2-zwOp47EXml62I6hu8qspru1FSNC_nXVMJj-p6tW6Jgp2AB88mJ0ahfLtzANwajWqny2kzPolyLb52hQERnGsCZ2oPLCVuun7KcVzA4Ydu0FtP0MefQ4geOREmiR82zt2rnUFyQtQARbJio3vjpY4MCoPMWHM0Uszv1OtogMnydIqjSYGa3w4oWwut_p_Rcs95GfiteFuZl030s-MbQHcaEgB8r8jvX-pMNB9sAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی نیروهای انتظامی به سمت بالگردآمریکایی در جریان عملیات نجات خلبان مفقودی آمریکا در روز روشن
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71670" target="_blank">📅 15:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71669">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=G80qyTWxokgNv8Qp1I3mmfTPM-3q_hWPDpRXa86DKWJb9Y8Vt8oW87u2CHGpKccxH8bEbcrCMyeB9xLEDP25Wz70HRHA1PYmt7AvY4zQa25TBDvPX-7qVcUlq9nDhhaM0OQ0AT7P69oQfyuxH_4WyZ7q6AB8XpMH8cVS_rkEnQuJsxc_9s8cCZe_gGBeBDYbgyebDS6If6V0mAdF_aCjh8mkVCt4RPnoRP_F6h0jq25FYECl0zZz8Ajv0ogLCQmQ9kFFWiyMaEi3tX8rJbkwET2A7B90TDUIhQgMwzBuctDYBVM1kXXOYXBPfDQv-tqcIzb48Z3XKoi5IYB4mK8NUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=G80qyTWxokgNv8Qp1I3mmfTPM-3q_hWPDpRXa86DKWJb9Y8Vt8oW87u2CHGpKccxH8bEbcrCMyeB9xLEDP25Wz70HRHA1PYmt7AvY4zQa25TBDvPX-7qVcUlq9nDhhaM0OQ0AT7P69oQfyuxH_4WyZ7q6AB8XpMH8cVS_rkEnQuJsxc_9s8cCZe_gGBeBDYbgyebDS6If6V0mAdF_aCjh8mkVCt4RPnoRP_F6h0jq25FYECl0zZz8Ajv0ogLCQmQ9kFFWiyMaEi3tX8rJbkwET2A7B90TDUIhQgMwzBuctDYBVM1kXXOYXBPfDQv-tqcIzb48Z3XKoi5IYB4mK8NUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر زنِ مجتبی خامنه‌ای:
مجتبی خامنه‌ای با همسرش سریال " فرار از زندان " رو مفصل نشستن دیدن و درباره اتفاقاتی که داخل سریال افتاده بود هم صحبت میکردن.
یه بار تو یه جمعی گوشی یکی زنگ خورد، من گفتم این چه آهنگیه دیگه؟ که یهو مجتبی گفتش این آهنگِ یکی از فیلم‌های کریستوفر نولانه دیگه، چطوری نمیشناسیش؟
‌
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71669" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71668">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohYG_osFtpqjn57RqzjWasGomVQxFp1r7XOaK2zuzbPiz_Sm_les28V8Xo8N2xbdtM02crdHRl2hYmMe4qTxGi9NwNYU_VchtYXR6er2s7OwHVDJE8V3R5Rd0XWrzGQMVnEiu8axPfaTdWx0hyhyb_GUoRn4c2sYvxqYl3WtKA-pEdrS8UBK6zRolF2amjQ3mEN8AasEdJFIazXiKT8zUv-EoFcBJdTkZl8UAxR5FFW0qPL5ycXy667kumustt-LPevBYtvcD22ZqcLDzvM7ClPf8yZ938buQ0OjG14H1jkXX66RwkqzMhJ9YgCdZMDct8BF2g-l_rtLmGGhPaG0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی:
«نشست عمان» با حضور کشورهای خلیج فارس برای تثبیتِ مسیر تنگه هرمز، با نقش‌آفرینیِ جدیِ آمریکا و برخی از کشورهای حوزه خلیج فارس فعلا لغو شد
عربستان» به بهانه اصابت خط لوله‌اش و درخواستی که از پاکستانی‌ها داشته تا ایران را راضی کنند که به انصارلله بگوید از فتوحاتِ جدید عقب نشینی کند، «بحرین» بابتِ ناراحتی از جنگ رمضان و پرتابه‌‌های متعددی که بخاطر میزبانی از زیرساخت‌های نظامیِ آمریکا در خاکِ کشورش دریافت کرده و «امارات» هم بابتِ اُفت جایگاش در آینده‌‌ی منطقه در صورتی که مسیر جدید تنگه تثبیت شود، در نشستِ مهمِ عمان شرکت نکرده و کارشکنی کردند!
ولی بازیگرِ اصلیِ لغوِ این نشست، آمریکاست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71668" target="_blank">📅 13:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71667">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حملات موشکی/پهبادی حوثی های یمن به مکه، طائف و جده عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71667" target="_blank">📅 12:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71666">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU-XcCT091USvQa7bOo4yS49SLe99jbDxdHQegLxwJXdfAYl-wHhKOZnIDHlen6I2fAibE5QIhPLc9iqasDglVO_LTSXFUFqEQ6_0c0DY9k83g6mq2LvGw_dy3K3HEBlgsiSeFBpT-XeRDxiCElvOryY3IVCAZglaynHTvgsSQsppEYDw4pd5CdKCYzC32rVsJJPYG1DSxM1ni5c9FZrJ06ZouRPVQpGSeNpdGZSlBnZawLn0Y1vASgmv8yWla4_ugRoI7THB026TrNiuK4LHFGRE4PFZ2NijfreufdhgEgdsbIE3pVU685dznwC0UaOrJNX--eQIBqwjZWuxLS8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) :
گزارشی با تأخیر زمانی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک منبع موثق گزارش داده است که شناوری مورد اصابت یک پرتابه ناشناس قرار گرفته است.
هیچ‌گونه خسارت یا پیامد زیست‌محیطی گزارش نشده و مقامات در حال بررسی موضوع هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71666" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71665">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=WUNCOpwsRMxltKYf5VNclfftZdbvsRIN4n7eqirpbtcw0d9L0ELI-RGpHqqtpolQt4ILSO3oYgwe_oc2MnBuyrMTIzUq5VLmnxpq7bnDo4B1VgZzEgPNrizryrcvUpurNnirL9E4bMo8t-f4rr8RdVR9TiGNMPM4k_QKpSLVLN7myCgKz56trzCOwVneOn49VYLBMuGoNUsy2xjjznU35Y4RPj-ofuAQzNTWsXZgV2vsRGwVaLLP2dIokq9ohRQJL8gSlcLdbfsZBgaflqse-P071TIEch5T2YAIx6uW52tN29kcrpxfBiJw9eRAJIvOPj9cCIySWJ1kyVwcECMG0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=WUNCOpwsRMxltKYf5VNclfftZdbvsRIN4n7eqirpbtcw0d9L0ELI-RGpHqqtpolQt4ILSO3oYgwe_oc2MnBuyrMTIzUq5VLmnxpq7bnDo4B1VgZzEgPNrizryrcvUpurNnirL9E4bMo8t-f4rr8RdVR9TiGNMPM4k_QKpSLVLN7myCgKz56trzCOwVneOn49VYLBMuGoNUsy2xjjznU35Y4RPj-ofuAQzNTWsXZgV2vsRGwVaLLP2dIokq9ohRQJL8gSlcLdbfsZBgaflqse-P071TIEch5T2YAIx6uW52tN29kcrpxfBiJw9eRAJIvOPj9cCIySWJ1kyVwcECMG0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبه ناو سپاه با عنوان «رودکی» که در جنگ ۴۰ روزه منهدم شد در حال غرق شدن است. این کشتی تجاری بود اما به نظامی تغییر کاربری داد و گفته شد هلی‌کوپتربر است اما هدف حمله قرار گرفت و نابود شد.
در جریان جنگ ۴۰ روزه تقریبا تمام شبه ناوهای سـ.ـپاه و ارتش از بین رفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71665" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71664">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71664" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71663">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLW9wvbSvpuCqjS_VKcaVv2sMWvzMtq6ZlabcymBvGXtXGU6aZSdwFv1m2PtemSSgCWTjesHrcICBz70mBffu0v7KQ7bsFLSuzSG6doymsH5bMWwcHeXPXRGqGyutPayTcafXv3Uxb-LR_7uUM3OoMo51caK_tp_JCvBU8o_9JlBc5WbGuea3XxK8zbSpYxm_eLG5LO2szr7m-uZhysweDO_mH56iAOUVidLpKO0ELGaBM4QBfjKW5GpCrSwOApqdnyQ7At1qhLbamKZ4s_ocUCacSQSGlsPzrNJkTu7FWNJEj1dILp4OYpOATeMruvAhrrikHuw3-jzm8tOfxkVEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71663" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
