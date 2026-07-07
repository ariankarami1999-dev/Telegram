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
<img src="https://cdn4.telesco.pe/file/jv5RsXZJTwr-9OF_Sc2Swus_8lRIF-IoUdzF4bGTNCYz-u_wHC_F9u8OL5bjhwOiTWCRvGfgm-B7S-nmT1BbdFXuCfBnOg6zKwTE3zfGr3lAiEPIPl71TrPf7crJNoMozh01qUdA3kmu1fB-rkHaT9BUfwnDPgDyan6u5MOnMP7rogXpChHq9A90XohYWbkZOnAeqD_5Q20Yxxe0Rd0ubBz4_K8JVAO4U0frii41EKUmZ6COrUc8Vlckn7WVgeQEWrldttbjQBXQfjJL_XKL7VktX5wXjlUMpjFNRNzRkXyHLE2hgfxINVYQ7ntvmJoZ1eQEMu3kVvlrxwsE_OVK6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 421K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0HBGEcACQuiC9-bTIJ2Szb-RxNwGwWgntOSLXlz4Hdvl8WPFZHcuAqo8RJ3pbOMrc3hNKSB6NuCQ-IfiObFXovKFB_xHkRQXFBxv3KDsPdnfvF6xwVqZJb71UKK1hRPFCOfslukfSW3ZEVCqe4mlyDz1EIJ3W-p6jNC3L6Nhp-nBA7agSWsm6-4f3P8hzy4cV0BmWwNwNYGVUnJEJHnAZYgwO2o4_lQ1khH5tC7_ldcDVls8FMoY06kWCa_clbcYO8Eng4YlabdQvvh7NwPvxVjLzCCLZH1K1CYtFrihRl-djyvsFMZ16ELH-BMG51uTKYjlxq3kg1v_jTJlA3IXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyjREq9_vZGuzrgOub3fBYBdCkZnvucFjp1gBKFY54Pvbk_VHhkpXno11WxVg99Ru85cudysIgFjy5hfBScwsijMbYBe7myzsAdVmmOBxNsoIjBx2z-WbB2ZVt7LH6M1U8IYOFAUap9Dh97uh8DB2S-s9ppt30sb2d1j86Z2EZAei6PQaqHqR_-CtyKkZ7n2j7yrl51m1VBH60_eVpst0Wn69HyX7v1BOIjc3ozxbXSJHt0qxoXEWLrp4s4chPXFKg3_sjF5Fi6gEn_TXVzxXPUDWq7jG-e6y6gbP76cMrMwKUpn670zUUrqJjuBBaWI2ewW5djw6u4L1Qn3LVlqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=U4i5fzuscC7RGbF-gulCFIH_6MWq5535gPqTuvkLmfPnehclinID1G5azhwcvtEfVqw4JX76S-VA73UVT5VXT9C8DnhOh9TdGgPOC-N5M2QU25fxJnpeZob_PkCVzRAyO8fsrgiTszzei-n6Jk7re8rwNfbAwRcIXk24yUDO-S7VsA-E_DSYlQ35N4pKs93PH_mkPeoW98_77hPaeqd7N78rl-hKlO4AIfvtSnsfLiTZ2FKRtRQylqmISbuojicRFmRqUypmoHP5vGcnda6lXFQZPb3eHVezsGmp-62S8wKZip3Lg46fhDfKMAZzHMZRoiU_qlEkxgdRzjNnWF06sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=U4i5fzuscC7RGbF-gulCFIH_6MWq5535gPqTuvkLmfPnehclinID1G5azhwcvtEfVqw4JX76S-VA73UVT5VXT9C8DnhOh9TdGgPOC-N5M2QU25fxJnpeZob_PkCVzRAyO8fsrgiTszzei-n6Jk7re8rwNfbAwRcIXk24yUDO-S7VsA-E_DSYlQ35N4pKs93PH_mkPeoW98_77hPaeqd7N78rl-hKlO4AIfvtSnsfLiTZ2FKRtRQylqmISbuojicRFmRqUypmoHP5vGcnda6lXFQZPb3eHVezsGmp-62S8wKZip3Lg46fhDfKMAZzHMZRoiU_qlEkxgdRzjNnWF06sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJAier7rFTKYau9JudxUzxAjcdK7LLtwO0a5xgKyW5FDFeP7cq51OfFjkwjmSO9e-INssaX7A86ulV88VDQlq284hcaahlRPw7bW6ftVFbXcF7OJNOLjOg_gKFM_UlOFUJejnauRj1kkfDbWDWbx9spC0j4ZCKBR3PclHcrLgVDPJAHz_BKuZxJMOIDCC1qrcJ9fbh_4BvZXy9k2tZkHOK95dwhSAs9G0XO5d7E6JmdHhJqj4yN-7pJdXU0g1ozFZRGxvSbz8L3k1S98ZvMgfZs6Bn0ZREKWpKwsWhve3gNsFqk7zDYcsVAb5L_Dh_xwkqkse6v-IpHVIefIzjZbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1vfVuot-pDgXJMn0zRDwY3h86idcyIi010lofuKJVV0wmU4VB9RwXLq9QN3lg_Q2vfzx4foAlTz66wx71EUA-9qdLvxaXqZpkM8deISatzNs7r3uU8xSf2M8e_K7Wj8B-sl1d16PPEKN6SPOD6cxRi34blNqrkse7vZRxlFswshOYZxjIEmFHWFHrszpaXFhujpFCtJSNNLr9OogO1w7s7UUx62qd7QarWiq6MjhJs87mdlWauRpyl5TSbpRm6gebgchDjoi__t2YBPT1JBTp-P_DIVuikykPD6ckhtOsPh49gKL6TVhF1e83TXRdfMP9VaoWrG0gL7fi-SVgjuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSbOCbkmUGnzAphfveRxrTFWaBpd4NvE6qc5rs1luOlxYmM7JL9ifzM6sC2Ea_AeKILLwTTNbWJKtf7ECTU1N3TgpwFL0pZUcIDuV2Onj3rN7OP3bs3mqtoFELxYp63pXlSWlARp53UKUu5duo8ZhBMcsLNg-lPfqIzYoQCobh6htc3MKDJ1_puqTPAwFrFAjc-aw9UQrAx8McYdAzdMpvdpMn5bsSbdbXxD1ySnP5P_wJaGnaQUZq8JswGYGAY0gNI2Zqizvg4EyLdggX86UIIq9ADHZxXpmISRxwAUGYvLasssJ1Z0AFYwGyeA7GKzSi4YwoFCjOuaghKoDb2JKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXqS6afEqCrvyi9JahzTaPZxkEmZsxvO3USggD6RSfFnmK71eztRaRxj7XOYJmAH8czMYT2Ny53X0Db6gzKAq-7EidOjwwlFFshQJVOU7SXFBNv_jT-9XzGGQJAIUhwFDSDt3F60pFRo1T6pSHgMiveM41wflCNb-IyKzli8fyE4_nhuMQtDdVjYaeCxvQ1tZ9z52sFn-0oKXgCy2xmubazSfPV5A5UndHnYYZQL8gRhLgI6ZCG0KTRVWVMEAKqWIZ2yUJv_zIAIdYYogInkMbHzx4xS_5ScJxlhXsihDpxs0gf5iScUB82OE_DpeO9gv9MjWQykRDFvnmtC12AjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DShEbdHrVACn8UrnUa0e7uMkXhLRzRp9ko2FZN3kN4RIOKPkrdANbGqTKCljjjSol0qniL4Pwu0YFxCuPv50mXWon5KH5hOlEheclnSbT5FqiJ_At-pw9udTckNG1YGaSSMqXkPvaBduvf_49x24vhYxa0SuX9ZzVCSDYZNw-g4a_UvVxb3HrM6YWjiHCQcGOcA5pvs1uT3DTx0rxK74dTx6idOWEPdeUwgh2NhdswssC8wTpVQc_UnT6C6WZI3wkLXu9wlcXeUouwM_ZXEDnuIRO3KcwUuQ6_0f849sJxCEy3GiVia19Y917oBAnk5KMO_sXXLlp14KoFnhFuEv9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ow8cpFdYQUAy3A8dd85qsyCNYilnQhmQjoWvDwYWlcujnoZh0CJvqXUUpQNarjuGCbAgAifS5lVs7jwNBWoaoRL2Z7gmM42W6b7W2LKyLtSGQTbnTFEvNq6Z-POyOYu-ku4LuyCNSGbcufeWnNUlaWJnnfDquCkAJHpi8HohU0h7XwDGl3TWsoZlJqaqRMBvf2p9Mu4mBwv9JUzLPLiJ8XvgSJIJBbEx0MSRqXwUnu5PNaF-1jmshiquu0Xh6-6C_HiAZBMYVlhFf4_8Wv4KM9S7hiyzD3Rq9XuylT7BT5sHc5myt8P6dx2rdLGqJd9L0HjYaeLp67DkRA-piTi7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7lcxfPIzx3P69kKSXxUTg0Yvz9zfy1Jj5CdFuEWOzlr0xHD1GrekzQKl4K0R-6tR-n0uMut7v0N59pSEsF5FOAWkmHvBn-UrVgbkTw4KOOYtTUQ8xP3vrxnN73bkoDH2-1dcWYg4kH0Vc2LwHPdA6i5sCU_ZkOrM5NcWCEcIhO4SNR78u3ygQQXf_kr57UcLc9Ho7ANhADVBECNXuvguvf7V_C4swrTw1XjGdwoMfmezLTPF0JDkG5-ThpPBu3ZNsXTQYvUERpGJ1BTYNiT47QT8-jSG_BUkqmmNgt-LmU3yZ6ewxLIXCjPWTzjGWNfmO83GHEa_aBRM7R2J_4EyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoVMA5nPhCW1zUADkgxravRwOPJdRBp4KIe-2kOJj6U_r7gqeSf_SX1q5dmm2uop3Ng40iLl6ZhPNvL-co_gQPUDQooA5oAUfNcJHAROXF_BaFX-7IDjAUj-wfzWUIBvQDwQW7di__fSjcCI43PP_6a9UH4a5KvoGcd5tkREbesxYL7p19aHmK7wV4Cjhk98e1zruNzjfJLxS8VRZ2faf8t6JTg6ow05TAexxnrjPSUIpkeStCOafwSguYsxaQS56tmX6xHOc_Lh6FmTDecuPjG3PCzhxGXnMeSAI7DKBS2l-RQH89OO40lRpn75ki0o_K4398oC4Rn6-o27X87QqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=KiEZYTkd1sZH7VvNEhcdW1MseP0LQwk5a5d8JS3pN5T-JlD8XyikFV7vEOFjxWv0td6TR6I1PVN71C6b7b0Yggn5GVGXhK5H8-GLCHNp_bneJoi9A2u8Zd84lHJFEm9lgpxwOkvAGFXD9LLMQ4HSaH-zu1DCwfcRnHsUxhNYMGqzsiaFNKLR9dx75-qgfyl2k-zF4eOuC8v24V3wthTgUfLa2MtnJTRTU2IDCwfSSh8XdpR_0mxYdD2SiGi8A9YtlTebtcqSf6OPR7HtyW-jDOpMygZQ7ctgTyI1-PN0-dagPwPtJl2GLzc8b-9SQUT7oZGIvJ4gCfhB5KnFTi2jWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=KiEZYTkd1sZH7VvNEhcdW1MseP0LQwk5a5d8JS3pN5T-JlD8XyikFV7vEOFjxWv0td6TR6I1PVN71C6b7b0Yggn5GVGXhK5H8-GLCHNp_bneJoi9A2u8Zd84lHJFEm9lgpxwOkvAGFXD9LLMQ4HSaH-zu1DCwfcRnHsUxhNYMGqzsiaFNKLR9dx75-qgfyl2k-zF4eOuC8v24V3wthTgUfLa2MtnJTRTU2IDCwfSSh8XdpR_0mxYdD2SiGi8A9YtlTebtcqSf6OPR7HtyW-jDOpMygZQ7ctgTyI1-PN0-dagPwPtJl2GLzc8b-9SQUT7oZGIvJ4gCfhB5KnFTi2jWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIrJRu57y_sJeGEAysxom0UKVDo37LQjQnpYBjwwhLb0iUQd_JPMlRVv_hF6C88Z4I9eZxtt2_pKYvzu72TqgOtpxpJWUFUa9Xgg7ikTI_mG133Fzg_F6KL5t9HGBW5PFdizzhbPkuzGqU38anGVC-8WSTyTJAUnHyE32KNiS3DGKs4-8CA8NhTkrJ7jHhU0wEtD_PtlXPfgmYaSA_kOsIoWe419k5ncMEt-XJUjkbCYOtCGu9fV6mHpjCaO8Ki99kURLnYpy0EjA2GAeLFliUr9Bs0jMOihoUAoDGE_Q45S2SOjXrsjRslcx_mGdPKvXDVrpnvZwfJW8-aRXyO0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=C_ZIMSt3ml2xDlGeudfCHft1yHYeqgnEhJ2tOOr6H1DXOvXqoayKWFfMHrR72AXPxj8efbwNd-KNlNR_useLmE7Nk9ebLGWXSOGRefL_XhxXUuj3z43IxJ5miX3QxKD7FluLC4JfN9aKC2ZZdhGY16cqQKf3__A44DKWZWjlGw4nHRdL1YnjYQBqbY7QzW2dQfqMSqFk3EOD82fan1aGsF1QvWPZJpfUPMy84NCghFcCRKtx6mC60OkW3x6L0V1yWQIlNWaBsSDEhe5P1aexRddUAP5Wsi94xtLtnThnz7_UkD7UuxvEC7QK9JLnXIebhb_dcs2h3HbwiTCX7p0YEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=C_ZIMSt3ml2xDlGeudfCHft1yHYeqgnEhJ2tOOr6H1DXOvXqoayKWFfMHrR72AXPxj8efbwNd-KNlNR_useLmE7Nk9ebLGWXSOGRefL_XhxXUuj3z43IxJ5miX3QxKD7FluLC4JfN9aKC2ZZdhGY16cqQKf3__A44DKWZWjlGw4nHRdL1YnjYQBqbY7QzW2dQfqMSqFk3EOD82fan1aGsF1QvWPZJpfUPMy84NCghFcCRKtx6mC60OkW3x6L0V1yWQIlNWaBsSDEhe5P1aexRddUAP5Wsi94xtLtnThnz7_UkD7UuxvEC7QK9JLnXIebhb_dcs2h3HbwiTCX7p0YEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=AVBN8OWZuNhAH-JsFtmK2TlJSl-0PPa880-NVAid0HsgQpxb0s5tKe_rpDwRkOT32xMxwvgRG8Ukzrb-zBV5HvZJCZCeZ3HHqYex6cKVkY1LwYGK8_NamiVAcfTAQ-KhJpTGIxKBlBgk2UyJUgcIDd2LM9EjClB8gkObF0DwiplOK4FuCm-JFkyzOQ99fxmOXTUKM2tWn54pxzV_71WBiM4snzBjcxQ4ZQooCW6D0lCbPUCzs9Tnw0yqYsWnu20wB8QGpyZtrB11bhyGKO0yKDoGZB0hSQMZm2zEgYOJIV-1Fi5ekMOAkhiDfxmOb6tmIFzWWNJtDMF9l9nlcQX06Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=AVBN8OWZuNhAH-JsFtmK2TlJSl-0PPa880-NVAid0HsgQpxb0s5tKe_rpDwRkOT32xMxwvgRG8Ukzrb-zBV5HvZJCZCeZ3HHqYex6cKVkY1LwYGK8_NamiVAcfTAQ-KhJpTGIxKBlBgk2UyJUgcIDd2LM9EjClB8gkObF0DwiplOK4FuCm-JFkyzOQ99fxmOXTUKM2tWn54pxzV_71WBiM4snzBjcxQ4ZQooCW6D0lCbPUCzs9Tnw0yqYsWnu20wB8QGpyZtrB11bhyGKO0yKDoGZB0hSQMZm2zEgYOJIV-1Fi5ekMOAkhiDfxmOb6tmIFzWWNJtDMF9l9nlcQX06Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=PGrmGWOF1kydO0Cexvbu5BmvNrY_S51qzDVdEks__7P8B6khdISfn7Tv6Y1325ocTk2ajqnSvVyEaczlPz97i1_eUAfwR2KhlI3-YUyNXrv9rawbrWhEJfvSnhBKRNNA0CvODFrRetufS03ut9dc9b73-VwtaOem88W4U0rMUnadWa0nePnAbdXyeko6UHDzGjl-ibXKRtH03bjia4tEOt_GizNuLXbudtG16fSxM3tWA1y2CrxG61MwU0SqIFF0_FnS9BgvHLWfvlFzZ4qFuwia7Kc4yRk-4JPJEDgxfwOeoEWxP5obf4YhzOhCSrdDuwAHpurCBDk1rbXANxijIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=PGrmGWOF1kydO0Cexvbu5BmvNrY_S51qzDVdEks__7P8B6khdISfn7Tv6Y1325ocTk2ajqnSvVyEaczlPz97i1_eUAfwR2KhlI3-YUyNXrv9rawbrWhEJfvSnhBKRNNA0CvODFrRetufS03ut9dc9b73-VwtaOem88W4U0rMUnadWa0nePnAbdXyeko6UHDzGjl-ibXKRtH03bjia4tEOt_GizNuLXbudtG16fSxM3tWA1y2CrxG61MwU0SqIFF0_FnS9BgvHLWfvlFzZ4qFuwia7Kc4yRk-4JPJEDgxfwOeoEWxP5obf4YhzOhCSrdDuwAHpurCBDk1rbXANxijIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsF8wNcZPhZL2WiZFOSUBXkH_PyFuaVr8Aeu3mUPSaG59jgX8L2AQNarWoi34oDY_ggrVqzeVIwk0NuOF8oW_S-dH1jOs66vv0p0swv81dmiLS8sgeZWC2o9JEJpv-SwbVM6QKn4yggQUkPjVx3zoWcHG5D3qbckknWd6-E6fDnWbkOsfP2o2-fHG8n5OZK7otvwfH1kFiey9BZgOw8DUOkIkztV8oXslfHEkUqSNL5WtMkgaupIt6rmQHYST7VOOp0wauRXIAADATMXEnDtwssN3u3SU8T776kwVK5NbfbpnAqBiXN7MQ4YJZOOj0lupbw8roBy7N3ztHKYekceqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAXVs71CgHbeLkZEf6tPGtHd_6gg2wQ9yP_1GREkMj2EQ5m2nAMKlj-B5lGzCfnndkqBInFBll6EuV172dtGKqPj4ETzExbhXZb4GGIJ_SHdosEJtti8VdNhOKoZpg9MfV70wsXL4PTMtW-iRasfdbaCVOumoEgKSTVzYFqk128NQxlQuXnqJEfrRkb0ggGz3yoDIfyZT1oVpZtuv1FizbCisWSuYEWJe1jj-B8yRVGnvQAdDnTi7UbiM5LGA3i58DemRCnwp-WRe2rk7x96qvSCWdZQCi_OCBBTTVPTv82MLvdWaQ4lirM4DAAgDrsBRsSsYuHS78LXeqX_wfq9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psHrTiXJr1kvjGvEPpIR7jCPE8qjlaj1NaI_JHEVCg7fd-9D7TEBe2PZW8hZFAtrl4wKfS0_jB_6ytaVdfhZ0tnckkzlQ0Tr_fvJvTJeqpOnzZW_5wdoqcM5YJfAVh2qkfAX3eUqxUih4_Cs5gBKXhtxrP94iLZE_s1huqGjFJGti6TGfO9F2BdL-A22PD43KnZUhwL2tRs3KvUP70gQqXO5mN0XcpAERDyn-0tiBLjMuDW1TnGYeVDpZdTkPE6ZkVAXQadaVRMGMzafXPB2ZENSxyOFppw0vPK61dPal7JCS_ZQrw8QpcxLoKp2PNvg5-tyjVteXSRBFlPRmSyuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyNbj_Br7AD55aQOXyVYG-UnrRA4eXscyupVA0B90XkqiK8ZQqhP6q8DjCj_rWe-q_-WKc4ZK-mkb28K_eJNH-l-vsWTKiPKwYx2rtOp6H6DqaqhKhSmXR-P_sx_l4HkA8TXseptNIkzLlyqnFTPB5NStmpj89FJzMxyYcpZyeAtl4SO3AnWJEVYZDXUnnwjfQeJKf7oevj2yAX-kzVXX0wV5RCptoYIIKkhhaQkLWUQSPEZEJhJUSjXrrfrAZG87qMtfFE-nn97TlRWVybT7bRKm3aqu7UlErMGu7YUZfKKQg6Q3T3Zvske-03IZr7Sp9VndBBjUOCiQozOYEyUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=fKHmTfIbgfBbaMjjH2dnkctf_Rz7Js-ZNKyWYx42VVYEUzK50hRj3E-TcLXBm_N72p9L-syirrKW6bOCwb3SP4dC2FwZ8-Gcs5GaVQ3yfbTnPVanICefmuuSuKxDG6-XBNYi-WTAPDNGxhFKsUiV9a1ATk0DD6m45jPrfR2VZG5xFq41uNEakQVMrJo73FJMyPxpM4wTqsHeQIjZkxW0mzz3XmedrriiQ_LhrkndxCs70Ok1QtA9ct1077R2X3HaWaPjA7UUEUGXG6dp-lgUB62QQPYU1hFkjPwNPIyhl3OgskgjBiENJUaYGnDE5ADKlKYJ5XZ3Hp8t0__ORfyGwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=fKHmTfIbgfBbaMjjH2dnkctf_Rz7Js-ZNKyWYx42VVYEUzK50hRj3E-TcLXBm_N72p9L-syirrKW6bOCwb3SP4dC2FwZ8-Gcs5GaVQ3yfbTnPVanICefmuuSuKxDG6-XBNYi-WTAPDNGxhFKsUiV9a1ATk0DD6m45jPrfR2VZG5xFq41uNEakQVMrJo73FJMyPxpM4wTqsHeQIjZkxW0mzz3XmedrriiQ_LhrkndxCs70Ok1QtA9ct1077R2X3HaWaPjA7UUEUGXG6dp-lgUB62QQPYU1hFkjPwNPIyhl3OgskgjBiENJUaYGnDE5ADKlKYJ5XZ3Hp8t0__ORfyGwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1vvXTy3ZEiMF0dK4aO18g_ZiUQytNQedP32iA9Rv0wH0CbLra8aA3n30I_SeMReMLT32KTEnxnw6SJPGeS7qzyy-sI8NojFss1_E8uBPDn28wgrfO-LVzoFdrG-_AOs26qjfMmKHMjr2a0ERXgmiH6EO0t3c6nwDWJVafvdToh6MgR8TQ26yZbt5aVl9405G8lk0M77yjr0yXGW4nxdb97VyNCPkyB7tCGIir6IvovvZUNdL5RfiU-IuuiwnQ4XEaDsR5th3B3or7atba79oCuSMbmG61prTAENhqneSKivpwAZWm9INGvELfeugYR5NLwOAoET0w0m0oNK4G2kjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYp5ukiHuQt69uWzlqF_q47fYpO4RMc_8hjzC50k5mp4aeGajbrtGVLXucOMlULguNFIrHBBxnMyw9lJJc6HehXbLjKZvOqS5yP_33S2UNAXfUEL8Xnrh0Hs997uB9sy8TLfmRZbgIkh3ISp96BXJ74xtFOe9cOszSh3kw8KimmlyjcimsJFXJuVVSfYUtYeThR7xpTL80E_n6Fdhf2bULr6dY2q51_o03Ba3VkYx4-eJ2BwTXRFTWe7dC6ZnDP3NbHekyzAXeEx3Qa8BAEFyGiCM-34TGTSERVol1OPwKaA2fAmNG9eHW8_Om4DRIB5b0jBELl_s1xb96vn46w6QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAXzwXqKu_5I3F5xUqnG-f_kMxL2wN-WHntkj83if2c3rEog1sU2gNabEjPx97Y9cSKcZTDSOBzpEw3gZLsnN5E9ImbS8JFf9X7ZR0LjG2BjyVWLAsVKrdbTvF5fx2xSvxEoZn9k_l6KxbWqfws453lk0QKywcsGz5a3duAwg6AqB_k9m4_ESZZdPxM3N_0u_loq90PAVimBKJSd_Q5n51KsfJ9FRawqrZ76h8wt66k8QBlVqiUC_e6-9q3B7JrO6ekQo-aMDk8TCqIvH_Mo1IFXJeXOl3mG0D9BHDCYZFtNJSgdg8QQ9R3eXAH6rO7S_eogiQ6WIrhnvpIq-sy9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5HADPGm_JwnhEHixfIHXq0bChgUv5xXhxhLmWdNOSKvaT92RCebkS1OSdllQG8YN08FzhArJGm8l4KJzPpmTlWp1NrbbyKZzvQoSAHm4KhHAD8tmPEUXpqZH-VSAp5-wv51i6ONvZhAUKw8Gd0UyshEZF8YgO6g7fYfm-YXb6i1NNF_7NddfdN5yA4DHU0qzxejJtEAABaiJNUA8P20H8cumPBezyFJJBx-kdddUhf4oCTV3ERdMeci0Lh5PdV9jn9f2CtejMWaUeoER9I6vDpnQdYSsJku3w9V9fa2Moo5WsibZNDT46fTUmJPIYDuNcHKBAzi3xWyphYMmygf1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sckECC_XRgd2qHgkO1zsPvrXyahJhPIZ5G9e2xD5iUuI9EGSqTbNip9NzTNzYTP9tdRiLCzRGq4h7wTrqjz8u46AkKyOOV3tNe0jsDd6TKMgBv1le_nmWBir95tYR2ATheu-sTaPo_Ems-jvdR1FxgpJpieSYMsbnWsOKV8Sbdt-XwrnJ0JPtyVNGKT2EtGkmBRvCZEAYMzp0Iqc4NGqLAoh-pu5pd8MdiunLUKhPubqgW5VooUDqAxxHCEnIHIwjK7rAinnIx9HH17E5fVwEf_RtSSEJ04wUXeYm0xO9XSxKrNA7R3w9lpcCSCWTlDqpndsJxwLs3v69Q0rW7zzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwjBNfbaj1gZGatc5n-q9ONRTOLwC0PQdyma4clKmxVTnlepk8RIm-orjYjyoRmL53PeNdz8_soodQkYmDvCtW0n60YskGi5xQqk2L4n3c-UC8sS1T3RizqmnqcPKYuBgzDFsBot-GyuEW-awxZZwHRDO0mZEI5-pjbPFXMiilrt588D6_f_8gs7xoA5scKG1f_GGGU_aNHrX8skCJScR1zNXMHsGt5ohkZKVsI9JByPuwRTPJgpKSc8RD8yEnerYsebb8Naq_rq2IgeJJL_XasxSIFnpvrNya2NUO6pDHwujkXIaS3_sht2NiCfB8JkiPDnpc2VdTn2GXUPCXrjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=hHDd7sjBmCly5hSD-6jB9u1b0BzIBBUhZmaFXet8yjAoTJ8--JvgFKqsZoBPC_8JuZmUacR7_idO9GATx1R22Vkz24UxDNCZ1DbjAerkhkv2AhX29AtohWsL8pzhVWSdy9zO1AQDxqA1_SQXijQx30bs_0rcXA9PGNVUTH_3DAYS9VkUzh5FdOlVlGy4zQ7Ub7DsJGa7Dc1qCg7yE7_OYE8YYmvL93zXKFefAPOqYVo43bP5pcaI-N8kM1vtfZbb93fAaXGL-9E0urb993sI7N3j0ao2o-JzROyPlMX0frAE5Zws9YU79mL2JT18sA3AWzFZwKps3s9AE88T_2H4LELRK3CDtdUcIZ8PYcinXZLNhnIto5D1Vfxe2hpibIxLCxiH9DtbEz-dZNCFl3Bu0Cth580axfiVLxWxrpQmdXYLEj9qKNVYvXeXeXfyxAgJYFgZexXWiookz8SKd396RdJJ7s7lyQEYxf4lP_ntaejAKA0Tcag_WI3s5xbTeL3BM1LGhdMCHxcdus9oMEiFJxbeMHTSEtfnG2VuIIJPXvwgWn1yDH_Ly3VV7YsYc5Ra-86ejJRhiHiy_0kEwo4mmXbZoV9Y8HmdZVWWApMJ-4FXa_EUKNOETsK1vCEz_McEZ8JR3PGUxibWJvMAooAJfnhyFGvZDcmUABM_rCHk4-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=hHDd7sjBmCly5hSD-6jB9u1b0BzIBBUhZmaFXet8yjAoTJ8--JvgFKqsZoBPC_8JuZmUacR7_idO9GATx1R22Vkz24UxDNCZ1DbjAerkhkv2AhX29AtohWsL8pzhVWSdy9zO1AQDxqA1_SQXijQx30bs_0rcXA9PGNVUTH_3DAYS9VkUzh5FdOlVlGy4zQ7Ub7DsJGa7Dc1qCg7yE7_OYE8YYmvL93zXKFefAPOqYVo43bP5pcaI-N8kM1vtfZbb93fAaXGL-9E0urb993sI7N3j0ao2o-JzROyPlMX0frAE5Zws9YU79mL2JT18sA3AWzFZwKps3s9AE88T_2H4LELRK3CDtdUcIZ8PYcinXZLNhnIto5D1Vfxe2hpibIxLCxiH9DtbEz-dZNCFl3Bu0Cth580axfiVLxWxrpQmdXYLEj9qKNVYvXeXeXfyxAgJYFgZexXWiookz8SKd396RdJJ7s7lyQEYxf4lP_ntaejAKA0Tcag_WI3s5xbTeL3BM1LGhdMCHxcdus9oMEiFJxbeMHTSEtfnG2VuIIJPXvwgWn1yDH_Ly3VV7YsYc5Ra-86ejJRhiHiy_0kEwo4mmXbZoV9Y8HmdZVWWApMJ-4FXa_EUKNOETsK1vCEz_McEZ8JR3PGUxibWJvMAooAJfnhyFGvZDcmUABM_rCHk4-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=UejOAfevinXexSda7D-CDKy6U4h6yqLYbCdimGFrElkpjdVKMuRxiMiJ-PG8sojvvSsc7B1J1ygrXmCsGstN4E4aK2URsA6mWPYC1huVsTmhLGyHkMj9J0ppK2ZqfV0L6FGy3P26WcN4wmbzhqRYd5T5C24rQmxoCHhh6lbHxpwJjiGfZfJMFdju5IWwILiPoUw0_261NV9UeqcdK_K9FF2u5pgoMAYhJvdo-OVyRZzSgYCLbuJfFuf1LxbYVf6iESiSiDigvht770jUM7iNI_D8bUkUNufKkQdR2ub95m4RLWlMdk2Ts2QufiOiaRU_AWnDI5M-hZVprx57ZI9s8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=UejOAfevinXexSda7D-CDKy6U4h6yqLYbCdimGFrElkpjdVKMuRxiMiJ-PG8sojvvSsc7B1J1ygrXmCsGstN4E4aK2URsA6mWPYC1huVsTmhLGyHkMj9J0ppK2ZqfV0L6FGy3P26WcN4wmbzhqRYd5T5C24rQmxoCHhh6lbHxpwJjiGfZfJMFdju5IWwILiPoUw0_261NV9UeqcdK_K9FF2u5pgoMAYhJvdo-OVyRZzSgYCLbuJfFuf1LxbYVf6iESiSiDigvht770jUM7iNI_D8bUkUNufKkQdR2ub95m4RLWlMdk2Ts2QufiOiaRU_AWnDI5M-hZVprx57ZI9s8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU0Vp0hZ60PeTAcYMF-w3EHElaU_YRMFha62l6dZUYlGDkt2kEBKr-aqy1mbBjpio6plyyMT48zSmjaBdBsCiZ7GpkyqYW6w4I8jdj515Un7ou2ZuwLkG852DNC1EkSXQ76q434JW6uRSnNNWHiLCC8xnZ3Nv_x7sqvsXMRqBNm59z2W9re_2gUTFFIAfCsaxROpeHZVrA-YYVZniIiw-wMdu7cLJ81UFLoaH-50Arv2BvuxCndZEHdlM3ERG2ZHwtdBIwWJcfxpyE4XOtKoIurahQxjrrBUl3VVaMk7F3T6PB2E5qBg8seICe3x9706Hwr5gtFHFljnG_nIb_DUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSKZqFRdc0vOkkpHf4sbk-QzyNdgnz8bZxJoD3o-0GJckoeTgGr4okPHvpP38Y4VXXDkoJDnYvhgy__CxuExCVR6Jc6bfrZ9Q1x2kOCM4x0iz5zIvBc18k_Uyk_m_F27uE3pg8-cT_0aDui3a0PocNpCnwTacSy_GTKbM-uaZIb1vV3STLaHP2MPl54WeAEoNFbfjfGCcplSXdVHHCZQDy4yfkIPFytwj8NsryDFzADsHYdsZXz4rljFIt5408qzZe7BgqKghqWZo_8NThjqHP0Yy0pw430v9cZF-SF4eht4pIkaYtTBSeedZ3E9ykZi-sVjV9OA6-OlKSXsdruzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czpnxaa7y8FClOrW22EWNK5TOv-svOePKDYkKxZwMhJvJnMTAv5Gatu9uaU0zhQxoRhxai9YX_kwoiR8PZs0cwbRrEHpaUwnyO1EaA3S93ZjmrEkWFrUYzEFMsRCtXTzgCiC4unbaTvFvjZ40OrHwXzJdY04s35SozC3BJzo_NizQTYU_WEfffrbVurAPFy_aFRWsRCu4apgJIYOj47VUXG8vRHYOB57rPAtiva_ke5pcepY3HUs6hrAbyp8QoV1rpuxH80HhQd0huabqIpZA4Ij_Co4jclNxrggM0SpJ_GdhJqVxkIdB9Q_cM_qnju06vjSPV5UijfFy1ZU4CrWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biSSYDFQtasWSJ8zfeXCSHTLkcQyk272tEqyejzZUS3dOmVL6mWwj-RHD2utAhZwHucIr3N4CAGs9gxlclhbGROcfs486oypDKSU2uEUxPBbmcaqUBgHJ69bXV9Tl3DWoQW6xvtxFJHBy4csRvIqJTo3pjnALYBaHaxXFUXBaakPiwHB-xvWCvt86AHVzyBzoO_oYqF2dlTmXHhYOsKfwvvoFjb-4FXAHO-rUIghWKztVg56ALab34qW7radMxW5IdWfy-yHdjfyUla_ACx-Qi0R242h1rzTKJzE-W9mJ5x_V3PLTR_IQKydPRx1yfKeOXPpn0SxUs7CD196niprzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYTZgClDs9hCeysKSU1KYTJLz-lX4MzHlQu_R_rcTT46aU8RXvak5K0Aa5gnrddAek58eY55kNmP9poSOMGIw52WsGVYtIflMrtx36IFr6K76LgjZ9_TANyCeNC187UhZ-cG05xEYbHYuWxn2F6O1__lfHdtL2K0GXkA6QIjtixtXzworpbM1CstBl0s4KKt2zMKH97oi09s5brkQJ7r48GOO4gnkFBfMNY26EbuiRFIRUNOx0pJUS4MgSZp23xF6MoQxjiJebeNeQOLpY9dX1jbQ3CkoVQlY16sDRZnPACeMf9br9ewSDPAMuC6fksVA3TUxpgNWo8mwYgk1vE__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRNHNBDJHXJ807KXfKFGqbBXYVYG6mvrmpTWh7aHsh_n54aSDQ_KBHXu8f7sEFgTctPvLvxjcKQKY6Q7tVp5cDa9B7MU7s71dUAZlJT3YsjNMIwpkFt5_Zu_vnNb_Cc2KzLtkXei7IcoZU8qhCH0NwRbK-0alkGKWpjj20STMWyZ0pQcsYguah2YE7Jqpjp_D2rH8pSFMJrQZZ1TvRFsudTgb57yTHj5LvQIxVdmoSIGF2Wf8Uj_5JWg0JPtrU-vQKejbOC8FOa-izv08bDmbpFtXcgMdXUEpVF8aI0in6DTvCXvuatf4dhOqiHIr_oXkp1XkfrVBnUcJjUrlCVxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNY-eTwdc2OpiP1WQmhy9nepJ7sV1byyPn0TNTau-qp9jI40YY_zFWK69EG_R7r7jhNi-RL_lv17RD57217TLvPhDHdGcuamnlaj_rBFjfI2Q3t5S2LJmr2muh2IhjwnCSimXM8KJXE4zgaJ46xrKT4VuVPa8M-T_6lJU02jfyZl9YRmCUVlqS-AgdWFsuA5p8geY6TER6Jjb26_24lrPmW8aMl5gPWpNZPO_4wDr0dqmPp_Djyf5h7GExjOWl9_mP4COC7Pu0Y1xP-O6zvt2X1VOiwYjbZIB8rRjr_gQrKfiUUUmTteXK-FwksZBntHOpprdzsw4wEsUVDuhlSx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QArJqmXLfZGPvCN6aimpjmqP_nB9hPvo7zsWLt5U1QQ_QcK3bwvafoOchNEUZwS43snwb0bnqcpnWXU6qFfLSneXlF9k92siICoRnXSMrVV9hlV80qRN4KI4k4wBZs43m1c10UlxbFphROv1f0c2lYYCnj5po3Ux2mAmFHfDYozMSiac_LrRQp0PbNeZiGYJIIrjqSaKrzkibDY2DZjVidmvECkrqfWp9UX3gzL6bLFp8yUcT_lyAp5J3K_Rcp0JiVrbigXvzbvvx6JmNnS2vgheaubSYNLAVafDsXJKEk_53XMPPQuY8Y409OSgK5EdIWjD-iL08vbmLUDqxkmG0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2xhkyLZsFgXc2OqXkA7pbNORvoccLgn1WiFXAs-McGJGoiOAWS_be2u_lAYKukBkw2BsTIQZ2w1Tj0wsq8FqaPZxGxFe37J8774z6ADC6mr2tLFH6Ky2yYdJ_CVBH3W2FvgrpBEvAq3CFr1s3PjWs9RtGC9dhGFJAIPIcBBDw26I4XLCoXkI7oruwtIdWQA64lw9ar53RfZbxoLJ-Emf8nmCuMehr6G9soLFEmr7EW7y_hu6--5bpWibfyBFV64GKJBhFm1jv6uwRsfcOKPUDCuUWYP19KOcVmml1IZcxsJ-9saO62fTe4L8Kn2Xxz3X_I5bJZlV6p8P6oN7X-kTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCZY2bsbpCU9R_i453zsN3Y47WgDdTgNZXzh9AORpJ6IdSfl0KsqkCPkjGZU8ql3RjPNcc_W868XNMVzXV9IEPv-HVKbRVybCleXhigsXfsqgQHJW9jVdLfnI8a9I6qrBH_W7HIYCNG60D7oRAS0oYgjOxZ-_pTege_rlL472uc-ah65GUBwN3t68HaPcMebjoYbHtQWVj2XU7tIeA2vwYEKqEA0Rdc2F8XLWO_R-3a_eDCyuj2VnD8ThPxW0dSo0Ik6WKyezpFYM6KatBPESM0lpyVucvhojOIF5a5r9Ryze4bTEOcohPkZeMR3a3rkooxJqA7Qw7M4qmdnYQMQZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25096">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn6qza87HPB5fF5c81DWrOl0U1cxcorBBmf27XWAOxlR0OYaAy5zJG3lZcpQ6eM64wUZuE0VGeo7v8yGcJ_kJq2HG2fcGJQ_s2pAJnAyiOqU02lR5WVgGwu4yPupmGPUaBoIVZiO-YVge2xDG4niJaKorqwZdWKoAohZQ55iwfQnG_uRZAPztb5UmEldrKoPHtGlT99t5tvabtLJGxYWbgDtQA_fZFd3JEmC0IqAafnn6bF3YhR9uryYWfdJsyJQWnvW_tWY_xcqQvNMWy_S9ZzYygJjxd3NSpMk-zdttczCCwiz9yRavJ1uiVdkcxy_bdX_xBLQ0HKTuFR6ahzYsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت رو ثبت کن!
🇵🇹
پرتغال
🆚
🇪🇸
اسپانیا
🎁
جایزه ۱۰۰۰ دلاری بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه
👇
انتخاب شما کدام است؟
🇵🇹
پرتغال
یا
🇪🇸
اسپانیا؟
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.
https://t.me/betegram_bot?start=p2_r4EF37DCE</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/25096" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukzpgcPWCY2k-xthUQvu3H7u0P8RNTDYSLeRCJ8-lNQ46mSRTkjVCe7V_sIi16bqFakk_WjK1AH6e-y6IKrGWTu8-jv0nn5Bf3TbmsOAzsUWo5f0yfKCozw8CEIUZsE7p7KS0BTkRL5ET8TRfx41jBodmVdKKsmsZIAmI5Zkx8wqXEvBhpJa30GL-JcPpvW9IRWShdhFWMmSsgLsGaFEhl4fszOzd1mWxww0V5h2WRL5-jar2cjBTfVRCMwZyaJRhYclOer9WbYvBJR8yKE3xTAzQSEJv40WUV6t4_u3kJ_JJBRJsS7U0MvQLj_FRaLzWKnVmnOtW6qRWqX6ptFfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmC9EuY5VXJ4wqciaTE0FITh0hu2R9EZ-8eo-q7HjnRqHJpXEZERG984n9dLJ9A1liuteqk9ki-6GWzibVo47Ke8X2M0OaHAq-cr1QNJFeGmOkmc4gpLvwEvqB-GGrM-hB5XvU8x9L-IjTXcOmHxXMxb1jufbIhC32qwmWJyFfpUr5VhLbzFXZDxvoiMzXGNcZyrnQ6_pe2nDkVBpiwrb2Dc9FjXSoatDXP3bmrhKgFapmBU1480bOj9q2jhDciZZuwwFrWAumf2PojYvwQa0xsm3jbhwudgUxIL_IGm6mzMVqUIRo95XDy-Mc2gVMgqrwJZqP6euXOm-mkKWRdWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oalb1iMu5K_ItSuTcqecKu-vpfD6zxwnNfbjcLGpmOcfxRKyBZOdx7SHIqS62XEMru7evT52jYHCESA4MgsSNKJcxiQAYE5uz6lstTyCOhh3jvg_GLOvLK0OBDnJGrAE0aASVbcWuDdfUZiooN6Hfh4hQZ8hHEXIpnxc1mo11Pnq2bLPenwg0teKOkQjzkJoXCXiFMeCH0d9LL5ZcGdRlTRShSLbJXN9O4IsS14lacJlNZ3RHVoREUg3pelStGP7oMDvzbrHTMc7Vh8lNBYYsAcx3JxM_HnYfRrYpC1630JG0fZjsStFGHPjlLLjqzMwjsTVbH2yha7GGQ7rsaWdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3DhrI22E8TaYYGlp4TkB43wEudLmNLHldGVLlNERyme6eYkUNbPkUDCwhg56odDFzDkm7EzZNw782sQavVaVhhMsWKwyA5rU1vYd-1_NBapqVm_PM8SDrhIp9niin4Uphpq9CSeoZTfmQYBIAHfbLoSDs6H4UCpu7MGHHgD5N8xCxmNbmDF_8DDERtRq6SHYQMROKJEc8fn-oECkl6jy8YaCn_L1RDpygl1IDSZw2o8G2P5pGt74AMb-iUoTwFcMq_rnYIX8ZxZAPEpFqYnZtQKVvIs92mI3JY-2LGk49Co-5dit9Q8dkq6ZdB06OUM5LRYMwo0lc3wd6c3T_XHJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsQuUDjqQE5nStFGxm2Zd9FtJUFlMJRbHywkrYqE_UygDw4W_Fmieq-wIxhdzsmI91XM__U2jFMnpy3zWAPACwLYdktEchP62uLEs2Nw9LcNfJT4PiKUk0sxfYzDeawuEKD9rr7QRD4JRoaGtK1JPFqJNoJ-G0tXRtyzG1xE8ZHH14FxaoGrYz7pB6veoGBgO3O_b3DT6GmcGyUuv6dS52hGfQdaV-5VMuogZ5DOcjhbE8TeXfMz3GTkb185H5q_cArHu7DVE5-UJhxAWhXed3RyJacuCPOxy9CNX2-UC0_hqX7Z8Lc7FC_hHCU6rLsqCwNoR7suBxjrZBAEtGbjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3Y-qRBH-RHlm7XplobJ5nHVQ8Bi-fv0rOv-wage2K_R9fwPqTDGGKxVdTYeMEfiqrb62FfwnIAOvTRm53dhFq2wnMrI2h7etW--Xfd5fks1q6ChnKUADXAQKkS68fli1g97e8mt6ocaUGJ7AzMvCV7EnxKrVQ8MV_yvwq8Piy-c_WmfaTaLQgST8cAipwRL_XJYu-jkNylZIN1ukGjK9RIM6O46bEbXDXurglgaiDNCtspgxtVQn2k_iaITiIhI055CBsRc-DBZGeFIjPPOftorU0zoVY3291F21CF3Yd22PdvMK0y17s5Tcep2hWioyscj2n7WfH7VsYGyPIszNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GruUBfZPQi7Wu6coLKc9714CKmR1Fjwt_IhBE28YDOCHRviN4OSlleZnrk8UijOUAFlOLXV7QA3fGHSMeDORJbxQKlHVKBlSuRojWfG5ndAJPeGfCWFwjvlKA98BGr7dV0BnCTqxq3ZbH9ViJZy8NFDYf24tM8IhIZEV_5V3BRr0WwPiHoFAe_uDITOhkLUk6RWiRwGrLmHjCgKWqOCNHgFZZlXbPybI4YDfx4tt5zKofuBTp8a8dXZcld6GBuCR83QhAyc0y-Ap0dmq_bU-XhE7fGKYCcelY-3gFeZNmbI-7rJWK3WveQP3ThkW8_1DInVH0x5zGFlS79euyQ2czXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GruUBfZPQi7Wu6coLKc9714CKmR1Fjwt_IhBE28YDOCHRviN4OSlleZnrk8UijOUAFlOLXV7QA3fGHSMeDORJbxQKlHVKBlSuRojWfG5ndAJPeGfCWFwjvlKA98BGr7dV0BnCTqxq3ZbH9ViJZy8NFDYf24tM8IhIZEV_5V3BRr0WwPiHoFAe_uDITOhkLUk6RWiRwGrLmHjCgKWqOCNHgFZZlXbPybI4YDfx4tt5zKofuBTp8a8dXZcld6GBuCR83QhAyc0y-Ap0dmq_bU-XhE7fGKYCcelY-3gFeZNmbI-7rJWK3WveQP3ThkW8_1DInVH0x5zGFlS79euyQ2czXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد
ترامپ رئیس جمهور آمریکا:
نمیدونستم که‌ کارت قرمز گرفتن به چه معنایی هست، اما وقتی شنیدم که به‌این‌معنیه که شما نمیتونید در بازی بعدی بازی کنیدگفتم‌این بسیارناعادلانست. چطوربازیکن رو واسه بازی‌ای که هنوز برگزار نشده جریمه می‌کنید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTPgTy0IPSm1MkYsl9tzYfMDv1l1rn4JjrhYTCDUExxux25_kxVxT-eglp7cqVgzLJSgoBOnK8nYZ5rU-ye8UdnPmobcyd-HhaB0jq7OSpw1DFASni9MAe1llaJ5Ai4obdRCBnJCKCyccUOAN39ltW6y_DHBqiKsQqbtjg7m-irS2ssblRN15Nl20FZQw0UAUdE7car7Wi-vOJFrxsgYzi3dtE9gmD07Ii9P03vRL-1wJuFSzIheEfyNKuNFlSaMK4ncD7DEoM1r_27UJUcBfgRFnEchHADKAIIlbTcKbxIeAgGLQxhuoGLNaWH3oUIUqGfa5dIkhLAAavtI7fPA3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUozIrxUZAJmJgZioe-sg3ugOBRQG6cZwyO6g0FU__SUstIdCf8ywdlWvlZvw5Zdf29M8Zh-BzA4fd6e1IJ7AA0lfxT8DJR_Cq5at9tlZk6HxJgQ0cgRN4ButlBPJ1M4E8ZqFwoTxP8Yhd_lB_7POK3NgUj7YGOfXjVuvrxW6BHI7twUubZQM790tTAfDx1cf-C3MX71ftue32XZffkaP0tU_xdCsXK-T7c7XONmOeOH-ui63BfKwQs6knAH3rmI6YISgd5Br1ntsGHo8OxH6Ng0teSl7R9kX9CKluTDnuvXrMxHOgERoPRhO8hSZoRbR0FLfmjHXO2BFYye09MQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9U9M4EVhk-3Sd2ifl2V840vFdme2e_EZ7jT-bpCuKA_uHWawXucV8ceRVhyT5Z75OMTbVXOSWgExfiEos2jObBXF603nKDI0O-piTCvmlMECttcxzrRmLJBvhKqVoVjGMKUkC0m-2wXjH4kacdI-Wgya2ipOxtkxP1v8R_6sA0VvcQ2Yd9sfGDsCicRxlMCedg1DAyqjxw1_zO6yT_bsTUKKZF-UJ32K2oHF4IkQrqakXuyDTDmMPptxS4kxy1C5f43KyYM7-zMu7ruOiKsfY9Nia216C5ucuKgDiF4urqXWqW6-OSti9Aj4JFrjKfzHkKc9MBmivdCS5WTmIm0Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aooYBxHMNEDzg_hPtFRvSe7TKfOnWoyTK0h2ohUqkl4dglEY3DAfCm9KXtKBk41iwMYr96E0ICJ0yiVLRNlHUzZ1cv9ccesFL6x_tDkSXUe_u7hfOQle2ifuSco0GlNm_sn0c15MdPNK7IrKdUYFZtzyhLo6FLGhhiZmULhbJgDyo_D5okcF-7jmb6u6jnlc0UBLE2kt84kSF9el8dAyq4GikoifqhQf73mndn-LQ5--d9Ee7ov8tvXervsQB_zkXsSuN4ylrzpmaONuTR1SkRf7WUBRkRoMMkh9ck5JIiC_WTT3QRYIpXmLpDXEIkNWsrGhPOxh3i7MYdvNaMQcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/en5i6-kEjSEVGnl-_Ysf9dmh_LFXuuBXjYjxI0dUHEc9aVeeuww4Ph4YVDv5PjKq7109X_9f6k-J7OW88cfkXEmP0fN9ONefKyQrpwl3rOht-sHYpA1jPM0P6mVUFsArD1WUxC5JI39neXd4mv-iRV7Gb8fWLOdCxuS-z-mO69MQdNsathrAu5wvpcHsO7qYXSVhUEfJvmHbaD2qp-VvJxfHcRhqtO16YEyX6py8mcuOA20w13dELW7ByVFLHi2IlmqbJc5MbOOFLR0L-etLY-T3HbBL-KZ7zAvdz7QkUW3bPai2qJZ8E584DvVOqgSdCpAHUjExaHaB9xF62AyFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9frnTkel3nl-j3vdlBFrRXzwZR8r8tMVMyceg9KXrGSW0sxZRD1uNThh2Xrv1ehgUsSKaUbd7nGfL7lONuZp_8Su9PHO2-2IucZxhMvKaQma45Ru6wY2eqI1x0AdwZMLE9ydDgilaBopnThKhCX3JXCmdGdhhtOJ3f-oefnluTCycwjy7jH5dt57NbPL7d7XcTEfgvXb44Fo5YVO1hkNVMBcbu6_55HZdDlHZQtll8ayZelf-QrzfpnFngWQSudRgB8SzPa1-12MghSLSkPiaau6fDh4zaAAvnEpkrBiNHfI183PnCSGKLMMbVn-9qk4-vQOO_H7nzKLNmr3uhRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_O614ZOsVAsdYe1yz2APPL1oVkt84CZgzigJeSdoCNpa7Fp2IW0ZXQr_r7Y_S9AC_Qs_jHXiDZK2rQ6cdG9NNvUHNNVTtAG7z4GPOguCyUJ2YRXTVwLRc6y4C_7NoaFbHSkQHpPniwzHufEUksolwXCYF75jU0QlXAZYFnpbYQpl8vSxVSG87mWOOTQepYBdewg7izTse6iMvOGslNpmgTUUVks3ZxnjkUaM9BfK3wrr33fWsfFIx1EdNrYe3w-x1PGM5qJzS3V5DnXZ_V3k5iEWrO4ECYWeZX749k-AD4A_slX5rzHwzdNx9m5yBgjp5nwQhhJGiwVYqpsznop6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocFt6c-p3ymxdqocn7NtVSu-yno-fgU-vwhkZPYRp5UwGckDXG8Z0K62SxXM3GLMYxssFLueNWFn6PvEjmZTAICVks1pPUjp51V-lTusTLWZigHchw0yGQShDhxyOYrYqodp_nlWNuzC4AW6qINAnaRq-1cYvEwGoVsFXg4byqbloKah0Tuf3TbWtfg6KWa40jbOx3jurHViq-gf-oDzuUJA83pfi3L2JmHFaiEvD5vYdC2uQScjsEYGhF_2EffYK30ryTlWaCp1Y4mymG_cfxojk7rchwZCO340QYFcOa4W9fKkk9lkcOtEOv-tRH3UF8YW-GB2mU_XlM5qPwcSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1ODW-ucJCakSGRzhpMbhNnVCpGMo4wYdACevPBMb3BePIX7A1Cmc4Ymr1Xuk2GD6Y94BpwvDdsNi5A3f2i34otgICorpxxzolYof-b8cwQqc93HhsF2sNiRMZwUNktqMZNw3KS6MjYQyo6Q2gjh07LPkFQzh1uknCjgEPGxKqLndl7tLv7oWimQh4XtUVkoC_oDJ-J3aEhPHtiqTTCpGDwRvbeBTHSpmDe8ADxZ3Vv5QokjB83y1yAV9_i43vdMfkY4Pk6fD6HDlmLVEH43v7xQs8EuyXM099jbpdFSfE-jqcZlQXqMFN5fmR-FueAsCFUjryUe8i6iyglhB54MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR2Rk5GJkr5IdL7s6pMznuinEZsg_Ueb0K9-gHbfGtOXX02G1M_E4tfIyaRy2n6W5oQ7OUMFzkcI6uTFnrYv9YROCcqAeGCkvsdodMnfwftgFVVqBUsOPAhEu6arxXAxsrNPYso-l4RVPiAhc_wKRrC2EbudOQN2IZTA84ym5xR_6mqYZvoGLpryK6kvfdBrUsThlM61K4_i7Aa9IHNIsnE-nqj5StKRUd_qmSuJaA6-_48-yrLm8bAjUQ_DJufTn7hCxSF6GLf3tcwh6kEczw5nB3Xo6BA79BHQse29Gzp5XDEkA84BccIr42hhNbtpj6-5EyFuBelNY2wRv8Ttaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekn0a_HQ8_Jn6Oo6mHheOkj2md0NB-AwQX9vEn1NxLoJXtskBsb69bn06Qm_DFk89enEKzG9g0sLIKMRf6dv9poUJ8xRI8SuRyIzyXNpXKJYj9i_35mlMtVG7QM2NtH1ThLFl9xvsitHtlJLTx78lSRZGPFU9tV7IOkihvRz9s6hRU1xyAOjvcEHSeZEYufIs9FhuUrattQuduKbacVNgz6A4b7c218HnNBJ252S5EAkmiMS_rcBUVdJVCIZQ2yhKPx6tJVjvaq5rpvsaOVzVggDvty3g_8PCvGFipGjlw9daxwuNhpjLlHixo0h4l6MMPVdkw9rRahhyAFPm5AYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9C9E1pjmxJjMddaHVz_h7CSLCFNkAF14vsIaSf1l68LAitOGVPWDdls0d6tS6fT8-f5nWAdv-Y58qyD3JC7-dWh3j9QUORDiqE7UtkagnynyxvfrQqYFiK44b6KvY16ugP2e_FohdD-PGVBz4eOB2ucy-aD9pJoPNa1MIrqlQyioseOTfJRt8HqLUALXcmQbl7pDtG3DnOWQ74PSSC2BiIm5-4ieLcrVT_YX-8jKLGhsbCox-kr9SscVX3myCwV5KUNKvfGMVklo95YnDv7IyNuKBW0Y2FbZwr9k9foIJ09eeks1M4hEo55NPusgAehEPFzVVWJrDD1QHqS0QWK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25077" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LssXfNsoMrW_oacHQISjvff1z57A1G3hQcOGRRSNpjH9APtmpL2IcnBzpv9_WJvQLkYJ0LBzopdC9eDX_7tzYzwgXFie48Ml1HfyBWfzioAy6m0wFKjOd8zyIADPOYP2M2wi7wzCPOxA4AQY4mXM77dhU3RjPbnhrUW9SBTBuzBqUrofhahhd39sOKer17bSH20khAF4GXGGQQpH0yZHjzCe789kvs0gOChiWrLETgP0_0DPDYkLfIwraZT1DHWxi8k5Q-mFFn0gwozq8E86LtUmDJntdOgAgOBA6M_I-5BeEccrswtBAu98TRn80TmgRpfYHcFNQk2GUvOOheQ0qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=B0wybo9ukWsS4Vfm9FmAXeh3X1ATeQ_mK6lgcoK22DwoKPIsyOFMyP_Dp2Qz8p95umU1LpEK25uUbnXC5lV_9l-LMNX_e_v72x8fqS8gvLjv0lSM0Xu2At8EaLpoU3G16Ob0tfLKnO5TsetY2EH7lbYD0aBr37i1iCNN1bClim92rMwWAfxZn1aPKa3izVEQI9JGA_Kn2S9H9ZO9sXvj71JHBMO8KRjNDb4P2y7BuiqjEfaQN8ftT5eGovC_iqRpKnX9dQ5mmSV5FkzEcSSntIUQilpsYUT0BUhL6arV8SGRZTmBqj2J9L3rIXLEXovJ8oKQv3dAkkwPM03wNshfew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=B0wybo9ukWsS4Vfm9FmAXeh3X1ATeQ_mK6lgcoK22DwoKPIsyOFMyP_Dp2Qz8p95umU1LpEK25uUbnXC5lV_9l-LMNX_e_v72x8fqS8gvLjv0lSM0Xu2At8EaLpoU3G16Ob0tfLKnO5TsetY2EH7lbYD0aBr37i1iCNN1bClim92rMwWAfxZn1aPKa3izVEQI9JGA_Kn2S9H9ZO9sXvj71JHBMO8KRjNDb4P2y7BuiqjEfaQN8ftT5eGovC_iqRpKnX9dQ5mmSV5FkzEcSSntIUQilpsYUT0BUhL6arV8SGRZTmBqj2J9L3rIXLEXovJ8oKQv3dAkkwPM03wNshfew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uzhr3s8uTSiHRfh3lyCLw35gGSjphyacSn19y6JDr2wbmsDEIBNKkSUT09EH9IqTjW8i4z7--qeobdmZO5gmT0G8qFGvDL_-DLiyAgZ8LotP_30FSruSl0smdUkHrxGNLngxOC86RAnOGx_1ta0_uJRzU5FhBLE7aeZLPcK0p8vEjAtPNKFr01g6KdgFf8IdtJLDJPbXT3mHVmG241sq7vbG4JbN24sA0hlE7jRkWigwxGIthy6j6sLRiLFx4kMF4Abk7NIBxgVdCdLRhA4PzOwYJey_aIcQlTS_vmQpMLhvmV47PLx68o3iKLAWJlQnAHrGhj1Hm8GDaLVg94vO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3w3ym2jBIMAYOZ6hbgMDf2jz4x_3Rmv3Vtnvt2EmGjRsW_ygizkVJI-0xP3qBumgjAtPmxXjQxh6NL1Lhz7stnntciRyW7n_DMg3_inPa0ANoZqSV-cyIfOGoBEjRU6UWHxY6znMkR9LcsuCdSDC4YFKn8TXzLlPCdNoJyUyvRJjwda70UAOQBfd7e44anzgHlVATNURMd6VXZ6qxlCZFb1S2NnXEBDyKmiB4EUQOL_P40jTESMsmZmCTEoNiMK5H1j7zgoYsnT9wlcLkt7u19xos_tPLczwZIsOoq-SDwHR1nMe4dVUwPxb_L2V8bOZD4DSoV0nFiVY8Qw-EnrDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVswiuXU26EqfFy5qGDiqA1bhzifC1he3zSyhgSwAzk_IDXR00WHIt4FOSA3H6gy9bClTS8Qk_USLwtkImY6R2SuEvDmgKW826Mo2W4rpp8jO_1WfA6As8EUl1h2O8oashhUIeGE0ncV-iwqXADqGCknviE_LFsfgeuN-D-twW8KRUuib6fEfKQzlo2zVhmn7YTzQ94FEk54277U8tOdTwGwMiP-UrAU-6RqxtTzBR1XYDTTP3qebdcTSorvxAkkidgOvJrAfwkYq8fWVUR9OwqFjV_T7pqcP8hTo1p8BXiF_hhHJ5hfWn7ukzBHdUA18YAia-W2dERtSiq0b1s7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWFC6EhzOD4YryaLUq-N_UuVaUPAVGFeZgCyPA20rAoCWRyJVW4ZLz2iqH4Mhu3rze3lfIHZL2xABl73IfhthMLFRN_eGk2-zJyt_Vfu-CmV-zLNiJt67U-LW6u31MTeB021zsL8Z1EvBDACFViCeW4JzKtNhMJiyap37iXFSflRPDbTu-3fWQVaVh6pKUIiOfxFqGXRSOzl2z78_dB5dFx0MzYgSRSZIPl3sQ2VLksvdFEq3tvBXojrKZKwi30phI0Ff2zFrD7uF60nqZULjVQ0234BY7PunaovbI_km76EOA1ShklPqPTHpjliWoFPTumSsRZzQglqavqCNIjfpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ3PzzP56to2LF2pMK06u6oGRZ7mTJESOO4nTJWYIxkm1PJmK0ssPHKPdTw7cV18zue6Bs0YwWJ63dsUcI9TgNMl3Ub_nzP8Sy7KMMU2jGv4qIjbWC94Sfmv4kijaVZOQDg021PpJCJoEp9falqkBLBOKKOWHulx0V5YT1Le2jETsQrALsbldJbEwenIwLM5cy_Dam6udJv9lc8bIonHub4RBipwxwhSeIYwlVBGdfIsw5haSKZN8rQq7ikQXf5eA9mAzKPNaqtf_M5ViXQ-0qUfL0UP9FFSEYjUmGClVmrgs-XG_BPg9Lnj3o95_StBU-JVe8_XNvjZTM9AowNpSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0Lw3gr4Q3SDIdrABjjAIxTSvKDP-Cr97zHqqlkBkeQymxS4U-03g-x_dR08TOfYXBZKVaT2QxNDffXSQzn42zaeM8OCN_uwIu01wtr4-Bbi5Q2iSJlc2TAJ_jeQj9HM2QB5mQgKdrIobcK1-QfUfkFfzXBtV7DRLe6jwMiD7H5r8i8W4p_YV9oUScFJ_AQNllzNPpsTZBPp9RVa1kroqDtW6vFpSGkvSCrkmkwdnZQrSiHp0DuZb83wgqRqGZLAcchgIb0Pd7mkSH_o2-76q3uP0nImlQ9m4wJKBotQ9r_bjK-0bvqJ_UuzkeR5m0NoiTn7RJpHrST9hRLMVrSNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0pVrvFxbHvYV1Fu54YWT5AFemAHK9ZLEaX-EYzlgOcDlWN-d_E4LElezBfhFsppizI_N-LgQADC8E_7jnXc66LSgoFRYJQXdjHjMlTYOLazwjbez9gxwjRFKAmcD0ffdOM327HCasd4_OeqACcCNP0fTSf7zQUfZhIHAaXTxTxsMlvfQVV5n1byI8cFb5Ob6ifdHm2TFSgWdpLg0xswcKy7P51aPePkW5tWA70nz8H49Ft3KhIwMUTOYZSQhn-kwp5bY7zUcWeqcv0JUfFibHJkLRVAW7Subs3SIPIF8jl8CWoL4ueU0xlwuZEtUOQ1oYBir1RtkyiKYxqe1KP0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=mz2nV_pAjS-OCxDn--7yoPJHUuTCrX7MFwh2IZ6q20YgGQTjTqI24n6_ppsLIHRe0qs1YF9G5jRXM8fhgjeDVu_T5lhkFtGPQOu-z7HL-8AepBYzZtOjA-gbWbQ6e50vZUNOHcuD6qyg02hNdc5VWYirncWosztftKff652jbHzYHDOwjU11g5LskH9NudSylYXhZM3zNujct-Kml7EYvlQNaHI00_mp2S6tfkKRn-X4-V_LMr9xKDi0xHdoK8-r8aR6S_GLvbElVfgeyre36ppz2aU6Ns6wBHN_of6uRG8UTWc6wODluTr8z5A9rsj-UVhcLKwLFsFo5DwIwzWoMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=mz2nV_pAjS-OCxDn--7yoPJHUuTCrX7MFwh2IZ6q20YgGQTjTqI24n6_ppsLIHRe0qs1YF9G5jRXM8fhgjeDVu_T5lhkFtGPQOu-z7HL-8AepBYzZtOjA-gbWbQ6e50vZUNOHcuD6qyg02hNdc5VWYirncWosztftKff652jbHzYHDOwjU11g5LskH9NudSylYXhZM3zNujct-Kml7EYvlQNaHI00_mp2S6tfkKRn-X4-V_LMr9xKDi0xHdoK8-r8aR6S_GLvbElVfgeyre36ppz2aU6Ns6wBHN_of6uRG8UTWc6wODluTr8z5A9rsj-UVhcLKwLFsFo5DwIwzWoMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25067" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkBaWU3Oj7ySQTcfN-TywZtjCoZZnB5o7NqQ4H5aJhofsVaBSyQsdXbwVcIr8AJ7LWU5sl-MVGh0cOYHKPH8RhYgS5VwXYNqfSBGDOjVdM4aRBVbTC1cSweJjqAALx1KpRHwUYkkh0kThNSyL7hp7YoroHRkPXVZtasA29pgpovoOr8uxpcPCwYXvS00D56aEDzl0E1XuZlrkMjTXCCWG53Yu-8zLNriIA4201LLu8tL4Kbt4PObn5pOut9cRKKxWloGgUjaphRWJCHAKJTMIdKdnLzig6iz7MKp_M9dbfplS60L-52KiSSPdWZeff6xo9qHmAWioBk73GmOiW3hyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzSaMNZgY1vbKYK-ZbJNpV6WkpWs6OVJ1dQjSnFdJsHZCEI416dm11z35OpviceRESPa608upOyUvKw9CrvsF1N4RyIDJkFCdCds-gV8dACwLLfFvUg5MLioa_YZyRdf93efW0YO93tnqgfbA0JgjyknLtUVMrFIij9dGCnQ1iGbgHTSHMcam6loNr9aasFyjxUKWJGOkrrmvG89qQ9dRZZjZS4BxJQDMIwS0yWYDS-DvcmB2ZsgN23AJ2KVFzuthm3yX-Uz5LnxAv3nmZyWJLk_47jE_Dt60O8w5C1Ox0k5aNvDbHpUx9_AE0VYREMNq1imS3G6suSTtRiQEHg7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=GzhZWvTL0plxelAl4QKU14mS-ucHL01izHdibEk616zBvZaP2uiN8vqpdoqNiHrneGlJ-Og0VbSFSUXXZxa9DJiDKFkIlc8QFvQltIFUI6yPAP9oJ5VGFxduIjVhkDbExCUyX0fYLlJK7_0AY6IwHQsr-F796m6JnOnD7w3JGveh3JgOKnafsquDgxt8qZzxxayUiZBAKrQOfPCm1CyTCe8kzzMpKwx7xGL4M1UO9x6m6EZ_s0MwKymYymMfLtRyZnlmUU6BTwaRhZN2LLqJFPZ8nyltXSh6DybH8LuUrXzwP5sjFB9CpRURFUIwo9ZhALj5XnUbJGEp78K3wp5tzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=GzhZWvTL0plxelAl4QKU14mS-ucHL01izHdibEk616zBvZaP2uiN8vqpdoqNiHrneGlJ-Og0VbSFSUXXZxa9DJiDKFkIlc8QFvQltIFUI6yPAP9oJ5VGFxduIjVhkDbExCUyX0fYLlJK7_0AY6IwHQsr-F796m6JnOnD7w3JGveh3JgOKnafsquDgxt8qZzxxayUiZBAKrQOfPCm1CyTCe8kzzMpKwx7xGL4M1UO9x6m6EZ_s0MwKymYymMfLtRyZnlmUU6BTwaRhZN2LLqJFPZ8nyltXSh6DybH8LuUrXzwP5sjFB9CpRURFUIwo9ZhALj5XnUbJGEp78K3wp5tzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=WGe51PCPJCT5xe99OvKhQqDPjRr3X-WrgmGWmP_qDzwcWVgR-Y1A_CPyhqD_VEYck1DIxLYIJXLR9x7k4bnSf2pH5K86vuUXRQf-1CURhklp46JmQbkAyzBZQvi4Vo1O_LQVm2GNszzfQ8swkRp8bD8YirUi0Afh96iVasS_aKpkGxeW0q2rYc8zLZR8gIQ7kdYyHoN54pR55urmUhTBGQnCTqya9U68bBIr7My70lMx4ReS3V7PofvMg5b76DUFuqgD-bu8uzfjKIjk4ibRrS--s_XFIbWBdUumEq1TgJmxsc7WUpHFm8U9nKeaC7kwK0Uvc98DlgdPGorhZCH_WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=WGe51PCPJCT5xe99OvKhQqDPjRr3X-WrgmGWmP_qDzwcWVgR-Y1A_CPyhqD_VEYck1DIxLYIJXLR9x7k4bnSf2pH5K86vuUXRQf-1CURhklp46JmQbkAyzBZQvi4Vo1O_LQVm2GNszzfQ8swkRp8bD8YirUi0Afh96iVasS_aKpkGxeW0q2rYc8zLZR8gIQ7kdYyHoN54pR55urmUhTBGQnCTqya9U68bBIr7My70lMx4ReS3V7PofvMg5b76DUFuqgD-bu8uzfjKIjk4ibRrS--s_XFIbWBdUumEq1TgJmxsc7WUpHFm8U9nKeaC7kwK0Uvc98DlgdPGorhZCH_WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=KgXpuWzibQZjxaMqJh6j6ZXa0PblSJK3SNuJhQ3XrC0lxxxjeYnH2oLBk40vqGkq0LgrYUxx8Rlre7iJgRxstna8Lc-qvGxsiY1QyFL37WIwd4TTm-i4Vc3mqFTBpwoRJ_qS1izQNaMKuh_ppGDv_zUo2k-9pka8geLHUVHJSDYORWiwgR10i7gDPsn3m1Jlkc0iC-yyAG-nrXFkBk5vHI_eVrwWtfoEKYWn0saJ_Rqeoab0k8ev8iLKF3WM9qdu3ut6g7KopSTDVyJ-coywlbvlatZsOB4tahJrKUWSNgMzzxAcxDPRieHw8vpGJdEPDysqFMDyAhaj1ftgcHP7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=KgXpuWzibQZjxaMqJh6j6ZXa0PblSJK3SNuJhQ3XrC0lxxxjeYnH2oLBk40vqGkq0LgrYUxx8Rlre7iJgRxstna8Lc-qvGxsiY1QyFL37WIwd4TTm-i4Vc3mqFTBpwoRJ_qS1izQNaMKuh_ppGDv_zUo2k-9pka8geLHUVHJSDYORWiwgR10i7gDPsn3m1Jlkc0iC-yyAG-nrXFkBk5vHI_eVrwWtfoEKYWn0saJ_Rqeoab0k8ev8iLKF3WM9qdu3ut6g7KopSTDVyJ-coywlbvlatZsOB4tahJrKUWSNgMzzxAcxDPRieHw8vpGJdEPDysqFMDyAhaj1ftgcHP7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حسادت عادل‌به‌حال‌خوب‌نروژی‌ها بعداز پیروزی ارزشمند و تاریخی‌مقابل برزیل و صعود به ¼ نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25062" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=ExIjW-c3u6mv-QV0wqbefTlcY0Quj_AuGmkGnIAyDAch6Cef1KoQQRXK6nh1jt65-9PP5_9GexHQztUNlnMrbEeETCszDgtOShmqCDrjflqw0sAo2jIvNF6tg3vF8IPRS24P7OPTQgk8aWJUfPG5K-mmcV8pBp59_-XLgmkZuDDyYVIX4qvWH31_P0ewRp3N8Dcy-1lwE9evFI_kztoJkrDoib8wAlYCURxI1g30ZJi5xMPz2Mkz_fb6EmaZ6U-03ueQxmJ7S_uII6nCtJ9FOEyWuc8yYz3nCi5ifW6_HN-ne8zVSG2Z71V_3Gmm9sWl4zoQWPeQrdBfcAZ7UB-i3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=ExIjW-c3u6mv-QV0wqbefTlcY0Quj_AuGmkGnIAyDAch6Cef1KoQQRXK6nh1jt65-9PP5_9GexHQztUNlnMrbEeETCszDgtOShmqCDrjflqw0sAo2jIvNF6tg3vF8IPRS24P7OPTQgk8aWJUfPG5K-mmcV8pBp59_-XLgmkZuDDyYVIX4qvWH31_P0ewRp3N8Dcy-1lwE9evFI_kztoJkrDoib8wAlYCURxI1g30ZJi5xMPz2Mkz_fb6EmaZ6U-03ueQxmJ7S_uII6nCtJ9FOEyWuc8yYz3nCi5ifW6_HN-ne8zVSG2Z71V_3Gmm9sWl4zoQWPeQrdBfcAZ7UB-i3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از صحبت‌های جواد خیابانی دیگ رد داده میگه باید در پایان جام جهانی بستری شم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25061" target="_blank">📅 09:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏆
ویدیویی جالب از نظر دختران خارجی درباره بازیکنان ایرانی و نمره دادن به قیافه ملی پوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25060" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=ogVgYO0laNF2VpKRAYuXXDyx7MXCZSKMmPzdXi6j8sd0I_VlAvrw0IZ739_5s-Wq7P5MfmJGmdySoMjM10j9sxJMLWY5CVgTmq_iPQ6c251JfHxCdwyk6B4lEIbNdAC7VRreXD3_uCZnO3Tz_kla21LKAf5DPT0HbSFg2DstC17B9wwvRGSXwO20lWc43hn6c4556JzPqvTtugY1mOnNqxXgthZJQWjKi9pBw6unAiknQV3zNrUZ3_1Yq2IaZTv3g38PwDzJtFC_zvzlYX9sVjI7GAklAWt2j7Eovg1T6dJQUXVSgnUy5DtqcN6hvhTS4NMofQGo_fCttCqUFqh0ZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=ogVgYO0laNF2VpKRAYuXXDyx7MXCZSKMmPzdXi6j8sd0I_VlAvrw0IZ739_5s-Wq7P5MfmJGmdySoMjM10j9sxJMLWY5CVgTmq_iPQ6c251JfHxCdwyk6B4lEIbNdAC7VRreXD3_uCZnO3Tz_kla21LKAf5DPT0HbSFg2DstC17B9wwvRGSXwO20lWc43hn6c4556JzPqvTtugY1mOnNqxXgthZJQWjKi9pBw6unAiknQV3zNrUZ3_1Yq2IaZTv3g38PwDzJtFC_zvzlYX9sVjI7GAklAWt2j7Eovg1T6dJQUXVSgnUy5DtqcN6hvhTS4NMofQGo_fCttCqUFqh0ZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هری‌کین بنده‌خدا درپایان بازی با مکزیک صداش بالا نمیاد خبرنگاره‌جلوش رو گرفته میگه حرف بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25059" target="_blank">📅 08:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6Ri9W_5a9qxUrzjsxjaPM0qoQKHgORaCVxQlrL9VhSoPkIGU3VH3T2Xgb7pcBC4yfHUmLjstXK8ALiYiOmY8MkDEDNXFaLbX85qGYWfF59Wcu4PmUhDZmF0Oi1F6SwKQ1BLZ8xoXLxD2i0c4A_HrFx3_JgPvWRgVxQnvAulhX9fh864QiXTNQGNyU2RjuZbyX2fkKqz609ms6cZGbN-IwsAm581Yl4R8mu7sflTuoZnB987bEnSqX0MnCEMfahohlFfPaVMaLt6GMUW0OSyr4Qjdrs7zM-aHkgJvb3oxEP3ihbjQqOinNnilw8L99ict4vxGetKq7rbw1PObU20Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مرحله یک‌ هشتم نهایی جام جهانی 2026؛ پیروزی‌ارزشمند و البته نفسگیر سه شیرها مقابل مکزیک میزبان و صعود به ¼ نهایی رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25058" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQbCBZN53NcP1NyNhkc1DiXdaKDRp8-4sua6ox-2msD9qD8UTEN7SpwRkT4JKJcsH2zzlowzwI_YEmgK7jssx29fJR4fuj_QEt67kKiZy58Jwv94_OCwnBsaGO6x3Z10Gg5yPpyVCm0QWlVM87WQ2sRtgekT251lOxcf1735zcbU3lmsdZrj_-lNQTNdVnPChbDvLf_msRuwF8GogSKiTh3Wyjqjzm6AvmS1dQOlrF0ATmcfc2XHudBC9cQyH9Y-P9EFHmZeoaZ61G_IrI5QVyL_5I3H80QkSuNpuziACtEF_VXUmRf1Ek1On66W6iJaHi3KIEqnpMilf42-NmOzbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odvS1PnIG88goQC0fpNDdQbzF7SYOVuXN62RGUBC1AUh1a9X2ZkTcQ7EyDDBsI0TGn4pvmkMAlKXkQo0B-lmuzVoabmyruI4Ab_8a6k0x2ie_k4ZGriU33Jbc4UHGPBn40TkFESd-OCQ8FSvT20EVGvTxiydObCGi-K_iQk-5lf5zuGqTbVnxqEwTEN1eWb1pTUJ683b166Sy725IFOTF5SJC3mBJVzL6RnuDhInizCwnNnpxcuQoluZn6zgbQo1o3UxquZXkjj94JDi2SV74V8cimJsjFEhBQZvwEIlkjtGlPVzzim-xDUC2Gb1c6NB33nUY4A320I7wF4TmK6hIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25056" target="_blank">📅 07:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8c1Pp3mOGWMeXw5oLqHvKNjWWqweySmuJxPqPLuyajW0-5nHz1uTX444d02fe8fJBSuD0SV5OpenM0I_-VqxIwTZ_xKGdJgd_EVKyZHqaHfMeXFC14JrZtd4-HzwDYVGN2ND9GDsMEIyYlCzZXCqQLowt5YEllhSyeBb2Btfk1CWdvaK1Vh3Xv5AP-so8DBSRIZ52B2BtW4mzi-qX6aRgsb9uiTzDVXOfcSqApa_PVpGhTros6C5areHIkdOMNMhze1xlvUXMCAAx_Mlx6agtumm6hY40AkA562qqr__YI-Tm8e2Ac4H4-phCsvaxOdRT1TLAJ6M4iTIBq3VQ7H9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYAvrzCbYUGCv2u3gjGgLfZHqPg3p4Aqpex4clRmNA993xHjrQSMbuwfAwiFxaGLoS_vCrRYDFYvSWHGkNgNbyZm4E_tnowl0utSE7mf076dzidmTNiLaDExLnwMB9EwNW8gVIxk4T-w5F2l9Bw5tu8hlAIzMwvzN3ZDpgHGp765KXsQQ8Ycl-ZDjrYtrDQt_ChOIlHxuNSf4Inxo-zIGT1QOv4e9H7W7FofmIaBgevioYr-uwUoBdG_cF1dO2D-YcmZ83f8VBXR5BuxXI4EpjKo2HzK4RjMi8DAw8-2hmP2eejdX1HCWz3TZIIty1SN81fNZxCF5Noa7A32UCYhow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G82OMEHs00WCcjTQrRML-MWFFUtXng2cOkDmSb-QAkG09IsO_xT-cGwHC3FkUy8nstVLMpYyS2T3p3y4rrsniQk4CWum0OihZUY1QQrF-tKEx5FxFz9ZITVpj2ciVBK86AjuFzm0lb3VsHbjxKp20QRk24gt5Nnl6VCO1jh6hZAYAyRi19rTcghUnYxR7zvD97MH-z0Du5OmwhXmEIaNdVGeGoNzYFA3_Icisu3hfCDNwI21WaAdxyTUJly0arxNaeryQYXfkBf5eOLmQDOVMbQQvKZ0T4mUSyjhhza87xo-TeFMJtvL22xkbZgYxMh2sXF5a2DL0HcrA6aCVLz1WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW36cBWFWEP2lXr1A_aaxXL15X9vLjORTVRgrqEsHW5qcuOVPSCC5nawS7Ha2Ak0nPNXGdpXC4MaXT-q6WAUhAYY84FduEDfV0rdANXJQHdf0ODeZN1q5tfz9Ak1WZPVU2eIZUaMN2-3trQ8E8n412-jHzUa2-sQt-lKSHGMJEgLnsn-ysACWllfTvP6hc1uKVS8DNr8bvrcrEa_mfQsbdKZgdcCJ5X7tGdOJPXhB8QulWnjDq0RR_fJyLasZ9ESoqBFyPDZRH7A8dFKSl_vdl5t34WWPA7v38GzNZypUJRlggDAsAFG6x5qMgtRMXvNkAe8_iIHTpA03Su-JaOt7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باز هم ناکامی تیم ملی برزیل در مرحله حذفی جام جهانی؛ حذف سلسائو در مرحله حذفی شش دوره اخیر جام جهانی این بار با کارلو آنجلوتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/25050" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWEIOL9Wy7LR-Hea7cHUcveBLVWzNdeUl5ldcAFydjji1xSam9pO9rXldkU5zlVeth7fDgGOHjNvN8kGOHOZtYEymIuHeWz1zzLsjMHrYcdAgF4C9CNNzFN3S1q2D8rRoC7g-pmuaze6D2auyLOpif-RyvOBTj8Ul921zn58wZxO8-gY6wGf5YsVlXWb1JkG8hwGUu90fqQXwMa1sBG8mt965MUOxzdgD-S208QdJh-yEx69O8STZMak9qyoQyIEzEIlYjMweienJ0oj0_rDW6CKlKuqOygjGtQg-TTa8MXVrMyViqT_hXS1erzgIpJnkBBDtKVLC4XQ-rgKpbmbWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/persiana_Soccer/25049" target="_blank">📅 01:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcaeDscWJuhkeDGBKDMi9Sc_Biz0G45jKQNF4bxTNWF6fx-UKgLCB39yAfSv6Sm9isluIt4bH1aAzs0-uLWGT_k4fnTUfXWLz9sse1J4YoVQbfjgqgxYr8zcwS7PbrNjwndVF0ICxH4R2tuq2UMAqJ6zxVIgZ367byGtFxDk0Ie2HEbHjJ2eExhjMI9aKIW044quKOSioNdn3KJM10kIeeerVJHWLOvvB0CE3qXxnRVHgfqTEP_fASkBuE8l8d80BKI4kXNEZYA19bEDQFS5YqApJnsyIESyJlE7PYcisqtpNz7U9jzM5EKei4hQpNU4kpj_wU5QaAUfpkGoZMB07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/25047" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eV4TUxi8cY2ku_qtR0ED8P_wQvH6aeJnZDhWjK1JRIFNRtjvkTuO8Yj_nKXx_UcjknrdtUGEvKmxenHZ6ah3iPKk6RpU2sN2etV26Dch6yv1BB1tZdml2VVRl-hGoT83tL2a-WpFhodP09B6KD3zDxL8hjDoDL6xY26cxL_ce1Cpb1JdzxQ9VGiEdCOm4TkBqXMp1upo7DDf58PKJgb1BfeRD5nlFm_GXNpVzZjfT1kiahYZWXo0C8zNIpW-O5wso44ziS4sG0oKUfbMnjrOHqG2ITt1XT4-crnmrRfzNkX87wdfi04nt0wBLbXGy7oZMEO0N2R2TFZY66XRd2ceeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود فرانسه و نروژ با درخشش‌ادامه‌دارامباپه و هالند و طلسم‌ادامه‌دار تیم برزیل مقابل‌تیم‌های‌اروپایی در دورحذفی جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25046" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiOMSQDZc4_xCWYlSXUIlUBQL0VCMeV_EsaEBfi69U-kr1TPm4iQPRGNggBmanEQv_lGc3F7nUz-gntXSOYsFozXXWl1cOQubmAQ8cDIBmpspQ_N5wZ5Uw2dkly5WBnbDgq2-kJdHBWqkaTIr57J7TrHlr8EOOttF5wboNOSxES6Dd2pOYv8u2GTlwzCM2NRGDYsHtl1YtTxRtFo_ZSQ09uOnmQeu_Uu82h6vWAI1XLn9zSIypy83TFk9h4PwLh7YdqOH4DLFLCl0vbEhNTdt4ANaVgA7lp8f_krw280u5j_lLd9F42iZfZd68Y5khTWxwK_hbzwZcJ2eV0rOn7KsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25045" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇳🇴
خوشحالی هواداران تیم ملی نروژ از صعود این تیم به یک‌چهارم نهایی جام؛ نروژ به مصاف برنده مسابقه دو تیم انگلیس - مکزیک میره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25044" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKdwApm1zP7_vehLoaHMFcdvFeJ79YlSpx8OtGwFG_Nxod1-X2zfLneg6DBs_Yp6P6ohOZW9rxlZ0ecHkZzLfjYT4xqk_YrZBP8Ng2lrRlTQ1YMIm3m9BxV_cXl_m4D9fsIxcI_dZ64EVpn17TP8g4ilXXfVLeQHke2auaJF6SGG6Ptq_2idNPZSddq65NjBzFErxCIqFDJiZq8kpzwvYbZhkq0Q6HtmWzywn3WRq9EoNqpkaOeGso7ufQpFq11kUG3g3e-qwDWxcVP48GwTSM1CZti-kVVI7MWx14BxcLBTRvoVU4QSyXJCVu5aI0ZEBfCbeFePWUraSz0GbVj89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25043" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de979c355.mp4?token=JhQVn-KD2LLn-mKN5sW5NvBJ9jRxmjzhG7jfC3ZT-wsVLY4uBQ1S9GXx31S7TsBBEtanlsTAI2RmkOZIcaXTnbrJ6n3dZRvg2Gqi0LocnK7URPovNS7QjNXmSDEj5dnU2CU69dGah2l6Q4IeXndaRT29gr6F3aTsRBI5fIZV1pTXcdgRLYzzvWvlFxNCZaRLM-OEGIoFOBT750awjXOuKga8oshTK51LxqQG6oFKAIDVvdP9C_1tmTW6MBvI45DogObz9AtjuHDC2CkHkIqy5NG37z56sAmfX0VFnzxOIWvJrs-BlJ5LUK7qG-Lxtf8IC5tVcRt4Eu2pL8G448ROYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de979c355.mp4?token=JhQVn-KD2LLn-mKN5sW5NvBJ9jRxmjzhG7jfC3ZT-wsVLY4uBQ1S9GXx31S7TsBBEtanlsTAI2RmkOZIcaXTnbrJ6n3dZRvg2Gqi0LocnK7URPovNS7QjNXmSDEj5dnU2CU69dGah2l6Q4IeXndaRT29gr6F3aTsRBI5fIZV1pTXcdgRLYzzvWvlFxNCZaRLM-OEGIoFOBT750awjXOuKga8oshTK51LxqQG6oFKAIDVvdP9C_1tmTW6MBvI45DogObz9AtjuHDC2CkHkIqy5NG37z56sAmfX0VFnzxOIWvJrs-BlJ5LUK7qG-Lxtf8IC5tVcRt4Eu2pL8G448ROYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25042" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=aTvSk5zY49spVXFKbeMTszkFiZ5zLNj2Gqd-YLGhTM9HEDxp5xqbR_PiLUJ3q03MxGf1lVS0LFbP8zWF9weyN9Cv_JwSPH2xyhA5QRktA__nVN4s3JYZqeJqTjyP1QfW2-nXHlngamKrjoyPA3ohiLQ_rylQhzDf9veZ2WN8_JFjdDB_JU_YC0VRkQ5bF62h3MZl8H8fyEyG_1Ve8vkKuMlZaaKLg6heeKSw3SFT9Reyvk6BZHbzQvJu1q2BTeTLBxeGmyzBBXD4GGOon-YlvipFcVZrCizXPkDuhE1N93TMZAng8jZ1GwWPAetN1gURrEraIffFJ6rL1d_leysgog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=aTvSk5zY49spVXFKbeMTszkFiZ5zLNj2Gqd-YLGhTM9HEDxp5xqbR_PiLUJ3q03MxGf1lVS0LFbP8zWF9weyN9Cv_JwSPH2xyhA5QRktA__nVN4s3JYZqeJqTjyP1QfW2-nXHlngamKrjoyPA3ohiLQ_rylQhzDf9veZ2WN8_JFjdDB_JU_YC0VRkQ5bF62h3MZl8H8fyEyG_1Ve8vkKuMlZaaKLg6heeKSw3SFT9Reyvk6BZHbzQvJu1q2BTeTLBxeGmyzBBXD4GGOon-YlvipFcVZrCizXPkDuhE1N93TMZAng8jZ1GwWPAetN1gURrEraIffFJ6rL1d_leysgog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=QzrQtJLn9zRkH2y6UXwkKCNO8588_pH7DpCXw5PgAcQVImUVs1uHhpKe-Ck-WJsRxD8xoQpo183hrTuHO14GWixbm5Fl8iuc36n-dUHIx4CoNIYxhl0QAD2FlPNQTnYYBVO0PCLxR8m1Y7_SiTplvkFcJUYyfJqHJtYpW20pJlcVQRgqWdnHgiA44kU6S54FfdkYrQ938-T1MUH-nsQMfN7ztCw-RXKuiGR1qPMzS3SWrVbK1vDkGevU1uolWn3e0HrLdHEnV21X-cOavzFtKqHi1IJjHthUhUroID5i67tsqGNe6HSaslDOA_hKF1aZcHtPPaN3Wgwe3wfEl7Bylg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=QzrQtJLn9zRkH2y6UXwkKCNO8588_pH7DpCXw5PgAcQVImUVs1uHhpKe-Ck-WJsRxD8xoQpo183hrTuHO14GWixbm5Fl8iuc36n-dUHIx4CoNIYxhl0QAD2FlPNQTnYYBVO0PCLxR8m1Y7_SiTplvkFcJUYyfJqHJtYpW20pJlcVQRgqWdnHgiA44kU6S54FfdkYrQ938-T1MUH-nsQMfN7ztCw-RXKuiGR1qPMzS3SWrVbK1vDkGevU1uolWn3e0HrLdHEnV21X-cOavzFtKqHi1IJjHthUhUroID5i67tsqGNe6HSaslDOA_hKF1aZcHtPPaN3Wgwe3wfEl7Bylg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb0RaYeGW9j9SlF3T0ItVy0OeF6-Axf5FtXepQAX4DtiSesX-07qGcHYFhkfn0vla-ODWNIwW_cwGbDxXdIewvgx5rnMMemUmr9UkxPx84UswuwdmK0ceTXkAx1IBY3-JuQJmuVP1umvbWnl8mpSpBTTJG4-M-8TMcmegl57Yv6Z_DPRNp6opuWN_T4oVGVWDN4QPmKH8mnbqxyfIZo_WILiexsduP10i9Ff84aN0L0mSj5_MXz1Rf08wOUKu7nbdkcWeBEWsgpuTPMWUWFFWAA63GY-rcWZIzLj5rwP3vjWIu0txClhFWrw1ed0giubvkSYcRnTiNhW74_l1-LWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqSPLEF-bGAcz03VrQvdahd1qryo4BJ2fEEkZj-89E0IW6O-4m9jtWdI5DTIdr3oKcjwoZ6td8Jau49SzzJ_7dMrUkg6eWyHfXTUcOsAkPalk1zlvSTraAVjpepbJILW93KZhbU6h-Bixwf5kL1Nv_ej9SsyDSg77MYIADbl2VDgHmb0MSTEfvwIFQqCgPcankcFUFzicTZ0LPlH9KuHlC14eG3oDbMRs9Mf9RvsgkdL7EYhD-PkvLlnUrbatUxAosgKmHygs9mU0k7a_bPGX_l1D_LuwnmTNKZoUuDUhohKNaXrFC-9Cx1I9RJey-FTkrLGXGaLo2j5Mcq2Flkl5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25038" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8NrsSW_lzD0fw0zyPmWwIPxrGPfcpecNnmN9IFWHwcSS4K-zf7C9zdXoIjrspA1mnxbs26c-12LRqVGwryElbRC7KP4toqT-nWiWZ7QhdAqGIJxgSG7gx1_fWzRU3X7DIM-U2M-L7n6g-P_SEnycJnUUkSYCOkRFG_PfmqSfZ-1vWRjz3brZ6ibecXgLun5OCYSafvRzCK-AzVByCA2YJSdW4uRDgtDLC1KxGtKzVTN8glsskQysFbgv8DuYA9YqRX3VJh8HiHK71y6Hjkgxf0gM7YI7e7DhaOwS5CpACQYVunmoPRMF8I6bMZaklewzTkXfHORCoe7-rMVFb3HDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باحذف تیم‌ملی‌غنا از جام‌جهانی؛ به احتمال زیاد کارلوس کی‌روش به زودی قراردادش رو با فدراسیون فوتبال این کشور فسخ خواهد کرد و جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25037" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=nXXWiGi5ZYJ5WpH9bUOOVDXHfh5plyvp_gc9CllPC3FGpkMMvGXEtmrcB4pCnX4S18GfYgC3Ba0Q3iz4ryoArGm2HEjIZling7BSalCFSU_p04TOn8Ipx8epPO2VKWJlYJH_NQtqtviH0AahDRd6qe2Rv1_upp5sd6IekhoF272QT1zf15S-f8M3oRP7j2JQuFcBzyzxJfGCjk6sn0M0tlXAy323VeMfKYPAwNfUt8n5DOsnk14utwsE9qg-BB96qWKxEvo8cKyysxKOlGbG5o_WKLc6kJ7NVZ0s5zO2mJ9loJiiR8rHcyMWXEWu3-eeLEBVOjY4YkNYfBAI2cv-vzzi9-jZJrK5lhZgizM9MAeTWAYlfZBQzcP55v8efELKiGX_HENe6NOuc_hVSfi5maRrMK8qnIJRYv7SzrkF7oPM75QJkSOGOXYeOSksBRgI01Ibom7o02w8UEGF4Ax2sITjwag6u9CHpD4FMvu3UsXRN481FKdLZyI5KYSZ7ExdzOtG_DRdBOGWLkJ5s6qYQSJ6fLujsezUfQfmlNuBoM4DdaP27pv3hiLNvOd9lmROrTG4B-HFAtOOrDsjc7DVD1ik3zKjKz7p2oXLnbazS0iwiU8ZBfCRc1mmmhL0ZJ-FeLigyYMeJhAgWn3DZ_hVhZv_YBabLs_C8RbM9xoCSys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=nXXWiGi5ZYJ5WpH9bUOOVDXHfh5plyvp_gc9CllPC3FGpkMMvGXEtmrcB4pCnX4S18GfYgC3Ba0Q3iz4ryoArGm2HEjIZling7BSalCFSU_p04TOn8Ipx8epPO2VKWJlYJH_NQtqtviH0AahDRd6qe2Rv1_upp5sd6IekhoF272QT1zf15S-f8M3oRP7j2JQuFcBzyzxJfGCjk6sn0M0tlXAy323VeMfKYPAwNfUt8n5DOsnk14utwsE9qg-BB96qWKxEvo8cKyysxKOlGbG5o_WKLc6kJ7NVZ0s5zO2mJ9loJiiR8rHcyMWXEWu3-eeLEBVOjY4YkNYfBAI2cv-vzzi9-jZJrK5lhZgizM9MAeTWAYlfZBQzcP55v8efELKiGX_HENe6NOuc_hVSfi5maRrMK8qnIJRYv7SzrkF7oPM75QJkSOGOXYeOSksBRgI01Ibom7o02w8UEGF4Ax2sITjwag6u9CHpD4FMvu3UsXRN481FKdLZyI5KYSZ7ExdzOtG_DRdBOGWLkJ5s6qYQSJ6fLujsezUfQfmlNuBoM4DdaP27pv3hiLNvOd9lmROrTG4B-HFAtOOrDsjc7DVD1ik3zKjKz7p2oXLnbazS0iwiU8ZBfCRc1mmmhL0ZJ-FeLigyYMeJhAgWn3DZ_hVhZv_YBabLs_C8RbM9xoCSys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
درگیری‌رونالدو بامارسلوبچلرخبرنگار برزیلی در کنفرانس مطبوعاتی پیشاز بازی پرتغال-اسپانیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25036" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQFBYcsl6vbDoIl02zBdLYt7VHv1TnIGZ-YK7wXAz5Yh70sUwwtGx2Padi5Td_e8F3EcqHp5I6HV1GtGVZxqgqVpLZiQvvPn7k7G51H4-UEYvBKirrQkOWAYe3WrDDaD5OhZjW8oNQKvdhXnZT1bmMeV-pfzvR5zerb7QrygO31s-ufLDmeFtQNwTgNM1g6x2LmVc9WvxPRUZbqVaQctd59eNIoa5HupyWxXtK554qPw6EG36Z-tAgerVMX4OLNKDpEf3VFycCdXP3MsWo-5km_4W6abBu2zGBNnrb1AXfV8ubZBozLs-Xv4vVXyLnxm82hRhoCK2XDb2qFEmQKfCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvHiLNLPsymWSXZ23hehd_91087rMjuFRXPTiRJwlPUHmI2rlRm2Pl-1vPKJImMyjiEu_GfpwvdMQwOGGdO-WZWkm25Sffr8lAZx9etUvNgybHDksd1y8L_Z3KMvZzfR-l6yRNc8WD_phff0anFc8Rz332C5f26AtYWgfzvrW8m7GcpDnxEbE_2ncOrBFJH8X7cLQNsdOlvgMdyMFhckbwOyvL22ePII30Q4Ovx3jD-CHOTX8HMy9oNmx_3L33AIyvmDxFE7zGSJqtkpU_U4erTyHO3Gd-S25Rt9L_dAAtF9n_xDCyiH6_Nrrd0tPqK4aKhtnWsyhqRjmg83PVGQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsjBvSha3NSZjKiaPCD3jSDWsPtqLzQp5thkuok936veecVL67sI6OJ4nUA1YOZ7ewkGSs6JJOXPhZuhMg46xB79DMnt3H_JIFkBlDYXgfbZ02Q1UaI7kmW26mxdPnVAxuiPIppdgDJnanLAEmBllRDZd2kG8oWmH0-gIswd7uexh-5NCgQf13IhD27R8kn0vK2MtaA68Mv-BFTUustXjefI4P3XFR78kAwnt2O2-LT38wXY1cYcZj8R_Sb-QaPpuovFfKp78iTNCQV-AUJzsbvGMKHQd6r97XwkjtXla9NvwLX80z-H7TQEGyPLYlltG3Z_LCpPqg-I-AsKYuGLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSjR9d-0gOJPSooSbpjkTSNwMlwYfKdpydaWV7GpNeuBREHPf2KP90dfcdiEf0ieVEKXTjqAohjAwUSwZXt_AK-S1LvVjr6F6JCzIcg9nBbp3I_KBcR1QfY-IJIQWaiMgHC5_81NxDHAkkwSDhiAPNmClc7pw3kQPupVwCd7kwWV_Iri3d9Uc79RK6Kty1yiFpdTfx6zrzbww3UJRQ9rc_12Y7GJMBHftAfx5gf9Nh4BExa4Lhg-XaQOdr_u49wcVPwMsIQn2ydD9zNdKysiek3CMpDKjIyEcYPKdHSqniGjTCcBhhYKG4UvTnSz3R6SG6BlOqSZ8obzuED_csVNJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWRn-dc6QIz_X2h97L0EW8-JVNAVMNPdibhKAuF59gD7fHjzR28KGSKGSAx_FrV8tVzXIURb3BHw2Cy3E5Kd22BsAHWK7KNnJOksCMwF0fMrMBW7_FwlTU1x0RAyGkQAqjG1oR86J_fYUdwn3R6TUtbbuax_uyoA96Q_l2ZjfhefDHozh9C-tPlk684kLVrxivZ_z9wPjweAWw_s1rQQzUVQzhlmhzU75_CgfVff590RltvadFwIf2rpBzUdHlF9e1xH4bY82mSkhUm0wX9hpk0GRvkmqcAGpUuPje0xu5mQU7nESEUMT0BPTjrJlhIB5bCw_f5zCmT-DSNVy8O7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzZJbEi5omhE5PgAS5TxoNyJfSkc6s-deeK1ackxLWRzzbU9v7BacDsi4zTSXDnSlOAKAJI7Yu2pnsgoBa8LOKJheM-BI0577H6KLJB-64uD8betz5EGpIL_InxY8tM5lspMw1NWTZHIEvU_1_qK927_1aYGdP9XygVV9P8r9Ra9yrWA0MoyL8YkWF3ELC6MQI3XEVqX1qU_77Ym7TeFmCet73hfoYx0UPSTAQg0Lzf-8L1gtETDAOS2Awo9gLQ0MnAwb5vz0jtVm46DYEde57KHp-VgSWx5ZXEdljseZSGbdhALXIGISqEtCH26yZk3qqV4DmFFOBn0TwostaiRjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A79MetnMiGEd2pFC3U-cEYzmzdvUCxiZL5G3Roc2O4y0ceMHRn8kq4O8UEljAGM9ChE5e9-65RFe2zd6eEw5QZcbzLlD6wfDCk1uWxvRHoS8MPYy8jKxLQpYpIBs-Ng0anLQr5dPCCZuBqijWN4r801CRU7jPBqHZVWs6cwaQMRICq1mpTHzR74mEwJu2pNBME64ltPEPwyuLe_KqCC25MCqkPBMbelBJB_6oJsXhZ6bZ_xdhfUMub6URLgeYQAk9ySszNtWtBbv4UOrPDgAjIN_lq7BuV9XIoiEnMsXgqUWzGLbAILPnBlI0uCyi5vsCpGFot71WSZWFuaiAu_fpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWZC45AFNqEjwF_71li8-P2n12-LSLmELpXCXoVTaVYCq8Xl9lXDQULjDhK_eHq7tXmHIe5RU_KEpU05LqlNaNQ5x2awN3qehwzV1HTdFG7gL-WYSDaxdXDgba3YSpTzvRV93uSP0TWD6oSawQWR4vEdN0wMTicX_FvDAoVYyvkGRNHe0eFs7t9Za9Ej2GQibL2W2JkOLaXv-UagGzy5cpTX4goE3CZw0LdSiBObly1RHdfwNEa50a0J-87CVfirrhBLT31V_8F_yupfaPD0kNWL7UB03cHHiAeJBa1wrBtlxjnfSc46WjomIuxNMP0EF1OnrgoQTzXTBuSws4Nhnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-uENVvNGhT3fCI4U7DORThdzuBPhLRTYP3c1jnAYOT4v7MzaFK4CErWdl491Tkg9NPS_0VA94ADzxvKOeSta4m7rSSVxz17YuBChpC0ghDzFK55PG8DjKD9zstK91vMLqXYe15i8KPYNLMRj6VoFPCx81Kyux2N8RONqI3sWv452zD2ZIFnhtcjVQ89DIKI4S8MOT9tijPlVRzLvO86l8yO905dPFgy_PHOXpwhkxdIbCIn-HQRP9fhaER_yWJrIv-cm14C7zuQjUU8BeCK6Vr8HS6TWwdPvVW8IRCN6rl_e_O95K1OId2lkPaye8RdBhtptzpvE8kxFoiQB_1-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
