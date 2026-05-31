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
<img src="https://cdn4.telesco.pe/file/oQliOaVH3QWR7vIbC25hx1AG6kcpCeBd15yOL1bYOaoyeVQdj24c7-TyLDpqHLruRgubFs5QlEg9ctvQLiIUE2Ey1YXw8GoszGTD536fnTtKece8cnKA3jbeA8dzxaDTffRx8uePGCaoDPLlCibfHDqXe7HFwx3oJGWaN9jZ4Zdu02t8tk349VaNsxlXpYZSehqYHEXu7bqasN8xlCPUwmcFP3_4Bp6OlkunXULNy_hB6OL2BhI_uWM56VU2lLxV3yGA3OHFmPFXHXCo2Qxjx-V5kSqphFAZHT4L4Es4XXVFEulScytPsnJidLvr9mOeXKKPRMMouBu0-NDEsw2T3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 179K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 13:13:25</div>
<hr>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یکم دیگه اعلام نهایی توافق و مذاکره طول بکشه از لبنان فقط اسم "سیب لبنانی" تو میوه فروشی های ایران باقی میمونه.
اسرائیل امروز لبنانو شخم زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/funhiphop/76445" target="_blank">📅 12:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مردی براي همسرش پیام داد   عزيزم تو چه كرده اي پيش خدا اينقدر عزيزي كه همسری همچون من بتو داده زن جواب داد نه نماز خواندم و نه روزه گرفتم و خدا از من انتقام گرفت:))
😂
😂
😂
😂
😂
😅
@FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/funhiphop/76444" target="_blank">📅 12:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مردی براي همسرش پیام داد
عزيزم تو چه كرده اي پيش خدا اينقدر عزيزي كه همسری همچون من بتو داده
زن جواب داد نه نماز خواندم و نه روزه گرفتم و خدا از من انتقام گرفت:))
😂
😂
😂
😂
😂
😅
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/76443" target="_blank">📅 12:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مطهرنیا:
واشنگتن به دنبال مدیریت ایران در دل یک نظم امنیتی و اقتصادی جدید است برای همین حذف کامل رژیم در دستور کار نیست
میفهمم چی میگیا ولی متوجه نمیشم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/76442" target="_blank">📅 11:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیوزسیتی پرو: با گذشت ده روز از خرداد، همچنان آمار رسمی تورم اردیبهشت 1405 منتشر نشده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/funhiphop/76441" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خاتمی جلو عادل اصول گراست
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/76440" target="_blank">📅 10:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76439">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آکسیوس: ترامپ همچنان به خطوط قرمز خود پایبند است و تاکید داره که هیچ توافقی با ایران امضا نمیشه مگه اینکه ایران تضمین مشخصی برای عدم دستیابی به جنگ افزار هسته ای بده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/funhiphop/76439" target="_blank">📅 10:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76438">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d2dea055.mp4?token=agh1jYB5NBG7-NJXVrJ16oF0ZhxmXIMYZmWYT4anjNJm0yY4hwWV5cNlal-70S4bZ7ZrLaenwyok_WrDhMOLF891QEZzXmePf1eEdzFOwjMSdaI2tcbGbZSIYsHFPWtzvdgaB-fIDgHo2_caWvO89bcZtlafVeDT0pPzgO-HLMnwxawhuVMARJd9yJ9cVP2XuehPhjOizE4WUegvgNEbjDQcb_iroYIqHEaoBAewH4CM_mx0uHpe5P_MJaPGFGs3ZUSze3G2ETx_BfVQlxDAUTyje4ct3x8j-mrW27Tm6G10rg91G31HaNV4TVJfHqnsnG450UqEBi65SXn0a6uSuGizDFVwuX1K4GFayt4r9TSNSAfS2sS9RD1DLnDSFbSSkdU1Fj0-uO3KB1U0n-VVFV0ikakJ8NLQKiHBdxvxVowJbwnGQ1huZkhtaOaJQfSByIhPsCHiSMuZhdZRO5s0abZqyIl2WVFkksuL4muu5ZUXvjXttDaJ6Wj2J9T1UfLhVHa6V2wmOTOdb5ZgdE5bFiTujQUagQ9pJvCCr9DpcrVRHQjB46GuSXShwqNlBCJlXGy6RsYchs1w37wR3fU_n6ECtYXF7cdRxcETDYAdeZv6AfkS4-YdUKWIJ2fuKriZYljQQ3qEEOVgC2EGbOmob6Jxdvf0j6zLjlirvr0r-o0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d2dea055.mp4?token=agh1jYB5NBG7-NJXVrJ16oF0ZhxmXIMYZmWYT4anjNJm0yY4hwWV5cNlal-70S4bZ7ZrLaenwyok_WrDhMOLF891QEZzXmePf1eEdzFOwjMSdaI2tcbGbZSIYsHFPWtzvdgaB-fIDgHo2_caWvO89bcZtlafVeDT0pPzgO-HLMnwxawhuVMARJd9yJ9cVP2XuehPhjOizE4WUegvgNEbjDQcb_iroYIqHEaoBAewH4CM_mx0uHpe5P_MJaPGFGs3ZUSze3G2ETx_BfVQlxDAUTyje4ct3x8j-mrW27Tm6G10rg91G31HaNV4TVJfHqnsnG450UqEBi65SXn0a6uSuGizDFVwuX1K4GFayt4r9TSNSAfS2sS9RD1DLnDSFbSSkdU1Fj0-uO3KB1U0n-VVFV0ikakJ8NLQKiHBdxvxVowJbwnGQ1huZkhtaOaJQfSByIhPsCHiSMuZhdZRO5s0abZqyIl2WVFkksuL4muu5ZUXvjXttDaJ6Wj2J9T1UfLhVHa6V2wmOTOdb5ZgdE5bFiTujQUagQ9pJvCCr9DpcrVRHQjB46GuSXShwqNlBCJlXGy6RsYchs1w37wR3fU_n6ECtYXF7cdRxcETDYAdeZv6AfkS4-YdUKWIJ2fuKriZYljQQ3qEEOVgC2EGbOmob6Jxdvf0j6zLjlirvr0r-o0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی زرنگی عادل جان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/funhiphop/76438" target="_blank">📅 09:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76437">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW5VvTbqyUk24B8bZ48JcmYomidYpgJarW_t1gQ6-v6hzwtpT5JV0BODMpgQeuUiNnzYtwS5ga7RxeuO-REsksgILjaflVqlqTc1czMHOQt21NyhhPUbK62lEnmOmV3Qa2KoJhd0YT2Ejbrenbjb7pKElXnTUQ1k9TJV2D3VDQ6gLRU-jiEJnlBD4oqgEt7Jd5DaHMGUgS3LGwO1VBduASIMwBupEP1vNCphg-cdjgu9vwysXZofy9iig1ofiy1rQiEpE3DN-VSC_WzqAGjDvUk-QXnubx3wUf4I37Bpt5REozxoSZFOApD9o7SZmjdEAf6XF3eqzknzpa1kNQezJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صب وسط بسکتبال داشتن همو میکردن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/funhiphop/76437" target="_blank">📅 09:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76435">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkkHjOeH92Li5V5jExeqDB5E3CiBoI2kAZna24ASwoCOxWtyBuwuiBWUiXh1lIYpYVdgLZQbXBvvaNVHOIZ4iSXr607wsSiIOxtCj3VocCORrsZoXNpoUrvbD79J1dyK-o53lPWA7RiewsnbVKrHLMnlIx115_fDH4P9MZ1dOKFb7u3tMwwDsViUzRmzf9pZza7uozQ5S0W0L98M8_rPA4UmZwKYpeErGY_llPBg4-a3XqWuTZj1RWvFHZSCXBFyh2slHdPS-wzCKdlCcuBZB3EoFtwtgE4JxQ4uYcugdqk0wKDvKFcoAZOsz6KL4IhfY5OQgdGJt8SFDyzqJhI08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce07890ba.mp4?token=vg1uRwYFSxte1tTiU737bpe8DUYw_WZhbRR4Un0TMK7C-e_X9VNU2rVBylQHtQIjPVAkacZ-mnTCFWCkBjQrolYTJ4oWvC89L61lmKt_1rOBrbDn8Tko3_v8HXjMIa6IPhcINGC_ijcH83LrdeAaivEv7dg14J2JLAXnfn-5J8YR0ndtI4xhLus6MPCkHP9a5xyzVc4AvqKX2Y1uyEGbW3fPPkCSjGh17RwW8KBTLeFRlydGjbHXvf6p0ZPfv2Q4-Bw1Zixv51lk4forOaUseqDOMIfiEnvmGfozbeAc9WSFXSnKDM71IsQp9N59TJwnAXnfgGOWXw1O7DUCxvUXGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce07890ba.mp4?token=vg1uRwYFSxte1tTiU737bpe8DUYw_WZhbRR4Un0TMK7C-e_X9VNU2rVBylQHtQIjPVAkacZ-mnTCFWCkBjQrolYTJ4oWvC89L61lmKt_1rOBrbDn8Tko3_v8HXjMIa6IPhcINGC_ijcH83LrdeAaivEv7dg14J2JLAXnfn-5J8YR0ndtI4xhLus6MPCkHP9a5xyzVc4AvqKX2Y1uyEGbW3fPPkCSjGh17RwW8KBTLeFRlydGjbHXvf6p0ZPfv2Q4-Bw1Zixv51lk4forOaUseqDOMIfiEnvmGfozbeAc9WSFXSnKDM71IsQp9N59TJwnAXnfgGOWXw1O7DUCxvUXGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو پادکست جدید بنی بلانکو ، بنی جلوی سلناگومز میگه که از نظرش زیباترین سلبریتی زن دنیا سلنا نیست و مارگو رابی رو خوشگل‌ترین می‌دونه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/76435" target="_blank">📅 08:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76434">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76434" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/funhiphop/76434" target="_blank">📅 08:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76433">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjwJxaZSi7MfbyIyFwiUIypHwfJgsLPxZTwHM-cWM-sfgTiUuP7eE8U9YMRoubNBUG5vxUZwsHYa2opyKpl0OGatIPmxLUXjKLuVKicd7-0xtD2gFy8GbXBzPblfRp-u1wRPmiXxiw9XSTtQ2DZjsMBBJxczQMW8fAXflT5Zw2i2GQoNUaeLBIYyOowzNStNCDwNztDuR8DTCiRZT3z_8kLFwl4eSyuuzmT52YzuyLz3AVq5Nfd_a_3Wuhp-NzTT6mGsF4W-w14S21tMVpPHx1FUYvwH0Q9O4r0VFCVZ6Nvmdmsxd8sRSWrZAgFfbYNEhhMQ1hcHwCCBoOVxPbqTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r10
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/funhiphop/76433" target="_blank">📅 08:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76432">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ به «فاکس نیوز» درباره ارتش ایران: «ما آن را بی‌سروصدا رها کردیم، زیرا فکر می‌کنیم ارتش آنها تا حدودی میانه‌رو است. آنها افراد دیگری دارند که میانه‌رو نیستند و ما به هر حال از آنها مراقبت کردیم. ما انواع مختلف رهبری را حذف کردیم، اما اساساً ارتش آنها را بی‌سروصدا رها کردیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/funhiphop/76432" target="_blank">📅 08:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76431">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2028de58a.mp4?token=F7P-ID0aFrRV-X7UJRXnCGuCK598STYkCv7MDqQ1cFAMqi3gdxSrawb6iBuz61ggO1hBJH7yWlRe1ANNfGAuGSxMMAWAy9Mia6zVhTvx41jAA_aVLepIdUixxUgwyaf5tiC1wo3R6Y3OQhLWv0d1Y4kDZchL97MpdET1hn4Qa-tjoxL9rJ1oNS0Gw9LNx6Dsb2XpUtCf-WhOmzbnhIIINK3YcMyclNY-6c9TP2ovrjf2iQ8Q794j22FuqsFEbEaJ4WnHqoXxfhjVyc6kM58ejoEZh93oPGAW236MekfnvAk1O33kapHnYBAgU5xwo2rcuhGmOuqJTi2Q3rdctQvQbmAZnJbk0Qlbg4Q7Lls33Zvs48eJInVH4LeV2ALCafR6md_akHAgfKY039faYYiHCutRigRu-B-5vsjjY6tOjvkkG01FtQuUhdWz92S1oQhF59iuc8IaKF6vur-D0tdI8ccc8pYBuftJSoN5tVEXmB6BGgRPBHfvd-kW7J5_kBfI0cBEWA4DGAAyBmjozkDLO0NOHzMvkZycGUsY9cnyuNYht5xqKPIQNzskIqa22-QvluMH2bF4lTwa9G8ZLeNfjjXLIEDsevyT0d8xZikS0ojGmuNZOzYr8UeUwvyR8Przq3G58Qz11OcA-ZQrEkVUAcYnuuV-QwpLQ6nrIzZ2lq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2028de58a.mp4?token=F7P-ID0aFrRV-X7UJRXnCGuCK598STYkCv7MDqQ1cFAMqi3gdxSrawb6iBuz61ggO1hBJH7yWlRe1ANNfGAuGSxMMAWAy9Mia6zVhTvx41jAA_aVLepIdUixxUgwyaf5tiC1wo3R6Y3OQhLWv0d1Y4kDZchL97MpdET1hn4Qa-tjoxL9rJ1oNS0Gw9LNx6Dsb2XpUtCf-WhOmzbnhIIINK3YcMyclNY-6c9TP2ovrjf2iQ8Q794j22FuqsFEbEaJ4WnHqoXxfhjVyc6kM58ejoEZh93oPGAW236MekfnvAk1O33kapHnYBAgU5xwo2rcuhGmOuqJTi2Q3rdctQvQbmAZnJbk0Qlbg4Q7Lls33Zvs48eJInVH4LeV2ALCafR6md_akHAgfKY039faYYiHCutRigRu-B-5vsjjY6tOjvkkG01FtQuUhdWz92S1oQhF59iuc8IaKF6vur-D0tdI8ccc8pYBuftJSoN5tVEXmB6BGgRPBHfvd-kW7J5_kBfI0cBEWA4DGAAyBmjozkDLO0NOHzMvkZycGUsY9cnyuNYht5xqKPIQNzskIqa22-QvluMH2bF4lTwa9G8ZLeNfjjXLIEDsevyT0d8xZikS0ojGmuNZOzYr8UeUwvyR8Przq3G58Qz11OcA-ZQrEkVUAcYnuuV-QwpLQ6nrIzZ2lq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز خداروشکر فینال رو بردن میباختن چیکار میکردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/funhiphop/76431" target="_blank">📅 08:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76430">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">MFGA
دیروز تو فرانسه مردم دست به اعتراضات زدن و  با پلیس درگیر شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/funhiphop/76430" target="_blank">📅 08:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76429">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">داداشم ومبی ضرر دیشبو شست برد</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/funhiphop/76429" target="_blank">📅 06:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k16_Adx56I452YNIkpHfND_mBT7jubkktoNhXssYni4eJSwQbJEYB1M5X-oGuOmrchWbBzrsZvoVC9zSst50GvE2P75RLqipJL2xSq0AHAECp4oQ1Ver5c96a8jo1jjokIsT726oSdcLOZ7AvfUjeaPPMz3XXs_tbPLfg2xBH6RJoy-VoeS8hyErEyUG0f7OxGQcllAfbspJ9heC_PpeDCpcTgBU13uoapl1HgtPAyP5C7tqlAFxsD38bw1bR-FqivUHw5KrkxY_sq1-Va6LnEyzSNkqg4g2B5hK0U73N3vy-NzYZEvfweKAieo8l-vSRHcb5xh9RC_potoOvxt_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب با پست کردن یه عکس از جنگنده‌ها و ناوهای آمریکایی:
شما درحال سردرگم شدن هستید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76428" target="_blank">📅 02:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2SXQaC-SA6GKt6UJg13ezKn1Ued9Y2tlGnT2zdtcqoluhPzMnMzWSU_nL0xgVJff0jWup7fWJ5FiTd0nJuUyzQ9j0QaEyBE1fRJMiM1ztN-xAjulfstVRyn80xpfbIB5FxrK5N9lkuv7bRE0oYtmwS2Kf7vPh6kuttQxhVvyIl9oHyy4rG8pb_J2SfjVBkV3TJ2d8Squ5wGFKdQHMrETqWNUcdwJa-Lolj3XWfBrI2Y52viGPLEzCLx3JbVY4SpJiqzDe0lReM_pOHr4H6QFHQOD7yZ4bbK9TbEjw50r0Zu54OFnlpTdiSDUryax8aBcF916c_7PVwqZ_UfBmTyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد خشن حمایت نکن آرتا، بهشون رحم کن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76426" target="_blank">📅 00:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76425">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-Wgzawaq_TZ4fy5tl2lxT-jkHcTfLpqKsiQ0I7LzDCa-ztrK7rZbZFP_RegvcLqSrlFpqM-tGtTT6ykLZyZaGlc4UsoT5AJ-y2WdakMY0zBcjz_b5vo7bL4r_n5KgBWk36u6aRURP2FFBsICzSSPr81rdZsuIIZUAOJiW7-8x1gEBYja_Q4v4Lqi3-EKhSgbH_imdgSCsPnK5sp7ooTz6KH1vsYQlF2Tone9zD1VcNf171WIZtKOmZ0gYkzgPNaTOQhu6lnCY25NK8M_iCKAIN40edozr9D6ZmaORvHiVcjFpW8ffRXXRC5YUtqBYydfX9TwveNZ24v90vKNh3n-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو میخواستم با کپشن سه تا تیم نجس تو یه قاب بزارم یادم رفت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76425" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اینم توضیحات منیجر ویناک راجب حرفای امین منیجر
خلاصش اینه که برا ویناک پرونده سازی کردن ازش باج گرفتن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76424" target="_blank">📅 23:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76423">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMY6f_SRYUuL6EXNpHJDkrPiqXbPOioiTiu-CBboRA6gGB--3dJewKH-_PXBlmZVf6HInHkUaS47hMAzmKjkBKLQIbn6UtDp35xZwKoLsAGUTRbpbsf96Vz2TXlEK0_P2w28G3B7GgSmEoESp3guk_SPc60CaC0y7PdzhPGvJF3if8gvnpRSd0QNSHE4Yi7f0p6E_ruMOWRw8n6Bspnmml_BlZsl22dlPIdr3vqwb6yjiWn0jTAStwutGTr7kw_DWF6Q43uN6SIyU6F_-uBhFEInr7rnvd474S9VimgFEGxPZEAuvy26d_zlJzEIjYkJgTBp4PCx51PqeRg0TKXmCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم گذاشت چنلش گفت بگم اینایی که باهاشون عکس گرفتی شغلشون چیه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76423" target="_blank">📅 23:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76422">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxcPGtDT0QeiuRi53OfYElZGoC0IfkR5dccHXn0HUVgVRLz_01tWHY_64jeKn0BwKHegyOj1LNF26NFFVDZf_Y8156TA0bf8nlrrF3xdSypqdDZ5GJZM5-Y1F5g5xU156YY7wQI1_4Y7B7UrPFZEweRJCpfTctpawgiEeUad5r7Isam0ZFPfoPAnflYqMHscCSk40-6l4gomUi43dQrAJMKuvqi5-KRKuG302YbIDowCYt4jsiB8uTHiOH4B3Svn75sStUndyrNaVVrg15cOvxti-s1dy30RtGbvBfdLwpUS0pPCGP2hAB0FqUSlVEIyImL4Rb569eO970L9bRULjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام آرسنال قهرمان شددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76422" target="_blank">📅 23:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76421">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2nDoU5tB_JHlaTY8n5Gp4Ovf_3rqU7zEjiiTW-vTA8uf1xeBtmTHsFbDTXpKCpvMtLmUM7XDPb7w7J_XnZAOHi4ULPwTY1jodg9BGHC5QisCxesL3v-yInQ-r8bNc-UFRIqamKGvYLPGZYvT29HjNJS3zt8k5yJUHBD7YUf9c-Exd3y6_GX49-_hXui05XXfNNhasWc6OJ3sP0YoeM3uMPOHEOCzJCsq9-IVYPEzwT5uhFnktD5bCgC2PFirrQK4uEkr8rCOO1iAuL8MIykh43RIbXhCdp5m1ig4DoPZcUkLJGgH5FbCYTY5l0nSJ1ASiW7NaYKOPeGSk8m8M_PeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم اینجا کیرخرم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76421" target="_blank">📅 23:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76420">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حاجی فیلم خاکبرسری ریری هم اینور اونور توسط یکی از اکسای قدیمیش پخش شده واسه زمان زاخار رکوردزه
😂
😂
😂
😂
🔴
برای دانلود کلیک کنید روی لینک زیر :   https://t.me/RapiFreeBot?start=get_uplzypfzeequaabv</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76420" target="_blank">📅 23:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76419">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9FjsaMnW9e42nYH-m0TXI2QBPkaQOMPGgXsTbk9aA0ePL9PoDL8cCQnBA6iisWitQvz6QfaTK-r6PUYYJ1kn9p200Q1uH1MsXm3IMGphgLVK20lPt4G2RY8S3FBqvIsoGz6EnuGr6OesHeNODmTc4fxfCt6ks0q6cZir3qLLVawfaShgq7W_1LVYxNGX8bcbh1GnL-27pmHXdtTf_5LJduLjpe8My_g7lwOzq8cIfJmSiSK2gkLTykEgZstiJJKFZ8nWSAkvI3jN_Gyt4qSeW2IHltLBhai17zM24x63JSxCQQQhEik-a8mhEp21G6_wynBhact60ydyysEr4rrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه من همین الان با یه اکانت رندوم یه همچین چیزی با عکس خودم پست کنم زیر ۲۴ ساعت اکانتمو می‌بندن و میان میبرنم تیمارستان می‌بندنم به تخت
ولی این کصکش چون رئیس جمهور آمریکاست همه می‌گن پشمام دیدی چی گفت پسر
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76419" target="_blank">📅 23:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76418">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UstPA-pqAvIBW-Fvsatmdzvg37HAGAIWcq15G9mEFeHSNneBPxU8ydN_jAZ4dgqRDgOgpHgslxrb6SMrG7BeUXeCvJ9gh7vXLKeJRHrA_VsX0rUeYCJaLtss5_S80ZpAWSMihci82bTOaHihn59ges8q23OS54W7WLv_4EJNm6bKbjN7XyctypOtWiria6iCk76hpNOIE3je30DOvm7G7WUyCpc149ZqKhwUfjFrhfBiaAPxpL0laM9pxjlTnaSNK4HcKstVO8GNAx03xx_-vDVBqU8FLWRb6gpQqOh5W8t4dEFrmHbr2R3M9k7Jm5twqHK5_iyzza-OVp962fyIfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی فیلم خاکبرسری ریری هم اینور اونور توسط یکی از اکسای قدیمیش پخش شده واسه زمان زاخار رکوردزه
😂
😂
😂
😂
🔴
برای دانلود کلیک کنید روی لینک زیر :
https://t.me/RapiFreeBot?start=get_uplzypfzeequaabv</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76418" target="_blank">📅 22:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76417">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">با این نتایج انریکه چندسالم نتیجه نگیره ناصر بهش دست نمیزنه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76417" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اما امباپه عجب آدم بدبختیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76416" target="_blank">📅 22:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SacIZ4aia98P8EMsHSQpMhz_Taw7kVKEKcmYpGnnq-KT67eW-zLXeQI1r2Oh_Se5U9CmDUWuKv_259TkHTJ_wzNgzVnTVZOHc4Rp9L_Gde3yndgALYeCALUFAyq_ciSqLoDvrUHsS3bmhwwp68zzvWTCDIBCgoRConABwrry0HNjqAhiLsC_ER58tMXoPb2f5fOgOy_HzqseF32HqfWouPzHkaqT0yQ33-kWHz4_1V1M-Vku-M-2TnPudHWST7p6rKljhVDJESP8Ec8JDZ4aUqGeQjqil1OVWLnpvBKbi2QBSZfVLtmB8yVbTUeNkgwkpDEJTXaoUpeoWwTRrylJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده مشخص شد https://t.me/FunyHipHopGP/12247710</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76414" target="_blank">📅 22:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76413">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید  اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو  یک گیفت Nft میزنم برا اکانتش  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76413" target="_blank">📅 22:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هوادارای آرسنال الان یه دوش آب سرد برید حتما چون بشدت حالتون خرابه امکان خدایی نکرده سکته هست،حتما یه دوش آب سرد برید و سعی کنید گوشی رو بذارید کنار تا فردا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76412" target="_blank">📅 22:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76411">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIQbBszGNwV47SyxozY0pPWimTrVEjy8EIiJ_9kdR_VyUVpBdLOg8R-6vWWIB-JT0Gn9ZLUKV0657ANPy0lIzpY-e8MsSwJ-S4uNJbo1T3zV9kVzaOUNLNMbmXA1YCOH-0SZpGyauSsO-qiZLv00Bu_c3-DlKRSXMkP26WrCIlL0J3mf3K4Tej--rRX2upS_w-rY4KHFZHYxlATt5eckZ4QvuSvttsoePXpwJXQfkm2ntNR6Mhaz1HkddvHSHkHhxAo3P30YMoq4Ws0mpTHbWhfvqR5VzYKCg8UVI6PXHUqBF5eoHtE6nrj4P3t3hJJP2ufDxbyieD3OkgEU9Bk9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پروف
#غمگین
#شله
#نور_از_دل_عالم_رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76411" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76410">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید  اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو  یک گیفت Nft میزنم برا اکانتش  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/funhiphop/76410" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76409">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گابریل
❌
اوساگونا
✅
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76409" target="_blank">📅 22:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پاریسن ژرمن برای دومین سال پیاپی قهرمان لیگ قهرمانان اروپا شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76407" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پنالتی  رو ریییید
❌
❌
❌
❌
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76405" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76404">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گابریل پشت توپ
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/76404" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76388">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رفت پنالتیییی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/76388" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آخرین بار که فینال لیگ قهرمانان به ضربات پنالتی کشیده شد برمیگرده به سال ۲۰۱۶
سن سیرو
رئال و اتلتیکو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/76385" target="_blank">📅 22:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76379">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گربه های مشهد گرسنه موندن امشبو
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76379" target="_blank">📅 21:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۹۰ درصد ملت لوز شدن</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76378" target="_blank">📅 21:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76377">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تمام
بازی رفت وقت اضافی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76377" target="_blank">📅 21:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76376">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">روح بن لادن رید به خودش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/76376" target="_blank">📅 21:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76366">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">روح بن لادن الان در آرامشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76366" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76365">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صدا سیما باز اون پدر تپله که پسرش رو شونشه و هردو عینک دارن و دارن خوشحالی میکنن‌رو نشون داد
چیزی رد شد؟!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76365" target="_blank">📅 20:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76363">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دوستان من اشتباه پوشش دادم
آرشیو وار گفته قبل گل آرسنال باید هند تروسارد گرفته میشده نه پنالتی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76363" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76359">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تو ضد حمله های پاریس هم باز ۵ نفر تو دفاع ان</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76359" target="_blank">📅 20:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بازی همینطور ادامه پیدا کنه صد در صد گل مساوی رو میخوره آرسنال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76358" target="_blank">📅 20:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76355">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گویا اخرین باری که آرسنال تو فینال چمپ گل اولو زده بارسا قهرمان شده
بارساییا نا امید نباشن</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76355" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🛑
ازدحام جمعیت در مشهد بخاطر بوی شله</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76354" target="_blank">📅 19:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76352">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هاورتز متخصص گلزنی در فینال لیگ قهرمانان اروپا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76352" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76350">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ارسنال زد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76350" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76348">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بازی داره کم کم شروع میشه
به امید قهرمانی رئال مادرید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76348" target="_blank">📅 19:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هم فنای فوتبال عقب موندن هم فنای هیپ هاپ، برا همینم اکثر کسایی که رپ گوش میدن فوتبالی هم هستن و برعکس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76347" target="_blank">📅 19:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستان به صورت قاطع فضای فان هیپ هاپ برا فوتبال مناسبه یا هیپ هاپ
فوتبال
💘
هیپ هاپ
🦄</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76345" target="_blank">📅 19:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شما منتظر فینال سی ال اید من منتظر گیم هفت سری اسپرز تاندر تو‌ Nba  پ‌ن: فهمیدید شاخم یا بیشتر ادامه بدم   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76344" target="_blank">📅 18:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76343">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جدی چرا اینقد آرسنال منفوره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76343" target="_blank">📅 18:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg4sckaEu9_0iCRnkbwPserfJyvByz874VdmAQ3pDIjT2vBRKsRLrfDuDwXaBA92dzGohgdAOdnUZLMkBPM3Zqj8olRYa7bhlZLmu8K6EN0u4v6seOeYwuEbr-ePWFG6_U4niViFTMP5E98CyrdA95fMk2D2xcIQZl2r2rhJV_qGJfBLv-cJ0CS_RKXJZVA7ID4wSHiT4ewZv4PO7qz_j2HoprPqN0P9SVjdL67STSyouoH5nQZeAgWZaoeeEW23HA8oQkfzeSm9exhNFC1Jv6igfe1uvFV0eEs-kjocv70xIGIEaEWhzGYLHN87yHXzBvlKvgBwQTGlrKXs_u7Tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمجید نقطه زن، کاخ سفید رو شخم بزن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76342" target="_blank">📅 18:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شما منتظر فینال سی ال اید من منتظر گیم هفت سری اسپرز تاندر تو‌ Nba
پ‌ن: فهمیدید شاخم یا بیشتر ادامه بدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76341" target="_blank">📅 17:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMImqoSp0jVizWsLP_PMEUdGPoXiKUV3lOKYvHdyXm34LFMT7cIZyW7UmZc5_D-yNFOjJXCsJ6fXm32OdFnUhNJu3qCX_8nV1JPtan7jeQlKLz3y5BjoE_fj3209-mLu9RiJ5dzIwDitrhf1iIPIbrdhElM1oUb15P0DzmO6vFMETkbbgbaC8bhMyqHCy0mDQO3q1Nr9JLpZrfp_X2HG6sPD9Z_mGgWtP7kqeseVeZB-OYfYtcWGjcCfAIVZPoAcNRysF-jg_3HeFy-dO2AQyyobGH9cslAclKam1u39QBdJnfc3fDx7Y5XL-2KIf8Dl44j0Cwrc5xcM0xDj6gqlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76340" target="_blank">📅 17:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcSZDRz1sxhcT3Sx7lkKlmbLmDXcxpHENVQQBI1hNlsI8rBroIxDZrJOVQNrvO3OhwfnW00KlTykBvfCqPtWGxCp_aU-q-UWOcxhdMN7XHcx1vNoL4z2GmTBnRKatJBjCPH4Ipv3m4mExOx2M4kSdfkLdWv0UtH4dPpTYNdQBsRAqHuOIRE3BwAf53onwfsA2ntfRh3iWm4D36Ja6LOB0EgnZTdxZO58gtPOR7YJt_l0p2ukuCLCX-f5vgvQpzKurCZb-raxx_Km6QI0BsYGusI3U_o59wXRSXwlc1_3RlEGdsXZupIBuXPCZDZqqLSA7Gz8yzcGAdprP10ib3HLoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشب ساندویچ کباب شامی رایگان از ساعت ۱۹ الی ۲۱
مشهد،نبش پیروزی ۱۴،رستوران پلنگی
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76339" target="_blank">📅 17:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vfjd0oB1FcVwt6tUJDCR0vGPJVd6OfrqYNS-CpBVFv-exsLc5YoCxjv4XQLNYCtksogc6jHA_2_edOrc9b0_JETAbM3bj00szTjFwCfnNk8nF0FR_vtipj8zGCMdZDVkgET6thth0Q_bHDCqzm_d1B3fRXJLlwYgOnmR7YcEx5p48EXh5pI47F6NYBv3ByEiAd7_tA854ZizDwG2HCbAzBKrlXA9PihHJnKt61P7_Nl6ZEVPK0JSviPW2TA6hlURJumirXxQ7QihQLJz9CMDgqJd5NJbKxtrebWp16vcKQaT7U1nse0PZMS8JFC15VBzuzhgCbngtp_kMRx5N7zCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g9
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76338" target="_blank">📅 17:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76337">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید
اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو
یک گیفت Nft میزنم برا اکانتش
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76337" target="_blank">📅 17:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76336">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI38xRhx6U5rNu9rwuCqjYSA7v3wyARs1N1TYpHGhJTNtLS5bn9qhpFOXTBjt0KNb5XybD9Sfc0EpJ85IAsxnupwEnGrHSp3QdKKQnr4aj0yhdZHmi0UvyQXHOw-pwWTzj8i6DLTnvIv2wcVNNwBd0avJUIC1VwLwRPh_YDHNWYrkqHQqoh2BZwWgKyO3Abq9ePmfqXFEaLA8X0V0d36MX5EUCqAn4PgrXaE2UFTU53xWPHRKAlymW6F5FLICbVkPoW08znr0n2SiwcpdS_zlAKKz1zg54sk9isp0Dbitae-1i0gfLR33g_I8CgSlHLmsPLQYePEOJiBEQGrqjmUpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایا فرار کن این میخواد بخورتت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76336" target="_blank">📅 16:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76335">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-W6eTELdi-lbSmJ6BhfJaLj4x1gF7-e_6JgFS0IomLEiqgEYJHL67UW_IW6SQC3GbMCFKonVvTkIQT9WAGNPXjD0AlpHtWQIvxzoMhDQ2E7q-nBLVs38xgSfUeAuq_8VXBw4XIgwwnYMzGo7i963D0B3hLxFleRJPyv2xJd9amy988MncL-q5L5C3foA-wnvcMX1Nf0dV7RVmcXHpwH3YQ4MKVBkVnE7dm-3fnFgaEUWJyPO8yFOvFthBCoDuwBJoKw0MR37h8G12t3FYdcc8tWLgE9Xh2I6eJpnqeL81702hPTHFe7bNbySv50C4lzpDdZza3VrT18OtiV37-UQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیدم مردم کوبا ازم کمک میخوان، میرم اونجا هم یه سر برینم امیدوارم اشتباه شده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76335" target="_blank">📅 16:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76334">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSQmWupNPqrRuhxPc7nqaWPDUmtkO72hUvVczrOtsIS_2W7OKFmivCMJES_rpsfN7xBsymNJD8luL4W3FKOsdwOib8zTtwaqrlt8M-BEId_eeNvEZ0T5Gak_7LT5RUmiDB1PGDQubzn5mzqa6ujTtzg2RiurYJ4RfBM9l17hXEudR2LE9jMmbKOcjg65h687_M6mQyLRkwMwqfai5IieU1taeb3L_n7HBMBplAZppp7QEaQlAFEGdkLhwFybob8I5d6UuvTTC5jTGHjrYkEXvWMhiejxJL0JJaWR0vqg3U4ycxtm9XJirOB-w73RX6DHUvWoZxW1bwSI_2a-7t6laQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه عکستو فرستادی برا ChatGpt و پرامپت آنالیز جذابیت رو براش فرستادی، قطعاً و یقیناً کونی هستی  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76334" target="_blank">📅 16:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76332">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگه عکستو فرستادی برا ChatGpt و پرامپت آنالیز جذابیت رو براش فرستادی، قطعاً و یقیناً کونی هستی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76332" target="_blank">📅 16:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76331">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سلام به دوستان عزیز در خدمتتون هستم با برنامه فوتبال با فرید   آرسنالِ آرتتا تیمیه که دوست داره بازی رو در اختیار خودش داشته باشه. از عقب زمین با حوصله بازی‌سازی می‌کنه، با جابه‌جایی و پاس‌های کوتاه فضا ایجاد می‌کنه و سعی می‌کنه موقعیت بسازه. وقتی هم توپ رو…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76331" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76329">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سلام به دوستان عزیز در خدمتتون هستم با برنامه فوتبال با فرید
آرسنالِ آرتتا تیمیه که دوست داره بازی رو در اختیار خودش داشته باشه. از عقب زمین با حوصله بازی‌سازی می‌کنه، با جابه‌جایی و پاس‌های کوتاه فضا ایجاد می‌کنه و سعی می‌کنه موقعیت بسازه. وقتی هم توپ رو از دست می‌ده، سریع و با فشار زیاد برای پس گرفتنش اقدام می‌کنه. در دفاع هم تیمی منظم و سخت‌گیر داره و روی ضربات ایستگاهی هم خیلی خطرناکه. به طور کلی، آرسنالِ آرتتا تیمیه که می‌خواد با کنترل بازی، پرس شدید و نظم تاکتیکی حریفش رو تحت فشار بذاره.
پاری سن ژرمنِ لوئیس انریکه بر پایه مالکیت توپ، پرس شدید و فوتبال تهاجمی بازی می‌کند. این تیم با پاس‌های سریع، جابه‌جایی مداوم بازیکنان و گردش توپ سعی می‌کند دفاع حریف را به هم بریزد و موقعیت خلق کند. بازیکنان در حمله آزادی زیادی برای تغییر جایگاه دارند و به جای تکیه بر یک ستاره، روی کار گروهی تمرکز می‌شود. همچنین پس از از دست دادن توپ، تیم بلافاصله پرس می‌کند تا مالکیت را دوباره به دست بیاورد و اجازه ضدحمله به حریف ندهد.
پاریس احتمالاً آرسنال را شکست میدهد چون در انتقال‌های سریع، حفظ مالکیت تحت فشار و استفاده از فضاهای خالی بسیار قوی است. اگر پرس آرسنال را بشکند، می‌تواند با سرعت و کیفیت بالای بازیکنانش موقعیت‌های خطرناکی ایجاد کند.
تا آنالیز های دیگر بدرود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76329" target="_blank">📅 15:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76328">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا:
محاصره هنوز برقرار است
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76328" target="_blank">📅 15:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76327">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">المانیتور به نقل از یک منبع اطلاعاتی ارشد اسرائیلی:
طرح سرنگونی نظام ایران با همکاری کردها جامع و مفصل بود، آمریکایی‌ها کاملاً از این طرح آگاه بودند زیرا یک جلسه توجیهی کامل دریافت کردند.
کردها مشتاق اجرای عملیات بودند اما واشنگتن در آخرین لحظه آن را متوقف کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76327" target="_blank">📅 15:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76326">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آرنه اسلوت لالالالالا
آرنه اسلووووت لالالالالا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76326" target="_blank">📅 15:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76325">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بکیرتونه ولی آرنه اسلوت از هدایت لیورپول اخراج شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76325" target="_blank">📅 14:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76324">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5Egks3mJQbiisDnOzrS48JgnfVuK3D-cCbbDGrvYuCuXShG4y_5yp5DeyDbKXH2EdA4cL-O6kmzIfG25HrwqnrSta1hjqz6BxA6YXq4IQlUB5FWnRCgnp0Bg3YZxtflY-5LP1jjJsfcMzp6ApxK_sGuaspH1amHulfl-qA-7U2G3F8XguEC3rrNNoUr6nm8YCsNwSuAkgxjKHHURGJjbHB-lzZM15qsDn5OIptfsXoDY-hFjqgpVatKt1m56YKT5TuCpqgLNeCotPZq1EBQ_UHUWUOIZEFsVB3aLCSbwOcu5WkdkZl1P7Xm1GMqik4x7_VXYga3t7kBPXad8kauRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسب دستور مقام محترم قضایی این صفحه به علت فعالیت غیر مجرمانه و طرفدارگونه ترفیع مقام گرفت.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76324" target="_blank">📅 14:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76323">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برا مثال شاهی به هیپهاپولوژیست دیس ناموسی میده بعد کاگان میاد باهاش کار می‌بنده الان  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76323" target="_blank">📅 13:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">برا مثال شاهی به هیپهاپولوژیست دیس ناموسی میده
بعد کاگان میاد باهاش کار می‌بنده الان
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76322" target="_blank">📅 13:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76321">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حاجی شاید نداشته بنده خدا مسخرش نکنین</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76321" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdJcSrsU8O2X019wYYQICe3K4H3zaf65pT0YPuFxFaLPTM0-MkpRNmzZme5I95JGf73caYs75Lt-hgNPatJCwACSpMpveCPsdxLBotgtU-QWNCrVOfVe_BGP3D6aHn1rgwrEt0ootrLVC9YyZDjDB-YnhavQYbGClIGsDwWNgqJa0heSfPZ7uGUVEN-Vi6GlKlHB3EewwyB4vzUXGdR8mtl8YRvlEojzbMr1dMByB9S8pXGnxllXgg4v0GWYXIAA37bAqxi4A4VfXNxwxcn5ys0X5hARzO3AjUFY1N5poh8liEV-afN_aIO4vBPFAXlgkrNXvp4fMS4AFTjgCigk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیو نمیفهمن پوبون جان؟
اینکه چرا کصشو تو میکنی بعد پول بیمارستانشو ما باید بدیم؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76320" target="_blank">📅 13:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتیجه بازی امشب رو پیش‌بینی کنید، دو نفر اولی که پیش بینیشون درست در بیاد باید نفری صد هزار تومن به کارت من بزنن.
@FunHipHop
| محمدرضا ناصری آزاد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76319" target="_blank">📅 13:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puac1iG8pHdRpP84tANCd7tjqVZYOs9pMVhUuQYa-lEevo5yyVCVGvBIGFuk-Jy23fQ0LoD7X7IFfYI4sFv2Y1po_zw-dX55TrDTtTv1ctBLgva-BpoaF7qBkFhOXq1-1LYHW3jofI-tq480q79ntFHnBIBCWyPjD3cVsYawaxALLTTY444f3PAlezHQB6ML372VSDBLPXD1lUZIAeambFghjRaNkCzbsx_adued3MoyAP8AonrpuPU8B1durkf97kony_5WOcK1yEBRUnOw3_uWxEjzt-h5h3a_fq25wDf2SFGA3ZdJjRaYd5NZSLLQWRyZ5OiGUmpzBiU_b_PfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76318" target="_blank">📅 12:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خداشاهده ۳ ماهه تو ضعیف ترین نقطه ی ایران توی روستا توی نت ملی و قطعی کامل اینترنت من وصل بودم
تا پزشکیان نتو بازکرده نصف روز قطعم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76317" target="_blank">📅 12:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کنکور سراسری به همراه آزمون پذیرش دانشجو معلم پنجشنبه و جمعه ۲۹ و ۳۰ مرداد ماه برگزار میشه، البته اگه باز نزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76316" target="_blank">📅 11:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76315">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پولاتونو جمع کنید ببندید رو پاریس، دریک رو آرسنال بسته</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76315" target="_blank">📅 11:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76313">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkqHUyFGE3CN7g2kdO4lRU2dPsIIupcB63NVhJVBA_Q81If-7bJRFzx6iqGIjX96maaboxEbiR0Sthe6Q5bGSsnT192WXsC6t4uCI9wdH286g1MO_LALLG96iXxCA8ttWZbYVnOPX7KZxu8-0zW0sDL4tjzrYhze-YVtIi0TkYTweAsQ0kz5RpvEim4brRvsYpnLJPCEMcfITO3Od6h_8_oNTPXj2EQWkIrNwS4uBTyKEdIRCg-9VM5APRIhk_ivTZodr7cm7ox3hRBqqM1_hMM_FKOSq0jGVsoVMu43IxxOfq0-ZC6dkya63czjsxqN31S6X3DojLNexRXzd4cG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس تهران
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76313" target="_blank">📅 11:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76312">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خدایا خودت امشب به سگ و گربه های مشهد رحم کن.
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76312" target="_blank">📅 10:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76311">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZMuUBRvOUYYWN_NtaC2jweHqmeBf6Y-tbzjGui4JfwtBjP0LwUDodZegiMmZeTypbshUBUq5KXmDNhYxvxDzOlUc195jrndjSy84tP95qjUt62jf8_YaWoRdgN6ed5C9MbPZfLDbIPM_ZJ7qOdmu5agOkEqtOrp1NzuaQfxXUVKjcKTdjNpoIe2mAu3ReVB5bU50mFbXXlAPn466Doiu4P6A2Y5g_p-OMCkQXvZ_WqZ3aiGoICwdJzPWW-WTstcayxJ15Rn1ZLOed6bUa2ONBZhTdpBieNiAx53OTh4aK5S7e4PqrLC0O486r5AOfg2hHO2yvs1kaKfHgK6MFlLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب فینال لیگ قهرمانان داریم.
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76311" target="_blank">📅 10:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76310">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76310" target="_blank">📅 10:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76309">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt3sfUSDbaQUfPiT29fGyl9oC-G-a-ndo4n-G7AFNjDzSGi4H5kZevx2fsbH6lGg5HRgr9LqRjtbBQmKgS0Egm0ehhBbA3NpmlZ06YmQEEBFK0dXYNMRnNiKVbFUePeInlEZxmCN-GNLfozYE0IaSmjsa6fOlk_UpYffWdUNjsygazvyfWMZdxF77sVY7RcCNre973-rKFpGL_4P_NiHAMhjbmktyyDQXlID7KGOObFXEzS_twKJlawm6m-mzauUMyUbrvjPW8PuTAiOM0WBHLmMqwYlx9bcr19GvLk3d-gzXeMsMEMKdbVnk1CjVdjbDs97pqiRm-GPIWfXneFMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r9
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76309" target="_blank">📅 10:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21fcfedbc.mp4?token=XnBnSbQAgNF1kYdeJ-IA_OePW14uIxkzm1PYHd8AXg_T2Pmy7bVlrLxpz8_UFR88yvs80R0Lk2pn-CwHysGSYU5FcYe2yCXgwfteiAxdlotPsWttTA7ZNBRAoAixcAhhWWI7ujc3sx8ZI4mZgLN94eblrnlB7katZRwYHl7hJkwH9rbXj5gufZyEosfhBCwNp3KDXvQNNOKvlXv35gXnK7FkucLsAWZyKojgbUSiMF16q0hooE_QqocFC3betkxz86D5kjerHW6yEySIGpi8eXr_dnfMhYsIHouREIlPDJrfG1qbRpAPkYAd9dsKM-Il3e1wVPxNkujit5jJ3aluhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21fcfedbc.mp4?token=XnBnSbQAgNF1kYdeJ-IA_OePW14uIxkzm1PYHd8AXg_T2Pmy7bVlrLxpz8_UFR88yvs80R0Lk2pn-CwHysGSYU5FcYe2yCXgwfteiAxdlotPsWttTA7ZNBRAoAixcAhhWWI7ujc3sx8ZI4mZgLN94eblrnlB7katZRwYHl7hJkwH9rbXj5gufZyEosfhBCwNp3KDXvQNNOKvlXv35gXnK7FkucLsAWZyKojgbUSiMF16q0hooE_QqocFC3betkxz86D5kjerHW6yEySIGpi8eXr_dnfMhYsIHouREIlPDJrfG1qbRpAPkYAd9dsKM-Il3e1wVPxNkujit5jJ3aluhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76308" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310846887a.mp4?token=d34HGS3Lg4F9OgDWCYrG5g7ZR6BauZrWre-H-fOgDO4JwO-dlG__j6-TvipS5nSqeZNsOIMP5jm2Ow2DB4hRH-vmT1ETewNpM7t9pFaVstZHJSIxL1zLBP48mYm_OMZCbmeVR5aat4KWxCsxZuQN5OPU4lOzbZ9zsk3oeLAqpiUHwoF7A4DP3B9IzcDGI3UYfrDghh75cV1IBW37bUGxt_y7h-pDrPsS6EyTVDZLLgTX7c1GcPk4lIIcpj0_BC1spT9hkuxTyrc6hUd-4TyxPeFCdxdg2cFcxGU2I4d_sDrwA-Q0205ORWzer2nnY_Y95xCAchQJGv7vsfUc1ImscA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310846887a.mp4?token=d34HGS3Lg4F9OgDWCYrG5g7ZR6BauZrWre-H-fOgDO4JwO-dlG__j6-TvipS5nSqeZNsOIMP5jm2Ow2DB4hRH-vmT1ETewNpM7t9pFaVstZHJSIxL1zLBP48mYm_OMZCbmeVR5aat4KWxCsxZuQN5OPU4lOzbZ9zsk3oeLAqpiUHwoF7A4DP3B9IzcDGI3UYfrDghh75cV1IBW37bUGxt_y7h-pDrPsS6EyTVDZLLgTX7c1GcPk4lIIcpj0_BC1spT9hkuxTyrc6hUd-4TyxPeFCdxdg2cFcxGU2I4d_sDrwA-Q0205ORWzer2nnY_Y95xCAchQJGv7vsfUc1ImscA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست:
همین چند روز پیش در جلسه کابینه بودیم و رئیس جمهور گفت: "هی، این یک معامله عالی خواهد بود، و اگر ایران نمیخواد توافق بزرگی انجام بده که تضمین کنه به سلاح هسته ای دست پیدا نمی کنه، میتونه با مرد سمت چپ من برخورد کنه."
و این تنها باری بود که به چپ بودن متهم شدم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76307" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vdz82EVn0Ipu5ayYWos4U9Y87iJ5cPDUgAgTQCQbHvfGWO7wKmPL_SQd5oCH9udPN2hrb2XqIUZpzu-fsyhmdlM1g8Altkxgaug8t04QqTj8lvBslX_bfneG81AkhNX3bYah5BZkptT6lrQsnfTz6SGaIfTOJk1yKOmGdr5yn3eElsuAhgi3j-HKjLJUTm7x7A_J9EsxTV2WzYMMq1ywCtIhkMfa9o69ga1RBpB9IexCT_g5CipltaGmIHG_ajTmkfp70qjDnBPZ0c-sPlydVdFL9dylc3XCO7mtNhuZiETKKcVHz8PYe2hFluMVzs4NlO2r-O8j-Ucb7qBiFm2jlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Moeed-P7rmM7pkmGMliCs1duf7JeI8cpc_D1i91eLcKqyua04QgV_dW_cEBsmOV4wd8N1raxekGyM6Y9E2z6lA9p25fbCcJf0EfQCoDjGRbsl-GsTe-YFERxo9WvptQysvz30X2ym7HBSof8yN1hTTfMxxMkKMfy6o8xeT9vHHheCjza3HqnHVILOeY_d842nxdjyQSS7MY7hAkBmY66wmvStK5gCks29wiW4t4GgGFWhFWHMR8nvbs-TrkjXZbzQthMzazjqtl-EL2PWD3De0TcCbZUYR-G36H7a3Q2oUxnjqkng7dIdECAlztxvCUjp9OEV4UJvH2ieOUNNHe34g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی نیروی دریایی ایالات متحده به دریانوردان و خلبانان هشدار داده است که سنتکام عملیات نظامی در تنگه هرمز، شمال شبه‌جزیره مسندم عمان که در وسط تنگه قرار دارد، انجام خواهد داد.
طبق هشدار USNAVCENT به دریانوردان توصیه کرده است که هنگام عبور از تنگه هرمز با ایالات متحده همکاری کنند. همچنین USNAVCENT اعلام کرده است که هر شناوری که در فعالیت‌های مین‌گذاری شرکت کند یا از آن حمایت کند، هدف ایالات متحده قرار خواهد گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76305" target="_blank">📅 09:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76304">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromInfected</strong></div>
<div class="tg-text">سلام فربد جان ساعت 00:23 است از خونه همسایه بغلی صدا آهو ناله میاد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76304" target="_blank">📅 00:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سلام فرید جان امشب نزدیک میناب ۵ تا صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76303" target="_blank">📅 00:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76302">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حوصلمون سر رفت بیاید فینال فردا رو پیشبینی کنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76302" target="_blank">📅 00:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76301">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VETNe47k93l4Qm6iumZtLH-oHhwpPyud09MGwV4YZJw6CfiqqiGIsUtv6fF2ct7XfUFxVV0GT1UApwip0TAKALBBhumRAWKvaO80ECjY16qbUj-A8v2PckHZIsVkZDGQnG3qJZz4MmBKyvwCtNqdirGlasKzCC07_SAlEsHSfSIn7UvBFrBVwIHTTpQySBxHYqyTBziJyDgHbIGlvwPHWgfdACj__Y-ReNaJfLy7qFjwFgrsWEzN_CDN_3fhf4Joi8VFKO_5SKqXfTmD1PovWfa5Z7zjg3bc0afSpF1ZAihZAGLh_v54IXebNJs-I8K9FUkszfMu6VLndOigKXjg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا 1411 با پزشکیان
✌🏻
@FunHiphop
| ALI</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76301" target="_blank">📅 23:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2XkYczrnayoaikTIpoZBbbalOwelVjLo1t87oRWkyjYNt2Apy1XOO-SOxJ9alp9rYRi3Ecq0Wl0UspUFg1PTynqSDUViMhIE-OPG5mOv8_nzcj961a-sKBJBPHwU8txrsPEse4B8oNOXOwlra7992JTBxKZw-6msSG0Eh7AcXDQTh1ZmJkqO4j99-_AiATka3YRB3AeCccxu7SRwaYEim3PO5QRPnQW4iMPzHdWq1NWPRe-JWIEck1wWsNTxiE6AlsUUaVDApZ7YkuSODfeQ_6jV5zAPwOAtyV7DAnIczvYWdD8eLYmQiaowzPduk9YTFUzI6pZwZa74GgC2CdSbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکش شبیه شوالیه هاس</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76300" target="_blank">📅 23:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNoah</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN84r9UugzyLums2kH76yIK_3GNoJZtkvW3EzAp-H3BAGmxxby3PXuVFfCoqwqTUVGUThU5vFsosTXkS4bj2UKNsdGmGH0pbO3V_K_up8WfG_rnwsjNS4Bkh0Ex5Lve2ON6iEftVFlUijqI55UsytyTAyWwoywAhSuX7zlRCzZ7b6MzI5Zw2WPOyS50Sgq6tf5P9V2hlgqHI9j214ceZ0gxR5az_XWXBBFrYATldoGM3y39ibZ40P-g3SChsbz5rl8X-JOtOdO0R4KhIuC2YeuKj4LK_v9hBzljKmfUmmFwDLfGSqjaQm0ULQWHjl3qJ75ssxvVP4DcYQsO59N6X2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس قدیمی گوردون با لیونل مسی
یادش بخیر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76299" target="_blank">📅 23:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">از گوردون پرسیدن تو که انگلیسی هستی چطوری اسپانیایی بلدی، گفته چون از بچگی میخواستم بیام بارسا یاد گرفتم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76298" target="_blank">📅 23:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پست جدید کاخ سفید: اونا بین ما راه میرن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76297" target="_blank">📅 22:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95e3a0cee.mp4?token=HHF7gr0jt52LmNw5P3WokpLm9-_HVAX99QlxB1sBHD9TzGa7lYpVvDFiuhrn6NS6F3_2cS4lxlhkz3WjoFMLM28RKQjRDi7qLDsJGCUBjoYa0iRPToMvtR1gUKk9wZ61NOg5602ipZFeqd4cRKKtYPsrUN0gQo11mxRLv7Eh9QzJFKWDWUfT6yXCdSx35jibaebcZOKCRzPpiJz6XMP0Sxe-3ddKECWQ68phJ9N8YhHbXtYj5IMi281BL1_CPocIl3-Mj9dYXJDkaARM0nXZ2Q4ux8__lN6928LbadOd6sBnMzdj_RFEk_phDQEfT3RAtxU8NcGxlx1vp2mhy2HOCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95e3a0cee.mp4?token=HHF7gr0jt52LmNw5P3WokpLm9-_HVAX99QlxB1sBHD9TzGa7lYpVvDFiuhrn6NS6F3_2cS4lxlhkz3WjoFMLM28RKQjRDi7qLDsJGCUBjoYa0iRPToMvtR1gUKk9wZ61NOg5602ipZFeqd4cRKKtYPsrUN0gQo11mxRLv7Eh9QzJFKWDWUfT6yXCdSx35jibaebcZOKCRzPpiJz6XMP0Sxe-3ddKECWQ68phJ9N8YhHbXtYj5IMi281BL1_CPocIl3-Mj9dYXJDkaARM0nXZ2Q4ux8__lN6928LbadOd6sBnMzdj_RFEk_phDQEfT3RAtxU8NcGxlx1vp2mhy2HOCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید کاخ سفید
:
اونا بین ما راه میرن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76296" target="_blank">📅 22:46 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
