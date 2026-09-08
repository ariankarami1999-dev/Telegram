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
<img src="https://cdn4.telesco.pe/file/O09Lk02bvORMsBNhKxcrzcS6JO_t9OhFhUGZzyXHFAaeWk8H75L9eCD6euCTu_RzMCd6EswLcEf8s4pU1TRwG6muryiXD7ynJAKVYrCHPW4cxAsjBNPUrHf8qgSOLeINL6EK19GMDZWL15idwssn-QmBIAIfH8vX2pg_qV-1V6knavnUh1sZ3CyTQS2Yt6ZRrOIR7mHznp5pal8vckfZ5LIenvGbBhTWQHJ-kVaYanqN0S6CYSp6jLsh-2zyE_tN2W9o7jBmw9usF4ILXr5JdZ6HSBAsjbXKLzTpBuHp_n2h2oQjkkvOVBirPB-RBS0mCER6xZzxzt7GdzXXUsnWWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 449K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 00:16:33</div>
<hr>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/withyashar/22606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اخطار اولیه  نیروی هوایی آمریکا و تاکیید به هدف قرار دادن موتور خانه و و دادن ۱۰ دقیقه زمان به خدمه برای ترک  محدوده موتورخانه
@WarRoom</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/withyashar/22606" target="_blank">📅 00:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش حمله موشکی آمریکا به سومین نفتکش ایران در سواحل شهرستان جاسک
@WarRoom</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/withyashar/22605" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تحلیل ساده
@WarRoom</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/withyashar/22604" target="_blank">📅 00:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دلار ۲۲۹،۲۰۰ تومان (سقف تاریخی)
تتر ۲۲۹،۲۰۰ تومان (سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/22603" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش پرتاب موشک از کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/22602" target="_blank">📅 23:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و…. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/22601" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرنگار صداوسیما:
ارتش آمریکا به نفتکش دوم در نزدیکی آب‌های جاسک حمله کرد.خدمه هر دو نفتکش با قایق نجات در حال انتقال به سمت ساحل جاسک هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/22600" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پس برم زیر سماور رو روشن کنم
🤣</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/22599" target="_blank">📅 23:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رویترز: امشب در سراسر خاورمیانه آماده باش جنگی است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/22598" target="_blank">📅 23:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مقام آمریکایی به وال استریت ژورنال: ایران دوشنبه، برای دومین بار، حمله‌ای را علیه کشتی‌های متعلق به نیروی دریایی آمریکا انجام داد
@WarRoom</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/22597" target="_blank">📅 23:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سپاه : به تمامی خدمه نفتکش ها در محدود اسکله های کویت و بحرین که میزبان آمریکایی ها و شریکشان هستند اخطار می دهیم شناور خود را چه در لنگر گاه و چه در اسکله ها سریعا ترک نمایند چرا که مورد هدف  قرار خواهند گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/22596" target="_blank">📅 23:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کامنت برای ترامپ
https://www.instagram.com/reel/DdCe4x2B6Qc/?comment_id=18626069959030735</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/22595" target="_blank">📅 23:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سپاه پاسداران اعلام کرد حملات موشکی جمهوری اسلامی علیه پایگاه‌های آمریکا در خاورمیانه به‌زودی آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/22594" target="_blank">📅 23:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مقام آمریکایی به فاکس‌نیوز : نفت‌کش‌های ایرانی را در نزدیکی خارک و جاسک هدف قرار دادیم.
این بخشی از تلاش گسترده‌تر برای اعمال فشار اقتصادی بر ایران است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/22593" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رسانه های رژیم : دو تانکر نفتکش در خارگ و یک نفتکش ایران در جاسک هدف حمله آمریکا قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/22592" target="_blank">📅 23:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/22591" target="_blank">📅 23:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22590">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش های زیاد از صدای ۲ انفجار در جاسک  @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/22590" target="_blank">📅 23:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رسانه های رژیم تازه تایید کردن</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/22589" target="_blank">📅 23:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">منابع محلی خارگ اعلام کردند که این حمله خوشبختانه هیچ‌گونه خسارت جانی به‌ همراه نداشته و کارکنان نفتکش در حال تخلیه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/22588" target="_blank">📅 23:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏I24NEWS :  نیروهای آمریکایی در تنگه هرمز به نفتکش‌های ایرانی حمله کردند @WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/22587" target="_blank">📅 22:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22586">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">صدای انفجار جدید از جاسک (ممکنه جاسک پرتاب دفاعی رژیم باشه)
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/22586" target="_blank">📅 22:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش انفجار مهیب در تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/22585" target="_blank">📅 22:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏I24NEWS :  نیروهای آمریکایی در تنگه هرمز به نفتکش‌های ایرانی حمله کردند
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/22584" target="_blank">📅 22:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22583">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/22583" target="_blank">📅 22:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4IToL8PTdtxTQMVLy5jQf-WUXgqG3buWZFRRuuW9ZkILY9KzhqXeRWiMQ7xhF-05q21TvtVJJL1f8hdO8rd1A_TwgvBIgY4f8c2xLEdIafpCBdqvOiCIpvTxt4wdJDU1015yEUdGiZhdsjnGlk8AUhpUtl2r1RJfx4hShh5AbG6RW_MrR0gp8t6pVPnqZkCye-lFnkP49cVVAeeP3mJHwIxb89fPQvmNUGFhWlxaxbEHlsEyHyN0P6ZkFib5IuT0aQESIYY1blJeCH4ZSC5FgAluBCZM5wBB-T3Gi8DhTke9e5eBs64IKOuILFkI8fP3bzA9qCkU6QJd305cHfn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد @WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/22582" target="_blank">📅 22:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/22581" target="_blank">📅 22:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22580">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/22580" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFThhiHq1b5d8SYMuXxvoo1K2DIfJf1sGlCBGXQiMIxfMrirVjqBOgQWvp4pdG9_xDw7zJ6_AM8OjQXhuVTnCmdFDxiy4_CPcAWqa8CLolSmFoJQX7AFjm2GRvE_OveQ4PvlyKSYiwy2Q55ybN3lHqcZOXb6FxTtq7DmbNwwG-YpAaWJxGM-E83D0Wh0aADG-8Yy-FkRubxoVAeCD3Lzwh_Qvwias2F5u6z2eukWESw09DQbW_S8SCjxJ7Wf_FH5ms1tplEt0Ks86hu2D2Gw9LNL_LsqwRzIap0ahbrkQEyUI6SoNTL6RsUHWwKcVgvarMLbgPQpuxMnL2be4XPy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/22579" target="_blank">📅 22:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/22578" target="_blank">📅 22:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">😾</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/22577" target="_blank">📅 22:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22576">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">صدای انفجار ها در محدوده لنگرگاه جزیره ( محل نفتکش ها ) بوده و خارگ در ارامش کامل است تا این  لحظه @WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/22576" target="_blank">📅 22:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سخنگوی سنتکام :
یک فروند زیردریایی بدون سرنشین ما روز گذشته طی یک ماموریت نقشه‌برداری از آب‌های سرزمینی دچار نقص فنی شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/22575" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش های زیاد تایید نشده ، خارگ آمریکا داره ۲ تا نفتکش رو میزنه  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/22574" target="_blank">📅 22:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش های زیاد تایید نشده ، خارگ آمریکا داره ۲ تا نفتکش رو میزنه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/22573" target="_blank">📅 22:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c17de1b0c.mp4?token=Ex5bQXyKkRLKERvFLR1eUwICMILZzfyawhWcQwSanPvUyx5hCooeGx7_QLUZQSxDmGaDyi3OgtyrWWWrwECQ7bD-7egbhcmNLE6RTh1WYB0LhEuZ8CDHa2XDvCCQMeOqf2xt2HMQqyFwxNBiKG4rl1Mc4a_APcI6DDwgOH2EAKSinULOo40XO1NRaZgWIp19GbvLU77UDTwCB9FqRXaWYY_ryKG5_HztBMsYBf_FGPbHXVfaNA3j17_rYHk2pFH7iaZvkP16EvQ9nEjXDlvOmhYN0EHH9epTQRv_OBXk9JbxcWTLgNBezwbQQjxPPDhp1gs4h9kk1inT5nrneX_P3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c17de1b0c.mp4?token=Ex5bQXyKkRLKERvFLR1eUwICMILZzfyawhWcQwSanPvUyx5hCooeGx7_QLUZQSxDmGaDyi3OgtyrWWWrwECQ7bD-7egbhcmNLE6RTh1WYB0LhEuZ8CDHa2XDvCCQMeOqf2xt2HMQqyFwxNBiKG4rl1Mc4a_APcI6DDwgOH2EAKSinULOo40XO1NRaZgWIp19GbvLU77UDTwCB9FqRXaWYY_ryKG5_HztBMsYBf_FGPbHXVfaNA3j17_rYHk2pFH7iaZvkP16EvQ9nEjXDlvOmhYN0EHH9epTQRv_OBXk9JbxcWTLgNBezwbQQjxPPDhp1gs4h9kk1inT5nrneX_P3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: یک زیردریایی نظامی آمریکایی بیش از یک روز پیش در خاورمیانه دچار نقص فنی شده بود. بر این اساس، ادعای سپاه پاسداران مبنی بر اینکه یک زیردریایی بدون سرنشین آمریکایی را در منطقه توقیف کرده، صحت ندارد و این شناور پیش از آن دچار نقص فنی شده بود. با این حال،…</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/22572" target="_blank">📅 22:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز: یک زیردریایی نظامی آمریکایی بیش از یک روز پیش در خاورمیانه دچار نقص فنی شده بود.
بر این اساس، ادعای سپاه پاسداران مبنی بر اینکه یک زیردریایی بدون سرنشین آمریکایی را در منطقه توقیف کرده، صحت ندارد و این شناور پیش از آن دچار نقص فنی شده بود.
با این حال، آمریکا تاکنون به‌طور رسمی از دست دادن این سامانه را تأیید نکرده و مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/22571" target="_blank">📅 21:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/22570" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22569">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/22569" target="_blank">📅 21:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش های زیاد از صدای ۲ انفجار در جاسک
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22568" target="_blank">📅 21:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22567" target="_blank">📅 21:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S14Gqud64XcK_-Z78XVDWS7Urv2brqqAlqBH_VtJ8q1iLUIZ_bpMA8dAp5lFH_a1UJsa9wN36RgJOFWlN-3EJ9hWZQ9wraorIJiG-BBjFwWJXXhBwjTv619fgKMFwAfPmdIAhwK8_Bst3kj3Vr2L8tqOU3pCqjHCVk-7NdTVzAQK0W6OJoj_wHtGyZOhvqXa0hiAcoHaLlvc3lr1Vvmjw9nGmjPLcC1pYt8-D54OJa3911kfvTBiUQsWOJPnViLGSoMHT8iXJwho7I9uPzxckF0GZ4Bi8Ohsd6EcNi1sWhyrtCHFj4wLkJfIjSuT1mo4DD6OdOTjIceyQnkXKvCelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل فردا، چهارشنبه ۹ سپتامبر، رویداد ویژه خود را برگزار می‌کند و انتظار می‌رود از آیفون ۱۸ پرو، آیفون ۱۸ پرو مکس و آیفون اولترا؛ نخستین آیفون تاشوی اپل، رونمایی شود.این رویداد
ساعت ۲۰:۳۰ به وقت ایران
آغاز می‌شود. آیفون ۱۸ معمولی، آیفون ۱۸e و نسل جدید آیفون Air احتمالاً در مراسم فردا معرفی نمی‌شوند و عرضه آن‌ها به بهار ۲۰۲۷ موکول خواهد شد.
نام «آیفون اولترا» برای مدل تاشو هنوز به‌صورت رسمی از سوی اپل تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22566" target="_blank">📅 21:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22565">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4dcb0a04.mp4?token=F-K9N-oCHWkWpBJ4lSg1LVRkZvyRasEKmRrzcfGfjQZMu6Y8MKJxgJwRe3OoA40BsZuf18jVL_-dPi2xJNk4a0dPkwfr7Tw7waFYyQQfqTynEjuszSM0w1OrhmxWruhcfbf4C5m5IocJWLDBjXG_POn3asvz8IC2lkvzWZWBojiSxLNe420Sq8gXQtTY_MPxD315cW2tMtgDtZZEWoNwYukigVaDWvKvGY_NHLUNn2FZCVNnOSYAKpFljB2kjmanV2COmeWTO0wD9mRIIqWtm8Q1GcItbzOnw-gFrbMPU0ECrVvhPrF5GzaDiKxow3tnOs558q2PCpq-57u52GqaUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4dcb0a04.mp4?token=F-K9N-oCHWkWpBJ4lSg1LVRkZvyRasEKmRrzcfGfjQZMu6Y8MKJxgJwRe3OoA40BsZuf18jVL_-dPi2xJNk4a0dPkwfr7Tw7waFYyQQfqTynEjuszSM0w1OrhmxWruhcfbf4C5m5IocJWLDBjXG_POn3asvz8IC2lkvzWZWBojiSxLNe420Sq8gXQtTY_MPxD315cW2tMtgDtZZEWoNwYukigVaDWvKvGY_NHLUNn2FZCVNnOSYAKpFljB2kjmanV2COmeWTO0wD9mRIIqWtm8Q1GcItbzOnw-gFrbMPU0ECrVvhPrF5GzaDiKxow3tnOs558q2PCpq-57u52GqaUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و…. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22565" target="_blank">📅 20:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoorena</strong></div>
<div class="tg-text">سلام یاشار رفتم خونه پدربزرگ دیدم هی داره پزشکیان رو فحش میده بعد فهمیدم بخاطر پست هایی که مخصوص دارن گرونی رو میندازن گردن دولت پزشکیان به همراه همه این بدبختیا انگار این گرونی بنزین یه پروژه هست دوباره برای هدایت خشم مردم به سمت دولت و نه رژیم مردم باید خیلی هوشیار باشن</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22564" target="_blank">📅 20:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cadaeb8025.mp4?token=jo2-wqwD8c2JoLIECDSR5pYOoscvyvQ_s35G8pMEDu2iJM6zJPmFekNU_UfXZnEkbheuGCFcjCvTrwg0u87bve9GH5wKIZ-GCAYbsE26JRb35bUUwRl3hjonaNyzGq2k6VU5UwqiRK19Nr6VWB1Q52Q8CZ7iFQlhpnG7tmKgXUsOBVhX86oiMsQaOH0BqTheb2bawuc6lPXOlfqCrOMEzNV3wA1pHZlHN1oQ2kunMYH3zT8mAKg_KGfXIXNGx44TNw8d03YDHPPmsR5h_IgwqBNKiI9BltVPxnlWAsLlkTphvzm4CrPwZF1hkpl5s2nFz6OjMBD9KYOWpy_3A8D_HmR-2T9CQ49w_zqPkRoxOoasal-5_e2-BMnNJI09sSOX-3PXIg8yBRZG3Y5LibCxfYHv_UVgTppUX7Ks_gdfA3U6Bqc-TzA60j3hKtTtq_SELwcwuAOnEXxKAgDyew7XApGJecrmJh8_FODteEJ6FVjzU6EVrXkhVwPnuQW7kKujnWeK2EP5yse0a0JcGVNmq-J8efxWrYL_c8G4KNS-5VQQKpfWfe9S1bwrZqi2F2H1r1-58qtmvi58fNDJSvyFaz-fXvXcbcfpkdhCYw29gaXHHa9Rc-82m2-esLIO6RrLUZWZz9P7q20rLFjh6NtUoexmpVFN78bEUEZhVutxIns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cadaeb8025.mp4?token=jo2-wqwD8c2JoLIECDSR5pYOoscvyvQ_s35G8pMEDu2iJM6zJPmFekNU_UfXZnEkbheuGCFcjCvTrwg0u87bve9GH5wKIZ-GCAYbsE26JRb35bUUwRl3hjonaNyzGq2k6VU5UwqiRK19Nr6VWB1Q52Q8CZ7iFQlhpnG7tmKgXUsOBVhX86oiMsQaOH0BqTheb2bawuc6lPXOlfqCrOMEzNV3wA1pHZlHN1oQ2kunMYH3zT8mAKg_KGfXIXNGx44TNw8d03YDHPPmsR5h_IgwqBNKiI9BltVPxnlWAsLlkTphvzm4CrPwZF1hkpl5s2nFz6OjMBD9KYOWpy_3A8D_HmR-2T9CQ49w_zqPkRoxOoasal-5_e2-BMnNJI09sSOX-3PXIg8yBRZG3Y5LibCxfYHv_UVgTppUX7Ks_gdfA3U6Bqc-TzA60j3hKtTtq_SELwcwuAOnEXxKAgDyew7XApGJecrmJh8_FODteEJ6FVjzU6EVrXkhVwPnuQW7kKujnWeK2EP5yse0a0JcGVNmq-J8efxWrYL_c8G4KNS-5VQQKpfWfe9S1bwrZqi2F2H1r1-58qtmvi58fNDJSvyFaz-fXvXcbcfpkdhCYw29gaXHHa9Rc-82m2-esLIO6RrLUZWZz9P7q20rLFjh6NtUoexmpVFN78bEUEZhVutxIns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت: «وقتی بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود. در حیاط‌مان مارهای سمی زیادی داشتیم. اگر سر مار را قطع کنید، مار مرده است؛ اما خودش نمی‌داند که مرده. بنابراین باید مراقب باشید، چون سر مار هنوز می‌تواند شما را نیش بزند و دمش هم ممکن است تا غروب آفتاب تکان بخورد. اما وقتی خورشید غروب می‌کند و هوا خنک می‌شود، دم هم دیگر از تکان خوردن می‌ایستد.
مار ایرانی، یعنی رهبری ایران، هنوز نمی‌داند که مرده است؛ اما مرده است.
»
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22563" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه
حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و….
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22562" target="_blank">📅 20:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22561" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دلار ۲۲۹،۰۰۰ تومان (سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22560" target="_blank">📅 19:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9ayJyehcckSGDroHG-uY8nnERjR7wZCDAwAeSh9aM8MsksbYGxt0ICJCrQpN3Vjn3uCd4O0BVNlYcBqZPMKiBW6t3d3bSjPE73UZRzipyrRsXauDGC7RQo7DcsWSHD3bBPiQj8mvK5MfBoRAb9I0pz2r5VC1uEDCRuu7A7Y1hs-Dxknuf7xUWr3h2klFLGRXJ4JRfpNH5gz1hN3d2G1XocGFqZX0BS_7oM0Xi7aSyoWCEDz3Xtm2h-QxJ5MEEi098W2tK22iNSfunqYsVyrIBAfUAiK8vZcqy1Whv4LxRVPJR8GB_YyCAlXjzvvRR2nzSpAPcv3ywNdNr1Mj3c4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا اعلام کرد هرگونه همکاری مؤسسات یا شرکت‌ها با صنایع هوایی ایران، می‌تواند به خروج آنها از تجارت جهانی منجر شود + لیست تمام شرکت های هواپیمایی‌تحریک شده
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22559" target="_blank">📅 19:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سپاه مدعی به دام انداختن یک شناور زیرسطحی بدون‌سرنشین آمریکایی در دهانه تنگه هرمز شد. گزارش‌ها احتمال می‌دهند این شناور از نوع Dive-LD ساخت شرکت آمریکایی اندوریل باشد؛ رباتی حدود ۳ تُن با توان ۱۰ روز فعالیت زیر آب و عملیات در عمق ۶ هزار متری که برای شناسایی، نقشه‌برداری، کشف مین و پایش کابل‌ها و خطوط لوله استفاده می‌شود. در صورت تأیید، دسترسی ایران به فناوری و حسگرهای این سامانه می‌تواند اهمیت اطلاعاتی و نظامی قابل‌توجهی داشته باشد,
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22558" target="_blank">📅 19:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eab716e17.mp4?token=CiYbwUP1RxdwJPsOr9ogGquBbpeD5Y5kypwcOPNXpm5uGGCTAYJXqLtE011UqXUEvh2gw6xWAQlRBmqENNCEa1RLmjGkEM5ge7T71W1l0vDfOY-LRy08HWLLcg7WA02nvXAlTailnZ9TKzgm3frBmg2rmTt0Gsog33vO0uiFuAwWW3J2XDEuYpkSdflLwOcaGM7NKfo2_kjnlTjm-nXm-6t1ThPv2U2Y10fSqFGxFcSeMkQ7POOHcN910-QTunofZJtjdnwPJIHItZAj_e3hzkuryfBdkKRgLMnRmTrYtoUIgYE6kF9iZaY8pF1cnBuXSZoEFTXk1_Scm1r9t28x5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eab716e17.mp4?token=CiYbwUP1RxdwJPsOr9ogGquBbpeD5Y5kypwcOPNXpm5uGGCTAYJXqLtE011UqXUEvh2gw6xWAQlRBmqENNCEa1RLmjGkEM5ge7T71W1l0vDfOY-LRy08HWLLcg7WA02nvXAlTailnZ9TKzgm3frBmg2rmTt0Gsog33vO0uiFuAwWW3J2XDEuYpkSdflLwOcaGM7NKfo2_kjnlTjm-nXm-6t1ThPv2U2Y10fSqFGxFcSeMkQ7POOHcN910-QTunofZJtjdnwPJIHItZAj_e3hzkuryfBdkKRgLMnRmTrYtoUIgYE6kF9iZaY8pF1cnBuXSZoEFTXk1_Scm1r9t28x5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی‌بی‌اس نیوز: خلبان آمریکایی جنگنده‌ای که در جریان جنگ در ایران سقوط کرد، برای نخستین‌بار در برنامه «۶۰ دقیقه» درباره این حادثه و عملیات نجاتش صحبت خواهد کرد.
این گفت‌وگو قرار است
یکشنبه آینده
از شبکه CBS پخش شود و جزئیات تازه‌ای از ماجرای سقوط جنگنده و فرار و نجات خدمه در داخل ایران را روایت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22557" target="_blank">📅 18:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شاهزاده رضا پهلوی در واکنش‌به پدر یکی از جاوید نام ها که به زندگی خود پایان داد؛ از روان‌شناسان، روان‌پزشکان و درمانگران ایرانی خواست برای حمایت فوری، مستمر و محرمانه از خانواده‌های جاویدنامان پیش‌قدم شوند. او همچنین از هم‌میهنان خواست منتظر درخواست کمک نمانند و اگر خانواده‌ای از جاویدنامان را می‌شناسند، به سراغشان بروند، احوالشان را بپرسند و در کنارشان بمانند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22556" target="_blank">📅 18:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c20f289d7.mp4?token=cp0xAEsqyqfZEHaTKbWHch0SW0Ti6A1CdgiSDynwhpnRpISa-1-tmGoBg2JgSZxtTs3YLbY-y3Y1f1K8oyhL5rggmLue3lBHSSHUid17xbDKDXhJ_k7XwJlnmiyTwCfLVsGF0U9R7eXv4A0GClP6RB9X6VoHIgM1AuBODbJcB2lGFeXB8YCAgNnQ0m_Qq-nVp9rDE0eN74NpFNm6nTclXyzSQUI_ldSi3wurMg2VtgFzIHrNBxg04xEYSuIweGFJ_HOjEIriUiiIJ5VnCDyF_IeF3jinPkW_gPCKuv7AYdLhOUqyXCruttRcgss0AdiVCW9CkBruA0PfKIn6Y2Sl1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c20f289d7.mp4?token=cp0xAEsqyqfZEHaTKbWHch0SW0Ti6A1CdgiSDynwhpnRpISa-1-tmGoBg2JgSZxtTs3YLbY-y3Y1f1K8oyhL5rggmLue3lBHSSHUid17xbDKDXhJ_k7XwJlnmiyTwCfLVsGF0U9R7eXv4A0GClP6RB9X6VoHIgM1AuBODbJcB2lGFeXB8YCAgNnQ0m_Qq-nVp9rDE0eN74NpFNm6nTclXyzSQUI_ldSi3wurMg2VtgFzIHrNBxg04xEYSuIweGFJ_HOjEIriUiiIJ5VnCDyF_IeF3jinPkW_gPCKuv7AYdLhOUqyXCruttRcgss0AdiVCW9CkBruA0PfKIn6Y2Sl1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران دیگر هیچ شانسی برای دستیابی به سلاح هسته‌ای ندارد و تحریم‌ها علیه آن مؤثر بوده و نتایجی فراتر از انتظارات به همراه داشته است.
ما الان داریم می‌جنگیم چون ایران می‌خواست سلاح هسته‌ای داشته باشد و خیلی به دستیابی به آن نزدیک بود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22555" target="_blank">📅 18:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بلومبرگ: نخست‌وزیر جدید بریتانیا با استفاده آمریکا از پایگاه‌های نظامی این کشور برای جنگ با جمهوری اسلامی مشکلی ندارد و این موضوع را تأیید کرده است
، دولت بریتانیا در چارچوب همکاری نظامی با آمریکا،
اجازه استفاده از پایگاه‌های بریتانیا برای عملیات مرتبط با درگیری با ایران
را داده است. این موضوع در حالی مطرح شده که نقش و میزان مشارکت نظامی لندن در جنگ با ایران همچنان مورد توجه است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22554" target="_blank">📅 18:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آمریکا ۲۸ شرکت هواپیمایی ایرانی را تحریم کرد
؛ دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا سه‌شنبه ۱۷ شهریور،
۲۸ شرکت هواپیمایی ایرانی، ۷ شرکت مرتبط با بخش هوانوردی و یک تبعه مصری ساکن امارات
را به فهرست تحریم‌ها اضافه کرد. از جمله شرکت‌های تحریم‌شده
آتا، چابهار، ایران‌ایرتور، آسمان، کیش، کارون، قشم، سپهران، تابان، زاگرس، وارش و فلای‌پرشیا
هستند. همچنین چند شرکت در
امارات، بریتانیا، ترکیه، مالزی و قزاقستان
به دلیل ارتباط با ماهان‌ایر یا شبکه‌های مرتبط با آن تحریم شدند. آمریکا همچنین
مجوز عمومی G-1 ایران برای صادرات مجدد موقت برخی هواپیماهای غیرنظامی به ایران را تعلیق کرد
و هم‌زمان مجوزهای جدیدی برای پایان دادن به برخی معاملات مرتبط با هوانوردی غیرنظامی صادر کرد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22553" target="_blank">📅 18:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تهران و کرج صدای رعد سنگینی شنیده شد همه نیم متر پریدن و فک کردن حمله شروع شده
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22552" target="_blank">📅 16:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22551">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری رسمی کره‌جنوبی،
یونهاپ (Yonhap)
، امروز گزارش داده وزارت دفاع کره‌جنوبی اعلام کرد یک تیم تحقیقاتی برای
ارزیابی وضعیت امنیتی تنگه هرمز و بررسی شرایط منطقه
اعزام شده است. سئول همچنان در حال بررسی گزینه اعزام نیرو برای مشارکت در تأمین امنیت کشتیرانی در هرمز است، اما
هنوز تصمیم نهایی درباره اعزام نیروی نظامی گرفته نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22551" target="_blank">📅 16:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پرتاب موشک از کرمان به سمت تنگه هرمز، نقشه و عکس ارسالی @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22550" target="_blank">📅 16:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22549">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqi6d7c1Eou0jjGJM23HA9QSgODArsUJTCxY-3CSM_4Zwld4bnPn-wZSwJrn1smN0P-0R5epLLGNQ5KcVXHTVrqszCB5oE4uamEGG_1kBZm9r7b8VvGBlnCH0A5n26s9Fvi2GUnxOgWhmOdf8c63E30Vfeqghz4NfevLR4VbVMP1zrYcDA6Qj6MH8V1NNl69TJVK-oE0XmXWra2q7SdpScU43vgrAY5Tb3Z-hge0rmVq1e5ZbDdmJi9Bqj3wtP2_3rJY6s-22XL6ceXghznVHIJ_JlMagJkXBRXrodQzatTn8wO96rzRNJFBpvx-q35YoZz14steneijKScSMf0yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش های بسیار از صدای انفجار از محدوده زندان قزلحصار و هم اکنون عکس و رؤیت ستون دود از این محدوده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22549" target="_blank">📅 15:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22548">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjJu5jRxOq8tO4CploZhH5c_SNvzWddpU-JOOBfdTkMOSisPyZ_jQKpMe7464aNl1cIEw9QiGlgGgDnYC8u5YESwLXi5i3Pcm-58S3nuCBp2d2EztDIkU3nS7VknQ3uGtVO3MPukLH6vv0IbGd64JzB_KdQGHOudts0obMxPOrbt3o5qOBJyJIoqB1SzvEIt6XLFbf_4-nCHbP91-28UWIIF0PBTEnJPLVZztjE_-bV2zm0EQi-eYm-iEYgT6qW0lS8OoYShES6VPfQqGMftgbOENQBF-N-3_sG4FAna-Bj-BkJcwa528mpWzOUtqDqjd3jA5BaxrALn8Mus2K2-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غرب شمال غزه هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22548" target="_blank">📅 15:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پزشکیان: نسل جدید با دستور همراه نمی‌شود؛ باید با او گفت‌وگو کرد
نمی‌توان صرفاً دستور داد و انتظار داشت نسل جدید از آن تبعیت کند. او تأکید کرد تحول در نظام تربیتی باید متناسب با شرایط نسل جدید و با نگاهی آینده‌نگر باشد و حل مسائل جامعه نیز به
تقویت گفت‌وگو و استفاده از ظرفیت‌های مردمی در مسجد و محله
نیاز دارد. وی همچنین گفت آنچه امروز در جامعه دیده می‌شود، برونداد نظام تربیتی کشور است و برخی فرصت‌ها برای تربیت نسل جدید در دوران کودکی و نوجوانی به اندازه کافی مورد استفاده قرار نگرفته است
@WarRoom
یاشار : این نسل شیک پاسارگادی خر نمیشه
🫶🏻
✌🏼</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22547" target="_blank">📅 15:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رویترز : دولت انگلیس امروز قوانین جدیدی برای تشدید فشار اقتصادی بر ایران ارائه کرد؛ این اقدامات
بخش‌های انرژی، فلزات، بانکداری، بیمه و کشتیرانی
را هدف قرار می‌دهد و محدودیت‌های تجاری و مالی علیه تهران را گسترش می‌دهد. همچنین اختیارات لندن برای تحریم کشتی‌های مرتبط با ایران افزایش یافته و
فرود هواپیماهای ایرانی در انگلیس ممنوع خواهد شد، مگر در موارد استثنایی
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22546" target="_blank">📅 15:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXT1i7kCjbtqdbcik5Qmkr3SSz4PuPQXU0gjXg5CDuYReFh5rXele6NzKrNwC28l4_2W1WU5DJ-XgTf56w0VeTcTxMq0KQXtULUIycNOWOhN-vXYnBnv3qbSwRqXiD-3v-qnWyRgoG71PoZpp-GdCEtZkvzuyAv-jI4MduVuZOfGd3MeQ0WG1HVBn7YGZG6I4HRJMU8NmpNUt2HEcO0WQyxXxiUJLPqUj9gsg-wgJw3gO0soqTKXi_Wz3F2ceTUeVHwS5excnwtzgOHsONUBw_b4QCNf5hAs8l-4KqTdfn7Eifc-RlqlpUCoT1rOtxThGnmDyw6qktfP9n0Wjjb6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پیش عبدالرووف اسحاقی، فرمانده بسیج پارود در سیستان بلوچستان به هلاکت رسید
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22545" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1rg4eY0d9p1Ax-0rUHhNJVCOGqUibq3cKVVj9FEEtNLsLGPIOGt6FOWaRHTwMMW0r2U2yw-XpLta9fmLOOCCFFEVtineoIfz6Bir8BmmM20WzT-rbhC9Ix7WeQ17qp8anqhDOPk96uXPQFx_ktj4vsKbOW52BOoLCHC0jgMxdExo6W2CLq18StIzjoT4MH62gSAhqT2WAJ14kX_Ag47hIpyUivCKjfJDNPXR9PW5XL4g9Afahp84c1M_iCgK2R-OFZIJn9_VzVwjyk3LFehLcuhVjLHDAr6j6XT9iYTHpT9Gdx3NdnMzqk5lTCWafu2MZB0FBJUnJUMmPuKFd2tng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک بالستیک از کرمان به دریای مکران
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22544" target="_blank">📅 14:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22543">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXvU7u1bAZJbYaCBpIavk7qfRSxgSDvKETfutl49DnxyVqXzy79UwNRFUi2JZtqk-AOORABhWVsU0XYwHbSi6QtVWpBMDORoe0JLDHntT3Y1bvkVFpvECXc2HDkrAsJIN1jKmN4hYgawkKKe3v5L8Y6tSzTcGEqAt6-j8HikASvlDDqz37g0glWvN3sMLJcpMUOluPYAsRrLLxNm8u_qLj6vsT7SbJhkWPLaoBTg3EcjGZOUP-vEK6dx8VoAltqPrH4m-v1zSpQf8HQqEJdpdhNUx2Bn42Sr_bNtAHbZJpEd6RJtppFA20lo_T7QBBJtzVo3oMsfe-39Co6avqwU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از کرمان به سمت تنگه هرمز، نقشه و عکس ارسالی
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22543" target="_blank">📅 14:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش های متعدد از پرتاب موشک از کرمان به سمت دریا
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22542" target="_blank">📅 14:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دیشب اعتراض به گرانی بنزین در کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22541" target="_blank">📅 14:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c790194bb.mp4?token=X75KLELvOEoRyHyCl0XGl3l1m6ejAQqvX13LjuSdCQ68x4hcSim-jBY1_had2iN7eQZ638u4-IHUdwQsoJ28QU6VpWLJvBAaJAhJamyui1_dk6aRHgBKTdsr0ZkJxN56ulRITsYue-FzwPsmBaK_bLmw7jk20C6oKPYh36oOVNYcoU1KvIp9oKNnAEJbtQ3iqQJM3zBxpFcvxCZt9gvKnjlPTDiMliiKj03zKG-ceYyVZeauLV-koFY7G-sKBtM_oToFvAuj6yzUgEM36nup50QOCZMQsPhpnLgSfz91emB41wE4V_65dYdIgdB3EQVM_llfKer3WEJGcTV-Qk1vk45ahYIvPxD9Cb_aU7M3XgcoRtB8hCzMVfwg25b5z4bTJOMlXo_vY3NBacbcs9z-5nTP6993Zmeu02qlIOkiakUv02hFxo0dCyKknimLtZPiQ4C17wD_CQ9E26nIYekrGH2x-wKBap9D1TWbT2LYe4-QBkMd6MDAfpenxxwWzLZdmOv2lzIgY_8EqwnVloBMi78bOPR9x3RJ65DsDPpn_540JYHsaqjFJU5mdU7MuyAizjEFqIwAOaTTs6atnUHXKc7i2f-kqE7yNWNp48Jm1o_b84vifNlYsKhT7ah3nLSsP17-uBLoF7kfIjJqHOJfNaycAtv83VTlDRcAKDgwgGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c790194bb.mp4?token=X75KLELvOEoRyHyCl0XGl3l1m6ejAQqvX13LjuSdCQ68x4hcSim-jBY1_had2iN7eQZ638u4-IHUdwQsoJ28QU6VpWLJvBAaJAhJamyui1_dk6aRHgBKTdsr0ZkJxN56ulRITsYue-FzwPsmBaK_bLmw7jk20C6oKPYh36oOVNYcoU1KvIp9oKNnAEJbtQ3iqQJM3zBxpFcvxCZt9gvKnjlPTDiMliiKj03zKG-ceYyVZeauLV-koFY7G-sKBtM_oToFvAuj6yzUgEM36nup50QOCZMQsPhpnLgSfz91emB41wE4V_65dYdIgdB3EQVM_llfKer3WEJGcTV-Qk1vk45ahYIvPxD9Cb_aU7M3XgcoRtB8hCzMVfwg25b5z4bTJOMlXo_vY3NBacbcs9z-5nTP6993Zmeu02qlIOkiakUv02hFxo0dCyKknimLtZPiQ4C17wD_CQ9E26nIYekrGH2x-wKBap9D1TWbT2LYe4-QBkMd6MDAfpenxxwWzLZdmOv2lzIgY_8EqwnVloBMi78bOPR9x3RJ65DsDPpn_540JYHsaqjFJU5mdU7MuyAizjEFqIwAOaTTs6atnUHXKc7i2f-kqE7yNWNp48Jm1o_b84vifNlYsKhT7ah3nLSsP17-uBLoF7kfIjJqHOJfNaycAtv83VTlDRcAKDgwgGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب اعتراض به گرانی بنزین در کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22540" target="_blank">📅 13:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اتاق جنگ با یاشار : مردم شریف ایران، شرایط ایمنی حمل‌ونقل کشور به‌شدت نگران‌کننده شده است. در بخش هوانوردی، گزارش‌هایی از اختلال سامانه‌های ناوبری گزارش شده همچنین بعد از‌جنگ اکثر سامانه های راداری نابود شده اند و از ترس حملات خاموش کردن عمدی ترانسپوندر برخی…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22539" target="_blank">📅 13:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش هایی ااز پمپ بنزین پاسداران و پیروزی هم دارم ، ایست شدید و چک کردن گوشی ها هم انجام میشه کاربری گفت گوشی دوستشو چک کردن و گرفتنش @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22538" target="_blank">📅 13:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK M</strong></div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22537" target="_blank">📅 13:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcOZZvCq1R6PjEwHmYmvjtez9zCHa5Wf8K3MM6y1oRhmaxluJrEKQOH1a95TjTqiNcPzcgIDqswWceIRxouCaeNhys9EB-wsQV_Hn9QOcY8Z7VKf5FuLb9XLuUyJCZzEIdQ1NIVV4Z34iyM5dcHjjWzABDlrr3LNZsvXm6oSZIDw5P0G75dFLM2h7D9fmdOKU4wWvpx5LGYuJi2YJb_J-i-MTo7zLmkQXsC2HHkvXK0vzs6cnckCsFQrdQ35vZ3fkncgOnDu0onKA9V8Zff9vMNGUgTEZKOaymep11vaO29MF7u8u7BDoT-w16MT12eCwlM1zsZdG4JWXSi3D-m4vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : درخواستی :
یمن وارد فاز درگیری گسترده با حوثی‌ها شده؛
چند جبهه از الجوف و مأرب تا البیضاء، الضالع، تعز و حدیده هم‌زمان فعال شده‌اند و نیروهای ضدحوثی در برخی مناطق پیشروی کرده‌اند. نیروهای دولتی یمن در الجوف و البیضاء نیز مدعی پیشروی هستند؛ در این جبهه‌ها نیروهای دولت یمن، قبایل محلی، نیروهای نزدیک به عربستان و گروه‌های مورد حمایت، از جمله نیروهای طارق صالح و العمالقه، حضور دارند. به نظر می‌رسد هدف اصلی افزایش فشار بر حوثی‌ها و عقب‌راندن آنها از مناطق نزدیک به باب‌المندب باشد؛ زیرا هم‌زمانی این جبهه‌ها حوثی‌ها را مجبور می‌کند نیرو و تجهیزات خود را میان چند محور تقسیم کنند. الجزیره به نقل از معاون وزیر دفاع یمن: «تصمیم برای آزادسازی صنعا و یکسره کردن کار گرفته شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22536" target="_blank">📅 13:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پزشکیان در توییتر: با توجه به ادامه حملات و شرایط ، جنگ ادامه خواهد داشت
جمهوری اسلامی ایران همواره با جنگ مخالف بوده و حفظ منافع مردم و امنیت منطقه را در پرهیز از آتش افروزی دانسته است. اما چنانکه تا امروز در برابر تجاوز، دلیرانه به دفاع برخاسته است این مقاومت را تا پشیمانی کامل متجاوزان با قوت ادامه خواهد داد و پاسدار حقوق ملت بزرگ ایران خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22535" target="_blank">📅 12:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22534" target="_blank">📅 11:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22533" target="_blank">📅 11:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به گزارش TRT ترکیه :
آمریکا پیشنهاد جدیدی را از طریق پاکستان به تهران منتقل کرده است
.
وزارت امور خارجه ایران اعلام کرد تهران در حال بررسی آخرین پیشنهاد ارائه‌شده از سوی آمریکا با میانجی‌گری پاکستان است؛ هم‌زمان دونالد ترامپ از قرار داشتن مذاکرات در «مراحل نهایی» خبر داد و دو طرف هشدارهایی درباره احتمال ازسرگیری حملات نظامی مطرح کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22532" target="_blank">📅 11:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tASEcSrW0RK2O8-_ld-t0m9JffhmgBknHtycUDYHDWAlaKVZH7gEPpKlVWleUNYRD0_edjRDad_C3InhXPxldcto9QfUTv7DN8BLtEqnSf7en1hKR8fk0rP9pbJq4tvoK48kj8LsrJcsUm1sYoCVvHw8yCwwR1cV-C4Jh54taTyp9-JAM6N56eSk9Hbxrmff7h4WwWfaklXMIrk7NJFNXvGuGXA8dkWr6rxwTUXxdf6MR34TM5-XOnqFtDQia8jL34VXfsvBimpD4NEUGgA23CfWLDlkMI_3jjvOwsJvfBLTpbaWlYSyWTKPntjzGa6d20l4_lP-kCoK6gs18W1G8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت ۹۹.۱۰$
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22531" target="_blank">📅 11:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الکسی لیخاچف، مدیرعامل شرکت دولتی روس‌اتم، در پاسخ به پرسشی درباره ساخت نیروگاه‌های جدید در ایران گفت: «بدون شک، آنها چنین علاقه‌ای دارند.
ایران علاقه‌مند به گسترش همکاری با روسیه برای ساخت واحدهای جدید نیروگاه هسته‌ای است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22530" target="_blank">📅 11:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی: دسترسی به برنامه هسته‌ای ایران باید فوراً برقرار شود
رافائل گروسی هشدار داده نبود دسترسی و اطلاعات کافی درباره مواد و تأسیسات هسته‌ای ایران یک نگرانی جدی برای اشاعه هسته‌ای است. همزمان آمریکا، بریتانیا، فرانسه و آلمان برای
ارجاع پرونده ایران به شورای امنیت
تلاش می‌کنند.
نمایندگی جمهوری اسلامی نزد آژانس
اعلام کرده اجرای کامل تعهدات پادمانی
تا زمانی که آمریکا و اسرائیل حملات خود را متوقف نکنند، از دید تهران قابل اجرا نیست
و گروسی باید ابتدا خواستار توقف حملات شود.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22529" target="_blank">📅 10:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تحولات امروز در اطراف علی‌الطاهر
پس از اعلام کنترل اسرائیل،
حملات اسرائیل در منطقه نبطیه و اطراف علی‌الطاهر ادامه یافته
و کفررمان، در نزدیکی این ارتفاعات، نیز هدف حملات سنگین قرار گرفته است. رویترز از کشته‌شدن دست‌کم
۱۲ نفر
در حمله به کفررمان خبر داده است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22528" target="_blank">📅 10:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وال‌استریت ژورنال : درآمد نفتی ایران در حال خشک‌شدن است
، بارگیری نفت ایران پس از محاصره دریایی آمریکا
۸۵ درصد کاهش یافته
و ذخایر نفتی شناور ایران از حدود ۹۰ میلیون بشکه در ژوئیه به حدود
۲۹ میلیون بشکه
رسیده است. این روزنامه پیش‌بینی کرده ذخایر موجود در صورت ادامه روند فعلی تا اواسط اکتبر به‌شدت کاهش یابد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22527" target="_blank">📅 10:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fllc6RJ8FjN0751BJDBqOX8Ie_0MXSfQls5nWiyLwKtgL_BFCCAGQ764eMTjUdEZz0trGVh6O2HrmGaH3IN8J_BpNNHlDd3BW02BJLF5KIA-1NlXNBdOfzNOuLm42zhXbyQoFGHZwrGUxNEUDWFkw2YM4auksVM0r80idOX_v7Glg0lhL8EVqgknraXHdddGoSUZ55sUevS5qUw5YtYrdEOnYV5qZf8Tm_h5bNOH2HSg_YldPCMCmc6TgQ6ngVomRaJ6NAdroNW1FIoGjS5MHLKMvphvqUH8aVlZhe1XEQE9CUfc8kUSrtuk1p77ZnPi7v5hplMh5FqWvlQfzXzpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : قیمت نفت با پیروزی ما در جنگ با ایران، به‌شدت سقوط خواهد کرد؛ درست مانند همه‌چیز دیگری که در حال کاهش است، اما حتی بیشتر! قیمت هر گالن نفت به ۳ دلار خواهد رسید و در نهایت به کمتر از ۲ دلار در هر گالن خواهد رسید. همه این اتفاقات به‌سرعت رخ خواهد داد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22526" target="_blank">📅 06:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh2a_g4FfWgeZlBRWVEmm5EdPUHDA7EnhWxJqLSRuSoB4ZDfPow4AGA8PhwfzKfu1MLB4s2dkkVA4dfvM8BCi2NbqdteDOAC5xCyh2cr8XhbHaARFQa0uVCv8HqLQ6kXjAthjc1vPw_H3WVpYIH6PQYU5vwwPu7r6hu9kexkz0f6Sry07VUJDFD2QJEHXTYo4AgBOX2o9j8LMNJ158CF7L0Qb1LPylOGxdL790itD_GjnazO6t92oXaa4v6eKp9jbITL1nLLFguRQsX_59mhFFKT7NbOPf-iFpskDUVqM_i8_PVEE-iDYHHGZ1Ijig9AHyLoC8ZpOYIlQzTg00k61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نیرو دریای ایران
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22525" target="_blank">📅 01:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش هایی ااز پمپ بنزین پاسداران و پیروزی هم دارم ، ایست شدید و چک کردن گوشی ها هم انجام میشه کاربری گفت گوشی دوستشو چک کردن و گرفتنش
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/22524" target="_blank">📅 00:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بوشهر صدای تیز اندازی گزارش شده
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/22523" target="_blank">📅 00:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش ارسالی تایید نشده : پمپ بنزین شهر ری‌در همین لحظه به آتش کشیده شد
@WarRoom
🚨
🚨
🚨
در انتظار تایید و فیلم ها هستم</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/22522" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AldweYsBb19xSapUBks9zW8Leubxpppqm0sCfY0r2dMg38ttZcyND51GEDJIbuxXjn0BMQMxaDzme07CsF8iswI_4JwQCSsLDRomRiZ3L5Zx1mrF6VIz4TXX04uFB85xGo7pFKqG2wN11awAgyvpD33t5zO3_elRV6VAuC7nAdK8_4C6flLAQu4j_bv9BYfIL0JOekRHneoj5CGHWGspQF7ZgZUAXOWc7fZIz5outeFz77hQDfTfF-2VyE0fwxxodLf6E1fkgsgFn8BNGFThZLnIIDiBfqF962ry_ZnSID_U2FWNip9TF_HiNenzNFckOfX4T5mZpNvkG-pqTNZoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای جنگ الکترونیک و تهاجمی ایی‌ای-۱۸جی در جریان عملیات پرواز شبانه، از عرشه پرواز ناو هواپیمابر جورج اچ. دبلیو. بوش به پرواز درمی‌آید؛ این ناو در حمایت از اجرای محاصره آمریکا علیه ایران در دریای مکران فعالیت می‌کند. تا امشب، نیروهای فرماندهی مرکزی آمریکا برای اطمینان از اجرای کامل محاصره، مسیر
۹۴ کشتی
تجاری را تغییر داده‌اند، ۳ کشتی را از کار انداخته‌اند و ۲ کشتی را با سوار شدن نیروها بازرسی کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/22521" target="_blank">📅 00:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نرخ سوم بنزین, از همین لحظه ۱۰،۰۰۰ تومان شد
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22520" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کپلر: تردد کشتی‌ها در تنگه هرمز هفته گذشته ۲۸ درصد کاهش یافت و به ۷۷ فروند رسید
بر اساس داده‌های شرکت کپلر، که در زمینه اطلاعات، داده‌ها و تحلیل‌های مربوط به کالاها و کشتیرانی فعالیت می‌کند، تردد کشتی‌ها در تنگه هرمز هفته گذشته ۲۸ درصد کاهش یافت و به ۷۷ فروند رسید
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/22519" target="_blank">📅 23:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxXaQ-C7AT1JZh2y5vx7AwH1rUefgOfjOrbweBtmf9SnJfyQQXAitCqicbHzUAMtSpU5ByUNuecR-701U89Q78xa28XRzb3SWpk3HpU-OHyb9AaKRdSuDTWKZdvYxqiFIeuGCqACydwFGWAXeAmRAwv3hl5xMYXsv6rNo2up08bKvu6iMa_O-nKZc9hnMYH4Jz8QJR-CJxDHkyADcouIpRA83apyarU4bNQtEEPKvFh3WDnp8Qdo6PUVgKuIQYE03ON0c_CrDRD_FmtMwQPJfKavR3O-y9qlDjeT_w5u6BL8CYD9Kx-zU1m-gBKxugNiFvxMJEOzEydTR_eyg1lVyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : چند پرتاب از سیریک به تنگه و صدای انفجار از تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/22518" target="_blank">📅 22:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71f020c05.mp4?token=r6Lxg1EFwrxK4C4lL0VhJnUMlF_zZIpFb5VdrXIX0qUrH5E25j9Iqk-yUoyeUyrDoDtY5ymKgiYqyOlo6k6g77G5HP08OIaKXejifOq3VGKBv5rEuSZUWBCQlbTwP-BCWf7sFEFa-I8eygVOMhm0Oex7-ZiZtKSEHfayQqFSQsDhwTGunthHwaCHhljXwVOz23WAZxsXcMsE6aKePFnOSr4gZwsiadT_2iGZouNrX0VNt6-stZxbrPjv15MxNr6wkDRQktFLR1ulenzsAIp-WDENaaayU3aGysh_O0jxONIvRasaG-OJ9iIVbKkxV2dlDUNR-5Zj1JeYRihHASy7tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71f020c05.mp4?token=r6Lxg1EFwrxK4C4lL0VhJnUMlF_zZIpFb5VdrXIX0qUrH5E25j9Iqk-yUoyeUyrDoDtY5ymKgiYqyOlo6k6g77G5HP08OIaKXejifOq3VGKBv5rEuSZUWBCQlbTwP-BCWf7sFEFa-I8eygVOMhm0Oex7-ZiZtKSEHfayQqFSQsDhwTGunthHwaCHhljXwVOz23WAZxsXcMsE6aKePFnOSr4gZwsiadT_2iGZouNrX0VNt6-stZxbrPjv15MxNr6wkDRQktFLR1ulenzsAIp-WDENaaayU3aGysh_O0jxONIvRasaG-OJ9iIVbKkxV2dlDUNR-5Zj1JeYRihHASy7tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : سلام یاشار این اوضاع امشب قشم یه ماشین بزرگ سیاه هم جلو بود پر آدم
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22517" target="_blank">📅 21:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSina</strong></div>
<div class="tg-text">یاشار خوبی داداش
داداش تهران به شدت جو امنیتی شده من رفتم بنزین بزنم غروبی تو تمام خیابون ها داره موتوری‌های یگان ویژه میچرخه،سره میدان ها یگان ویژه وایسادع حتی جلو پمپ بنزین ها
رفیقمم از پاساژ علاالدین گفت که خواستیم اعتصاب کنیم اطلاعات اومد نزاشت.
داداش تهران منتظره یه جرقه‌است</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22516" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid</strong></div>
<div class="tg-text">یاشار جان من رفیقم تو اگاهیه
میگه امشب اماده باشن
ک ی موقع مردم نریزن ببرون
😅
😅</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22515" target="_blank">📅 21:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش ۲ پرتاب از سیریک ۹:۲۰ دقیقه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22514" target="_blank">📅 21:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22513">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، با انتقاد شدید از اقدامات اسرائیل گفت که دروغ‌ها و خرابکاری‌های این کشور باعث شکست تفاهم‌نامه اسلام‌آباد میان ایران و آمریکا شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22513" target="_blank">📅 21:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">روزنامه تلگراف انگلیس: رئیس جمهوری سابق ایران ( روحانی) خواهان برگزاری رفراندوم برای پایان جنگ شد
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22512" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر در گفت‌وگو با CNN گفت
اولویت قطر بازگشایی تنگه هرمز، کاهش فشار اقتصادی و جلوگیری از تشدید درگیری‌هاست.
او تأکید کرد قطر به دنبال
راه‌حلی پایدار و گفت‌وگویی فراگیر میان کشورهای منطقه
است و معتقد است تحریم‌ها تاکنون نتیجه مطلوبی نداشته‌اند. همچنین قطر چند طرح، از جمله
یادداشت تفاهم
، برای رسیدن به توافق ارائه کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22511" target="_blank">📅 20:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22510">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ErQrDseLoHbRORTC2L2cbKsDq-feTAsL_h6iOwSXgXBQfGKGaIUzAj6y_exnrAtwKLvcWhnIzOe0LIgSF-VW-qHpiJJ69dx8vv8CbIlaUAebmhzk8km8D4Zy5_Ee3wT-ErqZctgqRsQhdJ2-RJCqf_TJY9coyxMrDb429kIeWr21ACdxgaKB3820YMLs9EUge7RQR2IEsWrNQBhiO-2hzwUUO4rvmCbGNGNUFHrxdj1cMm2rp1w7JtHDKqQ_rp07JoERcHpJQCU6u4qr8E6DAyHbHAH9lsnOi4E3VPxO5e2h99wzzoilPjGyaFl14yXXxLXs6Vy9VdYpssfmnOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث، گزارشی از
وال‌استریت ژورنال
را با این مضمون منتشر کرد:
مسعود پزشکیان و محمدباقر قالیباف
بر ضرورت
پایان دادن به جنگ و مذاکره برای خروج از آن
تأکید کرده‌اند و خواستار تقویت اقتصاد ایران در شرایط فعلی شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22510" target="_blank">📅 19:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ : در انتخابات میان دوره ای به پیروزی قاطع دست خواهیم یافت و آمریکا را نجات خواهیم داد‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22509" target="_blank">📅 18:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688ebf7bb6.mp4?token=H98td4kXQUGFq1ZN-L4bnDSeba_ojSHMptk8NM2gHZpy8ImoawuhBul9eBF8w_NL-_xjVUj3qY26LEPYZ_Zafn9AAvRthh8IxeyTAZ_KI8XA4zmJRlAc-FV9dHLtgxFp0f-4fpWR_w9pxm0JRbGHYHfSzDAz2u0uS0_tgcaJttTrZTR484skwHWTHE5QX9DkfqhqQjlqR_iD194_MupUaoyw8qyk1uE3jsr3EuOq2PSPkOJqiElpyc6LHU0slWmtFbu-9XJWzLsl-GEUDR4tMwyYGPFTn8fu9zLSEB_PcSYYSiC93uY-YoGneHflVFEElRKn9-ImIw8cXSjaFgNxkCY6WA-Gywdmc_AKOqBKwOKD4EulACg7glvuKB6UTrWvKep7HyTXwZbQOHF7KSxj_BHQnS_ikVrRwtE5diZi82B3uoHBALrkB5V5EqWx_IfjDRAvRw6Djj7y-kpKl9ichiH8_gG1sYQku5HFkeXBay7ewRvKJWc4hzrh-xePQs9T3ooh8l_xK-UERUVmX6f_b_ZpjaLl5ERnYW3dwlIPQ3Yhuxk0E4wl4woZ3Ci2Kd8Ym3KYsaZ7hhzbTUYetNtBn-jPeDeh-PTNyafgEIwG-ybn9ZKZItZCo5l3HdM3oVvm_OB8dFUoa0tBPs5zqDi_EXonjmes5m84nLty4wRFEf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688ebf7bb6.mp4?token=H98td4kXQUGFq1ZN-L4bnDSeba_ojSHMptk8NM2gHZpy8ImoawuhBul9eBF8w_NL-_xjVUj3qY26LEPYZ_Zafn9AAvRthh8IxeyTAZ_KI8XA4zmJRlAc-FV9dHLtgxFp0f-4fpWR_w9pxm0JRbGHYHfSzDAz2u0uS0_tgcaJttTrZTR484skwHWTHE5QX9DkfqhqQjlqR_iD194_MupUaoyw8qyk1uE3jsr3EuOq2PSPkOJqiElpyc6LHU0slWmtFbu-9XJWzLsl-GEUDR4tMwyYGPFTn8fu9zLSEB_PcSYYSiC93uY-YoGneHflVFEElRKn9-ImIw8cXSjaFgNxkCY6WA-Gywdmc_AKOqBKwOKD4EulACg7glvuKB6UTrWvKep7HyTXwZbQOHF7KSxj_BHQnS_ikVrRwtE5diZi82B3uoHBALrkB5V5EqWx_IfjDRAvRw6Djj7y-kpKl9ichiH8_gG1sYQku5HFkeXBay7ewRvKJWc4hzrh-xePQs9T3ooh8l_xK-UERUVmX6f_b_ZpjaLl5ERnYW3dwlIPQ3Yhuxk0E4wl4woZ3Ci2Kd8Ym3KYsaZ7hhzbTUYetNtBn-jPeDeh-PTNyafgEIwG-ybn9ZKZItZCo5l3HdM3oVvm_OB8dFUoa0tBPs5zqDi_EXonjmes5m84nLty4wRFEf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تفنگداران دریایی و ملوانان ناو آبراهام لینکلن، مشغول عشق و حال در کلابهای  پاتایا، تایلند. @WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22508" target="_blank">📅 18:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ در تروث ویدیو برنامه مارک لوین را بازنشر کرد: در این گفت‌وگو، ویکتور دیویس هنسون ترامپ را «معکوس‌کننده‌ی انقلاب» می‌نامد؛ یعنی رئیس‌جمهوری که قصد دارد روندی را که طی۵۰سال آمریکا و سیاست خارجی آن را تغییر داده، معکوس کند. در مورد ایران نیز تأکید می‌شود…</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22507" target="_blank">📅 18:17 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
