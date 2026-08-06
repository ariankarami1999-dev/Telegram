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
<img src="https://cdn4.telesco.pe/file/kEtxiJPpkxPz4QHlkN3mbf3ntNIzbDenfilj_yG8obUxjqnO-jThVkZwEFUzNnpxET0jToubOrp_gt_G6oesD-hiU_zWMvfJ5Xk11iOQQ7U3qFRM2_qtpQ8GzRBC4UHPfS8dUHV-rpHQaQF2wurlzlvO-xhR8VkpGxozF81chfXoPXRrC5RK3iYlaqCzBrbKZBqgYqZQKKCrQDRk8ubPZa52O_k39LRPWIGzOTsAFyk4W-Zi-wP8qE3y6bogIDqz1u84YUAHmuby4XCEBQwq7xCiRiSQmn_cQfh7PcNg0DD_Uae2r2DGF6Y70ePeMHk_soS2n8QeOzP1DyMvbUAATQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-81876">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edNSsoL51k5N53MDzKejFV6ENbPJin4zJ5jRcZ7UZifycGnIcJR5bY2n-ajb3hZDCvY_3fydAvegld6ejlWZzR4EX5uRkkZapOjj3fYasnhddUMI2eHblLvJOAMsfkbIYGC_SVXy2QjXjhkGaXfQ_GoNlm5tdrhN2YzPxSMUtPF376DOgdSB8uWWKYLYlkOHsndBUO91zFZ6Wg-afAHaEJ7kZWY_MrSokrZ5cJZ9_J6rLg4gzcrCYznzM6TF447L_PBrVJCh4blF4RRDv0C8Q082CeYTpAaqcR1ANtSJqPnhBhd0aeW7VPnd4fCarJQDlMYEaYzqGeTbSx94QP5cYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس بچگی دیامونده،
بازیکنی که با رفتن به رئال به تیم دوران کودکی خودش خیانت کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/funhiphop/81876" target="_blank">📅 17:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81874">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یوهان کرایوف میگه
اگه کسی برای انتخاب کردن رئال مردد بود بهتره که نیاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/funhiphop/81874" target="_blank">📅 17:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81873">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پدری رودری پدری رودری پدری رودری پدری رودری پدری رودری پدری رودری
پدری رودری پدری رودری پدری رودری
پدری رودری پدری رودری پدری رودری
چیزی نیست اسپویل از گزارش بازی الکلاسیکو این فصله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/81873" target="_blank">📅 17:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81872">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ماجرای فروش دریای خزر به روسیه چیه؟
دریای خزر در ابتدا در اختیار شوروی و ایران بوده است
پس از فروپاشی شوروی این دریا با ۵ کشور (ایران، روسیه، آذربایجان، قزاقستان و ترکمنستان) مرز آبی پیدا کرد که ایران اعلام کرد هر کشور ۲۰ درصد از آن را در اختیار داشته باشد اما ۴ کشور دیگر قبول نکردند و درخواست داشتند هر کشور به اندازه مرز آبی خود از خزر بهره ببرند که در این صورت سهم ایران ۱۱ الی ۱۳ درصد می‌شد
ایران هیچوقت این تقسیم را به رسمیت نشناخت ولیکن نتوانست بیشتر از همان ۱۳ درصد به خزر تسلط پیدا کند، حال شایعاتی منتشر می‌شد که مسئولین ایرانی ۱۳ درصد را پذیرفته اند و در مجلس قصد دارند آن را به صورت رسمی تصویب کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/funhiphop/81872" target="_blank">📅 17:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81870">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCMDANmnoBGWkjjvxY71t3bBnAuSp_v3FgSlhIDK-k1iwv6hkqCKgxfBS_yhw-nfJsbYbmWajymq4KDfUoC2-d4w-dXcFet7ZGaB6v6U8NPwXjkAU_-AHLZGP1qwWl62mm5oc_w-AEAItUlNGJ36HV0gGXONHWbEcG0Amp20pRALDA8cIVjnlV_dHddGlzJXKqdRzcD2LV0z6PsAXrFIyjydshDoN3IY2dWARh1xKVWrCQff-HGny4o-Q_vJJ8vTPjuOMNjltXOvcwcHJfKd8bKqEp1CX7KwhvyzUFpa0eoa-5nIWHYzSCbjLX4qiRDZBu6G9zeLmqcVoTErBdVygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان پیوند کلیه در افغانستان رو ممنوع اعلام کرده
گفته چون از یه بدن دیگه یچیزی میزارن تو یه بدن دیگه مثل رابطه جنسیه پس حرامه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/funhiphop/81870" target="_blank">📅 17:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81869">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آمریکا ساخت یه ناو جنگی کلاس ترامپ رو شروع کرده که ارزش تقریبی‌اش قراره ۲۴ تا ۳۰میلیارد دلار باشه و هزینه کلی توسعه این پروژه ۲۷۵میلیارد دلاره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/81869" target="_blank">📅 16:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81868">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بارسا نوک و دفاع لازم داره بعد لاشورتا رودری میگیره</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/funhiphop/81868" target="_blank">📅 16:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81867">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سیتی گفته رودری رو به بارسا ۶۰ میلیون هم میده ولی به رئال زیر ۸۰ تا نمیده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/funhiphop/81867" target="_blank">📅 16:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81866">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">81 سال پیش در چنین روزی دمای هوای شهر هیروشما به 3 4 میلیون درجه رسید  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/funhiphop/81866" target="_blank">📅 16:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81865">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">81 سال پیش در چنین روزی دمای هوای شهر هیروشما به 3 4 میلیون درجه رسید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/funhiphop/81865" target="_blank">📅 16:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81864">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwmDUSPj17P2clklEdlJqtXcnJoBehMUy2PXDFh8SezEOFjE3cQ4OrOzlejbev0NiVC-HIccqgFJiyYdiuZntTBLe-TsaDLhfJ2aYEwLxsmyCSZcsa2u9lco6IemyOzuGNJsIxEYL-5CM3krbYFC-CN0prn4Ww_d7HxFHPQLslgcUAt1XJ-oNtqnRUqKEVKD22JxdBfsTHvoHqFTDtzhkexMBRisBRREUD7ADjGY5Clb0uGeQxqALEbqfTUFHUKyi7ZtEnyr-YYudl5ZzvXWh9UG4XQL_m62SwDiw3SD40C6bd0Vtu49MUJku6B3ZZyjyvo5JuIOBHZiUxyELs6Guw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای رکورد ری اکشن توت فرنگیو بزنید حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/81864" target="_blank">📅 16:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ5HfBSMyhRDH4vWdZeV9IlOIlmZ6-jqqI-wavGvSfPzSrL0SRNQnvJLpN7qD4pEZ97W7VlGx0aX_Y8Zy8oovoZGcqS86pi9RHPTkj9-gyPsYmRVbvKRLP-1JOwmriQGkyH7JUQAwoliIyu548_Yedcpl-mNUZEB14hKtWr9DM9dncmrmYQ_v6LVS0PGuSBwHfFOhjbbh3Ez6op2cagJCWus2kuVllqDZIWVDRBsIKDRnwelskz9un0Z7V088DapaRHaT27Tz4cQT7GUaaURKnZQs6XHZmYeXMexMjDhTCAYeTQw-5LUwAUuuejD1vUzU4vPQxMlEVY8pJjwPt8tAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسری آهنگسازا هستن که بیت هاشونو تو یسری برنامه ها میزارن برای فروش و نامحدود انسان هم میتونن با پرداخت یه مبلغی از بیته استفاده کنن و روش بخونن، اینام همین حرکتو زدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/81862" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ما خودمون میخوایم از ایران فرار کنیم اونوقت اسپید گفته اوضاع خاورمیانه آروم بشه میخواد بیاد ایران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/81861" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یکی از رپرای ایرانی که احتمال زیاد نمیشناسیدش به اسم ایکس ویسکی اومده از یه رپر خارجی همچی اعم از موزیک ویدیو، بیت، فلو، تکست رو اسکی رفته و طرف وقتی فهمیده اومده یه ویدیو پر کرده داره میرینه بهش.  واکنش مردم ایران:  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81860" target="_blank">📅 15:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81856">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPH3qui53LpdF-wpU9rx1mHcEFctg_b1hAilb51_agSviBZI7S63BgPZEO_yH2vBddgXgaCXlelfHaoOe5PWD_VOBZ4A26LOnlahK4HZuCDlGaj_mq0ur2Xa8hAsqvwn-kMaYgPZU9eZsRrfmfdJ9LSZZeHVPog4eJmpHKWTKfI_a-hcWZepsywtHVySX-fXkrOT0fq0RS_gJq4hBmUGdYI8FaWRnRPkbRmF7RONAwWuL0CY8uCr7pX0gzqaxunVMsQZasEfGHjZRAo-SJhAOiouIGgvZdlIj2n54OdNbn6DTn3kThQomSZ4OoLDfnlzoKTnIqI2UZFG-h3Qtcnqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqbl1QBE05e1wHlmbMo6HpPUU2n8xys-JZ0n-CUpLuEXsi6SkLH11MEcJoG3U-skW5fXsAVgqt5hahEOmS5Mojaq9iYIswYi59c1v2eCAymhb7o-t50S7DsXGXMkO4SH98KWTYmAOvm4Dz574E1hOfN-cUmYMAJFUL_DcYUqy2S9Wt2JGDJYKvnFP82x0Nr7YKAdiMoQ8soQCYFaY1GEnaeNVr6OMf9VYUIeTfoowEQxz6RQ2CvvjktwN-hMSTI8EIXQ7I8InpeRnwaJEM30YbcbV7u14eSgTl34b-6-LM9_HdDd5jtbcANzV2cv7lPD2mz983RLP7POWMbjcH5ZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5-0uGxAFi-6wCnxvl9S33eCYx7wr2hc5jXANQEPH6tmQStVyOGZPksOBPdrM68Ba5pp1WPib0VX_sqg8pI8F8MRNMrgniy3J7KDUM4UeOHrnrxXotGUf-fecopevVkbRLEjIsYWPTiZvG6Glwle7F6EGC_jaobW4uMINreIKjkyLrdUx6TsrBaY3gmt0M_bTTGNaI2USq4md9EU-d2tyCJMeJVGdULBF4rMXOYQW2kVg1ug-5UlNc6yLr0dW6oyMSg1wRYv1hQDXlmnL9DP140NcyPXA-i1UbfOCSbq3TM-IDgCKXcIsut_44v3naa1SjivD-yz5W7QB2fhpIycpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe4e80290.mp4?token=Ff78znM4Vgg088ThK_M7BiOJOsFiH4AQw2GgDQWAUSIk8kIJjekas8NsSgli1cmIBEM6erWlniwagPk8u5Fu3TdS_GdT0XyhENjyT8rn0O3n_1iXKJp9QTQomgw1cTecWeUxygxjzhQr1xekUlnHEMqQhpbeqMrJMCWv3WtKYM_jU0nJ9qEvcHISSbPX2bEQTDKVODe9C84AGg9J6vZfsYJnKzofPiwR4_QDHknyGObISmMfmQ6Y9XZ6d1gS3UFKIN375lUXbPT-B4A8C96obOZHduNsFuMtyI-jdyloewIzGhHZSXCzomxdZf0Rye1b4_7vzlhlJrgTiop7oMRUxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe4e80290.mp4?token=Ff78znM4Vgg088ThK_M7BiOJOsFiH4AQw2GgDQWAUSIk8kIJjekas8NsSgli1cmIBEM6erWlniwagPk8u5Fu3TdS_GdT0XyhENjyT8rn0O3n_1iXKJp9QTQomgw1cTecWeUxygxjzhQr1xekUlnHEMqQhpbeqMrJMCWv3WtKYM_jU0nJ9qEvcHISSbPX2bEQTDKVODe9C84AGg9J6vZfsYJnKzofPiwR4_QDHknyGObISmMfmQ6Y9XZ6d1gS3UFKIN375lUXbPT-B4A8C96obOZHduNsFuMtyI-jdyloewIzGhHZSXCzomxdZf0Rye1b4_7vzlhlJrgTiop7oMRUxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رپرای ایرانی که احتمال زیاد نمیشناسیدش به اسم ایکس ویسکی اومده از یه رپر خارجی همچی اعم از موزیک ویدیو، بیت، فلو، تکست رو اسکی رفته و طرف وقتی فهمیده اومده یه ویدیو پر کرده داره میرینه بهش.
واکنش مردم ایران:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81856" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81855">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0baL3RXoC-W62kLebzr80z8L-8tRyiqEnJ0wCy9foD-hUEhbbR_XV8g1kGvPKY0d_iiWOdikd_X6zHulp4nuP78YcenQT2TEjyVA8F8YDg3SehiGZMLvXrdbD-R0fDhzolsPB38KPwctIwNyR_aVajlCeKDZWb05O29YL8LGlwrLrnXMAzM5eMlCG2FgtXwx4tfGKa4sHPODEjqFFEJrEzhssJqTEE0Jvhh24QlAHFt6Sk2TIrCGNzxWQrG1szxbKBuorQDs62ViGfoREtfWRQb2AUHMY17XEQQngDRuqUQtmhHBJZV1NG8VSnYwHe5KRYI-ci127QAM32u0P6M7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا.
ایسم وارد رابطه شده و عکسش با زیدشو تو تیک تاک پست کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81855" target="_blank">📅 14:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81854">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbYA5qAFHbhf8aFXRy-56n4gR2YE4b7jJxjjgGhNlv3r1sXV0_zkfLn45h6FKi_0zslcNv117RzKtyFUSSrqTzBvgk1xA8HB0dIHhrMdMfYLvBLCxi99dvLlNyhFwlxgj7c1TwkRaYh5OmYMISH01zZD0AJwJf8EqIAuyq25WawWV_FDyGDatHOLF41uYsedSykCItltNYuyAKfF3ffGMSwaSQK5kUYqUkCvvhEfJi6yTNrtWXPFAEWQRP7KOMey49nCws74X6luFA0J2q-81CE0asYMEdHL7Jp34SDodd-vArzvHWAKOCU8uHA8uPx49fgv22-Adn69KzjUNzsL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین چه خپلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81854" target="_blank">📅 13:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81853">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ساعتی پیش یمن یه نفتکش سعودی رو با کیر یکی کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81853" target="_blank">📅 12:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81852">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWD5Sss8rdtOhjxs3r1rOcFacU60YWN14-8stuuuNtK26v2SD0T34g96yIp0ugkfNHnCVsYAYAetpTKGt65c9rLwg8Q8-NnXss3IvnCZNCKHytaOaLg5gCj-jkr_KzQklfEwquMePph9enm-Am2t9piRaU0NpH5jGEPg8gor2FJIJeil4idyhgSL1kMJKmvA4CiLSCskj0-80KdMTxWbtJEUr31_ryPAgzP5RM_FAKZV-2sZqUS1CG5xn9XYoyyCVlD_9IxbOrFMCip9BVnQN1nqX2kZjY0cjsOMvdV7tvzr70BbA7wLfTqRBU0FzzEyQDXJMEppHn5ZvEGBzcGfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا به نام I dont Give a Fu*k(IDGAF) منتشر شد
SoundCloud
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81852" target="_blank">📅 12:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81851">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هفت خط لوله نفتی در کشورای اطراف ایران در حال توسعه است که بزرگترین سرمایه گذاراش آمریکا و چین هستن، این خطوط جایگزین اصلی آبراهه هایی مثل تنگه هرمزن که ایران فکر میکنه آمریکا رو باهاش درگیر کرده
پرتقال فروشو که پیدا کردید، بگردید دنبال چوب جادویی ببینید واقعا رفته تو کون کی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81851" target="_blank">📅 11:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81850">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اگه حوصلتون سر رفته بیاید کصشرای ویلسون راجع به شاهین نجفیو گوش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81850" target="_blank">📅 11:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81849">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/187d19388c.mp4?token=LYhPLlOZbwU6FxT47CZ33st4tJdk5MVGQ4qmgru7_uMvHR4xJmjtZExwpxQhwVrWcKdAFOzBnHmOmGbK5GsnwHtg3YhwuprIgIAV3mMUdxJqmdQBALL3wN0qov1LQ6IfojIQL6aZ8SpwJ2D2GiF6FiTGlCAjfgccMBH6RUHR7owUB3E63M4l1HRbX23Ms97g6-5bemxIqe7ESj2JNSN-eilKukVKIv_0Ne77kLU-0xGV2nHIveml83IIBDE2Ka8YTQDz3l-9epVQfhuxnloZwX9R8p-0tRh8AFyT_-KlR92B2t25N7F5yAnPZtjTyyp_ATvil7NQP65tZs2EcjoqMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/187d19388c.mp4?token=LYhPLlOZbwU6FxT47CZ33st4tJdk5MVGQ4qmgru7_uMvHR4xJmjtZExwpxQhwVrWcKdAFOzBnHmOmGbK5GsnwHtg3YhwuprIgIAV3mMUdxJqmdQBALL3wN0qov1LQ6IfojIQL6aZ8SpwJ2D2GiF6FiTGlCAjfgccMBH6RUHR7owUB3E63M4l1HRbX23Ms97g6-5bemxIqe7ESj2JNSN-eilKukVKIv_0Ne77kLU-0xGV2nHIveml83IIBDE2Ka8YTQDz3l-9epVQfhuxnloZwX9R8p-0tRh8AFyT_-KlR92B2t25N7F5yAnPZtjTyyp_ATvil7NQP65tZs2EcjoqMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیدونم چقدر میتونه این ویدیو براتون خنده دار باشه ولی من باهاش فرشو گاز گرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81849" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81848">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvjTx1a7vS32xIdM19wZpFSy_CQ4CSEWfGiTloAPh4Rhdpv8k6Rb9gjjosfP1ByW7BFNkpevGJ6fFTbgbNjULb5_kQ7LOnK7g8yOYfj5hGN7SKDpH1dI02drY0-Bv7Zq_-oK0XHltUDoWGej2OuoLdfwt8Dz9u_cZTCT9QT6y_cSzr1nAxORg2IJpCdDh5Rdw98FRSm_AOZ2IDhdezf0U4VGi-iixCvJUECEwrMkzKzazKGhykgL8KerKa4w-V9n8xz2zci7dK1jlfzh4TC4CflCeEs5azxnaBp-1AR7-LYIMrCpoA8IRUk5uNVqppGYqlFL6cq3tZeVbRtC1uS5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r15
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/81848" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81847">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جی.دی ونس:
در حکومت ایران افرادی هستند که می‌خواهند جنگ را پایان دهند و تندروهایی هم هستند که خواهان ادامه آن می‌باشند.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81847" target="_blank">📅 11:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81846">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3H6tSKLRQLasPMlm3nWLYbosuIx2L_1Sb_3_xOEPxXYZVZReP-ACptqvlAJrULA7iISqP_hi_taVm_Yxpbua7rgHecwC73LRUK5nHkfQlq8XPYAubqZ24XkMW5ZjzCdh0SP-yEs0ivDs08N3KwDPasp5AkpxB1leId8SaKdpMXDbQjnDqHIQxzhX6Po0IvxSr-DX15EI6IKeXj1U42gmQBWKfIw34vEtnWRzasXhUhu5-Sl9Gs1CEzSc0CbahZSwV36_K9Imw1dkz_LBFcAufogfUFOnb1a0BvVDmT71oP2YaYdeCDIMAWUNdvU1qtY3tfr6JExvt6EOR1WQAr2Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81846" target="_blank">📅 11:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j13hIcxFZxDjEqlPXGjzH-Pfi2DZYu6E3w7t3p6mhKVFKTYqCdErxzrdVm9KPOaZrhmpnfObf-tExj45aDwM6i3y71T27L1gVB7SkSQaan4xHXjOWn9Tj4_GUlKnTZm8zCAYe638h29cp6SGDL8FyWk81NTgWZrFUKlr2KufXTnYXJR3nL5UHUx3-A8PjDsbnHDk_0mjeBpXRVD8cg-crP8r3No30T5YLye4HkWxB9y34l8P5qE_ReaoTsLhBg6WaOg7s3BlxcqsDyJ_WzMDcCZpf4N3ZW412Uo926POWIKy5unESCyURldL8-iaCv_JsmyTLAdnwTFHkbkpMza0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81844" target="_blank">📅 08:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81843" target="_blank">📅 02:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حصین درحال فحاشی به فدایی و مهدیار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81842" target="_blank">📅 02:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m17CHoLvivyTGah7kI7UDl5q8yKtS-ybTrSyIL0nhs3zvBbWX4Gv-5MjFHM5dAEQaWzKvd3zEKDJVjtVkJb6p-gCnQr-y_AnkSFaI-Cnr_cNvKWP42YMXVtk-xhmZS-ztXwlFxzkK5Fdx8zS5lFo5wvCQx2nQX1vDxDjBI1T_EsLtEtLrXwv3jAUQ-pQQw4iAqTxSVchkxKbbDgWm9Dg28fTmmpqZpJXaviaEadkI0vZyaZoxRKLpV7TMXdt6nEfirSL8TMAaepdMVrtMBMSeiMJpsEZsHkgu386AU4PyV3QzqvMZCfNGICpEaqt43ud4KYEFJ9Fq8yUb4oL0mTBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپدیت جدید اینستاگرام که میتونید ببینید کی انفالتون کرده، هم دیگه رو تو چه تاریخی فالو کردید و حتی چه پست هایی از هم رو لایک کردید و چه کامنتی برای هم گذاشتید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81841" target="_blank">📅 01:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnBEU7a9Wly_0ueKVsdhUbxdgQFf3Jr86l2oIOr3Vf3XPwLbn34MyZ1wJv_O-fkdnoXrlkfaGSWgRCSy7MkzR6JPlYtrX3gNMwjON4lTshXKfQZsXR6o7xAJdOaa0N6TeUopc-gxpGtpqs3x0IwPACkFwXNo2RedQMgOhQUKsCeQoMvHWtGxVQML8LftAw9TjYqT1cxV4aHd20QJAiB8l5_yeUvcy6W15yRVG07WdPgZcNivoWW1mT5jybD54allh04yXYtUviUJNBVPiTNOfXddaeuSlSxuCYqqL8_iNg1TsKtXdPAo2Gj48XQrDi0JIne2lnjL5mjmoc3elnMx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت یه کاربر زیر پست تلگرام:
من آدرس مخفیگاه پاول دروف رو می‌خوام.
ادمینِ اکانت رسمی تلگرام:
اونو که نمی‌دونم ولی من رو معمولا می‌تونی تو خونه مامانت پیدا کنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81840" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81839">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سهام شله با کون خورد زمین
ارسنال 3 تا از بتیس خورده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81839" target="_blank">📅 23:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujNDcOTPFORGbUcz-Bt9z08J0O7WKkPWg2CCe5EuhcKkrgI_7svqb3OYKbMzWSlZAGTi1BZd_f71sKZl0mtN6bClNAHA7S8BfC7Kpf_BX-K7LvvGFCn5qpvoIOwWaidhhoIG5nMi8AsoIxz9IFjuAfsCebdI9IERspUqE9domjVhbGYGx3Olb42NH1Q6vpKGR7tk5IhcxSjnxDMhc3NwhRFnEWUzL0vHN9zdM2ZVNZG2MlCA96REbsw7UUidx4KYfM3Id5iiBuG7Kqg4MaxUioD3-iCO9oho3L5A1ikAJ0Oc4YMLMUCxTrG57RIrp_UyZrSh3v0t5JeO9L6eORdEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81838" target="_blank">📅 22:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81837">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترک جدید پوری و مهیار به نام "برای تو" منتشر شد  YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81837" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi8ssFhP0tckIuhIH7KqJGrpNwun8DypSxMLcddxynTq5IajzMGSzkkBgrSYkcrJ466JEnEF2R1e_mdhNNOpyBMdiTuMIDT0RvfTAoHloRQ7rUrBoHwyNqd4Xydi6e7y8wtZwU5YA6e5wN8ffM1ijHpgffQIGffasGq6FrZa-ZtnnLrlHHAS9tBXvILcHSccu0voFEv-xkEDLzxqVqRBBl-qKJlc8lvWeJPeLCbz41Z6_7aoAXdFOGBXOwMjC0xokCeyNrv9vwk3T7ujoXHYILNkYQYOzmgnhRl6jOtnu-bKulzyhlpW-9YZZR167zEsg62VzNpH5biHRcIu0p_r0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری و مهیار به نام "برای تو" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81836" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اخر نفهمیدیم ساواک خوبه یا بد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81835" target="_blank">📅 20:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCHzRBKnRly5oknNzgJkhcI7o25uDcqKc6ejavoAu9MiXM84jlyR-7IR0CWrg1EpMxzWci5VKCVfzWOD6K_yJ9YXcCzWtMV3mfAXLaPmXavtfxpU-QW2re3W_gRluxQzIgaQSRYJXN66cpyIsvIHKVYyoPBQX8qyat1bO96ELM4yzcNPMasK4doVG8H8qy1DJNKBGll6IUB4VweG9BcqYcx8k_euyeCAmkSv5c1qhFLYtnw8w1ZpoDcubcKs1jI9DhXlU162rQPMhVSx6ewDhOGFx2CQNfFtzAbQwAYX64t4hU60-N9FWSwohoK-iEPGLUsbRypLRopZsZusdplkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس قشنگ معلومه چندسال منتظر این لحظه بود یه آتو از مهدیار و فدایی گیر بیاره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81834" target="_blank">📅 19:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پوری و مهیارم ترک میدن نیم ساعت دیگه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81833" target="_blank">📅 19:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81831">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFOj63I0ZQSk3ESPqDoVejUBhiLyZFnZHgByfEwQ0-WMlJ1yljDxEFG5s-8ZwLpPeoPOHNjBiHUPZOQxebNRnZ92rgF5iMk7TR7Pf_TQdOO23bzdYaijLxXPz_TkdezyF0oPxWPxCx4N17I-SXOa9ByzdreI3a8gv5c5ustx_hE5QeN3GW0pWb-c5TojBduvmOqUYIgg9W-URhJ6srzXseGKk5o3DbHmEsoIBnm4Kjyoq00mhJL2xzxtpOawjKKmriDygy4fZR2phtfQWid31wx3cEj6EJsY_Zwv-c3cvzfujzNK5DV_-JNsWCZfdnMQuFkUy-8agwoYFVpHvxoiDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دورچی به نام "EDGEBAR" منتشر شد
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81831" target="_blank">📅 19:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81830">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81830" target="_blank">📅 19:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترک جدید هودادکا به نام "میبخشم" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81829" target="_blank">📅 18:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81828">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STv0hBvoSwH4pQbVHDCAoO6sZ0hxEuW2W7uwkKSmbV51y4fgCBi_QI8_oI5Qpd2ahj8G34ayopIisl2EUeSi4v2u2QpFPnecdE-0ZQcBt2IMtrJ33XUrsnWlzX5izPaHoRQDGbhESnd4uX1UdTcIL3JTPxvU488pUyhDgzSxVXt7NNb6DKrlhf0_dDx13YFb-rhYuiQnZ97Mc09Pe7D3-gK1RktniTUt74ZCbJlg8K5RLhTlQw0V0D6Mm0zNw17gxrAz3XHTEb56HdQdChTu0-N5HCOICIjRbo-202ACBT41Vs6Otv4yBdWywdO0Y88kFI2W2F2Y5NvarcCHyPjipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام "میبخشم" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81828" target="_blank">📅 18:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81827">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کیر تو رویترز و رسانه‌های اصلاح طلب با تیترای زردشون، تاحالا فقط اعلامیه لغو تحریمای یه سری شرکت هواپیمایی متفرقه مرتبط با سپاه رو تو سایت وزارت خزانه‌داری آمریکا ثبت شده.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81827" target="_blank">📅 18:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81826">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMg0mydFvaeCI3kZlFBkDLJSlZ5PNuAiUDG2_LV9abQxt43sXO92QxoQSFrXx2uwbEkgx6PkzXHkMH87rTWE0ORbEelzqtJAs4IItncHZ6LfE1qJ7KrzI67cbmQ6fuXz_y4zVhUZnM20PPXeGiRcynEZpVrnpVJAjwi9ejRsF7PsGshWvqDF0Vjvvfvg8_Mn69AGycVjAPHmCGPKCB8RFL_ftP9YFIywV7Q6PfjEBWnrqHc_lcBldBFF1n1-U45_dUr0CiMH4LcZiY5p7ic94xoeUAdN7TNtrKiIBdmKa5-0ozpf6H9cZ6VghnmBdX28E1-vn0TdqVhgyCIntrDgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوریا پورسرخ چه کراشی شده
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81826" target="_blank">📅 18:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81825">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81825" target="_blank">📅 18:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81824">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رویترز هم تایید کرد، تو وبسایت رسمی وزارت خزانه‌داری آمریکا اعلام شده و قسمت تحریم‌های مربوط به ایران آپدیت شده و اعلام شده که لغو شدن، حالا اینکه همه تحریم‌ها یا یه بخشیشون مشخص نیست هنوز.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81824" target="_blank">📅 17:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81823">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آمریکا تسلیم شد. اسکای نیوز عربی:  وزارت خزانه‌داری آمریکا اعلام کرد تحریم‌های مرتبط با ایران را لغو کرده است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81823" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81822">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آمریکا تسلیم شد.
اسکای نیوز عربی:
وزارت خزانه‌داری آمریکا اعلام کرد تحریم‌های مرتبط با ایران را لغو کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81822" target="_blank">📅 17:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81821">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اسرائیل هم وقتی توافق ایران و آمریکا جدی میشه میره عصبانیتشو سر لبنان خالی میکنه و خارشو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81821" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81820">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حسن روحانی:
یه سری ادم مومن احمق کم تعداد که با اسلام زیاد اشنایی ندارن فکرمیکنن اگه این جنگ تشدید بشه امام زمان زودتر ظهور میکنه‌
یکی حسنو بگیره تا غرق نشده تو استخر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81820" target="_blank">📅 16:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81819">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هرچقدرم بگید طرف اسکی میره و فلان، درحال حاضر هر ترکی تو رپفارس میاد و اسم کاگان کنارشه مخاطب حداقل یبار پلی میکنه اون ترکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81819" target="_blank">📅 16:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81818">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هروقت اشکان کاگان ترکیو درست کرد که مثل رانندگی در مستی خفن بود بعد میتونه بیاد نظر بده</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81818" target="_blank">📅 16:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81817">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5nJjWTsdeTMBO-9KqfzJcXE0hwx46OyUiwBU8RwX4oWJtLurZVXAHr31b1WcA7GMfpDyGYj6s6ODR0_a5gUTfDJ0oOmKbt1i-G2HLPXgr12H1CRhd4XNIWn-h1jK4DgnBx-YFeKcWr_2zEuTtTWqNLDwqD9CMq7lKQCl2lCAJFs5_mG7AD7hV1vEq1jySgIbDR1ykr2NLLGWVKevUK_J696saj2JJeareOg7c7EFTByiNFaGk0pUQ9HVwdpLf7FKW6n7zOZHSolbbfbYmqdBg6IHSmFvzJ3COFS4dl-yWVuCbj_ZbO_aNIsMwSYm-2dNEwoW3ugIp5uu5oCjxDUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربون دهنت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81817" target="_blank">📅 15:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81816">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07a77cdda.mp4?token=HQDxzCyi7tRHOQuxkW-IiDeglqVpjjMOaF6HznYDLz5X23Lj1miziPozejCy1w5Y2GrNk6HzRwXB2eyC6WkdOeon7MjmZ_7iHLrKpftIB_m1QBnp2iiU-AAPZCsa2JonF1Fg0qTZRgV2XB5HAtrAuwqCMGTWQVx4dHqnveMKPu8hVh07PdW1ptv3Xy-8Jy29CEzB9ue9kU6XYb-m5tnGkbV8BhUA2t_Sesb_TSXXZdXvcRL3rpqRBKSUQGq59gMWSQ8kNz46zvPe4V9nPEt5dYBYz5h-sKtYgy1r-InkcGz_rlOnkZTP8qeIA74fz97BE1_VCytKMkxllrDdcMVTcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07a77cdda.mp4?token=HQDxzCyi7tRHOQuxkW-IiDeglqVpjjMOaF6HznYDLz5X23Lj1miziPozejCy1w5Y2GrNk6HzRwXB2eyC6WkdOeon7MjmZ_7iHLrKpftIB_m1QBnp2iiU-AAPZCsa2JonF1Fg0qTZRgV2XB5HAtrAuwqCMGTWQVx4dHqnveMKPu8hVh07PdW1ptv3Xy-8Jy29CEzB9ue9kU6XYb-m5tnGkbV8BhUA2t_Sesb_TSXXZdXvcRL3rpqRBKSUQGq59gMWSQ8kNz46zvPe4V9nPEt5dYBYz5h-sKtYgy1r-InkcGz_rlOnkZTP8qeIA74fz97BE1_VCytKMkxllrDdcMVTcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قربون دهنت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81816" target="_blank">📅 15:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81815">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOqN1CM-tgUsjYYWwH97kqpMyJdetNEF1l1zWKEgrS-sWr1rWSQcKoa9q5vbSC0gOcsnFAOJPg23FaWkwPkvilVFzp7XaIbO3OOtyVCdFr8CBsU6UThH7yPVv2OJ6B7SydwXh3ByGTb6AfLJLO3kUTJ2vOh1RpU-Syhl2pH2qmCsDnag3zPgSGursceXhfkthda8ISLjcVYo4ob4eJd3-RlKW4rcuK-rJjws-WH-6WBQgNVsAiNIY2Nsx_vNyZUoZWYLwrhO70n9gnO27U7JsB0fxo_jvKc57vK9qyg0byNUWUAZlngExrzoBlgpSf7qwLIKvxW8wLAgbTXDBKes1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربون دهنت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81815" target="_blank">📅 15:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81814">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دمت‌گرم کلی خاطرات خوب کودکی زنده شد برامون</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81814" target="_blank">📅 15:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81813">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_-HSs_pqK2sRT80Jy-eLLcYLvZ2iAl0zDaD9Tak5D38_YXH0x4yZltbKxTPB519oppZWPR_KvHneTH6ILutRf1LLdn_mdHFYKMKjF9-Q11Qa0rCiR67o7mT9UtLTWl1HTmnl11N5f4zN02Uz4f1uQF_e3YGz-A53Z-oQIXQx3oqjo9uK9ktRr-jY5VkfvU_4r0dQvF9XrNESVe2FxcFPC6b2TnX3cDCkaCHCxP00y_NPhx097pqtDr2I1lVaieJCXhtH_u8NLalXL2nshR-qnK9HMENfe0uUv0zJ7B_ZcTRXSbCVgsDfmc7zLtiGBbaB_3tmR9XT4VX-wdSgCe1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم سکسی ترین خوراکی دنیا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81813" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81812">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چیتوز چیپس با طعم چیلی تای داده بیرون.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81812" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81811">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3jR1K1yO4Wcmg-D23-UVzNz8IzjQvJHOVbTdglN-dD75TlYzztaEof8SncEQCiUXqOyEwG2JUZBD3S-_duZ8OIz38WPPGuFxEYxCbYD5IF299Lw7uq-uMG68dByMJdLX8FKKhmhw1ssglBVLaPyjR0bK2dXSsyCQaDXW4USz1GA89CEh3LpDBFFP3N2SLIvAZluJiNbD_V0agxnL1auOKUDlo1FEw55zTqb9reurgMKPJsjPKX_wtNNQ6AAac29rxt4RH4NfeayjQZJ5gwdDk5Cdpr24iRpYOrp3CAgSNrzvtli1lcf7cZn0wXcog61KDOBVxsPshNlHQyA_ckBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیتوز چیپس با طعم چیلی تای داده بیرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81811" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81810">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/127bbc39c8.mp4?token=GUAWXhwuVGb87tFCmJbjsnRyM_NpxA4xch648QqP1HB2MtYL5fNaYf6TVZyNd8ia4r2W4A7Ixo6yI0HMSUULkeGTXj3GV-ulqfyqrmIDIWCTjzK7ue6w-eV9iW8o-yyVj__K5uqSAXE6NfSk2visDYgK9BM4wLYLLtSyYWQy1RxgtUNmKxDze-KM9V8rVbUb4aNXs3AkepP4rqSPF3zl7rsGDpeYo7Smn1o--esKDp_RrZ9YyW2YMA42TzuBWKNWgw68-BJWls7wBPtwMKFcRdNSkRE9vJAxQvHYmdMufNV_JDaK7h4k2qc0cjkY8QwrcINR-4LgwAB3LdaMrVWXMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/127bbc39c8.mp4?token=GUAWXhwuVGb87tFCmJbjsnRyM_NpxA4xch648QqP1HB2MtYL5fNaYf6TVZyNd8ia4r2W4A7Ixo6yI0HMSUULkeGTXj3GV-ulqfyqrmIDIWCTjzK7ue6w-eV9iW8o-yyVj__K5uqSAXE6NfSk2visDYgK9BM4wLYLLtSyYWQy1RxgtUNmKxDze-KM9V8rVbUb4aNXs3AkepP4rqSPF3zl7rsGDpeYo7Smn1o--esKDp_RrZ9YyW2YMA42TzuBWKNWgw68-BJWls7wBPtwMKFcRdNSkRE9vJAxQvHYmdMufNV_JDaK7h4k2qc0cjkY8QwrcINR-4LgwAB3LdaMrVWXMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان عذر می‌خوام مزاحم می‌شم می‌خواستم ببینم اگه کسی از تاریخچه‌ی این فروشگاه که پروردگار مسی دیروز رفته بود ازش خرید کنه اطلاع داره لطفا توضیح بده ممنون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81810" target="_blank">📅 13:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81809">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ گفته تنگه هرمز امروز یا فردا به طور کامل باز میشه و محاصره علیه ایران لغو میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81809" target="_blank">📅 12:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81808">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپو برای بار nام میخواستن ترور ‌کنن
حالا ما که میگیم ترور، ولی شما بخونید paid actor
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81808" target="_blank">📅 11:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81807">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob0_oGN9AdL5VNKAFaYu5BqoDoVQF3DrVhpiRJc2n7v8Ndzun02etUF3RlJbHfQJkolTmJthSDRu5Met9Veo7uWCa16s1io-IEj4EGel9Dn1t8nDf_6ezMZPuw7ySZc5zFOnQR-RVZdcD2N_5OJTctGS9SSCvr1ftI0My7DKKph7n9qePZO4QPSpZ717cW9VyNa81pHQ-RIODee3_SgQmqHnZkpLm1Ag8K6gznOCh3h5LmqSWkpfCsZct0G2YrO-OoP1HnveODlTKo40xqQoOMUlHGFgrMRboD1u3erjaCKdrKS8vbp7vHrisNPz7oVdvGoUWK0S4UkJYq-D8bmJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش به نام "Fiancée" منتشر شد
Spotify
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81807" target="_blank">📅 11:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff90305b6.mp4?token=rsdUwidDNnz-DLsRvqD7E15nmxsU4mJS8VHeK7VyU3DPfDoxo-cG5D6P27oWSLwD8m6qLqCpkJS6q3TRCDmLyGaLiAbEuVVo4fnlnsJyBMTfHJ2mOS1_CN9EUwh-GZzzRwa-L-nY_KscI1B_3E1lIvOj4zNPjhvdfMGxp3mF0J7Y1HPsx_DiNZDhNZ3szZff6xoPT-d68Z74mDbV5GlQsTy90WK687FRThg4WekIGd-Aeh4EMcWRgjE1fE6YH96mljgfopCyPRoHeitrf4kryjHsQ_eQQy3cnxARjuI-zAtRglAfZQOajJ2cy3wClpfS2zbUy9XflhMDMSzgSuB7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff90305b6.mp4?token=rsdUwidDNnz-DLsRvqD7E15nmxsU4mJS8VHeK7VyU3DPfDoxo-cG5D6P27oWSLwD8m6qLqCpkJS6q3TRCDmLyGaLiAbEuVVo4fnlnsJyBMTfHJ2mOS1_CN9EUwh-GZzzRwa-L-nY_KscI1B_3E1lIvOj4zNPjhvdfMGxp3mF0J7Y1HPsx_DiNZDhNZ3szZff6xoPT-d68Z74mDbV5GlQsTy90WK687FRThg4WekIGd-Aeh4EMcWRgjE1fE6YH96mljgfopCyPRoHeitrf4kryjHsQ_eQQy3cnxARjuI-zAtRglAfZQOajJ2cy3wClpfS2zbUy9XflhMDMSzgSuB7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی این چیه آدرویت پست کرده اینستا، آخه چرا؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81806" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptyuwBsTrkL5GWydPMxkG4wbBVS3MNupIulJ4Xpa32UoptmpuaIXKXsdXaJDcCdmvASfIFKNQNAsc4M1tWL4Qcczx2GY9kJT7sAKNBfZWwgePEcNLof6QBIlx14nONWss8weUSE4QKmBE2xYLbwMEbulr1d3AcG9OdZ6jAf3AEweqU94VkN1EthF4uDyBjMWmmc5hAwBCO_4TrdmLwDOynEjr4dv12b7YTK95mO8yiUzjmQacoMRJO0gE8dbgXLPxoBm2y7T80dtWhsTA65BUQpoK3u247ynlgbZtJzeh9BonjD-mul0cKKMHiX058dRaptJTRI3P2B9b57z_zlSCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81805" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ : ایران خودش زنگ زده مودبانه درخواست مذاکره دادند نمی‌دونم چرا انکارش میکنن
ـ داریم مذاکره می‌کنیم امیدوارم راجبه تنگه به توافق برسیم وگرنه ضربه محکمی میزنم.
-تا ۴۸ ساعت آینده خواهیم دید چه میشود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81804" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81803">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNuLonXxSDE3bkv08H4ocWxghg6r14tqLjeHRHqwfyo1efEQWQcGJYlaLipD0n0fy0cacdDGIeU89xYQB3U9LOJNe64tOdwjtZ8W4LqziqKY-0_O2DFH-EjLL-2eOV6X0C-GciR0qQfpf-dt89vhiT6OPGn04MHxnPKtJGcGyWZCzijtAE8P0T7ktLaieDEqiX15eDpvPzCl-r1JQlNq8s4ZY8D59HDQzMxCQwyR3vB2pJiZTkneqQjGbj7qmVFHlN5RUvI4KV4HIGVkOHxMIuprJGRNE5B19ZcAR0-525PPAbQ1-_eLwrPeXoi3IYeLd41VFOXjp_BbAqORDi7lYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81803" target="_blank">📅 02:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81802">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7efVkf0fHhFpVhAUOBLc8t548ShbGVl2iKGi_KCezlOs0cwDKIymXZFcUFjy2Bd0qr1BAo-NDBLi8ZETyxa66Wiau1xWSnQAN0HEZcmjUyAGG0OoPb-ZNejLfN5TtKYljqnnnvqiEF1bznrXnR8ETBwGywq3d1DFd-nwJBbCsOovLOK8JZKAuL09ulN4xEbk6yY6ZGW5KPrm-ghF5ySo3TYU6pnH4AAxoY64QvNweNMHZlfbV6SaoHAcM-P451qwdeFe8KfbOvxoCBGDjf6BmrubofgGp8WdE0J_1591dvL2UIxGWvmOcjK6GcAiU1wrtXs70SV7adJz0kHoIKDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد هم اومد پیشم خوش اومدی سلطان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81802" target="_blank">📅 00:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81801">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from꓄ᥲһᥲ</strong></div>
<div class="tg-text">این ناموس کونیا دریای خزر رو دارن میفروشن به روسیه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81801" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81800">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from`</strong></div>
<div class="tg-text">این ناموس کونیا دریای خزر رو دارن میفروشن به روسیه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81800" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81799">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE8cZa8EflTpvVH7jImzout4RlQrCdCfX9WlT1gj6s202RkeP_2-juvXjBH3Ofz7k_CV66TFP9tKzREKdEqM2YmMHnY6YhY5OAkpvlLba8PmaK_Ng1ieK8KjJAxR59S20XzXGanmlmGM9QhoLzCGM0Yrv03nTmZt2pdFGblIWX9XuHo9kvXGjxG-S5srggPPxH4BNIE2nafchGaKBFk9r4oqt5LD9HPdASRdW0YYKV1piD_88BSxzCgoOuDr4OpBsShAukLqOcarF8CxO3Aw6QJtK9hNG7dSLRf8fOJUbhy3tLNFHKtSHLbLTZqiqo7pneNJEOTeMZPYupyP-rf8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میتونم زن مدیریتو راضی نگه دارم، میشه استخدام بشم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81799" target="_blank">📅 23:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf7uxl31Mn0Rf9cgEamSjHmuyYec__fU53rDkQ-Cvn-SSqEwy5pMvxGZGmgt9KPCmDcr8ikLgbJ-R2NvWLfI0FS5SBRIYV5LQS6zN6PlStZBq78LIf4DbYlCXDyVa1HsZpW-RdMYTViXVi0mD_cPqNgFK7NfFHLAQuYymScYfBsARPyzrpUFG5Y_RN-T59Wzg8GLG1Sn0JPV4EhWkp6p9m83pP5GB9LN0RppP0LLKLhtVMkNqdoxjN_mPE6eKuwUqflA9gW7MGSGzX4WlN3P5j6mGOss5TRWLEzTPbtpi8r7rYM9pgbxld8gc287EliuO-EMmJteHoOMNjmknWEWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال پیش تو همچنین روزی، خیلیامون واسه اولین بار تو زندگیمون حس واقعی شکست عشقی رو تجربه کردیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81795" target="_blank">📅 23:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81794">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfRdtKT-PyiUFN2yjtur5Le4nTqn4N_TYfFapPSfnxmx1PEveK8buT3FjNYjKNYlShhLJ6gFKzsW-51Us9yqfoF2811HLlKQ6ppJ20hsrzsJtT260YsaTHuJz4VppZ9OWEi0CaYw_7L2Ma4LO8vDFCXMxPNpZZYuPBkiaqTjgzrmq5rnxmUY0tkcxhQOOqGcB0g2NgvG6FLZRGfpR3u_4SSgoST_eZCDptN4JelhH1Aq_BHcrmd42t-UV_aF_iroFofqpJ1eTLHDqiuhq-O9GwLuR4h3RcGVD7eHrVTAG0-2df5ODjFM_4aPW2Z4DgH8s9pe0hIKRLZ1lSWFI1tcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیک
جیلنهال و پارتنرش از هم دیگه جدا شدن
💔
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81794" target="_blank">📅 22:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvGx8B6efDWTAU505hlC7xzrUP7wOqGiT5WbPSVN0qorpFO9eWpj6LA0yr_lcYB0cEoaEmgR6IuNnDygRuG0XUG362zzJF-AA--uqYH0gXSnBypfMHpAp2PU-LPEndUPvNBrJh2Nm7TKJw98bRb-usXbDkhSlr07Bc8HkZmhaVSV3oEEDJYdyepzyI8Om-KQbYEgDtLBG0ESdt4Z20g19CuViIDUib30QscS3RJPixsPwSBkPeKKJSxUqrJW9BNGf_9qvswk-wcQHDufaVXLyyadf_KMi6j0hFIcX1jkRx4IP3-RMq-Qc1zd0jH8V5Qud5OhMazsfgH4dK04pZFzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپر اپلیکیشن بله وارد اپ استور شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81793" target="_blank">📅 22:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81792">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGG0UCMko27QNaoYsA5Gy8P6cKJyYnwd27NI2TlX_e58LiD-1DSMtU2pjMokC5bhSBRtz2r1kyG0PKqJ-FoFODLhMMjXTo_tZUdcWVxEIAI4yDus1EZ3CqZG34g1y1Aib17j4bCnYhO2XiNdfZxjYLr4q9e64Q1aPIU-vmPJ2lQKeWG1hRUq-h4BPVTFbZpNwhXq234yyFmu-Y42w2-i1jJM76-3vf792_LFHLSr9z4U7EE6HIDjjkXJSY-dmqMJV-f96KUsc05itZ41iZGrReUMXqlYInjGT25CbcfsBHPSn7pAwKoteyuVTIdbla2ZM2WOsRdFnQQV3g4nnPIvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81792" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81791">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ارژنگ امیرفضلی:
بالابرید پایین بیاید، جنگ کنید یا نکنید، موشک بزنید یا نزنید، توافق بکنید یا نکنید؛
هیچ چیزی به قبل از 18 و 19 دی برنمیگرده.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81791" target="_blank">📅 21:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81790">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06551d5d7.mp4?token=Ofu0cOS-xcYKAn7Yi1i45EEoxnq3Mo0duvIZ0ZGb37ejIlZqEqGsoH585n0zpnqEjqgYes-k83teHo9QWpcXXYz7_X6EjjbbpKfjEDV3MjEVEWjfUVV8vnNf9NIOBYxNFlyxgcO0tClBr-7JeeR5n_aT8uV0jq3ydz32cseUw9oaveCXGUASLmPGIUOijImRXiMhSh9hm0sQ7vULSSA_L4_XKGR-Ox98xtq_tVL6oBHVwNKxX0EgVo0iFnq5oOcHL5EVwAewfW_-tpISorNa9xSIfzv1m2yDsO8-nBF8tkre5KCzgnpklpksx8AYLTH2BoaDMFrO3CiPQ8Jx1v7NlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06551d5d7.mp4?token=Ofu0cOS-xcYKAn7Yi1i45EEoxnq3Mo0duvIZ0ZGb37ejIlZqEqGsoH585n0zpnqEjqgYes-k83teHo9QWpcXXYz7_X6EjjbbpKfjEDV3MjEVEWjfUVV8vnNf9NIOBYxNFlyxgcO0tClBr-7JeeR5n_aT8uV0jq3ydz32cseUw9oaveCXGUASLmPGIUOijImRXiMhSh9hm0sQ7vULSSA_L4_XKGR-Ox98xtq_tVL6oBHVwNKxX0EgVo0iFnq5oOcHL5EVwAewfW_-tpISorNa9xSIfzv1m2yDsO8-nBF8tkre5KCzgnpklpksx8AYLTH2BoaDMFrO3CiPQ8Jx1v7NlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی: رضا پهلوی مقصره که به مردم گفت برن خیابون کشتار دی ماه کار جاسوسای موساد بوده، کسایی که کشته شدن بخاطر بالا پایین شدن هورموناشون رفته بودن خیابون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81790" target="_blank">📅 20:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81789">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">طبق کصشرایی که گفتن، از این به بعد کشتی ها و نفتکش ها از آب های تحت حاکمیت ایران از تنگه برای ورود به خلیج فارس رد میشن و برای خروج از طرف عمان رد میشن، و در ازاش آمریکا محاصره دریایی رو به طور کامل بر میداره. به هیچ کشوری حق گرفتن عوارض از تنگه هرمز داده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81789" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">طبق کصشرایی که گفتن، از این به بعد کشتی ها و نفتکش ها از آب های تحت حاکمیت ایران از تنگه برای ورود به خلیج فارس رد میشن و برای خروج از طرف عمان رد میشن، و در ازاش آمریکا محاصره دریایی رو به طور کامل بر میداره.
به هیچ کشوری حق گرفتن عوارض از تنگه هرمز داده نمیشه و ایران و عمان باید تنگه رو به عنوان یک آبراه بین المللی بپذیرن و بعد از توافق کامل و پایان شرایط جنگی/عملیاتی بین دو کشور، ایران دیگه حق نظارت بر کشتی هایی که مقصدشون بنادر ایران نیست نداره‌، ولی تا رسیدن به توافق نهایی ایران حق نظارت رو داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81788" target="_blank">📅 20:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81786">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esyyxULBcvoPdI4EETi1YnxNbpkyLeHrjsStM2lNVaXy-uP_Ns7HibcTAp97P8_ShFXDKpkcU1-5m0UgvvmzZj4yFXzEn2i3nsXG-qNrd8JjxDKu18PuX1M-NbtR4q_F9aCqobCeZXP1HR4saknlQL5heUXZVG1duznGn1uk7rDL8iSF9xaC80qNA2V6waGtiP-8_D_vvIWL0zBCGUPqUEj57LakNprCFsbd4O5SvWVl3WItxaDleQMZRsOvpaJdh9u5AnXtlrjfUB_kdxXXc3QaA5ZTd8USePILDTcUKM3QAu6-ZEcmtBsKnHEq-NDSBDa5xV57xvDW22YDHDaMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4S8ezHQIGYAAFn3av_wv1wrdeqyW7gUH4NlAlZKRzoTobxdDdhc4bCK6UIKsUa4pvWKGxlCx5IhoOtPwhMInSYTsYXSjGVSIjt3An0XzxzQSId4oLSkC8OBOio3kV32R45qLhYQyB6nFO7xdLflJxoXYI3R5JpTGlDPaMD1CJDaRbERnhFnvwcVrtyuUF3FZ8l5Amc9DRHF3ZwSh0C76OwBKYnB3pfcmm0INrCjRS0mnA4TF5pHoAlNpVd2o5Hx2nfuZmB-WI-ygXbj9zQ8O9hRGh9BFWz6O6tmez0RJeCNHhPt_E9EbZSQunybKJIjx_lJyYS5oWLJxOgw1tRYfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ریدم حاجی اینجا رو زدن فک کنم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81786" target="_blank">📅 19:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81785">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ریدم حاجی اینجا رو زدن فک کنم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81785" target="_blank">📅 19:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81784">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تقریبا همه خبرگذاری های رسمی پالس های مثبت از مذاکرات ایران و  آمریکا میدن، فقط مونده فارس و تسنیم تکذیب کنن تا دیگه مطمئن شیم که توافق قطعی شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81784" target="_blank">📅 18:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81780">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS60xTu3YfFkYxkkwTx1Y50_uykVI5vZAsMGF7or4A4_2bW70E12_OtOfZaQRoFCaOxvSlxHmRSU39yRwBgq6MdujFhDCb8DSWxz3_L3lpOFnSLEsNeqzogn8C9kXqCJJ8jNLe6j2UgtB4lzSCiF4url05vl4dfqlnDqyoVnn2vP7PBHkDjUhq6Q98cUyCSMgczqWixs_P8PSBuLQCK6Xk4SlxSojAhvdUKfyGoWqyqPTtMKs7V8wTq2I2tNQkFZW1XNVNd75WtFN6x8Zh1sSLz__vABz_pIOJFkMIgZK22TWtYJC7g15FJkQdG-FPzFQjUZ7R-S1E-GLOzyVhfmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنون، مخصوصا اونایی که لباس اسپایدرمن میکنن تن خودشون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81780" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81779">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امروز تولد جاویدنام مسعود ذات پروره؛ اگه زنده بود امروز 40 ساله میشد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81779" target="_blank">📅 17:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81778">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKI5WnwkWuHIGjdYIjweVA4mL2Y0tG7dcU1mUm4KhZhhX-FkY9A6kYKrj6WEPCljUAWPeYJu27wCbzZkpmLiADlmF7SivRligMCdFiZSdf7RcIHQ2dAbfKstU2vHi6xva-s8RyLbdSHVrl8g3CcXFSFPyAwv2E5-VGkiBcluhQOr-Tml8mRcBoaGKCpU8MbOksNef9fyXK8IX1BgMQtlsz7ZFSO00iepMEfbGxgH3vAq2XwZdZVeAnQzfpBpVsJFMfEdHxr9YwOz9cx1ERWUhnP87XEpr26BhJHlxdZG-cT7c2vJ_3w3r2Fqc6Tib5MFlo2EGZCPNbctP-_3t-mVZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشیدنی مخصوص طرفدارای ریری که پسرن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81778" target="_blank">📅 17:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81777">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c3ab90449.mp4?token=Qs2-EU0mY3P7cUFEmDg2kj0TTifMM6Jb2g5A8WITT55898LJKqVeKriwS9QHGtt0VQO2gAnFOdpz6g5FoiliDXR9DGP2TrnuWNTg28N8OF6y_UGKqp2vgxhl98og_n3ZxU1QSDALnFm9gw5PPfETCjU-sWtRDnaU3RvpFifja_HS7XmTsrxcCBbv93KMtC4F9YbdWNais4vBkjI2rXtWaT6uUCK024qkNr99J8C-M902O1kzSKWxTsZ-5RKZ6mxQwr4l77weMuQM31v2WE9rjJyQfWll6DQfz7FTmvm4C_efcHXKG-52kWS-fZ5bXLxCFfBkGXJJZV0yFZ7IV-NELA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c3ab90449.mp4?token=Qs2-EU0mY3P7cUFEmDg2kj0TTifMM6Jb2g5A8WITT55898LJKqVeKriwS9QHGtt0VQO2gAnFOdpz6g5FoiliDXR9DGP2TrnuWNTg28N8OF6y_UGKqp2vgxhl98og_n3ZxU1QSDALnFm9gw5PPfETCjU-sWtRDnaU3RvpFifja_HS7XmTsrxcCBbv93KMtC4F9YbdWNais4vBkjI2rXtWaT6uUCK024qkNr99J8C-M902O1kzSKWxTsZ-5RKZ6mxQwr4l77weMuQM31v2WE9rjJyQfWll6DQfz7FTmvm4C_efcHXKG-52kWS-fZ5bXLxCFfBkGXJJZV0yFZ7IV-NELA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیدونم چی میگن ولی اییییییی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81777" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81774">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiQrIzGp_e8A5OjHA4xsw95-epgiMijY9pxamr2geGbYXQlG-kOigQO-3lHbOmJY8eZGo3NhVBr9DiozYO71rcoVBI5OjuvPqUF8jxPgx0Tza0r7zRFQoJWtoDduxsl6VRaI4g2DDBBvQqyCyX-nguEC9G0aYWr6SCLPC2WC8hDljZJTCjaWGzIw9mOAw9549Pci9111DNMJNA84uU4cprUHfbEHzjRYlPJLvO2mVyUf0HmAN4gvW1Rfd4ldJStlXGfdOxOi18H0EgawKkhqW1FfgVyC9swOlYxdDZFLgCEbeyafAkrCFXjtUkXURRm7x2NnPwvxkZ_RX2TSyllxNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۶  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81774" target="_blank">📅 15:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81773">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">باز تتلو از تو زندان داره ترک میده، واقعا دوست دارم ری اکشن اونایی که تو صفن تا با خانواده شون صحبت کنن رو ببینم موقع آهنگ خوندن تتلو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81773" target="_blank">📅 14:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اسلامشهر صدای انفجار
اصفهان هم چن دیقه پیش صدا انفجار اومدم یادم رفت بزارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81772" target="_blank">📅 14:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81770">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5a09YPki7HF4Rqs1KYlLQxx2QkThgAHVPlqZpNONolVvO2h2GokuHb-Zjsyn-6bN_L030PxEUVoerKByR8N-ZviYLYKI-6ZaRDR5Ae8mhWompZMXGPmF7DOj_OS3oSxdJ53bPEux3iYXykkJQWQoDcv7XmnyG-7kArPKKtSqWpKlbX5RZ_pHgRCBHz09SC5VE5VYoueOLgy3cY7KaHsUU9dx5k_Es72cOjf9eIAJeYxmzridDiT8-IJ6lpYGiXrZYhZazLKdV-jwKE9hGMrYsv9MCFNPa4hp22tShLKveQRLLkiYM_SwUyisB5-Y83NK9mRuU1zpdfs9jebtsXosw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا صبح قیامت بر ۲ مرداد لعنت!
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81770" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81769">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجار منفرد در شهرک صنعتی شمس‌آباد، جنوب تهران ماهیت انفجار تاکنون مشخص نیست و هنوز تأیید رسمی صورت نگرفته است  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81769" target="_blank">📅 13:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81768">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجار منفرد در شهرک صنعتی شمس‌آباد، جنوب تهران
ماهیت انفجار تاکنون مشخص نیست و هنوز تأیید رسمی صورت نگرفته است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81768" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKhode Khalse</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f145e00b.mp4?token=D--HIafb2YmQ4fPqJ5M6yCMwVaBvViFU2TFXBWg5cijEHcIYP0lSKhvDz6qaNOYDjiKufiG4UlDHGmoS_Wo7yyK0RkBx1vkdTLkubYW-EvJfSUG2BWU7TZPNVm3XsMSVJHzf45OCCQAQ_gTbac9ZVvysIxn_X98tdf8hJuYTwmH0CTws41-UlY9_8otpFsgJnkfhvIdUUZEEsTdHFJgvOLGxJaUMWc6NY5EgVD7d5a2564vTIiQkYnQFhbpjmhRIlarNzubjmrMtmPjejJMdZFiaVjLZGRsFOIYd_fnGx1aIIK9ESFpNnA4VoPuy7PB1U2_v90nV80d80jPwH18XNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f145e00b.mp4?token=D--HIafb2YmQ4fPqJ5M6yCMwVaBvViFU2TFXBWg5cijEHcIYP0lSKhvDz6qaNOYDjiKufiG4UlDHGmoS_Wo7yyK0RkBx1vkdTLkubYW-EvJfSUG2BWU7TZPNVm3XsMSVJHzf45OCCQAQ_gTbac9ZVvysIxn_X98tdf8hJuYTwmH0CTws41-UlY9_8otpFsgJnkfhvIdUUZEEsTdHFJgvOLGxJaUMWc6NY5EgVD7d5a2564vTIiQkYnQFhbpjmhRIlarNzubjmrMtmPjejJMdZFiaVjLZGRsFOIYd_fnGx1aIIK9ESFpNnA4VoPuy7PB1U2_v90nV80d80jPwH18XNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81767" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81766">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آدرویت داره میره سمت استعداد واقعیش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81766" target="_blank">📅 11:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81764">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ac04ad8ee.mp4?token=Iyx7lb0pUdD6eoliczhs5MYzFR2Fekl2gEUVgGEg6inkVFYInuw7m8prCYPG4Q-Tfg43vJTA2eZcl9my7oZAPJvktNX9VjKbZyyB10VNpMi1_xU5v7fRKO40R5zVUM-_8AEfeOfZWSycBc8OrosbEnLD4zogx0Nc2Jy9aUS4txau7usddXe8KNqHQi_lxj_j0af47DW9wQ52pvxnmip1_8CYmpAE6q4x7K4nvLz6vGts3B7v9L-Cwqq3q77ffGN1ORc3_d4FmZxEOIZXRDw9qP0CPVx0n_oXmZmBC8hQ_vpEHasWJK68NwoIzLUMVvU8hhtRM-nOGiH2QdRjrCSjJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ac04ad8ee.mp4?token=Iyx7lb0pUdD6eoliczhs5MYzFR2Fekl2gEUVgGEg6inkVFYInuw7m8prCYPG4Q-Tfg43vJTA2eZcl9my7oZAPJvktNX9VjKbZyyB10VNpMi1_xU5v7fRKO40R5zVUM-_8AEfeOfZWSycBc8OrosbEnLD4zogx0Nc2Jy9aUS4txau7usddXe8KNqHQi_lxj_j0af47DW9wQ52pvxnmip1_8CYmpAE6q4x7K4nvLz6vGts3B7v9L-Cwqq3q77ffGN1ORc3_d4FmZxEOIZXRDw9qP0CPVx0n_oXmZmBC8hQ_vpEHasWJK68NwoIzLUMVvU8hhtRM-nOGiH2QdRjrCSjJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران اینترنشنال: پزشکیان به احتمال خیلی زیاد می‌خواد دوباره استعفا بده و احتمال اینکه اینبار دیگهi حضرت آقاA استعفاشو قبول کنه خیلی زیاده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81764" target="_blank">📅 10:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81763">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvyHLOWjVQiWDKmkmMpQR3pHgqv7tXfxXV0_BFFzSnfhRb4zeWmDWhDiFjMttw3xdOAY2p9WO_RJr4X6BhRWC_99JizuldlPKpnk_hP-Pv7s1lXi0MyFKQVt3MtIMcr17ITLHSCH3lmpWmvtC6-5B6MRlctuAh_RBrCztVfoMRweA5kbbv9j0Lt12kCqJt158QwMqIUr-MwifKaPKGTsEGZstAxSCW9A0cROxqA-3XGeEbOPi4yldCUV6OocSLicqKih30CRzhaaoOyDacTBo-ITh95dBMghutm6jOTLEM27u2SdKAubelQbcrh0Qw4DmqGw9JVx52eJ4u2sWXETTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اصلی اسرائیل است: «ما را دیوانه کردی»
‏ترامپ: «من حمله خواهم کرد. من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81763" target="_blank">📅 10:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81762">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjb82OKO6mycStVKFgyZtbgqJPTrqcKypAtBaEKnh6FpX42Sp0BDHnWgotuBZ0u6QOJWN9c2C_-cO4DVZZbsb7URLDC_kdQXTo7hOjIRQ4FLHA9gi-WO7GSwWGLD56_av4zSJnk3iMTH4SRJPWHnD3ob8B7dk9W5-a6DHwNdDK5EP8Fnbillt7IMCasdwHrDWtX7SkDOcvFxbZVrxfur2nw5XVMwwOWHYRAGLzcx6zoc2HW5vrh72JPR4KIxmBpW22kOlRR90OfTLPZNlc0136tmPAndkjesGWZJ0GatFPofJVX9aJpeORXc1PuNuyhFMqPHss0Zcr_lGVNPPIozaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی اینجارو نگاه کن، ایران تو تاریخش هیچوقت گنگستر و مافیا نداشته که تو دومیش بشی، به خودت بیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81762" target="_blank">📅 09:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81761">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b42dc58af.mp4?token=k5pgero1SIIVsWtiZ-r_ozWEORtdp1IV_PBWFnbfHwmfvl5EkEtU6LiDUQ8X3hyqKB3hklpLSBiCxBSnN4yKtXX6wduC5ztDVH-7eZbdhPAzJZjQfgjO1Al73mD5G5dNSE7l2EyzUhl5S8wWzLTdaNBVodwCvU9-5hLa8ZFOlqFuZphvjLKqRacKRYl_4oZT4Vb80-i3WuZDzVRUQI_I5eXrHC1CIGugjXSauJhCnObiDVGNRZp4n9qtqrwG12kdBWfSqQcEpGHXVzYEU2oQNugG6OaF0WUQfciMoN_zUEb3KNyXxAvP-rD8g40U16ad7d1ELJ_Wd3WE677o-0H-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b42dc58af.mp4?token=k5pgero1SIIVsWtiZ-r_ozWEORtdp1IV_PBWFnbfHwmfvl5EkEtU6LiDUQ8X3hyqKB3hklpLSBiCxBSnN4yKtXX6wduC5ztDVH-7eZbdhPAzJZjQfgjO1Al73mD5G5dNSE7l2EyzUhl5S8wWzLTdaNBVodwCvU9-5hLa8ZFOlqFuZphvjLKqRacKRYl_4oZT4Vb80-i3WuZDzVRUQI_I5eXrHC1CIGugjXSauJhCnObiDVGNRZp4n9qtqrwG12kdBWfSqQcEpGHXVzYEU2oQNugG6OaF0WUQfciMoN_zUEb3KNyXxAvP-rD8g40U16ad7d1ELJ_Wd3WE677o-0H-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81761" target="_blank">📅 09:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81760">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایران اینترنشنال:
پزشکیان به احتمال خیلی زیاد می‌خواد دوباره استعفا بده و احتمال اینکه اینبار دیگهi حضرت آقاA استعفاشو قبول کنه خیلی زیاده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81760" target="_blank">📅 07:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81759">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستان خیلی پولداری که از سیستم‌عامل iOS استفاده می‌کنن هم مراقب باشن دستای ظریف و زیباشون اشتباهی نخوره تلگرام رو پاک کنن چون تلگرام از اپ استور حذف شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81759" target="_blank">📅 07:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81758">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان خیلی پولداری که از سیستم‌عامل iOS استفاده می‌کنن هم مراقب باشن دستای ظریف و زیباشون اشتباهی نخوره تلگرام رو پاک کنن چون تلگرام از اپ استور حذف شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81758" target="_blank">📅 05:05 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
