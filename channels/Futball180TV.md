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
<img src="https://cdn5.telesco.pe/file/vbDUPXRmE4AEGMmclH3iI-z3NYy4UU8ToIOq0ntwZy7gCrB49NE9oF1HjSe0ChxWbaFi_Jn4gVQIO4R8SebIFVFYv358Gpk66OD1FNyAsbLFTXQZlmMclvZQGKMRKbCUvpIPb8OXYwOldAZ-w_1eXE9vx3hmASntZOYCgOLSlEaZSc20v8aoFpTSEzvL7GhdevVxzhkk2rWrjwoQCOXuxz5XTGqpLNrDuNZGV_-Ra54ydJ_UZiZDUsDKEntIlYCtis_Y4-W8opPPnYzNAPmcPZZWLK-TjfyCbDHr6Dwtwibio0t45JVYgJy6w0ClQMG7QLy34yKTzkJbcPPp7-cwEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 577K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 01:18:55</div>
<hr>

<div class="tg-post" id="msg-100205">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a763ec0bd.mp4?token=qM-0xfRUd3LwDVm3TG9U0eNc3MBrTUzknIBUPFICsxvLFuGkbZQ1cWBy3aIV-F_L_ADExKZNCXZS6db1RKfcR-0azBLDbTZBJJWyLdgpDwn4G0iw6rYa7y3WENcjtZ0kk6CRry155xvuaVjgfJQfkki1EqD_Q4MjYWpHLa9rjfG-6tR_C1ZTMg4pjWSn-ARsKsTVdQy1wVvcZckjIb1ii77UM6XCndVWTGRbrP5JwsoYZ1i_WshUUobdWiBcvSJ2MTuilnRU5Y_cCLxYwhhQywe8ooAY7Uv_PNFc8vNaDq5R8kgrJ8hshwTs8jyLFRjSNwdut7h7ILFbJVdJ1jj__A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a763ec0bd.mp4?token=qM-0xfRUd3LwDVm3TG9U0eNc3MBrTUzknIBUPFICsxvLFuGkbZQ1cWBy3aIV-F_L_ADExKZNCXZS6db1RKfcR-0azBLDbTZBJJWyLdgpDwn4G0iw6rYa7y3WENcjtZ0kk6CRry155xvuaVjgfJQfkki1EqD_Q4MjYWpHLa9rjfG-6tR_C1ZTMg4pjWSn-ARsKsTVdQy1wVvcZckjIb1ii77UM6XCndVWTGRbrP5JwsoYZ1i_WshUUobdWiBcvSJ2MTuilnRU5Y_cCLxYwhhQywe8ooAY7Uv_PNFc8vNaDq5R8kgrJ8hshwTs8jyLFRjSNwdut7h7ILFbJVdJ1jj__A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
یکی جواد خیابانی رو بگیره. بعد بازی رد داده سرود خداحافظی میخونه برا امباپه
😂
😂
😂
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/100205" target="_blank">📅 01:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100204">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVRP8sAzOrbmYx8vKe2bZogzxPXNKQzH4Ex-gP2P0-52VQkj_aaxE_HHDQZNx6HTwMssedLbyupopxERPt9voqf3-wOPymspJUFEKtWR0BwYaSC0M3YqMc1uhdY32U4cqwc4NsPdrEijiYTA5Klc8cw8GTklgH30vezqZzFWmDewXzC46ubCjZE9MHIUxVTnDR6AW3lfqH3e_QagdZcb2eH7YivbqQsEnQxVR7KK8Uxzc7rb78OEHdfvirgoWw6Pa_SCcr-Up-DPTlaCIq0pw-WfJjHI2jH7TmIYJ0nNCazntIcrXuEswTzvREQrSOQ6FUn5KS9bCrGT_LK95Q_9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">25 درصد از شکست‌های دشان به عنوان سرمربی فرانسه در بازی‌های رسمی مقابل اسپانیا بوده است
16 شکست
4 شکست مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/100204" target="_blank">📅 01:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100203">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPypnt7T3CCfgDBRrcZ7rcwwEFt_K2In-80DRyY0Khi80cZ9HEC1nos7eHBu4wki5JtDSuqLKsGiX97WpvSzB-WabT3j73GQKLiYytUkx5zOVz4ZM744PU_dIjCbfk6NRWAA8WJkSy1Np8twi5rqYANqgBPfhmAmMfZj1DDQ0QoVe1cUjjRD61Se9e1iD8PDkaCor-t6YvuAVALZKp_I_30ptiMOdRh0SUa6yC4_SaBn1crcJeKdH4mxPDAmdO5jCQBHgphcV6pLEeca92gBSOrOuQZAFN24sN5SkG3VYZWeI5tE9011jpB1H4n1HTIN9PNtfAthh3OEgnHAJasnng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رایان‌چرکی علیه دشان: مشکل داوری؟ قبول ندارم چون اون باعث این نبود که ما گل نزنیم. ما به تاکتیک‌های خودمون و قدرت حریف باختیم نه داور مسابقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/100203" target="_blank">📅 01:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100202">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP-fDKxntqfnSbHaqVJmNI_GzHWNvrt-xVDYlniGaf5oUp6q8N_8uvLhfPko5Xyr88fc2Cu3_7uJGR-Uy7U1U8J73AHLqH3HgxqDsC2GwUu6Mcp7w-kW4R0YhZT9UUI21NfOyZeHnT1VG9BByi5bNt1wEy0Fg6YTRw-JitJ8c4U118FxahO-F3kQ_IEGKql4ydt4lze2aEdXadJvNZvpjP9RV4BR1l8u0vcrig5iymMqxrHY55AuszlMIZ-GT7FoSn-r1zHJUkOHD-k0wmxhtt4yvr9MMNcGvvA97m2-jadtdt7D05Vp79mftzD_eGPglFkkha2m9TQMFbV2ANwZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👤
لامین یامال در 12 بازی، به عنوان بازیکن اصلی در مسابقات یورو و جام جهانی شرکت کرد و 12 پیروزی با نرخ 100% کسب کرد.
😮‍💨
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/100202" target="_blank">📅 01:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100201">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrEU_6hb3SpYJWja2-UQ5I8CeY9DEBY8ZRroarQ-JQWaG4TT5qt28LnZfx_mQbuVRcRQZbTtKBwKq3xyg5QNYgl3q2ZlASTgj-cQbihkjlUCk4BHvMUjwxv9pYG3wSvVXfRFFA4TunrMJxetdfYSxXHRK4413i5CGAwQlUSWG3OdvXYfvXjysD7AeKDirROu9wEqcT94Mp7rtEsD58XPZFYj7vLuLogduskx7TSvh9x--5UGahKl4fz_u3lwLo3ZE9I912bLPaGx6q23W7dx3fFGZc7AJ4RfCHKQWlOgjTQd8y3UYzSLjg_jRM4OVl-FRAi8VWWBWPisU0kMllKbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
امباپه در تماس با اکسپوزیتو: امشب انتقام سختی در راه است. خواهیم دید چه خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100201" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100200">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ5_t5pUgO-EbzRntJE3-Hm3Am_mang-sL3tpT-rqb9qGAcaHm1-dZ70nl7MMgDgTo4VH5IWhB6VYVxIzN9hfLk9AvUFbw3jL05WMoLRmSW-t2NCIRSXdzbGvJz609qpzOs7m8gYQmQUyOBodl0BVE5BQjubPKmBON3zl1vT-ZTmJor2MrKz_gtTZL8AGZ62umjgt7_07XFWm_nKyGa24RkoyFrPsWnvUBSYR-uct-WJFzskqU586DHe0BV08yeDyLm9y2S-iWM2J3oO9IyCIi1OKU1SQKLtBW3YTvTEtyMzttn4BRt6QIcXXEmkKOpNNhh-1c9EhMt8TeLBCkmP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100200" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100199">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256044b0fc.mp4?token=m_ukYFcd4I6QMhyElr9yAyr4ZNlZLIqx9mTVa5yjq4OOqbKugYZjmaE9UEhER8kLuBEoju6fg0-_zgcdZZRO_PhpxWlEbyPh1p65mzTZ0rmydq_-5XwZqMYa8Pw0H27rIykvUDmZ6uH7wu0omnBQlefYLvxXJrkkEq7AK1x7c9b-yTL4HAtlrdK-sGrqFbbTYE-tHZjX1EG1rCFqpMPtLRRf5dMwMVEgW55qRySDjLdGxuJpCZgNJss76BJhquNlFF9uDqRQOUc9foGjoc4nwlQDTMg1fhSfalwUEH8-5SAUBNkTHqFOZSEVy40km7CFWMeFBpBTkEaDEZ2dp7n2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256044b0fc.mp4?token=m_ukYFcd4I6QMhyElr9yAyr4ZNlZLIqx9mTVa5yjq4OOqbKugYZjmaE9UEhER8kLuBEoju6fg0-_zgcdZZRO_PhpxWlEbyPh1p65mzTZ0rmydq_-5XwZqMYa8Pw0H27rIykvUDmZ6uH7wu0omnBQlefYLvxXJrkkEq7AK1x7c9b-yTL4HAtlrdK-sGrqFbbTYE-tHZjX1EG1rCFqpMPtLRRf5dMwMVEgW55qRySDjLdGxuJpCZgNJss76BJhquNlFF9uDqRQOUc9foGjoc4nwlQDTMg1fhSfalwUEH8-5SAUBNkTHqFOZSEVy40km7CFWMeFBpBTkEaDEZ2dp7n2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
ولی این صحنه خیلی حیف شد که اسپانیا گل نزد. یکی از بهترین کارای ترکیبی جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100199" target="_blank">📅 00:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100198">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHO3u6afEhdTluGstwaXDR00Qwoa8dITvv27v_quWEV3yNxojid6OHYOIHpPnUEaW7EsVTgjQ13tODl0rsjr4vkH4HP22z7A4IQkBPnsANZB76tI0lcY5tUrx5T4Vfaj8fX7pFHxYvioPvrALAgwcAZqmbvlc_rE40dEVWoPs5u4A6Iky39BwswT_EUGY_JQ0o34txU5OC9lrKlVCvWtlMfzPwR1GnV2DT7-vgAEGw5T3QVV898JmrKlt09m9podKZrVtC16u-3_A6Dx0pDJ5yD7zJHdX0PZ76j65hTz_UT6viwd3KHujiGwE3-kPueOUGLf0iNGJ_lk3cTysfqvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
رختکن اسپانیا بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100198" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100197">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
❌
🇫🇷
دیدیه‌دشان: یک سوال جدی از اینفانتینو دارم. آیا داور امشب عقل سالم و صلاحیت کامل برای قضاوت در این دیدار مهم داشت؟؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100197" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100196">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a2aabbea3.mp4?token=vgR0ZitOBq61Hlb1bGt1Mpe_z5BY4wHmyYtTwpDF-vvqndvgxAdO5om4j_PHjG83zjapUFHmo0GwTd6yUg97C5cOVzXp--rbPxQiT4_PzNsjWYX-fsX5wkXVEOyZUb1l3LDv7YwzTApMhqCHF1e0v81ozsfBEGVMU-rnexQp8ujz680e92zhcW7bLLPg6gtjqMeKPmtmSUviy4woLPeQfA0JTBuy514fNvlXZPU4WO3Toxrpnw-AWXmTa9ciWc432jyJdbihvDZbmEbHFai702UHKn1qLaU2E3g9yeKdonLO_l1rcveVo44f2f4y2Ya7TaQlvL73Qzve4GrxW65eYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a2aabbea3.mp4?token=vgR0ZitOBq61Hlb1bGt1Mpe_z5BY4wHmyYtTwpDF-vvqndvgxAdO5om4j_PHjG83zjapUFHmo0GwTd6yUg97C5cOVzXp--rbPxQiT4_PzNsjWYX-fsX5wkXVEOyZUb1l3LDv7YwzTApMhqCHF1e0v81ozsfBEGVMU-rnexQp8ujz680e92zhcW7bLLPg6gtjqMeKPmtmSUviy4woLPeQfA0JTBuy514fNvlXZPU4WO3Toxrpnw-AWXmTa9ciWc432jyJdbihvDZbmEbHFai702UHKn1qLaU2E3g9yeKdonLO_l1rcveVo44f2f4y2Ya7TaQlvL73Qzve4GrxW65eYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکراری ترین صحنه دو سال اخیر تقابل یامال و امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100196" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100195">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇪🇸
کری‌خوانی دلافوئنته سرمربی اسپانیا: امروز مقابل یکی از بهترین تیم‌های جهان بازی کردیم هرچند حریف مقابل بهترین تیم جهان شکست خورد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100195" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100194">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr5VUiAmevuZSgzk1ivcTG3mosbdDTyad9LIwpt7NwCeegYBNyXd3zykWNquUQHhWxGgHnUXbrgshKW3WbqguY9kF8zlzGrxxRexwET9o15yEgIh2MlkiM6dwNVr5kWCCOuTTgerGYUSLyLVAnnbl13nrCu8CxC2wjbVgkjktJSD-gcFGMplK6ihF0E-BHdQ03s6Qwchk0Cdb9KHHCCCUrmuJczt8iRzbFhzWjIFi7veEES83KCX0rWiUFdt7CijEaewVmMINKzyv8sIcsW7oFPzURYUTK-3lNcu9jh8sJ4_Oh8d6I2gdKTwzjt0x1t0VxHgfmP2DotJE-IDahQ_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
فرانسه در یک بازی برابر اسپانیا، کمترین میزان گل‌های مورد انتظار (0.30 xG) را از سال 1966 به بعد ثبت کرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100194" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100192">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyPnKWAPNM3vIxHpvLpvks0CNqfCxI3AjdoxES7Bn59i4fBv91NO56FOz6hfnDXsRJPMIMQcIXgFfgBpnMR7KVnL2WY4an8llDhopdkW-Q88r_CfvKP81wORTd3uUwWutBuAm3WlGJC8JLMsftDq_lb-Xd5bMO6B9S_uhvgg81oYPJUVK8IjbE1GML8XvaRwDjhtnsf9ielD68BJc7i2wqtOPPhmM--NgHnxqPuOC2VgreHUDeTO8fPWLOrNSW6W8VUeVoAYmO-R26gaJCIEu97rxpD5HrrKXgM0kNtq3K-EfcWNXQN4USY7bymd5X0MWMSwMkqpuU2wdmwl0PdnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
پائو کوبارسی: کیلیان امباپه ترسناک نبود. قبل از بازی هم گفتم که ترسی ندارم. من در لالیگا بارها وی را مهار کردم و برای از آب خوردن آسان تر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100192" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/BpliGVFJAc0OLOsfsAyXZAEEGA0PNMQdY3Bc-CqwteGKgL163NNHzIHZgPH8_XD-SXnV71rOGKGXpaj2P7C3290GVGZE6nhHT6kDZrNngNGlsomxCqf2PLtBZEnaBNd_Lc92l2MLMcXlA6B1Pnk_h4FJk5HUd8z_iSkg6p-alzXbYbNrW2wfFAaqvk1s9tRQgn5KOnvweEJfOaXZ2znbjZdQxLts0Jmn4ooZ1ywXn2YVq4Yfp5CHlikDflSjBQk0XiRNWxW9KrK6RuU2yzLBPdvaIkH3695PhzckyM57e0fCKHbpQTuW4REDMOsOd4NJjuUyZRSgl2mB-n-iBVcnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/oZdqeIMjc6E3bgqxf-P9WN9deYLGKvzhOf2-QnyxTryNxDflwgq25UC9cUcasFWPZSmQKqRjEIEDVSf8sKeGAgr8w2eHbkZm3NQFGZ1iYZi4V_NY5M8SafRwcYwEVYOcRUUk-m6Mu7MCJ_OGRLDcCRG9HIBj9jjCOgMFxPmCFb50SKSytXyJXUWCaINi_WgODasc3bHaNOPhPTgXM_t7_N20iZKIeY6wDRMBh2t7VshJTNJFVTSqYxMC-ScmJyUwFBZdphAseY3BAlJEhBGSOKcvkkUa_bjawTD3GP0oizNo6R2fiE7pYpaffQsL-3Fa9bRfA3aEOhKrMPxdEQP1_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه و این حرفا
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100190" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100189">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DCJwSRWLKebqwAZiP2D04GncGRs1RfoWrYQJEZN5_lFaHnXVqT8XuY1B5KhQA3T-wEOb4foWzevCEdXB71TeILbP7kFKo59eOqDJdv-HIeSXWTOdwZnanTWuXjH2OPDUX88U7aLY3YaJ5Dt-1KOemqgXcKKTRMNY93acY7Ix_kkD2uhSVdsy7NNuY_U4ZVmHs_3CWJg39qUlfPu24cE4UL4PbAUBW_r1ojCZqw4wU0QYCWZQFbDP5lctpn1RCRnYtoOC7vkrZKJGR1ycgdCGSUb-EYXKygGQ8xqdPcH-5Mnu6ud21PQYNJZSQluJcLrnfmg296r3Ff1oqiYbW7M6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🫡
🫡
🫡
🫡
🔥
Respect For Olmo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100189" target="_blank">📅 00:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HuPZ2MLU5yv1GckVhp4rtjFcApsiEbgQA6OstD8p6nRstLQi5mrfUcNiThky0xmBsii34igCb9E16EAmRB9QC7umArbBAFd7nbBKBynxDM2PIhp_MpFS8zgH9S3pH7VQe4WPxMA7EQaJFx_lGLyN0pJWFJzvuKsx8YH-bwJpDPtQ0YdUSu7NIdTzyjny4JJ9pFvfT4aY0H-Ik2MYPGjvMLQ00gu_roJcNUpdY9L-M_7cTwklvOXJqsfnsoa6WfolEZXYur0f7n8M5Ism7lE3Abt6RT8zxjQUPwEgOcH4eRP68AC6c5T4OVDH3THHtEoels7yA_Sacl0VpPjm1xBV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو کورتوا امباپه بعدی بلینگهامه برا
شون
زانو بزنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100188" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100187">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قابوووووو از دست نده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100187" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lST0Sdio9_LZqkvqmL5hf1WiV1TsMxIKWKcoIytrWv0BNRb4UEXDGJObkamJoiXIGY7IwAtVhIEcejDHxhnciBlDXOHxOmKfUnwmxw2URyMwqYDidYfM-8V4PrYi4cwQ_uUtuVDZ4JxmgYoXsuf-lm2XGglbo141u0tF-nXudbzFpAtJ5ZPQJ6QCCSXD8D0lhZMu2XfG12x3l2eWJ7yJiZsH2hRwwCWVBI6tWMFqt0QqXxdMuL_ty3WKevsVUiX93O3C9hhIZKs3aGXqhqYIGRq0E2YstzqyPpomoyED1Nc4Tt2WULxOndh6eooTxf0IbFmctJ0_jeI6__tjtA7Nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
#فوووووری؛ دیدیه‌دشان از سرمربیگری فرانسه برکنار شد و بزودی زیدان جانشین وی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100186" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100185">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohSfqnqTG-_7t0jyUUTHUE3uXaJULldH6Qq7w1eRRb1kgwPfC5Vb3hzdTGcI6v-CzzBLxnn0GvvIYeFJHsOmsiAKvk4p-X58Gz0LTJuKlB0gXzbg9avZxPSHWJh_DJjg6AQst90UhkHBd1NaRU7G0u2Arh7KeGPbOjDHUxLdRca67YDk7Y6jdon-reAaBlngztPVNCCSb8xSGpSHIccS9pzDItkrDdPsJ4bSZOlGCdXaTityuwm_8v73XaiytYwyik5qSbE8RZ8c8BRFRaK9llRuSqXYGSK3dX4u-tQrP1lkxsghe65bfsXjZEHTztqBLrFykabrVPe__8JswxTP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابوووووو از دست نده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100185" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRtsxAAKalkVW3AT8lhh1S58yELgd6WYmF8P8-bZVrb964A-AOcYEYSx0BSPdRnh4Nl97vMqcVrfeGBxAsgA6v48gSIio4Rz_HS8fSdhh1LfJr8xy-atGU6cQCYttg67Tx0IPmqJBMKf_H5HF7c9TUmcsdLHcEUj8efMwJeUbHchyHZeFw9rl7eoBX4ELI_S2vu6WSHadQOZsuJrbU8A4ggrk_EJVDjXeskL3ZyM2yUxkR47-qXbiUYHRKZyDOT2JTTTAJ8gMK6DOgqvc4196QdMuidwEuR67E-Nf7eGQ9zDamrt1m46rRft_TkQ_JATbroeoCZJhvacDRuTcpoNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
نقل‌وانتقالات تابستونی رو رئال‌مادرید با خرید کوکوریاااااا بردددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100184" target="_blank">📅 00:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فک کنم تنها بلنگهام موند و نصف دنیا مهاجر شدن انگلیس 🫩</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100183" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
#فوووووری
؛ دیدیه‌دشان از سرمربیگری فرانسه برکنار شد و بزودی زیدان جانشین وی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100182" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRAYcbWz0GFcMkBFReri37tRtLVnrUHv_Rdf-8uJSdoERi0ihx2UHgolieir-jUHH_LY-dgs57BLG-7NU5cH_Mr-rSL6gsfck2Rd3dj-HESyG4tKkHKX3iLzgVOqjs6sgR_sXfRogo7K9PU0VwQGiGj1hpjIqwvPsTTByu1zgQMco_aZDk6z6EvJIZzcS8POoBVI2wAeCCAHCwjFxxfUxH9lGpHXRAQMMNtFdYNzKRLwDecPxoYilkwIkqw7uPoOfTEcj33UpxuNXspk5hPxoDz8V-dUwb-bDi0qzSU1QBhYi-xofxA9NqdQEOjRq9D3n-nritWEinVeec3IQyUjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛
کیلیان امباپه تا این سن هرگز از جام‌جهانی حذف نشده بود و اینجاست که یامال 19 ساله وارد می‌شود..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100181" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/sIIXoANaDZx76DdM31dsCu7QKlLZs-J09zc0eaGglH2t-npX-JZFCdp-u0tTEVj1VLyT75wT1OYEV8LsG7MyIc5QFswglo69HkRQLlesETLv_d3y6zqWAHPyQc3hXxzv6GtaPsh6a5cUxl0FHxrM-fdrTKZZS0qL-nd_LlVix2rk2KOCMm0N3GG6iJYT0o8kV8nP5T8bvi0F3t7M29Cdx8ZrIrAXREn9ppgbwDhQbxaUt-WXnGnvPOyiyV3RUodykZxUh3bc8odIH6JBmocX2X8xsdAh8tWvqab0OPYqQqGl2mECQ1nMGPGKja717mXTP187nuU_9T1JSFOsSKFQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل یه مرد کری خوند و مثل یه مرد یه تنه گایید تموم تیم فرانسه رو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100180" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCQov6Hh_xCl38NAEgGjA7np3yF_BLTSjQMn8x3aKm5q0gk1RZPz2EUcOWOShAQnvIUJvWx7UtcefAFtIJ5f_K30QBM5X_CSdiWnZbLOdJgMt2JthS8ODb-r2e9IVWv1IxipyBS2eWL36Dum_igHGisjkx7vSqClUyL6ncjMVs0JDF0FrasbYw1AIPfnNs4mx__liLM9rBm-kAUW3hIl27Wsr40GUTD_0wdmzTdd5NZEJvcfpiJwbkSmTP_ObjVEG8K2dxgqM2KoaPifXBQcey-ZJIp4dvzHkCWBLDf98Qe4bwfR8cr31XAq3zSyrRmyjyVI8tTHAQ4VWIgMI3L_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🔥
🔥
📊
اسپانیا با رکورد ایتالیا برای طولانی‌ترین نوار شکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد.
✔️
۳۷ بازی بدون شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100179" target="_blank">📅 00:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100178">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOr48PT8UYGVfyoNeezdPoLNQQwK0tPAmCIs22YmElLZaN6YD6UAY0FL6qv0E_DctoPbdb_-lH8wCRts3I_LZ-3nlYT66ItYAKhC8ijO_wRa7aZvrRCYcM4AtOsbhuZ9SFlVkOkS1ZMRKk3lNe83uTV_tX2VRIrMy2WR41jOQkGXFbu153z1ddf-GoiZlTte7ZgR9Av-jAJBCKP5RJenEuA5etsMp-cSjjHSMkpR8YAKIUqQbTzroR_HnpuYe5_7eNLRcXmUDY3SXHfs-3IC3uHeU9I9lLK-sWuWkG8vNRcJ7XlRR5YPZJrMZD9QfjYGETyVYP5gwMsHrx5Cbydrsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
😆
۱۹ سالگی کری میخونه و حریفشو میگااااد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100178" target="_blank">📅 00:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100177">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrmBXhiH7Lrv4gZCuWQAloPh_1Bms83SdzQv6j08Wd9dleHEkesA5y4bGcrJm3LutOLL1Po_dz0jaBuVslbcWl72STy6fleO1Sc2V0BIyq6BdTR-fSsK1Kkb28m1R0kQ5x0mh2vLdJDecqfrCDXHIGl92DqJcPkcaRG9wIVCKyjkSONWW0HfRr3NWUPZyyHOGQ6m4v2mxHr74BBufMzd56_VJcmKfs_XpcmrhZ8cFFp2lLjpC83Iv0g3hBNLOve5RgyM7MoLPEZFzFZGHrlr2qA0ut4evzc-PQmgEDMsM0hLFnpRJoEpB4Q2J_5uI57AxlbYFqvG9ZPeuCidQ5RLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
پدرو پورو بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100177" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Byibf6bapnRbKL-tymTWpAzY2o4FYUJ86ivbbwbksPI2Fe5-cyogZYTOSloKDmODopc5r5mKhB-rA5FtbKqQswZS8BLtcrLngaataCBUewLQAukMhrfE-0hl5F-O9ktKvS4fqOExh_KMSdNjqVLnnDIjrJXzBgHPFEt6IRvCmgMFzex3hVjuwBzkUARu91hyRYWXp3dyEyr-sWk3Tk8NAqMzT6tGCQsFIFcSxdi482ZvYpljahKdpFs6xPxErGUJJWL_QAlkiUiGP0eYFF2j1VaCyLWqj3o3W2_wjU1cuZWFtHhjjkMdKSRDKxV7ocYXebaO7-DMqsSGHjaD7QZfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه باااااای بااااااای
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100176" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100175">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🏆
پایان بازی | ۹۰ دقیقه شکوه اسپانیا؛ فرانسه قربانی فوتبال تماشایی ماتادورها شد. خروس‌ها با تمام توان جنگیدند اما اسپانیا برای فینال لایق تر بود!
🇪🇸
اسپانیا
😀
-
😏
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100175" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100174">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHOddRHjpejIQse9WqXgiyF8wzy_9U-L1fdJKR4DGgxYOZnzduBY7fZ066AgkOZoHeqoJRcuL4VA4nIW3SHFmzc4sUnHhapIPm9jYbe8dNcaSA9ICbaIBhz41pPZnPvZy1dse0Lvo5lBtipx4PkVDTqQxswJquG9W7SKyuTiXkY6K0z6_fTmSA_BZrwSKE_AEsuqa2_Mj19Perp0v5Qute2Pt7FCR_FAJR3J4cnvLyiNKv54mASXkPhBOjkerWXCklfjBoUXj4uL8BqZYqQM27sGdvE2e-iDVoFgEAPpH33MDBuTZkrV9oXiKcZCJfEbfaK9ORA9FIl4lYKOuY0yCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | ۹۰ دقیقه شکوه اسپانیا؛ فرانسه قربانی فوتبال تماشایی ماتادورها شد. خروس‌ها با تمام توان جنگیدند اما اسپانیا برای فینال لایق تر بود!
🇪🇸
اسپانیا
😀
-
😏
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100174" target="_blank">📅 00:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100173">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">امشب یامال نشون داد ریس کییییه
😎
😎
😎
😎</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100173" target="_blank">📅 00:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">۷ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100172" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏
🚨
🚨
🚨
🚨
عصام الشوالی:
‏به نظر من، توپ طلایی سال 2026 به سه نفر محدود خواهد شد:
‏لامین یامال، هری کین و لیونل مسی.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100171" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امباپه رید تو کاشته</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100170" target="_blank">📅 00:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">زرد واسه امباپه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100169" target="_blank">📅 00:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Knovjh-P5GG7U74mwwfUWeNJ-FSMYDRs6Y4axonOKq7Gln68b6TP2IbS2O0I8So126QCcTAy8YJAdJ5s_AznZvowhAI4hJq48EzFvmOH7o21lJ9NOrvtSUWqW1KKx9E_gIHYgmOJ-elBR3AkoOoTt1IxZjRgOw2Gfyminmo-4ZdesrgaYe-YY-cYOjzemB3ZnMMruQxIDksBohbOcRCof1HEOeTV6yFO8RUUsaXxNq0_YWs-Cfg7b80ToaOOVtW9DQ7DIBcyDeJMRATsLGxXDq9V2tXN7WczI1Lii7HUsWbkgDIwoYViJ0v92ePcABFYvVN0WlHyi2-97w1fOgqNVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار لحظاتی پیش دوئه
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100168" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100167">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یورنته هم بجای بائنا</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100167" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100166">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نیکو ویلیامز به جای پورو وارد زمین شد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100166" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100165">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سیمون گاییده شد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100165" target="_blank">📅 00:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100164">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امباپه به لطف یامال امشب از ژنرال به سرباز وظیفه آشخور تنزل درجه داده</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100164" target="_blank">📅 00:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100163">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چقدر بد استفاده کردن از این فررررصت بازیکنای فرانسه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100163" target="_blank">📅 00:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">واااااااای</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100162" target="_blank">📅 00:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRBMm6lGmm8fxG847zDkjSpAQ97yGXgCMpT2LPzbMUwyVbFfJrZA06XYS_BhIzh6xoyqWmgatTIFRh1rXNdiWv549eGneQluMooszzAjodvd-bfcjw58yQxi6NYAQ-br6t1AlXK2zD0yh0m8CPRhYl_C69nBAh2xSgR4dXLa7Z1DqikE4chjRDCkFIsqfgCl-CWKygSLJfc3NhfoMAgHbw2jrlmSjQTJ9-jGKGsQhGnFa3DR8_0i9WF5h0cWpi1v4o4REZQs0uYKSZLpEredKnkNVhyMNsCF9ixS2s2k8VA90Ov6r1p_6ujbxnxC_TwwCMul08t3rzZWCLuvacEjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفیق رونالدو وارد زمین شد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100161" target="_blank">📅 00:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100160">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اولیسه امشب جوری بازی کرد که بایرن‌مونیخ اسمشو بزنه دیوار مهربانی</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100160" target="_blank">📅 00:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100159">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اولیسه و دینیه رفتن تئو و چرکی اومدن</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100159" target="_blank">📅 00:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100158">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">زیدان هم بیاری این بازیو نمیبری اقای دشاااااان
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100158" target="_blank">📅 00:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100157">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">لوکاس دینیه نمره ۵.۶ رو تا الان گرفته</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100157" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100156">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dcwa7CJyJzXPtNAqfKNO3OVNtpW2M1Bcx2Fj2KZrKNU9ijshxBov4oR3X7JhtZWcEndhDSTlCOaKNsjW7KFaAJzjxwExsTFAdtMoT6bifdisO5n5V3uE8Qs9F6xKB1b4qkA4lmSL0ZYOjBF3b_nrB0pPy1vVE1EOx-P7cCh2csUHJ5qG7zlm9RN6y2-vEZosXIQ7ojrYoGckIXgDMh3JEnBI2iFk1x5M97dvjrksBRn5Nbq_MVq5ZHcKPZ2a6EeZl9hAxY0i5XPR1arM_aBXV6OfMY4Jnb2qHbMIVNLiFnxB1m6pyGMoh6LQA221ip2aIsdOaWwDBobIpNzIcvFCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🥶
🥶
🥶
تو ۱۹ سالگی ترکووووووووووند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100156" target="_blank">📅 00:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100155">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">امباپهههه داشت میزدددد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100155" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100154">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100154" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100153">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فرانسه این بازی خروس نبوده مرغ بوده</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100153" target="_blank">📅 23:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100152">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلللل سوم ولی افساید</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100152" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100151">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c10bc62198.mp4?token=f-lwMKMH4wl-mOx2tEjPehJf8_WzwEEwAvzD8zGWZK0NQkMR1edXL5t0oAL9pXnc26zrSDNELJ6E_g7-U-zWqOJSCka6oCogciH1vQQ3dy-BLv9DNNypwYaWYy2K5EWBdJHFon6MgIm0CGjdYQ7YqWLQzeN4L9zOIyJQY1sAtj1yC-Rcagg1Mz10H2zvW64hHk-X0-LGbZszyq4gkeyOW5div3oe7GzmKNPhSyFp556BNf4T16LDaNZD8D_F-esIFdzquuNSUrNlydRlNwyFVdq_cbkWEo4qs8FlZlBMa9LV-v_X6BHmYI0BfB72xFfFDullHxniKzK3fFAUdZi9Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c10bc62198.mp4?token=f-lwMKMH4wl-mOx2tEjPehJf8_WzwEEwAvzD8zGWZK0NQkMR1edXL5t0oAL9pXnc26zrSDNELJ6E_g7-U-zWqOJSCka6oCogciH1vQQ3dy-BLv9DNNypwYaWYy2K5EWBdJHFon6MgIm0CGjdYQ7YqWLQzeN4L9zOIyJQY1sAtj1yC-Rcagg1Mz10H2zvW64hHk-X0-LGbZszyq4gkeyOW5div3oe7GzmKNPhSyFp556BNf4T16LDaNZD8D_F-esIFdzquuNSUrNlydRlNwyFVdq_cbkWEo4qs8FlZlBMa9LV-v_X6BHmYI0BfB72xFfFDullHxniKzK3fFAUdZi9Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100151" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100150">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
خوب این‌ پاراگوئه نیستتتت عزیزاننممممم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100150" target="_blank">📅 23:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100149">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پدرو پوووووورووووو</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100149" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100148">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فرانسنسنسنسنسنسسهههه نگایدیدیدیدیدیدیدمممممم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100148" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100147">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چه گلییییی چه کار ترکیبی اییییی</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100147" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100146">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسپانیااااااااااا</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100146" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100145">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گلللللللللللل دومممم</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100145" target="_blank">📅 23:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100144">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">داور قشنگ با فرانسه مهربون بوده</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100144" target="_blank">📅 23:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100143">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آغاز نیمه‌دوم بازی فرانسه و اسپانیا</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100143" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100142">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ربیو رفت بیرون و کونیه اومد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100142" target="_blank">📅 23:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100141">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9XyjXFg_y-04G5-n938kAqPVjQ02UXoho2o013fmXwF1oL4Z06e4DRjCNsrrfhlBi7DDIcDUCGdGndiZV1H_H91H_-YtzLyH2yyYS7RQe-3kdDBUI_BG1Zhk_1r3H3Hv-9lOgD3GbdQasrjaj6yOxHpJNmSOgUWCe9WodIWmMR_2WTzV5cx3DIUNyHLSBBvkt5v98D9EzSJ_GRiy8hV01FiflBHlVb_OCMIhP9dn7Il0XIrm6D_XsiAx-jEYmvhOz_RxQJX6OauHFoIX8N8PEYTJvFsfiUqi4_dV_AN5QuLyCuq9G-4DMtCta7VyMEEUN4zbuKfq_P1hD39Azy76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آمار نیمه‌اول بازی اسپانیا و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100141" target="_blank">📅 23:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100140">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فرانسه نیمه‌دوم بازیو برمیگردونه؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100140" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100139">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOYtd88NHJS8MesGd3skJ9GjEThjK8Bh7JXJSINIU6QlSltatN-PYH9JDDB6NqdGdi8pL-Z6qvRdAjlaQl3ZEpzGmt7H6NqJHeSK6a4DILrrDz5XS1AAQB6GoVgVcyjCsDpK7d0lY4mBQaOJhgmVehmOKcMZLBXblQ04Roc2glj4xSprGYWtI9c6xb4zZ0_f3_ChXB1w__D9zXFu-qKekDsi0jD64LGNf17OZxicrAkxTAtpd2vn5zzVVn5j8nOxgmW79AbH1oaVJ-C6eo1U31n4NTpQOKT6tgEhMGpGrx9LHNx348Y3kqKK9pY9Q42-QEJiGCVSuBq-NZDkYeZUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه نیمه‌دوم بازیو برمیگردونه؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100139" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100138">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gxH_vOvkdhE7_tknhAhy8OJkDg0obqxphPJzjP4ak1LDxLj8JVxwj2U2pcV1fhC_PAZUf_IzILIoygqM10ny5v5ptA5CQbS8U7BDLWN81KqlaLRKLv3RXMZBU-WCH_3P7pl9GK5qu8AofWHoO7FUUJ7XwnKBpbbbQ1njV4w1vcwuhj_vUYfzflr8MJkupBS8SmcePCVWeGUc2P55AJtnws23bWSZ2S_2mOPvAbleeSho405isl9CjbpAhPXp1-tJMin1n2J_jedEcL5tult-m7JroU557sWrmMuMKRfD08HkDZMxRfEKaPRCKsDggXO2C8K7_jRQ98k7nXRzmFep6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
اولمو امشب تو نقش مسی داره خط هافبک فرانسه رو میگاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100138" target="_blank">📅 23:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100137">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoBKJ7RHokp7iNXLJQVklA0FH4nEPDm6S7ZfP7yOY9fpSFWHvpzUmQFq4wWJaExTkUj96jgBZhtoEHNDz1gn7AbIVdJyEh76Fh-E-i3UzM0hlKmx_dn_ZN_MKoxg49FLH2qSCVtXrzYSifWN53zxyzMykLA9v2kyaAjNVYmZGdHBZ6DO1G1hjo7reQ1ksPQ8rGdkzwL511GRypwblv5nsBmkUIAgAoJgpT47aKFZtfxwM_BeXT7jpcY_MJL0h8Agb6tM4m2dqmk3rTWMbPswC7YsIbdc1drKVnRzvorianHNcEStarKyeKAqKoXv4MYvCj_NE6A697CMNaLJ7Zkmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آمار نیمه‌اول بازی اسپانیا و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100137" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100136">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9ENgZ1Mwc7gHBEyJjONQHET5IrRZUQHFL1iLM3tbywXZoFxggFyRtoMVk5TN3Oy-sPo0jsxiXCf34vXTzf6SpZuRCIJteRP0d7WOSoxNuXSzXDgkE_0P-SPUiTR0zlVogjI7kQyGpRvjaB4NdFfBcadF8RexcD3iBdxf_PtKeUk396YR1ALI_RAKZyjCYXCPNb07DvT357amhFd8Gyi7CmchCUfDcc19EupZdNV4OcbNKp8QIIBdLcsHZwg6SvJkuL55IVJxp4vFSl7IvEV4ozdV6A5qeMd5Inf4VROFLHIyCfYxrSHKEuGDoPjHCT_VkqamDejENQXgE_ir_ftXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
برای اولین بار در جام جهانی 2026، فرانسه در نتیجه بازی عقب افتاده.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100136" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100135">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f951af3a7c.mp4?token=Ye5yv-oVI2P1TqBbzbY7KgNDEf4IxddS0p2dJOxFqh2TliuiEVJL4T_Ypw7qDHc_iWqwSceSZWCyNgsnLJLFH10F40odXxuUj3BEFAO6XdBN9ije538pEz2aVp95kOLoujnsiE4K97zUT0NzeYP4jCi4cky2saUEGWVM7an0CFXlASIZtZSSAPRNOkvwBbrZYYRoxzj7BwuDeXsCFdrmmqxEqVRbSVbp52l0Ro2IKC_9vRwo3aOCT-enAMvdwWQRVFBzjW49c4BMNRFsEAEtoJvEsE6lYh2D12xYetyiccCOZiF8YIX8sHTx-kdcHCz-GBBa7PYZ0_A-gPP1-ioQZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f951af3a7c.mp4?token=Ye5yv-oVI2P1TqBbzbY7KgNDEf4IxddS0p2dJOxFqh2TliuiEVJL4T_Ypw7qDHc_iWqwSceSZWCyNgsnLJLFH10F40odXxuUj3BEFAO6XdBN9ije538pEz2aVp95kOLoujnsiE4K97zUT0NzeYP4jCi4cky2saUEGWVM7an0CFXlASIZtZSSAPRNOkvwBbrZYYRoxzj7BwuDeXsCFdrmmqxEqVRbSVbp52l0Ro2IKC_9vRwo3aOCT-enAMvdwWQRVFBzjW49c4BMNRFsEAEtoJvEsE6lYh2D12xYetyiccCOZiF8YIX8sHTx-kdcHCz-GBBa7PYZ0_A-gPP1-ioQZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت اسپانیا تو بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100135" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100133">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
پایان نیمه اول؛ اسپانیا 1 فرانسه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/100133" target="_blank">📅 23:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100132">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100132" target="_blank">📅 23:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100131">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اولیسه خیلی بد بوده این نیمه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100131" target="_blank">📅 23:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100130">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">داور گل کشیده؟؟</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100130" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100129">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خطای خووووش جا برای فرانسه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100129" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100128">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خطای خووووش جا برای فرانسه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100128" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100127">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چه حرکتی زد سیمون</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100127" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100126">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-lUnNS8JkUH72wH9RwXONEoGUQAtXFpo7yHr9if9L_4hUSI5lkvtLgtfTixk6T8-yH2NWk6zCN2OAfQO_nHsGSEul9q55KuhU0z17DPFIl20Q6RX0mUtEMqPkkIzSEGp8ZEGDIEMSdVnE2FGyStdzTlB9WgxerHxhBBT3t_mxOztNq8hbxuffZ93BHUzsuHYIyzQPvAsMMOzFRFmIYAMZwxhOyjcUmtxLMEr-kB2D5QDTF1OykOknYG_p2Wttvms2au8bgupy5uHMQ4BhtLk4UAGnZGxtTOfwQWc7v8A6pIKTRO2d6qfxHVXLamfgd00Vpvc_PY50JCgAUU1wB6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🥶
🥶
🥶
🫣</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100126" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100125">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امباپه همچنان تو آفسایده</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100125" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100124">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">امباپه همچنان تو آفسایده</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100124" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100123">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M47c7NTVwfO_6shz1JdWvFOMMCnEfiCxQGv_3PaPJfP3Ad2sgRK92VoIpr73KOGTNjQuRbNjHxJzIuZTkpaDZDGe-byK1dWR2aDbnlizuyN4PKYhZ0BMje6UsGAr5sh0pdWr1puazAGEKopFHSP3S8fx5EXt-pRnTD2hJzJgvG2BlTtrjIoKZxeR_i7h_Y73hKaOugcWNxiuRo1HWWy_Mra_4KXBij0rVrXaQpQlL1-gFcPFHWjSey3SI9rL4q4TvyUITYSSCOGe95zOj7FyNTBVa5tGrMG1D5AaauEtBABs7Rqd39PlSK3r1S-wU_HQg0jKjovpz6mGGlhrc9JKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری نیمار از وضعیتش:
دختر داشته باشی و وضعیت خونت دیکتاتوری نباشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100123" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100122">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/767e8b3586.mp4?token=Jp5W-F2QLXSDmeGvv6WAQAgLLInMmXpQ2J0FoVcfCCo0_9DzyZwWLY5K6tXAjPrJsdsN60Dv4WDYdsozv_g7U6X3QfCfNYGI_n4-GWqnqpXn-Wbhpc-kO-YM4oExeoyb0diUMpxzZdYqRqFz7QENmmMkTPbEwNoSwnPj9J4TXczYO39-SWF7otFKostv55ncg4Yc_Ho5B0f6vRTPQaejHFMR6nj0S856fq4lcj_FsmkakxLXi57YG1Q6z8qbEABTVJOBzNfAyTTUIrPyzXqogDAx4_F6syBVMoKHF6-qe-JC_dPR9jSg01oDWI1TfZUkSrPB33umV6iJvVPTbSjzv7hSfq3Y1MV-KnhB8QFBkSvHRV2EXZWEO_lvQKKGdZpx7ExY07JvLGfWdOpUOr7vU1etGYXE4r-M1miEU6SzDVOx0_XMIfi_tSZxXdhOonX4nilFbiKtPFKNtOAPABYtgx76w5jWr0ftldr7C9ftTdlFpYGl9vRBEDaQ0tYRqGs3ZEwaVLNU6IwA7hvkhp89ROvh5m3D47Os3_33ZAt8N6Cc_vQCwhQI1jlRwSCBTEmdQUu3WY0q0K5V3YyZ3eWDuN4FsvHutoP8Ki2Du7KWyZ5OPJEVSljQuPcW-tMbyuBPfZvt_-c_clpCyJLKc4YoF662s2QRo52rJ3ZQbk602u8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/767e8b3586.mp4?token=Jp5W-F2QLXSDmeGvv6WAQAgLLInMmXpQ2J0FoVcfCCo0_9DzyZwWLY5K6tXAjPrJsdsN60Dv4WDYdsozv_g7U6X3QfCfNYGI_n4-GWqnqpXn-Wbhpc-kO-YM4oExeoyb0diUMpxzZdYqRqFz7QENmmMkTPbEwNoSwnPj9J4TXczYO39-SWF7otFKostv55ncg4Yc_Ho5B0f6vRTPQaejHFMR6nj0S856fq4lcj_FsmkakxLXi57YG1Q6z8qbEABTVJOBzNfAyTTUIrPyzXqogDAx4_F6syBVMoKHF6-qe-JC_dPR9jSg01oDWI1TfZUkSrPB33umV6iJvVPTbSjzv7hSfq3Y1MV-KnhB8QFBkSvHRV2EXZWEO_lvQKKGdZpx7ExY07JvLGfWdOpUOr7vU1etGYXE4r-M1miEU6SzDVOx0_XMIfi_tSZxXdhOonX4nilFbiKtPFKNtOAPABYtgx76w5jWr0ftldr7C9ftTdlFpYGl9vRBEDaQ0tYRqGs3ZEwaVLNU6IwA7hvkhp89ROvh5m3D47Os3_33ZAt8N6Cc_vQCwhQI1jlRwSCBTEmdQUu3WY0q0K5V3YyZ3eWDuN4FsvHutoP8Ki2Du7KWyZ5OPJEVSljQuPcW-tMbyuBPfZvt_-c_clpCyJLKc4YoF662s2QRo52rJ3ZQbk602u8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
نجات دروازه فوق‌العاده اوپامکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100122" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100121">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فرانسه پر اشتباهه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100121" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100120">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اسپانیا داشت دومیووووو میزد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100120" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100119">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">واااااااای</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100119" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100118">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فرانسه نزدیککککک بود بزنهههه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100118" target="_blank">📅 23:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100117">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100117" target="_blank">📅 23:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100116">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
چون پاش نشکست و فلج نشد و هنوز زندست پس خطا نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100116" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100115">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سالیبا مصدوم شد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100115" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100114">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27954ba1f7.mp4?token=FuvW3559lh3fuGol8Ipz2Hu6E67frEwaKNDk2STCdCWaOdIHLi876s5kbGfcUnVQkf5kIZvbn1zYXj5WRQz3Trf5bf-RCX7pdQe3GeS9zD7CDHPB58IRGLuOmiBYQ3FEsEe2zD_EDDvEHJSBJo9gllOtr_gGzgpOW_EODexOKih5RdhRxIdeG3cSKh6QLueSz7S2pe96IW8OKPDErcQzMzxJYMyfUZLkFxi0DiXqXdmljnib5p_4Q_PmmV6zsTVZ-zDkfrllFI-qnWnHJu6INFCWDYmwkTc0FkY7PatDWZ-waWN3JPATrc3R8IKDeDC383SyP-2PlLGTerkg5qZMv7wsX5xhuv9HL-83LyOO9ZFacqjN4yvnKAgov-PANhgSGOORTAv6C8If-KIam5iBi8GWeFKqQDUbSMCe1NnypRQ97avcxFtzZn2mOCHB_VxlFBXDrjO2II8AxWorAMRGE5AIZ1kQkgzGKejHZkBdO5-NMQRI-6SLjVXGXutvux4dNLe92Sxvra_LYecbIURgFDy_E6ZeJe1To4-gFLeSHvLjrhsiQ8AUMK74eoZWRFyTliILVO4Utt7lCZjtQLwqDknoBJAP9LSYQUvZalYgrsEATRnUtymLYujnnpRelykCpghZpEGNcGF8iEcfFPS-II0gHfL5d8eBbKiXBN8ffS8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27954ba1f7.mp4?token=FuvW3559lh3fuGol8Ipz2Hu6E67frEwaKNDk2STCdCWaOdIHLi876s5kbGfcUnVQkf5kIZvbn1zYXj5WRQz3Trf5bf-RCX7pdQe3GeS9zD7CDHPB58IRGLuOmiBYQ3FEsEe2zD_EDDvEHJSBJo9gllOtr_gGzgpOW_EODexOKih5RdhRxIdeG3cSKh6QLueSz7S2pe96IW8OKPDErcQzMzxJYMyfUZLkFxi0DiXqXdmljnib5p_4Q_PmmV6zsTVZ-zDkfrllFI-qnWnHJu6INFCWDYmwkTc0FkY7PatDWZ-waWN3JPATrc3R8IKDeDC383SyP-2PlLGTerkg5qZMv7wsX5xhuv9HL-83LyOO9ZFacqjN4yvnKAgov-PANhgSGOORTAv6C8If-KIam5iBi8GWeFKqQDUbSMCe1NnypRQ97avcxFtzZn2mOCHB_VxlFBXDrjO2II8AxWorAMRGE5AIZ1kQkgzGKejHZkBdO5-NMQRI-6SLjVXGXutvux4dNLe92Sxvra_LYecbIURgFDy_E6ZeJe1To4-gFLeSHvLjrhsiQ8AUMK74eoZWRFyTliILVO4Utt7lCZjtQLwqDknoBJAP9LSYQUvZalYgrsEATRnUtymLYujnnpRelykCpghZpEGNcGF8iEcfFPS-II0gHfL5d8eBbKiXBN8ffS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به فرانسه اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100114" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100113">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگلگلگلگللگگللللللللللللل</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/100113" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/100112" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100111">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اسپانییییییا اولیییییییی</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/100111" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گللللللللللللللللل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100110" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100109">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خدایا این دیگه گل بشه خدااااا</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100109" target="_blank">📅 22:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100108">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اویارزابال پشت توپ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100108" target="_blank">📅 22:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100107">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پنالتییییییی اسپانیا</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100107" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100106">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH157ActwLAIF1yjwTTLi1FIJXwXwvvMA_OsMY3i0h-iuKSr8L6QVlY5piP3sd6Q4M8-MvJFa6ebY1LXq5_PbPfmTyisAnR8uoaJXZyS_LLrnv7T0HW_slO0Nqv-byt8sxb2QyE7nidmCMRrCvP24kWDuI1bQUohqGQkC7__j3J8TjN141uVxGEF5_ZkMJL3guMfKGxxCj8ECAjn6PLJXlRR6MV0_mgyIoK9VLiS05QFAM_ea0gpKEpTOqaVT8E0Snvcvd9SkSw3B7Jjr3dPWUy2fqzXa1c0_cDpLZ7l2Zkf0btOXy9ZvniWsdJJ43UBXL5bd5z7s7ZTWzJZEPQBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی کارت زرد هم به اولیسه نداد !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100106" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqypxXFiTGMTHn7QHSK8spy_SAlkAL6xO1grhT1QQftBEVCeIie2HTUP7wy0WonGQr6ZrTD5t93x2IrDSF7P_w8ZnRKysKkQfpx6rZVsv5zrP624hpeqjazpiuZC1bBk5oVUfwtirk3zDGkXLxB8d66NixS_GyqOslH9vf6ne78dH8A3puB-erO1RmEPFJlF0qha9WpQIrXoZxh6H-c7UC3snZ0LqCGfrPitaDb51JnqrIZ5F8spLa-R8f1n387QXPd5uvne6JsPHPADfIk5HuHtqLb2rSPChGUKNMfeDp44Uxomj1OXqsZ7fltyko6ehd3q90M2DNgAF8rqAzXFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی کارت زرد هم به اولیسه نداد !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100105" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
لحظاتی پیش صدای چند انفجار در اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/100104" target="_blank">📅 22:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خطای خوش جا اسپانیااا ربیوت هم زرد گرفت</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/100103" target="_blank">📅 22:40 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
