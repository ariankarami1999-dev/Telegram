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
<img src="https://cdn4.telesco.pe/file/LFcuQXxrf274e7JT5cOiGo5yQyWuJw5afbfTOptWp3lSN3CrQeIKnUsonMOYbJL8CUv-8HFeFHswsF-atpVCPdGK_cFux9kDymmZnY9RPzW7xE5kUxnNtvGoucj9tQMFM9BhdpgVMg24mKAUkQ_C1Gazr7AFWkEu3Dka5OGgn_W0FoCdAzsyhiqusGo13bS18ZHDh-o3ZslMEqqOTHNS61pqWJY1vaZXD_eQbtjTH9nb_ehqrTT8TxzC-Ikl_I2jzmTeRz7iKL4TclgE-CPtcMKMi_5lkMFJHhux7l4Cpff0Ql9rTSO44G5iPRHTFBDFt3Go5AlKDj8b4aBS3nsxVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 283K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 13:13:25</div>
<hr>

<div class="tg-post" id="msg-13007">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سلام خواهشا بگید مگه چندسالتونه ک جام جهانی 1997 هم دیدید..نمیخوره بهتون ک سن بالا باشد</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/withyashar/13007" target="_blank">📅 13:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13006">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-text">سلام خواهشا بگید مگه چندسالتونه ک جام جهانی 1997 هم دیدید..نمیخوره بهتون ک سن بالا باشد</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/withyashar/13006" target="_blank">📅 13:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13005">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الجزیره: [جنگ آمریکا و اسراییل علیه ایران]، فضایی را ایجاد کرده است که در آن هر دو طرف احساس پیروزی می‌کنند و بنابراین تمایل دارند در مذاکرات احتمالی برای امتیازات بیشتر تلاش کنند و این امر تلاش‌ها برای کاهش تنش را پیچیده می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/withyashar/13005" target="_blank">📅 12:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13004">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حالا چرا اینا الان نشون دادم ولی کم میذارم؟ یکی این که نگن پس فردا یاشار اومد اینجا، نمیدونم فلان جا بهش پول داد… بدون اینا رو داشت و ول کرد تازه و درس دوم این که بدونن که میتونست بره برای خودش عشقشو کنه کنه، ولی نکرد و قید همه چیز رو زد حتی‌سلامتیشو …. اونایه دیگه خون مردم رو تو شیشه میکنند و هزار جور کار می کنند که تهش شاید بشن این ! شاید !</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/13004" target="_blank">📅 12:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13003">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حس میکنم تریدری
🌚</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/withyashar/13003" target="_blank">📅 12:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13002">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-text">حس میکنم تریدری
🌚</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/withyashar/13002" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13001">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فعلا میرم بیرون  یه کاری دارم  به اخبار‌ ادامه میدیم منم یه هوایی بخورم انقدر عصبی نشم…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/13001" target="_blank">📅 12:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13000">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLtpU7EGbgdv4RKZ-Dpui0-0NgRWYn2-57AOm-Z8MJIADBgMPR04pPcrTIyVhOF1-QqFj0Op3kIa4QGPEZ130dxC8uQ7QQMNbUqif_IbysRTNcgHG9icAr6KsD_EazBbRKQ1imgUelJHAgNlSOtXp7IeBLYRP1UR4TdkOKNTe0JuJi6zItHYFrq4xhyQ78zzNsHbzeiemGC9OY-cqYaNx0d7LJOfns6FOOG5YXQ-mjsyPWWWrQ3DOfUkia5qVto2EgkHplLnRRM5D26HgRA9sARhWo1J77TBwolF-_FceUyz6yoNyDdpOEVZH-v6cCqx1i50Z5woJotJpM5Wx2eK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم SVR و G63 البته یه بنتلی GTC W12 و یه مازراتی MC و یه لیموزین بنز ۶ در و یه SL fabdesign هم دارم ، ۶ تا کلا
🥹
حالا به وقتش‌میبینید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/13000" target="_blank">📅 12:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12999">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مشروب یه کالای‌ مصرفیه ! کل اون مشروبا ۱۵۰۰$ بشه پول یه ماه یه کارگر معمولی اینجا ، البته نه کل مشروبام تو کمد هم باز‌ هست
🤣
…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/withyashar/12999" target="_blank">📅 12:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12998">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFarham</strong></div>
<div class="tg-text">یاشار میشه شغل اصلیت بگی خواهش میکنم‌جواب پیام بده خیلی مشتاقم بدونم اون همه مشروب چطوری کار کردی خریدی
💔</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/withyashar/12998" target="_blank">📅 12:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12997">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b74ad7b47.mp4?token=sQTaoBc83pBFM3bYjrbGJQs-jMFPgVPK8SOd-s1SCa4d8uC7aOHxPttz2s-3jJvR2JoARwsrW-UaXe6WEkTNzgafejmH4lJEhUzfnWTwjILBb4BOaYPkm_Uv7_10UXDVuCmFHJY5btSf4pmbPKP0cApBQBK4ScAhtAnoj73iAPg2CU4gzKxizVc2s7Uogo3iPV9ZTHuESxDIklui6Q8r_YZXyo46Bhy5cUUfDHCufOpu7jPl9B_0uebOLxdqCO7_mEygYoTAnskC16oCSAMfvIb-ex_1wduIjrHToz_biq7-d_gUv3akeAUFFAdIKpjFux9qHeT3zSTc4XvoSuP0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b74ad7b47.mp4?token=sQTaoBc83pBFM3bYjrbGJQs-jMFPgVPK8SOd-s1SCa4d8uC7aOHxPttz2s-3jJvR2JoARwsrW-UaXe6WEkTNzgafejmH4lJEhUzfnWTwjILBb4BOaYPkm_Uv7_10UXDVuCmFHJY5btSf4pmbPKP0cApBQBK4ScAhtAnoj73iAPg2CU4gzKxizVc2s7Uogo3iPV9ZTHuESxDIklui6Q8r_YZXyo46Bhy5cUUfDHCufOpu7jPl9B_0uebOLxdqCO7_mEygYoTAnskC16oCSAMfvIb-ex_1wduIjrHToz_biq7-d_gUv3akeAUFFAdIKpjFux9qHeT3zSTc4XvoSuP0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/withyashar/12997" target="_blank">📅 12:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12996">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/12996" target="_blank">📅 12:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12995">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نیویورک تایمز:  ایران خواسته های واشنگتن برای تسلیم کردن ذخایر اورانیوم غنی‌شده‌اش را رد کرده است
.
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/12995" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12994">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/withyashar/12994" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12993">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/12993" target="_blank">📅 11:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12992">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromkamyar</strong></div>
<div class="tg-text">یاشار خیلی حرف های درست و حسابی میزنی دردش اینکه هنوز یکسری هستن که حرفاتو قبول ندارن چقدر باید هزینه بدیم تا همه بیدار شن؟</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/withyashar/12992" target="_blank">📅 11:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12991">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/12991" target="_blank">📅 11:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12990">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEmmmmmaaaadddf</strong></div>
<div class="tg-text">داداش ما باید فحشت بدم جواب بدی</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/12990" target="_blank">📅 11:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12989">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/withyashar/12989" target="_blank">📅 11:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12988">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/withyashar/12988" target="_blank">📅 11:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12987">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehran</strong></div>
<div class="tg-text">درود یاشار جان احتمال داره دوباره متحد بشیم برا خیابونا</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/withyashar/12987" target="_blank">📅 11:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12986">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/12986" target="_blank">📅 11:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12985">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARVIN🏎️</strong></div>
<div class="tg-text">درود یاشار جان خسته نباشی
♥️
این حرف که میگن مردمو مسلح کنن باعث جنگ داخلی و سوریه و عراق شدن میشه رو نظرتو میگی راجبش
🙏🏻
♥️</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/12985" target="_blank">📅 11:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12984">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">@withyashar
SCARY MOVIE</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/12984" target="_blank">📅 11:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12983">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from2585</strong></div>
<div class="tg-text">درود
موافق پوریا زراعتی نیستم
جولانی تروریست بود
مردم ما معترض عادی‌ن
دست به اسلحه نیستن
برای متن نوشتن برای شاهزاده مخالف نیستم</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/12983" target="_blank">📅 10:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12982">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/12982" target="_blank">📅 10:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12981">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/12981" target="_blank">📅 10:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12980">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-poll">
<h4>📊 نظر شما در مورد فراخان اینترنتی ۱۱:۱۱ دقیقه شب</h4>
<ul>
<li>✓ شدیدأ انتقاد لازمه اپوزیسیون و تمام مشکلات رو همون اول بگو</li>
<li>✓ ایجاد ارتباط و اشاره ریزی به مشکلات برای شروع  (راه خودت)</li>
<li>✓ اصلا هیچ نگو اینم کنسل کن ( من تندرو هستم ‌یا عرزشی )</li>
<li>✓ من اصلا سیاسی نیستم فقط تماشا میکنم ، فل فل دلمم🫑</li>
</ul>
</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/12980" target="_blank">📅 10:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12979">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/12979" target="_blank">📅 10:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12978">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/12978" target="_blank">📅 10:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12977">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89c68ff2f2.mp4?token=QqzHKIH0aqNIvHiH_WObuzwGA2mSPBCBov9RPDFCvpuyoVWARWmUYpOXrW8NOZRkX4Nw9D1slTTFXyAR8a99MtXk6fpwiqo6m_X8vV7ZPjgF7Lx2kj3jNkqP5TbfTw3ZdUGOQrnvSEgBznGyyT1YRJ7BSrtw-vvKYAe2oL-iHw6ehdqHItDCtJvfmAfWxhINJlG3Op8YhSVNG1r29kY43rrrOE_xYRuunijyZrXh41ajkkbVrNl1XqLspYEk_A5tSoRY9zMPz1B93SgT3C7AK-MGjAcAfg_cjZLioP4eG1lb78fpMbEATHPH5r4UFBSdX45eQCQXwER_w6xDPthcbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89c68ff2f2.mp4?token=QqzHKIH0aqNIvHiH_WObuzwGA2mSPBCBov9RPDFCvpuyoVWARWmUYpOXrW8NOZRkX4Nw9D1slTTFXyAR8a99MtXk6fpwiqo6m_X8vV7ZPjgF7Lx2kj3jNkqP5TbfTw3ZdUGOQrnvSEgBznGyyT1YRJ7BSrtw-vvKYAe2oL-iHw6ehdqHItDCtJvfmAfWxhINJlG3Op8YhSVNG1r29kY43rrrOE_xYRuunijyZrXh41ajkkbVrNl1XqLspYEk_A5tSoRY9zMPz1B93SgT3C7AK-MGjAcAfg_cjZLioP4eG1lb78fpMbEATHPH5r4UFBSdX45eQCQXwER_w6xDPthcbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوریا زراعتی مجری اینترنشنال: اپوزیسیون ما رویا فروشی میکنه و وعده هاش دروغ بود
ما به کسی مثل جولانی نیاز داریم نه رهبران فعلی اپوزیسیون
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/12977" target="_blank">📅 10:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12976">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ارتش اسرائیل: کنترل قلعه الشقیف در جنوب لبنان را به دست گرفتیم.
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/12976" target="_blank">📅 09:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12975">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/120549a54c.mp4?token=vhkF4l5KxlGNfZuONtw3MHcXbFWoEkfBc8VVlyAk5IC7iGGZz_DN6XB0x5X5hEKdVjhNtJSZ7blexJq1e-plSrvg0cvjs4WsbtIZC_1Q0mT_78Lkc5DNzStd0I3mZ4MOHcwrMaczmH7GdanAyLIr4XnGULbpeBT7vyntAwW7ToLvFDpzsk2WjGbuuszEU0oEA_pmSZKD3YXgouyaXUwN5AFKahoH4aK60keIpE_lm5CUD0K4EpPmN1e1KQC0Pu0VvI8T-WV-mNkyi6PTtVZemfA4KX8gkPL5g9XoNi-vaBGWiHpgg_1pttdAQ7-2kpYHySWA4B7yhs2JhbJIaxtqMSo-yb4johCmGbMR2ENDvLpF8Q9MjiK_ujdzZr4AsYtOxvpM-r8eGY1HEWYTiZCQIMATrLx2STpLg0_z2QrZ4gYQWLQUsogJ4_OM9RZ78efR0s_75ml0oN1a-AWYvwbvqtse7JRUAivKWknQgcjl9-zBpfGq1jM2QMkTUb-wPxfWlGRbSD_Sgrd6sF8QxA9UgMfOOomItk4U5DeWeWUMzxQRbqhbd55J67s6RQcHbfLv3dR4fkr1UXGokfWrA7_Fxn67YnRqlUMaWONqlOgpp7YYqMxjGF6NqYVhh2Yx69bqSlr_1AO0gdRScid3GYGWx8CYpAAaewMvshi0I0M5SLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/120549a54c.mp4?token=vhkF4l5KxlGNfZuONtw3MHcXbFWoEkfBc8VVlyAk5IC7iGGZz_DN6XB0x5X5hEKdVjhNtJSZ7blexJq1e-plSrvg0cvjs4WsbtIZC_1Q0mT_78Lkc5DNzStd0I3mZ4MOHcwrMaczmH7GdanAyLIr4XnGULbpeBT7vyntAwW7ToLvFDpzsk2WjGbuuszEU0oEA_pmSZKD3YXgouyaXUwN5AFKahoH4aK60keIpE_lm5CUD0K4EpPmN1e1KQC0Pu0VvI8T-WV-mNkyi6PTtVZemfA4KX8gkPL5g9XoNi-vaBGWiHpgg_1pttdAQ7-2kpYHySWA4B7yhs2JhbJIaxtqMSo-yb4johCmGbMR2ENDvLpF8Q9MjiK_ujdzZr4AsYtOxvpM-r8eGY1HEWYTiZCQIMATrLx2STpLg0_z2QrZ4gYQWLQUsogJ4_OM9RZ78efR0s_75ml0oN1a-AWYvwbvqtse7JRUAivKWknQgcjl9-zBpfGq1jM2QMkTUb-wPxfWlGRbSD_Sgrd6sF8QxA9UgMfOOomItk4U5DeWeWUMzxQRbqhbd55J67s6RQcHbfLv3dR4fkr1UXGokfWrA7_Fxn67YnRqlUMaWONqlOgpp7YYqMxjGF6NqYVhh2Yx69bqSlr_1AO0gdRScid3GYGWx8CYpAAaewMvshi0I0M5SLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اصلاً نباید وارد ماجرای ایران می‌شدیم، اما...ما تا حد زیادی کاری به ارتش ایران نداشتیم، چون فکر می‌کنیم ارتش‌شون تا حدی میانه‌رو هست.
اما افراد دیگه‌ای هم دارن که میانه‌رو نیستن؛ اون‌ها رو از بین بردیم.
ببینید، دو تا موضوع وجود داره: اول اینکه تنگه باید فوراً باز باشه و رفت‌وآمد در اون آزاد باشه؛ هیچ عوارض یا هزینه‌ای نباید گرفته بشه.دوم اینکه ایران نباید سلاح هسته‌ای داشته باشه
همین. قضیه به همین سادگیه. بعدش هم ما از اونجا خارج می‌شیم.
ایران الان تو موقعیت خیلی بدیه؛ ولی احتمالاً بزرگ‌ترین سرمایه‌شون همین رسانه‌های فیک‌نیوزه.
@withyashar</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/12975" target="_blank">📅 09:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12974">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ادعای اکسیوس: دو مقام آمریکایی گفتند، ترامپ خواهان این توافق است و انتظار دارد آن را به زودی نهایی کند، اما مصمم است چند نکته را که برای او اهمیت دارند، به‌ویژه در مورد مواد هسته‌ای ایران، تقویت کند
درخواست ترامپ دور جدیدی از رفت‌وآمدها (یا مذاکرات رفت‌وبرگشتی) بین طرفین را آغاز کرده است که ممکن است چند روز به طول بینجامد.
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/12974" target="_blank">📅 09:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12973">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسرائیل هیوم: ایالات متحده به نفتکش‌ها و کشتی‌های حمل گاز مایع قطر اجازه داده است پس از پرداخت پول به ایران، تنگه هرمز را ترک کنند
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/12973" target="_blank">📅 09:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12972">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آکسیوس‌: ترامپ در جلسه اتاق وضعیت روز جمعه درخواست چندین تغییر در پیش‌ نویس توافق آمریکا و ایران کرد که باعث آغاز دور دیگری از مذاکرات شد که ممکن است چند روز طول بکشد
ترامپ خواستار زبان قوی‌ تری در مسائل کلیدی ، به‌ ویژه در مورد مدیریت و انتقال ذخیره اورانیوم غنی‌ شده ایران و همچنین برخی مفاد مربوط به بازگشایی تنگه هرمز است
موافقت‌ نامه فعلی شامل تعهد ایران به عدم دنبال کردن سلاح هسته‌ ای و دوره 60 روزه برای مذاکره درباره محدودیت‌ های هسته‌ ای و رفع تحریم‌ ها است ، اما ترامپ به دنبال شرایط مشخص‌ تری است
ایران هنوز متن نهایی را تأیید نکرده و مقامات آمریکایی انتظار دارند پاسخ تهران ممکن است چند روز طول بکشدrیک مقام ارشد دولت گفت : یک توافق حاصل خواهد شد ، اما خاطرنشان کرد که جدول زمانی نامشخص است و ممکن است از چند روز تا بیش از یک هفته متغیر باشد
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/12972" target="_blank">📅 09:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12971">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فارس : براساس برنامه‌ریزی‌های انجام‌شده، حجاج ایرانی از فرودگاه جده به شش فرودگاه شامل تهران، مشهد، زاهدان، شیراز، گرگان و اصفهان منتقل خواهند شد.
نخستین پرواز بازگشت حجاج روز ۱۱ خردادماه(دوشنبه) از جده به مقصد تهران انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/12971" target="_blank">📅 03:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12970">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عجب سکوت مرگباری …</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/12970" target="_blank">📅 01:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12968">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">@withyashar
JangHub</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/12968" target="_blank">📅 00:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12967">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86254cf93.mp4?token=e2c48k4EDbfefq45sFCS8ECSElUbL89_uS7-E3PTZi3F_xmqyUhErB7p6QlfYxAGzgT4WGPqZWDZ_HOGlhKZh_Qtf5hX3kllc04Ir6y3J5y0iFmsxq37iign5tZteAddV4kt3tvnNTQ5VTACA9KjtHY77WQVHJZ8KurUNH7bq1_-XcUh4tX0ybRBca5dpcXn3rZTPvebv-whtfPv9xaISnkjBavf9hSUgW5kFJ0ETk01BLGsqgTpn7ua4xlsaeyxe_cUzkCDm3w28-gNdNww0L_LYh0CErGbbgZ_rFLoMfNsb6q2umpdPDyyVhQbjN9PrGxeyFQunRFaDzJMw-K_gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86254cf93.mp4?token=e2c48k4EDbfefq45sFCS8ECSElUbL89_uS7-E3PTZi3F_xmqyUhErB7p6QlfYxAGzgT4WGPqZWDZ_HOGlhKZh_Qtf5hX3kllc04Ir6y3J5y0iFmsxq37iign5tZteAddV4kt3tvnNTQ5VTACA9KjtHY77WQVHJZ8KurUNH7bq1_-XcUh4tX0ybRBca5dpcXn3rZTPvebv-whtfPv9xaISnkjBavf9hSUgW5kFJ0ETk01BLGsqgTpn7ua4xlsaeyxe_cUzkCDm3w28-gNdNww0L_LYh0CErGbbgZ_rFLoMfNsb6q2umpdPDyyVhQbjN9PrGxeyFQunRFaDzJMw-K_gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای کانیه وست :
کنسرتم در استانبول رکورد ۱۱۸ هزار تماشاگر را ثبت کرده و به بزرگ‌ترین رویداد استادیومیِ بلیت‌فروشی‌شده در تاریخ تبدیل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/12967" target="_blank">📅 00:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12966">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89387a1183.mp4?token=mnS9EF6WIm5kMAq-SHOIcAnSdMY1P6OwGGD1BjZqs7NPOloY5EiLMTezdnCrk1-ZMYee8I7D_tFKaFyBfM9UREimWOgUuFPqbbhkcmwxmUCQ5aSqzol7qwniqJ3-PCmvYD1SLlFA9G0VROnDTl6gc5SKmkxf0kVkJ4RAMPuz2cTfw2WrNt3pVohABsE0FecoKX9BJkHac9FM6o9kZanwmGuA1yejsxVbAvWeKdw2ksFtiJBvzeqgPvzbqmSNqqaElwdQuO5Re3634paUWVrtxGlRklmJTxzE5Rw9tT3BUctK99H_Idq3UsZfC0ICCMY-_-7duFQOlXyB-HOBVJKHlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89387a1183.mp4?token=mnS9EF6WIm5kMAq-SHOIcAnSdMY1P6OwGGD1BjZqs7NPOloY5EiLMTezdnCrk1-ZMYee8I7D_tFKaFyBfM9UREimWOgUuFPqbbhkcmwxmUCQ5aSqzol7qwniqJ3-PCmvYD1SLlFA9G0VROnDTl6gc5SKmkxf0kVkJ4RAMPuz2cTfw2WrNt3pVohABsE0FecoKX9BJkHac9FM6o9kZanwmGuA1yejsxVbAvWeKdw2ksFtiJBvzeqgPvzbqmSNqqaElwdQuO5Re3634paUWVrtxGlRklmJTxzE5Rw9tT3BUctK99H_Idq3UsZfC0ICCMY-_-7duFQOlXyB-HOBVJKHlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی :
۴۰ هزار ایرانی برای تنگه هرمز یا برای یک توافق هسته‌ای کشته نشدن.
ما باید فشار روی رژیم رو ادامه بدیم تا نتونه منابع مالی لازم برای تأمین و پرداخت به نیروهای نیابتی و مزدورهاش رو فراهم کنه.
اما بهترین راه برای اینکه کار به حضور نیروهای خارجی در زمین نکشه اینه که به مردم ایران کمک بشه تا خودشون اون نقش رو بازی کنن
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/12966" target="_blank">📅 00:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12965">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رییس سازمان عقیدتی سیاسی انتظامی:
حکم قاتلان خامنه‌ای رو باید در ملا عام اجرا کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/12965" target="_blank">📅 00:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12964">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6mHoWnfAqBpfyZT8dJI_IyOKtNcvV6n1_VDZh4qvGER554ZtwBkqVi_TJeWOqlyYOonFNwj2tYzRsJeL9qGaHJBkfXOvILE0oIilPBrn6nmLyGPI2owMCEIKrwsWvkgoJkdL8ztZkxVm_adfw7rhJXmMkxA7RMfo5qKbpr49mJwTAqW4jrXp8Ojls8_EmtERdnTlyGlp4w07TxSSysXxjcjKgUHdJyMt4soqf9B04itNoplfc2W6pwN0fjoNnX3ZWKu5rxtNMkRr5Yt6AZNvsZRycj1ObMcyu3wOgfCScWN0C--Ufesrss5PE6vobD8nBwYhUkHF568q7bwq17Cxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث
🤣
:
«یکی باید برای پاپ توضیح بدهد که شهردار شیکاگو کاملاً بی‌فایده است و اینکه ایران نمی‌تواند سلاح هسته‌ای داشته باشد!
رئیس‌جمهور دونالد جی. ترامپ»
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/12964" target="_blank">📅 00:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12963">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31f4e3fc3.mp4?token=LikChH1HoR7qpy9--Uuhv-e80Octzhu3MA6BZCJVzRUD0UqeS6UX1vhC89BFW-Exmn4j6O7pVjqr-SZ00GWNSsWe8arTnjsT8rX7QVRQxR4yXCfN4skdb_4Y-mhe3iAqlQPp4AnIkJ9ViBC5bUKbbn5woJa7pNdEY1iQR3uxv_VY4e6oe7nwh-OoxmO4t8J1piWxjnfwVmlnKh6r0FAYW1xcW8Kl2etJe68nWOEVhqyeES7w0DTxi0FbJZeWwCBgFjf5DPtC0KX7UlRvWSAUcAotvou7yIJhU0Sw1lGXdwXJuO7yPoz4D96N_An-yVLlwGkSDUQA8jGbox3teTtB-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31f4e3fc3.mp4?token=LikChH1HoR7qpy9--Uuhv-e80Octzhu3MA6BZCJVzRUD0UqeS6UX1vhC89BFW-Exmn4j6O7pVjqr-SZ00GWNSsWe8arTnjsT8rX7QVRQxR4yXCfN4skdb_4Y-mhe3iAqlQPp4AnIkJ9ViBC5bUKbbn5woJa7pNdEY1iQR3uxv_VY4e6oe7nwh-OoxmO4t8J1piWxjnfwVmlnKh6r0FAYW1xcW8Kl2etJe68nWOEVhqyeES7w0DTxi0FbJZeWwCBgFjf5DPtC0KX7UlRvWSAUcAotvou7yIJhU0Sw1lGXdwXJuO7yPoz4D96N_An-yVLlwGkSDUQA8jGbox3teTtB-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا:
کشور من از همه طرف ضربه خورده؛ از داخل توسط همین رژیم، و از بیرون هم به خاطر پیامدهای بی‌فکری خودش. با این حال، جمهوری اسلامی هنوز سر جاشه.
بعضی‌ها توی این جمع ممکنه اینو نشونه‌ی قدرت رژیم بدونن. من اینجام بگم که اینطور نیست.
این فقط نشونه‌ی اینه که دنیا هنوز نتیجه‌ی درست از چیزی که داره می‌بینه نگرفته.
پهپاد شاهد فرقی نمی‌کنه کجا باشه؛ چه یه ساختمون مسکونی، چه یه میدان اعتراض تو تهران، چه دفترهای تجاری تو دبی.
پهپادهایی که آسمون شهرهای اوکراین رو تاریک کردن، توی همون کارخانه‌هایی ساخته شدن که زیر نظر همون رژیمی هستن که توی تهران برای شکار معترض‌ها، توی خیابون‌ها پهپادهای نظارتی فرستاد.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/12963" target="_blank">📅 23:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12962">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پست جدید بوگاتی شاه   https://www.instagram.com/reel/DY-ObumIJEK/?igsh=MjQ5cGt6dWo0dGg= کارای اداریش رو انجام بدید
💥</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/12962" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12961">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">در پی حملات سنگین حزب‌الله، به بیمارستانی در شهر نهاریا در شمال اسرائیل دستور داده شد تا بیماران را به تأسیسات زیرزمینی منتقل کند.
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/12961" target="_blank">📅 23:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12960">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شاهزاده رضا پهلوی:  با جمهوری اسلامی توافق نکنید، بلکه به آن پایان دهید.
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/12960" target="_blank">📅 23:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12959">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید! حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !…</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12959" target="_blank">📅 22:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12958">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzpX1cuGt6QF6uWQBCJkebiK5fgWpJNzqvVJGQdLXr28e5lV1oGwYP1kTybJ_Aaoht7e0wHXCxNwP7YYlrc4I18S2xCDdtRT3I6qBHdrIsUijq-iqcAygxNY8YRSdslxgDHmDqJpZHT8lSU0Sqjg1GLhe9LnNrv2sFebqaODnUvpwyCYHQ9XNbGVm3nGt20kCKOeloresopHqi3IgH867dgzjIhtCCJmqen9K9rkkb8gbGr9rY3ECKXkzDX-AeZjOvDVNKbTBKW1tSZyCH8m_No_Y-d3YKkvmcsEilWYTlCCsMoOO1qyDw1VzYwnu41UalOaC92MOuvS_c7tbTz-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ادعای آمریکا در جریان این جنگ، دست‌کم ۱۶۰ شناور دریایی ایران را غرق کرده است. هر یک از این شناورها می‌تواند منبعی بالقوه برای آلودگی باشد. وقوع یک نشت جدی در تنگه، مهار آن را بسیار دشوارتر از حالت معمول خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12958" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12957">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/12957" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12956">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKiasha</strong></div>
<div class="tg-text">یاشار امشب ردبول رومی خوری؟</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/12956" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12955">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سنتکام اعلام کرد کشتی تجاری Lian Star که از یک بندر ایران خارج شده بود پس از 20 هشدار توقف و عدم توجه آن توسط یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت و در دریای عمان توقیف شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/12955" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12954">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پست جدید بوگاتی شاه
https://www.instagram.com/reel/DY-ObumIJEK/?igsh=MjQ5cGt6dWo0dGg=
کارای اداریش رو انجام بدید
💥</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/12954" target="_blank">📅 21:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12952">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صداوسیما جزئیات غیررسمی از یادداشت تفاهم (ایران و آمریکا) را منتشر کرد
‌
یکی از مهمترین محورهای توافق (ایران و آمریکا) بازتعریف قواعد عبور و مرور در تنگه هرمز است
‌ایران مرجع انحصاری تشخیص ماهیت شناورهای عبوری است
هر شناوری که محموله آن تهدید آمیز تلقی شود یا بهره‌بردار نهایی آن در خصومت با ایران باشد به عنوان کشتی تجاری شناخته نمی‌شود و اجازه عبور از مسیرهای تعریف شده را ندارد
تعیین مسیر حرکت و تعیین هزینه خدمات ناوبری در حوزه تصمیم‌گیری ایران دیده شده
‌
هر شناور موظف است اطلاعاتش را در اختیار مرکز مرتبط با نیروی دریایی قرار دهد و فرم‌هایی شامل جزئیات محموله مالکیت و مقصد را تکمیل کند
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/12952" target="_blank">📅 21:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12951">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الجزیره: ترامپ برای جلوگیری از جنگ با ایران پیش از جام جهانی بسیار مصمم است
او همچنان برای دستیابی به یک توافق موقت با تهران تحت فشار است، اما پیشرفت فوری بعید به نظر می‌رسد
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/12951" target="_blank">📅 21:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12950">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شبکه ۱۴ اسرائیل : نتانیاهو، قراره به‌زودی یه جلسه امنیتی برگزار کنه تا درباره نحوه پاسخ به شدت گرفتن حملات حزب‌الله تصمیم بگیره
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/12950" target="_blank">📅 20:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12949">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/12949" target="_blank">📅 20:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12948">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/12948" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12947">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌊</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/12947" target="_blank">📅 20:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12946">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromhydrus</strong></div>
<div class="tg-text">درود میشه یکم ویس بدی دلمون گرفت :)
❤️</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/12946" target="_blank">📅 20:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12945">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frefrJq1u8y8a7lOgjUPhiH65RMA9KxMmHdtmelxm8jbAdy-q3jbAyL-8gzK4r0zDYtDZL4QI4Q2nEdJjUnJ2KPUXz_G_f5wsJ0o-9gS2I40IWNpfgeAc_8QDESSOinmH39AbkC05GpEo8ntSFeM5sZeGaNchtnup4j1JwlNrcYgKHm4HJh0ZMuzA5K-sqRE5k9iM1rgqABJm2UqePJV2vnuVO7ShfC_az72IWZoLMGq5P9oCPJoNJ4tXDgL2ZRnKVw7QTnjByp_Fzrx4LUF8SKFOi4HsR5XjpVb5X68RvzYTgyhhyScasLeqHg45sKiIVe6qY8YpdD_RHgNeZtsvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: پنج مرحله سندروم ترامپ هراسی
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/12945" target="_blank">📅 20:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12944">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نماینده سیستان و بلوچستان در مجلس :
برخی از مناطق زاهدان ۲۴ تا ۴۸ ساعت آب ندارند. ادامه بحران آب، استان را با چالش‌های امنیتی و اجتماعی روبه‌رو می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/12944" target="_blank">📅 20:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12943">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سخنگوی فدراسیون فوتبال:
روزبه چشمی به‌دلیل مصدومیت جام جهانی را از دست داد
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/12943" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12942">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تلگراف: دو ژنرال قدرتمند، احمد وحیدی و محمد جعفری، با هم متحد شدن تا قالیباف رو از قدرت برکنار کنن.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/12942" target="_blank">📅 19:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12941">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، گفت مردم ایران برای ساختن آینده کشور خود آماده‌اند و از جهان نمی‌خواهند آینده ایران را برای آنان رقم بزند، بلکه خواستار آن هستند که جامعه جهانی در کنار ملت ایران بایستد.
او در بخش دیگری از سخنانش، با اشاره به خروج اجباری خود از ایران در ۱۰ سالگی، گفت که با وجود گذشت ۴۷ سال، هرگز امید خود را به آزادی ایران از دست نداده و همواره صدای مردمی بوده است که امکان بیان خواسته‌هایشان را نداشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/12941" target="_blank">📅 19:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12940">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654bf3851d.mp4?token=i4thrGNSVcexxVe6A15H9mAcloK3ztnDqthKlRyE9w7OhcrQnk6uveqv_lv-vnhkCBmvWROzgPouRJcSn58AgEj_hX_Zwm_WNeCDptzTQs45kuUMW53dDfSaMzoq-t-17dwoQt6JBpNAKEXY25nKPxsOHdtn_HrnZ26uSZ-VoXtneX9PzDOt0j6uuIFDlhZcIntG1CqgtCNh62L5gSfGCPl3DVcrDdFhHSbt95_IRbhcdRW1P50HkBimnO2YeEoSf3RLDyfpmgYnCzCmAZLBFOFVofgJ8fQGOTEidW8qkLEVDBNUZWkdB8OX6gcRo7eNDNFjaKZJTmitBt6UwoeO7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654bf3851d.mp4?token=i4thrGNSVcexxVe6A15H9mAcloK3ztnDqthKlRyE9w7OhcrQnk6uveqv_lv-vnhkCBmvWROzgPouRJcSn58AgEj_hX_Zwm_WNeCDptzTQs45kuUMW53dDfSaMzoq-t-17dwoQt6JBpNAKEXY25nKPxsOHdtn_HrnZ26uSZ-VoXtneX9PzDOt0j6uuIFDlhZcIntG1CqgtCNh62L5gSfGCPl3DVcrDdFhHSbt95_IRbhcdRW1P50HkBimnO2YeEoSf3RLDyfpmgYnCzCmAZLBFOFVofgJ8fQGOTEidW8qkLEVDBNUZWkdB8OX6gcRo7eNDNFjaKZJTmitBt6UwoeO7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مک‌اننی از فاکس:
بلومبرگ گزارش داده است که حملات موشکی ایرانی چند آمریکایی را در یک پایگاه هوایی کویتی زخمی کرده‌اند. فکر می‌کنید اوضاع در چه وضعیتی است؟
مایک جانسون، سخنگو:
دیشب با رئیس‌جمهور ترامپ صحبت کردم. او کاملاً در جریان است. فکر می‌کنم رهبری جدید ایرانی‌ها می‌خواهد این درگیری را به پایان برساند.
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/12940" target="_blank">📅 18:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12939">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHgSr3rTf2e2IMHQoc2QEMVjAwMXLBZhNORqIlnx86q8f-wjRaFzodeqOvWQLOKRVtj3-DLNzQxH5iffbthpcJoveSmP3zQr7psspRchmD6NNebPus6waxJfI4vMCBclcgl0PAwNNj67FQf9MFldFTmlwwonSMIKFPUPC-gK2aqiuvB8iziH_O8w0t2Vph360gZayVO6wLeECxwH_2C28f_p_y8Z9Y_26PI3y5h0IMfxWTeGjxt3qrc6gMvy_Y87tgvT-neEt9Ii1NrZ-zJWaNBqTxTsEcAAX21d9YxeLfd87Ksk25sDHoZvjm7fI-alhtwpz-sDTz4gcUnyqCpEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می‌رسد که ناو آبی/خاکی یو‌اس‌اس باکسر (lhd-4) قرار نیست در حوزه مسئولیت سنت‌کام  مستقر شود. ناو آبی‌خاکی کلاس واسپ نیز امروز از بندر سِمبانوان در سنگاپور حرکت کرد؛ اگرچه اکنون به سمت شرق در حرکت است.
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12939" target="_blank">📅 17:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12938">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست «امنیت دریای سیاه» در اودسا در جنوب اوکراین، گفت که دنیای آزاد هنوز متوجه ماهیت جمهوری اسلامی نشده است.
شاهزاده رضا پهلوی درباره تلاش برای توافق با جمهوری اسلامی با امید به ایجاد ثبات، گفت که یک سگ وحشی در نهایت دست شما را گاز می‌گیرد.
او افزود: «پهپادهایی که اوکراین را هدف قرار می‌دهد از سوی جمهوری اسلامی تهیه شده و با همان پهپادها مردم معترض خود را در خیابان تعقیب می‌کند تا تک‌تیراندازها آن‌ها را هدف قرار دهند.»
شاهزاده رضا پهلوی گفت که تهران و مسکو معماران مشترک هرج‌ومرج در جهان هستند.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/12938" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12937">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عمان: در آب‌های سرزمینی خود جسمی شناور را مشاهده کردیم که مظنون به مین دریایی است‌
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/12937" target="_blank">📅 17:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12936">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea39bc17f.mp4?token=m9akx4PbwUh2TdWJFCcLO2vKIrIRs9esT2bsXYgS9gliGguJhnxz10WBILUgfl-IK5Hzj5jZ5dHoWA7jEB5PB6yDAc24EsPbuQ5ZxT8p04-MRAJryI_wT4ZhfY_Hlf_aaphqjBp17QGhw0-fbvsLuuMkdAfAY8ZrAE0kqhR5h3xNTodpqE2OQvSijp50ISBG24TvO2t5sVIOvmAqY3Z5fdso1mXlbV3HCWR1ZjXWoyT7_eQa8SfvTl-E-t3PCfrzzEkWkKg3VcRJxp5RDu2YW6m1NdkFo76tGc4GWOYpkD2UhrlIvM08GetByLM3ivS_rni7NHH4r1SLxMuKJwxOjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea39bc17f.mp4?token=m9akx4PbwUh2TdWJFCcLO2vKIrIRs9esT2bsXYgS9gliGguJhnxz10WBILUgfl-IK5Hzj5jZ5dHoWA7jEB5PB6yDAc24EsPbuQ5ZxT8p04-MRAJryI_wT4ZhfY_Hlf_aaphqjBp17QGhw0-fbvsLuuMkdAfAY8ZrAE0kqhR5h3xNTodpqE2OQvSijp50ISBG24TvO2t5sVIOvmAqY3Z5fdso1mXlbV3HCWR1ZjXWoyT7_eQa8SfvTl-E-t3PCfrzzEkWkKg3VcRJxp5RDu2YW6m1NdkFo76tGc4GWOYpkD2UhrlIvM08GetByLM3ivS_rni7NHH4r1SLxMuKJwxOjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست درباره ایران: ایران می‌خواهد بگوید که کنترل تنگه را در دست دارد، اما این ما هستیم.
و همه چیز پشت صحنه نشان می‌دهد که وقتی صحبت از آن می‌شود، ما کنترل را در دست داریم.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/12936" target="_blank">📅 15:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12935">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزیر جنگ آمریکا: به محاصره دریایی ادامه میدهیم.
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/12935" target="_blank">📅 15:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12934">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/12934" target="_blank">📅 13:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12933">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">#shahzade من تا آخرین نفس و قطره خونم از شما پسر شاه فقیدم حمایت میکنم تا رسیدن به آزادی</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/12933" target="_blank">📅 13:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12932">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓡𝓪𝓼𝓪</strong></div>
<div class="tg-text">#shahzade
من تا آخرین نفس و قطره خونم از شما پسر شاه فقیدم حمایت میکنم تا رسیدن به آزادی</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/12932" target="_blank">📅 13:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12931">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">#shahzade</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/12931" target="_blank">📅 13:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12930">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سفر قاهره با یاشار غمی ندارد فقط لذت ببریم از وقایع
👑</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/12930" target="_blank">📅 13:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12929">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صداوسیما : طبق نظرسنجی که از مردم انجام دادیم، اکثریت مردم از وصل شدن اینترنت ناراضی و ناراحتن. باید فورا مجددا قطع بشه
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12929" target="_blank">📅 12:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12928">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تسنیم : با وجود اینکه ترامپ در شبکه Truth Social اعلام کرد که محاصره دریایی ایران «اکنون برداشته خواهد شد»، ملوانان ایرانی گزارش می‌دهند که این محاصره همچنان به طور کامل برقرار است.
کشتی‌هایی که پس از اعلام ترامپ تلاش کردند از خط محاصره عبور کنند، توسط ناوهای نیروی دریایی آمریکا هشدار داده شدند که فوراً بازگردند وگرنه با آتش مواجه خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/12928" target="_blank">📅 12:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا،ماه گذشته احتمالا با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!  @withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/12927" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12926">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا،ماه گذشته احتمالا با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/12926" target="_blank">📅 11:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12925">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتانیاهو خطاب به لبنان : درخواست اتش بس دولت شمارو رد میکنیم
باید بگم که اسرائیل تا نابودی کامل حزب الله ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/12925" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12924">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کاخ سفید به الجزیره گفت:
ترامپ تا زمانی که خواسته‌های آمریکا برآورده نشود، توافقی نخواهد کرد و ایران هرگز به سلاح هسته‌ای دست نخواهد یافت
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/12924" target="_blank">📅 10:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12923">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc7jPaZt6BmQHc-QuN_Md9DSHYyRVYfD1p5_ZbEDTa3a40ITb8dXH5CxURC7gBN07seV_FLbzktWfjNl3fI8Tfyy0OGQsxfpbfLGnenf1e7_Qs2tHSAFt4-ok9xdGy-Dd4AryBXp6B39wQBMChC0snmQsCuBdt0qFuz6QPcDTftX-QPKsr-3Z01RsqFIj5--kkL910AC3xYmcwjSTuctTOokFUE0xxIHsltR9RSkRtIfH6xI6s4gBCovSCyXZdyfjh7BQ3xFXocU5zfiaSmwZFQGsfbs9XdBD26gjO1snv8t5pFp2y3_nG26AGcPzg7qnU2pS_3xwUTC6vt8icW4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشک ترامپ: «دست دادن مکرر»، علت کبودی دست‌های رئیس‌جمهور آمریکا است
این یک اثر شایع و خوش‌خیم است
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/12923" target="_blank">📅 10:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12922">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سنتکام:  هر شناوری که در حال انجام یا حمایت از فعالیت‌ های مین‌گذاری در تنگهٔ هرمز دیده بشه، توسط ما هدف قرار خواهد گرفت!
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/12922" target="_blank">📅 03:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12921">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80123d2be0.mp4?token=sb5GghToCshM161piAf0gEqmi8aW7oXqyjyNVuRilzK_a1eFvxcoPUGrCbegJ0GX4UGKiZYhe-CCn3OS2ZEpTG0O6wEEZLn0a7rsYzVus_U1R0wX9TaMh2ym3p5Qstk4WdwETXMc-Ojck7SdNUlfxbPcLd99YO3WT0ZkretI3rrxPbdSvJPcJovkFoVg7gcaB38vZndUcjDvgTdIApwLdxnbJarD8veMSdZJoO9kLuga7R38fOnan7Er8Z4gzrD24Z-v7-V0aquecDOSf4kX7kXn7Us4rHTgjXypLG-ErFDSPMDdhrlcctSLhe0zS5Ji1CA650EBLqpcU5JCiMrMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80123d2be0.mp4?token=sb5GghToCshM161piAf0gEqmi8aW7oXqyjyNVuRilzK_a1eFvxcoPUGrCbegJ0GX4UGKiZYhe-CCn3OS2ZEpTG0O6wEEZLn0a7rsYzVus_U1R0wX9TaMh2ym3p5Qstk4WdwETXMc-Ojck7SdNUlfxbPcLd99YO3WT0ZkretI3rrxPbdSvJPcJovkFoVg7gcaB38vZndUcjDvgTdIApwLdxnbJarD8veMSdZJoO9kLuga7R38fOnan7Er8Z4gzrD24Z-v7-V0aquecDOSf4kX7kXn7Us4rHTgjXypLG-ErFDSPMDdhrlcctSLhe0zS5Ji1CA650EBLqpcU5JCiMrMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلزار: نماز میخونم و شبا هم هر موقع بیدار شم شروع میکنم به دعا کردن
@withyashar
❄️
👃</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/12921" target="_blank">📅 02:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12920">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یک مقام کاخ سفید در گفت‌و‌گو با خبرنگار شبکۀ الجزیره مدعی شد: دونالد ترامپ هیچ توافقی را امضا نخواهد کرد مگر آنکه این توافق مطالبات آمریکا را تأمین کرده و با خطوط قرمز تعیین‌شده از سوی او همخوانی داشته باشد.
«واشنگتن هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست پیدا کند».
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/12920" target="_blank">📅 02:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12918">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">@withyashar
وضعیت</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/12918" target="_blank">📅 01:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اسرائیل هیوم: مقام‌های موساد معتقدند عملیات‌های اخیر علیه ایران فقط یک مرحله در مسیر سقوط جمهوری اسلامی بوده است. رئیس پیشین شاخه نفوذ گفت این واحد اکنون با شدت بیشتری فعالیت می‌کند و هدف آن «سریع‌تر کردن ساعت شنی پایان حکومت است».
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/12916" target="_blank">📅 01:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">https://t.me/boost/withyashar
بچه‌ها عالی بود
👏
👏
، بوست ۳۴۸ تا دیگه لازم داره. لطفاً این پیام رو برای تمام دوستانتون که تلگرام پرمیوم(تیک) دارن بفرستین و ازشون خواهش کنین که چنل رو بوست کنن
❤️‍🩹
چیزی‌ تا ایموجی نمونده
🤰
🫃🏻</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/12915" target="_blank">📅 01:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12914">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شکست مذاکرات پنتاگون
؛
اصرار تل‌آویو بر تداوم جنگ در لبنان
منبع رسمی لبنانی: طرف اسرائیلی با درخواست هیئت لبنانی برای آتش بس مخالفت کرد
یک منبع رسمی لبنانی در گفت‌وگو با المیادین اعلام کرد:  هیئت نظامی مذاکره‌کننده در پنتاگون، به درخواست خود برای برقراری آتش‌بس واقعی دست نیافت. این هیئت بر مطالبه آتش‌بس پافشاری کرد، اما با مخالفت مکرر اسرائیل مواجه شد.
به گفته این منبع، هیئت اسرائیلی از عقب‌نشینی از اراضی اشغالی لبنان خودداری کرده و بر «نابودی (توانمندی‌های نظامی) حزب الله» اصرار کرد.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/12914" target="_blank">📅 01:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12913">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bblZQn8mWZ13J84U5sJhoehFqDIrO-09MEPszDraUYanE12RsmjmlxLdS5TliL73YRjhiVaw5S6NipgAbIb90T0ZzE3s3bYrtheaZucGzJLRYoBiplicEibO7YUi5haIzQUAbTbenKxDpMYIOWRw5GgJmeKqWlydskdAfpocvbDkwVDPrvnXovsT_BBDE3-tKZX6zvbkoK744yDXCsvQOi_eY2rTPgvGLXkZeSr7wXChiEkkXiIVm7FiKg26nVXKxTVtBrXEae92TFgQ1CNu2IDGdMX93DIewJPbGN1ARRPJZv-kURspuqZbRENpqxyQU5Igi3RJFqYKskNKBnhOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از داماد ۱۷ ساله و عروس ۱۶ ساله در تجمعات شبانه
@withyashar
زبانم قاسمه کتلته…
🥴</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/12913" target="_blank">📅 00:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12912">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صداوسیما: منابع محلی از فعال شدن سامانه پدافندی در جزیره قشم حوالی ساعت ۲۱:۲۵ خبر دادند.
بررسی‌های اولیه حاکی است این اقدام به احتمال زیاد در مقابله با ریزپرنده‌ها انجام شده و با موفقیت همراه بوده است.
سامانه‌های پدافندی آرش‌ کمان‌گیر در روزهای اخیر عملکرد موفقی در مقابله با پهپادهای دشمن داشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/12912" target="_blank">📅 00:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12911">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حسین علایی:
سه روز قبل از ۹ اسفند به شمخانی گفتم امریکا جنگ رو با تـرور رهبر شروع میکنه؛ گفت نمیتونن اینکارو کنن. چون نمیتونن پیداش کنن.
سه روز بعد هم خودشو زدن هم رهبر رو. اونا اطلاعاتشون خیلی قویه.
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/12911" target="_blank">📅 00:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12910">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkZAeZYgdUsF9SStlZuTuKLKJ2z_6_VDV66ZXmvw6l9Sa1Td4GswBsz5xMuAa8CA5GXDy9V_I46sjKq-rV7sC1OjQbniXTsObwoXuWPDLLocxdDOQXfqf8AHal-NHTW7oYaepUPOMKaPfb6WyLc683JIpnfmRFDGcoNbY1xszE68XwQxQQ8p3Kgx8gYzhYS4FyB2UIUoXlL1iACMdhJSQe413U4jKs1la5_NzvHzt3s5VKGw4zDK6Gfo07GE2_lhvu9AqifWuyToSpCAzdpk3WOFK9WH03-V9GFzyi7z38-rzy6eYeQmfvndZKke8HN0t00ULWodnaG8TJum2xXbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مالک شبکه ایران اینترنشنال به ادعای فاینانشال تایمز
گزارش Financial Times درباره ایران اینترنشنال می‌گوید این شبکه به‌صورت رسمی توسط شرکت بریتانیایی
Volant Media UK
اداره می‌شود، اما ساختار مالکیت آن پیچیده و چندلایه است و از طریق شرکت‌هایی در بریتانیا و جزایر کیمن انجام می‌شود. طبق این گزارش، این شرکت در سال‌های اخیر با زیان‌های سنگین و بدهی‌های بزرگ (بیش از ۴۰۰ میلیون پوند) روبه‌رو بوده و اخیراً بخشی از بدهی‌ها از طریق تبدیل بدهی به سهام بازسازی شده است. در جریان این تغییرات، سهام قابل توجهی به یک شرکت ثبت‌شده در جزایر کیمن به نام
Info-Cast Cayman Limited
منتقل شده که مدیر آن فردی به نام
صالح حسین الدویس
معرفی شده است؛ او در گزارش FT به‌عنوان مدیری مرتبط با گروه رسانه‌ای سعودی
SRMG
شناخته می‌شود. این گزارش تأکید می‌کند که مالکیت شبکه شفاف و مستقیم نیست و در قالب ساختارهای مالی پیچیده و آفشور انجام شده است
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12910" target="_blank">📅 00:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12909">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شاهزاده رضا پهلوی :اگر اروپا می‌تواند اتحادیه خودش را داشته باشد، چرا ما نتوانیم در خاورمیانه اتحادیه‌ای داشته باشیم؟
چرا نتوانیم در پروژه‌های مشترک مربوط به امنیت ملی، اطلاعات و حتی همکاری‌های نظامی همکاری کنیم؟
چرا باید بخش زیادی از بودجه‌مان را صرف تسلیحات و مسابقه تسلیحاتی کنیم، به جای اینکه این منابع را صرف رفاه، صندوق‌های بازنشستگی، بهداشت و آموزش کنیم؟
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/12909" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12908">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نیویورک پست: وجوه مسدود شده مستقیما به ایران ارسال نخواهد شد، بلکه برای خرید مواد غذایی و تجهیزات پزشکی استفاده خواهد شد و پرداخت آنها منوط به تعهد تهران به باز کردن تنگه هرمز و پاکسازی مین‌ها خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/12908" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12907">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شاهزاده رضا پهلوی:تصور کنید که فردا مدل سیلیکون ولی در سیستان و بلوچستان اجرا شود. چرا که نه؟
هر چیزی که کشور نیاز داشته باشد از هوش مصنوعی گرفته تا فناوری و نوآوری می‌تواند در آنجا توسعه یابد.
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/12907" target="_blank">📅 23:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12906">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مقام دولتی:
نشست ترامپ در اتاق عملیات به پایان رسید وحدود دو ساعت به طول انجامید.
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/12906" target="_blank">📅 23:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12905">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیویورک پست:
زمان نهایی شدن تفاهم‌نامه بین آمریکا و ایران مشخص نیست
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/12905" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12904">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f2fb766b.mp4?token=EtPXPeNHlYhHrkK8jvwXhYRAmpL_1RvLrOog7eqgb_e7KRar2Vk7XI7Gr2rTbmAX5Ic94wlPRycZ466QAojUGUcMe1Fnkip8gB4Wn3hPkZUrIonzFvymhdlQ2mt8ZiHRiLPVvA9imFQk9n84dQSnIWOvtqz2k405FR9gYoEdwKpHZLvUUWZAbJjYWA9KoEpHx5-pnozcUzd74Wn90FJ6LbJTBSnhk2khGyjszkJOGBsieyEhKU40Y8v0E4cXbJaUsyXT8Zqv8mWIzbtyIlWjdGOtxUyqwLQIPCv2mh7ZiwalhrFnkGXsO_cc62nSinKb47r0nd7ga2niSVO0pOkb_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f2fb766b.mp4?token=EtPXPeNHlYhHrkK8jvwXhYRAmpL_1RvLrOog7eqgb_e7KRar2Vk7XI7Gr2rTbmAX5Ic94wlPRycZ466QAojUGUcMe1Fnkip8gB4Wn3hPkZUrIonzFvymhdlQ2mt8ZiHRiLPVvA9imFQk9n84dQSnIWOvtqz2k405FR9gYoEdwKpHZLvUUWZAbJjYWA9KoEpHx5-pnozcUzd74Wn90FJ6LbJTBSnhk2khGyjszkJOGBsieyEhKU40Y8v0E4cXbJaUsyXT8Zqv8mWIzbtyIlWjdGOtxUyqwLQIPCv2mh7ZiwalhrFnkGXsO_cc62nSinKb47r0nd7ga2niSVO0pOkb_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، اسکات بسنت:
ما حدود ۱ میلیارد دلار از رمزارزهای ایران را توقیف کرده‌ایم فقط مستقیم کیف‌پول‌ها را گرفته‌ایم.
برخی از آن‌ها شاید همین الان در حال تایپ کردن باشند و هنوز متوجه نشده‌اند که کیف‌پولشان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12904" target="_blank">📅 23:20 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
