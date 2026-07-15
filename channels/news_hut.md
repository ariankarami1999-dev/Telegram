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
<img src="https://cdn4.telesco.pe/file/HgkoQVlOyRrj3YgIiyBX1ZAUiF7bDbh8fW_S10At4-li5FNmrdSrgjlxr9heuiCmt-RiJmfAEuC_mJRkXfnL4sIDto9Gpak3xlBY9TSSDwv2vFO9dAKabIqBNsQAr3j7kp5jv_bsWQ3celvuTdUIWti89KTIj4G7HyCTPh21Jx4OP-TLyVWgqoZbfDTXuKUFDVJNCzT_GbA4m9eWSeL7WAxsMoFNw9sEcdYgTwgoZd6UETxmPp2uvIQxBJy5pbw8NjFUJudH_jiwBOdDhfEeHBWMPSWxlkoRHmXWLhrBTPncWLb-TF5dJXjKw2JTDA051HhJJh8RNNGz0eKidst52g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 171K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 21:13:29</div>
<hr>

<div class="tg-post" id="msg-68200">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
قالیباف:
همزمان با درگیری‌ها، باید از ابزارهای دیپلماسی و مذاکره نیز استفاده کنیم، به گونه‌ای که منافع ملی را تأمین و تقویت کند.
همانطور که بارها تاکید کرده‌ام، مذاکره در این مرحله به معنای تسلیم یا ارائه امتیازات نیست، بلکه در کنار جنگ، بخشی از استراتژی مقاومت و حفظ منافع ملی است.
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/68200" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68199">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
قالیباف:
برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/news_hut/68199" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68198">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
محمدباقر قالیباف:
تفاهم‌نامه وقتی معنا دارد که مفادش معتبر و در حال اجرا باشد. اگر ایران از آن سودی نبرد، دلیلی برای پایبندی وجود ندارد. ما بر اساس اصل «چشم در برابر چشم» عمل می‌کنیم و در برابر بدعهدی، متقابلاً واکنش نشان می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/news_hut/68198" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68197">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.  @News_Hut</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/news_hut/68197" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68196">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dphn2DnH9W25DWJCYXVqqeuuOp-8z-N4u025chL7UR43TpeVo_DOmP--rW4ASSCqhNzLQkvviba9HpWzzqIjgYaLCkSt4g6tyzAdXWa3Kf_tEyUZHbdgWv08Fs4vSJsPN75NSDhDXW5aseN-OatfDI-Qfoq87glsMZb9lCgQG18MLUR6Dbxfl-3wsnptSooBNnsK4m-Hlqr5iFDRChCdOk5xAuf3PCbyTR-MDQpNWjFg1OEZduvMETlxM-aXyuF2PjcpR0KHod6eHa8nQSakogtD6HdBTOMUuEWIRM3yTlyeARWyAULk0aPR3aOfZdwXTkbWHP3BoD4EseZPbTXklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر شهدای حمله آمریکا به پادگان ارتش در ‎بمپور.
@News_Hut</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/news_hut/68196" target="_blank">📅 20:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68195">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA5Qfs2l6M6qazajegQLIJt8j0RbAslwN8KQpwlQk4-zPlF6wGjQPysp8DWME2Y2jQlS5oOGyCQHivfhdXW0BMlxN458eZ5V0cpb6bB9xssOT_fzoJRWY6RQVfpLg2QnxdztvI1UfLtkKZPNS0LV992F_E_4U3BryETdsvCMWJUh9AjxgUL5Wkt5MKO3dbcx-O6HIzxepZRWouVphGSRJEoETMrjEUWpxiduMyUb6-vM4xmYMNcVXQjnB7PXXQbTZ-MFwT4Js4eIZDJ4yODnNvhfR4yU0Wo92s8Ob56-YnYtE6YbHlgcjlvehvNZn8mvUo4_w96JjD-aYwNpc9K5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب عادل دو تا اسطوره‌ی تکرار نشدنی رو آورده، فوتبال ۳۶۰ رو از دست ندین،
کص‌خار میثاقی
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/68195" target="_blank">📅 20:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68193">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMreza</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nc3qM4PGSbBuBeFcjvw_8vtDQehcQPbZTUirAJchzp8GdLDzZSKe0vJX3-zCORf891y2EX0170_1L1SsxtDvJEEu8PUK_pI1HLGJmVX_wNO2lwN5LkWeGig3rjSvf4ElS4qf5UheLQZU7RT5fR3Mb_J4DB51rQT9QVoQ4HVfC0DLiref7WxxcJfadMfF-EZrHZciiDYp2aYZflVJvZ86O9AMwbgn2Dl-4y7t39WI89Zx7aRMIKnTlgFBdFg7PzSMjMNbYul4n1UNZz6D3yeRA_8kHAfELI1L9u36Z2_yg4Y4LX2U4GiOrXUjj2q7NxLayhcZ8rIa7wJ8FZmjzVjBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ectU2xVd7ayyTy-EnoMcUHSb0zxDP1naMmD7M2Jkrmx00l2evBcX8XPqe1pKE020yaTkHAGBSCCGWwzf31gZ4jR4BaxwcWYLRAz1P32LlFZNSUZj9d0KSc-wCX6ZRGtUH8QI8-Kkej4Uz0UQkoNkOfUQew_MytwPoQUrUbUAgyieDFfntomnVRTG9kFYR71dIQrvnzSMkDQr2GqA-bxu8smRZ_s0u2ax35e1keIdsIjd6FzV3lJ8Tu0W8Swcz8lqMu1NvGILxf_twQ24UJJTrYmo_vrONcixjy7rnEYQPCEJi_bhOFz72iwiEA55TTkwS76LszYQPeSVEe7rG6Dj_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Siuuuuuuu
❌
Zhiuuuuuu
✅</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/68193" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68192">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=T7IpgnlLqIhOkocAfwjGJZchgmWNKDD5gEtqVky0KSQSEuFKP4ipf1prCziIgbQItTLWK_paXXUov6rUH-PawJE0nWKm-bgud9VRPnK0dOxIrpBRoHcBTqhU6hSbm86zxWtxNLbHz2lJoC4X455M3QSzbxzFi7v9FqPk4IOFW0ITkqqtKRbNmskrj2sCmVrC6KzymQ87AnJFKT8F6dXQXzByiaa42Fx3ONSW8MiQVi4FQP4bh8kQZ4InkxcjyHlrvkEB8jzG__fOt2DtynsA_aMhL5LGw5sH38dU3-60291jCt9IiStOW2zIQqZURsGnwWgDbaSwpLdsx9mmNA7YAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=T7IpgnlLqIhOkocAfwjGJZchgmWNKDD5gEtqVky0KSQSEuFKP4ipf1prCziIgbQItTLWK_paXXUov6rUH-PawJE0nWKm-bgud9VRPnK0dOxIrpBRoHcBTqhU6hSbm86zxWtxNLbHz2lJoC4X455M3QSzbxzFi7v9FqPk4IOFW0ITkqqtKRbNmskrj2sCmVrC6KzymQ87AnJFKT8F6dXQXzByiaa42Fx3ONSW8MiQVi4FQP4bh8kQZ4InkxcjyHlrvkEB8jzG__fOt2DtynsA_aMhL5LGw5sH38dU3-60291jCt9IiStOW2zIQqZURsGnwWgDbaSwpLdsx9mmNA7YAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا صبح می‌شه به کریستیانو خامنه‌ای خندید ولی کانال زشت می‌شه پس بسه، فک می‌کنه کریس آمریکاییه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/68192" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68191">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKCjyaZ3tAuicWphURu6cp1IKQDs_OOd_iagHFjVGEh-4iyt_KoOYe1fKE-eS9mEwU61AToO-Jdiwjcl1FNeWY2H4ajCkswOMXRq4KpB4uVYCFAOQZtXZG2NNnrzAcqIoqtGj7cl5G8M3DgGv8dmoJHjGK54ZGIuBwOPI2_fFiZ6PTUNb0IkGDlVoCW0orpw8ansLUO7azQ9ke7lL9DaNDjaX9sdodaocrrYGkU02RRjBPDGB94vesDEsoLTsyRx3vNVaXWi2Vr18YD1m62cwh6GPHp81ysTuKJk6FeDU7mgztPlRYh6Ohx343DADtpmQamK1_COciPuztWWumUYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو خامنه‌ای کرایه اسنپ نداشت بره سازمان؟
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68191" target="_blank">📅 20:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68190">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرونالدو</strong></div>
<div class="tg-text">اخه من چکارم؟</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/68190" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68189">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6P92hhrxQkOYWBEqxjmB-M792Jv6AIidCTHbPaliJGY6XXTSs83EbaNxcVl5fB51gorgEgLwGZVZ3dIPf0UANcz24_XeVC9S5zAAjC1ijXD7BxcnmZ0JHCi1fHRBSdmWoZCC529bC43VBcTvzw18W50PolGFIX6jr6cUvL2VRmkOQ_I9LJ9dCNFFvb9bVg3EAMKK7HqoWfHZq270Kohn18OAf1qyUlKUAUxwbRZLVQaQ-7XzMcg29T55oJRRX2NdfpYo_E1DdZdKWCk31ZtiGpmxcXsrXKGGg8lw5W061_eS7RLLQl8mpcZUzqmHX24-yAxKuwVxQP7ZAV0VNFHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:  #hjAly‌</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68189" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68188">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=rR1MGP30PYsobcIx_LNS9oBC80l0VhPAg87xqyQuSajQa5ltCfPERYL4Ya_I1VPsS77e-HdVCs2DrtBwoD4bQSruaN8EhhiuTQvbULEWmLMrx31UW-TYfH-ceIbSfFuT_OINL8YuUQ7CXia70VSNBaB54i0emdZvS-Z_infQiXnMCOjbE0f0VjR3bcki9A9uRBmcbShz6Lv4ivbm029i4QN7gg2doyGAMWCc4ZvaXXU3qUxblemcJTASwM2hxJ6nB1nBOttIPXQWblqG0j5EQa3Ywuv9Eb6Fqb4ol6ApKZtj1Fx-uS2XCAMg8sdTti9gbmuPDeRFgNYt8Dg_wceiSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=rR1MGP30PYsobcIx_LNS9oBC80l0VhPAg87xqyQuSajQa5ltCfPERYL4Ya_I1VPsS77e-HdVCs2DrtBwoD4bQSruaN8EhhiuTQvbULEWmLMrx31UW-TYfH-ceIbSfFuT_OINL8YuUQ7CXia70VSNBaB54i0emdZvS-Z_infQiXnMCOjbE0f0VjR3bcki9A9uRBmcbShz6Lv4ivbm029i4QN7gg2doyGAMWCc4ZvaXXU3qUxblemcJTASwM2hxJ6nB1nBOttIPXQWblqG0j5EQa3Ywuv9Eb6Fqb4ol6ApKZtj1Fx-uS2XCAMg8sdTti9gbmuPDeRFgNYt8Dg_wceiSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یاد سربازان تیپ ۳۸۸ بمپور
💔
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/68188" target="_blank">📅 19:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68187">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پاساز علاءالدین خبری نیست، ویدیو های منتشر شده مربوط به‌ گذشته‌ست
#hjAly‌</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/68187" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68186">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh4N0EBDmiG-JAV0OEq_KfayGBaP06TQvm1SPKRV8MVswxjphf2cXlhMkzeS98X2wUzQ4mahOMbv4jfCrRozSCwGirCMNM4bScfdqUqoUerGFiWfovqFNGbk9bkBMzFbQSHJWYuadqDxWo9BhMngrePb4N-p9l1bfT6paMOHfhu2_bQ-5hbKurWw05w1G0BYok35nviWbMFqsUsthAK57j6L67zDrWo1N8vQExKCDhRs8xe4gUGSwWwGig9wusnPZEPDQ9QmLIOpRnewFUuTctxoIGEBDyUiIgnreL-_OqG2jPPmZ1884uatEf-faAUFaO5vOvO8K7dWd5U8B5YTfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:
❌
ادعا: رسانه‌های دولتی ایران مدعی هستند که نیروهای آمریکایی در تاریخ ۱۴ ژوئیه به یک انبار غیرنظامی گندم در هویزه حمله کرده‌اند. این ادعا نادرست است.
✔️
واقعیت: در تاریخ ۱۴ ژوئیه، نیروهای آمریکایی اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. در همین حال، ایران غیرنظامیان بی‌گناهی را که از این تنگه عبور می‌کنند و همچنین در کشورهای همسایه حوزه خلیج [فارس] حضور دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68186" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68185">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJoX7c25sQwohtcTZQoTraiexe6a4WQOOhezvZ6YaSZFGc7vgMWpY_IIiTzJM-nqjIPay1Eua7DJiqkAVe5s-1X4dRzSSA7Ly0F7EPtGXjB3ofymnJw4DFj7d8C5DYwY0zw0PIaxlGLWFdZH3kCnREoaBhOgVqMOzQ3yHCiyABcPjdoV7ixDGt6MGGJGhuyh9BqIEiS5-DbzjaUKQ2cjgJkVgSH52Rb4dg40Ezt7HZvfX09pjlSxi4FbARj7Jgwamr0XqiTcBnj3coPExBZgQLVgsuD8UZhX2ugVvy2MnosLGNCMcUZGVmWZNqQ4Pmho58GhPIfznyrX50B4tFQ8Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68185" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68184">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQiiFWkztY3GJ4Vb1Cch7uTY2I-bg4hX1COiYatJUyZvzD-KIQwncMhMnXILV3mjlHjq0afaZgHhXWWS4cfe-qw4dl8Gz_Pr765SjjSru803VSwGCnh5aelQQe9vOPR3RKd8N_PAnBEE8yHN3CCHxmBlevEsxqO-WA4OXQ15M9ABp4fC6fh1L177V10GJHurWPX5YPSxPHuyoLpzQXuBczBUF132sLSyMVq8VverZuFpipDog8X7YTT7tXC770rpetyVzw684xAPzIn92LhrxAArRWXJsSxmBAxHfri3S840ZRcw9zt8RtnGw5GJfuvRlQHsdK-2DS3UZa1cC0c9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره دریایی بنادر ایران در ۱۷ ساعت گذشته، نیروهای آمریکایی مسیر دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند. ارتش ایالات متحده همچنان هوشیار و آماده است تا از رعایت کامل مقررات اطمینان حاصل کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68184" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68183">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/68183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/68183" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68182">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPx0ViGZZIZkizW4DViI-r1yhxa6KBiTpk76jMZ0nxWSoBbCIyf3gACQYvbpzCAbQy380ZkMU8nGy6VDQmsEO0IvJrHZL45eSsdERQl6kTFp9s2ID1TyGcDxdEXwpfcwD7tjG5VeaXXNWV4DAH1ltLflzI6ZlKAxPLoKb7HbcjtvSUhlcvwELa8HmtBepG4B9ZphI475tQBsvQc-MQSxR97C4wn4feoGeM4ibTfbwwyUpjRAE8qK-Y8kyiPRjULQgvbWa_Sct2GbMayA45xpJ4sgfhHimoBQrzqUxW3709KxomttFQQSZhQusCA0Dn5eETHl_RyGB1ztGBoZKgG1Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
Stand for Victory |
مجموع کل جایزه  250,000€
🎁
جوایز برتر:
🥈
جای دوم — 33,000€
🥉
جای سوم — 20,000€
4️⃣
جای چهارم — 10,500€
5️⃣
جای پنجم — 8,000€
🏅
جایگاه 6 تا 10 — 4,000€ هر نفر
🎖
تا جایگاه 450 جایزه دریافت می‌کنند
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/68182" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68181">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
انفجار در جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68181" target="_blank">📅 18:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68180">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=JBQkU_3vNKltDUHr_RKcsNzVXUJgB9ZpupXYznyT7Yhjdem0X0duegDVwEbl_vDr8KwtHPX5utexDeiQ1PVmm0O0JqBNcA1ItUbP8-nyvxBMttXQ3Q7iUaMNtdxr4e3DEXFKP_utRdvbktaUQM0j6mBSudH0ieFtjg-o3O1WaE0QZEYSK1DcPVcTBF-uWJ7jATSEVu3BXJ51Dh_4DS0ZLurbel-RntGvO0ycL7B4HnMNnwLZWQXe_F9XgssZsJuoUFKad_yLy49psh5TDovTX2njbohF7QYSEZVBe36KpEncPh576zO-KISZ1lYmWqePX9pdBrG2oM9V3G4__6YY6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=JBQkU_3vNKltDUHr_RKcsNzVXUJgB9ZpupXYznyT7Yhjdem0X0duegDVwEbl_vDr8KwtHPX5utexDeiQ1PVmm0O0JqBNcA1ItUbP8-nyvxBMttXQ3Q7iUaMNtdxr4e3DEXFKP_utRdvbktaUQM0j6mBSudH0ieFtjg-o3O1WaE0QZEYSK1DcPVcTBF-uWJ7jATSEVu3BXJ51Dh_4DS0ZLurbel-RntGvO0ycL7B4HnMNnwLZWQXe_F9XgssZsJuoUFKad_yLy49psh5TDovTX2njbohF7QYSEZVBe36KpEncPh576zO-KISZ1lYmWqePX9pdBrG2oM9V3G4__6YY6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی وزیر خارجه اسبق جمهوری اسلامی کاملا جدی اومده گفته:
باید به پایگاه های آمریکا در منطقه حمله زمینی کنیم و صدتا اسیر بگیریم ازشون و بیاریم ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68180" target="_blank">📅 18:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68179">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=c-uTsU-WPI0tOl5U4RUllpgsQr2xXh3E5t1wrEVpX1xaHoIs74tRJ2pMusrfZKi_q6L0-nSD05ZRawYAbhDOgw9IGwJ4zlZFZ6iDEbM51hsuIl_F2Jkvr91HH96NDAX00aWxcKt2DVjff3HIUDdjNAi6sploGUz9Clt4HVigT5Fyg58jK2ZEngpLk-CbOH2k5qsflUoIfudonz-EMleDl4oB8KhVfMCa_7cqclrLBJSezmt1z_0-kQ0LR1hiD8q-RuIbz53yien37YgVmYkP70pNtp7UVzpUtbHEb1uNSHERmuVewVckrphjFH0drZIFffqeZK3fPFWA8qW2IuPdBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=c-uTsU-WPI0tOl5U4RUllpgsQr2xXh3E5t1wrEVpX1xaHoIs74tRJ2pMusrfZKi_q6L0-nSD05ZRawYAbhDOgw9IGwJ4zlZFZ6iDEbM51hsuIl_F2Jkvr91HH96NDAX00aWxcKt2DVjff3HIUDdjNAi6sploGUz9Clt4HVigT5Fyg58jK2ZEngpLk-CbOH2k5qsflUoIfudonz-EMleDl4oB8KhVfMCa_7cqclrLBJSezmt1z_0-kQ0LR1hiD8q-RuIbz53yien37YgVmYkP70pNtp7UVzpUtbHEb1uNSHERmuVewVckrphjFH0drZIFffqeZK3fPFWA8qW2IuPdBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمسخر لهستان و شوروی توسط چپ‌کش اعظم رونالد ریگان فقید:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68179" target="_blank">📅 17:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68178">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=eajqB25EjJmRSfrZ1uBbZ0hseEB1JE3l8KHutTBOKWNWHOVPg9d2xj_HJvV5YNCCjBLFhIob59IDH848aHaTHY9qcJKIAbVr4WDkAudk23Iz3Q-uOBD8xsusjjomaBbpe7Pt6ah4F74ZQtQg7EU68ouhfwogX1sOxbouwtE31E27oqpugX1m-JajP4tpe8IHRNVffoKqH6rLLOMU2EzLZrKhyMFCDMOy-NsOtLKZy4OjDca3m1k7oBg1So56v5399iqaRpJMsT8fmDJBO_PI39sxU_Mm45RCUYjYslaOPiT_NYe3Gam1luxkW4_xfa8bGG7GN97fDfAh5Fd9NAV-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=eajqB25EjJmRSfrZ1uBbZ0hseEB1JE3l8KHutTBOKWNWHOVPg9d2xj_HJvV5YNCCjBLFhIob59IDH848aHaTHY9qcJKIAbVr4WDkAudk23Iz3Q-uOBD8xsusjjomaBbpe7Pt6ah4F74ZQtQg7EU68ouhfwogX1sOxbouwtE31E27oqpugX1m-JajP4tpe8IHRNVffoKqH6rLLOMU2EzLZrKhyMFCDMOy-NsOtLKZy4OjDca3m1k7oBg1So56v5399iqaRpJMsT8fmDJBO_PI39sxU_Mm45RCUYjYslaOPiT_NYe3Gam1luxkW4_xfa8bGG7GN97fDfAh5Fd9NAV-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از وایرال‌ترین ویدیو ها در 24ساعت اخیر در توییتر فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68178" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68174">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reX_HdEnuXf3Un24NHzgo9X6ruzriFMWKEsa7QYNUMT0ysAw1R63l9qCF59jUDgssLahTtDCKNnIttmw8u_NgrGd0ULaPq3xEe-tk1q0fQ8vFb3716iZ9yQ6eYqReum5I1wZpDdTSDP6Nw6WzBmeN4LgAWKyd2Ku7y679XNveuxd6juBNIjyWoZZ0kRLeayWRLUCxJ3x7_0z7BosUFLLktV7QYP6E0ayGfUAEG2NlD0LjwDwTOZo_2oY_Ghl-cehM8YtwWK-V7IhenFZyU1eFwbY6EtQMXuIzN6ygXEMW_vgclUoS-yQeXconHbVa-e-dFT_GNP_Hzeme14MSbk9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=wAuTyie6caxrmKj457tUEvo6DmdyHhtHFos7Eo4yVf9TwVXSCMbEnU8Li8Q4qjxPf8s77X5qywfW4BPxDpj6BTuPqCFyhn5q8oNTNotHs5HujCmNrEHheJ8l8mH8s_DXWSu83LcGQTWoVsGmeEMXwSI3Fkii_hL-K5_aPIzj4ryQGRRQNJ2QiMyIyOq7L4sWufBpPlBNWqxO6FaSA-ZjqRCWlK5eIT1Bl62WErPstHpVSAHoFSiSQq7jeuBqnzGq8xO0pfmVKt-AXmwkfwiTc73ksciaGDz96ry0AsfvlkomJPnJeRm6JoTMsjPrzS2YeRdkOg9XzimKgVzZB121wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=wAuTyie6caxrmKj457tUEvo6DmdyHhtHFos7Eo4yVf9TwVXSCMbEnU8Li8Q4qjxPf8s77X5qywfW4BPxDpj6BTuPqCFyhn5q8oNTNotHs5HujCmNrEHheJ8l8mH8s_DXWSu83LcGQTWoVsGmeEMXwSI3Fkii_hL-K5_aPIzj4ryQGRRQNJ2QiMyIyOq7L4sWufBpPlBNWqxO6FaSA-ZjqRCWlK5eIT1Bl62WErPstHpVSAHoFSiSQq7jeuBqnzGq8xO0pfmVKt-AXmwkfwiTc73ksciaGDz96ry0AsfvlkomJPnJeRm6JoTMsjPrzS2YeRdkOg9XzimKgVzZB121wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی منتشر شده از انفجار در چابهار صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68174" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68173">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=N4lXkAEW7-4abtyWuo2Doca0JrqisR8H6O6aF8a0Mm1w2wkdRsYRLFzYHR4Cl32bBokf2QLkq8bYjy7NF0WEtjSKXODVVwF3HEnaV4goodS7P9t5JyKJyFRzfaF2LNQD-zZ23TDB3rE3lsxYmV_Tb7u9ZEeU5yfA2C6l9xlik6risOrLT-er9QBjo8tgBfc8zdg1YdmrhggKFZJAyGCfQKC7PFi9JGS0mu4xfxomJgoqt3jaO8EDA87CZXV6D4P_deola93FUfIVcDUImPFH8UvntnzJYRs7QQ2cHbCMFJN-KE8FYei-sHjBjQTztIePQP4MYDNpYkhiuJhNyFopRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=N4lXkAEW7-4abtyWuo2Doca0JrqisR8H6O6aF8a0Mm1w2wkdRsYRLFzYHR4Cl32bBokf2QLkq8bYjy7NF0WEtjSKXODVVwF3HEnaV4goodS7P9t5JyKJyFRzfaF2LNQD-zZ23TDB3rE3lsxYmV_Tb7u9ZEeU5yfA2C6l9xlik6risOrLT-er9QBjo8tgBfc8zdg1YdmrhggKFZJAyGCfQKC7PFi9JGS0mu4xfxomJgoqt3jaO8EDA87CZXV6D4P_deola93FUfIVcDUImPFH8UvntnzJYRs7QQ2cHbCMFJN-KE8FYei-sHjBjQTztIePQP4MYDNpYkhiuJhNyFopRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۷:۳۰ صبح به وقت شرقی روز ۱۵ ژوئیه، دور دیگری از حملات علیه ایران را به انجام رساند.
سنتکام در جریان این موج عملیاتی ۹۰ دقیقه‌ای، با استفاده از مهمات دقیق‌زن، سامانه‌های پدافند ساحلی و همچنین محل‌های نگهداری و سکوهای پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68173" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68172">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=jJybG_j8CZIMRmM95r6w7_AXS8H4fZZz7oprod7rvGQYHHp4FxZWztIl3xTEB11UU-buAWzrlLaCmrStBj337nPx0gK3OSe5Gi_g7mZtSU7Zzj_A64Vif4pGRZVbNwSpWORrz_eCi0PEN3Fn2vcc7w-kocDOeB752DYTizgX_YV8m7lpwfxQdo40IFkvUMLOGAZTTAOrRrZEMDc5nvRfvlBaZmCb4voz-H0iYHu8wrFOlb5aNlDRLl_r5pj9jFGPq9h3bUMcbjtAr1M5Ye8nGN0Mlt61CiDThGvV5jzboOSu_sFls736oZGKZyzNlJcksVtnqx1bgPnIrJQfL3sZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=jJybG_j8CZIMRmM95r6w7_AXS8H4fZZz7oprod7rvGQYHHp4FxZWztIl3xTEB11UU-buAWzrlLaCmrStBj337nPx0gK3OSe5Gi_g7mZtSU7Zzj_A64Vif4pGRZVbNwSpWORrz_eCi0PEN3Fn2vcc7w-kocDOeB752DYTizgX_YV8m7lpwfxQdo40IFkvUMLOGAZTTAOrRrZEMDc5nvRfvlBaZmCb4voz-H0iYHu8wrFOlb5aNlDRLl_r5pj9jFGPq9h3bUMcbjtAr1M5Ye8nGN0Mlt61CiDThGvV5jzboOSu_sFls736oZGKZyzNlJcksVtnqx1bgPnIrJQfL3sZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جنایت ۱۸ و ۱۹ دی ماه؛
تا مدرسه میناب و پادگان بمپور؛
نام‌ها عوض می‌شوند
اما قاتل یکی‌ست:
جمهوری اسلامی؛
حکومتی که برای ماندن؛
ایران را می‌سوزاند
و جوانانش را قربانی می‌کند.
#hjAly‌
@News_Hut
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68172" target="_blank">📅 15:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68171">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH2YB2xHWxPkLmVM5QmmIqa9C0SUNHL5X9GPnC4_A01lE8ccI5iOqnrfXyoYwjZy0TeAqDUW89PApUftrKvP9iyM6prqZVBa_gULQvvRshlogE7kHVlv6_pC10ztL0efZNKq3V8KI1MJFBM5nI9jCOrlVcu89CtK6w0uZT6LqexBENaWk49SHLzFkLaX-cv4B46jpcs5oPsBLDPS4BvN7n9BBx1kmCQ9TcwgnAwV6s1wDe7lxu4_krXeWNzwoidHvKlGa7K_Pq7twzNmMe73oI83d2l-AfxXF5SnbH9VSUioEQ_Hw6twq0uCWT2yJ7NRqN_mQdaatR0bHQBkvNxyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری حامد‌لک:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68171" target="_blank">📅 15:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68170">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9X-czq37V2TTSOYic44sVS16_l0-200VEJF7diyHqlcSEiOMMGrcsHKEEVwbWbVQo9Zv13Ej7QdkY5xFk1MXlTiqaXxDZiiGfmvuCvQUpQe8pxnJDRnwy0z6cw_yLqBCWETR7W-Iolw2nFUnRaGTBYEJsFY7eHXnwBTO96mQsU8QZR7uYz0HZviIdUvYaHfzj0xVTGugaiBRZxWoLouW97gCsMQb6dVC06z8y5XXHRvNmjHhbvD2Vttxufxkyf9AJvFm_xLz9y5SoIPGO4IlZPMVjGh7actWM2PS_XyQJM9LLWlkRt-8xxUSRsy0ul09YdRWYuKXBMlJbh9yxMsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چهارشنبه ۲۴ تیر ۱۴۰۵ جام جهانی ۲۰۲۶ مرحله نیمه‌نهایی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس - آرژانتین
🇦🇷
ساعت ۲۲:۳۰
ورزشگاه؛ مرسدس بنز آتلانتا
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68170" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68169">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
پنج انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68169" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mob3k5bTCFsYS5Lw6jMlkYTV6BkVwbphH5EpTBWgk-b4FGqv1okbsDBGonMdia6sbs97Xb3Je-Z3KR6njnPU4D5eVlbtHFY_f0sBAcTmr60mcBiTdfy5_sFa7LMwUl3XgzZKBrchtGcTwUcVV5WpEwAUNnra-MeNM9-0StHsfm8dHOtxTwX7w13A94GZa8Cmvq4NXNF99eBVhySHgz50uPzuUYZGBCr05kd5KDdKyPfHokgy7j14RXjGWccxKChn4JSSoVkjkijq13vDq386TNNvRcZkzYDqI4EwSFsBxrIFdGOU4idXjdJFvlm02rUAbYkhNMMRL4x5vDHBrgYd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=gzfBSuBd8qCsD1gm6qjFONEVJ12y7zrp7ruBtSzsfJ3QIos9Yi9KiBpEyxNnuoGEeY-AV044HtlVHEh7Ak59v_1O7QYPtwGejaH7KuRtPb8wLwI6foW3MZAMtSi7lb2IZdqEAW0hT4-yVWprhtwxzPcdLiisFiJkNCVvrPoX81DVulnY-aMjfOGVw3zThs-JmyN5PAQd63LGdyBY174oJuovU2n8n7kMXBXr6_sVlykLVGYcE9JeC6VwSkGFFSOlpvpd_onfAtn3f8d8etbS82E-VM1f8ksrMmJrcUiEV-P6D9KBZ-dFQVH8wBhoOsLjVij7GJZNILzehi3tZ7Qhjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=gzfBSuBd8qCsD1gm6qjFONEVJ12y7zrp7ruBtSzsfJ3QIos9Yi9KiBpEyxNnuoGEeY-AV044HtlVHEh7Ak59v_1O7QYPtwGejaH7KuRtPb8wLwI6foW3MZAMtSi7lb2IZdqEAW0hT4-yVWprhtwxzPcdLiisFiJkNCVvrPoX81DVulnY-aMjfOGVw3zThs-JmyN5PAQd63LGdyBY174oJuovU2n8n7kMXBXr6_sVlykLVGYcE9JeC6VwSkGFFSOlpvpd_onfAtn3f8d8etbS82E-VM1f8ksrMmJrcUiEV-P6D9KBZ-dFQVH8wBhoOsLjVij7GJZNILzehi3tZ7Qhjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTREpeG0WWP1u_9yHIJyRZ8bnr_v8JluCYPU5_Q1lw_CZHkaH10aTqy5yl5df8DyChhY2HrRIq22TlEE0tvdXB3PWS4NsThBv72xvf1HkCs7WT0w5R-A4co8ja0vYFMvf8Vb2tKaKGcXQ3dInkk2GnZSUUm0_TOZrcR_nB7cw4uPc7vgDO0Rn_hg0aVebKoV1JV-zNHlgSn1eMVTrFDZYeZ0UZkQZRSbyijCOpv9AzqcCrZmL6TTaycIlYtVvhr45H9EinAvNIpxhc9MMh3OXldd9UPaw0xrTRRF2CKRY8EaBLoVN608fO-MLzkC6QjQz8IaEHtBZ-lEcPlYEidDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5ulyIA5lgEjKoVDcgr42_Z8UHT8ZC9JOBYKfYRC8cZs1Mjgr8fMVilKXmLsniOXMdySzOiAS5qmaiIhN63P7eV8kIsE_gLahIjdp2yXGW07XlZOWMhTTPg-IHQl5WTQ9ifidtNJuAqRORwPfQuwtuE8b1EGNi-iL_gmm7OkmUMesn5snSEgjvTlGbCNgEYoHMrTbGBfJrBPnCwEZrobIO1dWjXTbxkhhdLbxoomUo0fY3doOWTPviVW_ddqAmMi2rVq3uIREBrIWq2EQlP00zzfpbcGEPKXQ2o_FiBzG0l5XFc8Q3c1vbxBZmzHTY84eniRMStSCRnUGd1DOMoqww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJzqMGjZ3DKceddNOpsIcHj19nXt3GtHb8Hugm8kRak0l1wXC8SJu07H5vI94WyW-BWbTGB1qFgO7g8-nuv0taC447w1mRTCqxLrLp14dsXcFrSwh7XPNll4F2j1tYuLXglul_cmhd9y9xSYDu5JXrqlU-bbjN6mlsUb12zHYNVRdu4tV41qO5pGrLnB1YH4-w2ujucAapjuJNxP6WRVLJUBPxBV5H4fj_MnDfnHW8lp0jeNdNO5d3qO90zvVQHOW3pRDknCt-qjsauEOn15RI1kUs_6wCgmkP3LVd2fgAP_DqGBnxvexHnmzWc0f4WYO5NQ4zUSdshksum_wtwYfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=qmuglpwepclI_3JhYCaTIMGPcCVPbc7KxpKOjJJSTNezzfFCftgktFwmqa1POlpYn_C0Fa7L9fX-XwizjLX5_sYJiWxNZq3XBc5nDqPoufy70PGjtbhO6qZ1TPDq7NwOwB2RheF-3DKSn9zBcju0tG8KsV5gLrmBSCpC9XAMkOEPMlm7PhEXiZ8sRJE3jhMm_tVQMCYFD8MvX9jh2gIRiEOkwRUP3HcKChd5jY69JhW8iQi1Nc20V54blbeObEqLYD5RpG6XbwCJcvK_R3WmeVAr-RzTwCQ_jZaC3XADDRV5cC3ku0fZdzFbAIiqs_cWohF9Ml9nVC0_rmXJTiS3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=qmuglpwepclI_3JhYCaTIMGPcCVPbc7KxpKOjJJSTNezzfFCftgktFwmqa1POlpYn_C0Fa7L9fX-XwizjLX5_sYJiWxNZq3XBc5nDqPoufy70PGjtbhO6qZ1TPDq7NwOwB2RheF-3DKSn9zBcju0tG8KsV5gLrmBSCpC9XAMkOEPMlm7PhEXiZ8sRJE3jhMm_tVQMCYFD8MvX9jh2gIRiEOkwRUP3HcKChd5jY69JhW8iQi1Nc20V54blbeObEqLYD5RpG6XbwCJcvK_R3WmeVAr-RzTwCQ_jZaC3XADDRV5cC3ku0fZdzFbAIiqs_cWohF9Ml9nVC0_rmXJTiS3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68159">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCWyj4vwB5cQWO8ajtMlctZ-uDcWRF2CijQNgx0UGIaEukxU0YqqalPeVpHWtRv6GDseux-3232CSezLyhc6tztGbF2Vukq5cJNOHrAdkNuuo5D97hbnvIC5MqkORwhECQUeCTzOq13uRb1WBS1NK3E8Pz3-lNWBO-QS50IHttZqtgOts-obeTAgR37FZcmagVFqoPVpM4ijnZCGOYmiKZ1HDXbl_RzlJyJWSXW01WIWebKJE5lGGcJbmzBxAFre7YVFnaiBy4RX42Qh8Jo2suxq2I3OvSIhoxGX13fdsE9-8NZc_aHNQhExDd38swjrtVGe6VzX7L2wvCi-xjrZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68159" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68158">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSb6YbkDsdjsf2xE6FyrG54zwlSnCPYREhjz-fdJWdRPJDmYgyv9WOsCKCd_gFQ770U75nLd3WLtDQHsz5Ve8aGi0rt9DxWtF99o-YqVmuIzpUtGX5e_Ql4rPSXQFqw7xigekGtuJ_HmFgor9mUeYrK1yLXs9VGNT1X4rxzKENXPdvEkrZirNHPkHa7KrmAauZo1a4Lk888E1CEppoCtXVhjjhXwqZAkUaVrcvJvDKeUfN4CDvefzgjiSd1MEQWsoQtleCwDdJvvVqDyAGjy_P3XQl9tMdmNL19TzNDgXIgmUQ0ELAvBIvQNdjp7OGf8-SyYpskqTF7Raaa6fkhFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرِ داریوش فرضیایی (عمو پورنگ)، بعد از تحمل یه دوره بیماری، تو سن 90 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68158" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68157">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
امریکن گات تلنت یا همون عصر جدید آمریکایی ها
یک شعبده بازی توش انجام شده که حسابی وایرال ‌شده
👀
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68157" target="_blank">📅 12:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68156">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUycoNi1XiH2PJW-FETCaRowVvaTZkXcLvnXpR2Xs6n-RbumbHVhJ1_K1TSwhcW0IXdk-CDL7M7KQsFPwZRehs4NrRFKXlDtMzafyaySMGeZ_s602U2X8B_tHoZvjd0D1LA-yGP_xJZ33eQCR-k6aaN3nlp2-8NDBJhP6nKL5Z4FGWGcIdQh2wj6AntTnkA9HjqSNHNNgcFgKLdAXGfJyKq1Gipjhjy15Oab_dM8j0-JHgu-Cqzm5fxUVs12IS0Ms12mJCVswwkf-KfazcRcTfBo6W5KEMYPD8Z1CJ5PvT0CeSi1p1-1VRu04xleiF6SQmEpM4eKigFL_PiI3mTA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ا
کسیوس:ترامپ در «اتاق وضعیت» جلسه‌ای درباره حملات جدید و گسترده علیه ایران برگزار کرد.
به گفته سه منبع آگاه، رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای را در «اتاق وضعیت» (Situation Room) برگزار کرد تا درباره یک عملیات تهاجمی گسترده علیه ایران گفتگو کند؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
به نظر می‌رسد ترامپ مایل است جنگ را تا حدی تشدید کند که خسارات کافی به بار آید و در نتیجه، حکومت ایران تنگه هرمز را باز کرده و خواسته‌های هسته‌ای ترامپ را بپذیرد.
ترامپ این نشست را در حالی برگزار کرد که ارتش آمریکا برای چهارمین روز پیاپی، حملاتی را در منطقه تنگه هرمز و در امتداد سواحل جنوبی ایران انجام می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68156" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=Fa2TVgepk4k9bKciLZRdGcr9X3xoAu74Eyx16eq5P_J2ntj56mvDOD68z04vEoMigiTxmIhaiCfsytfEAMai1_roTznuF7LD1IUoHm-Ox85Kxe5wEwQ98okBx_i9Ek-APVVJ36qJvfk5A-3I6OkHyfp_dfzigSmqgVKuRkzQ3J_cBReelqPN70gboCGuJ_FU5-dTHbiTN1ezbxjrAujNfi6pJqJIfdhi_w_RDPz0kFr6j86jlf-pgdyHpDsXWfSEfRyc_DyorN3l-GvAHHuu4Tf8rIW6UESkufbdlOFjZpFVwE_2nRsW9NMtSIuHxZdBygZqr3hWBEhMJ1aTd5Bd5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=Fa2TVgepk4k9bKciLZRdGcr9X3xoAu74Eyx16eq5P_J2ntj56mvDOD68z04vEoMigiTxmIhaiCfsytfEAMai1_roTznuF7LD1IUoHm-Ox85Kxe5wEwQ98okBx_i9Ek-APVVJ36qJvfk5A-3I6OkHyfp_dfzigSmqgVKuRkzQ3J_cBReelqPN70gboCGuJ_FU5-dTHbiTN1ezbxjrAujNfi6pJqJIfdhi_w_RDPz0kFr6j86jlf-pgdyHpDsXWfSEfRyc_DyorN3l-GvAHHuu4Tf8rIW6UESkufbdlOFjZpFVwE_2nRsW9NMtSIuHxZdBygZqr3hWBEhMJ1aTd5Bd5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه برخورد پهپادشاهد ، به طور مستقیم به یک انبار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68154" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68153">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7d5NzAn5RiTW270I31OVwYr_qafwUKAwedclvH1Km2QtQbJJ5C5SCKKr7pMOKKsAFM9ivaKFv57yK8avtvj4JxPlX8YnEaet9p60KL2kr0iWpO-jT6qTpSzPivRqqY39lue8TczY853PzwgoSrCHRCaSdDa-8KXOCyRpZN2RZ2fF9AHEULTctEqbGL1LLu_PkGwpny9sgyP4iR-kewEiEENURzdXtEtj6aPAowf2UtxMXUlT58o2Ovkf5tqCn5GKeYULnyxnz8xbMsIZYj4m_gb-yIyL9iAPqLrdy588P-41rjt6qHYuHdhliIy8ireQ_mtjUfG5R1dyO-URTCteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:
#hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68153" target="_blank">📅 10:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68152">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=UpbnVsr3-9iZPvbFpNTlC2jXb6x4EIVHevgha63hdCDdCMAfz9AHBcMKbWJrk4dA8EsrToOC77-QcrJLAQ7l0NzfpsqQoPQFQAR8bOl3b7j7tG43O8-gaOYlH4m6ALpCfKnlBGrgwuTGse5J4f-dvwe9qGxQAtKDUQxoGY-1s5b7wiDeB2EaoV5tH17RT_BwHuiJO19Clfi2Zlj8I8ZBTdVwzDSWJwgpciAz0ZK6lY7N4p2yELXmA2nBLOKvSktXpqVERHg9IIa9UX_-uMVLnXZxYQd-wwr3mIl5VP0PjQEoNl787uAsJCm-2MUN_yvf9Hp8diU0VInbPN276pv57GaO3-QYHx5yC-lquL6C-GejEhA9AvoJ9eXgxC2whSbm9pdXCfYn2ACsicIkGFwf0ZidVSO4IDvHBzzPK5lvp-7IoSFM1BOCUhq_RF3bN3mJ5ZrHoIeyo7fb6Cpa6coDld_Lz_8JkMBE8bpFiREIthUpnNtt30cfKeDzLxUQXfmbivDPcfvR2IUfRLua03JZCd3rzgtz33WoJNFHfU4-O4Va26KeYs1z7ZtDryo7dRLNMKRFJEWTbqEZC8koM8s60kUrcnFe7NK6y0Rg1wZFKgeOf2NQI8FqdVzG3xYTq0pTow7fU81bAZoG7nKoUqx8GgnCYisgYznfMOAjKFWOiO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=UpbnVsr3-9iZPvbFpNTlC2jXb6x4EIVHevgha63hdCDdCMAfz9AHBcMKbWJrk4dA8EsrToOC77-QcrJLAQ7l0NzfpsqQoPQFQAR8bOl3b7j7tG43O8-gaOYlH4m6ALpCfKnlBGrgwuTGse5J4f-dvwe9qGxQAtKDUQxoGY-1s5b7wiDeB2EaoV5tH17RT_BwHuiJO19Clfi2Zlj8I8ZBTdVwzDSWJwgpciAz0ZK6lY7N4p2yELXmA2nBLOKvSktXpqVERHg9IIa9UX_-uMVLnXZxYQd-wwr3mIl5VP0PjQEoNl787uAsJCm-2MUN_yvf9Hp8diU0VInbPN276pv57GaO3-QYHx5yC-lquL6C-GejEhA9AvoJ9eXgxC2whSbm9pdXCfYn2ACsicIkGFwf0ZidVSO4IDvHBzzPK5lvp-7IoSFM1BOCUhq_RF3bN3mJ5ZrHoIeyo7fb6Cpa6coDld_Lz_8JkMBE8bpFiREIthUpnNtt30cfKeDzLxUQXfmbivDPcfvR2IUfRLua03JZCd3rzgtz33WoJNFHfU4-O4Va26KeYs1z7ZtDryo7dRLNMKRFJEWTbqEZC8koM8s60kUrcnFe7NK6y0Rg1wZFKgeOf2NQI8FqdVzG3xYTq0pTow7fU81bAZoG7nKoUqx8GgnCYisgYznfMOAjKFWOiO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوندها عُمر طولانی دارند و بیشتر از عمر متوسط ایرانیان زندگی می‌کنند:
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68152" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68151">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1084df804.mp4?token=Q1BGC3O5EmxISNXLm56qBHbz0sgVMyKmW8Pfzaw1TgLiNKWWptbSNfB-RNeSE2kogBcwwbdItabXHwDd8uF-zOC7siNLVHvU6Y6-fePt5OIpZGnghf_Ud-yskwchsdlfymwZH2cNlvmWY1FCj3u192XpO3ab8qn6L9XGsFuqvYeG2k8KplfI7jDGbEpfHAvc3lpQuIyn61L0e0wN-uT_MXL3e2M-MS69epuz8-HXcu10OoyrparSmbFh-EDb1MdN1mIy0n8qaganoNm-N57qxUZ967bDrYUY2EB1IWSpLQoBpjvIEOHjyYezvhNMYL6ENwzxGTdc5Z9oIakMqkF0fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1084df804.mp4?token=Q1BGC3O5EmxISNXLm56qBHbz0sgVMyKmW8Pfzaw1TgLiNKWWptbSNfB-RNeSE2kogBcwwbdItabXHwDd8uF-zOC7siNLVHvU6Y6-fePt5OIpZGnghf_Ud-yskwchsdlfymwZH2cNlvmWY1FCj3u192XpO3ab8qn6L9XGsFuqvYeG2k8KplfI7jDGbEpfHAvc3lpQuIyn61L0e0wN-uT_MXL3e2M-MS69epuz8-HXcu10OoyrparSmbFh-EDb1MdN1mIy0n8qaganoNm-N57qxUZ967bDrYUY2EB1IWSpLQoBpjvIEOHjyYezvhNMYL6ENwzxGTdc5Z9oIakMqkF0fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیش‌بینی پروفسور جیانگ از تهاجم زمینی به ایران
:
پروفسور «جیانگ» تحلیل‌گر سیاسی مشهور در گفتگو با «پیرز مورگان»، مجری معروف انگلیسی، پیش‌بینی می‌کند که «نیروهای زمینی» آمریکایی از اوایل ماه دسامبر در ایران مستقر خواهند شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68151" target="_blank">📅 10:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68150">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFL_i-KCdwy_0gVCZir_Od9XXtO-DbtRwhCX3F5qiTRJjkq2o9kv0735iTcUqDWO9YiYu4aNLToI279P215vPXfvgdlqf-zm_DXlRYPTtCdTViwdYYMPLnLyb7avTfqBPbct9Pf9ZkJ7_RhQNbNYwIVYrUT7iogC7FNApng0IVIIaktkohyEIs4nfgAfP9kqF9pwNi1wJOIr79hEOMfZMOM6lmJredXE-khsPPmKDltps0vXoqPoi0k1jgDA8M3k9ZVyK8wVeFo2WyP-WCFYQQiebKQk2P8sTvmtHiLVIjYXszG0fm5JNuXMxIkbX0DcQaETcnmvn14AihVgL41LBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ: کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
کلنگ گزلا (یا کوه کلنگ) در استان اصفهان و در نزدیکی شهرستان نطنز واقع شده است.
روزنامه تلگراف پیشتر گزارش داده بود که تأسیسات تازه‌ای در مجاورت کارخانه هسته‌ای نطنز احداث شده است.
این مجموعه در عمق ۱۴۰ متری زمین و در دل کوهی به ارتفاع حدود ۱۶۰۰ متر، موسوم به کوه کلنگ گزلا یا همان کوه کلنگ قرار .
ارتفاع این کوه تقریباً دو برابر کوهی است که سایت هسته‌ای فردو در آن ساخته شده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68150" target="_blank">📅 09:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68149">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=DVLHCT_R4pZW8iWbVD8xNhMf7Q12We0-INHhaedB5Tuu6_0Fl89N86PeOFF3ZuazAMStSnmKoC-jYDu7fGmI4kCS0mowUhfxY9GPvPAKkJUZyG1CKUQeHBqnWS8mWAvV695m5D33ZZsHNZ5MZzjHvsDnVttJXrBmuRLQHz3lzn9tFawzjknh1mmNPBZkx7ftiHM3y2YqUKaQoMfjYbUWIYTUlBA_vFXyBVcDr1HWBELAeo-qq03RbUs7TFewbg8OPZ0RHjSkkAqNrjXRUyO8RbRiVTYRlqLpPZBkSJ7-2tm5XoULjp1kYhLKNjLZFKWSGoMEpT-uoFL5whUREf76uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=DVLHCT_R4pZW8iWbVD8xNhMf7Q12We0-INHhaedB5Tuu6_0Fl89N86PeOFF3ZuazAMStSnmKoC-jYDu7fGmI4kCS0mowUhfxY9GPvPAKkJUZyG1CKUQeHBqnWS8mWAvV695m5D33ZZsHNZ5MZzjHvsDnVttJXrBmuRLQHz3lzn9tFawzjknh1mmNPBZkx7ftiHM3y2YqUKaQoMfjYbUWIYTUlBA_vFXyBVcDr1HWBELAeo-qq03RbUs7TFewbg8OPZ0RHjSkkAqNrjXRUyO8RbRiVTYRlqLpPZBkSJ7-2tm5XoULjp1kYhLKNjLZFKWSGoMEpT-uoFL5whUREf76uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه حال‌وش: شدت انفجار به قدری شدید بوده که در لحظه اول حداقل ۱۰ نفر کشته شده است  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68149" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68148">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68148" target="_blank">📅 03:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68147">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68147" target="_blank">📅 03:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68146">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68146" target="_blank">📅 03:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68144">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=gIr3DT7l8mKcD4pOkQHUMKS7I1zt6XXuLbSHEqFCWBCSDIBXUlWF0y0rpL1pFdte1wuOIpHrBdK8YduSoqUuxfkRves14v7HJKpe8lID5pEfjDWqfxstg6ncobhDARcU5JqJ7R2bBMvzjwdclWMOZ24d9wCalSge6d_yfhVQ5AKExfbHBF22rQBWWPgU7cqfai5Z_l642XmizVxJeddl4pA7SIXPM8MBNK0EfsDdockPvUH-2cAHBpBAyDrfb3DlH8bYwhL1kT8e3AD6341CwwTNXaHl0k7esvzEEfpAvdPN_WUmdiT0_fIiq6WJ1PTYTO2P02I8QmbnANpyAogqZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=gIr3DT7l8mKcD4pOkQHUMKS7I1zt6XXuLbSHEqFCWBCSDIBXUlWF0y0rpL1pFdte1wuOIpHrBdK8YduSoqUuxfkRves14v7HJKpe8lID5pEfjDWqfxstg6ncobhDARcU5JqJ7R2bBMvzjwdclWMOZ24d9wCalSge6d_yfhVQ5AKExfbHBF22rQBWWPgU7cqfai5Z_l642XmizVxJeddl4pA7SIXPM8MBNK0EfsDdockPvUH-2cAHBpBAyDrfb3DlH8bYwhL1kT8e3AD6341CwwTNXaHl0k7esvzEEfpAvdPN_WUmdiT0_fIiq6WJ1PTYTO2P02I8QmbnANpyAogqZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68144" target="_blank">📅 02:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68143">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حرفای امشب ترامپ رو گوش کردم، یجا گفت فعلا نمی‌خوام باهاشون مذاکره کنم، تهش گفت اگه تا هفته بعد نیان برا مذاکره پل و نیروگاه‌هاشونو می‌زنیم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68143" target="_blank">📅 02:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68142">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از تبریز دارن اردن رو می‌زنن، جالبه از پایتخت اردن تا مرز اسرائیل فقط ۵۰ کیلومتره، ببینید آخوندِ گنده‌گوز که ۵۰ ساله می‌گه اسرائیلو نابود می‌کنیم، امشب جرئت نداره ۵۰ کیلومتر موشکش رو اونور تر بزنه :))))
#hjAly‌</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68142" target="_blank">📅 02:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68141">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=MHEcUmOHZy5qZJHshAL1WCUrShmopCmfyZBvNEKgJ0m4Qk9futuin7Un2qEF200C46RTMRakp5VywjcriG3PaA7089tDff98dnCWsc21UFQ2vQt5LG769gjYuoNxmfrtq-PJLTmN2xDvnp8z8iEP5HMijURLwFjmlspyujHwxBL-lwCqXUU6MmSUCkz4bTXrloRmsj9O2zByfYhcgbvcA6Jag69USaGYbruVGVSZJbiPV-2RLilwaKhamWz10qG4L2n0S-jJHUbUzCCaie3bIOjUhFwZCoDE6bhqqqJJP7WgKJz-dFGMUYRv7OI2mk3VQ2_tCOjixQ2hndJDM0qNDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=MHEcUmOHZy5qZJHshAL1WCUrShmopCmfyZBvNEKgJ0m4Qk9futuin7Un2qEF200C46RTMRakp5VywjcriG3PaA7089tDff98dnCWsc21UFQ2vQt5LG769gjYuoNxmfrtq-PJLTmN2xDvnp8z8iEP5HMijURLwFjmlspyujHwxBL-lwCqXUU6MmSUCkz4bTXrloRmsj9O2zByfYhcgbvcA6Jag69USaGYbruVGVSZJbiPV-2RLilwaKhamWz10qG4L2n0S-jJHUbUzCCaie3bIOjUhFwZCoDE6bhqqqJJP7WgKJz-dFGMUYRv7OI2mk3VQ2_tCOjixQ2hndJDM0qNDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68141" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68140">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=RvyEdQ-viOmEBmE411gLjTNlzB9g0adYmmFP8RNuno7t2LUMv9boixiHHYnyuYAVOUd09IhvhewaA0iPXnF3I3TLlOPr5-xq-08h4P3vLDoXOd3AbA3VqM2KneK4gQuN5iRjRT_Ae3VSB6Lz23Vw92rAFowkvMkxOBhxArhlCkOGwt4uO1bTMcZ-I-MymZEmg7FI6oj1r1VIw60dBFYNKzFzAdpVIu0yf-4F9TgrGOaag_b5VHf2zsimJ-tnrIgjkqc8uUcMJMaHlS2MyyCwHSBOoaybS9vxWMvghP3kaa-IoiepyjFtWhtg2CYaU3-9K5LjXQQlsm1kFXKrri_vAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=RvyEdQ-viOmEBmE411gLjTNlzB9g0adYmmFP8RNuno7t2LUMv9boixiHHYnyuYAVOUd09IhvhewaA0iPXnF3I3TLlOPr5-xq-08h4P3vLDoXOd3AbA3VqM2KneK4gQuN5iRjRT_Ae3VSB6Lz23Vw92rAFowkvMkxOBhxArhlCkOGwt4uO1bTMcZ-I-MymZEmg7FI6oj1r1VIw60dBFYNKzFzAdpVIu0yf-4F9TgrGOaag_b5VHf2zsimJ-tnrIgjkqc8uUcMJMaHlS2MyyCwHSBOoaybS9vxWMvghP3kaa-IoiepyjFtWhtg2CYaU3-9K5LjXQQlsm1kFXKrri_vAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای دیگر از شلیک موشک‌های سپاه به سمت پایگاه های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68140" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68139">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=K-TA_GNmNleThsKfK98GuHkRudOWdNcT0vQ_Qx4r174RSG82-4ewfEDoqgRzlnKiG_YAk5LfO8dLaMpDpEdqjTiP3V9QI-aXKkwry7Ny4-JgsrqG78grrWoajF9UKzsSnV8gW2zHgLcZekS48i-LySP0WmQ7qGfUgo-mC8UJVeJ3MfBPyKp8SHIN-zs1GuONTah-Ff5lc580qcCsu5-mm15ETJZVYEA5mHfnHBmEuuYxMgsurcwSZol68AVqqqqzFk3WLz5hbS8i-wqvapN_XSbBFCk872zWczacjbKBLrQ8y0KWIEpVkqTRxJy5CNKzY21N7gyiVp75K8gB5ykBBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=K-TA_GNmNleThsKfK98GuHkRudOWdNcT0vQ_Qx4r174RSG82-4ewfEDoqgRzlnKiG_YAk5LfO8dLaMpDpEdqjTiP3V9QI-aXKkwry7Ny4-JgsrqG78grrWoajF9UKzsSnV8gW2zHgLcZekS48i-LySP0WmQ7qGfUgo-mC8UJVeJ3MfBPyKp8SHIN-zs1GuONTah-Ff5lc580qcCsu5-mm15ETJZVYEA5mHfnHBmEuuYxMgsurcwSZol68AVqqqqzFk3WLz5hbS8i-wqvapN_XSbBFCk872zWczacjbKBLrQ8y0KWIEpVkqTRxJy5CNKzY21N7gyiVp75K8gB5ykBBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68139" target="_blank">📅 02:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68138">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
💪
گزارش های اولیه از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68138" target="_blank">📅 02:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68137">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=Ngb6_pG9gjvzAhDEi0Gq9zXL4nlT4mkXNutmNoQcZO_Iymlv--qwhZWjpd68zyuKxQ3AzUiyqT1Zey6JvjpPqITBQJzvpORMys0Rk9A3kXtfmJGZceRa8wxytk8Fkrl4uPXwc5_DQjIyWl9UX-P-2wwdhRYeSZlWB3whpKIjhSAHOCc16GaRzAR8v9sK7e0PanP9xrIxgbS1Y_i83u6D7j5AVPQijVFWSmZ792NeGE1IHuwLOYSvAFFrSy5GIMIDW8Npx00MomyJtwsuIrqtYM3uhUiAn8tYOrPQPWSY1HOPUI7jt7M1XZuZbMhm6ZWlx1iFGsju7MAU5-IknIx9vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=Ngb6_pG9gjvzAhDEi0Gq9zXL4nlT4mkXNutmNoQcZO_Iymlv--qwhZWjpd68zyuKxQ3AzUiyqT1Zey6JvjpPqITBQJzvpORMys0Rk9A3kXtfmJGZceRa8wxytk8Fkrl4uPXwc5_DQjIyWl9UX-P-2wwdhRYeSZlWB3whpKIjhSAHOCc16GaRzAR8v9sK7e0PanP9xrIxgbS1Y_i83u6D7j5AVPQijVFWSmZ792NeGE1IHuwLOYSvAFFrSy5GIMIDW8Npx00MomyJtwsuIrqtYM3uhUiAn8tYOrPQPWSY1HOPUI7jt7M1XZuZbMhm6ZWlx1iFGsju7MAU5-IknIx9vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا همچنان قصد دارید جزیره خارگ را تصرف کنید؟
⏺
ترامپ:
خب، نمی‌توانم چنین چیزی به شما بگویم، چون اگر بگویم حماقت است. اما کار جالبی می‌شد و کمی هم خبرساز می‌شد.
⏺
مجری:
آیا احتمال عملیات زمینی را رد می‌کنید؟
⏺
ترامپ:
می‌گویم نه؛ البته اگر شرایط اقتضا کند [رد نمی‌کنم]. گاهی اوقات به عملیات زمینی نیاز است، اما ما افراد دیگری را داریم که عملیات زمینی را برایمان انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68137" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68136">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=YMhnyofurJnfbJrY-EIuWxeklkIxOIr4WlqgWc_X_82lE6z_KZDfdZ2p0m3gT-a11MUXbN1AWhoZw5ZE8iG2Fxww9z1Jf-LYyGo0lhwqgl10oqKuJKGNxWk5hQio64SaBoc1YsOfQLYnN_w0mC8ALdZzIzQjrDQbLoWdas5_TilzZ2HNERA-C_ofVGkuGBi8jirJ4wwC7fdfGIkBhDcql5nOZi_cicMYIvYnpzaIGx5zVNOTwfG7Mo-8UBHi7v202QxLmenpc2ZzVQlr35gVG488DCjTTw79ILAPFXgyQjgsdYg2jQITxrPkfTl-7P2-vsweDLnRgBFlbHBDoI828Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=YMhnyofurJnfbJrY-EIuWxeklkIxOIr4WlqgWc_X_82lE6z_KZDfdZ2p0m3gT-a11MUXbN1AWhoZw5ZE8iG2Fxww9z1Jf-LYyGo0lhwqgl10oqKuJKGNxWk5hQio64SaBoc1YsOfQLYnN_w0mC8ALdZzIzQjrDQbLoWdas5_TilzZ2HNERA-C_ofVGkuGBi8jirJ4wwC7fdfGIkBhDcql5nOZi_cicMYIvYnpzaIGx5zVNOTwfG7Mo-8UBHi7v202QxLmenpc2ZzVQlr35gVG488DCjTTw79ILAPFXgyQjgsdYg2jQITxrPkfTl-7P2-vsweDLnRgBFlbHBDoI828Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم. ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند. اگر آن‌ها کوچک‌ترین حرکتی انجام دهند، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشد را انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68136" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68135">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=ASZg6F4SCn0zdxOPZx69lWBKjC1JDUdMRo7DOORY8vFJxzvR4iwpVgPyofRiAFZ5Mz0-Tz_8hQt50VYBFHFH94xOmmSfBLlxy37T0KPtSTrP0T-hhruFjikBYdBhYP0Ng8iCupM_ByrcL39OnAhYxUjCkHR9KFOBzlImG0LGezp9T7bfsrW2VDRT8E6mP6EF0oncUHkOf9UCZYQ51RYHPAPxtaTBnhv0j3g0wDhxo0u5fuEX7Y15GJ9WW3bQIp7sA7yG-ah-I6Vu4WCdtqDy3G-zAAcenBvnaRhR5df68KbvJlAnQMZ8YN4iK-IQuQHR7-oHpSy0B-XNJhHlDi9rvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=ASZg6F4SCn0zdxOPZx69lWBKjC1JDUdMRo7DOORY8vFJxzvR4iwpVgPyofRiAFZ5Mz0-Tz_8hQt50VYBFHFH94xOmmSfBLlxy37T0KPtSTrP0T-hhruFjikBYdBhYP0Ng8iCupM_ByrcL39OnAhYxUjCkHR9KFOBzlImG0LGezp9T7bfsrW2VDRT8E6mP6EF0oncUHkOf9UCZYQ51RYHPAPxtaTBnhv0j3g0wDhxo0u5fuEX7Y15GJ9WW3bQIp7sA7yG-ah-I6Vu4WCdtqDy3G-zAAcenBvnaRhR5df68KbvJlAnQMZ8YN4iK-IQuQHR7-oHpSy0B-XNJhHlDi9rvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
«۱۰ فروند کشتی روز دوشنبه از تنگهٔ هرمز عبور کردند — کمتر از ۱۰ درصد چیزی که معمولاً از این آبراههٔ حیاتی عبور می‌کند. وقتی می‌گویید «تنگه باز است»، منظورتان چیست؟»
⏺
ترامپ:
«اگر مردم بخواهند از آن عبور کنند، باز است. ما آن را برای ایران باز نمی‌کنیم… الان باز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68135" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68134">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
مجری فاکس : آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
ترامپ : «نه. گاهی اوقات به عملیات زمینی نیاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68134" target="_blank">📅 01:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68133">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=FtV04H_9jMa2MUqSIRadtfKHWj5krKT7UeFZpx9h-jkLkFHHxxmg6jf5BaOz0lYVMgWTpWiqGZxh2aPupxFD0g3o1E1-zcOPohXDkXt_C8ZMBp-1CtwsvRZGDarHkK7HlQsUEFkrLqXjqjGi-0835v4BzFMhx_QWGxy3yq-VIcgd5almPFGG_FIp5TVnrGRzrwsTeEuMV9NOLv5yhXDWVvoxwoo41loIBf3bfKcCU1jL3M10hz6ev25BCLA3iSZIMLBndVbrMmUYgla9ZJRKreVqSaUJ1YoEWDWGD87iytWg6WWhPArl84_y35VjsvmJnS7OWnzGpTl3oJjbIansag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=FtV04H_9jMa2MUqSIRadtfKHWj5krKT7UeFZpx9h-jkLkFHHxxmg6jf5BaOz0lYVMgWTpWiqGZxh2aPupxFD0g3o1E1-zcOPohXDkXt_C8ZMBp-1CtwsvRZGDarHkK7HlQsUEFkrLqXjqjGi-0835v4BzFMhx_QWGxy3yq-VIcgd5almPFGG_FIp5TVnrGRzrwsTeEuMV9NOLv5yhXDWVvoxwoo41loIBf3bfKcCU1jL3M10hz6ev25BCLA3iSZIMLBndVbrMmUYgla9ZJRKreVqSaUJ1YoEWDWGD87iytWg6WWhPArl84_y35VjsvmJnS7OWnzGpTl3oJjbIansag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا اطلاعات خاصی وجود داشت که باعث شد تصمیم به آغاز این عملیات بگیرید؟
⏺
ترامپ:
ما می‌دانستیم که آن‌ها خواهان سلاح هسته‌ای هستند.
⏺
خبرنگار:
آن‌ها می‌گفتند که خواهان سلاح هسته‌ای نیستند.
🔴
ترامپ:
هر چه می‌گویند دروغ است. آن‌ها دروغ می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68133" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68132">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=WiFLdhG9-AlnYi_qrfNfHbT1BfSZaIAA59sMiL4o8tGDo_PRxDiOs49hGs26alxATDGnSOmZYsQSFSaQQ4xZamRcYK9UxnrLl8kQy8UKUsG50MZzOBP_PbMsxO9iSNPk5HO9-u-lpQRrsf8et9PVsigtKU4sxtDJ7pZiIIClD-9GF0cpPraN19wP6SWjOGCrC77SIknoSjaTriPq1RrwgOQVUObjF6yETIM0oCCq9US0C6mvkUC7_9YU2cd5UEJ0rNEVY4duugAI6JpU0kr11l7gMVBfJsg4ryd-EqtCukwLVzkDdqvXZPtXihCKlodUDNERBys9WUYVMjzThxmmHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=WiFLdhG9-AlnYi_qrfNfHbT1BfSZaIAA59sMiL4o8tGDo_PRxDiOs49hGs26alxATDGnSOmZYsQSFSaQQ4xZamRcYK9UxnrLl8kQy8UKUsG50MZzOBP_PbMsxO9iSNPk5HO9-u-lpQRrsf8et9PVsigtKU4sxtDJ7pZiIIClD-9GF0cpPraN19wP6SWjOGCrC77SIknoSjaTriPq1RrwgOQVUObjF6yETIM0oCCq9US0C6mvkUC7_9YU2cd5UEJ0rNEVY4duugAI6JpU0kr11l7gMVBfJsg4ryd-EqtCukwLVzkDdqvXZPtXihCKlodUDNERBys9WUYVMjzThxmmHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«همان‌طور که می‌دانید، ما پیش‌تر دو بار به جزیره خارگ حمله کرده‌ایم... اما در مورد تصرف آن، اگر بتوانیم توان آن‌ها را به اندازه‌ای کافی و عمیق تضعیف کنیم، این کار را انجام خواهم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68132" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
حملات به ایران ادامه خواهند داشت تا زمانی که من بگویم کافیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68131" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=GzRTJUXRE_kDhrbAJa-Xpl8NAF9tx5_643R-4Tz5Pj3_hV7VFKq3R7WOZV0M1UJ0Qq6VuoMcMegcT8Hfi8WDFNfRpIqt3W4xdBHFMf-LpBG_WVF2RwGdn8ykchl4iRW40RUfc_U3B9mjwA781FL_ufwxgdqi-dETDFUzw_vN-KUiuQ9uk9zgX8Pb61mTupimsQDF7mnEHdeFBOnCRxZ8EfpnFIOlj-WKRQCw8dsFbKX6Y_Uuiz69xvFkyDyGw-1NyxnWrKz98ufnyWm2t7TITT0GWPr_c9Tk867HD6YTYaSLlVO90y0RcPtOei8JT-a9VGS6vJixy2ckCUx1ucHLFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=GzRTJUXRE_kDhrbAJa-Xpl8NAF9tx5_643R-4Tz5Pj3_hV7VFKq3R7WOZV0M1UJ0Qq6VuoMcMegcT8Hfi8WDFNfRpIqt3W4xdBHFMf-LpBG_WVF2RwGdn8ykchl4iRW40RUfc_U3B9mjwA781FL_ufwxgdqi-dETDFUzw_vN-KUiuQ9uk9zgX8Pb61mTupimsQDF7mnEHdeFBOnCRxZ8EfpnFIOlj-WKRQCw8dsFbKX6Y_Uuiz69xvFkyDyGw-1NyxnWrKz98ufnyWm2t7TITT0GWPr_c9Tk867HD6YTYaSLlVO90y0RcPtOei8JT-a9VGS6vJixy2ckCUx1ucHLFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«در نهایت، اهداف حوزه انرژی در ایران را هدف قرار خواهیم داد. نوبت به پل‌ها می‌رسد؛ هفته آینده سراغ آن‌ها می‌رویم. ما تمام نیروگاه‌هایشان را از کار خواهیم انداخت. تمام پل‌هایشان را نابود خواهیم کرد، مگر اینکه پای میز مذاکره بیایند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68130" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36032be115.mp4?token=G2CDS4eDzAiihvfvc0qWeqAMqApwlxohTWGGoYlCZMt7iIMS6bljFa3PaWR0v6N3FqVslYy9hh2g7cWOvHmRYkaoZp1GQoZjM6hQA1YHA44IVeiaNE5NIazh5gDQMaT-UNhd7q1MREcYT1VXYgklPQ0TRghHc_uBzUF5wWw9P6Ss405KAgVL4jBTMIOE0bFgsqfIVQQqNF7aNTv87wJW72XZ4fows_3inQqbdx-dHPBWRdWiewsIKYkNxUKJG-ACBOUupd7EWSaet-COnENR2nf0zZHvxFbBTOq2HdXYaOYNUxxIgpbSrKj52ldBhtK3MG6YOy8DyFU_l2t87UTZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36032be115.mp4?token=G2CDS4eDzAiihvfvc0qWeqAMqApwlxohTWGGoYlCZMt7iIMS6bljFa3PaWR0v6N3FqVslYy9hh2g7cWOvHmRYkaoZp1GQoZjM6hQA1YHA44IVeiaNE5NIazh5gDQMaT-UNhd7q1MREcYT1VXYgklPQ0TRghHc_uBzUF5wWw9P6Ss405KAgVL4jBTMIOE0bFgsqfIVQQqNF7aNTv87wJW72XZ4fows_3inQqbdx-dHPBWRdWiewsIKYkNxUKJG-ACBOUupd7EWSaet-COnENR2nf0zZHvxFbBTOq2HdXYaOYNUxxIgpbSrKj52ldBhtK3MG6YOy8DyFU_l2t87UTZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا جنگ با ایران از سر گرفته شده است؟
⏺
ترامپ:
خب، گمان می‌کنم بتوانید هر طور که می‌خواهید آن را تعریف کنید، اما قطعاً ما داریم ضربات بسیار سختی به آن‌ها وارد می‌کنیم. آن‌ها باید ضربه بخورند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68129" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=artgeZk-mkchU2UeADRqLO3QU-R-keCi6UZiDwTmo4Yn0CUVk1sv-WCJbJXKdB8Wu6bmspVtvcj63jOltS52dWsUxh8wbqQcpJq6gXTcKlD9xZ0LU1vq_-dGZ1PLgAtD8wdbP2qNedsNqCpcZi9izwCT-_0YOVKyv2ZAFY9c_T_VbWCZHaeQ9rZzSDAxxd8olRC_64O8YxCF2hH5atXItMwAkcGh3Fni33tnGxhjT3IdwWpNgTViqXDDfLZqWm_RkuYoGaZQlQGFOuxESXvipSxweRWKlyyTj-ke4Ob9LG9VW9AvdfPdxQaW1py-sTsh2azF2ABBxEX8g89a9AvNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=artgeZk-mkchU2UeADRqLO3QU-R-keCi6UZiDwTmo4Yn0CUVk1sv-WCJbJXKdB8Wu6bmspVtvcj63jOltS52dWsUxh8wbqQcpJq6gXTcKlD9xZ0LU1vq_-dGZ1PLgAtD8wdbP2qNedsNqCpcZi9izwCT-_0YOVKyv2ZAFY9c_T_VbWCZHaeQ9rZzSDAxxd8olRC_64O8YxCF2hH5atXItMwAkcGh3Fni33tnGxhjT3IdwWpNgTViqXDDfLZqWm_RkuYoGaZQlQGFOuxESXvipSxweRWKlyyTj-ke4Ob9LG9VW9AvdfPdxQaW1py-sTsh2azF2ABBxEX8g89a9AvNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‏ارتش جمهوری اسلامی:
در مرحله هفتم عملیات «صاعقه» محل استقرار جنگنده‌های اف ۱۸ و سایت نگهداری تجهیزات ارتش آمریکا در پایگاه الازرق اردن را هدف حملات قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68128" target="_blank">📅 01:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68127">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68127" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
بندرعباس و سیریک بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68126" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=n1yzz-BMvpzlLCvPn6tkDFa5dohomA15ouvT4oOVUD5Non19YpvXjjmRCs43SzkYAj_LKAyestGT9Y2-NBy87TCvcdZ2YqN8YZTB5Fb1er__3yDihA_tIg7GLeuLjREZkGumUD6DqcBosxa_ISyeV7Js-itTAZOSwQWPBCoHT4mddC5BvxpXF8mVWZHeCDIUQoGXHJxeLKBLhg3A7KDluq-Blq6bhUc1crbvc8457xgSVWzDU97x0AgyXN7rkT7kKovhBWd7DIJi18V-HPFnFiTpN-I0QjIRRxchs_a6WhFYUn0U1xyAk6VOv1USbjLcBo9sTS9HL-EygP0HOT5d8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=n1yzz-BMvpzlLCvPn6tkDFa5dohomA15ouvT4oOVUD5Non19YpvXjjmRCs43SzkYAj_LKAyestGT9Y2-NBy87TCvcdZ2YqN8YZTB5Fb1er__3yDihA_tIg7GLeuLjREZkGumUD6DqcBosxa_ISyeV7Js-itTAZOSwQWPBCoHT4mddC5BvxpXF8mVWZHeCDIUQoGXHJxeLKBLhg3A7KDluq-Blq6bhUc1crbvc8457xgSVWzDU97x0AgyXN7rkT7kKovhBWd7DIJi18V-HPFnFiTpN-I0QjIRRxchs_a6WhFYUn0U1xyAk6VOv1USbjLcBo9sTS9HL-EygP0HOT5d8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
هم‌اکنون دارلین گراهام نوردون، خواهر لیندسی گراهام، در حال ادای سوگند برای گرفتن جای برادرش به عنوان سناتور کارولینای جنوبی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68125" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68124" target="_blank">📅 00:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68123">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
انفجار چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68123" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68122">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Za4WkbDTNyIQHy2-Tk7q6h1DGGW2mXr8isyjJP4buSBhEgrYys-vHnc7S56Gu97fhUJCKd82YCa9FdYTUEVAYKk2fKF55nuxF1MIt5WUfmTXwOR6nstzJ-5fxc7sC-jtCYq-aywFHH-aM8u61M-55nGCTPwEs1BZatdLh90JbQnyf77YryFLMcV4VS0JTZ2amvhQRUTN1H5JZlJio1p9glm0M-TE77mgERmSEXFUrgNMq4KIwU81gbTljJHqNY_GuD0XcSW4u04aivgB-0-KagwIqGsjNAFdiwy1hDmYRDy8xlYAHUhXw71USAeM8gQUH3X-qqh3ADCUTWv8pLHo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68122" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68121">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=Nf9TZGPI-uuZk-gWVeW2r6P3rL_FhSVXWGPw1OGxFTBGIejuYSrZVId3gAq3-rnWNYxuVwlXmvMBB2bktE6OLzk6OFZK0TX4XagdU7TcC2EbXvS4aoWYAFkEz1sd3JrsnrV70QbWXlXDkiBX35vwxKs3fxGHMKHgDPuoTis5PWgTEI1wOHAaF_csJWMO2D4CfQ2CReaVyVK3xKG3XFyZytyQGsXsP9CMBTCx6RkhgbLVAGLwfjLmbYFj5JT9gHDJz7tetOMtz425Vo2jLYOex15Us9LonzxG7zH7CPNpbsDUpg55dv9Z3ANAcMWagZaVO1R1dSBFwppay1ab_xPhEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=Nf9TZGPI-uuZk-gWVeW2r6P3rL_FhSVXWGPw1OGxFTBGIejuYSrZVId3gAq3-rnWNYxuVwlXmvMBB2bktE6OLzk6OFZK0TX4XagdU7TcC2EbXvS4aoWYAFkEz1sd3JrsnrV70QbWXlXDkiBX35vwxKs3fxGHMKHgDPuoTis5PWgTEI1wOHAaF_csJWMO2D4CfQ2CReaVyVK3xKG3XFyZytyQGsXsP9CMBTCx6RkhgbLVAGLwfjLmbYFj5JT9gHDJz7tetOMtz425Vo2jLYOex15Us9LonzxG7zH7CPNpbsDUpg55dv9Z3ANAcMWagZaVO1R1dSBFwppay1ab_xPhEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران تنها جاییه که بتمن هم به گا میره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68121" target="_blank">📅 00:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68120">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TztxTK544w4zUr_9e7CW7crYYPPSh4WXUFNv-FeVa-a0VTrQtchvthAI-0KzNQydXy4mh6emoMDGaVynTFD19qR4GcPUCrXVetbwZ6kSNVnIjEGZKndJ7hSfLyxlNzubdwvRlBkxU0iMZItQY2diwsbzf1ycoBImR-vu1DlsxeFI5PPA3lVgEIq5Delmc-T9IUOQxM8iV0bErlXCzaUlH36nnaIhDiXxjf3q6mOl6bTE2Aqz3BnkYiFB88AVeYnzXm3THsEz9GK_K66MQavhX_Vpt0MumVfpWLKmYiIijOD15Fgg9o5MZctw5Qp-lxT94W5RpnhHp2H4_REjv4ddNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده امروز ساعت ۱۶:۰۰ به وقت شرقی، محاصره دریایی شناورهایی را که به مقصد بنادر و مناطق ساحلی ایران و یا از مبدأ آن‌ها در تردد بودند، از سر گرفتند. در حال حاضر، بیش از ۲۰ فروند ناو جنگی نیروی دریایی ایالات متحده و صدها فروند هواپیمای نظامی در سراسر خاورمیانه مشغول فعالیت هستند. نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68120" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68119">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68119" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68118">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=B8sCXvGzwU3EAMCsfc9wj4cCkMqntXjDjmWpmAqP8Z9Cu6xvgJOwyyhYY4Z590B8ZxXMWKZEbHCF-lqkK5HGek9qHitLQzKqFYqCjwdyrdpkGrNfCvZDm3eDJxbjIFKI4at-fR1BiNV9tK1SS1s2aj5_wgs6XmsL02rqOHNZ2f6UOdsz0qf4DSNHcTAWGFsbcIb5x_7ue6pHYqnFrwR4oR_37UP0BnvkTLj468SIznOqn3Iy7kxWdrDI3auirZ0FUp5iICI_WJk8haK5_ChSiCJ9Ltbevqjsd3OJtrVfhHRowzZCiGPZli43ySAAe8QeSRtoTm1mamvXV_FPKmW1WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=B8sCXvGzwU3EAMCsfc9wj4cCkMqntXjDjmWpmAqP8Z9Cu6xvgJOwyyhYY4Z590B8ZxXMWKZEbHCF-lqkK5HGek9qHitLQzKqFYqCjwdyrdpkGrNfCvZDm3eDJxbjIFKI4at-fR1BiNV9tK1SS1s2aj5_wgs6XmsL02rqOHNZ2f6UOdsz0qf4DSNHcTAWGFsbcIb5x_7ue6pHYqnFrwR4oR_37UP0BnvkTLj468SIznOqn3Iy7kxWdrDI3auirZ0FUp5iICI_WJk8haK5_ChSiCJ9Ltbevqjsd3OJtrVfhHRowzZCiGPZli43ySAAe8QeSRtoTm1mamvXV_FPKmW1WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
علی خامنه‌ای، (19 دی 1404):
ترامپ که با نخوت و غرور نشسته آنجا راجع به همه‌ی دنیا قضاوت میکند بداند که مستبدین و مستکبران عالم، از قبیل فرعون و نمرود وقتی که در اوج غرور بودند سرنگون شدند، این هم سرنگون خواهد شد.
⏺
🇺🇸
دونالد ترامپ، (10 اسفند 1404):
آیت‌الله خامنه‌ای ایز دد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68118" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68117">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
⭕️
محاصره دریایی علیه ایران آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68117" target="_blank">📅 23:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68114">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cC_bpwOTv7N7qMS54d3D01tyzMX5jFPE9stQcRsNadvwkYJQ7dODZ2wfYdZFI838lpWxnLJHVsbnCgmXonQBqf3MGwVjFa_3GMRMipyxrfFvJRe9tFOsXdp5zNmwkClZJi9eUcYhZP5p2n71RiHVwSLVhUn9WbKdn-KuxkcuknSbwZx4EYwJ8kZ3_aas9Kp9PFRJDl1ynQe8xOxSzxyyVL6jxh76L8OWqyHYnvhEFNvrL9VC87Pl-rInAxlXjSkretY1JHpVUpdLC7Udyi-7uhtvxJL_7ahfQLNggMDWbqA16RVOVBFmjD7q26TPiJenpaXce0iIQ0KicmBuWgkCgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gozLa5IXJA-dRywFlvGulQKTPNDSVv5HsIt96cLnl06WIvz7UtT3hy36xDV-hZGfz3xzbg-6U_vAzolU7O51nAG-NRQUDUGz_Vdg1zfOT77ldJJ8cVKUH37YWlMEwaE51jUtV-4uB0KpdKmcGrAi7FyRdLvouYM0_ol8QbkhxWhzS-Irfk1MU0cNvwJelj_UhtaMNzYCR8LpXxv9RRuBogqPQSeGH2j_bBl_qxmv65eY1QFaTZPdidCe_QbMcHGh5-wwnXgdTpCtd4dtfAV5cVZ2lnblqYDXaeQnGTMtgR-J-AOd5njPA1oR45M8KNY-ZJB-JN0mTY7pA94QDhbdLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه می‌خواستیم نودای نیلی افشارم بزاریم، پس هر وقت بابای مانی لفت داد می‌ذاریم #hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68114" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68113">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
سیریک بیش از ده انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68113" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68112">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
انفجارهای جدید در خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68112" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68111">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
‼️
تصاویر جدید سپاه از حملات موشکی‌ش
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68111" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68110">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ماشالاااا اسپانیاااا، اینا بیان فینال مسی راحت تر قهرمان می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68110" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68109">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68109" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68108">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68108" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68107" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68106" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68104">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁪⁬⁮⁮ᴹᴬᶻᵞᴬᴿ</strong></div>
<div class="tg-text">مرسی که تک خور نبودی
💙</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68104" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68103">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ43Mbw2D55Ii45V_lgcYo72YJr0T39JbZ49eBPGsgx_KfSbODTblSgCzTjDmJSPsy3AfMvBxY01K6qViyNqmAczSt3s1rDNlAvYTnOZMv4JOmUqLq9cNV9nc9xzRjRhW_rSyb8f9SiRxXYqFQMDU22zqOm2Bk5Hd_QKBdFlBpAZVwKNQC0H6pPCqDuakG5jHYcnKOjjvjgAk7w3aBh8rotpZ5lpg4_49w_TMsnGdN0bX_zrLnbIdnOZ4M3UqRI8b5hKRhoi32CXHd5d542DpRHObRW6MVeG3Bel8kMdn_-C4dDbu7xEZ5aSXh-nkUoo-s9KwYofYdRR-85jRLD6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68103" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68102">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⏺
رسانه‌های حکومتی:
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68102" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68100">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTnMfeHTNP-uRuXZF-l79aKYRFe9stWDctMtcGxLnrV5sytDGsoufQh-05DBDRGsuQroLyOCv1ELkTrhn-mCD5q_pJUWZ10zF3ujq2T_FsAoTSGI5F9-jzvDQZJQU5aA7j03hZseN1bZuHdfNeIjdNPXYSdnvahlTFVjCnGEgQItCWUlT0jVlhT2F9W8Y5tWMdw9HkrlsOknUnp9Oqms47FaBSK6EoQ2th6-AJEvlRfXx_7ZOGvwoF43uKtnORmDfM-PQZoKCUGtTix4VAXZUzwQ0woyALzMhcGPAoke8SMAadg2JaIsF6O6Kbmk-i50HVgTCQiVZ0A8DvlVK6hsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hu4J12P3NtvDH6jmHG1w2LhfWX6kJRVvx7ntNI3WiSCTTnEV9E_BVYv7QDM8fjktH-6ig1Uxh18gIwz4bBkEdm3R9Wq49B8vSo5MdYOt88-5zE7EK7aHRw_E7x-iubsDEtvBHdl2gmXkRqOmaenAtMtmHW11JQDYrCKXd_EP4XF5OQkvYzbjsKeV_mndKQ7c_xbzI6LglfxHssC6xo3asS1kSSX8mDS8cX5gjBril4oMNJCdZkvkepatOFQiMNaPf0oYrEuJ3aD4-62DZSsg4U7eWF8Jzmtdl5_AJTB7aldPVpR9OmGRKJ_5yBg2g9ul4uV19dZuhaMcjce74xJd9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68100" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68099">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAtvE36ZE7rNUHpUgMH2Lw-z2oSr-5RgxE6Ai955YQC7JD-nNBwsbiEEpYdatcExlLA4LDjV2dR28_Wdz1SHVh4ncWK3co_mXy3ZV_FI6CJdqf35FmM15F6sfjAV9wmQBzSPIo7mxBFwObEZ4Zoaf1sdx1maOdXDqtMLH9ymI_GM3Vnh1F8evlfhC0pxETEBLgnoKgTBPZUo6WHrRl5ijGb1H1G-RuqSPbD6EnZNi_45-WcNNJhyfgdIUvDiJMPzZpT-zC7K3uNfDreIs4Hgrp2D4f__fIVHjSirU8Q8FBiFd-itmxraAQYg8R6t_MS9yDE_zkeGWIhxHSbezc001w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پزشکیان:
‏در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است. امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند. در کنار و قدردان این مردم وفادار و مقاوم هستم.
همه جای ایران، سرای من است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68099" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68098">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZYwDtiQ6dVm6lrwWkEaUYqG3pSKa3RUrD4UAoMPhZrvxK-roM2ImIic2fzAgu1Az_6YBwmYaH_VW79GFsHjpA0yzkQJuYmkUUONTNHKw9A0NDNx105uVDsMiA9EiLPfJT05m7IT5G1O5q-puateMeKNo_dNuDShLfL8fcVHtHOrVjzhjFzSixpaNo4IK6tt8NFA1zDGpiDuFWidAcEklD4-LyI6cpiAoARn2q8jFOyWBJc6w4jnwlKN08518_z3yZRTmj8yVjLuj7O6gslhJ6OJrAo3bzTTvWJEi5Wp5bwJ1itkWnFlBvot9c3JWJDeCCIRTUKIlXyfVn9rMEXE_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68098" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68097">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=dzRPVHAO0TAfnfb-VuVCX5IsFsiGYBeHU1rDqL4KKj0W3UduAzqrjF6BExvnaDH-RmCv4BUU_QxQ0jFyYBd0wOZy79QMRyeF8Q5tzKfTr3t8dvdgfmcfYPf6CKRNe1SnE41DI5wzCe8oslRZreG94sZZPQ0OaivTBO7K89Dly2dLx98QQEfkkbvuV6nFCFV3ouS1sTUEcEXhuqNfVU-fuGzQiKpFwJKgc08dz1kb9JG__Zu0KF4WbwCmY2g3TNvgXpxiLeGTUpvE_W207Xv4mRbYE4U7QhNj8SYZyCV9uzIxIaI4pz1rJlgcsPu-rxVOEXXKS6Rngc1tbNxV9OL66w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=dzRPVHAO0TAfnfb-VuVCX5IsFsiGYBeHU1rDqL4KKj0W3UduAzqrjF6BExvnaDH-RmCv4BUU_QxQ0jFyYBd0wOZy79QMRyeF8Q5tzKfTr3t8dvdgfmcfYPf6CKRNe1SnE41DI5wzCe8oslRZreG94sZZPQ0OaivTBO7K89Dly2dLx98QQEfkkbvuV6nFCFV3ouS1sTUEcEXhuqNfVU-fuGzQiKpFwJKgc08dz1kb9JG__Zu0KF4WbwCmY2g3TNvgXpxiLeGTUpvE_W207Xv4mRbYE4U7QhNj8SYZyCV9uzIxIaI4pz1rJlgcsPu-rxVOEXXKS6Rngc1tbNxV9OL66w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
👈
مهمات خوشه ای شلیک شده توسط سپاه در آسمان بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68097" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68096">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سپاه پاسداران به بحرین و کویت حملات موشکی و پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68096" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68095">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68095" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68094">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=IujEiGqV3Uog33ELwdIMhQqdV8atS61B7BNRNvKag6kfftFt-olzzfnhU-43NjX70K8Ceapj6BxEig6crq13lM7CRH-8SdTDYrRAvGot5VE1AsL_L8lmMkVvRXi9XpqvV6X45r39zSfuG0mnXFHrhkj7vnn8lNqq1VOsSX20QBu5vvNG3KHwDHNgOMV36PRiQgxCMiQ8BGYuaciae57ysuYaJlXw2WmiK3eokRd4tPsI98KMbIF8_Fsz4FVlGeZ8-rAyOcTZcaFxtQjeSouy9jKxX8it_cy0zG-clStOjwzuM-jm_LPoTN0GLpBqQGt89kWik4HcttAcymMAvqoqNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=IujEiGqV3Uog33ELwdIMhQqdV8atS61B7BNRNvKag6kfftFt-olzzfnhU-43NjX70K8Ceapj6BxEig6crq13lM7CRH-8SdTDYrRAvGot5VE1AsL_L8lmMkVvRXi9XpqvV6X45r39zSfuG0mnXFHrhkj7vnn8lNqq1VOsSX20QBu5vvNG3KHwDHNgOMV36PRiQgxCMiQ8BGYuaciae57ysuYaJlXw2WmiK3eokRd4tPsI98KMbIF8_Fsz4FVlGeZ8-rAyOcTZcaFxtQjeSouy9jKxX8it_cy0zG-clStOjwzuM-jm_LPoTN0GLpBqQGt89kWik4HcttAcymMAvqoqNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سر دادن شعار مرگ بر سازشگر در مصلی تهران
صداوسیما هم چندین بار صدا رو قطع کرد
🤣
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68094" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68093">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=E5KtquGJxT6vj2WMa9PY9r06iaZOqNJT_ifXBa3q_y8_21CIqmlv6E280tSkK3NcTa0TNWnRPYGbvNZ6LDBy8-PDejN8gJdJwnhphzUinJgPHf9gbn7dCiWUFl5yCRsX1_6IkflbuO0_IntBRNSHM28FlboQZVYdjBoo05GVXX4Ot1Unt4B8VxcLThc_KKU61LOTEEuPkuV96b-a27ysu91YVzUkuUmEO6cStmD82UdpjQCEWhK03YcoPAfoyJadjQF7pBjf5ihSlUw77h28wTNnXaK0L4qT07d6aBRKt7tLejb6eXc_-RPB0lUZUuc4Bryx-FBawvg-AXYwtFY5wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=E5KtquGJxT6vj2WMa9PY9r06iaZOqNJT_ifXBa3q_y8_21CIqmlv6E280tSkK3NcTa0TNWnRPYGbvNZ6LDBy8-PDejN8gJdJwnhphzUinJgPHf9gbn7dCiWUFl5yCRsX1_6IkflbuO0_IntBRNSHM28FlboQZVYdjBoo05GVXX4Ot1Unt4B8VxcLThc_KKU61LOTEEuPkuV96b-a27ysu91YVzUkuUmEO6cStmD82UdpjQCEWhK03YcoPAfoyJadjQF7pBjf5ihSlUw77h28wTNnXaK0L4qT07d6aBRKt7tLejb6eXc_-RPB0lUZUuc4Bryx-FBawvg-AXYwtFY5wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب ترامپ درباره تحقیقات اف‌بی‌آی درباره مرگ لیندسی گراهام
⏺
خبرنگار:
«آیا می‌دانید چرا اف‌بی‌آی در حال بررسی مرگ سناتور گراهام است؟»
⏺
ترامپ:
«نمی‌دانم چرا، چون فکر می‌کنم او مشکلی داشته... من شرارت زیادی در آن نمی‌بینم. می‌دانم که انواع و اقسام تئوری‌های توطئه وجود دارد. فکر می‌کنم اف‌بی‌آی وقتش را تلف می‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68093" target="_blank">📅 19:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68092">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=SsQO2925F0ikAHWKRcp1R0QDo9oRed3ujkL3hbMC0jl5rtI55cBPcrUwKIysIQHIOlzS2m_rkmZ-BhJCLtAh6VxwJJv--7oi-f844y3RLQ2Q0m785DcD_wvWM_X62rVM2VdtoYm5gQ9X8nOuhrdMWlpO4W4OOT4omJyCe67lwVcm9RP5FFeQdrGeUzM91hW7kYvmcYSSB5I1qE7imH0L7spBFT4zElpMUjYBddRvhq7uEdm0I5q1-Lx4PniTEh3GsOwhcAjm-AKWaOmsGpWVl_xyfj9mI2ruNCC1eANATBD67RtrrqFxgPFmVkTojt3AEvNtlO9c9RQRAee7IgtG7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=SsQO2925F0ikAHWKRcp1R0QDo9oRed3ujkL3hbMC0jl5rtI55cBPcrUwKIysIQHIOlzS2m_rkmZ-BhJCLtAh6VxwJJv--7oi-f844y3RLQ2Q0m785DcD_wvWM_X62rVM2VdtoYm5gQ9X8nOuhrdMWlpO4W4OOT4omJyCe67lwVcm9RP5FFeQdrGeUzM91hW7kYvmcYSSB5I1qE7imH0L7spBFT4zElpMUjYBddRvhq7uEdm0I5q1-Lx4PniTEh3GsOwhcAjm-AKWaOmsGpWVl_xyfj9mI2ruNCC1eANATBD67RtrrqFxgPFmVkTojt3AEvNtlO9c9RQRAee7IgtG7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره لغو عوارض گرفتن از تنگه هرمز
:
«آنها (کشورهای عربی)گفتند: "ما ترجیح می‌دهیم سرمایه‌گذاری کنیم تا عوارض پرداخت کنیم." و من این را دوست دارم چون هیچ‌کس نباید بتواند برای تنگه عوارض دریافت کند.
«در مقابل این سرمایه‌گذاری، کشورهای حوزه خلیج‌فارس مبلغ بسیار زیادی در آمریکا سرمایه‌گذاری خواهند کرد. این در واقع خیلی بهتر است!»
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68092" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68091">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
شنیدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68091" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68090">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LANa6l8vfJilw9y6lpq-MakJWspORY48AsSWbGuq6H5S7HkgySd92L-nafxv7ubbUyyOMULXKgYyjeZCDYBzSrPHkVhxbSRBVS2TFQtCDHkPql3k88OPlV-y5z3Ho2fMXPktq1ae-JERdlGwr_Vh1w0XCJt8fCYq4eOGu-Jjd4iQ7aewyxVkzGuUJzCJCR_dQe8Y42JRcxnQAaNaMAqw9RkJ_feVm7aaYXiWWX8Cf6soX2T7n9opFx79k4DPfeCIpdQSyDGfx3YHruSBrgnaUIt52qcDqHvufDAmNfawpBHAFnW0d9DunmkIzh6k8IeLCjED9n9qTXq6nHEme0uoMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
به لطف قدرت فوق‌العاده ارتش ایالات متحده، نفت بیش از هر زمان دیگری در جریان است. درود ویژه می‌فرستم به وزیر دفاع، پیت هگسث؛ رئیس ستاد مشترک ارتش، دن کین؛ و فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، دریاسالار برد کوپر. به واسطه تلاش‌های آن‌ها و تمامی اعضای قدرتمندترین ارتش جهان — که بی‌رقیب است — تنگه هرمز برای تردد تمامی کشتی‌ها باز است، مگر برای ایران؛ و این استثنا به دلیل رهبری دروغگو، خشن و بدخواه ایران است که کشورشان را به سوی نابودی کامل سوق می‌دهد. بنابراین، ما یک محاصره کامل اعمال خواهیم کرد، اما تنها برای کشتی‌هایی که به بنادر ایران می‌آیند یا از آنجا خارج می‌شوند، و یا محموله‌هایی مرتبط با ایران حمل می‌کنند. بر اساس گفتگوهای بسیار سازنده با رهبران خاورمیانه، تصمیم گرفته‌ام که «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌نامه‌های تجاری و سرمایه‌گذاری جایگزین کنم؛ توافق‌هایی که کشورهای مختلف حوزه خلیج فارس در ایالات متحده انجام خواهند داد. این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان فوق‌العاده سودمند خواهند بود. همان‌طور که همگان می‌دانند، ما در مقایسه با هر کشور دیگری در طول تاریخ، بیشترین حجم سرمایه‌گذاری دلاری را در ایالات متحده داریم؛ اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهد کرد. ما شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطحی بی‌سابقه خواهیم بود که میلیون‌ها شغل جدید و پردرآمد برای آمریکایی‌ها ایجاد خواهد کرد! آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای که نظیر آن هرگز دیده نشده است. دوران کشتار صدها هزار نفر — از جمله ۵۲ هزار معترض — توسط ایران به پایان رسیده است و مهم‌تر از همه اینکه: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور
دونالد جی. ترامپ»
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68090" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68089">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kks1VOdzvEdiUM8PKh2sDTpzkYm-hw3oUADxrLGp9eVsj6TCcKe8LNBRRFWbqz-C8H7iFu4npHBolf-AcVkXak4Ng-OZNsh_8e_HNvJKfb-o1OWokHO1bYYm3mE11JhtcTKe_PvpWPGep8isJqjSSqBoG55K7P1sOpXgwVURZz2Iz50EDjJDN1jDfmjT7TP3cM8RzkWpP6raiQ9xqnvJSOICnrFPquZB4hluUuJuVlN8EF9iqLAI7MuDfuO3H8dlJZDNH6_QrCb7zzsvUOPsAJOwwGg3-4QfnEIHXcFn9YfDUxyajl2BlbuQpF4oA8SkADpNg2CMHcibabRFXLl1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ پستی از کاربری که متنی از مصاحبه او با روزنامه گاردین است را بازنشر کرد.
کاربر : «وای خدای من!
اصلاً نمی‌دانستم ترامپ این را گفته است.
آن هم در سال ۱۹۸۸!
جزیره خارک را تصرف کنید!»
متن مصاحبه ترامپ با گاردین ۱۹۸۸:
«اگه من بودم در قبال ایران بسیار سخت‌گیر می‌بودم. آن‌ها از نظر روانی ما را شکست داده‌اند و باعث شده‌اند مثل یک مشت احمق به نظر برسیم. اگر حتی یک گلوله به سمت یکی از نیروها یا کشتی‌های ما شلیک می‌شد، یه بلایی  بر سر جزیره خارک می‌آوردم و وارد عمل می‌شدم و آن را تصرف می‌کردم. ایران حتی از پس عراق هم برنمی‌آید، اما ایالات متحده را به بازی گرفته است. حمله به آن‌ها به نفع جهان خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68089" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
