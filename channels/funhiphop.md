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
<img src="https://cdn4.telesco.pe/file/scMdUgBIEbdDAyvEY151G_O9QHCtWrU7SDOJ-2Hy1gM3JCVdmSsr9ibq77r7fwKnJoA55JEh2iY08xYzv1OIUBlo2c4BX3buftR-rzjZaxlbh0ZvBcBRnwHhM3wJQ4ft1WRvgGb96irZOBLQtU4LlhZT4UTgqH6Utk80luwb6Sssd3BxDi41YzmJvtZo0MIBLvInJSK44fCFzOZ2xbREJ0HLxeN_GSiTWG2Ea10qDaaEXzRfLKtK-9WXuULr_-Nam3vE1IqUWLbXXcDsjaNRZF7c7uTQLoVZdoVGJ9ov3YRx4YkDjnZOW7L3Zphaz347V5cI-54SPyZQP4CoTkkwrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 174K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 01:28:15</div>
<hr>

<div class="tg-post" id="msg-77172">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تماس تلفنی ترامپ و نتانیاهو(صدا کم):
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/77172" target="_blank">📅 01:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77171">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال ۱۱ اسرائیل:
ایران از طریق واسطه‌ها پیامی به اسرائیل فرستاده است که تهران حملات خود به اسرائیل را به پایان رسانده و حملات بیشتری انجام نخواهد داد مگر اینکه اسرائیل تلافی کند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/77171" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77170">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یدیعوت آحارونوت:
بر اساس گزارش‌های دریافتی، در گفتگویی که کمی پیش به پایان رسید، نتانیاهو به ترامپ اطلاع داد که
قصد حمله‌ای گسترده به ایران
را دارد.
رئیس‌جمهور آمریکا روشن کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.
مشاهده‌ی کیر
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/77170" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فووووووری اسراییل لیست ترور جدید پخش کرد
😐
😐
😐
مشاهده لیست
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/funhiphop/77168" target="_blank">📅 00:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پروازهای فرودگاه امام تا اطلاع ثانوی لغو شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/funhiphop/77167" target="_blank">📅 00:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سفارت آمریکا در اورشلیم از همه شهروندان آمریکایی می‌خواهد به دنبال نزدیک ترین پناهگاه برای خطرات احتمالی باشند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/77166" target="_blank">📅 00:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرنگار وای نت:
ایالات متحده پیامی به اسرائیل فرستاد که بهتر است چند روز صبر کند تا ببیند آیا می‌توان با ایران به توافق رسید یا نه.
و اگر نه، ما طبق برنامه به اقدام مشترک بمباران گسترده همراه با غافلگیری را از سر خواهیم گرفت و ارزش ندارد این موضوع را با درگیر شدن در تبادل محدود ضربات هدر داد.
مشاهده‌ی ادامه‌ی خبر
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/77165" target="_blank">📅 00:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سفارت آمریکا در اورشلیم اسرائیل از همه شهروندان آمریکایی اسرائیل خواسته است که نزدیک پناهگاه بمانند یا در پناهگاه پناه بگیرند.
مشاهده‌ی ادامه‌ی خبر
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/77164" target="_blank">📅 00:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">چند دقیقه پیش تماس تلفنی حرامز و نتانیاهو آغاز شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/funhiphop/77163" target="_blank">📅 00:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اسرائیل لبنانو زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/funhiphop/77162" target="_blank">📅 00:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانال ۱۴ اسرائیل: امشب فقط موشک‌ها و جت‌ها نیستند که بین آسمان و زمین در نوسان هستند، بلکه سرنوشت سیاسی نتانیاهو نیز همین گونه است.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77161" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77159">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:  من الان با نتانیاهو تماس می‌گیرم و می‌گویم که به ایران حمله نکند!  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/funhiphop/77159" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77158">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال ۱۴ اسرائیل: امشب فقط موشک‌ها و جت‌ها نیستند که بین آسمان و زمین در نوسان هستند، بلکه سرنوشت سیاسی نتانیاهو نیز همین گونه است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77158" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77156">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نیویورک پست:
ترامپ در تماس تلفنی ای که ما با او گرفتیم گفت زیاد نمی‌تواند صحبت کند ولی اوضاع بسیار خوب پیش می‌رود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77156" target="_blank">📅 00:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77155">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: حملات مشترک سپاه و آمریکا علیه مواضع اسرائیل بزودی آغاز میشود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77155" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77154">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: حملات مشترک سپاه و آمریکا علیه مواضع اسرائیل بزودی آغاز میشود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77154" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77153">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سخنگوی ارتش اسرائیل: ما به حملات خود در سراسر لبنان ادامه خواهیم داد، علیرغم معادله‌ای که ایران سعی دارد تحمیل کند.
اجازه نخواهیم داد ایران معادله جدیدی علیه لبنان ایجاد کند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77153" target="_blank">📅 00:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77152">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:
ایران «اشتباه بزرگی» مرتکب شده و ارتش اسرائیل «در حال تصویب طرح‌هایی برای آینده» است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77152" target="_blank">📅 00:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77151">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک ساعته ارتش اسرائیل می‌خواد بیانیه بده بگه می‌خوایم چیکار کنیم هی ترامپ مادرجنده بازی درمیاره هی بیانیه به تاخیر میوفته.
تا حالا سه بار به تعویق افتاده.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77151" target="_blank">📅 23:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77150">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل: الحمد الله در حمله موشکی هیچ‌کس آسیب ندید.  اگر نتانیاهو پاسخ دهد، این ادامه خواهد داشت و ادامه خواهد داشت. ما بسیار به توافق برای پایان جنگ نزدیک هستیم و این توافق خوبی خواهد بود. نمی‌خواهم این موضوع توافق را به هم بزند. هر دو طرف…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77150" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77149">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل:
الحمد الله در حمله موشکی هیچ‌کس آسیب ندید.
اگر نتانیاهو پاسخ دهد، این ادامه خواهد داشت و ادامه خواهد داشت.
ما بسیار به توافق برای پایان جنگ نزدیک هستیم و این توافق خوبی خواهد بود.
نمی‌خواهم این موضوع توافق را به هم بزند.
هر دو طرف حمله کرده‌اند و من نمی‌خواهم حمله دیگری ببینم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77149" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77148">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ:  من الان با نتانیاهو تماس می‌گیرم و می‌گویم که به ایران حمله نکند!  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77148" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77147">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7wiSRJseRq8INzNDzc4_It11SiEEjiAfGWOqxZMvBemjQlokXacLuW6QHkfPFKrxkRLGIHZkSUMN6nnuDVwrWRNBNj7OOjIJAi-qxopPkYSiU3SmXOiy0kuZbFdpKHDsWjxT44XWAEk4_WtsA3k7BkMKIeaECtayg09KvbqlSgYXgJn9_YXM9zpFtDgkuctUWp8s7PUJiFKdxajyI06UzTK83sbBfWZUxYp0DzYTHuvk33Mo7yFlHyqBHMoEd1NHEBZVQG5xT8mHJxUJxWczvkt_6yhabP2cVpvZdulEg11Ju-CM1gGsoC_Dz3KRWZSOtKW4wBRvDvrRhG_NT18lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت توییتر مجتبی خامنه‌ای:
نفس رژیم لرزان صهیونیستی به شماره افتاده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77147" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77146">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ:  من الان با نتانیاهو تماس می‌گیرم و می‌گویم که به ایران حمله نکند!  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77146" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77145">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی خاتم الانبیاء چرا نیومد؟  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77145" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77144">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حریم هوایی سوریه و عراق بسته شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77144" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77143">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اینجوری پیش بره واقعا کاخ سفید حسینیه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77143" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77142">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
من الان با نتانیاهو تماس می‌گیرم و می‌گویم که به ایران حمله نکند!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77142" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77141">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فاکس نیوز:
مقامات ایرانی معتقدند که ترامپ تمایل لازم برای ورود به یک درگیری گسترده‌تر را ندارد و مصمم است جنگ را تقریباً به هر قیمتی به پایان برساند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77141" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77140">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">همه موشکای شلیک شده رهگیری شدن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77140" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77139">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حرامز به فاکس نیوز: پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77139" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77138">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فارس نیوز:
حملات ایران تمام شد.
مقام ایرانی به رویترز:
اگر اسرائیل جواب دهد با شدت بسیار بیشتری حمله خواهیم کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77138" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77137">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تایید نشده  گزارش شده جنگنده ها تو راه ایران هستن   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77137" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77136">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ:
آفرین!
شلیک کردید دیدیم دارید، حالا برگردید سر میز، مذاکره سرد شد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77136" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77135">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حرامز به فاکس نیوز:
پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77135" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77134">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تایید نشده
گزارش شده جنگنده ها تو راه ایران هستن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77134" target="_blank">📅 23:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77132">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaqomixWpeFabNgAEOn0uPB0g4BcLoNB4TbX7qbOk1ThC5zI0GjRRNyGfxHnggOz2rmSfYvsPMbhpylYIAl1wWUz20hUvKOuWMqUgjR4B5nONynUoYmQhJ4kmjh5wL4aOspIo2KbxZYzihMLSRNkYufY7Q9k6ZFMF1ZOZhZCcfscPP_ea2QCVYhB0hQti-c3ZlDSO0Rxz6d5GqNikI8HFyqiXrZKQnJNj_z97sUt7wuI-xTBEhNUGEQ-Atsv-UDzJccgKKGRLlnvYtFqwL42kVgOd8T1IAoJE8IMxVtpZoLkfoK3wKMeGS9KV6yOq4ZIvP0xcncBFvSXXLWUkAbriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا به به
امام زمان آنلاین شد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77132" target="_blank">📅 23:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سخنگوی خاتم الانبیاء چرا نیومد؟
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77131" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اینسری هم نقض نشه دیگه نمیشه</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77130" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مذاکرات همش فریب بود  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77129" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شمال اسراییل یه برخورد موشک  گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77127" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پدافندا فعال شدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77126" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مذاکرات همش فریب بود
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77125" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">موج سوم آقا موج سوم  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77124" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سید مجید :
الوعده وفا
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77123" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسراییل منتظره چراغ سبز امریکا هست برای حمله به تاسیسات ایران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77122" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هیچکس اندازه دانش آموزا و کانفیگ فروشا خوشحال نیست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77121" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تعداد زیادی هواپیمای سوخت رسان آمریکایی از فرودگاه های اسرائیل به پرواز درآمدند.
چندین سوخت رسان ارتش آمریکا هم از عربستان و اردن به پرواز درآمدند
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77120" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تایید نشده
میگن صدای جنگنده میاد از بوکان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77118" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آکسیوس:
ترامپ در جریان تشدید تنش بین ایران و اسرائیل قرار گرفته و به زودی تصمیم گیری می‌کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77117" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77115">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omUlKhBSfzdm-4rLMxTINa7Ecv-WgdJ7KsHe0eKU4MsLJDtXPFos0eV4Pg0s_YbKfsvItxbuByCY_Ut06qhnMYyMCN_AuLNbHManbDpFUfSb7YKPsgtkj58nu-wIjkLaMUaBDIy90WJYgKLwWyzJgNmLIHRCAQyN2zcKX409bbWGvCXeuSic4oen2yj-wr4nBemvrH2Xd6pRvLJwpV1Pw5MiP7EG_aW3qLpQ3IpX-aVyDq6AqMWLjkLleq-XnuxZ5jB3wGRvdiTclrh9HbG21x10yImnTZpZbci6uRjtQO6k6tBFIY1uYUv-dJbJC6xpUDacGk5_OumtpL90ApMoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77115" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77114">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا:
اگر اسرائیل حملات خود را در لبنان گسترش دهد یا به این حمله‌ی ما پاسخ دهد، با ضربات قوی‌تر و پشیمان‌کننده‌تری مواجه خواهد شد و حملات ویرانگری علیه رژیم و حامیان آن آغاز خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77114" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77113">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توان موشکی سپاه خیلی کم شده
تو 3 موج کلا 20 تا بیشتر نزدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77113" target="_blank">📅 22:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elB1OMjkVAlT_E0CItxXDYmB-X9jJsHB7tHyyruVS0kjnNugz7WWJriY37Sm-Tj9pC1W_KEivxUTaoERKCn1zoG02U8Y0HA2Y5jg4SB1OJvfb-bb9Tzx40GwfmfjhJBQB5qsT5Rpwp8VJQv6mdLWb3gOEVWig4gTbzyS4kV7f6oEJUDiB_ic-Hq6hDLiE1yZpzYBEws2sbwnMSmTEcWJlVOSUhWbvw-sdzwfVajwf_jLjoPeDhbZov1gh41BO4lzICr7l57XhlKBuKJvKVhrHxjIHTb4RzZ9s4tCdYbIwdE28kzfbPzjb3uGDs2PI6xlvs_ggs7Rzf_AW0tmeIXOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده های آمریکایی بیانیه دادن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77112" target="_blank">📅 22:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">موج دوم حملات سپاه با حداقل پنج موشک شروع شد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77111" target="_blank">📅 22:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">منبع ارشد اسرائیلی به کانال ۱۴: به ایران حمله می‌کنیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77110" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مقام ارشد به کانال ۱۲ اسرائیل:
ایران می‌خواست معادله‌ای جدید از آتش محدود و سنجیده ایجاد کند، اما ما اجازه نخواهیم داد این اتفاق بیفتد.
ما گسترده جواب خواهیم داد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77109" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ارومیه صدای انفجار
منبع رفیق کسخلم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77108" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77106">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزیر امنیت داخلی اسرائیل: تهران امشب باید بسوزد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77106" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77104">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">موج دوم حملات سپاه با حداقل پنج موشک شروع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77104" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77103">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نت باز داره کیر میشه توش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77103" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77102">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سد مجید نقطه زن این همه گفتید اسرائیل لبنانو دوباره بزنه مام میزنیم وقتش رسیده پس جان عزیزات تلاویوو با آبگرمکن بزن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77102" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77101">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تمامی موشک های شلیک شده رهگیری شدند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77101" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77100">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">علی داره تهدید میکنه که یا دوباره ادمینم میکنید یا جنگ شد وصلتون نمیکنم</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77100" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77097">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خارکصده بدو بیا بگو اینم نقض آتش بس نیست  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77097" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77096">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خارکصده بدو بیا بگو اینم نقض آتش بس نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77096" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77095">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یک مقام ارشد اسرائیلی چند لحظه پیش به رادیو ارتش اسرائیل گفت که پرتاب‌ها به سمت خاک اسرائیل از ایران به معنای «اعلام از سرگیری جنگ» است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77095" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77094">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ریدمممم</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77094" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77093">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حملات موشکی جمهوری اسلامی به اسرائیل شروع شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77093" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">زدن</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77092" target="_blank">📅 22:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77091">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الان کلا یک هواپیما رو آسمون ایران هست اونم بزودی تو تهران فرود میاد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77091" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77090">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اختصاصی از ایران اینترنشنال:
سپاه پاسداران آماده حمله موشکی به اسرائیل است
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77090" target="_blank">📅 22:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77089">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtFCb4MSGF33aDfFyBCDjfJkABycpea3GqLWn5MJ0TNywW4P4d2rW_bh3GvtvsCMK4HPOD2I_pjeBFNr0FrFD9aiVCg7bjE7RjXJIqFL-vaAO14InoGMxHBhW7_KUNYfZF-UEHcElCKsRVOQkdSkERPuXcAJa09RxPqyb82iL_vdEOtJYsUWxTg4dFM73W-XvJ-ySG1J7xTuGVwh5HmYysKco7lQlm72AdPVuKBueOQzVgQfFvsUcSkwr8FaCJ2Nr5bHVYnT_3BhCCOkBJeVg8ZxEESiGC_MT1OkE5_aVGMflZBhbfA8MqBMnogZL5Rn11ymHM-_wYYKL_sNWCzUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان کلا یک هواپیما رو آسمون ایران هست
اونم بزودی تو تهران فرود میاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77089" target="_blank">📅 22:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77088">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA9jaR6fg9DPIuiyNRdo7oFr4LGUaq5sHoVhgagNraWdBn3vJ5CJgJ1RwCLT3hk0Ob2UXLagedYU7VNj7wSwb-lZTlWUgiLX-Ozy3fSkf88Ahbs-PAMvszjW4fnNnxQMq0kE1pNmjEIZ-Pj70HvRRBUKgzjtfDm9U8JH7VeOCSd9qAAnCvwdjscMf49a-sVzFB8e3L8aHFYyhrFuvIEibYTkn8zDNR4i0xclQDYEuYxgfHrh4m77pOEVGlyLG-zC0ncXFPXm963uavRy1FxnX-z0qO4YxeaNkIu4MMt2tLXZ-rtlZMwbhLL48ANRlIAGQ0_R8I-9zBqeaDbp1YxTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات لو رفته از اولین خلبان ایرانی سوخو ۳۵.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77088" target="_blank">📅 22:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77087">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زنده مونده دوستان
نگران نباشید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77087" target="_blank">📅 21:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77086">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کریستین اریکسن باز هم وسط بازی دچار حمله قلبی شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77086" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77083">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efev0uKDpk01lPkik1Lr2hMCSXr2cdeN9TbLiENUuss5_3AMv8DWEB-Rb4XJWP4L2JmLy-nNxl5MS8RXrJ2DohStJtlKaIn5z-vjxahWs90RqcpkjRYPSUd-qncsIlD2j5mQ37PrgadgCNzsK8OuOQwbPaVf3m5D99wwHbyZJ801CB5mHQ_ETcQygIEQ0aDdvfaigE2Xa59TOLsPHCqO-ltjAz0ilLPgoGMoRLcRmpw0Ww28KlHMtHuNwaAA-cBVIIxZCALH9hwVdZxOCClvIDz3SagNkFOfdZKCGhZM7YayozfY45iUHAw-PG7jlQTWElyas-wavWrrYLrh905dbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم به نام TXICLUV ریلیز شد.
🎵
SoundCloud
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77083" target="_blank">📅 21:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77082">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbcVrVdp-LRTcBYHeKSk3oEW9JlREZRsYgZMD4euDVOehukmwp5M-rI2V1YAxHyauS-Rd2-D1MR2E9VHnvrDY88f9OxuaHF1-31X39zvYQTppEYEYu5l-JAzv465eVSd5kZ4KuSgWo3LXgZOpUZt7nSnj07PQcvKCcVnISgG8aJS2DYhuqjdLdwjW3B8P_gsTxmf1dmbrwYN56uJp-Tsn_TlBnbql6b8g7Msj5mD9ODfJFjKNdyOcBRKNDpFJYuJVuQ05MysPk01hOQNc_uyb3zE1S31Uazu2b4S2ELV-7nRL-ShHwpvas4awvBp9MQitBsdRCerYMOJpvQkAnrVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود کلش از صداسیما کیری شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77082" target="_blank">📅 20:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiLffcqJzP1Meci3BO_XFLQlBy_gPERb5L2pfukBpGFSNRrw8gIQl39C1j-gCFEtS9XCCoykv99pSaYwCCrSe-kmnWvO27Sk7uUjuUSzbwyJ7nm2CZJnPXFWAC_TfdJtWIpuDw6YsrFdufEejKqJ8psc0_grJew9Gq9MDLa-s77o2yOrRRnjJsaT1uyoe5cUe53CPrU_wxh4zJkWN5rIZCAH_9pgkolCsm0y3m0hjpFj3lktViZYVwUZNVQH8NTFZ3h9V83OTMUkZ0-Ctt8Qj6n8Pcw1dgGouf6Fe-PKFB7HIrWWBDWahyk_0QJITLTLyvTIfreq6MBRyAAEwgezLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندبار افعی کردم خوشم نیومد، این سری کبرا
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77079" target="_blank">📅 20:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چه عکس بالا، چه این پست یک چیز رو نشون میده: مادر جندگی  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77078" target="_blank">📅 19:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77077">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qno8j28z2ukBtOh_6m6M16AOa2b6zUv1R0oQonhOBtk9K1nACSyNu1S14z4dNxXgiraGdqRHQXsLCZaqOSvXIxPwRQLzNUKHr1r1ORJAcoKRslqBpzfamz8kUCWKUj94gBzuVuBYgOlMcgIpV1KrROGoQAKpHS0jLKEaR9EqbIf0OU0pq7OkapQ3Dy2exjBRBPl83e0l8Q97_iQi_yzWBZRfP3Bhl8vfgZ2wLjp5bFnI4ToR5-KMJeIFxT22nYUvv6DXuGpRwfx65unxbi5Grx57lbARw6VqSQVaF_Am7hlZTexap1UT6GcMIHnGl5Gd9KYOkEO0L6QuIfMipO3QXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوزرنیم‌ها در خاطر باقی میمانند  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77077" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77076">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBfC0kT06-KSFlRQGYw80oXS8FxXwkTjbyq__ecH3A2YMFZ1dopE4DjdtWKGusPZiw2tSHbTybKIjz2s30mC2xEouwkDCQw5SM0DONrHaOizbnLL4quOoG6TuiIogVPoLcvEhzxuAIUf3lwtuW3vdBytLJMbwIb4YURd6xCC_310MoPxNqLkfgQVB7GGj9dD6jYSAwGyuwUjSIqU2-hgpDqMVdfJdHK9hZ5RH2jem8j6mPQPDDdvpOCvCUKLXhHn4GdcTMXdlcL7U9_vb0ESlkaSs7Nf3-SgAs65gCiJETZWFeGl-8nESj2WVb-xpbEyehhqU-B0sdIVEIfaxXiEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوزرنیم‌ها در خاطر باقی میمانند
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77076" target="_blank">📅 18:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77075">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مقامات ارشد اسرائیلی به چند رسانه‌ی اطلاعاتی منبع باز اسرائیلی گفته اند که احتمال بالایی برای «آتش‌ هماهنگ‌شده» بین ایران و اسرائیل در ساعات آینده وجود دارد.
(با رژیم غاصب و جنایتکار و جعلی صهیونسیتی هم هماهنگی؟؟؟)
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77075" target="_blank">📅 18:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77074">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی و سیاست خارجی رژیم جمهوری اسلامی، ابراهیم رضایی:   ما پاسخ قاطع و دردناکی به حمله رژیم صهیونیستی به ضاحیه خواهیم داد. این سگ‌های هار باید تنبیه شوند و به جای خود بازگردانده شوند. امشب به آسمان سرزمین‌های اشغالی نگاه کنید.  @FuunHipHop…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77074" target="_blank">📅 18:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77073">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خب مثکه باید کم کم رفع زحمت کنیم به ثوپر عاپلیکاطیون های ایرانی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77073" target="_blank">📅 18:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77072">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی و سیاست خارجی رژیم جمهوری اسلامی، ابراهیم رضایی:
ما پاسخ قاطع و دردناکی به حمله رژیم صهیونیستی به ضاحیه خواهیم داد. این سگ‌های هار باید تنبیه شوند و به جای خود بازگردانده شوند.
امشب به آسمان سرزمین‌های اشغالی نگاه کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77072" target="_blank">📅 18:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77071">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: از حملات بیشتر اسرائیل به حزب الله حمایت میکنم.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77071" target="_blank">📅 17:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77070">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_F0n5tOHtiW0lkfkfs-PKGSgHu0TvEluWD8YJ1P1_QoToPKN4FIVSKXnUe_h4rRszMFu0PynXR8nuhyxl1k25HIXc-s7JxYSY9YndEewNNn6BR07F0sA9lNB58l2NORLEOveWlUeEZjVeZbgHTl8vS6SSlxJrwnsgZ4E3kqGGP2pxy87yCVwWbRMwOG_x2HZms_rzyFBZ7Ym_s1QOdiNLo_FClAliau4zqZA2_1My0leiWb3wSl8IEchAwzC7Zu-rcA3HLyJdUSRl2yhb0TJ_p9d20wcE-bdrKNY5r_WvoamAvuKcG_08Ur0iRTVAo42sX0z2uee9syo8_2hEeZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اینکه چرا نتانیاهو اینقد قوی عمل میکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77070" target="_blank">📅 17:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77069">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رادیو ارتش اسرائیل: ترور هدفمندی انجام دادیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77069" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77068">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سد مجید نقطه زن
این همه گفتید اسرائیل لبنانو دوباره بزنه مام میزنیم
وقتش رسیده پس جان عزیزات تلاویوو با آبگرمکن بزن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77068" target="_blank">📅 17:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77067">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:
هیچ تحریمی کاهش نخواهد یافت و هیچ پولی برای جمهوری اسلامی آزاد نخواهد شد
اصراری ندارم لبنان در توافق کوتاه‌مدت ایران گنجانده شود
اگر ایران به توافق نرسد، ایالات متحده نیروی نظامی ایران را بیشتر تضعیف خواهد کرد تا زمانی که نیروهای آمریکایی بتوانند اورانیوم را به‌طور ایمن از کشور خارج کنند.
این برای ما جنگ بزرگی نیست.
آنها محاصره کردند، پس ما آنها را محاصره کردیم. ما محاصره نهایی را داریم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77067" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ یسری کصشر گفته باز که حسش نیست بخونم و پوشش بدم</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77066" target="_blank">📅 17:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77065">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صداسیما: منتظر پاسخ قرارگاه خاتم‌الانبیا باشید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77065" target="_blank">📅 16:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77064">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شورای عالی امنیت ملی پس از حمله اسرائیل به منطقه ضاحیه بیروت، جلسه اضطراری تشکیل داد.
‏آنها قول دادند که در صورت حمله اسرائیل به بیروت، به اسرائیل حمله کنند و آتش‌بس را لغو کنند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77064" target="_blank">📅 16:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77063">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9xyMJGT4GxLEA-LR8c2r67GVt8mPtJKVw08w0xfonyqCBNwTsAHQ5B_AlZwPLZfTSjH_bMI4QjQFdDkalAFTPQBnBLaPxZQralkAK_RWQtwHvosseWeIGhqmrGxZOyP1_X3deybWTRc3_jBfvZmhvj--rDCUzsW8AtiVJPMvDrIGFeUNg-qUL4iaQMGMSlinLPXdZa0e-G57rKwKaLjUUZz7sJLtWTGMZEAv1u1g_k1BvH3MijD91Xs794FufSA3isQ5QEPXZNxmzzVZAa47zOWHwayCdKd8K7afJvczDArbyPX6QxSDzwhu76LuJQOweLQLbtmimaM_VL5Xr6X7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رادیو ارتش اسراییل : ما یک ترور با ارزش بالا انجام دادیم
+ شیخ نعیم قاسم؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77063" target="_blank">📅 16:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77060">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/77060" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77060" target="_blank">📅 16:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77059">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV5lXE6M2lvzn9z1bMSyH5CPV1YC9T7IExSP0WA2o4Kubu-tIg_p33QSMZZsxw9xbgFwTjGAdk03DwH2820XnVOavrePeU9M7W5ZTg1hmPke-OA46owDCiKnYfYKjRsZE6l-2TjvTGyrcSeNIpugmSuXc_kVSRmj-oWGtPBnmMtRZKxerD0jWLan09e86Uc4d95Qu3ENtb8SCvys-gJ-aw9zBzqF06r864fyk_kQm9oaWwIgkp4J6FqsoVU4Ke3cPjUdhlEe6AFcFixKr9DmwxJG5XYvruF-7y3Bf_TzYx0PP_jl8q0g9Hgl1rryX3zj9AIQtDlR8h7_2JYEXNFUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g17
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77059" target="_blank">📅 16:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77058">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
حمله به بیروت از قبل با آمریکا هماهنگ شده بوده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77058" target="_blank">📅 16:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77057">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svdzmKSqtqmCQ3ssI7PnOzgOtxZqbgxlLiI_GVtVCXdqtS9h2LO-mh1xxo4Q5de5C62TjrsYRYzbFAOlxq3CkLLu_iXMJCOTtVxHST92ZTcXRVK4aVrEhA3Yqo9HkN-J711MYrzjZX_GohkUF7PzQ2oRY0vq3eQJOLHKfmyb42elTaYns2SmjwEILwtiDXGQRW2j-8DRcGyZ67G1JMI5mQ7vE3pfrVr4LkYFrNBzv2ibG_fk6n98YQ-XQwZRyoZ8suRuaP6LUlkn0GseQxotWl_Td2v-sb4ibaN2vujVoNQWcBPk9hw0BrGvvfwk0ZnMm92R90Vv3yFN4kEddhUi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو
مردی که یک تنه داره سرنوشت خاورمیانه رو عوض میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77057" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77056">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الان ترامپ عصبی میشه خودش اسرائیلو میزنه</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77056" target="_blank">📅 15:57 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
