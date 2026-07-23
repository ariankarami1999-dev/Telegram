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
<img src="https://cdn4.telesco.pe/file/AKt9Hvo8xGK6wy-8PY0z4DYAr7AuOietYKPee0Aq3adwUfx2SvnK_Ga9pn94wE2I-iNvAXWnKNIcWXrTiwHUafeRSbt8e11Xtf7AMOdULoKGLXMmu7IPTHyBwCkNvYDHB8T0ttuUGxOrGvCxHR9B_Uptim6a_DUSvZjz9sL0VDm5QbznyvdXpFc2MLslpamI2t1X6BzZiVS1t9FJuuJBZ3DrGGggDQziwf4uyLosCLZefObMC7x1NA2dtFUM6r8BJ6ishbBX1mFw0mHDA0wwU-5Ziy3Stvh-y1D0_DrwsCjRm_yvfq633S_dF91Utyd4gBUck2fqxZn4I-v8LiWB3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 152K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 21:23:04</div>
<hr>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=HT4MN5d3JUviflvvyy5Qsyh_54bO_zQn-arFelitsUhpyXxpI80L0bvIqs0s8RPbXhQ_FB5YCuMULc2HjnNXBzpiqDgCEkfArzBwlFmM6bLeM8LJx9SCJpV6SRbFTyd3dlJyajxSbTxLsEQ_g8NL70KJzFOGmlcLR_TTQ__qSl_ah-N2llTyG4AVqKejRki_I63AkZDfdJjO7PAfcnn05h127ijmCAaLBaNGOcSFKmG2VxheSNP26mJptPCRWfMNkgacj1PDNyS3Ho6P9-vtB_l-yecLPWL5n-kyUMZ7Qh-rtsYvhK4uM6WHTPEUZj4WH86XL1o340IrnMG7TPrGjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=HT4MN5d3JUviflvvyy5Qsyh_54bO_zQn-arFelitsUhpyXxpI80L0bvIqs0s8RPbXhQ_FB5YCuMULc2HjnNXBzpiqDgCEkfArzBwlFmM6bLeM8LJx9SCJpV6SRbFTyd3dlJyajxSbTxLsEQ_g8NL70KJzFOGmlcLR_TTQ__qSl_ah-N2llTyG4AVqKejRki_I63AkZDfdJjO7PAfcnn05h127ijmCAaLBaNGOcSFKmG2VxheSNP26mJptPCRWfMNkgacj1PDNyS3Ho6P9-vtB_l-yecLPWL5n-kyUMZ7Qh-rtsYvhK4uM6WHTPEUZj4WH86XL1o340IrnMG7TPrGjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=dqurP8zUe8W2PlykkBVJo-5YbTKNpB4S4Y3lUKlqYscjC_r71jrpBO4zbtj5G5-50sBkBkx-gtVg9isFd9WZjYl4R_tgr2RX9k2qoqSZ0yIw0o3T8UXkCBDwaVypNh4DWl8V65uXIV0j12MoKZ3ah9pYeB8HhM2EUKeM_kh-8F_VVA2AGpm3Tg3IBpk4LAiGHnbhcrcMIz9A-F7vjaepiyiA6E8xcjVg_Q4XF1duP9lIy55MuhUjKLV7e0AsaViDQLJoreY4TSHctB6BdYCKN13eJGk6fWVwUq5O2GwprJI4QTZGsOUWQ-as-5YR86cxRnolin1WIozQu2lUVhl0nI93fVNQTPnd1kse0d-Aq_cW9vsvEQ3-_NrgNXMCrH7cKyOUe2XhZBGGmcHpM9pkRP1zCSzXzuxxqC2WOourAUWKbNXwYfQA7y0vC4W1tiLZNUhCzwb2Zrv1Ziu8iQojWSnX3J6wGwcYz7vUJ-lvWaJ6WxxLTsCA1G4XXlA7uGwwsBlGeG9WO6YCZ8a3j1GHz7P5QdLAHvQwXgiHt4Wkxam4paBkoozp5cfZYcMDZQHIqZuDbQyINKIyQcLRS8HVYnS9mYsH-pcGFjHdH6hmE0zdeeGPRlQXANGoMgA34H7WBVfINz0N64ON_iIfXsGt7Um0KAzaYycdq5SQQ0Pq4-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=dqurP8zUe8W2PlykkBVJo-5YbTKNpB4S4Y3lUKlqYscjC_r71jrpBO4zbtj5G5-50sBkBkx-gtVg9isFd9WZjYl4R_tgr2RX9k2qoqSZ0yIw0o3T8UXkCBDwaVypNh4DWl8V65uXIV0j12MoKZ3ah9pYeB8HhM2EUKeM_kh-8F_VVA2AGpm3Tg3IBpk4LAiGHnbhcrcMIz9A-F7vjaepiyiA6E8xcjVg_Q4XF1duP9lIy55MuhUjKLV7e0AsaViDQLJoreY4TSHctB6BdYCKN13eJGk6fWVwUq5O2GwprJI4QTZGsOUWQ-as-5YR86cxRnolin1WIozQu2lUVhl0nI93fVNQTPnd1kse0d-Aq_cW9vsvEQ3-_NrgNXMCrH7cKyOUe2XhZBGGmcHpM9pkRP1zCSzXzuxxqC2WOourAUWKbNXwYfQA7y0vC4W1tiLZNUhCzwb2Zrv1Ziu8iQojWSnX3J6wGwcYz7vUJ-lvWaJ6WxxLTsCA1G4XXlA7uGwwsBlGeG9WO6YCZ8a3j1GHz7P5QdLAHvQwXgiHt4Wkxam4paBkoozp5cfZYcMDZQHIqZuDbQyINKIyQcLRS8HVYnS9mYsH-pcGFjHdH6hmE0zdeeGPRlQXANGoMgA34H7WBVfINz0N64ON_iIfXsGt7Um0KAzaYycdq5SQQ0Pq4-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu5kROcIziO2wlKuJs3uw8R3gNNToPC03cvtCe2wrOyoQUZvmm0zGYaXhLCJhf0QsnXNePV_TntYRDwnQ6wIo7zS4zk_xXXwAZySgC_qh7mqw1-sap-NZ0GPajzEJpF4QajOE-p9iXz_pOcRQsWbvUXBBQstY5cERMcZPfbIAk_0YI0Kjp4bXr3GZwlLFzJfyRN4xNx8gtbkggSWASDMOAdpHpDuf3QuT5__Uv106NE31XUYwSXlZb8G04neGAbFkvdEBn-CmJ4llD2uh54YuCi3FQGEQctiK6MyE0zUaC8gnGmJHvYrDEOWblyyQqxXGQdbUwF6yv0V0TbWf85c8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9qbkJ41vI9Lxca8GUDi6Ot3MdZ9e7z4yw-sU5rR9tmMDpSNt2MPQGU276-mL5Jws0YXngle3HKr8HCgTlCln5QUy1pbbZYbP_9Oh6Myknor_o5rTu4EEqPyHxhA35MTzoHQXvD0fCGOGSWdZUmM9rV7vsdOT_mHZ4bqIXm8XnZtYYbP-esngrTFJWLTaCcGjQ0lEbkpbiwaZHBcGRQQZA2dN-3IyUa4jikzT12Ctyy-KAl7CAKl6WUCPxw07g6ed8ub3q4Nu450BFS9Q2_q80AsPsS5hIS057gT1YoUiGTUdddHwPpfy4z3s4-VnWU_RVLkd9AYqJ0GbYkgMim61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=q7ewz2-vBLsxv_LTSEg8bk7yUhvL3A-QnSRKbiTC1MjFeHgQOOoClloOxLydg4DTkF9ipaP_a9crpDMJc9tV2AKQ524ALxh6IE89CoSs9adoifF_Z5u7CnKgzjiu4hwApKFAmUO7bNkJmh5zhHJgp2Xb83SNzj8xPBldR8nu6HlXpC54pJIIOV61MUuUwPaPQe0lt65AC9jWX5_KM61zYTQZE58yrWjhWgaRrmXNEDQaSr6tUXeZRAIJhUhhrrcKn0D-Uk6x66teplP4VjHem0Wh__XbhcU5SG-0gAOdGxOQqdihby3tBfzTHYp7WtwLm6JZCm2hsrBGNtOucmX8-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=q7ewz2-vBLsxv_LTSEg8bk7yUhvL3A-QnSRKbiTC1MjFeHgQOOoClloOxLydg4DTkF9ipaP_a9crpDMJc9tV2AKQ524ALxh6IE89CoSs9adoifF_Z5u7CnKgzjiu4hwApKFAmUO7bNkJmh5zhHJgp2Xb83SNzj8xPBldR8nu6HlXpC54pJIIOV61MUuUwPaPQe0lt65AC9jWX5_KM61zYTQZE58yrWjhWgaRrmXNEDQaSr6tUXeZRAIJhUhhrrcKn0D-Uk6x66teplP4VjHem0Wh__XbhcU5SG-0gAOdGxOQqdihby3tBfzTHYp7WtwLm6JZCm2hsrBGNtOucmX8-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZLzcJbyylgGGwmMSztt3AUs_l_gjMCORB9BgSwr7ut-jhGXGL35u0Lsk20GW_gutDBPkxTh5VRROTTXrA-kcFCDeBjT01GwXBzBQpfmi_dAlx9aX5hHbuBx5z2scPcQH-1HQafcdiKBi3tpzBkVfr_ZJDuuxmbH46VHGuEjKbZaxRl9WzAaZCBgLThNWmF5WFtlop-aI1rnCkDFYBs1AWOfdT4gbItp9sFnkp2waNKnpBZSRIZxa9RLlgmRgxK4Eky054dx0R3u9cmbqs1XSGws8MJpHXBDUzOlTza6POxbSlcnYehMaiRA760BSE_M5TqQaYg6l0Cg8Rfz_lJ0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBidrgKf0EN04vUFuPuk8uMFbPipG9M5ckqSyl1Kpk8gPVtSs5rAmALma2rAHBi3reLomx9SpVxaxeftulYq9DuLfhSL7Lxi-r8b1VIvgUemq0N7GQMp3B7FQlRF1zPdAaNKgwOytKpXL1Of-6AyKDxuo5jJlWloQ9L1BN-__tuARbWP82wUrsRJYij36ePJ-fNvFkjOYiI9DMniLPGc5JP8QrPIb8Xt5wwqKdFaQizxlAy_sOxxuxgEHEcyLVK4wSkONgLY-ylgReKmQPoNCgkvDk7DzRhUFGZw8ptPYSQB7oyNs31Z3EwTIAIC0qpvuSno6ed7b936pZERnDqxpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=uK8tIyFB9yX0ub0utXPunW3oS1fJ4cPdtBcRPkj815LfQtPXDekXhwzT1zRDxjEiZNJRnoSeB1iXNSH1TBFs73KnTQWVsRuPh9tfcfBBIr0-ONrimzQaC3AsF5d1vsfdMBKXBaqdHqQ69q7mq3lwPCpjfT1OFxZzuFFIxtsnM2qMUO1xldYtUlXWVvuNqntFKMtXIYyTHgfL7jYs_ZPU1NPiaGu0FWoQVDUBrKLASCbkU9Ar-Tzq9099aduTBRIyu9fMqAivSb0Gc4IGhHEjSaoPro_JieLxMcv3OFEZ7ptIwfgPmLqBEewbQBSW5zGp8bROaePskOmv6b_ijfPi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=uK8tIyFB9yX0ub0utXPunW3oS1fJ4cPdtBcRPkj815LfQtPXDekXhwzT1zRDxjEiZNJRnoSeB1iXNSH1TBFs73KnTQWVsRuPh9tfcfBBIr0-ONrimzQaC3AsF5d1vsfdMBKXBaqdHqQ69q7mq3lwPCpjfT1OFxZzuFFIxtsnM2qMUO1xldYtUlXWVvuNqntFKMtXIYyTHgfL7jYs_ZPU1NPiaGu0FWoQVDUBrKLASCbkU9Ar-Tzq9099aduTBRIyu9fMqAivSb0Gc4IGhHEjSaoPro_JieLxMcv3OFEZ7ptIwfgPmLqBEewbQBSW5zGp8bROaePskOmv6b_ijfPi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من بلافاصله پس از انتخابات به دیدار ترامپ رفتم و با هفت اسلاید بزرگ به آنجا رفتم.
اسلاید اول، اسلاید دوم، اسلاید سوم، اسلاید چهارم. "این کاری است که ما انجام خواهیم داد."
نه اینکه بپرسیم "آیا به ما اجازه می‌دهید یا نه؟" بلکه من به او گفتم: "این کاری است که ما انجام خواهیم داد." و ما به اسلاید آخر رسیدیم و من گفتم: "این پیشنهادی است که به شما ارائه می‌دهم."
شما بمب‌افکن‌های B-2 دارید – این بمب‌افکن‌های بسیار بزرگ. یک مکان به نام فوردو وجود دارد. اگر لازم باشد، ما خودمان نیز علیه آن اقدام خواهیم کرد. اما بسیار موثرتر است اگر شما بیایید و به سادگی بمب‌های سنگین خود را آنجا بیندازید.
او گوش داد و در نهایت موافقت کرد. من بسیار خوشحال بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=AL0J-FZodkbMRi8I7ffRidj39CNsxB8RMGcHeIdWLa-cVasc2JVRMEYOwdz6VTwIV5SrzP2KNiZ6BJx0EEgBHZsWHo5L1u4JKricvy8Pv8j-0rmD73BJFhbpp_90D5gpUZiaAntLFL506kIzNLA6xCP-d-4AL8Fql7LFgNCo35fpJcWrWab_NYjWDIAwg72sIIbJ6zd8KHng4133Ka8PoIiDxOZGKHMxVdEQoBowNGNSQ3cIKW6JK_bWQJP4XkdRoHsIulKxj4vzOG6OOBWRxP1bsl-PY9xXiEYKnGsZkSQbKuUxxvCq9RxFk_3V7rxV1Zw_Q8_gKhG2p7QdjEkPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=AL0J-FZodkbMRi8I7ffRidj39CNsxB8RMGcHeIdWLa-cVasc2JVRMEYOwdz6VTwIV5SrzP2KNiZ6BJx0EEgBHZsWHo5L1u4JKricvy8Pv8j-0rmD73BJFhbpp_90D5gpUZiaAntLFL506kIzNLA6xCP-d-4AL8Fql7LFgNCo35fpJcWrWab_NYjWDIAwg72sIIbJ6zd8KHng4133Ka8PoIiDxOZGKHMxVdEQoBowNGNSQ3cIKW6JK_bWQJP4XkdRoHsIulKxj4vzOG6OOBWRxP1bsl-PY9xXiEYKnGsZkSQbKuUxxvCq9RxFk_3V7rxV1Zw_Q8_gKhG2p7QdjEkPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری:
الان تو دنیا کدوم کشور با ما دوسته کدومشون دوسته بجز مردمشون؟
⏺
ثابتی:
اونام دولت هاشون مثل حسن روحانی تفکراتشون امریکاییه
⏺
شهریاری:
توهین نکن حسن روحانی امریکایی نیست بعدم تو در حدی نیستی بخواد بخاطر این حرفت ازت شکایت کنه اگه تفکرات روحانی رو امریکایی میدونی یعنی تفکرات 80 درصد مردم امریکاییه..
⏺
ثابتی:
کی گفته؟
⏺
شهریاری:
کی گفته؟ اگه جرات دارین رفراندوم برگزار کنین تا مردم بگن.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bypk7hnfNVoiiayhM41YftAGVriNZM_8ak8By9iPavRDC5MD59ZWwwl0bOT3Ub8ht15PvbjQlj1Xn7T2slchbfwhZctV8iPBfealMIJ-h4BGo5YtlqucjxjmWMDHIclBZXbYjXhhBoE10FnVDWGXOQK3U76al2kNGyImB99bywQsoEbCMAccNKJu8iLz4UiOE09oBiCWVW-WuQgNKWOimFI9id94UInjOVYgF9vos8AL0LlS3YXrmr1YqhiJ1eud4ZjvatBKGw4kjjCFH5OtI5A8onhFeGXoxWhBvgfSy2oOsnaD4gUfBglY-FhV_0PsYamFb4ESkaDaP9gMhZZk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTCU1Ypy9gfBDKNr9WwRr0-zmwMzou74ReYwelKDfQwZsjlSPtmPjfKq5M45hAkhyE0I9qj04t9YqnDh5uTKBVlsC3KxvOEoUQdFDoqFIF9wwZXZWbEwPGi4a-3mghhOmF4aqWXSrYXBY9yv9_KR46Cdfkclfso98icy9dVveS0ageTe3qw9jsajkW__oinfBFtPp02dsTbkcdlWl1BgF1cfw4rYk45kIzdBlvwknHEk5iK7d6Hh0GnyibmHmhqOTv-yi3uQdIQhQ_vAAD4yutJEtrMXLi_UKIQpqftyBvrulpLdhFdjEGXepbjMmw579X81H9NNzrmna7DimikQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=HJPex4XPbqnJGMftFuYa6OfsO_abN2mHD8CZi7f-ar-h-V_xgO47Pb2q_BA44UR-efdfct5p89vxem9ZM0nXTlP4baXZPKKdEMo0U4EVRfviiYBWUUDE6pl2p74UAuxB6U3DYQoyhVpRcT3V7TE-isa6cTT89RKSiDV-jHuVYuyPYyyPF2AKPWiT9GOEpMu92zlKdMa4KgXK7-TY1V-oO0O5Tqn0xJ-pgF0BTNIMaR5Z4UGyisVtMvmPk-VxzvisbRVEqJYbcGEIKxWADOyOIghuqajViHak8IvaYjkImZMlG1BHNcCuHpC17Zvrg44yV0v3APXCt37fkZqQjrnR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=HJPex4XPbqnJGMftFuYa6OfsO_abN2mHD8CZi7f-ar-h-V_xgO47Pb2q_BA44UR-efdfct5p89vxem9ZM0nXTlP4baXZPKKdEMo0U4EVRfviiYBWUUDE6pl2p74UAuxB6U3DYQoyhVpRcT3V7TE-isa6cTT89RKSiDV-jHuVYuyPYyyPF2AKPWiT9GOEpMu92zlKdMa4KgXK7-TY1V-oO0O5Tqn0xJ-pgF0BTNIMaR5Z4UGyisVtMvmPk-VxzvisbRVEqJYbcGEIKxWADOyOIghuqajViHak8IvaYjkImZMlG1BHNcCuHpC17Zvrg44yV0v3APXCt37fkZqQjrnR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjjP61JdTVCdNw1PgDMAv7-bevs9mmfasvlwjaJxUjnehxQ67O-iQPhaiE8d8WtxiOzhghnvkE7lSXeNOKJ1xgzIb_jgtm14kfG8TsEn_cFboJVYxW6tGwCwzgfmBA1Dqb04dZVhj3E-0XLFYeRdjAdNiObzpac9SZwN4H1s-7KYOqIqiQiiKW_S84mJ7kHw_tY-QReUmCSg7G9_ccyy7s6W6zu5bcGU6NGYulnMutOo61pI7iH6o0JYA5g0nDC0ZG_q0IaCXJHIivGqEKg1CVpHxqrYhI4oM8cRjND6MV9ZfsMhIeD6MhUQg6g0mwtHG6JMgvEQFAKOnJJO4_rSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J97-xMYL7b5M9xmXHkv28t8eAZfEXCLOGHL8yu4Vxg4RXElx-mGnHcHt0ZfsgP3vrx0ds9oCh1glkfDDGPY-i1Pl6Vbomt4VLqOwzJ3AXCsqwDXYmg4IMgRPqbrFrL5h1CO3_d369nOoszxIh9y-TrewScJQ_aXVdaGOMgBn6G65IDUVvME4hmcLwi1gqko_SgPwa0z_YmrNsUZU7etdwj2tge5IQw3HrI55G48dsQnYeagUXNmt3GulCmqmTHPYRZpjgE5JWeuKGEy0cFWVgW-TNxAM22nTm9cOjcZsHqDICXK4Z3XZQKcFZzIzCRZdrHbrFe1m05UkhMOcQWHXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد.
از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه، اکنون آن‌ها دوباره فعالیت‌های خود را از سر گرفته و دیشب به دو کشتی عربستان سعودی شلیک کرده‌اند.
لطفاً این واقعیت را مد نظر داشته باشید که اگر آن‌ها دوباره دست به چنین کاری بزنند، ایالات متحده ایران را مسئول خواهد دانست؛ چرا که حوثی‌ها نیروی نیابتی ایران محسوب می‌شوند.
در آن صورت، تنبیه نظامی سنگینی علیه ایران و البته خودِ حوثی‌ها اعمال خواهد شد؛ گروهی که عملکردشان تا پیش از این بسیار حرفه‌ای و هوشمندانه بود و اکنون موجب ناامیدی شدید من شده‌اند.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n08hvWNXbQH5YYz8XqV0iaLbryDnWUYm9ir1-OyrGUSUMevIWHd8o86fSiHOAAGNisaSsQ1bfxZxNqkiRIcvPbdw5N2Pw-3Yr8N-XmnVg62n7YBvNxzRkHE3Ql-errUwuSZdebZWuYNkz03hRL7O6Njfmkwdu1jITs8uvecoFIg8rQ2veSWqnVlJR8spnuHedcnHIvhXmC0x64H50jaCvN9jLwXSPq-VpM05fZLTWrxsc6MZt3WzXyHg97GRlGsaIqNZakj-s5wF5bCKGfTw0-yVtZyTGq-atRzn4P-1r4WbamfVPGht_vDRrbK7zoj5YSNO3PXDXl3R5AAqseHofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=PsqgkhKq0Opxnc_VRTrIb4U_H6uOXKt5icyj2XBCx-fcQ2PzUAIc0pT_YK2VfWAIV4EILY0G25I9yo5B7Pd1EKO1Kan15tKvBvNy44GJD7XBIAAdYlTGmk61bBg1lQQeK83FVnD3eE-iHm7hMMdnyOkj5fLYORrY2srQejfM_OeAn8UUvwGZC1CImOU59ua46rznuK0Ih46QkSRE5lQHKB-DDzAg0pIjpfzxLpik9oU1tqqAReBiZxMaL5LMf3zwX8Ql3UvJuPq3ddmIQrKZw6IZ9kejZTVNHcC_m-dc4DTOQks2-RXBrCq5Dr3AIDA4BSk1Cr83--Fk85NUv8TaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=PsqgkhKq0Opxnc_VRTrIb4U_H6uOXKt5icyj2XBCx-fcQ2PzUAIc0pT_YK2VfWAIV4EILY0G25I9yo5B7Pd1EKO1Kan15tKvBvNy44GJD7XBIAAdYlTGmk61bBg1lQQeK83FVnD3eE-iHm7hMMdnyOkj5fLYORrY2srQejfM_OeAn8UUvwGZC1CImOU59ua46rznuK0Ih46QkSRE5lQHKB-DDzAg0pIjpfzxLpik9oU1tqqAReBiZxMaL5LMf3zwX8Ql3UvJuPq3ddmIQrKZw6IZ9kejZTVNHcC_m-dc4DTOQks2-RXBrCq5Dr3AIDA4BSk1Cr83--Fk85NUv8TaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlJZWBiESMbE_vFnWeXPCkymoNJgXHUvaLC-fJP_KPKztuzskIgaDCna3qBars49gShT0tV5NKewT3RTJvJqkDGdAhFnNLfqjqjCpjVbxSinAkfaFxq_xkmDbxQao1cHYYFnIJ5rHd12yZsjiEaCxz58qgS-WcD-S-OWLh4TLjDY7E68s0MUrO2c1cjotrNQ5-jXoBQzZ7zFgO1T8xeR-rL_LbrGkrG6Z7Vonq6mw7fSWVEo9bn1EEVCvfvzYaFFw-vUJ96SDiaj_McbHMcWi7kvayKP4jm865ITse4YWCPgjkf56indwhYOQXNnj4Bty48_-Er_O-aUZCyl7t03WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=HZlWrPiePeA1o5hmlCakb-fif45Yz50l8xzO81VMv5p0MuVePoMwwlwcQfXLzEl4NLNcVPeA3YP33DBhsRjtmWKwhRUCoV_wlizfnBhfiesS4_ufZAom9E2Bi_Eprq9k_FCFfyFmrJvvTGdnRu3vWDbem2Y2RbaA_jrYgXAsMclAgmsJYK3soa_GbvYdhJi0q03RdOUUkgaen5U5fMWaemfLsgkNstx8fyzUC7zg7QtOXlTLfY_NiRQpiAurFfGr7qV_DaBrsPezvfEueCsYtT8pvQPSfEz5wrWWMHyJU2yeea40IWxhlwC4i5W7qt0oLYvBgyj2q9GO5RZfzJkySVaN5sbB5f75WiHaJKgbnHIHEnA_ha54xd4GtPixCwhGB9olHzuH4wDYgZtLdhYP5h8UPrWp4KnbYxLZ9YXHSfg38CoZDdIJbHLUwKPOertt9MVRjVWu16lx1OwLVbzbwnmn4KMrjljR5ledlA8oOe_EiLE-oVuyRdxfiwrwU0wxKhuf07mgnPejv4m4RqQyCyNV2QAfKSu7VGO_3FCWbSoMTQNGHlWz2CgblYap-ctS0Sp1HckXrYKxw5z4DWk17jYGUz7c9Ou5Q4DZqU80bls_LJn7haiMjh86UCqJmwhF_-gwYsNwX-iuES4RCvOSJqG5hGEqvLo584bI3yyCwUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=HZlWrPiePeA1o5hmlCakb-fif45Yz50l8xzO81VMv5p0MuVePoMwwlwcQfXLzEl4NLNcVPeA3YP33DBhsRjtmWKwhRUCoV_wlizfnBhfiesS4_ufZAom9E2Bi_Eprq9k_FCFfyFmrJvvTGdnRu3vWDbem2Y2RbaA_jrYgXAsMclAgmsJYK3soa_GbvYdhJi0q03RdOUUkgaen5U5fMWaemfLsgkNstx8fyzUC7zg7QtOXlTLfY_NiRQpiAurFfGr7qV_DaBrsPezvfEueCsYtT8pvQPSfEz5wrWWMHyJU2yeea40IWxhlwC4i5W7qt0oLYvBgyj2q9GO5RZfzJkySVaN5sbB5f75WiHaJKgbnHIHEnA_ha54xd4GtPixCwhGB9olHzuH4wDYgZtLdhYP5h8UPrWp4KnbYxLZ9YXHSfg38CoZDdIJbHLUwKPOertt9MVRjVWu16lx1OwLVbzbwnmn4KMrjljR5ledlA8oOe_EiLE-oVuyRdxfiwrwU0wxKhuf07mgnPejv4m4RqQyCyNV2QAfKSu7VGO_3FCWbSoMTQNGHlWz2CgblYap-ctS0Sp1HckXrYKxw5z4DWk17jYGUz7c9Ou5Q4DZqU80bls_LJn7haiMjh86UCqJmwhF_-gwYsNwX-iuES4RCvOSJqG5hGEqvLo584bI3yyCwUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUP5Bp8xcogTptLlrXlfoCYDkVAbYUFJxju5j1cp5gPUSD6URgNT4MmtBT4dl7h-TrL3bJvMIoIbhSnFzC73PNLLfIk9rxSsBCkchgZAF-CAFaa7EM9ikQ-Hjvf4N4QXCm3W_JgiphWNAPBXbMvzjCISi02RePrOK7gjzvVIlfcoCO95y1nAUFgcAJNMKcBg_uqcliCG2v7iKD0MfyXgfwW_vHKFKRZs73aj6y0u-DOR6Wjy1OhCQjwIomPDxzf8Lwsx_DIr_xMGwIaL2V3nHVOB2A-FYjeyI8Yzc3t3G4tugx1EXFpqs-N87dOMPAWaq0rCvggLuTdV5Sa4aEDqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=jVXC7mjqIfu0h8Au4swnQ55mWwRVtCZ5Bbgca7zmCt47gQzamjyYLWdF1QyNHlRKY-pzTv5KjwVvkgEaHELUgweYEoQwmsxfebLo4dVidQB7rpACYaOGqYPdZ_gGi2e_opPQKPV4K6BYht1rNxExqTfVOCmtMN8su6OGvtD-UXuPbK7g15btpQMosCuCddwxyYv9Dqpa8y2zXNlD62bH1fxXYfFjLxAT6OPX9azFWXc2qLo9Jbclzp6kfO5aeSMFIsmQEqjScDm4b71S2iQKCNXtdfpqJxF6Tytx1M_yYWtGpI0huqJqyYPKq5mFA9qj33XCi8GWaSygI6aWrn_scA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=jVXC7mjqIfu0h8Au4swnQ55mWwRVtCZ5Bbgca7zmCt47gQzamjyYLWdF1QyNHlRKY-pzTv5KjwVvkgEaHELUgweYEoQwmsxfebLo4dVidQB7rpACYaOGqYPdZ_gGi2e_opPQKPV4K6BYht1rNxExqTfVOCmtMN8su6OGvtD-UXuPbK7g15btpQMosCuCddwxyYv9Dqpa8y2zXNlD62bH1fxXYfFjLxAT6OPX9azFWXc2qLo9Jbclzp6kfO5aeSMFIsmQEqjScDm4b71S2iQKCNXtdfpqJxF6Tytx1M_yYWtGpI0huqJqyYPKq5mFA9qj33XCi8GWaSygI6aWrn_scA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0c9eSdb08r-rVivA52CFnCTIvIqMrpTnKRY0wQnTi1HoXtcBF2v6okkLz7fZ7DdJL3Ys8SZPrKbRyEOodvlSyaxBKZIDfKdtLs-TDexm8yyRs9nfbHuQau0T7sh5pjXkWiZlvhxHkuPiEQyoHEB2ernMof-N71XVj9_Ty3F-cPQ0GUyQFBlzkIchW7ql-qOgHPQS3YNXzhWbt1_OXwX5zwx0CKW2srXGdMmoGUyZxewBpsab4RW439L1sH1WYPCtwjz83fWW7CqnP7p56UTMHooK6P7Cv00t0QA283xiqWOP2TTaP8hV1yF49YPtuPNRQGKw8B7VCYMEGnVOiA6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=EIDnlQmKwk1xPO5sMStcXWKdiI2ieroIWEAL01veQD6JmEjnmtT1HzqQVqbiiCPy2gf_1KIA2ywQwPKFJa9pUlLUjkF-EnBLXiyPfnmYYF3_ZZe2da-4vRjzDCZY5naF9PMFoCC_uAbqG53sb56jQCV-n4X0zHtPlhE8zH1-ctlOHOij6ShKPDHdLB3E6mBalME5c5MNzt3ss0O9__WqXpDxcqt4SSjZQ5OWGJQn4iJz7j5RZk9L_e1ibz5Mk_wVCTkk74OBpa86_BaitEmHPIAp5yhxTaV91iK-e65HxcWUNHyhaCOyNQc2vtzHx5XokOjeZjF946uqUxBVA0fj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=EIDnlQmKwk1xPO5sMStcXWKdiI2ieroIWEAL01veQD6JmEjnmtT1HzqQVqbiiCPy2gf_1KIA2ywQwPKFJa9pUlLUjkF-EnBLXiyPfnmYYF3_ZZe2da-4vRjzDCZY5naF9PMFoCC_uAbqG53sb56jQCV-n4X0zHtPlhE8zH1-ctlOHOij6ShKPDHdLB3E6mBalME5c5MNzt3ss0O9__WqXpDxcqt4SSjZQ5OWGJQn4iJz7j5RZk9L_e1ibz5Mk_wVCTkk74OBpa86_BaitEmHPIAp5yhxTaV91iK-e65HxcWUNHyhaCOyNQc2vtzHx5XokOjeZjF946uqUxBVA0fj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
عراقچی می‌گوید سیاست آن‌ها "چشم در برابر چشم" است.
سیاست ترامپ "سر در برابر چشم" است.
آن‌ها بهای بسیار سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzaQu3zoy15SukZGy8R50deJP7Jg7X6b2ZXL0NJNg4G12WRzdFrNch1cbzKKDTs7CTKtaE93cqtczEa39t6JzwsuM7oumJ7wJsdlzGq6U3A8bW6DZhTQdeyfOXfoggIJ6AKWPjofhvv1JfsmQ2i4umGQL8ny3uUzjxn_gdAp3xxvSN-95GndkwQbl3ZmZR3EVj0liyl2KTSLK3RF9_6-HpTpFRhzVHCjcLf4AreT9T6ZgG6J3279XHVudeZ0In5POMcqBvEwUELDW39Qk3i54T6lECYIquv8fE36cN8NVVmyY3a7AXZ-1-1rJry6GtOy_JSt02jq6W5wxVdnM9RCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=pj9Fh6QgpeaziedWtui6weQorZEYwvTfx49Gdu3WM7i_6o9Ks3eOPdEs0iS8m-ZlQjbAokWVDdrR8paaz-tq6_ku17Fs_4WEf2gq9fCmhmy226V-pHGqZ94jrEp6Q2XZJPPKbh82u2t13WBj3x2zqOWUnC5wx-UEZaJASWg9QpzXfIqCisAz1AwclfzszTUAaNOgNImnf9c9p69gfyRY1PmKs83bZVQoCxqhORFsoOba1lrcLZgqS3HCOVM_v_Y5CqPWMKkF7Qeq61HqRdbtQcXqeKSgIzwpEuU5UaEL7YLHGTxhDocrKr9xoyoyXITsHaWeeIiNOUNEy44aETBk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=pj9Fh6QgpeaziedWtui6weQorZEYwvTfx49Gdu3WM7i_6o9Ks3eOPdEs0iS8m-ZlQjbAokWVDdrR8paaz-tq6_ku17Fs_4WEf2gq9fCmhmy226V-pHGqZ94jrEp6Q2XZJPPKbh82u2t13WBj3x2zqOWUnC5wx-UEZaJASWg9QpzXfIqCisAz1AwclfzszTUAaNOgNImnf9c9p69gfyRY1PmKs83bZVQoCxqhORFsoOba1lrcLZgqS3HCOVM_v_Y5CqPWMKkF7Qeq61HqRdbtQcXqeKSgIzwpEuU5UaEL7YLHGTxhDocrKr9xoyoyXITsHaWeeIiNOUNEy44aETBk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای ناموسی در پخش زنده
😃
⏺
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌ گید تنگه رو باز کنیم، مفت بدیم بره.
⏺
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
⏺
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=ggr8nyNcAOceg5zygr5XkOWo-979ZVTyvXpZBvJX2sew_s1LiUXFxNu5vuEbqhIdWT1v2PertvE7FoqvMJFAJuWPKJp6GnxaR8Ly9e9dGeh1BwVkDMtJ-ie1PzIJjfTxSY1aR8LnwY4qG4JDiiK1QT_-zUiKEADEV9P8FOVFsytuwX-h1YlrPQ9YE-w-K96wM6fToAY0pszdKe72OZu9iDhMYRzFi9ljqahOxhzZk5TBDjXR-v_q30-b5yMucnkoZ45rLP_yazflIgQXsayy_EOVE5kxBVLWzmzye9eiAIzpfj14NYA8oKYukTz-uaRnREEIabDzusgzCwlJ-IZjfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=ggr8nyNcAOceg5zygr5XkOWo-979ZVTyvXpZBvJX2sew_s1LiUXFxNu5vuEbqhIdWT1v2PertvE7FoqvMJFAJuWPKJp6GnxaR8Ly9e9dGeh1BwVkDMtJ-ie1PzIJjfTxSY1aR8LnwY4qG4JDiiK1QT_-zUiKEADEV9P8FOVFsytuwX-h1YlrPQ9YE-w-K96wM6fToAY0pszdKe72OZu9iDhMYRzFi9ljqahOxhzZk5TBDjXR-v_q30-b5yMucnkoZ45rLP_yazflIgQXsayy_EOVE5kxBVLWzmzye9eiAIzpfj14NYA8oKYukTz-uaRnREEIabDzusgzCwlJ-IZjfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دعوا بالا گرفته بین قالیباف و افراد افراطی!
🟡
الله کرم رئیس گروه فشار:
بهتون اصلا اجازه نمیدیم به هیچ وجه اورانیوم بدید بره.
🇮🇷
مشاور قالیباف:
به عنوان کی داری اینو میگی؟ نماینده مردمی؟ اندازه حزبت حرفت بزن زیادی نگو.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68841" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68839">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=oujL-tBepBqIoJ2fAJHSRXc2m_rcilLaFUuIslYEoAK6LtdVMDcu5vdEbWejJSUEYCV6XZtp5g-CqUTWmB6M25ysDQw7kbi7LFtDpqU5eJMh8Ya7OdXVddy-xcCpfDgJZwJBLd9Vj1QtN4a8DE3eaQQpQELJm5jzLevhtyqDmtc6btu37dpu6BBZAzyK_umjlVRtSLFh11BPWTUbQ3_Qg6VRmZ9uphigVz0k4HKd4HW84M0LrJp5wWaQEF-4NBzJbvQvhRwIWafDtbOeCCvyHmJ5ImILvQGu_mydviscvKwsPlYjac664U8GMJgeAOGyLyW3CrdmYswPmxCQww9Bdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=oujL-tBepBqIoJ2fAJHSRXc2m_rcilLaFUuIslYEoAK6LtdVMDcu5vdEbWejJSUEYCV6XZtp5g-CqUTWmB6M25ysDQw7kbi7LFtDpqU5eJMh8Ya7OdXVddy-xcCpfDgJZwJBLd9Vj1QtN4a8DE3eaQQpQELJm5jzLevhtyqDmtc6btu37dpu6BBZAzyK_umjlVRtSLFh11BPWTUbQ3_Qg6VRmZ9uphigVz0k4HKd4HW84M0LrJp5wWaQEF-4NBzJbvQvhRwIWafDtbOeCCvyHmJ5ImILvQGu_mydviscvKwsPlYjac664U8GMJgeAOGyLyW3CrdmYswPmxCQww9Bdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/soX-Uh6hcLBSm4KxeIhJ5FqjIyKa12R0dYRCknmHJHX8A9FE-f2oNioLlVu0OFFhLwPxyk_WNyfB0z8-MSgPlu-Axn6vWnPSOK3pXpZTenm_dA7dVXrqpkZmwYi40wwC8VbJebAsbVfP5UmMTo9dFkAYVvX9BH8_L3HdRUxRp6mzjDU6fB6GfbPj6bj_HNQGpf-5ogNExsWim6BiBWpAaENzlE7M-A7JnPCUr64q8C3g6-c03MC4hcMvFZWGhZVxmm6eHaqQqHX66o5ShClKfkqVWQKwWuWAF6oCbZSmJRQKHBLWdR8PKkkIJ-Uts1xsa_gio87qnCxEBqd0xnCeTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQQ0mVdacPstSJl5xyjsAdRDEOGKZLiMkPy8uotTKSOLo3NWWNfINfXITAQnGLAAIUYMK1RqJEA4UtVp6yJ9YT6Fte9NxmiyvKiKh7jbWErmTxcM-UVntmHluqGuPXotRhhi9_Z9jseckevs22Hq7jGwh20Tu4BaGOTD8k-xkW2k_cxX-8KlA3b3IoX72iNGRsLOrF0ZeXVhs-5bFmTwTtg_vfpxev1Oq87hSMJlb-GtNT45iyq9ME1yl0_1y2xpcohUMGZBXrF3ritGnyI4poICouVv3AyqhdEvX1G1WNP5cjs0qb8qpuTvHSizLAVTapTKsYel_KPmwi-NRNaOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=XKD75xp8apOeMsSmQ3lXsP6cBE7c7w6p0O9m7Vo2y1Tni6JSgKOXMu1DVl7zXQhpCaUpCiJa3udamItfw0vaKEzTpiSoOhaZdWrSYMOkOYUsX-zQS8y3DtbVZHU58vsvXe722hgWBzB2QDDL2qsPf-KLvQS37rcaMMIeHt2tWUOQDNM0DlPWwXYB8pDLmswSScH7ObBsjTuVc6lTSuNxiyYhfMG441jFU6LSFSbDm-7x490Nea2udE5P_dNcH729WheVH--cD5W7LwnzpLs0og3yR0j33icN1slngN691EXVd-dwpPZt-Jaj-xWkWObViU_xjqUNrz9TUypPbqCWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=XKD75xp8apOeMsSmQ3lXsP6cBE7c7w6p0O9m7Vo2y1Tni6JSgKOXMu1DVl7zXQhpCaUpCiJa3udamItfw0vaKEzTpiSoOhaZdWrSYMOkOYUsX-zQS8y3DtbVZHU58vsvXe722hgWBzB2QDDL2qsPf-KLvQS37rcaMMIeHt2tWUOQDNM0DlPWwXYB8pDLmswSScH7ObBsjTuVc6lTSuNxiyYhfMG441jFU6LSFSbDm-7x490Nea2udE5P_dNcH729WheVH--cD5W7LwnzpLs0og3yR0j33icN1slngN691EXVd-dwpPZt-Jaj-xWkWObViU_xjqUNrz9TUypPbqCWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛مجلس نمایندگان آمریکا لایحه سیاست دفاعی ۱.۱۵ تریلیون دلاری را با اختلاف آرای اندک (۲۱۶ رأی موافق در برابر ۲۱۲ رأی مخالف) تصویب کرد.
این طرح شامل 95 میلیارد دلار بودجه نظامی اضافی است که عمدتاً برای تأمین هزینه‌های مرتبط با جنگ علیه ایران در نظر گرفته شده است.
این لایحه اکنون برای بررسی به مجلس سنا ارجاع خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68835" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68834">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0hru1Lr04gM0V5ROdAvYjMji1PHq3SUktopY-J4ywK7ejwlqqXkgwJDgWnMZCBOcutvv1smFexIRz6MDw4cCV_wJyQMGyV_VbdoAXib_8Pj73mjrCJJAD068N2kAmesxSXxWJHQjT0lGTQe8FwSFJp9yiiH-huzGmhShQdzZ1EOrDEKlCnNjyhvP5nle0DfXRI7iRBftgvAGAGFygV3AvfCeiGxvJ886P3SZmfwRj4Qz3X-0hZIwQcVUBJMO_zSiCQRHVu62bxDistTUt_gKWABijX77-H3u-HgK8yamQdJ45e4atW1ZSnbdQs82a3ab4wHoeEV7Is4azi3RRF3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPYzyLotDAn_M200zMnhbYsfWfySmt_6ZHx0uCz8jDl9dABGNjFXr-HWabeHc3NUnPtzqglMIm6rxl5XO61S8TH33vt84GanG5BhsjziD5QdxJZLPgmjJgYbLo9YBQG9-oFiIo1qYFXJl2_PF9MO6G34HY9woz3fn4ecfU1t1tRSrDSc_Tgr0mHemganqwNNWyT-ecvE7EXWK5aGsxF6C8AHzXr3vbpgN26WQhTBsmd8zF-0BhTisTizmdSoo-9lEQ3SG6LHFGK7B5iJVysytGzV_V1KpjcgDNAx7vzH6TOc1b8RCfDmWFLMBVCaEi89qvQN9jYmapA0C41jYOByhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLdTFOhplI4qxCpZwC1duymJFQEBC2VRmQRPe5ghjLAOHmaU1nYGzawBQeO5VukN0wHKdUTObJ6l_4Ga5DNe9lFGGtB8wFVjMEUxeEjffh_MHrHIWF3e1Mrxfb6zjINu3y1ZMDTfcNmDYc1Kqgs0DXhWfxd0VwHxjeabRAiPHOlSOeXDLpo-tdKbwWDiySRox0IyLyBQ3Ggyd6r1URf8wNJ5oGQj3D_npF4oUgPZzlkMUMe5pLiAnY2g1fdgLnSlIVQaQcQwMavSW0iaA5axIt9KYEPL76fZv-FsHGbUMXWceXTenJQzV3o4CYpjZ3kdNkdvmaGE2F7dm3thXETbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=MKgS6NHw9XNzkjRph3DsCZeUUJ4W77X9HWcgvt6Hkr6aCUDDoaU--3w9F6KGX5Ps4rfVjsDMdAXs9z3hdm7hbx4iyV-0QaZ_A8zxJcFVkFdoFgWEUzF8kUecIv68IIRTcoln9jLDiYQS6DzAQB_LgrxQ2kpBjmB7fp_aL7fl3UCfjihust1rOZkQk1HcyXF2V-ZK12UjjPAiHyB_zFwTNSVvgw3HdQ0NODex9Gfn1rskaHljVW3abjlCwFeSQysU9U_b9FZNG0eceS0WNI6ppdoEFZPkWYrkQZdA4rh1W-G9rj-lJv1ZjzmuNaE7cdevmCx0lRsM7T9qGjOTILDFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=MKgS6NHw9XNzkjRph3DsCZeUUJ4W77X9HWcgvt6Hkr6aCUDDoaU--3w9F6KGX5Ps4rfVjsDMdAXs9z3hdm7hbx4iyV-0QaZ_A8zxJcFVkFdoFgWEUzF8kUecIv68IIRTcoln9jLDiYQS6DzAQB_LgrxQ2kpBjmB7fp_aL7fl3UCfjihust1rOZkQk1HcyXF2V-ZK12UjjPAiHyB_zFwTNSVvgw3HdQ0NODex9Gfn1rskaHljVW3abjlCwFeSQysU9U_b9FZNG0eceS0WNI6ppdoEFZPkWYrkQZdA4rh1W-G9rj-lJv1ZjzmuNaE7cdevmCx0lRsM7T9qGjOTILDFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68827">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
فارس:
حملۀ موشکی دشمن آمریکایی به یک سولۀ انبار آسفالت در اطراف رامشیر استان خوزستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68827" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68826">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI8HRQOhYXQZgtZt0k41PQzYGPpg4bT8eZrmHcW82dII0-D9Zizd8Q_UfXf2IZZv83r0V7U1OANpnhSVQoeDx_pMpNb0MUAnBAI8IotqyQ4vDmOdMLfnW2wJz9i9pkUw9cDyUkNRKUViZIjJ3rsYkdpQrmXTvdwrT_caZmVJPh2ofJcqFLVj6XZswy0FDslMt10YimU2v4qQ_gsPKC7z-cQoswjsqPlDoxMoeZWgBAVZqlSrPkMMIhxGIHqDK2Q6ExnWRgrleG3mlVthrf5moPawArzrlKb1SfcS0I5c7jBv7M7EZBCK9hz26AfnCRuCFaekG03ZXSJLJVi6tY0Crg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یک جریان مداوم از تجهیزات هوایی آمریکایی به سمت خاورمیانه در حال انجام است، که احتمالاً شامل هواپیماهای تانکر سوخت‌رسان نیز می‌شود، در چارچوب آمادگی‌ها برای تشدید عملیات نظامی علیه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68826" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68825">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
پاسگاه دریایی زیارت در سیریک هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68825" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68824">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
دقایقی قبل صدای چندین انفجار در اهواز و ماهشهر نیز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68824" target="_blank">📅 00:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68823">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
صداوسیما:
چند دقیقه پیش، صدای انفجاری در منطقه بمانی، واقع در شهرستان سیریک، شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68823" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68822">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030860acf9.mp4?token=jxoazNTqMthbWansIcWhv2TDFJ6YmFcRHv2VltqBgFevdWL2jM91T_WS0kgNOt5zmcEpjexzJRKyhrWYo9NqKgLcx7AtgU14S7p_K5P5AGPE4qF48sOnb0JQXTBFL8GY7DH7gXbuxOTt_OM4HbjoXXjAATCz4F6xvuDgRKZ2A7jNgsQ6PEeT_xqb3JqhZPT9LGYuCFcXPt17QySiHGok2tlUW5qT0qh9raKvfUE4ZpmDX82Ub5GO_go8wB2ktpAQpvWTDQ48hLo7t6W1-SxoPxI9QyNzEIhePOAAm9dlxi4ZJUSgVpsXQXLu1M4HeShJ2qxb7WLy0RKZJMcYGtgGIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030860acf9.mp4?token=jxoazNTqMthbWansIcWhv2TDFJ6YmFcRHv2VltqBgFevdWL2jM91T_WS0kgNOt5zmcEpjexzJRKyhrWYo9NqKgLcx7AtgU14S7p_K5P5AGPE4qF48sOnb0JQXTBFL8GY7DH7gXbuxOTt_OM4HbjoXXjAATCz4F6xvuDgRKZ2A7jNgsQ6PEeT_xqb3JqhZPT9LGYuCFcXPt17QySiHGok2tlUW5qT0qh9raKvfUE4ZpmDX82Ub5GO_go8wB2ktpAQpvWTDQ48hLo7t6W1-SxoPxI9QyNzEIhePOAAm9dlxi4ZJUSgVpsXQXLu1M4HeShJ2qxb7WLy0RKZJMcYGtgGIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه روز پیش که پل کهورستان رو زدن ، سریع اومدن یه جاده آسفالت از رودخونه خشک شده اونجا کشیدن که رفت‌وآمد متوقف نشه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68822" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68821">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=IljllSFwRb6bc1m4iCdpavkfnARiYlO-sL7pAYMl1Yb5Z-51MJmWUHFcANQchjNKAsVzm6E82amsCatn0tJMzZ0Dq-o9H0cb-jFtFkqcq1Gp5aCQJAN-Ce4WrGcOBDx-XdzEWHXAkVKf_6hTJH8wmPHtoVgdHT9jNNpSO85acQZDhXR8rdvq2wGZenNmw4hWpMT21j3XI_GRK7Sxi5p0u1N0W2tUEaibTl5J03TO4d8QQlCHSnaPR8hqcEy8TjrM8Q5x6tC83EMZPAwI4BnPeLXXGkPz5-7TGsuFvMlCT1Gz1YtM7yUzmBgpuRNL2C8BnUFd-qIrfR6zl7D2xX6-MIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=IljllSFwRb6bc1m4iCdpavkfnARiYlO-sL7pAYMl1Yb5Z-51MJmWUHFcANQchjNKAsVzm6E82amsCatn0tJMzZ0Dq-o9H0cb-jFtFkqcq1Gp5aCQJAN-Ce4WrGcOBDx-XdzEWHXAkVKf_6hTJH8wmPHtoVgdHT9jNNpSO85acQZDhXR8rdvq2wGZenNmw4hWpMT21j3XI_GRK7Sxi5p0u1N0W2tUEaibTl5J03TO4d8QQlCHSnaPR8hqcEy8TjrM8Q5x6tC83EMZPAwI4BnPeLXXGkPz5-7TGsuFvMlCT1Gz1YtM7yUzmBgpuRNL2C8BnUFd-qIrfR6zl7D2xX6-MIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به تنگه‌ها احتیاجی نداریم؛ اصلاً به هیچ‌کدومشون نیاز نداریم.
ما نیازی به تنگه هرمز نداریم، اما مجبوریم این کار رو انجام بدیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.
من اسمش رو جنگ نمی‌ذارم؛ یه درگیری محدود بین ما و جمهوری اسلامی ایران.
اون‌ها اون‌قدر تحت فشار و ضربه هستن که می‌خوان توافق کنن، ولی به نظر من هنوز آماده توافق نیستن.
الان هنوز آماده توافق نیستن.
ولی خیلی زود آماده می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68821" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68820">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
ستاد مرکزی خاتم‌الأنبیا:
رئیس‌جمهور ایالات متحده، که رفتاری بی‌منطق و جنایتکارانه دارد و به قتل کودکان متهم است، بار دیگر تهدید کرده است که به زیرساخت‌های این کشور حمله خواهد کرد.
اگر این تهدیدات آمریکا عملی شوند، نیروهای مسلح جمهوری اسلامی ایران اجازه نخواهند داد حتی یک قطره نفت از کشورهای منطقه صادر شود، و زیرساخت‌های نفت، گاز، برق و اقتصادی منطقه هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68820" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68819">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=tp8PjHSNKtwN8GxsW7ipYe_8ZL04v7RxNuS_u0v9hIrBgqCIIlAd_11kOGOsXFAmzLPisJhcFg2TZhQwJ4rWOg9u-P5LSGZZtWa_FsGbINvPIng02C4cxEfTEk_t0eT54QG9SpvYow2DT7_4LY-1tSafqb7yZjp4tEi8pdZJGydx9n7HMZaTwRAvjEfFtXI62qIg8OEPDAon216YzYPb7ML9tN5pdI3Vjlk4GrmllhUUp-yTVCs_vFx3sFNtZ55XfZfuHNMKFSuGAzToUbMNG1JI6eLdzB4dVqhLVW9P_Mx_pH0qXM1jRv37gLMOXjFdsFNMg55xF4WT0pJ0F025bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=tp8PjHSNKtwN8GxsW7ipYe_8ZL04v7RxNuS_u0v9hIrBgqCIIlAd_11kOGOsXFAmzLPisJhcFg2TZhQwJ4rWOg9u-P5LSGZZtWa_FsGbINvPIng02C4cxEfTEk_t0eT54QG9SpvYow2DT7_4LY-1tSafqb7yZjp4tEi8pdZJGydx9n7HMZaTwRAvjEfFtXI62qIg8OEPDAon216YzYPb7ML9tN5pdI3Vjlk4GrmllhUUp-yTVCs_vFx3sFNtZ55XfZfuHNMKFSuGAzToUbMNG1JI6eLdzB4dVqhLVW9P_Mx_pH0qXM1jRv37gLMOXjFdsFNMg55xF4WT0pJ0F025bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو این اوضاع ویدیو های سمی هم وایرال میشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68819" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68818">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDNbzh3hPj_nP9UWkrd-siJ2klbVimOP_A3uyeT8AtdT0B0acyp7URYTUez3mSKCkDNaTGEMhppld84hAuC0UUZhdT8wosjkncJUCdoIVL86gMHBhhDeuPTI_qjNVqXP9WoNGQclXl79UndZ3tDww6g8AIhVsuDESGAbAupZZREdyQBR8HISUBf8dggSwUVyJEDVi872Yg4oYzVkq2hC1B1YSH8bj6nWnU1JW3FtLF0rAg-ZVq-4pcgp0UDAL5s8nkq7CYBA18E9YRkCq9r7Pu7iBSngpGm6FMEbb8O2nJJTIQSFS7iORPr9DQz7TyxLG0gwqRpgvBNmPq8EuBQsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید موسوی فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما حمله بشه
خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعیه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68818" target="_blank">📅 22:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68817">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=Bifdjp6xMum2YwhGWIS740byiYQlJ_YusrRiubW1tJWI_l49FtlX7gPQWoYSAa1MLZF0GMNQdZwRT4N6cLHypr-cu7-TqQR0F20zFmjPuvMQGXQ5vJsRy1wEH5drIIVFzSd2KckVr3CdUECGcKxdWYkvlPjnjqw2SAqGT9tYiCfth3pKWDEj_WNWSaCsCq4GZ-3rmTl97kW7KYbIMRBZ6eLeqGUEl90EUP411iAVaba2w8oi0BWRvr-HWYCySKS1NRCfG6HI6NcePDG3_ynCg4S9JTc8THrCqaVLjQBlH6J5c3882dYLAlYMrDFqctTQ9S1q_BEbJKoWkeoYAXxm-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=Bifdjp6xMum2YwhGWIS740byiYQlJ_YusrRiubW1tJWI_l49FtlX7gPQWoYSAa1MLZF0GMNQdZwRT4N6cLHypr-cu7-TqQR0F20zFmjPuvMQGXQ5vJsRy1wEH5drIIVFzSd2KckVr3CdUECGcKxdWYkvlPjnjqw2SAqGT9tYiCfth3pKWDEj_WNWSaCsCq4GZ-3rmTl97kW7KYbIMRBZ6eLeqGUEl90EUP411iAVaba2w8oi0BWRvr-HWYCySKS1NRCfG6HI6NcePDG3_ynCg4S9JTc8THrCqaVLjQBlH6J5c3882dYLAlYMrDFqctTQ9S1q_BEbJKoWkeoYAXxm-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهر چهارشنبه؛ لانچر مستقر در تپه‌های پشت اسکله طاهرویی (سیریک) که روز گذشته مسئولیت شلیک به سمت کشتی‌ها در تنگه هرمز را برعهده داشت، خود هدف اصابت موشک قرار گرفت و یک ستون دود از محل برخورد دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68817" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68816">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbDHC6QfLDXz1YXXaXdh2zjyAOqv3vOS_wX1uZTIWhWMHA99pm9p75GQz4pjkYPsaPHfnvcgTET1DMZC-_EMgskEw9EauvgxmGx8m1YKKeNvDcFQ7ld_BDSEGlifvwC-UIhhyBzRy90wsWCQVzXqPuW7cFtPQptLk5kcT0Hir79ibcgLS19BGJv7wkEodUeLC1XENTanekekD7WgfAWSUKzQJ_tKXuie1Ki-0qBoECYDO11pDTgGVakq_JA4HIsab8qQiMOQb6r-eQaR-jlw-TCuOR5mU4dfQouNE1pymLZ5LQkF4rqwXVQZumQ2WSO2ci4R2kW7c4Jv6FJnIhB20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت.
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است.
بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68816" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68815">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAu6_ioni2ypBcpJ_C5IO6hoP_swachDM6bQhZ8D5zA-do0Zp5CrhOdgsJWUc_3scd5ThEQzt-kDBAb-NvVrm0nUvIQwAl2a-SQ2kL-ik21Kd_ams352UAU5fsbGdJvjU72KQAwhd1U5grKbZgsDGoS2vgSnhIFXbaECYBVmGhPgLWpqzI9JXg6_b6ESxI71NoamqfLR8cyLW0x-XE5DD990P074ZFyv5ZpXZUUxabdlQBuYKTjz_kYi-7DPQaa4ozRnKNpN2HYkdJ2_CMlD_DrXUl6Hn2APshbJDofp9iAgZUdSQ-tIcRj-z7Is280nh9cy4EeNsDa0w5m3apT2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال:
رئیس‌جمهور ترامپ به‌تازگی اعلام کرد که پس از کشته شدن نیروهای آمریکایی، به «سنتکام» (فرماندهی مرکزی ایالات متحده) دستور داده است تا «درهای جهنم» را به روی ایران بگشاید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68815" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68814">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68814" target="_blank">📅 20:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68813">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9FDxXVwo1SO0J_NNB6To3JJQ4xeuINAFFq7bg-4hyppji9bHO6-vnAOVBGsrQz1PeDJtv_tQ4Ksmeka6OMKqT0bZ1L5o85weikNZLfubTK9ITvONDyB2yHcnb8c0uYfuI5sp9pIgSac51clEwiYIxj0nOOXrEcaJ-1nPylDoZYm64bDQtZ0Q1wr9xSjG09xEctKZe-fCiqq5fSbU020sRdhY7x1Nki5csNntJPQaPdhlZ3wQMOgKT3BwwGsnKqkjep1Lp4-sENTF6StZnbfcoj1y5iH5YUqW0AIM7f0PY1Y7cLrUOZZ6cuIns6VZvdQ3rN0l2pjeR-K2_YsGR_HLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68813" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68812">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3yZWZqoJXAv-qeC-Y5N8S3doevjE3cIUru1899nfnTsO1fSoBLm2R3hSbvqdG58P8QIOgl8CJLxkcV0dIYDGphgVdLossaQlfGPveB-Kgj8tS4I6fucwoB0S4WKy2ZJ1DcrXNjayFi53BR0QcyzT_dcCDIkPVInt_Obr2EBj15Y_38jboXBFS6JdWavOYbev1grCyaw7_5z8YBmAM9TpYvXbFciRGAb6ugPNd94kcMiqr6MHNPWERgokzh03SsxrIadM-JLHWqg_uhJfo43yJxqhLZgdBrg9wUCjC4-lKKuZ1Hqs0zNRJlMLVuXuw9A5zYXDCnjPU33_Il-QaEo4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یکی از حملاتی که شب گذشته توسط سنتکام در جریان یازدهمین شب متوالی عملیات علیه ایران اعلام شد، بخش نظامی فرودگاه بوشهر را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68812" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68811">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyHig1etRKD2n-5vOUHsri3ODturlXRE_m2k1NGwHyhxu705epDd3B8wxrLkVbJR5ShIpiL17Ke0DAMYnbsrGJeBchuMLXGgGdGYHN8PTU5eTc7BGbol2tPmrS09Z0JVOTHujXwXjcLg9GasFtTCO4vc9Gx17nOZ1odRGtxAMlBXTcCqEYIWSeKdv-Q10YXW8HjvVk7caPCSVJi75MmVSoG9yDvn4BClg7PaDdUbWfnDJGHz61aCo0q1a9WcAkkRn7twhNQhU9SKEkzoXmwJUzafKahZed0qcARbiEjYaJY4IrY5uP9zurPLXHb8re7s2Uy4DqydzSL2DZrZWoxUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قیمت نفت خام برنت به 93.14 دلار به ازای هر بشکه افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68811" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68810">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbxHZIvIxGyevNOV_vvAWYslygz3929ZnUXsliEkVfRMlpQBANrt5kfvGdipD-cbKBh3zhJ1A1r9AF5HD3xme0Tn-T_Y-s3U9GwHuUAexmVtCwXlLjqU9Ym29qBTYA_KeILHeG1BddjFDxhhb3gPpnhWUnCOme5ir17DwUYm4JyFRBUPRksqRblR3_Kb4xwPObrDS8AADpEHj-h04f08dCptI3ni4dp2ZSeiYBfPA46DDfZ61_7VL38lMGgpNTanHRKsjRMl006ATaEjjMwrOFiADvwnLw3iWnkHtCcdPtzozLCUGis1TCsU0okFVd19LriU2-BeSAbBGhZgw2vwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68810" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68809">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=IfiP2uz_QafBt0X7FwYUu5Z0nssLpF1DGklHNyLroHBnvMIF50yDywwwOlo8z5x7v-_Mn50Wdo9oj-28cmWkMfWrqKLx0mwT3PacLqsLn89oCwDxyYBEnWimQFTgks5RaWL5_BcOCnI1DKKU1CdsnPmfaypM3jHkiJ6jAM7JykLotFPweW4k5UzyrZgItsNj6T-YZ224nxAej8oZyYURxMsVmbTqT4JxQKqUABPnTXKUIGOoEQCyBbpgZA2CiLDA3E7X0EW0ri0dREz_I9TpFPrnnaDzdEf0COhQtUAKgz6zkTAcx3ZG-g4zmsi9zw2QrXanDZHKyBjrJTUCqt23-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=IfiP2uz_QafBt0X7FwYUu5Z0nssLpF1DGklHNyLroHBnvMIF50yDywwwOlo8z5x7v-_Mn50Wdo9oj-28cmWkMfWrqKLx0mwT3PacLqsLn89oCwDxyYBEnWimQFTgks5RaWL5_BcOCnI1DKKU1CdsnPmfaypM3jHkiJ6jAM7JykLotFPweW4k5UzyrZgItsNj6T-YZ224nxAej8oZyYURxMsVmbTqT4JxQKqUABPnTXKUIGOoEQCyBbpgZA2CiLDA3E7X0EW0ri0dREz_I9TpFPrnnaDzdEf0COhQtUAKgz6zkTAcx3ZG-g4zmsi9zw2QrXanDZHKyBjrJTUCqt23-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس انقد کد کد کرد که
کص
از دهنش پرید بیرون
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68809" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68808">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=CP7iUiEzzKbXmXBAA7FcCEwSqAY8os2E0DDW4n3DltMLAjXQ1fDD0AHlLphEB2v-I9j0mmyDUlNy6I67Fxn9ODb6VjtBI7JCV6qKqK11NlGeUjkKjEvoJGFj-FyEe8HySVzd1FbmTmWojyhz6aPgI7Va2EDSfTukrCKTOrvrvstHsz9aQIr9WOJVC0l14P_d6QqmNc9rpQehGIzoaHEfIRRFhANNutYbskZfDxibZqEVCSXnzL7VVDn3hekr3sqJBdpP36HIqjtzNrovj8CMf7NoF4HpOq407TrkHZlRP9vfJyQGqpFOr_dILDjkOCxzexVTg5iR0NfpXdNyvpVQ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=CP7iUiEzzKbXmXBAA7FcCEwSqAY8os2E0DDW4n3DltMLAjXQ1fDD0AHlLphEB2v-I9j0mmyDUlNy6I67Fxn9ODb6VjtBI7JCV6qKqK11NlGeUjkKjEvoJGFj-FyEe8HySVzd1FbmTmWojyhz6aPgI7Va2EDSfTukrCKTOrvrvstHsz9aQIr9WOJVC0l14P_d6QqmNc9rpQehGIzoaHEfIRRFhANNutYbskZfDxibZqEVCSXnzL7VVDn3hekr3sqJBdpP36HIqjtzNrovj8CMf7NoF4HpOq407TrkHZlRP9vfJyQGqpFOr_dILDjkOCxzexVTg5iR0NfpXdNyvpVQ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
عراقچی: ما به هیچ عنوان غافلگیر نشدیم!
واسه همه سناریوها برنامه داشتیم و کد بندی شده بودن.
سناریو آخر این بود که رهبری (علی خامنه‌ای) رو بزنن که کدش 110 بود.
تو جلسات کسی دلش نمیومد درباره این کد صحبت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68808" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68807">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
یک منبع نظامی به تسنیم:
هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68807" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:  بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68806" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=WolfuMmj8p8b8mVFzKMPYteQGxI1KIZ61DdFpeedOD7r8SAXU_jxYfpT_VKSq_rBv5Lox5uyoRq1vPrf-a1JJqOvyjbhLmFOGdDoTy6dxKqKJV9T3okBcsBztoEvHF5ZnjUwKk3v-qyIyA4FBMqpITYzUmXVhixkMgndjUo2uK5o8VNYPjYtGUJb33fb0NjWzWObWQyHqXjkoGL9SzF5Gh72jqo-RtMT5kH4YJhXMsGjtQWEwp-xOBtVY6G4j-hs0llQo_1zBW3zwFXU-0S2S85_KVks1t36MZwi8RPhFO7OSG2XQhGbvCaa0zAv0AiMNtuyu0rstZKaCel4g5gMzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=WolfuMmj8p8b8mVFzKMPYteQGxI1KIZ61DdFpeedOD7r8SAXU_jxYfpT_VKSq_rBv5Lox5uyoRq1vPrf-a1JJqOvyjbhLmFOGdDoTy6dxKqKJV9T3okBcsBztoEvHF5ZnjUwKk3v-qyIyA4FBMqpITYzUmXVhixkMgndjUo2uK5o8VNYPjYtGUJb33fb0NjWzWObWQyHqXjkoGL9SzF5Gh72jqo-RtMT5kH4YJhXMsGjtQWEwp-xOBtVY6G4j-hs0llQo_1zBW3zwFXU-0S2S85_KVks1t36MZwi8RPhFO7OSG2XQhGbvCaa0zAv0AiMNtuyu0rstZKaCel4g5gMzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
دونالد ترامپ درباره ایران:
«آن‌ها بهای سنگینی خواهند پرداخت. آن‌ها در حال نابود شدن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68805" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhXtxVtCGOYSKcyX4hgfjzxiJFOFS47V06xSfcAlgH-vFS4hRN37g2-mUkD7_8pYWM5RM7IdrI6ZoNQVUZT2SHJIQAAjuAWnejUjqarKDdhKyNUaFvKKItjN0mzev55eYgsDwXRAuBqyeoZ7T_iSS1Wq9HlyPoDr_B_CkTcSBmSx8mNoWTGp_zvgokcRX3MPd1RqZOySIurgbe0kNdz-QaYWnJoUqJ3Rd9XnYOvAAPkmwNMEu1V5puaqqMMr9UWgXWj1F97ZkpIWO9UefNdXwQwIUJm2fgBsG2cCkTM-onxmHibeo2VbDq2TYBvuL4cCqtHOfzAgKetU5u3zeqt5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68804" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68803">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2AyeLe544e8UO1gPyJMSzKzxH489Ek0-cTfujTGgCF-a7friixTluxVS9s8i7U0aLXhLXavWr4s8pSzqDN7ahGXOfc2oaCo3QNQW-Sgn3G65Qd30LKIEYg-OtK1FmNTVdXE--uvFUXmuQPVbAP5HGfqMzY8ncy74yGu5KvvZm-DrDT1VBfAmmq8o4h9spdjEDnl7d8FL4NbzNPt9Wyq8-ZOWygPobBLQrBOUnjvbbfuKFwASIp1z7LrVgcmpLAPGB6RSzruVWgV60YjGKIj_aqOMsglatG9L8cZ2ACukaFdLG_nfBjo9COgRW3WiitzTp045MH1QJXO2KWQz1ZhLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه
حتی اگه نزدیک تهران یا داخل خود تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68803" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68802">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=h2KNH_JjEZJNQpl4cQzL2shpldqPIDQA7P9jJTUXMn3JM0rpUgAoABHPRup9BZ-Ku8yJPgQ-3J74te1ipvlEyjHg8bhJULo9kZvw8tgSbEUJb3axvsqIPlCy1on9bcE_hXHt4Ks5NPyQ3tSt_KzLyZGsRi8ydtGNrBdA03umCrursOfrFBQ9u9GYlJgjusxXcSj4fvbV_TZkKcPey5Xp65AYIw0NJzoOGVUmuj3lqn4h-_dsdhxcgMUA9IuspE1SC26cnI2DEO6qzrdebMbGkxkKud_UM1VudYuDI4iq0iYt8kzaTPm3OITuaQrQQCM0FL7G39HPJt1zbMYkFySxiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=h2KNH_JjEZJNQpl4cQzL2shpldqPIDQA7P9jJTUXMn3JM0rpUgAoABHPRup9BZ-Ku8yJPgQ-3J74te1ipvlEyjHg8bhJULo9kZvw8tgSbEUJb3axvsqIPlCy1on9bcE_hXHt4Ks5NPyQ3tSt_KzLyZGsRi8ydtGNrBdA03umCrursOfrFBQ9u9GYlJgjusxXcSj4fvbV_TZkKcPey5Xp65AYIw0NJzoOGVUmuj3lqn4h-_dsdhxcgMUA9IuspE1SC26cnI2DEO6qzrdebMbGkxkKud_UM1VudYuDI4iq0iYt8kzaTPm3OITuaQrQQCM0FL7G39HPJt1zbMYkFySxiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مقایسه جمعیت ۷۲ هزار نفری در کنسرت فردی مرکوری در ومبلی لندن (تیر 1364)
و جمعیت مراسم نماز و تشییع علی خامنه‌ای در مصلی تهران (تیر 1405)
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68802" target="_blank">📅 16:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68801">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⏸
ویدیو وایرال شده از گریه های یک دختره بخاطر مردن سگش
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68801" target="_blank">📅 16:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68800">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
🇮🇷
سپاه پاسداران:
«اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت»
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68800" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68799">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA9fTZnfrRIy6zQEI5d8EvogRKgisoNXxOcCITxoAtst_47ZOGfMC2rKqVoSmpP-su9ORZDdnJqhGuQcdOXPGtHjpYk5rhC7uIWiHr6fJf-sJaa2SmwBvmBvQC-YLjKsHWT41laqDjeCTfM7TOoVh-v-CZuwMEFJQVfz1Ymssnj2WQd-RWhHkPmoE0s0nEZUSMK0SSSB-xVOk-9lcy9n6gLRiLsvu4x4AJpstYXtWAjvuvqvUqf5IYvZBSvW9Yhg4PxpJUJXo1BhSh3oD2bhPB4A8_TyPBEGQvp99YsgSj4a34CMm4lpyWi13cx4Z7zadrRi4oyrsak-VtYecbHQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آژیر خطر در عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68799" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68798">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران به بحرین و عربستان سعودی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68798" target="_blank">📅 15:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68797">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=L5zgsxvHHIkUlH8yBUQENX0z8_zv4vUUqaTcAU6D7DGwt4vhbjUO5Ybvai34zSN7HgpxD0g8Jzok_4-9QPmyogKCeyjHCKjtKmhNvFbd4mZhYZT2wxh8wxs53qPywitMbaz0bw8wADB3S26oOP1S_2YAQ4Up9vIAUSnVLH0LTMuNGvDat1Y-0t2QaEqH4HWzyUqAIAvHaBUgXBTAhsrsYpof_XLLPKxTnm1UbYNkMvTVD7F8LHdtLXiI2cpTdTN8cDj5cgyCBGjAXHCN-C-T9RPDc1x7a_dsUPDCyJGBy5m5ebov_VAj7C6LhrU4irSqCVAHVxjbb3-klaSK1HxlzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=L5zgsxvHHIkUlH8yBUQENX0z8_zv4vUUqaTcAU6D7DGwt4vhbjUO5Ybvai34zSN7HgpxD0g8Jzok_4-9QPmyogKCeyjHCKjtKmhNvFbd4mZhYZT2wxh8wxs53qPywitMbaz0bw8wADB3S26oOP1S_2YAQ4Up9vIAUSnVLH0LTMuNGvDat1Y-0t2QaEqH4HWzyUqAIAvHaBUgXBTAhsrsYpof_XLLPKxTnm1UbYNkMvTVD7F8LHdtLXiI2cpTdTN8cDj5cgyCBGjAXHCN-C-T9RPDc1x7a_dsUPDCyJGBy5m5ebov_VAj7C6LhrU4irSqCVAHVxjbb3-klaSK1HxlzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی:
هم‌وطنای عزیزم، مردم بزرگ و شجاع ایران،
با توجه به اینکه تنش‌ها داره بیشتر می‌شه و احتمال داره حمله‌ها، مخصوصاً تو جنوب کشور، گسترده‌تر بشه، می‌خوام چند دقیقه باهاتون حرف بزنم؛ به‌خصوص با مردم عزیز سیستان‌ و بلوچستان، هرمزگان، بوشهر، خوزستان و همه کسایی که کنار خلیج فارس و دریای مکران زندگی می‌کنن.
🇮🇷
جنگ و بحرانی که الان کشورمون گرفتارش شده، از نگاه من یه مقصر بیشتر نداره؛ جمهوری اسلامی.
ولی جنگ واقعی، یعنی جنگ جمهوری اسلامی علیه مردم ایران، از 47 سال پیش شروع شده و هنوز هم ادامه داره.
همه مردم ایران یه جورایی از این حکومت آسیب دیدن. نذاریم کسی طوری حرف بزنه که انگار جنوب ایران تازه وارد جنگ شده.
جنوب ایران از همون روزی وارد جنگ شد که بچه‌های بلوچ به خاطر نبود آب آشامیدنی و امکانات اولیه، قربانی گاندوها شدن؛ از همون روزی که جوون‌های سیستان و بلوچستان، سرزمین رستم، مجبور شدن برای یه لقمه نون سوخت‌بری کنن؛ از همون روزی که هرمزگان و بندرعباس، با اینکه بزرگ‌ترین بندر ایرانن، تو فقر و محرومیت رها شدن؛ از همون روزی که بوشهر با اون همه منابع گاز، و خوزستان که قلب صنعت نفت ایرانه، خودشون از ثروتی که تولید می‌کنن سهمی نبردن.
👑
اما ایران آزاد یه کشور کاملاً متفاوت خواهد بود.
با روی کار اومدن یه دولت ملی، کاربلد و توسعه‌محور، سیستان و بلوچستان می‌تونه با تکیه به موقعیت راهبردیش، جوون‌های توانمندش و دسترسی به آب‌های آزاد، به یکی از مهم‌ترین موتورهای رشد و پیشرفت ایران تبدیل بشه.
چابهار هم می‌تونه دوباره به قلب تجارت ایران و دروازه اتصال به اقیانوس هند، آسیای مرکزی و بازارهای جهانی تبدیل بشه؛ با احیای همون برنامه‌ای که قبل از انقلاب 57 قرار بود اجرا بشه.
هرمزگان، بوشهر، خوزستان و جزایر خلیج فارس هم با توسعه تجارت، گردشگری، صنعت و جذب سرمایه‌گذاری، می‌تونن به ثروتمندترین و پیشرفته‌ترین مناطق ایران تبدیل بشن.
✊
هم‌وطنای عزیز،
🇮🇷
این حکومت نه برای مردم پناهگاه درست کرده و نه حتی توان دفاع درست از آسمون کشور رو داره. در حالی که خودشون تو پناهگاه‌های زیرزمینی قایم شدن، از مدرسه‌ها، بیمارستان‌ها و مراکز غیرنظامی استفاده نظامی می‌کنن و مردم ایران، حتی سربازای وظیفه، رو به سپر انسانی تبدیل کردن.
توی جنگی که جمهوری اسلامی به کشور تحمیل کرده، اولین و مهم‌ترین وظیفه شما اینه که مراقب جون، امنیت و سلامت خودتون و خانواده‌هاتون باشید. چون شما سرمایه واقعی ایران و نیروهای اصلی برای پس گرفتن کشور هستید.
دفتر ارتباطات و رسانه من هم به‌زودی توصیه‌ها و راهنمایی‌های لازم رو منتشر می‌کنه تا مردم بتونن امنیت خودشون رو بیشتر حفظ کنن.
آماده بودن و ادامه دادن این مسیر، یه مسئولیت همیشگیه. هرچقدر مردم قوی‌تر باشن و جمهوری اسلامی ضعیف‌تر، رسیدن به پیروزی نهایی سریع‌تر و با هزینه کمتری انجام می‌شه.
👑
پاینده ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68797" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68796">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=s0aZ040AxHN-vsRQkvQndZfc_vEHSqVgp3TYr3Ci9eo-mgN_xNXyw7UHcUEOJs6zfGLcoNU8dym0ret2Nm2augQMBr2Xs1NMeBqNuGoK669Qdx9SLATrVrO29_f0RjiAl9pEZn6eLZEHUVRUd0sea8ni7zUH5iZ-t66wq9nujFQa5vCaL70LR4P7GNroDgbUdg0SBVX5qBL_FxO8SMNkOVhi4W7hUA6huAcqBQy2HvEscWkLlQ8F41g_gqqabxvEl3DVY6TyCAYwY9f-KvhrD9TifxPIherIVcazi4YN2peeq3eLeSpxhHxO1HFKHQTyZioxpcg20pgPAZj4QHsUyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=s0aZ040AxHN-vsRQkvQndZfc_vEHSqVgp3TYr3Ci9eo-mgN_xNXyw7UHcUEOJs6zfGLcoNU8dym0ret2Nm2augQMBr2Xs1NMeBqNuGoK669Qdx9SLATrVrO29_f0RjiAl9pEZn6eLZEHUVRUd0sea8ni7zUH5iZ-t66wq9nujFQa5vCaL70LR4P7GNroDgbUdg0SBVX5qBL_FxO8SMNkOVhi4W7hUA6huAcqBQy2HvEscWkLlQ8F41g_gqqabxvEl3DVY6TyCAYwY9f-KvhrD9TifxPIherIVcazi4YN2peeq3eLeSpxhHxO1HFKHQTyZioxpcg20pgPAZj4QHsUyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تفاهم‌نامه هیچ حقی برای حمله ایران به کشتی‌های تجاری قائل نشده است
.
🎙
خبرنگار:
آیا این تفاهم‌نامه (MoU) ذاتاً دچار اشکال نیست؟ چون در بند ۵، به نوعی به ایران نقش و اختیار در تنگه هرمز را به رسمیت می‌شناسد.
🇺🇸
مارکو روبیو:
فکر نمی‌کنم متن تفاهم‌نامه چنین چیزی را بیان کند. این تفاهم‌نامه به ایران حق نمی‌دهد که پهپاد و موشک به سمت کشتی‌های تجاری شلیک کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68796" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=cvBORUI3DsdKjfK49NSP65NiZS_m0Qn9kXv4iy9vJT-Pszxr4y2GeNC6l_qgAR6nok83r3bnl3dJ1o6GCpFKmuwox90eDwvP9I9KcZkSea8UWvEHezl3jwVlzRPBf9x9F0O7GN_Nx478VHhxeWtd1Pg_rBKyC8oslyLpyoNdg6IWCxJwGFHYWHwp3glTiVWbEUhWVJc3c9TQkAS63jPl9-VuM8wBNZYmsHdOc720U8-rdUDXjoh03RLaJpT8PcqLze6MmMah80XqRcUwD8ZKleMydoBCGrt4BheMh9YaGYfoaUiVuuPw9yS4rMWmxiMUTXsZGEGF75KSFiddbqoFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=cvBORUI3DsdKjfK49NSP65NiZS_m0Qn9kXv4iy9vJT-Pszxr4y2GeNC6l_qgAR6nok83r3bnl3dJ1o6GCpFKmuwox90eDwvP9I9KcZkSea8UWvEHezl3jwVlzRPBf9x9F0O7GN_Nx478VHhxeWtd1Pg_rBKyC8oslyLpyoNdg6IWCxJwGFHYWHwp3glTiVWbEUhWVJc3c9TQkAS63jPl9-VuM8wBNZYmsHdOc720U8-rdUDXjoh03RLaJpT8PcqLze6MmMah80XqRcUwD8ZKleMydoBCGrt4BheMh9YaGYfoaUiVuuPw9yS4rMWmxiMUTXsZGEGF75KSFiddbqoFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مراد ویسی:
دیدم مردم به من گفتن عراقچی رو فالو کردی رفتم توییتر نگاه کنم ، دیدم نه تو توییتر ندارمش و رفتم تو اینستا دیدم اره عراقچی رو فالو دارم که احتمالا دستم خورده بود و انفالو کردم.
مرسی که بهم تذکر دادید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=el02LXYr7ChFa0DB6HWkUNjY89ybOhFOF7SJ30uyLRe8qHwaJJQPqa05uvMNKCYpWejxxncu2i8BWZt-Z8FMmEuP5HI_fS-8l4ZdBiEsjAxkw3g0nPF1rdAZrc3SMYwSbPKBypZvtwrs--eYPvFSmc3g2_U4yo9Qd060s4mupryt6efn5sAq3ozLpvUGAydU1aBz2BI1TSgGgUAEX_nmWSY1AY75M1F7xyaaBJpboXz-ObQ9WywWwSaE5yn4ASYUzUujDsDpzAFkaHNWzIr82HZymymJXzpPOh8jQoC5zaeUNILTkWm3VwE3Ue5Is0iSZjzjZLHmcU-AsiccvVG8uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=el02LXYr7ChFa0DB6HWkUNjY89ybOhFOF7SJ30uyLRe8qHwaJJQPqa05uvMNKCYpWejxxncu2i8BWZt-Z8FMmEuP5HI_fS-8l4ZdBiEsjAxkw3g0nPF1rdAZrc3SMYwSbPKBypZvtwrs--eYPvFSmc3g2_U4yo9Qd060s4mupryt6efn5sAq3ozLpvUGAydU1aBz2BI1TSgGgUAEX_nmWSY1AY75M1F7xyaaBJpboXz-ObQ9WywWwSaE5yn4ASYUzUujDsDpzAFkaHNWzIr82HZymymJXzpPOh8jQoC5zaeUNILTkWm3VwE3Ue5Is0iSZjzjZLHmcU-AsiccvVG8uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🚀
حملات شدید پهبادی اوکراین به روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=k_JrpBoWuE89jyZfbP46ww-PUefdMCsS45skWz1NcUASOAIIWcP2fXFDn4ZNSPn5RM_xIW9q2QBMxZLzEdwvqWO9e7NNHA9QAkAJFxJZQT1C6yr-dKnA5B39yLhmKc2Q-Q7EdHiXTPy2wgoOL1QmdYikr4MkSwl6ZlPSDZ74U21Js-Xze0Ib92yEtyTUavkuKPW3Fuu834d58ecqj9qvd3DN3MHZDyU2JcTRwuumT8xOipnJ_VY3NHqej_l52xjNmP31LzzrtcuhWL-d5nVYrCzPN4q8q_PhKkcWLOsybkVD-h9GQStGd6r-yIG25fPY8--KY_1aKfBnG5mMCVOSfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=k_JrpBoWuE89jyZfbP46ww-PUefdMCsS45skWz1NcUASOAIIWcP2fXFDn4ZNSPn5RM_xIW9q2QBMxZLzEdwvqWO9e7NNHA9QAkAJFxJZQT1C6yr-dKnA5B39yLhmKc2Q-Q7EdHiXTPy2wgoOL1QmdYikr4MkSwl6ZlPSDZ74U21Js-Xze0Ib92yEtyTUavkuKPW3Fuu834d58ecqj9qvd3DN3MHZDyU2JcTRwuumT8xOipnJ_VY3NHqej_l52xjNmP31LzzrtcuhWL-d5nVYrCzPN4q8q_PhKkcWLOsybkVD-h9GQStGd6r-yIG25fPY8--KY_1aKfBnG5mMCVOSfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی وزارت کشور :
عباس چرت میگه مشهد سقوط کرده بود، تو دی ماه من خودم مشهد بودم خبری نبود اون شب.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4cICyviAP2bfufFa0wRZ5Oxe085I1-Cp0E59GvQ3MmlyE-VCDzoSe2w9HE3ydkDZijTupn8sUWsF_39x-rCDnrR7lpTFvIMQWPsy9oplMxaAe6x1IoFiARsJ_AOkkIAsP3tdR-72DYZWn6m2uzQFGBlu-W8ZGId-OEnirnVLXj6a-WbDBESlv57FZ8lYWRxAtXmBE50dhdcRhxM0koTs_U2kZPVzQoz8YLdBCzPks2yhW5EesdrIKOnkhsc7IIfBs62BXdhPg-5UbMqN3evyNSGm8a4VehcuSa2NssuVQRHxx99S8mUwQRYmXOZNwy58q5tXozuskNUF-GqyhJe1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=AeKZavjZju6nnBuCVWCOsjR7szxAL3MM_F3gn946_Jq1DdPNjQ1hEEIgAIX-611hDszYmbclWUAM7ZpjYvUhSR3LUmIkx5ooMkLsOd-nls1xw_lbxfqGotEMEvLn2eXg9UpJG-gj6bjKbBf3RirfuNPqC3oVQoAtK7XRh99fB7kEARlMB3W2lJnnJlOi4c_Qi2WXjjWyN3R3vhbvX4eThbTOD9FVqW-WpgcU_PJlaT2U68LbSJ5SdW-o3nfW__yaSxryul74l0VHA0YIgJDcwjyxYqfWC2GNXju1si8FvAG5E-t9EFYp1DUyMq8B6v6Dl0TvFh80BLzA6UsW68Zx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=AeKZavjZju6nnBuCVWCOsjR7szxAL3MM_F3gn946_Jq1DdPNjQ1hEEIgAIX-611hDszYmbclWUAM7ZpjYvUhSR3LUmIkx5ooMkLsOd-nls1xw_lbxfqGotEMEvLn2eXg9UpJG-gj6bjKbBf3RirfuNPqC3oVQoAtK7XRh99fB7kEARlMB3W2lJnnJlOi4c_Qi2WXjjWyN3R3vhbvX4eThbTOD9FVqW-WpgcU_PJlaT2U68LbSJ5SdW-o3nfW__yaSxryul74l0VHA0YIgJDcwjyxYqfWC2GNXju1si8FvAG5E-t9EFYp1DUyMq8B6v6Dl0TvFh80BLzA6UsW68Zx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این ویدیو از اینکه نشونه آدم پولدار چیه، اخیرا خیلی وایرال شده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68784">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQBr-8INMLeAdWeYqsV9tQwKfdlnuN3F0EDdrUaq2BjyVDZFO1O5jTiND_0kjC8gwbQ49wIMw3DiN6I3V8TAMs_2PpJejK97fEOWu8Ry8A18Uq3cLwegrDZ--jCU51cm_I4vPtJcxgM6a_-Mnoq2FLx9t_a1cC3fj7hb-02lQjE7a11hkYit4J-Lxfpg5PqRGmBGYLD3m2r4d9g-X_k8uu1ck1QZ8l2qE4ozIykTBh_ia1KNswbIBzsAPKLhRMEP34COXrTp8wL-wA8O8Ybbr1v8IZvhAcK2aw3x3McfCcMPRo5gkEhO4Mjf0Zlm76x76vk0AhzCDB2WDVBaxoO0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
شلیک موشک از کرمانشاه به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68784" target="_blank">📅 11:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68783">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=vaoEJHLwX8-8XgNWXACEGk-BKEhI3RkR17KSgceQQ8a2_iUmepOVofUor_DN8TCf3hPsevV7XcElUEP5B3UtN_LYNzXnvZxZKt6AcOd8YNxhTzNQ4pA1KlbXEcKQB1k92Ks1eR9U-no1eSgFv_8UHyddpgPZmX_BD1D8CXboV0okdvgut_6ZlAeWkHZUGMqbasvTl6xMms6A7Nc0KGlnJoqU_O3urYI1D1sznflYZEZExXe6MEN0rQhbAQmBVu3IFT0yyR-PA7UhNLKlM7vdaL3mlUlyMweCOuOC5HZ3vN6y5m4jN7jiuVlF_hoaJqMq64p1b55iHjjMWju7Law95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=vaoEJHLwX8-8XgNWXACEGk-BKEhI3RkR17KSgceQQ8a2_iUmepOVofUor_DN8TCf3hPsevV7XcElUEP5B3UtN_LYNzXnvZxZKt6AcOd8YNxhTzNQ4pA1KlbXEcKQB1k92Ks1eR9U-no1eSgFv_8UHyddpgPZmX_BD1D8CXboV0okdvgut_6ZlAeWkHZUGMqbasvTl6xMms6A7Nc0KGlnJoqU_O3urYI1D1sznflYZEZExXe6MEN0rQhbAQmBVu3IFT0yyR-PA7UhNLKlM7vdaL3mlUlyMweCOuOC5HZ3vN6y5m4jN7jiuVlF_hoaJqMq64p1b55iHjjMWju7Law95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
‌علی‌اکبر رائفی‌پور، ازحامیان جمهوری اسلامی:
با شناختی که از سپاه دارم اگر نظام سقوط کند، سپاه پاسداران موشک‌های خود را بر سر شهرهایی خالی خواهد کرد که به کنترل طرف مقابل درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68783" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=s6rxXrp7e99C0yzj3vJ2TVzI27O0DAE9-dP0zJpRuAB84PWazFZcmyprNHYgfzR2OXRyt2TfRDh8oBLa4Rf4xAAu5VW4TuvaCrOoen9v7BxJnqgFNJrcKRNRK_XMU2fwC9VwF2N1RRQNSVj-ta7Vji3AlabhXBEDhC4Cuxh_w4_HEW8qXj-vRPEw8LfSd284nPiVAM6Xhh1UibaXbp3mYlkBd9qVYC_yns4h9PB3WmmTMlAtWHdXzhQ3xCPJP8tJa5cT0vhZUZZHbCu4hTMeolpcWzjdKQEfE7ideo4BEY7Xz9_tGSfAFM-w79WJIhfGSQYO5VJpbMPn8KejbdZGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=s6rxXrp7e99C0yzj3vJ2TVzI27O0DAE9-dP0zJpRuAB84PWazFZcmyprNHYgfzR2OXRyt2TfRDh8oBLa4Rf4xAAu5VW4TuvaCrOoen9v7BxJnqgFNJrcKRNRK_XMU2fwC9VwF2N1RRQNSVj-ta7Vji3AlabhXBEDhC4Cuxh_w4_HEW8qXj-vRPEw8LfSd284nPiVAM6Xhh1UibaXbp3mYlkBd9qVYC_yns4h9PB3WmmTMlAtWHdXzhQ3xCPJP8tJa5cT0vhZUZZHbCu4hTMeolpcWzjdKQEfE7ideo4BEY7Xz9_tGSfAFM-w79WJIhfGSQYO5VJpbMPn8KejbdZGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=DlnM5snit-suGpcSFFcqMpH75xay19NL-g7W7k12lAnw-Mu1X3BeGuEdbqgRoWAr-Qf1XDGscXGvisBdd3QCMmQQJIfNQUKGz3vrbe40_eFpb6fuArvwMaZOxYLiw_mMIT_IriOsiabgik2gh2kNM12CT6caXTd5JN2HQb8udQ5RtPhDDxoMDn8BOUrs0U58WT39In_LERClBmKtw-UzyR49cnZRDb4eVl0kdXbqTQ89rqZFLqTjd4id814jEisohle-nF8P3dbNs-3WmxwYQLbjiTJg7qz6HnKQHi9N8BFoIq-Ks0UzIwB7KCarXEIEq0prhc-naohTpLnULaPz4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=DlnM5snit-suGpcSFFcqMpH75xay19NL-g7W7k12lAnw-Mu1X3BeGuEdbqgRoWAr-Qf1XDGscXGvisBdd3QCMmQQJIfNQUKGz3vrbe40_eFpb6fuArvwMaZOxYLiw_mMIT_IriOsiabgik2gh2kNM12CT6caXTd5JN2HQb8udQ5RtPhDDxoMDn8BOUrs0U58WT39In_LERClBmKtw-UzyR49cnZRDb4eVl0kdXbqTQ89rqZFLqTjd4id814jEisohle-nF8P3dbNs-3WmxwYQLbjiTJg7qz6HnKQHi9N8BFoIq-Ks0UzIwB7KCarXEIEq0prhc-naohTpLnULaPz4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو روز قبل یه گونی آدم از مجری‌های صداوسیما ، اعضای پایداری و بعضی ورزشکارها در واکنش به کارزاری که راه افتاده بود، پا شدن رفتن جنوب که بگن ما از جنگ ترسی نداریم و این حرف‌ها؛
حالا کجا رفته باشن خوبه؟
بهمنشیر که تو نزدیکی کویته و 14 ساعت [1125 کیلومتر] با بندرعباس فاصله داره
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=d4CAkIJP8ekUGBnCC-OL54b9x2LVIWhOHssuETMUsAGHa9XrKWPtz1kBYFzwOmLtHJM9R5lW0bA7FgKHqCYdav1Hs2InfI4ym5PxpFJnS9ujPTj10Mi5dgPmNitk3YtiBDRGahPyuB9ZOQSxtp3wHsw8INStHXgUDL3CUo8Bwz52DupVm3WmzKmcr0yI0gOwDalVo_Oy2b8hq5H3QgtUbccPNXieTJUgJkMduHPcL3rL0XB6xbW0LhzEJyqri-d71WXte_7TIXvFH9LHNVZ-DZ3gyn54GS_wie4xYid2Ws8YuPjvu0TV2vWsCzo0kJ6h6TYZtx4mtSO_PWAqLCiuIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=d4CAkIJP8ekUGBnCC-OL54b9x2LVIWhOHssuETMUsAGHa9XrKWPtz1kBYFzwOmLtHJM9R5lW0bA7FgKHqCYdav1Hs2InfI4ym5PxpFJnS9ujPTj10Mi5dgPmNitk3YtiBDRGahPyuB9ZOQSxtp3wHsw8INStHXgUDL3CUo8Bwz52DupVm3WmzKmcr0yI0gOwDalVo_Oy2b8hq5H3QgtUbccPNXieTJUgJkMduHPcL3rL0XB6xbW0LhzEJyqri-d71WXte_7TIXvFH9LHNVZ-DZ3gyn54GS_wie4xYid2Ws8YuPjvu0TV2vWsCzo0kJ6h6TYZtx4mtSO_PWAqLCiuIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظه‌ای که عادل فردوسی‌پور تو لایو فوتبال 360 بغض و گریه کرد...
اپلیکیشن‌ و سایت فوتبال 360 به علت اینکه عادل و مهمون‌هاش از تیم ملی انتقاد کرده بودن، به درخواست قلعه نویی و باندش فیلتر و از دسترس خارج شده و مجبور شدن برنامه رو تو لایو اینستاگرام و یوتیوب اجرا کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=gKTSwBUgvMyVzPtvIXCbFqSc4x7bVhA5pj1hI-CrtAHqoiH15-SUIpNlRxBPUW7Psye7t9U-fPfayOL6EvVJllZkljKbim2iMXhzdW99BEFEf9pwz017Xvy-lud4HWHfY9qXzxIHa2PiHM8pZhwtCq7NK2hU9_aAS0Lf_f7KAbmIxRyeBNf3CN1n6AAY_NpAouam9kpo92oNBESxDovHM4Za7i9tA7IUPV-gm47_QLLiPoPS5jAvvjEct7SlCf3-v2f3jNoEYao3DF4ZqnvmT-ZaGJEI1FP29fQngbOmsz7oVMjctq2eZK2iYJWorZwtk9z_zpYzO-OoJDco6eE93Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=gKTSwBUgvMyVzPtvIXCbFqSc4x7bVhA5pj1hI-CrtAHqoiH15-SUIpNlRxBPUW7Psye7t9U-fPfayOL6EvVJllZkljKbim2iMXhzdW99BEFEf9pwz017Xvy-lud4HWHfY9qXzxIHa2PiHM8pZhwtCq7NK2hU9_aAS0Lf_f7KAbmIxRyeBNf3CN1n6AAY_NpAouam9kpo92oNBESxDovHM4Za7i9tA7IUPV-gm47_QLLiPoPS5jAvvjEct7SlCf3-v2f3jNoEYao3DF4ZqnvmT-ZaGJEI1FP29fQngbOmsz7oVMjctq2eZK2iYJWorZwtk9z_zpYzO-OoJDco6eE93Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
نظر مارکو روبیو درباره برجام (سپتامبر 2015)
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=s1i2486rldXBYi9Z6auiu3GiVOw8gux1ixo4Mbtq152bpxDxtNB80Zh9jksS3IXXIDhmMzWy940-41dkUgHSIWhQxUL8KZ_tbZxbxZXvBJSaiTpfsF62LAkb0JMUd7iFbL4cqjBs-1SJXRV0NTuxMsELNhDMS1J7aRrk4y397SXLc8l2Mo6x4dpb70661QhFulJs9DiSMcOMLvPvVfdB-zOsILydSNsEHhzyrmthRTGscnkeoHrhxzMpK7K7kITDDRnTI_avFB82aUBxy1664Gdu7eoS9UPpqnWH3DxHiODEv7mbb90gMMifOF1rYtsMmB4WNgw0Msl8B3Hum0JJJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=s1i2486rldXBYi9Z6auiu3GiVOw8gux1ixo4Mbtq152bpxDxtNB80Zh9jksS3IXXIDhmMzWy940-41dkUgHSIWhQxUL8KZ_tbZxbxZXvBJSaiTpfsF62LAkb0JMUd7iFbL4cqjBs-1SJXRV0NTuxMsELNhDMS1J7aRrk4y397SXLc8l2Mo6x4dpb70661QhFulJs9DiSMcOMLvPvVfdB-zOsILydSNsEHhzyrmthRTGscnkeoHrhxzMpK7K7kITDDRnTI_avFB82aUBxy1664Gdu7eoS9UPpqnWH3DxHiODEv7mbb90gMMifOF1rYtsMmB4WNgw0Msl8B3Hum0JJJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-d26kRs2sd4aVw1cyJ5az04axv2ZiCCB8QzD3ZgmEhEJq3ixc7hQWWEL_mYvnG09HvG5k0jjFwWPcIm8t5Cn2lpxvfgQCq_YGpMBfWGMLK6aG7pSMVRwYVc46T3zB4-6onMa-YAKPaNMmSnk6r_HDnISMqPyzVn7HY-DaIsiWLncdRipG4MRZqnKIIm7HkTFqt_adJCgO-ljmwIJBA-BvUQmnIKGBGDB1yMxFbzP7aSDx9DnlvIOng5Hp5HEHU4yoUKN6FmYR86Ipqj7oiOTQwQj7vgCCqte8EX-s5g0aBg5jCIzkAqGCJRWHNDoHYMnOovl0EfBY-voNt7X6EhsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
