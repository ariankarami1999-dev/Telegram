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
<img src="https://cdn5.telesco.pe/file/ZW7l5BbdOaRH2QaHB2PDZQKTk7RmrJ9NYhtmm-3fC-xQItcinGT9ReVJ2OgEOXRyH44yccQMG1clTkUhSqe1qNNNIwpR6EZRTWHuT1Ry0a8XMnKsFmGr0CYg0v_yUAd1d3JDl9zM9WAaG-dMmiAPy5EJupkrr_UFmVvGumBlDv0va1Q0fOmgHxQ_LRJOWk1ZCKh5UZ9vVRCv58rJwNyWtCIBQZ85WbF_xO0HgGZgBuJ7kdEZeLZxrvfY0KAG0Pe-c7NNXUynGrwf6HHBVeHsCvSlhplCoV5bgJLBWWW0MzO4bw5SpnFZE1TUYLkyV4sFxqXvg_vxE9HuNwHAShKj6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 396K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 23:34:57</div>
<hr>

<div class="tg-post" id="msg-107521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=ehoXbl2yrVn2y4DpcjSNF0RU2lL_vbIEqVr-JKsQciy9a7asLzyi_Ui0uNdRIPgIaM-W9YIUbJFnaVLFcGBeuCbvEYKj6CstjbfQWtq6TfAPzXhMif37hSZ1qaT0b8jHkrAi4K7WWelk_RcEZJhRWm4JwSU31yWqH1JDLSX_dxDZDgwmBZxmpZ-8y7QwE9KCyHh-58n3iaJi2VcDAi4hgyeK-KkLtEsVRwUahJ1UPSXdz0qnHA2RVTHKsp5zM0ANwsyzbm_t9KaPCsqHVCXe4tqAa0vVrb6pGTlqaBuDtWrHk_7l6bpaczfgpvFe37DY-MTvRHsxRPmPXMGeFjtwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=ehoXbl2yrVn2y4DpcjSNF0RU2lL_vbIEqVr-JKsQciy9a7asLzyi_Ui0uNdRIPgIaM-W9YIUbJFnaVLFcGBeuCbvEYKj6CstjbfQWtq6TfAPzXhMif37hSZ1qaT0b8jHkrAi4K7WWelk_RcEZJhRWm4JwSU31yWqH1JDLSX_dxDZDgwmBZxmpZ-8y7QwE9KCyHh-58n3iaJi2VcDAi4hgyeK-KkLtEsVRwUahJ1UPSXdz0qnHA2RVTHKsp5zM0ANwsyzbm_t9KaPCsqHVCXe4tqAa0vVrb6pGTlqaBuDtWrHk_7l6bpaczfgpvFe37DY-MTvRHsxRPmPXMGeFjtwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
قلعه‌نویی بعد از باخت به روسیه: از برخی بازیکنان در اردوهای بعدی استفاده نمی‌کنیم
ای کاش از خودت هم در اردوهای بعدی استفاده نمی‌شد، آقای قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/Futball180TV/107521" target="_blank">📅 23:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
‼️
⚽️
امیر قلعه‌نویی: دو بازی اخیر ایران بسیار مفید بود و توانستیم پلن‌های تاکتیکی خود را به نحو احسن اجرا کنیم. انشالله در جام ملت‌ها دل مردم عزیز ایران را شاد خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/107520" target="_blank">📅 23:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=jbPN44yLoRgf2fOGbgxC1S4qVny4Zp54__Xj_BeNDYwWL176ZXxuzmBJNyChzai2w7tC6vwVCMxHCTFeaO3uxMOUFueiiAb9QnoR4zWUYT8J9ru5RcfPeH6bOfZ18v4oB7sp2tJZ1P31abQ-1mJUra2knZBaCdGFjQnU2CYRPtlGyaR-wg7GyxnvWktuT0FTIILle77rNxEju-Wnt8zulyfuec9Ol_8h5u70xIY31yMchoH9M1C4jR7eCFds7s9XhQKaHCEqvlBMa_Jxm-Hf6zax4fZGeDHn2mNDBijcpqtkK9bWDodIWOVkwenGR7lrt3TegVTnfsheK_JQvBYzsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=jbPN44yLoRgf2fOGbgxC1S4qVny4Zp54__Xj_BeNDYwWL176ZXxuzmBJNyChzai2w7tC6vwVCMxHCTFeaO3uxMOUFueiiAb9QnoR4zWUYT8J9ru5RcfPeH6bOfZ18v4oB7sp2tJZ1P31abQ-1mJUra2knZBaCdGFjQnU2CYRPtlGyaR-wg7GyxnvWktuT0FTIILle77rNxEju-Wnt8zulyfuec9Ol_8h5u70xIY31yMchoH9M1C4jR7eCFds7s9XhQKaHCEqvlBMa_Jxm-Hf6zax4fZGeDHn2mNDBijcpqtkK9bWDodIWOVkwenGR7lrt3TegVTnfsheK_JQvBYzsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
پاس‌گل لامین‌یامال روی گل دوم اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/Futball180TV/107519" target="_blank">📅 22:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=uQmUCRGDSeCu6RizbRvgPpPLHvFecKOhpXzj2oLhFDI4M5of0VIIrCswGY6bkLARDYqCiQxVAVr8qwgSH-35uqifxS_4mkCLhzgFkLN_M5NrnDcJX5Ve6uUaPWw0ZEXCOCbQxbb2vd8ZyJMMEMDgpCarrdlm_ItpZa2oeEff3y1XL0gSEHe7LOGA_blJzDwkPdngdJBwQ3OlMKLwBeTMGMEkQgkV3HFO24DMkq9ntrJ79QQ-5EzlEmVFDBamNEKM4NZ8mN3qr0qCkkRhcbkV44zv-ajnzdpghpKFeR05PDnMJQqEGlOFUxVxaah1Lg87z_VEBlza2IN2iF9LhtWPkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=uQmUCRGDSeCu6RizbRvgPpPLHvFecKOhpXzj2oLhFDI4M5of0VIIrCswGY6bkLARDYqCiQxVAVr8qwgSH-35uqifxS_4mkCLhzgFkLN_M5NrnDcJX5Ve6uUaPWw0ZEXCOCbQxbb2vd8ZyJMMEMDgpCarrdlm_ItpZa2oeEff3y1XL0gSEHe7LOGA_blJzDwkPdngdJBwQ3OlMKLwBeTMGMEkQgkV3HFO24DMkq9ntrJ79QQ-5EzlEmVFDBamNEKM4NZ8mN3qr0qCkkRhcbkV44zv-ajnzdpghpKFeR05PDnMJQqEGlOFUxVxaah1Lg87z_VEBlza2IN2iF9LhtWPkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/107518" target="_blank">📅 22:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گلگگلگلگلگ یامال بازم گل زد برا اسپانیا</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/107517" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f859d863.mp4?token=CoALdKgcljXOsdr_ygRjqx6e8aT4ecPxBiNwxEe8FzMme_IB6HyHNLezC4VpmV1BRCyEXi4pGEfppWdasnQncFHI1KAeyUh_u9ppL3OnqCGWciHnGIt8tZAyucpB0q8XROIyxQTssS9udC4XXcW-RqOKYK2drbPOePK-2kcM5bRsotJl7bLpoZpTa_XI3FKGYSqrNq-Y5J9lcwZstLBS-EMlZ9p3Qx0br5OG_ZBiRsrhEv--uGKyG9lYyeExfm1s0S5x1hl4m-iu1pHfXL1a9yZOMKb3n41vn75eIITBWttyJrhUxJY5YEKZiT3lBx3jbMqafp7T5-FxWI-Ch-LQRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f859d863.mp4?token=CoALdKgcljXOsdr_ygRjqx6e8aT4ecPxBiNwxEe8FzMme_IB6HyHNLezC4VpmV1BRCyEXi4pGEfppWdasnQncFHI1KAeyUh_u9ppL3OnqCGWciHnGIt8tZAyucpB0q8XROIyxQTssS9udC4XXcW-RqOKYK2drbPOePK-2kcM5bRsotJl7bLpoZpTa_XI3FKGYSqrNq-Y5J9lcwZstLBS-EMlZ9p3Qx0br5OG_ZBiRsrhEv--uGKyG9lYyeExfm1s0S5x1hl4m-iu1pHfXL1a9yZOMKb3n41vn75eIITBWttyJrhUxJY5YEKZiT3lBx3jbMqafp7T5-FxWI-Ch-LQRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دیس ابوطالب به فان 360 فردوسی‌پور: فان واقعی اینجاست و هیچ شعبه‌دیگری نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107516" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107515">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNWD6nthcZNVvEPlUGLfwhjxEoZo9fqgz-RogqTZWrYrhjvubRIjHCgBSfGYoGOqDMVA0uaIsTVFX8QzarojRj_jesrZq6EWP8h7ZjS8Mu6rSF1hYA2PeYb66jlb_luuiXAfs2W82Qwpw2ocR99rAkIo_rcNFrT_7w2t66511-evJHnz85pr0uWYnJ3cG3A2HACW9eJk-cpBvy6_xEy8foUqaIvOmXbdFeOARVk-hte_f7OA-IkYjiINxwAvLJnkkuEP3j2LnVBhlgUebE_7zm1nDtASPAXk5TU5OLntDNZ6AGIAMxRApWmSACqIr01lYHGqhjQb1zTaxyDUsSiDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان بازی؛ روسیه 2 - 0 تیم امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107515" target="_blank">📅 21:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
پنالتی برای روسیه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107514" target="_blank">📅 21:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107513">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdBRPu5F6J0YFuJMCfdP_9bsDAO3JXGJmDopTzvl3_5aAz8cUims4Sa-IbCzczVpYYVD1RZX4tw0yHkNBelQeWPSEOrkF_A2-K2-ewyhnLbVdU5llHULTwY_6RdrKx0F2MFH1NPCiK9CPRWv5VUkZ_E8qRQu1Ehp8aJ0y14CwS_EqvgmmNLiZS-GNibel_WVH-94Re7E7h2yAUcCcM0xTZo_iAxthYMwuBzWfoFg4vA8hv6kpPetHVWufIC4lflzGbcYAUfjlwA1c9-P0R1mcF3sa8nN6-_fk0iL_gGBIm6ek0ELNrYgbKOm89XMiQ01uBFRbheDZwN109DHSg-5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
وضعیت پات چطوره؟ ران پای راستت خوبه؟ همه‌چیز مرتبه؟
🚨
🚨
رافینیا: «خوبه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107513" target="_blank">📅 21:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=CK1wKXAV7RNB44e_oUOjAdphf03hBnAnKoFL09blr280a9_93bn8x8CpFgKqyoafarCXcdc_RhtZfijKsV6ZrzQoffyqBdqbjlevtbYhSWHD66x5LiESlaybFoGCbQcMxFMZnmOG7YutjaXAIfWW9OJouwqZsd2cLtcomC9cV5cFfou-R9DeHIar4fPnI8_4SMlFYIAfocKP1z2R2IttzBh6PLTJarxLfbtyFcd45M-66ZdddS-BLOdx24TQspC-UIfo347DjrhFlhvqqJgVi7IwGE6KP4xqt43St48a6t6SkGiJu-NjznQ-WN_wvwTT0biecirIx8VTA-kw4WvnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=CK1wKXAV7RNB44e_oUOjAdphf03hBnAnKoFL09blr280a9_93bn8x8CpFgKqyoafarCXcdc_RhtZfijKsV6ZrzQoffyqBdqbjlevtbYhSWHD66x5LiESlaybFoGCbQcMxFMZnmOG7YutjaXAIfWW9OJouwqZsd2cLtcomC9cV5cFfou-R9DeHIar4fPnI8_4SMlFYIAfocKP1z2R2IttzBh6PLTJarxLfbtyFcd45M-66ZdddS-BLOdx24TQspC-UIfo347DjrhFlhvqqJgVi7IwGE6KP4xqt43St48a6t6SkGiJu-NjznQ-WN_wvwTT0biecirIx8VTA-kw4WvnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
‼️
چهره درهم قلعه نویی روی نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107512" target="_blank">📅 20:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC4gSXO3KL6LX9ihATvedbCGY9PpKyJCEWdzWtT8qCkFLybAJ8ipvKh_kFbyx-0ApfWYxlqv_jMpljcerCPEzxk8O0F-KD6G1Vo9dAEgxT4nth0aMvvDPOKUeoC_iB73dfAAIN2fqETJoPZDr__mZHbuceCCtLxjC6Pm7G2I8lxY4dMFpNQHkTzP2iPngv39ovGzdGxwoUzln_LXw1Dh0Iprhli0U7HJR5_pYfva2rm6RZ1G7uR-hoIIH15DzdGJphgd6UWZg8OUdpLqhDCkTFr7RZCy09kaqJSPqef96Wye9djzqNgSAT1y0WCH6qSLHsobDvHo9MzxFXrynOXwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
اعلام ترکیب تیم‌ملی اسپانیا مقابل کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107511" target="_blank">📅 20:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107510">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY9bBu_OLGFYLAMxDoYS3SexPMHRwc4Htko9UcDJb4KccbUe8Fk0uczwRGCRkJLIW0KfzF1sH_Jc58apZXCatf1Ov7bID90W6vS0z6ot9niiLcyMOOTvqp9TKiutDYLusdISanXW9ZNTvRmq0H97WoGrd7jL5JkXe8glmBk3Ulch4LZ7m5zazEJFTNaCyZek1-nkKwJXOYuxZyIBwEGRB3IZzXUQbQ4v1_6yCWnSvrFmUS5hSrRZJsoBH8ucsKEDKo9R6MEGkt_2CgBDK3xWUCpSSFbAgZ6Fe23J5NBFkZxhR3DUX41G3gAxSHo34yffzH2MHEviso8wcLtg4bSGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران حالا بهتر درک‌ میکنه که این‌ مرد چه نعمتی برای بازیکنان داخلی و لژیونر بود و فوتبال ایران رو از حالت کیری الان نجات داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107510" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107509">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=LqhY2o2t1YP6nEZ5lCSZCnoKI9SomEN_xZrRNvsvx2HERNoqGxY2auA7LHncYW8FcBw3q0lIK1bZMg1BQWkqNfzuzQW3w2mb9aom6lPJmk1xg3ZNJj9mp5sHvfWeIYoUnDwVDLA5mveJzEwHyYozWkLP9hFxjhCXy07RUb1nvSFD3qsJ3GkXP0Nj8fxUh2mx1KuvyksQQ4TqQM5_5S3Oblkkn5Z6AlWJxHIcSnvnbyjequsqLhlUl5JvlP44SvZgSAJrtYJr-LGizm-1-_jTGjCXK5o_tp2VKjkFvdy7DxiGf_up6WgPa_vhia8zSWZAXllKxJL3lK_8TdI7s9sDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=LqhY2o2t1YP6nEZ5lCSZCnoKI9SomEN_xZrRNvsvx2HERNoqGxY2auA7LHncYW8FcBw3q0lIK1bZMg1BQWkqNfzuzQW3w2mb9aom6lPJmk1xg3ZNJj9mp5sHvfWeIYoUnDwVDLA5mveJzEwHyYozWkLP9hFxjhCXy07RUb1nvSFD3qsJ3GkXP0Nj8fxUh2mx1KuvyksQQ4TqQM5_5S3Oblkkn5Z6AlWJxHIcSnvnbyjequsqLhlUl5JvlP44SvZgSAJrtYJr-LGizm-1-_jTGjCXK5o_tp2VKjkFvdy7DxiGf_up6WgPa_vhia8zSWZAXllKxJL3lK_8TdI7s9sDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل دوم روسیه به ایران توسط گلوین (35)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107509" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107508">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
گل‌دوم روسیه روی سوپر کاشته حریف!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107508" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107507">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117f9ab643.mp4?token=JsSv2cXdHyhktkwzrsyzAewCHlFXAmiZckH6Jv51zFjaFOxA0khbU0tfkoFsBmSmFoqySq-SL-43vgsfidX0rcqLZUeO41G06SEYi3PNpPlrvjXoHfFmX0phDZK8HY5rAv3tsY1sm0QPDOuty4dQrktfc9uEsE7O025S7nqwl9VNaRVNqVGGKTto9WmHNu3yqp0apScja54iUHZnRnk19U-3NA9oZDmM2A672OAScGiwFrui0fhDN-5afRVDEKFqsQ87ugOAD5qTjb7K5Y-Bm8wCObAUm6vPWQzfY9mWxLICgBQKOc_vikN0246PTI1MoE8Uzp9Pmr-ATEerwA9IKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117f9ab643.mp4?token=JsSv2cXdHyhktkwzrsyzAewCHlFXAmiZckH6Jv51zFjaFOxA0khbU0tfkoFsBmSmFoqySq-SL-43vgsfidX0rcqLZUeO41G06SEYi3PNpPlrvjXoHfFmX0phDZK8HY5rAv3tsY1sm0QPDOuty4dQrktfc9uEsE7O025S7nqwl9VNaRVNqVGGKTto9WmHNu3yqp0apScja54iUHZnRnk19U-3NA9oZDmM2A672OAScGiwFrui0fhDN-5afRVDEKFqsQ87ugOAD5qTjb7K5Y-Bm8wCObAUm6vPWQzfY9mWxLICgBQKOc_vikN0246PTI1MoE8Uzp9Pmr-ATEerwA9IKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇷🇺
گل اول روسیه به ایران توسط گلوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107507" target="_blank">📅 20:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">روسیه یکی به تیم قلعه‌نویی زد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107506" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-NeggMkbew7A2ZcxDR8ktBv6RRbsRF1W_4gOzvz5JMgoI-tKgIXuRh3zJIa3hl1ED2zjcBLXyKyp6w-ndqTPUueIieJjIuszUB1xOod2nTmeuNjDd-BdUbImXRb7VrisX5rmyr2vyfCRZpMzQvZu2g00QDgXMWGyXNTFDhMos4a86UeCv2bpyilrX4V4mwrUompkKZkWoxo8WuswJTgMa5yFsirEQzTSOHL4VnT0rcRSmTblHJQhEGpCZp9yYKWczzXiPikqac_im2zzpQFqRXJ26w_gkDBtwR7EOpblijaAxGyAu1QmmnepMCdJAVq8FmxX_Q1i3bH9rnkwJ7_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر تو یه بیانیه جزئیات تخلفات منچسترسیتی تو فاصله فصل‌های ۱۰-۲۰۰۹ تا ۱۸-۲۰۱۷ رو تأیید کرد  این جزئیات تخلفاتیه که تو بیانیه لیگ برتر تأیید شده:  منچسترسیتی با تعدادی از شرکای تجاری خودش قراردادهای جعلی‌ای تنظیم کرده بود که توافق واقعی میان دو…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107504" target="_blank">📅 19:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbW28HR_PTOO8znqRRc1QAEuwswkPsb7whRBwDyDIj-nHJluD_DimVLFIWServp6NbeMslcVt6mMTVrFA3Nl3IhzcCB355XXywjcD2lJ4BWgQ66hmsOb3coV1QIJCSIVMT9gHSerLH3bH5UVXIz4r8BZ08ft9CKZthS1rG-n8IRnatXMBOAm2RM3LP97OhVN7br7LygWn8OynuAyOJZFuxkhnSpVkMvrahI7BWh9DpL-kH0PH0nUM4GeH7uDEGHO77c_D34kdSCMyIAYe9PNnyRRTqh1AwvfjeaZWQgT46HPhFYh05k6nlvhqhhahC00NIrSEFESqlt5eP-yitnfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر تو یه بیانیه جزئیات تخلفات منچسترسیتی تو فاصله فصل‌های ۱۰-۲۰۰۹ تا ۱۸-۲۰۱۷ رو تأیید کرد
این جزئیات تخلفاتیه که تو بیانیه لیگ برتر تأیید شده:
منچسترسیتی با تعدادی از شرکای تجاری خودش قراردادهای جعلی‌ای تنظیم کرده بود که توافق واقعی میان دو طرف را به‌درستی منعکس نمی‌کردند. این باشگاه همچنین به توافق‌های «صوری» دیگری نیز اتکا کرده بود تا درآمدهای خود را به‌صورت مصنوعی افزایش و هزینه‌هایش را کاهش دهد.
این باشگاه صورت‌های مالی نادرست ارائه کرده و وضعیت واقعی مالی خود را از حسابرسان و نهادهای نظارتی فوتبال پنهان کرده بود.
منچسترسیتی به‌طور قابل‌توجهی محدودیت‌های هزینه‌کرد مالی لیگ برتر و یوفا را نقض کرده بود. در جریان تحقیقات لیگ برتر، منچسترسیتی چندین مورد از وظایف خود در زمینه همکاری با لیگ و رعایت حسن نیت کامل را نقض کرد که از میان چهار مورد ادعاشده، سه مورد تأیید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107503" target="_blank">📅 19:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a09194b9.mp4?token=YxhdwuzybbCPUxOveKtIh3eH0xibFG9eMOC-TQuFmwDCqUwptnKqoWnN99ULGkoOZ0qVXWlYqzVopVPZtk6y4anChCCUuVN6YL8mMhZtIYcg2rWXpd93O9RCJHG4bpYJmR61U0Aah5RSuPjueOFtRsw6A7Ry_4KJlyAA8l4XH9aKz4JaR1N4DQ5pbKrf9vDmtA1pWtwcPaWoxNYP8YXyI9nxauxj2xDvTnW_4F-3tRKEpiut23HR7kBS8wnB86jMgXnAh5pBtCfvedCuQS8A2Ycw2_Z-bnnBH4KehXBwgOWCHHFhcX41nuxeHZxw77zgWQS5rsDDVpiraiHw3Jc2bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a09194b9.mp4?token=YxhdwuzybbCPUxOveKtIh3eH0xibFG9eMOC-TQuFmwDCqUwptnKqoWnN99ULGkoOZ0qVXWlYqzVopVPZtk6y4anChCCUuVN6YL8mMhZtIYcg2rWXpd93O9RCJHG4bpYJmR61U0Aah5RSuPjueOFtRsw6A7Ry_4KJlyAA8l4XH9aKz4JaR1N4DQ5pbKrf9vDmtA1pWtwcPaWoxNYP8YXyI9nxauxj2xDvTnW_4F-3tRKEpiut23HR7kBS8wnB86jMgXnAh5pBtCfvedCuQS8A2Ycw2_Z-bnnBH4KehXBwgOWCHHFhcX41nuxeHZxw77zgWQS5rsDDVpiraiHw3Jc2bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باهم ببینیم قطعه ی زیبایی که استاد جواد خیابانی برای گلر تیم ملی، علیرضا بیرانوند تو مترو خوندن
🗿
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107502" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107501" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107501" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfM6VeKCB1xs6_LRiYFY90MoxD5cGYux-kN_Jc1_wIRaqmJVQUHThjkbixmT7DdnCcvLrof99b9nW4YX1TdH0lS5ILGLXx3xZYdupQbNnjncwntmaFfEFeebAmWE2gAWpS3vrPEKpBKq-9Ly5tFjqo8IBhrdzhr41DArVSbtRIH9EttP5xQQjq-En4ABi2YdBW_tEAVKlnHD5Zp1B0jbxDws_JxaZeRKOe4xlc_Cc5l-sbUdYoy4wVaBFil6hZYGWhjBXtDMbgvi7-zlU8Y0r6KzhdsFn-0ulc2EWu_747VbpOKQf4G6bX1j9OZsD4s950ldmds7DTtcKO6o3LjPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز کرواسی
🆚
اسپانیا را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
کرواسی: ۳ برد، ۲ شکست و ۸ گل زده
اسپانیا: ۵ برد و ۹ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107500" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTItXmAzQjxZirRm2K0vX6hcUMk9EaSRw5fFeh6pp-1X7RtFYmfzNrJ8EFNqH9GYmob5uQW8ObSij3_TwcV-hmNatdir9ar-Nz-oI2VovTxCNc6lFrsKRiQh-kiJ5F23HyVla9_oIb16nwCUuMavkxBL1Fh-15M72hUZHIymUnJK0cfTTJ7FCmWJWEzOh3O8GiHNOnG1WQxx3MSewKcxAFWo2xrvSanBxZtvcmibcoFQuDdLWg9iotFxIqozQNB_x5bVZsVpYM74iWBLEn28yj4X76dIFCFEqF0N9-QO76rDxL-Fo48YabZcHjYksMAbUMBPpoY0_Q2cfARvM_O5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
رونالدو بدلایل نامشخص در تمرین امروز پرتغال حاضر نشده. تیم ژسوس قراره فرداشب با دانمارک بازی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107499" target="_blank">📅 19:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=SNs-ftRhrUcxhvHqFhQp9QZDWIMOByRy3zHPKt-LEjoEMILUlo7jrNoYNdhAxpfDMXREYEAGS0Wc1Pl4nRaIFqWLOM3Hb1ckkQF-CGPv_Q9e_Fea_NhRkpOjjQxiD9iPJulLoDtKhTH-hYlnubBODx-Ri03tS0z_yIpAxFYeWh1Y_sHj5Eyak0BHv_yNaJZTDlHSOpJkcwGWK9kcIRYsH64SqHMNFRHctCZNMAS2m44cFYpL8-eLImIIE35GbxNRM9Q8vRwiyWm-A55Bfv68jyipLjfekxtmBgnKQCckKXmXSSZ9MfTVvVoyLSUMpoPvljgwkGvDw54f_imOTVB6TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=SNs-ftRhrUcxhvHqFhQp9QZDWIMOByRy3zHPKt-LEjoEMILUlo7jrNoYNdhAxpfDMXREYEAGS0Wc1Pl4nRaIFqWLOM3Hb1ckkQF-CGPv_Q9e_Fea_NhRkpOjjQxiD9iPJulLoDtKhTH-hYlnubBODx-Ri03tS0z_yIpAxFYeWh1Y_sHj5Eyak0BHv_yNaJZTDlHSOpJkcwGWK9kcIRYsH64SqHMNFRHctCZNMAS2m44cFYpL8-eLImIIE35GbxNRM9Q8vRwiyWm-A55Bfv68jyipLjfekxtmBgnKQCckKXmXSSZ9MfTVvVoyLSUMpoPvljgwkGvDw54f_imOTVB6TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صداوسیما والیبال را هم از روی آپارات پخش کرد/ بودجه ۴۰ همتی برای مخفی‌کردن لوگو!
📺
سازمان صداوسیما که به‌خاطر پخش قسمتی از یک سریال تلویزیونی در کانال آپارات کاربری عادی به نام نفیسه‌جون، از این سایت شکایت کرده و دنبال جریمه ۳٫۵ همتی است، بازهم برای پخش مسابقات ناگویا تصویر زنده آپارات را بدون رعایت حقوق ناشر تحویل مردم داد.
🤯
جالب این‌که همچنان سانسورچی به‌دنبال محو لوگوی آپارات است و مجری تلویزیون قطع پخش را به ارتباط با مرکز(!) مربوط می‌داند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107498" target="_blank">📅 18:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKeOcU2kHSJxP3tTDuyqx_PZxC-c-HJ7u48jAVf01AlBHWuJce8pH-J8j5Q8KyK6yha9QI3g5xOJdSmn89e7Yd5-kymshKRfDguCFV3K0zhXctPMajWM8z5vgM8z3_omMvc-KuFxTgLBpYQFhyzgg8_W1NgVXtZ3VEo8mkSOsHEqG4kvviAgmynT2d96lqOCFG1E9q0x_l9sgKeG-t5aVrAWBkFijiH8N9LBz6T2AV0VrFvgn6upWqYqDZOEcLUenZ0wiBaB9Mb9qOwkPtjI8P3bvep6dyZ4pSZSSrM1nFfOEpai710UfI2hUWdGHPLkRt5oRHH1oNRkRgAqCr2InA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب تیم ملی ایران مقابل روسیه
سید حسین حسینی، شجاع خلیل‌زاده، علی نعمتی، صالح حردانی، آریا یوسفی، رامین رضاییان، سعید عزت‌اللهی، محمد قربانی، محمد مهدی محبی، سردار آزمون و مهدی طارمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107497" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlHfq9eIKjUsFN2XgtcgBIlgU8AUCvSi-kLhXzHQKyTCofmVjY1dat9kLSKzncxfDsP_pusRq32BLYxv9RWMRnEtKIjT2rLvkUVINwxDBC9eoVEAciH7WWFLys7B6H7zHENzKgeXGVGuVW-TAEz7JtR9YbqXsq1LL5UMrEMeSYHWKovJEmHO887SKQi-z37awaq0HbQlWRgcZ1uz09GFVEYpVPtHYUFTWU5ssKi2xFPHK7rd7Id5_FVKsR748G7lZN7Ck2ddrzAbpDDPJzLoqsLJ8bj-tLAE2RUhmc1y6NNu7_auV41dU5djzHMIKlgew6qM_gcWU4ok0HTo-m50Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
مصدومیت های کریر رافینیا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107496" target="_blank">📅 17:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30660fe341.mp4?token=oKTsmbcKBBImvdyqaN0mu89ZVs46b2px5gjNciZiwT4R8bVSZjsGUb5GI8n__SEf6oMl7u347yqYUr-twnh96LgZYZhsraZ9msLOVI6wEDDdlcoo9FrA6pHC6STACCiZVQoAqa2SbTqAmNwcTnJLqahv66Hbbmv1FImOXoZuVryZPbEiQXgWlHTHYiMZywJTYmwbnkXHztzkn8GNfnIxfqGsieTDk4-hk5YT-zW6VNPLooRpZ1T5Q482tyDwmtP40Eyr2PqqKT2H-CAWpySTP1PPHe2xeV9qbQzidd_f2uUS-Et1jNi-UAew4UNL3HM13lUE8d9Ga8fTxqllqYb_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30660fe341.mp4?token=oKTsmbcKBBImvdyqaN0mu89ZVs46b2px5gjNciZiwT4R8bVSZjsGUb5GI8n__SEf6oMl7u347yqYUr-twnh96LgZYZhsraZ9msLOVI6wEDDdlcoo9FrA6pHC6STACCiZVQoAqa2SbTqAmNwcTnJLqahv66Hbbmv1FImOXoZuVryZPbEiQXgWlHTHYiMZywJTYmwbnkXHztzkn8GNfnIxfqGsieTDk4-hk5YT-zW6VNPLooRpZ1T5Q482tyDwmtP40Eyr2PqqKT2H-CAWpySTP1PPHe2xeV9qbQzidd_f2uUS-Et1jNi-UAew4UNL3HM13lUE8d9Ga8fTxqllqYb_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
على تاجرنيا: با والتر ماتزاری به دُمش رسیده بودیم اما پیام های داخلی برخی هواداران پرسپولیس باعث شد قراردادمان امضا نشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107495" target="_blank">📅 16:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107494">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=I-RmjWlAN138wQvcvx-p87TnKKwe3DHADPeFYptHklNpfHdMYP9w00gq4tfgk79zeuB9iBwAuy2XSms3EKkqfl_LZbRLvKLpyEn0I6bAjcRm2BgI58DEy8yBfeEE_OdsHqJNDSEbrsRYEm8ujeMQI2CriwtD9uJtocoBcfXc_CB_-90S32bgNRB-3VL4byvRzJbZfX3T8j4gKUV-qEcAmpwLBi8S_oPE_R9JJCuE27GUGHqc5SKtGR5x13_fNYYDy4kgwuS5joUygACanCDqx8H1HlRXJXxu1TazhO14cPae2vnCqaKy3WrptEgjxDlLQVajIO7xEqraYbUfCtbpEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=I-RmjWlAN138wQvcvx-p87TnKKwe3DHADPeFYptHklNpfHdMYP9w00gq4tfgk79zeuB9iBwAuy2XSms3EKkqfl_LZbRLvKLpyEn0I6bAjcRm2BgI58DEy8yBfeEE_OdsHqJNDSEbrsRYEm8ujeMQI2CriwtD9uJtocoBcfXc_CB_-90S32bgNRB-3VL4byvRzJbZfX3T8j4gKUV-qEcAmpwLBi8S_oPE_R9JJCuE27GUGHqc5SKtGR5x13_fNYYDy4kgwuS5joUygACanCDqx8H1HlRXJXxu1TazhO14cPae2vnCqaKy3WrptEgjxDlLQVajIO7xEqraYbUfCtbpEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
وقتی امیرحسین‌قیاسی با چندین یوتیوبر مصاحبه و از درآمد عجیبشون سوال میپرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107494" target="_blank">📅 16:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107493">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=aWIuIYQLiE4QLZSwbjuaLvCXW-PjaFLK_bn_PN_3V6-P0cNsbz28P_sNbv7RRzpZFIvdjoozYOtg-t7Zzre0U_dxskzB9Pw2Z8qt7kYA-KsH-tu_3gerrJDOc4ZPKMTt9AhWrsqYH4_dq3PmSps9Hbj3rg4LXFylf84St3ko2L6JeBVZuV-UQzfnTu351MEJyjA9TzZp_GjTQInklcaZg1dAwQ5V0rgIg3E74C72evgf1hWOJ3HpHIiCf6uAriT5fm6pqbQJkJoY7hQBQWX5i9cBUtV_Q1K5F0K2Ng0larDvnCCssDb-x9INrQA49ZEJTQAq51mJA8fQk8joGjYsaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=aWIuIYQLiE4QLZSwbjuaLvCXW-PjaFLK_bn_PN_3V6-P0cNsbz28P_sNbv7RRzpZFIvdjoozYOtg-t7Zzre0U_dxskzB9Pw2Z8qt7kYA-KsH-tu_3gerrJDOc4ZPKMTt9AhWrsqYH4_dq3PmSps9Hbj3rg4LXFylf84St3ko2L6JeBVZuV-UQzfnTu351MEJyjA9TzZp_GjTQInklcaZg1dAwQ5V0rgIg3E74C72evgf1hWOJ3HpHIiCf6uAriT5fm6pqbQJkJoY7hQBQWX5i9cBUtV_Q1K5F0K2Ng0larDvnCCssDb-x9INrQA49ZEJTQAq51mJA8fQk8joGjYsaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
#
نوستالژی
؛ درگیری تاریخی علی‌دایی و محمود فکری درباره تیم‌ملی در دهه هشتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107493" target="_blank">📅 16:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St_nzex2VJ6-6n1HnqeKCfh_Yl9SyPpr9cct2qUOSgqDQK1TPPpgdXprZujGrw5io00SaP51FKJuNufQ2Ni8XpmeHsZcigWAuCg7ZOZp59uhx6I3YSU27tJHQ0wPxxUuf58l_pH89J-v0j2komyu30d0wgVNIoNb2pqCYVVY-7yEZrdCWfrn2ayQaJj1JOgLVw-AX3RXfYzam01Y95c7vDDPuGVKLOLRbHHl_tQjmPzauFtZYX4fIEDseX6aZ7VH9PhB5B1G3pEL6Gr0yfNN8j87BqcANm3aUB4aVUerevYKmDB3q8m8UvtVzK9dzuE2oeD7ryvej07jcPhVJejcNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
میزان دوندگی تیم‌های لالیگایی با رتبه فعلی آنها در جدول مسابقات این‌فصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107492" target="_blank">📅 15:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بررسی پرونده فساد مالی منچسترسیتی به روایت دقیق رسول‌مجیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107491" target="_blank">📅 15:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107490">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚑
#فوووووری
؛ رافینیا در بازی امروز برزیل از ناحیه ران دچار مصدومیت شده و از زمین خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107490" target="_blank">📅 15:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107489">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=lRR1c72iqYa_5rZXVlKCxg9ACSbsu8YwY8wEc7Hha1YhUOdG_x3BiKXrGbhp5PKyU449Gi0dvJpb1yUIGXRT-KRVpfgZfudAK8iGh_So3BMCy4quWHYdIdMXCyO6bE5-wxvgvh9uGA4fY9ziqRmrdWYxzjoTQM2gskSGRZ7ydlNEsV5k0C3iuTm-D9Sl1rIZHoQLrf4n5QThiiB3q-_9XxpAOcOx7GwBFzHmUvMMkZsmH3I0JamtPPmvNp5ofW9Ao32FC0uC49j7TWx2WoiC-P_UoqLEwH90Ff5nrLmwbo8g5AB0SSzDhxcrHzk36xAuva0LW_DDjDkYLadbs_mPNoUwm9q4eAmJ0rINpyD54PHOueo0kUkE-RSiy8Vjx48A618JTNq2SrhQ7zJsSJ5ZKcXJVOF2o18VCywo60ixANufMVnYowxf58FLmjykH6I4gAV_p6ImOoseLmdqAFDAZu7U3wnJSaUhuuUuq5LCBY7mEake1kah71wtOP5HaoPMpsBWHcCoRt3lG444_JmEe7PczQI8xzHGLHCLp4641n2KzZy1x7H9isIqb-pce6LKkyCUCuU_UspCAc-Ti-L4DLKh_1UQf1xzaWHRwQPeGdzWbYXw87SoRRZ0MsQYEUJB7wd60a47i-NKzy9KaptVcODa90QDhp4bP_au_MLBCg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=lRR1c72iqYa_5rZXVlKCxg9ACSbsu8YwY8wEc7Hha1YhUOdG_x3BiKXrGbhp5PKyU449Gi0dvJpb1yUIGXRT-KRVpfgZfudAK8iGh_So3BMCy4quWHYdIdMXCyO6bE5-wxvgvh9uGA4fY9ziqRmrdWYxzjoTQM2gskSGRZ7ydlNEsV5k0C3iuTm-D9Sl1rIZHoQLrf4n5QThiiB3q-_9XxpAOcOx7GwBFzHmUvMMkZsmH3I0JamtPPmvNp5ofW9Ao32FC0uC49j7TWx2WoiC-P_UoqLEwH90Ff5nrLmwbo8g5AB0SSzDhxcrHzk36xAuva0LW_DDjDkYLadbs_mPNoUwm9q4eAmJ0rINpyD54PHOueo0kUkE-RSiy8Vjx48A618JTNq2SrhQ7zJsSJ5ZKcXJVOF2o18VCywo60ixANufMVnYowxf58FLmjykH6I4gAV_p6ImOoseLmdqAFDAZu7U3wnJSaUhuuUuq5LCBY7mEake1kah71wtOP5HaoPMpsBWHcCoRt3lG444_JmEe7PczQI8xzHGLHCLp4641n2KzZy1x7H9isIqb-pce6LKkyCUCuU_UspCAc-Ti-L4DLKh_1UQf1xzaWHRwQPeGdzWbYXw87SoRRZ0MsQYEUJB7wd60a47i-NKzy9KaptVcODa90QDhp4bP_au_MLBCg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
اگه‌یه فرد سیگاری هستی حتما این ویدیو رو ببین و برای دوستات بفرست؛ تاثیر مخرب سیگار روی سلامتی از زبان دکتر رهبری...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107489" target="_blank">📅 14:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=dI2dWUHeJSkNgAR9xpI5hp7rPJonC3VuwmBkWH1HYrENKB-PMsazUp3sVEHb42GAScQBCMp0b30SN4BISX4LIk29-b9o_RSdP4c-v3DjqTox2kjbPIAShbPpAOw3dsrX-I10jmcvWn4pUz_Zdgq6f9MLBtcR7iGhaHZMr6BWFsYBp_K3CopqJKrzM-pBTbO9dhvt2GalgKQYBTBKtPcviTtusCptMto7lVXI-YItgrNXwkJ4tZH8mRslu_DuGZxtpBaRNHkDzuCqeUMRqwAOhnEmk1M4tHnTVgfdoh5NWo899jn-DQIOfndUNhAVjywGEQj0QxQT6S4w8ilsS4uqAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=dI2dWUHeJSkNgAR9xpI5hp7rPJonC3VuwmBkWH1HYrENKB-PMsazUp3sVEHb42GAScQBCMp0b30SN4BISX4LIk29-b9o_RSdP4c-v3DjqTox2kjbPIAShbPpAOw3dsrX-I10jmcvWn4pUz_Zdgq6f9MLBtcR7iGhaHZMr6BWFsYBp_K3CopqJKrzM-pBTbO9dhvt2GalgKQYBTBKtPcviTtusCptMto7lVXI-YItgrNXwkJ4tZH8mRslu_DuGZxtpBaRNHkDzuCqeUMRqwAOhnEmk1M4tHnTVgfdoh5NWo899jn-DQIOfndUNhAVjywGEQj0QxQT6S4w8ilsS4uqAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇵🇹
پیام‌واضح ژسوس به رونالدو پس از نیمکت‌ نشینی در آخرین بازی پرتغال مقابل نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107488" target="_blank">📅 14:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107487">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=FUvgq-FTbOTdLldlU_7D8AyTe-o38DXyaj21ukOzY5nP0HE7g4X_XHndWzU6NEQ14XWpyz7A8Iz2AZ6ZQaSVtc6C2A5YXonRUWiHGA56GuuIkCVc3hZWprB56FiY0S5-IwpvEnKperGZZWPxotTYp7aUB3fMUn20Pv46YgjWME9WyV3-lFZ1e39ZDRvX53rWV30O6VV-lGXCCI3ZPd-D0XRSwdJ-rnZYF06IYtmCDSAoDZ1SLw1adWvX6R8j848asBjk1P4yTu4UgSUDlBYDKQxdgkO2QnDys3Gwq06WwL-F0xav1OdND24OqWnzgrJu5SCLtFTcLTsCRJPif7uz6rp1K__-xMZlkhL5QXPyGey7_1P95S8FP53Nzn1oEqnYj9NnzGiAXh_Cbvnr5ruuccX9b4q9s3wgBeS9uJfrVfYEpAfRZzlXnPnVVQHrS5xBAW_vFp6mdtzDuF3uEStXP8ZrDg5d6m3qnRMYCEtyN5jAP-wLxdGWEA5CWDdgEIB6pREA7KRcCl_H3zVkdC1iizm6ndv_ouOxiGccmzdMxIvJr2eH_C3-RrUSgWFkJF4PRKF1cns1PEIpCS28yzm41nz607i-AMLxnm_JZwewRpwyYBB3Xld2UmgtLh4kFq6fnX16wXGNN7ii5w9qBufKOD0rQCI2Xc8GoSrssvrI_yM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=FUvgq-FTbOTdLldlU_7D8AyTe-o38DXyaj21ukOzY5nP0HE7g4X_XHndWzU6NEQ14XWpyz7A8Iz2AZ6ZQaSVtc6C2A5YXonRUWiHGA56GuuIkCVc3hZWprB56FiY0S5-IwpvEnKperGZZWPxotTYp7aUB3fMUn20Pv46YgjWME9WyV3-lFZ1e39ZDRvX53rWV30O6VV-lGXCCI3ZPd-D0XRSwdJ-rnZYF06IYtmCDSAoDZ1SLw1adWvX6R8j848asBjk1P4yTu4UgSUDlBYDKQxdgkO2QnDys3Gwq06WwL-F0xav1OdND24OqWnzgrJu5SCLtFTcLTsCRJPif7uz6rp1K__-xMZlkhL5QXPyGey7_1P95S8FP53Nzn1oEqnYj9NnzGiAXh_Cbvnr5ruuccX9b4q9s3wgBeS9uJfrVfYEpAfRZzlXnPnVVQHrS5xBAW_vFp6mdtzDuF3uEStXP8ZrDg5d6m3qnRMYCEtyN5jAP-wLxdGWEA5CWDdgEIB6pREA7KRcCl_H3zVkdC1iizm6ndv_ouOxiGccmzdMxIvJr2eH_C3-RrUSgWFkJF4PRKF1cns1PEIpCS28yzm41nz607i-AMLxnm_JZwewRpwyYBB3Xld2UmgtLh4kFq6fnX16wXGNN7ii5w9qBufKOD0rQCI2Xc8GoSrssvrI_yM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
دیس دکتر ابوطالب‌حسینی به دکتر بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107487" target="_blank">📅 14:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=I0xh8FPPkJvTsyEegAVvGWJsfvaaUDtR61KDPVb6gqXxKDJ1mqPD5lHP9dcslEAc4hnxjmE0-2KqbKetyQQ0VDghqwuYuvWJJp6vDLsKY46HvMKDwpe5h9lw12iwAKgkGsF4zOwMIC0Ivb196gWzBYfHOL_SBnHQQMTRH8-pVH24tf8s2_MDPcQRZYFTqVeqyxFpCE9Dv79reO4MlQLztMgXUvFpDvKE7GLVAw4t8oC84ZJ-5Ijr85MQSUDKzuqrMhofjO8Vs4aBfA4yLRX7jSYJsulyWtnJ__90r56Wx0bl_QOncfQNZ9vlRmg9GyVm2TgPr1_uV8zJ72QY4Lxvbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=I0xh8FPPkJvTsyEegAVvGWJsfvaaUDtR61KDPVb6gqXxKDJ1mqPD5lHP9dcslEAc4hnxjmE0-2KqbKetyQQ0VDghqwuYuvWJJp6vDLsKY46HvMKDwpe5h9lw12iwAKgkGsF4zOwMIC0Ivb196gWzBYfHOL_SBnHQQMTRH8-pVH24tf8s2_MDPcQRZYFTqVeqyxFpCE9Dv79reO4MlQLztMgXUvFpDvKE7GLVAw4t8oC84ZJ-5Ijr85MQSUDKzuqrMhofjO8Vs4aBfA4yLRX7jSYJsulyWtnJ__90r56Wx0bl_QOncfQNZ9vlRmg9GyVm2TgPr1_uV8zJ72QY4Lxvbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
عادل: ناکامی تیم ملی مثل داستان تورم شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107486" target="_blank">📅 13:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107485">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=u72q6wxb5ozzS5crWg6A6O1l2tA_qz9aG72IXP0Bva64Dn1WHiuBepqr2UPCvee_KwGx-QJZ3yfJ0YXecWuMGX9ufQN_A_o2rISG7MN-32DLTdO2JToLcSRWnkpFJNWHMh_WJNsaa_nFpgxcye957A0baTS0N5UM02PxeNSui4dIfPIhZJNZ5nOv4wRAVOlW9ajDoZkrNyVUmVhLtzdKZzGvD4CmbHEqgZn98Oicf9rm7OtVP8SQ91U7Rhi7UHhWbyXQflLSpmzQYnB5OaPRN_OXTE8tZE_c-p7Hn1T7h4C47ZOCXrsgALa_rLSEtEopPE-jFqH8Zt8ZSva9ElgxkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=u72q6wxb5ozzS5crWg6A6O1l2tA_qz9aG72IXP0Bva64Dn1WHiuBepqr2UPCvee_KwGx-QJZ3yfJ0YXecWuMGX9ufQN_A_o2rISG7MN-32DLTdO2JToLcSRWnkpFJNWHMh_WJNsaa_nFpgxcye957A0baTS0N5UM02PxeNSui4dIfPIhZJNZ5nOv4wRAVOlW9ajDoZkrNyVUmVhLtzdKZzGvD4CmbHEqgZn98Oicf9rm7OtVP8SQ91U7Rhi7UHhWbyXQflLSpmzQYnB5OaPRN_OXTE8tZE_c-p7Hn1T7h4C47ZOCXrsgALa_rLSEtEopPE-jFqH8Zt8ZSva9ElgxkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📱
پست‌جدید سعید صادقی بازیکن سابق پرسپولیس که خبر از ازدواج‌خود می‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107485" target="_blank">📅 13:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107484">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
نیکولاس‌سوله مدافع سابق بایرن و دورتمند این روزها مشغول دروازه‌بانی در لیگ‌های پایین آلمانه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107484" target="_blank">📅 13:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107483">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=sXdo2GWA72FPoWLTqX6u9TdEncAKtAbjwzQZUD_N-Yq8c46KySTWWWjmY9PspE1FT9dc0GcFH9gei29AAkQo9K2hQbMz7t2Wy7obTqc2xqzaLpfMjVPkbkO3Js-JKv-ErCuA4r2JfZr5wVnOEOmUrk8WytX4NwB7G5bjf4L4q_rJg9ruYNME7B3k5vcxGatiobgathm59PbAmRzeQ8IKn6on6lY0x2By1kKU46bL8CgqWxVnLuToA0bRYB7FdiTbxDTbpDlgWhVzOkkL_MGkbB8umFPrEsSLzXEDOH5RI36nd0MybApZQTdzwJFD2e2n7L7mDUbwEXzgRPxvOat8Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=sXdo2GWA72FPoWLTqX6u9TdEncAKtAbjwzQZUD_N-Yq8c46KySTWWWjmY9PspE1FT9dc0GcFH9gei29AAkQo9K2hQbMz7t2Wy7obTqc2xqzaLpfMjVPkbkO3Js-JKv-ErCuA4r2JfZr5wVnOEOmUrk8WytX4NwB7G5bjf4L4q_rJg9ruYNME7B3k5vcxGatiobgathm59PbAmRzeQ8IKn6on6lY0x2By1kKU46bL8CgqWxVnLuToA0bRYB7FdiTbxDTbpDlgWhVzOkkL_MGkbB8umFPrEsSLzXEDOH5RI36nd0MybApZQTdzwJFD2e2n7L7mDUbwEXzgRPxvOat8Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
وضعیت وینیسیوس در بازی با استرالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107483" target="_blank">📅 12:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107482">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgixkyLK6Y9_Dp-sBmfSHgUyNaXYfs4SDho92IM0T9QDqY-Bozmldm3TkxB1E5fozjliZSaJOPQn8W5Zv9ZhV3-koYMdWeq6Ubn8LTN7bLfW9GmwRPeB7V6Q8xn_bpTdyjhIXZD24Fe4tZ11_ly6_6IjOgje8FtALSzLgOa1TVafQWlxY3vnr9LUqTPWo7yJPMYjuS0kYlQxOB6n-DnXCC3WsmGlOKfcH2iLm1PET3GOUYI_fhE3gIYlitttAJRRnSc4nDbAz-qbPB98Nu5B0W0h8hf24iHek7naysAry2RwMmq5UGIbAwxTohY68x2P-HriNHVB0CBPC9GavzkVHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
علیرضا بیرانوند به دلیل تاهل، داشتن دو فرزند و شش سال فعالیت مستمر در بسیج، ۱۵ ماه کسر از خدمت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107482" target="_blank">📅 12:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107481">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=VLJiKy9CQR8-poSMuyq4WJttc26mIk-1pDFX6ORiARK2l3hAGj7qnad2JxE2Pj0Oq2chFgQrjKIuA501gXB2QD3exqcKl7TrB8N_CTCqjAhvNPuTuAl_N3MWMDHbNZloDhlmbYZ58bs4moJI1iqtaAw1eT-dD2gr8IxeOeF4InW4xtZmV2tKUBTG_KHfNpRn2osFyJ8nTl487T6YtW_DZ0H0y7TJQIMzfRg3USf7i6xGyv8VdZu5FJPD8JnFLkyeiwT3hGjMG_HAhHz9fkPyK3NU8R3r8GRCevYD8Kh8gLh-sc94alrwbjKPbIHcTCXUyjMPad6oiMSNjSlQzEY7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=VLJiKy9CQR8-poSMuyq4WJttc26mIk-1pDFX6ORiARK2l3hAGj7qnad2JxE2Pj0Oq2chFgQrjKIuA501gXB2QD3exqcKl7TrB8N_CTCqjAhvNPuTuAl_N3MWMDHbNZloDhlmbYZ58bs4moJI1iqtaAw1eT-dD2gr8IxeOeF4InW4xtZmV2tKUBTG_KHfNpRn2osFyJ8nTl487T6YtW_DZ0H0y7TJQIMzfRg3USf7i6xGyv8VdZu5FJPD8JnFLkyeiwT3hGjMG_HAhHz9fkPyK3NU8R3r8GRCevYD8Kh8gLh-sc94alrwbjKPbIHcTCXUyjMPad6oiMSNjSlQzEY7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خاطره خنده‌دار امیرحسین صادقی از سوتی وحشتناک حنیف عمران‌زاده مدافع سابق استقلال وسط مکه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107481" target="_blank">📅 12:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107480">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBNuSTYX7yejZ5GH9zDbYVtc7aOXXr-HU6lUQZh2KVFcJNG9AbkEOUZgwGVpGBbeudrbpV3ju67XyM_yT93DVlJU9xL-4ZcBV-rK8EbUhgrrjkRQSw0ZBbqn5fFFUyifcfmTSmtnhX9G2wpMh0UK2fvSgZrekbY3Lq-guOTZeVyMw9eO_9UmEORN5wPqlckLPKo5JTSXLEA3aDZb6PuD-dv6dI4TMVpApWQ8LFm1TWZZVQzlZRp19onXcEQw4TnRg_f593ftqI139LboaQ6SACCRtOALNv4sMcGUzPWm7U8S5Qpg_cRnP0aaqbkPv2d8jGi_ThNqUtqsUmPcHe3tlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107480" target="_blank">📅 12:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107479">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=LebN8hIEF8d6NJoQX7C_OPhgm7WocEvaSSfXmGS8F91wu74kRm5jP_yWpjYagAZx9UaDERDdJqjz5NKTqEN70i7cDUu5HmzKbx1Wj31tDkH0AeZ3umDNHhOG5XEAtobcQy5VgEX9wo0JgWyzzREr_bgDTQguOB6YRnbkkoG3EjbweZS09Fan0bNmAtI1VURaMseoH4TwWz8wh3K_W_KJa2PnZIZDQlC1vmGU763og1RTotWAqZGHi5QyEybYCSW2NxX-oajIJ2DMW3Iuf3dbAiqijc6ORz6FNk0lu9ypDqhV6smNbWO1XxfrdqztbP9iVxLS5B3RXjMZF_lWtpWqvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=LebN8hIEF8d6NJoQX7C_OPhgm7WocEvaSSfXmGS8F91wu74kRm5jP_yWpjYagAZx9UaDERDdJqjz5NKTqEN70i7cDUu5HmzKbx1Wj31tDkH0AeZ3umDNHhOG5XEAtobcQy5VgEX9wo0JgWyzzREr_bgDTQguOB6YRnbkkoG3EjbweZS09Fan0bNmAtI1VURaMseoH4TwWz8wh3K_W_KJa2PnZIZDQlC1vmGU763og1RTotWAqZGHi5QyEybYCSW2NxX-oajIJ2DMW3Iuf3dbAiqijc6ORz6FNk0lu9ypDqhV6smNbWO1XxfrdqztbP9iVxLS5B3RXjMZF_lWtpWqvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
تشکر عادل فردوسی‌پور از ابوطالب‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107479" target="_blank">📅 11:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107478">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc8kyeubjYFFs_Tx4X5rQQYxS5UU2UcAYOYh9UnbcdLBh8bcl3ahpYqeUEbx4Th1RWYItNP-lzroX7_fpXt1aTp0pD2O4RS2YGmlLV5GQC5MMGXfEaUqfnFUeL6sdOheHcczn-K1cVYJ240Rjvu_7qqQ7AKXIdboF9D7ySFz3YnwHTAzpBTRSqHiUiEalGhVcGRZNbozXr2HpUPIJjx4_H7eNOq19xUOkhYUYal5UC2Zxj5IPX5mqrZ6D98WLjMmeuFaGjApzlu2qdIqI-4HIKCeDqV-eKmJllTk0J_ommkfckZeG9yjZw5jw4RvXrZG_GlCkoygzUkloWglgr6CNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
وضعیت دلار تا این لحظه: ۲۵۰ هزار تومان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107478" target="_blank">📅 11:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107477">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI52d5M-ykna_4WQcbUyzI9acuc9iVB7A92i0fgGvuUWwVIqOGxDqTxFXxkm6Q1xN_3fDjWYReyRsCR_0uvYjPk1Hzrne9XqPHu8RHe7CeIq4s-dlaVl_eBTlJRoszfynFPP7lQ5fXNatkQn8qbVxrboAHEQt3z7u2sk4ny4hq_zRDVH7KR8RbwbDWUSZCMjM5-hVQnUuCsAat4WPyI91NtMHLUiaEnaGYhMWpjwAErsrykbnJk_pWYP-_FU0-qcpAey2oviQcPU3lm1gKghAAsWkllKeKVWAmJAEWmpQPSBwYliJgxJP4hRDeyXgjPuPvNx747o04HrrrdFdsQxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
🇪🇸
مقایسه آمار رافینیا زیر نظر فلیک‌و ژاوی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107477" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107476">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nwsz3m6LiiUFBcjdkq2smWF7FH0YyoywPa57rHKDuBtYs8liOVswBH6t49_zdkUI0ySYveD7RCSyyQ8SAC5G56dU7Lplm5vvfmcFLMA4q6098fqVMCLoHwb4d4CCYI3dXXgFAcwcDdriz3xV0VHJ-Ia9IdwRPQqrvhrRlsaVdHGlY2Fnlidbb-nVB6yvvuxZ19WnsRTIOeC4spzclZklHDyrvQnj8jIKvphC6HQcpB0t4gGijDKX82J3_B92OY1GslIY6Soj4ESIbcllGAOeohjNmFTuxTMu5fRuF1BfzAhwKr3Dhf8ahFSa8O5LIDYSQ2cfRJ_YBDocidY7PSqe2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
بازیکنانی با بیشترین گل‌زده از روی ضربه آزاد در تاریخ فوتبال؛ لیونل‌مسی تنها دو گل تا تاریخ‌سازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107476" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107475">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107475" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107475" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107474">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh1ypW7yiKyRwgKtlXHIbcFFTa-coCACGpJwT5eodkG0QsugZ0djof3ktK9PDeczzzQu9LersSq1sys9nkZcs6u29lCq62HQl15HZ-tEHe1mdTNuNrR7qoElyoSUHO9tjXjFFbqSfnUJel3rfLEIKGrkERxuRBdnRtCuSFmp5eBMI4qIWnK6MypjdVWShYq1ohuLdULX0GV42qXgCGo3QJ0GmJo5qKnFgB-p13Vc5eWO9P3MOzAFK2lbCbnp4JKjgOAKFMZKKDqxIw2Z_XwF9Xb7s7CdGUN9YKeXFQ68mSQNx628HRhblAkcZCjO2P6e3qmU1j2FLpXw5CQed-BDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107474" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107473">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3862876082.mp4?token=k_eA22j8H2rwaTQjn8SYD6VpP-vBoExWzfNT3kil9V5zlq1z5INqYkFIpjw_gzCrEqMiz3p33JK0etLNE9ofaN1imNB-AP5ZvvUjzvC7OVd0kENa6_7AoY6IieU4S9gLNRVXIzGFHi0p1hKZFsPLFyCOu5yAThth55ro1EYw-YQ8tsYW9K95OXh2FCJ9zGbkptWyU8O67oNjuNE_1GkY1bz-mxclfTZP9ZG1aocOTZK6nmNr3NEWRuYh5uHvpJJPtkeO15Cb3z9zhP-iafDTYjzdVitxN00yyHbLgAGbssan3iC-ziENDB4HJGwmt_OWrQNw96l9wijeoY2Y7R1Rmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3862876082.mp4?token=k_eA22j8H2rwaTQjn8SYD6VpP-vBoExWzfNT3kil9V5zlq1z5INqYkFIpjw_gzCrEqMiz3p33JK0etLNE9ofaN1imNB-AP5ZvvUjzvC7OVd0kENa6_7AoY6IieU4S9gLNRVXIzGFHi0p1hKZFsPLFyCOu5yAThth55ro1EYw-YQ8tsYW9K95OXh2FCJ9zGbkptWyU8O67oNjuNE_1GkY1bz-mxclfTZP9ZG1aocOTZK6nmNr3NEWRuYh5uHvpJJPtkeO15Cb3z9zhP-iafDTYjzdVitxN00yyHbLgAGbssan3iC-ziENDB4HJGwmt_OWrQNw96l9wijeoY2Y7R1Rmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
انجام پدیکور فرشاد احمدزاده بازیکن فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107473" target="_blank">📅 11:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107472">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
‼️
⚠️
ضرب و شتم دو نوجوان سنندجی بدون گواهینامه توسط نیروی انتظامی که‌در فضای مجازی حسابی جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107472" target="_blank">📅 10:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107471">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=nJSu9QeUQlSmBZs2sw16_W3dVU0qIhWSotut1tDJmiztg-fanofVUwVYcvSF4wd4jfYuqCcg90G0aeqv-2WUkIXf-lPhyxnHp9dqhhF_3sx0IvruE_3hDy_NOTwf_VZDI2QOv-6dHaCLV_9aaERyPpIw1_BH42Yf7837zYcyMJgO6jDdx8JZEezCB190QTqSSdgtNofE4ILrMmK5yLq5yFkQRWhyiFWwlx4OrpoITT70PccgBR4CICFS7W5XpwKOjM2a3cS2XCZxqFu0WRBpkKTlhZWNKHT0MqIiDVtwoQwx66B5QB9eevMaB__c2lWhpGFu4Pvk9YreTZzMVKetvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=nJSu9QeUQlSmBZs2sw16_W3dVU0qIhWSotut1tDJmiztg-fanofVUwVYcvSF4wd4jfYuqCcg90G0aeqv-2WUkIXf-lPhyxnHp9dqhhF_3sx0IvruE_3hDy_NOTwf_VZDI2QOv-6dHaCLV_9aaERyPpIw1_BH42Yf7837zYcyMJgO6jDdx8JZEezCB190QTqSSdgtNofE4ILrMmK5yLq5yFkQRWhyiFWwlx4OrpoITT70PccgBR4CICFS7W5XpwKOjM2a3cS2XCZxqFu0WRBpkKTlhZWNKHT0MqIiDVtwoQwx66B5QB9eevMaB__c2lWhpGFu4Pvk9YreTZzMVKetvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از عجیب‌ترین مصاحبه‌های امیرحسین قیاسی که پس از یکسال مجدد وایرال شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107471" target="_blank">📅 10:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107470">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a5a16dba.mp4?token=NyoAPhtRkg4NRdc7Q1Qu1SoNHow2YzD2DnjedC5SXrMhpdLmqzwdrnSg8LdSW8xUEOHqu1rHIJqiyt1tdWyr_3Sx0sluEZTEzOxB9QmM7tJOAAOMIRHJy26iKx204ric3LpHor4cQbG4LH587SL6CbZGeGQARrs-zb5Wv8jl0TO_HzCNFKlMRTeiJRmGOA-IOjZR5bivLGu72Lhgxz9WQ1SHXEe6Q1VUJE0u8DphB6refThcMPFG-fKmh5QypBqtwSWCBsAy6AbcxhSrtyFDREnQC512tNLzk155cvrcUzCggyLcmQBQagONMmYMoajD_weGHpdQdNVjiF6LiVS7Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a5a16dba.mp4?token=NyoAPhtRkg4NRdc7Q1Qu1SoNHow2YzD2DnjedC5SXrMhpdLmqzwdrnSg8LdSW8xUEOHqu1rHIJqiyt1tdWyr_3Sx0sluEZTEzOxB9QmM7tJOAAOMIRHJy26iKx204ric3LpHor4cQbG4LH587SL6CbZGeGQARrs-zb5Wv8jl0TO_HzCNFKlMRTeiJRmGOA-IOjZR5bivLGu72Lhgxz9WQ1SHXEe6Q1VUJE0u8DphB6refThcMPFG-fKmh5QypBqtwSWCBsAy6AbcxhSrtyFDREnQC512tNLzk155cvrcUzCggyLcmQBQagONMmYMoajD_weGHpdQdNVjiF6LiVS7Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد نصرتی بازیکن سابق تیم‌ملی: آقای قلعه‌نویی آن مصاحبه مهدی‌قایدی را نادیده بگیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107470" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107469">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0c6152c5.mp4?token=MMXDhc-TWKBIUrYUYnIuexslbmV73_s3H5RkMvJ4ydz0PlWjbiWMgFtAQF1Kfvva8A-zcapcaWa6SY13wftwakvkDUzcslv9Zcwq5wGhKk99FTsSOYubJt5IpaVFXPD6xqFwVuO2bTr4NrkOox6tgjrAoXuGt82KJy4hfmFl-7fc-1SmRiOwvCLa8UuJQTVAT2bo1sHYG5NA90dGTU-82wvxj4f4kVo3rdacuRUgqfISyIXpP5-vpPcATEFOnFoCU4AoqZaveMLvW68VuWvMl0jL9WHg3M_ou_qEXfzg4esApCyrPXgnfansylFPqeJ2mzqxCCD4PZNm_iN2_aYnVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0c6152c5.mp4?token=MMXDhc-TWKBIUrYUYnIuexslbmV73_s3H5RkMvJ4ydz0PlWjbiWMgFtAQF1Kfvva8A-zcapcaWa6SY13wftwakvkDUzcslv9Zcwq5wGhKk99FTsSOYubJt5IpaVFXPD6xqFwVuO2bTr4NrkOox6tgjrAoXuGt82KJy4hfmFl-7fc-1SmRiOwvCLa8UuJQTVAT2bo1sHYG5NA90dGTU-82wvxj4f4kVo3rdacuRUgqfISyIXpP5-vpPcATEFOnFoCU4AoqZaveMLvW68VuWvMl0jL9WHg3M_ou_qEXfzg4esApCyrPXgnfansylFPqeJ2mzqxCCD4PZNm_iN2_aYnVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تشکر هانی رامبد از مردم ایران بابت‌ حواشی اخیر: مرسی از حمایتتون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107469" target="_blank">📅 09:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107468">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbj6NWFTTP9BigZ9gAyfaJPW79zpqidnscM13FXGuvtlwx6ZtoAhCYNlU0nPZuu9DrPfRpKUT708-FNln8-j8ZVYnvYJm0NgooEmKa5F1vRxnyzfKgUAKjQkN_Gt-H0AwEhZcrdAa7jv91z_oT1m-pqCADC_KumrB4uwUsVYHZ0TRSDL4GAdDl649A8zIF-ZCSvn-SarjPFsTukiO98zA6ywNWnS0VIDmcdjo42Torqsot20AlmD46B6H4WTRhL-JYuSp90hDI1-lqkQYN8M1VedmcMbACyKJj1_MmbsepIov9bjlBvAb4QviO0PJvS78QuThUIxeZ2DXpsFhscdgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‼️
تیم ملی اسپانیا هیچ‌گاه در دیدارهایی که لامین یامال را در ترکیب اصلی داشته، شکست نخورده :
🔴
۲۹ بازی؛ ۲۳ برد؛ ۶ تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107468" target="_blank">📅 09:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107467">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2d848cb.mp4?token=ij271wTGng240dnEICvhgjQ9-toJiNiBGND6sT3UWcze5NoL73-UjtOnzEKISlniT3RsNts56q2KAS-lXA_Yk058mpPwwTTYh0Fpe-SAwM7mCVu7shJelmgOP97fb1IAWiHH33Spwr2RoB1x6HXJtub5Fi8KY3J5EaFoIYU3Q8wY4-vst3TgyN2v56qAuxkQXPUIzzygSS0mPjOd8ZTihcYoLqWicMSNUXssRVTUvhrkf1RTgr2Sjd-vBhA50L3Nx90RB83EqaTzRWqnOxS9M-oePl6BLeslrl6Yo0pARQVl_aaPsnPEaxzctMuIRX--DqanAa9galCSdhER3lAFCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2d848cb.mp4?token=ij271wTGng240dnEICvhgjQ9-toJiNiBGND6sT3UWcze5NoL73-UjtOnzEKISlniT3RsNts56q2KAS-lXA_Yk058mpPwwTTYh0Fpe-SAwM7mCVu7shJelmgOP97fb1IAWiHH33Spwr2RoB1x6HXJtub5Fi8KY3J5EaFoIYU3Q8wY4-vst3TgyN2v56qAuxkQXPUIzzygSS0mPjOd8ZTihcYoLqWicMSNUXssRVTUvhrkf1RTgr2Sjd-vBhA50L3Nx90RB83EqaTzRWqnOxS9M-oePl6BLeslrl6Yo0pARQVl_aaPsnPEaxzctMuIRX--DqanAa9galCSdhER3lAFCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇮🇷
پرونده قهرمان فصل نیمه تمام؛
جنگ بر سر جام نامرئی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107467" target="_blank">📅 08:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107464" target="_blank">📅 01:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOhna3xEV4BEnOEgsTpUbD_7u1JdYqJCNA48uHD9qjig3bnNdvkW1uVGROBZywyZXo6k7mMdBzfVWESnKMHWGLFD5nwJC0J3M--QAvLOTvISwiHdubW7hs353JBFxl0cTYeYS3LV7g4W5gejy2gB6jXBO6y3UYvZlY86n3sZjPe1RQiLb0Tkrxr0PjooYGVGsjxsYK8kDHSx9fiE2D2WvefTJpS-7qqD7jzxC2OpL7Y3jIQyo4QZCZG-Q_yQH2SGd99-HM_1mDeqP0cFtrgUHArkcz93wPz7PFp-jAYxm2lFvSyPAakTBhnieesyuEV96lbFEH-ceOEx8AxM9qFgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
❌
⭕️
🇮🇷
با اعلام سخنگوی فدراسیون، قراره جام فصل گذشته لیگ برتر به شهدای میناب تقدیم بشه و استقلال یه لوح یادگاری بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107463" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=Ruvr_vOsNFfkF1BW3YnttU_DEbxv7eNtVZtL0Vb7sxobjcpGtLnrJgJX9ERFLgrfmGgysq9Sd_kRp02wlVRLYPfrJXNjPqfB2huO_r2UDLGX3bjjc7M1f-E2QLSmk1hiD3_FoLMhuf8bkeu2_SruEUoa6uFQUpR3xJcFDD8MDBGJTpcoO4n5d4cACGJEQspH_thk3KH96V2bg0jK2-KeaOggQKLEQh4xSFDW3o_xPGrNQ75oBk9WIDPSn9cdrg1uIw5akfjau8uKbUxlB5VpIzVNoPzYy2QSESh9fw1_2B1sSI7Pgi41Havu37I0zMhsAuRnODD6uZR_2Wk3Dp8yA1-Jjm3WLFryuZPjHBKCAffDsGdlP-pLPF6iqnQK0z7lKu4ZCtNjbryJtvWV_8SO7jEs4NZAZGp_57I1UK9V7hLLzfuF20wVQVq98_ncMjGkoEQl-uqCY_QRVUMbVDIQ2O8J2ZjwttpVfC33sANX_P0aneL-0JMjsKo1ZkRYtS3NAcOcQB83fU3_bdTLaIqmQ8vktNAsnScVRwxMgzcIOkN_t5WU7jz-mjf-MFTFIxoPl45utYxE1ceBfZ9YNdAVYqsjAT8pCUY5to76RUVrEbTJg0WrnJ1QTX9Kz93f41uFXpdUq7_HPzbvsJBmkto1ePU1HAf38ulml-9wTlmWorQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=Ruvr_vOsNFfkF1BW3YnttU_DEbxv7eNtVZtL0Vb7sxobjcpGtLnrJgJX9ERFLgrfmGgysq9Sd_kRp02wlVRLYPfrJXNjPqfB2huO_r2UDLGX3bjjc7M1f-E2QLSmk1hiD3_FoLMhuf8bkeu2_SruEUoa6uFQUpR3xJcFDD8MDBGJTpcoO4n5d4cACGJEQspH_thk3KH96V2bg0jK2-KeaOggQKLEQh4xSFDW3o_xPGrNQ75oBk9WIDPSn9cdrg1uIw5akfjau8uKbUxlB5VpIzVNoPzYy2QSESh9fw1_2B1sSI7Pgi41Havu37I0zMhsAuRnODD6uZR_2Wk3Dp8yA1-Jjm3WLFryuZPjHBKCAffDsGdlP-pLPF6iqnQK0z7lKu4ZCtNjbryJtvWV_8SO7jEs4NZAZGp_57I1UK9V7hLLzfuF20wVQVq98_ncMjGkoEQl-uqCY_QRVUMbVDIQ2O8J2ZjwttpVfC33sANX_P0aneL-0JMjsKo1ZkRYtS3NAcOcQB83fU3_bdTLaIqmQ8vktNAsnScVRwxMgzcIOkN_t5WU7jz-mjf-MFTFIxoPl45utYxE1ceBfZ9YNdAVYqsjAT8pCUY5to76RUVrEbTJg0WrnJ1QTX9Kz93f41uFXpdUq7_HPzbvsJBmkto1ePU1HAf38ulml-9wTlmWorQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تاجرنیا، سرپرست مدیرعاملی استقلال: ترجیح می‌دهم به خاطر بازی حساس مقابل تراکتور فعلا درباره مسائل قهرمانی فصل‌گذشته سکوت کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107462" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=qi-XzkFaWo1dIgRJSopz5AP2HdIGIZY3yhPx9w8r2opOlmIjzSAp4i_U_Sj7gMR9f3gU84iQ_Pfb2tT3ihUwuv9ZSJ8pITjkrL19NDC361LMW__CFQXQX8LOD0qBfR2Cl4VRqDgS5eWvyi4ibBpe0Qy2tVNwxNwaxl-jqbyj7sGi3ap8Q9mSr2V4kw-M0ljc9b1OSPMwN-yct4jZzt1uY5RjQA9SMOBpIAqwVN9z_y5sw6E0CPZS9OiF-e6eQPNeExySmgwOgo71y4J1cila0kpA8U8tQYV_zZApgqPlXoGU_u7zsESfoR8KiD1nH5XL9ffCN7TFsYT6zow48hC_yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=qi-XzkFaWo1dIgRJSopz5AP2HdIGIZY3yhPx9w8r2opOlmIjzSAp4i_U_Sj7gMR9f3gU84iQ_Pfb2tT3ihUwuv9ZSJ8pITjkrL19NDC361LMW__CFQXQX8LOD0qBfR2Cl4VRqDgS5eWvyi4ibBpe0Qy2tVNwxNwaxl-jqbyj7sGi3ap8Q9mSr2V4kw-M0ljc9b1OSPMwN-yct4jZzt1uY5RjQA9SMOBpIAqwVN9z_y5sw6E0CPZS9OiF-e6eQPNeExySmgwOgo71y4J1cila0kpA8U8tQYV_zZApgqPlXoGU_u7zsESfoR8KiD1nH5XL9ffCN7TFsYT6zow48hC_yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
علیرضا بیرانوند: اصلا دنبال معافیت پزشکی نیستم/ دوست ندارم به خاطر پرونده سربازی من، نظام‌وظیفه روی خیلی از بازیکنان دارای معافیت پزشکی لیگ زوم کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107461" target="_blank">📅 00:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
💵
⚪️
🔵
افشاگری عادل فردوسی‌پور از ماجرای پول گرفتن ۷۵۰ هزار دلاری فدراسیون از باشگاه استقلال، قبل از اردوی ترکیه تیم ملی بزرگسالان؛ نامه شریعتمداری به تاج برای برگرداندن پول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107460" target="_blank">📅 00:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/373e4ffb08.mp4?token=JyR1beeVndbI_-kjv5xsuoN9j7vRWeY1vqha2NqT_7DM8spvOOrcpsXH435wDqMdutSzA8rHJRA739vwnOO_yrpoCx5eD4QWo-qVMWBYjjp3U_lBfYo_zXJ_QdZPTOTEFGW8ikBG9fISXFB4ZSCJXKkDcmUeisE6l_e8lV_kHgGu7ol5LujTpI822mT9wnyun2u1LOgArEt3kkAAbzUVf6OrdPaScJdCvqPLrYuad4ESGi3bbMLw4M3wYFJQApwkJsHdlpeED7GzCXZ3Kzsv02OpOW6nF8LTV9h9N6JLZPiz017t1fh639HMwCbljtdKQUj0h2GsSSNJAD3h44XJNTgOOwbP0blprvxw4th9XLHawh95RElu3TNEqij-Jz3sS2okmj0xFTTMee4ygdpNEs49nw2i907im01GFS1p08X2Nhne9SIXz64474lpGXJdygXPUKfMfvkQabiNmzBmgV71_66BAImEU0nXpuHekBEoQkf7mglAgGtmvdoMdngEaT3tAtRlGAtq3ub-l72kfHkgxPLB-fUm7neWtA0LjIPA2CbslE6MyKDpPvLx-BT93UwfNnOwaq4m3GlLBzT7_bkOXSN0CP0vJkphR5qlqT1i9qfbWrJHrB3RdFA5jAB3N0tM1gS-XvbWWw0X57ws-8gOrYL-34IvHb99amot94U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/373e4ffb08.mp4?token=JyR1beeVndbI_-kjv5xsuoN9j7vRWeY1vqha2NqT_7DM8spvOOrcpsXH435wDqMdutSzA8rHJRA739vwnOO_yrpoCx5eD4QWo-qVMWBYjjp3U_lBfYo_zXJ_QdZPTOTEFGW8ikBG9fISXFB4ZSCJXKkDcmUeisE6l_e8lV_kHgGu7ol5LujTpI822mT9wnyun2u1LOgArEt3kkAAbzUVf6OrdPaScJdCvqPLrYuad4ESGi3bbMLw4M3wYFJQApwkJsHdlpeED7GzCXZ3Kzsv02OpOW6nF8LTV9h9N6JLZPiz017t1fh639HMwCbljtdKQUj0h2GsSSNJAD3h44XJNTgOOwbP0blprvxw4th9XLHawh95RElu3TNEqij-Jz3sS2okmj0xFTTMee4ygdpNEs49nw2i907im01GFS1p08X2Nhne9SIXz64474lpGXJdygXPUKfMfvkQabiNmzBmgV71_66BAImEU0nXpuHekBEoQkf7mglAgGtmvdoMdngEaT3tAtRlGAtq3ub-l72kfHkgxPLB-fUm7neWtA0LjIPA2CbslE6MyKDpPvLx-BT93UwfNnOwaq4m3GlLBzT7_bkOXSN0CP0vJkphR5qlqT1i9qfbWrJHrB3RdFA5jAB3N0tM1gS-XvbWWw0X57ws-8gOrYL-34IvHb99amot94U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
توضیحات میثاقی درباره شکایت اندونگ و کاریله از باشگاه استقلال
⚪️
محمدحسین میثاقی: در این هلدینگ خلیج فارس یک نفر نیست بپرسد که اندونگ کجاست؟ چه کسی قرارداد کاریله را امضا کرد؟ آقای تاجرنیا الان وقت آن است که مطب و آپارتمان خودت را بفروشی تا سهم خودت از این اشتباه را پرداخت کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107459" target="_blank">📅 00:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed66f5dc3.mp4?token=gJ0miOKho-ZMDCohGx8tTvYBXJYePpa52Xhynr09vr_fatdIvf5bfpR78XpJJRExQ1S2u6pRG8oAQtz2gaM2IwYBXeveVYDikpCUyYrfonYzSQm0KezhsWwtW60LZOfKaqijtByGHjsQ4twaQqcSSwq3IkPuLkKF843qn15ZTDFu5ddwZRH6amZmd5sAoNM-MwF-tYEbtGoeqk61KgsnHwNPOnF4XdiDIS5U7DKlOWlJtW1p27doIqN0eK_Nfp4xcvves6U4FmL4pbBJ6zC2OmREro2MzKy9fCX6z5jlG2B-SLWia8tZfffMlQTKCnqlnGsZKamQNSTj6VmbtrqWwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed66f5dc3.mp4?token=gJ0miOKho-ZMDCohGx8tTvYBXJYePpa52Xhynr09vr_fatdIvf5bfpR78XpJJRExQ1S2u6pRG8oAQtz2gaM2IwYBXeveVYDikpCUyYrfonYzSQm0KezhsWwtW60LZOfKaqijtByGHjsQ4twaQqcSSwq3IkPuLkKF843qn15ZTDFu5ddwZRH6amZmd5sAoNM-MwF-tYEbtGoeqk61KgsnHwNPOnF4XdiDIS5U7DKlOWlJtW1p27doIqN0eK_Nfp4xcvves6U4FmL4pbBJ6zC2OmREro2MzKy9fCX6z5jlG2B-SLWia8tZfffMlQTKCnqlnGsZKamQNSTj6VmbtrqWwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
⚽️
خوشحالی فوق‌العاده زیدان پس از گل پیروزی بخش فرانسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107458" target="_blank">📅 00:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=hKB4VsInPL9AjWxC7iFvPOLGx6hFAkx7ABBgvZhbut381UCFlQ0eRefPnQ3r0oBKlHM2MuOnPbrb5tj-3bYTR5qvffs4x5aNSrxoVy70k6kJ8Oyz8nEBASp4lqIgg_eyfBhLxL1Xs2D2RdHgYYaYnnswXz-dbJTDMbyrhiFpr6XO-46LJKtoYH8maGd0ZZk-XOaXNJf5ChzmFCHFmFE_P2BQGFO-hfKcXtQM8NqSPOiV7_xdHP1D8dppZ-NTFPbb5I5ieheUUOkPMbDW8xYaXnh7WpIQHNYSn5_nyXFz4Z0c8ASkimLxfx4-qSZErjkjkfdOuJ2LnVa1HVhoF68I4lNXeT-hEbdjHOkRNZIWRyODms11yT-rHtO6qstXjOb99Nnd9nDyOyaj2O-CyIj5sTAdXyq6Tj3SVJtPsSPIZWIrXVK8acr9VQ3dT-QwjPFtN5b966I6UIBvardx3um2geTEUOWR5HP7ehgmJ0RDr_JpKswZUp860bF2MoXOhpWpDRd2mb3cvofjEACgVNgSaGs21CYVG6HkN5Sx3sppaLphJvWPE0OxaNysyuoqe5DcbMssb_1bRc077Los0xaeh6g9q6Y3HliVC0Z1aJ1-tQ52RQNHrYPpsvhp9bB4vmvGcuao9ay76HYjqdJ9elgXpeWzBnvZZ1SR-UjgHyvh4dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=hKB4VsInPL9AjWxC7iFvPOLGx6hFAkx7ABBgvZhbut381UCFlQ0eRefPnQ3r0oBKlHM2MuOnPbrb5tj-3bYTR5qvffs4x5aNSrxoVy70k6kJ8Oyz8nEBASp4lqIgg_eyfBhLxL1Xs2D2RdHgYYaYnnswXz-dbJTDMbyrhiFpr6XO-46LJKtoYH8maGd0ZZk-XOaXNJf5ChzmFCHFmFE_P2BQGFO-hfKcXtQM8NqSPOiV7_xdHP1D8dppZ-NTFPbb5I5ieheUUOkPMbDW8xYaXnh7WpIQHNYSn5_nyXFz4Z0c8ASkimLxfx4-qSZErjkjkfdOuJ2LnVa1HVhoF68I4lNXeT-hEbdjHOkRNZIWRyODms11yT-rHtO6qstXjOb99Nnd9nDyOyaj2O-CyIj5sTAdXyq6Tj3SVJtPsSPIZWIrXVK8acr9VQ3dT-QwjPFtN5b966I6UIBvardx3um2geTEUOWR5HP7ehgmJ0RDr_JpKswZUp860bF2MoXOhpWpDRd2mb3cvofjEACgVNgSaGs21CYVG6HkN5Sx3sppaLphJvWPE0OxaNysyuoqe5DcbMssb_1bRc077Los0xaeh6g9q6Y3HliVC0Z1aJ1-tQ52RQNHrYPpsvhp9bB4vmvGcuao9ay76HYjqdJ9elgXpeWzBnvZZ1SR-UjgHyvh4dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
افشاگری
باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
محمد
حسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت شکایت کرده است
در همین راستا این ایجنت قرار شده است مدارکی به پرسپولیس درباره فسخ آسانی بدهد و همچنین این بازیکن به پرسپولیس ملحق شود و مذاکرات حتی تا پیش قرارداد هم جلو رفته بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107457" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b959785a.mp4?token=gdqEr6eGmy80kXMEV7dCulUNaRSfNgAPSVGp3dVcdIZHc8e5GX_DmF2MbL_3lWJYSLknwgSC2ROq4p-hkK_DcwuuHHlPNdY4OauZv2l0pkvC8uSwv_CHa8UzXcgDyMQYrYGUtfSHoeqzsNXyPZbqO7RmoJzsya_BCS3HGhmJQpPIoNAmsAz4CQ0gS69yohRFl0xnmMjruikZ0nmsiRdx67ZXVhzwBJeY4dlnqaqyxXhgeuwsrvXeK3ywocYc0m74oHskyvnnJDLZBwMiBlkg2-tD97_ywcVxodvf5xy1g7Z_nMIdbmvoTAWpaN-rehBhoa5ooYdkOsFSeb4t5z9ZFz513v9QcsddX34ZM6NIizknjoaQOfSVtBc265FnPRmTQF14EhKU47_RubXyFSlDeAFjpqZV8QQBPhvylNRtf-cNr-jGvkBSMhcYT5KTTN6OjL1mjoQe0WalZR-HqBsZmg6UYWMz4WHgHOYSsuG4DbKVp8xgD7aGaVjHvAIuq4R8vRyG6c3L2EZjZSpx5qTu7uJqzKBgTw4sVopZeNpFncMGtuKwlQZXxSnY73pwK9X1ylydmyZx9MM2LQumhHq5Tb_6G8grL1UenhQcrrx8MvMIbi49HkIR9WNyjQedR1_A5sG_evjtxM83fAlPzkZLgNEq9oBvO7vTNF4y9bUMrxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b959785a.mp4?token=gdqEr6eGmy80kXMEV7dCulUNaRSfNgAPSVGp3dVcdIZHc8e5GX_DmF2MbL_3lWJYSLknwgSC2ROq4p-hkK_DcwuuHHlPNdY4OauZv2l0pkvC8uSwv_CHa8UzXcgDyMQYrYGUtfSHoeqzsNXyPZbqO7RmoJzsya_BCS3HGhmJQpPIoNAmsAz4CQ0gS69yohRFl0xnmMjruikZ0nmsiRdx67ZXVhzwBJeY4dlnqaqyxXhgeuwsrvXeK3ywocYc0m74oHskyvnnJDLZBwMiBlkg2-tD97_ywcVxodvf5xy1g7Z_nMIdbmvoTAWpaN-rehBhoa5ooYdkOsFSeb4t5z9ZFz513v9QcsddX34ZM6NIizknjoaQOfSVtBc265FnPRmTQF14EhKU47_RubXyFSlDeAFjpqZV8QQBPhvylNRtf-cNr-jGvkBSMhcYT5KTTN6OjL1mjoQe0WalZR-HqBsZmg6UYWMz4WHgHOYSsuG4DbKVp8xgD7aGaVjHvAIuq4R8vRyG6c3L2EZjZSpx5qTu7uJqzKBgTw4sVopZeNpFncMGtuKwlQZXxSnY73pwK9X1ylydmyZx9MM2LQumhHq5Tb_6G8grL1UenhQcrrx8MvMIbi49HkIR9WNyjQedR1_A5sG_evjtxM83fAlPzkZLgNEq9oBvO7vTNF4y9bUMrxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
گل‌تماشایی مایکل‌اولیسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107456" target="_blank">📅 00:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba31d6094.mp4?token=voCJq5mh83FVfUMl5zgq48vCJorUxlVN_S0uhfsSs4nTgcHhGdne7C8Naspd0ggS9WMcHeteNfvPI1EFaEv7LoF3vjkfKFgOaw-NOeSU3t--smqhlxnjUDqUC8X3ZrLr06WTA8l5hz6SMQckld0dWpeD7PDY1SlOzosiybxDecPM319kl9qfg-zx2kg72ek2528shukO7RdsVdOPoQ0WM0OjnFE4ZYcLifx0_AcatmfpbNNWD7U-bE5m-ynA_Oz1LjRW8mlzF9r81EVsTMKGG4usG12f630a3bxaDqnKkOZKN4Ib1UazpQnNgMRSGJMbNsitajLZdpVNIlkYbcLCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba31d6094.mp4?token=voCJq5mh83FVfUMl5zgq48vCJorUxlVN_S0uhfsSs4nTgcHhGdne7C8Naspd0ggS9WMcHeteNfvPI1EFaEv7LoF3vjkfKFgOaw-NOeSU3t--smqhlxnjUDqUC8X3ZrLr06WTA8l5hz6SMQckld0dWpeD7PDY1SlOzosiybxDecPM319kl9qfg-zx2kg72ek2528shukO7RdsVdOPoQ0WM0OjnFE4ZYcLifx0_AcatmfpbNNWD7U-bE5m-ynA_Oz1LjRW8mlzF9r81EVsTMKGG4usG12f630a3bxaDqnKkOZKN4Ib1UazpQnNgMRSGJMbNsitajLZdpVNIlkYbcLCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
امیرمهدی ژوله جایگزین ابوطالب حسینی شد و برنامه فان فوتبال 360 رو اجرا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107455" target="_blank">📅 00:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beb68432a.mp4?token=ScJKa7NqKJ-1dhkW44cvtM_UeD2HsAeoQD0mgiiSTxsMDXhfj-ihZ41iMw1teJAQ2YM2DNUq2N-K_GdqvloEhpjtt8gbWbTV13h3yqm0PApeQWEFt-gMYyt47Dp4sYb0s8nyEQJEew8tnnFthL3ijdJHVX-p4PJCKmeZei6K7LIUF9KkISd5vMTX7U3i72mlH2fvnHCQB2lmiKCM28b1aNuQenqJGwhvTY1yyTTdKtwsfna1ybfuQQgMO-z3eJiogwmAO-MdtJd2ImEBewy2teoKSdPwMOyG97XNhzx1laPsbST8oNHchy02JToRuZ91NkDPnb0r9ZP-ucT_vmacUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beb68432a.mp4?token=ScJKa7NqKJ-1dhkW44cvtM_UeD2HsAeoQD0mgiiSTxsMDXhfj-ihZ41iMw1teJAQ2YM2DNUq2N-K_GdqvloEhpjtt8gbWbTV13h3yqm0PApeQWEFt-gMYyt47Dp4sYb0s8nyEQJEew8tnnFthL3ijdJHVX-p4PJCKmeZei6K7LIUF9KkISd5vMTX7U3i72mlH2fvnHCQB2lmiKCM28b1aNuQenqJGwhvTY1yyTTdKtwsfna1ybfuQQgMO-z3eJiogwmAO-MdtJd2ImEBewy2teoKSdPwMOyG97XNhzx1laPsbST8oNHchy02JToRuZ91NkDPnb0r9ZP-ucT_vmacUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
سوتی سمی عادل فردوسی‌پور و ریختن لیوان آب روی میز که با خنده‌های آسانی همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107454" target="_blank">📅 23:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5937fb4be6.mp4?token=lQrQgt2xBNohv1-70IEorHo7WCd4YGbVUnE6pz5PTrXa86kE6bahZjzBPV7SdkaH5cNZIGwhYjM0lGvy1kUIicV1zgyDBa4dFgH9j6V3TFewCdtGB6Ln15WIzQEdFED9jR3ys4t6nMW_i00kSxi5LbEscOtxIUEhNFXaMGbWXkDkgf2w_A3V_GIMURMCdClbzTIbEBVKJSuImNTvWEcjxXtWTTCHgHvVmEZN3fVhB9-4LTN86omQzAh9sqHeYqDbP4FXXgNiS_lHnCc-zT6DBI6zHSPRO84hw6YdfKRjHKKQC_HLTsDDvRpaAuteGtSIDytnFgQX7gWjdHVnVsezRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5937fb4be6.mp4?token=lQrQgt2xBNohv1-70IEorHo7WCd4YGbVUnE6pz5PTrXa86kE6bahZjzBPV7SdkaH5cNZIGwhYjM0lGvy1kUIicV1zgyDBa4dFgH9j6V3TFewCdtGB6Ln15WIzQEdFED9jR3ys4t6nMW_i00kSxi5LbEscOtxIUEhNFXaMGbWXkDkgf2w_A3V_GIMURMCdClbzTIbEBVKJSuImNTvWEcjxXtWTTCHgHvVmEZN3fVhB9-4LTN86omQzAh9sqHeYqDbP4FXXgNiS_lHnCc-zT6DBI6zHSPRO84hw6YdfKRjHKKQC_HLTsDDvRpaAuteGtSIDytnFgQX7gWjdHVnVsezRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سردار آزمون: دیروز به زنوزی زنگ زدم و گفتم یه وقت نکند من را گردن نگیری/ انتخابم برای بازی در ایران تراکتور است مگر اینکه خودشان نخواهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107453" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07eddda0fb.mp4?token=fZ98jVBvHkRjc6-cGgbUyanx2HxhKwoyLWG3w51E0-M7PvrAh2PRrAK5pa0ZxsmpmE2P4e0roT2471XdClRuRGFcXmuv0Sju5elE2zVNmqJIJdBw8hxBOYLVIihYBt_vGwFNE_w3yGNiu_-D_0wXyosyCfOui3bf1C3-EhvAa4Ik45XKfso5mX7nzZ5QNLf4YMxDFZ96f3z0Oj48zKKHnuxg88OmkZLWYozPGQAyuBguXjbSxArp45hYlP3h2si9CWTVON4nxN6A-MPoIoOGX0c9V4PpIrCt6QG5z6youuRY59lO7Qxc8CHv6WUyg6iPIsf26SnO9OwZ7Tz9zRyelg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07eddda0fb.mp4?token=fZ98jVBvHkRjc6-cGgbUyanx2HxhKwoyLWG3w51E0-M7PvrAh2PRrAK5pa0ZxsmpmE2P4e0roT2471XdClRuRGFcXmuv0Sju5elE2zVNmqJIJdBw8hxBOYLVIihYBt_vGwFNE_w3yGNiu_-D_0wXyosyCfOui3bf1C3-EhvAa4Ik45XKfso5mX7nzZ5QNLf4YMxDFZ96f3z0Oj48zKKHnuxg88OmkZLWYozPGQAyuBguXjbSxArp45hYlP3h2si9CWTVON4nxN6A-MPoIoOGX0c9V4PpIrCt6QG5z6youuRY59lO7Qxc8CHv6WUyg6iPIsf26SnO9OwZ7Tz9zRyelg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های سردار آزمون با بیرانوند درمورد رنگ مو و سربازی‌اش
🟠
همسر بیرانوند باز برایش حنا گذاشته ولی اصلا بهش نمیاد. یکی اکرم خانم (همسرش) و یکی اکرم عفیف او را در زندگی بدبخت کرده‌اند!
🟠
خدا کند علی در فجر مویش را نزند...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107452" target="_blank">📅 23:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
جنس متفاوت غافلگیرکردن یاسر آسانی!
👍
🇮🇷
خوش‌قلب و خیرخواه، مثل ستاره آلبانیایی استقلال؛ وقتی یاسر تصمیم گرفت برای اعضای نیازمند باشگاه، موتور و خانه تهیه کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107451" target="_blank">📅 22:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
از ختافه، ژاپن و عربستان پیشنهاد داشتم
🇮🇷
واکنش آسانی به پیشنهادهایی که بعد از فصل اولش در جمع استقلالی‌ها دریافت کرد؛ بهشان گفتم فقط وقتی پیشنهاد استقلال آمد به من زنگ بزنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107450" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
درباره رامین با ساپینتو حرف زدم؛ گفت برش می‌گردونم!
صحبت‌های یاسر آسانی درباره رابطه‌اش با رضاییان، اتفاقات جنجالی بعد از بازی با الوصل و پادرمیانی بین او و سرمربی سابق!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107449" target="_blank">📅 22:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎙
🇮🇷
توضیح آسانی درباره تکنیک‌های کری خواندن، از بازی مقابل پادیاب تا داربی برابر پرسپولیس!/ در استقلال، از تمام لحظات لذت می‌برم و خیلی خوشحالم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107448" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133f025096.mp4?token=dKhVKAsScB6nkDsHVhA-0YONqKPpdLNpOaYhkLo2UU15CpzyDfUxR09qwtYM8jbTgCRI8WIVuN104sowZllOfpQvXjn0jJPm_EeHuvYBUuQ7TnF1qnGq_Wgh90NCYsM5kBKycNKUGpMoxzEg4mbMgb4zPm0xXyeycSLyjKw0r5kEGelO94rQJsVNyLTegCv9JjzfPqbXeKIiFr91ugrhsOSOtIODh6FZAPKTiJh8O4D5J5ZbPNqOzLcHGF8bVaZKZHs6TbkrGbAAzULV-LDdQTKGYS6qiFaYZLJC6Zl9TuHVIzZxSn0gjsCo0O6sCb783yOZzOlVQTovU8HrCyoGN4QxXWSGFTgcwwgwd0A8w3km1t_sBeslGwAKAim5UFgXYaupcrLwcb2uMOqP1M2jQVQc6Zi0wQ_IRlpA-2_Ygoc8T_MXIZTEU_DDRB0kP8VNaX3m2T2kbSGW-DNxbLQwwi7UfAnvRZy8_sDy_RkOCJbolH9AC5eX3R_My6Mj1w2MXWEJM6boiFp6JvYzJihRtkb2Lsb9QvlmZZ7VCEhe_VTDXnq2vBm2Y_LIiP8AVbwXZYMLv360SclT6619UrceX0SP3t8jg81imRygE-Gm0Fl3sIWHtX9auuAjRjP0Uxz-5iPUzpOANHaHBm4TE3IfLdcUsRBTpPa7vb_GGGUz-UU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133f025096.mp4?token=dKhVKAsScB6nkDsHVhA-0YONqKPpdLNpOaYhkLo2UU15CpzyDfUxR09qwtYM8jbTgCRI8WIVuN104sowZllOfpQvXjn0jJPm_EeHuvYBUuQ7TnF1qnGq_Wgh90NCYsM5kBKycNKUGpMoxzEg4mbMgb4zPm0xXyeycSLyjKw0r5kEGelO94rQJsVNyLTegCv9JjzfPqbXeKIiFr91ugrhsOSOtIODh6FZAPKTiJh8O4D5J5ZbPNqOzLcHGF8bVaZKZHs6TbkrGbAAzULV-LDdQTKGYS6qiFaYZLJC6Zl9TuHVIzZxSn0gjsCo0O6sCb783yOZzOlVQTovU8HrCyoGN4QxXWSGFTgcwwgwd0A8w3km1t_sBeslGwAKAim5UFgXYaupcrLwcb2uMOqP1M2jQVQc6Zi0wQ_IRlpA-2_Ygoc8T_MXIZTEU_DDRB0kP8VNaX3m2T2kbSGW-DNxbLQwwi7UfAnvRZy8_sDy_RkOCJbolH9AC5eX3R_My6Mj1w2MXWEJM6boiFp6JvYzJihRtkb2Lsb9QvlmZZ7VCEhe_VTDXnq2vBm2Y_LIiP8AVbwXZYMLv360SclT6619UrceX0SP3t8jg81imRygE-Gm0Fl3sIWHtX9auuAjRjP0Uxz-5iPUzpOANHaHBm4TE3IfLdcUsRBTpPa7vb_GGGUz-UU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
گفت‌‌وگو با یاسر آسانی، درباره واکنش عجیبش به دعوت‌نشدن به تیم ملی آلبانی: حالا می‌توانم برای استقلال بهترین بازی‌هایم را انجام دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107447" target="_blank">📅 22:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d5953f9f.mp4?token=FKGezzYK_Jx_E1IsqE1k-FpXWxs1nIEs9W9NUTG2YNjuV3xAcw38iqbKT5DIUDu-GZUx1Fmbrj9I0984vI3gJBKN14HMqNi893h4sBtuusosUxJKFQXrYXu0lUk06WzosPDdUO44U-fHL-LqnKsZR1ytgd7Aw2OXkb9Tx9rbwfF6weKm54mGj5kRUtLeZO12auJr10mvFrF9XNIK3i8x7w3aHueRFestgidVBZjRAf7wC0SWLLE-CbnJ8OGKY4rNIiQsx5ZejmDSpJiO0-7_ObTtbAplcezKwrKvhRfyOe007yawPwJJlWcBN5uv1yaYaWFBLOU1hwlVFOSHlO6w4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d5953f9f.mp4?token=FKGezzYK_Jx_E1IsqE1k-FpXWxs1nIEs9W9NUTG2YNjuV3xAcw38iqbKT5DIUDu-GZUx1Fmbrj9I0984vI3gJBKN14HMqNi893h4sBtuusosUxJKFQXrYXu0lUk06WzosPDdUO44U-fHL-LqnKsZR1ytgd7Aw2OXkb9Tx9rbwfF6weKm54mGj5kRUtLeZO12auJr10mvFrF9XNIK3i8x7w3aHueRFestgidVBZjRAf7wC0SWLLE-CbnJ8OGKY4rNIiQsx5ZejmDSpJiO0-7_ObTtbAplcezKwrKvhRfyOe007yawPwJJlWcBN5uv1yaYaWFBLOU1hwlVFOSHlO6w4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
حسین‌
عبدی: رفتن به المپیک ربطی به سرمربی ندارد!
‼️
خیابانی: پس گواردیولا هم بیاید همین است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107446" target="_blank">📅 21:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEaHoM4ZI7wXQtWGFl5RHRBzDgwnDNjndc2s-zQRvfa-NQCFhow_IwMM_L0DfwS7KPMynHTk805JASVK3ImZ35aMoa4A21Xbr-XZeTfjx58kvZbLhz4NYfvBriZClO7tWFGxTr8pO1hGkVH79axqXXB_WX6NX6qB3zZFq5WAwGyxXZIGCJDdHhurHBXdYIs-7jFhTlvNEAA_DIxgmpp3Lj4y-rFa6Gcrfr9qt_o2VywsBNCElwr1lyAKValxh2x42UrLBX4MVU1L6XvmdV9woJWlOb51Fcxg_8Z80Gry6KijKG2YNjjvcrHBsfbib1NnOXt93Jr6zgxJ5Zq79-dn3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
یاسر‌آسانی تا دقایقی‌دیگر با حضور در برنامه عادل فردوسی‌پور با وی مصاحبه خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107445" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794b34067.mp4?token=mILlzsBzoRqYSU_aBQrFTCbOm1xeg2BkCl0OTsO9jfDtV2LQDBBcKqujmi4osQoH5FRg-F1IFM4HDmtHRBoUKYjKUwk6ByFxWviQhpeJdwM5TdiflsuIdWEYfEGQoHB2A3eolB8_-MyZ9OnNMx1z7OrsDOjZxar6WTHCWHLi-ke6lcWI-aHBgQblBRRT6v4nSb_4HELV_Pec1rwbUqbn04k0eDaGOJ1pWONE35eNYoMUgZ6t1XG1FRlZpGqWglENTIqt_sdolHH6XXUx69hYE2F92p_AAI-l3Nnt9CNz_-doIzBy8-LSlxhvaPtcl0yixXIiFQKvSS0G1F54CMHJXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794b34067.mp4?token=mILlzsBzoRqYSU_aBQrFTCbOm1xeg2BkCl0OTsO9jfDtV2LQDBBcKqujmi4osQoH5FRg-F1IFM4HDmtHRBoUKYjKUwk6ByFxWviQhpeJdwM5TdiflsuIdWEYfEGQoHB2A3eolB8_-MyZ9OnNMx1z7OrsDOjZxar6WTHCWHLi-ke6lcWI-aHBgQblBRRT6v4nSb_4HELV_Pec1rwbUqbn04k0eDaGOJ1pWONE35eNYoMUgZ6t1XG1FRlZpGqWglENTIqt_sdolHH6XXUx69hYE2F92p_AAI-l3Nnt9CNz_-doIzBy8-LSlxhvaPtcl0yixXIiFQKvSS0G1F54CMHJXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
مطابق گزارش خبرنگار شبکه الحدث در پاکستان، به گفته منابع، ایران با توقف فعالیت‌های غنی‌سازی موافقت کرده است، در ازای آن، تحریم‌های ایالات متحده علیه ایران کاهش خواهد یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107444" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107442">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VV-weBQ4y6oj-LpsXA-TNKj3hssMxi8A_ItzNtMOMhWoPznpfV8pNgXuHgrQm9jKeBVZjSZ1mW0ohXonyvreP91PY0X3u0UqrKxW6J1W5HPsxNq_HxMkZXlWSrITzLKe8cs16odpe8notrSDHPh7fa-5BXoijSAjZXBmb2nfmp2QSflhKSWbcDeOR5Li_EpMZSBvjAJPR1TKjWd-wsmGaqmMePu9ZLdxBdh4n5KD6PX5rXihcgnWECP5in4mzLuY-E6VKmxcu-s63bPg4xf0k0N2gXquIuHB5EyVkkqlVnye8HhNQUsbHYZmBsl7sMscdu9Lxv6X2PeZIRD1x2QlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AlxUKIrHlnnIKA9hSCOQSLpWaV1ATi6ArJEGps6nwCFYVyTPTmNqiHQ8XwwV24F7HbYzDnb0LsrEPj0M4Jd60CJLjj_5BfyKiF_9WNx3fLpgwBtN3OB61KekzPZwDhtaM-PyFVvky80laWEFbrG3Dtrf1Xt7Xh8MkDXmAWCEyvnyPrJ7quqG7zdgP6To-nkjyH89Hj-gX4fbRvDT6SaJ1vXTwIRtswOSYUpYmVIWhJAs9bdLzMTB1Qjw0_R_clRXPmWN5xparU3sKr_7CaWFFflrnGASZ1RHZ5C-hr4XmLTjYqzJEdDM_RzWJl869I1I_Dih8Q7OtzrSMaa4a9qZaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇧🇪
ترکیب‌تیم‌های بلژیک x فرانسه
ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107442" target="_blank">📅 21:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107441">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا : از هواداران پرسپولیس گله دارم و ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107441" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107440">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=SN9J6TCNhpJSrAB73qYoWlB1uZVzkMC9eBLdrxPLhP8_Tw74wQJNdwZ4QUHv3_UcFi1z_CNSEY7pOFARqhuzDhNGuMxZ18veuWJfQsDsuzjjEc7_E9JKQUWFpJ6Aq4BmFIDiASZbITa4tnDlbyF7N00_7BCarv-SDsw6POVidkfxC75SRq9B92saCDpeEPFM9GAX-0P9qnOobsMmCokrMnEpCAm2NgrQ45VW8WRpWfvtY04ot4qyNtUh6UeT6D9yLai-v_6k3_DUqQHYH2LpnsADXa5nH8x1e9_WtOpaJ0hrqQhHr3DpL1MadRJ75Y30RaKvV_J74qwx6hJCPDYaOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=SN9J6TCNhpJSrAB73qYoWlB1uZVzkMC9eBLdrxPLhP8_Tw74wQJNdwZ4QUHv3_UcFi1z_CNSEY7pOFARqhuzDhNGuMxZ18veuWJfQsDsuzjjEc7_E9JKQUWFpJ6Aq4BmFIDiASZbITa4tnDlbyF7N00_7BCarv-SDsw6POVidkfxC75SRq9B92saCDpeEPFM9GAX-0P9qnOobsMmCokrMnEpCAm2NgrQ45VW8WRpWfvtY04ot4qyNtUh6UeT6D9yLai-v_6k3_DUqQHYH2LpnsADXa5nH8x1e9_WtOpaJ0hrqQhHr3DpL1MadRJ75Y30RaKvV_J74qwx6hJCPDYaOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
کنایه مجری تلویزیون به زنوزی: باید از هواداران استقلال عذرخواهی کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107440" target="_blank">📅 20:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd102e93c.mp4?token=d58qZ7AyqQkwTvOhHMfXbposckIZgVJOa3phaJHhn7acnQwh9KFAADYd88avsFANYd-WCdJl4geH4Gz7pwmCCuyGJ-bkAQ7zWiCeR4vPSs2Cxnhr284XJShQP0NN5Ruxwkjdgqqfu2x7e2T3k-kWU5H7sSFCQdtt6aMXmQWjzrU-Ql3enwAkWxtJ0OtKSBRcEyFmaoiGPCkLeESjAhPjx6JWDcxMlJMGJBSsgZjkz96w7ReZduIGmGkTWepT3L_agP3De5-bAqc4p3RpGV20FbIKVmoY1wZIB8fLidwSJEi2VgIK2DoySYc2ETYo3Yu4HGpS1cBaKKNvXqSe-Vm3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd102e93c.mp4?token=d58qZ7AyqQkwTvOhHMfXbposckIZgVJOa3phaJHhn7acnQwh9KFAADYd88avsFANYd-WCdJl4geH4Gz7pwmCCuyGJ-bkAQ7zWiCeR4vPSs2Cxnhr284XJShQP0NN5Ruxwkjdgqqfu2x7e2T3k-kWU5H7sSFCQdtt6aMXmQWjzrU-Ql3enwAkWxtJ0OtKSBRcEyFmaoiGPCkLeESjAhPjx6JWDcxMlJMGJBSsgZjkz96w7ReZduIGmGkTWepT3L_agP3De5-bAqc4p3RpGV20FbIKVmoY1wZIB8fLidwSJEi2VgIK2DoySYc2ETYo3Yu4HGpS1cBaKKNvXqSe-Vm3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
یامال دیوث اومده از عرق زیر بغل نیکو ویلیامز استوری گرفته و مسخرش میکنه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107439" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107438">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee7cdbb4e.mp4?token=vm5XRBNiJFBydEayR7XJtRxvWm_w24nCxFdlxSSzXCdBFMwzA2_jxwhDLbnkrUGdIImVyp8uXqtGCOclwTOZPBEv0D3CUtRmLxW-XRElWksjaF32fniY55ureotkXCoM28XIzVIhJEC9IbX_PKyOMe-DuZ4STKjDmg0rNCX6GeBq_PUJxEVqXUdym3gfLxlU8xHx5CZOZ7xFzEOGjFPELpp1tNOkD1zAJAj0Mzkhpk5PXXdY-R47oc5EprEPN02ricj_xbmDAuLFQf5CblGEPeEWLreYMDPWh9y7Oww2QEu4HTbOU4KZhL4q2DzuUT4PwxI3v2NGxJiXRv48PXy1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee7cdbb4e.mp4?token=vm5XRBNiJFBydEayR7XJtRxvWm_w24nCxFdlxSSzXCdBFMwzA2_jxwhDLbnkrUGdIImVyp8uXqtGCOclwTOZPBEv0D3CUtRmLxW-XRElWksjaF32fniY55ureotkXCoM28XIzVIhJEC9IbX_PKyOMe-DuZ4STKjDmg0rNCX6GeBq_PUJxEVqXUdym3gfLxlU8xHx5CZOZ7xFzEOGjFPELpp1tNOkD1zAJAj0Mzkhpk5PXXdY-R47oc5EprEPN02ricj_xbmDAuLFQf5CblGEPeEWLreYMDPWh9y7Oww2QEu4HTbOU4KZhL4q2DzuUT4PwxI3v2NGxJiXRv48PXy1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇮🇷
❌
فرزین دبیری عضو هیات رییسه فدراسیون فوتبال : علی تاجرنیا به اعضای هیات‌رییسه نامه زده که جام فصل گذشته به استقلال اهدا شود اما هنوز هیچ‌چیز قطعی نشده و هیچ کس هم به تاجرنیا قولی نداده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107438" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXZ5sJHEQ89s7dGzehEojxoKF_H5SCy2hPsJ2_4S9Phmti9ig72j7LAlLDHn6-zU2jgWlv7sD3EQhqkT5jUwJOzzgiGF1y94dk40SWiNyFengcqERLm9236y5DGrJ44fSWi2l8b9bnG41Em-gEO1m8ZUEyrNqP9Cd5GW5WF0AhSNcmCi_cEvLRlqDgucW7Dew5TXuxRzLSJ7Rf7L9rfwRVOHXFNrcCXnMS1zRMwgFVgug9j9EN1LazcGTBpiJG3xZXwj9_iW4XsGUcF2C47ov0ZWE21s89Qn2wzKVmvCR0kwlCOH0fSJOW9Ob97D5SI7TEsau-H2Xvv_FvNXD20JtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
افشین‌قطبی، پیروز قربانی و رسول خطیبی سه گزینه نهایی فدراسیون فوتبال برای سرمربیگری تیم‌ملی امید هستند که بزودی یک نفر معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107437" target="_blank">📅 19:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d622742.mp4?token=Mk1Kt35DFPhiGNDVYNYiIk0dYDfQcoRViHed4gFPJw7KME40bxhvketxIUDcHWPj3i5aLSH8FOxTiBIecCW3_co-uvLgyI-hHWbclWXTjHsUPsL-WzYEd_hzKjtkLONpMK6Pb3nlGm6b9FxhDNFKKBajzEZpKgeEwK4c8kz9qRCUDwg_OltcAk6VIMePDjcR6q8IrasuUaNlEbfsizgGVV7l0P2lYjLMnbFqrwt-rt0ApvxLSjS56xnFUWXNAKz1piX15nWIArg4XW7aFLhSQQyt-xWwpC1_fcDNIQObQVnAnsHoAxvmoWogIHybUSBA-ZFyRTO2s8yKxbViKhYUTTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d622742.mp4?token=Mk1Kt35DFPhiGNDVYNYiIk0dYDfQcoRViHed4gFPJw7KME40bxhvketxIUDcHWPj3i5aLSH8FOxTiBIecCW3_co-uvLgyI-hHWbclWXTjHsUPsL-WzYEd_hzKjtkLONpMK6Pb3nlGm6b9FxhDNFKKBajzEZpKgeEwK4c8kz9qRCUDwg_OltcAk6VIMePDjcR6q8IrasuUaNlEbfsizgGVV7l0P2lYjLMnbFqrwt-rt0ApvxLSjS56xnFUWXNAKz1piX15nWIArg4XW7aFLhSQQyt-xWwpC1_fcDNIQObQVnAnsHoAxvmoWogIHybUSBA-ZFyRTO2s8yKxbViKhYUTTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👍
ویدیو‌دیدنی از حرکات بانوی ژیمناستیک ایران در بازی‌های آسیایی که حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107436" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6YteZWiTnuX9onyEF0aKNNDfgUG5TzDkGCul3DGZl0zqTLCGvZfvEdcRzuzOaB5vMOGh3xPSFvSFxFw4XwW7mtKAahG9CyEpA7Mu-vfCnVqmZHsxXTVZu8EX_5XuwpMRoW5qS7J4cI3WkuUFM0Oewz6GtUYUXwZxmEwIXrS1jdy5oFamqBx7aOO9cotwLxo_IwCcWWSvNS5QR7iwktuDcnLXOVtMa2Y9V-GO0kwTm37DElf6pYNvT9JXn2K3Q4HlmLLq3gAd6ZFgau-mhtUWlGcXQghNKB8aUxM8PnXSHDm_h_H554BVeLYoklPKAeTEiTad5i867E7N9QBRNZXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
دوایت باکس، گارد باتجربه آمریکایی، با تیم بسکتبال استقلال پیوست. این بازیکن آمریکای سابقه حضور در NBA تورنتو رپتورز، لس‌آنجلس لیکرز و دیترویت پیستونز را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107435" target="_blank">📅 18:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3874fb3e78.mp4?token=ZmUU48XBVI7vcu9hkOAu3dIppwfeOMF7vmXDdZrWO160eT6WeLjrBYgwWAw-OYJwRgp-qSVbYf8NlBoyixuylYNfEWIWSRq-94AK-DWvgwXGu03GuvsgKUVY_UYw6nXTApR-CejG9AltzLYomt14Y0jDLX7v1n7rTFwA4vTymaZYvBaf92KOluThCwyxP2YAtksZ16CnJViavMOlvhKDIS1mhZAUAg-tbG3y46VAJOGYe6vEhhxpFSP2C92FceCKX4-yFfWfaaIlU-VpyNONXzFia88d17LxjIgO0fDO7tcjkXr_Li12gRsZc1jDekD-EqmVvOX7eMpa6wFu8niAzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3874fb3e78.mp4?token=ZmUU48XBVI7vcu9hkOAu3dIppwfeOMF7vmXDdZrWO160eT6WeLjrBYgwWAw-OYJwRgp-qSVbYf8NlBoyixuylYNfEWIWSRq-94AK-DWvgwXGu03GuvsgKUVY_UYw6nXTApR-CejG9AltzLYomt14Y0jDLX7v1n7rTFwA4vTymaZYvBaf92KOluThCwyxP2YAtksZ16CnJViavMOlvhKDIS1mhZAUAg-tbG3y46VAJOGYe6vEhhxpFSP2C92FceCKX4-yFfWfaaIlU-VpyNONXzFia88d17LxjIgO0fDO7tcjkXr_Li12gRsZc1jDekD-EqmVvOX7eMpa6wFu8niAzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
تاجرنيا: خیلی ها من را سرزنش کردن که چرا موضع علیه سه جانبه نگرفتیم اما در نهایت دیدید که چه افتضاحی برایشان رقم خورد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107434" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvTjdL4RLxJC748aDXURnyIdr-izFIN50CPqcP3zTSew1nOexlE97WtIgy_MjjDsN-EdjNNBIsW0OGqGKBZWVdxj762U2GSX-ox-BRBtDvLxZQ16icDB4gqviYnt_Ck_5L2zXzj2yOVenhJxM5uBlsctbN_cESkoB4fNAEz8CFSFTUMcixpQyWgZuUt_5NrtKDqoMAABuDxnXXfUXYStcD_EgS-NIFea_l6ut6VuNjhcakodFI2hjgUDQGI1dUFQkyFUcWw3kmeUZGCueEEqEIP9djQsLPqHaEidRdcqYwH4nBjnR59ORNR5Edc378HInoiOYO7u0NZ7WmJ8pfKnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد اسپانیا در ۵ بازی اخیر خودش
🔥
🇵🇹
برتری مقابل پرتغال —  رنکینگ 7 فیفا
🇧🇪
برتری مقابل بلژیک —  رنکینگ 8 فیفا
🇫🇷
برتری مقابل فرانسه — رنکینگ 3 فیفا
🇦🇷
برتری مقابل آرژانتین—  رنکینگ 2 فیفا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برتری مقابل انگلیس —  رنکینگ 4 فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107433" target="_blank">📅 17:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107430">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387378bb2a.mp4?token=ANRsNNFnJgrlhTYshsxWaPyvTxrnZHGOfufidzhHudt1ScfvkZRBpyDyKkjW_-MHAaLoGc0vmVa8IWkL7WOAQIfKm9AaoXKhvm-QbxuGYAi1Gdz6_AfOAjeuHpuSuW0vN3n5qaaT5FjY-7rMsXpV0LgA2WowqJ4rCc8mR4VyixArWLEJ5iKsCVRFMlxr5MeyyU-OGwRk3qx8k-5_nmjp7HPj9pPrwrD7pmmaA_0BKn_vI5CbxdGlh6ydYLPPGDfwOrpvOG8R6QXiFDeCQq-QM2lopHagiARjOqwTjqZYfHwP1vaNWtMoSqas5tOKfzlSYy-n9S474RPTgI-IUoIv3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387378bb2a.mp4?token=ANRsNNFnJgrlhTYshsxWaPyvTxrnZHGOfufidzhHudt1ScfvkZRBpyDyKkjW_-MHAaLoGc0vmVa8IWkL7WOAQIfKm9AaoXKhvm-QbxuGYAi1Gdz6_AfOAjeuHpuSuW0vN3n5qaaT5FjY-7rMsXpV0LgA2WowqJ4rCc8mR4VyixArWLEJ5iKsCVRFMlxr5MeyyU-OGwRk3qx8k-5_nmjp7HPj9pPrwrD7pmmaA_0BKn_vI5CbxdGlh6ydYLPPGDfwOrpvOG8R6QXiFDeCQq-QM2lopHagiARjOqwTjqZYfHwP1vaNWtMoSqas5tOKfzlSYy-n9S474RPTgI-IUoIv3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیروزی پرتغال در خانه ی نروژ، در شب نیمکت نشینی رونالدو.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107430" target="_blank">📅 17:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107429">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwhmhwGZCRT2LgEm1T91zjmdErz0gIZxjCjNXBU2RX-Pxh5YXLauV8xdjigXuF82hY6i0AGWeCAZFcStmn01je7xGjx6zNLtre4sK27QNW7C-NB4KqxdCWVmLiPb3q-ucV9179hxsc555aLdrWeGLiu6fafRKwOop0mBZyC0H5wQoWTHCgRHclvOuzUNRZJcUHeagxHPWSfR5-OWffC5g_Iv8-u2kZt6m38xhpUPCQwtWoeaBrNwUTGG7rYB4QPUllZnhJipV4eYSgJ2lmM2k9sBnVFBd-Hz1M3vUiZTLgkhugFpQjuXGS-c4Jwi1l0It82rcWCXiJyW7CnzWaKEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عکس فوق العاده زیبا از برج میلاد و ماه که دیشب گرفته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107429" target="_blank">📅 17:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107428">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302c2a5126.mp4?token=PsUwzc6-K11FRFfqL-g_6WhxfjFhN1F02WNucCdCB0YHxCr5c5sFh1BjSl6gFlk0FrOhZEx2Ayrtxzsu6PWBK5ueSF4BcKce64QcXvbpCOif6dXIylOxBapH2KKOSCKNE8irGsiuN7swLzxs8yh5xEUvoXMPyjouUpqmiML2xwTh6vcs8rEnidooyojdTctUJSEw5KJ5ROpFRT6wam1JRfwfLqRFhBSlyn0Z2j3kspa6nd0vhLtKc9Qs_QA21jpnK7cGbEWcO96WkPxU67rbPUZOW7b4Ao3PfCKEbswla6zuBh2bBfqWCwUtehS7pA_xvR41Hz-5Vjyx7sBqJ5I6_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302c2a5126.mp4?token=PsUwzc6-K11FRFfqL-g_6WhxfjFhN1F02WNucCdCB0YHxCr5c5sFh1BjSl6gFlk0FrOhZEx2Ayrtxzsu6PWBK5ueSF4BcKce64QcXvbpCOif6dXIylOxBapH2KKOSCKNE8irGsiuN7swLzxs8yh5xEUvoXMPyjouUpqmiML2xwTh6vcs8rEnidooyojdTctUJSEw5KJ5ROpFRT6wam1JRfwfLqRFhBSlyn0Z2j3kspa6nd0vhLtKc9Qs_QA21jpnK7cGbEWcO96WkPxU67rbPUZOW7b4Ao3PfCKEbswla6zuBh2bBfqWCwUtehS7pA_xvR41Hz-5Vjyx7sBqJ5I6_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر بیرانوند روز اول خدمت
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107428" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107427">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📊
🇳🇱
🇩🇪
آنالیز تاکتیک جذاب ژاوی در دیدار اخیر خود مقابل آلمان یورگن‌کلوپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107427" target="_blank">📅 16:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107426">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6242b00b.mp4?token=SmBIBvesadGvROm2B3-fW7jPTjg0aEnGFOT1-tjaVPTag7iSegJ0PtTy0i8heNJ7_LjgLADQ8rZjX5DL0KiSSmPV8C5oZI-yRvLvrQUFRMYMEGGaXV1LUqaXtTdYswtLSI-ss8XX2nG_ZK-fDqp5R8Lbqixs3JQ8ni95FEKCPT9GpsdOA-ulSXfr_LMhObhETRAY67JKGJxP4CCBimHiC7zCk0SmUMTGgXfELQhsLDLtKCEfaugW68wdhZASTO59dB2dWRcXe0Jw1RECYjRs257JXvUGpfZt0QjoZ-bQ59QWdDo6b6BXmAwY8Fpy7cUUuH8jiAuMqvJoocV-YD95aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6242b00b.mp4?token=SmBIBvesadGvROm2B3-fW7jPTjg0aEnGFOT1-tjaVPTag7iSegJ0PtTy0i8heNJ7_LjgLADQ8rZjX5DL0KiSSmPV8C5oZI-yRvLvrQUFRMYMEGGaXV1LUqaXtTdYswtLSI-ss8XX2nG_ZK-fDqp5R8Lbqixs3JQ8ni95FEKCPT9GpsdOA-ulSXfr_LMhObhETRAY67JKGJxP4CCBimHiC7zCk0SmUMTGgXfELQhsLDLtKCEfaugW68wdhZASTO59dB2dWRcXe0Jw1RECYjRs257JXvUGpfZt0QjoZ-bQ59QWdDo6b6BXmAwY8Fpy7cUUuH8jiAuMqvJoocV-YD95aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مهدی‌مهدوی‌کیا: عدد فوتبال ایران پول خرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107426" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107425">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63162a7ef0.mp4?token=H5vXMflJpzIYDI11O9EYNHrU7F0gFJ9K-xruQBRPXqqDtDlpUeVbt123Gz8vpwrMPv8u_iVQLkhPHFyLK2epF90DDYtvi6pJIwq4fE38ytxdplX-tqZ9SLWAy2MIbgobUd1j3eLgtuGGG3Ug95wqMC8JXCu49gTIjk0jymZfT-mwzkLvQTGCCmMflkVbnNv-IHKJVFRFgOn14m2w98Pf3ZgOfiSi6_ASOW9gyul5WyLKlRhKtROKZ_cy4p8n9k-FjHkGLvDgqzOnvJYwx0MY8T7mLernI9Mtx01zy3zLMKMHjeSRcdgrq0MQCaORA_lxfAjZSoXk2QZjmlvhkJXYtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63162a7ef0.mp4?token=H5vXMflJpzIYDI11O9EYNHrU7F0gFJ9K-xruQBRPXqqDtDlpUeVbt123Gz8vpwrMPv8u_iVQLkhPHFyLK2epF90DDYtvi6pJIwq4fE38ytxdplX-tqZ9SLWAy2MIbgobUd1j3eLgtuGGG3Ug95wqMC8JXCu49gTIjk0jymZfT-mwzkLvQTGCCmMflkVbnNv-IHKJVFRFgOn14m2w98Pf3ZgOfiSi6_ASOW9gyul5WyLKlRhKtROKZ_cy4p8n9k-FjHkGLvDgqzOnvJYwx0MY8T7mLernI9Mtx01zy3zLMKMHjeSRcdgrq0MQCaORA_lxfAjZSoXk2QZjmlvhkJXYtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇪
نحوه برخورد بازیکنان ایرلند با اسرائیل در بازی دیشب که حسابی جنجالی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107425" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d3f57825.mp4?token=a48DCGduD5F4kSqWdK4wZSCP5k7cqzPOPpMjItMjxOcZfius7izqnFTbpWQdgJlqZ-a0ypMmkxQsOHOj-d3o-6VTH2cTQbzh13MPK3A8m5JK-tADcwntYtOEvV5fMpz4ryeav1GZjZ88913a3T87CWsqk0exqDJ_cPf3CJBHBg3EcZR2kDGhPnRnNTDUVxn5UgM5joqggDHb-xZdnFKPEnH1FcTVoEoVmb6qRTN1sXr4CO-aubXqwLDk90RbHQmWpfRO7Y_OwYGmsE4NuDyew4_iRJAQc6q9aJMDZj37yYnAl2Qq583zVnPhll0bMZvcZocgmT4CjbwTsvUyf71GxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d3f57825.mp4?token=a48DCGduD5F4kSqWdK4wZSCP5k7cqzPOPpMjItMjxOcZfius7izqnFTbpWQdgJlqZ-a0ypMmkxQsOHOj-d3o-6VTH2cTQbzh13MPK3A8m5JK-tADcwntYtOEvV5fMpz4ryeav1GZjZ88913a3T87CWsqk0exqDJ_cPf3CJBHBg3EcZR2kDGhPnRnNTDUVxn5UgM5joqggDHb-xZdnFKPEnH1FcTVoEoVmb6qRTN1sXr4CO-aubXqwLDk90RbHQmWpfRO7Y_OwYGmsE4NuDyew4_iRJAQc6q9aJMDZj37yYnAl2Qq583zVnPhll0bMZvcZocgmT4CjbwTsvUyf71GxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیتِ ناراحت کننده ی سرخیو آگوئرو.
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107424" target="_blank">📅 15:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107423">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmNYmhIHj_4WRgKGAzysKZuYvhKkI6J2M0eWFw3T7ikmUKsIAw42RxjAVX7-7FitDdOhmnZN5qGaKWdahDJFsuUs2EafVE5CbFQGVzu_4omUERfzyw8UmRgSW_IqN2IHJEounAXDV1PUewZmvXv-J09gqWloYQAm-0qwyXT5B90vqmcD7pZjSq2Ogd1GZhZQPiqrXm2IiJmi5_dsgoMjFVnxbFcnF_lVPEBkDJp3X5rRYrVn1sKNvwRQ1kljQ8epB9jDmU6jpLRjsUR3g_DC9gK4dxR6HfigRKo-PXx_ag6WH7CjQmyj_iXJXsk6SZvbYUC-0KS9dwtDBbE5vA0oBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مقایسه آمار هالند و رونالدو تا ۲۶ سالگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107423" target="_blank">📅 15:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107422">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ff849b11.mp4?token=XtPx-RQJ_3IwPOR8nchOqghbno84dK7axpcT7GYbDXnZ4dzcaMF0BOt4cm4utFWjB79kp_mXmVbLyqLVq7TZZrUSGxFSyL3tFvljC9Ca5ThajpQBtvk-XWueh97VdYpzue7vOLvZw1V2f-vtO6bORacTdNCL7504zmxREOmUbItdz8wRf9du92fjs-nTvSYjoIWjzzkkYPN0KF-4nLDSg7gCzDO-q2Ix3UYre6H1vOzt6iFyqFUw0qfGCXxpVwSMtQMwtCxyiF--bun7E6U127xOv9PBE3G4eX5drSOAwyCqhhK2eSAoujrueyDt8EH_tLLrDnXfn2WT4w-YI21xaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ff849b11.mp4?token=XtPx-RQJ_3IwPOR8nchOqghbno84dK7axpcT7GYbDXnZ4dzcaMF0BOt4cm4utFWjB79kp_mXmVbLyqLVq7TZZrUSGxFSyL3tFvljC9Ca5ThajpQBtvk-XWueh97VdYpzue7vOLvZw1V2f-vtO6bORacTdNCL7504zmxREOmUbItdz8wRf9du92fjs-nTvSYjoIWjzzkkYPN0KF-4nLDSg7gCzDO-q2Ix3UYre6H1vOzt6iFyqFUw0qfGCXxpVwSMtQMwtCxyiF--bun7E6U127xOv9PBE3G4eX5drSOAwyCqhhK2eSAoujrueyDt8EH_tLLrDnXfn2WT4w-YI21xaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بیژن مرتضوی به ایران بازگشت  بیژن مرتضوی، خواننده و آهنگساز، دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107422" target="_blank">📅 14:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107421">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1947c53917.mp4?token=TNtfXgp_gBpsDlhAAMXTdRMP5rWNRu_hUjv-KJGvNqI6H4mnLucb4c2K4vE8xzQRBZABZp0obzf9FlfJTgyQzN_qKfR-rLzdIV_UlPiGz658iqRAqlPNf4xwoqJ_XDvl6Qt_8VBcpP3RXi7kqhJw0bXt3FuwaLHDMYzXMC83f0pb6M2DuTe5gooK0BTJQUItUpQrFoMc35RrLSJmRVrBNEnIpi9_ijG_7ks0DhohowVUj4lNXfXWhTLBXByTaBlMp1-WIjsaX0XwsLi-9xmitv7LADjWv7EEHx4xOQC0GwiXOq4dAyNiE33BtRHa59AeZCwAmP3scbSFTl6vqAz4-awDp5kKjdHwEXssESxWRsYBwTKIy2UxDntsnoZB_OBXcpzs4jio0fJWMb8ZqYxHQNBjAaQSZefBWeLUBgjqcdPy3cflPewfdxLYx2WWfm5q5f59LR43gwJbQiYlqS6NJzYS-mV62u0WhDZKY1FrWW-oXaUWdzfxPow7NrqoWEXQoxRI698spmYkjEQb6d12DCd_fLIFs4C0jOI_eoAx9nfthjpxFW9XfCfSWexSW6zdgB-nSpo8g0QRLygk0uCNO4XqpEKvTntW3obbDxPUWtpRxkRixSWMe2bBZiLOwj2prT0ur76WkI1t5Uq6r2ohQHTdnOPNfgnUaDmvqRu0E80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1947c53917.mp4?token=TNtfXgp_gBpsDlhAAMXTdRMP5rWNRu_hUjv-KJGvNqI6H4mnLucb4c2K4vE8xzQRBZABZp0obzf9FlfJTgyQzN_qKfR-rLzdIV_UlPiGz658iqRAqlPNf4xwoqJ_XDvl6Qt_8VBcpP3RXi7kqhJw0bXt3FuwaLHDMYzXMC83f0pb6M2DuTe5gooK0BTJQUItUpQrFoMc35RrLSJmRVrBNEnIpi9_ijG_7ks0DhohowVUj4lNXfXWhTLBXByTaBlMp1-WIjsaX0XwsLi-9xmitv7LADjWv7EEHx4xOQC0GwiXOq4dAyNiE33BtRHa59AeZCwAmP3scbSFTl6vqAz4-awDp5kKjdHwEXssESxWRsYBwTKIy2UxDntsnoZB_OBXcpzs4jio0fJWMb8ZqYxHQNBjAaQSZefBWeLUBgjqcdPy3cflPewfdxLYx2WWfm5q5f59LR43gwJbQiYlqS6NJzYS-mV62u0WhDZKY1FrWW-oXaUWdzfxPow7NrqoWEXQoxRI698spmYkjEQb6d12DCd_fLIFs4C0jOI_eoAx9nfthjpxFW9XfCfSWexSW6zdgB-nSpo8g0QRLygk0uCNO4XqpEKvTntW3obbDxPUWtpRxkRixSWMe2bBZiLOwj2prT0ur76WkI1t5Uq6r2ohQHTdnOPNfgnUaDmvqRu0E80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
على تاجرنيا مدیرعامل استقلال: پاى حرفم هستم ؛ پول كاريله رو ميدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107421" target="_blank">📅 14:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107420">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdc8f323f.mp4?token=p8et_uQ0xklTifBPVkBbY4rrXlweBHSK4vF67pdLNMjKGl2sJYh84LCUIFNNndxmD4MXphUsWVvb0kz6HCOiskzq9irGG2fKfh6_SUTkjoYNW6g3M3fjcWm8jbcWy2iOgndGglHSxbxIL6_qyflAY-bjzG8g2JduTHAF-xAHYHao2gorY8N_BMA0818_-G9aPW3KiMrQo5CzyF0Hz0EJtypX5FsjoVwkWAzYaeRFC3Bpho09M8BjLfHhYAF0Ot9HOroDUvhADOrNmbS2Yb3JT6WOb-rEmx9f_AWSwKYtExpR8w74sb3N-NRpsTUTnqDj0kWg5-nkYTOVxpb-GB4Law" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdc8f323f.mp4?token=p8et_uQ0xklTifBPVkBbY4rrXlweBHSK4vF67pdLNMjKGl2sJYh84LCUIFNNndxmD4MXphUsWVvb0kz6HCOiskzq9irGG2fKfh6_SUTkjoYNW6g3M3fjcWm8jbcWy2iOgndGglHSxbxIL6_qyflAY-bjzG8g2JduTHAF-xAHYHao2gorY8N_BMA0818_-G9aPW3KiMrQo5CzyF0Hz0EJtypX5FsjoVwkWAzYaeRFC3Bpho09M8BjLfHhYAF0Ot9HOroDUvhADOrNmbS2Yb3JT6WOb-rEmx9f_AWSwKYtExpR8w74sb3N-NRpsTUTnqDj0kWg5-nkYTOVxpb-GB4Law" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بیرانوند از خیابانی تو خدمت مرخصی میخواد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107420" target="_blank">📅 14:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107419">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39074d4c05.mp4?token=eDgXwzz4LL_m76-G9g18YkewNAJZT9wx0d9KYm3mAgQI10IjG-RoAtt__DtD8Tq5CN-8TV-CDTuVkdEIOsV9ujunbWWWYrhAb5gbaVQusDsuGWQmJgwhb8Dpwf5mYqS553sf1hCpBnMmfTe1x43qKZiub48dyc44ck5iPm7OCfxuFU4CseKePiF7CjS3IHEIZclz-J85-crVL-UJSqEuCLDFSESYRu0V-sie87UwyM9ot5S32SeJWqx79Vgyh0snbItdzfQvzaRF5YJ5WPpdrxALxxMI_d2yIWHkEV3csxIYJQvXGuwOMPQWOPF0qhUo-ZnKUMMAEShbyPFdZmwegRXeCcrovenmpteDQPCvLfDG-z3Ndp0QZOSkTjg-O7bhF0hQIvIsn1k5KYTq0a1W0usiWzQlIXP-qCkt-pONKUeG3vFI1tcaubJWeAmxNLmseS2w2nqWQhqsiqHtJJ7wAg829EI6jhmQAT02Neo4fcfjbG01gB1lAuRseSyl7dbq7-v20zaZPubJFfUCZ8FWhAuKUN2sazqTuzj-dwjUdWB7tA7QGzwDbzph7urVRsTLzq8mS00ekxqYXyhOiVhOWEiND6vsGKJQCNAxPFfV0Fp2ALdZ6eLrZnHuprFPNY082xa1S4n5i_OMKPMq-ymz8p1z99_ZjP19w06uwJQwjvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39074d4c05.mp4?token=eDgXwzz4LL_m76-G9g18YkewNAJZT9wx0d9KYm3mAgQI10IjG-RoAtt__DtD8Tq5CN-8TV-CDTuVkdEIOsV9ujunbWWWYrhAb5gbaVQusDsuGWQmJgwhb8Dpwf5mYqS553sf1hCpBnMmfTe1x43qKZiub48dyc44ck5iPm7OCfxuFU4CseKePiF7CjS3IHEIZclz-J85-crVL-UJSqEuCLDFSESYRu0V-sie87UwyM9ot5S32SeJWqx79Vgyh0snbItdzfQvzaRF5YJ5WPpdrxALxxMI_d2yIWHkEV3csxIYJQvXGuwOMPQWOPF0qhUo-ZnKUMMAEShbyPFdZmwegRXeCcrovenmpteDQPCvLfDG-z3Ndp0QZOSkTjg-O7bhF0hQIvIsn1k5KYTq0a1W0usiWzQlIXP-qCkt-pONKUeG3vFI1tcaubJWeAmxNLmseS2w2nqWQhqsiqHtJJ7wAg829EI6jhmQAT02Neo4fcfjbG01gB1lAuRseSyl7dbq7-v20zaZPubJFfUCZ8FWhAuKUN2sazqTuzj-dwjUdWB7tA7QGzwDbzph7urVRsTLzq8mS00ekxqYXyhOiVhOWEiND6vsGKJQCNAxPFfV0Fp2ALdZ6eLrZnHuprFPNY082xa1S4n5i_OMKPMq-ymz8p1z99_ZjP19w06uwJQwjvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔺
آنخل دی‌ماریا پس از به ثمر رساندن گلی شبیه گل مسی:⁣ قبل از بازی استرس داشتم و سعی می‌کردم با موبایلم خودم رو مشغول کنم و به بازی فکر نکنم که یهو گل ضربه آزاد مسب جلوی آمریکا روی صفحه گوشیم ظاهر شد. وقتی توی بازی صاحب کاشته شدیم، با خودم گفتم امتحان کنم؛ درسته من مسی نیستم، اما شاید جواب بده. و واقعاً جواب داد!⁣
🥇
روزاریو سنترال در فینال سوپرکوپا اینترنشنال آرژانتین با دبل دی‌ماریا ۳ بر ۱ استودیانتس رو برد و قهرمان شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107419" target="_blank">📅 14:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107418">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4774088c.mp4?token=KYCWgjcjaeFvMIxRbTm5Hp5qEeHVQvkkd9OfnpBDQ2gVa8Aq5Ml8aYOK0SWoXT4grePR0zYzsuD9In2Ghr5JtHdvX2mpNxu8nNgSgdPI2GNe_KZp1_lhK7D8Pnw50_5Ux_pRvcWzDH0zElCyHuP-0rH3oqsiOz0SFdjmvZb3Rq15GiGmHihH0wXZ2KjTiYpY7OYINrk6L-ks8bv7eZi4N5F_ui2aY69I4qBMZQOKMC-pM9uNJ3AcOxCWTDnTjmZ-qVSCnJORxw_s0WmZ1Mf_jzxvvPR89bbgWbcZ-QN3vtVMsER3f3jXQtoAhxSAPZ3dwRqusW8faQwqnvCX8Yxfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4774088c.mp4?token=KYCWgjcjaeFvMIxRbTm5Hp5qEeHVQvkkd9OfnpBDQ2gVa8Aq5Ml8aYOK0SWoXT4grePR0zYzsuD9In2Ghr5JtHdvX2mpNxu8nNgSgdPI2GNe_KZp1_lhK7D8Pnw50_5Ux_pRvcWzDH0zElCyHuP-0rH3oqsiOz0SFdjmvZb3Rq15GiGmHihH0wXZ2KjTiYpY7OYINrk6L-ks8bv7eZi4N5F_ui2aY69I4qBMZQOKMC-pM9uNJ3AcOxCWTDnTjmZ-qVSCnJORxw_s0WmZ1Mf_jzxvvPR89bbgWbcZ-QN3vtVMsER3f3jXQtoAhxSAPZ3dwRqusW8faQwqnvCX8Yxfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🐐
سوپرگل دیشب لیونل‌مسی از نماهای مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107418" target="_blank">📅 13:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107417">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a5b80ac0.mp4?token=tUcPdcCR-Wp6XNf_FbxY2CO-kX6LQaHm36BBNR12ExTm1QBAnXW0Kkac1CTckjSflQL433d75wUIRbbaO7BG9Io7e2eaGrmLly14v_sQmKhHixNjACgsvKpnc85K-NTV2yZL9DrxkyNPhXNoPSOP3XpYnXjjdA_GrfD-9uUzVlGBqvF66R5DvB9hOEhrIE7wpv7-Ug_pcdo20gqFOpoyuJXe8nagctTHiQlddr3ME2g_jKZsLtBfO1vZJH1p7R5HUCw-DbQBz1Dz61CQzMs9iNd-Ig1zoBix2FgmsrFd_mTr2gW_-zQ_fGqj9n3bseu7TsesZMPuzB__qe-5YS8r3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a5b80ac0.mp4?token=tUcPdcCR-Wp6XNf_FbxY2CO-kX6LQaHm36BBNR12ExTm1QBAnXW0Kkac1CTckjSflQL433d75wUIRbbaO7BG9Io7e2eaGrmLly14v_sQmKhHixNjACgsvKpnc85K-NTV2yZL9DrxkyNPhXNoPSOP3XpYnXjjdA_GrfD-9uUzVlGBqvF66R5DvB9hOEhrIE7wpv7-Ug_pcdo20gqFOpoyuJXe8nagctTHiQlddr3ME2g_jKZsLtBfO1vZJH1p7R5HUCw-DbQBz1Dz61CQzMs9iNd-Ig1zoBix2FgmsrFd_mTr2gW_-zQ_fGqj9n3bseu7TsesZMPuzB__qe-5YS8r3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
ویدویی از درگیری بلینگهام و کوکوریا دو بازیکن رئال در بازی اخیر اسپانیا و انگلیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107417" target="_blank">📅 13:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107415">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f2619929.mp4?token=WY-JeqaPjqeLWl77Y-er-J0jO3KUv_oMQhMHypfnp3UWruQdWIicghcTY8LOuFho4gHUOdX5WLOrEujg_jWK1rMicbEU73sH4_Alooz3Yepaq4xzckKVhyNhjHXK3bsyEa7mrq3FX6ZUVBQnWrUF_n5dybfF2f90-FsvmPbIdIppiDtiiFOEDAB9KWzSRwVDEG6OfPedxYKe3MUIi6SbGONGj1d6StYLEX6GHjAOUnj1Kso3ClPUyopH3e3kk7jrP6n_u8dhFodoyVJ-cKzTeojOaLhxPbzLa40bLp09iBgocHLp7Eeta7Dzxmg_UJusron_C0WQ-vp2n6xq36QyNgoUQBK1N79Roqlzv0HePi21jxH44mu9yES9wyK_FyT3HWvV6rDLgg_zyZ3yjLBVsuLUvJGFpnPHBvGiX-RMA2j8ZdqCAqKdiT46dpYu-rb2Mo3GPLLecvw4XPE9tOx82HJkmyuVP1Bgws91VgJmeGC4t9G-hZz6WMR1WHiFmloPn7CU3nulKQdGaRCfqfwV25YHqr35EguEhiU_cA4IX6A1ssCWv1GysROlt9RTdw-xK5fG1N6xcMPsTaMzzAJwMb10b6CuXzmcf2uwXTbH2gk4FuFBmgiMmLxmIRuE17oiPaE8uOQKQ6kiv3I34Nt7tgLOScYBlQG4mOgjhXUb-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f2619929.mp4?token=WY-JeqaPjqeLWl77Y-er-J0jO3KUv_oMQhMHypfnp3UWruQdWIicghcTY8LOuFho4gHUOdX5WLOrEujg_jWK1rMicbEU73sH4_Alooz3Yepaq4xzckKVhyNhjHXK3bsyEa7mrq3FX6ZUVBQnWrUF_n5dybfF2f90-FsvmPbIdIppiDtiiFOEDAB9KWzSRwVDEG6OfPedxYKe3MUIi6SbGONGj1d6StYLEX6GHjAOUnj1Kso3ClPUyopH3e3kk7jrP6n_u8dhFodoyVJ-cKzTeojOaLhxPbzLa40bLp09iBgocHLp7Eeta7Dzxmg_UJusron_C0WQ-vp2n6xq36QyNgoUQBK1N79Roqlzv0HePi21jxH44mu9yES9wyK_FyT3HWvV6rDLgg_zyZ3yjLBVsuLUvJGFpnPHBvGiX-RMA2j8ZdqCAqKdiT46dpYu-rb2Mo3GPLLecvw4XPE9tOx82HJkmyuVP1Bgws91VgJmeGC4t9G-hZz6WMR1WHiFmloPn7CU3nulKQdGaRCfqfwV25YHqr35EguEhiU_cA4IX6A1ssCWv1GysROlt9RTdw-xK5fG1N6xcMPsTaMzzAJwMb10b6CuXzmcf2uwXTbH2gk4FuFBmgiMmLxmIRuE17oiPaE8uOQKQ6kiv3I34Nt7tgLOScYBlQG4mOgjhXUb-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا:صحبت های بازگشا مدیر پرسپولیس سخیف است و در شان من نیست جواب او را بدهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107415" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
