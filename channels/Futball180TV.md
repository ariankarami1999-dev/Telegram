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
<img src="https://cdn5.telesco.pe/file/fKriYYvzTOiAeuufOsxubZX_fSB5eZK6sDHlveIFM3P0s3lutitTCmQbMztfOeGuuY8NM9VLh834NtwtuEaTCpofk_3CiMoG2MCQLDBdtoZ9anvYiZoAGueW9bhfia6EUZYZkqWrhT1pyrJiLe_LNK7OPUpdEM8teBgmz3BdSPI4QfjIQTuQMwPkXUoyJJ2_xTI31cmCErv1-lJ2uDX39YyhiYjb3gVbHYim-ZLMQsctTiekOJZAMlwV4X8IwwT3VO5PrYKmMvzkTfLpYvfyETOKNjtBenZsQctk6XUF0s_SeqQS4rz9S4537G58MF8_-apzpI2dqMUHNul-THt2tQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 727K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 08:07:29</div>
<hr>

<div class="tg-post" id="msg-95391">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc4496f0cd.mp4?token=grjCt9uib7QbnpEVK4uGFHLt3XVPdEkk9eWLM_osBZ0CQU-G2M9xnA1KFMNcE3XrqdWkyTlPfHgFmXe5sRvglckUhyBj_s2kJ0RJnUjcPmMPuRt9ntuSIPwrbSXczOdzrllNEqzGopGPIs4QKM1R-lDQYIDgOyOcWTjmcosDTCkvt5SN4184uHQfhyWqe-Awt7CgZbHWrpLxS4gMlyD49e0K5uOrVdxvns_pemFZONPG630rwzG2uBwhPQf3n0GPor9_Z3_yhxj40J1lrOgyPndra1upuNdgOodIene04x-sWdfLOP6sub9PXGEGw2Ns8qeKbF2uGLsEZ3MVWkdyNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc4496f0cd.mp4?token=grjCt9uib7QbnpEVK4uGFHLt3XVPdEkk9eWLM_osBZ0CQU-G2M9xnA1KFMNcE3XrqdWkyTlPfHgFmXe5sRvglckUhyBj_s2kJ0RJnUjcPmMPuRt9ntuSIPwrbSXczOdzrllNEqzGopGPIs4QKM1R-lDQYIDgOyOcWTjmcosDTCkvt5SN4184uHQfhyWqe-Awt7CgZbHWrpLxS4gMlyD49e0K5uOrVdxvns_pemFZONPG630rwzG2uBwhPQf3n0GPor9_Z3_yhxj40J1lrOgyPndra1upuNdgOodIene04x-sWdfLOP6sub9PXGEGw2Ns8qeKbF2uGLsEZ3MVWkdyNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇿
گل‌تساوی الجزایر به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 322 · <a href="https://t.me/Futball180TV/95391" target="_blank">📅 08:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95390">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گلگلگل اول الجزایر به اردنننن</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/Futball180TV/95390" target="_blank">📅 08:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95388">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4yUs2vdCnb51qvNBOZ3na6cxnx_Frk-VE-IAJsXeyFUl5gC6tREZew4t1FkVNZbEMvwOiWbEmxfyP-47eHLg2ddCpduPX24v0YWLgOGIyV9siWSQHAEoyCsAjguTH9LH0p5deIDPjSWKBFys1VI3qNqh-vkhjZQ2rTb5i-cVjhFu5hMzq7mE_o9usF10oEYHQXrCM4zlBp-yLtWBLLOGpzV2WJjGtxF2bR6vjDA6Zi0qDjmEP8LRDqd2rEvkK-4GSAFGu58tEPhJQYJQmt25F8xt-u0AlROKN8yimxNSdV978UY46hesHNSzluGhSCcgbsqCnEIW0mnEPH-GO44Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muf41K1WJcDJQcsOGFBiQNPXSVGLFntKiVrvP1W-0PnhMVOcWKgXHO4mIhn_fkNIqZykFQ3z7q-pMzjxcBZbwaYxNz0u3KjCDyDwu_1eYoandxkfqibmLVAMg8qAkbthU_gK9uq6zF3demr5ZnETvbdape5PwTcV4sYPHPfr5gb4mwKjjJZtAroosiQPA8KmzQ5B-ryQmf5eT8oQ1ewiE81kaNebiD1EM1Kw6bkZk96mXOs_tFWyWr1rHlCTfUQnpMetB8GPgwb1FCIMUze47mOR-sRExbzB8_zvNF07CZpnoQHMQqG7J9f7nhHraW0jUH-psclTBTYfYmdb49Mnkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
کارلو آنچلوتی: یک بازیکن هست که من او را خطرناک‌تر از کریستیانو رونالدو می‌دانم.
رونالدویی که در آخرین بازی‌اش گل نزده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/Futball180TV/95388" target="_blank">📅 07:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95387">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09b400e516.mp4?token=uQuX_f-aEnVkLw72gPol6WV_28xckRvgK6BYR6Ht4AYq9RuX_33bb1wMhxhD2LnHOH9trIpFdl51nTmMfdqydFVAJcHq5etIWy3qUb9GnGcAxQgBJXPKIoLA0VeJY6CNubTHqaapeIctVtCxkWC633x0zquNpDUszlCKsnPca1_FjXqj-Sw6G8OOAJwdeI1PMRfUGe1tKw8X-c-Nhvhe6AyI07pKl2ovE0v_mYt6XEL5gH47I_MftVBCLjXVzPVA4Yr7L9OiFEGLXUvkr35U-MJdbx9sXem7ICGTPoL44e0Gzmya5kmg1QAXSm7ub_oZx4uBqnHk6IPBgmCAXz482w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09b400e516.mp4?token=uQuX_f-aEnVkLw72gPol6WV_28xckRvgK6BYR6Ht4AYq9RuX_33bb1wMhxhD2LnHOH9trIpFdl51nTmMfdqydFVAJcHq5etIWy3qUb9GnGcAxQgBJXPKIoLA0VeJY6CNubTHqaapeIctVtCxkWC633x0zquNpDUszlCKsnPca1_FjXqj-Sw6G8OOAJwdeI1PMRfUGe1tKw8X-c-Nhvhe6AyI07pKl2ovE0v_mYt6XEL5gH47I_MftVBCLjXVzPVA4Yr7L9OiFEGLXUvkr35U-MJdbx9sXem7ICGTPoL44e0Gzmya5kmg1QAXSm7ub_oZx4uBqnHk6IPBgmCAXz482w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل‌اول اردن توسط محمود الرشدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/Futball180TV/95387" target="_blank">📅 07:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95386">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گللللللل اول اردن</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/Futball180TV/95386" target="_blank">📅 07:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95385">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شروع بازی اردن - الجزایر</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/Futball180TV/95385" target="_blank">📅 06:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95384">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069fb238ab.mp4?token=ifr98j7zbAtDeQ06fbPe_JCdpkal6wE_-A4WNevwQVY8vRVZf5VtgI7OQa4EQ5UXJoeSygI-BOngbvNIyzFqEYqQUumht3GVNLzMamHrA9_1K_WwV77qfm2eSWGwcXoFMzkWYiw2bIvdMELBkslhrNEHU0bDFH8-IH5wCCjUJkhPg9GC7gScR1TLXcHx8B-EgM_x1jKbuoc4pkcc_Li9FzIRTXTYtdGJNpm0H2dJb36ljyMKgCvZDCGKD1OXNSvJVq2ddtKysQFe4qBmfJ4R8bd6KRkBToBpEpBTojXXp9jmxTKkejlbEl9oeqW6MEcwPw-lm_2k1l_HWepLT23roQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069fb238ab.mp4?token=ifr98j7zbAtDeQ06fbPe_JCdpkal6wE_-A4WNevwQVY8vRVZf5VtgI7OQa4EQ5UXJoeSygI-BOngbvNIyzFqEYqQUumht3GVNLzMamHrA9_1K_WwV77qfm2eSWGwcXoFMzkWYiw2bIvdMELBkslhrNEHU0bDFH8-IH5wCCjUJkhPg9GC7gScR1TLXcHx8B-EgM_x1jKbuoc4pkcc_Li9FzIRTXTYtdGJNpm0H2dJb36ljyMKgCvZDCGKD1OXNSvJVq2ddtKysQFe4qBmfJ4R8bd6KRkBToBpEpBTojXXp9jmxTKkejlbEl9oeqW6MEcwPw-lm_2k1l_HWepLT23roQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتخاب سختتتت بین تماشای فوتبال و ..؟
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/Futball180TV/95384" target="_blank">📅 06:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95383">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUOpiaKbMqLLkvv2tUK58eXXZrLOoGPXknCsBYFAwGiCW4Sq2R3ouI2PnsKsWAYItgw8TZpIVMmruA0fjVS7RVkdgS3o-b6urE0Xo9w9fb3HACxuR4-LeaH12MruhpdWdgOdbNX3CFCTlQBZC6qxKzR27_ooHTxlbnU7IhYnEopm2MF_vpIMKEEqHueY-GQ0o7z87nzeEomTQWYRiDfkuH0skd8EbpSYd9iBGHuigeLTV79TfDOXMHeBOT5p5REmfY7wU8bUCCh6lugFQJsSi1oQqU1gH1TT--jMwUmV75ci7hTjqbO5c00Bv8yd9-ocdlFK6wBRcsTqpsp4nIzaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی نروژم اینجوری بعد بردشون احساسی شد و از خانومی لب گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/Futball180TV/95383" target="_blank">📅 06:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95382">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFA-NNbe-A109Rox3oMBuD8LE9IicTlumUeDueiXI9b-VSYkdkWymLi_hQVklYU_nzXY73mJiGHd5JNADSdK4WOXX6BS5ZV281M8cjLwova08y4IykPX6y4sVJ_eLfeuYoQuWgbQMaVqCk0-zNfHewXj7EflV-RDjSBbabs12QjCFeh21Yq2efpxA5ngv7SSOtvxDjWosycY3tvn7ko0EVIbU976L_BaCCmbmm_0YsXTvsKw-hxO2WIxvmB1KtxQJSqHBgFQLrCpNkC_u5a5nS94RlllJPxtA0cykAsmfqr97uRld7UP7JuyFcdDngmtKb4kS9bXHBeVHlOFv8KJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقابلی که در صورت دوم‌شدن نروژ و پرتغال در گروهشون قراره ببینیم
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/95382" target="_blank">📅 05:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95381">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxp9ll8uOIYi0R8ELAwQZr-aVTX86jQyKXN6l2G2vWrISK3geNTgkFxrJDg-i0tDiTPaaeuMtAuht23lbUymAodPBfZDKyHmfpkp-q1qH5o9QfqBnsOxpAynkgLmA6KXOVWUb6ZDpRh4Z9-_RNtrssu_P0074RkgQu8Q6hq3j1dchLoAiSbcVFXHwO-zeTylb5gaH-_0c0HGWye2NGdXgaTFgPQnM3Yq9fUDl2eyPCk-tgLAS9yxsDXg-sQLTbZEosaWOU2amqH8HxVVPqRHh_1y6CnNpa1ohJngzzWgqtitL6-qtZMQCDesZ430epzBX-CUUIeAt5eVh8oNObSZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
در جام‌جهانی ۲۰۱۴ و ۲۰۱۸، بهترین گلزن جام‌جهانی تنها شش گل به ثمر رساند درحالیکه بعد از گذشت تنها دو بازی در جام‌جهانی فعلی هر یک از این سه نفر حداقل چهار گل زدن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/95381" target="_blank">📅 05:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95380">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7d89f979.mp4?token=T5mKIBR_QvCriTe0l2UvT8hbdy3XZnnebzha4pPqxVZABzQZmkRwsJkXuLH0qFt4HsV87kCC9G4ccIJ2GLfN5ReYgXb7xwOVXnuEPf51oteoeJ_wRo4Q8HUKTKofIuZ2SMz6vS0CLncICIArgopjSjW4sLPRgfY4FWhg-j_41PRXcfoxUHJaxc5kwio8aRgTgKFfumhjIiz9OEm1Un5MtYLGKWj4ZGWUWawFDwPxN6KeiBjV6qnCzZVspXMtPe16BC9iN-XdRlNlKJE3rpsDL5JXmbefcyGwpK7MWFresIW0LakKH1Tsk9_BN85Bga04XP693_feDrRXD8rdsOLISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7d89f979.mp4?token=T5mKIBR_QvCriTe0l2UvT8hbdy3XZnnebzha4pPqxVZABzQZmkRwsJkXuLH0qFt4HsV87kCC9G4ccIJ2GLfN5ReYgXb7xwOVXnuEPf51oteoeJ_wRo4Q8HUKTKofIuZ2SMz6vS0CLncICIArgopjSjW4sLPRgfY4FWhg-j_41PRXcfoxUHJaxc5kwio8aRgTgKFfumhjIiz9OEm1Un5MtYLGKWj4ZGWUWawFDwPxN6KeiBjV6qnCzZVspXMtPe16BC9iN-XdRlNlKJE3rpsDL5JXmbefcyGwpK7MWFresIW0LakKH1Tsk9_BN85Bga04XP693_feDrRXD8rdsOLISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم از جو پشم ریزونی که بازیکنا و هوادارای نروژ بعد بازی رقم زدن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/Futball180TV/95380" target="_blank">📅 05:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95379">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjIJtEXx2gEktVbDv_l0d3CiB4O3nqpvkg1uE69sC2r_eCTHh0jSLhJ117GjB5EW7Q5ShAfUUh2epKimnGgNmy9KnS1zOoPLAbeYht5LWbwezzmuK31B0-iHFiDP23Kz7FkskQaR1qWKAh5vUjWDd_zeiFli4dD5q_04Zv06xA3uH-aV_fQiMygb7vuRWJpJli_vnWBRSnPPm3nRh88Mb28WFmvEMWsAdXbcsz8Qy66XMK6-xwHMOCdjtwRGvIyzMmYqreb2zTOGf6siORCN7NNrFgh9ZytdSmjdD8CWp3gaHyMbNdtJnArP2trVYErsAYj9eFWIj0X_MxoOQYR5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
ارلینگ هالند در کریر فوتبالی خودش:
⚽️
‏• ۴۱۶ بازی
⚽️
‏• ۳۵۶ گل
🔥
‏• ۶۶ پاس گل
‏۴۲۲ مشارکت در گلزنی در ۴۱۶ بازی!
😒
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/95379" target="_blank">📅 05:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95378">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmbiYlDLYi8WOjcf_StzJzLoKx3CocOBc_0YPVB2xyWY8FI6p3NUkqpXzcFfLg3BfMQZ9mpopL_CXdoa6_FeNekwNY_c8-0n5-9iFEruUSJRUc1IyzCo1UaL-nDAYI0vtCLeAALZeOr9uLijGPNn2CUmLNK_yXENqYnvxiEfAvgmsiJf4ODxWcLCrIlBqA1ha-A-g2juSNh7D7qfXpCliup__sOkq2IIhqKHi6iIlAGM8vtpOY_RROKI6QrjPdUHTXJ5nFpDofH9EQRIhTWFx55OZgqbWD8RrJr9AhdT65nKP1R9lyI232PlkfASELEav93vj-J-NbWtXjz9dJ3X6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه L جام‌جهانی پس از پایان هفته دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/Futball180TV/95378" target="_blank">📅 05:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95377">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVLTZkn0C_3ITka7r1id2--AAtbwVcgpqqdPVRdgilKCgAeua3s0RuJz7wsq_9lttjhzKYmMWNHilAjL2klEryC7hsATbgXr3FX0iFNq3p5Fp4HR88pnjDyIWFiw2_16Y316RNbPq6x3F16w_nBi_ZweBp9SscaplZTK28fSDt6qp_trRKx__XWGGZAy_v3iyuoj3qBp934BQrZ2Gsg9Ys7svi7oSaBymWa5BWpuRxQwQrWC24mqdHqh0bOoWLARFxQN0D6SKhL4VandzniYwNfr4izrfVhjbXblDf1ibM0dFyHvIq74AVqKSSSw6VtkNJPQNdmEZJzH1ro-e2Gg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود وایکینگ‌ها با دبل بچه‌غول
🇳🇴
نروژ 3 -
🇸🇳
سنگال 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/Futball180TV/95377" target="_blank">📅 05:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95376">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/03c1e0c349.mp4?token=rr8O0-8piGOMdKSdR4NW1Hu6PR0QDz5XEzBKE9N_Ke893xbC3dlNM3jdNCLFJ6iY5FBCjB2FjD4jtofym28ZFHu3cDmpMdPkn9KCllf8auwZ71SXhQrEODO1Qnq9KtE1F4_ndhcdhv0_IE9a75dWJ5Tyt0T6DORjSmBKRmBrS6sz5KNjuxe28Lpbp7iLMpuuD9934CuVc8AkRyzImRvP4kEMwtYM8wB1VvcnQFu8cK8atdVII7vkblvhwyoqZAR69qHdvUR2Rk8-l0N-QjcV0ED39-MCkzG8s1SyjoddsX2r7f-F8AYsbNBZ8aHI33hngYYfx23vJL72rOfhiAyCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/03c1e0c349.mp4?token=rr8O0-8piGOMdKSdR4NW1Hu6PR0QDz5XEzBKE9N_Ke893xbC3dlNM3jdNCLFJ6iY5FBCjB2FjD4jtofym28ZFHu3cDmpMdPkn9KCllf8auwZ71SXhQrEODO1Qnq9KtE1F4_ndhcdhv0_IE9a75dWJ5Tyt0T6DORjSmBKRmBrS6sz5KNjuxe28Lpbp7iLMpuuD9934CuVc8AkRyzImRvP4kEMwtYM8wB1VvcnQFu8cK8atdVII7vkblvhwyoqZAR69qHdvUR2Rk8-l0N-QjcV0ED39-MCkzG8s1SyjoddsX2r7f-F8AYsbNBZ8aHI33hngYYfx23vJL72rOfhiAyCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
دبلللللللل سار مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/Futball180TV/95376" target="_blank">📅 05:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95375">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سنگال دومیییییییی</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/Futball180TV/95375" target="_blank">📅 05:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95374">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گلللللللللللللل</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/95374" target="_blank">📅 05:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95372">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7Z6OxFFgqKFKx1dUKqON6igcKKI5WyznuY1Ow9FYbiUpw54FojBnEHRMcX3Cl9RoPsTIxD6waWMgNp-vLmb_nz_UHzGE36xmiKjHOhObEixW-NIGKJc9Sqn16vj-98LEaaUvEQF6326Pe8yxkpHsSdUwhtcF2HK0CcDUrDqoreMHcrp9y3d8wK0xT0Q7z6vNzFsIFn4ZxgxHAgAz-EoDr_KyHBDDCWJVRb7VhpfhnbOkOCzk6kpzMKlZU1BgskCV6pB7MzVmmzKlz-ymKUt-aPCMjf5SAo4P-GRuyo0_uX0Z2EawgBcLH56PYroaY3cL17ltowbXcB0Y-FBvOOljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0ZKyMW0FJZd9TC1vifUZAu2zemXcBQJEjoAVqBc2SdOCVNEDK_Y03CapyAqf4bSzLaQDM86qs4U7YlAtl5xbgKUq7VBjbSmjqLpmWh3uXHGSqVcF9HHokMykeehxnh-fjT4rLpg0IqQwsxtEtb3bYEBmJ9TkTW8YkUbn9wslZxwJR98Aedhil9QJwl7cdtV4ZI3v7MdxVah1mfr0U_mMgP8nKpQsgFE50FyLw0opGb5HFjsFx696GMACAeaVUJN-2yznNVYy0Woc_37gyYQ-7ZnXNYwOoAa7DdD0aU7Sv1QU4myvB1Wf0P-TmqBvuFFOb41AtxRta6u781UC1cpuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇿
🇯🇴
ترکیب اردن
⚽️
الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/Futball180TV/95372" target="_blank">📅 05:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95370">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGNTfIeY4eQaySzu6rFJq1hXpITTWia1YnAN9X716pe2VOd0nhk55ADmAR6l3Ygv-RSGAki0WwL4klqSIqN81O1rEfv-nP_quraEGwfrYPq1WspxWSUL51cifpm7v1D86Qqx6RyTmSP6nyzhcK6pkVRXaCgpDARMi0aBurjo4GP2AaVaE51spEhmXHFFP7g4QB-oz1RDTSR6v77ksbl8ZLcAB7xbDSmZvkfLdO98Zzxaitr7Md5jVhkvbgzP6aEI_L453z1sx9iNhnButayEbqJZoS95prD2J5V-R_FMMuH2ZFvblIyEAeXfQGnR-ZMHlXzxAbm9VnW5O_xSc9O0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qes1e062iINPGX4m72OWqmDKAxmKnM4QyeaA1TW0jrz12pTrc0VVek1OGX9MhtwkFYXq2MLk4nezpYrJxdCM09Pm1kgIz15ZlOVojyBbpZ16T5Y1ent67exgkBpc3CBB_HGnZzG5eRdymmjMWjJx4XpIU9k9BwH_M8FFKsW1qL8cdyHIk_UH3FJtaKVhCajUkmjnSxUetCGaOBIGSMzuITCiMHekTK98kDBEPoe1JAJCOTYIb2plzrYrbDbtYKzuyoS1pbmR9iYCyd_Ie1BX47qQ1PAZKVvjCXgZZTiInhbDM9m9ZOPkghmVcPeDqNM0EgwEWbw6jHVyYROhudq2dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Haaland x Ødegaard
🇳🇴
💎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/Futball180TV/95370" target="_blank">📅 05:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95369">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDVf4UP5lvu-0wKpPaZvasMmRGA0XcvFy0_PqA3xsTFY-ODr_mdK2ImU-PDPV3EGdBJRN1MIJwEYyaIWVN7Jjn__0Cfp4OMLtvYh4Kk3E1zQwnkncJo6NIN1VQ_2YgEdJ5esG-cUFIN35sLWXRJuS4kdSLMStcf3XPDNMnE51ZWFHTjqJdO8fDdiJdP-mGOhDxb7wF4pRmtfJpWSVOWoX80-mAt843i1qQBQqjgunNILZxfwWs6dq5ILz2L5UosIxP1uk-z7qizDttwOpQakCOih-gkOCaEByoO3KG3JPLXz5wpZEVI3pAUNjZ2mIDokpIhSYuaDfH4qOccJ0yKRCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وسط بحثاتون راجب مسی و امباپه این وایکینگ نروژی خیلی سوسکی تعداد گلاشو به 4 رسوند.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/95369" target="_blank">📅 04:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95368">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مندی گلر سنگال مصدوم شد و دیا به جاش اومد.</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/Futball180TV/95368" target="_blank">📅 04:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95367">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwKpyB1vGCLSc678Uht2_kGE5vIFsCzyPrOqhBmeZg9fXpGRKNN0nwFOMT5ItKDzbmAoYAtY1I4pEHowV7131skL_BuDzGyqzs-ksBi_J65dcZefpZ_n1bSMAvMEyML16LUiop-D9MGi9SYj7zvh-vqLMnfGzyKlCNpT53XV1o1df2R05mxfF9fizqIxZw_l5KJb32LL75hPzNxxfkU7UK37ciOFLThdnEnDnU1-YocNwqgm51MsfB2hWHQSozryZPY9RjbvSl1U4As4p_jrDZTvE6kqZHFDWMvd2HHAta9D2UXLXPKe4j5HQ7CsFq3Qvb6II79H_zJ-SQFpb5nqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار پشم ریزون ارلینگ هالند در تیم‌ملی نروژ
❤️
🔺
ارلینگ هالند به بهترین گلزن تاریخ تیم‌ملی نروژ در جام جهانی تبدیل شد و در 2 بازی برای تیم ملی نروژ در جام‌جهانی 4 گل زده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/Futball180TV/95367" target="_blank">📅 04:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90bf733ce2.mp4?token=p3-SQFNIWwpGKdPuHtylsH-BpdcxSL1grsX5Oy2swHXwrl5BzAbt-Enr3I3FKlkjrLB8IvF8xQqA4itHXNZzapM1Zgw-Zlq2qiLWaX6PmW9H_e32twIinwF3EvxnCFfS2ijLQShHTPeW6Cy-JUR5ABIYYbvEX6BSoK8GN-s6VLrdtQDO8c7lKDnDB_9RewAAiWpkKRDD8CaXPA2CUR4qx4-zy-s6JVKzea-bznKt1tohi7jrWFFO884z7TjyadNdMaWfnLBR9iZQnL067yh34X_GLcxTplYQpJUh9Y-eMnSBLS1lteG1jziIn29C-_JCY40cFZ2oH_Tvgu2dcFAfWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90bf733ce2.mp4?token=p3-SQFNIWwpGKdPuHtylsH-BpdcxSL1grsX5Oy2swHXwrl5BzAbt-Enr3I3FKlkjrLB8IvF8xQqA4itHXNZzapM1Zgw-Zlq2qiLWaX6PmW9H_e32twIinwF3EvxnCFfS2ijLQShHTPeW6Cy-JUR5ABIYYbvEX6BSoK8GN-s6VLrdtQDO8c7lKDnDB_9RewAAiWpkKRDD8CaXPA2CUR4qx4-zy-s6JVKzea-bznKt1tohi7jrWFFO884z7TjyadNdMaWfnLBR9iZQnL067yh34X_GLcxTplYQpJUh9Y-eMnSBLS1lteG1jziIn29C-_JCY40cFZ2oH_Tvgu2dcFAfWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
دبل بچه غول مقابل سنگال
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/95366" target="_blank">📅 04:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95365">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عجب شب سوپری شده امشب</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/Futball180TV/95365" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دبلللللل هالند
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/95364" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95362">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d459d53d.mp4?token=oZSSxLKgRKc53kweVdKTP2Kgx3ywMsHDpTzLBkJKKD8hSjvUumNGROejSNm2lhKCFAtkiLt-M8YrTzeVhHdeGAHRRlQMOuremVcmKIZjvw46O3Z5MkKjefiydvf8uRK5-qn3BF8moIqjGjzqXn7-52fWhX4OdSVULtjyhoT1PsewsqBz1ErvKe9UFupyW0f-Pt1CYvYcs3-Ezemrz_ejb81QP_tPvoSbi6f3UHdvjjVcKY9r9yG2JPhqX_9ajUxIHKjfijQbra_OiVkQwx8o3sa0rbPkFWVCw8kF7RuWplLA_MDrU-2PdeszaRlC1hJ2IpWAxMc3gbWtNkVydYtf-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d459d53d.mp4?token=oZSSxLKgRKc53kweVdKTP2Kgx3ywMsHDpTzLBkJKKD8hSjvUumNGROejSNm2lhKCFAtkiLt-M8YrTzeVhHdeGAHRRlQMOuremVcmKIZjvw46O3Z5MkKjefiydvf8uRK5-qn3BF8moIqjGjzqXn7-52fWhX4OdSVULtjyhoT1PsewsqBz1ErvKe9UFupyW0f-Pt1CYvYcs3-Ezemrz_ejb81QP_tPvoSbi6f3UHdvjjVcKY9r9yG2JPhqX_9ajUxIHKjfijQbra_OiVkQwx8o3sa0rbPkFWVCw8kF7RuWplLA_MDrU-2PdeszaRlC1hJ2IpWAxMc3gbWtNkVydYtf-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به سنگال توسط پترسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/95362" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95361">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxC5sWPTRKF297Brdlmif8N317sr72mOhyrnEhvEmiQPQn2FC-C-t0A6SMjMBYmcaTFlStKb7K1_GbX3GQp_4Zm160O5C28ea43sVaoBwyeseJhUKssP1zsbaYtjCpb30p8zQ8ezEkob2xEJNtfKG5GdDM6ocpGNR9pLYLzD2ZDkQiA4c-QGFW5RiNpM5cc0rvuAd1_RQIRtRgJt7doo2-tYLznzJpG0TaGA6a7Jnh9EPAeanCEbHyIVfHig61udPkAaoqN0wYybB4FCMhgzDOU1FAryu0vC_FHlL6QyGJzjreiy6CZs0AsjXWe0NwYxDmrF7hUaKpJ5CLg3hEUcgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امباپه با جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/Futball180TV/95361" target="_blank">📅 04:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95360">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4D5CV7Ms67j5VK2s6iyFmzn-Oq1AFNrh76F0lGA_6kLQxFoxrbE5RIuzGDVjLjzw8pyvUDAulTUROoF7BViV9F8so8VgmKGw1edNM4EqI87TZWJmcTBw4jpCX7fIKt3_XNhPJRJ_D3jb8FLq8JIfQAah9O0YMGIge7rZ7NN-2WCkHXf8kcpYQqQh_PAaV4-qTZz779VfdcZTHA984AJ2Z3qvCzQJOaJDL-MPGRSh8tPxkHAgQQsPme-rV2Of1FZtLDvts01_gsNe6vvWxIFU_z_CCAH4yDkmkswpaLw853EKOOQP6SoGE3kllvnUFiFHIxHi3iNBmXc1sk4TAiULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
مثلث توقف ناپذیر فرانسه مقابل عراق:
🔺
امباپه: 2 گل
🔺
دمبله: 1 گل + 1 پاس گل
🔺
اولیسه: 2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/95360" target="_blank">📅 04:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95359">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TR24P_blXKb7NvwFckwn9UmOB3h3RePc_5mMWxgzJ4ucDoz0l1IMBYC9TVFEhvHkliyyqIrrNvFedBZG9Q7LiLeXDfehVIpEIQvuoShaYSnWD-9cSuC24DOJadkIq7Y3G2Zsb1Hk0Y4EFaHPDJxhz208rlthG4NhyW2hOcI-fBoKpIiWYG82g3SMYs6nbCvXcEA3kCTDpVIzsT3Lzkqw3KUskNibl7sIRZ5UtkjeUBQTmJb5ZeTWuWSy1_9F84-urSCf6utYiFEFd69fIESE5joVXyRZqaWf6U15swpvIVzbHFekCgAD9IlDGO_Fkoxd9yg-eFOT_MuYtxCoWgqkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیمهای صعود کننده به دور حذفی جام‌جهانی آپدیت شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/95359" target="_blank">📅 04:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48292dcba2.mp4?token=jbcfqusXaqnkCiR39oinQ_O3xzHraTUapdbo885jJ6iITd6UumEMr-uHPADXz7Ls9eTsHeqi-mf_kP7U_rrND95ZqlTT32VkOdXluTPwDGOnQzX2Qt0ill_yLt0f5Iq6s8-LFsoW84g772dCk6KxBbfR1beggSIlhYYRO6snD7YrpkkuyBlz_AAIoSvGlcwOxYoLcA6TywMs5awynwFPoPbguVl8vozafxdmk8_Lm06N9NivHm3B3tCFS8A_QZHK9QxmpS-3FASflGSkgVV7Rtbds9BKMJnrpQymZJUvDDPklCSjBkGoj3Mvdr6eaffWJacn8WBzi0A9291SKn0dTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48292dcba2.mp4?token=jbcfqusXaqnkCiR39oinQ_O3xzHraTUapdbo885jJ6iITd6UumEMr-uHPADXz7Ls9eTsHeqi-mf_kP7U_rrND95ZqlTT32VkOdXluTPwDGOnQzX2Qt0ill_yLt0f5Iq6s8-LFsoW84g772dCk6KxBbfR1beggSIlhYYRO6snD7YrpkkuyBlz_AAIoSvGlcwOxYoLcA6TywMs5awynwFPoPbguVl8vozafxdmk8_Lm06N9NivHm3B3tCFS8A_QZHK9QxmpS-3FASflGSkgVV7Rtbds9BKMJnrpQymZJUvDDPklCSjBkGoj3Mvdr6eaffWJacn8WBzi0A9291SKn0dTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به سنگال توسط پترسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/95358" target="_blank">📅 04:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnB_-2J-QXQrl8c3bcDxasSe3neDHD9Fb2ICEIy-SZSp2NBg2WsX1q-pFJbm-mIureIcYIhMr6Wsn5XPfsuDsNKymqA56H9UX__yQ9ma-pLGF_hx_JWCgVqG-q-XXb663T-Y4rUx9HBMkbZtvTKPN1zWCcRjE5AShM2kg0EwZ1pPE1nXhz7PaQ8OK9vqAMkGoyACzdj2ekrfGNIug7Vbd-78T54cvheNzmSelNd9XJc0I17kxUUXwbXM3BTUUYpsVrfWl0E7-mBvSbTGeSEqeDcHu1ivDQWsAudpwDzsUgzT3DKBXwx7Ls5rF5o0YgOCfs9-E1pqPqy3DuRGa5YYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | جوابیه سریع و خشن به مسی؛ صاعقه‌‌ی اصلی امباپه بود
🇫🇷
فرانسه 3 -
🇮🇶
عراق 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/95357" target="_blank">📅 04:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eflgykEgXm4Iy4pQTLzDlyOgmiKSrBoVp-0mq0keL9c6rhG-JsSPIA0-rIETYVjyVA_d1yJxd_AAJi63Z1rtaOCyS7OApGDot-wb7BdqAOi6OrYgPKSKOPEOxbqY_xfkDk0RSmOtU4jO_lBgHRUYFWOhMXkaPXCgQ9ftisx0ffkFPPL2NzYc26DJ5ODIeK_y6BDNlzLnxK2QjkAp9-QnYZ7DYZlsEgoAqHlgjtdKFteaOeJD-q5q77-emotVmM1B7bqmaYIfT2fbE4r6Km44yWKB9gRNst8e1cHsLg8QoOn40WiEZGv-TGEJ8Hs3yPMeMuiujgpY9KH6nvIFXtZXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از ابتدای فصل ۲۰۲۵/۲۶، اولیسه در بازی‌های باشگاهی و ملی ۳۰ پاس گل داده است
‼️
بیشتر از هر بازیکن دیگری در پنج لیگ معتبر اروپایی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/Futball180TV/95356" target="_blank">📅 04:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184c9dec10.mp4?token=uj7f-jWUQpnkpPhYiOC_gPsGDLhEY1hHO-USsxctIreK3qh1z8QwOL1_LjhhUEh6X6yQgsqoMBUqhGsQFAtHapqI8JtESfPu8KqVFE6XqTKsxl2KZsN-xYDJrqzGl5HX_UvYXlSDDvcOjSoH09Lbe-SogJatG7BBnjCz_6dzudEVi_vZQBDJFcm0_kgSRCvRLUSd6w74Uys3bPbYcNzvy-4dvs_NCsBMQobZM0-R4MjgEcWUmCpHEWoYTPFCLW9xmUzIudMIkpamzn7LsODtxvvb-JIPfKb43Sf5cV8NrLrfm4nCLhKZCpRtR-YaaRMNF9PrelKiZYOqAChulUHnGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184c9dec10.mp4?token=uj7f-jWUQpnkpPhYiOC_gPsGDLhEY1hHO-USsxctIreK3qh1z8QwOL1_LjhhUEh6X6yQgsqoMBUqhGsQFAtHapqI8JtESfPu8KqVFE6XqTKsxl2KZsN-xYDJrqzGl5HX_UvYXlSDDvcOjSoH09Lbe-SogJatG7BBnjCz_6dzudEVi_vZQBDJFcm0_kgSRCvRLUSd6w74Uys3bPbYcNzvy-4dvs_NCsBMQobZM0-R4MjgEcWUmCpHEWoYTPFCLW9xmUzIudMIkpamzn7LsODtxvvb-JIPfKb43Sf5cV8NrLrfm4nCLhKZCpRtR-YaaRMNF9PrelKiZYOqAChulUHnGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دمبوز هم به عراق رحم نکرد و اینجوری بهشون تقه زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/95355" target="_blank">📅 04:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3e060451.mp4?token=ce6899G-9qMwCWcUxEwzE8gDh1DEUrJnwgw1yPE6lbuR__QwpAiz29uyCdS_CReo56OsxRgEuCSFayfpj9lKQ1bVsfP6rirVJ7Bv4Muztsj6gKQCTX7XfB2SXOFdsapN_DGq7bPIYB7Vj07MbGB_6p8UxJEaz_67vnU0K_FYAL6Buuvng0or3jKeqyBGXkqFZqZrh-rkCGw9a5nxZosVWNuZYQCT_zMnmfXYChqoF-0RwPYNp78wpav-ZJRFGpnWZNbLlbaSpC8jDzTT3Sf9jOFAUwE9-r3sd1QmA4oft1vKDjQB_jHKCgE8aejM6BDxz9g9-vk0wqqL0UhMz16ZVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3e060451.mp4?token=ce6899G-9qMwCWcUxEwzE8gDh1DEUrJnwgw1yPE6lbuR__QwpAiz29uyCdS_CReo56OsxRgEuCSFayfpj9lKQ1bVsfP6rirVJ7Bv4Muztsj6gKQCTX7XfB2SXOFdsapN_DGq7bPIYB7Vj07MbGB_6p8UxJEaz_67vnU0K_FYAL6Buuvng0or3jKeqyBGXkqFZqZrh-rkCGw9a5nxZosVWNuZYQCT_zMnmfXYChqoF-0RwPYNp78wpav-ZJRFGpnWZNbLlbaSpC8jDzTT3Sf9jOFAUwE9-r3sd1QmA4oft1vKDjQB_jHKCgE8aejM6BDxz9g9-vk0wqqL0UhMz16ZVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دبل امباپه مقابل عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/Futball180TV/95354" target="_blank">📅 04:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95353">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
با اعلام داور ، بازی ساعت 3:20 شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/95353" target="_blank">📅 02:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95352">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYhbLsnH17llybIqbkZ8Rusfexf0my10OtLt8j3luK4MkKeIjwYwKmM2PvILDnKe-RQsclAkAtEsbXNGEuNHlqm0n4LTydi_TasuRHlcMDGHPWktyzg_JzorE3zevApbBgTrlZkHeRRUfn35tg32frfIBrQrcJdMjMj8yS2h7yiVWAWyyT3EK_LKrZM3Y71BZ14sMMzDTl3TK0UptWuxhtu-kwr202RwOB90kWhrFM717UIQSdcfvJPnFMT9bLAqISXaZNIOtCQrYFR2FP7p0_6PmOu9mNUiuhzvjuHLAFPyDkIuvr4TIjm9XLfFkgwDAcAPkAud9rFLS2JPcjC17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام داور ، بازی ساعت 3:20 شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95352" target="_blank">📅 02:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95351">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRyH_wPDFpiHZwIw1AfRvHc8KKWPHz68mSbQTk2Hfve0m11fJGuoDUZ2bC3DO7yotFm7L_FJYfXKRlqsyu0znq3fbfahLCxxImvb28XE3hdFghoRiXv63NiOlzW9PkAmuCS9kO2dnrXhWi5v6ZFPpdLU_CUzkziNkFxkyKpJ8lY_LKz8VA-ZktRimzupd1yZwqNVAGxle9jAodTlb-ommYdoGRtBB8viBGD8izd9w-_OycJqVcC1RPQNoOm9ChKAz0wZrYVX7JcDnMr6CSXP1syNAqz3YdSFY8waXj7RI_qCfLpbq0MWuwAGXFkMIsxo0q_UlcoMzI_sdoN5wMXPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدو :
خدای من مسی 38 سالشه ؟ من از اون کوچیکتر بودم از فوتبال خداحافظی کردم و وزنم رسید به 120 کیلو، بیاییم اعتراف کنیم که لئو بهترین بازیکن تاریخ فوتباله، همه باید اعتراف کنن، غرور رو بزارید کنار و این جمله رو به زبون بیارید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/95351" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95350">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🏆
#فووووووری
؛ با اعلام فیفا، ادامه بازی عراق و فرانسه ساعت ۰۳:۲۰ به وقت ایران آغاز می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/95350" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95349">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/95349" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95348">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ctAt1WCgsVnh4VSaKAspZbCxUhZD0dolwJ0ukBsy437I_MQGm-MDhwIvYICVu2erUTY2QFbxJDmLoRMp-KK5oUiFR6eoPPrxH0ucLa1XOGukSGfblPbd4S0fyfJdKTVULc8glVd5dnVvtOnz2TS182-m_2m3FWTfdywvhlV8RzYi7Ri87ZhV-z0fjaRegOMXqla1-5Fmk2is29CSI2UDV4rE0fc9mgMt_0b0QpTlXHdv0qs-IpuQ1elCPmwFas1ZrVn9KIZo6NmeqIrzW220m7W0Wq4xjfXcVBDkieTKKF_SLHYFEjGU2dKtD_RzjWk9JKo029djpeqAPXgKzhNL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/95348" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95346">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
#فوووووری؛ به گزارش منابع خبری، احتمال لغو بازی و موکول شدن به فردا زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/95346" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95345">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0yaVG_t1DTCfB5PZlV6Ex7gAXcxAs_NPLJVYOskn1HPwdfSPZ_S0-QZM0GFMIB2EdB70VC5OZydZ2FvyV_izRYFl7VQZSRjsLEFZu_CUwVLEN1Yj6aVhm4sEH-cMdwU8IBk9owZmcYNrjo_LP1cyMeCa25NlT-OFRiSUsc-etJLHWXnBYINH7-qSKl5F2tVaOwrnQ6T55Zu7E13YKr8wZgQdhr4snXuf1ijpi8vvayDYOjiwg8yXB2qF-W2rTCNhbVdYmoVGg754vfWjehogqTb6lVFu--No6KcE9B8vx6VB0htsPIBIMgGSmYYWzBfHT3UVpOf0suskJlYhzBQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔴
سوزاندن پیراهن آلوارز توسط هواداران اتلتیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/95345" target="_blank">📅 02:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95344">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lak6y67zGF4zX7ATjLDdznKy47o41kpD4uK4zkpQ5Zed6BP7lna7j01IsBGL0SuIvwBKHz1BT8Y6VE20vrOoLjet19uzxTDImkcLV-Y8VDvo7SvBALvZI5-wbHlMzRFrDS3cOiVr8EaE9ltGEdHWQlrMTg8C-efTI64CC90kSyqSr63vZBe4LTtNcany_M0l9ZnJFKwV5_U79HW4gtTB88-bShHfwn1we66kF-oobp37zt6FsnESyq-b8lTrAe7CsBKQpzhbEeoPBAxFpM84s-9ZkYzOjPnYeMTLG1gq7Yyn7dQpJB35B40PIyPCrvl67qMUanflqZqLUT2XfHyOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇪🇸
❌
تمرینات دقایقی‌پیش اسپانیا بدلیل شرایط جوی بد لغو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/95344" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95343">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
تو بازی سنگال - نروژ هم بارون میباره اما فعلا شدید نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95343" target="_blank">📅 02:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95342">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
دوباره صاعقه تو ورزشگاه رخ داده و بازی تاخیر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95342" target="_blank">📅 02:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95341">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
دوباره صاعقه تو ورزشگاه رخ داده و بازی تاخیر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95341" target="_blank">📅 02:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95340">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhO09q7xksAwmlTZUNOfBsdXt1gOrPdQJeIaEV_dQj7CT5YhC4dqvPWfQXSRZ_NnZNuhJmvP5vELq_UxJ8szT8KLPL7DU_P5iVsyxRJMAPe5PQ_mzJgpTBt4QU3mEmcrOT2OrD1qcIhutv2qSo5ZmMFro1HgOxjWrlJ6aZwXbji9Slwtf-OUZU0-xCCTRwzDT7gFuYBAnbc9DUC45_Qk_v6CDbY73UcNuYg-s2PMln49x1Y6hHQvNaLr5qDgzBW9XTOC0WPlRoqcrNQh6fXV6M1eOo_hgMsf_hCzl34RIir-5kCAoyitU2i6nRgifHSNr0NsTonHpp2MJCGS-GJSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
ترکیب سنگال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95340" target="_blank">📅 02:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95339">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
لکیپ : بازی حداقل با 50 دقیقه تاخیر شروع میشه، حدودا ساعت دو نیم به وقت ایران بازی شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95339" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95338">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95338" target="_blank">📅 02:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95337">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtumAJUI1bjU2h_MZejlAYtN9Zvrku4q2RcBULM7SsVqETSRY2nYCO8OWpKhxs7UIi_nifZEfICxGAurDiYqwCdckMpnQwb_VD6qEIgk-GcQUsJQe_1WiUPUPHfQpZcip9Workugf_OYBpfY-lcKP6EujD6uUAoEMNJ5GnAAuyyIT0xJDKwBZlX5qsS5kup1n0ib4J_N41d9nnq6FXg4cgEZ4xCxry1L9N9I7wKA4pDhENJ2YHD3wksYntDkdVlVTPIyPtg7yrUzkiG70lLjRHvIscNlJF43z7IMp_GgEJ3sOCW8CCvgaMGhHE0I4rX8DJutGNbFIxUuviAN47oFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری
؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95337" target="_blank">📅 02:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95336">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBnGMyG2CjdSGZcF805M68A5aGRpPQ1L6LGnscPl1UM5_2dk_4jSGTO7gq99JvBJhUAtfWJfQImJimrykCBX4RPN3k6jZeeYiUB_gWYbBWpk1zuRqiEAluZCfjVXSCOlfiqa2bGE5nYdsJFMNYq6vfQjBypnG8u-AXEzH3dBOmHtsPCEj8t7T5k1LTQ5dj64QLH73zhnnxa_AfM3ZKFIUPQEgMJ62zCkjSaR4AKSO__GZqinvTIa59rKBE5km2W1viECEM8ocNCbKk6-uCerHMVvIZco5-8D-LvE5iUflxf9SCq-YXm7NNTX7Hbaap1GiHIqCz9EgDegpsevwZCuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چیپس پنیرو تو استادیومای آمریکا میدن 8 دلار
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95336" target="_blank">📅 02:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95335">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ اتلتیکومادرید با ارائه لایحه‌ای از بارسلونا بدلیل اغوای بازیکن تحت قرارداد به فیفا شکایت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95335" target="_blank">📅 02:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95334">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkUS4UNrBQwRr0t6Qrdo2tfyAaa424dDsSbKrkxMLn0qQfFpg_zbXtB2anl35mN_8w9G618Ucnp3bi5_Tojm0XwkCYYkjTyB0AwIXMYgbyfDgVXw_F6fJIu9ahAwG7HMoT0OZR12CB-jpCHdy-AFbTfAZzucT4PP_KmoROSOqbshtI96zldRRHl8fu9_BCfFzzUViObTq6AtD3XpgaMjAZd-4xkwvO-1JPo0BDKsVRPI42ZlsE7dFSGtw0Ri-8kLZSvsQzz4Gi98AAkADtr4-9OZp_oyXufDHYxNZa8nfyObgrDtfdimIVNt6rlOmDfmc0MKg3xfwlbjn_hOo1DF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
ترکیب سنگال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95334" target="_blank">📅 02:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95333">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🏆
نیمه‌دوم بازی عراق و فرانسه حداقل با ۱۵ دقیقه تاخیر آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95333" target="_blank">📅 01:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95332">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری؛ باشگاه بارسلونا طی روزهای آینده پیشنهاد جدید ۱۲۰ میلیون یورویی را به اتلتیکومادرید ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95332" target="_blank">📅 01:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95331">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciun67hUYyU5hlUm-QtMwJ4SkiKQQ8m9qEJG9gvg5XNrCp_UtqMbT2UenjBy4Q4g2KychrzjrsPqPgd0rjG4z-KyIM7o0912bx8cA4sGX9h3461fVnUQoC6c2m6DIqlAHDhuiaLu9YIfIm-7DV5bc5WRRXlOa3cKUPeL8MYKM4fKo9VswgR2UexARouqBQ4FGOXFvvmG-K4rUsx8UQ2xi1YhzdADe4BBI6ydcyTOLdBbuJ69G1VYtg1swRqaUZtYgo32H2D8JNXwIPux3h27gbTbikia2MOl2YImDwe7v5Ia9C_fmgs5km1pL41lS8oTf3nE8xpHX4yrAyHdRWIuKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرشیو وار:
پنالتی فرانسه در نیمه اول سوخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95331" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95330">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DByfw0_DetnSsxyCYm4YJabul1vO5ypcfqRcs1L0T75nlK8NK5eaPE32owcYuK6fNmKqou_saGRe7kRAf26eJ9_2aSWF6ku8xDTB1ZmafuF8R8HL7z-fzxU2VtsaaFqAhIzyLj7YEzW8HB-blcoRYE6_MhmOqHUTh1MJVNUaRuYNUIA2gniDDBlf8CGwJGvEeNXfdFV8Y-fH9arjG6rWe75KT9DQppvIK-N04T_CoZDjnjSXkGrPS2nHKXwKEd3dFe7CsvrQs86eCLDUakq6iEc1Y9di0WnZSNzR_wU06JM10luMAkGlx2ZZwfXDJfpQhPd9nU-ioM4QTecf759tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری
؛ باشگاه بارسلونا طی روزهای آینده پیشنهاد جدید ۱۲۰ میلیون یورویی را به اتلتیکومادرید ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95330" target="_blank">📅 01:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95329">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sX5nt6clXi7xPWKweF-czEcpwfRxTGZqR-HKvIFKlUc4JUX7B5K7BUJb5G0pEwdQ6v-ejK64GLl6ZqhVQuf3crdt5pbwyChu15clEaVf7iJ2X2zoBHYF91N5uMPItcOGlq2o8e5me_qWi53aH0zrGdZ_dvw80NJ3tRlgUybHKCMkNX4bFpEnmyFOJ_kzdvHCwc51T2oVFmN8KfJdzcmtycJsWwY4IpGy7f5U9yrCyM8ok2ZtUX3I77TP8jfW9sRuxeb6NaTZpv_IL2q8S725q3FXyD00Ss1wzydWd1ORU-m_TbCH4C4yRp1itOMyOBIUr3qCvOHR6M-U397R-IzcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
نیمه‌دوم بازی عراق و فرانسه حداقل با ۱۵ دقیقه تاخیر آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95329" target="_blank">📅 01:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95328">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🔥
🔥
🗞
#فوووووری از رومانو: بارسلونا با آلوارز به توافق شخصی رسیده و اتلتیکو از الان مجبور به مذاکره میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95328" target="_blank">📅 01:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95327">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پایان نیمه اول
🇫🇷
فرانسه 1 -
🇮🇶
عراق 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/95327" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95326">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wk39N_YrDPRte325QYoH4F6TYizila67x-WXpNxVJwPoCDaajh28QjbF3fzkFB2L-PGXKd2hLzd7_3ONGOsRTO0aae4hzP3PTol-xeGuOsKGr2dYGtNO5PQpODYcMrBRzoRY1YXL0Vs9Q2DIvpnMn_CmFDK90Dpi9nwL4DrrKIi79pQ9JGAeNbMsg3oIPNT-NASiTi4omLWaH3OWx78e1vsmvHNbqyq0a_cNq-rjbxYZvUPZFqqjyOywvlo6fts-uPduyvCyCKQe9wny1ZNIv7lEFQPhhktYxniuHi1rHFUilCPLZNU58qntzTb50HapC9LfmMHbFcEP6jX_CBl54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارون تو ورزشگاه شدت گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95326" target="_blank">📅 01:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95325">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm9B_G4C3Vk4rhmC-zzA-1NqHnqr1JVxv9Lhv5EfDSo6DJOKR4I_nmwjTeR7W_LHv9wljQqxVwVe1a6tS-NAZNXfmGYtCEaLw8mJoU4XhlHQ4V9tlcLbLXeleSMXWbiyP4BF2ie11Olp0-wYusM1gRIouexLU59yPdsWUzH8bUKW1NJ61O_ZElWvW0evqUkuxHNfYCNTkn_fUuYFFj10Ex6PhVU88gEXD5-g_-3P90fxumDrllHbf11i016kjhIMrEIJAzDN3vmjkxo28VKRrXNBfo-XCrWIFd0trYzVOKPYaMSevGAP7L6fsvQcqq3oOeK-9FrQLmzPoSmBnfeEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکل فوق‌العاده مدافع عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95325" target="_blank">📅 01:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95324">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ اتلتیکومادرید از خولیان آلوارز به شدت شاکی شده و احتمال داره جریمه سنگینی برای این بازیکن در نظر بگیره. آلوارز اصلا قصدی برای حضور در فصل بعد در مادرید نداره و فقط و فقط میخواد همبازی لامین‌یامال بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95324" target="_blank">📅 01:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95323">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVglmnPHXloNamK3BS_GA5gNwan2TVs-5_BCv7dILbqHIsVviVYKkPSLdrLBCf8pYBiDoiwdk5Oa4PQ4DuWbPrAeVIMUCdMO8asX8aYIVS29Js0mbonknFMjt1-Kie8IGB4pmFdnt-oSoXdsaBXY0akf-yhDEIHfginC0uAuJkQdB0D-agxbv3L5NOzSV0IRRCls_gDATfME-q2sp_zOPtGldETSmd0MUQ8u54mp-nsPomrCz5nJ8jDUYN5PVNnmafxAbdjZg-iz5x46yvr8DMTcR9-PkPmIA30nCCxHRxoWF8ueccgY0i0Hcb4L-sstztTwF_Enwe0bTKwuOWyRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه به جوان‌ترین بازیکن تاریخ جام جهانی تبدیل شد که به ۱۵ گل زده رسیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95323" target="_blank">📅 01:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95322">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHfRbql4vyC_gvijc110ivo84pXeOqSWQjjSSts3V4z3x8xi04_K549A83dW63f8xE9WqKjO85LsHcKXseTpmnPIX6dRoctHUOSWVt-HLjOHPgauDhIMo7i1blW1gyeG9h2G20nDyzjO8LC1eo1QTBrfR0FdhpYD9e1hHLumfTnwuEYx0nCazg9Ah6uh8TXRCmNDkZg9KiTwlR6bfL9PSbjA0ROKeJvWLJPbUFcVQSVl1IoL_8Xkb__xLfy9kl9uPjNoZk9Bbn57YHnDHB8WCNkNvgoO04sRPBmW74RNnjTwg-FKlmjHcn5WOmQLa4n2vewomPEeJH3lQxgWmD-6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه گلش رو به پدرش که توی جایگاه تماشاگرا بود تقدیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95322" target="_blank">📅 01:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95321">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9ad943b75.mp4?token=MPhED4gIaIyRvGxfGSb2cPLvEuNVucwhQikDiQAU0zn4WfAkHOFO3Z7QQssXaQQYueuw4jBH4O2h2R76FvZZuvdgC8MnoCv3Mw_4YDyBPzm-2Hy2PmzuJztG07gkuzu8w7Hgv7Dnu5HphapZjjnqo4D9wQkXEHHZqrpbe431t5ya1uNvMX4Stn013kKgHekmlPb4vyIJo-l0_Ex14e-Ue7FO_9Qcr2nYU5x57ckcjmupfGM3BZxY0PWdXOnIMi7R6ngFkZ_AfVI40wlVybFidDo8hgYsotgXA-BGN8gzED4xiHahqCZjXViE28ve_FLa0OicDCu6PIrd3rOBMugzsYr3YrxrsGdwHkQrBGLR-bNRC_O7SoaMVkjOm4ZvfAb_t7N5-Axml0GYxFSgL3RJZ7ssd67UBnqpQ3vsJfD-0PLklHRx5HU9mO4BIfqluaragcvI1I2XpelNtLqmTrmdNF54Rc55nP7zgCMwP-GK5qlzUWEOJFMVLzg-jfeeCSRF-u4BL23DsCP3vA6cT8Po0BXanSHDZ83ATotSVC-ua0rFGjLmp5FzEh4hRIdzQZs2cOqWApxEwVeJDK5VZajxHet511t-Ab4lwd2xEyN3ENJgjuoeetFjY0okJed60L2o2bp00kdOZG-RsAHwiJ5ymdW1CR3Aim9DgQvDh92vgcM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9ad943b75.mp4?token=MPhED4gIaIyRvGxfGSb2cPLvEuNVucwhQikDiQAU0zn4WfAkHOFO3Z7QQssXaQQYueuw4jBH4O2h2R76FvZZuvdgC8MnoCv3Mw_4YDyBPzm-2Hy2PmzuJztG07gkuzu8w7Hgv7Dnu5HphapZjjnqo4D9wQkXEHHZqrpbe431t5ya1uNvMX4Stn013kKgHekmlPb4vyIJo-l0_Ex14e-Ue7FO_9Qcr2nYU5x57ckcjmupfGM3BZxY0PWdXOnIMi7R6ngFkZ_AfVI40wlVybFidDo8hgYsotgXA-BGN8gzED4xiHahqCZjXViE28ve_FLa0OicDCu6PIrd3rOBMugzsYr3YrxrsGdwHkQrBGLR-bNRC_O7SoaMVkjOm4ZvfAb_t7N5-Axml0GYxFSgL3RJZ7ssd67UBnqpQ3vsJfD-0PLklHRx5HU9mO4BIfqluaragcvI1I2XpelNtLqmTrmdNF54Rc55nP7zgCMwP-GK5qlzUWEOJFMVLzg-jfeeCSRF-u4BL23DsCP3vA6cT8Po0BXanSHDZ83ATotSVC-ua0rFGjLmp5FzEh4hRIdzQZs2cOqWApxEwVeJDK5VZajxHet511t-Ab4lwd2xEyN3ENJgjuoeetFjY0okJed60L2o2bp00kdOZG-RsAHwiJ5ymdW1CR3Aim9DgQvDh92vgcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به عراق توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95321" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95320">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دیکتاتور چی زد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95320" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95319">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امباپه اولی رو زددد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95319" target="_blank">📅 00:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95318">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95318" target="_blank">📅 00:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95317">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doIxpnHwUBiw6Y-WNcoH17fDCUhrfzxMx99uiCpsrkbTl9ufU85vG6sGFs0T3kNhtgmoSaoMyRTzy-wOlX0VH8V9oABetRkoSm3x6YOBH-Es7ffStyrPEIzxmnfEJlJazd7e18mm4tBv3Qu0OdUoOzoyKNyohlP-GeijdQzFh8_ITjpc-VbWsBXgZZKbG8jWX0wUM4PtAbi45U2Mwo2j02JrIfM3N8_LrEbEc7wPRPyK-kqSSvif-ROJctBCQ39UPpsBP__QPQjXf_thU6koKJFxfYkLomaRNqDp3q0hQfxG2giMRPs4mn2Squ2m9fyPKsz1OO6E_1_j22Pi2f9q9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووووووری خولیان آلوارز: من می‌خواهم رویایم را محقق کنم. با افرادی که باید در باشگاه صحبت می‌کردم صحبت کردم. بهترین چیز برای آینده‌ام رفتن به تیم دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95317" target="_blank">📅 00:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95316">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj6IeSJn9w3Rq4GINGOfCebyW8V3h_yO9_SriRfAv0GWnkwflALFTQX_hGX6lTztLB4nJo2rD3sEvD7a2Ng9LFT3We4Q87ItEfDnM5BGZlB-JdkZef18dYywE4FSkMbzHk3CIAMke_iCiblHvd4TCkxfmAxGE0y_xaPYwSR2hoIiutKVeQ2yGHdvfw1Lnpdc-Mg0PdqlL4iK7gF4kTtrm3G4eqK7xBNSL1lc5rPtbiFjUhZJ4zz9hpBSGD-Y_lIgBRpKt03aNIKFClOuLJn0n5Ee27Cl6qLIy33PzvLIJiHvlYrZRCvCXtm7WaJ32gx1HOW7wYXOgCyj4WIldA9jXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار خیلیم به کارل تو تعطیلات بد نگذشته
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95316" target="_blank">📅 00:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95315">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EcwF7IzocSUK08HoyGZlsGd5OJGkbVF3zfalHH6kgeaMujUHUCSEAFnMYYFD6ajItBU1mgzT8sfdnD8CjjllKDcSUfSh3BK2xWP0yOf_JbbWL1fdgUsuyymN8B4XarXZCi89ZrTBNDQTPGoVvEji2Crp59viLlPEn29GjUS9sOdDIiikPVRQoMtXmW9EhW6Ac88UTGEv6KEoiK-MVmWqEk5STgeBNNHS9aR1WHotfImOjnZbBvwjbUT-LeE1WVn_9audwkPM49CQTx1aXfpJuPRKEhRYit8tEYSYuCCJcjoqH6IO3Sk1n4SWNAZOuUHje640yR7jnlHGnRvDlED1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔞
🚨
🔹
اوه اوه
🔹
🚨
🔞
🇦🇷
⚽️
🔞
بابا بنازم طرفدارای آرژانتین واسه مسی سنگ تموم گذاشتن ؛ دختره بعد گل امشب مسی تو ورزشگاه جوگیر میشه و
ممه
هاشو میندازه بیرون
😋
😍
⚠️
🔞
🤤
برای تماشای ویدیو روی لینک زیر کلیک کنید
👇
👇
👇
🖥
🔞
https://t.me/FoootyHub_Bot?start=qcipRV72
💯
🔞</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95315" target="_blank">📅 00:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95312">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
فووووووری خولیان آلوارز:
من می‌خواهم رویایم را محقق کنم. با افرادی که باید در باشگاه صحبت می‌کردم صحبت کردم. بهترین چیز برای آینده‌ام رفتن به تیم دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95312" target="_blank">📅 00:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95311">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بریم واسه بازی فرانسه و عراق</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95311" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUT3x7g8l85o7ZxrwusORtT0gH7xwWV8Y7sWebzk7uWPZx9hnWBvLwnAlIPDd9BgmSz4FmdR1zaklsrdktNyvLHDB4MGQ4V5e4TQzQAw9MRJu3zyIriVysVFLSoOyMcNeVEU20jfowkCXqHlLYhflSHEivc2kfBI69iJN-wIpxxzOIk7NjKG1ajMwJ7VujIfAiLrnapSMbr-fTU0OZghChcjvAQEM1tjX2zaW2T_HIBofL-1TWXfdcLF2MVojVa6vV6h8oFo2mVHMaR0J_d74JGNr9ugHORH35UtGp0y0Tht_S57TZ6fPDR-WE4p6fHjhKIPtgL2TA_7xKGi6nhL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
⚽️
تفکیک گل‌های لیونل مسی به کشورهای مختلف در جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/95310" target="_blank">📅 00:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95309">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoGQCE5-MZK_uOm4PidldbNQnASnmZbAaerF3rBV-11lqMnggzIN2onYwgS2YSoSc8mOPCEdfVM1au1g_9Lec9UFjQfwpMEy9PhxaokAlSWJ2eWDhdSBksnHWgxOmkURC5g3JxusTlzccOY44Og4_X-OTeF_qjSXBCmF_9_RVMIG4GsgrNkwtNTnsgHvulfjp4byNUOtSkD_CSI-pOmwE02c4w5VODX-kmqiPdmOIm8HtyRuMstYnKtWjC_LW9URfv5Rhkj5OjYz88eug1X0QK6pHq8mCqICgSYiLEtgc98yx-Jxoy_ib3zXIEM6EPWXiC80H9sU4GO3hiLmNQ0JPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آلوارز :
مسی رو با کلمات نمیشه توصیف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95309" target="_blank">📅 00:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpFTWPa4iYWO3R3bhVKaKUFnJTqoZg3P-hCsiddefg88mB0YhaU2FN22ThV7WQOlWbdIgNlQlprp5gXODCkjBQDfErMH4BiccIUZMgD0KRGDoMacH2orL6IaeDc-Z6pzE_zzgO_FRCZ1-Pu-ecL5ot6OSvx6C4YixpzfaILisNx0KkMPdTFdFkzrUM8J6DmBGTMPgsYiodkWWP0tvOHIjgfHRr4F4-U2d6pm040jZcl9DFd575j3As3Js5C_oSk_ILemaL-hA_j_7l3Ui_I46r2ZFxCXOqg31GJbL59xMSU9mZLXaXo8KrhGXFrSOKV0QKILaGs7iW3ojirprP425g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب به تنهایی شرف عراقو میبره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/95308" target="_blank">📅 23:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95307">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dm8MYOP2AHwGixtdDwbcOAQf0_DymxUmNfqK3uo0Zh6oVDAQ7DgE7cjY4V-QQK6sWU7qF_OaPRYKOEh_vPv8N6N9XRoQG-5PzEdhNjGxhh4pF7NvSpHwYV4cZBuuJtlF0uhGM18uhgpjkGtSQ-m5rqtc3Ser76fu-5eMFTc0DAfoOMN_GEsoxJdh9LDKYv9dymxXybIeMKjSOocoVhwyNHI4fgJu3dpScgmTJzBAntnTyfTWX5HTEP2OewtmoLhFhJXr8msnZj2BwnETcsJ3utri4RvsRei6fVF14jEC3FI9UkRkOz2eLNiLtnHWKINxlTC1tx69o0uqi9nUVGvHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورگن کلوپ: ما هرگز بازیکنی مثل مسی را دوباره نخواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95307" target="_blank">📅 23:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95306">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6777a2d2b.mp4?token=fQ9_9Q4bDh2x36uXNiiSG9cwgxXd9WjrOU0gJb1wcSyciJ7AZNr8OPJwQy9ihZeqJgHnyUdPZfLC41vL3xLchew83v75SkD7PA0qxCJdK1h8UUWBpMhB-hIw-eAHyg0wyZ9_4_kYwjRlJSIcyYHXmMLuQFrCizD0c9qMxDDf-gMAlSCs6MHnl20Qn9fQmCcvdklBq_6iDE4HfPscI_4GTVoIEQQzqERKIxBaD_IRbaQ6rUD54Dh5AWB0q42PSIq3lPFdAKfZp9gq6FuSqBS7dI2bD_kKq7KrkmSHEI2yFDOFsARQupwq_9gN-7QbijCiyFGnCoVzc7A9q7vXRWMu3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6777a2d2b.mp4?token=fQ9_9Q4bDh2x36uXNiiSG9cwgxXd9WjrOU0gJb1wcSyciJ7AZNr8OPJwQy9ihZeqJgHnyUdPZfLC41vL3xLchew83v75SkD7PA0qxCJdK1h8UUWBpMhB-hIw-eAHyg0wyZ9_4_kYwjRlJSIcyYHXmMLuQFrCizD0c9qMxDDf-gMAlSCs6MHnl20Qn9fQmCcvdklBq_6iDE4HfPscI_4GTVoIEQQzqERKIxBaD_IRbaQ6rUD54Dh5AWB0q42PSIq3lPFdAKfZp9gq6FuSqBS7dI2bD_kKq7KrkmSHEI2yFDOFsARQupwq_9gN-7QbijCiyFGnCoVzc7A9q7vXRWMu3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا بیرانوند: بازیکنان تیم ملی می‌گویند موهایت را نبند چون شبیه یارهای جومونگ شدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95306" target="_blank">📅 23:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95305">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3ab2e493.mp4?token=FOn-Yg_Pk_4pv6WdsFHVs10y89fCHpWqQ5ErI8z9YdXmfuONP9nP36ipVZ4VZwiW6omdvslrk4g2NW8kBZPVxVYNdK-SnnbD89kQgCfC2UUZYLe9SJJ26rXtdPw4_XaHnw9KrduKTqUsSJeD_u8TK8XTvjEuAg4J8IbHYGGhpTxNHKckV4GS6EamoJgrEpPlbhTTS4iD8WN2yEdoHailYrl1yjh6K-CjjR7QFI0GHHzb5Oe-l1si9l9NPByEsCAeUmgnYtsWwRw5DP94Nem4sPdLCjBpLS-Ifk2jbEndKYOO04RZk-de0nVJ0KP7CfRavwEiZqwgSK2uIoq6-uc4OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3ab2e493.mp4?token=FOn-Yg_Pk_4pv6WdsFHVs10y89fCHpWqQ5ErI8z9YdXmfuONP9nP36ipVZ4VZwiW6omdvslrk4g2NW8kBZPVxVYNdK-SnnbD89kQgCfC2UUZYLe9SJJ26rXtdPw4_XaHnw9KrduKTqUsSJeD_u8TK8XTvjEuAg4J8IbHYGGhpTxNHKckV4GS6EamoJgrEpPlbhTTS4iD8WN2yEdoHailYrl1yjh6K-CjjR7QFI0GHHzb5Oe-l1si9l9NPByEsCAeUmgnYtsWwRw5DP94Nem4sPdLCjBpLS-Ifk2jbEndKYOO04RZk-de0nVJ0KP7CfRavwEiZqwgSK2uIoq6-uc4OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش دانلود به شدت بالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/95305" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95304">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ: پولی که آزاد می‌شود برای خرید غذا استفاده خواهد شد و این غذا به طور انحصاری از طریق آمریکا و از کشاورزان ما خریداری خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95304" target="_blank">📅 23:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95303">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b7d3caa97.mp4?token=seAnughIg53hKeX6emPN-RiEntH21lzMH1XourilAr1rKQBee05N7OzrOD4feNRPBGp9crJl8TCoL4f04Rv_EhAWWidOqso15EOupZHQNtvA9XGu1Q6KuNYWfxAstM4X-OOBigxVCyQOfa_drv_R21Wycs8QoN_hZweUOrZTAx0hO6regqSTnSelELcAQ2bbvuN0ETn4-lLZLOlbKV9fzNrLd_JuSa-gRYrcDRFcHy-OTNJDPm6CVfuvGJYY9WyFUJR5VDyTc50Z8wFkXYjnholcShCId-JwvSgDhLJbZLTTafYrt8KrOTfpzM5PgsdPAXI_wsTH-BXwtbkL8cOKZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b7d3caa97.mp4?token=seAnughIg53hKeX6emPN-RiEntH21lzMH1XourilAr1rKQBee05N7OzrOD4feNRPBGp9crJl8TCoL4f04Rv_EhAWWidOqso15EOupZHQNtvA9XGu1Q6KuNYWfxAstM4X-OOBigxVCyQOfa_drv_R21Wycs8QoN_hZweUOrZTAx0hO6regqSTnSelELcAQ2bbvuN0ETn4-lLZLOlbKV9fzNrLd_JuSa-gRYrcDRFcHy-OTNJDPm6CVfuvGJYY9WyFUJR5VDyTc50Z8wFkXYjnholcShCId-JwvSgDhLJbZLTTafYrt8KrOTfpzM5PgsdPAXI_wsTH-BXwtbkL8cOKZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معیار دخترای مکزیک
پول، قد، تحصیلات، استایل، بدن و...
❌
کره ای
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/95303" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95302">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d02fae5a3c.mp4?token=eJbYZ7-oAA7eUZs8j3Dey973p1eRWhwTeqfXgN4SMgZQU4YqMtiRRNwm7B7jBbAj2OQA6FZzgmN_3jClOZX9yGiTuiEsss3K4I4wYAM7IRd1azgP3TS77lLbhwE61Bt3JtuA1i4ap-MKrHB7KLnuW4pla5MsZVrgMsD-VuF2I08eJeLgi7Fxd3Q4tVj9_2V7_0qmXXGHR4xOl3quYF1eXB1CsfoMsoq6yxomE7uJCUcHfMzfwgDZvfzmUggmmL2IA67x-sOCsxx8Y0-juVNJKaR9W4qnxsGZBFtw-s6BpQQI9cvisP10kaX7Dq91ptF9CAKVk5oO-_rejx4_r7Hepg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d02fae5a3c.mp4?token=eJbYZ7-oAA7eUZs8j3Dey973p1eRWhwTeqfXgN4SMgZQU4YqMtiRRNwm7B7jBbAj2OQA6FZzgmN_3jClOZX9yGiTuiEsss3K4I4wYAM7IRd1azgP3TS77lLbhwE61Bt3JtuA1i4ap-MKrHB7KLnuW4pla5MsZVrgMsD-VuF2I08eJeLgi7Fxd3Q4tVj9_2V7_0qmXXGHR4xOl3quYF1eXB1CsfoMsoq6yxomE7uJCUcHfMzfwgDZvfzmUggmmL2IA67x-sOCsxx8Y0-juVNJKaR9W4qnxsGZBFtw-s6BpQQI9cvisP10kaX7Dq91ptF9CAKVk5oO-_rejx4_r7Hepg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا بیرانوند: مردم ما ۴ ماه سخت را سپری کردند و همه تلاش خود را کردیم تا دل آن‌ها را شاد کنیم و شرمنده آن‌ها نشویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95302" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95301">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNd5bwL6YDD9ZHvpsob2597pPJfgfseiXTm79mrmmLGJs7uTGVWmN0CH3nedtADX-6JOAvAvtkCcMslNGoUt0bePHEapLSNLAFyy1RkuJfPXZA2MapKDovsAeoLJHw0Il5Yca3dQUT7QsYmCTdX5ujAKTd5EeytEK6heMM_e4yB_VCg1M1Ch_w7mNxenN1EdlFx_-CVqs0hCNq7fiaRkuwsDtl9-fgNyfZLMZr_2JbJ9s1qXVb6NUQGmTV6JGZrQugdmD7P8NGNDGx09Dy8Y38crRSkCHKg1UzaShY3pC3IG39jOrPMLLdusXmpItOsalZf6OLk6t7Q80dyUe7_WHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لئو مسی با جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95301" target="_blank">📅 23:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95300">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiPNzSQcHxDensOwPlA5Didwa82OkHLKEDXMsLqq96BRv9-49gU7PRwGofW7T25TalRvTy2Zo-kL3_-ZpWo5aRbCPAXT7xNE8ifUa2KBVjKpyCMnkB-5DNRWum7sRLjxvGoUxghX_BmKdIGDNFBCEgcclIAx_xKagoqgydlKB9WTs0Y6oQBj2FTP9exe48KhUoz7rG16K846w6CrN6a_hx2eRYBfz23JFk2kBAd6r5mj5S1XImooqZbY8Ztl1zdwq3LPwZyt4FdmMsS5uhi8RtI7V2kR9a58M8seYB8k7O1-VHz-YAej_cdutKTjJ6NULlBnMUDOXsDDOqL8Gx_AIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی در 4 بازی اخیر خود در جام جهانی 8 گل به ثمر رسانده است که با کریستیانو رونالدو در 23 بازی برابری می کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95300" target="_blank">📅 23:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95299">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dee5f09984.mp4?token=WSWd02cK7fmjLbQ2gY5yAWqwY9Pseroc_PVxiwHG3Z0XJcmA7-KA-Csb4kg79IOvfXl2tJTqxnpAYpGl_d18mLMMbCROqIkIZMql_yS2XDvvGOGnFogLZJMS2IooNhGnZiMa2fdhNeo3cvf0j_SX-0971rzLUpaFCfF4kwoF3XlI74I3gYEBx2Jtx6xYxfH-89wL2aM0hgtBXNk6x41d-WY2pQ4--KKD0-BkHRYIBe4ypzJTHzTPsOOYXkolZ3vCKW8SmjVdXuddznxyVbF666jSibNDBUYco2pPkXcIJ9VREpQIPmLjkX4HrdJrfJnShQr-Li-IzNh6rnT0nc-zxY0aXvBWxQ6qHb8Ly51CNj4ZDK8J7NzIO-FCa0qmk7CIonMLx2pX-awE7Ofb31w-3ud97UQcztdTP1_NceUBxwO9yBlYZ_RYrLBcowBA1Vqw0BEs1fDzTt3HiOnBWiSI6OWoFdflTTlIQK2kOi6ahZsdbPLf8KoEKKfbAlxz27GGMc4h30pRanoQBXhDsy7SzqNWISjhESB6sA9BAeQrIDENbwytUdKlV7RfXnB-L4mBtkAL2dVvFHXeda1tqGzsxD4ZEnQ8CAEUCyPnj90h-H9LJE7weUX9V-FZ54BFJ7YHjQSEZ0B9WUi-uej3HIGuR73lNenljW12MlnAVUMyAUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dee5f09984.mp4?token=WSWd02cK7fmjLbQ2gY5yAWqwY9Pseroc_PVxiwHG3Z0XJcmA7-KA-Csb4kg79IOvfXl2tJTqxnpAYpGl_d18mLMMbCROqIkIZMql_yS2XDvvGOGnFogLZJMS2IooNhGnZiMa2fdhNeo3cvf0j_SX-0971rzLUpaFCfF4kwoF3XlI74I3gYEBx2Jtx6xYxfH-89wL2aM0hgtBXNk6x41d-WY2pQ4--KKD0-BkHRYIBe4ypzJTHzTPsOOYXkolZ3vCKW8SmjVdXuddznxyVbF666jSibNDBUYco2pPkXcIJ9VREpQIPmLjkX4HrdJrfJnShQr-Li-IzNh6rnT0nc-zxY0aXvBWxQ6qHb8Ly51CNj4ZDK8J7NzIO-FCa0qmk7CIonMLx2pX-awE7Ofb31w-3ud97UQcztdTP1_NceUBxwO9yBlYZ_RYrLBcowBA1Vqw0BEs1fDzTt3HiOnBWiSI6OWoFdflTTlIQK2kOi6ahZsdbPLf8KoEKKfbAlxz27GGMc4h30pRanoQBXhDsy7SzqNWISjhESB6sA9BAeQrIDENbwytUdKlV7RfXnB-L4mBtkAL2dVvFHXeda1tqGzsxD4ZEnQ8CAEUCyPnj90h-H9LJE7weUX9V-FZ54BFJ7YHjQSEZ0B9WUi-uej3HIGuR73lNenljW12MlnAVUMyAUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرانوند: مهدی طارمی قبل از بازی یک سخنرانی حماسی کرد و به بازیکنان گفت اگر سر خود را در مقابل بازیکنان بلژیک پایین بندازید، بلژیکی‌ها ما را له می‌کنند و آبروی ما را می‌برند و باید در تمام لحظات سر خود را بالا بگیرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95299" target="_blank">📅 23:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95298">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjtN1fzB8lVPwwLSmSffM8B3uXO5uEBWIW5yAD_7hZwWYzUNjbuYPY0W2p5FQMt7UeSv3qSzTVtzifqFiVnctm9c7Gf8KB0dULCp12DP7dEn8s4NBZ8Kp4H2uxSjV1kL5ozaiXbg9vJemrUtG-twrUI_wLRisqMps4O-J9P_bxHgQBEYpMTIH15eTKi0DratCuKOpO44zB353bBKt2BwRvNtxfIZnIJS8syu5TXXTpAg_3NNqpuWD85LOk89CunSqmU4aYF9fter8SaOumBiUyu03ldowyvH-7KquySqDQz779ri57FAJDLg4xRQ9hzkyA4m4fdr7q469oSPCcOptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهره کلوپ بعد دیدار با مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95298" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95296">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZGqjoQeCPSPoAGfG9tdjODw4DkKXoVLq2vbdyHZxItwT2xThE14h0gZ3cLt-DMwaIXSIA3FJKiTeWwrd3PcHSXok8erZvElhEvWElsMKRd-L0ev6wuQvui5v6AvaJMK7Kqi21pM6upUJwwRbQILeQXWi3KFi5ZwCM-nSZGB9M-0ziL-VKtVBKHQCPlkCPeNc_8NQ9LSHr5yjfaWMwJPASqxNDP_KNI_QElo-h3ulHCcZB_9afKHVe8ZPrLoPLoYD82AGe0pX_Dc4ae087luAEpEr9r5KtMquTxOiR7-npCWZQMOO85xBaLC775yCsmbQ-sslu9lP87By8Nncuxczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmpOruYayKMdkeZ2ZUqOdc1BS_fGGoid_EvaHQKTvvTCrz7qN_8wZfyi1ytYRSpKMrZ0jaZ88aonue3VriZbXDO6zNLFEFHh5_HiMYzhPATyaZgMhXRldf6XJ4XgW8aTULiLneADdM4OcQP4RXr3bTwzp2gCJ1zAyyzmEzhWObV37X2vsiJ3TBHT6JuaVVnt2oBKEbvvp0OtsmxZflWch8IX1YA_K_tzNQKIBDlfNiyEUkGG3k5CEvOOqskVQ1nrjT5TVqsGCMAHnwQjMK2luFQXj4RhhJUQ46765nMNf6w3XMKnJdG8GKflCTWGuXyp2b79qADAenfl0iKY2LO-qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
میزان توجهی که خبرنگارا به مسی دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95296" target="_blank">📅 23:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95295">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7151d02512.mp4?token=EQfSXNKKkI7XoSaIxRpvD2ZAqfarv02OQ6bnPc4_jI5hu1pSxBLsOEh8SY5QMpfANy-5pLAeFkZf6snnfQ6Z6KVicszG-xwwp-o-LWdPaTd4_2ac4ZjNiVjm22x8dv8yBqyeqcNAU2XmeNrUr5OaVWohu_AqQX9A2hFJVDBziogiu_vNH1d0jlXXwZJoh_hf6HVzijzlGmQvN6I0HmLDx8QwfHPh6qKlB5fXM99Hrfh_e25bV9oUGuseskJi3fOeAqgZTAB44h4TOBVedd9OjQg8Q9C5Zp4ZptJVFDyQuopL6M_33HGfRH-nXHD21hwq8lRi-RLWZl6AFcW7FYK35A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7151d02512.mp4?token=EQfSXNKKkI7XoSaIxRpvD2ZAqfarv02OQ6bnPc4_jI5hu1pSxBLsOEh8SY5QMpfANy-5pLAeFkZf6snnfQ6Z6KVicszG-xwwp-o-LWdPaTd4_2ac4ZjNiVjm22x8dv8yBqyeqcNAU2XmeNrUr5OaVWohu_AqQX9A2hFJVDBziogiu_vNH1d0jlXXwZJoh_hf6HVzijzlGmQvN6I0HmLDx8QwfHPh6qKlB5fXM99Hrfh_e25bV9oUGuseskJi3fOeAqgZTAB44h4TOBVedd9OjQg8Q9C5Zp4ZptJVFDyQuopL6M_33HGfRH-nXHD21hwq8lRi-RLWZl6AFcW7FYK35A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا بیرانوند: بعد از برخورد با لوکاکو، تمام زمان مسابقه را با درد خیلی زیادی بازی کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95295" target="_blank">📅 23:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95293">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOr8ANWjEvJfJTVf9FNwvLjv0uZyAf94WoRhndvKZmOwReyA4G8oJLr2jF1o5ncy3HhW3hlZtxDvKMkDq4LFGXs_rE5z_MBM5h6EsUUGPhlEpcp9clBxt6WaKRdncR3Q2JvkWZrMSTol80_bBSwMUCyAoolskJz1p844F4VhneLAJ8AQN0iKMVwKZ5EzHG6Vq5sSjM4xZMBeS33hmrq5lPecegWhT5_V_eoGk5WGS7JOtLBVnJ1K1fW3Mlucdfl4yMcLwN-HSRZlEBNNDTjgR2VrZaXG6kGhrnSXwSkrmV7S7qXfKxXAWsmSaxUWcic43Ci5lGvHECCr34y9S4BSTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJOYKGbFKh0QrwFIt9t8Ad9WiAKsZbL-27oE6KNQH6cM81_t9GqBjv_BKQrQJdE1VN3Vt8l9aMPdGHLgrBS3ynmhfW4qHYJuNaCb5pUTfnj7Zv2CZvItbsmgDXKMP1ROKJKNwxqPdzWjTwpiVgGuNFQh6eiSKpcUbuEYrD1P8yGyX-5hnx4G5NMv6LSC1uOR3Od1RBBngyHj_NnbCyHYJ2SfY61bR9UCLkSwhxPbODmBBO370g8XUsEk2-st5G9BuIjciouG1bWrwYwE5iWXftZD7PT_jlH8AJqBIpyaJq9W43lN1H1-JtdHSvHVFn5QVuxaeeNaKZsW4tJbUnj-3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇮🇶
ترکیب فرانسه و عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95293" target="_blank">📅 23:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95292">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwHB5pKFQSox7Mh8eg-lzun93xLHDVDRwZGK7iR_Sb5TGfT5igtk4Vndtc4J30vGD0dkS44PVuMHeKJbqV79WOmNz-RyKbfuyORY0wazK9yXK5xr0vSB5vD9TxSdIiOSANOBfOMsqw4uEfvgkgAVKB_ABRoHud4GWhoJj84sCn6H4rMELai-USRuFlb7ezx0Ftok_PgPH0kqTqDS8B3GObmMduGMjzpZgdzOqeB-izg80iKZTmwiF7oOF9TQ4008BO_9LtsCKyZefBgNlS3VkhWNwbfckPtwe7vrmZNDdM3dZ_-6Uaw9h1A2dDLc-hYVaICFBIOxtOz635VrGFUC1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خولیان آلوارز:
هیچ کلمه‌ای نمی‌تواند لیونل مسی را توصیف کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95292" target="_blank">📅 23:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95291">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d6be05b.mp4?token=q9fKJZ8NbDSGHpvX4N21Ti8Z62rnihnp_0xlQ4ZGQJ-2i3Q3daZUzn4MykCAw5lPqmkZJYhlpiExLDPBEM_UwbrlJtyxhZqHujvkgT59QL5KGOlXIct8Q0AL2IZKYfNc1ZPy_LEXxjXDKLES-7x5VZYU6Rd-kYdU36i48XZwwNplC1oCwgOFzujNyMcOeWnIxITsQ39hnh42iIcUyMUhMG395OCJWyxSC6wzpesikNBDGXr3RsGN4J0bRkBYHdPykt5sdR3jGBss2M4KedY5beF3X8oWVI_mfImi4GaMS11yi4gdGPxRDNRYBn4JFxMlKCtloBBmnQHl5ZWPx2VfHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d6be05b.mp4?token=q9fKJZ8NbDSGHpvX4N21Ti8Z62rnihnp_0xlQ4ZGQJ-2i3Q3daZUzn4MykCAw5lPqmkZJYhlpiExLDPBEM_UwbrlJtyxhZqHujvkgT59QL5KGOlXIct8Q0AL2IZKYfNc1ZPy_LEXxjXDKLES-7x5VZYU6Rd-kYdU36i48XZwwNplC1oCwgOFzujNyMcOeWnIxITsQ39hnh42iIcUyMUhMG395OCJWyxSC6wzpesikNBDGXr3RsGN4J0bRkBYHdPykt5sdR3jGBss2M4KedY5beF3X8oWVI_mfImi4GaMS11yi4gdGPxRDNRYBn4JFxMlKCtloBBmnQHl5ZWPx2VfHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا جباری، بازیکن سابق پرسپولیس: اگر جسارت دیشب امیر قلعه‌نویی را کی‌روش داشت و تصمیم مشابه می‌گرفت، همه کارشناسان از او تعریف و تمجید می‌کردند/فاصله مربی‌های داخل با خارج هیچ است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95291" target="_blank">📅 23:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95290">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcvA94NF8TJzmcEDGvMNjJEb7TbdzB9_mAkCeNgHvFsWSmaiUcVvmg4IrX444wNBI05-rONtlvN_EubvlSohN9O7PApdRqASGOnjD1iJk9mIeFBr9ENO3DsF9tHA2gvGsoKiruqrLJmw3iWKulpvE6Ut3sOsUgUnl801dZR2ioxPTPG9WCRca0YBa0EGeWDTO-eawQCd-VfqouvVKh5rhKt1PJJMvpqmjvymrVyIBOwt6_0NdiwUZZa8LIu_NSX-7yX6p-YPYn1KYTiSqgqLgE-ZnFErSB3IzCWMmLT13ZFql0aUKsJN6FWd0XxGcYWAcHYS-NOvuWrA-UxY7ALIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناظر عکاس‌های کنار زمین بعد از گل دوم مسی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95290" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95289">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej8cNxKSlUj2uECvMxDpJ4rxQtO0BInXKzBeIyc0Lx9jMrJS9S5QiG_GRnW78i6mPt3j9kbsCyjDlsHlrzFP4wsvIQanAmil2NGTnbEGSkZ5v7aFoyR2OGPuRyARTXlZuD0kgFEpGzqrxgYDGIw7Sit7C03YEDLKJwGTLHxsv_-oOgpben1ojKcOpz_XWCrEv7yDR1YK40rhWRxvgkBGMmABzCgysdAQTnAwb8jmz9VkYUURWsFgEIGF8SIIgEOwtlwe-RaAWMxhz68SyW9FWdp8BdYZusq08HiMWiLJhkzSpw7sND6XuwKb7Y6L7qfdyosrL-tmvUFetwvEfsDy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
افسانه لیونل مسی در دوران فوتبالی‌اش:
‏
💥
۱۳۳۰ تاثیر گذاری مستقیم گلزنی.
‏
💥
۱۱۵۸ بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/95289" target="_blank">📅 22:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95288">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMM72AgKE3DW365YMGlcJX0UT0jP9NS984eXOpqDvFtYmYd9C2nx_wEKUlQKhuK11eVd8w2RuZtHz-el9F-LzRf4BbFfwtmFCRs2rqclVyAPd1KgxlJoXKje8Gw-ejyjHAWCKqMvPo-2PbTsBuscN2t6u3qdTqUjO9M6tEyIXiazQa-qfNF1398mqVJBui4dAXP051HxybfTuAREwQXlN6qYntQ5XfRlUIPyRE7iXXDRASR3iVuPdjv_zHbCj7xkahHNT0_UdObu7PRTodfiM9liJFmzAH54OkQszUzUUBH89IiZq0u4WpMNu8LKzLqcb6DsD5e68I7wRtkGjO6SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
پادشاه فوتبال و لایق عنوان بهترینِ تاریخ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95288" target="_blank">📅 22:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95287">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMZCeEnVfL91s0t-MHRIor7ohYMfk7E1m0v4XBhF_3icXH1rymim4xSFajuJsoRqtay7g-A3XG4OSZKtWrwQJJ3Iaq-aOjA3ArLYbAWWhs4bKW9lWT95bMfdkTq6EIqMvYRWIihjx5oIhA2Y6nXBvZYCWHtIm1vf4uxLYm8q7hrGLiUqUb23oaDGVlvatGcJrdfvVED2uodFr3Yldc0PNo3tnaq-8n-1NpZ7lfa2fy56EIJuZVVccFJ1NqWKd2TIqNhXccEISg9Bd2CYvX2Nhuieu12iBl4VargzmHKdEHcPajavr1c5XzgyCeUoOREp-eBwFt1vP9N6E5mdzGVkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🤯
🤯
افسانه تاریخ فوتبال دنیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95287" target="_blank">📅 22:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95286">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NwbZnzehiVBc9kOepjM7WdNJYIFT7U33T7ZxafBta5ljnY2AU7WRKBm_we99gENdmLdPido8a5EPIoWdF_j-4Fp6JFNSze6d3gH21xCKgTnf4fLJ1DQ9sgEudi-Hqp5BqeQINEyrUcWyW048tiYJFxXu6tMCWBigSAXRZBB0rRUqvFPgdfiTLN9TVLgnwDJbZZU666TtbbJuzlBfm_3FWj7FKjsJqr4YlRZbCwXOEGIMGT8gJt4rZ-T67YHMHwpdTlziyl7tlybqau7gMzw0AP5UlBRc09N-pYDT3j2uotvE1a00KCY-nfisLjr3LrkcZBg5trPpPEc-5IfC7ny7MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو آمدی و توپ، زبانِ عشق شد
هر گام تو، آغازِ هزاران شگفت شد
از سبزه‌های زمین تا اوجِ آسمان،
نامت برای فوتبال، زیباترین نشان
با پای چپت نوشتی افسانه‌های ناب،
لبخند تو، پایانِ هر اندوه و هر عذاب
تو فقط یک بازیکنِ بزرگ نیستی،
رویای کودکیِ میلیون‌ها انسانی.
مسی؛
هر جا که توپ به پایت می‌رسد،
فوتبال، شعر می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95286" target="_blank">📅 22:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95285">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biGezRO_uN7gQ1koX9Rbsu-U82f5sE5o-2cQQEVtNV0_24MhsRKHErGUUuxITbPCNXuC1X4u_2urzbuSxZh8I1SbgyHrqlwjGduSLQqNiuC_kVC6E2O5UKGperRSe_WQI6TZgSGoWgbW0Z1_ZXQQwM4Kk0-0tXWSUp3gcS52A0w7A9838FijSPzpXUIngJJ2zBdVnmel7UT86dChLn6RLEkSdveLJ9c2OEsogMGJOh3U6apmbmbMpfr30ovvzWyR3USLNTrgDdrAXg_lVTnIKUHdyjJSiwfEgS1D_tIqyIaBghP29Geaq-bQ6ZN8PVMacjY6wx4IkRAQ3sRcL-damw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیمهای صعود کننده به دور حذفی جام‌جهانی آپدیت شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95285" target="_blank">📅 22:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95284">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5523d5321.mp4?token=gy2wyZUWFHJOmysY3il32LwE-qanlYYhrpm8CeDiXrOqjlgUeXG3IctTrxGR4u4DtwodF9EfE3WlFYSbgFvOZnJdJJ2gALgg3CUn8lb_f-YpE84Hb2t5S3LyTTCKcJ5_KVb-eLmWQ5KDR2L-w_eQbYt-6agILpRBG4YqDjmv7e45hN8MtsdMlxamYgd5Dk2XAIyShGtbdCGJvbRTs-Sgil8rKdj00WK2MU4IZflyjCE9vgckVnUhSDnNa02b7Afwk3dXO6NF-j4hlM42CTDGylhbuVzQ1rGDd9ePtASIjY8BaVcHf7AyafXdNd-XDySf58YAFeIfbtCkoYSl82pdVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5523d5321.mp4?token=gy2wyZUWFHJOmysY3il32LwE-qanlYYhrpm8CeDiXrOqjlgUeXG3IctTrxGR4u4DtwodF9EfE3WlFYSbgFvOZnJdJJ2gALgg3CUn8lb_f-YpE84Hb2t5S3LyTTCKcJ5_KVb-eLmWQ5KDR2L-w_eQbYt-6agILpRBG4YqDjmv7e45hN8MtsdMlxamYgd5Dk2XAIyShGtbdCGJvbRTs-Sgil8rKdj00WK2MU4IZflyjCE9vgckVnUhSDnNa02b7Afwk3dXO6NF-j4hlM42CTDGylhbuVzQ1rGDd9ePtASIjY8BaVcHf7AyafXdNd-XDySf58YAFeIfbtCkoYSl82pdVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید وقتی کیررررر میشه عالیه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95284" target="_blank">📅 22:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95283">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🏆
پایان‌بازی| دو گل از یک افسانه؛ مسی آرژانتین را به برد رساند.
🇦🇷
آرژانتین
😀
-
😏
اتریش
🇦🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95283" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
