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
<img src="https://cdn4.telesco.pe/file/ZbDf6Po7P_q4vOrRIKPTF6b16ZCOrFpetnwrX8K5Xcqz3sjKCMfnucu9i6ccHjCdHhP9KEAlyOH29SzdSIeHiDswZ8gJvAX0ylYS4BGtalRtzZByw9o6FF22Prv6ESxEoEuj0FBnTeeAUTDl4UoUu4PVK4uq7zxaojcDIhiQFcaoWf8j6UaADy1lOgQkfGlXi9XTvbW8HBw4FA5-V4AXsVNPv_70Z4VdYEGcqCeiOV-9oLt8wU5myebUpsJb7mGsekGH94VDz6Y9BZ1YFqeK1U1bTsmlMsvl-dVqDTYec997YeBNiP6WO__4w5vlbUV22D6rUqZYPo1P_asdu3bAHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 01:12:25</div>
<hr>

<div class="tg-post" id="msg-82261">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نمیدونم براتون مهمه یا نه ولی دلو فردا ترک میده، اگه دوست خودتونم بود باز بکیرتون بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/funhiphop/82261" target="_blank">📅 00:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82260">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-qS9ubnOg_v22XVjcMYsvV08B3OIisQMEg5nw4V4JZN3ALLalb6XmPtWhfvqeaJj3uEXZikNijLG3DXNKXTNvSuvQgSt-jKDQc85z6b6oKkE60sWPmsDl-8XOF0ju7ZYeYUaYXjzbG6nvwrzK2HKeOiV1gHH4n7UgV9vg-ATzSnZvCnsEF9IWlzbXQ-9Zll4BHzHMgIPyp5tdfB3ZRwnRk-x9qN_hqKpdk1FLyiTPoyi39FgSkBISb8a0ydreI7rfmsW7G91LkPE2WydXkRq4ZOHlN4b6p2dUYjQv8YbXIVUnwmbdrNqIuqDtI9OmmUkZNlwhHDTPH60Pps9ps-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم انتخاب خیلی بدی کرده و رو چیز اشتباهی نشسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/funhiphop/82260" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82258">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JcKYxtwQ5vJQTSP7xnS4sNPahlsB77RKZOxtII35u5bkRR228PYrr8s2ZmH1n0JclsuZRrknfqo5R2ouQSl0t0rFZP4iKdfPqix8yzQbl5xh77CoBxpTz5jqZZuURm0t50kN338ZCycRfmLyJEzKxGLa3yI1oFFk-97fMIn2d_B-b7483dohjEXZTUDDbAlHsLfEw-Yju1G61v2O4C50FaR1BbpuXXOSR1U9AjEIrxp51IXyelEycyBF-yL6QIFUaa2R2gjrrfbjQeBpfXM7XWXW-Y7-fgfLhWTJtgsUbeOpctqoXjlk3nasn8MTg3bDDSyBhgM1Yl14k0YS-KiQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5huNJkb-nfflA5c3tTn97Gzgi1bvKxA-iGU57lKnmP9hmHVEbeVAa3v3Y2dvHn5PGuY5CsIwG7piXyLQz2xVoaXv8s69Gc2fjEC5qKgUuaw1H35WzWdKz0kDyShmYl-Gx1Zs2-TXI1zKkPhczr1vNJ5TYTera7Zv8JN-s-lVGLNLzn0WhdxvP4-hvzziLY8aIMaM64MbksP1Ho0am1ZWAFnyo_daUZ99jx7YxGmqEvPNPVKThmzO6ods6DHvdDHdkmHO1Xo649MGpm8WYBe0ATO7G1VMjCBGucKsCcWL2OAmmNw_spbbaMFENFuKkSgZlQ3PBMcQehZR43NHP7mAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اوبی میرفته دایرکت ملت میگفته عکس با کارت ملی بدید عضو گارد جاویدانتون کنم و اسلحه بدم بهتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/82258" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82257">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛ + حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/funhiphop/82257" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82254">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtVP-l67t-c8CzHFT5g4DvW6gQhSuuqdWr0n6TkBLbylCW3FF2vpV8jhOzA7j6Jow-UokpynIpHxGgmWhWzYnfz51Wye6BPHsGhSDxiTDZJRHwJQR-FlzTqbeMvWi6-2FNZ5Oihvy34RQ_a9m7UTQ9dABzwHx6CGnPSy133E3rMkt650uxrYccJR8N0RUg9JXzKqWX14-oNvodGnBXX0fc3jzMMlJzyTcRHnV3_TLnNNo2RSjZQ156IH1C2yPAWwE40DHSWZNMGt2ONPolETX3FuRwrGKvHW9T1j1jO7dr25LB2FPijNvL12XiobdISR_I8Kgn7WIJhW4Nw93MoOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWpN1yw-HkvsjzdSYHKtH3aB3Fm82t9s6bipqxfHKmidTSR8EwPy0cjS-GWKBVIuV8aJre9fpCTh-OwHJ84bmpf8Hzvlp0k5fIZoiylFD_n4qFnzbL0uzIs0YcuwLp6vVVJAeBCofqsFxBFqnQi3NWq8ZwwYxrjkZRL2jOzLp77YGEq_t_RhHn3nPWu70cxAsxco907CKr2tWxp7yhT1kTGDQMaFvkQxi0lrs33UINxWmCO4p5NSMafgTLqcpsTPWbp5ShbMNVAN1euhOOoj1DvoVfdDo4lNFG-KTfTWkPdGNZp8Tbanpdl9WwlibH3Tpv7tfBtIoOCwppcMIDd9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBugwyUF67uJ-kYFSj6e6vVN9JCD3O4Kd84wMLBByys1zRj4zryJupZZjoK5Z5vObtdw1Ad3DaS1Y16aly3PzPRiAAjT5slqVg3YSjliayrb6LBTuX6wBKGmWrYLblGwvhsaplDDGQjcQSmXa1f0VNywsi5KMRfSxtEine23hKDjiZnQkFqWNd28hsTEflXopzc2H2yA0Ihhyf_ejS8Rz0LhTikrurOKOeTqEm3K-S0_XIPBZPms0P68OVXKZWOnTRvyi_T31a-iSXq7Bj6DGzCnfWcU_nXszqdcmtEi0A7PbzxqJL8WHjm21NI3ZQamIiIjpGuQ-pBmmt6O4A3CsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛
+ حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها
@TopTel</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/funhiphop/82254" target="_blank">📅 23:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82253">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">روسیه بصورت فوری تا زمستان ۲۰۲۷ صادرات بنزین و دیزل خودش رو ممنوع کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82253" target="_blank">📅 23:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82252">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=mrAblCHYrp_SqWLpBDP_ja-Ktfx7Vx30FctepiU3erWsOxJRsLRa00veWTl1AEuVWWh8KJqWUeGhOBnx0gI0yBOg0uPna0xfZ13L1YSzwI659PdzOBHhxWCViY77lHaJxrkqJFxGAu5YAJ44yyUqSThpPKokFF97iL29GDu8YHnJqT0h-qB5uKugUU73aHjxlbNCH1mlHwgKyptjeHCzKzSx6ng7mRhBQa9MQj2uJPWOG3ukQiVPSr3Xp5sopOgSCfR--qet3EUFgdd12amTthfyYeDncVqEyGdcpc2_pbfcqDophdFaAReMf-dJcfibtRWeHOYrlvq_YFyHk8wR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=mrAblCHYrp_SqWLpBDP_ja-Ktfx7Vx30FctepiU3erWsOxJRsLRa00veWTl1AEuVWWh8KJqWUeGhOBnx0gI0yBOg0uPna0xfZ13L1YSzwI659PdzOBHhxWCViY77lHaJxrkqJFxGAu5YAJ44yyUqSThpPKokFF97iL29GDu8YHnJqT0h-qB5uKugUU73aHjxlbNCH1mlHwgKyptjeHCzKzSx6ng7mRhBQa9MQj2uJPWOG3ukQiVPSr3Xp5sopOgSCfR--qet3EUFgdd12amTthfyYeDncVqEyGdcpc2_pbfcqDophdFaAReMf-dJcfibtRWeHOYrlvq_YFyHk8wR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کصکش فقط یک دقیقه‌ کیر گوزیدی، چطوری تو راند اول ناک اوت شدی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82252" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82251">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">راستی این یارو امیر علی اکبری تو راند 1 ناک اوت شد اونم با ضربه جب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82251" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82250">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سلام فریب جان سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/82250" target="_blank">📅 22:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82249">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سلام فریب جان سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/82249" target="_blank">📅 22:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyyVlmJG74CKlMntWMX7ZraUR3GD6VmY5hcZh-9S7DYETEuqWQrRjpTxwAMSGomkWbHAmpklnRWrG-G4JTGlmRaF3h-xcVbVChQR-E1keC7r2FFvvzRk9CTYWLTNHel_Flek4jOCRTLWD9GjOdRTVxmyPGzO-fD3F2K3xvtXvL1jRCCpisvShwpfAWYy4sEE6n4E8pkmGF0fnAV7XSECEJczDa2CF0-iiuDP0FxTzNmcYIDZw-otsJ29RFkKOd7dLVDeCDSwgC1U2SYLR-PJPjXz4m9tWQTHzVnwPqpR0gRh-9ivt8-k3EehUbiKhO4Vl5rPtDiAS4Hrhr_LlJpWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82248" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD4-s48PNZfajDaoMQXPn4bzSGOt-7nOlg37PSG33KtczHIn6eWh-UlfH4A3G2tWWRI8iXO4rY62sd24V7wfsKVz_X3DkaPI_GvKhJf8EWeQ8c8YiWhGLB89OkdEeLgBxFW4mDCDIUVsBb_bWXTURcpqww6nPmVs5ms-DSX5_9-QmOqnF3KMSZ8CWr3dvxcPMBNlDrnteHNcGFi6QnrA3U5r87yqyX0R4N4cHa_Wm2pe1n-f5V8_JBxcidAIU1h50jHKvh9sAX9NK3KJYXOSy70AHnjiM0TTy3imhsuLwPH6FEIM9_kJsDwzp2GI6zYOPrIsxOviQp2gaM00oK_qPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل نصف حیوون آزاری های جامعه این بازیه، فک کن وقتی بچه بودی اینو بدن دستت بگن کتکش بزن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82244" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82243">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔥
دنبال یه VPN واقعی می‌گردی؟
⚡
سرعت بالا
⚡
اتصال پایدار
⚡
بدون قطعی‌های آزاردهنده
⚡
پینگ پایین برای گیم
💎
مناسب اینستاگرام، تلگرام و وب‌گردی
📩
برای دریافت کانفیگ ریپلای کن یا پیام بده: @wizard_0061
📲
همین الان عضو چنل شو: @v2ray_configw</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82243" target="_blank">📅 21:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82241">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JTlw6r67hQWRHPY4MG8vjzqx8tiQ0LSWRYtqdMOLRaMNYv28MzASXSVoNEU6kaWlnfQLPtumiA_N0SsryTvSgUKZs_ZT4b804TEOFCnkQJPhY4hgLyPuaWwZ2c_HdPb4RvaiR7ZNAU6GCw-2uX2AxK7gQYGvLvqqqPzejvLqEKAmSpZZgKHXqg4oweWGHiAdQO5xQlP5lkkXVNoltYJN-bD-0isrr5T4TGysKXXJUWmdzurLaEF3Gpyp__diqEwvM3phpZFg0F5dVUf5ik3mdN8zNfwGP7AYDQvuJvZIYejdDRfpmc0Zgkwu_ONnoxEaMhtYtCYD0zI7x6YKFQGTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دنبال یه VPN واقعی می‌گردی؟
⚡
سرعت بالا
⚡
اتصال پایدار
⚡
بدون قطعی‌های آزاردهنده
⚡
پینگ پایین برای گیم
💎
مناسب اینستاگرام، تلگرام و وب‌گردی
📩
برای دریافت کانفیگ ریپلای کن یا پیام بده:
@wizard_0061
📲
همین الان عضو چنل شو:
@v2ray_configw</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82241" target="_blank">📅 21:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82240">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یارو بهترین کص ها ایران اشاره کنه زیرشن بعد بره دایرکت یکی نود بگیره جق بزنه روش؟
میفهمی حالا سطح تفکر من و شما و دلیل اینکه میگم نادون و احمقید؟</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82240" target="_blank">📅 21:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms5hIJh5BfuEQD2ZkxkRkC3YmRXE3Zm5hMzbJkLhINdpy1ewTUtEnRtjLYvuJoV2XvBHzydHl6mF17Ps6MlnMBfeg8-yVIFBXDrnPKG1SKhDJ8MjD_VedulKLEvIxiq6Ja8j93MCvtIyTOsYk-u70MgoD2EdfLOifMgWMTSQEtOoJRXsRWYQ-BZ4zkLbz4GQULSboYa5vG90vr715k_8ILKP5V42aqgYPre5BP4OdmDrkd4IM33QDmDbtEKh7kDfe-wJDnqWvBoK2ZgCUqQh0A6zeaN86RoP-VxMWTU64R19nrP1B_-EqbtPP7tpc6zOU_IeR-8xSH6l-faxEObsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه همه‌چیز رو میگه و آبروشو میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82239" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پرسپولیس تارتار بوی سه گانه میده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82238" target="_blank">📅 19:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQ1yYP_R_OCiEDr-viUip_yaonnjQg5G3h-3dnSBV4QBp3B4VypUtiZPjYpm31TB1wrDpz7vTlQ5DKgMHhIMgA60QFeowSbFmsZVWrHnxvBZIxPMzndVdIwng9KgaaFdx_CyxAKM5q9WWPbZB5sjqZj9_0rXrco1oQvuxlQ1zUu_Uf6AtG7yGSuTPUp8ZLMCd0ObHxIXmdWa8zA9QHxKbDmzdYiZITcG4kOAzCddbOK-Q5N-_sgW1pxGSd9vI9dYnn6y3YnVM-HwYNz1jaxrGIvcbEVRR7Z40oUVZDUz_E0QhCnwN59J1JKHjvQTSZGjn6r3rxM28RRywFSQxIt1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RL0KsV2WmhfkyaWtsRyZ8F-jTV52d8HakbMmAVoFX3Gpx-AY2s47kPVnqjC2yCVLRzEKnU-phYaab-eqMvBfxKK7fY6zidXOEFSHy77WOq48EMqwy_JS_htaHQJP8vP8DAvl475qtDnpjqS74QwmyN5BwS-j-u4K_k2S0K06OCm_rVjuoWbYP_MYcGd6b3_EvVBiBKWhtA4FXdmzCrRGBW9dUfwRDVJOjpmfgScOPnryp7YVkP2XRhrDQfAQKxKA6bW5TktDztPka7PNfBlt1Ooxu30h3hvuxRnJTBNHHouhnAel-bZyxa--pvIj6OyuA6dzBZQmnkLURVCrRdMQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O30yCNCFNjSJKJtPSEvzTVNxTgoPFVeKhrULIpXUpFYxTsUlVNn-I53atTWK3T6S3gwvC3aHX_BaKDuBeVrPNeBbPEuG3hHBBYmAZ2d4frZR466MyTXce_mcEso7hselPXF4io1cYHK8SEgdecZxWVynrtFi5X4rMO7VaWvFmQ4XKs4YGPECRp1P9jvX9tG3O3CN1Xd_YqX2_0DZJIfzMNnNikltUlENpTkWxeuRJDRFi9Vo5aDyaTOtiiFqDcqn2KlR5FcWP8AvGol_zVLxK_xTNqQs9-YH3uTs2AnYBRWK8uewIYA29ICAJ9SPwUh6zCcdLlrIa_9C7r_ZyhO5kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افغانستان
🤝
فلسطین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82235" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbLGWRlbx33hWduWa3AVZcMFO5XtyuXoYMx_0p8K3FHYysJI5_Pzy1ZYbAEPjXrEcHFJaMVZ6e8YE51MCNuG2jDSxQCVr0hAtrEzOWviElC68hjA-XdyUVLGP26dH0gq6x2NvUYZX0M8VFdTr50otsuxHFJNnVj0YNVfhNPk2HdGquKism8PMPYDvuLeDwn5v0J1FxlRudO3RbgmXrP3JTaI-BrGoVC8wsFuokDiDjm1MoB6dD9q29rBksaOqi0sNrBZXjMyQLRkgHqdwUhlS38ePNPHkni9ZzU79phwFtX0_KG49psEWuLUkIQRqqNvXjjmkSAg3rppRT5KlcmbVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه محمود خستمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82234" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=ixYHTc7XimXwAzxjf5J5_A29Ef8b3MoMq3EI6QTbRsZ_coUQJ7Zhkf1xmjfwJkmdw1emcDyyZgL9Jc3QywTchqpQ_d6WTfou_Bl_z323h6m5QHdIKyTjMwl09vl5b28nAj9jorr18aQ4sZ0WCQ9mCPRss60hT6owkPHJzZ0VjrP6Jo65mgmuTCjVONFEvQibRlkZlly-cbMofTfeFDgXfMWFKI2zf_OzM5neOusJCG4aAgI5X-kpoXZiTdeAKgmxs0j6IBtxkNkaGfiYsdCS6nUkdG4Ya1041uJF6OXul9cBMseHDuIPEsn_Xd-Kfn3W4_2fBT3-DdZlx-lzZGPBvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=ixYHTc7XimXwAzxjf5J5_A29Ef8b3MoMq3EI6QTbRsZ_coUQJ7Zhkf1xmjfwJkmdw1emcDyyZgL9Jc3QywTchqpQ_d6WTfou_Bl_z323h6m5QHdIKyTjMwl09vl5b28nAj9jorr18aQ4sZ0WCQ9mCPRss60hT6owkPHJzZ0VjrP6Jo65mgmuTCjVONFEvQibRlkZlly-cbMofTfeFDgXfMWFKI2zf_OzM5neOusJCG4aAgI5X-kpoXZiTdeAKgmxs0j6IBtxkNkaGfiYsdCS6nUkdG4Ya1041uJF6OXul9cBMseHDuIPEsn_Xd-Kfn3W4_2fBT3-DdZlx-lzZGPBvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم دیشب یکی از هوادارای استقلال داشت مصاحبه می‌کرد که یهو رفیقش جلو دوربین انگشتش کرد
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82233" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82232">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UadAzCBeGkfcIZJUAHy9VR_Rlc60w1wBzFdh4iMS7CyemJdhQRZYNvfEJ_ZoiSvLk0wsoLMIss2sFTYLlTH2VW_5JlGPzIWtl8pGPxbsAnmfX0waRH1fGPi2YQEE5fXmSN1OoePdzJC8oQ72UO8syVNNosRDQTUXtgHRYWzWCoGR9Z7L5em5VtLE1efkY5LWmkKqubeXtef980z0coLJflBaZ-w0NG631LqNuJi3pzV5BVVz3hqeyVtU1h7g2wia0_JVfYKGUkb4g-kgol1gccmjCaLbGHU70egqqYBknYY_OXC0n7-QDivSC4mDAuxII48nDSXW4SIalHGE96du0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
نشویل - اینتر میامی
🏆
لیگ ام‌ال‌اس ایالات متحده آمریکا
🇺🇸
🕔
بامداد یکشنبه ساعت ۰۴:۰۰
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📝
حقایق مسابقه:
‌
1️⃣
اینتر میامی در ۷ بازی اخیر خود در لیگ شکست نخورده است.
2️⃣
اینتر میامی در ۱۴ بازی اخیر خود در لیگ حدأقل ۱ گل زده است.
3️⃣
نشویل ۴ بازی اخیر خانگی خود در لیگ را برده است.
4️⃣
نشویل در ۱۰ بازی اخیر خانگی خود در لیگ شکست نخورده است.
5️⃣
اینتر میامی ۶ بازی اخیر خارج از خانه خود در لیگ را برده است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82232" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb0YNSt47KvBh2c4LHwjO1xxyM6YfYw1AzTA8N_szDRjBSh6UScCFqC9jfKua9SQivF0q2Mh4RkLHAv3zJrrbzgNzOCm6t5NiwSxW3ltMEo14CNDMMRjVHIhd5Jcw8vhTmJrzCNUPTh69Hf4fRWHctDfSn1F4jKU-KqsLNCDk6KwXfwM8TJobzF01UeN1GwNtRfJLF7UAhvHNna2ucQZZXG11kz5HRPCQ1rUQrh4iW4DJiaJRkeq9Cshun79ZJi48g9NtkdDyZcIRLk5y0I5i4rMTMNBZlW5DfsIFWaJeL-p78wAsKYj_MlElW9EoUytIhcETC-ZvO95KRI-dJ8QAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده بعدی توپ طلا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82231" target="_blank">📅 16:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حال ندارم عکسای خیانت بیگ شگی رو بزارم برید چنلای دیگه ببینید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82230" target="_blank">📅 15:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تیجی چرا آلبومشو نمیده، گایید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82229" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82228">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82228" target="_blank">📅 12:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82227">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=G5GBgwextO1uKyFoIfnZPjMGuXby1FJHDsOkj36g3qCWUZ5b-NrcyI9QeB0rW3CHEYs9OX7miYhC7FXpq0I55vV1h9IqlaKfNpcC-grz2phZ2kStHkorHohgNQso0iSrq0ss6NUeh-T0KmjNIvW-pJgJ-ZpJSSEiWmmh5LiQOsrhgCCwXzua33diunVgK-rbj2m_SOINYx6FznUPRK09gIZL1KeyY5ScOOGLFxF2BwGCD9r2TMAKHtQhw6jard_epSAZhWnwoKbUEK5fk-f_qkuJup4JWRLdZXwtwRHRoiUvViFUoZEANSiEslBMfJ5CcDzFhsaMTvS_YJMhlMRhAg0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=G5GBgwextO1uKyFoIfnZPjMGuXby1FJHDsOkj36g3qCWUZ5b-NrcyI9QeB0rW3CHEYs9OX7miYhC7FXpq0I55vV1h9IqlaKfNpcC-grz2phZ2kStHkorHohgNQso0iSrq0ss6NUeh-T0KmjNIvW-pJgJ-ZpJSSEiWmmh5LiQOsrhgCCwXzua33diunVgK-rbj2m_SOINYx6FznUPRK09gIZL1KeyY5ScOOGLFxF2BwGCD9r2TMAKHtQhw6jard_epSAZhWnwoKbUEK5fk-f_qkuJup4JWRLdZXwtwRHRoiUvViFUoZEANSiEslBMfJ5CcDzFhsaMTvS_YJMhlMRhAg0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴
: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82227" target="_blank">📅 12:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82226">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=QU8qPhdLw-5gqg-7DkUOc7y-uPGMeXJJBdLnwzM2BFbdX28y1aqPm_rbwJSyPo_h7CJq-rrK6ZmCV0-si33FfwSjQEjHL_d4STskKbeaVPCOJijhdn4oE5WkkRY3Znj3LpVaHPKoAJguIOLq9T1jsCQZpe-aE5rhTCl9PhJEbBxDM3H5lK8vg3l_cKSo1tTSknzJsnhV7oV8K5sFzAa0BcMCQD2aSdaEt_VYq1RcbGbtVy5z_lnHJCnqYPv35_prCXUQa_sIDBztUOtnO8k3Q1UKjjDNd-9MBbm6aA8LF8AT6DpLG8BzYRR2nMuv0rHOt81zAxOCUo1b6_kmPFNsTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=QU8qPhdLw-5gqg-7DkUOc7y-uPGMeXJJBdLnwzM2BFbdX28y1aqPm_rbwJSyPo_h7CJq-rrK6ZmCV0-si33FfwSjQEjHL_d4STskKbeaVPCOJijhdn4oE5WkkRY3Znj3LpVaHPKoAJguIOLq9T1jsCQZpe-aE5rhTCl9PhJEbBxDM3H5lK8vg3l_cKSo1tTSknzJsnhV7oV8K5sFzAa0BcMCQD2aSdaEt_VYq1RcbGbtVy5z_lnHJCnqYPv35_prCXUQa_sIDBztUOtnO8k3Q1UKjjDNd-9MBbm6aA8LF8AT6DpLG8BzYRR2nMuv0rHOt81zAxOCUo1b6_kmPFNsTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مامان ددان تو اینستا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82226" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82225">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خلسه میگه دیس خشی آمادس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82225" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82223">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=c0weBtP-aEVHsOK73HObaoT0BA3Mx6Pe3XdqMXY6V2d2g3TKSxoXcw-6oCQ0mTLtogqtL4V7kp7QVhQxBitOkWLkLe_S3uZL_UQrbxlDE2kYONDPtOYQMh4IsjSIh-EjijIupcjtnYigTNKBGW5Hi5kwvUI_QksXGuRGtsOZSomOzJkdzAv-Rn8QtH5g1YKTTOqIzIdgLnpZtEWxs_mv_4ob76pSUvSFIrtMHxwua08V1ufX3QiWCvXqnjAWgFjaMYn8RVOHatqo-YS7eWx3_UVwV4ci8z-4KWIulZqjypyJpI4w7L0WsJTRHw2UFgSxJ6m3VL7SPt4KRrDdBagjSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=c0weBtP-aEVHsOK73HObaoT0BA3Mx6Pe3XdqMXY6V2d2g3TKSxoXcw-6oCQ0mTLtogqtL4V7kp7QVhQxBitOkWLkLe_S3uZL_UQrbxlDE2kYONDPtOYQMh4IsjSIh-EjijIupcjtnYigTNKBGW5Hi5kwvUI_QksXGuRGtsOZSomOzJkdzAv-Rn8QtH5g1YKTTOqIzIdgLnpZtEWxs_mv_4ob76pSUvSFIrtMHxwua08V1ufX3QiWCvXqnjAWgFjaMYn8RVOHatqo-YS7eWx3_UVwV4ci8z-4KWIulZqjypyJpI4w7L0WsJTRHw2UFgSxJ6m3VL7SPt4KRrDdBagjSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فیلم Avengers: DoomsDay منتشر شد
۴ ماه مونده تا انتشار خود فیلم، این یعنی تعویق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82223" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82222">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-9EWCSyykywg3pSs8q0H8q-ffERskTaIZw6tdTiEHx7OhcT2q7hPLzaZab3gaCet7J-8T-UgrAJ8HkLARgWtai0is-2LBjfR_t8pB33XiIt1rDc3VvdGmJWg0HAEwF8oFvwfeFwEaaWqaYNejzXPrYoeIgEmjdTDOeJX9fIUKFCBa6j4-V53KKYxdJ6Q_wxUNqcSL0KUGVvWby8huBO7EvKdJ6gyZyrLEXZ8LTwSel8WndhHCm0FYEu3DIGb-mdPps5fuwgyyYXIZhvYVsPIWR9NfjWquS47KRoUu3mtekXazXtIxYvvGaOvQHKHbpojNPhSztEHUrkGIZP6pF4Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری شیپ استیلر و کوروشو کجای دلم بزارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82222" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82221">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuhqH011PJVDeetbPGZFGzTb4ZNDgydtVF0P6vA_QIkadgfh2KB08JFjnqCicCIqG_Qpl0eR7NshC50ZWspXoD1nCBdVuT_kSuScfDSAWg8nyN5j4vKEj8DBYkwGWqIKg0U05YkXyTYu6AAT71UhJEU6ruaJg52EOIkaBtgQh8YkqrlrF0hxRg3vA6NStTF5NwLuj4hrnoKviwpeOAixxktkiW2456s0IsD00b-HrtLcT72PaG9V5B-QwxPnXnpD3J2HjeNb-xTNUXhaFS788Y2AqhubMXFg2r-ONrZzu616Ye1vIurqXpTt1Pba4BLHR5_sv2tx2k-gGGq5MSyfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
نشویل - اینتر میامی
🏆
لیگ ام‌ال‌اس ایالات متحده آمریکا
🇺🇸
🕔
بامداد یکشنبه ساعت ۰۴:۰۰
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📝
حقایق مسابقه:
‌
1️⃣
اینتر میامی در ۷ بازی اخیر خود در لیگ شکست نخورده است.
2️⃣
اینتر میامی در ۱۴ بازی اخیر خود در لیگ حدأقل ۱ گل زده است.
3️⃣
نشویل ۴ بازی اخیر خانگی خود در لیگ را برده است.
4️⃣
نشویل در ۱۰ بازی اخیر خانگی خود در لیگ شکست نخورده است.
5️⃣
اینتر میامی ۶ بازی اخیر خارج از خانه خود در لیگ را برده است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82221" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82220">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">من بعد اینکه فهمیدم منو لک لکا نیاوردن:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82220" target="_blank">📅 03:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82218">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMmWtuun0SoZXYCmXstMsltBodhWjznqpa4KPv8uLcH-41_uGZ_QAM3KRMTpuirBtObAXqEtFxV65po07rZN9V_1QxOOhxH7CagqTU65F_Gji3-P3PlzDaxwByztNOrsfk6Y3c29YSxPkQ2HRt2al5OujxZ3Syaw8kvXGB8l9N4QQUtYnF5Rt5z2n5CehVtCY1dVCyal5_y0th9rvvkRDIq04o-3ubZTyjUHpEHJ97WVMF2UwGqYtou93SK8ST2fSxQ4oGbxcr0tWjqucriYmYp2huBn99lLrDr5zrAmFohJpKQL-npYevd8l7vAsHtJR99m5xdnKwXK13hsD_x7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etzHVXCoIcFj2ipBSL6r-AXicXrGpBZJlLZjdRhB9k1tLpmTOBHtjkoMldGksJSv5JWWjboc-pxKn7md8EA-YjCLcYVxO-3GjjzrSJBzZ2g_UdrNepVLvfrB7viuw0ZeFQ6p9xsRQdLpKEI570vt6vdTAH9km3od3pzFZP2YIj2gMtzB41bbxKfPOvMzBOX597sLWdIC4JeNkzDOMioqPzAE_ZItblxw0kvEy1dUFtfjLEJtvp9elRV3dfjXN2e33nEMn92dvA7Cusk7WqpHcLqiZpvzLZbM_C7fYRifGfZhyY7IkHT-y3nyeQee0tpYTYRnM04En0-fXYvhdfsV9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخه کی ظهر مست میکنه پوتک جان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82218" target="_blank">📅 03:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82217">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEclWlKC4QlO9C_TPF0hKCGwtQwtMCrG87USiskgTva1bM0F1YU58kkeH80y05vu632R2JTBoghdvjEO4rUTWONp8oYPLmyaml5fMibQtoizDADFCfBNO64fHPQWeBdtLlT4DEODF-WREv-gxW5lhgsaRGoYMXNrL6UURjCJSlNJvi2eSBK1GVdJ2TpChycnsw_7WOOGeP7HPdad7lwlF9KMxYF23_EbUf7SExJDWWNUB2X1vcFHO72fGWpoNCOql7UTR-Gj8Nj7UnbYdhrVu4MV6Wx6F4jNbLE52oZCZu6XmsgjwU_kwuYRjqiqv6eWTnm1y8QSYGQ4Ylc8BWLc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته بود: بچها زن نگیرید، خوراکیاتونو میخورن استیکر گول زننده هم میفرستن هیچی نمیتونید بهشون بگید.
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82217" target="_blank">📅 02:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ: تنگه هرمز تو کون ملانیا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82216" target="_blank">📅 01:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82215">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFrguqjDYBzcOcH5lFLutFC3p_zYnNfVtUaI5WpV5rdzCRY7jbIhNKNXUfl_297zVQEoNc0EMSFVGgMWUSO5veMnLv3q-qYE8EK2kU7_DxvxLb_KQ-5myET6vSb3QWmYrZ1WB_q6qr72INRuN3PfUZkYzR5ytzl7LPf3V2P8a1W4RcjO88p0rNlY95aKNy80lop8ABxGNR-eIoGR24e25YpD8H3aMgP_9TD1YKofzPs2QsNzN6TydewWeCNxjZbEwglY92g4LjMxka6wzLo8WTcpXSu4icnU8nztFwYoaEht-WZH4sQT_qwcbH43SgD_gP_2SK95K3VJnoGjuuf4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا همینقدر موجودات ساده ای ان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82215" target="_blank">📅 00:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82214">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پاریس یدونه مهاجم از دست داد سه تا گرفت، بارسا دوتا از دست داده یدونه هم نگرفته
رئال یدونه وینگرو ۱۴۰ میل خرید پاریس ۳ تارو انقد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82214" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82213">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLwEQRVpGakLpUy1NN9Iecb4KzosYb85P7Pjg-cHItytzAi7DqAXbF-86NPDFfX57GEbmbHS9D_J4nl9xdJEGsEdGSRX5hxsRjFIjZb8lupCU4JUdEdUAjfIByybtRj5pXnNN4kVvHJhj3iYvpzdZHdD7nNn7SECXiCUCaRCbOLufJ1IaC7v-aImB9d5DaVKCytfRnKgMUwaNaAI55VnUI3v1WhICoNh37oDY63t6f_tJSerdoaNdebAB2Hgsl55MJKvp9VXrpdxSrCsltowtwGfQAdQPbyUGEme-H0u5e2smzN1hinP2jDnjIvVgLXfvA-vzwJaTie0k_VhjbeLYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش و جیدال تو یه حرکت انتحاری مادر ددان رو هدف قرار دادن و دارن یه نسخه دیگه از همکاری هاشون با ددان منتشر میکنن و نسخه اصلی رو از پلتفرما میکشن پایین که کردیتش به اونا نرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82213" target="_blank">📅 23:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82211" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrGpxfvOJgRtCwlyIB3kf00u2LIlXYen9uY3wGVL51f5N4YLZeh08fyRDSRb8ZH6PvZck7T7PXI8_2hxhrZFRyOEHXN13HBFSeS5m9OuX_nbC6u7gercHQHkTUpRJBn3qo130p0WiywsLzDgS2uBqVjdUxL5FPFasqhcpGcU1FKUO3ooAH74jpnrKHhS3ve_LmmycOGXgsFoXrMBS24IN9gwXuqSk0TbCEG75cSaVkcAO2dAOcSetAuykMMpDKgGFn-EYdOubQ0-mXb1wBaD7uLIAGTamLencmzbEqntGcbGt7XIbrFf4lzCSv0Yu3O4UnpArOwMF6XvasQk4fQedQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو تروقران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82210" target="_blank">📅 23:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=L1p_Kmyk1PuiIQRaOVUJHlbGYSeUN94AtmUeGQp49SIPWIOmL9Zhy5tPBVohDZI9T_lX6qcjO_3iCPNR2qK4N7EJa10nPGZb5MYVLDIZCAgunW6LJponPgXb14vJNVAz_EVXkdayeTGRlWEot_VMPIAnFNhk_mxVSz6OeUVyhxvgcPIe7IQGZC1Ri7MZUyuSqjYk07DoWzysO2Wor8kbrtLUc_PWOpAGiQw6NsffW6jGWSJODp_SpXQG8Jxu57ae-9jhsQaK3vyJu6-ufc0VtxkovN0ZUrWRxKC-rRoHymFDp_YdSdVI2N8CNI82VSWinAypzEQ9af5qCSh3rgdVgDb4nRxTc6038EoOTUlT5RIcQUf259dF1GH-EakTJq56a8TRQk8HnQo_SKJsOJUhAGcE0aF_iBi1qujqVJ9PVfm2JRzoAmykhsDL10HZ0SFTLyZ7GLEEQMpeVVqWNiQCEf1p-f9SVwbaCfDsmEcBmrpw8b9ay9SYF6HKXddbSAGsURBcDAn0OpjGzhmmYDt-fikiU3XU7TKVrDYl_4kIZxHkZKnpABE_7nrk5OvbTt4mHqBTzv5Q0SEUXFPRfzKkXkTsaamns_bBq5nJZqDHAcCK9kirts58E-hgScdD4qffmVYOp7m7TjGKI64ZOnsuDC7HVDyMrE1VsOhr-SMBpOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=L1p_Kmyk1PuiIQRaOVUJHlbGYSeUN94AtmUeGQp49SIPWIOmL9Zhy5tPBVohDZI9T_lX6qcjO_3iCPNR2qK4N7EJa10nPGZb5MYVLDIZCAgunW6LJponPgXb14vJNVAz_EVXkdayeTGRlWEot_VMPIAnFNhk_mxVSz6OeUVyhxvgcPIe7IQGZC1Ri7MZUyuSqjYk07DoWzysO2Wor8kbrtLUc_PWOpAGiQw6NsffW6jGWSJODp_SpXQG8Jxu57ae-9jhsQaK3vyJu6-ufc0VtxkovN0ZUrWRxKC-rRoHymFDp_YdSdVI2N8CNI82VSWinAypzEQ9af5qCSh3rgdVgDb4nRxTc6038EoOTUlT5RIcQUf259dF1GH-EakTJq56a8TRQk8HnQo_SKJsOJUhAGcE0aF_iBi1qujqVJ9PVfm2JRzoAmykhsDL10HZ0SFTLyZ7GLEEQMpeVVqWNiQCEf1p-f9SVwbaCfDsmEcBmrpw8b9ay9SYF6HKXddbSAGsURBcDAn0OpjGzhmmYDt-fikiU3XU7TKVrDYl_4kIZxHkZKnpABE_7nrk5OvbTt4mHqBTzv5Q0SEUXFPRfzKkXkTsaamns_bBq5nJZqDHAcCK9kirts58E-hgScdD4qffmVYOp7m7TjGKI64ZOnsuDC7HVDyMrE1VsOhr-SMBpOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فصل دوم سریال Mobland که ۲۷ شهریور منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82209" target="_blank">📅 22:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82208">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_K8asz2uXHxYUNHQp-HsnYjXodkpP42Hs_TibLZQQiIewFOdrPuwEyqxaB2ck3t3rZL_X-zWIDBPgb60fTPDyoTAk4jE8keiVNdFhDZDXSXk2e-VZ8K5FyPfIlOtLVqfH9TIKxOa__K-HGeKH3-pZa6Be_qGdB21amrSt_3ob6g1GZY2CseBhoo9pTxIlFAgULp6LyZd-qm_ZXsnozGz0SNjl-vzcewGkfFc3RfeuQQfHnaSLPivHqVIjstIbmkhrg-z9c5c9yNxDpvrnv5b2p7I9sMm7YBhMgzfUdTc-rUNcWONFdwxO6D-Z0pG1WC3GEtu85gDY1gvcNIlgCH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم نفت رها شده در اطراف هنگام و قشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82208" target="_blank">📅 22:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مایکل اولیسه :
با تشکر از رئالِ مادرید، فصل آینده اگه مقابل این تیم گلزنی کنم به احترامِ حضوری که در فتوشاپ‌های این باشگاه داشتم خوشحالی نمیکنم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82207" target="_blank">📅 21:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82206" target="_blank">📅 21:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKEAg3pZjXxn3v5M4Ck7YZDJhXy92vTJfFy9tYKh9Srerp69A_TWklYCvyFtTe1tWqAAm6csmq7L1e6IwtKiHPun7Rr2ZJ5ZgVdCp10tEVyrjibL_M40PSpQ2obJai2GafPGJ-UhhK3oJBGALtIxyWT_ExntrHZwzAOv8X9_Q6mBKC5lHvvIOV_zmtDgi7UONPiGmpgxMskh6FY85yh4QoZ4vnnekmHF35wthEq0HjvdLvCzP4B0EMqpXO_t0JaRNR-7xDg_SvzbiwJe0oRo0-IhHt5jEGxXd2nVMQEYzryKKP2XH4HH7zGkPLsfMvgYiTZgYQAh908izMt8M0QfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82205" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj1I-dojd74vLI0-ZveOfSp_3S6K0EV-DZvW-HWs9kMcQBNLW10v5PGeeErZXcvHfycLGPhwd6tp2HUxzpY56dx1M2y85kizL90yfbCbZKGaGLyuYpAH7tU9nRKeCOcf0PLeaiXJaVyJPMED3fnYcfXw66oKrFLDzVNRsAlQftGCDKYDzfwcw7xK0mDjWMWmTEAHfIerlw9e5uHWO19RuBeuKisXV1fWfQuGTRXBly-i77qbcOgAsZJaPiyg8QWjz5e82CIq2Oif1SiRZNVCdj4KlZvqKVy9QRPfqKXHCRaLrORLDZ2zTcd3FDAo7YNiInkl6U7nT2acN2osyW3hvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از نسخه افغانی دیجیکالا به نام افغان بازار رونمایی شد :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82204" target="_blank">📅 20:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmCBvsXOGLNAQQz8ab0HN1zEsKDQpH4-4tZECzptxf6BLYAkJi5E9il4yrjfMaZHe4cQiR8nLUFs3MpUJYD5_e30Ty6v3FBM7bZB-OdT3rveHdgpnm4SnovPkyHz3gZE5UfDe3pUqI1sEZFain3nfOGvuaViqXvTx-rRl6SJ3ZIZsAvRjEEl_Nppp9N7jHG73OvaMndG9VqNS8cOuvBXK6HTEOIJuWhx4TGlqHikJpINzOvTm9HofyoS6QH0fiPc9hJ1S40QCi9DewhP1_CqCfw8UeMMW0WKGB6u5XjP-G2Xocpb7Bo9m-2uoGIihroMUVvM5QCTNauxJ06e2OVstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسمتی از وضعیت جامعه از زبان پرستار بیمارستان :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82203" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82202">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMiRk4zqajUwVpr35fRkypnuxrH2insJUPWUyfOk2toICUGBMOAPFQYl6M1S40ACJ-ukMXlZx9NP_NIEbXERINxFk_l_YAkbZ-0VCDsybIZEVgBMv_DSo1VESR4riXIJy0Mv84GFX33jQkUTQ2ytGDzSOBjpoyZWgkd9A8AqD_RGFzPrpktly_OVJcRSULNUzrmeHY-z7tatkDrRDmhCj-mW2hN89mYA-RQ6DEX4oKnVKxRAlTKIE16M1Bx2ESgMzVtO2dO-tjkOcQ-QjcyHUAsZxT7VbzNZVHUqAi9fJFmuWzAnnFshg05I7fp0Y7ubzCxp2e6aXpNPjwvRKQbziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال  پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌ فوروارد با توجه به مبلغ پیش‌بینی، در هر روز از رقابت‌های لیگ، تا ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
21
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82202" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82201">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ بزن که باز این لیگ کیری ایران شروع شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82201" target="_blank">📅 20:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82198">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atIjfNK8JdQbmYBdU84FNTLotCXuv5nBA9cGep-JicvSmHY9lOlzByNKjceycoILMRqYI_VVM38YywRIfTFM19ossZS8ktaQznQTLspHIxZFZK2MxjBDskyOJv6KBqSWUrVakD1Sl0XlZkZuMYuPikysq_73TQyZTuHMZ8lhubVkbE-o5tYshvjUlcick8GhG35evp5rgM49Ir9fX2tRXcNrs6k_MonpFkqq3_j-nWoKtJ77atLZk2_fOcWyyHM5-cCPVEEBpRNT_uKE6-OoJeHOO468J6W72y64N9_3MawO7_vHUbGH1SEuCqIuXuDSBRgrBFbUfircZxVdFPAlWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82198" target="_blank">📅 19:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82197">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Nr2JC_ejLyrtuvkqBGoZ-8ug10HjLiiqF0MyIgKW7SgNVJN4sdpuaF3pXkWNvcbneXfEXSuSYbJBY2EoDMwGf8wURgCr-wKq-P0c3SAAgflmq66edOlQHS1cE9voZJnwjmy2nUp8SrHlQYZMPxDxeiLUkbQuBGsH4M5JDTvuiogVW4NjRy0wiXHxV7bHTiFR2aDVWn25H-KaBaWDRasZWwzFS6qgA6VZX_0kGeMDCa5NxF0qZhMfvBEyYQK7-Fxl6kOBsBiEL69JtvP1-3dkZd7Djyk3iPSI96ePzzO0sA4NPnexyH84tHDPpUw3XIq7rekR7QHX7dJ-anxubjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه قهرمان‌ها شنل نمی‌پوشن
بانی بلو گفته موقع ضبط فیلم سوپرش با 1000 تا مرد تو کمتر از 24 ساعت، وقتی یکی از اون مردها شلوارشو میکشه پایین، بقیه شروع میکنن به مسخره کردن سایز کیرش و بهش میگن دول موشی ولی ایشون که تحمل همچین محیط کاری سمی و تمسخرآمیزی رو نداشته فورا دستور میده تا اونایی که مسخره میکردن رو از اتاق بیرون کنن و بعد به اون مرده دلداری میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82197" target="_blank">📅 17:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82196">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCJzAO6C-ZBCJrSMYb1lMw4H_bsJ4PjqUn-ZIipHI7Zu7956SVJVa829ToM4QyfDZwX0LRZTScyyHV1nTqXYT7Ffr5Zhk16mdc_2lKozFYc8Lrq97212YNJnm5fbWx1GpC0G6kDGTvI20Ub_tmMmuX6t68hc5UhJUTfW_-p2B09gmAk3m0OorJnKIEls2CaIIVdvYSXPCKclcIya2Ir7OmnQq1NMlgq57e2Kw7xitbiVHN6CAy1UJZuDgcrUwlL0T7y2U5f70iIYRA7xgPYh5fBUlTTNZPKfVlaBFAct8IQFmJjgJoFzB2QPuutE6VzKDMtZXI_fM9Vf-0HcnRdr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اکوادور ۵۴۰ کیلو کوکائین کشف و ضبط کرده که تصویر هالند روشون چاپ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82196" target="_blank">📅 16:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82195">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=tzbEUXwVIk8e0b_5uCyMfJGSaP5QmPN8SmX7reLYbbPS3u8ocFq5DkdueQ49uM3wmO-Z1Np9yElcvIqnOA1hjSN0h33OdouWibzCdSKH_6-E5LNMYuyaOKtC8871EHv_wXr-siAbG1NqdDJlymvhdTHxukfSooLoRZiw3uVLvOCUtAQINacE7EQS7fPY0Dp289jKDDci0GKs4ZaGbrsmgS_Jx_3BqREAvlu5LNdThUq5Qi37CER2Q_3CJxpOc8P9_N1PIv_TMuU0Xd6d76JpdLsG5HQa90zcfv5_pgBSgPe7cFxYD4lAGz1A_jWq1CtA6fQzhFUtECkjmNcnUBjdxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=tzbEUXwVIk8e0b_5uCyMfJGSaP5QmPN8SmX7reLYbbPS3u8ocFq5DkdueQ49uM3wmO-Z1Np9yElcvIqnOA1hjSN0h33OdouWibzCdSKH_6-E5LNMYuyaOKtC8871EHv_wXr-siAbG1NqdDJlymvhdTHxukfSooLoRZiw3uVLvOCUtAQINacE7EQS7fPY0Dp289jKDDci0GKs4ZaGbrsmgS_Jx_3BqREAvlu5LNdThUq5Qi37CER2Q_3CJxpOc8P9_N1PIv_TMuU0Xd6d76JpdLsG5HQa90zcfv5_pgBSgPe7cFxYD4lAGz1A_jWq1CtA6fQzhFUtECkjmNcnUBjdxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدایا ببین من نمیخوام برم جهنم، ولی یارو اینجوری پوستر درست کرده حق ندارم بخندم؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82195" target="_blank">📅 15:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82194">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بنزین آزاد قراره ۱۰هزارتومن بشه، فدایی حرومزاده رو دیس کنید همش تقصیر اونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82194" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82193">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5R-0_fF6j8qPPUqWb7QKt-gMKwBOy2SEzJmww0SGXmiNVONunimvM2Jvgbrz4vHbwvWyN-FOYOABCWoKbuv67sm6AOLPcPeYbCm0MYtd0LD0VDw4J4KdnGHGbAcd2plZMkVuPWlU7WRl_aAoQTVLXTzKdE9J9KfrbCIe4TFMyIYUsLSadjWwyN_dsrhGvxvyVeObKg8w5w_r6WSmhjFV3-ekE_VbPwUeYiYBuX3cRTyRiGfiuajKDf3I_99VKS_o4HgrAv-2BcIg2V3nQrVXa4U9d2if1vB7yC4edKrNee9plp1JaZR5UAVZ8ckdGeHd9JHq3W2DOZelilqFYHj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیش سال از این شاهکار گذشت و اما بارسای قدرتمند اون دوران با حضور مسی که نذاشت بایرن گل نهم رو بزنه
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82193" target="_blank">📅 14:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تو اگه منو میخواستی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82192" target="_blank">📅 14:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">7Khat – Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82191" target="_blank">📅 13:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
  <div class="tg-doc-extra">7Khat</div>
</div>
<a href="https://t.me/funhiphop/82190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بخدا خود هیچکس یادش نبود همچین ترکی داره، بعد ممد ازش سمپل کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82190" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82189" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6qhnp_6Qqa3C4ks0tvmTE6rqokaJ9oYGPHet_qWMRMzBTfXg1Dqe3_bigFEZ8_C0QCVuRuYtSc1ABL_tfcts4_v5qZsQG_wmK2rCklgp9yovCif8enWri6mnBU0ja2rm69yWO-IxB23SxKynDMNQNdPdyMRUCATcBzaK_RUYNWsH_cqp6m4VctQ4gcAvMff89QmmhNVy2l44TbvD7HzAm1DwCd9z5DpsMfJ-skWeeLJxWAXohn-ZhL5GZh09wr5Cf6y0xcrJGP1QyyWgaaAkz326X-p4KRmR9zMy5hbVbwn-4iGWxL9ZzXXK041_EMU6WZ7uLvRXerpdsfv0tCxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82188" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJFSpuw3DrYJkrybMFOFjiRRZYKCcE-QAIfu7KPY5teZgWjgK3VYAPlyArRqS2KNE4N9leadCfzz3wcTblEEKCaDo-VcY7dmDha49URW40z_SC07kc0Lg6_tCXVo-x7XuJLah5lFH-87UsauI83s2vYluk9t0vYZJ9FF8dJ3eDIsYFSKOdIyAg-keMysKMwA_yRnQsAeP2B8WbSwToxSgQ9ru8adqjb3ilay1rChh6s367y5XzBtE-UwCg2nTGDDCkdZbbKB_oNeMYR63NmUb3zFHy6AwkiQMclc_xx_FbAzRHGxVBwiklEvayz1lLxdFzXN69PYxRsPMeuABeY4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد روبیو و ونس  ترامپ مسائل ایران رو سپرده به این یارو که در عین حال گی هم هست و شوهر داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82187" target="_blank">📅 11:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Oiby7X1Ahx5zUu7qFQybqtAIHRR12Ev4VxocOhIu7BGasP8RBa3aAVebydGwN_pcVliFEyzcROOkZc1Isnk4WIkjj3124pPr50cdoHRD-NwynPLQQH_uQ93sGGrBcBUpG5S7tuSniZgxnuXbzta9XIjuilxoHt67v0HSEubhGswZBvGXdUaaabG_CKETPl5WafJj_g3Evr4gO_50J3F8avBHeBAdM3FrPO0X7qkPm5QuFKwkv01cA9INhsyzbm6ucO8bGb5ZenlI1MHrZWcUk34_ARydhhPjgpjCkvMznzaGXH8s3My4-itDvK7uA12-zqvWGL-mFUUD33czFUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون یه پلشت بی فرهنگ کون اینو نداره ۱۰۰ متر جلوتر پارک کنه و پیاده برگرده عقب، ماشینو ول میکنه وسط خیابون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82186" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82185">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQTKlUXLTsZsVu5dXI-OnsqQb_-KKW8QVGNO7tkMdptOTC2SfDHLKJS635yyNWPKzMUfer7iEMsYWSFQOHP3L2ITMSzxaaNc0jHapItMRqKL2L9p-sX9SWzXsK7K0R6UumhGDtJhKeYjJ8d60vA-kA13JUHrT8JfMuuVGJ6wOAAAezpteJ_QCqUPkasiZdmwkwtMJtfncnNtGnDhC2Cwz20riNtWGzJcnAsaYPapbUsjtDQ8U8rXPvsyiiHCvCfHKTWsUK4RAAyf13RsRY9OTUbgAm6z3ORwVInYU7KEZUgyyFZxNA1zDuz6595TbSg292oi9nIkEESiQNrHDlIcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تراکتور
🔴
-
⚪️
پیکان
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
جمعه ساعت ۱۸:۰۰
🏟
ورزشگاه یادگار امام، تبریز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز+
📊
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۵ برد سهم تراکتور و ۱ برد سهم پیکان بوده و ۴ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
قبل از شروع، سقف مبلغ و زمان‌تان را تعیین کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r23
💻
@BetForward</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82185" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEpGHA65w03_qDzkRc5-X-QVoHNxRpBv7pj_6fsR67CalRhR1FgDsznaUa4-408oqotCuwzhjZt_t5yCfnXHLNlqfy4oQuJ5yBaQhXie6oWne0V6ZFEvu0oo91VxSWPPucQefRIQIsnrpbveTqUr8cbZjYtvZGhQfzGKwDH4irFzRV9j0eO5mFwD9P4i4fU6MNfI-vwBn2vDbPk6UgfyRoWcd4ZxFrKWLPD3VBOvNXzhkS4vAsK0YGqUr0NjY6YzutPIQLRO9A99noUpX9ytIUkAGdSZR_R32_oM3R0FyCfBMOhaYBHhZyPbr8xzkSrmJMGwpp3ENE8UO3aQWjJOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز بیشتر پشمام می‌ریزه از ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82184" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0OwbAbL15KK2Wc0RGOcAL_UoRr62BKT64anwLPXeCGnCBt9kieMNii_0ljnLVVTsU1ZYrbCJ6X70umnp8Z5v0TIdyLoOQGElRvMA5iJL7zEf_9WzmNJYFGSMf7sW5VAC8zxoc0oDPU7ZLiUs6ce9Q32pCHxxT7ZAXtHTtIvkxnYFPTo01dQ9llWHhjIZHlmDYRAWoEhFV5Als1GSPc1CIhCmlzGX0MFbGvCrvP_DHEamPnUUGBBao0zaQIj5XxHp5MbhAvYLOGP_HyVgb9wBkoAityoQi0ufcUqtJLjFVeX8Wtci9T-f8eUAE5VxEKESWHnimKvDMV-3SAcOoG5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا که جای مغز تو کلتون ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82183" target="_blank">📅 10:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82182" target="_blank">📅 04:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82181">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl8XKrhqeEwBjyuvazBpAmlnOZWoCLMu_7PtEtZFXTZrnyNZkurEAL8mkV1AR3y3w1euNnBTdXxxdAUoEIBOwd8RPXKU5aYJLh_3KAT9UAL55WFy0AC2_S7rDvp3k5xh1EuzwzjmZgR4wXWPCrNeoawKn1UgQx-0WXO6u_JPAiSc5A3HvkiyQOPU3EirsK09906nO6ygbGsRmT-QGp3AS63nagYzTyLDLrlPd7mzxCtl2v2pA6xF7vv5_SxHcpXTV29AvecIqg3RFewWpcFc5Y6ycla9ZCcqoSRKSISYtIpW0hplGU9hbFvZddX1GpdA1uV4HqkCsjLTXRFP4K0JSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اگه رستوران بزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82181" target="_blank">📅 02:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82180">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK1frAz38ehcir8UgqIUNtQBj3w30XJT0ClNEMgnOOjYVDHl3q01vyJZgngBNKSuWjtYOToJVPFUYbqG25KozP4c_--8sX8qBgNceBr_T-zU4WGkqFJ6v5ai6Kvt0RYrTOeZSPUlYNHDsqiFQM5Yk9lzzFSVKWhX3YnX8XyGCwnGqGwIpNm7Ts59jeDc2OzlHH5YlPaful-4fxtOPzHTQiMZxkCipRF5_Xj401hLH5uHCuBJ3bhqFgcM25V7SyXegHCJwTIR0qScVkm_5SFnsH0simqK02bcHH6uftT8o9FbL2nSfgdbhR3kWuOStpSKIovnxEm0IpYC1LkCFZG5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه شکار شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82180" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82179">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apr1r8OcgU-a3m_e4X4DVumxeNQcYXCGrftXmG8p1W8LaR6wpkNyGgtWH_CchFgZcnNldRX4gfqvDrce785wIZU4tZwloX4Me5T-wgn2nVjxgaCHVH2ctNoRcbuNFV-l-7YaQy_mrFJOhs5ou_WZw6wRSaROBP7sXxqog6gXxn8tm7_OjhW6G5mO2W77yYTuT6tEOig2oqgRMjBAvrEVgYQ12hjvozySuKs7oLsb47kw2cTfc0-CPbRjCaHTlKrwG7nDIWV3mhFj5HBGdruDrQ8Tn6580P-rBTkfAZ0clyT6gUad50l9QabBWj7QPqMHIFK-dyYZHnZAsd1d7bKf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیری پلشتی کیانوش  @FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82179" target="_blank">📅 23:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82178">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5782494606.mp4?token=e6pmAUhqhCbhQEWAYCYOp8HL904EEn7-0_YYhK2PIwuLbEuXO4zteXmo4OMHD_YLDNFwPOLfl4ibyml61GMCSZNJwStLaMEBlwWLBqbzQOhDoD0O9dpdASKU6ZUKy7FvKx-dCG35GboAs9GusPKREcsY2X6VTceQ7u9cDGBgjxHE1xSldhfJkKzO7cafERaQN1-QNflGJZQc22tUTZ0LtNNlnq9RtIwxqEc8tCJhdsU7aC77xdx7Ya3AEGyr7aP07wLtidOncqXuZ31ss2PsgxWt7oiyMKog5VoYsoqHNuIFvAzXncBTyU1p6BDpYTCOZrFe9J3h6urciSTE-N6602oL8tkE8plL9oTkImgrBLqZFjnxVLi4VDAWkzNFa2SleSZ_DCEN8RphKf75KrOORI_FLztNVHY-idP5dXp53nl2dVGhrU6nVAabYD1Yo_NLGwKfv7omtw_cOXPvdev_0j4BugrPx_-Ir4GrF6tgzyStV_xOHo400fWzeVVmN-04o_j-AastdgS5pJoOanzDh_3Tb2P7roBNe1tha7rOpcZ_rP5nh_nh7YwAoSTVgNnOqF2O1Llm6pGi2BLdwDK0I9Mt9SsnRQiuXH895HVVJakYteZbQB8-LxG7du5IaTIff61xL9CgK7LUpT2brmyIb--O-1VYSzhBM_fcjF9WBL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5782494606.mp4?token=e6pmAUhqhCbhQEWAYCYOp8HL904EEn7-0_YYhK2PIwuLbEuXO4zteXmo4OMHD_YLDNFwPOLfl4ibyml61GMCSZNJwStLaMEBlwWLBqbzQOhDoD0O9dpdASKU6ZUKy7FvKx-dCG35GboAs9GusPKREcsY2X6VTceQ7u9cDGBgjxHE1xSldhfJkKzO7cafERaQN1-QNflGJZQc22tUTZ0LtNNlnq9RtIwxqEc8tCJhdsU7aC77xdx7Ya3AEGyr7aP07wLtidOncqXuZ31ss2PsgxWt7oiyMKog5VoYsoqHNuIFvAzXncBTyU1p6BDpYTCOZrFe9J3h6urciSTE-N6602oL8tkE8plL9oTkImgrBLqZFjnxVLi4VDAWkzNFa2SleSZ_DCEN8RphKf75KrOORI_FLztNVHY-idP5dXp53nl2dVGhrU6nVAabYD1Yo_NLGwKfv7omtw_cOXPvdev_0j4BugrPx_-Ir4GrF6tgzyStV_xOHo400fWzeVVmN-04o_j-AastdgS5pJoOanzDh_3Tb2P7roBNe1tha7rOpcZ_rP5nh_nh7YwAoSTVgNnOqF2O1Llm6pGi2BLdwDK0I9Mt9SsnRQiuXH895HVVJakYteZbQB8-LxG7du5IaTIff61xL9CgK7LUpT2brmyIb--O-1VYSzhBM_fcjF9WBL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه عزيزانى كه از رفتن خانم کارولین لیویت سخنگوى كاخ سفيد ناراحت بودند ، مثل اينكه ايشون مى خواد بشه سخنگوى جديد كاخ سفيد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82178" target="_blank">📅 22:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82177">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3mpnDlGovXm0n6O3a6e-qHz6CZ5wsXGksZYB-PibQSF27Jj7bs6XLCFq_WMLDAlzmwfjd98YvUPvyeWnQfdbxnySj0wn-1Xy15mBQE7RVkEhqkoiPzb4S5CvvRA1UhbBfSTPkxB-9ZiHQxPbEnDHbApEOtZLMm5Bn5byqOBlJtfiJxdAv87bVWT81wbn9-TVhB4Q4CxClz3ticGF2b_9-__H6uuZMzG_eM1DXphUPqR9On2E5uFOP0Jb83ZL0L5T6jhcGVJgOn3m8iqUspMO8BKx8nopkaWDsvM-PKaeKHubIjC9Ref_EFDvtHeLTnk_koi_ctG-f_ocWGdNTRvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "قبلنا" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82177" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82176">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403c217675.mp4?token=JZ6JpIYP69Al9SscME-P3hkMuxkjdGGWpSRsP24w_VjL0E5L_bBHGsysVo16GvZCRmMeugsdntzYVK-N6lZryiIfhBZ-vQ42az5sQ0mAkvnbZkYidgn1efRnWNThW1EvL11cBFOwhCU3sIYybVLySoGw6zNDGJVw6ahDWnWuz0lPmcTfsHLyBmBMUXj0pU11hEi2Qd6PSpQ7Zx63WLO-Ae-JHJXgo1KCA65Rh1k6FsviHjCEYOmc2cj5PDiVa9INBPFyTluEj-b06MliGXWVLqbhqs4rEuoT7P0xfJr3YWIBNBNO9um09SdPTE6Tm3AcEVH8iMp8hbY8Yzfot0gtOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403c217675.mp4?token=JZ6JpIYP69Al9SscME-P3hkMuxkjdGGWpSRsP24w_VjL0E5L_bBHGsysVo16GvZCRmMeugsdntzYVK-N6lZryiIfhBZ-vQ42az5sQ0mAkvnbZkYidgn1efRnWNThW1EvL11cBFOwhCU3sIYybVLySoGw6zNDGJVw6ahDWnWuz0lPmcTfsHLyBmBMUXj0pU11hEi2Qd6PSpQ7Zx63WLO-Ae-JHJXgo1KCA65Rh1k6FsviHjCEYOmc2cj5PDiVa9INBPFyTluEj-b06MliGXWVLqbhqs4rEuoT7P0xfJr3YWIBNBNO9um09SdPTE6Tm3AcEVH8iMp8hbY8Yzfot0gtOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آروم بخندید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82176" target="_blank">📅 19:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82171">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7ITwEC1uuwrIH2jiW2lLPEO31CjyVpAagVX4ivVrDzIpNNdeSWX-3IqFTvgIZ3XZ1NeeHyE4e_VxlO156bUoNtBi6dyA8XsyWcHgmY5pTciLOPRSe41W0M3iSt6wEWz__KgXeMvmxH6Elao0vHX4Bl1KQpXtaztx-U-GIBvs-3G7A8L7wQNOKFBzIN1V3ChHn51cqR_pXj7uFT4EF28t1j9sLickO9ObdM3uZ-zxKxSR5l6LVQrkjQYd2_vhQ9ljge4Tn-QCxGeh8HTX6YMpTi1igi6RN_QNKcuKrir1Pv-dW9TkNnPWqk2dkOp2tV39AnJxV-AooGRgu8gixJUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZDTOKEAjqeZFDTfv1ffPhcOSZ7UcRxRHf5EIE4JBJ2sHWNUdSjZM_UycK6yKXmMMvQdsDcXw0hrPaMN9IFRelqwgwBpGfYRGFOiSV0oXj_QlMmCMdmp4mKN8M-uDMDOgNyQZ7CIX0g7TOHFarlBHmFwT5aSZabbnY83BNtbJkjVvIXiHbaCg7DiWbzDDV_1D32KaZ7nm4gIKyd4h9NiOi6h3pYKzaBaTFm5RSPJAtceX28QDyp2oUz-E-fyjuwLfHT5B7axIrmIrrYVttHSwF7SSJI6C42nKKJXTHjN8UF372pqNFvWBz66rb6ccyOeiiVS6ZVan1Ssgw4mihgevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9WWnpi1pYwqHgqRW5GCIp4Txf9N8zGZNbhBuDXLCh58ImsPCuNBxl513ZJNXtgT0RLh5KnQrOcbpVH-Pfvphy9TksDZf3EX_OdpJ4oB_DqFLt_XPXWmGt6BWkrwhFrmWNI4ABNY18gTugpX1wqh-eh-DJxbWaglpfu4ls8aJRe02Iuer-Kf80czXf6X3TMv9i_a2NPdMEJGRglR3GjWzGJ1m0yFyUo6NV7UrebzOJXRBo6Cgkgy1onIDLsRLkOWcKMSQD-RvTA55nJdBOeS_eAxMuRnw7FvZ8o4z-ihmq65E59_x4c9_3RZg0XnIKJ7saEc8GPJRNu902WGtkjfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZpJNW3iv7id2DqerCsbSpDO-11niq5Ev-xqu7E4E8sTPuTx1S_1LxCjTCHW_9FASfARgy2Ju1UL6T70-frMIRbSs2UDDkO2Z0bE-ZVPYdUElGotsnJVCGC2sv7VLo5K2gTxk-hxy_SYvbxWptknupV2j-zlCQM7K4BSFeIXXwQIjEVka1dnUFLBhGYmP-77FnAWrg0FMG0oNmynn1gIf2oO1DGhXzsGgz2f9ceCkomB3Lowv1m8ko6c18SQvBng4XPhghZZcm2FYi1gqnwnWv5BGBfIoVrxD002iAsVf5ROKLUPSUkdexAOrkvtVaUKZbfayX1YMWkWawXPYAdyGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=D5fgWV7ZBAghcN0t8u4YrFonFLyPXFJyY03F1zL9DLKBddmUxMz_Sf5rWH7AjI4qw91KgDPo9MQu19VfxpSJtdl8nCOFGEFstVWplzfqBk-st-wZBv3hMMWZBP75cUko1bmhlMDibMcowj9jW495tCoANNfSTcZuMiBUgvpE6n3E58mA8sKqCqtV1Csks_mBcIjZbMOlIfk_DDJFy505h4N7o75l3xoEklYqu_innS0yFBnOFIUKfMfj-7MFNHAxzuO1x3YUxLKNAZBJM9CjgcJOe0aQGX-laXaDa-Az0JvbM9frHxxyik0sBR45Ag_iYQJOI8bs9GtBfvnJVyijvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=D5fgWV7ZBAghcN0t8u4YrFonFLyPXFJyY03F1zL9DLKBddmUxMz_Sf5rWH7AjI4qw91KgDPo9MQu19VfxpSJtdl8nCOFGEFstVWplzfqBk-st-wZBv3hMMWZBP75cUko1bmhlMDibMcowj9jW495tCoANNfSTcZuMiBUgvpE6n3E58mA8sKqCqtV1Csks_mBcIjZbMOlIfk_DDJFy505h4N7o75l3xoEklYqu_innS0yFBnOFIUKfMfj-7MFNHAxzuO1x3YUxLKNAZBJM9CjgcJOe0aQGX-laXaDa-Az0JvbM9frHxxyik0sBR45Ag_iYQJOI8bs9GtBfvnJVyijvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامنتای اینستا واقعا جذابه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82171" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82170">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2cUuvkRR6xK9CdFP0pWx6yegkn1Jw2qD0CK26XB54rS0LgeG-Yf09ObWikupeK5H3N0u9hF2Tjw8ahHmjWuXfSnoyKDW8Xey3n52xs_glM2zcz93qwvgU87Im6ZbIiBLIfmnvnTOuPa-vzk_qqifGE1bGioU7JP8iGAYc6uxVVsMeKytJnAy54YTgOYZu5q8sk693_W8qvkCzzp2Xm0I7m68eLPu6qUV4ZEen4BkKTueIYVfneG2RzaMwiaGXHVds9DV4vcRfl-5K0KLyh8OqWKTF4kge8vx6nBK8cQ3vHDs_wX_cbXxJQ46-cSmyRrwYfyiWZqxsALBepuo3EUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودتو گول نزن ارسام کیر کاگانم نمیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82170" target="_blank">📅 18:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82169">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پس دابل آلبوم و این کصشرا چی بود
این چه کصشریه</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82169" target="_blank">📅 18:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82168">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بزار جیبت بیبی</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82168" target="_blank">📅 18:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82167">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82167" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82166">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL5Fv_XLIs8XfrygulwvfVn12TSW1K4gvTvBSMdTkqhReMquExhrZbaL4mCK5BzYQiTZxYmXqEq5ECF3B2S8zqdKIlRInCFuaM9Rswp5KHbOEqb9odHxHRiTwcqxR8Buc07JpKLKvO98f3HpYw6NrbnNi0vDw5izJmzona0Kb_2y8D5R9n8Ttdo0yDTH7SfVcAS3pHkNMZtgr2rDJwzirrwXHULjCTT7BFKSoI4T42eKKq4fl6d14BYK9oNAHVGMda6Wg62xmTc-whnCK46XoyIPFZzuGeiRilwuNjpO2yeB30H-qBRVNYyntkHkLncRA1R3rgC8HOvMK13BLSaUsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82166" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82164" target="_blank">📅 17:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbnR88iywTaRbhyeeXbvkyvuQTE6bEm5R30I2VqKR9b_VC89HlNk3uimdb5uYn9-2UQz1FMKyBeHXk5biUbm4FTPOruztnSw-sABjlHX-bkvh-l4E4qFoXJ83zfjfmo0tlCCBU2ea6MHeEXE2a3xaFz1VUR7IgdLIFO-1Burkb7C_X2AQdizeVzGWZfs8GOSUHzm69JP3iacdl5IPPVa6LCQZV1jE4RO1_mw_1bjzd9dbiRv2YAHK9YuM3KCDjZOVT7I3MCWh0RxKNQrVM3P4SwzfSU1fcdpxGlKH3wC5lsHsnGwcZJ140BYvrwjlJFFnpARGKars8TCQEBnLjoN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82163" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=seug9quxKIDbXAkhm6IovM80V_wH6FLgm1Z4JsiRmX80RyFoMmWFmSadAs6s841LqPoj6z0zPDIC--N915b1luySHgkthxLgfsieoEGUTF8yoLRKuKUo8_Te9Bd1rO0gP2VlKZyUEK9snwAe5_IVy2QqusFYhJCjHS3KGGj7MmIkNc7ZqibZgaQ62pPfcUw4pMF5O81B15JNc6g5U91HA0J0M36ObGFoscOUxGcI85qV8W_qZ1B_7DhvwRoEJzpTWMw1K1xn6VVZNCGCQ_j8uOettnBHnUjvwruzIgfDMBS7cs4VV_hw8VboaxjCTjpeOEmLZu2CMscTmBYqH2lCoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=seug9quxKIDbXAkhm6IovM80V_wH6FLgm1Z4JsiRmX80RyFoMmWFmSadAs6s841LqPoj6z0zPDIC--N915b1luySHgkthxLgfsieoEGUTF8yoLRKuKUo8_Te9Bd1rO0gP2VlKZyUEK9snwAe5_IVy2QqusFYhJCjHS3KGGj7MmIkNc7ZqibZgaQ62pPfcUw4pMF5O81B15JNc6g5U91HA0J0M36ObGFoscOUxGcI85qV8W_qZ1B_7DhvwRoEJzpTWMw1K1xn6VVZNCGCQ_j8uOettnBHnUjvwruzIgfDMBS7cs4VV_hw8VboaxjCTjpeOEmLZu2CMscTmBYqH2lCoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82162" target="_blank">📅 17:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a59034baf.mp4?token=l0UR2ZS-lKIZ0yp8oX6sPlxOEveJAqCPk4LsbYFGBGzRcgWL0fkTIJyyUORqKWlU3amlM3sD2M7hjLarXqmxS0N-0qRhUSOm6gHr-3y-N0TXrHoky6vWDtYwEC-pReriyLSuEr4BV89xjBr4Un7V1Iaab6ympTdzJQedVIIQPgoUgxa-nhDFwwAmLOB48-cOn1DU2ZgGIAB_XoBun1sQ47P9aVttooCZsvd05N68fMybJuZuSRivS2N-xmmWQvcJV3EfamrgY4uHra2HBQVHrzH8KGO_z8OoHN3ev5uBa5Rio32Ss2ozbQXmlx2SW_jfKt_6dAfN6gKN09ruqSjJRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a59034baf.mp4?token=l0UR2ZS-lKIZ0yp8oX6sPlxOEveJAqCPk4LsbYFGBGzRcgWL0fkTIJyyUORqKWlU3amlM3sD2M7hjLarXqmxS0N-0qRhUSOm6gHr-3y-N0TXrHoky6vWDtYwEC-pReriyLSuEr4BV89xjBr4Un7V1Iaab6ympTdzJQedVIIQPgoUgxa-nhDFwwAmLOB48-cOn1DU2ZgGIAB_XoBun1sQ47P9aVttooCZsvd05N68fMybJuZuSRivS2N-xmmWQvcJV3EfamrgY4uHra2HBQVHrzH8KGO_z8OoHN3ev5uBa5Rio32Ss2ozbQXmlx2SW_jfKt_6dAfN6gKN09ruqSjJRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارتوش کورک
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82161" target="_blank">📅 16:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82160">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سیتی خداست، هر سری که تیما اون پولی که برا رودری میخوادو میدن میگه نه ده تا بیشتر، خلاصه قیمتشو از ۴۰ میل بردن رو ۸۰ میل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82160" target="_blank">📅 13:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82159">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnZiBkw6h1YHxG1SQjXLTym3RJFR-CWFBXOHqGV4I05_ojKGBV7sYPmlB7Y89Xkujg6-61v0FvZz5NFPn4hdmb0Q9BPEuz_b90HmtqpahcpjtjE7l5MyelKGzH4Q5EZNmWumTva204HfMc9k-kR_2IkYTL3ThRVrctwbrKBTTt4JOaZfUTlYRG_XHcbv3_KFDUuZXXl1dllwsXqgF0t2PDhu7mm8x4sEDEQyw2HFr65OL9y9g2XWQhpqVKFOxNJ8HPq0HmV_6A0vwQRNHvrvVOCiNBMiDKYsukUn1CRU5De6WjTUVdxvo5pMseOxWi7QQvrrsPMBUcxfzVyqU7BGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویرو هربار میبینم جمله "آقایییی محترمممم" میاد تو ذهنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82159" target="_blank">📅 12:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmMvXXA7AaTftkNq9q8FdANdEBbxIokkhQmjGryRX5srnqkjOHJAgDQqudoo8vxel0W8591l-0de_MJipYBTr64JHiPWwSUDxrWSHwb9XA3YmzoTgP2Cz5D5-ite-GYqx4dH7yIKouGGlvhEizFSBxKC2DVYKDB-FwEow6FRCO5T7jfW8RECzZfiotwPBY0S6sBZmNPSv9cRKAdX-pmqfMnUZVde0fDkYvs53jiOA5Pr79fiRkKsO-KFFhGv3CnCVvx3uIfhWrYJVptX_TjTAtzO_m7IezyU0H0InypmHWcq48bU3Bh6ln4wk1zY3pdKatmMAGbgGxWkQcHrQijbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفه ریدم تو سلیقت
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82158" target="_blank">📅 11:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82157">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e23ac6b2e.mp4?token=nJidxAe4kkxBQAaweKQh-8e9qtPgC4yJAA6tvMFwp_LQ6xSJSPbLZCKQg9b8-LIDYB--QnLc4BrGSnCiSP3dbe10Et2Ox_Cj7bLk2t56wBkeofyz7kigdzocExG3MqTan0lKnb2JGuuD4KtE5SL4uuFdGje6ZnATrNYPlkZ68SfoDubKYNrbIf-Sx-BbOAwat3C68hafP2ZfIcrQvs-Oq8ps_Fer-wZAZSYE96UPzbVxoJN0auwzmHLyKTqKy5c_Wt4i95wCiZjR8u1U_72Ci3kQcCexJUosQUfcTrx9zNSOkyCSJY1ZnOcwu7-x9_gUbLvg6GvHLzuzD6PbunfWVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e23ac6b2e.mp4?token=nJidxAe4kkxBQAaweKQh-8e9qtPgC4yJAA6tvMFwp_LQ6xSJSPbLZCKQg9b8-LIDYB--QnLc4BrGSnCiSP3dbe10Et2Ox_Cj7bLk2t56wBkeofyz7kigdzocExG3MqTan0lKnb2JGuuD4KtE5SL4uuFdGje6ZnATrNYPlkZ68SfoDubKYNrbIf-Sx-BbOAwat3C68hafP2ZfIcrQvs-Oq8ps_Fer-wZAZSYE96UPzbVxoJN0auwzmHLyKTqKy5c_Wt4i95wCiZjR8u1U_72Ci3kQcCexJUosQUfcTrx9zNSOkyCSJY1ZnOcwu7-x9_gUbLvg6GvHLzuzD6PbunfWVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سم آلتمن مدیرعامل OpenAi:
احتمالا تا ۶ ماه آینده، Chat gpt بتونه صفحه نمایش موبایل شمارو ببینه و بخونه!
به این صورته که کارایی که در طول روز با موبایل انجام میدین رو میتونه تحلیل کنه، مثلا وسط چت با پارتنر یا رفیقتون، کمک میکنه چی جواب بدین.
یا اینکه سر کلاس آنلاین، جواب معلم رو چی بدین؟ حتی می‌تونه تماساتونم ضبط کنه و وسط مکالمه کمک‌تون کنه!
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82157" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82155">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33fe099a1.mp4?token=bsqBw7vBM02pp8aaX7NeNcIAuP69dRSPybORsCkAxh5DI3rJU9D7AFQUI6D2mLCecFSniZEcEwwyxz2Duht-B9o_CsRbgnwUFlZI1QBdGa4cFUd4_aFQcM7wyIWheKxtNda1XZGbpHNuf9uVYl9qvr3FkXYQLZRgWT-K_6l1I1YGPetHryWx7Ow31qyMUXDazHDlphc_rsJXcOGIwgpA6951nChndD9pVtgiPn-IET-x1s-jryxdolFy2CfK0BhVZhdX_8zpTYcpiLQen7fPPVqUoz64LxQPgtoCdMHd-tJ5uqsE1hzsv84GiTSLdYQP8i0wHEWz9mE8zYFjHB9OHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33fe099a1.mp4?token=bsqBw7vBM02pp8aaX7NeNcIAuP69dRSPybORsCkAxh5DI3rJU9D7AFQUI6D2mLCecFSniZEcEwwyxz2Duht-B9o_CsRbgnwUFlZI1QBdGa4cFUd4_aFQcM7wyIWheKxtNda1XZGbpHNuf9uVYl9qvr3FkXYQLZRgWT-K_6l1I1YGPetHryWx7Ow31qyMUXDazHDlphc_rsJXcOGIwgpA6951nChndD9pVtgiPn-IET-x1s-jryxdolFy2CfK0BhVZhdX_8zpTYcpiLQen7fPPVqUoz64LxQPgtoCdMHd-tJ5uqsE1hzsv84GiTSLdYQP8i0wHEWz9mE8zYFjHB9OHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال شده باشه اگه سندی چت کنه چی میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82155" target="_blank">📅 09:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82154">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یعنی نتانیاهو با اونهمه قدرت نفهمیده پوریا زراعتی آدم جمهوری اسلامیه و بردتش اسرائیل و باهاش مصاحبه کرده ولی چارتا کصخل تو توییتر فهمیدن؟</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82154" target="_blank">📅 08:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82153">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">درکل فیلم قشنگی‌ بود بشینید ببینید بفهمید تو چه کشور گوهی زندگی میکنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82153" target="_blank">📅 03:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82152">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=UgzVVxGf7t0IKjkYdfEY12nF-jmoHeb-8d6QIwyZW-MA-TJW4WTClnZtkXGn7NtqVXiTYoTcVv9sHrvcKoaYLfTRlC5pZ3U6a65f_GWQome37hcuAIuwhPx-RbNYQXUabbqgbzW7lHCmkJnddBjuDzWrJw4nMbhFc8fmaar3yuoDPLPFLy8-gMjseYO8ER0Caj3oEfYOsmA0mdoHFlEmmi422eWXrw2uqtjt8dgaXi5stkxYWTTkYB3L80GOpQ9-PXHpmy-V6bHI4o-hAJW_nL2BA_xlSAY1TvD6HSIkvzvzhZGl4iCed7-qEgllHslpkyaQplB6bHJKyy5_6wxKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=UgzVVxGf7t0IKjkYdfEY12nF-jmoHeb-8d6QIwyZW-MA-TJW4WTClnZtkXGn7NtqVXiTYoTcVv9sHrvcKoaYLfTRlC5pZ3U6a65f_GWQome37hcuAIuwhPx-RbNYQXUabbqgbzW7lHCmkJnddBjuDzWrJw4nMbhFc8fmaar3yuoDPLPFLy8-gMjseYO8ER0Caj3oEfYOsmA0mdoHFlEmmi422eWXrw2uqtjt8dgaXi5stkxYWTTkYB3L80GOpQ9-PXHpmy-V6bHI4o-hAJW_nL2BA_xlSAY1TvD6HSIkvzvzhZGl4iCed7-qEgllHslpkyaQplB6bHJKyy5_6wxKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82152" target="_blank">📅 02:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82150">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82150" target="_blank">📅 02:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82148">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RonK9UbatD9X9DqQ_xXQ4S9QULYXssP-9Z17GbaqHU01vGMTNV0YqtSxuImsVxmaWqxMtuchA34nX9xJsyvMy3O5XPMsgmOFj60vHiKaA5xgO9S4tLYCYsDsKvM_4OPJcdB5cATtlyNXrNMnPjZ9Gh2QpP1S3Sg43Lsb8sB_askNpId4YihGfpqsuXlCUglgqWb2W4ycKuweEBmR3-gaqyujLSCDlV2WLpskim4WU0FnRLBVsZw67kLdDoFpbGCudcGEBlfaXTOd3gQYGYoM7FVxs_rbddUEdQDnRHUauF4gr_IoScqaVZFOIL0vAqcbvfYN8H9ziW0RYOOW1y-35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0e2ba89a.mp4?token=LvlaLNbDR9wDkhGb_ZdJmKXVU0cMbT-NMICMV3w0ttpzOkNod5ZLy483oMTg_mBIE-ty4_9Ii0_ef7uLYl2VHdhRus0Gj8gofCSfZ_2bZpm1Qg4HuzgeF7f5X6K6GNUIC3RamS30Ks7aUTBs6lT2wAk1C-Z3ebHUasX2v3oXpx3z6TF_j4KvjJSCX0QQ40YRyM6mB99OZ8oXDCZCShwAylwDzwJ0F8AzyaSV5v0pei9ARY7V4pX3s1gXGTpwGZywR9YihxshWROdfUSX8K0EmEFmCfloD-9dtc6q0ufkuiOKaOf4cbcTF7yVtttgvgu7Vs7ehXSfts7S03QfHZHp-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0e2ba89a.mp4?token=LvlaLNbDR9wDkhGb_ZdJmKXVU0cMbT-NMICMV3w0ttpzOkNod5ZLy483oMTg_mBIE-ty4_9Ii0_ef7uLYl2VHdhRus0Gj8gofCSfZ_2bZpm1Qg4HuzgeF7f5X6K6GNUIC3RamS30Ks7aUTBs6lT2wAk1C-Z3ebHUasX2v3oXpx3z6TF_j4KvjJSCX0QQ40YRyM6mB99OZ8oXDCZCShwAylwDzwJ0F8AzyaSV5v0pei9ARY7V4pX3s1gXGTpwGZywR9YihxshWROdfUSX8K0EmEFmCfloD-9dtc6q0ufkuiOKaOf4cbcTF7yVtttgvgu7Vs7ehXSfts7S03QfHZHp-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئال بعد دوسال جام گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82148" target="_blank">📅 00:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82147">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG1cEYSWrOSrGrG-3df2RSB5vqmDuHsmkTFd4TPeuSwIZw56X3BY0c7sF8kaZM41LSJpnqg9iKpQ7xc1OjY71x9wqP-xCMcv2aShjdNf0yhRsqQrKGJP7LKF1iZo9xleZUEYmuufLijwNKKXG7Jvu01XyfiEEac1gQBPyqs3ZRTISGTC3E9clrP1OXdyUiRqAoc1ZiC5E6SCsNV6DMbSzntKmq-Rc6X4ioJGQKZfJbIb7jeKOU5wHdCs6BnpPpSoTPy3YW04c1U6gCT8bIYov85O0_XOgClc9blUPv9tUaraE2T9xesW1y6vg2BBxZCOmUNvc2yKBtH_FXWnNYk3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اوکراین هم عده‌ای از گیمرهایی رو که مأموریت هلی‌کوپتر GTA رو با موفقیت گذروندن استخدام و مأمور کنترل پهپاد‌های انتحاری کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82147" target="_blank">📅 00:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82146">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پاول گیفت تدی تروریست داد بیرون
🎁</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82146" target="_blank">📅 23:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82145">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کیرم تو توپ طلا اگه به کسی جز کوارتسخلیا برسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82145" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82144">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVCvqRfHa3RrTaVS65ihLlMtsGnxHxA-3NQ6t7xLa90bSMjrv7om-pEF4wBUSOjzIs-su1eJ7YB5KcbYr9goKYNlZTaAAiXlsrBSUkzNm7ICqNvZ32bAO1FucmGI1Kct34swPPBSuDndyr7wQ1AlZm2fgivyofDcWx-qNNCkyhb_L_VeNawypCHN4U75nJ_AnvJnlSK5CSkejKi8EY5lNQI5SKQE5pknYQ_gYL-zVbgpLbioZbVVWg6t8_TpF2INTKXjZMHEIUexek4UGqTEpXjyHvancI4Nd9SvrrvajjrtupNvV9B5F8DlSSREcu7x62EMOT0HGO8LuBD1CO0i8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به قدرت جدید فوتبال ملی اروپا, هلند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82144" target="_blank">📅 22:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">البته ما کی باشیم نظر بدیم، چین برامون بنزین میخره</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82140" target="_blank">📅 21:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82139">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">موضوع سادس، نه میتونن بنزین تولید کنن، نه پول خرید بنزین دارن، حتی اگه پولشم داشته باشن بخاطر محاصره دریایی نمیتونن وارد کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82139" target="_blank">📅 21:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تورو ناموستون شما دیگه حتی با افغانستانم نجنگید ممنون.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82138" target="_blank">📅 21:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">داشتم فکر میکردم ماشینو بزارم خونه با مترو رفت و امد کنم یادم اومد کلا ۴ تا استان ایران مترو دارن</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82137" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
