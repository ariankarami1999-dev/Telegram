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
<img src="https://cdn1.telesco.pe/file/TXJVEELWGCLELyETIQ0P3RuH3SgwYTZIJP4PKXTxwiiH_FrM_TfZ9uGFhNoAmL4HW3DiNpH9plNpxkdEOOZPYY7ZNb_Y24vqjZV3DzyzBW9ruSZXV3Pt0zr6zEE2EXVCDnPQhfT99_89HXi1x6WKIB8XU-xCJUlZEdP617Q1gmWN3XEyMJEYqzSm5bgurLfffc5eCN8p7QZG8HwVZQHcaM0xQAUZIHn2TOwj3xz-V0umtL_SU1lr8LIxgO3OGmuIiij9d5EGrdCmHlpEc2dLlNOc3oyLHf8ApY9G4h2nMu5xpJ02xccpO1E10IkzsQImVeb6jbr7ecHuoPFSJEGipQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 02:28:59</div>
<hr>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YzbVp-AXifei49CNPkRZMxhYmjlp87yW66S1Bjtf2r0f-UI_sLVfDyC3oPvM1i2VJb8gDIz9S_oDkrc-Y7KFP8sbdGZc-xJ4pR68gN502sRdaRqhC9DgO3MTu5MempbAhN4w9n7uq_hJZ27xPK8Zq3wB7yCPLKDHkf8vDpXshq3HWKvL02PQqbGEzfI9jBTJ9G6EmT2Q8sb_s353DPYkkfF0wNjTOEKfhW58Y6FT9WGGsoYNTLmIA9dQ9A1N90bPjIlWYWm5FhpQL8NE1ZZ823dM1edPiK357erYke9Lmo1uMGC7jZenYXOeWdyWBSclr7DjY3pE5-0oVP1kvyf0Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c0F1idn0LeceLCLvCOwEapGqT-nvSMUx6cbsb7k78ReKqSIoYxXo0WD5TXHhsG80YSTUaSC-5yKEoobpXCezbU2vWnuPmhho1el1n3x5JT11fq14UxrTa4VYHAN_c1QTLs6hRyYZN9FcuVMZ9a_hYMN58elHCXlXVW3L1rRmYfsodqsCDv2GJZMhLPcpLeIE1Mvny-XnppWggoPCophHSEGe3_6nfoqzaOjx33_TqGUW9rnLnSEkK5AtbhJ0JC07WK5wpVvZjjPqIiq0yKZ0fsb1sHiBJS5YXFxvdNrfAgJMR46BxT0mmsrF2BJIy7mJwXSwPu8s95XQuefXt-xrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mYCVbNh74LL89B6HBjccXM9a9nuZEwiSpyGLRITzB7XFfLrwQxGylWOl_uI4AEKXaxaBM7hnEoKR7Hp5hr1cjAiUN3NITnY06dVferH0pXBdTsXQm9vvehRS4qmLOR57rt-Crmspt6_GMl8IsAaU-8L4M1U5jKYZidCKjKCWc-qVCgXR4M1UDrM8tU0TUZH1Ypk7XWS_q4EPvUdakmVH8cw2b0saeUYT5wm_JXqyylK7397lN42yEna7s8KL7q9-xzdQQlVS2xa8H-hGCngxss62JUBcHyes3LVRRd9NB9FbzuqUVPLDvT8bvLWZw0ndlzhvWHjvTeoOaINHp1SwxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZhJsEV7O6gz2cZSDkULi4E-OBGdEUM2bLvEPIr640arpKHzupqNwnEpiAy_guFROkKFY_3SxkT-IzVo8HBzSfGf3ZdAEqFif-CxKy85KENYrkW9AMxNfzLfTavKstAl6HlsQptcOJ2jMcpSSCKUwHmS9bj9xEKxwCSmyGTk6ioeljTODxr3mTJJKcdXxknxiAb2Twd0Txh8UoTqQ68v7JF8KfUefO7-SLvC_aQIlFmf9xldDxRQLsDJErgNQESy1wMhqqeV9GvC8JqP9PJ2gKgRbDQMmh9q9upTiiTjCBwJsCDN_LXKCgC5hZmXjoqbjJVRFwtNz2Q2Wk2uu531smg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hwcCnyR3VRkENX98OlzD40QWcNfdxcRsMplFjeEidAuQJki3zGXvRoOa143QyDw6UZz6fhX3JyhmAnyCTzxb9LAc_jI82Ki5gfVa8ECpq0Rs3Ta9GqXZzcSQrFa0svZYBdah8CnymO4QAOW71CWXJJEsU-3hwD00ejM_e75N6Etlx2j-0NbpdRiW__zoOkcMYaqvWdyM7NCAEiAmB6q4NUA_2je8ZjEuuRqG1PADpnOqFXiks3RP8a5SkcaG4a8NVpw8D3DGKd4OX3tvvNg7YlTNBmHFuYPZaJVnO-mJKai16l8fo0XcpsEspmgXbUoNxrMCBJhY5IXtcUSknQnvIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S2xgY3Ogg_TWHYW7ImIQsui6q7nTizBsCghDRnec0C9g4-CF8VnN7eLMP9Bm83FNjoR9fCEeOuh9HWZR9CUOK_zvjUbe8DnHTB6llxk4vOxOQoEl9YezwA7-uLvHjoK_Umu99WG7nE30OCXFyStOkn7rGMN4bG0Wt2KNjNejsQDzo-o9nZpjEk2JgL6maKIAzCQzzI_DfStnyBH8h4FtYIFauoa1oZ0DQJ9A9xM52FS6qjsBMmvvR4wEGupgpPFlZptvtJ5Vq6TGQpiNorAG_8sSa-z-tsoMzps5C9Rs_lOENOlXTQFR_Cr5b0erA_Rv1dI02O8XVfgxX5j1R9pMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iRvM_fgeikUXVI4dPJrF8-FW7QMCojYug0GJCGnibt2Fmuvny4qyiYHMnrnD1Lt9hyUgGsXcZui18oMmfPD9hAkIRBe_AghHdJVfcUznRurGtQP28KLOHQdyY8J4BfKQLrP2oPUylcXIsdxB-PEXizmFHVbE6I0SZpRBG6vBvZy59F09PVtf8oS0U7WVw1Sqdt3ELOFEtdi3Neq1acFEpITT0kcJOFj1Ksikg2L2fbFrAfaKVsH38Mi0i7lW5LBYI3eo3w7947EFGojE6NdSuauUwRWxjj0jvai1JU0sOx0iQ9cylgnsnKNQbLAUgw3zYwmgJrGximxwtfqJnoYgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n15bnOGiIjbxwXZtzf9VzgkPQwk9LtH9B0mN9ubuevR0ONqc20OuaOpfoIDeor_gQRyARv0wXEbH5XSoPwhr7M-7em-onf3GTDjtoOu40BHXgdDZ3U9NbeLp-qjwiwnZ3uAZnnB3Kyw_INCcPmQKlrhwYxzP6g7Tp0FaK8f1Ni5toxYpYgGUtKumvuD0qCNqRaq04zt4Usr2Z6wVnokfPjll7no6Be0OGNoOq9UH0wwZrtwtbvtRYpX64D99jdFwAYjqMSoAn-VHgx7eFD5OuO3P1ykASKrAQIKJ1VeB76SdiE4HRFUSiRCaxw0fSkhwqS3h_BX296PfofrREev2cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ پشت سر هم پست کرد
تصاویری است با عناوین نظرسنجی‌ها درباره توافق + ترجمه ماشینی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WavEG0ZwnLSuuKPxMbC2Fp561OSY3EBz-Gn71zMQurS0qrLZDZ3ZVpyv9kOXW-w3UBLhuklvO_ZehZkyBnxQ7aetUS1DpNmKpnOInsx3okQS165Vm10G1ihUZSNfsq5TnrT4HAKl7pAD7JKDxwAG5TSO2Gi2nQgjXtkSeOtDITiwBCClC70u0qSZzPlW9TfPwoTxN4bRDt8vtWCKPa_S_N2mYCoTwyai57KjP-hr6LrmfIX3iwlufVUFlcVOB13ujNlAzRsDk27yRmQHN1TjwMWstCcKYu7J0B3LywKg3ZTf683N2H-ik0wPax7MiZhhYvxoQ2J2WwuMr_YEXABYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a2d9ce530c.mp4?token=ivLxc53_j6ZHdM3hd7B8wLbkEGOoK_I0mjEsD8OIxmj-_aOsRUh6NcCIYd-QDzjue1sTUOcBs3_h8BlGdwSoeFbVj1JfeN2a3U5kpeeZIsX9iNHhQOcjzfxBQw6Bm46e_0YCMXR1YOVbyrNRRB_KPOpxw_jLLjQZZGyGiOnbBLxhNY45CUqgHJ4L3b3eIf0dTc-xlsYtZwkoJz09-qXV7pOIFQQQHxIli8EGRZ80STdkOF6yRD__CXN9gMzDyI7W5pEBm6RNAkVVzsJBuyDzQlUU-ukPxGz3EQUKYMKfKdV87ecQ_dyp-9L0iUL452Otwb1AdNPDBUTrv0Y9HDbHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a2d9ce530c.mp4?token=ivLxc53_j6ZHdM3hd7B8wLbkEGOoK_I0mjEsD8OIxmj-_aOsRUh6NcCIYd-QDzjue1sTUOcBs3_h8BlGdwSoeFbVj1JfeN2a3U5kpeeZIsX9iNHhQOcjzfxBQw6Bm46e_0YCMXR1YOVbyrNRRB_KPOpxw_jLLjQZZGyGiOnbBLxhNY45CUqgHJ4L3b3eIf0dTc-xlsYtZwkoJz09-qXV7pOIFQQQHxIli8EGRZ80STdkOF6yRD__CXN9gMzDyI7W5pEBm6RNAkVVzsJBuyDzQlUU-ukPxGz3EQUKYMKfKdV87ecQ_dyp-9L0iUL452Otwb1AdNPDBUTrv0Y9HDbHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اوضاع ما  ‏در مورد تنگه هرمز خیلی خوب است.
‏دیروز نفت بیشتری از هر زمان دیگری از تنگه عبور کرد؛ بیش از   ‏هر مقداری که تاکنون از تنگه عبور کرده است.
‏احتمالاً این را می‌بینید.   ‏ما با یک فوران نفت روبه‌رو هستیم.
‏تنگه کاملاً باز است.   ‏این را می‌دانید.
‏خواهیم دید همه این‌ها چطور پیش می‌رود.
‏اما ما دو چیز داریم.
‏ما یک تنگه باز داریم و کشوری داریم که   ‏هرگز سلاح هسته‌ای نخواهد داشت.
‏هیچ‌وقت، هرگز، سلاح هسته‌ای نخواهد داشت.
ترامپ در پاسخ به سوالی در مورد تنش‌های احتمالی در تنگه هرمز گفت
تا زمانی که ایران به ما احترام بگذارد، نمی‌خواهم بگویم از ما بترسند، تا زمانی که احترام بگذارند اوضاع خوب خواهد بود.
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه عصر گفت اگر جمهوری اسلامی «به توافق خود عمل نکند یا اگر رفتار مناسبی نداشته باشد، من کاری را که باید انجام دهم انجام خواهم داد.»
او گفت جمهوری اسلامی اهرم فشاری ندارد چرا که «نیروی دریایی آن‌ها از بین رفته است. نیروی هوایی آن‌ها از بین رفته است. رهبرانشان همگی مرده‌اند. کل کشورشان به هم ریخته است. اقتصادشان نابود شده است.»
ترامپ: نیویورک تایمز جعلی گفت، اوه، وضعیت تقریباً همان چیزی است که چهار ماه پیش بود. نه، چهار ماه پیش، آنها یک نیروی دریایی داشتند، دقیقاً ۱۵۹ کشتی. آن از بین رفته است. کل نیروی دریایی از بین رفته است. آنها ۲۵۰ هواپیما داشتند، همه از بین رفته‌اند. ضدهوایی آن‌ها از بین رفته است. رادار آنها از بین رفته است... همه چیز از بین رفته است. رهبران آنها از بین رفته‌اند. کل کشورشان از بین رفته است...»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=Z3HTDLxNUobIWaO11sZJSnA3jDTgTs_aMT6jmg_I1V_n0kmsyFsgu1_v_flWYchlxvCgUAn7UzR9BusNnmbQhR1ZIbdTx8Cm0CzDyDqoxmuG-Riao-5t01uphdko8tODiEZt2nMjDKXWxlGuFZGcuG20y23p9bVMdq5hdP0wnIC-SPEcNhfCRWKWXw17Oj5UZAD18ew9Wo0EaGa8IBDQj911YB92CtZ2vV4uGyTY6rWpRY_IUvS4SCmCNrvkeYTkECK93lM0FdVfNHCqww0fG8R-ir3me-sAVw9vUTmpLEBJPAd7r06NXrshKrrERJOX1ifxIM9zbCBE8eSsJv_mfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=Z3HTDLxNUobIWaO11sZJSnA3jDTgTs_aMT6jmg_I1V_n0kmsyFsgu1_v_flWYchlxvCgUAn7UzR9BusNnmbQhR1ZIbdTx8Cm0CzDyDqoxmuG-Riao-5t01uphdko8tODiEZt2nMjDKXWxlGuFZGcuG20y23p9bVMdq5hdP0wnIC-SPEcNhfCRWKWXw17Oj5UZAD18ew9Wo0EaGa8IBDQj911YB92CtZ2vV4uGyTY6rWpRY_IUvS4SCmCNrvkeYTkECK93lM0FdVfNHCqww0fG8R-ir3me-sAVw9vUTmpLEBJPAd7r06NXrshKrrERJOX1ifxIM9zbCBE8eSsJv_mfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس، ونس هنگام ترک سوئیس، ترجمه ماشین:
🔸
سازوکاری ایجاد کردیم تا مطمئن شویم نه‌تنها تنگه هرمز باز است، بلکه باز خواهد ماند.
🔸
قیمت بنزین همچنان کاهش خواهد یافت.
🔸
سازوکار درستی ایجاد کردیم تا آتش‌بس منطقه‌ای تضمین شود و درگیری‌های اجتناب‌ناپذیری که پیش می‌آید مدیریت شود.
🔸
ایرانی‌ها اجازه داده‌اند بازرسان تسلیحاتی، بازرسان هسته‌ای، پس از مدت‌ها وارد کشورشان شوند.روشن است که ما این رژیم بازرسی را تقویت خواهیم کرد تا مطمئن شویم آنها هرگز به سلاح هسته‌ای دست پیدا نمی‌کنند.
🔸
بخش زیادی از تیممان را آنجا گذاشتیم. ایرانی‌ها هم بخش زیادی از تیمشان را در آن اقامتگاه گذاشتند تا کار را ادامه دهند.
🔸
این دارد بنیانی می‌گذارد برای چیزی که می‌تواند خاورمیانه‌ای واقعاً دگرگون‌شده باشد.
...
خبرنگار: آقا، خیلی سریع؛ دیروز لحظه‌ای بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما دست ندادید و بعد او از اتاق خارج شد. آیا احساس کردید به شما بی‌اعتنایی شده؟ آیا فکر کردید این کار از طرف آنها عمدی بود؟ شما آن اتفاق را چطور تفسیر کردید؟
باور کنید، در چند ماه گذشته زمان زیادی را با ایرانی‌ها سروکار داشته‌ام. گاهی آنها را به‌عنوان مذاکره‌کننده‌هایی بسیار گیج‌کننده می‌بینم.
اما ببینید، ما یک نشست خبری کوچک داشتیم.
آنها آشکارا در ایران از همان حمایت‌های
متمم اول قانون اساسی
که ما در ایالات متحده آمریکا داریم برخوردار نیستند.
ما با شما صحبت کردیم و بعد چند جلسه واقعاً خوب داشتیم. چیزی که برایم کمی خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی توفان در شبکه‌های اجتماعی شکل گرفت که همه می‌گفتند ایرانی‌ها می‌خواهند بروند. و بعد ما حدود ۹ ساعت دیگر با آنها صحبت کردیم.
بنابراین فقط به رسانه‌ها توصیه می‌کنم کمی به آنچه از شبکه‌های اجتماعی ایرانی می‌بینید بی‌اعتماد باشند.
آنها می‌توانند مذاکره‌کننده‌های گیج‌کننده‌ای باشند، اما احساس می‌کنیم در حال پیشرفت هستیم. ممنون از شما.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rOtyuF9GKCIMUVraOndW5osMJnFfjB3Wb2iaJfcDO5j2Tfrw2q7-FCWMd18OxVo1E6FIWHfIh4frnhr6WtsZJ0EHkv9pYQVfZwkotqQgUKRyIWQoz73hoITf5Fpb0l2x3Vp-Sej4JFQkIZxJz3MmGmnk3o6i_9evtbZhp1a2ZsIy6oLF_dkhuy-ql1-PTNf06LEQ_cJwQI1k_Pc_k8mN_9e9A3xFDsPplSAm3oyRv5TxQFEHx1qB-AlRO4q9dhxcoInNUoJ6LY99xsWXhbrgB8-STSX7nQs5DYegR3wi0Dz9KGZF4v5I_FcF5Zy7VtZDZbEdb3yvqyktfz26uE8XSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9m-Z5WtF6KQJVshfDlcBbW8QjIs1L57vI7Taw0pdVYmvbgwNLg3CJh3O5Gf5_iU57eRvjtta0syMzk3aKVq87ajm7FMagGwlXZIlddO2gDEhSHlP0XxsZlanq7BUvuTP3S8tSmRoHFvrxmh_Isey_L5_ODeRAWBfp29ZVuXKKZeXivevzPSxSuC0yJoiQOUIHkDATY0yGBix55K5NPBqm33_nShxbaipBSVrbgvrfgJmaCgHtCYviMsNgAxHyBLa_YaBtUWqAqCyAURJfKljXGrtWKoxbgNO3feXbREy6PNNYKqFHmBk5BLAhN6e-I6ciD59sWcpzdA2vx76UvHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، رسانه‌ها خبر دادند که محمدباقر قالیباف، رئیس مجلس و رئیس هیئت مذاکره ایران، که تازه از سوئیس به تهران بازگشته بود بلافاصله برای دیداری دیگر به مسقط، پایتخت عمان، رفته است.
به نوشته روزنامه هم‌میهن، قالیباف در سفر به عمان به همراه عباس عراقچی،‌ وزیر خارجه، قرار است با هیثم بن طارق، سلطان عمان دیدار کرده و در زمینه ارتقای همکاری‌های دوجانبه و تشریک مساعی «برای تثبیت ترتیبات ایرانی»‌ برای اداره تنگه هرمز گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76598" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sKH2yLwUfGJV_B_LxnTf6h-vEN6czN5K5XhnuTq825RQqg6UMr3WzCpyCDRtldDLr379g4fa1fmku0DQ0bHlnTrBu-NhhWo7J6oM0yLVhKxaakTnoXmmeHGt6cxPFsiTm1QClwL1te1x2okbwwOcsvknuTlZ3pWK8l0Ca6Xy2GCzOwe0B1jS4j_c2eFIZ-K2wLA8as5zcXosZGouqLgcaf4XLLbd1MhCJI1VVAiVaKTc1WsqadaMya1-I401vQUhEz0RADWfMfwRssR2JYJEjm-d6-q7PCVJX5QaLuq0rTU-a7yuV1oqAAIKdYBKPT5bt9ObV55dHrtxdC1eJCy7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نوشت اظهارات جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره بازگشت بازرسان آژانس به ایران کذب است و در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76597" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=SZxb00i8fbmN8xoADlbk7YpbiR_sEMLFEGrXAJU5g6ZVnGu0md1O84gEUK2BF8urxT6hVxiKy3C4rftkTeKCqYfOmftvc2raZTjKiN7h5yUI4oV5GwrgmwuHsVL7nJ1McPDUD9OHGSRsUSx5M9po65jNTz7vQFJLTrbamUI8O5uu-MgVmFqrPY9q0ztuETZiK-B6SR1wvYGGOVIQBh41sAB-jZMwB0InuYRde1Qb_p49wAbQwSSEJ1jfiyAGStYvOW3shK57_l_z9OS77NB0CLhnD1oAzkS78rDotaBz4B0RTF8o1qnKNAGUXiM2blqEpVZ_gOFeShjm9uMwzou31A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=SZxb00i8fbmN8xoADlbk7YpbiR_sEMLFEGrXAJU5g6ZVnGu0md1O84gEUK2BF8urxT6hVxiKy3C4rftkTeKCqYfOmftvc2raZTjKiN7h5yUI4oV5GwrgmwuHsVL7nJ1McPDUD9OHGSRsUSx5M9po65jNTz7vQFJLTrbamUI8O5uu-MgVmFqrPY9q0ztuETZiK-B6SR1wvYGGOVIQBh41sAB-jZMwB0InuYRde1Qb_p49wAbQwSSEJ1jfiyAGStYvOW3shK57_l_z9OS77NB0CLhnD1oAzkS78rDotaBz4B0RTF8o1qnKNAGUXiM2blqEpVZ_gOFeShjm9uMwzou31A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تا وقتی که لازم باشد در جنوب لبنان خواهیم ماند
بنیامین نتانیاهو اعلام کرد که موضع و دستورش به وزیر دفاع اسرائیل تغییر نکرده است.
نخست‌وزیر اسرائیل نوشت: «نیروهای ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم علیه خود یا ساکنان شمال را دارند.»
او تاکید کرد که ارتش اسرائیل «هیچ محدودیتی در این زمینه ندارد.»
نتانیاهو بار دیگر تکرار کرد که ارتش اسرائیل «تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهد ماند.»
در مذاکرات ایران و آمریکا در سوئیس، هر دو کشور تاکید کردند که حفظ آتش‌بس در لبنان از موضوعات محوری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76596" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ofjh4mn3zTW9P8YUG6ropWoTL-v0G1SBASfnS7fXaCRRP7dPVwbZt02mzwHMttBHa03y9-Rg0lKJjzJm7v2epYp9JILvXyExKIEYfRPW6a9ocCAmlCdCTkkEUz-Uy0N3Wc5MfoOnNXauko8L7XMDrBSwQJ1yfd-NaVKrzPQTP_EiiRMXejVppQ2OqQQBUWdPuHoEYht6oCXbRzCMOeJ4PomrQ9jSsLz3G1LChc6Z8je7oQZAs-XbGHcHqZFzKnBVj2Z8bnpnF0FuMuV3PoSeltPhcUCoqdbNPflPVKw4NkaqprJUDRq4PL8Vh-1ymH4MVNdaMVOrm3XXD34ri8hZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا با صدور مجوز عمومی، تولید، فروش، حمل و تخلیه نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران را تا ۳۰ مرداد مجاز اعلام کرد.
بر اساس این مجوز، تمامی معاملات و خدماتی که برای تولید، فروش و انتقال این محصولات ضروری هستند، از جمله بیمه، مدیریت کشتی، تامین خدمه، سوخت‌رسانی، ثبت و پرچم‌گذاری کشتی‌ها و عملیات نجات دریایی، مجاز خواهند بود. این مجوز همچنین شامل کشتی‌هایی می‌شود که پیشتر تحت تحریم‌های مرتبط با جمهوری اسلامی قرار گرفته بودند.
در متن مجوز آمده است که واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران به آمریکا نیز، در صورتی که بخشی از فرایند فروش، تحویل یا تخلیه مجاز باشد، امکان‌پذیر خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/76595" target="_blank">📅 16:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8Zl_LS5GIRO-1zaNkh1yGsY5trn5YWH4mSEpCBpcmakpcBSppcSU8CtLvj8g6MLGviB-PxJQa9vOZeJQUgLSADDKkTiPLrPTlG4Q_haJt9cFHVUkY4jyBOCgZ6MribWrCtvVhLKZVr-Na3EUrRM6pvhXiKf-3eJnFq7U2GJ7OLOiRNLElCEctkG9MxUHhemVQH6wHZVkq3XpOZyIwmi7-m38upn8Xo73DPmeVaS-FT75-BkQjrW5pXgGHS5ZOtPydP1xq-kQqs_LMAIXhdqStQ24QFeuSzqkKCgTAqCdSjN00VDkZI1CBbvZO30l_cW-uQQ7uYElJf_KlwSTIoajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش هرانا  در خردادماه ۱۲۷ حکم اعدام اجرا شده، ۱۹ نفر به اعدام محکوم شده‌اند و حکم اعدام ۱۲ نفر نیز تایید شده است.
هرانا همچنین از ثبت ۸۰۹ مورد بازداشت در حوزه آزادی بیان و صدور مجموعا ۴۹۳۳ ماه حبس، ۷۶۶ ضربه شلاق و ۵۱ میلیون تومان جزای نقدی برای ۸۰ شهروند خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/76594" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AP8fWNaOnwld9y1qzF-tF2KELPwV_NtUL-zvIWj4LO-j_OoWgD4ZTlkANdrnfuQjnVmNd6DGmuiU1AXR7g1TqDNN1Ij51x5ZnZiawh57Sf3bDG_nHfKvPZbPD5B-kr7CR3qGMGlNgfYeoCF07TW02fAxvntfxI8TAiU9owmEP0V4psyHpMgLjhQIincGGqRxdaPiWH9icdSHF6Js16S3osI0bzpLEH8Ha7e_-b83DL55B_n_Z5UVggGfz6EDysHip90S-X_Kdivonzv8FTDHFW28A9r3CMeMfEJ1dUR8AviCY_pKfyb7UQQYICDtZXXqrWbLsAwJZNdHGeoDDWzocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VF3cPbeDB0--9VVbtfh7qtJi-v8jXQzF7Y8cvvvuFVwm28ukc7G7KZAjQ0HNA0xxWtwO2-ftoV2zZyhbSE7qiQLMmowmd6AMEzUeoHPJKXJXzTpZNdOWoXNoOg0OaU5lsELkZy0Wu3q0pKl8UV0RrCgldo-IgpVRZGTJSTYrNGvh2pV6pOi6hy-b1dXQzFX4utZIKDi4MA4yvgUP6aZSzY1QC_QmgZ1EmdugICCX1ODuGVDBEh-tY0sB68MXRwZX7qKLffm33xvTKFSkH8raSh8Gc0Tj8Zx9DujZvKXCN33NOOXdYPoEZsWJDVyEG3-uz7Oy_yeQVR18qeHJkahpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XpmqUzpXSQV0ZSE1qyWbbK5HKuGDsTwXYG9DS7Sps_03jJ7715k86WAxKOqD62Omemm9fVDvxRbLHtZxFBSmOJa9u8XQ2OqGfVcL-aGQaQezi53dDfva66s6gNT7PBPL7DAvStZ2bWFL_Rl-n_iYa4F4ITMnUsLKbETxLk8IcLChFM50kllyTI4E1qP95T4fQ5j5LRSA-NFKD_8rJcHJWlpLVV4C3BmzX5vEE7jabe6tkMLWvYfow9yEZ6iGnzOJ_VaucraN1Dp9Fe4j7otFNU-RT_Li0I5YvAyL6cNMB5PuH4so8KvWHcI27iyYzLaiEmGHvaCBsNzvvibGizJQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DjcsrVkWXFUXrI9NeDG5yOfnwH1sQswnvUumfgLAllBjT_DA10nJMHAIabzTloYWlfp7JgRHnSb9aoLX7IMoazPm2aNqzZtzmnnndR_U0PKeNpibz5Vyp8-yT54nY1Hf6QqBQW4TRZfVmmA7ljaex7Zit8cSxEHQVWvwM-7-oIpPPBqD03Zu5d19lwAFeAqempCrGCaXf7LgLYRP_-leSIqo5px9XqfXybIs0ckvSHBM2WxIwYX7zDkv0pZD2kijLzUXqoYVl_-R3eMzxOx7Z_adJtjyM8zuSyjYuVxPLEKUKn4ytYpXsyFsAV1OjvUwe18v7RolBj-a4IGuCqPvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AjwxTPolliUPF44ylIh_M8-3JmfPGeeVuT0MpR9xk_lQ6xXG4YWhwSkC3YhIwHve_rdPpSKfUPrhXROnDAtvJIHS4Xph4M40beRcA1NOprpG_mk4oZjgoeTitaR59zZmN4k1DRvK3lD6DrWO9oPB9hrALev2YnxxaAAXb6PfaAgC0esMk5pDG2XjXCorRl3Ltj5vsQShBB1Um5qvJSrJ7UuZHNc54QnI5WoIuOlvU5XN_2rBWiwdTepk4gCXs_0ztW1v2RZJ53vErIktzbBcEff0_4s15CYqgpOLI0Fd1Z8vhYuW8oJC6eiYnb_2dBwKJz8Ks35yzzLOO2xwhmxL1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=Dkd1edVUCXy7TPsL6NahGZXSK2No3Y6ZaKdREUHpmEgmHoRPWOhvVNIXqbRI3noyH5L6PdZYZYuSZKfTdBUBMumE9tfKqTuRw1mXvK-Ye4l1blhsiQC7hO8Awsife6zCfbQB0SNFDU-1SIyoYpesKPulWj0cC2R9zqxJ7JJONPjpDNSm5KlzMwDeKhwqStkGPBOKiDn3OvphLK15SUlmtSbdKHuUxQzZN_lLwqhaA5YU4OWDTtqwpGk8g872LthPa-SwJYjEWmk7O1G2Jes_uyNESkGHrWw10XhhCG2T9PfWFqJY1lBWZuDPfReSDzsbt6oAxoW2a4TZeQFgOkHNiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=Dkd1edVUCXy7TPsL6NahGZXSK2No3Y6ZaKdREUHpmEgmHoRPWOhvVNIXqbRI3noyH5L6PdZYZYuSZKfTdBUBMumE9tfKqTuRw1mXvK-Ye4l1blhsiQC7hO8Awsife6zCfbQB0SNFDU-1SIyoYpesKPulWj0cC2R9zqxJ7JJONPjpDNSm5KlzMwDeKhwqStkGPBOKiDn3OvphLK15SUlmtSbdKHuUxQzZN_lLwqhaA5YU4OWDTtqwpGk8g872LthPa-SwJYjEWmk7O1G2Jes_uyNESkGHrWw10XhhCG2T9PfWFqJY1lBWZuDPfReSDzsbt6oAxoW2a4TZeQFgOkHNiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی گزارش داد «تحریم صادرات نفت و پتروشیمی تعلیق و محاصره دریایی برداشته شد.»
علاوه بر این، عباس عراقچی اعلام کرد برخی از دارایی‌های مسدود شده آزاد و طرح بزرگ بازسازی و پیشرفت اقتصادی ایران اجرایی شد.»
آقای عراقچی این موارد را در پستی در حساب کاربری خود در شبکه اجتماعی ایکس اعلام کرده است.
@
VahidHeadline
معاون رئیس‌جمهوری آمریکا اعلام کرد که در گفت‌وگوها با حکومت ایران پیشرفت حاصل شده و جمهوری اسلامی با ورود بازرسان هسته‌ای به این کشور موافقت کرده است.
جِی‌دی ونس، روز دوشنبه در سوئیس گفت که گفت‌وگوها درباره بازرسی‌ها ممکن است از همین هفته آغاز شود. ونس درباره زمان آغاز کار بازرسان هسته‌ای در ایران تأکید کرد: «احتمالاً همین هفته، شاید از امروز.»
معاون رئیس‌جمهوری آمریکا افزود: «ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم. گفت‌وگوهای فنی در هفته‌ها و روزهای آینده ادامه خواهد یافت».
@
VahidHeadline
معاون رییس‌جمهوری آمریکا، گفت یکی از اهداف واشینگتن در مذاکرات، ایجاد سازوکاری برای نحوه استفاده از دارایی‌های مسدودشده ایران در صورت آزادسازی آنها بوده است.
او گفت هدف این سازوکار آن است که اطمینان حاصل شود منابع مالی آزادشده به مردم ایران کمک می‌کند و صرف حمایت از فعالیت‌های «تروریستی» نمی‌شود.
ونس افزود جرد کوشنر با همکاری مقام‌های قطری طرحی را ارائه کرده است که بر اساس آن، در صورت آزادسازی دارایی‌های مسدودشده ایران، ایالات متحده و قطر بر نحوه مصرف این منابع نظارت خواهند داشت و باید آن را تایید کنند.
به گفته معاون رییس‌جمهوری آمریکا، این منابع مالی برای خرید محصولات کشاورزی آمریکایی از جمله سویا، ذرت و گندم اختصاص خواهد یافت تا در اختیار مردم ایران قرار گیرد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در پاسخ به سوالی درباره تهدید تیم مذاکره‌کننده جمهوری اسلامی به ترک میز مذاکره، گفت: «آن‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم در شبکه‌های اجتماعی چنین تهدیدهایی مطرح شد. اما ما دیروز تا مدت‌ها بعد از ساعت یک بامداد در حال مذاکره بودیم، بنابراین آن‌ها جلسه را ترک نکردند.»
@
VahidOOnLine
گزارش‌ها از سوئیس حاکی از ادامۀ مذاکرات فنی ایران و ایالات متحده، به ریاست کاظم غریب آبادی، معاون وزیر خارجه ایران، است.
رسانه‌های جمهوری اسلامی نوشته‌اند که قرار است دوطرف روز دوشنبه اول تیرماه در مورد سازوکارهای اجرای یادداشت تفاهم اسلام‌آباد و تشکیل گروه‌های فنی مربوطه با یکدیگر گفت‌و‌گو کنند.
با این حال تیم اصلی مذاکره‌کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سوئیس را به مقصد تهران ترک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/76588" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lishfZbftEvV65F-gpgsKCOGDjQLVC4nZEFjudpyo9X8HpXu4MDLMLmwQZzJbEj8FMf4ivTovv-HJCm2pLXirvU3_UqroAsNERJb2lLWM_u_HYa9WRm9G0v-JjHfinNeyNSQ7Y4BPhLZGSodzTslfEZtDMkfOwEre0bMSezNonlT3R0LzqKkT3J059Y9-kQl_TgCToFHNoiPqsWx1vdj3-DfKm_rxdlA40JLIfQH4H1fSur1grYhFjJQ-wblUPOCtjvS_-e7P7JZ7MBfSlXDl_2wNtAFFsYqxp-cBP5c8F27LmfSH9p9JKmAEHiq-uT6yIZNfnWYTW4JVvYQv1Qg9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانجی‌ها اعلام کردند ایران و ایالات متحده روز دوشنبه اول تیرماه توافق کردند خطوط ارتباطی مستقیمی برای باز نگه داشتن تنگه راهبردی هرمز و پایان دادن به درگیری‌ها در لبنان ایجاد کنند.
بنا بر گزارش‌ها دو طرف از طریق تشکیل یک کمیته عالی مذاکرات، بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیدند  همچنین قرار شد گفت‌وگوهای فنی از همین هفته در بورگن‌اشتوک درباره همه موضوعات ادامه یابد.
در بیانیه مشترک دو کشور میانجی یعنی پاکستان و قطر آمده است که: «طرف‌ها با تشکیل یک کمیته عالی موافقت کردند که مسئول نظارت سیاسی بر روند میانجی‌گری خواهد بود. مذاکره‌کنندگان ارشد به‌طور منظم به این کمیته گزارش خواهند داد و گروه‌های کاری مسئول موضوعات هسته‌ای، تحریم‌ها و نیز گروه نظارت و حل‌وفصل اختلافات را هدایت خواهند کرد تا اجرای مؤثر تفاهم‌نامه و دیگر مسائل تضمین شود. کمیته عالی بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیده است؛ نقشه‌ای که زمینه را برای آغاز فوری گفت‌وگوهای فنی بیشتر فراهم می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76587" target="_blank">📅 05:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GRXbHmTBhDUg92jobpU7SauByid7W1uTff1XjGhfOWgt0KvdNg7_JD4BF6iV0TdcX1lIJbjql2-m5vsKGYWGjy559qgh2kQ3sI5ayqYgatPbuS7Yl9TGJZNL_eg1Q62zfItNfmgyl9HS3J843tqJGlyw6exlD5r94VErbWGDNeEHV4H4v8ckVWCOZmmJDliL2aixlWHGRN02vGaqXrigxIGGlchy7MaIQoYt1bUzyiQ3iYqYddAaKip93OWsDU2z1hscSBA9yrlYkWMhb6G1yL13SlwkVv3EiO9bniJideK7_rk84lQmkw-MtqvCFl764bW6LjjsF0rb8eH9D-bw9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین: ما این‌طور از سرزمین‌مان محافظت می‌کنیم. mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76586" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qFm0gpfIC6INR-dYbpYnlVrr0wjO6Hf2--HFl34PH0UDwoBIU-DuCRN5031QhVfXfuD2FZXdaU7z3Bfk1YRltEW1frcWDFpnFReCJfTzppZxsqWjZDaaWUoPLd-qQ8YXIinMCyJnhRWI1xM91-wzWn9tBl3OKxbhv9tqMFV3gVcz3F7W6c_Jq9F_9hRH1MDcEZ9XA5wS7HYR7NABoe4lMvatDZZkioZhTFRPofLNi5PuV5ht11S5gUtGsQut1Jx8b6Hvdc8_F35aNQ45aGCJBLRHkVsmEIN-mpcbhpLIwIcn8sRWmCvPQuvw4nCzETqmpz_rjultnUk4crg5HMu-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/As0I3hU0IK-HsFK6H40oqQtnvWuh5b3a709agInYgIXbNVhKiTdlTROQ--Di6kdYlVkBUCeKNQkoErpyrcbqywfroHki3IprabGeVvgRrTrSzha1Q5H3r9i4YSO32rR5O2RElE-XLdKLfzJzNZvqRj69QlUEoyViYhvB09lPwi-qCweRFfio1WldrjscWUMfTMzQrae36Pwm-YiWz_wW1C8HzkPw5SogxrmTEE_H9FJzCZzqryraN_kLYeY8g_aFDKgiEm2wDHU61MF_pPqdTjTeNd-4201gt6MAq5bgEVds1LmaD_bzn1A_5tEsDYdlItmKsbaDIUwoD026TO5zlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، اعلام کرد مذاکرات سوئیس با «پیشرفت‌های خوبی» همراه بوده و گفت‌وگوهایی درباره پایان جنگ در همه جبهه‌ها از جمله لبنان، فروش نفت ایران، آزادسازی دارایی‌های مسدودشده و سازوکار عبور کشتی‌ها از تنگه هرمز انجام شده است.
او گفت درباره صدور مجوزهای لازم برای فروش نفت و آزادسازی دارایی‌ها پیشرفت حاصل شده و قرار است سازوکاری برای موضوع تنگه هرمز نیز تدوین شود.
بقایی همچنین تایید کرد هیات جمهوری اسلامی پس از انتشار آنچه «اظهارنظر تهدیدآمیز آمریکا» خواند، از ادامه نشست چهارجانبه خودداری کرد و مذاکرات از طریق میانجی‌های قطری و پاکستانی ادامه یافت.
به گفته او، تهران بر اجرای تعهدات طرف مقابل، به‌ویژه در زمینه آتش‌بس و تعهدات اقتصادی، تاکید کرده است.
بقایی افزود گروه‌های فنی دوشنبه مذاکرات خود را برای بررسی جزییات اجرای تفاهم‌نامه ادامه می‌دهند و قطر و پاکستان نیز متنی را به‌عنوان جمع‌بندی توافقات حاصل‌شده در جریان ۱۸ ساعت مذاکره منتشر خواهند کرد.
@
VahidOOnLine
تسنیم به نقل از بیانیه مشترک قطر و پاکستان گزارش داد که نخستین جلسه مذاکرات نمایندگان جمهوری اسلامی و آمریکا در بورگن اشتوک سوئیس و با میانجی‌گری پاکستان و قطر به پایان رسیده است.
در این بیانیه فضای مذاکرات «سازنده» و روند پیشرفت «دلگرم‌کننده» عنوان شده است.
به گزارش تسنیم، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
براساس این گزارش، «مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.»
تسنیم می‌افزاید: علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.
@
VahidOOnLine
عباس عراقچی بامداد دوشنبه، با انتشار پیامی در اکس از پیشرفت‌های حاصل‌شده برای پایان دادن به جنگ لبنان در پی میانجی‌گری خستگی‌ناپذیر پاکستان و قطر خبر داد. وزیر خارجه جمهوری اسلامی نوشت: «صادرات نفت و پتروشیمی معاف شده، محاصره برداشته شده، برخی از دارایی‌های مسدود شده آزاد شده و طرح بزرگ بازسازی و توسعه برای ایران آغاز شده است». عراقچی با این حال تاکید کرد که اولین آزمون واقعی و جدی این دستاوردها، عملکرد «سلول مدیریت منازعه لبنان» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76584" target="_blank">📅 05:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI8DOsDGTxk-yNDSOsHWluVL38NE6tUeVi00tB1mekxBDwBiVFtiWPuo1lHr1hVTKhWBrdhyBOx49H2ZbmIUFaYe7sGcHre22YeCd3OcB855B918GgrUBelqdWMUc_L5d02LOn1pE90zJ5wg67H64ul--MAofQzX8dpAI4bVA8DOYz1vbwLE-hFQm44zTsEhFpdhwHwtCAN4Tdqi0UYYqy80SAfhXayRZ7T98aAu_eVRzpXAww9sICb199xf1qw9Ges03psjpmx-uCVYK7L3zoRrRbXAsq6X8c7BurImJyodA7zNbBS5xxfvZn9XNYSktflMII39cHzMt3Kb-R7NNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، از دو روز دیگر، یعنی ۲۳ ژوئن (دوم تیر) در سفری دو روزه به خاورمیانه به امارات متحده عربی، کویت و بحرین سفر خواهد کرد.
در این سفر، آقای روبیو درباره مجموعه‌ای از اولویت‌های منطقه‌ای گفت‌وگو خواهد کرد؛ از جمله:
تفاهم‌نامه میان آمریکا و ایران
تلاش‌ها برای تضمین عبور کامل، آزاد و ایمن کشتی‌ها از تنگه هرمز
اهمیت حفظ صلح و ثبات در منطقه
وزیر خارجه آمریکا همچنین در بحرین با اعضای شورای همکاری خلیج فارس دیدار خواهد کرد تا درباره اولویت‌های مشترک کشورهای منطقه گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76583" target="_blank">📅 01:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WC2Ap0Q57MhldZgntUGcAyol2BUNP0l35OB7cVxHIF_cKbBS3sGhHW1hUXY40If-7d3fvk3oSi0dnuZlO6_DsfBIuTHppzKN2SHbaqYRCdr9lbT50mNDovgOhr03WHai7GReppKz3Z-WS-Un9hSY_r1gXOPARv10DuhpioXoXSE-jF0hn0nDggYgpdkvcdRhDzqttscWbYmTtOnoceJ29Cy0riGHCa5ERaCcxVqWtW4V2czIP7bbaE_z-5286kqV_X25o8PgWw0pbdjjHLaQvDsBovJocG3CMgUvW6_sWOPv3rTOm1Lf5NdCEPv4ULi_sq19QY3m5Ka-lhDK3lGLYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین:
ما این‌طور از سرزمین‌مان محافظت می‌کنیم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76582" target="_blank">📅 01:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/obz810yIheyrK0yy8Ykq19wADD41b-jomhjTxL8L9S2H2AZ8iSo4sfrcSCZnOtH8FJ2JKPqqQlS8y4GmEH6xmirX4kc4yp49sn5hr8NFGPBaIyEW4hnhyPTzkzFjgRjnHfNKVJaENyqbw_wR7u8Ci8PIv-b02zsKjElpHL-eW3q1K7Djuy-CZInoZHqnv8kLec2Jcb3HEagZgXVGx8o9ZDn7gkA6UUSyvd04KJCYeEjQKiaxOmh0eDzE8d0e_NA9iHhwf-XiCDgv7Nm4yB_6GAKbtACGVrHyu076NV86kR4ARcksSH0wBBZNGMPfWuy4eSlYblYx4RelrDoy3888Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست ترامپ علیه نیویورک‌تایمز درباره اخبار جنگ:
تیتر نیویورک‌تایمزِ فاسد و رو به سقوط این است: «بعد از تقریباً چهار ماه جنگ چه چیزی تغییر کرده؟ تحلیلگران می‌گویند نه چندان زیاد.»
واقعاً؟ ارتش آن‌ها از کار افتاده، نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آن‌ها تقریباً نابود شده، دو رده بالای رهبرانشان از میان رفته‌اند، تورمشان به ۲۵۰ درصد رسیده، اقتصادشان درهم شکسته، به سربازانشان حقوق پرداخت نمی‌شود، تنگه هرمز باز است، نفت با شدت در جریان است، و بازار سهام و اشتغال در آمریکا به بالاترین رکوردهای خود رسیده‌اند. این‌هاست آنچه تغییر کرده، ای ترسوهای فاسد و بی‌اخلاق، و حتی بیشتر از این‌ها!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
نحوه پوشش خبرها درباره ایرانِ بسیار ضربه‌خورده و آسیب‌دیده از سوی نیویورک‌تایمزِ فاسد و رو به افول، از طریق «واقعیت‌های» جعلی و ساختگی، به نظر من «خیانت‌آمیز» است. من همه گزارش‌های دروغین و مضحک آن‌ها را به شکایت چندمیلیارددلاری‌ام علیهشان اضافه خواهم کرد. آن‌ها مجرم‌اند!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76581" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eTFNb-_qgBTfg7sW3mhUvnAGY51LNLG-_fU64kg6AIpP9oOkJ_XCAGsMwo3-VgZCjjuVkFdO2yzcEJoC89kOdnzHFMAPCbw9Q0ZvNCqggTCsCBisDuXd_NpGoIH3Gof-QNZRtqycpymp-D2TAZdFA1bzQKA34mj5vzUyZZlcRmNTlFwPujIXzkuxYZZn0AxpejkABrKoEC8HI4rLJ91vE7bpyYv_rQbBrOP_D-MnX7zYMI_xRgc4jgaL0UWazdDopzWwTctPhQdQZREAlOWls0Ty7w3ZWPDFNs3LMb_NzJietwAyeRyyqa7cq60VHrhvEGfVv1odGvb1TaLk19ArUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GG0npwgv1cBTAo15eG6-WEPeRQ5RkzyxAO1_Aoe0fBuiovxl9o39jlsM964KlplED4kNYmBywPX7mU7aEKa4unaQiztNQzcZXT0iXnharThrFgVHpIOegIrgbOCuuTVOn7-kIGvetLgKlT0QbxFw7RDhbzYv5ch44D0368nch_w0wzoghrSwRCOafRjlPFvw-Zg5pTX1j8Oxk15gC5l4aZAqrf6Vyf13zbfjuQgtyKRSVXmQfEOnBIronT7jJISeJJD7tV8qvsIR4WnhSYY76HupB1rJbVA54kGzV0Qz2Ui1nlqT3DW3xSucpou8NOiJyVh984ZgnJ2DK_VGkxLadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EevuOBGbDHDFkaM0WoyEra3_C3FdixEGhibeaBVM8I9QG7gVxTD_s36ZFFX1z6nC5xCqMnyXunCWlmjO8_K73vZh2UKl9wXimCKtWMZemQOYin2zrASGEtW6nvzrmBnC9_nBplR83inblizsAiJexJDdAANTkzj6Qlq_8SSbi4s2edajJSu7AdKRwcmWnCqRU81nK_oJazGAqzJRkJVn6cBM2TmIlJpmaDeddbriJLFfrXGct3diHy0X3Q3GpG4oWvJD4-zkrksSfAfm4wWd5YiysDrfbnbx5LUTxVR_JCvVDN0Sl4oQfjy--LjEJGee6A0V71SdOq_N8eeOrw-xDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qLNe-MrIxdvPytWaZiyia2Uo7mP0N_Xf_L19itTvA7rnTtU6_gBfLWRANvml2XJlLUGme8fwdzU6vWTorepGK0Yim5UF4T2OyMQcD1OwnlqR_welKbiV1b3oWb6D516imIwQxwXGJcv4vW0G1_9_p_ojbHqrobToomMTZGuVzme-jpr6JPMxBIZvzSUe7PX84zdFtFjWL-M2Q9oKp3qU4HxsigIUCISH96l4Zrw6qRAQdoUBk9jdjBU4514Gat6pcH6gE3NBsH-e_vCNarowhxzCYAQlItokK4qGv1bRpRPVzBmlbEtqH5oHAAp8CDUjo0pw0EALzawNbFYoTQ0HXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d4Eb0lXQDsSPOTUpchIS_3M5Jaur-5GlGe78BvA7kv-l6vSrwAW7E9FL-t6wC3_PYU2hGC4IMNKZl_3YJp65dRag6svt4QXPlU0tU1w0G2JUw7CHeR8cJkRmyOk2_HzCpvwXGrTJgxkHYf15zGHISRcQ7bfFOJk11EiAixtvMNNPQloPL8_KRNY0-y_AvcXrLMfSzeqLTd9MymLEmr2-nf6jcGmvvJjdaRHW60OZM_A4aOaQ2Oy1_s1wstYXtDckCIbzXSYSm9xl01Zxu8Af4H9DzqTerix7MmsJOD-6-abKAeadIzVnZnkHxpXNAHA8K2AgTyd2hhSDOXdbKX4tVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vwLzbb5yA0D7hyWRX00mbiEOfxXGwERMICy0DCFUt4Lg4HQyzEfOb0zD7S4Su_e5P4EmCGY2wDgL_GiCDqkYCF_PD-Eh1GevtuNUMQik22wQXjdMBgu5B8Ja66_1MgzW-A1XVanaEugp2m9HCulHEO1uvgKueOajQascaWhCguPP3QeKrgLXxkXJCrx5zNdpDsqAbQ9KQdnAy09Ew_fWEpHdN1NRFOogbgxpJQlj34WT6ihFoLmO-tCgQC0CGK9wydFGK6NB4DbvKB5S6UR7x8DFK3OCKdEnFdx8gcCPTt_BkV-Mu1SFxItc__3Ct19-231S_Xt42RwmZNCSsjXVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XHxhgxG7j8_uCltr5dAOViq8Yf-5KbXUt39frWgKO4p3e3kISuuL1mTk7EGVws0mgFlr9JMocc3VQvDfwigAR2BsZ9YfUvemWs1keh2E43dqwHPDeO39vvEzZkudC5gRO6sAgvn4ZkpDLu8g33EyiyKf8dvoDnxH-gOXXr6KhnFUwB5dyESiYP0AICbqmzgdP8gICUK-4MJ9YNeqLcJo3mgSA7Y-yDiyx_MTGmP6S20uxbL8ceGTVoSgpFZF_JMfsO7jHFZYAXjOzG3k3kA0KKM-c7tGXeNQBdWsNyBrbiTYljwnH7offikxDhfTi5FpYCHTBprJpCdqQZog8Pw6Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=cmu98cNKZBc9DPgk2dhVC7XJ2s0G_fCtBe7iB8j7mMefEINmsm65Yjcv_XgT3zLl0li6xSsWt3cSfmQC0Idm34k98MnCkYHUfANR1KKP1ViSkSxsyVTSYRft5lQdiatQIwW1tnB9hG2mLpSRXb7UEMX3zn9dOkazAggWU8JV9SDABB2aOOZjRhAho5pKRFg8rRBG7KHo4__6RXMSrrpTFrpjJDDFa4M0KwpLRQLWh1sCm7_sRSFzb8UV83rVxnm9ye4VCTQw1N-g1aCtvpSj1zmNjZ2QbNR_0GQLoeLgLZFbiePGnGC7IbhVdJGg5pq8ol6gFxnC_IUQHkq-Ggg1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=cmu98cNKZBc9DPgk2dhVC7XJ2s0G_fCtBe7iB8j7mMefEINmsm65Yjcv_XgT3zLl0li6xSsWt3cSfmQC0Idm34k98MnCkYHUfANR1KKP1ViSkSxsyVTSYRft5lQdiatQIwW1tnB9hG2mLpSRXb7UEMX3zn9dOkazAggWU8JV9SDABB2aOOZjRhAho5pKRFg8rRBG7KHo4__6RXMSrrpTFrpjJDDFa4M0KwpLRQLWh1sCm7_sRSFzb8UV83rVxnm9ye4VCTQw1N-g1aCtvpSj1zmNjZ2QbNR_0GQLoeLgLZFbiePGnGC7IbhVdJGg5pq8ol6gFxnC_IUQHkq-Ggg1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال ایران در دومین دیدار خود در مرحله گروهی جام جهانی ۲۰۲۶، با ارائه یک نمایش دفاعی، در ورزشگاه سوفای لس‌آنجلس مقابل بلژیک به تساوی بدون گل دست یافت.
مدافع بلژیک در دقیقه ۶۶ از زمین اخراج شد و این تیم ۱۰ نفره به بازی ادامه داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76571" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GlrbsEwKG8wmrrbqvutJS9jqPAtZ_ddKmAG65GvOi6cRc8LDtfCwl3ekwwqoDviudQdc-0ORdLnAz9ZP3RlIebclHidLeG3_G2MOfjZTF1Gy_bqQjfBokF27LItn7Rs34SibUv0VI5VmGjanMBSTE9ljG4wbPfy5BTIp2jHuY4SfOiWDV7H7IxW7WP2SyEFu2q_D7u-1aCB4gTEbd_vF9brk5UPqAZGSo8oFULo6PPRFjhCzG6XIOFHoNc6g8qHgTSy6JYXqeqxdbd8_fbLNUlGTB3BlcDfp58Ofbt-bm2gjivDFFoNnCvTa6521FS2i_wE74RlKVQlcDAtsB_8A5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
بعد از آن‌که تریلیون‌ها دلار خرج ناتو کردیم، ایتالیا و نخست‌وزیرش حتی فکرِ درگیر شدن با جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آن را هم نمی‌کنند. دهه‌هاست که ما از آن‌ها دفاع می‌کنیم، اما وقتی پای آزمون به میان می‌آید، آن‌ها برای دفاع از ما و بقیه جهان حاضر نیستند. خوب نیست!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76570" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KtkGGuNnHLQHQJ9mYjNibZtY8A7x3jGzOxnpcAXi9JxaPkP4yowH58oV61sG-H4vDkB0VIMXyQvbWItRnizW9AqNZhfl-t9CFSmOk3NOpupoVjlrLuOWVksBvnkVnyrjXdas0mltRqsSoxKU9Q4qaHcTY9qZD21ALyvv32He2SKN41Gc4eVnvBDvIHVbBxjlWfZbqmCyr1n3ZRqcNVtnfFhb7k174W2qC2xzIVbZpkrHXCXe5pmv5XDPNWu0lZhY8cNEGS87e0S2cCYHp9QwO4A0XrasuNfaanfo-zkD2jYvb9ZbIk6U6IgILL2A0hKpdb8PQ97wkOqCg5jOy8Y7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ک مقام ایرانی یکشنبه شب ۳۱ خردادماه به خبرگزاری رویترز گفت مذاکرات میان ایران و آمریکا در بورگن‌اشتوک سوئیس متوقف شده، اما پایان نیافته است. این مقام جزئیات بیشتری درباره علت توقف گفت‌وگوها یا زمان از سرگیری آن ارائه نکرد.
این اظهارات در حالی مطرح می‌شود که گزارش‌های متناقضی درباره وضعیت مذاکرات منتشر شده است. پیش‌تر باراک داوید، خبرنگار آکسیوس و کانال ۱۲ اسرائیل، در شبکه اجتماعی اکس به نقل از یک دیپلمات حاضر در مذاکرات نوشت که هیئت ایرانی محل مذاکرات را ترک نکرده و گفت‌وگوها همچنان ادامه دارد. با این حال، خبرگزاری ایرنا دقایقی بعد به نقل از یک مقام هیئت مذاکره‌کننده جمهوری اسلامی گزارش داد که مقام‌های ایرانی پس از دومین دیدار با هیئت قطری، محل مذاکرات را ترک کرده‌اند.
@
VahidOOnLine
خبرگزاری ایرنا، رسانه دولت جمهوری اسلامی، گزارش داد هیات جمهوری اسلامی پس از دیدار با هیات قطری، ساختمان محل مذاکرات در سوئیس را ترک کرده است.
هم‌زمان، یک منبع نزدیک به هیات مذاکره‌کننده جمهوری اسلامی به شبکه سی‌ان‌ان گفت گفت‌وگوهای میان جمهوری اسلامی و آمریکا در سوئیس متوقف شده است، اما پایان نیافته است.
به گفته این منبع، گفت‌وگوهای غیرعلنی همچنان ادامه دارد تا طرف‌ها به میز گفت‌وگو بازگردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76569" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sEGwQEs4vtKuUeJfIZGKDv9E82fvxbOEwg8js9ZX8QM-3xFXCMqT8WtxoUjl7GEtWDSMShqpzMh0cYViza7SUoxGQXYnV7TJWgqgPD9K0kV0ppwPaqhiLqTYCC5bAUcjMtQgd9Fq4yKHrV9xU76OwVgwMecU4FM7xvuWI6Eq7t5BIFInPZDQQd8wdeMoHwFwqcnSbVh94LS-Lpeb9ngFbTxTZVbK37g_gzk8BO0GAoFhwvyQQP5q3oscOhcEOnpys4PC0UjX9z1-gZNNSsFT1HzFPk4htFZxfQtDAoqUjkXyuK8Ty6Jy11YKSWGqoCT59D2oPf-wY2AHu7PGPHVCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
"
ادعای فارس و تسنیم به نقل از "یک منبع نزدیک به تیم مذاکره‌کننده"
پیش‌تر در
اکانت قالیباف
همچین توییتی منتشر شده بود:
با خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76568" target="_blank">📅 20:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NVDu6pQvgSWI_hjrOagdAa08aoyv2_5qV0YW3J6now-B-dEEhJiQxPwKqdDgk-N1OzSNv9fIR4Pt4hXRc9Ni1lpSrRTxT-9BPjYmgnsk04l0A1tVf5-kWk9ihJaufqIN2tAroJSpG8Q_3QIbpqsz6Bfmq3EQHwXm6T9_T8ukNIx6f5T68C7H1dkM6bUR7wdXmY8bMA20CXrPj58MD9wC1K3OHLtZrW_V8xe3tuvKmaAERqtFquwKVDKlrlCO3PpiMyfv1wUxtXANDh5PRD9jzOCAXlEDQlUkX3gSP7BCbXyvfzTZ_F7zTzTmEplSYHvU0jRJAay9TeITG2gbbdiYzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در واکنش به اظهارات مسعود پزشکیان، رییس دولت جمهوری اسلامی، درباره ناچار شدن آمریکا به پذیرش تفاهم‌نامه میان دو کشور، هشدار داد که تهران باید در مواضع و رفتار خود تجدیدنظر کند.
ترامپ در گفت‌وگو با فاکس‌نیوز گفت: بهتر است مراقب حرف زدنش باشد. بهتر است رفتارش را اصلاح کند، وگرنه ما کنترل بقیه کشور را هم به دست خواهیم گرفت.
این اظهارات پس از آن مطرح شد که مسعود پزشکیان روز یکشنبه ۳۱ خرداد گفت: آنچه مسلم است از حق غنی‌سازی اورانیوم هرگز کوتاه نخواهیم آمد و طرف مقابل نیز ناچار است آن را بپذیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76567" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L2E5lWSm_TczQfL4Z4Wq_ogpUxoPHqmY-mehETwxhJqPhGH0PwcckPYsBwtooQPeyGhjkFsb952FhaxBkCB2zFGcJqDdScop0iOK9iU6aLcH-P9SgyjQOckdI8AqcuD6ocqWmxPsuW0CvBm9Cu-0uDc8yn23cpXX-wk2I0hiJkcpC4UhF5VRSVeoo5fxctYORy3KQ8NBZwfiCtQu45-hsKwKd44htzH_rZWO1SMLWBBNWMlb0V-zYKM915LDX96_RXBCxq4BHH0eF155uL6MITAXB2JAseJ835ZZZplOE1GMNwBI82OM2rVwapV3MZ73tw90-8aQ3YLGAoQhvR8mnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد همزمان با برگزاری مذاکرات در سوئیس، به مقام‌های جمهوری اسلامی درباره هرگونه اقدام برای بستن تنگه هرمز هشدار داده است.
او در گفتگو با شبکه فاکس‌نیوز گفت این هشدار شنبه شب به تهران منتقل شده و تاکید کرد در صورت چنین اقدامی، ایران با پیامدهای سنگینی مواجه خواهد شد.
ترامپ همچنین گفت به مقام‌های ایرانی گفته‌ام که اگر تنگه هرمز بسته شود، «دیگر کشوری نخواهند داشت و حتی امکان بازگشت به کشور خود را هم از دست خواهند داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76566" target="_blank">📅 17:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xl-BWCgqTVrOgmADwooK23bEqVhHYSMmkWZAYGDJYbvEeM8-CZuzipxZCvobmwZ_RKk5mEuj4j0D3sMX77p2SmpS9y8HUwtYP1gJKemaHfJ7Ui2R2csVOOLSrjid7L1zYuonjQXTdPC4eIxY-2HrWcL6XJiGnol2cIZ_0gi6xmcu5LnV5UaV989XJfysqvh5GkPRuikE4yp9A14I55LxqFjWZE-WokxkZkKXd6cVoSVRDRG3SROD_58oBMc92EusIUDyPbZntg_Rmfy6U1KtomZkEv38E4L4tRrXUz5YiYdmYUGybPsdNZmaGqG4zSiAU4gPNi6M7QgdAJedc33teQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران باید فوراً جلوی نیروهای نیابتیِ بسیار پرهزینه‌اش در لبنان را بگیرد تا دیگر دردسر درست نکنند.
اگر این کار را نکنند، دوباره به ایران ضربه‌ای بسیار سنگین خواهیم زد؛ درست مثل هفته گذشته، اما این بار شدیدتر!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76565" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=Hqx2bf-Br57OiTAfllZicyAvu-0XjnCrvPDqNRq1JE2nwGHbmriwj9H4AFHnW2ZsC_f2gjUMFJ0SOye5HU9PO7n-OtkjNvHXRyVTJYAC05VEyW9ZS9a1nJhof9sTAY7nxlMrI0gCCVx8L4ET13SUy_0uavYejc2Gm3Ajjuutqc43pRd_WFYu58qRrYvX05VDg3rKO8mK72q6504ERWWGqP3s1RSNqr13VLXaUTCJJ4qJRHw4U5yh03wzuzP02Vbh7lxV_RdYyvh88RL8yavZOG5214bRhrT1ughKPnXERisJ2ljsB7nobl2mICbNYd7MzEVjIscTI3VXWOTXv2B_wg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=Hqx2bf-Br57OiTAfllZicyAvu-0XjnCrvPDqNRq1JE2nwGHbmriwj9H4AFHnW2ZsC_f2gjUMFJ0SOye5HU9PO7n-OtkjNvHXRyVTJYAC05VEyW9ZS9a1nJhof9sTAY7nxlMrI0gCCVx8L4ET13SUy_0uavYejc2Gm3Ajjuutqc43pRd_WFYu58qRrYvX05VDg3rKO8mK72q6504ERWWGqP3s1RSNqr13VLXaUTCJJ4qJRHw4U5yh03wzuzP02Vbh7lxV_RdYyvh88RL8yavZOG5214bRhrT1ughKPnXERisJ2ljsB7nobl2mICbNYd7MzEVjIscTI3VXWOTXv2B_wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس و عراقچی در یک قاب
خبرگزاری تسنیم به نقل از یک منبع نزدیک به تیم مذاکره‌کننده جمهوری اسلامی گزارش داد که هیات آمریکایی و برگزارکنندگان نشست ژنو قصد داشتند پیش از آغاز مذاکرات چندجانبه، مراسم عکس مشترک و صحنه دست دادن میان هیات‌های جمهوری اسلامی و آمریکا برگزار شود اما محمدباقر قالیباف مخالف کرده است.
به گفته این منبع، محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، با این تشریفات مخالفت کرد و اعلام کرد اعضای هیات جمهوری اسلامی در مراسم عکس مشترک با هیات آمریکایی حضور نخواهند داشت.
این منبع افزود در پی مخالفت هیات جمهوری اسلامی و خودداری آن از حضور در این مراسم، پخش مستقیم و برنامه عکس مشترک لغو شد و پس از آن هیات جمهوری اسلامی وارد محل برگزاری مذاکرات شد.
به گفته این منبع، هیات آمریکایی از هیات جمهوری اسلامی پنج دقیقه فرصت خواست تا خبرنگاران محل مذاکرات را ترک کنند. او افزود مراسم پیش از آغاز مذاکرات، بدون حضور هیات جمهوری اسلامی برگزار شد.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز یکشنبه در آغاز مذاکرات ایالات متحده و ایران در سوئیس، این گفت‌وگوها را «تاریخی» خواند و تأکید کرد ایالات متحده آماده است روابط خود با ایران را به شکل بنیادین متحول کند.
ونس در حالی که در کنار نخست‌وزیران پاکستان و قطر ایستاده بود، در اقامتگاه بورگن‌اشتوک در کنار دریاچه لوتسرن گفت: «این یک دیدار تاریخی است. پیش از این هیچوقت رهبران ایران و آمریکا در چنین سطح بالایی با یکدیگر دیدار نکرده‌اند.»
تصاویر و ویدئوهای منتشر شده از محل نشست نشان می‌دهد هنگام حضور معاون رئیس‌جمهور آمریکا در اتاق محل مذاکرات، عباس عراقچی، وزیر خارجه ایران، نیز حضور دارد.
معاون رئیس‌جمهور آمریکا درباره اهداف مذاکره با ایران گفت: «آنچه رئیس‌جمهور از ما خواسته این است که فصل تازه‌ای را آغاز کنیم تا روابط خود با مردم ایران را متحول کنیم و دست دوستی را به سوی آن‌ها دراز کنیم. پیامی که به مردم ایران می‌گوید اگر رهبران شما حاضر باشند از نقش‌آفرینی به عنوان عامل بی‌ثباتی منطقه دست بردارند، و اگر حاضر باشند در بلندمدت از جاه‌طلبی‌های هسته‌ای خود صرف‌نظر کنند، آنگاه ایالات متحده آماده است روابط خود با آن کشور را به شکل بنیادین دگرگون کند.»
او ادامه داد: «این بدون تردید هدف ماست.»
ونس همچنین گفت: «ما تنها در چند ساعت گذشته پیشرفت‌های بزرگی داشته‌ایم و انتظار دارم در ساعت‌های پیش رو نیز پیشرفت‌های بیشتری حاصل شود.»
او با اشاره به اراده ایالات متحده برای «متحول کردن» خاورمیانه، افزود: «ایران در گذشته یکی از عوامل بی‌ثباتی منطقه بوده است. اکنون آینده‌ای را می‌بینیم که در آن همه بتوانند برای پیشبرد صلح و رفاه برای همگان با یکدیگر همکاری کنند.»
@
VahidHeadline
جی‌دی ونس پیش از آغاز مذاکرات اعلام کرد واشینگتن طی ماه‌های اخیر بیش از هر کشور دیگری برای توقف درگیری‌ها در لبنان تلاش کرده و این روند را ادامه خواهد داد.
او با تأکید بر اینکه «صلح آسان نیست» گفت رسیدن به توافق نیازمند تلاش و «بده‌بستان» میان طرف‌هاست و افزود هدف آمریکا تنها صلح با ایران نیست، بلکه دستیابی به ثبات در کل منطقه دنبال می‌شود.
ونس همچنین مذاکرات جاری را «آغاز یک گفتگوی فنی» توصیف کرد که قرار نیست همه اختلافات را یک‌باره حل کند، اما فرصتی فراهم می‌کند تا طرف‌ها برای نخستین‌بار درباره مسائل اصلی به‌صورت مستقیم گفتگو کنند.
به گفته او، حضور رهبران سیاسی برای تعیین چارچوب مذاکرات و حمایت از تیم‌های فنی است و با وجود چالش‌های پیش‌رو، طرف‌ها با انگیزه برای ادامه مسیر آماده هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76564" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=XWA6jEjl75LhNI39JcRrEGGm-5sHxah86kEvB8EAH-mz8hRsyJiEpLVv7Az6tSlxa6_abN7eVNHFzuB2QS5TpobxWvb4iA21hVRXQti4rsAfWD4qxxdYLCRJxKKku3x6dr-YElY4yM68tEV6_BKxjNyF6CmwEfZkK81nowHTtoEJ1_II9ShUV6FB43WeYOSwnNo_K5dz6qtg9CEgHE-AQaSQzbhmwfPJLOd68ya8tx2DPIaKbRp2I1Gwb7Z4nQv0oRfiBPfYxVwtSoUXYUt0uzIYxyAeTdEoOz8_tIKDafDHheHI-ypbqlfKPCkeYeWVHBvS8xjcoWo34pI92KQK5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=XWA6jEjl75LhNI39JcRrEGGm-5sHxah86kEvB8EAH-mz8hRsyJiEpLVv7Az6tSlxa6_abN7eVNHFzuB2QS5TpobxWvb4iA21hVRXQti4rsAfWD4qxxdYLCRJxKKku3x6dr-YElY4yM68tEV6_BKxjNyF6CmwEfZkK81nowHTtoEJ1_II9ShUV6FB43WeYOSwnNo_K5dz6qtg9CEgHE-AQaSQzbhmwfPJLOd68ya8tx2DPIaKbRp2I1Gwb7Z4nQv0oRfiBPfYxVwtSoUXYUt0uzIYxyAeTdEoOz8_tIKDafDHheHI-ypbqlfKPCkeYeWVHBvS8xjcoWo34pI92KQK5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، همزمان با برگزاری مذاکرات مستقیم میان ایران و آمریکا در سوئیس، گفت همه نظامیان در شورای امنیت ملی موافق مذاکره بوده‌اند.
او در جلسه‌ای به مناسبت تشکیل بسیج اساتید در دانشگاه تهران، در میان صدای اعتراض عده‌ای از حاضران گفت: «همه امضا کرده‌اند که این راه را باید برویم. حالا هر کسی می‌خواهد تفرقه ایجاد کند، این گوی و این میدان.»
او با اشاره به نظر فرماندهان نظامی در شورای امنیت ملی گفت: «فرمانده قرارگاه [خاتم الانبیاء]، فرمانده ارتش و سپاه، و نهادهای امنیتی همه بودند و همه یک حرف زدند و همه متحد بودند و همه آن چیزی را که می‌خواستیم عمل کنیم را امضا کردند.»
این سخنان پزشکیان در پی افزایش انتقاد اصولگرایان تندرو از دولت در پی انتشار نامه منسوب به مجتبی خامنه‌ای صورت می‌گیرد.
آقای پزشکیان همچنین با تاکید بر نقش دولت در حمایت از نظامیان در دوران جنگ گفت: «۲۰ میلیون بشکه نفت که مال دولت بود را به هوافضای سپاه دادیم. ارزهایی که داشتیم را به این عزیزان دادیم.»
@
VahidHeadline
مسعود پزشکیان، رییس‌ دولت جمهوری اسلامی، گفت نگرانی اصلی او این است که دولت نتواند رضایت مردم را جلب کند و نارضایتی‌ها به اعتراض‌های خیابانی منجر شود.
پزشکیان گفت: «از آنچه می‌ترسم این است که نتوانیم به مردم به درستی خدمت بدهیم، ناراضی شوند و به خیابان بیایند و اعتراض کنند. آن وقت ابهت ما فرو می‌ریزد.»
او افزود مهم‌ترین قدرت جمهوری اسلامی، وحدت مردم است و مسئولان نباید اجازه دهند کمبودها، کسری‌ها و نواقص باعث نارضایتی مردم شود. به گفته پزشکیان، بروز چنین وضعیتی موجب «خوشحالی دشمنان» خواهد شد.
@
VahidOOnLine
بعضی از جملات پزشکیان به انتخاب خبرگزاری دانشجو، وابسته بسیج:
🔸
اظهارات عجیب پزشکیان: من از این میترسم که نتوانیم مردم راضی کنیم و به خیابان بیایند اعتراض کنند
🔸
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد بود.
🔸
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔸
۶ میلیارد دلار پول ما در قطر برخواهد گشت.نتانیاهو اولین ناراضی از مذاکرات است.
🔸
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم، این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
🔸
شورای عالی امنیت ملی در وحدت و انسجام تصمیم گرفت؛ همه یک حرف زدند و متحد بودند
🔸
مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده/ آنها پذیرفتند که حق ملت ایران را نمی‌توانند نادیده بگیرند/ قاعده عوض شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76562" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAI__707wBgUknWv6uHUyyoC8C_ZOxTQApd7zoC7dAXDP6akutk_RZ0C5JRYYTEnezpqn-zOmUbyM0ePKPxcSpJZXncVE7KkP2adhUgdXMItenDovUFVktso4gQ82LCOX62cJQjPxDW-JEyXFrpMqsrJjZfa5FCt9UBaW5E7osGOjW5TefMYboKmYwsivdNEpDimG3raOIKac_8q-1zKS1N8L8wfNtbVARofpwdossprPTCEtBlyeUWIFx5PRU9qh0sQEMeMhVSvyXE0d2H7_td7Zd0fvWt5mPpRqWJXRkpwukw9aMU-JZ5EQarkWCWaU0TyW6CuwZb8eT-AeFMuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو منبع منطقه‌ای آگاه گزارش داده است که آمریکا می‌خواهد نخستین دور گفت‌وگوها با ایران با دعوت تهران از بازرسان سازمان ملل برای بازدید از تاسیسات هسته‌ای ایران پایان یابد.
به گفته این منابع، این تاسیسات پیش‌تر هدف حملات آمریکا و اسرائیل قرار گرفته‌اند و آخرین بازدید بازرسان از آنها پیش از جنگ قبلی، در ژوئن ۲۰۲۵، انجام شده بود.
اکسیوس می‌گوید: «آمریکا در مقابل آماده است به ایران اجازه دهد به بخشی از دارایی‌های مسدودشده خود دسترسی پیدا کند؛ از جمله حسابی به ارزش شش میلیارد دلار در قطر.»
بر اساس این گزارش، ایران می‌تواند از این پول برای خرید کالاهای بشردوستانه استفاده کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76561" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmfzgcIy1QEbQLHLDlnFi9Gd9JUO6fct5dGFYq45hMZ0zuZuhBOK4bVKYrIM-HWpZC8ayAffERIbWEsro9LCq--gHmAKUTG-AYon7Vf2x9Zyc9uUPsCrI1wDl8GbszuferJYQz9JK10O96aomtjfiFSxdc4vKZ61Faitcyhyd_-FFeCDjuLnz-alqru-aG6o63EHBySTEY-HrGV8aoI1stefgiogandlkWXueBqNIlsx-0GMw4OWgOmFt5CoJkGl7EseZd0rPUX1gLSydZDtMuIX2cvP8sV6RIBujh-jx4ZSaW0aOGQ1s-I91kT8hhB4ZdTQw0bLy7vxp8oEJdMs-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های بهداشتی در غزه می‌گویند که دست‌کم ۱۰ فلسطینی در حملات هوایی و تیراندازی نیروهای اسرائیلی در چند حمله جداگانه کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76560" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_cR5rzihMpANfswrFPdtGysEYBZGDnct4fJfXkWwPAsDf7Rf0lOX60UnGYXt5px8HEAkU3u51wBI-hR0ffQv4_rMu4yt_MuFs-DM9EROdNGsH-1UCpLtpaJu7tCv0QKvh_Sq3R4woFpUOeY5D0dWByGcMySzfL1iXEZIEcEPHHSadGGOWWtjZNfbGbruj9ourRJQvJAEzJsUyIipQNrv-yu9wjkYpqJ_pBGuqpZck6Gs1AkzgchdfnRnXJgO6fafWflzTAPAoiYWSsSr8mP_9DbpL4-xdjNDjnCrMkt6ql4KaqLN86-b1mM9h_vlr_3i9oQQD7l46YFdGLPEE_2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از هزار دانشجو و فارغ‌التحصیل دانشگاه صنعتی شریف با امضای نامه‌ای سرگشاده خطاب به محمدرضا تجریشی، رییس این دانشگاه، نسبت به آنچه «تشدید فضای امنیتی» و گسترش برخوردهای انضباطی با دانشجویان خوانده‌اند اعتراض کردند و خواستار پاسخگویی مدیریت دانشگاه شدند.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف تاکید کرد که بیش از هزار نفر این نامه را امضا کرده‌اند. انتشار این نامه یک روز پس از رسانه‌ای شدن صدور احکام اخراج برای شماری از دانشجویان شریف صورت گرفت.
امضاکنندگان در این نامه نوشته‌اند که در ماه‌های اخیر دست‌کم ۳۰ پرونده در کمیته انضباطی دانشگاه تشکیل شده و ۱۳ دانشجو با احکام بدوی تعلیق یا اخراج مواجه شده‌اند. به گفته آنان، احکام سه دانشجو نیز در مرحله تجدیدنظر تایید شده است.
نویسندگان نامه تأکید کرده‌اند که آنچه در دانشگاه می‌گذرد، ادامه «روندی نگران‌کننده» است که به دلیل نبود واکنش مؤثر از سوی مدیریت دانشگاه، هر روز ابعاد گسترده‌تری پیدا می‌کند. آنها همچنین نسبت به افزایش سرخوردگی دانشجویان، گسترش بی‌اعتمادی در فضای دانشگاه و آسیب دیدن اعتبار علمی دانشگاه صنعتی شریف هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76559" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRWPaKrYe76byZInIT2Xh-5Xn_58blBhmkb0nGj_sJuILzWtD24Ia5A9Hev8HpWdiO0lAsgAjv96_jEG1IH3DIEkJX1yRvG4biZt--DyaiqCn390kfTJXbnuCwITwN0eqWyeM10EhOAT87u4ex-Q3ndKnJqTWtufQGGPDZYLrYeoywFEC9NsacutgNIDSLvwWVUHKbpdh39imkmSIyrQd-4Xh6encUX8R4tZ_gtc2r2Ywb2ADK7Mv1CqJCFBDtcugo_bxiZPA6gNgPC7x7Ar45EoPsg4uDdpU8cEzUUQuYp-AwGK_3jtH6HcOQ0yDN8cbgBxch2w5nrwBT-pqkpAug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Beb64atVUR1Yet9-XcPbMn3IgojxkmNfbsWR3k0Jj53rHCCc5K6EaiB3a78C6lwyuUe3mY64oT6SW65QNeVsxQBcFNh6sETAZFaSmvaSjulFMAGgAC17WbKmykWk50x72nzHNtug6xHidTv5Hk0DAIbO5LxX920koEzIb3NApTjB0xun8SYO8RyJUeCRADbkaTREKNB4YjdY0YrCwfyHI6xC8233AFmdQfhaevhXihV7G3VnLKJc81DMpCMohlkYcgqYxyOKo8VJQa4GQBJUlMGVQh6yDUAH7FYpXHTcynY9ONt-d5KqbS9wgONszmyq1ArLx26gBSMYH9mN9p9T5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
جواد علیکردی، وکیل دادگستری زندانی، توسط شعبه اول دادگاه انقلاب مشهد به ۱۸ سال حبس، انفصال دائم از حرفه وکالت، دو سال تبعید به سراوان و دو سال منع خروج از کشور محکوم شد. جلسه رسیدگی به اتهامات او در ۲۰ خرداد ۱۴۰۵ برگزار شده بود.
🔸
به گزارش خبرگزاری هرانا، آقای علیکردی از بابت اتهام «اجتماع و تبانی برای اقدام علیه امنیت ملی» به پنج سال حبس و از بابت اتهام «فعالیت تبلیغی برخلاف امنیت ملی» به ۱۳ سال حبس محکوم شده است. پرونده او پیش‌تر در شعبه ۹۰۲ دادسرای مشهد مورد رسیدگی قرار گرفته و پس از صدور کیفرخواست به دادگاه انقلاب ارجاع شده بود.
🔸
جواد علیکردی در ۲۱ آذر ۱۴۰۴ توسط نیروهای امنیتی در مشهد بازداشت شد. او ابتدا به یکی از بازداشتگاه‌های امنیتی منتقل و سپس به زندان وکیل‌آباد مشهد انتقال یافت.
🔸
آقای علیکردی برادر خسرو علیکردی، وکیل دادگستری و مدافع حقوق بشر است که در آذر ۱۴۰۴ به شکل مشکوکی درگذشت. وی پیش‌تر نیز در پرونده‌ای جداگانه با اتهامات سیاسی و امنیتی محکوم شده بود که اجرای بخشی از احکام صادره
علیه او به حالت تعلیق درآمده بود.
@IranRights</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76556" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a9CQpboaw2oZZJ-iojM5AqGu4tI5La96PtHXpLn-mbY3AvO-lkkc8_QFnARGdunpCGd9XqUjIdXT5EW9TTCeJqc0Xioeb9qd6SfJRfnfBPURvZPndPjUjWc87OaPsnyUpq8oL8O2ERSyIWrGGv_TyXutFarqtDyEvKC61JCkak6QKRjJ9V_Rd-L0YI_cZtK1IVcYT0xuDjyIG5QS8M40eM_lshnZ0g-Nyz3wjuElsA87p1Jtxn7zHY78xbYJHW5QlDId8eMoE42OEYCpcmtOTvPW-yxmGgGlFjUPaGffW39VKm0UYriD-WjP-U6KRY983NnYb0GEnxTA8J-wN2llTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هیچ‌گونه عوارضی در تنگه هرمز وجود نخواهد داشت مگر به نفع آمریکا
ترجمه ماشین:
در دوره ۶۰ روزه آتش‌بس، در تنگه هرمز
هیچ عوارضی در کار نخواهد بود
،
و پس از پایان دوره ۶۰ روزه نیز
هیچ عوارضی پرداخت نخواهد شد
؛
مگر آن‌که، در صورت تکمیل نشدن توافق، این عوارض
از سوی ایالات متحده و به نفع آمریکا
وضع شود؛
آن هم بابت خدماتی که این کشور به عنوان «فرشته نگهبان» کشورهای خاورمیانه ارائه داده، برای جبران هزینه‌های گذشته، حال و آینده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76555" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJL63xeZZrHM50-S6x1VO6LT0-BiASh1JsJNF4obJ-CSJhi-YIXSdAYca55p4GP2BNljAj55xlpFLr2B0FYVFeXOFcq_Pj0Am0llwYBiPaN9t0N-2wLBy5R1lXyWHRk_oh4TJV8fJNSSsg6I8Re6a4Sb6U-L2et64cpPOCaxMY23ixd1mY4-rcQWdvE0tqwt9LBgeCPCo78vvNinnuZHYpOiWP0KV9LyqRqVFvtkBA24IzIBg3cPkMLwD0Cc1z-DOQRWoaWZwqK0TqvE55TrT1-sQv04DV5p2usK3LoklFQ0x0Sz_B_P53PjBhkI6p2A5On8DFRXovBSw2HdW-RME-a2U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJL63xeZZrHM50-S6x1VO6LT0-BiASh1JsJNF4obJ-CSJhi-YIXSdAYca55p4GP2BNljAj55xlpFLr2B0FYVFeXOFcq_Pj0Am0llwYBiPaN9t0N-2wLBy5R1lXyWHRk_oh4TJV8fJNSSsg6I8Re6a4Sb6U-L2et64cpPOCaxMY23ixd1mY4-rcQWdvE0tqwt9LBgeCPCo78vvNinnuZHYpOiWP0KV9LyqRqVFvtkBA24IzIBg3cPkMLwD0Cc1z-DOQRWoaWZwqK0TqvE55TrT1-sQv04DV5p2usK3LoklFQ0x0Sz_B_P53PjBhkI6p2A5On8DFRXovBSw2HdW-RME-a2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبویان: مجتبی خامنه‌ای نامه داده بود که چرا شروط من رو در مذاکره رعایت نکردید؟
07:20
صدا و سیما: افشای مکاتبات مجتبی خامنه‌ای از سوی نبویان در شبکه خبر پیگرد قضایی دارد
صداوسیمای جمهوری اسلامی ایران اظهارات محمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس، در شبکه خبر پیرامون مذاکرات پیش رو بین ایران و آمریکا را «مصداق تخلف قانونی و مستوجب پیگرد قضایی» عنوان و اعلام کرد «مدیرکل مربوطهٔ این شبکه استعفا کرده است».
محمود نبویان، که به جناح تندرو موسوم به «پایداری» تعلق دارد، روز شنبه ۳۰ خرداد با خواندن بخش‌هایی از متن‌هایی که گفت مکاتبات مجتبی خامنه‌ای با هیئت مذاکره‌کننده است، مدعی شد رهبر جمهوری اسلامی در مراحل مختلف با روند مذاکرات و بندهای متن‌های گوناگون مرتبط با مذاکرات مخالف بوده است.
این گفت‌وگو پیش از آن‌که نبویان به متن نهایی تفاهم‌نامه برسد، قطع شد و موجی از واکنش‌ها را در میان دیگر چهره‌ها و فعالان رسانه‌ای جمهوری اسلامی در پی داشت.
صداوسیما در بیانیهٔ خود اعلام کرد نبویان در اظهاراتش «اشارهٔ ناقص و مخدوش به برخی اسناد دارای طبقه‌بندی» داشته و سعید آجورلو، عضو تیم رسانه‌ای هیئت مذاکره‌کننده و از چهره‌های نزدیک محمدباقر قالیباف، نیز او را به «تحریف عمدی متون» با هدف «فرار از پاسخگویی درباره ادعاهای نادرست قبلی» متهم کرد.
محمود نبویان، ۲۳ خرداد ماه، در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا، در یک برنامهٔ زنده در یک خبرگزاری نزدیک به سپاه، متنی را که مدعی بود تفاهم‌نامهٔ ایران و آمریکا است، روخوانی و از برخی بندهای آن به‌شدت انتقاد کرده بود.
نبویان یکی از اعضای گروهی بود که پس از اعلام آتش‌بس جنگ ۴۰ روزه، همراه هیئت مذاکره‌کنندهٔ با آمریکا به اسلام‌آباد رفته بود.
مجتبی خامنه‌ای، که پس از اعلام رهبری هنوز هیچ صدا و تصویری از او منتشر نشده، پس از امضای تفاهم‌نامه توسط رؤسای جمهور ایران و آمریکا در پیامی مکتوب اعلام کرد «نظر دیگری» داشته اما «با تعهدی» که پزشکیان به او داده، مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا گذاشته است.
@
VahidHeadline
حمید رسایی با انتشار ویدیوی بالا نوشت:
نبویان در آنتن زنده شبکه خبر، در حال تشریح جزئیات نامه‌های رد و بدل‌شده میان رهبر معظم انقلاب و شورای عالی امنیت ملی بود که پخش برنامه به بهانه میان‌برنامه به صورت کامل متوقف شد!
ما که از یادداشت‌های آن امام شهید در این باره اطلاع پیدا نکردیم ولی گوشه‌ای از یادداشت‌های امام حاضر توسط آقای نبویان در حال پخش از سیما بود مانع آن شدند!
صدا و سیما:
🔹
روابط عمومی معاونت سیاسی صداوسیما: به استحضار مخاطبان محترم شبکه خبر می‌رساند اظهارات یک نماینده مجلس دعوت‌شده به برنامه امروز زنده این شبکه و اشاره ناقص و مخدوش وی به برخی اسناد دارای طبقه‌بندی و مکاتبات مسئولان عالی کشور، مصداق تخلف قانونی و مستوجب پیگرد قضایی است و سازمان صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار می‌دهد.
🔹
شبکه خبر ضمن ابراز تاسف بابت بی‌توجهی مهمان مذکور به قواعد اخلاقی و الزامات آنتن زنده، به اطلاع می‌رساند مدیریت این شبکه ضمن پذیرش استعفای مدیرکل مربوطه، برخوردهای انضباطی لازم را به دلیل بی‌توجهی به الزامات برنامه‌های زنده و سهل‌انگاری در مدیریت حرفه‌ای به عمل خواهد آورد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76554" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hUUYih4BYFtENJiMLXDEZcsYcVmkZpLxAdfy1ggwfOqKeRLnSltKnt8v-M1SDQizF6p2bs4LMFKhWxdSTbPQfGHa4w5QjBJYjvuoSPpYG2-EjbqkkS1x71dHc5RUk10-JR5y7Of6qy1ZChQlPk8StxiWQKitU_XXL9e47jAvCSIIasFVWO1EeM-nCIwQlWBNQibhZOII3MFrJT3LdDLg-9IGRzAF3DYGTbbwDMErjYDzDPrleb9cKCNhN7j6zlQ20HMbI4SJf2cu8PCkFwOXSKwVQojZ48mYCxy0y71mO97kVTk7-o2lhEZ6mc1KqjVFR_B9BkAXpCwKtFUByEUOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h1Ff-NxcFJZrU0xDZeNYNNh-kzP3tattMFESwePbsWTShebeOTS9IZIRJPnZSESU8m2Jy-7L8Q9ARY-SYujdYN_4NvkgMLwQMUA8jJO9o6L6DFRcy_NjkF4RDd1wYkLmMzH7koipuIwZX8Z4rSL0wQ0gOLUQQZAT6ak9nu1nZkKAPwHtai4zhcF8ACd6PPfnM6cVNmcrU55ZgEaXaNn2HU3Q3Drg3oye9lNCAGgyr23EQH7IzOTmN2HlGU25I_YZVDEqHcK9eSenCi9IRgg0iVm8dY6ty2ZkrJIyzIHsVYyVb2CHZdmNMbXFvw3G_xvrLIidayKBnevBJWZpqfoqog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ در تروث سوشال نوشت: محبوبیت ملونی در ایتالیا به شدت کاهش یافته، شاید به این دلیل که او و ناتو در جریان ماموریت جلوگیری از دستیابی ایران به سلاح هسته‌ای، به ایالات متحده پشت کردند.
ایتالیا حتی اجازه استفاده از باندهای پروازی خود را به ما نداد که یک مانع لوجستیکی بزرگ بود؛ آن هم در حالی که آمریکا سالانه صدها میلیارد دلار برای محافظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند.
رئیس‌جمهوری آمریکا در پایان با لحنی تحقیرآمیز تاکید کرد: اکنون که ایالات متحده ایران را از نظر نظامی شکست داده، او می‌خواهد برای بالا بردن آمار محبوبیتش دوباره با ما رفیق شود؛ اما نه، ممنون!
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، با انتشار بیانیه‌ای تند در صفحه اینستاگرام خود، به هجمه‌های اخیر دونالد ترامپ پاسخ داد و حملات کلامی رئیس‌جمهوری آمریکا را «بی‌دلیل و بی‌معنی» خواند.
ملونی در این پیام خطاب به ترامپ نوشت: «محبوبیت من به هیچ‌وجه به رابطه با شما بستگی ندارد و دوستی با شما نیز کمکی به آن نکرده است. محبوبیت من حاصل توانایی‌ام در دفاع از منافع ملی ایتالیاست؛ یعنی همان کاری که همواره انجام داده‌ام.»
نخست‌وزیر ایتالیا همچنین با دفاع از تصمیم خود در جریان جنگ اخیر و عدم اجازه به آمریکا برای استفاده از پایگاه‌های نظامی این کشور، افزود: «نحوه استفاده از پایگاه‌های نظامی آمریکا در خاک ما، تابع توافق‌نامه‌های متقابلی است که ما همیشه به آن‌ها احترام گذاشته‌ایم. تا زمانی که من نخست‌وزیر هستم، این توافقات نباید نقض شوند؛ چرا که ایتالیا یک کشور مستقل و دارای حق حاکمیت باقی می‌ماند.»
ملونی در پایان نوشت: «در هر صورت، میزان محبوبیت من اصلا به شما مربوط نیست. پیشنهاد می‌کنم شما روی محبوبیت خودتان تمرکز کنید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76552" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AOAC3dUfKUXTVq_meuUq_LmQKqqAnpMyCiFvbh5d1oMZ9IPiywxuflD5mgZfd5udu-z3C2iKbnTkfEWvDp4OTpACwWAXMDidD4w-oAnN9OjLaUF9bkW5XdZKArHEXjq_GzWDLjhktlkkvz9scwz467U5w4Jqp8OksDb3_1PnbKaIorcN7N-V5VXEVIBae_MtaO4rmxR-Z95e6BTNi9-FXAvz0ib6Tddl_2MAcPO_ahJ46fSWMo9Lx9qPp2Kj9oJNsu6osSKbJ_wPVZYaJRYgwqc-sfVsP6pcwLE9_rcz9veUOHLQb3G8mBqF7D4n7sGbfkMSwROpIdHq3ZV4uiFBRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که هیات مذاکره‌کننده جمهوری اسلامی به ریاست محمدباقر قالیباف و با حضور عباس عراقچی، عازم سوئیس شده است.
بر اساس این گزارش، عبدالناصر همتی، رییس کل بانک مرکزی و علی باقری کنی، معاون بین‌الملل دبیرخانه شورای عالی امنیت ملی نیز در این سفر حضور خواهند داشت.
همچنین کاظم غریب‌آبادی، معاون و اسماعیل بقائی، سخنگوری وزارت خارجه و حمید بورد، معاون وزیر نفت نیز این افراد را همراهی می‌کنند.
پیش‌تر وزارت خارجه پاستان اعلام کرد که مذاکرات فنی میان جمهوری اسلامی و آمریکا، یکشنبه در سوئیس آغاز خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76551" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rpEJRjny9t7I_OjViwapxrvcycmbqPe1Mz1PAhHeNiWw4UZIHoCcDsYynyfTjAyoSbRi-W4SNUmFMpS8GQTT0jqUKwTIRjK3D1YuAt5IFDL1acCU1kpcBrturpTPquafWAImqQocrJfrxegoMXD9mBTKsUlWejL7PpmpwPxUToY4_A7KtcZHYymAHnt89YfTuesEF4tKQEuhReF8nCF6-8xLQD2iM8Y6_aW4ZSUFVUTV1rPA9hj-qkG8gNtBTSMcK9ETZqjhQantsza83c4WXBcL6STdNV-g-qlMiyC99EhdexJezVM5DMajO6a-aPcvRGLkzMcYVaiYfrKWQfr2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی مرکزی ایالات متحده،
ترجمه ماشین:
عبور کشتی‌های تجاری از تنگه باز هرمز
تامپا، فلوریدا — تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت؛ همزمان نیروهای آمریکایی به عملیات خود در منطقه کلی ادامه دادند تا از آزادی کشتیرانی حمایت کنند.
امروز عبور امن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری از آن عبور کردند؛ کشتی‌هایی که حجم زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل کردند.
مرکز مشترک اطلاعات دریایی این هفته اطلاعیه‌ای صادر کرد و در آن عبور امن همه کشتی‌ها را در یک مسیر تعیین‌شده تأیید کرد؛ مسیری که از ادعاهای خودسرانه درباره الزامات یا هرگونه مانع، آزاد است. جزئیات مربوط به عبور امن را می‌توان در اینجا دید:
ukmto.org
نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اجرا و به‌طور کامل برقرار و لازم‌الاجرا باقی می‌ماند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76550" target="_blank">📅 18:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=GjIapsp_Mmh2RmN-14U5plF7fmGgLGHCaBxBGPPKtwPm8-yxno0b-xRVp9XstoqI0cHkYeQWFDqkLGwK9PN1PysEDwYpNq9Q6OAExfWyfAuPM5byWuzavR-ixPzPCm7GQ5q2g13I-5j9F8xeagZbSLrARm65OY8WBANQakH6Ek6IZslCQS_Jo-kkZYK8FUwU1M36-cV7dy8-B13PUv3WmD6MQ7HTCGZ8X_bmyfL5Y71MFjcljohSUlUwtiXdZ3PLiJ1ZBDoNlgo3IUu09oLcnmI4xIqYnki-p0r1LD5S39hLGCdOroD10ZNu0T7obWNEJJEAz-U-LssRVlQu-BzAhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=GjIapsp_Mmh2RmN-14U5plF7fmGgLGHCaBxBGPPKtwPm8-yxno0b-xRVp9XstoqI0cHkYeQWFDqkLGwK9PN1PysEDwYpNq9Q6OAExfWyfAuPM5byWuzavR-ixPzPCm7GQ5q2g13I-5j9F8xeagZbSLrARm65OY8WBANQakH6Ek6IZslCQS_Jo-kkZYK8FUwU1M36-cV7dy8-B13PUv3WmD6MQ7HTCGZ8X_bmyfL5Y71MFjcljohSUlUwtiXdZ3PLiJ1ZBDoNlgo3IUu09oLcnmI4xIqYnki-p0r1LD5S39hLGCdOroD10ZNu0T7obWNEJJEAz-U-LssRVlQu-BzAhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی پربازدید شده که مادر مانی صفرپور، جوان کشته‌شده در اعتراضات دی‌ماه، را در حال سوگواری برای فرزندش در کنار یک دستۀ عزاداری نشان می‌دهد.
عکس پسرش را بالای دست گرفته و می‌گوید «پسرم، پسرم».
مانی صفر‌پور، جوان ۱۸ سالۀ لاهیجانی، ۱۸ دی‌ماه ۱۴۰۴ با شلیک نیروهای حکومتی در محلۀ سلسبیل تهران کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76548" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76547">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pr69zsWU8sLubwUIG4bDsafbP9egml1yIcfKR94qVAShzomFUxhf7T69iX3GBWUVswm460mGP6C36bnJzqVmqaqXiPvz2U1oUzYvRBsfZvfft6P2X1_yQJ1ztBqrQo-X1kqzFGEN9qCdI3uZM0EY8_AyOyUFePqlLWKJ0S6OWpNcbO7GzApV7ZTPgQc28bURxUdMAjSrnlXPtKdz0vCNmo7u9HcZayotdneq8Fbz0YFYyC4EwcWPLxm1xjpaIXe0Hp9qB0udCtdgA1HY1MurwMaPSK3Cy9YT7pWXXDZoi-CmU5MHWsBLWc7GTvttGIoSU9nHBfE0RofvDnYrBK9-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد تنگه هرمز در واکنش به «نقض تعهدات امریکا در اجرای آتش‌بس» و «حملات اسرائیل در لبنان»، به روی همه شناورها بسته شد.
نیروی دریایی سپاه همچنین از شناورها خواست به تنگه هرمز نزدیک نشوند و هشدار داد در غیر این صورت، امنیت آن‌ها به خطر خواهد افتاد.
قرارگاه مرکزی خاتم‌الانبیا، واحدی از سپاه پاسداران هم اعلام کرد تنگه هرمز به‌دلیل «بدعهدی و پیمان‌شکنی» امریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه، به روی تردد کشتی‌ها بسته شده است.
قرارگاه مرکزی خاتم‌الانبیا روز شنبه اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.
خبرگزاری فارس، وابسته به سپاه پاسداران به نقل از یک منبع نظامی در نیروی دریایی سپاه، عصر شنبه اعلام کرد که تنگه هرمز از دقایقی پیش به‌طور کامل بسته شده است.
حملات اسرائیل به جنوب لبنان در روز شنبه دست‌کم ۱۰ کشته بر جا گذاشته است. اسرائیل اعلام کرد این حملات در واکنش به پرتاب گلوله‌هایی از سوی حزب‌الله، گروه مورد حمایت جمهوری اسلامی، انجام شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76547" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O96JxKT8-UH-b5ZtqJHE_UOO657XjjS70L0-V_L9djUAovcz_2rFSpXcJ2dpB93YrTOxg3o08KxtLv22gwsNx9pfcH7yF_fulrQ7i2SQyKxadtNime94c4W_MXJSYjZpk7Vv0Qy9wExUg8HCPEmI9R3FQk8LltBW5cAFRJ_rlSu1NjSasHHli3SIgKn_pS34kY32zNn_QcVpZaOkfVncd_vSb88KwQZatKpL24uQnYxn47Eruf1_eNxf19hEXBTBuK0OY0HXX0h7q0n9xR7ApTD4Ke0lRibmLNYnwZ98GwI7VT__JKXyeg5zXCeYskNm6KcohSj_A1foQ-0XyOuE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، روز شنبه ۳۰ خرداد در گفتگو با فاکس‌نیوز اعلام کرد که استیو ویتکاف، فرستاده ویژه ترامپ و جرد کوشنر، داماد او، «چند ساعتی است» که در سوئیس حضور دارند و مشغول بررسی «برخی از ابعاد فنی این مذاکرات» با ایران هستند. به گفته ونس، کوشنر و ویتکاف در گزارش‌های خود تاکید کرده‌اند که «امور به خوبی پیش می‌رود.»
ونس همچنین از احتمال ورود میانجی‌های قطری و پاکستانی به سوئیس برای پیوستن به این گفتگوها خبر داد و افزود: «قطری‌ها و پاکستانی‌ها می‌خواهند مطمئن شوند که ما این کار را به شیوه درست انجام می‌دهیم، بنابراین من تلاش می‌کنم به این روند احترام بگذارم.»
معاون ترامپ که سفر خود به سوئیس را در اواخر پنج‌شنبه شب به تعویق انداخته بود، بار دیگر تاکید کرد که انتظار دارد طی دو روز آینده عازم این کشور شود. او با این حال خاطرنشان کرد که هماهنگی‌های این سفر «همواره یک رقص هماهنگی ظریف دیپلماتیک است.» این مذاکرات که پیش‌تر قرار بود روز جمعه برگزار شود، پس از وقفه‌ای کوتاه دوباره در آستانه ازسرگیری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76546" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6zQVDdJmCrtq7nLQlKNdiZZWcAZjARgubegkYF1fC4YROM7XFTmCE2UcwnArmJHMgWnoqad1FK0d7S5huHAHDX9sURuN0T2zdNf7Y7l4ooIxmM91KlWpp5nT02huzHpW6K34Ibf7WGDad0xa6ympxy5LV6X8cyZEWmEbpGkh2XPjfN0vLEGpzAIAXmoTBK6vnFi8ampnWy916P56Hx8bgWbel6D_re_6dRiZgx90zZ3UqcGW0sew4hP2CuQcVfAw7x465eA5GlENA94TkS1Sk4MMgVgmZCHPT1Odopmb3Qc4p1vZIjgejIeqMALnemZYz8YeBWJ9YmjlcZn_-SsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«طاها نظری» معترض ۱۸ساله که پیشتر به‌دلیل حضور در اعتراضات ۱۸ و ۱۹دی۱۴۰۴ بازداشت شده بود، پس از  تشکیل جلسه رسیدگی به پرونده، به ۵سال حبس تعزیری محکوم شده است.
ماموران اطلاعات شاهرود، در فروردین ۱۴۰۵، طاها نظری را شناسایی و به صورت تلفنی احضار کردند. بعد از مراجعه به محل، این جوان ۱۸ساله به‌صورت موقت بازداشت و تحت فشار برای پذیرش اتهاماتی نظیر «ارتباط با تلویزیون‌های فارسی‌زبان و فیلم‌برداری از اعتراضات» به او نسبت داده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76545" target="_blank">📅 17:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T9Z7X009cy14Gaikl4BjWpvkfIr2zApZB1eabURFQZZsSM1vfm5qXpgUnZAH03plCm3bq6Dmh7lKUnfJy4YJIWsXX8Y0szuEE2KIht4GIyrlLmsAkz7lSAEm6idB2CW7mskAsgvAu00xoOSJZIu7ot2Y35hn3SVVz3I0oUYynQx0aQGEgxTpxQh0Cx5iu3cZI_MjcohiBhgJzZbH22rTGd_RTm7PKNC9Ew7KZv7umL-1fZOSGAEpu7tE4KoBRHqUmqzhx3gIy2aLGgKqcoFughHXALRcHAbb9t8hQDpT6tudqAP9XJlJ_zLFcBiVSWLcbbYuE_qyNWCW8GQoEcruFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vro0uSn8JZG8z2TIqo1wNJVT67i-tuVrqF-n0vIHXWc1tNJR_A5trU9bIgs6F_opMFHJ7FRG3WI1LrHcqDIjLAIoev2sgHlJq1xkdkaPKILhFA07CuC3sKCo89C3f5MjhfV2t_8OqmwTRO1rjRUnpVMn8lZuYX4HMRQz1g3w0MUl_z5nIr987rlMNVMAPzuv80afFXC9BVPH1qZXAXNORs8h8TTgY9gXjs1l5NpS5NMu76IPp8QVXcIDxxmTnpHmwvjv-U6PLShwoa9GwajhluEwfWAzFr2Qx18n2_1nTCChcH-UnHEGIt-Qwhnf0MgV1UNO8dij7LSer1nvKnkvOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت دلار و دیگر ارزهای خارجی که در پی نتیجه موقت مذاکرات ایران و آمریکا کاهش یافته بود بار دیگر افزایشی شد.
روز شنبه، ۳۰ خردادماه، قیمت دلار آمریکا در بازار به ۱۶۲ هزار و ۵۰۰ تومان رسید. قیمت یک یوروی اروپا نیز در این روز به ۱۸۶ هزار و ۴۰۰ تومان رسید.
این در حالی است که در طی روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسیده و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شده بود.
روزنامه هم‌میهن روز شنبه قیمت سکه امامی را در بازار طلای ایران ۱۶۹ میلیون تومان گزارش کرد.
از زمان اعلام تفاهم‌نامه ایران و آمریکا در تلاش برای پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران شاهد کاهش قابل توجهی بود.
@
VahidHeadline
حسین صمصامی، عضو کمیسیون اقتصادی مجلس شورای اسلامی، در گفت‌وگو با سایت خبری تابناک افشا کرد که در هفت سال گذشته بیش از ۱۳۰ میلیارد دلار ارز حاصل از صادرات به کشور بازنگشته است.
این در حالی است که حکومت برای بازگرداندن ۲۴ میلیارد دلار دارایی مسدودشده کشور وارد چانه‌زنی فراوان با دولت ایالات متحده شده است، امری که نشان می‌دهد تا چه حد به این پول نیاز دارد.
در این میان بیشترین میزان عدم بازگشت ارز صادرات مربوط به سال ۱۴۰۴ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76543" target="_blank">📅 17:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76541">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hc9jimrvZbf-9s7s2VLomMvdL9cBKL1A-f10QQ4nK8paoX9W9JWiNov0pLVfhtTPNC_BxNI7XPViSUMFqfzTkLliuoo3fgptK-T3liGf0cWXf1M_BgiFnh0H41indi1xV5935JvtbYhfppY0LzR41KviWx6vF3LESShHYiySUMutqA3hLdvFgSWy-1PEGgIMtK6Fev3lJ8LgEgMajlNt7qGkFRC-d2U05_WjWLDv1kUXPHeSLVSAKuhso0WCNaOfjeQeRTsMRLuLXhw7-1mjkZpxrLvkeZfFswDTfQsLpuPxQZ5m2OQnbyd13nEGP1O-4PDvayOUwvp7JBjIZfz8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=WBGhhZtak1tP2U0hBKAzniiOBEjb0baCEgC7EVHKM5s4PoN4Sci4nOOR8sy07xlx7vFJyXT4cF0Bmqs5P-RBS94XeRuVxfuS1fnXf-gJGZao2M6BO8EO2OiYaPK6-ZNLnxLFGeNCkounDEqHXsI7DaPQ-DHo1ZvEKJXj_sx4eODwUeYHEynuxr7Ok9g7SmwYefM0OlEaZ0Y7HgLnp0hwoPAuCuipNBLeu_ndntIPMVJsK4JK3Xoo2kkbPUFiNdsBuPzilKD_kK3VC4Wi1Z9qtiB4M2ZQHo8N-jA_2YwO3P5pTsJQc2FWlxyBI3fTWdhKqrpZOA8pXu7XDzEzCCEMUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=WBGhhZtak1tP2U0hBKAzniiOBEjb0baCEgC7EVHKM5s4PoN4Sci4nOOR8sy07xlx7vFJyXT4cF0Bmqs5P-RBS94XeRuVxfuS1fnXf-gJGZao2M6BO8EO2OiYaPK6-ZNLnxLFGeNCkounDEqHXsI7DaPQ-DHo1ZvEKJXj_sx4eODwUeYHEynuxr7Ok9g7SmwYefM0OlEaZ0Y7HgLnp0hwoPAuCuipNBLeu_ndntIPMVJsK4JK3Xoo2kkbPUFiNdsBuPzilKD_kK3VC4Wi1Z9qtiB4M2ZQHo8N-jA_2YwO3P5pTsJQc2FWlxyBI3fTWdhKqrpZOA8pXu7XDzEzCCEMUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که هاجر نادری، مادر متین پرویزی، در صفحۀ شخصی خود منتشر کرده است او را در کنار آرامگاه پسرش نشان می‌دهد که می‌گوید «من به پسرم فقط یاحسین و تشنگی را یاد ندادم، به او یاد دادم که جلوی حرف زور بایستد»
خانم نادری در ادامه با شرح کشته شدن فرزندش در اعتراضات ۱۸ دی‌ماه می‌گوید امسال محرم برای فرزندان میهن که «ناجوانمردانه کشته شدند» عزاداری خواهد کرد و ادامه می‌دهد که «می‌دانم امام حسین هم برای این جوانان عزاداری خواهد کرد»
متین پرویزی ۱۸ دی‌ماه سال گذشته در سبزه‌میدان زنجان با شلیک گلوله جنگی نیروهای حکومتی به سرش کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/76541" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eifQPGklTJ4V49JJD968wHM2iJv46Y91xtJbwMiP2etF-kD5O8tHMAIG4SWkgTxWuQbheOiX2OlkCJ_YVVRvXa4ECwA3gK4pN18VrCy4jYis6o8DsnU_sgUQmkccAwAEACfsXy854pIqPKABVQjCNvV1na-r38bKzJB0HVR0Ia9DsvnHxJrEUiWBEa7SXbApdM6PyNcuDbc09Y6fWE6LAUQmys4eXAC--YDhjTKyuJBvfAH0SA3spGCJByg3nhNjG89Uzn6zUuS9sbc92Cr70MvNKPC9BPPS7W3iETaxTrCaUdWMh1uLkpmeOyEXgWJFvI4b9Lya2kzf4CnuAmH8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، صبح امروز وارد مشهد شد.
ایرنا به نقل از منابع خبری در استانداری خراسان رضوی گفته است که او سپس برای گفتگو با مقامات عازم تهران خواهد شد.
بر اساس گزارش‌ها وزیر کشور پاکستان قرار است در این سفر در مورد از سرگیری مذاکرات مستقیم بین آمریکا و ایران در سوئیس، با مقامات ایران گفتگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76540" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76539">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQP-p_czrDBFqI8TZXo_BoanJK0XmRilO48CfY5kK6NhEQnFrGwDIqpT5SVAjeo7a4ulyB7y1qpdMZJwNP6cIPHWsr8eDSg26CsQ156j1QTLtjCVibkJ4WicHgLwGASgqDB8g52ylZcDnq_Y_I0QT5_ZolxbbIH2O_fT8a6D88rvmaUcUWAukgCJUlWVB39Hif53K3jKT4Aqn2L68ObV_UzWj77sxIxQ5fSUGoM8rBO39jTWS0_nZfFQARCJoiPyiVT9Hjf8pC6NhqFPZHZtlPco9cGjLMzWG_Tyyaeab4lgbTbbm2hL-wPeJGP-KiznNDA3-Tk8iTEhOGrXJsFpig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز اطلاع‌رسانی پلیس استان لرستان از پلمب یک واحد صنفی و معرفی فرد متخلف به مرجع قضایی خبر داده و اعلام کرده است این اقدام پس از آن صورت گرفته که به گفته این نهاد، واحد مذکور «ضمن عدم رعایت قوانین و مقررات، اقدام به هنجارشکنی» کرده بود.
این در حالی است که تنها سه روز پیش نیز مرکز اطلاع‌رسانی پلیس لرستان از پلمپ پنج کافه‌رستوران و سفره‌خانه سنتی در سطح استان خبر داده بود. در آن گزارش، دلیل برخورد با این اماکن، اجرای طرح موسوم به «ارتقای امنیت اخلاقی و اجتماعی» و آنچه «هنجارشکنی» عنوان شده، اعلام شده بود.
در هفته‌های اخیر و هم‌زمان با فروکش کردن فضای امنیتی ناشی از تنش‌های بیرونی، گزارش‌هایی از افزایش تمرکز نهادهای انتظامی و قضایی بر حوزه‌های مرتبط با سبک زندگی شهروندان منتشر شده است؛ روندی که به نظر می‌رسد بار دیگر کسب‌وکارهایی مانند کافه‌ها، رستوران‌ها، فضاهای موسیقی، پوشش و نوع تعاملات اجتماعی را هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/76539" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=R-iM-UqUBi3dnzqIoSvA0tRRZ988ZTbCy20-JxiSSnJjJXe4aVr1wAsW2_DQyWLQI1JUE7tCSANHc9B-j-IT_TGO2SOSsaNiV53pQsIpCQo1bNatMBIBNNDtXLd3t0ACLg0eg7kJbIIlUsro030GJbymvcD0HyCX0A_qy85N8U3VjxxfrFzK4EdCIdbETVai-wSb-I1fJdrFMA1wl3Rt3rFzGqhOumDCWWE8lbIshfn7YPnHz5MXNvqBjtYRtU9VOxKPM58PHC46grZlbucslNLockN3f0isTNOteamTt_cl9JUBrh_0zc12BG5P_YCnrrCm7gHzu_A_FiI7LAlAzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=R-iM-UqUBi3dnzqIoSvA0tRRZ988ZTbCy20-JxiSSnJjJXe4aVr1wAsW2_DQyWLQI1JUE7tCSANHc9B-j-IT_TGO2SOSsaNiV53pQsIpCQo1bNatMBIBNNDtXLd3t0ACLg0eg7kJbIIlUsro030GJbymvcD0HyCX0A_qy85N8U3VjxxfrFzK4EdCIdbETVai-wSb-I1fJdrFMA1wl3Rt3rFzGqhOumDCWWE8lbIshfn7YPnHz5MXNvqBjtYRtU9VOxKPM58PHC46grZlbucslNLockN3f0isTNOteamTt_cl9JUBrh_0zc12BG5P_YCnrrCm7gHzu_A_FiI7LAlAzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع‌های اعتراضی زنان به فعالیت‌های معدنی حوالی دو روستا در استان‌های کرمان و سیستان‌وبلوچستان با حضور نیروی انتظامی به خشونت کشیده شد.
بر اساس گزارش‌ها زنان روستای پشموکی از توابع فاریاب استان کرمان روز ۲۷ خرداد در ادامه اعتراضات مردمی نسبت به نحوه واگذاری و بهره‌برداری از معدن کرومیت پشموکی تجمع کرده بودند.
گفته شده که نیروی انتظامی علاوه بر ضرب‌وشتم معترضان، شماری از آن‌ها را بازداشت کرد.
هم‌چنین منابع بلوچ گزارش داده‌اند که زنان روستای سرسیاه از توابع تفتان استان سیستان‌وبلوچستان هم روز ۲۶ خرداد در اعتراض به گسترش فعالیت‌های معدن طلای تفتان و پیامدهای آن بر زندگی مردم منطقه تجمع کرده بودند.
در ویدئویی که منتشر شده شنیده می‌شود که مأموران نیروی انتظامی با خشونت، تهدید، توهین و واژه‌های تحقیرآمیز با این زنان برخورد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76537" target="_blank">📅 17:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lSgaiZpXAyFtJXEcYxhn4ijzRHUWatD9El2KwFCwK5bza5vsAzKb_HQpWBTfJBkfEDStG0SarchWqIv9MUFQHb9IL9Bo8bbGEZbdRH-adJlKk2gm_oy4gbOxVCLnI_e7GoLUyBL0OiBzNew0WwH7p250lMNkI_x3ThgrPpDd28qrbiIsLFea41SiYyH05T70IQHza71eE-erZFoeV0CqIpd5wIE_ajMVK5-zz3PZVAMIsWmYpVxHvUfZZ6n0ag_-55547p_2CegRMaotwK5cu3wXngp3qQXREEZnQ99wmcSaZiHJ294lovfmgXjMohY4mWnnCcmmTPtvJBuOT3uRSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kXJtoQQoyWqKTDdUupzK-GCSHE-lVptNxse7GI7gJzox-rphKl9s7u9yCB2SSi0YBApf-cDzelbHZ1yaMhv60XbR1m_6m_eqZQmza6RzPJInS-S_HMrIIufVqZiEHueoxHAnJZ6M5CR8kILtU05eJX-TM9YSVyi_soFspuI6wTR-jVw2IO6eXnh-E08IcSV3kAh0rIEXRFaOF64NEW34swUIQq6uEhEKmg0CVyPcjkDVS782WyWhTBwUYTIQBaHEWYbP_Ncrx2KLrVvFEOqjNDIrZ6DusGYrdGcxkTxtOzzOG-yCY5VqtP3ZXVfFt_bLb38IcnHHIKr6eaY4kocMhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: استیو ویتکاف، فرستاده کاخ سفید، در حال سفر به سوئیس است، جایی که انتظار می‌رود دور اول مذاکرات با ایران در مورد توافق هسته‌ای احتمالی برگزار شود.
به نوشته اکسیوس، قرار بود مذاکرات جمعه ۲۹ خرداد آغاز شود، اما به دلیل درگیری بین اسرائیل و حزب‌الله در لبنان به تعویق افتاد.
@
VahidOOnLine
خبرنگار اکسیوس به نقل از یک منبع آگاه، روز شنبه اعلام کرد: «عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، در حال برنامه‌ریزی برای سفر به سوئیس در روز شنبه است.هرچند این برنامه همچون گذشته ممکن است تغییر کند.»
این خبرنگار به نقل از منبعی در یکی از کشورهای میانجی فاش کرد که عراقچی روز جمعه به چند تن از همتایان خود گفته است: «موضوع آتش‌بس در لبنان برای ایران یک مسئله حیاتی است و حکم برد یا باخت (تعیین‌کننده سرنوشت) را برای مذاکرات ایران و آمریکا دارد.»
خبرنگار اکسیوس همچنین به نقل از یک منبع دوم از میان کشورهای واسط افزود: «ایرانی‌ها صراحتا تأکید کرده‌اند که می‌خواهند پیش از سفر به سوئیس، شاهد برقراری و تثبیت کامل آتش‌بس باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76535" target="_blank">📅 04:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=swrfmr0oCHBpotqoCPNs8aYy0k4fV02HAN-1d1saXebyBVJxvoilN_MmVCctsU8RwY1SIRnUVX9Kf_ZjKvHgyQkXnUdKf71EW5Vw1HJBxeLy5ZkDpEQWcxXzUQPEmY5yVgsNyMTcVmFSeu7D61or5lTwB97bgCwYTNH2uRqRvP5JcY-IkVamEFveHa0qyvZzQzMTuqzfkOSYskgwfrXLpYaQLYhmMJ-63S6_-I2-ISAtiIC1n7r_DAFnU1Dil-EKA8ZDtnVVM1DrGpjCa9D9h5XryA7l2pSKHtVybSqHJ9i3uugjDqFYNNU5-3ywkfAes3k7pHVwD943jirNL5eN4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=swrfmr0oCHBpotqoCPNs8aYy0k4fV02HAN-1d1saXebyBVJxvoilN_MmVCctsU8RwY1SIRnUVX9Kf_ZjKvHgyQkXnUdKf71EW5Vw1HJBxeLy5ZkDpEQWcxXzUQPEmY5yVgsNyMTcVmFSeu7D61or5lTwB97bgCwYTNH2uRqRvP5JcY-IkVamEFveHa0qyvZzQzMTuqzfkOSYskgwfrXLpYaQLYhmMJ-63S6_-I2-ISAtiIC1n7r_DAFnU1Dil-EKA8ZDtnVVM1DrGpjCa9D9h5XryA7l2pSKHtVybSqHJ9i3uugjDqFYNNU5-3ywkfAes3k7pHVwD943jirNL5eN4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بخش مربوط به ایران از مصاحبه امروز ترامپ
متن کامل این بخش‌ها:
https://telegra.ph/trump-06-19
بعضی از جملات همان متن:
ترامپ: و من آیت‌الله را کشتم. یک مقام سپاه هم بود. و متأسفانه به آیت‌الله دیگر هم آسیب جدی زدم. به شما بگویم، من او را ملاقات نکردم، با او صحبت نکردم، اما دیگران درباره‌اش حرف می‌زدند. او شجاعت خاصی دارد، چون به‌شدت آسیب دیده است.
با وجود همه این‌ها، نمی‌توانید بگویید بی‌خیال. من ارتششان را نابود کردم. نمی‌خواهم این را نادیده بگیرند.
برای کسانی که می‌گویند شاید من به‌اندازه کافی سخت نگرفتم، باید بگویم من ارتششان را نابود کردم. بزرگ‌ترین پلشان را زدم، چون دیر در جلسه حاضر شدند. گفتند این کار خیلی قشنگی نبود. من گفتم پل جورج واشنگتن؟ سه دقیقه‌ای نابودش کردم. خارک را زدم، همه چیز را، جز یک چیز. گفتم به لوله‌ها دست نزنید، چون نمی‌خواهم به اقتصاد جهان آسیب بزنم.
بنابراین فکر می‌کنم خیلی سخت گرفتیم. به کسانی گوش ندهید که می‌گویند می‌توانست سخت‌تر باشد. کل ارتششان از بین رفته است.
پرسشگر: چطور تغییر رژیم است وقتی هنوز خامنه‌ای جوان‌تر و خیلی از مقام‌های سپاه آنجا هستند؟
چون افراد متفاوتی هستند. خامنه‌ای جوان‌تر با پدرش فرق دارد. افرادی هستند که بسیار کمتر از دو گروه قبلی رادیکال‌اند؛ و من هر دو گروه قبلی را می‌شناختم.
اما به این فکر کنید: همه آن‌ها رفته‌اند. بعد می‌گویند چرا سخت‌تر نگرفتی؟ تنها راهی که می‌توانم سخت‌تر بگیرم این است که دو یا سه هفته دیگر وارد شوم و آن‌ها را شدیداً بمباران کنم. اما این چه چیزی برای ما به دست می‌آورد؟ تنگه هرمز باز نخواهد ماند. فرض کنید این کار را می‌کردم. فرض کنید تصمیم می‌گرفتم این کار را بکنم. الآن بازار سهام ما فوق‌العاده بالاست. قیمت نفت در حال سقوط است. قیمت نفت تقریباً همان جایی است که قبل از شروع کار من بود. تفاوت بزرگ این است که ایران هرگز سلاح هسته‌ای نخواهد داشت. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت، روشن است؟ خیلی واضح و ساده است.
آیا می‌دانید در دو ماه گذشته، من کشتی‌های زیادی را از آنجا خارج می‌کردم و کسی خبر نداشت؟ می‌دانید چرا خبر نداشتند؟ چون ما رادارشان را از کار انداختیم. همه تجهیزات دفاعی‌شان را زدیم. آن‌ها قادر به دیدن نبودند. هفته گذشته، یک شب ۲۵ کشتی داشتیم، یک شب ۲۲ کشتی، یک شب ۱۹ کشتی، یک شب ۲۱ کشتی. هر شب، همه این کشتی‌ها بیرون می‌رفتند.
ایرانی‌ها مردم بسیار باهوشی‌اند. نوعی نبوغ ابتدایی دارند، اما باهوش‌اند. منظورم این است که باید جلوی آن‌ها را می‌گرفتم، چون اگر سلاح هسته‌ای داشتند، از آن استفاده می‌کردند. می‌خواستید ببینید؟ بگذارید چند شهر را در جایی منفجر کنند؟ مثلاً اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت. چون من توافق باراک حسین اوباما، یعنی برجام را لغو کردم؛ توافقی که مسیری به سوی سلاح هسته‌ای بود. آن‌ها پنج سال پیش به آن رسیده بودند. به نظر من، در همان هفته اول از آن استفاده می‌کردند. اسرائیل دیگر با ما نبود. اگر من آن کار را نکرده بودم، اسرائیل سال‌ها پیش از بین رفته بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76534" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsDf3KAVY3XUM7ozIapvQNdicyBggVI8pO3rEg0J5mrSwWp-D-4SuMvoapz2N_JGqpbdY8vZM2ezwPEXmdMePicIiJtmrzC11fgvG_wNQIe7Jefdpi1GeAoXsRreI40KngDK0Wj59w7-5GUbMAB7NjC4SwmgBjhE6DzC2TlAeRaIBihjaz9sJU7VBKMT0Qo3ynL14lrDbqktpF3uZdVLsHxKz7F61-52bhvGcuGAdd3mxM1t5wIBs4surCCoCz8-xR1bG9dRqVmPuO9ri49dvn9-VzoAdpsT625S-tsHn5pvdnyr7R3b58su2umxArWbNUz1vbHPmvPR5VKwCbRbLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا، در مصاحبه‌ای با برنامه «آکسیوس شو» با دفاع از تصمیم خود برای شروع عملیات نظامی در ایران، مقام‌های جمهوری اسلامی را «بسیار باهوش» و «نابغه‌های بدوی» توصیف کرد و هشدار داد که آن‌ها در عین حال بسیار غیرقابل‌پیش‌بینی هستند.
ترامپ با اشاره به مداخله نظامی اخیر ایالات متحده گفت: «من مجبور به اقدام شدم تا جلوی آن‌ها را بگیرم؛ چون اگر سلاح هسته‌ای داشتند، حتما از آن استفاده می‌کردند و با منفجر کردن چند شهر، از جمله در اسرائیل، هرج‌ومرجی واقعی به راه می‌انداختند.»
او با تاکید بر اینکه اگر اقدام او در لغو برجام نبود، اسرائیل سال‌ها پیش نابود شده بود، توافق دوران اوباما را مسیری هموار برای دستیابی جمهوری اسلامی ایران به بمب اتم دانست. ترامپ همچنین با ابراز شگفتی از زمان‌بندی تقابل با ایران افزود: «چیزی که مرا غافلگیر کرد این بود که آن‌ها این‌قدر منتظر ماندند. آن‌ها صبر کردند تا من به قدرت بازگردم؛ البته این کارشان عمدی نبود. هیچ‌کس، حتی با وجود سلاح‌سازی ساختار حکومتی علیه من، فکر نمی‌کرد بازگردم، اما من با خروشی بزرگ‌تر از قبل بازگشتم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76533" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76525">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشجویان متحد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lost6xdtlEk3Wz3fGs3iKpJVAe9_pqo5v9_cMnWx_Yegak_q0L4VRIgg3-jCTU3bWRcLdjSvbPOoXiIkoX3umtO81SSdAIx2vKj_K2iYukbV0KgPXLI_vcnBw_p9kX81EvTvoslOYTkPHNtuYMFGMVyFl4RQhZOEo1pnHp-4evhqDZHEWIpAvHANTqHgLbERm6GRtBhQw8LUMP3ajYNYFCzM0ez4w4_5UrKJVl9CBScbP262DIfPiJQkqZqoG8EC1SwxhEevOEUG8xSI4WsHrA3V2VCYIsho5YQm4QWPnatXOt5pAtxJE_H2yoimL_lsJcIQnq0sjLM7qQ7usHbXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CA0bOyDnuCVsUe8JNwWVpUsExuAV8I3h_tk806qS_cQD4LB2OhFCNq__cAoCMbEmn2eDPxUC1VzbLA4iBLzhwVZRZ5H5hzJrQ2AWG7yDKJ31H4vO9iawhIkQhUPf084oKXkaEAPuIiJUT1dOsq6c_0uyTttUDbRLDFT4_069cfamcWINRJ8M75pbbp966f_RtSwvAblPlYRpqp6dbFi8HSVb-euHhIc1O-shQnsu41XWvVRxzjOKVc_79P7dKkon3SSKrnyl9YHC6OPmLi_9s3WrupUubTC1uc6K3siEAdu8yPRUJWLrQQTtBXzzWO8I8STnzBrSlEaGQ0ubWg2Qhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyhpO1YMghv9uo6zXHgQbcmoTu6aTa1zJo8x3oHhXZZo8OT15DIpDvnlwiVEK0h_HLu_pKuIM283Omz-GIVY3_j5zVZ6a_h-DNwBkJFxOicI2jxLbli3rabG0UxrLu__3-KkrSzPAdt3uoUPsOAAZ8NFghyDQO1mS_Io9tosT7_czdfH8Cx4MFN2WLZokKM5GfqmIU49A2Ua9KeMSjLGXMQtraSjXIMmWriq3XFwpHeHJOHx_Q8N5ifwMyB3E_RRZ-ajgq6vq0hTjMD18dWSXyznB1d9veca9Fne1MXLbiFogyOBuespLv8mNo9kYYX6XNC1P63DJNOgN4RowzjmWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_ll9a7i1i50yoVk4flVHXO3MRiAFsRUhoSZbMFcDwbbdzI5SsiGQ03H-_pCSaL72q2Ljb8Qwp6Zt6fM7thtyJ4hqG-WmLiIsV_6Ft8N3_76QPFK9uP1TGwAWrCHAUZ4HNg5oEWjC1CQWSIMvK38gmR82ZDraIcAAV2mE5OMxYG-40XzPuV6xNiQkqiSq5A3EpsUjmcT8hk3eazMLNqvneA_0dPIvWxORUK6MPRXra2JXR8rZB44YZ8S7XNO1kCkyuk89dZBFyg6k1tIpm4SXuS9SqbMYZzk727d_guud8dVkh_PpSQCYWs1l_Hja9_rtUGFIg5VV_vmm14XVIuHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHW8x8EmPGwrwVjVmtaz5IiLrDyag3GMA67J0_Qd-Rjqh63m3C1CduqWugihCxS9LGjUF1VpGMXQI16OClM_5rKbpKrJe4LI_ahSKudIKwUYdD5knlP7gocvXz4dNo6BQVX55MSVpyCJb-Zo7zpoX_NIC1J0Gftb-jZj0cJPRNa8yZD-nLRJxZlxoHIREPdP-6EG_mo0Yqb2UsQYnp-aSBNFrG-kwsLCBc2Riun4fU7YS2YYFbiCWQvRCrg5zg3Ex_zjRa2z0xA3THendRNDia_gq7_W2sAaIEJPR8S52PryN8fHy5UTQNjFLIxT0BUaikuvdKAlOCn3sJ5mbFzxwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZuDez90CwSz7p1w3VY6gGDVLkbIOATizvLidcxKzlmvRMa76tbK8DdbO9U3gECTL-IQHI2TzkA7JcTyS0D_lFnFMu0Q_co8PivVfDtyD4pwB2cpza-JCOX14ipkyD3FpCPnZQldB5q1MIXplHokEMgq96N6tUyuB88Oz36oz653eLHNaeustHzLG3jcxycQ3ZfJ_VhQv8AO2PzvXkdsqmSeenFw0PVnm7tjNg_P0dUNU0S8UR-iyATdT4tUOnltxp6WoeYFDmZJKkHG4eQK6Xdh_bVvsV69yRJM1EffUDEmE-CfNF_PbRVzbtw-hoi_6Xbzmq8dlUti9ZJnQBTvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtnUx8Td6023Z-zMPxVGHDj3APocXLWe_qv8YKBVGqgpIxaxhvwmEG7aX5-nViC_3kD3T_4LtrpjLmV8T00E5yvmQyKeF6Z7SLr04Dq6yEvGk-EBsNA17kwuSLvJ1V21I-vZ24GlXwjnHRS6VKAXP_RpdShA-kJB1yM5AU6BB6TKttPF3AMloq4uw41viyWBqlVcp0zKqX4CbbOMnCBG8HicyvxNTs-5qlDkcOEzI_Qk_BCiT6xdfoazVHSRP4C3ADPKXCnKjPy2gTrKc5rGXHW5msutd3mDDIVDJuNxSD2yWVO2C_0Uavuveunqd-UlgdSBsr96X16Bd31p-KbCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0Jwn7TzKtCrYVsQf7rvLEwRve5P7KOdbfG8FN13D96xUG5bEnKdpRW3aNOaSyafRo8RdSVRv5lsy-E41w8KNkX29E2Qa3C196lwNkqymvNe0JhfesBUhfoD273OcBGEnEBb8gA1VVZ0hrbzhFiZZzsZdc4VfEuOfFlg-07q5vqinaip6hOyRJ3Z7n7qJhvgKibpn5GIxjEmWjD6M9BjJjiEW8Imyh98egjNBGvTbW99VVHgp35WwZhOCovd3YcqmP39Iz3gpzpEdAby9uWctu-p5gFRcuSr4l5BqePUEd33-i5eWIJEnBU9ucTkQUcvkQSJ7ODt8qADno1vn0XDig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
صدور حکم اخراج برای هفت دانشجوی دانشگاه شریف؛ صدور حکم غیابی برای یکی از دانشجویان بازداشتی؟
🔻
بر اساس گزارش‌های رسیده به دانشجویان متحد، کمیته انضباطی دانشگاه شریف، برای هفت دانشجوی این دانشگاه حکم بدوی اخراج صادر شده است. اسامی دانشجویان به شرح زیر است:
🔻
رضا دالمن، ورودی کارشناسی ارشد ۱۴۰۳ مهندسی کامپیوتر: اخراج و چهار سال محرومیت از تحصیل
🔻
فاطمه خاکپور، ورودی کارشناسی ۱۴۰۳ شیمی: اخراج
🔻
حسین شادمان، ورودی کارشناسی ارشد ۱۴۰۴ مهندسی صنایع: اخراج
🔻
سپنتا سعیدی، ورودی کارشناسی ۱۴۰۴ مهندسی کامپیوتر: اخراج و پنج سال محرومیت از تحصیل
🔻
مسیحا باقری، ورودی کارشناسی ۱۴۰۲ مهندسی کامپیوتر: اخراج
🔻
فریبرز کهن‌زاد، ورودی کارشناسی ۱۴۰۰ مهندسی برق(تغییر رشته به مهندسی صنایع): اخراج و پنج سال محرومیت از تحصیل
🔻
پرنیان خدابخشی، ورودی کارشناسی ۱۴۰۲ مهندسی و علم مواد: اخراج و پنج سال محرومیت از تحصیل
🔻
همچنین در برخی رسانه‌ها خبر صدور حکم اخراج برای «آریانا کوچکی»، ورودی کارشناسی ۱۴۰۰ مهندسی صنایع، نیز منتشر شده است. هر چند بر اساس گزارش‌هایی که به دست ما رسیده، ایشان در حال حاضر بازداشت هستند و خبری در مورد برگزاری کمیته بدوی ایشان نداریم. هر چند صدور حکم غیابی برای دانشجویان بازداشتی در جمهوری اسلامی، پدیده تازه‌ای نیست.
🔻
لازم به ذکر است از میان هفت نفر یاد شده، کمیته سه تن(سپنتا سعیدی، حسین شادمان، مسیحا باقری) با محوریت فعالیت در شبکه‌های اجتماعی و کمیته چهار تن دیگر با محوریت اعتراضات اسفندماه برگزار شده است.
ارتباط با ما:
@Public_anjmotahed
🆔
@anjmotahed</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76525" target="_blank">📅 22:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=uGB9J7LVNoTUXN3YFlp6rn5j9AtNUPfy_qmT4nbHEq9H2e-8Sr-izhr3Y7yOe2zCJuzYLcnDW3CQXshSsFlVYC0wQ-V_72RiG4mTn_LEeihJ73p4_kGBra8aDfO6CnhtQOsCmMTtLPjJFCAtKBxSXMIQhHE-F1kjWZXVYme8RXA2KMZr263dSFLPO56HIy7rdtEhBElF3VKR4-jcvsJMWiF6VFwUC1ns_e6NJkogNiYFBihQGqNwhXZWkmxOjG0ZT7qAca2pabWwi5Smk93UmxoxwgjQlOu1gtqgR4Qg2OocZf0XMQWievnX3MItX-P_JxBZnmlW1ZQvJOXhmId67g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=uGB9J7LVNoTUXN3YFlp6rn5j9AtNUPfy_qmT4nbHEq9H2e-8Sr-izhr3Y7yOe2zCJuzYLcnDW3CQXshSsFlVYC0wQ-V_72RiG4mTn_LEeihJ73p4_kGBra8aDfO6CnhtQOsCmMTtLPjJFCAtKBxSXMIQhHE-F1kjWZXVYme8RXA2KMZr263dSFLPO56HIy7rdtEhBElF3VKR4-jcvsJMWiF6VFwUC1ns_e6NJkogNiYFBihQGqNwhXZWkmxOjG0ZT7qAca2pabWwi5Smk93UmxoxwgjQlOu1gtqgR4Qg2OocZf0XMQWievnX3MItX-P_JxBZnmlW1ZQvJOXhmId67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه جی‌دی ونس با زیرنویس فارسی
گفت‌وگو با:
الی بث استاکی، مجری و مفسر محافظه‌کار مسیحی آمریکایی، میزبان پادکست Relatable در شبکه BlazeTV
برنامه‌ای که در آن از زاویه‌ای مذهبی و راست‌گرایانه به سیاست، فرهنگ، خانواده و مسائل اجتماعی آمریکا می‌پردازد.
او در میان مخاطبان اوانجلیکال و محافظه‌کار آمریکا چهره‌ای شناخته‌شده است و در این گفت‌وگو با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره ایمان، خانواده، سیاست داخلی، اسرائیل و توافق با ایران صحبت می‌کند.
یک ساعت درباره مسیحی زندگی کردن
حرف زدند
و ده دقیقه درباره نقش و نفوذ اسرائیل در سیاست آمریکا و توافق با ایران برای مخاطبی از اون نوع
اینجوری می‌پرسه: می‌خواهید یک مادر معمولی چه بداند؟
متن این دقایق:
https://telegra.ph/JDVance-06-19
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76524" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76523">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvpCUqIxfClUPgj1Vj4HxnZ5VMZ9qWMZppwsizX113JE2FFlQYxPd_4SPwNukGkEfym1KtEwnybLE61Ebr-ki7R9aCf_6cqstJ7BbcWKlCPTFB4GwAjFezoKrMFxQv1Z4HYefH9moL9z2AOZvZZA1dy3ArMH7H46Fx44r2R5Y21kq8TM5qTsdtynTCHQ2axGUyoCO4E1KOPrEm2vZYnMTYS3jJLytY4JIFgh9buIcIZ8ROUrjbis9HeArBY9mIs6AN2hTD93iMXKsu_Z64RCfiQz9The_bcUEsj82MKDh0SezhIzSgafKo1dKczGHw8nNmAt_YJThVtcVNz0l3ZHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در یک گفت‌وگوی تلفنی با شبکه ان‌بی‌سی نیوز گفت که روز جمعه با مقام‌های اسرائیلی صحبت کرده و از آن‌ها خواسته است با گروه حزب‌الله بر سر آتش‌بس توافق کنند.
بر اساس مطلبی که خبرنگار این شبکه در شبکه ایکس منتشر کرد، ترامپ به این مقام‌ها گفته است: «بعضی وقت‌ها فقط باید آرام بگیرید و از عقلتان استفاده کنید.»
این خبرنگار همچنین افزود که ترامپ مشخص نکرد آیا مستقیماً با ‌بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفت‌وگو کرده است یا خیر.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76523" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gNl71MTAyes81RZzZZhIZyk-NysvQQNG5xUTC1UmDo_h6tGFco2Re_QwQbUrwozOW7eAZ18YapzEsPU7QEGenwFXneXNwSzESLOuYMwms4y3ENmcxJVmtMUcBV6p1E1D3tHC11_oXx4VrqUEgvzuR_2rMilAOklvA4dprs3uimqVMU24EfUAxrqCyPlTv0Z1cP1HdbR5Sj0U50JockP_onCtjB32BAwJLaYWSCVDO3rr1YTp5lfvEI62uqw7ynqIrx1j_Hbgq6VHsJ25dZfGWH6uN-8Y4gczd_1dlUIKAVwqd5qXtzAf313Cx2GVc1bGKItzMfxDpxMG5CQ8fd7tMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
او تحویل سلاح‌های حزب‌الله را رد کرد و افزود این سلاح‌ها برای مقابله با اسرائیل هستند.
نعیم قاسم همچنین گفت که ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
دبیرکل حزب‌الله لبنان ادامه داد: «ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76522" target="_blank">📅 20:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76521">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_vo8nr1Xp6RFdPX5YbMW0VQ0RfuViXa7nelefEimIEQD-EC293ZC1Lv5doUyHa1iPt5gcaifON-hEr4rJ8bp8haz_cKs405JpGUBIhZdBYA5-oxi0BcC_ctr-usbnCMmhMsreoYZV-qnYhv2VSsl1kZYhXqDx_xun3N0VPYQY2d8AO-RBuNuIBXjx_TfobHl5y2pjOy1mC-9arF4iYuNa3sgiPpCYekd8Nnw8mohGR9oQ1wxT4vu9Pz0vHdJSbCWhdCfUhtYkI6u_7nBag1Ex4QxVu2rnXlX4N2x71NNZGkJ0WIDfeJBd5UfUEpCA0BhZeOnFLvT0ykba4RD8vbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه ایران، روز جمعه دعوت جمهوری اسلامی از بازرسان آژانس بین‌المللی انرژی اتمی برای حضور در ایران و انجام بازرسی از تاسیسات هسته‌ای را رد کرد.
او گفت: «بازرسی از تاسیساتی که دسترسی آژانس به آنها به‌دلیل حملات نظامی متوقف گردید، منوط به روند مذاکرات و نتیجه آن خواهد بود.»
پیشتر جی‌دی ونس، معاون رئیس جمهور آمریکا پس از اعلام توافق اخیر در گفت‌وگو با شبکه ان‌بی‌سی گفته بود که بر اساس تفاهم‌نامه میان واشینگتن و تهران، بازرسان آژانس بین‌المللی انرژی اتمی «قطعاً» به ایران بازخواهند گشت.
اسماعیل بقائی همچنین گفت در حال برنامه‌ریزی برای برگزاری یک نشست طی روزهای آینده هستیم.
نشست بین نمایندگان ایران و ایالات متحده که قرار بود جمعه در سوئیس برگزار شود، لغو شد.
سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد: «با توجه به اینکه امضای متن یادداشت تفاهم در بامداد ۲۸ خرداد به صورت دیجیتالی انجام شد، برگزاری نشست مزبور در سوئیس فوریت ندارد.»
او همچنین گزارش‌ها درباره بسته شدن تنگه هرمز را «بی‌اساس» دانست و گفت کشتیرانی در این مسیر در حال انجام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76521" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76520">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7LTIj4RMTMCkLuZ6QubEsjM36jMreC_6c1UxevQOa71HhgGsrZTg_PK7yqJwyL1-tI1qjz8HnJMdx1o4I9jINdQQ_dV116oiv2KiRvTpAIPe32M41SuZIhI8p6TD6NNUO_umu6l9uhugxHqU3ArglWDR8ZiaeQSYuQeRWXketR0sKcJ_5FpcgXPH6YqC4t5GlaQVUOXheNGvyNpKR9fkv_ZFbMXo7iCG37Ov4Pg3qxNuk8c9ovJ9NZb9tozjEFKSYHuGvvoE0mi2kfIbAGcbqxBDrI7m_cQ9Z4GtdwGpxkKSnn3Biln_RV556LBm4_bp4BSEcrDvYawcndVX_z_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز گفت که اسرائیل و حزب‌الله بر سر یک آتش‌بس توافق کرده‌اند که قرار است از ساعت چهار بعدازظهر روز جمعه به وقت محلی آغاز شود.
این مقام که نخواست نامش فاش شود، افزود که مذاکره‌کنندگان آمریکایی و قطری با کمک ایران این توافق را نهایی کرده‌اند.
این مقام همچنین گفت: «درک ما این است که پس از تبادل آتش امروز، اسرائیل و حزب‌الله اکنون در وضعیت آتش‌بس قرار دارند.»
شبکه العربیه نیز به نقل از یک مقام آمریکایی از توافق برای برقراری آتش‌بس بین اسرائیل و حزب‌الله از جمعه خبر داد.
این در حالی است که نخست‌وزیر اسرائیل ساعتی پیش اعلام کرد نیروهای نظامی این کشور تا هر زمان که لازم باشد، در خاک لبنان باقی می‌مانند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76520" target="_blank">📅 17:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i2q1xh8VKPoqTmfpIIwTuhVYGQTzkkXtuz6N8M8UOsavZ0f3nAuRjcbtoIec08Qo3JbBBv6s0IJuorD2A14HA3nr3CKcDaIHaOETRsscxpxEHLNiE63ARCUGWBZScb1u3smnoQMVwiX_eLLLea-toUP3x8TUWhaTBLt1eyI3Cj9d9Px7n0RGwFRuJCAed3oRiK1823RUlT9jBGv5fFvj6zUD83xdPAvnc5jjnKwx7tNQUMQmKr7nCeiygaeT_LMOu-v_7Qiao8dv6NyPtx3mepWvBLt6_YaHUn0wL29ue5Sv3-xWfHiYSXAhbrFbjNTvb97tWzRGDyeX__ojOUGPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957528437f.mp4?token=F48A9DAhwXpPTKmU6xZxdzm-8LPSlI-8VQE4cIOtIa-lTwVaPqWlN4tcKPbJT35GpEuq6ZTZHoBu4RUOFOhmSCQXQX3dB6Eym-Hper5tSYfCwrKGRau5yNpz7J_ypnl4uH1M8rGxQ7lL9hSiSLFkUEh2Rh3bkCn2kzLUWPsrNvlYiU-JnW79BVfZAZn8L9vmZJPnkgJk5cUetmNfGoc7U7Fu_ZX0RXSGe_uxW01iyYfKjlIHQpDzmn-8TZ0_cu0-csN2Th1rQAzt-JcZKSBhrAV7HImJYeYGYjmaRNcmnz0jpXCvwuXJ-_8snhlToJD8_LVPGVrw_yI9QIbAbe9wpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957528437f.mp4?token=F48A9DAhwXpPTKmU6xZxdzm-8LPSlI-8VQE4cIOtIa-lTwVaPqWlN4tcKPbJT35GpEuq6ZTZHoBu4RUOFOhmSCQXQX3dB6Eym-Hper5tSYfCwrKGRau5yNpz7J_ypnl4uH1M8rGxQ7lL9hSiSLFkUEh2Rh3bkCn2kzLUWPsrNvlYiU-JnW79BVfZAZn8L9vmZJPnkgJk5cUetmNfGoc7U7Fu_ZX0RXSGe_uxW01iyYfKjlIHQpDzmn-8TZ0_cu0-csN2Th1rQAzt-JcZKSBhrAV7HImJYeYGYjmaRNcmnz0jpXCvwuXJ-_8snhlToJD8_LVPGVrw_yI9QIbAbe9wpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه ایتالیا روز جمعه اعلام کرد در واکنش به گزارش‌ها درباره اظهارات دونالد ترامپ سفر برنامه‌ریزی‌شده خود به ایالات متحده را لغو می‌کند.
آنتونیو تایانی در شبکه اکس نوشت: «سخنان شدیدا توهین‌آمیز رئیس‌جمهوری ترامپ… به همه مردم ایتالیا اهانت می‌کند.»
به گزارش شبکه ایتالیایی «لا۷» ترامپ درباره دیدار خود با ملونی در نشست گروه هفت گفته بود: «ملونی آن‌قدر می‌خواست با من عکس بگیرد که فقط از روی دلسوزی با او موافقت کردم.»
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، در واکنش به اظهارات اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا، این سخنان را «کاملاً ساختگی» خواند و گفت از نحوه رفتار او با متحدان «مبهوت و شگفت‌زده» شده است.
او تاکید کرد: «نمی‌دانم چرا رئیس‌جمهور ایالات متحده این‌گونه با متحدان خود رفتار می‌کند» و افزود این نخستین‌بار نیست که چنین مواضعی از سوی ترامپ مطرح می‌شود.
ملونی همچنین این رویکرد را «مایه تاسف» دانست و گفت او قاطعیتی را که در برابر دشمنان غرب نشان نمی‌دهد، در قبال برخی رهبران متحد خود به کار می‌گیرد.
نخست‌وزیر ایتالیا در پایان تأکید کرد: «یک چیز را باید به خاطر بسپارد؛ من و ایتالیا هرگز التماس نمی‌کنیم.»
در ادامه این تنش‌ها، آنتونیو تایانی، وزیر امور خارجه ایتالیا، نیز اعلام کرد سفر برنامه‌ریزی‌شده خود به آمریکا را لغو کرده و این اظهارات را «توهین به مردم ایتالیا» خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76518" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5x9_h2lka6jMX38FQcAWiqJ-c6W8kUvywK9MfZ9iQ9RK9D-4S8Go5_2X9R0narm72EGLxqd9sbuMztS2RehgkEzdIKUIT-S4beKfaq-xfvFqpmG4HJBkP7uWLDNsX5XzdoEmch4nDhWAsuOQ5B8agW_nofSMBg5EbTldjPNF_03q_lTF9WXSu2M6qt52zgJTQO1nUxH7KVUrsS12SZwBh8j8KzyoIQtCwCOVhRXXx3Cad26TZOrPU8tgA5fhB5MO9liMAgJtZCPnUbdHJxQvFvGwFZ6ocLNmspwsJ4SpPQZk-WmPce2kmdtT02Nj0O1W1wBCD0W1m8sbuMnmY2C4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅️
#محمد_نوروزی
، شهروند افغانستانی ساکن ایران، که در روز ۲۵ دی‌ماه ۱۴۰۴، در منزل مسکونی‌اش دستگیر شده بود، توسط دادگاه به شش‌سال زندان محکوم شد.
🔹️
طبق گزارش رسیده به کمیته پیگیری، محمد نوروزی پس از بازداشت به آگاهی ملارد منتقل شده و پس از ۴ روز همراه با ضرب‌وشتم فیزیکی به زندان قزلحصار منتقل شد. او طی این مدت مدام تهدید می‌شد که رد مرز شده و از ایران اخراج خواهد شد.
🔹️
او در نهایت با قرار وثیقه یک میلیارد تومانی از زندان آزاد شد و سپس توسط دادگاه به اتهام "اجتماع و تبانی و تبلیغ علیه نظام" به شش سال زندان محکوم شد.
این حکم هم‌اکنون در مرحله تجدیدنظر قرار دارد.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76517" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bklq9vFc4ELLbDcnVLsYtqFeAujYiH7lBx0xRLu3KyhBnNP39e1iRPxWlmEytkbwR0mcdbc622QjARLk5BQ-xn2Rij9vdkX8joySNsSnTt9L8wDLJq83qAOK1_JFx1qNyTCaa_o3hXS_iFxc2YQIf0J1N7l8sDgEV_NckDjp7tjk64QgN8pCJLXVzdp9rjvunQn2-ZsUtXBeE7dgMuJ6bpD9rryjPPLJpfvHAr6JtLz1LYZS1IYvqvimWYFVK-64axyMkLvRreiZuGNc3U1uHq3dTRh9czsPVQ7zx3rY5r2XC7944CSESBXhyY2AUusDbdV7UZxQbj1M5feug25G6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز جمعه بار دیگر گفت که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در لبنان باقی خواهند ماند و وعده داد که حزب‌اللهِ مورد حمایت ایران برای حملاتش «بهای بسیار سنگینی» خواهد پرداخت.
او روز پنجشنبه، ساعاتی بعد از امضای تفاهم‌نامه پایان دادن به جنگ توسط ایران و آمریکا، نیز بر ادامه حضور ارتش اسرائیل در مناطقی از جنوب لبنان تأکید کرده بود.
نتانیاهو در بیانیه روز جمعه که پس از اعلام کشته شدن چهار سرباز اسرائیلی در لبنان از سوی ارتش منتشر شد، گفت: «اسرائیل حمله به سربازان یا قلمرو خود را تحمل نخواهد کرد و بابت این حملات بهای بسیار سنگینی از حزب‌الله خواهد گرفت.»
او افزود: «اسرائیل تا هر زمان که برای حفاظت از جوامع شمالی لازم باشد، در منطقه امنیتی جنوب لبنان باقی خواهد ماند.»
یسرائیل کاتز، وزیر دفاع، نیز گفته بود که ارتش در لبنان خواهد ماند و افزود که به هر حمله‌ای «با نیروی قابل توجه» پاسخ خواهد داد.
لبنان اعلام کرده بر اثر حملات اسرائیل در سراسر این کشور ۱۸ نفر کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/76516" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76515">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sd2bqRMDojTy_VzcK5y4QS800NuDuqi-97-i6_UG7JFd90sMSJYRK1O6BCGjek4LI1npkSK9XUYJrKFWsU-_8RBT9x0CCTVnowyI5uyU6mSixzHc0kmYxmflpaSG2dC9JxcPPJFYR8ILMkIWsVUlopigwRqujgoe9y8go2EEUzFZnQXgDQqJIRvRiJebWXwiGMZ76rniiAJRpRxZV9mfQYP-o_iJYUo4IbgaIFnEGfO3ELgV0cMOkI_yjynZqIaleNRRAqxKXE8bxW4IFKhGMdWfgSET52GbCONJ7EbiOjPU3QEB0kDxqGcGmaAUwgSgrPOBRYNZbUMvAuInvW3dsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینعلی شهریاری، رییس کمیسیون بهداشت و درمان مجلس جمهوری اسلامی، در گفت‌وگو با دیده‌بان ایران، با اشاره به ادامه «تعطیلی مجلس» گفت: «مجلس را بستند تا هر آنچه خواستند امضا کنند.»
او با تاکید بر اینکه تفاهم‌نامه با آمریکا در نهایت باید به تصویب مجلس برسد، افزود: گذشت آن زمان که برجام را در ۲۰ دقیقه در مجلس تصویب کردند. ما یک بار از این موضوع آسیب دیده‌ایم و نباید دوباره همان اتفاق تکرار شود.
شهریاری همچنین از اظهارات عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره احتمال رقیق‌سازی اورانیوم غنی‌شده انتقاد کرد و گفت موضوع هسته‌ای نباید در مذاکرات مطرح شود، زیرا به گفته او «جزو خطوط قرمز» جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/76515" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EXxTfcxg0XdO4_ycK_Sx_xpHnrzt4HGm1QvqX2iBffPZyMnpxPC5okHf6HDIjWqqNAqrhaeeulBzYmJU0s3cfPxvZ27wD7oZm3QmLOg0CFNw89HoKffn4mD6bdXGCsqr7UjDKo0OhFpG8kn1-4qaI4gK2MU04hxH-co2FO6AFrPOHkvJfswTVkiRuhRlM51WNwNDlTya5bmuQI9w1rAQwZZ8oJN-yMQA3NJNQJ2dckVVcgceXojF4m53Nfdw_XTcJL_bzANHSVA_zszGUrUJJ9oveO3F7RR3vOYR1LvcMR6xxmWCkhuVwMF0hoUfTHTyqu-aSRDFcTRkah09yOHZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام پیشین مرتبط با تحریم های ایران درباره «صندوق ۳۰۰ میلیارد دلاری»: پیش نیازش لغو همه تحریم هاست که دکمه روشن و خاموش ندارد
میعاد ملکی، مدیر پیشین «دفتر هدف‌گذاری تحریم‌های خزانه‌داری آمریکا» در یادداشتی درباره موضوع «صندوق ۳۰۰ میلیارد دلاری» برای ایران که بسیاری از کارشناسان درباره آن ابراز تردید کرده‌اند، می‌نویسد: با کنار گذاشتن موضوع معافیت/مجوز نفتی و نگرانی‌های مربوط به عدم اعمال تحریم‌های جدید، باتوجه به الزامات برای اجرای واقعی بند ۶ (صندوق بازسازی ۳۰۰ میلیارد دلاری) و بند ۷ (لغو همه تحریم‌ها) به این نتیجه می‌رسیم که مذاکره‌کنندگان آمریکایی یا می‌دانستند که توافق نهایی ناممکن است، یا این یادداشت تفاهم فقط تصمیم‌گیری را به آینده موکول می‌کند.
ملکی که خود در طراحی تحریم‌ها علیه حکومت ایران نقش داشته در این یادداشت می‌نویسد: این چیزی است که «اجرای کامل» در عمل، فراتر از امتیازهای هسته‌ای، به آن نیاز دارد:
بند ۶ — صندوق ۳۰۰ میلیارد دلاری:
صدور معافیت ریاست‌جمهوری از تحریم‌های الزامی بخش ساخت‌وساز ایران طبق ماده ۱۲۴۵ قانون IFCA (معافیت‌های ۱۸۰ روزه قابل تمدید که در هر دوره نیازمند اطلاع‌رسانی به کنگره هستند).
خارج کردن سپاه از فهرست سازمان‌های تروریستی خارجی (FTO)، زیرا در غیر این صورت سرمایه‌گذاران با خطر مسئولیت کیفری به دلیل «حمایت مادی» مواجه خواهند بود و هیچ مجوزی این مشکل را برطرف نمی‌کند.
استفاده از معافیت مبتنی بر منافع ملی در قانون ISA (قانون تحریم های ایران) برای سرمایه‌گذاری در بخش انرژی و نفت.
در نتیجه، هیچ نهاد سرمایه‌گذاری حاضر نیست میلیاردها دلار سرمایه را بر پایه معافیت‌های شش‌ماهه قابل تمدید متعهد کند.
بند ۷ — لغو همه تحریم‌ها:
ماده ۱۰۴ قانون CISADA (قانون جامع تحریم‌ها، پاسخگویی و واگذاری سرمایه‌گذاری‌های مرتبط با ایران) رئیس‌جمهور اختیار معافیت ندارد؛ تحریم‌ها الزامی هستند و لغو آن‌ها مستلزم تصویب قانون جدید در کنگره است.
ماده ۱۲۴۵ قانون NDAA (قانون مجوز دفاع ملی آمریکا) معافیت‌های ۱۲۰ روزه قابل تمدید که در هر دوره نیازمند ارائه گزارش اجباری به کنگره هستند.
تعیین بخش مالی ایران به عنوان «نگرانی پول‌شویی» تحت ماده ۳۱۱ قانون پاتریوت: این موضوع نیازمند مقررات‌گذاری جداگانه از سوی شبکه مقابله با جرائم مالی وزارت خزانه‌داری آمریکا (FinCEN) است و صرفا از طریق دفتر کنترل دارایی‌های خارجی (OFAC) حل نمی‌شود.
تحریم‌های مرتبط با تروریسم، حقوق بشر و موارد همپوشان با پرونده روسیه: هر کدام مستلزم اقدامات حقوقی مستقل و جداگانه هستند.
ملکی در ادامه می‌نویسد: «لغو همه تحریم‌ها» یک دکمه روشن و خاموش نیست، بلکه پروژه‌ای چندساله در حوزه قانون‌گذاری و مقررات‌گذاری است و کنگره نیز در آن حق رای دارد. و این پرسش مطرح است که چگونه می‌توان اتحادیه اروپا را وادار کرد محدودیت‌های مرتبط با ایران را که در چارچوب پرونده‌های مربوط به روسیه وضع شده‌اند، لغو کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/76514" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9-xlMKeRIpzzGOE7BQwSLot2C2t_BtPWEw8HJaFb1wAz1x4xipCX6QAggUZNTc3f6cMXk09Ik_hy8JVYdSo05ZFavcBM_F2mI-7NbNdNGJ483x87go0ZOfThJ_NPZGagz1xZ_DVNoRdJr5XvEMlPdrLV63xrT4lfYPBdUBtnZDYbyZQ8AMYzbEj0Nquu_tpc0tdxR1bnlaMSyqyvpuhoxfYoBqzwlaBYS3VC2XQ2B5I9pCFDS78eMWdZDrYsbHDIIEBcylJwqSN9l_eOyHz36uUKtDLn987KTJhBYZ8Ey0obEqhnnIWYYKx4hOmw7YX78qySHO_RJydUNN1Ogj8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه هاآرتص در تحلیلی نوشت توافق دونالد ترامپ با جمهوری اسلامی، برخلاف انتظار بنیامین نتانیاهو، نه‌تنها به تقویت موقعیت سیاسی او منجر نشد، بلکه شکاف بی‌سابقه‌ای میان واشینگتن و تل‌آویو ایجاد کرده و نخست‌وزیر اسرائیل را در آستانه انتخابات با بحرانی تازه روبه‌رو کرده است.
روزنامه هاآرتص در تحلیلی نوشت نتانیاهو امیدوار بود سفر ترامپ به اسرائیل و حمایت علنی رییس‌جمهوری آمریکا، مهم‌ترین برگ برنده او در انتخابات پیش‌رو باشد.
به نوشته این روزنامه، نتانیاهو انتظار داشت این سفر پس از «پیروزی کامل» بر جمهوری اسلامی، سقوط حکومت ایران و انتقال ذخایر اورانیوم غنی‌شده برگزار شود، اما اکنون نه‌تنها هیچ‌یک از این اهداف محقق نشده، بلکه ترامپ تقریباً هر روز با اظهاراتی تحقیرآمیز از نخست‌وزیر اسرائیل انتقاد می‌کند.
هاآرتص افزود توافق آمریکا و جمهوری اسلامی در اسرائیل به‌طور گسترده «فاجعه‌بار» تلقی می‌شود، زیرا ترامپ برخلاف وعده‌های اولیه خود، جنگ را بدون تحقق اهداف اعلام‌شده پایان داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/76513" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jn65TEW5pPESQaquXrKMmxhjQKMtzLyyjliiRwQhVtCSF0OfZZzZeM5UHZSnRCdTftN2Cq57RvyZaPf-dGl-w3J7cmIAZFShFox3sXpahcmWsUL4QApGGvJFRRxqtvV0mVvAf0Y0D-H6iKIlJfF3ZRT-i6QK51iahN8hBG9WQtU3yAEKYW88ms1pctGDn6lFC-iAaj57VMXaWRdE34u1pCO9uZEXknaCKHkyGF39QF28fZ7Hm1T4mueBvPEM_jRVGTkSYcSY_LJiqRST919cR_GObh_CaTUgO8tnRjyc6Bv2I-AVkckgUjf2Ta2wu92nS7p7GcncGRvmalkrogyfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«معین بصیری» ۲۱ ساله، ساکن شهرک اندیشه تهران، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله از نقطه‌ای مرتفع و از روی پشت‌بام شلیک شده و به قلب معین اصابت کرده است.
او در پی این جراحت جان باخت و پیکرش پس از انتقال به کهریزک، به بهشت زهرا منتقل شد.
نزدیکانش می‌گویند پیکر معین بصیری را از بهشت زهرا تحویل گرفتند و مراسم خاکسپاری او روز ۲۱ دی‌ماه برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/76512" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76511">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JQnBt9W3-U-bO8IloiMqTt3CqU3KQ58Dm5t6CBLE0UyxxBjSRdaAna4SIkQgUgsaUpYgBTKYmbrKGQCcX7C9SouB_L-4J4BKKym5hJnid_mlpl3IV6p0dWsGDkar9walPKi0qlz8PERHoJHxcm-cXFEERHN7rwyRq25_PZ4AOkKWbBeqR2b08lb15WLEL-qwIfQ-MMlZk7LeEEMw9AjNZ5H7y-7-03FNy81mKH9y2JTyWF5skkGMYURThdws1Ug2aQthXvpEYsBxmlgla7Jv40DrygwAngBaGpQn5lB6AsBIfTQ4LXvRRGxiko8XSWCQ47PT76MIPTFPu4E6sTxQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
«جنگ، ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات ضدهوایی، نه رادار، و عملاً هیچ چیز دیگری هم ندارد؛ با این حال دموکرات‌های احمق می‌گویند ایران الان از چهار ماه پیش وضع بهتری دارد. اصلاً می‌توانید تصور کنید کسی با چنین حرفی قسر در برود؟ بعضی‌ها چقدر می‌توانند احمق باشند؟؟؟
رئیس‌جمهور، دی‌جی‌تی»
realDonaldTrump
«ما از سرِ درماندگی دیدار نکردیم؛ ایران بود که از سرِ درماندگی آمد. کارشان تمام است! این ۶۰ روز را هم طی می‌کنیم. هیچ پولی گیرشان نمی‌آید، حتی ده سنت!»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/76511" target="_blank">📅 17:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QrCdezYMu2rLqhJq-z4pKv8Erum3RVDA0GupkbiErsFORa8yfkYyZCb-HtllI9A0JMJDTAgffDNs--qmwf8AZkqSSNwrQBwyid3n02Rv4p77R7n5qkX6sRQxsGKEKES2zd3uLADHswofuNNnhkS5C1uslSu7QlNfhDY6q2gcgc_5DZ1nfhr-FSOy0cijMOj-wJi_iFRPYNr8OoTifIYG2IPItat26TxjJWPyb4kiylXnsaKsh8i6smTuvUIkDZKvYNX19es36Kl5gt59hhTQVWbV9qIMiBZrfQotLktpOIeEbOE2aPEbN8z9wdWOowwgqDaTMYeO50tNtsUAqf-vTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O1f7KvF5THJ4Hmsvy9yce67O-kRJ1RFRsoXLoRtoVzbhKFk1V9VWN1J72gXn7u7U2N_qHLXEbs8eXdd9xBgxhKf4HqGmrm8FYGX7r0gnOA033f0Rnzw1MGkiQ_u_bpV1pTS0zvAWy9Codns6dJCL9dv7ZjfXMSONtuAG8ppiiWDOxO80MELmGM70mgEXmM5wIdQh2957wCBpK7P17ewH3pQfKMQr7IjzrzNIrc8SDOVuqOAPQy5TxgcG5SbG1g6z16yfksGIbNmVAanxElb-CtFJQXycsy9FIeIEQBnDjUo1FNaW0Q0GYj6jhhMvhSlh4O1LPnfWY8UAtEkYYESM5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر خارجه فرانسه می‌گوید پاریس تا زمانی که اطمینان حاصل نکند مذاکرات درباره برنامه هسته‌ای تهران انتظاراتش را برآورده می‌کند، با لغو تحریم‌های شورای امنیت سازمان ملل متحد علیه ایران موافقت نخواهد کرد.
ژان نوئل بارو روز جمعه ۲۹ خرداد این موضوع را اعلام کرد. فرانسه یکی از اعضای دارای حق وتوی شورای امنیت سازمان ملل است.
بارو گفت تا زمانی که مذاکرات آمریکا با ایران به ابهامات مربوط به برنامه موشک‌های بالستیک جمهوری اسلامی و حمایت تهران از نیروهای نیابتی پاسخ ندهد، ثباتی در منطقه برقرار نخواهد شد.
او افزود: «ما به یک تغییر اساسی در رویکرد ایران نیاز داریم.»
@
VahidHeadline
وزیر خارجه فرانسه: کشتار معترضان دی‌ماه را فراموش نکنیم، مردم ایران بزرگ‌ترین قربانیان جنگ بودند
بارو که با تلویزیون «فرانس انفو» مصاحبه می‌کرد در پاسخ به پرسشی درباره سیاست فرانسه پس از «امضای تفاهم‌نامه پایان جنگ» ایران و آمریکا در قبال تهران گفت: «مردم ایران، بزرگ‌ترین قربانیان این جنگ بودند. آن‌ها از یک سو گرفتار سرکوبند و از سوی دیگر به رویشان بمب ریخته می‌شود. ما کشتار ژانویه (دی‌ماه) را که در آن خشونت دولتی بدون تمایز، معترضان مسالمت‌آمیز را هدف قرار داد، فراموش نمی‌کنیم.»
فرانسه حملات نظامی آمریکا و اسرائیل به جمهوری اسلامی را «غیرقانونی» توصیف و بارها اعلام کرد که در این جنگ شرکت نمی‌کند.
دونالد ترامپ تفاهم‌نامه پایان جنگ با ایران را در کاخ ورسای و در حضور امانوئل مکرون امضا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/76509" target="_blank">📅 17:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB9m8-SzhMg9gsgDXq0HJUCTn_OAgk9NSiFXsE314yr6Vt_hh1aGVOr_5OFH4FPuC6ZrX9nZ77o-CNUqMGREZAnKR8Wg4lsfatqtcUFgJ_vb0RD8BqyIfC8e2g6w-Cn2K17kIkS62HhX49FEzGiytIAIw3IYKN-8J1n0ahuB7FZ5TkdeF29O9c7RCkRsgz_I4c92ASn0pYagW4w6c5Mf8JaNe2fHwYxHSjx9cAH_y0gPMmH8x_UrchWku44QypJD79KgFE-I_jPhg_JQxCq3sbE7Qlk6jwnJJ9g3MMIiYirCKA8Cr8DB5cNAExmk--sj_u3mgFQNlFe43HDeZ5X0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال از قول منابع آگاه گزارش داده که طبق توافق پایان جنگ، ایران حق دسترسی به شش میلیارد دلار منابع مسدود شده در قطر برای واردات اقلام انسان‌دوستانه و غیرتحریمی از خود آمریکا خواهد داشت.
به گفته یک دیپلمات آگاه از جزئیات توافق، این منابع مالی به‌صورت مرحله‌ای و در بازه زمانی آتش‌بس تمدیدشده ۶۰ روزه آزاد خواهد شد و تنها برای خرید کالاهای آمریکایی قابل استفاده خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/76508" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76505">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjofNrsOfF1cxuHq7H5clVjkb4xmE8rA68NZ2wPXj8BTSlrvNO7A7fC5wRvM7NNdBNb3bFQjsUxdOdoHp4qEO1xI2dYrf9pa92l3bGJOiYAHx9o52M-ttYJSxT-xV58z2U-dxVfhhbZCT3n0L0D8fvxTWqO_tTNszTpomRMyJJXwXJB_XvLVdKdgbaQB2RDav9eKDYp216URHaGQygO6f_YSoOM7YKfLcV3fNvqAYaHSU5No1spFeTQwsrXgpVwR1sk8arICMrLUwm8ccGaG7bT89ECtqsSVwU2MQoiMmEg5UUFpp8lkPUvNgoEtM1fUQp2X4ncUu_TGwRaQ5f8AOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gceqFxMB05KgK9aun-8Sys5izySoqorL8QX6teGK7cMrpEBqkB2DZE1Z8K0yKU6pJOjLtqQUJluSAzXx9eEUCKQJRWNvpF2Tu7fWRD1UTdjphuPAj3syVAEYWJ_HybT3PIP2s3HclnT1nTZ8JxrsQnGNxb9kyRGGhlhcCFdnfAz7mopHFTtMQZxOdgOD37zn_YSCnvP_2nnHFmBNo1bK6Wt_iQ3pLg0t087aSzsyeBQH1R_jf2WQxSt_wMTvYt65Kq1zSQ-_ixvlVccuXr-2fewCdMzbsVhSOlMn1tpYR4MFtC7VIn340h8T7XgnzOPdS-qwCDoVmbUu5Db3asqP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYSSIb045QAfueriVP5e89Q_WxXSyzZhYj-0guAqmtdls7GhV9hvLlKdH5ixBfjMEH-eGJWOGsVx6fHXq16NHfb80-K7lLmHIPbSQkDjwJHFx1rTwHXSMViLlH4vHvlVa7HZLiOCK5Gab2f1g41_xGvRw-GiftwiMQwn_pDNaVynhcqn07EZ2bGRs-nQjZFLSgcLiq93Z-uvv8rHBEds3p0dMJdSqBikHmFvQ65DNrFpKmc6zaIM6OzfVbj8c_cQ3mQd3-7CN-GuuY7ZeNTvpZPf3NPHxDT-Nh6OWzHi1EGelHIwpdZi7NfZT5ZMjR1UybRGdh1BaV4N5OxH3BBWgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بيكر علی حسن‌پور را بعد از ۱۰۴ روز به خانواده
‏تحويل دادند
‏
🔸
⁧
#علی_حسن‌پور
⁩ در ۲۵ خرداد ۱۳۸۸ در خیابان آزادی تهران بر اثر اصابت گلوله به سر کشته شد. خانواده او پس از ۱۰۴ روز سرگردانی، سرانجام پیکر وی را میان اجساد مجهول‌الهویه پزشکی قانونی کهریزک شناسایی کردند.
🔸
اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است.
🔸
علی حسن پور یکی از این افراد است. سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/61687/ali-hassanpur
@IranRights</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/76505" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL3dRIdnOlKNfovULnCdGQLfQI5eg5TaTzR6-UQugYGli94squRooEmjmLXUWDq1RGpsVHkVu7zFehzMkw6AvKY0lqu269QbE8OpkzfGvHR4gDk3_1CrtZe47H71pRluoNlBsfm9dh7tOzM8NrwN-WX578j37o6L-9pWZ5ZRQtlyOgRDNjwZ4t-MJ_ZjNFq_k9aUL5MN86apzkOBjmLX_X2SYtYDpL-Mqjdb0_drWzw67rwPdVfX2PUGs7x4k-wVM89MrXHlrwx5rgEiP1ksfbLG-35o2xWFte5kLBhftwyfRH3INhCmgywDIJFfai09W6jnhFCft74hDZweBujeVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ملی لبنان می‌گوید در حملات اسرائیل به شهرک‌های شرقیه، حاروف، کفررمان، کفرجوزو کفرصیر در جنوب این کشور دست‌کم ۱۶ نفر کشته شده‌اند.
به گزارش رسانه‌های محلی لبنان، از ساعات اولیه بامداد امروز، حملات توپخانه‌ای ارتش اسرائیل به شهر نبطیه و مناطق اطراف آن ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/76504" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yq7R4umdJaZYNfEJNrGMFr7ujKk_1-RQI2hCp4chZ16eiUkWxRn-PDxPD4BEk9h1UOvqZoKaNOVuJEBIkJkz6itM0uBB2obZSNLNe_bAqvWPrxfOjPPOwiFaGIssyGydTMDGWaWeGudg0lxR3PO-g3g0bd8pSo-3_dQJ1iPb2AsdkohnX3QI7549ZVrW_ySkJV2vYJTSDmXCXkPLN2EyT1LfwgQ3ChwTuPzzUAGOCHXH1UELvd5y89Q_x71v_2I7KMNNuUoCFK6T7SbCEFAfw9oznyNzBpCIKflKeKFQ_rTHtUYY1CFv_j9AS3ZSiKYLRt9oh-DznfJ4c7Ud81qNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی اعلام کاخ سفید مبنی بر لغو سفر معاون دونالد ترامپ به سوئیس، وزارت خارجه این کشور اروپایی رسما خبر لغو سفر هیئت آمریکایی و لغو مذاکرات تهران و واشینگتن در روز جمعه را تأیید کرد.
لغو آغاز فوری مذاکرات بین دو کشور متخاصم تنها یک روز پس از امضا و رسمی شدن تفاهم‌نامه‌ای رخ می‌دهد که یکی از مهم‌ترین بندهای آن ۶۰ روز فرصت برای مذاکره درباره فعالیت هسته‌ای ایران است. قرار بود این ۶۰ روز بلافاصله در روز جمعه آغاز شود.
اما خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز پنج‌شنبه خبر داد که مذاکره‌کنندگان ایرانی پیش از آغاز دور بعدی گفت‌وگوهای صلح نیاز دارند نشانه‌هایی از اجرای توافق موقت از سوی آمریکا مشاهده کنند و هنوز تأییدی درباره سفر هیئت ایرانی به ژنو وجود ندارد.
در پی این انتشار این خبر بود که سخنگوی کاخ سفید هم در بیانیه‌ای که پنج‌شنبه شب منتشر شد، اعلام کرد ونس و هیئت آمریکایی آماده بودند به محض نهایی شدن برنامه مذاکرات، عازم شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76503" target="_blank">📅 17:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PJ-UT6ux6n0Tln7iM30KRzhbRvx6z_0Ta2WqiZwOIJCkSPwr7yEwl3AViUgPm5uiSF3WxOqLz95_wXIUfeiyJaeqZ0HtAs3ckMGyFk0rbE9eQlSTTNvbRqPf9-BiLgv6UWZyWa6OoCwfQroS9smaw7T4f5qwbTh_KL3CLIZoyvi5nR5SiTGkBnI_xLfhbXnD656etlA5cyHRnRx3NWXD4JsRWvJKI7PGSVdvACOKhn6oijbc9n-uUdDufTFrU9n5nBuNn636ivqj-jG38G8b823I6UbjeRXUW4UYA1fC-1-38o8eeeol8tvXnsrNjgvuEPvff-_OAZYVQFccMvvIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود قنبری‌راد، متخصص امنیت شبکه و از کارکنان یکی از شرکت‌های تهران، با اتهاماتی از جمله «اجتماع و تبانی علیه امنیت ملی»، «جمع‌آوری اطلاعات طبقه‌بندی‌شده» و «ارائه اطلاعات به اسرائیل» روبه‌رو شده است.
بر اساس گزارش‌ها، محمود قنبری‌راد، شهروندی ۴۰ ساله و متأهل، اردیبهشت‌ماه سال جاری در منزل شخصی خود بازداشت شده است.
یک منبع مطلع به دویچه‌وله گفته بود که او هیچ سابقه فعالیت سیاسی یا مدنی نداشته و به‌عنوان متخصص امنیت شبکه مشغول به کار بوده است.
گزارش‌ها حاکی است که او در تماس تلفنی از زندان، پرونده خود را «ساختگی» توصیف کرده و گفته است که برای پذیرش اتهامات تحت فشار قرار دارد. همچنین اعلام شده که وی از زمان بازداشت تاکنون از دسترسی به وکیل محروم بوده است.
بر اساس اطلاعات منتشرشده، محمود قنبری‌راد ابتدا حدود یک ماه در زندان اوین نگهداری شده و سپس به زندان فشافویه منتقل شده است.
همچنین گفته شده که او از نوعی اختلال عصبی رنج می‌برد و خانواده‌اش نسبت به وضعیت جسمی و حقوقی او ابراز نگرانی کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tbjNhmio1kKGClwpghCSlpNSNMWyFN6Np4WiHcMYsv4Y36NdwG_AFdzizxJzDY_eD-LWI_i-NAgK623jDLfP22ztpHkhub2Dy68tOTNT6qlM-AhPbpupgOkHpPuL1ff2GJeUzedrJBOhKI34LdecSDgOZ_QUKTklCOEJDoFSJo_mpoTNoy9P2fIf8aTHcU_bydDGctRWeBfo1mYdnF7GK-9arqqvdNs8Vt9IEnuSGP3WMQGUav1dDGQL5VKZTiy4Iv25z0dVTEL1BCsH6Kraw8l10vwD-cuWJ_T7-85D8OxQaouhvNwPpY9nMo1B_xhTQ6euSHtavHAQkwWf7t4kuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از امضای تفاهم‌نامه میان واشنگتن و تهران  را
منتشر
کرد.
این تصویر مربوط به مراسم امضای تفاهم‌نامه در کاخ ورسای فرانسه است؛ جایی که ترامپ در حاشیه سفر خود به فرانسه و پس از پایان نشست سران گروه ۷ (G7) حضور داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76501" target="_blank">📅 05:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q07l1wQlvkm1w8vboYcnvjkgQoBsykc0Zpk7kW4BkdPlYvjmkasQtyMwd7bCOvQQwSIJt8KZoPaQSdML38Cwfm_-A0VL0rY08Ds8o-GWL9VMCyg4_bhUQ8mI0dK0jMyDEbEiNP70UjdF3NVQ3rxPzTn47kwzCU8UNGMOOPX9Zi8apt7tVK83WCv6L9oxzkuG6wQFxrJsm25s9lJDWtKag5aPp4ydObfrwDstknJSIOwbSWB4u2IPNwyW6IARzmVLWB2bL4e_BOHifClhaf5vbm0WU7L73ONskYHgMDCSYn1wGqu3CulLtXdbDmWGPYJhq-nTLXXuDcBVOUajXgiDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در«گفتگو ی تصویری با اکسیوس» گفت یادداشت تفاهم امضاشده با حکومت ایران را می‌توان «نوعی تسلیم کامل» از سوی تهران دانست.
او این اظهارات را در پاسخ به پرسشی درباره تفاوت میان خواسته پیشین خود برای «تسلیم بی‌قیدوشرط» و مفاد تفاهم‌نامه مطرح کرد.
مجری آکسیوس در این مصاحبه به ترامپ یادآوری کرد که در آغاز درگیری‌ها گفته بود تنها «تسلیم بی‌قیدوشرط» را از ایران خواهد پذیرفت، اما یادداشت تفاهم امضاشده چنین تصویری را نشان نمی‌دهد. ترامپ در پاسخ گفت: «خب، احتمالا در واقع تسلیم بی‌قیدوشرط است. فکر می‌کنم همین‌طور باشد.»
رئیس‌جمهوری آمریکا همچنین با اشاره به جنگ اخیر گفت ایالات متحده ایران را «کاملا از نظر نظامی شکست داده است». او با تمجید از توان نظامی آمریکا افزود واشینگتن توانست محاصره دریایی موثری علیه ایران اعمال کند و هیچ کشتی‌ای نتوانست از آن عبور کند.
ترامپ همچنین گفت پس از جنگ با ایران، محدودیتی برای قدرت خود نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76500" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xvy5RUCnofqBzqxH1tSK1H3cjqGJLnUWgmLlo5oMedd7bKHMI7XDKjAZp1hLClS0H1EHEDaydSG6YbHiIOqZU3Sz0t88FhgAa07DPdsLWuzORw-_m2a5aFWGq9m41eH_vuFUVmDPJsENN9nTowqYtrfGMCblgVg0o8qXfEqMoYyQ64OLAjN_aEcKQlNDf7_FgBlPcqvgolQMuMIBPyxLqtyXoA3gDGBnKg0oK_oQO13LHO8UNP5uS8Lz7iqHTs49DeaJmN9j3EH8RtNoC3GezQGCkljcdVQ-Q3XphygtuwxJVZq1PH4DUeOzlF7MMu--9xqtievZdHbaCSonc_-Hzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر جی‌دی ونس، معاون ترامپ، در اطلاعیه‌ای اعلام کرد که او سفر خود به سوئیس برای شرکت در مذاکرات با جمهوری اسلامی را لغو کرد، زیرا برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و تدارکات و هماهنگی‌های این مذاکرات ساده یا قابل پیش‌بینی نیست.
در این اطلاعیه آمده است: «برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و هیات آمریکایی آماده بود در نخستین فرصت ممکن عازم شود، اما تدارکات و هماهنگی‌های این مذاکرات هرگز ساده یا قابل پیش‌بینی نبوده است. در حال حاضر، معاون رییس‌جمهوری امشب عازم سفر نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76499" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dFHSYwPaYd0dAju5mQ0R4qCfZ4MHGUskRbMgn3B9AKij-KcRd2WdarQIV1l9QbkX80ssIhdHZOj9X2pABGcqQfw628av8UOC2ORZeQ0OLOmYlOpc7QKjz0KJYA_FjUmBn61A4Ab5pCKhsQfXUnq12Yd6PcBfBsdvTXp18Vq-F-7pEnnl-Pp0TnZnbozp-LWYH8QS9FEkcCZDubAgdanVZFaeSTKsgp-l3NAlnZwLP9Cs9lPosoQTW0CJiITOHTRyjEnDi-2UIYbfoXI46X_5D0tRXevog9l_v2kSIfTWHTXKwn455K1OejhQgK30Uq63zQxrHvo3q8hcNZQ80-On5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آسوشیتدپرس گزارش داد استیو ویتکاف، فرستاده دونالد ترامپ، پنجشنبه‌شب در نشستی غیرعلنی با قانون‌گذاران آمریکایی اعلام کرده است تهران از آژانس بین‌المللی انرژی اتمی برای بازرسی از تاسیسات هسته‌ای خود دعوت خواهد کرد و روند شناسایی محل نگهداری مواد غنی‌شده را آغاز می‌کند.
بر اساس این گزارش، ویتکاف به رهبران کنگره و اعضای کمیته‌های امنیت ملی گفته است تفاهم‌نامه میان آمریکا و ایران هیچ توافق جانبی نداشته است. با این حال، تهران و آژانس بین‌المللی انرژی اتمی نامه‌ای جداگانه تنظیم کرده‌اند که در آن دعوت از بازرسان آژانس و ادامه همکاری‌های نظارتی مطرح شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76498" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA2KwJpdBNsvwj0oQTF6cJBEyijcF92Fs-Op_-CAJJngcSqtIxhqiqnmcaNdZvv84jd799OAuOfF2HbRFk8xyEand4f5ESqt0xFOd3MAhHcDpg94vMarW71GpaMpWb5u8kS5UMv7-JpMTjdfpnDPDjt2upWjoGG8Qztd4o6nHIgwweVzWH5bXnz2QfZDeDXvHBjFqU2l2uVQHObDZfIQnzhNcWVcPnc1fG3pcaiKHynISWFxxVvSDMWMHgBw_a-ylAObRM3KCc7zqVtREkqkL9WiUN5f5vSXMmCeRQl9KiVG2zq7aPlIARkIiVCZWovAQKwR5bhrowWv-bvIao0oCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجه اتحادیه اروپا، گفت هنوز برای بحث درباره لغو تحریم‌های اتحادیه اروپا علیه ایران زود است و این موضوع پس از دستیابی به یک توافق هسته‌ای با ایران بررسی خواهد شد.
او پیش از نشست رهبران کشورهای عضو اتحادیه اروپا به خبرنگاران گفت: «زمانی که شرایط فراهم شود، کشورهای عضو درباره مناسب بودن لغو تحریم‌ها گفت‌وگو خواهند کرد، اما هنوز به آن مرحله نرسیده‌ایم.»
اتحادیه اروپا در حال حاضر مجموعه‌ای از تحریم‌های چندجانبه علیه بیش از ۷۰۰ فرد و نهاد در ایران اعمال کرده است که شامل ممنوعیت سفر و مسدود شدن دارایی‌ها می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76497" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76496">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7PS6qUeTDGfjKMQrJwR8b6GIM-bvXOtVXuyD0Knkbe4ptFXO1pIEdxbQimChQBBPH5h1rTmHK9vRYlPx67VrUbXH6K2IAzOSefz5ji8f1CsLPcMZICP2aU1ZOunFFIZ8iRrMFZRfbbzWGCW1v_UTKg1Dysxhnhfu1eRK9zPb15NftOBsBvkHkILM0LdhRis9IBrIblUTIdVN8NIOdz4P9WtwEMUc1Y8QOPf5JCF2tsBx0KM-ehHL2YboWplOzCXRKNqFhwWt2fEs0D0m2jyf3FvPMJgBA75CoCmys3JfhkrsP5fSbGBJ03Q3cKawpcdTYkDWXoPpoONTpK_aU4R5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین به نقل از یک منبع آگاه گزارش داد هیات مذاکره‌کننده جمهوری اسلامی به دلیل ادامه حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس برای آغاز نخستین دور مذاکرات ۶۰ روزه را به حالت تعلیق درآورده است.
المیادین افزود: تهران پیش‌تر به آمریکا و میانجی‌ها اطلاع داده بود که پرونده لبنان در ادامه یا توقف مذاکرات نقشی محوری دارد و هشدار داده است حملات اسرائیل تا عمق ۱۰ کیلومتری خاک لبنان نقض یادداشت تفاهم و توافق چارچوب است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76496" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tEEl-ulFK-kqkC7jeXS0Y8u0gKxqdj49ZdElDgin20dyp43YkbbRiMA_fDIZQK99n_HBLIcZRlWlaRZEUSa24r84McM8zKSylbgV-8B2abO_31YVT2sXSuuqvbJRNNC-d0L9b4S7PnmJkQ_KnBZ4La0tUs37GT7AqeY78GI-mh1vXyjE87eS70MuhghN0da5QhUJMyMkc7uLZAfNa-HIqsjwplbYN-2U6GFbEpSafAqUwr03rrPHHVY1uihQZo_Wczn5wwwAObZ1cX8h-_BTVJk6ANIJHWFoBXywqvcp5yvbRmcrY0ypp7tCb5Lcv1zQWRfCyubLJirjgUG5fnzKEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت کاخ سفید:
رئیس‌جمهور دونالد ج. ترامپ تهدیدی را حل کرد که واشنگتن چهل سال صرف مدیریت آن کرده بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
یک پیروزی برای آمریکا.
🇺🇸
WhiteHouse
ترجمه با هوش مصنوعی به تصویر اضافه شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76495" target="_blank">📅 22:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OzcdEW8i6jlZUXGl38YQrQMa9Ua0WGFY3ovNp6nryXhv-to-8Uyg2CoEtlPORSDI1Y7dQ6SPLFW13bHeb4htOoEdLTLjYh1YrlP7bJyBoEtb9JXbjJxpRIkJNl_mu6IICAsmrwZaXxbkg93H2kcBExnSTgFfE3Huoz2tB_6A4fmZsRJ-P8UC9f0XZkCztlh4u9GlAzoysQWmFGArmEEBLfWZ_LkyxkUAcYJ_H9YE6NjgqcLYlBS1n-ryAGBYB29Zh1pwJG5K3vgjMSL5cqYyA5pPhHMj0VJY7ih-bP346q0ysfBBycRNUTLn6BABswgXC1gAYhOXa7gz7BlG_o_SMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'
بیانیه شورای عالی امنیت ملی
'
منابع حکومتی:
🔹
در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (PGSA .ir) ارسال نمایند.
🔹
به موجب یادداشت تفاهم اسلام‌آباد، به مدت شصت روز، هیچ‌گونه هزینه‌ای از متقاضیان اخذ نخواهد شد و این هزینه‌ها توسط دولت جمهوری اسلامی ایران تأمین می‌گردد.
🔹
بر این اساس به مدیریت آبراه خلیج فارس دستور داده شده است، در جهت تحقق اهداف تفاهم‌نامه درخواست‌ها را با سرعت و اولویت رسیدگی و پاسخ دهد.
🔹
با توجه به شرایط خاص و وجود برخی مخاطرات ایمنی در مسیر عبور و به دلیل لزوم حصول اطمینان از تردد ایمن و جلوگیری از حوادث دریایی، لازم است کشتی‌ها در مسیر و زمان اعلامی به آنها عبور نمایند تا به تدریج، امکان تردد افزایش یابد.
🔹
ترتیبات اجرایی و جزییات فنی عبور از تنگه هرمز از طریق مدیریت آبراه خلیج فارس اعلام می‌گردد.
🔹
در خصوص سایر موضوعات، از جمله مین‌زدایی، اقدامات لازم مطابق بند ۵ یادداشت تفاهم اسلام‌آباد انجام خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76494" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76493">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OUJSScKEae7FHQSuWNJJChae9x6yiAtKcXy3_6US9Na8TzJJjERaIJo7V5iYCjVrA3MccH58I2PrXAzLqaxhCQzC7Nv9kjUtpEAflprSb79r7Ck4huCg6JEMgIhOLSQP5wvhKRovmvFHaY9FuHMrC3KYCB9o5bv5rZp7UfKpauJeX9c4EaTofQ6L2KVaqkGaZy2Q8fjrvh0nuGqCIoUgyqVyhn4IERQXVC3CWuNlMw1r3u8QaLZixselEoZWF6rkgvgZXkbcPY8aEYSzPDesRk-wmHmAavKnECQzU2-V2ypIFUMWBw-EQoLL4YSCLzklvi1uvMRAVNH_R9sdw1bGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: انتظار آتش‌بس کامل در همه جبهه‌ها از جمله لبنان را دارم
ترجمه ماشین:
ایالات متحده به صلح متعهد است و ما همه در منطقه خاورمیانه را تشویق می‌کنیم که به تعهد خود برای فراهم کردن امکان پیشرفت زیبای مذاکرات ما پایبند بمانند.
بازارها از آنچه در حال رخ دادن است استقبال می‌کنند: قیمت نفت به‌شدت پایین آمده و سهام به‌شدت بالا رفته است.
ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76493" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76492">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPourostad وحید پوراستاد🔷(Vahid Pourostad)</strong></div>
<div class="tg-text">« پیام منتسب به مجتبی خامنه‌ای در واقع نوعی فاصله‌گذاری حساب‌شده با تفاهم ایران و آمریکا است. مجتبی خامنه‌ای رهبر جمهوری اسلامی اجازه امضا را داده، اما مسئولیت سیاسی و اجرایی آن را بر دوش پزشکیان و شورای عالی امنیت ملی گذاشته است.
پیام همزمان رو به داخل و بیرون نوشته شده است. در داخل می‌گوید رهبر با رضایت کامل وارد این مسیر نشده و دولت باید پاسخگوی نتیجه باشد. در برابر آمریکا هم این سیگنال را می‌فرستد که تفاهم، زیر فشار ترامپ و دولت او به‌معنای عقب‌نشینی قطعی نیست؛ بلکه مشروط است و اگر شروط ایران محقق نشود، موافقت نهایی رهبر با توافق نهایی هم تضمین‌شده نخواهد بود.
در واقع متن، بیش از آن‌که اعلام رضایت از توافق باشد، تلاشی برای حفظ دست بالا در مرحله بعدی است: هم مسیر مذاکره باز می‌گذارد، هم امکان عقب‌نشینی تبلیغاتی حفظ می‌شود, هم به واشینگتن گفته می‌شود که فشار بیشتر ضرورتا به انعطاف بیشتر ایران منجر نخواهد شد»
@pourostadv</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76492" target="_blank">📅 22:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tojUbgKMP07p_EnDhq36aIIK85-_elWWU8WMLZ_QFSAKnjRKxnnyt7vNnG-kvRDqY9B2iGqxLmBRz4RLb8uT7yyPIchCx79N0AsJujbNlJ3iOHU7TrJGa7Eebl-V4q-p8ylv-8_zoj3J2Gn5rtqDYFh5fcN4-lF94w7dWYGdqUwc0j0GOu6Rij5Bu9CZQCDMj61PwMmo208fEw6STsgSvuzBycAnxXVCOOQImsGnCaDIU8d49kGwjcEKdwWhVql8wZywEVw0ZyJaVm57UAmr9LyRRYCiio5OjtMH41G7B2N0XvnHznGKk6KMm_f0pTCMyNM6Ac0xCygiOE7nVxIAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول
گردن‌نگیر
جوان شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76491" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZhpM3jkADsBzGzub4iYxM7qhBApxbbvPw29OgnbZX2EE57xRLs7Blx3NEYC3kNzNld37JcQavj2g4yXMMYL_i3a1_f5Dpfj76LzLtd5nSAk1fvm7G3FntV3qtbVi69ltEyhjoSxZhWszR-sHGpMpwmFxu1Plmj26L-8HCYtbEMnRi57-SmebTimOyRBhbKQ1qXfoBvSV4DRIdM2cl76f_8ZSwnXGoyBt-LNzmMy3xMH5Uq9jvuDrTRnX8khiQfZqSHXudzOPjvmH_YJL21BwanKpej07ik2Dv1FsD4cFN4YMimJ7HjHYTI3DOSCcaxytxyXw2f8pUHQfAh6YCgyCLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پنج‌شنبه شب متن پیام مکتوبی منسوب به مجتبی خامنه‌ای را منتشر کردند که در آن رهبر جمهوری اسلامی درباره امضای تفاهم‌نامه میان ایران و آمریکا گفته است که «نظر دیگری» داشته و مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا دانسته است.
در این پیام درباره توافق با ایالات متحده آمده است:
«بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیت ملی از طرف خود و سایر اعضا در پاسداشت حقوق ملت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه آن را صادر نمودم‌.»
در این پیام به تفاهمنامه اخیر به عنوان «تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و آمریکا» اشاره و گفته شده است که رهبر جمهوری اسلامی و مردم از این لحظه «منتظر تحقق شروط گفته ‌شده» خواهند بود.
در این پیام آمده که مذاکرات حضوری آینده «به معنی پذیرش نظر دشمن نخواهد بود.»
VahidOOnLine
در تیتر و متن نامه و خبرهایی که درباره‌اش تولید میشه بسیار تاکید دارند که این تفاهم‌نامه‌ای بین پزشکیان و ترامپه و نمی‌گن بین ایران و آمریکا
در واکنش‌ها از کوچک‌نمایی نقش
قالیباف
یا محافظت ازش با سپر کردن پزشکیان هم میگن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76490" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ufc7pccyvEqFJymaRdkUSqHjzMNxjsvF4ZacmmWSi2Nc-ZBvCYpKQQjK3Z68qiArOAtoLqhC_68ABFuX5CPh1NEj6WNEe_3L0PRjpdhaVyXqZ6x6JeOOip2HY4yzgjC7EGBgtrQM--fQy9D7FBzhfb69HqtXSnw3G2Z4Z5fSK9v5ESGgDGO9f5jDdMMb-ueDhPNERXyUmou6bjbMx2ixKSmnO5C2qbzMj31Bsp2CgtipxsU55XGilL0SouC0cPDNy-KVfCWUprpXhu0C2VLYyUR3J7eUYSdNM18s3ytyqiBNI5sPDnMPdteBlelz3kmhsmrJ_XzyPOyegXfJO8_nqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!!
رئیس‌جمهور دی‌جی‌تی
(توضیح: Dumocrat بازی زبانی تحقیرآمیز با Democrat است؛ از ترکیب ضمنیِ dumb به معنی «احمق» و Democrat. در ترجمه می‌شود چیزی مثل «دُمکرات‌ها» یا «دموکرات‌های احمق» آورد، بسته به لحن مورد نظر.)
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76489" target="_blank">📅 20:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FsSTYFSoGE4bUQODW8YucI0Jnu2tQwaIr_lc2DTtRBwXYAhQUCxgavJOl76ZNROojfGbEiRM4x8qfSh4H-nnf6bEme8gM_Nxw3BubS2GazlaIVAsxO5mrJKeMn1hD-xBU1_XggYtBR8egYo05pxYDZSQtss7PqJXH4GDeQtbbF9wzwoSoxBArEgd6sx3c8jB2XgO2jfDU50N9jMqucDoKBVMQCfR10ySxHvHwCsebm84Zxl-nfqQiqMDf-LhvUQjKsUesGDYK1DyMDhBvktphkBkpxFttH2mdKXYtUhZaMPpImOIMa0h_Kum_vjggmMoGzgrA4cHQfQoQrPmNVMp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام پایان محاصره دریایی
پست سنتکام، فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
امروز، نیروهای آمریکا مطابق دستور رئیس‌جمهور، محاصره‌ی همه‌ی رفت‌وآمدهای دریایی به مقصد بنادر و مناطق ساحلی ایران و از مبدأ آن‌ها را رفع کردند.
نیروهای آمریکایی مانع عبور کشتی‌ها به سوی بنادر ایران در خلیج فارس و خلیج عمان، یا خروج از آن‌ها، نمی‌شوند.
همه‌ی تلاش‌های نظامی آمریکا برای اجرای محاصره متوقف شده است.
کشتی‌های بزرگ نیروی دریایی ما در منطقه‌ی کلی باقی خواهند ماند تا اطمینان حاصل شود که همه‌ی جنبه‌های توافق رعایت، اجرا و به‌طور کامل لازم‌الاجرا و مؤثر باقی می‌ماند.
CENTCOM
البته سنتکام ننوشته خلیج «فارس»
🔄
آپدیت:
توییت رو ویرایش کردند و در نسخه جدید اون جمله مربوط به خلیج فارس رو کلا حذف کردند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76488" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76487">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qKRanGgMxiXD7vEXD4dc_p7m4uXLSXjuVDLBfL4Gdh-fDuemcQwkQAn8D7zjAtP4PI5_D5v4oQnxFtwlOM4qoTYI43QR_y1XYYJhAbgHEc1bXOCA35NhlPIz7-WoRktlAxFQz6EH9Y6HmwYp1Alfa2X6RZy8iNp0Bvl6n8af8H_crd6AZ7-rtzLtb8N3AA0TVcz4Vgs0YVvN0meE4RTBtAJNfCg0sX9vGt0nTBLFfi_uqpRJ-_MRelLQUR4g-V9HQKv14wzmziYqX-ntI5bEWTNYVaT8udrZmSEMbjcLlQqCuiNxdrabNJcMynyKrptS_8amHetMFo-iDpZRBcZBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره: ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار. realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76487" target="_blank">📅 20:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=iiZ8ZbctI71EZL2gKyVfn3zLd8uptepSoG5a3tnb_yVMg46ANpcHzUo-YFfD74mO8l3HiXzLLW2GnXZcCa_2liSEB67DsSudyBVYKoXm5bdS2wuf4Cc7Vz-3wS2O1Lhp-9PTmrQJImDb8ROf4ETdlIKitk-_-7bpOyXBWJYBrfOOOb_rWIucI3VDcmGTTKi6BkY-tmWHKU8R3UdxSGybUJwaVft_8HWM9fZG6Afz07q_mv8LoxOGW7N6K_BwLCzYV2NK3fyNANEYxD2OQF3Tyvf6pdkqp3Q1C8z4BTsOcA4MLTOI4TRc31MmDQoo0QF5mb9Y2JI3THGoPwJcA755XA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=iiZ8ZbctI71EZL2gKyVfn3zLd8uptepSoG5a3tnb_yVMg46ANpcHzUo-YFfD74mO8l3HiXzLLW2GnXZcCa_2liSEB67DsSudyBVYKoXm5bdS2wuf4Cc7Vz-3wS2O1Lhp-9PTmrQJImDb8ROf4ETdlIKitk-_-7bpOyXBWJYBrfOOOb_rWIucI3VDcmGTTKi6BkY-tmWHKU8R3UdxSGybUJwaVft_8HWM9fZG6Afz07q_mv8LoxOGW7N6K_BwLCzYV2NK3fyNANEYxD2OQF3Tyvf6pdkqp3Q1C8z4BTsOcA4MLTOI4TRc31MmDQoo0QF5mb9Y2JI3THGoPwJcA755XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی در ایران که ریاست هیئت مذاکره‌کننده ایرانی با نمایندگان آمریکا را برعهده داشت، عصر چهارشنبه در مصاحبه‌ای مفصل با تلویزیون حکومتی در ایران به نهایی شدن تفاهمنامه میان تهران و واشنگتن واکنش نشان داد و آن را موفقیتی بسیار بزرگتر از مقابله نظامی با ایالات متحده دانست.
او در مورد دستاوردهای ایران گفت: «هر آنچه را که با اقدام نظامی می‌خواستیم به دست بیاوریم، چندین برابر آن را از طریق مذاکره گرفتیم؛ اصلا قابل قیاس نبود. هر جنگی ممکن است پیروزی‌هایی داشته باشد، اما اگر این پیروزی‌ها در نهایت به یک سند حقوقی و سیاسی منجر و ثبت نشود، هیچ منفعتی نخواهد داشت.»
او در بخشی از صحبت‌های خود درباره انتقام کشته شدن علی خامنه‌ای گفت: «همان‌طور که خونخواهی امام حسین، ظهور امام زمان است، خونخواهی رهبر شهید هم آزادی قدس است... صد نتانیاهو بند کفش امام شهید ما هم نمی‌شود.»
قالیباف در مورد وضعیت تنگه هرمز هم گفت: «تنگه هرمز هرگز به شرایط قبل بازنخواهد گشت. البته این به آن معنا نیست که ما در تنگه هرمز بخواهیم برخلاف قوانین بین‌المللی و مقررات دریانوردی عمل کنیم.»
@
VahidHeadline
قالیباف در مصاحبه‌ای که همزمان با انتشار مفاد تفاهم‌نامه تهران و واشنگتن از صداوسیما پخش شد، گفت برای حضور در مذاکرات با دولت دونالد ترامپ تمایلی نداشت و به دلیل نقش ترامپ در کشتن قاسم سلیمانی، «کراهت شدید» برای ورود به این روند احساس می‌کرد. او افزود که با وجود این مخالفت شخصی، به درخواست مقام‌های جمهوری اسلامی مسئولیت مذاکرات را پذیرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76485" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPSjgSHfvUjgzSj4FYcpfqzF50MIcMvpeWh48RIF-nVvk-srtIZNIVBPmIDtAJa7vUb8VuZ8ydrGnO4tzadx1dfky-zAJWVQLHzs7GBMPxWzpJjpJtl4wMCLzvi8cNIrICMg-12o3o5SIaZPCMIe60UdbFRbCMOMFoInlKTJtSEXFHV7UeGSA6xQ6IjMtTepxWyYqbwUiTUNYeXdsD-Ins4LgRRWupX12UE1QsnRmI4rvA-nnhlsFc1ZF1Tif5ukQIRUDAWrsd5UsQdt9KtiuVyVDQR0iXqvg7e_2Rz0c4ZMPcIjqEw4WcNAPivmA576p86Tmce3A04zWLX8fSCJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، یک روز بعد از امضای تفاهم‌نامه ایران و آمریکا در نخستین موضع‌گیری خود اعلام کرد که نیروهای اسرائیلی از جنوب لبنان عقب‌نشینی نخواهند کرد و تا هر زمان که لازم باشد منطقه حائل امنیتی خود را در آنجا حفظ خواهند کرد.
این اظهارات پس از آن مطرح شد که دونالد ترامپ، رئیس‌جمهور آمریکا، طی روزهای اخیر از عملیات اسرائیل علیه حزب‌الله لبنان انتقاد کرد و آن را بیش از حد «تهاجمی» دانست.
نتانیاهو در یک مراسم رسمی گفت: «ما امنیت و رونق را به شهرهای شمالی بازخواهیم گرداند.»
او افزود: «این امر مستلزم حفظ منطقه امنیتی در جنوب لبنان است؛ مستلزم آن است که آنجا را ترک نکنیم، تا زمانی که نیازهای امنیتی اسرائیل چنین ایجاب کند.»
رسانه‌های رسمی لبنان پیش‌تر گفتند که در حملات صبح پنجشنبه ارتش اسرائیل به جنوب لبنان، ساعاتی بعد از امضای تفاهم ایران و آمریکا، سه نفر کشته شدند.
از سوی دیگر، یک مقام ارشد اسرائیلی پنجشنبه به خبرگزاری رویترز گفت که اسرائیل «در حال انجام مذاکراتی سرسختانه» با ایالات متحده دربارهٔ موضوع ادامه استقرار نیروهای اسرائیلی در جنوب لبنان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76484" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شروع سخنرانی جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔸
دیشب، ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرد.
این بالاترین میزان از آغاز درگیری است.
🔸
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آنها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است که دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به تعهد خود عمل می‌کنیم.
🔸
شما چیزهایی درباره ۳۰۰ میلیارد دلار یا ۲۴ میلیارد دلار، یا این یا آن عدد یا مقدار پول خواهید شنید، و واقعیت ساده این است که تنها راهی که ایرانی‌ها به هیچ یک از این منابع دست پیدا کنند — حتی یک سنت، به هر حال، از ایالات متحده آمریکا تحت هیچ شرایطی — اما
تنها راهی که آن‌ها می‌توانند از این معامله بهره‌مند شوند این است که کاملاً مطیع باشند و رفتار خود را تغییر دهند.
اگر ایرانی‌ها رفتار خود را تغییر ندهند، برنامه نظامی و هسته‌ای آن‌ها همچنان نابود خواهد شد؛ اگر رفتار خود را تغییر دهند، آنگاه رابطه‌ای تحول‌آفرین با خاورمیانه خواهند داشت.
این یک برد-برد برای ماست.
🔸
در ایران تقسیمات واقعی وجود دارد.
آنچه دیده‌ایم این است که عمل‌گرایان در حال پیروزی در بحث هستند.
🔸
من کسانی را دیده‌ام که به این توافق شک دارند — افرادی می‌گویند ایرانی‌ها هرگز رفتار خود را تغییر نخواهند داد.
خب، شاید این درست باشد، و اگر چنین باشد، آن‌ها هیچ‌کدام از مزایای این معامله را به دست نمی‌آورند. اما آیا ارزش امتحان کردن ندارد؟
🔸
می‌گویم دوره ۶۰ روزه رسماً امروز شروع شده است.
پس بله، توافق دیروز شروع شد — ما امروز ساعت ۶۰ روزه را شروع خواهیم کرد.
🔸
تمام چیزی که رئیس‌جمهور دیروز گفت این است که، البته، کشورها حق دفاع از خود را کنار نمی‌گذارند.
اسرائیل حق دفاع از خود را کنار نمی‌گذارد اگر حزب‌الله به اسرائیل راکت یا پهپاد شلیک کند.
ایرانی‌ها حق دفاع از خود در کشورشان را کنار نمی‌گذارند، اما
ما انتظار داریم که به عنوان بخشی از توافق نهایی، آن‌ها نتوانند موشک‌هایی بسازند که بتواند به طور گسترده کل جهان را تهدید کند،
و این همان چیزی است که رئیس‌جمهور ایالات متحده دیروز گفت. و ببینید، خیلی ساده است: نمی‌توانید به کشوری — چه اسرائیل، چه ایران — بگویید که حق دفاع از خود را نداشته باشد.
🔸
خبرنگار: رئیس‌جمهور ترامپ دیروز گفت که اگر مذاکرات این دور به مشکل بخورد، شما را مقصر خواهد دانست. آیا نگرانید که او شما را به عنوان مقصر معرفی کند؟
جی‌دی ونس: نه، اصلاً. فکر می‌کنم رئیس‌جمهور شوخی می‌کرد، همان‌طور که اغلب این کار را می‌کند.
🔸
جی‌دی ونس درباره تنگه هرمز:
ما هرگز نمی‌خواهیم این اتفاق دوباره بیفتد، درست است؟ این موضوع مربوط به عوارض نیست.
این درباره اطمینان از این است که تنگه‌ها هرگز به عنوان نقطه گلوگاهی برای اقتصاد جهانی استفاده نشوند.
صادقانه بگویم، این چیزی نیست که ایرانی‌ها بخواهند.
🔸
جی‌دی ونس درباره برداشتن تحریم‌ها:
صادقانه بگویم، ما این را به عنوان امتیاز بزرگی به ایرانی‌ها نمی‌دیدیم — ایران... این را به عنوان امتیاز به آن‌ها نمی‌دید، چون چیزی که مانع فروش نفت آن‌ها می‌شد تحریم‌ها نبود.
آن‌ها بدون هیچ تخفیفی مقدار زیادی نفت می‌فروختند، چون تحریم‌ها اساساً بی‌اثر بودند.
در آن زمان، کاری که تحریم‌ها انجام دادند این بود که سیستم مالی ایران را به نوعی به سیستم بانکداری سایه‌ای منتقل کردند.
با برداشتن تحریم‌ها، ما در واقع قادر خواهیم بود کمی ببینیم که سیستم مالی آن‌ها پول را کجا می‌فرستد و از کجا دریافت می‌کند. این یک مزیت واقعی است.
🔸
آنچه به برخی از منتقدان توافق که شنیده‌ام می‌گویم، کسانی که می‌گویند «خب، ایران تمام این مزایا را به دست خواهد آورد».
تکرار می‌کنم آنچه را که گفته‌ام و احتمالاً باید چندین بار تکرار کنم: مزیتی که ایرانی‌ها به دست می‌آورند و قبلاً نداشتند چیست؟ و پاسخ هیچ است.
آنها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتار خود را تغییر دهند. اگر رفتارشان را تغییر دهند، این چیزی است که باید جشن گرفت.
🔸
هیچ‌کس نمی‌تواند حق دفاع از خود یک کشور دیگر را نادیده بگیرد — اسرائیل حق دارد از خود دفاع کند.
اما اساساً، اسرائیلی‌ها، درست مانند همه‌ی مردم دیگر، باید به این روند صلح که اساساً برای آن‌ها و کل منطقه مفید است، احترام بگذارند.
🔸
در انتقاد از اسرائیل: به نظر می‌رسد که ما درست در آستانه یک پیشرفت بزرگ در توافق هستیم، و ناگهان یک انفجار بزرگ در یک مرکز جمعیتی غیرنظامی در بیروت رخ می‌دهد و بسیاری از افرادی که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل قبول نیست.
🔸
توافق هسته‌ای اوباما اجازه غنی‌سازی داد — توافق ما این اجازه را نمی‌دهد.
توافق اوباما اجازه انباشت مواد با درجه تسلیحاتی را داد؛ توافق ما در واقع به نابودی آن انبار مواد غنی‌شده منجر می‌شود.
توافق اوباما بیش از یک میلیارد دلار پول آمریکایی به آنها داد؛ این توافق هیچ دلار پول آمریکایی به آنها نمی‌دهد.
🔸
آنها تعهدات هسته‌ای بسیار مشخصی داده‌اند.
آنها متعهد به نابودی ذخیره بسیار غنی‌شده‌ای شده‌اند که در اختیار دارند.
اما نکته دوم، تنها کاری که ما انجام داده‌ایم برداشتن محاصره در تنگه است — که اساساً آن را به وضعیتی که قبل از درگیری بود بازمی‌گرداند.
🔸
خانم‌ها و آقایان، کلمات مهم نیستند، ما درباره تأیید صحت صحبت می‌کنیم.
🔸
فرض کنیم — دو سال بعد، آن‌ها آنچه را که ما باید در برنامه هسته‌ای ببینیم انجام داده‌اند و تحریم‌ها را طبق توافق آزاد می‌کنیم.
سپس تصمیم می‌گیرند که برنامه هسته‌ای را دوباره بسازند.
البته در این صورت، آن تحریم‌ها دوباره باز خواهند گشت.
و به همین دلیل است که این موضوع واقعاً شبیه یک دکمه تنظیم است: هرچه رفتار خوبشان را افزایش دهند، ما می‌توانیم تسهیلات اقتصادی را افزایش دهیم؛ اگر رفتار خوبشان را کاهش دهند، می‌توانیم آن را قطع کنیم.
🔸
آنچه واقعاً اتفاق افتاد این است که ما یکشنبه یادداشت تفاهم را امضا کردیم. این موضوع شرایط توافق را تثبیت کرد.
ایرانی‌ها به ما آمدند و گفتند: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً این را درک نمی‌کردم—می‌خواستم متن را فوراً منتشر کنم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «باشه، ما تا جمعه صبر می‌کنیم.»
و سپس در طول دوشنبه و سه‌شنبه، در حالی که رئیس‌جمهور در نشست جی۷ بود، شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را تشویق می‌کردند که این کار را انجام دهند.
ما قطعاً به آنها می‌گفتیم:
«ما تمایل شما برای عدم انتشار متن تا جمعه را درک می‌کنیم، اما می‌دانید که ما در یک نظام دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق را ببینند. ما قطعاً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها تصمیم گرفتند که رئیس‌جمهورشان آن را امضا کند، رئیس‌جمهور ما آن را امضا کند، و سپس متن را به عنوان یک سند امضا شده فوراً منتشر کنند.
🔸
اینکه فکر کنیم فروش چند میلیون دلار نفت قرار است اقتصاد ایران را به طور بنیادین تغییر دهد، درست نیست.
🔸
در مورد وجوه مسدود شده، مقدار پول — صادقانه بگویم نمی‌دانم.
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. در واقع اعدادی بیش از ۲۰۰ میلیارد دلار هم شنیده‌ام.
بیشتر آن در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در خلیج فارس است، یا در اروپا، یا جای دیگری.
اما مقدار دقیق پول را نمی‌دانم — مقدار زیادی است.
🔸
من گزارش‌هایی دیده‌ام — نمی‌دانم این از کجا آمده — که قطری‌ها میلیاردها دلار و دارایی‌های ایرانی را آزاد کرده‌اند.
این اصلاً درست نیست. برای قطری‌ها غیرممکن است که بدون موافقت ما این کار را انجام دهند، و قطعاً بدون اینکه ما ببینیم.
🔸
درباره موشک‌های ایرانی:
توانایی آن‌ها در پرتاب موشک به طور قابل توجهی کاهش یافته است.
آیا این توانایی صفر شده؟ خیر. اما به طور قابل توجهی کاهش یافته است.
ما آن مأموریت را رها نکرده‌ایم. ما آن را به انجام رسانده‌ایم.
🔸
خدا را شکر. خوشحالم که پاپ چیزهای مثبتی درباره تفاهم‌نامه ما گفته است.
🔸
آنچه ما می‌گوییم این است که
نیروها را به سطح قبل از درگیری بازمی‌گردانیم،
قصد نداریم چند گروه ناو هواپیمابر اضافی را آنجا نگه داریم.
ایرانی‌ها این را نمی‌خواهند؛ صادقانه بگویم، ما هم این را نمی‌خواهیم.
🔸
خبرنگار: چه کسی آن صندوق ۳۰۰ میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
جی‌دی ونس: تمایل زیادی از سوی دنیای عرب و حتی خارج از دنیای عرب وجود دارد که اگر ایران رفتار مناسبی داشته باشد، واقعاً در آن دخالت کنند.
🔸
کمی به توانایی رئیس‌جمهور ایمان داشته باشید، با توجه به اینکه او ما را تا اینجا رسانده است، می‌تواند ما را به گام نهایی برساند.
🔸
دونالد جی. ترامپ تنها رئیس دولتی در سراسر جهان است که در این لحظه نسبت به ملت اسرائیل همدردی دارد.
اگر من در کابینه دولت اسرائیل بودم، شاید به تنها متحد قدرتمندی که در سراسر جهان دارم حمله نمی‌کردم.
🔸
در سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط دست‌های آمریکایی ساخته شده و با مالیات‌های آمریکایی پرداخت شده‌اند.
مشکل اسرائیل دونالد جی. ترامپ نیست، و هر کسی در اسرائیل که فکر می‌کند بزرگ‌ترین مشکلشان رئیس‌جمهور ایالات متحده است، باید بیدار شود و واقعیت وضعیت کشورشان را درک کند.
🔸
خبرنگار: چه چیزی مانع ایران می‌شود که در آینده برنامه هسته‌ای خود را بازسازی و از سر بگیرد؟
جی‌دی ونس: اول از همه، آنها باید پول زیادی به دست آورند تا بتوانند برنامه هسته‌ای خود را بازسازی کنند
.
c-span
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76483" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjEkB7t5ERlNu136vJ9TLt_9NEI9K5YLJ83bJynLi2QRUhEM-LxWAUg9Xs5UIOe7FgOzYcs3K2YxLFOPm_O4lwKCpysyFWKFuCKTRjp1Ih1OXCUu9VoDSU8UzxRXiQ-4zkP-OKQjG-YNJGWN_tMuV5hE6FOgUWxIoBjM1CExc3bUjIoqP8W1cj03QHABJiq63kmG1whdUoA2GG28PsTjY5SEH0XDN68ux0yJiiO34mBqcjTFiz3UuEY_bSbZShQ09QWZuwK346n7mQqB7hFOgFqk4rQsLeK94JyfVl4hQiGfFoUkbl44q3mlkedqFYdh8LZzfQZcglykfrkab0mfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر کشور و رییس سازمان امور اجتماعی ایران می‌گوید به افرادی که در تجمعات شبانه «دوقطبی‌سازی» می‌کردند، در یک نامه به طور «محرمانه» تذکر داده است.
«محمد بطحایی»، بدون اشاره به نام این افراد گفته است که «مورد اول مربوط به یک سازمان و تشکل سازمانی بود و در دو مورد دیگر به‌صورت فردی، نامه‌ محرمانه و البته همراه با احترام و تکریم برای افراد مورد نظر ارسال شده است.»
پس از اینکه گفته شد ایران و آمریکا به امضای تفاهم‌نامه‌ای برای رسیدن به یک توافق پایدار نزدیک هستند، برخی مخالفان این توافق که از چهره‌های نزدیک به جبهه پایداری، تشکل سیاسی اصولگرا و تندرو در ایران هستند، علیه «عباس عراقچی» و «محمدباقر قالیباف» شعار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76482" target="_blank">📅 18:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bwzee5EaV5__b9pbxnxg-UbDlpwNglnfr5Bd6W0KZ8rdeInWnRt5DuYH4-kpBumhtpV92ttvjlpNFSTCX6dt-UTANtlqe60M-pRhm_xcmBe5KXL-_MSnOhLPtb59FH3EKrXvczdwvrgzR4Y7L2-JHqxod83Ge2mz2LTB559st62OwHn_QDxpz34sTEd-PFfhAJyuxWVSQ90FmjYwW8UsQUSvHHxkIhBVO6_4iWkjRCVtD0gtt6scobNzp6cbXxV-IrSrPLRgexJTtWhiDHbPW7QAlM3uS0TGhRpGeh-8SjYHFlf1QVG58wg56zgK1ZG-mRM2KsLAAb4-0cz7hVyNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرنا: به پاکستان گفته شده "نیازی به برگزاری نشست حضوری در سوئیس نیست"
ننوشتند کی گفته:
منابع دیپلماتیک پاکستان گفتند که سفر برنامه ریزی شده شهباز شریف نخست وزیر این کشور به سوئیس لغو شده است.
این منابع مدعی شدند که از آنجایی که یادداشت تفاهم اسلام‌آباد از سوی رئیس جمهوری اسلامی ایران و رئیس دولت ایالات متحده به امضا رسیده است، به طرف پاکستانی اعلام شد ‌که اکنون نیازی به برگزاری نشست حضوری در سوئیس نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76481" target="_blank">📅 17:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ko0yt-ibj-ja36AqkwyUQatWpbT3p2qJH6ZZ6TErim7j88-B5Q1c2YVIyKxE6Pif3jsBdiUIoOeekXW4sAYKZYjCfciW6KgB3NUJfS5sIk0yfM2aHJtcHkXcOyeGCVg7DMFFBp9OT-3P96G3czwB6ss4royv5WSkbsSwGjr-AaihzXJRW-KHz5yHx-lS0DRO4ftdxToEe_rzfgOpSzZ0IQJ6uicgfeFrv6DaFq_XIswEqn2ShCM5uNSFRLGBWU1rdjc0BUt_10WiW4WRIaAqKz_xAO_WNLeRBB_Z2GixiyzlEvsj9LoCO3mdABWrNIC8qsLVSTosmZGjerXZDa5Nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
«نفت در جریان است، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد، جهان امن خواهد بود! بازارهای سهام غرش‌کنان پیش می‌روند، مشاغل در سطح رکورد هستند، و قیمت‌ها در حال کاهش‌اند؛ مقرون‌به‌صرفه شدن! کشور ما مثل هیچ‌وقتِ دیگر قدرتمند، امن و محترم است. «خواهش می‌کنم!» رئیس‌جمهور دی‌جی‌تی»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76480" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BkADGHFRnLQNsF85CRm5qfu1Jgr3EZU9PZFIEUqLM0EZUoW4w0h22vXjcwbEx7AL3BJ1JIFabs58f5z0glBicYLbhtdSVKNGqd5J7RH3Q5TPZVUI3kzNyDW0LZpN95rRplqTVMq-oA0jA3DV6blwr8jcCjseZgowXjpixAorBxBltWNhYd70ojANjFVvrXgJN079OA5tlGCPPttzl202CymNTQicaEPnRTg5CRcSN1xLNgUOaIAib1fWtanQRHO4yRIxmZgpPPBhn621w6t3qEscVwmvpfG8Qc6-_eEw8vlGfV7TEgSdpaMuBu_kfghNW8PXnVyRzG6dBe5_bVexKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند دقیقه پیش ترامپ: "پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد."
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76479" target="_blank">📅 16:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uf6zXz_z31OjBElgj430pyYqVQh1xNh2l3uQ2STih9grwoUGp1n4jy6u2fWWCrddYBZ_td1yfRz9zF0QZ4wEi3GvSULa4OjujWqEwgm_Ey38riflJwIf2y_I5hCYNPHGB6LklrWzHkVwmvmz2cfTrugCbI1qLTv3HRu2yRCtqKq9t1pGGfew1FMubWcbQbncETBirR0WV8qXM-3aSShw0S0MAo5TTwDWqEsAlIqr9-spb_70iKhsrm1I__CRFjhZ7cA2El5eM3Qe7mvzfPUK7q5ncbHnc0SL1FmOdllRxKnWIEykmeNqqDEdU3B4wbFN75zc-szH-IJsRlLiNvECsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند ساعت پیش ترامپ:
این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سخت‌گیر نبوده‌ام، در حالی که بازار سهام همین الان به رکوردی تاریخی رسیده و قیمت نفت هم دارد «سقوط» می‌کند، یا حسودند، یا آدم‌های بدی هستند، یا احمق‌اند.
آمریکا را دوباره عظیم کنیم!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76478" target="_blank">📅 16:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ndHUpu10yzHs8UHUSlA0Kx93QLCHZkfXNqknvo73ggBoVsKF3bD4fdyOrQQKha-PdvQBmE3ckr3CRDPdyZMG3eM1PDJikMOZ8hfz4-hb1x2V9NFDFqhdv3Tqig3DjJVusxsNd9X7WDFWEjoRQFbbipfTDoMpTDuK9Wcqyyp6jmp744OSnmo_VbwzmpxS6aotCYmwohNOWdxIwDlYAe1rG3ZZgKdD8eaC_ITKaaz1hd_23CXOcz6BPWrHWfPSLSuTQ0zVOM7JQGl8wh1waeCGK1-b7TaatZek7hbREE_wXP_jaBafYyLzCym1mXjhQBE9CPAIp12RiN0Md9DEpWhllA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز پنج‌شنبه ۲۸ خرداد در یک موضع‌گیری درباره تفاهم‌نامه اسلام‌آباد تأکید کرد که ارتش آمریکا قرار است «چماق بزرگ پشت مذاکرات» باشد.
او همچنین تأکید کرد که هر گونه تغییر در اندازه حضور نظامی آمریکا در خاورمیانه «بسته به شرایط» خواهد بود.
این نخستین اظهار نظر هگست در پی امضای تفاهم‌نامه اسلام‌آباد میان تهران و واشینگتن است که بامداد پنج‌شنبه توسط رئیس جمهور ایران هم امضا شد و رسمیت یافت. دونالد ترامپ ساعتی پیش از مسعود پزشکیان سند را امضا کرده بود.
متن تفاهم‌نامه‌ای که دولت آمریکا به امضایش رضایت داد حتی از چند روز پیش از امضا شدن هم انتقادهایی در پی داشت، انتقادهایی که با انتشار متن کامل آن افزایش یافت.
به نظر می‌رسد که سخنان وزیر دفاع آمریکا هم تا اندازه‌ای پاسخ به همین انتقادها باشد.
به گفته پیت هگست،‌ آمریکا «از موضع قدرت به توافق با ایران رسید».
@
VahidHeadline
وزیر دفاع آمریکا همچنین گفت که برخی کشورهای اروپایی آماده‌اند در عملیات پاکسازی مین‌ها در تنگه هرمز مشارکت کنند.
هگست در عین حال از بریتانیا خواست نقش گسترده‌تری ایفا کند و گفت که این کشور باید «گام بیشتری بردارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76477" target="_blank">📅 16:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTql-MFWHa8lKtGoEmeNxotR4z5_j7707Nizi-H4h4RqS06u-FAL6uc2wvRN115gCR1uwMfxCx4g7NeeMe3O60tlRC_ja8z5cCLfjV-gTz_Tm-PVmXXqtBn1oRBbqrk6WAWzXlJV6LaKLNSNBv0qAOqdixm5Lo0w0wK9gMUQz7tUDtlyEQmTzh5tUgIcfkc9RgVkTF8dQpIOmQUc3LHS17Yfi-1m8eJAE6D7HfND2jtvvCdwxfDfIr7nUC7KOK5YzcmYF1vG5pIAb3suKsodc94bDnhEJxfD0UBfev7X9zmMovC-ZnBkjP6p-IxjldwMuXjnGdIjtKZnMpXOhqmMKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه کیفری استان قم، پرستو احمدی، خواننده، و هشت نفر دیگر از دست‌اندرکاران و نوازندگان «کنسرت کاروانسرا» را به‌طور جداگانه به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال ممنوعیت از فعالیت هنری محکوم کرد.
اتهام این هنرمندان در این حکم قضایی جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» عنوان شده است.
پرستو احمدی ۲۱ آذر سال ۱۴۰۳، به همراه گروهی از نوازندگان مَرد شامل احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا، در کانال یوتیوب خود ویدئویی بدون حجاب اجباری، از «کنسرت کاروانسرا» یا «کنسرت فرضی» را منتشر کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76476" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/evH02PSfg9AfGZ09IWN8t2tu398Ze0SuqnkI625WF06VrGdlHlTny2fnJ0TzkItuOWMmJ1El0aQztkXfF-bw614HXOS5IP6ZkHjCNWW2ng0sFehGBqBguoJ_f_GR7-KiwKIqPsW2I4XMAj5rtb2kkfxiv68CJY-EsqWliyidJLxaW_t8W58K8ZrotKCVXvNPSCyHNBaSCc73DVpAbI26pH_kJujN66BZQEr6iEQiZDtO1bG23TJE9R-ufO6O_vHr1adnS0UiHLwRef6NFkVR_loYDyhCsH1WXb_N3sDjdwGV45_2eb7_jyxnDWQzSlbVb_dpb0jdERT_TiLs01QGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره:
ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/76475" target="_blank">📅 05:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YtiPd1dNR3yu8zmNeZuhthxQNEcJloQbQOp9Uf8RsY2KwkUr0q7W6XHfD2F5hy33M_V_fnynkYiV6zmCA-os4qHkFz8ty-T1TVPRMCKWJYC7HUOkXfuRmGK0TVEnWKjLzvDvtiygWvmZAFTHfSXVv6FKNVBTI0yRIZ_WD91VW1Gi-rToqd7cYc173s-8HhOIMU0m_YvGCNUEkvEGjnjgOH3BFxZM4i43_cgaB8IRmq4w6t-jF-WUYHwRA9hoNq5e-9o1U8IXriMlzvcaywqpK96BLT-ppJ288-iPOPbD47GqyfgWPS7E236PeLq0sqaxAj-N8OUoPHadd2DekYetaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درستش کردم
MahvashJebeli
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/76474" target="_blank">📅 04:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hZIZSz-8GxBJSg2Wmkyd7iq3Bkq6FoDsexMjaiAmL_Jsl9rLBKtJz_rJHtBsEPcZz7bh-e2Y0fvivMT7ql59y1ZvSORPSqrdPn03AknDCkbj_jxA1-wTC2wAufUqJZqZBT8epHwOBL5B6NEP0Fk4lwrB0aM8gy4MZVguv1L3KrLagN26zS8CwGStFM-CyJsQH0f5aMJc6FErhn0vhOOLyd6Hhru5bRecUQ--OfIK8U8k9-1mu0dodwKeCPdKJDsF5iXNx1fEmyMZY0PRLXutIImJNhl4vNYq5ULp-m8BR1lm_25KIwmVYurZCGXN51tyjMO-bW88-RaWtSrtBMv4lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ClnFFpfHmfZqjpvH7f5cenA0haHtz98M2CyIXLJ_L5eD2S1gaJnPDgeSwgV5uL2THaktxlyGxOuEWuO1LaVzsMkhv0fx5TVh1_2RpIG_nCsO-53n7qiR7STYKdt16o48k22j0Mkcun-_SGHGlSal9R8xATRXq7LdMXqrRcv-tyR0c7im7DD4rXa9rf_AHRAr7nvqf3pB07XmoOTluQu3ve5_p_xs7MqpqYOIj7iuHJnjsUX0y90xhcyvhUs8wzZGvDEj3NE_chYccVFcoi7T65R__2d2ECVSU1Q5DxBg879XRwK6v2Xw_AohWK4byBIaqZeDYp8pmHGLVexxbhYRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bqk7XIsZ9zrNEwUXnwrZHdxIm2j80sg2atNY_3jsMY30GF_2JgJPBIaylAU1DHY7c-p-qCFcv4p4Ei9oAzvtPZyak7orZr2UYoY7RVT5I8swT90mY6XzdBGJT0zQqW3InSoGLMBc8Naw8OWArMFxHcZf8RSUAIuBWQM3rJfUXEu21GCZO0wdJDOuNF_Uh39cjAmV2LIT7i0hf4HUqGmaftF4lVxhnBFtxtRoz0M8njkKQidBxHyQCrEHEv7v-kZyc5FPQYZd3ogobs5y2PdnuUhQ9T1imXvgXoApNJJPwLzUsck6cY02uX8ybe8P8DprzxYkuNiK6aEhzbFyBTqBWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امضای پزشکیان پس از
امضای ترامپ
تصاویر منتشر شده از سوی ایرنا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/76471" target="_blank">📅 03:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6a09c6ccc.mp4?token=R9ux44rH2nT80WBrmiKtqa3yssczus3yLjKbmRthgH248c5iXXQJWol8PAWVi3RppSkmjEW_y5YkzY0i6D551QhelM7Cu-n2YsIeVPDTUtUP8_vExACsk-t9Ig3xrl1nCCXjprKYs9A_qRuNqxXj1qd1xlDp2s2-V9jWIdqeefPEi0Ua8LniAKSYmACbCPUv6DikAHwq_yIvT14kZHBGudKwE1S80hK172vy2PP7cX74lvPapHZqTe0hozsB9uOqPatQY1bIS7bPUB0ttbubmwYEvHJiKgJxfQfwNTNcPIWEJw1uw4tGeCeIQ0DVjQAeTUDfX4RPYW4attbEXwf1Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6a09c6ccc.mp4?token=R9ux44rH2nT80WBrmiKtqa3yssczus3yLjKbmRthgH248c5iXXQJWol8PAWVi3RppSkmjEW_y5YkzY0i6D551QhelM7Cu-n2YsIeVPDTUtUP8_vExACsk-t9Ig3xrl1nCCXjprKYs9A_qRuNqxXj1qd1xlDp2s2-V9jWIdqeefPEi0Ua8LniAKSYmACbCPUv6DikAHwq_yIvT14kZHBGudKwE1S80hK172vy2PP7cX74lvPapHZqTe0hozsB9uOqPatQY1bIS7bPUB0ttbubmwYEvHJiKgJxfQfwNTNcPIWEJw1uw4tGeCeIQ0DVjQAeTUDfX4RPYW4attbEXwf1Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه امضای یادداشت تفاهم از سوی ترامپ
دونالد ترامپ، رئیس جمهور آمریکا که چهارشنبه شب در کاخ الیزه میهمان ضیافت شام با امانوئل مکرون بود نسخه نهایی و منتشر شده تفاهم‌نامه با جمهوری اسلامی ایران را امضاء کرده است. مسعود پزشکیان نیز این سند را امضاء کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/76470" target="_blank">📅 03:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10e61c88b0.mp4?token=Y70hagDMiIcQReOMgNZXybuZsdH7VROHoW9VoY1cuDQyNqfivZ0jNsU6y5ebVocMdBsOPpahOobv79k60AODb9LBMuK655FqWLoZI-HSZEcjVxkqKwtJsH0FwQkm1kSTA8uHmTHjLyRu-U-KytiXxZaU5F7tJF6sgJ2nZGL8yxNIgyuBNd2ENEi4wV4udaoXKN8dezheZ4Bm7LZipE4cDJ1qMN8KC6o2mVlDyxaf4jI8OVR5VDQdqzsXpCpUqGML2vFbftycV0NEm1mPkDlnoan6q0ztEBeewM-BrNGfxpVSeCBITKTA-nysI26FU2a54ilUD64VxOxWLVCB_hF-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10e61c88b0.mp4?token=Y70hagDMiIcQReOMgNZXybuZsdH7VROHoW9VoY1cuDQyNqfivZ0jNsU6y5ebVocMdBsOPpahOobv79k60AODb9LBMuK655FqWLoZI-HSZEcjVxkqKwtJsH0FwQkm1kSTA8uHmTHjLyRu-U-KytiXxZaU5F7tJF6sgJ2nZGL8yxNIgyuBNd2ENEi4wV4udaoXKN8dezheZ4Bm7LZipE4cDJ1qMN8KC6o2mVlDyxaf4jI8OVR5VDQdqzsXpCpUqGML2vFbftycV0NEm1mPkDlnoan6q0ztEBeewM-BrNGfxpVSeCBITKTA-nysI26FU2a54ilUD64VxOxWLVCB_hF-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☄️
ترامپ و پزشکیان امضا کردند
دونالد ترامپ، در پاسخ به سوال خبرنگاران که آیا تفاهم‌نامه با جمهوری اسلامی را امضا کرده است پاسخ داد: «بله امضا کردم...در ورسای امضا کردم.»
@
VahidHeadline
پیش‌تر
:
بقایی: همین الان که با شما صحبت می‌کنم یعنی بامداد ۲۸ خرداد احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
آپدیت:
توییت شهباز شریف نخست‌وزیر پاکستان
ترجمه ماشین:
باعث افتخار من است که اعلام کنم «یادداشت تفاهم تاریخی اسلام‌آباد» امروز به‌صورت الکترونیکی میان ایالات متحده آمریکا و جمهوری اسلامی ایران امضا شد. این یادداشت تفاهم به امضای رؤسای محترم هر دو کشور رسیده و من نیز به‌عنوان میانجی آن را تأیید کرده‌ام. امضای این توافق در بالاترین سطح دولت‌های مربوطه، نشان‌دهنده تعهد دو طرف به حل‌وفصل دیپلماتیک این مناقشه است. یادداشت تفاهم اسلام‌آباد با اثر فوری لازم‌الاجرا خواهد شد و در نخستین گام، جمهوری اسلامی ایران فوراً تنگه هرمز را بازگشایی خواهد کرد و ایالات متحده آمریکا نیز بلافاصله محاصره دریایی را لغو خواهد کرد.
پاکستان، با حمایت دولت قطر به‌عنوان میانجی مشترک، مراسم رسمی را طبق برنامه در تاریخ ۱۹ ژوئن ۲۰۲۶ در سوئیس میزبانی خواهد کرد تا این رویداد تاریخی گرامی داشته شود و گفت‌وگوهای فنی آغاز گردد.
صمیمانه‌ترین تبریکات و قدردانی خالصانه خود را به رئیس‌جمهور ایالات متحده، دونالد جی. ترامپ، تقدیم می‌کنم؛ کسی که تعهد استوارش به دیپلماسی و ترجیحش برای حل‌وفصل مسالمت‌آمیز، بار دیگر به پایان دادن به مناقشه‌ای کمک کرد که می‌توانست پیامدهای ویرانگری برای منطقه و فراتر از آن داشته باشد. همچنین از تلاش‌ها و کوشش‌های خستگی‌ناپذیر تیم مذاکره‌کننده ایالات متحده، از جمله جی.دی. ونس، استیو ویتکاف و جرد کوشنر، به‌خاطر نقش ارزشمندشان در این دستاورد تقدیر می‌کنم.
احترام و قدردانی عمیق خود را نسبت به حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر عالی جمهوری اسلامی ایران، و رئیس‌جمهور مسعود پزشکیان ابراز می‌کنم؛ به‌خاطر خرد، دوراندیشی و دولتمردی آنان در پذیرش آرمان صلح. همچنین مایلم تلاش‌های تیم مذاکره‌کننده ایران، از جمله محمدباقر قالیباف، عباس عراقچی و اسکندر مؤمنی را به رسمیت بشناسم؛ کسانی که صبر، پایداری و تعهدشان به تعامل سازنده، در به ثمر رسیدن این توافق نقشی اساسی داشت.
مایلم به‌طور ویژه از تلاش‌های صادقانه و تعامل سازنده رهبری دولت قطر در کمک به رسیدن به این نقطه قدردانی کنم. همچنین از رهبری پادشاهی عربستان سعودی، جمهوری ترکیه و جمهوری عربی مصر به‌خاطر نقش ضروری و مشارکت‌های ارزشمندشان در این زمینه، بسیار تقدیر می‌کنم.
همچنین مایلم به‌طور ویژه از فیلد مارشال سید عاصم منیر یاد کنم؛ کسی که تلاش‌های خستگی‌ناپذیر، فداکاری بی‌چشمداشت و نقش کلیدی‌اش در تسهیل این پیشرفت و پیشبرد آرمان صلح و ثبات منطقه‌ای حیاتی بود.
باشد که این یادداشت تفاهم، بنیانی پایدار برای تفاهم بیشتر، احترام متقابل و رفاه مشترک در سراسر منطقه باشد.
CMShehbaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/76459" target="_blank">📅 00:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">"متن کامل یادداشت تفاهم اسلام‌آباد بین جمهوری اسلامی ایران و ایالات متحده آمریکا"
به نقل از ایرنا:
https://telegra.ph/mou-06-17-2
ترجمه متن منتشر شده از سوی آمریکا
@
VahidHeadline
مقایسه نسخه منتشر شده از سوی ایرنا با نسخه  نسخه آمریکایی که بی‌بی‌سی به آن دست یافته است، نشان می‌دهد دو نسخه از این توافق ۱۴ بندی تقریبا به طور کامل یکسانند.
تنها تفاوت جزئی در بند ششم دیده می‌شود؛ بندی که با این عبارت آغاز می‌شود:
«ایالات متحده آمریکا متعهد می‌شود با همکاری شرکای منطقه‌ای، یک برنامه نهایی مورد توافق طرفین با حداقل ۳۰۰ میلیارد دلار برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران تدوین کند. سازوکار اجرای این برنامه به عنوان بخشی از توافق نهایی، ظرف ۶۰ روز نهایی خواهد شد.»
آخرین جمله این بند در نسخه آمریکایی چنین است:
«تمام مجوزها، معافیت‌ها و اجازه‌های لازم برای انجام معاملات اولیه مرتبط، از سوی ایالات متحده آمریکا صادر خواهد شد.»
اما در نسخه منتشر شده توسط ایرنا، واژه «اولیه» از این جمله حذف شده است.
با این حال، به نظر نمی‌رسد این تفاوت جزئی تغییری اساسی در مفهوم یا محتوای توافق ایجاد کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/76458" target="_blank">📅 22:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZogOaUEYzIkwj8f9qr89hFGFj65YHzbuZuIrtBamyyfTSgmuD7WjK7_xegqc5iOPNIRSX2JHkp_P9vZGCjAQcR4ujK40gFkcxe10RmveBbRR_-uzWnLFu2piem89Qr4o1m9a4RJuRMKJdAozMh9g8kDUWM12lcXYmmaIBdLwmpSLJR2O6KmuRnWn6eLGVvdJiXxJTHjgdEk9z8kWN02fVJ2ao_xkDCfWAXhTopRQPopydzEKNaEIQNsOGpgC0DFSAXXGhKM8QrOmgziv7TjBgCXbJY-PFJgA3gfJOECbRmZoT-MKukqDLoFD3nRiEmNkRqDPHWkflDvJaiQofvRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی روز چهارشنبه از احتمال امضای توافق پایان جنگ توسط روسای جمهوری ایران و آمریکا خبر داد و گفت این مسئله «در حالی بررسی است».
به گزارش رسانه‌های نزدیک به حکومت ایران، اسماعیل بقائی درباره احتمال امضای یادداشت تفاهم از سوی مسعود پزشکیان و دونالد ترامپ اعلام کرد: «این ایده مطرح است و همچنان در حال بررسی است.»
پیش از این طرف‌های ایرانی و آمریکایی خبر داده بودند جی‌دی ونس، معاون رئیس‌جمهور آمریکا، و محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در سوئیس این تفاهم‌نامه را امضا خواهند کرد.
دولت سوئیس تأیید کرد مراسم امضای این تفاهم در اقامتگاه کوهستانی بورگن‌اشتوک برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76456" target="_blank">📅 21:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25681b6811.mp4?token=jmLGrGXaezfe3XRZX_SV9MyTyV2lWIzcde6asb-ivmkRB00hrgb2qVg0r7Cfpk-vadQvYskMYAgm-SdxgBnn783yF5pUAGsODkGQdhcGS70Xxq2jhyrfIf-iQCdtiZ24geuNWatyzXgJyHAFyGJcInwrmbHpjEMYRJ0I70QEUmifpLrEgKmcZitKmiz4CsV48UvtefRvVnzIea4klZB9pPFI19wE93ZsS2v3X3eAV3sk-Sc5Y_BgQ8Qs3IAOQCbY0U_rTuy5qcfKCctGFgwfjktV1qYbPsgl2EtudctEiNth9UeCIfoP-e5BMUf4UHne03I4H_AXU9SQp-hr-sB0MSz6kUyS4vuUkKMFkapLa6EYWSbal6PAdT5YQinyCxt2m96WCudD07XCM5WQXxk0hFnOvyttKE7QCnTP0Gppn0c45UduJTMmzsUauSmkE_E8tpSof5kuY6biozbBtZAk65WVSN4umrTbTt7kl8KfEXlC_RMgSeTcj73wWcQZPPSq23i9YsKP-mYbtXFEU-NfmM-_mrdfcY4ksn2JpXIUnYVuilnE_1ETgUrLXnjvxebpXBifroodgVqCgjbr25DloMHj9aWT5xOJd_j-m3jQVKTHBKP8y1CAP7oGm4-RuD9Lyb1o81jp9gcTzdwSZq_SUm-WX-lVyQi1yYgMwX_tQP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25681b6811.mp4?token=jmLGrGXaezfe3XRZX_SV9MyTyV2lWIzcde6asb-ivmkRB00hrgb2qVg0r7Cfpk-vadQvYskMYAgm-SdxgBnn783yF5pUAGsODkGQdhcGS70Xxq2jhyrfIf-iQCdtiZ24geuNWatyzXgJyHAFyGJcInwrmbHpjEMYRJ0I70QEUmifpLrEgKmcZitKmiz4CsV48UvtefRvVnzIea4klZB9pPFI19wE93ZsS2v3X3eAV3sk-Sc5Y_BgQ8Qs3IAOQCbY0U_rTuy5qcfKCctGFgwfjktV1qYbPsgl2EtudctEiNth9UeCIfoP-e5BMUf4UHne03I4H_AXU9SQp-hr-sB0MSz6kUyS4vuUkKMFkapLa6EYWSbal6PAdT5YQinyCxt2m96WCudD07XCM5WQXxk0hFnOvyttKE7QCnTP0Gppn0c45UduJTMmzsUauSmkE_E8tpSof5kuY6biozbBtZAk65WVSN4umrTbTt7kl8KfEXlC_RMgSeTcj73wWcQZPPSq23i9YsKP-mYbtXFEU-NfmM-_mrdfcY4ksn2JpXIUnYVuilnE_1ETgUrLXnjvxebpXBifroodgVqCgjbr25DloMHj9aWT5xOJd_j-m3jQVKTHBKP8y1CAP7oGm4-RuD9Lyb1o81jp9gcTzdwSZq_SUm-WX-lVyQi1yYgMwX_tQP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنفرانس خبری ترامپ
:‌
🔸
یکشنبه، ما به توافقی با ایران رسیدیم که همه چیزهایی را که قصد داشتیم به آن دست یابیم محقق می‌کند—همه چیز و حتی بیشتر.
🔸
اگر این توافق را انجام نمی‌دادیم، می‌توانستیم برای ۲ تا ۳-۴ هفته یا حتی ۲ سال بمب‌های بیشتری رها کنیم.
شما هرگز تنگه هرمز را باز نمی‌دیدید.
🔸
اگر من ژنرال سلیمانی را نکشته بودم، احتمالاً الان درباره این توافق صحبت نمی‌کردیم، چون او نابغه‌ای دیوانه بود.
آنها هرگز نتوانستند جایگزین او شوند.
🔸
رهبران جهان از اینکه ما به توافق رسیدیم بسیار خوشحالند، همه‌شان.
هیچ کشوری به ما نیامد و نگفت «لطفاً آقا، بمب‌ها را روی آن‌ها رها کن. لطفاً بمب‌ها را رها کن» — آدم‌های احمق این را می‌گویند.
🔸
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آنها بسیار کمتر رادیکال شده‌اند. فکر می‌کنم واقعاً کشورشان را دوست دارند. آنها خوب هستند.
🔸
نمی‌خواستم شاهد یک فاجعه اقتصادی باشم؛ اگر این روند ادامه پیدا می‌کرد، ممکن بود اتفاق بیفتد.
هر بار که درباره صلح صحبت می‌کردیم، بازار سهام بالا می‌رفت.
بازار سهام از هر کسی که آنجا هست، از جمله افرادی که روی این صحنه هستند—به جز من—باهوش‌تر است.
🔸
بازار سهام بسیار درخشان است. و هر بار که چیزی شگفت‌انگیز می‌گفتیم، مثل «ما قرار است توافق کنیم»، بازار بالا می‌رفت.
و هر بار، هر بار که چیزی منفی می‌گفتیم، مثل «ببین چی شده، ما نمی‌توانیم توافق کنیم»، بازار پایین می‌آمد — خیلی زیاد، خیلی، خیلی زیاد.
این به شما چیزی می‌گوید.
🔸
من نمی‌خواستم مثل هربرت هوور بزرگ دیر کنم. من آن را نمی‌خواستم.
[چت‌جی‌پی‌تی: هربرت هوور رئیس‌جمهور آمریکا در آغاز رکود بزرگ ۱۹۲۹ بود. در حافظه سیاسی آمریکا، هوور نماد رئیسی‌جمهوری است که بحران زیر دستش منفجر شد و بعد متهم شد که دیر، ناکافی و با احتیاط بیش از حد واکنش نشان داد. حتی محله‌های فقیرنشین دوران رکود را با تمسخر Hoovervilles می‌گفتند.
پس منظور ترامپ احتمالاً این است: نمی‌خواستم آن‌قدر صبر کنم تا بحران از کنترل خارج شود و بعد همه بگویند رئیس‌جمهور دیر جنبید.]
🔸
درباره کشتن قاسم سلیمانی:
این یک همکاری مشترک بود، همان‌طور که در کسب‌وکار املاک می‌گوییم. این یک همکاری مشترک بین اسرائیل و ما بود.
ما یک ماه آن را بررسی کردیم. تقریباً یک ماه قبل می‌دانستیم که او با کدام هواپیما سفر خواهد کرد.
او فقط با خطوط هوایی تجاری، آن‌های بزرگ و پرجمعیت سفر می‌کرد، چون می‌دانست ما او را سرنگون نمی‌کنیم. آن‌ها خیلی باهوش هستند.
اما ما می‌دانستیم که او در آن هواپیما خواهد بود، او را دنبال کردیم، و سپس اسرائیل به من اطلاع داد که آن‌ها این کار را انجام نخواهند داد. و من باید تصمیم می‌گرفتم.
و من به او گفتم، «خب، اگر اسرائیل این کار را نمی‌کند، ما همه آماده‌ایم. آیا انجامش می‌دهیم؟ دوست داری انجامش دهی یا نه؟» گفتم، «البته، اگر می‌خواهی انجامش دهی، ما می‌توانیم انجامش دهیم.»
🔸
درباره نتانیاهو: بیبی نتانیاهو مرد خوبی است. گاهی کمی هیجان‌زده می‌شود، اما اتفاقاً مرد بسیار خوبی است.
ما یک اختلاف کوچک درباره لبنان داشتیم — من گفتم، می‌توانی کمی ملایم‌تر باشی، بیبی، لازم نیست هر بار که کسی وارد می‌شود یک ساختمان را خراب کنی؛ این کار حزب‌الله است.
🔸
نتانیاهو به کشور آمد و از باراک حسین اوباما، رئیس‌جمهور، التماس کرد که برجام را انجام ندهد. او گفت این می‌تواند پایان اسرائیل باشد، و اگر من وارد ماجرا نمی‌شدم، همینطور می‌شد.
و اوباما به او گوش نداد.
بیبی واقعاً به کنگره رفت و از آنها التماس کرد، اما به جایی نرسید. و آنها این توافق وحشتناک را داشتند که برای اسرائیل فاجعه‌بار بود.
🔸
این یک یادداشت تفاهم است. اگر در ۶۰ روز انجام نشود، اشکالی ندارد، ما به بمباران بازمی‌گردیم.
می‌دانید، من نمی‌خواهم این کار را بکنم، چون خیلی خوب است، خیلی خوب.
اما، خب، ممکن است مجبور شویم، چون هرگز اجازه نمی‌دهیم آنها سلاح هسته‌ای داشته باشند.
🔸
توافقی که ما با ایران روز یکشنبه به آن رسیدیم، به زودی امضا خواهد شد، فردا، شاید روز بعد.
🔸
ترامپ درباره اسرائیل:
فکر می‌کنم آنها می‌توانند در مورد حزب‌الله بهتر عمل کنند. نمی‌گویم نباید از خودشان محافظت کنند، بلکه می‌گویم — وقتی دو پهپاد به بیابان شلیک می‌شوند و بی‌خطر سقوط می‌کنند، نیازی نیست ساختمان‌ها را در بیروت خراب کنند.
آنها می‌توانند بهتر رفتار کنند. و صادقانه بگویم، آنها می‌توانند کار بهتری انجام دهند — من آنها را دوست دارم، به عنوان یک شریک عالی بودند، اما می‌توانند در مورد حزب‌الله خیلی بهتر عمل کنند.
🔸
ترامپ درباره ایران:
خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
پس کسی باید به آنها کمک کند — خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
تقریباً هیچ‌کس چنین پولی ندارد — این همان نوع خسارتی است که وارد شده است.
🔸
آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند.
🔸
درباره موشک:
ما در حال کار روی یک تلاش موازی با کشورهای خلیج فارس برای رسیدگی به مسائل غیرهسته‌ای هستیم، مانند موشک‌های بالستیک متعارف، که درباره آن صحبت خواهیم کرد و حمایت خواهیم کرد.
منظورم این است که آنها باید مقداری داشته باشند، چون دیگران مقداری دارند، شما هم باید داشته باشید — کسی این را گفت، «نباید به آنها یکی بدهید»، و من آدم‌هایی دارم — بعضی از این آدم‌ها را دوست دارم، اما فکر نمی‌کنم این را، فکر نمی‌کنم آنها باهوش باشند.
«البته، نباید اجازه دهید هیچ موشکی داشته باشند» — من گفتم، خب، من چه کار کنم، آیا می‌خواهم به عربستان سعودی اجازه دهم موشک داشته باشد، اما آنها نداشته باشند؟ «بله، قربان.»
اینطور کار نمی‌کند، می‌دانید، اینطور کار نمی‌کند، و موشک‌ها مشکل نیستند — موشک‌ها به یک مکان کوچک برخورد می‌کنند، اما سیاره را منفجر نمی‌کنند.
🔸
اگر آنها به توافق احترام نگذارند، یا برخی موارد حتی در توافق ذکر نشده باشد — این یک یادداشت تفاهم است، اما ما درک مشترکی از برخی مسائل داریم بدون اینکه آن را مکتوب کنیم — و، اگر آنها به آن احترام نگذارند، احتمالاً دوباره به بمباران آنها باز خواهیم گشت تا زمانی که به آن احترام بگذارند.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کار می‌توانند بکنند.
🔸
مردم می‌خواهند من پل‌ها را بمباران کنم.
من قبلاً این کار را انجام دادم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگ‌ترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن در ایران.
اما ما آن پل را بمباران کردیم، شما دیدید.
🔸
می‌خواهم از چین، رئیس‌جمهور شی، تشکر کنم، من با او بودم و او کاملاً بی‌طرف ماند، کاملاً بی‌طرف، و من این را قدردانی می‌کنم.
و می‌خواهم از ولادیمیر پوتین تشکر کنم، او بسیار بی‌طرف بود.
🔸
خب، آزادسازی پول‌ها — پاسخ آسانی دارد.
ما مقدار زیادی از پول آن‌ها را گرفته‌ایم، و پول آن‌ها را از آن‌ها گرفته‌ایم.
وقتی پول ما نیست، پول آن‌هاست و ما در یک زمان مشخص آن را مسدود کردیم.
فکر می‌کنم باید آن را پس بدهیم، می‌دانید؟
اگر پس نمی‌دادیم، هیچ‌کس دیگر هرگز در دلار سرمایه‌گذاری نمی‌کرد.
🔸
گزارشگر: یک مرد دانا زمانی گفته بود، در ژانویه ۲۰۲۰، «ایران هرگز در جنگ پیروز نشده، اما هرگز در مذاکره شکست نخورده است.»
ترامپ: این را چه کسی گفته؟
گزارشگر: دونالد ترامپ.
ترامپ: اوه، فکر می‌کردم همین را می‌خواهی بگویی.
🔸
اگر آنها پرچم سفید تسلیم را بالا ببرند و بگویند «سپاس خداوند را که دونالد ترامپ بزرگ‌ترین رئیس‌جمهور تاریخ است»، نیویورک تایمز و سی‌ان‌ان خواهند گفت «ایران پیروزی بزرگی به دست آورد.»
🔸
راستی، محاصره تأثیرگذارتر از تمام حملات هوایی بود، جایی که ما بمب‌هایی به ارزش یک میلیارد دلار روی ایران ریختیم.
🔸
گزارشگر: چرا حالا برای شما قابل قبول است که آنها بخشی از توان موشکی خود را حفظ کنند؟
ترامپ: آنها چه چیزی را حفظ می‌کنند؟ آنها اکنون کمتر از دیگر کشورها دارند.
ما احتمالاً ۸۴، ۸۵ درصد از موشک‌هایشان را از کار انداختیم، بقیه زیر زمین هستند و حتی نمی‌توانند آنها را بیرون بیاورند.
🔸
ترامپ درباره ایران: آیا می‌خواهید اجازه دهید ۹۱ میلیون نفر از گرسنگی بمیرند؟
🔸
خبرنگار: آیا اکنون می‌توانید بگویید که آیا کسی در دولت شما بابت حمله به مدرسه‌ای که در اولین روز جنگ بیش از صد کودک را کشت، مسئول شناخته خواهد شد؟
ترامپ: اشتباهاتی رخ می‌دهد، جنگ چیز زشتی است، می‌دانم که در حال بررسی است.
من از پیت هگست سؤال می‌کنم چون آن‌ها در حال بررسی این موضوع هستند.
🔸
خبرنگار: چرا برای مراسم امضای توافق صلح ایران نمی‌مانید؟
ترامپ: ممکن است بمانم.
🔸
گزارشگر: آیا در این موضوع عنصری وجود دارد که شما معاون رئیس‌جمهور را بفرستید، اگر موفق شد که عالی است، شما به عنوان کسی که او را فرستاده نابغه به نظر می‌رسید. و اگر موفق نشد، تقصیر معاون رئیس‌جمهور است.
ترامپ: من این ایده را دوست دارم. خب، به این صورت، اگر موفق شد، من اعتبارش را می‌گیرم. اگر موفق نشد، تقصیر JD است.
بهتر است مراقب باشی، JD. او هواپیمایش را برمی‌گرداند و از اینجا فرار می‌کند.
بله، من این ایده را دوست دارم. فکر می‌کنم ایده خوبی است.
📡
@VahidOnline
بخش‌های بالا رو من انتخاب نکردم. هم‌زمان با حرف‌هاش از منابع خارجی با ترجمه ماشین گذاشتم.</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76455" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
