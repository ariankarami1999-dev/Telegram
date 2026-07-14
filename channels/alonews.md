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
<img src="https://cdn4.telesco.pe/file/OFmAsl6AJkLnCDdVMTYWn0Nvq4a6zMxJkG7jW0LVOWH0zYiDhf8XYAfIYYEbtUaHMt9KBURRypRn607pWUJOE9IA78uZwioSJPKGswfd1ruU0z6iQaJjwa_BrpbbqkrQDIMzzOSAIY8XouiewMkIyl_W8k4UZ_TZHpL1Y9fEuCUrb_jmqcLUhGAAT4zBwd5_mTMUXrD1FFB1Y6PyvCrUKEj30I6qGNc51Udtn9IPVyPkf0rwqP9vbr5CMKDo7COiNh4M2nKEZtAf1ZOiFsmmKu6rN3csrbxgZw_emlj4uyQ8zgNyC9piy1cPnelRsnxLk0FKWmc3CzW_uMN449fR0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 22:34:32</div>
<hr>

<div class="tg-post" id="msg-134186">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/انفجار در دزفول
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/134186" target="_blank">📅 22:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134185">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/alonews/134185" target="_blank">📅 22:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134184">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azrrd3pGwG5971pUhHqnVqjWD6m49CoXbX2A3ySu4xPhursCzdQjznQ97rb3o_49Sp_XJm0arSaOlnEAjKUhFKp8dOZ00Pj2cdlrS8W5Tp2tdD9XupIhgL3Q2XqBzNwFKb9ggssXcC0j-jHmbBqqvF02UyrS6hwjLHyRhdM9MzzhmExHnjUd0FKuaHJHFGzPOQkaHMjgGiw82oUOh8k8TKaNfp9bZAKiXCMhISvmz73hWntr3g_aCNEo4o5BgJbPdlBvWpe06dKqYgTBsvyElveCFIY5kdJFhWRkyMIDRJ1eRQC76Vn6uy461sSo_XEJ_56er_o8X-InNWGiXcEmOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
زیر 18 سال نبینه
‼️
بلاگر دختر و معروف عراقی که فیلم خیانتش مثل بمب ترکید و توسط همسرش تکه تکه شد
◀️
مشاهده فیلم خیانت بدون سانسور</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/134184" target="_blank">📅 22:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134183">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری/سپاه پاسداران:
تا زمانی که نیروهای آمریکایی در این منطقه حضور داشته باشند، "حتی یک قطره نفت یا گاز نیز صادر نخواهد شد" و بازگشایی تنگه هرمز نیز به تعویق خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/134183" target="_blank">📅 22:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134182">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw_rNIt0p7faQ5PW0ArxX1BwrFh9WeTw_PGw5vNKXCLdTUdEHHBZdSCzAPKYJ6F2S5xAXdGVBN__jmYJXOm8otfDIAvmKn9MjELOfy5OL782o61fDr_bIzFhe8RlKoJoRnAci4llbzINxA_7nJt-9s4gpVxhILQuOQDmjPRBbAovesrjnW2mGJ1IKs1FKT25dZbjldXScSboXNakB1VNBec__6xgheNHOWqCjkm6f3jYNeHaCc47c5-Z7i-EnmJfDcrOfyOMYfVapp6fCfRsWh6sQaEG_6HiLCCOOITFjd30ZYDsBdDvd62zbCz9j7_epaiFFHva1tDkQ5GeEHQbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت پدافند اسلام آباد غرب فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/134182" target="_blank">📅 22:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq-FJHfGtNetNYXWZPh2GU0vQgeGd8BwbbI142Ocs48Jf98zgK7R2vzdflKhqzZrQd9JHevnFMXEHZ5HcPlikuZRw_Rh7F6Ct6u4wrTUsEh_uTbHOxaFOiaE5DTPIiTuhKabFf2-d_uyRb0x8Yixf3f9hD2kz25eusOLlQD5ES2nC-76Uuay-7WwhZpgZb4XTfeEFzGLYwDwEc2tslh4tkpUw43hqlzUCQnphJHUHmLe7egXDQNuW1RjhfzqRrF3l26EcZ085mqFN2iWbmpj3DlGZLTA9vW1QHjOamxVLv5lq89vOh68y91ZkHnlkWqPczgG_ez1JwGeSJkGf2a_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
غریب آبادی معاون عراقچی: هرکسی که در داخل به ما بگوید برگردید و شروط را اجرا کنید یا تنگه هرمز را باز کنید حرفش برای ما اهمیتی ندارد
🔴
دیگر متعهد به تفاهم‌نامه اسلام آباد نیستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/134181" target="_blank">📅 22:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134180">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/by6Ig35tEiXhLZ95KmnbKAduWFOkZ-szRRK5gNpDpe4K_nmeUmtrFY9skQ6GN4u-ouYCLgSLqfl0WKzoEMy-tvAl3EA-KH3NPXNeeBHyQWXzlr7TkXeZf3WyINfq3WbSgUARE5inzxNXQc39TmJvMWOI8j3xkSfptFkaOCX_KOWYj7tGTP423oktaRwHnsOiyXOKV3ojvWrqhc0ZfBNwpm_mQiu-37fDKKWlg8wqVffWMP76cTGn6hlwDlCj-h742F_BDaAmamNb38rVWND8KGd1cyHtFglNaHU5PYFaiy7RM00F4vz90BMRkDSw7cr6N8cRD53hK2vezu1BCSF75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پخش زنده جام جهانی ۲۰۲۶
🇫🇷
👊
🇪🇸
▶️
کیفیت FULL HD
▶️
رایگان
▶️
بدون سانسور
🎥
شروع پخش زنده</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/134180" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134179">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مایک والتز، سفیر ایالات متحده در سازمان ملل:
حوثی‌ها، یک سازمان تروریستی اعلام‌شده، پیروان تهران هستند. آن‌ها از دستورالعمل‌های سپاه پاسداران انقلاب اسلامی (IRGC) آموخته‌اند.
و این اتفاق می‌افتد: وقتی ایران غیرنظامیان را ربایش می‌کند، حوثی‌ها نیز همین کار را می‌کنند. وقتی ایران پشت سپر انسانی پنهان می‌شود، حوثی‌ها نیز همین‌طور عمل می‌کنند. وقتی ایران زیرساخت‌های غیرنظامی در سراسر خلیج فارس را هدف قرار می‌دهد، حوثی‌ها نیز همین کار را انجام می‌دهند.
وقتی ایران شعارهای «مرگ بر اسرائیل» و «مرگ بر آمریکا» را سر می‌دهد، حوثی‌ها آن را کلمه به کلمه تکرار می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/134179" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134178">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NibiqQ-W_id63cxKrc9kpbciNrKNAGyM4Xs32ErsNIk-9oXZUiwJOGrS5Wy6B0lh4LBnDEh3SgMc57mVoaPyreFzkQ5B0wVt3Je7bkfUigLywo-_3Fjd7g1ODOSEZ5GEARrKyo0ihZx6H_c0Ixjl4Xjm30ufmw2nUlsUDUoeHIQOtgw2X8QLbCrbQKczQpKck9EyYOfCngCSEpQJspgr240BVLbzUGX3KxS5gnjjF3N0izCX8MZRWHbLEfKFtQEzNzwhtSs1iWuF2W1Yw8KPjO-O8aDwaUjochTACmrCyBXQ1-hjZa8OBL997I4OnPj91lYNDg5rS6keSvOjmIcUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه کارزار راه افتاده که میگه کسایی که موافق جنگن(بیشتر جبهه پایداری(خوارج) و وزیر اموزش پرورش و نماینده های تندرو مجلس) به جنوب کشور فرستاده بشن و اونجا اقامت داشته باشن و کارا رو جلو ببرن تا از درد و رنج مردم جنوب که هرشب حمله بهشون صورت میگیره اگاه بشن
😁
به شدت داره وایرال میشه و همه دارن امضا می‌کنن!!
اینم لینکش
⬇️
https://www.karzar.net/333344</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/134178" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134177">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/134177" target="_blank">📅 21:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134176">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
آموزش‌وپرورش: حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/134176" target="_blank">📅 21:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134175">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
به گزارش پرس‌تی‌وی، وقوع انفجارهای پیاپی، پایگاه‌ها و تجهیزات نظامی تروریستی آمریکا در بحرین و کویت را به لرزه درآورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134175" target="_blank">📅 21:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سی‌ان‌ان گزارش می‌دهد که حداقل ۲۲ کشتی تجاری در ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134174" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
اکنون وضعیت در بحرین عادی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134173" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134172">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/ یک مقام آمریکایی به ای‌بی‌سی نیوز: نیروهای آمریکایی در حال حاضر در حال انجام حملات هوایی در ایران هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134172" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134171">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت کشور بحرین: «آژیر به صدا درآمده است. از شهروندان و ساکنان خواسته می‌شود آرامش خود را حفظ کرده و به نزدیک‌ترین مکان امن بروند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134171" target="_blank">📅 21:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134170">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJCDH0Y_c-nvJ3BLtC_HPdm107ijbZdKOXtplf5_utFuwl6QOuovTVINZzZ162S92h2zyiSiKOTlnCs01J4aC0-lsyhy0tI61cdgC4RQ5xsXtPDa7Cj64AJJ-fGYR2EuaX3kfxdkuv05hLZSd6W5Eo8vdNp70e38JQtsR2Bd1k2DSBBJmTYTFyI1thcjY0Xi8r6v7GhgjRIfvUAkZlyGueoMJcMegICNfAclKEcH178aIOJ-e9ttSMFKLq65_GmOgUn75ldJ2z05HApAFe0-sUsxpbI-GKYANkoCsppJQitFJjCCC8vFjrvuhnPRqUrW1K0uWy4g3Fr9hlBo8xbDrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ا
نفجار گسترده در جنوب لبنان؛ حملات اسرائیل در ساعات اخیر چندین منطقه را هدف قرار داده
است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134170" target="_blank">📅 21:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134169">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / پایگاه پشتیبانی دریایی بحرین. صدای انفجارها در نزدیکی پایگاه شنیده می‌شود. احتمال اصابت وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134169" target="_blank">📅 21:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134168">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فعالیت سیستم دفاعی C-RAM در بحرین گزارش شد. این بدان معناست که پهپادها به اهداف خود بسیار نزدیک شده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134168" target="_blank">📅 21:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134167">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c346e03d.mp4?token=mrtN_b1V1hjlt4gZd1cNBf3OdL-A56dXxJs_Adh16GXKlNIkHM4F89t3L9gV6JE3IPv5fcAloH2jDw_K9P59fytDf1Nwx1UmaS9A6knzlrhgipW_I3fnN9cWjKB_rBTFcfEErBB2A8hNNiSaSh6Tpt-btRNEcVVVNX3OpvQUjhG_HO_cTox1JuQNtU1gP7FF7VRVJ52AXaRYnIf7D3eqAvGWL3mvVW1cuwfWt2akvGHsHnCE6uSoX-pPPl0etzCOFy98tJ0aCJASxD7exXLb7EsM4KGGzXcu1szn3GbZnDJnAZ8eHZaGLplD9i3FKKa-RIKq5Q74XIrBdZMn7wpH-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c346e03d.mp4?token=mrtN_b1V1hjlt4gZd1cNBf3OdL-A56dXxJs_Adh16GXKlNIkHM4F89t3L9gV6JE3IPv5fcAloH2jDw_K9P59fytDf1Nwx1UmaS9A6knzlrhgipW_I3fnN9cWjKB_rBTFcfEErBB2A8hNNiSaSh6Tpt-btRNEcVVVNX3OpvQUjhG_HO_cTox1JuQNtU1gP7FF7VRVJ52AXaRYnIf7D3eqAvGWL3mvVW1cuwfWt2akvGHsHnCE6uSoX-pPPl0etzCOFy98tJ0aCJASxD7exXLb7EsM4KGGzXcu1szn3GbZnDJnAZ8eHZaGLplD9i3FKKa-RIKq5Q74XIrBdZMn7wpH-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهمات خوشه ای شلیک شده توسط سپاه در آسمان بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/134167" target="_blank">📅 21:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134166">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی و اسرائیلی مدعی شد: ترامپ از نتانیاهو خواسته نیروهای اسرائیلی را از سوریه و لبنان خارج کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134166" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134165">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سخنگوی ارتش: تنگۀ هرمز وقتی باز می‌شود که در آن ترتیبات ایرانی اعمال شود
🔴
مطمئن باشید دربارۀ تنگۀ هرمز حتی به اندازۀ سر سوزنی کوتاه نخواهیم آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/134165" target="_blank">📅 21:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134164">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/977fdbd2de.mp4?token=jIjv5D1-_meR5KiwgSmP3_FLxciLjtFUhD41htg-ErDzLeLymPmFCWof6G9ppgKlMBgKgEe7LBFBCtIpPudzowjeNAHMloHELcUWhpGA8HkZDeic04Zjkz-zEfVRe7p9U0CtwkbNeNBOXxlaEnambwHSLz_T9aNCKkjYys4EPmEYJs14IGxRWP-S_QrP8AKn9kgKzCP4fgJte7KBRo7JguWGTOsHk6ipF_h6tixgCIEi5cJdvRHmQxtr7EpDTQBzh-2orEmXMizSLHp_N6lScDsl-S3788ISbcDANKYd-nachrCDLPWGmNhDaiZ1jZFoBiOHi_RS7vv-oIFoy56Bfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/977fdbd2de.mp4?token=jIjv5D1-_meR5KiwgSmP3_FLxciLjtFUhD41htg-ErDzLeLymPmFCWof6G9ppgKlMBgKgEe7LBFBCtIpPudzowjeNAHMloHELcUWhpGA8HkZDeic04Zjkz-zEfVRe7p9U0CtwkbNeNBOXxlaEnambwHSLz_T9aNCKkjYys4EPmEYJs14IGxRWP-S_QrP8AKn9kgKzCP4fgJte7KBRo7JguWGTOsHk6ipF_h6tixgCIEi5cJdvRHmQxtr7EpDTQBzh-2orEmXMizSLHp_N6lScDsl-S3788ISbcDANKYd-nachrCDLPWGmNhDaiZ1jZFoBiOHi_RS7vv-oIFoy56Bfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‌دیده شدن جنگنده اف ۱۸ سوپر هورنت آمریکایی برفراز چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/134164" target="_blank">📅 21:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134163">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بیش از 25 انفجار در بحرین شنیده شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134163" target="_blank">📅 21:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134162">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
صدای انفجارهای بحرین به قطر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134162" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134161">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8vim3RQaxk4tUUdmp8uFYvcp6AsyId1uMjhK9_jwxSY1Q-CWbUu5H8bI31fn4LkdNvFRkVNLVpNnLWuZF-Lnuf2JAF4MWop-Pw-vFlu4N5ogOnQnL47-RoQqOIXNHnFluExoXTptwiSbqMORd2d9aPPOnUX1OZGSfKlsLoOdha--ijffMHOp3-H_ZWmW54fXnQyqAmecDXKeM2qVHTk7KDSqTSQaXVGqe7hyljlLUR4HpMLYWpDCpLMYttHj7RLlwarb0HwuQ7Sz_jYvBLcFg0_mierzPQRPdlssFG_LOYMbHYoYDA5VAJU-T46uhbBXOj7K6VcYTMfBzFTDfUqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای غیرنظامی عازم کویت در حال بازگشت هستند و برخی دیگر به دلیل حمله مداوم ایران وارد مناطق انتظار می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134161" target="_blank">📅 21:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134160">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
هشدارها در کویت؛ سامانه‌های پدافند هوایی فعال هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134160" target="_blank">📅 21:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134159">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346a1329e1.mp4?token=WI7lF2-UQPQCYx6faWCRgINAMYhEJMTq43Rp8HX4YlGVd-YEdhN_0XXF66Bz6hLWne3Ccg29Uam-V8EeOzWkrY7llRWhu9CyG1PcB30BACqSX1E5znCdm30aSMV3iJSBODftPwV2HN5r3m9pzsdhrHALR65I3quMeFfDOr9HIn3RmpCQPlUgG4kCMKJWTrFdaga75j3jx8NsrZiOkWx6xGwvFgw8yugvQZgLvA2dR2JaRLjMYswHeMfPYetZO7nIFV0_eOcAY9wNvwzp2gZ1E51rezBq1rpSeMxLd9iXHd1zNGIAYPuC7VTNjFIvAe4kf_FdFQJTy8AesXQfmMtj8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346a1329e1.mp4?token=WI7lF2-UQPQCYx6faWCRgINAMYhEJMTq43Rp8HX4YlGVd-YEdhN_0XXF66Bz6hLWne3Ccg29Uam-V8EeOzWkrY7llRWhu9CyG1PcB30BACqSX1E5znCdm30aSMV3iJSBODftPwV2HN5r3m9pzsdhrHALR65I3quMeFfDOr9HIn3RmpCQPlUgG4kCMKJWTrFdaga75j3jx8NsrZiOkWx6xGwvFgw8yugvQZgLvA2dR2JaRLjMYswHeMfPYetZO7nIFV0_eOcAY9wNvwzp2gZ1E51rezBq1rpSeMxLd9iXHd1zNGIAYPuC7VTNjFIvAe4kf_FdFQJTy8AesXQfmMtj8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیگر از بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134159" target="_blank">📅 21:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134158">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk_0dklz_0ztfnjNiPr4PzohUk9K_zHkOl-EpvPh0CqH4MFJw0tGPwTpWok2GjpZT3Ldw58XFlF2AUQ9AITv1DMxetSvDS1MWrO6hwlBvcu1MV44RjSAtucg9aufY521hbNc9q01ZlJ69wAuccyCh-_wycpgMjI9hk5qNJHPU4tw0rjH2BrCRkXkFMOmd0k2hu34g4DhR0a1BSWLjwzlfmjsOU8LG4gGdihxG8b2TW-K5lIi2Vcv8-IWHKUuODt4lLHwB3OSNFFT-sPvXoId8iV0gIxoWeHsk7MU-g7YyoaeIaWBDlF4FJFVK93ggX6KW-u55QHH36aZnRSe2l2VTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظاتی پیش بحرین
!
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134158" target="_blank">📅 21:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134157">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
انفجار های سنگین و متعدد در بحرین و کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134157" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134156">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134156" target="_blank">📅 20:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134155">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6605e1c2ed.mp4?token=Hw4KeWjToYwRnt0yNcdrOUh396A78TEjn2kbDuoX48Q314LDGJ96BD69bgIuBZHns9gWIqk6bC5NZjHESKtET5hjv9wfj5RGDUGGHp44BvLlCdfo_9VnR3nrOvl1rZAGO6f1WpHPcG9EhqsVGG98jF--ifKpfP30w9VFZSGKrrxSCl7M6G_fOwFJZeL5KEHpg27J-UFLA4bC9Zl3E4WSGwgMTpQpvkdY6pPpOxcYKXyvyYw5QTWCHc0wj5-InxPeRvSe4RePjq0pxx8QYW-o3Lhpv3XEa92IP0AZExFpiuFnNomF3VB7mCsEZbEqYJ_9j3I7PojWXCMM48slWd4uVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6605e1c2ed.mp4?token=Hw4KeWjToYwRnt0yNcdrOUh396A78TEjn2kbDuoX48Q314LDGJ96BD69bgIuBZHns9gWIqk6bC5NZjHESKtET5hjv9wfj5RGDUGGHp44BvLlCdfo_9VnR3nrOvl1rZAGO6f1WpHPcG9EhqsVGG98jF--ifKpfP30w9VFZSGKrrxSCl7M6G_fOwFJZeL5KEHpg27J-UFLA4bC9Zl3E4WSGwgMTpQpvkdY6pPpOxcYKXyvyYw5QTWCHc0wj5-InxPeRvSe4RePjq0pxx8QYW-o3Lhpv3XEa92IP0AZExFpiuFnNomF3VB7mCsEZbEqYJ_9j3I7PojWXCMM48slWd4uVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تخریب ساختمان مخابراتی بندرعباس درپی حملات آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134155" target="_blank">📅 20:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134154">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
جنگنده‌های نیروی هوایی پادشاهی بحرین و نیروی هوایی ایالات متحده برای مقابله با پهپادها در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134154" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134153">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=kR1OG-aVEVpyCLQh3kajgLB_8UmfTIjIaNkDTIkChWGdSOiATVp4ynbKg7PBEcISaiBp0EhHukufskOWjM3U9oZerzz21dQJI-TcaVs1UVYWi5pFKUFsJqMdskLmREqJlzVUBnzz3tsgdlugQLXFwAzHHsjnXhNM_6Q0jgFWk_EvKsKE2Alic0sNkwJFhpW3Ex7XpUaeGWFLkgm_15zz28KO-2ujYZCASNmIffsnRxX9usoxspcENCKDIAjJ6kzUE6Tk44HbvA7tN-P01yxSq0P6hVmt-debe4T16qjzEyXVrWBHixTDyE2LBU7NbTNPj45fzZHrIyhw0vGPAj3Jrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=kR1OG-aVEVpyCLQh3kajgLB_8UmfTIjIaNkDTIkChWGdSOiATVp4ynbKg7PBEcISaiBp0EhHukufskOWjM3U9oZerzz21dQJI-TcaVs1UVYWi5pFKUFsJqMdskLmREqJlzVUBnzz3tsgdlugQLXFwAzHHsjnXhNM_6Q0jgFWk_EvKsKE2Alic0sNkwJFhpW3Ex7XpUaeGWFLkgm_15zz28KO-2ujYZCASNmIffsnRxX9usoxspcENCKDIAjJ6kzUE6Tk44HbvA7tN-P01yxSq0P6hVmt-debe4T16qjzEyXVrWBHixTDyE2LBU7NbTNPj45fzZHrIyhw0vGPAj3Jrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: لفاظی‌های ترامپ را در عمل جواب می‌دهیم و از وجب‌به‌وجب خاکمان دفاع خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134153" target="_blank">📅 20:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134152">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afTfrXZu0pKhtSLSRvLYu7gGr6-6BNHM1v1R64hazICgWQCTf1tCSTAzGMthX89bQkC3yZeiYNFwdpVgahi9bTXZmu1J5f3IhdONFoVNL6j6d4-iXUmT7-pTE5aneeoH37fcRr0FpBNBvq2Kf1Id-ZrKeUXgLThGQey8FYys-bF0njMtUQzajJRIF-rmYUh3pxxYR2x5TLUgtOrcFkrnjH4AOkQ-1sc2RWD9VMtMv4bT61ol5tYtfq-xuGYWfP0JrC5SccAzZZ8Q12GuGk9DLbKPFC9l02f6UDzy-ffzgmJZlUQduFCP-YxN02okkvkoru8I0XqJPLM7cXiTEt6bnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: دموکرات‌های مجلس نمایندگان آمریکا بر سر توقف کمک‌های آمریکا به اسرائیل دچار اختلاف شده‌اند، در حالی که انتقادات داخل حزب از سیاست‌های دولت نتانیاهو افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134152" target="_blank">📅 20:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134151">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / انفجار شدید در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134151" target="_blank">📅 20:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134150">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رسانه‌های عبری: فرودگاه‌ بن‌گوریون به حدی از سوخت‌رسان پر شده که ممکن است باعث لغو یا اختلال هزاران بلیت هواپیمای غیرنظامی شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134150" target="_blank">📅 20:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134149">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی و اسرائیلی مدعی شد: ترامپ از نتانیاهو خواسته نیروهای اسرائیلی را از سوریه و لبنان خارج کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134149" target="_blank">📅 20:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134148">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a553552bd.mp4?token=hX63q5X9z5rFjJbQuIOyzH7XAfB7sIomWNF6YDgXnqK6uvkf7WovpPx1fQC9MQ_3D7w0f5Cis_VNYcQF-fg8WWoV2ueXovXuTTdqHS5Q4On_C5lsC8H1elonG2AQTIpxAbyzSo1-tSP_xDCbCMueSB1LKAgro0RD6yx1dtQP9fKwxTipR6ARvyqdeRwCNAfTu3DFBXqL06U0cL1YjdAJiEshayjHd5Gd1TayuemkmFLyYe15Yy_d54uQYK2nCmTPTQoFMnKjBEaJ2zRfL4-645d4P-q0S62q38a93-POESBsd6K-1H2YI4k4BtvzD3NEbBdZZBJhXVy3yuR0_-8ygL_ryS-WcKJD-XVe08v0hfcQ0-cpzjg6kdTxwsAbk33ESO8cTX__VfZCRfUnMHf2SiphKswXTxd4_6-a5lcuN5m3ACeW2Gm7vMfzfMgpmMmjKuBx4AmgYDtzxdB2GhjyZIvCoW3teLm3x6Tb_6RwNkWBa3YQHJj0S1J4O1KpKzhQEj9fp1Ooi39n_jxi8RRBFq899jQz6LevrmxJkYExE5MW0G-OfvfW9TodNfaMYkM3u1Y2_X-RA2z6DGWBkYPN-0NKeED8XwKrIJrjCLnI0eWvnWj2VH7jPWF9mWPT6h1PD89QeMhMgYW75JWxTPoBP-VcsNv9WDTbiaX_QIeMRIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a553552bd.mp4?token=hX63q5X9z5rFjJbQuIOyzH7XAfB7sIomWNF6YDgXnqK6uvkf7WovpPx1fQC9MQ_3D7w0f5Cis_VNYcQF-fg8WWoV2ueXovXuTTdqHS5Q4On_C5lsC8H1elonG2AQTIpxAbyzSo1-tSP_xDCbCMueSB1LKAgro0RD6yx1dtQP9fKwxTipR6ARvyqdeRwCNAfTu3DFBXqL06U0cL1YjdAJiEshayjHd5Gd1TayuemkmFLyYe15Yy_d54uQYK2nCmTPTQoFMnKjBEaJ2zRfL4-645d4P-q0S62q38a93-POESBsd6K-1H2YI4k4BtvzD3NEbBdZZBJhXVy3yuR0_-8ygL_ryS-WcKJD-XVe08v0hfcQ0-cpzjg6kdTxwsAbk33ESO8cTX__VfZCRfUnMHf2SiphKswXTxd4_6-a5lcuN5m3ACeW2Gm7vMfzfMgpmMmjKuBx4AmgYDtzxdB2GhjyZIvCoW3teLm3x6Tb_6RwNkWBa3YQHJj0S1J4O1KpKzhQEj9fp1Ooi39n_jxi8RRBFq899jQz6LevrmxJkYExE5MW0G-OfvfW9TodNfaMYkM3u1Y2_X-RA2z6DGWBkYPN-0NKeED8XwKrIJrjCLnI0eWvnWj2VH7jPWF9mWPT6h1PD89QeMhMgYW75JWxTPoBP-VcsNv9WDTbiaX_QIeMRIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای پهپادی اوکراین، مجموعه‌ای را منتشر کردند که حملات پهپادی به ۱۱۶ کشتی روسی در دریای آزوف و دریای سیاه را بین ۶ تا ۱۴ ژوئیه نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134148" target="_blank">📅 20:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134147">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
صدای انفجار مجدد در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134147" target="_blank">📅 20:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134146">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9yeHR4CnotwPH4Zf9ldhGeuPE7eZcvQlOp6eQqznN5ewIhiKbpcO59FkWDpvXfGjMwHVeHSWvauR4o2BCu9bKTUn5_rGtqX3j3K1sDeXtTRq1VX5uPQIeFmRwYVNz5tjjsPFn97jQWQIdsbjT0yn2K-Q3L1SiSjVJKf4g5V82sZuNA38lUUIkIjKfauG2IsaisQXy32Y88m4qUrNi6Z6tE6feVCyIo-EbQd1-_t-82wucBn_Zbhyvu405DzX-eQlCItK1uwxrfjyZtYy2HGy8YHT-fPRw8zpLPOK-Nd_p_wZGRiQURUDz57to6WhKFpkBvQu3XcIRd2YYtYD4Un2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روسیه هفته گذشته یک تمرین نظامی با شلیک گلوله در دریاچه پیپوس، نزدیک مرز شرقی استونی، برگزار کرد. این اولین تمرین نظامی از این نوع در این دریاچه بود. مقامات استونیایی اعلام کردند که روسیه هیچگونه اطلاع‌رسانی قبلی در مورد این تمرین ارائه نداد.
🔴
هاننو پِووکور، وزیر دفاع استونی، این تمرین را بی‌سابقه خواند و احتمال داد که نیروهای روسی احتمالاً در حال تمرین برای رهگیری پهپادهای دریایی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/134146" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134145">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ارتش کویت:نیروهای مسلح در حال مقابله با حملات هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134145" target="_blank">📅 20:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134143">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLqoPkfNI8vCV58hMS_BD3EWa5k_GocxqKRwI3Z8Di0CBCZdad7kRE7DDUOOZNGgqJbrd2l1Sjlgz2BRPSLo-b4C7XDgF-ouQWgfrqbtS2KoXRtd8RhnIK0qHLJQfGKiWsacwv-DS26mIWamO2dwgcVaHUGKjm_9gYAJAFpstAEzYnQBbMQS5zoKBG2hNniTqJm0dW-fUHSbmD5_2LhhAC2o2cW-P7zonoAwhRF036NhSk3igx_98aG-YrQkZG2MCQt4cjzBNMq12LrmH8wVOJB6oznQMUeQCbgPIhjceUneH_Np0UpSRSwGLoDQgsGKTU884Qvh_DwkAQ3zVSd59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYVjjPvML84QoyJZmJB-1Rmxl8HUCiHadIVP2Jkngjlx8n77nM0OUGumQX4OyAmGF8lftlHsQmOmjDgoBn-HE0vPHvqF4ss_dgbQ4xhqDE3Elevi8-0v1p-IeVmwyf16Op7AfbaPsC44lUrQL7UEeFCTY45saRsN0ZcxsGe9Wp9dDhHmzvU-tbKqqQTHYGmSR60FJoE8M9inOu0WzujIMWRWKSZEBVwkTa-5M3pPg65ZWx_LB42gd4Gfs4dUZ7MfB90NNz8uPat_GEfXRkCSbL3FnVhH72acII4y5N_r5TyLn2qhQrzjuOt3-CUv0ljXl0nec0kUYtmqhfCoGA7Dug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون پدافند کویت درحال فعالیت شدیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134143" target="_blank">📅 20:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134142">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ:  فکر می‌کنم بغداد و من قرار است با هم موسیقی فوق‌العاده‌ای بسازیم، قرار است نفت زیادی استخراج کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134142" target="_blank">📅 20:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134141">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ادعای برخی منابع: درگیری شدید در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134141" target="_blank">📅 20:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134140">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
آتش‌نشانی: دود شرق تهران ناشی از آتش‌سوزی یک منزل قدیمی در خیابان دماوند است
🔴
درباره دود مشاهده‌شده در شرق تهران اظهار کرد: دودی که در بخش‌هایی از شرق پایتخت مشاهده شده، مربوط به آتش‌سوزی یک منزل قدیمی در محدوده خیابان دماوند است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134140" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134139">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
حزب الله عراق: در صورت جنگ علیه ایران، مشارکت نیروهای مقاومت فوری خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/134139" target="_blank">📅 20:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134138">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3a89e89b.mp4?token=dLv663SoWy9I5Arm7XwAnqVieLa3yxDa_yy4v-77lytexqSN-xaj7l7R21e0HK1sc6SgBczpF_cUkpLx6ZzaiuChz8e4J93lS35zJ_cbNeK97WgT4nErETVxG9FP9mILyeTO79rnsf2rv_t8dmQqwyiwGEi4brhOpyb5r_6H1uceI4Ijkh2hFu2E8N5GtiI91lC1xdlTA_qMHpUZaYWupzWqcbzfK4fLP4CptsoaUNCZkfzk7UZci-J9t4u9ZjAyhj8k1dCM6L2GG0gWDWXdqJk_OAd_7KAIdEadyByJWlplnzRCtPVikHIAiNV174jpqcHbPTpQkJKG4zxsFn-uUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3a89e89b.mp4?token=dLv663SoWy9I5Arm7XwAnqVieLa3yxDa_yy4v-77lytexqSN-xaj7l7R21e0HK1sc6SgBczpF_cUkpLx6ZzaiuChz8e4J93lS35zJ_cbNeK97WgT4nErETVxG9FP9mILyeTO79rnsf2rv_t8dmQqwyiwGEi4brhOpyb5r_6H1uceI4Ijkh2hFu2E8N5GtiI91lC1xdlTA_qMHpUZaYWupzWqcbzfK4fLP4CptsoaUNCZkfzk7UZci-J9t4u9ZjAyhj8k1dCM6L2GG0gWDWXdqJk_OAd_7KAIdEadyByJWlplnzRCtPVikHIAiNV174jpqcHbPTpQkJKG4zxsFn-uUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره نخست‌وزیر عراق، ال‌زیدی: ما قصد داریم روابط بلندمدتی با عراق داشته باشیم. ما قصد داریم روابط بلندمدتی با مردی داشته باشیم که یک رهبر بزرگ خواهد بود. به حرف من توجه کنید.
🔴
من می‌دانستم که چه کاری انجام می‌دهم. این مرد قرار است یک رهبر بزرگ در خاورمیانه، فراتر از عراق، باشد.
🔴
نفوذ او در سراسر خاورمیانه گسترش خواهد یافت و ما از این موضوع بسیار خوشحالیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134138" target="_blank">📅 20:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134137">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e38a8a0c7.mp4?token=AghzeIjYPIPYqMRdXFUhqbVZKPD2IwVzLPvd5L3SxM_AHlVif5Ft_ZXCeBEj1C98CtYEwbg87meJXWIx2_sakhBzt--2h4qEkK9R3_8_uztyQmgeK8-9Djka11ZsTKEdkGI724qaEJfZjhOND-W0hwywqfxJ-31XjvNlRYo7lqYB5tf7rc-BP5rb4o9JSda-PEWHKy2DR4FDEvD24QaUmzTUTPWylF-PNJDjsBPSOWmRW8WY72EH2BTO3p2pDLVJtcHPKio4jgS3w9hvj8Gy-U772C0HQpa1puS1qMlWx3L9bdt8vv7rG3bLccbPBgdX0sRaaVPuLlo2EtgsAS05mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e38a8a0c7.mp4?token=AghzeIjYPIPYqMRdXFUhqbVZKPD2IwVzLPvd5L3SxM_AHlVif5Ft_ZXCeBEj1C98CtYEwbg87meJXWIx2_sakhBzt--2h4qEkK9R3_8_uztyQmgeK8-9Djka11ZsTKEdkGI724qaEJfZjhOND-W0hwywqfxJ-31XjvNlRYo7lqYB5tf7rc-BP5rb4o9JSda-PEWHKy2DR4FDEvD24QaUmzTUTPWylF-PNJDjsBPSOWmRW8WY72EH2BTO3p2pDLVJtcHPKio4jgS3w9hvj8Gy-U772C0HQpa1puS1qMlWx3L9bdt8vv7rG3bLccbPBgdX0sRaaVPuLlo2EtgsAS05mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد اجلاس آنکارا سازمان پیمان آتلانتیک شمالی (ناتو): این اجلاس فوق‌العاده بود. راستش را بخواهید، یک جشن دوستی بود.
🔴
آنها آمریکا را دوست داشتند. حتی من را هم دوست دارند، اما بیشتر از همه، آمریکا را دوست دارند.
🔴
این اجلاس بسیار شگفت‌انگیز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134137" target="_blank">📅 20:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134136">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17915cf19.mp4?token=tKR-czQnqwQhLDh-7kj3uiofayvZZ7NdVDdVgUnpAsBk1k1SOY_TlK6qJQVn617DfMUTqHa4A0WS9-rL9uiOk4OKQiWIuyiuwHlHLbP59DXTozDK8OOn-QStsHFuz0MX6VIjAmAquKKt1l4mR4Y-fm1TWjWEEHi9mXYChN9Gkdr4Fs0FCsqwMvb5heAYDwRZ5SzI1hqJv6J9P1-skQ6aUFJhihYruGwXU9O5utp1UXMjQnPTUBegHBZ1qet67-MFFh-X91bv5GEjg3_lCqW67k9a7CCiPEv0YHtXFIpibxxHIK0vfevq0HBtarZ_ZWj-ruDWK7pWM0OThaVTFWWEyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17915cf19.mp4?token=tKR-czQnqwQhLDh-7kj3uiofayvZZ7NdVDdVgUnpAsBk1k1SOY_TlK6qJQVn617DfMUTqHa4A0WS9-rL9uiOk4OKQiWIuyiuwHlHLbP59DXTozDK8OOn-QStsHFuz0MX6VIjAmAquKKt1l4mR4Y-fm1TWjWEEHi9mXYChN9Gkdr4Fs0FCsqwMvb5heAYDwRZ5SzI1hqJv6J9P1-skQ6aUFJhihYruGwXU9O5utp1UXMjQnPTUBegHBZ1qet67-MFFh-X91bv5GEjg3_lCqW67k9a7CCiPEv0YHtXFIpibxxHIK0vfevq0HBtarZ_ZWj-ruDWK7pWM0OThaVTFWWEyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به نظر من، و باور کنید یا نه، خاورمیانه در حال متحد شدن است. ما در حال از بین بردن زورگوی خاورمیانه هستیم.
🔴
ایران، زورگوی خاورمیانه بود. آن‌ها عراق را تحت فشار قرار دادند. آن‌ها با هر کشوری به همین شکل رفتار می‌کردند. در سراسر خاورمیانه، ترس وجود داشت.
🔴
دیگر ترسی وجود ندارد، زیرا توان نظامی ایران به شدت تضعیف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134136" target="_blank">📅 20:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134135">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره نخست‌وزیر عراق، ال‌زیدی: حتی من درخواست برگزاری یک ناهار را دادم، در حالی که این موضوع در برنامه نبود.
🔴
به نظر من، من قبلاً هرگز این کار را نکرده‌ام که بدون برگزاری ناهار، بگویم: «بیایید ناهار بخوریم.» می‌دانید دلیلش چیست؟ چون من از او خوشم می‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134135" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134134">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: اوضاع در مورد خلع سلاح گروه‌ها در عراق خوب پیش می‌رود
🔴
ترس از ایران در منطقه وجود داشت و اکنون کشورهای خاورمیانه از شر یک موجودیت هژمونیک خلاص شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/134134" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134133">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996bdd34c5.mp4?token=CBlInm-9k_LGQ_BcGlHZAAgqWsnWHGWG-5XXqqRXFjLO2ic-I-9R60sBJvUS4zbs2TA318v1BsFFc09WRcwHLqzOZKJ3_IKQyd_bVjzjMnKrRzMjk1-Uj4EVl-RJqqAelLi21o5XBu_ltlYB_XcWII8pgVt8XJIvVkOvBXA16UM6v-qoIbMkt28reiBCU_mf6aWyY8O8wctyxyL86N7VmXke9wceSa6udhI6294TWqgb9_uU1ZzN_E0llwJsfpvxaSkC6kKGtbebt4Bnbi2eRG5VCrgofv4xcj1V5AJWs8gtLt_L9xdMKjeUDrFr2QPm3T3jNSZkTlxL6yORS-Y9TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996bdd34c5.mp4?token=CBlInm-9k_LGQ_BcGlHZAAgqWsnWHGWG-5XXqqRXFjLO2ic-I-9R60sBJvUS4zbs2TA318v1BsFFc09WRcwHLqzOZKJ3_IKQyd_bVjzjMnKrRzMjk1-Uj4EVl-RJqqAelLi21o5XBu_ltlYB_XcWII8pgVt8XJIvVkOvBXA16UM6v-qoIbMkt28reiBCU_mf6aWyY8O8wctyxyL86N7VmXke9wceSa6udhI6294TWqgb9_uU1ZzN_E0llwJsfpvxaSkC6kKGtbebt4Bnbi2eRG5VCrgofv4xcj1V5AJWs8gtLt_L9xdMKjeUDrFr2QPm3T3jNSZkTlxL6yORS-Y9TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد سخنرانی پیش‌رو خود در روز پنج‌شنبه: آنچه قرار است در مورد آن در روز پنج‌شنبه صحبت کنیم—بزرگتر از این نمی‌شود، زیرا بدون انتخابات آزاد و منصفانه، شما کشوری ندارید.
🔴
ما در مورد سایر موارد نیز صحبت خواهیم کرد، اما قرار است اعلامیه بسیار بزرگی باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134133" target="_blank">📅 19:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134132">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
در حدود (۱۹:۵۰ به وقت تهران) صدای انفجاری از نیروگاه مسن و قشم شنیده شد و در حال حاضر قطعی برق جزئی در شهر قشم وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134132" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134131">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: شاید آقای بایدن فردی آرام بودند، اما خدای من، او می‌توانست تورم را به گونه‌ای ایجاد کند که هیچ کس دیگر نمی‌توانست.
🔴
ما بدترین تورم را در تاریخ کشورمان تجربه کردیم. تورم به شدت کاهش یافته است. این بدان معناست که قیمت‌ها به طور چشمگیری پایین می‌آیند.
🔴
فکر می‌کنم ایران و حزب‌الله نیز به طرح قانون تحریم‌ها علیه روسیه اضافه خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/134131" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134130">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ درباره عراق: عراق به دلیل منابع نفتی خود، پتانسیل فوق‌العاده‌ای دارد.
🔴
ما قراردادهای زیادی منعقد خواهیم کرد. ما مقدار زیادی نفت استخراج خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134130" target="_blank">📅 19:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134129">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead5bf33bf.mp4?token=U287BTXFFZN9TGjqkU8tWpL3Ko0c2nrnT9_rqOD-2MTcEmTmJytaiT-7P7aaVpfZmFW5bAUxZ8ze3Ln8kVnQWy_1OQOo6U2YMfqZOD8WkzY6gwqzYBk16WaVb43HDUOItgT3aNTJ6S4-EYdsANYfKyOh0okS1WahJ9_nYy2Z1oKY4S9cnkgLmLmE1e6ocmXkBoehCStkz-bLsvanTWHKCS47YFK-CEsw1bZL74uOWDcT8fyDbZKApiNzRmMkPGDGUBaezKhcb3hphN5_MuREgy3UElVsZbhdAvPj8XiNrsRX1UjJM16_sUfbHJbigXryCwO-CLv9huDcewftaBPo1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead5bf33bf.mp4?token=U287BTXFFZN9TGjqkU8tWpL3Ko0c2nrnT9_rqOD-2MTcEmTmJytaiT-7P7aaVpfZmFW5bAUxZ8ze3Ln8kVnQWy_1OQOo6U2YMfqZOD8WkzY6gwqzYBk16WaVb43HDUOItgT3aNTJ6S4-EYdsANYfKyOh0okS1WahJ9_nYy2Z1oKY4S9cnkgLmLmE1e6ocmXkBoehCStkz-bLsvanTWHKCS47YFK-CEsw1bZL74uOWDcT8fyDbZKApiNzRmMkPGDGUBaezKhcb3hphN5_MuREgy3UElVsZbhdAvPj8XiNrsRX1UjJM16_sUfbHJbigXryCwO-CLv9huDcewftaBPo1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره ایران:
سلیمانی یک نابغه دیوانه، یا احتمالاً یک دیوانه بود. او کنترل کاملی بر ایران داشت.
🔴
رهبران ایران از سلیمانی می‌ترسیدند، اما من او را به قتل رساندم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134129" target="_blank">📅 19:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134128">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: از لغو محاصره دریایی یا اعطای معافیت‌های تحریمی به ایران پشیمان نیستم؛ من به آنها فرصت دادم تا به توافق برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134128" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134127">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: من دانشجوی بخش زیادی از تاریخ هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134127" target="_blank">📅 19:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134126">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5f8cdc26.mp4?token=WvlKJTRwQ3DZgtenCAQVueU1RVvvlUr4MarxgNTnFjYCX37Uzhv-YJZQftiAwZrU0RWaDTmq86izHx7LYyCicrOB6gtxcS678vvcpAODaece1-ZUf3Nl2IitrJ7kLvXli-0v3FsmNydjtoB3p4_SZo-oTYV0ELRV-gOdEYoYxDQAkdvo7JNKgx9eYy0m2VyKrD3NBy0MuD3HuQQ2-SYeegYr5jkArgX2-bsud3oTlFCAqjtHWNtvTQD4f1FBA3UqGq_FqG7H6vRMm3s2DHlNJuIH5BscZ2TnHMuhAovRGcJfZgjU6gHRZ5XoHvUvxZKUn6IXAeHV0qXKOxpzxZ8qaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5f8cdc26.mp4?token=WvlKJTRwQ3DZgtenCAQVueU1RVvvlUr4MarxgNTnFjYCX37Uzhv-YJZQftiAwZrU0RWaDTmq86izHx7LYyCicrOB6gtxcS678vvcpAODaece1-ZUf3Nl2IitrJ7kLvXli-0v3FsmNydjtoB3p4_SZo-oTYV0ELRV-gOdEYoYxDQAkdvo7JNKgx9eYy0m2VyKrD3NBy0MuD3HuQQ2-SYeegYr5jkArgX2-bsud3oTlFCAqjtHWNtvTQD4f1FBA3UqGq_FqG7H6vRMm3s2DHlNJuIH5BscZ2TnHMuhAovRGcJfZgjU6gHRZ5XoHvUvxZKUn6IXAeHV0qXKOxpzxZ8qaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موج جدید حملات موشکی ایران به کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134126" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134125">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها بودند که اولین گلوله را شلیک کردند و ما به آن‌ها پاسخ دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134125" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134124">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9826daa30b.mp4?token=GIfiSc6ukadTG6-lLwzQIjj7sQimT2TS9wBgChRyfk0y2R5XmKZu_6uf_Uf-3x-S-HSFOnX9Aim1V3kDLG3Y_kS9BPi7IJ-krNZgq4Wvn18_zIKV-sBR1vrwse4jXwEk4ecQa9PhGJ5YrXqPW4FMUo78crUo0M6c0_cejHYFDlap5PiqcMqC57DCJeUnFAr5sYzwwgjwNEzZu-fGfwJbeTUXKTQlHLP39Ggl2SlRLS8WSVe0mC-EWj4_-rvP--th7EITnKYikvnw9Z7q5seGjuA3nIvJCHAPd9aqnWpEpjDJ9KfTR6-wy5FmujKBWDMc5jqTstkg54O1mLMYBspntw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9826daa30b.mp4?token=GIfiSc6ukadTG6-lLwzQIjj7sQimT2TS9wBgChRyfk0y2R5XmKZu_6uf_Uf-3x-S-HSFOnX9Aim1V3kDLG3Y_kS9BPi7IJ-krNZgq4Wvn18_zIKV-sBR1vrwse4jXwEk4ecQa9PhGJ5YrXqPW4FMUo78crUo0M6c0_cejHYFDlap5PiqcMqC57DCJeUnFAr5sYzwwgjwNEzZu-fGfwJbeTUXKTQlHLP39Ggl2SlRLS8WSVe0mC-EWj4_-rvP--th7EITnKYikvnw9Z7q5seGjuA3nIvJCHAPd9aqnWpEpjDJ9KfTR6-wy5FmujKBWDMc5jqTstkg54O1mLMYBspntw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بوش و چنی: من همیشه می‌گفتم به عراق نروید، به عراق حمله نکنید.
🔴
صادقانه بگویم، آن‌ها به کشور اشتباهی حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/134124" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134123">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ درباره فوت سناتور لیندسی گراهام: امیدوار بودم که او بیشتر به سلامتی خود اهمیت می‌داد.
🔴
اما آنچه اتفاق افتاده، در واقع چیزی است که تشخیص آن بسیار دشوار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/134123" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134122">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e705c2c0.mp4?token=AKDK11dwLBkKEF60-xeHtrgxGNzLj2_QdtafuKC6-5zCPu8pWXP6md_z7v8_rahkU2IfFrgA7kyGKO72YTl4PLghhosjifShkgHmr3fWwMn5Gba1ltxsqV9RnudbVmTme9fhFiBdRBJjiHlnWYb6Pm7h09XJwOuN710-m0RMPO0SEvo4S1hYRiVVfdb00ZG9-l9gwzIn0lAYZEmh4bz0Nf9_knUPuBWg1okHyeC06J3_R96pTNwBMa_55OjRcHnVzktQKA53WtUKu1K-5WJTLI0AYACvV8KSds85PVZnf7G3P0eKWfrzi_Pq-gEInudyNRtCQlCE0cAQB1zUJiH12b8EWxlGUW3DFUjq-VrnrX1kcX98c8WEfPmm266hgDg_yyvfhzWdrpoRzZ4d1csPdck5yIsTT6fLdxiqciSmRZ_L4aSHrZBdrbTTxhzojWS8R5CsRugxQwU0O2pjlokiPhzHBU17S6xcNzcoArbL_IJCjJc1OwjEpVPz_2hMd52FZarKW3KL0skjJC4tbk0Ah4Pc8I3HhPSNa4s1HRbwXvBvCgbMj9bGbMmMi3KPE_Srk8Oo9CcGSzwd2pdV1RxH82576QgXTolqWQ3sR2hHopEfFIvAiupgLMlM1ajKiekmryoMbxEc80hoykdOleVgBgWaNDWfbg7oCxB9dM5iV48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e705c2c0.mp4?token=AKDK11dwLBkKEF60-xeHtrgxGNzLj2_QdtafuKC6-5zCPu8pWXP6md_z7v8_rahkU2IfFrgA7kyGKO72YTl4PLghhosjifShkgHmr3fWwMn5Gba1ltxsqV9RnudbVmTme9fhFiBdRBJjiHlnWYb6Pm7h09XJwOuN710-m0RMPO0SEvo4S1hYRiVVfdb00ZG9-l9gwzIn0lAYZEmh4bz0Nf9_knUPuBWg1okHyeC06J3_R96pTNwBMa_55OjRcHnVzktQKA53WtUKu1K-5WJTLI0AYACvV8KSds85PVZnf7G3P0eKWfrzi_Pq-gEInudyNRtCQlCE0cAQB1zUJiH12b8EWxlGUW3DFUjq-VrnrX1kcX98c8WEfPmm266hgDg_yyvfhzWdrpoRzZ4d1csPdck5yIsTT6fLdxiqciSmRZ_L4aSHrZBdrbTTxhzojWS8R5CsRugxQwU0O2pjlokiPhzHBU17S6xcNzcoArbL_IJCjJc1OwjEpVPz_2hMd52FZarKW3KL0skjJC4tbk0Ah4Pc8I3HhPSNa4s1HRbwXvBvCgbMj9bGbMmMi3KPE_Srk8Oo9CcGSzwd2pdV1RxH82576QgXTolqWQ3sR2hHopEfFIvAiupgLMlM1ajKiekmryoMbxEc80hoykdOleVgBgWaNDWfbg7oCxB9dM5iV48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره فوت سناتور لیندسی گراهام: امیدوار بودم که او بیشتر به سلامتی خود اهمیت می‌داد.
🔴
اما آنچه اتفاق افتاده، در واقع چیزی است که تشخیص آن بسیار دشوار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134122" target="_blank">📅 19:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134121">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری /  حملات جدید به کویت؛ صدای انفجارهای شدید و آژیر خطر به گوش می رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134121" target="_blank">📅 19:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134120">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
صداي انفجار در اندیمشک شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134120" target="_blank">📅 19:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134119">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
جنبش انصارالله اعلام کرد که صبح امروز، یک پهپاد شناسایی مدل Wing Loong II متعلق به نیروی هوایی سلطنتی عربستان سعودی را در آسمان استان البیضا، در جنوب غربی یمن، سرنگون کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/134119" target="_blank">📅 19:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134118">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ: اگر عراق به حفاظت نیاز داشته باشد، ما در کنار آن خواهیم بود.
🔴
کشورهای مختلفی با من تماس گرفتند و گفتند به‌جای دریافت عوارض برای عبور از تنگه هرمز، مایل‌اند در آمریکا سرمایه‌گذاری کنند
🔴
کشورهای حاشیه خلیج فارس قرار است [به جای پرداخت عوارض عبور در تنگه] در آمریکا سرمایه‌گذاری کنند و فکر می‌کنم این راه‌حل بهتری است.
🔴
فکر نمی‌کنم هیچ‌کس باید بتواند برای عبور از تنگه هرمز عوارض یا هزینه‌ای دریافت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/134118" target="_blank">📅 19:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134117">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: ما برای تأمین امنیت تنگه هرمز تلاش می‌کنیم و به نفت منطقه نیازی نداریم، به همین دلیل موضوع تعرفه‌های ۲۰ درصدی را مطرح کردم.
🔴
پس از تماس‌هایی از کشورهای منطقه در ازای سرمایه‌گذاری، از اعمال تعرفه بر ترانزیت از تنگه هرمز منصرف شدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134117" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134116">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca55b57e6e.mp4?token=lm0McLk98EIcWUpHuYhzrZsq1HrWLE9DafNLhljuhKJPY3sGWZDrXE9u7Dy06rPrMJd-8WiBh52VytIVlQQIk91ITtQ5GxP1Sfd3k-Uts41iyNNaPZbtC22cMTwB_DvsZe-w-2jRk-iIaeoCUywqPzv3guJq7W1DOPgdJvtm90buUxn9z8BXnb1wePRmUSEwlXSzuxfws_0-17oa0KpPZ2dOhwLLX-JUSOHYDJMg4HZ2_DjUjmAWN6SC1abLSQw_OO2qOcKSe8bdEhwtwvfYCbzmWUZOks8myBBPGyo08WfBhgKh2T1wINOq7HEc5scmfkXT6OqvpwW1zkZMfWqvbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca55b57e6e.mp4?token=lm0McLk98EIcWUpHuYhzrZsq1HrWLE9DafNLhljuhKJPY3sGWZDrXE9u7Dy06rPrMJd-8WiBh52VytIVlQQIk91ITtQ5GxP1Sfd3k-Uts41iyNNaPZbtC22cMTwB_DvsZe-w-2jRk-iIaeoCUywqPzv3guJq7W1DOPgdJvtm90buUxn9z8BXnb1wePRmUSEwlXSzuxfws_0-17oa0KpPZ2dOhwLLX-JUSOHYDJMg4HZ2_DjUjmAWN6SC1abLSQw_OO2qOcKSe8bdEhwtwvfYCbzmWUZOks8myBBPGyo08WfBhgKh2T1wINOq7HEc5scmfkXT6OqvpwW1zkZMfWqvbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد نخست‌وزیر عراق، العزیدی: او مرد جوانی است. او جوان و خوش‌تیپ است و من این را دوست ندارم. من از این موضوع خوشحال نیستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134116" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55016faa3.mp4?token=DDS7PUtP5OB0ZjgchnMtQ-MI09B5pE8g2YMhr81ACrvGBc3ALaZJUJTd_ItPjiBduWpv06sx5rhP-kUWw1K_aMRIDTM1HgtJ_AEFBnU2pQGzYg_pVU8Cy1EYHj-72xrHzyuoJf05FkBPh_fl5jI3cEXoQAwAz4Bsd7leCPmCmOuZ_-IQHtsn_gahQBPG_0WfhwM2yHWJj5PHCxC1x3HbxFOTpHbZMCB9wXR9cieqoPKpqE0OaUZPZYHJ-W6R-wILQnFEe1yAcD0V_HLJlrNeW00e8qokrIcohoXRYwQbU4FEDWiOeJkZHFSTb0yVZFsayGyD8-LeHhrdM4ehUCc4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55016faa3.mp4?token=DDS7PUtP5OB0ZjgchnMtQ-MI09B5pE8g2YMhr81ACrvGBc3ALaZJUJTd_ItPjiBduWpv06sx5rhP-kUWw1K_aMRIDTM1HgtJ_AEFBnU2pQGzYg_pVU8Cy1EYHj-72xrHzyuoJf05FkBPh_fl5jI3cEXoQAwAz4Bsd7leCPmCmOuZ_-IQHtsn_gahQBPG_0WfhwM2yHWJj5PHCxC1x3HbxFOTpHbZMCB9wXR9cieqoPKpqE0OaUZPZYHJ-W6R-wILQnFEe1yAcD0V_HLJlrNeW00e8qokrIcohoXRYwQbU4FEDWiOeJkZHFSTb0yVZFsayGyD8-LeHhrdM4ehUCc4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: قدرت نظامی ایران تنها بخش کوچکی از چهار ماه پیش است.
🔴
بنابراین عراق مشکل ایران را نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134115" target="_blank">📅 19:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134114">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: فکر نمی‌کنم به حضور نظامی در عراق نیاز داشته باشیم
🔴
ایران باری بر دوش عراق است زیرا قلدر کشورهای خاورمیانه است.
🔴
شرکت‌های نفتی در سطوح بی‌سابقه‌ای وارد عراق خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134114" target="_blank">📅 19:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134113">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: فکر نمی‌کنم به حضور نظامی در عراق نیاز داشته باشیم
🔴
ایران باری بر دوش عراق است زیرا قلدر کشورهای خاورمیانه است.
🔴
شرکت‌های نفتی در سطوح بی‌سابقه‌ای وارد عراق خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134113" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134112">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
صدای انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134112" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134111">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ایران اعلام کرد که زیرساخت‌های شرکت اسپیس‌اکس (SpaceX) متعلق به ایلان ماسک، هدف نظامی مشروعی محسوب می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/134111" target="_blank">📅 19:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134110">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9Y86jN_gQO29cZquWUKXuV3w3NlQhPldG0Cdh-yD-9LL3wvE_llOwJ_km5VpDsgFiYkBRCO0zcnyZj-TaDy1pi94rInkvmYdfwg6DB5NT1pJLDmftTlijG3yrogN0vWxRgk_j7CloaoFzeDdJj2rlIrw9vsE8wEi9XutaKmUf_8MIpIh4fOPNKkFXATddxoOHZlcrWlI0va4So6X1EdvfX6iPaCXeQpc3H9F96Cp522cua-VyVuOJ7H4R8dGd2vAlCFpDnheuHObDIhQ5mRE1L0mr7Y1AHHGWH86b5-MiH1PRJGBW1Kac6YLB5QTBJ46B88_2bjlTZf4PlpRmPnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134110" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134109">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ce5aae87.mp4?token=XhfIcvbYmqj9-AZ8YfySCDy5D2bu-XEl2Qu2aej0MWVDWu6T9wsJg9G6Y-QM1q2aHTFhFKX37oAzotP5B7NToHnGx7tkugH2tKGx3G4rKs4_Ay9SxcaUBq1ZggcMgpE_NbCpU3R_EZJm86p-hA5FottxMcm8IPrcwLFO6q47NP4FusyPx5g5J3aVLjBoS9xd4o8jcuDlRdAuhvRFO58rmz8UtZHXpVvpClv4dVVwpwk6jtO2OLX0nrGv5p_AbaRbjLAhuY4VGeLYR-53IiGhCaEWFsZviK3MXFEXUcIIxaI6BaXmsafBdE7R5HQWiZi1on4S1k9vMvxPPCdvyWKWZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ce5aae87.mp4?token=XhfIcvbYmqj9-AZ8YfySCDy5D2bu-XEl2Qu2aej0MWVDWu6T9wsJg9G6Y-QM1q2aHTFhFKX37oAzotP5B7NToHnGx7tkugH2tKGx3G4rKs4_Ay9SxcaUBq1ZggcMgpE_NbCpU3R_EZJm86p-hA5FottxMcm8IPrcwLFO6q47NP4FusyPx5g5J3aVLjBoS9xd4o8jcuDlRdAuhvRFO58rmz8UtZHXpVvpClv4dVVwpwk6jtO2OLX0nrGv5p_AbaRbjLAhuY4VGeLYR-53IiGhCaEWFsZviK3MXFEXUcIIxaI6BaXmsafBdE7R5HQWiZi1on4S1k9vMvxPPCdvyWKWZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستون‌های دود در کویت، نزدیک مرز عراق، مشاهده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134109" target="_blank">📅 19:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134108">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
شرکت آب و برق کیش :  قطعی‌های موقت برق اجتناب‌ناپذیره و بررسی‌ها برای تعمیرات داره انجام می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134108" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134107">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618a7045f0.mp4?token=HYY5URvMC_-mEN_vI7DX0p4YE4GSOKhEyRQc1SDooao_-mlch-e2r_xV6FGMJ8Q68RppU6RMLScl85vsOR2iGRct_NPvqH7niatAAkRSJYZRaTliGcnY7t23gblfQg1IjPVqDElEVxsXbGAkKh3DfJSIZPFxZ9d-qXTDydJg-6y4fpD1b31udtakAvlZ6U6ptcf4wA0F8m3-alFeb6OJBQ9QZdiPnej9v6zvGHN2NAHWAbQiOFqammxlT7n7ToIUop4XWMjs7E-JheUhTWoJshxwJHn0KwND5mThsf1TsLhevogxGFKBwi6gykZ5nAxL62aAHC2jruR8R2sn6VTXqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618a7045f0.mp4?token=HYY5URvMC_-mEN_vI7DX0p4YE4GSOKhEyRQc1SDooao_-mlch-e2r_xV6FGMJ8Q68RppU6RMLScl85vsOR2iGRct_NPvqH7niatAAkRSJYZRaTliGcnY7t23gblfQg1IjPVqDElEVxsXbGAkKh3DfJSIZPFxZ9d-qXTDydJg-6y4fpD1b31udtakAvlZ6U6ptcf4wA0F8m3-alFeb6OJBQ9QZdiPnej9v6zvGHN2NAHWAbQiOFqammxlT7n7ToIUop4XWMjs7E-JheUhTWoJshxwJHn0KwND5mThsf1TsLhevogxGFKBwi6gykZ5nAxL62aAHC2jruR8R2sn6VTXqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی الزیدی، نخست وزیر عراق که به واشنگتن سفر کرده، در کاخ سفید مورد استقبال ترامپ قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134107" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134106">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
صدای انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134106" target="_blank">📅 19:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری / اخبار تائید نشده از هدف قرار گرفتن یک نفتکش با پرچم لیبریا در سواحل عمان
🔴
منابع خبری گزارش دادند یک نفتکش تجاری با پرچم کشور لیبریا در نزدیکی سواحل عمان هدف یک حادثه امنیتی قرار گرفت که منجر به بروز حریق در این شناور شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134105" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بر اساس گزارش‌های رسانه‌های دولتی، شبکه ملی برق کوبا بار دیگر دچار قطعی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134104" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134103">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / انفجار در سفارت آمریکا در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134103" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134102">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری / ارتش کویت: درحال مقابله با موشک و پهباد های شلیک شده از طرف ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134102" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134101">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
فارس: صدای انفجار در قشم
🔴
صدای چند انفجار حوالی ساعت ۱۸:۴۵ در جزیره قشم شنیده شده است.
🔴
صدای دست کم ۵ انفجار در جزیرهٔ قشم حوالی ساعت ۱۸:۴۵ شنیده شد.
🔴
ماهیت انفجارها مشخص نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134101" target="_blank">📅 19:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134100">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnqIMcHUrmvWNo15xPCHBkLcvbWqCNFr_57528BHNpHnMbX8LOsghumeVU6Wpeqvt07ZDLlDkf7GNXOzaXXx3rQC9cPC-EdxORwp7W9P25EL345k4a-7qAfVuy4LyntUHcODfK-uI9xOuWaSvBbh7N-ZdGEtyIiNYtxgGH-Pn0bbrx2X_r1BwOhz24VVIAr_r3u5gGyVvzHc3dDjGwu4FZbKvtQ7GfXqPVMHITIT4SN7mQbEeDmPXik1Q2swNesj-QnTx3jVN0kvMtKqqqh1-ahiUoSAgMD6NOUCP-Z4kRSZh3Qn-usxx_LnP6fnDD8XjorKfzuThbtgXR3MjB_5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است.
🔴
امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند.
🔴
در کنار و قدردان این مردم وفادار و مقاوم هستم. ‌همه جای ایران، سرای من است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134100" target="_blank">📅 19:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134099">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / ارتش کویت: درحال مقابله با موشک و پهباد های شلیک شده از طرف ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134099" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134098">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imGQ3a6rtgQoeT2QqjiWC7HWt8V8YqqB-pL8H2rgAEFlAuFw8GrUSyEflmOlGLII6b7nzLmghr0bxQ_Fme2kRwWBcNmjFFXYGNmVxDSVNF_HgZdGqOKV9Hz7HZJJTBsCu68dK9jvqSowKGgrrJ-dME21z9vOwgi4dE3_5pt1Ho81I8O0sAaW0LvtRRzFAfZVPGe_Tbfp4uG2sXVVIHvRgzf_jHlSMBhK22KpPrPse-HUL5fbeBLs2bHgk0VefI2G1L8YXASahKCJkcMH4b2IIriGnZQSSB80S7EEG9SlVcKRvLjQsO16n6EV3nOJzG5e3xnX4yZwSWbfGlLTIiHguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: ما یک محاصره کامل خواهیم داشت، اما فقط بر روی کشتی‌هایی که به بنادر ایران می‌آیند و می‌روند، یا هر چیزی که مربوط به محمولهٔ ایرانی است را حمل می‌کنند.
🔴
همچنین تصمیم گرفته‌ام که هزینهٔ ۲۰ درصدی بازپرداخت ایالات متحده را با قراردادهای تجاری و سرمایه‌گذاری جایگزین کنم که کشورهای مختلف حوزهٔ خلیج [فارس] در ایالات متحده انجام خواهند داد. آن سرمایه‌گذاری‌ها بسیار کلان (عظیم) خواهند بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134098" target="_blank">📅 18:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134097">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
آسوشیتدپرس: تلاش میانجی‌ها برای ازسرگیری مذاکرات ایران و آمریکا
🔴
خبرگزاری آسوشیتدپرس به نقل از دو مقام منطقه‌ای گزارش داد که میانجی‌ها، به‌ویژه پاکستان، در تلاش هستند تا آتش‌بس را احیا کرده و ایران و آمریکا را بار دیگر به میز مذاکره بازگردانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134097" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134096">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: ما یک محاصره کامل خواهیم داشت، اما فقط بر روی کشتی‌هایی که به بنادر ایران می‌آیند و می‌روند، یا هر چیزی که مربوط به محمولهٔ ایرانی است را حمل می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134096" target="_blank">📅 18:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134095">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترکیه حکم بازداشت نتانیاهو را صادر کرد
🔴
به نوشته «ترکیه تودی»، این حکم موقت از سوی دادگاه عالی کیفری یازدهم استانبول و در چارچوب رسیدگی به پرونده مربوط به توقیف ناوگان صمود - که عازم غزه بود - صادر شد.
🔴
فهرست اتهامات علیه نخست‌وزیر اسرائیل شامل «جنایت علیه بشریت»، «نسل‌کشی»، «صدمه عمدی» و «شکنجه» است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/134095" target="_blank">📅 18:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134094">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf5t_VawLFw9RXNlg8SFvNkKXDIAZlJxlKz5SD7W-zQIDIW-D4xaQ9jN2W5m2OPDLPfamaxeGczQnTwIKA5BcjLZq3KXWMKr7631TW9piUqNTCCu0-BOH5u1dKzm1RsTPrpjF3ND_nQStvp_Phb4vfc911K-Bfi3jGmlGuyjpr1me4_pGreSj5pyBlD3xIyQ_k83KtW99qnRQh4rIOYqdaQFJdtv79RgrOXhl0RPTJP7VxJ3mLur9Eo2FkKVabNL5uUY11t0SUXK1t6IyaDqacmpc8gz_tz8nOKAzgMpNCcl7_wY8hpNdpbuuk00iXRq0lU8Z0MIwn_bWXAWomUbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه منتشر شده توسط آمریکا برای اعمال محاصره دریایی بر ایران
🔴
برخلاف محاصره قبلی که از سمت دریای عمان کنترل می‌شد، این محاصره جدید هوشمندتر و دقیق تر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134094" target="_blank">📅 18:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134093">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بمب‌افکن‌های بی-۵۲ آمریکایی در حال رفتن به سمت پایگاه دیگو گارسیا (پایگاهی که در جنگ ۱۲ روزه توسط بمب‌افکن‌های بی-۲ استفاده شده بودند) هستند.
🔴
امروز این بمب‌افکن‌ها در پایگاه Guam آمریکا در غرب اقیانوس آرام سوخت‌گیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134093" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134092">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORj5Q8P8PnwwgoHdwJ7BQyIYIv0Uhq3TpduDSJVu_aBTAGycPZSowNFttt6IoKEX7NUNsg1AOAoJrLq127M_1T-lkYP4yfYK8hKQuoRKohPt83y777aMo-KUWWSn1uGnIlyXQmDiar4Z89BR7CY6xr87zARopwu33-DynyvPKTV3Rj75wpgc_Cw067slN30TMTv8sT8U5Jg5A7vXy4w9f4A97L6v4D_iC_hX_cpRrDHYuACWqw4EW7yo0amQnIp4S0e61r8-yNPxUbRiB3_SO_u6yDjk365aLMfVzdLee_awDIfSUFaDVn8CA3mkDgjdUUHanPpAFH2Jn00XfniXFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
شاید باورتون نشه اما حدادعادل برای اینکه معادل فارسی کلمه کنسرو رو پیدا کنه 64میلیارد تومن بودجه گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/134092" target="_blank">📅 18:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134091">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_rzymoAC2rIYSRYmb41LrwbRyrN39gdEwnxVex1sk2RXB54Hy19oQbyrWIwmJQlnP-AmMM3aq4y-40ypxPf_bgALBT174iO60oJrYoFoxUBmUX29qPQ0mXN8dwO1MDXKjsiWWj1i3JJtixV9YpPJnXvRmJaHBjTpzM5AlAZtkSYLTnUR8GfqO8w2nNxC4MD8cfCndf-3zl8kyghyJ0C3sMRF5uduE6r-2aSrsnVu9QAPPEmnKJz9nc7EMFy1Vwmf6Gt1L0UoIM7YWOva-i9PQrSsSnQey3M62YJHxpELMBvZTffZk8SUbX-KKPReBzdzFJN0OVfRCmhYxRXX2zfGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ این پستو رو ریپست کرد:
"اشغال جزیره خارک!"
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134091" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134090">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd0bc9aa7.mp4?token=Gq1g4ycrP1d7xVJo1uMOeUvqGMWeYc0oUxBq5-OaKJpglZYAT0NMQDcMhllqNwRd9oBLRMWHSYuTSgSJU5PhnfrSyUcnfhqbL3T2EV_SOSPDJ36pYyiBYqSHyNQ_AKh-RtwIpr-ryCiYwbVOyLvUBXXOt9nz8wf7WuisdvMievBuYXYqRDqqATdfIpUlQA7OKEeUCknBW7XDvYmjNDBw1mIjXzhdwUn7zKMiFOudXYN9IesPxxrqlpXagMveo7DEX58eY7UT4JF2AnkPC02EAD4FR705ZTqbVlHO-5IYOMi82hH212-bMc_uSUgheNSP58z0xf0MkBjm4jPIwZVirA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd0bc9aa7.mp4?token=Gq1g4ycrP1d7xVJo1uMOeUvqGMWeYc0oUxBq5-OaKJpglZYAT0NMQDcMhllqNwRd9oBLRMWHSYuTSgSJU5PhnfrSyUcnfhqbL3T2EV_SOSPDJ36pYyiBYqSHyNQ_AKh-RtwIpr-ryCiYwbVOyLvUBXXOt9nz8wf7WuisdvMievBuYXYqRDqqATdfIpUlQA7OKEeUCknBW7XDvYmjNDBw1mIjXzhdwUn7zKMiFOudXYN9IesPxxrqlpXagMveo7DEX58eY7UT4JF2AnkPC02EAD4FR705ZTqbVlHO-5IYOMi82hH212-bMc_uSUgheNSP58z0xf0MkBjm4jPIwZVirA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل 20 فروند هواپیمای سوخت‌رسان آمریکایی در فرودگاه بن‌گوریون اسرائیل حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134090" target="_blank">📅 18:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134089">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAL5xBTz6swEGXEyL5MLrsVBzHkLh9E9KvkSNHVWWh8djHvfM7cvGuTn7b0-Ps1v_1Yk2MFjXihVc8m8L0-Pc7cpPdZHAa-IGpX1IJ2BLvCD3tm8MDEncHM9UzJ1fzcFhHCfYoytkrINfHy9hKUGl5OG8UXWhzB-vXmFVQ3h-yIErqKFalMtpnCh8-CQICnooQd-4rlsfemBHGos7rAMaUaZ7wSdqDu0xuryIuHnhtV9S1NPD1lWUGqaF5hI8A0jcSQi6zs9E_pbQZYlmf4tBvAH60y2VvIkVoCOIkd5lsL-CqGHAo5vki0NE5MEP3IfoFLD5PnZP1Th-6TP4DaGAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون ۵ فروند هواپیمای سوخت‌رسان نیروی هوایی آمریکا بر فراز منطقه خلیج فارس در حال عملیات هستند!
🔴
همچنین یک پهپاد MQ-4C Triton متعلق به نیروی دریایی آمریکا پس از تکمیل یک مأموریت شناسایی، مراقبت و جمع‌آوری اطلاعات (ISR) در سواحل ایران، در حال بازگشت به پایگاه هوایی پرنس حسن در اردن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134089" target="_blank">📅 17:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134088">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
توانیر: از فردا قطعی برق برنامه‌ریزی شده در شهر تهران آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/134088" target="_blank">📅 17:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134087">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ارتش ایالات متحده تصمیم گرفته تا بازگشت برنامه‌ریزی‌شده‌ی هواپیماهای سوخت‌رسان از فرودگاه بن گوریون را به دلیل تشدید تنش‌ها با ایران، به حالت تعلیق درآورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/134087" target="_blank">📅 17:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134086">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
آمریکا رسماً وارد جنگ با ایران شده است، دیگر یادداشت تفاهم نامه ای در کار نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/134086" target="_blank">📅 17:45 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
