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
<img src="https://cdn4.telesco.pe/file/ugdklN52CwXJRtIv2FAqLqGzUQeWupP9Gd65ewfnHndEa7MQhBaeN1FZhXrzovDt9bJqna_NgAYpcH7xBI59C6ltK8Fr1TkB1XiRIIttjZeArLT7e7uSatxAuwdZ6sJIL006ga1sfuRX6Rg2ruE1pLc_H_0npUL1GiYE6PN56MTwdwNtNc75R68U9m-7E0c7uVtFQXo2bJLMLFIluRfNMdeRd_tuBOpxfhYIaf7_47J5Sv7qBSruorXharmu2SBxVshEOB94DiYhu300PrITVTgHL0aKbQ6i9_MArQbd_3IhB7xWvLoH6BCKs9-OVrLs0YF_-N_L7foGW8SM99Yw0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 186K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 02:18:09</div>
<hr>

<div class="tg-post" id="msg-79153">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مکزیک قطعا اکوادور رو میبره
شب خوش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 612 · <a href="https://t.me/funhiphop/79153" target="_blank">📅 02:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79146">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرمانده نیروی زمینی سپاه درمورد جنگ زمینی:  یک دفاع ملی چندلایه برای ایران آماده شده است که ساختاری غیرمتمرکز و رویکردی نامتقارن دارد که جنگ را برای دشمن سخت و غیرقابل کنترل می‌کند. جغرافیای ایران زندان و مردابی برای هر مهاجم زمینی‌ای است. نمونه‌اش ماموریت…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/funhiphop/79146" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79145">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcD0-BzMWLM3DPOrk_10k_aecTLMKutDHOFNphvSQNx8qHaU0ljQsQ3zlnspoejksKM-X_epP-PprrOjdbD2p8bGkcc31Ea5R9lnfUviAMFAjqACMX2c7p3VD03fO7TK5-SQLIPdLmqTGL3TjwVb_lDOe3E8CBzc66_M8zpTMR7URaLrOk9oc-8DcXJLZRv8sngQLMWhZQgw121bhKWL8RvB1CmdzFc0VmWeZz7lW1MlK1QWDZvcL1PP7WOcs5GN5C18cLR_V8dmL6R8Q2T4O9EuIWGp0-WX_euu5IMWrPIKzhFBI8ktM27oGyHO1FHJOWSQRaPHmOagigOnhwv44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده حمله زمینی امریکا باشید
ناوهای آبی خاکی USS Boxer و USS Portland آمریکا شامل چندین هزار تفنگدار دریایی وارد منطقه خاورمیانه شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/79145" target="_blank">📅 01:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79144">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اولیسه و امباپه جوری کنار هم خوبن من بارسایی هم یه لحظه دلم خواست اولیسه بیاد رئال</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/funhiphop/79144" target="_blank">📅 01:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79143">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">امباپههه
فرانسه برگشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/79143" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79142">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اولیسه داشت گل قرن رو میزد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/79142" target="_blank">📅 01:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79141">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امباپه زد ولی افساید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/funhiphop/79141" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79139">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUApEzH0s_rWrvZs9xK2gWimZb3TvsVC1yoQmj0LqZ5u_m6s6UIPcjt05fWiToZFj5O-EquEPs8EBDx_MOE2jZOIvkHf-nEQdE-pv-rjG1ztOQotYiUhITTGtF5iGcrMFSxwb_8z8El0DTVN_9mDAsC7f8G361uRfAt39fivt6JZ0iHGhsiqRN33753JcD51zY0Oc1eL6uaRVGbbeVGEcFSQjOZNAmLZslPhcRH-mQekq-vhxcE0EAz3rRXlbF7qlEm0oYXw0rm67RjkFAioYAlmI1DNEFMOXzELzIiNfTaK07PDPWDZD4-pK2bxTtoX6AujRFUQO7gbZEVi3xLt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس تابوت علی خامنه ای منتشر شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/79139" target="_blank">📅 23:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79137">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صداسیما سخنرانی ممدباقرو قطع کرد
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79137" target="_blank">📅 22:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79136">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXRaRTweylwEjOqx9ABn_dimuyI96cwRksAKvIcPGV8ofBmdQ0gZhxiJGF01bdlzhMde66GJMsGnownWHXUZCK4ssNs0vQZarqzqFaob_clD3-xb3od3frd0UA4avk3NaiZHkrQAeFYo4y9_ydpN8HObpfKZMP9y6nDMJYXXXTNuB1wNp3-8aLTMPQIoqgsKiBviPDGUmAYVdBVU3QZtH-LiOKwJuu33PH8dOrEJYDxHTWHq-iQ2qHCsMzp7LvjonOLc1rysnepuC_GpmWidb5gIDDZHb6z2M_40y3NWtLgW1KBDvDkm49UZGRp82f55PN3oLgZkjpSrUctGCOvaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنوپ داگ
:
«یک نفر دارم که تمام‌وقت کنار من کار می‌کند و تنها وظیفه‌اش این است که به شکل حرفه‌ای برای من ماری‌جوانا و گل بپیچد. در رزومه آن شخص، در بخش مهارت‌ها واقعاً نوشته شده «پیچنده حرفه‌ای» این تخصص اوست.
من سالانه بین ۴۰ تا ۵۰ هزار دلار به او حقوق می‌دادم و تمام هزینه‌هایش را هم پرداخت می‌کردم. اما اخیراً متوجه شدم تورم در آمریکا خیلی بالا رفته و همه‌چیز گران‌تر شده است. مجبور شدم حقوقش را بیشتر کنم. تورم آمریکا عجیب بالا رفته.»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79136" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79134">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🚀
20 گیگ
--->
❗
فقط
49 تومن
🚀
30 گیگ
--->
❗
فقط
72 تومن
🚀
50 گیگ
--->
❗
فقط
99 تومن
🚀
100 گیگ
--->
❗
فقط
169 تومن
🚀
200 گیگ
--->
❗
فقط
299 تومن
🟩
تست رایگان
♻️
ضمانت بازگشت وجه
🔴
تمامی سرویس‌ها
30 روزه
و
کاربر نامحدود
هستند.
⚡️
قوی • سریع • پایدار
📶
تمامی سرویس‌ها
آیپی ثابت
هستند.
☄️
مولتی لوکیشن واقعی در
8 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🇷🇺
✅
خرید فوری از طریق بات
👇🏻
✅
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/79134" target="_blank">📅 22:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79132">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۶۰ گل ملی در ۵۳ بازی برای هالند
😐
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79132" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79130">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=qJrNe-XHj_7Ht67CE4csPKHAkkM9IAchvCe8YsoVKIL6DzTmyXUyBompSs8Y-azp16IkqVVZ1nM9rlsIIB3uEXG7A4ySZgSKjFP2HyQXt4B1JWHO2a-vMRMc37UdXjaBLd3AtDtshvDxQyuI8KncOqQoGXNiMXaiAMYEgrNO7ecmiGAjd6EGVyucHxtOjvXTRZJ82U-5YcFk3zlsGm_NSWPU4KScJIFGKh6ZLChNM5l_eiLECK4-zPNLonf_WmbFWM0fgZXY-8QMQxgHjLFgdJRgvv3ZzIefA8JZM_EZu9oGoj5Xfz5oyGEWWCH6ubLzr5JgIGfgCPrepZWhiva87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=qJrNe-XHj_7Ht67CE4csPKHAkkM9IAchvCe8YsoVKIL6DzTmyXUyBompSs8Y-azp16IkqVVZ1nM9rlsIIB3uEXG7A4ySZgSKjFP2HyQXt4B1JWHO2a-vMRMc37UdXjaBLd3AtDtshvDxQyuI8KncOqQoGXNiMXaiAMYEgrNO7ecmiGAjd6EGVyucHxtOjvXTRZJ82U-5YcFk3zlsGm_NSWPU4KScJIFGKh6ZLChNM5l_eiLECK4-zPNLonf_WmbFWM0fgZXY-8QMQxgHjLFgdJRgvv3ZzIefA8JZM_EZu9oGoj5Xfz5oyGEWWCH6ubLzr5JgIGfgCPrepZWhiva87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خالد مشعل یکی از رهبران حماس درکمال گستاخی اومده گفته رهبر معظم انقلاب اسلامی زبونم لال فوت شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79130" target="_blank">📅 22:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79127">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ساحل عاج واقعا شایستگی یدونه گل زدن رو داره</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/79127" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79126">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">میثاقی: بیرانوند از بشیکتاش ترکیه پیشنهاد داره  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79126" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79125">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">میثاقی: بیرانوند از بشیکتاش ترکیه پیشنهاد داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79125" target="_blank">📅 21:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79121">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ساحل عاج فعلا بهتر از نروژ بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79121" target="_blank">📅 21:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79120">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نروژ یکی از استان های خوب ایران
به امید برد فرزندان کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79120" target="_blank">📅 20:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79119">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=P0YBXfZ7aqlgBR880jo-lHEWRmn9TpySEcrvY9e3gdFEfBt4SHJznpbcqTr7Fszu4tEwIl39RrabzAguvVULojnqO8wAaS0FKMdY8EUjVX_GWC4Ksn1UawFwrxWy3N0rQTYfdJ1u37G4-F0_Y2me2ZgFhnp5kKI3imPeRH02I4kZFamInysGHFlcJzX0SMz7QyuWkPM3Cbtpu1iwVY2ZeD0BtKNnG24fjx9mx4LSM5y0I6umJG_Jtl9m_kNfwvZkvej8opy-VUhXCMmFCytScCqQ9ZYrY0NUF2xAvP8LrOyzEfpCxiWBLmW6QlEm7k60xODkc7wAWld34ykBzeDvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=P0YBXfZ7aqlgBR880jo-lHEWRmn9TpySEcrvY9e3gdFEfBt4SHJznpbcqTr7Fszu4tEwIl39RrabzAguvVULojnqO8wAaS0FKMdY8EUjVX_GWC4Ksn1UawFwrxWy3N0rQTYfdJ1u37G4-F0_Y2me2ZgFhnp5kKI3imPeRH02I4kZFamInysGHFlcJzX0SMz7QyuWkPM3Cbtpu1iwVY2ZeD0BtKNnG24fjx9mx4LSM5y0I6umJG_Jtl9m_kNfwvZkvej8opy-VUhXCMmFCytScCqQ9ZYrY0NUF2xAvP8LrOyzEfpCxiWBLmW6QlEm7k60xODkc7wAWld34ykBzeDvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تحلیلگر صداسیما:
جنگ تموم نشده در وقت استراحت بین دو نیمه هستیم؛ نیمه اول هم ایران یجور زد گاییدشون که کل جهان خایه کردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79119" target="_blank">📅 19:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79118">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJik Vpn | جیک وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC7LiZwtYfStnXb4kTZ8qJOjnyF8LsJjjZuDBudE0frK7LXxTGmhQ8PewHHbVxuu77lFDWsoRJMGvHBBkoUETMO4Gfp-hTZgwjpB2pe9asIK2xp4TuVrcrn3kkM8q01fGHLP48QsHq7KJFAGYk8-n8Ormq7wI5HfEc4tC6YpR9tPbIGzhEtR_hpistxf4mIovGaM0HaOYiSi_gDp0IvvDxs-HphJWekcl_gol8hsxVSDvE9cKHhRXS13Idn2wTWAl8pdnSNW1U7Kni8GSyZzJmeGp2EjzIlX0ofpoi8rr1qYMm8QD67hbpdZ3n6cuMWeMvsAjA7BQx-eu5NKZyk3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
Jik Vpn | جیک وی پی ان
🔥
فروش Vpn نامحدود یک ماه | دو کاربر | پر سرعت
فقط = 99/000 تومان
💀
سرعت بالا
اتصال پایدار
🏖️
پشتیبانی تا پایان سرویس
🏖️
کاملا نامحدود بدون حجم تعریف شده
🏖️
😎
جهت خرید از ربات
👨‍💻
@JikVpnBot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/79118" target="_blank">📅 19:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79117">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه بروزرسانی داشته باشیم از اتفاقات اخیر: محسن پاک‌نژاد، وزیر نفت رژیم جمهوری اسلامی استعفا داد. محمد اکبرزاده، معاون سیاسی دفتر نماینده رهبر جمهوری اسلامی در نیروی دریایی سپاه پاسداران در یک حادثه رانندگی در استان کرمان کشته شد. فرزاد جمشیدی، مجری صداوسیما…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79117" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79116">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه بروزرسانی داشته باشیم از اتفاقات اخیر:
محسن پاک‌نژاد، وزیر نفت رژیم جمهوری اسلامی استعفا داد.
محمد اکبرزاده، معاون سیاسی دفتر نماینده رهبر جمهوری اسلامی در نیروی دریایی سپاه پاسداران در یک حادثه رانندگی در استان کرمان کشته شد.
فرزاد جمشیدی، مجری صداوسیما که در تجمعات شبانه بار ها علیه تیم مذاکره‌ کننده ایران سخنرانی و از آنان انتقاد میکرد، به صورت ناگهانی سکته کرد و مرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79116" target="_blank">📅 19:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79114">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به نام خدا
بریم سراغ پیشبینی دقیق بازی های امشب
۱: صعود نروژ
۲: صعود فرانسه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79114" target="_blank">📅 18:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79113">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d3fbfab9.mp4?token=tLdIYpV5XaiOn_9krSfFEHYcMumW5OH_xEhLAdcyT3bERzAMU97Avf19ywz3wcArfbqgUREhehpIIIMqBHJLO-RkS-rn8AVKqZ9XaEIqdLBJZIZsFpgSAqGMn9RuIW1WDZAcphokokUt11tQshvVotaw9PPrbBH9E07gXI8RvEiRNSx4cRU7jkmRDmN5n80r2FDJTQFvsVJhzA5zyD_1eT0goBFYYg1oV43s-TzXx5FsSZ6Bk8Iu8BcbxV84JeX0jAMyGIM6hmeiNmcJ5wif8lplUQBRFbYjhMBhJUNbDKVgilNdSU0d_JtcKfrtbgmWaR-8NesjMuz0F3IvZRgAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d3fbfab9.mp4?token=tLdIYpV5XaiOn_9krSfFEHYcMumW5OH_xEhLAdcyT3bERzAMU97Avf19ywz3wcArfbqgUREhehpIIIMqBHJLO-RkS-rn8AVKqZ9XaEIqdLBJZIZsFpgSAqGMn9RuIW1WDZAcphokokUt11tQshvVotaw9PPrbBH9E07gXI8RvEiRNSx4cRU7jkmRDmN5n80r2FDJTQFvsVJhzA5zyD_1eT0goBFYYg1oV43s-TzXx5FsSZ6Bk8Iu8BcbxV84JeX0jAMyGIM6hmeiNmcJ5wif8lplUQBRFbYjhMBhJUNbDKVgilNdSU0d_JtcKfrtbgmWaR-8NesjMuz0F3IvZRgAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیزر تبلیغاتی جدید فیلم اسپایدرمن با حضور بهترین تاریخ
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79113" target="_blank">📅 18:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79112">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj45g0MRuxZylsPOe2Lk1Ey0gZ6JxgtYTuZDVlm7tBvA5TxYmRTj_tZcgirHzb-Zg41EjCqrep5j_mntyRJWImAm3sfBnMXj464VslGpUTeWm132cmz8F8M6aew1A6rNephqLP5ntU29A9TUVmoRMCXadd-ftWNQP_QlR2bQ-sfRzJalPeVGaVlwApEmpT05OpyX9BFmF-JvUq8C-UZn4fv3P-r_h2v1Ubr0YLzcjtwkkNbUgR6unhvjJAM7zgHHH_3RiLT2tjPS9S3B7_V-i6IJsoQxjlBzPGBaViiBCNSHcpsfjV3IuKaOD6iU9hc_5vsZ-iXcFjw5neLXBLu4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇸🇪
سوئد
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد چهارشنبه ساعت ۰۰:۳۰
📍
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- فرانسه با ۳ پیروزی (۹ امتیاز)، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- سوئد با ۴ امتیاز، به عنوان تیم سوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی آلمان و پاراگوئه برود.
- احتمالا در این دیدار شاهد پیروزی و صعود فرانسه خواهیم بود.
🧠
آگاه بودن یعنی انتخاب‌کردن، نه واکنش‌نشان‌دادن.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
G9
🅰
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79112" target="_blank">📅 18:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79111">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOfcxmnlbdQ4os_6cOnx5jQe3jRyhJu_rltQ6gRYLhKMAL_tZZMEQB2G10M8ij8ksKljXdaqnCMwq5gwjAfvJUGKjsbqF8CSryN-4x9r1oV8YLu_0ThzW3r7OzbpxR_rynQzFRGCLRX6YexvPzSjuvsEDuAPKL9zp_APd_tVKuUlYpZUI0jqO4OOoDymTNY_8De2UcRLuHSsRXuWVs8rY5hXpAOdZQx6jxIcEMiCu9O8UEKO_E2R0-rY-doCgKJNkZAYfqIMMQlmSGqaV3dXeZJomnsXYFukI_jip_3C8tJkOsamq_VRXGc6Ea2vAI8mA3bTIUdP8VlNeKIontoyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا و ارژانتین رو هم حذف شده بدونید.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/79111" target="_blank">📅 18:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79110">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شبکه i24:
ارتش اسرائیل در حال آماده‌سازی برای ازسرگیری فوری عملیات نظامی علیه جمهوری اسلامی است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79110" target="_blank">📅 17:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79109">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbwMhxMncpoouO_TsI3sUNNxjT2XdXocnNXhC4qn13ZgFaipK9Fu8NkwRwX9GnvjJHkxwP1UFQLC1mtUROV_jiJbbxMZ52IXvHNtMNu1TS-jMFqpXcv8wOlZV6L3IPMexqhaUjFX0K0RnRAaL0U8dNhd1Kt6j-uVMJ_xOUEmJp3ezj4CZV8JQ8HK38Khn7D4vy5oOmCQua3GVY3uovwQm5sL9S11e_ksxmboD4brPkI8B8WYpNv2XA0nJw6jeDMFK8JOljY3fiaq5d3fNRvnkK5A4uJwlSDDxZq0btIHTqGY41bq-xM-Q2zh1E8_jciwPlC2uOxHPZtdJBgQHFHG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج اسکم در علم نجوم در آستانه‌ی خط تورات که به معنای انبوه است قرار گرفته، اسکم انبوه در راه است
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79109" target="_blank">📅 17:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79108">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uc1_MIcQzMMC4WWWacn9zpCGPifrBzI_QbTQzIhk7BAm0R2QEgR3ESwnfyGUVOsvelC-OCyZn2NKZSv7GTbQBvZA4DqgdWNE3SksrJSISGO5wds_3inmc1gV4PLodjG_MeXU3W0Lz3LQhYM02wgZBp6pPgH0Qx4qLpluUJqYeDHbVcV3YgkMiN8jhWUitjdshlRQ1-Tzo91HaEZN4VyZkzfmxa9oU0TP77-kyuavvC7CS7c6pZnUZ5KW2Wszp1y-FfwYWX6dhIOwcaQ10Tn6v6xKWnkIHFKsIkVHX0I4iAX_ypdGGE1saSv7nKvyLqcWDGFoEQ_39wgJAxJEEJDnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هفته توی ارومیه یه نفر بچه‌اش که دختر بوده بدنیا میاد و چون از بچه‌ی دختر خوشش نمی اومده، یه پسرو از بیمارستان میدزده و فرار می‌کنه. پلیس و پدر و مادر پسربچه الان دنبال این فردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79108" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79107">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSN7uAp26qBoIY49wSpKB9ClpgiMg2vQUMVm1buCORIYi2KD4mtGORfk5DSg6F0OMyXgsUf6mrvHBW8VtseyoL3Uwb1BHtfreF4gXlmidnCh4Ox293M5aAqmEab8ed_-1s7wWYLXvPwMDLsECBc7a-6CCn375tT7wdZ2VEjpU00KErPJDki3X8JnQWwXLm2dtK-UK97ndE_1frXNgrEk5SkvabtCt9ZcFXt5sxvoYPCjel5VK3qDVO8t-dcmBYTtABpsDBIzAjUl_ASJStKcoU5YD00RCYFK_pNDq9ATsTAk3n9oclbzxHSt7P98342qsAiAH75mOVzm21kDGRJZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل: فن خال سرمربی هلند شد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79107" target="_blank">📅 16:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79106">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0WxP_iEsEDJ1ca67DTlj2N0j_MVYF854CRg8ETeh08TdSoN0ttHl8Sqvwzonq5OBsaO40N2pqA9RWsBKd79XELMIX4mO_gkLOZQ_w6fImSSTh67Eg3-7tTsbkdlYydfeBcExHyo39rLG82WvrVfQoXYTCJvMIXD_yUPEaGW0GQrEpzN_rjMMh17CIviPcFIPT1GSOAVJn5oqajyDVtllvLQ9spYB4RwB3PHgAigKU3ZicedCfckLatHkY52STw7PhxLVerBfUQ_ddbwtGHy-WQ9yM6nHwYPvGFgsBA-YgiLZprkPAi-yZ60Gv2tCwRKtSVQu-4fw1YJh6SRYwvIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو کی زده گاییده</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79106" target="_blank">📅 15:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79105">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائيل گفت مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی «برای مرگ نشانه‌گذاری شده است.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79105" target="_blank">📅 15:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79104">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جدی انتظار دارید آنجلوتی وینی رو بزاره نیمکت به نیمار بازی بده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79104" target="_blank">📅 15:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79103">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSdisr6m1YtfTnhFVDwGgh8uuqyWAjqv4nHU9PJssqoEET9sY-v1Ow5u04icqrLPH9RhiGq4EWcUHclS6C3GznIRewq-UDnQjC6VrHa-55_KWGtyIHq2WzZLzYOI6MziJUwz93eqcA8EpPOUsn05pljSCFSRhs8Z8dfwZOr7W91ovGGaP1VDo2l_ajNdC1wpfwmDPm12EeR2TmzvFua_D8jkJWwnA1m-9h8_m2QCVfPN4pgRnanWoQ7riCjCFi_sifGtHvX16w3PY-hQOjHgRQaHzoqFmNEUOvALeVfzRM3iS1b5gX8WJzFGvaPa0iObtIStf-Oitx9XRcKXz6waLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79103" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79102">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شوک به تیم ملی؛ سعید عزت‌اللهی به دلیل ۲ کارته بودن بازی جمعه مقابل سوئیس رو از دست داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79102" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79100">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvGjYfv5aPeP3-jMXDDQp-kuJz-WSCZKZYtQehSTK1aqKHRog-tirC-5pOSHOaFc4oPGVySiSViWfd1ey2_QLWY76yDc9BqsRBxHoWyzXOmtcsLaOzzzXT2tb_MPCaiTWnEoh6nYn_A4LAtGTfqAn_kbK6zXrShYlpp0utxcR-v0CHJ5qe4OAFaMslx6f0zZBvUxQSdpl5ecxpoiaA3U8rlxLiBv96j-QaC2pMDDfJz-jG7EvqdbTqlnprLacYKhC55r_1r5bhekWnzcHow7ESXjXyAB0KDqKFkzFIs1FQVjN7kk6MTU1J46UoMzMY0qVpbumwOpZOswyjIuXbL-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کونکشم داره آرشیو برنامه هاشو میبینه هرکیو مسخره کرده رو دعوت میکنه
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79100" target="_blank">📅 12:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79099">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از الان خودتونو برا ورژن ۲۰۳۰ مراکش آماده کنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79099" target="_blank">📅 12:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79098">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWxyBcPBU2X3UpPbZ2XCp42ztT02_FxqpgizL6HTI1G-DX7nzs-pcPmtAY8M4lGIF5lkHBb4HOD0aSl1YYRjGoYGYX3qv8gJgtVJOd6ctkx9dnf1jddjhjbxEmfK6DzW2l8RBbOvVNivc5pF_BJq7auolV00mFzZIBqDrgKIGipp8_iwIYWIY_-vaINiq4DHYufHZVz7xFyezdkyBsUzSbDIz0O6fUtrtWMMygIKUVXPoTYeQAQO7FpGgd4Dy2X2jljCXPotWg0zSE6YoyT4yHPp-niLPi4NMMWj1r7c4XFNtByuqeuMJdpAEPEaWsubi7E_5IR3lKiF5gcdV-RaYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امان از کرم داشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79098" target="_blank">📅 11:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79097">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7jCbGbBKtwmS1_gXejmmos3pDAfUURF9BNynYNqfw_gFqDQgIuEYlQj1fo0sxxVsaHNYINCjYMIABNLpjnAPFVQcVFxo_ss6SrfB9_zKeBoc20r9NqI5awQmxPIUOl4r8XGP8Imkt5oYDCp6auosMBEYW1BoACEpUBtPx5nyG-jEZ82bGP1k6LVcEq-NKnAORPRGCMUs23Emhl9zwGGWyxhWGvngJ6lIIFn_bWI8aq4cVZYdT756Fp8wtZiQmZcx194B_xvBOEElVe_ozymReibgqI5YJYD0Zex_FiJFJz5cSH6tRN22ZGMLSKZX__TPAyMspPb89A7zJ1A7sPYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇸🇪
سوئد
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد چهارشنبه ساعت ۰۰:۳۰
📍
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- فرانسه با ۳ پیروزی (۹ امتیاز)، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- سوئد با ۴ امتیاز، به عنوان تیم سوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی آلمان و پاراگوئه برود.
- احتمالا در این دیدار شاهد پیروزی و صعود فرانسه خواهیم بود.
🧠
آگاه بودن یعنی انتخاب‌کردن، نه واکنش‌نشان‌دادن.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
R9
🅰
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79097" target="_blank">📅 11:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79095">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کی قراره دست از این که مراکشو یه تیم ضعیف میبینید بردارید و بفهمید اتفاقی نرسیدن نیمه نهایی جام‌جهانی قطر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79095" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79094">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdjpftMXfq8pCdn64jI1TnqYgLleEUsVKaB_nEeweKjwvc74WwHYQglaHFuwgMQdf2BTov33EuID4QHm65r4wOfA4k7RPL7DWR5IvFPZu5YDjv8kAUTWWMwYTbCsLC4gyW-X9_2Zot-bpybSCgiWTyPXgDD1964mfUoZDZi3_Knp4s-GYfejqQ_v5088BkP6nwpVL59hgrr3cC8VmfSD3f9GvtJ47mQIUPmP4FnlyU7zjzMr8ki4FW0SO27t0sIujPQBtr5cTGTM_IapCK3vgKa0-AxDqtlShC_Gkc6yThmLm8qqkjbwtu1QYEoPv8D2DsPYOarazmGbwQ0dE1dRTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان تازه بیدار شدم مشکلی پیش امده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79094" target="_blank">📅 10:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79093">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چه جام جهانی عجیبیه تیمای بزرگی مثل آلمان و هلند و ایران حذف شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79093" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79092">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAgbnlnwdzybACquPjHO8oiiPAFUn5be3ZwQ0YFFiRJY_K_ggMGQw6mHzjKCKba41GLL9V0wp7BL9xTWJz9vCiMJNThZGdiJLzGddivK7xqjTsbJcTT3b_-oxqOd0_1lxMf39hfW8wICvWsA-bGa73acI4znRvAkvaJPDX6A6HoP7BcuQpCdeLjzFX-ksjw9KeN8alQC3bTr2xbthcMlYFTS8nAT4gXKFmZtgR0ZIYWcEYYGYzPHAe4m_csIgYih6no2a9HrRFgRDD125Rb-xZjRgbk_aUcSK_lqx0EkP8OMGFToeJZvMCFk_ipowebNF64U1bzJnJrx6kfEpMN0UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79092" target="_blank">📅 07:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79091">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هلند هم حذف شد
😂
😂
😂
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79091" target="_blank">📅 07:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79082">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فرید خوش چشم نظری راجب بازی هلند مراکش نداره؟</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79082" target="_blank">📅 03:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79081">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ناگلزمن در مصاحبه بعد بازی:
واقعا نتیجه عادلانه نبود ولی خب اینم شاید یه آزمایشیه خدا داره منو میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/79081" target="_blank">📅 03:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79080">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دیگه هیچ نماینده تابعیتی و ژنتیکی‌ای تو جام جهانی نداریم
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79080" target="_blank">📅 03:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">میدونم چی میخواید بگید
ولی جدی جدی بنظرم هلند دیگه مراکش رو میزنه
شب خوش
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79078" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">و تمام
آلمان حذف شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/79077" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79072">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عشق ابدی فصل سوم اکسای تتلو رو جمع کردن اوردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/79072" target="_blank">📅 01:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79070">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">میثاقی رو در یک کلمه توصیف کنید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79070" target="_blank">📅 00:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79066">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کصخلا غنا جادوگر قابل داشت مردمش از گشنگی نمیمردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/79066" target="_blank">📅 00:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79065">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCFoZBkPAsbIJVIeRYviDriO4pcrxkxdFrzc23DIvQNmB587x5w3jw1jzZAShCV00LF-_Reh-cn-h9HlvuNV8lUs9-szTigxQCfPFgx_ZYVyOZsQYeTPuM1j0w3SkYnN2DmDAgbIZmcv8dbpD8-SHXVFiMbHphSETU20gkr5bmwffwTzS3hMzmfbxyz5BSgVPoAk2yCCxmddYqUiROh-fZFeVczD6RKvJJcvXxxfBZRsvB7l3-WCZUN32nGndf5u4xE1yFuf3qJggXTNfxWgpWeDZB5IMGuXNMTXSLjZVXo5erSXfFVSqIVOx9Evc6xhwv8fIW_S2c3JH6wb-S5jlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😏
😏
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/79065" target="_blank">📅 00:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79064">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سلطون هم رو اورده به دعا نویس
جادوگر غنایی:
کیپ‌ورد تو مرحله حذفی، آرژانتین رو حذف می‌کنه؛ از الان خودتونو برای این شگفتی آماده کنید!
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79064" target="_blank">📅 00:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79060">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هرچی دارید رو بذارید رو صعود آلمان به مرحله بعد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79060" target="_blank">📅 00:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79059">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزیر دفاع اسرائیل: آغاز جنگ مجدد با ایران ممکن است در عرض 2 روز آینده و با شلیک موشک از ایران به سمت ما رخ دهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79059" target="_blank">📅 23:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حله داداش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/79057" target="_blank">📅 23:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امشب ژاپن کل دنیا را سوپرایز خواهد کرد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79055" target="_blank">📅 22:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">برزیل برد و رفت مرحله بعدی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79054" target="_blank">📅 22:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79043">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جدی باخت ژاپن به قلعه نویی عجیب ترین اتفاق ۲۰ سال اخیر فوتباله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79043" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79042">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ژاپنیا همون عزیزان افغانی هستن که مهاجرت کردن به شرق آسیا
پس رگ و ریشه ی آریایی دارن زنده باد کوروش کبیر
🔥
🔥
#sajat</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79042" target="_blank">📅 21:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79038">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">امشب زوج سوباسا و کاکرو کار برزیل رو تموم میکنن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79038" target="_blank">📅 20:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79037">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI_3UGb1wOAo4E_hStzIJZLlpGMBvbzoVbAjjaBRMU9Pk_z40A0lEwqldyWCq33r6QvpGt8EhduffzLFVOuH_o1r1WwJGPokWS57WbmdvK_pwDbdgDy_kxqKzlXiHCV3i6uifvcYDlJuGk-xgSSQjfY-8_jxL5qJMEIr5TnIwB67tW9F9Otei6KJwUHh_34zinzaipI97LZH-5p_gNnPlYofp_xwxG7haWhp2bQD_AXPjUMe9ojm2Jm7DoRKBNSRE4LasR_uF4z59MZxU2g_gzWVOWaa13pdJ_nkweHKeeLv2aH3NpEkDTTZzzaNkN6KL0jJlIdBZp1LEO3gAmOtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون موقع که ما به توماج صالحی فحش میدادیم امثال این آدم به ما میگفتن شما وصلید و فلانید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79037" target="_blank">📅 19:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79035">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtiliLxH7EkkYwOY3Xh7so3xmFibp4cFyTJ2aO5533IdI9HYc-pykhBBylbkLTILUyB_8yU5BvmXxXG4MYwns54PvH1c_12jy1RfQUjr3AcPAiRmIfK0fKKc_scKCoo8fW78ab_tiqBGnPOcMqZOvr_Fe7cJvmLi9EdHQDGGv3wIIbAvFyZL9HNf3vH8bQF9xtuBoJZvo1o4QzPL1FZ1edD20MExvSdAO1ZTS-bIYLQoQv-3J28AOqmZzc3flshft1DAuNqvRiMw5PoCcGSc2_co2bti5tRW_a0JAU7S-WisuPs8GpQvLbMG75Z0tcZhaemlNzeKnDlgqZCxeQfeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwDKSEfCiTAIoYa0HsJs0rUZbCexkPys007e_ALN2u4OhDcQybWLukjnGjMAJMyxsFyi7xYYEeA96Vrg8rbMJLZXV1Qw-Dk5yaEgdw9Va6wB0M4DBfVieTS6wmqwXUhnDe3_j3NOCL9ZGu4zLxA9G_FtTGYuI74r84ziOTsze1GofW_DXrKC1E9MKOSObpQcZFzmjWltCAieAVfbyb-PigwtyMrnxSr2WKH28RdC252sCZ_sTGJ1rmvhiTerv_xxQj0o55o09ldE47cPW_-m5YrAD7ffkVsoMDcuNK31rCqX8ZOt5uxNaDFs1EBEhM8KPzE__oIYmkkR4DiqVXhfMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیلی ایلیش رو به پسر ایرانی وقتی تو کامنتا چنلا یه پیامو کپی میکنه و ترتیب میره:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79035" target="_blank">📅 19:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79034">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niE937511x9VTHKrc73odDLN4QFjPdcUisnHKtZ2tQRIkohcebWTAjSw8X2JDY9_JiGIgaSEJsPucHfr9N8GfP25DClXolkGo2bJERNVdEsZKYDIUJ-yVwqp2elYqhCsG-5H_ZMm_YgWdVVS9L08AeW2uYKcsrzRB5-dv4jxW8ELbOg_qdpYRhxoDhsoLvLagC5k94thnveRqsHVPzpzlEpaaV-HbYFLNNF2GVq0n0eeNZUYEI5AwnW_OXDuUOPMQNKnjnLPpmcBcobc4eiciZKOYQy0QOLzrC9oSrj0DngPbJkkQS905dY6nGSUNF4ilZOQYhggL-oycXYbrpvaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم از روزی که دمبله بعد بازی مسی رو لخت کرد.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79034" target="_blank">📅 18:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79030">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چرا هوس اف دراگون زمین تا آسمون با کتابش فرق داره</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79030" target="_blank">📅 17:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79028">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سارن و کوروش کی قراره به این نتیجه برسن که ترکیبشون کیریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79028" target="_blank">📅 17:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79027">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان پدیده یعنی شما حدس نزنید کدوم تیم قراره باشه، نه این که ۱۰ سال منتظر باشید مراکش و ژاپن همرو ببرن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79027" target="_blank">📅 17:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79026">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کسی داره ۱۰ هزار دلار دستی بده؟ بخدا برنمیگردونم
@Funhiphop
| محمدرضا ناصری آزاد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79026" target="_blank">📅 16:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79024">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کسی داره ۱۰ هزار دلار دستی بده؟ بخدا یرمیگردونم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79024" target="_blank">📅 16:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79022">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حزب‌الله رو که دولت لبنان اجازه کامل به ارتش اسرائیل داد خلع سلاح کنه، عراقم که کودتا شده دارن مقاماتی که ایران تغذیه میکرد رو حذف میکنن، از جبهه مقاومت فقط یمن مونده درحال حاضر.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79022" target="_blank">📅 16:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79021">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حزب‌الله رو که دولت لبنان اجازه کامل به ارتش اسرائیل داد خلع سلاح کنه، عراقم که کودتا شده دارن مقاماتی که ایران تغذیه میکرد رو حذف میکنن، از جبهه مقاومت فقط یمن مونده درحال حاضر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79021" target="_blank">📅 16:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79020">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فنای بارسا اینطورین که از بازیکنا هیچ تیمی اندازه اتلتیکو بدشون نمیاد ولی عاشق آرژانتین، حالا بازیکنا آرژانتین کجا بازی میکنن؟ نصف بیشترشون تو اتلتیکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79020" target="_blank">📅 15:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79019">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4pbJ9yaQ8iPQlcqGyTUqswuuWG4sxZrqgzxmuTiuwMmNlau3vvDuKWaL0cMkJ4Wl8_6UT6W5IvMWdSKy3IfJcLUfRGaWj30gNR9OZ7NNVTfydTEtYae3g4UlW27PoHGMQDUlT2nJtuZSNshdfIKdgMXy0S-V2NjpxP2UU3UfZ_6jayIwW65IebJFhSlP5itvR_C7lcf5P92qrLsq6lBPVAyvUP3P8rfcYJslAcngePkYpnN3i8oWww3WQZAY9eTRyLH6UlVeCsTjsaW08T6qyzhPWmfC44wVBNd-TAitJYU6abcG8Hckl-Olu8PeXEgVI5u5hsed_dz6vDjj2nDaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان خودت نزدیک تر بود ولی.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79019" target="_blank">📅 15:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79018">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSYaEpv8cMz11LZIZtjMbRH5lasHU_VZUSnhR5PNgbeBGnWEr2N9DX8BZuH2U6Yvi9wKtRFY1FywC5LfQpFP49TVnDGBE1zQykN-OusM8vYmvGCLEkAr5y42eVUHdAQviWRjuX7MrRI1ESa2eK9Q8BYs_RhizmfnbHCSN7l9SCXZ_cA8KRlZLNRnb_6DBj87LIRESFz6_AnAV3QqOLYjLdxnf_waYP0S8xDhdyDR6S1FrbFnxyU-CfLdqxjS1XVjNwYOl2xKUx6hh4-wMBVBTtyZIHYjyX3k5jP5hT02wR7LfF_udeG4_DiUMnGRE8huhE_u1umiprjc-SFM7Xp91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79018" target="_blank">📅 13:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79017">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">میدونستید یکی از اهداف اصلی ارتش اسرائیل برای جنگ بعدی سایپا و ایران خودروئه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79017" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79016">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آناناس مادرجنده تو دیگه چرا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79016" target="_blank">📅 12:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79015">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_si39uQeEIJd31IEDNkV-ye9vaSq0-En-etJAuo_5axzaxyOWZJHa7iHKkVsstrsvjAnh9A2oDhlCGjQ5Ny6mF0xTKVPKH4JX3G9pX9STpcijQEdPPQ1eZ20cEd05Ud-cG1TYYzKamErOe_EVtB47vc7lt74P8qLtLnbuOoUD_NTx9X5AjRIc09dLhfWmvaZ-vZY9-bIZ_fO5Bwu6_pny5tLauZDsHZ5YaRcTakEf-RxjsQO1H7D3eRrvmvZHWZDwsxIt4ktgyEMbSDwxAHX3WUDMyjKqAtEnbRGNcYvlmUs_rEXVIh11ho7AUuSrFUpOTvsg1fw-Xr4E8LPFnzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش و سارن به نام بهار ما گذشته منتشر شد.
Youtube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79015" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79013">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">امشب ژاپن کل دنیا را سوپرایز خواهد کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79013" target="_blank">📅 12:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79012">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be7060d94.mp4?token=OKf-3lM7jjW3knLTFNO4vdEQwPeuAWeTPsf5NaJqqK_dnwZiH-LFvuqvuSE-OLLwSZUnouTIGDIfBaWIqRMzPRVeFH0-rEhZY4V2M7UE2_eOqaI68omoPNomSOWO6qo9G0SKRLf20Bx2ki4M1A5tXL7s0l7sP2qRi54jsm4N04r4fMPcZVM0woP5_PzAU2_XcVuZ4_MAEqqc9Ot9QVz7Meg7J2mfzAl4uOSe3T77n4XUeK18vIV3MTw_pXKr2W95WGNdrFzfqLLr5QYlyb4edOX6RUeJDMCIQrM5su4ZP1Dd06vse0BrgeAf4LiXjoo9mxMHmPuzu4fNk5Mvv5_Tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be7060d94.mp4?token=OKf-3lM7jjW3knLTFNO4vdEQwPeuAWeTPsf5NaJqqK_dnwZiH-LFvuqvuSE-OLLwSZUnouTIGDIfBaWIqRMzPRVeFH0-rEhZY4V2M7UE2_eOqaI68omoPNomSOWO6qo9G0SKRLf20Bx2ki4M1A5tXL7s0l7sP2qRi54jsm4N04r4fMPcZVM0woP5_PzAU2_XcVuZ4_MAEqqc9Ot9QVz7Meg7J2mfzAl4uOSe3T77n4XUeK18vIV3MTw_pXKr2W95WGNdrFzfqLLr5QYlyb4edOX6RUeJDMCIQrM5su4ZP1Dd06vse0BrgeAf4LiXjoo9mxMHmPuzu4fNk5Mvv5_Tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیلیان امباپه 178 سانتی متری در کنار ویکتور ومبنیاما 224 سانتی متری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79012" target="_blank">📅 12:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79009">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yjx7teuzuDbCUmjOKqcBe831VDjzuz0a7xbVwHWou1ttbdkgMil1WPg38CSPK6mp50EPZXdlEsT51buqxt5pYs-qAL0RX6gBT-WOM9vRfIUmuDplVaikKFGsKMtdsy699rmU0lbqzN4s0rc6QpnSw1i3KkRBS_Umb7rBAhR6ZBK6YwCvuOp8Uiq9vtSQImXV4laxqjn0cSf6CsWX1maOIjsk72SG_4yzC-Mw-ch_5OeRHqa2lfqNSTc2xtfwAfyCaLdXO8SBGDJUra3lJz65GP87TWkePdP_6N3bQ6ojrf15DuL0h4DtB6ZGdw5ck3pbjV1iITfpXND9yRESYtErnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه کیرم تو دهنت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79009" target="_blank">📅 12:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79008">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ناموسا نمیدونم دخترا از چی پسرا خوششون میاد، پسر خیلی کیریه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79008" target="_blank">📅 11:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79007">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ناموسا نمیدونم دخترا از چی پسرا خوششون میاد، پسر خیلی کیریه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79007" target="_blank">📅 11:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79006">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هعی از وقتی اومدم کسی من و تحویل نگرفته:)
چه چنل مسخره و دختر پسندی:)
ما پسریم همونایی که موقع حرف زدن بهشون میگن هیس:)
همونایی که نمیتونن کراپ صورتی بپوشن:)
💔
🥀
✌🏿
حرف دلته؟:)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79006" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79005">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حال و احوالتون چطوره؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79005" target="_blank">📅 11:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79004">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حال و احوالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79004" target="_blank">📅 10:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79003">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پشمام با این گل کانادا رسما تیم قلعه نویی صعود میکنه مرحله بعد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/79003" target="_blank">📅 00:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79002">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتیجه میگیریم دریک کیر منم نیست</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/79002" target="_blank">📅 00:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79001">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانادا زددددد
دریک برد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/79001" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79000">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">لیگ ایرانه یا جام جهانی؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/79000" target="_blank">📅 00:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78999">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیمه اول بازی کانادا آفریقای جنوبی از کل بازی پرتغال کنگو خسته کننده تر بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/78999" target="_blank">📅 23:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78998">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مثلا بازی با سوئیس بره پنالتی و بیرانوند همه پنالتی هارو بگیره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/78998" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78997">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بازی امشب میره به ضربات پنالتی
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/78997" target="_blank">📅 21:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78996">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z46P4B0TpJuyv15FYGnQzegQ5ljtoxCaJYbJLppJbBxDORXs7ghsQX5zPtnrDpxVCmkRE65YK27IaucosGVw_0RgUh7fttoGXpTR2kWEfl4U03bZ1dzHlwskox2DNKtlI79mkHDK0jBGe9YgDnx3LyKFMd4T16fesD9oyPKNmJ8U0QXBUJe3IUedgeH0ZJC02shhCBCtgR1bDlGH5liDMdSmMuoheoNAJDXTymFvFIikEAG084IhJdRaO94smJCuI5gtmMUkT93etMH5CTuxCqNMLrDtK7AM0sxFsv8IYJCwt4VCk-ceRjPzFwR6hHDQufMwguvSh9T6eJLbpgfLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگیتونو بفروشید بزنید رو صعود آفریقا جنوبی، دریک رو کانادا زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/78996" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78995">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjeM_wM8XR9kBxfmSr5TiZrZHi3h8PC00qrRyMXpiJRhsjy9pE7lEBqMsCSwDdwJpPBuj7qWBa4Xp4dxJcrHpYS1INVayKHP2HczmwdyvaWQXROmTHL8ZGCZP-OtHEiQ-971gb8F4fVhvF-T8GsEq5sr0dC4pPltlhBfBKFMFCeSZa0a5eaRN5R81KBQqUkUOZtigvGXBcp2g-9WwD5gqwwnLbq9Ao-_bvSCImtd-GJTlX0XI2a69CDB_UdfhSEnkuXE_WYg5ZMlIz5iGjl0EZNWkzkWJog4KZ5nFXLUjv37gjT2FfBq75lYsY0_RYrIZwOy95ta1AgplOZoED8zpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو افشاگری جدید برنامه Jeremy kyle مشخص شده این زوجِ گی بعد از اینکه 3 سال باهم رابطه جنسی داشتن فهمیدن با همدیگه برادرن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78995" target="_blank">📅 19:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78994">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpL4_V49ZfO7SHm7pfsmGJ3oRmvTigXSf6IUL_MXaG5EsaanC0adzzY7mazFzGLt352r3g0itSwEB1JJt4VmgVSrr2YTnwbql5wzg6Plwl03wArtiPMoy7QkZ2EVIUcOQpOWsA6se3gWaM2QW0_IRc-wy88EB0EXI092djx90xkctZDQrhnNaYGjj7IRGWT6aoF4mz5Pck88rqUTnbIAY7QMCFxCX4Q2OY8M3PbUdqefsJ89z2FnkvMmCSHtx46NCnajwLK7IkUm1KgECy1ubOXi7A-7ZsrXZOZtREAZhBEOlkoeUrenOse1yi-9gecEURHWlWEEkhqypicy9YAKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تکست کصشری داره ترک جدید پوری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78994" target="_blank">📅 18:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78993">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz2L4YGOatNw1A9YtO5aiLgrispoSyiCPzKxrUWMx1_Fh6psfTtrjEE_ymdW438ke6DA8bwNE_c2L7EKcq-SszHM5KPtDv2TOw4DBELgdbx0lFn91gthva2UdcTkrXhZlwkRIjz4ppH0Knvic44hEN5Rj2cvH2udZzWiyHMNW7HAhtIhfJoZr08YskE4p_BL9jND09zGUbzs4rP1mMyG-t6HlTANBEZcZDtbR6aQf-l4VAMeXWXPscdgcMsVXCe2Dd2YjkPmHUX172kwxPnMZ71JMV1Bk-gxHhugQ-EF-jL56NBsekkl55ScN7xMpbxkl5grZgW47sCBPPXw3FpeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید گوگل و تبریک صعود به مصر :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/78993" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78990">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxE9c9cMwacX651CI07zEgbw1XmPlFpehQARCrAxZPJIfDE-XI--8Bzh2l8XBPQCZdw0H60KwC7yDeUe8_Xx0PsR0-7gJvOiNj0isOvATE4QR55oVYGrMiPoFyueS0QQqlKRIvRfHbe9mZxKOod87EF64cZ1yH0Mx3tUjV7He8O8SoiqZ41wfUsQNNEnGy0UEfAQau9t-n_Wj3yODBqK1Ep54pX6Ib8wksxooaOYB3UTMOavmQrF9usMb6_X_aQjrbMpbc2T2ze93VN9jMqZkMaVeKJ2UylEcBHWQF0J9zRKMVS_gEuwAwbBLUDYVgrEQP341eRnMYi36dkbEiNBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78990" target="_blank">📅 16:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78989">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد  @FunHipHop…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78989" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78987">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fblDjuMv0QzeS09r0Kfoca7VaKJ9zhNqi6EUpuzeW43sItvM8RkDPIPWLUWSiq6ilMGYAnygjH7H4jahv6V5DQB5cyDh5EWW_XO64KotfZtSF4hAzbYeafqf4LadcAgP9yO97W78wc4F_x0jrSSNc0kT5cNIn4rNxUKz7Y9Eg3_9lb3fbWTFPoOny-Nh_LRVenzZnn3JfOmLvdBIJZumPcK6CaUwA-ZaN-CMpY_zsx2jL920Xr3S_QDtYm4oclsK9tdME7eXfm1pNKIyTlDjrvpU09QKane7E3hMSGbx7wc2LlptRw_laJpNgmU1uScXaNM7EI0TTt2WpV5UELEL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز خبر اومد که رئیس‌جمهور عراق یهو زده به سیم آخر.
یه شِبه کودتا کرده و با لشکر کشی و تانک و... حدودا ۱۵ تا ۲۰ نفر از وزرا و نماینده‌های مجلس عراق که اکثرا حامی حشدالشعبی بودن رو دستگیر کرده.
با خودم فکر کردم که یعنی چی می‌تونه عامل این اتفاقات یهویی و غیر منتظره باشه تا اینکه با این خبر شاهکار روبه‌رو شدم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78987" target="_blank">📅 15:10 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
