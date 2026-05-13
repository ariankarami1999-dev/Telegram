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
<img src="https://cdn4.telesco.pe/file/lowYcSn0XK7aIQbaTOU1ed5wfYafMkO27kNDECxkMbv6mh8EZ5ryeZX-3U7fH5gC6JuobQ1Ntxbo2hHKcyMLQfa2nHd6TD8KmqzGZ3ZHxYditFOu57loIvQ8pcTPNUJsqwgn7MbbcZiXoxHbHSGuNK3mN4RcBOL2IaTaCk2oYlSB2lH4IfNYmwzNBRfUISgEzI1ZBugwf1XeUqpsRwdkIk6sAb3-vFOXQ5fOzeEBpZC8OrK_G5lFImwXeQcK4CDy5naXQiXnOnsfgarGoDiWsyIuKX1bAyQ8JupI8BKQlHSP-FbRGfr8VNXorcfN_T9t_7mQdWxa-03kCyC8oRSLkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 961K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 12:53:21</div>
<hr>

<div class="tg-post" id="msg-119683">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی کمیسیون فرهنگی مجلس: تعداد کاربران در پیام رسان های داخلی از مرز ۱۰۰ میلیون کاربر عبور کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/alonews/119683" target="_blank">📅 12:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119682">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
بقائی: تا زمانی که عضو ان‌پی‌تی هستیم حق استفاده از انرژی هسته‌ای را داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/alonews/119682" target="_blank">📅 12:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119681">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نائب رئیس اتحادیه مشاوران املاک تهران در برنامه صداوسیما: وام مسکنی که همین الان در حال ارائه هست آن‌قدر ارزش پایینی دارد که در بعضی از مناطق تهران نمی‌شود با آن یک متر خانه خرید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/alonews/119681" target="_blank">📅 12:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119680">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/razsjHCkt3DOAtCaY_kIFzzZXzJO_pIEqiCyKBy0Fz9OEK76q7hjbFrsEaymYL908pGE68r1lpgQjDF0lXItL6eCTl2bHuc-x-vRgejkcY4BHXHQkrSJsStiMjwC1tksQS9mZx1Yo2c1GoLNmVP6STR1LwrgsliHzcFoY2qmoQUr12I0daRXhMMlEzEdqAyJkhv_0rbXMUl4xaS5xi9vkFQJrcYyton2rhAhYvYuvXEH6d3mAPrRxFHQVwccOKeA_XxmZxGe93IU5IOKhgJZhoS7uIOk97LB2YKqJg1B9y6yX8miaV7TZsXwyFbUrGEz0SQP6ZBrMZ5FCwfCIPFJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تهران تا یک‌شنبه خنک می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/alonews/119680" target="_blank">📅 12:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119679">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر رفاه: داریم تمام وقت تلاش میکنیم که مبلغ کالابرگ رو افزایش بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/alonews/119679" target="_blank">📅 12:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119678">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و جمهوری آذربایجان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/alonews/119678" target="_blank">📅 12:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119677">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
الشرق الاوسط: چین نام روبیو را تغییر داد تا او بتواند وارد خاک این کشور شود
🔴
مارکو روبیو، وزیر خارجه آمریکا، روز چهارشنبه همراه با دونالد ترامپ، رئیس‌جمهور آمریکا، به پکن سفر خواهد کرد؛ این در حالی است که او همچنان تحت تحریم‌های چین قرار دارد، اما به نظر می‌رسد پکن با تغییر شیوه نگارش نام او، راهکاری جدید برای مواجهه با این موضوع پیدا کرده است.
🔴
روبیو در دوران عضویت خود در سنای آمریکا، از منتقدان سرسخت وضعیت حقوق بشر در چین بود و پکن نیز در واکنش به این موضوع، دو بار علیه او تحریم اعمال کرد؛ اقدامی که آمریکا نیز اغلب علیه رقبای خود به کار می‌برد.
🔴
چین روز سه‌شنبه اعلام کرد که مانع همراهی روبیوی ۵۴ ساله با ترامپ در سفر به چین نخواهد شد. این نخستین سفر روبیو به چین است و همچنین اولین سفر یک رئیس‌ جمهور آمریکا به پکن در حدود یک دهه گذشته محسوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/alonews/119677" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119675">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlLqVwyIOq5Lrj8Ay_4uovsFv85YJ_q4u1zWtkegeElerg1XycSW3qmQXKspTuCUGwG6u7tqS8y1JnM3cOK5GuvBpf0QW6ZzR97OPrFnLnGZMPkWXMdB_s4vYzXLf30PtAszXa1Dmo30gNzxnoZ1vTnI8Lfpv_5FbDVQm76eXqM5mB_IcdYDO-_IpTLdP4_5SNyCxsZDGoo7gkTSGhUGsNFtnVAjd0n57Kk0MqXMYqOPachC14jqiXafSMXJcXlQ09krARIvsMaWImU5bgPUyOSHE55lzMPqYl2rM1zW85YZj5vNTZY09eJapGqm5Tc6yTg1_uqO74HK3nKw1Ns-LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kp2qS8nraJ63o6Glw-zL8wcsWAIPcCupBOK7AzTSsGYNs4mXNWRUtlShV2KpuXLE6YhkmOjmLFqNA7FqmxsRGx6GtZ8S5rsVPAcw_XzriTLRnh3fn2BwqEznz3Eza6z4jXBpX3T5VIymoU5kOyJhZWo9X02Vfwq8dliFVaudrqp30IRAHb8FCFr5dLZSSqu4IGL98scAxhnbCXTHj1QGWhQ_2hYmVRvE9Z1Xga2fWvVrJoLtWxNum1oa_jxF2UlgHZAE-eQxn5svAiw6A6ciLHVZz8Ngtnxax7lyUcR0r0Gy4Bga5Uyt9BLK3CPOVqcqRZzMIMssxhOz2DfodoWfdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله جنگنده‌های اسرائیلی به دو منطقه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/alonews/119675" target="_blank">📅 12:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119674">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
الجزیره: وزیر دفاع کره جنوبی اعلام کرد ، حمایت از تلاش‌های آمریکا برای تأمین امنیت هرمز را بررسی می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/alonews/119674" target="_blank">📅 12:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119673">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنگوی شرکت آب و فاضلاب استان تهران: مصرف آب تهران به مرز ۳ میلیارد لیتر در شبانه روز رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/alonews/119673" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119672">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نیویورک تایمز: قصد ترامپ از تغییر نام عملیات «خشم حماسی» به «چکش سنگین» این است که یک عملیات جدید ۶۰ روزه حمله به ایران شروع کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/alonews/119672" target="_blank">📅 11:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119671">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: جهان ذخایر نفت خود را با سرعت بی‌سابقه در پرتو جنگ «خاورمیانه» مصرف می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/alonews/119671" target="_blank">📅 11:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119670">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رویترز: قیمت نفت روز چهارشنبه پس از سه روز افزایش شدید، کاهش یافت، در حالی که قیمت طلا ثابت ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/alonews/119670" target="_blank">📅 11:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119666">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cRxq1jAEXcQXsqS4QKIdHl7ucLEeXeAj3V0qsFIj05CHY0HaNkqmmUZJRir9jvyd1TQLK0F3n4cjZnyxxdyBAWtfba5k_U4cfrCK1Td6e996kJfu7iGvooKhVi8KVTTSKj1FU71mLlIhcORAR6rB0sZ8R1Ep_2XuBtsKW_-v7kfpgzZZ8gLtQTwqOZJi1jDVmlvgb2O4ZQNSaOiPtfKBlk2nGabedpXIcBzNNQ4J6kM31tgtBZEcvkS8M9m3xObu5YAqZtdOtQ0ntiuyXAHwCHQ3EVVX35OPY--HbM51THDYc8KizrO0_CcwmZMSHw3nZ0YHD7WkF8Rxx7-cdX_Gvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rYZ8aoz7ZFFaq3ePTIaKqMR19c6L3GYgAT1Tyj4hnjsKSLwiW1rblCVz70jkKC1oKd2oGzJvfOjwgXimaWkP4kLz9vjilne9xVMIx6721oLbO8OlA7stnQZLCqYDIP3ZrDq4tldD31vtokPqpB7El6JPFJVPAejiC0qe-4TUql9rIK6JHwp7zL2LCes9tMPAlSalE9sl14QBsCM5ZOGuvJa8m180CE0CgeMM8GX7rLB-qWSdnb-HYge4JGBFEfsR3aXLA4FcoPN1sd0sY4QsO5YnSgTx0Qu-5pr1EpGFLYQK-yMyVzq6GKP9qMAPRgoqJfRPK3cKrOlYx4k0tVsTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PzgGZzX7OAY6FYN7JICHSDrz6ruhoqD0vnbhQJdNPdIwqynAjrdKDzom7htUIIidZfQgRSOxs4aBSQoOayKlqYY3ykBS_xZkLGrJsGcc-F9dmG8jqgLunqXywOR3EcDCv0SDn849R-SGPtFV56R4c8w68ncRK857Yl0J_vSyu_Z3_3Bv4lkTsvmL8b8NfpnaNRwKZI238optW0L5RQW7xNCWJbc31HFNWu99nzFNH3Qng5LqD-cbgac-EueUyOAfel7wsy9RdxF4jUH0JsHW4D8xPWo_EfEMi1LubsV0bn48rXxotVOoEyd_n-tbEI3HZKoENpctFeW2TgCA-aKG0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cTCFGWKhrrzki7Cqy3PMp-PIZQhbkXLo5QSw2ggfEEwz8MQ9PAu3QIXI6lnYXg47CErUcsKzAl0pwwmdXhG_wQQVN169SzY73uC9lzUuXnsKJzBaFdSZRSpTPI4e5bpG3MjjvgnBLMd8Erxkg3tM6IJG4Uwcp_D7FEcEm6-Vhox314Y7GmlXBknb2Yz9X06KV9BAzv_YI5ejNcqtarHhqqaRcBzmJdTHs5Tu9oDWQU1cGoCrbd67dM-bN2Eq-lLbUjqiXuvJ_QSUWbC7u7wEpyrxUd_dIXDDfSA0y5sP8rM0qPE9oyQmc678JKF9RIGfptBjPV65j0ppOnAFx2ptew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
یک اعدام دیگر
🔴
میزان خبرگزاری قوه قضاییه جمهوری اسلامی با انتشار تصاویر بالا نوشت: احسان افرشته اعدام شد
🔴
قوه قضاییه مدعی شده که: افرشته در نپال از سوی موساد آموزش جاسوسی دیده و اطلاعات حساس کشور را به اسرائیل می‌فروخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/alonews/119666" target="_blank">📅 11:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119665">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
به گزارش رسانه های عبری : نتانیاهو امشب جلسه‌‌ی امنیتی محدود برگزار میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/119665" target="_blank">📅 11:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119664">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رویترز: قیمت نفت روز چهارشنبه پس از سه روز افزایش شدید، کاهش یافت، در حالی که قیمت طلا ثابت ماند، زیرا سرمایه‌گذاران در انتظار نشست مورد انتظار ترامپ و شی جین پینگ، همتای چینی او در پکن، در بحبوحه تنش‌های مداوم مربوط به جنگ در ایران و بسته شدن تنگه هرمز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/119664" target="_blank">📅 11:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119663">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f7e26a3b7.mp4?token=Gf21CFFRq1evufanPnhEODjb-NaYB1JvX1YJacDICmW6ITyb7XiGwmEFCooUjO5AWzWuwvkePgX8dAZtonTcQIEDuJ7CGZ1_STIqVdbf0n9EdmwqoJCgG3qk-_TJ_35Rm_TCCIE6Mf5OqaaGFNM_DHWF9p_jvaTMy2cB0exrPbNDryJus2LQJZb3uVoCerItMvQQLhWR8U2YE7Sf3sm0FLC1obgKiexRwS_nMMW1YjG_8qGkJS7kWB7dw90B0u9_uhzl_11fBx3KCYPeH_pGLDro_YzPxXW1cxqTK4ZXXeSFAAP2AjfOXd7t2fVqtDoqDBWR8kJzFLyG_WPJrhqkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f7e26a3b7.mp4?token=Gf21CFFRq1evufanPnhEODjb-NaYB1JvX1YJacDICmW6ITyb7XiGwmEFCooUjO5AWzWuwvkePgX8dAZtonTcQIEDuJ7CGZ1_STIqVdbf0n9EdmwqoJCgG3qk-_TJ_35Rm_TCCIE6Mf5OqaaGFNM_DHWF9p_jvaTMy2cB0exrPbNDryJus2LQJZb3uVoCerItMvQQLhWR8U2YE7Sf3sm0FLC1obgKiexRwS_nMMW1YjG_8qGkJS7kWB7dw90B0u9_uhzl_11fBx3KCYPeH_pGLDro_YzPxXW1cxqTK4ZXXeSFAAP2AjfOXd7t2fVqtDoqDBWR8kJzFLyG_WPJrhqkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرودِ هواپیمای ترامپ تو الاسکا برای استراحت و پرواز مجدد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/119663" target="_blank">📅 11:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119662">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
با اعلام قوه قضاییه جمهوری اسلامی، احسان افرشته به اتهام «همکاری با اسرائیل»، بامداد چهارشنبه اعدام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/119662" target="_blank">📅 11:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119661">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
بلومبرگ: نرخ بیکاری در فرانسه برای اولین بار در 5 سال گذشته از 8 درصد گذشت.
✅
@AloMews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119661" target="_blank">📅 10:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119660">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بلومبرگ: یک نفتکش بزرگ چینی در حال عبور از تنگه هرمز شناسایی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119660" target="_blank">📅 10:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119659">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iCRQ7yNUq3ZPIv7tM4hDiZVx6aIN5WW4Lw9EdWxGlb6RM93BoBwRhupuqH4nl36olh4JZW7WTvuYxSV2cLUNWAfoMqEt_YYJ5nK31nCClJxQANUeUvTJoIJtNa4jiTn9TZuvv57a-FkfUOujeH0AIJu64aYswlMX47ygPsu0zCDAi2oFClaxEATRs6sHIFxk6lCQTpq345g7dgg6o0TqkTp1rJ4cqAGsQWPM8ZkmQV5RVa9MBlzY1t91AWi8oXnmMypMdICKUbKolTjRiFWOxaVT4AvLo5EH-IZTSdecSn-xJSnt4-fqn8_P6ohJWAeq2je3bicgLfh8jWPcFNv_6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تشکر اصناف و اتحادیه‌ها از پزشکیان برای جلوگیری از توقف کسب‌وکارها با اینترنت پرو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119659" target="_blank">📅 10:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119658">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر اقتصاد: انتقال کریدورها به بنادر شمالی و مرزهای زمینی در دستور کار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119658" target="_blank">📅 10:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119657">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
المیادین به نقل از لاوروف: روسیه پیشنهاد تهیه پیش نویس بیانیه ای از سوی گروه بریکس در مورد وضعیت تنگه هرمز را ارائه کرد، اما اختلافات ایران و امارات مانع از آن شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119657" target="_blank">📅 10:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119656">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRXlgfbmTb0AEI4nH-nhHWECqp1D_f5CV8-XjHIvJfgCQIeQALATyatV2JH0eKBxV0dAm9FA2hFR7__DBt3DYBJpjaJcq1jtbHJ8cnrR8I7ChuvP8-6G1Cqet2i8N3cFpAKmOmqYHBXBmIdRt5Xq4EMRAacP5VcRR0IBFZ_2PEc5GNz3W4ntxA7vuKNBN1PkZUag2cScmnhddRJbFeOTDhKsaCI5eoX2lCkb8eknc2p95hMtwOWi6LwJuziIzMbQGWbFqfrWAfuCCBJzijeIwPj5GXsWFr30G93RVwj5cK01B4mj9FsF9zS0vQj4lijnXawyh2j3SYIfcho2xzatpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه NDTV تصاویر ماهواره‌ای با وضوح بالا (تهیه‌شده از شرکت Vantor) منتشر کرده است که به‌نظر می‌رسد گزارش‌ها مبنی بر پناه دادن پاکستان به دست‌کم یک فروند هواپیمای ترابری نظامی C-130H نیروی هوایی ایران در پایگاه هوایی نورخانِ نیروی هوایی پاکستان (PAF) را تأیید می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119656" target="_blank">📅 10:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119655">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
روزنامه نیویورک تایمز با استناد به ارزیابی‌های اطلاعاتی طبقه‌بندی‌شده آمریکا: ایران به بیشتر سایت‌های موشکی و سکوهای پرتاب خود دسترسی مجدد پیدا کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/119655" target="_blank">📅 10:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119653">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKJIdBtI8J_7IqdKINe2e5UVg52BPuE32QjlQnElCX3ggGB0BXrQ0HYooAnm_HBAzGSgPeHi-gK_Xxvax_36jH4M0F6VL0l4qsfOYlAuMraupwph4aeboTiug8IaZMJ7E1P6DILGZ-O-bqlwOurwiwUMUiyCsGh0sR2iGFV-NGbVgkAD96oMAFdYJD01RY5GJO0eK_RfPX7Jgbp0cOZfk8oFTXC_-dnk4jArM2ZC8mONBpnIu-vveESCeA21FOnEBQOf6qaCU1B_16XLBzCfjTG3qrmwpdrbo77Zn_8wYenSR7iH2Bya1y6jHoQmUAezIrGMNNZz7bSi2_hIxm9lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q141jBEWtSJud9c3TgJdlRdNHWcwd2sKKmYyfFkUrZgYTW1N43W1h4xurCoX6KMlnIRC_0p1G2PMj8WqWSSLgF7R5yrCBGUuDejp9PUBPAvLrbK-t1vhMMwtqjUL6TFiidnGA0hQsEsBOuaC7pEr7nHADqlQcsuXIchvhm3SRpoIebx1jZsX-ccEn1rM5lRWvkpOVe1srFU5YkVWoeDrbehjjwOnUaVfTCZD4Aecul_XeeaqA61Kik0MnHLOuDMTGPz6KBA18_3grN8jaSCL7a-OudjvVLagPAmOoi1Bws7yxWw6qghM31v_uK5z1iURdqY-oG1HMIfIK02LQSxWhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مارکو روبیو توی هواپیما برای سفر به چین مشابه ست نایکی رو پوشیده که که مادورو هنگام دستگیری پوشیده بود
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119653" target="_blank">📅 10:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119652">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUij0_j9DGFarQoa8HRKTbO5r8Xpn11SbsxRxsqgf1xc4-xpA-VTDG9q9x_25Bkobiu7Pg2NxlcddEEDMJgVP_e8sNgwWd4XAR82gJ18uyAHNh-ZT9odfLuSB96h4H_xoILMtimQItNWFSrZzhUXXBfXUn9umqf8sBiFz-DDQCdtVk7553V3OXBkqmy-btzJ2nCHoMfQvjHBDoc_eekZeV36TnUzmQU1HovoxMe3yFL2aIOTrOO8DKPHz_TCHBhEm3BuKX9y5ub-yKueQwjeElAUr7LB40V1tbpUEpSPZ2sFJa6mxf7ixN2fUWwtwtp2XrstXoPL3suEqOuEts4a_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پهپادی اسرائیل به یک خودرو در جاده ساحلی جنوب بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119652" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119651">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سی‌ان‌ان گزارش داده، یک کشتی باری روسی که دو رآکتور هسته‌ای حمل می‌کرد و احتمال داده می‌شود مقصد آن کره شمالی بوده باشد، در شرایطی نامشخص در سواحل اسپانیا غرق شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119651" target="_blank">📅 10:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119650">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دلار هم اکنون 182,000 تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119650" target="_blank">📅 10:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119649">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
لاوروف: اگر درگیری در تنگه باب المندب رخ دهد، بخش انرژی جهان آسیب زیادی خواهد دید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/119649" target="_blank">📅 10:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119648">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در محدوده بهارستان اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119648" target="_blank">📅 10:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119647">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ژانگ هان‌هویی، سفیر چین در روسیه، اعلام کرد که در 7 آوریل، شورای امنیت سازمان ملل قطعنامه‌ای درباره تأمین امنیت کشتیرانی در تنگه هرمز را به رأی گذاشت.
🔴
چین و روسیه به دلیل نامتعادل بودن سند، به آن رأی منفی (وتو) دادند که از تشدید تنش در منطقه جلوگیری کرد و شرایط مساعدی برای دستیابی به آتش‌بس موقت و آغاز روند مذاکرات فراهم نمود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119647" target="_blank">📅 10:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119646">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tldv8fo59SONA6Op6SN63QrhJGE663qvrp1XlIeKQnXECbBKYDl5BUpjvy1lwtqyGUxLnvvyvZYkAC9Rh-5gVaZzIcuGOlLFXLinCyKBt6e6gPWBNO9lPcTKtC-F2jR3t4A6XQQOWrHX7O-p02yc_pfrNzMHyO_jP1OB9RIb6BPLUhBdASMm0Rmo0h2mG9AnVifvsK6MBnXrdKTHaxeg0eJUlcMF4NyDYWYcJTiYMIH_pGZznKtMNORSilEZELWUng_owIJ9njKWyH1uc7-82K7hUulyGooXt3NTr0vXYzBxnCACZu4rwpLRMfnmPmdJge4ERADqW3pSxmXOQaCQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ نسخه‌ای از پوستر نمادین جنگ جهانی اول «من تو را برای ارتش ایالات متحده می‌خواهم» اثر جیمز مونتگومری فلاگ را منتشر کرده است که خودش جایگزین او شده است: «من تو را می‌خواهم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119646" target="_blank">📅 09:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119645">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941b50d546.mp4?token=Qgxa6XqccpkTFJUoT0s6WKrbCcKxvZKp8E8Rs4MeIpmWUZ3yC_Q4E_PpVCnct6fulmtKD0HhiXAsihbsNBdeT6XmhI3_WZ5ffgH0-H6nO_IddMyf_U5O4obJ8G18UW5HhLaEoOxLWsjI4KTOk4vGzpvvsNrAKBboGswmSPWUpLdUGf8q3ZBJvo-vh8EA5hW-OHqyGqhNLXNEco4el9LvhEXipVQcYkQGNMvCvgL5A6Mbu0IJxDDWu2YkIIyA-N4sYAOPpxrp1hZD_SFVAacJ3YpZM15j7iowS5jcsPt5xsMHXRCd-2DQo6KJ2w-jj3WbpkJMzy9zZjWYpSBDHG7GBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941b50d546.mp4?token=Qgxa6XqccpkTFJUoT0s6WKrbCcKxvZKp8E8Rs4MeIpmWUZ3yC_Q4E_PpVCnct6fulmtKD0HhiXAsihbsNBdeT6XmhI3_WZ5ffgH0-H6nO_IddMyf_U5O4obJ8G18UW5HhLaEoOxLWsjI4KTOk4vGzpvvsNrAKBboGswmSPWUpLdUGf8q3ZBJvo-vh8EA5hW-OHqyGqhNLXNEco4el9LvhEXipVQcYkQGNMvCvgL5A6Mbu0IJxDDWu2YkIIyA-N4sYAOPpxrp1hZD_SFVAacJ3YpZM15j7iowS5jcsPt5xsMHXRCd-2DQo6KJ2w-jj3WbpkJMzy9zZjWYpSBDHG7GBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
براثر بارش شدید باران و وقوع سیل در استان سامسون ترکیه حداقل ۱۲ نفر زخمی شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119645" target="_blank">📅 09:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119644">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
احتمال شنیده شدن صداهای شدید انفجار در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119644" target="_blank">📅 09:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119643">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
الجزیره: ۱۱۲ کشور از قطعنامه آمریکا درباره تنگه هرمز حمایت می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119643" target="_blank">📅 09:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64e8e7d0d.mp4?token=LqXfOBgc6o0-sGOeIvkdOwouBBh9YXKNBe-9yE0n3qmUagqrrCQHqa_KXPMduRE4h42nDsMdPTJoUWjPqUFfk8C903EKybSlPMNNLS6nkKiq3kHK2V9VJl7vXz8wqJjg-FHHNjffPhdTgCjhh4T8sMlmmQhzLsm1sDMOdENmLrwa65-xFZAunv6cpTblPR87HEeHi0FmmAcTuc7HMf5pUeNFEiG7vbbEfciHXxElPU4FL9Qvzsib6-9qdPU83dqiBQzc01r0xDAU2VFiT1rcpODsJjObN15M2wU_CWkM8lLsKhf5A6YgOeDd5LwpGivHkpK2hn4eM59n06wmqGKK4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64e8e7d0d.mp4?token=LqXfOBgc6o0-sGOeIvkdOwouBBh9YXKNBe-9yE0n3qmUagqrrCQHqa_KXPMduRE4h42nDsMdPTJoUWjPqUFfk8C903EKybSlPMNNLS6nkKiq3kHK2V9VJl7vXz8wqJjg-FHHNjffPhdTgCjhh4T8sMlmmQhzLsm1sDMOdENmLrwa65-xFZAunv6cpTblPR87HEeHi0FmmAcTuc7HMf5pUeNFEiG7vbbEfciHXxElPU4FL9Qvzsib6-9qdPU83dqiBQzc01r0xDAU2VFiT1rcpODsJjObN15M2wU_CWkM8lLsKhf5A6YgOeDd5LwpGivHkpK2hn4eM59n06wmqGKK4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل فیلمی منتشر کرد که در آن نیروهایی که در جنوب خط دفاعی پیشرو فعالیت می‌کردند، یک شبه‌نظامی حزب‌الله را مشاهده کردند که از تجهیزات نظارتی علیه نیروهای اسرائیلی استفاده می‌کرد و طبق بیانیه رسمی ارتش دفاعی اسرائیل، این فرد با آتش تانک هدف قرار گرفته و از بین رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119642" target="_blank">📅 09:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQl6Q286MICoPjuUbwHWAfZj_YNZVCG7dzPWZ0Hg3W3NPszMr2CUNvueKXWgNfTrE0d823ti7g6i6FfjI3o1fcyRFMZEdm71hgxuvhnZqDh6BExVNgCZic6xvP28wfYQ3y1uLkc7tPTUevRZU3PVMIPZssVCvVL7DT_YmrNZkfTugB-GYDgXuaHTdPNpVPCinzQ5BiYV9G1V38yD2LcsRv0cG-OvBk4QwupKXndn4K7PkaUJEi0DQ_o6SOykOK_fkH8PqpP9MoshmIvcL0piQrL4JocA9MZfWwQ4ytUnI3Qh7qGvvtcOBzasa3ev09jJqIOiyXrDSYM9nAn3Z7JnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید در ابتدا فهرست مهمانان رسمی را منتشر کرد که مدیرعامل انویدیا، جنسن هوانگ، در آن نبود، اما طبق گزارش پولیتیکو، رئیس‌جمهور ترامپ در توقف سوخت‌گیری در آلاسکا دعوتی در آخرین لحظه به او داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119641" target="_blank">📅 09:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oksM9Qhy8RXbMxkm-PMT3txoUgt_0PxfYANmCLjImEA_2sbaapnmPZc7sDVA53Unzj1bFu9XFwHimWDDNHIRzi_YlZPEzTEnZh1DLNbT4NF5z_PjM-rzp-EQqpkZ9-61OQtpq_-TUibTkxM6AlB7k-lnfGUrR6IJqmwXn0Cgu3b4ukUw6UNcppNtezGpbIznOKThFkbJw4JuwSEPDxKxixkcjjHhzrFfJpM9PXbitVyAhlkUCjcgTsj5y8AHXH0Q27GZrd_xUnP6_Ggl5m03bTS0Ov3N3SCtWQKlzHhk04gMHdfd3VYwz3KB8NsyIYMU32-HGEv1yk1ZXq_ckELdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی
CIA، لیز لایونز، گزارش سی‌ان‌ان مبنی بر اینکه سیا مستقیماً در ترورهای هدفمند عوامل کارتل‌ها در مکزیک درگیر است را
رد کرد
.
🔴
این گزارش کذب و توهین‌آمیز است و هیچ‌چیز جز یک کمپین روابط عمومی برای کارتل‌ها نیست و جان آمریکایی‌ها را به خطر می‌اندازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119640" target="_blank">📅 09:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ مجدداً تأکید کرد که آمریکا برای پایان دادن به جنگ ایران نیازی به کمک ندارد و تأکید کرد که آمریکا یا به‌صورت مسالمت‌آمیز یا به روش‌های دیگر پیروز خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/119639" target="_blank">📅 09:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NM0nLMXdG0RpaYQOlPLApXv6HC_KfJuihgKOqLtH5aE4lGCL6uc1CVk9CDJgRp7E9CgVG8grrv9MSVMzmeE2AWpH64ypYisY6Ftqpn6vfrn2kD5Fd2L2JNf_Zyh5yFJmPmSE8n_omYzsx3_5DsA8bZ2TkNYW_0JgIef0k9VhHdjXL68y6ZTUiJxBjuiBlQouP6h-HSPiKBKBQZFoJVdwlaP1RwE6zoojcM6g0g7B_nv3T1aQMn1txrWmY3RHb8GUlmdZOK4FIrr0FHv1CO-0pxhIE5r9xzOqkAwVnJVrcbLJZ_39rxqWURbXXJ4LLKvHmYDk0S7aVI0G867VAbIXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آواکس امریکا درحال رصد مرزهای جنوبی و خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/119638" target="_blank">📅 09:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwvtPE2sEKWGRiBTRAHaW19rQi-IP3rkF5xuP7tZLiRGhcOmzr3p4JehcvWonRajSS-OJbtNWOL4s7MT0gunybu7_bD5k9iYb26BhSxeVlU2LQDv2NPiM4nik-m_wVl4u7v212K_GdkTPlYsB4tz2sOFlohU2qDS_xwG6tlPahYBcDHrVRj1-rsLPUZbUmaHMZnULjOO1TnCfbdtkpy2bChnGw9u1r1zqW3PppoB0Byruld9eDeP3pTkddE2PftVGH_msBmM-26XKryGEzGxLiFdQDvI7W8fqwlybOkPCRdpnk-4K2jnNV6aJU9TE6n09s6hbcFWcjmGkGXccCuEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۶.۳۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/119637" target="_blank">📅 09:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سی‌ان‌ان: اختلال در تأسیسات نفتی خاورمیانه تهدیدی جدید برای جیب مالیات‌دهندگان آمریکایی
🔴
مقامات وزارت انرژی آمریکا پیش‌بینی کرده‌اند که قیمت نفت احتمالاً در هفته‌های آینده بالای ۱۰۰ دلار در هر بشکه باقی خواهد ماند. طبق جدیدترین برآورد اداره اطلاعات انرژی آمریکا (EIA)، میانگین قیمت خرده‌فروشی بنزین امسال به ۳.۸۸ دلار در هر گالن خواهد رسید و سال آینده ۳.۶۲ دلار پیش‌بینی می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/119636" target="_blank">📅 09:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3402d146dc.mp4?token=CpxY7ryO6Vm9KzJbgNGpdh0z1TOzDX7d157cY-CaosLJqsA4bJ-D_GAi6Q6SVSwRP_M_BDHrqpS-jdRJ_D1Ga18WHyR0_k2jLIR2yvcJukJ6tCf9cQZuCHHMuAiWEa3N9FVhthW2sbqzpjw4IixN0PPYHA5cZQ-LLoBQPCJySbKjQtFmfk0BGRQPpN93bksHO0TIXdCpP4DxHWmgywgVDkx_ejoyT6ow3-bA_mArozp1H4FxCIx0h7p65hrtQNNcYHoCP4cLq8ZR_4PX5Sx_22NDoFyJDVkFdD9mvy1L7ArOO8EKXpDmuFI1pL8vddNyxJQtvPQnf83t6TegT3vV3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3402d146dc.mp4?token=CpxY7ryO6Vm9KzJbgNGpdh0z1TOzDX7d157cY-CaosLJqsA4bJ-D_GAi6Q6SVSwRP_M_BDHrqpS-jdRJ_D1Ga18WHyR0_k2jLIR2yvcJukJ6tCf9cQZuCHHMuAiWEa3N9FVhthW2sbqzpjw4IixN0PPYHA5cZQ-LLoBQPCJySbKjQtFmfk0BGRQPpN93bksHO0TIXdCpP4DxHWmgywgVDkx_ejoyT6ow3-bA_mArozp1H4FxCIx0h7p65hrtQNNcYHoCP4cLq8ZR_4PX5Sx_22NDoFyJDVkFdD9mvy1L7ArOO8EKXpDmuFI1pL8vddNyxJQtvPQnf83t6TegT3vV3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه فرود هواپیمای غول‌پیکر نظامی سی-۱۷ آمریکا در پکن در آستانه سفر ترامپ به چین
🔴
احتمال این هواپیما حامل تجهیزات امنیتی، تیم‌های حفاظتی و دیگر دستگاه‌ها و موارد پشتیبانی برای  آماده‌سازی‌های ویژه برای این سفر دیپلماتیک ایجاد کرده است.
🔴
هواپیمای سی-۱۷ یکی از بزرگ‌ترین هواپیماهای ترابری راهبردی ارتش آمریکا به‌شمار می‌رود و توانایی حمل تجهیزات سنگین نظامی، نیرو و سامانه‌های پشتیبانی ویژه را دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119635" target="_blank">📅 09:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggdifVzI0eR7fQtd_9zQbqQc4tzZH8d-WU8WAvSarZnrGV0NLRt_TS7hXf-iHT0He64TLELdkMAzr8QKxelovtEgw0EivF1WfU8OgU9-Lm36JScRaHO9kid62j1XPzRf-Cne6XfWLvwLUatQnZpHOtIgfNbrJvgJXjfvSCY9Bs61uFNWcbfBnLR0ZpxlQ_uv0sT5qkLm27Y1fI6gpVAZbA7H1eO0xzQIR50MmNX_5yunBHeJc_k0s4LicpN8o1y-bH2ywI5arr5TMAzyWIL9-C7kFqksoXDvfve9x39396qf6hXtE5GcFXz5e6kZCp86qbivOMSJzmfmWLsnf1zPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ ساعاتی پیش، نقشه کشور ونزوئلا را با طرح پرچم آمریکا و تیترِ «پنجاه‌و‌یکمین ایالت» پست کرد و سپس به یک خبرنگار فاکس نیوز گفت که در نظر دارد ونزوئلا را به عنوان ایالت 51ام آمریکا در سالگرد 250 سالگی آمریکا معرفی کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/119634" target="_blank">📅 09:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کیهان : مذاکره کنیم جنگ میشه ، مذاکره نکنیم جنگ نمیشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/119633" target="_blank">📅 09:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نیویورک تایمز: ایران هنوز به ۳۰ سکوی موشکی از مجموع ۳۳ سکوی خود در حاشیه خلیج فارس دسترسی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/119632" target="_blank">📅 09:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7swM9MbjVjsF3Izn3zMHq7Y6xG8EDoU8Br_8mR5PXpp_YNiPgw-KvuIA26xoAz6pfInQZEfWNUdNykqiJOpr80-0f4czBAZcJIhEYLAqWWg6WKX3o8RSeyW_kycaxgW6-AwyvJwdfIAXo9L5FXDtb6XH-fnvWoWA3TYijFSRbTDFAVH3j3T2R3310Cno304tl-Sh0s_gLrnOR2ZYP6w1vBpTiVTT6c38bIR7S7kVDzRH8Q2aI_b7tnTaNzyWHb-ZFj2H4rLP_1JM1RZafcmB_AF6zlF4bYrSsOKj7AxKJ84TnGop1QzprKtikaxUx7OP1bh0mx1Y9N-zPrR0eXR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تهران امشب رو ویبره بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/alonews/119631" target="_blank">📅 01:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b1310b3d.mp4?token=CWmfZaTaDYwwbfLDT-1sq6iW3U5RDBKmSG89YRMeiwilgawEHCM9MQWiPnnuIy_3PnWCPkWkt7uSipLeKg1EM5ICiT7HHr3BpmFiY_FEEl41YAyJBkU8YAZmsHJsXCrRvI4Vp7kuyY35pPKx69s5a-EhC9l7BduaomBPFJTKEPrjl9t0-PA1PHP7hGskiQ0M4ORRx8-qnqGGxkwseVljQ1qfEPMqHF_V5m9Vs2qtWNZ-6lJdwhE1WSdPl_H8KwcSTBKxMkAQx4E4hLX87wIFxZ3afgdMsUBREiVpE7NlqGHUizNv1VvJmP_h9pBlJIqRt7Jcf3N5IRBLF9WlsTijwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b1310b3d.mp4?token=CWmfZaTaDYwwbfLDT-1sq6iW3U5RDBKmSG89YRMeiwilgawEHCM9MQWiPnnuIy_3PnWCPkWkt7uSipLeKg1EM5ICiT7HHr3BpmFiY_FEEl41YAyJBkU8YAZmsHJsXCrRvI4Vp7kuyY35pPKx69s5a-EhC9l7BduaomBPFJTKEPrjl9t0-PA1PHP7hGskiQ0M4ORRx8-qnqGGxkwseVljQ1qfEPMqHF_V5m9Vs2qtWNZ-6lJdwhE1WSdPl_H8KwcSTBKxMkAQx4E4hLX87wIFxZ3afgdMsUBREiVpE7NlqGHUizNv1VvJmP_h9pBlJIqRt7Jcf3N5IRBLF9WlsTijwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور مردم در حاشیه شهر بومهن پس از وقوع زلزله امشب
🔴
برخی مردم در خیابان خوابیده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/119630" target="_blank">📅 01:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnMcqjkJI2OARX7M9k3ZRVbBYd7Dpe9csZTpVxDPWeeqWPyWPHrmkzBYG2rfxr3Ibzs7u1RHP9uK-VHhkMkeT-hHhaWkQ_Pn71mnFSrtoCu1_63DY9LPBFzVJGE0xj3a7qFn7XeyNVq5Vx57QJCmzncH32ALPJBJbJWqcMiiJNtvjLbgLf4bzPPn_6P6cdVk0M2CE5D9gpnGdBTFzaBtDNOiY60zzT32PDkwBNOw1ecoxVs6Mlk-8vBTwc1k7q-MP30QPOQZAV5QCMNr8Bomb2_yUemvb6IgtpLuetVNyN_C8m7uPSpDl-DBBWLjIesTg-eq3XB3fuHnQRJext-SUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: منابع میگن عربستان مخفیانه حملاتی علیه ایران شروع کرده و تنش‌های منطقه‌ای هم شدیدتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/119629" target="_blank">📅 01:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vp9VZf79tk6LdWtjCZleW00P8OBS_0IdzqHdwlxEoVq9qR83gP-elwikWHsegiFa3vK_mESFFnW9UmwbfMNRcBJCTVWWuIHCynz12Rt4psh6np-u02TErEqjoiCtCcCmYJZHF6pc3MeVvcNTaHzBn6DyQJ60TpM-SoRVtm1467tQZy_XS_51D6VCwhjdrXWMSPkS9_5zGKCqpBic63XS88Nf-BIziHY1yGZX9nMcNoL7WuMqIxDWHDCN5oSfaYZbqKUly-c9y3M0CxplSqH8G80v0RNKGKaFo15wTwMqISsYd6pUriGbhLpyx54FQjY0VQXWnh1fsZd5nd23zioCEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به سی‌ان‌ان گفت: اگر توافقی حاصل نشود خوشحال خواهیم شد اگر محاصره ادامه یابد خوشحال خواهیم شد و اگر چند حمله دیگر هم به ایران شود، خوشحال خواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/119628" target="_blank">📅 00:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
طبق معمول پمپ بنزینای تهران شلوغ شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/alonews/119627" target="_blank">📅 00:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
گزارش مقدماتی زمین‌لرزه مجدد در تهران
🔴
بزرگی: ۴ ریشتر
محل وقوع: حوالی پرديس
زمان: ۲۶ دقیقه بامداد
عمق زمین‌لرزه: ۸ کیلومتر
🔴
نزدیک‌ترین شهرها:
۹ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔴
نزدیکترین مراکز استان:
۴۰ کیلومتری تهران
۷۶ کیلومتری كرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/119626" target="_blank">📅 00:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
چندین پس لرزه خفیف در تهران ثبت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/119625" target="_blank">📅 00:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119624">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
عوضش اورانیوم ۶۰درصد داریم میتونیم بزاریم تو شیشه نگاش کنیم و روز به روز بدبختر بشیم
😍
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/119624" target="_blank">📅 00:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری/زلزله مجدد در پردیس تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/alonews/119623" target="_blank">📅 00:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119622">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
مردم تهران باید امشب رو هوشیار باشن و زیر وسایل خطرساز مثل لوسترها و پنجره‌ها نخوابن، احتمال لرزش‌های شدیدتر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/119622" target="_blank">📅 00:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119621">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
پس لرزه‌ها تو تهران شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/alonews/119621" target="_blank">📅 00:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119620">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری/زلزله مجدد در تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/119620" target="_blank">📅 00:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKfdt7b3wWGcKDRz8OVrwlfUReyXxAU3kwSPrS9UtfxRdXG1pz5HHrZSRNh92QhmV78a841xfTF4Zu3ix8l02UYQwh34npSHZ5t4k9yRn_VQWIiB37pS9S-HaoulERHPRDonCuaBCzzH2ydMzet4hdYvdvCQ2VKw9S6HK2b8QO4xt-CFBh--GXb3bQTgbXPMvof6Dxzv0Meac9FWbpyD9GK8AkRwBBaOgmJ79DWrSTSyfhD8vQXesp-ojcLqIFYYxFywrdS3szVpKBobERVRUOCsNISXUe96RRTKwetsfyhhk6PCNcbHYfM6Ab19V2bog4XwKCRhEX_PwTsHapuMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مردم بعدا میفهمن با قطع اینترنت چه خدمتی به ایران کردیم
🔴
دشمن برنامه‌ها داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/alonews/119619" target="_blank">📅 00:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119618">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
⭕️
⭕️
حجم 1 تا 100 گیگ  بدون ضریب با لینک ساب بدون قطعی سرعت بالا  و ضمانت بازگشت وجه   قیمت هر گیگ 235
💸
برای خرید به ادمین چنل پیام بدید  خرید آسان و راحت با کارت ب کارت  ثبت سفارش از طریق ربات:   و اگر تمایل به همکاری دارید کافیه به ساپورت چنل مراجعه کنید…
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/119618" target="_blank">📅 00:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سخنگوی اورژانس تهران: در پی زمین لرزه در تهران تا این لحظه مصدومی گزارش نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/119617" target="_blank">📅 00:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhJvAOaji6kJ3-3bPbdv5B7i3z4N62pIeVU0fT4B5D-YEkbLOnfApeBTTeLOZ20eUclmILOpV3_rUOCtU6jo_Y10FRxnEYvOwSJJQ4R6G0uMsH6ZNVWwybvnuAdikYGqJkcNUu1uGDseP7M5mRz1HHQwHbX7GoLHjKTSxD4vud2n5P-3if5xvjaJ1QG9fDINzKTwWOF_P9hpTqPeTpa7VbcfDfmEIdxfKAgCIQQHSfFn8iNv2LhVaocv0KeZ8Rt5f0LAI8M0cZxKuWZNIFIAcXInF-V6-i01lrxZXHkKBQwERqeJ4SRamPBYlObSVKClSMjvbkEHJ7U_ykXZ-oWDRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در زمان زلزله چه باید کرد؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/119616" target="_blank">📅 00:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119614">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS5Oo3ludhesBm9dG1r5XwBW74n46f1KBsL9U_20Cdx4z69NE68prG_FE5kwkzhGIGaAXhfxNVeS0beu1ZzKZbRVNxqhLDcGM-ucYrt4Q-uFG4YH5dKm617h9wN8J5oZLmw3pPyqyxDvotIXH_zkn-0Hdl1vePb2MjXocN0wXS8Fw51up2i8yPccLuQLISAPILWFQeSkB0VIAN27NoKvB5aTsvyHb5As2CAhdW5QPZcUqU7l-dtUzJERgtuLc1MjN-wp62WkmT8EHZqv17ge4wndQvm-y4fbdj7_uDS36Un0fh3cUFNTRWLMQxhV2bPGTRaNzVPGag1jJo433esgNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانون زلزله لحظات قبل تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/119614" target="_blank">📅 00:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119613">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مردم تهران امشب هوشیار بخوابن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/119613" target="_blank">📅 00:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119612">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8qmvaGZPa6U5vBtgz07m9x40G_zVhr9Ro2Iznq6MzsN4ZFw6TC1FiVwyJVPY1qr2J4NAFSsP6L4xVbP2DNGGp4m93GtiOmuJhJJn11XcT50hMujugZFx5AM0G_H0WbHN66lF3ZYRlvgZr-VXSfyVogx9AEBJE2jvhfCX5KbqcOAMJeQypNwKAByxPzIoh7xibhuQ3TjLIhIyhHf1BV2NDG9jj32Wcy-WBWAKii3P2ivybhpttpinvyKafDPxcc8od-NUAATNfftCCSUqhrEb4Byesdnxl6rPGrzFPdNUS3vPdGHHOXgOSyVZJQ15pIdTe0-eE8KYFXB-SS20hj6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: وقتی اخبار جعلی می‌گویند که دشمن ایرانی در مقابل ما از نظر نظامی خوب عمل می‌کند، این عملاً خیانت است چون چنین بیانی کاملاً نادرست و حتی مضحک است. آنها به دشمن کمک و یاری می‌رسانند! این فقط به ایران امید کاذب می‌دهد در حالی که نباید هیچ امیدی وجود داشته باشد.
🔴
این‌ها ترسوهای آمریکایی هستند که علیه کشور ما ریشه دوانده‌اند. ایران ۱۵۹ کشتی در نیروی دریایی خود داشت — هر کشتی اکنون در کف دریا استراحت می‌کند. آنها نیروی دریایی ندارند، نیروی هوایی‌شان از بین رفته، تمام فناوری‌ها از دست رفته، «رهبران» آنها دیگر با ما نیستند و کشور یک فاجعه اقتصادی است.
🔴
فقط بازندگان، ناسپاسان و احمق‌ها قادر به ارائه استدلال علیه آمریکا هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/119612" target="_blank">📅 00:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119611">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
گزارش مقدماتی زمین‌لرزه
🔴
بزرگی: ۴.۶ ریشتر
🔴
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
🔴
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
🔴
عمق زمین‌لرزه: 10 کیلومتر
🔴
نزدیک‌ترین شهرها:
🔴
8 کیلومتری پرديس (تهران)
🔴
10 کیلومتری بومهن (تهران)
🔴
11 کیلومتری رودهن (تهران)
🔴
نزدیکترین مراکز استان:
🔴
41 کیلومتری تهران
🔴
77 کیلومتری كرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/119611" target="_blank">📅 00:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119610">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
تمام پایگاه ها و هلال اهمر در تهران به حالت آماده باش در اومدن، تهرانیا امشب حتما مراقب باشین و از زیر لوستر و دم پنجره فاصله بگیرین.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/119610" target="_blank">📅 00:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119609">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
شرق تهران باز لرزید
🔴
اهالی مناطقی در شمال و جنوب شرق تهران از لرزش مجدد این منطقه خبر داده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/119609" target="_blank">📅 23:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119608">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/مرکز لرزه‌نگاری:
لحظاتی پیش زلزلهٔ ۴.۶ ریشتری مرز استان‌های تهران و مازندران را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/alonews/119608" target="_blank">📅 23:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119607">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بعضیا میگن تو شرق تهران تست بمب اتم در زیر زمین بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/119607" target="_blank">📅 23:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119606">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ایرنا:
در تهران هم نزدیک به ۱۰ ثانیه لرزش زمین به طول انجامید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/119606" target="_blank">📅 23:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119605">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
امروز پردیس چندبار لرزیده و نکته ترسناک اینه روی گسل بزرگ تهرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/119605" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119604">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
این وسط فقط زلزله کم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/119604" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119603">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef9a6ce7f.mp4?token=v6WX1TO1lwJvICDB3KgpaQWuSR8N4ZHhpi2P0DYQwqf0Z5g5AYky3Kg9oGL6qj5HNazPFLVQaiZY8FWr9VWmMi7AAziuHUTnY5cZjyeJ-TXtbGMJC3tTvMGGoxc02QLkoMsKX_Qwgh1GdvUu2-SYH8McEUt7EyKnsykNbmgT66IdeQju482EBDsjGjWD73tRqTGlMCWx5fJU1yzuIiJIGos3AfpXtqKlM7j8oLmKtM84UoNOG56xKiedwIF06nMjKzwgWEXhbPhabaand75PGTeaFVif0jz8wPYS17jc4galowjA-PvTVqrSCyHZ6yoHQ5ciT-59d7F5IvNFav8ZmSO-ZGBPGKWGJp0r8C7cH3aJWM5X0Os_k9S-slKcze3Qw_O4R568CpYDZLjk3Ky9h6SVcVTAgxHLzux2J7C3OYI_-y0bvkwDwdYQlDC43pMiL-tTruY1ginpthiafX4zOsYBJo6Ds2-68Tv10ofrZ3j0kLVwXSFOMW4EMMxXU_KSYVSxpWm_qTOZhB3Yi8nwmIMfS8GDM9ChbwAUpVW1VOaU54N2D6imsmzPHmu-MgN8H9y18HMsXHi8tVQy5jwPcnQ--uxmc0axuCGPZTDnx1caY2WV4Hd4fbbUFXc3IhvEhlqR-MlFGf9ul0-ZEoOjIgLRDuhi4JaHjTRZBphfk1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef9a6ce7f.mp4?token=v6WX1TO1lwJvICDB3KgpaQWuSR8N4ZHhpi2P0DYQwqf0Z5g5AYky3Kg9oGL6qj5HNazPFLVQaiZY8FWr9VWmMi7AAziuHUTnY5cZjyeJ-TXtbGMJC3tTvMGGoxc02QLkoMsKX_Qwgh1GdvUu2-SYH8McEUt7EyKnsykNbmgT66IdeQju482EBDsjGjWD73tRqTGlMCWx5fJU1yzuIiJIGos3AfpXtqKlM7j8oLmKtM84UoNOG56xKiedwIF06nMjKzwgWEXhbPhabaand75PGTeaFVif0jz8wPYS17jc4galowjA-PvTVqrSCyHZ6yoHQ5ciT-59d7F5IvNFav8ZmSO-ZGBPGKWGJp0r8C7cH3aJWM5X0Os_k9S-slKcze3Qw_O4R568CpYDZLjk3Ky9h6SVcVTAgxHLzux2J7C3OYI_-y0bvkwDwdYQlDC43pMiL-tTruY1ginpthiafX4zOsYBJo6Ds2-68Tv10ofrZ3j0kLVwXSFOMW4EMMxXU_KSYVSxpWm_qTOZhB3Yi8nwmIMfS8GDM9ChbwAUpVW1VOaU54N2D6imsmzPHmu-MgN8H9y18HMsXHi8tVQy5jwPcnQ--uxmc0axuCGPZTDnx1caY2WV4Hd4fbbUFXc3IhvEhlqR-MlFGf9ul0-ZEoOjIgLRDuhi4JaHjTRZBphfk1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
شیعه وارداتی از اوگاندا تو خیابونای تهران دارن داد میزنن:
🔴
«مرگ بر منافق» [یعنی معترضای ایرانی]
🤔
یه عده خارجی از یه قاره دیگه اومدن تو کشور ما، بعد دارن برای مرگ خودِ ایرانی‌ها شعار میدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/119603" target="_blank">📅 23:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119602">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فعلا بزرگی زلزله تهران مشخص نیست و لرزه پردیس برای چندساعت قبل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/119602" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119601">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/زلزله در تهران
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/119601" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119600">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیل نگران است ترامپ ممکنه قبل از حل کامل مسائل اصلی جنگ، با ایران به یه توافق سریع برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/119600" target="_blank">📅 23:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119598">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/زلزله در تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/alonews/119598" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119597">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhy7bhBKIK12feiBVh5_8Z5bua6MuCLe2-o0nTRLuXpWeyxkNG3dL1MB_bnRhAMEIfDdKl7ASV32aXd1Q7zN0gwBMq4kunKNMASBU9hezT_l7lwhCr-agMnUpa20FgbcvK1nFIOdrX7VF59UAYTrNoeVvoS3iupSw9aB0KR6tNZqtflCWXz0QJMKvmV2a4lAPIw_EYyvdVvu7z_nMWNW6ZoDTSXh-XuEQUhP2uKkXHHe_SpBIW-4TeCTnDIXsd52CDmFUD_i-ksSNts7J6pq4TZ0fTdbTkoWcFCr7-vDIw23lgElGTSIPAnR7-98707hPfrTjwTY4zlgghKYW4pNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهبازی، مجری محبوب صداوسیما: هرکی ناراحته جمع کنه از ایران بره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/119597" target="_blank">📅 23:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119596">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در کانال
#الونیوز
به کانال زیر مراجعه کنید
👇
📃
https://t.me/ads_alonews
📃
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/119596" target="_blank">📅 23:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qMb86eVlW0DI_p5k9PlZZanRSKrkLCofcTQjQG-mzLOg8S3DR7i8WP7CVByRaj7CK3ay9fiGbMJZvrX5VjzqD_Ifneho_j7rjvvbGy3z1kqGASTq34ZaMn-9m1RgFufxzc9n9SgPhkrcq2qtcrXBpEwHW7lHoovREN9Omlb9GcWoLEBM0s5__gnstqTD2fkNYxVju_nxSpe_IN_Z1BGndxjImrk71YlNfUDfkCFsKqnWfHCCcuA81swbCBBcqBAkfX0Mie56FYHX_dVMHIiUJJZQ-UbkLvoWKJWEqlSdhqGTu0W8YyBBj7X0_-s8dt_X-FpBCJMdbNGLYUqjN1JDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران عالیه؛ فک کن اول باید نیم میلیارد بدیم تا موبایل بخریم، بعد باید یه مبلغ عجیب غریب بدیم که اجازه بدن موبایل آنتن داشته باشه، بعد باید پول بدیم بریم بسته بخریم، بعد واسه بستمون باید بریم پول بدیم کانفیگ بخریم که بتونیم از اینترنتش استفاده کنیم.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/119595" target="_blank">📅 23:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119594">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c91d54e64e.mp4?token=rHRrw_UjiZ6rriLslix2r17Tt4NhKEBEyoq0L6sxICbXn1SXI-BVAwp7I4a1NhyqBw66B5veZPmorlx0pBTzXYdhZ_0q8GO51V7oEpTps5jI8GUpWEJVHtkhNkzTenHaaQxDmLjxunQuSv0DZxdLGbANxvu6mJ-umF6M1tMg5gpq0QSTaYeJuDyCI4Et77y07neYqYBFMohmsVjxsnNWQVtx8KGsTg5Ozg32_IWZjBIUNXzgA1mJwgloGHr6F_9TSI-l4j-KyIVyXOJQiPonP-C4oGFGJFVVRPHID4f5GEgz43CLOpKGFQAIAVTxtyU4yP9yKDrEbd7eJOwxl-qDNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c91d54e64e.mp4?token=rHRrw_UjiZ6rriLslix2r17Tt4NhKEBEyoq0L6sxICbXn1SXI-BVAwp7I4a1NhyqBw66B5veZPmorlx0pBTzXYdhZ_0q8GO51V7oEpTps5jI8GUpWEJVHtkhNkzTenHaaQxDmLjxunQuSv0DZxdLGbANxvu6mJ-umF6M1tMg5gpq0QSTaYeJuDyCI4Et77y07neYqYBFMohmsVjxsnNWQVtx8KGsTg5Ozg32_IWZjBIUNXzgA1mJwgloGHr6F_9TSI-l4j-KyIVyXOJQiPonP-C4oGFGJFVVRPHID4f5GEgz43CLOpKGFQAIAVTxtyU4yP9yKDrEbd7eJOwxl-qDNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : نتانیاهو در تلاشه که انتخابات اسرائیل رو به تعویق بندازه تا قضیه ایران تموم بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/119594" target="_blank">📅 23:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119593">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
دیدار معاون وزیر خارجه نروژ با عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/119593" target="_blank">📅 23:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119592">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
صداوسیما:
الوعده وفا؛ داریم اینترنت اونایی که کسب‌وکار دارن یا تو فضای مجازی فعالیت می‌کنن رو وصل می‌کنیم(بهشون سیم‌کارت پرو میدن) که برن عشق کنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/119592" target="_blank">📅 23:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119591">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An9RPmD2CeQRV0mjz8Kpk95Y2qcu8ZEZpNuBgNEK_jLjnJSlSBAS24eEJNqK3gfozvXau-6inh4fyprEMPwxgqJrVaEwwGQ5iQmtvFjaeg_q5Hmh23jF5TGo_0ltM5w0zzD_MwV9ykGsz4mE_srVh58hKGcORwci51oXYxGpCQABrBpivTDpjTf2Qp9SFlaFg64Bsu6c7GRPuiUDFSdNHZyP4e_02AieWJ0eoFSQ7In-H_HmsmcYfQjVPnjtdlNlvwNeI7eFbSagOTnZjokARof-jdz7ljlRJrMQj56ZvB1g1w2QiTTg5qvvXLgROD_B01ZgX49HBaVqsf4_259xNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیست میلیاردرهایی که با ترامپ به چین میرن
🔴
رئیس شرکت بلک راک
🔴
رئیس شرکت گلدمن
🔴
رئیس شرکت مسترکارت
🔴
رئیس شرکت سیسکو
🔴
رئیس شرکت متا
🔴
رئیس شرکت ویزا
🔴
رئیس شرکت اپل
🔴
رئیس شرکت تسلا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/119591" target="_blank">📅 23:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119590">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c8339b93.mp4?token=tLd1lw4TyZ1tKYG4IisI9gAkG2x2vXsC62WAofu9L14fdqBQtRbEiGiZcJY_as0p0PuB5HEmUKRugFJOZWUAI3c5snPZrcor2km_uTPlBeEtvff-Gn0WolJBsQ2jfev0KHg-yKu_eEWUcM5ECHL5DXP2hwziguse0K5zJhSF9dNy9vIwZSQTG1H65AYQ340T9e1JeM8UckjZUjr6szkkYy5wOAc7940BJRa5ITcb7alnzoo32LH5KEpKANOr0FmVS3mrjLHJTtKG6UT697AN25dWQpEnIief5OXcxN1kTWk2_wwQo9C161hS7B541gQrnvbQ2ysCVZeyqkvReBVscmJhwWsMXPgYIUp94A4usOBjGltiTL6QXqy-hXdCiCsAOiV4Finy8cyzDYzANkzmjLjMB2D6-ng9TK5U3TgXU8msrfnUQLoHSwvX-mYMD5FHyZSXOIATCamnWjVXIsBQrXBUETSG2PwfEFpSc4AX3ndz4RXNI7GgBs2gCFE-dwttcYvaTYVq2aNf1spzAN_o9VepBSk_SxDcdNgxBw13uiI-604nbHYBAyC5kOxDmfs1mao6m5H6saeCFFCmRvsA3exqWiDQla3j0ONLQmIQOZUvk_Xa01R_1gd_lF9kWnJhdLa67RoU5iynh-3M7n1GXrQ-zDPWYosCnXB4RReCqG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c8339b93.mp4?token=tLd1lw4TyZ1tKYG4IisI9gAkG2x2vXsC62WAofu9L14fdqBQtRbEiGiZcJY_as0p0PuB5HEmUKRugFJOZWUAI3c5snPZrcor2km_uTPlBeEtvff-Gn0WolJBsQ2jfev0KHg-yKu_eEWUcM5ECHL5DXP2hwziguse0K5zJhSF9dNy9vIwZSQTG1H65AYQ340T9e1JeM8UckjZUjr6szkkYy5wOAc7940BJRa5ITcb7alnzoo32LH5KEpKANOr0FmVS3mrjLHJTtKG6UT697AN25dWQpEnIief5OXcxN1kTWk2_wwQo9C161hS7B541gQrnvbQ2ysCVZeyqkvReBVscmJhwWsMXPgYIUp94A4usOBjGltiTL6QXqy-hXdCiCsAOiV4Finy8cyzDYzANkzmjLjMB2D6-ng9TK5U3TgXU8msrfnUQLoHSwvX-mYMD5FHyZSXOIATCamnWjVXIsBQrXBUETSG2PwfEFpSc4AX3ndz4RXNI7GgBs2gCFE-dwttcYvaTYVq2aNf1spzAN_o9VepBSk_SxDcdNgxBw13uiI-604nbHYBAyC5kOxDmfs1mao6m5H6saeCFFCmRvsA3exqWiDQla3j0ONLQmIQOZUvk_Xa01R_1gd_lF9kWnJhdLa67RoU5iynh-3M7n1GXrQ-zDPWYosCnXB4RReCqG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
هشدار یک شهروند معمولی ایتالیایی به ایرانیان:
🔴
اشتباه ما ایتالیایی‌ها در سال ۱۹۴۶ را تکرار نکنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/119590" target="_blank">📅 23:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119589">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSt9u3-LuFxsTfaFW4RmNV1yRfMmTXtIR6s49EyaiGn3u6poyWl1sl-UZt5VMLjtARxwml5fFjuNd7EOemCV4hzy9oaSHK5kymKpEPsM1kKSqkFNu73Bjew7F1jzMs4uEgbAHpbEeJLV3z21eP7_nZ08REW8Cb0zpBIvLePf5vAh_TwJnQV3q5jXHbcRMCP11YJH2NEqiZfIDmJ2Hf_b8UXsybb9TZ6I_uPAkK-fDdXBlijF5lHOWUnb_hBSXLx8a8du9tyBkN76DAS2IFL4BytRWR4alFMou-5KWCYCW549FgjwmZeKBDhyMiVwDnmxU63of6N9rp088oNJtOvFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: همراه اول به 4 میلیون نفر پیامک اینترنت پرو ارسال کرده اما تنها 450 هزار نفر آن را فعال کرده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/119589" target="_blank">📅 23:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119588">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر اقتصاد: کسب‌وکارهایی که تعدیل نیرو نداشته باشند، از دولت تسهیلات می‌گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119588" target="_blank">📅 23:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119587">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیر اقتصاد: به صورت ناشناس در تجمعات شرکت می‌کردم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/119587" target="_blank">📅 23:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119586">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFXdtwenkzPjDTMf-8tMmdp6lrq-c6h5rWnKXDZ3cTpoQO0JZgkSRpWi70rIb7p6U_1j3iTz-BZokWsK1sR1IOrI4jN5h3CyTcuavOP6R8Zz290FXXJBT-gg3T2tfvpUg-gi2gVbYZp6XsVRfc0u_zxsHOzk4JNXUp7ZoZOsLsu4kz42nhsSgmXybyXCJRNDbnsNCDTw28fLKvEuysDLLe34-cySwkzTMYS-2bdxXyrQw3N4ho4N5Iu4kec9ocKHkN86i3EtX0DDlwCqP9nYYP9tVy-jr7oVDcKb7sEMz12nnHbrjEyjwmc5OS_2-zYnNw2t5SAzdL8769cU6BWrBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا دبیر: ۱۰ میلیون ایرانی خارج از کشور داریم که بیشترشان آدم حسابی‌‌اند/ ۵۰ هزار نفری که پلشت هستند و می‌رقصند، در خارج ول هستند
@AloSport</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/119586" target="_blank">📅 23:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119585">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
مارکو روبیو از جی‌دی ونس پیشی گرفت؛ پیشتازی در نظرسنجی ۲۰۲۸
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119585" target="_blank">📅 23:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119584">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
فارس به نقل از منابع: ایران به میانجی پاکستانی اعلام کرده است که تداوم محاصره دریایی در محدوده دریای عرب و خلیج عمان پس از برقراری آتش‌بس، گزاره غیرقابل اعتماد بودن مذاکره با آمریکا را بیش از پیش تقویت کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119584" target="_blank">📅 23:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119583">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رویترز : مقامات ایرانی و غربی گفتند که عربستان سعودی، ایران را از این حملات مطلع کرده و سپس تماس‌های دیپلماتیک فشرده‌ای در کنار تهدیدهای عربستان مبنی بر تلافی بیشتر صورت گرفته است که منجر به تفاهم بین دو کشور در مورد کاهش تنش‌ها شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/119583" target="_blank">📅 23:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119582">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9fca472b2.mp4?token=i9t9ecYsGcR8pl3vFb2MsizlYUfn8JFKE6wYQDG0KCvT0VAbGquDSX9yaAZFpkx3NsjfnB0kCHYtAVdhlUeM0hi2rXtx66LbpmlmMWVzi10TxwE3lbdp2ha3lSpiFwVOik1ltoXEkutpVbEuR6xErFwYIKCCSDv755RKSUlpJeGzCXRAvxw5FCHtVia9OKr3ufEQDNhuTYKAWv6vprJriTAGlH7zdssQ8VPO4iTNRQKjaZBUU_XCixn9UqowzPgbzEuWAoAy4g1Mq1Hpy2GFUUgI7a2YP7I13vvrvE20lY1y_s8rmp5r2vEiH_DRm0Clxizid9fro_pCpfjmI7gKOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9fca472b2.mp4?token=i9t9ecYsGcR8pl3vFb2MsizlYUfn8JFKE6wYQDG0KCvT0VAbGquDSX9yaAZFpkx3NsjfnB0kCHYtAVdhlUeM0hi2rXtx66LbpmlmMWVzi10TxwE3lbdp2ha3lSpiFwVOik1ltoXEkutpVbEuR6xErFwYIKCCSDv755RKSUlpJeGzCXRAvxw5FCHtVia9OKr3ufEQDNhuTYKAWv6vprJriTAGlH7zdssQ8VPO4iTNRQKjaZBUU_XCixn9UqowzPgbzEuWAoAy4g1Mq1Hpy2GFUUgI7a2YP7I13vvrvE20lY1y_s8rmp5r2vEiH_DRm0Clxizid9fro_pCpfjmI7gKOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
ویدئوی دردناکی از مشهد، 18 دی. فلکه پارک
💔
جنازه .... جنازه .... جنازه .... اینجا هم جنازه .... همه جا جنازه ست.
🔴
این جوانان توسط حکومت تروریست جمهوری اسلامی و عوامل بسیجی و سپاهی با تیر مستقیم کشته شدن، نه توسط اسرائیل و آمریکا.
🤔
انتقام ما رو توی تاریخ مینویسند، شک نکنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/119582" target="_blank">📅 23:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119581">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ادعای حسن ایوب خان، خبرنگار ARY News پاکستان: طبق اطلاعات من، لجستیک اداری و امنیتی هیئت معاون اول رئیس‌جمهور آمریکا، جی. دی. ونس، هنوز در پاکستان حضور دارد که نشانه آشکاری است از اینکه امیدها برای برگزاری دور دوم مذاکرات ایران و آمریکا در پاکستان همچنان زنده است.
🔴
با این حال، هنوز هیچ پیام رسمی از سوی هیچ یک از طرفین درباره ورود آنها به پاکستان برای گفت‌وگوها صادر نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119581" target="_blank">📅 23:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119580">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر اقتصاد: افزایش‌ قیمت‌ها مقطعی و به دلیل آسیب دیدن بخشی از زنجیره تولید است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119580" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119579">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت دفاع کویت از دستگیری چهار نفری خبر داد که تلاش کردند با یک قایق ماهیگیری اجاره‌ای وارد کویت شوند.
🔴
وزارت کشور بعداً اعلام کرد مظنونان اعتراف کردند که به دستور سپاه پاسداران انقلاب اسلامی برای نفوذ به جزیره بوبیان و انجام عملیات خرابکارانه هدایت شده‌اند.…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119579" target="_blank">📅 22:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119578">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر اقتصاد: برآورد خسارات منازل مسکونی آسیب‌دیده در جنگ درحال انجام است و برای تعمیر و بازسازی و لوازم خانه، منابعی توسط سازمان برنامه‌وبودجه در نظر گرفته خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119578" target="_blank">📅 22:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119577">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
طبق گزارش NBC News : ارتش ایالات متحده در نظر دارد در صورت فروپاشی آتش‌بس و تصمیم ترامپ برای از سرگیری عملیات‌های عمده رزمی، نام درگیری خود با ایران را به عملیات چکش سنگین تغییر دهد و این جایگزین نام قبلی عملیات خشم حماسی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/119577" target="_blank">📅 22:42 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
