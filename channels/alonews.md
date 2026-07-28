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
<img src="https://cdn4.telesco.pe/file/NN4HfmiDHW0sqdnzSg7OUi4qHOzjbIdiVVC_KKl3ycV5uKohRGQ9O2m4FnlHP_x8PWY6wNz1m2xFs3IiwlRVrazdN256QAxqVpP2VhLgLoBZ9YehYMVfNFp8_EYGjNmrSzO0fXN6e7pQUr4D_GMvoAtrpNQ_jNhKr3T7oBlDA3QHzGqLgoRU9zwH45RKTlopK5AlbRE_trmUvGH-zD39t1eHNTjKGBLhUTH3KyFCjCVm8yIwJNQZ0TAY6P2TLVc7qZ0ZtZvQk1lnMeaGXod6v7XfOIruruDk3REBXePd5iSLyRAzWqXSJLDwB_L0zz3XrEHbn3iK2OQK3TxYG5RIxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 974K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 11:27:23</div>
<hr>

<div class="tg-post" id="msg-138076">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3de200d8a.mp4?token=Uli2phxHrlVNwHFIch-c4wHR8CG2mV8hW0NHeNoaD8KdU0o-f0dLW0gf7ZD7yhBkcF5e54uLXgL8CxtN3Ekld86vpHKhypnUH9SaZ__v1ksSnVFBsp5aDpvPxsh59Rjga26vyFnHzuPx3ttCf7ZWlu4obDY6hke2tgaknb1ROYas8zdM7BVwNjA-By94JTRqSUbYJLOr9x92PFQZ_IelyO0Me4GnrH6kttSXcnjAo6Yartc1Cgyrcn_kLZ1xt6h_9IDogpLnqW13r08SNSEy4KYsK7-arRIJTA7CssA8vwtC9UrowhwwguS7jLc2w1EWx08Y3cgCKQqUY0u9av1bYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3de200d8a.mp4?token=Uli2phxHrlVNwHFIch-c4wHR8CG2mV8hW0NHeNoaD8KdU0o-f0dLW0gf7ZD7yhBkcF5e54uLXgL8CxtN3Ekld86vpHKhypnUH9SaZ__v1ksSnVFBsp5aDpvPxsh59Rjga26vyFnHzuPx3ttCf7ZWlu4obDY6hke2tgaknb1ROYas8zdM7BVwNjA-By94JTRqSUbYJLOr9x92PFQZ_IelyO0Me4GnrH6kttSXcnjAo6Yartc1Cgyrcn_kLZ1xt6h_9IDogpLnqW13r08SNSEy4KYsK7-arRIJTA7CssA8vwtC9UrowhwwguS7jLc2w1EWx08Y3cgCKQqUY0u9av1bYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برشی از یک مناظره/جمهوری اسلامی تنها با زور اسلحه و کشتار باقی مانده
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/138076" target="_blank">📅 11:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138075">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=e8P_qhjY8V2O45doXp3XJ4VkrREogNUN3mwqcBVUCxiQ-ORUHSDxu2vVnpe0Apwqo4WVd727azWcrfpckNjqnAycgqnLz-2AZ5LbVsSHOBFKYb22ALWR3cQuoyFLr4jI7tSBcIs5j-bZ7ADWK8zB5-KKbKjSfT0nGo7AyM0vwTIufQQPupXgg5gOi-vlelU6Mi_MMXNh78CBwrF-1jPEkuAE3bfQwgjuwF3giLufZ456BlCXNtocaK4jnTom6TtnnzXtgL9c-T-y5UMV3MYfwTJ8LYHrvhlZeiaaLNJQAvWY9Fkv_LdzjyI2iLzpYr_NBrTp-d_oBXavkjVpV_w4nztwMmUXvV-o0aiiGDncAM9EImTsI0KapQglUrIDVEpYAGrBmNrma3qD6m_JXAJg_ZAFcVyQQh2vCLI3GUq5DKLOMmPi7kL03ZlH8PJgQ7Tw921_cVR1jJiuRODsGt8eXTDa_FdcUOIDX0--9uTW_Hwh8ujp83VZSKGTQssQGSbhJlzJOjlAFDqbdGfory34Yric5UeeAFoQLyIjhMV_EuVQlmnUAuCqM6Wfjnoof1vhhKYEfDvMxdgzVO4rCL3CUE07FdB4Rqw9hp-8gubv1Na4ptfxYXwtVLcVT-aztGkJOtvLG2C_Br9FSyfkMhmgoNuLwa1ofeUllz5ypQyMHP0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=e8P_qhjY8V2O45doXp3XJ4VkrREogNUN3mwqcBVUCxiQ-ORUHSDxu2vVnpe0Apwqo4WVd727azWcrfpckNjqnAycgqnLz-2AZ5LbVsSHOBFKYb22ALWR3cQuoyFLr4jI7tSBcIs5j-bZ7ADWK8zB5-KKbKjSfT0nGo7AyM0vwTIufQQPupXgg5gOi-vlelU6Mi_MMXNh78CBwrF-1jPEkuAE3bfQwgjuwF3giLufZ456BlCXNtocaK4jnTom6TtnnzXtgL9c-T-y5UMV3MYfwTJ8LYHrvhlZeiaaLNJQAvWY9Fkv_LdzjyI2iLzpYr_NBrTp-d_oBXavkjVpV_w4nztwMmUXvV-o0aiiGDncAM9EImTsI0KapQglUrIDVEpYAGrBmNrma3qD6m_JXAJg_ZAFcVyQQh2vCLI3GUq5DKLOMmPi7kL03ZlH8PJgQ7Tw921_cVR1jJiuRODsGt8eXTDa_FdcUOIDX0--9uTW_Hwh8ujp83VZSKGTQssQGSbhJlzJOjlAFDqbdGfory34Yric5UeeAFoQLyIjhMV_EuVQlmnUAuCqM6Wfjnoof1vhhKYEfDvMxdgzVO4rCL3CUE07FdB4Rqw9hp-8gubv1Na4ptfxYXwtVLcVT-aztGkJOtvLG2C_Br9FSyfkMhmgoNuLwa1ofeUllz5ypQyMHP0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری تسنیم روز دوشنبه با انتشار ویدیویی حاوی اطلاعاتی درباره فروشگاه‌های مورد علاقه ملانیا ترامپ، از کسانی که آن‌ها را «آزادی‌خواهان جهان» نامید، خواست بانوی اول ایالات متحده را هنگام مراجعه به این فروشگاه‌ها به قتل برسانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/138075" target="_blank">📅 11:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138074">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dec70a1e2.mp4?token=vJYFJhOp5FX2suVy0sYOqKJUpE5w_1w70ZYmZE7i7gTVLP9QnVKeiTtcWMcVh6E1BybQbiwJ-Fn0NgPKVI2zy4FqluNoQIi1Gv7BR3KXFNTZEiwtj0B27Oa4RDcZOmzLkwnJvNBr7SqsGdxBTEONqOcf9QzoCCuf28LnSALhQu0coGmXNzwa4C_sXnXWNAWgRM4tRbMWRf6WUnCxnmeNbnShzLxMhYKnHlO0xs6nxoJuCbtAsmvnoKooNA9QCtYWWEB_aP8JUDcgy4eSS0FtQDhO9UzpiGnbvIzmsSvQWaXrUxXIwbq1yFsv1xp1Sbx2V8yi9JaEjR39ij5r9tGoqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dec70a1e2.mp4?token=vJYFJhOp5FX2suVy0sYOqKJUpE5w_1w70ZYmZE7i7gTVLP9QnVKeiTtcWMcVh6E1BybQbiwJ-Fn0NgPKVI2zy4FqluNoQIi1Gv7BR3KXFNTZEiwtj0B27Oa4RDcZOmzLkwnJvNBr7SqsGdxBTEONqOcf9QzoCCuf28LnSALhQu0coGmXNzwa4C_sXnXWNAWgRM4tRbMWRf6WUnCxnmeNbnShzLxMhYKnHlO0xs6nxoJuCbtAsmvnoKooNA9QCtYWWEB_aP8JUDcgy4eSS0FtQDhO9UzpiGnbvIzmsSvQWaXrUxXIwbq1yFsv1xp1Sbx2V8yi9JaEjR39ij5r9tGoqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدون شرح از یک حجری
🔴
پ.ن: راهکار ساده هست زن سیبیلو نگیرید تا با دیدن اشخاص دیگه مشکل براتون پیش نیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/138074" target="_blank">📅 11:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138073">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
توهین‌های داماد دوزاری علیرضا پناهیان به آیت الله سیستانی مرجع اعلم شیعیان جهان!
🔴
پ.ن: آیت الله سیستانی بزرگترین مرجع ۲ دهه اخیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/138073" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138072">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVPJNGT-QuQsCOwUP__oe_EKEF7gMr65DfD0drgf8DyuhpE8INVJHh8aEnej9F-Dr3oc-jIyAl7E6o0JGUIRQKolsj1HldACT7RbpxJ9Y1XMRK0RWllnwtEmOvIUhhWCjb7jUhn3qePQo69moVACElpU2T-xsPfWm6aZzurCbknAd7OA0DIn252SlZKA6FOsWBRDdHK6tHXefpJY6EAdUS_6f9PbLKpTsZ6o2wU5KsUtTAylod3aKYHilN4Olxa2kMSHB-2nLkutRBwMb6KE4KQfXAk2j4kt9UCa5oaS_e_0yxVSUXti4m0ptYX_-1VoRHMZE_lZW3XE1-ypNwjl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل به جنوب لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/138072" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138071">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a635b8a91.mp4?token=YD54F59RHw5o7pI9CECdeqYw82haPyfeu43YynoWrG0PEw1mbI095A0DVcruxl1eSwyL1JUS62vBBx88tujqb93RuZmF_d6KdEwfjwULnxIBGpCB0fxV2kMlDMvuwZCYE0ycUL8AnVB5N3NvNK4bd-6d6xiobGCtzstxYslLDKHnwQvm6f0gExmvaVPTgyV5ZIEPo9Iahn1z43MaiFdxWeX_Ps47qi74NmLVi_DaF1nSVtbMPO5MracAlaTOQfNSFvo9iB1gPJEwgjQP1HXfNVgOU7om0GCyJlZ6mwAnNypcFgSiBML_iR-by1RG6gj3k0R74mor-BFRtzW5QgUs2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a635b8a91.mp4?token=YD54F59RHw5o7pI9CECdeqYw82haPyfeu43YynoWrG0PEw1mbI095A0DVcruxl1eSwyL1JUS62vBBx88tujqb93RuZmF_d6KdEwfjwULnxIBGpCB0fxV2kMlDMvuwZCYE0ycUL8AnVB5N3NvNK4bd-6d6xiobGCtzstxYslLDKHnwQvm6f0gExmvaVPTgyV5ZIEPo9Iahn1z43MaiFdxWeX_Ps47qi74NmLVi_DaF1nSVtbMPO5MracAlaTOQfNSFvo9iB1gPJEwgjQP1HXfNVgOU7om0GCyJlZ6mwAnNypcFgSiBML_iR-by1RG6gj3k0R74mor-BFRtzW5QgUs2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: قیمت بنزین سهمیه‌ای تغییر نمی‌کند/ هیچ تصمیمی برای افزایش قیمت بنزین غیرسهمیه‌ای اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/138071" target="_blank">📅 10:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138070">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PH2BVJysmsbbn1n0-JVRu3EmjesJAgreF1SmyxzBOXVParSwcFjUZdOSl4TkYnEKbYivs4Q10P4zsbss4xQuboLyCAsfSIrM6le34hvvb1t_pt4e6gDWvDprlUEe1qreXTdsKLgPC4O2ZNY9FtyBlTM8lBk13DTkGzwcABRbSVMxV56wdSxv8A7tyhEppw8WpdP09VSR-HH2hsKG7i-b_jL0i5wTh3hA67OqDk9EgZinLr_q8vm5721NtDVmiZqAyVu_4RzPGBbNl2fh013BKv_J4BWrXW5WKyNkaBauOancy0yDmnjK2TQafS0ZNHobyFzaIkm680S6AoXmNmSvTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال یک آتش بس پایدار با ایران تا پایان ماه جولای ( تا یکشنبه هفته بعد) با یک جهش بزرگ در پلی مارکت به ۵۵ درصد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/138070" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138069">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/138069" target="_blank">📅 10:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138068">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
فعال‌سازی سامانه‌های پدافند هوایی در نزدیکی پالایشگاه‌های نفتی بقیق در عربستان سعودی، به دلیل حمله با پهپادها
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/138068" target="_blank">📅 10:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138067">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
حزب‌الله: با حمایت ایران، لبنان رو آزاد می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/138067" target="_blank">📅 10:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138066">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAZ4MWcrdP9_SQFAXYh6b58NArK7hlIqxaNR_9gMX9YTpLqvvDuFfyEqlnZZ42dwLeT1WZQ4r31NCgAPNeKMshCZhWFut_OYzpA49vJX_7_lWmSCI0MtEixnremZ4bpSJhii2GKM0MbNc1UuSffP3NVTCYrj7AfkrtkeaqC9ZGK0snACyl6v_l9O6EK8y0Wk353OfqcA5o1JdVd80LochtXmSsjhx3UXQP8GzzPovXZlodvRgRX__kauKUU8BExypl25GmgdE1PH8KBKTDW3tePFb0l9gEmuqFeYB8w6iXIGESbUTVtc-bB6NOKmXE6oNdo7krHMmT5Ivbbwc7WEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین: شناورهای تندروی ایران در درگیری با آمریکا عملکردی موثر داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/138066" target="_blank">📅 10:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138065">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoXl88anJ2_41iAn0omqETNcsSpZ0l5WKBbOg4k-pdgD8EJyg1WJKlvJE2GPikWJFRK8Rgb4y3Wx8TzOtwWNVBmzOSKIxhja-sIDFPxozjX-rS-H9Wa6DHfmYV1-kIRURx3B7sd2QtS-HklDH-tAHLa-GfA7LDncdxcvxnTurNnh_yrdqERGedkQr6iJDl7gNuFTf-jrjejzDiCiSLuFx52arz6hqU_Tzc5Qt3ue5TtC1FF0aJclnlN0-gyNa9x1jjYs6GNrOkWIz8USijnTE_f9x85psVpFdamEi3PFjQ52HnancfVVeOVrGt1guzRFrT2ZIvHq3RpudvZ9DlY1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش مارک لوین به اعدام و سرکوب مردم در اصفهان:
🔴
با این نازی‌ها مذاکره نکنید. مردم رو مسلح کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/138065" target="_blank">📅 10:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138064">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فرمانداری امیریه : دلیل انفجارهای امروز امیدیه انهدام مهمات عمل نکرده‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138064" target="_blank">📅 10:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138063">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سفیر ایران در روسیه با اشاره به هماهنگی مستمر تهران و مسکو در حوزه‌های امنیتی و دفاعی، از تداوم تماس میان نهادهای مسئول دو کشور درباره حمله اوکراین به یک کشتی تجاری ایرانی در دریای خزر خبر داد و بر ادامه همکاری‌های راهبردی ایران و روسیه تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138063" target="_blank">📅 10:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138062">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وال استریت ژورنال: هدف از مذاکرات ایران و عمان، توافق بر سر مسیری در تنگه هرمز است که کشتی‌ها بتوانند از آن عبور کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/138062" target="_blank">📅 10:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138061">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
همشهری: ۱۵۵ نماینده در نامه‌ای خواستار اجرای قانون برای جلوگیری از رشد بی حجابی شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/138061" target="_blank">📅 10:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138060">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0pbJAorLBafTU-C61JHis27iQAmRVWRrj0EpD1Mh22qJr7Yka5Vh0Wy8JsY39AlO477TRWyt6mOYp6mUEQ_MnbyWmmvPzwiHKZz8h7SdM-tJ4G-iy5oks9TV1KUqQ2ACy0wpjJGBfNlzw-_YpTW3vvi39f5qugy_nZL69zv4Tx_wAeyOxqhB2rQOxMKJ4MDHXw__Ib664HmrL_I80qvII-ohUqQ690sixqWqSUmm6CbTYlj7_3VgRK-zKGG_DlNtZsuSgx00dhh8kVq1L3Wmglz-TGpCKZzviEcvxxaFMZWb--9wpitXhz47KpvTJAzjK_cCy2O4nnLqFyPNZgqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش وال استریت ژورنال: دونالد ترامپ، رئیس جمهور آمریکا به طور فزاینده‌ای در مورد چشم‌انداز اوکراین در جنگ علیه روسیه خوش‌بین شده است در حالی که پیش از این به مدت بیش از یک
سال به مشاوران خود گفته بود که کی‌یف در این جنگ شکست خواهد خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138060" target="_blank">📅 09:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138059">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام ارشد کاخ سفید گزارش داد که دونالد ترامپ امروز میزبان بنیامین نتانیاهو خواهد بود و دو طرف درباره جنگ با ایران گفت‌وگو خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138059" target="_blank">📅 09:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138058">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کیهان: صحبت از «مذاکره» و «حل بحران از طریق گفت‌و‌گو»، اگر خوش‌خیالی نباشد، ساده‌اندیشی محض است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138058" target="_blank">📅 09:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138057">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وال استریت ژورنال: مرگ لیندسی گراهام و مشکلات جدید اسرائیل
🔴
مرگ لیندسی گراهام، اسرائیل را با مشکلی بزرگ‌تری در آمریکا مواجه می‌کند، زیرا واسطه‌ ماهری مانند او، به هموار کردن اختلافات ترامپ و نتانیاهو درباره ایران کمک می‌کرد.
🔴
جایگاه اسرائیل در میان دموکرات‌ها و جمهوری‌خواهان در حال افول است و دیگر کسی مانند لیندسی گراهام با آن وزن سیاسی که دوست نادر اسرائیل باشد، وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138057" target="_blank">📅 09:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138056">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KyFHCPKU6-mib0tN1ooLHY2I2mgtZC2yudN9bBE3KspgjE86V4cvHNNoFbHzNBlOZlMIB_fGevsc1UC28YQx3Urayw-vRVH5VNMFz_pCelgpVo5_JpFZ_7Y8jsj8mMsSYuXBKFMLEGrXmtAURBjPzIafwbZM628LP_YTx0dv-2JeKh7Yuyjo18nxrmHo81ZfQjqVCGBNyJAMujlFnS45c2L9Kvrq5FWSRQnHWBV0og4SyldpZiA8_iZUG47mxNrp4JW3ltjq1GntCgiJs0PkXEtfpGH4cKSaqikfUAg0EyAuJ2a9LNgeu6EszI5rfBv7DoMgtiU97XVbTFUhh25kPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اداره برق به جز اینکه برق رو قطع میکنه؛ یه اپلیکیشنم طراحی کرده که پول میگیره قطعی برق رو بهت اطلاع میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138056" target="_blank">📅 09:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138055">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وال استریت ژورنال: هدف از مذاکرات ایران و عمان، توافق بر سر مسیری در تنگه هرمز است که کشتی‌ها بتوانند از آن عبور کنند
🔴
مسقط پیشنهاد ایجاد یک کنسرسیوم منطقه‌ای برای تنگه را مطرح کرده که بر امنیت دریایی و سایر همکاری‌ها نظارت دارد
🔴
این پیشنهاد شامل تأمین مالی داوطلبانه از سوی کشورهای منطقه و صنایع کشتیرانی و نفت است
🔴
آمریکا به طور مستقیم در این مذاکرات شرکت ندارد، اما عمان این کشور را در جریان می‌گذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138055" target="_blank">📅 09:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138054">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
صادرات قند هم آزاد شد
🔴
سازمان توسعه تجارت در نامه‌ای به گمرک با صادرات قند به‌صورت مشروط موافقت کرد.
🔴
۳ روز پیش نیز وزارت صمت ممنوعیت صادرات ۱۵ قلم کالای کشاورزی از جمله کشمش را لغو کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138054" target="_blank">📅 09:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138053">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ارتش اردن اعلام کرد که یک پهپاد را که وارد فضای کشور شده بود، سرنگون کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138053" target="_blank">📅 09:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138052">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=spKi-jsYejbBzQiF8mK1Y4uyGwJmPCQgBsBNu7VOeojBHJMtyiLPg4yEMXENyyKAHmoVzMbJ3Z8mP0LHkGHMpxkm3xJyLwAlHacl74mIRnJNFl-9GkisW4rjPvZFMcY8Xlb9arQqiJ89JR-ju9MebEXiqrZgQxXTJX6rGIK-NG1HI9sEvJ8hOAAPUPDvY2or9iwIO65RatWl3P0Y_Y6AmqjLMcVmvTKQWDlH-elAFwL3JqnijViBoHdgXeEKFgB6tpyDUlXTEdJR2ldCsuUtijvrk8gj_9SeXdsFgfY-VEdY8x0M0Kf4ZIRcejsc-OhdzypQiFdKhImZWb2n6sUeaRTA-On5hywBuU6IvzX0GWm3mbu6URLnGTvlPybvjhMrWylO2JT_AtHG23olyDaCW7HfGqGJhHtlLNQIQUrLGiwmAx9x34sIv-IMUG8uUnbY6O1jN10x1aVo_9e7oKL7t75ERFzZP-VVNCTeigcSxMLFqQ5XpXwb9ZuvwyFlkvsHfWpPh13O0vgQwaaHXadWCgCZnAt4HcFZaf1OC9ybF93icIApsGwuwMM84zeftJRP4h2RoPcIAyaWuFBUEyCw_Ajz3w6Dsia4eEk8EopaFHefE_p8pW3s7pTkmbMT-8aF4jFm86bojTYgkItH7FbY-4BgE6kg2tmwNtW4la-hwwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=spKi-jsYejbBzQiF8mK1Y4uyGwJmPCQgBsBNu7VOeojBHJMtyiLPg4yEMXENyyKAHmoVzMbJ3Z8mP0LHkGHMpxkm3xJyLwAlHacl74mIRnJNFl-9GkisW4rjPvZFMcY8Xlb9arQqiJ89JR-ju9MebEXiqrZgQxXTJX6rGIK-NG1HI9sEvJ8hOAAPUPDvY2or9iwIO65RatWl3P0Y_Y6AmqjLMcVmvTKQWDlH-elAFwL3JqnijViBoHdgXeEKFgB6tpyDUlXTEdJR2ldCsuUtijvrk8gj_9SeXdsFgfY-VEdY8x0M0Kf4ZIRcejsc-OhdzypQiFdKhImZWb2n6sUeaRTA-On5hywBuU6IvzX0GWm3mbu6URLnGTvlPybvjhMrWylO2JT_AtHG23olyDaCW7HfGqGJhHtlLNQIQUrLGiwmAx9x34sIv-IMUG8uUnbY6O1jN10x1aVo_9e7oKL7t75ERFzZP-VVNCTeigcSxMLFqQ5XpXwb9ZuvwyFlkvsHfWpPh13O0vgQwaaHXadWCgCZnAt4HcFZaf1OC9ybF93icIApsGwuwMM84zeftJRP4h2RoPcIAyaWuFBUEyCw_Ajz3w6Dsia4eEk8EopaFHefE_p8pW3s7pTkmbMT-8aF4jFm86bojTYgkItH7FbY-4BgE6kg2tmwNtW4la-hwwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش تند چند آخوند به حسن روحانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138052" target="_blank">📅 09:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138051">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری /  صداى 6 انفجار در نزدیکی‌ تأسیسات نفت و گاز واقع در منطقه شرقی عربستان سعودى شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138051" target="_blank">📅 08:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138050">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
گزارش ها از برگزاری یک رزمایش نظامی بسیار بزرگ و بدون اطلاع قبلی که به صورت بی سابقه توسط تمام کشور های عرب متحد آمریکا در خاورمیانه و آمریکا در خلیج فارس طی ساعات آینده خبر می‌دهند.
🔴
یک نوتام( منطقه پرواز ممنوع) برای بخش بزرگی از خلیج فارس صادر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138050" target="_blank">📅 08:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138049">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
با اعلام خبرگزاری فارس، حکم اعدام هر ۳ نفر اجرا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138049" target="_blank">📅 08:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138048">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
المانیتور به نقل از منابع آگاه: وضعیت عجیب است؛ ترامپ می‌تواند جنگ با ایران را از سر بگیرد، اما نمی‌خواهد؛ نتانیاهو می‌خواهد، اما نمی‌تواند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/138048" target="_blank">📅 08:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138047">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی و میانجیگران: ایالات متحده با چالش محدودیت موجودی موشک‌های رهگیر پدافند هوایی مواجه است، در حالی که ایران همچنان زرادخانه عظیمی از موشک‌های بالستیک و پهپادها را در اختیار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138047" target="_blank">📅 08:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138046">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
جو شدید امنیتی در میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138046" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138045">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2b428aa9.mp4?token=k9GHbCQLrOzIDePa6FOM1lGWmLvHb05O500sGPadvYzTBcQriMv-1SuGoYEeIBVjaXmkNb0CT7Gyi4Ao7-llHvyCdSIh2e_GwkiQxtdyaxvb7plcYmXTz8jfdjAtV1WPSQk2GYpy4cpyAlikgQtUY8L0a4XgDDiC6O4nSsPytOP3ycUa7DzQAK-MH2f27c9ESqHG4K-As3yiPZwNdnL-jntjUA3rQxi18oFZZ_FSXoVsl86JUyUwf9rR1TybajEmiqJM15-6ZryCfwSTQo7zdNAAUWLe5pTPh2fep86WlWypJ9nLB_Yp1NJuzajrhE1vg7B1VaHSphbaa87hFObXAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2b428aa9.mp4?token=k9GHbCQLrOzIDePa6FOM1lGWmLvHb05O500sGPadvYzTBcQriMv-1SuGoYEeIBVjaXmkNb0CT7Gyi4Ao7-llHvyCdSIh2e_GwkiQxtdyaxvb7plcYmXTz8jfdjAtV1WPSQk2GYpy4cpyAlikgQtUY8L0a4XgDDiC6O4nSsPytOP3ycUa7DzQAK-MH2f27c9ESqHG4K-As3yiPZwNdnL-jntjUA3rQxi18oFZZ_FSXoVsl86JUyUwf9rR1TybajEmiqJM15-6ZryCfwSTQo7zdNAAUWLe5pTPh2fep86WlWypJ9nLB_Yp1NJuzajrhE1vg7B1VaHSphbaa87hFObXAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ورود نتانیاهو در واشنگتن دی‌سی
🔴
نخست‌وزیر اسرائیل امروز با ترامپ دیدار می‌کند تا درباره ایران و اهداف احتمالی «تأسیسات هسته‌ای» گفتگو کند.
🔴
گزارش‌ها حاکی از آن است که نتانیاهو «اطلاعات محرمانه‌ای» درباره تأسیسات هسته‌ای کوه کلنگ ایران آورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/138045" target="_blank">📅 03:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138044">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb91a1151e.mp4?token=JsI8apk9veM2ZfhWvtpE3_zT91BifGKslaDl1w7aDQXuVJ939diCwv9lPqBvJRNvvFjhrZZiuJzQ-MjJVo2Qw2KYwrNx8BwkV3zTNgS0XuNvOuennS47s2VlJ8cS2-DGfBkR88XSAbnTyMZ9Iy1VqSLe-KqdBFwbpXwJXNRcyPbsB66CMSVVwopi_GFpEyR0twz1kI-Dr3H5AGEj-cznoDbTQtBUTHBBv2AJTZOSIZHnWDNPPPAe2Aa6gTZzNmhsmMJoi3e5wDpHZWFJMwEj6cg54F11z2ybnvr5Dz3WPWWceGpspxpWvZxGChIKsxKYcXjVl8GgvzSY5--V9r-Sww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb91a1151e.mp4?token=JsI8apk9veM2ZfhWvtpE3_zT91BifGKslaDl1w7aDQXuVJ939diCwv9lPqBvJRNvvFjhrZZiuJzQ-MjJVo2Qw2KYwrNx8BwkV3zTNgS0XuNvOuennS47s2VlJ8cS2-DGfBkR88XSAbnTyMZ9Iy1VqSLe-KqdBFwbpXwJXNRcyPbsB66CMSVVwopi_GFpEyR0twz1kI-Dr3H5AGEj-cznoDbTQtBUTHBBv2AJTZOSIZHnWDNPPPAe2Aa6gTZzNmhsmMJoi3e5wDpHZWFJMwEj6cg54F11z2ybnvr5Dz3WPWWceGpspxpWvZxGChIKsxKYcXjVl8GgvzSY5--V9r-Sww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گریه خانواده اعدامی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/138044" target="_blank">📅 03:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138043">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOgI9zBzXaS9-1dY-cQiNagLhGQ7nhKUX4Djes6KEsEEshV-TUHKNF9F11qIEms574Shn25gloA3GSMfnvfCS2ohL9phTnrtqKj3OjMqswLKNISh0CKBfAcA2fmqEeFXvE6WVnvXQjd3_sMq1Gxwpvs2RDLnX1CNw8MhIAjYZEsbiQ3_Y65oTAnQkmvqtvUtDSB7AYSoDgB6kXOvsU0N3eRt4T7jJS3s_NXsScB2i3lrXXyx1ygFSZq7IOGj8u2easdGgC4shdMA1iCTdQCxDklrIZ4JC7W8IkRHgX4jfU_6osntT5H924K16K2H4HNGtFXygcAOLnMfGoIxL99PdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس): نباید به بازداشتی‌های اعتراضات عفو داد و باید همشون رو اعدام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/138043" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138042">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96ac69ef8.mp4?token=VReDsNLqvkrir6AWAf562g26Qy91aSoTzDJvBOEIt3lo8BqiaxT4xc2BTnbsnUEm4CAUxMPYBbwKXhiaIjcj_kk8FfnDkXQ9oR5KNdmICrvStCeMsnb0vtwPtlAMtA9I0JmC2VKMYVHSG07apn438ZcGgWMhSBMpLqiqV_ZyOnkJAyi3X-SFOHy5Sp7ybLeIwcHxeRI19dmdZ219IXjB2d4oOJBktcyF9dzIHvWmRTN1DrFnTVZE7A6-ZShzvOpuR31_wFJg1begJzTjlsvMDm5vzliGMxu290XX348SKQEfSZ4X9nV3zMCYciWio_hmNOl5v1RrneZfWTnFmUH6j01Sf83vE0oMOyAXMe8bgqnvMI_XgOuTDjOXpFB9LqERBYCFrAkdRBBHliFVW1Xc6akWNyFUetZ99fZuor8OiAYoOqskcMLDlgFVgt74w4zFpzsxdYSxBX8xIKjCWVYV4QySOtE9ir4BecLSo0h5JuDBvTHb37Ubp0eHSw2zW6BPvmW4a-EktiukzBVQSfhpcDwm6WloPtA3vbdE7uVIUwtiYUb5dsJB2zZSU1YL8ye8JaNi89smJrEt2M8Pb853DnEVijccSEQe4OlQ6Xv2jrffwQG5gdp4JTRcZVs6fMKyXATeFqHQbdqsNOVU9woWVDtgrJgRj14qkiV4jS3IesA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96ac69ef8.mp4?token=VReDsNLqvkrir6AWAf562g26Qy91aSoTzDJvBOEIt3lo8BqiaxT4xc2BTnbsnUEm4CAUxMPYBbwKXhiaIjcj_kk8FfnDkXQ9oR5KNdmICrvStCeMsnb0vtwPtlAMtA9I0JmC2VKMYVHSG07apn438ZcGgWMhSBMpLqiqV_ZyOnkJAyi3X-SFOHy5Sp7ybLeIwcHxeRI19dmdZ219IXjB2d4oOJBktcyF9dzIHvWmRTN1DrFnTVZE7A6-ZShzvOpuR31_wFJg1begJzTjlsvMDm5vzliGMxu290XX348SKQEfSZ4X9nV3zMCYciWio_hmNOl5v1RrneZfWTnFmUH6j01Sf83vE0oMOyAXMe8bgqnvMI_XgOuTDjOXpFB9LqERBYCFrAkdRBBHliFVW1Xc6akWNyFUetZ99fZuor8OiAYoOqskcMLDlgFVgt74w4zFpzsxdYSxBX8xIKjCWVYV4QySOtE9ir4BecLSo0h5JuDBvTHb37Ubp0eHSw2zW6BPvmW4a-EktiukzBVQSfhpcDwm6WloPtA3vbdE7uVIUwtiYUb5dsJB2zZSU1YL8ye8JaNi89smJrEt2M8Pb853DnEVijccSEQe4OlQ6Xv2jrffwQG5gdp4JTRcZVs6fMKyXATeFqHQbdqsNOVU9woWVDtgrJgRj14qkiV4jS3IesA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جو شدید امنیتی در میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/138042" target="_blank">📅 03:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138041">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ به سی بی اس: مایل به توافق هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/138041" target="_blank">📅 03:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138040">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یه سری کانال خبری هم که فاز مردمی برداشتن دیدن ویو خوبه بین خبر اعدام تبلیغ شرطبندی گذاشتن تا پول بیشتر گیرشون بیاد
🔴
یه حقیقت تلخی هست تو این مملکت هیچکس دلش به کسی نمیسوزه و همه منفعت طلب شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/138040" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138039">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIEV_1gKVwIexNskcaImjZjdVou_7QaMhA95zQLH_HT-6vOBCI0czX32rZEAbVI1W2vgqXgQQZsIlHX60mS-_vyAQTSihClaeJP4rnZ07gbmk_RW7H6Umao4jfswKqHfqaDd_ojXTyrGTpgEMPEg7E5dKepnsunoR-q57ybqT-LPupSFxIKw6GB8wk7ultZme0k9Wr59_ZG8eNcyCnfP1prHa7AbdcvUI9DK7QWfu5OaEPvEqtRKD5Fdg70a9cl-0LNV9PeTaKm4kVFtbKka7OEsbJPkbP--x-9OXMb-OoxN13-8DO7DUiwgQsGsOREoDGZdzzWAHbVNNFDeIESfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعدامی‌ها رو آوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/138039" target="_blank">📅 02:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138038">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c5d18645.mp4?token=XiuPptiJqjIZ3uJTm6dC_G2grbI9sTZ47AIJiEXkTOQdXEiSZftffrPBfYltOZuRjvFM3Qc8ZHFbLu-tRX8c6Gg_hmWb-B4icAE-GIvs7feS1oyMXUEJwTYOB0AG57ZmpOkq02E8ErIPRlbI6vUf0E4SjK8TM9a9veMM9De33zKIKsS6nNaRvBV7WyLeRxZOKutrsDHWfAtXk0gwK5vmGkDFvg0AlXSRoFkGQBgdW23byhfxB7n64m9LwqMmk_aXrSh51QQaNGlqGvCkoGrK4KIbiuUsGNfegKbR8kN0beJIIEf7OMM8xhmXa5oE4z8VgEIkBmrpf68ryMAM-XEj9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c5d18645.mp4?token=XiuPptiJqjIZ3uJTm6dC_G2grbI9sTZ47AIJiEXkTOQdXEiSZftffrPBfYltOZuRjvFM3Qc8ZHFbLu-tRX8c6Gg_hmWb-B4icAE-GIvs7feS1oyMXUEJwTYOB0AG57ZmpOkq02E8ErIPRlbI6vUf0E4SjK8TM9a9veMM9De33zKIKsS6nNaRvBV7WyLeRxZOKutrsDHWfAtXk0gwK5vmGkDFvg0AlXSRoFkGQBgdW23byhfxB7n64m9LwqMmk_aXrSh51QQaNGlqGvCkoGrK4KIbiuUsGNfegKbR8kN0beJIIEf7OMM8xhmXa5oE4z8VgEIkBmrpf68ryMAM-XEj9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعدامی‌ها رو آوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/138038" target="_blank">📅 02:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138037">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
طبق گزارش‌ها، دقایقی پیش چند دستگاه آمبولانس و ون انتظامی وارد میدان علیخانی شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/138037" target="_blank">📅 02:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138036">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/710f6ceb7e.mp4?token=Avxjs4n2yyLxU5xKAmBeVGHTl5YRINr_30B70SmCP_X9FJ1IQNeXNF-idR8dTCFh61uC7GK57JTPoo9SFi21Pd46VV-39wSyh214zJ5DNRLNlAqymAdP_PAIBsYwLuD4bJLTTcsbjcbzwJAiODqnGtg4JMv-2KW7Nr3FGFgZ1hJe_g1uVY4t7OdXwJMznlGbGyXZ-icAfBssZLDAgP27Wg6baIzt7Q5jDtcm9M8s2Relbc3AWjaeC7WJJpqBBGXrVyBVmFqUW89pTGRrTGUVLKWU9XN-4IbLEGnjIJwiFjKEQbXNbrW1y499IZQ2JSCXZ8pWIXl7lPPANmnQswPxgot2AxQz9Cq9VYDyQy0Kyc6FC3NEzHtDQ6UgUvQA_PUP5vM3Sf-vcZhQCUo3cNOWip2ggaDZ0fs-fAxHaWC9Dd3KvY6Sa-FcstsdbZIxkJpy6M0cC7Ao_IyWJvCcs814g7T9Carldil-01bN7fdQKIbzCDcA4Nv9msOzlRcJJ0yuMo4kTfZwVsBNRRh-oeSDwDG7SXevr4sgsiqeF2OEYmu5o1wUee8NFc08HJYV_50RCMMElIRLFBoYWLmd3_6bgqHlsN8C4vj99XDQaIDpj_2zRkgUvqqIKK_QumZeG8xJ7oYDbe5Wd784SCSKALYsGKnUiR8U41UeaFPGuUTB1q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/710f6ceb7e.mp4?token=Avxjs4n2yyLxU5xKAmBeVGHTl5YRINr_30B70SmCP_X9FJ1IQNeXNF-idR8dTCFh61uC7GK57JTPoo9SFi21Pd46VV-39wSyh214zJ5DNRLNlAqymAdP_PAIBsYwLuD4bJLTTcsbjcbzwJAiODqnGtg4JMv-2KW7Nr3FGFgZ1hJe_g1uVY4t7OdXwJMznlGbGyXZ-icAfBssZLDAgP27Wg6baIzt7Q5jDtcm9M8s2Relbc3AWjaeC7WJJpqBBGXrVyBVmFqUW89pTGRrTGUVLKWU9XN-4IbLEGnjIJwiFjKEQbXNbrW1y499IZQ2JSCXZ8pWIXl7lPPANmnQswPxgot2AxQz9Cq9VYDyQy0Kyc6FC3NEzHtDQ6UgUvQA_PUP5vM3Sf-vcZhQCUo3cNOWip2ggaDZ0fs-fAxHaWC9Dd3KvY6Sa-FcstsdbZIxkJpy6M0cC7Ao_IyWJvCcs814g7T9Carldil-01bN7fdQKIbzCDcA4Nv9msOzlRcJJ0yuMo4kTfZwVsBNRRh-oeSDwDG7SXevr4sgsiqeF2OEYmu5o1wUee8NFc08HJYV_50RCMMElIRLFBoYWLmd3_6bgqHlsN8C4vj99XDQaIDpj_2zRkgUvqqIKK_QumZeG8xJ7oYDbe5Wd784SCSKALYsGKnUiR8U41UeaFPGuUTB1q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قوه قضاییه:
علت حکم اعدام متهمین میدون علیخانی اصفهان اینه که این افراد در 18 دی ماه تو میدان علیخانی، مامورها رو با طناب به تابلو بسته بودن و بعد از اینکه با سنگ زخمیشون کرده بودن روشون بنزین ریختن و آتیش‌شون زدن و درحالی که مامورا زنده بودن اونا رو روی زمین میکشیدن و با چاقو تیکه تیکه‌شون کردن و فیلمش رو برای رسانه‌های معاند فرستادن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/138036" target="_blank">📅 02:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138035">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIautNwdWHjtVTi4XVLJTpNKLBkO2d9N9MOEdn3M_s8vVjGBITYL5ma_1P_l8xx4g8tKK7DwXDcJQdXrMEvF2m-vg_Cxl-XD2-G2HI1_EoXH1ze4fSh0UCF5yslsxhsVjfdf6xg_w_6nwO93ZlQFkpBo12IyWhQYAoWKD2GD3SPKLf77B9OLcpwEA-EQPNvoU65HbGROzrjhKtoW0kgrEPf-6o-_LVkOeCbEY9owOyd0b_p5KDTnEHVk-crsuVb66Bto2LEDvNpZZMnR5i91Tuz8qPsc5XDxQnKyHCkPZ0dh74NC_Crvew21u2-DGt0avmziztpyflY4DCwx-e4TNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا همزمان با اذان صبح، مهدی ظریف 23 ساله هم بخاطر شرکت در اعتراضات دی ماه، در مشهد قراره اعدام بشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/138035" target="_blank">📅 02:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138034">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ql2ISSGRfkWmL5zsWx1byQkrsSr8dKQWNmN5jvai-Kf3DTHTHmTt9xVnt1XZbT48_s1AUWmHME9AqmhJ87HkSETslNIEeytRZKSFoT2fDlihniI4WxbgrNRQqyHxCivs-fOW5cv6vD95pNgD-oVNPSI0ewj2g3QNTntwcBHTBhqMDGx8mwTxEI_zthn-Hw-vYY6u_7zYzsghuWO0gqx-kKzzBEpbEXInRN2oyD2rYObzJyMC3ihvVmkX2UGUXdPwFMFroxQIh9HmC9c2LZ2UyxPtbsp7Hz4KRw_wRVSro5vxEDD3SSYZLnU2iBROf48SMBqVWY2fCIYcUCxD4YGv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر نصب شده در میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/138034" target="_blank">📅 02:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138033">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=hObqQ-EjI3-ylu7ExeCB2vtNWLsvepEMxTl9s0hnTxBTLJZnFbmKRtNg0NrqfPE9wyG_vgL45QRqthHEUosSVVczppyE_ZlZm4f9EanOrkWzL_Xiv70VoGnEY_SIytghwJy9ZBbdMr49awNVqyunJbHPumkzgzCXi_Z9P15g1tcI7m1TE-e5e9mIre2KysAfw5-9f8x3jac1LoaZcI4Dp-2IVgS-UhH_atXmIKklSJ5E5xt7wdbVGvbt_jYxHasLuyaKjipFFZM2P7Xvk7j-iiSWwWHipJt_GGr9ZZTytuC2zH8WfvtBWo-GTOCe49d_FmU5FMNRz6aGIu_79qEERQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=hObqQ-EjI3-ylu7ExeCB2vtNWLsvepEMxTl9s0hnTxBTLJZnFbmKRtNg0NrqfPE9wyG_vgL45QRqthHEUosSVVczppyE_ZlZm4f9EanOrkWzL_Xiv70VoGnEY_SIytghwJy9ZBbdMr49awNVqyunJbHPumkzgzCXi_Z9P15g1tcI7m1TE-e5e9mIre2KysAfw5-9f8x3jac1LoaZcI4Dp-2IVgS-UhH_atXmIKklSJ5E5xt7wdbVGvbt_jYxHasLuyaKjipFFZM2P7Xvk7j-iiSWwWHipJt_GGr9ZZTytuC2zH8WfvtBWo-GTOCe49d_FmU5FMNRz6aGIu_79qEERQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/138033" target="_blank">📅 02:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138032">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">#نه_به_اعدام</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/138032" target="_blank">📅 02:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138031">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1dfac21ffc.mp4?token=K1uDZ_SraTF9hxGgnCx9elK5F_6DL0WPJaJcB3ab7pLeu0WsAE3UB7c_M5r1-OnikmYwbsKkptPoLcnN8bVTAqeuKNM8isQzQrHr8e4ecf_k3fY2_xRPPpRfDMdDaYecLDfwTBSqMm4aItGB2oHtbr7jxO7jgH0cL3QdsIZdrlvAbeqj79i3qVf9ZrjuNI8IwEUF4_LnL6yFPDwEa_7QvnXAyTDDrfGWRDrtLGexbXHn0t6PMJLm00Q393ZixhBiAIBZpN9Wy4KPWjhCsF4BwJGMSFmDyoeWyxsWDkbwKSddQa8x_4hAbR5inHILYuuKfxEjRYHHHrtrZOc63vp4lw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1dfac21ffc.mp4?token=K1uDZ_SraTF9hxGgnCx9elK5F_6DL0WPJaJcB3ab7pLeu0WsAE3UB7c_M5r1-OnikmYwbsKkptPoLcnN8bVTAqeuKNM8isQzQrHr8e4ecf_k3fY2_xRPPpRfDMdDaYecLDfwTBSqMm4aItGB2oHtbr7jxO7jgH0cL3QdsIZdrlvAbeqj79i3qVf9ZrjuNI8IwEUF4_LnL6yFPDwEa_7QvnXAyTDDrfGWRDrtLGexbXHn0t6PMJLm00Q393ZixhBiAIBZpN9Wy4KPWjhCsF4BwJGMSFmDyoeWyxsWDkbwKSddQa8x_4hAbR5inHILYuuKfxEjRYHHHrtrZOc63vp4lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/138031" target="_blank">📅 02:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138030">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YTkRszIQl170K4bLAU1nmGi-wjZ6RbObrW5oNXCWJ-KesDG06cyICRXLh6s4RrcvmvdjeeYHctR1t9EfDzaS5fmduXS_9t6gnAgQ1eAXNDOVZbt4W_uX7NEQ67zG4565wyxB1HWG9y_NQLGdZB4uto8L3pcS1ht6n6jTuKwRivsSUayRfbGCKALqF4Ng2ISm5DI8Sd9bZH5VCDIicmqJgoqovnSy2FqCrRHDs0DYsMyYuJ8GL4gnLTKnyOVweksmfKxfnt-Sh3imwuzDUlIMQD1oDmPswYIVeQ1gQIR8U4mUg0yp3S6F4q_NLGma3UAV1oxYdnIX8yVYscmryOP-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه نگاه به دستای امیرحسین صفری بندازین!
🔴
این طفلی اصلا معلوله! آخه چطوری میتونه یه مأمور رو کشته باشه! چطوری دلتون میاد اعدامش کنین
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/138030" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138029">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0967f8fa4.mp4?token=hTRyN_wwKEPD4x6uhJieB0kaHS4hZOThSa4A8yIpsm11yqkXmqaccVdM7qo9huzM0FplQl6fRr_xbrQbmSpoqVwPecpcAyt_sT4QKIWYYgZ1wLlYJVjbtiXCH3JufN4e4BqEL3eX3FsuzJQKM-Y6wc0yQnq3myxUTkB7Tz_IkyQqKnhWqu3w_r7c_co2wZqyWzxxwfGIsDB-hMdaQ334ofX-w_1Bt0MkqoxCGT0xlaB6bw-vdGBmL2mvcMRDhYWbqnarMo7JwlcxVdtzbKKTeUVONUeWmpIFvbBvunXl4YOCAOnH0TbzNw7usdX3orHLaplRym2JQGdVAYGUdeYyPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0967f8fa4.mp4?token=hTRyN_wwKEPD4x6uhJieB0kaHS4hZOThSa4A8yIpsm11yqkXmqaccVdM7qo9huzM0FplQl6fRr_xbrQbmSpoqVwPecpcAyt_sT4QKIWYYgZ1wLlYJVjbtiXCH3JufN4e4BqEL3eX3FsuzJQKM-Y6wc0yQnq3myxUTkB7Tz_IkyQqKnhWqu3w_r7c_co2wZqyWzxxwfGIsDB-hMdaQ334ofX-w_1Bt0MkqoxCGT0xlaB6bw-vdGBmL2mvcMRDhYWbqnarMo7JwlcxVdtzbKKTeUVONUeWmpIFvbBvunXl4YOCAOnH0TbzNw7usdX3orHLaplRym2JQGdVAYGUdeYyPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون میدان علیخانی اصفهان که قراره ۳تا جوان رو اعدام‌ کنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/138029" target="_blank">📅 01:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138028">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
هواپیما بی‌بی نتانیاهو دقایقی پیش در واشینگتن به زمین نشست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/138028" target="_blank">📅 01:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138027">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
به صدا درآمدند آژیرهای خطر در کنسولگری آمریکا در استان اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/138027" target="_blank">📅 01:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138026">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501833108d.mp4?token=frp1ck1Qmwmov6l6vEz0IXjDfiZtorYU5lMWAMbt-AJheTXwlAFQl18s8NmWXF2UoLxfNbPFiAiohm4ofuuYFvXObq3TRVY9M4B3dLBNXxgeV8rFjB30hXnRHHOtnyfKvDZBmcBq-EXaos5WTvrp-0jSvuhCizSdO-TLkt9DhGYWny0VgEgXRFvxoC9_gYaW_2eP74oPa15OCBkluUnuBGivUaLWP0O-d9GhPVso0nc5OqUxAlPQAl_3ixCxSmi-39FTegi9qluz7jKDnVgET7mGnPXBZRIjjuQP-CXb9kl3GJda7H7Bn3PWmNHGuIl5qahJDrX4HYcEEvS4nWZiLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501833108d.mp4?token=frp1ck1Qmwmov6l6vEz0IXjDfiZtorYU5lMWAMbt-AJheTXwlAFQl18s8NmWXF2UoLxfNbPFiAiohm4ofuuYFvXObq3TRVY9M4B3dLBNXxgeV8rFjB30hXnRHHOtnyfKvDZBmcBq-EXaos5WTvrp-0jSvuhCizSdO-TLkt9DhGYWny0VgEgXRFvxoC9_gYaW_2eP74oPa15OCBkluUnuBGivUaLWP0O-d9GhPVso0nc5OqUxAlPQAl_3ixCxSmi-39FTegi9qluz7jKDnVgET7mGnPXBZRIjjuQP-CXb9kl3GJda7H7Bn3PWmNHGuIl5qahJDrX4HYcEEvS4nWZiLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش حمله و انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/138026" target="_blank">📅 01:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138025">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=ei-eUB9aS6gjND2F420UlEugahrCPC_5sMLNcj8DsrJICXPgRgKfYqaDsUFGSpP-kWweTs1SxpfY-Tq3MGY8j0DPp5Bxdod3hdYUfOvsR3B0YsXoCH87tVBlTaUsje8sj2YVWrNN8KuWJimk9xvHwwDI6T6F0NfMiSbf3RylA_hDfqiie_53oGueEgxecG9B8R88rT_E3pIk_mRicFoSICzKMZ7aY84IyWRSDICzQp8nWVYmByVwpEbKTzoVt6uSfa6iMEjwxa9rwPdClg8ozWs1uyUpbFVT7fopcUcGvLEUZXYvCXustZH8PUVHNwuKOMz0z6EQ0M4Ss9tA85zqyIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=ei-eUB9aS6gjND2F420UlEugahrCPC_5sMLNcj8DsrJICXPgRgKfYqaDsUFGSpP-kWweTs1SxpfY-Tq3MGY8j0DPp5Bxdod3hdYUfOvsR3B0YsXoCH87tVBlTaUsje8sj2YVWrNN8KuWJimk9xvHwwDI6T6F0NfMiSbf3RylA_hDfqiie_53oGueEgxecG9B8R88rT_E3pIk_mRicFoSICzKMZ7aY84IyWRSDICzQp8nWVYmByVwpEbKTzoVt6uSfa6iMEjwxa9rwPdClg8ozWs1uyUpbFVT7fopcUcGvLEUZXYvCXustZH8PUVHNwuKOMz0z6EQ0M4Ss9tA85zqyIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش‌هایی از سخنرانی ترامپ در میشیگان:
🔴
آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
🔴
همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
ترامپ: ... ونزوئلا.. پس از آنکه تقریباً ظرف ۴۸ دقیقه پیروز شدیم، گفتند: «اوه، حرکت خوبی بود.» خب، همین اتفاق اکنون در ایران در حال رخ‌دادن است.
مردم هنوز متوجه نمی‌شوند. ما نیروی دریایی‌شان را نابود کرده‌ایم. نیروی هوایی‌شان را نابود کرده‌ایم. رهبری‌شان را نابود کرده‌ایم. تسلیحات ضدهوایی‌شان را نابود کرده‌ایم.
پهپادهایشان اکنون با حدود هفت درصد ظرفیت قبلی تولید می‌شوند. بخش عمدهٔ توانایی تولید پهپاد و توانایی تولید موشکشان را نابود کرده‌ایم.
اکنون با ما دربارهٔ دستیابی به یک توافق صحبت می‌کنند؛ اما اگر ما این کار را انجام نداده بودیم، هیچ مذاکره‌ای در کار نبود.
آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
آن‌ها قلدر خاورمیانه و قلدر ما بودند. اوباما ۱٫۷ میلیارد دلار پول نقد سبز به آن‌ها داد. یادتان هست؟ پول‌ها را داخل یک بوئینگ ۷۵۷ گذاشتند و به تهران فرستادند؛ ۱٫۷ میلیارد دلار پول نقد.
او تصور می‌کرد می‌تواند به آن‌ها رشوه بدهد؛ اما آن‌ها در عوض با خودشان گفتند: «این کشور چقدر احمق است.»
نه، نمی‌توانید به آن‌ها رشوه بدهید. باید شکستشان بدهید و ما داریم حسابی شکستشان می‌دهیم. اما خواهیم دید نتیجه چه می‌شود.
اکنون مذاکراتی بسیار دوستانه در جریان است.
نیروی دریایی ما در اجرای محاصره چقدر خوب عمل کرده است؟ حتی یک قایق [نتوانسته عبور کند]. آن‌ها می‌گویند: «دیگر محاصره را نمی‌خواهیم. لطفاً، لطفاً، محاصره نکنید.»
---
ترامپ:
اکنون قیمت تخم‌مرغ بسیار پایین‌تر از زمانی است که کار را آغاز کردیم. خواهید دید پس از آنکه تهدید هسته‌ای ایران را از میان برداریم ــ که بسیار زود اتفاق خواهد افتاد ــ اوضاع چگونه خواهد شد.
اما افزایش قیمت‌ها ربطی به من نداشت.
---
یکی از سخنرانان همراه ترامپ:
۴۷ سال طول کشید تا کسی بایستد و بگوید دیوانه‌ها نباید سلاح هسته‌ای داشته باشند.
همچنین چندین دهه طول کشید تا مشاغل را دوباره به داخل کشور بازگردانیم.
---
ترامپ:
نمی‌توانستیم اجازه دهیم آنچه در ونزوئلا اتفاق می‌افتاد ادامه پیدا کند و اقدامی که انجام شد بسیار قاطع بود.
همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
اما هزینهٔ عملیات ونزوئلا، همان‌طور که گفتند، تاکنون جبران شده است. به همین ترتیب، در برابر جمهوری اسلامی ایران نیز با اختلاف زیادی در حال پیروزی هستیم و تضمین می‌کنیم که آن‌ها هرگز به سلاح هسته‌ای دست پیدا نکنند.
وقتی کسی می‌پرسد: «چرا این کار را انجام می‌دهیم؟» پاسخ این است که نمی‌توانیم اجازه دهیم شما سلاح هسته‌ای داشته باشید. همین تنها چیزی است که لازم است بگوییم.
اگر قدرت سلاح‌های هسته‌ای را درک می‌کردید، دقیقاً متوجه می‌شدید که چه می‌گویم.
---
بار دیگر می‌گویم: ایران هرگز سلاح هسته‌ای نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/138025" target="_blank">📅 01:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138023">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JB07cU6JlHuHJYSjpc-EF88M6tYrFz4dQ9S262DwnF7hVT1IfOhhQdl5fNNek0OtlZ8-7xA1mzgjEBCO0Da5S6SasEtMsrX_xg10HY-CF6aitY9CIBVTIwogRvbHTnhZPvh1zAQ8EAQXvNmKPVuZLB4x1-JX7ZYizdEC1ATxlU1xIZL8xGJK4s3PFrjJ2jPFF3NPYDcfTVXR7tvX_4bh5UX3VQp5kvcNXdRGPAn-dQ3fQfKWgTZXp6IQVlibTJafiTL16CRNLB0qBu1kIY0h85_XpBstWqsC8PC0QEaHhuF6spCcsfUpfhbFojDUeCWkudIMoUN-5Aqx8W5WKFV6LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryopj8XH0Q_uH_uNJih8ze6dU9PMHKhxNKYcSZPEFudWXLaIPly7FKRtq-F_5_ZT53JWEScMAyZaQJcYaDJ1v5xmcWWd11sfb_PyrY2DHrVgg3lqvu328yq9k-xVpaZngrC-VVGXlO9Z2CdXiz5a8NvdvpgcI7R2ZWH9k6w7eDZDN-6q90hLtQhMEiiu-qhtC4dvMuXCChO-XB4baY9lG6-ENiGFjmCRUfgWROYz4ySCgZ6aA0JEpZLMRlwwMm6DKok0P6CJe-aSe_fXPUGR0laauV_D0dwJlvpStS0YdvcYMZQucRIKKfECjWy6Iw0bTVvx82SEO81f5jQVfJhUjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یه پسر ۱۱ ساله داشته بازی می‌کرده که از ارتفاع ۱۰ متری سقوط میکنه و از شانس بدش، میله آهنی مستقیم فرو میره توی باسنش!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/138023" target="_blank">📅 01:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138022">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9b8525811.mp4?token=X4AwBkuUmklD77AgU8G_PAbUw27B4BWrqV4veNwxOD4Qi0idpx74-UpSDpwOUzlZbRRzgiQI3o-R8ttTy5LEx8HUFVSELg-HIC1Tn0lM53FSgSKbvh4_nLjgrF0iOr6CjGnrVoAhGhdAdllkEJ2_BehCYh1TbPZ4QuUDclnsj4K7cI3OB74RoItcESH7nBzcTIkaYP0OgUWi7SJrvkdnZYjQWtfOX4EFS39vLnzWMZzDiectI_lM2FUV5C8cTgAIy6vTPhv3NGLjkkPrYlcxVzK0ndiZ6wcW7ZB26Nb7h-a3FG07I20C__LwESStuBbjbTfHKvGbIpXs9pHA5NWfKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9b8525811.mp4?token=X4AwBkuUmklD77AgU8G_PAbUw27B4BWrqV4veNwxOD4Qi0idpx74-UpSDpwOUzlZbRRzgiQI3o-R8ttTy5LEx8HUFVSELg-HIC1Tn0lM53FSgSKbvh4_nLjgrF0iOr6CjGnrVoAhGhdAdllkEJ2_BehCYh1TbPZ4QuUDclnsj4K7cI3OB74RoItcESH7nBzcTIkaYP0OgUWi7SJrvkdnZYjQWtfOX4EFS39vLnzWMZzDiectI_lM2FUV5C8cTgAIy6vTPhv3NGLjkkPrYlcxVzK0ndiZ6wcW7ZB26Nb7h-a3FG07I20C__LwESStuBbjbTfHKvGbIpXs9pHA5NWfKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مصاحبه زنده یاد کیانوش سنجری با شبکه (آیت الله) بی بی سی که حرفاش به مذاق این شبکه خوش نیومد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/138022" target="_blank">📅 01:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138021">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
گزارش‌های تائید نشده از حمله به کنسولگری آمریکا در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/138021" target="_blank">📅 01:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138020">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4fa9f23e.mp4?token=JehaEih1SgamyYKArM1bmDHDtcTaCbEx7XFa5Hv5kzEdvNxb5-ASGgToRdG_6VDRgQm0XD9OiD3OWN0IdQ9pBRg74dEAasN2GJaWeS6PFZI3lYAMXUFpMwXJtwPt4Sv2AGbUhiRYwFCvxVAOfenYsxdMCxbY5VI9KAtYo2wy3J97eCvrOEbZBk5zl1Y5LG391W2-bItqNgBrKlZGwU7A9LqPYDrP_KJOuKcllYVM8TjW7ZGNrSIbJrenaTC549ZuyBCycsXx9Zc23qk1uasjdlnfqFYw4tSPHtDORy-0osS23POjqc5T3P-0Mm9aFB-M6YeoCjn6O-lhZBYROxs6-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4fa9f23e.mp4?token=JehaEih1SgamyYKArM1bmDHDtcTaCbEx7XFa5Hv5kzEdvNxb5-ASGgToRdG_6VDRgQm0XD9OiD3OWN0IdQ9pBRg74dEAasN2GJaWeS6PFZI3lYAMXUFpMwXJtwPt4Sv2AGbUhiRYwFCvxVAOfenYsxdMCxbY5VI9KAtYo2wy3J97eCvrOEbZBk5zl1Y5LG391W2-bItqNgBrKlZGwU7A9LqPYDrP_KJOuKcllYVM8TjW7ZGNrSIbJrenaTC549ZuyBCycsXx9Zc23qk1uasjdlnfqFYw4tSPHtDORy-0osS23POjqc5T3P-0Mm9aFB-M6YeoCjn6O-lhZBYROxs6-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حکم جلب این بلاگر طرفدار حکومت بخاطر نوع انبه خوردنش صادر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/138020" target="_blank">📅 00:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138019">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رئیس صداوسیما : اعتماد مردم به صداوسیما از اعتماد مردم به دولت بیشتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/138019" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138018">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سپاه: نسبت به دوران جنگ خیلی قوی شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/138018" target="_blank">📅 00:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138017">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تو میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده  طبق آخرین اخبار ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری به انفرادی منتقل شدن و قراره تو ملاعام اعدام بشن #نه_به_اعدام #زیرساخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/138017" target="_blank">📅 00:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138016">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2x1xyzeXT03QRxjwUQM3zivH0uYzpdn-0mU0s5Xkg7Oh4RKTmGk5iq5kTD6IpFvM_OhdsZuMOVVcbSev23GCOkmdMeSmN36_-3ieXxc7IqbF2tWrp67vyGCDmiVCq2zVPUoVYT8KYVoiSdKFl7ps-0xtd4wvNjgUH-nMpKcANg4QIW4B-0EviV_rAMo9aHqmOnFn5lkvfNDFEza-AwHT0baVqxhmLgaktC6XkQa1-V1CwCsLb04i9kw-P68IJtgek8p5dP_7-bcX1zs4NKJ0CxK4zkcHbUlsSWBpPmGQ-JBqy_8Y99w_-14vvwnocXptGyeLZ1n7mjkMVkwc8mmZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده
طبق آخرین اخبار ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری به انفرادی منتقل شدن و قراره تو ملاعام اعدام بشن
#نه_به_اعدام
#زیرساخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/138016" target="_blank">📅 00:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1lgmQ3nM8vXvn9QXJQDUTEmRhwvuEy66qaSs3IqPvt6d9qDbkfJDH43DbSYEkIEo-g7ZK11X4WkI4Y_RS4ew_c7FUHg2fGB_FXjy-GIR7R7qJx3-xn0QH7a3hJV_pbR_NahC5c_uRs4671W4c1YemKD-rAJeA4aPezOArrA_5FNDC1Dd02OU9RwEqJO-DspRwZ7LCkrSNZZdFiIJOvHrpQ-loyTeGv59M8d8CRFPtjDqPrwF-PC2do3TgP65lqcyOrx3q-mHqPqw2fdQDVD_v1e4FdFFcN1MHjYFy-3GdyJZR5oEqXc9m6pVtZciBNBKb6p2-CogfQFh915dT7_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caSUO2AIhwcl2w2dOz9MuAMeIVzndFDjEvB3Cg1qLgOwrgFpC7B4fkgBXcwqSumzLYx6TblnFHeGLa6yw8mZfaF1jmFcmnztHoTbiyyEWfNO-AQuKa7YX1plCFlGjI8s3hxlikd_aFYV5K4x_b1g6lYPiBT3RMUVOz1-HyyITlfAhsNCSSEZPLgWU4Dp6b2skhuxExxxsDMQQKs_3yimL_l1dg6xTMj1FP5pG410GC54QcXmzPzr6Uh2pPu5-xTmcJ4xgM63FCr7hYadKsIrHkUFlLBb1SNnBLOrxlZiIZsF9AEBGh55usd3ougEo-T6vSRbBgjQ8b-4uH-ghWF5HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امباپه با بازیگر معروف، کوماتوزه رل زد
@AloSport</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/138014" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
این وسط از دقایقی قبل یه گروه هکری عکس ترامپ تو جزیره اپستین همراه دخترها رو منتشر کرد
◀️
مشاهده فوری
به شدت داره ویرال میشه
🔖</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/138013" target="_blank">📅 00:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138011">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ سه‌شنبه میزبان زلنسکی و نتانیاهو در کاخ سفید؛ ایران و اوکراین محور گفت وگوها
‏
🔴
یک رسانه آمریکایی اعلام کرد: دونالد ترامپ رئیس‌جمهور آمریکا روز سه‌شنبه در کاخ سفید میزبان زلنسکی رئیس‌جمهوری اوکراین و بنیامین نتانیاهو نخست‌وزیر اسرائیل می‌ شود و ایران و جنگ اوکراین و روسیه محور گفت وگوها خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/138011" target="_blank">📅 23:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138010">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6dd15287.mp4?token=j2ziSii4-estWz7DZNbVw0lqPmYbVnYitIAaqt6LcOXfrUhz5aj1yLvXp6lqMj0h8fGZqSGwbtDqkUJ95S6ETTvcoVdaIXaJYJAC2OA9_tvIQxlptU2QWxyxKb63QKxa7CuSOG75EQff6h_D3jy2v6FBHpgBdHCEUB9EYVtcTZeeqk3BoaqnmB_uO2FTg-FToZEWaW2HTlG6RAJXoqBU2t0w-ZS8xKATRTghUkyLOUNy2JwYSbL9Lq5mKsxMjVGuv28pAfUgUlTmrgYpIoBdbcGpnNozaZ1qG7cffqurWIYB2_0FaPvhIEbw_hbuCdaR0zZpJZVZSrI69vgVpgIgMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6dd15287.mp4?token=j2ziSii4-estWz7DZNbVw0lqPmYbVnYitIAaqt6LcOXfrUhz5aj1yLvXp6lqMj0h8fGZqSGwbtDqkUJ95S6ETTvcoVdaIXaJYJAC2OA9_tvIQxlptU2QWxyxKb63QKxa7CuSOG75EQff6h_D3jy2v6FBHpgBdHCEUB9EYVtcTZeeqk3BoaqnmB_uO2FTg-FToZEWaW2HTlG6RAJXoqBU2t0w-ZS8xKATRTghUkyLOUNy2JwYSbL9Lq5mKsxMjVGuv28pAfUgUlTmrgYpIoBdbcGpnNozaZ1qG7cffqurWIYB2_0FaPvhIEbw_hbuCdaR0zZpJZVZSrI69vgVpgIgMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما به پاکسازی کشورمان از مجرمان خطرناک، قاچاقچیان مواد مخدر، قاچاقچیان انسان و افرادی که از کودکان سوء استفاده می‌کنند، ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/138010" target="_blank">📅 23:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138009">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73846f9e59.mp4?token=Cr8Jj58F_K08IfnCLbPcbuUfXOEs26DwqVZBIWfmGtfps89sISF6u3PTY9iLzU4YJ1Dk7La0kKic_XVOoAFZqsPVRoEHS9TXlii_HTCURefPE3pnhuReq23MPqD5s2Gz20dGTtcWDxiKpBoqfk92SWjoF6riXBWYDyX75FehFK5kTCBLC7P3_0BLqEuyR6gp2ev6w3yQ5C_h7go5hK-0_zuV55zBu3xaswoufapWVAOZcEQFiOnT2X4NqWDRQp6ZT1Qwi8UkAD9_J7gm6pK9GhRm6fZYKTF6z1_BQT2r36BIiKU4I0x7bS7BcmDBttdO7fuUbKWBosniLF1ZWZnuUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73846f9e59.mp4?token=Cr8Jj58F_K08IfnCLbPcbuUfXOEs26DwqVZBIWfmGtfps89sISF6u3PTY9iLzU4YJ1Dk7La0kKic_XVOoAFZqsPVRoEHS9TXlii_HTCURefPE3pnhuReq23MPqD5s2Gz20dGTtcWDxiKpBoqfk92SWjoF6riXBWYDyX75FehFK5kTCBLC7P3_0BLqEuyR6gp2ev6w3yQ5C_h7go5hK-0_zuV55zBu3xaswoufapWVAOZcEQFiOnT2X4NqWDRQp6ZT1Qwi8UkAD9_J7gm6pK9GhRm6fZYKTF6z1_BQT2r36BIiKU4I0x7bS7BcmDBttdO7fuUbKWBosniLF1ZWZnuUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در روابط با جمهوری اسلامی ایران به موفقیت‌های بزرگی دست یافته‌ایم و ما اطمینان حاصل می‌کنیم که آن‌ها هرگز سلاح هسته‌ای نخواهند داشت.
🔴
وقتی کسی می‌پرسد: «چرا ما این کار را انجام می‌دهیم؟»، به سادگی بگویید: «چون ما نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای داشته باشند.»
🔴
این موضوع بسیار ساده است. این تمام چیزی است که باید بگویید. نیازی به گفتن چیز دیگری نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/138009" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138008">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترکیه فروش سامانه S-400 به مصر را بررسی می‌کند.
🔴
بر اساس گزارش Defence Arabic، آنکارا در حال بررسی فروش سامانه‌های S-400 به مصر است؛ اقدامی که می‌تواند یکی از موانع اصلی بازگشت ترکیه به برنامه جنگنده F-35 را برطرف کند.
🔴
گفته می‌شود این موضوع در جریان سفر اخیر وزیر دفاع مصر به ترکیه مطرح شده است.
🔴
مصر هم‌اکنون سامانه S-300VM روسی را در اختیار دارد و در صورت نهایی شدن این معامله، توان پدافند هوایی خود را بیش از پیش تقویت خواهد کرد.
🔴
به گزارش منابع، ترکیه این معامله را بخشی از یک بسته گسترده‌تر همکاری‌های نظامی و فنی با مصر می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/138008" target="_blank">📅 23:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138007">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21566da8a.mp4?token=cQDXBKenuBsswheWIlBr2rNP7uoxZcnazFCSJoHshS-5njNPdWA8dtVNLF1zAnrCfcaJ_wmzNg9TZhIeHocPkRnqRfZ0atvw8HFlZDutgsEGcEfJKnB6PDwikNJtbZJxToGHCHRWoYNrWftauw2sGI7bgqbAmAePXI4Wb7upGo5HI6SZt5AmHOuuDkK1JA9BhakBl450qwNQdeW4zOiBdIuMNL9DFhDhvpKLLeIyG1myR8nhTDM-0hocOlZkCki1q4iQuGEBTYYi34e5EJdBmPTRC-oVfjua9Mt3zjtjc5dPRB4oVWdF4z7YhKxWwye4Fn2J9p8tnChtTYzKzadKew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21566da8a.mp4?token=cQDXBKenuBsswheWIlBr2rNP7uoxZcnazFCSJoHshS-5njNPdWA8dtVNLF1zAnrCfcaJ_wmzNg9TZhIeHocPkRnqRfZ0atvw8HFlZDutgsEGcEfJKnB6PDwikNJtbZJxToGHCHRWoYNrWftauw2sGI7bgqbAmAePXI4Wb7upGo5HI6SZt5AmHOuuDkK1JA9BhakBl450qwNQdeW4zOiBdIuMNL9DFhDhvpKLLeIyG1myR8nhTDM-0hocOlZkCki1q4iQuGEBTYYi34e5EJdBmPTRC-oVfjua9Mt3zjtjc5dPRB4oVWdF4z7YhKxWwye4Fn2J9p8tnChtTYzKzadKew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
در ١٨ دی مردم رشت شهر رو بصورت کامل در کنترل خودشون داشتن بدون اینکه خون از دماغ کسی بیاد.
🔴
ولی در ١٩ دی حرام زاده های حکومتی با آتیش کشیدن بازار باستانی رشت برای به قتل رسوندن مردمی که به اونجا پناه برده بودن و به گلوله بستن مردمی که سلاحی نداشتن، جنایتی راه انداختن که هیچوقت از ذهن این مردم شاد فراموش نمیشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/138007" target="_blank">📅 23:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138006">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نایب رئیس مجلس: همه راه‌ها را با آمریکا رفتیم و جواب نگرفتیم
🔴
آن‌ها فقط زور می‌فهمد، پس چاره‌ای جز ایستادگی عالمانه و هوشمندانه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/138006" target="_blank">📅 23:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138005">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0413f576f8.mp4?token=P-Nt0-YqbOxfjKjCNDTdTIbtvCBXco6m8YwrMgffMa9-8qNEtni-PgDT-aqRwkgu3YLG8koBx5fG3P9kawJKIuyt21-4NWiaDxIAQXHJfhuyjm5-5uCtDwqIXnoeL0YaI_mO_lBLgyoBrdQoHmM0bd1eaHhJF5jdrRFkqWmKNBeVkWQZJh0TeWByOVU8d3hmJCAzU0ka6dmAKnSHdZO42ueZxbitV9zv-0vt1Tgim3rZDAzCqEcpVQ9EPNXPWdKsrMVRD3xjJ8Rh76r-1dz5fEh2fTPckthBCv9JGvOlbwuZx_EXHDPXMRqMVeJSag1jnh3Gd1ZHcuLMOhxly1hflw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0413f576f8.mp4?token=P-Nt0-YqbOxfjKjCNDTdTIbtvCBXco6m8YwrMgffMa9-8qNEtni-PgDT-aqRwkgu3YLG8koBx5fG3P9kawJKIuyt21-4NWiaDxIAQXHJfhuyjm5-5uCtDwqIXnoeL0YaI_mO_lBLgyoBrdQoHmM0bd1eaHhJF5jdrRFkqWmKNBeVkWQZJh0TeWByOVU8d3hmJCAzU0ka6dmAKnSHdZO42ueZxbitV9zv-0vt1Tgim3rZDAzCqEcpVQ9EPNXPWdKsrMVRD3xjJ8Rh76r-1dz5fEh2fTPckthBCv9JGvOlbwuZx_EXHDPXMRqMVeJSag1jnh3Gd1ZHcuLMOhxly1hflw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ گفت: خیلی از جمهوری‌خواهان آدم‌های خوبی هستند. ما حزب بسیار مهربانی هستیم. اما اگر بخواهم صادق باشم،
🔴
شاید نباید این‌قدر مهربان باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/138005" target="_blank">📅 23:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138004">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ : اون حوضِ زیبای کنار کاخ سفید... یکی اومد با چاقو خرابش کرد. مریضن
🔴
الان داره تعمیر می‌شه و خیلی زود دوباره درست می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/138004" target="_blank">📅 23:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190b4a0822.mp4?token=r6VIkZ3ttQd1HRVScb0h_1vltgQ4A-tddOvK2Dxw4mphmfZD0BIX35Yx_RVbom9_Z5vXcVJByhqtLrL7PNvT4sBwOR__GqnqCPM1XI5hpI5eL0Fj79TrfHqdsFtrjJSG-Khl8XoJ6x3CeSdquOk-A_IIgLGzY8ElgMKmPxwoXc9MkHfUlD4iVPW_JSfls6BSZJ_6_Lyh6DAUBG9Z07l1jZt1D1nvrJgOrqkJWBLmq3X9aixTOGtr0YS1Jazmw236Z8g5W8GxzDPdM6r2W3X2XDtkO3dOt0sBCfmw1qKp6f_T8PgDZCsG7w0Pu4ge1FAcz7lhWgQZHfssZNSPaM-t8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190b4a0822.mp4?token=r6VIkZ3ttQd1HRVScb0h_1vltgQ4A-tddOvK2Dxw4mphmfZD0BIX35Yx_RVbom9_Z5vXcVJByhqtLrL7PNvT4sBwOR__GqnqCPM1XI5hpI5eL0Fj79TrfHqdsFtrjJSG-Khl8XoJ6x3CeSdquOk-A_IIgLGzY8ElgMKmPxwoXc9MkHfUlD4iVPW_JSfls6BSZJ_6_Lyh6DAUBG9Z07l1jZt1D1nvrJgOrqkJWBLmq3X9aixTOGtr0YS1Jazmw236Z8g5W8GxzDPdM6r2W3X2XDtkO3dOt0sBCfmw1qKp6f_T8PgDZCsG7w0Pu4ge1FAcz7lhWgQZHfssZNSPaM-t8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به طور موقت، تنش‌ها کاهش یافت. اما آن‌ها رفتار مناسبی نداشتند و مجبور شدم دوباره وارد عمل شوم.
🔴
اکنون آن‌ها دوباره رفتار مناسبی دارند. این شبیه به نواختن یک ساز بانجو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/138003" target="_blank">📅 23:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ : یه کم ناراحتم چون شاید تا دو سال و نیم دیگه رئیس‌جمهور دیگه‌ای داشته باشید. شاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/138002" target="_blank">📅 23:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/006cb45ccc.mp4?token=AdCfUHPQkuTC77gcro0HGAoGZ6sypcYF0Nogs_PjsLqxESxkhhIhD9iEgnuhkFdOKAqYchNknbybDi0kxwz8l6wVwFOmq0amdH3u_qL96EJ4n-FXbppndkIUCKZyl9XPASh_AwpL1MjnQJWMZ3cysbp_CKf6cUmbN0CgG_bklBqLB2J3hNxdZ3V2FtrKZ6-a3xCBWRBU7CYlOq_FIWlcmvtaMKqVYPqvqxaIoBqxTDIgSW-t8p8Yq1NKSsLat4pYYQx1WPE9JZIjDTDie2PR5AgXZMoIP7W_cSWjbk_byWQCtiur9ujYQu8LcPk-FzN3vsO5BVnHljz02VOIpRHj7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/006cb45ccc.mp4?token=AdCfUHPQkuTC77gcro0HGAoGZ6sypcYF0Nogs_PjsLqxESxkhhIhD9iEgnuhkFdOKAqYchNknbybDi0kxwz8l6wVwFOmq0amdH3u_qL96EJ4n-FXbppndkIUCKZyl9XPASh_AwpL1MjnQJWMZ3cysbp_CKf6cUmbN0CgG_bklBqLB2J3hNxdZ3V2FtrKZ6-a3xCBWRBU7CYlOq_FIWlcmvtaMKqVYPqvqxaIoBqxTDIgSW-t8p8Yq1NKSsLat4pYYQx1WPE9JZIjDTDie2PR5AgXZMoIP7W_cSWjbk_byWQCtiur9ujYQu8LcPk-FzN3vsO5BVnHljz02VOIpRHj7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران گفت:
نمی‌توان آن‌ها را با پول یا امتیاز خرید. باید آن‌ها را شکست داد.
🔴
و ما داریم حسابی آن‌ها را در هم می‌کوبیم. باید ببینیم در نهایت چه پیش می‌آید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138001" target="_blank">📅 23:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ : الان مذاکرات سازنده‌ای در جریانه. ایران می‌گه : لطفاً، لطفاً محاصره‌مون نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/138000" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be3db46cf.mp4?token=q96XCCewOVyvD-yXovWl-VRAs4tSwgvCKxAUTN8jnAgAWl8ORyUksClkIeL1mWNugW5jf9LvI3Lq1V3SpjTtBAmFUTlCYUXuC28LuYC_7IkSFJ6vaRlN75j4XbpIZcUZ-YVLniaEUFz5qQ9qqAHl6wxTwObNo3kL_AE732i0JhV7VEIj1C3d6_wnispb9qX2seXvVHsugIonDbtD5937fbMfrO1dx9zVHgPsp8rLiLzMBEy8DNXyoTdJgJ0RLMSwQUjWBqkAWyeBsKk-BXBE92_PGGyTuiKk9zvKvFrHM_WIo57KWm1HHRR-2cvNLqj3swMlYltflE3EHmxxM5BpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be3db46cf.mp4?token=q96XCCewOVyvD-yXovWl-VRAs4tSwgvCKxAUTN8jnAgAWl8ORyUksClkIeL1mWNugW5jf9LvI3Lq1V3SpjTtBAmFUTlCYUXuC28LuYC_7IkSFJ6vaRlN75j4XbpIZcUZ-YVLniaEUFz5qQ9qqAHl6wxTwObNo3kL_AE732i0JhV7VEIj1C3d6_wnispb9qX2seXvVHsugIonDbtD5937fbMfrO1dx9zVHgPsp8rLiLzMBEy8DNXyoTdJgJ0RLMSwQUjWBqkAWyeBsKk-BXBE92_PGGyTuiKk9zvKvFrHM_WIo57KWm1HHRR-2cvNLqj3swMlYltflE3EHmxxM5BpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: مدتی بود که اوضاع کمی آرام شده بود. اما آن‌ها دوباره رفتار مناسبی از خود نشان ندادند، و من مجبور شدم دوباره وارد عمل شوم.
🔴
اکنون، به نظر می‌رسد آن‌ها دوباره رفتار مناسبی از خود نشان می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/137999" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d9a0a947.mp4?token=uGnQ6kC5FSIYd3pB-tKTGxCltolyyp44sXzGE4sa2bhZPqwy7NfgaKBHRXy_mLT1ilSiNfhKJ88kOOtQnNtf4SX1BbD4CzV38vLXsI7QvZfFqnoocT81PVf29GcPsZa7dezBnLFnUTgomgWH-9MoB1dky97rkpi64yvlVq0rB2ci0aoyfMmKhbENqLb4DCvB_oM6xNATOkssZqD9CUSm1LfEF9jFmn7Q0ps1KPUvMm8v6PN_9yBcWUUImSlZwChynM2xfeKrsntwo96L0TTMM92_I0xzJFPkRU4gNXJ4MAQQ622cVtiAwy2K5zGCxe3Dmze-RAr3ox8IlQVgR57atg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d9a0a947.mp4?token=uGnQ6kC5FSIYd3pB-tKTGxCltolyyp44sXzGE4sa2bhZPqwy7NfgaKBHRXy_mLT1ilSiNfhKJ88kOOtQnNtf4SX1BbD4CzV38vLXsI7QvZfFqnoocT81PVf29GcPsZa7dezBnLFnUTgomgWH-9MoB1dky97rkpi64yvlVq0rB2ci0aoyfMmKhbENqLb4DCvB_oM6xNATOkssZqD9CUSm1LfEF9jFmn7Q0ps1KPUvMm8v6PN_9yBcWUUImSlZwChynM2xfeKrsntwo96L0TTMM92_I0xzJFPkRU4gNXJ4MAQQ622cVtiAwy2K5zGCxe3Dmze-RAr3ox8IlQVgR57atg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس جمهور آمریکا:
با وجود علاقه‌ام به رونالد ریگان، او اجازه داد صنعت خودروسازی آمریکا به ژاپن و کشورهای دیگر منتقل شود.
🔴
من در زمینه تجارت، از ریگان بسیار بهتر عمل می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/137998" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ : همون اتفاقی که توی ونزوئلا افتاد، داره توی ایران هم می‌افته  فقط مردم متوجهش نمی‌شن
🔴
اینا رو نمی‌شه با پول و امتیاز خرید
باید شکستشون داد، و الان هم داریم حسابی شکستشون می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137997" target="_blank">📅 23:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bed1c3e10.mp4?token=AyBUV8eEFBkNRknPxt15LVoBbGg2ab8n3NfEPWhXRc1Gs8OYS-jnfuvCJLz7iIqSYd7CIWChTGVGCZ3HB3A5Pfkx1TaKnRU9Ie6gbYqUKi9e45zUEMXj81G9cowGg3yQwsDLc_XAN6nilTwx4B3Uv6v7znKHfmlMFRf06NCEBvhcc1XMc827Om0CH4WHK6eKsOQTjXmB-2e8h8Pfo42i5AERghKAUIC57Xe8DwDbdMVynI6qfUsos7DEnOFrnQq5XRmf7pTSVhwX7K06B8vplGeERYCGarF8kPTBQSR2_ZceJ5ywlWBMu4jJegUY3RRNovYoA_DJgoS9vbnjmmCVsoOvVCeuQ_vmwnwkdZvZctOV6pK5VWnrPMMyUvvf87IpvTv-q1OayQ22noSalZnX8o1I73PN53MdNMnpa6lyP71Y2p4Tturea1Hi9IiIXZL2x3AyfLaPnIT5dtIXAsRJo0rXDZNYZWSItsPFT1orPBdnG1ZxTtJ_5KTPlH-XeITRghAeGsCe2ORdEO3aDSCrgniR0hIdyCFkpmEz6Tq0ErLzEWV7VAdYxRsn_URq6fyoFyZIkCxb-N1YY8cWnvfBx-bX-qduEGbSbcpeJM-2ISEiBSW4jmB6pZAcYVtFkvn1Pr96v_9TY_ecYe_dO2wlQcyFVaHMjc9il9HItmoISfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bed1c3e10.mp4?token=AyBUV8eEFBkNRknPxt15LVoBbGg2ab8n3NfEPWhXRc1Gs8OYS-jnfuvCJLz7iIqSYd7CIWChTGVGCZ3HB3A5Pfkx1TaKnRU9Ie6gbYqUKi9e45zUEMXj81G9cowGg3yQwsDLc_XAN6nilTwx4B3Uv6v7znKHfmlMFRf06NCEBvhcc1XMc827Om0CH4WHK6eKsOQTjXmB-2e8h8Pfo42i5AERghKAUIC57Xe8DwDbdMVynI6qfUsos7DEnOFrnQq5XRmf7pTSVhwX7K06B8vplGeERYCGarF8kPTBQSR2_ZceJ5ywlWBMu4jJegUY3RRNovYoA_DJgoS9vbnjmmCVsoOvVCeuQ_vmwnwkdZvZctOV6pK5VWnrPMMyUvvf87IpvTv-q1OayQ22noSalZnX8o1I73PN53MdNMnpa6lyP71Y2p4Tturea1Hi9IiIXZL2x3AyfLaPnIT5dtIXAsRJo0rXDZNYZWSItsPFT1orPBdnG1ZxTtJ_5KTPlH-XeITRghAeGsCe2ORdEO3aDSCrgniR0hIdyCFkpmEz6Tq0ErLzEWV7VAdYxRsn_URq6fyoFyZIkCxb-N1YY8cWnvfBx-bX-qduEGbSbcpeJM-2ISEiBSW4jmB6pZAcYVtFkvn1Pr96v_9TY_ecYe_dO2wlQcyFVaHMjc9il9HItmoISfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
مه‌هی‌او!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137996" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0eae498d1.mp4?token=JoMI777w2TIuUulEWqlFs2n6meI8jihl1uNYU0GdHUXsXOD8tiAUUztNX1kLZowBRQnH0F4VbSzLveLiO7Y8OIob18QaA9AFyX8j_GBEHnPQe46EMMNpKZ0fboN4QU0CJdbVS64TSjhshsmhUWQynv_wfAJaurxBPGn3bFDqeTQLtLjJTc_TZd9dIxa-jmkkDpn63UFtWjPwhfTeBQmFwIx-4vv-dznFA8FIG6T4zu83h-FThNoRStQ-p0R1-8Vk04xTvaRm3Rylz9eERmvaXz-dFDAWMMOU3ZWXVtGjkqlE8xNaeh5OFxA3WOLL65b16dM4qFPQIwpk7sIiVPB1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0eae498d1.mp4?token=JoMI777w2TIuUulEWqlFs2n6meI8jihl1uNYU0GdHUXsXOD8tiAUUztNX1kLZowBRQnH0F4VbSzLveLiO7Y8OIob18QaA9AFyX8j_GBEHnPQe46EMMNpKZ0fboN4QU0CJdbVS64TSjhshsmhUWQynv_wfAJaurxBPGn3bFDqeTQLtLjJTc_TZd9dIxa-jmkkDpn63UFtWjPwhfTeBQmFwIx-4vv-dznFA8FIG6T4zu83h-FThNoRStQ-p0R1-8Vk04xTvaRm3Rylz9eERmvaXz-dFDAWMMOU3ZWXVtGjkqlE8xNaeh5OFxA3WOLL65b16dM4qFPQIwpk7sIiVPB1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:دولت دیوانهٔ بایدن کمونیستی بود.
خودِ بایدن نه. آن‌ها به جو گفتند:
"جو، بیا کمونیست شو."
او هم گفت:
"اصلاً کمونیست یعنی چه؟"
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/137995" target="_blank">📅 23:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ خطاب به یکی از معترضان در میشیگان گفت
:
او یک کمونیست است. ما در حال رقابت با کمونیست‌ها هستیم.
ما با اختلاف زیادی پیروز خواهیم شد.
می‌بینید آن‌ها چه می‌خواهند بکنند؟
آن‌ها می‌خواهند خانه‌هایتان را بگیرند.
آن‌ها می‌خواهند پولتان را بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/137994" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137993">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8546f48c6c.mp4?token=jCx9CR15TYhBTe35mYgbYBJKwd3gLJcyUvZ6al3r4pGZTvbez1ZSSSjOiB01MyXfLzX4nYoSFL3t8ra5Aa6vaEULVI7su9QS7RvvSqr4tq8XUDNgvo9wyvlA78Ge7Xc0Zrx8yOoH2-YjcScjHpQ1Q3bymkvyw-nd82cnFAZmrQFYV9jCDctWVFOBxMCzVzEi1TEtbiyIyn0oeHJm7VFwwGCbRpqtmgxpsYJ-xadj2y06oIPY5ZTO0_PeoVhxhCfeGv2A0u05OX4EFRSS72UubtcL3lPayBR1beCVmpNkeBzJ-TXMUYhg9sfAhHsJBZcnffERwJjwrtMwU9lKGYq9HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8546f48c6c.mp4?token=jCx9CR15TYhBTe35mYgbYBJKwd3gLJcyUvZ6al3r4pGZTvbez1ZSSSjOiB01MyXfLzX4nYoSFL3t8ra5Aa6vaEULVI7su9QS7RvvSqr4tq8XUDNgvo9wyvlA78Ge7Xc0Zrx8yOoH2-YjcScjHpQ1Q3bymkvyw-nd82cnFAZmrQFYV9jCDctWVFOBxMCzVzEi1TEtbiyIyn0oeHJm7VFwwGCbRpqtmgxpsYJ-xadj2y06oIPY5ZTO0_PeoVhxhCfeGv2A0u05OX4EFRSS72UubtcL3lPayBR1beCVmpNkeBzJ-TXMUYhg9sfAhHsJBZcnffERwJjwrtMwU9lKGYq9HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ گفت:
من بیشتر از پدر و مادرتان برای شما کار کرده‌ام.
من بهتر از پدر و مادرتان با شما رفتار کرده‌ام.
و خودِ آن‌ها هم با من موافق خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137993" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137992">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c3ad23df.mp4?token=oE9HHHoMUojc8C_qIaSKxhxi0jpbCUFqAdtwjRXiIQsy8-jDbVOHY8qxfP5bWMNPf00TtRTsiyjO5CTKUR5lRhUSNLdiiWA2hMby7SIKLVC7O-KGc09RROKqduwKiaarv1jX_KTRHVRggCTif-0UWUuNfimAzDAPobMKsYCY3IJparWi_qDIn_4yryWeXrfJgKIrvREAxRHwRhPHbwMt37IFFZ344w9aJ67j8zB8QhfF6ucSuUnFWCtZ_qH5jCTWlqoce6GwZpSM8zfMekfCdumi_EohQPGEhMkrmzhQ90-wpX8SGLUbDtDH7xtykrCtV8Fa6N8mIPycvCuu2pIy_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c3ad23df.mp4?token=oE9HHHoMUojc8C_qIaSKxhxi0jpbCUFqAdtwjRXiIQsy8-jDbVOHY8qxfP5bWMNPf00TtRTsiyjO5CTKUR5lRhUSNLdiiWA2hMby7SIKLVC7O-KGc09RROKqduwKiaarv1jX_KTRHVRggCTif-0UWUuNfimAzDAPobMKsYCY3IJparWi_qDIn_4yryWeXrfJgKIrvREAxRHwRhPHbwMt37IFFZ344w9aJ67j8zB8QhfF6ucSuUnFWCtZ_qH5jCTWlqoce6GwZpSM8zfMekfCdumi_EohQPGEhMkrmzhQ90-wpX8SGLUbDtDH7xtykrCtV8Fa6N8mIPycvCuu2pIy_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ
:
من رونالد ریگان را دوست داشتم، اما او اجازه داد صنعت خودروسازی ما به ژاپن و کشورهای دیگر منتقل شود.
ما ریگان را دوست داریم، اما در زمینه تجارت، ترامپ خیلی بهتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/137992" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/137991" target="_blank">📅 22:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137990">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/137990" target="_blank">📅 22:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137989">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
🔴
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/137989" target="_blank">📅 22:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137988">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d2424e0d.mp4?token=MVf0gUC131muOdezlWJjeQHheTD5aXaq_qx0S6a-8q7Yk54pnwNAPFloz4PMjZLIK9XLfrJA6wyNDHjn_zPfCZKyJyuHdCnggm-Oj3btqeJrmDWnRApwgRytgRMdAZcCqmST-Io-aPWtOYfulIMNgPBiG8lsfe78-Yhel5ggu3HevwHnQbZ-V57p5EoH7Xs5U5PRz9o22AtSGoZKsHfD7lUxFY5hIchlKhyD3mlu--kLLxPm8HKahQDU6YceYqDoqKuX9yRqNRjwvSJp0eb5VXG_ZZIdEYvA8GQSAUk1JfJo09TdTnavLxlsyWNL6k_hne2eCdqSISnZ-abDk6pCYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d2424e0d.mp4?token=MVf0gUC131muOdezlWJjeQHheTD5aXaq_qx0S6a-8q7Yk54pnwNAPFloz4PMjZLIK9XLfrJA6wyNDHjn_zPfCZKyJyuHdCnggm-Oj3btqeJrmDWnRApwgRytgRMdAZcCqmST-Io-aPWtOYfulIMNgPBiG8lsfe78-Yhel5ggu3HevwHnQbZ-V57p5EoH7Xs5U5PRz9o22AtSGoZKsHfD7lUxFY5hIchlKhyD3mlu--kLLxPm8HKahQDU6YceYqDoqKuX9yRqNRjwvSJp0eb5VXG_ZZIdEYvA8GQSAUk1JfJo09TdTnavLxlsyWNL6k_hne2eCdqSISnZ-abDk6pCYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری عبری زبان
: ارتش اسرائیل با احتمال بالا ارزیابی می‌کند که پهپادهایی که صبح امروز در نزدیکی بحر المیت و هفته گذشته در کوه هرمون سرنگون شدند، توسط گروه‌های شیعه در عراق شلیک شده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137988" target="_blank">📅 22:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHh3tBYvWCi3p5zq9c75mwn8r6h5G16IMpHwQSWJLalfrkX4qrphYOwiFE73rSIk-6B0oX2otnPW3JiUhKeLBXfPLypBNIkqPmgTby1jsG4HNfyV9u2H0QbygERr9CLVLqzw0JKbVDRwTWAnE4NZMpj7Hloxnmv_5a72y9kdFZ3uKis5sPH3Sxjr1HMpisoDse7pgT_3vo_guNzhogrjFfl-C_8RoOhmuetrq7XWt1s7jIlnSdmVu5kUSZIjsAZ5R3a5OFquA9oplivMxw4jbVkMJVHeISqnDBrT8LSDwO3wCKpMQz3ywtxmqbj7fp26ZnJMsrPXSdLntcx-E1MIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی:
مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137987" target="_blank">📅 22:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137986">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAZZXs2sN3UoIAadw4HjtJCPyZgzLjjfxM7bY9uk2b61YM62UhHI-Jm2B1lYLwNMT-6FS1UQUQ6-60JPijtWpoeGpKKXEdaKM_5rO02XASJupUa49QC10_2UJqeFP_3y1Rq9dSgBBuvMdiy7R3-4M7r9Jo9LcBKgjR_a3Fi1uVEX862YrjpWGgf1IwCS-_nmxlzjECuSLltyKDic4wSflSPfOJR1AyIu_i7RAiu77MR5kPSATXK4TAUpLtgFOn8XaWrBkplsSx3FwUinYOKwCUEN5tpu6vtbZll2jQFtUUgRa9cFpDrJuMIYhnIJKXdwfEsX7uisSwJXSBd0lIsZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام آمریکایی به الحدث:
مذاکرات با ایران جدی است و ممکن است امروز شاهد پیشرفتی باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/137986" target="_blank">📅 22:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137985">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مقامات آمریکایی: مذاکرات ترامپ و نتانیاهو به موضوع ایران و توافقنامه ابراهیم اختصاص دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/137985" target="_blank">📅 22:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137984">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کانال ۱۲ عبری: نتانیاهو در دیدار با ترامپ اطلاعات حساسی را در رابطه با ایران به او ارائه خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/137984" target="_blank">📅 21:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ3klAa5DcdSHWKLQpJFj4uII7rK8gMp8ADanJYhHNJiEW_kok3FaY_j2HVHhAEM3cgoh7iRv8wc1D80A6UpM3pFluQAVn7UCdIqshWrxOqj2sZZ3q-KJVN1vEqmBiCg7A_ZTn9LpGpzpZu8_FL1OHQirCAuVdFcczG_5lJdh5E5H8D-xBU1P4eaKTzpr0V2LfcKDl9w8sjtJPIkci3v2w4mLlBuPna18PfZNhDplWiG48z6I0i2EulSBXl1DpAqMAKj_qUti9AU3HeSL2znLf3cN1iLQwLwIlMStQgP1yQuJ9c3oXA2hjTEmnLpaC7eH3RbN_IIneEzX2dXrdKhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی پیش نفت به قیمت ۸۸ دلار کاهش پیدا کرد
🔴
۱۲ درصد کاهش قیمت در ۲۴ ساعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/137983" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رویترز ،مقام آمریکایی : ترامپ با نتانیاهو درباره ایران و توافق‌های ابراهیم صبحت میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/137982" target="_blank">📅 21:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مکرون: اسرائیل فورا باید از تمام مناطق لبنان عقب نشینی کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/137981" target="_blank">📅 21:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur54JfPpeIuSNQ2x9_eqjuRLfpxsn9GOKYSbo9k-HAMEhKPdrkdZdU8xvn4nNmf0yZA9Qx54OOUJ9-ErTvnzGZy4TR9JMj6QGXsmCPqA8z3qxXjmcIvEaArZLE8KraROyc2CwjboN7noxYCfsKSLERHAPUXtPH63DXrKzyRI7aSilp3Sb4n-Wtw2PrYiLjC46QQNNrHfFGpToAqZyNdi-E618_-4WfOrVAF7e4SphtBz-sQDqd-ISfMaxrq-W7ktpSSzh8WGr6hApCRaqylWAPaGvJU16UcD_rCv7uyKthcLe-7-wvZxIFK_F4qHCVLoPjForU_yjKFNluPcZA8BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام آمریکایی به الحدث: مذاکرات با ایران جدی است و ممکن است امروز شاهد پیشرفتی باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/137980" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137979">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
دفتر نخست وزیر عراق: الزیدی دستور تحقیقات امنیتی در مورد آنچه در بیانیه عربستان سعودی در مورد هدف قرار دادن آن با پهپاد از خاک عراق آمده است را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/137979" target="_blank">📅 21:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137978">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
شبکه i24 اسرائیل : نتانیاهو در دیدار با ترامپ با فشارهای قابل توجهی در مورد چندین موضوع از جمله سوریه، غزه و لبنان روبرو خواهد شد. این دیدار بسیار مهم است و ما امیدواریم که راه را برای عملیات مشترک اسرائیل و آمریکا علیه ایران هموار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/137978" target="_blank">📅 21:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137977">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
استقرار نیروی هوایی آمریکا در قطر و عربستان دوباره تغییر کرد!
🔴
در پایگاه العدید قطر، تمامی هواپیماهای سوخت‌رسان و ترابری بار دیگر از پایگاه خارج شده‌اند.
🔴
در پایگاه پرنس سلطان عربستان، هواپیماها به آرایش زمان جنگ بازگشته‌اند و سه فروند هواپیمای آواکس E-3 نیز دوباره در این پایگاه مستقر شده‌اند.
🔴
به نظر می‌رسد ایالات متحده در حال جابجا کردن هواپیماهای بزرگ و راهبردی خود از پایگاه‌های آسیب‌پذیرتر نسبت به حملات ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/137977" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137976">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd0b82ccc7.mp4?token=tq9cZPINL8iWYS1LoQmaKylPYlb0tNp_1OVrUvbjxTv0mkyc6P6b2mh7frEXXXV2SGo3TSF9uxB3wULelnn4KLfhlFl_Dq_yumtFnOGpPBkWAvHxnJ4flHbK0Vb4gWqGYpeKgCpQAf6yIlj8smiJTVwdK1Q6EpqbSSvDBe5qIR4wVXZSPn5yHrO1B0j0cVWrHJ-7z0KNQ4Hsx7jASyp5ptyKWdyzV-gPUog27SOziJe9TCulUxyGeScnhOAWZ7oX6fMxxnP6U-DzZjPVgW6clhoOXW4VPnahWY7BZsTmd3PUZw3QOqMCVGC88yWHIAd2KUD3SvQb8YH1qy37rCOkwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd0b82ccc7.mp4?token=tq9cZPINL8iWYS1LoQmaKylPYlb0tNp_1OVrUvbjxTv0mkyc6P6b2mh7frEXXXV2SGo3TSF9uxB3wULelnn4KLfhlFl_Dq_yumtFnOGpPBkWAvHxnJ4flHbK0Vb4gWqGYpeKgCpQAf6yIlj8smiJTVwdK1Q6EpqbSSvDBe5qIR4wVXZSPn5yHrO1B0j0cVWrHJ-7z0KNQ4Hsx7jASyp5ptyKWdyzV-gPUog27SOziJe9TCulUxyGeScnhOAWZ7oX6fMxxnP6U-DzZjPVgW6clhoOXW4VPnahWY7BZsTmd3PUZw3QOqMCVGC88yWHIAd2KUD3SvQb8YH1qy37rCOkwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کشتی ایرانی که مورد حمله اوکراین قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/137976" target="_blank">📅 21:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137975">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بلومبرگ: ایران و عمان درباره راه حلی برای مسئله تنگه هرمز گفتگو می‌کنند. یکی از پیشنهاداتی که مطرح شده، باز کردن مسیر میانی تنگه، در آب‌های بین‌المللی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/137975" target="_blank">📅 21:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137974">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afba5829f9.mp4?token=eYI-tEnp3P9PPjUnXFfVLuL03HNN6tEyzlpKCjyXUXHw8x1b70V3SVGjV95bVA0vDhlAFnSTepgxewwsnAfgzkgb0xuhXcZwngrcV95u1BEAbU0pZvjdyM0-lQOU7-Y2v3hbxEoE_jQXC5pMtC-QWmJZytAgXi3ccof6hnLdLKetKYeXi24ji6hHA0kioFpKk65vo7AcXOIZMBQgY-a6UJBiFk07fywkNF7FNs5-2E0TkTrZhT9WeNFnKM8vyp1CMNI6-ovpEH0WdXTk_HfwiwpbXJVB3Nl68Ks_yz_KCF9zd0urQsQvGoUsyoztH8Bzdg_S64YYiKzxWmhkjt6q6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afba5829f9.mp4?token=eYI-tEnp3P9PPjUnXFfVLuL03HNN6tEyzlpKCjyXUXHw8x1b70V3SVGjV95bVA0vDhlAFnSTepgxewwsnAfgzkgb0xuhXcZwngrcV95u1BEAbU0pZvjdyM0-lQOU7-Y2v3hbxEoE_jQXC5pMtC-QWmJZytAgXi3ccof6hnLdLKetKYeXi24ji6hHA0kioFpKk65vo7AcXOIZMBQgY-a6UJBiFk07fywkNF7FNs5-2E0TkTrZhT9WeNFnKM8vyp1CMNI6-ovpEH0WdXTk_HfwiwpbXJVB3Nl68Ks_yz_KCF9zd0urQsQvGoUsyoztH8Bzdg_S64YYiKzxWmhkjt6q6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: روسیه تجهیزات نظامی زیادی به ونزوئلا داد.
🔴
ونزوئلا تقریباً تمام تجهیزاتش روسی بود.
🔴
ولی تهش چی‌شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/137974" target="_blank">📅 20:55 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
