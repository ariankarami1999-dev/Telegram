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
<img src="https://cdn4.telesco.pe/file/vITvtJNjeu5ybJ6rs3XbSiJr_G3Hon71mB-ORM5q3qRNzWsh_tOBw8B9k0SoZf4n-uq9hFVu4csO6JV2-3eiabOVwNxx5EH426FdDvx4FgCsSf8W_IvQfoK9VG6ds1tA7tEmQL6KnlHnwXGcpVMHC0AYDrupRoCzgVujkDRqiDrT7Jru17v7rpJAbmWLwZjJ0kofDv2ynUO1Xx3P21n9I7Urw-93nEbP8E_sb1GsgVSpAQrbkysjQNxiJT4x1gF4X8c_dGc7L7bxHRpk_Wp0WT6gFZNHuBgW3tB-J4HnyMATbHIo-Im6a7HCwcKZ9ZVItcS17xrc6onUS57fm3Mqmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-696339">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGGKjfYjv5hA2QT8-0xLUwNhp4MYft-fpjeuTaeLoHyYuc07Dq5qXh3w4b51Dg--FG8PxWISy7RGFsQpbFwQIPcPoKYzcWr2qJv6jdkrrwqZiernUyh-Jn2pPru0z3maQbaPGUC7MlFBXckRsiTMvQWyrCUQuWc3imp5rjERoV7QCMJBn-s5qRwkoMLCXnQsEM2aVSeYnyAZdXpvzeYJMpXYaklEzbOkwcbLgeEHJxPEAGbPR775WNc92LWlbs989Ufjyi3RC0foNJJkXLA9VTO9AB52LPR07EQ68kRBtHTeiioizspOOvp8AIb0USMk-2gNYnDnigGQbSQN-P1wMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی انواع گوجه فرنگی ها
😨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/akhbarefori/696339" target="_blank">📅 13:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696338">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wArVLxneWrAX4ttZ8DthecQG3w5rplSAAfKS-f70FunW_Yb8jqtcgN53RwE5eFaipxWpqJ8MJ20BAqSI303rmPaVj9Bpiezs_nYq92wJ0rFKanwU5_ZDC7AzkU-oaD-8k6ZhiscmVsq69_Dyiq-2Ay_pChcD3vETvXZucAlT6XiYjej8gYeTdwR9V8oTBGcjmvwjKTdQte0Q-qayqRaGuNDMtzvEb86U31zEf2Zj4ajFkYrNOOjVG-lvK0L27KmQ8gQt8V6Vm_2oIC5KqkX_jaUrDTBCzfe4pIqZMeeJqASXSp0plxVeB80tsWUIsZ5-xF3FGFiW78UC82zoNJaNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هرگز اجازه ندهید کسی به شما بگوید که این ماجرا از ۷ اکتبر شروع شد!
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2107764403290394935?s=46</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/696338" target="_blank">📅 12:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118a1b3ccb.mp4?token=C79egTW_Iounx3eeJDTTWFS-9YK0zgxH_jRqssPfD5koaXKRxXlduEHvmJQ7RRYeOvJ-JFdJF7CsXyW4AMKCOVMJKbaiQWS-Nzne9qOwyAsIip_V5Picy7B8r9-N4dFLhP-LnS-ZnGTj3-bkYvuDqwxTVKL9g4-N9Mwxl1zaA1Ea5OL1nsCmwC2m9Z_EOD-PyYv7dnpK6UtKIWhvXdEqaDHEm7jzFkLfWpKWqIcT5OYhfWT_c7I--pqrN811gDTDVmIl2ntNbGLG25XmNRwV07hRtqTM4u_GxaigLpd2p1OczV3N1IQi14lAnk_IPEjYCD-vIjUjbdTh7JLGZZ-_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118a1b3ccb.mp4?token=C79egTW_Iounx3eeJDTTWFS-9YK0zgxH_jRqssPfD5koaXKRxXlduEHvmJQ7RRYeOvJ-JFdJF7CsXyW4AMKCOVMJKbaiQWS-Nzne9qOwyAsIip_V5Picy7B8r9-N4dFLhP-LnS-ZnGTj3-bkYvuDqwxTVKL9g4-N9Mwxl1zaA1Ea5OL1nsCmwC2m9Z_EOD-PyYv7dnpK6UtKIWhvXdEqaDHEm7jzFkLfWpKWqIcT5OYhfWT_c7I--pqrN811gDTDVmIl2ntNbGLG25XmNRwV07hRtqTM4u_GxaigLpd2p1OczV3N1IQi14lAnk_IPEjYCD-vIjUjbdTh7JLGZZ-_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: گاهی فراموش می‌کنیم خدا به ما دانش را داده‌است که مشکلات مردم را حل‌ کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/696337" target="_blank">📅 12:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696336">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
یک تالار در قم به‌خاطر عدم رعایت حجاب توسط همسر علی‌دایی در آن‌پلمپ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/akhbarefori/696336" target="_blank">📅 12:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/696335" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696334">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d94d6ebf0.mp4?token=R97-bFhW25ITFFILtaDaWjVQ3Ws8oO8IbjGRNjAm6rkN0jkeK3sujxD2RjBkoyeubNHxY5LayMYmvhHiie4-d0l6BzYJKbItECABUT0zS9j0R-nrePO0IIQs5pzCTREG9OVaVa4-meVHSRGAC4iFYLPgkBxx1s8loNNg-GOpfgPU0u_UVprD_Qayr11oXPEZPiXSUXh1oWvAaua8rclM39mqxL4QuAAgCHyxqn6H-C7h1y86gdTYKqRKiKgV0cV6Xp2_3ag6F7omctYz5axMaVB9GeFmR97u215k82zWHCtrLUgGLiqAJDHGJ9ak6uMyvUDq9Z-a_gPMSSoAOaI6Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d94d6ebf0.mp4?token=R97-bFhW25ITFFILtaDaWjVQ3Ws8oO8IbjGRNjAm6rkN0jkeK3sujxD2RjBkoyeubNHxY5LayMYmvhHiie4-d0l6BzYJKbItECABUT0zS9j0R-nrePO0IIQs5pzCTREG9OVaVa4-meVHSRGAC4iFYLPgkBxx1s8loNNg-GOpfgPU0u_UVprD_Qayr11oXPEZPiXSUXh1oWvAaua8rclM39mqxL4QuAAgCHyxqn6H-C7h1y86gdTYKqRKiKgV0cV6Xp2_3ag6F7omctYz5axMaVB9GeFmR97u215k82zWHCtrLUgGLiqAJDHGJ9ak6uMyvUDq9Z-a_gPMSSoAOaI6Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر مکمل را چه زمانی مصرف کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/696334" target="_blank">📅 12:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696333">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLOlnNttd4oL4Af7EwUZAAhkdnkOEwcZcXhDC5Mog01KeEpsn7FTwvIATHfT3J0VEgO_Ck8eEA-lwFCH9xImFcuASalXq4RX7FT9VWLfCMp_E2JQDtjqsGtUQt2hoUb3Yvs9mnCoKif-XeFkBnJscphinoGcAqJgXgx518Bs8Fiseh14DXMhiLaGxTiXw-lWos_IROPbjFeDzeDlwcvr30BUE9YQdArrRLaFgMPmBR0T6zklrledffKu0_ZLr836w5ly7_opaYosyYiQJq0i4J6MR1ULzCXomGb1aUbOT-dD1QHHXcaDHbAMMbfO5OkJhtNcGrcyAYiH2yzfqR-w_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای زهرا عبداللهی خبرنگار پارلمانی: یک نماینده مجلس در ملک مسکونی بدنبال زیرخاکی بود
🔹
اسناد موجود است. خانه در بستری تاریخی قرار داشته است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/696333" target="_blank">📅 12:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای وزیر خارجه آمریکا: ایران نتوانست از چندین فرصت برای رسیدن به توافق با ما در مورد برنامه هسته‌ای‌اش استفاده کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/696332" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
کالابرگ ۳ گروه شارژ شد/ افزایش ۳۰۰ تا ۵۰۰ هزار تومانی بودجه ۳ گروه از خانوارها در کالابرگ
🔹
سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲
🔹
خانوارهای تحت پوشش نهادهای حمایتی
🔹
خانواده‌های نیروهای مسلح
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/696331" target="_blank">📅 12:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696330">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
خبر عفو امیر تتلو کذب است
🔹
ویدیویی که از نسیم، خواهر تتلو در دقایق گذشته منتشر شده قدیمی و مربوط به یک سال قبل است.
🔹
نسیم سال گذشته در همین ایام در یک ویدیو خبر از عفو امیر تتلو داد که صحت نداشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/696330" target="_blank">📅 12:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696329">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای وزیر خارجه آمریکا: ایران نتوانست از چندین فرصت برای رسیدن به توافق با ما در مورد برنامه هسته‌ای‌اش استفاده کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/696329" target="_blank">📅 12:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696327">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUd2qpugJbXF53pP_XHLE6f4qkFTPXxNzyXKYFQAnc41dlygYYyapOnxxBct5eFbZB8RTV9Dd5B_qjPfyWbhw2fNwTKymwds5RImRwCCcH5fDqptjcNLL14bPxZAeOUwGGjZsN9mqLv51S-ftp2UdlOAHlntEpKDzN3ucFU1_IBDqkqepm8esVHQ0Wh8BA4XBoLSOlnERG--LIdoU60hcR05bmdgR9LCZU3WO4qve2_uIg1Ato2Q8C0E-fsCEUPxLvAMsAalnnrhTxZYlBqhJJ0gYBWL46R0vv5FHQoXjRYfvnfByDnu1a8cPY1gsNXn-H0MP2fXhOmRrOiy_Z9iEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار ۵ ساله واردات خودرو کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/696327" target="_blank">📅 12:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696326">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7yk30JV70fiBXEZRaA-a3Axi98MvAZAP6n3XRjI8UUHLC3TCfZwGLJz24gWNC8vchIPj4wtS1uQsXD9aGkmSoeQdtzpudKmDWYSL7sTPZ37iR8s9HFgAZ6xEx7n2T-D0IkTZf7BzIK2WNUMOn0pMrUTJQF1_4smjlyqHzN9VBz6d0CWLc8SZjDQLf7gBn9tP8w_nndIacJ-B2kg7AA7QnoXmws5MA2wCNykdAy9UUzoYomDJpY2f5i4eB_6VOk4R3Y50p0xPsu0uahwjRuG4d4ZgAKHBK2REi4t_0zApPnwbH-Z_PnGHDKPcxpSZ7buykukUCMTgik-tTXvszfMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زاگرس دارو در آستانه تصاحب «شفادارو»
🔹
عرضه بلوک مدیریتی ۹۰.۵۲ درصدی «شفادارو» با ارزش پایه حدود ۴۰ همت، در حالی انجام می‌شود که نام «زاگرس دارو پارسیان» با نماد «دزاگرس» به‌عنوان خریدار احتمالی مطرح شده است.
🔹
حدود ۲.۴۵۵ میلیارد سهم «شفا» با حداقل قیمت ۱۶۲ هزار و ۸۳۰ ریال عرضه می‌شود و در خرید شرایطی، حدود ۱۰ همت باید نقداً پرداخت شود؛ رقمی معادل ۱.۷ برابر ارزش بازار دزاگرس.
🔹
فروش شش‌ماهه نخست ۱۴۰۵ دزاگرس با رشد ۲۹۴ درصدی به حدود ۷.۱ همت و سود خالص سال گذشته به حدود ۱.۵ همت رسیده است.
🔹
«شفا» مالک شرکت‌های مطرح دارویی و پخش از جمله دانا، اسوه، جابرابن‌حیان، کیمیدارو و پخش رازی است و خرید آن می‌تواند زاگرس را به یک گروه دارویی یکپارچه تبدیل کند.
🔹
با این حال، دوره وصول مطالبات حدود ۲۸۰ روزه زاگرس، تأمین مالی معامله ۴۰ همتی را به مهم‌ترین ابهام تبدیل کرده است.
🔹
اگر تأمین مالی معامله به‌درستی انجام شود، خرید «شفا» می‌تواند نقطه عطفی برای دزاگرس و زمینه‌ساز شکل‌گیری یکی از گروه‌های بزرگ خصوصی صنعت دارو باشد.
🔗
متن کامل خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/696326" target="_blank">📅 12:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696325">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6dc58491e.mp4?token=qBVfotvz8N8P1WCj5V7P0pJuH-t9AJ40QFCcooVQKBV78rE36bPuDQ1vIe7itZj48I0Rdm905qINVSCjEXy17mIL929vZaj0wm4SRZnTjpKkF6ahA1VAnZiaDZrpoQkEq-ss6Nvgt-mL1umlCOR-c0qZpAxOjwhdu13rRH43vRdNNUx-D9vmHMBm57k18ibVQ0Z1wxjx6vD63oMRxe9oLxjJSs0z15PJi3P5_6V-ZEkT3_Yf--MR1xGympJ32icT34LmJAQPE24E47R6LOgw9lUroWt1Y9G1bEkH9YlKtTZO0mwDRqpyPgkWGcwXiXYQGKkFD-GBDDTGygpmVFEMjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6dc58491e.mp4?token=qBVfotvz8N8P1WCj5V7P0pJuH-t9AJ40QFCcooVQKBV78rE36bPuDQ1vIe7itZj48I0Rdm905qINVSCjEXy17mIL929vZaj0wm4SRZnTjpKkF6ahA1VAnZiaDZrpoQkEq-ss6Nvgt-mL1umlCOR-c0qZpAxOjwhdu13rRH43vRdNNUx-D9vmHMBm57k18ibVQ0Z1wxjx6vD63oMRxe9oLxjJSs0z15PJi3P5_6V-ZEkT3_Yf--MR1xGympJ32icT34LmJAQPE24E47R6LOgw9lUroWt1Y9G1bEkH9YlKtTZO0mwDRqpyPgkWGcwXiXYQGKkFD-GBDDTGygpmVFEMjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ایده ساده و مهندسی که کارگران بهش نیاز داشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/696325" target="_blank">📅 12:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696324">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452d5d369.mp4?token=kkdngRJRlCu1JIRirp55yPuTIFBA0oh7eMvqSJq_DGxLEEMXK7Mf2SCC9ZJLVC05gczyThJiGcdvQyJPao847waVNJQHHwano2dQQBlkQ02RRlUnJ9-gu1wIK0K2fWnPa4GAKbUIv-GThhfVgnuM5zf-B86xY2psqITw9QCXhIU9KdmzW61EuVbG4a0H1KSbSpTwSjpBP_SCT8S0kAbPXKY_s32MIGwfxrbVEyW9j46ik77GfQW4nEXPHlotSb7xHU13c9AAacOUF3h3lN7RqmUJaXCsWiApW8V_XJuFgTiM9B-KMqfE5Qqzp7Svrr2A7Rb24_2f_Ox4PV7Iv-SIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452d5d369.mp4?token=kkdngRJRlCu1JIRirp55yPuTIFBA0oh7eMvqSJq_DGxLEEMXK7Mf2SCC9ZJLVC05gczyThJiGcdvQyJPao847waVNJQHHwano2dQQBlkQ02RRlUnJ9-gu1wIK0K2fWnPa4GAKbUIv-GThhfVgnuM5zf-B86xY2psqITw9QCXhIU9KdmzW61EuVbG4a0H1KSbSpTwSjpBP_SCT8S0kAbPXKY_s32MIGwfxrbVEyW9j46ik77GfQW4nEXPHlotSb7xHU13c9AAacOUF3h3lN7RqmUJaXCsWiApW8V_XJuFgTiM9B-KMqfE5Qqzp7Svrr2A7Rb24_2f_Ox4PV7Iv-SIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراگیر شدن اسلام در بریتانیا
🔹
می‌خواستند اسلام را از بریتانیا حذف کنند اما اکنون ۱۰ درصد کل جمعیت بریتانیا مسلمان هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/696324" target="_blank">📅 11:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696322">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c02f8c6e.mp4?token=eOj4TmM-c6T34mndAa666vBv7Korj16oUPzYT6kAYoJmxC9vaz_Ncz4SSrC9lwXgveQcLYDoSPnbWVzZWAkmbQCoJifcjFmQo21ivWp8uj9A8AaBLvurQVuXL1IueWaw7qYq4YuwA7EB1UXdoRJVcXtW4tn5l2BOfX90mJIW4oxtJ_QnRW6aNvyFywaxC1ghU1xoXE_PTzfw0kb2jSTICEAjJJKFAtb6Fq-FIKZO0IDMyO2-t3a5aZd73vt5FYzp02pkaeLrO1nXAVEPZlOv1-s8KYkspPYA2Bw0noTtq48WlFf38DZT4S6rmeHioQNKzV1bOJZI6pPP07Evnv2Dbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c02f8c6e.mp4?token=eOj4TmM-c6T34mndAa666vBv7Korj16oUPzYT6kAYoJmxC9vaz_Ncz4SSrC9lwXgveQcLYDoSPnbWVzZWAkmbQCoJifcjFmQo21ivWp8uj9A8AaBLvurQVuXL1IueWaw7qYq4YuwA7EB1UXdoRJVcXtW4tn5l2BOfX90mJIW4oxtJ_QnRW6aNvyFywaxC1ghU1xoXE_PTzfw0kb2jSTICEAjJJKFAtb6Fq-FIKZO0IDMyO2-t3a5aZd73vt5FYzp02pkaeLrO1nXAVEPZlOv1-s8KYkspPYA2Bw0noTtq48WlFf38DZT4S6rmeHioQNKzV1bOJZI6pPP07Evnv2Dbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش نگهداری صحیح مواد غذایی
😃
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/696322" target="_blank">📅 11:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696321">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWvVxegIgj9V6uNphGKS2ZbhrBH19hndaow3XxU4hPGoLsqOz9peXz0GwcZJCaFRzRFHOm6Zdit2cweFaUVhFAdosjuLQISbjQB2t4j0wM6K8vTa_TtQurcB_G9DYYTKlXSfcDu0yF_-4FkM0fLCYq0BkaCZw1RRZ_3hB2jocpz-styD4HblnTviAmou6O5Lb8imdytHBdjqlVRcJh8GEXtC9uSy6i_HwH8q3ONNUstmVaceXrpxzmMPrXQqtnaL8l-v4MubmpzzS-fNHdGSJt0Jz0EezjltxjWEBRrZPV5tfYvlIrbSZViBBXjxRWiuI90AbCkqc5YuCf2kF86cyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داریک به سامانه ناظر بانک مرکزی متصل شد
🔹
اتصال پلتفرم به سامانه نظارتی؛ گامی دیگر برای شفافیت در بازار طلای آنلاین
داریک با تکمیل الزامات فنی و نظارتی لازم، به سامانه ناظر بانک مرکزی متصل شد.
🔹
به گزارش روابط عمومی داریک، با این اتصال، معاملات این پلتفرم در چارچوب سازوکار نظارتی بانک مرکزی ثبت و پایش می‌شود. سامانه ناظر میزان طلای ثبت‌ شده در حساب کاربران را با موجودی واقعی خزانه تطبیق می‌دهد و اگر تعهدات پلتفرم از موجودی آن فراتر برود، معامله ثبت نخواهد شد. سامانه ناظر بر پایه دستورالعمل اجرایی مصوب هیئت وزیران و در قالب چارچوب تازه‌ی تنظیم بازار طلای آنلاین شکل گرفته است.
🔹
داریک مثل همیشه همکاری با نهادهای ناظر و رعایت الزامات قانونی را در دستور کار خود دارد و توسعه‌ی خدمات را با همین رویکرد ادامه خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/696321" target="_blank">📅 11:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c43870cc.mp4?token=haoZt4ZBBHHqSUHy8aKXMtN1_9jR8VRwtWDw_GR4Wp7H-PcHru5xtu7IbzJ5-UpeE9tgWhZOBu1cSfAps4OGOzo60oZng8BAFFBE0dUHqH5jQ-xMnMWdD17m-tcLrlJlsIn1lpYS5t8fxEOSe2z6ILIz-xdSg_tHzk2RejEmyUuJsmzEjVSHEJhkl-JfTIXJluSLKsgpRqbqtq7Eq29wX0lvvd4Q7OSfxQpMRR1GznuaWBTyriqV4RNGEp07Kgt-TtYeQQxa-7vvAel1Mso-si-SYoFI3ReW4G1kuugk0jQ35CG2PqJq4a8PW2-JnmH_Ga45l7BxcWTFFjg9rs5pnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c43870cc.mp4?token=haoZt4ZBBHHqSUHy8aKXMtN1_9jR8VRwtWDw_GR4Wp7H-PcHru5xtu7IbzJ5-UpeE9tgWhZOBu1cSfAps4OGOzo60oZng8BAFFBE0dUHqH5jQ-xMnMWdD17m-tcLrlJlsIn1lpYS5t8fxEOSe2z6ILIz-xdSg_tHzk2RejEmyUuJsmzEjVSHEJhkl-JfTIXJluSLKsgpRqbqtq7Eq29wX0lvvd4Q7OSfxQpMRR1GznuaWBTyriqV4RNGEp07Kgt-TtYeQQxa-7vvAel1Mso-si-SYoFI3ReW4G1kuugk0jQ35CG2PqJq4a8PW2-JnmH_Ga45l7BxcWTFFjg9rs5pnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوشیدنی شبانه برای کمک به چربی‌سوزی بیشتر در خواب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/696320" target="_blank">📅 11:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696317">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frmwPKY917nbIIt16MslZq3C6KR1hPfEYyGUWykdi7-hmu6u1czLzMZpttv7dDZJhoe6YCD0YiTfSQv36sefmAl3CU9LmY7r-Ld8e0jp0QslDhlgMQqmdZNUVGoqDGKjWmQmeYJTG6BaQewBxKq3iW63fAveannNoYnUT6_AvT5-_xrwtw-cwhF5y83kZeUtXsPeq7e77g9ldNM2reXMS6dBNnN3NW7aYvDMa8XR9pDZ-OVTAnWQoHeWZz3pKUWl_ftQjmT3NKyyFy5uVvjRSm0TMifXYKYHUHjAGT19CwNdT09gqgZhu-kfxKkhaWCm1Ok3udPYZ0wgP7EtNVOPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرطرفدارترین رشته‌های کنکور ۱۴۰۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/696317" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696314">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFSCFYD3-__h4BzOt4dINIILD9I9XtBUQvz4obAmW-Uf3fYddjJR2qmTFBZtAcpdE8pHldA4Y-RkJpsQtFWip1reLyVr0eK-yAEthfrWPUBeSs3afdXpxw3WeXnGAitWqoYwYNA1F9emDH2AhtM4pwl3o9tMJp5OH0JnGFgxWkk9JaV_6Vskbkmf49gH8EtCSeaXVZlxwY0-6BtgSoQJS9aQ0DCFyY3qWFVAFUb3jC8pbidqGmY70xrIo3NeA0yqg90jb6B3hVxJqVe7NMevkdeQ_8y70NAO8F6Gq1PUG0SsPkGowiCNjzHNZ8N8HAkB2fxBdT1VWtQ67jVvOFAjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
برای ویزیت حضوری دنبال پزشک می‌گردی
؟
توی اسنپ‌دکتر می‌تونی پزشکان مختلف تهران رو ببینی، اطلاعاتشون، تخصص، آدرس مطب و شماره تماسشون رو بررسی کنی و برای گرفتن نوبت، مستقیم با مطب تماس بگیری.
👨‍⚕️
پزشک و تخصص موردنظرت رو پیدا کن
📍
آدرس و شماره تماس مطب رو ببین
📞
برای ویزیت حضوری، خودت با مطب تماس بگیر و نوبت بگیر
اگه دنبال پزشک در تهران هستی، از اینجا شروع کن
👇
https://drsnp.ir/v7wU3LNSk</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/696314" target="_blank">📅 11:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696313">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIgwUodgkQoD0bxiNPQ4pEqJum9YLkpEgG4GwNtciaypNI_Mk_mwfJSPDB-TtAcnJx_YE0A5ukgkEFFEpzg5Q3feoGXh6K1Hnga3V-PyZ0qswTUpR4M2OSDgAUbSGMUY4ozP4yikJ-o9zftOZII5htHepwaqU1Q26OOzU6mIVruJmn_Dn-_2Cqro8dVO5FO8jGUUN0o20sJf8jOlrn7ngmvisPMj7bTupPLJ-EHO0nDFRrltfHVPWrnlkuziETzd6vGhiUJeToITLeqbJzOHfT6HU_ly5iTAygd_bYpUT7ABSIVjdLTaseOIFlmtS1KkXo2ABEY1Tyw89oW2lRHMug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهره‌برداری ۳۲ هکتار از کلان پروژه بوستان کرامت مشهد
دکتر مهدی یعقوبی؛ معاون محیط‌زیست و خدمات‌شهری شهرداری مشهد:
🔹
امروز بخشی از کلان‌پروژه‌ بوستان کرامت با مساحت ۳۲ هکتار و با ۸ باغ موضوعی ، با ظرفیت‌های مختلف و امکانات و تجهیزات مناسب برای طیف‌های مختلف مردم، در اختیار شهروندان قرار گرفت.
🔹
افزایش سرانه فضای سبز منطقه ۶ از ۶.۲۱ مترمربع به ۷.۵۱ مترمربع
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/696313" target="_blank">📅 10:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696312">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f7132483.mp4?token=XyDLtMIH5WHl4cHazmGzS1kfYuMInMcna-uy5z_7PSB7_xSufjbPHjrzOyu22cAW7L0CLqhUw8k8WJd2TCa3EUXmVoGushD-jPbLi1o9BV9QBpEjXyqbYr2jRv3HXTE7LzmN_I7XkYfbNkCI6q57PAPdJS4EMqhJ1bnaTiSPk0pWxuge99toRI2xBwoD-Jri37v-NOnS1g9v5ECp9uLia9IoBN4LBO2qT7CngtzZ9tqklN7UmsD1w14ww4RUA4eqa8viprmVrZA0zBXoAxyAuwBPSGbQBOeYFiStF9mVJQx4Ql3xEq86AlCPMnMQj8OP6vECAOH0q_Drh5-dOgUOIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f7132483.mp4?token=XyDLtMIH5WHl4cHazmGzS1kfYuMInMcna-uy5z_7PSB7_xSufjbPHjrzOyu22cAW7L0CLqhUw8k8WJd2TCa3EUXmVoGushD-jPbLi1o9BV9QBpEjXyqbYr2jRv3HXTE7LzmN_I7XkYfbNkCI6q57PAPdJS4EMqhJ1bnaTiSPk0pWxuge99toRI2xBwoD-Jri37v-NOnS1g9v5ECp9uLia9IoBN4LBO2qT7CngtzZ9tqklN7UmsD1w14ww4RUA4eqa8viprmVrZA0zBXoAxyAuwBPSGbQBOeYFiStF9mVJQx4Ql3xEq86AlCPMnMQj8OP6vECAOH0q_Drh5-dOgUOIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرود اضطراری هواپیمای سافاری در تانزانیا پس از برخورد با یک گورخر
🔹
یک هواپیمای سافاری حامل گردشگران در تانزانیا، به دلیل برخورد با یک گورخر هنگام برخاستن از روی باند، مجبور به فرود اضطراری شد. هر ۲۶ مسافر و چهار خدمه پرواز به سلامت از هواپیما پیاده شده‌اند و هیچ‌گونه جراحتی گزارش نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/696312" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696311">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdE20Hx-RqhD2R63as4UD-0FLs6uFd7Dpoouuabu9CtLWn061_Jn0P39C8I9MR2wNzdSsnIxzDHR5CKOSN-QGd6k0RDg1jYm2naiD-mT_phxqYtaBUG8Kvn__vGHJO5CdLbMPNRaO_UANr8Fny4SL8kivjfTK353X6roBnU_gD_oY9MdusbEih61bdxBP8Q_wf1H_gEy_yHZAPMBe7ft2OZj61hwqMBGPwVlp0Jxx1gddCqHGduQJsYPO1Wwxudi0mEOiWKPvG2f7zH40O0v66K5518heVGVcPVUN91tSxJ_DHj76N_ptxsvOJDpIxE9px52AYQyAAue7juMfPeW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از پاییز روستای گنبک، رودبار، گیلان
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/696311" target="_blank">📅 10:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696309">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y-cMnUBuoKzgeHBrEuPqTtIHCP6aU6QhHoNhFzbFlcRMWFe0DB7A5RZlIjTLmhTAFQFPzjzX1V8xDUC9g_-41tCoBUvKPF_APvRcwKVt943aihBETrS_slHHz4BFXEMotSWecnv7VhevfgWFeEO83pdZvnKnPmCv0jIMkNVd7-5tUqPFclRMSCOjt5PjwTVGgMU_GVK-bpqcsLFI0nZQIgYYy7V-LoRFZM-BlGYJwew66z-R3s4Iov1b9n5hhIAjQuR84m-Bn05LPeOtMXRdvPGAJ6MS4wUYDk4SArvaCzNFD_mIWD6yLYyqxLYruY8mEDEyIH_EKQ9n5wEx6ktzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JbFZl4PA3Fa7YOt6KwuKvDgnLaLOF15gqKkn3wy5LLyeK0n8kDneTNYcXl38sAhbWojQJJeeY-AYn5sb-aykqVXD9SDohDWKByEjq7R0fNmY0iCiM4auqRqtJGfm3597j_ve2tNI0XoefDkivoK2G4m9eSoZEd1VlTBbI5e08TF1wVjxUIYTxcmKfX5AUPY1_C-JnRAikbSHhAm_eGG7sxSl_Ve0iADcyukUpIe7IDlxYlr0xkiMgP81jSAqQiVT_2d28-VAX8U2UybeaPdJZ3mCU22P6GOQSdmlYbfAjFoDA6Ok3RqHWMY8Q99fA0mkZfSZxiLzoO5BIcuhiTPxYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گادی آیزنکوت شانس ۵۲ درصدی برای نخست‌وزیری اسرائیل پس از انتخابات امسال دارد، در مقایسه با ۳۴ درصد برای نتانیاهو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/696309" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696308">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nRnyMsFerRYQV0bGQn3mAZ11Ngh4njqPyLBUX3NU08t9s6FRCrVFmRT0Yl9a4SPQJRIW0H0ZTHsNiXfSPt7qhwQd5qxFy0wxAFhMz3AS2C3Rn5ZcCHw96whuqV3BPPhPXVQ09Dnhxhnw6Kx3VBqCcJBj1MNO60FofaJqjATrHBRiutMDpJ-uaY0DsRyX6dl5JTsy_xWrgSkqJ0jZXDM_DRcnkUVbELuMUIX8gESueZ2Y6UIPc_xlpT0zLkXeb9xIqIjRn2Jqhs1JfgZVyvxHfSAu-lcKuftUQplMhPJycjU0Tb7hkcCDSQwRhHI6QkH9RMgiyBguih3-laWTkK5FBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حامد بهداد: از خانواده شهید عذرخواهی می‌کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/696308" target="_blank">📅 10:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696307">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
بانک مرکزی افغانستان در گزارشی خبر از شکست دلار توسط پول ملی این کشور را داد
در این گزارش آمده است که:
🔹
سال ۲۰۲۲؛ ۱ دلار = ۹۰ افغانی
🔹
سال ۲۰۲۶؛ ۱ دلار = ۶۵ افغانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/696307" target="_blank">📅 10:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696306">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fc0faa3.mp4?token=kr-6-fvLky4C4T7wb2BatqnSjHId4dxsvGLzlo9RVepjZy53GsdGejPJvrP_ZtrTLhNea07qsD19rXBVU8PFFtZ78yEcvbcsnfCRuOR-_4fxusBMJfMKqiAxsV5A98xh0QhwUEkzvEoe0bug_rkwIFMFO4AJ6xJaB9MSK6L0K3CrhqPOesHPIj3Co29r2hzcJNBkS237tT29VDyrkAEk6dzMes50miBH7f4cmS1WDdfq0hc1w-V8ORIeLGlOIJblLXJcrxJ96gnivDhiG6LYMasPndHRZ7po90Avk_UKDBeRKtx-O1W5rEDkAfHJVcPZbwCdtmejhsvc6FUoJej8oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fc0faa3.mp4?token=kr-6-fvLky4C4T7wb2BatqnSjHId4dxsvGLzlo9RVepjZy53GsdGejPJvrP_ZtrTLhNea07qsD19rXBVU8PFFtZ78yEcvbcsnfCRuOR-_4fxusBMJfMKqiAxsV5A98xh0QhwUEkzvEoe0bug_rkwIFMFO4AJ6xJaB9MSK6L0K3CrhqPOesHPIj3Co29r2hzcJNBkS237tT29VDyrkAEk6dzMes50miBH7f4cmS1WDdfq0hc1w-V8ORIeLGlOIJblLXJcrxJ96gnivDhiG6LYMasPndHRZ7po90Avk_UKDBeRKtx-O1W5rEDkAfHJVcPZbwCdtmejhsvc6FUoJej8oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ایده فوق‌العاده خوشمزه و خاص برای چاشت مدرسه
😋
#آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/696306" target="_blank">📅 10:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696304">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f17eadaec.mp4?token=G2hjKlqBFWqd3JmorZXFEnv9aNMoBfKZjZeVfMtvto8hE_c9MsqL1xTh92R246C16CkaCZRM59STndXOy34i5Fv_zZ7mtmZwugeaUPFHZlvzsF563tu2actd_XhBrZX-xZVcxxYuo7l8pAxqOwvmdnSI1qij2txFdbSxMiI4LB-7a5z3oLJPKK_ssDg0ALxHRbOYuLmRsJn-lspb9RoPE41kLM-xfEbmosEU3jqOloSDcMHLPylMoLPbaGF3bTUXw0XrLE3gWQuaAZ33ZPYzCHj9tZ8L07nsJufxmQ5uazpOURr3u03lmb_RT6__J2Gs9x_byDHpqpBUFBP401MSwYWOgoFLMLH7LZ1o11-hqHFYpSRALey0OzmrvpDBdyfnUGxvgvXo27WSp-kmoQOPf_nZGHn6LXIBPK6TUBletkAeBoGg8QqsdE9NEt3QA4NInxfjTVZrBtdLl7b0wEJdSuNlfNgufJN5HBwxm-l6fM0QMzOtu8x2hXgBgMq9tG38wA7RRrUlR_GvkxDukFftK_Filv-m4J3lfVrwIqFQt6ZYesyyhQsTYOS4LqQfA8joc2fYqZy6fh6MIXP6wKbFHNrdsOijL4GXYhVirOrsrrsU37pxN2u25-oln1UblYj7memeZohgGjOj8FT_jtoR0h9_oRfpDKD_bIXx_Zo9N3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f17eadaec.mp4?token=G2hjKlqBFWqd3JmorZXFEnv9aNMoBfKZjZeVfMtvto8hE_c9MsqL1xTh92R246C16CkaCZRM59STndXOy34i5Fv_zZ7mtmZwugeaUPFHZlvzsF563tu2actd_XhBrZX-xZVcxxYuo7l8pAxqOwvmdnSI1qij2txFdbSxMiI4LB-7a5z3oLJPKK_ssDg0ALxHRbOYuLmRsJn-lspb9RoPE41kLM-xfEbmosEU3jqOloSDcMHLPylMoLPbaGF3bTUXw0XrLE3gWQuaAZ33ZPYzCHj9tZ8L07nsJufxmQ5uazpOURr3u03lmb_RT6__J2Gs9x_byDHpqpBUFBP401MSwYWOgoFLMLH7LZ1o11-hqHFYpSRALey0OzmrvpDBdyfnUGxvgvXo27WSp-kmoQOPf_nZGHn6LXIBPK6TUBletkAeBoGg8QqsdE9NEt3QA4NInxfjTVZrBtdLl7b0wEJdSuNlfNgufJN5HBwxm-l6fM0QMzOtu8x2hXgBgMq9tG38wA7RRrUlR_GvkxDukFftK_Filv-m4J3lfVrwIqFQt6ZYesyyhQsTYOS4LqQfA8joc2fYqZy6fh6MIXP6wKbFHNrdsOijL4GXYhVirOrsrrsU37pxN2u25-oln1UblYj7memeZohgGjOj8FT_jtoR0h9_oRfpDKD_bIXx_Zo9N3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بی‌احترامی تماشاگران سعودی به سرود ملی امارات در فینال یک تورنمنت بین‌المللی
🔹
هواداران عربستانی شب گذشته قبل از فینال یک تورنمنت فوتبال در جده، سرود ملی امارات را با سوت و فریاد همراهی کردند.
🔹
خالد عیسی، کاپیتان امارات، به وضوح خشمگین بود و طبق گزارش‌ها، هنگام پخش سرود ملی فریاد می‌زد: «شرم، به خدا، شرم».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/696304" target="_blank">📅 10:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e90115f95d.mp4?token=JFnQkqhc06oTAbEDV1A7RvKoF6-Ljq6vg8__UEn4QOlr4nHceFXJf-10TLNYZYxgsvx2tLpsTX_cpULXvOtIf_RhynfrbZ66ELgcxx8WCtbuVLn835uIxnEA_Jbm-vJWYhP8Ye6_8tqYdi9FiU4hXxc3NME7jSLRwbyY0D-1JD0xDhAFanH5-8TXOkNug7icjD0TPZnlMIjYey687DycMtY1PSwpHQ51ewswjOFM6wv1mxPXlYIgfd3IfQmCFfklyeNLYu5qWy_CtUx4OFWBU_IuIj8YIUziC3gpaIswkxWHT0IMJe-GgsbNc4LpnN3HCBhZ0L08nAUC2OxMXf97ZXmKx7eB4uNthTcDgEPeBIzAlSvk3tqnwDrjD7ZRIH-VsJom0wzn39aoMJ3UjolxmTojpyhRfgL-xLvik_4TijBKSRlaR3xd6Ov0lHOe-rVeogjS8ZtQ2uVue00PpZSkz9TbxdN9dHgvMzMxBzCIC5V2k4mHO35b7PI-zsIbDW_mo1O453u1nBveQOavYfi501IJaBTjYULnhZ_y_Mu4o-kXQM09xKPYAG2JtHihLAaQKRHbe6yjXROAvOLz2nF9tljO2cstOtT3ALJHeu5Afa1yUx8kSBOc3kwySJlq_GbTd1vVXXvq40b_iTxhaxe0VG250yoYCdh93JDrdqRgA1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e90115f95d.mp4?token=JFnQkqhc06oTAbEDV1A7RvKoF6-Ljq6vg8__UEn4QOlr4nHceFXJf-10TLNYZYxgsvx2tLpsTX_cpULXvOtIf_RhynfrbZ66ELgcxx8WCtbuVLn835uIxnEA_Jbm-vJWYhP8Ye6_8tqYdi9FiU4hXxc3NME7jSLRwbyY0D-1JD0xDhAFanH5-8TXOkNug7icjD0TPZnlMIjYey687DycMtY1PSwpHQ51ewswjOFM6wv1mxPXlYIgfd3IfQmCFfklyeNLYu5qWy_CtUx4OFWBU_IuIj8YIUziC3gpaIswkxWHT0IMJe-GgsbNc4LpnN3HCBhZ0L08nAUC2OxMXf97ZXmKx7eB4uNthTcDgEPeBIzAlSvk3tqnwDrjD7ZRIH-VsJom0wzn39aoMJ3UjolxmTojpyhRfgL-xLvik_4TijBKSRlaR3xd6Ov0lHOe-rVeogjS8ZtQ2uVue00PpZSkz9TbxdN9dHgvMzMxBzCIC5V2k4mHO35b7PI-zsIbDW_mo1O453u1nBveQOavYfi501IJaBTjYULnhZ_y_Mu4o-kXQM09xKPYAG2JtHihLAaQKRHbe6yjXROAvOLz2nF9tljO2cstOtT3ALJHeu5Afa1yUx8kSBOc3kwySJlq_GbTd1vVXXvq40b_iTxhaxe0VG250yoYCdh93JDrdqRgA1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمیشن لگویی، این بار ۷ اکتبر را روایت می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/696303" target="_blank">📅 10:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
انتقال محموله مواد منفجره به مشهد با تماس مردمی ناکام ماند
فرمانده انتظامی خراسان‌رضوی:
🔹
در پی تماس یکی از شهروندان در یکی از شهرستان‌های خراسان رضوی، خودرو حامل محموله‌ای از مواد منفجره قبل از ورود به مشهد در فاصله ۱۵۰ کیلومتری این شهر توقیف و مواد منفجره کشف شد.
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/696302" target="_blank">📅 10:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696301">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a451b7817.mp4?token=db0QQ_gOCVJspjhFLB0hrO5gv4R64MxaZmDZpkGg_fG8PUrYqZbZ0dCMns-vFesfzZAGAtQN0dSAIMVpdsZpqcmYdtN_TgWVwmBwDDW_I6HoOkZ2zGxoJTWsojmeAvIesaqOeX5Du3iUlWpzeC3p4TRECQC-L-ZdwAT2ocAMD7byhM6U-7LKKZrJJFKqxrwioQBi6xw8RWhCVnewtrfXm_bamUpRMujs9MKGFlXeq-T23kPT_F1_Rf3fHZrLDkneO3aea7jbByQHFBy4EJFWp9-rymcbzWPGaFimIUph7BC1teGhiWSScQ_LgHLzxfjNxwizBJvsaWAM53D9JkUzFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a451b7817.mp4?token=db0QQ_gOCVJspjhFLB0hrO5gv4R64MxaZmDZpkGg_fG8PUrYqZbZ0dCMns-vFesfzZAGAtQN0dSAIMVpdsZpqcmYdtN_TgWVwmBwDDW_I6HoOkZ2zGxoJTWsojmeAvIesaqOeX5Du3iUlWpzeC3p4TRECQC-L-ZdwAT2ocAMD7byhM6U-7LKKZrJJFKqxrwioQBi6xw8RWhCVnewtrfXm_bamUpRMujs9MKGFlXeq-T23kPT_F1_Rf3fHZrLDkneO3aea7jbByQHFBy4EJFWp9-rymcbzWPGaFimIUph7BC1teGhiWSScQ_LgHLzxfjNxwizBJvsaWAM53D9JkUzFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر تیروئید کم‌کار دارید، این نکات را برای کنترل وزن ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/696301" target="_blank">📅 10:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696300">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d6d557b6.mp4?token=UbmV0fGJN6YPgF6MlAYPrhYDn_0APnbxf-Kmzd9YCS8hqL_oWzdVX7e3GNQlMB1vIYyZIs5uWI3Gvf9qkd3nKlfx8bMLAPDiQOt9xwXPs9-M5gLUquBbiteBnMVHGwhNe12kvCeH7GwAM0tv946ZmlMssaH9_rH5bFyP5dkTHbZe9NcSNNmEa2Y10NGq6IRE3H_Zj0NChlrjjZS3Cf3HMRMebYTEPGq0oFDndhKUzWbjBR0_fwAAqLDch4SOAJ0-G6kqdl482W1HfKd09r0lunxuizQ783oNvFfrt8DoRlYKpVJiKfbKlH4PAXj5UGeMaxeCVy3ghg-1AhVYIk0xE6u0CSiM_vQu3ruuwD7CMRLGVDGIS6bHHvyn76Hjf5eZOUFPeFBf_wDEjvSRzAZRAUM614ZtU12whZ9Gq5a1iHiEhcreANH83FJJ2VmDht8n8xTWOpeFzXHRtCGmb_g8RciUvWdR-4dONx77IC_qYcGu2ugLPXP7zAypjyqc8miWkOHxVyVqJW3ZDb3e3AFBiYElKtuvWHi-6p0rUqs-RqBdwYhKjeRRb7L5SdT1OaJy8i_2xMHyV2lFaqcpay94pBRaFRlO9eNQEh-octmFFuQx77vzWPGMKofFr6Z3gV4VIKmkmkzDfhqLX9PMXhruu1akyuxuSggdqYCAaVYOk6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d6d557b6.mp4?token=UbmV0fGJN6YPgF6MlAYPrhYDn_0APnbxf-Kmzd9YCS8hqL_oWzdVX7e3GNQlMB1vIYyZIs5uWI3Gvf9qkd3nKlfx8bMLAPDiQOt9xwXPs9-M5gLUquBbiteBnMVHGwhNe12kvCeH7GwAM0tv946ZmlMssaH9_rH5bFyP5dkTHbZe9NcSNNmEa2Y10NGq6IRE3H_Zj0NChlrjjZS3Cf3HMRMebYTEPGq0oFDndhKUzWbjBR0_fwAAqLDch4SOAJ0-G6kqdl482W1HfKd09r0lunxuizQ783oNvFfrt8DoRlYKpVJiKfbKlH4PAXj5UGeMaxeCVy3ghg-1AhVYIk0xE6u0CSiM_vQu3ruuwD7CMRLGVDGIS6bHHvyn76Hjf5eZOUFPeFBf_wDEjvSRzAZRAUM614ZtU12whZ9Gq5a1iHiEhcreANH83FJJ2VmDht8n8xTWOpeFzXHRtCGmb_g8RciUvWdR-4dONx77IC_qYcGu2ugLPXP7zAypjyqc8miWkOHxVyVqJW3ZDb3e3AFBiYElKtuvWHi-6p0rUqs-RqBdwYhKjeRRb7L5SdT1OaJy8i_2xMHyV2lFaqcpay94pBRaFRlO9eNQEh-octmFFuQx77vzWPGMKofFr6Z3gV4VIKmkmkzDfhqLX9PMXhruu1akyuxuSggdqYCAaVYOk6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زد و خورد و درگیری در پارلمان ارمنستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/696300" target="_blank">📅 10:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فروشگاه و رستوران خود را با هیوا سیستم هوشمند مدیریت کنید
از صندوق فروش و بارکدخوان تا ترازوی دیجیتال و گزارش‌گیری لحظه‌ای فروش؛ راهکاری جامع از نرم‌افزار و سخت‌افزار فروشگاهی، برای مدیریتی دقیق و حرفه‌ای.
📞
۰۵۱ ۳۶۱۴ ۲۲۱۲
📞
۰۹۰۲ ۴۲۹ ۳۳۲۲
🌐
hivasys.com
📍
مشهد، چهارراه ورزش، مجتمع ایلیا، طبقه اول، واحد ۱۳۸
مشاوره رایگان تجهیز فروشگاه و رستوران</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/696299" target="_blank">📅 10:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/696298" target="_blank">📅 09:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696296">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
خواستگار ناکام، قاتل زن جوان و همسرش شد
🔹
مردی که سال‌ها پیش خواستگار زن جوان بود و پس از جواب رد، بارها برای او و خانواده‌اش مزاحمت ایجاد و او را تهدید کرده بود، به خارج از کشور رفت اما پس از بازگشت و اطلاع از ازدواج این زن، تهدیدهایش را عملی کرد و او و همسرش را مقابل چشمان فرزند ۸ ساله‌شان به قتل رساند. حکم قصاص او برای قتل هر دو نفر در دیوان عالی کشور تأیید شد./ همشهری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/696296" target="_blank">📅 09:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696295">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICc2eMHOfMU-6eJYGGyMNYK0r6y_aIUnTMYNCmwDZfyISvWTL6dyXbhJTye_RCiCFPe6TpVKlMfDc43ifKmclq4Ozxg_VRGK_MMjLz9wRZC_YSdtV2x3egI8cWMRLnfhRUy7Qwg9HJVHNNtKayiF_FCJQZbrbrGUA1wM18HRjU7qMS_Im4Ql33vfFMCy_z2MMbAVLStik1n2hAlDQRINvHqLutgvs4HWe4w0owOoz4QkQsfpyj1-HvvhGb9mjZ0RfU-fymMI1PB5MjIGADiN6miLGnA9BGneX6GOzvUmevuxcW2ShsnH_3rUiWPIhJaseRmVZX-KXl8pMTAsOGfyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر آردی برای هر شیرینی مناسب نیست؛ با انواع آرد کیک و شیرینی آشنا شوید
🍰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/696295" target="_blank">📅 09:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696294">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4hS0KT3HvUgkjygFSjtmah880tWzza-rrjKSnr6m1hcWDjKCbnicmpzYuxp2U7_glZz1z4w1HXCu3G2RNenlItSodmqdxklmlyHmNa91TxOSK4nSqVo534HGNb0gWBPQGVp03wCH2MF8PnvOTeudMLZ7mF9Jl8Fr-ZeGvM1LAz3DizspVEZp3E39ieEKEmjAGz9tXnb6OHXdISEIrisEovvCsVopAIOk22_PhXMGurxbzdK0zT4ANeZ-zIDLl6bd-iEru4rJB2v7oA-fpExnAAhsd6Oc7zp1iHJWUUwOqryc_jzNevBcPIfRP7RUSmdxcmEdn8_hNiQvCkS11w3iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار عجیب افزایش تعداد مساجد در بریتانیا از سال ۱۹۵۰ تا ۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/696294" target="_blank">📅 09:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c3d132d7.mp4?token=CrtTPXDhLyPSf_KivMdRTaQ_yQnzc4asW37deMyStdpONEE_NEqM4tftrXdk_YDpieilZjAeG5EDpfH2kzUf3atlR5qU2yU_gISYT39nqg6tLKzHtfJLHjk_pFN9C_v6eDzUQENZvNVyBuJkYweG0DOTUM5ClKTWW1nOOoZVxiOBcJGT25QGDfyRuWXICw4OJbPbfGBNX-mu_qr9FAvBIUoDyZb-7-7ZWQmqPgaeTPEWUd9v74wFqLu6LwnHJJoDUu7k4xjcft-kfcZ6K255pMXHBMetcaYTE7i6W1e-ytetnYd9mydURNNCohAKMGMO-1Z_cQ2UWdbGhMz6GIS42g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c3d132d7.mp4?token=CrtTPXDhLyPSf_KivMdRTaQ_yQnzc4asW37deMyStdpONEE_NEqM4tftrXdk_YDpieilZjAeG5EDpfH2kzUf3atlR5qU2yU_gISYT39nqg6tLKzHtfJLHjk_pFN9C_v6eDzUQENZvNVyBuJkYweG0DOTUM5ClKTWW1nOOoZVxiOBcJGT25QGDfyRuWXICw4OJbPbfGBNX-mu_qr9FAvBIUoDyZb-7-7ZWQmqPgaeTPEWUd9v74wFqLu6LwnHJJoDUu7k4xjcft-kfcZ6K255pMXHBMetcaYTE7i6W1e-ytetnYd9mydURNNCohAKMGMO-1Z_cQ2UWdbGhMz6GIS42g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور فشارخون را بدون خطا اندازه بگیریم؟
🔹
روش صحیح استفاده از دستگاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/696292" target="_blank">📅 09:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696290">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473e037d06.mp4?token=tkvo5KrXEDJeTSKuGbkt-bmDHVSUA0-8Ga2FfD-xDBqr463RqVp2SlWzOH4lPjcR8X4vG3orL3r-mgYs5YwJ_BAT2WQtEW9KX3qLkam_vPyk28fZ63FvY9vJJNNagspmx5yxhGnB0zQiV4GzYrlKfk1OYjG_6u-EhE1IfBi0yIZImGbxxyYBN3MKO9-MvsE1MzncbJw3CY6oZZPAKUoyzAGrGziVYeZItdwRM5hUU55Fe5cqND-BaiYGlvV3n4riLXsSBkTeXfJ2i9bqjHXMu97b0JGI7AkEjI1fgv6xESxawBfNTlIgWHbiWK1IFOiW07DkYt0wIW6Z0yFlsr6kQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473e037d06.mp4?token=tkvo5KrXEDJeTSKuGbkt-bmDHVSUA0-8Ga2FfD-xDBqr463RqVp2SlWzOH4lPjcR8X4vG3orL3r-mgYs5YwJ_BAT2WQtEW9KX3qLkam_vPyk28fZ63FvY9vJJNNagspmx5yxhGnB0zQiV4GzYrlKfk1OYjG_6u-EhE1IfBi0yIZImGbxxyYBN3MKO9-MvsE1MzncbJw3CY6oZZPAKUoyzAGrGziVYeZItdwRM5hUU55Fe5cqND-BaiYGlvV3n4riLXsSBkTeXfJ2i9bqjHXMu97b0JGI7AkEjI1fgv6xESxawBfNTlIgWHbiWK1IFOiW07DkYt0wIW6Z0yFlsr6kQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین گل و آخرین خوشحالی مسی با کیت آرژانتین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/696290" target="_blank">📅 09:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696289">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efedb8b034.mp4?token=cRJ_YlFEO1GHzpUCQjIc3pYgIelEuPNA7zmpUhY29DpArka-aVYfEhwnJLfX_Pu9UoMGg-ZBDSxoeGvnBEscE_UX3qQb451GiJ-FUbEo8yQ6wF8Js-tL_VGkZAx_uzgpB6o3OKfwKzHi7hhQ6Kwup18f6WXRWpx9pQabljilIHp1A5V0L-RQ99evRSzPikhhrR3LaLqDMN_mFTScAvBE77ndy66L0P3iib5pus5qlC0MYVZEv-LmNJ7f4ZjUi89qqIuIwsZEu5peVYi3V7pUjd6yRyLNKMA8jm45-me4AlfRIZq6sbjz7E2RVHHPFjXikQ89vXb9YLcEsbmUdHzkHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efedb8b034.mp4?token=cRJ_YlFEO1GHzpUCQjIc3pYgIelEuPNA7zmpUhY29DpArka-aVYfEhwnJLfX_Pu9UoMGg-ZBDSxoeGvnBEscE_UX3qQb451GiJ-FUbEo8yQ6wF8Js-tL_VGkZAx_uzgpB6o3OKfwKzHi7hhQ6Kwup18f6WXRWpx9pQabljilIHp1A5V0L-RQ99evRSzPikhhrR3LaLqDMN_mFTScAvBE77ndy66L0P3iib5pus5qlC0MYVZEv-LmNJ7f4ZjUi89qqIuIwsZEu5peVYi3V7pUjd6yRyLNKMA8jm45-me4AlfRIZq6sbjz7E2RVHHPFjXikQ89vXb9YLcEsbmUdHzkHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به اهتزاز درآوردن پرچم فلسطین در جریان اعتراضات دانش‌آموزی در فرانسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/696289" target="_blank">📅 09:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه هفدهم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/696287" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه هفدهم؛ فتح آشکار
🔹
خیرات‌ و حسنات برای نیاکان منجر به اصلاح گذشته و جاری شدن خیر در زندگی می شود.
🔹
جریان هستی بر روی محور شدن پیش می‌رود وگرنه احتمال نیستی و نشدن همواره از احتمال حیات و شدن بیشتر است.
🔹
به میزان ناسپاسی و سبک زندگی غلط انسان از فرکانس موج هستی فاصله می‌گیرد و دچار بیماری، افسردگی و حتی میل به خودکشی می‌شود.
🔹
در نور المقدم و الموخر، سرنوشت سالک درفرکانس اقبال قرار می‌گیرد.
🔹
قرارگرفتن در نور المقدم و الموخر، منجربه اصلاح گذشته وترمیم آینده می‌شود.
🔹
نام‌های المقدم والموخر در نقطه‌ درست زمانی و مکانی انسان را در صراط مستقیم قرار می‌دهند.
🔹
استغفار،خویشتن داری و زیستن در اسماء الهی انسان را از محاصره گذشته وآینده نجات می‌دهد.
🔹
با تابش نور المقدم والموخر بر سرزمین‌ها، گذشته‌های تاریک، پاک می‌شود، آینده و سرنوشت در خیر و نیکی رقم می‌خورد و همه‌ تصمیمات و عملکرد‌ها در فرکانس اقبال قرار می‌گیرند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/696287" target="_blank">📅 09:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNR0fWib54-zDh3teHng4BdYAaJWsxbvxAYuy9Y8jEQM2FLEtu4ASsgh_SPZ6-h_Jg6QRB0nz9AVR5eToofMTkBYIFcimA1WPNJ7GJ13Eatxfu0mVybAF0rj2VaJI9Oj1VS7UaTLYBwctnjdGM1Y8D8A3YngvCfAJgGizMxNQh9zvcQ-AA2UGvfW8aLtylF8vpMgoN2pjjpk5fsiW6L8vJ3qnBegvS7naC_494VINy55Cv4fW3FBVzClw3C8wmQlRzhsAZQJW3IDYTAbxfvj9CvFnhVT69JivaXRBevMxRPRzukCt3GAULFVtKG4C3f7fUTo6K25cHSSOa32pbKh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبری‌که همه‌منتظرشنیدنش‌بودن
❌
پژوهشگران موفق شده اند ترکیبی را معرفى كنند كه مى تواند سلول هاى بنيادى فوليكول هاى مو را از خواب چندساله بيدار كند
😳
😳
✅
این تحقیق روی ۱۰۰۰ نفر تست‌بالینی گرفته شده و نتایج فوق العاده در قطع ریزش و رویش مجدد داشته است
✅
🔴
حتی روی کسانی که ریزش‌ارثی هم داشتند اثرگذار بوده
رویش مجدد مو به همراه دارد
🧬
در حال حاضر در ایران این روش بالای ۳۰۰۰+ نفر رضایت‌درمانجو داشته
به زبان ساده، موهاى خاموش را دوباره زنده مى كند!
دریافت اطلاعات کامل و نحوه و هزینه درمان
روی لینک واتساپ بزنید
👇
https://wa.me/message/R7FMNSDOGSIXC1</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/696286" target="_blank">📅 09:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
رئیس سازمان ثبت احوال: تا پایان پاییز کارت ملی همه کسانی که درخواست المثنی دادند، به دستشان می‌رسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/696285" target="_blank">📅 08:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696283">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f505847526.mp4?token=VsXb6JOUudYr8_uhAGWCLx9FDxq3TbDy_GF4qarQBWt6E4hucgPNo7izE5O8nX4WMKU6mPoYbNcaiQKkDPI_BjNUQZytwgUXWKFe8kp2tfQ7M6F0N0UkY__PQ75MOdNMlk963MLAUJiAd7jbfqra0ldtuBlp_H45lriHMymx2FREpGgWEYnn4wlC0OBqzvQvndK_UdnQKyWyH_d7uTYfVldvbYy7E-d_xFsEejsbE1La22q8eKStjp-EL99rZwVS2yScTTV-Hbk4gyDlzxSdA2AHi-WivdaK9HsNdinP6INGpIPszgVAq59jct6vlokb3lzIrdPZpaIAMl2ZXByPQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f505847526.mp4?token=VsXb6JOUudYr8_uhAGWCLx9FDxq3TbDy_GF4qarQBWt6E4hucgPNo7izE5O8nX4WMKU6mPoYbNcaiQKkDPI_BjNUQZytwgUXWKFe8kp2tfQ7M6F0N0UkY__PQ75MOdNMlk963MLAUJiAd7jbfqra0ldtuBlp_H45lriHMymx2FREpGgWEYnn4wlC0OBqzvQvndK_UdnQKyWyH_d7uTYfVldvbYy7E-d_xFsEejsbE1La22q8eKStjp-EL99rZwVS2yScTTV-Hbk4gyDlzxSdA2AHi-WivdaK9HsNdinP6INGpIPszgVAq59jct6vlokb3lzIrdPZpaIAMl2ZXByPQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از صاعقه در آسمان دیشب رشت
⚡️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/696283" target="_blank">📅 08:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696282">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
یمن: با موشک بالستیک فرودگاه عدن را هدف قرار دادیم
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای اعلام کردند که با استفاده از موشک‌های بالستیک، محموله تجهیزات و اقلام نظامی عربستان را که به اردوگاه «بدر» در مجاورت فرودگاه بین‌المللی عدن رسیده بود، هدف قرار داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/696282" target="_blank">📅 08:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696281">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039dedd4df.mp4?token=Lj89p6FoxyfgAKVTIaAxyYglC9PBA6KqyiNvs0els7TWwz39PvIRNr--1mkVxWTCUh1mtXaNy_KlvdbrMq7XRwp1STpyXQrxfHynyTlgM1uCV0nrqAHxN8PXN2iLQbJzPE-JDGuXl6lWVmUoClZFDtJf7LQ_3x0tq_IYjNTREq3stLmfoohFg25xaMv0YIbelSwaVdCoynyKT4PQQrftLvyMv5sYCMmK7sxrxWca4xPIoitfgZSlMMLv3OtkazBDVUWRi74e3Bi8tkQPEDISPKkIyXwjJaN8USNs58BAbtodu5j7TeLeKXzsBfzZccqH4nb9zUoJyWSng8kkx2mvrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039dedd4df.mp4?token=Lj89p6FoxyfgAKVTIaAxyYglC9PBA6KqyiNvs0els7TWwz39PvIRNr--1mkVxWTCUh1mtXaNy_KlvdbrMq7XRwp1STpyXQrxfHynyTlgM1uCV0nrqAHxN8PXN2iLQbJzPE-JDGuXl6lWVmUoClZFDtJf7LQ_3x0tq_IYjNTREq3stLmfoohFg25xaMv0YIbelSwaVdCoynyKT4PQQrftLvyMv5sYCMmK7sxrxWca4xPIoitfgZSlMMLv3OtkazBDVUWRi74e3Bi8tkQPEDISPKkIyXwjJaN8USNs58BAbtodu5j7TeLeKXzsBfzZccqH4nb9zUoJyWSng8kkx2mvrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آوازخوانی ترسناک هوش مصنوعی الکسا در خانه کاربران!
🔹
اسپیکرهای هوشمند آمازون اکو مجهز به الکسا پلاس دچار اختلالی شده‌اند که در آن دستیار صوتی در میانه‌ گفتگو با کاربران به تکرار ممتد و حتی آوازخوانی عبارت «لالالا» روی می‌آورد. نکته‌ عجیب‌تر آنکه الکسا پس از پایان این رفتار، هیچ آگاهی یا خاطره‌ای از عملکرد خود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/696281" target="_blank">📅 08:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696275">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFrZ8286-9dEssgSohENlCWSK69553B-NpebwIovODor2MEQ8W3wOY06z2xlyNRWRR0jXmaoKxqmyNhBRM70fkgxbNMEErZG0jUkk7mScukd1dpFSmdzHGFyCvxItkNwiudAVULJ830U-Qj_DkLsvuxMBPrVu0siSwxEqK79WZehJGnb3mA3VyBJWwAg7T8M1op6hkLusToS5bwkUMqAIMN925F5Eg8KCyoPdNal2GykGOmJ5NXGse2LVEFN3jAxdxs_PF_d3uMaRoJOrFZh392sEZesDXjryzPyCgCh1Ll5rniUcecVS8vMflE3EylfU35_Y6PIqoKKgNxHDieoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7SSB410D-yd5Eh0EADRC50IdydDxi0FB8Edy4ATkFmAfwtem-LKfJtIgX0PKBpOkO9vR9zuJ6Q_wS7QbnqTUYpS5fM3EjrvhyMUPSJOOTR3AyIZgUQnaUSnbRnplOmoprNoiL7n36zHWNiW0sviLltIn3l2Q3WI3fB8LPV_lVBCDh9RTYcX4HTv6mF-CAK6fP5yuR17T5Fahcloyo3fRx9MfpmyMClb_1YAA-odyqqf4Mx5TVVGv3iknGZno52nTwIihpqNjfTnlbXTXuLHdoM1ywZhjgM6t7vUPQYXAc0jtLx6w87SGo-UD1N_rJBFYGEvlJos-Tmy41yScyFPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onqOxpwpZiPKn4XZtOSxxTTXlzIh8BMBPqHpfJKAj8_dAQSA-7RyxvnfJeKh1BBKqzPXRco4LeBOhATlkbQi6D70foa1bbzMkCogFB_9Cyp5hxZo09IxgpdeZtepMsYtTtxpuLQD2I1uZjByLo2K5oVa7hGscmW9BUXkWoVID0MSmz64lWuRWT0zKBcVegl6xSDQyGAjK8dgrZKPG2UcBxIDC-glepH9-LQ7r4mLFA1wHqsFFa02CIk2QL1fphRDN3yqFly1FbFRdkUW51kS_hNzYhdPc6cFYdJdZzgHL5nnaHoxNIdaDC4gwzM7cSTGZBdHl9yUm5_OeLjqEHK5zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxxGwuRGekRYCp5a7pUd_iyIMg9TjLLhv_tRQYW5QuHzIrBmm8KbtzemWN3lGSpnVS4ccSAmaDmQo_n3cyxYcyF2T1_tGfV3K0pMqRteosF5xsUJY-qaMEyBDUZjtkcQ-biuB-qSJcUnqOcH9kDQwiABjB4RLp3t0JBZEBMTdeKDhDrM6G-NzI6r6cKQKBCnwZn4zggRVBod3LVg5I3yAW8C3Sfx8Opf0Ql7yrXJRa2QKfIH8V_bysQ3RjkO_IPD2nr-vEauuOF4aktsYLUroKzktn5O7ujpfodt-_fU5cdbmRbww8W8QFlAi6umag6fpU4c_wDseJh9m1ksvaMpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKvCjMbOGJqonuNvKBGcHqcsqaj37v4qTI4vCxVNHJ6a5PS0HwM9Basd5rIUIYX-GuU4n3sCw-kFuZiDKB0KeYfE2fvpdP2aBWUxqoz4uv_dRuiR91T5gpB6yg8KX8IXFL7pC2p6m-ecnejB0cWZqwRFFSIbMCayE2Vc4u8oo7NvPULt1oai8y7SxYSYyGiO7f-BmZBrKbInzorWUuljx_1THX2Xi2a3unm0569FESBai80pb4x639bGdHF8rCm-sL4-9Zvp0O0EfJcCxTt0mG3NjcrFfTEospZbUXyXppMpqJ_YGgj_ENhGTg-UY4dA6Pg-MKboa_LcpFjlpyAQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQsILzbmVKXGme-M2V47cfL62zkIpkRvLuwwxLYgA_9VsWf20HagUbjewQUpfloUzz1SLBeu4D8whwCi3hgtqlZIWrtsp5EqfToIlshoJVpbPQgNUtnkDoCPfWqDSJFubNkA_9VTHtH4oJRF4j_067sxwJRkwXQZK-fEs5LoCv9A2TMrhX7FQPRBSOwX7h8wsqwbtnzg4nuC0bsmEJ7QdLg4meEML9nsWIoHHmLs4qt7aXfjhc7hDJeTEBZlvX1n9ZpXXRtRZDCkPd7SxvMQai6iTKypUp9B1qFxcSpLgTShwiX6W_Ce1gKXBgjJI-hEcZVIipXX4x2Y9cVdbNXd4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدام گیاهان را بجوشانیم؟ کدام‌ها را دم کنیم؟ کدام‌ها را سرد بنوشیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/696275" target="_blank">📅 08:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696272">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2554da7b5.mp4?token=Z2FvnWeSKN9xCgCiDj7yd9xmcPK9kUqtrO__1m6typt8eD62wjIIQtTgDFuaQKZFbltC84-JBHsj5WH84DDKibbpSHsvzcEqj-5Rg0qhW6XIxMNBwqmAyVMB-2iSLr1mKvJVPqK3oCH7Die8ZrUsKPkrWxZuMpaB168XBk3QMnDte_U_ImPJcjcQJdEa4KKDKiwsVD8LPpVymbM1FzFa3o21daYk7TEJa_ovjT52GNzOcBqI3rvxPKWKUIcWpjWjkgXga97g_mdQzC4XSA9ikaBJ1FajEh-mgN0g-VCcrRiVfzqeB0euNHuVZp9raGhdC_hePaIYHqpgHcm6tLUx0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2554da7b5.mp4?token=Z2FvnWeSKN9xCgCiDj7yd9xmcPK9kUqtrO__1m6typt8eD62wjIIQtTgDFuaQKZFbltC84-JBHsj5WH84DDKibbpSHsvzcEqj-5Rg0qhW6XIxMNBwqmAyVMB-2iSLr1mKvJVPqK3oCH7Die8ZrUsKPkrWxZuMpaB168XBk3QMnDte_U_ImPJcjcQJdEa4KKDKiwsVD8LPpVymbM1FzFa3o21daYk7TEJa_ovjT52GNzOcBqI3rvxPKWKUIcWpjWjkgXga97g_mdQzC4XSA9ikaBJ1FajEh-mgN0g-VCcrRiVfzqeB0euNHuVZp9raGhdC_hePaIYHqpgHcm6tLUx0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار و آتش‌سوزی در دومین پالایشگاه بزرگ ونزوئلا/ آتش‌سوزی این تأسیسات را به تعطیلی کشاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/696272" target="_blank">📅 08:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696270">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1023a449d.mp4?token=HRTbcfHBd68FSEYJmAcGa-o4oFeKysUDpQKpLElGYWij5wyDBwnqtTzz-8hwb3TNBQ227lFiGqf19694T9kK1AixqfO3Cyeqps7dGBI40fVWqBBwOmg8I7wunFMpmXiP-5-olW5YjCTQEi8ONeDdIVDWdCC_6LI1GDlBCtCYsHKcxNCY_O6x9Ahqin_qGmYLj4JH1l1wYrw_fTR1AGck64-j2dlXRoBDeiugnAZrW3WpYL4bzP5FnWvTGC986QvpNhPuQnW64y8_OkxG8X6TImixgfmhiJFgi_GImhT0R_-LU9jugjzPZZhK7GCp4s3YMfh-kd7IZ4vM8bSrg0M_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1023a449d.mp4?token=HRTbcfHBd68FSEYJmAcGa-o4oFeKysUDpQKpLElGYWij5wyDBwnqtTzz-8hwb3TNBQ227lFiGqf19694T9kK1AixqfO3Cyeqps7dGBI40fVWqBBwOmg8I7wunFMpmXiP-5-olW5YjCTQEi8ONeDdIVDWdCC_6LI1GDlBCtCYsHKcxNCY_O6x9Ahqin_qGmYLj4JH1l1wYrw_fTR1AGck64-j2dlXRoBDeiugnAZrW3WpYL4bzP5FnWvTGC986QvpNhPuQnW64y8_OkxG8X6TImixgfmhiJFgi_GImhT0R_-LU9jugjzPZZhK7GCp4s3YMfh-kd7IZ4vM8bSrg0M_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پالایشگاه آرامکوی عربستان در جده
🔹
امروز، نیروهای یمن تاسیسات مختلف شرکت آرامکو در عربستان، از جمله در شهر جدّه، را مورد هدف قرار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/696270" target="_blank">📅 08:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696268">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606a4b8eb5.mp4?token=iVcXWxm8wkMdgVO6HVaJkIdEqvxMNqO7uot-i79BQzeGh0kux-IHCJ5F9RgITXRmagbYSoLPZUn6EeJ6N3sCAjsAx2yjAq5VU-oNM9YzUA1DI_7r8JRb_Oj0z-eIJCrgta1GSzsf92ElLmligLY0R438Zf9Ftx2JKuARMz7D9v6Z5xdRO3FpKBg8z5meRg2UjNMeErrAIcXhuiUaXt2HDMUqEtbjmALY3DP_rII9kqc4T4YlZ9WRQ1QY3tZV5XA2bYObtV6fYA2hezPN2THF6HUNjpQJ1M-KGQvpYoTbgIjINCrHm2RRjSSlZR91o3V3NxZ10lYnf01YpPNimh7DSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606a4b8eb5.mp4?token=iVcXWxm8wkMdgVO6HVaJkIdEqvxMNqO7uot-i79BQzeGh0kux-IHCJ5F9RgITXRmagbYSoLPZUn6EeJ6N3sCAjsAx2yjAq5VU-oNM9YzUA1DI_7r8JRb_Oj0z-eIJCrgta1GSzsf92ElLmligLY0R438Zf9Ftx2JKuARMz7D9v6Z5xdRO3FpKBg8z5meRg2UjNMeErrAIcXhuiUaXt2HDMUqEtbjmALY3DP_rII9kqc4T4YlZ9WRQ1QY3tZV5XA2bYObtV6fYA2hezPN2THF6HUNjpQJ1M-KGQvpYoTbgIjINCrHm2RRjSSlZR91o3V3NxZ10lYnf01YpPNimh7DSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش نور پهپادی شبانه بر فراز ورزشگاهی مملو از تماشاگر در پایان دیدار مراسم خداحافظی لیونل مسی
🔹
لیونل مسی: خداحافظی از تیم ملی برایم درد بزرگی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/696268" target="_blank">📅 08:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696267">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
کالابرگ ۳ گروه شارژ شد/ افزایش ۳۰۰ تا ۵۰۰ هزار تومانی بودجه ۳ گروه از خانوارها در کالابرگ
🔹
سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲
🔹
خانوارهای تحت پوشش نهادهای حمایتی
🔹
خانواده‌های نیروهای مسلح
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/696267" target="_blank">📅 08:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696264">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
معاون ترامپ: امتیازات هسته‌ای ملموس از ایران می‌خواهیم
🔹
ونس مدعی شد که برای پایان دادن به جنگ، ایران باید توانایی غنی‌سازی اورانیوم خود را به شکل ملموسی کاهش دهد
🔹
او که این بار به‌جای کلمه «توقف» غنی‌سازی، از عبارت «کاهش توانایی» غنی‌سازی استفاده کرد، گفت مشخص نیست ایران چگونه تصمیم خواهد گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/696264" target="_blank">📅 08:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696263">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9Uq3bVGY40nJ5f4E1y9V3PoXyQIOwhRXwrtfzj0xhKq1D8icZBd2SIoXRwJtX12me3tPwURe2exFn7v1-fZ-wZFE0TaARtzkXe2VQjVhNdhhy9lwvyyow_rOOAXmmdeCwO2O4brZpY6y9S2nsa2WgmwOLPZCelV4aeRJuoot2CRiOcdkhKR1vBSq7H_fV-OxYBue75qbm45UrQIQf0t7YvO51L4CWuQczIqS6SfoJYO2zQE0da6yKjtj6XwPxsMOBpHjWFwa_scJfpzbbawI6lZvr50mRmdMGCGtAc9kqaGEL083EXxSXHeGuOF7AHxRFgrE8ByYEWU5ve1H0zakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۵ مهر ماه
۲۵ ربیع‌الثانی ۱۴۴۸
۷ اکتبر ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/696263" target="_blank">📅 08:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696261">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psdj-DkmpkU55po-iINDgVjHMsyemgFmYd-4GNTFZE-B5Y7vikh4O-2kUVGasqDvXkGIbqT5ol_UEx47yDM76XOrA1bkhM6jxoqOMx6_rJ8I8iQ5EA6DwSbVohESW4QriibkgI974i1_HhR6dNi3bobhXSEWLFYzF3A_czD5tnXel-0Isd0Du1GAY-TvPsURbLYAeVOfZhQhrCz-cfmYCD8xDya_7w8AoF13KCU4edcMTdGX41tpNfCkVfkE4jnRPlp6cQJYyMZJcd4Prn0kN1hVNFh59XJd60XKfF07y_yMQCrG3Fo3P-kpyCOajAg1wIdSNhILTAkq0Wwh1MUsng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول ۶ ماه گذشته خرید آنلاین داشتید؟
🤔
این پرسشنامه برای یک کار پژوهشی در رابطه با
تجربه خریدتون از برندهای معروف فروشگاه‌ آنلاین هستش
و هیچ اطلاعات شخصی ازتون گرفته نمیشه
لینک پرسشنامه
لینک پرسشنامه
ممنون میشم با صرف
کمتر از ۲ دقیقه
از وقتتون، این پرسشنامه رو پر کنید
❤️</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/696261" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c218f42d.mp4?token=kBDYYdpye0KaJbiN893dYUbcchlpVD3zdNt-IHhR9ktdjn4Qy-wYSwR8668AiQFI3hemcgnzAENjBxaWCuk2KAjkfw3PWhjuqD5tsURJ5EojVj_ObIdOAA8NV6n4CRFuoWQWFT6V8dQ9c2tdvyit1q3Wo9ZlbK7mKWV3g9HQlL7GymljwpAbMTLKAT7rPCfBnUqXtnKJslBUBB1ECpM1dcWMSwpSkHtCI1Rp6oFkQTaWI_n06CtK-RF5_sGvOl-pLFxUW9myhMJ4UCdy0e90zg13Xid3_AQx2Y-a-uyuVHk2xBHAZkDCmcSWeDiMn3rAtjmC0ZR7EAi4ieAXNB6KTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c218f42d.mp4?token=kBDYYdpye0KaJbiN893dYUbcchlpVD3zdNt-IHhR9ktdjn4Qy-wYSwR8668AiQFI3hemcgnzAENjBxaWCuk2KAjkfw3PWhjuqD5tsURJ5EojVj_ObIdOAA8NV6n4CRFuoWQWFT6V8dQ9c2tdvyit1q3Wo9ZlbK7mKWV3g9HQlL7GymljwpAbMTLKAT7rPCfBnUqXtnKJslBUBB1ECpM1dcWMSwpSkHtCI1Rp6oFkQTaWI_n06CtK-RF5_sGvOl-pLFxUW9myhMJ4UCdy0e90zg13Xid3_AQx2Y-a-uyuVHk2xBHAZkDCmcSWeDiMn3rAtjmC0ZR7EAi4ieAXNB6KTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔨
میخ‌کوب دستی؛ یه ابزار کاربردی برای هر خونه و کارگاه!
برای نصب، تعمیرات و کارهای فنی دیگه لازم نیست کلی دردسر بکشید!
با
میخ‌کوب دستی
سریع و راحت کارتون رو انجام بدید
💪
✨
مناسب برای کارهای DIY، نجاری و تعمیرات
✨
استفاده راحت و سریع
✨
کاربردی برای خونه و کارگاه
💰
قیمت نقدی: فقط ۱,۶۵۰,۰۰۰ تومان
💳
امکان خرید قسطی هم وجود داره!
الان بخر، هزینه‌ش رو در چند قسط پرداخت کن
😉
🛒
برای خرید، همین حالا اقدام کنید؛ موجودی محدوده!
https://memarket24.ir/product/fast/57235/180124/</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/696260" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW75makijk4afGbY6o_b40VGR0ALVVwl58Rz2dM9Zn1ClIjyANBOvEZ2Y2mTH8P40dzYktHPobgxbdMJ2ReUW2zU_NbU6dG1KOrippMtnESRApa7beOpnt0xmIu56lMdlpatv1_XgKIEmF6FIIBn06XfoZv3sdGq8qd1xTiXk2UhA_mTADxDUCBvdhbwL_mFnSv-giK_YOqTFQGBIkxX_rcfz-CDNkKQxEZxp2BWU6SBOZa1sYBH9qe66qbgNAXE0jrW2Tl1o-CHMuwQ5ZjCbbyrGeSDqS9oaun6nhTCC4yWNCAVpdynkkGeq7oY_p-bQ5ebyELyQaWbXbB3EIiGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبری‌که همه‌منتظرشنیدنش‌بودن
❌
پژوهشگران موفق شده اند ترکیبی را معرفى كنند كه مى تواند سلول هاى بنيادى فوليكول هاى مو را از خواب چندساله بيدار كند
😳
😳
✅
این تحقیق روی ۱۰۰۰ نفر تست‌بالینی گرفته شده و نتایج فوق العاده در قطع ریزش و رویش مجدد داشته است
✅
🔴
حتی روی کسانی که ریزش‌ارثی هم داشتند اثرگذار بوده
رویش مجدد مو به همراه دارد
🧬
در حال حاضر در ایران این روش بالای ۳۰۰۰+ نفر رضایت‌درمانجو داشته
به زبان ساده، موهاى خاموش را دوباره زنده مى كند!
دریافت اطلاعات کامل و نحوه و هزینه درمان
روی لینک واتساپ بزنید
👇
https://wa.me/message/R7FMNSDOGSIXC1</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/696259" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696258">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f09f86fbb.mp4?token=s1l5NjQIdq7omNe7iJ_ScK9d4egn93QoqDrv6HL2Dg0FeItrMS-8V0Rl4vv1g_oyTCQME_l4EDiNvrE86BRIjDF6RheEMgQAHQAloA8day10EnhrMpEbHBMGflMrbdTu2hL-DsXzUmBbpEbjZVDRz31xIMHAm-FE2zTv1pI3tKhMSuO0geJkifb0vDcwkeluTpprwhhDUFsXQXHWhfRQgty_ORKexvKf_kY7Wvx8zvXMQDUEUY4WjJ7sv20b5AgwuKJlkxXTLjil98MTSi5c9WIXdMvNlg3LUaWmdHAzN-MR3qESHu6vV-M63t-32h3gk2do54NabjKtQjSxdHytcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f09f86fbb.mp4?token=s1l5NjQIdq7omNe7iJ_ScK9d4egn93QoqDrv6HL2Dg0FeItrMS-8V0Rl4vv1g_oyTCQME_l4EDiNvrE86BRIjDF6RheEMgQAHQAloA8day10EnhrMpEbHBMGflMrbdTu2hL-DsXzUmBbpEbjZVDRz31xIMHAm-FE2zTv1pI3tKhMSuO0geJkifb0vDcwkeluTpprwhhDUFsXQXHWhfRQgty_ORKexvKf_kY7Wvx8zvXMQDUEUY4WjJ7sv20b5AgwuKJlkxXTLjil98MTSi5c9WIXdMvNlg3LUaWmdHAzN-MR3qESHu6vV-M63t-32h3gk2do54NabjKtQjSxdHytcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: در مورد شیوع بیماری طاعون در روسیه، آیا با پوتین صحبت کرده‌اید
؟
🔹
ترامپ: قرار است خیلی زود با او تلفنی صحبت کنم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/696258" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696254">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نتانیاهو بار دیگر به شهروندان اسرائیلی: به شما قول می‌دهم، ایران قبل از انتخابات به ما حمله خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/696254" target="_blank">📅 00:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696253">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAeQI0dxTeDSnv_RnmVm0hPDYATcOBs8nRoWHniE4gYDTBbqnbED7MtmqAKolkvy5hrrhxWRon55foSjOpMbJjpm97r0of8tqn9l2HpBcEqpKChsKJFQ6FsAaE4w8RUIl1D4vQlmNBdnfUKIAd6z4KT2xJfJ-MzMFbvRzIihm8vMYa82B_RWpehtlbpchxvm3bUQQ3n7TvY3FZIIF-zwXm5jPkrHvebLef7_ebQNjAjZ_KMWaFfKxxnO6qmTM74uguoadWL8HtP1dTVMWM-4ipBPq_K_3J_Y0Qo9bWhqi7T9G0W02BxRlJOrxupYFHH87QRw912nzIjZ09XzM62h9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر ژئوپلوتیک امریکایی با کنایه: تعداد کشته های فرانسه به ۴۶ هزار نفر رسیده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/696253" target="_blank">📅 00:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6UXzAzUA2Gd8BaeepIb2ChJrQ5Bo2qbhHk76Fq8r679RFlxbjmF1Uvd_cccT3nhZ5sNHOMDx4XgJaaBMXF9a4I9ovHnucGpH3rGctHzmCPCELxmh5IPM72JrFRb-A27wETe2bp633ThrNWx-U445fU97xXuBNi1AK5LtRZjyF1lNI58Z52zHHUc9uledBMc55iFN55QLaJ_B0hnXPmS8UQkYj7ldWefgBsGJL_eyP8Lx0lmNmc5cq6eDCdTVmDSyFh_7rSfOIPMKdaeOMeWL1NotVJHOkWwFpEhP5P3QKurWYYdP1r6Rk0qsrzDCwu314lIgwv6dH2Bbdvaf7uOZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تروریست وارداتی
🔹
در روزهای اخیر هم‌زمان با افزایش تحرکات تروریستی در سیستان‌ و بلوچستان و شهادت شماری از مدافعان امنیت و یک شهروند، وزارت اطلاعات از انهدام ۳ هسته عملیاتی گروهک تروریستی ـ تکفیری در جنوب‌شرق کشور خبر داد. هسته‌هایی که به گفته این وزارتخانه، اعضای آن‌ها آموزش‌های نظامی، بمب‌گذاری و ترور را در خارج از کشور گذرانده و با هدف ایجاد ناامنی وارد ایران شده بودند. این عملیات با کمک گزارش‌های مردمی و همکاری فرماندهی انتظامی و سپاه سیستان‌ و بلوچستان انجام شده و اعضای این هسته‌ها در خانه‌های تیمی شناسایی و منهدم شدند. با توجه به شرایط موجود و حمایت رژیم صهیونیستی و آمریکا از تروریست‌ها با هدف ایجاد آشوب و ناامنی، ضروری است دستگاه‌های نظارتی و امنیتی بیش از پیش نقش فعال‌تری در مقابله با تروریست‌ها در سیستان و بلوچستان ایفا کنند.
🔹
هشتصدوهفتادونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/696252" target="_blank">📅 00:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f062b623d6.mp4?token=VP0XSpdzNLr7NNFoxO3HaNRRercNcvSZ9ddcJo9iD1R_QwmDVcmSJ6jE2fkNcUzq8SGdgN-glJIY2xFHoX-VESZsOVnzIUgWAAv0k-fW5M1tgr5ir3j-bk1GtF-SdRW-KXgMTXf7JdXGJqo6l6nOG_K6hiagOk8o5t1Ht0uGkHiZu9XtvGqr6sMlZpjPM2ne5Orn9hIcf1hTE5SAtFCLgOpu8FVccFNOgqRsXOgI89rbUIaNYxwPcApRvntQnGaSpTiGsWhYe50UOFLyJbtYIzOduiPsMJH8X23f3w067Npd4J15-j4ztN9JxjNez-GYqiXKdkedrUyouRbOTy4YIXtebPDOhjqf13IzbpjWqalI5zLoNa4lSfisR1hyj94f_ikqLQizT353SOLoriQXYKbK8K4mSvjMq5QyJLLdKQQ-FCeAzLfP3rIeRABJr6QIwiDsapHtZ8FL30WBf_W-vx5GY6BaNku4ay8R3itd1AGCa4uPFqMwmhrUvLPLImJQCu-TppA1JkxrnJTGKxXUQT9y-8XF7mZ_X6xG5g03ZBKMew1W6tk3cSENIsBHo1svzUO3wcBxU1nPFzWOJCaVIeZrxKPbJNKnpVHYPg7Rwa-WN-Q420jICSLy4Jw6hQAlqX0wICoOOvQyDwk2l0g5ALWgbrixUB-_YjGMkefTGHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f062b623d6.mp4?token=VP0XSpdzNLr7NNFoxO3HaNRRercNcvSZ9ddcJo9iD1R_QwmDVcmSJ6jE2fkNcUzq8SGdgN-glJIY2xFHoX-VESZsOVnzIUgWAAv0k-fW5M1tgr5ir3j-bk1GtF-SdRW-KXgMTXf7JdXGJqo6l6nOG_K6hiagOk8o5t1Ht0uGkHiZu9XtvGqr6sMlZpjPM2ne5Orn9hIcf1hTE5SAtFCLgOpu8FVccFNOgqRsXOgI89rbUIaNYxwPcApRvntQnGaSpTiGsWhYe50UOFLyJbtYIzOduiPsMJH8X23f3w067Npd4J15-j4ztN9JxjNez-GYqiXKdkedrUyouRbOTy4YIXtebPDOhjqf13IzbpjWqalI5zLoNa4lSfisR1hyj94f_ikqLQizT353SOLoriQXYKbK8K4mSvjMq5QyJLLdKQQ-FCeAzLfP3rIeRABJr6QIwiDsapHtZ8FL30WBf_W-vx5GY6BaNku4ay8R3itd1AGCa4uPFqMwmhrUvLPLImJQCu-TppA1JkxrnJTGKxXUQT9y-8XF7mZ_X6xG5g03ZBKMew1W6tk3cSENIsBHo1svzUO3wcBxU1nPFzWOJCaVIeZrxKPbJNKnpVHYPg7Rwa-WN-Q420jICSLy4Jw6hQAlqX0wICoOOvQyDwk2l0g5ALWgbrixUB-_YjGMkefTGHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افراد با هر نمره از ضعیف بودن چشم، دنیا رو چطور می‌بینند؟
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/696251" target="_blank">📅 00:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696249">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Orbg9JA1l4JhiOD64zC_KBCO0v8Ft_7rJeq4h4tLQbkxKWCiYTyHQVA1JBal-W8D-Tmx8bQNnKC60JmD2h8zJttkczUINvrIMpmMfFbblAtg9la_e1E8UBmXfE1k3eaO2CAzfDdtKaebcGuvINRbvAtiDVwtRaypRC6SJcmrhS0MnsyEw1q1WQ_5aRAIzm95OWgaZKDBtu0MOsLcco_o_wmVhk_7X9i7izw3IVuZwEv_KeazShzirfvhNhrRYw1dEgs1HA3ja3n1U1GzGVTrSJ2V3ACEtU0v1eJzALV0MMj5pdk_Mgu-xalt-a55Rip1POuaJVoB9T8TS2-G2F2CVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PA-XGqda8S2kITEa2qX_oXfpWbJ8XfaQV1h_FUPf1--XyiujFnZc9jgJt031Xk-6YXmli1BEihanxkO6pXe9AryP2sTngJFRI1MEsmbGFGUR1-oMxKhpedtPeciJ8zpwCgddjuYuWK5pxCBkDqdX7SeWxv5b71knQr7FjvMRJ1bJm3ZKfy-HZxLr6g5UmMjK_c6TynLz-mmYocBQpx3sEHYNmaJLU019KKv0rBK-D9tV0_iWB2otQN1xYH4Gb87K43W9kM3Dr6DYLBJQqU2bVRdApj3BSOQcA9Ao_HafG4Q1xMEya_8q7FbQRMY0vHT1xADLJ_L6xBp10DEAn6WZ_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سفارت آمریکا در موسکو از یک مورد مشکوک به طاعون ریوی در منطقه ایرکوتسک خبر داد که به مرگ یک نفر منجر شده است و از شهروندان آمریکایی خواست روسیه را ترک کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/696249" target="_blank">📅 00:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696248">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4OhtH_rFQ6Ydm0zWwceUIP_YKnbcRgWdZb_Yr5IQhFKAqY4tAUnFkE_3ph2zFbjDmeybafjdSuubGo0qTqi4dYIDSVGeAup3RoXiQJMjlyxCpdlgMdsfQkIBT0ZdIx9t3oHixWWO8jEHP0XasAS_vQsuBIXHAnm7AK1jOInchRlxvLLZPSG62EyUaiUqNQpXhM--2Pn8p6rHqByBKDFyz7ffjnvebNgfETfBjkqGs9B8HBIib7DwXljCnJrtMKDWhqfhYGZ7P5oO0XTj1NANqg932KCwXcH34X44b0_BfzHJCC7I4NYQyydlexb_PEYdIKtk6pOrmS0_Wgeh1twmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانال ۱۴ اسراییل: طاعون روسی دومین کشته خودش را ثبت‌کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/696248" target="_blank">📅 00:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696247">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59388c5edf.mp4?token=GYzWE-5vky4PfprMLNTTJyaHIqyjpqR5qmHO3t9xknvUbe4QggoG7eOpm83lp2XFq6v-8urIRqFrmmABl6dIi6_e90swcZiF0bph5vL_u1CHJQQ4JLJtaVrT5kokp7oaLQC918VpUyGulTCch4WBOPAUkAYrztwqFxoJaI8sFmClCR2nuWYUDXGhuDlw1ciy6u5RiClVhCOyWIJZp2_iat3nzGZBTn92vY5LgMMedfAZZ2B9CMT5bc84qKO-G3yx4NLZgPXkeS8094R8XlH4AiXFkcWflop_0Qp5s4IuVY4DzHYGc11ut0nYu7THfkGM5de7nne3pzhXdcXKXYWW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59388c5edf.mp4?token=GYzWE-5vky4PfprMLNTTJyaHIqyjpqR5qmHO3t9xknvUbe4QggoG7eOpm83lp2XFq6v-8urIRqFrmmABl6dIi6_e90swcZiF0bph5vL_u1CHJQQ4JLJtaVrT5kokp7oaLQC918VpUyGulTCch4WBOPAUkAYrztwqFxoJaI8sFmClCR2nuWYUDXGhuDlw1ciy6u5RiClVhCOyWIJZp2_iat3nzGZBTn92vY5LgMMedfAZZ2B9CMT5bc84qKO-G3yx4NLZgPXkeS8094R8XlH4AiXFkcWflop_0Qp5s4IuVY4DzHYGc11ut0nYu7THfkGM5de7nne3pzhXdcXKXYWW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پارک دوبل بدون دردسر!
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/696247" target="_blank">📅 00:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696246">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
هذیان‌گویی وزیر مالی اسرائیل: از منظر تاریخی و بین‌المللی، پروژه‌ای در قرن‌های اخیر وجود نداشته که عادلانه‌تر یا اخلاقی‌تر از پروژه صهیونیستی باشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/696246" target="_blank">📅 00:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696245">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c748440d.mp4?token=uxbN9TnkedHp2CCpT0UC6FVroLGg3pfsCfrNK-sh8HlI3KqKg3w0rYwi9xmNdsxreLoaCa5eSwofpSVX0yiz1MMVPPI6a-rUtjgZpXFtRuzUY9QGPxQWGF92y_G-vIvsm2FwhdSAYj4xGXV4rGJEYYzdAg6lZ4D-jhUz8B6mQPyenlfZB0QSksT-EWGCN8XzDcE7fOocDT1nppSo9R3PFB3ECjwW-j7DO62WPLuJJKNuyg0PSgL4EbeggWeRjva_NJbEtmXQoI8LvaoINkzyu_jTF9oboPNAJn5jcZ53Y0JGcfdTTTrN63SZ1FkSS0AgkH51t--3PHmclqB0Eb7eEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c748440d.mp4?token=uxbN9TnkedHp2CCpT0UC6FVroLGg3pfsCfrNK-sh8HlI3KqKg3w0rYwi9xmNdsxreLoaCa5eSwofpSVX0yiz1MMVPPI6a-rUtjgZpXFtRuzUY9QGPxQWGF92y_G-vIvsm2FwhdSAYj4xGXV4rGJEYYzdAg6lZ4D-jhUz8B6mQPyenlfZB0QSksT-EWGCN8XzDcE7fOocDT1nppSo9R3PFB3ECjwW-j7DO62WPLuJJKNuyg0PSgL4EbeggWeRjva_NJbEtmXQoI8LvaoINkzyu_jTF9oboPNAJn5jcZ53Y0JGcfdTTTrN63SZ1FkSS0AgkH51t--3PHmclqB0Eb7eEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیال پردازی ترامپ: ما در واقع ایران را به پایان رساندیم، به محض اینکه بمب‌افکن‌های B-2 به آنجا حمله کردند، زیرا این پایان برنامه هسته‌ای آن‌ها بود #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/696245" target="_blank">📅 00:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696244">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a175aade2.mp4?token=NDUg2fd7d_oBWkE_Bmrjv1W6peVQjQazkd06bQyQpi_8s67Xgge6X_q0ay3I92j41uJCMoDs7K0yoMQojwXLg65OvNGVapTBbPFD20UscQraA6cuVF40Wisc_-lsNq6zm7tLIA0oI1285OVN_nzXPOvo4YsPI9D36ah2lCad0i9XBtbNQyvlpmfWMSRrSJY39dnVaDVnQ6Ed5nm5rfveSfSZThfrqhVJvwCjnYCYUKeTjRkWlIaYJDpNGtmKGgQmerTvNZk3jQ2QjDuUsElDo1pqslmByz0wk7KRL4iZIU9C60EEso2AHaGWuAZ3TChGSG2dFCaUOCM1MMGPwDguUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a175aade2.mp4?token=NDUg2fd7d_oBWkE_Bmrjv1W6peVQjQazkd06bQyQpi_8s67Xgge6X_q0ay3I92j41uJCMoDs7K0yoMQojwXLg65OvNGVapTBbPFD20UscQraA6cuVF40Wisc_-lsNq6zm7tLIA0oI1285OVN_nzXPOvo4YsPI9D36ah2lCad0i9XBtbNQyvlpmfWMSRrSJY39dnVaDVnQ6Ed5nm5rfveSfSZThfrqhVJvwCjnYCYUKeTjRkWlIaYJDpNGtmKGgQmerTvNZk3jQ2QjDuUsElDo1pqslmByz0wk7KRL4iZIU9C60EEso2AHaGWuAZ3TChGSG2dFCaUOCM1MMGPwDguUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: همیشه از رهبران کشورهای مختلف تلفن‌هایی دریافت می‌کنم که در آن از من به خاطر جنگ با ایران تشکر می‌کنند
🔹
من به آن‌ها گفتم: "خیلی خوب. چه زمانی قرار است هزینه آن را بپردازید؟" #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/696244" target="_blank">📅 00:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696243">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b24259bc.mp4?token=VKgRAil2crL3h_bWTtTecVUzs9DCKlEEgg_8HTYwaHzbyYja3tXPIaA_FGxP5ENoxtaM-ba_48JNDs_XQzY3TABxmpO5tIPjFW7DCuZa6eudejkzOaP2CIXUGTF5LPIhyijaAGwtjMI40NeUx_c6S7qwjH_Vpa-_BD6A8-ydxMBdUboxasy-j1ChEI7CVXPsijFLLbwBQpNmeu1GA-PCRyzOUk7bi05MoHiMJBbZz9UPpI6hEWrxAeUcScv2B9wdsHJ4AgNrwv6TJUBOeiWcft9AUISp3sDqJo5-mQKowqtbLaqLf1c3m1zMqFfgSqCTgMm8jPzlym3cCk4525LYcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b24259bc.mp4?token=VKgRAil2crL3h_bWTtTecVUzs9DCKlEEgg_8HTYwaHzbyYja3tXPIaA_FGxP5ENoxtaM-ba_48JNDs_XQzY3TABxmpO5tIPjFW7DCuZa6eudejkzOaP2CIXUGTF5LPIhyijaAGwtjMI40NeUx_c6S7qwjH_Vpa-_BD6A8-ydxMBdUboxasy-j1ChEI7CVXPsijFLLbwBQpNmeu1GA-PCRyzOUk7bi05MoHiMJBbZz9UPpI6hEWrxAeUcScv2B9wdsHJ4AgNrwv6TJUBOeiWcft9AUISp3sDqJo5-mQKowqtbLaqLf1c3m1zMqFfgSqCTgMm8jPzlym3cCk4525LYcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهمات ترامپ: تنگه هرمز متعلق به ایالات متحده آمریکاست #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/696243" target="_blank">📅 00:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696242">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
یاوه‌گویی‌های مکرر ترامپ: کل ناوگان ایران از بین‌رفته است!/ ایران دیگر قلدر خاورمیانه نیست! #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/696242" target="_blank">📅 00:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696241">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knPYhYuROAl0ZWQeWFZ9YiYNFQOuar0TBdPuCyNQGinFKYk1o3pne-jjbci8zZtI6TVl-_uMhSQT5pdY1X23bH4T7qOMtordbW3qjglnZwkScyfGrACZ7moKmNEgY8oSpON2OUm1BNq7pkMlRcjwGyKcvVsJjMygC79GZxl_idh7qnTuxajnYFhaUNqc4AF_URenwSpYOxuBcXkUGpPt44sYCkj3dg4tBX4NIB70YqCadg58PyFucO4fFTGmHMrGLAv-rwO5FKUJBwFLaDLEiknzlDx4GNNzVw5CGDXTtVOabCPuiFeNb2-62GRNAMy9umVjdHpeXX3my4kPzJRiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/696241" target="_blank">📅 00:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696240">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ترامپ بازهم وعده توخالی داد: بعد از پایان جنگ با ایران قیمت ها پایین خواهد آمد! #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/696240" target="_blank">📅 23:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696239">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ترامپ: به زودی متوجه خواهید شد که ما چگونه کارمان را درمورد ایران به پایان خواهیم رساند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/696239" target="_blank">📅 23:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696238">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
خبر عفو امیر تتلو کذب است
🔹
ویدیویی که از نسیم، خواهر تتلو در دقایق گذشته منتشر شده قدیمی و مربوط به یک سال قبل است.
🔹
نسیم سال گذشته در همین ایام در یک ویدیو خبر از عفو امیر تتلو داد که صحت نداشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/696238" target="_blank">📅 23:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696237">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106ffa55c9.mp4?token=S2BnLdTJ2aWy9SHi3H4BJrQQgnUw8Z90yTQGVe8d5uz3HKsZpwE7c2EPqNeVggXkpRoFUrm-RKHcxXUa3fdSTydt7ENcR3vu0SihQKs32W0I_7ky3qeeRZGunqpW_nTHmlLiK0Rxo8biAIOPXIkBH9LYtgbYYNCj6sNnWHsG5dDafv10pDBLcnzeoaNr6GLqru0dh1zv2xJO8U_89fawedbd5U47KRklBlO9NSNqLYcTH0YFGZHVsps7ltALv285bNEZncGjIf4Wprcnetv1QisVwyyp1isQA2W3tbhPSpxQS6b-alvYyL8AN2rrfOhhWqd5DRKTl-XAdKLb8ZCUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106ffa55c9.mp4?token=S2BnLdTJ2aWy9SHi3H4BJrQQgnUw8Z90yTQGVe8d5uz3HKsZpwE7c2EPqNeVggXkpRoFUrm-RKHcxXUa3fdSTydt7ENcR3vu0SihQKs32W0I_7ky3qeeRZGunqpW_nTHmlLiK0Rxo8biAIOPXIkBH9LYtgbYYNCj6sNnWHsG5dDafv10pDBLcnzeoaNr6GLqru0dh1zv2xJO8U_89fawedbd5U47KRklBlO9NSNqLYcTH0YFGZHVsps7ltALv285bNEZncGjIf4Wprcnetv1QisVwyyp1isQA2W3tbhPSpxQS6b-alvYyL8AN2rrfOhhWqd5DRKTl-XAdKLb8ZCUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: به زودی متوجه خواهید شد که ما چگونه کارمان را درمورد ایران به پایان خواهیم رساند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/696237" target="_blank">📅 23:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696236">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
خبرهای جذاب را به انتخاب مخاطبان وبسایت خبرفوری دنبال کنید
🔹
🔹
نشت آزمایشگاهی طاعون تایید شد | ۳ بیمارستان قرنطینه شد | طعنه ترامپ به شیوع طاعون روسیه: باکتری‌ها باهوش‌تر شدند!
👇
khabarfoori.com/fa/tiny/news-3250303
🔹
با آمریکا یا بدون آن؛ نقشه اسرائیل برای عملیات مستقل | تهران ممکن است معادلات حمله را تغییر دهد | تقویم جنگ تغییر می‌کند؟
👇
khabarfoori.com/fa/tiny/news-3250265
🔹
نتانیاهو نزدیک‌تر از همیشه به سقوط | بی‌بی کمتر از یک‌ ماه به انتخابات دست به جنون می‌زند؟
👇
khabarfoori.com/fa/tiny/news-3250387
🔹
روایت تازه از زندگی خصوصی مرد شماره یک فلسطین در سپاه قدس؛ همسر سوری حاج رمضان کیست؟
👇
khabarfoori.com/fa/tiny/news-3250333
🔹
پشت‌پرده استعفای وزیر نفت؛ ۳ روایت از یک جابه‌جایی پرابهام | پاک‌نژاد چرا رفت؟
👇
khabarfoori.com/fa/tiny/news-3250353
🔹
صفحه ویژه اخبار پربازدید خبرفوری را دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/696236" target="_blank">📅 23:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696234">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8751deb3a7.mp4?token=GCHq56cp7pQM0T5vVuLzIELNJ36Z9qfUGAtpICnsgUNj-Tc3YXZmiI9JBpcTbRLJHQw-1lwOJIcpzolvQ3GB-s5p6Dj3D4iH6NxdeToYFY2Lm3mozSEVFYZCKWCwGpiViuYpAwpZvxHrRqu7TMzseIA48Mn1-qM1jPHILLIlrbnx8flwsUkcdi2LuCR8Cx1DrgLEEOraetP2gBKRjpkUoXNqCPCorYagsC_9uJxnSap2v87p0njvdCKJC_z1IeyaAWAlV2frnUy0IK59Up4BXGDt2HAFxI7jTnmLRwEA1Crmwe2C3LYltlfI7fsJvqQvBXfR-wexlC3XtPmIzCtHRAgWxDHAUVsVTS6MhRwrkAyCYh7KzHUwOa4e2goo13TDwi8WAuBlFsXwq-FejEu4h5RCk3oDQI1YJ79hzQeRxYiTxi3JIyx8f75vTjHgIN_u9dtN93A_Kt80MaVfGzAzgzF-RDiLk_jAgLjiZPJLwMT5dretmXR7dTLWYTmQRPWK2mKHtXgI6h6X2IIeapu9GahKvw7RDDZqrYXVqv6WbAiPUHgsQ2IdDJhtIvktT7Tlpvf5tQvcECJpbQVgCV1xp_kiI6FVcikC8OEAvcoyMLw9wgx4df6DVxplys66AFqLDXN5kdV_fiDP9Pfi2ZYi0AWzYwt5_69di70VfN2J1EM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8751deb3a7.mp4?token=GCHq56cp7pQM0T5vVuLzIELNJ36Z9qfUGAtpICnsgUNj-Tc3YXZmiI9JBpcTbRLJHQw-1lwOJIcpzolvQ3GB-s5p6Dj3D4iH6NxdeToYFY2Lm3mozSEVFYZCKWCwGpiViuYpAwpZvxHrRqu7TMzseIA48Mn1-qM1jPHILLIlrbnx8flwsUkcdi2LuCR8Cx1DrgLEEOraetP2gBKRjpkUoXNqCPCorYagsC_9uJxnSap2v87p0njvdCKJC_z1IeyaAWAlV2frnUy0IK59Up4BXGDt2HAFxI7jTnmLRwEA1Crmwe2C3LYltlfI7fsJvqQvBXfR-wexlC3XtPmIzCtHRAgWxDHAUVsVTS6MhRwrkAyCYh7KzHUwOa4e2goo13TDwi8WAuBlFsXwq-FejEu4h5RCk3oDQI1YJ79hzQeRxYiTxi3JIyx8f75vTjHgIN_u9dtN93A_Kt80MaVfGzAzgzF-RDiLk_jAgLjiZPJLwMT5dretmXR7dTLWYTmQRPWK2mKHtXgI6h6X2IIeapu9GahKvw7RDDZqrYXVqv6WbAiPUHgsQ2IdDJhtIvktT7Tlpvf5tQvcECJpbQVgCV1xp_kiI6FVcikC8OEAvcoyMLw9wgx4df6DVxplys66AFqLDXN5kdV_fiDP9Pfi2ZYi0AWzYwt5_69di70VfN2J1EM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دو هواپیمای آمریکایی و کانادایی در باند فرودگاه لس‌آنجلس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/696234" target="_blank">📅 23:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696233">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5d01a674.mp4?token=WeoLzMDlBvk3OLMP6jXOSHVBZFiYTEws_SU-dNeLPuxuzzGKVTepiwRs_bmJyG9q2rRj3JCom5cETNZ2bAsbbMQUdDottyO_tDp6yoN0H1i8YMO9_47Gw79DhuBuOpjGECjGe3ucVzv569-soaA90SYXBdOFD3Xj5XcX1gZo8chHAqh1ybRCNioVkQvprq8q-49vWs_s5Icg9PAoCa_lSMS9UZc0g4UH4pJqTLCIXWrt0ImAxbylfzv6FhH_NB5t8QKrDlpKDDzmLtLrY6TC8ZkYI5ixTuGjD1WJWrpJv7ifqhJuDzofzDQfN1ShPqrsyN5DY0Do7acprddjLnt98g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5d01a674.mp4?token=WeoLzMDlBvk3OLMP6jXOSHVBZFiYTEws_SU-dNeLPuxuzzGKVTepiwRs_bmJyG9q2rRj3JCom5cETNZ2bAsbbMQUdDottyO_tDp6yoN0H1i8YMO9_47Gw79DhuBuOpjGECjGe3ucVzv569-soaA90SYXBdOFD3Xj5XcX1gZo8chHAqh1ybRCNioVkQvprq8q-49vWs_s5Icg9PAoCa_lSMS9UZc0g4UH4pJqTLCIXWrt0ImAxbylfzv6FhH_NB5t8QKrDlpKDDzmLtLrY6TC8ZkYI5ixTuGjD1WJWrpJv7ifqhJuDzofzDQfN1ShPqrsyN5DY0Do7acprddjLnt98g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جدید صفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری صحبت‌های خوبی با تتلو داشتن و اگه گزارش خوبی هم رد کنن، امیرتتلو فردا آزاد میشه و به استقبالش میریم!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/696233" target="_blank">📅 23:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696232">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کانال ۱۴ اسراییل: طاعون روسی دومین کشته خودش را ثبت‌کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/696232" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696231">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/613b040bef.mp4?token=Y0J2id7fowLT99K-cmkDQxCvIfPxqvPr5sWAfmEPzC8MHmpyPj1Yn6qLQUSk32XFn1zNms0yvAcMgbmMmI9lxbJkKUM8-zj6busQ3gfyg_n2_Fc7opdp6-qlugUMnxx4IRHKqdtd6UB8si8m6JWAsYtSVTdgHGPFqjXGyuZ6I1BdLR2PFhnrEiBtbelbHOU_RmXwcGbs3k-f12ervrcAtsayAM9JqMEfRuMMBscBPYKmcOKEp4ODbTG5FAQ343hIVEpry4y0tKBWx-t2BGBKHOvLvgWZEYJgNqXI7JWQ7Nbb_fR7DWjj7qzfpRRMKDcmX5SjrEj2IB_8lkOhdtlr7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/613b040bef.mp4?token=Y0J2id7fowLT99K-cmkDQxCvIfPxqvPr5sWAfmEPzC8MHmpyPj1Yn6qLQUSk32XFn1zNms0yvAcMgbmMmI9lxbJkKUM8-zj6busQ3gfyg_n2_Fc7opdp6-qlugUMnxx4IRHKqdtd6UB8si8m6JWAsYtSVTdgHGPFqjXGyuZ6I1BdLR2PFhnrEiBtbelbHOU_RmXwcGbs3k-f12ervrcAtsayAM9JqMEfRuMMBscBPYKmcOKEp4ODbTG5FAQ343hIVEpry4y0tKBWx-t2BGBKHOvLvgWZEYJgNqXI7JWQ7Nbb_fR7DWjj7qzfpRRMKDcmX5SjrEj2IB_8lkOhdtlr7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر نمیدونید دقیقا چه شغلی برای شما مناسبه، این تست رو انجام بدید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/696231" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696229">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOH28cLOkqUkkdjmc59SbhxZuwJpWG-rQjsXEemo23cSwRPyGrahvw6BYKnNqy73J4Emqpmkpk5kWKU0gnHHZX51XndJZGae53GBY1eAqPqFgLIzrWzir0SIVWYPfs37Zn-z2ENFpQJ_-UH7WZnNymRdnkqnKKc9bJ-jXsONbvEmAw8beEy11DvxI4cyeDr-rQkBQMvc_4vmj-CgqfxYU4LT6JVAbQIqI2Z7yW5eix3tJoeKRFsWS28qMC0aUBNeDXuLgaUNE4zpwSwVgSL74zgpEBQ2dvXfuni7N39wnm2_byxolnGt18F07rHw7MMLmFKp-9ut39plYLijb6dYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل رایتل: اپراتور رایتل سودده و در مسیر توسعه است؛ واگذاری سهام، فرصتی برای ورود شریک راهبردی و سرمایه هوشمند است
🔹
مهدی فقیهی، مدیرعامل رایتل، در واکنش به برخی مطالب منتشرشده درباره واگذاری سهام این شرکت گفت: تعبیر واگذاری سهام رایتل توسط سهامدار به «ورشکستگی»، با واقعیت‌های مالی و عملکرد شرکت همخوانی ندارد.
🔹
فقیهی افزود: رایتل طی سال‌های اخیر سودده بوده و در سال گذشته نیز زیان انباشته شرکت به صفر رسیده است.
🔹
وی ادامه داد: واگذاری سهام، تصمیم سهامدار در چارچوب سیاست‌های واگذاری است و می‌تواند فرصتی برای ورود شریک راهبردی و سرمایه هوشمند به رایتل باشد؛ شریکی که علاوه بر سرمایه، فناوری، بازار و ظرفیت‌های جدیدی برای شتاب‌بخشی به توسعه شرکت به همراه بیاورد.
🔴
مدیرعامل رایتل همچنین از برنامه این شرکت برای توسعه ۵G، حرکت به سمت «اپراتور صنعت»، شبکه‌های اختصاصی، اینترنت اشیا و توسعه خدمات سازمانی و دیجیتال خبر داد و گفت: در بازار مصرف‌کننده نیز بهبود تجربه مشتری با ارائه سرویس‌ها و خدمات جدید و متمایز، از اولویت‌های اصلی رایتل است.
🔴
فقیهی تأکید کرد: رایتل ضمن احترام به رسانه‌ها، انتظار دارد تحلیل‌ها و اخبار بر پایه اطلاعات دقیق و واقعیت‌های مالی شرکت باشد.
🔴
وی در پایان گفت: رایتل حق پاسخگویی و پیگیری قانونی نسبت به مطالب خلاف واقع و آسیب‌زننده به اعتبار شرکت را برای خود محفوظ می‌داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/696229" target="_blank">📅 23:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696228">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079b034b2d.mp4?token=Fg_rJHWbtz6yi5AK9JRK5dDpo2Cxh3DabYTti6s9XmCWMqSHKsqK0vkc_bpHztUb5aIlhN29KrpSeLVUJ5E9FqsdVJ2r2pG8gj3bkUsIxpwnK-dNu6gNnpIl50l1x8PzeCd27ZojOgAa86IU_OduFBB7NDoh_RMMBXsnL-9OTw9befO5ODE-aI3sOtNJ6E5jvHpwj2sK1iT3E-SwoiwfcdtposqpG3hslduPVUFFE7ioqxcUtqwycw7fkV5WnoPWa8OwWWUnx99Io1oTZuMbopct1gYZg98HMgpFqArGoem8Gf9tAGX0k_iKIhWJVwP5cICmMnfg6CM0v2Ebpt5nZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079b034b2d.mp4?token=Fg_rJHWbtz6yi5AK9JRK5dDpo2Cxh3DabYTti6s9XmCWMqSHKsqK0vkc_bpHztUb5aIlhN29KrpSeLVUJ5E9FqsdVJ2r2pG8gj3bkUsIxpwnK-dNu6gNnpIl50l1x8PzeCd27ZojOgAa86IU_OduFBB7NDoh_RMMBXsnL-9OTw9befO5ODE-aI3sOtNJ6E5jvHpwj2sK1iT3E-SwoiwfcdtposqpG3hslduPVUFFE7ioqxcUtqwycw7fkV5WnoPWa8OwWWUnx99Io1oTZuMbopct1gYZg98HMgpFqArGoem8Gf9tAGX0k_iKIhWJVwP5cICmMnfg6CM0v2Ebpt5nZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: بانک‌ها باید از بنگاه‌داری دست بردارند و املاک غیربانکی خود را واگذار کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/696228" target="_blank">📅 23:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696227">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
کنگره آمریکا در گزارش اخیرِ خود فهرستی از جنگنده‌ها، بالگردها و پهپادهای آسیب‌دیده در جنگ با ایران را اعلام کرد
🔹
بر این اساس، فهرست هواگردهای خسارت‌دیده ارتش آمریکا در جنگ با ایران به شرح زیر است:
۱۲ فروند F-15
۱ فروند F-35
۲ فروند جت A-10
۷ فروند هواپیمای سوخت‌رسان KC-135
۱ فروند E-3 Sentry
۲ فروند هواگرد عملیات ویژه MC-130J
۴۵ فروند پهپاد MQ-9
۱ فروند بالگرد آپاچی
۱ فروند پهپاد MQ-4
۳ فروند پهپاد MQ-1
۱ فروند بالگرد امداد و نجات
۴ فروند بالگرد AH-6
۱ فروند بالگرد Sea Hawk
📲
﻿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/696227" target="_blank">📅 22:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696226">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
همتی: کالابرگ ۴۲ میلیون نفر حداقل ۵۰ درصد افزایش می‌یابد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/696226" target="_blank">📅 22:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696225">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای ترامپ: مقادیر بسیار عظیمی، میلیون‌ها بشکه نفت، فقط طی چند روز گذشته تحویل داده شده است
🔹
ما اکنون نفت را با سطوحی عبور می‌دهیم که حتی به سطح پیش از جنگ رسیده و گاهی نیز از آن فراتر رفته است. #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/696225" target="_blank">📅 22:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696224">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای ترامپ: مقادیر بسیار عظیمی، میلیون‌ها بشکه نفت، فقط طی چند روز گذشته تحویل داده شده است
🔹
ما اکنون نفت را با سطوحی عبور می‌دهیم که حتی به سطح پیش از جنگ رسیده و گاهی نیز از آن فراتر رفته است.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/696224" target="_blank">📅 22:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696223">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e439ad57a1.mp4?token=IWN-5hUzKmYaHw9nOzqOCekrbKg0locEys1HvU7YkhG8MSOsit5jXyS2BNZZnSVswhv2Kd0QLNanFMR-T1baHUxqHGk28rnOSLETR9gj8ppCfJ7NreAT1AQ49AUwDaxaWJrr8acZ7kYtKgN6ylS9yU4g50B7bVhJ9dP05TXDH8QD-udAT5uZV2s0FiDEKsvfeM1CMYp1inUiskeFOYtHeUAeeQHqiQ0gqGZgErooKWSu-ciyRt73WkR2WBbfbKDNdX89w0FUG-3BNyRJgzDz_noz-TQkHVk0Nc8I_sIUPbWy9wuVFAuOPyJ-4osJS10ppMwBHm3iyeDigpqcrRGCuLOB6Qsp923o-PpaxUimxtmbC3Ossb40GuPaplJbD22hf-ONRVuDqG5EWNWysUzTxlzsUr2QXR2uy0AFHgGzc5jbBHhzpQHI9ow2HHswc8kHsigI_whJqRIBh8xl50cugelzXCKpbEf9n-LGhJ5Uz4GT1vLe2eIXKavqvkTRqswlMXAGua3ftoT4aO59g_ShWbByJC8i90xppM_8ihzRUFO-xU-BM2NF4xeDkfbf64PCLlBFzltsSm7sjn5XA-kfJ_Z80rEyPdI_CMNpizgtH8BuvaBUuK_DXUnrkFHI0sT6CdTHXExzCl_-l2ZSPfbXRamKl28lt80aJt0bxP5hy0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e439ad57a1.mp4?token=IWN-5hUzKmYaHw9nOzqOCekrbKg0locEys1HvU7YkhG8MSOsit5jXyS2BNZZnSVswhv2Kd0QLNanFMR-T1baHUxqHGk28rnOSLETR9gj8ppCfJ7NreAT1AQ49AUwDaxaWJrr8acZ7kYtKgN6ylS9yU4g50B7bVhJ9dP05TXDH8QD-udAT5uZV2s0FiDEKsvfeM1CMYp1inUiskeFOYtHeUAeeQHqiQ0gqGZgErooKWSu-ciyRt73WkR2WBbfbKDNdX89w0FUG-3BNyRJgzDz_noz-TQkHVk0Nc8I_sIUPbWy9wuVFAuOPyJ-4osJS10ppMwBHm3iyeDigpqcrRGCuLOB6Qsp923o-PpaxUimxtmbC3Ossb40GuPaplJbD22hf-ONRVuDqG5EWNWysUzTxlzsUr2QXR2uy0AFHgGzc5jbBHhzpQHI9ow2HHswc8kHsigI_whJqRIBh8xl50cugelzXCKpbEf9n-LGhJ5Uz4GT1vLe2eIXKavqvkTRqswlMXAGua3ftoT4aO59g_ShWbByJC8i90xppM_8ihzRUFO-xU-BM2NF4xeDkfbf64PCLlBFzltsSm7sjn5XA-kfJ_Z80rEyPdI_CMNpizgtH8BuvaBUuK_DXUnrkFHI0sT6CdTHXExzCl_-l2ZSPfbXRamKl28lt80aJt0bxP5hy0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از کنکور چگونه انتخاب رشته کنیم؟
محمدمهدی محبی، روان‌شناس و مشاور تحصیلی:
🔹
انتخاب رشته نیازمند نگاهی همه‌جانبه است؛ نباید تمام تمرکز را تنها بر یک رشته خاص گذاشت، بلکه باید شرایط خوابگاهی، هزینه‌ها و سایر گزینه‌های متناسب با رتبه را نیز به دقت تحقیق و ارزیابی کرد./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/696223" target="_blank">📅 22:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696222">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
رئیس کل بانک مرکزی: تا نیمه مهر حدود ۲۴.۹ میلیارد دلار ارز برای واردات کالا تأمین شده که نسبت به مدت مشابه سال قبل حدود ۱۲ درصد کاهش دارد
🔹
این کاهش عمدتاً مربوط به بخش صنعت بوده و تأمین ارز کالاهای اساسی کاهش نداشته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/696222" target="_blank">📅 22:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696220">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
عبدالناصر همتی: به بسنت پیام دادم من به راحتی می توانم ۲ میلیارد دلار اسکانس در بازار می دهم. فکر نکنید با توییت می توانید اقتصاد ما را بهم بریزید
🔹
بسنت اعلام کرد تا دو هفته دیگر ایران فروپاشی اقتصادی می شود. ده روز از این دو هفته گذشت و اتفاقی نیافتاد.…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/696220" target="_blank">📅 22:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696219">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
رئیس بانک مرکز: من گفتم میلیارد ها دلار خریدیم و دپو کردیم حالا فکر کرده اند ما رفتیم از فردوسی دلار خریدیم؛ منظور من چیز دیگری بود
🔹
به مقام معظم رهبری هم پیام دادم خیالش از بابت تامین ارز کالاهای اساسی راحت باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/696219" target="_blank">📅 22:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696218">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
رئیس بانک مرکز: من گفتم میلیارد ها دلار خریدیم و دپو کردیم حالا فکر کرده اند ما رفتیم از فردوسی دلار خریدیم؛ منظور من چیز دیگری بود
🔹
به مقام معظم رهبری هم پیام دادم خیالش از بابت تامین ارز کالاهای اساسی راحت باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/696218" target="_blank">📅 22:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696216">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb-vSzpD6uhnG2Mq1-ntpe6XRTLvKEgGz59Hw7WtIzSddNyBmAvTfD9qFVVKW8TpSc63YgBqz3jpB8IhHzcTG43l1b2K0wp7ZNmjokD1giXDnPJ-f6XifMwxT1EjyhyTmwQsbfsM-bnl-b7hHV8vpUNSJvDpRk-abhZUNhzG3gbhMr8aLDL5W771Q3GQxC4rM0raGsjV-BVU3bTYWgJQeEqQyqUs-BWy5myy6EmhZHswYOxzj0Ld3SkDvimC6sVynOUSA_m9Z7DZprUaWZlgkm9c6Ae0xG2tdgFEjZ6iQlvE6pwiDPZXYlh1lvaAEQ6uMTalssKJEY-8rMlQvNbl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست وزرای مستعفی در ادوار مختلف دولت‌ها
🔹
از دولت بنی‌صدر تا دولت پزشکیان؛ کدام وزرا استعفا دادند؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/696216" target="_blank">📅 22:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696214">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jh1KdOJWxI259ZNL7V4kGPQXdEzawSNWcP-NIWTEGihHHLbbQAfZCrvfNmwuKDVTBmj89FhJ9lnoJMcK-1lScLRERdfPJ7B4Ok9ObXMcze315Jln6wp8aIDjW5UAG1adojpFrklf8Ea_YNe36FHzWwT27xe0MYcik3LIzwApfNFGU8Aua63qN3Kyo1TKdnUrOi-yW2zuaDMHucu9ZdJvRxZq_aXzU_19ezDOY6Zxf9tynXFm_0lHDieiQRuwD3Sh5sw8NKSPon5-rcbcPzvuWAPPyA4oTPUUrxs5HO5YEr-YxEopsHIvqk-UiEnkoD6mKu3Opx249t8DieGISBekCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/os2iErzezQnTYFtl4QQU_QrC0zibrn-IkdhdsdekBg-kuMQhXIhcwQ-exCNNtIanz1op4yyKMr07t5kwXmPcmLIk506v1m89Y8ImcUP2DDlIAcvFMC8tARWPdAJkOByG-NBXQNMst3Mo4eRTxeIqEI3yHteHGw94EAcf6ct5rkf4wevnPtNiZwg0IXnX-mrWAd3Tgw6hCTsU0wo55EzCIVlrTeTsITSJaAkfhI8b_PiY4sKDd6f-nFz9yEuz0V-NnBVUcT66Lbvexpt89TKxUY9qIcStQHorgo9V_LC5p0iik6vs3OKxRUqisEEVA9lf0sccIykfXTlCZ3c1OTEewg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدل‌های iPhone 18 Pro پس از یک هفته از خرید، شروع به رنگ‌پریدگی می‌کنند!
🔹
برخی کاربران از تغییر رنگ مدل‌های قرمز و مشکی آیفون ۱۸ پرو، به‌ویژه اطراف دوربین‌ها، خبر داده‌اند؛ مشکلی که یادآور تغییر رنگ مدل نارنجی آیفون ۱۷ پرو است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/696214" target="_blank">📅 22:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696213">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
فاکس نیوز: ناو هواپیمابر «بوش» خاورمیانه را ترک می‌کند و تنها ناو هواپیمابر «جورج واشینگتن» در منطقه خواهد ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/696213" target="_blank">📅 22:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696212">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW_9d9OLlayUM2sSpnuquQs2VFywMZpleVAmMgsFmY1tXUZ7v1BA43_bC5RgSj_f_XpKXh5xLgoCdHvx_D3NPxNdF8yWZzykXs6CuOEckMuLbSmrYJ-LkaL60NN5ArLPv0YcVMxkBucGU3Hm4BgRhCIjuNwUzFb-89qGhsANkd68bX7psZHNfBFcXd_jtLwOCcjv-6DXG75pp1jAh5xvNaqCU-iG_OMncWR09LsYmGbmEBl33MLy5acDBiaE7unK3ggK94Dz0n0wQ0t3XhCzPZl4jznV9KOeZBlgHs3R1Hnpm0Kj1AQeelld6qqamnsSV-_oimqFWkMkXXMjIrX8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام رئیس بانک مرکزی، نرخ رشد نقدینگی نسبت به ماه های قبل، کاهشی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/696212" target="_blank">📅 22:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696211">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
فارس: جنگنده‌های آمریکایی در چند روز گذشته چند بار تا نزدیک مرزهای ایران آمدند مانور انجام دادند و برگشتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/696211" target="_blank">📅 22:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696210">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzoMCToS6fxHK30g91lTOGGuBYrMSS1Ujh5s2rBPEhgqKes104RSiXb7UnP-dMT2UzC3OKGUPF2aSDE9Lw-THKr_Wa3O2uPJDxHv0EZGoor3d7HiGK5ns-Zoxgo57IOuvgXvHXAY8LXOAytgBNEKlh3HZEjrNG9sS9of5y0enTO_0Lx2RTQAhrFvK9aekigx4C4lFhTUFHJSOINMucV6NQoE595kZ5cTpWKf343KmyKLsfZEjAtiV4wgarvoNWfoSYR8dqOrvqeq-NrPbHMMCqFHUfoXGBt9ue7z97NlViTH1coSmbuhOXQ1p7mjRyrlEbjb9pG6d88CHs4Al0sVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف در واکنش به اظهارات وزیر خزانه‌داری آمریکا، با انتشار یک میم اقتصادی: آماده‌ای تا روح تو را تسخیر کند؟
🔹
در تصویر دیوید زرووس، مشاور ویژه جدید بسنت و حامی کاهش نرخ بهره، دیده می‌شود؛ همان کسی که گفته بود تا فدرال‌رزرو نرخ بهره را پایین نیاورد، موهایش را کوتاه نمی‌کند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/696210" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696209">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26145c3b5.mp4?token=Rwr2NaW9y-nrqwfOsHbmizYqD2jCS5pbNTxuK1Ily_a8cTeSyq7DiRZjjDMlraKEm3D9WsJI0CIyQa219qGe5b2X-Clg3S4pi3CaRbEL87FMyj4o2oaL_G-_eMXSH_Mhm1q-oyq7Och4newk0mbg7OsV-cawHhzHWCkI8w2zodVoQ1u4TqpG-xbelsUTrro8eK_YRIE8oSWJOICc7GET5Pqsa7eHfO5nkGphq_XWrKb4DG6urdXuGOOFJfAFC8bcLpuUqTxrMbQ84PA5d7NjDpN8iDExeuqar0jjUhliUYqfKZXeCnyk73haSVbG5U0wTZ6MRaLjuTKEnrJBlphRwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26145c3b5.mp4?token=Rwr2NaW9y-nrqwfOsHbmizYqD2jCS5pbNTxuK1Ily_a8cTeSyq7DiRZjjDMlraKEm3D9WsJI0CIyQa219qGe5b2X-Clg3S4pi3CaRbEL87FMyj4o2oaL_G-_eMXSH_Mhm1q-oyq7Och4newk0mbg7OsV-cawHhzHWCkI8w2zodVoQ1u4TqpG-xbelsUTrro8eK_YRIE8oSWJOICc7GET5Pqsa7eHfO5nkGphq_XWrKb4DG6urdXuGOOFJfAFC8bcLpuUqTxrMbQ84PA5d7NjDpN8iDExeuqar0jjUhliUYqfKZXeCnyk73haSVbG5U0wTZ6MRaLjuTKEnrJBlphRwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توقف مسابقات فوتبال در آرژانتین در دقیقه ۱٠ به احترام مسی  سایت «ESPN»:
🔹
با تصمیم فدراسیون فوتبال این کشور، قرار است تمام بازی‌های فوتبال در این کشور در هفته پیش روی لیگ‌های مختلف مردان و بانوان در دقیقه ۱۰ متوقف شده و به پاس قدردانی از دوران حرفه‌ای مسی…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/696209" target="_blank">📅 22:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696208">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def57d600a.mp4?token=AzcADsbZz-eTEKFrNSxACHH_YTUhf3ktUEN4JcHpqM6SjFmVbbWjkRwUI1CV2KnyZWOaGviSaS4Lf_KlM25z7YhaxCEA3RA_0q_LX2PQKO11Mywq5Sd1Gdyi78YCeZEKfw_06vclo-RzFXksTxRoosHHjvnZhnhHPsdpAd7RNbGwmRGM6mB7fs_NecvAUurE9jFL4wCjwnGEQFln8ZATDxQPl5B8tilYgkN_jp12qpcNqVjDpvv26rdKv4rtBkQ-Yykiw7RjfRX8gvg31ZDCYWnHgZv92BmcJnXVUVaINWjv6m-miHUyh78aignEYhTIJrU8i_2sJP4SXHVp1bse4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def57d600a.mp4?token=AzcADsbZz-eTEKFrNSxACHH_YTUhf3ktUEN4JcHpqM6SjFmVbbWjkRwUI1CV2KnyZWOaGviSaS4Lf_KlM25z7YhaxCEA3RA_0q_LX2PQKO11Mywq5Sd1Gdyi78YCeZEKfw_06vclo-RzFXksTxRoosHHjvnZhnhHPsdpAd7RNbGwmRGM6mB7fs_NecvAUurE9jFL4wCjwnGEQFln8ZATDxQPl5B8tilYgkN_jp12qpcNqVjDpvv26rdKv4rtBkQ-Yykiw7RjfRX8gvg31ZDCYWnHgZv92BmcJnXVUVaINWjv6m-miHUyh78aignEYhTIJrU8i_2sJP4SXHVp1bse4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ اعتراضات در فرانسه را به اسلام نسبت داد  ترامپ در تروث‌سوشال:
🔹
مهاجرت انبوه و از کنترل خارج. این موضوع درباره مدارس نیست، این درباره اسلام است که می‌خواهد کشوری را که زمانی بزرگ بود تصاحب کند!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/696208" target="_blank">📅 22:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696207">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as6g3wWPVG_MJIGmLYxkB6-pU_ABBpm56hHGz0kxgIN3_jKoqoq4qLtP5TW4ZeRWnmmNUhjhqVXlugdQ313FAwABAwh4RYFudo6jIzuQ6nzXjHjRcbL-K4pmg6lg4sq5XvCXgKBvxt7Z3dZLVHxf_E1K-SxEPbyquYnh_GNPBfEWtqAjxQ-_mKhjRRQVACBjHjCEj7NyAPulrFUneM1PG-OsL5EONY5AXPRASN0vO_ss94AmNvFfoABnMK9RRBM3RB6sJZ31um2-V9Qe3REvbkIkhFv0hrzFZzEoevrU1jllxPinsr3xKNCaV8HLHrpqho03XlHcCXWz3CNhOmtZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت دلار فردا افزایشی است یا کاهشی؟
🔹
دلار، طلا، بورس، مسکن و اقتصاد هر روز با یک خبر تکان می‌خورند؛ مهم این است که بفهمی کدام خبر واقعاً مهم است و بعد از آن چه اتفاقی ممکن است برای بازار بیافتد.
🔹
این کانال رو به تیم مدیریت می‌کنه که از اتفاقات بازار زودتر خبر داره و همه چیز میگه
👇
👇
@EconWar
@EconWar
@EconWar</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/696207" target="_blank">📅 21:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696206">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
علیرضا مطلبی: سلیقه گرون داشته باشید سلیقه گرون باعث میشه پول بیشتری در بیارید/کسی که سلیقه گرون داره در خودش یه چیزی میبینه که دنبال بهترین میره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/696206" target="_blank">📅 21:57 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
