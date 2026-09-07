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
<img src="https://cdn4.telesco.pe/file/iFi5XvlBLPrOdghwSKbo3rsmT6J8NefTDpmM2MaujNGFLpc5Xr1HKyLPdEtFEaxMFPYVCg0qxZ6Xg6CoXXKBY9t7Lf2pQdt2cWu3UCJHDtc7nMpnRha9UAQG35ErEkEFqjN1Tl64xZTnYiHlyGcsgQD8ssZVrbwLZncwkcg8WCyP3WCJOAX8RMDstqNtLGyRte2ACBX_54xpjFmNhJCUW19pIZdHFrRZv5Sgb7-lKBG4p8FIjYk2Fmwew-feTTLKhm9drDRErod1H2I_GStVyJtl_KlMH79YifL_NurBwTUnN9gXeY9rLMeYElRwVMimV_q44xRcUtMhPHwiu4VybA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 930K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-146112">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کمیسر حقوق بشر سازمان ملل:
هوش مصنوعی می‌تواند خطری «وجودی» برای بشریت ایجاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/146112" target="_blank">📅 19:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146111">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
اردوغان: اسرائیل محور شرارت است و باید متوقف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/146111" target="_blank">📅 19:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146110">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVYl2OMfA07bi65KoKBCd8Qo6uYDPZz4xO5TsQmxBpD-G6Ajjlg1ixwUN4a744TSpZGz5a3VaACv1ov03bRBYlaD_p4Vdfmw3qaOoD6R8OvCLSYnGv1r2ncNv9dfF0qx8o6JFyiDUyOYa9xjXL_Ae3ciPwJhTbs-bwQn78Hv5aTjJ3Z4l7LPLNZw-xPvVorEnLpSenOdZwHYFkxNMVJ0zi-1U2ZlMU_zls8L_YcdgjCTVNHS3OHoIp7W3SpTY2c4O4WvCDG90h_AaqHx4eMXRBCy9UavONBIDBJ22e0xru2MIlkTJ0VV9ZFT2r5s5u5lLWy4QBnPR2TAqH69GfaNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت ۹۸ دلاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/146110" target="_blank">📅 19:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146109">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
فواد ایزدی: اگر ایران آب شیرین کن های منطقه را هدف قرار دهد، چین از تهران تشکر خواهد کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/146109" target="_blank">📅 19:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146108">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4Y4uejdsqJoNdIPvdmbN90Ke2b8OibXvoRW2vDbb_k3J-P3Pr2YJCUDAvzR2UEBju_jNq-SDJMPd6KjugoZ3BjkPxhBThjgIhB2q2ViimP_zQGK0llm07LfQpKSHP7NzVJRux-8kEI1i0zvrsoTmcHWJDve3AkJwbLWGNc51On9csllRhpKXA6LyB8ss-FXxLnC8e7VU6ezcWbR7aBWcgdIrD63iCb38NikSmYLwrH_N3G6jsqazS7TCLACA8772CRHUFeYzsW89BspGOpONtQx9-aPMA8WTIwPAEmt1OuOvhIJV0IuWGlGvGu4616RIr3zY6tpG5g-7rLuodb5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ خبری از وال استریت ژورنال درمورد اظهارات پزشکیان مبنی بر لزوم پایان جنگ را به اشتراک گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/146108" target="_blank">📅 19:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146107">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzNVw6GAJWzNJdiirxjR3jOhiuw37yaTSfY3-U3ThNAY6trSeuj5jKdWASnt7D7_B0LyNwCJH-dLpfI0zn2gexAhIqEfUb6d7w7qyiGSz32vRfO9HWrPzUOiVmgAZF3XhOoyfiVuVm0UxGQ3u3EGlw4r6KSD0NOU4VwNeizpOjFmdT837xE6E4ozp9v4IZQNIfxDFVhpadVy2sOy4CYXKW9w3olirzbz5Ne9OmbJoCdJbx3XgCadRo4FWJmP0UcJEkMAatrnIWuCTo97doUxuZK0qtng3rRi66mS-WlFqBrWCbhfVh6ZHnNQ4gfoFzXFfTl5392h7AEVvV9gR6xLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/146107" target="_blank">📅 18:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146106">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab852706fc.mp4?token=dzC1fI0vSU9We6EIktrp1O9p2PHmr0xugUwT3pGAOhNPsAn2ykrezimmPJLzQFkvIxtWnc7FCRmSCX190A2NONQC_xqlyNfzpiFpUO3NVV6hzrpNKikFUk3xLOX-ZVAZVb6mw0Kq048Ja5CZaQueMhD4DIr1oiqxcVKsc64TkRtihHNjXl34Q2H2mDzJdSjWqIutLb-MgcyBg3Ace02ovqfxupi34hZnZpDuOn8jZV2TEtT6n6tVngHjzKcfxenS51hnJL3nisdbwPBDFAYSqv2knsA172QqJIaGaymejMiqS8Et4fvNQGNdaD8CuZJM7yMvDIxRUxYvaMlKgpl-aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab852706fc.mp4?token=dzC1fI0vSU9We6EIktrp1O9p2PHmr0xugUwT3pGAOhNPsAn2ykrezimmPJLzQFkvIxtWnc7FCRmSCX190A2NONQC_xqlyNfzpiFpUO3NVV6hzrpNKikFUk3xLOX-ZVAZVb6mw0Kq048Ja5CZaQueMhD4DIr1oiqxcVKsc64TkRtihHNjXl34Q2H2mDzJdSjWqIutLb-MgcyBg3Ace02ovqfxupi34hZnZpDuOn8jZV2TEtT6n6tVngHjzKcfxenS51hnJL3nisdbwPBDFAYSqv2knsA172QqJIaGaymejMiqS8Et4fvNQGNdaD8CuZJM7yMvDIxRUxYvaMlKgpl-aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز یه خبرنگار لبنانی داشت از شهر " نبطیه " لبنان گزارش تهیه میکرد که همون لحظه اسرائیل بیخ گوشش حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/146106" target="_blank">📅 18:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146105">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: در انتخابات میان دوره ای به پیروزی قاطع دست خواهیم یافت و آمریکا را نجات خواهیم داد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146105" target="_blank">📅 18:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146104">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=dHlOb57aicHW5A64k97Zei-2IxqQ_bnuPR74fC8uBduOH7FrB3Z0dy2y1ATkrUPHxYMEPx5ZsU451DKbqW7kDuCi0QGGfM6d4j-_ylK6RqxdQj04sgU9UUZ90IWSy6oJ6VS0QTD9IIVf3PA8FoaJS1dpx-zJJ8KJitx89QBi0EhCp9xiPYs8JFCQB0eNtC5_aAG3z78pVPjrNh4I6pe1VsEqD56ZsmQfMf6YcN-m_GSPOjT0Yls0M0cLhLm7PuIwTHLzFmx3WDDMoGz2m5xA1fcJoH9zxUBfRJdESZlGHg7ArPRqLMhp7djQfq7iQEvdMR41PsE_6E-H6Ktc_mmwebr2RKffON0A4wXxKOkGcBJr3isp3raYIB3K73yO42cYntwTzcg-Kc9RyxIJ29QBZzvSH1FEuShnhDtk47x5tkk97-BPsgu0nwbNTKUTURuR4c0XsOmrtbeufMWuK_7BR74wR8SBtGDhXtUJqcRh-EV_HdzIfd7I0LR-RD8UPdRD9Podbzd2KUEtm3Yxkr6mka7o_LuBPedz-1xMyHCEI-rcqpNBsuWcR7k4zwMVf2OyBAgm1eccFkBjU7QMy6Qw7ydfzv9bBDgqb2KaskIwzO6vj8j2Zl0Q9rOsdP4jgETDDm9uIQzgr0Gkd1FExFbpsy-fbnhpOOgmXBZsxcfWw9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=dHlOb57aicHW5A64k97Zei-2IxqQ_bnuPR74fC8uBduOH7FrB3Z0dy2y1ATkrUPHxYMEPx5ZsU451DKbqW7kDuCi0QGGfM6d4j-_ylK6RqxdQj04sgU9UUZ90IWSy6oJ6VS0QTD9IIVf3PA8FoaJS1dpx-zJJ8KJitx89QBi0EhCp9xiPYs8JFCQB0eNtC5_aAG3z78pVPjrNh4I6pe1VsEqD56ZsmQfMf6YcN-m_GSPOjT0Yls0M0cLhLm7PuIwTHLzFmx3WDDMoGz2m5xA1fcJoH9zxUBfRJdESZlGHg7ArPRqLMhp7djQfq7iQEvdMR41PsE_6E-H6Ktc_mmwebr2RKffON0A4wXxKOkGcBJr3isp3raYIB3K73yO42cYntwTzcg-Kc9RyxIJ29QBZzvSH1FEuShnhDtk47x5tkk97-BPsgu0nwbNTKUTURuR4c0XsOmrtbeufMWuK_7BR74wR8SBtGDhXtUJqcRh-EV_HdzIfd7I0LR-RD8UPdRD9Podbzd2KUEtm3Yxkr6mka7o_LuBPedz-1xMyHCEI-rcqpNBsuWcR7k4zwMVf2OyBAgm1eccFkBjU7QMy6Qw7ydfzv9bBDgqb2KaskIwzO6vj8j2Zl0Q9rOsdP4jgETDDm9uIQzgr0Gkd1FExFbpsy-fbnhpOOgmXBZsxcfWw9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رقص و پایکوبی سربازان آمریکایی در یک کلوب شبانه در پاتایای تایلند
🔴
تفنگداران و ملوانان ناو آبراهام لینکلن، چند روزی در تایلند مشغول استراحت بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146104" target="_blank">📅 18:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146103">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر دفاع سابق آمریکا:
جنگ با ایران حداقل 6 ماه دیگر ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146103" target="_blank">📅 18:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146102">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
موشک‌های بالستیک حوثی (انصارالله) به کامیون‌های سعودی با تجهیزات نظامی برای دولت یمن در اردوگاه الوادیه در منطقه حضرموت نزدیک مرز با استان نجران سعودی هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146102" target="_blank">📅 17:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146101">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEo_q9gAxYu85lsq6h-ELfDEQ0QO1AtBk2Ewysr279UciqDdKdZkvIpZw-xGQVmxYMOrOxG_jcbOU4k3cHaEbTCvQaR6_8U4lMS3EVfqvdLsQ7MIqVfFFR4C6M0iKumEUUSRWAZlzmN7VaJe36_iKM6YB1aMzML0XUc18xemgVkzn-SfzzO26zcesZAzkmnPoNv3v4MhtQDtsB40bME7AT_RyeIjTZb9nerQTftil0zQcdOVO4-EMZiuvUZR8vJzsuo3D2KQkHq8qN-KWV064iRIOCUJssRkNxjts1BWsEYX6cvREm1w4wuRMvOgU8Q4t2req_iDePSNRMi-UH2R1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت محسن رضایی:
دیگه اون پسر مهربونه نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146101" target="_blank">📅 17:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146100">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): در پاسخ به پرتاب دو پهپاد انفجاری به سمت سربازان ارتش اسرائیل در منطقه امنیتی: ارتش اسرائیل به تأسیسات تروریستی حزب‌الله در جنوب لبنان حمله کرد
در طول شب (دوشنبه)، تروریست‌های حزب‌الله دو پهپاد انفجاری را به سمت سربازان ارتش اسرائیل که در منطقه تپه علی‌التحریر در منطقه امنیتی جنوب لبنان فعالیت می‌کردند، پرتاب کردند. هیچ زخمی‌ای در ارتش اسرائیل گزارش نشد.
بلافاصله پس از آن، ارتش اسرائیل به چندین تأسیسات تروریستی حزب‌الله در سراسر جنوب لبنان، از جمله یک انبار سلاح، حمله کرد. علاوه بر این، ارتش اسرائیل به چندین تروریست که شناسایی شده بودند و در حال انتقال سلاح در منطقه کفر رمان بودند، حمله کرد تا تهدیدی که برای سربازان ارتش اسرائیل ایجاد می‌کردند را از بین ببرد.
پیش از حملات، اقداماتی برای کاهش آسیب به افراد بی‌گناه انجام شد، از جمله استفاده از مهمات دقیق و پایش هوایی. ادعای اینکه چندین فرد بی‌گناه در نتیجه این حملات آسیب دیده‌اند، در حال بررسی است.
علاوه بر این، پس از پرتاب پهپادهای انفجاری دیروز (یکشنبه)، ارتش اسرائیل در منطقه نبطیه حمله کرد و چندین تروریست حزب‌الله را از بین برد.
ارتش اسرائیل اجازه نخواهد داد که سازمان تروریستی حزب‌الله به شهروندان اسرائیلی یا سربازان ارتش اسرائیل آسیب برساند و برای از بین بردن تهدیدات ادامه عملیات خواهد داد، در حالی که به توافق آتش‌بس پایبند باقی می‌ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/146100" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146099">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
اژه‌ای:هرکی صداش دربیاد جرمه
🔴
هرکی خلاف وحدت(ما) حرف بزنه جرمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146099" target="_blank">📅 17:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146098">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1b21e927.mp4?token=lSO7-lF12xshwUKYJIRmi73B5QRiBl4MXQIt4seNyyjEVhBuvc8F_GewMBiCUAKwWOCdJqzZPVst4yKan6M73crZily9U_hUsn6mjGibgKZaMA1al04sasxKoQ1oA-jwFv_7t7Ew7j34j6nnRiPjPYOXmF5I-y3epGN6NZiYx8Ud1ZGelvgtMhs_7m1SIl1j-ePAOVWc2ASC8gpt4gYc6sSItc42qIPzNbr1HUFoXFKfkjYacndAkeXVvM1XI6PQB3QGRDy3SAI3sWDEZ8picx6t-QKJpzn-UM0LUdni4eUoIAXgr7JV6TZvbN2gM3tcRUYPZRxf5EwgPSTh13OH5nW3ZmeD7z0tPyvFFzmIcaPfrp9UGMEPvtcQrNptQlfric5phrkAUG-388xlqVuP64CpBHuJkZfyqmddwscXW4KYrTg3aB1zDQzWhBTpLSwloHeGwYIdDBk-FwhwOmcN6QvMGLK7VED0IfzWoJi6LKrEiSEp-nKHMqD1KKBNWxG0zoyC9Q5yN7SyoZ1GtqVbWHA866gx9Ni4rHsa-SRZasusS0hKChtZu7hUPy9fJk-GV0Dlnrp8XQtabgU5Tg2iRLlXC3_V6YcsWa60-iKXA7TnxvZa-84Gd4IqjePuiWA4YUsP0lPhiJsklNoLHEoxVeJklNxpksLDKh319J61_x0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1b21e927.mp4?token=lSO7-lF12xshwUKYJIRmi73B5QRiBl4MXQIt4seNyyjEVhBuvc8F_GewMBiCUAKwWOCdJqzZPVst4yKan6M73crZily9U_hUsn6mjGibgKZaMA1al04sasxKoQ1oA-jwFv_7t7Ew7j34j6nnRiPjPYOXmF5I-y3epGN6NZiYx8Ud1ZGelvgtMhs_7m1SIl1j-ePAOVWc2ASC8gpt4gYc6sSItc42qIPzNbr1HUFoXFKfkjYacndAkeXVvM1XI6PQB3QGRDy3SAI3sWDEZ8picx6t-QKJpzn-UM0LUdni4eUoIAXgr7JV6TZvbN2gM3tcRUYPZRxf5EwgPSTh13OH5nW3ZmeD7z0tPyvFFzmIcaPfrp9UGMEPvtcQrNptQlfric5phrkAUG-388xlqVuP64CpBHuJkZfyqmddwscXW4KYrTg3aB1zDQzWhBTpLSwloHeGwYIdDBk-FwhwOmcN6QvMGLK7VED0IfzWoJi6LKrEiSEp-nKHMqD1KKBNWxG0zoyC9Q5yN7SyoZ1GtqVbWHA866gx9Ni4rHsa-SRZasusS0hKChtZu7hUPy9fJk-GV0Dlnrp8XQtabgU5Tg2iRLlXC3_V6YcsWa60-iKXA7TnxvZa-84Gd4IqjePuiWA4YUsP0lPhiJsklNoLHEoxVeJklNxpksLDKh319J61_x0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو کرج دوتا از والدینی که اومده بودن مدرسه دعواشون میشه؛ یکیشون اون یکیو هل میده سرش میخوره زمین و متاسفانه میمیره...
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146098" target="_blank">📅 17:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146097">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: جنگ ایران نشان داد که کشورهای عربی خلیج فارس نباید برای امنیت خود فقط به همکاری استراتژیک با ایالات متحده متکی باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146097" target="_blank">📅 16:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146096">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
روزنامه هآرتص : ارزیابی اطلاعات ارتش اسرائیل نشان می‌دهد احتمال دارد ایران، در سایه فشارهای دو چندانی که بر این کشور وارد می‌شود، تصمیم به تشدید رویارویی با اسرائیل بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/146096" target="_blank">📅 16:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146095">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نفت برنت در پی تشدید دوباره درگیری‌های ایران و آمریکا طی یک هفته بیش از ۱۰ درصد گران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146095" target="_blank">📅 16:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146094">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نفتالی بنت، نخست‌وزیر پیشین اسرائیل، درباره نتانیاهو: در حالی که نتانیاهو بخش‌هایی از سرزمین اسرائیل — ۱۳ درصد از کرانه باختری — را واگذار کرد، من یک سانتی‌متر زمین را واگذار نکردم.
🔴
در حالی که نتانیاهو به بایدن قول داد کنسولگری فلسطین را در اورشلیم تأسیس کند، من امتناع کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146094" target="_blank">📅 16:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146093">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqWtGqN9iLd8N4lk7kjk-PZyBwfZ-b2jDjXrCpif9N4FNGNQnOqNLhN24Jc-m73bLXQnJf-rP8FgXEnijFKUZV6riTbPN8V-s7Hkz72nusxM6UFjsEV4MZIjLG5r3GYhyp1_jWmkjppa4As0CuL57c7enDgpAOZcG6kS5HGwN7kkfUtwRO5UfbZvG76_oLv3PMma2wgAq9wqnBhSmE-UoFAaX-kHaZDjpPiXGKdxYfVFqhdFTq-9YypwY03W6QOM53Jb5Dfij1I5pi4whEQBYNKa84ArVjrDtVDBlEpT7F3yQuH8JBDManOd-oPl6IExd2dMJS_jTwisC8o51Hl8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران در غنا با انتشار نقشه آمریکا با طرح " بته جقه" ایرانی نوشت: نکته جالبی در حمله به ایران وجود دارد: دیر یا زود، فرهنگ ایرانی شروع به رخنه در وجودتان می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146093" target="_blank">📅 16:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146092">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBwtBT1cq6x_KeMEZvqhsB2Ys4skSu7S_D8i9UOGSYle_9Twr7HBBkJbaMquGKZBMyxOZXkEsAE6zZvJ6vSfwt8IvKWQhJxVs894LUnrzsDC29e8Qt4BNfSAmMFBxaZTWoaG8X4QZcyRq1F6Yk8fZ5RPPYn1GFYFyjHURVt2WalO_04Ert_Xb8q1U6uc9oEBtNioj7Tid6XbWv2ynrXVZoXRZH7EFptgi9VEnw5WzbGxkEkoFFV5lBIk8eV7f3QKo4UItbxTP7krF2QEsWra-Sm96MfxszHjBuzYVVmd8ie8rt3O266OsDvdKAKPmjkkEleRAVSKtJhx_H7YrJxQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره :سوخت کشتی‌ها در حال کمیاب شدن است و سوخت بانکر مورد استفاده کشتی‌ها در حال کاهش است و این مسئله هزینه حمل‌ونقل دریایی را افزایش میدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146092" target="_blank">📅 16:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146091">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / بلومبرگ: آمریکا قصد دارد امروز پرونده هسته‌ای ایران را به شورای امنیت سازمان ملل متحد ارجاع دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146091" target="_blank">📅 16:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146090">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4aab690b.mp4?token=Cmz5x4jrQXk9OMHYV9LORh-b-jr9UoUuVKGzmKUnPZiEWXKoPHS0hz2Y8HyVNBnGQBmR2Ea9io33scN9O9DXj_gc_JIakil4l_0o6k6juQGInHyd8OsNFcXS6sAyT4AiS4jRE1URlurcXYFaLzKwzguG2IkwlTgIAVMfhbZ7HESytMAS2fhh6My5gjzHwr4iSDa_LnjmsIGbxfY-Jiw5A8iH9RfUylE-XaQczSZLEIsqJYwtzpNXWVf5SiVYF87vTtyvrFXJos_nfpQ91-MX9OlppRzpxoEvj7DRbdm3G066akrj11BgdoY5N_snoKfhD2WfaIc1yCSNhT-LvY7MGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4aab690b.mp4?token=Cmz5x4jrQXk9OMHYV9LORh-b-jr9UoUuVKGzmKUnPZiEWXKoPHS0hz2Y8HyVNBnGQBmR2Ea9io33scN9O9DXj_gc_JIakil4l_0o6k6juQGInHyd8OsNFcXS6sAyT4AiS4jRE1URlurcXYFaLzKwzguG2IkwlTgIAVMfhbZ7HESytMAS2fhh6My5gjzHwr4iSDa_LnjmsIGbxfY-Jiw5A8iH9RfUylE-XaQczSZLEIsqJYwtzpNXWVf5SiVYF87vTtyvrFXJos_nfpQ91-MX9OlppRzpxoEvj7DRbdm3G066akrj11BgdoY5N_snoKfhD2WfaIc1yCSNhT-LvY7MGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار گسترده‌ای که توسط اسرائیل انجام شد، شهرک زوطر الشرقیه در جنوب لبنان را به لرزه درآورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/146090" target="_blank">📅 16:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146088">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNe8m_3nk0na8uggCBGdDvwvSrrc0g_ZaDMGT6TfPBcP6_BL2ouFILelPy3zu22uOXTVpbxL9-ehWwz5fKskXlMYV5atD0y8qcoEk5SIdTAJYItfgdb5K2bkEchdr1346PfT5RzNUbeGROgfSlbrDpwmAQ4pbCRRBdXb8_GXr5cdx2ARLr2whwIGSWYSBXgv1RrHgZXP3Gg5y4wNTOsjzVuBK1XhVhLdxH6kUrNxixGetSdiGq7YRo9_3H_Ex6mYPPhf4KZbqpW2cFhntEDih4fz9AtJ9OZKVEWeG5Tz5xTl0lhA6Ls47Awls8tqnqAywnhquR757RhPyxy4M-2wCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVoYkLUkxP6IcrSBIQxtm8mM_QSitsu9lPzJHkvzItMEu4wXBGzgvu9lZfjI9iODYG3lg4axW5nzJR0l77ghquPJ66fouPVXV1iqatnvuYtiVILuqjXagjwWFphATIECpToofTPFDyxCSfRI76Yj3d7FHVFA5CyzwXRlvLjQDZbvqjISbjK3hlaY02fFmsakAlHMdTJ3iN6YfQUUNuPogsNYRIfvTvWg6zX3LYy3AyRtycS4TW9G7rrFj46XBaBkj9gSvF5Db5jmHTaE_m5zGQWDkfCFX47Rmu0Wylp0B77NuwZg4o-2beJ8CRq1XvCu14spsXId3v4jttMbp3u4Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پالایشگاه جازان در عربستان سعودی در اثر حملات حوثی ها دچار آتش‌سوزی شده است. تصاویر ماهواره‌ای این موضوع را تأیید می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146088" target="_blank">📅 16:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146087">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان: ممکن است عده‌ای از ابزارهای فناوری سوءاستفاده کنند، اما نباید به این بهانه، راه رشد و توسعه را بر خود ببندیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/146087" target="_blank">📅 16:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146086">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فرمانداری: احتمال شنیده شدن صدای انفجار‌های ناشی از خنثی‌سازی مهمات عمل نکرده در حوالی پایگاه هوایی بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/146086" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146085">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رسانه‌های جنگی یمن: منتظر بمانید تا ساعت ۴:۳۰ بعد از ظهر، تصاویری منتشر خواهد شد که لحظه هدف قرار گرفتن و آتش گرفتن کامیون‌های حامل سلاح‌هایی که از عربستان سعودی می‌آیند، در پایگاه ودیعه را به تصویر می‌کشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146085" target="_blank">📅 15:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146084">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
گروسی: ایران همچنان عضو پیمان NPT است / آن‌ها باید به حرف ما گوش دهند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146084" target="_blank">📅 15:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146083">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
هواشناسی: شدت بارش‌های امروز و فردا منجر به صدور هشدار نارنجی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146083" target="_blank">📅 15:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146082">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee153a30e2.mp4?token=VPqMxEswkcd2vKgJDQ-kk9NIYBqujGLQp4WQaDBxKIt6Cogca2kjbIKZycMbLx3bIjmd-vKiaghBvk4hT_j7kSeNHOoJ2JVtrG_4TNY-e7AUxuR0fPJwGVJdlnwOprO8NNZOhxIFoc3dqEwihdbARM867e9VsXn-Efc3YD97HGj3qEB6FlWkOavqKItMITqaSXkPJddaycoYxE79CCQHzpQEaO43dz1t57TEEnZ-fIQks-ZYVoDuk_2kRhnvATaJP2y78rp_JhyUkJ8o7pSEx9qnoebE3gfzB7JJsrmuMlYfbv-iYFQuQfhelM41PbtUUCr0lvLFVniAnMNDMQc8Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee153a30e2.mp4?token=VPqMxEswkcd2vKgJDQ-kk9NIYBqujGLQp4WQaDBxKIt6Cogca2kjbIKZycMbLx3bIjmd-vKiaghBvk4hT_j7kSeNHOoJ2JVtrG_4TNY-e7AUxuR0fPJwGVJdlnwOprO8NNZOhxIFoc3dqEwihdbARM867e9VsXn-Efc3YD97HGj3qEB6FlWkOavqKItMITqaSXkPJddaycoYxE79CCQHzpQEaO43dz1t57TEEnZ-fIQks-ZYVoDuk_2kRhnvATaJP2y78rp_JhyUkJ8o7pSEx9qnoebE3gfzB7JJsrmuMlYfbv-iYFQuQfhelM41PbtUUCr0lvLFVniAnMNDMQc8Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه روسیه، لاوروف:
غرب به این شهرت دارد که تمایل دارد از طریق اخطاریه‌ها مذاکره کند، و مطالباتي را مطرح می‌کند که برای بسیاری از کشورها تحقیرآمیز است و بوی استعمار می‌دهد.
🔴
ما باید به مردم یادآوری کنیم که استعمار چه رنج‌هایی را به سرزمین ما وارد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146082" target="_blank">📅 15:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146081">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
علی رغم ادعای وزیر نیرو مبنی بر پایان خاموشی‌ها، برق در مناطق مختلف تهران همچنان با قطعی روبروست
🔴
طبق گزارش تعدادی از شهروندان، از صبح، لویزان و شیان با خاموشی روبرو بوده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146081" target="_blank">📅 15:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146080">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نرخ بنزین با کارت سوخت جایگاه یا همان نرخ سوم از امشب به ۱۰ هزار تومان تغییر می‌کند اما نرخ اول و دوم بنزین، بدون تغییر می‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146080" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146079">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: برای یک جنگ فراگیر در کرانه باختری آماده می‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146079" target="_blank">📅 15:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146078">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g30rR1hcR7dvPMPFG1vEBfUQfksHAkixkd86GdumELLIKHanMPM88j_-ETIeAo7RdkHKf-kvymKqHdMcyRT7fvd-znGmSNFl0sPEB7Y80QvmGdws2vkMl3-owginSCYvXGk2mDVf7JiPn67crcO2glbanw_mwScljAwajTupi_ZD3-Yz5uZItwjrQcxXPAsbYOJiiNAVKd_iImmfcs3OKPUZsinfrI2W9kcSl57TE4JUOGPO3tl9qmMQLcVkd5x6BCO-8Pmn7BfR_vV82WLlqE-x2MNmp8VBbuDJFR2qp59AVVtQbW_N44ifioZaPrh3dLDcSRqdxLAKy0IuUhnZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی اعلام کرد واسه استخدام شدن تو شرکتش باید گواهی عدم سوء پیشینه داشته باشی و تا حالا زندان نرفته باشی
🔴
پ.ن : بابک خودش چند وقته آزاد شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146078" target="_blank">📅 15:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146077">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
الجزیره به نقل از یک تحلیل‌گر: ایران به آمریکا اطلاع داده که در صورت تصرف تپه علی‌الطاهر توسط اسرائیل، مستقیماً وارد عمل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146077" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146076">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjSvirwW-cz6sT_GrK81s_Wcsl0Q0y7y_w26U20k7KVUH3P9zOkgMjRO9xa8d_Xnb7c7JaiMcN_SDH-LQ5fhFC4-Y8a82TxuVam67uQqTDijfWDVa-Z8uoozNyxkPNmJw6MOTDe666hLTJCzO0_c27MkmCzohlyqVJnecviA5k3P5DhBul7fY7BxJrLhDHK3h07R0UnYYg0pmc4pQijIc1bXQ5A6zjWQBWBFPNf_vcv6bpmgquPemDs6pJGoup48K8haRzMTlO9_okfm7FoMcIVhI601pVMfnonJPBBix2SmnWdq7qOLwVPrr7nSzVr-Uib5dPfg5-vflrB77Pp2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر آبراهام لینکلن طی ساعت گذشته شهر پاتایا تایلند را پس از توقفی ۵روزه، ترک کرد
🔴
گفته شده این ناو اکنون در راه بندر سن‌دیگو آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146076" target="_blank">📅 14:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146075">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏
👈
پزشکیان: اجرای یک روز در هفته تحت عنوان «روز بدون خودرو» برای دستگاه‌های دولتی دنبال خواهد شد؛ توسعه دور کاری و کاهش سفر‌های غیر ضروری و بین‌شهری نیز باید مورد توجه دستگاه‌ها قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146075" target="_blank">📅 14:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146074">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سخنگوی کرملین: روسیه احتمال ازسرگیری مذاکرات سه‌جانبه درباره اوکراین را منتفی نمی‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146074" target="_blank">📅 14:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146073">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مهران رجبی: اونی که نمیاد تجمعات باید بهش بگی فازت چیه که نمیای ؟
🔴
این وظیفه ملی و دینی ماست و باید بیایم کف خیابون
🔴
ضرر نداره بیایم و شما کاری میکنید که کفار ناراحت میشه پس بیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/146073" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146072">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گروسی: بازگشت به دیپلماسی و مذاکرات در موضوع هسته‌ای ایران ضروری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146072" target="_blank">📅 14:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146071">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فایننشال تایمز:پالایشگاه جیزان شرکت آرامکوی عربستان سعودی روز دوشنبه بار دیگر هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146071" target="_blank">📅 14:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146070">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک منبع اسرائیلی به i24NEWS: مشخص نیست جرقه‌ای که باعث شعله‌ور شدن اعتراض در تهران شود چه زمانی خواهد بود، اما خواهد آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146070" target="_blank">📅 14:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146069">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مقام اماراتی: ممکن است دهه‌ها طول بکشد تا اعتماد میان امارات و ایران دوباره شکل بگیرد
🔴
انور قرقاش، مشاور رئیس امارات در کنفرانس هیلی در ابوظبی گفت که ممکن است دهه‌ها طول بکشد تا اعتماد میان امارات و ایران دوباره شکل بگیرد و تعامل با ایران برای امارات و دیگر کشورهای خلیج همچنان مساله‌ای محوری است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146069" target="_blank">📅 14:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146068">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کره شمالی، دومین ناوچه مرتبط با برنامه هسته‌ای خود را به ناوگان ملحق کرد.
🔴
کره شمالی، دومین ناوچه خود به وزن 5000 تن، به نام "کانگ کون"، را در شهر ونسان به ناوگان ملحق کرد. کیم جونگ اون، رهبر این کشور، این ناوچه را بخشی از سیستم پاسخ هسته‌ای کشور توصیف کرد که قادر به "نابودی حملات تلافی‌جویانه" است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146068" target="_blank">📅 14:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146067">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نیروهای دولتی یمن: در محور البرح در حال درگیری سنگین با حوثی‌ها هستیم و تجهیزات کمکی برای حوثی‌ها به این منطقه رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146067" target="_blank">📅 14:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146066">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2eb91028.mp4?token=K8ErV3j08SGaGCEBT-TZTEOPuGCLYzAgpP5jo3Gflcf_N_4DeGWclEeZ2g8UPJKX16f0Jw0SE0TFRPfTXuC-c1uqbJ1LWVRFNO0vKiZ11Caf6CTFRJDU2E1k1h1p_qIMXX_4pibu4huuLEROziyWINwmnPDIsC3gAdMduWDBt2bezgI-wfpTUFwwJXViRN2CCvRnXxAkinNmrCKKTtpnru6xDlanE2tbNeao_bhigd-w47Fv2Kjw3oTqRy5pBHvsghfU2OkexWgv4CNhne5QTVlOMYG2fJkKfTZe0eGAPQc5mlZjqC7JyGWN67uJQNCGmyiAW22YF08Lds2CnwV6an4WATktYt8PwVBO6Qf9CWZPBoPrreXCRxFM10r8TjNBnPCeNzGo5j41dFn8_gxt87ZJ4-N9jpKXXUvSdRqxZYZ7ydYX8b-KaJYfZEnAEYgtiZUVQOvMa6QCCd4GdADY7jVEYHzNfmkpZej3Xc93tBf4dRnQLVJ_Dwo2CrK6MH9CHbP2QicoN47dNTwCdbsSazgj6ujToOeXTXBFbM8W_x5Lq0hu-yrC4SNd4_nMEtbJDf7b5iyQLUMJke8DM6-S_ZyoejA6EZ_LAXKlLkHifdTJPXpAtbqpd3WbkbKQP16SlYWMS1qjb5WiPEr0StbdC9N8_T9l_dsNrAEy2Ok4Wuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2eb91028.mp4?token=K8ErV3j08SGaGCEBT-TZTEOPuGCLYzAgpP5jo3Gflcf_N_4DeGWclEeZ2g8UPJKX16f0Jw0SE0TFRPfTXuC-c1uqbJ1LWVRFNO0vKiZ11Caf6CTFRJDU2E1k1h1p_qIMXX_4pibu4huuLEROziyWINwmnPDIsC3gAdMduWDBt2bezgI-wfpTUFwwJXViRN2CCvRnXxAkinNmrCKKTtpnru6xDlanE2tbNeao_bhigd-w47Fv2Kjw3oTqRy5pBHvsghfU2OkexWgv4CNhne5QTVlOMYG2fJkKfTZe0eGAPQc5mlZjqC7JyGWN67uJQNCGmyiAW22YF08Lds2CnwV6an4WATktYt8PwVBO6Qf9CWZPBoPrreXCRxFM10r8TjNBnPCeNzGo5j41dFn8_gxt87ZJ4-N9jpKXXUvSdRqxZYZ7ydYX8b-KaJYfZEnAEYgtiZUVQOvMa6QCCd4GdADY7jVEYHzNfmkpZej3Xc93tBf4dRnQLVJ_Dwo2CrK6MH9CHbP2QicoN47dNTwCdbsSazgj6ujToOeXTXBFbM8W_x5Lq0hu-yrC4SNd4_nMEtbJDf7b5iyQLUMJke8DM6-S_ZyoejA6EZ_LAXKlLkHifdTJPXpAtbqpd3WbkbKQP16SlYWMS1qjb5WiPEr0StbdC9N8_T9l_dsNrAEy2Ok4Wuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش این گروه، گروه اسلامی "تحریک طالبان پاکستان" (TTP) یک حمله با استفاده از پهپاد علیه افسران اطلاعات نظامی پاکستان در شهر پیشاور انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/146066" target="_blank">📅 13:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146065">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jaxD82p84EFUUiBNB4m1MWj90KcE7sx_jbtVYcVXCyahFHkspkrmV5FE1EFGrE_TO11apNpe1vh-jrJyp8scuYO3qttOn0IjDe1NuApojVBy6P02VvRPLCnfZc3BEkYpsuX_7rLnpZkE7n9GuxJMYymdJvbosx9QgfC9ykaj5quKDsKaA24mRJfI3pUZt3WhUQ7HEYA2iYrVzEbcOT8sFRq2RedSz-a0vctTFLRvmtp02eDwhzCF_cz-5EntEaUzxBKJ8VtZhBR6GifHlpk-VcW459ANrOI8NCArV9Xyog0uaxPhoEiZTuZmuO6iIdoygo7Z-BxmmebTfvm_fCE5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال با استفاده از Ai
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146065" target="_blank">📅 13:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146064">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvT1R2SCEbQmAIzu7GsvTzORqpyGQcdPSe5xHjaRchrIXLmNoaFQIPUn5GY_rHq6aR_Di4JNubSPQ1wBelaMHO6MTtSvOCWckyaHVqSz00vQ8KWTbbyCRuLUm-FCISg0ypeiYqPym4e6aQqJXgFBQ-pXU2RSlk-UodgCjmMpPQjEW7ljon7P3ViHxSVZj9lzPzAElqkpowKc7oc22sSbHVSTtwMX32ZicMX4imRH7QNVxdVlC4oC8DGhb28GYiKQlhuTJJdX0aoWbb-uei3Kd9-cEBJceQh0PzcbNXKQyqpN6VYK4zTnyvNzeNWnIGjvLU7XHOy6hyOm853OQc1Kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زمین‌لرزه‌ای به‌بزرگی ۴.۴ ریشتر در عمق ۸ کیلومتری، بوئین‌سفلی کردستان را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146064" target="_blank">📅 13:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146063">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx4_y3X72Q69QyxQqPY_aleiVsi6B-x1fix9YhkdsL8e-G2D9Kimwaz9fOCQRdMcCZaSwrbo7PQgM03ju7kgRo9UTnnfqe3ZVqBjV8BozLXBjebWAqQ_zZxaT4kgBi8BR9dxuXQm0QFl4JUH3TnmAapOuvlYaYHyVbg5j7G956YkUW_1e5909w0qiKoy67D44nA7H60W_mnaA9t8I1kA9n0-zg3AomZmlUlyFFSAXEkXKThRgsahQ-AsgV7OhvHhR174KQeBVKZEiEYZFBFWmV9KOAZb5h6JzBYfO-LKJkorUtbpozal_uJ_5_3DpSR-D2DwxKfzh629C2us53ameA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی اسرائیل مناطق نباتیه الفوقا در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146063" target="_blank">📅 13:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146062">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b643721ea6.mp4?token=WgveawNLZfZm2pD0QkD0npM1_r1zv2NnJnkja9fKZVK2OZM-0dLLvU2Isq83GaG47B6hqpWpK7sbBxAe3hR8fS3RcfROMY9yKe7LW_ARbkO16x72l6gqB8I42LJsVCCveIgVSIZnFY-V255XfeJIDM6yiYMoG8974KCo1Q18zAUe3oOZI-qkbyX6fyXERaPbhFO8PRngFPURme440RTcrQ9AHZNW-FnCWX89CjD_CuOodGuhKSobyDViPbijKY37AiON8evciCKidg-A6nCxq-oduk20ERoww_MUYjav3XGqxy_uBJJ0OqgZKTCz7JhzBJd83uGrVqi9UEVCK90DXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b643721ea6.mp4?token=WgveawNLZfZm2pD0QkD0npM1_r1zv2NnJnkja9fKZVK2OZM-0dLLvU2Isq83GaG47B6hqpWpK7sbBxAe3hR8fS3RcfROMY9yKe7LW_ARbkO16x72l6gqB8I42LJsVCCveIgVSIZnFY-V255XfeJIDM6yiYMoG8974KCo1Q18zAUe3oOZI-qkbyX6fyXERaPbhFO8PRngFPURme440RTcrQ9AHZNW-FnCWX89CjD_CuOodGuhKSobyDViPbijKY37AiON8evciCKidg-A6nCxq-oduk20ERoww_MUYjav3XGqxy_uBJJ0OqgZKTCz7JhzBJd83uGrVqi9UEVCK90DXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویروس کرونا همانند دوران اوج ، از سطح هشدار، عبور نکرده است
🔴
معاون بهداشت وزارت بهداشت:
برای پیشگیری از ابتلا به کرونا و آنفلوآنزلا، همچنان رعایتِ نکاتِ بهداشتی در اولویت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146062" target="_blank">📅 13:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146061">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fec8ba7a.mp4?token=AvNGr8LOOrTgZL5gsm4fBcKr0l_ajMJUyk1uh-dtDFljKE8Y17_GMk7WGVj3M4I57sVZfSm9GGvBNQP4Zn0ftdvu7l-V1Lesrk3An8hQSPkF_eQaRkoAZsLnyZ6YB2LLTPiJdOW-565sLOcRZPbftyEmdn7VEZLAfYSWj-eUgzfidJ7PeG72TzNPMUFkwHxt3pcvqmEy4AeWYwwOqcsHiodaOQJN6kH91qnhVTJplzC522la8q8nzyVtSmot0xsWfjfi2A4onaNW0S7CUxCW_ALoATRQG1znX98NJBuJj85_77QZjdcPSbV-h_wNPll9JfFzcEfkv1CvXa7b4DWQEINxkYLIBd7vRjeKOONEYUSaHHOyZlzealpKoJ0yjRBfx7GcsdbCyPtVUi410bMjzf6FjZ9Yo4HbwuHuAsRBxsC81tndQjBCzoDP3RZpqaR90BFDTkY-gxjLfu7NgQ1n7TihUlHCJbqfh_Yo1MHC6JpDg84AN62voaG693ROK4G7p9oABEZjYZw3dJVIDD6VPK-2TqPWd428i2MoPTfJQ1YYwibmxd34Gmp0OEBP9IGonmMEyCysbhBTQIfGuDdrfvh5vq_S2tOc5KBeZx33AWIUvsPJym64MM35CsF4olvLMEOLP3_SYEIhr2koMwDxcZTTAfrh3EbDxuE1gSG7IY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fec8ba7a.mp4?token=AvNGr8LOOrTgZL5gsm4fBcKr0l_ajMJUyk1uh-dtDFljKE8Y17_GMk7WGVj3M4I57sVZfSm9GGvBNQP4Zn0ftdvu7l-V1Lesrk3An8hQSPkF_eQaRkoAZsLnyZ6YB2LLTPiJdOW-565sLOcRZPbftyEmdn7VEZLAfYSWj-eUgzfidJ7PeG72TzNPMUFkwHxt3pcvqmEy4AeWYwwOqcsHiodaOQJN6kH91qnhVTJplzC522la8q8nzyVtSmot0xsWfjfi2A4onaNW0S7CUxCW_ALoATRQG1znX98NJBuJj85_77QZjdcPSbV-h_wNPll9JfFzcEfkv1CvXa7b4DWQEINxkYLIBd7vRjeKOONEYUSaHHOyZlzealpKoJ0yjRBfx7GcsdbCyPtVUi410bMjzf6FjZ9Yo4HbwuHuAsRBxsC81tndQjBCzoDP3RZpqaR90BFDTkY-gxjLfu7NgQ1n7TihUlHCJbqfh_Yo1MHC6JpDg84AN62voaG693ROK4G7p9oABEZjYZw3dJVIDD6VPK-2TqPWd428i2MoPTfJQ1YYwibmxd34Gmp0OEBP9IGonmMEyCysbhBTQIfGuDdrfvh5vq_S2tOc5KBeZx33AWIUvsPJym64MM35CsF4olvLMEOLP3_SYEIhr2koMwDxcZTTAfrh3EbDxuE1gSG7IY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری دسته‌جمعی با بیل و چماق در سعادت‌آباد؛ ۱۱ نفر به دام پلیس افتادند
🔴
درگیری دسته‌جمعی میان چند نفر در محله سعادت‌آباد تهران که با استفاده از بیل و چماق به نزاع و ضرب‌وجرح کشیده شده بود، با ورود به‌موقع مأموران کلانتری ۱۳۴ شهرک قدس پایان یافت و ۱۱ نفر از عوامل این درگیری دستگیر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146061" target="_blank">📅 13:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146060">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
لغو خروج صیادان بازداشت شده هرمزگانی از امارات
🔴
مسئول نمایندگی وزارت خارجه در هرمزگان: بلیط بازگشت صیادان دستگیر شده در امارات به بندرعباس صادر شده بود و همه هماهنگی‌ها لازم بین مسئولان ایرانی و اماراتی برای بازگشت آنان صورت گرفته بود.
🔴
در آخرین لحظه، طرف اماراتی بدون ارائه دلیل موجه، از خروج این شهروندان هرمزگانی جلوگیری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146060" target="_blank">📅 13:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146059">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خسروپناه، دبیر شورای انقلاب فرهنگی: امروز همه نهادهای ما باید پهپاد بسازند؛ پهپادی که اف‌۳۵ را بزند، چون فضای هوایی را مورد تهدید قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146059" target="_blank">📅 13:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146058">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7d7ebd36.mp4?token=A7RXFUcQBJf0s3tMdHU-qVMRe0a2vo_ukQJVdd_YfXmm9j4Vrkrik2eVCfcn5RekHPFGQokbmkv1tcAee2-hzQny52DeIOzsbSkaofRo8yayTB_5KkE94aPdR7k-WKcHMC0Ep3q5XpnTYtdc9gLOvHkjjx0d_RXYa-kHkrcikuA2cS6ULpcLi_Sncjrkz0a12ecARWOzempIHpjcXVANQdwqia3IMDQFZ83-vuwfc1l78HRL4lM0rOxHlbPxdp1lqJDnnfsXSbAq13M6VOhieAQKJNrZiyF1rFDXvC3E-SLkVnaAw7UbktDtWmf_oz6fGjwzDIr3fGs_yuMZZGirVpoNS3HSLW4lXdnB52fg4yWf4A2DJPOhM0jRuY5EyZ7wWUUYwpJDuIxvg9DQs8pU73bFwPLsgaUK8FmRJVsLiG7BxbEiC-eXFxOXDkb1aTm0dwzrNqSZ5zdZEc6AVovxCmYVGz5FcreHFPfFdoU1DR1PD7_cayVe8gqsKr55ao7CyXkpBqCCFVMRKE05MB3Ns2bbA82ueTe-Og6On7jKUBVstrsZb8Gpy03CdiVee40m-ZErU2ZTXYlyAyB9KzpnvlHHqZ_-bCVc4oAIQ0LRLcBlQfhOg9Bs5dcyNKDLjOrfCZMytn2-UKtSuQwuEcnEusb9nT6UMNHYHsezxqTUSG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7d7ebd36.mp4?token=A7RXFUcQBJf0s3tMdHU-qVMRe0a2vo_ukQJVdd_YfXmm9j4Vrkrik2eVCfcn5RekHPFGQokbmkv1tcAee2-hzQny52DeIOzsbSkaofRo8yayTB_5KkE94aPdR7k-WKcHMC0Ep3q5XpnTYtdc9gLOvHkjjx0d_RXYa-kHkrcikuA2cS6ULpcLi_Sncjrkz0a12ecARWOzempIHpjcXVANQdwqia3IMDQFZ83-vuwfc1l78HRL4lM0rOxHlbPxdp1lqJDnnfsXSbAq13M6VOhieAQKJNrZiyF1rFDXvC3E-SLkVnaAw7UbktDtWmf_oz6fGjwzDIr3fGs_yuMZZGirVpoNS3HSLW4lXdnB52fg4yWf4A2DJPOhM0jRuY5EyZ7wWUUYwpJDuIxvg9DQs8pU73bFwPLsgaUK8FmRJVsLiG7BxbEiC-eXFxOXDkb1aTm0dwzrNqSZ5zdZEc6AVovxCmYVGz5FcreHFPfFdoU1DR1PD7_cayVe8gqsKr55ao7CyXkpBqCCFVMRKE05MB3Ns2bbA82ueTe-Og6On7jKUBVstrsZb8Gpy03CdiVee40m-ZErU2ZTXYlyAyB9KzpnvlHHqZ_-bCVc4oAIQ0LRLcBlQfhOg9Bs5dcyNKDLjOrfCZMytn2-UKtSuQwuEcnEusb9nT6UMNHYHsezxqTUSG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتباطات: مردم حق دارند به شبکه با کیفیت و اینترنت پایدار دسترسی داشته باشند
🔴
از این حق اصولی و شهروندی مردم کوتاه نخواهیم آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146058" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146057">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
گزارش‌ها از لاذقیه سوریه حاکی از وقوع تیراندازی در داخل دادگاه جنایی این شهر است که بر اثر آن یک نفر کشته و یک مأمور پلیس مجروح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146057" target="_blank">📅 12:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146056">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نشست فصلی شورای حکام آژانس بین‌المللی انرژی اتمی از امروز در وین آغاز می‌شود؛ نشستی که می‌تواند آغازگر مرحله‌ای جدید در پرونده هسته‌ای ایران باشد.
🔴
آمریکا و سه کشور اروپایی در تلاش‌اند قطعنامه‌ای را به تصویب برسانند که زمینه ارجاع دوباره پرونده هسته‌ای ایران به شورای امنیت سازمان ملل را فراهم کند؛ اقدامی که در صورت تحقق، نخستین ارجاع پرونده ایران به شورای امنیت طی حدود ۲۰ سال گذشته خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/146056" target="_blank">📅 12:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146055">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ایران: مشارکت کره جنوبی در عملیات نظامی در تنگه هرمز پیامدهای وخیمی خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/146055" target="_blank">📅 12:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146054">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: پیگیری پرونده ۳ خلبان ایرانی با اعزام هیئت فنی به قطر ادامه می‌یابد
🔴
سفارت ایران آزادی شهروندان بازداشت‌شده در کویت را دنبال می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146054" target="_blank">📅 12:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146053">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">اگه تحمل بی حجابی رو ندارید وانمود کنید که ندیدینش، همون کاری که با گرونی و فقر میکنید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146053" target="_blank">📅 12:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146052">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
تو این وضعیت اقتصادی یه چیزی رو برادرانه بهتون بگم:
رفیق گلم تو کشوری هستیم که بدون درآمد دلاری نمیتونی امور زندگیت رو بگذرونی.
🔵
با حقوق کارگری چند سال کار باید بکنی تا یه پراید 500 میلیونی بخری یا یه خونه 5 میلیاردی؟ تا کی میخوای شرمنده زن و بچت و آرزو و هدفت هات بشی؟ میخوای زندگیت تغییر بدی ماهی 500 میلیون در بیاری تو این کانال عضو شو ، نیاز نیست هزینه ای بپردازی
💰
:
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/146052" target="_blank">📅 12:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146051">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEXGwcdL_Rhja0IDSxzGXlb_lDjkQBwyDcnSluRFCTJaH6JA6vupLOfqoqqIIlF69PcwONpZFY-6nPUsej4ZFWIRMdTcY2Tcn1kRauahGAv9W5vcKPEwFP4oW6C4RvmmUTL3_UDOz50NCscpE_QZ9mRYA5GkTyXCQehc_JbcO3ar5QepL2YX3pt4dmMfiU9lIEE-nBkZzG7bR4IolHk5L8X0yP-zUL7EJWyJO16_1WFVUvG6CjzHnsw-UJcqqQmPpjTgGbY85_S9PnFzrrZ_2HFQIpYOgG_2y22wO8va173iIW0pJ9mWDWEUc64eCdUxJhJs8ZLqTE0EWoZQCZdkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسروپناه، دبیر شورای انقلاب فرهنگی:
امروز همه نهادهای ما باید پهپاد بسازند؛ پهپادی که اف‌۳۵ را بزند، چون فضای هوایی را مورد تهدید قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146051" target="_blank">📅 12:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146050">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که یک پهپاد شناسایی-حمله‌ای مدل "وینگ لونگ ۲" متعلق به نیروی هوایی سلطنتی عربستان سعودی را صبح امروز، در حالی که در حال انجام "عملیات خصمانه" بر فراز استان البیضا بود، سرنگون کردند.
🔴
این سومین پهپادی است که در ۲۴ ساعت گذشته توسط حوثی‌ها ساقط شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146050" target="_blank">📅 12:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146049">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06303045.mp4?token=b_an5Qj9qXX4htgZSkSg6JZHo_4qPvLeMipp1dZTAuNogCqs4Dl-kfvnas7UQ3wUgzxzbEIi_vu2Y8M_uGOpHxqxHqFrc_SUshjTQL-Qa1WQLUxfEIp9N0Gxlbz-ssqLu4rO-OkukEV3teGeW0Ht3pdQtzYbC9YbToJ93yePx0bOJ9PMtf7kvgg3fJZlOEtV8q5yVKzsIbQgHFD_lQKC6MfALgpymk9g70NqE8v7u7LsWRHlDVpBPBsB7DUYC2gGo6jxX4BF2MbQurnL4YMvJbviGpI_4NfwTrqTDCosd8sxBPK5dGQRxaMYHmKEJPEQQMy7JKxK0_ehbJBw57p2fUWZcfBX0QHAgCsbIVDksSu4mUiZwyKv1b3reawLvOI-FmrU8tk0u8Engla5quAlIYyjiQBLPqMKOdp3FeCIw1CTLNJyjbxfjp6VreNWGRK5Jvv_6kXyhKvY0VCNMPoCcRy6NAxzrniVQZ2AaLlsdO8edKIIz4wjfJ11SQRhftB6bVZcViet1TwUsP--vPmXJRwChM_Pmkoouu_chabXi-zq-VFfHBZDCL6NPlWQBEfy_XJKS3cAOkmt5vvkGFPw4MxgxdgivFbIEvTCqtlBvskuzxAiPF2anVzJp81jt1Ifw5oUZvVCivslG_53hQMp_LEttjypbRIEpWHk2uYqnpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06303045.mp4?token=b_an5Qj9qXX4htgZSkSg6JZHo_4qPvLeMipp1dZTAuNogCqs4Dl-kfvnas7UQ3wUgzxzbEIi_vu2Y8M_uGOpHxqxHqFrc_SUshjTQL-Qa1WQLUxfEIp9N0Gxlbz-ssqLu4rO-OkukEV3teGeW0Ht3pdQtzYbC9YbToJ93yePx0bOJ9PMtf7kvgg3fJZlOEtV8q5yVKzsIbQgHFD_lQKC6MfALgpymk9g70NqE8v7u7LsWRHlDVpBPBsB7DUYC2gGo6jxX4BF2MbQurnL4YMvJbviGpI_4NfwTrqTDCosd8sxBPK5dGQRxaMYHmKEJPEQQMy7JKxK0_ehbJBw57p2fUWZcfBX0QHAgCsbIVDksSu4mUiZwyKv1b3reawLvOI-FmrU8tk0u8Engla5quAlIYyjiQBLPqMKOdp3FeCIw1CTLNJyjbxfjp6VreNWGRK5Jvv_6kXyhKvY0VCNMPoCcRy6NAxzrniVQZ2AaLlsdO8edKIIz4wjfJ11SQRhftB6bVZcViet1TwUsP--vPmXJRwChM_Pmkoouu_chabXi-zq-VFfHBZDCL6NPlWQBEfy_XJKS3cAOkmt5vvkGFPw4MxgxdgivFbIEvTCqtlBvskuzxAiPF2anVzJp81jt1Ifw5oUZvVCivslG_53hQMp_LEttjypbRIEpWHk2uYqnpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه و کره شمالی یک پل جدید را در امتداد رودخانه تومن افتتاح کردند. این پل دو کشور را به هم متصل می‌کند و با گسترش همکاری‌های نظامی و اقتصادی این دو کشور، اهمیت این اتصال نیز افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146049" target="_blank">📅 12:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146048">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در صورت صدور به‌موقع روادید، رئیس‌جمهور در مجمع عمومی سازمان ملل شرکت می‌کند
🔴
نمایندگی نیویورک تا اعزام سفیر جدید توسط معاون نمایندگی مدیریت می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146048" target="_blank">📅 12:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146047">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37f1a3a50.mp4?token=FDtmEPACsgx0hs2CJuyfw372WNP2lQgTmgRlNOLdxAKrAIBKFm3aT-wZMbc69rXXZRlB5kI3l4j2XBMGVyfkbENJ1msmX1P5Wa6QkxveqGt9vgDd-HL1hzl7z1C2Zjp6jkzrzoUVFRfl-rB_Rvu6f2xpbVyR1P2s7TEdI1lTAl1PDd9_LxMKHd1-FyeB2kdmQIUhB4AZsygZCIZqTlHBNWH7Xza_w4ZUmenJ8GJeaOynMLnSjJq0YrkleD3BPHB_3sTts58psaYJkN06Hgn5O6bfz1DoOHeB5CZzBepvcSJymeZpuD4nQBieKifGuwqZOSnJvgsrj3GU6AatEfTaeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37f1a3a50.mp4?token=FDtmEPACsgx0hs2CJuyfw372WNP2lQgTmgRlNOLdxAKrAIBKFm3aT-wZMbc69rXXZRlB5kI3l4j2XBMGVyfkbENJ1msmX1P5Wa6QkxveqGt9vgDd-HL1hzl7z1C2Zjp6jkzrzoUVFRfl-rB_Rvu6f2xpbVyR1P2s7TEdI1lTAl1PDd9_LxMKHd1-FyeB2kdmQIUhB4AZsygZCIZqTlHBNWH7Xza_w4ZUmenJ8GJeaOynMLnSjJq0YrkleD3BPHB_3sTts58psaYJkN06Hgn5O6bfz1DoOHeB5CZzBepvcSJymeZpuD4nQBieKifGuwqZOSnJvgsrj3GU6AatEfTaeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: رای منفی آمریکا به تغییر اندازه نقشه جهان شاید به علت کوچک تر شدن گرینلند بود
🔴
علت عدم حضور ایران در جلسه قطعنامه اسامی جعلی روی نقشه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146047" target="_blank">📅 12:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146046">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/70ee904e74.mp4?token=RKx5avryYHPOYbh3Chv0sPAgHdTYbtjmKJ7HAQm8sbIVBS5KWHE5zSZGKOEAPwY2WsqTpdqmSek4NBmmqrj7HyPB3c4QkbtD_4-MmFtBkr3-aQxjgYfLgLR4DcXvmus6s5JcApPQu2foSKfee_-nD5frmn35HrWqBn92Uy-QDD_IZLvRrMp4hrWRa9FUZY9AMjdap-k6448HnMBo7VkxGi8_YEKuax1dy0fwsqsgRUU2aCtnH8SrpOQRNxb7E4VjLdiKQ2jJHn8bkZmNRw_jEQ7V-hqkCo4kaLLGJqoE9UMzMLTExp2MwDefWuVfsWsSejyQ83BdQAsSVT6XPeT8_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/70ee904e74.mp4?token=RKx5avryYHPOYbh3Chv0sPAgHdTYbtjmKJ7HAQm8sbIVBS5KWHE5zSZGKOEAPwY2WsqTpdqmSek4NBmmqrj7HyPB3c4QkbtD_4-MmFtBkr3-aQxjgYfLgLR4DcXvmus6s5JcApPQu2foSKfee_-nD5frmn35HrWqBn92Uy-QDD_IZLvRrMp4hrWRa9FUZY9AMjdap-k6448HnMBo7VkxGi8_YEKuax1dy0fwsqsgRUU2aCtnH8SrpOQRNxb7E4VjLdiKQ2jJHn8bkZmNRw_jEQ7V-hqkCo4kaLLGJqoE9UMzMLTExp2MwDefWuVfsWsSejyQ83BdQAsSVT6XPeT8_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش بقایی به قطع ارتباط پرو با ایران: خالی فروشی کردند!
🔴
قبل از این هم ارتباط دیپلماتیک با پرو نداشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146046" target="_blank">📅 12:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146045">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5bb5afd21.mp4?token=upHvE2NXrwjbgX2LrWB0cfp4LEzqQEZIVq9AGVmTDANB-T5kB04IWRROu17-c35OQL5jgiONG1lff5pPFk1QdTAWvCZVi5hlO54p3mvkkDZIS2n6hoQiFJLGJLTiGHrhiNMnPYSs4j6irMQFAj89rHjS3T6LU0YHaeNo-OXuVsokM_GwNoc3phwm2wgC2KTMerQvsnybIZo9io8qF-Gtx2CArNA_ony6bgBqU6KILdAbCrQgucjQg3fGCEPmtd67PK8GFRYEoxeu3QDnivHYfVNgEt3yrg39TllY1Cxa0DijGWNTPVwi-2mXfMMeDHaP_xZclvrgcYEOc3KGax9odg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5bb5afd21.mp4?token=upHvE2NXrwjbgX2LrWB0cfp4LEzqQEZIVq9AGVmTDANB-T5kB04IWRROu17-c35OQL5jgiONG1lff5pPFk1QdTAWvCZVi5hlO54p3mvkkDZIS2n6hoQiFJLGJLTiGHrhiNMnPYSs4j6irMQFAj89rHjS3T6LU0YHaeNo-OXuVsokM_GwNoc3phwm2wgC2KTMerQvsnybIZo9io8qF-Gtx2CArNA_ony6bgBqU6KILdAbCrQgucjQg3fGCEPmtd67PK8GFRYEoxeu3QDnivHYfVNgEt3yrg39TllY1Cxa0DijGWNTPVwi-2mXfMMeDHaP_xZclvrgcYEOc3KGax9odg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: هیئت قطری دیروز در تهران حضور داشت و برای کمک به کاهش تنش‌ها دیدارهای خوبی با آقای عراقچی داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146045" target="_blank">📅 12:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146044">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxLFQKXLIpyKB6cOpNcVNIEXV_V3GbpzoFLf5UwfGiW-XSTy9QBqfYxtJUxivDV5RTNlGvP7U6YztqdxhoHyJLJWRog1abEG3SK9dolWFN9VfsGFrzrM-AhtnRIe_SMT9UrzddLa3o7XUmsnabu8ALiLJS1irrUoHMyyEaDlcdVo1mDANxGXRppCVmr1iNC4DmBX_BsM8Demg5XmJtke34w77q8vf3TDdTsOqVZjGFB7iRo2IJruug9zUmWA0vAGI8I4idqXtLnkivmp2rK1p-hJtW1A9PCCC1brMmLGtMAwNsbc5WkemOkiA75YLnvk2g11Z0Agd78_EgKOjI220g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف در پاسخ به تهدیدات اخیر پیت هگست وزیر جنگ آمریکا از استراتژی نظامی جدید ایران گفت:
🔴
ساده و قابل‌ فهم است: زنجیرهٔ تولید نفت و گاز در این منطقه گسترده و پراکنده، در دسترس، و آسیب‌پذیر است. شرکت‌های نفتی و گازی آمریکایی که در این آب‌ها و تأسیسات فعالیت می‌کنند نیز همینقدر آسیب‌پذیر هستند.
🔴
اگر به دارایی‌های ما حمله کنید، مورد حمله قرار خواهید گرفت. ما این توانایی را قبلاً ثابت کرده‌ایم. از پایگاه‌های نظامی‌تان که غیرعملیاتی شده‌اند، بپرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146044" target="_blank">📅 11:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146043">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت امور خارجه: ظرف روزهای آینده، تفاهم ایران و عمان درباره تنگه هرمز نزد سازمان بین‌المللی دریانوردی ثبت خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146043" target="_blank">📅 11:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146042">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فارس: نفتکش تحت حمایت آمریکا هم برگشت خورد
🔴
نفتکش TITAN HARMONY صبح امروز هنگام نزدیک‌شدن به کریدور جنوبی تنگهٔ هرمز مسیر خود را تغییر داد و به‌سمت جنوب بازگشت.
🔴
این تغییر مسیر درحالی رخ داده که قبل از آن نیروی دریایی آمریکا درحال پشتیبانی از عبور این نفتکش در مسیر جنوبی تنگهٔ هرمز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146042" target="_blank">📅 11:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146041">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بقایی: فرانسه، انگلیس و آلمان به دنبال تشدید اوضاع هستند/ حتما ایران در قبال اقدام نسنجیده‌ سه کشور اروپایی و آمریکا تدابیر لازم را می‌اندیشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146041" target="_blank">📅 11:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146040">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: جنگ اقتصادی آمریکا علیه کل جامعه جهانی و تجارت آزاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146040" target="_blank">📅 11:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146039">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر شلیک توپخانه در منطقه قنطره، جنوب لبنان منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146039" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146038">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b44caa0c7.mp4?token=ryz3o4JR6uWlxGhDutJvapB_nE-R7iy5CQqu3_x1QbtnoYWlkfk1Dxy7jsO0UZczGXCxgBusjhNHiYkY3cUPIX06711uyWWRKpPaM8dTZo3Y-yE5fK-cRDQpyMn_O3Xkkt3BqAWGjJe4x41QABrGQcMuMmB8yje3aJ6ewxZevrl8nRU_ZgCnSuYwDXDBv3hG5WvyvyQ8eDHEVDCOR2s4KXFosKVZCq1w-Xof3zcmTvc6f4oDiExcBlGQZCZCpV2q_K4Z1k87_KfSzKC96DOTCwt8tj_gMPMLnUECTVIlahDLsGFDRvb3fbuLcuk8mNks5ZlYTpkT2HWPGjK1Ietzbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b44caa0c7.mp4?token=ryz3o4JR6uWlxGhDutJvapB_nE-R7iy5CQqu3_x1QbtnoYWlkfk1Dxy7jsO0UZczGXCxgBusjhNHiYkY3cUPIX06711uyWWRKpPaM8dTZo3Y-yE5fK-cRDQpyMn_O3Xkkt3BqAWGjJe4x41QABrGQcMuMmB8yje3aJ6ewxZevrl8nRU_ZgCnSuYwDXDBv3hG5WvyvyQ8eDHEVDCOR2s4KXFosKVZCq1w-Xof3zcmTvc6f4oDiExcBlGQZCZCpV2q_K4Z1k87_KfSzKC96DOTCwt8tj_gMPMLnUECTVIlahDLsGFDRvb3fbuLcuk8mNks5ZlYTpkT2HWPGjK1Ietzbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئو وایرال‌ شده از بازی دختران محجبه در بازی مافیای نفوذی
🔴
در این بازی ترامپ، نتانیاهو و رضا پهلوی نقش مافیا را دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146038" target="_blank">📅 11:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146037">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فحاشی عجیب و بی‌سابقه علیه حسن روحانی در تجمع شبانه
🔴
اگر به خیابان بیاید دندانهایش خرد خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146037" target="_blank">📅 11:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مدیرعامل شرکت فرودگاه‌ها: ۲۷ فرودگاه در جنگ آسیب دیدند که آسیب‌ها در سطوح مختلف پروازی، باند، ساختمان های ایمنی، دستگاه‌های کمک ناوبری و بازرسی، ترمینال های مسافری و...بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/146036" target="_blank">📅 10:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F67U0D93ZhDTfrzmjsjfa79rYSp0XzlOgDGxowkTe7j8yRlgMUWx8BMsC1L8wklX4naHRhKoZcwZZuXZgKEZYvl0-iiYN2HPOU_AOmsdZeenRxIZwTjxdBPyiE2-QAyxQPiGGnRrpbNHUEPMkgln5jW_99v_fifzo3_SmZd_47e6wAor_6154FTYg_JOjqkDpejnZ0rzu1IClSbQihL2qGBdtYUuAan8jnabY4BgBOY6fXHhfhh21_hvYSUziZzwWheCZcI1G0mPivbKa_sF56EMyYtpUmFFa5FhLeS9_yRyKlZtQREpKy_cVIncvQcLQS619V-CblfWve0pg-dFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت به ۹۸ دلار در هر بشکه رسید
🔴
وال‌استریت ژورنال: افزایش قیمت نفت در پی تشدید درگیری‌ها میان آمریکا و ایران و بالا گرفتن نگرانی‌ها از قطع خطوط عرضه نفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/146035" target="_blank">📅 10:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146034">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رویترز به نقل از سخنگوی وزارت خارجه قطر: «ما در منطقه خلیج فارس باید درک کنیم که ائتلاف راهبردی با آمریکا امر خوبی است، اما کافی نیست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/146034" target="_blank">📅 10:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146033">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آمریکا جنگ را آغاز کرده، اما انتظار دارد تمام جهان هزینه آن را بپردازد و هم‌زمان ایران را مسبب آشوبی جلوه می‌دهد که خود عامل آن است
🔴
این وارونه‌نمایی، به‌ غایت بی‌معنا و بی‌اساس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/146033" target="_blank">📅 10:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146032">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بهای معاملات آتی نفت خام برنت تا ساعت ۰۵:۱۲ به وقت گرینویچ با ۷۹ سنت، معادل ۰.۸۲ درصد افزایش به ۹۷.۰۷ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/146032" target="_blank">📅 10:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146031">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY0t9Y_Ouylf_HA6aB_OVaamzp3wcgnvnB-ESYyEXX4o7XQFc4Wc9a5-bTVw5fvwZV3z618ahBd5RPmvQilMueMGMJ02vXEZBNSXSTbfOXh42rY4LnLhX8ZLMrOyyu0AvFtCdybTcAAj1Bp73LeBSE-svllj2PdTzbyhfpz1NEORKZBT_kSZsfeOirlnXc6TR20QpSU_I7L4Xr6-Bfk7H4lNhRfWQeOQLzoGIQzHEzNFkBnp_LbxILySCu45gU0qdy3gGmFz69E0G_Ve8l_XbI60bmUwPrmjjtL7ryDCL2RqcDkn9f9Ebs3CWTXFUw7lt04mFOcfD528z9pLFfoAiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کاروان کوچک از کشتی‌ها در حال حاضر در تلاش برای عبور از تنگه هرمز از سمت عمان است، و این کاروان تحت حفاظت نیروهای آمریکایی قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/146031" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146030">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
به گزارش الجزیره، حملات هوایی اسرائیل به شهر کفر رمان در جنوب لبنان که شب گذشته انجام شد، جان حداقل 10 نفر را گرفت.
🔴
در این حملات، 9 نفر در اثر اصابت به یک ساختمان کشته شدند، در حالی که قربانی دهم نیز در یک حمله جداگانه که هدف آن یک موتورسیکلت بود، جان خود را از دست داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/146030" target="_blank">📅 09:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87849029ee.mp4?token=apOYUI2fw4nGha8rboQEH2Cnkgt9T6tNmf72Du4pM-jE2qL5pHeUh2XWkGq7GUOx7dD7SoomGVPFbexmP1l5vxzZA-rf5Emw7cAw8k3P--aesFOcfCwvM3812T0MZ81htQ8wBHfbKSkZrLC0owDLIZu7zoiTo7Dfu1kWBMkI8d1JoQF-AsQXN5_15tdXA8tjNcSc1yrZnjiYMJnfP3S-kIREQefho9xWDI3JigaJ1sel5Fk655QpO7x2byH5vUwitwSeC8YZtGY1BCIxJ6rl7aw4_dv2svBAwf_gllgX9_h2jSsxBIszIh1tElFmXz0bCs3ex0CG5xzArPXYKaQ1xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87849029ee.mp4?token=apOYUI2fw4nGha8rboQEH2Cnkgt9T6tNmf72Du4pM-jE2qL5pHeUh2XWkGq7GUOx7dD7SoomGVPFbexmP1l5vxzZA-rf5Emw7cAw8k3P--aesFOcfCwvM3812T0MZ81htQ8wBHfbKSkZrLC0owDLIZu7zoiTo7Dfu1kWBMkI8d1JoQF-AsQXN5_15tdXA8tjNcSc1yrZnjiYMJnfP3S-kIREQefho9xWDI3JigaJ1sel5Fk655QpO7x2byH5vUwitwSeC8YZtGY1BCIxJ6rl7aw4_dv2svBAwf_gllgX9_h2jSsxBIszIh1tElFmXz0bCs3ex0CG5xzArPXYKaQ1xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشته در انفجار مرگبار مواد آتش‌بازی در مکزیک
🔴
انفجار مواد آتش‌بازی در جریان یک جشن محلی در مرکز مکزیک دست‌کم ۱۰ کشته و ۶۰ زخمی برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/146029" target="_blank">📅 09:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146028">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f89acc91b.mp4?token=BiZ9YK4s0cNMzuiiByuTelmCWg8iZCHX7MUIKWjeP3wMrL9bNvYZ9Z5Q_NAMd1qHzTWDcA2mu1guJ8KAU9ttHfmfbDcGwi4KgOvQRkb9RFa87RvvBJn-8XZUaAZih2unuPxXN3K6hef5jwV0oDlQ-X6BdF4wZf83Sj2HAR-iDFlChr_7zWkVUjBQd5PUaaKnnY97O5QFXiwYA4FCChc_-_DNoUlyuF5YRPwSFq9s3NXgDeiIYpHw2z0elFdw-NYFm6pa0tf27cRAdgjtbi_l_u06c-BROjFhONXEd_CylVHLoEponLZZ0FcUKwY7i20Z5jYdsLezCZpvIxphNMevSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f89acc91b.mp4?token=BiZ9YK4s0cNMzuiiByuTelmCWg8iZCHX7MUIKWjeP3wMrL9bNvYZ9Z5Q_NAMd1qHzTWDcA2mu1guJ8KAU9ttHfmfbDcGwi4KgOvQRkb9RFa87RvvBJn-8XZUaAZih2unuPxXN3K6hef5jwV0oDlQ-X6BdF4wZf83Sj2HAR-iDFlChr_7zWkVUjBQd5PUaaKnnY97O5QFXiwYA4FCChc_-_DNoUlyuF5YRPwSFq9s3NXgDeiIYpHw2z0elFdw-NYFm6pa0tf27cRAdgjtbi_l_u06c-BROjFhONXEd_CylVHLoEponLZZ0FcUKwY7i20Z5jYdsLezCZpvIxphNMevSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از پیامدهای حمله شبانه اسرائیل به دیرالزهرانی در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/146028" target="_blank">📅 09:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146027">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d1c3bb64.mp4?token=hdKiCZlU7isMAXWAi-DW-O9mE9fGw8LOQgSN00Hdj6Td6dspnRm8U1fhz6xeov0VuLxK0NAI6Vl0bax1XMPczXnj4asMzHojp2fyseM644DNbFHtsYrUN6oXz41-rzZW5Ep3fv6ORpLXWXq8TAoxT1DKbyH2FFwOM9APwmgxlUg5HwPvuZO5nLaQ4Wv6bB5epjyjexMV1QTuQAdlLwM8DbKAznUugML8Hwi_hIkfpVeI_ND5clOammRp456oaEeN88tsLeQvSEGJkJIp1ibSW_LhPPTPY5Ptn_cNKNyZxjAxJ47oWF55cjKZi96z8JBDy_Alz-fPOG7UROAsZxzXYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d1c3bb64.mp4?token=hdKiCZlU7isMAXWAi-DW-O9mE9fGw8LOQgSN00Hdj6Td6dspnRm8U1fhz6xeov0VuLxK0NAI6Vl0bax1XMPczXnj4asMzHojp2fyseM644DNbFHtsYrUN6oXz41-rzZW5Ep3fv6ORpLXWXq8TAoxT1DKbyH2FFwOM9APwmgxlUg5HwPvuZO5nLaQ4Wv6bB5epjyjexMV1QTuQAdlLwM8DbKAznUugML8Hwi_hIkfpVeI_ND5clOammRp456oaEeN88tsLeQvSEGJkJIp1ibSW_LhPPTPY5Ptn_cNKNyZxjAxJ47oWF55cjKZi96z8JBDy_Alz-fPOG7UROAsZxzXYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کفررمان در جنوب لبنان پس از حملات هوایی شبانه اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146027" target="_blank">📅 09:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146026">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=BikJyvv0dz4uIbyJpHGXBuWefVtFcyl_Cl-GcNKh7nDAStqBmfIwcAUeNVycayPCAjnbB9M8iWqWpuTb9WgCpuqlEiO5kvxbs0_CWOcYkKIVPZguSKTOif7VgjDFXmpv6RAoHyYLzDjkkiCWkFs0rMRGKlCG9LcLJux8pMVkcpzkNiU-cdUw_vaR3aaVptSgYwdg1ax4hMZgvdQSNA5ECQy0BtSc5V_B8Qt_aP-zl5HxIlnO-n9owp6fSwS2mBLLb6yXToQoJ8eCLHGGlTvO_M7EjFpsrINlU3lTCSMjwI-GSAzQLsG94a-HWHDnRaT8YwKbPZ-xVwX6OsHZrHqblzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=BikJyvv0dz4uIbyJpHGXBuWefVtFcyl_Cl-GcNKh7nDAStqBmfIwcAUeNVycayPCAjnbB9M8iWqWpuTb9WgCpuqlEiO5kvxbs0_CWOcYkKIVPZguSKTOif7VgjDFXmpv6RAoHyYLzDjkkiCWkFs0rMRGKlCG9LcLJux8pMVkcpzkNiU-cdUw_vaR3aaVptSgYwdg1ax4hMZgvdQSNA5ECQy0BtSc5V_B8Qt_aP-zl5HxIlnO-n9owp6fSwS2mBLLb6yXToQoJ8eCLHGGlTvO_M7EjFpsrINlU3lTCSMjwI-GSAzQLsG94a-HWHDnRaT8YwKbPZ-xVwX6OsHZrHqblzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید در شبکه اجتماعی X: «در روشن‌ترین روز و تاریک‌ترین شب، هیچ شری از دید من پنهان نمی‌ماند. آنان که قدرت شر را می‌پرستند، از قدرت من برحذر باشند…
نور فانوس سبز!
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/146026" target="_blank">📅 09:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146025">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=KvNb9ABKPX6c2TqJ4Ox6t0L2UJNr_Wf9VgnhSx0uvCWYKsVJd35aAi4Va4iwFfhBlFF5MWLEiURoezI9jAqPGJMVS6NoVk0363KFzAPARSBQ6Ki88zDsd0p1i1HHBTfjKROQ7VwYkcX_66aSIYOiK-y_qfXzyKMALPDSsQyMfIojaggOyGJzX60iOrMHSe1dcjZ1Zk8T7rI11VRKspMtLtEK7DII_bAb9CjSB6z-6onTPpAKUWEd0zmohSZARqBMQU0RlWoF7lLs6ubNFckKZttG0CV5a2mC-_NfrvaU88q0MGTHIXKQ-RSZ3BU3sAa-92N9Ijl3y0XXsWpcebwkmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=KvNb9ABKPX6c2TqJ4Ox6t0L2UJNr_Wf9VgnhSx0uvCWYKsVJd35aAi4Va4iwFfhBlFF5MWLEiURoezI9jAqPGJMVS6NoVk0363KFzAPARSBQ6Ki88zDsd0p1i1HHBTfjKROQ7VwYkcX_66aSIYOiK-y_qfXzyKMALPDSsQyMfIojaggOyGJzX60iOrMHSe1dcjZ1Zk8T7rI11VRKspMtLtEK7DII_bAb9CjSB6z-6onTPpAKUWEd0zmohSZARqBMQU0RlWoF7lLs6ubNFckKZttG0CV5a2mC-_NfrvaU88q0MGTHIXKQ-RSZ3BU3sAa-92N9Ijl3y0XXsWpcebwkmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی لحظه خروج هواپیمای باری آمازون از باند فرودگاه بین‌المللی میامی در روز یکشنبه را نشان می‌دهد؛ این حادثه به کشته شدن ۵ نفر منجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/146025" target="_blank">📅 09:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146024">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزارت نیرو: تاریخ دقیقی برای پایان خاموشی‌ها اعلام نمی‌کنیم، شاید زمستان هم برق برود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/146024" target="_blank">📅 09:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146023">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhIF8SXv6Dfe186PAOfKLSrbzJEg6oMCNypU3SuAUALIu0hjWvliTfZ03eSPvOeTefQTxThKmHbzZxX_KLqkYNhBwlBpC_0qiuhvjohN6T_lXmk_6HMJU5vNZx-78-OyrCP0Qb1Qn-Dd1Ayb5TmsMjpLFN2Fh8Trsxmwdr6DjmCnssA4H8C9LiDne1kTrAtEQTUCRS8PY7G0dGv0QUj67xI0peg5n7eFm0zMhZN8XYtLrPU9apWz7kT1IZresspuwLDylfy1fzlSBMd6i3kU7ZFrlClAFAtyyvTDiv0QynbQbn7UAoZ20ZAeJQlLOFTb7gQnMnX2zrA_kOZuH-WIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):
برای تخلیه یک ساختمان در
دیر الزهرانی
در جنوب لبنان هشدار صادر کرد و مدعی شد این ساختمان متعلق به حزب‌الله است.
🔴
ارتش اسرائیل از ساکنان خواست حداقل
۳۰۰ متر
از این ساختمان فاصله بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/146023" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146022">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سپاه اصفهان اعلام کرد: عملیات انهدام کنترل‌شدۀ مهمات امروز از ساعت ۹ تا ۱۴ در جنوب اصفهان انجام می‌شود و احتمال شنیده‌شدن صدا در محدوده صفه، بهارستان و اطراف آن وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/146022" target="_blank">📅 09:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146021">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
آتش‌نشانی: آتش‌سوزی گسترده در هتل آپارتمانی در مشهد
🔴
۳۰۰ نفر از میان دود نجات داده شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/146021" target="_blank">📅 08:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146020">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۵ ریشتر ساعت ۷:۳۱ صبح امروز در حوالی دانسفهان و شال در استان قزوین به وقوع پیوست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/146020" target="_blank">📅 08:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کپلر از کاهش بی‌سابقه تردد کشتی‌های باری در تنگه هرمز خبر داد؛ میانگین روزانه تردد به ۱۰ فروند رسیده است.
🔴
شنبه فقط ۲ کشتی و یکشنبه ۶ کشتی از این مسیر عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/146019" target="_blank">📅 08:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146018">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آمریکا جنگ را آغاز کرده، اما انتظار دارد تمام جهان هزینه آن را بپردازد و هم‌زمان ایران را مسبب آشوبی جلوه می‌دهد که خود عامل آن است
🔴
این وارونه‌نمایی، به‌ غایت بی‌معنا و بی‌اساس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/146018" target="_blank">📅 08:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146017">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np7OZBhlTSKj5dgjsyvtnjghmHn_lc_2OWR2a7WdPIfUnefcA8_H_LngATB4tZPYRmt7xQhjhnmhxNr6DYKt6qeI62u4BOUZ-yMVjPlh9uO4NsmbzskNrScNtG4YRd01ulktd7A0u1ym47B2y4206RpnAy299s_zuc8eA-CnmoQ-t4cKa4PErZypqk1m9Q5K6B6FuRWiUorsbp3-BIgneWza-y4uoGIl0vkYl-i2N7V7mbYmCcJ934LC29CPvI88j0Vhzj994aZzk-R_kxjS5T952q5BoM-LFmMqgHIXOzBuvZgpCfAiVjYFZ3do8KFvhlIGFhB7eMYmeE4iWpAEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید تروث سوشال ترامپ که یک یونیفرم برای نیرو فضایی آمریکا نشان می دهد.
🔴
جالب است که این یونیفرم شباهت بسیار زیادی به یونیفرم نیروی ها امپراتوری (نیرو های پلید) در فیلم های جنگ ستارگان دارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/146017" target="_blank">📅 08:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146016">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b63173fb93.mp4?token=t2OiCBwQbso-HVwBRSCQm8y5tac79VXYrfZYyykVhvOtqNp2h8Xvwh9j0HRHejcxFQtG5eBHFSjejrU6NGTaDHrZFmTXwWR46vrRYg5ZILEM--EC36ffzdkcX9lzGIZwzcFMiGi6yz9ndKjChHyqO-eP5nk-nZ01G-l2adSPN-FR311gykXCfc2hesFpb8PgXqhn2bCAhegXcV18X5gMIRsR7n6hQ0xXyLY7IH6dZ7u_5Yl_SOhKx7hWluZkmLAaZOOfTfA9iJIwTdz1xIgK-JC7L3kj-7TBBz396BjDCnufw5ecwyZoVNjuCmgxqDB34qEd4gkOp_h24cGSGMbVXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b63173fb93.mp4?token=t2OiCBwQbso-HVwBRSCQm8y5tac79VXYrfZYyykVhvOtqNp2h8Xvwh9j0HRHejcxFQtG5eBHFSjejrU6NGTaDHrZFmTXwWR46vrRYg5ZILEM--EC36ffzdkcX9lzGIZwzcFMiGi6yz9ndKjChHyqO-eP5nk-nZ01G-l2adSPN-FR311gykXCfc2hesFpb8PgXqhn2bCAhegXcV18X5gMIRsR7n6hQ0xXyLY7IH6dZ7u_5Yl_SOhKx7hWluZkmLAaZOOfTfA9iJIwTdz1xIgK-JC7L3kj-7TBBz396BjDCnufw5ecwyZoVNjuCmgxqDB34qEd4gkOp_h24cGSGMbVXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درحالی که ما داریم غصه دلار و قیمت ها رو میخوریم یه عده رفتن شمال پستونک پارتی گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/146016" target="_blank">📅 08:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146015">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKPGrIMFLnUK_sq_3ekkhOTWQ3pOJBROQ_7WTpQ5U3fiQAvfj31afNR7N_jT2yF27KwrO4Bk0afPqEZ1ElC0lrOoHIUrlufAOiL9Nr1Nb71_s2FP-_s1PKgOHoe8KurrOvL1rh3EmEQE36btqs3zLJJcjuXuQbY1AISvnQ-kW9WIE8aKBbJFSisMHu6Wb0jO_zdCJslTZRQ5fi6SlzSgp1ycMKJMlAW6ofvcUaQnXaLM1O8cGWRmgOL6FmeRccLaeqwKqAvUruwQiQxZgGdu8A83UgUjB-1aSA2le2hfMqFPZ78kmmWtuJ-is1aRJ9OUqCH3fil47l3Mx1oRm2gpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: برای آمریکایی‌ها جهنم تدارک دیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/146015" target="_blank">📅 07:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbZ5-gqufNT3iUgP8OrHZ7VV9XhRYENdAKpIyuV6eaj2SO8xWnaGwlyf_R18MKF8vFOtvYzx0KYkifhfGGDkatXIGt-FJlXz5MfGsweuCcrTBvCQwLsDpUBV5fWC27UUTzSObUu-XlSjUpbQnDlMieBSB3g3jNvLaByWIueS63jiLynXmTxt-CRP9JYLh8nsEBx5DfVksdSeUBPmf7zd_vEZ539-bzbz6UVA2JIoWL1smq7xUCagxlp05wDsqfqBP4NJztWS1fE-HKeFq9_hEbps2WOCZZX_Ea96qn6SHGjHq2IpX1cZO0KJjM2MsORNSqRQs_WhCzQyCUxxbP-fQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">LIT VPN
نسل جدید فیلترشکن
🔥
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
🔥
فیلیمو
و
فیلم‌نت
و
نماوا
رایگان
‼️
سرویس نامحدود فقط ۱۷۹ تومن
‼️
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کدتخفیف ۲۰٪:
IRAN
❤️
ربات تست رایگان و کانفیگ:
@
litvpn_bot
🔥
ربات مخصوص
همکاران
:
@litpanel_bot
🔥
پشتیبانی
۲۴ ساعته:
@mahan_lit
🇩🇪
•
🇫🇷
•
🇳🇱
•
🇦🇱
•
🇦🇪
•
🇴🇲
•
🇸🇪
•
🇪🇸
•
🇮🇳
•
🇺🇸
🇨🇦
•
🇯🇵
•
🇹🇷
•
🇮🇹
•
🇬🇧
•
🇺🇦
•
🇷🇺
•
🇸🇬
•
🇪🇬
.</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/146014" target="_blank">📅 01:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgIYgtCTXSiRQpN_6R6CB_WIrQ7QZXDVAS7bwTk07JnJBHXnWcN8gFRp8b3tALioMTwQ_w89vIJoZjt_TWlsU3Weu8MOo9tTZcx4u8ZHo1ZwZmiePeG7X24Xuc9xgU6WPumNT1xWzRRioK-S8ZOqP1daMiq4GzWNAeeDP71tLC6WHykjzwn1w7-1YK4KXHTbVv0ebH-x5gsdukjGQyNCcGc-k46XwdJoSTxHt71Pde188iGpEgPDS08CXsS8EQS2rTI1dqkA7V3UTGZhRRG6poyLXyKPxBH5txBJ0ku4pfyzWJOLi0pHZ2OBCZDYjizXi-5MpNHNpF_gp-qDBTevpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش رویترز، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دستور تخریب سکونتگاه‌های غیرمجاز شهرک‌نشینان در سراسر کرانه باختری را صادر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/146013" target="_blank">📅 01:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146012">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e8536959.mp4?token=VPtnr8znSXNKIRd9YtMCneA3R8tYUlEZUeIXBfJ0Nr1QkmBfkwo2jO7yVILN-3s-Tjbz8NbmLnxNYALxUOVHL-WzMF7xx1devVqOSZSkk33ZYAYHUtN1FAGdQoKoK-z6e9q93InCrUTX0ZtDKsjL3KoiSefGmZ_DLobAdsng7xudddpgN1hd7j711ym9WB-iEl6qA4FFZMWPj7hYXCp-U4wSgOxkCafw_-70NJW232kwaQ50UL_ggpYINaM65cMaxKM-AmqFVWQKBYhHYdHYy-NsvykyuYFiYSj07sPkEeoT04SwTtmUOJZEgkO0HTUODtSr4t2OCk2KNIWZsTcacw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e8536959.mp4?token=VPtnr8znSXNKIRd9YtMCneA3R8tYUlEZUeIXBfJ0Nr1QkmBfkwo2jO7yVILN-3s-Tjbz8NbmLnxNYALxUOVHL-WzMF7xx1devVqOSZSkk33ZYAYHUtN1FAGdQoKoK-z6e9q93InCrUTX0ZtDKsjL3KoiSefGmZ_DLobAdsng7xudddpgN1hd7j711ym9WB-iEl6qA4FFZMWPj7hYXCp-U4wSgOxkCafw_-70NJW232kwaQ50UL_ggpYINaM65cMaxKM-AmqFVWQKBYhHYdHYy-NsvykyuYFiYSj07sPkEeoT04SwTtmUOJZEgkO0HTUODtSr4t2OCk2KNIWZsTcacw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز: پس از فرود اضطراری یک هواپیمای باربری آمازون در فرودگاه بین‌المللی میامی و عبور آن از باند فرود، دست‌کم پنج نفر کشته و پنج نفر دیگر زخمی شده‌اند؛ این حادثه واکنش اضطراری گسترده‌ای را به همراه داشته است.
مسئولان میامی، پلیس، آتش‌نشانی و نجات و نمایندگان اداره هوانوردی فدرال (FAA) در حال ارائه به‌روزرسانی‌ها هستند، در حالی که مقامات در حال بررسی این حادثه مرگبار هستند.
اداره هوانوردی فدرال (FAA) در حال بررسی این سقوط است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/146012" target="_blank">📅 01:15 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
