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
<img src="https://cdn4.telesco.pe/file/kBp2hlhP7nNusbHDRj09YtrK1v52AwtOaWJ2sh5w6V9w_OTxWRgFE-yI4f_zrqqY43ZoEsnTEoPReXrJhlPPOdZk7VDmflUtzfCsLPrmyNHDqpfPYag2qapdajrZN5lbMnE99lPN5Vw9DcOQEQg0CyGyIHBZ8pK4-heW7qB0u6v6xXB6TynoDnDgODIeMxmAVCX3Prb-vHmAsIjXJyiUi9Y96Qo7i2TJXYcBgGxZN5VXLrDio9m8-sSbC5ADmtR-sDUOpxrAsTBxA6ytXlyKTTg6qQgtFnY4N8o0uGT9UO1dYX8xRFZ8W6LV0T3bgOwA369cFzpESx8KjGpd7lFtVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 170K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo92tKMpWXV4pcVrW8kYGrVBjsE53jcqfa_cnluVUGrF1VY8Aat-fJg2VmKHGtnHk2lsZY5sq5IpxxLBcX3Fmy2aSMQOCoxpttEztLBKiLuERV1k6LIowdr1KGq3Tm5cURiihrSGauEsnJDZZtqc7ZWWE0XT9YAGL8ivRLh1OCPqL3S23WuzBRcl45HlHSGYMw51A_hms6poPf1KI4nkxkU46L00BrIdmSjrJRMfCSpcYukvGSjToFGlFiM97V8wqzWX54f9gSWyM4iIyho4Qo-nyR8FM5h9SXFs1dDlO5FCg0tcFlSpFzkaowvyb34swFs59wgx9LAT_z5L8ZZyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت اوردم براتون که توش میتونید خودتونو درحالت امضای توافق با آمریکا قرار بدید
پرامپتش:
A tight close-up mirror selfie, black and white, grainy backstage aesthetic.
Subject 1 (Foreground): A young man with messy, sweaty wavy hair. He is wearing a tight superhero suit with a web texture. His face has realistic battle-damage makeup (cuts, dirt, bruises) and he looks exhausted but calm.
Subject 2 (Right): A girl leaning her chin heavily on the man's shoulder, snuggling in very close. She is holding a small retro silver camera directly to her eye, covering half her face, smiling.
The lighting is harsh and direct (flash photography style), creating strong shadows. The background is cluttered with a hanging white t-shirt and messy towels. High noise, raw, candid snapshot.
‌
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/funhiphop/78189" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78186">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/78186" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78185">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/funhiphop/78185" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78184">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRrrLIu_t9V0ipYxgZWzOgYKqknhNdBrFBDC3cXiprx7L8iVpS8uoXCPHS9IXAEy2_8ZFrqJKmjvWItdcq2NaMEMyDZ9oF0HIBuCZEmFIaxkARx8u4T-r23BmhqT8vH7u8XJ90W0znaKRFljYqi3vSfFslNuy-uaCtpkme_--IhOjubyYPc-Al6L074xVYrtj1hkbQVKMI2WvwNfxhr2ZwjO6e_p4zsHsH7PN7xqoBRx6s83C5n3VIjDtflh5vePvDyfl7edKgfPiILon0iz1dSOlIk6KxjHBNw6YbDlegujJwdxYNMMC5QKjVpJuxcTcM1C7k-DLUztMoNqUKpHQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/78184" target="_blank">📅 13:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خب دیگه توافق هم امضا شد و مانعی برای سخنرانی مقام معظم رهبری در ملا عام وجود ندارد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/funhiphop/78182" target="_blank">📅 13:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/funhiphop/78181" target="_blank">📅 12:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTP-r8sCFQOWFLlrvGy987yHhuIO4Yty8gMIlLQJLQ8JLAJl9sZSrIntvH1fSJUm8O4PXjcV2p_u19r9FoQIvscrpTd2MK1nt6orlv9Lm2aCWgOOVOzeXMKik7m5tkquN-mdpM3bPFYQxYSgYgg7OOwmppwYkAdUmIQ_OGLTrrcnQ5uhJ5RDrMSQA-SGt7JLITOKl6zVfFbSnm6n65BvQ8AGmtfMwars_R5FocTL08sjmotWCUUfrG9H-YCTpeM4pfN7wTqKTPY4CoPVo_88yEPyveONIk8-Y1CiVacycvFwjH4Z1zj52Ohvhi3OHTSD0xOd1P8lduDtZzyASoC_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/78180" target="_blank">📅 12:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عرفان چطوری میتونی انقد کصشر باشی داداش</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/funhiphop/78179" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آرتا:‌ کصه بشینه نمیره عین جمهوری اسلامی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/funhiphop/78178" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78177">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/funhiphop/78177" target="_blank">📅 12:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/78176" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1Zn4L-ynMzwYeXNF906DNMPNOQCDe3i1n-vIOB0c_KTUQFQ9dnu-og1kA8gIghCenW4TEws9n7pUc1izypt-izxYIl82KhqAxZv0ePqvtao1MlJZ8PnXPgRccNq030D8QsuIPQQ8eBJK9SCtNf5G5e-r0iMVd_IWdy6F-AFEVLpjo7BOQSvGjrremhtqfxpJqX4-8UNude0uRwL5RocedAtjv193MCauP-6SwxApqR8EQWhfzr9gyzCyP289OZ7qMQqZsg8NRjW4_dgGB02gW3kPl00RWZKAVyN48RBLV5z_c6spG6pKq8rENEqcB1Qo5r8DX1-0xGk2FY-Yoxf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.
Download
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/funhiphop/78174" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آرتا، ویناک، عرفان پایدار، کوروش و کچی فیت دادن</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/funhiphop/78173" target="_blank">📅 12:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78172">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgjX8gG6KJSkH5A1Xsb0CAbiH6eqpIRgp2maxUyHKs23u03HB39W32GeCuRpNKGZUtg3vU8oVu2QxpGHsduKwbd_JaCQir7wVRfJ3b-S1OK-c55B4nW8_-LrK56WVCWzqSLhcVUvSYm99yo3Pon93ImWMGAX3MNfLEms74e3h24L3slGmom7ywpA72lxdPvLnayzlWxRRfG5mvIcCT_hILuB-YcDQq0uKZmiMji299Spopbl8Aj13FMSaYaNfdlFGTmtlBerNmWcfIYPGG8I0o5B-ua_ld9Ikd539yOEg8GiMY9AK10Z9RX4UayYgW2uDclDP9l24AD8_spOYHPl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی بدون خایه نمیمونه، بالاخره یه جفت خایه پیدا میکنه برا مالیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/78172" target="_blank">📅 12:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آیت الله سید دونالد الدین ترامپ(دالگخیز): عادلانه نیست تمام کشورها موشک داشته باشند اما ایران نداشته باشد
آنها باید بتوانند دفاع کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/funhiphop/78171" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/78170" target="_blank">📅 11:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78169">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/funhiphop/78169" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شاهین نجفی نوستراداموس   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/78168" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=J3Ok-aQjFhZskhZVOu2YPG_mWz_VZDJC-dmwttczp6PusVurUCXO52WFZgqRUrlAm_C47j2FXu-40m9jVHOGO-rgRvv-wFtqfvYnDq22j1kpyqk1BMArOtaLuXp9fcB_4Z-xbJCT2j6-DUVDBCjPJqDkpuDFEEJbp1KMA8sDn9pCDzm_6DaWh9-478xVqZKk_d4kBLBb8S-d5R_WmrmoRuGqgan9i3GZ9hkF1MaQMp00nRNuasVkSOTGux48VA3iP5xWkyUvsKzFiBKOuru5pQAe6DSK45y6qnNY9o1Gp8OjKZ6F5I328km62Z9guqfAOYqpaD2cxK2P3KdgpSY1Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=J3Ok-aQjFhZskhZVOu2YPG_mWz_VZDJC-dmwttczp6PusVurUCXO52WFZgqRUrlAm_C47j2FXu-40m9jVHOGO-rgRvv-wFtqfvYnDq22j1kpyqk1BMArOtaLuXp9fcB_4Z-xbJCT2j6-DUVDBCjPJqDkpuDFEEJbp1KMA8sDn9pCDzm_6DaWh9-478xVqZKk_d4kBLBb8S-d5R_WmrmoRuGqgan9i3GZ9hkF1MaQMp00nRNuasVkSOTGux48VA3iP5xWkyUvsKzFiBKOuru5pQAe6DSK45y6qnNY9o1Gp8OjKZ6F5I328km62Z9guqfAOYqpaD2cxK2P3KdgpSY1Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهین نجفی نوستراداموس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/78167" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msEarlcuNZhuATzM_gjwHWHVX7FFAq_47oM-qhboXHL_4pG7dt52Q-_HkTGxlaIdYWf9L3Reso8qYaKJyLzN7oPcbEG7m6-rIbF9EdiWdHFw3KVxe7p1GXFtTG0azxm4cXiztlIg5GnnKwYK_S3CfaliWjS7XBgsMNstWD5zsc_Lc34gnR1kTQqAxk96Zojeopu0cJC2NW8C2ZMyST5lJjA1B4mqHEg8YnXNt7GHmtg6ROxQNhIuWX7-RES8xyQOTPq8syNlESx6Valr6PdsXCiTaKpAY8eP93wF1k2_TAlTagqlIZ-kIlWq9HgicfwmeVCRy_qTcCKQK4JEEszLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ها درحال درخشیدن....
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/funhiphop/78166" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/funhiphop/78165" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoBQWkp53Ju2NMRgi4lcHmFm72aVsfVPrbN_rtqgCcUhUDzv8KwgddlSUbgzLa_oOI1yOVWr-znGTZSIy3T6Ikf70qvXJfPnph6pGIe2A2-zbf1J6ZMKbmON2lvAuzFy25k8Dgl_JCBG7UxL6BCT6U9y4YILwe6Em7E3edfaauL5JyMgafVViNGjOv1toPodN9aAtncZZvtnMEfI-FvVE_CTq988do8z7y6UmZO-j8GWMI9jnSu8GWwdXPHuRVeIKX_iGZcRGCJ9L4Bh_YLo61iy7Aw7WSu_i4eGwytNq33ZXexgrhAOdEVP9Ts7Yl78mDQ4u8RrmOJk6pLdxOSMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r28
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/funhiphop/78164" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78163">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=ty-GjrLDUXNX9jSUf0CTSQeoKPi4Th0OK5QzmdkeBZp4zUQTFURnv9cIU-m570flFtjYLy8nKmAT29QF1qnjrNhvda3Z6AFBIdHG5Ll2LsfJIlQt7jZCzQQik2sS7YcqPvJhkt-NxZPAHEzauY-JMSLj44XphxB0fBz6mTOGXH7VcaXQfoThHTsgV41pQtJdDq1QZ8EOCJbaKAAHD81aBqLKmJA_8cnSllkf1BWU6qQyT7nClosbowLa3piqBQamBTBGdNwY7TCiHkTUaAGOHeEXbulBH3g2JlgdEZiKd1-eV7K-PPwP1IRSSAUvhFx1Sehd_7PYSWjp0jOQ8xLOaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=ty-GjrLDUXNX9jSUf0CTSQeoKPi4Th0OK5QzmdkeBZp4zUQTFURnv9cIU-m570flFtjYLy8nKmAT29QF1qnjrNhvda3Z6AFBIdHG5Ll2LsfJIlQt7jZCzQQik2sS7YcqPvJhkt-NxZPAHEzauY-JMSLj44XphxB0fBz6mTOGXH7VcaXQfoThHTsgV41pQtJdDq1QZ8EOCJbaKAAHD81aBqLKmJA_8cnSllkf1BWU6qQyT7nClosbowLa3piqBQamBTBGdNwY7TCiHkTUaAGOHeEXbulBH3g2JlgdEZiKd1-eV7K-PPwP1IRSSAUvhFx1Sehd_7PYSWjp0jOQ8xLOaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
یک انسان خردمند در ژانویه ۲۰۲۰ گفت: «ایران هرگز در هیچ جنگی پیروز نشده، اما هرگز در هیچ مذاکره‌ای هم شکست نخورده است».
ترامپ:
این را چه کسی گفته است؟
خبرنگار:
دونالد ترامپ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/78163" target="_blank">📅 08:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78162">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBHZTV5udG-3DUwf9dtQVAeM5kv1vH_O_qgN0RRpNaII_ngy_c6djist7GKwrF5GEPUld0Qfat1Uf4dDGDFtG1-D7srP69QNYk70Y9ZZhp6rC08XAucVBZICKAxCmulPveDEJMTv04Ma1rkHYcttZNB-_euhOAGpYaH48QYoLmzlI78NLT1kDgL7BZLfEDdbhDAZwBZvqO9SFityfPU06HvMgQ53pd9Y7fF-eS4R-HJTdT6_Oilu3xW3iYKppXXTbDf0ychs4_i_-VgdSy0h5boW_Vdv8EQO-1MtqNPxN7gHIzTD5uX29zM-Cs7bE7cPND6bW3CODtxTeZGuMAGN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78162" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asCWaoS9-zWSyh5jfCkzKgHkLeek0mCuKsshQsQhzdDeVa8H-C4kbvd59Rjuo9tmB217DYhzKCk9r_H8URl5gsZ52Tr05zRIGUmTLd4pYHsWgcvAron05USEZx0vLzW3fsL-8LHMHeVFYQe0XZtNOGHZhfnzSLWbahoPNX1-D9q7NVQlyRsQJ1wFin00NI5APpOiq1klks6C8WREraqjLjKzMzsQGXfO-pxeBrp3pD0rUJJ_i4WZ7V09qp3NUcJh75Puy7d6Q7-i8XA0BtbLCWdZ9sdyhZ60MVXzGpeYilRKFh7RleuO-HhFULW9Q-MEJx1rG2zO99TV7bkRNECwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFhErLMd9h3YXOdjyssmKXYb1GLqeDgeXbytuzJux5rZyYx5pfM2gax8NEyR8iWOgzT3ErMGIYlKlELAX54e5xaKmngUdTBu8_dYaJqXW6WLXsusAD-dQjn47Ej_Cx2Vwz1Grm6qC_qXCGbcMrQCFu1wmzhZajLED2Ohfn12KrziDkNGTtDQoG560_2VzZvpEmzi8h3mmcKh1ag3MNZv2LVJqDx3Kz7I5f3bWO4-3ASRUQRyWvmLF11xLFyNcXEyPQzgxGb_G_yM1MSmlnZiDmFWYMRqUmyARo9A460lHxuuDTqC9i0cie3icXCCCVjglPHPN6aPH1Hp1W1IyVUl3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78160" target="_blank">📅 06:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جی‌دی ونس دو سه روز پیش اومد گفت تمام بندهایی که از توافق تو رسانه‌های مختلف پخش میشه پروپاگاندای سپاه پاسدارانه.
امشب خودش از رو تک تک همون بندها خوند و تاییدشون کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78159" target="_blank">📅 02:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ایران دو قدرت هسته‌ای را که توسط برخی کشورهای دیگر نیز حمایت می‌شدند را شکست داد.
ما شعار نمی‌دهیم؛ ما واقعاً یک ابرقدرت هستیم.
روند تعلیق تحریم‌های نفتی از امشب آغاز می‌شود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78158" target="_blank">📅 02:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاخ سفید جدی جدی حسینیه شد؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78156" target="_blank">📅 01:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رشفورد چهارمی رو زد و تمام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78154" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خب طبق بررسی های میدانی و حضوری تیم من در ژنو، تفاهم نامه به صورت دیجیتالی توسط پزشکیان و ترامپ امضا شده؛ ارزش قرارداد سیصد میلیارد دلار با بند فسخی که بعد شصت روز فعال میشه.
Here We Go.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78153" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">میگن که تفاهم نامه رو امضا کردن ولی فعلا بچسبید به بازی انگلیس کرواسی این مهم تره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78152" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عجب سیو پشم ریزونی کرد گلر کرواسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78150" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بلینگهام گل سوم رو زد برای انگلیس
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78149" target="_blank">📅 00:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc2oQDv6Hmhc05dC0W1DgUYFIYqaSD6umYcY5V9ivGDJoVeDtizXmrNIqURyDBKVPYgsIpKqQ1UXcDkQ3v4gCCTTl2vdujOYq0j8gSwMH7rAZqZbeJnRoRs0wRE4spZGjsPeCVVwmj5vmlPpNPoC4_fSCwE-j_gYx6rjNI5KAIABLFLNSSCrTwSLzrvNy8GBw6BiJ0gFfb6xtn7uLJCUCzQM8eT41BGIeKSdzUxOwWKTKk5KwGxbu0XYUSuAUIwUeL_1CdylSYH-w_j-Eo9tDPf68JcURtYPYCPYhxAa0hOrxRvadIhQOoqB_w15mGe3yQ4Y5h4s7ULLPKR9OMdgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر از یک هفته تا منتشر شدن فصل سوم سریال خاندان اژدها مونده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78148" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAxGyPkAkw4sP2RadGzBHQyq_4j8fdzqNFPKCwtmUbSh_OxEDcSb7wWi63vI5PEhPvCz1e3RO_c4kzVrae7kaot4CjYVP15EKyOWb9wWxewnVZ79Zl3zoIAbSo8wOI7srwk-SSG1Mgafs9G2R1Plr0oyBToXkPhCKg125GTGTuvy_m8cTExo3oIjxcatLuSpcrZlNfVg16WipFSib2LCQZmFVeVN1nQnkdHaaO9TXL1EPsQ3E5UQ-p5TPbUtPtnoCo-9Jcub7fJt9DPZjzgtGwiQxabQcPlcVvyxhotXDP8i6bKzPXurGHA_Kq4-1twEzZmONs_sLICocvnpweLlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری مامان پوری از مهدی طارمی.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78146" target="_blank">📅 00:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کرواسی زد
۲ ۲ شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78145" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مثکه متن تفاهم نامه منتشر شده ترامپ قمبل سیاسی کرده برا جمهوری اسلامی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78144" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این بازی داره قشنگ افتضاح بازی قبل رو میشوره میبره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78142" target="_blank">📅 00:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=cHAHqsTbg-YnpUjF60UTXDyD4mmFmPMmVy4-D02YtcHOkIo17Jix1O9kMkaUaUN5U-M2kFgba8BmN5zJK-VhO9t--YG35TCDL455H6XwTd1JBOlEnuUoLDiAvvqyiqOcByzIfpAmenPtftSfRUV7GAFVk1BUPeNBb5O97pi6T7KZ88x3hedQEz18r7vCyljhXmzQzjlVuTVHNGZ6047E81BzmBX31nnd4ioVeBC1Ik_QhFpcw9zmQR2IHST56h3LZ2TEhA9MJ7ERThuWdO-TdOn-Uk-R058tp6qYUR3QnxskE9fNZgTVifRcy3V74t6MlI31x-sU2khk0hG49EeFJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=cHAHqsTbg-YnpUjF60UTXDyD4mmFmPMmVy4-D02YtcHOkIo17Jix1O9kMkaUaUN5U-M2kFgba8BmN5zJK-VhO9t--YG35TCDL455H6XwTd1JBOlEnuUoLDiAvvqyiqOcByzIfpAmenPtftSfRUV7GAFVk1BUPeNBb5O97pi6T7KZ88x3hedQEz18r7vCyljhXmzQzjlVuTVHNGZ6047E81BzmBX31nnd4ioVeBC1Ik_QhFpcw9zmQR2IHST56h3LZ2TEhA9MJ7ERThuWdO-TdOn-Uk-R058tp6qYUR3QnxskE9fNZgTVifRcy3V74t6MlI31x-sU2khk0hG49EeFJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خخخ:
وقتی همه‌ی کشورهای همسایه ایران غنی‌سازی دارند، منطقی نیست که به ایران بگوییم به طور کامل غنی‌سازی خود را برچیند به گونه‌ای که برای تولید برق اتمی هم غنی سازی نداشته باشد؛
درمورد موشک‌ها هم همین است، وقتی همه‌ی کشورهای خاورمیانه موشک دارند، خب عقلانی نیست فقط به سپاه پاسداران بگوییم موشک نداشته باشد.
بیایید کمی عاقلانه‌تر با آتها مذاکره کنیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78141" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شما یادتون نیست ولی دالیچ یزمان کنار شفر گزینه سرمربی استقلال بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78140" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کرواسی لاشی همیشه جام جهانی غول میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78139" target="_blank">📅 00:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انگلیس چه خوشگل بازی میکنه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78137" target="_blank">📅 23:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ: ما حتی ۱۰ سنت هم در ایران سرمایه‌گذاری نمی‌کنیم /از یادداشت تفاهم، بد برداشت شده است
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78135" target="_blank">📅 23:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7FBa0YiomJYnVZyTEKYhIZ2JCcW0OcuDi3RULWy74fKu3TJPq0CoFnTQNtNmH6xSElxqUXgYUn_yxovGVxoXcKUG38N-j-i41p1J0KeCYVyu6vo7cKNSCFvGOfY9B87ttEBB42YFldBEoImgsHpMKLxD6THbT7pBLP94dik8RFmKTKYyHB6JyplsiMSR6sHWcjqkHxUBKlHI7dm1_Nh2Sm7YUwCpZiFexCk7XuaX2DNv5q0Jc-4wIBh35Q5uqu2wwe8LpJ63ONDq_r71A8cD5_tm6kWbcF-4t4uISz2LD20niz0GKCqYX98hb9-ZykBFGwIdMTxEAGvBXIMcdbBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوادو
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78134" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار  +
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا  +
🛜
تمامی سرویس‌ها آیپی ثابت هستند.  +
🎛️
پنل کاربری اختصاصی و حرفه‌ای…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78133" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
📦
20 گیگ --->
❗
فقط ۴۹ تومن
📦
30 گیگ --->
❗
فقط ۷۲ تومن
📦
50 گیگ --->
❗
فقط ۹۹ تومن
💎
100 گیگ --->
❗
فقط ۱۶۹ تومن
💎
150 گیگ --->
❗
فقط ۲۳۹ تومن
💎
200 گیگ  --->
❗
فقط ۲۹۹ تومن
💢
تمامی سرویس ها
۳۰ روزه
و
بدون محدودیت کاربر
هستند.
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78132" target="_blank">📅 22:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78131">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه صحنه گلر پرتغال هم اومد پاس به عقب بده به خودش اومد دید خودش آخرین نفره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78131" target="_blank">📅 22:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تخمی ترین بازی جام با اختلاف
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78130" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78129">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">همون بهتر ک توپ نرسه به رونالدو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78129" target="_blank">📅 22:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78128">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فقط یه رونالدو فن میتونه بگه ترکیب منتخب بهترین هافبکای جهان نمیتونن تغذیه اش کنن</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78128" target="_blank">📅 22:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78124">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بعد دیشب گفتم شانس ایتالیا از پرتغال بیشتره یسریا به کونشون برخورده بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78124" target="_blank">📅 21:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78123">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تقصیر رونالدو نیست
گذاشتنش نوک بعد یه پاس نمیتونن بهش بدن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78123" target="_blank">📅 21:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78122">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رونالدو مادرتو گاییدم پول منو کی میده</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78122" target="_blank">📅 21:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نوس با قد اندازه کاگان چطوری با سر گل میزنه هی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78118" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dInDBnIbQTekcZ3vNpUf9CayExZfzScTJuctHQEbV_lrmv20Q93jFZsgqznRuIU-tCKxmPbwgtW0rd2ehVWGYFLoTq-9zk-ADaLaszovpzDcL5D-kyBS-cilkbMmWkhANA-Dl_8HIJjdNf_J77eF4L0KaKnh8DRVdB_BAiqjMdfNZHblzAasKkNnfcUzQPu_PggfUtDejWf_GjYC2E4d7qQhFOWYN-S0kyWcCBakEeYlfU8GfqNO35utbNoFUzCTolUL6SMe2BKsGVRmZNfI0t1qVSFpSAdskHPl4T5gz20-ImvMdy6GyZ05ntEDG7KvEumlMK9B5XmmpIlpbSUTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا عارف
تولدت مبارک مرد بزرگ
❤️
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78117" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایت الله جی دی ونس میگه چهارشنبه متن تفاهم نامه منتشر میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78116" target="_blank">📅 19:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78115">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نه داداش پوری خایمال نیست اینطوری میکنه فدایی باهاش بیف کنه و کیرخر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78115" target="_blank">📅 19:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مسئولین جمهوری اسلامی حاضرن هر کاری بکنن ولی نرن حضوری قرارداد رو امضا کنن چون اینطوری مجبور میشن با قاتلین آقاشون دست بدن و روبوسی کنن
فک کنید همچین عکسی پخش شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78114" target="_blank">📅 19:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78113">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=sbx2pLvy9xifLWNBE3xrohsvub7S3uQ9xRqXEfTHHv-bTqtm9CQdOpsgbGIBa-H0HPSGuyMauutcXgSR7PtQhmo_X_RDWqXFtOeNLwHuoMrRHAM6Em1RZKOJ-w7CezJ8xALEYk66I8B1bETCgxrJ_HA_cWf58RMCF7LXat00sCk1HNKXWFD20Yss4DZKa0m6851n4WDG5REV7XQOnYKTu6Vagdv2d_p1gcs6uWWAcUfSokAdaRY4X1lalJLvQB9-bvXYX3f1j1sGouW3X6E0WJ2RPyDB37qHqEt1P1EdVZx0tyMPzUvrUxiI9vWj0ktgTiFXzBZ_wCP7DcJgWBwoVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=sbx2pLvy9xifLWNBE3xrohsvub7S3uQ9xRqXEfTHHv-bTqtm9CQdOpsgbGIBa-H0HPSGuyMauutcXgSR7PtQhmo_X_RDWqXFtOeNLwHuoMrRHAM6Em1RZKOJ-w7CezJ8xALEYk66I8B1bETCgxrJ_HA_cWf58RMCF7LXat00sCk1HNKXWFD20Yss4DZKa0m6851n4WDG5REV7XQOnYKTu6Vagdv2d_p1gcs6uWWAcUfSokAdaRY4X1lalJLvQB9-bvXYX3f1j1sGouW3X6E0WJ2RPyDB37qHqEt1P1EdVZx0tyMPzUvrUxiI9vWj0ktgTiFXzBZ_wCP7DcJgWBwoVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78113" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78112" target="_blank">📅 18:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcnjEC9HV5Yc2wLWm77G0Uj2MUuKZ5m5ZQSsZbKwNcxBhOYntz18Hx-xLv5lMoWghtukInBgnXSjY6AgTvStomVNNZf4iNCqR93TwZS45_FU5w3Y-NELneKjI3kHzjmFqGh9sz25zKA67VmtmaJFQwCIZLnioa_we-zHHRfZVlvfSK5k1W52NMT9ykc6pIhlAwD4-gFt_oVwN_G8TUxNbcxEMN7-oQ1MWpnQ2BaeeF8gKKnd-rgVewBvWQe3YfH-DhsTTkIjr_BOp6E69f8hfmq0-D0njJ6n5WEd5-CyOwcQ0l0zYQTElMv9qrxkMmvKKxJwp-hxhH0IfgJxc0oG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-fQPR1JNZuZ-tfR4xX1tBsREuexsx5CxNuA9QRqL0NNxQDNIFJ6EiKa1t70dJcHaTnSxx9z0yUoYhAt0T2bwbOSaEfqPa9HoJrGqkkafAw46cOZF23UZXEFTqw8JzTuFmDdvulwAwZuBgv5ZrLfYiamMD9S32BttTxCeVtxqRYaIn91LxpKNBvQJAaJ3uSjUH_7eUsGY3Fgr2lQB_zxhW1wYgtUtvHBS3l7HZWKdKtfHLJmsu5ApU5BV9seFeEGDyq16TFPQ2Yw0N_S84f4kmpf13t_K8NOw9ZkVQu3tsl-hYLgcUN-4MDMbGI_B_ycm8sp2g-m0j8ACOdLCrkpmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78110" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/funhiphop/78109" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwocjAMHt5d7N11vHXcqI3DYXQ72qElLAWf72Ipp9tYq5LKPSJRDmJZSTkWLTsRBotShNTmL3Avx6f99Jk412ry5XrNe_qDi5ghSI6t5znETZ-rcVEpGw4TC2vXlkbt4too4hQZWWXUIyVrRtwfjHReNek4Oh2ItEFxs9sNGGPIiGpj_y878PnOVtw0cDXuHPlwC6rp1PcbOwZyKeXm2E3AzKQDdkaoHj3yfkzq3X5O-tptVtuuNnIlLKm1yq8vsAyeC2IaV1yv42WzfnR8Qddni63FwOw6Y6WPe19xQlDPEGqo7zNqbmRUhSguS9zwnCHtRjDSf1YxRqKDBi-Ygkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g27
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78108" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78105">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78105" target="_blank">📅 18:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78104">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLYHjkYteVZgDLOaY8r4z1ZIS000X5ALuXnQztHrNh0mqn5kN-FdR9LXBUj6XlrkKtlMnS2waGgL_FdyZ83ZDVfhkzokJL-ULQTkswWTEw9l_0uNFm5PNWBd6iTImhGXMfXdn-3cBHhODY9eFWCQTLaxFxXFoHUNt1MHjg6ILQILif_naUdi-4GVAMRH5ThEfAxSeDawr3Zg06MdG8I_CbsJmy3VKm5Z1mPSAMEX_ar4WMF017miAEhjqcAD-2bVZrAa9CAs0jMviLKYO-5_Advi27Op6z2n4zArFFg8gU_mjjMvSxGzlxXyxgcm0Oith8KHZdoLXnogmPhqwbHZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78104" target="_blank">📅 18:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78103">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=N0Hnz-3pX_RzvCmGHeRjTU-xqyglcvE2yIIlfuTzIrkcGw8r7fblW937J53MEmbxr9QZ0AUt3llGNkuXbbbPdpfUpwol1SJ_oA3gmcDVRLzEl1-zdcBtw1sLJg-wV-cV646ZOf_sf3Jc6sXAIkwtJCqwCmuxRwo8KC-DPOITRhd49hDB77qXXZTABuBBA2xsFl_zsLkjpOVeS_R6K4VpF-zz4EVs8AXhmr_A2h3S-kwOi7cNw1eKOUneLekHYx15QI35abTzBXsKByFMf1DTpPo8s3CrYaSxt8d4AkOZkzTDYKT1ntYbD2dO4oPuu2_r8yBpXSD34wUbp_sX7y_COjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=N0Hnz-3pX_RzvCmGHeRjTU-xqyglcvE2yIIlfuTzIrkcGw8r7fblW937J53MEmbxr9QZ0AUt3llGNkuXbbbPdpfUpwol1SJ_oA3gmcDVRLzEl1-zdcBtw1sLJg-wV-cV646ZOf_sf3Jc6sXAIkwtJCqwCmuxRwo8KC-DPOITRhd49hDB77qXXZTABuBBA2xsFl_zsLkjpOVeS_R6K4VpF-zz4EVs8AXhmr_A2h3S-kwOi7cNw1eKOUneLekHYx15QI35abTzBXsKByFMf1DTpPo8s3CrYaSxt8d4AkOZkzTDYKT1ntYbD2dO4oPuu2_r8yBpXSD34wUbp_sX7y_COjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسخوش
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78103" target="_blank">📅 16:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78102">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مثل برج میلاد بعد ترور سران نظام هنوز سرپام
😂</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78102" target="_blank">📅 16:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78101">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ابوطالبو بخاطر این که گفته بود تیم ملیو دوس نداره چوب تو آستینش کردن و مجبور شد بیاد معذرت خواهی بکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78101" target="_blank">📅 15:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78100">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترام: توافق قطعی نشده اگه هم قطعی نشه دوباره بمباران میکنیم ایرانو
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78100" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78099">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ: بخشی از تنگه هرمز باز شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78099" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78098">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: گزارش صندوق سیصد میلیارد دلاری کذبه و آمریکا چنین کاری نمیکنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78098" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78097">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ: ایرانی ها به ریش اوباما خندیدن گفتن اون یه حرومزاده احمقه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78097" target="_blank">📅 14:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78096">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اندروتیت ۱۰۷ بار تو یه صرافی لیکویید شده.
الان دوباره رفته صرافی و شارژ کرده رو بیتکوین لانگ گرفته.
اگه لیکویید بشه و پول از دست بده، میشه ۱۰۸ امین باری که اثبات میکنه تریدر خوبیه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78096" target="_blank">📅 14:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78095">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/827713cec2.mp4?token=nzHkuHWamH6KH5FZju5GxuFAQuRHGJ3reWRU6CuacMyVZNYNFls9ujPCulV0k3X1R6F5lZr9XbwjENvzYtYzWCjUpqb7FZIi2w89ztdNCZdDyDk8Y3a2b9VzFpRUBskRggq8U6q89llF6MEbyxsUloMc8GbjdQC4_gZN1c1_cCjNxdvZYQbcgBfJbabgE0PIOKOKmxqYFqlJJX9JlvrWObzvGmnaVtbBzk1BHBH-GPvd2uFn6ipSJqckQeluwX1XS5aYujALcXCS9Hm_8pWWUCA2Yzbi9USZR0to7N9kjnjHk1yyl_XmSPwjX7zPjvqnPRr_sa0zWg-4hLY_9ynhfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/827713cec2.mp4?token=nzHkuHWamH6KH5FZju5GxuFAQuRHGJ3reWRU6CuacMyVZNYNFls9ujPCulV0k3X1R6F5lZr9XbwjENvzYtYzWCjUpqb7FZIi2w89ztdNCZdDyDk8Y3a2b9VzFpRUBskRggq8U6q89llF6MEbyxsUloMc8GbjdQC4_gZN1c1_cCjNxdvZYQbcgBfJbabgE0PIOKOKmxqYFqlJJX9JlvrWObzvGmnaVtbBzk1BHBH-GPvd2uFn6ipSJqckQeluwX1XS5aYujALcXCS9Hm_8pWWUCA2Yzbi9USZR0to7N9kjnjHk1yyl_XmSPwjX7zPjvqnPRr_sa0zWg-4hLY_9ynhfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاااارهههه تو موهات بلنده زیباس
کلی شیک و پیرییییی تو شب کلنگی نیم‌ساز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78095" target="_blank">📅 12:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78093">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOlTqmITiH7aj3KJZzSEk8DF14uB98kLxoTyRSLHLIadmbBI8rb9bfAU7QdpiRudAwPLOYchW4mC2atQz4W1CACJqAvVqF2Od3lVDBfcTNzwQoGSPjYaTsqKTj96hp2MmS9jqhnWP7Ees3M3ezHuddWHxTwx9c9SCJ5Myf4_otFSX_aATYszZ1zIC5P6MAParnZ1cSKDp4v5sOtJ4jl60OCiNyolNqfQX3Fm5jgmoOJUQ5Z-auv7TBd2GxYYX-Y_kZdIkZlGcLWLQ0Y4DkRGW-2QhXm0qXtuLR9LoWySoefDwi_HmD8_PznmIc9ZhjSFksMP-tdbgwZUWSM-L3aVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJLadbHtlR8Uk_dteHKDxTpCxe1Iqv_vMEtTURdA_lQ5_mivCsWV52rmh-XhZP1Od7k3zSeeruCCb1uEx5l98AF_qa2tHGeh-rjRdBvtPXx7kMOSm-9VsQ_TQHMq8laY4fRYUQ9IFuKDjPZtuDgyi_at6Rf-Dq3jFRRmL-OEfmiosPmXCBD2RUHjOZdW-VG7wmBh19zckyNXlqjEMI30n1LIk9qDbrLKG11-D0tNu-72ChQcVbdHJg3q5rJiENr_MZKE43KvnHt3U2xqoxVot98UCf6zmSvrvOqS2AXmlP7M56ELFD4mkLoc98uyYYu35BDPz7lAWZ8dl7F9bCHM1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این داداشمون هم به دخترایی که فالوش میکنن بک میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78093" target="_blank">📅 12:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78092">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-OtO8YhiChd70IDK_1zuVv1_aWmPU2KT_K_T0wK_ErryUVBaAxtTJIsKlLlPC6PsyVIGunG7657lIehwclZOHTHWyn_pPg_H8L7CheXv7m43A-1CH53fTmE4ksW0hASejZ0HIaeTlSIYt3aVLWdq7VwrN0FmKZfW3nlrZw0z2X94KR6xB4C6EveFT84F2nEWOrCTE72_Ioew_o-05qSrTpc6IPAxJyfNkZYUk-ga9QH6fY-M3Cxew7Y_A65VZYC1T4t6OMmno-lcm6U36QFhSc9cYKkIVcS9b4QbbGoSxmXLgm6Yzum1C4YJmKwUaFbt70noo_f3NK8oAsOhHutQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی چند روزه زنشو نکرده اعصابش تخمیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78092" target="_blank">📅 11:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78091">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0oZBIxcSYipkaOKCVBaJ0Khpy9OxXOsQJnSK9Ia8VUoCfq8P17aJq2BRRb2MjmhA5E4dY9JTrCACyoNS1xcwXJE4ZCHi6pCZxjko7qRE3CYztzpCqapfRquUq5pdO9XA-BIVNlZSCHXLKoYbD2jQQ9ZtR-Vir7nQaAh-BsCSnIIUmNMiZMZ8nTB0G-aQ_H3D-dBDQqYlE6mh-517uRrnvabwN_4ZhEt3GuU_LEXof3Msna1DoE6-BBn1wbU1rKR-aCx-Q2ihN7rTKPKnPiTuY8EBQv_8tHbAezdodlGX-wkwqiE1uWFdx6AKYuIzcyRic-711NZ_k206gs4gbkCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت نگران مصدومیت نیمارن
واکنش خود نیمار:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78091" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78090">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78090" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78089">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEplNdL-qojQzFIDNtGhU_lyd8XGJbDA0c9Gr9CiiSildXxUnKd4GQfANwPWia5lGzemqCslScWe4dIM-cpunh7zx-gLWN63tQ78pysc1cfULUhRnDqR80TonLcJcuiDbAcXFowehtj3h9bVlqtues5TK-PEZufWMxZH-0ELNA7XJOvfQeUakJFXhQLTJzC9iuEc155uI18X-RemZMnMaHWUYTluE9hClai0T4HDt6e6cOfdAYTTuckcExEbjvxFlhemVBxy1LYVP-mUcgbGws4OGcppdysUjX2yFMivHO8ratfMKr8d9qm7uDgVTaiYIZHw2X2xcIQD93RE0UTuLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r27
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78089" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78088">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olUjzq-wudK17NiGufRNAoHxQTnBQNG62dCAgx1N4M4_iiL6E2D-sffDZjhZX1Bz5Btt7MXo6K1bUMXcu_hPkQbEJ0fcqg6EjeceOXE4RZ1F6gLzQLfI3c_k78THMsX-Hs6iGHZZTihZ1_CcLQswFq078ODYFL0q67Gc64b59GWPpREShHym4GBB6kE-TnSgdwV4irV6codsWtz9UTU4rEgpeRDKWtM72vzrKMuooNIpHVIwMAI8I_hqX0VRWxy9KtqqUeTbdW_DJdNuI5_q2aNQAamkt13VMlP-vhiJ_XJPMeMnhn-qm83kd3qLm0vB1BPzCbM0o7TNN63fvK8bfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت پدر از پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78088" target="_blank">📅 10:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgrIOZYtPN8f9-pjjfVl9QdINGtC-PRJooW_LpUgbmKFFGbaB4X8tNEwvxx2GWb2blqvPBfIG2M9hvJvIN5PLKlmX9b3IvsmyUfOSrNGj7ipVtUMe3zpxueRNSoVlAJVaWcwNHWuJt-_9hgBoIh9Cgwrl2lxfMcvz0EWXnYdkbNhL30vWNWsmXEj34vXkfyMEI8CTLtHAxzzC3tKAzwBkCb9SwCU7wVRtjvZBEVM0_yiU2OAqtFE6DwGG0g3_lI7lbfHtanjdMoEwOyJh-nm6OlTFHybt3sXiqyOg7mz9X5yKxkla5cL1rdsUCAlkg-wMSGKPUIRlvjH_tq38ysjSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو دریاب پسر، یاخدا</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78087" target="_blank">📅 06:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حالا رونالدو مصاحبه میکنه میگه نه ببین گروه ما از آرژانتین سخت تره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78086" target="_blank">📅 06:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پادشاه فوتبال تعویض شد تا استراحت کنه و برای گاییدن بقیه تیم ها آماده شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78085" target="_blank">📅 06:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نویسنده کتاب فوتبال هتریک میکنه
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78084" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78083">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گللللل
لیونل مسی
کارگردان فوتبال جهاااان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78083" target="_blank">📅 05:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78082">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بهتره برم اول وضو بگیرم بعد در مورد خدا و اسطوره بی بدیل فوتبال حرف بزنم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78082" target="_blank">📅 05:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بهترین بازیکن تاریخ چییییی زد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78080" target="_blank">📅 04:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78079" target="_blank">📅 02:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خوار عراق رو من گاییدم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78078" target="_blank">📅 01:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هومان بدبخت یسال موزیک نداد مجوز بگیره، تهشم بهش مجوز ندادن دوباره شروع کرد به موزیک زیر زمینی دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78077" target="_blank">📅 01:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAstWAa1FQwbeKidMmCKMAa89sF9DFl0dksRXaQ7Raim9aQS0YrZ4S7KmFLTFoeNAdIR0xh_rUnTN_J1jxmQLkDuSKOWmIHnhrdyxc_wDoATwfBWvntkO-wSnqbwsFwsyGkpDiy49C6ow1Dhke50S5Scm1_peH15VC_kZ3aiS8ZbKX9oIrxk6_H5bxnEbxfSdnOOSRgmbca_oiFE-7zwBqG5WytVXFr9JwHgi21Lj_ahSEC5_PK4Y6XS4X1bhn_sejLE3pYzTUK8un4g3ULO3nCdD3eEKFcyqPqayUH7g-hbKDeJLdfDQkFOQdC69cWyq7zNcIfVdC1AVkrxy1Xiwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا از مزرعه‌ای که توش کار میکردین خجالت بکشید، یعنی چی صفر کارت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78074" target="_blank">📅 00:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78072">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قبول دارید کسایی که جلو اسمشون پرچم گذاشتن زوال عقل دارن؟</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78072" target="_blank">📅 00:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3PqVGjG71dtTIavqYvSQ4wjSozSqC82ms3Y5FfVjsJEduBRpTskIqGbDNrgx96MeQQuWLyL7kyhZXPaQ_sOq5tBy4IROME8PIU2IpEWWwfrw845WfcG1f0idv78o55BltYeoq9YDj7poGIrEpjqhHMGNc2ynY2vpZrGmjBO3Oq_Dg_wQWDn5_Cv-PtBnc3wxEzIB5zvUUq132puxORgLNHwwPTXw4hi7h8rLf6Rjj1lpRdRcPk586ZgMHtwNeADJv7sB5BGoyZFQqPo62ktulONxa5r5TwJ411qLsHEcLxHSNriStVAmNBUVbWphPheayv8tlqGHBY80SMikZgyuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78071" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78070">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78070" target="_blank">📅 00:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78069" target="_blank">📅 00:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78068" target="_blank">📅 00:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گل دوم هم زد فرانسه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78067" target="_blank">📅 00:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این جام جهانی احتمال زیاد امباپه رکورد کلوزه رو میزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78066" target="_blank">📅 00:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چه‌ گلی زد سنگال که رد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78065" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">امباپه زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78064" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
