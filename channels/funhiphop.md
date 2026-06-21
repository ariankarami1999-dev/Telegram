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
<img src="https://cdn4.telesco.pe/file/jThnqugnP8x18RGiS_zkUPZ-CIXnZyJ5E0U1Ttm48i-IQSMFu9UTNoprDPgFhFvFrJW2CuEQiun-GUIwGaGS38Bzi0MsWxFX8kPjukh8hYGWYkndBBDj261BmquOY7_OIpigXFxCDbMw1YbNlu-fGZN_yoy3Mf0zWgx-09ZTkKmRmhXVOeNPJ-CePag0DP-GSmC7E1PG5ifMJeQIbIpESvkN8wO7kS97XQ_tLiYewIJlRI6I06LbAfUendvENfNZDtpVHhnpHlW8L3m9o8mVjCX2rO8I8pCeKnn6rS8BFOu3lZaQz1AgDscaBFr1vNWncuXjpEhrbRv9H_HqGBbANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 21:50:26</div>
<hr>

<div class="tg-post" id="msg-78376">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رو برد مساوی ایران بزنید پولدار شید</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/funhiphop/78376" target="_blank">📅 21:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5sZ5Qn9wOzJA2flSvYZxFSC8qotPGo6BguL72_1n8eXwGbNoyBE6vAb_vki5WptDSQ6beSLScezkOnX-D9v26xN1CnHNrt8E_bCan3J2OPR_OulRWqLdIDjftZmyybRQBYNBYn2hWt2bVmeN_UOEzUMcjdshyP7qybpJ0v-t8Y3rgNklXBRh9I_7znM85v7fD3EZ_jOzLAgdM4snkeIomRQseN1fjW6AoMy-znw6kicAv4dCkNmDYVkf0G2UAaVOwKIh-SGsHETGbn_Dy3Mm9r8Alc5oHyCjg2DSZbpFvyDmo6uRHPyd16GuJxwYH00XU9Zt4vEaYAh9RuYPyJzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال کاملا حجومی چیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/funhiphop/78375" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78373">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امضا میکنم که نعمتی امشب بهترین بازیکن از نظر ما میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/funhiphop/78373" target="_blank">📅 21:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZLwOCQ5ch74dtv5uPyeEvaE_pzwI20wY8Sjn3DbHW0U0ASxY8ZY4hsVHcygm-PdRcaN3a2o7NSReBXK9Bw0mQ17xR6IdnBOC9C4R1fDDgfVNqkB2NkCDORrTQDGsn_Rh8fpq0niz1CQ8F5bB0Y8m00wLLW9k_fSVVbBtK9xEAz6XyE_PfsEBJzH496cFY3GPrlVogEg0W8eVopsPNg0-qhlQJ2n3H5ElodTpGEfz-zh6-1olikmnK0d5taT-imgXD6CeG1KwGaoTK49MUuQ1GN1nNynPkod1bZTRikfWQWbWlMnJzxnT8tUPksUdFuFW5Wwvylwq7w-eSxtySvI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب مادرجنده ها اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/funhiphop/78372" target="_blank">📅 21:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW6MtQ3YSJXBaS0yZT1r18BFys9q1XXc30Z9ADq29z_NGb_Dx7uYJ4bK2CA0vqwSyuyy1G9cSj-3lCHx5k-mCiDVJS8khaMb9oaJyL-PHdykzDy4FmwPWEHExhFxpjir4hlX5DgR1aSIoqFWh10wW2cS2ZUbSkjml-lFPwipq928dwyTkrxRUDoEqYu0Wxx_CFXifujXuFCtXqcb2tkseMCI-CzJRJbsgGvY0cYdytesVukMzQNJmtVpu0sSc7Nf3tTybOuvXPA2JbTXU0r0T9Xf9LuLtcaiwlD7SCKK6goxZm0UzH5y0QaOlcw3kV3Ycjcyi7V0wJD-z1gv60Thbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم ۴۰۵
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/78371" target="_blank">📅 20:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8a4c0df7.mp4?token=gl3QhxYJlK-faJbT19ncUjOd9uN55zMRjjjiGEbjBobEex0n1VjtkSvLx07UTRgU-hKQ7PKLRn7v179ilLJtBuKf3n9jVhNZoEl1sPPI1JPRCcL_nmenqLvSzESpALjTfzHHnR8Kijq6R1je2Kh1mthd7XdXAEFI5--s2PaHvPmagS-_KFuPqcOxdJHwFAOOJCS3cVFQ35fsoHFVPRv3xc6PV75PEaHC7L1KybvXmPZ8PNwgktsvJrnXvzbgoM5UcC6MLLmm_1JfzY7d9QxDD_JBarVSr3-j-4Q2BWytWUdMXRwMO2uztbTMOTLeju3c_lwtiEjGKZBTmon19krJGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8a4c0df7.mp4?token=gl3QhxYJlK-faJbT19ncUjOd9uN55zMRjjjiGEbjBobEex0n1VjtkSvLx07UTRgU-hKQ7PKLRn7v179ilLJtBuKf3n9jVhNZoEl1sPPI1JPRCcL_nmenqLvSzESpALjTfzHHnR8Kijq6R1je2Kh1mthd7XdXAEFI5--s2PaHvPmagS-_KFuPqcOxdJHwFAOOJCS3cVFQ35fsoHFVPRv3xc6PV75PEaHC7L1KybvXmPZ8PNwgktsvJrnXvzbgoM5UcC6MLLmm_1JfzY7d9QxDD_JBarVSr3-j-4Q2BWytWUdMXRwMO2uztbTMOTLeju3c_lwtiEjGKZBTmon19krJGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی رو برد یه تیم میبنده
بازیکنای تیم مقابل روز مسابقه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/78370" target="_blank">📅 20:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ریدم قالیباف: تهدید های ترامپ بکیرمونم نیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/funhiphop/78368" target="_blank">📅 20:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اویارزابال هم که به یامال  ایرانی پاس گل داد اصالتا اهل هراته و ریشه ی ایران باستان داره
هرات استان خونی خاکی ماست و به زودی به خاک مقدس ایران برمیگرده مثل اربیل و سلیمانیه و …
دو ایرانی اصیل کارو برای اسپانیایی های آریایی درآوردن
برادر برای برادر
❤️</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/funhiphop/78367" target="_blank">📅 20:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آرژانتین به عربستان باخت و قهرمان شد
ولی اسپانیا داره به عربستان تجاوز میکنه
ینی قهرمانی اسپانیا منتفی شد ؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/funhiphop/78365" target="_blank">📅 20:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78363">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مهد اسلام داره فرو میپاشه</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/78363" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMqSQE8jleRK93j0U4lU8uvn_jz-_dj32tkfTcKsdKA9ElLKZh3-r2m0Fa-6L3KUwaY-pzdkQyYVDNoEEGvPTRi1jhQfctasv1jlA7oMzQyJhQkWTHib7AKsL25v7_UF790UNijV4Zqid_abddEkKZSb90Y2IyTCuv6whgX3iquOeaaEwFDYSj_FuCyLPCFHD8Z29hmYPmo_pAskGwuqytGSXtZWK2FH85eeqR28o248r1DuKNtUXaqC9S2DgVIluGd0-aH1zs1C4bKkz0OCB7OxfICsPttvnnazAIEFtD8NTCk4FPn5Fcn80eLc50H--ZlGwbU78kS9UW52EVyPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
قالیباف: تهدید های ترامپ بکیرمونم نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/78362" target="_blank">📅 19:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78359">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو: تا هرزمان که لازم باشه برای حفظ شمال اسرائیل توی منطقه(جنوب لبنان) میمونیم و همچنین اجازه نمیدم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه.
ما از جنوب لبنان عقب نشینی نخواهیم کرد و هیچکس نمیتونه اینو تغییر بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/funhiphop/78359" target="_blank">📅 19:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
عباس بیا بگو چیکار کردی چه سوپرایزی برامون داری از مذاکرات
ترامپ به فاکس نیوز:
شاید کنترل تنگه هرمز را بدست بیاوریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/funhiphop/78358" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کونکشا دیگه زمستونم که مدرسه و دانشگاه نرفتید، دیگه دلیلتون برا تابستون فن بودن چیه ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/funhiphop/78357" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78356">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اووووو رامین رضاییان
🗣
🗣</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/78356" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQRvw4HWYRAIsxHzr4uG8N-j-l9jY8xl4jAk-SheRhst_cw3wBBtTtcLgvXpwQSjUtIUU4Fx2Cv9XRC6v1-8YUZWvL0ozDOPQF9EQEM2iQppyLjGduTSzRj4bBLHleXoWOJj48VNpS3ODyeRj1mA69gYNLPqryzGrGctVj6E0slK5Oxb50NsdxkLvscbx90x3EMOnkzZvfaW9Uie4Hj4JwLorSOPKDkXLwd8yuwzac3t8dgGHAsoumWohz-nLav5h9DKFVe5i5AVabYFnCMlLENIpMQVAV-dYVOTBq_JrOKt10xF95Sw_jj0Xey502V1H1pEAIuboE28lNBGcoHRgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در بازی آمریکا و استرالیا
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/78355" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/funhiphop/78354" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78353">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYEflhn_cIlW8tSnrrzqr6lFsIg6gcz8TDAQBsdrfzW3RfJjMRoOxOCho63IJw2Qd25o_GH0qGse0YtD29C0ouSmExssdpkJyCP_2GAV3aqoo5YM3XhdHJ7SJFQXyK03wmshpbTr5LoF_k9_Wr4zaFcC2vqdP_7WlvMydXtFKyV-GeNtmYVcCgY63xsCqfeMDC3ABS4j9Tw_aFVACgISlK22MN0AHFB14jajC0ntN7lMdf-EwBZqDoZMT54z2uFW9cIyQPstRr8QIrx7Z4FaRYqi4ijMAqjUcUd7UoAEvgfHQSidJ0x5cpOQW7evgusoPq7003XzTafaiiKUmNEw7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
🅰
g31
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/funhiphop/78353" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تحلیل فوتبال با سامان ویلسون مثل تحلیل سیاست آمریکا با مرادویسیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/funhiphop/78352" target="_blank">📅 18:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مطمئنم که سر مهریه به توافق نمیرسن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/78351" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ:
به مذاکره‌کنندگان ایرانی در سوئیس گفتم اگر تنگه هرمز را ببندید ما بقیه کشورتان را هم تصرف خواهیم کرد و حتی کشوری نخواهید داشت که بتوانید به آن برگردید.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/78350" target="_blank">📅 17:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/78349" target="_blank">📅 17:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91dac02670.mp4?token=QmCMbXL5V1X9qnfb2Qcvrt2P1Ugh5II6ZmbyemN8n203hLmqXEUXL-z3O6RwEz2T6F5R8OYPwLK-G7Wl8U4Ul-y7tUIaoRzyKb87JiAZOYuOC3BFmD6YZojfz32ZvtYXZf88TV-JgxQVL_he4pLTP-Jb-51la-bdjF13WCrzerq7lKhaH0jpQEKZ7UzLl-R6hAyjoZCXcHD1_-UXRRzDL9oAJRzWwPbYF0cD2mL0SChkByTpEfhgixps536pOdGDHxxFFnCjsR2HRkNeiS1thvNGrr26x8rCRjqhd_aQbGB7L6MZu_mdshMh0rzE6e-oehryoRfDuzM_SjzOjVrO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91dac02670.mp4?token=QmCMbXL5V1X9qnfb2Qcvrt2P1Ugh5II6ZmbyemN8n203hLmqXEUXL-z3O6RwEz2T6F5R8OYPwLK-G7Wl8U4Ul-y7tUIaoRzyKb87JiAZOYuOC3BFmD6YZojfz32ZvtYXZf88TV-JgxQVL_he4pLTP-Jb-51la-bdjF13WCrzerq7lKhaH0jpQEKZ7UzLl-R6hAyjoZCXcHD1_-UXRRzDL9oAJRzWwPbYF0cD2mL0SChkByTpEfhgixps536pOdGDHxxFFnCjsR2HRkNeiS1thvNGrr26x8rCRjqhd_aQbGB7L6MZu_mdshMh0rzE6e-oehryoRfDuzM_SjzOjVrO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس یجوری نگاه میکنه انگار اومده قرار دعوا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/funhiphop/78348" target="_blank">📅 17:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دیت جمهوری اسلامی و امریکا شروع شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/funhiphop/78347" target="_blank">📅 17:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ:
جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/78346" target="_blank">📅 17:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVlHci3M0elQACSqjHricvKIf8B9RK7A3_fhI1dcpDDaPy5tBiXim3kpnXv7MQEmc0Wr9gJO4B8sNH7GtJzLNHp9uuCbwqtqLGA-nm36oJQEJ2wTOCDNU2xiRUtjBf494ERPInc-7JFOBkGgYG1Ozn2vM_51eY3n19PXOQY2phC6RO4RrbZZlhj_N_NlUSlVg2qESilZAaS5DoSW4j7utGuLeWqJn-UgvRI-nSYjGfkePQB0Vi0SKFcAG9PWtjq8TyX7Ipr9tkHgsU_hCoV-nsyWs21qrubZQHdmi8UoETQASg5T4mSvaBDkW0gCVRJlCpdDkapRwinqN4Jx2CSveQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/funhiphop/78345" target="_blank">📅 17:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عباس دهنت سرویس سوئیس هم بگا دادی اخرش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/78344" target="_blank">📅 16:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c4bf1909.mp4?token=B1V9JvDiTCLEPgvw6PkX4Vmwq_lO2nDwiaTk5cD513lvAZWZhU9-lJDyl4-JcFIJSf4FxMMG8JjzuGXn1cphPaktiSYrTum7fjNbOzLpS0V0qZCU9slvdWV3pnXtNONBxr9lnEE5XMdc3qIrdrQxcfx4qVNP27ximTl20j4eCU2074bv3gkqnik5bUCIr6va9ENEb4HHFqPnosn1quUQaHlYN3AjvCOY4JlraTuDzcDqod2B5CgY6ggEmRkLqRiTPXm5Qi_UUhAKE4kJh0k-LriT2TqfePqzpje8Z_XTl0vbRAvgZY-Bzps3IVRQ01lzcWKiVpiAsi5ohxZdUyeXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c4bf1909.mp4?token=B1V9JvDiTCLEPgvw6PkX4Vmwq_lO2nDwiaTk5cD513lvAZWZhU9-lJDyl4-JcFIJSf4FxMMG8JjzuGXn1cphPaktiSYrTum7fjNbOzLpS0V0qZCU9slvdWV3pnXtNONBxr9lnEE5XMdc3qIrdrQxcfx4qVNP27ximTl20j4eCU2074bv3gkqnik5bUCIr6va9ENEb4HHFqPnosn1quUQaHlYN3AjvCOY4JlraTuDzcDqod2B5CgY6ggEmRkLqRiTPXm5Qi_UUhAKE4kJh0k-LriT2TqfePqzpje8Z_XTl0vbRAvgZY-Bzps3IVRQ01lzcWKiVpiAsi5ohxZdUyeXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوفون و نویر وقتی میبینن نیاز نبوده ۲۰ سال کون خودشونو پاره کنن و چارتا سیو جام جهانی کافی بوده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/78343" target="_blank">📅 16:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پزشکیان:
نگرانم مردم ناراضی به خیابان بیان و اعتراض کنن. اون وقت ابهت ما فرو می‌ریزه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78341" target="_blank">📅 15:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اگه برزیل با درخشش کونیا میتونه ۳.۰ ببره ما چرا با وجود اینهمه کونی و مادرجنده نمیتونیم کاری کنیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78340" target="_blank">📅 15:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78339">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پزشکیان:
توافق رو گردن من نندازید، تمام فرمانده‌هان قرارگاه، سپاه، ارتش و امنیت در جلسه شورای امنیت ملی با توافق موافق بودن.
دیس به مجتبی خامنه ای؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78339" target="_blank">📅 15:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستان یه نکته ای بگم
مجتبی خامنه ای طبق بیانیه ای که داد گفت به اصرار پزشکیان این تفاهم نامه رو قبول کردم
نکته ای که وجود داره اینه که حکومت اگه یک درصد امیدوار بود که این مذاکرات نتیجه مثبتی براشون به همراه داره به هیچ وجه اعتبارش رو به پزشکیان نمیدادن
پس نتیجه میگیریم که این مذاکرات صرفا برای وقت خریدن هست نه توافق قطعی
ممنون از توجه شما به این موضوع
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78336" target="_blank">📅 15:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مذاکرات تو سوئیس شرو شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78335" target="_blank">📅 15:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه رپرایی با معروفیت کیرگوزی میکنن که سر جم ۵۰ هزار نفر نمیشناسنشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78334" target="_blank">📅 14:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن    @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78333" target="_blank">📅 14:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ولی خب اسپانیا چون تجربه ندارن قهرمان نمیشهط آرژانتینم چون بیش از حد تجربه دارن(پیرن) نمیشه، تنها تیم معتدل انگلیسه که اونم لوزره</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78332" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هلند بوی دوباره کیر شدن تو فینال توسط اسپانیا میده</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78331" target="_blank">📅 14:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ژنرال شماره دعانویستو بفرس
تروساد هم از ناحیه کتف بگا رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78330" target="_blank">📅 13:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78329" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0Z4Ia0mBFbQoU4BiQIRct01srBKVsqlitBO3qVZB4hiBShUNJkymcEUIpySr8ACfyZsI0lKmyx4vR-MXYwhGqXP6cid_VFtx8lkXZs-3vQfdORlB5YvCuNMe3YkXByw7GL9L9oHZ1UELTOI3L5Qk2KSGelcMAUofxZFmaJ2QLURN7dM82_TwtCihDeBMAsXNxtu1I_P3hojfDNwofObkMSqiT7VBDzJfaY0CaW74kJN7NdCbq5hzuClcq69-1zMYZXlmD1jiTIHqaJ5-KWdOCOn_WZRTUje0S8Uf_d9znUGYWpga1C3uRsV-STRNyw4ug6PawTkKKBtvhXNupVhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرچم یکی از پر افتخارترین تیم های آسیا در بازی دیشب
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78328" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mupVnaddIFVAJ16xSw9fZG13oyg3YGLXrraekOHbCekSm8R1EvAuT05FLeW0vdwH40bOoTEnADBh2HWXAzjgsPoLCeykzdOVtCh6zqD861_GlhXjfuPA9HxT-PDGL3_0RxaNfQPUWbXyML3X64Fmr8WO3jebpvtPBGwkIJGq4rxUipTR77b995ZaI17-e0EiOJSrcnboqf9qt07qWVjfxiQvij16A4b5MNkCxi7HDbBS_XjX_3TVHGTt8IfdZmtF3Ajy-RA8xbfkSPnuYKvYNt4E52iBLkUqiMtzcsfVUZfJwQBctMPtIMx0AO_2dp6wKtQ93sblScSEcVcnZa065A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال توی یک تاکتیک پیشرفته رفته عکس بازیکنای بلژیک رو زده روی دیوار بازیکن های تیم ملی تا امشب بازیکنا تو زمین نتزسن.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78327" target="_blank">📅 11:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnfej3zAS3JRz8l4tMycOUMY-PuFh7wyTPma-WMPIoo9yQdimauzsSSiGUBENPR8bqQLJjysz6pxhfyBAr9zEt9R2TIlWc1E19nf6ZWBJliyzHjuNTY8UpRwsw8KN0j9MkA_bf3H66JuT9DZ9_eIa1d3aK-rpnaJFxAPko3RCZNyauAY4i3erDmfyuAtce137UjnK6bZ51MJOBRE3sGrz36n-RFfrt6Twjcb8M1lMjw3isnwCFp2pPlVl9z4t3MkBvaPAcI2ELVA6deeSqGXaDtGQRE_b08LWdjF1i-ZxkcC6TjnL4vgax8vNYzOl2gKCk9_P7ZuaCDLvThDhqL0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم رونالدو از مسی بهتره، چون ممه های زنش بزرگترن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78326" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان دریافت کنید.
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78325" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4SzoDHiyIANp0SOl_sSmXvfpNO0HIJYg2G2KTR-YfrH1HZfbIdDnlKaafxjEXIjf1AjyU7Txx1OKvmgirRiol0j5DrTFUCbmvPmFv3xpYZ1pYDOizErmfVOQFOXTdNPxAKGeEScQxJd1PjrJsAjYdDgmOCenL5Ltrf3bCFyBStRwCpRrBGT7jxwBs_q0Ao6lLilwmuMWL0IfNoLeejsMumgFdmDzqeqyu4QmSNqoPvUakNSn3sHzLf2NkctDWN7neb0cuSciwthicKp5aFssKQFFA-Jt2VwgwkWQIAwHn30U1dWyL41zrL01PfjpDoUM4kHx5uuJJbKmlDCj7xE6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیشنهاد ویژه فقط برای بازی ایران
🇮🇷
- بلژیک
🇧🇪
🎁
🤩
🤩
فری اسپین رایگان کازینو در انتظار شماست!
فقط کافیست حداقل
🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان دریافت کنید.
⚽️
بازی ایران
🇮🇷
vs بلژیک
🇧🇪
💰
حداقل مبلغ شرط:
0️⃣
0️⃣
0️⃣
0️⃣
0️⃣
5️⃣
تومان
🎰
جایزه:
0️⃣
5️⃣
فری اسپین کازینو
⏳
فرصت محدود!
همین حالا وارد شوید و شانس خود را امتحان کنید.
R31
🅰
❤️
Winro
هوشمندانه بازی کن، برنده شو
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78324" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کارتون فوتبالیستا تازه داره رو ژاپن تاثیر میزاره</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78323" target="_blank">📅 09:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این چرا جهانی شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78322" target="_blank">📅 09:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3uHw6cMfSd-VWE0JlOuJaoEG2fVg3ZQ5bjiZdPOA8LyZLlJF0mDhPW2s8dDXOYYj8zKMcGsRO6-CRWuf-yT4eODo9CtcElNaZQnkdjwoYlyu2Iw2ZbVoqg1YSPNoZK925-0wqNABlJmm-8C8adYO9mN8Sk2-oMFYmb6P1atgHFLBixKr1Zc9kfRtX1wlrEUCc-ms2fRd33Juuy7LQerw6SBq_c08bBrzAOWcAymDy31GHcnip-rSTTDQ9hCJeCfRB8QaLHfXWhFYLr8YLplSg7TDepyMurXS6yGhemLwoXI9uuQuuTn_cwf6V3J9pZSynpYJVG2CV5qf1MIB87UEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چرا جهانی شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78321" target="_blank">📅 08:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عباسشون رسیدن سوییسا  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78320" target="_blank">📅 07:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIQU6YCtPJVK9aF1qkpOvhsc4lii39vTunC3C-6HYrwtQxB0PV1jWoNV_MgrKFJ6xmOQBBmx66I0A7TmkkWDE6OgnVDzX2Kfbdl02HLxGQCGos0deoN-07xLTUdOAFVqFbf_dr_r_NT3XHV3MhkjpCNTiajpdgUMHnC2pZ1fWQBvE_-HVIhMvlYYR7SlA_RAh77PxmDP9eEAdKGtCLT6dD8peg3eCJ7kUChM9QX7i1RZ_iqgYtGIccZnsVmrK_93q4a115OlfhyFURnr1Ej1rreqgjIok2lF3vf9TEBv2Djg2LjHZNHlWzjAY-2Txg6iyrl1pZkQ_tjLCSNlhIT6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست دوستان ارتش اسرائیل یکی از گسترده ترین تونل های حزب الله رو کشف کرده که پول من و شما ده ها سال صرف ساختنش شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78318" target="_blank">📅 02:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_SQKhvFSwUJr3golQ7ctZX0l5wfYWAj1Ox59mTvgWCn23xAcHtvSO8hpVpbNBxk7foIx_KGAKTCWB7xrm7F82ij2WTfvchjSeDktp5rdqe10XrCb_uUTKsfrR0Gz6QaZKofLX2rzWqWUC4ZCmEwrOxGA2y-LZBEXTDynkmvxtJO-GYDcZ0ZNn5Bw4UgbViTgastOnBOxvoBh4m2jj14TvwOWa0_AmJu2Yo7sc0W4038j61IvoaP-OuMyTYvQv4CxMYDckjaTBd80Ka042EpsJnPyG1uipS4Miy2QG4iGFD9eqbH7TdAIKcwfw0BYR_qaY8tlL5B5F4dBl-I03VfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Iranian power
❤️
👌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78317" target="_blank">📅 01:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حالا جدا از شوخی ترکیه خیلی به کرداشون ظلم میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78316" target="_blank">📅 01:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCdr3PEnVYYLLntoBiHChVG0dsXfu3d32ulPmNS1aCPZRbcecZZyRXRftH4X9qV78v6kaox_sxiZWWE_ZJSz6QwBuFHgze5CynGBV9aT3rnj_Qyn9Zwsn5D9gS4M2DKN5nQ2LlAGoQCsv8BI5cYLHrjPmQdY-IGyIZFbUdiNApf0E9Y3vxHS-CGtNg2SLI_bivkUUCxhOV5rf9jdJicLOHlSQsybwitJGxkxB8xk689Tpx6HN_NEBhFEGh87pnk7PfFeoMfI8WRCM-ER4nuk2XaASg_2ih54BomIJSHMaH_A5s1z9MhN-nsUbCS6ilfBrrLDoJf8wTy7M7SbaRK1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴ کامبک تکمیل شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78315" target="_blank">📅 01:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یه طهلیل بریم
آخرین بار ک آلمان به مرحله حذفی صعود کرده بود قهرمان شد
پس این سری هم قهرمان میشن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78314" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴
کامبک تکمیل شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78313" target="_blank">📅 01:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzpTAFEEzVVcsE__ZsnIEELZb6uvBnyrLea_N0HVKgNPjMpElLqeZi4YlRw6ru_KmZhB4vTWKhQdjSHxAvqfPPtekbopwJOodKB3GUXHz4M4tx_lMcTspgrCGzBhSBlR6W5_AnevzC_kGq0mi_BvYCrwtDBP6MLXR7jlJtTFV184Jq1TeKr2YcAdM7wuhM0FGtOdiBjkafBbU7UtkuwyaJPYtCrs85s-9i8C7sn5-KrSnT8zISTx_pQgcA3KgKvoZXsX1LN9Ye0mCPl80EOHVUQelMSJA0RL7D9fT2aihpIJfTxCTS37GIaI0I5dSEkV4Ff4Y4hqYudwJmOE5fifkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمرینات قلعه نویی قبل بازی با بلژیک؛ رسانه های بلژیکی میگن لوکاکو هم از لیست بازی فردا خط خورد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78312" target="_blank">📅 01:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آلمان تیم خوبیه ولی مثل تیمی ک اومده جام ببره بازی نمیکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78311" target="_blank">📅 01:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78310">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آلمان اگه این بازی رو برینه عطشش برای ادامه تورنمت خیلی بیشتر میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78310" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فوتموب باعث میشه گل زدن تیما برام اسپویل شه، لذتشونو گرفته لعنتی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78309" target="_blank">📅 01:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78308" target="_blank">📅 00:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عباسشون رسیدن سوییسا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78307" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کیر نخست وزیر بریتانیا استعفا داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78306" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوکو به دلیل عفونت تنفسی، رسما بازی مقابل ایران رو از دست داد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78305" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">المان خورد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78304" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هلند تو این تورنمت همه رو سوپرایز میکنه
یا با قهرمانی یا با حذف مدعی های اصلی
این پیام بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78303" target="_blank">📅 22:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گل پنجم برای هلند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78302" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سوئد یکی از گل هارو جبران کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78301" target="_blank">📅 21:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حساب کنید ژاپن چقد سوپره که ازین هلند مساوی گرفت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78300" target="_blank">📅 21:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الله اکبر گل چهارم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78299" target="_blank">📅 21:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گل سوم برای هلند
سوئد پاره شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78298" target="_blank">📅 21:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گلر هلند عالی بوده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78297" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78296">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سوئد زد ولی رد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78296" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اسرائیل آتش بس لبنانو که پذیرفت الان شروع کرده غزه رو میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78295" target="_blank">📅 20:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هلند گل دوم هم میزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78294" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هلند گل اول رو زد به سوئد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78293" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGhc0s0WiXUqfLHzrUNgCLWYQcUP2iAauQtGzVgg2TZXnzAMJoSa-iYMWNRZbigSG4Yc7r8005Z64y7ZAHtn0ciDL9ikj3IsnUjSaAD2gWSEcf3h2sHVtTGUe_oTiRyxZ9FXCvBKWw_3xrzFDVSOFYWq_5f0136l3Xq4l6c36CJaD6zp_xvia8otsGpZai5bJF1NVuK7xI7JVUYyE0t-RUwqRrIftuvTB-dPSZMKqsrumf3TCrZflWljAXUUTTO0yt250kN91Bdxr1N_hy1QqpBBKj5y8BmWEGkeGZfz8MocbbTLeEX54Ttr-KzKEbUlY-xQbh1WQc6Er9kipabs_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه هم با باخت امروز صبح از جام جهانی حذف شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78292" target="_blank">📅 20:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjRRxYEIBs6d0ORG7hT7pyGBBqelVVkoC6QHSPbx-UHp2zuoHDtvWKrtE3Ca-qt-BQE_v4OaAukHn2DRblRhfXuGH_CMt08nFzla6StmGUV217LFm-Kp7tlGAljXdxab7M2V8USZxfqg7abSGIy9MG2v_6lnsWwwH6DJOFyMRubDP_atYXRc3ytc6UiCpcUilZJb_tQQrW9kbqIU5ekuEVBhg86O-EI8wQ-j0JQ9k5xjnX6-u4O-qNlAE7ZEZquFzRymcEv_DOucQT2_s5klTrgyCcbjGFX4NobUYpjBJpTZ0ZvFShKROIWKUnNzAIgpqgfG3eqbrGuCSdHP-KrC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUuofrVtOxaOrX94T87E5ejAKxDVUerW4vD38tEBtIsIDLyvR3xCqGDrjzSOEjX8xqnGmWWkXRm4iOTBtBkjkTsz14-L7AEA3Aexnu7kvc0PrvXJ8Gmg5T73oWXpNVACNdjsEuIhGwwPGS1zBrI3kVbNyhKU76v0K7PMSbFAQzzSfAuZo5FzrZdAv8sATqmiGMMe_FmlKMshVCR093EiU88ZPc8ZkCd3HRW09JhZPe_APsZdPsp-NV03diwHnwsfND17ktuI25Jg22DamFQi3I3Py3n-GfTQu3XrH7KTo0ZK9Kkq_6wqtqxeO2d2hr-kn5sGL4IWukLl_VhWZrbDrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78290" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmafUq4TEYcelKtetoh2pO7cIvOmyUqPEBJyZR2hqwOfe368pfA1qTjy-FawhzbdDAwLfgJY-cFlwaCLC-hUlptUSFF4HvJ5XvcB2flaloReDjYy-pKRVQa4e1e0W7SJSWxvWT1NwSWPewjJcAsqlYHzgzF8yC4Nod4tcHPvaug1sa-SDHL15AanXBhtCjZxtuMxhGAbrFVUxzWsKJ0hRDKtkY2Uq3jDXmuNAaGq-0WanQ-Gyyewaa3n7FGx1r5_Jd5po81l6byUsQslyvAtxnJc2OhVVA9azYteO6uREU11XFItyfDqExyQzxS3EyNY2seVzDKiI3ngiSlDmGOcfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78289" target="_blank">📅 18:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GN3Xr87OC3fJA1e6htHn4xlOWkuxrxt0mSv59QZsio7KPO89oTwNyOVzST_5xngK-a5v3HHPRbR8l2hWTRzsFzZNDO7G9PXQbb_Z7clWiuxLS5FEXcE9zebqiTXzyAZYx3yB9THu8UB0TZqu5DNvWtz_xFY6UV708EN2B8fUiDPDbEIJSQfa7JBAm-FkvMHa3a0Lz9uoxbJBw9gwVKQVEAO4Cq-8Z-etkKeO5GZLGcga9QdKDN408l75OwivTfBww8aP-LosfIeDpiWckp7bjXTXVI_Az4OdsRwyisKoTbw4wzjaHafkXLOgH6Y7YdFZ5csDjs7sHHHwHYbFqYboWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداشاهده بمب خنده، فرانکی دیونگ و تیمبر تو تمرینات هلند شاخ به شاخ خوردن بهم و الان تیمبر مشکوک به ضربه مغزیه و دیونگ هم احتمالا بازی بعدی غایب باشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78288" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78287" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baTBxjGOqjml-4dE99YdIQTbEtM1jzb4uWaCcDI36XmJ6Uc8ds-kc5Vf-NOcT1vJ-Hm3EBtIOFs-L-0ehABhWv4oN9u9NWUPk6BVzU5mSoSYqe73KAD2QMymhkmxIxZ64pXSYg4Wf-vLzRLP31LNspxEByzG73sEl8jPTA6jumcJS99f2-v-1tG-XjX7NuVJBRkJDVIP01H38x1UM0UpWrTbnkFj9w3Md4oxLQu_d_xU8TsYCeDsCorL2ub9mkhD6vV9sqltzg48prp-LvHeUyLQrNH6_HJuZfbGbbEUFYEWUvj6A_25g8kXa4BZ5REkSzpPF4QvjHeJqUUxBClluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
G30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78286" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I08TvuDHCz98NHP4FUbyojiRkpAiQzeTEuWGxxdBuvqPSC34wHOP-Xj5FfTrEZRQMKlUoLzzLPu880aQUj8vgBB5JQMTfS5BAtc1B-s5OC0P3Znx9XtKCaLal0CazvXTLu1L4jATyRtrQ4Uo-jDjaz6FLDTIserx8BTON0uFAoJ5YvJF1VcTvW77dcmMxeq5UqKvviGIS_nAKjMc8BflkafSr0P-sUNsIeT-cdBfisouZK6x0nbK4r7yMfH9UT6YOlCiz3oFvea5YmiLRB3JVhf31B8H9SIr9sSGPxWAvmKmaFANYLC-Y3zFx5yPBuav2ArvAqPydIBRhqMdNw8JEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نتونن تیم ژنرال رو متوقف کنن حریف احتمالی تو دور بعدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78285" target="_blank">📅 17:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgFrjW_1SaqXoduZ-JDiIFTfYqY3UUaquqCdWrTlTjATShN25908FC3LD2qtORl_YiuvQ0VxJJHrmEwP3ZJcy69bQHQ_UvJuHIlulWyczAndTzvNAc-jD2i_RSBYBrvvNXjpVVSi53z5ty8bRMg7qCLbh5J3VwEhzAl6IDl7IYIbR1a8m1aLoOvihbhQmqUy8elkWjWSKFdTzlFVdG_a5fnxHY3hi2aEbtc1llcjTMY7cM19sxNg6fEISZx5gUY5NGC-ivLRaZKrzUE8HGm7jZpfjHSKHfULJNH7F11g_nX0nJxrWC_TA4kER26i0qrlKjHVNoOPmcYEUH3lkkYC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی تیم های سوم جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78284" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78283" target="_blank">📅 17:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_2ndaZUUGRXop_kyjzDOOsE6a0MOkCTMnpFzuSzHoPLFgbeKN_Cj0ygPOXKEdegC_5u8V0E3QIpM8MKLZRH0oYGEIc9w1IRgiuS2roZ2S6TZy0_b5vUi6UPqXf82KGbOMXWeN5tqFc9OFPYbPF8JLvjHgIWHFTe96asZ7HBqS_dy24B0UVgk_3ZaFCpZQmARmBfWBkH3lFsJKr-Su8FH8TkgV4-A2qciusvEuNFL5_hWY-pNhGh42TCmZtk_p7imgzp3RPjXZNMi5gAgan5bMIFctmMItQHLicTJCJenn-EHsXVVkUZIIJWEPRuZbJQ9HyVBTojYU2PkDeOV-a7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم بالاخره افتخار همبازی شدن با بهترین بازیکن تاریخ نصیبش شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78282" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی وزارت کشور: کسایی که به مراسم تشییع پیکر خامنه‌ای بیان، به صورت رایگان تحت پوشش بیمه قرار میگیرن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78281" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78280" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78279" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دولت عراق مجوز استفاده از استارلینک و صادر کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78278" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJgEzjIuxV2oWGBGQ3eREQJSCOTkP2zZ7U7O-NfAICpM01yUHeqKd4ok3cGMyG0SO9KwdhlBjwq8IiUHtgoqbV5Hg5mp_vvVhje12TTZp5Pf15sAB2zMXJJOXXzZOSlm1DQjVEKxcdtDDX3YD1TSu3Cf2o2MfGiniqc1xZNZL2TVNNuAHmQ3mMpU6ch6Rk-OQ6M1Pd_JBUCtxWBWZb_xgzysk1ODf4F1VevkTKmmTXGp5hTvH4D5IWKvhQGJuewFIScLnFNjV2CSby7M5wB2dFX0wzTCH48AQxVgIxD38xs04fxy3XHMtAzU8XH4VhbE3ucEkK7sHmVaETPXDzdEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدینیو و طرفدار گمنامش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78277" target="_blank">📅 14:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78276">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v03zaw2X8Og7TwN7CCp5ZxioGp2ubTXaXevQvH3hUNsQWORkVSnotA67DmPniftkTCmfYmQCIGZxgvhaSdQNzEnIs3wvSAM-iVQYOjRqEjNEbLCchhY3ARd5jwjd_68Jp9fpqeFAQnJWQn6n0-SEVpDJExC4dQnrYxMAGvAWaH71XAB4F6odSda19UiS0BxL3QQFzYXAsvgPxj2sVcseBQwlvPv3qmT1ptteSNN5b9dkcDk1yGreWGuniRpjDi6szOcom5pHOlFAecz9p_mUkJIUPS7QliEb20eVbDbPaTFbu5DeipL7qD5UErC_hRegiOYDC04Nx8LDr1GA_u5F3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باهوشا جواب بدید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78276" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تو جنوب لبنان داره نسل کشی و زمین سوخته سازی انجام میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78275" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dx_3hU0GkN2F8_nMcqyljx8EGRjDKK9yg5R--a-PPZVltInRGxL1aWf4zGVF8An2wFpX0wiWvV1vHsecwy1JHpBupzTJuUIsnxOi_hU7C2eILXiPXfyiqvo7Gw5CfcbRhIuRuc4PMsZzIxpLjN9YrEFaA_l3QtQ7_Vb91qhfVwI5CfA0x-_BaThYnxLffGVvTu1AnkK8azLlf3soxfvMFzmKV8z4ml1eNltIrQTvWjkShB3qfyGlHIBvVSTZKIAR8QvTi_Nds8-dtzrbMQCpQUqjMuXrpIu-J9LPNrzXW2oDfKBJyMo01QYJ4x0PHde7xPudcc9XFouX0P6yyF9NsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخواید اعتراض هم بکنید لااقل یه متنی بنویسید که با عقل جور در بیاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78274" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78273">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D27TvhZJDpxs4ltQuzWMgMQasMIycAUHDpyscD6uYWO1tWPvRajr65U2jt8b2HRM49gusgbjZ05CUbznddXzEoEq4LWH7D_prWndxgWa2qY3SdQOHQZe8CfDeTDzqJ3JlsiIzas27URETbqBTP3pdUhhDFfOK0SDVKUNfpuzzlTAUQvdhnURk3jcH6NOWBODyDM87XmLdWSLpIjJbYvgWS9zD5w8HOzWa_F2QSqF2fvO5_t5AC6-yu7WqSNxilCPMMhbR1i21wlULRDNIEp5V8WZRXnWJa_B0S5jGbBdqHHHyyaEQgdXASojRhVa7tpMofQkd2V35QCJpZnZVSVzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیک‌تاکی ها هم کم کم دارن آدم میشن
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78273" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78272">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78272" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78271">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEgAMss_ogun6-up__awgit9Czy_WVgF6MZMT4WrNMf8PVI_A5uIezrVKSDLgAhrDMMmtMsbEarap6xrFaeVt1uj9jkKnQX669oHffQnjpllr0C_NWfMzrzqPANv51ekZxp0zS3Gmx8K_miaRsypknmfr9lrdyeaVV11WQSvXbzBxcwLaxv010L0m-foeg6DNQD-_AgbUmIivwKrupto7WyFsBF9CJfOxl6vfqFtde2mGMnZmUDneWXx8JoX9kzv19GNDu0E3CEA_ys-wriuQRygpMMuLfIdrliG5wnkD2_YGVmq5iz5PXu-vX_fXelwwfPphulP4v9f1-rhrzJXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78271" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78269">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نمیدونم چرا بازیکنا برزیل نزدیک ۳۰ که میشن با هر بدنی تبدیل به شیشه میشن، من دوسال پیش اون بدن رافینیا رو میدیدم میگفتم این اصلا مصدوم نمیشه، حالا ماهی یبار مصدومه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78269" target="_blank">📅 11:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الان وضعیت جوری شده فنای مسی دارن از پرتغال تعریف میکنن فنای رونالدو از آرژانتین
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78268" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78267" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گل دوم برای آمریکا
پوچتینو تیم خوبی ساخته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78266" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ دوباره مصاحبه کسشر کرده که به خاطر اعصاب ممبر های عزیز ترجیح میدم پوشش ندم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78265" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
