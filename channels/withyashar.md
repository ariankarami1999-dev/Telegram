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
<img src="https://cdn4.telesco.pe/file/p-hI0ly1lm7c1VTKhaMth0gzLXHUlV2A-BH9E1cVMZJK35nMFBEVenufJqyVytgmMiKiMhSZw-8PipeW0OL4AsvSVTv4DKHUa4RDSIxQCltaRSvTzgS_mK-Y_kttN_AMOMJgVfwjnaLvbwxmhK7t1rDAj2_jZRvwg05tfLR6AyFWyXuz17WZhZo_F_84oiu7uPfagKdlVb0YlG3Ot02ftgh_xjncFzG_IMKxnVuggt2plHyAvbNfbzX9HElO_Cmu7UKR-tRxw6i4kf0iuOQn1DKAVvChCu1ER4wvWlxjZQvUhQruY2DltzEUVWSErjShU8GgIe0tNHUhTPsuuDBAbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 397K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 23:31:29</div>
<hr>

<div class="tg-post" id="msg-18464">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بوشهررررر سنگین
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/withyashar/18464" target="_blank">📅 23:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18463">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قشم روستای مسن رو زذن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/withyashar/18463" target="_blank">📅 23:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18462">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">همدان ، احتمالا نوژه رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/withyashar/18462" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18461">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فرودگاه ایرانشهر رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/withyashar/18461" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18460">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روابط عمومی دانشگاه علوم پزشکی هرمزگان:
در پی حمله دقایقی پیش به محله تپه الله‌اکبر شهر بندرعباس، تاکنون ۷ نفر از هموطنان مجروح شده‌اند.
بلافاصله پس از وقوع حادثه، تمامی نیروهای امدادی و درمانی دانشگاه علوم پزشکی هرمزگان در حالت آماده‌باش کامل قرار گرفته‌اند و اقدامات درمانی لازم برای رسیدگی به مصدومان در حال انجام است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/18460" target="_blank">📅 23:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18459">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سخنگوی سنتکام: ما در پاکسازی مین‌هایی که سپاه پاسداران در هرمز کار گذاشته است، به پیشرفت‌هایی دست یافته‌ایم و ادامه میدهیم
@WarRoom</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/18459" target="_blank">📅 23:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18458">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تسنیم: دقایقی پیش تپه الله اکبر بندرعباس مجددا مورد حمله دشمن قرار گرفت.
حجم این اتفاق به حدی بود که برق این منطقه در بندرعباس در حال حاضر قطع شده است، هدف مورد اصابت در این حمله یک دکل مخابراتی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/18458" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18457">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سلام یاشار پایگاه هوایی بندرو رگباری داره میزنه الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/18457" target="_blank">📅 23:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18456">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قشممممم بد زددد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/18456" target="_blank">📅 23:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18455">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دارن گرم میکنین ۱ ساعت دیگه میان شهر های عمیقتر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/18455" target="_blank">📅 23:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18454">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجار قشم
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/18454" target="_blank">📅 23:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18453">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بندر عباس میگن عباس هم رفت فقط خود بندر مونده
@WarRoom</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/18453" target="_blank">📅 22:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18452">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اهواز باز زد سه باررررررره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/18452" target="_blank">📅 22:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18451">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/18451" target="_blank">📅 22:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18450">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش انفجار در جم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/18450" target="_blank">📅 22:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18449">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/18449" target="_blank">📅 22:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18448">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کبودراهنگ همدانو کوبیدن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/18448" target="_blank">📅 22:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18447">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9358a92cf5.mp4?token=I7n-CT_iOvbwx6JmjPP6u0CXMiNZVP8fJl8-x-iSNgW4Ji6hwyJo1LY52jZwgiOShrRpG0kMz80RZsC9PSgTmuTew50GBHcKuWxni1jveX7gPUB2fQdAHsQZKE_8Nd4FgqxO5lVJVwYSYQ-0bGnJ3uNcyhFrSeP32S07Q1mDPlklynKZwp9tny74A6FcBMHgh41mChBLH22QgZuQp2Td1w-LQlDiuFYAg4ofKZnfXhy9gzlEo-srtjfCpuX76Vd9mwHImo78APGEJTqK659utv63copRzwIz9jHL_pSgGPbDA7jnR4L1iIIJ5RDt5sOBsdHjWU2ZYgqp0x7Df4Oq-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9358a92cf5.mp4?token=I7n-CT_iOvbwx6JmjPP6u0CXMiNZVP8fJl8-x-iSNgW4Ji6hwyJo1LY52jZwgiOShrRpG0kMz80RZsC9PSgTmuTew50GBHcKuWxni1jveX7gPUB2fQdAHsQZKE_8Nd4FgqxO5lVJVwYSYQ-0bGnJ3uNcyhFrSeP32S07Q1mDPlklynKZwp9tny74A6FcBMHgh41mChBLH22QgZuQp2Td1w-LQlDiuFYAg4ofKZnfXhy9gzlEo-srtjfCpuX76Vd9mwHImo78APGEJTqK659utv63copRzwIz9jHL_pSgGPbDA7jnR4L1iIIJ5RDt5sOBsdHjWU2ZYgqp0x7Df4Oq-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله موشکی آمریکا از کویت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/18447" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18446">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجار در قشم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/18446" target="_blank">📅 22:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18445">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار دوباره بندر عباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/18445" target="_blank">📅 22:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18444">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار جزیره لارک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/18444" target="_blank">📅 22:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18443">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اهواز ۷-۸ انفجار در مجموع
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/18443" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18442">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اهواز رو بازم زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/18442" target="_blank">📅 22:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18441">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بهبهان رو زدن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/18441" target="_blank">📅 22:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18440">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجار سنگین اهواز
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/18440" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18439">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0125430a.mp4?token=TQqLxGIgmVsob4CIV3qLC5iab6hjkTJSixBfxMQ3sOJBfD98tg0Q3JJwXdWZKIG7EIKY8iXVQNCAk6xVI9c_ksEyTv67zGeQwdbMQKLHiZdhihsk5GLT3LaNl4fai0yCVtyyqOfYPoTT8xuwxlJa1gE_84hqbst_aAav5JjFBLjAhDckzSIgNKpHgOMXMJoOwUZMvS5szQ9J2SJvxEYnrTUbMG3I8wgL-OpfIxRfA3Lt8xxO6jjdOyKvbtoMx0w74OOKHWym7IP4td8t5cypCZgM1H2NUKkP1O6Oh3RBFXzruzvAZxgN3Wm49_RcPhjy6ARoUaaMwp7liKnBuOo6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0125430a.mp4?token=TQqLxGIgmVsob4CIV3qLC5iab6hjkTJSixBfxMQ3sOJBfD98tg0Q3JJwXdWZKIG7EIKY8iXVQNCAk6xVI9c_ksEyTv67zGeQwdbMQKLHiZdhihsk5GLT3LaNl4fai0yCVtyyqOfYPoTT8xuwxlJa1gE_84hqbst_aAav5JjFBLjAhDckzSIgNKpHgOMXMJoOwUZMvS5szQ9J2SJvxEYnrTUbMG3I8wgL-OpfIxRfA3Lt8xxO6jjdOyKvbtoMx0w74OOKHWym7IP4td8t5cypCZgM1H2NUKkP1O6Oh3RBFXzruzvAZxgN3Wm49_RcPhjy6ARoUaaMwp7liKnBuOo6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از بندرعباس؛ مجدد همون دکل رو با 4 تا موشک زد
اینبار واقعا شدید بود
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/18439" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18438">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رسانه های سعودی : شنیده شدن صداهای انفجارهایی در بندرعباس، بوشهر، چابهار و کنارک
@WarRoom
.
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/18438" target="_blank">📅 22:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18437">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش انفجار‌ در کیش
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/18437" target="_blank">📅 22:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18436">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e346db66bb.mp4?token=Z8Yd_mObpHbtC7yChfT3TgpLhbkxsZr_se8ptr8gXIYZLPeDCQvw_9-pkunN62nfZ0LBY7aIRCVQEayRacs8DqLL7YLIxNDsh6QrAdZH5VZA09hUi_ljJqInRYKRJInb6G0U_vnRfwBiYxaePSCd_d2CaDgPH-sgPDitDnrTw-VNdq2fI_OdqOW8hOunpVeRTAY2ncXQ5FB-94DDm9WlWa5wRoHYsGdiii-WcLzWeVHVH-8ot3rXZUfeCi96F0eKoMczMEha4MQsbigQsT0Jj1YHg83rfPWDouvD3lvFqizy3keoeGH-tGlHub0oIxDN6fCQ19MH_e83sPL18VBwIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e346db66bb.mp4?token=Z8Yd_mObpHbtC7yChfT3TgpLhbkxsZr_se8ptr8gXIYZLPeDCQvw_9-pkunN62nfZ0LBY7aIRCVQEayRacs8DqLL7YLIxNDsh6QrAdZH5VZA09hUi_ljJqInRYKRJInb6G0U_vnRfwBiYxaePSCd_d2CaDgPH-sgPDitDnrTw-VNdq2fI_OdqOW8hOunpVeRTAY2ncXQ5FB-94DDm9WlWa5wRoHYsGdiii-WcLzWeVHVH-8ot3rXZUfeCi96F0eKoMczMEha4MQsbigQsT0Jj1YHg83rfPWDouvD3lvFqizy3keoeGH-tGlHub0oIxDN6fCQ19MH_e83sPL18VBwIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس هم اکنون
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/18436" target="_blank">📅 22:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18435">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هم اکنون دوباره سمت ایستگاه رادیویی پیامبراعظم بندر عباس @WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/18435" target="_blank">📅 22:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18434">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=Ans5omMdf9ayrMQlOrzQCFyFQIH2G4JRV_EbObEC8-KpgKu3jWD2Ut92N60tUAtM83eVliOD_b7JiU9jUWKNXQTK3Yj0b5hdy7SBbCroXk9PJRjW9Rr1O_q69_rViIHgXmIxKwPItiKh7afmDqeIdCLnSovkm2qAVpzN8QwdnHab-dxxbsu0wVgJ2KdNiqc7l-AhUHadAo3SOh24tb_yGky1Mq-Nbse9SRZZCZETz5Only3X8ko5B4s-jbNzlTsTrEaK6ah_Mzs1B_dgfxe2ejh7rlYi_skhcaJKpKEfQKGtjBGlGoAQbu7KTS8CRshrSGUXSXY5N5LoamsdQiJscg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=Ans5omMdf9ayrMQlOrzQCFyFQIH2G4JRV_EbObEC8-KpgKu3jWD2Ut92N60tUAtM83eVliOD_b7JiU9jUWKNXQTK3Yj0b5hdy7SBbCroXk9PJRjW9Rr1O_q69_rViIHgXmIxKwPItiKh7afmDqeIdCLnSovkm2qAVpzN8QwdnHab-dxxbsu0wVgJ2KdNiqc7l-AhUHadAo3SOh24tb_yGky1Mq-Nbse9SRZZCZETz5Only3X8ko5B4s-jbNzlTsTrEaK6ah_Mzs1B_dgfxe2ejh7rlYi_skhcaJKpKEfQKGtjBGlGoAQbu7KTS8CRshrSGUXSXY5N5LoamsdQiJscg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/18434" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18433">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجار چابهار
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/18433" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18432">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بندرعباس چپ و راست آمبولانس و آتشینشان میره سمت شرق بندرعباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/18432" target="_blank">📅 22:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18431">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">غروبه هرمز @WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/18431" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18430">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سنتکام : در ساعت
۲:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
امروز
(۲۱:۳۰ به وقت تهران)
، نیروهای ایالات متحده
موج جدیدی از حملات
علیه ایران را آغاز کردند.
این حملات برای
پنجمین شب متوالی
با هدف
تضعیف بیشتر توانمندی‌های نظامی ایران
در حال انجام است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/18430" target="_blank">📅 22:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18429">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش انفجار بوشهر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/18429" target="_blank">📅 22:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18428">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">لطفاً تا فردا صبح هیچگونه سؤال سیاسی اجتماعی و تحلیلی نپرسید. لطفاً در مورد اینترنت خبریی ندهید. لطفاً صدای جنگنده ها را نگید. لطفاً فقط گزارش صدای انفجار رو بدید و تصاویر و عکس. همچنین پیامها را فقط همیشه در یک متن بفرستید، نه ده پیام جداگانه.</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/18428" target="_blank">📅 22:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18427">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vff7fqWUCnMZ6Uy04y7_PHhN7DwDWqG2n98emQz-jINEel7OdapTCcWqeo8_HQAEYoQwHtIrcl9KxtCx6iqEuWk06OyiTJCZOxX1HHHfmcDRVHvMWiyeCRq0-T5JpzzhKDGdw26I9SP5j_hzIZAf4rVxYZYVWlMmxaHQJrd5M4UNsHP2V0aylhj2Ku98B9_YjIDY2Nu_AzP1bJ6oMecR_s4JnhL3thIdFgZbZa2zXUnuPKctBihALg5U8xpn5BRWfUptzHROHYvloeTTzw7gtau7YK9NNqbVU3cDRgY53IpriqUpJ0kwOXZkr8NHXgHX7wIerL3IxWi65nwa2AyNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دوباره سمت ایستگاه رادیویی پیامبراعظم بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/18427" target="_blank">📅 21:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18426">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/18426" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18425">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ادعای ترامپ مبنی بر آزادی یک زندانی آمریکایی از ایران تکذیب شد
ترامپ در حالی این ادعا را مطرح کرده است که با توجه به بررسی‌های صورت گرفته هیچ زندانی محکوم و یا جاسوس آمریکایی با مشخصاتی که ترامپ اعلام کرده و یا با هر مشخصات دیگری از زندان‌های ایران آزاد و یا تبادل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/18425" target="_blank">📅 21:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18424">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بندر ادامه دارههههه ۵-۶ تا شد</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/18424" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18423">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ولی باید ببینیم امشب به اصفهان میرسه یا نه الان مرکز هدف اصفهانه کوه کلنگ</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/18423" target="_blank">📅 21:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18422">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجار همدان
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/18422" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18421">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تهران رو شاید بزنند ولی‌ نه به حالت زارتان زورتان به همون پارچین اینا بزنند فککنم</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/18421" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18420">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۲ بار قشمممممم
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/18420" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قشم رو زدنننننن
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/18419" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18418">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بندر عباس زارتان زورتانهههههه
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/18418" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18417">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت منطقه (۴ سوخترسان جدید بلند شد ، تحرکات زیاد در منطقه
🚨
🚨
🚨
🚨
) @WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/18417" target="_blank">📅 21:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18416">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
حملات امشب شروع شد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/18416" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18415">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شروع انفجارات بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/18415" target="_blank">📅 21:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18414">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae627587b9.mp4?token=iLCeomC25M2qcPzyRzJof_XcoeG7oyeMmXO0nGqKNW4vc-2GhiUQhhiiL_54j8YCrcGe7QclVD-L2gQwE7In-msNcj7tRaNm3ApoWGcoHtqjhaLmXRuME6MA0WPuakielaSF5sOZgNCDqq3N5rvyt2CVdrRaH8wuM_BgywCPOOwN9o4NOZb6i1XyrW9NTP9tXH8Gyvua6k3zKZwfO5kFxCYu9nN8jS3SHEf4ahUr4qeClKttf3tFb_gsGWZWIIYDQoghPkFC0ZcSbj9T1ERIHqjo42VyUT0ZIrulIeMCmqJbmDSYFGMabLLBwWHVPDMvSFbdIOXklYromW24d4w_mLQQWyuxSuQP359P3CChZTSotX2_tTUkkBEh5aWs-Xe94yRh2f1k-oEhT8WG_8ddEdCvFAKW7j4g1o__0hLAGQNIiPkrK7OkLyIZSsy_5I7eMR225lRUGGMDiUsP-XqJ2UlHKh99ZlBaXut5o1sw2JWcHCOk3tEUHkwj8gz4WzndHmKe2O53urfNFS9c22qXNhlQpSjr52ceCu_hJENbVySlTMnoNinhIhL61o0UmdUXMHwDmg_ay56Cqbp-1qziM7BpqIUzam99nd5Tl6Ms1Jf-6eQZzL4qPJGBdUNrBRbDwtTSDW7-gsP67LhuFIlmR7Yi_-KncWbpp09Kt0DHNH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae627587b9.mp4?token=iLCeomC25M2qcPzyRzJof_XcoeG7oyeMmXO0nGqKNW4vc-2GhiUQhhiiL_54j8YCrcGe7QclVD-L2gQwE7In-msNcj7tRaNm3ApoWGcoHtqjhaLmXRuME6MA0WPuakielaSF5sOZgNCDqq3N5rvyt2CVdrRaH8wuM_BgywCPOOwN9o4NOZb6i1XyrW9NTP9tXH8Gyvua6k3zKZwfO5kFxCYu9nN8jS3SHEf4ahUr4qeClKttf3tFb_gsGWZWIIYDQoghPkFC0ZcSbj9T1ERIHqjo42VyUT0ZIrulIeMCmqJbmDSYFGMabLLBwWHVPDMvSFbdIOXklYromW24d4w_mLQQWyuxSuQP359P3CChZTSotX2_tTUkkBEh5aWs-Xe94yRh2f1k-oEhT8WG_8ddEdCvFAKW7j4g1o__0hLAGQNIiPkrK7OkLyIZSsy_5I7eMR225lRUGGMDiUsP-XqJ2UlHKh99ZlBaXut5o1sw2JWcHCOk3tEUHkwj8gz4WzndHmKe2O53urfNFS9c22qXNhlQpSjr52ceCu_hJENbVySlTMnoNinhIhL61o0UmdUXMHwDmg_ay56Cqbp-1qziM7BpqIUzam99nd5Tl6Ms1Jf-6eQZzL4qPJGBdUNrBRbDwtTSDW7-gsP67LhuFIlmR7Yi_-KncWbpp09Kt0DHNH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تناقضات میان ادعاهای ونس و ترامپ نشان‌دهنده این است که در یک جبهه هستند
خبرنگار:
درباره ایران: رئیس جمهور ترامپ اخیراً گفته است: «از نظر من، سروکله زدن با آنها فقط اتلاف وقت است. آنها دروغگو هستند. یک جای کارشان می‌لنگد. آنها عوضی هستند. آنها آشغال، بیمار، شرور و خشن هستند.»
سپس ونس، معاون رئیس جمهور، دیشب به جو روگان گفت: «من از آمریکایی‌ها - و صادقانه بگویم از مردم کشورهای دیگر - که می‌گویند نمی‌توانید با ایرانی‌ها مذاکره کنید، بسیار ناامید شده‌ام.»
خب، پاسخ شما به این تناقضات چیست؟ فکر می‌کنم با توجه به پیام‌های متناقض، می‌توانید درک کنید که این موضوع چقدر برای آمریکایی‌ها گیج‌کننده است.
کارولین لیویت:
رئیس جمهور و معاون رئیس جمهور دقیقاً در یک جبهه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/18414" target="_blank">📅 21:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/18413" target="_blank">📅 21:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18412">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427068d887.mp4?token=J2S7HITiRuaMZHvef2USbKjPKlniSUJ8sXSCXgW8N_UYvl_K_FstXCx-iXe8CCrBgz8GyIb0C7dfdRoGD6F87PabNEHOqil80WaDKzR-QWa0sKpCDs46yjQWoUfW1yCUMMNZB4Ux1yp6TsGVhEWAWtVRy50NLLY08Tk-k54RhfyvJPd3-jvga8fGeCXCpLz4yy5odLySyVSxjtp_fYof1J59FiuMymHgKgJ7ZGLL8YfcYthEKhAeWQ4zh9c1dBbanMfiOeHpsjnR0uGeHCL1OqhFTYus3Hxq4vj_aHFxHi-vDxYryPIHz_f25wgi-NS64Dw-5elazxgNkg54eMJim7qcCVGCu7lz09zjj08Y44Dh8b7jKzKCi-E2rOxxStPZEpp8np50XJ9CL0K2m2jslYG6dABmkPvad6PBEc11UF3kjqJjrOj687d-BxPBEQxDCxJFDY1lcqWr8tAxv10NsIS4TCLQuqpyAlr5NiGSe8WrbjJ3Y386YZed_9wHstgLdVki_aOLqqGR5tfpj7LBlcJD4tpO8BEsWJjsdYQXcuvYr-euy7fL37PjzhhIMGs-RxNBpa5zliKZ-GIqLdaEwp5dqdvg4OyA4ETU83WwRmwrwJlG78b4UWgR9tbNc4ZTa_l62xOQ-uC-XqxQCfV9s8enRxNGy4KDV2mCrXIvgvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427068d887.mp4?token=J2S7HITiRuaMZHvef2USbKjPKlniSUJ8sXSCXgW8N_UYvl_K_FstXCx-iXe8CCrBgz8GyIb0C7dfdRoGD6F87PabNEHOqil80WaDKzR-QWa0sKpCDs46yjQWoUfW1yCUMMNZB4Ux1yp6TsGVhEWAWtVRy50NLLY08Tk-k54RhfyvJPd3-jvga8fGeCXCpLz4yy5odLySyVSxjtp_fYof1J59FiuMymHgKgJ7ZGLL8YfcYthEKhAeWQ4zh9c1dBbanMfiOeHpsjnR0uGeHCL1OqhFTYus3Hxq4vj_aHFxHi-vDxYryPIHz_f25wgi-NS64Dw-5elazxgNkg54eMJim7qcCVGCu7lz09zjj08Y44Dh8b7jKzKCi-E2rOxxStPZEpp8np50XJ9CL0K2m2jslYG6dABmkPvad6PBEc11UF3kjqJjrOj687d-BxPBEQxDCxJFDY1lcqWr8tAxv10NsIS4TCLQuqpyAlr5NiGSe8WrbjJ3Y386YZed_9wHstgLdVki_aOLqqGR5tfpj7LBlcJD4tpO8BEsWJjsdYQXcuvYr-euy7fL37PjzhhIMGs-RxNBpa5zliKZ-GIqLdaEwp5dqdvg4OyA4ETU83WwRmwrwJlG78b4UWgR9tbNc4ZTa_l62xOQ-uC-XqxQCfV9s8enRxNGy4KDV2mCrXIvgvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت منطقه (۴ سوخترسان جدید بلند شد ، تحرکات زیاد در منطقه
🚨
🚨
🚨
🚨
)
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18412" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18411">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۵ اسرائیلی: ایالات متحده در حال آماده‌سازی برای گسترش حملات خود علیه ایران از نظر دامنه و تعداد است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18411" target="_blank">📅 20:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18410">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGq6hpcIV9-Qt4BWtmnDDs40F9_LKhjsehha3obVvnMokQgDygUaPY_BXoQRM0mDis69PEBF8rL4b2dpunJ2h95XViDXtIU6Y7eiZD4ZyvBO2jkuWjyngGsvGQyWHtRy46rXYlBtas_mJPYX9Zpk_iRnPmcrH0LE96K00kd7d3BT88guCQ4QE006YzVwiirniahYmK_18uZHgDy9uJaipKoQtRp93WHwCistUEQ0idk6CF_ZzNhqibdF11ZxTLDMDyaGoC5No2A-m-sc1N8NLV8WRuDeuuFqvnJ6zoXeqX0Sp3TI1GCU9xyG7xRUodvFX6PgQpqnA_uTJb_1DcTbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : فرمانده اطلاعات نظامی حماس در تیپ خان یونس را با انفجار خودرو در جنوب غزه به هلاکت رساندیم
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18410" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18409">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اتوبوس …. ببوس
😂</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18409" target="_blank">📅 20:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18408">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رویترز:حمله بزرگ علیه ایران نزدیک است
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18408" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18407">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18407" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18406">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رویترز رو تبر‌ زدن خبر دبی فیکه
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/18406" target="_blank">📅 20:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18405">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اتاق جنگ با یاشار : میزو بچینم برای امشب</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18405" target="_blank">📅 20:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18404">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبرگزاری فارس:حملات هوایی دقایقی پیش چندین نقطه در اطراف بندر عباس را هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18404" target="_blank">📅 19:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18403">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شاهزاده
رضا پهلوی:
سرکرده‌های رژیم آخوندها در تهران و پناهگاه‌های امن پنهان شده‌اند، اما سربازان وظیفه را در پادگان‌های آسیب‌پذیر رها کرده‌اند. او با بیان اینکه حکومت جان نیروهای نیابتی خود را بر جان ایرانیان ترجیح می‌دهد، از سربازان خواست جانشان را برای این نظام به خطر نیندازند و از خانواده‌ها نیز خواست تا حد امکان مانع اعزام فرزندانشان به خدمت سربازی در شرایط کنونی شوند. شاهزادت همچنین از اقدام مردم زاهدان و مناطق اطراف در کمک‌رسانی و اهدای خون قدردانی کرد و تأکید کرد جوانان ایران نباید قربانی بقای رژیم شوند، زیرا آینده کشور به این نسل نیاز دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18403" target="_blank">📅 19:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18402">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حسن روحانی : قبل از آخرین جلسه ای که قرار بود تمام مسولین نظام خدمت رهبر برسند (رمضان ۱۴۰۴) احساس خطر کردم و پس از تلاش های فراوان و فرستادن پیغام های مختلف برای شخص رهبر و تیم دفتر ایشان، موفق شدم جلسه را لغو کنم
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18402" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18401">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1dea65f9.mp4?token=kjMORbZL7DI0OdorQkHMZFDnppsvqOgO1v6wivBIc30Fi7WrToDEZ6W1RrfRevGXXfS7EPAfwZsL8MlpPcfkO7l2BJtL49GKzCWHMOBc3yJYJbe0KxhebysgStsEwlr9DMNKDBlvMZqdL_F0W692DErJ_0VYg4wWflbEHQ72RBhQu5f2bM_Xvi4Dn5LGwFtPsVg9WDwm1V1iVcUs19JeyROOdb6BeHgDxPCBeaKhg14uCf6s8474Ktgp26H_WkkbvzY_SkJPt1Rr8myfw97rw18nHEbCURUiUT4aylgV8Z0ztu8_xG2zxIk8AYRnSIucEgjGMlwbY8IIhiXK1a1QFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1dea65f9.mp4?token=kjMORbZL7DI0OdorQkHMZFDnppsvqOgO1v6wivBIc30Fi7WrToDEZ6W1RrfRevGXXfS7EPAfwZsL8MlpPcfkO7l2BJtL49GKzCWHMOBc3yJYJbe0KxhebysgStsEwlr9DMNKDBlvMZqdL_F0W692DErJ_0VYg4wWflbEHQ72RBhQu5f2bM_Xvi4Dn5LGwFtPsVg9WDwm1V1iVcUs19JeyROOdb6BeHgDxPCBeaKhg14uCf6s8474Ktgp26H_WkkbvzY_SkJPt1Rr8myfw97rw18nHEbCURUiUT4aylgV8Z0ztu8_xG2zxIk8AYRnSIucEgjGMlwbY8IIhiXK1a1QFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهبهان ، خوزستان
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18401" target="_blank">📅 19:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18400">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صداوسیما: عصر امروز یک پرتابه دشمن به روستای مسن قشم اصابت کرد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18400" target="_blank">📅 19:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18399">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سی ان ان: مطابق گزارش سی‌ان‌ان، ترامپ در مدت کوتاهی پس از خرید سهام شرکت‌ها توسط مدیران سرمایه‌گذاری‌اش، بیش از ۲۰ شرکت را در شبکه اجتماعی "تروث سوشال" مورد تحسین یا تبلیغ قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18399" target="_blank">📅 18:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18398">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">@warroom
جی‌دی ونس</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18398" target="_blank">📅 18:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18397">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir chvaie</strong></div>
<div class="tg-text">نظرت در مورد حرف‌های مفت جی دی ونس</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18397" target="_blank">📅 18:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18395">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">@warroom
تنگه باب المندب</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18395" target="_blank">📅 18:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18394">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK!YΛП</strong></div>
<div class="tg-text">اون هواپیمایی که هرجوری که شده خودشو رسونده به یمن چه چیزی رو حمل می‌کرد؟</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18394" target="_blank">📅 18:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18393">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدای‌ انفجار از قشم/تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18393" target="_blank">📅 18:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18392">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه جولانی به حزب‌الله حمله کنه، پاکستان و عربستان به حوثی ها، آمریکا به ایران و اسرائیل به همهشون، روسیه هم که با اوکراین میجنگه. پس باید به زودی ناقوس جنگ جهانی خاورمیانه رو به صدا دربیاریم. جنگ جهانی ۲.۵
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18392" target="_blank">📅 18:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18391">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داد نیروهای آمریکایی در پیام رادیویی به کشتی‌ها اعلام کرده‌اند «مسیر جنوبی تنگه هرمز باز است». در یکی از ارتباطات، یک ملوان در پاسخ به این پیام با عبارت «گمشو» واکنش نشان داده است.
افسران نیروی دریایی آمریکا هشدار داده‌اند توان موشکی ضدکشتی و پهپادی ایران می‌تواند در صورت تشدید درگیری، تنگه هرمز را به یک «جعبه کشتار» برای نیروهای آمریکایی تبدیل کند. این گزارش تأکید می‌کند ایران همچنان دارای زرادخانه قابل توجهی از موشک‌ها و پهپادهاست که می‌تواند عبور کشتی‌های تجاری و نظامی در این آبراه حیاتی را مختل کند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18391" target="_blank">📅 18:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18390">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال 14 عبری: دستوری برای سیستم امنیتی تصویب شد مبنی بر اینکه حفاظت از نتانیاهو و همسرش در طول زندگی‌شان ادامه یابد، به دلیل نگرانی از احتمال وقوع انتقام‌جویی ایران از طریق ترور او. فرزندان نتانیاهو نیز در 5 سال آینده از محافظت برخوردار خواهند بود.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18390" target="_blank">📅 18:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18389">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رویترز،: یک مقام پاکستانی پس از واکنش یمن به عربستان سعودی گفت :رهبران ارشد ما به ایران اطلاع دادند که حملات به عربستان، حملاتی علیه پاکستان است و عربستان، خط قرمز ما است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18389" target="_blank">📅 18:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18388">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه جولانی به حزب‌الله حمله کنه، پاکستان و عربستان به حوثی ها، آمریکا به ایران و اسرائیل به همهشون، روسیه هم که با اوکراین میجنگه. پس باید به زودی ناقوس جنگ جهانی خاورمیانه رو به صدا دربیاریم. جنگ جهانی ۲.۵
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18388" target="_blank">📅 18:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18387">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رویترز: نیروهای پاکستانی در عربستان در حال آماده‌سازی برای اعزام برای جنگ با حوثی‌ها هستند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18387" target="_blank">📅 18:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18386">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMeli</strong></div>
<div class="tg-text">یاشار من سرکارم تهرانپارس اومدم دیدم عکس شاهزاده رو چسبونده بودن رو دیوارا اینام داشتن تند تند میکندن
🤣</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18386" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18385">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جلیلی : مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام رهبر رو بگیریم.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18385" target="_blank">📅 17:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18384">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54f24594a.mp4?token=Rb8xh-LU3zTQ4m2NT06LfqDLG75Yr_ZygD5SqzuskIej6A1-dI95kQ9tQpTS5gH7bjMLdf1mGHV6dpJN_eyr-GVvVultyldaOsxgEWE_49Dswz4-hUyMmqAzEAJluWb6WeaAiCkotI5hLzfLeyNwg0XSkYw-hmbaMpk4-miec6JMJcqt3WQ3JOheXYXiw1nHDd69217j1m2fdaQWLe1HpK1ShBg1vTiLXihYh8zNe7ezCu-QHfl1RsYGfRAXFL5UbHhKoSc8W9TOhFQIdGelrotGjSfbkGenidN62ayGnQ4QOnCiqc02ahaqm7X_DX__7ovZBzCdJLdEFO44f048qheoTN2tpB83fWSq4d030u35zoZDKkVdzVGShBhfIT-i-71AC69dbYTslqafSh-70GA2eYaWrAlrHH8NewV3rhG5Dc7gRdSbjh3BOz26p47fecdg9Px0hnuDPSvMSx-3M8GDO12D3sutzNzOJtxe7-mcSGiPjJNJuIgxxLfDkF_5tqW_VI6LxuvID64BMcCqrNVpKWtmXVXA6Hpxb2V8dB4a3O7JNJ_BlPkrLut6EWaI_Castk3tCxe1aKsHnB-UEhQctScyzwAytodzeFg0HUvHU9hwjaRI3r6TnZMSWKX2X3Q3KjQNlG0ZoCLbDmXNyQ-7kbm6qi_w9YKuHXJFR6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54f24594a.mp4?token=Rb8xh-LU3zTQ4m2NT06LfqDLG75Yr_ZygD5SqzuskIej6A1-dI95kQ9tQpTS5gH7bjMLdf1mGHV6dpJN_eyr-GVvVultyldaOsxgEWE_49Dswz4-hUyMmqAzEAJluWb6WeaAiCkotI5hLzfLeyNwg0XSkYw-hmbaMpk4-miec6JMJcqt3WQ3JOheXYXiw1nHDd69217j1m2fdaQWLe1HpK1ShBg1vTiLXihYh8zNe7ezCu-QHfl1RsYGfRAXFL5UbHhKoSc8W9TOhFQIdGelrotGjSfbkGenidN62ayGnQ4QOnCiqc02ahaqm7X_DX__7ovZBzCdJLdEFO44f048qheoTN2tpB83fWSq4d030u35zoZDKkVdzVGShBhfIT-i-71AC69dbYTslqafSh-70GA2eYaWrAlrHH8NewV3rhG5Dc7gRdSbjh3BOz26p47fecdg9Px0hnuDPSvMSx-3M8GDO12D3sutzNzOJtxe7-mcSGiPjJNJuIgxxLfDkF_5tqW_VI6LxuvID64BMcCqrNVpKWtmXVXA6Hpxb2V8dB4a3O7JNJ_BlPkrLut6EWaI_Castk3tCxe1aKsHnB-UEhQctScyzwAytodzeFg0HUvHU9hwjaRI3r6TnZMSWKX2X3Q3KjQNlG0ZoCLbDmXNyQ-7kbm6qi_w9YKuHXJFR6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غروبه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18384" target="_blank">📅 17:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18383">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مصطفی نجفی، مشاور محسن رضایی : تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18383" target="_blank">📅 17:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18382">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">در اقدامی بی سابقه، وزیر دفاع عربستان سعودی و معاون فرماندهی مرکزی ایالات متحده سنتکام در 24 ساعت گذشته 2 بار با یکدیگر دیدار داشته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18382" target="_blank">📅 17:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18381">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سی‌بی‌اس: ترامپ از رد پیشنهاد توافق هسته‌ای ایران ابراز پشیمانی کرده است
شبکه سی‌بی‌اس: دونالد ترامپ در محافل خصوصی، واشنگتن را به‌دلیل رد پیشنهاد تهران برای محدودسازی برنامه هسته‌ای مقصر می‌داند.
او معتقد است این تصمیم، فرصت کلیدی برای جلوگیری از گسترش درگیری‌ها را از بین برده است
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18381" target="_blank">📅 17:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18380">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هآارتص : ترامپ در حال بررسی عملیات زمینی در ایران و حمله به تاسیسات انرژی است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18380" target="_blank">📅 17:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18379">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">منابع محلى از وقوع درگيرى دریایی بين نيروهاى مسلح ايران و نيروهاى ارتش آمريكا در تنگه هرمز خبر‌ می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18379" target="_blank">📅 16:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18378">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">همه برای من زدن که میگن بندرعباس صدای انفجار میاد، ولی بچه های بندرعباس، رگباری کسی پیام نداده که بندرعباس صدای انفجار شنیده باشه.
@warroom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18378" target="_blank">📅 16:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18377">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO1kaCdDWKgQCahXhaWltFEJu2U_dgvg0C-ZC5IGmK3XmlfwhohzyWOCZsh_UYlGxnDg49HLBsYofolA1cXso02W9PFpQEGF0GVC2xhM7bKXk-uuQflXw2PVT3NrnraX0sYbQP8zcVp3vbALaLjJbpGSkdtJfXtDQEjuQjbJVBjgUNZUzi5ZqtKtXnu82iDyXd55t0Id9nIuX9_fA-WCaFZEQJZ3YtvS_CC_aSFRQLEHG9OFm17ROwII6d_0IJjdGzU6hNObQqmeWd7H-96IJ3JSfKBaVwxadSGV2hOKomiyn3WjAAD60WWWmU5lWRoMocfXRfdlfbjOYvJWqdbJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان آتش‌نشانی تهران: آتش‌سوزی مقابل شرکت مینو ارتباطی با این شرکت نداشته و ناشی از سوزاندن ضایعات توسط یک شرکت خصوصی بوده است. @WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18377" target="_blank">📅 16:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18376">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqKbt4OPQBfy6yvgArrgQ7MPWO72Hh0mRqjXWQfoHKTyC67zSnu6Blft3aQD-sMz2LupM0u0MIcHQel1c6159aJuWzKdTxaXerFTlrrbyUdQ9AYeaeiDiuwyjwSK9JFaojyHSuQ2vljVLHD8ctXJRrSvJWKvV8bBM5PERKIf5_oNyn8lpvqz9U2ta-8p63W3w8xNFxgppLRlPMZq92ow3gyjS24hXknOg_76TJUOuhz26up1CMtDm0IAwbg-yea6HJZSWo7IoxBElBQBnQYQreVTfWXXFpcq0M7tTFP1Pyz4PtSXcowONN_nZYI5B-TMOfP_zbcb4w8RJsFGJlS5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان آتش‌نشانی تهران: آتش‌سوزی مقابل شرکت مینو ارتباطی با این شرکت نداشته و ناشی از سوزاندن ضایعات توسط یک شرکت خصوصی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18376" target="_blank">📅 16:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18375">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ شامگاه سه‌شنبه نشستی برگزار کرد تا درباره احتمال اشغال جزیره خارگ یا بمباران کوه کلنگ گفت‌وگو کند.
ترامپ در مورد اعزام نیروهای زمینی تردید دارد؛ او بارها از بزرگ‌ترین تهدیدهای خود عقب‌نشینی کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18375" target="_blank">📅 15:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18374">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اژیر خطر سفارت امریکا در بغداد فعال شد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18374" target="_blank">📅 15:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18373">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال 12 عبری: دیشب، ایالات متحده و ایران با یکدیگر تبادل آتش کردند. آمریکا به هدف قرار دادن اهداف در منطقه ساحلی ادامه داد، اما برای اولین بار، اهدافی را در مناطق پایتخت یعنی تهران مورد حمله قرار داد. ایران نیز موشک‌هایی را به سمت کویت، بحرین و اردن شلیک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18373" target="_blank">📅 15:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18372">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2488574cc7.mp4?token=PKJuCXAQwEDNluxnguDgeI71j_upZ8CrwAaZq3gek3ozmqIoHQgQJEw-OD6qY2iyJYNMUYwUtwXbN9FsZo1l4Xoxha5u0jqhieB76KBsnx86NxZpukokVrfTZUfIZnrr82kp1jzGbCT99i8gSvaNJ2h4mlcWDU8-yvyInd1H4q7Wg0e54ZvG5VG9JqXnl9aUPx2A4RyTsBCREx6ygGoZBqRyTRZo_7AUVlEu8bUwxCb-URuE_UnpPn35vquBN4r4BzGNj3d7llGDHz-QfAW6UHhkULLHF-RuPFaeDsIy0BSOo5XZQsT7_HgFF9IlKN7PSzct17HOPa5T-DUCpQ4gpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2488574cc7.mp4?token=PKJuCXAQwEDNluxnguDgeI71j_upZ8CrwAaZq3gek3ozmqIoHQgQJEw-OD6qY2iyJYNMUYwUtwXbN9FsZo1l4Xoxha5u0jqhieB76KBsnx86NxZpukokVrfTZUfIZnrr82kp1jzGbCT99i8gSvaNJ2h4mlcWDU8-yvyInd1H4q7Wg0e54ZvG5VG9JqXnl9aUPx2A4RyTsBCREx6ygGoZBqRyTRZo_7AUVlEu8bUwxCb-URuE_UnpPn35vquBN4r4BzGNj3d7llGDHz-QfAW6UHhkULLHF-RuPFaeDsIy0BSOo5XZQsT7_HgFF9IlKN7PSzct17HOPa5T-DUCpQ4gpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : جنگنده‌های رادارگریز F-35A نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط یک فروند KC-135 Stratotanker در حین گشت‌زنی بر فراز خاورمیانه.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18372" target="_blank">📅 15:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18371">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حمله هوایی اسرائیل به شهرکی در جنوب لبنان
شبکه الجزیره از حمله هوایی ارتش اسرائیل به شهرک النبطیه الفوقا در جنوب لبنان در ادامه نقض آتش بس خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18371" target="_blank">📅 15:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18370">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFw8VW9z7oAQ3_OONqD-LDM6xAnWIAAAwSOmNXT7vMH2s3TyFA7tpiFr3ZOUgNge8WGifskyN79JWC8YrHak-dHRomqFhJTnsI1BUBysbmYTj3HEnaE4K_UETzBkN3y7ZW12ifP3b0jHyqvwutpKw_Oh2gaOIM-1T0oLS-_47frLnpbQLPF7OC9mawSSU0ewVYbuMlB3_Hv2goMSGEagu5FG-Lcs-yrH_Lg8OUqidMycNcok_ctEaTi5FwUIuhzbCKcNDJkGowrqrJyyOod2qEWsA-gU-_EGPZ0Br0vvIx1wuNdUd-0jslGxc0iPtRwHgZM5YtL2kvuUbQwd-K1jMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا فغانی به عنوان داور فینال جام جهانی ۲۰۲۶ بین آرژانتین و اسپانیا انتخاب شد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18370" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18369">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ارتش کویت: پدافند هوایی ما در حال حاضر در حال دفع حملات پهپادهای متخاصم ‌رژیم ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18369" target="_blank">📅 14:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18368">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هم اکنون موج حمله جدید رژیم به کویت و درگیری سامانه های پدافندی کویت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18368" target="_blank">📅 14:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18367">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ارتش ایران: کشتی‌های ایرانی به عبور از تنگه هرمز به سمت اقیانوس هند ادامه می‌دهند و اگر واشنگتن ما را تهدید کند، پاسخ ویرانگری دریافت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18367" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18366">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اتاق جنگ با یاشار : تمامی کودکان بیمارستان سرطانی اهواز در سلامت کامل هستند و حدود دویست نفر آنها به مکان دیگری منتقل شدند. این بیمارستان هدف هیچگونه حملاتی نبود. فقط چون حملات بسیار سنگین بود در اهواز و در نزدیکی آنجا، مانند تمام نقاط دیگر و تمام کودکان آن…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18366" target="_blank">📅 14:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18364">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">استرالیا در بحبوحه جنگ ایران، هواپیماهای راداری Wedgetail را به خلیج فارس اعزام می‌کند
نیروی هوایی سلطنتی استرالیا در حال حاضر ناوگانی متشکل از شش هواپیمای Wedgetail را اداره می‌کند که به عنوان پلتفرم‌های اصلی هشدار زودهنگام و فرماندهی هوابرد استرالیا خدمت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18364" target="_blank">📅 14:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18363">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حمزه امرایی، معاون سیاسی استانداری همدان از حملات بامداد امروز آمریکا به نقاطی در شهرستان کبودرآهنگ در این استان خبر داده است.
جزئیاتی در مورد محل‌های مورد هدف منتشر نشده است.
پایگاه سوم شکاری نوژه همدان در شهر کبودرآهنگ واقع است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18363" target="_blank">📅 13:33 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
