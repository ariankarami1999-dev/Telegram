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
<img src="https://cdn4.telesco.pe/file/Rzl0lk4EP-mIODiP2PIxaxPhHaxtMXOGvAHK3w0M1ohVNd81zI_WH6OUhyqCQ7byVlkRoTw7QYqxYYkIxKNqwjkyvU_-ztHOJ3IHYYC_XbA-vsn9NgpmLdwwWhHqJMRuTPZRljzOYJ1VbBvjou9nY6VODcH16wMFRUsPfYi1XxI5W5yKTHFyLFgyMKt-FrGjDS9zZGz2M4vl-vM_u0yb3YNjbOON3CvaUAVRTButj9cpx55MYyy5TLNjvIMzJz57lHKBjuyNcY0Jl4xX5i6WWL3DhE1dCMttMWwGYCeyd-pn2li6LAuyjt4aiI0XRjyxXDjIeQI9Qn8026SSAJtDqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 19:56:33</div>
<hr>

<div class="tg-post" id="msg-81834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCHzRBKnRly5oknNzgJkhcI7o25uDcqKc6ejavoAu9MiXM84jlyR-7IR0CWrg1EpMxzWci5VKCVfzWOD6K_yJ9YXcCzWtMV3mfAXLaPmXavtfxpU-QW2re3W_gRluxQzIgaQSRYJXN66cpyIsvIHKVYyoPBQX8qyat1bO96ELM4yzcNPMasK4doVG8H8qy1DJNKBGll6IUB4VweG9BcqYcx8k_euyeCAmkSv5c1qhFLYtnw8w1ZpoDcubcKs1jI9DhXlU162rQPMhVSx6ewDhOGFx2CQNfFtzAbQwAYX64t4hU60-N9FWSwohoK-iEPGLUsbRypLRopZsZusdplkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس قشنگ معلومه چندسال منتظر این لحظه بود یه آتو از مهدیار و فدایی گیر بیاره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/funhiphop/81834" target="_blank">📅 19:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پوری و مهیارم ترک میدن نیم ساعت دیگه</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/funhiphop/81833" target="_blank">📅 19:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81831">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFOj63I0ZQSk3ESPqDoVejUBhiLyZFnZHgByfEwQ0-WMlJ1yljDxEFG5s-8ZwLpPeoPOHNjBiHUPZOQxebNRnZ92rgF5iMk7TR7Pf_TQdOO23bzdYaijLxXPz_TkdezyF0oPxWPxCx4N17I-SXOa9ByzdreI3a8gv5c5ustx_hE5QeN3GW0pWb-c5TojBduvmOqUYIgg9W-URhJ6srzXseGKk5o3DbHmEsoIBnm4Kjyoq00mhJL2xzxtpOawjKKmriDygy4fZR2phtfQWid31wx3cEj6EJsY_Zwv-c3cvzfujzNK5DV_-JNsWCZfdnMQuFkUy-8agwoYFVpHvxoiDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دورچی به نام "EDGEBAR" منتشر شد
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/funhiphop/81831" target="_blank">📅 19:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81830">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd1550d00.mp4?token=ukNYOweBsJLg34Gd-lfsVwPMdkSxqrpuo2p-ttBQlp1X4RMD-G9ci_DgB6-0ieZoiABxHzzFqSThp7sdRpHmNRqYf0gO2L0nSvYTtAPUmFUIEwzxEIJM6CvmO1qWVMEMU8XJyT--z9VVvYzGqDj7gVNR1_MhQv9oowigIH1N9EYy7Kgeo8uIk0EFzX9o4FspOz1CcgVcWpV_TypFT5BuUEDblRcLEepWSJ02SiZdWWH5cgOXBgr7jvUqLTQVXNausLDDfDpmKuT3ZkKAjQOANaj3KlcafcfQdP6TkROVQfWZd-B0RQC1Qb_Goj09ihjyws6UkjDogSjBM9YSZ4TIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd1550d00.mp4?token=ukNYOweBsJLg34Gd-lfsVwPMdkSxqrpuo2p-ttBQlp1X4RMD-G9ci_DgB6-0ieZoiABxHzzFqSThp7sdRpHmNRqYf0gO2L0nSvYTtAPUmFUIEwzxEIJM6CvmO1qWVMEMU8XJyT--z9VVvYzGqDj7gVNR1_MhQv9oowigIH1N9EYy7Kgeo8uIk0EFzX9o4FspOz1CcgVcWpV_TypFT5BuUEDblRcLEepWSJ02SiZdWWH5cgOXBgr7jvUqLTQVXNausLDDfDpmKuT3ZkKAjQOANaj3KlcafcfQdP6TkROVQfWZd-B0RQC1Qb_Goj09ihjyws6UkjDogSjBM9YSZ4TIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین فوت فتیش ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/81830" target="_blank">📅 19:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81829">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترک جدید هودادکا به نام "میبخشم" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/81829" target="_blank">📅 18:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81828">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STv0hBvoSwH4pQbVHDCAoO6sZ0hxEuW2W7uwkKSmbV51y4fgCBi_QI8_oI5Qpd2ahj8G34ayopIisl2EUeSi4v2u2QpFPnecdE-0ZQcBt2IMtrJ33XUrsnWlzX5izPaHoRQDGbhESnd4uX1UdTcIL3JTPxvU488pUyhDgzSxVXt7NNb6DKrlhf0_dDx13YFb-rhYuiQnZ97Mc09Pe7D3-gK1RktniTUt74ZCbJlg8K5RLhTlQw0V0D6Mm0zNw17gxrAz3XHTEb56HdQdChTu0-N5HCOICIjRbo-202ACBT41Vs6Otv4yBdWywdO0Y88kFI2W2F2Y5NvarcCHyPjipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام "میبخشم" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/81828" target="_blank">📅 18:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81827">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کیر تو رویترز و رسانه‌های اصلاح طلب با تیترای زردشون، تاحالا فقط اعلامیه لغو تحریمای یه سری شرکت هواپیمایی متفرقه مرتبط با سپاه رو تو سایت وزارت خزانه‌داری آمریکا ثبت شده.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/81827" target="_blank">📅 18:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81826">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMg0mydFvaeCI3kZlFBkDLJSlZ5PNuAiUDG2_LV9abQxt43sXO92QxoQSFrXx2uwbEkgx6PkzXHkMH87rTWE0ORbEelzqtJAs4IItncHZ6LfE1qJ7KrzI67cbmQ6fuXz_y4zVhUZnM20PPXeGiRcynEZpVrnpVJAjwi9ejRsF7PsGshWvqDF0Vjvvfvg8_Mn69AGycVjAPHmCGPKCB8RFL_ftP9YFIywV7Q6PfjEBWnrqHc_lcBldBFF1n1-U45_dUr0CiMH4LcZiY5p7ic94xoeUAdN7TNtrKiIBdmKa5-0ozpf6H9cZ6VghnmBdX28E1-vn0TdqVhgyCIntrDgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوریا پورسرخ چه کراشی شده
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/funhiphop/81826" target="_blank">📅 18:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81825">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5UCxoEGJl931Px7jLMVSfpQgXAbYBdOTe1zHKEcUc381iKMPVTQO0e9YWKyNnYatp9Pyvb5GS4sID1BisDjI33CGqTl8u932iCUAJc6tIoAzDXga193PndvoGpyeunghE1YYw8IPwbWx63XCrv1vUQ6M8cd_yWzbnO3a36CcZn2ffFT83X9EBZQSCtKu3HhwK0JgmNczJJ9jPfyaVrZYVr43Ogx8ckunoYSPH6-5q_8GXx8EZv0ZCAleyrtLB1QE5j3nuEWP3i46EwGd9mBbsV7_gaUor4lhxkWdYvVJYeuhg9ZPe7E7zL3RaSZRzGYvO5PXT0Q2KSY0aJt9rW3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
پیش‌بینی گروهی (توتو)
🎁
مجموع جوایز ۸ میلیارد ریالی بت‌فوروارد در انتظار شماست!
💰
📝
با شرکت در برگه‌های پیش‌بینی گروهی یا همان توتو بت‌فوروارد، با پیش‌بینی صحیح ۱۰ مسابقه، بدون قرعه‌کشی، در جایزه ۸ میلیارد ریالی سهیم باشید! حتی با یک یا دو پیش‌بینی اشتباه، شانس شما برای دریافت جوایز دیگر همچنان پابرجاست.
💥
فرصتی طلایی برای تبدیل دانش ورزشی خود به بردهای بزرگ
🌟
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@betforward</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/81825" target="_blank">📅 18:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81824">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رویترز هم تایید کرد، تو وبسایت رسمی وزارت خزانه‌داری آمریکا اعلام شده و قسمت تحریم‌های مربوط به ایران آپدیت شده و اعلام شده که لغو شدن، حالا اینکه همه تحریم‌ها یا یه بخشیشون مشخص نیست هنوز.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/funhiphop/81824" target="_blank">📅 17:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81823">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آمریکا تسلیم شد. اسکای نیوز عربی:  وزارت خزانه‌داری آمریکا اعلام کرد تحریم‌های مرتبط با ایران را لغو کرده است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/funhiphop/81823" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81822">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آمریکا تسلیم شد.
اسکای نیوز عربی:
وزارت خزانه‌داری آمریکا اعلام کرد تحریم‌های مرتبط با ایران را لغو کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/81822" target="_blank">📅 17:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81821">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اسرائیل هم وقتی توافق ایران و آمریکا جدی میشه میره عصبانیتشو سر لبنان خالی میکنه و خارشو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/81821" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81820">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حسن روحانی:
یه سری ادم مومن احمق کم تعداد که با اسلام زیاد اشنایی ندارن فکرمیکنن اگه این جنگ تشدید بشه امام زمان زودتر ظهور میکنه‌
یکی حسنو بگیره تا غرق نشده تو استخر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81820" target="_blank">📅 16:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81819">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هرچقدرم بگید طرف اسکی میره و فلان، درحال حاضر هر ترکی تو رپفارس میاد و اسم کاگان کنارشه مخاطب حداقل یبار پلی میکنه اون ترکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/81819" target="_blank">📅 16:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81818">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هروقت اشکان کاگان ترکیو درست کرد که مثل رانندگی در مستی خفن بود بعد میتونه بیاد نظر بده</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81818" target="_blank">📅 16:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81817">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dahRoLAWn__dKZBmfGBHDKQ8Raod3cd0AkStNatlVBwrptTRWU0wkBaIdphVy6qGZvNjzALHAUuNWjnvIzmo7aY67hjipGfIjWHNE6YJmZf0sqTWdduHnBSyM2nzhCVtYfWuEA5OCRZgEfBIQYCOKLQQtij1zH_rxRQgIAiXuIIz3GvCbRfj6Fq1lZLPcJ12gGjxK-DhFjbjCUHnxeFtwiRduevQ817FFRKrOwvXsqH5Q1UNEZsJ_KWYAPYVfW9iGh463AvO5i_4nECDDTZy4cr8J6Lh5Ivm2lFw55BqsO9mwIEt4Qyt9_zzJwSKQp42O5G_LO6zmvSnprDMyL-nLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربون دهنت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81817" target="_blank">📅 15:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81816">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07a77cdda.mp4?token=sbhZItkiWMIrjbrhVfjRN-tLbldAJDa-e4r_iBLk7fZB0CG-5IJU0-ZfkSsIcrK1DdQBMQR7Gjf6RIX4R_CrRRLkYZ4bIfVOeg_KZB2tIc58VAztG2Q_mT5Tj_Dt3-bpIEMa0NOJnOek5-OtDDP-PCKldX5_LfV-9_PUoxtgInt53HcW7TKqm-nI-LYlrBxhj18xyEyOeQvk1d-jqQ3jCJRypg_rJ-kknA5pwbY5u88-XplRT8WnmuGpNOl6_Hl328DwzdoMop20ojqDEtE2tJeO99qWhRui_gHL_EYir0NzD3SbFtnrDaxh_Baqx43eCaZHF1iIBPNrRwyu3xRTvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07a77cdda.mp4?token=sbhZItkiWMIrjbrhVfjRN-tLbldAJDa-e4r_iBLk7fZB0CG-5IJU0-ZfkSsIcrK1DdQBMQR7Gjf6RIX4R_CrRRLkYZ4bIfVOeg_KZB2tIc58VAztG2Q_mT5Tj_Dt3-bpIEMa0NOJnOek5-OtDDP-PCKldX5_LfV-9_PUoxtgInt53HcW7TKqm-nI-LYlrBxhj18xyEyOeQvk1d-jqQ3jCJRypg_rJ-kknA5pwbY5u88-XplRT8WnmuGpNOl6_Hl328DwzdoMop20ojqDEtE2tJeO99qWhRui_gHL_EYir0NzD3SbFtnrDaxh_Baqx43eCaZHF1iIBPNrRwyu3xRTvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قربون دهنت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/81816" target="_blank">📅 15:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81815">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGzOdG_qfAaaRov3vDvZ47_MC0i8uHKdO1F58YKe5BCr_wJ4pCSfWdbd-ERrILyNF4-Xn8sLDQ98WUyD7yQje5UKqLcH5XF9f8fF1cbSl8lb4NU6F06bBdCyqW7TPJLDIggBRlYroFEQ5aXwV7I2cKiF-ZAO5DIssrAWqXliTjqquHbup5qytP58RHmiGNK--gXGdTaR510AN_xJsWJih7DMC3yqrKzN91obHn05M4Vk3ro2b4TiIPHTLPc8HiqikasUmzIMxBnvyfDsK_zMaaEsG7DtHAyPzPoQFbOZ2HbvOBazaHZHuU-81Z9Fh0jMSyNvbh9Qf-oAae1N09-_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربون دهنت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/81815" target="_blank">📅 15:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81814">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دمت‌گرم کلی خاطرات خوب کودکی زنده شد برامون</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81814" target="_blank">📅 15:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81813">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-iVjXRzG9M7Lde2a0wlTCN0b9sc0HMMvXBNDgTVdpGZZ2xd-jz4UEXrlDzuWQW2kmguAPUTTFguNHgXrx-JBCEF5vx8v6Tka3V19DYZ_Ah-bw2_ZWsrjg9joEH7AMvilwOpW4KjPyE6BLyin_S9jJ3c3Pk1rcLtYdkZlPhItum-tuJXKfR6BLvy9kh-oiZTvY0evpf1REhbt1J91BiIjN3Oaoe9JHP691-UeQuroWckOGNYLNsZGBvBn5gjoudZXm1M7N_Av8E1EasPkimrJR9p4l26CHSWFfFV0TNfo5q816dZ976x8qWIemjp1UTQyoNW48Kjw4SAnnL0BEbWMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم سکسی ترین خوراکی دنیا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81813" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81812">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چیتوز چیپس با طعم چیلی تای داده بیرون.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81812" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81811">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPY774kp2AXCvn85hddkCZKsJh4szeimhn5iH8_3cBfJAVI23Q1HTpgNqmvUXdBW4NGxT75EyZXe9dkL7U2Hxzys2s2J5Y6imInqacE2MuKrt6QydCi-XMx81q9P4v3uMm_Yd3SRuggZdPrizJkW8BgxdJJWsF5EaUGX8mxLoCByuqlRYMbyOBCBZrO4qtPYdyjaoGN9KIB9lx9mbuUkTRmRYNJHXrb3og8H6J1__kbm0OcWyn81pkJG9WOFyoomYuVxffQB9koYvRFgavUseQ-H0drNSZpD9R3Z_GcdlvbzQpbcbcwJNaFCYy0vvslh0ZW7gQ2RCUyCFt2mSYB3gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیتوز چیپس با طعم چیلی تای داده بیرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81811" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/127bbc39c8.mp4?token=reQsZOFxLMa-BcZK_WqGnEYnuApnLwQ8RA1GE6kQHMBP1sKWTHYDP2VNsYblTYKvrjG4mNWR2bOYrdbnOEaVFjLBsIYeaSkHjVE6ak__dL_hbBu3bjR0c-DuidD1uckjNcfX2Wfr8R6hoYvYtQhK72rhWF-kaF99_cYpJRR1GTOg_r5oswA_r8jBSqmPag4vWvFlnecZv_QiLfzH5BXsveRCDNcF37ZvGrOBLnrJDqGrIf2R7-kjrmVLuTvEklnF3EgQYu-6fvm0LeP6qYdjYlJ6Aqvjuc6uv37hMKYMHu78Yj-9TeVqapHsVN7P6yL3kKsxFKmr04bZ1gqi0gLO1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/127bbc39c8.mp4?token=reQsZOFxLMa-BcZK_WqGnEYnuApnLwQ8RA1GE6kQHMBP1sKWTHYDP2VNsYblTYKvrjG4mNWR2bOYrdbnOEaVFjLBsIYeaSkHjVE6ak__dL_hbBu3bjR0c-DuidD1uckjNcfX2Wfr8R6hoYvYtQhK72rhWF-kaF99_cYpJRR1GTOg_r5oswA_r8jBSqmPag4vWvFlnecZv_QiLfzH5BXsveRCDNcF37ZvGrOBLnrJDqGrIf2R7-kjrmVLuTvEklnF3EgQYu-6fvm0LeP6qYdjYlJ6Aqvjuc6uv37hMKYMHu78Yj-9TeVqapHsVN7P6yL3kKsxFKmr04bZ1gqi0gLO1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان عذر می‌خوام مزاحم می‌شم می‌خواستم ببینم اگه کسی از تاریخچه‌ی این فروشگاه که پروردگار مسی دیروز رفته بود ازش خرید کنه اطلاع داره لطفا توضیح بده ممنون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81810" target="_blank">📅 13:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81809">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ گفته تنگه هرمز امروز یا فردا به طور کامل باز میشه و محاصره علیه ایران لغو میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81809" target="_blank">📅 12:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81808">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپو برای بار nام میخواستن ترور ‌کنن
حالا ما که میگیم ترور، ولی شما بخونید paid actor
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81808" target="_blank">📅 11:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81807">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJ4TFtnJncSjSnuAcGnDwzC3LExsLBjwnm3bqRkbj3ImVyJuQc8pX0zNIS4jz_wyb1BENPOvrWXKdsmPIG4kiCRdu5vNpFHR8dMW3Y77y-A64aD7aP5CbiRDxOfJ2tuZuNvU8UWx9ISZlw02IXRYlGbFWf0lYejLq1X7tZYqNXkPuX2T5-pQ2cp5aE2VKf6iOO4Qwdgq0IPRpzjgexAfoB0Y-0_zpzcYNc7NXhac5J2IS77wnx77Cg62kQGsGxg4sdQvaYQ5793QEpN72PnDkGxcvpdIJTwWxuehLEkL-L0Ik3iaILR2hS0TLXhM52peBb8ZqBPi3LLtjTKoCMTNbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش به نام "Fiancée" منتشر شد
Spotify
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81807" target="_blank">📅 11:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81806">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff90305b6.mp4?token=Xdd_mtJWnbOW8L8Uxqv9aDNjiBEwVwVl8cZRQhecSnhSL7yqMwEmp0f97eNece6klV1aOczp1JOIZBEXZndd7jesR2wMSDMkVzJMQHdmX27oXZvoXBljBNX5KOmyfK80WhVG_iRKvDNYIFfzhHauNf_JUdxssh465JvA7T63DA_xo1uOjN4dKXbSBp7ekO9CvwPUWJVRG_ZF-FepmgPPnYRxALRR06VBscWbjGzEmMyKJEPg3YZb37uC-C9eUeXrx9AoYdTiaJTIqWyhNJn-RwU9vjK8rtsR4WI5YwUizykcZMMkXvVYyx_yiVx4KC4cBVmpPRRhSqkQhv83IGbGbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff90305b6.mp4?token=Xdd_mtJWnbOW8L8Uxqv9aDNjiBEwVwVl8cZRQhecSnhSL7yqMwEmp0f97eNece6klV1aOczp1JOIZBEXZndd7jesR2wMSDMkVzJMQHdmX27oXZvoXBljBNX5KOmyfK80WhVG_iRKvDNYIFfzhHauNf_JUdxssh465JvA7T63DA_xo1uOjN4dKXbSBp7ekO9CvwPUWJVRG_ZF-FepmgPPnYRxALRR06VBscWbjGzEmMyKJEPg3YZb37uC-C9eUeXrx9AoYdTiaJTIqWyhNJn-RwU9vjK8rtsR4WI5YwUizykcZMMkXvVYyx_yiVx4KC4cBVmpPRRhSqkQhv83IGbGbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی این چیه آدرویت پست کرده اینستا، آخه چرا؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81806" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81805">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHhqoO0jw0vaEK-Mii6hBeBQP0llKy5WkDsAL4TC-uQ0G4f0p8fisPh2mdhouREKx6c7abhrLRDsCBWc6_deZnm-1sxTQpQHvfaE8fUQE79-fqe9hQhLv_Tugosm4AQBSSX1arZUr4TahpmU3KXt08QCDdJ6wDHWj6laQfeRQ3E79f7ydkErJ6NfSQ0ZRX2yCgKQmkzjZJQEs1ap7Wki0wQEULhYwVlrhYmtpLylZOYeWnkZ7GRfrbUW1m0m0_fwHJx-LGDLBC9pAoSBDo6T4EyRLTtyIoDENaCQN1LSe2k8Pb6IQHSM-E20ChEfFAYVCPqdymy7rL990VQuSjggUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
پیش‌بینی گروهی (توتو)
🎁
مجموع جوایز ۸ میلیارد ریالی بت‌فوروارد در انتظار شماست!
💰
📝
با شرکت در برگه‌های پیش‌بینی گروهی یا همان توتو بت‌فوروارد، با پیش‌بینی صحیح ۱۰ مسابقه، بدون قرعه‌کشی، در جایزه ۸ میلیارد ریالی سهیم باشید! حتی با یک یا دو پیش‌بینی اشتباه، شانس شما برای دریافت جوایز دیگر همچنان پابرجاست.
💥
فرصتی طلایی برای تبدیل دانش ورزشی خود به بردهای بزرگ
🌟
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@betforward</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81805" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81804">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ : ایران خودش زنگ زده مودبانه درخواست مذاکره دادند نمی‌دونم چرا انکارش میکنن
ـ داریم مذاکره می‌کنیم امیدوارم راجبه تنگه به توافق برسیم وگرنه ضربه محکمی میزنم.
-تا ۴۸ ساعت آینده خواهیم دید چه میشود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81804" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81803">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHbx9r2v6PUgJnToCMwavXHrUVvDnsJJ3PnHuWuZbwIC1IPBg2A2LU7qvVNaPj3Q3_pkkk791Gq68u1ySrHpcdNGyK-niSgdve9-JNQudRU_S3drj6qyPe6_wn6HWQww0OA1gb1Q0nlqzzWLVV5hOaVSMelEyDKYe3jQ3HZIDf9FF7M2x8vgYqsspgRNQVOA6Dzpksj6wrSgOyQaE30LzJ993XFigOMlWzeh-1XT16dMjK_DHeKX_QiUUOfybSP-fvWmKaD3S6Gn_5OEzy7zd_HJCrPhKBptz_cujrJUtBR3xJRbu9HFJzcJFDUHF5rEGVbgTQpUYFDmrtdrDD8-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81803" target="_blank">📅 02:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81802">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwUH2wT-vqxeR3qCk2tARqcj0BZk1t9no9zpMC8tZJ_m8PGxhL0kkhNv2tMAM5FEBsAW2H-vrcyynOSXLyK62cltMpo1OT_1y_DnkcU9PJO-uRiBfOEDVz8397Gy9OMVYIt0sls272UzUWj-We9HLLwX0vxsJ09HFrzcRNwtsD6CcJ8rlgFuwCwFGskaeY-YSe6xl-TPoMxNT7Ks1mAoD5atVGq1mUMGJ-Dgkzfhl29fqkuDZlLaJ58H_UEZOhbBdyHciCRSQu982rEEwDtuXwdWLqFt-o11W-GF2TsvN-TAJU5o0LamZE76kNGiPzavf6lk4a9d9yzdsh8oXN_RCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد هم اومد پیشم خوش اومدی سلطان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81802" target="_blank">📅 00:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81801">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from꓄ᥲһᥲ</strong></div>
<div class="tg-text">این ناموس کونیا دریای خزر رو دارن میفروشن به روسیه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81801" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81800">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from`</strong></div>
<div class="tg-text">این ناموس کونیا دریای خزر رو دارن میفروشن به روسیه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81800" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81799">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fuaf0_jgmaK_yGp8uF5pF2itV0ITFA-sE3QmABnwgKR41h7nkzT_HJkkYy5m4v2_8tMKPMYejOpBUSUXmY1B56zDsjQzCoglBIETRF17eP7Ce-mxTKLpTVqo2mxHDXEXClYUw3fJcHLvLQvgd9yFDK8KTbB3tg76SEW5Ju-RnYfRsXLCqTYFsw5cNdZNdpTUHWDMSiyifvhv2DUh9afem32lr3XaccBfC3O64RRrBzlctQNn019zH-tuu3X5RSRBkZxm6CF7TvYkF-SmCRpIvTJKFd2-WGidWvXaMOGL0jg4ZDo3DprAGfz1W5osYtVONCrDrcXTl-OD-Tr1sq7t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میتونم زن مدیریتو راضی نگه دارم، میشه استخدام بشم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81799" target="_blank">📅 23:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW6TOzXV8yWaefbAAuvv5nas0h5RIEmpWeCtHjN1iQy6JHfvKBlGG_hXN3ErGJbvsDNnQmSJIysZwTXFYj9Fk0w8vCbs4PCsih3RRWgHkmJX-ct7-IkaB-IHxUxpS7FmcBtt4C3zbIIVClej9md2_1sWzPqsHPX7xEO5fnJAiABuFl5twndAr5VO3Crw-4lcyR62ipbbOWxaaHssHRgnE--yQowOIwvl21whjhl040fYD0DwQ50_NDLjFiBkoZb2F_QEobjTGgT4cr6rQB5ivtAgPrMzw3RbL4B2tVwbmRyeAOHtzZuspSFK1LoCcHxSyaxmSgO6gsRDZntQkOd3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال پیش تو همچنین روزی، خیلیامون واسه اولین بار تو زندگیمون حس واقعی شکست عشقی رو تجربه کردیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81795" target="_blank">📅 23:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81794">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNRoEAPKn0A8iqjwOnOP9Lp8sI1qVV1COw3sL47lFEJVqhuZTQ5KAcAxmXl73JBiZetIJLVIyve3Cra-zsrd2eSpFWUOuPAAV3MIQjmA0e1pVR34P5Sfh-HDmO53zqwH6vIsxTroYhZ89JWfialH8iDklmvNXEVpSs5KoL154Itj2IXvzcXHy9HrWDxdQajrAthgg1eSiahnd1XPIo_29UdIFrCcQ2DwrFqbl1vYqaZSB_Mc8A3xKDz1Q0Jpzk04mZYit7kNjxDG2_VIr2LW9hH7gSw4D2p9qGjGre3v0k4QAMoJ5kjQ9QIpZ6qBfRBXRRDxASo102-4SkUFV1k8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیک
جیلنهال و پارتنرش از هم دیگه جدا شدن
💔
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81794" target="_blank">📅 22:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81793">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyBa-xE7clnojLrv4rugjsMWCzkdFpQzDWLG3xRwEpI1vPqXQBUle9co4Y_WN4eQHLU1ttIPLUND2Pw7BTqvcPN7_tJD0W7kjCHlYrODvVpNiKPKeF_LbMOVIgmjP2eBrqpHrI0i6daQvYkKj-8bGfV2tEzEbXSJlNVqxGnKgZ168iVkC_NCTJ70IhvCiZJPsUd8ALDzGE2DObdzdPmm_RVOD9nOhicT-X7bjS5pGDFfx58disczmEwwRSVUXKXPf_69cqmCpKbb-fuN2G4lpAXRnx9p2TpOTHHozhQMQUDTwQATBNbmMxvIktBhmGjCkK8HO47eaolm9NTaH9mO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپر اپلیکیشن بله وارد اپ استور شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81793" target="_blank">📅 22:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81792">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMVr8x-n_vrnELsRJPZ-vv432Sqz3_oWgGrMIbGYTCbNmx3gMynH5FiwGAm8IgoRvd2o3oUrAqRbSVYN31gYTEN3lugciJrV_bypVWaexWFlRJKb9y8W9llppWunyIp7PZjdsPMWDtR-hEvIg4dHS0a89CKlyLJa9ygv82zjFmnrqdhippkQkV_I1cxRtY_CnRjmLM4No7eWgVTvnoqP3j2tGEKLCFVvfi7-2kC3LSIcNHA93WrFUighvT7b5ErrUkK3Gq2EpEUk_zJJTEucKQdlHE3E1eg3XCjNQU8U4HqfTC7hw06X-EfjnDMwyrJ3zn3V-vu0jiyU1D2VMaN9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81792" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81791">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ارژنگ امیرفضلی:
بالابرید پایین بیاید، جنگ کنید یا نکنید، موشک بزنید یا نزنید، توافق بکنید یا نکنید؛
هیچ چیزی به قبل از 18 و 19 دی برنمیگرده.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81791" target="_blank">📅 21:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81790">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06551d5d7.mp4?token=B5Wi5G3z8k1LDydjLdCxRu6RF1a4XY02hzEEcUO5YASPGvIgN5XAe647o83BwWynl1OyHJ1omCPG44DQYqv3Of1cyHlJBRCGOC_zp3mHl-MA0U6I7bGe-tT0kB_X1eQ_ZvglX2OHe54O9n7hmx22NM75hL4hkYINr5CW3OPN6tnSYHOctveglUvcV8fn0eXlR_lpmcM5FZucOL8FvIVDUVr06kYrQrDI_0dOssxGLrIjOG0HNDgZ9pQM8ZXGiPw5mAdHpEYjEC0K1HUj1u4CXCqu9Rkpl0IQRhSNEQwxVuxFOP7CYokPsZ5nE6QlQGMk-fapAcDApGCL2d_-_Ov-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06551d5d7.mp4?token=B5Wi5G3z8k1LDydjLdCxRu6RF1a4XY02hzEEcUO5YASPGvIgN5XAe647o83BwWynl1OyHJ1omCPG44DQYqv3Of1cyHlJBRCGOC_zp3mHl-MA0U6I7bGe-tT0kB_X1eQ_ZvglX2OHe54O9n7hmx22NM75hL4hkYINr5CW3OPN6tnSYHOctveglUvcV8fn0eXlR_lpmcM5FZucOL8FvIVDUVr06kYrQrDI_0dOssxGLrIjOG0HNDgZ9pQM8ZXGiPw5mAdHpEYjEC0K1HUj1u4CXCqu9Rkpl0IQRhSNEQwxVuxFOP7CYokPsZ5nE6QlQGMk-fapAcDApGCL2d_-_Ov-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی: رضا پهلوی مقصره که به مردم گفت برن خیابون کشتار دی ماه کار جاسوسای موساد بوده، کسایی که کشته شدن بخاطر بالا پایین شدن هورموناشون رفته بودن خیابون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81790" target="_blank">📅 20:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81789">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">طبق کصشرایی که گفتن، از این به بعد کشتی ها و نفتکش ها از آب های تحت حاکمیت ایران از تنگه برای ورود به خلیج فارس رد میشن و برای خروج از طرف عمان رد میشن، و در ازاش آمریکا محاصره دریایی رو به طور کامل بر میداره. به هیچ کشوری حق گرفتن عوارض از تنگه هرمز داده…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81789" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81788">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طبق کصشرایی که گفتن، از این به بعد کشتی ها و نفتکش ها از آب های تحت حاکمیت ایران از تنگه برای ورود به خلیج فارس رد میشن و برای خروج از طرف عمان رد میشن، و در ازاش آمریکا محاصره دریایی رو به طور کامل بر میداره.
به هیچ کشوری حق گرفتن عوارض از تنگه هرمز داده نمیشه و ایران و عمان باید تنگه رو به عنوان یک آبراه بین المللی بپذیرن و بعد از توافق کامل و پایان شرایط جنگی/عملیاتی بین دو کشور، ایران دیگه حق نظارت بر کشتی هایی که مقصدشون بنادر ایران نیست نداره‌، ولی تا رسیدن به توافق نهایی ایران حق نظارت رو داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81788" target="_blank">📅 20:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81786">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esyyxULBcvoPdI4EETi1YnxNbpkyLeHrjsStM2lNVaXy-uP_Ns7HibcTAp97P8_ShFXDKpkcU1-5m0UgvvmzZj4yFXzEn2i3nsXG-qNrd8JjxDKu18PuX1M-NbtR4q_F9aCqobCeZXP1HR4saknlQL5heUXZVG1duznGn1uk7rDL8iSF9xaC80qNA2V6waGtiP-8_D_vvIWL0zBCGUPqUEj57LakNprCFsbd4O5SvWVl3WItxaDleQMZRsOvpaJdh9u5AnXtlrjfUB_kdxXXc3QaA5ZTd8USePILDTcUKM3QAu6-ZEcmtBsKnHEq-NDSBDa5xV57xvDW22YDHDaMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4S8ezHQIGYAAFn3av_wv1wrdeqyW7gUH4NlAlZKRzoTobxdDdhc4bCK6UIKsUa4pvWKGxlCx5IhoOtPwhMInSYTsYXSjGVSIjt3An0XzxzQSId4oLSkC8OBOio3kV32R45qLhYQyB6nFO7xdLflJxoXYI3R5JpTGlDPaMD1CJDaRbERnhFnvwcVrtyuUF3FZ8l5Amc9DRHF3ZwSh0C76OwBKYnB3pfcmm0INrCjRS0mnA4TF5pHoAlNpVd2o5Hx2nfuZmB-WI-ygXbj9zQ8O9hRGh9BFWz6O6tmez0RJeCNHhPt_E9EbZSQunybKJIjx_lJyYS5oWLJxOgw1tRYfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ریدم حاجی اینجا رو زدن فک کنم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81786" target="_blank">📅 19:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81785">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ریدم حاجی اینجا رو زدن فک کنم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81785" target="_blank">📅 19:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81784">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تقریبا همه خبرگذاری های رسمی پالس های مثبت از مذاکرات ایران و  آمریکا میدن، فقط مونده فارس و تسنیم تکذیب کنن تا دیگه مطمئن شیم که توافق قطعی شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81784" target="_blank">📅 18:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81780">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUvko4LPUuxCoxbbRtdwtPacobKHyTiST6xOhuwfQIr_kF5lbEJq-FIT3Vv8Ta8hVPcHqBgDiLxQ8XomAeZmq813T4ujL87Z4OXajs7Sb0D_OHdhICPL8fRPm-aVgk7DaLalm5-f4KC2WqP8GfKfTBVngRKHPLJ89nPWk2MQtWJhTpKQhJDxl4zNWmLnokHAame5F3c-0lHt9CZFWm4wKoCubzKvai5aQB90yVhgpZ1DZcPnilt3uTMSyWndtjJC3gzHINRwmUYgKWFu7exX6VVjGDhcypn39NP-7zM3f1fzb6EAl5Quk60XlYh_P6lf-EGLF3lCRU4rZuz3kcTyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنون، مخصوصا اونایی که لباس اسپایدرمن میکنن تن خودشون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81780" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81779">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امروز تولد جاویدنام مسعود ذات پروره؛ اگه زنده بود امروز 40 ساله میشد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81779" target="_blank">📅 17:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81778">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_Qsnr881vpGkSB-PqF1BO2mhcqWYv4o7LL0Nus1EEomCZSCnGJs0DXhvCHd80_k2N8c2js6S-J4PTjAp0z5P9Jbfko4EMEnSupV--o3IPOzMCfgzTxrcx1dyHse-vr-3v7AnV9m8Y5C2sF0cBlzYIVdwmBtmzdm12QKwM_H0u0O8LOwEoxKaaIhtVIR21e9FRvmSGDNJXSnSEmHlK7VQLXs2upI2GIYrikY0UDUlac7d7G9xLh9aR6AWeav1wbHE31zHHSuZJtyk5ZGLLzAzJmqXtm3XO3sgQWLhFWIuA4wT8PghjHesz5BoqabP-lBFfkw4NVFDQaZitP9RPb4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشیدنی مخصوص طرفدارای ریری که پسرن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81778" target="_blank">📅 17:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81777">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c3ab90449.mp4?token=Hlm_vjfkL250T2gVcV6XCfAEORg4JKqRfi1SAuQp2u--JBuXYDN4yHIW7Zwjv_rsYBBXwr8W6zSm2GeM3w2vFuGLDQTtNi4jIO2mMiDsL2eK-NO5hnkHjKaBNwyRw-3wA9rN-ceL9ud8ZqgBnkNWCX8Qcl6j_A2sUCbFYb6MqiWiVs11rNKYcU5oF8H-nGzVYQ6sthQPkWUaF_sq3qY_JYqAgt-V8-B6CCfRxkdLzEbiFJLQI8yxZYfaQh0N8WvzLj9QSple7B3Sd14QcZm6qEoNpfN2ZraOhMyLiqM-rdCoclFP0gU0wWdHotMMyi58DTJLW3B59jmMBOOx0CDpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c3ab90449.mp4?token=Hlm_vjfkL250T2gVcV6XCfAEORg4JKqRfi1SAuQp2u--JBuXYDN4yHIW7Zwjv_rsYBBXwr8W6zSm2GeM3w2vFuGLDQTtNi4jIO2mMiDsL2eK-NO5hnkHjKaBNwyRw-3wA9rN-ceL9ud8ZqgBnkNWCX8Qcl6j_A2sUCbFYb6MqiWiVs11rNKYcU5oF8H-nGzVYQ6sthQPkWUaF_sq3qY_JYqAgt-V8-B6CCfRxkdLzEbiFJLQI8yxZYfaQh0N8WvzLj9QSple7B3Sd14QcZm6qEoNpfN2ZraOhMyLiqM-rdCoclFP0gU0wWdHotMMyi58DTJLW3B59jmMBOOx0CDpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیدونم چی میگن ولی اییییییی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81777" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81776">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkanCfuiJ3UV4IJCuEg5lDALKJeaPP7Zm00t7h_WuNeCX39uH1SDz05P9ZMFwFDUkdlqIDoOiAk08K0a5pjgBGmSqqmG5_BC4UusHBs7M-ZRLw-J4z-8YVt9C7c04nB1ZIeBsCILvWeDNjBI1-4rGI9jLs053WR2SW6UzHXimEeb5b33TeF89jNsYxGX8SHLnJB6R3mvWmh6tZVeDXgVzb69AE-sbibi5pFFBW3-OkgearUqjaDmPuqX1yLfKM07nxfaRsgndYz7egNgayOxeGP_6jXQg4Um9MJl8DuMUrJPMuDqPS_dznE0Xumw8O7_hPi1u4PDiPk4j_v_7ydX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بازگشت نقدی بت فوروارد تا ۱۰ درصد
🎲
🔥
با حداقل ۳ میلیون ریال شارژ حساب کاربری و سپس ثبت حداقل ۳ میلیون ریال پیش‌بینی ناموفق در میزهای کازینوی زنده، ماشین‌های اسلات و یا انفجار در طول هفته، بت‌فوروارد در هر هفته تا سقف ۱۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را به عنوان بونوس نقدی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/WEEK
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81776" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81774">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fku-LaA-mdVz_MK_TGGEK6-yMEXMuQdmuxGGEhFrw0CeWwgpoVqS_fCo25O6Jof7VKIFKe2LjOct48vmSXgJmCO9wYds0oj92suKG5Ej9NNs8EUvDWAsh5v_kewZrtW7LsNh0IaHPVyGS5IeoAgjyX6GD-WHNWjE4qwJEGwckdoIeDx22au2UKZuWU4vPms1B9Vci38srMx6F5PcVhfHJT39TX4cCWcB9HGFZVjVJZvDbp9EGoxAYh0tEUHFJQxreV7uFN9-v-a2KXqMjNAh-F5QM3heB6CXRYrT9Gt2_zVqB_mKyOm5_cNitQJ6PzVQ3kI0G0bTv3IUE9b_4ae2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۶  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81774" target="_blank">📅 15:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81773">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">باز تتلو از تو زندان داره ترک میده، واقعا دوست دارم ری اکشن اونایی که تو صفن تا با خانواده شون صحبت کنن رو ببینم موقع آهنگ خوندن تتلو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81773" target="_blank">📅 14:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81772">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسلامشهر صدای انفجار
اصفهان هم چن دیقه پیش صدا انفجار اومدم یادم رفت بزارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81772" target="_blank">📅 14:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4_SeuOko29Z9Bu-J8vK-LJfLBzG3TZ_CqxTDK_aDhfZLQvcK1RsiqWECLzF4wPWN945YG_4fRDfAimEMzym-u1OXZCWd98fD3T_VC2bsjrohwmdfaySqZMR_gTIvkTmgMY4fD5uRGhL8mag4eGQDMaDcFcGqBY22RFipnXqReoAW89MWh4vkem1bOd6CHyIMbkE9vfk42WzIJAQBiGeWeW-kElBw0RRGkFA8vTeDFhf0E7xhlp45PWJNupyZuPESfqgcyvhh8N3vxN7XH80-NDl0C_UnY3vogjHNG8oOch0IKHkYn5BMAvGmMaS7Vsp9ODy6Z5Frui1KKNOg3Krbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا صبح قیامت بر ۲ مرداد لعنت!
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81770" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجار منفرد در شهرک صنعتی شمس‌آباد، جنوب تهران ماهیت انفجار تاکنون مشخص نیست و هنوز تأیید رسمی صورت نگرفته است  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81769" target="_blank">📅 13:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجار منفرد در شهرک صنعتی شمس‌آباد، جنوب تهران
ماهیت انفجار تاکنون مشخص نیست و هنوز تأیید رسمی صورت نگرفته است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81768" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKhode Khalse</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f145e00b.mp4?token=QI1jt7ATRcF576tHiVy68qQzVdymRfoX1w4AtSkI1T6WdxQtNRLiJv1lSzkzRPaJjx-fZfZL8Wj7871lfbkBqi_hlL_AR_tAm_wznzOMPnyZaJTzgCllS_7f2L0cDJlKgb4bbiqRp_CwifNTsgPbOKLcVidPV6HW1wjxu6Ertht7Fha3eivwC4rkVVg2ef68M7VQnqnlEKzk-S4SFWaNphcXnxbSlRgiVd4YkIwqLBTWz9RSP_WCzsCP5ufYy9INc7Ivf1ncVnHwjsHmHNRFrpKEQ765UuBy5W6toj0dHLh1-o2WaFLd5Av5YUGodau49QsNEFfvrCfG48Le7khhjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f145e00b.mp4?token=QI1jt7ATRcF576tHiVy68qQzVdymRfoX1w4AtSkI1T6WdxQtNRLiJv1lSzkzRPaJjx-fZfZL8Wj7871lfbkBqi_hlL_AR_tAm_wznzOMPnyZaJTzgCllS_7f2L0cDJlKgb4bbiqRp_CwifNTsgPbOKLcVidPV6HW1wjxu6Ertht7Fha3eivwC4rkVVg2ef68M7VQnqnlEKzk-S4SFWaNphcXnxbSlRgiVd4YkIwqLBTWz9RSP_WCzsCP5ufYy9INc7Ivf1ncVnHwjsHmHNRFrpKEQ765UuBy5W6toj0dHLh1-o2WaFLd5Av5YUGodau49QsNEFfvrCfG48Le7khhjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81767" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آدرویت داره میره سمت استعداد واقعیش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81766" target="_blank">📅 11:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSYE-QEdYnWL25WBAiwm8aXevi7isJrUS2zIge8mAtU0SVoC6GyNgHQH2k-IWZGVh4--5b40yklQFAO_lV_koyDA4InpoaDwIb-kSOt2HWpLPVGEMzdRfuuiJ2jnQEIZ6uzOvLe_-21ZY8twW3wbjlhzkvVWBXYA6VlKuy8ciBWptjolPuK5taDmv9nu8vdBLRbxCMNtXEDqIH-QUdQjaFnu7vyqS9Vj84pyN_zwHMgvl5EJKLcoFsMXYQ4Gs17VtOmnC1R0H-848LE83tuTymU7FuzqDXmLkJjxiv7xVYzRyUS02Zom4k1fqYl2TviPqunIs6mJLgcHZfGuEumfBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بازگشت نقدی بت فوروارد تا ۱۰ درصد
🎲
🔥
با حداقل ۳ میلیون ریال شارژ حساب کاربری و سپس ثبت حداقل ۳ میلیون ریال پیش‌بینی ناموفق در میزهای کازینوی زنده، ماشین‌های اسلات و یا انفجار در طول هفته، بت‌فوروارد در هر هفته تا سقف ۱۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را به عنوان بونوس نقدی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/WEEK
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81765" target="_blank">📅 11:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ac04ad8ee.mp4?token=Hjr9zDoiBZCTK3scGgATN1GVcPpT_bdpRSHScN8b2ULWr7eNZBSBD7QMNuLXoqdrhK2zJft9AVvK-IRPBk1CIEjDgKCzAnIT3B_Ip71cH0DdyHxXqTMiZngUrgm4cmjQ7cswol2TFD1eDAWim6_HGj9JLvvolchj-PBl1UEpIHNjcWAUMPj2iWsyMKql6YEF1Oow59T-xT4oYJSYVLjVbjCR16g0QBbVQP68q7pro_tuEk4QUseANWoQCod9GSfnGQfnfalPvHiDjMKYdtSvQgBR_A_D3_75vTdfZQTJUj9hECimQMScQsuKtmkJwvuDj761EV1YCjjMOrnIr9Me3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ac04ad8ee.mp4?token=Hjr9zDoiBZCTK3scGgATN1GVcPpT_bdpRSHScN8b2ULWr7eNZBSBD7QMNuLXoqdrhK2zJft9AVvK-IRPBk1CIEjDgKCzAnIT3B_Ip71cH0DdyHxXqTMiZngUrgm4cmjQ7cswol2TFD1eDAWim6_HGj9JLvvolchj-PBl1UEpIHNjcWAUMPj2iWsyMKql6YEF1Oow59T-xT4oYJSYVLjVbjCR16g0QBbVQP68q7pro_tuEk4QUseANWoQCod9GSfnGQfnfalPvHiDjMKYdtSvQgBR_A_D3_75vTdfZQTJUj9hECimQMScQsuKtmkJwvuDj761EV1YCjjMOrnIr9Me3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران اینترنشنال: پزشکیان به احتمال خیلی زیاد می‌خواد دوباره استعفا بده و احتمال اینکه اینبار دیگهi حضرت آقاA استعفاشو قبول کنه خیلی زیاده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81764" target="_blank">📅 10:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWp_RpaRaVztDS9KpYZ9c1DQ0oWDH9QD8FaUZaRsfmdwGhEqWgYc5Mo7x_HMLSbO6eseJt-BKCyJvafKHlWCe45a5E9Wekf-BhW3D0veNzn4oCcEvEp36P0yCN-m-auQWIbcNKFIpFiQiejPYblHnmDJtw-ABAwYoTRHjUpKjeO6PktyfX5-yq4V5NHA_vVvWSFPp9-Q7QnHW8A8lhwwaFMtXJaWRXBxw58Or7-scQub-9MPVpyU4RRzOgReU0HbO_YFFYa2NOgGjbXBFzvG8quuVaMqXYQGJV6qcdUbY3XUaJcNRztBO5_COEhV3OaoCAnbeEYyitmo6H0a7C2roQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اصلی اسرائیل است: «ما را دیوانه کردی»
‏ترامپ: «من حمله خواهم کرد. من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81763" target="_blank">📅 10:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHk4z2nYWmxuYTG6FUuT82N7_FI9APdyUH0ZPxvsr1cxoHUA_P1uFO1d7h3uD885w6V6PQ808X51KHLfWBV6rm07NUibz9UgJlJXNth9IMZTn2zwh7MCj4smap0KHAgyMjLrIkHNxpnxrl2w7zal-Aqaa785rWrIc0UGFp3sq2AW2gs8dXksn6hslWPxtFz-hi6U9qIi6hAcYVOb6d2ZgaMXCndklWNc4-MJEMHzAWhn3Hjunyoz7JMtaD30mGqtNj8b85XmH5Udrx4qHzk3qlFtR61-2PQREvq7TrQx8iMbWUCE5duW_ffcrFataiql2E0XllB--lHklegPU_TqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی اینجارو نگاه کن، ایران تو تاریخش هیچوقت گنگستر و مافیا نداشته که تو دومیش بشی، به خودت بیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81762" target="_blank">📅 09:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81761">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b42dc58af.mp4?token=SJva5R49eXldJsu5eT_Z6Wkl4OFJZ1wI7_Ol9VDhcotW9TUAGl_uz_5rGH-AOfSlpLrLZXgLZ5U0H9U0zFaCJbDyLO-JDZxMLXriqkOgSbk3CqdrjUXpu1Idvi2Pqk_oLItjoFpHDCvWh1C1LCM7V_OnbLuNdidgTWrMkDLJfJNd5N-wVky0uCSnbBNYAhGy09knpWlnzbvAq7VBQ08gOuaixzMOPUQwLnpMvz6twXkEs0gnCcUWFIq2MbRLwqwa8p5D0Xs8pHDR0Iukg_PFpRCSH3VTV375NmbnbY-2_C-VaQuMbhIBeDIZrM7Rovd1zR4_BVNDWxY1a5_hAfs3YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b42dc58af.mp4?token=SJva5R49eXldJsu5eT_Z6Wkl4OFJZ1wI7_Ol9VDhcotW9TUAGl_uz_5rGH-AOfSlpLrLZXgLZ5U0H9U0zFaCJbDyLO-JDZxMLXriqkOgSbk3CqdrjUXpu1Idvi2Pqk_oLItjoFpHDCvWh1C1LCM7V_OnbLuNdidgTWrMkDLJfJNd5N-wVky0uCSnbBNYAhGy09knpWlnzbvAq7VBQ08gOuaixzMOPUQwLnpMvz6twXkEs0gnCcUWFIq2MbRLwqwa8p5D0Xs8pHDR0Iukg_PFpRCSH3VTV375NmbnbY-2_C-VaQuMbhIBeDIZrM7Rovd1zR4_BVNDWxY1a5_hAfs3YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81761" target="_blank">📅 09:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81760">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایران اینترنشنال:
پزشکیان به احتمال خیلی زیاد می‌خواد دوباره استعفا بده و احتمال اینکه اینبار دیگهi حضرت آقاA استعفاشو قبول کنه خیلی زیاده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81760" target="_blank">📅 07:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81759">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوستان خیلی پولداری که از سیستم‌عامل iOS استفاده می‌کنن هم مراقب باشن دستای ظریف و زیباشون اشتباهی نخوره تلگرام رو پاک کنن چون تلگرام از اپ استور حذف شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81759" target="_blank">📅 07:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81758">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوستان خیلی پولداری که از سیستم‌عامل iOS استفاده می‌کنن هم مراقب باشن دستای ظریف و زیباشون اشتباهی نخوره تلگرام رو پاک کنن چون تلگرام از اپ استور حذف شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81758" target="_blank">📅 05:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81757">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsLIifEiEzVfY9EnRBcuwm7QxyE0ur2zXltk8aOYUoI5YAf0uuRlJ6DwTxrKhxcDw-IebkwchLrZ6yZozXEDN7mRh2FWkVQLdXvZh2bGX0nhuJkg9R46FN6DR3xOj9ZkGlqDycf8biNjol7I7tXo7tymK3AK4dmSWuuAqAnMOMSoMTvs8wOQvr7Qzyxus0G4wU7HVIvyhvI28Ujzv8qPgmzJBVowz5rDA8UYP1SqpME1ecWQqjO_25C8v2MFyZePJaz6r5Ly6RYBSglv_hYQ6z3__GYhX3X2bpAn8Vke7smq0LbWHO3tWqIBcP-bC41VrHZo93SMBlNMg2XduhlHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یکی دو هفته‌ی دیگه به این شطرنج ۱۶ بعدیش و مذاکرات عمیق با توهمات و تخیلاتش ادامه بده، ارتش آمریکا تسلیم بی‌قید و شرط رو می‌پذیره و بعدش روند ۶۰ روزه مذاکرات سر فعالیت هسته‌ای آمریکا شروع میشه خدا بخواد. #بماند_به_یادگار  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81757" target="_blank">📅 05:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81756">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ مادرتو گاییدم تو که بزن نیستی فقط تایم خوابمونو بهم ریختی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81756" target="_blank">📅 03:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81755">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7AnoQRwv7sGbbjUjj75-EAIEp0KasJZKXOcYZo5GrKUZKgfbcib1tM4k-l8kR5s6Z0o5zAcb2zSMaoxlq4zlsjhNEhMYJKPfn_v7d4UKOm4772soPSWZo2d-hITrpFG_Mk-oJeL3Mga9BUkdEq1t2U6BklWdFt11UWDVDf4t7LID5c4ixOAb1Fr_Bo-Mzwl5BCNnJ9zaL9midJUOtg8eTKCI1EQdayZtzUom1ksY7XETG_d8x4Dj7xRwTF0Ln6AKkrXSRzwHHFgBNQc1DFxIEyFBhQz4OaBVUEmKPzUfR4Ip6Bhp_Ks4hPcAHavw3eJEaDx6366VVViSb8mLgFVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصخل کسی که تایم زیادی تو خونس خودش نمیخواد باهات ارتباط برقرار کنه اصلا که تو بخوای دوری کنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81755" target="_blank">📅 02:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81754">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">محکم ببند درو، دیگه ماکان بند نیست که بهمون حس ناکافی بودن بده و بگه کار اشتباهیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81754" target="_blank">📅 02:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81753">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZfkf7n30WZk7a6GDvRPHSgdxpWgrkdiQ5GeZmHEeSW07dNdAeaN7aA4oclcIN8FfKGH8epu3tIiRBHJkqov_AcSIlaZzTEjkqoJdgSNeA8aSXWeDwxw8ehmCY055f_Rvd5DmS8NibyNyLbhMYv6wWH9IyZ2xXPwEnZ58DYW5SCtSDfvAr6G_Wmp3qR5pmYZktoeNDWEBS8nsiqBM7K7U-X-EB8rcTuKT6yuBr73rRGjYLb_D0NWKbXnpDJUOVF_QYnO09irWhA_b9Ka7W1vrreS9t2kOmUHaZfqekIzzDkesRWtl_IQaehJFGQbHLThToJ-cBT14xIXxbQrjz0qYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرا رسیدن اربعین حسینی رو به همه شیعیان دنیا تسلیت عرض میکنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81753" target="_blank">📅 01:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81752">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ستار هاشمی کیرم تو ناموست این چه نتیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81752" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81751">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b8952566.mp4?token=tFEBb85PysmvLHhC6GhmPkhe06zzg7dVHitYC67jQAicaqBj0BEWsN0_10vtg3lG0jBus7kO1Z1cAN5oVOoJMFW1QCGY4IOVcxBL41_dup3cfcY53r1IOAxI5o15IcdXFUVoumqzlYtPMUMSaJwIv1qLVOT6BofZ9_v9Evl9UHvDFvOK9tuIbx7i_Y1692Wb42KJqrJPam9bH9CsdZ2Cag-R4JzY3lboLD92b13s0RN3BGCiqB60y9YVHttOvOx01ToBL-phqK7xpy7eqx75Ef8YVxdew850rQGpb52mxF6RYTBJ612GhagdvYsYKVV_556E8fxeBithHN50HV6w7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b8952566.mp4?token=tFEBb85PysmvLHhC6GhmPkhe06zzg7dVHitYC67jQAicaqBj0BEWsN0_10vtg3lG0jBus7kO1Z1cAN5oVOoJMFW1QCGY4IOVcxBL41_dup3cfcY53r1IOAxI5o15IcdXFUVoumqzlYtPMUMSaJwIv1qLVOT6BofZ9_v9Evl9UHvDFvOK9tuIbx7i_Y1692Wb42KJqrJPam9bH9CsdZ2Cag-R4JzY3lboLD92b13s0RN3BGCiqB60y9YVHttOvOx01ToBL-phqK7xpy7eqx75Ef8YVxdew850rQGpb52mxF6RYTBJ612GhagdvYsYKVV_556E8fxeBithHN50HV6w7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آره خلاصه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81751" target="_blank">📅 00:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81750">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96365f95a.mp4?token=vnvzlMkz0KnOGcdFHh_6m2ZULk9RLutnWMZ8UxjTrXoMFBHnu8bTvv0PyuCS1w2BTkAznXBPXuVosJb-vUo9BfdgGB1FG4cJsnPgnlBIWyiB8ZdqZ29qSP7aFdNClmC6s3oOe-MFyIOJ7gWUF0U_qsAVU-AfTDyCL8OqRCti_ZNqMl3gNmg9kpjvJcd5QOcD_BaNM-fqmNCJvv_KcaJi2vVR3_bwRR2oYxmkr6Q0CunnXHC6ughJwUGAL_4gzvAlFAn-FlDm0nkr1xSfZ6krKZoseRc27YPeUPoLPvJdy2_DRbZF9_CHgow4x3kHOAwfHkNJFFDYQne2PDi8CxK7xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96365f95a.mp4?token=vnvzlMkz0KnOGcdFHh_6m2ZULk9RLutnWMZ8UxjTrXoMFBHnu8bTvv0PyuCS1w2BTkAznXBPXuVosJb-vUo9BfdgGB1FG4cJsnPgnlBIWyiB8ZdqZ29qSP7aFdNClmC6s3oOe-MFyIOJ7gWUF0U_qsAVU-AfTDyCL8OqRCti_ZNqMl3gNmg9kpjvJcd5QOcD_BaNM-fqmNCJvv_KcaJi2vVR3_bwRR2oYxmkr6Q0CunnXHC6ughJwUGAL_4gzvAlFAn-FlDm0nkr1xSfZ6krKZoseRc27YPeUPoLPvJdy2_DRbZF9_CHgow4x3kHOAwfHkNJFFDYQne2PDi8CxK7xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81750" target="_blank">📅 23:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81749">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
الان میان میبرنم
ترامپ:
چمن مثل انسان‌هاست. آن هم زندگی دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81749" target="_blank">📅 22:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81748">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ امروز (
درحالی که دیروز گفته بود فردا با ایران مذاکره مستقیم داریم و تنگه باز می‌شه
): فردا تنگه کاملا باز می‌شه و بعدش هم در مورد هسته‌ای مذاکره می‌کنیم و همه‌چی به خوبی پیش می‌ره وگرنه خواهیم دید چگونه کیر خواهم شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81748" target="_blank">📅 22:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81747">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ درباره ایران: این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است.
(آخرین فرصت از فرصت یکی مونده به آخر قبل فرصت جدید دادن.)
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81747" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81746">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است.
(آخرین فرصت از فرصت یکی مونده به آخر قبل فرصت جدید دادن.)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81746" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81745">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azhkpfclAu01WkvUTxfMomXwweQrSITiwgwlhOxSqLTigY8zoLLme7IeGRXchrs_5sSRks2JTdEuPD1-SfVQPmYuedPTzwq1-vZTxx4BFgSVOKibJkalA7KgnOj63UYSkvKjJGCAXnYbKViHVWvii6Qxp5GDLLQcOLrV_VIFChZleuWsJH310G2Fr5NEEhQ3NoVR8y2QmhFhWPaGmhKrN2MPp-rSyMet4zfRs3J38FY61qYdVHQcpH5bJCKAn_Bsn0Jd0MkqDt_05GuD9fXS-3YRMrSIRvM72pwHooVO6mj-mT8kZgoE446Uu-q-TXVL7AKWr6_Jx6TiNDg3BtVZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسایی که جانفدا اسم نوشتید نگاه کنید شاید بکارتون بیاد
مستند تفنگداران دریایی که با همکاری نتفلیکس و ارتش امریکا ساخته شده درمورد تمرینات
و
مانورهای
واقعی هستش.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81745" target="_blank">📅 21:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81744">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqSftCXAF3H3EMAk1m7sAe7NMoiY6zxBpq2Wtj-pcl3zrE3Cg8Nl17jbgZGmjMLS8YJ7q8CHUxxdYLM-fSzNllYDmRJrUZLNvOw81XasxrjIS1N0ehGOVgzd4Vu2wKl6Y8Viynvey7rdQ4bHtor1K9Kz_BmroTSFbJWXDJJmgbsytE0hHBWTyRrszknuuXZTZSbC0JpKbB_nvqRMyQbixTZawuK1x_JmKhlRclSYaSpgDAV4ree1HXqoRiG5T7EbRCdYYLI8C3VrgzC4s4l7KiC58qWhLsVfOf3kyHmi6lczvpqjJueGjysiqHdksVfqNUhkEeRsbj54WM58HuPaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاحالا دقت کرده بودید اگه نقشه ایران رو برعکس کنید میشه صورت ترامپ؟
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81744" target="_blank">📅 21:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81743">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-VxCELbhF2rnOharrenV6jOrdF8YbLxkKjC8yeMZ2YkDOURteirPY8fNuEMJR6Ll79qRpouQ5XNJsXMBRV9ib9IQ8G9zozqZFMgPVXyQJghzpPqgIltm37Q5M_0IFfX5T2ElOGnwp5Fj5JBQyLforvBjZhAakdt7PpSTLD7Eu9x3FzeE8-udsd7dRMTKx8wlzWvlkBYgEdn4LNSFdhXqLXUV2Hl-_VOcuKqZVT194mX97ujK8nWMf5vr3phUZ4UnFsLAn8gEK60tcFBm1nErPEheBdH172L9xpgLZeoa67oNp3YYnwKzqsoBfSQ1o0Oy5v8gXe2hfIt1wJY6gbDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی جدی می‌خواید بگید هنوز هیچکدومتون تاکتیکای بسیار هوشمندانه‌ای مثل «انتشار عکس مونث بی‌حجاب کنار صندوق» و «مجهول ضرب در ۳» رو به این میانجیگرای خوش تکنیک یاد ندادید که به این زحمتا نیوفتن؟
این بود رسم رفاقت و برادری؟
💔
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81743" target="_blank">📅 21:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81742">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gnu3EJWBaVoo4ROkis_2_HMZSvEpMzEXYmWxz4ID7FcXXfCtyTO1NG7wfC1ziYy0M5bwxrdLLfupkyExXXdE37hWO0DehefL8pvPChVLk0G3QB97Sw53K0HipGmYc-_5mNfjKt3MP6ra9hGObvQIgS2A7VQ3e0iGa1tvUeFszh2OTGExGFHF7zIkK5T9JVNXSRIkEoJC6QbN56lvYGWpu1YIerUsdBntQwXsvwMJLM0dTWRyf2EaSSR5gvJALsTDw_OHkieBshAycM8C0EYtpqOkL2KHBqruPCRHrdzTW1xKbO5JIAT7baRQqSaaoPeCiGcVjfSv7KJAqnXnQAiF7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یکی دو هفته‌ی دیگه به این شطرنج ۱۶ بعدیش و مذاکرات عمیق با توهمات و تخیلاتش ادامه بده، ارتش آمریکا تسلیم بی‌قید و شرط رو می‌پذیره و بعدش روند ۶۰ روزه مذاکرات سر فعالیت هسته‌ای آمریکا شروع میشه خدا بخواد.
#بماند_به_یادگار
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81742" target="_blank">📅 20:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81741">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به ابر قهرمان های ترک میگن ترکمن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81741" target="_blank">📅 20:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81740">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4xqnlijAI-BUhwl02rA5DSq2zu22umfg-d0wBq_NVSzqppPRqpkfIH4DzubQF_XdYRLzuRY2v0JfI2gXh04CDvnf5-2Ju-sTcEgWKxvKxeQk44_IE7W9fL4hN97tQRhezWW6RYvm0znJkpWAZMIfWTLjDGJoNqQTPEyTcJY0IMsS2GUzxZDtKy1Pw8H8pkzZagCycvdHFlK2et9mkt9FDDbPDBAz6kd66us2eDbkBsJEoxsw8sbwUMl1vJtxV0lLIxPmgXCTXCyTOp1lbkBYG4Qt8XOYL5nRLpieCUqvF29tBs-3YZWizXOZNdr4qQnUujt1CvIEIpaA0OW9SERMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.2  پ‌ن: بهم اعتماد کنید و فصل چهار به بعد ادامه ندید و ولش کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81740" target="_blank">📅 18:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81738">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9DvRdGmy3iRdbZGi9Yny2QGJa_uT7Ya89zfldx2DR1mdHJe0Y4QYkvG3RqEmpSXsY-y0EDlGuKsOFyND-mvTy6b6twbyWzAKhrnNs2kte5FMlnwtb7-0Dfu-Dt2QXy2FuUXF-mCKhVFNuDN-6vjhNHt-v7CyVFQXpfDcblSg2VkLjhIS4Ad_oq-x9bQuyhqQn9alccGP9rB-kbbTgNMxLwng3zGrNcwK3akEngq9_KwozLmUmRnGakIin8cxS5N2WEddF0xqskH6-VNV7-ulWn4riK-4ZRux3GqktpWR_j6htRDcTTY3lZ6FxXf9qpjd7G3Y_fDAEpxj2ZQ77uKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هری؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81738" target="_blank">📅 18:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81737">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef_wXsafa6X7qxKNzd5HRyeMrbQUBrSq7SixSaC67Z26ycSV__kWKhgbhxwql6ARjPFQyaU5dAlt72PdNxytEGXy4ToIDelDvXnRPKlwEPNA_V-isLlzzTVC53lpW5UzbVxwCD0dAunb7pJUp44NrIrG2bN3g3CMLzp_ExmpkANYvCHFeyY7OKxCDP0tELRPbCa70invWJ2E75TjD7RrNms1pCI238t1qbgmLF3soogVrCZe_wP9PXQfLokb0fv-j7wHk3cY2RZHAtYv1WNFbgaVk4U5alnHPCayS2Bvd6YzQWzvL6n3p12BgXX6s47wt4H1rXuBEKXQxIqexg0fIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فنای تعصبی رونالدو و مسی و رپفارس شروع کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81737" target="_blank">📅 18:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81736">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحَسَ</strong></div>
<div class="tg-text">نشور سفید نمیشه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81736" target="_blank">📅 17:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81735">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQD5ilTONhMRqc885DbLavlrxSVUBGoOYZCxLJcPbx5qlryGi4ML2dDbwH7FDcx_bvNOnLUT7GmxeKNkeYlbZf_lUkBOLMDxzoGv5DqP5awJgs3GeLuU6qwcGTlp_Z-KQSFtbVZEx1J_E1P5H1qUOiQqhjELIv-Np2j2_8Lc1SWOlI8b9sxjLRpDE2bImMjfIbfNPB95PflVXnRxJ9i_3fqAXsO1YaQyiWC84RWdhBvRdOkx3_ER4AETW8-MXPC5d0wW-tuU_0ZPEXeGy6zFYHxyrGCzUZxAUTtc_ZxHtjeCdnqrNf98FJ_rvQ4tEGed5TpiiB-XLhSFK5PcxjBDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوس دختر وینی داره پتشو میشوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81735" target="_blank">📅 17:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81733">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">-خانوم جورجینا ایا وکیلم شمارو به عقد کریستیانو دربیارم؟
+عروس رفته جام جهانی دامادو بیاره.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81733" target="_blank">📅 17:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81732">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YezOnc0u8B9iGQD2fKZsqaYT_6rOWLNnVFSdZmnmEYhssdrSBY3UvQ8epyb9AGjvdGu4yAynA7cofytbI5rjiRNQqO2_PsivOVM2LeWaMLyN7sdcQsa-wQi5z2DtNnQHJIcv_FDJjXYQVCZn5heDNLT_6NMIgcPJq9_dtj4totiOA9DptBwIO6F6c3VTpd-CH0XPX8vwes_jJa-VLf0U_PeyHlNru1IawzvE6pvpHuqnptQkBQhww-CJsL6418qL5_4nIpblYMpWgJXgV9tlcguUvRCJu4XU1zqVextjuNymyatI2cvOHxAJTEwsR41b_NYFwHD5DucdPZvl7CFdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش هنوز انقلاب نشده ها
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81732" target="_blank">📅 16:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81731">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خفه شید تلخون ترک داده</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81731" target="_blank">📅 16:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81730">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جواد ظریف: بسته موندن تنگه هرمز، اجماع جهانی با همراهی چین علیه ما ایجاد میکنه
پ.ن: خدا از دهنت بشنوه اینا باورشون شده قراره تنگه تبدیل به یه سلاح خطرناک تر از بمب اتم بشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81730" target="_blank">📅 15:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81729">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5x8wA5n0fD4AVbyAd8sYZJDiqYJf_t0I7rRx5rEVOPAwu3--qtrGQ5gmFOTEzPcqLyQd5qgX1hlQ3YHAeybQHG9q_1LWbOJoO9OFjvCItBlRqiaH7fY_BeRGNSmXwZm65yuQa0ZhbWOnX32OjLZ3oK5VAFyxlgz5EK_65WwhnSEa_iPD4J8UVj5BjX_aQrxsjZrlih53AjTE0XY7ZHpp1WKC9P6tZXuBggmtGzPguVsiQOLmV8teTExus-s5OgyxppZEGspLzasVHUf9RDpCBvUuEFz_nh7fGOI13YKOKtHpVNofv3z6SsES5SxoqVg_-w2WtAAEgxCP34k31QY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر دردناک بود و جانگداز
امیر و رهام از هم جدا شدن و گروه ماکان بند منحل شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81729" target="_blank">📅 15:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81728">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0SW-3gn3w8zEz_mq1fgvc8ghdQHT2VWq8on_Orq5oU7120JXCk8lAMA9eEx_ivNz369RuUFim-nApctxWx5hOhnD87ZFODBjXEXwO5sW-LPa0Ws_jR-QLaAky0mMEKmNpHqwR1zVUXLX6ER6W6g5dbFPhxJNMaL-V8C_N1K1A7X-zW7LT2yvLllGVoW0QrL_2oxLv-6YrV-46EUuJaBJ6TGz8_xqC8OrGHLN3l-T6ImM_eYt6Y6ygxaOG3hKSGplspZDYoiYUeRqqPeER5QQktYxysd5qyZAkVJ_C1R2VfydX1pF5mZMe9cu5aRXF_uJjm-3P5CyM2yjhMTKWR_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترک چندوقت اخیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81728" target="_blank">📅 15:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81727">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بستنی قسطی ندیده بودیم که اونم دیدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81727" target="_blank">📅 15:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81725">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MctCkrMVH-AkNiet1v9wQBjFynQjuAm0iv6jGD8YIZML5YdFqwNFR0d_9M1lOVMpjc8QpUydxRvgk1C-tL7YvohhCDnpV94yK7q7g7NBHUSYupArq10_e8Gko4UMA9fqLkiLeeOq55fB44oBtC7S-Yk98T0311r3CD90JTDjypqCqvP68wspCrlvwai_9pXsFduLaJ4AB3D5X9BHFg5E398MRi7JorPgUdShwwS8K0ryArmJRGYHdJHYcDy2847xhBuyUlvLFm9Vm7f8ZdAWeH9F3_xTzzSaIxnYqzrVqeyE5TMCBZaJWJByint9fWcIUOFrSw7ENohJNcYFK2grdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بستنی قسطی ندیده بودیم که اونم دیدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81725" target="_blank">📅 14:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81724">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هرچی پیج تو اینستاگرام میبینم به دستور مقام قضایی بسته شده، وقتشه برا پیشگیری علی رو دوباره ادمین کنم</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81724" target="_blank">📅 14:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81723">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ft1YCyhB9iQ1nkZqQNQwePl2O3uS89DvqPOWafHfN2BmUfCEITDx8E9ZozUXHY5wIQP8Rx6YTs7OORkar4CyRl6jVTok5rQTSD6lY_mdOhEg6ebYbQTteUp6yMbdXkpLv0GZpkPMC3MDiEhbGoRr3aYKYGnK1kjtpymOazi9PMIBxswV-RT4TXDVGGu0iIlG8DATkMYfrUOv96xSFzd5T2qlQJHcfdZZMPpKk3-_KWA_9eZVVyYzGs_d5OEtRWxT6mEw7QN5-IcdhNzQghklgOiqAXfkpzI-OdEb4kw1Pn7EzR79Of8V6kM_gWTvTgoDJaLAIUwRm0HxuHR1uNM9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا، حافظ ممبر های فان هیپ هاپ باش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81723" target="_blank">📅 14:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81722">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">با این حجم از هواپیماهای باربری نظامی آمریکا که به خاورمیانه میان و می‌رن دوتا احتمال بیشتر وجود نداره:
یا دکتر عراقچی پخت و پز کرده، توافق خیلی وقته پشت پرده بسته شده و آمریکا داره تجهیزاتشو از منطقه خالی می‌کنه؛
یا اینکه دکتر عراقچی به معنای واقعی کلمه پخت و پز کرده و آمریکا داره اونقدر بمب برا مراسم بعد از مذاکرات انبار می‌کنه که قراره ازمون یه سری یاد و خاطره و چند تا کلیپ فرید کنزو تو آپارات باقی بمونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81722" target="_blank">📅 12:35 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
