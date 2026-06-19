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
<img src="https://cdn4.telesco.pe/file/JhXm_j_VTlTuWEsdcpxzKBf8PUWxeunYTdZO1mQk2_1Vb5V19cTagxVpMBO1uhwFQKcrhhQemAzrGy09_oT2wrS3HTGt8gdrctKal--c8ErY5JE-aw-20VBp24Vh8TeJoKsBxPjrBOi5rfeQidrfaKw7t0HEHaFj3HNpZ8kDoTQ3e77JLwZ5zkBij1sJniaVn-kFnzIfFoGnIGQfpaiIr4m56sBysyvFUAOd86ioSImGcz1lBwwua3qRmrzmun9J_Da2OvR7NzQVBuGsha1h1_-668-EckVGrrSVCot3i_Nn_p64BcItGp8ABvep_0WDST160wBxTVuIiiihhpVDDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 23:41:36</div>
<hr>

<div class="tg-post" id="msg-9163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">💦بابا به‌به💦.npvt</div>
  <div class="tg-doc-extra">16.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9163" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 406 · <a href="https://t.me/IranProxyV2/9163" target="_blank">📅 23:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مسئولیتهای زندگی دارن مزاحم عشق و حالم میشن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/IranProxyV2/9162" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKcJCo_17eHcqFssnLK6wrIZWv8pu1nAEYLgti27fzKaQDzhwdWE2vV1favy2vLRO3Spfy4D61uJQ7MjeFeZTsWCJch0F8ry-f6u4R0nBDEe-koTQijjjYD_keoSqD6WNvhxrIYatEzDSMuDDKh4EucjbKp5eONqEb-WQKnSN7FLSLf3ci8fKD9-QS0oUa601zK-Ivp69J1H6iSTdbZ8pzfdzUka7SmlI1wRdAYNkUb06QxDX9WKdq0lz0h8ipxjIzFg3V5Fw1IHT1qCnyt0NPretw0RhCfWoGHah_742-kPdwKDMlSVhPeX7Rc6ULaC6hFDsy3YxBh63FG9Xv_77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی مغزم به‌جای اینکه به حرفای طرف مقابل گوش بده شروع میکنه واسه خودش خیال بافی کردن:
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/IranProxyV2/9161" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9159">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">همیشه آخر راهنمایی‌هام به دوستام میگم "ولی بازم خودت میدونی" که اگه یه روز به فنا رفتن، بگم تقصیر من نبود.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/IranProxyV2/9159" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9158">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خانما لطفا نچرال باشین،
ویژگی های خاص صورتتون قشنگ تره!
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/IranProxyV2/9158" target="_blank">📅 16:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9157">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏اتفاقا خیلی خوبه آدم هول باشه، به شرطی که هول یک نفر باشه تا همیشه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/9157" target="_blank">📅 14:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9156">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyFwHcWiU6mN0ap4qUSy_wefLXhpaTxQjUyz3lhOBHIMR7bYtXfkzU-WVqe0okxAbnmou2nTzeDqA91Dh4UM1g43pqipROS-4fvRhRhe-36VilskbqBYwMzVrvzvq9mwmL16HYREOb17GeHkFhriSE4GA-qlWOGtjaoxo7ZkCwVoelKY7m-0qOIgz_0aW-uQs7QOFtryRGAws05_FMla7tGrdOPt0eVFYvTNHfQx0EcOWXlVGYhRZhkK4iSZSPeCOzuhB5RUX_iBRtglziDL1l2Yu_mEJDnR8UhwLzM5f8p0ZJR_4Tbs8gmKewaFIdd9Jz3WNPwCeTL0Xaa4gDPuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظریه پر طرفدار: ساعت عقربه‌ای خیلی قشنگ‌تر، شیک‌تر و جذاب‌تر از ساعت های هوشمنده.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/9156" target="_blank">📅 13:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9155">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
امروز 19 June، روزِ زشت‌ترین سگیه که تو زندگیت میشناسی.
پروکسی جدید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/9155" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9154">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جز خوردن چایی، پاسخی به مشکلات زندگی ندارم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/9154" target="_blank">📅 12:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9153">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">10 فیلم که باید با پارتنر خود ببینید :
1- Irreplaceable You
2- Always Be My Maybe
3- Falling Inn Love
4- To All The Boys I’ve Loved Before
5- Isn’t It Romantic
6- P.S. I Love You
7- About Time
8- Her
9- When We First Met
10- Alex Strangelove
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/9153" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9152">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Open vpn.ovpn</div>
  <div class="tg-doc-extra">6.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اوپن ویپن متصل سرعت بالا
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/9152" target="_blank">📅 10:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9151">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حتما تو زندگی قبلیم پولدار بودم و عادتش روم مونده وگرنه جیبم چطور جرات میکنه از این خرجا بکنه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/9151" target="_blank">📅 02:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9150">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فارس: ‏با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داده تا برای سناریوی حمله به ایران آماده بشن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/9150" target="_blank">📅 01:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9149">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دارم واسه جام جهانی می‌خونم ولی یکم امتحان دارم که نگاه کنم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/9149" target="_blank">📅 01:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9148">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عطار نیشابوری، اندازه نگهداشتن در روابط رو برای اینکه احترام از دست نره زیبایی سروده
"اگر گِرد کسی بسیار گَردی...
اگر چه بَس عزیزی، خوار گردی"
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/9148" target="_blank">📅 23:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9147">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1Th8_DJa3mpq8o89SiII-f3Cr3a7yYUzf4shdU8LxdThkkULladbTewxFeU1lMXKyVWE0mGfSLUgeoOsK0XyMvlwYflL04RKUGxMAfenxDI5EiOVN1Qy44a-a5xObrgJwAExdTUMWoKVQcSQ7GGF4BKiknUoRpf2aWaxZaIOlncp6_V1K9VE5dMk4eE217KzUObCNGBDcuIrjmVwz5ZJ3kCmJp96kvRmQGFcLNQe21aSFXsqHP0HjejYJokHCArYZJGZcMtGUjkgNqj_VqDGUlfVdXkdZe69IcLyihod1qw_UXEBvOxcnY_F16SYZwKWNl0GtFeRINZaYvEodf0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین مکان برای بوسیده شدن با رسم شکل.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/9147" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9146">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏مامانم فیک ترین خبر ممکن تو ایتا رو باور میکنه ولی حرف منو نه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/9146" target="_blank">📅 22:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9145">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🔥🔥.npvt</div>
  <div class="tg-doc-extra">24.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/9145" target="_blank">📅 21:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9144">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یه جمله امروز خوندم که خیلی تکان‌دهنده بود. ما رو بیدار می‌کنه و به زندگی‌مون و رفتارهامون آگاه می‌کنه:
«مرگ تو در یک روز معمولی، وسط برنامه‌های ناتمام فرا می‌رسد و جهان بدون تو ادامه خواهد داد.»
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/9144" target="_blank">📅 18:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeX-gfWzBZugkl7HCecyE2UC1p08Yzj3DFUN7iftvdRBQCPVD1VGbTUn6xe5l7Dp7-8OhVr9UFDZsluJQiIqaIuzxiSCFvzUj62xmA8SQ1ScvIvNygqcR7P2FqruaGCovUZCRYJp3oZsn77h-dBAdRd0igx1tTELEvHyMIdhJsX5aF861f76d_nw2aofAlCB_duRmDvGGrEWLGFVxC_FkQx8UfyBGOfjSoCfZFC6WGcxqpa13-JidcHe-uu9b8s_rKKcZzSXm13ASmEYRtxV7vjsCDIVYcLF1gPC_21c6U22Ao-MBQTsrV5N1zCDdtcwy_saIF15e3jpw8Wowhi2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور بازی جی‌تی‌ای 6 رسما منتشر شد و پیش فروشش از هفته بعد آغاز میشه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/IranProxyV2/9142" target="_blank">📅 18:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9141">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e2c48cc4.mp4?token=NgJ6e3cRFwnmQBNUxjd8Yd89EPUMpEgp-p34KcoRd5OXoqVXOV6ci2UrkU-Z7vF50eoeHfbf7RmPauXSK3m-MP1MQp-FxngPcPHCjd9HSau4yw825SkwmWgxUDSB37oQDmHKgMJcgpALML5a_1d4JKPuPk6SoVGVyzWi7wDex0rDf1Z_zWyExDC0AZacnJQ0GjGzWvWFTLrRzn97spzrL9p_af5_iCq2UDATCCLfIZxvY1YbLOOyxKaF-liJ8Ah8WwUphPaz8ROC2Xsk8Ljz5N17L1TvrGpOqTPjUgtycVJlPQADc5fyazNT2GfEINo5YL0zwmAV8uuaKpQNEFbhCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e2c48cc4.mp4?token=NgJ6e3cRFwnmQBNUxjd8Yd89EPUMpEgp-p34KcoRd5OXoqVXOV6ci2UrkU-Z7vF50eoeHfbf7RmPauXSK3m-MP1MQp-FxngPcPHCjd9HSau4yw825SkwmWgxUDSB37oQDmHKgMJcgpALML5a_1d4JKPuPk6SoVGVyzWi7wDex0rDf1Z_zWyExDC0AZacnJQ0GjGzWvWFTLrRzn97spzrL9p_af5_iCq2UDATCCLfIZxvY1YbLOOyxKaF-liJ8Ah8WwUphPaz8ROC2Xsk8Ljz5N17L1TvrGpOqTPjUgtycVJlPQADc5fyazNT2GfEINo5YL0zwmAV8uuaKpQNEFbhCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بنده در حال انتخاب اسکوپ‌های بستنی:
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/9141" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9140">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">طلا باید برای استفاده، زیبایی و لذت می‌بود، ماشین باید برای سوار شدن می‌بود، خونه باید سر پناه می‌بود، زمین باید برای خونه ساختن می‌بود، هیچکدوم نباید سرمایه و کاسبی می‌شدن. هیچکدوم نباید مایه‌ی این حجم از اظطراب و استرس و بخریم یا بفروشیم می‌شدن.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/9140" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9139">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWTS3O9-Ku9sLDJfbaApY5CiSXIyT4KZca5KGRGP_odV15B7ucwpmBAfk4Dpt8p8YWp3H8AMVpPqg8-WLnZcfsw0mIL00VExA91WaE378mz0fG6JD0bUVV5f05mTjg3EIbBMqlGoSwjv6s8y7OGmmjWNmxAfvKNgi5ZtGjwvAraC-VWR0ZyeKXos44rkkyxoqvlsBEcPXMPyOOjYh1Y6GalQQ3AtmZ0WtWpHLvAoysbR2FIk7q6lwqqH4KRvdOCt0d2t1JwccETIc4LFIj30c-6TasPztbUKemwakndQ7_c3N82_FnSBz_9ZpE1FV4L6p2ILOrTS0xkX3rTbeuRkLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- لغو 11
+ نوزاد شما با موفقیت لغو شد
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/9139" target="_blank">📅 16:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9138">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏وقتی پول دارین چهارتا یتیم رو خوشحال کنید که بهتون بگن ناجی، نه که برین مکه که چهارتا عرب بهتون بگن حاجی
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/9138" target="_blank">📅 14:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9137">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آدما خیلی دیر میرسن، خیلی دیر محبت کنن، خیلی دیر میفهمنت، خیلی دیر پشیمون میشن و دقیقا همین فاصله هاست که از چشمت میوفتن و دیگه هیچوقت بهشون حسی پیدا نمیکنی.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/9137" target="_blank">📅 12:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9136">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به فرزندان خود راهنما زدن، دنگ دادن، حرمت نون و نمک نگه داشتن، با دهن بسته غذا خوردن و متعهد بودن رو بیاموزید.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/9136" target="_blank">📅 11:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9135">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دیالوگ یه فیلمی بود که می‌گفت وقتی واسه زدن یه حرف دو دل شدی اون حرف رو نزن چون اگه درست بود شک نمی‌کردی.
‌
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/9135" target="_blank">📅 11:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9134">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQZ4dylaWo_PfczMciDGy8wfv4GWdRyfj5a5Ao9eAQYkSXQc8ODa-CvWn2wIvPckyfHpzwCYSdhcvMwIqGYBScJXU0Q46VZLjk-1QWZ0MbqB6zX-HOH2RxxvQXOiPN-khawCiAfZCv2BCuNENQFRQk7DO65vz3EujgRzzZhgz6Df-xp3S-kRYeMDGo-gjSe9O29g4OyyntLbVS9jUFEE-36kK1mtOzW7yqcdHjVgfxE1R9IZmHZoGW6d4RM7PS7E0YpGKvRTfrpSHv066M0HIqDLzfQj5nPSU_y52nvt1ITAjSQdf4VLvm0c7Mc1M8GZOd8_iw0NlIH9crvdR1M-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری میا خلیفه برای طارمی مظلوم
واقعیِ واقعی
پروکسی متصل
پروکسی متصل
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/9134" target="_blank">📅 10:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9133">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرصت‌ها معمولاً وقتی میان که دنبالشون نیستی.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/9133" target="_blank">📅 23:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9132">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm7ziVPKjoQGukTK6jNd-ifugnPev1nSk86cyFmoD_jQepviI8GzTddevKOTN0RmaoE5kFosb3psJgpONy94yo6BQhaUus6RQjH3ELZ0UPzrj9D19KB0idVKJuNMOtBOs5ZJ9lUV9fZHSaM0BgaFZo0-FXsDoLIl0qCf4kWaShY7JK9rKhxGV0rVZPY-GUElbL5ME1DtUEzLKjOXFPt8_uUQzgeeTixADoEvFnSFmRTPfzeCD07HJctyeg1fUZ_PtsJv-lIyUvHSz9Mv0uozTVYgwD0LxL-BPafgqTw2aaYYXnODpk2j26nYoRthLEmrSxeHV-MWVw0uuDVqJK97SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماهی زلال‌پرست وقتی داره میره به شب‌نشینی خرچنگ‌های مردابی:
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/9132" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9131">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏اولین تجربه روی زمین تجربه ی ناجالبی بود، دیگه تکرار نشه لطفاً.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/9131" target="_blank">📅 22:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9130">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مطمعن باشم شماهم مث من بازی پرتغالو بخاطر رونالدو میبینید دیگه؟
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/9130" target="_blank">📅 20:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9129">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏دلار هزار تومن گرون می شد
ثانیه ای جنس گرون می کردید!
الان که از اوجش ۳۵ تومن ریخته دست به قیمتاتون نمی زنید؟
خیلی پفیوزید (ایرانخودرو هم این وسط گرونتر کرده)
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/9129" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9128">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بچه بودم یادمه 3 ماه گریه کردم واسم یه
شمشیر پلاستیکی خریدن آخرشم با همون خودمو میزدن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/9128" target="_blank">📅 17:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/is44kP9DbUEKo9yq-Tvh78agw4RshcwTu6kRO69MubPTyNqD52waOYfn_tmI8sSFCsTnHtY5Hwj-0PgqStJ-LWpArle6Zox3wL9cjuw3sO-VJq_Hg4PRUTSNS9l_W7YB_VosOfURPvbsappST_yKYTyKjM0hPltiRQ8gzHu6eBa-zROz4rwPczUvpstnYvPz_QeLWXy_nMdHJsNgerp6-vjsywAX0Dkj_UX1KkmjttO8N5PEJx52Dh5yPQDzk5etdcpMEasxJXxZw5pI3B9zlPDQPystzItdMsBkMYegpx0xX0oRQ6paRTJP6sQCbqm4Da3Jx_QxgewXxs5VFjJhtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QhV7wbcrnQbYHRbMg35RlUkTmzlV1xSExTO1XnjW-uha6c8gpg1FFXXLhrvi7rpdGHGx_XXYMJEzmKYACtnZK2wns3eFnQSczgbKrlCnb03_NPM5ZgXAHusi4XPM2dQrTB7xeiPWFDAjniIs5xHgd9Ws6bI12HwussrRIDHIzug6LeKdnoKJodCBoB0lzgyXpq4BBtx37omhkZ1jjZ5IN6H25rJMb8TGlEzqsBts2b9brwf13RBOVYucM9rRd5emcHWMq8jhUuNTe1PoWOy0dJVmbEmgFOPBxw-VOaHaVUikLzFe8-15ZGO5wcpHQ4D1SmNS6poKqplml0wyfPhNZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چین یه توالت رباتیک ساخته که با یه دکمه میاد کنار تختت، کارت که تموم شد می‌شورتت و خشکت می‌کنه، بعدشم میره خودش رو تخلیه و تمیز می‌کنه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/IranProxyV2/9126" target="_blank">📅 17:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9125">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شما دو ماه بطور جدی روزی نیم ساعت تا ۴۵ دقیقه زبان تمرین کن، هر زبانی. اگه اعتماد به نفست عجیب نرفت بالا حتی اگه لولت اونقد تغییر نکنه،که میکنه . روتین برای یادگیری زبان معجزه میکنه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/9125" target="_blank">📅 13:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9124">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از آدمایی که دلخوری و ناراحتیشونو واضح بهم میگن و انتظار ندارن که بهم الهام بشه خوشم میاد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/9124" target="_blank">📅 13:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9122">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bryYlb6R0t2XRbdTazZpEw4WIeNItA9N4B1KpQWfiIEKadthElW6TuMD4Po6dLE6rkt6JRj4Vabe_iTGnyLmcpC4JIUxbpEgfDWFYMTj7_kLFP-b9TGeAFvmDE4RvCxfs1VqAzCShKsZXpwHfJX-booZUrLrTK8Rt9SrA7op4tfpDrWEdzMuUJOIV7sMVehuuerPDESk-wrqsVlks3ynjtY8_lvNuN1vGsHv2208h67_4_dBYqNUCDWN7TGy7So3CGZ3vQJZM2ENWVNd9HlII17VnFuQP6dmDxComGIQ-2M8PkvO68urMxnRkpu3lcGntXi-ud7pc-3rsoDNZZDmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjrU9mwTiPQQhSCAO9Oy_LOFEWB0Kh2AyBk92JmqwseGg2uFhBbjzhCKilWVQUOG4vpnlJ1pet9XPh_STU77XfYHk4Z31GLiPJD1nUKETsrrmOCU315J2c8NI2RtKXnDUEr5VWfTuUHbYYvWauI7TOJHSpKNYHXt3s2F1bu-kgd64PRx-cgtmzBxPSWtCW4Z_p5D5wF8VTHgEs07IwNZztILJHmPaI0fDUJs2Oqi1cDVsLJLL5uUzx8_Ix5w7fivPUatEniFTQ0UDGPzONrIUriruE_yM6Zwwsu7DzRlPmX9iNlXVwUdTZLWrWi16S9M8pubfk91DP6QetANex5h6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیوت بودن اگه عکس بود
🥹
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/IranProxyV2/9122" target="_blank">📅 12:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9121">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">راز رابطه ی موفق یک‌کلمه است :
احترام.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/9121" target="_blank">📅 12:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9119">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یکی از خوبی‌های پول نداشتن اینه که همه دارن از مشکلات بانکی که پیش اومده میگن، و تو اصلا خبر نداری
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/IranProxyV2/9119" target="_blank">📅 10:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9118">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">از آدم‌هایی که در رو نمیبندن متنفرم، در اتاق، کابینت، کمد، دستشویی، مخصوصا دهن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/9118" target="_blank">📅 23:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9117">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">100 گیگ کانفیگ رایگان
✅
https://188.121.124.130:8000/sub/djMsNDAsMTc4MTYzNTMzNw2e14b71496
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/IranProxyV2/9117" target="_blank">📅 22:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9116">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏امروز روز جهانی برآورده شدن آرزوهاست و هیچ ربطی به ما ایرانی‌ها نداره.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/IranProxyV2/9116" target="_blank">📅 22:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9115">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">میشه به همه احترام گذاشت به جز رفیقم، اگ به اون احترام بزارم فکر میکنه باهاش غریبه شدم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/IranProxyV2/9115" target="_blank">📅 22:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏دوستان رک بخوام بهتون بگم برای هیچکس مهم نیست که شما تو نوت اینستاگرام چه آهنگی رو دارید گوش میدید.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/9114" target="_blank">📅 21:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX1-rhlbo477TuYyrqCl5NWFybRlOFR1ebsOb1m1PRf9k1wYmOzSNRBK91vtk9oms4zj8n-wHLK-SeHYPvu3tV-CvSPY-p2wj1uxE4xiuA89wrlMDYOjnLPCtTAhJMlX-Ph9Tb0O_rt2H7ilcSNP5aW86Tm0grBWUOspSx1aQTcmR5jFNgQrr2or0W2G3qqDWvNgSLMY1itXJSjrPq0oZAX7K2b0tG5EFXRAeze2DVRu4lNksXUZIt1CzltDnot9gVfawundisMmbCa25SQPIhbUpduOy32WE1GnX2ev1Jx-wpJ--nRB5HwyjPOu514RkkbSnjhkS2eUdmynmF1IZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">﻿زوج پزشک ایرانی ۳۱۳ عمل جراحی رایگان را به عنوان مهریه ازدواج خود ثبت کردند.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/IranProxyV2/9113" target="_blank">📅 20:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkRAkXAaUYGDVf2ghPUeIRFkpI20_Uh7DzGjCDIF2tjvspZ0yPj0J-XjcAk-6g6gNEWolCcGuzbbAommN3CDxnNfhxGbRlnyq0EdyCyYRG0iyEgyPYNcompR29W4rTalz9ns8di_kU9sHQSjKNRRDWhyCyx-RaMNZ7qGuA6512fXusVjVTMKGVgmWJ1AnIX-PtuoyU9Qi-dwomLwNOnTs096n90vdHMtRU-by1oj9fgewOK3JyWO7-hCEiJ7-IW4GIdZZzlA8F-M2Vzn_RVNsNoDBQgvM2gnVTq-Vm6eNt1WHdhnFCS-IyjWyrjoGHbltBbwZTbEAUN6b6PJA0yhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/9112" target="_blank">📅 18:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مسئولیت‌های زندگی دارن مزاحم افسردگیم می‌شن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/IranProxyV2/9111" target="_blank">📅 15:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آخه آمریکای لامصب؛ تو که ساعتت انقدر با بقیه دنیا فرق می‌کنه، برای چی میزبان جام جهانی میشی؟
آخه کی 5 صبح فوتبال می‌بینه
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/IranProxyV2/9110" target="_blank">📅 13:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سلام بر کسانی که،
وجودشان از غم این دنیا می‌کاهد...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/IranProxyV2/9109" target="_blank">📅 11:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BETX7qMdl5GKaw8c3HIvGM9kDl0kp4sRrjtJxWry6XsZnuv9yGWQoYHNa9hX0P_Gru0tlxaESmpzUItPIU6IHTZGaMEXBSQxbuW-LKcTmMEKa-pbavDGsrx6B8ZjlLq2SkwHKLFRTazCejCWAfZN2b7RK2qbQ54-HHRRKYzAczHMrDMM-hoFhtW-_PiVUAVvVUNIMMp-Qru58csm1sKihXpnrUoZUTHzWbuZrDNx1toORCW394LrlI5CQ37muf0zLZP1jW5vdei_frBw3wanMhCoOvGny3AZcMmCuKUn-oaYgz4VkiuUUJoZJM1wvO3NdKNIcs2j3i3HGrPCHlSpUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی ساعت اینو ازش بگیره :))
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/IranProxyV2/9108" target="_blank">📅 03:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوست باید جوری باشه که هم بشه باهاش بی حد و مرز چرند و پرت گفت، هم حرفای عمیق درست درمون زد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/IranProxyV2/9107" target="_blank">📅 03:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242ac19f99.mp4?token=VXfYLPGctIzvGlSb9wM_4bGk2ncHZ3-AHxIabwNd86DEDxuFfO80rlbwDKUrYjUn7iAgrdVR_9UvzXF3naaoCra5fWBRdyxfkbmzfiMHno5fJX6SAeb05NA440_7oEZPE9inasRtz2VStLXHAlRmmOc3O3JWfA_u2UeJKGga924bcgThTLzEe8mWiTZ20RwolPOdXq0TnPPg63Ro9rfqCOQ6AkrS7aAKPfS9UoXZPO-pFgYRIuFebNbTPgnq8qHMZMXmO4NCene47jdt3tk-OErlG1a9_SCIXfXi6GurZ4C-_koDetAZB1zHP5hPrhde6mAqtNOIjG3GwikhkKN3qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242ac19f99.mp4?token=VXfYLPGctIzvGlSb9wM_4bGk2ncHZ3-AHxIabwNd86DEDxuFfO80rlbwDKUrYjUn7iAgrdVR_9UvzXF3naaoCra5fWBRdyxfkbmzfiMHno5fJX6SAeb05NA440_7oEZPE9inasRtz2VStLXHAlRmmOc3O3JWfA_u2UeJKGga924bcgThTLzEe8mWiTZ20RwolPOdXq0TnPPg63Ro9rfqCOQ6AkrS7aAKPfS9UoXZPO-pFgYRIuFebNbTPgnq8qHMZMXmO4NCene47jdt3tk-OErlG1a9_SCIXfXi6GurZ4C-_koDetAZB1zHP5hPrhde6mAqtNOIjG3GwikhkKN3qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر خوشگله core
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/9106" target="_blank">📅 03:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2MezrvTUxhG3QcPpg-TsaGnLCMYhm-g0BbUSBP33E0f23TpD9hTIlsACxhQSdMuf9zA0EZNwaVAJ26v7478SWbGYSznoBCkZDH55uEH_F0ATwNLRS5jIw1W6t72-9ukgjCifMv2XboFtrTcyfVSVFOhB6AJsNwxHSpNj0o9MiT1UmPvY_bO9oDTshnrl3zjC00_ex1YEz4OgUCWbEJWSW-jsSxD0w2VCnoUcMGjZsicrOT-KiGWt9j-ZcFNlXN0meogSErrYAPSS2F1bVhM1gMiRHkzh0CD-g6aVCSQqv3WAae9BEgl0SXHy1l6TKv8JZRReMrpexHxmUdkKG1x_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 8 هزار
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/9105" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9103">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تیتانیوم 94.npvt</div>
  <div class="tg-doc-extra">52.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9103" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🔝
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/IranProxyV2/9103" target="_blank">📅 14:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=87.248.129.183&port=443&secret=ee74531eb0ee43745c6ddb8efe247626cb3132333333332e732e732e732e652e6565666566656665662e69722d2d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/IranProxyV2/9102" target="_blank">📅 14:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">50Gb Cfox_Server A76.npvt</div>
  <div class="tg-doc-extra">7.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9101" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/IranProxyV2/9101" target="_blank">📅 14:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=194.120.230.97&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/IranProxyV2/9100" target="_blank">📅 14:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6j_LvhHG1itYFFmZwaPUd6UeYePzeqku7ycqkX1LaNAwkoJMiEkTt6MSRsFlotQot-TlX-iAW9yq5cT5qmuBZv5m2pAVhCsUSqab2XNRQfcM85ZNujTrfg8WjNaPSGZPlhsDsgTijJiL_dB63Ujv15HDSXrrYWHaZFsRNENxoQ1NjCaAWmhaGCydP1ywSW9sh1Yx5h7npg8iPQahXnY9U1EhlRVk5Qo8iw3PgyzhaqRS0yWTA1JEydQPZjnG5JTjoXKCEBCr6FmTbsOiiyMvgi8cJ6luD7SUJfQxXhnyVknwZGwsy6N9NK2ivxvVbe5lcH85RsP4K2XC5EI7NnQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 6 هزار
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/IranProxyV2/9099" target="_blank">📅 14:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=play.proxyvpn.site&port=443&secret=ee4d0c82ca73f261e6933ec36e5d902ff6706c61792e70726f787976706e2e73697465
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/IranProxyV2/9098" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فوق پر سرعت🔥.npvt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9097" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💯
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/IranProxyV2/9097" target="_blank">📅 13:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">TIMSAR 263.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/IranProxyV2/9096" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-poll">
<h4>📊 بت زن داریم؟</h4>
<ul>
<li>✓ اره</li>
<li>✓ نه</li>
</ul>
</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/IranProxyV2/9095" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🐝.npvt</div>
  <div class="tg-doc-extra">4.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/IranProxyV2/9094" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🇨🇦.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9093" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/IranProxyV2/9093" target="_blank">📅 18:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">◀️
دوستان این تخفیف فقط تا آخر امشبه</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/IranProxyV2/9092" target="_blank">📅 21:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9090">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://d3d046fa-d372-430a-8ed9-083d62c44efb@45.130.125.194:8443?mode=auto&path=%2F%3Fed%3D2053&security=tls&alpn=h3%2Ch2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A1000000%2C%22scMaxConcurrentPosts%22%3A100%2C%22scMinPostsIntervalMs%22%3A30%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22noGRPCHeader%22%3Afalse%7D&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=ssd.mojaz-persian-music.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/IranProxyV2/9090" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9089">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=51.250.65.108&port=443&secret=ee3a9f22462890489c0bde045048ff9a17617669746f2e7275
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/IranProxyV2/9089" target="_blank">📅 11:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9088">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فول متصل⚡️.npvt</div>
  <div class="tg-doc-extra">149.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9088" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
🆓
npv tunnel
🙂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/IranProxyV2/9088" target="_blank">📅 11:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9087">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=zone.nolags.pw&port=443&secret=dd04d2a884220d45de24af8bade64322ac
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/IranProxyV2/9087" target="_blank">📅 21:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9086">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ʙᴇꜱᴛ🇳🇱🇩🇪⚡🚀.npvt</div>
  <div class="tg-doc-extra">14.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لوکیشن هلند و آلمان
🇳🇱
🇩🇪
Npv tunnel npsternet
💥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/IranProxyV2/9086" target="_blank">📅 20:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نامحدود🛰️.npvt</div>
  <div class="tg-doc-extra">149.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9085" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
👀
Npv tunnel npsternet
🛡
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/IranProxyV2/9085" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9084">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes⛱️.npvt</div>
  <div class="tg-doc-extra">3.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9084" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
💯
Npv tunnel npsternet
🟢
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/IranProxyV2/9084" target="_blank">📅 19:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CIVAX🍔.npvt</div>
  <div class="tg-doc-extra">1.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9083" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پرسرعت وصله دان بزنید
⚡️
Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/IranProxyV2/9083" target="_blank">📅 17:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9082">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇺🇸سرور آمریکا.npvt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9082" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✔️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/IranProxyV2/9082" target="_blank">📅 16:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9081">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🚀🇩🇪.npvt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9081" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
💙
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/IranProxyV2/9081" target="_blank">📅 03:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9080">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=87.248.129.219&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/IranProxyV2/9080" target="_blank">📅 03:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9079">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🇳🇱.npvt</div>
  <div class="tg-doc-extra">24.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9079" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
📊
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/IranProxyV2/9079" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9078">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به…</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/IranProxyV2/9078" target="_blank">📅 03:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9077">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پرسرعت💯.npvt</div>
  <div class="tg-doc-extra">3.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9077" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/IranProxyV2/9077" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9076">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
چنل دوممون مربوط ب اخبار رو دنبال کنید
✅
با ما اخبار جنگی بروز باشید
@russiamilitery</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/IranProxyV2/9076" target="_blank">📅 01:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9075">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d71xSaqaHz1xNbAqQVk-DbQXQKbOzsged5UDzV2hgvtqmdt64fmuL_Xb81qUF_c6ZaW2XPXwKMEIaCN36e9brrSen2ej4fBOqJLAewsYaEi_W9mev_s9A6FJLf_KIx8XAy7egQOCVRii3dtHbxpteHijBeMhtIGK6jOZ4-HH2CgDJkDeMPKUn8v7OqJUxWEk8tb0iXLToLmKWgdHGHQR27F8r4qB_KuPfY4GscLO433jTwoL8XdZHUvCaKrgPM1GiMxnVi30_j-Gr5hgYy-04fTldkkGtikDh0MME3_xQHIOi_eJWSDUwfjvbh1BL8Nlb3FmFDUVCrpCLSnMWQLkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت اختلال و قطعی نت بصورت موقت مارو در روبیکا دنبال کنید، هرمتود رایگان متصلی که پیدا کنیم براتون قرار میدیم.
🔴
rubika:
@activityall</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/IranProxyV2/9075" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9074">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=157.90.171.183&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=178.105.50.21&port=8443&secret=dd104462821249bd7ac51913020c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/IranProxyV2/9074" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9073">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=north.nolags.pw&port=443&secret=dd9760e74174fb9717de21cc7e17027e34
https://t.me/proxy?server=87.248.129.226&port=443&secret=FgMBAgABAAH8AwOG4kw63QFgMBAgABAAH8AwOG4kw63Q
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/IranProxyV2/9073" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9072">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
احتمال اختلال و قطعی اینترنت بالاست
کار ضروری دارید انجام بدید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/IranProxyV2/9072" target="_blank">📅 00:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9071">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری/ترامپ : به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/IranProxyV2/9071" target="_blank">📅 23:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9070">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=46.224.226.79&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=91.98.229.218&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/IranProxyV2/9070" target="_blank">📅 21:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9069">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
ترامپ: شاید نیروگاه‌ها و پل‌هارو بزنم شایدم نزنم، محرمانه‌ست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/IranProxyV2/9069" target="_blank">📅 19:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9068">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
💣
🇺🇸
فوری ترامپ: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. ما بمباران رو از سر خواهیم گرفت. ما حق انجام این کار رو داریم. آنها هلیکوپتر ما رو ساقط کردن.
🚨
ترامپ: ما امروز دوباره به آنها حمله میکنیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/IranProxyV2/9068" target="_blank">📅 19:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9067">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4lzIUEzXDCLDPZUYDXVrJvn69loQmUKcny77jG-PhrxRXiChY64mGGPQGRzosqM96Fhm2cfnBMHbLQsQ49HkdyOVQ4kZyCBn8GBCxV8Upfh_zSTfJbDa89BFZ35eAp764nKsBL5HjR3SeiVDXob_cRR9bkc-QkRkKLfWTxVPGbT28x7Fygj2lZFwGwy8Ums2SBwVugp4XUl5yPqYCT2-BzsepluWxWGWj255YBLfnJSw50zd-M66uCakdo-P6mhV3oL729amIPSXM8To-plE9Tx0WROlSSOv9Ey5UMUfxU-3kvKOJIlkUxIpmdAxAb8PRXl1lVjcjtt3U6HguXW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/IranProxyV2/9067" target="_blank">📅 18:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9066">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تازه نفس♥️🤌🏻.npvt</div>
  <div class="tg-doc-extra">1.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🎁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/IranProxyV2/9066" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9065">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرعت قوی🚀🔥.npvt</div>
  <div class="tg-doc-extra">2.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9065" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/IranProxyV2/9065" target="_blank">📅 17:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9064">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دکترنیک ظهرونه.npvt</div>
  <div class="tg-doc-extra">17.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9064" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/IranProxyV2/9064" target="_blank">📅 17:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9063">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🐕‍🦺.npvt</div>
  <div class="tg-doc-extra">6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/IranProxyV2/9063" target="_blank">📅 17:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9062">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری
-
ترامپ به فاکس نیوز :
به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/IranProxyV2/9062" target="_blank">📅 15:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9061">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db9gAZHfDXrovOjCWobFHF-kFRNoLQbhgEuCfuLMnNNrYrSiLsZl6U0ZIs_OoY0TLbHTX4Gj5NpQ3Mrbn3SAaI-_e8N5pIBwXejZ-B4Z70uEM6mE20_0g2JEiM9py0riF0yvhkI34OPTgXqy8au-lpscxHjZKtznyOKtkDBl-XAHCDzkKqbMsBch4_yPQkx1SWoA-vMygn3h6Xcu7A87LEqoWUn9e1ryLUU9MaFFw9KLMHZAxwko3LsI7_wX2RG9gmL1W6qjHi3eSOeo_QGqhn9xDtGd0b4_TnXeIcT0zSIdYCZxEt95iGS2wKQj6pH52qRq5I4qHzn7DjNpY9lI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری-
ترامپ:
«ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد!!! آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!!!»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/IranProxyV2/9061" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9060">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اکثر نتا وصله
🍸
✅
vless://9dbaa630-c895-4883-aa8a-20e8a48ff4b2@fff.oakcup.ir:2052?encryption=none&type=httpupgrade&path=%2Fapi&host=Ip.oakcup.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://5960576d-829e-4d09-8232-0e80121a6fe4@45.130.125.193:8443?encryption=none&type=xhttp&security=tls&path=%2F%3Fed&mode=auto&sni=ssj.new-persian-song.ir&alpn=h2&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://0c09799a-47ca-494e-a50e-828632ef9d81@199.232.78.159:443?encryption=none&type=ws&security=tls&path=%2F&host=bazaryabab.global.ssl.fastly.net&sni=default.ssl.fastly.net&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://5960576d-829e-4d09-8232-0e80121a6fe4@45.130.125.162:8443?encryption=none&type=xhttp&security=tls&path=%2F%3Fed&host=vi.mojaz-persian-music.ir&mode=auto&sni=vi.mojaz-persian-music.ir&alpn=h2&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://07dce2d7-9849-4e22-adb9-36d2763c3b89@snapp.ir:2095?encryption=none&type=ws&path=%2F&host=api.aramonlineshop.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://fc965ad9-bdd7-4815-ad71-b39ec5972dc1@141.193.213.11:443?encryption=none&type=ws&security=tls&path=%2Ftsghdws&host=octopusss4.com&sni=octopusss4.com&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://cabbfe13-038b-4dbb-9c45-5079c829abfa@167.82.0.1:80?encryption=none&type=ws&path=%2F&host=max-gb1.global.ssl.fastly.net#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://8dc7722c-2767-4eea-a28b-2f8daacc07e3@sca11.myfymain.com:8880?encryption=none&type=grpc&mode=gun#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://fc965ad9-bdd7-4815-ad71-b39ec5972dc1@89.116.46.68:443?encryption=none&type=ws&security=tls&path=%2Ftsghdws&host=octopusss4.com&sni=octopusss4.com&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://44b3ee72-cffb-4d66-ab7c-3138b9bdeeef@54.36.162.217:443?encryption=none&type=tcp&security=reality&headerType=none&sni=speedtest.net&fp=chrome&allowInsecure=1&pbk=upTVUrc_t7xF1ULni8pHRDhRES1sT4BDm1r8rugTzyQ&sid=ff815f58c7e77aa9&flow=xtls-rprx-vision#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e4e7866d-920b-4a53-a8e2-6ae9b2a42fc2@47.77.214.201:10035?encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://ae852d97-85f5-45cf-82a4-254eba345480@144.31.131.33:443?encryption=none&type=tcp&security=reality&headerType=none&sni=cdn.cdnjst.org&fp=chrome&allowInsecure=1&pbk=djH9iD2QV748ocK-wPH7HvDd03lu88zHhS4G-61w6Dc&sid=a120&flow=xtls-rprx-vision#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://d3d59da0-31a4-45da-bf9e-373c6ab140db@62.60.251.131:45656?encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e0de62c9-f317-4275-b7e5-8da7b7fa9bc6@77.110.127.191:9443?encryption=none&type=ws&path=%2Fpourya#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprMWRCT21PQjRvcWk3VW1wMzdhMWJR@82.38.31.192:8080#
%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/IranProxyV2/9060" target="_blank">📅 12:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9059">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=45.32.233.182&port=8443&secret=dd1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=mercedes.nine-gear.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/IranProxyV2/9059" target="_blank">📅 03:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9058">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
♨️
مهر:
شنیده شدن مجدد صدای انفجار در جاسک
✅
موج دوم حمله درحال انجامه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/IranProxyV2/9058" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9057">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
لیست جدید پروکسی متصل پخش کنید مخصوص نت ملی و شرایط عادی
🇮🇷
https://t.me/proxy?server=87.248.129.106&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.235&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d#proxydotnet
https://t.me/proxy?server=protocol.fast-mt.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=proxy.speedbreaker.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=free.feel-fly.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=www.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.107&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=172.65.104.042&port=25565&secret=7hYDAQIAAQAB_AMDhuJMOt1iaXNjb3R0aS55ZWt0YW5ldC5jb20
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/IranProxyV2/9057" target="_blank">📅 02:30 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
