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
<img src="https://cdn4.telesco.pe/file/TXjFBB28p284z6vBwR0Ilz-KNyFcpfDSaPszQK124QlyEALApjLF0iWpR_KiTr7Tpnar2JZUAytd4Kih4fd_r-Ynj-0J3lJRhsv0m3HaulvP0td7qZEGtJblarRR7NzP--QhtckYI6aC3fwAPShB-k4xGrAk6WjG0qCCMXWJtcX17EBkLJSYnwntqx_1sVcn4lv1QkBEtMaGAv3d0q3gJ4J4sXqm36bNlQQzi1JH78zOXcTAZ5yuM2CDHAlEM3HZ9kSry2z2-FGC20q8QPwN2aDe9-GIKAW5q6Bbj7ZcZ-ze_2W4SAurtQq2bqcFTCYyP8Us5TskzNiUCfsH2OKSHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 00:41:31</div>
<hr>

<div class="tg-post" id="msg-463535">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61f9e2678.mp4?token=RHRTuINeEKXPj-wVjLdSPJX03OurIGRLI8bfZ3w-JPHD0uS6Nn9tHEeQKHED0vP7ikWcml8ntq0l-7A6Ph_xg7mWgiArzjg0auuuf3AXhlZzXc_r-gMYfEwhW2IFDMCXuIxAubR6DLp9j21FjeabtCdwHCe80JHGFCr8Jgko4qkq8wPB6BnzZJNmQNnGQf270XgkjHgdRbd6ouUNitylsSR7PA_Bqj6podwJb31pBFdQsp2ZjtBKk1nJTTucEzVQqacQf3CQU3O_VJ4tb3tJ80TEqa7HjvXYvUqmpztUTXQ6X8ShCqc3--PMptbhLN_vPV5AMHOfNfL8Q4O8GvvBxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61f9e2678.mp4?token=RHRTuINeEKXPj-wVjLdSPJX03OurIGRLI8bfZ3w-JPHD0uS6Nn9tHEeQKHED0vP7ikWcml8ntq0l-7A6Ph_xg7mWgiArzjg0auuuf3AXhlZzXc_r-gMYfEwhW2IFDMCXuIxAubR6DLp9j21FjeabtCdwHCe80JHGFCr8Jgko4qkq8wPB6BnzZJNmQNnGQf270XgkjHgdRbd6ouUNitylsSR7PA_Bqj6podwJb31pBFdQsp2ZjtBKk1nJTTucEzVQqacQf3CQU3O_VJ4tb3tJ80TEqa7HjvXYvUqmpztUTXQ6X8ShCqc3--PMptbhLN_vPV5AMHOfNfL8Q4O8GvvBxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حضور رهبر شهید انقلاب در حرم مطهر کریمۀ اهل بیت(س)
@Farsna</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/farsna/463535" target="_blank">📅 00:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463534">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKgvNjWBd6A9e3c8eL-UfGO_6SeZbj8iNUB4KyqtBYLRqEQizmDz3JpNoXfE3sys9dq2x8r8Z7nXBnsV4IhAUdA5ZtqqWObbLCbtxI8n9a_uSJoBCXAlGUbnPMVtuuJghgWtI0LAs3XGty6A9vMlIAWv1Z3HmNo41OYx7HHchsuGFCNEZiYEwtNOiQGJheIx07BfKfUTyzXZmYIORjwnqrFdE_1ZqFBSzZ27Eq47PZ3BtcW21nLBg7wH76UlKniyScRZh5dEzykNDoJkf8akEYjuYsek-ZAzpAoa2rraklmzV251bPhWwqBpeDfw-EHp2Qj7oMwyELrl-T0rUo11VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ مخزن ذخیرۀ نفت در قلب ریاض که منفجر شد
🔹
بر اساس تصاویر ماهواره‌ای تازه منتشر شده، پیامدهای حملات اخیر یمنی‌ها به ریاض، پایتخت عربستان سعودی دیده می‌شود.
🔹
گزارش‌ها نشان می‌دهد دست‌کم ۷ مخزن ذخیرۀ نفت در تأسیسات ذخیره‌سازی و توزیع نفت در نزدیکی فرودگاه ملک خالد آسیب دیده‌اند.
🔹
فعلا مقامات سعودی در این‌باره سکوت کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/463534" target="_blank">📅 00:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراقچی برای شرکت در اجلاس سازمان ملل عازم نیویورک شد
🔹
وزیر خارجه در مسیر سفر به نیویورک توقف کوتاهی در دوحه دارد و دربارۀ آخرین تحولات منطقه رایزنی می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/463533" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdcKANPMJljTuFksxtpVpZgTurUjl34SVn4k04hAnSZWUpW8FtO5aeAjV7vr_S3IpLFGUr72v-wflb8-SNXUZ4YMG8YAZewUu3AUe2jjZyOgb_t18MOcKrK4z2DMDezNpAzOCiJb3R8MARFt9-zOEBLhU7ERLg1TjNNRwUku8cw308Aow1AjsbvgK2XcfbtmCt30UN504YqxKYabKL1RNSB-38IWrclitEdWLl7KWKlKkXuRbX-EY42Aw5HCVb1VWrSCO4XXADJi5l-rayalK9HF-I0DmqVIalR0WYhZFEr1_hbig4waABMYsyZJ0lR8_Z7mgndkhKgPcyJWtfUMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورنومنت چهارجانبۀ تیم ملی در عراق
⚽️
تیم ملی فوتبال از ۱۶ تا ۲۶ آبان در تورنومنتی چهارجانبه به میزبانی عراق شرکت خواهد کرد.
⚽️
ایران، عراق، لبنان و فیلیپین در این تورنومنت حضور دارند و تیم ملی ابتدا به مصاف لبنان و سپس به مصاف برندۀ دیدار عراق-فیلیپین خواهد رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/463532" target="_blank">📅 00:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOQfuF7W28SAKwk-mdsTYgbmU4_strNK_jllSDZsW-Y4WJH2jSF3LkTYHxNOtMGVXDNPBe5aXY0QMyy9ocLEngx_CmkwtCVNLKZoA1VjFTqElkSCKbc513r9aMnK7jWWaMer37g7HZYuLRCFWSLrvw58BUnmwv-yMUv3fB4R8lwaJS5UZKceKGdZ7CxwNIw9HwM9oDS29xIeRAOat-G1ZsKYJZje058xNL1yS8r1K2Gy2SvT5dJBgAvE_lphsfZ6jvpQF2i4CJ5l5RRs1hpp6AthrwBN9y56pgyGeL-ylqAI04P5LGvZfqE_sE5jqu_OLMCHygiCDrDjtk6wwRSHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سقوط مرگبار بالگرد خبری آمریکا هنگام پوشش تصادف
🔹
در پی سقوط یک بالگرد خبری شبکه «ان‌بی‌سی لس‌آنجلس» هنگام پوشش صحنه یک تصادف مرگبار میان یک خودروی شاسی‌بلند و اتوبوس، ۳ نفر جان خود را از دست دادند و یک نفر دیگر زخمی شد.
🔹
علت سقوط این بالگرد هنوز مشخص نشده…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/463531" target="_blank">📅 23:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463525">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4m9BqPuHVx53WWS1mgvjjhxC0UZ0uv6_Qc7RP0Zqo1T_Sr9LjiH8thb6DBtOOlwYPNjqImkTk6La4q2jWoYi6fGPQvOITwa7fDWkCBVbh3HkGODbQeOune5jUZScT9CwhB-xuXeSri-I9Fr08ljOe0ZwBH7l0hnxr4Nc3Jf8UhhcZSL1VBxt2OVu36f8SU8v7uEw8_mFb6Jq09ZhYVvQS0CR8WqRsCePk-XGUjfUVngzaP286VHmpzG77V4_RKQgLi8lTeuO95cK6UdjFWyj5D7O9y_szAdmwY7LAL-1dfCOa7jKxtlsXugy2SHHYrhlXW76CApdGQog7sBG4iibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHHxH_0tosIxKUcez3LjiGs9gOF-tCheWzdeLRKf-HWGVtbkmg952xPcJPhUGCmgIvasQoykOU1l42AwXW_KgcTxQCDwrHlrrci4XSOhsV6BTi1jHl2OWbqNcqsB7BGbSdmw2a1CUPZJne6jXFj3dcMw6AGPoWeFMRMIsOC4qC-OYQQe5zTL62VIs5OYf5d3etE_sSOaxKg60RBQsS5m3jA1JBJ6kgIVOV0svc834ffFUf2KbjCHTXe-A5ipADBI9N6ls33Zoz6-kqcx78BbT-leykith6XM3653YVuHaywI6bOmbfLAoJuZcWqGyIxPG_4zejy3gD5hQ5fWE_i0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-Pv7xcVt74qmoT-5a05-CLfzVwbulbnVoV5Ym5C2I-pqgR_xVkO11K_gl1o3YqAkMYg3sMjAuIzKIXgz8h1_eIvlTgDGm06zJPp4Zs9LDIkBoh3p7QHmRGcMAoNH-0WpMc-e_9r7U13feJZ_PGqDlCN-yLYEScWee2BNIKydvqCFJZBsWJ5pQiT8NZwDZ-6wwHmEDkKE9Okl5O_Mtb5ZXHbWG6UItl-HXsMbYSkS79_FUKfGUrEGOXPRxsQn_fe43-fDt_mf3WvIdeYEbdCHbhoc86Q6HTs9PX7lMasWKf8-MwC-cIUt0vZf8pepHuzCpAN2zP-_YuelNA4KETZuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOAGZhUU0fVag0O00fvJFI1z_e2gPTLfPQJoHgrAJJmYX11d-F9-0JdmjQ_Wf9i7JWo7e2svDq1MTRA9lE3I2dgpMBNFdjbeEeucxY6xIG9mLXyw2kL1VTtrN_WEhEg3MDNYXlkr465XtmfG5EA-0GJaO0oHoPXVwArsyhte55-YrgcJ5o8RFb4XQWqfit7jk3TYXj0tIAl5Kbnvy0Xua_wOePEjxzmRfnS-kBXA_gxIerSd1ICB4OgrYA0mYjPSHQqQEtstKkdTnqBDfamKAhL3sUf9VEMNK3J-gudJoNUsNadz_FV8Kto42ofFQniXpiqG7Nd5Hr8KFsIH7jqNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0eETXtEL0hFEeI1sDWWt7uw2FJPMlx237rKxpt3Q3-53Z-dBrLJqDq8OH6yWw9kvY6rN-RJDg32ALFOn1_ti1aIoMyrZJDVe7J0k8KkOsdKc7f_XiyzhRv63PDDUL9DGh_AB4EboLl9BjlNCcduNKav0L8lIXLBZspHwC1DIrzUilOvfaNxbISBeKs9UKOvD9m01XXR1D9isgblcWVyiFag2vASyv47s43JOld9bIJZyGS0bkLiFLn6qOo_VnPi_c6Om9YIeWsWpu1H-ngxf6X7TYHwP7BPG0AemiaCOYzb2DHdA5FDmah6GycULqbYrYGdvXYUKw2zf0pv5oLtLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WfUV4u4tcxyjvSOfxmoU3k4HptgDuf6H29FEnGkqRvTIgB_A8gM8yDNwN3nX6rnfv3vtGQP7HLsvxOfkobZZw85FxRDu_joO5i3QNLWNdCv6gjh3Ok3anHAeikH2c9I_u9PxcbV9f0RblV6z0YsleBEEyfVxNAwAQXAcLrsq1DDisVWY6b6GAsKIXJT298H_x4hc5JtUn9JkSzGd1NbHZ6R5-dpn-X_dMu0SP53x2ML6gz__2mwDPRnj1TsQN9Wemww-nqtqX_8GZ4q_qnRYaXh1K7B9gNKAUGLzm4zdcKGwLDLR5TRmwWM0XMlzDbR8DokcJysEYmJj9bEM7Fyezg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تمرین شبانۀ تیم ملی در تهران
@Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/463525" target="_blank">📅 23:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463524">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEvhMIfG7jhYXKf3vOtk4-pZe_hjdqXz7PPUH6PmKEadtP7uy1FqdycF9DPiOm7iZ_lTiW-Khf6OmcCaa254I2Y16RNYUZ5IhdmfvEYRxYwTSOi2w-a3V0Za_UW5ViGxCVgxBgqXNDoxYZbTj0gY7Dg1j4ez_sjli73PQtku28eUo7kJzf3ir4TKPWJzBOiU6TQSaOwp1hfm8VMN5tgfskwU6W7y44jRP2d176si19Ih6PdLnoK12d8D9SEAoDSkAqZbGk1g8b6SrxZnmiTWXBq_NkVj2RjBf5JxUBRD2xndsaxzpciej1EdKc_c5Hg4KyJp-SfUEWn8xK1HIJzcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب‌رئیس کمیسیون اصل نود: هر اقدامی خارج از رهنمودهای رهبری، از مسیر وحدت خارج است
🔹
حاجی‌دلیگانی: معیار تشخیص حرکت در مسیر وحدت یا تفرقه، توجه به پیام‌های رهبر انقلاب و میراث امام خمینی(ره)  است.
🔹
اگر فردی مطالبی را مطرح کند که در نقطه مقابل این معیارها باشد، طبیعتاً مقابل خط اتحاد حرکت کرده است.
🔹
نظارت مجلس، سؤال از رئیس‌جمهور و سؤال از وزرا، همگی در چارچوبی است که قانون اساس تعیین تکلیف کرده؛ پس هرکس بر این اساس عمل کند، به وحدت کمک کرده و از اختلاف جلوگیری کرده است.
🔹
در قانون، برای اظهاراتی ازسوی مسئولین که برخلاف شئونات باشد جرم‌انگاری صورت گرفته و برای آن مجازات نیز در نظر گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/463524" target="_blank">📅 23:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463523">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWuSbQlw3nyj4-6lG2vLeOtFYLNw57iUFmS261-MCxu_xjxdMPFXYt99NZgrsbu3-07ugFtcD7m6tyKtl_jNUcgrysP0pWXjCAoqk4T9Kt7uARUH5zIGoy9aHj7CUylguXAGj6nRrIJHgoxkQwiLf8SJJgi3gU-srLaNudKiFSVnZL0Dec43ZaDTk18SYWHvigakjXYF56D0EN43u1ejLGuMoh_AB171xqFkvbntH65oTPSGv3zTjTVsaCjE9LFLf1rtS385l4-WTJg7Gcqw_kUB6D3gip5MsKw1tuVN3mGQcun3cZ9afItBvV6_RqtWBjXO5H7JOQnasmW522qnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب پوتین در انتخابات روسیه رکوردشکنی کرد
🔹
حزب «روسیه متحد» که از پوتین، رئیس‌جمهور روسیه پشتیبانی می‌کند با کسب ۳۵۵ کرسی از مجموع ۴۵۰ کرسی دومای روسیه، اکثریت قاطع این پارلمان را به‌دست آورد و رکورد جدیدی ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/463523" target="_blank">📅 23:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463522">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5521d6342b.mp4?token=Kdu2PO95u9yge6pdYYJAbwTJ_XIlxm_6rKKgsjb_iyg2rBIDZsbTeTmw5Vk67Gq7i6MLlg2FnSa7dhWFEPcpUxpw7dB9LVA7UywOgiuW1Vepnoiig9oijvH100CypjuJoIzPPRgq_7yxhpBtMKVQ33Us0fzh9OX0goprdoGXsUsPotADCzP-h-fV2OWD8Ez99E1pI4wL9CVx5-mjSUDLRvhNCoCeBwvEoiiQCKXKl0Iz_fDvDFllj-qudE0aeqQEIQbjuMIIqhGywpisDpEsJoJcs_ipACoGFbs8qOF6gIyCa7Qi37kh0IeUnQ3Tml9ADPKBwWhPhZqdKjDHO3CfEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5521d6342b.mp4?token=Kdu2PO95u9yge6pdYYJAbwTJ_XIlxm_6rKKgsjb_iyg2rBIDZsbTeTmw5Vk67Gq7i6MLlg2FnSa7dhWFEPcpUxpw7dB9LVA7UywOgiuW1Vepnoiig9oijvH100CypjuJoIzPPRgq_7yxhpBtMKVQ33Us0fzh9OX0goprdoGXsUsPotADCzP-h-fV2OWD8Ez99E1pI4wL9CVx5-mjSUDLRvhNCoCeBwvEoiiQCKXKl0Iz_fDvDFllj-qudE0aeqQEIQbjuMIIqhGywpisDpEsJoJcs_ipACoGFbs8qOF6gIyCa7Qi37kh0IeUnQ3Tml9ADPKBwWhPhZqdKjDHO3CfEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محاسبۀ غلطی دربارۀ ایران که در ۳ جنگ تحمیلی تکرار شد
@Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/463522" target="_blank">📅 23:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463515">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYnZnauRQWKv-3n2U9cMks3Z1XUxYjsIa6OqcPoKtdeU4pGAng4MC9LSPrZQpV1dO0ejV7FBKQdyZj_LDvAIK9l7jaeHQBfEI2P4kCfYDoxiCAPqqdNecTY0j0Xy_GpaTqEr3-1SU-uzGipaNnRQ8qKiYqZHiXB5e-wZ4D-e_UrnB0vKl_c9UuNv8v_wzQ05fdGUWceKM3U4ROpXyaj5mbOdGuxFk8Ay87lWHSmC4BFdeOozwu1UR1X9XbzVs2WMKccTBXQ5_pPaui0ieggBEqd7zG4Sdg1u5EnTUjIxltTkSnfmogrtCiBw06GCFu-BM4-paHMvuhd6hSbHz7Kmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7PECGj_i93KpFNElENpI9dP7TpgM3KrGDSDNb7pelQlzLrj-bTqgpuKs3xeiN6JPxYBOSfSb66wMsYGtMpjo2pNRUyuo4au4cDbtOEyd0mWZxbtJqeOLvh5fWwRUTL1orJBfHkYsJGzhjlnqflNw8IU7RwxNRUj9ziQ_1TpIQX0gPhpB3q8mMOn95iFb6Z8eDZkcwbrBJZ-4fkhMILKVmRjHArK2uy_egvIOzUKVXoTqca6-W6qr4d6whNm72Kz2ZTL6CWk9o16M3SEJomCyUZ9QowN4Uamx1SBZEIZeqX57medali22S8y6YHZQn1GcFgZGRl5WKnB9ow4W8KIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eI3b2yC3cRsNPiWa3iHbvYnBzbCQKYOG5j2ESxSdBfLjk7HVByraChAm2SmpzvgaYvdeSTaVzBUGUhtZoU5t2B2r04M8Jqz5xEYEEUCVxgnAKKdVS_VDR2rqWk4QJ3mrQrrm41KuuiMcC-rkadOoAcMnJvxFHUpusCCUxUdmJcHC93cpsGhN9NyxdqdA6BPXzaIW4H85E9ptrbAQAyXUhofMeS5aVuGcAztc_w905Uqd9nKem-IYU6MsZs_frOtO5pr_0mKOLjm_uISNvFu5tvVM2pHoqf4AZDNlpwM_fLkmyo8PdRPsaTDHQtXtnDcndTe-Eu8rHB_OGnNvH1wSXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEbIvF-E1QQso550ckGpvezYAzf65wypsww5ddhIkGXmzEEWDbQtPhzrjXpP-34fB6dIeaR3uSeoqb7Hv2XWS5xzDvJ4XMO04s9M72BVTVtpygXwaFq6wrO4K7X3iCbvec2C-gH-OxgibXf7NC4MdK05aWPCopeBH7gsiHigHBlAuUfZkemEMcUTGKl4E7QHZkopYyJR972H_s0HD8u2nTnYPgkOQN9Uvd-CUIUBw2nOBWd6lGkFV9LYP3Ekbn6iuCbalg2lkYvP8jq0Ao_MDOcCsy7Bc7CnDO2yR7A6h6miV21cz0AlNICu7HJCSEQcX7NQ4IWWieoKUniZd0sfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJet7uQ2z2_dGeSD5ou8SZ2b4KKi8YVX7-CzCFAkMpF-HmrKKLfcOWDYPDs48p0YDoXdOD9u5Aaw42FB-hCRzxqu1OW7AR3wsesXGwpqe5brQZqbK_F6IqZ4zkvMqxYaW6sNUqYYH2-UWAJFxMCrPdndqzOdSEi_DISyYof9anE-ZpConpQg5XrpYnXH2RUHIpNNwQ0g3L6pAs1ohePzX2vZi--TKwwPDCz9Am3J2Lbno_dIE3QF8UAvmSpUzAMDaRUqMTwhRBIOidAvSbYEre0X8SQ2R3WW4VxiuPrRJPm5tbYgOVZbUEyqQsWdNuT2VpIku5XbcL8Ek81q8ybPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJR9UnJfJIJgfptZwTiI64am-fq0x2XGm_ef_KL4luY5oFuPEv759YqBG9ZAwaCI0kWMXPCQzkfCs-YEovX7Omy4khUGqpTGQbxeLTB1Ao7FqqG_kXnP3gZB43ciZ1Bq0aUsCOIPn8DmLbsmSmZ0pMpdHlj2p1WWX5NvMKNMo7RO4sELpmZAHyeOKyI-qPX3T8MW_GKcl9SVIElbymEWTWy6ZQPk0jZTJ96Sl7YfA0m_7YcD1PMjimTvGNxSpSuU1018zwt14cU26VOQvJROUCGvlPlpgGOoZAyZuIpkFSXvud-YvdDOjFGSYnzNBGgTR0NnuwTYSMzmqG6Dsh4-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bp7QdLZks_b1Kityq3YDxghemHvyQfut9al3iof1c52g7rzUNgdPxA_7VMZ_-knfHLr1O2jbsOpOT91dNHv2segiIaYkvsTHJRK_OUfAP27r7_9Y6-n6_kfyOKawyxqsmlL_VvIfutUBVXT675dQfKGXotoYxGBKpME1BGQ65-D7ZhjDYFK913c_bOZzYlwthzLFXZcA0iKf7LWCSnDBiej9qk981Mpu1_eVXY_DOlbKePR0AQSH_FehBcoTzyKfBPIwe-CemKJTslTnlJ5Dm08z71JdEt_OuZSUyRiVKpWYQ6-Vb_ltuACiCaS_f5NS9XAU8scxsmYX_RUc2EJmQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین وداع با پیکر مرحوم آیت‌الله شبیری زنجانی
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/463515" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463514">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJyJq-h7VeEJt75W0GG_wItW4cb4uoI8np3UFqN50D556MIHclwPdmrs5Ub0od31HutIBX1w042ZsCJgHfIrJuEFYjyhyFKe1jeweXdGFGg8Ot943cKGj-n8cdUfPu-me6m-YxxN59bsoD2OS1skORS07JoD4Xp-DgDmniyxEMwoeARRPBuk9Wo2tqU9KrjwaBH-AYQGQqDrK_-dQliG9J7qjeSUQC0YkO9Et3YozZDkIZmKqhrem9fUPkGcZbhNItzOnkbAA1QHuhXrwIx1LhDUPAZMfpRulEFKU2ExcH-8WtubHWWOvasmTjBcif3aPENqehSzrTTF586bTkTYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جانشین فرماندۀ سپاه: درحال تقویت توانمندی‌های نظامی هستیم
🔹
سرلشکر ایزدی: اگر هوشیاری مردم در صحنه استمرار داشته باشد، بسیاری از توطئه‌های دشمن نقش بر آب خواهد شد و این خود اثر بازدارندگی ارزشمندی برای کشور ایجاد می‌کند.
🔹
ایران امروز در حوزۀ موشکی، پهپادی، موشک‌های کروز، سامانه‌های سایبری، جنگ الکترونیک و پدافند هوایی درحال تقویت توانمندی‌های خود است.
🔹
جبهه مقاومت اسلامی نیز در میدان حضور دارد و رزمندگان یمنی در مسیر مقابله با دشمن حرکت می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/463514" target="_blank">📅 23:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463513">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMjJdO-O2bMecPFs7OnALRc2N3Iau065GP9fpLlrAQcAgJ_og06yXePdQNvw34bl3g8sPE5aCo9PXC2nYcgTZZmCp1J-UILZQOmW_xgrJnHR3ZfHplxUFPFh_NIDpUpUtuO6YU4GZkAn9lz5GcVUA7asXAtkqdg_OZq4RT-AaFtYYt4ljtcNSdkN2uxJ5oTJrGq44a-jdNUzwytCIf64lDr85AwrXaiUDG5W3cwNOdgu29od25LYF-4PI1vpyNSka7iC7RuypkbXVrafrqS1-dgrLXG9I3YGzb3ww4yWfHs9Dn0VwownJKESv_Cw5eQH3G2WNqrdaaGlNPBR14fddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک به چین؛ ذخایر نفتی ریخت
🔹
موجودی نفت خام در استان شاندونگ چین، یکی از مهم‌ترین مراکز پالایش نفت این کشور، در ماه ژوئیه حدود ۳۵ میلیون بشکه کاهش یافت.
🔹
افتی که بر اساس برآورد Energy Aspects، بزرگ‌ترین کاهش ماهانه در داده‌های این مؤسسه از سال ۲۰۱۶ تاکنون بوده است.
🔹
شاندونگ محل فعالیت بخش عمده پالایشگاه‌های مستقل چین موسوم به «تپات» است؛ پالایشگاه‌هایی که سهم قابل‌توجهی از نفت تحریمی ایران را خریداری می‌کنند.
🔹
کاهش ذخایر این پالایشگاه‌ها می‌تواند آن‌ها را برای بازسازی موجودی، به افزایش خرید نفت در هفته‌های پیش‌رو سوق دهد.
🔹
داده‌های جدید همچنین نشان می‌دهد برداشت از ذخایر نفت چین پس از ماه‌ها کاهش واردات، همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/463513" target="_blank">📅 22:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463512">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01ac8747a9.mp4?token=I9ON3103agexrz2kPL8XVqNAp7odn5KLuJg0i69Gwfbwk4Fw7RcC0w8OSzwuvPCrBAHRyqDfC07prY5XFZSj42QNRjWbWVA1Bt4wawD0Itgvz3VxHvic15cKFT9N0bP8qVnNtt5sk9LfjOF8L0K_xLm6jySjLXsjCDYOvu22mWz_F513Kvmhwl-iFK1FQ_TtJsRVgpyzSzuowdSNR7EgeKAeHTj7ubPk3XodWjv0ejv-ybG9q4YgpqM3WTBPORvFDmUr40kAKy7yw4zHg-A3nV1gKHSzT2grCOp7tTkZ7Qhsutlxa9jqPFPzynWCHlD6BTeZRW7cCH8YZPtzL3AMVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01ac8747a9.mp4?token=I9ON3103agexrz2kPL8XVqNAp7odn5KLuJg0i69Gwfbwk4Fw7RcC0w8OSzwuvPCrBAHRyqDfC07prY5XFZSj42QNRjWbWVA1Bt4wawD0Itgvz3VxHvic15cKFT9N0bP8qVnNtt5sk9LfjOF8L0K_xLm6jySjLXsjCDYOvu22mWz_F513Kvmhwl-iFK1FQ_TtJsRVgpyzSzuowdSNR7EgeKAeHTj7ubPk3XodWjv0ejv-ybG9q4YgpqM3WTBPORvFDmUr40kAKy7yw4zHg-A3nV1gKHSzT2grCOp7tTkZ7Qhsutlxa9jqPFPzynWCHlD6BTeZRW7cCH8YZPtzL3AMVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الهویی، دستیار قلعه‌نویی: ۷ بازیکن تیم امید در لیست تیم ملی بودند
🔹
اگر مسابقات آسیایی ناگویا نبود این افراد به تیم ملی بزرگسالان دعوت می‌شدند.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/463512" target="_blank">📅 22:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463511">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b814db725.mp4?token=uTnN_uiumNVheVpF4phWN9x_fZWi_1c1FlGCIbjTevpGhtQnaVKyWozkkcNfKZp8bozj5VVFXZHbjSgQtCkTgfz1ELgZaDbVP3DZ7rFV5Gzpk6jNixrZKxY6QyVoDGioPJYs6dxhmXj29Mo1qrjKb6VceGNMuuxyEWVAcDlCw0kSbU0usV2q-hDdU_rB0Z_XJx1bE-r37aLM4OQhyIkMij04xlhOnywTNLQ2JuT2YUrEsT3VJ9lmQC1R92Jc3EGpRtUs1MnxfXOzIPBbcxj9cx6oty9YZiOisWNiP8nE2J_HealJdt_oINKRp9HtUyV-ggxWzDrQzqtt2YzQ8LrZEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b814db725.mp4?token=uTnN_uiumNVheVpF4phWN9x_fZWi_1c1FlGCIbjTevpGhtQnaVKyWozkkcNfKZp8bozj5VVFXZHbjSgQtCkTgfz1ELgZaDbVP3DZ7rFV5Gzpk6jNixrZKxY6QyVoDGioPJYs6dxhmXj29Mo1qrjKb6VceGNMuuxyEWVAcDlCw0kSbU0usV2q-hDdU_rB0Z_XJx1bE-r37aLM4OQhyIkMij04xlhOnywTNLQ2JuT2YUrEsT3VJ9lmQC1R92Jc3EGpRtUs1MnxfXOzIPBbcxj9cx6oty9YZiOisWNiP8nE2J_HealJdt_oINKRp9HtUyV-ggxWzDrQzqtt2YzQ8LrZEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد ضد استکباری کرمانی‌ها در اجتماع ۲۰۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/463511" target="_blank">📅 22:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463510">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رکورد حزب پوتین در انتخابات روسیه
🔹
حزب روسیۀ متحد به‌عنوان حزب ولادیمیر پوتین با کسب ۳۵۵ کرسی از مجموع ۴۵۰ کرسی دومای دولتی روسیه، رکورد جدیدی برای خود ثبت کرد.
🔹
این نتایج اولیه مربوط به انتخابات ۱۸ تا ۲۰ سپتامبر است که رئیس کمیسیون مرکزی انتخابات روسیه اعلام کرد.
🔸
این نتیجه اکثریت حزب پوتین را افزایش داده و رکورد قبلی این حزب یعنی ۳۴۳ کرسی را نیز شکسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/463510" target="_blank">📅 22:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMCpvET44NsAuBxRQaQfEKGV7qNWVf6yLA5melU8PfJRYThjJbSKzzwc05Q_V074NTtWJRw3Ei6KZ7brka-eoJS9FrN16CIVfaZuRFYhs9B96nXBi0wY_CaNrKMWAMBMfNo1Zp13TwSqF1taR2IA-pgcG92SbLgSx3tflhIWf0CP1hPyMUzxq2VwiUZZwmiPexbbZ17aivHG9GSY6WYPA4VXLwG0GSDqiHO0Wv39KDEh7RVo48ICLZEGFP1vXEp7s1WVpvBLRgJsVCGj5oy28SroMcA_L7ngX90JFwiATQc9RbAIJb0u014P202m27FB-Emlk-epCxmDB7p6evI5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر سابق ارشاد: دوگانۀ میان «جنگ» و «صلح» غیرواقعی است
🔹
اسماعیلی: رهبر انقلاب با صراحت اعلام کردند ارتکاب هر آن‌چه به ضرر انسجام اجتماعی باشد، ممنوع است اما بخشی از نیروهای سیاسی همچنان با ادبیاتی آکنده از ناامیدی، شکاف‌ها و سرخوردگی‌ها را تشدید می‌کنند.
🔹
نمونۀ روشن آن، دوگانه‌ای است که بین «صلح» و «جنگ» ساخته می‌شود؛ درحالی‌که اساساً دوگانه بر سر «مقاومت» و «تسلیم» است و تنها راه ادامه مقاومت برای تأمین منافع ملی است.
🔹
ما باید یاد بگیریم مطالبه بر اساس موازین، خلاف انسجام نیست؛ آنچه خلاف انسجام است، تخریب و توهین و ایجاد بدبینی به مسئولان نظام است نه مطالبه‌گری.
🔹
انسجام واقعی، انسجامی است که در آن هم نقد مسئولان و سیاست‌ها ممکن باشد و هم مسیر دیپلماسی برای تأمین منافع ملی باز بماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/463509" target="_blank">📅 22:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429a53ffd0.mp4?token=Ar5xcj3KriPbXLtLOcBJVmrNGInbKgHJ3oso2MJLQm1y7etQQDQi6ZCQ4Jl5mBOIARvFnSyMS2us-lYODFwVtl5HeaByI7DJzruia3fgRi1vXggZeYT0JgxfvrBC7NJlZ7nJV3Ve_LU1_1x44Trrq69blvWIE0c0IUvmwcbwAtjmv33N-N-vILIo2swQcvz8dyzQo-c12sRSg3XJmaawNjMO3DKTohG6dwulXU7i_oqFGorFmohJRKmQEhZJDOsraekDyF6YeRynWwdfOsmIvHe7Ylda_2siDqMMlciGBL4vAoqmNgPCOLauDhZIalBmN3kxoY21Xhp6LZX9LUr9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429a53ffd0.mp4?token=Ar5xcj3KriPbXLtLOcBJVmrNGInbKgHJ3oso2MJLQm1y7etQQDQi6ZCQ4Jl5mBOIARvFnSyMS2us-lYODFwVtl5HeaByI7DJzruia3fgRi1vXggZeYT0JgxfvrBC7NJlZ7nJV3Ve_LU1_1x44Trrq69blvWIE0c0IUvmwcbwAtjmv33N-N-vILIo2swQcvz8dyzQo-c12sRSg3XJmaawNjMO3DKTohG6dwulXU7i_oqFGorFmohJRKmQEhZJDOsraekDyF6YeRynWwdfOsmIvHe7Ylda_2siDqMMlciGBL4vAoqmNgPCOLauDhZIalBmN3kxoY21Xhp6LZX9LUr9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوزادی که قصه‌اش از میدان خیابان آغاز شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/463508" target="_blank">📅 22:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463507">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFafty5YR6Trh2znZnl1YX-LgcSe4npATsfYmwS9G3JpO3ypl84rvipkLLQZGwRSaWb4ApJIU_t4zKiSSozVGBvVXt7HMSdfsDe2_Oyl-Pbl28z2jB-nRJyLDa4JduhBdm_QPg8PLRsXiZtC78JiCeMqiLtdVpM-392YYdfEo3UVG0KCVNvEkqLS7gvef3rsCJvpx7-gdna4pj00Ow0_OHWIHzwRi8ElfXVlD3iSn0VnCLX9oU_t-37MT0i2cjz8x3VPa6flT1-oaJ1Qffytu-gDbfOlSeqwlemmPsi6_c_0vgOJZiUEs9W9hq_bL372Da-eov2-x1EJs_8ieJvJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت ۹ انگلیسی مقابل کارخانۀ سازندۀ پهپادهای اسرائیلی
🔹
۹ معترض انگلیسی مقابل کارخانه‌ای متعلق به شرکت اسرائیلی البیت در استافوردشر انگلیس هنگام اعتراض به همکاری‌های نظامی با رژیم صهیونیستی بازداشت شدند.
🔸
این اعتراض‌ها در ادامۀ موج اعتراضات در کشورهای اروپایی علیه همکاری‌های نظامی با اسرائیل و در واکنش به جنگ غزه برگزار شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/463507" target="_blank">📅 22:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463506">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
من
جوانی
بیکار از
خرم‌آباد لرستان
هستم. با وجود استعداد و مدارک مختلف به‌دلیل کمبود فرصت‌های شغلی و مشکلاتی مانند شرط سابقه و پارتی‌بازی، هنوز
نتوانسته‌ام کار پیدا کنم
. بارها برای پیگیری به مسئولان مراجعه و نامه‌نگاری کرده‌ام اما کسی پاسخگو نبوده است. خواهشمندیم صدای جوانان بیکار را به گوش مسئولان برسانید.
🔹
معلمان حق‌التدریس دانشگاه‌ها از جمله
حق‌التدریس‌های دانشگاه المصطفی
از
ابتدایی‌ترین حقوق یک شغل برخوردار نیستند
؛ نه بیمه دارند، نه سابقه مفید، نه امنیت شغلی و نه حتی درآمدی که بتوان آن را متناسب با زحماتشان دانست. در حالی که بسیاری از دانشگاه‌ها نیاز آموزشی خود را با استفاده از همین نیروهای تحصیل‌کرده و توانمند تأمین می‌کنند، متأسفانه هیچ توجه و حمایتی از این قشر نمی‌شود.
🔹
چرا دولت وعده‌ای می‌دهد که در عمل اجرا نمی‌شود؟ برای ثبت‌نام
کلاس چهارم در یک مدرسه هیأت امنایی در منطقه ۶ تهران
اقدام کردیم اما با ما تماس گرفتند و گفتند
باید ۲۰ میلیون تومان شهریه پرداخت کنیم
. اگر هر کلاس ۲۰ میلیون تومان پرداخت کند و مدرسه ۱۰ تا ۱۲ کلاس داشته باشد، درآمد مدرسه از این محل به حدود ۷ تا ۸ میلیارد تومان می‌رسد. با احتساب حقوق معلمان، مدیر و معاونان و سایر هزینه‌ها، این سؤال برای خانواده‌ها مطرح است که
این مبالغ دقیقاً صرف چه مواردی می‌شود؟
وقتی مدارس دولتی و هیأت امنایی هستند، تکلیف آموزش رایگان چه می‌شود؟
🔹
لطفاً صدای ما را به گوش مسئولان برسانید. من یک کارمند سادۀ دولتی و
نیروی شرکتی هستم. چرا برای
تبدیل وضعیت نیروهای شرکتی
اقدامی نمی‌شود؟ با این حقوق پایین، از طرفی قیمت کالاها نیز روزبه‌روز افزایش پیدا می‌کند. با چنین حقوقی چگونه می‌توان از عهده هزینه‌های زندگی برآمد؟ آیا
مسئولان کشور حاضرند فقط یک ماه با حقوق یک نیروی شرکتی زندگی کنند؟
🔹
لطفاً شکایات مربوط به
وضعیت خدمات‌رسانی در بیمارستان سینا
را پیگیری کنید. رسیدگی به بیماران بسیار ضعیف شده و شرایط برای همراهان نیز عذاب‌آور است. هر زمان همراهان نسبت به وضعیت رسیدگی اعتراض می‌کنند، پاسخ داده می‌شود که «اینجا اروپا و آمریکا نیست که هر بیمار یک پرستار داشته باشد». از طرفی گفته می‌شود شب‌ها خدمات کافی به بیماران ارائه نمی‌شود و همراهان باید برای مراقبت از بیمار، از بیرون پرستار خصوصی بگیرند.
🔹
من یک کارگرم و یک
پراید دوگانه‌سوز
دارم که
تاریخ کپسول‌های گاز آن تمام شده
است. برای تعویض کپسول مراجعه کردم و گفتند حدود ۳۰ میلیون تومان هزینه دارد. با حقوق ۲۵ میلیون تومانی و داشتن دو فرزند، واقعاً از کجا باید این مبلغ را تأمین کنم؟ در شرایطی که
هزینه بنزین هم افزایش پیدا کرده
، خودروهای دوگانه‌سوز برای ما یک ضرورت هستند.
🔹
حدود ۵ سال از تحویل
واحدهای مجتمع فردوس مراغه
توسط انجمن خیرین مسکن ساز آذربایجان شرقی می‌گذرد تا به حال
اسناد مالکیت
واحدهای مسکونی به بهانه‌های واهی که اکثرا از اعضای تحت پوشش بهزیستی هستند،
تحویل داده نشده
و موجب مشکلات بر این قشر آسیب‌دیده شده است.
🔹
من
راننده تاکسی درون‌شهری
در یکی از شهرستان‌های استان خراسان رضوی هستم و حدود یک سال است که مشغول به کار شده‌ام. از همان ابتدا درخواست بیمه داده‌ام اما هر بار که برای پیگیری مراجعه می‌کنم، مسئول مربوطه می‌گوید
باید جواب از تهران بیاید
. واقعاً نمی‌دانیم چرا بیمه رانندگان تاکسی شهرستان‌ها باید این‌قدر بلاتکلیف بماند. ما هم مانند سایر رانندگان
نیاز به بیمه و حمایت داریم
. با توجه به هزینه‌های بالای زندگی، دارو و درمان، نداشتن بیمه فشار بسیار زیادی به خانواده‌ها وارد می‌کند. فرزندم نیز معلول است و هزینه‌های درمان و دارو برای ما سنگین است.
🔹
خواهش می‌کنیم در مورد
افزایش شدید قیمت انسولین قلمی لانتوس و نوورپید برای بیماران دیابتی
پیگیری کنید. قیمت هر قلم با وجود داشتن بیمه تأمین اجتماعی، پنج برابر شده است. من همین شنبه برای تهیه انسولین یک میلیون و ۵۰۰ هزار تومان پرداخت کردم؛ این در حالی است که هزینه نوار تست قند خون نیز جداگانه است. ما بیماران دیابتی هر ماه به انسولین نیاز داریم.
چرا ارز ترجیحی انسولین قلمی حذف شده است؟
این دارو برای ما حیاتی است و بدون آن امکان ادامه زندگی عادی نداریم.
🔹
کارکنان کارخانه
واگن‌سازی زرند کرمان (پلور سبز)
دو ماه است که
حقوق خود را دریافت نکرده‌اند
و هر ماه به بهانه‌های مختلف پرداخت حقوق به تأخیر می‌افتد. در حال حاضر کار کافی در کارخانه وجود ندارد و
اعلام ورشکستگی نیز شده است
. از طرفی طلبکاران برای وصول مطالبات خود و مصادره اموال کارخانه مراجعه می‌کنند؛ در حالی که حدود ۲۰۰ نفر از کارکنان همچنان در این مجموعه مشغول به کار هستند و زندگی و معیشت خانواده‌هایشان به حقوق همین شغل وابسته است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/463506" target="_blank">📅 22:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463505">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0ZHvU7IeGLAfT66XLs66igehxljxZZVznsi8mtWfrK8KGpL2aZRDrtV7t2bASw5r9qDiqhRFm87V84aEcw6W1LUaXUF6grzaN1X8WUWY7EKAItAn6RCXc32sG6JURQgt6BGeBNfyynxYdgbY09-6wy-YI2LNNPt_USLvUk2yZSOUi77JCKUIddVypljpl8Ne0LlYIszPhrp3ZB7Q7LKqWdS6cgGPJHeKosuSOZokV05TwxIzYbYAGIUf8687C4ED5MHdS8E4u5g4tulKlQQGm91tUPPOwQONpYD4St99Wr6kM0Qw5paeEzEkFAn6NRPwq9RkWOQDQgbJ_CyIY62GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیج: حضور مردم باعث همبستگی و تقویت روحیۀ رزمندگان است
🔹
هفتۀ دفاع مقدس، یادآور حماسه بزرگ ملت ایران در دفاع از تمامیت ارضی ایران و آرمان‌های انقلاب است.
🔹
ملت ایران با حرکت در مسیر رهبری آیت‌الله سیدمجتبی خامنه‌ای، مسیر عزت، پیشرفت و سربلندی را با هوشیاری دنبال خواهد کرد.
🔹
ملت مبعوث و بزرگ ایران، بیش از ۲۰۰ شب است که با حضور آگاهانۀ خود در میادین کشور، حمایت و پشتیبانی خود را از نظام اسلامی، رهبری و نیروهای مسلح به نمایش گذاشته است.
🔹
این حضور موجب تقویت روحیه رزمندگان و تجلی همبستگی و عزم ملی شده و  جلوه‌ای از همان روحیۀ دوران دفاع مقدس است.
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/463505" target="_blank">📅 22:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463504">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار یک خودروی ارتش اسرائیل در نوار غزه
🔹
شبکه ۱۴ رژیم صهیونیستی: یک بستۀ انفجاری در خودروی متعلق به ارتش اسرائیل در شمال نوار غزه منفجر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/463504" target="_blank">📅 22:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463503">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b1ff18b5.mp4?token=Wt5ePF38QT3djv6GSBbWui2cD2_0EdNR-jvdTYdyfHl7T5-e1f6sMEKGb0A2b_RWWEyAJ3kyT1tHvw_Mhjb4eZ4M_bZaofPximj6m6S4ZuHlCpipfm4aoIXpxvpR1UGV6cmwNuEzpSh9HZXCcYb_vkqFY3NOKq7vGztoMK_dsEbTnok9a89qYl5CZ1DJungGcVDt4j_YOB8Oosx_umCaN5T-rnhAPw_QXvEDuV3CGQw40OXNkQY3h8kiHSN0fTulYhPM2d9ONBIugzPSstimEL49BOn6zZ1wKMnF-S6Cj1I7zKTjHPZPThMOs_VsdwBLpRcLb8R7JYu2WD_a7vDcfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b1ff18b5.mp4?token=Wt5ePF38QT3djv6GSBbWui2cD2_0EdNR-jvdTYdyfHl7T5-e1f6sMEKGb0A2b_RWWEyAJ3kyT1tHvw_Mhjb4eZ4M_bZaofPximj6m6S4ZuHlCpipfm4aoIXpxvpR1UGV6cmwNuEzpSh9HZXCcYb_vkqFY3NOKq7vGztoMK_dsEbTnok9a89qYl5CZ1DJungGcVDt4j_YOB8Oosx_umCaN5T-rnhAPw_QXvEDuV3CGQw40OXNkQY3h8kiHSN0fTulYhPM2d9ONBIugzPSstimEL49BOn6zZ1wKMnF-S6Cj1I7zKTjHPZPThMOs_VsdwBLpRcLb8R7JYu2WD_a7vDcfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چراغ خیابان با حضور مردم در شب ۲۰۵ همچنان روشن است
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/463503" target="_blank">📅 22:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463502">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
خبرگزاری رسمی لبنان: رژیم صهیونیستی مناطقی در اطراف شهر صور را با چند بمب فسفری هدف حمله قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/463502" target="_blank">📅 22:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463501">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e45ab4a5.mp4?token=MzhpmyWSjtOKwKaWnWmgaVqlAlkutZ2cmVczCil3nkT_alyF9HzMb6fwrF8LTW38BKhL7NGpJwy3Ai7xmkamBJvxtIutfyV3KwW8_yzE5E_V2GCSBMMq0orh8RrQao9cKTNkw3ZErSAEdAkh6HTDm7RGaekXe1XOp9gaBjemXmMe-FME3bfAJhswRoSaR6c_T08Cf5PQLVWhQCte0IN9xUG5jpNCw6kyFZRbelTGw7Jr1CNz48c2rAWrrr90U_rzr1h0X3PbD4tYR3dFgrgxoyQWjR-xgLOLaKIUGNvafklO7874OxDNbp5i2DXolu0kz7te30T5UUmtm6SJFk56ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e45ab4a5.mp4?token=MzhpmyWSjtOKwKaWnWmgaVqlAlkutZ2cmVczCil3nkT_alyF9HzMb6fwrF8LTW38BKhL7NGpJwy3Ai7xmkamBJvxtIutfyV3KwW8_yzE5E_V2GCSBMMq0orh8RrQao9cKTNkw3ZErSAEdAkh6HTDm7RGaekXe1XOp9gaBjemXmMe-FME3bfAJhswRoSaR6c_T08Cf5PQLVWhQCte0IN9xUG5jpNCw6kyFZRbelTGw7Jr1CNz48c2rAWrrr90U_rzr1h0X3PbD4tYR3dFgrgxoyQWjR-xgLOLaKIUGNvafklO7874OxDNbp5i2DXolu0kz7te30T5UUmtm6SJFk56ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۵ شب ایستادگی گنابادی‌ها برای وطن در شب رحلت حضرت معصومه (س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/463501" target="_blank">📅 21:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463500">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1lUDB5-gp5VH6Nrkhjj2rb9_s_Ge4zwPSt2zMWJDTqlV7grk54OgMl9Fi_2h6aOTfzOpfJvkyZ8z-I4zeXROauban5Ds3B0tscZBpTXuKWCPskMNMEnVrsw_hP7DbgQOmfKu8Vzj1cZbpZK1oAkNTmgGWLa88kQx3IoJuKmQZCfiQKh4UCqulYM9z8vgEfUWlo9crmnueuhliTrkKeAXEbyORk7ETt8diSfkCi0p4CXHCE-Ir1CBOij-Y0IQlop3sm3QNG5Rp3WDwrG5-C7t44eQlc9JocrZwBIDf992m_kKvYPCC_Udf5Yc680G-42j_NNYGG0ZMjBO6rLL2AM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیابی کاربران برای گوگل گران تمام شد
🔹
رویترز: رگولاتور حفاظت از داده‌های ایرلند، گوگل را به دلیل نحوه پردازش و نگهداری داده‌های موقعیت مکانی کاربران به پرداخت ۴۰۳ میلیون یورو جریمه کرد؛ پرونده‌ای که به نقض مقررات حفاظت از داده‌های اتحادیه اروپا مربوط می‌شود.
🔹
کمیسیون حفاظت از داده‌های ایرلند اعلام کرد گوگل در فاصلهٔ سال‌های ۲۰۱۸ تا ۲۰۲۰، در ۳ قابلیت «فعالیت وب و برنامه‌ها»، «سابقه موقعیت مکانی» و «دقت موقعیت مکانی» الزامات مقررات عمومی حفاظت از داده‌ها (GDPR) را نقض کرده است.
🔹
این نهاد همچنین گوگل را موظف کرده ظرف ۶ ماه شیوه پردازش داده‌های موقعیت مکانی خود را با قوانین اتحادیه اروپا منطبق کند.
🔹
نحوهٔ عملکرد گوگل می‌توانست باعث شود کاربران از استفاده از موقعیت مکانی خود برای اهدافی مانند هدف‌گیری تبلیغات یا استنباط علایقشان آگاه نباشند و کنترل کمتری بر داده‌های شخصی خود داشته باشند.
🔹
این جریمه چهارمین جریمهٔ بزرگ کمیسیون حفاظت از داده‌های ایرلند از زمان اجرای GDPR در سال ۲۰۱۸ محسوب می‌شود و مجموع جریمه‌های این نهاد علیه شرکت‌های بزرگ فناوری از مرز ۴ میلیارد یورو عبور کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/463500" target="_blank">📅 21:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463499">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سپاه پاسداران: آمریکا و اسرائیل دیر یا زود باید به خروج از منطقه تن بدهند
🔹
بیانیۀ سپاه به مناسبت هفتۀ دفاع مقدس: نیروهای مسلح با آمادگی کامل و هوشمندی راهبردی، دست بر ماشه آماده پاسخ‌های قاطع و ویرانگر به دشمن فرسوده و متجاوز هستند.
🔹
آمریکا و رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/463499" target="_blank">📅 21:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463498">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سپاه پاسداران: آمریکا و اسرائیل دیر یا زود باید به خروج از منطقه تن بدهند
🔹
بیانیۀ سپاه به مناسبت هفتۀ دفاع مقدس: نیروهای مسلح با آمادگی کامل و هوشمندی راهبردی، دست بر ماشه آماده پاسخ‌های قاطع و ویرانگر به دشمن فرسوده و متجاوز هستند.
🔹
آمریکا و رژیم صهیونیستی باید به منطقه عاری از وجود پلید و جنایتکارانه خود تن دهند.
🔹
نیروهای مسلح جمهوری اسلامی ایران با تکیه بر دانش بومی، نوآوری راهبردی و خوداتکایی دفاعی، به سطحی از اقتدار رسیده‌اند که هر تهدید را در مبدأ خنثی می‌کنند.
🔹
دشمن پس از ناکامی در عرصه نظامی، به جنگ‌های ترکیبی، شناختی، اقتصادی و رسانه‌ای روی آورده است؛ اما ملت ایران با اتکا به ظرفیت‌های درونی، اقتصاد مقاومتی و اتحاد مقدس ملی، هر توطئه‌ای را خنثی خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/463498" target="_blank">📅 21:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463497">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286a62c5b4.mp4?token=QLAS9Pjz3bDovBtoKySinjN91xeWJebt-xbX6TKjEp8uQxW4E4Mk_BxppYXOJrSUWGnn-YY7XMo_4OOffo-mpoVwYa6JPXZV5ijG54kT8gNfFSdGSyjD1EiX1M5vMCDFyv_Q0eNqitdjKcRgp623wCPaFmR46UefD-NIx4sUURqpDTEG1Hg98nMNuHYtweLezQESPSO_30bmCFNz6DC8x5FF0gzr-F474DG6y4tEYvu5rBAgmjmOTW02jW1HT8IguTtyZiI5YhDDYCEHg7ZsvtSVv5odIPIYBuzRqgymf0JwgKjhVzSmuwlB1qelAWj_rgMwweVmSdeo8Q8mVEG34A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286a62c5b4.mp4?token=QLAS9Pjz3bDovBtoKySinjN91xeWJebt-xbX6TKjEp8uQxW4E4Mk_BxppYXOJrSUWGnn-YY7XMo_4OOffo-mpoVwYa6JPXZV5ijG54kT8gNfFSdGSyjD1EiX1M5vMCDFyv_Q0eNqitdjKcRgp623wCPaFmR46UefD-NIx4sUURqpDTEG1Hg98nMNuHYtweLezQESPSO_30bmCFNz6DC8x5FF0gzr-F474DG6y4tEYvu5rBAgmjmOTW02jW1HT8IguTtyZiI5YhDDYCEHg7ZsvtSVv5odIPIYBuzRqgymf0JwgKjhVzSmuwlB1qelAWj_rgMwweVmSdeo8Q8mVEG34A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های عزاداری وفات حضرت معصومه(س)  در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/463497" target="_blank">📅 21:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463496">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ebe0de86.mp4?token=b7nSHMjOzlzk9GNJcftAEsunJaVCBqH6QPyK8Sf52aGBr7Qa9HCYhqasmTv6TIEKbZvrDNTJSlgnDV50oDi4sGE_YJjbWZ_hTq-T6-doNcpe9X0F3Gqdu5Ty83u9KPbqNMbQ7DZNE_1hH82QJKr0XyiVencluicj3cMVC-ZAH1bc-JYI4nj3IN6NsSYjs52TryyeNiWgScBIMM1o6tzBXsBNPFSiAaDe1EBCtn7LNQi-JRGUeE_67sPx5PFmyXP89K1UKgtYGBuzkx2C4LVBaDMOt3isbHcrbKsROEmqecTtTaOexfeUeGKdq4hKproWR45t1EbvQtvXFx2ho1rzPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ebe0de86.mp4?token=b7nSHMjOzlzk9GNJcftAEsunJaVCBqH6QPyK8Sf52aGBr7Qa9HCYhqasmTv6TIEKbZvrDNTJSlgnDV50oDi4sGE_YJjbWZ_hTq-T6-doNcpe9X0F3Gqdu5Ty83u9KPbqNMbQ7DZNE_1hH82QJKr0XyiVencluicj3cMVC-ZAH1bc-JYI4nj3IN6NsSYjs52TryyeNiWgScBIMM1o6tzBXsBNPFSiAaDe1EBCtn7LNQi-JRGUeE_67sPx5PFmyXP89K1UKgtYGBuzkx2C4LVBaDMOt3isbHcrbKsROEmqecTtTaOexfeUeGKdq4hKproWR45t1EbvQtvXFx2ho1rzPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی محل آموزش نظامی «جان‌فدا» در تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/463496" target="_blank">📅 21:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463495">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787e477c67.mp4?token=jAUKzRwQDOXVmstbvY-cFtqlXwFLUkCbwDF-jeX8RVztrLiCpeO_TEgpYkQirhHHq-iO42xyls3C7BuS7NOCqST5fpqiGF6QvFnRnexiuqjrsO9m_0pO0BQlrWvlKOsIx7mlVLp7q2CUnnv8sH1-fZYIcl0OhQw820fCGs-1_LHAWTR3ZirrSB3qI8poOJO5RY5LPhwi2qkUjzaNxtxUaSgR1cfQNHMMiyntTY92ErkegvEBGrx4uK5t4pfaeo4XMDJoS8nRGmFa-14KAGKb6zm_i12FVMc9MkJsNFUZoiixn5WvJmfooXNfu2oKcoKanTP_DvnHve2JzXZw6DbK3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787e477c67.mp4?token=jAUKzRwQDOXVmstbvY-cFtqlXwFLUkCbwDF-jeX8RVztrLiCpeO_TEgpYkQirhHHq-iO42xyls3C7BuS7NOCqST5fpqiGF6QvFnRnexiuqjrsO9m_0pO0BQlrWvlKOsIx7mlVLp7q2CUnnv8sH1-fZYIcl0OhQw820fCGs-1_LHAWTR3ZirrSB3qI8poOJO5RY5LPhwi2qkUjzaNxtxUaSgR1cfQNHMMiyntTY92ErkegvEBGrx4uK5t4pfaeo4XMDJoS8nRGmFa-14KAGKb6zm_i12FVMc9MkJsNFUZoiixn5WvJmfooXNfu2oKcoKanTP_DvnHve2JzXZw6DbK3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قانون خوبه یا بد؟ بستگی داره کجای دنیا باشی!
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/463495" target="_blank">📅 21:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463494">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/717a4fbd05.mp4?token=KudYMUa24kGJbttKhaR2f1K1U_YeqY_1uK7LKiq-Cq7Fdyq_zHwSdm47DbfY6BU7os788DUk7wEf2WqRTa1LeXH9JugemKC9_eaEQkAaqr_Or2GpHhHG2DaoZiFHkBxOb6VrU6sqsfsrTqQMMTHrA8lSmVdfx-y0F2Jk42f_lpZZ0V3OflRt0lc8bzEXjrIVWWk0w3WO0T4G49dFOgFmzXkgyRSDlr1oxunVxncVrtT8TSpOPJFjWoN2gVcMyGnmgapKj3214ze8Fs907WZWxjLd19Rzy2DXuOaQi1flf4dlIygOieoAsPfg2a9Kit7Vr97st1DLrMYtDzO-3_a9ymsJkogJPHP57qQbV9kuj9qVdqXQzhcLlNxYcSts4bEJl3sl3ew3K8IX8YsXWpMkPTJEHnINUD4gPlOjnSgDHo5J2SPt1nKxucziCyO26RqDJGJDlzVC8IylG1CprbVFxT2YMYcQdn3p9_bzpMrJFhdpsWItuQVXzg-z4itVQ0oAs6mdVbObC38nxI4yJy1HXxEzoQ6Ymz1iDxV2gByBm5fO4_OoSQX1d6INnr6rEDoVqi3oN_GR3_7ZJDMz40ogdFtad4DpsfW3nJR273F0Swf-No2sSOgnDkvhPHbHu4IWSkpq7kVZoNRKtNDKLu9gHJU8M0fNPweA8FeKpKRHcMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/717a4fbd05.mp4?token=KudYMUa24kGJbttKhaR2f1K1U_YeqY_1uK7LKiq-Cq7Fdyq_zHwSdm47DbfY6BU7os788DUk7wEf2WqRTa1LeXH9JugemKC9_eaEQkAaqr_Or2GpHhHG2DaoZiFHkBxOb6VrU6sqsfsrTqQMMTHrA8lSmVdfx-y0F2Jk42f_lpZZ0V3OflRt0lc8bzEXjrIVWWk0w3WO0T4G49dFOgFmzXkgyRSDlr1oxunVxncVrtT8TSpOPJFjWoN2gVcMyGnmgapKj3214ze8Fs907WZWxjLd19Rzy2DXuOaQi1flf4dlIygOieoAsPfg2a9Kit7Vr97st1DLrMYtDzO-3_a9ymsJkogJPHP57qQbV9kuj9qVdqXQzhcLlNxYcSts4bEJl3sl3ew3K8IX8YsXWpMkPTJEHnINUD4gPlOjnSgDHo5J2SPt1nKxucziCyO26RqDJGJDlzVC8IylG1CprbVFxT2YMYcQdn3p9_bzpMrJFhdpsWItuQVXzg-z4itVQ0oAs6mdVbObC38nxI4yJy1HXxEzoQ6Ymz1iDxV2gByBm5fO4_OoSQX1d6INnr6rEDoVqi3oN_GR3_7ZJDMz40ogdFtad4DpsfW3nJR273F0Swf-No2sSOgnDkvhPHbHu4IWSkpq7kVZoNRKtNDKLu9gHJU8M0fNPweA8FeKpKRHcMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماعات شبانه، حال‌وهوای اول مهر گرفت
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/463494" target="_blank">📅 21:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463493">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOTxle3pE7fvOua1jmchHXLJnyYkuOkmN792FhVCEXiJJsztv7nq_2slW5S8vPLR-i0Tf7_5nG7KAtmHjmaWc-yu6Ex-hKCZLgPF1IK1DueknmrxTt9SQYruMOembAL8XQaGptNqZ3LzLETKrORXmqykI60-VazKDkZxuOda8QREx7w6PSP2_idBINHVroeSoDEzirmgbOM4jnw6y73UuBIHGcZwqmYB5S4cpRAt2pQ_RmcUVRi0uBAmc1zHdmwcZNLj6Ouxwb52FAwgtFwip2DtasC90g4WUUQt9sTzOlPpa38JsmJyT4OZEIEFccBHVXlHeX55PUY1_BvLa0pBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار با وزیر کشور پاکستان: ایران و پاکستان از قدرت‌های منطقه هستند
🔹
امیدواریم با توسعۀ سرمایه‌گذاری‌های مشترک و تسهیل همکاری‌های اقتصادی، شاهد تعمیق هرچه بیشتر روابط ایران و پاکستان باشیم.
🔹
اقدامات و فشارهای آمریکا، زمینه‌ساز افزایش هم‌گرایی و تعامل مستمر میان کشورهای اسلامی شده است.
🔹
ایران و پاکستان از کشورهای قدرتمند منطقه هستند و از ظرفیت‌های عظیم برخوردارند؛ اگر این ظرفیت‌ها را کنار هم قرار دهیم می‌توانیم بسیاری از نیازهای خود تامین کنیم.
🔹
تقوی، وزیر کشور پاکستان هم گفت: معتقدیم که روابط ایران و پاکستان هیچ‌گاه در چنین سطح بالایی که امروز شاهد آن هستیم، قرار نداشته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/463493" target="_blank">📅 21:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463492">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34d716b53.mp4?token=jYv7HqlYCwoJX9NY8V5UcDciXn-hUDG3BAzwL0oh6TK4t5NXJ0Ntbo4YkKmExUGVPpREBAAIXBJx5blnzQ7mcl21RQbz0VB-YxLz7LNb7ftHF-20NAcb9SmSHgaMChhWwA5bwtgHgsmhRfvbviDZO14wF1MXMSjpp4e3PYoqCLbet59zVSTfsroUYnQpsS_JQI9JgFpsHhhEWUEDIg9o3L4MafKGXaxd4-pV2ibTEyHeMXqlpAfGkmFKiqRk1eyX5E0nb-sGFxvhWAo9OQqwn_fKxwKERz2O1Q13KGkcYsxZFZyTlWzNuIPe1gCOxPJELudMJAfVitpVnaux5tvUGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34d716b53.mp4?token=jYv7HqlYCwoJX9NY8V5UcDciXn-hUDG3BAzwL0oh6TK4t5NXJ0Ntbo4YkKmExUGVPpREBAAIXBJx5blnzQ7mcl21RQbz0VB-YxLz7LNb7ftHF-20NAcb9SmSHgaMChhWwA5bwtgHgsmhRfvbviDZO14wF1MXMSjpp4e3PYoqCLbet59zVSTfsroUYnQpsS_JQI9JgFpsHhhEWUEDIg9o3L4MafKGXaxd4-pV2ibTEyHeMXqlpAfGkmFKiqRk1eyX5E0nb-sGFxvhWAo9OQqwn_fKxwKERz2O1Q13KGkcYsxZFZyTlWzNuIPe1gCOxPJELudMJAfVitpVnaux5tvUGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیء ناشناخته نورانی دوباره بالای تهران دیده شد
🔹
یک شیء نورانی ناشناس شامگاه شب گذشته در آسمان تهران دیده شد و انتشار تصاویر آن در شبکه‌های اجتماعی، گمانه‌زنی‌هایی درباره ماهیت این شیء به راه انداخت.
🔹
پیگیری فارس از سازمان هواپیمایی کشوری درباره این مشاهده نشان می‌دهد که تاکنون پرواز مشخصی که بتوان آن را به این شیء نسبت داد، در رادارها مشاهده نشده و این سازمان دربارۀ ماهیت شیء نیز اظهارنظر مشخصی ندارد.
🖼
اما شاید برایتان جالب باشد که بدانید ۵۰ سال قبل هم اتفاق مشابهی در تهران رخ داده است
.
🔗
ماجرا را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463492" target="_blank">📅 20:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463491">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCQXRihJ6SJZ9g7T-Qfhv-uvo-VH4ngZqy_e1yOTbTH-zTgUwUn_WsyDbNLaw7bj8XKMWl2INbp_sSOc0hqwIY5XggGyw2vv8XhMLdIeBSGReZBHJY5Os5_NALt4Znwpy7JUAJslf9Yj5Jwtpb1m4F4_OPPCm5P5GqvqXOGo1M1-2V23JfDlBotPu5J6pwjyPeT7UrPPtT_JulaTi4RDYFtDSFYC9ff2mlh_isRqHdKI5_Ur40IB5EM0kiK2GKvFkxbPEdb4tcQOPHdZCUGp8L_GIY3UT9N5slbieLZyDX7d4fENEB6yk2WGwT7QmMhTQ0JgBSeP_a1LC3EEC6pPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: از هیچ کشوری باج‌خواهی نمی‌کنیم
🔹
سخنگوی کاخ کرملین: روسیه هیچ تهدیدی برای فرانسه یا دیگر کشورهای اروپایی محسوب نمی‌شود و مسکو قصد تهدید یا باج‌خواهی از هیچ کشوری را ندارد.
🔹
پسکوف گفت: پوتین بارها تأکید کرده که روسیه، فرانسه یا هیچ کشور دیگری در اروپا را تهدید نمی‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/463491" target="_blank">📅 20:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463490">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7616ee5118.mp4?token=BrZEMzDe74W9Rdd1TmnyBLGTEzzQeaUtTkV_XFZZeN--6kls_gquLwZPM7cu-8L0W_F1QcdVeGKkifcOjI4OxLcQbIlsU5En0ntSbw8CenCYWJGwi0gFYQ8dPupTgM9cJ1NYYnOX9tToQfUQi46X3bxld1tj4nBdsoT44weNH4Vry16xMUMYdun6m8sQLKw9qroib4qVfexjO4gJQ1mBlR2eBwYcGG7sbqCbuPqe884AbyG2G-z7uVPNqKJiHavL8rEBljvqVgDBXBsif2VoZC4Fw73QI9DTZNuPJhF7_WoDFjAabvre8gL2KWS5uxbY3gTvokIteaYrf1bD8agcEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7616ee5118.mp4?token=BrZEMzDe74W9Rdd1TmnyBLGTEzzQeaUtTkV_XFZZeN--6kls_gquLwZPM7cu-8L0W_F1QcdVeGKkifcOjI4OxLcQbIlsU5En0ntSbw8CenCYWJGwi0gFYQ8dPupTgM9cJ1NYYnOX9tToQfUQi46X3bxld1tj4nBdsoT44weNH4Vry16xMUMYdun6m8sQLKw9qroib4qVfexjO4gJQ1mBlR2eBwYcGG7sbqCbuPqe884AbyG2G-z7uVPNqKJiHavL8rEBljvqVgDBXBsif2VoZC4Fw73QI9DTZNuPJhF7_WoDFjAabvre8gL2KWS5uxbY3gTvokIteaYrf1bD8agcEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رواق کشوردوست به روایت قاب‌های تازه
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/463490" target="_blank">📅 20:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463489">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd6215379.mp4?token=nfEgdSx3cEM45OWETt3StMUoGASzOMi6U0BGefelSjOwFwuQofFycwilIPDYry-6bggXwT0ZwoYJACSJOJHL6K8esqRsd7t6Kt-vN1aAWyon5qF7tWPluAWe1nUI6QmhAmyxP2F6iTpOs_TD7PA7BnRejtuX_d7njqqxEgBoMMR_0E3LpNRItB7tVvAnuVzkXL2q7bFed9podri7n36DjaDSAOHewA9Vzjtn3AKs4gVmP71M5cfWD0gxvvK_u3CAHThS9Xlm9f1dcLGWusGE7ZkNC5KMQrk5zSKem4EbocGdatr5KWFsHKbKpXazBJ95TJqoAZ6WVWm0yhJRsoYhKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd6215379.mp4?token=nfEgdSx3cEM45OWETt3StMUoGASzOMi6U0BGefelSjOwFwuQofFycwilIPDYry-6bggXwT0ZwoYJACSJOJHL6K8esqRsd7t6Kt-vN1aAWyon5qF7tWPluAWe1nUI6QmhAmyxP2F6iTpOs_TD7PA7BnRejtuX_d7njqqxEgBoMMR_0E3LpNRItB7tVvAnuVzkXL2q7bFed9podri7n36DjaDSAOHewA9Vzjtn3AKs4gVmP71M5cfWD0gxvvK_u3CAHThS9Xlm9f1dcLGWusGE7ZkNC5KMQrk5zSKem4EbocGdatr5KWFsHKbKpXazBJ95TJqoAZ6WVWm0yhJRsoYhKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کالای غیرضروری جای کالای اساسی را در واردات گرفت
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/463489" target="_blank">📅 20:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463482">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZO8Klw0h2jxxlX8MXxxt5jt7vZptWjExuNB87v0fkrd1ldCrj9evW3PhyDccyFWFXKEGw6OaJKjZ0CKtzizYHbl33MWo66h5P_2sV01C_hYMoQ9JtjvwKiWQzsh7E0BSKt9b-0LZr285ypW-KryhN3948UoATd4-aa6dnQOnFq26F_O9mrPWYDGMkO5UGzUZsOQ8SaBRtfrR0UjfwshfwniNFKOeFHBUeFAXx82CaDH2grLoqN6kAY_s3Xiz7D-bHKj9LKtVsJ39YOMsb9WLgkUXv6Nwrk3V8Gh-54SWmaRVXVKNA3KQ0ttak2QgiQe7nLC_PEFXafPIeCvbK-LD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEooeMR24eqUOfrzwMri9QNDekMo_gncNFGnET7EvgdG4EXiLiwTTe9nVkP6wtuJ72aqJmAZgcPZ9aJc7kfNQJrmV9nfKaDZZs7hQf2xJ2uNAcweQV42_kpg7-mlBCgupwxN57InDpwPT_yTT5hJiGoCaMW6gOavYZliRO0YBk9ugnvhqZNW99xxG2R6aIpklM3Xn8lYRgP0O4m7A6054vKXCB7-RXpXJMg3BNx3syrNquF1waFJqNrc8i6gngQ4unBblNWnJ_ZNNEoHc3weg9WVaQpkMW_EyC0VFgFl05WSyZ0q5kYH-lXCImPO9YkK5yM9uwCi5PRfPf3Vw2mI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8v70L2S_lx1icxa0VCr7xewKxSG_mSbu60ZlzbHJwdMhFQ84RDUCBPWsk1fZq_0EWv1LTtPIQAI19AaVR9m0P-O8ooEKlIBN7mwuMaAFURD3IPfmVplaOzy2Hp1rYadsxvGiAafQV6cQlzQHmr-ny9oUufUsX7_zc5fqwaPlZqnfyk7lHbKC1NB5F6VrE6BYJhtqH3MZF6pDVxP5m3-_Uy32adrEoORYOGYEo67CHzyeNxq7IqeLHmnoDy3Lrqvh4xVkyptbE4XWzP-aEiggRrJSk7P_wI5JCy6RQV6aXMV3xWOZg4RC-1dTEG5NCCQNccyZj92it2YPPB-c14wPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNSrItI2ElqR9ouB8z2seD1_ps04j8FzM9QsSQ9XyIkEVCzaPBZt1Ebtx2yI2EHDdcijEkNNtxosjOyvG8iFNm8YG-nfC94xHKv6maHSF9Xe5FPdrO1uehEWYSO2w0MVtGeC1fD6kWOWDslQFcUoAIZ1kAje6c8eC2rb-I5txIF6ViBFQm-ZL7DRBuZUZGIBziudFaH5yvuLSTEv2TjQsjp-O9aAcEo6Enp9HfEZH1FVbb3CUuD1CUjAzVT0UHtypoaTYlDthXAmOYwoG0npjVcZ_4dRkJlrLYjM7xhQ4zKn5sPsAc0_gwcVy_LmCld-0oX0Bml3xnsGKZFJyd86xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DYZFluRJsZK-M8-z2CTaKYbMP2tibr_8TaFnKQbI4BIxOLQcNqCJ_f5WdVbY3vQNnXhiIOTcsczGhP1TD6-7H3KTNRzrooFxrhY53QKXu23iWgWhBTL6nhABcWgTlGYd5KYpIbCAkYEH7-i_nC6stsbENrsdRsj8kXJ_1XcG2IgkbLlgww3bSAcov7UqZWerp1OGez7iOjhGgDuyR8lFkBpF4lk49p5QMjGODZ9i-00Kw2lxewE5Mgp5lV-01MVOepHfbSMZYg-n64uIBHt1DcYkJk6InFnGCivvzPhYCIW1yKP8pjVzrzdg5V6gpa6dGvprO5dR9GKfmEiLY-XuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYzhqLAUmCky3KSrEJzf6kLUhpQ8QLJLG80msPvPqivK3H3QgAg6Uw3K0tuqrKErq0YP66J_IXVI4mY8zyuUtdQrI5WG0lvGlCulF7sNMy3fszRFYrlAIBRLkO1YjBOvM1zr7TCmH_Kgi_JP8l0hxtuZa6bAv9u0YCdBkHeUPhUx9ssMgY50b1vdG330qzQ69WT7DP-JU0UHTVfEvqDhRB_C4pCkn_QkFj42VoOStl9spT1zGuYknWk_NSAWVVWIPiwxvppe3Ahw1Z18bqvSGrXINWbN8K25AqIGcttc6LzTmJ5ej9lDK6a7WXW-4ayjFuGPEgCkQQpHbnJKXiKPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XS0eGNDX9CCrS22MZioWH0Ct9MYnwvEIdduvFY72hp1A5izYMv20DD9e2bBZuJwVyjCl6dPTrDxRkYm_lCWJEUzvUNTXcuOZPoHU3bi22jcaHHSQl5D9oBqY4wqKwmqpfMmHq-5Az1ku_e-lRhv2SuvLwX7L3hnlX-k4JYRNjGD2mWdKzhn2WLyt0PYWYCQSrGUDUlu5X4vBlXQwq2i0lKWyMClkH9nj_5ICmOtIPn9HnRUVKW5vIkzb04dSMUGI9xaRgFOOb3Us7KD1IcUgn_KTMCGk09M_lBy0wgCOcm60tObPo48z8uj7EH_O0dwpm5Ic-wixdKHTkcFK69rXkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اهتزاز پرچم عزا بر فراز گنبد حضرت معصومه(س)
◾️
در شب وفات حضرت فاطمه معصومه(س) پرچم گنبد حرم بانوی کرامت به رنگ مشکی درآمد.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/463482" target="_blank">📅 20:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463481">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAHFZJT5o0OBA10N2YboJnLYlZMRYiqEGX4zK74Cdr5ckhBn9MZ_iXh462nYtNXuZ0ywOLnR7_5NboYkoAyULsxlQ8AROF_-NPl1Dh4zSJ8k3sA6L-KkuNfp7zoMSbqnWpP6JZF0eXhqpZgqPJeWMOjZo_GFA_fTMIeZmOXwL9NAuR1VGiwr9h8FPXtdAcIpEo5IxRbNGNdZXmyUmPkHuiZWXPnepN6_9DZTAVcJ_nFg_7s-GmeZ24_VvMW-EJhdsehSpcr2gBGMF5t_VDhkF802zNd-A1sfwDWNLslX2TEnr2tSE3-5qlgfnTbN1KtOJGCe-4b5-i6arTLccEueIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
در آیین اهدای لوح به سکوی تامین مالی جمعی بانک شهر تاکید شد
✅
«شهرکراد»؛ راهکاری نوین برای تامین مالی بنگاه‌های کوچک
🔹
مدیرعامل کارگزاری بانک شهر از دریافت مجوز رسمی فعالیت سکوی تامین مالی جمعی «شهرکراد» از فرابورس ایران خبر داد و اعلام کرد که این سکو از سه ماه پیش فعالیت خود را با ظرفیت کامل آغاز کرده است.
🔴
به گزارش روابط عمومی بانک شهر، در آیین اهدای لوح به سکوی تامین مالی جمعی «شهرکراد» که با حضور مدیرعامل فرابورس ایران، علی محمد خانکی مدیر امور مالی و خزانه داری بانک شهر و ... برگزار شد، محمد گودرزی مدیرعامل کارگزاری بانک شهر با اشاره به چالش‌های فعلی اقتصاد کشور، گفت: کمبود سرمایه در گردش یکی از موانع اصلی پیش روی شرکت‌های کوچک و بنگاه‌های تولیدی است که این مسئله مشکلات جدی برای این واحدها ایجاد کرده است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/463481" target="_blank">📅 20:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463480">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e890df7bd2.mp4?token=likzL8kbyVVKTEBrNxOtsIX11_vsFqtvmkVNHvBCkw_oAiv0BRtm1RCb9NJnQ-8RwzWlI0LZn424xFR146r59REJBxol2RgJTxUG9PEVdnhArQNID6qMJISRGQWDLXCaTRcqpysDZPMkLWcIl32BRpVXD18XBOyV8WFMpyVQxlaksnKULjcKwnMcx0EaGmpr7qY6zjmAKTYej5gsVuKOfwQndaND25RgEZ3WoNt9rP6zqCuxx_p743S9N7smyRv_yFC9F-hJ3haKiZ6_svFIO1dS47MH3kXrhHIWdTeeYg5-DeUkQ_HIU2pX0mo7rDyI-MAs3OUUeJbOC8MXb-HRzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e890df7bd2.mp4?token=likzL8kbyVVKTEBrNxOtsIX11_vsFqtvmkVNHvBCkw_oAiv0BRtm1RCb9NJnQ-8RwzWlI0LZn424xFR146r59REJBxol2RgJTxUG9PEVdnhArQNID6qMJISRGQWDLXCaTRcqpysDZPMkLWcIl32BRpVXD18XBOyV8WFMpyVQxlaksnKULjcKwnMcx0EaGmpr7qY6zjmAKTYej5gsVuKOfwQndaND25RgEZ3WoNt9rP6zqCuxx_p743S9N7smyRv_yFC9F-hJ3haKiZ6_svFIO1dS47MH3kXrhHIWdTeeYg5-DeUkQ_HIU2pX0mo7rDyI-MAs3OUUeJbOC8MXb-HRzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📸
اجتماع بزرگ «امام زمانی‌ها»
🔺
همزمان با فرارسیدن میلاد باسعادت حضرت امام حسن عسکری(ع)، اجتماع بزرگ «امام زمانی‌ها» شامگاه یکشنبه ۲۹ شهریور ماه ۱۴۰۵ با حضور اقشار مختلف مردم، خانواده‌ها، عاشقان و منتظران حضرت ولی‌عصر(عج) در میدان راه‌آهن شهردارى منطقه ١١ برگزار شد.</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/463480" target="_blank">📅 20:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/463479" target="_blank">📅 20:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/943ee487e7.mp4?token=Cn61hj5tSISEHsSKSOiI0wkXZpqMVob662gMjgIe3ip2FEalNdNrQEpJPQC14ao1mSXMN-jBgl1ML4NxSiQCbRdrFNYYn1ZsGtofwIHYELq8piX7UG0G4gjMtOIEljd83NLjsl-0HiYVlzj1BNpgVlZbtKrbrmMhk5DyLorgg0VOoLUu3RmDh_lcIYCOrifO4-91onxHlVMvs8NRt-F6L-Dxtbfrh_GTq3atxnIv1Z-3TgSlZ4IW7OwmrjbBu7lsLyko0cdPh0wDFW5Bdumnds-n0_ZKsrDTgoY0LUrM2YdoIVy8V7sHVCKfVlohfoc5_gqK5QmPBYnE7Ezm-BFqYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/943ee487e7.mp4?token=Cn61hj5tSISEHsSKSOiI0wkXZpqMVob662gMjgIe3ip2FEalNdNrQEpJPQC14ao1mSXMN-jBgl1ML4NxSiQCbRdrFNYYn1ZsGtofwIHYELq8piX7UG0G4gjMtOIEljd83NLjsl-0HiYVlzj1BNpgVlZbtKrbrmMhk5DyLorgg0VOoLUu3RmDh_lcIYCOrifO4-91onxHlVMvs8NRt-F6L-Dxtbfrh_GTq3atxnIv1Z-3TgSlZ4IW7OwmrjbBu7lsLyko0cdPh0wDFW5Bdumnds-n0_ZKsrDTgoY0LUrM2YdoIVy8V7sHVCKfVlohfoc5_gqK5QmPBYnE7Ezm-BFqYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوفه‌ها پیش از پاییز به مدرسه رسیدند
@Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/463478" target="_blank">📅 20:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463476">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc03265dc.mp4?token=oTF14OwSlnsGwkv1ImWfQlIHctu4zHdYDbY5l0ztRZISjaL813Jh0gdN6wxuu0fxWG8Xe2PanP9VvXO_7EV06DONUR8y7-WCpee6usTndfHDepdkI1jqsTcMLC3p07kSHxblA0uTokkg9LvzdYYzSrkr48GGmZ2PMyfISnBwwLgdbaUmaaDN9xMj-lFlbOwUpHb8s9i8Y6qAQ5RylKCLPWVmdbvcBS_yw92jpWPvmKEeU_s_ouin0VJL5w-NIzJmmjXruFpWz8nd5KmxcrxFyl_X2ZRdBPFO8pId2_FtXeXmsLqT6be4R8teSJYIhrp3ylOSBJ1JhgfqRWxwp7sPwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc03265dc.mp4?token=oTF14OwSlnsGwkv1ImWfQlIHctu4zHdYDbY5l0ztRZISjaL813Jh0gdN6wxuu0fxWG8Xe2PanP9VvXO_7EV06DONUR8y7-WCpee6usTndfHDepdkI1jqsTcMLC3p07kSHxblA0uTokkg9LvzdYYzSrkr48GGmZ2PMyfISnBwwLgdbaUmaaDN9xMj-lFlbOwUpHb8s9i8Y6qAQ5RylKCLPWVmdbvcBS_yw92jpWPvmKEeU_s_ouin0VJL5w-NIzJmmjXruFpWz8nd5KmxcrxFyl_X2ZRdBPFO8pId2_FtXeXmsLqT6be4R8teSJYIhrp3ylOSBJ1JhgfqRWxwp7sPwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار و فرناز درپی مقصرنمایی ایران
🔹
یاشار سلطانی در میانه کلیپ افشاگرانه‌اش درباره تراستی‌ها، بدون اشاره به نقض‌های پیشین آمریکا، جریان سیاسی پایداری را عامل برهم‌خوردن تفاهم معرفی می‌کند.
🔹
این همان روایتی است که پیش‌تر نیز در گزارش فرناز فصیحی در نیویورک‌تایمز…</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/463476" target="_blank">📅 20:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463469">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxsACEu_yPf86ust_0_AhuauCic_288NJFfVudeMEvJTJTyV1UJpwk5Ka6ykI-nCYL9Ft8zDDHIbvmdQmop_5FRNRBplXjlwdbJsK5YOXR8kxo2vOb8ZtRMMIxImrcywaMz74wnaQuByyX1IQUMwhVl-H_FSkDN82Z-7Vf9HvgPRXnzZmNFWxj8PYTjanhMYu1UQvcUVoneXN0BsKDUJXIW-nxq01NVLuZ20EmdeWthSVvm4NMZB0egh_0L1yV95FDKf1DYHpg4UkR6eyX6f8RjHXhHJpqcwL8bZ0wszTljs-ISVs_SrbKP2jzMpF3Z3qLwcP3lQUqCtF4yy6Yi5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vf8qIKhGBfC3rS9A7J6EwtAKDuOpenF1KD77_eYWqwZ5rpFeMmthUe2iIdMgzizzl8mkCL9_JzGc3zV98Ca0FFUN4QhJvohT_a_JDngJ1FJ87fjaxP1H6FScFPzRQ4OMX9s-NYczRnUj3UNp5KCbmYbSR31e9AljI2j_9ka8i76Zb0lgZdmQBBl1j7VjMvehoK8_MilfZf5afE9psdEkNNnS7FEGiaEXwIE8WyvDCCBqwc8Nn91ekLvpJN33x6eKL4VgawiH5mv2x6jfvV61DH7MGSTUBUXFOLRlVGxrMtrgHuff--77p4VQDudNxn-sQLGSmcYnv6iYSW71N3P3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmLY1g274TKsZOKm6TzdTdMtOZUnaiD3NTjfgQ0RYEuzz1uU3hUt6S4OzSIOOIwQsDm3Mvavl4KWPOhvUe3ek7lwBd3_FarBOxt3-VrxooMeIfwKCifAjzpAWrahhPc-XIL39VqEeuBUZ9t2pJgMxfYKeejrIZK9NvMRQxRR1gg1JI7u1KqW2WIwZJEUYbB6y3z53TeRx647XMz7-HW4c9hipIkI7f_Eg5Stdrvv9UUoOB7QKI9kYujyg7hZbNgboHvsf3zg0SLCmmLUdgLEDddQoxBMxpV8Q66E2qWbz1ha6HshsbIwzoyLSuyBEgZpcuzE_MoltoFH9VhqtpMcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQ2e62uE0g9-cYZJTjgHIFJh5AfBIPzMQ4J3x0ceyLMvWQQpN-whDxZgg7ymaYmAYyvxG_mJcrGsxbDBsKn7vb-AmHFQb6nxbna4qyPu2MBtkmRA3PO0I2NGcxi8EZmexqNZl1PNYsaeOZ5xf_Te38CSV2KdT5PvhnKkaMx--t-RhJThjv9pzy5ZVpxFK2mXYPaFkbnBizX8EYQQps9GOATKWljjxcTB3J6nZ-M_wxOWVjslnUN_-e6Yu4Y6kauZG4-dvqVg9GZyBqiqaDK72-GvzSMAJNSwVjcPlcWFStJTxKJG2yHGfZAAylwK4Bb3Q8V-jZoM3EpP7BeRsVVXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuxk48Dv59Ne3MAI-8je82A1F8p0eNDc6BcG4TricCal2H4w-uO05CiCZ7EgYPbQlDJc9i3lOLld7VcE9CJxA_fbcNq2QVXNkJ9EinDvR8Ahh71P3YyAm_EoMECeHWiGeAvURmQNh5PDUCML6McVGeSg73uw_2wbngI-ymrGOqEDOH-S5ySimCMJD3l_GGv5LupZbbY-z0y2wiI4oCXbCTLAf4U8WmxXCt8_uDa5922eoGvuc3ayW4jrKQY9CzRktWyfrBkH-97vEFl1DAejCFRJzMCNWGLZIfHBhBbCGL0v9elNVDiUnUjayBxsTVSO-nHgBKQWpckSoAQG8S5_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uY3xz965nuZxWw-cxNjE_12MSnSnz3t2Nb-zscoL0VcEvOfDcSxidNL09UrZM4iIg9kWr0e8TJHRXjijuhPoe5jwiruefCFjQxbk2NiNupshhc-AKLBC4FM3ZDQefqRN8I0uF3kG5C8G03ekoS4k6U2XwpQBFAEm-sN5sKKLVv-1KbwzmvYqgTJtZaocuRYGzDCgMp5U2lWhuXSpVhQHi0_JGZkyMxfbQXh4C5eM7q-c24genqDIfH7xtYvtxbypWZMtGD_GaOgu77QmDilG_k43rOGWwMN0pssEhcgMTkDM20B1XZYQ_OPpIDh_qekEtFj0aHF8NGvN8QahW8UxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMKAZ28IS2Ylskjh5KhaLF2WCJTy_KRpa73lo7z3fapiOMQTRBceRbKEsm2Xbwq7ogCgcLUV03cS-rgOjCsVhLnT1S0_US7HlXOaqunySwRUwEcbmJqybCH0IUxAAB3Sc_R2cqmCwPOauflaNZe1s7PErBZp6epU9_-aJwmqpVfc2snGElLP4h3SiAdk9IsqA_Jd4DLJXqHEllwGJvc6JBLvGpLo61Hk74WWn7ld8_jjSihHAaR1n0TrTHjKPZbTHm9wfxUw1QPf34ktP11-nh0_um1yylXAEVALX8AsUyhF_w4nm6sej_gGcKUwu8uxMOi9k-sctXIquwPln2Hk7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور نیکزاد، نایب‌رئیس مجلس در خبرگزاری فارس
عکس
:
میثم نهاوندی
@farsimages</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/463469" target="_blank">📅 20:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463468">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6MzscNv0b06SCPL3P1xJ9vF15Z48OjR0qyFOC4HI35Ws2geido5a3LNJhTE0OB2udUfO0cI4RbIoAYiFWuvRycb-5loMAlCHtrLJ9LXXuP9R2UsYYVGW0N9l8-dObLnXTWkObSmmMcH7J6GLxvT7F2IPKtXvMychKGZHJzhPVWLzRCerkXWU2Gsx9M1ffGdIfk-kfGqx2yIXpD6LdzVfU3vyUEZ410e2jo8JhhwxlBzTbAVv7zhZTqolmWyULjSURyALYMKz2vPGZJpuV3G8ySKfAASKLbsM0zCFDqN70oM3nGhAz-BABe3U7Q8M92_21o-PMBDFfVxK5Ks2rtQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌آیت‌الله شبیری زنجانی دار فانی را وداع گفت
🔹
دفتر آیت‌الله شبیری زنجانی اعلام کرد: روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🔹
جزئیات مراسم تشییع و تدفین پیکر ایشان، متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/463468" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463467">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f717cb916.mp4?token=jAE8V8Au-LL7pn9m_PHDYPVye-1FkJ6nCGwqgORiOv6n6cllvuSCMVIqI8WKCIkuXAFjpCDZN_2MBvprHp78LN57npv1Mc-er7SL4KtBhRMXwsHTSoJta7qxy2QbQ2QGZyfplgrmQyKx2EGDI4YX6m6RcbNbSomfoeRpD8LrAnn7UMiB0cJG5dCgG2rKBbIhM4HVe9LGcbBwol5HI_6e2-MuIULp2SK9Ze5oRuLPq9fRhQwxkgMDSPY4X0FhRpeLtoz20gxNFEsLkRapALUsUgJZwVyrjkcAdaLAe_-2I-ZEs8uCLrLMHeG5Fk37p8bIXIWVapY5Aj2Cmzr7Ovo4nFLGV4nQe6SbjCHSTijg3VRqmJF6RyJClm6r64qGX3YMATAfzii1pgbSMzituPJwzSITPWJSkEK4qnzuCWTzPN63Ml7TAkzgDouv2l46xFHXHg1cCRvdNr4D7_mO9xSF6Rz54SWd-IOePVLydx6bcgfkycuBbd2u5avcr9qLjYWqPLuPOzRjg3MUg4bqVGdCg1fF0Xnk9hX6jXPN6UoCrUbZ6CPtu8yof0D2n64aWJX4JvtRAz79MPvmYypSYeuyb5CD0L1mmjFNpxcOIbe3DBV9EEuZ6_JjD_-PkROsgq0_4VKZjN900PDzxrw0cMgHoALChAJvozpf4eWbkuJkJtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f717cb916.mp4?token=jAE8V8Au-LL7pn9m_PHDYPVye-1FkJ6nCGwqgORiOv6n6cllvuSCMVIqI8WKCIkuXAFjpCDZN_2MBvprHp78LN57npv1Mc-er7SL4KtBhRMXwsHTSoJta7qxy2QbQ2QGZyfplgrmQyKx2EGDI4YX6m6RcbNbSomfoeRpD8LrAnn7UMiB0cJG5dCgG2rKBbIhM4HVe9LGcbBwol5HI_6e2-MuIULp2SK9Ze5oRuLPq9fRhQwxkgMDSPY4X0FhRpeLtoz20gxNFEsLkRapALUsUgJZwVyrjkcAdaLAe_-2I-ZEs8uCLrLMHeG5Fk37p8bIXIWVapY5Aj2Cmzr7Ovo4nFLGV4nQe6SbjCHSTijg3VRqmJF6RyJClm6r64qGX3YMATAfzii1pgbSMzituPJwzSITPWJSkEK4qnzuCWTzPN63Ml7TAkzgDouv2l46xFHXHg1cCRvdNr4D7_mO9xSF6Rz54SWd-IOePVLydx6bcgfkycuBbd2u5avcr9qLjYWqPLuPOzRjg3MUg4bqVGdCg1fF0Xnk9hX6jXPN6UoCrUbZ6CPtu8yof0D2n64aWJX4JvtRAz79MPvmYypSYeuyb5CD0L1mmjFNpxcOIbe3DBV9EEuZ6_JjD_-PkROsgq0_4VKZjN900PDzxrw0cMgHoALChAJvozpf4eWbkuJkJtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۲۰۵؛ بافقی‌های یزد در شب حماسه، پای عهد انقلاب ایستادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/463467" target="_blank">📅 20:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463466">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQIe6IiXHYxRPBcFXGAe8V1lK2UaVANFgWM3b6H3iJFN4e2la6eyTYZ_eBDV3nucTHMgW0MZ7g24yKUyRrYw4RcS7rj7tsdT-wz6SFjmR-fIiFMV40fi5r-YEklOsNh42RnHEMNhyVQspVcj0cF8REDmLIuKnvKpECPIHNrh1vzkgLV_uTfjCGucEtLchmeFjbmrgMgyvBSKLTkmQPcKhKmdpxQI4Ih_pCp4exoR0XeWmqk0j0UF8nIFmRtI9z7GmGsrTmpTPTxSZ2JagGH1ZzZAqPLqFnK_uzjC9YThU7ppgR6iHAaB8lhXY76PV6_rwwKmTgu5Y-Owf188PIDMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیروس ابراهیم‌زاده درگذشت
🔹
سیروس ابراهیم‌زاده بازیگر پیشکسوت سینما و تئاتر پس از تحمل یک دوره بیماری، دور از وطن درگذشت.
🔹
او در فیلم‌هایی همچون کمال‌الملک، هتل کارتن، شمعی در باد، مسافر ری، چهره، همسر، تحفه‌ها و مجسمه نقش آفرینی داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/463466" target="_blank">📅 20:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463465">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: دشمن سعودی استان‌های الجوف، تعز، صعده و مأرب را هدف قرار داد؛ این تجاوز گسترده
بدون پاسخ نخواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/463465" target="_blank">📅 20:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463464">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY_9bhLVpVx_llHytofOS2pg51pZ-wefon0J2zaHx80CHlUDBpZ6yTlY6LYnxsAiXWlkvsRXlrL0sRV69zyW61_Cp0xt6qOucshi2hXBxj0Vt7kIcimRpBYTnIvLm-h5DGiXkDjtdjrn-jfyPL0gjPt_C0gv98UMYYK-OjS9BwUyqOOrOBbonvlY0JNFWPWZgYlOUDyTyG9doUjd2l0HWsqYQPhj8kc_I3cOQ-LkHJGoDEq7P9R21JLAp-jPsFXIEi2wlS-ep01EuXApAvf15OtzAwluKjHqVi9RrlA9fgOnrp8_Yk7cxL9cZqIy6jHea_UdnUqFoRKrrnRVZqDQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت خارجه: هیئت حاکمۀ آمریکا نمی‌خواهد صدای حقیقت شنیده‌شود
🔹
بقایی: وقتی هیئت حاکمه‌ای حتی مانع از دسترسی رسانه‌های خود آمریکا به اطلاعات می‌شود و همزمان راه را بر خبرنگاران خارجی‌ از جمله تیم رسانه‌ای رییس‌جمهور ایران، که نمی‌خواهد صدایشان شنیده شود، می‌بندد، این کار مدیریت دسترسی نیست؛ بلکه به معنای تلاش برای مخفی کردن حقیقت و ادامه کارزار اطلاعات نادرست جعلی از طریق نقض حق دسترسی به اطلاعات است.
@Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/463464" target="_blank">📅 20:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463463">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38893fa310.mp4?token=SI4p6DtzWRH77BzhdV4JdtA3jQC4z0lWpXA5T3gG-nmWKT5mhf3FeWSvnRx6N0mklZcZDC1rBkebJfS9YJsmCoVsnIBC9a6fuwqDhNsEQe2z4PEGPHmEHSex-cKlO9CmlyhSss3JN7m-9N0WKDmtj4GXbL0A-9ghDFQHa0LYCNWAD7_ltPogir7CtkzDswoGglMxui8_Ng5_o5zSQJsG5QP2zw9aZ6YcVFpy6_VMGP1JhEWJAOMf59SPml9fy-ejvdiXzPeRtaJ0m2oTUCmZTfzDQEpWhUvMjRoo7-GZJ2bZmjoD4kvvrndbxVeCssWea8XReNQq5ecrsMiGUFwUIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38893fa310.mp4?token=SI4p6DtzWRH77BzhdV4JdtA3jQC4z0lWpXA5T3gG-nmWKT5mhf3FeWSvnRx6N0mklZcZDC1rBkebJfS9YJsmCoVsnIBC9a6fuwqDhNsEQe2z4PEGPHmEHSex-cKlO9CmlyhSss3JN7m-9N0WKDmtj4GXbL0A-9ghDFQHa0LYCNWAD7_ltPogir7CtkzDswoGglMxui8_Ng5_o5zSQJsG5QP2zw9aZ6YcVFpy6_VMGP1JhEWJAOMf59SPml9fy-ejvdiXzPeRtaJ0m2oTUCmZTfzDQEpWhUvMjRoo7-GZJ2bZmjoD4kvvrndbxVeCssWea8XReNQq5ecrsMiGUFwUIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌علیه عوامل برنامه «با ضیا» و مهمانان آن اعلام جرم شد
🔹
قوه‌قضائیه: دادستانی تهران علیه مجری، تهیه‌کننده و ۲ نفر از مهمانان برنامۀ اینترنتی «با ضیا» به‌دلیل طرح ادعاهای کذب اقتصادی و اظهارات غیرمستند اعلام جرم کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/463463" target="_blank">📅 20:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463462">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3TBwtT3CtCjmvJjL3-65sqwTIinfcikXE4d-MeZsU5HZ0gf1aRh3aHIKMjRXHz6mLOjw4xSGkEz3HxM4NwmENvYEMT7I_F8oVqQ4D2DIlpb1vdZcK1dyQbIwKOxk5MCj_j_V9zhff3vbYRaAPMIp0LfGSRso5VhvAIv64E51gU8-G-v_uA0kzdnS6Q0lqKigQw5aCRfz3kMRl5EdTHz3iDP7DPCBeMz101nlO5vuVNKBb0X2Np8-HgWooaN8mr3Uy6vU4UIi6ImOG0RtONkSlZR_Q-UID8PUmsrenhFH_pjyNqo8KdIMIWXhNBKS8pNMHuYP84qR2JBketaHQ8xxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سود میانجی‌گرها؛ عبور ال‌ان‌جی قطر به مقصد پاکستان از هرمز
🔹
بلومبرگ می‌گوید پاکستان مجوز عبور یک محمولهٔ دیگر ال‌ان‌جی از تنگهٔ هرمز را از ایران گرفته است.
🔹
در همین ماه یک محمولهٔ دیگر هم از قطر با مجوز ایران از تنگهٔ عبور کرده و به پاکستان رسیده بود.
🔹
این کشتی حامل ال‌ان‌جی قطر قرار است فردا به پایانهٔ واردات پاکستان برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/463462" target="_blank">📅 19:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463461">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng55FA6-JnqPGj2fzyWX8khLgY5CtGktDrg2ef7Qeam4SppKq_yXSVnoM23fAYdTaVOVx73Syew0BopasNvKLRZrzepeZTWFBx0Mzqi4JZQQKEUWMjMpg-V-aAS9vB3W8YACtMhkV7vqf-V-aSp4MfjHHivs-QI-Byll1uqmjkyC_3gDy0zk31S8BoEsJQFgcMaJGyfzU3KUoQ4FGdEX_8s5zh1uO3FTQcHlWQaUZlulrAKME6j3XdmQGBchigT6W1Z0z_5I2-Uw0LmsKPoLznHv1BUB8TSOUwq4vDBL2SU2EEgS9JnwiHn25o0txgoHXtJ1S2PboMkBUPjn7ppi4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عیادت نمایندگان رهبر معظم انقلاب از سیدعلی موسوی‌گرمارودی، چهرهٔ ماندگار شعر و ادبیات
🔹
غلامعلی حدادعادل و حسین محمدی به‌نمایندگی از رهبر انقلاب با حضور در محل بستری سیدعلی موسوی گرمارودی، هنرمند انقلابی و چهرهٔ ماندگار شعر و ادبیات کشور، از او عیادت کردند.…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/463461" target="_blank">📅 19:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463460">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mamrOb7dxuEpo5fEsZ_c8ZUm5VMNQWKK7MGe8KGFJ55M9wwQoGa3MB5hmil5bISn2mFjKbBUUU6bF-TT0bcuNLeg9OD3rlVduie7f4CUY0P6DsvkijGnx6nKp6OuF77wvpxySwppurB9h7zegMvuCPhlZDSV1h_7HuuCK3KpIYgccD7D-yx4MrpSfCqIwSDoaL3qMWdIKMFHeI2rgctOn4TlPtpnkkLGhIyNUUaCVkiCgmB9EQ4RGays44njPZzPXWL-Xe7ebbeCdOSwmeRTw8-9VGoyi6l71wrcr7vj3eSkU43y22gnInRdJ0EWgk0FHJzdI2dyXRXL-RH6GeTS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۰۷ ماینر در یک خانه در بندرعباس
🔹
مدیرعامل شرکت برق هرمزگان: ۱۰۷ دستگاه استخراج رمزارز غیرمجاز در یک واحد مسکونی در بندرعباس کشف و جمع‌آوری شد.
🔹
در صورت مشاهدۀ فعالیت‌های مشکوک مرتبط با استفاده غیرمجاز از برق برای استخراج رمزارز، موضوع را از طریق سامانهٔ پیامکی ۳۰۰۰۶۱۲۱ گزارش کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/463460" target="_blank">📅 19:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463459">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41cb84f9c.mp4?token=wBryn2PicvDd_JN7i8zmMAOmQ0_EJd2T0_lKqSBhcGzZVggzBjuvfybrIKQEV3ACyofw1qELB2yOYei0_w5t1-02rod7DI6h8OczmLvUVFgSxVhVy5K1KWeh6XC7V4AWfl4f5wpST2hLpay5sJbTx14Huz-gWTd7cZOGhpap05zkAkte7aQbeijPmbVLP-Z7yAxYDQYra4BwMnDkN0oi-bHMwKkodQwbrlaBu4Llo6J4T8L-vhTdZDdoM7FkAMe4aDgokyUr8DL7n0nmmztTIhPKM0tBX7WTE1OqIGnE3b1UUm02fLTC3eVTlH_d8Yzcs6xyFOi50yCMRSMM7d_AtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41cb84f9c.mp4?token=wBryn2PicvDd_JN7i8zmMAOmQ0_EJd2T0_lKqSBhcGzZVggzBjuvfybrIKQEV3ACyofw1qELB2yOYei0_w5t1-02rod7DI6h8OczmLvUVFgSxVhVy5K1KWeh6XC7V4AWfl4f5wpST2hLpay5sJbTx14Huz-gWTd7cZOGhpap05zkAkte7aQbeijPmbVLP-Z7yAxYDQYra4BwMnDkN0oi-bHMwKkodQwbrlaBu4Llo6J4T8L-vhTdZDdoM7FkAMe4aDgokyUr8DL7n0nmmztTIhPKM0tBX7WTE1OqIGnE3b1UUm02fLTC3eVTlH_d8Yzcs6xyFOi50yCMRSMM7d_AtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، دست‌به‌دامن زلنسکی برای کنترل بحران سوخت شد
🔹
با تداوم افزایش قیمت سوخت در آمریکا دونالد ترامپ، رئیس‌جمهور اوکراین را تحت فشار قرار داده تا حملات به پالایشگاه‌های روسیه را متوقف کند.
🔹
یک منبع آگاه به فایننشال‌تایمز گفته تمام تمرکز گفت‌وگوی روز یکشنبۀ‌…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/463459" target="_blank">📅 19:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463458">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgU15QRFLQGMbwA83dz5xNAVdYvwGyq9NOfcwCu_rZiARZi1H8rdjpMiVxsfXBJRTDPgMbQ4fiO4cR_1lvu4pBCxKhlNG472jlwxO44BX5anwTBIoYdv-xJIYEu5H-wdj164CMAqNaykd-s98eNL1f28RjCzAVyK2McDrgKUzv-9yvIUwc3eytmq-OQJPvIOO6cIGnR23K9dL3ToBrKzOMycK-Be938NQMwTnEms9nWJvIK78LfBVvJ5_MeZn1IITCGu0qubpb3D86YxI_WrZRtgbydC7xTyBedNRZiJINAwDw4fRX1kl-_4F2FkDCePIGxqH6kx6Z3MZzFnKYTQtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، دست‌به‌دامن زلنسکی برای کنترل بحران سوخت
شد
🔹
با تداوم افزایش قیمت سوخت در آمریکا دونالد ترامپ، رئیس‌جمهور اوکراین را تحت فشار قرار داده تا حملات به پالایشگاه‌های روسیه را متوقف کند.
🔹
یک منبع آگاه به فایننشال‌تایمز گفته تمام تمرکز گفت‌وگوی روز یکشنبۀ‌ ترامپ و زلنسکی بر مسئله عرضه گازوئیل روسیه متمرکز بود.
🔹
این منبع آگاه گفته ترامپ در این تماس از زلنسکی خواسته حملات به پالایشگاه‌های روسیه را متوقف کند، چرا که نگران است این حملات کمبود جهانی گازوئیل را تشدید کرده و قیمت‌ها را بالاتر ببرد.
🔹
یک مقام ارشد اوکراینی هم به فایننشال تایمز خبر داده که پیام اصلی رئیس‌جمهور آمریکا دربارهٔ «گازوئیل، گازوئیل... گازوئیل» بود و از زلنسکی می‌خواست به ارتش خود دستور دهد که حملاتش را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/463458" target="_blank">📅 19:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463457">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpWR2ueMbVuW8wd7NKDp6QD2Q645RMaJh8ITKHy8IH56F_6GFOwLHi0ctn2L0OqclRQs-Ic2IYECLIz2lU5Vc1hkk4LLyjZQeq-bSfSTjZslapfnavUNZVYPuThYHctCHHR8Psqwtn_wpQUydKIZEqSpbEv2TW5MJNF5Sd65wN4j_r8zR8DNWR_R4WbYzDx4ooZC8_U9ODqoPXsHgn_ptpWdmv5t3c0cqwyGLYwMatfnvsaYHc8mffb4F3HTZYGbHdMDu_YOG-_fCQUpIX8mV-81FFj4921Hk_CVWjRb9mOF8Pf2jwmI6MaQaFOBDAUCNH-rCGm3lPQ85IukUqLVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هرکس در حوزۀ هوش مصنوعی پیروز شود، پیروز است
🔹
ما الان از چین و همهٔ کشورهای دیگر جلوتر هستیم و من می‌خواهم همین‌طور باقی بمانیم. من نمی‌خواهم رشد چیزی را که از انقلاب صنعتی یا حتی خود اینترنت بزرگ‌تر خواهد بود، محدود کنم.
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/463457" target="_blank">📅 19:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463456">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d1e33680f.mp4?token=qgMvpUVbSRhyfV7RIQv4kxarOXknF2WOCBLc9FIEhQd-RYm_UvXFceSy95psxTIM55-harBWtr9a7cgUhzkgeYLVHq-49S6uwJ6QGrNZrulcgL8wSwcuA-WA_GOG5g_KH-XpHRemCj6Wsr_BAjNhP-iexLzSPz4PvO3Fr_-SQdinS1pFoysoInshnDTn_Nuf7DDD06nt42OkxUpk_eJeI_X0264vZ7nU0bUEhkErs1b88LDheeQLi6RhqGYDooNDp7uGNnJ2KFqpMigI4DpqM2b3IsXlKs109Unc9hKUw7Oc3UlJ2cC8-7o48-R4tRhyxhHdAAUyPIGAFeJWjkGYeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d1e33680f.mp4?token=qgMvpUVbSRhyfV7RIQv4kxarOXknF2WOCBLc9FIEhQd-RYm_UvXFceSy95psxTIM55-harBWtr9a7cgUhzkgeYLVHq-49S6uwJ6QGrNZrulcgL8wSwcuA-WA_GOG5g_KH-XpHRemCj6Wsr_BAjNhP-iexLzSPz4PvO3Fr_-SQdinS1pFoysoInshnDTn_Nuf7DDD06nt42OkxUpk_eJeI_X0264vZ7nU0bUEhkErs1b88LDheeQLi6RhqGYDooNDp7uGNnJ2KFqpMigI4DpqM2b3IsXlKs109Unc9hKUw7Oc3UlJ2cC8-7o48-R4tRhyxhHdAAUyPIGAFeJWjkGYeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سازمان غذاودارو: کارهای واردات ۲.۸ میلیون دُز واکسن آنفلوآنزا انجام شده و مردم باید چند روزی صبر کنند تا وارد کشور می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/463456" target="_blank">📅 19:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463455">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46267a6b76.mp4?token=Cbv1jPo1rl4ByuVWZje_QS2MtEO61hS06tHpFbshei9gETqJxS7tr-iL2r2y7BWi_SzmpGzZx98eHb6id5QSZdIbu6hv0qTlidiQDGtyYrjAfPDcrVX-A8Gk2kq96sv4yOAk9QSZYPuGpe_jFol15rS6Ope9TsrXc_QiIKTKljnyQ5S1YGG8gBAc53KZIFTLyOyaBKCX2A8sDAvujrLopKozyQsnUsxQbRhgVUCbExG2o-oTrNLDANf1rjk2FWMVtqLEM45t9xwivGyUB6clnmgM44EgoKGbc58zqOzTHrjOWL-w_78mGMyua42_6O-UXkKoTp3vJTST9if_AY4-hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46267a6b76.mp4?token=Cbv1jPo1rl4ByuVWZje_QS2MtEO61hS06tHpFbshei9gETqJxS7tr-iL2r2y7BWi_SzmpGzZx98eHb6id5QSZdIbu6hv0qTlidiQDGtyYrjAfPDcrVX-A8Gk2kq96sv4yOAk9QSZYPuGpe_jFol15rS6Ope9TsrXc_QiIKTKljnyQ5S1YGG8gBAc53KZIFTLyOyaBKCX2A8sDAvujrLopKozyQsnUsxQbRhgVUCbExG2o-oTrNLDANf1rjk2FWMVtqLEM45t9xwivGyUB6clnmgM44EgoKGbc58zqOzTHrjOWL-w_78mGMyua42_6O-UXkKoTp3vJTST9if_AY4-hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر بهداشت: کمبودی در واکسن‌های ضروری نداریم
🔹
هیچ کمبودی در واکسن‌های موردنیاز عموم مردم، به‌ویژه کودکان، وجود ندارد.
🔹
با وجود جنگ و تحریم و محاصره، واکسن‌های ضروری تأمین شده‌اند.
🔹
واکسن‌های فصلی مانند آنفلوآنزا نیز به میزان کافی تهیه خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/463455" target="_blank">📅 19:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463453">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff46b68e7e.mp4?token=Jrc118poIS_pbbQ31Oj8RQHERzL1d4c4qrkG-DJ2L_W8r7_hdNLyUlSNK7hp-sQO0zR_nr2Cd1CGtBU-hARDpqc-MEXiEV2djI5WR-GRZyjsShwGf7T3aHQ4kCuU6b8kHPTAxNzZ_E8C-kVjF-pwJCPtuDh71rC7NZgOy7keAcBZorvMLVe_YjVlD5xp47olCG_LeXZ-oOj2FIibDGGw2ldg4JI4psMjU4dr0RUiGK6ASwlsyEzkK0wk8aCuTysXEU9tX48nFdNcDg1-3WEDRtTw7cIB3xSoto-oIZBuUepW4JhV47wHe7PHFbgMXowDZQYfcg-By9gHbCycoAXShA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff46b68e7e.mp4?token=Jrc118poIS_pbbQ31Oj8RQHERzL1d4c4qrkG-DJ2L_W8r7_hdNLyUlSNK7hp-sQO0zR_nr2Cd1CGtBU-hARDpqc-MEXiEV2djI5WR-GRZyjsShwGf7T3aHQ4kCuU6b8kHPTAxNzZ_E8C-kVjF-pwJCPtuDh71rC7NZgOy7keAcBZorvMLVe_YjVlD5xp47olCG_LeXZ-oOj2FIibDGGw2ldg4JI4psMjU4dr0RUiGK6ASwlsyEzkK0wk8aCuTysXEU9tX48nFdNcDg1-3WEDRtTw7cIB3xSoto-oIZBuUepW4JhV47wHe7PHFbgMXowDZQYfcg-By9gHbCycoAXShA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خواهر سلطان در عالم کار سلطان می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/463453" target="_blank">📅 19:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463452">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f999a366.mp4?token=S5-oZLoLdK-F6d4h5bka_jp9JQCQmnRsfk89swTz5syIJUdtrCKovonzIfxbMIzcJ8xSrIHHm86v1u7jUwzFGmBDl184oTvOKnT8Zf9e8MtCga-QX8Dx6n21-Nm2WUJlYFLnNT9uReacbw-YTPoRXjCdDSGYJFrrzhilAZh5Lwfi4P_lBkiIvlpT_ckUQpycC57lh3veMzHMH0PMBVaGU8sqFATfi8AciQph9zNMhmP9TrqkBtTYaa9zZ7LOY0aTt84nwVkUpeW48hjhAEkitXVzIJvPZyFEJEo0ZLt3Dy7WqNDhsccsHpQXr7fjotXpw_ZzXOcDFdW1TTGdXJEw-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f999a366.mp4?token=S5-oZLoLdK-F6d4h5bka_jp9JQCQmnRsfk89swTz5syIJUdtrCKovonzIfxbMIzcJ8xSrIHHm86v1u7jUwzFGmBDl184oTvOKnT8Zf9e8MtCga-QX8Dx6n21-Nm2WUJlYFLnNT9uReacbw-YTPoRXjCdDSGYJFrrzhilAZh5Lwfi4P_lBkiIvlpT_ckUQpycC57lh3veMzHMH0PMBVaGU8sqFATfi8AciQph9zNMhmP9TrqkBtTYaa9zZ7LOY0aTt84nwVkUpeW48hjhAEkitXVzIJvPZyFEJEo0ZLt3Dy7WqNDhsccsHpQXr7fjotXpw_ZzXOcDFdW1TTGdXJEw-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از پیام و پیگیری رهبر معظم انقلاب دربارۀ جان‌فدا  @Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/463452" target="_blank">📅 19:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463451">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNf5aqKUv1jmwMke71iSzOXCHi2zqrIG8j9rH33W_EZLzIOB6pHeqpBeMSi0_KnIMbw7Sux4ExLzxLcVwCSEwM7nHg29z7LfUqTtOTtyK5oscPcuVjWco1JkE_cQiHAZ2S1T9331L8WCI1cEyR4kuCWRI-qNC6vdn-GMANL3rIjDtsayWii4Vro7jxENykClbvmpNZ5uO86tJ1HTZjzCdhQtcbnvGXkL4Qjx4SDj4_Lyq_GHEWMX4WTLpRVc-UiPLtz2KC8uFEkgWNW_I-SBpY9az59WbuIZMumkcXpgbhA_tE57eTgpYH-LS_HrQddcU2v6arI24aO7P6cgkkOwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز زبان فرانسه یا محل اجرای پروژه‌های ضدایرانی!
🔹
مرکز زبان فرانسه تهران موسوم به CLF که امروز با دستور قضایی دادستانی تهران پلمب شده، مرکزی وابسته به ساختار فرهنگی فرانسه است که مدعی‌ست در تهران در حوزه آموزش زبان فرانسه، برگزاری آزمون‌های رسمی TCF و DELF/DALF،…</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/463451" target="_blank">📅 19:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463449">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d86b1053.mp4?token=XEpvYEbd_5HfelZ8C07o-RORViwko_Exd6_MqFzKzRB55fUlQVKrFwAhEUKwsOeNN4q6yr98oyWM8K37FdB17n-j70MY_vO-eU3HB4clrvVu8ZgnKfEerrWbHwdtc9Pqc-e3oKSCwioCqy1QmTonVWVQWFc2YWxVjprxnKVp1mdhHYUj2YLj08lFSdFCEwFyEz5d_oT1YcsLO-ahkVnUE9TdQ8SypJVApwOt5JQ6ROkhuXRYxvfZq56V5X0aBHnXYSVjgbb2DsrMNqsjs6I9zZm9z7Mb0cn4391LQhQiJRPgw6Wo4Or8fvSU7VdA7VbW9I5O3HXbMTvZxD8w1Dkezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d86b1053.mp4?token=XEpvYEbd_5HfelZ8C07o-RORViwko_Exd6_MqFzKzRB55fUlQVKrFwAhEUKwsOeNN4q6yr98oyWM8K37FdB17n-j70MY_vO-eU3HB4clrvVu8ZgnKfEerrWbHwdtc9Pqc-e3oKSCwioCqy1QmTonVWVQWFc2YWxVjprxnKVp1mdhHYUj2YLj08lFSdFCEwFyEz5d_oT1YcsLO-ahkVnUE9TdQ8SypJVApwOt5JQ6ROkhuXRYxvfZq56V5X0aBHnXYSVjgbb2DsrMNqsjs6I9zZm9z7Mb0cn4391LQhQiJRPgw6Wo4Or8fvSU7VdA7VbW9I5O3HXbMTvZxD8w1Dkezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از حضور جدی مردم در کف میدان از زبان سخنگوی ستاد مردمی جان‌فدا  @Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/463449" target="_blank">📅 19:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463447">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e92902081.mp4?token=dLl-cGeqSQyvAeAC2rYEl2cA20s2x0ixEQRL7w3MOibDWmrRJHoROXdANhGu4YkmEhl19HOfRImaQs8ybID8w0mMjro-9cXfwBcahJlxXRil8ETp7iAv2LaRir0wdKKBkWmOEUMtOu19RUhhkHUfU0cw-94j9rOO5Knkdbj4qJF2VFbmvbQQ1rfkPOi98uBZuZQybhJVio7WHrMfdtVgUJcNBhjXsKdZCl7OfQAmzUcQKQPzt2EafavW_8Y8Mb2lSvndMbd7TdhP9CTsd5lYl77Py9N_qJHIQj4spsdQAXRGdPAdm4JiagEEXzM135gj653CaqtgkIxc7daq_2cncA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e92902081.mp4?token=dLl-cGeqSQyvAeAC2rYEl2cA20s2x0ixEQRL7w3MOibDWmrRJHoROXdANhGu4YkmEhl19HOfRImaQs8ybID8w0mMjro-9cXfwBcahJlxXRil8ETp7iAv2LaRir0wdKKBkWmOEUMtOu19RUhhkHUfU0cw-94j9rOO5Knkdbj4qJF2VFbmvbQQ1rfkPOi98uBZuZQybhJVio7WHrMfdtVgUJcNBhjXsKdZCl7OfQAmzUcQKQPzt2EafavW_8Y8Mb2lSvndMbd7TdhP9CTsd5lYl77Py9N_qJHIQj4spsdQAXRGdPAdm4JiagEEXzM135gj653CaqtgkIxc7daq_2cncA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای ترامپ: خطوط لوله در سراسر خاورمیانه درحال احداث است تا دیگر نیازی به عبور از تنگهٔ هرمز نباشد.
🔸
ترامپ تا پیش از این مدعی بود کنترل تنگهٔ هرمز در اختیار آمریکاست. @Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/463447" target="_blank">📅 18:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463446">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd66c8779.mp4?token=qVmaIFKD2hDGrMKqiip8LGkW0mA6jd_Aa7Cug1Ns84ptyHviKEU-xrGAzbe73wGyI4bjjxUzKOshFPilxTaSzCMl7Ny4OCo8E8hnz_cjS4mumpdwj6W3fckt6PAVlYAzgeHXolgflOOvJ5ECH8akD-4OxKI58Yv4idTa545o-nmBqB6wzDE7d74dXrcp6WXn8JV9q1UIfCBmDwYwbmP-WZAhD6atB7rrlnL872UH2cMgF6AYtkg15p59hL1UkJqi0r30uLIhawXs6eKYL43my6c_oxNsKx6jIfjsvAlLA_decq37BlwVaF2R85hY95_mI2wjrnOWf_ooPbw3GCcnIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd66c8779.mp4?token=qVmaIFKD2hDGrMKqiip8LGkW0mA6jd_Aa7Cug1Ns84ptyHviKEU-xrGAzbe73wGyI4bjjxUzKOshFPilxTaSzCMl7Ny4OCo8E8hnz_cjS4mumpdwj6W3fckt6PAVlYAzgeHXolgflOOvJ5ECH8akD-4OxKI58Yv4idTa545o-nmBqB6wzDE7d74dXrcp6WXn8JV9q1UIfCBmDwYwbmP-WZAhD6atB7rrlnL872UH2cMgF6AYtkg15p59hL1UkJqi0r30uLIhawXs6eKYL43my6c_oxNsKx6jIfjsvAlLA_decq37BlwVaF2R85hY95_mI2wjrnOWf_ooPbw3GCcnIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت سخنگوی ستاد مردمی جان‌فدا از حضور داوطلبانۀ پیرزنی با واکر برای دفاع از وطنش  @Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/463446" target="_blank">📅 18:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463445">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9585b17f3e.mp4?token=K6sDIt4iVlLv13fOm9M7e9J9covg8Lf14huolVsKj5pkhdG4mwLqlcfw8pDA6_OPF4lZ4ZqiFdfNpClHdg335zmDFS-q3ZukivW2dd69k24aVXvbjcdRxIiGrAwfV1ZVBJ254OFjAldxZU5ZXYO83iwFS3nM255KPXyvNB5HtdlLwdevHT9YZHUH1sjTxeh-sYFYAeR2s3_EDYX3-gysUign6kTaeSrTuqxTcg2vi9FgCadJwREr4F3mkCYeXh7EKfB1gaicL_Nwxa8zPDyZe8Ek8j1EVkUsuv3U8R2udMrEvL3VB__QA996M_NOXwvGCbV0reea5yLcc2ApDHgeRABWl6cZyQ88n9YoEeGxQH0rDZgV3_YjHl_sarCEss3U4Q9YwPODLJiIeYigCvLNIRlGHe91cXEPRWlX5j_XyEgQGwT7izCRUDiEFjx1QyfuJCZMaEZVO6whoSCqVkUYdIQPT55fR1HnuelHNME--5BJawNBosh3N_s8fUOLFGi33FgOyxRAWdecTNZvLS62CAy43f2Oc13BhKx_dcp2mjupiAjyQXnB9pTzIsm8MLXE2Yeu0oKg1kV2OhSIjX2ndVJmlVaBMue1tAKV_MGInm2sU8qoOtE6T4G4dSemLCYFOgWe_WjiOFI3o9XrOs_VsKtVm8xcVxeCZLPb3ql_VZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9585b17f3e.mp4?token=K6sDIt4iVlLv13fOm9M7e9J9covg8Lf14huolVsKj5pkhdG4mwLqlcfw8pDA6_OPF4lZ4ZqiFdfNpClHdg335zmDFS-q3ZukivW2dd69k24aVXvbjcdRxIiGrAwfV1ZVBJ254OFjAldxZU5ZXYO83iwFS3nM255KPXyvNB5HtdlLwdevHT9YZHUH1sjTxeh-sYFYAeR2s3_EDYX3-gysUign6kTaeSrTuqxTcg2vi9FgCadJwREr4F3mkCYeXh7EKfB1gaicL_Nwxa8zPDyZe8Ek8j1EVkUsuv3U8R2udMrEvL3VB__QA996M_NOXwvGCbV0reea5yLcc2ApDHgeRABWl6cZyQ88n9YoEeGxQH0rDZgV3_YjHl_sarCEss3U4Q9YwPODLJiIeYigCvLNIRlGHe91cXEPRWlX5j_XyEgQGwT7izCRUDiEFjx1QyfuJCZMaEZVO6whoSCqVkUYdIQPT55fR1HnuelHNME--5BJawNBosh3N_s8fUOLFGi33FgOyxRAWdecTNZvLS62CAy43f2Oc13BhKx_dcp2mjupiAjyQXnB9pTzIsm8MLXE2Yeu0oKg1kV2OhSIjX2ndVJmlVaBMue1tAKV_MGInm2sU8qoOtE6T4G4dSemLCYFOgWe_WjiOFI3o9XrOs_VsKtVm8xcVxeCZLPb3ql_VZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
جان تازه در رگ‌های فلک‌الدین خرم‌آباد
@Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/463445" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463444">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzuZzoLGXWAVD1Q40d2wiPZh6blIx5S1nIV_j2Q4ffIrAHQul8nt5BgRbTYR8rHZhr7O_bbFDke7_WuZx1McrUzETNvmKE1lOuZKyfNWjHFhcarAKjQR7hxbPYFueFgNwpwXP5CboNJgk1M55wq6QaQZIwgssAW2YLBKMPcqQJNrAL-UyaBNCUy0PRd5v8nvtQSj1po3DXpsZ_cVNbp3GN9fjsvW-_dPrMdf_UTmanlH-spSFahCaQRRen63dNVMlDezFKdFEcdjBxawqmRZL-EfxZiSo71aI1XsnX8OSeYPnOMhVQG3ty7sA-Zwovv454uvQpVqW6GDLCje7_p9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حضور بانک کشاورزی در IRAN AI 2026؛  گامی در مسیر توسعه بانکداری هوشمند
🔻
کنفرانس و نمایشگاه «کاربرد هوش مصنوعی در صنایع و کسب‌وکارها» (IRAN AI 2026) با مشارکت بانک کشاورزی و به میزبانی دانشگاه صنعتی شریف؛ با حضور مدیران ارشد، متخصصان، پژوهشگران، شرکت‌های دانش‌بنیان، استارتاپ‌ها و فعالان حوزه فناوری آغاز به کار کرد.
🔻
مشارکت بانک کشاورزی در این رویداد، گامی در جهت تعامل با زیست‌بوم نوآوری کشور و بهره‌گیری از ظرفیت‌های هوش مصنوعی برای شتاب‌بخشی به تحول دیجیتال و توسعه بانکداری هوشمند به شمار می‌رود.
🔻
این رویداد تخصصی روزهای ۳۰ و ۳۱ شهریورماه در دانشگاه صنعتی شریف برگزار می‌شود.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/463444" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463443">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/463443" target="_blank">📅 18:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463442">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg9eN4oUGzOffFQWDrYkrQtl2SPJwm6AQ2F3gIYz6xLn_ZdBwUQ0_YEwVm0c3nyRlLgwvKA-2T1UUriFNz6YZMmC9Lwm2Fhg5D3w8id2NJ_bHfROPGYXvu8yzykk4g4mHgjWg4OnWtGrOT822xGqUtTh_PdkQ1r6xZX6fIjp2YuS83zY8TYaOk8uHpWPA98_n8F2EPXbI-m4DXllXzthiHM16zweN9uuW4JpH9spzli9qDFlsIHP6EBGDEmwylN4s7Ih9j3ilYvmNCRcZZa7siyr2Ad-eCV8G79d44VOw-d49WturPF2p-nNRc1BabbTrljUFZCMPgqDAgA6o3BuEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان به دنبال حذف ایران از جام ملت‌ها
🔹
گفته می‌شود برخی از کشورهای منطقه با هدایت عربستان در تلاش هستند که با فشار به فیفا، فوتبال ایران را در آستانۀ جام ملت‌های آسیا تعلیق کنند؛ این یعنی احتمال حذف تیم ملی از جام ملت‌ها وجود دارد.
🔹
افراد مطلع بر این باورند که این پروژه شبیه پروژه‌ای است که برای فوتبال روسیه در محافل بین‌المللی رقم خورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/463442" target="_blank">📅 18:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463441">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: در هر مرحله‌ای از تنش‌افزایی صهیونیست‌ها علیه ملت فلسطین، با قدرتی حتی بیشتر از آنچه در طوفان‌الاقصی نشان دادیم، در کنار فلسطین خواهیم بود. @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/463441" target="_blank">📅 18:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463440">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: تمام تلاش رژیم سعودی در این برهه، وارد‌کردن ترکیه و پاکستان به جنگ و آوردن تکفیری‌ها از سوريه است
🔹
ما به ترکیه و پاکستان توصیه می‌کنیم خود را آلودهٔ منافع سیاسی و مالی بادآورده از سوی دشمن سعودی نکنند.
🔹
دشمن سعودی با مقدسات کاسبی می‌کند؛…</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/463440" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463434">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: رژیم سعودی مکه را اشغال کرده؛ ما از آن‌ها به مکه وفادارتریم
🔹
رژیم سعودی بیش از هر طرف دیگری از بزرگداشت شعائر الهی فاصله دارد؛ بلکه آن‌ها را شرک می‌داند و از زمان اشغال مکه مکرمه، مرتکب فجیع‌ترین جنایت‌ها شده است.
🔹
مردم باید جنایت‌ها…</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/463434" target="_blank">📅 18:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463433">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: گرفتاری‌های منطقه‌ای، دست‌وپای آمریکا و اسرائیل را برای همراهی با عربستان بسته است
🔹
کارشناسان آمریکایی و صهیونیست، دوشادوش دشمن سعودی درحال همکاری و فعالیت هستند.
🔹
ضربات کاری و ایستادگی مؤثر یمن باعث شده تا دشمن سعودی تلاش کند پای آمریکا…</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/463433" target="_blank">📅 18:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463432">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: رژیم سعودی می‌خواهد ترکیه و پاکستان را هم وارد جنگ با یمن کند و شب و روز دست به دامن آن‌ها می‌شود
🔸
حملات هوایی عربستان تا دیروز از مرز ۷۶۰ حمله گذشت؛ اگر حتی همین تعداد حمله به پاکستان یا ترکیه شده بود، جنجال و بحران بزرگی به‌پا نمی‌شد؟…</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/463432" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463431">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avcd0EiPVx9SFmuw8gNYBuqCslCtQSOJILYkf2x5dwdR4xYM24ax0cNhebiYCunywL6wwBit4IXzV_RljOEf2g69SbVsw_WNSV9FBFMvwKucnl9u-rq1axReH_pCmAg8F21YR_89HSd2go7eCYcXX__pXht6nOaCIQUfcSpLjxh2dYDo1756MwpsQdGisWP9g2a3F6fE61zsDJNZDAa-dvQqMTQIgkrA6k_54y1meOPTbVZzLZ968PpOkTtp2Ab8484Wwve---QPAYZaLmNRPxEKWfgUwlID6r8v-dH0Ik8DYssofwrMVT3p1-SwHkVI3DVxYw02Vo2t8l5MQqsrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای کشتی حمل گاز در تنگۀ هرمز
🔹
سازمان تجارت دریایی انگلیس: یک تانکر حامل گاز مایع درحال خروج از مسیر جنوبی تنگۀ هرمز، هدف اصابت قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/463431" target="_blank">📅 18:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463430">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: آیا ترکیه یا پاکستان می‌پذیرند که عربستان در تمام سیاست‌هایشان دخالت کند؟ آیا کشورهای حوزهٔ خلیج فارس چنین چیزی را می‌پذیرند؟
🔹
دشمن سعودی می‌خواهد تنها مرجع تعیین مسئولان در کشور ما باشد؛ تا جایی که هرکس توسط عربستان منصوب نشود، هیچ مشروعیتی…</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/463430" target="_blank">📅 18:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463429">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🎥
درخواست دختران میناب از وزیر آموزش‌و‌پرورش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/463429" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463428">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: کسانی‌که ایستادگی ما در برابر تجاوز و محاصرهٔ سعودی‌ها را زیاده‌خواهی می‌دانند، خودشان هرگز نمی‌پذیرند که عربستان فرودگاه‌هایشان را ببندد و مانع سفر شهروندانشان شود. @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/463428" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463427">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌ روایت رهبر انصارالله از همکاری سعودی‌ها با صهیونیست‌ها
🔹
رهبر انصارالله: رژیم سعودی فرودگاه‌های خود را در اختیار هواپیماهای شناسایی صهیونیست‌ها قرار داد تا از آن‌جا به سمت یمن پرواز کنند.
🔹
هنگام حملات ما به اسرائیل، رژیم سعودی تمام تلاش خود را برای رهگیری…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/463427" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb0b4a106.mp4?token=AHb6iWsgNO3xrPgrZpv4irqy0TZk7KE9Le12BLl47AuZ4A1p9fwzxOSl3dZwzaj_SnQSGtD6FnkbDbbbrn9TVRNlY-i-cWV2vvbMu6Jt7uQjcnB58TMai9JdwOaIn0mWZOUzs89iVko8VwFT_MXYCDtQbrOIF1NMzd7MFnLL8GTc3zIk7Dd6USdt9VyDRONugwfULip1zKhhnhcxNJNTahG9qQGfpiTFnO-dVXlGDFUuiZmwFXsh02Utoj7bwZPtCKa5Q8aCvxQqKVqQb8MSPLPglSzefzvtoftYjEdcLJ7aYFIMsxuGtf4-hwBnBl_-7xutr-bNQDqIbhtENEzaUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb0b4a106.mp4?token=AHb6iWsgNO3xrPgrZpv4irqy0TZk7KE9Le12BLl47AuZ4A1p9fwzxOSl3dZwzaj_SnQSGtD6FnkbDbbbrn9TVRNlY-i-cWV2vvbMu6Jt7uQjcnB58TMai9JdwOaIn0mWZOUzs89iVko8VwFT_MXYCDtQbrOIF1NMzd7MFnLL8GTc3zIk7Dd6USdt9VyDRONugwfULip1zKhhnhcxNJNTahG9qQGfpiTFnO-dVXlGDFUuiZmwFXsh02Utoj7bwZPtCKa5Q8aCvxQqKVqQb8MSPLPglSzefzvtoftYjEdcLJ7aYFIMsxuGtf4-hwBnBl_-7xutr-bNQDqIbhtENEzaUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد، نایب‌رئیس مجلس امروز مهمان خبرگزاری فارس بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/463425" target="_blank">📅 17:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
رهبر انصارالله: کشورهایی که برای تأسیسات نفتی عربستان اشک تمساح می‌ریزند، حاضر نیستند یک روز در شرایط محاصرهٔ یمن زندگی کنند!  @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/463424" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03dc3f3612.mp4?token=oTvmSKAvFSWf_-f5QcAdFeuYK-D6FSp5vgB9baKFNyMdpNAtyd70rABxvLEYRAm0ux1PuklYDhKjROAnMa-UqXc5op8JIC1KdrgQ_7X7ZXTkhE1chGnTjmx9n8DCdGSji4I57zaE1HLVsFOvGKfh71hKtbkdJ8YjNFSG2_3ksrBh8Cg0Z6rMlt8lQ-k7CH0xPxHFi1XKnSIMZ8C8ld8dzF-SfYmsod9E-K4E69gqD1gPBfo7cTilGmgvlSgJn8jzgfNP7Y6t5HDdY9NvG8tWdfVAJh74giF3eK3SBClNMSAWtQspmIG2R4gEVvqgqIVg-e8A--eKOfIS6FssInrYD2KBOJs7vqO-W3V8VVEOnmnT7uJnLMp6DTl0945s7H-RhvidoKxQ1bxNnHjSHcUahDApMXwxx1dkBuy9IIrsmiERCKg1VUWzzIWGT8bQEHTwdvzm29_jseiDr7Vo4QL5TO0FizKowpg3GeH57Ef1yfoOXxNrsQ_TtK7y00mvdonM3j0_BsUObMqoFLk1mz4LmshPcm1EyVhxv_FT3HDeoDjF99W1fNJdcCmURnJMgjU-dGZifiP-YMeWzssphUtdaJoZY7p4AWYyl01JvW0jJX5JK2CAKMnNlHTLu2TPvZonTt6KbXT8zvXNKFFCZzhjx2Q7gBBC9UVgVlUWt5VxxBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03dc3f3612.mp4?token=oTvmSKAvFSWf_-f5QcAdFeuYK-D6FSp5vgB9baKFNyMdpNAtyd70rABxvLEYRAm0ux1PuklYDhKjROAnMa-UqXc5op8JIC1KdrgQ_7X7ZXTkhE1chGnTjmx9n8DCdGSji4I57zaE1HLVsFOvGKfh71hKtbkdJ8YjNFSG2_3ksrBh8Cg0Z6rMlt8lQ-k7CH0xPxHFi1XKnSIMZ8C8ld8dzF-SfYmsod9E-K4E69gqD1gPBfo7cTilGmgvlSgJn8jzgfNP7Y6t5HDdY9NvG8tWdfVAJh74giF3eK3SBClNMSAWtQspmIG2R4gEVvqgqIVg-e8A--eKOfIS6FssInrYD2KBOJs7vqO-W3V8VVEOnmnT7uJnLMp6DTl0945s7H-RhvidoKxQ1bxNnHjSHcUahDApMXwxx1dkBuy9IIrsmiERCKg1VUWzzIWGT8bQEHTwdvzm29_jseiDr7Vo4QL5TO0FizKowpg3GeH57Ef1yfoOXxNrsQ_TtK7y00mvdonM3j0_BsUObMqoFLk1mz4LmshPcm1EyVhxv_FT3HDeoDjF99W1fNJdcCmURnJMgjU-dGZifiP-YMeWzssphUtdaJoZY7p4AWYyl01JvW0jJX5JK2CAKMnNlHTLu2TPvZonTt6KbXT8zvXNKFFCZzhjx2Q7gBBC9UVgVlUWt5VxxBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: اگر در قبال جنایات رژیم سعودی در یمن، منتظر سازمان ملل، شورای امنیت و دیگر نهادها می‌ماندیم هیچ‌یک از کارهایی که الان با سعودی‌ها کرده‌ایم را نمی‌توانستیم انجام دهیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/463423" target="_blank">📅 17:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
رهبر انصارالله: ما با کشورهای محور مقاومت اعلام همبستگی می‌کنیم
🔹
هر تجاوز رژیم صهیونیستی، آمریکا و انگلیس تهدیدی برای تمام کشورهای مسلمان است و وظیفهٔ کشورهای اسلامی، مقابله با این تجاوزات است. @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/463422" target="_blank">📅 17:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb8c7aef2.mp4?token=i1ydA_KksOeSZzO3MChBS0EECqs1B2DX2YVkrHeEkpgF9aoA-nVwf_h51ZuGKASIIdi6KE1m0VuZxWYRwJf195sWCyhuYMBnjLCjSssO2_1hyYHUsJ8vBFHJXaerqYiXKuZgUAHXMjeVf5ysjt32SNPwc63DOyp-hmKWcndJ8iw9Yl9w4haua3xReOpaQBrzSyE0j-sWWJOg0nWCHOfRu3fgsQxZ3uG-xChCzCJU5GXQzCXevJ_9rg9dVXpYG85_QF1DAmK3ryydL3PomfGcbGaQjfh3pZjRBxNO-Xesn3uQ9otZQjXlIDHTg9Q43c88GVTQGWI0XJufl-ud3Fb2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb8c7aef2.mp4?token=i1ydA_KksOeSZzO3MChBS0EECqs1B2DX2YVkrHeEkpgF9aoA-nVwf_h51ZuGKASIIdi6KE1m0VuZxWYRwJf195sWCyhuYMBnjLCjSssO2_1hyYHUsJ8vBFHJXaerqYiXKuZgUAHXMjeVf5ysjt32SNPwc63DOyp-hmKWcndJ8iw9Yl9w4haua3xReOpaQBrzSyE0j-sWWJOg0nWCHOfRu3fgsQxZ3uG-xChCzCJU5GXQzCXevJ_9rg9dVXpYG85_QF1DAmK3ryydL3PomfGcbGaQjfh3pZjRBxNO-Xesn3uQ9otZQjXlIDHTg9Q43c88GVTQGWI0XJufl-ud3Fb2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: رژیم متجاوز سعودی تابع آمریکا، انگلیس و اسرائیل است و چیزی از خودش ندارد
🔹
رژیم سعودی با مشارکت آمریکا، از نخستین روز تجاوز خود، مرتکب هولناک‌ترین جنایات در یمن شد. تمام مصادیق جنایات جنگی در اقداماتی که رژیم سعودی در یمن مرتکب شد، وجود…</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/463421" target="_blank">📅 17:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
رهبر انصارالله یمن: تا زمانی‌که هدف آمریکا، تسلط بر ملت یمن و تبدیل کشور ما به پایگاه‌های نظامی خود باشد، مشکل ما با آمریکا و عوامل آن ادامه خواهد داشت.  @Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/463420" target="_blank">📅 17:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463419">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1igNzNyZ9AYGHodpnr5xVgs9gHGPErW6810sydjs7m4G-fb2Fu79ngLEEKQu2iftf8R3Yoqy6SPdoN7T6pe1IvqadtqsgeZ0siVCI98pbxyGyg_y99SYnwpsdisosie2ima3zrjpdHd3Gf8Ltt0sWIiy4Vy9B9atUp1AmHkZV_BxEasKJuD2luAm6-R9NCNw2xYouHrO8ZlLT6A429RBv1gpvxoM6bpsdoPPrIJHUkUlHpctVklJ8VL2kv6MaUcNnkaKx4lULLUDoh5DNDy64YPsgiM2zGyx5wUdN8Ei6ctSZEo2xwXHnb8ScYM2EZd_R3bbZekpB3pK9J69sHRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزهٔ ۵ ساله برای مالکان خودروهای فرسوده
🔹
مالکان خودروهایی که به سن فرسودگی رسیده‌اند برای تعیین تکلیف وضعیت خودرو خود باید در سامانه ثبت‌نام کنند.
🔹
در این میان، آن دسته از مالکان که امکان اسقاط فوری خودروی خود را ندارند، با ثبت‌نام و اعلام آمادگی در سامانه تا پنج سال از محدودیت‌های قانونی ماده ۸ قانون هوای پاک مستثنی می‌شوند.
🔹
قانون هوای پاک، محدودیت‌های سنگینی مانند ممنوعیت تردد در کلانشهرها، ممانعت از نقل و انتقال پلاک، کاهش سهمیه سوخت و محدودیت فعالیت در تاکسی‌های اینترنتی را برای خودروهای با عمر ۲۰ سال و بالاتر (مدل ۱۳۸۵ و قبل از آن) تعیین کرده است.
🔹
متقاضیان برای استفاده از مهلت ۵‌ساله، باید از سه‌شنبه ۳۱ شهریورماه به
سامانهٔ نوسازی و اسقاط خودروهای فرسوده
مراجعه و ثبت‌نام خود را تکمیل کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/463419" target="_blank">📅 17:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463418">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
رهبر انصارالله یمن: تا زمانی‌که هدف آمریکا، تسلط بر ملت یمن و تبدیل کشور ما به پایگاه‌های نظامی خود باشد، مشکل ما با آمریکا و عوامل آن ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/463418" target="_blank">📅 17:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463417">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شهادت مأمور انتظامی در حملهٔ مسلحانهٔ ایرانشهر سیستان‌وبلوچستان
🔹
پلیس سیستان‌وبلوچستان: ساعتی قبل، در پی حملهٔ افراد مسلح به یکی از مأموران انتظامی در ایرانشهر، این مأمور در حین انجام مأموریت به درجهٔ رفیع شهادت نائل شد.
🔹
تلاش مأموران انتظامی برای شناسایی و دستگیری عاملان این سوءقصد ادامه دارد و جزئیات بیشتر این حادثه متعاقباً اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/463417" target="_blank">📅 17:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463416">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqFp0OFkAx4oS2lzVn9VFcVOoXFkMIeys8CsxdK35EWBVbjfZdZoH_5OTWxIKfWgeHtTUyPY1W-a7G2_YcAYEVPurNAZuSqupRFbJFesDjY5tRfgUd7cKgQrpCnDDByBUDntEE8LkWwHJHnqbMgNnMOgtR98G3yXpydV7EZRBbCypPKfH33BdOTlYlvhu9MiwbO7zlGx1kKGWc1VKZYybudBkawo0_pjFKQyB8dXvyzIKnlCvpwCwsFA9Fljvh_DlWMkT6GPApVaDLTH-8LOt54ROLpIOVwCNI6d9DyqtQABEuznSjT0BK3yc8PfvZKKAWmQ0xvNgh2WNtuqCU0-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور چاپ پول بانک‌ها دنده خورد
🔹
نقدینگی ۵ ماهه ابتدای نسبت به آخر سال گذشته ۱۹ درصد رشد داشته است و حالا کل حجم پول و نقدینگی در اقتصاد کشور به بیش از ۱۸هزار هزار میلیارد تومان رسیده است.
🔹
این روند پرشتاب از مرداد ۱۴۰۳ و تقریبا هم‌زمان با شروع دولت پزشکیان شروع شد. آن زمان رشد نقدینگی حدود ۱۱ درصد بود.
🔸
اقتصاددان سعید لیلاز می‌گوید روزانه ۳۰ هزار میلیارد تومان به حجم نقدینگی کشور اضافه می‌شود در حالی که دولت ۶ ماه برای افزایش ۳۰۰ هزار تومانی کالابرگ بحث کرده است؛ این رقم خیلی بیشتر از مخارج دولت است.
🔸
مهم‌ترین عوامل رشد نقدینگی در ایران را می‌توان شوک ارزی، خلق پول، ناترازی بانک‌ها، کسری بودجه و نشتی منابع به فعالیت‌های غیرمولد دانست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/463416" target="_blank">📅 17:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463415">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFIq6WRxYJeSqDm-BP_u7Mk8YLZqte7LCvITHBcr0DzBiPpbwapH-6ZcLJjuK4Kz92yXLrziZdOgTvcSWIxwAl9JGEy__Lr8NKSyl2oEyimkR9W8P4CH6e7woT5E8ulujSUoh7EKyq35MocTn9lFiR2hk8afxYtKn4EKGK1fHTlYW61ETpM2TaKbdiAy-4pD_Ut6PN3pEzKJPyKKnMAZPtscejnjHiGr363JOc7zgfpNDChVnoelQgVEeYmcTYZ8Dzv9yvxPQ5NhvSnVj2LRum5OI-tqiWPKzWFg7AqK_6qn6Mv7rYyZLnsp6FOWFaMNjNQYPQnLl7RGbJdUPEYRWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیرخزانه‌داری آمریکا: پایان جنگ با ایران، راه خروج آمریکا از رکود است
🔹
وزیرخزانه‌داری آمریکا امروز در مصاحبه با سی‌ان‌بی‌سی گفته که پس از پایان درگیری با ایران، نرخ بهره کشورش باید کاهش یابد.
🔹
۵ روز پیش، فدرال رزرو نرخ بهره در آمریکا را به ۴ درصد افزایش داد؛ نرخی  که ۳ سال بود تغییر نکرده بود و ترامپ برای بالا نرفتن آن رئیس این بانک را تغییر داده بود.
🔹
جنگ علیه ایران و بسته شدن تنگهٔ هرمز  و افزایش قیمت انرژی، تورمی برای آمریکا به ارمغان آورده که حالا ترامپ به بالا بردن نرخ بهره راضی شده است و این اقدام یعنی وقوع رکود سنگین در اقتصاد آمریکا.
🔹
حالا بسنت در همین مصاحبه می‌گوید، «نمی‌توانم به شما بگویم درگیری با ایران چه مدت ادامه خواهد داشت».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/463415" target="_blank">📅 16:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463414">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6933ee189d.mp4?token=n2DcV_8plag3T3lylgNfX_bfIFMQnA1AmVKHY-UeAVAvYXdoY1Uj_y-9za0wcJWexIDsZKnYREPgQQ9V1aG7AowjXxX-q9thjcY6xRn9AtOnNBRuz8acuwYFJfOkzzCQRGnsPNDIAzZM2K5PdU8peokYBLjKJHXAL-kUemKaJmV6oCvumTy8XAkncbgueXjOfNknTwuoxIXq9Kn4mCaB3ivoepOcI1NWi7nocQNo_jqvAoXI3Oty22wo-C-4KWrl6ysUHTShuoHIQCiCfVBOcmm0HvI3afLLr_feJ9pprsuz83Mw7LY9nnin3kudb5Q5Y67owFYWYMy_OjPN76l8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6933ee189d.mp4?token=n2DcV_8plag3T3lylgNfX_bfIFMQnA1AmVKHY-UeAVAvYXdoY1Uj_y-9za0wcJWexIDsZKnYREPgQQ9V1aG7AowjXxX-q9thjcY6xRn9AtOnNBRuz8acuwYFJfOkzzCQRGnsPNDIAzZM2K5PdU8peokYBLjKJHXAL-kUemKaJmV6oCvumTy8XAkncbgueXjOfNknTwuoxIXq9Kn4mCaB3ivoepOcI1NWi7nocQNo_jqvAoXI3Oty22wo-C-4KWrl6ysUHTShuoHIQCiCfVBOcmm0HvI3afLLr_feJ9pprsuz83Mw7LY9nnin3kudb5Q5Y67owFYWYMy_OjPN76l8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر دریادار سیاری: دشمن می‌داند که اینجا موفق نخواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/463414" target="_blank">📅 16:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463413">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e94bb1174.mp4?token=VtrmiI-DJ2XLc9yJ99GcnmzBv1UyIPYgvijNl-IE6WA2uLcsg7drtUAgUktqf7GGHhHEhBuM3R77wzkAO5t1fiznDEraC_CC1RnMxL-m-GV9mz-TF0komHxr9ZQ1vwPka73Mwyz3s-qXc1sP6pFpOXnz-nYqKa58QOZi4ZPCh_anUG5sd20_E2O3H4wKYaGvYIvQgHcIzkkFfUKXvYzOBKqFpJGYkE95KyOuVjkaOdMkAxWVw6lAwd5gu8VH0t-xZMBngR1QhFVm80Q9jyafB4pKxAYJOUsbHOxheHaCxGLhTkmH9hGMl6b22VUgPKc57zW4Pbclzpe5M0fH_Z0m-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e94bb1174.mp4?token=VtrmiI-DJ2XLc9yJ99GcnmzBv1UyIPYgvijNl-IE6WA2uLcsg7drtUAgUktqf7GGHhHEhBuM3R77wzkAO5t1fiznDEraC_CC1RnMxL-m-GV9mz-TF0komHxr9ZQ1vwPka73Mwyz3s-qXc1sP6pFpOXnz-nYqKa58QOZi4ZPCh_anUG5sd20_E2O3H4wKYaGvYIvQgHcIzkkFfUKXvYzOBKqFpJGYkE95KyOuVjkaOdMkAxWVw6lAwd5gu8VH0t-xZMBngR1QhFVm80Q9jyafB4pKxAYJOUsbHOxheHaCxGLhTkmH9hGMl6b22VUgPKc57zW4Pbclzpe5M0fH_Z0m-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت سخنگوی ستاد مردمی جان‌فدا از حضور داوطلبانۀ پیرزنی با واکر برای دفاع از وطنش
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/463413" target="_blank">📅 16:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463412">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7IUh-gBF5Z_XR_Fc386E9ZRiElDnQdmuzI_YWAFnXO7tW2NCr_GUdvmrgv85Eh4cRcCxM47ecwwbTiPyW3aNuWNhH7pdq69mj-J-oHdVBqdvZmRse7qJril9I0G0micgG4kRUrgvkHxYT5DoC1YU1z5LABgR0xeQ-vMUSe0c5eOaNjHUadLyzU1xFLo9OotgboXk2FJ7l0NCHzrKoUybLHGdYzZHnN2kyAdfUeKLKfbQsfPBGEM3IKJtJvB-tY0TrkeW31jIBOOm7kvHZQeRYgrjPBoDxvGFCayVbgUVELjGlybd-GfOIDvmrdptTVt54KBN6a2bSzhe59IMb6m2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پزشکیان فردا به نیویورک می‌رود
🔹
رئیس‌جمهور سه‌شنبه به‌منظور شرکت و سخنرانی در مجمع عمومی سازمان ملل، بدون تیم رسانه‌ای عازم آمریکا می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463412" target="_blank">📅 16:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463411">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e80bff3f.mp4?token=IAn-O3Df1KxAu9jx_B6eLimQMhJqDii52adIfAX7iTZSqUUXQ2Uk8Mb0KqSFeg8260rIXbO7UQ82B8zWExnL_3Wxse4pwlUgv1EYvydQGzMlJpurxMrq8U29y_AeWJoIWrNjdpPTsTp9KUiMCzPGkqcCamiTQ339PJvAcGGN6F-NVbHnEnwmejWVL0VDIh2Yji6xQ3eQvvIOuiMhO8_TnOS_cfWdrEblK8vh8Q-MEoAxdDQ9fVE2mjojO0jDXtUQ4OTPwdEdCwfZaJpk6gF6QckMMZX-eDWZQLyW6oRcJob4g5eVT2FUXlr_TFVS4bS_dgDXuXtFTlkdssmvIqNKbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e80bff3f.mp4?token=IAn-O3Df1KxAu9jx_B6eLimQMhJqDii52adIfAX7iTZSqUUXQ2Uk8Mb0KqSFeg8260rIXbO7UQ82B8zWExnL_3Wxse4pwlUgv1EYvydQGzMlJpurxMrq8U29y_AeWJoIWrNjdpPTsTp9KUiMCzPGkqcCamiTQ339PJvAcGGN6F-NVbHnEnwmejWVL0VDIh2Yji6xQ3eQvvIOuiMhO8_TnOS_cfWdrEblK8vh8Q-MEoAxdDQ9fVE2mjojO0jDXtUQ4OTPwdEdCwfZaJpk6gF6QckMMZX-eDWZQLyW6oRcJob4g5eVT2FUXlr_TFVS4bS_dgDXuXtFTlkdssmvIqNKbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ رهگیری و انهدام پهپاد MQ-1 ارتش تروریستی آمریکا در صبح امروز توسط آتش سامانهٔ نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکهٔ یکپارچه پدافند هوایی کشور در آسمان  تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/463411" target="_blank">📅 16:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463409">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8rNjnGuh2PkPFWaNwD2-BPBshIoYlVHt0--y3QBBd9Pr9Z8rSr1eRiY53O-QAEKAG6J-2dYumBcDa4SIukHFsRoWYbzjqPQNGNiEQcEpHxZa-9yQ63N2T9n6ilY0LbkQwn9ChrvwPYmM0zlEj0MpQjjHHq0-KpTqz5-q5o-HgjauGH2JZrHjW2nSr-Yi-gRhgWGK_SeK735nCfSunWxPzihb85BreIQZzsNGiV8DhkW4njIBw7EdmudHAIszVza56KsTTCPrMGfCrghDtFmEDWxffyECin1DvWU1aJeL9mVTWGtH0V6tl8I01MXCg8u7lU55A3Wp33RXhRDiu4smA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴۸ سکۀ متعلق به دوره اشکانیان در دورود
🔹
فرمانده انتظامی لرستان: در بازرسی یک خودرو، ۴۸ قطعه سکۀ تاریخی کشف و ۳ نفر دراین‌رابطه دستگیر و برای سیر مراحل قانونی به مراجع قضایی معرفی شدند.
🔹
بر اساس نظر کارشناسان میراث‌فرهنگی، اشیای کشف‌شده دارای ارزش و قدمت تاریخی بوده و برخی از این آثار مربوط به دوره اشکانیان اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/463409" target="_blank">📅 16:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463408">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سقوط قیمت نفت هم‌زمان با سفر میانجی به تهران
🔹
هم‌زمان با سفر وزیر کشور پاکستان به ایران، روند ریزشی قیمت نفت شدت گرفت.
🔹
پیش‌تر هم، سفر میانجی‌های مختلف به تهران زمینه ریزش قیمت نفت را فراهم کرده بود اما هیچ پیشرفت قابل ملاحظه‌ای در پرونده مذاکره اتفاق نیفتاد.
🔹
هم‌اکنون قیمت نفت در معاملات اخیر حدود ۳ درصد کاهش یافته و بهای نفت خام برنت به حدود ۱۰۰ دلار در هر بشکه و نفت خام آمریکا به حدود ۹۷ دلار رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/463408" target="_blank">📅 16:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463407">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl_YyUv0Qz05rcB9JLtviJId_59L-9Dhche7hAEc0BzRRwt7Ai27ltzK5VKVDElNX3_zzxzpUe7CKgeGGMmTR-45o03zeJwJYs1xX9yGEasxGBO4cyNZqXaql6FjDTFDQYn4V2jpopGq4gCmcUYz-sdV_cbeNvtvV_LNsdcWDviZYRh4w8rEJLGY7xmUVpHJueqoOxzJ9lbE_FZjVd42wxK5omMWqYdVXQo4-RxJ0kXX972_J8ruSjf9CeF7Cb1vwsXewmTZrMIaaBsT8rpWrLwMAoQM-oDhSu4Bc_UG2MM0wzjeeb7xLjaGZf6wCUa6mrDGKtEh_fLU5U3iaYHJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هدفمندسازی یارانه‌ها: یارانه نقدی شهریور دهک‌های چهارم تا نهم واریز شد
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/463407" target="_blank">📅 16:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463400">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PygJ_-KUt6O5iDNPhkxBgOnIx6VkEtsX1A8HYuinMttVWD6SvVThMtwfQCYnOKtwUopw55EKBkh0ob-jzjK0etbd_RXwhd6HVY4oSxtycJgCK9hVVajVcnI12MWBquTs2xFvw-YRSH8XMfpayPaOo0xcllTiFS5ZNWN5Qya3J23NFYg0Y4Rxk8zCuoaGn3SeISGKD_A9-ke3fdkUDzwPlPCDxDIkWVvC8R74DZKDjaoEf3RntanUO-odwOXPmwVTLg_Hdy6qlaeFgHq-8VSX3DZUMwDAzLP5c6XpLTsXvI78TESVw5CAuCdlyPu3NEPEgzeDq9FW25XhKYGWp642ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7HkjfeBuA1UeTwq5TeWjsTYC9QhtA2lmGBdLgDMFt7p_w8V4XQBrILntsUUN7KXBBotRXOyiIT1QwslfVHyh_zvGf_eKgpZya_SHMzeps0JffTwr9BYhuZIKk7Hmn-tphFpqZ3r4sPVYB9WJHCnglRjXAgkHAxbK_HXeI0XMOpV9kK4kS4cA85h9aDIxEVndNy1gQgs1Eml9NlVKhw8sawqy4DQoIkwsRahWC5onPXD0z1tQBab4HIL61JizFRBGrmXy9hqtkGxJv4z1NwkDRef921obJ2ppOUtJNqtSIFbW7JZMwoD1x6SHjqS63xjXiCclficAK5n8LwEETdgGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7baLZKXNr2ccCM2w14HDNSmlSh-v7pupu-8Kw9Oz1qj3GPEWoYirHffAinRtRRBktqc_6Yfb0p3ij76BNe5_1tr-FAy3rBZpPnnWPaImUWWVpBVmlvMswLRCEZz58Qeo2YoUR8M3bRhmS8VrLfLHqLqVWAPHECFnktO1fi0t-mwLTuqc8W1NjOZSSvYUrrZOmp7lHmUSinDQX31ehofiWsDxS5TbuKz3vwLXZ__LY1xVNQ9qM5kvLqZDcZlAkODuXQICpj8Mvq7aCRhh9nl5g0jw7yo0NOYnZZjUjKq8NK6bWAzMse3Fo_G_t2A6VDACccHzntMq8T5JvuyRTAEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/einp8Q5Jd7H8pEIQ4BWhwQYM7WaLOsX7rpkhnyv30GkadVzJcc_Nrw5A86WLkfrVxzxU1WURh1rCPjgW-M4yvpAMRwk5BfJs8OlhI2YMvhnmNXg5Xzrya93eKdX-lB9OxhbwlPpURCLuykWaIKhoEgkte3GpXeXjh7DvETRKmWOrFLoCpEdclRoUAs-771T_cRekd3Rb5FCBacBGXgGnka6cV468uM4JLhAp1jxc3b780xBEaCZ8ZdwMitbe6gwKU8mvuUf9m5-1TmTea1AjAGBEP_omMx7Eo6c3HhmwrI9hpMjzNvQbv-fMvAGfswl12b8PQ83Fkopw0QYwCbntPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6BMsI5MjKgE05re7Dz5GpDn9KHE8eWlqT4vI7-PI0JF0QzdW7KIeMlCQavdkg0FeLQy9sCpxbD7ygwpxJ7Dfm1yb7zvL8YVYTy11usaK-J8n3MJRjp3FNVGQMTUZuvBXZ0vhQxULelySHm0kkUB_GZ5cKchv603CB2gp-fgb5GcTfBFl2j_hddNdLh7VlnAFJQrlUF4aPcubCCHP2qo8Y29YKq9g-IPWDhP7f2MMWbDx5X-dQxJvgpY4aYPxJycXIXtVEMvefut0Pexzj1Dic0HMZdTBFnbqVTqMWKV3amwebaFU8b8kGcxOK3EqLyXovUAfeJ2uoq2Tg5Wjq562Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErTnCvtytA0NwracmJo_8LExwvhmrRLldSolqOGemfvM6t79a_VO0WO7eso_Nnf3MKb7noLiGGGz1YB0vPOej3tUbZbdvykp2EXj2Xj9Z_WtgGNmtamZirOG0rwb0JC4rO7Xd10YmRgBtfBmKIvZ6afiWsIboB_ylOq-r5DET9x9p7qhtfZydu-OVyHpW5R9w5dmuZmBrEaLCpmzYhm2BQ8cq6-dN6qfBcnF2iU7z3ju2Umdc5SJmGSNKKX_VieD75s9kO0bg_gIJY5X3QFot5lU1PmTqYqUZhIMrDeUx5EzPij4KO8-eq5z2o63mPXRPWJrcIpj2IiyWEj0mLou4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TbJgDlF1Wb3mnnQIW-WnKj7OJ37jtlsZ6uuvF3BmOKCogo1vYL-9MbHo4NhXRKSqC0IlQyn5WSFkDuZMQM2WizVjNlrkR59S61GRS3wWJZjiznzeHh-PcSCk9jqg8oRjW29zb9C4-TN9U2fo4Vq22Bx5tVobn15mH2T4mO0NBea2xIg2FmvygIyxFdAAn-49Z_CHW8E4yxUhARu5wFzzfn4dAmX4tJUD4MqWl7MkAfK0quFpN9qzyZJPbWlGscc7NI1KctLd38pFnEabPgQMUEsLMi42kVJma05y7kgrVAhLkXPkzoRIJexlm2-tC2H0rZUsQlJnz4t-WNG6T5VI-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان امروز هم‌کلاسی و معلم دانش‌آموزان شد
🔹
رئیس‌جمهور: هر دانش‌‎آموز یک لامپ خاموش کند، ۱۵ میلیون لامپ می‌شود. نخواهیم گذاشت چرخ کارخانه‌ها بخوابد.
🔹
فشار می‌آورند و مدام حقوق اضافه می‌کنند از آن طرف تورم بالا می‌رود و حقوق بی‌‎ارزش می‌شود. به‌دنبال…</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/463400" target="_blank">📅 15:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463399">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a465c69810.mp4?token=RlEnTd06fhSPEfwC7b0hdeY2zqg9ZsZ3enIIfAJA1YNnY9x0AhkGf3NxgGQFWc3N2SVQ-AnSNY8iYOAPDuceHVDCF1B6Gc-4EaCiA71PwbxWsfNgTrhODKPTBlVPsJVh1nY25-gIWUom4kcABbm2YV-huuIJ-_cQiTVLvJDk4h919BGWDJLjI4X4gwx-g5jNBnAJ5rgsugVwBAu2m5oKV9SmP1SiVRJaH8bq5X1V3-4cYWkztElv00IS6KKcR4d2LgaUBTNmNdH4qTcLcxJ4rHyZFaE3DJsh3n6l8zHA_J2r5qFAPDwe3GGzld38m01RCcv-QfjnbMcTBGxJLfwUfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a465c69810.mp4?token=RlEnTd06fhSPEfwC7b0hdeY2zqg9ZsZ3enIIfAJA1YNnY9x0AhkGf3NxgGQFWc3N2SVQ-AnSNY8iYOAPDuceHVDCF1B6Gc-4EaCiA71PwbxWsfNgTrhODKPTBlVPsJVh1nY25-gIWUom4kcABbm2YV-huuIJ-_cQiTVLvJDk4h919BGWDJLjI4X4gwx-g5jNBnAJ5rgsugVwBAu2m5oKV9SmP1SiVRJaH8bq5X1V3-4cYWkztElv00IS6KKcR4d2LgaUBTNmNdH4qTcLcxJ4rHyZFaE3DJsh3n6l8zHA_J2r5qFAPDwe3GGzld38m01RCcv-QfjnbMcTBGxJLfwUfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان امروز هم‌کلاسی و معلم دانش‌آموزان شد
🔹
رئیس‌جمهور: هر دانش‌‎آموز یک لامپ خاموش کند، ۱۵ میلیون لامپ می‌شود. نخواهیم گذاشت چرخ کارخانه‌ها بخوابد.
🔹
فشار می‌آورند و مدام حقوق اضافه می‌کنند از آن طرف تورم بالا می‌رود و حقوق بی‌‎ارزش می‌شود. به‌دنبال…</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/463399" target="_blank">📅 15:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463398">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">استانداری هرمزگان خبر غیرحضوری‌شدن مدارس استان برای دو ماه آینده را تکذیب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/463398" target="_blank">📅 15:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21b2c97f9.mp4?token=sFLKviVI_B2u59Rp0NYcM-frvlUoQpwIxihSbB5J0DrVnmGd0qBc-nthUvGh95iV59SHsJKf9UhZyKLarxw7sW26yVQUF8tiIefL2UGznGtUkA02bfXMR3Ls52LFEso32PKMyQUHSG6cQd52Rk1UhxHgamaItbWQ4wv4WhEEiXjT6DZC2HHJYfrJJda0brr5kp4wy0RXyz6kQuPAN9zodqtJtWHs4WIBBdOqo0VFBc84g5q0TbVliO5qTn-D-T9-FYe6fFnWvtlOVycUIk_bjOz9yJX2COmCuoaPBlKd_8SAl91i_AiWBprH6Xi4L1qJNDzrqK2gG1O_AU-AyQh2IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21b2c97f9.mp4?token=sFLKviVI_B2u59Rp0NYcM-frvlUoQpwIxihSbB5J0DrVnmGd0qBc-nthUvGh95iV59SHsJKf9UhZyKLarxw7sW26yVQUF8tiIefL2UGznGtUkA02bfXMR3Ls52LFEso32PKMyQUHSG6cQd52Rk1UhxHgamaItbWQ4wv4WhEEiXjT6DZC2HHJYfrJJda0brr5kp4wy0RXyz6kQuPAN9zodqtJtWHs4WIBBdOqo0VFBc84g5q0TbVliO5qTn-D-T9-FYe6fFnWvtlOVycUIk_bjOz9yJX2COmCuoaPBlKd_8SAl91i_AiWBprH6Xi4L1qJNDzrqK2gG1O_AU-AyQh2IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی سپاه: اگر تهاجم جدیدی صورت بگیرد، قطعاً سلاح و جغرافیای جنگ را تغییر خواهیم داد
🔹
اگر تهاجم جدیدی صورت بگیرد قطعاً تغییرات قابل‌توجهی در دفاع ما و هجوم متقابل ما وجود خواهد داشت.
🔹
آن تغییرات، تغییر در جغرافیای جنگ، تغییر در سلاح‌ها و تجهیزات جنگی…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463397" target="_blank">📅 15:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌آیت‌الله شبیری زنجانی دار فانی را وداع گفت
🔹
دفتر آیت‌الله شبیری زنجانی اعلام کرد: روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🔹
جزئیات مراسم تشییع و تدفین پیکر ایشان، متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463396" target="_blank">📅 15:27 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
