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
<img src="https://cdn4.telesco.pe/file/GtgpS4OSr6-C3lKDcBTpU0TTIzrlOuB0-an4VuSbr0DROZgN1gtvmWYdfD_V9ATD7KXqbp_IEQRXEBe0BmfzoDtujY1DI14xTM37MwOM4nkeg7BZp6guvijfJb_YWpMy8ZtN7jDLejTy9cHEffsNzOL0U-q2pACYNvSMoweHj8l7IdJ1BAjKQ8l48fMnOPQTcv3iWcprBh0r75E2oIIC7VIRGNQX1nkH2iIG8bG0YljPFRw_H--WsKRujNw-GiXM9nENIxq74GuBRARD-8tmrA-mpikxcYiMHJw-IqQpnYiAFcLa2W-pstEvb9couoX1bHzYQikI6UACRdLUpUVi1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 218K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 07:33:24</div>
<hr>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=QCODCCLiZyVsDpy9ZM4Y-Uek1u35h2nGSFfdnUBx1Xp6eBtOExHZxJJwaJEEVanKCC589FBYW__OGa4UQjz81WzGCuxKba3iUoYz0dGCJ4DBc4OzzrZTZ1mTY4OohaQh0bD_y1M6D8ug6wSwhNbGBqKolXVMERJORDV-OOstC4n4IaKIn69ot3rT21MTUuK_UP_0h6cBpA8bAeR1pzqmhKWybIxoCbz1KfLPnLdFOMXzoHBwkY8-mtF6mxyh9S7algRD8qy313xQDlDdStxCgHCgtJ9bG6L_lLVcPG3mRCbc1BQw5GSXy_8uqU-O_PJ0wccd40csYhLPw6HrYylbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=QCODCCLiZyVsDpy9ZM4Y-Uek1u35h2nGSFfdnUBx1Xp6eBtOExHZxJJwaJEEVanKCC589FBYW__OGa4UQjz81WzGCuxKba3iUoYz0dGCJ4DBc4OzzrZTZ1mTY4OohaQh0bD_y1M6D8ug6wSwhNbGBqKolXVMERJORDV-OOstC4n4IaKIn69ot3rT21MTUuK_UP_0h6cBpA8bAeR1pzqmhKWybIxoCbz1KfLPnLdFOMXzoHBwkY8-mtF6mxyh9S7algRD8qy313xQDlDdStxCgHCgtJ9bG6L_lLVcPG3mRCbc1BQw5GSXy_8uqU-O_PJ0wccd40csYhLPw6HrYylbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کیرم تو الجزایر، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4Hbcfdde5il5B0uyatE-LcFh8559iDy9BmB8kUsgwz9YWhopdHeuL5gCuxH9XsNlMdWJK8qcoDF35qzqdr8nnMXR9Ab9bEmY0-i_lPq8iZxHfHs4Hdi_yMJJaFJF5f_U_QdAhTEpMdsAY-v1TSV_NbIBcFkRc4pMp0VHeMzgUy8FTQWoMQNyTzugbCMi2QMPoT0Qlg889X9tfVCzyNnrlKPP7N6caKbLEOEbygqCaNnL4hVxf8O6bd2qCwsGaakfHv9LBxbL6YjS2lqFrYTlX6e1G9UplzdGWt2bBQVbtzAp-tVEtDh0zbpQQaiEByStGTxzuFkm8DIihZEBlB35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qTaYzhQ7hXhw1vW3PnyyyUuKT9E3mfkyw4e2Obf3OI2dlyyFyC7TyhoRenlftuUHREwxPwTF53fnQEgI-pH1xpPtUg2P-C3Xd-nl4gUosoxRLAS9icxGgtJ5DqJZ-8whMrJ0q9_EM8wkpcM3NOEzYoyO6ujoSwEQeCGzHOU-z2hG4wCZe8Ts6dyuZj9RWbBnD2lJiq25gSxcgVbQq4SqMZ8ZGkLBdkvDVh8i3J7M_M-sVC7sTfWGh3JNVro4EQQfwP5DkJCozOmfFCTmUC60LuI747w8km9UPOT1DiCbt3IxfWltOuEKw7YplqPkpIbIpB9HoNcnhTBVsWeRkuOuCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A88N4T4pvo_jiBIyW1KhyPdRx0C6lUpWXM1a2eao1yW1Kr-5AfORmQGPxZ5OBV65EQO5H2vPXcEMTvB8u2havJIG6mZ7zSHb-v0sSealZ9v6O3PXhDb4rdR7Ed72CDVXYoh9SRuL_1VykfHW5VKxpXvu5y01oGT2LURVsN6UfK5OubqBFcgPBfsUmA_KeO9urDUcIoubeOj3oVrNrD3z9FFT2FLqWblQ4N9dfcqgGM727QIcv-2MJJC9UGHOh_Kf-e5i07Tmp8ELp9obSYxw0iPoTn1r9BZJXawBYflyV8veLKMBGXrRj32gnFdwsdo6P2vCPyqrEDA1DF_ovTFMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmYq-4c7nuu38RydXJNJcxrt_2iDNIvonEroP_Iz-uYgDcA3nkvN1SN3B7ZwaeBU_KJA7JURSN9vsWMMGQtnXvykJaqNJiAxc3D3ZGdU-7Li06koLvVlizFZ-LJ5-G7hM3CFsR4TZd_0p_M0K30EM3L5cQoDFipT5m_owQ5bACz8tg-BPoOeej5eLdcaU-FC0uCf1d-rZxtFcjjQxK7b5xr8CpKzfBIPngHiWwY2us-4WgzGW1T5bLolk5IvTIL-8ZlEC0NQpGg2QN6wdkimK1CXCyKLN3AjaqfIOcaZy4cdgmTAz--3h6EYzJvJTbmvuB0AGjD9pfnNKKfbArcmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDLG4IX43CIeWq0Ioo1OWWTSJNDDFFlYXX3GcSgcivJJmMDvQOhOEMknB9CcF-RyZDX5HpRM2uMuqoNehKTvrelk4qpbt77pNUcM9J946N4epU_kccO03kt3gohmkNDZ391jkXHnlmPH-vqYdLzJp08m6BbgUP1eRp-ze7IlzDSKkBo_ppvzVrdbYOkV_fhzIVQXJO6hbcmAY3RbbaxM7IyyIttRT5NykD2B2KOqS1vsAyb7AuwRTXobvS9b8AIFJs4hp7ZXKGxjAv1Y3ZF6KBKrdJBp95wlBmdhqa3iBDwbZEo_GwxOXMXNblCIx-f0NnTZGUsq0o_TpdvmFd1lgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
به گزارش وال‌استریت ژورنال، یک مقام آمریکایی اعلام کرده است:
🔴
در جریان حمله روز شنبه به بحرین، دو پهپاد ایرانی شناسایی شدند.
🔴
یکی از آن‌ها توسط سامانه‌های پدافند هوایی زمینی سرنگون شد.پهپاد دوم بدون اینکه هدفی را مورد اصابت قرار دهد، در منطقه‌ای دورافتاده از یک فرودگاه به زمین نشست.
🔴
این مقام همچنین مدعی شد که:
یک پهپاد ایرانی به یک نفتکش حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز برخورد کرده است.
🔴
نیروهای آمریکایی نیز دو پهپاد دیگر را که به سمت کشتی‌های تجاری در حرکت بودند، رهگیری و متوقف کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=vxPILOBHOxgLpYh17lYRHXz70b7RD7jlN5r5yvCRK9hdfvlWmmdNnaYCOwR7KcscWImlAh35Tp88cVHBMCEpPQkm_E5TeP6gug0C3_-w89UyJCvEP75sSMcpxwIsUFtGiQHCIhw27FXSxGuLJjwWknsZ8zz2Hjd4-q_GRPcG1jR6ZTYWxktd60mtMS5iG728Tj1hbk72N7ClWVuMN58T31oe3CUOUXnTHYQH8JMb9pJptBkci-HuOBiFPoIs_WqFH9qC57bRHEPadSnnSl3vpd6Y095lyW1UCCG3QyeROObspfJg-j82VysGTV2acn1plvZTVOEg6y2ARLiFWv_BBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=vxPILOBHOxgLpYh17lYRHXz70b7RD7jlN5r5yvCRK9hdfvlWmmdNnaYCOwR7KcscWImlAh35Tp88cVHBMCEpPQkm_E5TeP6gug0C3_-w89UyJCvEP75sSMcpxwIsUFtGiQHCIhw27FXSxGuLJjwWknsZ8zz2Hjd4-q_GRPcG1jR6ZTYWxktd60mtMS5iG728Tj1hbk72N7ClWVuMN58T31oe3CUOUXnTHYQH8JMb9pJptBkci-HuOBiFPoIs_WqFH9qC57bRHEPadSnnSl3vpd6Y095lyW1UCCG3QyeROObspfJg-j82VysGTV2acn1plvZTVOEg6y2ARLiFWv_BBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=VAhixyIDxronvba-TluvJEfVNpmE-h2gMd8t51E7ySBxuOi3IazoFTE4Ra0jsi6N4NtcCfE-ukMqpGjn5UV6Xcu69TshR71voPFiAZDH5iBmpmjFkMr5nfYZep8-f5mmWPbqEmbj7vguvQoaxRalJzaq3uuz70hXTkagy1vcSOiiWuQdHA5luTkbERuXffMukM7YEy3VplpI6ChXsbwPD2u3dHVodU26yh88yFX86w0IwSWKQUBeTbNniaO-s07I5tgng_Uhgm_M82gyIGDvgziy9vv6skiRGDkW8FbAuHfXPzViJZV46SRCu244YDfewjyi7hjS7ivbUKw5jsbD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=VAhixyIDxronvba-TluvJEfVNpmE-h2gMd8t51E7ySBxuOi3IazoFTE4Ra0jsi6N4NtcCfE-ukMqpGjn5UV6Xcu69TshR71voPFiAZDH5iBmpmjFkMr5nfYZep8-f5mmWPbqEmbj7vguvQoaxRalJzaq3uuz70hXTkagy1vcSOiiWuQdHA5luTkbERuXffMukM7YEy3VplpI6ChXsbwPD2u3dHVodU26yh88yFX86w0IwSWKQUBeTbNniaO-s07I5tgng_Uhgm_M82gyIGDvgziy9vv6skiRGDkW8FbAuHfXPzViJZV46SRCu244YDfewjyi7hjS7ivbUKw5jsbD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e1890541.mp4?token=WLM3mIqL8A6IcreADiw_gP8Jn-f4ikkU3nVCD0VbWZGhUcIUmQ39polKVIaEDzKg48qhWNbMrvAzeeoqPAQY5xvmlLuW85FHZ0js1hzKd5vuqJ1R3tFkGYNixJTFVWB-rcmPpa-WDCHQQBi3WDLO4Kgd4crCF97eLc_I6zWdaagzz0Lqhxv0twHt572xzBKVxg89tD9kPQxILxf8IWXyTyqCZ1NIwFR-yd_wNKdnEluLeitYTXaVG7aQXTEg5ERNXRcwyuqyCHU-Ox4Wc5YDKoc0NLiIFGsq8P6ztomdMV_c_8BLw9L0dFRe2nWlXqbyib7Ij0Z9AGqCEvunb_wI7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e1890541.mp4?token=WLM3mIqL8A6IcreADiw_gP8Jn-f4ikkU3nVCD0VbWZGhUcIUmQ39polKVIaEDzKg48qhWNbMrvAzeeoqPAQY5xvmlLuW85FHZ0js1hzKd5vuqJ1R3tFkGYNixJTFVWB-rcmPpa-WDCHQQBi3WDLO4Kgd4crCF97eLc_I6zWdaagzz0Lqhxv0twHt572xzBKVxg89tD9kPQxILxf8IWXyTyqCZ1NIwFR-yd_wNKdnEluLeitYTXaVG7aQXTEg5ERNXRcwyuqyCHU-Ox4Wc5YDKoc0NLiIFGsq8P6ztomdMV_c_8BLw9L0dFRe2nWlXqbyib7Ij0Z9AGqCEvunb_wI7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف گرفت رو تندروها؛
اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=YU8vhMNkHsTbbL2QOr8LqpcUjM9dbYakBZw9oW9nXDZlnXfpOm1pGazoR1e_n9bwu9PKSquHIV-SsKk2bxXqjMRa0bYbbe_g5u-JLQAStm_l1fytOdON6ZRmp5p2Vb8fpuUA-bBqReDHoqpfyoqLoR3eTqCL_sFC5dlHs4FkCgaXPs1d2qmDAPMLsh3EeW16xDfcO84qiMHkRzbZKhcOmEhjnWPgjUNOjp0pnGasmwIrBZTp01m94UbR8FJuoI2YGmAmnGQsi4jcvFe6fQTgKf-xN5Br2hX4-m_2bZMnl8XdQreYveY7Xk4AFwMzjq2Ei6Jb1yExobKVSayiQwXpvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=YU8vhMNkHsTbbL2QOr8LqpcUjM9dbYakBZw9oW9nXDZlnXfpOm1pGazoR1e_n9bwu9PKSquHIV-SsKk2bxXqjMRa0bYbbe_g5u-JLQAStm_l1fytOdON6ZRmp5p2Vb8fpuUA-bBqReDHoqpfyoqLoR3eTqCL_sFC5dlHs4FkCgaXPs1d2qmDAPMLsh3EeW16xDfcO84qiMHkRzbZKhcOmEhjnWPgjUNOjp0pnGasmwIrBZTp01m94UbR8FJuoI2YGmAmnGQsi4jcvFe6fQTgKf-xN5Br2hX4-m_2bZMnl8XdQreYveY7Xk4AFwMzjq2Ei6Jb1yExobKVSayiQwXpvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66939">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=esl9njUAoYewhC5__UsK6mG-SmpmUvpLO05M5OQlC7GcN0uGfQcN9P-aM2cippM0mtX916X9MZPZVxG7ILxrWhGRDhiaTWIO-5aFoPIxuJAA6XgdbOPlecBWBIzqBG65JFI1GqY6fvMluIkBkUUfwZwESaOM-PU6uNfkwhEVF5xxWvaI2jTQTv8W6Gc-tbL8DZ4ciG2kGf9Rr3klzip8kO5DnTULhzLg9QfkV64zNiuVwQjkHEX5j7U2Hh8rxpzwC8aYIi1jXEYgVIhKYYEU8iMy7kF8mBQafViFCz0nI-V-n7tw-bl1vd0TNy7icbscKW6Sr3G-0HRmLkWXIzYf-S4ntiA2_PXkr0EXgCUuWAxQhphgR_UrBrXyS5ixAsuPFx2Vk1nUeEtH91UhxPi_UuX1lZ1ZaUgVup2JWqsjpT95PRQeVkKq4miEKXv3Ts7U9LjnutdBCmmQMeIqwRi9PGiBQkFi3oJB9q6rfkIdA86REhGkX7qybYQqDv2H43epWrQYRihf4Y97qDD3gRX1JeYDoDDD3dYdkpYUlPAUCcAy_A-F4vfaD8ODxCSzoW7m3iqizhyc-n_gK85Ehyvo6UhQz4Jps_TAGZ-sgR0Q280XyqmSlvpOqt0rw0oO2ozIKtux9c5bhbIyhcqW2SRv2L3eA9fsYCWbDx8X-hIm7zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=esl9njUAoYewhC5__UsK6mG-SmpmUvpLO05M5OQlC7GcN0uGfQcN9P-aM2cippM0mtX916X9MZPZVxG7ILxrWhGRDhiaTWIO-5aFoPIxuJAA6XgdbOPlecBWBIzqBG65JFI1GqY6fvMluIkBkUUfwZwESaOM-PU6uNfkwhEVF5xxWvaI2jTQTv8W6Gc-tbL8DZ4ciG2kGf9Rr3klzip8kO5DnTULhzLg9QfkV64zNiuVwQjkHEX5j7U2Hh8rxpzwC8aYIi1jXEYgVIhKYYEU8iMy7kF8mBQafViFCz0nI-V-n7tw-bl1vd0TNy7icbscKW6Sr3G-0HRmLkWXIzYf-S4ntiA2_PXkr0EXgCUuWAxQhphgR_UrBrXyS5ixAsuPFx2Vk1nUeEtH91UhxPi_UuX1lZ1ZaUgVup2JWqsjpT95PRQeVkKq4miEKXv3Ts7U9LjnutdBCmmQMeIqwRi9PGiBQkFi3oJB9q6rfkIdA86REhGkX7qybYQqDv2H43epWrQYRihf4Y97qDD3gRX1JeYDoDDD3dYdkpYUlPAUCcAy_A-F4vfaD8ODxCSzoW7m3iqizhyc-n_gK85Ehyvo6UhQz4Jps_TAGZ-sgR0Q280XyqmSlvpOqt0rw0oO2ozIKtux9c5bhbIyhcqW2SRv2L3eA9fsYCWbDx8X-hIm7zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=pagtbWNGi06q7SvHMA92r0tlSAyzPgUIuzyfqLaysrrwTmlGDDwtrJLlJrwC0nH8Hy0HhSHaIEkOrbkGgwreOgeNHtgq15CRGyEBFRgVCGprCrKHEyZTPubFxIdh9mG6Pq3fscYIoL3Y8s_Vqv7dU0rG6SUk9DO7cviZGXnoHm7-3aApWuHvQOtBhoMkfmsJCLkh52BigiUIkujnf1UMb0KTeBfeseMR4VpX2VHl0ktjA-REf-pjw8oh-XbiClXFfhiTF72lXwHMoBYze6ZQscRM_9UHBxZDkXYTfVAuR1NKXK8LlwMpWJzYQAH-LfJE-mheDdn0yv3v4YvJmua1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=pagtbWNGi06q7SvHMA92r0tlSAyzPgUIuzyfqLaysrrwTmlGDDwtrJLlJrwC0nH8Hy0HhSHaIEkOrbkGgwreOgeNHtgq15CRGyEBFRgVCGprCrKHEyZTPubFxIdh9mG6Pq3fscYIoL3Y8s_Vqv7dU0rG6SUk9DO7cviZGXnoHm7-3aApWuHvQOtBhoMkfmsJCLkh52BigiUIkujnf1UMb0KTeBfeseMR4VpX2VHl0ktjA-REf-pjw8oh-XbiClXFfhiTF72lXwHMoBYze6ZQscRM_9UHBxZDkXYTfVAuR1NKXK8LlwMpWJzYQAH-LfJE-mheDdn0yv3v4YvJmua1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8KMrJMrSqeADz7xqtE1sehGPQyw16MYXOFOEDeoDFpfuFfBwCp0Jh_S3ztInHcyI0pu97wkNj-et4mza45BQLOgeB1MVoF3IcLcpu1il-Dxy_4yI7gqjcc1_S9-v0oFd2lchmM8dlijFIYV9K_lzegZ6qWGHDlOZT55SWrNH3pTlquM42F1vBQUX5ftlzH9m-iJJCNwA0lWA8dkn421XqtTsHUGnqrRDh8qjmmG7EphqualUHs4BFe3OYvtHdY2rsyGpffotgZwAqKpiXR9BpGMG5mTQL0iRyHoJoHGWBe5-ngGBWAnvm41R-N1VuV4vL_AFsV2-P1rmF5ugKWn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KV8yrRWd6bcOPlPLHkmTl-itH8illelxyH99UavFuI7Efgr99T1Bq7DGyeKYahg2tVBexklkpuvRBkzbZoSbbgsKUc62F2eTqOQHAr7zZJNswCCSmb3y0XnUEPNjtdsQdiD3khIws_TrQwYI8EzA3SUiBg-bUsYOQyTNv76lgcbOeJelrlg1Q18-Bv0X0lAn9-v4y3KWmrEg-WDUSv0udfe55wnZa6n8iHpmUVrL-xjsuqoZAsDID12-TSgnXyxELiHZj5rRFQRAX8PUZN7ChHYIFzZtRf-u1lfY70NA_ubwmRU-BA3ugEMBpc8HLGcVaEJlMwlCd1xZEEWh4o-MKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAM3pt0tJaht_Ro9SDqWpeYfByIHM2e3Dp-IvWnuviXnS6WfnJ_72Uftif7uCvs7oOLBeicX851YIoCcH7nWM-F6xijCgibwaUPAIDFTOQ3xjwa97MjG_4Yx6dPv9eenM75veWkAVPKcMHbxiyxijaw_r7j_4nvvmyBcnY2421-LkV82T4-xYJuJ4eBqulS2TYbvc8FTPxJkBpmsPPryLRbf_hf37zbxYzl3b9tUqZnzh6yuJL8Vde3Kh_0NwZpktVJosYYhb3Rl0jEtIjE-sbq28mSpyyzHhhO4R5gIFyjEWsFa7JUwg3BrCQb-43bco2ysORNIVCSQV4xfB2qw1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWXqgtVdeEtlH480L06Tcgx6i_FMRLuiiFJgJp5dA9t_1dd9HCrR-akhDqi2PLSC2fRod075ShkQpFZq8ZSaTTiK6WGfzzCvkLIRU8xVBg9p_LoZbc-Y5pvsgZOqRsYdrNiRC-8HaWNRjdBtZcGO6Cuej8f7ZFWXMW3BtXgaRk-wH5AxLZlB16yUdenBhrFPvA62JsMT4VPF88o0TTbja4zsSZrnIJw5YnjZfczrJCz6lU5nEJ8aroU6j_352vFYS9UBs2VHlnQM0duaL_c6KuWWU2CmRSOpLMMoUY1BEexjoWm5k76PSNSFe-mHgExnoZI0j4Xp8DYbLGQYuy9fXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quxvzbJAjYCCk7ecuy_ywPjqHeKQDxqHJ8BVnqc7FkU0kNqinZLdE82eZOMb3FO2eSP7GvPgrB7KXueTDm2OH0s5a24-2YJYyDkpRDS8gN4BDXrW_hDrpgy7warZOTxGUpedHV6ZpJM0LBbnb5zEDI20DfVx0V6vwrudPqfyGBRcEOtm6WQDrFwohpyGsAyq5PpNP7gU-Jwimf5bfVgDRsF8L_5m8pfguFlUN92dK3dbrcrmFkkRhTvgU5p3JpMB3WYUZ3lat2BUEHW3mupHBWG6xCVa25_XRvQj1XFVQDsOT7AVzJrlYo4IHfF--2-kY6hzovOFb3na_x3EJXk5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=BPdQu5xi-GjZPCuQ-jqOzv2g0mk9YVrl8ZUm2uscfewlr8zXFaFclcii6uVCvPeqWhGI5du0eGlDz-MiamlwFg_jh_q01Jv9N98zZgyEGwLiBfjVrdo-FUE_Lt9yvJoMK5Z11pjZKH3EQwMXyBEDv78DigQVKp_Dw0-rGxQUW7TIdNvUy6sosqmGhwjzU8mKWpQpjGNv-jGZ8pANqMZ_SOrGomOcIdzeMorANfLbqH3tvKsN1s9ymy-Gjh4Lw2CGNZhcQhvfr7yyITmMCMT5JRZxpJcQE8qJHsFIb9F-4NVlVZMTXauqdNXQHdRjvGy6H8LxaQTH2NKrJ15gqV3Whw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=BPdQu5xi-GjZPCuQ-jqOzv2g0mk9YVrl8ZUm2uscfewlr8zXFaFclcii6uVCvPeqWhGI5du0eGlDz-MiamlwFg_jh_q01Jv9N98zZgyEGwLiBfjVrdo-FUE_Lt9yvJoMK5Z11pjZKH3EQwMXyBEDv78DigQVKp_Dw0-rGxQUW7TIdNvUy6sosqmGhwjzU8mKWpQpjGNv-jGZ8pANqMZ_SOrGomOcIdzeMorANfLbqH3tvKsN1s9ymy-Gjh4Lw2CGNZhcQhvfr7yyITmMCMT5JRZxpJcQE8qJHsFIb9F-4NVlVZMTXauqdNXQHdRjvGy6H8LxaQTH2NKrJ15gqV3Whw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=bbalWJXusDVvu7Svt3osCUTP_EmeC2MCsJ48HAW8A08hDESQENvLi7HhqPNzT5eMmenMAO-29cRUdX5x9VsBdNMmQLwhRulLeaj62KMICXdS3MHJtD2hz9jgPHcm48YwuEcPcb28-0n4uLHEkmPJZDqB0XPQyQKzpbx6r4nyuTudCktOoh2-PkCV-mepIG7harJ0tjF8T3sAgcgfbBdWyNBVJ8zw2oEX9o4PvrpLujtyuVyNcGlpRRvMVzUR1YYWF6fCgs0Ix2JlVz480mFrmZZtraGP-ef5ntijsQBNZEUN5aumUF3s__DILN7vDJvDZLpcJ7aTFS3pY4KTbeaH_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=bbalWJXusDVvu7Svt3osCUTP_EmeC2MCsJ48HAW8A08hDESQENvLi7HhqPNzT5eMmenMAO-29cRUdX5x9VsBdNMmQLwhRulLeaj62KMICXdS3MHJtD2hz9jgPHcm48YwuEcPcb28-0n4uLHEkmPJZDqB0XPQyQKzpbx6r4nyuTudCktOoh2-PkCV-mepIG7harJ0tjF8T3sAgcgfbBdWyNBVJ8zw2oEX9o4PvrpLujtyuVyNcGlpRRvMVzUR1YYWF6fCgs0Ix2JlVz480mFrmZZtraGP-ef5ntijsQBNZEUN5aumUF3s__DILN7vDJvDZLpcJ7aTFS3pY4KTbeaH_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نفهمیدند رفتنش فقط پایانِ یک پادشاه نبود؛
شروع رقص طنابِ دار و بوسه مرگ بود.
عکسش رو از اسکناس‌ها پاره کردن،
و از همون لحظه سقوط شروع شد
و نسلی که خیال می‌کرد وارثِ آزادی می‌شه،
وارثِ تحقیر و فقر و چوبه‌های دار شد...
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=lwU8DNLGsBfraOIHBq3_lQFiWKJb_zkBSSRqqz6DLzDo-NxTvGpHS_xrjWBOELJ7OG3O-LxC9cxruW5o0h6RmBliOGruki-4w2XowzZZb_O7vGAvNyY1cSwYNhnfyWfDtATCPAZpoIFiKw0BeEny4fsiU7eapekS_uqbXfZJZziaZYI7GqJ37TXPy7jMU0vGGqwugiM-OqGYdMStoi1mzHiPow4yc0fmeKi6x3PVeZ-6ucBGUexOuPqG5uqe9kRt8_mnJkroPyC3rQIm2oL_R-WDJ4x27AyfZ259b-B216fscCk9yDFd65-MlRU79EFm0AYcn-qofa3XBgXa_6VjHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=lwU8DNLGsBfraOIHBq3_lQFiWKJb_zkBSSRqqz6DLzDo-NxTvGpHS_xrjWBOELJ7OG3O-LxC9cxruW5o0h6RmBliOGruki-4w2XowzZZb_O7vGAvNyY1cSwYNhnfyWfDtATCPAZpoIFiKw0BeEny4fsiU7eapekS_uqbXfZJZziaZYI7GqJ37TXPy7jMU0vGGqwugiM-OqGYdMStoi1mzHiPow4yc0fmeKi6x3PVeZ-6ucBGUexOuPqG5uqe9kRt8_mnJkroPyC3rQIm2oL_R-WDJ4x27AyfZ259b-B216fscCk9yDFd65-MlRU79EFm0AYcn-qofa3XBgXa_6VjHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krxVMbbD-b9Fwuz5FsKZYNm3kNf1p5lhEfLs70-VF1Kcg2WBkBzfKOssYd6S-PqKQpZtZAGXN1rBW6az7gcvP2VfMV-ADOhTaPteip8aY1MMIz_oaE-bK4qLWJnsbBh1oWAuvUeAlYNKnDowL0AJVZjHiQLVMJeL-QnU3fTpC2onudC2Yu-rl57_R3Ka7wJooaA7zrkae1DiLZ1s8N_eBKt_I7D8afpybqyk2VQFr04OqFZK_flbrl31s0FLIuqS5OKCBeqT0MYg1OOH-WMl_oQLWPf2QIj1w-mrS2CskYHYqNukBhFxyOyfDBdlCO6O8sTZzow5CPtENpsoAzuDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=m3lcvhFppsqx7nOibf1MH2AX6CoKq17Vlz0JbFbGJN0PdUc7Bpbmds0sLVib5qYHL1qqW_3zfrmGo-apX1ZBimtPDq-KI5mTyOh0VVQu4B4twLEpAD8FELD5tby84xISQ_PVXK7dd6yp7rB9BUcRYqNBLXiEb134hm7pDIE9PGaykQ8KakiE1JH7gQ7S-kqcAiDF9ZpLbOGqMxGcdwnMmdKATvAxglyAvveqrXae33msAfM6a3JAuDDSzzd65uJ6Fff-6dpK2hDVZHsNueJ24W0z_gLSI45Z0zhJq17R5JbUw1pLUpoP7oM2Bnm77IV5ywahH9VXG5PSTst2WLs4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=m3lcvhFppsqx7nOibf1MH2AX6CoKq17Vlz0JbFbGJN0PdUc7Bpbmds0sLVib5qYHL1qqW_3zfrmGo-apX1ZBimtPDq-KI5mTyOh0VVQu4B4twLEpAD8FELD5tby84xISQ_PVXK7dd6yp7rB9BUcRYqNBLXiEb134hm7pDIE9PGaykQ8KakiE1JH7gQ7S-kqcAiDF9ZpLbOGqMxGcdwnMmdKATvAxglyAvveqrXae33msAfM6a3JAuDDSzzd65uJ6Fff-6dpK2hDVZHsNueJ24W0z_gLSI45Z0zhJq17R5JbUw1pLUpoP7oM2Bnm77IV5ywahH9VXG5PSTst2WLs4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
صادق خرازی برادرزاده کمال خرازی اعلام کرد عموش بعد بمبارون خونش زنده میمونه و تو بیمارستان بستری میشه که موساد میره بالا سرش و با گاز خفش میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=GgEkcE6otmZrT3AjNBYYqaIQTfPy7APys7lJol-IgEeCQu0YxrsszG-mPJ9mgJDT73QCEXkGM-sAebkaYj-IGaUgbqX7evJ5iKk09UmOgh2X0pSDZpPbFmVluUoucVj1x9HoaYbtU91czJvxp9AbONMS-Q_8z0ub_5hnxl-we4GpRn8oo64bX00taDFeXXz1AAucC9LdvKaNwra-WRwH3wf2_Tx4Juo4ytYKpiwX9OUuqDlr_7u08ZtyL9DxoVsyy8dAA4EmoLOAg3lx8Em18uF6xJu8BlITLQoxGZg4g5EspbkU2sJpt_M2Hvjew2LCmo4cSCWRU0M4P-ligj7XrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=GgEkcE6otmZrT3AjNBYYqaIQTfPy7APys7lJol-IgEeCQu0YxrsszG-mPJ9mgJDT73QCEXkGM-sAebkaYj-IGaUgbqX7evJ5iKk09UmOgh2X0pSDZpPbFmVluUoucVj1x9HoaYbtU91czJvxp9AbONMS-Q_8z0ub_5hnxl-we4GpRn8oo64bX00taDFeXXz1AAucC9LdvKaNwra-WRwH3wf2_Tx4Juo4ytYKpiwX9OUuqDlr_7u08ZtyL9DxoVsyy8dAA4EmoLOAg3lx8Em18uF6xJu8BlITLQoxGZg4g5EspbkU2sJpt_M2Hvjew2LCmo4cSCWRU0M4P-ligj7XrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=thksge3Hv2N1-k4oh4a7n04qtYbdCBsjdXEo1ZZBsORx6KT58zcBu_u3DkopQv8L40b28yEDWUtxXfoLVo498-6tSguQeCeXlgtUiGl4Xll5xc8QEURtwK7nEKK-BC5M8XXbymPjrHUz83xycjtbZ9J7U8-EJugZphRuDfa-g4X4w8gY7Nn8qA6o4LhDLLCuTTi8J4RPO7eCwiB61bQtNBh8tgqxVbxAHALR-NfMoGPN_Lh35fBCbFIqotGoFevgK8vo10dPqXITY9tIWhevnFI4r2Ef3FgF8MAl3G8ydPIf7b2zO8MEvrPYk_J3K6UGSTgEx3PqtSwqxaz781oAig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=thksge3Hv2N1-k4oh4a7n04qtYbdCBsjdXEo1ZZBsORx6KT58zcBu_u3DkopQv8L40b28yEDWUtxXfoLVo498-6tSguQeCeXlgtUiGl4Xll5xc8QEURtwK7nEKK-BC5M8XXbymPjrHUz83xycjtbZ9J7U8-EJugZphRuDfa-g4X4w8gY7Nn8qA6o4LhDLLCuTTi8J4RPO7eCwiB61bQtNBh8tgqxVbxAHALR-NfMoGPN_Lh35fBCbFIqotGoFevgK8vo10dPqXITY9tIWhevnFI4r2Ef3FgF8MAl3G8ydPIf7b2zO8MEvrPYk_J3K6UGSTgEx3PqtSwqxaz781oAig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=XLfulJ4yLvKWk7dBQ8AgbM3h5Iplv3r-LIX0dhEaP7jLNUh7eZ8QfKa0-KINZSu53ODlhl62WYvPFB9k9ezu2dwDXNrdKxkPtWOs6NutL70mCP5fuTeA4La5OVB-7wPVZAS6bRrXQyMLB7mjPQfnSPSTXBas7xW1mrzT1RDT8WJYhFko70xGR-ozcGb1-bk-86cAYvmjjHrm4XgCP8Ib278aYNNsHLZ0g1DOZhlOzUYYTVCx7X2Ho_gi_tYpHWzQkXK-j-d8qZ659bN233KhR7v_q5SLyTVud_FvlQ119fWqdleabShvIqKK7aFoPEhvSDLkYFhZVj1T5wWSrvlcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=XLfulJ4yLvKWk7dBQ8AgbM3h5Iplv3r-LIX0dhEaP7jLNUh7eZ8QfKa0-KINZSu53ODlhl62WYvPFB9k9ezu2dwDXNrdKxkPtWOs6NutL70mCP5fuTeA4La5OVB-7wPVZAS6bRrXQyMLB7mjPQfnSPSTXBas7xW1mrzT1RDT8WJYhFko70xGR-ozcGb1-bk-86cAYvmjjHrm4XgCP8Ib278aYNNsHLZ0g1DOZhlOzUYYTVCx7X2Ho_gi_tYpHWzQkXK-j-d8qZ659bN233KhR7v_q5SLyTVud_FvlQ119fWqdleabShvIqKK7aFoPEhvSDLkYFhZVj1T5wWSrvlcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=B__oPwVIHAMh4iJW5hYctSkBUOZh7ajiNt3BgeBNo6WcQucmqpvbYA1wwoeaPmUhLytLTsH5E3jjGObZlM1ub9jG9eV2_bYbsMTYarr5qeiOQuauaTA0OPszAEKXs70qxbIrbbKM9a-UPJQDNW1Z1nLL_Px3w931nCQEsJ84ZT73Zha1b6pfpP_gupjrxcoQKkk9s7N5wFmYM29E9r88dDOBpbiB0XQtxDU8ls9lwHKxVvn14Do5t63we2MMItmy_SFfBIKQEoCgmEnPyKAVDWH3gyilDXoKU7SL8HDcg9_iUfryuov4-HlW-cQ7qSV3YD3Z-9Mb_Sf4gRr9gzGjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=B__oPwVIHAMh4iJW5hYctSkBUOZh7ajiNt3BgeBNo6WcQucmqpvbYA1wwoeaPmUhLytLTsH5E3jjGObZlM1ub9jG9eV2_bYbsMTYarr5qeiOQuauaTA0OPszAEKXs70qxbIrbbKM9a-UPJQDNW1Z1nLL_Px3w931nCQEsJ84ZT73Zha1b6pfpP_gupjrxcoQKkk9s7N5wFmYM29E9r88dDOBpbiB0XQtxDU8ls9lwHKxVvn14Do5t63we2MMItmy_SFfBIKQEoCgmEnPyKAVDWH3gyilDXoKU7SL8HDcg9_iUfryuov4-HlW-cQ7qSV3YD3Z-9Mb_Sf4gRr9gzGjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgC2Gh9lAPm-Sytlwe2MJTZn0rqvEs3J-UCCWAPQrj0nk6V4ZkS58U6al_JP2ND2Q4Y87FE0ldZt8J3Xiyec8Sxd90KdvKgTYbDcym4oF3igqADc03jFYzWqZNELx3H9ctOfbM09GKwN46UusthHhmknOZO1NuOZ7qrarPkPJdi43TpuDlFXA6WHTGhclawMrmnm9sDLQJ_73i1LTO03BacuYhZtnj4Rp2ZlM0MrmXAcU5WNs46JXijcKFYel5x3_ystu__2KakJ_jdEXMIi5ErfkKpMwou1vSqsJVfTKqF6ulhoD2JopNVfjzPh-TYPwHZVuRyDILZwTjHYX6EsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTs5JR1aXXhEBrHTmfNOT_qQlCt92QoPp_z6VsTp70s_DVlTXqIZIHCLjcz7zSkFbLKIpOJDfTFWqPyxG3u8o38jUJR_byDTRMgnKXz83XNSL91HZUm-Yb2FVgmZD3bkqp2TAwFEzJnLVC839GiQUaJrHCtbExrYmC3D5h20gzjTv6tmmdsObB53DT1u1NVWHa8ppnDm25JprLk4NCnk1oi4rEnCFl_KroWoi019jWFMRvtiGLGG5cwWFMUA7_TcSPsSHQKqCKEGlI-xdUdP5-xHLiHykGqY8NMjEtzathI_MaDF6L4oBmsaZNe-DzZHtOUIOPcMVxPvUV4relc94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvWRSqtPgJWEfT1gkr_wSEesoZpL8nGvhH4NcMUpsB31gE_Lyv85edsGJuXtiOXPZdAXipPfWsjloB1n5i1L472bCmQfxHOjcH6H67k_CGjgIwzkJpiGBiSqxH7BG9skAlyvVcQgL6QgbfoYbSc_6JEob2SPj3O7H8_4ioDTHhZNr_2vDJK-CXYnsF5TDavFFhYD1Ds7CI-VXq8Ic-QOXiaJKOembwg4uPE9hNeLrho8c0qi5-f7Lw5ck2yY_b6fGsaqUdqv5MslcUpiSZMhWlEmEfafS-QfdUPf4SdTy2c1rcjk9aDfdVTfZtYdJvMl-nkbi4w66FKaeqoG-H_r8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=CBCRfT0N9siJjsoTZhrtBdeO02m8aGRd63BPxcIGYZ3xjMUhadN5lmGvYtRwambAgQgI6HXFuQBgQez-1lSRlPZlvz4jBLvwMgkUfLlHVVeQfUgpDES6RkgQStzrQoa33-RzbnI9hubst28PrOVfAo5P7HVNJkYjWxw3iZazP_v74WBVk709HlXq1OPEINXnNWM6xcoLXbvTVe4vjpOTCMa4UYLQ4BC9IKCalnvllj6SY14HP8HGT0VOynkEXa_0qSlWpIz8m9PpoGD-Np-seuzisDQTBzkthwkLl3mD79km3s8cQoqcAvXzuSXwHRCIAiVGdp3Rk7s4TSCMBBfjUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=CBCRfT0N9siJjsoTZhrtBdeO02m8aGRd63BPxcIGYZ3xjMUhadN5lmGvYtRwambAgQgI6HXFuQBgQez-1lSRlPZlvz4jBLvwMgkUfLlHVVeQfUgpDES6RkgQStzrQoa33-RzbnI9hubst28PrOVfAo5P7HVNJkYjWxw3iZazP_v74WBVk709HlXq1OPEINXnNWM6xcoLXbvTVe4vjpOTCMa4UYLQ4BC9IKCalnvllj6SY14HP8HGT0VOynkEXa_0qSlWpIz8m9PpoGD-Np-seuzisDQTBzkthwkLl3mD79km3s8cQoqcAvXzuSXwHRCIAiVGdp3Rk7s4TSCMBBfjUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlf3k9TXdq8D44ve_uadCLO5tJwOJMbkafc9XA6e6ITVCvjqOgP4Ln681-ffb2P8hxEq9KPQdtfoictJbf77s8tFiz91JzG3to4o7cf58YM1J2cQMhc-0sFBHWoZXles4PGF3y172UR7QIN9zlGpSScw5vp-x7JGmebZyvScbzB_Ij2XIcWbCaB5SWDCER6GzkZsdJg14f_KImnxIA2u3jJKyi-9nr1qt7gFzxjiH4DDuDd2bmD7fpa1ZmQMavSPJnCVK5qDqzx2EBaWFlRV8Yp7saR38PHmjeJysQ_Wjsag2t6Kr69l5We61lfi12YNkQFDD0NCL0BnBNc4En3A_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaqzUMpLk7krhB4PtaJmupmutvwvg9KzWQWAMevE3-1YDKdK3D-Yk0Q88JinhH6aNGzDvbIWFpZ-6YkAGfcqHGWxjveFRPWzgRJxnRapO_QRDE_WzJkZM5q9hgc_UF_dWztxlp4EEVHzoAEG-Dnkqz8LNMqHVX_CMw0ifBDESFJ1cKBsgFvfVlgxoGzzJWnYxKmlEKGT-fzK7ElhmZmo0ZL1WYpsE7G1gwtZD3X2dfOciCNEuCieEtqHXwrec7dadAnm4HV25ITWfYqAEtAFD6dywevTvm9fOQDd1Q_BFDyZPnA3J2bGVO6V9Rs09mRDPEGSu2Obfp9eMEZZtqHUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJJn9gM8OEL-Wy9GzVzbXm_kop0eBm6ncb_RsketF2hyZE82D59rBZuX2DTCRAwl5lAx6bgykV23BhUPxBXz1Yg_NXFC3o53-wSYdp-T7iqzOP5TfM9BWIpPydXFF2aEchRdowAAJzRW0eT1KPlYWnmUDrYuq9HH3is-WWsCfqWyeGwL1noKgenMWLyt_UCaD1zm3K34Hr7wn5QQQXgo75MiL0_ATLhWGQUp_HKZvak2Sax24i0xX0xfJM77mHL15_5eqLSsPc-3Gm2hR5Fc_gvl-8v2Z5KWWDpgVKRGbThCIZgnyCZF-j6QWD99rZz4SFPKBwWfolhmZx3m2Z0rcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwhssOpsAVUQGHwhyDBwPs06NE61Yvgrbpsm0SIR_kshMblp5MwnTf6ltjO4EiQEzrgXXXo9G7FB_mLAVopRKN7pg9MBu0_W3PxoUxiitPdToU0Kg1cXvIhYfQvntRSYPBiBfI_eScmMpJr9BP2QZdi14VRMrPGpew580HtoqXbkB-KTH1mCTSZWLsbitGtlpOGlJ_2w-hGaVT3ZGxfBpeLJ9Tip0qdRFeeiuTioIQzgx7_vGK85FwrNqmUfVz-3H96WgcTewui2HW-xWpU2LEbCryTpvBmeXf9zmWoSmY0qIk8YWnFhk2nSC9ak90FXh76ynNdw0Bs7QnDgckYX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=NRCErFg3HSWJKX18yJqVGckup60i5rcpaR6evvmaA9ywzvmFvFtsThaaxQ_pFpVVK0RDPqbAyPaQc3TBxAEnBFYrGoH-EurCyB3H6VmRCzI3v2rVj8MQBuOTBjric01YsSiU19bH3b42te7RvkabNwRjuU8-J0dNM9tLXmMZyEdYjCelge6ul9ID_ayytpwxmHjmviNRveiQVnEIdKwcHHjQAghlis-wviZU_GowyFhVM0f4FAmKPJVDKHWF_cTybXHdS1w5cMysuVs8g1FXGv3DpIi98B84a71rrnlQbNTBe--s9oFaHfFmoXcL18AzHTRpMr0jj1iG6xhxtLjBWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=NRCErFg3HSWJKX18yJqVGckup60i5rcpaR6evvmaA9ywzvmFvFtsThaaxQ_pFpVVK0RDPqbAyPaQc3TBxAEnBFYrGoH-EurCyB3H6VmRCzI3v2rVj8MQBuOTBjric01YsSiU19bH3b42te7RvkabNwRjuU8-J0dNM9tLXmMZyEdYjCelge6ul9ID_ayytpwxmHjmviNRveiQVnEIdKwcHHjQAghlis-wviZU_GowyFhVM0f4FAmKPJVDKHWF_cTybXHdS1w5cMysuVs8g1FXGv3DpIi98B84a71rrnlQbNTBe--s9oFaHfFmoXcL18AzHTRpMr0jj1iG6xhxtLjBWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=Ysps5SssW-3_SPKxGGAJFM_c9Pz0vXE0kRL1lGWFYAzEslSHSV-jX7ExXVDNdpdXNhNBX9G_ZufYM4XnFaZO3ccaW4wub4w60Pd9I4ccHlHCPagDCEvnoRaPpq6r0Y7dJIFoX5lukSJJi95V1qLIkyfc75gTUBU3FaqjinL-IrlZ4o82S6ABWbuvLqioyAPLfDJYrpA1DkJTfQIUv0HIFjA0_TMph-e9pTHqOkquVupDRpNDKfFbadF_pDy_h1lLgPmq8byx4brBMbq3wRDcrK-D-52mn4zzJPCTZ-4MhZ1-TLqpLqUuVhybhXmSaeU7MqY3MqvphG11P5QNYy_G4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=Ysps5SssW-3_SPKxGGAJFM_c9Pz0vXE0kRL1lGWFYAzEslSHSV-jX7ExXVDNdpdXNhNBX9G_ZufYM4XnFaZO3ccaW4wub4w60Pd9I4ccHlHCPagDCEvnoRaPpq6r0Y7dJIFoX5lukSJJi95V1qLIkyfc75gTUBU3FaqjinL-IrlZ4o82S6ABWbuvLqioyAPLfDJYrpA1DkJTfQIUv0HIFjA0_TMph-e9pTHqOkquVupDRpNDKfFbadF_pDy_h1lLgPmq8byx4brBMbq3wRDcrK-D-52mn4zzJPCTZ-4MhZ1-TLqpLqUuVhybhXmSaeU7MqY3MqvphG11P5QNYy_G4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O_cE9SgDQd1pwdariR66FhFir45z0Gr-iyDRT_3v97G726nKHNm2TDxl2O_w1hRh6J49eYyt2WWlCPHoBE5sB19fAwMxU8ezJUoOJtmUzyZZaWts16TXOQFrhR0tkTyDZ1CjG6nSddg5V4TQX1GeUPt93TwmAJRbiO9eLep67jk-U2xNM4i33xnO4Tv3vNFrbVN_YCYKrgPS0yBAgYpAc9Ha3ZIm1gj9erV95cIXLKluhaLG2_pFWM2QOdmMF3wBHyryCD5steNk4fafPnDRkSRKlQq0HH96mVpqJf0JLKWfnXvAhw933Asc4TL6RriohdZuyT1Onn_dwVUQDJvgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=iI6MGw_Y3JTGQEFCiyy0MoiwsDCyqcpB_tUZDv1jEgJ-eDkfZOy2hmDzb2fF77TkBHGsdApC0UfhplsO3X4Z1g8hLVCgNdkYrVY6CcS77B8sr7BBghpIZ2WSJWOpZGjnbSrPFTOiOgR9l2Rf1S5IfNkhXfNl3N2qov9j4scFmXFexN_AInoyQ_y5LppeHAu-UJLUPtPN3mEYP5mHzMQu3gii50sWHFD18tLZBWF0Q1Anje16x4_9YS0mBzQaRTKLFdsIP-nIPeQl-59jZ7X8OO47E4L7QFWAntEyEU-LsiyoNDk6-w8d6xU6YBdLvq3aPdqOofptpfdhzj5STlUD9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=iI6MGw_Y3JTGQEFCiyy0MoiwsDCyqcpB_tUZDv1jEgJ-eDkfZOy2hmDzb2fF77TkBHGsdApC0UfhplsO3X4Z1g8hLVCgNdkYrVY6CcS77B8sr7BBghpIZ2WSJWOpZGjnbSrPFTOiOgR9l2Rf1S5IfNkhXfNl3N2qov9j4scFmXFexN_AInoyQ_y5LppeHAu-UJLUPtPN3mEYP5mHzMQu3gii50sWHFD18tLZBWF0Q1Anje16x4_9YS0mBzQaRTKLFdsIP-nIPeQl-59jZ7X8OO47E4L7QFWAntEyEU-LsiyoNDk6-w8d6xU6YBdLvq3aPdqOofptpfdhzj5STlUD9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2dJUbzTQauCO_ciIKS3yxYF1vuNa320SMxZanGwEG7MQgJzfkej5AKvTjcdnvBrV8T4RiKR3RHUl4ON5OGtKg_xgFiAmOFDc87VWwQFm6LyAtG3hcPg5TJAC0Pi2kIDAih5FLgWHt5dsajT1LLVb7pdieGGg25jKETqrStR79ftFIZaosNa-hRsQJP_hScKG23QTMe9PoIgmFoD3-kzninrf3ugm0NZfqjUAvm9SJK-hwiYVQO_G9T-_kptkP_JwFUTIvneZGTjs7Pthb1llfEMppwPRdIxMNlzHdSkiWxUeNbMvPzNFRMkeSB5Rp24vh4zNoNknBGeivlmfC7k4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=Y6oXxrOLRLkAJiocaNq4mynxzdqUUuATqyDnq2k25-NpR9Hs8M22fNRfWScscm3e9VzYYE6rqRQXw6ULZnPQt0cNEfJr2d_OsJXWMFGBune7kwh4hSotHxU6M6GmioVy1xctAVr7Mmb-sx3sjq-HYYDZjgaWDMQ3ug_WdaTpYph3OgtFn69ay6ZvpWG-YrPviKffeEHBYBCyJde1az0ohb9FU-v7XSfko51EvYTy4J5PTs4gdQrYtcEHN_gkSeMmZoMVoRYAUb8pla5E3soQwH3ECVo8qMGaKJGeqdzbswAdTCMJ5LdR-CRmIdpuWj37qmI-iJh8EvnEBvgCyXp0SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=Y6oXxrOLRLkAJiocaNq4mynxzdqUUuATqyDnq2k25-NpR9Hs8M22fNRfWScscm3e9VzYYE6rqRQXw6ULZnPQt0cNEfJr2d_OsJXWMFGBune7kwh4hSotHxU6M6GmioVy1xctAVr7Mmb-sx3sjq-HYYDZjgaWDMQ3ug_WdaTpYph3OgtFn69ay6ZvpWG-YrPviKffeEHBYBCyJde1az0ohb9FU-v7XSfko51EvYTy4J5PTs4gdQrYtcEHN_gkSeMmZoMVoRYAUb8pla5E3soQwH3ECVo8qMGaKJGeqdzbswAdTCMJ5LdR-CRmIdpuWj37qmI-iJh8EvnEBvgCyXp0SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTu82XpTbfI-slcQKtrwhgXnxShvPycpWOsKj4h-3MclehoYDeqPxrSGJPG-TO0dqkvKTR5wGUm-xyqeB7fbTE8AxZn2maySpq6ncsX499JnH595k7ZqbucdhJ1IDcBqjzKNSDiehS0_ZjtC8Q8wKODbZY36bQlN1AajzJAtMlkG_hmFTyP0GhqPpSdh9Qg3-8qb3tI44gg573ok_Ai9Rfd1aYoWuPR97ft4fbNSk-6p_oqsIQK3x5pfe_s1aKY_R5tHxaK7oo4RHF0NB_6WCCFvclYYOGOInBxEGERSOVHjWWL1f6idPriSLLLYZk58xCmMU6XMiyv7323XjpP1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=sp90W8nJpeT-QNUcvNRlsxXNNOzP2EMP2umdBWiErhq8A_PoGEA_uDvYNEYXDPvuL_lGTS9lNa19feDnfU5KTGhOeAYvt7G2q9jZ_e-4-zbADJQHSnZX8CqX0zh1vl97BWegT78wFI38x6ueMw1zY1LJQXC5srdGABfPbIysMlDcqFlBm0SRy3D2ZHAtp7GNDAykpi5Q9eRwH58gCefFOi_8C1oLAS6d7O0-CD_U4XPxcR5UuAToCEFlobwdugZTmoMd5lqxR9ImD59wUBZxbkVFY0VrzzoUQ8lyDRx7ZjGvN3o95cu7BhcETpksFLm5zkeJcTMeF2ouW1Pg7pYG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=sp90W8nJpeT-QNUcvNRlsxXNNOzP2EMP2umdBWiErhq8A_PoGEA_uDvYNEYXDPvuL_lGTS9lNa19feDnfU5KTGhOeAYvt7G2q9jZ_e-4-zbADJQHSnZX8CqX0zh1vl97BWegT78wFI38x6ueMw1zY1LJQXC5srdGABfPbIysMlDcqFlBm0SRy3D2ZHAtp7GNDAykpi5Q9eRwH58gCefFOi_8C1oLAS6d7O0-CD_U4XPxcR5UuAToCEFlobwdugZTmoMd5lqxR9ImD59wUBZxbkVFY0VrzzoUQ8lyDRx7ZjGvN3o95cu7BhcETpksFLm5zkeJcTMeF2ouW1Pg7pYG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=I7_8zCDLbga60z_CTdFUcnTwR3Klx8ORpp2amnfqYlQxOr2TbV_WOwLIeiIr7DkQh8c_gd-wKhgEKPzhQrsQq9IGnb9asdHYFceaQz6yz2dzaiB9oNd2hwJa1W2YVVKwqSPtHJty9glacwz3mSBZsR7o-W0nU4jCYiCMT0Avle5mtiTujAeWxTWPssghskbkFRcgwGGr-7TC_jnJaZeGetJtMTiVuaNBUQ6OC0avvSwib2kc1SNdy23sZbT8l4lARJWiWPKGQzldQAILDlCsGD1KFHGBD89LcRiTZP6hGPvPyh01GrujqCknodH5U_h2orJMEN0g32JSV-vadc7EEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=I7_8zCDLbga60z_CTdFUcnTwR3Klx8ORpp2amnfqYlQxOr2TbV_WOwLIeiIr7DkQh8c_gd-wKhgEKPzhQrsQq9IGnb9asdHYFceaQz6yz2dzaiB9oNd2hwJa1W2YVVKwqSPtHJty9glacwz3mSBZsR7o-W0nU4jCYiCMT0Avle5mtiTujAeWxTWPssghskbkFRcgwGGr-7TC_jnJaZeGetJtMTiVuaNBUQ6OC0avvSwib2kc1SNdy23sZbT8l4lARJWiWPKGQzldQAILDlCsGD1KFHGBD89LcRiTZP6hGPvPyh01GrujqCknodH5U_h2orJMEN0g32JSV-vadc7EEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZHtRpkEk7cNhGKRFRqNPEmccNHMw4AT2FaRzodSNh3WOcY2f4_XhxRwfFVo3YLBzStBQGmPvSbpdsyL8sAPZyA77Fg2HuYCtt-93OQfsvOTd0Moba0JjrYETW1AJzKv7kHKonX4qOjrTD-XtalXcLnO1XdNSJeSsECFY2XlqnMTUcKoRjyUT25cKcYi8hoiC1Z_WhdyWHurW7bcVDckpgdt7e_mC00TGvqM-yivthAHFyvXuLMjiXt7P2Gx9lSUjCUYgoTbtF3cXrff_UX6AJ4DjkhHGWt0cg7rlmU5gVGY74hKhDvEzOBZWov0RCpKq-sH9uyCyh8l__gSoBaUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=B0CjT_KAYt1ieLUWHMS-UKrAb0gga1yLuYduJVCY_Wo4oDhXIJiodt-C6X5ovFSxxYONVxnuEM4qcmFIerFgf5zsKPc03zxlmLkdQ4vO1na_bcUmV5fcJi22fxeFhX0gA8OMPwhSCADHutEQlJPi-gDaUbZSHLcPPeGaPOXizuNwGK4CXP9BWOpbjE3KKdLBDEIWpXFp7HjjRU-RVG1qRu3x5IicfkocBtFtGkee7CSjxJuQniZ5xEnhmhEtUOi1bt3AiD0_q_fFEW36D53LeeeoywaFTP7rkwBqR50Lz3zd-f-5k5z966HubLYjq5wq3EW1vUypSek6YY1AzEopNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=B0CjT_KAYt1ieLUWHMS-UKrAb0gga1yLuYduJVCY_Wo4oDhXIJiodt-C6X5ovFSxxYONVxnuEM4qcmFIerFgf5zsKPc03zxlmLkdQ4vO1na_bcUmV5fcJi22fxeFhX0gA8OMPwhSCADHutEQlJPi-gDaUbZSHLcPPeGaPOXizuNwGK4CXP9BWOpbjE3KKdLBDEIWpXFp7HjjRU-RVG1qRu3x5IicfkocBtFtGkee7CSjxJuQniZ5xEnhmhEtUOi1bt3AiD0_q_fFEW36D53LeeeoywaFTP7rkwBqR50Lz3zd-f-5k5z966HubLYjq5wq3EW1vUypSek6YY1AzEopNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScNRobec8veOSYHilS1a7_C-545tDuxbwSzKe461yw7Y-d4fZnI8y6kpxSqdxoZmuSEyIlLZTsdD9J7OgE23sMSAwsp1UqycZBNBU3jW5IpfXN3oNsWCx9l3H5sM-QGOe2Z_q8hnfWvXueHNENSZFyLMUMWCcEJuK6kX52vCX47ZijQIouZRodUf4DExqydIevEuApJ6Z5B5r9l17-weuDPzcwW7sosJG-R9hJwGDBXdiPDqjwp_SBChLJf2L9W571ApoLV6hiwoQju2QUhn7UzzMqM4YTdtMr32mTeiztVc35g6sl1f0N9ohDNeEo9I9eOaL_bwnAJk2mIUNIaUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=sTBeIPVzU_umTukhiIrRjz51sL9fDL-OgBdgom1iu0PAXgI-jjnak4uknCHwmexh4ANFm0xG-j6sYyePx4J6UfwfktPDPozvwCTFGvQZsULNh6tVETmsIk3t2JvXfKYsCRyoZAXmXnCfSE3ynMFyUfMr2Eq84NjZJM1e_c9DaBXli-3Uxn1jFdAjL1yZnX7pcFo1vx6nWFPDCt-GGYC0FPjucqY6WgjxcZhcEtv2X6XtO8sfKw91KB7I71BzLUhlQ5GuqLhZKBGT6EM9IJaMFuvo59bD9tLWPk8fPSEI6FAV5Ehqvk1Q42f53lD7xAfX-6FfCd27lWCaa3sGdyglfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=sTBeIPVzU_umTukhiIrRjz51sL9fDL-OgBdgom1iu0PAXgI-jjnak4uknCHwmexh4ANFm0xG-j6sYyePx4J6UfwfktPDPozvwCTFGvQZsULNh6tVETmsIk3t2JvXfKYsCRyoZAXmXnCfSE3ynMFyUfMr2Eq84NjZJM1e_c9DaBXli-3Uxn1jFdAjL1yZnX7pcFo1vx6nWFPDCt-GGYC0FPjucqY6WgjxcZhcEtv2X6XtO8sfKw91KB7I71BzLUhlQ5GuqLhZKBGT6EM9IJaMFuvo59bD9tLWPk8fPSEI6FAV5Ehqvk1Q42f53lD7xAfX-6FfCd27lWCaa3sGdyglfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4N1uMPJIcbVwa-SRWsAhaDIxtJTdd6bwYBKjM7hJm6YaJqeSCEoeuu1mAStj5jRQJOKUOMQ2BLCDI3gIp5VH8dYtwU-ROQ8au4CrDZn98r7NWqegSx087PeqyrlplqwBnWIOyFlUW5kKlH2R3MMg9t9E-mr9fWPwp7SZX3qrDV7XnnI80_Qj2nVbHq6QLncwLrL2lcHE6jTleW0dB90C0vcHqcU0v9mCDyq2_gtzReWePI4akg0WTcuf4yapQC4sVpOnxprKTPmK2ZoIedivLEFH9FgIk8aVV8pJPcMUgwa7Qju6ryd6zlZ3tcBmYrb7nHOlTYqZ7dAM_j4dQOSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrGpOuA6DGeUw-cnI5OkJ4Q8FiO4rDEVIzBIgfXAQPRszTXG8cAqjldQaupBwQIu_IWJIjGH3SI-TH9H0_bQvwjDr2P23lq42tniCIU5CbrQIq70tOzDjU4eH8MQJ7CY3MKDwnT3S7R15QSBbZU9LK1CnS3sXm_Gq1yOuo1gIDoOrpMhIaCdzpu8SDA11dWl04-reDnYG5k3SViZuF3wrOyyUWHQHItTt16KUiPSom-yXHTcoYgMvgcboZrKfb1tOeyK00zDoN55dk5yKKINhFwD4zKUV_Scw6xPWomo4H8krE2PF0JiZQK3VgfjS3DXejSbESe3UyjdyBrrXn8eGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSS3TkWW6dbHIQWQYPCgr5fZdF7SuaWXKpvyS-AOgHHaY5_b9hEPdix3Xl4IAxFtkoZfPxrU49bu6sjyib7binbYtdEHmh9wPYPxjrUPj_-9uNGX3XlEriahA3UhLRYQh9UQQAF0kJEyoAcphQcopMVR3J4VTOmuEQn9VAU9UIe9mNfguSbgcbZCaAC3u2fCU38jnGJmW5Cf7dZ2rEokwVSvwhd0XVQYaXmmdejVNivY3zEfBf_pvY4imCcQ6IlKtsjtMH4rJs_3EbFgnOGVIBi5KUABJ-Q3TNV0v4g_bka4o1iBCX6Xe65LuuL347VPtdBPJJ9UsK8XS0l6JCzZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ysbkf05DPRb4xh_APpUOoCtmcCGkXBw9cMovdKK82B0Qh39Kf-_iWiU5hAHqTYL7D86w7sQFhaMjB14lgBEwVe836g2obfTPQMti3qKjPcsyNIXcwnFiBCObJKQduooO4ToXQU8XWP3-eaV26bAPXc1WyiDpFsW8EVbv6Q0fsl61ulDHkpZOpemsFcHEV5o_d3NE4gqqwD8D3Lfj_al6ONTwIxJCN34JNLgr_YipUYJyMjEWwwgwhD_T6EMGUg0LXV1HR2TYGAbIf9m_Jh2_L1dwmUdhoU31MRSm2bJQiZjuRmDfMEvV4wjlmaCUwvmC0AHYslb--83zdlutK7mAUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKyoGfDJCZrrmrRch2bhyQck4LjVR2aU9ox9cd9739-4xNBWeYu0PiS_tvGL45CcgWCOS8-c-wGAJcgP3OFmHdJgyNuObaLhh2O-FOg0RIScGTzx4LLK09O-07oxtLecEstOrNeOdkfNH61f1xQaZOyKrUkGiDgTjQCG1NFa0M_jm9_XUEWp_gpmWaqEDVE-u4CnfZiYgdjiIXQENg5zvb14Jlnf_P8kH9eGJ1Rbxv_zpfGHmoSblo42Cq2_dVFcTs62HnPciD1EkQWFYcmlRGYX03qGXXQ3L3S1i0cRp6KL0wXM12O8fuOuS7iyFzqS6qGFcmGHFhjUXFSploCYcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbRTnz0wMswVCnSUYoZ-u6cJ5YXUkvEbJJimfvjJccRfSD62NEMvF18m2QGVsqtmfpg6wud5AHvVSPUMc58amSpJYFeX3JBbseboN69cMpotf1VZepg443OZY0r1xfHFejaAZj-evVQWDD3sZ7JZF0VaUHMqE9Ok5zMnxG8nZsZcctEFMCU0IjZcZ40ac_Xz54ojPUxgW6m8UZ0G3tR1-8QJOJPly6DtM8eVVgZdy0ljItVtBBpzCSMqktNy2fVTLSVUFNqCokM-bUMBp2xZuN3iJch9bg_dJ85NesikcBfDSPhB7EsMZy2E1F6VtGgQ4sN040-igys97hyGrtC1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emJmh9g1N0nvjnKcbZUR_-gR7dIC-9gOgd3b8h6VjLnW4JkK0_2xM4q7-0EWysylm91-AOr0GbRvZ_1JHxXp9MhfTciSNoFrTAEDkaqfVrGT9jyrzJ_Du1-xeSqNCOD_ZzSvkpHjkd73-dmkn-qixJWILDgwu8VJrXQJRxm272hn5lhpI1SaPU-nrSlvko95M6DORr1Atd0em_0ZuQYU29ewbcUnpvFB5i-L2bYoSsW9YISrk9Ji_2cY-q7EwxzgfT6EW69bB_k8une4xVw3ZI8k867p8E_vazH7N9RrOhsMGH8cbNKfXVaAJzPP6JtnOC0Tz8baK5G7bMZc7Zg-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=HE-DIKY7MbZpDSmcqjKIgZAy2CrNOYe2oT8Ii70eTpxK-qL-LmDkNUonI5z9iloe1wjC5fcdWMSF_HN4vgrDC5obfMQ38UfCpbwFFMzUqc6-dGy70jlOrU9qxxmApdAdCm-PYDdwfO5TBeGVPd3CrFBenFt_BZ4-7GzpN3S_ViWfs_PLOXWJpRi1p0X811_6YprMSJB4E9R4Z8F8tWItdI02kL3hjJjDmPK1ACJhgBlcP6YtxWTYFvjSRv1EUqMVtjfSofi9vgjAhiUOBnTBQ51k-bQgw1YA27e-W23azRHf80Sg1N287HEEqBV8_afgZTbBFgSUnfpjY6J21MvHFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=HE-DIKY7MbZpDSmcqjKIgZAy2CrNOYe2oT8Ii70eTpxK-qL-LmDkNUonI5z9iloe1wjC5fcdWMSF_HN4vgrDC5obfMQ38UfCpbwFFMzUqc6-dGy70jlOrU9qxxmApdAdCm-PYDdwfO5TBeGVPd3CrFBenFt_BZ4-7GzpN3S_ViWfs_PLOXWJpRi1p0X811_6YprMSJB4E9R4Z8F8tWItdI02kL3hjJjDmPK1ACJhgBlcP6YtxWTYFvjSRv1EUqMVtjfSofi9vgjAhiUOBnTBQ51k-bQgw1YA27e-W23azRHf80Sg1N287HEEqBV8_afgZTbBFgSUnfpjY6J21MvHFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI_qLk0-ri0Qgjh_fuZ8O2py6oBHQlLcbP4ZDcyDcEgjKH_tJ2-WCMxYentwIH7jColVykifYTVW5lAV6bepFoC79SOojehEEvs3spizwTAV62j6WigUY2jAQTNyVhdPlS6zrFjelJ_qwnber_bSef_3-1ouFLF6l8khVtvxcO_g_FvbfGtO2K7folgDCYMvS4vMfkW9gRAG4ytVHdd1J-Ph8mWLu7RyOZ7FnNCt5RJneJJu3GgHfPiOMrrnZc8bhBsLXmn0H2k3ZJJiWGicahOvQztmL1URbvw7aHDRnI2WXDXp9pMpLfoB-OUXeZo_v31G2MxRzdP6JBTgE0R1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=pisCPR3CBOGNVN7OsejB5VoTcgOVAkXLYykEV5BNpNDoqukFutCixB_sCG1xSJxEUWmLwciGqA2_QU6NuqKPC5lC0Tx3yqN9EL-J8qhVfLl52Y5cO_EN3_WgfybzwXO2sbO_18_5VjMP_lsfuAE4VWxs4S6sY30CvushB2yipYHfa75yuJC5hgXWv-TcHy9NSNDmJJkdnbtkL-X2lXYZLzc-URgg7LXdkFSUMnP4PWgEVENTffip7dEb4ZbF4cvcVVpuQAjHuEuR3IYgUYzLGyUe6W3bPkVicMbiz-TnUUEFbfO9mgqvWznx6lySInsE5TjW7QNiMD8R1nTWJbQEgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=pisCPR3CBOGNVN7OsejB5VoTcgOVAkXLYykEV5BNpNDoqukFutCixB_sCG1xSJxEUWmLwciGqA2_QU6NuqKPC5lC0Tx3yqN9EL-J8qhVfLl52Y5cO_EN3_WgfybzwXO2sbO_18_5VjMP_lsfuAE4VWxs4S6sY30CvushB2yipYHfa75yuJC5hgXWv-TcHy9NSNDmJJkdnbtkL-X2lXYZLzc-URgg7LXdkFSUMnP4PWgEVENTffip7dEb4ZbF4cvcVVpuQAjHuEuR3IYgUYzLGyUe6W3bPkVicMbiz-TnUUEFbfO9mgqvWznx6lySInsE5TjW7QNiMD8R1nTWJbQEgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdYyOkD2CcQB6oU_wXbvPo5ao3cRQKCg3jyojtYIvMm0U6D5yaCueUx_7GYoGSF7XYbsPEL8lu958QqhgIVpQCaHrAj0EDQsRIMl8zj2k6APjxZLDmq8slKXWd3RLjrPUIa4TYpHWKr1NWQZKoKnv1yCQRh-hEDnJuXATpdqjMvwEd-MjLJYyUROiC2TyOCNjmcScw7WhXacgk8nR9fwD-gSgQnfB0HNChCO3yaXA7sMJWlm34xmfwG7x8UqgCx9KNRxhzkJbMvo2oBAKMeJBZBBf5L2t8_03df9XX2G_pNcVaeigIf73TvBYa4ryRZyzNVQ9b-K_X5cRQIPEXWkXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIW5Ew9T9DcNqIotiRqNKBgfdf4ZCwu9iXVouRkGO46I_p1mnhopXkjZjT7zKchzzojTAWSkimxEyg8G1TITPZTeNnxpHzptbnqmmv0iECPA8JlMncA4c-TaZ-xcCijTvTuZY7MtdJxRHfGF-gpXlSWvnfjf79jvRz4tIvArqMgjDEYfnZYqD7XjIiqNBqNlmzzo-AIaSEQp-tqpK07I3214dgUz2ZKVtASVmoWfFAFewkUSIZ98Y7wbjcNYGn1PNssHkJ8Ad_aL_Yv4DVGI3lUKCTMsMfGZ76nftLjmp7lMSG2FDg6mjfouGUklj0mj6krFcNtkqPDK3JWcYQO7dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=MHKCEsMLv59st073Xx3YCvIOw7QzkFTPbhnjwe-mUT_E2ZGHY9Aaj8M_U92v2sRQvaNVOYIJehnBy20IbARSCMkyiiPmLJv_AQYvj8jTAg43ZTsNeHdRS9eglrmOxMKwEg6REUL4bRp1otkdopCoaFcUH8hYZY4qetlv3MZ71qrH2-HLgCEQMxdS1MVygjSPpYeW3JPCMDvrxx8Btaj1VqRRUsW69Bp7A2wcRG401dWagqBwtWM5_ghzPGloiwVqgL46OUiNEidvpD828Vu3NDmdpk4hJgl3naZqVqGHiXezw4MQhFciGdi3F58YdnOF0AbhjUDefCmQJ8Kbx-X2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=MHKCEsMLv59st073Xx3YCvIOw7QzkFTPbhnjwe-mUT_E2ZGHY9Aaj8M_U92v2sRQvaNVOYIJehnBy20IbARSCMkyiiPmLJv_AQYvj8jTAg43ZTsNeHdRS9eglrmOxMKwEg6REUL4bRp1otkdopCoaFcUH8hYZY4qetlv3MZ71qrH2-HLgCEQMxdS1MVygjSPpYeW3JPCMDvrxx8Btaj1VqRRUsW69Bp7A2wcRG401dWagqBwtWM5_ghzPGloiwVqgL46OUiNEidvpD828Vu3NDmdpk4hJgl3naZqVqGHiXezw4MQhFciGdi3F58YdnOF0AbhjUDefCmQJ8Kbx-X2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=lP61JhF1qi1BN9n5B7EIH3BD-GHcw1F2YmpQ6KcJK_pB-zi40N-xzAjnM7P_aPRyULKO8IbSp5MGngCKEGgBOTmbRKdwCyMk7bfAxW0bPiwStjIgM4wXAB-EYy0PG2mvoNpAnIkhsZQjnpmlx479KcU23YE52rwVWAJCZc9kIMDjaU5zyjOLHVjx5I_SlqH4uAPk1ytdP0qJ58ti4qGp5_mVhVr-ViTKBn2ikujxw5O76Sl4LG6mmY6J6kkIs9apSBi8Ri0DrZCHqfTUslFtZvSu_72iMLn03A7IBStIUAIklsrK77H2SkcPh7qOpFZDo2cbRL_eJ8q6owCwRwKMkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=lP61JhF1qi1BN9n5B7EIH3BD-GHcw1F2YmpQ6KcJK_pB-zi40N-xzAjnM7P_aPRyULKO8IbSp5MGngCKEGgBOTmbRKdwCyMk7bfAxW0bPiwStjIgM4wXAB-EYy0PG2mvoNpAnIkhsZQjnpmlx479KcU23YE52rwVWAJCZc9kIMDjaU5zyjOLHVjx5I_SlqH4uAPk1ytdP0qJ58ti4qGp5_mVhVr-ViTKBn2ikujxw5O76Sl4LG6mmY6J6kkIs9apSBi8Ri0DrZCHqfTUslFtZvSu_72iMLn03A7IBStIUAIklsrK77H2SkcPh7qOpFZDo2cbRL_eJ8q6owCwRwKMkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=mqATysasm6HeU0klLoWDKiCyDZrc2ZDKXFqkpM-beJQ-CJA8b7iPZstD8Y2lUACCn-xVM5TGcwOAwfqTALA0hpRH6D8mcooAAaX2ilRkYQgwDp4YrZkqoXCogg3b1AubB5IAiPbjd4uojDyiyvo0yPUZ1g7P0GJdLCipaE0QexH8-V3H_vJNiwXBUxwFCp4qtiWlj_v4ATmKaFcY47iCZ1iA0vRBytXO3A7VvqmGnVL1v5ux0-LeVI6RKtmvNUqaBobjzC1kQ-XDROWuGT8PPJYUqt8Zu4_fiBf-2MtqrgOrrH8GFTx3TkNQdO_0lh5uGjBgNvBcDALvfKv45rubdRYlmh7KTb2JExap6Ary2h6OgDi9cOLhfFbX6akGhqUX-nGjkR2wsrSyTI5NNnvXSoB6OiJvPBJQVdfK8fhin1GCknuRQcmtXBnkd9xtehz0iVnfVvFrTjRlatyIPfDAzrk4sknmVHtcg1i1esYNv_um5bvmWli5SKrnEPvkj1Xyc58xDAC0lFhxuqtf5x_2oiDIYRMaNBet_TgQ-6m4WHvRKPNZLyDcwquVN0jWLl4Sf_rGwJHmudoETsg6sC5pFX-VwPLk8i9MkAYbU-VRImgb4q55xwuQJN1l1Gull0VKm-wp2wnZDwjre_qLGYgbZppJ9D7lmOVGz60KM4JbDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=mqATysasm6HeU0klLoWDKiCyDZrc2ZDKXFqkpM-beJQ-CJA8b7iPZstD8Y2lUACCn-xVM5TGcwOAwfqTALA0hpRH6D8mcooAAaX2ilRkYQgwDp4YrZkqoXCogg3b1AubB5IAiPbjd4uojDyiyvo0yPUZ1g7P0GJdLCipaE0QexH8-V3H_vJNiwXBUxwFCp4qtiWlj_v4ATmKaFcY47iCZ1iA0vRBytXO3A7VvqmGnVL1v5ux0-LeVI6RKtmvNUqaBobjzC1kQ-XDROWuGT8PPJYUqt8Zu4_fiBf-2MtqrgOrrH8GFTx3TkNQdO_0lh5uGjBgNvBcDALvfKv45rubdRYlmh7KTb2JExap6Ary2h6OgDi9cOLhfFbX6akGhqUX-nGjkR2wsrSyTI5NNnvXSoB6OiJvPBJQVdfK8fhin1GCknuRQcmtXBnkd9xtehz0iVnfVvFrTjRlatyIPfDAzrk4sknmVHtcg1i1esYNv_um5bvmWli5SKrnEPvkj1Xyc58xDAC0lFhxuqtf5x_2oiDIYRMaNBet_TgQ-6m4WHvRKPNZLyDcwquVN0jWLl4Sf_rGwJHmudoETsg6sC5pFX-VwPLk8i9MkAYbU-VRImgb4q55xwuQJN1l1Gull0VKm-wp2wnZDwjre_qLGYgbZppJ9D7lmOVGz60KM4JbDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWRmj0ZgUOAQTtakIJ0d_1f_za0NmUxr06tFtcfJzDCjZLXO8iS7VjY5SXVHOwk5VZn82eLhTTXwMnUB9JMuTo2emmWAczCw73od7FBGpiLKfMJU7KpeNGZJeiYC0wS0uxTEoZZYEmfIiWuTia6qA4kYb-ixCgbgk9mtIFg2U1f8aKvjBAttqyWxBGDDNmoK-Moq0VzKdaVc3qjLK1i_EcpTwBhrxOFJvAr4aMuvH-5b1Mx2cdVBUsGaLHgYBJdTiMa2f2V75hxCBpdaNj7BTTO8q6e_1EYw709eyGCTGUbzsVj9E9XSuE3JIEjccBl2Jq0b6kJfi45mnUMr7UrM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=HVhPKtl3gFaSctCWx9RTVNcA7ITwQMfE63nGZhKEiUE_rLscLLm2LB1mD7GCE5qW7FXDaZwxIUt4CXQFwCvps7DEpTVJu8EVJXdjq8nowP0iWT2EieErwg_i1eS86OphauSKoP78aSGRWnS6tBOY40DjrahopdGWElwH49sk1kTeU8GFMmbIQgDUlZz2Vm_0cGOpu5QVZXUM_kALdmkebderEHekI2fKJaMsA7miKuYGbnC0Pp_ZuLhWRA5WRgfMiv9QkpymxxLl7ASVXfmEAIWwiQC9TcFxNI3b42eSDtd6HpJ2zFVAxLUrol6pOXHyrF0LM2Zy0X57c8rENBb4vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=HVhPKtl3gFaSctCWx9RTVNcA7ITwQMfE63nGZhKEiUE_rLscLLm2LB1mD7GCE5qW7FXDaZwxIUt4CXQFwCvps7DEpTVJu8EVJXdjq8nowP0iWT2EieErwg_i1eS86OphauSKoP78aSGRWnS6tBOY40DjrahopdGWElwH49sk1kTeU8GFMmbIQgDUlZz2Vm_0cGOpu5QVZXUM_kALdmkebderEHekI2fKJaMsA7miKuYGbnC0Pp_ZuLhWRA5WRgfMiv9QkpymxxLl7ASVXfmEAIWwiQC9TcFxNI3b42eSDtd6HpJ2zFVAxLUrol6pOXHyrF0LM2Zy0X57c8rENBb4vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=O3akffez5Kr76zvelWFa4z-yf0f-AIiVg5GjBv5R08--1y1S5Ia9VJqEV0rIJhpVNhZJOCAfBFfIZmoaNxADkpw7oOt4cEey4d-LoBV9pwGJ0m2QavBPsk-z8zqJ8aG-PAmxJvBEy0SZMkhxIY_cbKwp0tqgfwRjR0oMVYCpx8Xe-GdO5KtMUMFaF3jTgrzKcQHSye_P91Gd7xAhPn_UcZwzB4qoDGUpw63_Zf-hilTU544-uyAJf-WTkCMlU-wF-yBdggZq8Ss-D5PsRz4ewpr5LOvLU3HRdDeHuuYNT0LVap7Y1K6isx8dAqhfjW0E3NQ7j7qmub8q2fCCn2Nu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=O3akffez5Kr76zvelWFa4z-yf0f-AIiVg5GjBv5R08--1y1S5Ia9VJqEV0rIJhpVNhZJOCAfBFfIZmoaNxADkpw7oOt4cEey4d-LoBV9pwGJ0m2QavBPsk-z8zqJ8aG-PAmxJvBEy0SZMkhxIY_cbKwp0tqgfwRjR0oMVYCpx8Xe-GdO5KtMUMFaF3jTgrzKcQHSye_P91Gd7xAhPn_UcZwzB4qoDGUpw63_Zf-hilTU544-uyAJf-WTkCMlU-wF-yBdggZq8Ss-D5PsRz4ewpr5LOvLU3HRdDeHuuYNT0LVap7Y1K6isx8dAqhfjW0E3NQ7j7qmub8q2fCCn2Nu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=mcQaWO2t2JxwcBjg4Dy7VzQAKoeXV9MlpKUfjkf4d1p4r5axHugolUD7xjf1ZL0ftojdmnAUDTw_H6Ij422-dgzBWucw96Qgyj3NaA5GLBbtCiKHDO21BLYlo_OFxVL_owIXSAVXcA4qeNuXn_Xyrhc8SVtDpcq3Qsyua4O6mpxrwRnxeDCwoQIkII7yXUiWEEEbbDb24l6Ys78CnJ4TIns6CqIyllV4qKa1wrmCGhuT74Bm8otGfum4sCrvSvYj70Ur-FvXlIA8iL-CiemUhXZ4U-B7_PyDs_pPS-qlnevVB1HOt8IpIynvKrJ7V9stvEfS-eT_HcHAbCUrH6eArA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=mcQaWO2t2JxwcBjg4Dy7VzQAKoeXV9MlpKUfjkf4d1p4r5axHugolUD7xjf1ZL0ftojdmnAUDTw_H6Ij422-dgzBWucw96Qgyj3NaA5GLBbtCiKHDO21BLYlo_OFxVL_owIXSAVXcA4qeNuXn_Xyrhc8SVtDpcq3Qsyua4O6mpxrwRnxeDCwoQIkII7yXUiWEEEbbDb24l6Ys78CnJ4TIns6CqIyllV4qKa1wrmCGhuT74Bm8otGfum4sCrvSvYj70Ur-FvXlIA8iL-CiemUhXZ4U-B7_PyDs_pPS-qlnevVB1HOt8IpIynvKrJ7V9stvEfS-eT_HcHAbCUrH6eArA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FiClrAPPouU4TTvvQXo8hv6v02MCxKvHtnVgfJtLuwY0j2z1AvkIa_gidrz7GYzWbqbv2jLMGqnaFhqwG5df-KP736kYYnFl1wu8geqDLbtCIlu5AbGgt0WjzuN108Pujvc3Ly1YAxO9UPGOeRME4AMjoRlgGaJCsPs0tuPBC5ILqGCrlw2GmqYTrYSGhRx6CK9eeRLq-NPtI6zVy6bIYGlZfaCwtpO7uCckdjCoKiqOuT3wkWZCTX5pXIM1BXkTO8sIfhsrg8jy02FTNs8PSyQjeXEtaAm-dPH2ls88ISwIC-sY_HYUoVt7kLwv4Ktidr7s3YqMCIYfNQOZQW4pQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndONf3z42nbIX9J6yY8hBuFWN2YTT6fyJUuJRcMbClDVOCsMDoNMElottNh1nvm45D8amHdUncEuKYv1qoz4NIPprVVk22gCg0IjV_kwyPymow5il4c3s42bf92IXwB11WwLKMhngnHpmYg52JZlOQWeWuvOFTXf0jfJGo1Bbn4sGi2XK5gtIEAyqKYlrhLQSlGzduEeJsWzaFHqpQiCF8apuMXshxyi7K4DhRs7Evmh0Cw29JpyXQMONAlflXDb5yRrnaGUETyiUHuP32-X5vuv5RdO74JU2p3Tem__0prTIRly7jcxWlNkiPx8XTwq2ZkpaxWheGk6VUIkC1gERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5IJ-0S5zdd4PdGIwyZnOkkuV9vX3mcxEWrd_48cp8OHHP5yx_edVDGtJIMBoAmOhevnmfqvUOyB7u4xdDm-6UkMV9kBvYGdBmHXUQVp_YIbnIYqqewnQvFBSLQ9wFwQkvhZ5hCaEDHbVMycd-rt948caTz0kwoEjhu8ISbYO1Rk2okMZdeb6AH16IhgzjDrISXIB43ex3EBwACU9Y1q2TZHl0JgiOb699j8VeKge5vuH9UTqJBAoLVtiauPi_J_tLX0gW794h-a-c_Jr4-_0MvrowjT1bttEhe9HA_tvNT-BpmKRe5Kw9a9vBqp-qokylV7doDZZeMoQ_6rn1myKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=r5utqHgEfty_rVvRfc0GBnnEVDywwOESK3NcB7AUCfnYRI-wySPKqyn0INeROhaHggu2LFage0TuP6-GNIo7Mpbg70ywBP9yAAU0evnDhwOkmFdP9Xhh4fUBosdqu5wHNYb6MnlcaqfAyaQUD9kEZKx54x3HMOvwDn_fm7a1sPnvihbRSMZ_dUZZ--4jxUQBNhtKTThBp1MsEnhDnr7Bv0fk-oQ-PatCV6dx7jNDyh0DdOHcjZxIuZorFfp02DJ1Srkv8mSF3lSr87w3EjN-YMwJveT6CDqHmBIZu_dFuSnbL-L4WLmQiYuGy--2OujvikSeAT47G3Tz6l3RmJzLkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=r5utqHgEfty_rVvRfc0GBnnEVDywwOESK3NcB7AUCfnYRI-wySPKqyn0INeROhaHggu2LFage0TuP6-GNIo7Mpbg70ywBP9yAAU0evnDhwOkmFdP9Xhh4fUBosdqu5wHNYb6MnlcaqfAyaQUD9kEZKx54x3HMOvwDn_fm7a1sPnvihbRSMZ_dUZZ--4jxUQBNhtKTThBp1MsEnhDnr7Bv0fk-oQ-PatCV6dx7jNDyh0DdOHcjZxIuZorFfp02DJ1Srkv8mSF3lSr87w3EjN-YMwJveT6CDqHmBIZu_dFuSnbL-L4WLmQiYuGy--2OujvikSeAT47G3Tz6l3RmJzLkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2x78XLA8QK6JxtozR_dnla6ZHTQEtW_rjy4WWv_c3pcO19ZKTbCT7-qFnVPkefNPMBWzurCJSVwvmWn78CRzg9VQPKk1e45mW-ikhin3QDPeQfcB-KbJxsQzO6R14jdyfYSHq1gIYN9Dzk9M8tbpZ58SciFK4-oFxTXjNNpQ1Ohv4a3fiQa_olRA_ZpzVVqnShYtD9KJukPreWBui8N27thF1tuMPcLpV9C3R7H_Mnnb-acdHZLTaLRbtIGVeJd1h87HSJtaffZmjY7xpTDo1EBb2k6i8xpU1j2l-BubxyJW5EO6RIek6sC8Z0-GPcQe6m7Vso6VCysZVzpLxvM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=VHHeYfu_V3Uc5kGmzs9fCV-cB0rqMsucGNCv5VT3j_VyHFLhPu6rFvPYjQs5zkRo4bBR2ZP-HAU_AQzaJYHdB4FG8aMwHNc1F1LNGAuwRbP6piKMCA2H__6fwDYuFXRAe0iljDSoIob5V60ynz6XqbpAlJK4elC4OIqFsD6c0IFupwsX7_OFDdHKS0meBte_r42aly2YkZEI4_K7IKcNouVjzB7dMhpRfTbDhf8PdbZY-qv_50bJrpfgUkn2UICssRWVjhCtlXIAHs21wpJ4qgjzUUj229EXHRSt2aiB6Ku3DQQDJJyshDF8nTbuZOORVepl25zQP2W0uDE89eSlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=VHHeYfu_V3Uc5kGmzs9fCV-cB0rqMsucGNCv5VT3j_VyHFLhPu6rFvPYjQs5zkRo4bBR2ZP-HAU_AQzaJYHdB4FG8aMwHNc1F1LNGAuwRbP6piKMCA2H__6fwDYuFXRAe0iljDSoIob5V60ynz6XqbpAlJK4elC4OIqFsD6c0IFupwsX7_OFDdHKS0meBte_r42aly2YkZEI4_K7IKcNouVjzB7dMhpRfTbDhf8PdbZY-qv_50bJrpfgUkn2UICssRWVjhCtlXIAHs21wpJ4qgjzUUj229EXHRSt2aiB6Ku3DQQDJJyshDF8nTbuZOORVepl25zQP2W0uDE89eSlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=ZjQo53Sdil3DaTxohy2H7elPel9IYeMNuouSFFtL0qvf4BLZFJQ59oeOVw488zF3283PdZkhsE9XlwUKfi1R5hAgYTlr7nmbYTlF4RX9BI_ZBwifkaKs9nYXQ3ZOe8Go3-EDn5qcGbqQjoSaCMWAO3hLjl0_ugGA8eBfrt_seW2fnqjm4lJPjQA7emO618z-0YAFZOiFqu91Uo7dejlfK_Y4Oc5MhOAS76R6anVB3zHQVIvYs59gdUUDdVjyluY4Za5ub-SQD3syjqNeymjGQPce-CJijPfL-MOAo71TdnppDyLdoWvnHRoh-sH7asH0eZ8xP4KMGLoX8LGCzznLwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=ZjQo53Sdil3DaTxohy2H7elPel9IYeMNuouSFFtL0qvf4BLZFJQ59oeOVw488zF3283PdZkhsE9XlwUKfi1R5hAgYTlr7nmbYTlF4RX9BI_ZBwifkaKs9nYXQ3ZOe8Go3-EDn5qcGbqQjoSaCMWAO3hLjl0_ugGA8eBfrt_seW2fnqjm4lJPjQA7emO618z-0YAFZOiFqu91Uo7dejlfK_Y4Oc5MhOAS76R6anVB3zHQVIvYs59gdUUDdVjyluY4Za5ub-SQD3syjqNeymjGQPce-CJijPfL-MOAo71TdnppDyLdoWvnHRoh-sH7asH0eZ8xP4KMGLoX8LGCzznLwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=o0JNPbCGnLzdDLnVnDcT-DGTOJJ95uUrFzJ0lJ5V0kP9ujPmofpOrPGHTswf0cAqtHTXlE1YPqWURpRpfhErqHIMo9hCvjNulrUmVbjAwCPYf71U6hlAsBKhI_ReC5UFeqEiSylC29yUJ8lCuwyEQqo5pL9BfIj0k9-i0uw4GVH51FqFpE8bhc1wPgRwJ0ldIk6jrmLDKYoCRBjyfgtRen2_FElPwoZfxlvrh_j3gAkC14OXYysejumWIuesqJ_FtffYCh6QUIDo40Ad5dDfPC5kr-0qlp8p9fG9vP4D2h2wk3WQbeHkX3wXTekEq7kWRdX_tD8ZmgiL0NkVMpLtwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=o0JNPbCGnLzdDLnVnDcT-DGTOJJ95uUrFzJ0lJ5V0kP9ujPmofpOrPGHTswf0cAqtHTXlE1YPqWURpRpfhErqHIMo9hCvjNulrUmVbjAwCPYf71U6hlAsBKhI_ReC5UFeqEiSylC29yUJ8lCuwyEQqo5pL9BfIj0k9-i0uw4GVH51FqFpE8bhc1wPgRwJ0ldIk6jrmLDKYoCRBjyfgtRen2_FElPwoZfxlvrh_j3gAkC14OXYysejumWIuesqJ_FtffYCh6QUIDo40Ad5dDfPC5kr-0qlp8p9fG9vP4D2h2wk3WQbeHkX3wXTekEq7kWRdX_tD8ZmgiL0NkVMpLtwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
