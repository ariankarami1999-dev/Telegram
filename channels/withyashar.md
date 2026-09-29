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
<img src="https://cdn4.telesco.pe/file/sUayCqhsaXomu0GcDXiCvYhm0eNJ1Jv7ooLf8njMzmT-TWDuK7ExgC05MgTTEU1OUv6z_9xaccLEUPIgBPmAz-3zeqpAbw2EdY6h09BVSfjc6TxvfSnlo7odI-1_Htd5RDT2JLhVDYO9MnrDwjw72Yi8HJzHNMpnvCzqkaipBRSRcj8t2uTjRoHqIV7IS2-VxquqkQackEk-f5O6Kep2-xWrY9AEQ9qVfcU7jqjlWWEoI3fDxDOV-GIgewiDj52LARFw_9UufdE4mCDqmALiUH26fofa7qmovjE-jnvYauecmmQyX6dZrk9BvYL3hF5ORoG5zSygfJirbvN76-siag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 477K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 03:20:11</div>
<hr>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXrBTLZdcgs_VA6SajtlWWqHBS2ayT7LegLiRn3I6yo7uBFn_KMwhyyzMUNW6364tGkom33Ud-SOSBlxqIXzc6S_N50WGqzr4i8ROxXBgYWreEOqf37J6vAK_R0mUEqfgm2YITygsqfBsBJB3cCdXfOFdwmMhI_Z-vZCr9L68tG2Mx7U9XgkEzZdqYee0OZPOybUDiEetBGFQHRYQC4eX4_xSFkP7L1dpVwCOAua1VTDlxehHB4UHseaspR4DB-R1PKHcFHLuoimh81Z1NlCei7gohKw5WDuGyjuAgzvenH8eY1RXsvoRCfI1r6ZN7sL85-XB9K6lAmR3vRsk0difQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی و هیئت اعزامی بالاخره از نیویورک دل کندن و بعد از توقفی در دوحه قطر به تهران بازگشتند. همچنین شش سوخترسان در منطقه تنگه هرمز و خلیج فارس فعال هستند و یک پی-۸ پوسایدن در دریای مکران فعالیت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/withyashar/24519" target="_blank">📅 03:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آکسیوس: احتمال شروع جنگ بسیار بالاست
آکسیوس به نقل از مقامات آمریکایی: ممکن است ترامپ پس از انتخابات دستور بازگشت به عملیات رزمی گسترده علیه ایران را بدهد.‌‌
ایرانی ها اعلام کردند تا زمانی که واشنگتن با بازگشت به یادداشت تفاهم موافقت نکند، امتیازی نخواهند داد.‌‌
هیچ پیشرفت محسوسی در مذاکرات روز دوشنبه حاصل نشد و ایرانی‌ها چیزهایی را طلب می‌کنند که واشنگتن نمی‌تواند آنها را بپذیرد.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/withyashar/24518" target="_blank">📅 03:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUB4C94S8GUO9RPZa4DmLgBY_IkB97YMQ5hqIcehOEGdj5G04TCI7zAifQ0K1i_3tKQti6MFKWPBm2a6rMGO83ePFp8B9-DNU1Tyx6yNvcj7YcAMU6jPD6bTVYfpfV-2c69Al0jkoJUeVTK0qtbf2A1YsZWV2OI8YoD4fmxPtCfRlHeoXoJ4pMy43KqNx_K-WZw5A-kRDAMAmCE3Eog7L2Mx_oeUniP3b4y2o4zUgZkE9OziPS1ZUjCqDM84VEf2Hxo2-EojHCmY10wCqb8EbMSsuGsPLu5QLY8Ao1GLbNFAu3tcdq_1XrlaZy4k2_54exK_GtFmEaMbM2DcnD5K-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا در چارچوب برنامه «پاداش برای عدالت»، برای دریافت اطلاعات درباره
احمد فرهادی، عبدالله محرابی و علی‌اصغر نوروزی
، از مقام‌های نیروی هوافضای سپاه پاسداران،
تا ۱۵ میلیون دلار پاداش
تعیین کرد. این افراد در توسعه موشک‌ها و پهپادهای ایرانی و تأمین مالی و تجهیزات سپاه نقش دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/withyashar/24517" target="_blank">📅 02:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5adfdf90.mp4?token=IMD4MGGXF3MaetpcTKLZ3MInhZUy-WpzheXVG4tBW_oY4pWLkBBRvGyGFruPI3TxBipJxXfqYF0cYTdEryhKkPTI1wNMH4LJ-iCWcnl2AuiUuDVHpP9NaJzLy7AZ7JdLuQQuW1k32nvrpWAuTbhx2569a-iRMg8tGfEplobK_zBFbBPiF4vX_tCfj59jPZyke_XoAza8wLKjT7UI3TT2MTVyYlk-KCfeVXus6Qwhvz6ibzPdqZxmTy2-1v0NAyLecgj5NVXRTfiCQgir5nioVGN4O3xG5VBij3Z8NY_9PiUZno9_ZG1965Kd5Eq-XYqsPjyCFwnM-J-SYXcrDuRZYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5adfdf90.mp4?token=IMD4MGGXF3MaetpcTKLZ3MInhZUy-WpzheXVG4tBW_oY4pWLkBBRvGyGFruPI3TxBipJxXfqYF0cYTdEryhKkPTI1wNMH4LJ-iCWcnl2AuiUuDVHpP9NaJzLy7AZ7JdLuQQuW1k32nvrpWAuTbhx2569a-iRMg8tGfEplobK_zBFbBPiF4vX_tCfj59jPZyke_XoAza8wLKjT7UI3TT2MTVyYlk-KCfeVXus6Qwhvz6ibzPdqZxmTy2-1v0NAyLecgj5NVXRTfiCQgir5nioVGN4O3xG5VBij3Z8NY_9PiUZno9_ZG1965Kd5Eq-XYqsPjyCFwnM-J-SYXcrDuRZYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی مجلس نمایندگان آمریکا، مایک جانسون:
سناریوی وحشتناک این است که، خدا ناخواسته، دموکرات‌ها کنترل مجلس را به دست بگیرند. آن‌ها هر کمیته‌ای از کنگره را به یک نهاد بازرسی تبدیل خواهند کرد.
آن‌ها در تمام طول روز، هر روز و هر ساعت، به جای انجام کار، فقط به دنبال حمله به رئیس‌جمهور، خانواده‌اش، اعضای کابینه، حامیان مالی حزب، چهره‌های برجسته در بخش‌های تجارت و صنعت خواهند بود.
@WarRoom</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/withyashar/24516" target="_blank">📅 01:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مارک لوین : آماده باشید، سوپرایز در راهه
@WarRoom</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/24515" target="_blank">📅 00:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/042e52e439.mp4?token=MedopXZWwJFZ6NqES3vM6eUDGkOJ5jMGW2HDhVCikh_S33dNEVhYvLQwAYt8O_Y9kroA-kIC1_VjiNIW89qef43OEQGrwEllcSIJIvQ0k_VySiM8zLID1mTIpK6x5M1DFCVLdXsI-nK8o2-KeGvmiqyxscjlfxCqf8M0bv6qO_mAQcV5hBmp-a8cwuLNYwNYhIG1PtKuehMzXMmvtFj--oHaieSPUSFdya26i0c0vYPwMLCVyZY1CfN5pQl5dC7geHdpW9yQ6KIn02aoXEZcH74DbH3U0yEnz6JGwoo_iJGhEvrbJ4s12X_PSEtN_5OTklFDukoVamXbYfLgVdnQHZeJkyrgTDyA2rE-TRXnIKbMeDuBxlafEtQM-4JxkU5KzJ9vMUF3jWuBRYzudN6i63-zIi_cGEgJWVJHyANqSvPQxDEnghmRpBurPTOJK12m_DGKClRhz1-Sshq1dsEwtQ8Td5_fECPeAzmKzNkTwrmA2SS8kN72FCcEFcBDXW_IdjOnvlDt7f8t3vhfol0Li82rSE2ZENMJ-vE23vMTb25BaJ1cdS-dyz-jB4lsMg1nIVTkPYVt1Dh1etKxute-t1aNN4R6SnPP983g4qqoGhGcJGzjO2qeWrNmljiefu7tYY0RKy56TgimhudYoHzIK58WZbJIpLFLf1zSIwTchuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/042e52e439.mp4?token=MedopXZWwJFZ6NqES3vM6eUDGkOJ5jMGW2HDhVCikh_S33dNEVhYvLQwAYt8O_Y9kroA-kIC1_VjiNIW89qef43OEQGrwEllcSIJIvQ0k_VySiM8zLID1mTIpK6x5M1DFCVLdXsI-nK8o2-KeGvmiqyxscjlfxCqf8M0bv6qO_mAQcV5hBmp-a8cwuLNYwNYhIG1PtKuehMzXMmvtFj--oHaieSPUSFdya26i0c0vYPwMLCVyZY1CfN5pQl5dC7geHdpW9yQ6KIn02aoXEZcH74DbH3U0yEnz6JGwoo_iJGhEvrbJ4s12X_PSEtN_5OTklFDukoVamXbYfLgVdnQHZeJkyrgTDyA2rE-TRXnIKbMeDuBxlafEtQM-4JxkU5KzJ9vMUF3jWuBRYzudN6i63-zIi_cGEgJWVJHyANqSvPQxDEnghmRpBurPTOJK12m_DGKClRhz1-Sshq1dsEwtQ8Td5_fECPeAzmKzNkTwrmA2SS8kN72FCcEFcBDXW_IdjOnvlDt7f8t3vhfol0Li82rSE2ZENMJ-vE23vMTb25BaJ1cdS-dyz-jB4lsMg1nIVTkPYVt1Dh1etKxute-t1aNN4R6SnPP983g4qqoGhGcJGzjO2qeWrNmljiefu7tYY0RKy56TgimhudYoHzIK58WZbJIpLFLf1zSIwTchuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید ایران نمی‌تواند سلاح هسته‌ای داشته باشد. چرا؟ کره شمالی می‌تواند سلاح هسته‌ای داشته باشد؟
ترامپ: «آه، چون شما رئیس‌جمهور متفاوتی داشتید!!!
کیم جونگ اون
. او دوست من است. ترامپ را دوست دارد و من هم او را دوست دارم. تا زمانی که من اینجا هستم، او در امان خواهد بود. می‌دانید چرا؟
چون برای من احترام قائل است.
»
@WarRoom</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/24514" target="_blank">📅 00:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24513">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a35cfdae.mp4?token=ptfS9tHhb6eFvR65Nsk3uptip1vAah-QapvwvBOu1f-mZodJCWk9WI05Vkdkcv3JM7bA7sxgPwrN8GcUByflJLY9d1nAZGqmrLlMsAmBMnWnzq_zV8NVdmcWR8yVnhWQgmmsS8_Sf3ge66nHR2hSMJPlbdBQVA-YhmcG3H-A04IuE9SNZklmBKKxAPu3vOjPs16OX9FbnLOyJysrc1AsZyFSj3Z5tb8bLQRcLZxZDGR2oGCCB_LK94JFfBvIgbbdbJIUhKIRXna5l_kc875mCDim3ItnviMzDUZPi8AsxIRzQbFKC6Phdl7rF186l7ckOM2XP1Ur-BwE16cy3RcMfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a35cfdae.mp4?token=ptfS9tHhb6eFvR65Nsk3uptip1vAah-QapvwvBOu1f-mZodJCWk9WI05Vkdkcv3JM7bA7sxgPwrN8GcUByflJLY9d1nAZGqmrLlMsAmBMnWnzq_zV8NVdmcWR8yVnhWQgmmsS8_Sf3ge66nHR2hSMJPlbdBQVA-YhmcG3H-A04IuE9SNZklmBKKxAPu3vOjPs16OX9FbnLOyJysrc1AsZyFSj3Z5tb8bLQRcLZxZDGR2oGCCB_LK94JFfBvIgbbdbJIUhKIRXna5l_kc875mCDim3ItnviMzDUZPi8AsxIRzQbFKC6Phdl7rF186l7ckOM2XP1Ur-BwE16cy3RcMfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران و تنگه هرمز: «ما طی دو روز گذشته
بیش از هر زمان دیگری در تاریخ، نفت را از تنگه هرمز خارج کرده‌ایم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/24513" target="_blank">📅 23:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431a4ea541.mp4?token=VSXXmgQLN8JktCx34a4Dk7BNp_isdnAic3P6uumKowuYthxPiWUvo9av_LODTRbXbb51SpWZqsNOjWyQj0_xuXOYVjOyA1_URFQckNftXsBQx8XtALr4b-qb7_BFAoaWIPlv4yLvV1xRKu5VkCmsSvx_3vMy-IadPMYsvn7-zp9wxawhhShzHQWQZUqAbs1hzbbb-SdC-ZCnJx8pevcpHTVXD3zT3obl7s_iuwKvmnoepkeakjVYCjN8wGB4jdDcFBJ1vDxXP1drpld748yNZEQEeYk6l3cWsEPWn6otgm7xxPk3R7vP7xDpAKk99KscV1ykK21MfrazyDywu35cBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431a4ea541.mp4?token=VSXXmgQLN8JktCx34a4Dk7BNp_isdnAic3P6uumKowuYthxPiWUvo9av_LODTRbXbb51SpWZqsNOjWyQj0_xuXOYVjOyA1_URFQckNftXsBQx8XtALr4b-qb7_BFAoaWIPlv4yLvV1xRKu5VkCmsSvx_3vMy-IadPMYsvn7-zp9wxawhhShzHQWQZUqAbs1hzbbb-SdC-ZCnJx8pevcpHTVXD3zT3obl7s_iuwKvmnoepkeakjVYCjN8wGB4jdDcFBJ1vDxXP1drpld748yNZEQEeYk6l3cWsEPWn6otgm7xxPk3R7vP7xDpAKk99KscV1ykK21MfrazyDywu35cBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران: «نمی‌دانم هنوز قرار است تسلیم شوند یا نه، اما
تسلیم خواهند شد. آنها وضعیت بسیار بدی دارند.
»
@WarRoom</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/24512" target="_blank">📅 23:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8KHtEZyUV9MQd52FazNMytWvOoXn9GTZSyhWUw_ExGc54XpgauQ2Ya_KbHrR5V335MysM4hz_TMi7CWGFGqjPLfd_X28zg9GRL9c0wzw29qtkPb7i6hnAJpTK8jhJ_e8twyy95STJINy0Y4-Tf-QV_08cNyUoeinsDMoznPcuNEZxdgYBGd1_3bTZnmjiCYu2qygSbe0P_lWETXVV2vk5esUqYiyQ0CRfd5moNosA6X0MNtYauPxP1BIy_xBjerZ4kVBiyMGaHacWMqU1ZXtabh7OVepjehOw0_lmwUxQY2WfkaU0LCxO0oecyfmXPDP9rhOwYnRv7wVF2eZUfV5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ سوخترسان و یک پی۸ پوسایدون در حال انجام مأموریت در تنگه هرمز و خلیج فارس
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/24511" target="_blank">📅 23:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24510">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTKr29zDypkEOnUqRt_auwBkZwoF0HMP00frVp3reoIytEIvZ6Y_rmNkqgzqJdcc3NHSNrqKQBwFP2Zalq-5zJmKv-oxI9nXnTzZlO4b48MfIStMYKpPYa_pDkA6poDZaG9SI1jSV_t6q1S_oITtmIhZ5sv8kUoA62YkjooVOPh-OBfnjNYgjjsSzZK-IOaYYVh60LG-ECmHQolrm1feakdCJhsYXJUwHctaqOlltxBALjNZx_pz52i9UZP5nO92aBfAdFzrf2LphwcNMGGTgK1SLTBT93G2cL_ZpRx4Iilavm3XOhyaCqu1wMmI577k-WqJRLBvUXH5ldaSya2YyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ اسرائیل
: اسرائیل برای جنگ بزرگ تر از ۴۰ روزه بمب سنگرشکن خریده است
@WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/24510" target="_blank">📅 23:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دلار ۲۵۶،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24509" target="_blank">📅 22:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55c30c663.mp4?token=YT7ZdJMoeXkmGmwr5LAJyBPXLD7LTWeXqLD2DVEWcXvemlPZPQcfRx3Vg1LUvB13ttVBVAryIs14j_pMSYtAMBuOdcNWXhJBuKdOTeOqfh_OwI78AQ0dgIBSw9_gAQKx3dbF5g794gXTSMqFPCozjuK7fgAyEvSJvo1xgi-orMl4ZQGRLzGdGbMXjr-WYsbzAVA7TgVvJwnU2oYoh1HL55fjDZTzH-a63aYzM3C0lXfHpwkDxyswj2LwL4pHfntSRPUFQx242db7DvK2ar6qLpEfNx88v6H-HBWFVGuUGY27qtlLCbyvxoVGFbFEmmO0AwgBmKi5sXJZZY9KTf6EjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55c30c663.mp4?token=YT7ZdJMoeXkmGmwr5LAJyBPXLD7LTWeXqLD2DVEWcXvemlPZPQcfRx3Vg1LUvB13ttVBVAryIs14j_pMSYtAMBuOdcNWXhJBuKdOTeOqfh_OwI78AQ0dgIBSw9_gAQKx3dbF5g794gXTSMqFPCozjuK7fgAyEvSJvo1xgi-orMl4ZQGRLzGdGbMXjr-WYsbzAVA7TgVvJwnU2oYoh1HL55fjDZTzH-a63aYzM3C0lXfHpwkDxyswj2LwL4pHfntSRPUFQx242db7DvK2ar6qLpEfNx88v6H-HBWFVGuUGY27qtlLCbyvxoVGFbFEmmO0AwgBmKi5sXJZZY9KTf6EjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار: دونالد ترامپ، رئیس‌جمهور آمریکا با انتشار این عکس از ، میزبانی نشست ناهار با مدیران ارشد فناوری و هوش مصنوعی در کاخ سفید و محل نشستن آنها خبر داد.در این نشست چهره‌هایی مانند ایلان ماسک (تسلا و اسپیس‌ایکس)، مارک زاکربرگ (متا)، جف بزوس (آمازون)،…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24508" target="_blank">📅 22:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اتاق جنگ با یاشار : انتخابات پارلمانی اسرائیل
۵ آبان
برگزار می‌شود. بر اساس آخرین نظرسنجی کان منتشرشده در امروز ،
حزب «یاشار»
به رهبری گادی آیزنکوت با
۲۳ کرسی
بزرگ‌ترین حزب است، پس از آن لیکود به رهبری بنیامین نتانیاهو با
۲۱ کرسی
و حزب نفتالی بنت با
۱۱ کرسی
قرار دارند. در مجموع، دو اردوگاه اصلی هرکدام حدود
۵۲ کرسی
دارند و هیچ‌کدام به حدنصاب
۶۱ کرسی
برای تشکیل دولت نمی‌رسند. در سنجش انتخاب نخست‌وزیر نیز نتانیاهو با
۳۹ درصد
تنها یک درصد از آیزنکوت جلوتر است.
جمع‌بندی: یاشار فعلاً بزرگ‌ترین حزب است، اما در رقابت برای تشکیل دولت، نتانیاهو و مخالفانش تقریباً برابرند و هنوز برنده مشخصی وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24507" target="_blank">📅 22:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اتاق جنگ با یاشار : انتخابات میان‌دوره‌ای کنگره آمریکا
۱۲ آبان ۱۴۰۵
برگزار می‌شود. آخرین نظرسنجی‌ها تا امروز نشان می‌دهد فعلاً
دموکرات‌ها دست بالا را دارند
؛ در نظرسنجی‌های ملی، دموکرات‌ها حدود
۷ تا ۱۴ درصد
از جمهوری‌خواهان جلوتر هستند. این برتری می‌تواند برای پس گرفتن مجلس نمایندگان کافی باشد. در مجلس سنا اما رقابت نزدیک‌تر است؛ جمهوری‌خواهان اکنون
۵۳ کرسی
و دموکرات‌ها
۴۷ کرسی
دارند و دموکرات‌ها برای رسیدن به اکثریت به کسب چهار کرسی بیشتر نیاز دارند. ایالت‌هایی مانند
تگزاس، اوهایو، آیووا، آلاسکا، مین و کارولینای شمالی
از مهم‌ترین میدان‌های تعیین‌کننده هستند. جمع‌بندی فعلی:
دموکرات‌ها در رقابت مجلس نمایندگان موقعیت بهتری دارند، اما کنترل سنا همچنان کاملاً رقابتی است و نتیجه نهایی مشخص نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24506" target="_blank">📅 22:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کانال ۱۵ اسرائیل : صدای اعتراضات در ایران بلندتر شده و حاکمان خواستار اقدام تهاجمی پیشدستانه به دلیل وضعیت وخیم کشور هستند؛ مقامات افراطی در ایران گفتند : "انجام حمله پیشدستانه علیه آمریکا و متحدانش ، بهتر از تحمل وضعیت فعلی است."
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24505" target="_blank">📅 21:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda61c2c14.mp4?token=aB4z8ZWzmvrMGL0FhXXUWKIGxNDQtizhSsSMPAO4VXoq0ZjUI-2s42Kyk9x3nhb8dxLj5JQw4jwZFBpSvENyBFY-HfU45MTwhY0CCOQg6hlcCnOgJuemGLF-iarHe4JgFhcMNA9aSYw360fVHzV60FffTnw51inuSfZxAAW6hPiZksLa2u17Y4PBIIpL2iV_RSgH6fQSZR6qMDZWVIsz2QhLUrZJGKHRMDlUQYFxnOzDmcZiKfSoUTIDiuZPUrnFrmCMRb9RFlbXPnC-vCJV7hgP0R77Su3aNx8rb4QdT_YWVQh10oX_PMqdiRosVYRo7Bd4IzERCFySgMi4OPshEG3mvLJ7mHaD8pMPmiBVGrdWJkWOWqoPNGB1ytry8lbADsUv-dwjFW3eyoyEaPq9e3-mSPNN-uM57zndTzcSyj2vdbZqMc8I66f8QIUildzdAUgJuLx5mSOA3Ndakny8NEeHGXwe1NMydAEYw4ojXX34Bt9EaM5NiiB1LKCrGkNuE48l0oQyEgXYLYCf79y24yIWafZL_9lpbqtUgLN3T0TqzhD8UYw5y243MIttINk11xE6oN3Y4oCQAq2Mm37WPwBZ8p75KmCB6lEPRUhBkiL14v57hRSLP89Oly0QwpShwkjPlbvKy_tUZh_YquUInf9kMGFtIePQGQI8c6T-Hpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda61c2c14.mp4?token=aB4z8ZWzmvrMGL0FhXXUWKIGxNDQtizhSsSMPAO4VXoq0ZjUI-2s42Kyk9x3nhb8dxLj5JQw4jwZFBpSvENyBFY-HfU45MTwhY0CCOQg6hlcCnOgJuemGLF-iarHe4JgFhcMNA9aSYw360fVHzV60FffTnw51inuSfZxAAW6hPiZksLa2u17Y4PBIIpL2iV_RSgH6fQSZR6qMDZWVIsz2QhLUrZJGKHRMDlUQYFxnOzDmcZiKfSoUTIDiuZPUrnFrmCMRb9RFlbXPnC-vCJV7hgP0R77Su3aNx8rb4QdT_YWVQh10oX_PMqdiRosVYRo7Bd4IzERCFySgMi4OPshEG3mvLJ7mHaD8pMPmiBVGrdWJkWOWqoPNGB1ytry8lbADsUv-dwjFW3eyoyEaPq9e3-mSPNN-uM57zndTzcSyj2vdbZqMc8I66f8QIUildzdAUgJuLx5mSOA3Ndakny8NEeHGXwe1NMydAEYw4ojXX34Bt9EaM5NiiB1LKCrGkNuE48l0oQyEgXYLYCf79y24yIWafZL_9lpbqtUgLN3T0TqzhD8UYw5y243MIttINk11xE6oN3Y4oCQAq2Mm37WPwBZ8p75KmCB6lEPRUhBkiL14v57hRSLP89Oly0QwpShwkjPlbvKy_tUZh_YquUInf9kMGFtIePQGQI8c6T-Hpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر نخست‌وزیر قطر درباره جمهوري اسلامي:
ایران همسایه ما بوده و برای همیشه همسایه ما خواهد ماند. ما جایی نمی‌رویم. آن‌ها هم جایی نمی‌روند.
ما دهه‌ها رابطه بر پایه احترام متقابل با آن‌ها داشته‌ایم. همکاری‌ها به دلیل تحریم‌ها محدود بوده است، اما ما تمام تلاش خود را برای حفظ این رابطه همسایگی خوب به کار بستیم، هرچند در طول این دهه‌ها و در بسیاری از سیاست‌ها اختلافات زیادی داشتیم.
@WarRoom
اتاق جنگ با باشار : اگه موندین به خاطر همین رژیمه ! هم این رژیم میره هم شما میرید ! بماند به یادگار… به دل پاک بی بی قسم</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24504" target="_blank">📅 21:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزارت خارجه دانمارک:
دانمارک در تازه‌ترین توصیه سفر خود،
همچنان از تمام شهروندانش می‌خواهد به ایران سفر نکنند
و از دانمارکی‌های حاضر در ایران نیز می‌خواهد
کشور را ترک کنند
. وزارت خارجه دانمارک وضعیت امنیتی ایران را «بسیار پرخطر، ناپایدار و غیرقابل پیش‌بینی» توصیف کرده و هشدار داده که
راه‌های خروج از ایران ممکن است با اطلاع کوتاه‌مدت محدود یا کاملاً متوقف شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24503" target="_blank">📅 21:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24502">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا:
۱۰ فرد و نهاد مرتبط با شبکه تأمین تسلیحاتی
وزارت دفاع ایران
را تحریم کرد. اسامی افراد:
سید اصغر علیرضا‌زاده طباطبایی، علی فتوت احمدی، پریسا لالی، لی فِن و وسیم پاشا تاجمل
. نهادهای تحریم‌شده نیز
کاوشکام آسیا R&D، EC Mojo Technology، Cavalier Dynamics پاکستان، Cavalier Dynamics عربستان و Cavalier Dynamics ترکیه
هستند. به گفته آمریکا، این شبکه در تأمین
قطعات الکترونیکی، تجهیزات دوکاربردی، موشکی و پهپادی
برای ایران نقش داشته است. تحریم‌ها دارایی‌های این افراد و شرکت‌ها در حوزه صلاحیت آمریکا را مسدود می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24502" target="_blank">📅 21:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24501">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سخنگوی فرمانده کل نیروهای مسلح عراق : نیروهای آمریکایی به کشور خود و پایگاه‌های کشورهای همسایه بازگشتند، پس از دستیابی به توافقات. مأموریت ائتلاف فردا به طور رسمی به پایان می‌رسد, ائتلاف فردا خروج خود از کردستان عراق را نیز به پایان خواهد رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24501" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال i24 عبری با استناد به منابع اطلاعاتی آمریکایی گزارش داد:
«ایالات متحده، نتانیاهو را در ارزیابی خود در مورد احتمال وقوع حمله به اسرائیل، سهیم می‌داند.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24500" target="_blank">📅 20:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks2DoT6fTDShcU4KO6DIcG6uxYLqGtpPvtdc5Kfs894v_AQKDZdTWdg9wxGWuArxb7erhSI3Xz66IEPnx8jQahsbGlaYDFiQnUx2hYB7U3CEK0S0rT9Aa8rH0Mqh6W8omx06sdPgjfsPDIyuJ7gUGXOvMEKZqK4SmhvfwZQPo8982qGu6eFNOeMlyOB3y4wvVcrc3tdtKv1TBa1Uy--7zzCougruJJxLalTDuLv2TByHiv-RLMCzKlSkrct7i6Xl1pY68phyKTCzsrDfb_tSdi5umJB1p_C7dux0qf6gRSZ5AAHWB4t2aQEkLGadC3eJfwsRMazoUR0l6nJXsRjwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بمب‌افکن B-1B لنسر از فرودگاه پر حاشیه فیرفورد که مورد حملات احتمالی تروریستی جمهوری اسلامی قرار گرفت،  بلند شده و مشغول پرواز تمرینی و تمرین سوخگیری هوایی است. شکی نیست که این از آخرین پروازهای تمرینی قبل از حملهٔ اصلی به ایران است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24499" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24498">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">از قشم پهپاد پرتاب شد به سمت تنگه و موشک کروز نیست اینبار
@WarRokm
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24498" target="_blank">📅 20:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24497">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXcb5qjIPa6pOc8WlPA-kRujh7V91svFgK5Gakn4bRJcdpzzkFCakfEw225El2T55cHAvhlFeQqM9bSLXQFT9BrxLaUfxbKLCelahjXbTam1ilFWm7GzMKcD1sfDvQ-8IVrohlC_W4qz-QVMoXeM4mcKetdR3doHUNMeHeOKIrC4IP_L9J5mzHX4tZzaX7nhxv-ZfJDu6VIxbVbmeL3IpixwX2rjjUFAFJl9V0AkR3i6elAXH3KImiSU0lN4I5MYIedBVDWheut5Dr31Ue-NR9vvFA3QQDplD7NsY_o6_oXLwmPAeFY61im-Ne2vnnfzWHC_5NRhAzxaWCdDxOD_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار: دونالد ترامپ، رئیس‌جمهور آمریکا با انتشار این عکس از ، میزبانی نشست ناهار با مدیران ارشد فناوری و هوش مصنوعی در کاخ سفید و محل نشستن آنها خبر داد.در این نشست چهره‌هایی مانند ایلان ماسک (تسلا و اسپیس‌ایکس)، مارک زاکربرگ (متا)، جف بزوس (آمازون)، جنسن هوانگ (انویدیا)، سم آلتمن (OpenAI) و داریو آمودی (آنتروپیک) حضور دارند.موضوع نشست، آینده هوش مصنوعی، رقابت فناوری آمریکا و چین و امنیت و مقررات این فناوری است. حضور هم‌زمان مدیران بزرگ‌ترین شرکت‌های فناوری آمریکا، این جلسه را به یکی از گردهمایی‌های مهم اقتصادی و فناوری دولت ترامپ تبدیل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24497" target="_blank">📅 19:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07f7a9d90f.mp4?token=kiYt3P4bAzeXpWHKMHpCs59aJForsc85z3-PEDpiAfoiAUrjB3B4vN_lILEGhrKgQLSEoLbhHGcodTskOfgN823Kn7nHt9ttcGFS4VQMGJET2FfPmRzy4wbGnV2gzzx5CiBDvv5lAOwyTfhpowUK_W2Vhaa0MtZ6VBQ-Q14_fhbRChbMC_JwBUMRbApk5qGST-t5NT4B02yD6DynXCJZe3vgONh7Phsb_X3UvrJ30CQR4XIZuZtdZxzM1Z77oAUGEhWKaHQV68_T8NSFTAiQvZljTNEdtDhGh0JiUiV8_KyZXKuB9-thbQiZTenpmcOUsW1dPoCEn-9R4eQVvQkWOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07f7a9d90f.mp4?token=kiYt3P4bAzeXpWHKMHpCs59aJForsc85z3-PEDpiAfoiAUrjB3B4vN_lILEGhrKgQLSEoLbhHGcodTskOfgN823Kn7nHt9ttcGFS4VQMGJET2FfPmRzy4wbGnV2gzzx5CiBDvv5lAOwyTfhpowUK_W2Vhaa0MtZ6VBQ-Q14_fhbRChbMC_JwBUMRbApk5qGST-t5NT4B02yD6DynXCJZe3vgONh7Phsb_X3UvrJ30CQR4XIZuZtdZxzM1Z77oAUGEhWKaHQV68_T8NSFTAiQvZljTNEdtDhGh0JiUiV8_KyZXKuB9-thbQiZTenpmcOUsW1dPoCEn-9R4eQVvQkWOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی وا
l
نس، معاون ترامپ، درباره جمهوري اسلامي:
فکر می‌کنم [مقامات] ایرانی‌ها درک کرده‌اند که اشتباه کرده‌اند و با ما توافق امضا کرده‌اند. آتش‌بس داشتیم. قیمت‌های انرژی کاهش یافته بود. و امکان وجود داشت که اگر ایرانی‌ها رفتار مناسبی داشته باشند، از یک رابطه بهتر با ایالات متحده بهره‌مندی زیادی کسب کنند.خب، چه اتفاقی افتاد؟ آن‌ها رفتار مناسبی نداشتند. شروع به شلیک به کشتی‌های تجاری کردند. اکنون، ما می‌دانیم، زیرا اطلاعات بسیار خوبی داریم، که بسیاری از مقامات درون سیستم ایرانی نمی‌خواستند این اتفاق بیفتد.آن‌ها فکر می‌کردند احمقانه است که تندروها دوباره شروع به شلیک به کشتی‌ها کنند. اما این کار را کردند. و نتوانستند آن تندروها را کنترل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24496" target="_blank">📅 19:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597407c8b0.mp4?token=c4Dg8ZUJ4BEg2Bs3CFrTfnbS9gS6mp0fi06qui70l9m9BZhKbWm3qNfzEnaYZ9Kg5jCggAeddc1TMdunPJXWyU3M4qM7O4aI1HXpT2IRGw_UQ64CVerm8IB-mlfH5AKr0L4XScHUwONsliGpkBM7ZK06LPcCH8KMOkNSWxNZApeneaoobEKQBUIYDReqS7YREHEWW5Ps_P4udKpzhilldpZcA8auNLKxMXKzzjSMi42u5srU_ZPaqG6uiWycxE0Jy3Dahc7ml2gjQY2QE1qTRSr29cv5s4BM7Nv-G8lLGhV8pbU359gLSFQnNiLd_DGW6sgJkPMUWVXefBHCmxW3IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597407c8b0.mp4?token=c4Dg8ZUJ4BEg2Bs3CFrTfnbS9gS6mp0fi06qui70l9m9BZhKbWm3qNfzEnaYZ9Kg5jCggAeddc1TMdunPJXWyU3M4qM7O4aI1HXpT2IRGw_UQ64CVerm8IB-mlfH5AKr0L4XScHUwONsliGpkBM7ZK06LPcCH8KMOkNSWxNZApeneaoobEKQBUIYDReqS7YREHEWW5Ps_P4udKpzhilldpZcA8auNLKxMXKzzjSMi42u5srU_ZPaqG6uiWycxE0Jy3Dahc7ml2gjQY2QE1qTRSr29cv5s4BM7Nv-G8lLGhV8pbU359gLSFQnNiLd_DGW6sgJkPMUWVXefBHCmxW3IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ، درباره جمهوري اسلامي ایران:
جهانی وجود دارد که در آن می‌توانیم با تهران توافق کنیم. اما این امر نیازمند آن است که مقامات ایران رفتار مناسبی داشته باشند. این امر نیازمند آن است که مقامات ایران به تعهدات خود در قبال ایالات متحده پایبند باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24495" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b80bc12f2.mp4?token=UeCtkE3YSZrn4idVip4q_Bcurti09B1sQm_9czO3eu1E9bUil4EdfWR2dayszHgkxuKVRiL7CYWr0sZI3ISVA_tniTkDAlSIPOwkGMa_zBkRHO_aqYqBeCpXVTsD7hDEFZIDuG8uaYZJ0gsJrc5a8AkaI-VqtQH_kE7YImLh3ZOzvULdQMJp9xnVFONEuTa8nVmGUWxxJDQ6rdQk2pgfUEhAmm-prx4NMV5ZPiAEVIo2nBCz8yW0pmkQp2OjjgNk0lDptCL_xrP-xWQEBTwnvqyKREGx0UoDM4eR63LDh6Ed7tZ4VVZeEDAFer6jlK-Ttfczl8aqvj13_mE5rR1azg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b80bc12f2.mp4?token=UeCtkE3YSZrn4idVip4q_Bcurti09B1sQm_9czO3eu1E9bUil4EdfWR2dayszHgkxuKVRiL7CYWr0sZI3ISVA_tniTkDAlSIPOwkGMa_zBkRHO_aqYqBeCpXVTsD7hDEFZIDuG8uaYZJ0gsJrc5a8AkaI-VqtQH_kE7YImLh3ZOzvULdQMJp9xnVFONEuTa8nVmGUWxxJDQ6rdQk2pgfUEhAmm-prx4NMV5ZPiAEVIo2nBCz8yW0pmkQp2OjjgNk0lDptCL_xrP-xWQEBTwnvqyKREGx0UoDM4eR63LDh6Ed7tZ4VVZeEDAFer6jlK-Ttfczl8aqvj13_mE5rR1azg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا: ما معتقدیم رهبر جمهوری اسلامی ایران زنده است. برای اینکه هرگونه توافقی میان آمریکا و ایران امکان‌پذیر باشد، ایران باید رفتارش را تغییر دهد و به تعهدات موردنظر آمریکا عمل کند. @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24494" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8091040c3.mp4?token=lQlbcB5tyR9NzdCiIjFbCoZ0mtH_DgiXoSN97RLEYT702YC9OUl1dYq4-DbqkgHzVYumS3MYLnBHNN-ZglqAgwfL9lrHBwJ5oaiLUnLosUBquuQHCzmhKtlU98Nb4gg0WUuW5tqO-NetQMSB25Eg6XLnvuJpLTrOE-4O9aYYESKgdpJZxLpt6hTyLndf8VXQohnXnXdwgUHwj4ySxvvTNYJ-CusqDZf1Me-Dbgq13T-QoHuACdGOqnY_KZbyVrmog7oEUoCGLrVGFc9NvUpd4zoGat8-CuiH0j7HB-LpMqc_iN5X55C2dKuUuoX4gNvktGnuR-j4fryax5zfYYFTKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8091040c3.mp4?token=lQlbcB5tyR9NzdCiIjFbCoZ0mtH_DgiXoSN97RLEYT702YC9OUl1dYq4-DbqkgHzVYumS3MYLnBHNN-ZglqAgwfL9lrHBwJ5oaiLUnLosUBquuQHCzmhKtlU98Nb4gg0WUuW5tqO-NetQMSB25Eg6XLnvuJpLTrOE-4O9aYYESKgdpJZxLpt6hTyLndf8VXQohnXnXdwgUHwj4ySxvvTNYJ-CusqDZf1Me-Dbgq13T-QoHuACdGOqnY_KZbyVrmog7oEUoCGLrVGFc9NvUpd4zoGat8-CuiH0j7HB-LpMqc_iN5X55C2dKuUuoX4gNvktGnuR-j4fryax5zfYYFTKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
در سال‌های پیش رو، آن‌ها تاریخ کشور ما را خواهند نوشت و خواهند گفت که جنگ ایران یکی از مهم‌ترین کارهایی است که ما انجام دادیم.این در واقع یکی از مهم‌ترین کارهایی است که ما انجام داده‌ایم.</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24493" target="_blank">📅 19:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fe3fdc3bf.mp4?token=lu5rPxK34c7agHVueRZKfa_NkR_XxUbPc458QzqsnYniaTwYSXVQ_LC5hqeEDLprJl0aLcsuWZ8kOafVMYTiV4kZ8CQ53M3C31CsPp1JAt9PhlEzPKyrV1-2iIP_g6LMfBTeePyAc-0XSdiDFgtrDdN1FYQJhkrRabyQEwhL-epvuvGkYxLg5yyVzFokcCEHw_f6vER6pFjMEqtUxAL373C50rfJuRlXHIKrsZFNfL42ReLn9h-RjOcfioXPFeg5R6U-_qJunLoIw5p4OswWk7bYvc0rmIdAkeDONvqsIlG3kio9Ss9PbWG1NHgVH7A_jBTzmmqKydTDjlUnXKJaTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fe3fdc3bf.mp4?token=lu5rPxK34c7agHVueRZKfa_NkR_XxUbPc458QzqsnYniaTwYSXVQ_LC5hqeEDLprJl0aLcsuWZ8kOafVMYTiV4kZ8CQ53M3C31CsPp1JAt9PhlEzPKyrV1-2iIP_g6LMfBTeePyAc-0XSdiDFgtrDdN1FYQJhkrRabyQEwhL-epvuvGkYxLg5yyVzFokcCEHw_f6vER6pFjMEqtUxAL373C50rfJuRlXHIKrsZFNfL42ReLn9h-RjOcfioXPFeg5R6U-_qJunLoIw5p4OswWk7bYvc0rmIdAkeDONvqsIlG3kio9Ss9PbWG1NHgVH7A_jBTzmmqKydTDjlUnXKJaTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران سلاح هسته‌ای نخواهد داشت، و آن‌ها خیلی بد، خیلی بد در حال شکست خوردن هستند. این ماجرا خیلی زود تمام می‌شود.خیلی، خیلی زود تمام می‌شود. آن‌ها سلاح هسته‌ای نخواهند داشت.قیمت نفت به‌شدت سقوط خواهد کرد، درست همان‌طور که قبلاً بود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24492" target="_blank">📅 19:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262002a591.mp4?token=SrAU954ZlJNCSoocTHDrw_v5tRw678TErNnfZ0LdRz2tc_R97G_osjs-m9EKDn8vzVovHfN21_ZyIh6mf2LXB_nN5AmpLh0t8UhWfLmflj1ph6YEqaCL7UwUrBa_BYlSVt3tBRSpStmUFN6qdTez9bq8WwSi-GKsw_9eI78Wie2eILe25PdQM7ZGLfTwVdwJ1DWFCn5HzmsppejnKYd0JYcumu-fzQsoyBKwb7ZRyQqP8ZWf0rWZefdxmgGDtkEW89Y0nSjAi78JpoyszKifRsob4S2W6YGlz0eCqc-PLZb3_ChSrDnk-yLPEdnBkQK-V8iTjYn-VT6PGXzzC-o74Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262002a591.mp4?token=SrAU954ZlJNCSoocTHDrw_v5tRw678TErNnfZ0LdRz2tc_R97G_osjs-m9EKDn8vzVovHfN21_ZyIh6mf2LXB_nN5AmpLh0t8UhWfLmflj1ph6YEqaCL7UwUrBa_BYlSVt3tBRSpStmUFN6qdTez9bq8WwSi-GKsw_9eI78Wie2eILe25PdQM7ZGLfTwVdwJ1DWFCn5HzmsppejnKYd0JYcumu-fzQsoyBKwb7ZRyQqP8ZWf0rWZefdxmgGDtkEW89Y0nSjAi78JpoyszKifRsob4S2W6YGlz0eCqc-PLZb3_ChSrDnk-yLPEdnBkQK-V8iTjYn-VT6PGXzzC-o74Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار ۲۵۵،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24491" target="_blank">📅 16:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14e804573.mp4?token=apCABodHK2wnxCzpDb-f9Xi6vP01oqr1ZXuuMKiS9tGGtLcYis-OQCHeCLgwIEh76nymyGc5EYbMYvsh9dK-YKua6YrC--kiP2_GZvs28NcqRbzPvmwyaX42TyJUqwbJBl6JvK4CmtRLr9CPX-2YJtK3zQ439YZ8XZ2gUCGYIjiuU2o1CEXO-2xYBx4raPb-WfuehI66Aup56242WIBQov6cwAC9V0n8aFtG95TRh_7m8_f8HS3usV2GtEUvIrudT0hxg6XmbBTyB7hRAl4ZT0OosPzJrvuKQr9VRwdDG5LE4nIWzAh-4SlXGF5pxgh2cKyYNkT0P01Ln0awvzYuyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14e804573.mp4?token=apCABodHK2wnxCzpDb-f9Xi6vP01oqr1ZXuuMKiS9tGGtLcYis-OQCHeCLgwIEh76nymyGc5EYbMYvsh9dK-YKua6YrC--kiP2_GZvs28NcqRbzPvmwyaX42TyJUqwbJBl6JvK4CmtRLr9CPX-2YJtK3zQ439YZ8XZ2gUCGYIjiuU2o1CEXO-2xYBx4raPb-WfuehI66Aup56242WIBQov6cwAC9V0n8aFtG95TRh_7m8_f8HS3usV2GtEUvIrudT0hxg6XmbBTyB7hRAl4ZT0OosPzJrvuKQr9VRwdDG5LE4nIWzAh-4SlXGF5pxgh2cKyYNkT0P01Ln0awvzYuyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آشنا نیست ؟ خودمم ندیده بودم !
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24490" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خبرگزاری آناتولی:
یک فروند هواپیمای
کاسپین ایرلاینز ایران
به شماره ثبت
EP-KPB
در فرودگاه استانبول به دلیل بدهی حدود
۳ میلیون یورویی
به یک شرکت خدمات هوانوردی ترکیه، توقیف و از پرواز به ایران بازماند. شرکت
ACM Temsil Gözetim
به دلیل طلب خود علیه کاسپین ایرلاینز اقدام قانونی کرده بود و پس از صدور حکم، وکلا و مأموران اجرای حکم در فرودگاه حاضر شدند. هواپیما که مسافران خود را سوار کرده و آماده پرواز به ایران بود، با دستور مأموران متوقف و
مسافران و خدمه از هواپیما پیاده و به ترمینال منتقل شدند
و سپس عملیات توقیف هواپیما انجام شد. روند حقوقی میان کاسپین ایرلاینز و شرکت طلبکار همچنان ادامه دارد. این هواپیما یک
بوئینگ ۷۳۷-۵۰۰
است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24489" target="_blank">📅 16:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
ما معتقدیم
رهبر جمهوری اسلامی ایران زنده است.
برای اینکه هرگونه توافقی میان آمریکا و ایران امکان‌پذیر باشد،
ایران باید رفتارش را تغییر دهد و به تعهدات موردنظر آمریکا عمل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24488" target="_blank">📅 15:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHfA00YCTByW373qyMDd1MYl97gbH53s24u6oGDJn1Hz1X9BvhLK8ZcZ8AHuGTtHiojFPTyJdLnrpvRZQJtUSfb5brudfR_YIOB3sk_AduoNgQoq3K_keGMBBOMdOi7jLO1UU-a6vGfkfCN5bM2rOQUk9oBR8hf0r7m80nak_TgJLUJB_eHeJML5DU_yd9V41iKcqQDo7eOhM4mst3U8MwcrIY63tJbvlflGKbKk3HxB_k7HdOYTKdIoGFvrHcVnhPxbrjajNAKoSFDwTK0lpFYxbHhhUFjRVzstq0zDLKC3wgm-iresUMf4YeW8m6yfq9IM7dECsnb-l0QHTOcpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان ۴۷ هاموی و ۵ کامیون از آمریکا دریافت کرد
ارتش لبنان در چارچوب برنامه‌های کمک نظامی آمریکا، ۴۷ خودروی هاموی و ۵ کامیون دریافت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24487" target="_blank">📅 15:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8fb30205.mp4?token=lcrRenkwNkX01Ly-4xwi-VAirP3bYnEjsCcMJRn19ckpEOBo9wmQCM1fiXHzFUzDDbusQH0Rqhe69WaWUtNqw0c_wslkOdEHdHtml68pOqn4RGMs5vBI5-swXZ0MCWoEfMQP-O8tGrb8NdkUTCHkMvGpAqrOFGWHcW6efwgEIJLzilby-Oq1CdR9q-JBOJFvp5UQfC8n09rOOeBkBGELu0vr6T1odaE9dtedITrl-4bS5q_hbDhf5YgJtYJ8a-fyTrJabZ7IBmoAkp1javo7-UQwdlbrLwjY-3hwxcbSO636dxg2IhjglD0yMTqQEcAYOy1sNiZp5yVLiiHnd8osYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8fb30205.mp4?token=lcrRenkwNkX01Ly-4xwi-VAirP3bYnEjsCcMJRn19ckpEOBo9wmQCM1fiXHzFUzDDbusQH0Rqhe69WaWUtNqw0c_wslkOdEHdHtml68pOqn4RGMs5vBI5-swXZ0MCWoEfMQP-O8tGrb8NdkUTCHkMvGpAqrOFGWHcW6efwgEIJLzilby-Oq1CdR9q-JBOJFvp5UQfC8n09rOOeBkBGELu0vr6T1odaE9dtedITrl-4bS5q_hbDhf5YgJtYJ8a-fyTrJabZ7IBmoAkp1javo7-UQwdlbrLwjY-3hwxcbSO636dxg2IhjglD0yMTqQEcAYOy1sNiZp5yVLiiHnd8osYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
دشمنان ما ممکن است پیش از انتخابات به اسرائیل حمله کنند.
در هفته‌های اخیر بیش از ۱۰۰ تروریست را فقط در غزه از بین برده‌ایم و در لبنان نیز به عملیات ادامه می‌دهیم. اجازه عقب‌نشینی از دستاوردهای نظامی را نمی‌دهم و به دشمنان هشدار می‌دهم که بازوی بلند اسرائیل هر جا و هر زمان به آن‌ها خواهد رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24486" target="_blank">📅 15:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا به دولت عراق اجازه می‌دهد پروازها بین عراق و ایران را تحت شرایط آمریکا انجام دهد:
. پروازها فقط از فرودگاه بین‌المللی نجف
. پروازها فقط به مدت یک ماه
. پروازها فقط از طریق هواپیمایی عراق
. باید اطلاعات تعداد مسافرانی که جابه‌جا می‌شوند، نام‌ها و شماره گذرنامه‌های آنها، و مبالغی که هواپیمایی عراق در ایران برای سوخت، تعمیر و نگهداری و سایر خدمات هزینه کرده است، در اختیار آمریکا قرار گیرد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24485" target="_blank">📅 15:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsw1l4S2rfGs_R-9n4BO1QdGNx4gl7hb3nzi_luEKA2u-N1R4FkJoSHk12pMeLCJVPkYVxre239JY1mZYm-BxW7WrDg_rOqD-b0c1cwvK0mK7jiHyRQ4tlHZQ5XzOh-Em5tkMntbSo0Q-EoHM6_lr5bnilPwuLKAOnvZBurQ9b_S-U4PnM9fG0DBhTvwjAJlmHOK7-50oxb2FhOzz09rHajWVMOvZ9Ez2k6fB5sI793xT7l59hD6CSJbzNCwdN4mMS-lV42ad-YQjglmcXRAq0fH_smBHtfnRfkDRUUlVtrKSr1zla3kFkaFgO_vpwFODLF0-wo8tL9MQpOxHacejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار دریایی UKMTO: طبق گزارش دریافتی، در ۲۸ سپتامبر یک کشتی در تنگه هرمز هدف پرتابه‌ای ناشناس قرار گرفته و دچار آتش‌سوزی شده است. آتش مهار شده و کشتی در حال حاضر در وضعیت اضطراری نیست. خدمه سالم هستند و گزارشی از خسارت زیست‌محیطی یا میزان خسارت وارده منتشر نشده است. از کشتی‌ها خواسته شده با احتیاط تردد کرده و هرگونه فعالیت مشکوک را به مقامات دریایی گزارش دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24484" target="_blank">📅 14:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فیلم جدید The Fix با بازی لیام نیسون (Liam Neeson)
، داستان عملیات مخفی برای خارج کردن «مریم رجوی»، دختر فریبا رجوی، از ایران را روایت می‌کند؛ که در ازای نجات دخترش، اطلاعاتی درباره شبکه مخفی آمریکا و وقایع سال ۱۹۷۹ ارائه می‌دهد. فیلم با نمایش اسناد محرمانه درباره
خمینی، دولت آمریکا و سیا
، روایتی جنجالی از ارتباطات پنهانی آمریکا در تحولات منتهی به انقلاب ۱۳۵۷ و سقوط شاه ارائه می‌کند و همچنین به
مجاهدین خلق (MEK)، باج‌گیری، خرابکاری و ارتباط با قدرت‌های خارجی
می‌پردازد
منابع معرفی فیلم نیز تأکید کرده‌اند که بر اساس یک داستان واقعی ساخته نشده است.  مجاهدین خلق  پول خرج کردن باز بیان تو هالیوود ؟!! باید فیلم را کامل دید…
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24483" target="_blank">📅 14:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24482">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دلار تتر ۲۵۲،۳۰۰ @Waratoom
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24482" target="_blank">📅 13:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دلار تتر ۲۵۲،۳۰۰
@Waratoom
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24481" target="_blank">📅 12:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وال‌استریت ژورنال:
یک گزارش مهم از کمیته تحقیقات سنای آمریکا می‌گوید
۸۴ درصد از ۸۴۶ کیف پول رمزارزی تحریم‌شده مرتبط با ایران، عمدتاً از USDT تتر استفاده کرده‌اند
. گزارش مدعی است این شبکه‌ها برای دور زدن تحریم‌ها، معاملات نفتی و تأمین مالی شبکه‌های وابسته به ایران استفاده شده‌اند. موضوع برای بررسی بیشتر به وزارت خزانه‌داری و دادگستری آمریکا ارجاع شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24480" target="_blank">📅 12:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد
عزالدین البیک، فرمانده تیپ شمال غزه در گردان‌های عزالدین قسام، در حمله اسرائیل کشته شده است.
البیک از فرماندهان ارشد نظامی حماس در شمال غزه بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24479" target="_blank">📅 11:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نرخ دلار ۲۵۰،۱۰۰ تومان (رکورد تاریخی)
تتر  ۲۴۹،۶۰۰ تومان(رکورد تاریخی)
بیتکوین ۸۴،۰۵۶ $
انس جهانی طلا ۴،۱۴۰ $
نفت برنت ۹۸،۶۹$
@WarRoom
۱۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24478" target="_blank">📅 11:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عراق: پرواز نجف به ایران برای یک ماه برقرار می‌شود
اما تنها شرکت هواپیمایی العراقیه، مجاز به انجام پرواز میان دو کشور است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24477" target="_blank">📅 10:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ممباقر
: هم آمریکایی‌ها و هم سایر کشورها بدانند در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت
خطاب به ترامپ: «بچرخ تا بچرخیم
!»
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24476" target="_blank">📅 10:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اتاق جنگ با یاشار : چند فروند جنگنده اف-۲۲ رپتور طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی لنگلی به پرواز درآمده‌اند.علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی آمریکا با نام عملیاتی CORONET نیز به پرواز درآمده‌اند که احتمالاً در حال پشتیبانی…</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24475" target="_blank">📅 10:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فاکس‌نیوز: اسرائیل برای ازسرگیری حملات به ایران آماده است.
فاکس‌نیوز گزارش داد
اسرائیل کاتز، وزیر دفاع اسرائیل، هشدار داده است که عملیات نظامی علیه ایران ممکن است دوباره آغاز شود
و ارتش اسرائیل برای اجرای عملیات مستقل علیه ایران آمادگی دارد. کاتز پیش‌تر نیز گفته بود ارتش اهدافی را برای حمله احتمالی به ایران مشخص کرده و در حالت آماده‌باش قرار دارد. با این حال، گزارش فاکس‌نیوز به دیدگاه‌هایی در اسرائیل نیز اشاره می‌کند که از ادامه فشار و محاصره بدون بازگشت فوری به جنگ حمایت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24474" target="_blank">📅 09:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رویترز:
پرونده امنیتی
RAF Fairford
وارد مرحله جدیدی شده است؛ پلیس ضدتروریسم انگلیس اعلام کرده پنج مظنون، همگی شهروند بریتانیا و ساکن لندن، پس از بازداشت به قید وثیقه آزاد شده‌اند و تحقیقات درباره احتمال دخالت ایران ادامه دارد و پلیس احتمال ارتباط‌های دیگر را نیز بررسی می‌کند.سفارت ایران در لندن هرگونه ارتباط با این حادثه را رد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24473" target="_blank">📅 09:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وال‌استریت ژورنال:
صادرات نفت خاورمیانه به‌طور محسوسی افزایش یافته و صادرات عربستان، امارات و عراق به حدود
۱۳ میلیون بشکه در روز
رسیده است؛ بخش قابل‌توجهی از جریان نفت از مسیرهای جایگزین یا با استفاده از تدابیر جدید دریایی عبور می‌کند. در مقابل، صادرات نفت ایران تحت فشار محاصره دریایی آمریکا کاهش شدیدی داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24472" target="_blank">📅 09:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c37bfc6165.mp4?token=dn1T95CvE--4cdpjm59xhpilJeQNZ786kr4Evl1KpDR5PhNalPO_d14xr5K3a4zp5YOjs_SYTXdE1ozEvI_9cL2m5YaYxBf4UId4_blL-XnYgCS_Y_sVG5ojynQjNF3Uql1IewTPHAMdDleCP8CY1ymNF161ZNGqMTm3hQ_u9NjLIhalGc9g1oqA0dqI0tlinpvsQWZusJY0DNyJWwPaCjbJeJAkFpThFgUnEJkkX2vjEJy0sn8bJOwBh7szcXIoNGdCrT_N-B_jw0ncFVOTAEMt_lUAOdFfppoXf0j1PiRTsyMjzr7XEOXlWocHc1qTF_18bJylXXT8Xp88U4s-2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c37bfc6165.mp4?token=dn1T95CvE--4cdpjm59xhpilJeQNZ786kr4Evl1KpDR5PhNalPO_d14xr5K3a4zp5YOjs_SYTXdE1ozEvI_9cL2m5YaYxBf4UId4_blL-XnYgCS_Y_sVG5ojynQjNF3Uql1IewTPHAMdDleCP8CY1ymNF161ZNGqMTm3hQ_u9NjLIhalGc9g1oqA0dqI0tlinpvsQWZusJY0DNyJWwPaCjbJeJAkFpThFgUnEJkkX2vjEJy0sn8bJOwBh7szcXIoNGdCrT_N-B_jw0ncFVOTAEMt_lUAOdFfppoXf0j1PiRTsyMjzr7XEOXlWocHc1qTF_18bJylXXT8Xp88U4s-2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (سنتکام): ویدئویی از برخاست جنگنده‌های
F/A-18E/F سوپر هورنت و F-35C لایتنینگ ۲
نیروی دریایی آمریکا از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» منتشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24471" target="_blank">📅 09:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وار زون : یک فروند جاسوسی SR-71 Blackbird با شماره NASA 844، آخرین SR-71 پروازکننده در تاریخ، از محل نمایش عمومی خود در مرکز تحقیقات پرواز آرمسترانگ ناسا در پایگاه ادواردز ناپدید شده و اوایل امسال به یک آشیانه دیگر منتقل شده است. این اتفاق پس از انتشار تصویری…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24470" target="_blank">📅 08:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیروی دریایی آمریکا : یک فروند هواپیما هنگام فرود روی ناو هواپیمابر «یو‌اس‌اس دوایت آیزنهاور» در نزدیکی نورفک ویرجینیا،آمریکا محل استقرار ناو در ساعت ۱۸:۱۸ روز ۲۸ سپتامبر (به وقت شرق آمریکا)
دچار سانحه
شد. دو خلبان با خروج اضطراری نجات یافتند. در این حادثه چهار ملوان نیز زخمی شدند که یکی از آن‌ها با جراحات غیرتهدیدکننده حیات به بیمارستان منتقل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24469" target="_blank">📅 08:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرنگار فاکس‌نیوز:
اگر ایران به سلاح هسته‌ای دست پیدا کند، تنگه هرمز و خاورمیانه چه وضعیتی پیدا خواهند کرد؟
مارکو روبیو:
ایران تلاش می‌کرد با انباشت
پهپاد، راکت و موشک
به نقطه‌ای برسد که دیگر نتوان برنامه هسته‌ای آن را از نظر نظامی متوقف کرد و سپس پشت این «سپر تسلیحات متعارف» به سمت سلاح هسته‌ای برود. ترامپ مانع رسیدن ایران به این نقطه شد؛ وضعیتی که می‌توانست
«کره شمالی در خاورمیانه»
ایجاد کند. اگر ایران سلاح هسته‌ای داشت، می‌توانست
تنگه هرمز را کنترل کرده و بر جریان انرژی جهان اثر بگذارد.
او همچنین حکومت ایران را مسئول کشتار
ده‌ها و شاید صدها هزار نفر از مردم خود
دانست و گفت داشتن سلاح هسته‌ای می‌تواند تهدیدی برای آمریکایی‌ها، اسرائیلی‌ها و دیگر کشورهای منطقه نیز باشد. روبیو تأکید کرد مشکل،
مردم ایران نیستند، بلکه «رژیم» حاکم بر کشور است
و تصمیم‌گیران اصلی را
روحانیون شیعه تندرو با دیدگاهی آخرالزمانی
توصیف کرد و تاکیید کرد تصمیم‌گیران اصلی،
آن مقام‌هایی نیستند که با کت‌وشلوار در برنامه‌هایی مانند Meet the Press حاضر می‌شوند، بلکه روحانیون شیعه رادیکال هستند.
ترامپ کاری را انجام داد که رؤسای‌جمهور پیشین آمریکا درباره آن صحبت کرده بودند اما انجام نداده بودند:
جلوگیری از دستیابی ایران به سلاح هسته‌ای.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24468" target="_blank">📅 08:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مارکو روبیو: ایران اکنون به‌سرعت به سمت یک
فاجعه اقتصادی
پیش می‌رود؛ موضوعی غم‌انگیز، زیرا ایران کشوری با ظرفیت‌های عظیم و مردمی
باهوش، سختکوش و پرتلاش
است که از
تاریخی کهن و دستاوردهای فراوان
برخوردارند. ایران پیش از روی کار آمدن روحانیون افراطی، یکی از مرفه‌ترین کشورهای خاورمیانه بود. مسئله فقط تحمیل فشار اقتصادی بر حکومت ایران نیست؛ این حکومت طی ۳۰ سال گذشته هر زمان به درآمدی، از جمله از محل فروش نفت و گاز یا کاهش تحریم‌ها در دوره اوباما، دست یافته، آن را برای ساخت بیمارستان، جاده یا بهبود زندگی مردم هزینه نکرده است. ایران این منابع را برای
ساخت سلاح، صدور انقلاب و تأمین مالی حزب‌الله، حماس و شبه‌نظامیان شیعه در عراق
و همچنین حمایت از تروریسم و طرح‌های ترور در سراسر جهان به کار گرفته است. محدود کردن درآمد نفتی و اعمال تحریم‌ها فقط مجازات حکومت ایران نیست، بلکه مانع دسترسی آن به منابعی می‌شود که می‌تواند برای
کشتن آمریکایی‌ها و دیگران، کشتن مردم خود، ساخت سلاح، تهدید جهان و در نهایت پیشبرد برنامه تسلیحات هسته‌ای
مورد استفاده قرار گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24467" target="_blank">📅 08:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مارکو روبیو در مصاحبه با فاکس ترکوند ، غوغا کرده
🔥</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24466" target="_blank">📅 08:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری آسوشیتدپرس: ممنوعیت واردات کالاهای کانادایی به ارزش یک میلیارد دلار از سوی آمریکا اجرایی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24465" target="_blank">📅 08:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تتر ۲۴۹،۰۰۰ (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24464" target="_blank">📅 08:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تتر: حدود ۵۵۰ میلیون دلار USDT مرتبط با ایران را مسدود کردیم.
شرکت تتر امروز اعلام کرد در سال ۲۰۲۶ و در همکاری با مقام‌های آمریکایی، حدود
۵۵۰ میلیون دلار از دارایی‌های USDT مرتبط با بانک مرکزی ایران و شبکه‌های دور زدن تحریم‌ها
در کیف پول‌های مختلف مسدود شده است. تتر همچنین اعلام کرد با بیش از ۳۴۰ نهاد انتظامی در ۶۷ کشور همکاری دارد و تاکنون از بیش از
۲۹۰۰ تحقیقات و پرونده در سراسر جهان
پشتیبانی کرده که بیش از
۱۶۰۰ مورد آن مربوط به نهادهای آمریکایی
بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24463" target="_blank">📅 02:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">روبیو: من با وزیر امور خارجه عربستان سعودی درباره امنیت و ثبات منطقه‌ای، از جمله موضوعات مربوط به ایران، غزه، سودان و یمن، گفتگو کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24462" target="_blank">📅 02:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزارت خزانه آمریکا : بسند در‌ دیداری از دولت لبنان خواست تا اقداماتی را برای مختل کردن شبکه‌های مالی مرتبط با ایران و حزب‌الله انجام دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24461" target="_blank">📅 02:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6ac7d7f6.mp4?token=ErJzaPAEckg--XhEGLl6nqIm9UhLF0n59J56zD2MRubiSTV-VGlOoinh1M-9_6m5XndLMIHsxN4JvbYk6hF6V9IgKONIn2AalE61brFEAC1QYvH8aPdW5D1F839igVB9tCqn8ta2Yt2S15YJlY-_ABRMQIZP4z6vtf7ZQwULujLolfkBl70ESLP3ZwRrg-SFqJCDIJf7F6oRIJ8pUovbSFgBrixxFPtdka1hZIkXHnTxTzaqjiOrkPn9E44B1jPmzYFCEYNyYwMziE9eEEDt7WT9Y05Nb_OsdR7H5IUpnXgReQM2fLKV7Vq4Pf09SqUlSn6INvdtSGD-iKtoZiFqSIv6BpGPt2xqdxdPklJr21MAhm6r3Ng1OCkPumAHYg_tjF-JmvFFxVeX3CBYHSyZpDtUYTdlsAlofK2c3_42Jxv2LOQUwtO8L0NbH18kSv2Ss1xgYLm0yOd49HaZspSPuwxyLWAuOW2Cje6HsZ6od8_JsYvNqqv_JzFGdDvLXQNwYcPy0lFB1ijyZyarbcMeCzREbVJOJuxqNAeFIcB-o8_1hpo8t2Z-q8WIBfeC4YsqXJ7fSikauFmhXIMUNxLX7eR7HAKJ_qvOd8mqs_hneMDn2lBhwdKA4iL5XHYiwHrZZE_Ogep_Mr15pWnidE9DW9W6mxOoxUBZxX5q8FRJm44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6ac7d7f6.mp4?token=ErJzaPAEckg--XhEGLl6nqIm9UhLF0n59J56zD2MRubiSTV-VGlOoinh1M-9_6m5XndLMIHsxN4JvbYk6hF6V9IgKONIn2AalE61brFEAC1QYvH8aPdW5D1F839igVB9tCqn8ta2Yt2S15YJlY-_ABRMQIZP4z6vtf7ZQwULujLolfkBl70ESLP3ZwRrg-SFqJCDIJf7F6oRIJ8pUovbSFgBrixxFPtdka1hZIkXHnTxTzaqjiOrkPn9E44B1jPmzYFCEYNyYwMziE9eEEDt7WT9Y05Nb_OsdR7H5IUpnXgReQM2fLKV7Vq4Pf09SqUlSn6INvdtSGD-iKtoZiFqSIv6BpGPt2xqdxdPklJr21MAhm6r3Ng1OCkPumAHYg_tjF-JmvFFxVeX3CBYHSyZpDtUYTdlsAlofK2c3_42Jxv2LOQUwtO8L0NbH18kSv2Ss1xgYLm0yOd49HaZspSPuwxyLWAuOW2Cje6HsZ6od8_JsYvNqqv_JzFGdDvLXQNwYcPy0lFB1ijyZyarbcMeCzREbVJOJuxqNAeFIcB-o8_1hpo8t2Z-q8WIBfeC4YsqXJ7fSikauFmhXIMUNxLX7eR7HAKJ_qvOd8mqs_hneMDn2lBhwdKA4iL5XHYiwHrZZE_Ogep_Mr15pWnidE9DW9W6mxOoxUBZxX5q8FRJm44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بن سبطی (یگال سبطی) پژوهشگر، روزنامه‌نگار و سخنگوی سابق فارسی‌زبان دولت اسرائیل: مجتبی خامنه‌ای زنده‌ست ولی هرچیزی میگه برعکسش انجام میشه ، اسرائیل منتظر درگیری بین رهبران رژیم مانند آخرای شوروی یا قیام مردمه.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24460" target="_blank">📅 02:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عراقچی: من پس از چند ساعت به تهران باز خواهم گشت و امیدواریم که سه شنبه پاسخ نهایی را از طرف آمریکایی‌ها دریافت کنیم.
هیچ تغییری در مواضع ما در رابطه با برنامه هسته‌ای ایجاد نشده است و شرایط ما برای بازگشایی تنگه هرمز کاملاً مشخص است.باید حرف رهبر اجرا شود
ما همیشه برای جنگ آماده هستیم و همچنین چیزهایی برای گفتن در عرصه دیپلماسی داریم. موضوع فعلی که مطرح است، صرفاً تنگه هرمز است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24459" target="_blank">📅 01:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عراقچی داره برمیگرده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24458" target="_blank">📅 01:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24457" target="_blank">📅 01:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی ) @WarRoom
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24456" target="_blank">📅 01:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyO6e7YnAYJbbSuQm33VagEnAIse2YJ0TeWUpP-Gmg-Uev9gy5nqshTKwwXUoUdT-4GuZWrakIJPx-RSsiIr3n0V0GDt11s2ANTwriNS_0stxNPQyx0lFcZUaxx9O1IFj-oddhB4Nk6H0NpW65tx0ZM34K8q6u36qYuPFOVwgdzj1hPI9JuR-erjfHZQtrfcKjC3dahi0HXsuWtaee5t4E2ur-1je1Ly97lCqMlNGdJfL7PcI1SMc9XPE1iFwdHtM6CnFWsietPNL0yFst3HGYJeBx_rq_DPxbbo5Lwojb8uj3eIQheMi8WGyBxHGusMwp2vjIbPuvmiXVtKmAuxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «آکسیوس به‌تازگی گزارشی منتشر کرده که در آن ادعا شده من به ایران
رفع تحریم‌ها و دسترسی به دارایی‌های مسدودشده
پیشنهاد داده‌ام. این ادعا نادرست است. من
هیچ چیزی به ایران پیشنهاد ندادم!
گزارش آکسیوس، مانند بسیاری از گزارش‌های دیگر، یک
جعل
است که صرفاً برای اهداف سیاسی منتشر شده است. آنها باید
فوراً این گزارش جعلی را پس بگیرند!
»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24455" target="_blank">📅 01:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24454" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی ) @WarRoom
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24453" target="_blank">📅 01:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5CSkk7CELdC_OBTAu3cZpXrtlQU4Sqz0OsW3ZAqythkMmMecMmLE4HLgp-pNPQYIVPnEc9QMQlOPD3zHjgEbMqDCLgoD__GM2HvWvvQZrr08Y75D6zMZ_twH8vMWRfBrqQ_13egBuX-hOBWP01OVJCm8b_8dP_jP_Y-Q3Wz5NkxzBHm0vslEPjI1xahSu36ZmqBJHVoS_AUoYPadw2gPldW2D5iNomi91gfpZPvGN5CIOSDCiJcE2pOxX8EWF4dPk-SQTvhP_UlfNz4FPElq1CxF_enF7soZoSszcG6Qxo8hNiSax7VwTmOpnAt9ryo9r7u3WdjZs-OP67xiwZl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوی باشید ، تمام دایرکت شده نا امیدی غر نزنید ، بله اجماع شکل گرفته !
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24452" target="_blank">📅 00:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24451">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">داداش یاشار کی مث قبل لایو میذاری بگی تا صبح بیداریم امشب شب خطرناکیه  چرا نمیان پیر شدیم</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24451" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from....</strong></div>
<div class="tg-text">داداش یاشار کی مث قبل لایو میذاری بگی تا صبح بیداریم امشب شب خطرناکیه
چرا نمیان پیر شدیم</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24450" target="_blank">📅 00:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزارت دفاع عربستان سعودی: خالد بن سلمان، وزیر دفاع عربستان، از شیخ منصور بن زاید آل نهیان، معاون رئیس امارات و رئیس دفتر ریاست‌جمهوری، برای سفر به عربستان در روز سه‌شنبه ۲۹ سپتامبر ۲۰۲۶ دعوت کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24449" target="_blank">📅 00:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پرتاب موشک هم اکنون از هرمزگان بندرکنگ به سمت تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24448" target="_blank">📅 00:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دفتر نتانیاهو : بنیامین نتانیاهو و همسرش روز گذشته به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، به امارات سفر کردند. نتانیاهو در این سفر توسط رئیس شورای امنیت ملی، رئیس موساد، دبیر نظامی و مشاور سیاست خارجی همراهی می‌شد.  @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24447" target="_blank">📅 00:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دفتر نتانیاهو : بنیامین نتانیاهو و همسرش روز گذشته به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، به امارات سفر کردند. نتانیاهو در این سفر توسط رئیس شورای امنیت ملی، رئیس موساد، دبیر نظامی و مشاور سیاست خارجی همراهی می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24446" target="_blank">📅 00:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آکسیوس: پیت هگست، وزیر دفاع آمریکا، در یادداشتی به تاریخ ۲۲ سپتامبر، به پنتاگون دستور داده از
توانمندی‌های اطلاعاتی و سایبری برای مقابله با مداخله خارجی در انتخابات آمریکا
استفاده کند. این دستور شامل جمع‌آوری اطلاعات درباره تهدیدهای خارجی علیه انتخابات و انجام عملیات مشترک سایبری با وزارت امنیت داخلی است. با این حال، این دستور
شامل حضور نیروهای نظامی در محل‌های رأی‌گیری یا توقیف تجهیزات رأی‌گیری نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24445" target="_blank">📅 00:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتایج یک نظرسنجی جدید در «کانال ۱۴» نشان می‌دهد که اکثریت اسرائیلی‌ها در مورد هشدارهای پیش از ۷ اکتبر، به روایت بنیامین نتانیاهو، بیش از تحقیقات روزنامه‌نگاران اعتماد دارند؛ به‌طوری که ۵۴ درصد معتقدند این گزارش‌ها با انگیزه‌های انتخاباتی منتشر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24444" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شکایت «شین‌بت» از شبکه ۱۲ به دلیل افشای خبر سفر به امارات
سازمان امنیت داخلی اسرائیل این شبکه را متهم کرد که با افشای خبر سفر نخست‌وزیر به امارات در زمانی که هواپیمای او هنوز خارج از حریم هوایی اسرائیل بود, یعنی حدود ۵۰ دقیقه پیش از فرود , جان او را به خطر انداخته است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24443" target="_blank">📅 00:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR4PpaxJMi1jGrS9LG37-UieLXOBt-AIUWcs9UIa4RHfHwCOAjVfweNyVIS3eStbXRBeygQl0G19r97JcP49HUHLvewRLXh-Gm0jPI_BgzZkxobRnUCrV6-jrIFvhaZvof0pYdybwNnA2krniwOw7M-Psvb5j9RYkzgMxb_W-Z3qbdoCQ7nmlXWCjl1DF884mj-NAN5ejeyuyfpXrGLnzf4BRZKUjk7jiPYDHwH9CJZ9vqwg-h605G8tLJ0CUulWK9beXR_vTKfpYHkx_aY-I_AFvX0nV6Gbul_z8eXo0Eaq9N2JWgWCBxUyEsCSLJ9VwDDRAVuCuVORAMjyne8glA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت توییتر کاخ سفید: ظرف دو هفته چیزی از اقتصاد ایران باقی نخواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24442" target="_blank">📅 00:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4109be46a.mp4?token=SdH-LN2HzpkM0zy-2XA2w0OSY0UU_aPeyfZcLIw1bc6mBG2l_LY8dXsihnQsH3vth2uvWy0SBOw8k2fY8o2sPFA4qGuA7Risfo3j8lgmIKkaSjGhrQNfhsv3zHFy6rSf4s6FNCobf3_yGMspABeheM6HOh2WTDeYalMroLa57xl3njw799HOAfad2kIoROhFnJmpcUsiFWRfkxIU9280LPq5Hx12LlaY27pYsys49kixoWMbY2-Y2tas4ee5z7H65sprvNQAgMARy5f5gdEr_aZ3g2WzuN2CXtWQHAKdK2Gh5eufh7XI7NjDdvJHSaA9hZr7p9XqbJcduC6xUgmZNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4109be46a.mp4?token=SdH-LN2HzpkM0zy-2XA2w0OSY0UU_aPeyfZcLIw1bc6mBG2l_LY8dXsihnQsH3vth2uvWy0SBOw8k2fY8o2sPFA4qGuA7Risfo3j8lgmIKkaSjGhrQNfhsv3zHFy6rSf4s6FNCobf3_yGMspABeheM6HOh2WTDeYalMroLa57xl3njw799HOAfad2kIoROhFnJmpcUsiFWRfkxIU9280LPq5Hx12LlaY27pYsys49kixoWMbY2-Y2tas4ee5z7H65sprvNQAgMARy5f5gdEr_aZ3g2WzuN2CXtWQHAKdK2Gh5eufh7XI7NjDdvJHSaA9hZr7p9XqbJcduC6xUgmZNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا تیم شما امروز با ایران صحبت کرده است؟
ترامپ: بله.
خبرنگار: با میانجی‌ها؟
ترامپ: بله.
خبرنگار: چیز دیگری هست که بتوانید با ما در میان بگذارید؟
ترامپ: ما پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24441" target="_blank">📅 23:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تنگه صدای ناله های حسن خرسی میاد</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24440" target="_blank">📅 23:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">قشم صدا میاد</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24439" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24438">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیویورک پست: به نقل از یک مسئول آمریکایی، دیدار مقامات ایرانی با کوشنر و ویتک در نیویورک، منجر به مذاکراتی از طریق واسطه‌ها درباره امکان باز شدن تنگه هرمز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24438" target="_blank">📅 23:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uy1sLzlSf-1qXgt9sCUXeiPE2x6ptMew1KvLT9W3IOwt0_acz54dHhD1i_wIEM0heKzZEkRcyusdAlNWhpuE6qi35V1D2uy7F1f-UKnRLrZIgu6TkIHCU7dSQcSy3HK4ZtiHMa0SJGZN75M1xVFH7l0KN16-O8s7rTNoMjgoMB9nxiEP2DlfxZzqUNvF8olL-oPM-YSLFsJeOVOFhK38sPGq3pEgZ0WAIUbFXB-8vhzHbzWdERI_4T15isECa7HJi6W82sxKjY_r38Nghnuh8yGEzGdbKo0TGlGE0j5UbwblqVezoU3D4IXO9Qa5v8lfC2ffUYjecQkE7JmlceK7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : حضور
پنج فروند هواپیمای سوخت‌رسان، یک فروند T-38A Talon (هواپیمای آموزشی جت مافوق‌صوت)، یک فروند پهپاد MQ-4C (پهپاد شناسایی و مراقبت دریایی دوربرد) و یک فروند E-3B Sentry (هواپیمای هشدار زودهنگام و کنترل هوایی)
در محدوده تنگه هرمز و خلیج فارس رصد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24437" target="_blank">📅 23:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37e38e4cc.mp4?token=QYiRQDA6SLmd49A5JYXheG2O8MMw6oHrQaV2zIwkqYYPbRZP5M5O-wgStVMzu_u0BnOkr2ijkykHd9GvR-aBP100cWnkLFWDWEC3lq9uxhE2CpjD3ZaXkWMUv-NRRSXLBar8fey-bjRm7x4Jc_eQXbhahNvNMn7R5opAwebnSYRVKQ6NdqSNnFElsK6DskhlQdIF0IzRaLRJRVQEz1xsZt2QPYiasyaBysPEgb2ndnUsHBNIaaOuAsZwWaouD73Hwi24aR6RPq1R_b8rMVB13J2116WIFQKtfUcDJNN-z2wscpw1TEZI7wnMvVh13H3FM7XKjSqNdgT6Jtpjo9bmoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37e38e4cc.mp4?token=QYiRQDA6SLmd49A5JYXheG2O8MMw6oHrQaV2zIwkqYYPbRZP5M5O-wgStVMzu_u0BnOkr2ijkykHd9GvR-aBP100cWnkLFWDWEC3lq9uxhE2CpjD3ZaXkWMUv-NRRSXLBar8fey-bjRm7x4Jc_eQXbhahNvNMn7R5opAwebnSYRVKQ6NdqSNnFElsK6DskhlQdIF0IzRaLRJRVQEz1xsZt2QPYiasyaBysPEgb2ndnUsHBNIaaOuAsZwWaouD73Hwi24aR6RPq1R_b8rMVB13J2116WIFQKtfUcDJNN-z2wscpw1TEZI7wnMvVh13H3FM7XKjSqNdgT6Jtpjo9bmoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «من وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاقاتی باشد که تا به حال برای جهان رخ داده؛ برای ما، اما در درجه اول برای جهان. اسرائیل همین حالا از بین رفته بود. دیگر اسرائیلی وجود نداشت، خاورمیانه‌ای وجود نداشت و بعد موشک‌ها و بمب‌ها به سمت ما و اروپا روانه می‌شدند. و من جلوی آن را گرفتم.»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24436" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcbc9a39f.mp4?token=jcPFPjtibQClMCkABV4HfGcQvp1j-iSAGTQi0sWqmQNGSyAfPqpuQuQcYPibYzWTR0j6kOTTgJPh-RnMiJCJboE0OzvuoBeRu5IhxinLqQJQMeIeVKgY8dgv3D-e6k53IWTr8c13_Uto7qzl5u0wsBiwBASq6pZH-dbsnMma5qPNmE0DOGtVpfb1RekRsoQ8IciY3D_YX8ms8NJxSs33BQhgHbvaZM30kTovgzRI0KP42MBC41vmlu4eZXR7MbXk5QIJBDLg77Eva8CJVgH4fHGf4k_5uyXfPDNL2Zlbpdf8u5b7DolU1gc1NzaG91-KDQ23BG6PVCeFRSFGo1bj9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcbc9a39f.mp4?token=jcPFPjtibQClMCkABV4HfGcQvp1j-iSAGTQi0sWqmQNGSyAfPqpuQuQcYPibYzWTR0j6kOTTgJPh-RnMiJCJboE0OzvuoBeRu5IhxinLqQJQMeIeVKgY8dgv3D-e6k53IWTr8c13_Uto7qzl5u0wsBiwBASq6pZH-dbsnMma5qPNmE0DOGtVpfb1RekRsoQ8IciY3D_YX8ms8NJxSs33BQhgHbvaZM30kTovgzRI0KP42MBC41vmlu4eZXR7MbXk5QIJBDLg77Eva8CJVgH4fHGf4k_5uyXfPDNL2Zlbpdf8u5b7DolU1gc1NzaG91-KDQ23BG6PVCeFRSFGo1bj9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «به‌محض اینکه این جنگ تمام شود، تورم به‌طور کامل از بین خواهد رفت. کاملاً. هیچ‌کس درباره این موضوع صحبت نمی‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24435" target="_blank">📅 22:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24434">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd292496.mp4?token=rC37eSEL5zJJDZ4xVTvdwN-rCAlUGf1xzCvfAZG6ukXPi9TsDvIR2MUkAUDU-ZeHEyIvJv7k0Rzf1cHuHPkIpySRexIMHEDwpK4yP7tQpv8MgjZPvZrEim_qG2lokkqRBbJxy5dAMbesqTXlibciAJptujjPv2AabH4N51lgb-uksnS29M6W8-jFLoZwzBsZVTDAU444C_lZ7QpdxC0g7i0kKtaa9_U9frkQByOrEWegfRF6ndOE_LLTqQTEzDjlWay3ORckFzUrs-lEUd5eDUWoelRI55bAXhVaPOcKx18RChf8D1-uk4EL44g4KguaqORmVTS12LpLa4LUeYLmzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd292496.mp4?token=rC37eSEL5zJJDZ4xVTvdwN-rCAlUGf1xzCvfAZG6ukXPi9TsDvIR2MUkAUDU-ZeHEyIvJv7k0Rzf1cHuHPkIpySRexIMHEDwpK4yP7tQpv8MgjZPvZrEim_qG2lokkqRBbJxy5dAMbesqTXlibciAJptujjPv2AabH4N51lgb-uksnS29M6W8-jFLoZwzBsZVTDAU444C_lZ7QpdxC0g7i0kKtaa9_U9frkQByOrEWegfRF6ndOE_LLTqQTEzDjlWay3ORckFzUrs-lEUd5eDUWoelRI55bAXhVaPOcKx18RChf8D1-uk4EL44g4KguaqORmVTS12LpLa4LUeYLmzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «اگر می‌خواهید شاهد آشوب و یک فاجعه باشید، بگذارید آنها یک شهر را با سلاح هسته‌ای هدف قرار دهند. من فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم. بگذارید آنها با یک سلاح هسته‌ای به خود ما حمله کنند؛ خطاب به تمام آن آدم‌های احمقی که فکر می‌کنند چنین چیزی اشکالی ندارد. آنها دیوانه‌اند. هیچ شکی در این باره نیست. آنها واقعاً آدم‌های دیوانه‌ای هستند. من همیشه این را به آنها می‌گویم. می‌گویم: «مرد، تو دیوانه‌ای.»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24434" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec45ce4fdf.mp4?token=coRv5ymQFjfLXhP5dNnho9zIN7Mx8z1iazki0iAXT88mw6WFCYLJvHUZKSBUKmI8HsfKTNlOVVttRjtiyUSnw-vmdfOdyWSoVlyRvrYq5gDMQGQFSQ3jaPlX5OWr_51onxWQKuNSD057CFk_JUSoOgNJiV7-8xuuv4jZwB-u-qA_RUMioYsIue_6Ewgu6sJQ5mW6GKDRPsURxmwovEjkk1FjtJOewWCgO9Z5i-Phk-ZaFAbG34ryx9UJ3Lo-JPeL1reu4FiO_hm3N6Xj58rzSuL-eEyRPuSXoJj-0VxHD-dt_yD1pKbAmzn0Yo8Pa-GkbQ58YYHy_qXGavn615QpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec45ce4fdf.mp4?token=coRv5ymQFjfLXhP5dNnho9zIN7Mx8z1iazki0iAXT88mw6WFCYLJvHUZKSBUKmI8HsfKTNlOVVttRjtiyUSnw-vmdfOdyWSoVlyRvrYq5gDMQGQFSQ3jaPlX5OWr_51onxWQKuNSD057CFk_JUSoOgNJiV7-8xuuv4jZwB-u-qA_RUMioYsIue_6Ewgu6sJQ5mW6GKDRPsURxmwovEjkk1FjtJOewWCgO9Z5i-Phk-ZaFAbG34ryx9UJ3Lo-JPeL1reu4FiO_hm3N6Xj58rzSuL-eEyRPuSXoJj-0VxHD-dt_yD1pKbAmzn0Yo8Pa-GkbQ58YYHy_qXGavn615QpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا حادثه پایگاه RAF Fairford به ایران مرتبط است؟
ترامپ:
«ممکن است مرتبط باشد، اما باید بگویم از اینکه آنها [افراد بازداشت‌شده] را آزاد کردند،
متعجب شدم. من این کار را نمی‌کردم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24433" target="_blank">📅 22:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24432">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: امروز از طریق واسطه‌ها با ایران گفتگو داشته‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24432" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24431">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6885716a79.mp4?token=SCSBIHJ-ViB7EvBEVurCR6FgL3EszQjbqTVTWJMtc_t8Bq1sjbjX0hz7maOYojZBG2ALh1DmCVTmeFvwds0Wu91dekqt9omydBOBD0aSeOr5F2A6awis9WUAZpKla5XxmtC-ikgwuskZ4g0hQcSAS4gR-6YE9J62xx4ccs9R_vs6ZhD2ILWYCLFDQp5hpkIde8f_nj741i1IylGBfKCVb5b789LGnNY7mNnFpWX-NReC4XPdc0h-AUC14rFur97LQN4kwKjZpXii03ti99Nv9eYLTeHcdSR_0ccv7daSvmar67sptZ3lViweTs2YQPxIQ9Koi_04EY99vtizfZKNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6885716a79.mp4?token=SCSBIHJ-ViB7EvBEVurCR6FgL3EszQjbqTVTWJMtc_t8Bq1sjbjX0hz7maOYojZBG2ALh1DmCVTmeFvwds0Wu91dekqt9omydBOBD0aSeOr5F2A6awis9WUAZpKla5XxmtC-ikgwuskZ4g0hQcSAS4gR-6YE9J62xx4ccs9R_vs6ZhD2ILWYCLFDQp5hpkIde8f_nj741i1IylGBfKCVb5b789LGnNY7mNnFpWX-NReC4XPdc0h-AUC14rFur97LQN4kwKjZpXii03ti99Nv9eYLTeHcdSR_0ccv7daSvmar67sptZ3lViweTs2YQPxIQ9Koi_04EY99vtizfZKNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما
خیلی زود در این جنگ پیروز خواهیم شد.
این جنگ تمام خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24431" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24430">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e7e5f951.mp4?token=ITOWA-1MyNVK8LbZja8W9jVLu3STgSAaIybgF3DuNM4w4g6dtxQZ_8aE27Lckd4wW0GUCvXOiM0_Qkj69Wh37aOqhaasPKkbsuZKltjS6PabPqx2z9YGwTGNGver-1iGecUkcFRqZ34Qk7UAHylN3-ySdhzWXxtvY5YMUpEvwTCjIxisbBN1AYqZ1B5XJLBeuAxSIwKS2mrWDcmVAtlKrQoHz63PVNf4iIsqqBek9u_fokjzlJhxvi7PUfi6oe1_9P5QOmOYyc-zuwY24d7G8dCFXX-a_VyQ45gs6DCbnr1pM9VWW77yCN8xiPlTFrSHZpTsxoEDa_QjpOC_odJOPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e7e5f951.mp4?token=ITOWA-1MyNVK8LbZja8W9jVLu3STgSAaIybgF3DuNM4w4g6dtxQZ_8aE27Lckd4wW0GUCvXOiM0_Qkj69Wh37aOqhaasPKkbsuZKltjS6PabPqx2z9YGwTGNGver-1iGecUkcFRqZ34Qk7UAHylN3-ySdhzWXxtvY5YMUpEvwTCjIxisbBN1AYqZ1B5XJLBeuAxSIwKS2mrWDcmVAtlKrQoHz63PVNf4iIsqqBek9u_fokjzlJhxvi7PUfi6oe1_9P5QOmOYyc-zuwY24d7G8dCFXX-a_VyQ45gs6DCbnr1pM9VWW77yCN8xiPlTFrSHZpTsxoEDa_QjpOC_odJOPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ:«اگر جمهوری‌خواهان در مجلس نمایندگان و سنا پیروز شوند، به هر فرد بزرگسال ۵ هزار دلار پرداخت خواهیم کرد. و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند، چون هیچ درآمدی ندارند و کشور را به سمت رکود اقتصادی خواهند برد. آنها هیچ پولی نخواهند داشت.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24430" target="_blank">📅 22:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkLdNXNPk3xPTJ1ilpdN29Cju8EmXePlC0OObazPwljA08rR1V73ouuvsh58r_DtcVK1ICwXC8viD6nf1l-grJ4hh_3AebZcpXJcfgtuVJ_HvMSrrNR79Nt5_WepYj98TMIp88wABpaiRauJQHkEkmMTK66Hw8Hsy3F_NqLXbMcgofTEXE_k-SAuIMhO0PIjKMtRgGnvFBhmae4V4rHgI-6D0a1NVh_XiH5aF8tKLEdOuzoJDvja4tFVsFuSVf9oeMx1EEEJ7CDkhFPbl-CZHMLdPclnhefxtplbM08eih8Wqpt41tfspKzLxlpE8NeG-vtUcVkhUEAoQtv-PYjUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بزرگترین کارخانه فولاد در آیووا ساخته خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24429" target="_blank">📅 22:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">باراک راوید ، آکسیوس :به گمانم ایالات متحده می‌خواهد شاهد آن باشد که ایران بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کند؛ کاری که در جریان مذاکرات سوئیس متعهد به انجام آن شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24428" target="_blank">📅 21:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24427">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">امارات متحده عربی سفر نخست وزیر اسرائیل به این کشور را تکذیب کرد</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24427" target="_blank">📅 21:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70875dba60.mp4?token=EGEJWockiGGvwdzUlLp5gojSPNrsQGsfRDmVvzQVr-0oQWSjXjsawC7oZIlzgxOIsy4GIiiyJspht2sUbqpnMamP-3IWK1bod422hr9ETApU6Tz61fCUgRvh37O-osSKU-SzypmKJ4YXmDh-ast5DJx9OtAiniE3QgY6EDxy-EJHnd9BUCLFYUNEz7jv56dwLVdmrb6JKBhQPdhbAVRQsaiA5-PDiJqaskJxk19xeHiqNSvXDR4K6_bUTLPqgMV0wU4VtR9VyI_OJLEcy2erAD6C8LKatptaqLfT3Riu27N4Va2WAhjpjMxH3bZtQgneBmoDqEX8jFDOvDMcq--P1gpZZMaMABrxz17KaH0rEnwD5A5b2E6M8ncsRlV5ryhjO11QEOoDpfKgbTqc4nmqyjSvkhC3QPl0Udf9111Vbo1rTDdfJJymXGEwX3m6QKcRfh0KXfKbjZCXTRgsSg6SmydjOmX7APvNPcvC_D1QuYcnNE-CULzwb4_FSLsa0N5y7aXk4ml-EXH_ZfOHBcFnjqolSHiajublh0YdBrzJbiwKcXVjBFOy682FKRfhf5EuL1tSP2pZxatFB3Lt9EnsWFy7Ys8rzwgkMzluoC8LCi68jzk07HAMfhwDYWokD-UJl0SSuYjrkzXYoTtw-2o6lBeXTUcbTRf1owBE9sctCoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70875dba60.mp4?token=EGEJWockiGGvwdzUlLp5gojSPNrsQGsfRDmVvzQVr-0oQWSjXjsawC7oZIlzgxOIsy4GIiiyJspht2sUbqpnMamP-3IWK1bod422hr9ETApU6Tz61fCUgRvh37O-osSKU-SzypmKJ4YXmDh-ast5DJx9OtAiniE3QgY6EDxy-EJHnd9BUCLFYUNEz7jv56dwLVdmrb6JKBhQPdhbAVRQsaiA5-PDiJqaskJxk19xeHiqNSvXDR4K6_bUTLPqgMV0wU4VtR9VyI_OJLEcy2erAD6C8LKatptaqLfT3Riu27N4Va2WAhjpjMxH3bZtQgneBmoDqEX8jFDOvDMcq--P1gpZZMaMABrxz17KaH0rEnwD5A5b2E6M8ncsRlV5ryhjO11QEOoDpfKgbTqc4nmqyjSvkhC3QPl0Udf9111Vbo1rTDdfJJymXGEwX3m6QKcRfh0KXfKbjZCXTRgsSg6SmydjOmX7APvNPcvC_D1QuYcnNE-CULzwb4_FSLsa0N5y7aXk4ml-EXH_ZfOHBcFnjqolSHiajublh0YdBrzJbiwKcXVjBFOy682FKRfhf5EuL1tSP2pZxatFB3Lt9EnsWFy7Ys8rzwgkMzluoC8LCi68jzk07HAMfhwDYWokD-UJl0SSuYjrkzXYoTtw-2o6lBeXTUcbTRf1owBE9sctCoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وس استریتینگ، وزیر دفاع بریتانیا، درباره ایران:
«فکر می‌کنم حمایت از اقدام دفاعی آمریکا، کار درستی بود.
کاملاً درست است که بگوییم جنگ در ایران، جنگی نبود که ما انتخاب کرده باشیم؛ اما در عین حال، هیچ شکی نیست که ایران نیرویی شرور و مخرب است که بریتانیا، منافع ما و متحدانمان را تهدید می‌کند.»
پلیس گلاسترشر گفت ساکنانی که به‌دلیل احتمال وجود توطئه‌ای برای حمله به پایگاه هوایی سلطنتی فیرفورد (RAF Fairford)، از حدود ۸۵ خانه در اطراف این پایگاه تخلیه شده بودند، اکنون می‌توانند به خانه‌های خود بازگردند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24426" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک منبع آمریکایی به شبکه العربیه گفت: اختلافات و موانع بزرگی بین تیم‌های مذاکره‌کننده آمریکایی و ایرانی وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24425" target="_blank">📅 21:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBXd_JhbsNIzlPc2bCSCiMbfiWh3cfd7r_cQ4e8KYgINET9DEbJL8gWo3Z_N7usAsRrgEDpB6zc6b015dNf-EsgtqlHNgwY3UDePXHkeysLviGOrmpP1fZMdHQ3FvQs3gZ-3UjbfoEV2vYDUFb0QmPIAVgKjY_fhjArc2XLFgXyJKUY1epOUD6a5nzr57ar3fdA7O3Re5dnPXEI-RsLdXItYtFAduwqvVlojtNwliOFqLImRMQmh26QPLcyZoS-WYBkGL2Eo2nY_9-UAuilz4ZKtBGqdZwr5Y8nmF-rVtvSg-0IowAlKBw8nceiKd8jHKA1w-0Te-Jx9nCuqGnIcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
عملیات طرد اقتصادی باعث شده که ریال به رکورد‌های پایین‌تری برسد.
ما به تخریب توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24424" target="_blank">📅 21:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ارتش اسرائیل : لحظاتی پیش، یک موشک رهگیر به سمت یک هدف هوایی مشکوک در منطقه‌ المطلة  که سربازان  ما در جنوب لبنان در حال عملیات هستند شناسایی شده بود، شلیک شد.جزئیات در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24423" target="_blank">📅 21:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال ۱۲ اسرائیلی:
نهادهای امنیتی اسرائیل در حال آماده‌سازی برای احتمال از سرگیری درگیری‌ها با ایران هستند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24422" target="_blank">📅 21:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEanZjy3plNwbn-dVRvpFoY8Jkro-qddsjzpezsNrNsbKll4qbt7lujbR7-d47f-vY4ErtFmvL1TTDD4yADFVMz0wOVgYrNKzDz3m0T3lXVPUVhB1OMLpPlaq6hZ-Otyv-fCdQ44zKY-9PDjEP5Fb4XTid_nfrrurzDbY0HCyMPoa16sZpHihoHM4a1izx9mV8wSAXuzv-n_anSafrHiwLTbm8M4mDUkhPIN0OcdCFlgtgnpCQKGSre3DzWWtz4Oc5KXo_Bz6zI_kK3gyph72HDM2Yz_iaYL9sWeWcSoHUEmtZLzEGIAv_mSPWHYIbD0uCsFdUv_y_JY4_T98-mpCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل:
شَدی ابوحطیرا، از تأمین‌کنندگان مالی حماس که شبکه انتقال پول «ژنو» را هدایت می‌کرد، در یک حمله هوایی دقیق در غزه کشته شد. ارتش اسرائیل مدعی است او
ده‌ها میلیون شِکِل ارز خارجی
را برای شاخه نظامی حماس منتقل کرده
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24421" target="_blank">📅 18:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مورگان اورتگاس، معاون فرستاده ویژه آمریکا در امور خاورمیانه: «سناتور لیندزی گراهام هرگز از باور به شما (مردم ایران)دست نکشید. او باور داشت که شما دوباره آزاد خواهید شد. او هرگز از تشویق رئیس‌جمهور ترامپ و وزیر خارجه روبیو برای حمایت از آنها (مردم ایران) دست نکشید.»
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24420" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
