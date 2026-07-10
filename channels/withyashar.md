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
<img src="https://cdn4.telesco.pe/file/H4bqKjD4rdv_c84_ZlYevoNSNt5Fbx56UKNzSnNDexAwB1uzk08dXaCerJV5s8WXWYgntjm-lSDZga0IL0uM88ref8ablTkhJ5niu3LgjILmiPhWJma3IlZW1JdByzkdoLOiLWjxuFnTqkmHlkP6djCOtkRxZqMJ6aeQZqRcX4KiVexo6tSTJtjj9sXtGcNm8O0RpXt5vWT3oImsjpRGxbI2Pg47vP5yEQ64ax_UGtGcHvej7wqs3q3GevQ5Mt1jli29MSBRZbOooOIJ4UWWLV-oUj7WJO1kv-MwgXX_xOfFuDljjiFnzQfAA0Zvirb8rGilM5VpxPpqqHc9D78tOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 364K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 22:25:00</div>
<hr>

<div class="tg-post" id="msg-17342">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شورای رهبری یمن: از رژیم ایران می‌خواهیم از استفاده از یمن به عنوان میدانی برای درگیری‌های منطقه‌ای دست بردارد و از تشدید رنج مردم یمن جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/17342" target="_blank">📅 22:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17341">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbf7psvqLqQ_ljs1JUuxK38HRi06Nu_0mP99sWrenxPSheP9YZn7ZsLAv-n1AyTYR7Sw82e_XgNVwGHB9Mf7a6huwU1vKVXZ-kM5UNQ-bfVYfT014NWWbGZI1d-lmB9qPW3SEeGWsVsErYAuVcpfsqBsjvCyhUGGxOpBCiFYjXD3N7lBEi73X1N5EJYmKLp5V1T9NREoJ8jvNFWIpJfiWEfwgXvpXPz37QdSqXq3W4SJ076NWrBKLh3KPweVE_cjeejtfoSJJdDmqJYH5tf1Fi3OJVJ8abs83525KYUk_FmfssQnJdC7en_Gv5o7ghTuD3vFNBXCF9IPCTalrUvlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود ، کرج الان مثل اینکه یه چیزی هست که کلی پیغام اومده
@withyashar
به علت تاریکی زیاد نور تصویر رو خودم زیاد کردم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/17341" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17340">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آخرین فرصت , طبق گفته رئیس اطلاع رسانی آموزش پرورش فردا قراره جلسه بزارن برای تعویق کنکور و نهایی
@withyashar</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/withyashar/17340" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17339">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کرمانشاه الان  @withyashar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/17339" target="_blank">📅 21:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17338">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بند دیگری از قرارداد تفاهم ایران/آمریکا به فنا رفت
وزارت خزانه‌داری آمریکا تحریم‌های جدیدی مرتبط با ایران را اعمال کرد.
@withyashar
یاشار : این تفاهم نامه رو رو دستمال توالت نوشتند !</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/17338" target="_blank">📅 21:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17337">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bd1cd0af.mp4?token=YCxxrgl5DAAYkhaKk34_wzj0RSNYAnXP6WIT9L1vc0icG2w1c_HrVSyxXzF3IVcHUz2OVVxuUy1TPJxmzyvHxWYx50FISzbuACezR5xm8mZSo9iBC8ZQNQ5xoGitGn0dkgU7Iq2yfX5rP8OoT_L_WuAQ-4gC9aAOem8UZIZpK9JpXXW6q7o4asxF1y5dsU5mxVnL_l3gCwhtZTcd7YzMjxMd0ac49n2uDHrfx-UaFAWWhBp3Pall9zcQvDdGl_9CYUPPri6210RFir3rcCzqNd3MGsgIRrO-p0FnG_TA6xVNcf-zrbBdClBqNwmNsGnZO4aTpyISGLHiKr9K8hrxEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bd1cd0af.mp4?token=YCxxrgl5DAAYkhaKk34_wzj0RSNYAnXP6WIT9L1vc0icG2w1c_HrVSyxXzF3IVcHUz2OVVxuUy1TPJxmzyvHxWYx50FISzbuACezR5xm8mZSo9iBC8ZQNQ5xoGitGn0dkgU7Iq2yfX5rP8OoT_L_WuAQ-4gC9aAOem8UZIZpK9JpXXW6q7o4asxF1y5dsU5mxVnL_l3gCwhtZTcd7YzMjxMd0ac49n2uDHrfx-UaFAWWhBp3Pall9zcQvDdGl_9CYUPPri6210RFir3rcCzqNd3MGsgIRrO-p0FnG_TA6xVNcf-zrbBdClBqNwmNsGnZO4aTpyISGLHiKr9K8hrxEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرمانشاه الان
@withyashar</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/17337" target="_blank">📅 21:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17336">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حمله کنکوری های کرج به اتاق جنگ
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/17336" target="_blank">📅 21:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HorChGH2VMn_dTmI7QSNgYuIE3fnnHdXlzVdBH1Jf4r-tabkJiWg2vvUAxuJhwFmCE8bySfWvzWLOKYaGFBXnLLbTLmNPoS7chaUHmPmbIAxM9TKB8djobOjtqTE-ws2xZEHVU1_nVcImgyLU2HrrpoG7ZuKN2uKdIPrKd9gzl60rpMu0WDm17XUs4mNDnNVJBXvo80rzbLGFzKKNcii0uNcWV5NT5fcuD2r9wT3MhRtIoHomxJ06ESU-vmN1BfpZtTf9V0B5sABk7F495XoGrNi-BmIlvUUnGcRZxWD5G2ALMSYuAKHS-sxUd32zwouMgdODfwLBJfO__hJUL2nug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرم‌ترین شهرهای جهان تو 24 ساعت اخیر
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/17335" target="_blank">📅 21:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیویورک تایمز: ایالات متحده و ایران در لبه پرتگاه درگیری نظامی هستند واسطه‌ها تلاش می‌کنند تا دورشان کنند
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/17334" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">صندوق بین المللی پول IMF پیش بینی کرد رشد اقتصادی ایران امسال منفی ۵.۴ درصد خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/17333" target="_blank">📅 21:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تایید نشده گزارش زیاد از صدای انفجار کرج
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/17332" target="_blank">📅 21:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/17331" target="_blank">📅 21:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبرنگار CBS: مقام‌های ایرانی روز شنبه برای گفت‌وگو درباره تنگه هرمز و اختلاف بر سر مسیرهای کشتیرانی که از آب‌های سرزمینی ایران عبور می‌کنند، به عمان سفر خواهند کرد.
میانجی‌های قطری به‌تازگی مشهدِ ایران را ترک کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/17330" target="_blank">📅 21:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تصویر ماهواره جدیدی که منتشر شده نشان میدهد ناو هواپیمابر جورج بوش و گروه ناوشکنهایش به فاصله(۲۲۰ کیلومتری)  از چابهار قرار گرفته  حتی نزدیک تر از ناو لینکلن @withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/17329" target="_blank">📅 21:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470c8df2f2.mp4?token=kyQXpxrCxDGuHYf_6g43TeCLDgIHTEPKPJc5Dp9HACMy-Xm-lH3mN8mDysD_wex8eIbKEK-qmZIVaSb9Yp_VwAJltG4Jgjgg3DbjgAGzYHHFdxYjIWRdL_Sevh4F98nLpM4QOyxcj8Hn0g35ICDusZi6WTe8F6019Y6fG8UKIkEOy_tkak-XueYIN_6YfXPcrus44dXYvHLNVtaCwGvI9SFis3jr3REM8Sm9esfGmpfzIAk-wOMQ9Shs5Pv1X92X7jw6TOlUYhtOkqCFQRzn_htRLHpaTgn_2Hpzxa2pT7KdvsVV5xbS47P2-JlIQxeEdyiXtpiow-mQrk5-6wAqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470c8df2f2.mp4?token=kyQXpxrCxDGuHYf_6g43TeCLDgIHTEPKPJc5Dp9HACMy-Xm-lH3mN8mDysD_wex8eIbKEK-qmZIVaSb9Yp_VwAJltG4Jgjgg3DbjgAGzYHHFdxYjIWRdL_Sevh4F98nLpM4QOyxcj8Hn0g35ICDusZi6WTe8F6019Y6fG8UKIkEOy_tkak-XueYIN_6YfXPcrus44dXYvHLNVtaCwGvI9SFis3jr3REM8Sm9esfGmpfzIAk-wOMQ9Shs5Pv1X92X7jw6TOlUYhtOkqCFQRzn_htRLHpaTgn_2Hpzxa2pT7KdvsVV5xbS47P2-JlIQxeEdyiXtpiow-mQrk5-6wAqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داده های ماهواره‌ای امروز دو اصابت آشکار در باند فرود در فرودگاه بوشهر در ایران را پس از حملات اخیر ایالات متحده نشان می‌دهد.آثار سوختگی نیز در اطراف باند قابل مشاهده است.
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/17328" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اقوام ایران
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/17327" target="_blank">📅 21:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تسنیم : بررسی‌های میدانی حاکی از آن است که اخبار منتشرشده درباره وقوع انفجار در شهر یا سپاه ناحیه قائمشهر کذب بوده و در زمره عملیات روانی دشمن قرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/17326" target="_blank">📅 20:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9a172fe.mp4?token=oZcKuygmpix4O_P7KySv53BzOAg5M0_P1pIYW-_vwezg4wuz_Qhcgo1IhwJspBISISWojOHENafvm2zBFRsSF2E-NDLHJDyJnSAcy3skwoUiVFM0WzAiqD1zKCL-vNg4xXGmm_qVLLsa_N1Ept57qRg6-ZwHTbqTFogc4-SVvRwXzwrhDsW4fTAg7LVxcH2MmJeUh_cpiIRHxJtyS23aXoLt-9Y0skx5THk7f_JrPqMhHVb9P9mPr-wOprVvtJjxP7kUgHUcjGeTI5d0mCEgEOXT3kULM_Aa4NMUe4A6zqVFNziwag77VyRLW-1FfagCh6o1D6-6VVGyrS5CbfStkqrcZlyzYC9oyrHKN2fEB1VhkX_0xGgBboOfjkqHrMzQI0lNXQJyp7eTZDemMxUiUGxEPRpaXggl85HdoDp9G2ndLe5mirlantQYGUXyJaTAmH743tZ2AEFJ8KVOy_z8qaAnXY5e9mSs4O_5NJfNhP8GV6aHFzdQnGLnUuop5Xpr6QMekb_ULsc6TgwuZYnI5OuxqILvvBbH3etGeOmnuy3BPBPo_x4ILhzdvB2ncEGoTvBQ9f1tgQH41oAgJwWFBLhjoDJa08G1mmgVV37_8q0RiUSUPsAU9ESgcks8CxnF4QozbZPOe9LASn-Oo7sDiIPei_4DrpuDmiEYVFnQb3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9a172fe.mp4?token=oZcKuygmpix4O_P7KySv53BzOAg5M0_P1pIYW-_vwezg4wuz_Qhcgo1IhwJspBISISWojOHENafvm2zBFRsSF2E-NDLHJDyJnSAcy3skwoUiVFM0WzAiqD1zKCL-vNg4xXGmm_qVLLsa_N1Ept57qRg6-ZwHTbqTFogc4-SVvRwXzwrhDsW4fTAg7LVxcH2MmJeUh_cpiIRHxJtyS23aXoLt-9Y0skx5THk7f_JrPqMhHVb9P9mPr-wOprVvtJjxP7kUgHUcjGeTI5d0mCEgEOXT3kULM_Aa4NMUe4A6zqVFNziwag77VyRLW-1FfagCh6o1D6-6VVGyrS5CbfStkqrcZlyzYC9oyrHKN2fEB1VhkX_0xGgBboOfjkqHrMzQI0lNXQJyp7eTZDemMxUiUGxEPRpaXggl85HdoDp9G2ndLe5mirlantQYGUXyJaTAmH743tZ2AEFJ8KVOy_z8qaAnXY5e9mSs4O_5NJfNhP8GV6aHFzdQnGLnUuop5Xpr6QMekb_ULsc6TgwuZYnI5OuxqILvvBbH3etGeOmnuy3BPBPo_x4ILhzdvB2ncEGoTvBQ9f1tgQH41oAgJwWFBLhjoDJa08G1mmgVV37_8q0RiUSUPsAU9ESgcks8CxnF4QozbZPOe9LASn-Oo7sDiIPei_4DrpuDmiEYVFnQb3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مانوک : ساعت ۲۵
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/17325" target="_blank">📅 20:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">@withyashar
ماتریکس</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/17324" target="_blank">📅 20:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قالیباف : تنها با کسانی می‌توان با آمریکا مذاکره کرد که برای جنگ آماده باشند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/17323" target="_blank">📅 20:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">@withyashar
اتاق جنگ با یاشار</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/17322" target="_blank">📅 20:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ایلان ماسک می‌گوید اگر اسپیس‌ایکس به اهدافش برسد، «ارزشش از کره زمین بیشتر خواهد شد». @withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/17321" target="_blank">📅 20:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ایلان ماسک می‌گوید اگر اسپیس‌ایکس به اهدافش برسد، «ارزشش از کره زمین بیشتر خواهد شد».
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/17320" target="_blank">📅 20:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f319acbe99.mp4?token=LI-urAJh9gWHoUhlKa87cAihfgRIfeF2pq4-17qCsYjHE0v3y8n1BDVYBiWBm8XXHiYQx7sxtP2yZbJaJJRo3BfBcPEZTK9nOUdK9hO2gEbqMUlg4sDVV1wvWt35TZ1eS-WjglnXo_McbwWgMg3T5HbPxa-Avfdup54Cv2mE-M6qdCSBuyfX8ZYIhY8_kZo0sWKGPBhw_p-JNa56ieIZMTa3ZMveVh2DoFbnoxhePQaygohkl6pl5baJRmc_r2u7VThjGFGawkv59DVBxiVwnuzqVgEL5rhm4TXVTNi0LXEIR0fEncK58meHD6RKeDj6-T7Rhnpvy9txM5uNTntUUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f319acbe99.mp4?token=LI-urAJh9gWHoUhlKa87cAihfgRIfeF2pq4-17qCsYjHE0v3y8n1BDVYBiWBm8XXHiYQx7sxtP2yZbJaJJRo3BfBcPEZTK9nOUdK9hO2gEbqMUlg4sDVV1wvWt35TZ1eS-WjglnXo_McbwWgMg3T5HbPxa-Avfdup54Cv2mE-M6qdCSBuyfX8ZYIhY8_kZo0sWKGPBhw_p-JNa56ieIZMTa3ZMveVh2DoFbnoxhePQaygohkl6pl5baJRmc_r2u7VThjGFGawkv59DVBxiVwnuzqVgEL5rhm4TXVTNi0LXEIR0fEncK58meHD6RKeDj6-T7Rhnpvy9txM5uNTntUUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرمانشاه دید بهتر و نزدیکتر
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/17319" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSSnhMNgl-V2imRPrTyzxOmuDdcQ_dVs1zLHL9UrW08e-T0qTUvKgq1BbvGk0k76gDjEYzsIfiiaioDs6bLzpnmcv5mCh0BTYbMDW30J_WAELdCnmtqxWgEUUeEAsVIZsEhndtorCQq8yk5l60jspueAYXO-C-KQmeRtVgon6JY-xi0PCk-E1VH3wly8ZcPJH5CeGtb3ucjeeWWKJC9JXoNg6TcdC-KNY1ufQUtRnSq9ZZEEwJUtpDIE1qdlJRwSaN16hPchV4ndyyPYYCVmWKw9449YXYLm1kP6EVz6wvq0_R4NZv-tmdc39zpbQD_z6UpFOM9RZt8q8h3FiiXk4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرمانشاه الان
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/17318" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8dgrSwcAbMxutks9s3AmQ60tVP_9Hm-sKOrGZZVLc4e9u8jJ--LYSeoPWefQ5EMnYQJnvrcQbVKx2YvS2lZj9EcZcN0vGseINSVka-sKlXMWA-xUisl1DqSV3-Z9x2GEL5oJn8aLNsynM32QgQDprl4MtseQDTNbxTPDF4SpywRBfsvi9m3xyGsxBPKGSwKXt40mm4QZchrW8usB0piTV2dvA9Zzs_O1IBavJvahdze1D6VlOZNGhD2fRTIfcWTQRqnchOPBP4Tp5Hz10L0wvpz_UJZ-ZXMJm7CEI48OuDVuXBwCQ2IEqnO-umwsoVxgp2N6kaNKTrPaxRiCOB_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرمانشاه الان
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/17317" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فارس : تکذیب شایعه مذاکرات جدید ایران و آمریکا
یک منبع آگاه در تیم مذاکره‌کننده ایران:
ادعای العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات در هفته آینده کذب است
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/17316" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkkqUk6qU2U_Bmc4v5BkB--H87eMGquz0PjGPOZEhBqd3KJuNUFtej0NZE2ICuOKmOYbD7g_bR27jW9SEkjYEBo2YCylx5c7H4_67JpXaLLIWBu4e5Lk0HUALuM-DwYY7JtzHRvWqJioymQUIBNBPHs3ob-J-4xpu5DMSEFJNulSDyxbNHfhvTfjzNIgVF96xxrtwHfDamUKpKCmE0SOKXozh-PuE0lhbfvFPiAIjoo4przRA8nVpAHTLsKitC6fWnFzWXuuCGNSkODCVKQtaucuFKNyvFcls02_4zmuOwThEs-aLzvVfB66HCwxA5yFmdfvAvrzSU80Db1lh1wVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سری انتشارات فرازمینی ها پنتاگون این عکس را که توسط فضانوردان در شاتل فضایی کلمبیا گرفته شده است، منتشر کرده است. در این عکس، یک جسم ناشناخته در مدار پایین به دور زمین دیده می‌شود. در اولین عکس از مجموع سه عکس، این جسم در نزدیکی مرکز تصویر، و سمت راست کره زمین قرار دارد. این عکس در طول ماموریت STS-80، بین 19 نوامبر و 7 دسامبر 1996 گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17315" target="_blank">📅 19:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17314">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اکسیوس: قطر، پاکستان، ترکیه، مصر و عربستان سعودی در تلاش برای کاهش تنش‌ها بین واشنگتن و تهران هستند
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17314" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چندین گزارش تایید نشده از انفجار/زدن ساختمون سپاه و اطلاعات (کنار هم بودن)  در قائمشهر مازندران
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17313" target="_blank">📅 19:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17312">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش‌ انفجار اهواز
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17312" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آکسیوس: دور جدید مذاکرات ایران و آمریکا، هفته آینده در ژنو سوئیس برگزار میشه!
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17311" target="_blank">📅 19:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f831f063a2.mp4?token=RuXgegABWQKz72-El8i2_E-XFauaKkY9DFgX0CR6brRzSuDe73p9SN0g_draIt1wVgopJas-7_py0JMwxTdJV7OrGDLqTQ9fo0IDtHRQrTHGUFAssxUsj0tpKeRxS2Sso05sHzSFbSer7Kl3MMuzc6mR0YdSWncMqA67V9a8dqXwjLO39FNzRb2gLKTtSFpTwE7dwc2hrKHMuyoMNW8W49zq6zQEFEXQ_LHaM0EM5jrn_N92RHT8VQM5CZOBFf4Q5Qk15_F3m2Zyo4HIBvHmNPaA8r7E25_pVahCoEPHiKM9KjKgKeV-PkHHaHDg31n_zYn9vI_9vUZoG-aSdyOL3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f831f063a2.mp4?token=RuXgegABWQKz72-El8i2_E-XFauaKkY9DFgX0CR6brRzSuDe73p9SN0g_draIt1wVgopJas-7_py0JMwxTdJV7OrGDLqTQ9fo0IDtHRQrTHGUFAssxUsj0tpKeRxS2Sso05sHzSFbSer7Kl3MMuzc6mR0YdSWncMqA67V9a8dqXwjLO39FNzRb2gLKTtSFpTwE7dwc2hrKHMuyoMNW8W49zq6zQEFEXQ_LHaM0EM5jrn_N92RHT8VQM5CZOBFf4Q5Qk15_F3m2Zyo4HIBvHmNPaA8r7E25_pVahCoEPHiKM9KjKgKeV-PkHHaHDg31n_zYn9vI_9vUZoG-aSdyOL3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجموعه اکسین پلدختر
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17310" target="_blank">📅 19:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17309">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش انفجار جدید از بوشهر و بندر
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17309" target="_blank">📅 19:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rb5h_kDr2Idex6ObwZ-IPzkUl0lTS4_SstWnL4BS1Rvjsw6Pj_gB5kiWT3T7LBEVV4rCsWCvFIqUYy14wUHzsBMdS4WgmOqVuoFAr6IarCRj6Wo5uA3a3cwUU0JvShLTsW0LnthcTfQNulcC2NPDXC9yLE2ujHCz2ZmUn49RoJdBD4wncfRQ9ZzBXjN-5wrF56XBFjtI6htvMh86VFQcgedGJN2xv_5XLWqlXzkP9tMKhg1mv8X3p-CUDRoABUOcS7iY-V3BWaNlBCO4E_49ruC7QBBxx8rvqk6D3iO4Rznkc6EPh6zQKCYhEg7VmXPcJKTCsUSyYfy0gCLgU9XLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالایشگاه نفت پلدختر,
یاشار : بعید میدونم کار آمریکا باشه
پالایشگاه نفت پلدختر در استان لرستان، در حاشیه شهرستان پلدختر و در مسیر کریدور انتقال خطوط لوله نفت خام و فرآورده‌های نفتی کشور قرار دارد.
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17308" target="_blank">📅 19:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxl86vXaNXY-W3xeIWswvFeDEZIukS7DPA43JcY0z1LkRp7zyZoS5QQOnOZDb0q7bYwDAMJnJz8c76cviQ3h5xESKzM6motFND-oab4XXvbgWbIBJ0zpzVlTAsC8_zDOtXuxql_tfHme9m_iOvvoyxFlgMLQYW190P9ZlnNR8DrsuCtdUU8-zWh_xhndHwgzmrHQxk_N-tw5lLf5Re12BSK85XnBgCVmugkiX3si8uCQNgiIbrxpMiXjVHHM47MYcDYWn47GsETxoY9xHpYVpYIA_QFHe05eQOKv2S673zHKeeZI3CD2efKuyREbs-EW-yD-OPll_zWYyYxNKGlT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالایشگاه نفت پلدختر, همین الان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17307" target="_blank">📅 18:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbd4b57ad.mp4?token=LTmFWoJ7Gmdht_E4KcGAI2-Z6qBgR1aRfRG9wpziK1OihbLDTje541jt3351WNh6cQWZslJs2uWuLH1J8qSQbeVxVXpIPEVJLGpmTwJYh8p4prFriiobNeUtJ4BKxE-FnxHSmG1WCCVQqgqMZW1N_f9cBS4LQRB9q9Mt7FtrOSNcZFRhlxD-uyByu90QQUX221NcRuff-H2uawzwONoZaK7SEV8K2ADJd9ZfDaw-rFiUoQYGYlYGIJZitdPV43zke8gEUaeWvHccdx4Ip2YbHnyVYSoSab-PhtADIC30q6a0XJiP_a3roES_Kq3cp-NQ0xJgxsX_RFbLZFL03TKGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbd4b57ad.mp4?token=LTmFWoJ7Gmdht_E4KcGAI2-Z6qBgR1aRfRG9wpziK1OihbLDTje541jt3351WNh6cQWZslJs2uWuLH1J8qSQbeVxVXpIPEVJLGpmTwJYh8p4prFriiobNeUtJ4BKxE-FnxHSmG1WCCVQqgqMZW1N_f9cBS4LQRB9q9Mt7FtrOSNcZFRhlxD-uyByu90QQUX221NcRuff-H2uawzwONoZaK7SEV8K2ADJd9ZfDaw-rFiUoQYGYlYGIJZitdPV43zke8gEUaeWvHccdx4Ip2YbHnyVYSoSab-PhtADIC30q6a0XJiP_a3roES_Kq3cp-NQ0xJgxsX_RFbLZFL03TKGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای، خسارات ناشی از حمله موشکی اخیر آمریکا به پایگاه موشکی ضدهوایی بوشهر در جنوب ایران را تأیید می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/17306" target="_blank">📅 18:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17305">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در مصاحبه‌ای اختصاصی با روزنامه نیویورک پست: «اگه مردم ، امیدوارم دلتان برایم تنگ شود.»
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17305" target="_blank">📅 18:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17304">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سی‌بی‌اس: ونس، ویتکاف و کوشنر در تماس با مقامات قطری در چارچوب تلاش‌ها برای تقویت دیپلماسی با ایران هستند
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/17304" target="_blank">📅 18:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVO_3p3B8Ryv1oshFP7hdESKcNfEQRdkWXWNnDCNlOwCpXKeNSaVSZ3-xkBt_OlzO2I1-E1BXuU2DeL3_EnkEhXvyO9pygESfmc-xM_34pRwRsmOCCDnMOoW5GfNzLtJVmLwsCBGvwJDgb9PRFUrMB7NnrD14XpM8k3whkvU17rIQZl_ahK8-CdHhLQeqZuDvROuXL4_tWhGbAoJ4gy7SDlrW821w-lF_3pO-MF6QC8VvLaEpKjfC-ctkewyoDwSSSzEiCo_058uSIf8K18LRbc4pPGiJYQwhzLr2osefDhGj7dB6MqMBxtZG8CDIhc0e5vAaMaMZnyBpkg8_b6CDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ماهواره جدیدی که منتشر شده نشان میدهد ناو هواپیمابر جورج بوش و گروه ناوشکنهایش به فاصله(۲۲۰ کیلومتری)  از چابهار قرار گرفته  حتی نزدیک تر از ناو لینکلن
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17303" target="_blank">📅 18:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/17302" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ62biSsUA9_Qy3W8DvoQBiP7zKUn0KStB7PUzGcLcsq1erMiQUKOseV1tNH5U91nbchXqD-VrVEmcRi92jEcUvTlnTK1VF01102ZOU1zZDpfOFqIUhlpyKBT3Iq6BVn2Et3Q0tiLLFWaspikG8TDUnUHQwDfpmWliNRNTtmpnJI1n5rj2MDoQU6tauHkJkkYcoDFng7OIkkdsdQd-CqlAc2FrLRMo-stfNqtcILUI3hSLTb7FTvrIYTcJNXi5OO6oXC_rtRIEBd2MxvodsZuDLZxGChj9958xHJfuWIF7R1X7akLm-k-k1GazF1VBh2vWAhlJZI3yUzuLpUdVgNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهراً پایگاه دریایی ارتش در کنارک هدف حمله قرار گرفته. @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17301" target="_blank">📅 18:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش تایید نشده شنیده شده ۳ انفجار کنارک  @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17300" target="_blank">📅 18:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زدننننننن
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17299" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش انفجار بندر عباس
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17298" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17297" target="_blank">📅 18:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش تایید نشده شنیده شده ۳ انفجار کنارک
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17296" target="_blank">📅 18:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUu7YnF7K7HODRNZ7Q6oMdAw1VAJBta-pGWtEfsym2MMXJ9p5r3T0OowPEcKRO7dGrH06JBiIPXtQmYMYr2E2IXRBK1p6YDcuQZ9SyySXouRhZh0Gz7-GqpnLH4tn0dRDkoYOxFX3JOVo4t4wxvjDRdyBEykkKMOPGY4bvRJOFrjUPgmJ8Qcacz0kKkZII3jSgyqo6elVZ5LJ6jiAuu1GQdT8MlHF2zfWawlCA8DowvvVdgcBHCHEScNJs4b2Ziao-NbF1tQ90udBmlTY-GiGLKHxTGFS86fQ5eJakgC3W2gSbbRpkmhD16a8wa_Cel4es2KWP18w-SZuYzCklBjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد هواپیماهای نیروی هوایی ایالات متحده که امروز در پایگاه هوایی شاهزاده سلطان در عربستان سعودی مستقر هستند، به کمترین میزان خود از زمان آغاز این استقرار در اوایل ماه فوریه رسیده است. آخرین هواپیمای نظارتی E-3 در اوایل این هفته از آنجا خارج شد. در حال حاضر، یک فروند E-11 و ۹ فروند تانکر در آنجا باقی مانده‌اند. به نظر می‌رسد که ارتش ایالات متحده بار دیگر فشار خود را بر ایران افزایش داده است، و به همین دلیل، بسیاری از تجهیزات حیاتی مورد نیاز برای انجام عملیات‌های بزرگ، از این منطقه خارج شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17295" target="_blank">📅 18:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: اگر جمهوری اسلامی در ترور من موفق بشه، از قبل دستورالعمل‌هایی گذاشته‌ام و در اون صورت، ایران به هدف شماره یک آمریکا تبدیل خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/17294" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBAsyOOTyn_jiCoehga6J43u_6_WPPE6aUmjrgkjERkduZac-LWMkylu7JaJAw6fTJUwIBhvHfx4n4tWxKXozQRHdIyvmwQRJO4eeaApTECBB4Lvjg6UjxYc0GWA4nFHLZKfwdE87Gp6glPhWzOE4OeLde6MXf_VDkMmmduPQRiy_9ADN0aI9vyTLSlNbC_yZ1TkpNU9eP854dXo5S21iD2DBPVpJIsGiVf1zKa3DK0knX_1KiLdE0lIv06_2WtkU-4cIeSrBKoC5L6EUHoHoZUI8-blHqPeLE_Kryvfnk2aUg_-db5-QjXoofj6t5ZQqvLFHfs9IH6kyOflDjMJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ایران از ما خواسته است که به «مذاکرات» ادامه دهیم. ما با این کار موافقت کرده‌ایم،
اما ایالات متحده به صراحت به آنها اعلام کرده است که آتش‌بس پایان یافته است!
از توجه شما به این موضوع متشکرم. رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/17293" target="_blank">📅 18:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwN_u7LX7pTQCYdDPS7HY9JmyjLoLab1yOwaOqm4ZWCDllFRfZtg3wtZ1QgJ8hLCEHJcUsvk-_aLN0AmxeHQzruaoUuLDNUVtHIm1sH1pUBbVa4HXKS7PP5HPefSm4Imq9TrKwn4n9tYwpXHR1LZszS04i5WzaNCp6OLUhq9Tn4KOm3Z1sesxeiOJDUzsOB95P_6p3fZs7IEU5ies06kYLPcOlSRNBAw_nA65STtXQoWM-LcEg86pPRDgEiNvGWzPFsjz7PShPgSxzJj1MSDH1Z3tJnf3SVWiyAKByCo9AaPyHK2fVZiMafc5sPDUMsAKNO41GdFpaYFbzo90dhf8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق تصاویر ماهواره ای منتشر شده؛ ایران مسیر های منتهی به سایت هسته ای فردو با تپه های خاک مسدود کرده تا مانع حرکت سریع با خودرو به سمت این تاسیسات شود.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/17292" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9KvzKPaTbqi9eNL_khl0wJYyFitwKo9Uh5hpnO2XOQUTcuIXQAvqxt2XDIXHhQGMh1FkJmfwF-unF3YGXRFg1AxNwLuV4KVMYhISZYa_5d7q-lvTddz4ooI-5ys1fr-_ZSOra8CVgPCJGVqWC15F05FRXNtesOiTYvreUdJFpZtBQGcZsr1tca1rtqyJZ6SbmGSDcRZxf3u4YW3-nKjCLLD-cFkk-zjf2Y3r3TPXxhCYYb6z6ecAMZ2FDahOuSip46kezwFUTx0PaAvGbNe1QRipZDxRBLYwLf4pMn77DD4ny_LgL5A9RHjDGcQaiMxRO5R1OK4L_vHqAv6ytpApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر‌ ماهواره ای گروه رزمی ناو هواپیمابر آبراهام اینکلن و ناوشکنه های گروه ضربت ناو هواپیمابر ۳ در نزدیکی چابهار که شامل :
* USS Spruance – کلاس آرلی برک (Flight IIA)
* USS O’Kane – کلاس آرلی برک (Flight IIA)
* USS Frank E. Petersen Jr. – کلاس آرلی برک (Flight III)
میشوند
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/17291" target="_blank">📅 18:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بازهم روسیه و چین با طرح بحث درباره برنامه هسته‌ای ایران در شورای امنیت سازمان ملل متحد مخالفت کردند.
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/17290" target="_blank">📅 17:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOR8ijD0rqSh545076G32AtxELtf0nFzKNjsQEzM_ImvzerTOxHji0CR4dh6NFGyaPK3ZfZ1_NAno4GSEoONNHYIfPkI1Sdz3QIIMnGPfTHxE_cfc75mLHLsTvEZzDkHFwpH5_zZH0btWOZZoF_bqu5gKckV2_rWgzTRalDnRDxCmRWgSDrF3DHlzUpkDU1MSMWUg1zc02Xsj2tuRrlc9yMIczdhzvmHlPlt46yzEkJIpJ8xwHFVskMMsiO3IV3hxAM9MV9R1TpgLj6jwB3EnIrdJOtu_EVpc5w2WYdEfTt3BOeMhlBgRWQNPtgVcrSqY7vDxtyk6S9J1vU4gy5MjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن (CVN-72) و چندین ناوشکن مجهز به موشکهای کروز تاماهاک در خلیج عمان، ۲۵۰ کیلومتری چابهار آمداند ، همچنین دو فروند هواپیمای P-8A Poseidon نیروی دریایی ایالات متحده از جیبوتی از صبح امروز در حال اسکورتش‌در این مسیر بودند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17289" target="_blank">📅 17:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17288">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/17288" target="_blank">📅 17:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17287">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تسنیم:یک هیئت قطری به منظور تلاش برای تثبیت جایگاه میانجی‌گری قطر، بعد از حوادث روزهای اخیر به ایران سفر کرده است.
گفته می‌شود هدف اصلی این سفر، تلاش برای تثبیت جایگاه میانجی‌گری قطر، بعد از حوادث روزهای سه شنبه یا پنجشنبه باشد که در جریان آن متعاقب اتهام زنی قطر به ایران در رابطه با یک حادثه ادعایی در تنگه هرمز، ارتش آمریکا حملات گسترده‌ای را طی روزهای چهارشنبه و پنجشنبه علیه مجموعه‌ای از اهداف نظامی و غیرنظامی ایران انجام داد.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/17287" target="_blank">📅 17:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17286">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرگزاری CNN :
دولت ترامپ در حال بررسی آغاز مجدد محاصره دریایی علیه ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/17286" target="_blank">📅 17:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17285">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/17285" target="_blank">📅 17:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17284">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/17284" target="_blank">📅 17:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17283">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ce7bfbd.mp4?token=Ai1qGIeszbZnSKcwdn3d8ob7xQRVFKaERP5g7-BcRLi9PRhhWqUx_mMLqddIBNP9cmbU5CiiqozWB1plpGascFBNAsVBeYd-lfBLR9zhRWNUxZZx5BJ3yPc00IjeCnTI3JkSA2y2wb1nJD2oRQ4Z3Ps67wjCZITJg-Yudp-0YsNE8liTEEi4HMIhWcpledDihV__TUzLeQNloVy6s2m-7sbb1EKp6me4CyzqQSiZLEp1ciBPEi0PuZ2T2iXWiEmloUaCGLQLMIDL1jB_1mrd49awgA8yx-fjuq1jt6F1qy4QVwOyHIIi53pBcY-bUYgJV7M4M_qPMZsr2mO5G-2KWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ce7bfbd.mp4?token=Ai1qGIeszbZnSKcwdn3d8ob7xQRVFKaERP5g7-BcRLi9PRhhWqUx_mMLqddIBNP9cmbU5CiiqozWB1plpGascFBNAsVBeYd-lfBLR9zhRWNUxZZx5BJ3yPc00IjeCnTI3JkSA2y2wb1nJD2oRQ4Z3Ps67wjCZITJg-Yudp-0YsNE8liTEEi4HMIhWcpledDihV__TUzLeQNloVy6s2m-7sbb1EKp6me4CyzqQSiZLEp1ciBPEi0PuZ2T2iXWiEmloUaCGLQLMIDL1jB_1mrd49awgA8yx-fjuq1jt6F1qy4QVwOyHIIi53pBcY-bUYgJV7M4M_qPMZsr2mO5G-2KWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از قبر علی خامنه ای
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17283" target="_blank">📅 17:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17282">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گیلا گملیل وزیر وزیر علوم، نوآوری و فناوری مصاحبه با اسرائیل هیوم:
"شاهزاده رضا پهلوی و من، «پیمان‌های کوروش» را آماده کرده‌ایم؛ آنها آماده‌ی امضا هستند و نتانیاهو با سقوط رژیم شرور در ایران، این پیمان‌های صلح را به خواست یزدان امضا خواهد کرد.
رژیم ایران درگیر جنگ‌های داخلی است،
و هیچ شکی نیست که این رژیم سقوط خواهد کرد!"
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/17282" target="_blank">📅 16:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17281">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d923ee58.mp4?token=HjAcIMW8QMuPFXhZsPoGFOxP4ltr4UfqFdDfWB-MUiRCgmDwtfyezwaQxI7vE1vdWzuzp_4TYepwaPiQLFV5HaFm3mQvxTq0iJvqENFfxysKXf0rTNNmirtaHmwRa3Rp0EW-KslZ_bqYXu1UskpDb9IUHzdSDzBmONBH5mtnVN1nIbx-mg1DJ38sbg1xiEFhfYg7enP5nqD5_7LBs_kXvOotrPYhWwCLWud5W5KqEMQALJ4HtH_aWDWqQLC0gZfUghXQjgqx5uGB5S1uzeWnDpwBJHmKinPWRWrYkmUVIatE8__i_XbPWwtdANZX86HoEgwMD1fMux62LNzeGZ-BNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d923ee58.mp4?token=HjAcIMW8QMuPFXhZsPoGFOxP4ltr4UfqFdDfWB-MUiRCgmDwtfyezwaQxI7vE1vdWzuzp_4TYepwaPiQLFV5HaFm3mQvxTq0iJvqENFfxysKXf0rTNNmirtaHmwRa3Rp0EW-KslZ_bqYXu1UskpDb9IUHzdSDzBmONBH5mtnVN1nIbx-mg1DJ38sbg1xiEFhfYg7enP5nqD5_7LBs_kXvOotrPYhWwCLWud5W5KqEMQALJ4HtH_aWDWqQLC0gZfUghXQjgqx5uGB5S1uzeWnDpwBJHmKinPWRWrYkmUVIatE8__i_XbPWwtdANZX86HoEgwMD1fMux62LNzeGZ-BNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو آفریقا جنازه خامنه‌ای رو بدین شکل تشییع کردن
@withyashar
🤣</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17281" target="_blank">📅 16:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17280">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات اسرائیلی:
دولت ترامپ تمایلی نداره که اسرائیل در عملیات نظامی علیه ایران شرکت کنه.
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/17280" target="_blank">📅 16:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17279">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خبرنگار آکسیوس:
به گفته یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و در تلاش برای کاهش تنش‌ها و ایجاد شرایط برای از سرگیری مذاکرات باشند.
این دیپلمات گفت که جلسات در تهران بین مقامات قطری و ایرانی هنوز ادامه دارد «اما واضح است که هر دو طرف می‌خواهند به یادداشت تفاهم بازگردند».
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/17279" target="_blank">📅 16:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17278">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miz0KTB0MD3cNPJa9uzCyjZDV25zUsbJCvl8lxbXfm16wqVMxJ5fgS5HbI0YZkDdJ3a2dHqdV3JjllYJz5UvCfKqr-PUjCPxCfKJaH1PGkaZ-fCYMzoNncv33_Rls7AddBhqoaTjyBLS6dTsalBuTY3K-PZPRhzrrcAprzRozzq0o4k6pZg6ZRuUuiSRZ0n7hYX72RzQ1UdTGDCSaR4hVjDcdqJ_j_eDdgYyANGpAAHvcQzFbinESssDGeMMF5kOZSgxueFAS_KCbSnkmpEqGtGATypzvauFHW_hOHPneU84uWUdI6WBis5T9JfjNbQcAyOcyQx89_HRMjp-AU_iPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون  گزارش های زیاد از ستون دود عظیم تهران فکر میکنم سمت شرق(بزرگراه امام رضا-جاده مشهد)
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17278" target="_blank">📅 16:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17277">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfFb19cjUR9o4aCZBJ_w4lqwp2e9QhcPMCt4m6aZQDrb1pi4aLVqsU2vR8McAALu0bPfdRSdJuKi6MVvyn50dQzHzM2qOuEbthEiJY-_gOD3k85exnQ6bKPhdRd38DDaRMEP_7KcbiQtvg9ASCd84bEbcOAFslOvWS8FaOc461vUXvaPHy2FnJH6whjXJ_Lag0D1q866iLk4dtJ9DdwxtEHDcXX9JBIayuUCfqgauKP4NMP2GxihwP92eQDChciJinTlf2DXpI3qwMNraEuuv13S5abXFnHmYVVD_31obVwDC35sJk98ZfWFaAM_G0Wn_XCOKW3AjszUeJUnW_hS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دستگیری 8 جوان امریکایی باتهام تلاش برای ترور ونس و ترامپ در هنگام بازی بوکس UFC در محوطه کاخ سفید . این طرح از ماه مه شروع شده بود . یکی از این جوانها    Tycen C. Proper, 19, of Danville,  تایسون کوپر 19 ساله هست و عضو گروه ازادی 250 سال -هست . این طرح خیلی خام بوده . امنیتی ها هم اجازه دادند اینها کارهایشان را بکنند 4 روز قبل از مراسم ، با شواهد دستگیرشان کردند که به ترامپ نشان بدهند تهدید برای وی جدی هست . این 8 نفر از 8 نقطه امریکا بودند
@withyashar
حقیقت یاب اتاق جنگ : خبر پخش شده مبنی بر ترور نرامپ در‌ امروز و دستگیری ۸ نفر فیک نیوز است</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/17277" target="_blank">📅 16:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17276">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترور ترامپ</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/17276" target="_blank">📅 16:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17275">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">منابع آمریکایی به شبکه CNN: آمادگی‌ها برای حملات بیشتر به ایران تکمیل شده است. در حال حاضر، واشنگتن فرصت نهایی را برای مذاکرات دیپلماتیک با میانجی‌گری پاکستان و قطر فراهم می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/17275" target="_blank">📅 15:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17274">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">محمد باقر ذوالقدر، دبیر شورای عالی امنیت ملی جمهوری اسلامی هشدار داد اسرائیل پشت این اقدامات خصمانه قرار دارد، آنها از پاسخ ما در امان نخواهد بود. در صورت وقوع حملات اسرائیل به زیرساخت‌هایمان ، انتقام خواهیم گرفت و به آنها حمله خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17274" target="_blank">📅 15:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17273">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYfiyXnJwQdVWa4ywp3uyqjLwIEZEoXiiyIAM5dDFiUUAmqVvoA00a0xP5od3XRiISpOEevmpAgXpxiwjXuUDorCyjoeyPUQ8LmYrDq9acVIKMCiSH4-9bFU29hkSSlpAjt0kOVpD6rHLEI9rE2C3oRSzf4YyJ7gVWrlH7N7v-FmFlQUpTja8cBVQo01vePj7Gg38wJgQ0rOhqA_KJIBE_I5zxS7M0E7LV6OeaIq3WgQrujlOnF6nBY3BeymRMLkuwk9aXI-ZiTm9_8D_4JgbdJPKHLpYWfaMmxhGRcz6jeUpywv-UOYdCWeYXPYTuA_MEuIbXz_0Q6xjyrahn7wjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ فروند اف-۲۲ امروز صبح پایگاه هوایی عوودا اسرائیل را ترک کرده و به بریتانیا بازگشتند (در حین پرواز توسط KC-135R مستقر در رومانی سوخت‌گیری مجدد شدند)
چگونه باید این را تفسیر کنیم؟ فعلا جنگ نمیشه؟ یا محافظت از مهم‌ترین دارایی‌ها قبل از هرگونه حمله بزرگ احتمالی؟ زمان همه چیز را مشخص خواهد کرد..
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17273" target="_blank">📅 15:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17272">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce7054159d.mp4?token=oW3PL095ZhWdhHGpt7-JO_D2xuu28XSvvvgiyxizV3pcOTKfUU-mTeOPz07OJUJ8mJtb3-u-qLSuoEUo0lscSrr6hQ61ThBXg6X5N_sdPkD8yp3q4yXneXFz6oNR3fttUg3_swJiM_icVUMEWdwf5cE7y9TtvDBXD9pT-JN_vUoM6hUIZMzMYQsEhRbXTt5lOxix_ijxbfplVWLdG1H1Zk1SLrMOZijN9iOpbXNMmdybWWWHDNnNmafMjLAVn1iHW4Fv9T1I0RhZG9bdW89OXGarkkIroKvPpeL5sPuHTCCBIFqDHeMd_ukCRhSKxZSYTZ6ATNRgKC5-m-HnWI7oRIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce7054159d.mp4?token=oW3PL095ZhWdhHGpt7-JO_D2xuu28XSvvvgiyxizV3pcOTKfUU-mTeOPz07OJUJ8mJtb3-u-qLSuoEUo0lscSrr6hQ61ThBXg6X5N_sdPkD8yp3q4yXneXFz6oNR3fttUg3_swJiM_icVUMEWdwf5cE7y9TtvDBXD9pT-JN_vUoM6hUIZMzMYQsEhRbXTt5lOxix_ijxbfplVWLdG1H1Zk1SLrMOZijN9iOpbXNMmdybWWWHDNnNmafMjLAVn1iHW4Fv9T1I0RhZG9bdW89OXGarkkIroKvPpeL5sPuHTCCBIFqDHeMd_ukCRhSKxZSYTZ6ATNRgKC5-m-HnWI7oRIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مراسم خامنه‌ای در قم یکی از محافظان سعی داشت مثل اسپایدرمن، جلوی ماشینی که تابوب خامنه‌ای رو حمل میکرد، بگیره
@withyashar
😂</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17272" target="_blank">📅 15:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17271">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به‌گزارش یسرائیل هیوم، دونالد ترامپ به‌دلیل نگرانی از کاهش شدید محبوبیت خود در آستانه انتخابات میان‌دوره‌ای، قصد ندارد جنگ با ایران را ازسر بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17271" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17270">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر خارجه ترکیه: آتش‌بس میان ایران و آمریکا پایان نیافته است /دو طرف واقعاً می‌خواهند به سوی یک توافق صلح‌آمیز پیش بروند /امروز با همتای ایرانی‌ام تماس داشتم و آنچه رخ داد، سوءتفاهمی درباره سازوکار عبور از تنگه هرمز بود
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17270" target="_blank">📅 14:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17269">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2511809773.mp4?token=WcOt6s7SZnTwbWoXTjfRBOJQxnL-ObNTrxXDQQ9UpQCC-NJG2N23Cdb_acI2QyZHQsSg-0KxFpbu2q1apRULiJeDChkxYUPEYoA8LG1uOjtBFrjfFtxMhO8eAwTptcO-nk2hBBdT3ICIqLptRu8ts3ZxTa2ozdW4u24USZLTUuM7FDGV9GM31ZEjybarWSOvuycXsVAzz8uInP3AMp8wbH9aa7i98lMTlix1DkWjHq2UE75nddN9ilj5x8WZFI9NAK2g0dUVDyXtBkFlRA7MBjwJdSNOkZlCC9xS94tzKYNrGAVLY4LdPLOnSC-m6bGx5JscuPWTIt-0A-_x2qLwzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2511809773.mp4?token=WcOt6s7SZnTwbWoXTjfRBOJQxnL-ObNTrxXDQQ9UpQCC-NJG2N23Cdb_acI2QyZHQsSg-0KxFpbu2q1apRULiJeDChkxYUPEYoA8LG1uOjtBFrjfFtxMhO8eAwTptcO-nk2hBBdT3ICIqLptRu8ts3ZxTa2ozdW4u24USZLTUuM7FDGV9GM31ZEjybarWSOvuycXsVAzz8uInP3AMp8wbH9aa7i98lMTlix1DkWjHq2UE75nddN9ilj5x8WZFI9NAK2g0dUVDyXtBkFlRA7MBjwJdSNOkZlCC9xS94tzKYNrGAVLY4LdPLOnSC-m6bGx5JscuPWTIt-0A-_x2qLwzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل اعلام کرد یحیی سعید محمد حمدان، فرمانده تروریست یک تیم «نخبه» در شاخه نظامی سازمان تروریستی حماس، در حمله‌ای هوایی در جنوب نوار غزه به هلاکت رسیده است
.
او در حمله ۷ اکتبر به پایگاه رعیم مشارکت داشت و طی هفته‌های اخیر نیز برای طراحی حملات تروریستی علیه نیروهای ارتش اسرائیل و بازسازی توانمندی‌های حماس تلاش می‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17269" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17268">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کارخانه فولکس‌واگن در ولفسبورگ در معرض خطر تعطیلی و صدها کارمند در معرض اخراج قرار دارند، زیرا صندوق سرمایه‌گذاری قطر، از توافقی بین این کارخانه و شرکت رفا جلوگیری کرده است. این توافق برای تولید قطعات مورد نیاز برای سیستم دفاعی "گنبد آهنین" بود. صندوق سرمایه‌گذاری قطر، سومین سهامدار بزرگ فولکس‌واگن است و با اعمال حق وتو، از انجام این معامله با رفا جلوگیری کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17268" target="_blank">📅 14:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17267">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سی ان ان:اوضاع به شدت متغیر است؛ احتمال از سرگیری گفتگو ها وجود دارد اما احتمال جنگ هم همینطور
فرمانده ناو هواپیمابر آبراهام لینکلن در دریای عرب به خدمه خود دستور داده است که آمادگی خود را حفظ کنند و منتظر هر دستوری باشن
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17267" target="_blank">📅 14:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17266">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جواد لاریجانی : باید لیست افرادی که در ترور رهبری دست داشتند را صادر و اعلام کنیم که از نظر ما مهدورالدم هستند
این جنگ به پایان نمی رسد مگر انتقام گرفته شود.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17266" target="_blank">📅 14:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17265">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال 14 اسرائیل: اگر مجتبی زنده باشه از ناحیه دو پا آسیب جدی دیده و روی صندلی چرخداره، به همین دلیل مقامات نمیتونن اونو در انظار عمومی نشون بدن
@withyashar
یاشار : اینو خوب گفت
😂
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17265" target="_blank">📅 14:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17264">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">با تمام حالات چراغ اتاق جنگ امشب روشنه و ما امشب رو بیدارم
🙌🏾
همیشه احتمال هست مخصوصا وسط مذاکرات اینشکلی اونم اخر هفته که مارکت بسته میشه</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17264" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17263">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اکسیوس:  ایران و آمریکا از طریق میانجی‌ها توافق کردن فعلاً به همدیگه حمله نکنن و برای حل اختلاف‌هاشون، به‌خصوص درباره تنگه هرمز، دوباره پای میز مذاکره برن
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17263" target="_blank">📅 13:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17262">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بابک زنجانی: در خصوص (راه آهن) آق قلا حرف و حدیث‌هایی از خرابکاری به جای حمله دشمن البته وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17262" target="_blank">📅 13:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17261">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">@withyashar
امتحانات ۲</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17261" target="_blank">📅 13:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17260">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اتاق جنگ با یاشار : عمو اگه امتحان دار‌ی خواهش میکنم درست رو بخون
🙌🏾
این خودش ضد خواسته رژیمه اونا میخوان تو بیسواد باشی ، این خودش گارد جاویدان بودنه ، ترس رو تو وجودت راه نده سنگر رو نگهدار ، ترمیناتور باش مثل شیررررر باش نسل بعدی ما نباید روح و روان خراب…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17260" target="_blank">📅 13:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17259">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">زیرنویس شبکه خبر: ازمون های نهایی بدون تغییر و طبق برنامه ابلاغی از 21 تیر شروع میشه @withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17259" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17258">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یکی از کشته های تیراندازی در مشهد
🚨
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17258" target="_blank">📅 13:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17257">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسرائیل‌هیوم گزارش داد آمریکا، اسرائیل و برخی کشورهای منطقه در حال بررسی گزینه‌های سرنگونی جمهوری اسلامی هستن
و ازسرگیری هرچه سریع‌تر محاصره اقتصادی ایران رو یکی از راه‌های رسیدن به این هدف می‌دانند
یکی از مقام‌هایی که اسرائیل‌هیوم اونو آگاه از تحولات داخلی ایران معرفی کرده، گفته اختلافات داخلی در جمهوری اسلامی تشدید شده و سپاه ممکنه کنترل رهبری غیرنظامی رو در دست بگیرد
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17257" target="_blank">📅 13:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17256">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیویرک تایمز : محدودیت‌های تصاویر ماهواره‌ای ایالات متحده، روزنامه‌نگاران را در پوشش جنگ ایران با مشکل مواجه کرده است. اما منابع دیگر راه‌حل‌هایی ارائه می‌دهند که پنهان کردن اقدامات ارتش‌ها را دشوارتر می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17256" target="_blank">📅 13:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17255">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بلومبرگ: روسیه به دلیل فروش نفت در جریان جنگ ایران، کسری بودجه نادر خود را جبران کرد
پس از امضای تفاهم‌نامه بین ایران و آمریکا قیمت نفت خام روسیه از ۸۶.۵۲ دلار در ماه مه به ۶۳.۵۲ دلار در هر بشکه کاهش یافت
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17255" target="_blank">📅 12:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17254">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDenzQYol4AGtGHO-zOnmJP_gjYrLSLONxALHUpAJYBXRWXWGCS15-_Dh_eYiLW-NlGa3Lyy-QMC2EVx9hlTory1Z4voJ_n-7JVuOfv5pNJIEYMH-yKuDQ0s7WA6tJElWtmIE_QaF0MWaUvHiO9eBan9qAbELOQVdCr6HEK2w4JJpkIpFiCrNfM2fmMA6qHysVzcnEFmFR2coBdzI9q-j318Gd1wJcuI6Fbeh2QaM0Bu-b5Dh40bCgb_0JC83gILtOb7lByEGV4rZ4KeNY5HTMvKT-aOkaaLakeFZbojHgahyAdxF7UQOIDmhbLW0w7B5DCDntHWX620BM_Et-lCcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر: ازمون های نهایی بدون تغییر و طبق برنامه ابلاغی از 21 تیر شروع میشه
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17254" target="_blank">📅 12:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17253">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سیتی ژورنال: وزارت خارجه آمریکا جلوی دیدار مقام ارشد تیم زهران ممدانی با سفیر ایران در سازمان ملل را گرفت
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17253" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17252">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترکیه برای دریافت جنگنده F35 آمریکا، پدافند های S400 روسی خود را فروخت منابع ترکیه‌ای مدعی هستند که ترکیه سامانه‌های دفاع هوایی اس۴۰۰ ساخت روسیه را به یک کشور ثالث فروخته است و نام کشور امروز اعلام خواهد شد. پیشتر آمریکا به عنوان شرط فروش F35 به ترکیه اعلام…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17252" target="_blank">📅 12:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17251">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رویترز: جنگ ایران، جهان را تا آستانه یک بحران غذایی پیش برد
درگیری بعدی در خلیج فارس نیز می‌تواند همین پیامد را داشته باشد.
کشاورزی مدرن به کودهای شیمیایی ارزان‌ قیمت وابسته است. این جنگ با گرفتار شدن کشتی‌ها، تعطیلی کارخانه‌های تولید کود، هراس کشاورزان و افزایش شدید بهای کودهای شیمیایی، تولید جهانی غذا را در معرض خطری جدی قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17251" target="_blank">📅 11:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17250">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مسئول آمریکایی: واشنگتن عمداً حملات متناوب را انجام می‌دهد و سپس متوقف می‌شود تا از تشدید تنش‌ها جلوگیری کند و فرصتی برای دیپلماسی فراهم شود.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17250" target="_blank">📅 11:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17249">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJSzOHQvccWj8D9CP12Yg0C7oJZYI2JmTtOv1Ai4pDD4mPDaqqNpUvhnIbkuSM7wkrbhhB3Le_jUTWY7glqF3-FpU3dTr7KcUNkAamNHWYILDKkmdj_yNeOZJP5sqCkTYYO973EJQUVBZsexpc_b923kK7oDK9E0iEQ76JQTMQoE2EIsFRXoHtK3SC4LegMop1MTIMuoKQ79H0D5Bic6mZszULk-68I7H2mDkOTt76ZErEzpa3MbUS34dJgYC7unlQrbA6DxojaZbmDnnnDoThaqsNEa7t-2zj3ySNJDc-ZsLU38QA-nM-O5ov9kiWfAR--BZ28F2r84xk6ZN-SY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه اردوغان به سران کشورهای ناتو که در اجلاس آنکارا شرکت کرده بودند.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17249" target="_blank">📅 11:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17248">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یاشار : خیلی از‌ اخبار که امروز پخش میشه من دیشب پست کردم
🤒
قبل فرستادن خبر‌ در ‌دایرکت چنل رو کامل اسکرول کنید و ببینید
😩
❤️‍🩹</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17248" target="_blank">📅 11:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17247">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkbfO7TTisJDWkxhZTrB9KdJKglkjZA5CCqx-5fzD0DlEiz0Bbu1CtQqSa3ZwuzgOM176tskjjLIReQo2b28uNsz1ElDLnc2ZMJjR9LHkafaoR2K0-kNMfCy07SyebL-YoeHmqakk0db_oxGwSfe5Eu8djwqfS329W75aB1dI0Oc9ss2fwCq3d34L9bT6sRare17SmbgdbLfODgWN4YAOKUzwzl-Ks42JXFA2f3xosGL-uGItKWdR92rdDrBmT8R6eSJIX_H1KJNamHfOX0TUwKrk-dGEmYd8O3znZGjTnbLBVG7FaS5yCKq_oJ_mmdacgHr7Bf3JJmpop5I5vY5Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ اسرائیل: ایران با جذب شهروندان و اتباع خارجی، اطلاعات و تصاویر مراکز حساس از جمله اطراف وزارت جنگ و مجموعه نظامی‌«کریا» را جمع‌آوری کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17247" target="_blank">📅 11:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17246">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tch7iewT8YYcqkOPWREGxdcM7h2h-Aa22VwvZdvY_AC6XIjuB321vBpUFjGGfuTuBeH9iApXC5iV-383imCxhrF8q1SYABl_Hstnj82iKZ-0jppaDuKw6yA9vD4Ut12Y7fFxCqHfioU57Ux1iTmQ0OJLdXjvIAvbEVNaBgvyYwu9x0sdo0mAJxjxtL1fIymScn087PHW9LaFFUKxWASObTC7boYseD-Kcw29Si3UiXmojOOXuauyG9ZTAUcuWelp7EQyqvXBOqvFE9Q9CtMbUTu-6jD-OlklpirvwTci96g6GJly52S8o9P2k7VumCZRaUZa9oVECc9JjPttV_GPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه برای دریافت جنگنده F35 آمریکا، پدافند های S400 روسی خود را فروخت
منابع ترکیه‌ای مدعی هستند که ترکیه سامانه‌های دفاع هوایی اس۴۰۰ ساخت روسیه را به یک کشور ثالث فروخته است و نام کشور امروز اعلام خواهد شد.
پیشتر آمریکا به عنوان شرط فروش F35 به ترکیه اعلام کرده بود که برای خرید F35 باید سامانه های پدافندی S400 روسی را نداشته باشد
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17246" target="_blank">📅 11:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17245">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شبکه اسرائیلی کان: اسرائیل میخواد به ایران حمله کنه اما منتظر چراغ سبز ترامپه. مقامات در اورشلیم برآورد می‌کنن حملات متقابل میان آمریکا و جمهوری اسلامی در چند روز آینده ادامه پیدا کنه.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17245" target="_blank">📅 11:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17244">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">احمد وحیدی، فرمانده کل سپاه پاسداران، در پیامی به مناسبت خاکسپاری علی خامنه‌ای رهبر پیشین جمهوری اسلامی نوشت خونخواهی علی خامنه‌ای و مجازات عاملان و آمران آن، مطالبه‌ای «قطعی، مشروع و فراموش‌نشدنی» خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17244" target="_blank">📅 11:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17243">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ در ‌تروث: امروز روز بسیار مهمی در پالم بیچ، فلوریدا بود، و افتخار بزرگی برای من بود که فرودگاه بین‌المللی پالم بیچ، با رأی قاطع، به نام "فرودگاه بین‌المللی دونالد جی. ترامپ" تغییر نام داد. به زودی این یکی از بزرگترین و باشکوه‌ترین فرودگاه‌های جهان خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17243" target="_blank">📅 10:55 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
