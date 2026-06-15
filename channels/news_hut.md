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
<img src="https://cdn4.telesco.pe/file/puVy353vPb7d6UE4Gagx_fYfykHBsEkUqxeYAxpYXLs243-rOQSgE-wioe724d4EHr1uHyCnXaHVC0GBlUj2UEfKHZJPMi6qSMDFkYT1qvxbIZiIFct2pR1bKZYxB4FQYKFhCsHhch2xIc-H9-gX0sq4ItrSWywfIHgQXI5L5Wd7iXf6GbbdXaC8eqv8pnqz_PeGj4ht8v3labKRbIdtZUIUjLNu3I7wm7fF1RPcmy1NsFiDRHcuGaQRJuoCkPAcnTAiQ16QjuHcY-fHA_9updrAW63PsugthGpRpkyGy48KYAf70-HAtSdFtuqyPL8ATWsOguX1957MytrI_eFdfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 224K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-66149">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APN6xYnnCSigNhzZ1uhDT2ertdmqJOxR-vCvNUxohKPhuXWxGVLj0n2NXDgB-dfUiZZ-tLFoPoyEILVW6D0MhGaYyU15H5QZpNAIZSZmtfgjs4TA6jFIv4HzPUURY2tSzkhJXPXd5yCJoxFj8GsVT11I1Mug_t_VDM1ZmGJgNUvsonhLkE1Vuojj_SNU-gqhvhwkVBWCyLSeK71gUEN2ezKvoYS_ExIz7WB617XSRrSkW_2ZY6A27Kh6wW0CyF_lMLw4hr0dFtX8xB07QAOr6ZnnrdscVD9V-_R3nOTYPHxMWt34dUhYfd2HqbSToiFp1QztVu7Kgzru47vtL0I7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل, کاتز:
وزیر دفاع اسرائیل، با رد فشارهای بین‌المللی و هشدار به تهران مبنی بر اینکه هرگونه حمله‌ای به اسرائیل با نیرویی کوبنده مواجه خواهد شد، اعلام کرد که نیروهای دفاعی اسرائیل به طور نامحدود در مناطق امنیتی در سراسر غزه، لبنان و سوریه باقی خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/news_hut/66149" target="_blank">📅 11:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66148">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24ffc7435.mp4?token=FnTXZBvdHtK5eP3IRamk4mQDIdcyT9yL06kNfZX6pYCW_n-O2bJxmX7WER8irZBHfYa-ST-Ez1_TE9xW4vYG5njO7sVwpWZoawVVVRXanHtkfhli8EPDmIEYeAklwwdzyxi0ise9zbNwie1ctP950N58hx5HRbVXg2s1f-gHx0GztGW_k7Kwkys0TPTIlEcsYHq1sWpD-kqQdxknbaLiDEQLBgtb9uQMl-PLD4aue8DvcQmKA3pxdxjtric0Urw1VWPOz7phHB6N6mfs42dzqikBD2vE0PmRxz377YRkAkqufc9zrPw639u7pbWppnAyZ6pLQXXPfeVHpSnQXnQUMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24ffc7435.mp4?token=FnTXZBvdHtK5eP3IRamk4mQDIdcyT9yL06kNfZX6pYCW_n-O2bJxmX7WER8irZBHfYa-ST-Ez1_TE9xW4vYG5njO7sVwpWZoawVVVRXanHtkfhli8EPDmIEYeAklwwdzyxi0ise9zbNwie1ctP950N58hx5HRbVXg2s1f-gHx0GztGW_k7Kwkys0TPTIlEcsYHq1sWpD-kqQdxknbaLiDEQLBgtb9uQMl-PLD4aue8DvcQmKA3pxdxjtric0Urw1VWPOz7phHB6N6mfs42dzqikBD2vE0PmRxz377YRkAkqufc9zrPw639u7pbWppnAyZ6pLQXXPfeVHpSnQXnQUMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان مقیم آمریکا طبق درخواست قلعه‌نویی واسه حمایت از تیم ملی ریختن جلوی هتل
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/66148" target="_blank">📅 11:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66147">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPIZ9LWbiWBF3Z6kLgbgQ8wboL4Ki3kzdLdAtD8bPMoaN-dG3BqHLikuI76g2DZMk-RZhYgTW9UR4vSqTE4um6l2MNgm1XTrVP9AoNdt9aVinnaSMt5bfefNbRY2syO74Q1AJSy3uVoBavleJtAE1dGz82jmiYU9RkDxbuKFWCOkJGexkU1ruVFx4X-3hBpBNdQsWVddvHq3LZJ3WKjUFnRmXnzuF7JidfJHZYRPSyk74diTuSrbfjGL9PxMZ6QEM--LYy_XHGz1K50IBD9VkihgUvMuLBbpr8wafgxtNr9uxnvRixAwf9g6UKk_sBVM9VisZHjPm38gIgHxMbFLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت عرزشیا هم اکنون:
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66147" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66146">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSsKnTmBM_av6LoYELS5JUapGuvfsz1J0q38zsrTYf1dUpiATNxKCQ6V6CgK0_sawn_yiYqHQI-cO-LIFt_x8bm7j4_MbtL0Vm9JvqKIimMj3hfxBKZB8qmCMhjYU2thynotMObPfFcaAQenejpdVPwKIJTt3v1HiMkoII4W1SygUHO9WaeFFa143rpGLGEjl20n53J1eTAUwX7xG4o4hRAqgbI1KO3PHMoBNXv2xNZdO0Bp4cGZF30aKAbE59V65rKbbKlNIgyYtTb15U44d9kLwmrO-1c83ZupqAbpK9FmnDEbfHGEGJtlgqVFf93TaUsRmEGwQOz-ZN9Mdht5lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عایشه قذافی دختر معمر قذافی در کتابش:
به پدرم گفتن موشک و برنامه هسته‌ای رو بذار کنار تا درهای رفاه و آسایش به روی لیبی باز بشه.
پدرم همین کارو کرد، اما ناتو شروع به بمباران لیبی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66146" target="_blank">📅 10:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66145">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccd116404.mp4?token=lcJiCXoLsJTvnPgF_2rk9H82v7q5IGJZDJzRAzRSWvSahywckFOEx0EFb1UetSzjcX38X3W1SPxpZPbP1uqyOtXlfvZ8leahG53Dy1GgHE-OmMIcl7DjjWHDqs0lr-HqYEXbT5Xh4uCx1rjxAn8MsEda0NqY05zx-RwtTDyo9pc--fvMNwPY9rOsuI8MFE7cGk1SqMwFtumUbDIC3J_khlNH12nWq3lcHDhbK4NDTd-pYrc5s3cBN-8JlB0-YMbbWrkY9tRh0cZiyqPK8ikFACUP7IZQXbVm-d4j19GzsKN-RpOZ6v3wAzAucU0RrcyrtndmntO3wkuPrClPT3pi_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccd116404.mp4?token=lcJiCXoLsJTvnPgF_2rk9H82v7q5IGJZDJzRAzRSWvSahywckFOEx0EFb1UetSzjcX38X3W1SPxpZPbP1uqyOtXlfvZ8leahG53Dy1GgHE-OmMIcl7DjjWHDqs0lr-HqYEXbT5Xh4uCx1rjxAn8MsEda0NqY05zx-RwtTDyo9pc--fvMNwPY9rOsuI8MFE7cGk1SqMwFtumUbDIC3J_khlNH12nWq3lcHDhbK4NDTd-pYrc5s3cBN-8JlB0-YMbbWrkY9tRh0cZiyqPK8ikFACUP7IZQXbVm-d4j19GzsKN-RpOZ6v3wAzAucU0RrcyrtndmntO3wkuPrClPT3pi_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس معاون ترامپ:
من قطعاً قصد دارم برای امضای توافق در سوئیس آنجا باشم، اما ممکن است خود رئیس جمهور ترامپ نیز آنجا باشد. ما این موضوع را حل خواهیم کرد.
فکر می‌کنم می‌توانیم با اطمینان بگوییم که ایران هرگز سلاح هسته‌ای نخواهد داشت.
ما کارهای زیادی برای انجام دادن داریم، اما امشب یک پیروزی بزرگ به دست آوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66145" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66144">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4991d46b.mp4?token=f6tmPO_o1RTR9Vl_F0mWgkdiv251MDhX78zOREHSvSPmApHV2hXDD4szuDp1F9AAC2C4YhqOlXbLSk1vMmfPcjtXRaL2k6w946EeMbeNtd9ekYy5gaxFivoQ5UA22lA7Kq9T4Lq8gdvFKeBZRuYv_IHqWNygIZbxaysMSDOeifEUq47z9EDAdiF0-ggjDtBY7aAmlcuGg9YaExY-cwC-x4l_LSkxSWbuibXi7eDk-3m2fwDDzzIbsaf5SbfRrHP3lHroXmBUEp_BMeOOlDNq9cWwyBeTppTiol9FppHO3AT5dnzmeIL5YqXLxrS4CNrf1Ur68NTbSixkrHV5hn3-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4991d46b.mp4?token=f6tmPO_o1RTR9Vl_F0mWgkdiv251MDhX78zOREHSvSPmApHV2hXDD4szuDp1F9AAC2C4YhqOlXbLSk1vMmfPcjtXRaL2k6w946EeMbeNtd9ekYy5gaxFivoQ5UA22lA7Kq9T4Lq8gdvFKeBZRuYv_IHqWNygIZbxaysMSDOeifEUq47z9EDAdiF0-ggjDtBY7aAmlcuGg9YaExY-cwC-x4l_LSkxSWbuibXi7eDk-3m2fwDDzzIbsaf5SbfRrHP3lHroXmBUEp_BMeOOlDNq9cWwyBeTppTiol9FppHO3AT5dnzmeIL5YqXLxrS4CNrf1Ur68NTbSixkrHV5hn3-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی خطاب به بسیجی‌ها:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66144" target="_blank">📅 09:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66143">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
ترامپ به نیویورک تایمز :
اگر توافق هسته ای شکست بخورد، حملات نظامی را از سر خواهیم گرفت یا در ازای ۲۰٪ از درآمدهای منطقه، واشنگتن را به نگهبان منطقه تبدیل خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66143" target="_blank">📅 03:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66142">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=Doxdxo_d_h3z5v6cFsfr7LVwRQXOerNXQ6zWzEiB6LwnmLV29DuQSOCYaO3Z-oTVOKtuJSuWmdvY3ji9VQg7dg5iVNh6gkgU82c2oHsk8RiglFQWLGkUSseniYLcPylDy0wJAGGbCbWWNDz3orDhtERPghB6Zj6LRtwWqtrFHPUDqe2a5tT_8mExTghgoJs_pc-blm1JFvBKLXgxM_tsv8mCHmRIR0g_st2DvkZqFu6JMKU3OGQFaub3kcJ3P7MayXzwQ0HoqdXKGzusEG4qC6GGSAOZWE7J7JW1L2hUiYSCdovKJIfG1oFXPbthxLpnQz7a8Kz_3qBGT8zsPdHqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=Doxdxo_d_h3z5v6cFsfr7LVwRQXOerNXQ6zWzEiB6LwnmLV29DuQSOCYaO3Z-oTVOKtuJSuWmdvY3ji9VQg7dg5iVNh6gkgU82c2oHsk8RiglFQWLGkUSseniYLcPylDy0wJAGGbCbWWNDz3orDhtERPghB6Zj6LRtwWqtrFHPUDqe2a5tT_8mExTghgoJs_pc-blm1JFvBKLXgxM_tsv8mCHmRIR0g_st2DvkZqFu6JMKU3OGQFaub3kcJ3P7MayXzwQ0HoqdXKGzusEG4qC6GGSAOZWE7J7JW1L2hUiYSCdovKJIfG1oFXPbthxLpnQz7a8Kz_3qBGT8zsPdHqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم لبنان و نوچه‌های جمهوری اسلامی پس از اعلام توافق ایران و آمریکا
و عدم حملات از سوی اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66142" target="_blank">📅 02:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66141">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
جزئیاتی از یادداشت تفاهم ایران و آمریکا:
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
آتش‌بس کامل در تمام مناطق و خروج ارتش اسرائیل از جنوب لبنان اعلام شده است.
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66141" target="_blank">📅 02:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66140">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nToN9D3sGMXz-GcMiHdOz_TTI9qPxP8l2Dt6cp4E1Q0J8eVS4A9eX90zq1dSrBvcp7IRMf7EIWg5f2x9xRsxcOOWrUhbcxF46sl_sNO9U5aiuAf-78WxRoQu0fWPUFINaTiSfgBaKNPiZjR4WxCn5lHIIzP7zq2nLTN8r2AcjB80mznDe5MpL7gXF7vwkKzttFFP7HqKiJE_J1L6NbWtS3_9uq6F3pGJTHUUDeV-53rxdCHjhZMuH_gJ3sbgq9h2D977rJctd2u5n54hinQyLWLlypxo3ROhru3sTazJdBTyBrKDoRtBKv_bWe3N9A55nVveK5_5hZzL_gamPOmX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
این توافق بزرگ، صلح و امنیت را برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همگی پیش از من شکست خوردند. رهبران منطقه برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آنان در دستیابی به صلحی واقعی کمک کند. با بازگشایی تنگه پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66140" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66139">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66139" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66138">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frOPIMJ-exzuG3hp2xICYScYscvYr9Zpp9qcCw7nY2MrlUD0F17KFrQvT0b9C9DXW8UlQgYLC1WWoEoyXyzO_9sA5tyjTu0UslN6ZzC9XLFRTJB-JrHkpa1ESOreYnSm3E0J0lIBhWBaVwc1qhgU7URBXK9xkhynPfgAzWflIHc9aiuwheXc4k-LbAsZgDJZy8lUR6xLaoss7OZ6W5gu3zQa_C4dfVfd9hiDNz7MaxNQeDecZqFyU3I7522S6TM3GEonnqj1L50V1bFZnYa7h4AThXD9P-8BlD6LIZkr_7AOjPcQekP4hgqnDuR0a3IXU6kj-kDBtWK_Dwjcb_uiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66138" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66137">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nonGkhbGYWtRzBiLBQZHPHPvK6B14KreCJLA3K0nwccv2iGDxoPJItw-OsRYeIoxGj4WgWUrOvY1LMgzXRw6NA0pI3rUbfO6QqbP7GfNJXecY4UE7WKYQZixSzpsvMamvAAxLpIoG98LuKyuXc4-7wMCZ-8bH0FN5JvOrAvFccJPjk-PBlslfB4KFed6YcPUuGmfljl6lPV0aiPad0TQZF-oWyEGyDS730dSqnroM7ARofLBnPx7KIBwGRpFVyEeigwNZv_Fjy8ZeFCwFuG4VcFLo7CKjJkDdTE7qk0qwJye-xy1K_gJx2RghBr3BJvgJoTKx_H63d1YPZ7x2XLnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیتر شبکه خبر همراه با این تصویر
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66137" target="_blank">📅 01:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66136">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=Lx7MTuz4ygwZMru7pFTWorDN-rJ9_bBHatgC7aTNKeME4IpHXKRUS0gntt-lMTpmHoUDuRFeMi8LrbA3gHTlM-3w1T8441Gg_I4SDtRzG7noZtFHzi0VDbsIF5NXqCgEWOhcKPV8g7JCw2o385JTrj4UNAj2Yh-ykABV54qJYgHcExxvXbgIIj9IjIyxI9sVbhzavURflJz8K0LLcI4PAZH-I0vNs8GNFYzLEv0xEjL5KjNV6eXxhKmH5ZgWo-kXP81W4dZTKqPL7LbMYifg-gyGnG0EXSepPRw3tkHQpBs0lBMA4nRgkHBnABI_BXQgCMc8gSBvG35N7CAs3orupQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=Lx7MTuz4ygwZMru7pFTWorDN-rJ9_bBHatgC7aTNKeME4IpHXKRUS0gntt-lMTpmHoUDuRFeMi8LrbA3gHTlM-3w1T8441Gg_I4SDtRzG7noZtFHzi0VDbsIF5NXqCgEWOhcKPV8g7JCw2o385JTrj4UNAj2Yh-ykABV54qJYgHcExxvXbgIIj9IjIyxI9sVbhzavURflJz8K0LLcI4PAZH-I0vNs8GNFYzLEv0xEjL5KjNV6eXxhKmH5ZgWo-kXP81W4dZTKqPL7LbMYifg-gyGnG0EXSepPRw3tkHQpBs0lBMA4nRgkHBnABI_BXQgCMc8gSBvG35N7CAs3orupQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
علی‌خامنه‌ای یازده روز قبل از ترور:
امام حسین فرمود کسی مثل من با کسی مثل یزید بیعت نمیکنه: ملت ماهم بیعت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66136" target="_blank">📅 01:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66134">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=Aoqg-LK7I23gDpSZU2Ld-Jz2DfbOWP2g_gF2WPu_JYUJ-1bq1tcTC7yZVuHTvI6TsqV_JLJuX39kSebe-AkFLYGD52sO6ZPz-LTfDe6Nzonl_khVq2fK0SxXfi5Z_we8ZHETTqaft805iLQHycwZKYERjs6kYDzi0B0w6GLf_I-TwkXEb3zTpFm1xbiQ1oi5Po9hyreDWVgQf8ya5nm5Luozr-jetXBesJnzCXG8Bjg3ODxq1d53axc-pQoAb9hGv0NNnviXdrnUaanc7bGef1B1QaSMk9NtAzM1Jn_FGSQ7fLrmSNWjRvLKxAu_NEQnEhk_X6-wINVz_j63-Enixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=Aoqg-LK7I23gDpSZU2Ld-Jz2DfbOWP2g_gF2WPu_JYUJ-1bq1tcTC7yZVuHTvI6TsqV_JLJuX39kSebe-AkFLYGD52sO6ZPz-LTfDe6Nzonl_khVq2fK0SxXfi5Z_we8ZHETTqaft805iLQHycwZKYERjs6kYDzi0B0w6GLf_I-TwkXEb3zTpFm1xbiQ1oi5Po9hyreDWVgQf8ya5nm5Luozr-jetXBesJnzCXG8Bjg3ODxq1d53axc-pQoAb9hGv0NNnviXdrnUaanc7bGef1B1QaSMk9NtAzM1Jn_FGSQ7fLrmSNWjRvLKxAu_NEQnEhk_X6-wINVz_j63-Enixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگر این توافق جمعه امضا بشه تازه میرسیم به شروع سناریو زنده یاد مانوک خدابخشیان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66134" target="_blank">📅 01:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66133">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
‼️
دبیرخانه شورای عالی امنیت ملی جمهوری اسلامی
:
آماده حمله سهمگین به اسرائیل بودیم اما به درخواست ترامپ و پس از گرفتن امتیازات لازم، از انجام این کار منصرف شده و‌ توافق صلح را پذیرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66133" target="_blank">📅 01:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66132">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bd274791.mp4?token=bvyA4xteRxK0a6Yno_1w1QBSPG_ncIBxQq0WuKqp512rXTOEPWvEs8JA0Ezx-jlLWY0iAXGibhhWwLfreULIOcs5BCD3dEWgTuwIlKwSHzPPvST_13qH1eMSTqKT-JIbx3LkM0ZM2VD0ITyM3KIv9vIBpC5umrGOVz-rUQynei6v90sgIuxOY_pK_Ai9p_g0Ng_TEPh1IdYFJNAi4mlawhZAx40sBQ5ssTyspS1ITVBQG75aM_9AVwOcDQMYoGlR08fJhOp8FTV_nVnzoHBNgtTYKPMuUnZHI5lwtcfXTAkJDiGfTiknbJP3kuCMnK3MJZHgb_j7wnMNeN3qT-KCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bd274791.mp4?token=bvyA4xteRxK0a6Yno_1w1QBSPG_ncIBxQq0WuKqp512rXTOEPWvEs8JA0Ezx-jlLWY0iAXGibhhWwLfreULIOcs5BCD3dEWgTuwIlKwSHzPPvST_13qH1eMSTqKT-JIbx3LkM0ZM2VD0ITyM3KIv9vIBpC5umrGOVz-rUQynei6v90sgIuxOY_pK_Ai9p_g0Ng_TEPh1IdYFJNAi4mlawhZAx40sBQ5ssTyspS1ITVBQG75aM_9AVwOcDQMYoGlR08fJhOp8FTV_nVnzoHBNgtTYKPMuUnZHI5lwtcfXTAkJDiGfTiknbJP3kuCMnK3MJZHgb_j7wnMNeN3qT-KCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
دود سفید در کاخ سفید. طبق سنت، این به معنای امضای توافق‌نامه صلح جدید است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66132" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66131">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
📰
تسنیم: تا دقایقی دیگر مسئولان ایرانی درباره خبرهای منتشره راجع به تفاهم صحبت خواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66131" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66130">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3KVJoOh7BzKMyNl2S25KC9By8x0Ne3aoCBYpnp_Ews6UXzs9I-RVu7Vn7imzo_Row66Smr52p362un8o6byi93NnIyjda8Zjw0fSyxTgUV35ORldVVuA4KqQ-eGW4InbW-a7BVlpiiUentIdWCNNwCoNW1CxoAuzddgFxW4JlPLpRr8Sv-gTDsNEiCYFuZvDGRdxg38U79V6B-vc1f35G5M_hZFs0os_D88qDVps1A-cHyqKCMNSQfyZ7x9t8l6lu6zYkYnpk3uOXb6eEayMMUR9_0DeyE3nSBgXnyUB-2MN4t9HZY__HuhxAHnhA1n_uBXnbpnuDOemOo1HyVqjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
یکی جلو صداوسیما رو بگیره. چند دقیقه دیگه تیتر میزنه آمریکا رو نابود کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66130" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66129">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co6EiFZYJfMR3K4y_53eVLYJt95qpCQjdA99ZgJuDYGZgsNQ0StqEv66Z-lg9TXRrGP-EEwQYRhA_jD_Oewy6rmUUldUuFVsC_qN06pWwbTNlKlHOyK8GkN_Q8EwcmO9OXg5dUXYANPeWW1lHITsSVyJLb2ZJHg_vDhD7EKJlAyT-paSgiA-oeCCG80zF4GoOh3wMSgKd3whEv8MW-C3jot9AgmDaY5Tw6cKFzPwVng1Z6geceyCXQAq1qDpCxUZhphg3ZzKFdUTzJwwWpBdldiuHI7liLdtXcCx-QwHLaSoEV9OQinoTMPDtmHd2mbtbVYspAH-a3YzE-aL2zvIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب الان وقت چیه؟ آفرین حمله به ضاحیه بیروت
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66129" target="_blank">📅 01:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66128">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66128" target="_blank">📅 01:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66127">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFb6kYGslc9U1ukaw6Cx13FG6gooS6a8ZfvkbM_S6fFcn8KdHEq4WqC3ai9ct0HSeYKCyYXxFK2XNVgW_lA-e2RCZggx-HtdGbm82Cm6MJ1LZzMb1PrSkD0RUC2SfXOEcRn_023ZhAdPeEopkTvHd2y4-niiUF3jidtnH4erUAHetfQFsXVDktbcqGTR1zkc3-WXe4ytXvsB3TOEITWCjBY6N34paLQVAU4fNBps0MNEJ-pgHujCGhBiIzVoMQdve0F3lntk3VQXDdPzd5ioJ3N6CVfy9z20t1Zw1CP-FsnY8JfgKKVYZCVfKR-a7Vur8Vy1tJb7YLOdrB7l9obDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقام خون رهبرتون گرفته شد برید خونه حالا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66127" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66126">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=F4frzzq2UEVmLDFWOdgSgoyqcu1N-msfXSHU_vFLPqyAZnbyPN8JXwcDlNkCXBz9FIJ_yHTtWUVkA8T_tnZH4XTfMiWoMjrct_002DMGhYY6tWH0KsMurSVzt77rrvgBn0uzZSZPoTDMNrrO1rUc0hd5oF8jPREqUvV26a3Zr48OvHhpgQ13g-2tV8zX1Qghkowgu-E1JzsXmouZB2Iq9NvDfMd-uPUR89fJrai_b9828TypJZyW7qXKQsUAJCdpYsnOaYa73WMY822FvCmhMFxmR4RE1I0lP_kavZRgQnL5XZgkp-r7od0dgl_kvePaGF6p6YA9SWLUSpA5Au2FQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=F4frzzq2UEVmLDFWOdgSgoyqcu1N-msfXSHU_vFLPqyAZnbyPN8JXwcDlNkCXBz9FIJ_yHTtWUVkA8T_tnZH4XTfMiWoMjrct_002DMGhYY6tWH0KsMurSVzt77rrvgBn0uzZSZPoTDMNrrO1rUc0hd5oF8jPREqUvV26a3Zr48OvHhpgQ13g-2tV8zX1Qghkowgu-E1JzsXmouZB2Iq9NvDfMd-uPUR89fJrai_b9828TypJZyW7qXKQsUAJCdpYsnOaYa73WMY822FvCmhMFxmR4RE1I0lP_kavZRgQnL5XZgkp-r7od0dgl_kvePaGF6p6YA9SWLUSpA5Au2FQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش مجری شبکه خبر به امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66126" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66125">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBrv_6IML-DM1RgcB_FIA7p8qvPQ6gmMJ43UDafpfMXEsrjQr5HMqfPW7CkGD__yOWn3BMyFNgg8IllAI6TAtNFwCOhmpdXBKewy-856G12-hliBjpDa2wQUqglLxhPd0KXf7PCIqN9O1D2YGOZZZSthlwC-UqoYP7s1bltSYPooXtmPUvnrvxRXnmka7XbFY60S9KS0F_O2xOLY_PjCLeAcJ2RIk5R5GdZl2NzFZgzJaZlXAeQHSWQScD9l0U3sUmWJ81JIiSuqRIoU4_cqhMNL93W70WRO_0E2AtPOTYeSl-c9LKW9A2PfG1uGRk0C4qpIBRHqGGn8f3eP6j7ryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری
؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را روشن کنید. بگذارید نفت جریان یابد! رئیس‌جمهور دونالد ج. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66125" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66124">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQTKO9h-ch08lRYQaSfFLa6iizaU_0dLAQRSN5q9XLHfe2Y2jVEi1sfSN2qxc1ym40ILnrUKu3Y6J6mxFNYxwxFB881l1jTwZoDi_2RfFDHxGsfErnpZ2Lx59u1Nom872bCSPpeaQkmTZWBSNEGTKn3d-o5U0kCpnYgsWkmDSNcMtUsiuy8iYl5TSE0B5236oWCHAOt00bFf-1OJvfJB0lnbcQ4YP-NgddVHpDpt-eM1QMJ0Jb_6G-LPBhAc7UEFht5WcoeH5JrEMqB6ENutvNqdgjgqCIjYLQbF1zMnnFqgc5ZIvvb16oX3mhbx8RlSaQI8dmQsX2xP6KN5mNoVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زیر نویس شبکه خبر:توافق با آمریکا انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66124" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66123">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
مراسم رسمی امضای توافق روز جمعه 19ژوئن در سوییس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66123" target="_blank">📅 00:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66122">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇵🇰
🇵🇰
شهباز شریف نخست وزیر پاکستان:
پس از مذاکرات فشرده، خوشحالیم اعلام کنیم که به توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران دست یافته‌ایم. دو طرف اعلام کرده‌اند که عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، به طور فوری و دائمی متوقف خواهد شد.
مراسم امضای رسمی این توافق‌نامه روز جمعه ۱۹ ژوئن در سوئیس برگزار خواهد شد.
از ایالات متحده آمریکا و جمهوری اسلامی ایران به خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای این منازعه صمیمانه تشکر می‌کنیم. همچنین از برادرانمان در تلاش‌های میانجیگری و رهبری خردمندانه کشور قطر برای حمایت‌شان در رسیدن به این توافق قدردانی می‌نماییم. به طور ویژه از رهبری خردمندانه عربستان سعودی و جمهوری ترکیه برای مشارکت‌های ارزشمندشان در این زمینه تشکر می‌کنیم.
پس از امضای توافق‌نامه، میانجی‌ها تسهیل‌کننده سلسله‌ای از جلسات در این هفته خواهند بود. این بحث‌های مقدماتی پیش از اجرا، پایه و اساس مذاکرات فنی و مراسم امضای رسمی را فراهم خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66122" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66121">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
نتانیاهو از این توافق حمایت می کند و این برای او خوب است زیرا تحت هر شرایطی مانع از دستیابی ایران به سلاح هسته ای می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66121" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66120">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
محاصره دریایی اعمال شده علیه ایران موفقیت‌آمیز و قدرتمندتر از حملات است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66120" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66119">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
من هرگز به تغییر رژیم در ایران علاقه‌ای نداشته‌ام و در حال حاضر با گروه سوم که منطقی‌ترین هستند، سر و کار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66119" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66118">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: ایران در ازای توافق پول نقد دریافت نخواهد کرد، اما ممکن است تحریم‌ها کاهش یابد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66118" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66117">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به وال استریت ژورنال:
ما وقتی آماده باشیم، مواد هسته‌ای را دریافت خواهیم کرد و این اتفاق ظرف یک یا دو ماه رخ خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66117" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66116">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsWlZQUzPUEoc4jIjnVGh_CYSMtuz3oDRP1uRzMhmfsYkREoJBZyXcam-8OPlCXGn5v5QXFjd_xo379o4ZCIJiOrTFGPSVVbG3Mvvc0iw7A__ktf0Yry1ueCACI7FDv9UfQHIu8vNugBuW0J_Q3cdExON3WlyfLMJibId7YBXLbD219QqNzV-m9P1EF8PIQlE6vq_OsSkhAIPhcgZ0ikjl9n4jmX-dkqmCSBKB_uLK2btXubOGN53JB6gFfBpfGurtS5b63ZV2Qr-VZOtbOnVj8agdWiGPprbhkSRkH3YLFRNmeLVc11WyAH_dhytJMFx-f72K41umk-S9s-gq3YFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محتوای تماس بی‌بی با ترامپ:
#hjAly‌</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66116" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66115">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ و نتانیاهو دقایقی پیش به صورت تلفنی گفتگو کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66115" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66114">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
ترامپ: این توافق به صورت الکترونیکی، یا توسط من یا معاون رئیس جمهور ونس، امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66114" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66113">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به وال استریت ژورنال:
بزودی بیانه ای صادر خواهم کرد تا تایید کنم ایالات متحده با توافق با ایران موافق کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66113" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66112">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
#غیررسمی؛تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید.  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66112" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66111">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItoQ26Frr_nXwHvLCFhD12EyuyV4DXmoBrWyYrwd5khKts5oRY1Acv8ryGIUFK7XvlMgWzVvbQ5-5j476QTA3tNia0Uq7OBketPWqlIDLSW-rqV7UEzo1Ao3glM38Cx_gcEt47Y3-AbAWZqKxLQyU6H30oDVnK3bGoEWsJmC4KpErvcocC5Onl17lT-YufRuqUat2BxoL3ZKqqNm92V3ZuRYycBF3AeR-cOGUZGX4A2773aoIhhaMog2D0l8dI_0K9BmCDnEtrqaQX8B0eaEJpThfQHJaGfc1pN8t4Lvf-F2YFg--B3FeVMpkWrQt8VdTFgsUb5J3cFmp5CJU3yk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توییت وزیر کشور پاکستان: الله اکبر.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66111" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66110">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc582fcae.mp4?token=c7EIiLuRxMn8c2wXK0bW2YZNJ4HJJgUywZWBrZnPH9sPtwkRaWVP01v-VDzUAp6EXXej_HVuKYvZ-g0VpDq6al5p_HT9uRV0z69wUkbRXoawVkyBC1TUVyfJQ50iLSSobUHtLoVy8fudZmSEODZ-umeUQ__PKjOLOHHX2gPYRJbYjxu2N2b2lwLvLqj-gEDgOmC0dmuyykgHiHHFeA6BHnVoHc6sXSZPJE6u2JRXEalOMSUF7iIM1iS__lkZgEfs3Q662XYIStjix6Fnu4SU2Pus7NJZ5iaccqlwg_MoqvuKknpbfxQ3Er3lHWF3HflbV9BVtlqYrGG4jbVPGh5BlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc582fcae.mp4?token=c7EIiLuRxMn8c2wXK0bW2YZNJ4HJJgUywZWBrZnPH9sPtwkRaWVP01v-VDzUAp6EXXej_HVuKYvZ-g0VpDq6al5p_HT9uRV0z69wUkbRXoawVkyBC1TUVyfJQ50iLSSobUHtLoVy8fudZmSEODZ-umeUQ__PKjOLOHHX2gPYRJbYjxu2N2b2lwLvLqj-gEDgOmC0dmuyykgHiHHFeA6BHnVoHc6sXSZPJE6u2JRXEalOMSUF7iIM1iS__lkZgEfs3Q662XYIStjix6Fnu4SU2Pus7NJZ5iaccqlwg_MoqvuKknpbfxQ3Er3lHWF3HflbV9BVtlqYrGG4jbVPGh5BlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صداوسیما تو لبنان:
انشاالله امشب قراره ایران، یمن و حزب‌الله به صورت همزمان به اسرائیل حمله کنن و انتقام بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66110" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66109">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
#غیررسمی
؛
تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66109" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66108">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j08_nBwJWZhXuWkIdbhKdGVg6FBYFO23beQvRihgZRZczecV-oJUKoYQAtB-YJbTDEcX2bMCqBMitXDEdFdF--oWjfml-oMYTgyuAchZtw6dq0c-Cuzd0bSl6IhUb0sQYh5-v5KAN-veiVGZ6A_s7_r4OquSbPv7HSruZH4u7daxziJCH4rVq5UE6jSMN-At-5fmUV_a352HC3v6-y9b6gGwS--kV_pnP4CNkzJwywTjBETF7inBG1RMGFKL9VYrrrumBpASQr20j6to0az1HVsJ-ub7FsVmD2BggDUOfXkKVfbW97qSuyqBACV-Rr9WlN3xawMSN0YWnty2b5TnDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرزیدنت ترامپ از طریق Truth Social:
ایران هرگز سلاح هسته ای نخواهد داشت و تنگه هرمز به زودی برای تجارت باز خواهد شد!!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66108" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66107">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
#فوری
؛ ynet:
ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایران به اسرائیل جلوگیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66107" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66106">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">محمد باقر قالیباف:
هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛ مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی‌ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66106" target="_blank">📅 23:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66105">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بشتابیدددد که فاک بت آنالیز از بازی ژاپن و هلند گذاشته سریععع بیایید و ازش استفاده کنید
💸
@FutballFuckBet
💸
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66105" target="_blank">📅 23:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66104">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
کابینه اسرائیل:
اگر ایران حمله کند، ما نیز حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66104" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66103">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDoCvrRxPldayh6VaEYnCH1LtPQmmp6vfuI5n66lnZNlpf-WMolw-cOaIpwRniC5o-BbFIzwxRih0rTVhPs_QustwJ3DkM5L1eTE41NwT-tLO9O0yTv8w20E1h-xF3Z8SUzscWlNtnGpDlrltnYJOjnm9mgjx42wilaakYePgUZoOAcKBDgNcZJmnDd6xz1pwRdiHn6volRVa_XJyk8KGI-CuAB8LnPo-vZKBT-O0TbSol993U9LHh0jQOTlljncZ-wb7HiNlBJbVmK79K8SC1ybE1KyJZhdA1qRCsUM5fan3xv8w4rTrkeq8oHdTPtqm9OaJ0u9bjZj-w13wJsayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور هیتلر در ورزشگاه و حمایت از تیم ملی آلمان.
آلمان این بازی رو۷/۱ برد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66103" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66102">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJcFRD8zR_RvWCgNvwoFagThdyNRpdxldI9VpUeBwH_KJVbwPZ29iPrznNCayKKHvl5ij8M8TnhIt08AHuHV4mhAl3weJBgQUNvzm63pRz5BTuVmKCcS6f0n2PZT6d74OW_9IB_17dnutq8m-QuhoeJdXYCcONJK6n8e-hbGsi53UVlprVAYsN0Iu1jIUh2PwqlmiajDmZx4iZlVVcrdUHWZx-zjDmJSflGU2H7L2ZHoZqk4cTatEcpj5yf4n5bv6o-uMhs6CMFM9LcKI6Grepx3uXB4BeV0yDxzumGZGTrlIK6AwmKwvbgOUB-lWJ6mgsjXgwdorcdpeCs1qsVuzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛ مجاهدت‌های رزمندگان غیور لبنان و دیپلماسی مقتدرانهٔ جمهوری اسلامی ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66102" target="_blank">📅 22:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66101">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
به گزارش Ynet:
نتانیاهو درخواست‌های ترامپ برای توقف آتش‌بس علیه لبنان و عقب‌نشینی نیروهای ارتش اسرائیل از این کشور را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66101" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66100">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری تسنیم: حریم هوایی غرب ایران بسته، و تمام پروازها در این مسیر لغو شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66100" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66099">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0112560fb5.mp4?token=jHNhy72UP1PDV85PzUTSdxZ_yg3ciaDadURBBVJ4-IOOuNOGIyZYY7VIhXHTWHycaImwAzxr1OIqJdHH5WWW3wTp1w_LrP9kZArCEOvy6hzCAg260c2Rm0GnSHuF_imh0qlk3GMrgKsZqMi2Id0tvxXFCXqpXMVtNt1Zw9VhlduBCc-8XKPMfWORM5TtmhCUdgneQbaVeOrGDbv7RHV6OgRdAUytCcRL-_LVtW0UjYiJie34FQTQ8RNPqzd9iUuZ4J8Kf-eppeng-uwUAXOq5FcO3dVjZKqMVNLgUbNMJXp_-a1p-6CjD7UIm7u5WOJpmKqYOnbMO-cxrPN8o8P_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0112560fb5.mp4?token=jHNhy72UP1PDV85PzUTSdxZ_yg3ciaDadURBBVJ4-IOOuNOGIyZYY7VIhXHTWHycaImwAzxr1OIqJdHH5WWW3wTp1w_LrP9kZArCEOvy6hzCAg260c2Rm0GnSHuF_imh0qlk3GMrgKsZqMi2Id0tvxXFCXqpXMVtNt1Zw9VhlduBCc-8XKPMfWORM5TtmhCUdgneQbaVeOrGDbv7RHV6OgRdAUytCcRL-_LVtW0UjYiJie34FQTQ8RNPqzd9iUuZ4J8Kf-eppeng-uwUAXOq5FcO3dVjZKqMVNLgUbNMJXp_-a1p-6CjD7UIm7u5WOJpmKqYOnbMO-cxrPN8o8P_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعار تجمع کنندگان تندرو
عراقچی بی غیرت اعدام باید گردد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66099" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66098">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
#فوری
؛لغو پروازهای غرب کشور تا اطلاع ثانوی رسما تایید شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66098" target="_blank">📅 22:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66097">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml6mz0re7uhsXptWl50x6qs1x0tAgPIvzTSqLsbvKGv2QBGEHvPsImj93fEcwhCCbJOkTxV1jW3u1aCno3PLQ7pdnG4LHlbQLpuSMrug9zZFKo8O-_sCyrS1pFkay9qLX1pjxOWF6jd59CWZIt6tydMLGfpCjfV4PNsMyJa4ldLTckqCrMFJWS1OR47sYUK5jl56Mf6fn1c_K6F6Z6kK3c9XKE2GSEXsWf0IJ9Sm-PA2uLL02FoZi0exJJy7pOyIlJTaj59GQOa1t22r89MJNj3wuB_urwYc59U1zXVxBgz7dspcsadXG_G5wT4EYUh2lVYOi4UmBvVDfP03Q_hR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به نظر میرسه ایران حریم هواییش رو بسته.
«هنوز به صورت رسمی اعلام نکردن»
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66097" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66096">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ افتاده به دست و پای بکن‌ ملانیا (سردار وحیدی ) و ازش خواسته به اسرائیل حمله نکنه #hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66096" target="_blank">📅 22:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66095">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
حنظله:
تا ساعاتی دیگر، آغاز خروش آتش های سریع و خشن، به نقاط جدید الکشف حنظله در آسمان تاریک سرزمین های اشغال شده، هم اکنون به پناهگاه مراجعه کنید. شاید هنگام فرار حوادث دیگری رخ دهد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66095" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66094">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
یدیعوت آحارونوت:
ایران خبر درخواست ترامپ برای عدم حمله به اسرائیل در ازای مزایا در توافق را رد کرده و گفته است که به اسرائیل پاسخ خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66094" target="_blank">📅 21:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66093">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
زیرنویس شبکه خبر:
پاسخ به حمله اسرائیل قطعی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66093" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66092">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXUwp8tKAi_1zBIOYVQXVix7xCqK5SJe5sfYytfo-iGQoi7zuUs23ELiOxDFav97PRY5dAlypwlDERarei0yPE9Q6nQzoMggRBdRngPSdAixKPNbgOxMtUfif4lybY_POZxlb_qEV20agzqvYpqJWbxWXAZP712OrbynmIcLwhZtcTy7qe6BIoSFDV5Oz8cD7PTyjNgfDSK4rNDUhQctdpHXHDSelVr5zJJQ65wTSlot3TUQrw9Pfof2Po245bFzEurCeaKgyixLOAM95DDZ3wZ93b99nDxNT0H-63pLJO2uGmQLu0JCcd09D_zJXs31-4oleGXbgPTB7UXu1I9MPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدباقر ذوالقدر دبیر شورای عالی امنیت ملی:
‏
پاسخ رزمندگان اسلام در پیش است.
وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66092" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66091">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ افتاده به دست و پای بکن‌ ملانیا (سردار وحیدی ) و ازش خواسته به اسرائیل حمله نکنه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66091" target="_blank">📅 20:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66090">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7T7_Pg-dOtqsFk3cQr_hpYo18Z4g1V2RWnFV4EcxFlx-dP5YW7xLm1Um24ol8lsyYsK1AqB6AjK28cdCoD9JG18pz_oMq7brLXh2ZOk9LNp9VQUqYRysSujk-GUBgVxKIke_YiHFlGx5582NmAwPOPH6eomzrtp83wlqv_U8qrLoxNOpeqFCW-kX-uEbTH9JCa5d49iCMbGXZnJmVmN7Fm2lTsVFfoJjtQoDQL8X7wZX9Ktpzw9y8TCfoVdbnsXgUYiidchSVOpDNjT_h-eFsTr0jr9gWhVQit3E1FIKm2us-P_XvqizX9RZ8kvW8bBoVW0gJv6NLM_ZA2anQJehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل قطعی است
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66090" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66089">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66089" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66088">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VembokfbIeDeoO8ftFixAMoF7KhzrqWN9vSeZj3rsP9qeM7QZEsY3HQumJioGKxbKIlUqauB-pVvY6YBqJSrOWPGC41m8B1LAvdltcAOP3O3Sn8QiUXO04nxnqLvJ4V3cW9HiFiaiEXfL40NtNe9ZPBZY_llAETiw-3JIen7H0tAKhi8DHjqJ0Qo43-VVkc0FEJor-WlBlphfxIyAh7SUSZouyHNa_WeVHKrMHUFp2Ls5JOl8VGi2ha1g0WFG7fGbyclAMMvwLGt0h8ALB84EQ7SDmTCeOLCNDAjzc9UnWnz3G0z2zBNqHRZIXokmM45M9k5vBfK8uxNazy9tM1h1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66088" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66087">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a73d88cf6.mp4?token=Nt16g3moeBNtilo5M5AMiEFoeohh8WsoBqMQ8izJoQdJbS_cCA_RjJBnz10QMN8xji_Fcpp7UyYbhv4qOL0YGoBnQamTxnd1DJCk7dxASDCELcFPVHQzO8gcwnrvyH2gqoITYhdsnuL8Zxa8jRsjA1OQX9hfKdBQxAYIg6Q8OBIugklnSTjuZ1ppobOin4YUur3YLM277CgNR73dskl7HB9kxPZKaAAR8OWFL5dDNLZx4qoNvZZcTme6SICC3AU1g4rgv7xHVQIP33q2yLvubyO0auoZddUoTHsWR6DONJL-QPU42ac8p1OW489sIxfp7J0LLINqt_TqxN5gf38HzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a73d88cf6.mp4?token=Nt16g3moeBNtilo5M5AMiEFoeohh8WsoBqMQ8izJoQdJbS_cCA_RjJBnz10QMN8xji_Fcpp7UyYbhv4qOL0YGoBnQamTxnd1DJCk7dxASDCELcFPVHQzO8gcwnrvyH2gqoITYhdsnuL8Zxa8jRsjA1OQX9hfKdBQxAYIg6Q8OBIugklnSTjuZ1ppobOin4YUur3YLM277CgNR73dskl7HB9kxPZKaAAR8OWFL5dDNLZx4qoNvZZcTme6SICC3AU1g4rgv7xHVQIP33q2yLvubyO0auoZddUoTHsWR6DONJL-QPU42ac8p1OW489sIxfp7J0LLINqt_TqxN5gf38HzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ به خبرنگار فاکس‌نیوز گفت انتظار می‌رود ظرف چند ساعت آینده توافق  با ایران حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66087" target="_blank">📅 19:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66086">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm6VUGTcmbBWwPzl4iiwvAsr5veYZhZXPBHtkCas7-J6qEXRR08uI0tquieUH7DU3B1QNJMd89DFVM1qzx9L1gB7C3eYlMVAkSKnRAYW4DF-YQXSKCRD1Go_cvExMNlXi4x6MWM1t_I-ctKejoy8PEOlO4Ii0c0YJWfAbVNwp7L5zq9zOV4QX9E13XoljkaRUEQ4k2psQwp4iV7Wlu3o3OcrUgt2Y4_aVOk9wYvIAECCc_xs5ieykMujAUWPiz3NaT-v8HXZPCyG4dlfcD7AfnwxfyBd0DUDwcHQK_rvwIg0_g8EoSW8OZuMARdlH-WIgviOtTWths9JBq0EeTHDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید: رئیس جمهور ترامپ در یک مصاحبه تلفنی به من گفت که معتقد است علیرغم حمله اسرائیل به بیروت، توافق با ایران امروز امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66086" target="_blank">📅 19:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66085">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پزشکیان:
شورای عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
رسانه ملی در حالی بیانات رهبری در خصوص عدم مذاکره را مکرر پخش می‌کند که بنده در مقطعی با ایشان درباره ضرورت خروج کشور از وضعیت فرسایشی "نه جنگ، نه صلح" گفت‌وگو کردم و ایشان نیز در همان مقطع مجوز پیگیری مذاکرات عزتمندانه را صادر کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66085" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66084">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVc9fIKRFyVbj2czhPRGB3jP2Qs5YNqn90P0W2U2CwJnZQdkqL__P-s1MRekNT1KeQzh3zBiNobPUbuqE6gq2JQD3EGcJqRKd1jh-Srxhbm2aZ_lwXbFKSkgziNXYmgZ4kV5_ccLZ5WaRRzkgnKwd8slVExo5EWZ0ni9JjaGcrozalpnHVPj7aBTvuhTl4q8aj98UAD45bIsUwqLrnpHAST5RAjqUWxCArIyqTWSR_G-1ZcKXlG0X0CpMIgh1o14nB-0HBxPva1BsJzTOmhY5B3JF_zEa9gA1Szpf2Vlrgxv3mrTOfCP4bUx_CogyB6Ro3DnD_S46KbRQmZaqJzOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ در مورد حمله به بیروت:
«این نباید اتفاق می‌افتاد، ما به توافقی که صلح را به منطقه می‌آورد بسیار نزدیک هستیم. بیایید آن را خراب نکنیم.» او از همه طرف‌ها می‌خواهد که عقب‌نشینی کنند و حملات را متوقف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66084" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66083">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
وزیر جنگ آمریکا به سی بی اس:
انتظار ندارم حملات اسرائیل به حومه جنوبی بیروت توافق با ایران را مختل کند.
ما در مسیر امضای توافق با ایران هستیم و مسئله این نیست که آیا این توافق را امضا خواهیم کرد بلکه مسئله زمان امضای توافق است.
اگر ایران میخواهد این موضوع دوام بیاورد باید افسار حزب‌الله را مهار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66083" target="_blank">📅 18:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66082">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66082" target="_blank">📅 18:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66081">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66081" target="_blank">📅 18:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66080">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
احتمالا طی ساعات آینده ایران به خاک ما حمله کند
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66080" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66079">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu_vmXJ6b1UXh_-8ydGYr9gf1msJWQT-JKMOrAiEpDNetCb9jXPFUWIRTCzUF47Vj8sK17-TY-tJGwBw0lhCmujr1hgCZcsN6k-jA4kSOZj2ll2KU446GlpxKlGvksZF1qCGFkBVXLESjzTpFtNtOcfEDgV-kqhS1Sr5Z0b4adD5ls0Y_cNDLwUQxsk-bYH_vrPKQVyEbFRzrK4qFyX313VDZVzbQObRvKI-19AvfSnaZQBFRSjosmDc-JnXCbEIAskFgyE8VEovCpNlreieyL4BJ0xcP4yIjWb6mKJRFxckvTlP5qk7Bm9TP7PpqB1pq-C4aMwq-Dm9ItDREF7Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی:
حتی اگه توافقم بخوایم بکنیم باید اسرائیل رو بزنیم تا ادب شه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66079" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66078">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyj3Nwo_2-mbny7y3i1XpIbaGG1WOZI4xv1bf11D1oneEDH_v1Qo3gXMgOYXpky4GhM2qx01DOoGlFyAWYlJhnr0HIVoM4yW7moGFPdfWiBjaYIPablmFzfk_qekNrzPv4sVmC-xVGGhxfhHkZoeAAfsxlMs2Dp2rW0Mr3-eMIgsgVuw9vAZlJe1Amt4z7Cn2cVjhpfzyWIjxrD0qAO-FhyKSjM6gPEPp4TKE-MoQ8ajXMyaOoKYHpChlCYyUy5LM1rkhINJyRYrpB6P66Z_i8tmd5_yU5JqPow7LZV4AqramxDU5ISYg0XX8Mz9KLyXkGwpL5ZydqiJNDtFtD5i5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگری در کار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66078" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66077">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e954c10201.mp4?token=mkjr6jVhM1aPr5IOlVnXysLZGDkGBx8eMRHvPVNWls1e7n16ZSJtzz6rJsBJnPVAF_H-qCOUsd8NjkhE9qy3omA5sg76zQVCRq5J8IUeVqvBpzK2tlPO0lyKOsJaUBAhYewDI3fJURY2YctXa20EZNReGJAESgidOTbWjVZ85cICm61J9pD7Ef4HD1RQDrBRA3EQ9q6rtL2QGAKF6fvWhbZCK2Y-0I9pV7xh8dBVvMK2ziS04FihfeHypxon51yg7IAIfumpRmLNyOCt1yiEFgyad5zTmKmVlfsU1pGADsKE-ZHI6_61-LhgAmplVA2XS4jQn9G7NUfldKMIKfYv1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e954c10201.mp4?token=mkjr6jVhM1aPr5IOlVnXysLZGDkGBx8eMRHvPVNWls1e7n16ZSJtzz6rJsBJnPVAF_H-qCOUsd8NjkhE9qy3omA5sg76zQVCRq5J8IUeVqvBpzK2tlPO0lyKOsJaUBAhYewDI3fJURY2YctXa20EZNReGJAESgidOTbWjVZ85cICm61J9pD7Ef4HD1RQDrBRA3EQ9q6rtL2QGAKF6fvWhbZCK2Y-0I9pV7xh8dBVvMK2ziS04FihfeHypxon51yg7IAIfumpRmLNyOCt1yiEFgyad5zTmKmVlfsU1pGADsKE-ZHI6_61-LhgAmplVA2XS4jQn9G7NUfldKMIKfYv1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت اعراب حاشیه خلیج‌فارس توی این جنگ
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66077" target="_blank">📅 17:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66076">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66076" target="_blank">📅 17:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66075">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه!
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66075" target="_blank">📅 16:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66074">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a237733a.mp4?token=nBt2auEl0Th8EoEw8-dO_1K6KYx0iCTJFS8ushh13MWq0KY-Klh3I3VuOCCUWxXjlU9faUseu3klvANON2vjYDRisezEoFgBcmYL8Vo0R56k1_IOkBC_8kwTAibh7R1J1mLjI5ij1bbjhyoQ6M6s410p_HGHBv1IIhXS9gZz3PlpwAYPOmsIecWPXrpcn-uJ5qg6HEOHqx2U7YODQ6SboZ99bxkSdz8skHnVYhMs9d0HQiDX7aCVaDbsBP0POw5Cg5Vaz_uACmBjZ-rVp_AMlrEtVt2oYvPp3_0Z19yaVaNA2x1botiIkBjMhBjgD3nNXgQPia6i_J5x3DrGkGipUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a237733a.mp4?token=nBt2auEl0Th8EoEw8-dO_1K6KYx0iCTJFS8ushh13MWq0KY-Klh3I3VuOCCUWxXjlU9faUseu3klvANON2vjYDRisezEoFgBcmYL8Vo0R56k1_IOkBC_8kwTAibh7R1J1mLjI5ij1bbjhyoQ6M6s410p_HGHBv1IIhXS9gZz3PlpwAYPOmsIecWPXrpcn-uJ5qg6HEOHqx2U7YODQ6SboZ99bxkSdz8skHnVYhMs9d0HQiDX7aCVaDbsBP0POw5Cg5Vaz_uACmBjZ-rVp_AMlrEtVt2oYvPp3_0Z19yaVaNA2x1botiIkBjMhBjgD3nNXgQPia6i_J5x3DrGkGipUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی نماینده مجلس:
اگه میخواید این تجمعات شبانه تموم بشه باید انتقام خون نائب امام زمان رو بگیریم و این انتقام تنها با محو کردن اسرائیل از کره زمین به دست خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66074" target="_blank">📅 16:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66073">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRdwdKwW82bdnnGPIbHwlSHfBdzeKmHXaEVVcg1NcqEUabjoac4Rt1V5kLOYn6jhSx1aAT05uxbo3LZ9RfppTzc4bH29TSHm8uxu4CmvN-ZD-nRGU4eWnsX8PWcI3WFzdEX8jmBD9dQhjEcj7L2czJLKbDqtf2lH79rTIxwS0Ydnu4YgFlFAv07TTpW49Zqnn0NAV7zwYtr4W5XgNoNtGn1RbiMlm4iBQ8fFSXYuw-RHOPjB0j9YXp1pEOrT_z-DRO5Mn4d9dU6Fx2cgCFtR_htexaRXi0wMBOuqVhUaDmfj8iRbE6MKXGI4yEt7zhguyAfjWLPxzgcMyyGBZKpU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
تجاوز صهیونیست‌ها به ضاحیه باردیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را. با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است.
اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66073" target="_blank">📅 16:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66072">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از مقامات آمریکایی و اسرائیلی:
ارتش اسرائیل،فرماندهی مرکزی ایالات متحده (سنتکام)را اندکی پیش از حمله به بیروت مطلع کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66072" target="_blank">📅 16:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66070">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=cOwYRud7o3kqubKpUarx8ZhJMWqH2YCSd7Yxdmtl2KBfAK7DtT3ZLSs3OhjQwkWggcxGMzOmFUX2HeNGB4QbumdEvLRQf2UlTJFwiQD5nfMyP55vN7MSRw3qwalHRRaarY9ib5gWWCF2hAB1p0aSJjRBuqgD-fnDHupj8vydd-SQHwtt2FvdXU8RF1ypC98a4IZjCHyNO2G55hxC767NNYwIEQQAfialrrYC16KHK8sU9VFwDH2b_K1DjTl4nB6oMnjFNsnp6r3YKUTnwViWmz0OD03Ub-oPQkH2KdnrfNmACLkZcPCbsD44wmD5Wz0tlKOF2gP5DJEbnWQbNruHoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=cOwYRud7o3kqubKpUarx8ZhJMWqH2YCSd7Yxdmtl2KBfAK7DtT3ZLSs3OhjQwkWggcxGMzOmFUX2HeNGB4QbumdEvLRQf2UlTJFwiQD5nfMyP55vN7MSRw3qwalHRRaarY9ib5gWWCF2hAB1p0aSJjRBuqgD-fnDHupj8vydd-SQHwtt2FvdXU8RF1ypC98a4IZjCHyNO2G55hxC767NNYwIEQQAfialrrYC16KHK8sU9VFwDH2b_K1DjTl4nB6oMnjFNsnp6r3YKUTnwViWmz0OD03Ub-oPQkH2KdnrfNmACLkZcPCbsD44wmD5Wz0tlKOF2gP5DJEbnWQbNruHoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم اکنون واکنش نتانیاهو به توافق
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66070" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66069">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">طبق گزارشات رسانه های لبنانی حداقل یک نفر کشته و چهار نفر در طی حمله هوایی اسرائیل به ضاحیه بیروت زخمی شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66069" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66068">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66068" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66067">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=R0cKYo1phU4_ZaKtGSk2ryvfzGwnJItDDVhvHk03DdNjzALVNvMXknOqtYUeM0xa89CW_lEasHkL6ySXEi06NnlvZRQuNLxkdjGY9Uor0lXovKeHOmg5sDrpKHUxcSTjk8iS3GMz4UbsKxX_I61YM1xZMR_YUtpDyAUJbnrICQWYu3N3qdJuwfGPwC3AU1q2DxnYEKjfguHgQAI17GCsmfeRWt8LpnfE5a3bxKgVZ-iSc7fGMWgVFLxR8-pUiEfrRDzwDQ-8glR-A2gjWUoJyinq_iVktNVms-Ago1tmSqXTDlIWdxHT2peNgJke933KgxuqJpnPSCS85U2f-G3iBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=R0cKYo1phU4_ZaKtGSk2ryvfzGwnJItDDVhvHk03DdNjzALVNvMXknOqtYUeM0xa89CW_lEasHkL6ySXEi06NnlvZRQuNLxkdjGY9Uor0lXovKeHOmg5sDrpKHUxcSTjk8iS3GMz4UbsKxX_I61YM1xZMR_YUtpDyAUJbnrICQWYu3N3qdJuwfGPwC3AU1q2DxnYEKjfguHgQAI17GCsmfeRWt8LpnfE5a3bxKgVZ-iSc7fGMWgVFLxR8-pUiEfrRDzwDQ-8glR-A2gjWUoJyinq_iVktNVms-Ago1tmSqXTDlIWdxHT2peNgJke933KgxuqJpnPSCS85U2f-G3iBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: رسول خدا و همراهانش در جنگ لت و پار شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66067" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66064">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=vmC_IjS8oUbm5P636tYdTR1B-TadujUzxrkb_KFW1VmLqEJInoJmykZVYMLJa5Cs1zS2Mcurki50vkZw0F2ZhforvMtMxTAKVK7XBs_b-Ld1vRIYUx5gaaZea-6bcFBWUWj0X6ZubSelvlj6GAQjbuIwca8w8lhh8BJwDNLCuo5U8DxaEFI8bsh5n36sBE5xjUJ2AnH6qFWg6jIjpI63CphPiyznM4PMEqcVavskCFTbxqk-ikN_-4utt_8b18A7CSkb5qvawYga6KYCdV34DUYNq4YB5t-IjvImnO8nGYWHRCQTzkbEDEW3pahrVyPy-4mIFh6rXDdjvvuD7jLO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=vmC_IjS8oUbm5P636tYdTR1B-TadujUzxrkb_KFW1VmLqEJInoJmykZVYMLJa5Cs1zS2Mcurki50vkZw0F2ZhforvMtMxTAKVK7XBs_b-Ld1vRIYUx5gaaZea-6bcFBWUWj0X6ZubSelvlj6GAQjbuIwca8w8lhh8BJwDNLCuo5U8DxaEFI8bsh5n36sBE5xjUJ2AnH6qFWg6jIjpI63CphPiyznM4PMEqcVavskCFTbxqk-ikN_-4utt_8b18A7CSkb5qvawYga6KYCdV34DUYNq4YB5t-IjvImnO8nGYWHRCQTzkbEDEW3pahrVyPy-4mIFh6rXDdjvvuD7jLO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که ارتش اسرائیل از حمله به ساختمان حزب‌الله در ضاحیه بیروت منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66064" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66063">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
کانال 12 اسرائیل به نقل از یک مقام امنیتی:
این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد.
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66063" target="_blank">📅 14:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66062">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
کانال ۱۲ اسرائیل:
هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66062" target="_blank">📅 14:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66061">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیشب تو بازی قطر سوئیس، یکی از هواداران(خانوم) شرتشو در اورده بود انداخته بود وسط زمین
⚽️
@fotbal_xc</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66061" target="_blank">📅 14:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66060">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=JaG8gf4hD-SJbHjlABlWhoDoy8AltK2JuLyBSEwB0qi1Q6r0HQLsrrUc4KGYjhBcwLe3YAzXj0hTlhebKhkgTpf2yZl2Iux8JFyYm-XO7g87Pjj0DjNjQ2xNhBakB_r8vJPppmuFaqBmxFkzDydmXctdX73GXZrIEqa4cJz0-Rl2cuzQSdLaiU28QSCLuJyxM8kAqrk7AYnr8hBmaUzXhB45ttoEgVcdT0DjFHoJ1VmoYv1T5Orq3FACepm8JEveVv3DB8N_L78ZTn3uuPX0ocjGPcsTuaAg49UcJZiPCfkQHDk9RNfdOMFazMBcQDgbVgUtFz7qttOXQmXMizuhiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=JaG8gf4hD-SJbHjlABlWhoDoy8AltK2JuLyBSEwB0qi1Q6r0HQLsrrUc4KGYjhBcwLe3YAzXj0hTlhebKhkgTpf2yZl2Iux8JFyYm-XO7g87Pjj0DjNjQ2xNhBakB_r8vJPppmuFaqBmxFkzDydmXctdX73GXZrIEqa4cJz0-Rl2cuzQSdLaiU28QSCLuJyxM8kAqrk7AYnr8hBmaUzXhB45ttoEgVcdT0DjFHoJ1VmoYv1T5Orq3FACepm8JEveVv3DB8N_L78ZTn3uuPX0ocjGPcsTuaAg49UcJZiPCfkQHDk9RNfdOMFazMBcQDgbVgUtFz7qttOXQmXMizuhiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چندساعت قبل، اصابت پهباد حزب‌الله به منطقه ای در شمال اسرائیل.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66060" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66059">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66059" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66058">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=sSNv9tIHw9LOIIvZbJZE11iANGI9YNoBEKqdoFlBeUrpbGjhyYwIgNQn9vGNWIz1F9WkPS3SwDnEBJoegdarUQwgHdycHkc2fHdRljf_o00HZb1WeNNpAiCYC1uhA6oIut49KMyoofNGur5xR7-ErbFHATgiunEPci1HxiEOD2blc_COniR--T_0TfAAZtGCpft6D22f7S2QyevSW9-wNHXCARRfXIbr3VoJZd7Jfg3M4CQMXtep8H0_5gQj2U2MwC8AV1LcBIMcn1v_HnxF6qMJZ-SL2vgnt6r5-6pBRRIWAoHuuUemSXt_6i_u5KyRBiRHyICD-bjEp3Puk40iTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=sSNv9tIHw9LOIIvZbJZE11iANGI9YNoBEKqdoFlBeUrpbGjhyYwIgNQn9vGNWIz1F9WkPS3SwDnEBJoegdarUQwgHdycHkc2fHdRljf_o00HZb1WeNNpAiCYC1uhA6oIut49KMyoofNGur5xR7-ErbFHATgiunEPci1HxiEOD2blc_COniR--T_0TfAAZtGCpft6D22f7S2QyevSW9-wNHXCARRfXIbr3VoJZd7Jfg3M4CQMXtep8H0_5gQj2U2MwC8AV1LcBIMcn1v_HnxF6qMJZ-SL2vgnt6r5-6pBRRIWAoHuuUemSXt_6i_u5KyRBiRHyICD-bjEp3Puk40iTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66058" target="_blank">📅 14:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66057">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل:
حزب‌الله با نقض آتش‌بس، سه موشک به سمت شهرهای شمالی اسرائیل شلیک کرد و ما در پاسخ به بیروت حمله کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66057" target="_blank">📅 14:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66056">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6OPE7DkoPcRwUAlSSGsRSa1tETY6SysW4LJ8HS1Am8mIUIb4ODNSG6wEaWeMnrmiHOn38SIpq35bRp4V_rlEO2ar6rqsvVr6wV8thVbIS0xeuyanRhCf3VjaXaX8-yv4hOZTYwyaT-FTQNqhAELAEkCQD5TtZGySxl1aOx7AhECyKSOXXviPCVNHS_rN0zb2Tl1mocWtW3376J-SAveIn6_Wg0xH1s0LWxJTl2GVc4l04AxYoSS0bIR3rj6samNSbNPqx45BKjTJVPMzokFYK12aF7NN4BUWvrd3GcoVTGGm0-6nkwZsmwLsBiwxLhPiqYBo3CVVOrMXZwCGXa08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه نتانیاهو و کاتس:
ارتش اسرائیل اهدافی متعلق به سازمان تروریستی حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66056" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66054">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pceQCWdxIIiiJICppzrQ6HyurIu4F6T5fSdYGtPnhD0_BA1Tfhn9Zppb5aic6A8P8f5-9y1ZDENvWNr4McdFWVrm2Xcn4QhGuh2ypFn3KBovcQSij5p9qDqE4641YllndW9CHRr60sWf4jb_y5CAnWiZPL-HVzA4dNCfPT5aJQlbIWTBQ9aVcAkz9H-DfGmcNCSkNZZ7Tpol3GlPE6Aw1TTPJftVyXBETtQMRvxlvWARYYO0RDQVLUhE80FVbUW2mCtTvOkUIf2UqBxyj3muhoRhNrYRixQCygPriC3iuvQCZNO0WpbbKiZu1vZfKxHS-euenYJDwJOE8IYTBcRtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها ازحملات اسرائیل به ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66054" target="_blank">📅 14:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66053">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=O1RNEVZjBnHCXdIamQl24JLnaGsZqKG0bROtcY5nwQGJvME-YTGaI-EtxF31iuY5qhmTMxSzHsy0FGquNg06hEsS3T3_ECjk16d14500o0q6w-GWb1r10ewg55jcoNVaLbNiAzYJi_0dR-MvLm8iobpu7DrtzZXEKxiMXmMeWcHw4iZ-j01A3qJbwZE-bVw5MQUXShU42FNuYtUUTMxq7t8P27ZSr9vSbTwmgL5gxesF_nrSeyVaTUgE5t_qiASV6b9E55m_MXJdxEEVPf_z8w3SMFhwuZubDFz4QPhQ-yzhXW74z6Xcx4mywi8XyDdnsQl-y4VxDmSA2Ro44v6n8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=O1RNEVZjBnHCXdIamQl24JLnaGsZqKG0bROtcY5nwQGJvME-YTGaI-EtxF31iuY5qhmTMxSzHsy0FGquNg06hEsS3T3_ECjk16d14500o0q6w-GWb1r10ewg55jcoNVaLbNiAzYJi_0dR-MvLm8iobpu7DrtzZXEKxiMXmMeWcHw4iZ-j01A3qJbwZE-bVw5MQUXShU42FNuYtUUTMxq7t8P27ZSr9vSbTwmgL5gxesF_nrSeyVaTUgE5t_qiASV6b9E55m_MXJdxEEVPf_z8w3SMFhwuZubDFz4QPhQ-yzhXW74z6Xcx4mywi8XyDdnsQl-y4VxDmSA2Ro44v6n8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
تصاویری ترسناک از لحظه بمباران یک نمایندگی خودرو در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66053" target="_blank">📅 13:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66052">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=SS4DvqwIiHIIALjBzJepW2_I5VLmrb8Fb_hyvblD6iUyaf7a6qIT0KajCIDDKwxjNMWz2YyGt6jPpPWNSm8RL5KHGVazQittHMq8ajCtceXf2BbgUiTjuUWmlw2SNhu6fe47dLaFXaU53ThIYk_I3h1t8bV4v8EFlxHvlx1m1xTWDQHgwG46rNLJOeeeYv4DaquZPyjFcfY2snS8Z0fzXPm43_NZZIZa2bIzqAkHDhM3Rf0EFvOtUDwKpfYqa9B71NibDu2k9yvyaxMHDis_ZryrAekw0nQ1-o5SgTp-77GyXpeMXmgbGr2hCpAEsmCCjpJVa-qfbgv_NU-j-QGWAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=SS4DvqwIiHIIALjBzJepW2_I5VLmrb8Fb_hyvblD6iUyaf7a6qIT0KajCIDDKwxjNMWz2YyGt6jPpPWNSm8RL5KHGVazQittHMq8ajCtceXf2BbgUiTjuUWmlw2SNhu6fe47dLaFXaU53ThIYk_I3h1t8bV4v8EFlxHvlx1m1xTWDQHgwG46rNLJOeeeYv4DaquZPyjFcfY2snS8Z0fzXPm43_NZZIZa2bIzqAkHDhM3Rf0EFvOtUDwKpfYqa9B71NibDu2k9yvyaxMHDis_ZryrAekw0nQ1-o5SgTp-77GyXpeMXmgbGr2hCpAEsmCCjpJVa-qfbgv_NU-j-QGWAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو برزیل یه دختر 21 ساله رفته بانجی جامپینگ یادشون رفته براش طناب ببندن و انداختنش دختره هم فوت شده
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66052" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66051">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66051" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66051" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66050">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FN9j0suiKbv-JcNAHuueUDP9dYBJOlkotIYJhBPM5o8rF6HNoZlNrMRw06MWqSikQCQazzOQDYXv9ffvRo4_St7Ba2uK2Odocll05RewfmMzNIKjNOCd4U8x72SLvHeVx0jPf5yFV1biUcAeR9SpqBqzuPEHavaI925nzF55vJTSPZH0UKnXHWorCsMU-Au9EkRdor6IJCq-27i4m667zN6H3vjFdofzJUGEbpmsQolRF1Ax12V2vd350AenhMahppAbzEe5CC9NTB0OSfdJeTDo0CDiRKtpgXoiBF43ya2zyrL5PHP0Mf5Svyl54bCsvSkdSTm2vBrbe0D4WhmgKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66050" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66049">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db36249809.mp4?token=O-fZXj2CsKaU8Vnyi7PICUuv3Dl7y8lLXpMU5TCOP4qHn1T6QmxOpQ6bcGwwMm5KDbrfoz2Z-ghYUwiGUH2zxsFK88SQuQb5ZSq9NsWpmLJcoqGOujGKz-sohBtW48PXEhvJHo7kcDyE7iSNs0kldVXs3J4NGCHltxCGSBkQPeNT6aUPwRWgGbZR8Ie2XSSFWaPvuOe1g3cLNzMb26KkG_zmCaS7xguGskdsfJX7xTMj4Ht5718yMTFW6NroYRXIYXMhFvZ-VvLo99VD8rYZd-PUQFaLdCa08w2cDZ92cSz0ksinIgUAOqVgJfA6Lnhad8Z1a48MJr4t7cp7_073xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db36249809.mp4?token=O-fZXj2CsKaU8Vnyi7PICUuv3Dl7y8lLXpMU5TCOP4qHn1T6QmxOpQ6bcGwwMm5KDbrfoz2Z-ghYUwiGUH2zxsFK88SQuQb5ZSq9NsWpmLJcoqGOujGKz-sohBtW48PXEhvJHo7kcDyE7iSNs0kldVXs3J4NGCHltxCGSBkQPeNT6aUPwRWgGbZR8Ie2XSSFWaPvuOe1g3cLNzMb26KkG_zmCaS7xguGskdsfJX7xTMj4Ht5718yMTFW6NroYRXIYXMhFvZ-VvLo99VD8rYZd-PUQFaLdCa08w2cDZ92cSz0ksinIgUAOqVgJfA6Lnhad8Z1a48MJr4t7cp7_073xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۱۵ سال پیش زنده‌یاد مانوک خدابخشیان جنگ میان جمهوری اسلامی و آمریکا رو اینجوری پیش بینی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66049" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66048">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
امتحانات نهایی پایه‌های یازدهم و دوازدهم به دلیل مراسم تشییع علی خامنه ای، یک هفته به تعویق افتاد.
پایه یازدهم: شروع از ۲۰ تیر ۱۴۰۵
پایه دوازدهم: شروع از ۲۱ تیر ۱۴۰۵
جدول زمان‌بندی دقیق به‌زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66048" target="_blank">📅 12:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66047">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28745391f.mp4?token=hwQh3XaY802vRxmUZgsUOyU4YKNzRtXqUomHG-UoVda8Lp8wkWZIAav94Iwi1RPy_4OHV-sibVfAggCTjV-xs59gps4RS_BQj2hRF6pL0RZeCTgjbCdx0p9Vu-IXKdOpbM2xFz9d32RIv230uI40-2iT2fzF-IOEJEID4ScIGp3GCGG8oz-m-2GVmJYs4H2pxv052zP1xlSwNW6Yt50FBPmled4wmmx-o0zcfa0AJU8DRHMO8rMawWlXSuIm99bw-sqkWmm21OCvZUMolFoc0yvipxfOR2ILTkNZwY00lkAogkFuCsqtZZD7KJt9mYLhFijs1nTTo1Nv3TgxytgkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28745391f.mp4?token=hwQh3XaY802vRxmUZgsUOyU4YKNzRtXqUomHG-UoVda8Lp8wkWZIAav94Iwi1RPy_4OHV-sibVfAggCTjV-xs59gps4RS_BQj2hRF6pL0RZeCTgjbCdx0p9Vu-IXKdOpbM2xFz9d32RIv230uI40-2iT2fzF-IOEJEID4ScIGp3GCGG8oz-m-2GVmJYs4H2pxv052zP1xlSwNW6Yt50FBPmled4wmmx-o0zcfa0AJU8DRHMO8rMawWlXSuIm99bw-sqkWmm21OCvZUMolFoc0yvipxfOR2ILTkNZwY00lkAogkFuCsqtZZD7KJt9mYLhFijs1nTTo1Nv3TgxytgkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
صحبت‌های حمید رسایی علیه مذاکرات نمایندگان جمهوری اسلامی با آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66047" target="_blank">📅 11:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66046">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
ثابتی دیشب تو تجمعات بسیجیا: عراقچی خائنه و من طرح استیضاح رو به مجلس ارائه میدم
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66046" target="_blank">📅 11:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66045">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXKSxCeJcAlKascEhaNykqmjUXOJa49ye75Vp9NXGrEqeeq8Ech4Xb_ySvtRa-hQ9nBzeVbdyJmbdoJnll4zg92h-TF3hVx_dFc0VALGJP1I9GztzCjIMS05k8tZIQW0N_di81sOYzZqZ_H2i82cZRDOa_uKgcJ8GBfKJDBD16TnCJoWRnA7gdGihUatrXssh3nYYklKkQ9Qytt8_IjN6ziDDlNvq42eWcJdgp7YaEJnEF96THd2FaNEfkh9V6WXk67JDZjJQjYafvmmJtHymAKcnpyihfdAiYDEYXkm43ExSOwy1FdJu66iBQ9MqomPLZj-OgG6y9iXsXM7cmR9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی والا مام خوبیم
بابامو کشتن
زنمو کشتن
بچمو کشتن
«ولی رفتم باهاشون توافق کردم.»
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66045" target="_blank">📅 10:35 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
