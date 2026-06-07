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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 00:13:13</div>
<hr>

<div class="tg-post" id="msg-77156">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیویورک پست:
ترامپ در تماس تلفنی ای که ما با او گرفتیم گفت زیاد نمی‌تواند صحبت کند ولی اوضاع بسیار خوب پیش می‌رود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/77156" target="_blank">📅 00:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77155">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: حملات مشترک سپاه و آمریکا علیه مواضع اسرائیل بزودی آغاز میشود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/funhiphop/77155" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77154">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: حملات مشترک سپاه و آمریکا علیه مواضع اسرائیل بزودی آغاز میشود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/funhiphop/77154" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77153">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سخنگوی ارتش اسرائیل: ما به حملات خود در سراسر لبنان ادامه خواهیم داد، علیرغم معادله‌ای که ایران سعی دارد تحمیل کند.
اجازه نخواهیم داد ایران معادله جدیدی علیه لبنان ایجاد کند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/77153" target="_blank">📅 00:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77152">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:
ایران «اشتباه بزرگی» مرتکب شده و ارتش اسرائیل «در حال تصویب طرح‌هایی برای آینده» است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/77152" target="_blank">📅 00:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77151">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک ساعته ارتش اسرائیل می‌خواد بیانیه بده بگه می‌خوایم چیکار کنیم هی ترامپ مادرجنده بازی درمیاره هی بیانیه به تاخیر میوفته.
تا حالا سه بار به تعویق افتاده.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/77151" target="_blank">📅 23:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77150">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل: الحمد الله در حمله موشکی هیچ‌کس آسیب ندید.  اگر نتانیاهو پاسخ دهد، این ادامه خواهد داشت و ادامه خواهد داشت. ما بسیار به توافق برای پایان جنگ نزدیک هستیم و این توافق خوبی خواهد بود. نمی‌خواهم این موضوع توافق را به هم بزند. هر دو طرف…</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/77150" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77149">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل:
الحمد الله در حمله موشکی هیچ‌کس آسیب ندید.
اگر نتانیاهو پاسخ دهد، این ادامه خواهد داشت و ادامه خواهد داشت.
ما بسیار به توافق برای پایان جنگ نزدیک هستیم و این توافق خوبی خواهد بود.
نمی‌خواهم این موضوع توافق را به هم بزند.
هر دو طرف حمله کرده‌اند و من نمی‌خواهم حمله دیگری ببینم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/77149" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77148">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ:  من الان با نتانیاهو تماس می‌گیرم و می‌گویم که به ایران حمله نکند!  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/funhiphop/77148" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77147">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7wiSRJseRq8INzNDzc4_It11SiEEjiAfGWOqxZMvBemjQlokXacLuW6QHkfPFKrxkRLGIHZkSUMN6nnuDVwrWRNBNj7OOjIJAi-qxopPkYSiU3SmXOiy0kuZbFdpKHDsWjxT44XWAEk4_WtsA3k7BkMKIeaECtayg09KvbqlSgYXgJn9_YXM9zpFtDgkuctUWp8s7PUJiFKdxajyI06UzTK83sbBfWZUxYp0DzYTHuvk33Mo7yFlHyqBHMoEd1NHEBZVQG5xT8mHJxUJxWczvkt_6yhabP2cVpvZdulEg11Ju-CM1gGsoC_Dz3KRWZSOtKW4wBRvDvrRhG_NT18lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت توییتر مجتبی خامنه‌ای:
نفس رژیم لرزان صهیونیستی به شماره افتاده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/77147" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77146">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:  من الان با نتانیاهو تماس می‌گیرم و می‌گویم که به ایران حمله نکند!  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/funhiphop/77146" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77145">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سخنگوی خاتم الانبیاء چرا نیومد؟  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/funhiphop/77145" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77144">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حریم هوایی سوریه و عراق بسته شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/funhiphop/77144" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77143">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینجوری پیش بره واقعا کاخ سفید حسینیه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/funhiphop/77143" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77142">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:
من الان با نتانیاهو تماس می‌گیرم و می‌گویم که به ایران حمله نکند!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77142" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77141">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فاکس نیوز:
مقامات ایرانی معتقدند که ترامپ تمایل لازم برای ورود به یک درگیری گسترده‌تر را ندارد و مصمم است جنگ را تقریباً به هر قیمتی به پایان برساند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/77141" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77140">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">همه موشکای شلیک شده رهگیری شدن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/funhiphop/77140" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77139">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حرامز به فاکس نیوز: پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77139" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77138">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فارس نیوز:
حملات ایران تمام شد.
مقام ایرانی به رویترز:
اگر اسرائیل جواب دهد با شدت بسیار بیشتری حمله خواهیم کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77138" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تایید نشده  گزارش شده جنگنده ها تو راه ایران هستن   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77137" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77136">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ:
آفرین!
شلیک کردید دیدیم دارید، حالا برگردید سر میز، مذاکره سرد شد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77136" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77135">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حرامز به فاکس نیوز:
پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77135" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77134">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تایید نشده
گزارش شده جنگنده ها تو راه ایران هستن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77134" target="_blank">📅 23:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77132">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm7oP7j9TPy4QITgDW67peOVZC1Ep0pPJUzmcHYY3Cal9xZslj5X1H737rntkHBrrrTIwBBvIxGrTRCR0Rlv-SHHQWJvoBMs_9jVK7I3Z_aSeJJGX3AJyx0w9mx0f3l3_DNP0iDlOgDfyhXc1l2f2ZRvna2EPo3muxmZPZwSEjG8cgaxQnkiDSIbfo2VrhUSto7dDVv9YM_Qb2XzhhPS0rZQfGA3fvyTAVc1ZWvT91644VXiZADRrrYO-ariuz_A1QWt8Drg1gwdogzg2sRtzwg3fWAmtOuP9If4z803C8RsupPtR8JeOHxsrfZlmujIpZJzLognIDRy_-xkm94q-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا به به
امام زمان آنلاین شد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77132" target="_blank">📅 23:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77131">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی خاتم الانبیاء چرا نیومد؟
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77131" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77130">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اینسری هم نقض نشه دیگه نمیشه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77130" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77129">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مذاکرات همش فریب بود  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77129" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77127">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شمال اسراییل یه برخورد موشک  گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77127" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77126">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پدافندا فعال شدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77126" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77125">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مذاکرات همش فریب بود
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77125" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77124">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">موج سوم آقا موج سوم  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77124" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77123">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سید مجید :
الوعده وفا
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77123" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77122">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اسراییل منتظره چراغ سبز امریکا هست برای حمله به تاسیسات ایران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77122" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77121">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هیچکس اندازه دانش آموزا و کانفیگ فروشا خوشحال نیست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77121" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77120">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تعداد زیادی هواپیمای سوخت رسان آمریکایی از فرودگاه های اسرائیل به پرواز درآمدند.
چندین سوخت رسان ارتش آمریکا هم از عربستان و اردن به پرواز درآمدند
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77120" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77118">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تایید نشده
میگن صدای جنگنده میاد از بوکان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77118" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77117">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آکسیوس:
ترامپ در جریان تشدید تنش بین ایران و اسرائیل قرار گرفته و به زودی تصمیم گیری می‌کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77117" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77115">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omUlKhBSfzdm-4rLMxTINa7Ecv-WgdJ7KsHe0eKU4MsLJDtXPFos0eV4Pg0s_YbKfsvItxbuByCY_Ut06qhnMYyMCN_AuLNbHManbDpFUfSb7YKPsgtkj58nu-wIjkLaMUaBDIy90WJYgKLwWyzJgNmLIHRCAQyN2zcKX409bbWGvCXeuSic4oen2yj-wr4nBemvrH2Xd6pRvLJwpV1Pw5MiP7EG_aW3qLpQ3IpX-aVyDq6AqMWLjkLleq-XnuxZ5jB3wGRvdiTclrh9HbG21x10yImnTZpZbci6uRjtQO6k6tBFIY1uYUv-dJbJC6xpUDacGk5_OumtpL90ApMoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77115" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77114">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا:
اگر اسرائیل حملات خود را در لبنان گسترش دهد یا به این حمله‌ی ما پاسخ دهد، با ضربات قوی‌تر و پشیمان‌کننده‌تری مواجه خواهد شد و حملات ویرانگری علیه رژیم و حامیان آن آغاز خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77114" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77113">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">توان موشکی سپاه خیلی کم شده
تو 3 موج کلا 20 تا بیشتر نزدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77113" target="_blank">📅 22:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77112">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elB1OMjkVAlT_E0CItxXDYmB-X9jJsHB7tHyyruVS0kjnNugz7WWJriY37Sm-Tj9pC1W_KEivxUTaoERKCn1zoG02U8Y0HA2Y5jg4SB1OJvfb-bb9Tzx40GwfmfjhJBQB5qsT5Rpwp8VJQv6mdLWb3gOEVWig4gTbzyS4kV7f6oEJUDiB_ic-Hq6hDLiE1yZpzYBEws2sbwnMSmTEcWJlVOSUhWbvw-sdzwfVajwf_jLjoPeDhbZov1gh41BO4lzICr7l57XhlKBuKJvKVhrHxjIHTb4RzZ9s4tCdYbIwdE28kzfbPzjb3uGDs2PI6xlvs_ggs7Rzf_AW0tmeIXOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده های آمریکایی بیانیه دادن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77112" target="_blank">📅 22:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77111">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">موج دوم حملات سپاه با حداقل پنج موشک شروع شد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77111" target="_blank">📅 22:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77110">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">منبع ارشد اسرائیلی به کانال ۱۴: به ایران حمله می‌کنیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77110" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77109">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مقام ارشد به کانال ۱۲ اسرائیل:
ایران می‌خواست معادله‌ای جدید از آتش محدود و سنجیده ایجاد کند، اما ما اجازه نخواهیم داد این اتفاق بیفتد.
ما گسترده جواب خواهیم داد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77109" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77108">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ارومیه صدای انفجار
منبع رفیق کسخلم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77108" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77106">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزیر امنیت داخلی اسرائیل: تهران امشب باید بسوزد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77106" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77104">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">موج دوم حملات سپاه با حداقل پنج موشک شروع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77104" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77103">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نت باز داره کیر میشه توش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77103" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77102">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سد مجید نقطه زن این همه گفتید اسرائیل لبنانو دوباره بزنه مام میزنیم وقتش رسیده پس جان عزیزات تلاویوو با آبگرمکن بزن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77102" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77101">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تمامی موشک های شلیک شده رهگیری شدند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77101" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77100">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">علی داره تهدید میکنه که یا دوباره ادمینم میکنید یا جنگ شد وصلتون نمیکنم</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77100" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77097">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خارکصده بدو بیا بگو اینم نقض آتش بس نیست  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77097" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77096">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خارکصده بدو بیا بگو اینم نقض آتش بس نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77096" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77095">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یک مقام ارشد اسرائیلی چند لحظه پیش به رادیو ارتش اسرائیل گفت که پرتاب‌ها به سمت خاک اسرائیل از ایران به معنای «اعلام از سرگیری جنگ» است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77095" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77094">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ریدمممم</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77094" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77093">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حملات موشکی جمهوری اسلامی به اسرائیل شروع شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77093" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77092">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">زدن</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77092" target="_blank">📅 22:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77091">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الان کلا یک هواپیما رو آسمون ایران هست اونم بزودی تو تهران فرود میاد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77091" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77090">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اختصاصی از ایران اینترنشنال:
سپاه پاسداران آماده حمله موشکی به اسرائیل است
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77090" target="_blank">📅 22:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77089">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtFCb4MSGF33aDfFyBCDjfJkABycpea3GqLWn5MJ0TNywW4P4d2rW_bh3GvtvsCMK4HPOD2I_pjeBFNr0FrFD9aiVCg7bjE7RjXJIqFL-vaAO14InoGMxHBhW7_KUNYfZF-UEHcElCKsRVOQkdSkERPuXcAJa09RxPqyb82iL_vdEOtJYsUWxTg4dFM73W-XvJ-ySG1J7xTuGVwh5HmYysKco7lQlm72AdPVuKBueOQzVgQfFvsUcSkwr8FaCJ2Nr5bHVYnT_3BhCCOkBJeVg8ZxEESiGC_MT1OkE5_aVGMflZBhbfA8MqBMnogZL5Rn11ymHM-_wYYKL_sNWCzUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان کلا یک هواپیما رو آسمون ایران هست
اونم بزودی تو تهران فرود میاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77089" target="_blank">📅 22:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77088">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA9jaR6fg9DPIuiyNRdo7oFr4LGUaq5sHoVhgagNraWdBn3vJ5CJgJ1RwCLT3hk0Ob2UXLagedYU7VNj7wSwb-lZTlWUgiLX-Ozy3fSkf88Ahbs-PAMvszjW4fnNnxQMq0kE1pNmjEIZ-Pj70HvRRBUKgzjtfDm9U8JH7VeOCSd9qAAnCvwdjscMf49a-sVzFB8e3L8aHFYyhrFuvIEibYTkn8zDNR4i0xclQDYEuYxgfHrh4m77pOEVGlyLG-zC0ncXFPXm963uavRy1FxnX-z0qO4YxeaNkIu4MMt2tLXZ-rtlZMwbhLL48ANRlIAGQ0_R8I-9zBqeaDbp1YxTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات لو رفته از اولین خلبان ایرانی سوخو ۳۵.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77088" target="_blank">📅 22:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77087">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">زنده مونده دوستان
نگران نباشید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77087" target="_blank">📅 21:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77086">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کریستین اریکسن باز هم وسط بازی دچار حمله قلبی شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77086" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77083">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KI_6eNQXAbv5sp1UwgaZRScjOcD2LVO5MSW5VzUpDc7XRt9bwcVqnRdPTE4943lc3co__kbSfJns1RoCJWMD-pl3J_8Qw_9-QEeq58UKvO0-wWKIBapHve7rsqQUI8mxdF_wpBRqyjKlm6YNTrWcijYdzQj4H_SphL9QVjZu-Ir-3v_Wob_SoePapHDDiqp4JrXI74S_kNntJtsJILu4piAeXCB4vQ_pSUX5DI9Eo3p2IV3YMln64PY7JC3LgO4riIh5lpjsU0xlpqQ42MvSiuCMT4fdpKc7IsjtXP4v2Z1hPpfKzUM46nzhYvnpAGiVwrV2rFvPXRnRTkj0BKRsUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم به نام TXICLUV ریلیز شد.
🎵
SoundCloud
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77083" target="_blank">📅 21:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77082">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgBsABSLJSwVGg9erxQNU0_sUCFWjF1I480TJe3MOkf852tBIA4zb1yBx92opD6ozGKK1fL1XuqrwQ-eqg21HJqr3m_kJamgQRSyMVQl1keL0aGYWJeB64ffZS2Ob3S96Cz5bXZrH21tRLL3Hg__oDrYGb9ZkWDIVw6uB84Tv_W3MgoBalpi8CuTsrqcGBNlU9PE-xnNr3VTraplheyaFPZYWkNT7axubb4qviyMOpmaeAC7BrruTqKR-oxIZlwcuGKwF15xbhFy6S3nU4Yt9oueXESAnptJaflYyA1-_JvSIsWq9UlUbEmq5crkI4zHmMQx8GKLFk-0Kn7vWtu8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود کلش از صداسیما کیری شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77082" target="_blank">📅 20:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77079">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfOSfbejW1xVJ_QddPeR0O7X5jhhJ84kgQZfqtXeMfTVTd8rqht2-vfypaYa-eT7Ed3EsEAlfj0e4F0hBsIMnPwg4fiOuU5JnsQBD1oo8_mtIitWVuIfwQ_yZOz7HX-ppATO37yG6cx6Y8VRfafCyxYMldx2Q57g8hVrCWCulj1OO4tfhrw_8RtutwNRsse5qa92mF6E2PXo168NIarUze6RWDc7aScDv1sNgB_XyH_xt6W82_SF-241dXTUS6B8ZbwcjFXVJJf0lEyQfK6-1QrFOOKmQOXebyogz8MiJBB7_KhzoN-KekPJWjbqilaMxudOMtHgnZJN5N7BVp_Zlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندبار افعی کردم خوشم نیومد، این سری کبرا
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77079" target="_blank">📅 20:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77078">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چه عکس بالا، چه این پست یک چیز رو نشون میده: مادر جندگی  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77078" target="_blank">📅 19:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77077">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKA-H8zQuZWepDutVdP6LGYFtB2cMw9Sa22czhR2lqdHQCtqhGCMnzO40kmKhf7EtZlI_XeEAlmCqW1UszaQ6cbXgw6iI7efaCgo3vh0STUo_FTbANUf42Cj5ha-NLEZcHQGrziMitomJEWSNZqmQQJxCDxFyCoRzD_DsTNYTmJLxmMt3HzjDJ5CiYM2lKWQFq-o08KUKwSetFRk0tVkud0aLTOMAy_CkT6ingEIPk630JtMegiGLrsYmn8n9HDOr1eSOjNrXSEk4v0aLqm29nIEQQ22cm79-sqYslu195xqBLFK8LJJKhckE6o8KELySPXPulPyNv12Pr3ljL0wFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوزرنیم‌ها در خاطر باقی میمانند  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77077" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77076">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL7zcweWZiAo2A3YA7seQz5x1WLiAVd9CjK8z-QTBKQxK6xZhGEcz6-G0RmtuAMonaFPEtDr0oC6RdjoumD-FoCLdGS3gcMh0-YYVfjHh9kBShPu1APszauhIDtKdV7epl-xgGFpBh7iunSARp2P8LvEhTY9hiN8Bh7IY3Vhk3LYo-Popu_lMduMaJvpfLJueHyg1dNYfJTN7BCwLsQCc71VGA6VuR4nV4D5aLzd5PUpoqVY-62MjLOpe8-toQhOvImuQWDKY1XIAbKMfO2xwSkCiTmaVwdXpeXAiJXklUm8gtCmT-djEBtrDPo6dckQNbl3WU3ObnGv24F4rLGlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوزرنیم‌ها در خاطر باقی میمانند
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77076" target="_blank">📅 18:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77075">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مقامات ارشد اسرائیلی به چند رسانه‌ی اطلاعاتی منبع باز اسرائیلی گفته اند که احتمال بالایی برای «آتش‌ هماهنگ‌شده» بین ایران و اسرائیل در ساعات آینده وجود دارد.
(با رژیم غاصب و جنایتکار و جعلی صهیونسیتی هم هماهنگی؟؟؟)
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77075" target="_blank">📅 18:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77074">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی و سیاست خارجی رژیم جمهوری اسلامی، ابراهیم رضایی:   ما پاسخ قاطع و دردناکی به حمله رژیم صهیونیستی به ضاحیه خواهیم داد. این سگ‌های هار باید تنبیه شوند و به جای خود بازگردانده شوند. امشب به آسمان سرزمین‌های اشغالی نگاه کنید.  @FuunHipHop…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77074" target="_blank">📅 18:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77073">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خب مثکه باید کم کم رفع زحمت کنیم به ثوپر عاپلیکاطیون های ایرانی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77073" target="_blank">📅 18:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77072">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی و سیاست خارجی رژیم جمهوری اسلامی، ابراهیم رضایی:
ما پاسخ قاطع و دردناکی به حمله رژیم صهیونیستی به ضاحیه خواهیم داد. این سگ‌های هار باید تنبیه شوند و به جای خود بازگردانده شوند.
امشب به آسمان سرزمین‌های اشغالی نگاه کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77072" target="_blank">📅 18:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77071">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: از حملات بیشتر اسرائیل به حزب الله حمایت میکنم.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77071" target="_blank">📅 17:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77070">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBFKRV3fiHoEw09L8fhyM9b61x_XVnIhMyD3Gl2w4qHff1F1ppcsZRgVkNZhGvZ7cjKLFbHqbz6YUbMseWmDJ9nIgp5Gx498psCAOG8qsyS7bEcq6pqAjLeNrvpGiksxDmNMdIOsx0sSQ-blKtnESyM3EZU2bQ1BVWfk4G6gJ-vv_u1AuNdN0MrX0Zh0NHbYSZ0VqmkWH_HQDEN9fbE77N0lvliScGjm_NExKgl7L7zsI3rqGeFY3xX3CWMexmG9iNZDkdqvRGEV5bbW06qFeATdFQ6tFXjykSMzfYDdufxxJS2oHP8L1TFCxIUzV66yckLHgHT61XHZ6bHzhKJHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اینکه چرا نتانیاهو اینقد قوی عمل میکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77070" target="_blank">📅 17:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77069">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رادیو ارتش اسرائیل: ترور هدفمندی انجام دادیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77069" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77068">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سد مجید نقطه زن
این همه گفتید اسرائیل لبنانو دوباره بزنه مام میزنیم
وقتش رسیده پس جان عزیزات تلاویوو با آبگرمکن بزن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77068" target="_blank">📅 17:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77067">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ:
هیچ تحریمی کاهش نخواهد یافت و هیچ پولی برای جمهوری اسلامی آزاد نخواهد شد
اصراری ندارم لبنان در توافق کوتاه‌مدت ایران گنجانده شود
اگر ایران به توافق نرسد، ایالات متحده نیروی نظامی ایران را بیشتر تضعیف خواهد کرد تا زمانی که نیروهای آمریکایی بتوانند اورانیوم را به‌طور ایمن از کشور خارج کنند.
این برای ما جنگ بزرگی نیست.
آنها محاصره کردند، پس ما آنها را محاصره کردیم. ما محاصره نهایی را داریم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77067" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77066">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ یسری کصشر گفته باز که حسش نیست بخونم و پوشش بدم</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77066" target="_blank">📅 17:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77065">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صداسیما: منتظر پاسخ قرارگاه خاتم‌الانبیا باشید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77065" target="_blank">📅 16:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77064">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شورای عالی امنیت ملی پس از حمله اسرائیل به منطقه ضاحیه بیروت، جلسه اضطراری تشکیل داد.
‏آنها قول دادند که در صورت حمله اسرائیل به بیروت، به اسرائیل حمله کنند و آتش‌بس را لغو کنند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77064" target="_blank">📅 16:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77063">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAScWmo6VkBiuDHYZQfZ73pUvSnZt3C3lOCWnMcjaYMn03OkvkCxqoLG-s2-Yi3RuJqqZsptrFx38RJpxXt4HsfhETOuL_2c2ZUwxRPzlfrLzfMWbyc6x0XKPNR_gSHhevY5TaBGvBR8j__ijY7jXrT6crerP0rIyCeZxukMYOjT6PbpSDJrNBqUF-G-5fGtDY6k1_poty2mEn4rOy8UnnX-5f_c9nYUAcXgLtEkXuICA14Iqs6Uf2DU22n-NLyYAlEXXC45E74hXKL4xBtpiAtI-rpuXzSmaywwA7iMtNtdGM1oVA1xrl3ccgpj7fiBplmG2FunRrcck2LTSOMtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رادیو ارتش اسراییل : ما یک ترور با ارزش بالا انجام دادیم
+ شیخ نعیم قاسم؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77063" target="_blank">📅 16:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77060">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77060" target="_blank">📅 16:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77059">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da46p9Pg-eWOwOV4k_4alq3jebdvpOYBBAwItlWhu_zs005K3ex4I9gybHFxjnplkvsmv2E75eYWCKioRWErFLAEW4AmovXHMgu0WM7glgjup7FEOEYR7wg4gQQ9GJ_Y6LpHimOHwecbYfzG3E-Me6k_fRwCx2LIGiLnit1lUmsqLffo_N1c-1SyrBO2T0nfS8B6_Fk8M6qtpIO43GA6D0v6QdmKUfNQlaBy1DMIlEvTXAU3OUTe09igkYh1kfAHPd60_7XZ-tbkCFxrr-NPS3il1fmzmdU1XCjWf9kW0d2Al__26RZxr6MDKi_ngKaIaerSJxxxekNTaWunPYntoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77059" target="_blank">📅 16:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77058">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
حمله به بیروت از قبل با آمریکا هماهنگ شده بوده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/77058" target="_blank">📅 16:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77057">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrbKKXvIbR3YuEr7pcEfz6EL2jybhmgMPiVURFUuUgOsKjSaHyL1GMr1qP5wIaoeGpFAMUJxn4f4_Ne407gEh9fxI73Ll-bIz_i6klEaTOo7tX5AjYhCBDgM8HrAkvZPMWEkfnVuAUoAZnW44pAECUFtEx26owyO3rZww00n5NOOk_xMOv_PDiIbqsQe_-kprOvt7qNLFKMx40z7RGpySg_d22EmLA3wVjPGQJNmw14eWAhZ63Y7WmOBJZmqjQk1tZCGZuqkdHITVwIfR9q6kuQfh1BZPOExqezkSkWGgkXcU9jSyVsthS2iHlGYpC6gfKChdjtkGphGGvCMPUu2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو
مردی که یک تنه داره سرنوشت خاورمیانه رو عوض میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77057" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77056">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الان ترامپ عصبی میشه خودش اسرائیلو میزنه</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77056" target="_blank">📅 15:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77055">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه گفته بود اگه بیروت بمباران بشه به اسرائیل حمله میکنیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77055" target="_blank">📅 15:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77054">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پشماااام اسرائیل بیروت رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77054" target="_blank">📅 15:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77053">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کالابرگ افزایش پیدا کرد، دیگه میتونید روغن بخرید با کالا برگتون
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77053" target="_blank">📅 15:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77052">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مردم مادرید در صف رای  پ.ن: حاجی منم با سیاست های پرز مخالفم ولی الان بحث، بحث رئاله  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77052" target="_blank">📅 15:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77051">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYMx7qqFnQcnkAS0CtU0bFL52xllf4Nl8jm-i2PiSbiy7OADUZDeTz6ZzmqJvamp_c7N2q6wLD-qOsPaJf4P_6vBgp5sEs9nV9oKdD_2dMFh1SKZJO8q20i2vBkC071LF-28WppDINauWKMcBV0KS75zHK1DzUbYgt8Uu-1bIxG2QVoJPy4YI8YisK-tTmL6GeauY0S3s7M6hYhho4nLHW_eGI6YTuNjVxa-CupDtAj950zCFUHkkWV03aPQMn1F7gAajLe8XoCMTMajLcwQV-9k_8Po3zFceghB3ISLfL3IgOhpJV2XZQz7reLk3UYE9Xc0RPi1fTgTidoBxnU_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم مادرید در صف رای
پ.ن: حاجی منم با سیاست های پرز مخالفم ولی الان بحث، بحث رئاله
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77051" target="_blank">📅 15:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77050">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SolPFylWhZ0LMd8Kcuy6L_v5gppmEp-pbskfjuxw0qc2ZYuNUofmQ9TRlXLbg378IidBQB5ykDf51GKPESLASpr0BmHOtcTQvD32no_u-FMxYZmyEVpG53Tox7yV9yodHaxEAJXJAo5drE0h83njR9XsxJK3PVP7XQESRQhhOfvf7rc7Ca4uA_ShuAC2N1QPy7BfzJFdq2IsNUShVA4cwb_adQgmPaSMIaUk2Y8ZLa2zDsfECDFHH-v8sBPOMkooY4LC2Olx3eN0slPemi4vVagYMjD1FMqGFgXYMW4iFBM6kz2I851_Ou-WTy7JR7a8g8mleke8YxL1K4Euce2TbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیموتی کصکش زیدت کایلی جنره بعد هر شب میری بسکتبال میبینی؟ کونی تو اصلا نباید از خونه بیرون بری  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77050" target="_blank">📅 15:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77049">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وکیل تتلو: امیر تتلو واسه ماه محرم درخواست مرخصی کرده تا بیاد مداحی کنه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77049" target="_blank">📅 14:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77048">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtHuRc48Sq77huMfMVLidHpazxrqLlWSF0d3ie0g99EbbTyGC4e5odYafrw1j08l6TqYz6k5EGnGcFtN13JgvzDRuDBTLHfcZlQpauqlCwz-NDFIolRzquDZa9QpxXbMcA66dBGZGkfZIO7bLfs2ixhdt0SBA5WvBwrWXO9gZsabMxhXotgFr-VMfmUiq2QEeuS1iFE7PMcy9i5uK5bOsqSVuI3boizD3qqFGYDIwEn7pQDe_jeSh6s2IbIAHwFmJYcWv10sBkwbMUN5oDQu56c-MhFMqPH6JNuV6Sc2jHrzWJK03CJlWaKu1h5H9a1VrMaeRPxcMmCsTT9XhndVjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آیت الله جوادی آملی :
ترامپ و نتانیاهو باید فورا کشته بشن و همه باید یه کاری بکنیم تا کشته بشن چون این خواسته و دستور امام زمانه !
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77048" target="_blank">📅 14:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77047">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHunter Vpn | هانتر وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F__wdScpi3cWb-tf6oWu9hNEyDkjBzU0kMzwva1haO3ppzaGp6gOsEkQo2bOdKMXXkP5hhy9o0_6QZ_YwcUAtRVt_IgTnCUVRAuQCWqwI8rlXm6iZpiAN_Jf6A57n_OQbA6yO2uXPPD1AD3qABAMaj97CC8SXO7U7NC2lKHZ3KY9JLCUtIsUIMVdUZYYwyAHG1fUrdKH8m4tWj8In0wz9pBK6wzso7AUdVuZejoNM25OHZWMLkflzwV_WhYicfeVnIN0etVIruz6ZuOGqr0_cxrKHkQ-p938DgMD25Mv6NJ1md7Lv-JTOLCkJHPeMEiyWkhzuv-rHhuJ-GjZYRhnyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش محدود فقط گیگی 2/800 تومان
💥
💥
💥
به مدت محدود، ارزان ترین قیمت
❤️
☄️
10 گیگ = 60/000 تومان
💵
20 گیگ = 99/000 تومان
💵
50 گیگ = 180/000 تومان
💵
100 گیگ = 299/000 تومان
💵
200 گیگ = 560/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/77047" target="_blank">📅 14:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77046">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اینهمه ناشکری نکنید، درسته قیمتا نسبت به سه ماه پیش سه برابر شده ولی نسبت به سه ماه آینده یک سومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77046" target="_blank">📅 13:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77045">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هنوز جام جهانی شروع نشده قلعه نویی حامله شده   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77045" target="_blank">📅 13:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77044">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrVt3KG53yiH67XPlHzkKqNSuQ7txxLYHehbcNyK_ufcerI2xCSTY1AWXaLBVbDy3vgOgSX4locY1Nt7q2nyDbUbhxX_6chuiiy50OR6adNcHdYWFs9Or4YnENqPyjSgx4Wmeeu88qOw8sAHNTfchgey6lI6ah7okHedq6KG5ZBn9K5oyzHNA9pQc_ESIlypONTUrreE79WWFdtY_LEDcN75uSJElEmhYcelUoAkc_2fy1Azg2Rhp-KOKvMEYfQRi7QYRIL0QK5bi0kya0ZtuP4GQSao7fKjnvVrpCpOfvx4nVbTcwnW5NosuIdOHZBMbGqBAapNLyYYZTvxTeaGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز جام جهانی شروع نشده قلعه نویی حامله شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77044" target="_blank">📅 12:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77043">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQa8vBBACESSq2THKqZsTB9-yAvVvbcskztx4HPoZOJ1__Xyqfoerq0CLNociZNOopAxIDwew9xo2kIew8C2Sjgi3NC_d_eXJE6NxgMN9nO22KXSQUTHPbpWoqXHg-0YCMkn38TNcUBA1vDINO-6hZe4tsWvurGMDnVqyM_BpHq7MvMXWPHGO8Nf9uCsl-rCfWL4QS3EtagL5TWD--MolK_DEsBstRtQB8Mlud2Oq34ny0zgJcJ1SQ5sYpOJQEs54DzhxSzzVAN4hlERF5XkAxPP8L6tzNvrkoLEEApV7-TV5sJq4AyH4O3_AsE_QtIw8hf6KaZP3zrCHVcwnxJx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77043" target="_blank">📅 12:49 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
