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
<img src="https://cdn4.telesco.pe/file/NLRxiNNJBocQNzHtAzunIrEE9LkykRZvy2Sl_ZdG-VO4V0edKexSBP7ls4IWFEuEKtCMUTYMHZZuvJoWOke0OSaiXDKRRTdF386sTuZS6qN4DeWWdkpQGm5UuZozkXd7AuFTvHXt3d6sVqHKzBSlIwryPoBW-Ni6I3iXlEkZl6DQGyzAx4Pe0VfxLplOrInh9Z1b8gMjHEMEc0cYBLpoLk7ivneQg-AmazSElzDYbFd0b05trXfhbybkNl3HpZ2K1ffIZvo0knLt11C4LXniCcA_cOs4u6jKaBU6fQUeEH1sVzb7ntoU7MMMWwWyzx3X6cBS_SjfUCnpS9c0X7unhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 23:33:12</div>
<hr>

<div class="tg-post" id="msg-460761">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bde5b1eb7.mp4?token=QxPUlv9N7EbkO4y_19_LKThrXdmguWS2jrAcjSstboQ-0Tqsm5Y7qjoanc_7_7G-AOQ9YcvTYEPJbP2V_Xn_GFx2bUvPGfSkY3CqLZuuDDMiC8HEL8t_RuIOt8UI-3YDV0rGLvp0O41SvKzj2swDKksb3pI1KC-eSWXNEyd_WiiLlNcEQL8aQFDFxo28_I9vjp_QfNQavF0KwcAkP734QUi25gbL3pVay0hGPmVart1eR8oalpqcvrJXISaAaAXJ8BWPG4gC90z0ehiV9W6ecLVPJS6e1mP1Qa1jaKZ-tec2RUTJgTA2k_GgkKBp5RsJyKkOOxxugms1yqecQiLRyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bde5b1eb7.mp4?token=QxPUlv9N7EbkO4y_19_LKThrXdmguWS2jrAcjSstboQ-0Tqsm5Y7qjoanc_7_7G-AOQ9YcvTYEPJbP2V_Xn_GFx2bUvPGfSkY3CqLZuuDDMiC8HEL8t_RuIOt8UI-3YDV0rGLvp0O41SvKzj2swDKksb3pI1KC-eSWXNEyd_WiiLlNcEQL8aQFDFxo28_I9vjp_QfNQavF0KwcAkP734QUi25gbL3pVay0hGPmVart1eR8oalpqcvrJXISaAaAXJ8BWPG4gC90z0ehiV9W6ecLVPJS6e1mP1Qa1jaKZ-tec2RUTJgTA2k_GgkKBp5RsJyKkOOxxugms1yqecQiLRyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سارق حرفه‌ای موتورسیکلت در دام پلیس بروجرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/460761" target="_blank">📅 23:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460760">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گردهمایی مجلس باحضور همۀ نمایندگان
🔹
سخنگوی هیئت‌رئیسۀ مجلس: گردهمایی حضوری نمایندگان مجلس با حضور بیش از ۲۰۰ نفر از نمایندگان برگزار شد.
🔹
در این نشست، حدود ۱۰ نماینده به قید قرعه انتخاب شدند و دیدگاه‌ها و مسائل موردنظر خود را مطرح کردند.
🔹
قالیباف نیز در ادامه درباره مسائل مهم ملی و منطقه‌ای نکاتی را مطرح و تبیین کرد.
🔹
مسائل روز کشور در حوزه‌های ملی، منطقه‌ای، بین‌المللی و معیشتی از محورهای این نشست بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/460760" target="_blank">📅 22:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460759">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309854c321.mp4?token=h3BiXkni0pL3JzyXLBdqJGlF0soANJkMMc_mIAdG_6S_h19hfa7ZdWsBDk9V7cRFFVTaljITtX_HKhHpb56A1l8BeTYFNRNzgEe7jTc4ORVNLs68Pe59naUOv199aAeWwFeq5fh1QIHBG4P3wGzF35Dr_G6ogxR7CCv3qJxGQBqGPXba9Lz5lKJS98gz44UrVpmxpsIJRbOQN6swmImLiSrW_eFJVOIpRkpMSkqfT0ZKhP-Pc_olWff2u_tUdDZ8P2zul71lDhvV7MBSzCfmvT3-3ZYAiw23_FzAqGaDuV5Ce2H9c0lS6CcJIOVXqMuY42KJjbyWQBVn6XiTBURdcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309854c321.mp4?token=h3BiXkni0pL3JzyXLBdqJGlF0soANJkMMc_mIAdG_6S_h19hfa7ZdWsBDk9V7cRFFVTaljITtX_HKhHpb56A1l8BeTYFNRNzgEe7jTc4ORVNLs68Pe59naUOv199aAeWwFeq5fh1QIHBG4P3wGzF35Dr_G6ogxR7CCv3qJxGQBqGPXba9Lz5lKJS98gz44UrVpmxpsIJRbOQN6swmImLiSrW_eFJVOIpRkpMSkqfT0ZKhP-Pc_olWff2u_tUdDZ8P2zul71lDhvV7MBSzCfmvT3-3ZYAiw23_FzAqGaDuV5Ce2H9c0lS6CcJIOVXqMuY42KJjbyWQBVn6XiTBURdcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع شبانهٔ مردم بیارجمندِ سمنان به ایستگاه ۱۹۱ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/460759" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460758">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2a24bc0a.mp4?token=CSbO_xuVjD4LPHZ5AvaY90xwv_1h4zdC6_U3sSZTNbml_QmQY7d-NrLlABrqDb-mZzjm7dgGt_Vwyss0yWE16AEMxUoEmNSsNM9l5m0RWlXNtTnwymn_CwDIIvdSMRaTCIsgfPC_keyPAtnk6K_wTWCOKHEBU4zHdVZDcA76EhxP4EshEUWSdAAWWkjDGRZn5u_qO1WAQiXrJIAKkOQoR3rGCaT1LXamLd8YBjZkraIWjq2nOwhr52d07AR_x7Jh-eiSZwx46KfX4ZcYCN2JYWdttG4xhK6duuZLZtI6A8ItUZlaqV_m5bxkRo-LFLdDlWlUNB5RzFLcECbbS5Vdqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2a24bc0a.mp4?token=CSbO_xuVjD4LPHZ5AvaY90xwv_1h4zdC6_U3sSZTNbml_QmQY7d-NrLlABrqDb-mZzjm7dgGt_Vwyss0yWE16AEMxUoEmNSsNM9l5m0RWlXNtTnwymn_CwDIIvdSMRaTCIsgfPC_keyPAtnk6K_wTWCOKHEBU4zHdVZDcA76EhxP4EshEUWSdAAWWkjDGRZn5u_qO1WAQiXrJIAKkOQoR3rGCaT1LXamLd8YBjZkraIWjq2nOwhr52d07AR_x7Jh-eiSZwx46KfX4ZcYCN2JYWdttG4xhK6duuZLZtI6A8ItUZlaqV_m5bxkRo-LFLdDlWlUNB5RzFLcECbbS5Vdqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترویج دموکراسی به سبک ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/460758" target="_blank">📅 22:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460757">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc-GTrYqz2Qdt4qJea3bHlhQzKDCI5FGiRuFC5vJ8MxmOyhnHhTAfr5WWq9z3u2IqZwzTtZRs119Dvc8BXxIW5QExQv1Og_bGUb6MtT9h33xDRULz1H5Mbi436ZmNen8l3BXowrFokijS-7GvHJMjE7o2lPYbM4GVDcaoMzi-hsIWAQjHNeuz7t3AZfxXxBqaB8yjgVjpHGfAVaSr5JnzS1-px21USwAz2jmT7rifkXM9r0eDAPQghiRvNjipIn58mxeIMP-tOGn73aEVE2CxjN5YynN7OIL2o-0cRMLc11MWLuBPdV-bILQJ-A5SozULJETWuZZ3WnVDqYBnNKIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس ذوب‌آهن را از پیش‌رو برداشت
⚽️
پرسپولیس ۲ - ۰ ذوب‌آهن @Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/460757" target="_blank">📅 22:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460756">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWW06DQfv2X8PuAu7FsBq4deTl-1CWD73m9gWVuQr3NPxMOHVuW6IV8VvloBETQSsWtvGZXZbQbENtxYVihnLAFgpEvhRNfOJo3V94CuIdqC12t5PFLNWp_YrVyuIKjALYNe_GJbxIXLl7r1jGmw8BIq6Rwc8o4lfrqqcfvovk1BDQYgiXby_Ivfpw-XjEndBGktyyt-0eZ_z66DRrIaPHGqLkqY1NtIbmvpSzQIrJh-QCjcyCg_-VJnqN4xIQhh83K2BQzoZDHMvLdbKjLcWlW74F2aM5FctiWcJZvVenT2gJenBtIAAHend4mJLzRZnAHheKxlUyjkqub_nlqhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار دبیرکل نجبای عراق به آمریکا: بعد از ۳۰ سپتامبر، سربازانتان سالم برنمی‌گردند
🔹
شیخ اکرم الکعبی: اگر یک سرباز آمریکایی بعد از  ۳۰ سپتامبر در عراق باقی بماند، اجازه نخواهیم داد سالم به خانه بازگردد و تنها اجساد آن‌ها از عراق خارج می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/460756" target="_blank">📅 22:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460755">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a73c92806.mp4?token=iv_5e2R4uENj_XscKIYqlMP-I8f-EmiXdynBN9LRS_3f55_RHsTcK3yGbfaQOY43bx0iZDRFKmIyJcOUWkBfyF6S2esXWS8iTnbe5rb3e4dogGcqsDSgIrP6Gs6e16c2RAL4UB8KAoscnmfUJXcN5aemYKrQ_o5gWMnKMZA6OZqe0ylqJ8mMPcCUol-XvNphxKtNogHIAu-Sr8V31ixkAwfC7tVseuxB169TTR2EWTSEBeOp_ntzZZ2RuR-oa6zxCkm-pyve6-l790Rsoo78o_TyjfIxMRdjjKt1hPiaiQy7bFYHjW61lnSnMzKVp8uHdbBWFep1-mNh35Y0y2WZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a73c92806.mp4?token=iv_5e2R4uENj_XscKIYqlMP-I8f-EmiXdynBN9LRS_3f55_RHsTcK3yGbfaQOY43bx0iZDRFKmIyJcOUWkBfyF6S2esXWS8iTnbe5rb3e4dogGcqsDSgIrP6Gs6e16c2RAL4UB8KAoscnmfUJXcN5aemYKrQ_o5gWMnKMZA6OZqe0ylqJ8mMPcCUol-XvNphxKtNogHIAu-Sr8V31ixkAwfC7tVseuxB169TTR2EWTSEBeOp_ntzZZ2RuR-oa6zxCkm-pyve6-l790Rsoo78o_TyjfIxMRdjjKt1hPiaiQy7bFYHjW61lnSnMzKVp8uHdbBWFep1-mNh35Y0y2WZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب‌های ایستادگی مراغه به ۱۹۱ رسید
@Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/460755" target="_blank">📅 22:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460753">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5p36dzdVBnvhCQH-GJuiacYzpSpDK8jkRA8gphPG1V1o8MUNu1H4OMJuqOiGGxpkGqmG7UE6eLIuPbfnyhvLB4goWY7zfARPrgBLN3nYTPkNkJDxQPSpOP-_gofixRfmxEVSAmKo2b4Wcxu72aWXHQpRM0iAHM2QIXrjuE4eUrdZxrHK-u6bVVk_I4QHmibxso1fsotJ6OiKGULcIJ7BURacTtiAt2vsL5gBkiCYgi1T1pCk_ELBYr1EMkvQlWw3ktjYf_0_F8UAMmTZ7O-egA_uaU7P6g-0mfN1axRW3vOJnsqq3VdRtb99gqhlLHuHkAat_j-KPtsKIpH7mKufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ابزار قرار است کارهای روزانه‌تان را پیگیری کند
🔹
دیجیتال‌ترندز: متا درحال توسعهٔ نسلی از دستیارهای هوش مصنوعی است که قرار نیست فقط به پرسش‌های کاربران پاسخ دهند.
🔹
بلکه می‌توانند هدفی را دریافت کنند، مراحل لازم برای رسیدن به آن را تشخیص دهند و بخشی از کار را به‌صورت خودکار انجام دهند.
🔹
پروژهٔ «میوز» یکی از مهم‌ترین تلاش‌های متا در همین مسیر است؛ مسیری که می‌تواند نحوهٔ استفاده روزمره از دستیارهای هوشمند را تغییر دهد.
🔹
تصور کنید صبح، به‌جای این‌که فهرستی طولانی از کارهای روزانه را یکی‌یکی بررسی کنید، فقط به دستیار هوش مصنوعی بگویید امروز چه کارهایی باید انجام شوند.
🔹
در مدل موردنظر متا، هوش مصنوعی می‌تواند این درخواست را به چند وظیفه کوچک‌تر تقسیم کند، اطلاعات موردنیاز را جمع‌آوری کند و برای اجرای مراحل مختلف از ابزارهای دیجیتال کمک بگیرد.
🔹
در چنین شرایطی، دستیار از یک چت‌بات پاسخ‌گو به یک «عامل هوش مصنوعی» تبدیل می‌شود که هدف را دنبال می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/460753" target="_blank">📅 22:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460752">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2d3dcac7.mp4?token=A3TlT0sSUr2d3KfHI_zTBIBwpma5tTeaWYIRvCWIXo2Y9mGfSxE5k4uEVbq7O2bb6KGYT19oaj9IY0F2goMrrPquB36FRG0W5gUk-oveucTm1_zJ2BOIPuHCyDb-Dh2KaOTCdcajYdhoXq4pNZGZft7XLzsN78Q1DAVemhoP9LYq3jOhpY6WwtgrZpgSVPLgPYULcfVU4MBb6_OrrtFrjz1GTHFqZBj3JOSjAr5isOSEmotE4wL9CbppjRCyjfxBeYwYo4Q8Gdje6NihcFeldMJjYCTenfwrp1Oh1u74oI8frvJ1ESFZ9kntayIIC13xyedAqHAngY_mnWaptERZkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2d3dcac7.mp4?token=A3TlT0sSUr2d3KfHI_zTBIBwpma5tTeaWYIRvCWIXo2Y9mGfSxE5k4uEVbq7O2bb6KGYT19oaj9IY0F2goMrrPquB36FRG0W5gUk-oveucTm1_zJ2BOIPuHCyDb-Dh2KaOTCdcajYdhoXq4pNZGZft7XLzsN78Q1DAVemhoP9LYq3jOhpY6WwtgrZpgSVPLgPYULcfVU4MBb6_OrrtFrjz1GTHFqZBj3JOSjAr5isOSEmotE4wL9CbppjRCyjfxBeYwYo4Q8Gdje6NihcFeldMJjYCTenfwrp1Oh1u74oI8frvJ1ESFZ9kntayIIC13xyedAqHAngY_mnWaptERZkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ هم نتوانست تولید دارو را متوقف کند
@Farsna</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/460752" target="_blank">📅 22:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460751">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnSD3jtg-z8nVXYBnp3nbAjyKdeJggzL2AZRKLEmwZi4ofV39O9nr2lhCfwY6aY-Xv2Q88hAJHFG3CqODoPvTPlfzaoRChLCLWDDyTC4zObvY9FXxwMLcmBnNjO5ut5IwfBlvaI9nBnY33GNXkv_8MrrpUptxq18aGqWLQB1V8thaBfqEBFXsHTLzy3c_DLmdA__LbZwjEnf5dtxM2gKVPhA8q6gmclrfUeZIIneg1H-l6R10bFNKAH_16Iagw6nO0rj5UBSkh4yQDhGlOuqGiR2exfmrkMcgPn9NcxvfqOvoUL85mmyR45dVtoWthoLdVpTrHGqvKmz8ArMZK9w9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان ارز‌بری خودروهای داخلی اعلام شد
🔹
تولید هر خودرو در ایران‌خودرو حداقل سه‌هزار دلار و در سایپا دست‌کم ۲۵۰۰ دلار ارزبری دارد.یعنی برای تولید هر خودروی داخلی، حداقل ۵۰۰ میلیون تومان منابع ارزی مصرف می‌شود.
🔹
در سال‌های گذشته وابستگی به واردات قطعات های‌تک پاشنه‌آشیل خودروسازی بوده است.
🔹
بازوی کارشناسی مجلس می‌گوید تا زمانی که زنجیره ارزش قطعه‌سازی تکمیل نشود، شعار تعمیق ساخت داخل روی کاغذ می‌ماند و جهش ارز مستقیماً قیمت کارخانه را بالا می‌کشد.
🔹
حالا بررسی جزئیات آماری نشان می‌دهد تارا اتوماتیک ۴۵۰۰ دلار، شاهین پلاس ۵ هزار دلار و ری‌را ۶ هزار دلار ارز می‌بلعند.
🔹
این ارزبری در محصولی مونتاژی مانند هایما X7 به بیش از ۱۶ هزار دلار می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/460751" target="_blank">📅 22:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460750">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رفع مشکل اپلیکیشن خبرگزاری فارس
🔹
مشکل دسترسی به اپلیکیشن فارس که در روزهای گذشته به دلیل تحریم‌های جدید آمریکا ایجاد شده بود، با تلاش تیم فنی برطرف شد.
🔸
هم‌اکنون کاربران می‌توانند با به‌روزرسانی آخرین نسخهٔ اپلیکیشن از طریق
سایت رسمی فارس
یا
کافه‌بازار
و
مایکت
، به صورت پایدار از خدمات آن استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/460750" target="_blank">📅 22:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460749">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d2bcce6b.mp4?token=KenISqO6fpEfKWn48JqPshew8q_F1wi1DRCQxgGDtEx3_sVkT_pfJWgSzzBTKwqB-1NK4Eq8XFWehogLgQdDZLpZ31yr2hiiOWUbo2ytojGTVN1RLHgpdUhOGprDvrMekjd0rov8RzAKViJg_ksvGFXGyxQnSpkAnIaPMaM0pjbWlAnHKEYPlfgIpqQ1DYfdcJCB4tXz3LZw0xyTDzeGp9MuhEV7Vun1xnrcpWJ5ErbQdavv1ZeaZFN5BYMlA6TA3bCqciZH5hGQ0XKZaUx5fE23s2APCRTx2PNWo-Y66TUffv3P0LV3PKY64UEMNOON4ZjdSXVEx5IqyEzXc9j2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d2bcce6b.mp4?token=KenISqO6fpEfKWn48JqPshew8q_F1wi1DRCQxgGDtEx3_sVkT_pfJWgSzzBTKwqB-1NK4Eq8XFWehogLgQdDZLpZ31yr2hiiOWUbo2ytojGTVN1RLHgpdUhOGprDvrMekjd0rov8RzAKViJg_ksvGFXGyxQnSpkAnIaPMaM0pjbWlAnHKEYPlfgIpqQ1DYfdcJCB4tXz3LZw0xyTDzeGp9MuhEV7Vun1xnrcpWJ5ErbQdavv1ZeaZFN5BYMlA6TA3bCqciZH5hGQ0XKZaUx5fE23s2APCRTx2PNWo-Y66TUffv3P0LV3PKY64UEMNOON4ZjdSXVEx5IqyEzXc9j2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ جانباز؛ از میدان جنگ تا امروز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/460749" target="_blank">📅 21:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460748">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a89db0851.mp4?token=ejVJ06BHYuQfGY1zT-9RNb1w57SSBQ4FWfLSmRxR22VvRS4DPYbQEEL1SVXGfS8PGGlvj1R2C6VU1qVQ3EHt6H5uyubkHCIZIE5F_gxLoNnCAnEK0N-oqLplJvZxIhGjPLaL2RDbhuFrh1On5VhP0pPf3XXahZqVw5_SPM9at6jyDHtwmxunqWjVFRajjMs94cGUHLJLZZITdfHbtDGuwMaSqrTFAfpDUlpxsTc2WsH_T02aPSj5_I8F5WHHqDwkiEl0NU5Ox-Jal0_u6c11bK36zTxqpNGthllLm0O0PQ2QKm8EL43PRlwr7lVLemPXDFEa9t31LNHvcM4ZoTN-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a89db0851.mp4?token=ejVJ06BHYuQfGY1zT-9RNb1w57SSBQ4FWfLSmRxR22VvRS4DPYbQEEL1SVXGfS8PGGlvj1R2C6VU1qVQ3EHt6H5uyubkHCIZIE5F_gxLoNnCAnEK0N-oqLplJvZxIhGjPLaL2RDbhuFrh1On5VhP0pPf3XXahZqVw5_SPM9at6jyDHtwmxunqWjVFRajjMs94cGUHLJLZZITdfHbtDGuwMaSqrTFAfpDUlpxsTc2WsH_T02aPSj5_I8F5WHHqDwkiEl0NU5Ox-Jal0_u6c11bK36zTxqpNGthllLm0O0PQ2QKm8EL43PRlwr7lVLemPXDFEa9t31LNHvcM4ZoTN-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمار متناقض ترامپ از نفت عبوری از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/460748" target="_blank">📅 21:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460747">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb2f7c881.mp4?token=Ez_2MIg4W5mVeeUPrTizT-jwbrEJczAD0lgQ4P-xobnNSOWohN-ToAdEwsFUnY9AeUQgyFEmwIaZBoCO44dbgBX2N3MC0DkyYUaOf-zUt_LKPY4YaXdaI9zh86cmNnR4F_rX_F0_yUwXZ8VVn1zE7bv4WsqQWW70b-J1leSbwplzSI0T9HrcTktAZR1FflDP5egs869EI9CVwTkhNfkV3y6KY_f9jgCohbSEfm3y5Be2AUaAVXJl9wKxwCLk4dc89_Hh5JM43-R1sPZuwT-no2RiQ6TBSrh_bkeiK24civ3Z_wCOP7Q8aZK1pcQaMHNbj-M7BUtp7S6uTzc1CP2jxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb2f7c881.mp4?token=Ez_2MIg4W5mVeeUPrTizT-jwbrEJczAD0lgQ4P-xobnNSOWohN-ToAdEwsFUnY9AeUQgyFEmwIaZBoCO44dbgBX2N3MC0DkyYUaOf-zUt_LKPY4YaXdaI9zh86cmNnR4F_rX_F0_yUwXZ8VVn1zE7bv4WsqQWW70b-J1leSbwplzSI0T9HrcTktAZR1FflDP5egs869EI9CVwTkhNfkV3y6KY_f9jgCohbSEfm3y5Be2AUaAVXJl9wKxwCLk4dc89_Hh5JM43-R1sPZuwT-no2RiQ6TBSrh_bkeiK24civ3Z_wCOP7Q8aZK1pcQaMHNbj-M7BUtp7S6uTzc1CP2jxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف دولت از افزایش نرخ سوم بنزین چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/460747" target="_blank">📅 21:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460745">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ff4bcd6c.mp4?token=T0LmTMGzA1DtFy_8SwOobIlGkpJ54uJIHXTOZmklNZk_cMMVmYq2bPfAUNbcRzGSaShM5M5cTsIGG1i48TxGUgPJMAhO2JqHB2zCYD4OLNMLWnEjnCvkx5cELljZyb1uwqdN9ow91r1tbtujl04vDiQ3_RVKHnaQvurClquwhFaq14k6WIxYHqtA44wM6V4yRRyXD9JzzJEKhgtkfW_rr6BX4ckbZTREMNeCJsC4Ue5y10sZ7qKz9fflvIW7TOxxXeU66lasyELVnbHKT0g6WVbHv-7pBXXwA8UlSKx7PX-2wXCjtv8it6b_W7kjWvO0Ne7qs1TEf9nV7HDfAZVfzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ff4bcd6c.mp4?token=T0LmTMGzA1DtFy_8SwOobIlGkpJ54uJIHXTOZmklNZk_cMMVmYq2bPfAUNbcRzGSaShM5M5cTsIGG1i48TxGUgPJMAhO2JqHB2zCYD4OLNMLWnEjnCvkx5cELljZyb1uwqdN9ow91r1tbtujl04vDiQ3_RVKHnaQvurClquwhFaq14k6WIxYHqtA44wM6V4yRRyXD9JzzJEKhgtkfW_rr6BX4ckbZTREMNeCJsC4Ue5y10sZ7qKz9fflvIW7TOxxXeU66lasyELVnbHKT0g6WVbHv-7pBXXwA8UlSKx7PX-2wXCjtv8it6b_W7kjWvO0Ne7qs1TEf9nV7HDfAZVfzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام مسکن تهران یک میلیارد تومان شد
🔹
با اعلام مدیرعامل بانک مسکن، مبلغ وام مسکن به‌ازای هر نفر افزایش پیدا کرد.
🔹
تهران:  یک میلیارد تومان به‌ازای هر نفر
🔹
شهرهای بالای ۲۰۰ هزار نفر: ۸۰۰ میلیون تومان
🔹
سایر شهرها: ۶۰۰ میلیون تومان
🔸
یعنی زوجین در تهران مجموعا ۲ میلیارد تومان برای خرید مسکن دریافت می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/460745" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248b05fa76.mp4?token=smIN83xv-ps3pE_BXLzmWTDkEbdw4P0sNwmog1CNbStNfowGMxynyIWTxOaUrKhw1v5dWcxKodvzWenG4ku0L3D_hR1bDoWvL2Sz5JK13YN_TkfQ8YhcD2puvh-MCA2hcM6NVTDTr_HL-DUxqqJMnvgf-34MLOZmE6iRuSAmB9_t42Cn1xV53fn-mXM93F4_qk-K33RuDY46Qytn1rAf7W954tCpoT3fzHNlh0DbU33eF5vOMUmYFdST4ReNB950ZfAyqY0iIYZy88AIw8SwMGxn1PRL9IrRIECEeNGE5Ts6vp68-U82Xf-MoR-kyCc6l1w4Qkg-jA88Z9t5W4Po6WxCVK96uw_H2JmTk5qSjk8126QuIhxNTINXgK1lDZvj8EJ6rPzl9hoXb8X3tvSoQggT0PGd7XCnXYXlmtwoBVntU_yHMAYdWiOupgzFBXClseXJ-mgvCdZ6furUhGYxUtteqvj8-CaBlNk8nbmjUHTM2tI1I0thVAY68IdYipDW2C6HLQINxWOFX2vkYYABRy6MMW3yOrjHgSiCkYtU4233fEK03yEb_4JkniLDyiTUESjOQvC_GwNzm4grIvePtVhtxmB7genJD-CxR2Ws-4Ix1A1zT37XzNH9FVwArH3MKYh92DU6LA2X9fiMpzUMCP9GcPiPO9jMkbhCR6TZ87U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248b05fa76.mp4?token=smIN83xv-ps3pE_BXLzmWTDkEbdw4P0sNwmog1CNbStNfowGMxynyIWTxOaUrKhw1v5dWcxKodvzWenG4ku0L3D_hR1bDoWvL2Sz5JK13YN_TkfQ8YhcD2puvh-MCA2hcM6NVTDTr_HL-DUxqqJMnvgf-34MLOZmE6iRuSAmB9_t42Cn1xV53fn-mXM93F4_qk-K33RuDY46Qytn1rAf7W954tCpoT3fzHNlh0DbU33eF5vOMUmYFdST4ReNB950ZfAyqY0iIYZy88AIw8SwMGxn1PRL9IrRIECEeNGE5Ts6vp68-U82Xf-MoR-kyCc6l1w4Qkg-jA88Z9t5W4Po6WxCVK96uw_H2JmTk5qSjk8126QuIhxNTINXgK1lDZvj8EJ6rPzl9hoXb8X3tvSoQggT0PGd7XCnXYXlmtwoBVntU_yHMAYdWiOupgzFBXClseXJ-mgvCdZ6furUhGYxUtteqvj8-CaBlNk8nbmjUHTM2tI1I0thVAY68IdYipDW2C6HLQINxWOFX2vkYYABRy6MMW3yOrjHgSiCkYtU4233fEK03yEb_4JkniLDyiTUESjOQvC_GwNzm4grIvePtVhtxmB7genJD-CxR2Ws-4Ix1A1zT37XzNH9FVwArH3MKYh92DU6LA2X9fiMpzUMCP9GcPiPO9jMkbhCR6TZ87U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا ۱۹۰ خسته می‌شویم از شمردن؛ اما از حضور هرگز
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/460744" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrwKtOiFY_QSQZOT_3tQyaDaLBn35jmZGHTuetf545UPptIPpzujH5L2aPG6xxmgBR1vaJysBUE8y0IQPa7MTg9wjXhORc4B-vou8CvQWoAtB0c-ZySpOmKOy0_IeDM1Rte8WMgt2ZjX23xwfPUlgUE5S7dV8jqR5bwS8cEzJi2Z5KSEI65LzLswYUM1qcXAPIGNGeWk5fIM-iYJQJRpOn_BLSaWE0zuRlBhg2ZN3WvU0Vq8CpjFcdSShBYHcDOMgtnMzYIFH0-T_VOa6FiRFgvNGBIR2nLUZDkPhlrljxLZfEixEggqFIT0jbkz2rXZeH7sZQhlgwBC0MFKzQJD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور پیشین لبنان: مقاومت تنها راه مقابله با اسرائیل است
🔹
امیل لحود در پیام تسلیتی خطاب به خانواده‌های شهدای جنوب لبنان نوشت: تاسف‌بار است که تقریباً هر هفته ناچاریم همین سخنان را تکرار کنیم، در حالی که غرب نظاره‌گر است؛ به‌ ویژه آمریکا که قرار است ضامن آتش‌بس باشد، اما این توافق‌ها همچنان روی کاغذ باقی مانده‌اند.
🔹
از زمانی که پای میز مذاکره با این دشمن نشستیم، آنها همچنان به تجاوزات خود ادامه داده‌اند؛ تجاوزاتی که علاوه بر حملات علیه غیرنظامیان، شامل سوزاندن زمین‌ها و تخریب و با خاک یکسان کردن روستاها بوده است.
🔹
این دشمن به توسعه‌طلبی خود پایان نداده و نخواهد داد، زیرا جز منطق قدرت را باور ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/460743" target="_blank">📅 21:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4addf5a73b.mp4?token=BAkgSDyC1_pD8q65aLpwJKqXUagDuWbiVZRwlmVKiLPDTAhk4zkNPkfK6GWUN5oZzTMKJPC_e8IpjQjDcl-GwrBkp3o4XnEM5dHVblCTRq8cEZIaoeDT_yjmgwrETywjalhPTGd2_WoGPMyyR9kTjgnBU5fX946-wO50lOofdIiUKzav4WZTHWsYvP137VCJnZMF8fVxIfbY1Jz2sI9gH-sfu3fC7737smVQ69_hVLC1ZrSxh7iTEYqR-HQWXQu3owSEkTmzYgPdruDoV0smnhPU36cN9z-ly0rNDowmZQ-_QnWKF4c-ErAuJAa-4dA9hQ7YylDkiJq3_xWMlHqcBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4addf5a73b.mp4?token=BAkgSDyC1_pD8q65aLpwJKqXUagDuWbiVZRwlmVKiLPDTAhk4zkNPkfK6GWUN5oZzTMKJPC_e8IpjQjDcl-GwrBkp3o4XnEM5dHVblCTRq8cEZIaoeDT_yjmgwrETywjalhPTGd2_WoGPMyyR9kTjgnBU5fX946-wO50lOofdIiUKzav4WZTHWsYvP137VCJnZMF8fVxIfbY1Jz2sI9gH-sfu3fC7737smVQ69_hVLC1ZrSxh7iTEYqR-HQWXQu3owSEkTmzYgPdruDoV0smnhPU36cN9z-ly0rNDowmZQ-_QnWKF4c-ErAuJAa-4dA9hQ7YylDkiJq3_xWMlHqcBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرسپولیس ذوب‌آهن را از پیش‌رو برداشت
⚽️
پرسپولیس ۲ - ۰ ذوب‌آهن @Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/460742" target="_blank">📅 21:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90e3e6478.mp4?token=DKwBnlTC3b3nwAR2Uvqo8_YVuZK34gbnfY3up05k2FAGOYFZS51KtW2Fli_5sZlKKUDHDjqABil6ah03BhSQz05ZoApnwg33zGKynMx59Ia4uK_27TJqKGSQ1kBsWTbLLZTtVAy-79Zp9oz_BZI24TidhSnbfnfpEMrDVvViDKQemn4dNX0zl5jdF-rP1CvSh3RLmu7-LQxW5jNO95Pzh_2VFpeLrnd_eaUXY4TPw4IDP5-3wM0XHO_GXl1bP082DiIqP46oSxEAUgZt-8g1wRoXZXXR5ils__lM9na_0-mIinBYTD56Kz4ak_ijoh30pSLl_p1dNB24-vkUF1pWLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90e3e6478.mp4?token=DKwBnlTC3b3nwAR2Uvqo8_YVuZK34gbnfY3up05k2FAGOYFZS51KtW2Fli_5sZlKKUDHDjqABil6ah03BhSQz05ZoApnwg33zGKynMx59Ia4uK_27TJqKGSQ1kBsWTbLLZTtVAy-79Zp9oz_BZI24TidhSnbfnfpEMrDVvViDKQemn4dNX0zl5jdF-rP1CvSh3RLmu7-LQxW5jNO95Pzh_2VFpeLrnd_eaUXY4TPw4IDP5-3wM0XHO_GXl1bP082DiIqP46oSxEAUgZt-8g1wRoXZXXR5ils__lM9na_0-mIinBYTD56Kz4ak_ijoh30pSLl_p1dNB24-vkUF1pWLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمار متناقض آمرکا از نفت عبوری از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/460741" target="_blank">📅 21:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460739">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzayaKFkFrBj1ZMli-vDPNtJdci-QqRpBLo3NDyKd3faGx2FPL9gykjJdOTyn0J7h6cGood2DP7Aa9OYIx4d9OWyPZl4gCWGJ0K7jhjt4J0oR5HPuohi-4YVucm2J4gPidJbXs54of2B1gnb97wukaC459zqjzNtACfuTChIJYOc4tbzTDhs31_sDX6WTHMNFgzb_TdicwkwY8zTVVxeF06X6k30jrzDRPfxjrz2eN1r_ST35omfBTDQueARmvjRmZwH47pKnTZRIHNhpSD3nAtAR6_lH23hbKq5SZf3xU5ArgAa1c5sMURWle57O1gpTz7QX06spnwEIvP_v8DpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل دوم پرسپولیس به ذوب‌آهن توسط شهرآبادی در دقیقۀ ۶۴
⚽️
پرسپولیس ۲ - ۰ ذوب‌آهن @Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/460739" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460738">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de63667a28.mp4?token=R6zgRkVqvSLb6u9E70YKS831HoxhvLgZTr95ABtk4nhE97KKFkHWe0M2wKYJhZ3NS_ejtyqi-NC7uIzBUSAa9J4w2eEwKKPXqTRVreHpC9fMHJoOsNCrfGmaHNZSUFx26L8zY95YTNXa9f43qZzlVFY4prENdXGN09f_VDROBZ-wVbN4yjjtgNpz21u5IkbmdVdNL1XOjKe1ed6fAX-SrcWbJQLjvvFB7o6NpX4quHOSdF7XNLGSaG6tKC5FXC2SLKo5kZNqzlpWsNzL4o62727kBCd_Iw1C8jmWBTiqMwGmoFnCN61n-paSKfS7aMjUmKoRHTd4BTRr02wf671Ryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de63667a28.mp4?token=R6zgRkVqvSLb6u9E70YKS831HoxhvLgZTr95ABtk4nhE97KKFkHWe0M2wKYJhZ3NS_ejtyqi-NC7uIzBUSAa9J4w2eEwKKPXqTRVreHpC9fMHJoOsNCrfGmaHNZSUFx26L8zY95YTNXa9f43qZzlVFY4prENdXGN09f_VDROBZ-wVbN4yjjtgNpz21u5IkbmdVdNL1XOjKe1ed6fAX-SrcWbJQLjvvFB7o6NpX4quHOSdF7XNLGSaG6tKC5FXC2SLKo5kZNqzlpWsNzL4o62727kBCd_Iw1C8jmWBTiqMwGmoFnCN61n-paSKfS7aMjUmKoRHTd4BTRr02wf671Ryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای عدد صفر در جایگاه‌های بنزین چیست؟  @Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/460738" target="_blank">📅 20:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460737">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1PLaRo2orHOsjJfOarZSA5Ptyh5r9kmju68hJiQ1ecK5ZvxdhNzB8ZkYRYtlIzwIp3mvr7FdKyoR5DoZ2iD_EnR7HHYlr4mS3EwPQo4EFGZum0rtB_bf-mgpqJHCfrxZVhOdUJZvmQuU4GhEfEd7QvR94Bjy-AiO_b7RatJGZsjepnVHLjaCTSqzm2WzBRm98YMWHb-p7iIJAF4QefzH7Z9G1mwK3yVsvMd_DagDyAs-UBNu1JUU73Xxz5EpReCJvIHBJrgisoozuYbP2MeUdrWhPA7Uium7RgEZ9tuf3cmQyW3Rcw7ErmpsJpSicUuLxvwnyeIn0B1zCJpaDZQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان: تاوان جنگ‌افروزی اسرائیل علیه ایران را همۀ جهان می‌دهد
🔹
تا زمانی که گره تنگۀ هرمز باز نشود روند افزایشی قیمت‌ها در جهان ادامه خواهد داشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/460737" target="_blank">📅 20:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460736">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46bf1f598.mp4?token=Y881rCTrA_g5cufJznbO3buwJ6QlnQsmS0a0XZFruhq96KcBa8va3kv5hsfha1WKBoL_tGs2TdSAuRWA6PNy3vwRsaqdGHcbS0H5FmLiEu2yhLSAgvJBUmFteaBddcx9ZtSUXCqP8czuzibckLGHzDHgoqJpY9uauuwKK_vLYVGgiTVkQQZYJvsZkShpfGqw6jq0TrXCx6lO1TgXJN9TYIAHaQPy3vnti52v6wC7OewN50DPlMAxQ5oOujbN2e-8q5gzw-uk3Gqp-xIEURZ-zfoIvJr7OvmY4LYZDg3hoOoXu0si7K4SPMdc16ggRlrbPyuj1zA159LUmTFyTkl9YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46bf1f598.mp4?token=Y881rCTrA_g5cufJznbO3buwJ6QlnQsmS0a0XZFruhq96KcBa8va3kv5hsfha1WKBoL_tGs2TdSAuRWA6PNy3vwRsaqdGHcbS0H5FmLiEu2yhLSAgvJBUmFteaBddcx9ZtSUXCqP8czuzibckLGHzDHgoqJpY9uauuwKK_vLYVGgiTVkQQZYJvsZkShpfGqw6jq0TrXCx6lO1TgXJN9TYIAHaQPy3vnti52v6wC7OewN50DPlMAxQ5oOujbN2e-8q5gzw-uk3Gqp-xIEURZ-zfoIvJr7OvmY4LYZDg3hoOoXu0si7K4SPMdc16ggRlrbPyuj1zA159LUmTFyTkl9YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای عدد صفر در جایگاه‌های بنزین چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/460736" target="_blank">📅 20:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460735">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b74acdb12.mp4?token=pEmbUHF2lWxY85IKIQeJxd1WSBwzKeBMDrwbOU_Ccu-i6GOcyBWJRkirxZnCGL5cT1XqQzihCt_FXUrCFI6EUy11_w72CuTB-7oBmeDJ3j3GqVHojOAjsAZR1FZForVBwOpnF5f0Nynrbeuxn7Tw1f3NiWMVGXceCmHgx51cf_pSW1iVrFC--T-8IHTEy1vE26tHMEh77U7xvrAaIQsl2WHFk9k-8O8dftlrhxTGgxsirHuqwkg9eZ-Z6rB4F_Bk3wPwFwE5a7K1Ot-JQFbUy0pDXU1wz148f1OO6egg_UDA77Y6FS6FS_e-y_PkwHKg_-pkMOWe4WIKlxhmhinVmDyBXcqiaPkrqss0UITzvzp4k6AeIyZOeydLqGYIr8TAcv5WCbhBlY3u-ejk3sPSJaWTx4UFbubB7MsEWFdCFuYyzJwxoIuuP1POfhUEcF7zr3ckQQclAaq7ne6UGgt4a1G_PG_aQiHJyS0yoMhHi5N_wk7g4xQq7Oc4lC4WuOZVLf6Fv_7vyTB8bHVhm0fE7hLxfrXTU1hkmgWWJepZz2fXUv0ZCwB17WBop3GnxuZdQepcH_-KuJxhOMfOkrP7qvy1efvaWAm7FDLuTfxGJNnQmNIRvxjcpTr-PWTMKXGShIVkvMl1rT2ZJWGHdhOMMOpEUm46fxExpVIY8vXcpoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b74acdb12.mp4?token=pEmbUHF2lWxY85IKIQeJxd1WSBwzKeBMDrwbOU_Ccu-i6GOcyBWJRkirxZnCGL5cT1XqQzihCt_FXUrCFI6EUy11_w72CuTB-7oBmeDJ3j3GqVHojOAjsAZR1FZForVBwOpnF5f0Nynrbeuxn7Tw1f3NiWMVGXceCmHgx51cf_pSW1iVrFC--T-8IHTEy1vE26tHMEh77U7xvrAaIQsl2WHFk9k-8O8dftlrhxTGgxsirHuqwkg9eZ-Z6rB4F_Bk3wPwFwE5a7K1Ot-JQFbUy0pDXU1wz148f1OO6egg_UDA77Y6FS6FS_e-y_PkwHKg_-pkMOWe4WIKlxhmhinVmDyBXcqiaPkrqss0UITzvzp4k6AeIyZOeydLqGYIr8TAcv5WCbhBlY3u-ejk3sPSJaWTx4UFbubB7MsEWFdCFuYyzJwxoIuuP1POfhUEcF7zr3ckQQclAaq7ne6UGgt4a1G_PG_aQiHJyS0yoMhHi5N_wk7g4xQq7Oc4lC4WuOZVLf6Fv_7vyTB8bHVhm0fE7hLxfrXTU1hkmgWWJepZz2fXUv0ZCwB17WBop3GnxuZdQepcH_-KuJxhOMfOkrP7qvy1efvaWAm7FDLuTfxGJNnQmNIRvxjcpTr-PWTMKXGShIVkvMl1rT2ZJWGHdhOMMOpEUm46fxExpVIY8vXcpoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عارف: برنامهٔ اصلاح ساختار بنزین بر این اساس است که یارانهٔ واردات به‌تدریج حذف شود
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/460735" target="_blank">📅 20:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460734">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXMfcPdARbDLr_1VPs8FqwSzJS-FGIJ8r1gnsHoNoOCfxZx_SRbOBwyjw5p3Dt3j2qzCu_peloUozfRdi43PAY_jsAl_8Qrtb30SOR1SstrtPmD2gV5fZ7-bQvPx4LHYFuhd4VXlWmPjWdp3SYuwceBPf1vRLTQ1aXTdpvv_Qi-svnZuzMxk-bVYr1K8WHByBUFE-12bAxndzSOxYGeGRqrAzO7ZAvyQ4KUxZ_49d0BGe9xtyCxHcrtI0wwxzFr2yIYq-TJ_gQieD5tEWpV0v22NPUcwNz-Gx8IVwT-KO0JPoIrz07RbB0vVWx4GSiOk8gxgRSu9rw8gfxRkRa4ZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنش هرمز قیمت گاز اروپا را به بالاترین سطح ۳ ساله برد
🔹
قیمت گاز طبیعی در اروپا در آغاز معاملات هفتهٔ جاری با افزایش چشمگیری همراه شد و به نزدیکی مرز ۹۰۰ دلار در هر ۱۰۰۰ متر مکعب رسید.
🔹
تشدید تنش‌های نظامی میان آمریکا و ایران در منطقهٔ خلیج فارس و نگرانی از اختلال در مسیر انتقال انرژی از تنگهٔ هرمز، عامل اصلی این جهش قیمتی عنوان شده است.
🔹
براساس داده‌های بورس لندن (ICE)، قراردادهای آتی گاز هلند (TTF) برای تحویل در ماه اکتبر، امروز با رشد ۳.۳ درصدی نسبت به قیمت پایانی جلسهٔ قبل، در سطح ۸۹۲.۸ دلار در هر ۱۰۰۰ متر مکعب معامله شد.
🔹
این قراردادها روز خود را با افزایش ۳.۵ درصدی و قیمت ۸۹۴.۶ دلاری آغاز کرده بودند و در ساعاتی از معاملات امروز حتی به بیش از ۸۷ دلار در هر مگاوات‌ساعت (معادل حدود ۹۰۰ دلار در هر ۱۰۰۰ متر مکعب) نیز رسیدند؛ این بالاترین سطح قیمت از دسامبر ۲۰۲۲ (دی ۱۴۰۱) محسوب می‌شود.
🔹
تنش‌های نظامی آخر هفتهٔ میان آمریکا و ایران که به حملات متقابل به نفتکش‌ها در آب‌های اطراف ایران انجامید، نگرانی‌ها را دربارهٔ امنیت تأمین انرژی از غرب آسیا به شدت افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/460734" target="_blank">📅 20:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460733">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d269b74f.mp4?token=L1JZVnTUg-zhOi4nR0Hpg-bzjaJGdZHHiF85msS_ihpbWH7TWwtzz_I3dhDwv8O9WocG5KbP9miMTKPY7h9mIbHFy2WtiZzho10xZi3cDR3OJ_oQ6QlEyLyI7RXxvNCkzYTkBDvihTYIbtalzDmobmWCxFMdACmKMlYdNsxAJKcQ6Ikw4A8zv-ZsJLGaU4gocSlaaRKH2bCr5DtNFkPy56pPa1a1BSv0UF9Bcl65UUktJuZvvbgemTTlUAPQTYkS48cj9BU5J4bgHXs6LBZAGxTLuVqMk5mMUvFYVddK8RIFmgqgV2_sJ3DEJglJlvJ3sMVxX5dh1TaniBDwYdD4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d269b74f.mp4?token=L1JZVnTUg-zhOi4nR0Hpg-bzjaJGdZHHiF85msS_ihpbWH7TWwtzz_I3dhDwv8O9WocG5KbP9miMTKPY7h9mIbHFy2WtiZzho10xZi3cDR3OJ_oQ6QlEyLyI7RXxvNCkzYTkBDvihTYIbtalzDmobmWCxFMdACmKMlYdNsxAJKcQ6Ikw4A8zv-ZsJLGaU4gocSlaaRKH2bCr5DtNFkPy56pPa1a1BSv0UF9Bcl65UUktJuZvvbgemTTlUAPQTYkS48cj9BU5J4bgHXs6LBZAGxTLuVqMk5mMUvFYVddK8RIFmgqgV2_sJ3DEJglJlvJ3sMVxX5dh1TaniBDwYdD4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به ذوب‌آهن توسط علیپور در دقیقۀ ۴۳
⚽️
پرسپولیس ۱ - ۰ ذوب‌آهن @Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/460733" target="_blank">📅 20:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460732">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlWdUD01YW_ns0TSOwPUzubigF0Ti0s1tlbpROACxkI701sP-Wihor2i3dsaNAn1NrCyUns0VoJVXsxk7i2QvAe2s4wlfjsHFnj9GPdqAWueLdBRMgjLcumX3O5n8Y4_5KVP5-MDAzAZwYwlUrnSJN3maREZShVNL05Ha5AN9dISQpuY1wuja46D2Fe_MDCtcdOi4oiqpPrpYUhAcUvWCpUso9NRE_bZXMcx_174M9NZ2YP2Pbya3pR3D98SDJRXHgPXIQErgYHnPBqABQmNAonGQwMd-smBDmhpyFb4Z7A_2_lCur6PFq8ZYQG7sm1mYwpfcv-55lgImeDiHISipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت قضایی عالیشاه از خداداد
⚽️
در پی اتفاقات و حواشی شب گذشتۀ دیدار تراکتور و گل‌گهر، امید عالیشاه در نظر دارد از خداداد عزیزی، به‌دلیل فحاشی‌های صورت‌گرفته شکایت کند.
⚽️
گفته می‌شود فیلم و فایل صوتی مربوط به اتفاقات رخ‌داده نیز وجود دارد و عالیشاه قصد…</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/460732" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460731">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e3566765.mp4?token=jCEvFGK-W9dzRgU_SFyn6SZkxtHXPSSdaauWe6DRj3icrSyKABeJB8AESaYegUDlFVMrOYkxS0GN-gUy5bfjFy-1unFNxX5PMIzAt-7EXON0vL1o7NHvTAM_YKu3IcF-SA8Hy8cqEk1pJ5bSMh8ZCfWDphR7fwnRUWdGZrEF9gZCLhWTRp53Wdm1HM-_894qjd1N3ma_IKHFOQWR7H1-P8clJrKrU3AwoBN9nfFPZ9n3KBDqohYIwT3IS5A9VGgpKZWfvCa9OflPdznQK4tcSebL_g0u9SAKNTrKewqKNL5Z4K1bPpWCYhSL5mQh8MsZkt0qkXX-71-olHW5G-_WdYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e3566765.mp4?token=jCEvFGK-W9dzRgU_SFyn6SZkxtHXPSSdaauWe6DRj3icrSyKABeJB8AESaYegUDlFVMrOYkxS0GN-gUy5bfjFy-1unFNxX5PMIzAt-7EXON0vL1o7NHvTAM_YKu3IcF-SA8Hy8cqEk1pJ5bSMh8ZCfWDphR7fwnRUWdGZrEF9gZCLhWTRp53Wdm1HM-_894qjd1N3ma_IKHFOQWR7H1-P8clJrKrU3AwoBN9nfFPZ9n3KBDqohYIwT3IS5A9VGgpKZWfvCa9OflPdznQK4tcSebL_g0u9SAKNTrKewqKNL5Z4K1bPpWCYhSL5mQh8MsZkt0qkXX-71-olHW5G-_WdYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: مردم ضرورت برخی تصمیمات را درک می‌کنند
🔹
امروز پس‌از اعلام قیمت جدید نرخ سوم بنزین، صف جایگاه‌ها خلوت بود.
🔹
این نشانۀ فهیم‌بودن ملت ایران است. @Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/460731" target="_blank">📅 20:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460730">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fd6c268e.mp4?token=TXhNRjIbmsWeg5-0bowAeRjSgZM5OYCc2RAFi0Ayzfl74qdd5-PjHfCEt7GGM7rHV7y-5JrAgFND754L1pRoQc7XC7zlwuFBHldcvZ5HcIJvb-KyWRwVvgEE3l8qG8AzT6ojd-WHQiBsbUtX0Xxv8GXeSW-5lFe_3cDlnBjk4k7k-8NozibLY-6EDiLjXKFkBCExaHB7wRuDj8jvHTDNIpVVvPTjdLu3xqeKmPZaiLO_c3NuABOyJScyxrfPD7J8BTe1VLVl8bjM0XwRI727Mn6gxVpeB_iweBuo5dnOynrtfBkQc7dRbfrL1cdtuCJoK3avxDr28REHmDgCf0leiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fd6c268e.mp4?token=TXhNRjIbmsWeg5-0bowAeRjSgZM5OYCc2RAFi0Ayzfl74qdd5-PjHfCEt7GGM7rHV7y-5JrAgFND754L1pRoQc7XC7zlwuFBHldcvZ5HcIJvb-KyWRwVvgEE3l8qG8AzT6ojd-WHQiBsbUtX0Xxv8GXeSW-5lFe_3cDlnBjk4k7k-8NozibLY-6EDiLjXKFkBCExaHB7wRuDj8jvHTDNIpVVvPTjdLu3xqeKmPZaiLO_c3NuABOyJScyxrfPD7J8BTe1VLVl8bjM0XwRI727Mn6gxVpeB_iweBuo5dnOynrtfBkQc7dRbfrL1cdtuCJoK3avxDr28REHmDgCf0leiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سود نامتعارف خودروهای مونتاژی
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/460730" target="_blank">📅 20:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کنوانسیون خزر و زنگزور دو لبۀ قیچی علیه ایران
🔹
مدت‌هاست ترکیه و آذربایجان با چراغ سبز آمریکا، کریدور زنگزور و کریدور میانی را پیش می‌برند تا منافع ایران را از معادلات ترانزیت اوراسیا حذف کنند و با بازگشت کنوانسیون خزر به مجلس، میدان نبرد ژئوپلیتیک و تجاری…</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/460728" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460727">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjr4GZzArdp_b2V0qQp89qI5tbHYi7kLn5hMzlLm5St7iQBIMWVDWPfDtKMFPifjS4M4kjkHuVqZokkra0nB4cYz1PU8JBtENJF7lGPZKeJQZfhwk0mVTFG_3xxrLkKlrKpq-ZFIgOeMgFrkHmJdkBP3FEinktNlLw_GbWqTX0v3nUJGgnY19Wp-o3aIDElJc8ZRDs3pYw6iQczRjCGMxC_KsxqiirbH_oBE6bZHLjNZY4IcnoTc6VUnW6msonLzOI6bygh9oLggp7vOiZIzAuSU-ChQnDX99DkN_KX-ObO1nQQ-yDGbct9XrmNdRIPoM3maFBRTq4wLFjSYwnr5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چوب حراج ژاپن به اوراق قرضه آمریکا
🔹
بلومبرگ: آمریکا نگران بازدهی اوراق قرضه بلندمدت است حالا در این میان توکیو احتمالا برای مداخلهٔ بی‌سابقه در بازار ارز، اوراق بهادار خزانه‌داری آمریکا را فروخته است. بازده اوراق قرضه آمریکا اکنون در بالاترین سطح ۱۹ سال گذشته قرار دارد.
🔸
یک ماه پیش، وزیر خزانه‌داری آمریکا برای نجات ین ژاپن از سقوط حاضر شد دلارپاشی سنگینی در اقتصاد این کشور انجام دهد تا توکیو اوراق قرضه واشنگتن را نفروشد چراکه این اقدام یعنی افزایش بازدهی اوراق قرضه ۱۰ ساله آمریکا که تورم‌زاست.
🔹
حالا آمارهای ذخایر ارزی وزارت داریی خزانه‌داری ژاپن امروز منتشر شده، نشان می‌دهد که اوراق بهادار خارجی که ۷۰ درصد آن اوراق آمریکاست در پایان ماه آگوست نسبت به ماه قبل، رکورد ۸۷.۸ میلیارد دلار کاهش یافته است و این کاهش تقریبا با حجم مداخلهٔ اخیر ژاپن برای حمایت از ین برابری می‌کند.
@Farsna - Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/460727" target="_blank">📅 19:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b39c9b653.mp4?token=KcaPaMAApLrWOeUYGPbAolWcfpjmuYfFbE_c6fYSxrjqB4xXS6_I_U5_Apif9dV3S2xiWKvEOTLpOByky_Uow_EqbxWMNiEmL-WldLfWJmKC5TCqIRgwSzybpsQoH8-0XjAnIsn2gk80saJU0nYBf37xUMaIQIBtw3hdx8Vqksq7KnaUJTwS9uZosVq0OssnFk2M_VnGrrH7MvACPgaO0LTxo7J_uVb-HwVp5w7A4uSO-zKHrupuA0xriN2UVcopPFtWKRxp9zwOZz4Ort9Fv71UY6gWmAwFedfqtBTGmY7AFiKa_uxQL170N7_JYJTtb6bnPX0gOus9y4khabDspg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b39c9b653.mp4?token=KcaPaMAApLrWOeUYGPbAolWcfpjmuYfFbE_c6fYSxrjqB4xXS6_I_U5_Apif9dV3S2xiWKvEOTLpOByky_Uow_EqbxWMNiEmL-WldLfWJmKC5TCqIRgwSzybpsQoH8-0XjAnIsn2gk80saJU0nYBf37xUMaIQIBtw3hdx8Vqksq7KnaUJTwS9uZosVq0OssnFk2M_VnGrrH7MvACPgaO0LTxo7J_uVb-HwVp5w7A4uSO-zKHrupuA0xriN2UVcopPFtWKRxp9zwOZz4Ort9Fv71UY6gWmAwFedfqtBTGmY7AFiKa_uxQL170N7_JYJTtb6bnPX0gOus9y4khabDspg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به ذوب‌آهن توسط علیپور در دقیقۀ ۴۳
⚽️
پرسپولیس ۱ - ۰ ذوب‌آهن
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/460726" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460725">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPDVJV-_NaU2e3NnwX0BKrLOw8evDJsBm_b-nM1FeM8732dYlUMEZszQiWbtuFUbKqcIxqghDWk-bmO2RZhrAeiofFgwZjrNpkUKGlQ1y_GpiTUH1yTau-mAeh4p3VmkJp5vQZSY-zbsg34m_rem9gbAGzb_Jdtpx0M9vHSfLAugTJvG4ekTV0CDP31dbjZlFCTsAsyMGhB5XQFJ6VbdnsDHjnXmgq-SXLQ_tXkmxi4jaML2a4pQED-Su6_X3Vjpq2E0Qh_8eTqbpXNdwrvgmh6_f-b9jJF8IuXS4AgHeRMse1fUILNEDSib45VriUlqqXJaKIPeDQP64kHOqQt3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساقط‌شدن ۳ پهپاد عربستان در ۲۴ ساعت گذشته توسط یمن
🔹
سخنگوی نیروهای مسلح یمن از ساقط‌کردن یک پهپاد وینگ لونگ ۲ ارتش عربستان در یمن خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/460725" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460724">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f06863f5.mp4?token=gaci01jtqfOwmjGuMTerGtln2Lr99UYCVrNYO7A2aNrZfNAR5kuZF7ajRQPe9mfKlRsBGWRmnf0wLX4NZusD4XpQRzBy_xx7pBuXuTikNhYMKx8-xYATa0e8wZLBznifxEaJpalglNPCZgsCjP58_Zg9XSaIOIx6M6Enu6VTRmcb5Kwcepa0PC4VwL9ouDmgScF3YxNUkDqXLVPGvftvynh7LxK2T57S0Pkghj2N1rGPKx7DkSAtJVJ57wxVYGjofQhFr9lJ2I7aXWY7zHvavFOejOqO4Qvqo27PwRdcHNla4uGX6H7o6Tha-nI3P9DpT9XE0DNtYbsS7B_5Or5sAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f06863f5.mp4?token=gaci01jtqfOwmjGuMTerGtln2Lr99UYCVrNYO7A2aNrZfNAR5kuZF7ajRQPe9mfKlRsBGWRmnf0wLX4NZusD4XpQRzBy_xx7pBuXuTikNhYMKx8-xYATa0e8wZLBznifxEaJpalglNPCZgsCjP58_Zg9XSaIOIx6M6Enu6VTRmcb5Kwcepa0PC4VwL9ouDmgScF3YxNUkDqXLVPGvftvynh7LxK2T57S0Pkghj2N1rGPKx7DkSAtJVJ57wxVYGjofQhFr9lJ2I7aXWY7zHvavFOejOqO4Qvqo27PwRdcHNla4uGX6H7o6Tha-nI3P9DpT9XE0DNtYbsS7B_5Or5sAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی پسر‌بچهٔ مهمان برنامهٔ محفل ستاره‌ها به آرزویش رسید!
🔹
اقدام جالب فرماندهٔ سپاه گلستان بعد از دیدن آرزوی جالب پسربچهٔ گلستانی
@Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/460724" target="_blank">📅 19:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460723">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
*ببینید/ توانمندی درآمدی شهرداری، پیشران پروژه‌های شهری/ مسئولان شهرداری تهران، از دغدغه خدمت به شهروندان در شرایط جنگی می‌گویند*</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/460723" target="_blank">📅 19:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460722">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJvbvdxzGzwDbSZY7lNdeIzgRMjSQwXyQTyKLmjAssROr8YHZQ9NNDQhTUoR8Cpzp6Zt9SVMbBZBTDYZL683dz6vWzKC-c2bJu3MqKlck1XqTAQt60QYQKJRp8rImU20RdbacC-nWa-5wQJLX6yuq3vY3bazHmaDLSuCmfnssAR2S2GkTSLSWBGCJsDT1ejh76T60UiM0Ku8BkqagsogZJLjsxhvMJ8Kwx68IgAA7kkhYMi3PZA1lg3tnGvde0hcI0ZMvy78LkpExvoxsR9U7i9GW2qJ64EPJlFt-XoL4hfSeaaRp-jnBD_Npfk7b9d7lhZjh0jN8CnXDu7KXEc78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
با کفش ملی،برنده شو!
❗️
جشنواره بازگشت به مدرسه فروشگاه های کفش ملی شروع شد.
✨
تا 50٪ تخفیف
🎁
قرعه کشی: PS5+دوچرخه+120میلیون
📍
خرید حضوری از 220 فروشگاه کفش ملی سراسر کشور
خرید اینترنتی و چهار قسطه از :
🌐
mellishoes.ir</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/460722" target="_blank">📅 19:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/460721" target="_blank">📅 19:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460720">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLySZALY5XX8Zr5sEd6Z9YIaUaSwrgywYQebyvv8Zz2-4QyQsCRrkMOORoC1wXYobZoHX2GxB3yVwVeWA49kpG7skXIYvGgenLSwUx5Q_oYxnhzVu7tQAQEFZRhPpeJWUjJtzW4rXaSvjYqIusdIdpBf-v95ONARFrodp6SU5EzCXzuxnJ7tAmIKcXwCCTyRMotxfrRkfW23B7aXnBOP6Uh3TeAq5hBrSYjTFMObaZ7jvxMBej1V-RTteKEZOt9F6devaRkUkpVNSSi9zYqcHImgO3S0Lllb6dgL-jBpPsC9y76ikCNUZkeYdhK8NBjxET5kVdAAvXqqi8C1Qmiw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایزمن زیر موشک ایران و تحریم جهانی فروپاشید
🔹
گزارش جدید رسانه‌های عبری نشان می‌دهد مهم‌ترین مرکز علمی-راهبردی اسرائیل در آستانۀ ورشکستگی و فروپاشی کامل قرار دارد.
🔹
یکی از دلایل این ورشکستگی، تحریم موسسات اسرائیلی توسط محققان بین‌المللی است.
🔹
همچنین کمک‌های مالی اروپا به محققان اسرائیلی هم ۶۷ درصد کاهش یافته است.
🔹
در کنار تحریم‌های علمی، حملات موشکی ایران به مؤسسه وایزمن در جریان جنگ ۱۲ روزه، ضربه‌ای جبران‌ناپذیر به این مرکز علمی وارد کرده است.
🔸
رئیس شورای علمی وایزمن گفته ۲ موشک ایران که به این مرکز برخورد کرده، بیش از ۵۰ آزمایشگاه و تجهیزات تحقیقاتی را به طور کامل نابود کرده است.
🔸
او گفته خسارت مالی این حمله بین ۴۰۰ تا ۵۴۰ میلیون دلار برآورد شده و حدود ۹۰ درصد از ساختمان‌های موسسه در این حمله دچار خسارت شده‌اند.
🔹
این حملات، وایزمن را برای نخستین‌بار در تاریخ خود از فهرست ۱۰۰ مرکز علمی برتر جهان خارج کرده و به رتبه ۱۱۱ سقوط داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/460720" target="_blank">📅 19:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460713">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4el1qVV5thAkuvfjx38a0if2SB3pHsUHFC-4t_Bzv8Rkzq5dlxmqDshx4Tnz4tA4ocN6iYB7M1EgMYC31dHWj2fqg1HmcPtg4W5Npa2AuVxQHm1FTRm7CbOn9FflFuWFkBI0O9QDxLj5dvoG7QrshP15BsUzHeGc6_DnM9cImDq7wmHBW5PWBoHhKjGOz4tD1Jk_NDyKnhZgNlIMWCRMNvBIeIOt_Fy_xhl36h-HSkGgy84zhlYFa1hWT9kepxwIFMHYQZ64R47r5nhQxAJLNqfxXTo8vjQshvHEyUtUZgWC46EkWy5DKGDPyEzh_vr8FIaL28c2XypgOTvK1qVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpBVp36Y3TvDD1sK6dFkyla7Hi5chXAdGCrAc8HJIcWo_Dn50VsndJXJFVc5ZmxIm2FUoNLOpysQotrpeYFmwyzRo4J7uP-686zLi6PtyK6FMsiEfrHkcV85_Nv9N4Zl_V8HarlUswsH3QmVnFChoWzm6zgUvuDidCnbicY0n3xV-25b-j9__7RTIhgYRskSPbUVsZvvJxoQHCJHrNLZTVqwy35OyvbSJAERjIFsjHJ1HpTKnMIsJqXzhSN2N1la2cfIkJW_rFxjTy9HlQQRUCzjj3jTjshnsJQSCW2SEuYekbw93L_cjgnkX1ojWgx2W73J95jTW6X0gmTWtiB9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jMD9zGPcsfpPFqEVPGufsqBz9WK0yRiQFyETiwp3kPxS0ObQyHDQBxXYnpSglplqLANltSJqq3MVZhOhgiqiqYj6CUjFUFEwve2DplhVwfKm3X3kiw6aEkRJAtT1CqacreVTYX80zdxDwfme-iUpPYhJcyNPGLJN0ogRteTUV-RvvU0w-deBfR2JtsX0FNNfQi9AWFSvXut1uvaYLwDXdQJyMNmjhzH9LDWT-TGnpanVD_9y83nvDy31JjMV71x-mb0y8ChxnmrE4na0RACmOC-_oVxdO4cIW88z9Yl0ea3tr_gj-6AkmmvXmqRUtKZDVeZP4r2zGDgC2padXtWt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bn585_pz3vhgqR1ncBqlrSPCW30KkT5T1o478M0YTz_fCjVsffSjCtlwXBZ3jASUixHpXzPNcjuHbedu4Ct2JCrlW8I5DInAKpxmF7qY5ULXXS-R-pFLtRKzUepz7zXRNP7816z5U8c1jKW5dq0YUtBJC9H9YrQyxj6t_UHZEHFNdweRuT_YKdTjN3i4FInEu_ymTRvCip1RWBau1f-Kfe2DzqiTtrJ3wkof-rNN9WOt2F7_EDefmFeZl3aQqJvaX81ko8lyLMcTDpLmM6N3uzCnAdoMbeiDPsqnLsu1pGWIu7207jLNOHLQ1LZXcGIgL_kP_mlw6sVdbmYveNi_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TV3gP6uvJoRvKmUsGCrXgXRwwdc05Gts_luziHXQIIBdfcqdV9OkU4TqJRzJkINRoE1z3rmGsL6B_nk50mck_j3wiKs9w3_2jh9kk3ki0d6WSJU-Ykr7VPSWao7eImastrfs1jXQPZ3P1ZvYgoLJuFNGEztWjh1lh3a6KZheu9KI9_yq80ueJawIQr4kyrqO9UD1PhZMPz_efsV3x458RYwvTYN1e7tHGJLYb5h7qbjve5pn-QtEBcbscTBxRC4M5xb8Y-NyxH8GCuuP0E90xUnjO2PnGeCfB9fqrqixXJKNdyj8oJ5q580wtWQPLZ7qa9tfQihNJrcwJIOMZImKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSMYvXgsIdlslwXAHj0Uk45Jup9rC0E0pMbz4SMNPHdcqq2QnFYz8ql1KFUDuIiFFw-tMtQPoQx-QEiBasIhQ3GIfWFAgZe3Wue5BBypkaWK7OVMeIq3YnEUPPwBIG9hqA3URunkCjgfZ46g1YgUyqeTxWLZ2M5jkbXeQ1YMZHawFzLx5o3xp_a3vw4F58s6dQlZ82fVKm7UYWaU6UF5i8r9ywtV_sWt9ky9_zjpaYCJK7vgWragriX2uFOVqg4F2zkjuAmYua2ZwO2IHM8plKTJix5vpM9yFMJiwz2XpEn9gOY_vmY2MaF4R0EVt7jf0RspHB5XypQtawe79fGzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/maugZH5BdZ1Kh7Y7pn1dOYdYZJZVTbZR4qsOruez0UQYaCxIbPnD-q3oQOK06MnOO9LIFv12_ZjyrUv1myJhLAp6M5eyy6p9zrXZS7pRXegdcv_VtDCcdghBmxRx8_p4sTKlJAqjP7uFsCEc4LustFLBw2XuBNDPA4HUO7MdE_jYverctWJU5iEplC17IVcxolR88dUXiLxT_NgFyaLG9NsCY80HNtl4Wqmo9IF2USIr3FkxhlGGg2JSgJMMAe-RYrfiVXpkUyI4LJ53AAy7OvmhM_ZaLQ1jeODIDo4sd4oOJhMCtE_y0CvxxVvutu6JjJGTL3GjX408gu7pByFmvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن پسته‌چینی در قزوین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/460713" target="_blank">📅 19:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460712">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02cc1840b5.mp4?token=Pd340Xm-DRgjUt22AbR0lSeeHXW_hX_LLRTxUQj20GAUKJvTq9SMjxHhxjUkVdndpcRIKfWw6P3QE7aN-ny-qvBncdf2SSplrtxDeu4J7MJZquxiv7fbmCQkXT2qhWg7RD9sow5J9VnLt9NR6EHxkEpEsUI7YfkK7gA3y0z8YEVZoMZgfbhXUuUfqfQ6JL9ESbwFMrEx0cdqmU5K0w6fj9xRjhDtYK8XTlPr-sQrQe4uB8RDzhhccMWJ92f4A5ztwYuX-VyQPoysudc-6mSrvVkXgaexKHhI4V1WySFGBD7Q0gVl613hK4fW0x_xM-j-lGxOchjmXZL10NU38NPaHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02cc1840b5.mp4?token=Pd340Xm-DRgjUt22AbR0lSeeHXW_hX_LLRTxUQj20GAUKJvTq9SMjxHhxjUkVdndpcRIKfWw6P3QE7aN-ny-qvBncdf2SSplrtxDeu4J7MJZquxiv7fbmCQkXT2qhWg7RD9sow5J9VnLt9NR6EHxkEpEsUI7YfkK7gA3y0z8YEVZoMZgfbhXUuUfqfQ6JL9ESbwFMrEx0cdqmU5K0w6fj9xRjhDtYK8XTlPr-sQrQe4uB8RDzhhccMWJ92f4A5ztwYuX-VyQPoysudc-6mSrvVkXgaexKHhI4V1WySFGBD7Q0gVl613hK4fW0x_xM-j-lGxOchjmXZL10NU38NPaHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهکارهای پلیس فتا برای جلوگیری از کپی شدن کارت بانکی توسط کلاهبرداران
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/460712" target="_blank">📅 19:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460711">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6ucUfsdHR_7DpAkXSmnqbWMjYXwChlMYTsDHKwnrlPW3KVAsBqIKWEb99QzgsDKBi5W4DMrbmE3TCaeHBdtG1jG9L2Qzz3w3obz5zsxYfiRe9oYxrZyuKoZEE0zGwhVC7ZwWMyefMH-V5nSiy8dbDNOIYD6eYIzPnNP1Ty09jbC2f9QdcjeoPd3xEeLWvH0geuI368zMc6PSs8ndqmtb7ER81xZbLfJ73FCrNkkhO0ePJy62NBDvAOU4fWryXJV_g7HWYsJisH1i6ubWIftaeKD8uvajp5kRBng0fb-OSPkwdWvWeyYCvfBvpLJ_h4L2uHrq5XzOzn94UrZFqAXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت امید مادران شارژ شد
🔹
معاون وزیر رفاه: مرحلۀ پنجم کارت امید مادران شارژ شد و مشمولان می‌توانند اقلام مورد نیاز خود را خریداری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/460711" target="_blank">📅 19:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460710">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQNr-NzVdmZM772--hZA7S5ecBQ6ED-VsdWwfYZe5Bl63-p8fVK_lcgW352dHjtsGTYJiPomL59yzhafhzdsWbwQ-ffbz7kKOJvBalthyguH2fmVUl47UZMAOwggjccVzlneUKQeHX_tm786WCVxUjPJxtZRrguAoSZd47zGqCBINJ79RB92xXhiD-T3A27YbaPqxpbfiJzSXQ9M9uyyz0sMqKGa0i9uayE0f3LgIuCyiUCt_LfzP-gF4h-Huzm8ZVThKHyWQEp0l70CEu2wWFE28FSFYS-i6T4HyrD2pStVHtf54DK8gHanSli--5IsFgcaFlXROAZX4Zy-ImGK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان: تاوان جنگ‌افروزی اسرائیل علیه ایران را همۀ جهان می‌دهد
🔹
تا زمانی که گره تنگۀ هرمز باز نشود روند افزایشی قیمت‌ها در جهان ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/460710" target="_blank">📅 18:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSuD1_9x2l9eFDLnrH0KpRktwFCScjJj-vhnLRt2vsgo76Uj5rjdhH6YF2tymU7fHc7fqRe92njhuZjTSRGpWmssgrYytAxGyQ2TCv2CFCVAvoBOfl4_BoOdV4iubGLEIn9PtTwZtX7fmYMSwGRNUUYGKJPl3jtTldmTgnh70Z_uxXjxPIWvZBiqsASL3DARXOaL7lsT1YgSz6bA-4VXrWr0dfyZNYLXlpqqvElEMQTj89uk9qG_BSYAWjpiQP7g8rhTMlyz3zAYdlEWKsdG4FoK-qpkKf2r82b9Nr7SoVdkmCLCCdVKj3Hh-VfZViPb3BsFrsKzCj_gs92bgWCChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجاهد: روحانی به‌دنبال بازگشت به صحنه با دوقطبی‌سازی است
🔹
معاون پیگیری‌های ویژۀ دفتر رئیس‌جمهور شهید: حسن روحانی به‌عنوان نامحبوب‌ترین رئیس‌جمهور تاریخ ایران شناخته می‌شود که کمترین میزان مقبولیت در بین سیاسیون را در بین مردم دارد و از سوی مردم طرد شده است.…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/460709" target="_blank">📅 18:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460708">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df16f61f4.mp4?token=TviSMtFB6onGVN3j0sWwMIkOsihJbjB2pQ1cchs2MIpCmQbFQeeMl92FTHV8_I-r5kRxR9MYHJzXnt-Aql2aBphSvzoA4e-QTWofBVQITD8mtEUFwWuMBhoxIu4nmSt7JRqTCd80c7LOoS8yh-y-MeLyj-A8qTtFn0cN4WNi_m-WKfjjYrExKDVSF4z3Er17H9pV2bwtMx2zmEj_gyLI4qb9pmHYv9hczCu0463_F_94CWLjEFBm1akXtU_RhxdIgTCd70gehDBQCdWzw5Ni2GlYiXuFX9rHzCkj-VoqfQyjtNR57i5fzowtzv8l1Zftx42R5ukYOb88wGI_Bkol_YphuD7lAUykuIWdsug8pZSgTrkdKATpkjKWGcHwl6xVxshVfRBcjDJjKQBMtwOulKgpoZysblV2w3pnAsjutBVf927gcf76_Lcc5iqGl-LFv1iJ_wz7qUr-GTuC-9qBtwk9OlpNB_sGdHThw1VcJ00-HkjuOBWleGIe8BGc08mQrJuxZTy44lp05IRMLcF7JyVlWCLgaJMC3I8a1XfFFGVoJfQmhG1Uu0BJ_ScN4GxWBTg-glPGLRsKz98EX-wj5Hp5bRcCTE-ww_YJscMsuwHbSk0OSgAVY56RJP3awFR_aUKD4r7xiOmHRvGy-RYx2wcm-gjUilhe9U81y_Sotiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df16f61f4.mp4?token=TviSMtFB6onGVN3j0sWwMIkOsihJbjB2pQ1cchs2MIpCmQbFQeeMl92FTHV8_I-r5kRxR9MYHJzXnt-Aql2aBphSvzoA4e-QTWofBVQITD8mtEUFwWuMBhoxIu4nmSt7JRqTCd80c7LOoS8yh-y-MeLyj-A8qTtFn0cN4WNi_m-WKfjjYrExKDVSF4z3Er17H9pV2bwtMx2zmEj_gyLI4qb9pmHYv9hczCu0463_F_94CWLjEFBm1akXtU_RhxdIgTCd70gehDBQCdWzw5Ni2GlYiXuFX9rHzCkj-VoqfQyjtNR57i5fzowtzv8l1Zftx42R5ukYOb88wGI_Bkol_YphuD7lAUykuIWdsug8pZSgTrkdKATpkjKWGcHwl6xVxshVfRBcjDJjKQBMtwOulKgpoZysblV2w3pnAsjutBVf927gcf76_Lcc5iqGl-LFv1iJ_wz7qUr-GTuC-9qBtwk9OlpNB_sGdHThw1VcJ00-HkjuOBWleGIe8BGc08mQrJuxZTy44lp05IRMLcF7JyVlWCLgaJMC3I8a1XfFFGVoJfQmhG1Uu0BJ_ScN4GxWBTg-glPGLRsKz98EX-wj5Hp5bRcCTE-ww_YJscMsuwHbSk0OSgAVY56RJP3awFR_aUKD4r7xiOmHRvGy-RYx2wcm-gjUilhe9U81y_Sotiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: سعودی برای جنایت علیه مردم یمن مجازات می‌شود
🔹
تجاوزات بی‌وقفه علیه یمن همچنان ادامه دارد و دشمن سعودی تشدید تنش را با انجام حملات هوایی و ارتکاب جنایاتی مانند کشتار در الجوف و تجهیز مزدوران خود به انواع سلاح‌ها ادامه می‌دهد.
🔹
تجاوزات…</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/460708" target="_blank">📅 18:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460707">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQLXz4KEWijWoovuX3KqZkA8IB3TJh9opzro1zs1z4kQ1yqbc9EM1Hn3uwhQyGv5QI_7f5Mj3bo8z0acFaykj-MKH2kEj3CbxWWSAFlonJ8hyX6YPBgqaUTJy9N0PFebUQ96TypTMUsz7iAqKX1S0hX4PG7nD9NFC8Ga7jsC7uMY5H4VJXZ46LdFFQfbn4CS3hYBLDdbjiokOEn6QThBNxeXsg_i0O8VQ7fKz5R-HKvCrzskx5YryZ9v1DSZ5Ij_8Y8XRlj0yHHojQvkD9GwTXH_RrGh-KaNeYQXdDSgSmfJAeuFUzsbQkVtGjw59febkCqUc3I9VWXUpfj8l3yIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان توقف ۵ ماهۀ واردات موبایل
🔹
پس از ۵ ماه توقف، سامانۀ ثبت سفارش تلفن همراه فعالیت خود را از سر گرفت و درهایش را به روی واردکنندگان گوشی تلفن همراه باز کرد.
🔸
از ابتدای امسال یک میلیون تلفن همراه به کشور وارد شده؛ درحالی‌که در مدت مشابه سال قبل بیش از ۳ میلیون گوشی وارد کشور شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/460707" target="_blank">📅 18:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460706">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRYNfunlhqbI2xTIzRjMEbTnseLeAx1SMmGDy4G6fmy2x9F7GOKHZw5TW16f4TgM1O_JXS1DxwmK8Og-0SToiwW1zXQV6t5m60mOL5zvAtPegTLmLwQxHB6ZIaXVnHCX82AEDiLwZIo05LVFgDj1mXpx7SdEquGdqj1RSKE14FsER_tLr-pul5bOpW9n6I7V2vfGRpXQqHOFSge6BYp09jWOcrta_erqAf6lCyjzcxPk3POg1a3r7Tf0o_QHKgvQx6I4ZjfdKs9WqIBNWmnktP4URscVc-fvu3i-zXKZS5_pMGxiusTfdxkuHlC0Pj9k7QtE7rKroaiMVZsoMNGgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خاطرۀ سردار علی فضلی از حضور رهبر معظم انقلاب در جبهۀ دفاع مقدس ۸ ساله
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/460706" target="_blank">📅 18:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460705">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHw1uxGUGA12_DyyO2fMxd6gJ0EcA6zFjd6_5KuJACvf7zAP7IW3zSWbQo77s2Vu1ONkK7l3ETsXlKay3ib8unkqmUbU27-kx33KO5KGoHCIW4pslLZhQ7JDZiRnlQqPZzNyKypf9e_IY7tglzde97Bcy_mk4qPpmGmS5zcGpd2lmjatG01Id6bsItbAPfE2fFIwF--Ec8sGCW5vqCT7h28w12TYdyTLzWA9LLZD9gCgvU9Fs3aB2cWWunNQV3Eojfcu1hk3eA5nge35QY_AHZ8BAkddKBvZTiVpmvDuiWNiz-TR8IrUoOjkNxIk_otoxoBZTGUjo0DUl-bggJdAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: سعودی برای جنایت علیه مردم یمن مجازات می‌شود
🔹
تجاوزات بی‌وقفه علیه یمن همچنان ادامه دارد و دشمن سعودی تشدید تنش را با انجام حملات هوایی و ارتکاب جنایاتی مانند کشتار در الجوف و تجهیز مزدوران خود به انواع سلاح‌ها ادامه می‌دهد.
🔹
تجاوزات مستمر سعودی علیه یمن بدون پاسخ و مجازات نخواهد ماند، و دشمن سعودی باید عواقب جنایات خود علیه مردم یمن را بپذیرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/460705" target="_blank">📅 18:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908dd4af2d.mp4?token=OHHLOEo14EVv8RJhcGmH-6uWWObiesF4kS4igIFf9mBuHdHp7yvyMBtHouyQPnDFUTMmSlSCeXmjdAxsPl457ENgnhUNZfKFf2m7zh8OCaJayRN6IEcF7PJMRtxl-Vv6Q75TNrxOgl7Jm66qOAw2562-8krR-RdmGjyjxNzT7TIOmlvtc_wPzY71KSocd_AxpaFSiTW3_Hv2fJODCZM-MxascfRwgcw9wgJn-a9LugI8l7UZNixo4U1p8OzdYW6fzIDxD22Zpmt_CgEOwY41IJ3HxsjLMTiZFIq2U2F2CmKsbTwOcwvtjQATtd0D7bM8dR7br2gHL_WFyv9D7vI8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908dd4af2d.mp4?token=OHHLOEo14EVv8RJhcGmH-6uWWObiesF4kS4igIFf9mBuHdHp7yvyMBtHouyQPnDFUTMmSlSCeXmjdAxsPl457ENgnhUNZfKFf2m7zh8OCaJayRN6IEcF7PJMRtxl-Vv6Q75TNrxOgl7Jm66qOAw2562-8krR-RdmGjyjxNzT7TIOmlvtc_wPzY71KSocd_AxpaFSiTW3_Hv2fJODCZM-MxascfRwgcw9wgJn-a9LugI8l7UZNixo4U1p8OzdYW6fzIDxD22Zpmt_CgEOwY41IJ3HxsjLMTiZFIq2U2F2CmKsbTwOcwvtjQATtd0D7bM8dR7br2gHL_WFyv9D7vI8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برنامۀ چندسالۀ آمریکا در مرزهای شمالی ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/460704" target="_blank">📅 18:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460703">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKWUzCv3kLtK-L1SUrhFJgMR_JbwgW7iDGlE_7u6ui6ZxT-JU1r-xHZYIKxXEJrhPDxApIfMPXkpcL5dbc8l1EHokjBEVKEJJuF1tpQ83NXDL3SmmRkFEgJL7HoZCXbMtuohAiAOBFcoDaQIxexcYQIOOv-Ly2PV-VpDKE2o7Zj3gIrfLwWkUceqJngITwKojev2O0cKPIyWYjGHy78OwfZVZR680yxZER118TV3onmMwnUvzktamcauiJ2QiPbIa0_MH59El5xqn9g_APAX7XizjLnxAt8XYueoQPaZ6JzHrNPr-JSeeYed0EYH98u387KlFVHAwSC75jB7z2C-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال نتیجۀ شکایت پرسپولیس را می‌داند
🔹
با وجود اضافه‌شدن شکایت‌ باشگاه‌های پرسپولیس و آلومینیوم به دلیل استفاده از یاسر آسانی، باشگاه استقلال همچنان قویاً معتقد است که این پرونده سرانجامی برای شاکیان نخواهد داشت.
🔹
طبق پیگیری‌ها از منابع مطلع، باشگاه استقلال و تیم حقوقی آن از به نتیجه نرسیدن شکایت پرسپولیس و دیگر باشگاه‌ها در کمیته‌های نظارتی فدراسیون فوتبال اطمینان کامل دارد.
🔹
به‌علاوه استقلالی‌ها معتقدند باتوجه‌به شواهد و مدارک موجود در صورت کشیده‌شدن کار به دادگاه CAS نیز این باشگاه آمادگی کامل برای ارائه دفاعیات لازم برای اثبات قانونی‌بودن بازی‌کردن آسانی را خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/460703" target="_blank">📅 18:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کمین رزمندۀ حزب‌الله در مسیر اشغالگران، ۲ نظامی اسرائیلی زخمی شدند
🔹
ارتش صهیونیستی: یک رزمندۀ حزب‌الله امروز از داخل یک ساختمان در منطقۀ شقیف به سمت نظامیان ویژۀ اسرائیلی از تیپ گولانی تیراندازی کرده که در جریان آن ۲ نظامی زخمی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/460702" target="_blank">📅 17:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460700">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAg9hYdR3_T2lPOl-SEa8xPpK0IsLLCiJt3YGKYoNPEwFhfyfS4IFG5t20s0fXxxlpaPk5iwipmHyALw3vRqw6eq_zWylZEwednkeSVflvwDLpGi7k90MAIUKkQo6j2qPwQLiPWRPNrurVWSYOwi4cOd9FkZleqBojIubKJhwCuTZT5vroO1reD_fvK2sMrXQNYi8F6jje2slYrkmZw96bHxdKv6KkyqShDQCuQjuP9HmQkJpvVsRAOgkgqQ3iz9RhNNEgmFhiKG2G-8h1nzeNNLBgBJ1emWX-8F9dnhJJfJPtXFIQRQI5pVUi_HXBmihP-NeWxzCrCrt-kGMWjw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHRbFg_OLx5I0JdI_RLIVvTX-Msp3vp90hmhs9rDmOpUtSP7A3Z7hMxfHPuGmCntrAsVvqUEC3SdavKcAghbiPSxJNf__-M3Ka4aN5wJMB4Fa5-PYXJ0NjaAyqQmrPMF9TRblc00fKKYTdAN5IKrHJdR5vAyJ_1QnEw1IEvX-isrHxeOo1xJiszWB5XXon9LCTLolsmN437rAsrFOOZ6o09Wpt8jKuLDiGBYyjp-9M6vPtVG7ESDbQxqITBfwxI8C8d1eYJvjimAXEvaH2JG715b2fbaexWZPNfM4PcVs8tTV8R3ay48OLIfHTdKBhLSPCMncZTTmH4334CtdierGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلسۀ بررسی همکاری پیشکسوتان سازندگی در بازسازی زیرساخت‌ها آسیب‌دیده
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460700" target="_blank">📅 17:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460699">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe85c09791.mp4?token=dXoB40jGAeazCCF12K7ncXn7lawThw7yaJ0IamMyeyqFRjRWKECAOSpYFENViwDS-iZzAX0Q1VVV32ZLCRb5wDZzpOWD39oJneZ_TqjxIdYDJy0_Fec0ECRNHxyBW_iGWXfkozt0hthKABTWDbugQ36Iz-XW080m1vlfSsMwc27CdPswmshmtVHL496MXYb5wMkkC4ykZ7VlbcUFYaRdRgvvbND9e6UN9ZWI6j0pYOGgqoTyBFxuqbwtZn_p33gypHZTovnqkJHgRcQ-8IUj8WVFmlmSXOFtHkFrP62112w9-972UZ19IlHeuSOzn8wxFHZt9T612aeTQAo3UBV6Dqu53nvFs2Y36NRUVuYvQWUfMFqf77o_w4K3FqJAP7t-a3Sfjn9KHjb5P2vvyVDosAPb_TcwCd5CFrIYUt9SyXEKOCeirXtI_aOoYmDpbowdcXIF6Dniqz31ZNvFaaf9WCHbuqw3yXaR5rz_S3QUsSZWS0EimAk_rWbSQcorqq3JSZnEba9el9OvHxnCpwCqg7XaG117OmZWxfPb2lHu8BNKGax-ERYlgdgEXsxZWHvtdoUbcL5yRg_psfsU1GFVH7ItHz7ilh_ovUj6x_crGg3YS0Z4iPUc6LzylZAp1fjvtgSSZhIPQQxsRYEzVG-ZgFdjr5X6Y3E_XHN0RfInIQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe85c09791.mp4?token=dXoB40jGAeazCCF12K7ncXn7lawThw7yaJ0IamMyeyqFRjRWKECAOSpYFENViwDS-iZzAX0Q1VVV32ZLCRb5wDZzpOWD39oJneZ_TqjxIdYDJy0_Fec0ECRNHxyBW_iGWXfkozt0hthKABTWDbugQ36Iz-XW080m1vlfSsMwc27CdPswmshmtVHL496MXYb5wMkkC4ykZ7VlbcUFYaRdRgvvbND9e6UN9ZWI6j0pYOGgqoTyBFxuqbwtZn_p33gypHZTovnqkJHgRcQ-8IUj8WVFmlmSXOFtHkFrP62112w9-972UZ19IlHeuSOzn8wxFHZt9T612aeTQAo3UBV6Dqu53nvFs2Y36NRUVuYvQWUfMFqf77o_w4K3FqJAP7t-a3Sfjn9KHjb5P2vvyVDosAPb_TcwCd5CFrIYUt9SyXEKOCeirXtI_aOoYmDpbowdcXIF6Dniqz31ZNvFaaf9WCHbuqw3yXaR5rz_S3QUsSZWS0EimAk_rWbSQcorqq3JSZnEba9el9OvHxnCpwCqg7XaG117OmZWxfPb2lHu8BNKGax-ERYlgdgEXsxZWHvtdoUbcL5yRg_psfsU1GFVH7ItHz7ilh_ovUj6x_crGg3YS0Z4iPUc6LzylZAp1fjvtgSSZhIPQQxsRYEzVG-ZgFdjr5X6Y3E_XHN0RfInIQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر حملۀ موشکی یمنی‌ها به کاروان تجهیزات نظامی مزدوران سعودی در اردوگاه الودعیه
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460699" target="_blank">📅 17:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460698">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5ebc0865.mp4?token=Wa_R_G0twlWhdvVxis2a-NnGp9lKA4raCWIJGhJhVjit1pb01mPuIV3G3E4yZgVhDskiTAXD-0wvxDpaGg8hihtxmEqgs7KRPbxsN-JukQFDH5YmkB1kU0YaHJsD70C_5h0W2Xnu9SGFTJvRQgoGEtrhMZo1381GFgd8cGMm5jwAGxVa7VtpHttUJMjpntJxsH2AaXGyOhjXTUIdkbYTY7AnZwlr4ifoi5-bdoKz03DojgmDkxz9fSpX-mVd1UmCrgX8kv40pKAS9Ifysm7OXAq_-OtEBW5RwO1wWdUiMo-SiiMcmwEUbsSX-c11L5CUcGqNk0oupv2GF47WNhnN7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5ebc0865.mp4?token=Wa_R_G0twlWhdvVxis2a-NnGp9lKA4raCWIJGhJhVjit1pb01mPuIV3G3E4yZgVhDskiTAXD-0wvxDpaGg8hihtxmEqgs7KRPbxsN-JukQFDH5YmkB1kU0YaHJsD70C_5h0W2Xnu9SGFTJvRQgoGEtrhMZo1381GFgd8cGMm5jwAGxVa7VtpHttUJMjpntJxsH2AaXGyOhjXTUIdkbYTY7AnZwlr4ifoi5-bdoKz03DojgmDkxz9fSpX-mVd1UmCrgX8kv40pKAS9Ifysm7OXAq_-OtEBW5RwO1wWdUiMo-SiiMcmwEUbsSX-c11L5CUcGqNk0oupv2GF47WNhnN7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین وضعیت نفتکشی که در خارگ هدف گرفته شد
🔹
براساس بررسی‌های فارس، عملیات اطفای حریق نفتکشی که روز شنبه در حوالی جزیرهٔ خارگ هدف حملهٔ آمریکا قرار گرفته بود به‌پایان رسیده است.
🔹
همهٔ خدمهٔ کشتی نیز در سلامت کامل به‌سر می‌برند و این حادثه تا این لحظه منجر به نشت نفت نشده است.
🔹
امروز گروه‌های مختلف برای بررسی وضعیت این نفتکش به محل حادثه اعزام شده‌اند تا برای جابه‌جایی کشتی تصمیم‌گیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460698" target="_blank">📅 17:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ6LjWLssCW-4t5JZdbauztkcigmIxmo2XsRPN6l2cv8eQ6orzgpZq6lgfUmUdKmBkfn5CQNxFrdJL4rngTt2GUGKcnTtBfbId3DPvjthSv6HAZE3khUBisrSFMwcmjBNFI3JdVrB5Qod_o990qecO4kifNOqN3QdKJjcLOEjiEv3DqLm16Guas24kNUs6lTnSLHAi6X8erzxoGwjB_OB-4dm0Uf7VK7VWsWKMP6ZUHu08H9GVjRECG0LHxJprSFHPxwsd5lVmfpFe0Yc9-Ny2lXZiQsx7lELtzv71jsNakctValTUw1ppTQTmryOQLbGLWs4cx98bdemT_AnLw_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دست رد دیوان‌عالی کشور به سینۀ متهمان چای دبش
🔹
رئیس دیوان‌عالی کشور: درخواست اعادۀ دادرسی بیش از ۳۰ نفر از محکومان پروندۀ چای دبش، از جمله ۲ وزیر اسبق، رد شده است. @Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/460697" target="_blank">📅 17:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b99b0a2d.mp4?token=P0KPRB6kkgnAg9X-opTPImNHkZNn7uuiBNiG_0rTwtdDmAojyz1ZpYXO7ilCldSV0uAZPUPYl7ngNnCKpkTDOnUFFepp2isI4Ys3Sq__86VVeOaNcDGcaekRPktn3tAU0TZVbx6XOOOxILWL1TjEgqF53IoWoPmet-rOvKb9mnvyh-BEW7I2fQjj8sp7RaaJm6NVHTZ7bdOs9WAP1QcrTjj9m54Cn2QxzgJiBacc1tsThbV6ZgHmLqpRG79bM-PZMP31He_muiZFIoaKj1qtKSOlLyMFlsH83NlPsqnWruYnc4Guj8QDL4hy2027q2QFP25SbsLGSq8wBfdvMD9zxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b99b0a2d.mp4?token=P0KPRB6kkgnAg9X-opTPImNHkZNn7uuiBNiG_0rTwtdDmAojyz1ZpYXO7ilCldSV0uAZPUPYl7ngNnCKpkTDOnUFFepp2isI4Ys3Sq__86VVeOaNcDGcaekRPktn3tAU0TZVbx6XOOOxILWL1TjEgqF53IoWoPmet-rOvKb9mnvyh-BEW7I2fQjj8sp7RaaJm6NVHTZ7bdOs9WAP1QcrTjj9m54Cn2QxzgJiBacc1tsThbV6ZgHmLqpRG79bM-PZMP31He_muiZFIoaKj1qtKSOlLyMFlsH83NlPsqnWruYnc4Guj8QDL4hy2027q2QFP25SbsLGSq8wBfdvMD9zxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: وحدت‌شکنی از هر طیف و گروهی خیانت و جرم است
🔹
از هر طیف، سلیقه، جناح و تفکری، صدایی بلند شود و عملی سر زند که وحدت‌شکن باشد و تصویر مقتدرانهٔ ایران در اذهان جهانیان را مخدوش و تضعیف کند، بی‌انصافی، خیانت، جرم و گناه است.
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/460696" target="_blank">📅 16:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaec964408.mp4?token=G5a7a8mRkXoxlq2bE9LFi_c8PwWsO8_VXwUJ1Ym3-uaxs16cbc_85ClflUgSPRppjDwGquX2mBxNy1Kgbpqru5jtj73B60Nec7ZWjjqlnaqUVdOPr1m46u5IUIvgHsFLkeE1yKLYPXbJmBPB3auZJOzc4n41ob-fheiocN-lREId1H1E4aYkXVEeyPqyCYu4AHNQMlPaaCMsVSYDiEkoWFPyGuoKR3OvQ2vnB9Btp0E-1mB88UeVwgI8XDKITWLJ3i0EuaIHFf4rEjCYwSwef9gz2jzbQm4W00C3U2hu7Dfybl__q2Jviw373aJdhPTTf4XTOwjwT7mYfi-9AKV5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaec964408.mp4?token=G5a7a8mRkXoxlq2bE9LFi_c8PwWsO8_VXwUJ1Ym3-uaxs16cbc_85ClflUgSPRppjDwGquX2mBxNy1Kgbpqru5jtj73B60Nec7ZWjjqlnaqUVdOPr1m46u5IUIvgHsFLkeE1yKLYPXbJmBPB3auZJOzc4n41ob-fheiocN-lREId1H1E4aYkXVEeyPqyCYu4AHNQMlPaaCMsVSYDiEkoWFPyGuoKR3OvQ2vnB9Btp0E-1mB88UeVwgI8XDKITWLJ3i0EuaIHFf4rEjCYwSwef9gz2jzbQm4W00C3U2hu7Dfybl__q2Jviw373aJdhPTTf4XTOwjwT7mYfi-9AKV5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز دادگاه حادثۀ تروریستی خاش زاهدان
🔹
آمریکا از طریق گروهک تروریستی جیش‌الظلم در غروب ۲۴ بهمن ۱۳۹۷ اتوبوس حامل تعدادی از نیروهای سپاه پاسداران را پس از اتمام مأموریت مرزبانی و در حال بازگشت به خانه، مورد حمله‌ انتحاری قرار داد که منجر به شهادت ۲۷ نفر و زخمی…</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/460695" target="_blank">📅 16:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460694">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ca05586f.mp4?token=R091Z19PkM9_KD0AOa3FChRsgBgGU07X3Ud3Xjdd5xavuYixaXLKbvws1hOqH1jwuqOPHTuZn6o2ialrFO7wpGQZxlPl_pzcVFw4L70CHWHzUy0uUlrzpSDivz_ODVDa2RoCfkBDOJzxZfhRNOppjv164FG84sKrDvj9QyH7RKCez1qaUOFqLdVjBvZxcqg3xnYKqGP-qBxT9fs5icRnUhhBsj1qsu3NxCfspZSmGgRwF25puhIAp8UyycfqcdiFm9GY0z1hQW2_mO81rrDWt04V_bQFZ6aNUbckOgAu0lPa9k_TWNwpsIxo3UHev43NBCb6A8r68m-2tCiqiy1C5UyyQyYEwmHaZQVLvGayRg41Y72hhiXNj1H-_4dNN4t9Qc10hLiVw6YiYmASQ3IK13gN2EtvqjlEdIqXdjR0pSYPbeA8eu5CA6EmnFzMQn-uD_a8VhzeF0S6f2sGpXYIDap_yEZLWXn41OF0C_jWp_buItofQK2A0mRp-CO4vra_7spmAp79aAjfrBEeKMpPH38zqOA200x8yOb78A5pPOKJx9fufoWAI68KLEJiDSZXTwBhvMXOZ1TKS2rGdDy4-7ryUiNqvs4uPnI0ptia9GYfh1WonCGeiIEJKYG07GUTL2Ohc084lijzqWJIadbIzEoZYnMGKli1MW94QTbVO6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ca05586f.mp4?token=R091Z19PkM9_KD0AOa3FChRsgBgGU07X3Ud3Xjdd5xavuYixaXLKbvws1hOqH1jwuqOPHTuZn6o2ialrFO7wpGQZxlPl_pzcVFw4L70CHWHzUy0uUlrzpSDivz_ODVDa2RoCfkBDOJzxZfhRNOppjv164FG84sKrDvj9QyH7RKCez1qaUOFqLdVjBvZxcqg3xnYKqGP-qBxT9fs5icRnUhhBsj1qsu3NxCfspZSmGgRwF25puhIAp8UyycfqcdiFm9GY0z1hQW2_mO81rrDWt04V_bQFZ6aNUbckOgAu0lPa9k_TWNwpsIxo3UHev43NBCb6A8r68m-2tCiqiy1C5UyyQyYEwmHaZQVLvGayRg41Y72hhiXNj1H-_4dNN4t9Qc10hLiVw6YiYmASQ3IK13gN2EtvqjlEdIqXdjR0pSYPbeA8eu5CA6EmnFzMQn-uD_a8VhzeF0S6f2sGpXYIDap_yEZLWXn41OF0C_jWp_buItofQK2A0mRp-CO4vra_7spmAp79aAjfrBEeKMpPH38zqOA200x8yOb78A5pPOKJx9fufoWAI68KLEJiDSZXTwBhvMXOZ1TKS2rGdDy4-7ryUiNqvs4uPnI0ptia9GYfh1WonCGeiIEJKYG07GUTL2Ohc084lijzqWJIadbIzEoZYnMGKli1MW94QTbVO6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمله‌ای که رهبر شهید هنگام اعطای حکم فرماندهی به سردار شهید تنگسیری گفته بودند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/460694" target="_blank">📅 16:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460693">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68324108a9.mp4?token=lnw3LN-Wb9gaIFR7leyEyI7hHe5BJbVLgbr4cvgfQIDW7fzBHOyLChh7ZEz5ZgMTYhNpJov4BMRruccqcKcPE8Mp7o6Treo70Ee9mg2G91Jn8vEEorvaKaUcjBHAZbD_UYgcf9GVem9xqcfcyc6Q6ofA47IQLg05tkwi9MBlvx-R4wivvuitLsRerAMZP1TpthMMRzwgkUobUvYUBCNMXzJCSIOGzdDd8X-tVMvDfhxfahO67mkWjgKId22ougE4SADWDWb-qQWb7suyx9Ap3apjkEuHbBE_s-rsG3VYPJroM3wxdDCQC9zUpBsiKMcEQcSPERQNaJ_WxC5RuRrAPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68324108a9.mp4?token=lnw3LN-Wb9gaIFR7leyEyI7hHe5BJbVLgbr4cvgfQIDW7fzBHOyLChh7ZEz5ZgMTYhNpJov4BMRruccqcKcPE8Mp7o6Treo70Ee9mg2G91Jn8vEEorvaKaUcjBHAZbD_UYgcf9GVem9xqcfcyc6Q6ofA47IQLg05tkwi9MBlvx-R4wivvuitLsRerAMZP1TpthMMRzwgkUobUvYUBCNMXzJCSIOGzdDd8X-tVMvDfhxfahO67mkWjgKId22ougE4SADWDWb-qQWb7suyx9Ap3apjkEuHbBE_s-rsG3VYPJroM3wxdDCQC9zUpBsiKMcEQcSPERQNaJ_WxC5RuRrAPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ مجروح شدن خبرنگار المنار در حملۀ هوایی اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/460693" target="_blank">📅 16:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460692">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7v8t6uL8se1F8rWQ3JonnCTa1_iuRsujuu1lUKhJu_DYN5zkQEJKm6ALmeqDwOGZPA_8t51ji2HATaJXFC18g4iKh3YnrPTDn-OQeQRChixVm0FDOJ7ureQoVfpyqMap9M8qNCbYIY5WpIyzlSRfs9zuVlM2QK8081vMEZt-tBD5cXeA13RrGKDJknfn9M4bwM0y_7vouW3NF5KU4wKUJYD5vPyYWBaZiZCUwKXQQqoTZnZf4JMr1BTw6boV2EsBE80Ky_el0N_BViSgdW0ZhwH4AfcazCNjzyfLLuQ3ge5fuP7ORKYdymcWeJWSh7svpju3cNuSZ6wzniScXyqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدهٔ وزیر روی زمین ماند
🔹
با وجود اعلام رسمی وزیر نیرو برای پایان خاموشی‌های برنامه‌ریزی‌شده، گزارش‌ها حاکی از آن است که در برخی نقاط کشور، قطعی برق همچنان تا ۲ نوبت در روز ادامه دارد؛ در برخی مناطق نیز این خاموشی‌ها به‌صورت برنامه‌ریزی‌نشده و بدون اطلاع…</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/460692" target="_blank">📅 16:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460691">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duqkXm0zRtL2wS8bxFeP74DQyMT0xPdN7-Se_iL-iWLH3dyyy2YqwZ1ymD7TrxKRC8FyokmhFVpbmmJTLEfHJGyNJ07aXLaIbUXL5BDtHjFPOldvw6TUt0jIfacVXZam7pulbdGRZU7JtRaQ5jU77NoQrXIS4pgARaton0XHm93Jy7pQtEH0bo3WEeqbrSAqoaIJfrCZrbN64zqe5ZUETZu6f0DBDDF9eEru-lNZp7xKaHNTe4x9BZ6FR_RmtXAKbmRcwdVOlbiPUBUD2QRtrvsxtbknDcPujWxhAuHOX-jo7zBBuqIvurBKQ7CoWrc8JViC4ThtzZVO7gI3WvxBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدی: نقطهٔ پایان مصونیت در تنگهٔ هرمز «خصب عمان» است
🔹
معاون سیاسی نیروی دریایی سپاه: عبور ایمن از کریدور آمریکایی در جنوب تنگهٔ هرمز عملاً امکان‌پذیر نیست و شناوری که وارد این کریدور شود، پس‌از رسیدن به محدودهٔ خصب عمان دیگر از خطر اصابت مصون نخواهد بود.
🔹
نیروی دریایی سپاه در خلیج فارس، تنگهٔ هرمز و دریای عمان، با اشراف اطلاعاتی و عملیاتی کامل تحرکات شناورها را لحظه‌به‌لحظه رصد می‌کند.
🔹
تمامی کشتی‌هایی که قصد عبور ایمن از تنگهٔ هرمز را دارند، باید از کریدور تعیین‌شده از سوی ایران استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460691" target="_blank">📅 16:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460690">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3FAC-visSDzMgudMgIJolSVfOUJWvaJl0hsZvYay3cB4KLIcjWQ6Tx2v5m_h0rF9pDRcf9P03AewB5iDQUo63FwJtUmSV4owyEMgyXgcf3QPNMf-TlXwl8WUwHWCfPWPay1Jj1tdMcuBsx5nW3ncGbFSVQQBGUnrPTQKyk1RfJzWUmHYCLkValcHpDxpYsrHhPeTT2s_bwbYIZwTQzp2py3Nm-Ft70oEvXCMNdGk2w_kOZKI2au5P8J0uTJBdrlZMypm8_YuYtB1-2s3DYm3kLkjkmuz2t2KwKbzBL62TnKetXY3kdSk1pjhOo2tkvP50ZiswXCvgsDCPM0aMPPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای روحانی، دوگانۀ اصلی، «مقاومت و تسلیم» است نه چیز دیگر
🔹
اظهارات حسن روحانی دربارۀ اینکه آیا مردم حاضرند «۲۰ سال دیگر» با قدرت‌های بزرگ بجنگند، با انتقاداتی مواجه شده. منتقدان می‌گویند پیش از طرح چنین دوگانه‌ای، باید دربارۀ تجربه ۸ سال اعتماد به غرب، مذاکره…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460690" target="_blank">📅 15:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460689">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزیر کار: معوقات فروردین بازنشستگان از امشب براساس حروف الفبا واریز می‌شود
🔹
میدری: هر شب ۲ همت براساس حروف الفبا به‌حساب بازنشستگان واریز می‌شود.از بازنشستگان عذرخواهی می‌کنم که همواره پرداخت‌ها با تأخیر مواجه بوده است.
🔹
درصورتی‌که از اوراق گام استقبال…</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/460689" target="_blank">📅 15:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460688">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⁨ ⁨ کسب‌وکارتون رو به فرصت‌های بیشتر وصل کنید!
✨
💫
با «شهرآسا» بانک شهر، فعالیت پذیرندگان می‌تونه مزایای بیشتری برای کسب‌وکارشون به همراه داشته باشه؛ از تسهیلات و جوایز ویژه گرفته تا امتیاز و قرعه‌کشی ماهانه.
💳
با اتصال پایانه فروشگاهی یا درگاه پرداخت اینترنتی به حساب بانک شهر، از مزایای ویژه شهرآسا بهره‌مند شوید:
🔸
تا ۷ برابر میانگین حساب دریافت تسهیلات تا سقف ۱۰۰ میلیارد ریال
🔸
جوایز نقدی و هدایای ویژه اصناف
🔸
تجهیزات جانبی ویژه
🔸
تقدیر از پذیرندگان برتر
🎯
به ازای هر ۱۰ میلیون ریال تراکنش در ماه، یک امتیاز کسب کنید و شانس خود را برای برنده‌شدن در قرعه‌کشی جوایز ارزشمند افزایش دهید.
یعنی اینجا، فعالیت بیشتر می‌تونه فرصت‌های بیشتری براتون بسازه.
🚀</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/460688" target="_blank">📅 15:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460687">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21401f4c23.mp4?token=c6QWE9k_XgRlqMSzEr-UBpqrbLkNCmDDUy7xjo04Wdjoa2OOpvlYv_oMWKbLmvt_zFdKkJKHAqw0Qt28ZR2kgAWY-BsRKDHV8hI5T0IEOttoOnbHhoKrSf2ZY1nId-U14PSboIWQbhBEGOpFXS7EpGLTemSHGi7ukZjeiD0O-h8kRvGg3nIhLQwWcDsf__kf0CwwrrOkf3GudLIZhBskRhjPjQHV_uDceuOCNcw7e5FTwUjhxk7uFDSaDgyzw0CD80KB1RvsQCj0HeOOHztgzfrYsp7wB7jwSc-ks58pO8ORu5dNKN103Cy19dp4EpJ3acyFPV1cXhC6I7nx8a8lMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21401f4c23.mp4?token=c6QWE9k_XgRlqMSzEr-UBpqrbLkNCmDDUy7xjo04Wdjoa2OOpvlYv_oMWKbLmvt_zFdKkJKHAqw0Qt28ZR2kgAWY-BsRKDHV8hI5T0IEOttoOnbHhoKrSf2ZY1nId-U14PSboIWQbhBEGOpFXS7EpGLTemSHGi7ukZjeiD0O-h8kRvGg3nIhLQwWcDsf__kf0CwwrrOkf3GudLIZhBskRhjPjQHV_uDceuOCNcw7e5FTwUjhxk7uFDSaDgyzw0CD80KB1RvsQCj0HeOOHztgzfrYsp7wB7jwSc-ks58pO8ORu5dNKN103Cy19dp4EpJ3acyFPV1cXhC6I7nx8a8lMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
سوت آغاز هیجان زده شد!
🏁
«فرا‌لیگ» دوباره شروع شد
⚽️
از لیگ برتر ایران تا جذاب‌ترین بازی‌های انگلیس و اسپانیا؛
📲
نئوبانک «فرا‌رفاه» رو نصب کن و وارد فرالیگ شو؛ نتایج بازی‌ها رو پیش‌بینی کن و با هر حدس درست، امتیاز جمع کن.
🎉
به مناسبت ۶۶ سالگی بانک رفاه، هر ماه ۶۶ شرکت‌کننده ی برتر فرا‌لیگ از هر لیگ، برنده جوایز نقدی خواهند شد.
🎁
در پایان هر لیگ جوایز ارزنده ای به شرکت کنندگان برتر تعلق میگیره
🔹
"فرا‌لیگِ فرارفاه؛ میدون رقابت فوتبالی‌ها برای جوایز میلیاردی"
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/460687" target="_blank">📅 15:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460686">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/460686" target="_blank">📅 15:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460685">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c185f8a03.mp4?token=KrCXrqHlc_K5RtsisQ_duq6u-_iGSwFl4ERUNiWh6wrD3cbUt-sN05sk0CZ2HCD7jWBS-H5TVUtmrUi_30yTEoBrMNOKUrAEoNoy-z7d6Ckrqepg2iN2McuIg8mf7X9ueUd9cycjvCaic8yqdzcLVM4Ecsz3jxI5iPgQSme_h8fuGOMp4fYNj7oyQHe1kufQo8pYhAaLsValjLr0iiND28RZ7FlGD9EJnIJs20FruTwQNQEMnxZWRScYtsokLStNdxEVkm0aDiI3cKwVwLXquPgdpzy1b-iBmSVtl5d56A7zzb0maRbqrp8K6KIIlJC0HuKZyG5DirYIKCJtWzX2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c185f8a03.mp4?token=KrCXrqHlc_K5RtsisQ_duq6u-_iGSwFl4ERUNiWh6wrD3cbUt-sN05sk0CZ2HCD7jWBS-H5TVUtmrUi_30yTEoBrMNOKUrAEoNoy-z7d6Ckrqepg2iN2McuIg8mf7X9ueUd9cycjvCaic8yqdzcLVM4Ecsz3jxI5iPgQSme_h8fuGOMp4fYNj7oyQHe1kufQo8pYhAaLsValjLr0iiND28RZ7FlGD9EJnIJs20FruTwQNQEMnxZWRScYtsokLStNdxEVkm0aDiI3cKwVwLXquPgdpzy1b-iBmSVtl5d56A7zzb0maRbqrp8K6KIIlJC0HuKZyG5DirYIKCJtWzX2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: شدت بارش‌های امروز و فردا منجر به صدور هشدار نارنجی شده است
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/460685" target="_blank">📅 15:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460683">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4414a580ef.mp4?token=qNtEZ2zA3ibfu284xJL41fCilFR2vSaAovEX21zH6Sx3JkxPdCus5CzLKHUl2WajMHSOAyNGsGrMir7dmO4BRXZw6WYo2jygQSHnYCW6xmL4LdMZQe7X3YXzmdKE6QTjKRsiSq4Ji56syd_Rc5unMpMQyJBXBTLwypjhQM-_fLtw-_V5PMesYnawcNwTbsmWJQqZiEQl72BbE_fz70y36b7w3kn_whCunaOJsq_4CLFrKYIg_mswnIQun2NBDaEMC4gYJpe7lmjSvdJzaHbDurGF20HtKuETxg0kGwJuzZmTHOQqUoPC8hzzGFjaxIf4wpgBGZCxotfwxtvV3IGbiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4414a580ef.mp4?token=qNtEZ2zA3ibfu284xJL41fCilFR2vSaAovEX21zH6Sx3JkxPdCus5CzLKHUl2WajMHSOAyNGsGrMir7dmO4BRXZw6WYo2jygQSHnYCW6xmL4LdMZQe7X3YXzmdKE6QTjKRsiSq4Ji56syd_Rc5unMpMQyJBXBTLwypjhQM-_fLtw-_V5PMesYnawcNwTbsmWJQqZiEQl72BbE_fz70y36b7w3kn_whCunaOJsq_4CLFrKYIg_mswnIQun2NBDaEMC4gYJpe7lmjSvdJzaHbDurGF20HtKuETxg0kGwJuzZmTHOQqUoPC8hzzGFjaxIf4wpgBGZCxotfwxtvV3IGbiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکایی‌ها همچنان از آرزوهای برباد رفته‌شان می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/460683" target="_blank">📅 15:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460682">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c445b6b71.mp4?token=JlDmpIvJDz1kYFHtFJKfpWgYiz07C3hGin3H_2WqowpKLskKn-7ZvFpusxmZKvqk3yvP-OgORhIBaXr61fIq6DsAdDrmDGSfmh7SH4fuj5GsJnXzEBSws2s0KXzsL00q7dcgKEFQaR9R7To7SFJdEfGqdQrgB5IOqZT5lLqSqoAhX-JEu2_fGObbBf4MHF8YtFZnM_CQZ8GdXCQEK-TKAXqTbkNFjJOEtHK7T0AK_iuX2rAMVDqiHy5p2vfHpEZiPHfVMWWxdQJcCtdGHr4h9lYi7Lmra1GgRjaFTTuG4lUnwg6B4hlKfBGTHyCq81RBne2vHIoJPhXVCrMu60YBYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c445b6b71.mp4?token=JlDmpIvJDz1kYFHtFJKfpWgYiz07C3hGin3H_2WqowpKLskKn-7ZvFpusxmZKvqk3yvP-OgORhIBaXr61fIq6DsAdDrmDGSfmh7SH4fuj5GsJnXzEBSws2s0KXzsL00q7dcgKEFQaR9R7To7SFJdEfGqdQrgB5IOqZT5lLqSqoAhX-JEu2_fGObbBf4MHF8YtFZnM_CQZ8GdXCQEK-TKAXqTbkNFjJOEtHK7T0AK_iuX2rAMVDqiHy5p2vfHpEZiPHfVMWWxdQJcCtdGHr4h9lYi7Lmra1GgRjaFTTuG4lUnwg6B4hlKfBGTHyCq81RBne2vHIoJPhXVCrMu60YBYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگاران خارجی برای انعکاس جنایت‌های آمریکا به سیریک و میناب رفتند
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/460682" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460681">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
این مردم ۱۹۰ شب است که در میدان‌ها حماسه به‌پا کرده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/460681" target="_blank">📅 15:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460680">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e5181b6f.mp4?token=hYaM5q-FpKl9J5EtNksllw1t1sda0iM7ONqfNI0dghdwEZp6JB1IymZRVwu2BiHfHeaCSYd82MUQtHuw4JshIidhQjBqeBpZfIsaPFvcuv-3_0qMOXpCjWE7xkb-5KNYCdV5aD1EjsAC9DWKG4K5cBYIu5NTokR8oaUOLy5jTuNUSDqcucZ0zipJyCwBscwjpdpVS4ZAc9vvA0gjCIWG6GndFIl609isR33NfsmPSlRy1JfyR7I_xgzOJHMkjzUTBMMKXvI4A3AduxIpdwsK8mp7Tp9y43y2jmkRu3uxpQAcrvHSzaJwNA5ik10c-rcO5Bzd-PGjlfoyK0ucV3DPUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e5181b6f.mp4?token=hYaM5q-FpKl9J5EtNksllw1t1sda0iM7ONqfNI0dghdwEZp6JB1IymZRVwu2BiHfHeaCSYd82MUQtHuw4JshIidhQjBqeBpZfIsaPFvcuv-3_0qMOXpCjWE7xkb-5KNYCdV5aD1EjsAC9DWKG4K5cBYIu5NTokR8oaUOLy5jTuNUSDqcucZ0zipJyCwBscwjpdpVS4ZAc9vvA0gjCIWG6GndFIl609isR33NfsmPSlRy1JfyR7I_xgzOJHMkjzUTBMMKXvI4A3AduxIpdwsK8mp7Tp9y43y2jmkRu3uxpQAcrvHSzaJwNA5ik10c-rcO5Bzd-PGjlfoyK0ucV3DPUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلزلۀ سیاسی در آلمان؛ پیروزی چشمگیر راست‌های افراطی در انتخابات ایالتی
🔹
برای اولین‌بار از زمان جنگ جهانی دوم و سقوط نازی‌ها، یک حزب راست‌گرای افراطی در انتخابات آلمان به یک پیروزی مهم دست یافت.
🔹
برآوردهای جدید حاکی از آن است، حزب راست افراطی آلترناتیو برای…</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/460680" target="_blank">📅 14:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460679">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای آتش‌سوزی در یکی از تأسیسات آرامکو واقع در ینبع را تأیید می‌کند
🔹
این آتش‌سوزی در حوالی یک مخزن سوخت اتفاق افتاده و تصاویر توسط ماهوارهٔ Sentinel-2L ثبت شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/460679" target="_blank">📅 14:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460678">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/471897a3ba.mp4?token=vOwGnKb0bBbRQIG-nw6opDTHJJvgn3DJTnEztBRsPgp1Xj6DAuAVzn8H_oR-Qv-5M2-PMsdCnOhehsMeRp8ZsC9ibt9gTWHqZ1jtbodjTrkw8NlTUX2z9asp_jUhL7wy8gSO3gk2xyVhO8mn_5bRad2tiQOUqWg0YmXoNl740MTJWkUXgen9SmjwKMX3i1zq4lnuP5KM2SGgUwd3pZdhHf1c_tBASS7_wvC3S8q9K3Lac66j7wVYm2R9-5W3OpVRSiM7m8g5j1PJUnUF6sOnasC3UZ4fHszcTO55ckyf1d-vA_MbvawO-N9zuukFtD6GQAxqQTYVldK9N3t8LQERfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/471897a3ba.mp4?token=vOwGnKb0bBbRQIG-nw6opDTHJJvgn3DJTnEztBRsPgp1Xj6DAuAVzn8H_oR-Qv-5M2-PMsdCnOhehsMeRp8ZsC9ibt9gTWHqZ1jtbodjTrkw8NlTUX2z9asp_jUhL7wy8gSO3gk2xyVhO8mn_5bRad2tiQOUqWg0YmXoNl740MTJWkUXgen9SmjwKMX3i1zq4lnuP5KM2SGgUwd3pZdhHf1c_tBASS7_wvC3S8q9K3Lac66j7wVYm2R9-5W3OpVRSiM7m8g5j1PJUnUF6sOnasC3UZ4fHszcTO55ckyf1d-vA_MbvawO-N9zuukFtD6GQAxqQTYVldK9N3t8LQERfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی خطاب به ویتکاف: بیشتر به اینجا بیایید تا اوکراینی‌ها بتوانند بیشتر زنده بمانند
🔹
رئیس‌جمهور اوکراین پس‌از گفت‌و‌گوی امروزش با ویتکاف و کوشنر، نمایندگان ترامپ، از پایان دور نخست مذاکرات با هیئت آمریکایی خبر داد.
🔹
زلنسکی در پیامی که خطاب به فرستادگان…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460678" target="_blank">📅 14:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460677">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04260caec9.mp4?token=nlb9Ybb3ehmuS_mr5gK_vc8CsprvrPyiHL6awmi0TmR0rp05TFnPSkta7HETaE_DDUsWIhuwCLO_uWvu9q60SPSWbUJd1bWYM-K0HWwXs-roCEQOLyZQXFMoMh7kZK2ojmvhSAlSXiSUXLWn91lqYI3WvP7jfY66GOAyiWmagNe29quuvEwv3CExUAGRTDeqJsMMwEANQEGIGUjDjIgT_XCpSzdOvnJRwR-SigRysurx0WCTtUSSrVPiSMLafxdiNwPfOR2zbSZRP3TCnaXl4Fh5TZ3wXHfehB-1tIyN9mZrcbYd3KE8tIogIAu0ZvG7bWFA_mgLfT1as_COK307YkD_iSOH03anNSJdV3pshX4SGeMehk7PAPCTUxat7lGe6E9SPGkmdLsKx4H9W5ER42icyikOjQRWhTREl858W1eVsnuS5slZi5FKUD7H0SjQ5zMH3nEKJcZgt-PvGjWUh-OcDKPoZbQl3wG6W22hAd00qdRBJocLU20HTnaUL2C9b1AAqOwpnCXPhmbPsQlyx-l8G2P3z6zYGDz3ZmZqD8Zp8zcGUt2jb3btCyppsrZtXD1gHQv3GCqdrpFTR_f9eOlCCqQDKZZfd66lL7chdYDN9VQX02pCMcEQFsuCk1I_kRLKQ4__xGjAFHpCdpM0OVKrRuv1omgtq2n5OvRljFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04260caec9.mp4?token=nlb9Ybb3ehmuS_mr5gK_vc8CsprvrPyiHL6awmi0TmR0rp05TFnPSkta7HETaE_DDUsWIhuwCLO_uWvu9q60SPSWbUJd1bWYM-K0HWwXs-roCEQOLyZQXFMoMh7kZK2ojmvhSAlSXiSUXLWn91lqYI3WvP7jfY66GOAyiWmagNe29quuvEwv3CExUAGRTDeqJsMMwEANQEGIGUjDjIgT_XCpSzdOvnJRwR-SigRysurx0WCTtUSSrVPiSMLafxdiNwPfOR2zbSZRP3TCnaXl4Fh5TZ3wXHfehB-1tIyN9mZrcbYd3KE8tIogIAu0ZvG7bWFA_mgLfT1as_COK307YkD_iSOH03anNSJdV3pshX4SGeMehk7PAPCTUxat7lGe6E9SPGkmdLsKx4H9W5ER42icyikOjQRWhTREl858W1eVsnuS5slZi5FKUD7H0SjQ5zMH3nEKJcZgt-PvGjWUh-OcDKPoZbQl3wG6W22hAd00qdRBJocLU20HTnaUL2C9b1AAqOwpnCXPhmbPsQlyx-l8G2P3z6zYGDz3ZmZqD8Zp8zcGUt2jb3btCyppsrZtXD1gHQv3GCqdrpFTR_f9eOlCCqQDKZZfd66lL7chdYDN9VQX02pCMcEQFsuCk1I_kRLKQ4__xGjAFHpCdpM0OVKrRuv1omgtq2n5OvRljFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در همایش افتتاح ۷۹۴۷ طرح خانوادهٔ ارتباطات
🔹
رئیس‌جمهور: اگر باایمان و اراده بایستیم دشمن نمی‌تواند مانع رشد ما شود؛ ما میتوانیم همهٔ مشکلات را به همدلی، همراهی، انسجام و وحدت حل کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/460677" target="_blank">📅 14:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460676">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcBZScg0I5kExWiww1BKEROmIldlRLCUD4QyCgQZjtKMDj0IuSI7mjjui1eO8apWkerb4v1ekTBgKsG0g2iDg6DP2kljJVf3YkH-NiXNoXdKh0eJKwAbGxw3jslTIy1Xb9j6-2QT0XgMBY5l6csz0npGwPMBJYtXMAfmKRcu-lXsKonjaiK7cqLcS6-5S9UFaOu5bbjPebp03DwSnjLgopWrfgAwlli5l2mHucGct-Dy_LpsnelcUXcgH2p46CmnBs2knyKdHMRPeXBmUIvaqvzlu3HFPQ2H4FTLaNqBiICQ3ct5sVmECofaJGi9zZ_yI7MghFqE7UOi5HVDZH0i1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: روز بدون خودرو برای دستگاه‌های دولتی اجرا می‌شود
🔹
با توجه به ضرورت مدیریت مصرف بنزین و اصلاح الگوی مصرف سوخت، تمامی دستگاه‌های دولتی یک روز در هفته را به‌عنوان «روز بدون خودرو» برای کارکنان در دستور کار قرار دهند.
🔹
توسعۀ دورکاری و کاهش سفر‌های غیرضروری و بین‌شهری نیز باید مورد توجه دستگاه‌ها قرار گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/460676" target="_blank">📅 14:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460675">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌ نکردۀ جنگ در بوشهر
🔹
فرماندار بوشهر: فردا از ساعت ۹ تا ۱۲ ظهر خنثی‌سازی و انهدام مهمات عمل‌نکردۀ باقی‌مانده از جنگ در حوالی پایگاه هوایی بوشهر انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/460675" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460674">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGqZ_UaFvn6M5y6Q4u0UvvKtWsgaScX5D2Gw7sJosWtRPAlHcno9xp8Hw2Pp890B99ss9V3X2wG-WN6iD18k_LCWevr3YFlUSPw-3Jw28UefB9SDojuNrrZJ3CG0Nvf9y4sbcf5yD-rEnhi3HbkkEkfzPfDl9u5qcqA7FSXcd4ydxUW7KEBhWZkJWArMcut8TwVyHWpKGVXia7oHqVcjoFI53jQOuZ_sxN0e4agMlgh6slapiueNr0XebJOHKGcwQImUasKew4cyNng1wSuHr8S9jsAnaiakARL24jij0tmyCcM1krhN9okCiEhPe_LEAx0-Cr-FuFc0EWqUDO_tqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی دریایی ارتش: می‌توانیم دشمن را در هر نقطه‌ای زمین‌گیر کنیم
🔹
دشمن امروز ابتکارهای عملیاتی نیروهای مسلح ایران اسلامی به‌شدت نگران است و با توجه به پیشرفت‌های حاصل شده، در صورت لزوم می‌توانیم دشمن را در هر نقطه‌ای زمین‌گیر کنیم.
🔹
غافل‌گیری دشمن در مأموریت‌های مختلف، به‌گونه‌ای بوده که توان عملیاتی برخی از ناوهای متخاصم را برای مدتی طولانی مختل کرده است.
🔹
مأموریت اصلی ما این است که اجازه ندهیم دشمن به اهداف خود برسد و در این مسیر موفق خواهیم بود، چراکه تحرکات دشمن به‌صورت لحظه‌ای رصد می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/460674" target="_blank">📅 14:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460673">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d21b4626.mp4?token=GtKyYeQrDoCpGEWaRRYoDdCXekOZcJdjNgHvicC71mgH58E2toN21984tGCg_pTz_MyI15WbB08_QDjcniuphlDx3zf6CxEFOAC3pzNkKzrCWeDXdYiO2HPqiDzEBrPP4luhKmRLM3I1onGEZgArsAwcEznekhOvNlAPSbLUHrFd4yOyOyiFdCf_U5JUlq2TscwDNCpA1fFKkL8X9mChNVMcHLOzbThGSXIkvji4BMjMEXk-adKBayZTgng5tRaRB0ftEQVTplGrw5y4Qda3VvwPhqBPiVIAGQo8NgQlokkbn_Ot_y4RBXsNxUIZZM_VQt5vggIDCSYrROuDl8HKPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d21b4626.mp4?token=GtKyYeQrDoCpGEWaRRYoDdCXekOZcJdjNgHvicC71mgH58E2toN21984tGCg_pTz_MyI15WbB08_QDjcniuphlDx3zf6CxEFOAC3pzNkKzrCWeDXdYiO2HPqiDzEBrPP4luhKmRLM3I1onGEZgArsAwcEznekhOvNlAPSbLUHrFd4yOyOyiFdCf_U5JUlq2TscwDNCpA1fFKkL8X9mChNVMcHLOzbThGSXIkvji4BMjMEXk-adKBayZTgng5tRaRB0ftEQVTplGrw5y4Qda3VvwPhqBPiVIAGQo8NgQlokkbn_Ot_y4RBXsNxUIZZM_VQt5vggIDCSYrROuDl8HKPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رشد ۸۵ میلیون دلاری حجم معاملات ارز تجاری
🔹
حجم معاملات بازار ارز تجاری از ۴۶ میلیون دلار در فروردین به ۱۳۱ میلیون دلار در شهریور رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/460673" target="_blank">📅 14:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460672">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwitSORKoFQtgTWUkYO9DMO-Tn2sjLuUpYcGMQfkbYw_ViTmm-GRGSkiAvSBr5PYyBCsua8EEmlIXIYTHDNFlPuv6KJjeVvmSk3xbSVPbUYwT3q9WKiO99J1rPXKPAKitijkVt0rdwlNZE09bX7DJi7laBjMMPEnlIOMIleQJpI0lGsfz1rz63loHigVpAu9rToaELkBzMW19hsQmhrHchMNHsMIx1YzTs-0imZgKYgazchLbkPtXu_Fw_6zyQ5sqjWo-RxtAHJo6gRgG4C1TXkkh5UPSP8i-s7l_yPyePAS-TRyLn1mdof069dTDbzVibRh30Ck5wlL-UtUcidcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات شکار چشم عقاب امروز روایت می‌شود
🔹
ویژه‌برنامۀ «عملیات شکار چشم عقاب» سپاه پاسداران، امروز ساعت ۱۷ از شبکه اول سیما پخش خواهد شد.
🔹
قرار است در این روایت،‌ جزئیات جدید از شکار هواپیمای آواکس دشمن آمریکایی در عربستان بیان شود.
🔹
همچنین علت حملات موشکی به پایگاه اردن نیز جزو اطلاعاتی است که برای اولین‌بار منتشر می‌شود.
🔸
سپاه ۷ فروردین با پهپاد شاهد ۱۳۶، هواپیمای آواکس E-3 آمریکا را در پایگاه شاهزاده سلطان عربستان شکار کرد و یکی از چشمان نظارتی ارتش آمریکا را از کار انداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/460672" target="_blank">📅 14:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460671">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNqwBQ0Zpvasask0cyvJW1pxaLZUFm_U23QnGsv7oBe6hXVY-xwGF2vH46MKER5lWITIz9xlSJk2pjAgS7pNUW5geqt9XEaQHl4xu2-D-jJWO1xR_JS4RM2-RLRs5Dx0lGR-aIHP8WXzCLAMwupNciINvlZyd-Aet-OqMzPwPMjQFqukGnVd9fJgsMnPxuK3DBB3OsCgzoFpWRZ7abBvWdawyQ2xjCD3gZi9km2bxrfN5AzB9s3wbI95kiTfVEc8FrKCxRd2Rh3orqR2nrQUgbT2oZ5JSRJ1z0RummuiL0ZOPNkhtFq5QzN8DtHpXi4k4qDfR92KVZ25217qSuZ25A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزش معدن اسفراین یک فوتی و ۲ مصدوم برجای گذاشت
🔹
هلال‌احمر خراسان‌شمالی: درپی ریزش معدن آلبلاغ اسفراین در بامداد امروز، یک نفر کشته و ۲ نفر مصدوم شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/460671" target="_blank">📅 14:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460670">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuFcAYmBUdAGactL60UB5oEfHimj46GUVC6O1xVru7NlQ56jmaaIucYn7Kvz0qXzS5nnYEHnCtaX-_ItZwZ8JRTng_PCp2122QS8mT7Fs5x2eQoaVFFAf7e-Cj85zT9j2ODAsiXMFSiu75v_Okx81fPqp6iZUXdgzKbkkXfe8ChHMYNY68VZmVt7ADdbn6r13OsJdbf03Q8iYOA3Ega52c4rVeQ9_U10jFMXTqOv0P87qYH6xWHyt6ZJqZkzLKO_sqlXZYmY1KKuur9L3cAyx6kcNZlksyWEvvRnLIemL4jE9pZBKUYEWD9QrHCYRqEL1wFnRCkHxv9HW0PTc_f4vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب‌ شرکت ملی نفت ایران بسته شد
🔹
کسب اطلاع فارس نشان می‌هد بانک دولتی صنعت‌ومعدن حساب‌های شرکت ملی نفت را به‌خاطر بدهی بست.
🔸
پیش از این وزارت خزانه‌داری آمریکا در قالب تحریم اقدام به محدودیت مالی برای شرکت ملی نفت کرده بود.
🔹
اقدام این بانک در شرایطی…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/460670" target="_blank">📅 14:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460669">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0321e63b.mp4?token=GJd6bUbIC77QMw64oT_ZqoOzubqRqOnA13fIXdNFhLxDn0zyqHiD0D3iJozCUcS0w88kTiWTNqWLqDKTwN9RI2LB8sq1j02NWpSo1VQlaTE3KYnR3vmxEHh7zixwzwX3R0UFzYOwXZ3OIvAye9PTL6LLr5zNqsdH-96UVmhwk4WBIftKIz91Ns0MIwlrmqGV2Uk6ESjo8cagUSFfNjg4r3Ie09GorojGBVypHvUlj3KZGM8jPkGZ_gtGyZAS4s7HO6dv95OYCPLmjgt13ZwK4jtCS1Tm7crw834KK4BxMchRvbO6d2jn30AoBt26dBdH-1ZRWyiNV4rrgYKLdJgWvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0321e63b.mp4?token=GJd6bUbIC77QMw64oT_ZqoOzubqRqOnA13fIXdNFhLxDn0zyqHiD0D3iJozCUcS0w88kTiWTNqWLqDKTwN9RI2LB8sq1j02NWpSo1VQlaTE3KYnR3vmxEHh7zixwzwX3R0UFzYOwXZ3OIvAye9PTL6LLr5zNqsdH-96UVmhwk4WBIftKIz91Ns0MIwlrmqGV2Uk6ESjo8cagUSFfNjg4r3Ie09GorojGBVypHvUlj3KZGM8jPkGZ_gtGyZAS4s7HO6dv95OYCPLmjgt13ZwK4jtCS1Tm7crw834KK4BxMchRvbO6d2jn30AoBt26dBdH-1ZRWyiNV4rrgYKLdJgWvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از حضور خادمان حرم رضوی در جنوب ایران
🔹
کاروان خادمان امام رضا(ع) با سفر به هرمزگان، در روزهایی که جنوبِ قهرمان ایران آماج حملات استکبار بود، به دیدار خانواده‌های شهدا و جانبازان جنگ تحمیلیِ آمریکایی-صهیونیستی رفت.
🔹
خدام رضوی همچنین با حضور در میان مدافعان «ایران امام رضا(ع)» و شرکت در اجتماعات شبانه مردمی، پیام‌آور دلگرمی، امید و معنویت حرم مطهر رضوی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/460669" target="_blank">📅 14:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460668">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8YaWB-8Yb5W1T7_a7LxxmVy_rxZ6vTbVdYoCnGOWXXAa6W4QEs0e5ynGXlgs6l1PkRWLgdhc4OvY2xDdQEhru3_mfqFmrcIVXnTgQqiefKxz8PDwWrHY0JrQSx_b9lKIVAvUV2DKHCADp-4bhDE-CoRXIXlLccp0tEy-sL30EZMhhm7zVMO7Q3vsJvukjjr71XRvJdBJBC2GaybpuiJz3LafbliVyzblzwIOKRAwzcFGQRHeIaNdvCwEtyfQK8_xEVs6Azg1fFnebZGmRb9FHzMUZ1nNdsontQs0Mf0UUGiux7BpO6lR7a6yU2nhdw60y5egaMXCVd6bxNW-jAKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل تاپیکو عنوان کرد: آغوش باز تاپیکو برای دانش‌آموختگاه شریف
مدیرعامل شرکت سرمایه‌گذاری نفت، گاز و پتروشیمی تأمین (تاپیکو) در مراسم جشن فارغ‌التحصیلی دانش‌آموختگان دانشگاه صنعتی شریف، با تبریک به دانش‌آموختگان، پشت سر گذاشتن دوران سخت و پرفشار تحصیل و دستیابی به موفقیت علمی را حاصل تلاش و پشتکار آنان و همراهی خانواده‌ها، استادان و مدیران دانشگاه دانست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/460668" target="_blank">📅 14:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460667">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخانه ریز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHyUDgrWOu1KCUf9K_OHKnzi_Y3vkalmHd6AT6SRNEpf3tl3XsbR8E8HvSDUJYA2ErJ_JqtLNqRuZm5RqOHFK7n2O0jtP3VrOFsI9Hvhz36XwTpvIbXF59G-vtVuthv8MKWI552LVAtL9mG5HsLsSVBtI3wbVaGQfplkaQo1Che3nu_xB6GY_FYPp82CszmM8ely0PhZQhT5_MIIVMyyiY6gjneFcSDDG4M1lA5is4Smyk_EfwaK1mr9t_JHsb4GqOjgfaq519QMmlw4Lr_72zAsMVjR8NqmR-P2nsYkPx90UxNld_XsHnRxMjpEnbr32rTNlh_ZZN6xhCbq2Wwnew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرحله دوم فروش «خانه‌ریز» در شهریورماه؛ چهارشنبه ۱۸ شهریور
در ادامه برنامه‌های فروش «خانه‌ریز»، دومین مرحله عرضه واحدهای پروژه «فجر» در منطقه پنج تهران، روز چهارشنبه ۱۸ شهریورماه از ساعت ۸ صبح آغاز می‌شود.
نخستین پروژه
#خانه_‌ریز
با عنوان «خانه‌ریز فجر» در منطقه پنج تهران و در بلوار آیت‌الله کاشانی در حال ساخت است. این پروژه شامل ۵۴ واحد مسکونی با زیربنای کل ۱۰ هزار و ۲۹۰ مترمربع بوده و در حال حاضر در مرحله گودبرداری قرار دارد.
علاقه‌مندان برای کسب اطلاعات بیشتر و مشاهده جزئیات فروش می‌توانند به سکوی آنلاین «خانه‌ریز» مراجعه کنند:
https://khanehriz.shahrzadcity.ir
@KHANEHRIZ_IR</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/460667" target="_blank">📅 14:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460666">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/460666" target="_blank">📅 14:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460665">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ8jQkO-jk_oTk3-14pdYSflco-vBzguTWUBzD87nBgp40Pn2T6sFNAAnwx3aVE_NXccQ4KOJAeFFprDPDrGSbg0gZlke-s4aBlYTGUa-JhLJuKCTTZcZPC_oLlfY4QfZKZs4aHaI5Euh6tpM75wj5_cmW3fYglbPaj4yWV_PaiBBLi43ngbaWQTAPI9-IDC3g3ilsjq0_F9DZrJLECGqw2Hes7Jau_UCts6oq7tnaEV85ykB6jOYakJtf65t1itw8f41MLdjn1NghqnVvL-w-bZNsJE0iB38DU0WgsyTLHqxA5cUIDzKM3PNd07cZlEkkc1bo8zbLOH3R3TtOyfIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر حیدری: تغییر معادلات جنگ از سوی ایران خارج تصور دشمن بود
🔹
جانشین ستادکل نیروهای مسلح: دشمن پیش از آغاز درگیری‌ها، بر مجموعه‌ای از سناریوها و محاسبات خود، حساب ویژه‌ای باز کرده بود.
🔹
آن‌ها تلاش داشتند با بهره‌گیری از جنگ ترکیبی و همچنین استفاده از عوامل وابسته به خود در داخل کشور، ایران را با آشوب، ناامنی و بی‌ثباتی مواجه کنند.
🔹
ایران با بهره‌گیری از ظرفیت‌های راهبردی خود، توانست تأثیر قابل‌توجهی بر معادلات اقتصادی جهان داشته باشد.
🔹
دشمن تصور نمی‌کرد ایران بتواند معادلات جنگ را تغییر داده و عرصهٔ نبرد را به سطحی منطقه‌ای گسترش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/460665" target="_blank">📅 13:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460663">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDnuFtaEVFEAbxgdSaUQLo8A-3B3ylKVFOX2feWiRLYn-EXShMxdC3a6bXMR76GhzFnk4hFIWhlqjODk6HsZQbvdOR1x0rNuMyHj77CI4DqqfSgYDNAQtAC6mgnKfi6Ukn5gDUYiNauwSosN7TId2tOlnja6Ce08BVLdDIZeVCYGiQZJ0xsYQDU5WC7FkoyVSP5Bd8R54N-_JD1bFCNLnc164PKTbe27-1GIs8Nwjr7bUtgFSpj9ESgHkzrwW5O9OEmDvZeWDdnpDONUxvucirAuMr2qJbkJ6DVrB6FZ4f6nrdjV0NC9na3GFT2_hhZmH6jkAy_aWn0HuEdHf_DVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAHJNYUGw6JA-QyrUBiO2sLUE5gqmTmSbPqhwv9ToPQdvu0DwOUnnbpXDg8Hl9op8LtrzawL-mqBwFMEtMbp4fiyK7nXi2XV71cbPocTI2rVvvhk10jOAnxu96VVimE4Pi0jG5xc6-A5_exPj4mQebPey5BXQKN-G5F-eRLRfYNI1X8qdN6AhCfDqmHDKZQ45fH9syTbf34peEHCmeeMZ7N-qA45GBSS1Sfb5qt94z4sYl5GkTOkpnkIvpLk2RFk1IEwKAZR-keTiBASc83Dcde-MagfyoN6A3-RiPB3EJxr0U8VeLYIUI7netTfh1va38BWbP7YH6QtLG2mfW-vvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خشم کاربران از رویکرد تحریمی آمریکا؛ جهان از دلار عبور می‌کند
🔹
وزیر خزانه‌داری آمریکا با تکرار سیاست تهدید و تحریم علیه ایران، از اعمال تحریم‌های جدید علیه بانک‌های مرتبط با تهران خبر داد؛ اظهاراتی که با واکنش گسترده کاربران خارجی مواجه شد.
🔹
بسیاری از کاربران با انتقاد از رویکرد تحریمی آمریکا، استفاده گسترده واشنگتن از تحریم‌های اقتصادی علیه ایران و دیگر کشورها را نشانه‌ای از سوءاستفاده آمریکا از جایگاه خود در نظام مالی بین‌المللی دانستند.
🔹
بخشی از این واکنش‌ها بر این نکته متمرکز بود که تحریم‌ها زمانی مؤثر هستند که کشورهای هدف و شرکای تجاری آنها همچنان به نظام مالی و دلار آمریکا وابسته باشند؛ اما با گسترش سازوکارهای مالی خارج از کنترل واشنگتن، قدرت تحریم‌های یک‌جانبه آمریکا نیز می‌تواند کاهش یابد.
🔹
کاربران همچنین به نقش بریکس و تلاش کشورهای عضو و شرکای آن برای افزایش تجارت با ارزهای ملی، ایجاد سازوکارهای پرداخت مستقل و کاهش وابستگی به دلار اشاره کردند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/460663" target="_blank">📅 13:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460662">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHdQrmZoSTclg9T8txl5tumOpJIiDk0hrjREmwpB9xxBRuSc4sMovbh3cdCbZfW38AbH5DPOPltQ-AxLA8XbKzsb4bvVyot1EY4L2TT4BXatDIZB1_yorULmtogpK0Htt2a8M-BVa3NUkswBMERYJorybxYZVc3Zhv8dKUHqrFDgudnDdSJLZI3SUyRYJ7MWDKi71cMazEFRhQ-hlwRWMhbCMI2e34GdARtYfg1cVSgKKHCGaVnz5XpLb8ayv4tEhnrR8LnDE4ojxPSy2_Dz0YuidlRfjFA-nRa7tU8TSuSoa-Pso5x9r20DppLukUYAWg5CCA6ChhGmhS1mWmLmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۴.۴ ریشتر در عمق ۸ کیلومتری، بوئین‌سفلی کردستان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/460662" target="_blank">📅 13:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460661">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌‌‌‌‌‌‌‌‌‌‌ دفتر نمایندگی وزارت خارجه در هرمزگان: ۱۰ صیاد مفقودشدهٔ بندرلنگه‌ای امروز به میهن بازمی‌گردند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/460661" target="_blank">📅 13:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460660">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF2oTCJEtPXEkmg4cc08UjPwMUnIX9QavANNL7GZM74i-aAwXNgjXO5P7Eiv_wS40sNe0s86FBpB6N0v_w1A2stKFsIYVKPiEO_9rRcIFte5AgecBQ7J_aC-wC4Kh9M8Ke3hF2PPRdr4EDRTaGlJds88VM-6C_DvrNRpi8sJF2UQ5UsqiUgiqfF1AyW14im0tEkFPvqTK4sVXOHYS_PN9a7RcgTuk1wi0-jYp3lu3wUswuL6KJ4ZrWU4qZlPF9bHhE5cxcJxUgTyp84VWgyd8sk2TsXqugz9zZl3b4koV3gUssMhHjv74eWHyfX7I0-XIMsWKuwv-fPuI_chjvPD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تجمع دانشجویان شهید بهشتی در محکومیتِ پرچم‌سوزان
🔹
دانشجویان دانشگاه شهید بهشتی امروز در تجمعی در صحن دانشگاه، با محکوم‌کردن هتک حرمت پرچم ایران، حمایت خود را از آرمان‌های انقلاب اعلام کردند.
🔹
اما در آن سوی این تجمع، برخی دانشجونمایان با حضور در بلندی‌های…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460660" target="_blank">📅 13:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460659">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-URwlJsPoQiWWimaZY4s3M4K19LiJvDqEJVliPQyWT1Zu6eILq2SjRNO0MASRYMKADHxYcrtKQB6mLe0XkszK_pe9sBPhqn0m2uPdxI5GldYrUDFtQNd_CW5OPZV4ABGPvjiGp2VSq1hqwH01iFDkY7hjx4_5oprhBHjpfb0B3EdpQBgbHTFtClRZ8aT8lOoTxVyxl9KiHYacCro8X-rxDV3qBRRy5mO7Hqa9MzDrHV5qsQMiy4z9ahPxanNpmKmffFhVglMdAQZQZEqcylipg8r81jTBE9RwN3zHQ11EXBz4ExJZdxo7uW0tLwzqaM1Bwi0HoLdXoAUDjC_7DDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنگونی پهپاد ارتش عربستان در آسمان یمن
🔹
نیروهای مسلح یمن از رهگیری و سرنگونی یک پهپاد شناسایی-تهاجمی مدل «CH-4» ارتش عربستان بر فراز استان الجوف خبر دادند. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460659" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc_Tbmi9We8H5IfkcUQ4YXMzZ0eOAVzu10YIWhVULSqA-oniuNT6GMg045Rb_Bp4buBPRHl_JemeEenFheRxekx7DzuyYH1bX_PNMX5lDnyEcqWsakyjs4RQ6ouBo3RPKsHA8-OqAL31rm3LYDI15heYwnSj2NV8HTnE04x-P6-D2zaZR8HITLLGbXDf8daa3A2A-5fGxh6_Cr1WpnknzMisuC3T0DVqmgPZiy2lCjgNYYdrnApnpzabMKfpDO1KtlhfaNsvjCXQC8fU0DXzZu3LAz9aaCJ2XSa0sXUKchIJumHeX9dkmCLl2Y54cgBcHWL1zExmHIBFNZdGV22ouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عروس رفته گل بچینه...
🔸
کمپین خیابانی غم‌انگیز، به‌یاد شهدای عروسی سیریک
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460658" target="_blank">📅 12:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460657">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OktBpXzTaBo6sIBAAAgsaDkbm-yOczFy6vUjIkfB1yYJm8Hoy1VUy_afYH38HPLKQ6QOcOucLqqDmG8wZye3Ve9vMY7gEd5Lhn0fxOyRzvSdmh6c8kZpXQ8VNtjfN7U1qvpYnq-5t_eqAw1pWjdU1Th2ORHvKxrGEEzBlO-scifaCBalhy9GQv0NOs_aDd8_G68jmTsda5P2OL1_egpnLoMLpEbVh2oUCdvnQMf-DSxBk2k0SHUD0NYHSe84OeuUsF4_1t7Vt2DQx71pnGgoo_ECHvTlNjqCTeWGDbazG6cNegVHSX6WIsPRnWbwFvr4cSNKmJnK7C3KeVfNEJtJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس امروز فقط ۲ نماد منفی داشت!
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۸۴ هزار واحدی به ۶ میلیون و ۹۰۸ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460657" target="_blank">📅 12:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460656">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbEadwQEoJ9WHm2D80M6ZqXig2UcbQBVxmyqMHbwqwpNKmwgKSfl_PNUjSFageVoD-U6ztTUQF-YmF8xi8AyEgF13ye7hv0f9PVWex3QSAxSEiKsF3I4wsruXcdV_Afbm5YrO-rOeHB1YhXmonXgK4BZETY1bLgxk126cqJZAjf-PLt2NgIf9sQBhfdOkoQRprlgFHISBl5s4b4rcIGaiXE3NACR3WH4rtUuq_bu1c2xyrZKDKQBJ5id4S4deLcdUizLU0p3rXeu1fzlNSYVgXUYPhJsyE4Bgjj-NH1ehKiUJughyqECX-n17fv8TZhQQEnG725uE2zi9irAo7HXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: ایران براساس اقدام واقعی طرف مقابل تصمیم خواهد گرفت
🔹
رئیس سازمان بسیج: بدعهدی‌های دشمن برای ملت ایران ناشناخته نیست؛ مردم ایران بارها وعده‌های دشمن را شنیده و نتیجهٔ آن را دیده‌اند.
🔹
از همین رو، جمهوری اسلامی ایران نه براساس وعده، بلکه براساس اقدام واقعی طرف مقابل تصمیم خواهد گرفت.
🔹
پیام ایران روشن است؛ هر تعهدی باید اجرا شود و هر توافقی باید در عمل به تأمین حقوق ملت منجر شود.
🔹
دشمن نمی‌تواند هم‌زمان تعهدات خود را نادیده بگیرد، تهدید کند و انتظار داشته باشد ایران از حقوق خود دست بکشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/460656" target="_blank">📅 12:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460655">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0RCvaLUYazhxqO1vXhecKOag8c5Qh9GEo6EAofHZAxKRJT2v_gNFo0J8fM60qcdFxOhmL9RH29qTrDfe5pe971HJMjzyhrtvee_YXNv6i-DzQBbfoOZy0WxdH8wJDUKGauallAUSaaz1Fyo4dPIcCJoIZI-QTdnJm3cb08wkdlSYTlIejLas6wGrfpt8wCTvp4uWnJx4qnl9ch-xKLi9McVOCqwBc0a5Vw9BxDLAg2bq75ytinYIMMT31Dve_x3Yp1xFgABsrOgoibF84AStaVAC-GuCWZD04j1KjVFYVMUxhg0Wcgv6wH_hHDb8qVleXDdGC6vLMIEsHgpW57BRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
از داده خام تا فرصت کسب‌وکار با «قالی»
«قالی» همراه اول، یکی از محصولات معرفی‌شده در نمایشگاه اینوتکس، با هدف ساده‌تر کردن تحلیل داده و استخراج فرصت‌های پنهان از میان حجم گسترده اطلاعات طراحی شده است.
این سامانه می‌تواند جریان‌های مختلف داده؛ از اخبار و قیمت‌ها تا داده‌های مکانی و زمانی را دریافت کند و به کاربران کمک کند با ساخت فرضیه و مقایسه الگوها، ارتباط‌های پنهان میان رویدادها را کشف کنند.
محمدعلی تولایی، مدیرعامل هوش مصنوعی قالی، می‌گوید این سامانه می‌تواند شباهت‌های زمانی میان اتفاقات را شناسایی کند؛ برای مثال مشخص کند افزایش قیمت یک کالا، با چه فاصله‌ای می‌تواند با تغییر قیمت کالای دیگری ارتباط داشته باشد.
نام «قالی» نیز از همین ساختار گرفته شده است؛ داده‌ها مانند تار و پود کنار هم قرار می‌گیرند تا در نهایت یک «نقشه» از بینش‌های قابل استفاده برای کسب‌وکارها شکل بگیرد.
هدف این محصول، توانمندسازی کسب‌وکارها و متخصصان داده برای تبدیل اطلاعات خام به تحلیل و فرصت اقتصادی است.</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/460655" target="_blank">📅 12:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460654">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7ae037ce.mp4?token=YZmn32LIFd11zouGvwtxvO6pCVXHB1E9LEK5Wu_jY8OH_HyQZMshGgPAloE8fcPHF2cIrSvBgP35V2wyUThSHrQtU2ejCoJ7tR8kOdel91oi7qgmpkNC7xdzLqBYk8Bzp4-veFZTRlRk1aWdWApdu5-Q2YfQU4kp1Q6gcGrFrCUfpmjxAlzrL0iTqyyOLhWBzShqfulwWGpFRsEIlcFdPMLNVHSfixPnWv2lTQ9J2bcd1lpQBE7QMXHOCGzMALwzKuyqEZg3rZaE-FzgBu492FBdpnusJR3ydSgdkCKpTjxkJRdrIfOPLGFId7E9RrYNNCptnKFDU5iKUG4iSdVH5LzJMQOW2pn7mvaD6ggfxE-VE9crH_KUVmfOvkaHWePXUijwBQ7R6oOTVOo-1lF4RYkdLq9qK_60F3-InoudPplNw1gRlOaNPZ_niYJQg4kDswJ3IthjJF74UAovNfiLLu4WfZl1sxKN0RfeD_YlXTWiBfRiySqNRUYceyRUEVQli1N9iGuxxtgXJrtwsm2zjD9fjN7Po1JBfZUCnVd-8vsVo1p2HrzeGAT5VXGqnZrzfxeKcRz6niWW4_ZH7sGRvYAbbcard8-gm9gTy1nf7VHR7yLERN9J6V1X59X32mlaairzSV2d3s0kfud1nnAx9gY1PLIUgDiI8XzEJyycaLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7ae037ce.mp4?token=YZmn32LIFd11zouGvwtxvO6pCVXHB1E9LEK5Wu_jY8OH_HyQZMshGgPAloE8fcPHF2cIrSvBgP35V2wyUThSHrQtU2ejCoJ7tR8kOdel91oi7qgmpkNC7xdzLqBYk8Bzp4-veFZTRlRk1aWdWApdu5-Q2YfQU4kp1Q6gcGrFrCUfpmjxAlzrL0iTqyyOLhWBzShqfulwWGpFRsEIlcFdPMLNVHSfixPnWv2lTQ9J2bcd1lpQBE7QMXHOCGzMALwzKuyqEZg3rZaE-FzgBu492FBdpnusJR3ydSgdkCKpTjxkJRdrIfOPLGFId7E9RrYNNCptnKFDU5iKUG4iSdVH5LzJMQOW2pn7mvaD6ggfxE-VE9crH_KUVmfOvkaHWePXUijwBQ7R6oOTVOo-1lF4RYkdLq9qK_60F3-InoudPplNw1gRlOaNPZ_niYJQg4kDswJ3IthjJF74UAovNfiLLu4WfZl1sxKN0RfeD_YlXTWiBfRiySqNRUYceyRUEVQli1N9iGuxxtgXJrtwsm2zjD9fjN7Po1JBfZUCnVd-8vsVo1p2HrzeGAT5VXGqnZrzfxeKcRz6niWW4_ZH7sGRvYAbbcard8-gm9gTy1nf7VHR7yLERN9J6V1X59X32mlaairzSV2d3s0kfud1nnAx9gY1PLIUgDiI8XzEJyycaLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔖
روش‌های متنوع انتقال وجه
✔️
پُـل
✔️
پـایـا
✔️
ساتنا
✔️
کارت‌به‌کارت
🔝
برای اطلاع از روش‌های انتقال وجه، این ویدیو را ببینید.
👍
#اعتماد_می‌ماند
#باجه
#خدمات_غیرحضوری
📥
دانلود
#بام
،
سامانه بانکداری دیجیتال بانک ملی:
📲
https://baambank.ir
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/460654" target="_blank">📅 12:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/460653" target="_blank">📅 12:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8943cc4e99.mp4?token=R8bj6ZX4WdqZC6RFSpWS53_f49uS5J626brhwJGQ2Apys_jwierixFEyDi7BPUnw3eK9F4Q9Y9bF-3BKOXzwNFCaK5ov0Z9adPWztEkCdBIgxFoF70wgmfMurRwgH-cabOhb8Ms266CdVSLYWdZ0fpAxBOVcM6Vk2wcJmZQLaAZLQP44pDo1dRx3w_0tY6QPjV1kD3SIr9sQ06T6vHhk-iSsIxeVnaGTbbz05UgwdkyPO3fZJk43ySkQZwTSAPcyeQ6yi7El_Xqw5ePXL0Sah8hsrhs3bXE2t78oZLUsz8CxTuSAHXL5ySh0KcITysuTV-wdcH8bf8Ft9FGLu2VpZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8943cc4e99.mp4?token=R8bj6ZX4WdqZC6RFSpWS53_f49uS5J626brhwJGQ2Apys_jwierixFEyDi7BPUnw3eK9F4Q9Y9bF-3BKOXzwNFCaK5ov0Z9adPWztEkCdBIgxFoF70wgmfMurRwgH-cabOhb8Ms266CdVSLYWdZ0fpAxBOVcM6Vk2wcJmZQLaAZLQP44pDo1dRx3w_0tY6QPjV1kD3SIr9sQ06T6vHhk-iSsIxeVnaGTbbz05UgwdkyPO3fZJk43ySkQZwTSAPcyeQ6yi7El_Xqw5ePXL0Sah8hsrhs3bXE2t78oZLUsz8CxTuSAHXL5ySh0KcITysuTV-wdcH8bf8Ft9FGLu2VpZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: هنر مقامات آمریکایی این است که صادقانه دروغ می‌گویند!
🔹
سابقهٔ حملات آمریکا به غیرنظامیان را مرور کنید تا متوجه بشوید آمریکا از الگوی اسرائیلی پیروی می‌کند.
🔹
الگوی مقامات آمریکایی این است که ابتدا حاشا می‌کنند، بعد برخی می‌گویند «توسط…</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/460652" target="_blank">📅 12:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8326718891.mp4?token=hDOwtV0lFAeCd0_iq2z25r9zEBU34VdcQr_AYvYjRg2Z4C2GAfvXOogejA81f0-hdw-sWegKl-N5bLJ-ryQKR3IHMrQ0sJBGu9ONGx8ZczgPEtXo0FNuzaWOVrmdvSic-T45s3ekzTQrwGXawbTMNOXWAfCxfqfNNYTZG4_W1FRr1ppskjvcwRsRb7gDueCG77A5Lz7jkpFgICASFQCrZ1Se6BVjQwGXNUmQ6aW12JSDGyvzWtlwiDUtvkTGlxF2nO6Wa9aI3jb0WBHLcXRTV4OSjfz6SJbgDbXlIIC9JimJTsS8fZdmx38nT1y21jm3wJVh9f3zLoEjPktTFjlQBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8326718891.mp4?token=hDOwtV0lFAeCd0_iq2z25r9zEBU34VdcQr_AYvYjRg2Z4C2GAfvXOogejA81f0-hdw-sWegKl-N5bLJ-ryQKR3IHMrQ0sJBGu9ONGx8ZczgPEtXo0FNuzaWOVrmdvSic-T45s3ekzTQrwGXawbTMNOXWAfCxfqfNNYTZG4_W1FRr1ppskjvcwRsRb7gDueCG77A5Lz7jkpFgICASFQCrZ1Se6BVjQwGXNUmQ6aW12JSDGyvzWtlwiDUtvkTGlxF2nO6Wa9aI3jb0WBHLcXRTV4OSjfz6SJbgDbXlIIC9JimJTsS8fZdmx38nT1y21jm3wJVh9f3zLoEjPktTFjlQBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: هیئت فنی ستادکل نیروهای مسلح در روزهای گذشته به قطر رفتند تا وضعیت خلبان‌های شجاع ایرانی را پیگیری کنند
🔹
قطعاً ما از پیگیری این موضوع صرف‌نظر نخواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/460651" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bceae9093c.mp4?token=WIhTk8EzxiGdH55q1pV2kSlbqJl7Kw0yIzTYOBsUQhFQMTpMfbtgJVA16e4XWiXTa_Hk9UM_xzVsOHm6tr8DjGErXo7nG3rG-VIywbDiwd_JgXdC5ubKkWlAE1owvI4Jw0I6Z5eOt0vXoIRHdso-J1Jub7IY8yYQtOlunYVC9K2rev9cyd35Pujt06VteKx00JRJqC_s3W1TPnpxfvVBHG12Y7WXIBhz5rvPaVcCOFc4fATaSkDQhKmBH19KSNTIE228s8gOonkQ7gFUiFORV6KLetdBRsnXXWZwKuPBPy-_GizlPVocMZ1OMUu5b27SmF1ao0k1amTg95uvKghRag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bceae9093c.mp4?token=WIhTk8EzxiGdH55q1pV2kSlbqJl7Kw0yIzTYOBsUQhFQMTpMfbtgJVA16e4XWiXTa_Hk9UM_xzVsOHm6tr8DjGErXo7nG3rG-VIywbDiwd_JgXdC5ubKkWlAE1owvI4Jw0I6Z5eOt0vXoIRHdso-J1Jub7IY8yYQtOlunYVC9K2rev9cyd35Pujt06VteKx00JRJqC_s3W1TPnpxfvVBHG12Y7WXIBhz5rvPaVcCOFc4fATaSkDQhKmBH19KSNTIE228s8gOonkQ7gFUiFORV6KLetdBRsnXXWZwKuPBPy-_GizlPVocMZ1OMUu5b27SmF1ao0k1amTg95uvKghRag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: به‌شرط اینکه آمریکا به تعهداتش در صدور روادید عمل کند، قرار است در نشست سالانهٔ سازمان ملل در نیویورک شرکت کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/460650" target="_blank">📅 11:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6bb9013c.mp4?token=KujqIQ_uHBAzEf4cpUfqRLpQzfStle8Qd4tEuxg6yfz2F0CCv8KHvpJ6Ymfs4ft-SB6IYSc__l1yEW0-fTRunQDx-jiMVnc1gtLHu568sEStpuYavv69WioqXO-mLe82jBGBFMRNNBtkaKPqS3kcrbdimNz0MYnWX8g6egESagbgUicMNCN0B-68nhu8UeiaajZWIa_1RjSbwiwU5YALMkwl5WiN58G0_Aq0YjYplv_XxH4AVGH-dnMzByG_pxSu1REsRKU3yXtLuhhw8bv2o_Achm2fUoG04MVKoWctBUSXqaFaEIKmPTVUPZr03fxlQq2mEbioeIYazVhqPHKA6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6bb9013c.mp4?token=KujqIQ_uHBAzEf4cpUfqRLpQzfStle8Qd4tEuxg6yfz2F0CCv8KHvpJ6Ymfs4ft-SB6IYSc__l1yEW0-fTRunQDx-jiMVnc1gtLHu568sEStpuYavv69WioqXO-mLe82jBGBFMRNNBtkaKPqS3kcrbdimNz0MYnWX8g6egESagbgUicMNCN0B-68nhu8UeiaajZWIa_1RjSbwiwU5YALMkwl5WiN58G0_Aq0YjYplv_XxH4AVGH-dnMzByG_pxSu1REsRKU3yXtLuhhw8bv2o_Achm2fUoG04MVKoWctBUSXqaFaEIKmPTVUPZr03fxlQq2mEbioeIYazVhqPHKA6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: هیئت قطری دیروز در تهران حضور داشت و برای کمک به کاهش تنش‌ها دیدارهای خوبی با آقای عراقچی داشتند.  @Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/460649" target="_blank">📅 11:57 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
