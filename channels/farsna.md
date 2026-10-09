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
<img src="https://cdn4.telesco.pe/file/jnf4tpVuUsnUQFVu6JShczmXpIGXudOhGoAhkuqF7oTInQ43GtsEtKoKHZPZxMQiU_JYqxc4pWISiWx4s16Gy_h3RbtMz3hnXwxyj2CTu_XX7Jj8dgMmSdp46Zpl2vP1URq_lJzY4yz9LqVBKU0fuPmkQPBrltDvOY_uc1LGLzjTLrh9Xpzn_wDH9gzwjkTzMtehrY8w5sNXim2OqPuSimwjB98t6LBwOxW5vfDXP2TmryZ--4P7rgbW_wyTJxHGsGDAWjPmeZEVyaGHCmaAHkhC8HwcEc8bcVdQ3aDtJfM5adjT1wBwLgcoxJ8EMnxR2CwYRekp4mOn7eeePZ1BzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
<hr>

<div class="tg-post" id="msg-467381">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAuNN9SygSVSpwRgClG3mvaDPmYiWUaMRmRCc54yBkC0WLXg3Av2KMnRVbg7xjRkvekxm7OxeEpbQ_ozhYkrREssJXzv4MDyMAcgPmD82OgUt0Z-CCfyeiafJOJPAfO37hmfCi4K8jwPKtvK9DlWCaJgLKKiiJRiuD5bWtRAZ3B5vRT_ZQELvSuMD2Q1X47Oa4SUbd4-gQiEbkrin_QdD9aJIwulV1ZMyuDY0Z2RPfwa_IoF5wCEE0gDq-rigaj3fzPkS6jpjGv4c2_Nxk9_3u1lSwKxXjwXg2Sr4hEFCeoldilsAQU4dhrkNGJSfW_7kwa2qNWWqERsMXU1COcjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-8ihuj7p1ilMKf2MPGtyv6xSoWG7E23maytvI3u2GQK7g8zozh3Sm-wWN2sroBKsXEKFrg1x7kQLKXnwEb1-ZFN8uVBSfT6Q2IJ54z2FOeqVjHfevxMzMQKydbS_pAqtOktiFmPSRUWaG2XrXOvgythGtAwFIaNjULb1YSJzmYN8Myx3ie_YHJHGFlxw_J8FItsZCuLPat6qqanslIqq_D_B-XV3j-Q2CknyTfR4Hy0NLc-uQCqvvVYu0juZyZTQvJnaNUfF0PPi4nQhUpbvEHgy6d70_qToAoRXTPN3YUH5i2Yh0H-jvMYpFsClCKTC2SkvICYxXEarqNUlq9rUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EK3BR6a2roDEm8DKqClaWetuTh-IJR3ZoFvT3BlSO6qV5OFcnpyxk_2ItlOKylNsMEvEFmZO6_V74ZeiQ9B56LwIxhPi83dDWefzKepVcNZ9bibOKYlq6enaVDZpguzR3cXDLNRCyus9hH9sfbPRVfOe85Rr3fvS6adndulMqkhs-PNsPXJzZsO1pNLtioXaejZY8966tIHQVGamrNskYbmHUWARyeqHrrMBNnU-fAQHN9UPTLo4Pw591Pt2m5_n-DlyCpmPhkDzeTfaKQjhfFHSYPEfIFAHQcNC_qeaxGhm8YGMzR0VY0JGgspSdh_50GsZlMx7D5YvNIuABTyeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eH4C-07mtYu8052zgZ_gnWOmb_OSMvToQlKeYLeMFNHkiff1NAHwbLkqxsKQnKTZOyIgdZ7XqhU3gcohXL_eHjKXzu08Zg3CQayd95DGxmM07P3FbHNBZGwqzQ2iGmCC_4NcsYgMpXL_2r8Xb_xMND4u3EJzsB2PnfX_wTAQL7Gk-r5Re6yLSZHn29pWdoISDowuIq-Hv5dA7iMjWtoF2AlH82e4bhAqmmCBVFXgNwzweZCRw-RYUcW252SNGZbMJulvFXGw6DJ5DDQLbBm4sa-X19ENJ_x2oYK4ESt1MwVsFBgbN23vUnMQjEpoiYe888iqn3aMT4FS-Im1KhqLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_sFsQqmKEGT8innfA2ACa4cZlxUXURj6XZuuLU-v4u6BM939dQskZFGwPavLfJ7SX4PiJ6R-1uqzQMbtUjOPFxj56gy5xi_uRA114vre86a5TWd-Ncm39fPRPgYpUEp7DLDWO6MsZCJ326XtUZGCI6SBDI2ul5Ideas92vFYg36QECLrfCRCspr3UjW2MeHORrS-fOUua3hELCcS0prDve27a91OMG0b_HfG-28otIqsZsD8PWkHv39P5WRlYKw7GOA5y9_agI4WecK5OC_5dxfNQ2pf6hW8DL96_9gsCwlb2Jt1rHmhK92q2pVwLmL0qLHUaha3QHFUnlaH0A1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dI3wSg2qCmCbyvFGazSpG4KJ-Ji41ogIdKjsP6kb7qe4hQDPlDDD9osOBC0mysmIzPTZMia8IomMFlKkd_WSsBMzDiAg0Tul1Kd6LpDnfR90f5Ab6vFn_PhUDFR-TaC-oAfuAQEh0HfgDv7SlliK3OE8XDHX0y_X_UtRVO2eEfA3-YefeJgYgGWBtsbovpWICLxjUKaXLDtg7RCSAtGuRqrogy6DVLZICMxLUAT4cWaf4N4eh7p1ULCs37TbBhFJ7-GHt8f12tkUMCNOsCyP-lMyZdxf6OrkYItOllXd5yc9Y1y8oEd2HIWMggMj5owbnQ4ylnsCNtMWWD5iMBKo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLbIUB8B4sI5f5j_8QN1gsmSfRcqQGHxJSShoDK3u4T7r-pklP5QZK-xNv_kmhoww-x7Qw93hFCp5EiG_T0sL7YSHyNmiT_YDIluAU1g1Wp00SEHoid9-RlnN_WijLXBTWPxn7uWUyE9dErYzxP9TLn037U72hSk0qRDHRU8Nkf2-EHMP4v_Wt-p84CsTrth7VviU-fEH89Vt_Rw2xUq7OmysArrtNdwum-qutROdC7farYJ2ixbgEZWwsO8WtW5rFBPbXuMFKvyoN3a_qFiWyJFJYnL2tj5HVe9pjONX9Y59sERTrcGWj-4PWrp7Ka7wznSAaO8z1J8nfjwOZbi_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گل سوم برای پرسپولیس؛ اورونوف در دقیقه ۸۵ اولین گل فصلش را زد
⚽️
پرسپولیس ۳ - ۱ صنعت‌نفت @Farsna</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/farsna/467381" target="_blank">📅 23:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467380">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvX8w6TkHano7gxIb8Hb9ZxJYS-eru276RSpkMXWcMyWh4UbNd9gmtBs33YL2qmf6Z2yYSLTT9qDrUJonaUd3rxwE5E_tRPI6487F4vqmq194sijE2OFnJY2RI6E9HBvBtWTs_cBeLk4csRoLoIOydlyCn4P6w9isjKSAcP9y6bQbQNnGUV57XF1JAeqkSjYnBowMeUBxCs_SGqBMc5UnNQNnzNNWiMOsSuV4BQ5BmOPmJu_G_cJj3AuUmFmWLtzBFkYLjd3jqtXmLQo-x8jRq7z_QdAnUxVn1xSgh97hx1AHNnLbPqHryw2CK9gMg45UVPR5h_Rm6-7VBGqMZlteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کابوس ترامپ به کف ۴۴ ساله رسید
🔹
ذخایر راهبردی نفت آمریکا در تازه‌ترین آمار رسمی به حدود ۲۸۳ میلیون بشکه رسیده که از پایین‌ترین مقادیر ثبت‌شده در بیش از چهار دهه اخیر به شمار می‌رود.
🔹
بر اساس داده‌های اداره اطلاعات انرژی آمریکا، ذخایر راهبردی این کشور در هفته گذشته با کاهش حدود ۷۸۴ هزار بشکه‌ای به ۲۸۲.۹۸ میلیون بشکه رسید.
🔹
این رقم در مقایسه با سطح حدود ۴۰۶ میلیون بشکه‌ای در مدت مشابه سال گذشته، افت قابل‌توجهی را نشان می‌دهد.
🔸
کاهش ذخایر در شرایطی ادامه دارد که دولت آمریکا با فشارهای ناشی از اختلال در عرضه جهانی انرژی و نوسانات قیمت نفت روبه‌رو است و ترامپ با انتخابات میان‌دوره‌ای آمریکا و نیاز به رای مواجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/farsna/467380" target="_blank">📅 23:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467379">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU1FYdDR0HnDzxspkfLeY2rYoB0meUISLf3HYZXmCx61psYsZNgXiTewu2IQXweBtVb408UHlE71BtZhnIwu5ZnUE1Mn-vWR1gfnqsm5LXBrJBH2Qg9WDBm23e4gEu-Yrl6Vw2Dfptfquo9i_hCkHVIB6HWAc4rjb1zG2wHzeGrAN_qBWDY-iQfpd88MfUE2iQzyfZbGj3SFuPR9a8eGinQpDKPSHKXAOvpAXwn9XAqa31tq_fJ9Dy1IODqGEcL6Cksbn4aKTfPwb8XQ0NpNsp9A_fTJwnF3ppFoqCiKUSlga13gSI5NKEORD4JO30GFwmWdrgwCJhjtuEFBngpcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ دربارۀ توافق با روسیه برای تأمین گازوئیل
🔹
رئیس‌جمهور آمریکا مدعی شد با پوتین توافق کرده تا مسکو بیش از ۳۰۰ هزار تن سوخت گازوئیل در اختیار آمریکا و بازارهای جهانی قرار دهد.  @Farsna</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/467379" target="_blank">📅 23:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a40913d7f.mp4?token=VCApqXnDbhRlI6-9SsFinTD1KBRyOS4zqvKVnypzK3iCp3G5UMmtQoTsdbtsfKcSYIxpcA74h5sOn27tPbczRP6f1-sKPKtJIuZZ-8EpfikL7MdZQBIRRt8UFoMgW9mUOvZe8GSjgHitFCGKbyr-CjhFUH77U00iXznavud8Sm2-P0ecCtJWzr7DaRXvreobKdJ7wk2_msr_SdE_iX90OvczHWTIFb0ylvH-hkp4-tfl1YA4wY1o7SdBwdeL2SvcLQAN7He9ozzftjIllVXRkJJBc4lcBxSf81jmLLZ4wvACDGnWrdf8c9OT1GhiAO1IxnJl1Afm3p1EUs2wx-WzIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a40913d7f.mp4?token=VCApqXnDbhRlI6-9SsFinTD1KBRyOS4zqvKVnypzK3iCp3G5UMmtQoTsdbtsfKcSYIxpcA74h5sOn27tPbczRP6f1-sKPKtJIuZZ-8EpfikL7MdZQBIRRt8UFoMgW9mUOvZe8GSjgHitFCGKbyr-CjhFUH77U00iXznavud8Sm2-P0ecCtJWzr7DaRXvreobKdJ7wk2_msr_SdE_iX90OvczHWTIFb0ylvH-hkp4-tfl1YA4wY1o7SdBwdeL2SvcLQAN7He9ozzftjIllVXRkJJBc4lcBxSf81jmLLZ4wvACDGnWrdf8c9OT1GhiAO1IxnJl1Afm3p1EUs2wx-WzIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: یحیی گل‌محمدی به تیم ملی امید نزدیک است
@Sportfars</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/467377" target="_blank">📅 23:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBMSHrQyfWHor9AOaNbi95GE1Ww9Ql2iiHFKa-81qYLp2YSYc3_Tg89et5Zh-b8xIh5akyWPJ1JXQU-04-YfQFObOAU7RZuCiW1Y-wKHHjN3AHwIZLRIa29Ff_VBEJGebiy56_Df8isZT53txZqYssSvYRzlUgA75phn7CKuZ4Nx0ZEKvtLCGMzyzBHdBzS_vhzqURhOsL2UROz7nLCbOoyA20vGjsQjQjCxH_wq3wOJf119Hk9xn8IRYvz9vHf1CsT2rRUYkVcpA_-ZNksQq8JXGmeTnD-xkUyn00i8G7rLM0h3DoZoGrsWxll9T8moT57qPqIhNJ9ayKDWdTz04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه نهاد آبراه خلیح فارس در مورد وجود دامنه‌های جعلی
🔹
نهاد مدیریت آبراه خلیج فارس: با توجه به برخی گزارش‌ها مبنی بر سوءاستفاده با دامنه‌های جعلی، تاکید می‌شود کلیه مکاتبات پی‌جی‌اس‌ای از طریق ایمیل و با دامنه
PGSA.ir
صورت می‌گیرد و سایر دامنه‌ها فاقد اعتبار است.
@Farsna</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/467376" target="_blank">📅 23:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls4BHMF2hEnbehwuCB59M7CSjec5Z5kIzqD834pFufTqCzkFuOkdb9EinuIPIVJfeca9LlonUwenQWk-w65VQ-Kemi0CiCImIIQx79ufEkpgWZBLSPqVqZxDN08UAd-LMYJwJ8WoRndleV-eQTse9AXxu7sKv8srWOt1_t4Sp04Uy0O8naKpiJoF6QmP4kqmdklUSbx3yfA_pcHf0GgCL3aVS1yNvlY5alX2-Fp7VnLfy7XRVT1vY504u5t3XKjvutZhfr7McWDofJEVi7venfI7VkucTk1C7w8CmkpkVDBuS8_uDUnjvugCfIzhpzHwt5vGu_CZndM4JVSN4yzOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: کشتی غول پیکر حامل گاز ال پی جی مورد اصابت قرار گرفت و دچار آتش سوزی شد/ مسئولیت تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست
🔹
نیروی دریایی سپاه: ۲۲۰ شب حماسه حضور میلیونی و ایستادگی و پایمردی شما در دفاع از حق و عدالت دنیا را به…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/467375" target="_blank">📅 23:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxHXtYNWryxVRQHvlnzfkhJp8TAYOkaIMSFgRDjyAFg8sYrA5nRiFU4_jLmiMHkq03kpQcLKZXwl1FkC8TJ5DBg7mImDmopW0QgdpY2eyH85XYQA7bVL9c3GFPuDOhronT6qowgyrIGeHJkbBNU-30t-SOH9ZHsSlMiu76dZMqmjDi9_ksW4QBw84xhWD1Ug-0UViEsTgjAyAstAVxRG-0fcIG2jslvBUVxkZrE92ZZ977M1H8ZWihRQadNTV1fAcqBMMFnYxTyPHXrUyw0RXui1K6bZZ5_hjKE1ccd5gCSW61lRIoT_OWbwvh1KEiLrZXFScJo8i1qmfh5rYbCyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مسیر فرار نفت عربستان از هرمز در آتش سوخت
🔹
تصاویر ماهواره‌ای جدید یک ایستگاه پمپاژ متعلق به خط لولهٔ راهبردی عربستان سعودی موسوم به «شرق–غرب» را نشان می‌دهد که درپی حملهٔ پنجشنبهٔ گذشتهٔ یمن، به‌شدت آسیب دیده است.
🔸
این خط لوله حدود ۱۲۰۰ کیلومتر طول دارد…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/467374" target="_blank">📅 23:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467373">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2407f2c6f.mp4?token=O4FWpIhRoPOWmIDKUI1TZ572lmwrCBeQoe_w_2uKLwds-H5SV5H6ce0Lp-EjDOIiP5aVeopJ6NcuHlHdyiJhANBscpOjaJ3FF6iyPE5NEmc97n7DBb-jn5YtgboqRjDGAJYSNxYEDXiYWW6DO9xs2lx902dtfhrxQkKFizxrd3wztVm8xlOXy2GGdybUl9x5tOiXGXpJN9R6IFfvYidSKq6zqWvPVUpuTv_KtbWuMItB3RG22LYb9pPcB4Y6QWt_ACqIIIZNJ4k-ZF3SNmVYk8ap1U_MMGUafmgsznIzHako_bLTAkUIY2ey_gN1wDtd_G8zfg5khFzqjELK0nCjD7UuDfR2Ijt_vfyQr41-tB84-BZV5g-CGPlyAXhDELmQzLk4Hy9aLAuLJC5oKE0RoXaqdCYn4r2SYj37-Zp54fb64Vff-nTEPt7lJnzqH5yJXkLeknne60fB3yz0uKhu_23LFASETc7YAZVKh4ELHwpNlvt5J7CsEjIcvk68SM2e6Pa-PaY0rsLpSEXc6dakGcb9auEGZETXCoE7HUrIq2AH_YdEkpHRHob7lq5dLDWxIh-RebspejWMQyVvlgz30oFxC3QDMJKW4XbExe0zrZEk1Hn2GMuwOLB8lUT23jGyTGmjlUlVeibae7cQQWF5XCVzGj2FRhF_nkiIZfZJCT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2407f2c6f.mp4?token=O4FWpIhRoPOWmIDKUI1TZ572lmwrCBeQoe_w_2uKLwds-H5SV5H6ce0Lp-EjDOIiP5aVeopJ6NcuHlHdyiJhANBscpOjaJ3FF6iyPE5NEmc97n7DBb-jn5YtgboqRjDGAJYSNxYEDXiYWW6DO9xs2lx902dtfhrxQkKFizxrd3wztVm8xlOXy2GGdybUl9x5tOiXGXpJN9R6IFfvYidSKq6zqWvPVUpuTv_KtbWuMItB3RG22LYb9pPcB4Y6QWt_ACqIIIZNJ4k-ZF3SNmVYk8ap1U_MMGUafmgsznIzHako_bLTAkUIY2ey_gN1wDtd_G8zfg5khFzqjELK0nCjD7UuDfR2Ijt_vfyQr41-tB84-BZV5g-CGPlyAXhDELmQzLk4Hy9aLAuLJC5oKE0RoXaqdCYn4r2SYj37-Zp54fb64Vff-nTEPt7lJnzqH5yJXkLeknne60fB3yz0uKhu_23LFASETc7YAZVKh4ELHwpNlvt5J7CsEjIcvk68SM2e6Pa-PaY0rsLpSEXc6dakGcb9auEGZETXCoE7HUrIq2AH_YdEkpHRHob7lq5dLDWxIh-RebspejWMQyVvlgz30oFxC3QDMJKW4XbExe0zrZEk1Hn2GMuwOLB8lUT23jGyTGmjlUlVeibae7cQQWF5XCVzGj2FRhF_nkiIZfZJCT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا خودِ مردم راوی ایستادگی و مقاومت‌شان برایِ ایران هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/467373" target="_blank">📅 22:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFJpp8jB0Wx23kqP0t5_oAU7O7zVFbGbeQzBmMBuTTNNcuv336m-ezlTh3FuxCcF3Lo17j04bc9fZYlLMiRdCrp4eZgPC4x6cCcLPH1aVUfmDPOlThyEztP-yRP-_FhW8rdg-rXhijE-f5CsUz9_OEItJQM1__hwZNKZritXIXWAvZb9ZoX2lHGjfiQ7MsE3iJEnKXiAwJMUtThu4BvGxLaQ5ODggXxdlTbFx1BD9qmZqb3Ciwu5NmYwikApH-9P9fvCeWduQwLzfuyMypQumlBMlKTslBVoiD_5GZJlF10r_3jsApAttKb6Lf4oHz1FO4Q5sxzxEqSUhyCJBwHaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حالا نوبت دعوای خطیر و کریمی شد؛ جروبحث دو عضو هیئت‌رئیسهٔ فدراسیون بر سر تمدید قرارداد قلعه‌نویی  @Sportfars</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/467372" target="_blank">📅 22:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maJA_zalTWhCPp92YfY7qECzZ6LLT5jKFKvYcEPnN5cZPMawwt_PIY3969MmwmLR7Nw6lKH5DKq0I1tfpTTNbemI7oOZGbhTPCWMd9CrMs2E4KF7UPPoXIXiUEuTOZCbuXYYZja6gbi9Ua9o8riUpVeaVoRBQPNS01_q-XJxrYFy-R1gJi-DbvGOElK2dzsGKR2aM2FRZqVPqUEmv6iUMeUyZLplxthV2J9mPv_75Z79GWeCky3YquqmPL4Xxs1Ff-aUBj72jxJPpoOTlAAb6lPL7DqGgmTYNSow247r3xLbQ9Jy9ZhzlbDbjczQ69MW4tePY2oetnJQF0D-hckcKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف در پاسخ به روبیو:به سرنوشت والرین دچار خواهيد شد و زانو خواهید زد!
🔹
رپیس مجلس در واکنش به یاوه‌گویی اخیر روبیو در مورد تمدن ایران نوشت: در طول تاریخ، ما ایرانیان با کسانی روبه‌رو شده‌ایم که خود را سروران جهان اعلام کردند و کوشیدند تمدن‌های کهن را از صفحهٔ روزگار محو کنند. آنان با آتش و شعله آمدند، اما با گرد و خاک و خواری رفتند.
🔹
کسانی که به دنبال میراث اسکندر هستند، سرنوشت والرین را خواهند داشت: زانو خواهید زد.
@Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/467371" target="_blank">📅 22:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c65ad3179.mp4?token=P_U_mz4r0bwvwrAWFkjQSvxWSuH148FgpluncsVSPjBXdR2WPz0Eu9zait6o-w4QGrVo1VZcfPX5mgdztbCKazxi4YQv0ejGEqs-kFHSMKAO-GrJjFhQbj8fqBligdZ1WBFaby0u-6wmAaqgQ6d35ku4pgId_NtstFn7dzHzmlaPQBcaihdaEKy7fUgWFXwYDgXpSZLiIyXOFTNl6hMUna1BgKt8ruo2p4ye-CsqjnexeBecjucpuhIRhU4T-kjUe2tYqBTo-g4AovCrm5wruLLGRub6JiCGl97xGqhr33-ncRauTTBxDH64Or7VGFgWIWLPupaCS5Auf2T20VDy-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c65ad3179.mp4?token=P_U_mz4r0bwvwrAWFkjQSvxWSuH148FgpluncsVSPjBXdR2WPz0Eu9zait6o-w4QGrVo1VZcfPX5mgdztbCKazxi4YQv0ejGEqs-kFHSMKAO-GrJjFhQbj8fqBligdZ1WBFaby0u-6wmAaqgQ6d35ku4pgId_NtstFn7dzHzmlaPQBcaihdaEKy7fUgWFXwYDgXpSZLiIyXOFTNl6hMUna1BgKt8ruo2p4ye-CsqjnexeBecjucpuhIRhU4T-kjUe2tYqBTo-g4AovCrm5wruLLGRub6JiCGl97xGqhr33-ncRauTTBxDH64Or7VGFgWIWLPupaCS5Auf2T20VDy-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم رشت مثل تمام جمعه شبهای ۷ ماه گذشته نماز استغاثه به امام زمان (عج) خواندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/467370" target="_blank">📅 22:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467369">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شهادت مامور فراجا در حملۀ تروریستی در فاریاب کرمان
🔹
سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش درپی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب، به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/467369" target="_blank">📅 22:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467368">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYDSYNOHGV_HNQskSvgqCkeKYuDpsOf87cxcM_4lm3FmQsQxYdF_P1Rkeu-BwBhR2ei6PB6PXVh_OSayjEPn7SidmX9C9VeRJ7PhGx7MC7DXM7KSyAnjOSZKVceiV3tCrr6vlF4tkTbR5m0CErr2hzBVKbpgznOmLsfsPKM6PRhArtR7_S726sICF6FcGqVsID6d2AUrP_tLgquo_reqyI6NVOLC4BzE8ZrTE-v65fchOs0btuQjl7RTHVD8jSNDGLajNLTShR3-F-mw1bH_XE6R2_cBQD3hTNFfTz_PI8-M41owycriZY2LmEONNl8-dmMNQaEUumoluKUMYAvkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ دربارۀ توافق با روسیه برای تأمین گازوئیل
🔹
رئیس‌جمهور آمریکا مدعی شد با پوتین توافق کرده تا مسکو بیش از ۳۰۰ هزار تن سوخت گازوئیل در اختیار آمریکا و بازارهای جهانی قرار دهد.
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/467368" target="_blank">📅 22:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467367">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8698bd0285.mp4?token=Olo9_324RvL_TJ22bK4lNw7LNCrW_IAOpi1P517jjSYGCwvlNXjCOeo4zx8Bp3vBTEa1w4ut5Lk1ZjFm5gtotebeKZhBGuGbkIO6HDMFLDos9Sr3M7lDRW2heLQczCjmqJGY6vqa_HxM20z5ZJlqEEkCFCo8iwKsFio8fgyg-raM9X2_5gxWwb-nxTRz9yTNOyLUOMvRU9K3gzEcX-3RbiH2xdp0Z_BDZcrfIfCPBhtbGquSQYRc2OAn6obrzF64vVL_ZRahor4oexnYgt3ItF6-mpvg8oYoExZ5YMpZd5WkpqR2L1ZTxBHIciHK95CzaBjrLhXcqFeQbS_KQPc89w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8698bd0285.mp4?token=Olo9_324RvL_TJ22bK4lNw7LNCrW_IAOpi1P517jjSYGCwvlNXjCOeo4zx8Bp3vBTEa1w4ut5Lk1ZjFm5gtotebeKZhBGuGbkIO6HDMFLDos9Sr3M7lDRW2heLQczCjmqJGY6vqa_HxM20z5ZJlqEEkCFCo8iwKsFio8fgyg-raM9X2_5gxWwb-nxTRz9yTNOyLUOMvRU9K3gzEcX-3RbiH2xdp0Z_BDZcrfIfCPBhtbGquSQYRc2OAn6obrzF64vVL_ZRahor4oexnYgt3ItF6-mpvg8oYoExZ5YMpZd5WkpqR2L1ZTxBHIciHK95CzaBjrLhXcqFeQbS_KQPc89w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خون‌خواهی امشب هم بر دوش مردم گرمسار  بلند است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/467367" target="_blank">📅 22:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e9475d72.mp4?token=jp1gfgUq2H0120dNBOHq0nNa3-jLbcoyfBXq0rCtkTFD677gYNFkf-FtN1yLHcnwXKY4nLfq2J4flj2pEfjdDw1v_k6grgPbP45X-Rpp0eFcU2Idof2JO44QIdqqD5VF8R9qj1dX26p5gOkVBjTe6GYlC8XHIeblkr2B4Bq42zbesb_A3_iYG2jiW0LyycgUKALXOIx6GmNPhgygo6UJaqtlnqjngi5ha7ks1b2Ks-dmNSMXboR57p2D66TYxapzhXU8h7ZkE8j5kWnVth3fl_fL_H5QS93341J8pptnLmnonfdkrcSMSws9azFo7R0Rrk23JwIM4Tx8b-Z-NhGm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e9475d72.mp4?token=jp1gfgUq2H0120dNBOHq0nNa3-jLbcoyfBXq0rCtkTFD677gYNFkf-FtN1yLHcnwXKY4nLfq2J4flj2pEfjdDw1v_k6grgPbP45X-Rpp0eFcU2Idof2JO44QIdqqD5VF8R9qj1dX26p5gOkVBjTe6GYlC8XHIeblkr2B4Bq42zbesb_A3_iYG2jiW0LyycgUKALXOIx6GmNPhgygo6UJaqtlnqjngi5ha7ks1b2Ks-dmNSMXboR57p2D66TYxapzhXU8h7ZkE8j5kWnVth3fl_fL_H5QS93341J8pptnLmnonfdkrcSMSws9azFo7R0Rrk23JwIM4Tx8b-Z-NhGm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گناباد، شبی دیگر در امتداد ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/467366" target="_blank">📅 22:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06b82efe1.mp4?token=iN-Hw35smnr6Pvay4MkqYvZtQlKyVtob1KQf5tU0PkNXAVIaW_CcfgbIaX10NFi2x8a-Xu2IP4iC2V8LbfWtQhzFBw0phGAoDqgpwt8duJVUIU9XnKKn9wgS3GKtuX3aOHxVwkp3E7iRXpzLTKX1AzP8kCGAy68A4ediRvgAyB-oAv9V3P3AjnTEeJ-W44qvGWRM1NGIRpDT2KvnvIawRoI8IGjxKD735-E-2Kt5JM2cTilVR0_25UiSsUxH0MK8nSVJ76mjjuPd4PlE2A0ztGKwsxg2KGVCojHYd2l-rR2ORtFQzkH3e2jKh0q1_LJ5PfleblmT2U1EGEkl4NTlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06b82efe1.mp4?token=iN-Hw35smnr6Pvay4MkqYvZtQlKyVtob1KQf5tU0PkNXAVIaW_CcfgbIaX10NFi2x8a-Xu2IP4iC2V8LbfWtQhzFBw0phGAoDqgpwt8duJVUIU9XnKKn9wgS3GKtuX3aOHxVwkp3E7iRXpzLTKX1AzP8kCGAy68A4ediRvgAyB-oAv9V3P3AjnTEeJ-W44qvGWRM1NGIRpDT2KvnvIawRoI8IGjxKD735-E-2Kt5JM2cTilVR0_25UiSsUxH0MK8nSVJ76mjjuPd4PlE2A0ztGKwsxg2KGVCojHYd2l-rR2ORtFQzkH3e2jKh0q1_LJ5PfleblmT2U1EGEkl4NTlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترافیک سنگین در دو مسیر محور هراز
🔹
حرکت خودروها در مسیر هراز به کندی در حال انجام است؛ حجم ترافیک در مناطقی همانند پل لاسم، گزنک، محدوده آب اسک، بایجان، منطقه چلاو، تونل سپاسد و نارنجستان بیشتر از دیگر مناطق است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/467365" target="_blank">📅 21:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467364">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d9e35815.mp4?token=L1WaEyXHxXNaadg-ZtTDcfb_e--Ycij199FuhMUKjR1kooPC_YrYst374oynhPm64xqZkJxUwRExJYB16RvAu1QnIcHjqzImykICEhpg-YE8Q_eZ2R1fuxGAv1MNQg47LtJKW8sypuJKHJqwTUAid78Twtu8018Q1LHGnXEN7iqL5-VFtgKMEoP5BQsxjhR6lkH3Q_K9AAJrXxyrQITeeXx6d-nrn2GpAaKNNIXJsNa1ZyDUWvMKYBsA6wlEwd0_P3YqPXjTx3cE4TvGyfDOzTyHfRKdy1lZtljsxNaNqUTyjBFjqEOpm3z3HFClAktxQW9Oc2xS7QiH7KdRYEdgbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d9e35815.mp4?token=L1WaEyXHxXNaadg-ZtTDcfb_e--Ycij199FuhMUKjR1kooPC_YrYst374oynhPm64xqZkJxUwRExJYB16RvAu1QnIcHjqzImykICEhpg-YE8Q_eZ2R1fuxGAv1MNQg47LtJKW8sypuJKHJqwTUAid78Twtu8018Q1LHGnXEN7iqL5-VFtgKMEoP5BQsxjhR6lkH3Q_K9AAJrXxyrQITeeXx6d-nrn2GpAaKNNIXJsNa1ZyDUWvMKYBsA6wlEwd0_P3YqPXjTx3cE4TvGyfDOzTyHfRKdy1lZtljsxNaNqUTyjBFjqEOpm3z3HFClAktxQW9Oc2xS7QiH7KdRYEdgbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محیط‌بان منطقۀ شکار ممنوع سوادکوه مازندران در جریان گشت‌زنی روزانه با گله گرازها روبرو شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/467364" target="_blank">📅 21:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467363">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1f2962c2.mp4?token=Xp82YwfcbrfZwUC3xcFfppUfRjosrJbcykmCy5f1xtDMP1tHzW53F3StZ3TtX_cuALdLU8E7YCeDK7P_E_3w9FG5hKV9QSdRYLKKhFAMXpQ3YkNWGGt6Di01f26SunUD1eLufC9ULzT-ei0sRGQ-XCMqMbKxB63R_ynv7IBh-OAwLGIRqNcw7YPhpqfs6ESl05owpKq0OT2iRxTUeJHx9n-K8KnEhUudOrRP5MLMt9D-0_cMQ5CsEL5pGhv6tC8Tthg-O94L1DHmmifJiXwmSJWZIjnUyJaUoBFuLEjhMn24QHfpCDz7ze-WQDTKxSKxoFzj2wkHqaVTW_UbGba9JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1f2962c2.mp4?token=Xp82YwfcbrfZwUC3xcFfppUfRjosrJbcykmCy5f1xtDMP1tHzW53F3StZ3TtX_cuALdLU8E7YCeDK7P_E_3w9FG5hKV9QSdRYLKKhFAMXpQ3YkNWGGt6Di01f26SunUD1eLufC9ULzT-ei0sRGQ-XCMqMbKxB63R_ynv7IBh-OAwLGIRqNcw7YPhpqfs6ESl05owpKq0OT2iRxTUeJHx9n-K8KnEhUudOrRP5MLMt9D-0_cMQ5CsEL5pGhv6tC8Tthg-O94L1DHmmifJiXwmSJWZIjnUyJaUoBFuLEjhMn24QHfpCDz7ze-WQDTKxSKxoFzj2wkHqaVTW_UbGba9JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامه نماز استغاثه به امام زمان (عج) در شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/467363" target="_blank">📅 21:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467362">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c10040e9d0.mp4?token=j2Ug4WarqoKMJKHwHm5AXainfMBr0nmgh3Z1XycbA22Kn-AjTsjnjM9oPXGzj-UkE2H_73UD5aOWTx0yqbSCjjhaTQjEC34LmZ7w5E2FeRX3S1UFoarIqLy0dOwEyw6eboV6Ur-hoCOAmlP8zAThwQrkeSfMc3IV5li3F859tetegsIelRgNpl0VrdKoMb7PTDZSJpByzH9cBYim92Yy7NWPMdRZW33RP6wcApxODWIzFKz_cYwFYeb-lYSqERqjbW4gKuM45UYbBRB3Wv_QStuIXpXs77p47NlVhsZxfVtvpt0PyUWgCCSQP605rexWQX5pV29pI2Rt5W5eXpu9GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c10040e9d0.mp4?token=j2Ug4WarqoKMJKHwHm5AXainfMBr0nmgh3Z1XycbA22Kn-AjTsjnjM9oPXGzj-UkE2H_73UD5aOWTx0yqbSCjjhaTQjEC34LmZ7w5E2FeRX3S1UFoarIqLy0dOwEyw6eboV6Ur-hoCOAmlP8zAThwQrkeSfMc3IV5li3F859tetegsIelRgNpl0VrdKoMb7PTDZSJpByzH9cBYim92Yy7NWPMdRZW33RP6wcApxODWIzFKz_cYwFYeb-lYSqERqjbW4gKuM45UYbBRB3Wv_QStuIXpXs77p47NlVhsZxfVtvpt0PyUWgCCSQP605rexWQX5pV29pI2Rt5W5eXpu9GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۲۳ شب ایستادگی در میدان ۲۲ بهمن ایلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/467362" target="_blank">📅 21:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e7470cc38.mov?token=Mk0kp1x7KW2h527BnOtPDC27uh3HjFReH162J2Vqa0XaWFtaN05JMt4FIdvow3L_labToBLFRfvSG3PB19HWH2mlEi3T2W8wT9BXR7aiopl3MOew7eXUnT4Du7H-Z4iS6QqP4WFSb1W28HhHuEJBZW-plwmq9lYK9yRwIjKzF_A0EmTtKSBkHM_Ux4cexUCPcZBxpdadfEFho7HINErdOnyRFLQHKYLuhko3hnDoQNks6pM2RChY8KEPm01IhDKoEBxDU6l72sth9TwqBDVf67Vx3uxLs1-enDQBs9d-jsNqR8RgNr_oJj4osHg1_CYV3_OUqHSRBS3fT--Yglxd8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e7470cc38.mov?token=Mk0kp1x7KW2h527BnOtPDC27uh3HjFReH162J2Vqa0XaWFtaN05JMt4FIdvow3L_labToBLFRfvSG3PB19HWH2mlEi3T2W8wT9BXR7aiopl3MOew7eXUnT4Du7H-Z4iS6QqP4WFSb1W28HhHuEJBZW-plwmq9lYK9yRwIjKzF_A0EmTtKSBkHM_Ux4cexUCPcZBxpdadfEFho7HINErdOnyRFLQHKYLuhko3hnDoQNks6pM2RChY8KEPm01IhDKoEBxDU6l72sth9TwqBDVf67Vx3uxLs1-enDQBs9d-jsNqR8RgNr_oJj4osHg1_CYV3_OUqHSRBS3fT--Yglxd8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: نشست سه جانبۀ ایران، روسیه و آذربایجان به ابتکار روسیه شکل گرفت
🔹
بعضی پروژه‌های مشترک مورد بحث و توافق قرار گرفت که همکاری اقتصادی سه کشور را دربرمی گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/467361" target="_blank">📅 21:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎥
بدون تعارف با روح‌الله رستمی، پرچمدار کاروان پاراآسیایی ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/467360" target="_blank">📅 21:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ae424ebf.mp4?token=Dzs0tZMc2N-23uoOLbLS6Ksd7E7hq3a18OBf2EDJDZclyOFyo8SzRQVZF14OSMexnuWb4zilox7wmvOTHrjDjbbVT0VlLJP2xS--20CQidl2mW-OJ5za4_Uk986MUtuUkBW03pMG70Zlj7lCw_o3hl5RcSQ-0L8b8o96l5-wJy8vZ_WMFdzjczHwyCf2slHo-81GM64xNQvlrrItd8s4q35CpnMfTmCBvOTAr3g3Oo4sfePdKZxgt9SsUJry-6VE90t6doZNwquHzG1L3psmZHkb8qsMUEDEV3h0lH9-znejlRlW6bw2Sk0hbpWQe0M_J0smydUkbg0tMK079cd_yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ae424ebf.mp4?token=Dzs0tZMc2N-23uoOLbLS6Ksd7E7hq3a18OBf2EDJDZclyOFyo8SzRQVZF14OSMexnuWb4zilox7wmvOTHrjDjbbVT0VlLJP2xS--20CQidl2mW-OJ5za4_Uk986MUtuUkBW03pMG70Zlj7lCw_o3hl5RcSQ-0L8b8o96l5-wJy8vZ_WMFdzjczHwyCf2slHo-81GM64xNQvlrrItd8s4q35CpnMfTmCBvOTAr3g3Oo4sfePdKZxgt9SsUJry-6VE90t6doZNwquHzG1L3psmZHkb8qsMUEDEV3h0lH9-znejlRlW6bw2Sk0hbpWQe0M_J0smydUkbg0tMK079cd_yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منشأ توفیقاتِ معنوی انسان در بیان رهبر معظم انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/467359" target="_blank">📅 21:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhlUrnfCNL0oSRNYpj2wsyA0U2E_8uwh-29BrXOeKwlGMEg_m3wmM9M1LfPAqC_GHwa_AC5s9rebpmWGh3KhUVq3YcQyOHwf8s01d5BU5j0ybSambsHxVpJrg9WfFzdxyE9A6rIyL30-5quIpptiPkPe4yqUpdjKnytMrE2yBHMROsgnvTZsqSVN8JuccUy6bFT_NVl0DxdJoA9xLAYHZ-KuCCqrytNJkqEkXgzRLpDuyzqHpgFAU_Lr1OHaDt-CvPDQleT6AbkJUHRFRWAelLvdjS--TuSH3w26y2SmH4mTbfpy7cSE1DMptma8uFLKdtKu9YbVERZsvUx1MDD9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  فلای دبی پروازهای خود به ۳ شهر عربستان را لغو کرد
🔹
شرکت هواپیمایی فلای دبی امارات، پروازهای خود به ریاض و ینبع را تا ۱۰ اکتبر و پروازهای خود به ابها را تا ۱۱ اکتبر لغو کرده است. @Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/467358" target="_blank">📅 21:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467357">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۸ کشور تحریم‌های آمریکا علیه دیوان کیفری بین‌المللی را محکوم کردند
🔹
فرانسه، آلمان، ایتالیا، ژاپن، هلند، بریتانیا، کانادا و دانمارک در بیانیه‌ای مشترک، مخالفت خود را با تحریم‌های آمریکا علیه دیوان کیفری بین‌المللی اعلام کردند.
🔹
این کشورها هشدار دادند که تحریم‌های آمریکا تأثیر قابل‌توجهی بر فعالیت دیوان کیفری بین‌المللی خواهد گذاشت.
🔸
دولت آمریکا به ریاست دونالد ترامپ با متهم کردن دیوان کیفری بین‌المللی به هدف قرار دادن ناعادلانه شهروندان آمریکایی در پرونده‌های جنایات جنگی، اعلام کرد که آمریکا نیازی به این دادگاه ندارد.
🔸
دیوان کیفری بین‌المللی در واکنش گفت مقام‌های دولت دونالد ترامپ در حال تلاش برای «اخلال در روند اجرای عدالت» هستند و اقدام آمریکا را «حمله‌ای» به نظم حقوقی بین‌المللی دانست.
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/467357" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467356">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRjEfVWFlMmLNWl8S42Vsz30CJ1AkbCtKFXkhIoUu5MSqGlUqvoVslDkQItouogfq2l7ZTonIKrKqse5GcZbWMpOyD2jloA0AU_jbArkqio3TeyL5JHKXDhnTwVIAOgLbEsVnKwh5UnbGYl0kI0nSjCqA82UAVOBNA6BmT55iScTyGDgrjpmQj_jGc3N3XdlyyOoCHEG8NvLSQOjUQHQLQSLLAAtaAgXSpv46m34shytNBgJTvAkks9MMQx85pkTmQwhx7U9FpuymBPvildlD6UaYDiWqWqXJ6zlW7GIODPeig3MJtjxQdE34S09AH7kfkn9CGoehoDRfTzg25JlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو طلایی تکواندو ایران در پاریس
🔹
آرین سلیمی و ابوالفضل زندی نمایندگان تکواندو کشورمان در سومین مرحله مسابقات گرندپری تکواندو پاریس موفق به کسب مدال طلا شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/467356" target="_blank">📅 21:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9NUk_aBLYbsfnckUOWkj5uVYAwCmkQd02jeoJMgQK8KIQ6Jn8dMNq5ycdzrMnbu6t58NZdzSVJAhefEM1CtrfaN5GEsLWm1sfCt5dl_zBmPZQ4t0LNrHtd1jDkc4ZqBQF4iC-54F4_o0dLdrEuX1xIefl7s3PyKWwm2GZsS2e-HFPWM5P0u7inH7UByslkDxjKSeuvlFJ0o3dMNbTtTalFH9x72crvt_YAxr_RdRnsqjXPZf0yE2ForzPFg6hHhJi4STcfPGcUdH_q2num_zW9PNehVlSCEYEczyYjJj9cVoFaRzdzG9Q6eaA2S1_Rnm0FYTmQeXBf3E_WvX9CWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت معاون اجتماعی فراجای سیستان‌وبلوچستان
🔹
یک منبع مطلع از شهادت معاون اجتماعی فراجای استان سیستان‌وبلوچستان در منطقهٔ چشمه زیارت زاهدان خبر داد.
🔹
شهیده افتخاری ساعتی پیش در جریان منفجر شدن بمب کنار جاده‌ای در مسیر حرکت خودروی پلیس در زاهدان آسمانی شد.…</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/467355" target="_blank">📅 21:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084aee65df.mp4?token=D8sciSmBCrtoZcyIqxlMttkp1v5JO1sO_v4E0wO7-uSCmLKKRhRO_O1umXq8fngJHBdHP8juAtn6yFUseiJmt4ScLsjxbezvEzFq5nEO7L7Ka7g2l3uvRWOjjU9pH11dpanO9Jj0exlpxZiFT--1A_7sba6mmPb95In4_HiibR6AGwLyJYMRPEEdJgFeTNHVBTpPbkQe8dmULVdY3e_1gciBs0qG94lM4546aSOezn_2OBvBWpLzlt4vKSxxncLOmgE4r6VdMKayKxHz-y9v3c3yqz-97oGk-jYNPco5HbC40qbx2LdWBimzy67mK03OVaURS-_VMDMPxlI18rUqzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084aee65df.mp4?token=D8sciSmBCrtoZcyIqxlMttkp1v5JO1sO_v4E0wO7-uSCmLKKRhRO_O1umXq8fngJHBdHP8juAtn6yFUseiJmt4ScLsjxbezvEzFq5nEO7L7Ka7g2l3uvRWOjjU9pH11dpanO9Jj0exlpxZiFT--1A_7sba6mmPb95In4_HiibR6AGwLyJYMRPEEdJgFeTNHVBTpPbkQe8dmULVdY3e_1gciBs0qG94lM4546aSOezn_2OBvBWpLzlt4vKSxxncLOmgE4r6VdMKayKxHz-y9v3c3yqz-97oGk-jYNPco5HbC40qbx2LdWBimzy67mK03OVaURS-_VMDMPxlI18rUqzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ؛ از «اعدام نکنید» تا دفاع از پخش مستقیم اعدام با تیرباران
🔹
رئیس‌جمهور آمریکا که سال ۱۳۹۸ در حمایت از دو سارق مسلح که اقدام به سرقت از یک زن با سلاح سرد کرده بودند پیامی با هشتگ اعدام نکنید منتشر کرده بود امروز از اعدام یک افسر سابق ارتش آمریکا با جوخه تیرباران دفاع کرد.
🔹
او گفت: «ما برای مردی که ۱۴ سرباز را کشت حکم اعدام از طریق جوخه تیرباران در نظر گرفتیم. حق او همین است.»
🔹
پیت هگزث وزیر جنگ آمریکا روز پنجشنبه گفت قصد دارد امکان تماشای عمومی اعدام افسر سابق ارتش این کشور را فراهم کند.
🔹
هگزث در گفت‌وگو با رسانه‌های آمریکا گفت: «مطمئن می‌شویم که مردم بتوانند این اعدام را تماشا کنند؛ این مجازات باید علنی باشد.»
🔹
یکی از مقام‌های وزارت دفاع آمریکا نیز اعلام کرد: «این اعدام به‌صورت زنده پخش خواهد شد و جزئیات بعداً اعلام می‌شود.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/467354" target="_blank">📅 20:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZxoTBeToWY6VOjJ2Irb_Dci75CLazljvC-cTMnJDeMm3zuDP0SNsadspuPIjNIk2JCdfsCphG1g3IhIR35duIiE9AWKAHrd4gHqm3gPcWgeqiCl4bAOzodAyVzv7pn8PitLswy2dkX47sc04XGjshzRw3J9GZmn_NzaxK5h7ecXA5BFBY81MP53kpbM7lI2tBWfUHMTE-FcTsKxnIAFrn3RihSk56TsAp8KGnpJS6i-GpcJIZIvCH8e3qxTa72sQaABh6p7pCSB6GY4cSZl2syDw561WA5ctdXLQ3oZF0OR2Jeb3p8g-vnd9Hpn_n3hyjbR5xiqZo6dXN6IW0B2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">التماس زلنسکی به آمریکا برای کمک در جنگ مقابل روسیه
🔹
رئیس‌جمهور اوکراین با لحنی ملتماسانه از آمریکا خواست که به کشورش در جنگ مقابل روسیه کمک کند: کمک به اوکراین برای آمریکا هیچ هزینه‌ای ندارد؛ مطلقاً هیچ هزینه‌ای. من آشکارا گفتم به ما کمک کنید از آسمانمان دفاع کنیم و بر آن مسلط شویم. آن‌وقت پوتین پشت میز مذاکره خواهد نشست.
🔹
زلنسکی سال پیش اعتراف کرده بود که جنگ با روسیه را با وعده آمریکا برای پیوستن اوکراین به ناتو آغاز کرده اما اکنون می‌بیند که واشنگتن چنین قصدی نداشته است؛ او گفته بود: آمریکا هرگز، حتی قبل از دونالد ترامپ هم ما را در ناتو نمی‌خواست و فقط در این باره حرف می‌زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/467353" target="_blank">📅 20:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467351">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b55f86f9.mp4?token=JF4XCGA_EN9TpG_sCbx4eGSTVeEcbKCwEVRvJ3SjGoAiR7QUQJb31u_P3Has3XGlsrqCdfoDPkUuiyJWTfXpYuiR87hbZtjDC84w6QSiaTbtSaRaT7XpLecRiO9NF0W7er7H-TK0LDlvVeIzt9MwADuJ-ya8oaSA23zQH72PNjlRXUeqJOERv92QKIHH0ml_WleqkZkxesc0I_2aA8IkXeKk137Jk-dYu5bJFkynEYVO7KN8RXX5D-nBvpFnWv_cdfwoZWdFGDbVj5L0c5LELDrJdvjYqFSQ38s-mxKiFjv95ZMnPwOW2vldTJy4YNapbpCjkEnpprwmn1BR4hUlnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b55f86f9.mp4?token=JF4XCGA_EN9TpG_sCbx4eGSTVeEcbKCwEVRvJ3SjGoAiR7QUQJb31u_P3Has3XGlsrqCdfoDPkUuiyJWTfXpYuiR87hbZtjDC84w6QSiaTbtSaRaT7XpLecRiO9NF0W7er7H-TK0LDlvVeIzt9MwADuJ-ya8oaSA23zQH72PNjlRXUeqJOERv92QKIHH0ml_WleqkZkxesc0I_2aA8IkXeKk137Jk-dYu5bJFkynEYVO7KN8RXX5D-nBvpFnWv_cdfwoZWdFGDbVj5L0c5LELDrJdvjYqFSQ38s-mxKiFjv95ZMnPwOW2vldTJy4YNapbpCjkEnpprwmn1BR4hUlnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر جدیدی از عملیات آفندی علیه مواضع ارتش تروریستی آمریکا در عملیات‌های نصر ۱ و۲ و تنبیه متجاوز
🔹
این تصاویر که برای اولین‌بار منتشر شده‌، شلیک و هدف قرارگرفتن مواضع آمریکا با پهپادهای شاهد ۱۳۶ و ۲۳۸ را نشان می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/467351" target="_blank">📅 20:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467350">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aePzfv7DcuD-e1r_K2APAOJsdXGvQB_JWBi3FBtpB24s82fpuyfjHlgHMJFHMxLiBWjIIa48w9DNDp-kCMUCXjzkhJ3ixbJq6uxp0iHsN1YpDtkkNXcYZRFFQvoVLsOwoJY_MfJDtRLtFYAUIV0dyIRUXYtaCv3gut5_0b7lmpC6DOIu5kMCGLQA-EwF33oVwCz8HtDhCvB9yqbnpK7JIBOl9Pp1QB-ce1LELoTmZOE26cjlkqsNG4HGPxRqCVBi13iEKcFfRwnBgsfZJabsONx3pE0g-1qr6EQV26GWSRWMPPmTTHDyta6GCW-UhdB-4dwJEgLjwAwKoRqs-CL-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
علیرضا دبیر و محمدرضا گلزار به تمرین امروز استقلال رفتند
🔹
تمرین امروز تیم استقلال در سالن وزنه فدراسیون کشتی برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/467350" target="_blank">📅 20:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467349">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af42fe811.mp4?token=KvCf2NdHQ_4-2y81hLWBOSaMoUS5XD55Kmx74dqsY933Z_-RTjptHOD4gEyOHTOvzsNuv7JH6sXVrHSzj9OrxEz4JIceYN9dE3o-3c3JyStZ0RzBDpFvZwsguU12kpXdUx5_UWeRb99OsOC2WFDCIA4IUs22IDEwOpJY601a-ljdSd1DJ7e6iaBLzS7VXwWM2Bla-ujQAJSwWtmR1gHv1wqSmGvYm2eBu7qz13v2slndkOqPhzRIOHjpUFaT3bE-STjCva3fBL8yBM_dVhsdvwFtEw_1ol0Pq1yjsxpjYU7V-AFE26VmiM5xkN197qlRbto0plwih0G5vkmc6xvaEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af42fe811.mp4?token=KvCf2NdHQ_4-2y81hLWBOSaMoUS5XD55Kmx74dqsY933Z_-RTjptHOD4gEyOHTOvzsNuv7JH6sXVrHSzj9OrxEz4JIceYN9dE3o-3c3JyStZ0RzBDpFvZwsguU12kpXdUx5_UWeRb99OsOC2WFDCIA4IUs22IDEwOpJY601a-ljdSd1DJ7e6iaBLzS7VXwWM2Bla-ujQAJSwWtmR1gHv1wqSmGvYm2eBu7qz13v2slndkOqPhzRIOHjpUFaT3bE-STjCva3fBL8yBM_dVhsdvwFtEw_1ol0Pq1yjsxpjYU7V-AFE26VmiM5xkN197qlRbto0plwih0G5vkmc6xvaEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهتزاز پرچم سرخ خونخواهی در آیین جمعه نشلجی‌ها در استان اصفهان
🔹
اهالی روستای نشلج کاشان  پرچم‌های سرخ انتقام رهبر شهید انقلاب را با خود به آیین سنتی جمعه نشلجی‌ها آوردند؛ این مراسم همزمان با هفتمین روز شهادت امام‌زاده علی‌ بن ‌باقر(ع) در مشهداردهال برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/467349" target="_blank">📅 20:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467348">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNaINZkIbZWAXT-5zpKz3Wd9buWlro3GP3MEcYbyChjxHwV28lvfoMnjkfwLANwX1vNf1jTP7DkidBeM1os1RDV_lDVFOdd9Sa7lh_lmH9bF6-TqewOXWAsx0-bohKU3X8ZacLeIOKd_L-FB2mIh_PH1Vw67RvQD1zr6SO5eRkNIoE3apyKEIqLUmuFye9wrL4ZucYbyryUPPzOlkN2wWzcHro5oL_CmPIbQ-GDV7nFffXQnrUPUq7504drfsK8i1AdPLCC1OrKA78Hjz8RDbnFwvaRTh7vqlpeDZFeTFKFSplTIJz5NwYyXbNi9VXLn8YcuNhcinaoOIQ1PhgF45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس آمریکا در اسارت هرمز
🔹
ریزش ارزش سهام شرکت‌های آمریکایی در سایه تنش با ایران ادامه دارد.
🔹
مطابق آخرین داده‌ها، حدود ۷۰ درصد شرکت‌های بزرگ آمریکایی در ماه گذشته میلادی بازدهی منفی داشته‌اند.
🔸
افزایش تورم در اثر ادامه تنش‌ها در منطقه و کاهش عرضه نفت، شرکت‌های آمریکایی را با بحران مواجه کرده است و پیش‌بینی می‌شود این بحران به زودی دامن‌گیر شرکت‌های پیشرو بورس نیز بشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/467348" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467347">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itu1vT5DWI6T2yCw67ZoXcCm6dl8l7gDlhq_okRSdRYeVF8PyPk23bBVd-eKZWqMN5bT3YMUqpou6Bzf57snjV4MWCGL7wng-4O2ov2Q6OEYcaWMFWyLd0a3OZfR8m2KEKWQW6kPtHLZvOsyRvH7W2t_UuGgtOuY6uIUTgmrixYXy8UEmoWro3rWZSj3Bhb-SokHLnNuj2kaN509FX6DgpfEKwx0H9K3LNgucSi0sHMTbXsnlUk0YR6t1ABufhQhrIOgcNeBogiR2vOfNazR53QorFbwEbJp6KOm8F1RrnAnWQaOoflwyNvy36T45O1FillXm2RuhB5fvy0VhyT29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی به آمریکا: برای تکرار شکست‌های تاریخی از ایران آماده باشید
🔹
سرلشکر رضایی: وقتی پس از شکست و تحقیر در برابر ایران، به آتن می‌روند تا روایتی از جنگ تمدنی را شکل دهند، بهتر است بخش مهم دیگری از تاریخ را هم بخوانند: جایی‌که امپراطور روم، در برابر شاپور اول ساسانی زانو زد.
🔹
کسی که پای تاریخ را به میان می‌کشد، باید برای تکرارش هم آماده باشد!
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/467347" target="_blank">📅 20:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467346">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8f3d265c.mp4?token=kDct4VrQETe9RCOC_uyAwYcda7e7bySnie9JFLba9CdnH6PH50peXoHl3S8zpbTw1A_yHJjAWmLP8D3pjcKYW9dy7uDsxy01Hnhus3qrVjy1ii2UYMEdnUu2SyI2SzlXuHw3auAdKRJygB4WAXj7cAwBlfM4pyNMR6blMDZcHJGpyXamP8J0BvkrMu7G2_n0GUFwuqOC8c7KHBitk5I7-vxC4ESI-18fPtw7CfRdN4BRBxGthdZdt3xb43z4YXdGWzD8sA_S96SNmR0FW9QmkxAXLiS5rKskztGq7e_r-qwMW4Gc8faSE4VgTMrA34J6rQGeCN-MNeXowNSufIdrcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8f3d265c.mp4?token=kDct4VrQETe9RCOC_uyAwYcda7e7bySnie9JFLba9CdnH6PH50peXoHl3S8zpbTw1A_yHJjAWmLP8D3pjcKYW9dy7uDsxy01Hnhus3qrVjy1ii2UYMEdnUu2SyI2SzlXuHw3auAdKRJygB4WAXj7cAwBlfM4pyNMR6blMDZcHJGpyXamP8J0BvkrMu7G2_n0GUFwuqOC8c7KHBitk5I7-vxC4ESI-18fPtw7CfRdN4BRBxGthdZdt3xb43z4YXdGWzD8sA_S96SNmR0FW9QmkxAXLiS5rKskztGq7e_r-qwMW4Gc8faSE4VgTMrA34J6rQGeCN-MNeXowNSufIdrcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هاشمی، معاون وزیر ورزش: ۶ ماههٔ دوم امسال ورزشگاه آزادی به بهره‌برداری می‌رسد.
🔹
دولت ۵۰۰ میلیارد تومان دیگر برای بازسازی ورزشگاه آزادی کمک کرده است. @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/467346" target="_blank">📅 20:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467339">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4JESQwIg_L1c5suL_331-nzRYCvyIpgU4IcgQ5dVQJp0mvVHBt2RZQyfr9JgjKCLMHB6UaNqUf7q7whWWj488p78G0c6EMFi3ogqjBDmNkZB3hVgXVqC1BF6nm7QnrxXIIQfmtkpu-9AthhML0mGLu4RawiEW01IfUix5p35KOOEc6Izj-nlEwzt5K7iN9YHLGBL6H8D6BAGfkLHoDGmClbqUAw7Q0NpYI7A4dYfkvQCh2eooZksyj_p5Nd2Wnl7peEMJlrhWCY6DDUzd9o6DhKqXAAhObSisjfaS03sx11dAQ4CAWRzkeqwU1oUfiaPObsIqnGNUxSIYY1LyE5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvGDmAMT5Ys-nwsW6-rV2nNvh0fueZfhPrAaRP_vHZE6HYr1HZlcAGbIpUUW5m5r736A55WVKdRY7Z1VD6If2xntl8tOWFc4qEKUncwtNN4LJV2QNCLRgDWPkiZsJueI2UykbBEW58R9nTidEomdUJEywJo1_9xa89Qn869WTxLXvDVgdJZFdM0DblIQ5L4ZZNUDroJRv6PkQbE-KpZztCz0yuNcqRf7ukMUamq2woDP9qEXM7qrpw5DmGvqbnG_Gjt5LfatVg5qpmUJSvqhvzfvkf4xKfT_puonNXrIceNItVKm_pr9-BnndNTSBMJ2PHNuc4fZO6ecm65wg8gLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnPOyxn7hM4VoVOS_VlKH3gSdSLTQiYmV8NW13dzQcP4YJPC9TVpfck1lI5S0WVtSiMSXLe5G_ZVfO9YduH0Pw5xH87dmg34YEm4wCO2Q4KbTF7qXqB7EMSsoSId6G67f6I1HCumU7qxlY1bqXE1efe9hHc5R45FcgtJ7_001Kf_Da4vwedJ7XHh0VIyycZ5nbPJ_xWcgJKz1zsX9noQ6VZ72Pr7ZC2NgYMA22tXGeW9MiEKWEup6BHsEL5DFYfVvAbkWHlRxhuyXlAukYr164VvAE95VcKhI8SH0Lq4i0F0jJQr7r_h2gRuOK0yu2Bpt762_H84bplUzN6E5ksVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QX5Qamxg5DtJTKtGVfaoddSPd0RgHlEWhWJfc3WLauJCnOGUZCQh_WLXGYOLT4yM0jjT8SQcDuZezMfpkHpWedbyVjeDDI2L8tCmtjPHlTqee_DE3uQiMjY2xneJ8EMabfzZnxNvc4alL-6L1jHXXdQqIZcJoLbUNLFog2VeWCoC-tUzXbNhMgd-EMqo9QPx-LVzV458qcHdBMSsnm2tBkb56UFot__jGgQAiiD1C5lVe0RNEjIuzy5GxI2-Vc4XkSh719gsTevwgakRorVmN2ZeoQwnjMVf3WKQAcAMJyPSLBN1_ZL_e-TaSoBXkXXedBN04CnOycFCdlKxjIcClQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5f9BZOZ1f2DTe69vBagzDMJfuJuZbuia2BrCWzx_aqWf7KG-XBBr8ODxiLuf22u7z3xp2njL_EpSxRsW48fcFe7ArOIAujZyi1IG7wAG5BSCNzRM2rSZqo1L_LSjWeUxn8hGKEhlDw__jpdyHigeoPuRvRaohEzMan0sFusQNSfkzdrrSeZ713bza9gDPhdg_ll1E8tkr6JZJ1sEXH9kvUFe-wwWGyR8usUJvcDy1oXuEPHqHpnagyPOssRd1bC4WVk2ZJOvPBOK-kj4I-ubQ2vGfixQCGMX0qEhmYAegKra878aJY7SV4BQIpC9ffa4ND31XefUfmVCONdaCgr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNOqVqI-X8WczRHR_wX9G-fRHMqkLYS5usjE2zzBx40U960lFLT7AWwUDAu4sNTNWQ1vT_-PAtN5iM8t5tEew1kYaHh65gweWm0cGHfruRdGPn4q32PZIvBo-_znlA6N3hKmVT1LOR3yC69ibNA2p1Gg4zY6GhloWr5oFDT442CZoph2GGl5aPiHYc1VBPCW8STnrkxKS0R66S3kxviIi2Yzrzt4zQkEViHgsy7JGEiS__eH5COgaR1b9sKCj9cPpIrkE3YF9pHm8smjYY4aRIOgYRyXVf9F1FmEJrtON6jpZKJH7s70oz6HLbeiUvWuVOXP1lJrAiADDf8ui2gEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiOupRRcl7J83bBk23hstYg-PfojkXXnHEn2kj7pt9Lwqeirq0VsEZiPZP0KxVhNCNkB40jFhwpNGvRMtlgYBx1dehpLjsYstGFqT1JgMUpUyg167U9p1Rh-cdNFcUCpEQnvFZeK8d7A9IXr8CvzS-PBwetFl_aoSEGeV0kajvk-D3-M7q54iiwhr4yUvHz8snCJv59SPZcbrlrQjswpToTIN_vTUZjeQX7LxWPguGcZcM-LdhA6fFF2MNFt0VO3HqeNRV9xX2j5992ko1njTXy_quns04h-GxdHLJTCblSmvifKbYlZLqk-wT3WX3nVP-43C0HHyiInr3Ouwgl4XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روز شاد کرمانی‌ها با پیاده‌روی خانوادگی
عکس:
مهدی امین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467339" target="_blank">📅 20:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467338">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mctyu5NUAq1EZFUHasoOViqa3kglEqBVBsk0V0lC9_3_IHhperDAytDUiKzjJoOw6R8Alclfrb4IxoGhVJ4OwUf_37ACXbak7WOOjvZ4xe3zziFesphJtpBLu3ok3M2nH9r85yt6_rEQ7fsiTPonLUJtMIaQpKqPnn3IuFPduAeK9KKML8PxSCF8ldfe6R3PxALOOuABfLrpo83xguYE_FEroy9MloCfxgVbqrr9Pxi9lcGcl1SvyNVdnYXJurUxoT-5SLUI8ylFcsgATJdf2Tsi9EwOdvCT3CYGePTHs9YYYchHCvjP87U5qBmi_ULWqrc8JkuMwYy4eG6kwZiZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آغاز تحقیقات عربستان دربارۀ پرواز فلای‌دبی بدون مشارکت اسرائیل
🔹
عربستان سعودی پس از حمله هفته گذشته در کابین خلبان یک هواپیمای فلای‌دبی، تحقیقات مربوط به ایمنی هوایی را آغاز کرده است.
🔹
رژیم صهیونیستی پیشنهاد کرده است در تحقیقات ایمنی تحت رهبری عربستان…</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/467338" target="_blank">📅 20:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467337">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPQBaf9l3tBoWPaLNAUlWLvqJKFGNRtWEkw1pMv-KN4vc72tMYe5rwN9tCw0fCtEQPNs2z4gWJbOs42hgpD8HK4qfCzjVfsTSQfbvMpDfQKsnBtPbc1RUIx-7dJETPM0UUnQ2-L3Uk1rfmCdTuskfDs_qklpEPqapbI-Ed6l5qkbMQ6oAEv6Dl3_p7yCcgZRx_IXKx3sAvUb7jMVoDRZrVT3Pir-Px-pqjdx8TxC-hYsETPaha147NwH27wjtsk4yE3XT0ezjgTyZsNba9nYTMGtgBHA9i9tut0ktvEkVyAHbrjC9YNobBhSs6f_g7zzwalRtAkN00oqX7-RWteLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه نشانه از شکست راهبرد انزوای ایران در محاسبات غرب
🔹
به باور تحلیلگران، سه انگارۀ «عبور تدریجی ایران از محاصرۀ اقتصادی، تداوم ضربات ایران به نفتکش‌ها در تنگۀ هرمز و حفظ آمادگی نظامی و امنیتی ایران برای مقابله با تهدیدات خارجی»، محاسبات آمریکا و غرب را تحت تأثیر قرار داده و فرضیۀ شکست «راهبرد انزوا و حذف ایران» را تقویت کرده است.
🔸
تحلیلگران و کارشناسان می‌گویند که بهره‌گیری، بازنمایی و تقویت انگاره‌های فوق در فضای رسانه ای روایت پیروزی ایران را تکمیل خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/467337" target="_blank">📅 19:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467336">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuGLaLNPB8FtXDGo9gxpfBQrUhqXicd3E1Lxa7vp_0UiFvXx2AWJcUP3JfWqjhx1Ns-O5LQpVY9YFpHjRusLNHw6TCwgr_9Velyvjh-5zJeyLoM31UAyUae0jiUb_sTjMJd4LHKhsBjxyvW8MN8kvVVo2bZT9W68GnkE_RVuz5SsnEuWlpcm33G6YoW6dHk63K_QuJVqeTZ8xMkv8th-AdYoX0ep2W16ZSrtcgTfyXoNFTYlbssv_vPS_-_Yx2e9FelROiOACExeGtMazlzt0lXexHF2ofVMkMsQ4Sitm4UaqfiJkX98KNDSPOJ2aRSlzh1JQ1zv2RNaNXfOr3hHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدارس هرمزگان فردا غیرحضوری است
🔹
معاون استاندار هرمزگان: فعالیت تمامی مدارس استان فردا در همۀ مقاطع تحصیلی به صورت غیرحضوری خواهد بود؛ نحوه فعالیت مدارس از روز یکشنبه مهرماه به شرح زیر است:
بندرعباس
فعالیت مدارس در تمامی مقاطع تحصیلی به صورت سه روز آموزش حضوری و دو روز آموزش غیرحضوری و مجازی در هر هفته انجام خواهد شد.
قشم، سیریک و جاسک
فعالیت مدارس در تمامی مقاطع تحصیلی به صورت ترکیبی از آموزش حضوری و غیرحضوری خواهد بود.
سایر شهرستان‌ها
فعالیت مدارس در تمامی مقاطع تحصیلی به صورت حضوری خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/467336" target="_blank">📅 19:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467335">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
شرط یمن برای پروازهای فرودگاه ریاض
🔹
یحیی سریع سخنگوی نیروهای مسلح یمن امروز گفت فقط پروازهای بشردوستانه‌ای می‌تواند به فرودگاه ریاض صورت گیرد که مجوز پرواز را از مرکز هماهنگی عملیات بشردوستانه در صنعا دریافت کرده باشند.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/467335" target="_blank">📅 19:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467334">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e625a1a11d.mp4?token=fsNe_qvJCj2sO2T5gisKe06fEZRqRT9kvd29xTdwB-GaHEaGKx-ZZSXd8IRStpmDmkDFC4tjfapoxbG2cVhfkpCntfOKP8vY_rSRiCXz3SIXPr21IstYBYzhDXqqOCYqrtdBpNvoeHly8HrkrmqjJsRJLnbE3UDpPjuSVIVzUPU-1ExG6fCbj3RTBt7cbC7n_YywcCmWW2iYLymh3_TPv3Z9xJeE7XC3b0v5xu_qdCq7BlTSLqEPv1ADNtRrKkU4ac1E0M6g8s1aedGdxvMnRJU44BslyDPat-jXRPETSLF2VZvJDVU4gqzjTJQqNJzyXBcGQJGLhHEsshFddrC7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e625a1a11d.mp4?token=fsNe_qvJCj2sO2T5gisKe06fEZRqRT9kvd29xTdwB-GaHEaGKx-ZZSXd8IRStpmDmkDFC4tjfapoxbG2cVhfkpCntfOKP8vY_rSRiCXz3SIXPr21IstYBYzhDXqqOCYqrtdBpNvoeHly8HrkrmqjJsRJLnbE3UDpPjuSVIVzUPU-1ExG6fCbj3RTBt7cbC7n_YywcCmWW2iYLymh3_TPv3Z9xJeE7XC3b0v5xu_qdCq7BlTSLqEPv1ADNtRrKkU4ac1E0M6g8s1aedGdxvMnRJU44BslyDPat-jXRPETSLF2VZvJDVU4gqzjTJQqNJzyXBcGQJGLhHEsshFddrC7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تحریم علیه ایران، اقتصاد و نظم منطقه‌ای را تهدید می‌کند  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/467334" target="_blank">📅 19:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467333">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891ab99c87.mp4?token=ukprgkVeHjrnp5lr8VLlzYO8o5cNbOx2l0oXShQ1CS-gCIyWJ2FBL62ahNbjp57odgBOXmiEkVFKlkU3PzAoF-l63-x0mYi1s8JmhE-7mi3CtTqPjZsuMCrMyM1G8K3N4p7MmhN7TSKSz2dZQuNQVyqv_3JKgwdeLNQ8BcB4kQgAB8LsGUHyQvkNWeWMmQzqajdzFvl-S6pAVaOdn-UXlfwBxwmCGVGKpz0ha0YUaRcS8VCiby2PURoxr8gruDb-WvptBCzw_jXkgyUX6s0zZ6bkzvObsdB-lGuAxu9Y4IPAtti45pLf3-44Xe_WCa9nG6PCjqJWMESjIrQwNmehqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891ab99c87.mp4?token=ukprgkVeHjrnp5lr8VLlzYO8o5cNbOx2l0oXShQ1CS-gCIyWJ2FBL62ahNbjp57odgBOXmiEkVFKlkU3PzAoF-l63-x0mYi1s8JmhE-7mi3CtTqPjZsuMCrMyM1G8K3N4p7MmhN7TSKSz2dZQuNQVyqv_3JKgwdeLNQ8BcB4kQgAB8LsGUHyQvkNWeWMmQzqajdzFvl-S6pAVaOdn-UXlfwBxwmCGVGKpz0ha0YUaRcS8VCiby2PURoxr8gruDb-WvptBCzw_jXkgyUX6s0zZ6bkzvObsdB-lGuAxu9Y4IPAtti45pLf3-44Xe_WCa9nG6PCjqJWMESjIrQwNmehqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول صنعت‌نفت توسط باصری در دقیقه ۶۶
⚽️
پرسپولیس ۲ - ۱ صنعت نفت @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/467333" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467332">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te240zFpeRzGbGUOSqGQx3gjNuymdwGTSJz2hWCDUGgRxZPZ3NjL10xbkTdkP-2oW3eUnUguE-uPuoCJA5JIfpRpdJKHWGd7cVGKNaPquKW8tS4Cayp3M9j-d6jYfwEHDuLFS1mAvxiaWJP7_JtrwlRpQC8B04TxfsobV8eDbTvnOzsyhbu1NXw40Bb1aOnoidZYjWN0d1GF3VsyRFMN4I7l91NqQ7pOOboN3wi53bEsM25uNjQNLp9w2MBSUOOOAucPsq8YzjjnpCUllOjRw90ScWnN-mPkQ8_tT6xMKmCb4Rqd-qvd3iuSNr8AZt-3QXoGhbO-J0f2qKR3QRHfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعاً مدارس حضوری خواهد بود
🔹
ما تمام برنامه‌ریزی‌های لازم را برای حضوری‌شدن کامل مدارس انجام داده‌ایم.
🔹
اگر اتفاقی در نقاطی از کشور رخ بدهد، اختیاراتی به استانداران می‌دهیم و استانداران متناسب با آن شرایط، به‌صورت نقطه‌ای تصمیم‌گیری می‌کنند.…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/467332" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467331">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2934295f.mp4?token=fJbGajBqbnvTf4Kn5N9PIL50HQl9fWXISjA7PkuVsaX1UmxgGn93hD5pD5klsCcoyqqIuZWK9tK7GGEVokbHIrYcoJZ2w7T8bSb-qGT2CQ94kIGzT6dw9Uk0KrAmbOZV6auCzXLWcivrsOG5HuUpZqWsvULMC3UZLvSwgI7q2aQLgz4Oi-SHL3WvK2zWtJX0KSJbTM1RakmXKB0vpydX5Fkoc9gClLmyUgTKhHWlOnBUx17uv4CN57wcdhVLvkuUzXv34pRKCkhZ_TMr8Sl9jDTUtoMBX5VKotl45pP84qlciKtREyoUrqCsOtHASo2zRVL85amM4JucsQazt0oxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2934295f.mp4?token=fJbGajBqbnvTf4Kn5N9PIL50HQl9fWXISjA7PkuVsaX1UmxgGn93hD5pD5klsCcoyqqIuZWK9tK7GGEVokbHIrYcoJZ2w7T8bSb-qGT2CQ94kIGzT6dw9Uk0KrAmbOZV6auCzXLWcivrsOG5HuUpZqWsvULMC3UZLvSwgI7q2aQLgz4Oi-SHL3WvK2zWtJX0KSJbTM1RakmXKB0vpydX5Fkoc9gClLmyUgTKhHWlOnBUx17uv4CN57wcdhVLvkuUzXv34pRKCkhZ_TMr8Sl9jDTUtoMBX5VKotl45pP84qlciKtREyoUrqCsOtHASo2zRVL85amM4JucsQazt0oxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلطان، نام پلنگ جوان شناسایی‌ شده در رودافشان دماوند
🔹
مدیرکل محیط‌زیست استان تهران: یک پلنگ نر که پیش‌تر توسط اهالی روستا مشاهده شده بود، با تلاش محیط‌بانان و نصب دوربین تله‌ای شناسایی و نام سلطان برای آن انتخاب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467331" target="_blank">📅 18:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467330">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/577177c5a9.mp4?token=dPye-wFQIvqwguT_hijxjblkBE471MKtgyepwSU-39JK6izGB41lOT8LMiuW3DxexGYDNkI2js_NJiuMlC3YDnq0jOv9DEa1FuL71gbneWUeHdLgKZjpa7dRuP8CrYkOL2dw3w7gtzzztFqVA7v4w3s_4HeK7xAIqupsNtvT6Rm5yFEGj6-EdXvpDtpHQ9Rxy5UTeigvbwy3BR2du8y1DqrMFwYRKT19U-L7RgoPbrmRPtgt7i06uXDV-2ikOS-CTJi9kKEeoDce4iwnSgu5XZg0Fo6yxgReHXSDkrj_fXsor-j6mUReDKxBNxFM0ZfVSGCiVOetPLe-EH80RyiuLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/577177c5a9.mp4?token=dPye-wFQIvqwguT_hijxjblkBE471MKtgyepwSU-39JK6izGB41lOT8LMiuW3DxexGYDNkI2js_NJiuMlC3YDnq0jOv9DEa1FuL71gbneWUeHdLgKZjpa7dRuP8CrYkOL2dw3w7gtzzztFqVA7v4w3s_4HeK7xAIqupsNtvT6Rm5yFEGj6-EdXvpDtpHQ9Rxy5UTeigvbwy3BR2du8y1DqrMFwYRKT19U-L7RgoPbrmRPtgt7i06uXDV-2ikOS-CTJi9kKEeoDce4iwnSgu5XZg0Fo6yxgReHXSDkrj_fXsor-j6mUReDKxBNxFM0ZfVSGCiVOetPLe-EH80RyiuLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس توسط بیفوما در دقیقه ۴
⚽️
پرسپولیس ۱ - ۰ صنعت نفت @Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/467330" target="_blank">📅 18:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467329">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9sGTXnrCdVGp4ytbSlS5pk_G2L69P7RtEKpXGheTaE9PAR1ugcLhrvf5unNe-8R-Z8NoRrnzNxWWcQz5hpQqD0MUZ4tDW37Yjdmf3ANQ_ANFo80qVIZd0fXKNsU05gy6dRBb0sFtUJpScGsle-GYOh9EJYlUB3LGa_MzHpbizjNtW1TYmSGmuUKrfROhSQjpHe8CYMtgr37kBSYAa5eFJThwqdsa_CYqGn_KM2PxJM4SjDkYHfgcsZfzqyvZ0J6pdbi9_58pygEaEeWwfi6wMjAfvjEDIpdcjO8XSoagiRtSIm5SgSyF3juCF_YVpPjurt8oqcw7c8L3oHM2FGDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  یمن: مانع حرکت مزدوران سعودی به‌سوی باب‌المندب شدیم
🔹
سخنگوی نیروهای مسلح یمن: تحرکات مزدوران سعودی برای پیش‌روی به‌سوی باب‌المندب با مقاومت رزمندگان ناکام ماند و حملات موشکی موجب تخریب تجیهزات و کشته و زخمی شدن ده‌ها نیروی دشمن شد. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467329" target="_blank">📅 18:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467327">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3cdYsJYbS6YqSfX0NaNXqA5llkvQ1sNX_5EBHourj6tbBF42Vlf6bROGhCBOdcXod5U_-MPuJytHYKqLOL5ioiSw0el-bnrlOpnmrdkP2rfqgICiG_R2WIjgTKBS08f7mGZAUCJMOK9MLWGfHlgqw0Okj_67ntEaDBYlVXkco6sXtH3Sysf4dl-62JAoqWv5Iv2r2ZCo1PChSif_ILkq3WdlsLBR9ldoWM6OUdGb8OKFYzJP5uU0SfsrVPQ2bqqDqNTl-uXUzdbm9VgfD7WIxTOkZIwBD24CFD4NjqJzuJx6kC6pidLjUX-IzspcCxA7Fc22FbUse7P8kRQ8H7tAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
یکی از ستون‌های مستحکم امنیّت کشور
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/467327" target="_blank">📅 18:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467326">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbad3ed44.mp4?token=AkjoVcwfxeqeocoa1d1_neAfCJPbzq_NMF-moiP3PD8hofFFtkqZdIewEUVBYugPKrkO7V8kMN9gpV8qH0u8X0yHB1477fj86DLmhwJzRHg7oZXj4VYwS4s8qADdE2k6iFD2C2QsCCr-l9eLI7F76RKATQgrsAfy8o1E3RxwSbo8McIDlClksnQVoZDGNZCabFk1KT7u2JnMRuelOqQ_sYHlckTq_usvHTo57WkwPAMrL8NsROmNjoKyGo0KKMQA9jyH0CeXRQvGYDw8jYzx3k-ZRQMdaAd62aSG3fBqYbyCtdoswpxp2nYo3f3yh00_kVJZkk7wETgdHH4Dk1DFJWvouFF7EmFEJHABJFnoEfOdF-_PI9y6HH9modsxE9J3oyAu65hbjW6JDPJ8UyQZKDpbqSr5fcL1maXuNrCNlXu7jcOvNiq7c4dLXqYYoGUs70HfQUsmeL0HSvf_AGvrMlWcWFDho9E9oaDIa6Y_rzz8DBB9b0Eg9_S_n2b3FGZCL1Lv5o1xsZDJ9XF-xwQ0NE1dgcmv2kmjl5Vg5xcHtk_AMGDjar0Z36XON8l5HWVQqbUSYSzKxGSaDPmFREaYCwQXhRuzTlqzCeDzeBS9sEerg8MW5Mj2URwF62Y1fEMOhdZrMe97tVP882EvdLI_WxPrkPjCdNw-S1TlVkwV_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbad3ed44.mp4?token=AkjoVcwfxeqeocoa1d1_neAfCJPbzq_NMF-moiP3PD8hofFFtkqZdIewEUVBYugPKrkO7V8kMN9gpV8qH0u8X0yHB1477fj86DLmhwJzRHg7oZXj4VYwS4s8qADdE2k6iFD2C2QsCCr-l9eLI7F76RKATQgrsAfy8o1E3RxwSbo8McIDlClksnQVoZDGNZCabFk1KT7u2JnMRuelOqQ_sYHlckTq_usvHTo57WkwPAMrL8NsROmNjoKyGo0KKMQA9jyH0CeXRQvGYDw8jYzx3k-ZRQMdaAd62aSG3fBqYbyCtdoswpxp2nYo3f3yh00_kVJZkk7wETgdHH4Dk1DFJWvouFF7EmFEJHABJFnoEfOdF-_PI9y6HH9modsxE9J3oyAu65hbjW6JDPJ8UyQZKDpbqSr5fcL1maXuNrCNlXu7jcOvNiq7c4dLXqYYoGUs70HfQUsmeL0HSvf_AGvrMlWcWFDho9E9oaDIa6Y_rzz8DBB9b0Eg9_S_n2b3FGZCL1Lv5o1xsZDJ9XF-xwQ0NE1dgcmv2kmjl5Vg5xcHtk_AMGDjar0Z36XON8l5HWVQqbUSYSzKxGSaDPmFREaYCwQXhRuzTlqzCeDzeBS9sEerg8MW5Mj2URwF62Y1fEMOhdZrMe97tVP882EvdLI_WxPrkPjCdNw-S1TlVkwV_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌صحنهٔ خبر بازگشت گلشیفته فراهانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/467326" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467325">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
نمایش دستاورد علمی ایران در درمان فلج مغزی کودکان برای اولین بار؛ سل‌تک فارمد نور امید را روشن کرد
🔹
همزمان با روز کودک، حدود ۲۰ خانواده از کودکان فلجِ تحت درمان سلول‌درمانی، در جشن «رویش امید» گرد هم آمدند تا روایتگر تغییرات و امیدهای تازه در مسیر درمان فرزندانشان باشند.
🔹
سلول‌درمانی، فناوری نوین پزشکی در لبه دانش جهانی است؛ عرصه‌ای که ایران با تولید ۲۰ محصول از حدود ۱۵۰ محصول سلول‌درمانی جهان، سهمی قابل‌توجه در آن دارد.
🔹
سل‌تک فارمد تنها سازنده داروی فلج مغزی کودکان در ایران است و ۳ محصول دیگر در زمینه درمان‌های پوستی و مفاصل دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/467325" target="_blank">📅 18:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467324">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpuzuAyofTSxBEa-wg83-2iLNMCcjmHcfF56VS6wcbmuoQmYwK8DRv8P3keJX59N5-ViuRlnyX-H72ZVK_OZdR5IQi5WCMFTMnJP2aA1pFcYIxJpyeFnwbuXPPRH5us_ZmIY1myc8tfqJsZ-tKN-ODtiALvXycP66A83qcYMXC8l5rP5V-HPhob3tTfYyVg4pLHZwRWMW_3Mji7_xTTTHrJA7QI5dd-duPChWMY5fKfy1qq9pCaKadP68tbBsqZcRBT5hzI0qlalzCXyGkp9uTGLrovpDghD3hZi2V9zeY4ObZi3Qlsjhf-t4iBui6x2MhOaSFhhYUsXbTUCqgDweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/467324" target="_blank">📅 18:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467323">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/467323" target="_blank">📅 18:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467322">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opAbzu2Dye8yTUWjNYBMbMWJ2DymGScJTkRjBgvARkyzVk2MWou4r2L0H8-q8e0EFG9T5nwI8bS1pgJsXoW8qwzb2M-drGNHhz0lAFEt_Kq5omPRfmPmlK5k11VyZ0W6PQ7y6z-3_tQNfdfh_QKDCJqkAK1Iy1gtpqMT0AFIyKqk7XCmJDzHIeXr2US_wwXCP9MUSIHdcDLjIGAlBOGiHUU3rWeMK82ehMYpdo4dHYytonDlX0TnCAo5oAUoASepfBbeUH0l6r_DYosrzEj7MWjfuVf7z1cjzmlpI-IIYWWzEcO695E5y9MBK1k3b7p5WrbKRjXQYtdadN_stnhbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار مدیریت بحران به ۶ استان کشور دربارهٔ بارش شدید باران
🔹
مرکز مدیریت بحران کشور در پی صدور هشدار نارنجی هواشناسی برای روزهای ۱۸ و ۱۹ مهر، از استان‌های گیلان، مازندران، گلستان، خراسان شمالی، خراسان رضوی و سمنان خواست با تشکیل جلسات ستاد بحران، اقدامات پیشگیرانه را اجرا کنند و دستگاه‌های اجرایی و امدادی را برای مقابله با رگبار باران، رعدوبرق، وزش باد شدید و گردوخاک به آماده‌باش کامل درآورند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/467322" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467321">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7qoKyfDccEwbvNtS5TqtZR_8MIAp8nOSLSrOdgOWfuezsDhITXaZZVP1cvmoJEtIbnVL1O6FAsBwjAIGlSblT00VFrpDyypN7XUtURI07j2twy_L2b8AeJOomjZ2Pr605ov0ZKb-XJuiVX8AVkN5qWvYR-mBmEX6vpiQc_7wZdXHEJShi8wJuG2qIldEZEMZulkTssIrpVIilNQlYpc6Y7NyeJoJHUQOMipYPxFsAyqe8r03eqMOE4hNdcjX-jaq_yJbFE3SXWXbsyWB3Dhq9nyWwg7ipvNB1_GI4a2cpqtKywTFAgSmy7isRX0W1cGNh5AxQiDK2OIJsjWaEYOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش سخنگوی وزارت خارجه به مواضع متناقض فرانسه دربارهٔ موضوع تسلیحات هسته‌ای
🔹
امانوئل ماکرون رئیس‌جمهور فرانسه به هنگام آزمایش یک موشک بالستیک دارای قابلیت حمل کلاهک هسته‌ای می‌گوید: «برای آزاد بودن باید ترسناک بود؛ و برای ترسناک بودن، باید قدرتمند بود.»
🔹
اما همین امانوئل ماکرون درباره ایران که از اساس دنبال سلاح هسته‌ای نبوده است، گفته: «ایران هرگز نباید صاحب سلاح هسته‌ای شود؛ نه امروز، نه پنج سال دیگر، نه ده سال دیگر؛ هرگز.»
🔹
مسئله این نیست که فرانسه چرا بازدارندگی هسته‌ای دارد؛ مسئله این است که چرا منطقی که برای فرانسه ضامن امنیت و آزادی است، درباره ایران، حتی در بحث از برنامه هسته‌ای صلح‌آمیز و تحت نظارت بین‌المللی، ناگهان به «تهدید» تبدیل می‌شود؟
🔹
واقعیت تلخ این است: آنها صلح را برای همه نمی‌خواهند؛ انحصارِ ترسناک بودن و مشروعیتِ ترساندن را می‌خواهند. خودشان باید قدرتمند و هسته‌ای و البته ترسناک بمانند و دیگران را حتی کشورهایی را که صرفا به دنبال انرژی صلح آمیز هسته‌ای هستند، با تصویر دروغین «تهدید هسته‌ای» محدود کنند.
🔹
صلحی که در آن قدرت‌های هسته‌ای، سلاح خود را ضامن آزادی و امنیت می‌دانند، اما همان منطق را برای دیگران تهدید می‌خوانند، نه صلح، که انحصار قدرت بر مبنای خودبرترپنداری است.
🔹
نظمی که برخورداری از امنیت و صلح را حق همگان نمی‌داند، بیش از آنکه حافظ صلح باشد، مشوق سیطره‌طلبی یک جمع خاص است.
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/467321" target="_blank">📅 17:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467320">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3b26fd38.mp4?token=Z5356hTGDEr1o_aOsv0Yev9PFAe0GS6Zlfaf2HLgjtlxMDGQ5wJtn01nUQNVF41QuxsiZnMBcB5ZRc8GZ6t_pgoKIc5sKZTULXWfBGR8wO1WnVxODMEW5chP7bwGA_sDXD4n8cIXA2W517nxq4wtgsa3QaUPAsqOhEJvhOpj8US8D6TL4BBvu4ca0uBi_QpiePEDWKLAwl_vDDLzVR54LIciXhLOLjGinW7aInThoNxdmt_muD7wV6K8BoqAlxUhWMJLe3huuhKjCPWd6YNOKUHOwXzbNtXDeDNcSEgAIjIaRY1RdrYuIPZwhpn7X4a-nb_Xdqaq3j4_t6bGEd-mOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3b26fd38.mp4?token=Z5356hTGDEr1o_aOsv0Yev9PFAe0GS6Zlfaf2HLgjtlxMDGQ5wJtn01nUQNVF41QuxsiZnMBcB5ZRc8GZ6t_pgoKIc5sKZTULXWfBGR8wO1WnVxODMEW5chP7bwGA_sDXD4n8cIXA2W517nxq4wtgsa3QaUPAsqOhEJvhOpj8US8D6TL4BBvu4ca0uBi_QpiePEDWKLAwl_vDDLzVR54LIciXhLOLjGinW7aInThoNxdmt_muD7wV6K8BoqAlxUhWMJLe3huuhKjCPWd6YNOKUHOwXzbNtXDeDNcSEgAIjIaRY1RdrYuIPZwhpn7X4a-nb_Xdqaq3j4_t6bGEd-mOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان پس از شرکت و سخنرانی در ۲ اجلاس سران کشورهای مشترک المنافع و اجلاس محیط‌زیستی خزر، ترکمن باشی را به مقصد تهران ترک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/467320" target="_blank">📅 17:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467319">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af5WWh_l5Q8GitdfzK0EslFOUxJQqZdH43vHbUH_gMm8xDBFkj5pqXPkyKaGAyoe-NYXeVYOjPj46-E0Fb93Nsr7YqxPgmzIRzw4ADtTPBA9Rk8DuFT33_QYYMggSgsQHmYfuEhdvh7MVq71a5O7EDTNtIGW20dBHprWw_SA4U36_33Xi0waxa8uSOKL1_T_r9V-fTBLSrD6G02HaayadlR2nEouyfMpUHsPw7OdshEcZAP--yW0kubI608KrjJIAVzGlB-IekFXEE2v0Xa4HDehnZ4Bjnf-AgRnw1w67gRicnXAbbHNbkVGswW4lh6brZgtUOw-7aIkqKh7ENHupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
انفجار در مسیر خودروی پلیس در زاهدان
🔹
دقایقی پیش یک بمب کنار جاده‌ای در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان منفجر شد.
🔹
اخبار اولیه از جراحت چند نیروی پلیس در این حادثه حکایت دارد.
📝
اخبار تکمیلی متعاقبا منتشر میشود. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467319" target="_blank">📅 17:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467317">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080ffd578f.mp4?token=CQOKx6FKELaCxnzM60SCg6myjZ13KqEpzKwOrP7BjeBcM6B1d7IT8BidfU2ORmKcrBHLuGnVZs3O2EWZdQLbYkgDaB47PsIKZUN-T-581xlQKNqo66oZ1IO_mtaGA2lSp6O0po7gISynKR5Tn-uU6ipi563IucR_j8gXM76hrHC2ZrZsdfFRx4ej4OdfYdmHEQRXxgp1b5gMx9uVs0Piljq3fdUIwrnk5DK4o69_-Ugsm-dVOGr6qEIN_CGkAFHIEOIqZlmFhWvnzzHcauFw5Tb7elL7F0aq9ivlM_vr-YjlU0ouKAl7oQ-Iw1GCpazEnhaMwYvmzvsNnTh4VTGtcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080ffd578f.mp4?token=CQOKx6FKELaCxnzM60SCg6myjZ13KqEpzKwOrP7BjeBcM6B1d7IT8BidfU2ORmKcrBHLuGnVZs3O2EWZdQLbYkgDaB47PsIKZUN-T-581xlQKNqo66oZ1IO_mtaGA2lSp6O0po7gISynKR5Tn-uU6ipi563IucR_j8gXM76hrHC2ZrZsdfFRx4ej4OdfYdmHEQRXxgp1b5gMx9uVs0Piljq3fdUIwrnk5DK4o69_-Ugsm-dVOGr6qEIN_CGkAFHIEOIqZlmFhWvnzzHcauFw5Tb7elL7F0aq9ivlM_vr-YjlU0ouKAl7oQ-Iw1GCpazEnhaMwYvmzvsNnTh4VTGtcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان سهمگین در راه سواحل آمریکا؛ هشدار تخلیه در سه ایالت
🔹
مرکز ملی طوفان آمریکا اعلام کرد طوفان «ایسایاس»، قرار است شامگاه جمعه به وقت محلی در نزدیکی مرز ایالت‌های فلوریدا و آلاباما به سواحل آمریکا برسد، به یک طوفان بزرگ رده ۳ تبدیل شده و سرعت بادهای پایدار آن به حدود ۱۹۳ کیلومتر بر ساعت رسیده است.
🔹
بر اساس هشدارهای هواشناسی، وقوع قطعی گسترده برق، بالا آمدن سطح آب دریا تا حدود ۲.۷ متر و بارندگی تا ۳۸ سانتی‌متر در مناطق ساحلی محتمل است. همچنین احتمال شکل‌گیری گردبادهای ناگهانی وجود دارد که می‌تواند فرصت کمی برای واکنش و پناه‌گرفتن به ساکنان مناطق آسیب‌پذیر بدهد.
🔹
در پی نزدیک‌شدن این طوفان، در بخش‌هایی از ایالت‌های آلاباما، فلوریدا و جورجیا وضعیت اضطراری اعلام شده و دستور تخلیه برخی مناطق ساحلی در آلاباما و فلوریدا صادر شده است. مقام‌های محلی از ساکنان مناطق در معرض خطر خواسته‌اند هشدارها و دستورالعمل‌های ایمنی را جدی بگیرند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/467317" target="_blank">📅 17:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467316">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUb1SpiAXAYCrZtebekwzb8Stnrz_aCcSByaEXKG_Crxuy2qU_mv9_q35QG1HiFyLlhpEy3BFN4NUzN0o1yae-ExnhUjux9tLEkMYs9-4I1Xj_GthnXrOUAi4lDuWpbfWaz_Uki3FeiEwJ6E3F7LYNjtYNcKrPGfne92IR9z9049I8Y18Eo2FZvS1CFooHJrNvhLNeP_Gf-bp5LnScS7GpajINLgCxaAgCh1NTgEmNyCTyK6Z-bCsoyBNn7uOyK7QW05WhkAvq34z7gVmY6o5MSsPjl5tzjNM37Xya9Bi2UrbotRj9SWT6s2mwdmRgpzC9SDyt1kXmIZrgXczm0WUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس آمریکا اسیر هرمز
🔹
ریزش ارزش سهام شرکت‌های آمریکایی در سایهٔ تنش با ایران ادامه دارد.
🔹
مطابق آخرین داده‌ها، حدود ۷۰ درصد شرکت‌های بزرگ آمریکایی در ماه گذشته میلادی بازدهی منفی داشته‌اند.
🔹
افزایش تورم در اثر ادامهٔ تنش‌ها در منطقه و کاهش عرضهٔ نفت، شرکت‌های آمریکایی را با بحران مواجه کرده است و پیش‌بینی می‌شود این بحران به زودی دامن‌گیر شرکت‌های پیشرو بورس نیز بشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/467316" target="_blank">📅 17:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467315">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترکمنستان چه می‌خواهد و گلستان چه دارد؟
🔹
ترکمنستان سالانه میلیاردها دلار کالا وارد می‌کند؛ و سوال اینجاست سهم گلستان به عنوان همسایه اصلی مرزی از این بازار چقدر است؟
🔹
ترکمنستان در سال ۲۰۲۵ بیش از ۵.۱ میلیارد دلار واردات داشته، در حالی که گلستان در همین سال ۴۸۱.۷ میلیون دلار کالا به ۲۸ کشور صادر کرده است. لوله و محصولات فولادی، فرآورده‌های پلیمری و محصولات غذایی، بخشی از ظرفیت صادراتی استان برای حضور در بازار همسایه شمالی است.
🔹
اما نکته اینجاست که ظرفیت به‌تنهایی کافی نیست؛ رقابت قیمتی، کیفیت، بسته‌بندی و حرکت از خام‌فروشی به سمت محصولات فرآوری‌شده، شرط ماندگاری در این بازار است. کارشناسان نیز بر ضرورت شناخت دقیق کالا، خریدار، قیمت و مسیر صادرات تأکید دارد که اینچه‌برون می‌تواند دروازه ورود کالاهای گلستان به بازار آسیای مرکزی باشد.
🔸
اکنون سفر پزشکیان به عشق‌آباد و اکسپو ۲۰۲۶ گرگان فرصتی است تا دیپلماسی اقتصادی از تفاهم‌نامه عبور کند و به قراردادهای واقعی، سرمایه‌گذاری و اشتغال برسد.
🔸
مسئله گلستان کمبود ظرفیت نیست؛ مسئله، تبدیل این ظرفیت‌ها به سهمی واقعی از بازار ترکمنستان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/467315" target="_blank">📅 17:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467314">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
تداوم حملات هوایی عربستان به پایتخت یمن
🔹
شبکهٔ خبری المیادین از ۱۰ حملهٔ هوایی عربستان به جنوب صنعا پایخت یمن گزارش داد.
🔹
المیادین گفت که در این حملات، شبکهٔ مخابرات هدف قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/467314" target="_blank">📅 17:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467313">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104e3f811.mp4?token=ti8bss-axaTxHSUhClOeQiZGzxrA_XquTBZg9euC_1XLhGJGm7t_5a8EpUCqSX_wunrpUVyAhTk6a6gzt01te2ClBtw9hXhFBCmmmnF3a5FBTwB5PVycVrvKZf-N353hPIUzFweVChefD3TodFbFsalhr7bG42KQrXQ2yO8ijPqyua2E_aj7s0xLckX7q5Zv8g2JFvEpKNCjkVr40JLVEKXe9dUj9ESQEujvWdTjW1GNuhmpU46r4guJCMfdWHWXS5kXlLbaOO02R8TPnEFE3SIkzLKUEQ37CZC0_wqwn41waHyywzyeO_NMRGWGbaZ6umvkXXZiVkENTUndwqvNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104e3f811.mp4?token=ti8bss-axaTxHSUhClOeQiZGzxrA_XquTBZg9euC_1XLhGJGm7t_5a8EpUCqSX_wunrpUVyAhTk6a6gzt01te2ClBtw9hXhFBCmmmnF3a5FBTwB5PVycVrvKZf-N353hPIUzFweVChefD3TodFbFsalhr7bG42KQrXQ2yO8ijPqyua2E_aj7s0xLckX7q5Zv8g2JFvEpKNCjkVr40JLVEKXe9dUj9ESQEujvWdTjW1GNuhmpU46r4guJCMfdWHWXS5kXlLbaOO02R8TPnEFE3SIkzLKUEQ37CZC0_wqwn41waHyywzyeO_NMRGWGbaZ6umvkXXZiVkENTUndwqvNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس توسط بیفوما در دقیقه ۴
⚽️
پرسپولیس ۱ - ۰ صنعت نفت
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/467313" target="_blank">📅 17:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467312">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwXopFHhK0t_xhd3Pz2e9vobjU75MCvp9HBxWp_zux3M-egBvtJpDKD_sGER06Wojki9j2wDc6rGTeJmGCUKO9xfksJFLb6n669k_TE0IYhcWp_LhoT7TN0VE4DJ-xNRirOS2R6Oq-MLcgblW1jQK6r5n88FJS_NVBIRwcgEPYX7xPJa6iwJLFNVX0Ccu1KyundnAIhGKRUlIbUM1C8pVN0ED9kaeoxrSUWXCGxYFoTncmPIIDzAFDC7_hsXGI_ieyafVYk0Xz2P_ji3vmxpbgUa3nU3ESDDO2RKhOCkFuYqXvGQWhvhgo2WTDtv0nq1I5plvBohgUdg8tjEou7pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا پزشکیان در عشق‌آباد برگ برنده را رو می‌کند؟
🔹
سفر رئیس‌جمهور ایران به ترکمنستان، فراتر از دیدارهای دیپلماتیک و گفت‌وگوهای معمول، می‌تواند فرصتی برای بازتعریف روابط دو همسایه باشد؛ فرصتی که اگر با تصمیم‌های عملی همراه شود، معادلات منطقه و به ویژه شمال کشور را تحت تأثیر قرار می‌دهد. اما سؤال اصلی اینجاست: آیا این سفر می‌تواند به نقطه عطفی در همکاری‌های اقتصادی ایران و ترکمنستان تبدیل شود؟
🔹
استان گلستان به واسطه موقعیت جغرافیایی، مرز مشترک با ترکمنستان و پیوندهای تاریخی و فرهنگی و قومی ظرفیت‌هایی دارد که هنوز تمام ابعاد آن در مناسبات دوجانبه ایران و ترکمنستان به کار گرفته نشده است. در این میان، نسبت میان ظرفیت‌های موجود و آنچه تاکنون در میدان عمل محقق شده، پرسشی جدی پیش روی سیاست‌گذاران قرار می‌دهد.
🔹
تجربه همکاری‌های منطقه‌ای نشان می‌دهد که همسایگی به‌تنهایی مزیت اقتصادی نمی‌سازد؛ آنچه اهمیت دارد، تبدیل ظرفیت‌های جغرافیایی به سازوکارهای پایدار برای همکاری‌های مشترک است. از همین منظر، دیدگاه کارشناسان درباره آینده روابط دو کشور و الزامات عبور از توافق‌های روی کاغذ، اهمیت ویژه‌ای پیدا می‌کند.
🔹
ایده منطقهٔ آزاد تجاری اینچه برون _ آلتین‌عصر همان نقطهٔ عطفی است که می‌تواند پایه گذار روابط نوین این ۲ کشور همسایه و تحقق اتصال واقعی ایران به بازار ۲۲۰ میلیونی آسیای میانه باشد.
🔸
اکنون نگاه‌ها به نتایج این سفر و تصمیم‌هایی دوخته شده که می‌تواند مسیر آینده همکاری‌های تهران و عشق‌آباد را مشخص کند؛ تصمیم‌هایی که آثار آن، در صورت تحقق، محدود به روابط دیپلماتیک نخواهد ماند.
🖼
سوال اصلی همچنان این است: آیا این بار پزشکیان برگ‌برنده را رو می‌کند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/467312" target="_blank">📅 16:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467311">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c2f4c6813.mp4?token=HFVWAzVII86HxM7Uqc0Py3Suu2g-HJaPiQy7cWzxzyHutGylEV9IQjIDQM4LsZrHA99qzk-ElE_B4LkEjj9GYtyAZdwy_yZBbFy8ZRA025PVB0k6RbxxVTb-TXj-ztbjBlQdt0MV54fVqPDLM3Nv9o9xmTVjJa2YGZsQLNm-dwhYVtmfNyuG4vJbnsWVYuDAAPlDlHEYP7A4PtMiGiW07DKHujix6SYpWkeh3hcF1QAGeP1zP-OgdBmesEF8Sz7rSdT0hjwxr4dBloO2wCqJeS9NEEEJ496WRQVCoatiRwqEmGSvIaLV0AjV8HLD79Gcf7NRvFNopO_56oLMnlUZTDKvTcWcdsNHBAn6shIa74H_XtE6x46N6Vr0iSBApZgD_rQ7K5Is-tyVAyYy0wjoUx6JmyFcFTAghCzXuddIdODvNiLhe9qGc7CrFcorypNuQ5fnCgYamqaY34dNf4tzeguSNmLoi-nPcy-l7hnQ3mmXrP0hIGc3bf2LTnz9Ez5N3EEJBWs5AB0-s_zAJX3IWsLH-elrtOExEaz3hoBQx60NWYzx6YIRevi0I_ihTeHxm4rimSAnQCMqIPhzfcZ8EpCG15ULCy_9IXmhyRKJqwtEBH0kvAkqyYc3H-zcZvTgpKn6iV1NOuTQlEqhG2UjkQMtezEo8zhaRtsmuEIdL2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c2f4c6813.mp4?token=HFVWAzVII86HxM7Uqc0Py3Suu2g-HJaPiQy7cWzxzyHutGylEV9IQjIDQM4LsZrHA99qzk-ElE_B4LkEjj9GYtyAZdwy_yZBbFy8ZRA025PVB0k6RbxxVTb-TXj-ztbjBlQdt0MV54fVqPDLM3Nv9o9xmTVjJa2YGZsQLNm-dwhYVtmfNyuG4vJbnsWVYuDAAPlDlHEYP7A4PtMiGiW07DKHujix6SYpWkeh3hcF1QAGeP1zP-OgdBmesEF8Sz7rSdT0hjwxr4dBloO2wCqJeS9NEEEJ496WRQVCoatiRwqEmGSvIaLV0AjV8HLD79Gcf7NRvFNopO_56oLMnlUZTDKvTcWcdsNHBAn6shIa74H_XtE6x46N6Vr0iSBApZgD_rQ7K5Is-tyVAyYy0wjoUx6JmyFcFTAghCzXuddIdODvNiLhe9qGc7CrFcorypNuQ5fnCgYamqaY34dNf4tzeguSNmLoi-nPcy-l7hnQ3mmXrP0hIGc3bf2LTnz9Ez5N3EEJBWs5AB0-s_zAJX3IWsLH-elrtOExEaz3hoBQx60NWYzx6YIRevi0I_ihTeHxm4rimSAnQCMqIPhzfcZ8EpCG15ULCy_9IXmhyRKJqwtEBH0kvAkqyYc3H-zcZvTgpKn6iV1NOuTQlEqhG2UjkQMtezEo8zhaRtsmuEIdL2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: گفتگو زمانی کاربرد دارد که در سایهٔ زور نباشد  @Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/467311" target="_blank">📅 16:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467310">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
تداوم حملات هوایی عربستان به پایتخت یمن
🔹
شبکهٔ خبری المیادین از ۱۰ حملهٔ هوایی عربستان به جنوب صنعا پایخت یمن گزارش داد.
🔹
المیادین گفت که در این حملات، شبکهٔ مخابرات هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/467310" target="_blank">📅 16:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467309">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
انفجار در مسیر خودروی پلیس در زاهدان
🔹
دقایقی پیش یک بمب کنار جاده‌ای در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان منفجر شد.
🔹
اخبار اولیه از جراحت چند نیروی پلیس در این حادثه حکایت دارد.
📝
اخبار تکمیلی متعاقبا منتشر میشود.
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/467309" target="_blank">📅 16:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467308">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gqr448du8Ll0E7aQApBo83cPlBh6bbKg9vCvTXqf7pS0swunF8LAKAt8DWQfUybREOQm5CoUwxG_qjR1PVmcdKVej-F3kitSVMSTrEYX-ECXtHTKeuoK0P22wRz68v22-zWOLp9lzJ3mwDLVmoJcoaKxchv7gtsYrJSrcwHoktkq1Km2RB56e4gztu-UMuUjjlRC842Mx5wtbMe3VahLeqHCBBcgf0UsrW361W22Fzhy2bUDumPHZdVDFmg-K52hthXD9QrD46xWILQze1GTNXdJ-dgo-ZNrtvpQ3_1IAUmmywlUUNzQPxP5GLd-O-GfP_kI1r7U09ze1J9kQ6jR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش حمله به یک کشتی در خلیج فارس
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) از وقوع یک حادثه‌ امنیتی برای یک کشتی در فاصله ۱۳ مایل دریایی غرب منطقه الجزیره امارات خبر داد.
🔹
این سازمان اعلام کرد که بر اساس گزارش‌های دریافتی از چند منبع، این شناور در حال عبور از مسیر خروجی، هدف اصابت یک پرتابه ناشناس قرار گرفته که در پی آن آتش‌سوزی رخ داده است.
🔹
به ادعای این نهاد، آتش‌سوزی مهار شده اما وضعیت خدمه، میزان خسارات وارده به شناور و پیامدهای احتمالی زیست‌محیطی این حادثه همچنان مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/467308" target="_blank">📅 16:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467301">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgXFGHW13unDH2Dds_3CCf6kpvIKbwhnL5Q4DVbSQG_X90Ul_lkk6VTGlHFc5qllab42zIufZX2u-oJ4nFssUdf12TnGRJqc-U3dXatKfktbf9znWPlLReC93tUZPmIUDD67eLqBUidCFFDFSDkVCw3TCW5OQr0wBGLGJ4PYrltqFbuudXtLPVxlKywGykaIlJtHowNWh8GGluk2uT2FRGW4mUXqSpK_OXdpDo6w0sf5UXPo_BsE2Y-hYZDudnGib3mxXgxr-4jPC3i9zVl3SN9wiQwwTqM_5FCJapKA3-bIIRs4eq8UF6GEd_fzKoWyBy_h3ixodX_YF70YlEXzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqTfc8-8w0CVynehHQzxr3yrQDEsYBXgFElD8uW9JDep2NumpQfdoUFcjO-mcrk1vyjx0UhQ22m6uqWksSF14mu4yPmOs_fS44R2cFbow-0aVD7Kzk28zBi6ZzxQ2HSBggOPGI4y7xIoWinm4LuPQg_b0wSPAx0SfSuI84N0JRVmVBTvLJZbnDaJW4ITEI4EwVXMOZMqeneLMr19NY4_ndJtYcBacdBAXoJjhlroVNSClsP9cQQ5vupB5K7jFHgpN9uTGZ1P4FBczrRIQTfpqg3q1DbxbMj9hGJFmcV_uUixgZbE8qdghzGoE8Inm4MYgXFcQaWcX859xv-yoMJo5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrT4XrVecjBxbe1zu6Yu4RGh_RwpoeKpz6zUUt48ZwZTbLJP4MgzGAhHNtWrODvHPho35pDIYJQa15La1JTVpjg252aEAxfjtDbvX8IpdNgr2Z--j_WDtRnA86Y2XWQCEkfpGRkrYPMfvI9CTOrU6k18YEEOXzh_zx5FUdQyqw70xbVgIrHhgMGnTp7a6EePlZRCn-UrYYdpb92-kG1xnYMEnk5Xf0A3i3ZGzRFM1WVqaMGZjKNY6sTEw5PV5XQ7W7sclpk-hFSc2ggwfTAvOhwUJRTAlTrYgaZof8fBmic8-Gb-KIaUi8sNh0YoRjeIFLe4ZHe3e4F-CkLPEQIkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUuLR5Wdbdn4lOBAYKIRW_KYPUogB6xwHVnuQb-LakxQdN68yY2eKCkqKongiW91N6Yf8IqrN47Ywbep3ZG0KZdS96XMVyyyhiSTuHYiqLTwNxPBAw4qvm6S3yOcq2D6dwSkPLSn8-UOu5sGeDyAMKRc-FspS_Aw0zOxDADxf2JOPpj5WOGl_EalqMIC3mG6_S5f0yx1-KN4TepXfTLQQT86k0Y3IXArnZVNErHBxb2NqUlLH5vjN5Z0bO6UwpayGn0ypapDMMv8ioEnOXn-TN4AifhwzHtt63pMY14soWhQg5R7A3wM_fDx_c7houbkqADzhoj4ECEO3TX48yHqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXx-LY-tWppxxzWWCBnl-aRXoHGRl-Bvi5iG-SGLAMVPai_NRgiWbwYLiZdVvfFCvRyA7PgPktTNuJ9k1C_qWbgItxFlpfXm8uui3-GuZmU-M-waE2UtHSxjyN3tjg4vYmwp-4NODGJEOoBPiF7chyRwXavhSPVGdLrlKU3jUllcLtZKxiUQHybFrDTrriGmdSMGGBt_kw1IZ4FsYFRtWlHZyaHXwKO4V5g4wzwAww9nUKSqvgRGw1PExI-tuFztpMOrRhEYPJfTUQWGZJ-_AEgcjm7lPIv3OsHpQuPROy2Ygpa080HXXlBY7PNBOWiF6mH63kDVY-nyGxLAO3CJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUx30wr8x-UeBBS_SHWHHXIRhRucVjZsb0F7KZuAwz_fWtjKA4hNfRkdgVlvKBvU9X_riZ1nZcpOAC0-_z_3ze-8QgBz3-EcDeGQ-P5u4ACw-soFRETPxd3I8hbSrwlTc9U1vWawNsDbUFoRn898sFOD6VeD5UGgbfn2QfPaY2EmBwWjgkm7NxzFm_LbOGWj_FC2ggIbpU6cOXceoN7BvtqMYRrkSWsrWXQkQbogObStsgBRew7Dv1ZLrwmESz2NUFrjGMtUqj5qdkcdHU2FlN23fSg4GZsRygSJsP7q6RUTfWpOkVsK-HNgi2Ok4f5JHDX2TE-ORKDbmuoNFSoU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyUxNX_nodrV_jNaVWhqbQ56MVFguuJq-YnU--22Z23uU6xFjWUzpr6W9qEYkVHtWx09soNIvlLjBm-lrpWvbDZMppiyZEJhW4hE7-tAgpfVZFw9PFkX-CDVyZ2YdGeXhfk_cih32DSDkBwBVFoE-Fn8F6pQFgLWiEz6hlugcSNZcP26h9ZaoAaLv5M-GQUqLEnLYnindLPxl5r0ww-RKMAyOC5aDoX6PjJM0zRG7CiWAfoGM0N0e9bzOOokOYqGGwCrsLKiZPqagt2tOjdzhtJHcDeQdXPxYeQdBMETSTIqX7KsWH5lapJZLlDR2TW-6yZj4l6cFjVJyEzHUrlZAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ خطیب جمعهٔ تهران: تنگهٔ هرمز تا تحقق کامل شروط ایران باز نخواهد شد
🔹
حجت‌الاسلام والمسلمین حاج علی‌اکبری: ایران شروط هفت‌گانهٔ خود را اعلام کرده و پس از تحقق آن‌ها درباره اقدامات بعدی تصمیم خواهد گرفت. وی افزود تنگهٔ هرمز تا زمان تحقق شروط ایران باز نخواهد…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/467301" target="_blank">📅 16:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467300">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmJm3wc9IXVAwYKhSVpea3k_GxrAOoWCfjsxsP3dxWXtpF0V3NNPccQye2PBhAq0Gfy4WxLHOVSkGY1k35HWPXQ8XQYFXgHI21L5SYlzW9oe7mTByKv5n1oLtd37JfgQYo8_HjRJrO1vXTOiS3VilgwYQ6W49Z4Xw7vo8HaNqCcJSjs5ZCmC_yjr5AfbI1Dq8eJd7nC62-coSGjx7wHurDdVVPbb_WeDGotj8p5TBCpu02ahitU-tgNtiQC8-RQdvWq1-DSSGZ19_IOEGUbJVkoWuElWdcKr16MV4c2CGebIVdYSwPL8cSfT6fmntJp1jVwWTqZVhoY4gldRvUS4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شرط یمن برای پروازهای فرودگاه ریاض
🔹
یحیی سریع سخنگوی نیروهای مسلح یمن امروز گفت فقط پروازهای بشردوستانه‌ای می‌تواند به فرودگاه ریاض صورت گیرد که مجوز پرواز را از مرکز هماهنگی عملیات بشردوستانه در صنعا دریافت کرده باشند.
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/467300" target="_blank">📅 16:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467299">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjQNRzHNRTTQZJV-yiyJx0wQfYSvuPi79Qv42bu2yPzPhPKbMggbrx8d6gNaidq8wbwl2gk7_zD4aPfIB7Sq1um0xPiKGllV-acIamKgrAqvn8-tueL6tn-wqgZJqhIBvXJvu6aEdWOzEEAV8yPUoXtpsPHbqHffAWk99fNm3UtHiKxSOgE512-3TOTmCraVvYO6PtYejOtb0kuEIv7zGNSxhYHcKzrc3sTzenneZ6bji2a2S37Kzxg2jE1MPCtwe87mQrSf1iV9IAGQ0q3ERJScO9YO7JkILaHALP8nDX0IJvSGh59QB7FaoxYGgAlYIU64BIXOD4P6X9BdHw3McQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویر حکم تنفیذ دورهٔ اول ریاست‌جمهوری حضرت آیت‌الله شهید خامنه‌ای از سوی حضرت امام خمینی(ره)؛ ۱۷ مهر ۱۳۶۰
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/467299" target="_blank">📅 16:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467298">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
وقوع چند انفجار در اربیل
🔹
منابع خبری امروز از شنیده شدن صدای چندین انفجار در اربیل خبر دادند.
🔹
هنوز علت انفجارها مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/467298" target="_blank">📅 16:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdTQ7T_gpt3a_yJ-A3B_ZY00vmYqVU4DXBLMnl4142O8yIT6YyFxUlZUJE-3BnIPjBJFw7IbP3Fjy5byMIWh1NlS1lO31-_4r0FuH2pLZHYnFoBs1S2jmS3l0lkQ5CppDV3nHsNlaGXouBkWUKFX2cmC50r2yvpGdC4wW1IEE1IdoT8rDDGNeNWaT54uLzWwHLH9QFg2gMyQunW4U-IQ-lTcUFA2LtZ0sXPc9KTmhpUUl0SMNHbJ0bou9H8ldLdQ6Te_U7GrGxb5jDucTn6bybDn2djrke_IbFKszloOwWy9IoJmm-ZrfVlH-WoqorUAOpOP1uqqfvIQfWQ9hOYiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: کشتی غول پیکر حامل گاز ال پی جی مورد اصابت قرار گرفت و دچار آتش سوزی شد/ مسئولیت تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست
🔹
نیروی دریایی سپاه: ۲۲۰ شب حماسه حضور میلیونی و ایستادگی و پایمردی شما در دفاع از حق و عدالت دنیا را به شگفتی واداشته، ملت ها را به نقش آفرینی در اصلاح وضعیت جهان فرا می خواند و مهم‌ترین پشتوانه الهی و موجب دلگرمی رزمندگان اسلام است.
🔹
دریادلان نیروی دریایی سپاه در تحقق فرمانِ فرماندهی معظم کل قوا و خواست عموم مردم ایران مبنی بر اعمال حاکمیت بر تنگهٔ هرمز، اداره تنگه را در اختیار دارند و اجازهٔ حضور ارتش‌های متجاوز را در این منطقه نداده و نخواهند داد و با شیطنت‌های دشمن برای اخلال در این مدیریت با قاطعیت برخورد می‌نمایند.
🔹
در اجرای این ماموریت، ساعاتی پیش کشتی غول پیکر حامل گاز ال پی جی به نام اِن‌وی‌ سان‌شاین متعلق به شرکت نات‌ویت که قصد عبور از مسیر غیرقانونی جنوب تنگه هرمز را داشت مورد اصابت قرار گرفت و دچار آتش‌سوزی گسترده‌ در قسمت موتورخانه و سامانه رانش گردید.
نیروی دریایی سپاه اعلام می‌دارد:
🔸
همگان بدانند مسئولیت مستقیم این حوادث و تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست که با دخالت و فریب مدیریت شرکت‌های کشتیرانی و شرکت‌های بیمه گذار و پرداخت رشوه‌های کلان، مسبب چنین حوادثی می‌شود و با ادامه این مداخلات، حوادث تلخ روز به روز افزایش خواهد یافت.
🔸
شرکت‌هایی که فریب متجاوزان آمریکایی را بخورند، تحریم می‌شوند و اقدامات تنبیهی لازم در مورد کلیه شناورهای شرکت‌های متخلف اعمال خواهد شد.
🔸
من‌بعد برخورد با شناورهای متخلف محدود به تنگهٔ هرمز نخواهد بود و هر شناوری از معبر غیر مجاز عبور کند در سراسر منطقه تحت تعقیب قرار می‌گیرد و تنبیه آن قطعی خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/467297" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467296">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEJj1mLztdRrDuwAnw3XFt_IEZbO6A2DqPkCmhJlAvH0F3setNsMzbD5jbKdvxMvuuZ0wGzl9Ic4AEgfZiyIB8usvPvOBnznKRC_ncy3Ubi03rMxSaUZa8-qCHsy4idsOdjuTdEAHTqdjb4JpnSjNxmW36iMuHQKbRhhbmRqMTT8k0Thgq0f0oU7i0tbkE3--_3bq43QBQVzWwok-6kkz7iD9U5tlavKn9rciqmhrIvVwvZjGtxX3h5Rq53apodb1T9t7Z1kKTbqEB6lP_pRlHLuzcOq8recSnm7FrxoPB53I62_yt6wVL7WgWPd8HnOOYGMraJTpdI_WMlZK8MAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان: بدون محاکمهٔ عاملان نسل‌کشی در غزه، نمی‌توان از عدالت بین‌الملل سخن گفت
🔹
رئیس جمهور ترکیه: ساختاری که در آن اراده بیش از ۱۹۰ کشور عضو سازمان ملل متحد تابع تصمیم‌های پنج عضو دارای حق وتو باشد، نه عادلانه است و نه صحیح.
🔹
تا زمانی که عاملان نسل‌کشی در غزه پاسخگو نشوند، هیچ‌کس نمی‌تواند مدعی عادلانه بودن نظام بین‌الملل باشد.
🔹
توافق‌نامه‌های بین‌المللی کارایی خود را از دست داده‌اند و دیگر امکان اجرای احکام صادرشده از سوی دادگاه‌های بین‌المللی وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/467296" target="_blank">📅 15:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467293">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWZHHVYHuVB29MtEuILDepyO7czObjZqoD-JCabNGHYK_FQBzQ-zl3Ps-mg671-Tudz1lxVKFNIU6X9Yd6h578CqgRHiKJp6P5s1pds-mdapdKk_YCvq1e0jqaH1DxgXpzQn5XsTbbRgaFduiIpXCbkzKgY7cRSP1GL93OcwoAVgDX7q-rZZJgWKIR2h_8YFJ4abVKvQMB1sOwJRqoNlHDA6Gn0K8J7ITLTeAs_jiGd1xO1l6R8vYabsRnaH9wbYJ7YGsaszCxJcINHSrK5_B_RDWKgl8fUXYFc5VZ9WIML82Rz1opmTHirulmBF3luRf5v6GIva5al1wCE4NM9fMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVtaF8pQ9454yw2tNm0BKHNMK9jDGut9MIxn2QgvJ7usViQitOO0SykCExm9dqvJCBi_N6lEIoWHNYohfM_WF7H06uGJulrr4hkqmw8vXuOp3bvknMfmzoUX1CmNgS6-nGsjVXVPFqIbowb-tJ3ffvdwpN0tXiNB9Ii7jV1QiMEujh4F0byAse57Rh-ea2DhFj2LvINVZNPwwYxn7Rn2n6rcibZcYOvdLN3icR-N1xDMxe2jR-lUmjcvcC4dTk5H1YZtWdFSGPR2KIi6VIw0zxvAtfctA7yoAPZ48Y3-vti23oicurotFLe6wMdhoShLJepYwaAWk3Bes2d94eAE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2DYT_KjtI9YKWDxnMFwe25UBZxd9PRONhh8JF3AFskvC-v-KHt1eJeEOZ5rsZ9T4UQ2ZQgMXBmNKfP_9ETb4GPjl566yoTLJchwJCIiKkvpzCkhxIin9y9CpKnxkVdr3nioRe_vsabghqw4SaVW01Qg8m-PIXNrbc16u13dEoJzLTHh0s3iUpc1jza7o3kvBwv86I-vJBf4xuKrZ0NrT5LGYL4qdXzesnmctyqK1VPB9vVIb1ZZIqCH2xcHHwbVrXIimPAfqf6_IB_ZlIHYKYbhEXAggr9QwnpLfLsMfpgSaxwxgjeD4Sq7U-sinFWCEtPDueFTs_S9bjoiXAAf3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان به دبیرکل سازمان همکاری شانگهای: تاثیرپذیری از آمریکا و عدم استقلال در تصمیم‌گیری، منجر به از دست رفتن قدرت و انسجام شانگهای و بریکس خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/467293" target="_blank">📅 15:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467292">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg2IW4ZNmCjoorOX-BpFIMpQ4ayD1MAWvuOvLzJS6mXnP4WZgaNbfeYKGweTBRrlaogWy4XzE8JhTMqacnZ1lHyai2SWGsrlxQaAlyHPwlUhsVuPtCDRzfiziPz7eq4y6qp4eEQSNqMiF7kKdjztjo8Te7nGL5l3JxRm4Wg_UcB3A78e4M55r6O6hpFvqiT60AfExjsag8xJS6eGIG3rJLUTGDsj3ssL8eSU8_l6FYT7FJwaMWzusCqXfICeorb_TRiLBGK-CodHLovrDVb9dg0Pvw0VS8BBW5XtrkldDOG2YcVy0H6KMzGjiOrZPImL4YKHtRE06g8yRdfTamyEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار پزشکیان و رئیس‌جمهور ترکمنستان  @Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/467292" target="_blank">📅 15:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467291">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ddfnh4A1rwYSFAj5ZzsO2WbfM7dhDDYUHA1lDnyEWpigX_lxBepN4bkX8QSgg3JaHRs7A4z88a9Iu0GB0buDriBq1ceTgYIomrEi13WHzacoLuR2ocCOOX6Z_7_Bjb-vDBuqdA8sxHvzvikta5IHcC-nstizj33YGCJGebeZWRITlxs4_skUhku-fzfAQx4MCVJZCt6v7jFCU0TvWHrneK_HDt6VNLLTmBhkyGM07I9X7DXDR1XaXuTFK3ketl5mamg4mARYwiSg3AJj40s5mZ7JplJX6rfESP4y6aqJNhDc_h72dZBl2m5QxXDVatvjjVz9MvhJLjd95Z0oBDsTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینهٔ سنگین اعزام کشتی‌گیران به جهانی لاس‌وگاس
🔹
فدراسیون کشتی برای تیم‌های ملی کشتی آزاد و فرنگی کشورمان جهت حضور در رقابت‌های امیدهای جهان ۲۱ میلیارد تومان برای بلیت هواپیما هزینه کرده است.
🔹
علاوه براین فدراسیون باید برای ثبت‌نام در مسابقات و هتل نزدیک ۱۱۰ هزار دلار هم پرداخت کند. تیم کشتی فرنگی امروز در لاس‌وگاس مستقر شده و تیم آزاد نیز فردا راهی آمریکا خواهد شد.
🔹
فدراسیون کشتی توانسته با رایزنی تمامی ویزای تیم‌های اعزامی را بگیرد و حتی تنها مربی جامانده به دلیل نقص مدارک نیز با برطرف شدن مشکل، ویزایش صادر شده و با تیم آزاد به لاس‌وگاس خواهد رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/467291" target="_blank">📅 15:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467288">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLD1QD3H9e63YEXtbemBqYPPal2_B04q7TFg0Y94gSIIiIPo7XObreg_XRwmjEOWJMZGvjWubw6Pyfe8ugjx2cgrvkR2nlBghbProt5nvwCD7_mfC43LTtEgiaGxerLrLsfrh8Ba3EJTamFieQm99R2mCStZ7XXOutNEY27eebFbjCh5Zm3IuF7G0M00f_ZimvegUuJLNeFT_IHcQTOMKJXsJcuymjZD5imvdNyDwGox2m_X8lByhOQcH4B5sy_FiR1qKtCdCsSsWQ303A8g9XJEh5Gr_kqUocx8zh9rrRZ_R4NgD-vT-7pvbczue7-eXBHHb5K9ID2LG9G_GujH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DggUV5leLZsF4XZVz4UJx-Ajpxi5aFh4WXiujqpKz0r46toTzgmzZSe0vdGyc75dfxwUU47W9Tbsgq4FQdi6nB01uOFsuwr7kiKHjd5gVddo8FYxscmjttrjlC1gX9Vr-LWfJgrnxxHXOe74TvjLixtzzVbRUmxuy-jTb_0U3k6kltVWurQP3emMskdebuJ2SYAVpX5tnXsTWR47VoStH6hMnpyzMwiDOhZgopbM2Y0Tzv_MMjquTEn8z_L-534jKh-dWxvPX1f-707KF6wjbGEFDo2QUPZBCqj2jhdvTrDZyqth7bgYSZjVQPalInD477Q69BnjFHTmwfLV7RGcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOZFIunmz7RFWUd9GGdrCkRBPj7Dw57Q0PRL3kMGHHr426C8RfhsoHpbbUiL-xCtXDE87kUO0GjW3FgdNBp-xQa2eS9JKkYL0v53trcH0XB86CemXhPhqIEBp0PMLwut0buNM4cDGuebfahAo3uOuSCdY7VRz7P01v0ayNCPaPa7WxSBNL-EjMQ6JN59Tk3Mwd4M5Lelhy7EbclNiNBEUG54sXM9MyXPEw4jbIKktkemhBhD6wkHVy5cIdUk-4_lBenOeL3QiNa42Dvlnjwl8fwejxxo6UH6ddW6jYabAklShfayi3IpjDqXL-qnIlo7uSgHQahEpI4nbNenTDA1pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
در نشست سران کشورهای مشترک‌المنافع چه گذشت؟  @Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/467288" target="_blank">📅 15:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467287">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2HUCKq0UAx9mmrFPFYGjFKkeVEgj_5z1Y0P5nlwdsgf_3MbBrtvsT1kvsodxFfj6vOIuOadLMKNkuhjzEXx5idAGTRc69aU25hn9RJGAP0rCc1RemD1cQ0nqWKVvZL0FEHK5Aw7iXntjFbJlQGiZzYdrmbq-P8PJIiad2wUZJKM7NIpwlceHi3uruwYozPSY1wUxWQF2tS6OT76v2BGsYGqDMJ6dsvkFmdj9jWzZIm5JAdnI27woFizZYqeQ23f8dwkWA6TqmOubWKPiPEU66QUovKeqJZQ0evQ8LKH58oZtkFiTrBDu2pH_MUZTt3IOaYsYxPojx9Wii9xY7htpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامۀ تلویزیونی «ثریا» فعلا پخش نمی‌شود
🔹
برنامۀ تلویزیونی «ثریا» که با اجرای محسن مقصودی تا امروز به صورت زنده پخش می‌شد،‌ در صفحه مجازی خود اعلام کرد که امشب روی آنتن نخواهد رفت. و تا اطلاع ثانوی پخش زنده نخواهد داشت.
🔹
صفحۀ مجازی این برنامه نوشت: «امیدواریم…</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/467287" target="_blank">📅 15:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467286">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f99ad6ee08.mp4?token=eanXURcB7Xd8ZJnGY78plZ6NCjlsN_dHAVvontUQn5P63do87yrl-BlpfG-lbbDu6OlJnEa9xqpw-snK_3MnnJBiplsDWk39iBiv0gfaKwBLLr4uHWE3dRi2PBCyaCBsLEudIy3wEyZemQ4DA4FwHAkdrnE_3reWfm2w2VsAABSlU9ZTE2bnNAYUOekyatrfRbYG4pm6LpHO-iXnla_FV3VINx8y506snHVp-fXSqp9DupmeE9NdhBOLAbiv2xaZLCG8Lih18U-VWlTkQSk5GrMTAe1g4pGrQ7UX-XWeBDqRraBtvkO1TTAU4thayv1hJq-Ubx-CmBQ0zy5c3xxRkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f99ad6ee08.mp4?token=eanXURcB7Xd8ZJnGY78plZ6NCjlsN_dHAVvontUQn5P63do87yrl-BlpfG-lbbDu6OlJnEa9xqpw-snK_3MnnJBiplsDWk39iBiv0gfaKwBLLr4uHWE3dRi2PBCyaCBsLEudIy3wEyZemQ4DA4FwHAkdrnE_3reWfm2w2VsAABSlU9ZTE2bnNAYUOekyatrfRbYG4pm6LpHO-iXnla_FV3VINx8y506snHVp-fXSqp9DupmeE9NdhBOLAbiv2xaZLCG8Lih18U-VWlTkQSk5GrMTAe1g4pGrQ7UX-XWeBDqRraBtvkO1TTAU4thayv1hJq-Ubx-CmBQ0zy5c3xxRkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نظامی به فرزندان شهدای فراجا؛ قاب ماندگار یک جشن کودکانه
🔸
در مراسم روز ملی کودک و هم‌زمان با هفتهٔ نیروی انتظامی در باغ کتاب تهران، حاضران به احترام ۳ فرزند ۲ تن شهیدان احمد حرآبادی و جواد انصاری، از شهدای نیروی انتظامی در جنگ با آمریکا، احترام نظامی گذاشتند.
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/467286" target="_blank">📅 15:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467285">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3defd3519.mp4?token=tKVYQfOP-Gv1qflPyqLW__AbVzxHkkuFMCT2G8ocK1BU5NYXoVI8HaE0izJO323DW_05PdN04NDNt0t0qXlp67Pry20MYujXBQkbd7PwUw3_7M1ym0Xufk4Rfz9vYQTtXlRGB5HS7buRtcQLf7bjH3RoVBXvHGuLLAEMjoLc2cof4yhzhg_IT0mNP2UJD8wZp3KC5OjW3zj-DRkb4FilBOg8SZ_U8nNWtd-xuzmqt3B5eofoWsN-BZr1lPWDrkan1t38oZoTdNLSMUhLOsDRgUkKkWIQ6z2VQ1M14YE8xgBZO2AI0MzfQyvyaSNkbp4-Lbgs2UQwa5fsPUwsifoKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3defd3519.mp4?token=tKVYQfOP-Gv1qflPyqLW__AbVzxHkkuFMCT2G8ocK1BU5NYXoVI8HaE0izJO323DW_05PdN04NDNt0t0qXlp67Pry20MYujXBQkbd7PwUw3_7M1ym0Xufk4Rfz9vYQTtXlRGB5HS7buRtcQLf7bjH3RoVBXvHGuLLAEMjoLc2cof4yhzhg_IT0mNP2UJD8wZp3KC5OjW3zj-DRkb4FilBOg8SZ_U8nNWtd-xuzmqt3B5eofoWsN-BZr1lPWDrkan1t38oZoTdNLSMUhLOsDRgUkKkWIQ6z2VQ1M14YE8xgBZO2AI0MzfQyvyaSNkbp4-Lbgs2UQwa5fsPUwsifoKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان دوچرخه‌سواران ترکیه‌ای «مقاومت شهدای میناب» وارد ایران شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/467285" target="_blank">📅 15:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264f5e51d8.mp4?token=q4SC8_qYypoMP2J-7J_n18D0FW3F0hExP4Fk6yZcj1CiSmUdM7XhWo3TvWgfrZGkPVDvn3erLEb3XLLVrJLcoxSlgPTZGsfDql7poOQ2iQmUeVVjCvnlJbLPVPqhXtqzJYTsT6G6z0kfJQw8cwe7icag1gbi-OMYYPaiPMX1maitdvXNxKnPtd9cb7BTcitFcX4TeTacehfU3u0akHmp1yAX6H1ooiT5Fwjy5z2dFlsaJicXIJ9Xqxwo8A7RA1oAGcRbl4RcZ3E2tz562GPVFM1SBUuCFnQ2JxubXXVQGuXoNqAQ0KV-r1E3fzNuNHmXsgJRXRtnpDcdxVmgL8UScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264f5e51d8.mp4?token=q4SC8_qYypoMP2J-7J_n18D0FW3F0hExP4Fk6yZcj1CiSmUdM7XhWo3TvWgfrZGkPVDvn3erLEb3XLLVrJLcoxSlgPTZGsfDql7poOQ2iQmUeVVjCvnlJbLPVPqhXtqzJYTsT6G6z0kfJQw8cwe7icag1gbi-OMYYPaiPMX1maitdvXNxKnPtd9cb7BTcitFcX4TeTacehfU3u0akHmp1yAX6H1ooiT5Fwjy5z2dFlsaJicXIJ9Xqxwo8A7RA1oAGcRbl4RcZ3E2tz562GPVFM1SBUuCFnQ2JxubXXVQGuXoNqAQ0KV-r1E3fzNuNHmXsgJRXRtnpDcdxVmgL8UScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چراغ سبز دولت به ارزانی سیب زمینی
🔹
معاون توسعه بازرگانی وزارت جهاد اعلام کرد: صادرات سیب‌زمینی تا پایان سال ممنوع است.
🔹
قیمت سیب زمینی به کیلویی ۱۰۰ هزار تومان رسیده بود یعنی نسبت به قیمت یک‌ماه اخیر ۳ برابر شده بود، فاصلهٔ بین تولید مناطق گرم و سرد عاملی…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467284" target="_blank">📅 14:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467283">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1423c4aa4.mp4?token=fOxQRzISaWooG7UNjd8menUH6ZCricSxnaoWAF2lXsmDNL6mkL4RSVziDcbZLOsp2SwRymf83FdzJ_wMfd5rwbnWkYsT19jlmP9t0Z3TyDuctjrlRrwOnOniw-kMsh7oQy2vv1CDuHFS9EaKdysnEZNA8YCu1-yLoxpWnxuexpoX2Yfs5J4hqUfhuhpdCnGGmH7XACLIQZ0kxHV1V8G4HN5TW2VlmEDIM7mkebNxC1hfeINRWCuKJkAKOnQ2o0SSLuAVNv7FuWM1aWQgCxRrAuk1OaWeyxOdhWuDckCzwiVRgwjlSP8snBFohKXGsIIpJoKDv1_0Nhdd8hnljAR6hweCrjWO6ebAFYF0bw3U4RJt5wlhRjyrtfNybcpVcnKZGJP7-9FMNr5RYkEVcORO7e6vxieTnU6UUkshKlOblpcr0BCBm9eyWWdu9x0eJKuh_D-bZlb7TWvgCI1PgvPiSqtPde5apUpuqAtMJeeq2m0Z9FgjWi0T6DwQVUj9EcG7V0Nwlk1lGl1AynPNO5XaJzXaPl37fgK9lmAUSqb9UrhAVDD_vQWy4KG5Sin8tHjDrA1WTP73Uv-q_IqLz7w7tQ-jo5k7YDoeuMxWiUmwlm8mnk-hz9jlWfLbx-BoTPm2t0v64aCTgZGSqLEsMImuEVME9Gz98mlblnC6iWOKum0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1423c4aa4.mp4?token=fOxQRzISaWooG7UNjd8menUH6ZCricSxnaoWAF2lXsmDNL6mkL4RSVziDcbZLOsp2SwRymf83FdzJ_wMfd5rwbnWkYsT19jlmP9t0Z3TyDuctjrlRrwOnOniw-kMsh7oQy2vv1CDuHFS9EaKdysnEZNA8YCu1-yLoxpWnxuexpoX2Yfs5J4hqUfhuhpdCnGGmH7XACLIQZ0kxHV1V8G4HN5TW2VlmEDIM7mkebNxC1hfeINRWCuKJkAKOnQ2o0SSLuAVNv7FuWM1aWQgCxRrAuk1OaWeyxOdhWuDckCzwiVRgwjlSP8snBFohKXGsIIpJoKDv1_0Nhdd8hnljAR6hweCrjWO6ebAFYF0bw3U4RJt5wlhRjyrtfNybcpVcnKZGJP7-9FMNr5RYkEVcORO7e6vxieTnU6UUkshKlOblpcr0BCBm9eyWWdu9x0eJKuh_D-bZlb7TWvgCI1PgvPiSqtPde5apUpuqAtMJeeq2m0Z9FgjWi0T6DwQVUj9EcG7V0Nwlk1lGl1AynPNO5XaJzXaPl37fgK9lmAUSqb9UrhAVDD_vQWy4KG5Sin8tHjDrA1WTP73Uv-q_IqLz7w7tQ-jo5k7YDoeuMxWiUmwlm8mnk-hz9jlWfLbx-BoTPm2t0v64aCTgZGSqLEsMImuEVME9Gz98mlblnC6iWOKum0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا به خیال شکار آمد، اما خودش پرپر شد
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/467283" target="_blank">📅 14:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467282">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جنجال واگذاری اراضی چابهار به افغانستان؛ اصل ماجرا چیست؟
🔹
اظهارات اخیر محسن زنگنه، نمایندهٔ مجلس و رئیس کمیسیون ویژه اصل ۴۴، دربارهٔ واگذاری اراضی چابهار به افغانستان، با واژه‌ای همراه شد که موجی از نگرانی و انتقاد را در فضای عمومی ایران برانگیخت.
🔹
او در…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/467282" target="_blank">📅 14:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467281">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8b0e0034.mp4?token=ILrIQ-8IKGXPXWsjf0xQBWXXZ36Y0VvIwjgA_FiIwa9V0u5J4dViy1xN957FdnM5GV-bN-sh263wl--UiJcbuTa5nGPbnP6Z93vTnQ1ntuCqWd8ej9I-fv6r1ymaeoprNKzKH026nahxP2n_IY9yutohVeFXYAqdaR_RlH9V5Mp8UhlUSlePFvMEL2l7ZwN8jSO5tS2Ika7T8Qgizn7187TgZW5T10pj2blQH65cq0n4Ap2FoONsPXMArKHjZ-KhxSukAwSeIwxB3E9h0pqQjG2ZNYgwZodBHBfuzHE3tDwRwMy_3O32b_w4eYhvTaXZ3VbDN0Fm0kxUCAfvcYI3MIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8b0e0034.mp4?token=ILrIQ-8IKGXPXWsjf0xQBWXXZ36Y0VvIwjgA_FiIwa9V0u5J4dViy1xN957FdnM5GV-bN-sh263wl--UiJcbuTa5nGPbnP6Z93vTnQ1ntuCqWd8ej9I-fv6r1ymaeoprNKzKH026nahxP2n_IY9yutohVeFXYAqdaR_RlH9V5Mp8UhlUSlePFvMEL2l7ZwN8jSO5tS2Ika7T8Qgizn7187TgZW5T10pj2blQH65cq0n4Ap2FoONsPXMArKHjZ-KhxSukAwSeIwxB3E9h0pqQjG2ZNYgwZodBHBfuzHE3tDwRwMy_3O32b_w4eYhvTaXZ3VbDN0Fm0kxUCAfvcYI3MIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: گفتگو زمانی کاربرد دارد که در سایهٔ زور نباشد  @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/467281" target="_blank">📅 14:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467280">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
هشدار امنیتی آمریکا در اردن
🔹
سفارت آمریکا در امان، پایتخت اردن، از شهروندان آمریکایی حاضر در خاورمیانه خواست با توجه به «شرایط پیچیده امنیتی منطقه»، هوشیاری بیشتری به خرج دهند و آگاه باشند که احتمال لغو پروازها، بسته‌شدن حریم‌های هوایی و اختلال در سفرها…</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/467280" target="_blank">📅 14:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467274">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhql3kbOpeKuWkQ03tBgAwhuiDNR0zoUL7jWWua_BWdrbusZk2FYgzQKzrB6iC7RcILJ3elTbRw_v4C9ayB621VOlovUgXaXp8A4I793_GU0r60pmAbib3li9IgIK1n0PuCQFxabq6-KLanbYzN0n8ZTD-Y2_a3H7VZD5Mxe6qdmMlCIcqRn2L5ixB077-1UwfL8VxEatz-urNindE-KwNGGAVrv2laOU7gYXBcqgG6-OAuEbV3fLjUXO3FnzTa1hwsj0kA6e8yTUZ5RzvCAKgxUrTcMNNmkk9DgC6zPQvDebM-8tAAQ9F7DEWCO7MY3WGLeINp5fDSuJreUxBB9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdR-M3zQLMJO-b75o3Iouq23RlRuI_ckGYy89hLYEHeDttsExEydVhgMyNemwyWYEVpND3XixYsRehe3O5I1Zbl5ZqYN4A6dmqfm3jHgP2kflm8IYdwWw8uWvZs_bUmSkqUDcxBPfNF0GJvkCIZFisvwhT33vho1SNtJpZmCIV3obdoUceNtr-xxbbckVRA0PJz3Pn0EpAMQVaFdH6Ehi7CW5svX-ox4SdOcwgR2iGyit2kwFWZNYxGLoGPcxHlvFzxavwQl61YcAtqIywXpWACNBT0eLylXKYI6ksq2e2x2XxA7NGdrsODa3VILVIxMEiyYwqGz_I8F87TMbPkD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9FUtB5pNpduH2xqO8X5G_rzI0yYqn3ukbVtjWdfRmnICBJGJ_AoQTI3w--8zyk7c-3xkp4IpkEiR12HY_HydUbfg1A6eph7R8N8s_a6KBv7h12Y2Xp_3cxS5MgFYkg3ls7j5jrOHHDR4D_2OjbJ13z1U1a5IzXOJToALORfi2oT59LxarA2MmhgMgq1n-N7ZUBJrmRazinaG59tHL0gU63kIdMnnZ__CQDZ_tGQXqP0EQQ4Dy_qH3Rx9wqqSfzXt5zv-ZkTgvTmpdVQFwNCDerB_5dcS5CN6_8Qpvv4CYMWMxl5PTQgAwvABLuOGr8DtTNxaes9IA6j4BuyDk-KSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_NuXAETkLd31PrnEuLc15mQ3L0BB9v2vPkg55RsOvb8GPPSR4YmsdoeKOQmvNBZYiZzYV-nZbW4fcU7J5CoAF7MXJxguMG2Gj0fjsIeOW4siVU7hKCt38zwjie-0vsG4YoYP_k52-jNc0AGmWqzP9XVaEDVqlIZaxoQ6zEFbQJHXjm63B-pjKiCTu1jzpe-7-LuTTkZ9U2vKzNR2ip0vIzzmGvfVEYQh4JY3wIO5pXsM7yaGb0XVOAMfw2xfdy-9NV1pUbfr3tK6jSshUGWKUOav-UffaUXs8zfkzZsuTN-_F4uuhBtpF606VKbyH7FjXE_d1ZS6nLhzWfsZHHu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCrNtCdrmSAIO8PyVNl8ew88pQ-i9u-eNsQkuZLPWDvFTZw13X4fYA3vdX5Zl8CDdyvAKf07BHPT3ibGnj0EXCn2oNP5Y05GQIr2o3c19TYf2geJSjNYEFiuoGON-DnpgF5eegbXd2ENp-nS7Q1rp2Jkr8o5sDACBcW6GOYnntbvuarwPLEIcKJpRgSYUCnHHjXzJU4xubMv1yoGUoP4lTB31RMJBdtEWBerBAVa9YXUUH6nnRK3F2Go-54807CiZEKD-XR37ByAd8AvjdPnM-dBbW9bG2hTvYRBJtW9uALTekryRiuhOGpD9yh-Bhfs1DPcNeJi2pvWg49YEVlR5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: گفتگو زمانی کاربرد دارد که در سایهٔ زور نباشد  @Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/467274" target="_blank">📅 14:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467273">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b1af67f1.mp4?token=Pjgr1AM4MApx7av94BOLn4zjng3Ztlg-ncfwo_70WPfKpFc8MU_z1ndG3vjLT_CUvGmvRJx15LB5FGmFITU8pij9VqkdEwv-4r4BoG_kgkrphQBN84P84O6KAU9JdK53tVoKVMt_FMIDgO48icmINmPQ-2d6lsKbHkYel-FOVKr_CjykrAQ617blG8Cys9ArljXJvDDQzj5g_szYt-lRjie24EJfhWnj3VgpX79V8xUsLD-VI3AH0C1Ct4TXaX2XEL5BlDkn2Qk-K2zmcceG3u7haqQZ_0h97TKSkwZR4aZg9ISvTcczTiTo6VbdXGgiCUeQVC93SsFiApwaB9Z4Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b1af67f1.mp4?token=Pjgr1AM4MApx7av94BOLn4zjng3Ztlg-ncfwo_70WPfKpFc8MU_z1ndG3vjLT_CUvGmvRJx15LB5FGmFITU8pij9VqkdEwv-4r4BoG_kgkrphQBN84P84O6KAU9JdK53tVoKVMt_FMIDgO48icmINmPQ-2d6lsKbHkYel-FOVKr_CjykrAQ617blG8Cys9ArljXJvDDQzj5g_szYt-lRjie24EJfhWnj3VgpX79V8xUsLD-VI3AH0C1Ct4TXaX2XEL5BlDkn2Qk-K2zmcceG3u7haqQZ_0h97TKSkwZR4aZg9ISvTcczTiTo6VbdXGgiCUeQVC93SsFiApwaB9Z4Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: حضور ایران در نشست سران کشورهای مستقل مشترک‌المنافع فرصتی برای گشودن فصل جدید همکاری‌هاست  @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/467273" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467272">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dcfef82ee.mp4?token=ue0DfEfEy8dW1Py0_u3K2d_adCzsMjj8weNzVRSeMuu-989iRCu15GSnAc6UHaT_i0COBYAqZf7LK5R4_aq36DIUbwpM1fNT7iwqhA41OTEKEKNV-yyO6y9vxa2V7f2mwmh6xjh6fCbV3ZICQ4CKpFUhj_KOpIMSfrn2x_yFvCBhqbFZhx3cq6lev_uNmNp02mZcCkdiKtcVym0vlqqInBuiTXZivV0gswrlAXrhm5elqEzJqIYtu_OUFTHEHCwDL2Hrpaps1hjTGIGh8RZnQAYAf3JOMjdS-W-E9OVhhfgHciGE1WMgLgM_eD5vd_CE3vZwWA1DsY2FTOHkuoIUEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dcfef82ee.mp4?token=ue0DfEfEy8dW1Py0_u3K2d_adCzsMjj8weNzVRSeMuu-989iRCu15GSnAc6UHaT_i0COBYAqZf7LK5R4_aq36DIUbwpM1fNT7iwqhA41OTEKEKNV-yyO6y9vxa2V7f2mwmh6xjh6fCbV3ZICQ4CKpFUhj_KOpIMSfrn2x_yFvCBhqbFZhx3cq6lev_uNmNp02mZcCkdiKtcVym0vlqqInBuiTXZivV0gswrlAXrhm5elqEzJqIYtu_OUFTHEHCwDL2Hrpaps1hjTGIGh8RZnQAYAf3JOMjdS-W-E9OVhhfgHciGE1WMgLgM_eD5vd_CE3vZwWA1DsY2FTOHkuoIUEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار دبیرکل سازمان همکاری‌های شانگهای با پزشکیان  @Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/467272" target="_blank">📅 14:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467271">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZP7gSs9g5G7NHgzWA-hZR-bJrQNOFRuYrENHgDURIIIEFc7WM9hN9uuoAdJTx-LLPfJXJixSo9slKCmFKJXn9-RFMJwFSbD6WX1eDGFhhI6g_agvso19ng15HmNKIHLobPzUg4h2vng_nFOzdLYp3Si4vfJBhvg7mrPNDc85n73_9cZW2QXRgOX0ManDHcXYqns0k0qCryNybKmtnZQevmI3gRKtPe2CifJr2m9ElKZqqw5DYzjHh0mhTn_sQy-ZKnlvnS9BWfJ0-63EVsdhFnlcyincVDHBoeC5TmxSpc9Dz4_f9JbWVjUqLjQXrdczewcXx2PnsesGrR04pOdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای ناگفتهٔ اخراج پژوهشگران در اپن‌ای‌آی
🔹
انگجت: ۳ پژوهشگر حوزهٔ ایمنی هوش مصنوعی که به‌تازگی از اپن‌ای‌آی اخراج شده‌اند، در نامه‌ای سرگشاده به تصمیم این شرکت اعتراض کردند و هشدار دادند نحوهٔ برخورد با اخراج آن‌ها ممکن است دیگر کارکنان را از بیان نگرانی‌های ایمنی و همکاری با کارشناسان مستقل بترساند.
🔹
جاسمین وانگ، میکیتا بالِسنی و تومک کورباک در این نامه اعلام کردند که پیش‌تر می‌توانستند آزادانه دربارهٔ خطرات هوش مصنوعی بحث کنند و با سازمان‌های مستقل ایمنی همکاری داشته باشند.
🔹
به گفته آن‌ها، اخراج ناگهانی‌شان این نگرانی را ایجاد کرده که قواعد همکاری در اپن‌ای‌آی تغییر کرده و کارکنان دیگر نمی‌دانند چه رفتاری ممکن است به اخراج منجر شود.
🔹
این ۳ پژوهشگر همچنین اتهام نقض رویه‌های مربوط به اطلاعات محرمانه را رد کردند و گفتند ارتباطاتشان با کارشناسان بیرونی در چارچوب مسئولیت‌های کاری و با اطلاع مدیران ارشد انجام شده است.
🔹
آن‌ها همچنین هرگونه نقش داشتن در افشای اطلاعات مربوط به معماری مدل‌های جدید اپن‌ای‌آی را انکار کردند.
🔹
پژوهشگران در پایان نامه خواستار تقویت نظارت مستقل بر مدل‌های پیشرفته هوش مصنوعی، حفظ امکان ارزیابی رفتار این مدل‌ها و حمایت از گفت‌وگوی شفاف میان پژوهشگران داخلی و متخصصان بیرونی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/467271" target="_blank">📅 14:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467270">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df44a64bc6.mp4?token=nyp_rIw426TL1AT2CK-I-TEMzd_HrBtTSTOZUPrfcWl1kfL4aknPL3VWxK9ZzatlIZgnc5q5gxKEvW-2dG8cHqPYafw0rlUaU_moXjdKUJ5kGQ44W8HQnzfcRAcjXFOf2JiCGGhlzWWazMc5KWYMf-WPAHDP4w6gbPoOZr1lxrBRFRV8cT0An2Ey96-AC5lxcmgsZYy-kdNcyFM1C-DVcfGQK6-AMdIgpVpGrUX37stHhgCKShKt-OBp0GEDcC4z2-PEerhj4CzHAPB71BwV9G-VQOjAgmTPoo7CHTxEG0lOpo9lxNbbMOV-Kr9b9aZi9MC9IR2hm6Qp_TcTIFeXuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df44a64bc6.mp4?token=nyp_rIw426TL1AT2CK-I-TEMzd_HrBtTSTOZUPrfcWl1kfL4aknPL3VWxK9ZzatlIZgnc5q5gxKEvW-2dG8cHqPYafw0rlUaU_moXjdKUJ5kGQ44W8HQnzfcRAcjXFOf2JiCGGhlzWWazMc5KWYMf-WPAHDP4w6gbPoOZr1lxrBRFRV8cT0An2Ey96-AC5lxcmgsZYy-kdNcyFM1C-DVcfGQK6-AMdIgpVpGrUX37stHhgCKShKt-OBp0GEDcC4z2-PEerhj4CzHAPB71BwV9G-VQOjAgmTPoo7CHTxEG0lOpo9lxNbbMOV-Kr9b9aZi9MC9IR2hm6Qp_TcTIFeXuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
«رخصت»؛ صبح رو با یه یاعلی و رسم پهلوونی شروع کنیم!
🔹
برنامه صبحگاهی «رخصت» با محوریت ورزش زورخانه‌ای و فرهنگ پهلوانی از راه رسید؛ برنامه‌ای پرانرژی که قراره صبح‌هامون رو با ورزش، نشاط و آمادگی جسمانی آغاز کنیم.
🔹
«رخصت» فقط برای تماشا کردن نیست! شما هم به گود رخصت بیاین تا با هم ورزش کنیم و روزمون رو پرانرژی شروع کنیم.
🗓
از شنبه ۱۸ مهرماه
⏰
هر روز ساعت ۷ صبح
📺
از شبکه افق</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/467270" target="_blank">📅 14:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467269">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lo1v6okFfLZJahLSIyGXxlCF46woDHgfSGlMriCVAen4UfMZtPRP4JDg_aEotbxiIUX-J82qhjCrx7cfjjqh8fsHGQ_cqS5rRf6JHo8nPnjG2pVBoiVnjnC2vZRy3PWNG0OPYOuPTgNVqFGSkgPmtPq2K951YuDoZFK8qel2eK3FFH8CuJujC30gfOptsDWyw_HP-5iYFcq_02r_ybaLP20Qsfq8r_i236F_0G65hfgtIbwy8Sj4vJRwSGp7RXC7xl_shL1C95sXjfOsniDz5KjFPpl7U2HHOSvRWo2U4TB_YDJ4BatfuYNhpG5b-LBm6Tn3Aoh0PHxIrJ1iKhQaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی
#بیمه_البرز
از نخستین برات الکترونیک در صنعت بیمه
در گردهمایی مدیران و رؤسای شعب بیمه البرز، از نخستین برات الکترونیک صنعت بیمه به همت بیمه البرز و بانک تجارت رونمایی شد.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5111</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/467269" target="_blank">📅 14:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467268">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/467268" target="_blank">📅 13:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467267">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">لوفت‌هانزا و پاکستان پروازهای ریاض را لغو کردند
🔹
با انفجارهای روز گذشته در ریاض و توقف موقت فعالیت فرودگاه بین‌المللی این شهر، شرکت‌های هواپیمایی لوفت‌هانزا و پاکستان از تعلیق پروازهای خود به عربستان خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/467267" target="_blank">📅 13:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467266">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9e6jJsBtONQUcm3QfXhTazLXib8NvdoUzDyrC_az3NGl6cPMOUoUadxz0EFH24iRwv1Q13hKJ54bI4d0DIB4jQVe_lwI-bVPKSn_GGmnjR3-asp_eri9_47IA9MA5hTrC4F1Y2QMIuwK2Y-vArKmyrtPX5-jfSQiYCZmyJsrJkADBAwa7-eQnjkZtPyqUZZtuVbb5HwOabYppJhmbb7tUJ1_vUxOR_OTP6N8ZjG0Wg_dJ-LQ9kiNytwPu8qAM0s6MPKW-fdkPFyDdmU92Kv_SrOtyLY97YanaKR-zMLEuXpVEAF-7w9Ibqok5EbW8ysAQdUFmB_I9mGhtiGJjX6Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاج علی‌اکبری: صیانت از خانواده به یک نهضت ملی فراگیر نیاز دارد
🔹
خطیب جمعهٔ تهران: امروز جامعه ما برای حفاظت از خانواده و تقویت بنیان آن به یک نهضت ملی فراگیر نیاز دارد و مراقبت از سلامت روابط زن و مرد در جامعه باید به‌عنوان یکی از راهبردهای اصلی در این مسیر…</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/467266" target="_blank">📅 13:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467261">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfpUFtoBoRruZE5dkb3XTh7Hx3uLGZJIzN4qDmTpN5QfDfm1DfJ4Sy_RN0ZmUhF0_zyUbHa_SIIxjfOngyj9PNhhRyPX51Awjya0iuD0fr85_2AVZ63YZxCI5Gklg_ADyb4m9mTXrI_ygqKfz6CpNvWeEu1WPrwEUtsJhZCF0RaIVxF0KIAuc9miRqUK5JOpdV3qLKpgKnm6mVAiFFGyVVHbewVQr_Kv99Oiq571v6N3HXFqDKIYdbkVsLl7zXkAjgPXhtU9l8Ko4p6TsSxSgKIbgIc9X4lYC-QjeUTZq5Z-kisEgW2o6QbyrbpoDM-Vr9ENCILNtoAHjlYbXCU90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7IGNNESyVatHRNetYFgjKaRHLUH_JdYoeMiCxmKxSe8s2W5_tLWL9Nbrnn6y9vSoIQMWfN_EuTyJ_UBqHD5YYVxM7BVC3on_sYSQvpnvgZyv3FE0arSjjtkmCZWxl1ad2ekpS7XQ12yTcByH2t3QFFMd1zCnt5kgS-BMUBuPHUK3YRL2XreF7jn4lNWzZGFvBgfUu-CB9syXS_e9a_h46OjSx27A7p4GSsZjRREIedo0sU0Nm7TZxY1WFUFDpOB70cp7W648PMHl2XsZleqp_kFWl13AjZQ4RqyVnLrGvGRmMv0geb0Bi_y0K8_tx0cp_215ootAnAhErJUeGey6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suAlWXjbZVm5Q3zsa07GJgRtWT40_jBAAs5R_IpdRXq_XfcA6DJVqGh1fWXutpR8jUMrirFTysezAf5eH4_qiWc4FOov6-QzGgV5uhPL5HbAtCgA2LSwjseU01JlMAhA3xh7FF7ucZQ5Ak1Gj-NnB43xbG-YoFFG_JgNvURz70s4Yo719fPyMHFkM5L_PIoD33D7VfQ5cTkg1aAMZpj1kv7y0wbgGdVcdEIGENqwlwEgplJQysvd2icz0BG9D2_zp_p86tMsA14RFQ5HCUFMhx5UK5XFNKaRFCUfIL8y67zxl7_7uNQxn_Z2kkSI3eFE6mASGSJWC6CqXi6LPSxsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJ43sF2SEsMoJ5qp7l1dwkTg8zd1OMWykln3YYATUKlz9TCcmNDSTAvdCDhAmm9WGzLNvxO9GboNmSwBNlfSRimUkZUqPs1YXxJj1jYFCdOjwbcNTJEY_8LNjbUROJ77lKn49lcVggCFqieIVkevtetcyxcgetwsKSamBMchfQHHldP6_yHZ56Zsr2iJw0F_31mroxURzxUF8KZQFim7y7YEht24W1zp67kKOfhw99MdvacPZQMH_5SDiHrnazAC0vuH05Mp5eRNFNq-4aGMMnbe3UXP7nnqlnGR3GjDRUBpqykX8MltbXKFth16Srv6qcS3sZdogWRUpaurcdRmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEdWuD8_iixz38m3Kxc9lo0ggbB_qBNky595v6HkasaAXHQXufwLpKB7-CH5FYmDle0NO2Tx8ffncXz33ATzGpeBMT9L7ZiPfCeT-CUSNV0pQNPaw6UlaNXKrwnNuGblUoYSrLvNZ4IIiwaKk6XoVcQGwTX0rD8oJPZ6p6w4dsbE0CcOPoRS3MlA4wjABxlFrXNDxHkbiWSpaMxmY0OJ6OSM4RPttpVNuNPdE4VN8Y_nRXE04tBZangx75RlA12z771qhjnKAhnYNfEQFovqKg1fpjnsc8pkJW04skAMGNdYvXxL6w9TbyM_Dof8r11uWyeY4Ti6KKWvyZqH27mfjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از اجلاس سران کشورهای مشترک‌المنافع
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/467261" target="_blank">📅 13:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467260">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صدای انفجار در مسجدسلیمانِ خوزستان تا ساعاتی دیگر
🔹
فرمانداری مسجدسلیمان:  تا ساعاتی دیگر صدای انفجار در سطح شهرستان مسجدسلیمان شنیده خواهد شد که این صدا ناشی از عملیات انفجار و امحای مهمات عمل‌نکرده باقی‌مانده از جنگ اخیر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/467260" target="_blank">📅 13:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467259">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAQWturE-GpRf0Qu0phmIUQGGrF8gKokqbhTdV1iHcu9AcTXXwd9815Dr4bO-8OnIk67s3PyBtM7i_lJ_sRpI1-XqLfOsBfnbVb-AH1s9sqmShEY2guwPHB1ndp86gzErAQVm7xY9K0AS9S5fn-g29ezDhnWd6_q5-uNfxH2dUs2NikusSCfKLzDH5HxBjDgTujUlrdFYFSCgEwBO7sCHbFvhFCrPqJTZnjniMxVkEqK1QLhkwpHkR8g6kN51V6pkJmrw86MvuBtE-ECdSj--z6-lPiXtxd1tuUx443NlCWo6CKjN5gMUHxAIstYoa8EWOqYwIF2OEXd1djAtccQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار امنیتی آمریکا در اردن
🔹
سفارت آمریکا در امان، پایتخت اردن، از شهروندان آمریکایی حاضر در خاورمیانه خواست با توجه به «شرایط پیچیده امنیتی منطقه»، هوشیاری بیشتری به خرج دهند و آگاه باشند که احتمال لغو پروازها، بسته‌شدن حریم‌های هوایی و اختلال در سفرها وجود دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/467259" target="_blank">📅 13:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467255">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtTaIm8HixdJ56TcCvE7KzPoG_yWzzR8Sh30oG9EsLi0UJIiPzvj6CYqkkacRj8MfYWbKfS7oqeBCDbQUCfzzIkfeiLAGhCJvydHlm9LPQUnJmB3WO6-ccc35aiBj97GDt6niy2fd1syZdmdAL5PTF3e17pVOYlGBp5JqwSifkzKSmldslZukr8rdmfeh5vmSiailKwH22B7QpVsMIe8tAMOSicSPEpk7yXMKq-aV_1w_ScXkJhkuc3PGRx1sJGfxZ2ZgIl_kedWW_q_unr_2atVOyRYMzgfHx0uxyAcjAugyqm11Lc3ZZy6JRKL3ZU8Xl0PkBxRMcW52GL4EyMy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBNaDRdpXRN2xz4Y3Wva4-WU_8Mt4ZbHpoL3tdNHMbw-sTEnLA6WEBn1t6OYsZwDvf7FMKrN_j97Am00maq37Ox0SQ0qv2zJqRrmlotnDmi3-dUv0ha5vs-rMQ8jUMsYJO3-9rg7XJon3AApZUqQAdH8iAe6gxb2_BxXY4vLmw8iNQTaa_Q6loTLXdVXGBTHWQsHyHzW_aR39cPLAR_62hszaK3J77ZEjdzc4GkajMkdkiaYMF_Nua8ryZ9z2CMBWWWjj-Cs4WxqhQhDSgZOavfd27dKQ1k3yNKfeDhyW6sg6jCR4eDlT-odBUlDhY65U407udbzigXVgcFIog3vlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONkD15xq67Z6B1fMEa9QRSglgFzfy_fmqFhj658X8Gip4cOdcZUivI_zJ7hKCeGUuYjhQWLGwnsTfkMZz-tkWPFZvlmNOxKuIX1MKlby0a2JXWSMntlA3QW3BLWx1z2qqhtiK1cErGs9TORjFJBU3GkwcgAR5Rl3LaA98keswmanLHkC5e_5uoJvWwuDEL0i1BUla3rOuVx7OHNtykCDxnpHynvK3TKnvLf9psHjUs4UOE5mIFqNScjr6qmMWQ9GQjwXl-MUHI-SBD0XtceEjU0ThUkl-905z1N1t_swQ2VYW3_ppJr4NzSSB9N-8_ERaZzRDmKv0bKuIjds_NT5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJVrSyv78absXTxNNFdBZCvMYsYqd0qJJgbhmB9iTzGS6krkC9T7GejwUj5IQ3f8PPooG9B6NjyN6m02mfKsoP8TVLx_DpIyiN7PmJ7Km_kAvGDGzDTmtNNuhDJUT0v1R3pjyT56QcFbTIPrTdh54cg5gufmoTXz4CXdv0TfJdbhwfKDix3EBxMMHESF5hJIoeP05sBbhZzCrBwKYnHIFk9Bcf-YxHeqKfr090OoDoRykJGekg4jaQEb0ZqYdpY9GKI-6LYvH-zv9bX8hltfUMzBhLQ1MZF6h44WTT0Bm6cMuVdcJBaEGjqFUmuuBM9vv5KTbPfeSQfU5bYuEWoC3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: امروز بیش از هر زمان دیگری نیازمند چندجانبه‌گرایی واقعی در منطقه هستیم
🔹
رئیس‌جمهور: منطقهٔ ما می‌تواند به‌جای رقابت برای حذف یکدیگر از بازار انرژی، به شبکه‌ای از تولید، انتقال و تبادل انرژی تبدیل شود؛ شبکه‌ای که نفت، گاز، برق و انرژی‌های تجدیدپذیر…</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/467255" target="_blank">📅 12:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467254">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl53NEe7XW04UojlH1GYkGaPfsbvwaDFj-SB1NEWDKLmSEJlpAbcgkaSv5y7EPJA77siPntMX5eR6OQYyqksGaRYuZMOou1vSEzudfTXbsxKROd9UOhyhxUQK_L7HGr64dRdiMsQPwSWlyvDnY2n2XJL2TYCHUZ_XyoXh-f40Gen9nOm0H-ShZRJSQBu5tg1LxvR-w6zR7yydQJAITdTDKUM06KGxeiaUyJCgWcGa5P31BuqwakhjGUxG0AjVLNfhABzqPIxgrc6y40NrGw0O5pfUq-160HpZyLpFSB48jaj04LXw7Pf0WKLqMpap5aEVuAlVxAOITW3o-H3dP86Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاج علی‌اکبری: صیانت از خانواده به یک نهضت ملی فراگیر نیاز دارد
🔹
خطیب جمعهٔ تهران: امروز جامعه ما برای حفاظت از خانواده و تقویت بنیان آن به یک نهضت ملی فراگیر نیاز دارد و مراقبت از سلامت روابط زن و مرد در جامعه باید به‌عنوان یکی از راهبردهای اصلی در این مسیر مورد توجه قرار گیرد.
🔹
چراغ خانواده در غرب رو به خاموشی گذاشته و این روند، هشداری جدی برای سیاستمداران، نخبگان و خانواده‌هاست؛ هشداری که جوامع دیگر نیز باید از آن درس بگیرند.
🔹
ملت ایران به برکت انقلاب اسلامی، پرچم ارزش‌های اخلاقی و خانوادگی را در سطح جهان برافراشته و زمینه توجه بسیاری از ملت‌ها به این ارزش‌ها را فراهم کرده است. ازاین‌رو، چشم امید بسیاری از مردم جهان به ایران است تا در پاسداری از این ارزش‌ها پیشگام باشد.
🔹
امروز به یک نهضت ملی فراگیر برای صیانت از خانواده نیاز داریم؛ نهضتی که حفاظت از بنیان خانواده، تقویت روابط سالم اجتماعی و فراهم‌کردن زمینه رشد و تعالی خانواده را در اولویت قرار دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/467254" target="_blank">📅 12:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467253">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK9gEnUcO64dbm_rMeGb7zM8CMrxkQ2rhxIRQJnfyOhDfyXFrvD3cnyjNd7s91R-S1jceQETNyKH13VxxNHdA1eYpcZorGhiOrJfZsOZ-wLIaaGuvlRYfFVGKGQ8B1pWYnDF4p77Cixi29r7vZXRIyMll2-FC5sEa3emP57Q1jWKZQ1o1QZpfy8d2Vd00zTC3nGl3JFUppL9rDVQobzCD6mQa_CqL6nPB1w1mcRNF0vMP8HwtyqMGHOcVYYCr63apnTq8GXiU0GqjjXxRzzzAlVtNhXHKSEH_KeeSqYo7MzoyNSW9QD-sS3mP8vEKc6br82Zh8k5gFDBKc5p7spHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور رئیس‌جمهور به عنوان «مهمان ویژه» در مراسم عکس یادگاری نشست سران کشورهای مشترک‌المنافع  @Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/467253" target="_blank">📅 12:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467252">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psgvJSnV76BJXpY7gT2I6K8YYJVFNf1VtYf8nNOnByZd-FXywF08WvbNlfd5o3s5nRs9sbQvqwuRBlbxGilk_XLms4FH9WIYttbxNZ2aPvklNPg3y_mwBRi1FfMgdd0AnwiDnfsKbhZiAGEkMMjvtF4_EvqW3U7q0tI2cqPF63wkPchPs1BRWA5FCY0XhOeqIy9ckcZfkvs_6cQHyOS4O2JBhQGPevUDSEBYqZIu5U428NUZ-cbppXwk8zNUo5OT7hTuJv84kPfvbBZL5EnMWlKTiEZpUwPeVUgv-1BxPgnm9IizslW_0a_-d7ytjBCpru83Rg5xcoYRW4T2fghUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنجال واگذاری اراضی چابهار به افغانستان؛ اصل ماجرا چیست؟
🔹
اظهارات اخیر محسن زنگنه، نمایندهٔ مجلس و رئیس کمیسیون ویژه اصل ۴۴، دربارهٔ واگذاری اراضی چابهار به افغانستان، با واژه‌ای همراه شد که موجی از نگرانی و انتقاد را در فضای عمومی ایران برانگیخت.
🔹
او در گفت‌وگو با شبکهٔ سحر افغانستان اعلام کرد که «افغانستان بتواند در بندر چابهار در منطقه آزاد، یک سرزمین متعلق به خودش داشته باشد».
🔹
زنگنه خود نیز بعدها به تحریف اظهاراتش واکنش نشان داد و تأکید کرد: «موضوع، اختصاص زمین برای سرمایه‌گذاری افغانستان در بندر چابهار است و به هیچ عنوان به معنای واگذاری خاک یا حاکمیت جمهوری اسلامی ایران نیست».
🔹
در شرایطی که منطقهٔ شرق کشور با تهدیدات تروریستی مستمر روبه‌روست و هرگونه تنش رسانه‌ای می‌تواند به سوءاستفاده سرویس‌های امنیتی رقیب منجر شود، انتخاب واژگان نادرست از سوی یک نمایندهٔ مجلس آن هم در گفت‌وگو با رسانه افغانستانی می‌تواند سریعا به یک اقدامی ضد توسعه بدل شود.
🔹
آنچه در چابهار در حال وقوع است، اجارهٔ بلندمدت زمین برای سرمایه‌گذاری است؛ الگویی که در ده‌ها بندر جهان، از اروپا تا آسیا و از آمریکا تا آفریقا، امری روزمره و پذیرفته‌شده است.
🖼
اما آنچه در چابهار با افغانستان می‌گذرد، دقیقاً چیست؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/467252" target="_blank">📅 12:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467251">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8TS0V4ylpH6NaSomDttCINsm38wqJzIDI04wCrJ8BEdCYfBfTIlCLtlTZuQ6bkeTPEvEKyPsW-6mxhX9sUe-9k55eRL9g9tmV4MQkOq_7v4lwsb3xRrsiYZ-5GMcY3pgQOU5KjCw5un1vVS_Y6ciQ5xS9EhCT9GlyGCYsjlT1-mKCS2CvYZ5nNgQbwV1nhHaVaM_AjbTF14LjMP9us3VkmteRHUG5E1d8Nb6IVdl-IUz8fDTPBz1kUTXRr2jsEFnLlFtLj6axgcXEpwICK26Mt3p6fwshwKydYCf_tx0zUdRWG6QxDhG19a29tQxpyapeVZ7AsonwGUiiHGXyOdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بیرانوند در پاسخ به مدیرعامل تراکتور: اعتبار حرفه‌ای من برایم ارزشمند است؛ دفاع از آن را از مسیر قانون دنبال خواهم کرد
🔸
مدیرعامل تراکتور علاوه‌بر انتقاد از بیرانوند برای «خسته‌نباشید به استقلالی‌ها»، گفته بود او در بازی مقابل استقلال عملکرد خوبی نداشته…</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/467251" target="_blank">📅 12:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467250">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یحیی سریع: به فرودگاه‌های عربستان حمله کردیم
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد شامگاه امروز پنجشنبه فرودگاه ملک خالد در ریاض با دو موشک کروز و فرودگاه نجران و پایگاه هوایی خمیس مشیط هم با موشک‌های بالستیک مورد اصابت دقیق و مستقیم قرار گرفت.…</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/467250" target="_blank">📅 12:15 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
