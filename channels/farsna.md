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
<img src="https://cdn4.telesco.pe/file/kMA480aO3f68fndHC4hfG6R_FWf5dLBG8Gc3gO4v6jfzcDIhmnQWE4Hb3HdGdWwuXe-NLIsP8dO8zJ2yY07hL8dvPOgFsHTQMcYR86goavRIV4yZEdxbV4b3c1BZKPuYERw7PlZ1-TEYoXFc6rHOpx8KE6EhFB1QYfQVQMrlE0-vKYaQmjsIm0FooRTTuMzsws5dEvkTgUhX9VCqpZu2VFNV8ZtktZKsTmOyPgR8lsC9rjB7sPY7Q8s_o5gdkjF8DDj3vtu9hhHNs53rH_1BFJftUEtTYobIxlGoXH55tAWy_8npmAdarsrfjuo6DoHTRhxRCg7Gcud9kPWnySH9WQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-440713">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): پاسخی دردناک به رژیم داده شد و توقف عملیات اعلام می‌گردد
🔹
درپی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.
🔹
پاسخی که رژیم جعلی صهیونیستی و حامیان آن باید از آن درس عبرت گرفته باشند.
🔹
بر این اساس، توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما تاکید می‌شود که در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/440713" target="_blank">📅 14:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440712">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی لجستیکی حامل مهمات و یک دستگاه ارتباطات متعلق به ارتش دشمن اسرائیلی در الشقیف با پهپادهای انتحاری مورد اصابت قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/440712" target="_blank">📅 14:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440711">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=sMw63B0iVRDrdYEP0d96CU5gfZB3JDnTYiptk4a5ZRzR6TWF-R59fKrzq26UYF8WABGpF77KLOsIDUECjDT2Ml7dm2U2zohJwO0mTeF8-oYPLg6fxkOtDdYjj0CWWINd67OgOrPky921zm2FHoInFoMhhE6-iXERimTvFG8EbTHNeeCFG3YoV6q4vfVQOAfZqEb_-fW3lBJrJDrgZMW9-YaUbHaiRLmTORLW7wA9H7uIqaKTQn2rR-3Tf45IR1lRuxzYuwGhNaDBG5JoVufWE0UeLDwhs3BKQEqygTBnDw4pRrGl53e8CgZaFozgd8prI0gq_jl_e0c9J_TLGFzqcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=sMw63B0iVRDrdYEP0d96CU5gfZB3JDnTYiptk4a5ZRzR6TWF-R59fKrzq26UYF8WABGpF77KLOsIDUECjDT2Ml7dm2U2zohJwO0mTeF8-oYPLg6fxkOtDdYjj0CWWINd67OgOrPky921zm2FHoInFoMhhE6-iXERimTvFG8EbTHNeeCFG3YoV6q4vfVQOAfZqEb_-fW3lBJrJDrgZMW9-YaUbHaiRLmTORLW7wA9H7uIqaKTQn2rR-3Tf45IR1lRuxzYuwGhNaDBG5JoVufWE0UeLDwhs3BKQEqygTBnDw4pRrGl53e8CgZaFozgd8prI0gq_jl_e0c9J_TLGFzqcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از تنگهٔ هرمز و کنترل ایران بر این آبراهه  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/440711" target="_blank">📅 14:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440710">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce31a395bf.mp4?token=Ie9cFlsyJCh5pILdeiWQlzfu-thtttWQ0gN7QzL-XTUOgZvUblHBRYFZ0jjtTMw172YM23T2vMCYMoxdkNmgzdAEFmv2BsjkyZS9tPjnvi1VeMVGFQSJjTZXe7OGOMsmxbXaC_fBlGfj6SV1C8pAePPSgBIdhr15Z05wJHOoqIZaoEFhjecmFhZLYWrTBTNjcGLCN3FOROZhc9soNVW7fw4TPpohOtOANShQOP4MBwKH-S2BTIQASZmcwI6TP2yX0QNBG4R5HFpMtt_hiaIsOnOq9UAYyfL_bU7xY7hImvm00yUiqcbn3OMTuoOy2_kOhjUfWr_FYlqDhWsdkP0GyjEcxFRH5IWCnGpAJMVsWJ8tPQtOqPP6Kr8hNloodJg15QOX0EbBrtFW33m29s-zwenbn0i28HX1CQzghqQ7LdgOPrrTZXjd7nYes4MCQvNqhzYzSKu3IXeGLglfarUFVnsZJPyKxXZnIDAzScKugnP4xHSEveEAbAUowhnxW8GxuTbsz3O55_GcZs4pY-OEq91sx8pLvTeQ_hkYkV4G2Y6NzIbVY6FQA5BpSUfH2GvBdZRt3LRVgzb69EXL44BWMg9lfUf2n9oDxgjQ6QAquwa896mUyDOfyUI8arSx0x_lxAdcOkGtz9HTjOzzcwbJ1N422_K660ejiNwHpASj0IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce31a395bf.mp4?token=Ie9cFlsyJCh5pILdeiWQlzfu-thtttWQ0gN7QzL-XTUOgZvUblHBRYFZ0jjtTMw172YM23T2vMCYMoxdkNmgzdAEFmv2BsjkyZS9tPjnvi1VeMVGFQSJjTZXe7OGOMsmxbXaC_fBlGfj6SV1C8pAePPSgBIdhr15Z05wJHOoqIZaoEFhjecmFhZLYWrTBTNjcGLCN3FOROZhc9soNVW7fw4TPpohOtOANShQOP4MBwKH-S2BTIQASZmcwI6TP2yX0QNBG4R5HFpMtt_hiaIsOnOq9UAYyfL_bU7xY7hImvm00yUiqcbn3OMTuoOy2_kOhjUfWr_FYlqDhWsdkP0GyjEcxFRH5IWCnGpAJMVsWJ8tPQtOqPP6Kr8hNloodJg15QOX0EbBrtFW33m29s-zwenbn0i28HX1CQzghqQ7LdgOPrrTZXjd7nYes4MCQvNqhzYzSKu3IXeGLglfarUFVnsZJPyKxXZnIDAzScKugnP4xHSEveEAbAUowhnxW8GxuTbsz3O55_GcZs4pY-OEq91sx8pLvTeQ_hkYkV4G2Y6NzIbVY6FQA5BpSUfH2GvBdZRt3LRVgzb69EXL44BWMg9lfUf2n9oDxgjQ6QAquwa896mUyDOfyUI8arSx0x_lxAdcOkGtz9HTjOzzcwbJ1N422_K660ejiNwHpASj0IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
🔹
یک منبع آگاه نظامی به فارس خبر داد ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد…</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/440710" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440709">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKmtBS7iErYP1zZWNQzcmdxauQdXf1umflnnW0uFQhQ5ZtcCN5YRPvhECTTEPcV_gQ7IdfAjSAi_U7Ue7qg_pRu0AT0BQD_B4dXV4B4EGLkQCRIBk-dsTC2mjdSRqMkvrGZWXvK402_fIvPWJO0Xir897P7ri06cRtg-o_61HmWa2VdqNvJ7JkosknGT--fpehOgSiY6j38u61Lze8M6UPPzdpwpvvzgwpo4FFP_iD2DO9IAZXj3Gul8I6_92XR_2-APMe3tnSiPK0Vmeg8gl8RFBHpjj3ngkO-qXdq1nMEVVBJUR57fw8waFKxVr9BrlWFioWPZESz45u783AZRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و ایران باید فوراً «شلیک به‌سمت همدیگر» را متوقف کنند.   @Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/440709" target="_blank">📅 14:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440708">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2cc8dba14.mp4?token=jXpTaj-05Dhx55eGSVQa9atFMQHXfV8Pb-lGymbrn8efWN9pj0IMqfvVbG3-K4yFhir8sEUzuRRGwFncDfuVXetDWGmOrjpFgiqi5w4Uta8vdqgTqu6oH6B6KNdvlaIXnEpVXLs9MqbtGOSxJpA5Sm8reDnVElTDGLMf48R0bx8RO95YZWW4THXRKJdkQ3Qo_x2KDmJrdnL7X3GY8CMJ2E0jguLaF_WtlJQ_mZvfoOIahbV7ybP5vMpe0BYvKIaI1nemJBh-130YXzhBnu3FH5PCWR80bk6r7eorcIrZ34EBYDEyaqiDGB7jVi8iMNKrcZ3CX_3Nt9oMj1UfyG_cd2BTWS0_aFSg_dl6-eGIrVu3mhUJSMtor6rlYVN-MwKMeF8-9uVuv1TKGRe6djSDOCPkpkm0JzsdOyt82AZOABQ8sJidmnsuunxfP75xuHk8H-SdNlDqCck18fSzfMiVO1977rkOQoR080XFPrp-7d5Wc-GYNabWw_MKkcX8GjpTyu0VveH-ZTpBVCXWTVuao4MPXekO99cXS0dByktI4ah03SR9VSAjWmBomi_ZKsVId3rR9rYEkTUN9w42rF8uERUFvDEm0khT8wOrdd8soF-6b5ltrbbA3e-deq4UGK44zFg_7ryFqkIPs9tHu17Lnq4uHrgk95nE5Ha7m4dA6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2cc8dba14.mp4?token=jXpTaj-05Dhx55eGSVQa9atFMQHXfV8Pb-lGymbrn8efWN9pj0IMqfvVbG3-K4yFhir8sEUzuRRGwFncDfuVXetDWGmOrjpFgiqi5w4Uta8vdqgTqu6oH6B6KNdvlaIXnEpVXLs9MqbtGOSxJpA5Sm8reDnVElTDGLMf48R0bx8RO95YZWW4THXRKJdkQ3Qo_x2KDmJrdnL7X3GY8CMJ2E0jguLaF_WtlJQ_mZvfoOIahbV7ybP5vMpe0BYvKIaI1nemJBh-130YXzhBnu3FH5PCWR80bk6r7eorcIrZ34EBYDEyaqiDGB7jVi8iMNKrcZ3CX_3Nt9oMj1UfyG_cd2BTWS0_aFSg_dl6-eGIrVu3mhUJSMtor6rlYVN-MwKMeF8-9uVuv1TKGRe6djSDOCPkpkm0JzsdOyt82AZOABQ8sJidmnsuunxfP75xuHk8H-SdNlDqCck18fSzfMiVO1977rkOQoR080XFPrp-7d5Wc-GYNabWw_MKkcX8GjpTyu0VveH-ZTpBVCXWTVuao4MPXekO99cXS0dByktI4ah03SR9VSAjWmBomi_ZKsVId3rR9rYEkTUN9w42rF8uERUFvDEm0khT8wOrdd8soF-6b5ltrbbA3e-deq4UGK44zFg_7ryFqkIPs9tHu17Lnq4uHrgk95nE5Ha7m4dA6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انهدام ۴ هستۀ عملیاتی گروهک‌های تروریستی تکفیری
🔹
وزارت اطلاعات: سربازان گمنام امام زمان (عج) در اداره کل اطلاعات سیستان‌وبلوچستان در چند عملیات مقتدرانه ۵ تروریست این ۴ هسته را به هلاکت رساندند و ۱۹ تروریست دیگر را پیش از عملیات انتحاری، ترور و ایجاد ناامنی…</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/440708" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440707">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9M9YNgTtSHtR5hyc4Y3nDAT9VG2LaeW58fhFDca-b2V_j500KnGlJCfygS3xmcbTZB7TVvel9hnncl4rDXJpwvrDS2p6fMkMVBNmXOBCaRVO_1-w8pXBXdnxqtao1csiVPnxYAOEHG5vlQez4JP-pU2myrTeDzmmwPk8xLTi92HXUsXrR_OfEuaLwSnTJpnKS531j2-C-YofMZfULzPIZXKA3DPmiOm_8_KYtskXgb-syCGiYxiufMq7Fjj8G9PizeN_kaS-iwk3rJMVKt_ONK1VLD-zCOKtqxbR2x8AqEgZ1DtPC8ZoF0SMvGHM0-r-cgZ67vWXwjMQ35HB5ydZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۴ ریشتر در عمق ۱۰ کیلومتری زمین، مهرانِ ایلام را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/440707" target="_blank">📅 14:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440706">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c4a04703.mp4?token=gwHwgwIK_RlO1fDZqzhcwg6losYjSJlfNSQ0VivsQ3mMORvVLXWeqc-8qr-AxhTk5F9PA_1hoGk6WB69u5qB6ywG-11TiasUzs6FUbmytw2Bj6Pbjxqrwf4QA7fii1p14uKDOdTBnSLbC6TyEzdJsOloCALNaxo6L8lWuK4H4UEIXGBIWfZKLwepjdn6kxaJCMPCRBxIDUklGDvnA0GCNr-HnVo26U-_mKfqByV0IlC86H8DThi7eaitVnUnfhic1g2_YOR3Qrgu9jK5VqSssDDRNEXBeBhzbTrqppZIOKNnqL0p6vlU3BDpE8jKIuziSruhriOk5sbF8lemOL9tog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c4a04703.mp4?token=gwHwgwIK_RlO1fDZqzhcwg6losYjSJlfNSQ0VivsQ3mMORvVLXWeqc-8qr-AxhTk5F9PA_1hoGk6WB69u5qB6ywG-11TiasUzs6FUbmytw2Bj6Pbjxqrwf4QA7fii1p14uKDOdTBnSLbC6TyEzdJsOloCALNaxo6L8lWuK4H4UEIXGBIWfZKLwepjdn6kxaJCMPCRBxIDUklGDvnA0GCNr-HnVo26U-_mKfqByV0IlC86H8DThi7eaitVnUnfhic1g2_YOR3Qrgu9jK5VqSssDDRNEXBeBhzbTrqppZIOKNnqL0p6vlU3BDpE8jKIuziSruhriOk5sbF8lemOL9tog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در نفتکش هندی در سواحل عمان
🔹
مرکز امنیت دریایی عمان از وقوع آتش‌سوزی در یک نفتکش حامل ۲۴ ملوان هندی در ۵۲ مایلی سواحل عمان بر اثر اصابت یک شناور بدون سرنشین خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/440706" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440705">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انهدام ۴ هستۀ عملیاتی گروهک‌های تروریستی تکفیری
🔹
وزارت اطلاعات: سربازان گمنام امام زمان (عج) در اداره کل اطلاعات سیستان‌وبلوچستان در چند عملیات مقتدرانه ۵ تروریست این ۴ هسته را به هلاکت رساندند و ۱۹ تروریست دیگر را پیش از عملیات انتحاری، ترور و ایجاد ناامنی بازداشت کردند.
🔹
در جریان این عملیات‌ها یک سرباز گمنام امام زمان با انفجار انتحاری یکی از تروریست‌ها به شهادت رسید و یک نفر دیگر هم مجروح شد.
🔹
از مخفیگاه این تروریست‌ها شمار قابل توجهی سازۀ انفجاری، سلاح کلاشینکف، سلاح‌های سبک مثل انواع کلت کمری و نیمه‌سنگین مثل دوشکا، نارنجک‌انداز ، سلاح‌ M16 با دوربین دید در شب و سلاح M4 کشف و ضبط شده.
🔹
وزارت اطلاعات از مردم خواسته هرگونه موارد مشکوک را به ستاد خبری وزارت اطلاعات به شماره ۱۱۳ یا درگاه‌های رسمی ستادخبری این وزارت‌خانه در پیام رسان‌های ایتا، بله، روبیکا و سروش‌پلاس به آدرس vaja113@ با تیک آبی گزارش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/440705" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440704">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">واکنش تحلیل‌گران به چالش‌های اسرائیل و آمریکا در حمله به ایران
🔹
دنی سیترونوویچ، رئیس سابق میز ایران در موساد: اسرائیل با دوراهی سختی روبه‌روست؛ یا واکنش نشان دهد و خطر درگیری مستقیم با آمریکا را بپذیرد یا عقب‌نشینی کند و به ایران اجازه دهد معادلهٔ جدیدی شکل دهد
🔹
رابرت پیپ، استاد دانشگاه شیکاگو: آمریکا و اسرائیل بدترین دام تشدید تنش از زمان ویتنام را راه انداختند؛ ایران قوی‌تر شده و این یک شکست بزرگ برای آنهاست.
🔹
هری سیسون، فعال رسانه‌ای آمریکایی: ترامپ دوباره در صحنهٔ جهانی تحقیر شد؛ او ضعیف است و نتوانست مانع اقدامات اسرائیل شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/440704" target="_blank">📅 13:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440703">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de135c17d6.mp4?token=Og_HlXV-LiZjc2HYbD7r8h-vDlsQat9Me-Xg_OK3R1hgka1PvpxfoXCux4tEITJYcjNZH4nt5RjgAQ01Krc65cpU1c1ji4N6wANN_IF95xegFTk1NVxX6olFdqOHdbdyNlrT71vLvuZ8lcYzuI0Ch4ThFGtzng7vj1OCF8hhwgpWyokcr3w1uUMczndXjRWK3SXvDqYr7cnBehp_bJl5_u2ucxTsCNJPKNgXONK2SWsKjiweFd7qm8hXgKZ-lp7ERNbWuQ0fV2ggJob-VT-YKr3ZSSpS-PETr9P_p7EopT4iQSz4KRwmUu1Aikzmdh2RCDhzqjEud890Xy8HPd5HOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de135c17d6.mp4?token=Og_HlXV-LiZjc2HYbD7r8h-vDlsQat9Me-Xg_OK3R1hgka1PvpxfoXCux4tEITJYcjNZH4nt5RjgAQ01Krc65cpU1c1ji4N6wANN_IF95xegFTk1NVxX6olFdqOHdbdyNlrT71vLvuZ8lcYzuI0Ch4ThFGtzng7vj1OCF8hhwgpWyokcr3w1uUMczndXjRWK3SXvDqYr7cnBehp_bJl5_u2ucxTsCNJPKNgXONK2SWsKjiweFd7qm8hXgKZ-lp7ERNbWuQ0fV2ggJob-VT-YKr3ZSSpS-PETr9P_p7EopT4iQSz4KRwmUu1Aikzmdh2RCDhzqjEud890Xy8HPd5HOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
🔹
یک منبع آگاه نظامی به فارس خبر داد ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/440703" target="_blank">📅 13:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440702">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU0rpkZmYssXr9cvdhCD_n4ZkHrdmZ4fwF_jvoxyw-wq9BIVmrokyrbz6FIY3HTUOoqkiH-TiP0nrOx6KalPw-G29hn7O8XdO1y0YCrJQ76-bTDl-2kqRqluXTye7o8LbZTTB8jW2uMJPiIU7VfBMAroku9l-BiOLC6tYR3Lziir0sJXQEI7hbABciUE2UtWswyKffkJaynwgKPitopaaSpBOaefbHdiH8fpAbuZA3tk4dFVkuHnH5bUTkcXDeBd2y0h2cxYbHYMXcPAB0G2H6N7mzPmMIp2P8WwFbJgNXJRtlBxV0A-32uvuJWPHiew7tRfDGwV508aja6ZU26oKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی مجلس: تا لحظهٔ پشیمانی دشمن سکوت نخواهیم کرد
🔹
نباید دچار ‎خطای محاسباتی شد. راه آرامش و ثبات از درون جنگ می‌گذرد. اگر خودتان را برای پاسخ قاطع به دشمن آماده نکنید جنگ درب خانه‌تان را خواهد زد.
🔹
نیروهای مسلح ما پس از سکوت صحنه نبرد، بر قوت‌هایشان افزوده و آسیب‌هایشان را هم برطرف کرده‌اند.
🔹
ما قوی‌تر از نهم اسفند آماده پاسخ هستیم و تا لحظهٔ پشیمانی و تغییر محاسبات ذهنی و ادراکی دشمن سکوت نخواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440702" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440701">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWP7v6P8zxWiOIA4TSMu1KwCV7aE-1xtrWa0agxVkRQPOoV-l8YVcYTNsWcBaHS6QztjUBQ2yYh1Keexds7Z2v-XVfulgCIMH7AWVAeW__DiBD3roOnE4VBr-KGVV7PNk-355gEPiMyv0sMCbUdK6GN_GFNeXmoGAVDUeirHts9itJXYVmbMeKyyB2-z6K3wdYbXC2ZITJUQ-vnIF1IL40vQQVaGf2I_DOkAVyfDrmPHQajdBFFMFED6apCO0Ebkd58SCj4p0yPbNckI6OIEhzctld6MKG3xFP2uaJHVg6LJwWIPEBuGPgFU3ca3ekt8kS-UPKXU0gqddyj_YEqO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: پشتیبانی از نیروهای مسلح با قدرت ادامه دارد
🔹
سردار ابن‌الرضا: رژیم کودک‌کش صهیونیستی امروز بیش از هر زمان دیگری به افول و فروپاشی نزدیک شده است.
🔹
تا زمان تنبیه متجاوز، لحظه‌ای از مسیر دفاع از منافع و امنیت کشور عقب نخواهیم نشست و تمامی ظرفیت‌های دفاعی و پشتیبانی در خدمت نیروهای مسلح قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/440701" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440699">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837911a19e.mp4?token=ZxIuwbe6UIlzbInrkaLpGTFjc_757bU3w-5ciPScrdHLhctyWRdQeCqfHxgrerDWDXjihpODsQpXhaoeLc1gLj_mxtYqcakXAYI-8Ws0gQ-0TNNdMBRCBdv8tTmKSN2KCnUiUIoTLfN81nA-86e6gy6JuG0V1FL9Rmu4M5tpWmdFGWG9hrUj4g9leBT9GO_HoqSkUCzrjDwD9dR-0fNqlBLO9L1IUr9RNYBK7WevRPTEIikIr7A8qDyNBetdhOJxmkfpYZ0VILUTWMXsEYpD0CxaLzTyqHbK2yBZiBkgQRZ9e17YfiZ1rRfZxaHGA0hsJJPzG1B8BsQ2txiEXDhMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837911a19e.mp4?token=ZxIuwbe6UIlzbInrkaLpGTFjc_757bU3w-5ciPScrdHLhctyWRdQeCqfHxgrerDWDXjihpODsQpXhaoeLc1gLj_mxtYqcakXAYI-8Ws0gQ-0TNNdMBRCBdv8tTmKSN2KCnUiUIoTLfN81nA-86e6gy6JuG0V1FL9Rmu4M5tpWmdFGWG9hrUj4g9leBT9GO_HoqSkUCzrjDwD9dR-0fNqlBLO9L1IUr9RNYBK7WevRPTEIikIr7A8qDyNBetdhOJxmkfpYZ0VILUTWMXsEYpD0CxaLzTyqHbK2yBZiBkgQRZ9e17YfiZ1rRfZxaHGA0hsJJPzG1B8BsQ2txiEXDhMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
🔹
یک منبع آگاه نظامی به فارس خبر داد ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440699" target="_blank">📅 13:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440698">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1934e5bb.mp4?token=Lm-ZCElchxC38sJBkS9DSlEqxtIZN_Y7O0gXYPqRmOY1GogELeV7PNIqUm2BhQpMYb2Hy_iX5v8acHC60BfK2eIy7MKY76ZiPXvTD1aXoT5QVlqet_ir_WMXUzkbe7yZXXOBtdPGW7PeMqJcTgHvnWnrU4cn41YgVXGseZM7Yo4RQ_6cLGbJ0ZrhO_qDOEm5X5BYSgIkB2-rijQqcGW2ZYa-ERTTBj0fCpK1_VfCbSZ8kbBoBgXrU9IBi58hrXLQfE_26CRoR_0131L7lURs25G25P5qIrIU7I3fH1e6e93x6hhtJhlny61Oj-LILcxL-aHltTf9vRQF4kPeZ2uh7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1934e5bb.mp4?token=Lm-ZCElchxC38sJBkS9DSlEqxtIZN_Y7O0gXYPqRmOY1GogELeV7PNIqUm2BhQpMYb2Hy_iX5v8acHC60BfK2eIy7MKY76ZiPXvTD1aXoT5QVlqet_ir_WMXUzkbe7yZXXOBtdPGW7PeMqJcTgHvnWnrU4cn41YgVXGseZM7Yo4RQ_6cLGbJ0ZrhO_qDOEm5X5BYSgIkB2-rijQqcGW2ZYa-ERTTBj0fCpK1_VfCbSZ8kbBoBgXrU9IBi58hrXLQfE_26CRoR_0131L7lURs25G25P5qIrIU7I3fH1e6e93x6hhtJhlny61Oj-LILcxL-aHltTf9vRQF4kPeZ2uh7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
دادستانی کل کشور: انتشار هرگونه محتوایی که به تأمین اطلاعات موردنیاز دشمن یا تشویش افکار عمومی منجر شود، طبق قانون تحت پیگرد قضایی قرار خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440698" target="_blank">📅 13:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
انهدام پهپاد دشمن در غرب تهران
🔹
پیگیری‌های خبرنگار دفاعی فارس نشان می‌دهد پیش از ظهر امروز دوشنبه یک پهپاد متخاصم در غرب تهران توسط رینگ پدافندی پایتخت رهگیری و منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/440697" target="_blank">📅 13:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440696">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6qKRumJWW_cdKRewSn7PlgltKjn-jGbnIpA3t4uMnyYSO3jh4O8wuetdkuf2bvscajqM3FpMggYeJfWSqDQowJOvjLGW42SIYRVEsaSrZCKFyRLNmn6viwbW3VmzPrGsDkBrM9-CWwV6MPlsBi3tejanqo7TnS4pf8duiKDpQEwv2yeJFA5blbyFz1UqSkO0Llrp1zIxtB20VNsh9EzXwxFWdwXagijyTGhKjMDMl0gZu9sJM_n2AUYGLwZZqS-jo3web-iMgdBvZiU31CWuy8ZMqTS13V_J9lOxk4B25YZ-0OjNefnjsVyzucAE5-O0voSiPOjE3UihVrSdbEMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و ایران باید فوراً «شلیک به‌سمت همدیگر» را متوقف کنند.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/440696" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440695">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9OJAtsPMX3f-_F4iwalZoFbz86XFYp3WduylvuP3VhVcSttGbE8WKovWKvFZ69NoDCLqTYTKzyw5Fv0F0m1mebhzRdhTxV5XlSiLL4tIzo-ImPFMjxeRFGIH_0fZCw6mEzq1UqjzysPYgJ32Oybo180G0NpCR2jCnAdEshbLw9JcgSRNGxALTQdKQQHqBkD0EkmVjnEFNhS8b4XEQzWwKgTJAM7bipkRLmbgloJmMw7A_zuzgKC1GYI8s6xOylPpcYVUWR1HZKgZ5K_lqqp-TccVxj61rF6XdmUHltShgFyCnLuv7N148Bz-WC9QEB3N6n1ho22oeDAC1_YO9GJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس مجمع تشخیص مصلحت نظام: تهران فصل تازه‌ای از سیاست دفاعی خود را گشود
🔹
حملۀ ایران در دفاع از لبنان، صرفاً یک پاسخ نظامی نبود؛ بلکه اعلام رسمی یک دکترین راهبردی بود.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/440695" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440694">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
دادستانی کل کشور: انتشار تصاویر و فیلم‌ از محل اصابت پرتابه‌های دشمن جرم است
🔹
با عاملان انتشار این تصاویر برخورد قاطعِ قانونی صورت خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/440694" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440693">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
دادستانی کل کشور: انتشار تصاویر و فیلم‌ از محل اصابت پرتابه‌های دشمن جرم است
🔹
با عاملان انتشار این تصاویر برخورد قاطعِ قانونی صورت خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/440693" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe2032c8e.mp4?token=u01zHdrqU2Dtl-DnSrO-AjfAD1DSxGi793UprJSlJfUKO0RwHibnMCrMqdsmWe5vn9NpnU_G3gUOxyansQAv81j3_MdqSEjcr6HmtIog6LjKXJMTcHWTsoNYCJmJeMp9uy-r4x4DFo5I2PrGvp7TKL4kBWdmitlk6Nau7s1PPhtWa-BRNismbyWbxc71LH_n2-jgk_ikVwjl_fJd6UOXtgo7pECrCSzj54gzXXVInmEd7QSgNuEa7hTLPHvy30iB25G04CQnm9-qXpiCtZwuPfHoDnhMdee3treDwAT4NKkzGiQQITly8XVUKUJFhLyiP0Hdpak-UJj3DO-r-KoJRi8EhH2-FoKqVqR7jPb9ZoJsQyJSgmTnfbuu4Sw6vjtQxvulhv25vzIXokCMNAsQpO5csyiqm8NNv6LU9NWgwo_wfR6yu10AeqMUn8fdDp1c4N7zi-AzpeueJ0KOeQLtXKqiUSZQfa3nEBXVup5DfmpxZTlsCCaQSLb0FdTysDEfW-haFcS69RjsACEkBF2-lQmNXwmlcDY-nHB8tJNwBcSvFjaMjj1KbbwQ9_q3eR76LpKK9ifh0qflOFa9iaIdVbNShp6S5_Od9YWvAxmQUwM5RgAHMMVp_y494APDaqlvz0_CAoTOToFARZa-MHM_WlZfunYAUkaN9vqaVpkBZRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe2032c8e.mp4?token=u01zHdrqU2Dtl-DnSrO-AjfAD1DSxGi793UprJSlJfUKO0RwHibnMCrMqdsmWe5vn9NpnU_G3gUOxyansQAv81j3_MdqSEjcr6HmtIog6LjKXJMTcHWTsoNYCJmJeMp9uy-r4x4DFo5I2PrGvp7TKL4kBWdmitlk6Nau7s1PPhtWa-BRNismbyWbxc71LH_n2-jgk_ikVwjl_fJd6UOXtgo7pECrCSzj54gzXXVInmEd7QSgNuEa7hTLPHvy30iB25G04CQnm9-qXpiCtZwuPfHoDnhMdee3treDwAT4NKkzGiQQITly8XVUKUJFhLyiP0Hdpak-UJj3DO-r-KoJRi8EhH2-FoKqVqR7jPb9ZoJsQyJSgmTnfbuu4Sw6vjtQxvulhv25vzIXokCMNAsQpO5csyiqm8NNv6LU9NWgwo_wfR6yu10AeqMUn8fdDp1c4N7zi-AzpeueJ0KOeQLtXKqiUSZQfa3nEBXVup5DfmpxZTlsCCaQSLb0FdTysDEfW-haFcS69RjsACEkBF2-lQmNXwmlcDY-nHB8tJNwBcSvFjaMjj1KbbwQ9_q3eR76LpKK9ifh0qflOFa9iaIdVbNShp6S5_Od9YWvAxmQUwM5RgAHMMVp_y494APDaqlvz0_CAoTOToFARZa-MHM_WlZfunYAUkaN9vqaVpkBZRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چاقوکشی در نیویورک در آستانه حضور ترامپ
🔹
درپی حمله با چاقو در ایستگاه پن نیویورک ۶ نفر زخمی شدند. این حادثه نگرانی‌های امنیتی را در آستانهٔ میزبانی نیویورک از بازی‌های فینال NBA که قرار است ترامپ هم در آن حضور یابد، افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/440692" target="_blank">📅 12:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440689">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
سپاه: تجاوز دشمن به صنایع پتروشیمی را پاسخ دادیم
🔹
سپاه پاسداران: رزمندگان نیروی هوافضا، در پاسخ به تجاوز دشمن آمریکایی‌صهیونی به یکی از صنایع پتروشیمی، دقایقی پیش صنایع مشابه در حیفا را هدف حمله موشکی قرار دادند.
🔹
اخطار می‌کنیم؛ دشمن صهیونیستی با اقدام…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/440689" target="_blank">📅 12:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440688">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af6ca7cd0.mp4?token=s9zStDfeWWpl4fJBol1fhYJYBmyxCSxyuEteWQE5wHISlRJnt3uovbx9qUD7eGhzOd4fFiYVSA2gbGDElp6FsUT9_jv8C5B_7qNkPpBIVUbGY0RVSj2BP3axcCcU8uz2qAz0wCXqsdGyucMZeudauPddregLXrfAeob7vuj0VCZAStTJF9jeY57R_I7K8XpRFd1MNmZCKJanWaPu0QMnZO3nwBzZ5jWHImML5DONlSS605AcrJEg1QQx3ndxctJ8IyqKUd4UV2smpadabJOPswxVn-lY2SvEn6XACeOqpKxuoax_GPTMihmZclZ1O70O8sYVeW1cWoGWOcdAkxlAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af6ca7cd0.mp4?token=s9zStDfeWWpl4fJBol1fhYJYBmyxCSxyuEteWQE5wHISlRJnt3uovbx9qUD7eGhzOd4fFiYVSA2gbGDElp6FsUT9_jv8C5B_7qNkPpBIVUbGY0RVSj2BP3axcCcU8uz2qAz0wCXqsdGyucMZeudauPddregLXrfAeob7vuj0VCZAStTJF9jeY57R_I7K8XpRFd1MNmZCKJanWaPu0QMnZO3nwBzZ5jWHImML5DONlSS605AcrJEg1QQx3ndxctJ8IyqKUd4UV2smpadabJOPswxVn-lY2SvEn6XACeOqpKxuoax_GPTMihmZclZ1O70O8sYVeW1cWoGWOcdAkxlAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ خواهران منصوریان به رئیس فدراسیون ووشو
🔹
فدراسیون ووشو در بیانیه‌ای اعلام کرد که پس از شکست سهیلا منصوریان مقابل رقیب خود، خواهران منصوریان به رئیس فدراسیون ووشو حمله کرده، به او توهین و اقدام به خودزنی کردند.  @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/440688" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440687">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch-s73nTkup-Km7IRgUkOA0JqS3IzOLTYWfe85jkN6oYiL0YS5d5IhuGnaAoA-uDBOOse0fG7twcvyxWXN62RodWGnVRIZrdrplIl95OH89Dr63NlAW7BWEwdqCgGwWjJUTbRaFW_z_SYtX9RSc52yZbT2o8qZjXrMOXbmapCGS-p5fX7nwy7MWBb3hZklK9338Az3V3xJBIWmsfrR-EJs1RE6SRdXeWEp4Lm0hAha5rv6YIfHnddomkIDFF4i_Mpu2cTPDeV9T0VXJA6lHHtWvaDc0-k3lHmc4k2nzogLAZCaEcXyVmXjcQgW-ox-OIQFGRZkxLoJ5g30ar-mF9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت عادی شعب بانکی ادامه دارد
🔹
رئیس شورای هماهنگی بانک‌های دولتی: با وجود تنش‌های ایجادشده، شبکهٔ بانکی کشور با آمادگی کامل درحال فعالیت است و هیچگونه تغییری در روند کاری بانک‌ها و شعب بانکی در سراسر کشور ایجاد نشده است.
🔹
در صورت تغییر در ساعت کار بانک‌ها در روزهای آینده، شورای هماهنگی بانک‌ها اطلاع‌رسانی لازم را انجام خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/440687" target="_blank">📅 12:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440686">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6142cc848.mp4?token=iBuN1VT7wRhcSA9wpVeakikYFvYlLyTU5lL2Tycvt8TWmbicafkmNjmOSbqpEK9cYUD6_nxF4s4laUXkdPJ2gf8m-WBUDxxCt-dExuIXcKmD37-I6SIvyaxLBomJuaME0-w9PEFhccXBlrX8OSM-G1sJor7zDN4vOpiA0QK6ey5KBA9_g9uzlCau_vNZ3czb5vBj985h8-iB4szbkIyF83xF4acqvPXf6v8_aUo0ab2GWcsbX3YaeXAXPAkIv2vUfUCtP9oUIvuFFNfddcuLDp3qZmws7fLN1upyjZOTYJf3qIAhBZPj3YFsPVmEhS36nuSv3TOGSs0dhbGusBUceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6142cc848.mp4?token=iBuN1VT7wRhcSA9wpVeakikYFvYlLyTU5lL2Tycvt8TWmbicafkmNjmOSbqpEK9cYUD6_nxF4s4laUXkdPJ2gf8m-WBUDxxCt-dExuIXcKmD37-I6SIvyaxLBomJuaME0-w9PEFhccXBlrX8OSM-G1sJor7zDN4vOpiA0QK6ey5KBA9_g9uzlCau_vNZ3czb5vBj985h8-iB4szbkIyF83xF4acqvPXf6v8_aUo0ab2GWcsbX3YaeXAXPAkIv2vUfUCtP9oUIvuFFNfddcuLDp3qZmws7fLN1upyjZOTYJf3qIAhBZPj3YFsPVmEhS36nuSv3TOGSs0dhbGusBUceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از تنگهٔ هرمز
و کنترل ایران بر این آبراهه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/440686" target="_blank">📅 12:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440685">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پروازهای فرودگاه هاشمی‌نژاد مشهد لغو شد
🔹
سخنگوی فرودگاه‌های خراسان‌رضوی: با توجه به شرایط پیش آمده کلیه پروازهای فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد لغو شد. @Farsan - Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/440685" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440684">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIQz8N418-g-aBFEaYPTlNsCQzfEV6famFjour-ZzZUQZhEUEDZSAPuL-BbM_m90snYUCxGg58cyT7QUU8o4b7hdpetiW9Ohk-ftQ6akQ6w8k8CTODAXgalpOXvQND1uLHut5b3DLK26Rloc8OClgIXqoD2u36YJYdZJEU78ixsmmvMVzs3WPpMaxFm3Nrj1MbIikjV_i1sUY6DNHh7FEmdv7DwggCLoG8LZNATIcQSpg1lbhDxYU9xQJO25eW903BiVsFJRe3-alZCOFYO0628qu52ib4bd8YWbGPklBSk5tQRUJrv-WiEQYrue_7cpNB4RzaMMdnmrPivSZ9Vlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش الجزیره از سانسور نظامی در اسرائیل پس از حملات ایران
🔹
در پی حملات موشکی ایران به اراضی اشغالی از شب گذشته که در پاسخ به تجاوز رژیم صهیونیستی به بیروت و نقض آتش‌بس انجام شد و امروز ادامه داشته، شبکه الجزیره در گزارشی از اعمال سانسور نظامی گسترده در اسرائیل خبر داد.
🔹
به گزارش خبرنگار این شبکه، ندا ابراهیم از رام‌الله در کرانه باختری اشغالی، به‌طور کلی در اسرائیل بر این موضوع تأکید می‌شود که در گزارش‌ها اعلام شود ارتش تمامی موشک‌های شلیک‌شده از ایران را رهگیری کرده است.
🔹
با این حال، به گفته او، تعدادی از رسانه‌های اسرائیلی از خسارات در برخی مناطق، از جمله در حمله نخست دیشب خبر داده‌اند؛ اما ارزیابی کامل تأثیر این حملات و میزان خسارات به دلیل سانسور خبری همچنان دشوار است.
🔹
در این گزارش همچنین تأکید شده که در اسرائیل سازوکاری تحت عنوان سانسور نظامی وجود دارد که از انتشار اطلاعات حساس در رسانه‌ها جلوگیری می‌کند؛ از این رو، برآورد دقیق میزان خسارات ناشی از این حملات همچنان با ابهام روبه‌روست.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/440684" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440683">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEpaSgn092HB3gFHslxV3k2RAgkoZ5CRbRJgsOJaVjnDRNQqgq5m5_-aI3U97BVfJmwiWp2dn66uKERBkFHREtRIA_BMqrLv6oa0OHh9eNC_lXsnDcofD0UlTygDS-bTvg1vXqRE2kycQII69ioaselXFtoMZFVwZFs5G3eULhC7WfnmNN0HzhqFtBNhIN7Z3Y8EPoJu_CEJe2LrSuammrkDvmcMRpEHqyi_R3W7QiVZlFfYXqKMBQHEA64Dgn3xowQdzFT9yCLSVqPdnXFwn9_kJvoSuwHJNkj8j39OzliTlyqVksbkLacz9WkIVlFHro4ZZMCSnaxvD7k4fBhBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‎ حمایت دولت از رایگان‌شدن مترو و BRT در تهران
🔹
معاون اول رئیس‌جمهور در دیدار با شهردار تهران، رایگان‌سازی مترو و اتوبوس‌های تندرو را اقدامی مهم و قابل تقدیر دانست و گفت این طرح می‌تواند به کاهش آلودگی هوا، ترافیک و مصرف سوخت کمک کند.
🔹
عارف: درآمد حاصل…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/440683" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440682">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7rPdGdi5wddg4zsAr3ccwoxb8TD9ez1d58nGn8E9zWTfyBGve3O-IGDCcLqqvydMMmOkXrpFGJK1WA6ICZoyaieJjqPsgY68dKzGVYosdSogbzBknd6eEABzwuyTu4PBCORht4-_Oni6FnX3yBz69T_5vSTh-9RXaqszz5DGqiRtRc5ulqIL00MPWndHDTviXYdYl7Y98wifAzwseM83Ukwr8C6Bw6bwPTGBvdBboNbeZY2QP8rAaHgGBtcppnGJp4QzD6LUmKeYyGIibqSM6lR2XyRTNpdXuRJP5-zPhO6NhJuHPtxyE-1zHuJrNgxpW9EEVrkdI0LezJl3yG-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۱۰۰ شب مقاومت، ۱۰۰ سال امنیت
🔹
سازمان اطلاعات سپاه: اطلاعات میدانی از ضربات شدید و سریع نظامی، امنیتی و سایبری دیشب به سرزمین‌های اشغالی و نشان‌دهندۀ موفقیت ۱۰۰ از ۱۰۰ است.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/440682" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440681">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اعلام زمان شارژ اعتبار مرحلهٔ سوم حمایتی از کودکان دارای سوء‌تغذیه
🔹
معاون اقتصادی وزارت رفاه: اعتبار مرحلهٔ سوم طرح مذکور از امروز به حساب سرپرستان خانوار دارای کودک ۵ تا ۵۹ ماههٔ مبتلاء به سوءتغذیه، تخصیص خواهد یافت.
🔸
بر این اساس، به‌ازای هر کودک در خانوارهای با وسع اقتصادی پایین، مبلغ یک میلیون و ۳۰۰ هزار تومان و برای خانوارهای با وسع اقتصادی متوسط، مبلغ ۸۰۰ هزار تومان تخصیص می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/440681" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در غرب تهران
🔹
هنوز محل دقیق و منشا این انفجار مشخص نیست؛ همزمان پدافند هوایی در برخی نقاط تهران نیز فعال شد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/440679" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e4a03961.mp4?token=DifpPB5a8IBkih6ORdU4okSfJ0F7-lwTiguM2R8-sx_FMQipN4uRNwdloEbEcIdpBesCCro8BHZX739ygDKiY-PRrCJYWvYFBWBM2sYH5Eqs2qz6sGEN2xKmlCUKgHKv9KL1lyH5I_jZX1YMvnB4zL8_gsxPZTts49Ah1qLE6S_uBdtzQBTf-Zh-rVM2H8D6jwTtj8CboQc_NDFPc0OetE1aWrKOwQzly2cCrW3p3eNZmRT-xybrtW24_CIVdpSGabY8ysPpFVEsRV7zUbDBbQacCteboGoxw4xBiWGm0jX1VgTmWEnhecFQSiN2Eg6i_o9lHTL8-S6bydl9FeMMQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e4a03961.mp4?token=DifpPB5a8IBkih6ORdU4okSfJ0F7-lwTiguM2R8-sx_FMQipN4uRNwdloEbEcIdpBesCCro8BHZX739ygDKiY-PRrCJYWvYFBWBM2sYH5Eqs2qz6sGEN2xKmlCUKgHKv9KL1lyH5I_jZX1YMvnB4zL8_gsxPZTts49Ah1qLE6S_uBdtzQBTf-Zh-rVM2H8D6jwTtj8CboQc_NDFPc0OetE1aWrKOwQzly2cCrW3p3eNZmRT-xybrtW24_CIVdpSGabY8ysPpFVEsRV7zUbDBbQacCteboGoxw4xBiWGm0jX1VgTmWEnhecFQSiN2Eg6i_o9lHTL8-S6bydl9FeMMQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: هیچ مذاکره‌ای دربارهٔ ذخیرهٔ اورانیوم ایران انجام نشده و اخباری که دربارهٔ آن منتشر می‌شود صرفاً گمانه‌زنی رسانه‌هاست.  @Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/440678" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
یک منبع آگاه: در صورت خطای مجدد، زیرساخت نفت و گاز منطقه هدف قرار می‌گیرد
🔹
یک منبع آگاه نظامی به فارس اعلام کرد، در صورت ادامهٔ حملات به زیرساخت‌های انرژی، کلیه تاسیسات نفت و گاز مرتبط اسرائیل، آمریکا و هم‌پیمانانشان از جمله تاسیسات انرژی منطقه‌ای هدف نیروهای مسلح ایران است.
🔹
این منبع شرکت‌های نفتی و حوزه انرژی در منطقه که سهامدار آمریکایی یا صهیونیست دارند را هدف مشروع ایران دانست.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/440677" target="_blank">📅 11:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7fc74cda.mp4?token=deXxcsPrewVNEjrI7LluVicpq4YNH4STOvVVEkziQzprRPvxA2wnwNCVAvXLPr5f9iWlJY0rlEU8QrhRcK7NTZeQRlwLEIRAvbIp4i8Jynnk4DH5F7nVdp3ufVIknEV5PjDjretjVBUztZ1Zu83fOjET6yTY_n6WMF3Djy3rD5swnfGBso81UviVw6G0bj9WjjkuaDfXzNpGexqteV4iirdk1ZpG-BQ8FzFBswfgOUajHn0EUIOtji2WNgIiiIoLJ6WJNWFcWIKJ7XZ5VUh7b4Vp3pOAuNa2AA397V9HsofrC4aKQa7QfbIOBDC-yLkXUTM_zbegsAPnJzgP38vaZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7fc74cda.mp4?token=deXxcsPrewVNEjrI7LluVicpq4YNH4STOvVVEkziQzprRPvxA2wnwNCVAvXLPr5f9iWlJY0rlEU8QrhRcK7NTZeQRlwLEIRAvbIp4i8Jynnk4DH5F7nVdp3ufVIknEV5PjDjretjVBUztZ1Zu83fOjET6yTY_n6WMF3Djy3rD5swnfGBso81UviVw6G0bj9WjjkuaDfXzNpGexqteV4iirdk1ZpG-BQ8FzFBswfgOUajHn0EUIOtji2WNgIiiIoLJ6WJNWFcWIKJ7XZ5VUh7b4Vp3pOAuNa2AA397V9HsofrC4aKQa7QfbIOBDC-yLkXUTM_zbegsAPnJzgP38vaZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: حمله‌ای به عربستان انجام نداده‌ایم.
🔹
نیروهای مسلح ما به هر هدفی حمله کنند، آن را صراحتاً اعلام می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/440676" target="_blank">📅 11:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440675">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حریم هوایی عراق به‌مدت ۷۲ ساعت بسته شد
🔹
سازمان هواپیمایی کشوری عراق با صدور پیام ناوبری (NOTAM)، حریم هوایی این کشور را به‌دلیل ملاحظات امنیتی، به‌مدت ۷۲ ساعت به‌روی تمامی پروازها بست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440675" target="_blank">📅 11:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440674">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd7978d06.mp4?token=bhHagxE_QsU584kkvccHnjbHSpcIUzidrywmZkF3WEolBbdX6fCuK6JVxshLtoal01THKkdfKY33tDW49flZgeEVT46Sa3AsV759dS4Lb_i3HXOsApikC_-6yGNCqO54VNyx9SyMAsFaATbeAsILllS071SqSAoluYqPi0u18wqMLLnfwlKkV3Jp5K-Vi3CRqR_57ldUd0ZWcFUEW96VhJ7BUXIcVfnUTec3R9Xsg3HhN2MiMKBeEeIKCQMtg_4eSq2ihisJz6H1Qs00sin6kxDT4pT7fbxI2pcM87LvBsZv9hl0vNSMIoikS47M3zpyjXEizRTFnOzV8g6paMzKDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd7978d06.mp4?token=bhHagxE_QsU584kkvccHnjbHSpcIUzidrywmZkF3WEolBbdX6fCuK6JVxshLtoal01THKkdfKY33tDW49flZgeEVT46Sa3AsV759dS4Lb_i3HXOsApikC_-6yGNCqO54VNyx9SyMAsFaATbeAsILllS071SqSAoluYqPi0u18wqMLLnfwlKkV3Jp5K-Vi3CRqR_57ldUd0ZWcFUEW96VhJ7BUXIcVfnUTec3R9Xsg3HhN2MiMKBeEeIKCQMtg_4eSq2ihisJz6H1Qs00sin6kxDT4pT7fbxI2pcM87LvBsZv9hl0vNSMIoikS47M3zpyjXEizRTFnOzV8g6paMzKDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: به‌عنوان دوست لبنان هر اقدامی که بتوانیم برای کمک به صیانت از حاکمیت ملی این کشور انجام خواهیم داد.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440674" target="_blank">📅 11:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440673">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc4d44e05.mp4?token=ouFRQtWa2aWmMxZChv5jVvOusUmwqFyvjJ-Zpo3ZgOZ4Kxco56AmqAz4IT8-dKBSHumNecYnuoNR_CQgjNTtxAg5a6EQunGCUdnEUHpgbz_590hjNudTrwGXGuU-NrGoOIRABXEMBQgDNoAQ0UsMx6mKuS7XnJs5aiNa6B-CIrNb_PBaEqDnieUJxHTPNElizYKWvcHwPDuhh-T2HhKj1AmSnxG1ot5Ay5QvMnkdC-c6zNUn2f8dyRlTEByyuQbRw72vMieHYiLx7gUA1gpSsxr-mFBXArYjyN0uJHKRgDXwswNMLVG5ydW9ZJ53xjcpMPgFnUanoefbs-Ietiam2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc4d44e05.mp4?token=ouFRQtWa2aWmMxZChv5jVvOusUmwqFyvjJ-Zpo3ZgOZ4Kxco56AmqAz4IT8-dKBSHumNecYnuoNR_CQgjNTtxAg5a6EQunGCUdnEUHpgbz_590hjNudTrwGXGuU-NrGoOIRABXEMBQgDNoAQ0UsMx6mKuS7XnJs5aiNa6B-CIrNb_PBaEqDnieUJxHTPNElizYKWvcHwPDuhh-T2HhKj1AmSnxG1ot5Ay5QvMnkdC-c6zNUn2f8dyRlTEByyuQbRw72vMieHYiLx7gUA1gpSsxr-mFBXArYjyN0uJHKRgDXwswNMLVG5ydW9ZJ53xjcpMPgFnUanoefbs-Ietiam2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: از آغاز آتش‌بس خویشتن‌داری فوق‌العاده‌ای نشان دادیم
🔹
ما با نقض‌های پیاپی آتش‌بس مواجه بودیم و حملهٔ دیشب ما یک اقدام دفاعی قانونی بود. اظهار بی‌اطلاعی مقامات آمریکایی از حملهٔ دیروز به ضاحیه نشان می‌دهد که نوعی تقسیم کار بین آمریکا و…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/440673" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440672">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdca724ace.mp4?token=Ih7Ibj217_5PR2QErbs1cyrweL9vz40Ty3qu-ZOAeppmztZl9n-rGCZ45ePlN2BEFLJ1jKjkkKJW3w5FCiRnm0kYM_bPki68CI9wq7B4-haOdFKU7Ip1vWISvhBjHTSpXtBAYcgpxHGkRJQxxuUvUw1q0Zm_d3gWPc-d5gzFE5Jm0-n6KcRDIIMMNVDf6GxHLaV2s1iiyKuhvYIibl3UE7u9i6kaIq5UmWtxQeTacYsQtcnKAVofU5AE_sT8OwyyiTT3Zj8bv3LKjfZFHzDtx_Qf3-ntZpRLMyOmvqB0OPd20W-9p58c3RMjWVLGsgDfOQv1qMcQrqpPOqnl1M2dLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdca724ace.mp4?token=Ih7Ibj217_5PR2QErbs1cyrweL9vz40Ty3qu-ZOAeppmztZl9n-rGCZ45ePlN2BEFLJ1jKjkkKJW3w5FCiRnm0kYM_bPki68CI9wq7B4-haOdFKU7Ip1vWISvhBjHTSpXtBAYcgpxHGkRJQxxuUvUw1q0Zm_d3gWPc-d5gzFE5Jm0-n6KcRDIIMMNVDf6GxHLaV2s1iiyKuhvYIibl3UE7u9i6kaIq5UmWtxQeTacYsQtcnKAVofU5AE_sT8OwyyiTT3Zj8bv3LKjfZFHzDtx_Qf3-ntZpRLMyOmvqB0OPd20W-9p58c3RMjWVLGsgDfOQv1qMcQrqpPOqnl1M2dLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تبادل پیام‌ها متوقف نشده بود و حضور وزیر کشور پاکستان هم بخشی از این تبادل پیام‌ها بود.  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/440672" target="_blank">📅 11:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440670">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b45b849b.mp4?token=ESpyaLMIro-2zbOXgaWAKqjwZzhgX64PI6GsEroohfNurPmFp1zU7ifRxdV9eJW5r3xsPGjoJzhJult_hy3ge2xmICCqFTz3eWR4Rp4cgaOrdHCnX1Ci0L0cVlRGCN4j6Gw2fDkIs1zXtAoM24oSAvCSOS3bGDFam1CQv6iigrlMzzr3KeFQiVwMxXMxleT_FltfbtXwUzBPmHYPVYEKjTQGB2CSCtgSlQh-jhJTnR_EyyTwQ0YVen-_kau6uKKb9UtdywqEV-MitlRBk5ImDWK4W7QaJzpzw6mRSmdM3h-nX8uqubqna-kVKTL3r8X-NcuUsii7A6uUD8YSn6SPnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b45b849b.mp4?token=ESpyaLMIro-2zbOXgaWAKqjwZzhgX64PI6GsEroohfNurPmFp1zU7ifRxdV9eJW5r3xsPGjoJzhJult_hy3ge2xmICCqFTz3eWR4Rp4cgaOrdHCnX1Ci0L0cVlRGCN4j6Gw2fDkIs1zXtAoM24oSAvCSOS3bGDFam1CQv6iigrlMzzr3KeFQiVwMxXMxleT_FltfbtXwUzBPmHYPVYEKjTQGB2CSCtgSlQh-jhJTnR_EyyTwQ0YVen-_kau6uKKb9UtdywqEV-MitlRBk5ImDWK4W7QaJzpzw6mRSmdM3h-nX8uqubqna-kVKTL3r8X-NcuUsii7A6uUD8YSn6SPnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ادعای ترامپ دربارهٔ آزادنکردن اموال مسدودشدهٔ ایران ادعای مضحکی است
🔹
ما از هر طرفی که نقشی در تجاوز علیه ایران نقش داشته طلبکاریم و این طلب را به هر نحو که بشود نقد خواهیم کرد. هر تفاهمی صورت بگیرد، آزادسازی منابع مسدودشدهٔ ایران جزوی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440670" target="_blank">📅 11:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440669">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8df649b271.mp4?token=Ze0siHXhpCPWwYBVGvXrA4L2vumptCAHmabtK8rlikilPeQP_3sDiXD6QAX42kn6ZfP3G4DmCgAABZvT1gm9My-jQQ27AjXeD5je8hf3u5Lwyzr0bw_uq_D1ZJ2ztkgCjIn_QS3v65a_gWOo8UElWlR2NHdq-jTAVYchrH8-3lt0P2PMmNWe8k-kWSmHqVqcjW_Pzsalfdu6B0H1tIplpPxVV8MZfcZ3S1ZtCLUGqrB4RRlfS7WOEr5FEtzM2C_NVCQ5ftiu4uD4jkdDRhg-KeZOzBxGojIcFP82QpygNyRbgKxM1T6t5qCGPRaZOeVIH2IpTchBtGGYo3iIg0HZAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8df649b271.mp4?token=Ze0siHXhpCPWwYBVGvXrA4L2vumptCAHmabtK8rlikilPeQP_3sDiXD6QAX42kn6ZfP3G4DmCgAABZvT1gm9My-jQQ27AjXeD5je8hf3u5Lwyzr0bw_uq_D1ZJ2ztkgCjIn_QS3v65a_gWOo8UElWlR2NHdq-jTAVYchrH8-3lt0P2PMmNWe8k-kWSmHqVqcjW_Pzsalfdu6B0H1tIplpPxVV8MZfcZ3S1ZtCLUGqrB4RRlfS7WOEr5FEtzM2C_NVCQ5ftiu4uD4jkdDRhg-KeZOzBxGojIcFP82QpygNyRbgKxM1T6t5qCGPRaZOeVIH2IpTchBtGGYo3iIg0HZAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: تجاوز دشمن به صنایع پتروشیمی را پاسخ دادیم
🔹
سپاه پاسداران: رزمندگان نیروی هوافضا، در پاسخ به تجاوز دشمن آمریکایی‌صهیونی به یکی از صنایع پتروشیمی، دقایقی پیش صنایع مشابه در حیفا را هدف حمله موشکی قرار دادند.
🔹
اخطار می‌کنیم؛ دشمن صهیونیستی با اقدام…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/440669" target="_blank">📅 11:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440668">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
🔹
معاون امنیتی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
📝
خبر تکمیلی در خصوص خسارات و تلفات احتمالی…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/440668" target="_blank">📅 11:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440667">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28575da85.mp4?token=uoyw8aHJ-N1e61w-Pf0A0Ag5OTodB2Uy1CLtTZC5idfRYYhTtr10zSbpnhlQlM1XABLQWZMC_PVDJhTYbOY-tYjRXUCHfAFh-FM3p14woFdPnELDsx5B0ii0-YSZUKQB8QF9_xKPT2lg1aHdUt0ZOGXSeBPNvSVfofVxRfpiU418-eO8YU_WGt8Ra-YuMvXtXDAMR-qOsrgsAARPmS05M0BpMY6sQwg_GaibYuCa2SDIJ5Grj6e50uT50Fodrrh9Exj7Vwi1J6DmETiFZlfRA9VW-UQsQRLl-XcFpwCb1RcM2GfF_QtikKCpBuwYrb70BrG9-vguX0XcTGxyxammcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28575da85.mp4?token=uoyw8aHJ-N1e61w-Pf0A0Ag5OTodB2Uy1CLtTZC5idfRYYhTtr10zSbpnhlQlM1XABLQWZMC_PVDJhTYbOY-tYjRXUCHfAFh-FM3p14woFdPnELDsx5B0ii0-YSZUKQB8QF9_xKPT2lg1aHdUt0ZOGXSeBPNvSVfofVxRfpiU418-eO8YU_WGt8Ra-YuMvXtXDAMR-qOsrgsAARPmS05M0BpMY6sQwg_GaibYuCa2SDIJ5Grj6e50uT50Fodrrh9Exj7Vwi1J6DmETiFZlfRA9VW-UQsQRLl-XcFpwCb1RcM2GfF_QtikKCpBuwYrb70BrG9-vguX0XcTGxyxammcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه خطاب به دولت مصر: ۳ سال برادران و خواهران شما در غزه تکه‌تکه شدند اما شما کاری نکردید
🔹
ما مشکلی با مصر نداریم؛ اما این که مصری‌ها بخواهند با تهدید یک کشور مسلمان تحت تجاوز رژیم صهیونیستی کسب اعتبار کنند، تأسف‌بار است. @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440667" target="_blank">📅 11:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdbbc4f19.mp4?token=IQfW-WVdAKK68PJ_jcHL6_6UIQCy3-OxgmVMcbfg-dqzKGnvOMztjj3CIlPTZ4O1VErygR461zUfuS5dp6vFMh6-RNFpxPJRqcaFQJrU1judhDjzaeAiL4J8RKlY29xPH0RW4b68F-uVq0UpXNhM9OMYv1zy3hEamalaPq5nhzFbvbTQnuuqy07F-kZ6DpeDzbzC_RGHCZ9bzgZpPH7G4DZK4DzR6tfRj9l58ur8LOQkXcNix6Db_tkiFLIeUikqTZzeT3a3HX4lgCAziW7f8lbQ1kFO8h7sqUP2MaDERonNFXj4Qow18vnpaM3bomlDngbad4BA5Rv0VSxA_HFeHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdbbc4f19.mp4?token=IQfW-WVdAKK68PJ_jcHL6_6UIQCy3-OxgmVMcbfg-dqzKGnvOMztjj3CIlPTZ4O1VErygR461zUfuS5dp6vFMh6-RNFpxPJRqcaFQJrU1judhDjzaeAiL4J8RKlY29xPH0RW4b68F-uVq0UpXNhM9OMYv1zy3hEamalaPq5nhzFbvbTQnuuqy07F-kZ6DpeDzbzC_RGHCZ9bzgZpPH7G4DZK4DzR6tfRj9l58ur8LOQkXcNix6Db_tkiFLIeUikqTZzeT3a3HX4lgCAziW7f8lbQ1kFO8h7sqUP2MaDERonNFXj4Qow18vnpaM3bomlDngbad4BA5Rv0VSxA_HFeHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: گروسی همچنان رویکرد نامناسبش اصرار دارد
🔹
در صورت صدور قطعنامه در شورای حکام آژانس انرژی اتمی، به آن پاسخ مناسب خواهیم داد. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/440666" target="_blank">📅 11:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440665">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پروازهای فرودگاه هاشمی‌نژاد مشهد لغو شد
🔹
سخنگوی فرودگاه‌های خراسان‌رضوی: با توجه به شرایط پیش آمده کلیه پروازهای فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد لغو شد.
@Farsan
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/440665" target="_blank">📅 11:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440664">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17be14ac20.mp4?token=aYBI67nQJWtKNrucbJdsL704q9UY7XsQbLiZms4uteIQIDHVt1gWwDxNiyVBtQvPnn0X6FMRQy4yW2pcCVAp_Y_1K9Go_fhRY_s3lWDGzlBi1SND3gIh3kqyVBrhNjxn4NvfivUEHkMq-yV12PPvf1fptXfJ6FRMyjvd4AT0iQ91T1nhHNpccNjux-oAkXSyDMOu4yTvKD4INd2bbMak7RczriXUvCnJmWUZd2nki8_PvEGzINJDneSB4krZzLoaMMHgjx4y7m0-kNdF4Z5HXtjtGKJr2lEPG7dqpYIhwywSXP2JR7DjoC40OcirAltFMtIzd4faZsJ9thVBDLdEsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17be14ac20.mp4?token=aYBI67nQJWtKNrucbJdsL704q9UY7XsQbLiZms4uteIQIDHVt1gWwDxNiyVBtQvPnn0X6FMRQy4yW2pcCVAp_Y_1K9Go_fhRY_s3lWDGzlBi1SND3gIh3kqyVBrhNjxn4NvfivUEHkMq-yV12PPvf1fptXfJ6FRMyjvd4AT0iQ91T1nhHNpccNjux-oAkXSyDMOu4yTvKD4INd2bbMak7RczriXUvCnJmWUZd2nki8_PvEGzINJDneSB4krZzLoaMMHgjx4y7m0-kNdF4Z5HXtjtGKJr2lEPG7dqpYIhwywSXP2JR7DjoC40OcirAltFMtIzd4faZsJ9thVBDLdEsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آتش‌بس به‌طور مستمر و مکرر توسط طرف‌های مقابل نقض شده است.
🔹
ما هر وقت لازم بدانیم برای دفاع از امنیت کشور اقدام خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/440664" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
🔹
معاون امنیتی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
📝
خبر تکمیلی در خصوص خسارات و تلفات احتمالی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/440663" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440662">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e040c786b2.mp4?token=fjfIqJ47tjwbAKYJEFQp2MmjypWSv6N-dB4EMyJtF2heg9ogtm9Iu6zFU6ydObBP5SGo57mHSIsgHq5S8CAscnNOTfEPE9Fqcs4Q91jEJoKb0XJZjfNgzbbOgKPUXBNn-Ax16-viu19hZXkjkbfTrmlXJNeG_Rm3kCQ2OodhSRZrn3qWMC769CNHC1TdyuQWnV75UiqDIm43mS3E-E-wrCNS0yZONsLZaxTxjs3xCrIYjuxWI71SjekUOrJqkpDS08ewnXLswOI11mP5s315V7gUmkRxMCyK6rGbhpbwWIV6ju27x1NC4z8zrmfWII19By74S3jierWNfHSMvR3czw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e040c786b2.mp4?token=fjfIqJ47tjwbAKYJEFQp2MmjypWSv6N-dB4EMyJtF2heg9ogtm9Iu6zFU6ydObBP5SGo57mHSIsgHq5S8CAscnNOTfEPE9Fqcs4Q91jEJoKb0XJZjfNgzbbOgKPUXBNn-Ax16-viu19hZXkjkbfTrmlXJNeG_Rm3kCQ2OodhSRZrn3qWMC769CNHC1TdyuQWnV75UiqDIm43mS3E-E-wrCNS0yZONsLZaxTxjs3xCrIYjuxWI71SjekUOrJqkpDS08ewnXLswOI11mP5s315V7gUmkRxMCyK6rGbhpbwWIV6ju27x1NC4z8zrmfWII19By74S3jierWNfHSMvR3czw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تاکنون تبادل پیام ما با آمریکایی‌ها در فضای بی‌اعتمادی بوده و اتفاقات شبانه‌روز گذشته به این بی‌اعتمادی دامن خواهد زد.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/440662" target="_blank">📅 10:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440661">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عامل تروریستی شهادت شهید یوسفی در زاهدان دستگیر شد
🔹
معاونت اجتماعی مرزبانی سیستان‌وبلوچستان: در عملیات اطلاعاتی مرزبانان در شهرستان زاهدان، عامل تروریستی شهادت شهید یوسفی مامور انتظامی شهرستان خوسف خراسان‌جنوبی در شهر زاهدان دستگیر شد.
🔹
عامل پس از چندين روز کار اطلاعاتی، توسط مرزبانان سیستان‌وبلوچستان دستگیر و یک دستگاه خودروی هایلوکس نیز از وی توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/440661" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de88f8ba46.mp4?token=S9BWX081feu1k74-ys7NfKFggyiW-L5InMOlQUaJmiPTjq7rL84YzZOyLGP1iXwBTgM65i7qyp8a_cRwHaS5Zt7w-EQ0VMrbfGemSuHIwRWMVSqrBeYHajorg2Mb7PTaxAj0JAhpDCDxY507f8xGn2Oc94-pZg6rTr59i9hG5ibvNqGkD0sCi2tUaiyzc-jhTxdkxiNANMywl_ZNiDaJNBKzf5GfVNn9E52uwtJUkx-4hF_vzRnR8f5AIVkYmC89LOsUKYhUq9DQMWpofpjAQ_U-qyDJzJ0C3qoPftbZ6QqBMX6Z-GdB8cLWIvN70Y7OMtrdkprI7T3KWTd2tZroOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de88f8ba46.mp4?token=S9BWX081feu1k74-ys7NfKFggyiW-L5InMOlQUaJmiPTjq7rL84YzZOyLGP1iXwBTgM65i7qyp8a_cRwHaS5Zt7w-EQ0VMrbfGemSuHIwRWMVSqrBeYHajorg2Mb7PTaxAj0JAhpDCDxY507f8xGn2Oc94-pZg6rTr59i9hG5ibvNqGkD0sCi2tUaiyzc-jhTxdkxiNANMywl_ZNiDaJNBKzf5GfVNn9E52uwtJUkx-4hF_vzRnR8f5AIVkYmC89LOsUKYhUq9DQMWpofpjAQ_U-qyDJzJ0C3qoPftbZ6QqBMX6Z-GdB8cLWIvN70Y7OMtrdkprI7T3KWTd2tZroOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تاکنون تبادل پیام ما با آمریکایی‌ها در فضای بی‌اعتمادی بوده و اتفاقات شبانه‌روز گذشته به این بی‌اعتمادی دامن خواهد زد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/440660" target="_blank">📅 10:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893570ccfc.mp4?token=tBXd-X6y2d7bHlY5T4LFSd1uScrG0dYiS1yBPG0cejl8f9xR6f0FxFncnwDmJ0DOcbu4nos6ZrtzCAxDWXwz78GSc324oMG0Iay7cYxlTV4sCvmFLLQGDomo1DM99y9GQHaLrezBjh_ZHytg_MS_Syz9zHDC77KEBIsc9jsTXd-1_AGi-ua5Zn7KUMgV12rDCCpvl4LLDDdaHR7cXh5_3JIZwDN8h9XzlT3Iqgk04gSAtRIZoxRQS6ntmonIdpPvorWa1zPIKGR6RYVVEWE9FC2kWITnSjWI4s0y1fX9tn0EAwCH5LlJ_0Vly87PIAgq4WQBnEtBziXSXH4HPuVnrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893570ccfc.mp4?token=tBXd-X6y2d7bHlY5T4LFSd1uScrG0dYiS1yBPG0cejl8f9xR6f0FxFncnwDmJ0DOcbu4nos6ZrtzCAxDWXwz78GSc324oMG0Iay7cYxlTV4sCvmFLLQGDomo1DM99y9GQHaLrezBjh_ZHytg_MS_Syz9zHDC77KEBIsc9jsTXd-1_AGi-ua5Zn7KUMgV12rDCCpvl4LLDDdaHR7cXh5_3JIZwDN8h9XzlT3Iqgk04gSAtRIZoxRQS6ntmonIdpPvorWa1zPIKGR6RYVVEWE9FC2kWITnSjWI4s0y1fX9tn0EAwCH5LlJ_0Vly87PIAgq4WQBnEtBziXSXH4HPuVnrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیکی‌ها با پرچم ایران به استقبال تیم ملی رفتند
🔹
جمعی از ایرانی‌های حاضر در مکزیک و بومیان تیخوانا با در دست داشتن پرچم ایران به استقبال تیم ملی رفتند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/440659" target="_blank">📅 10:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5w5YkY31W3UbkPgKSq-2HzLqS73d8RVXU9DL2ksixl1NW0_mip7wDCwX7UQ8EnQt6Ug9Ok8XRy3qcuQiORiMxy1Lyi6PQm-lPP7EOQ1JoOejRkYCMtnQ8Vm4E_HCRlMpLheABml6u4bXLimKODqHih2Ig7ymaeAakCKeJP6baek_KCulHULjKZaljXAiVlqShNL3WhuN6poVKdiWdNA6duQh3LzgMJJK8egXn9ZlIMZjhdXEMxh3-41Badb0vf90PgiCYZWIxCwga0u8MaTZaOQHFye4yIWff0iVO0KcPxYnztRlwMDfRONM1Lb_KDD56ijT6prDqsituEFV2K2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ خواهران منصوریان به رئیس فدراسیون ووشو
🔹
فدراسیون ووشو در بیانیه‌ای اعلام کرد که پس از شکست سهیلا منصوریان مقابل رقیب خود، خواهران منصوریان به رئیس فدراسیون ووشو حمله کرده، به او توهین و اقدام به خودزنی کردند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/440658" target="_blank">📅 10:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tafftJtgTcK10iH1nAroCeWqeHBisYYhlh1VgO8ffKyH0MQSGCJgvgdzvj8YLKpt2xuE3gEW3P-kIQNs9g2z_IS99JcbAXm89-CtnU7l8irUQgGaU_5u7inQviDZDKvUN6O5LjeTW8KbD9Wu7BwqzniYVs8ad2qRYrdwJabPQ0pztiPtKfkHWjOHrjN-oU-I4Zs_mkm25T--bY7FmduJIJb_fA2gLmO7X-rGkurP5szY2vdoBUNosoZ3H4MwmLH_8VERFCygM6bFoZYwNPY_eE8Od3vDIQE8Lv5_ZFmVHP9f87DOIf73DMOSfHb5_d6DpsCt5iemAOhBT-plGkKWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دست‌نوشته شهید لاریجانی:
🔹
اقلیم پارس را غم از آسیب دهر نیست
🔹
تا بر سرش بود چو تویی سایه خدا  @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/440657" target="_blank">📅 10:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
موج جدید موشک‌های ایرانی به‌سمت سرزمین‌های اشغالی
🔹
مشاهدات میدانی خبرنگاران فارس در استان‌های مختلف از شلیک چندین فروند موشک نیروهای مسلح ایران به‌سمت سرزمین‌های اشغالی خبر می‌دهد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/440656" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaQ5aCT4y1pQRB07NOo0MjjCx_0vHSuM-i9IAcTR8C42kr5acbgTasI4SAkjhiE-0wYdCh0vvt_UZ3ig2Ow2uBG7jqxsn4hx6hnTi6Eyv_0Kt3vKfquAHDsqJ4Me9O6v6CvZT3hGPdL87pP33DnFl90YDlenW45gCUqAFpCzHi461xoQSoqAsd_YAry78vJUdfcZzVmL-070sk2aHujTL63xps6fv7uHB9nb2Kr2JMsdwwrLJAt4FBgoTzeIGGjnoCxGnXOp8c6Bo9OWSrkfyZ6r7HreSD-pWPjy6TLE4IcP9F-hMpca8KGqQr0s0epu5BzXjdOpqvm4sLjgt92Flw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزادراه هوشمند تهران در آستانهٔ بهره‌برداری
🔹
ساخت فاز اول آزاد‌راه شهید شوشتری که مجهز به سامانه‌های هوشمند است با طول ۹ کیلومتر به ‌اتمام رسید.
🔹
این فاز محدودهٔ بزرگراه امام رضا(ع) در جنوب شرق تهران را به شمال استادیوم تختی، بلوار هجرت و بزرگراه بسیج وصل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/440655" target="_blank">📅 10:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c0cd0635.mp4?token=OJsOHs97mVVe-9XqjbD5YhVSVHcrv0Isi7_o3q7E4HT841gjYoA3miXT_POuXp2qQ9E-AqCY71xcwR4m0KEdhS63DxCAk_-NOeHWOd7zbb7DCG7a1LZIRcSvXm8naTMtYgsHw0DGoLCh_CsHWLnxcQTp21XwL8Cr9uWSE0-1Ri_rEd1duOGLP8IU-e7D3tsD8oc9vJoZ98tP42h5S6wZupKdvSY1y37aNrfysvKhewm2lH5NMLAlpSaBTzGl2M1a1wBxIx-pKxXLy0zPAwJPRxAFNfZxG4MOkYIR9IfAgIobdbduRTPi_tE_YtIoJt8rmC2YH_ZMeJBbTxBvxvnaig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c0cd0635.mp4?token=OJsOHs97mVVe-9XqjbD5YhVSVHcrv0Isi7_o3q7E4HT841gjYoA3miXT_POuXp2qQ9E-AqCY71xcwR4m0KEdhS63DxCAk_-NOeHWOd7zbb7DCG7a1LZIRcSvXm8naTMtYgsHw0DGoLCh_CsHWLnxcQTp21XwL8Cr9uWSE0-1Ri_rEd1duOGLP8IU-e7D3tsD8oc9vJoZ98tP42h5S6wZupKdvSY1y37aNrfysvKhewm2lH5NMLAlpSaBTzGl2M1a1wBxIx-pKxXLy0zPAwJPRxAFNfZxG4MOkYIR9IfAgIobdbduRTPi_tE_YtIoJt8rmC2YH_ZMeJBbTxBvxvnaig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شنیده‌شدن صدای انفجارهای پیاپی در سرزمین‌های اشغالی بر اثر حملات موشکی ایران
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/440654" target="_blank">📅 10:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تمامی پروازهای فرودگاه مهرآباد لغو شد
🔹
تا اطلاع ثانوی، تمامی پروازهای فرودگاه مهرآباد تهران لغو شده است؛ مسافران پیش از مراجعه به فرودگاه، آخرین وضعیت پروازها را از طریق سامانهٔ ۱۹۹ یا شماره ۰۲۱-۶۱۰۲۱ پیگیری کنند. @Farsna - Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/440653" target="_blank">📅 10:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
اسرائیل‌هیوم: تیم‌های امدادی به مناطقی در حیفا اعزام شدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440652" target="_blank">📅 10:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
منابع صهیونیستی: پروازهای فرودگاه‌های بن‌گوریون متوقف شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/440651" target="_blank">📅 10:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
اسرائیل‌هیوم: صدای انفجار در تل‌آویو شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/440649" target="_blank">📅 10:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
منابع صهیونیستی: چند موشک به کریات آتا و مناطق شمال اسرائیل اصابت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/440648" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440647">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpuVVnmHK19gPNiuzZ4Sqi5v9hWEoUtPTcHCogdOHCxmDxgyM2_iH-cOfbtUYHLhinAKtc8YsbewTY5FTyKYonTTlxIGOmT90YhBpoyY-68Y98onEDCdu4lyliA0JCQG_84DKBBnmiWncz-eilWY-1EOnau5pZemLv9VxJ7VLYCquOFWzPOsZL_WJA0Zg1SsL2AryuzdcRtHB9hX7DOMjpkjJDPXj1QUadxJU0MngMexyI6_yRfeEY4R7t4f8nngQl9LIRbMUBkRzS0KFdsM-u9zP4gQF43fsmzbT5zeyxpdZVdAuZl4IfiNufA8WKtWil-dAtGroM9_wtfrQH4bhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدارهای اصابت موشک در حیفا و مناطق شمال فلسطین اشغالی فعال شد.  @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/440647" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440646">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUNwaJRo9NSSVKoZQFsL-kCz2xC87Q6E3uBn2W7-02aIqA0tlBT3-uYP6DVsCfD_M6tc7kwgeLG3_vuGe4F9Migb888fKmnoJeVAXC3FCrZ9FkMPihlMBPSUr27YwaNw0S8JcthzVpBfFflsZWzprNbYXYSGvUwHZB_ew8KPPajRSEqvyYT41DcHa7Idvb5IlCTZ7V_erE4pkhLzQY_zqGAOJXr_vqZFstSuoz48jo__bANC9FI3XU7wenZLJ3mlY15J9T8TVswcDnLgro89rL-KTJtmdOrWoEGi6krdfU5-qW2MdC4NrlKeRS0xSNpBtPhV-sDSeY_QAUr2OHkN3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدارهای اولیهٔ حملهٔ هوایی از شمال تا مرکز فلسطین اشغالی فعال شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/440646" target="_blank">📅 10:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFfhNG8voTpMvos4Fth0HxQBpVOJLyK1Hv3nJiA0Vmp6aNPvaEnhDcZdPLw-Wmim0WQaprTN6TtP99X-ntn5y3j3Le4fG0pHKOD7pLQ-u9SQfCdRQwwSxQjhQZfwe0DEooO1HOKQAbHgVF86vtT-rXV8upwg-KFMRPKzeM5mnz60sXUPoFY2jCDpY5aUprDfOk47INWaBIUi1YV1RecOdbukqXWeKMsDi2OT00r1wMtgOamcssui4Oa3aUzQlvB8NjwYsXn22YnEBn4ulMF0BF9hScSzSgzWdP545l51rLFT_lX6Qjf-CLnOxpbKu1KM5sCSOBP4mbxvTZUuv9wUZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
شبکه ۱۲ رژیم صهیونیستی: یک موج دیگر پرتاب موشک به‌سمت مرکز اسرائیل شناسایی شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/440645" target="_blank">📅 10:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
هشدارهای اولیهٔ شلیک موشک در شمال فلسطین اشغالی فعال شد  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440644" target="_blank">📅 10:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440642">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOW6_aoY2ccN0ANdBP66g4IaOkjBFULhc910XcYE8DMYOMapstSk3KFUT9DJNh9QW57P7GjpRhQ7UF-u7TS_HtlivCtqBRo_gV-ABgDWSjZzZuHRxGQjkdQeG0hu1YSAx08eQorFZRFIBfXgkNEp641O9fCP5MZu9iBw16k42A0Cvhgz3qj-zVJT5I5-nAJePccaxmgsViGe_f-p5iLaC3HrO8UrYlXh5IS-5zUIsqXzeriXvCXQ89eXFlWxYPgP84rc_ypVJ7NTZQNuQ2SoVB5WgGT9ejN_KUhNx2VYz2vueXMBiR8pBWSf5kOmSGkKSL9iBwbBLf8S1lFa0Q6pog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدارهای اولیهٔ شلیک موشک در شمال فلسطین اشغالی فعال شد
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440642" target="_blank">📅 10:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440641">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
لحظاتی پیش صدای انفجار در مناطقی از تهران، اصفهان و تبریز شنیده شد
🔹
ارتش رژیم صهیونیستی حملات به ایران را تایید کرد.
📝
اخبار تکمیلی متعاقباً ارسال خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/440641" target="_blank">📅 09:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440639">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFwwKuBiPChdz_WvBJ4Bd0pKuI9jWE4RomTFGVtFdvFTAXMUXYitbFhte2zmrRQmAcZXquhJjWuNOwWq_hHUn0dmQWgaxeqIOGT39KBfyDB9nYpq20h3bHq3dkm9_zaODno9x_Yjpzssj9LzehHq_I971XDTF3sA4jjhLkxSCNoJ8oyITM-00EFMMdXiTlQDcBcFrmqFiNO0MPkVpwrrswwijebN49GFHgxIX71qmtj1reJhDHtWhtJ4LKTdXH5FxrR1fAGczTGnimCTvB7p2z0jw7C31JTb4GaLN3YN3dTCpuYVKu9f7pUDjp2Z2_91z26kJTxzWOfSDYDQ8NoCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی سپاه: برای چندمین‌بار ثابت کردیم که آسمان سرزمین‌های اشغالی و منطقه، تحت ارادهٔ ما و در تصرف غرش موشک‌های ویرانگر هوافضای سپاه است.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/440639" target="_blank">📅 09:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440638">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تمامی پروازهای فرودگاه مهرآباد لغو شد
🔹
تا اطلاع ثانوی، تمامی پروازهای فرودگاه مهرآباد تهران لغو شده است؛ مسافران پیش از مراجعه به فرودگاه، آخرین وضعیت پروازها را از طریق سامانهٔ ۱۹۹ یا شماره ۰۲۱-۶۱۰۲۱ پیگیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/440638" target="_blank">📅 09:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440637">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaSP2sGGEQEUz4blyMd7FCSClsTdxzFoJBoXcEgZzC4ekhjM_y3ZIwzg6cS6G0qGGYsRKs4cmPQgbbVtKrLovLlHaN9QAV9anHMdL4re0zH5-fmTBNI7DYvosBuC7R7SEDuTMcLGfbK94PngxXPqL5VP2gbitAESYjXa1NH6CsYLu_CyvwEgD8d_IttqOe21EcQe7QK47MkXqvcYqFayeuGWLpq0ChvzMMbmCmNhbdbNzVZgwnNk3c2WBwqna0w924SNsePkI_Gars906XqCkBmMTbBASVBURcmLU0oNTndH8hGwTB8z4r_gG5r6fwnyFW65jcYxz-aA8qiV1TUw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجوز‌ حرفه‌ای ۶ باشگاه ایرانی تأیید شد
🔹
با اعلام کنفدراسیون فوتبال آسیا AFC باشگاه آلومینیوم اراک، چادرملو اردکان، استقلال، گل گهر، پرسپولیس و تراکتور مجوز حرفهای برای فصل آینده را دریافت کردند.
🔹
خبری از سپاهان نیست.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/440637" target="_blank">📅 09:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440636">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI8JgciZ7pSmyLWDjnGVeDTWjKgsc3Y1YKTQX9FkEd38M0phhT7IYzlCEKiZNDgZ_9KRAFf2YhPyzuG32CZK69j2LKIm3I5_R5J2eMChs7PVyijJj2vLm-HCkCrL3aBHpOl08MZrohpS5jh_3IOzcbQ7-MSQbwVDgL1iIhk1H1kfwNv69je8bUC3Orogb0X9E1TKtVAsk58-GpIJteVWk03Y_rpRsTeOas-cKvSnro9uK-WdeYJz6ceh7Gk2boTGzXdTY-ilt7zoaSvUOJcYqjmPPiPp6hwiDWXeQUZRdZJTswzCU-U_yStV2wCBYtYlyJRJfMvX50mouAxm1DHE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ حملۀ موشکی یمن به اراضی اشغالی
🔹
ارتش رژیم صهیونیستی: ما شلیک موشکی از یمن به سمت اسرائیل را شناسایی کردیم و سیستم‌های دفاعی در حال رهگیری آن هستند. @Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/440636" target="_blank">📅 09:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440635">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">درخواست جبهه داخلی اسرائیل برای اعمال محدودیت بر فرودگاه بن‌گوریون
🔹
شبکه ۱۲ اسرائیل به‌نقل از جبههٔ داخلی اسرائیل اعلام کرد که خواهان اعمال محدودیت‌های جدید در فرودگاه بن‌گوریون تل‌آویو شده است.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/440635" target="_blank">📅 09:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440634">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c1fd0bcd.mp4?token=DKBYJoU1UJ5bBTTsj7syBkdf4vnSQyl-G8calwGNfeXi25MpLVVVvv3hxWjDrCIIAOU06Y7TBdrrHK2r3PIGWIfnpkEy09fdnK-86LMemizIXTS6dzh11Kqi_r1Ru3uTjbzAJhmwDmEeLd5YO6k2vK9HM04OyoUQKhBn9ifsZe5g1ukrI8qtnJC9ZglNyfHcMMf8C3PPw8FUApTlYxYumJ_rOP-7u_6zw-UpCpO7umoVjv01NoVqdMBSbwHvgRmrsqtYoB_Rk3c46686jccrZLXNqZh0aHK0TaU6KVRgaFe700_IQSZ1w2ThCtUGw7NG8qjD451pKJf3-l5qh23QLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c1fd0bcd.mp4?token=DKBYJoU1UJ5bBTTsj7syBkdf4vnSQyl-G8calwGNfeXi25MpLVVVvv3hxWjDrCIIAOU06Y7TBdrrHK2r3PIGWIfnpkEy09fdnK-86LMemizIXTS6dzh11Kqi_r1Ru3uTjbzAJhmwDmEeLd5YO6k2vK9HM04OyoUQKhBn9ifsZe5g1ukrI8qtnJC9ZglNyfHcMMf8C3PPw8FUApTlYxYumJ_rOP-7u_6zw-UpCpO7umoVjv01NoVqdMBSbwHvgRmrsqtYoB_Rk3c46686jccrZLXNqZh0aHK0TaU6KVRgaFe700_IQSZ1w2ThCtUGw7NG8qjD451pKJf3-l5qh23QLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعان، کارشناس مسائل غرب آسیا: حملۀ امروز صبح رژیم صهیونیستی به خاک کشورمان با هماهنگی کامل آمریکا بوده.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/440634" target="_blank">📅 08:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
آغاز عملیات نصر علیه پایگاه‌های تل‌نوف و نواتیم
🔹
سپاه پاسداران: دقایقی پیش رزمندگان شجاع نیروی هوافضای سپاه عملیات نصر را با رمز مقدس یا حیدر کرار و هدیه به شهدای جنگ ۱۲ روزه با هدف‌قراردادن مراکز مهم پایگاه‌های هوایی راهبردی نواتیم و تل‌نوف آغاز کردند.
🔹
این عملیات در پاسخ به تجاوز موشکی رژیم کودک‌کش صهیونی به چند سایت راداری در ۳ نقطهٔ کشور انجام شد.
🔹
سرعت عمل در پاسخ به تجاوزات ارتش رژیم صهیونیستی و گستردگی بانک اهداف جزو اقدامات گروه‌های عمل‌کننده در این مرحله بوده است.
🔹
کلیه یگان‌های رزمی و عملیاتی سپاه پاسداران برای انجام عملیات عبرت‌آموز گسترده در تمام جبهه‌ها در آمادگی کامل هستند و برنامه‌های اقدام را متناسب با سناریوهای دشمن تدارک دیده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farsna/440632" target="_blank">📅 08:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440631">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFPF7JKYTuCudYpxH-OaNbfsHoSq0BOobjD09zL4GYKpqsocl9k2y5NX2gb9cDuw08U1ERUcIk2ZWNah9CHaY6D0QqEXYPNCkUqunef2oJQB85q0CCXshhCxrNdxnCAEfbKctiZBlURU8wG0Ma7wJwyWl43L7nDhKzpr0Zitx3Ngv3sG7xCwO_C1-hhMiOvFvkCIN_CJzDGakvXw_iKFjYs9aX_xY_rdxM2P2i0AI_DLwhEo6G5XRZ3_1ZlVn9_RYRP47vCaR-QKQ8TQkzQ0AjFjUtW_drcvQY2Ibv1XfwHZDa3FdgyotaVwMWSLOjANbdoqhlTR9TPbJKnZT58bUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دست‌نوشته شهید لاریجانی:
🔹
اقلیم پارس را غم از آسیب دهر نیست
🔹
تا بر سرش بود چو تویی سایه خدا
@Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/440631" target="_blank">📅 08:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
🔹
معاون امنیتی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
📝
خبر تکمیلی در خصوص خسارات و تلفات احتمالی…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/440630" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سفیر آمریکا در اسرائیل به پناهگاه رفت
🔹
سفیر آمریکا در اسرائیل در صفحهٔ خود نوشت: الآن در پناهگاهم. صدای انفجارهای مهیبی از بالا می‌آید. امیدوارم که رهگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/440629" target="_blank">📅 08:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6c5571ea.mp4?token=TrgG-lgscR-wR_Z3ZU03UM0gvzGGxLQL9-SqjOHbMwRZwVBxjRRYMdnm53-bz72kNYJiQr7sk6bNew8VMlRWFdOn8MzDHMn2JEZRUBs8uhEnzqf4GKTa3yikRazMLKUoI5Eb0UxD9l8JncFMG0oC6T6lqVwoNRKxFHkdXr-wvcp0lhWr5wAV6LwpS12avWcr9aEGowFA8SPqZjlVuOhdZ897fTV9QuL6EATvIsbOucAOgPRj65VS1drNtB1GZAMZkVPPtU9WaugWEzXG0Y7B08CTxwekfzX06mfjn0ALLWxsNDLhWklxhaf5LyGmr7Wf_zfMi371Qv1baKkdfhNirA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6c5571ea.mp4?token=TrgG-lgscR-wR_Z3ZU03UM0gvzGGxLQL9-SqjOHbMwRZwVBxjRRYMdnm53-bz72kNYJiQr7sk6bNew8VMlRWFdOn8MzDHMn2JEZRUBs8uhEnzqf4GKTa3yikRazMLKUoI5Eb0UxD9l8JncFMG0oC6T6lqVwoNRKxFHkdXr-wvcp0lhWr5wAV6LwpS12avWcr9aEGowFA8SPqZjlVuOhdZ897fTV9QuL6EATvIsbOucAOgPRj65VS1drNtB1GZAMZkVPPtU9WaugWEzXG0Y7B08CTxwekfzX06mfjn0ALLWxsNDLhWklxhaf5LyGmr7Wf_zfMi371Qv1baKkdfhNirA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ستونی از دود در محل اصابت موشک ایران به هوا بلند شده است  @Farsna</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/440628" target="_blank">📅 08:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🔴
گروه هکری حنظله: به هر کشوری که برای تروریست‌ها فرش قرمز پهن کرده می‌گوییم نوبت شما هم خواهد رسید
🔹
هیچ سرزمینی بیش از حد دور نیست، هیچ سروری امن نخواهد بود و هیچ شبکه‌ای از دسترس ما خارج نیست. منتظر بمانید و تماشا کنید.
🔹
شاید همین حالا هم سایه‌ای در…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/440627" target="_blank">📅 08:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
گروه هکری حنظله: از شما دعوت می‌کنم تا شاهد ویرانگرترین حملات سایبری علیه زیرساخت‌های حیاتی و نظامی دشمن باشید.  @Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/440626" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
گروه هکری حنظله: از شما دعوت می‌کنم تا شاهد ویرانگرترین حملات سایبری علیه زیرساخت‌های حیاتی و نظامی دشمن باشید.
@Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/440625" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
🔹
معاون امنیتی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
📝
خبر تکمیلی در خصوص خسارات و تلفات احتمالی متعاقبا اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farsna/440624" target="_blank">📅 08:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f8a2558e.mp4?token=cAxdFuPr2u8Eib51JiDShdqTLZqea1krjqoFTQ1e5iMovUE7NphSmSZ1Z8ET2WzCOGAllM5CMHkM14sVWwF99VB0SSnxamq2j12QcQ4DuoHHVHmeN-rtVztt53cKo4QjzQRx1NdAvWOiAK5h79ED-ILv5inaxvfWhEC-L82AhXlbhtKwSqbDjX_AvRLsDj0PYy57lL_4I3tpGMVIlns8_WCDD6K7iLUfSZSCzIApSqGU8mVXDVECsAqQsKDQD_kTHfEi6ycijpr6_8Hprs17rsmzc4p-yA-xv5AXAs_AyX3buKJym_NWjCWQwt9GEkUoNahsOezwbYSZyk8OM2py4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f8a2558e.mp4?token=cAxdFuPr2u8Eib51JiDShdqTLZqea1krjqoFTQ1e5iMovUE7NphSmSZ1Z8ET2WzCOGAllM5CMHkM14sVWwF99VB0SSnxamq2j12QcQ4DuoHHVHmeN-rtVztt53cKo4QjzQRx1NdAvWOiAK5h79ED-ILv5inaxvfWhEC-L82AhXlbhtKwSqbDjX_AvRLsDj0PYy57lL_4I3tpGMVIlns8_WCDD6K7iLUfSZSCzIApSqGU8mVXDVECsAqQsKDQD_kTHfEi6ycijpr6_8Hprs17rsmzc4p-yA-xv5AXAs_AyX3buKJym_NWjCWQwt9GEkUoNahsOezwbYSZyk8OM2py4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
اصابت موشک به منطقهٔ شومرون در شمال کرانهٔ باختری  @Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/440623" target="_blank">📅 07:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvchchLJ54o3wyGoEgZdr7oLwvr8hcHHfmREd9449xC2Yh-hEEwY_aGZUccRkj110b29Cu8XEW9Sie-SAnMro13vFnU-wntctGOcgRCH2_XbwE-1FPowoQMzM267K64bIz0lkOsLwo2738A97Fi-u5CostD-L_Xu0GJv8_odCWDWIFxhXG690Ec9gT_y2lyAQTuj7Cl7JGJtEp2LdAw8EUnWMG3Bsy5UzwvYGds3KRMml88U6Gk9u6dnQ3cDUOZMq0K8X9JL9iE4pHgIfDMtFqwg4AaY5viyEkm0oqdAbR1vdYf45NWKg3Fo7jmtdnGclbcu4MWe272su12Y9ZaVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آژیرهای خطر در اراضی اشغالی بار دیگر به صدا در آمدند
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/440622" target="_blank">📅 07:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndAYii9tfdkKCRya3QKplDrx8dgHrs3jYDxFga6BuJrDJVBsHDTMWBgmWHLY9Wp09TbDZbuUQ8LbMK0J9PVr-iF0hyt7sDerqIHxMQiMMqTB7COaEbs32Vj8zDk5W8EZwK8liVHL3qSV_7Kb0cO_rlFZWxXmc5IR_E5H2tv7n8qTki3FoszDCUJ88EofBfJh_0XEeKYrlgYl9aqzME1E8VGG3160r3zuKU7nQqPmfkf5npjGGTdu2eMrJ8wtlRlejExniviXfAuxdmbABaXYyYtwG0jrr5rJaUB0dmB1DtDNzU94UYQuAPQTIY8KmuCw4yhN9CDl_b9nVqiSP4IpNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عبری: یک موشک به یک مقر نظامی اسرائیل در منطقه کرانه باختری اصابت کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/440621" target="_blank">📅 07:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_gCydviaHckvTlDwE6jIw2CH71f3FhZQVFVwPyuEH7kAIzcO_bryHJQ8x4QmWCfANhOQX3GlhUbzPfhPvHeZ21M_8JncwVFWCirBnVHUfV1xlnV35obGvbBjD2_iz8l9cQfu4xraMYO6zf-SvVXhYC_WocSr7cCM51xZ1s-QYtkESI5OkxlPvZT5eDp-XQUs7Rfue6K7bR7bOULVpEycmiYF3pb7MoYK4co8iUmg9ITTUfND5j6ISD1yDV-7-89hQBiNB0T9G8u7Ot-hJpVHZKjO3hmRVYEWWZL4i9WFI4j3GxnA0ww-1_64FSvEnAW6byR9mD1gTEq_1tgXh_Cnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
المیادین: در پی حملۀ موشکی ایران، صدای چندین انفجار مهیب و مداوم در سراسر فلسطین اشغالی شنیده شد.  @Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/440620" target="_blank">📅 07:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌
🔴
شبکه ۱۲ رژیم صهیونیستی از شنیده‌شدن صدای انفجار در منطقه قدس اشغالی خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/440619" target="_blank">📅 07:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440618">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
آژیر حملهٔ موشکی در اراضی اشغالی به صدا درآمد   @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/440618" target="_blank">📅 07:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440616">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
منابع محلی از موج جدید شلیک موشک‌های ایران به سمت مواضع دشمن خبر می‌دهند.
🔹
همزمان هشدارهای اولیه در سرزمین‌های اشغالی  صادر شده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/440616" target="_blank">📅 07:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljt-2gHoHLHkWzlPaJYcQudz6xqKH19K_r2o5cshNK2BX3xIHM5tqT5xKflLWA3hhs5xl_lZIS_gZK_gn3QJ3hLogaSTRCtxPYJudmBvFYfxg7FONDb88XdDp47hT_8YLcsj3pirZw_bzVRO81tG8JL5OLdDbj6659HxeIvEE90DTMp3bxM4cJqA0VM2nqPXr8rIlXtN_-FpjWUCCCEZflKyVkM6P80AFvs8YAO8XdZvzmku-fXb7SissMHkq2EEduSzeqR8CIkj6mtQ2LDDnv6NIJybZX9ta3qFXHciQ3BMqNS3_2EnlZNhWmmuzmbFd0s3jLN6hA4bbXYvhlVZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آژیرها در اراضی اشغالی به صدا درآمد   @Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/440615" target="_blank">📅 07:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440613">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEtQ4xoEisQ1kdGI0PfoxYKT3bkglfIA-8tNANov_FpTqcwdq9vPlWknz4SGdHdE9vxuZN1mi4G3cOvBI67W2k_kGO1sPkr_tQxm0GKJSEVtYjO-2dmcf7msRCb7nXS8uFBtWiRWlJOQkopF8j8w7WQBxXeIQn1zvqN_tcpTLXftaF5XZdKOcviT_-wm2vfEvepSrdyNSbnuWvzyiDe80xzeDQdq7Asud6RS0oj7yHJZxduWudAruLGTEMAScdYo-z6SL5aZ7MecVuQ6_WYx7TbpgGaBrwIyeV19apw_XKdfNz-X-H-a7iOmt9WbuIHjLhkeIzdQZkQ0i1yzzAwFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله از معادلۀ وحدت ساحات خبر داد
🔹
«حزام الاسد» عضو ارشد انصارالله: تهران، بیروت، صنعاء، بغداد، غزه؛ امروز در میدان،‌ معادلۀ وحدت ساحات را ترسیم می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/440613" target="_blank">📅 07:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440612">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
اسرائیل هیوم: اسرائیل حمله به ایران را با آمریکا هماهنگ کرده بود
🔹
برخلاف ادعای کاخ سفید مبنی‌بر عدم دخالت در حملۀ بامداد امروز رژیم صهیونیستی به مواضعی در داخل خاک ایران، روزنامۀ صهیونیستی اسرائیل هیوم گزارش کرد که اسرائیل حملۀ خود به ایران را با آمریکا هماهنگ کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/440612" target="_blank">📅 07:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440611">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
آژیرها در اراضی اشغالی به صدا درآمد   @Farsna</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farsna/440611" target="_blank">📅 06:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440610">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4oT6e15KY8r_fAt9xemx5d59aq0h7SIcfsiG4ysx3eV5lMdiJuPkbFslUHWsG7cld1MGIr6t2DoGhpkMS7CIj960Dgr9g-aXRRK12pykl7Y8y12VarkT4glzUwrgeisCtfooi04jsT0rJ9bOAdfif02z5_-weOauCORfAWHruzywsJOr8hnwLZeb4iytuBrN39z8jkPgjkUY1Tney1ARbi8MpJ9UojEv6YNIcwL20e26CMMy97HfRdYIyIRnQ276dKVH4CZXDHkkeU8COr9F6wJvYMaJ4hmL-JOT_BTffbRCfRIG_TcjJfvUXNCA0I1zk-QugOaXynj-VV8FFqpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
منابع عربی از شنیده‌شدن صدای انفجارهای مهیبی در پایگاه هوایی سلطان در الخرج عربستان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farsna/440610" target="_blank">📅 06:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440609">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
عربستان برای استان الخرج، محل استقرار پایگاه هوایی آمریکا، هشدار اضطراری صادر کرد.  @Farsna</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farsna/440609" target="_blank">📅 06:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440608">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a18kvgYs4Q1_lErOmZ2Ue_WM78InKKTY0jgzPhGDR1lano-xfgQGLWs5RUft4vkXTSH3N-SPDLVbVONiLYFMZqK4VhxnEcc0be5JfK_E4YMCz1GxuRpqaCEeJqZgv5Z14KxcTvikHqhELX0sEJ6lRgtjR7J_31N9iT8ZW_xLdfO9nnx30wi0FxwGbgYY3jt_7a0b7UBmlvYMy2voL0hIVAR_V9mEUaSj7_cgWuepQJBKV-rxAqug1xiLqe3qtkqCczo9YQt78YdPSjvqKw9kHcxlRJHpQ4NkmTDLRoCJmSZtnYnjO0OJcNVUrenw4pi82ylhag7EpegjAnqViaDB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عربستان برای استان الخرج، محل استقرار پایگاه هوایی آمریکا، هشدار اضطراری صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/440608" target="_blank">📅 06:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440606">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌
🔴
منابع خبری می‌گویند که در اراضی اشغالی، صهیونیست‌ها در بالاترین سطح هشدار و آماده‌باش قرار دارند. @Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/440606" target="_blank">📅 06:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c95296f0.mp4?token=lnVvVy1kgeEZoIWuNM8VEqHfuc7mnVc9fW6LKuaujN37E_v0sr8f7VUci92pwmxC_FdFLVGVEejgooG6Rf1SPbu-7JMZTf6HxjxixM8AbeaKAIEmU_B8XmPCYtIgUS8E7K5fPNL1Z02JAXzYx-GLwMHEpUCcOwuwnMFJDAsBPWi_wRV3Mby4gwcdT8GYUF8rVexa13ZPIjsSuo2Loa2-pNqeNZkTxItbz6kdJe5nADsxEp3pK3YxST9uapjEYsMe6I-VwsXPKjb1dmzbfJGGH2JoORAKZOK-JUdZeQVMZke5eim89BQFrkzQycaASCb8gP6VgIGMN6Zus71om6Efmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c95296f0.mp4?token=lnVvVy1kgeEZoIWuNM8VEqHfuc7mnVc9fW6LKuaujN37E_v0sr8f7VUci92pwmxC_FdFLVGVEejgooG6Rf1SPbu-7JMZTf6HxjxixM8AbeaKAIEmU_B8XmPCYtIgUS8E7K5fPNL1Z02JAXzYx-GLwMHEpUCcOwuwnMFJDAsBPWi_wRV3Mby4gwcdT8GYUF8rVexa13ZPIjsSuo2Loa2-pNqeNZkTxItbz6kdJe5nADsxEp3pK3YxST9uapjEYsMe6I-VwsXPKjb1dmzbfJGGH2JoORAKZOK-JUdZeQVMZke5eim89BQFrkzQycaASCb8gP6VgIGMN6Zus71om6Efmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعان، کارشناس مسائل غرب آسیا: آمریکا و رژیم صهیونیستی می‌خواهند نقش پلیس خوب پلیس بد را بازی کنند
🔹
ترامپ دوست دارد آتش‌بس ادامه پیدا کند اما با این شرط که آمریکا و رژیم صهیونیستی به هرکجا خواستند حمله کنند و ایران هم پاسخ ندهد.
🔹
محاصره دریایی، حمله به جزایر ایرانی و حمله به عمق استراتژیک ایران از سوی آمریکا نقض آتش‌بس است.
@Farsna</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/440605" target="_blank">📅 05:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440604">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌
🔴
رسانه‌های عبری: اسرائیل درحال آماده‌شدن برای پاسخ موشکی فوری از سوی ایران است. @Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/440604" target="_blank">📅 05:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
🔴
همزمان با اعلام آماده‌باش سراسری در سرزمین‌های اشغالی، مدارس اسرائیل تعطیل شد. @Farsna</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farsna/440603" target="_blank">📅 05:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440601">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🔴
رسانه‌های عبری: اسرائیل درحال آماده‌شدن برای پاسخ موشکی فوری از سوی ایران است. @Farsna</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farsna/440601" target="_blank">📅 05:21 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
